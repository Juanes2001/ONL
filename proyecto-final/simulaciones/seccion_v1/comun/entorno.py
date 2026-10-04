"""
entorno.py — apertura de sesiones Lumerical y seleccion de perfil de ejecucion.

Aisla lo unico que es especifico de la maquina: donde vive lumapi. En Windows
hay que registrar DOS directorios DLL antes de importar (bin para las librerias
del solver y api/python para interopapi.dll); manipular PATH ya no sirve en
Python 3.8+.

Nota de entorno medida en este equipo (2026-08-22): la PRIMERA apertura de una
sesion FDTD tras instalar puede tardar varios minutos mientras Lumerical
inicializa; las siguientes tardan ~5-10 s. No es un cuelgue.
"""
from __future__ import annotations

import os
import platform
import sys
import tempfile
from pathlib import Path

VERSION_LUMERICAL = os.environ.get("LUMERICAL_VERSION", "v202")

# Perfil de ejecucion:
#   "completo" -> resolucion de produccion (barridos largos, horas de FDTD 3D)
#   "rapido"   -> resolucion reducida para validar que TODOS los pasos corren
#                 de punta a punta. Los numeros NO son de diseno.
#
# Se busca primero en la linea de comandos y solo despues en el entorno: al
# lanzar el Python de Windows desde WSL, las variables de entorno de Linux NO
# llegan al proceso hijo salvo que esten declaradas en WSLENV, asi que un
# --perfil por argumento es el unico canal fiable en este montaje.
def _leer_perfil() -> str:
    for i, a in enumerate(sys.argv):
        if a == "--perfil" and i + 1 < len(sys.argv):
            return sys.argv[i + 1].strip().lower()
        if a.startswith("--perfil="):
            return a.split("=", 1)[1].strip().lower()
    return os.environ.get("PLATAFORMA_PERFIL", "completo").strip().lower()


PERFIL = _leer_perfil()


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  ESCENARIO de perdidas                                                   ║
# ╚══════════════════════════════════════════════════════════════════════════╝
# Un escenario es un juego de perdidas de propagacion distinto del nominal.
# Sirve para correr el protocolo entero bajo varios presupuestos de perdida
# (los que produce `perdidas_v1`) SIN pisar los resultados de la linea base.
#
# Con escenario activo, los contratos y las figuras van a
#     resultados_<escenario>/   y   figuras_<escenario>/
# mientras que los barridos HDF5 pesados siguen en `resultados/`, compartidos:
# la superficie Delta_n(gap) o el barrido de anchos son FISICA de la seccion
# transversal y no dependen de la perdida. Recalcularlos por escenario seria
# gastar horas de solver en reproducir la misma curva.
#
# Se lee de la linea de comandos ANTES que del entorno, por la misma razon que
# el perfil: al lanzar el Python de Windows desde WSL las variables de Linux no
# llegan al hijo salvo que esten en WSLENV.
def _leer_escenario() -> str:
    for i, a in enumerate(sys.argv):
        if a == "--escenario" and i + 1 < len(sys.argv):
            return sys.argv[i + 1].strip()
        if a.startswith("--escenario="):
            return a.split("=", 1)[1].strip()
    return os.environ.get("PLATAFORMA_ESCENARIO", "").strip()


ESCENARIO = _leer_escenario()


def hay_escenario() -> bool:
    return bool(ESCENARIO)


def sufijo_escenario() -> str:
    """'' para la linea base, '_<escenario>' si hay uno activo."""
    return f"_{ESCENARIO}" if ESCENARIO else ""


def es_rapido() -> bool:
    return PERFIL == "rapido"


def aplicar_perfil(cfg: dict, overrides_rapido: dict) -> dict:
    """Sobrescribe cfg con overrides_rapido si el perfil activo es 'rapido'.

    Se aplica SIEMPRE sobre una copia y deja constancia en cfg['PERFIL'], que
    acaba en la metadata del HDF5: un resultado de perfil rapido nunca se
    confunde luego con uno de produccion.
    """
    cfg = dict(cfg)
    cfg["PERFIL"] = PERFIL
    if es_rapido():
        for k, v in overrides_rapido.items():
            cfg[k] = v
    return cfg


def _rutas(version: str):
    if platform.system() == "Windows":
        raiz = rf"C:\Program Files\Lumerical\{version}"
        return raiz, rf"{raiz}\api\python", rf"{raiz}\bin"
    raiz = f"/opt/lumerical/{version}"
    return raiz, f"{raiz}/api/python", f"{raiz}/bin"


