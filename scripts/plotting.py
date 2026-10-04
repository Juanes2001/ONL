"""Helpers de figuras compartidos por los estudios de simulación.

Convención del proyecto (CLAUDE.md §7): toda figura se exporta en PNG **y** en
PDF vectorial mediante `save_fig()`. El PNG es para revisar rápido y para las
presentaciones; el PDF entra en la tesis sin perder calidad al escalar.
"""
from __future__ import annotations

import os

import matplotlib
matplotlib.use("Agg")            # sin backend interactivo: los scripts corren headless
import matplotlib.pyplot as plt

# ── Paleta del proyecto ────────────────────────────────────────────────────
#   El color codifica el SOLVER y el trazo la GEOMETRÍA, para que la identidad
#   de cada curva no dependa solo del color (legible en impresión B/N y para
#   lectores con daltonismo).
COLOR_FDTD3D = "#2a78d6"
COLOR_VARFDTD = "#eb6834"
COLOR_DROP = "#1baf7a"
COLOR_ANOT = "#4c5762"
COLOR_GRID = "#dfe5ea"
COLOR_INK = "#12171c"
COLOR_MUTED = "#79848e"

DPI_PNG = 220


def apply_style() -> None:
    """Estilo común: tipografía consistente, rejilla recesiva, ejes limpios."""
    plt.rcParams.update({
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.titleweight": "semibold",
        "axes.labelsize": 10.5,
        "axes.edgecolor": "#c8d0d7",
        "axes.linewidth": 0.9,
        "axes.grid": True,
        "grid.color": COLOR_GRID,
        "grid.linewidth": 0.7,
        "xtick.color": COLOR_MUTED,
        "ytick.color": COLOR_MUTED,
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 9.5,
        "legend.frameon": False,
        "legend.fontsize": 9.5,
        "figure.autolayout": False,
    })


def save_fig(fig, out_dir: str, stem: str, *, dpi: int = DPI_PNG) -> tuple[str, str]:
    """Guarda `fig` como PNG y PDF vectorial. Devuelve ambas rutas.

    `stem` va sin extensión; el nombre debe ser determinista para que volver a
    correr el script sobrescriba la figura en vez de acumular variantes.
    """
    os.makedirs(out_dir, exist_ok=True)
    png = os.path.join(out_dir, stem + ".png")
    pdf = os.path.join(out_dir, stem + ".pdf")
    fig.savefig(png, dpi=dpi, bbox_inches="tight", facecolor=fig.get_facecolor())
    fig.savefig(pdf, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return png, pdf
