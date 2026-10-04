"""
dispersion.py — dispersión a partir de n_eff(λ): n_g, β2, β3, β4, D, ZDW y D_int.

Convenciones (Agrawal [A2]):
  β(ω) = n_eff(ω)·ω/c,   β_k = d^kβ/dω^k,   n_g = c·β1
  D = −(2πc/λ²)·β2   [ps/(nm·km)]   (D > 0  ⇔  β2 < 0  ⇔  dispersión ANÓMALA)
  Anillo de longitud L: D1 = 2π/(β1·L) [rad/s], D2 = −(c/n_g)·D1²·β2.
  D_int(μ) = ω_μ − ω_0 − D1·μ ≈ D2μ²/2 (orden siguiente pendiente).

Las derivadas se toman de AJUSTES POLINÓMICOS de β(ω), no de diferencias
finitas: la segunda derivada amplifica el ruido del solver.
  - en λ0: polinomio de grado GRADO_LOCAL en (ω − ω0) sobre una ventana de ±VENTANA_LOCAL_THZ;
  - en toda la banda: ajuste local móvil de grado 3 sobre N_VECINOS puntos.
"""
from __future__ import annotations

import math

import numpy as np

C = 299_792_458.0

GRADO_LOCAL = 5
VENTANA_LOCAL_THZ = 40.0       # ±40 THz alrededor de 193.4 THz (≈ 1.40–1.73 µm)
N_VECINOS = 7


def beta_de_neff(lam_m, neff):
    """(ω, β) ordenados por ω creciente, sin NaN."""
    lam_m, neff = np.asarray(lam_m, float), np.asarray(neff, float)
    ok = np.isfinite(lam_m) & np.isfinite(neff)
    w = 2 * np.pi * C / lam_m[ok]
    b = neff[ok] * w / C
    o = np.argsort(w)
    return w[o], b[o]


def betas_en(lam_m, neff, lam0_m, grado=GRADO_LOCAL, ventana_thz=VENTANA_LOCAL_THZ):
    """β0..β4 en λ0 (unidades SI: s^k/m). None si no hay puntos suficientes."""
    w, b = beta_de_neff(lam_m, neff)
    w0 = 2 * np.pi * C / lam0_m
    sel = np.abs(w - w0) <= 2 * np.pi * ventana_thz * 1e12
    if sel.sum() < grado + 2:
        return None
    x = w[sel] - w0
    c = np.polyfit(x, b[sel], grado)            # c[-1-k] = β_k / k!
    bk = [c[-1 - k] * math.factorial(k) if k <= grado else np.nan for k in range(5)]
    return {"beta0": bk[0], "beta1": bk[1], "beta2": bk[2], "beta3": bk[3],
            "beta4": bk[4], "ng": C * bk[1]}


def beta2_banda(lam_m, neff, n_vecinos=N_VECINOS):
    """β2(λ) en cada punto por ajuste cúbico local en ω. Devuelve (λ, β2, n_g)."""
    w, b = beta_de_neff(lam_m, neff)
    n = len(w)
    b2 = np.full(n, np.nan)
    ng = np.full(n, np.nan)
    h = n_vecinos // 2
    for i in range(n):
        a, z = max(0, i - h), min(n, i + h + 1)
        if z - a < 5:
            continue
        x = w[a:z] - w[i]
        c = np.polyfit(x, b[a:z], 3)
        b2[i] = 2 * c[-3]
        ng[i] = C * c[-2]
    lam = 2 * np.pi * C / w
    o = np.argsort(lam)
    return lam[o], b2[o], ng[o]


def D_ps_nm_km(lam_m, beta2_s2_m):
    """Parámetro de dispersión D [ps/(nm·km)]."""
    D = -2 * np.pi * C / np.asarray(lam_m) ** 2 * np.asarray(beta2_s2_m)   # s/m²
    return D * 1e12 / 1e9 * 1e3


def ceros(lam_m, y):
    """λ donde y cambia de signo (interpolación lineal). Lista en nm."""
    lam_m, y = np.asarray(lam_m), np.asarray(y)
    ok = np.isfinite(y)
    lam_m, y = lam_m[ok], y[ok]
    out = []
    for i in range(len(y) - 1):
        if y[i] == 0 or y[i] * y[i + 1] < 0:
            t = y[i] / (y[i] - y[i + 1]) if y[i] != y[i + 1] else 0.0
            out.append(float((lam_m[i] + t * (lam_m[i + 1] - lam_m[i])) * 1e9))
    return out


def anillo(beta1, beta2, radio_um):
    """D1, D2 [rad/s] de un anillo de radio R con los β de su modo (curvado si es posible)."""
    L = 2 * np.pi * radio_um * 1e-6
    ng = C * beta1
    D1 = 2 * np.pi / (beta1 * L)
    D2 = -(C / ng) * D1 ** 2 * beta2
    return {"L_m": L, "FSR_Hz": D1 / (2 * np.pi), "D1": D1, "D2": D2,
            "regimen": "anomalo" if D2 > 0 else "normal"}