def importar_lumapi(version: str = VERSION_LUMERICAL):
    """Importa y devuelve el modulo lumapi, o lanza con un mensaje accionable."""
    ruta_env = os.environ.get("LUMAPI_PATH")
    if ruta_env:
        api = ruta_env
        binp = str(Path(ruta_env).parent.parent / "bin")
    else:
        _raiz, api, binp = _rutas(version)

    if not Path(api).is_dir():
        raise RuntimeError(
            f"No se encuentra la API de Lumerical en {api!r}.\n"
            f"Ajusta LUMERICAL_VERSION (actual {version!r}) o exporta LUMAPI_PATH."
        )

    if "lumapi" in sys.modules:
        del sys.modules["lumapi"]
    if api not in sys.path:
        sys.path.insert(0, api)

    if platform.system() == "Windows" and hasattr(os, "add_dll_directory"):
        # Los dos son necesarios: sin bin/ falla al cargar el solver, sin
        # api/python falla interopapi.dll con FileNotFoundError.
        for d in (binp, api):
            if Path(d).is_dir():
                os.add_dll_directory(str(d))

    import lumapi  # noqa: E402
    return lumapi


def abrir_mode(ocultar_gui: bool = False, version: str = VERSION_LUMERICAL):
    """Sesion MODE Solutions. El llamante DEBE cerrarla en un finally."""
    return importar_lumapi(version).MODE(hide=ocultar_gui)


def abrir_fdtd(ocultar_gui: bool = False, version: str = VERSION_LUMERICAL):
    """Sesion FDTD Solutions. El llamante DEBE cerrarla en un finally."""
    return importar_lumapi(version).FDTD(hide=ocultar_gui)


def ruta_motor_fdtd(version: str = VERSION_LUMERICAL) -> str:
    """Ejecutable del MOTOR de FDTD, para lanzarlo por subproceso.

    ⚠ 2026-09-11: `app.run()` desde la sesion oculta NO lanza el motor en esta
    maquina cuando la memoria disponible es escasa (dos veces seguidas: .fsp
    escrito, `ansysli_client` vivo, `fdtd-solutions` con la CPU congelada y
    ningun `fdtd-engine` en 25 min). La GUI muestra un aviso modal que con
    hide=True nadie acepta. El motor por linea de comandos sobre el mismo .fsp
    arranca en segundos y deja su log `<fsp>_p0.log` al lado. Es el mismo
    mecanismo que usan los scripts del cluster (ENGINE_GLOB).
    """
    raiz, _api, binp = _rutas(version)
    if platform.system() == "Windows":
        return rf"{binp}\fdtd-engine.exe"
    return f"{binp}/fdtd-engine"


def dir_trabajo_motor(sub: str = "onl_proyecto") -> str:
    r"""Directorio NATIVO del sistema donde el motor FDTD debe trabajar.

    El repositorio vive en WSL, asi que su ruta vista desde Windows es la UNC
    \\wsl.localhost\... Sobre ella el motor de FDTD se queda colgado ANTES de
    empezar a calcular: el proceso queda vivo con el tiempo de CPU congelado y
    no aparece ningun proceso fdtd-engine. Medido en este equipo: sobre la UNC
    no arranca nunca; con el proyecto guardado en C:\...\Temp la misma
    simulacion corre en 19 s.

    Por eso cada paso de FDTD hace cd() a este directorio y guarda ahi el .fsp
    antes de run(). Los .fsp quedan fuera del repositorio, que es ademas lo que
    manda CLAUDE.md §5 sobre archivos pesados.
    """
    d = Path(tempfile.gettempdir()) / sub
    d.mkdir(parents=True, exist_ok=True)
    return str(d)


def correr_motor_fdtd(ruta_fsp, hilos: int | None = None) -> float:
    """Corre el motor de FDTD por SUBPROCESO sobre un .fsp ya guardado.

    Sustituye a `app.run()`, que en esta maquina se cuelga con memoria escasa
    (ver `ruta_motor_fdtd`). El motor escribe los resultados dentro del .fsp y
    su avance en `<fsp>_p0.log`; despues hay que hacer `app.load(ruta_fsp)`.
    Un motor que vuelve en < 1 s no simulo nada: se trata como error.
    Copiado de fotonica-integrada (barrido_radios._correr_motor, 2026-10-04).
    """
    import subprocess
    import time
    ruta_fsp = Path(ruta_fsp)
    exe = ruta_motor_fdtd()
    hilos = int(hilos or max(1, (os.cpu_count() or 2) // 2))
    log = ruta_fsp.with_name(ruta_fsp.stem + "_p0.log")
    t0 = time.time()
    r = subprocess.run([exe, "-t", str(hilos), str(ruta_fsp)],
                       capture_output=True, text=True, cwd=str(ruta_fsp.parent))
    dt = time.time() - t0
    if r.returncode != 0 or dt < 1.0:
        cola = ""
        if log.exists():
            cola = "\n".join(log.read_text(errors="replace").splitlines()[-15:])
        raise RuntimeError(f"el motor de FDTD termino con codigo {r.returncode} "
                           f"en {dt:.1f} s ({exe} -t {hilos}). Log {log}:\n{cola}")
    return dt


def preparar_motor(app, nombre: str, sub: str = "onl_proyecto") -> Path:
    """cd() a un directorio NATIVO de Windows y save() del .fsp ANTES de correr.

    Obligatorio: sobre la UNC de WSL el motor de FDTD se cuelga sin arrancar.
    """
    d = Path(dir_trabajo_motor(sub))
    app.cd(str(d))
    ruta = d / f"{nombre}.fsp"
    app.save(str(ruta))
    return ruta
