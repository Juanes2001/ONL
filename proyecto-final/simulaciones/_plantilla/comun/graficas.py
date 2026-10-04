"""
graficas.py — estilo unico y exportacion PNG + PDF (CLAUDE.md §7).

Backend Agg siempre: las figuras se escriben a disco, nunca se muestran. Un
plt.show() interactivo bloquearia un barrido de horas hasta que alguien cierre
la ventana.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl

mpl.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

plt.show = lambda *a, **k: None

# Okabe-Ito: legible tambien en escala de grises y para daltonismo.
AZUL = "#0072B2"
BERMELLON = "#D55E00"
VERDE = "#009E73"
ROSA = "#CC79A7"
AMBAR = "#E69F00"
CIELO = "#56B4E9"

ESTILO = {
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "mathtext.fontset": "dejavuserif",
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "figure.dpi": 120,
    "savefig.dpi": 300,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "axes.axisbelow": True,
    "axes.spines.top": False,
    "axes.spines.right": False,
}


def aplicar_estilo() -> None:
    mpl.rcParams.update(ESTILO)


def guardar_fig(fig, nombre: str, directorio: Path) -> Path:
    """Escribe PNG y PDF vectorial con el mismo nombre determinista."""
    directorio = Path(directorio)
    directorio.mkdir(parents=True, exist_ok=True)
    png = directorio / f"{nombre}.png"
    fig.savefig(png, dpi=300, bbox_inches="tight")
    fig.savefig(directorio / f"{nombre}.pdf", bbox_inches="tight")
    plt.close(fig)
    return png
