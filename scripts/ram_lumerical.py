#!/usr/bin/env python3
"""
ram_lumerical.py — ¿cabe en RAM una simulación de Lumerical junto a lo que ya corre?

Lumerical (v202) corre en WINDOWS, así que la RAM que manda es la de Windows, no
la de WSL. Además la VM de WSL (vmmemWSL) le quita memoria a Windows. Este script
se corre con el Python de Linux (sin dependencias) y consulta Windows con
powershell.exe. Tarda ~3–5 s y no toca ningún proceso.

Atribuye cada proceso de Lumerical a un proyecto:
    ONL                 -> ../ONL         (motor en %TEMP%\\onl_proyecto)
    fotonica-integrada  -> la tesis       (motor en %TEMP%\\plataforma_*, cascada_*, ...)
mirando la línea de comandos del propio proceso y la de sus procesos padre
(el python.exe que abrió la sesión lleva la ruta del script).

Uso
---
    python3 scripts/ram_lumerical.py                      estado actual
    python3 scripts/ram_lumerical.py --celdas 40e6        ¿cabe un FDTD 3D de 40 M celdas?
    python3 scripts/ram_lumerical.py --celdas 40e6 --freq 1000 --puntos-monitor 2e5 --monitores 4
    python3 scripts/ram_lumerical.py --necesita-gb 2.5    necesidad ya conocida
    python3 scripts/ram_lumerical.py --fde                ¿cabe una sesión MODE/FDE?
    python3 scripts/ram_lumerical.py --json               salida para otros scripts

Código de salida: 0 = CABE, 1 = AJUSTADO, 2 = NO CABE, 3 = no se pudo medir,
4 = LUMERICAL OCUPADO (hay una sesión o un motor de Lumerical vivo que no es de ONL).

REGLA (Juanes, 2026-10-04): ONL solo corre en el Lumerical local si está LIBRE.
La tesis tiene prioridad: cualquier proceso de Lumerical de fotonica-integrada o
sin atribuir vivo => OCUPADO, aunque la RAM alcance. ansysli_client.exe solo no
cuenta (es el cliente de licencias y puede quedar vivo un rato).

Calibración (fotonica-integrada, plataforma_v3_slot/ESTADO.md):
el motor FDTD 3D usó 1.2–1.6 GB con 30–37 M celdas -> ~40 B/celda.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys

# ── Modelo de consumo ─────────────────────────────────────────────────────
B_POR_CELDA_FDTD = 40.0       # medido en esta máquina (v202), motor fdtd-engine
FACTOR_SEGURIDAD = 1.3        # malla auto non-uniform, PML y picos al arrancar
SESION_GUI_GB = 0.35          # fdtd-solutions / mode-solutions -hide (medido ~0.3 GB privados)
FDE_GB = 1.0                  # sesión MODE + solver FDE 2D típico (orden de magnitud)
RESERVA_GB = 1.0              # lo que se deja libre para Windows y WSL
UMBRAL_AJUSTADO = 1.5         # disponible/necesidad por debajo de esto = AJUSTADO

PATRON_LUMERICAL = ("fdtd", "mode-solutions", "varfdtd", "eme-engine", "fde-engine",
                    "interconnect", "lumerical", "ansysli")

PS = r"""
$os = Get-CimInstance Win32_OperatingSystem
$av = (Get-Counter '\Memory\Available MBytes').CounterSamples[0].CookedValue
$procs = Get-CimInstance Win32_Process | Select-Object ProcessId,ParentProcessId,Name,
  @{n='priv';e={[double]$_.PrivatePageCount}},@{n='ws';e={[double]$_.WorkingSetSize}},CommandLine
