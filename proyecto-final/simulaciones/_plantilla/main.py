#!/usr/bin/env python3
"""
main.py — orquestador de un estudio (plantilla copiada de fotonica-integrada/plataforma_v2).

Lanza los pasos EN SUBPROCESOS INDEPENDIENTES. No es un detalle de
implementacion, es el mecanismo que hace real el desacople:

  * cada paso arranca con un interprete limpio, sin globals heredados. El
    protocolo anterior encadenaba los pasos por un dict `state` que cada modulo
    volcaba a sus globals con globals().update(state); bastaba que un paso
    dejara una variable a medias para que el siguiente leyera basura sin error.
  * cada paso abre y cierra SU sesion de Lumerical. Mezclar sesiones MODE y
    FDTD en un mismo proceso es una fuente conocida de bloqueos.
  * si un paso revienta, se lleva por delante su proceso y nada mas. Los
    contratos y los HDF5 de los demas siguen intactos en disco.

Uso
---
    python main.py                          todos los pasos, perfil completo
    python main.py --perfil rapido          validacion end-to-end reducida
    python main.py --solo paso04_radio_sensor_fdtd3d
    python main.py --desde paso06_acoplo_critico
    python main.py --listar
    python main.py --continuar              no se detiene ante un fallo

Perfiles
--------
  completo  resolucion de produccion. Los barridos en FDTD 3D son de HORAS.
  rapido    malla gruesa y pocos puntos. Sirve para comprobar que los diez
            pasos corren y producen sus resultados; los NUMEROS NO son de
            diseno y los contratos quedan marcados con perfil="rapido".
"""
from __future__ import annotations

import argparse
import os
import platform
import shutil
import subprocess
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
DIR_PASOS = RAIZ / "pasos"

# Lista ordenada de pasos del estudio: un archivo pasos/<nombre>.py por paso.
ORDEN = [
    # "paso01_dispersion_fde",
]

DESCRIPCION = {
    # "paso01_dispersion_fde": "FDE 2D · n_eff(lambda), n_g, beta2, A_eff",
}

# Pasos que abren una sesion de Lumerical (los demas son analiticos).
USA_LUMERICAL = set(ORDEN)


def _python_ejecutor():
    """Interprete con el que lanzar los pasos.

    Bajo WSL, Lumerical vive en Windows y lumapi solo se importa desde el
    Python de Windows. Se autodetecta uno con el stack cientifico instalado; se
    puede forzar con la variable de entorno PYTHON_LUMERICAL.
    """
    forzado = os.environ.get("PYTHON_LUMERICAL")
    if forzado:
        return forzado, True

    if platform.system() != "Linux" or "microsoft" not in platform.release().lower():
        return sys.executable, False

    candidatos = sorted(Path("/mnt/c/Users").glob(
        "*/AppData/Local/Programs/Python/Python3*/python.exe"))
    candidatos += sorted(Path("/mnt/c").glob("Python3*/python.exe"))
    for cand in candidatos:
        try:
            r = subprocess.run([str(cand), "-c", "import numpy, h5py, matplotlib, scipy"],
                               capture_output=True, timeout=90)
            if r.returncode == 0:
                return str(cand), True
        except Exception:
            continue
    return sys.executable, False


def _a_ruta_del_interprete(ruta: Path, es_windows: bool) -> str:
    if not es_windows:
        return str(ruta)
    if shutil.which("wslpath"):
        return subprocess.run(["wslpath", "-w", str(ruta)],
                              capture_output=True, text=True).stdout.strip()
    return str(ruta)


