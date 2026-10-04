"""
pruebas_sin_lumerical.py — controles de comun/dispersion.py y comun/no_lineal.py
contra soluciones analíticas. No abre Lumerical.

    "$WINPY" pruebas_sin_lumerical.py        (Python de Windows: tiene numpy/scipy)

1. β2 recuperado de un n_eff(λ) sintético: β2 = λ³/(2πc²)·d²n/dλ².
2. Solitón fundamental (N = 1): conserva |A|² tras 5 L_D (Agrawal, cap. 5).
3. SPM pura (β = 0): fase no lineal en el pico = γ·P0·L, con signo +.
4. Dispersión lineal de un gaussiano: T1/T0 = √(1 + (z/L_D)²) (Agrawal, cap. 3).
5. Conservación de energía sin pérdidas, con β3 y self-steepening.
"""
from __future__ import annotations

import sys

import numpy as np

sys.path.insert(0, __file__.rsplit("pruebas_sin_lumerical.py", 1)[0].rstrip("\\/") or ".")
from comun import dispersion, no_lineal  # noqa: E402

C = 299_792_458.0
fallos = []


def check(nombre, ok, detalle):
    print(f"{'OK   ' if ok else 'FALLA'} {nombre}: {detalle}", flush=True)
    if not ok:
        fallos.append(nombre)


# 1 ─ β2 de n_eff(λ) = n0 + a(λ−λ0) + c(λ−λ0)²
lam0 = 1.55e-6
lam = np.linspace(1.0e-6, 2.2e-6, 25)
a, c2 = -0.3e6, 0.05e12                       # 1/m, 1/m²
neff = 1.8 + a * (lam - lam0) + c2 * (lam - lam0) ** 2
b = dispersion.betas_en(lam, neff, lam0)
b2_teo = lam0 ** 3 / (2 * np.pi * C ** 2) * 2 * c2
ng_teo = 1.8 - lam0 * a
check("beta2 sintetico", abs(b["beta2"] / b2_teo - 1) < 1e-3,
      f"{b['beta2']*1e27:.3f} vs {b2_teo*1e27:.3f} ps2/km; ng {b['ng']:.5f} vs {ng_teo:.5f}")
check("signo D", dispersion.D_ps_nm_km(lam0, -1e-26) > 0, "beta2 < 0 -> D > 0 (anomala)")

# 2 ─ solitón fundamental
beta2, gamma, t0 = -20e-27, 1.0, 100e-15
p0 = abs(beta2) / (gamma * t0 ** 2)
n = 2 ** 12
T = (np.arange(n) - n // 2) * (20e-12 / n)
A0 = np.sqrt(p0) / np.cosh(T / t0)
LD = t0 ** 2 / abs(beta2)
r = no_lineal.gnlse(A0, T[1] - T[0], {2: beta2}, gamma, lam0, 5 * LD, 0.0, 2000, 5,
                    self_steepening=False)
err = np.max(np.abs(np.abs(r["A_zt"][-1]) ** 2 - np.abs(A0) ** 2)) / p0
check("soliton N=1", err < 1e-2, f"error max de |A|^2 tras 5 L_D = {err:.2e}")

# 3 ─ SPM pura
L = 1e-2
r = no_lineal.gnlse(A0, T[1] - T[0], {}, gamma, lam0, L, 0.0, 500, 2, self_steepening=False)
fase = np.angle(r["A_zt"][-1][n // 2] / A0[n // 2])
check("SPM fase", abs(fase - gamma * p0 * L) < 1e-6, f"{fase:.6f} vs gamma*P0*L = {gamma*p0*L:.6f} rad")

# 4 ─ dispersión lineal de un gaussiano
G0 = np.exp(-T ** 2 / (2 * t0 ** 2))
r = no_lineal.gnlse(G0, T[1] - T[0], {2: 20e-27}, 0.0, lam0, 3 * LD, 0.0, 200, 2)
I = np.abs(r["A_zt"][-1]) ** 2
t_rms = np.sqrt(np.sum(T ** 2 * I) / np.sum(I))
t_rms0 = np.sqrt(np.sum(T ** 2 * G0 ** 2) / np.sum(G0 ** 2))
check("gauss lineal", abs(t_rms / t_rms0 - np.sqrt(1 + 9)) < 1e-3,
      f"T1/T0 = {t_rms/t_rms0:.5f} vs {np.sqrt(10):.5f}")

# 5 ─ energía con β3 y self-steepening (sin pérdidas)
r = no_lineal.gnlse(np.sqrt(3) * A0 * 2, T[1] - T[0], {2: beta2, 3: 0.1e-39}, gamma, lam0,
                    2 * LD, 0.0, 3000, 2)
E0 = np.sum(np.abs(r["A_zt"][0]) ** 2)
E1 = np.sum(np.abs(r["A_zt"][-1]) ** 2)
check("energia", abs(E1 / E0 - 1) < 2e-3, f"E1/E0 = {E1/E0:.6f} (el self-steepening conserva fotones, no energia: ~1e-3)")

print("\nTODO OK" if not fallos else f"\nFALLAS: {fallos}")
sys.exit(1 if fallos else 0)