[pscustomobject]@{
  total_kb = [double]$os.TotalVisibleMemorySize
  avail_mb = [double]$av
  procs    = $procs
} | ConvertTo-Json -Depth 3 -Compress
"""


def medir_windows() -> dict:
    r = subprocess.run(["powershell.exe", "-NoProfile", "-Command", PS],
                       capture_output=True, text=True, timeout=60)
    if r.returncode != 0 or not r.stdout.strip():
        raise RuntimeError(f"powershell.exe falló: {r.stderr.strip()[:300]}")
    return json.loads(r.stdout)


def proyecto_de(pid: int, por_pid: dict) -> str:
    """Sube por la cadena de padres buscando una pista del proyecto."""
    visto = set()
    while pid in por_pid and pid not in visto:
        visto.add(pid)
        p = por_pid[pid]
        cmd = (p.get("CommandLine") or "").lower().replace("/", "\\")
        if "onl_proyecto" in cmd or "\\proyectos\\onl\\" in cmd:
            return "ONL"
        if "fotonica-integrada" in cmd or any(
                k in cmd for k in ("\\plataforma_", "\\cascada_", "\\perdidas_",
                                   "\\pruebas_", "\\anillo_slot", "\\espectrometro")):
            return "fotonica-integrada"
        pid = p.get("ParentProcessId")
    return "sin atribuir"


def necesidad_gb(a) -> tuple[float, str]:
    if a.necesita_gb is not None:
        return a.necesita_gb, f"dada: {a.necesita_gb:.2f} GB"
    if a.celdas:
        motor = a.celdas * B_POR_CELDA_FDTD / 1e9
        # Monitores DFT: 6 componentes complejas (2 x float32) por punto y frecuencia.
        mon = a.monitores * a.puntos_monitor * a.freq * 6 * 8 / 1e9
        tot = (motor + mon) * FACTOR_SEGURIDAD + SESION_GUI_GB
        return tot, (f"FDTD 3D: {a.celdas/1e6:.1f} M celdas x {B_POR_CELDA_FDTD:.0f} B = "
                     f"{motor:.2f} GB + monitores {mon:.2f} GB, x{FACTOR_SEGURIDAD} "
                     f"+ sesión {SESION_GUI_GB} GB")
    if a.fde:
        return FDE_GB, f"sesión MODE/FDE ~{FDE_GB} GB"
    return 0.0, ""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--celdas", type=float, help="celdas de malla del FDTD 3D nuevo")
    ap.add_argument("--freq", type=float, default=0, help="puntos de frecuencia de los monitores DFT")
    ap.add_argument("--puntos-monitor", type=float, default=0, help="puntos espaciales por monitor DFT")
    ap.add_argument("--monitores", type=int, default=0, help="número de monitores DFT")
    ap.add_argument("--necesita-gb", type=float, help="necesidad conocida en GB")
    ap.add_argument("--fde", action="store_true", help="evaluar una sesión MODE/FDE")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    try:
        d = medir_windows()
    except Exception as e:  # noqa: BLE001
        print(f"No se pudo medir la RAM de Windows: {e}", file=sys.stderr)
        return 3

    procs = d["procs"] if isinstance(d["procs"], list) else [d["procs"]]
    por_pid = {p["ProcessId"]: p for p in procs}
    total_gb = d["total_kb"] / 1024 / 1024
    disp_gb = d["avail_mb"] / 1024

    lum, wsl_gb = [], 0.0
    for p in procs:
        n = (p.get("Name") or "").lower()
        if n.startswith("vmmem"):
            wsl_gb += (p.get("ws") or 0) / 1e9
        if any(k in n for k in PATRON_LUMERICAL):
            lum.append({"pid": p["ProcessId"], "nombre": p["Name"],
                        "privada_gb": (p.get("priv") or 0) / 1e9,
                        "proyecto": proyecto_de(p["ProcessId"], por_pid),
                        "cmd": (p.get("CommandLine") or "")[:160]})

    por_proy = {}
    for p in lum:
        por_proy[p["proyecto"]] = por_proy.get(p["proyecto"], 0.0) + p["privada_gb"]

    # Lumerical local LIBRE = ninguna sesion ni motor vivo que no sea de ONL.
    ajenos = [p for p in lum if p["proyecto"] != "ONL"
              and "ansysli" not in p["nombre"].lower()]
    libre = not ajenos

    nec, detalle = necesidad_gb(a)
    util = disp_gb - RESERVA_GB
    if not libre:
        veredicto, rc = "LUMERICAL OCUPADO", 4
    elif nec <= 0:
        veredicto, rc = "LIBRE", 0
    elif util >= nec * UMBRAL_AJUSTADO:
        veredicto, rc = "CABE", 0
    elif util >= nec:
        veredicto, rc = "AJUSTADO", 1
    else:
        veredicto, rc = "NO CABE", 2

    salida = {"total_gb": total_gb, "disponible_gb": disp_gb, "reserva_gb": RESERVA_GB,
              "utilizable_gb": util, "wsl_vm_gb": wsl_gb, "lumerical": lum,
              "lumerical_por_proyecto_gb": por_proy, "lumerical_libre": libre, "necesidad_gb": nec,
              "detalle_necesidad": detalle, "veredicto": veredicto}
    if a.json:
        print(json.dumps(salida, indent=2, ensure_ascii=False))
        return rc

    print(f"RAM Windows: total {total_gb:.1f} GB · disponible {disp_gb:.2f} GB "
          f"· reserva {RESERVA_GB:.1f} GB · utilizable {util:.2f} GB")
    print(f"VM de WSL (vmmemWSL, working set): {wsl_gb:.2f} GB")
    if lum:
        print("Procesos de Lumerical vivos:")
        for p in sorted(lum, key=lambda x: x["proyecto"]):
            print(f"  [{p['proyecto']:18s}] PID {p['pid']:>6} {p['nombre']:22s} "
                  f"{p['privada_gb']:.2f} GB  {p['cmd'][:80]}")
        for k, v in por_proy.items():
            print(f"  total {k}: {v:.2f} GB")
    else:
        print("Procesos de Lumerical vivos: ninguno")
    if nec > 0:
        print(f"Necesidad estimada: {nec:.2f} GB ({detalle})")
    if not libre:
        print("Lumerical local OCUPADO por: " + ", ".join(
            f"{p['nombre']} PID {p['pid']} [{p['proyecto']}]" for p in ajenos))
        print("ONL NO lanza: la tesis tiene prioridad. Esperar o preguntar a Juanes.")
    print(f"VEREDICTO: {veredicto}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
