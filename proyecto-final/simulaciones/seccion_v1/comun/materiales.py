"""
materiales.py — índices DISPERSIVOS de SiN, SiO2 y del analito (agua), y absorción del agua.

Por qué hace falta: β2 = (λ³/2πc²)·d²n_eff/dλ² depende de la dispersión de MATERIAL
además de la de guía. La tesis usa índices constantes (1.99 / 1.4469), y con eso
solo aparece la de guía. Aquí cada solve del FDE recibe n(λ) del material.

Modelos:
  SiN   Sellmeier de Luke et al., Opt. Lett. 40, 4823 (2015), DOI 10.1364/OL.40.004823
        (DOI verificado en Crossref; coeficientes tomados de refractiveindex.info,
        confirmarlos en el artículo).
  SiO2  Sellmeier de Malitson, JOSA 55, 1205 (1965), DOI 10.1364/JOSA.55.001205.
  Agua  Tabla n, k de Segelstein (1981) / Hale & Querry (1973), en
        datos/materiales/H2O_Segelstein_refractiveindexinfo.yml (refractiveindex.info, CC0).
        Su n(λ) tiene estructura cerca de las bandas de 1.45 y 1.94 µm. Se SUAVIZA con
        un polinomio para que la segunda derivada no herede ruido de la tabla.

ANCLAR_A_TESIS: se suma una constante a cada modelo para que n(1550) sea el índice
de la tesis (1.99, 1.4469, y n_analito para el líquido). Una constante no cambia
d²n/dλ², así que la dispersión de material se conserva entera, y los n_eff quedan
comparables con los de la tesis. El analito es la variable del refractómetro:
n_analito(λ) = n_analito + [n_agua(λ) − n_agua(1550)].
"""
from __future__ import annotations

import math
import re
from functools import lru_cache
from pathlib import Path

import numpy as np

from . import plataforma as P

RAIZ_REPO = Path(__file__).resolve().parents[4]          # .../ONL
TABLA_AGUA = RAIZ_REPO / "datos" / "materiales" / "H2O_Segelstein_refractiveindexinfo.yml"

LAMBDA_AGUA_FIT_UM = (0.95, 2.30)   # rango del ajuste polinómico del agua
GRADO_AGUA_FIT = 6


def n_sin_sellmeier(lam_um):
    l2 = np.asarray(lam_um, dtype=float) ** 2
    return np.sqrt(1 + 3.0249 * l2 / (l2 - 0.1353406 ** 2)
                   + 40314.0 * l2 / (l2 - 1239.842 ** 2))


def n_sio2_sellmeier(lam_um):
    l2 = np.asarray(lam_um, dtype=float) ** 2
    return np.sqrt(1 + 0.6961663 * l2 / (l2 - 0.0684043 ** 2)
                   + 0.4079426 * l2 / (l2 - 0.1162414 ** 2)
                   + 0.8974794 * l2 / (l2 - 9.896161 ** 2))


@lru_cache(maxsize=1)
def tabla_agua():
    """(λ [µm], n, k) de la tabla de Segelstein en el rango del ajuste."""
    filas = []
    for linea in TABLA_AGUA.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s+([0-9.Ee+-]+)\s+([0-9.Ee+-]+)\s+([0-9.Ee+-]+)\s*$", linea)
        if m:
            filas.append(tuple(float(g) for g in m.groups()))
    a = np.array(filas)
    sel = (a[:, 0] >= LAMBDA_AGUA_FIT_UM[0]) & (a[:, 0] <= LAMBDA_AGUA_FIT_UM[1])
    return a[sel, 0], a[sel, 1], a[sel, 2]


@lru_cache(maxsize=1)
def _coef_agua():
    lam, n, _k = tabla_agua()
    return np.polyfit(lam - 1.55, n, GRADO_AGUA_FIT)


def n_agua_suave(lam_um):
    """n del agua suavizado (polinomio en λ − 1.55 µm)."""
    return np.polyval(_coef_agua(), np.asarray(lam_um, dtype=float) - 1.55)


def alpha_agua_dbcm(lam_um):
    """Absorción de volumen del agua [dB/cm] = 4πk/λ, interpolando k de la tabla."""
    lam, _n, k = tabla_agua()
    kk = np.interp(np.asarray(lam_um, dtype=float), lam, k)
    alpha_1_cm = 4 * math.pi * kk / (np.asarray(lam_um, dtype=float) * 1e-4)
    return alpha_1_cm * 10.0 / math.log(10.0)


def indices(lam_um: float, n_analito: float = P.N_ANALITO_BASE,
            anclar: bool = True, analito_dispersivo: bool = True) -> dict:
    """Índices de las tres regiones a la longitud de onda `lam_um`."""
    lam0 = P.LAMBDA0_NM * 1e-3
    n_sin = float(n_sin_sellmeier(lam_um))
    n_sio2 = float(n_sio2_sellmeier(lam_um))
    if anclar:
        n_sin += P.N_SIN_1550 - float(n_sin_sellmeier(lam0))
        n_sio2 += P.N_SIO2_1550 - float(n_sio2_sellmeier(lam0))
    if analito_dispersivo:
        n_an = n_analito + float(n_agua_suave(lam_um) - n_agua_suave(lam0))
    else:
        n_an = n_analito
    return {"nucleo": n_sin, "silice": n_sio2, "analito": n_an}