def correr_paso(nombre: str, perfil: str, exe: str, es_win: bool,
                escenario: str = "") -> int:
    guion = DIR_PASOS / f"{nombre}.py"
    if not guion.exists():
        print(f"!! no existe {guion}")
        return 127
    entorno_hijo = dict(os.environ)
    entorno_hijo["PLATAFORMA_PERFIL"] = perfil
    if escenario:
        entorno_hijo["PLATAFORMA_ESCENARIO"] = escenario
    entorno_hijo["PYTHONUNBUFFERED"] = "1"
    # Sin esto, el Python de Windows escribe la consola en cp1252 y
    # destroza los acentos y los simbolos de las tablas.
    entorno_hijo["PYTHONIOENCODING"] = "utf-8"
    # Los pasos hacen `import _ruta`, que vive junto a ellos.
    entorno_hijo["PYTHONPATH"] = os.pathsep.join(
        filter(None, [_a_ruta_del_interprete(DIR_PASOS, es_win),
                      entorno_hijo.get("PYTHONPATH", "")]))

    print(f"\n{'━'*100}\n▶ {nombre}   —   {DESCRIPCION.get(nombre,'')}\n{'━'*100}",
          flush=True)
    t0 = time.time()
    argv = [exe, _a_ruta_del_interprete(guion, es_win), "--perfil", perfil]
    if escenario:
        # Por argumento y NO solo por entorno: al lanzar el Python de Windows
        # desde WSL las variables de Linux no llegan al hijo (CLAUDE.md §5).
        argv += ["--escenario", escenario]
    r = subprocess.run(argv, env=entorno_hijo, cwd=str(RAIZ))
    dt = time.time() - t0
    print(f"\n{'✔' if r.returncode == 0 else '✘'} {nombre}  "
          f"({dt:.1f} s, codigo {r.returncode})", flush=True)
    return r.returncode


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--perfil", choices=["completo", "rapido"], default="completo")
    ap.add_argument("--escenario", default="",
                    help="escenario de perdidas; escribe en resultados_<esc>/ "
                         "y hereda de la linea base lo que no re-corre")
    ap.add_argument("--solo", help="un unico paso")
    ap.add_argument("--desde", help="empezar en este paso y seguir")
    ap.add_argument("--hasta", help="terminar en este paso")
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--continuar", action="store_true",
                    help="no detenerse cuando un paso falla")
    ap.add_argument("--sin-lumerical", action="store_true",
                    help="solo los pasos analiticos y de presentacion")
    args = ap.parse_args()

    if args.listar:
        print("Pasos del protocolo v2:\n")
        for i, p in enumerate(ORDEN, 1):
            marca = "L" if p in USA_LUMERICAL else " "
            print(f"  {i:2d}. [{marca}] {p:38s} {DESCRIPCION[p]}")
        print("\n  [L] = necesita una sesion de Lumerical")
        return 0

    pasos = ORDEN
    if args.solo:
        if args.solo not in ORDEN:
            print(f"paso desconocido: {args.solo}\nusa --listar")
            return 2
        pasos = [args.solo]
    else:
        if args.desde:
            pasos = pasos[ORDEN.index(args.desde):]
        if args.hasta:
            pasos = pasos[:pasos.index(args.hasta) + 1]
    if args.sin_lumerical:
        pasos = [p for p in pasos if p not in USA_LUMERICAL]

    exe, es_win = _python_ejecutor()
    print(f"protocolo v2  ·  perfil={args.perfil}  ·  {len(pasos)} paso(s)")
    print(f"interprete: {exe}{'  (Python de Windows, para lumapi)' if es_win else ''}")
    if args.perfil == "rapido":
        print("PERFIL RAPIDO: malla gruesa y pocos puntos. Validacion "
              "estructural, NO valores de diseno.")

    t0 = time.time()
    fallos = []
    for p in pasos:
        rc = correr_paso(p, args.perfil, exe, es_win, args.escenario)
        if rc != 0:
            fallos.append(p)
            if not args.continuar:
                print(f"\nDetenido en {p}. Corrige y relanza con "
                      f"--desde {p} (lo ya calculado sigue en cache).")
                break

    print(f"\n{'═'*100}")
    print(f"total {time.time()-t0:.1f} s  ·  "
          f"{len(pasos)-len(fallos)}/{len(pasos)} pasos completados")
    if fallos:
        print(f"fallaron: {', '.join(fallos)}")
    print("═" * 100)
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
