"""
no_lineal.py — cifras χ(3) derivadas de la sección, y la GNLSE para supercontinuo.

Fórmulas (referencias en proyecto-final/referencias-no-lineal-SiN.txt):

  Q intrínseco      Q_int = 2π n_g / (λ α_p),  α_p de POTENCIA [1/m]
  Anillo (LLE)      P_th = κ² n_g² V_eff / (8 η ω0 c n2_eff)          [A7]
                    κ = ω0/Q_L (tasa total), η = κ_ex,bus / κ, V_eff = A_eff·L,
                    n2_eff = γ λ A_eff / (2π) (el n2 promediado que da γ).
                    En acoplo crítico all-pass (η = 1/2) se reduce a
                    P_th = (π/2)·n_g²·A_eff·L / (n2 λ Q_L²). Escala como 1/Q².
                    ⚠ Se usa n_g en el lugar de "n". Es la aproximación habitual
                    para guías dispersivas; vale como orden de magnitud.
  Pulso (sech²)     T0 = T_FWHM/1.7627, P0 = E/(2 T0)
                    L_D = T0²/|β2|, L_NL = 1/(γ P0), N² = L_D/L_NL         [A2]
                    Escala de fisión (anómala) o de rotura de onda (normal): ~L_D/N  [A3]
  GNLSE             ∂A/∂z = −α/2·A + i Σ_k≥2 β_k/k! (i∂T)^k A
                            + iγ (1 + (i/ω0) ∂T)(|A|²A)                    [A2, A3]
                    Integrada con RK4IP (Hult, J. Lightwave Technol. 25, 3770 (2007)).
                    Convención de Fourier de Agrawal (e^{−iωT}): Ã = ifft(A), A = fft(Ã).
                    Sin Raman: en el SiN es débil frente a la sílice; se puede añadir después.
"""
from __future__ import annotations

import math

import numpy as np

C = 299_792_458.0
LN10 = math.log(10.0)


def dbcm_a_alpha_p(db_cm: float) -> float:
    """Pérdida de potencia [1/m] desde dB/cm."""
    return db_cm * LN10 / 10.0 * 100.0


def q_intrinseco(n_g: float, alpha_dbcm: float, lam_m: float) -> float:
    ap = dbcm_a_alpha_p(alpha_dbcm)
    return float("inf") if ap <= 0 else 2 * math.pi * n_g / (lam_m * ap)


def q_cargado(q_int: float, q_c1: float, q_c2: float | None = None) -> float:
    inv = 1 / q_int + 1 / q_c1 + (1 / q_c2 if q_c2 else 0.0)
    return 1 / inv


def umbral_opo_W(n_g, aeff_um2, gamma, lam_m, radio_um, q_int, q_c1, q_c2=None):
    """Umbral de oscilación paramétrica [W] en el bus de entrada (LLE)."""
    w0 = 2 * math.pi * C / lam_m
    q_l = q_cargado(q_int, q_c1, q_c2)
    kappa = w0 / q_l
    eta = (w0 / q_c1) / kappa
    aeff = aeff_um2 * 1e-12
    L = 2 * math.pi * radio_um * 1e-6
    n2_eff = gamma * lam_m * aeff / (2 * math.pi)
    p_th = kappa ** 2 * n_g ** 2 * aeff * L / (8 * eta * w0 * C * n2_eff)
    return {"P_th_W": p_th, "Q_L": q_l, "eta": eta, "n2_eff": n2_eff,
            "FWHM_pm": lam_m / q_l * 1e12}


def escalas_pulso(beta2, gamma, t_fwhm_s, energia_J, alpha_dbcm=0.0):
    t0 = t_fwhm_s / 1.7627
    p0 = energia_J / (2 * t0)
    ld = t0 ** 2 / abs(beta2) if beta2 else float("inf")
    lnl = 1 / (gamma * p0)
    N = math.sqrt(ld / lnl)
    ap = dbcm_a_alpha_p(alpha_dbcm)
    return {"T0_fs": t0 * 1e15, "P0_W": p0, "L_D_mm": ld * 1e3, "L_NL_mm": lnl * 1e3,
            "N": N, "L_caract_mm": ld / N * 1e3,
            "L_perdida_mm": (1 / ap * 1e3) if ap > 0 else float("inf"),
            "regimen": "anomalo" if beta2 < 0 else "normal"}


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  GNLSE — RK4IP                                                           ║
# ╚══════════════════════════════════════════════════════════════════════════╝
def operador_lineal(omega, betas: dict, alpha_p: float):
    """L(ω) = i Σ_k β_k ω^k / k! − α/2, con ω la frecuencia relativa a ω0."""
    D = np.zeros_like(omega, dtype=complex)
    for k, bk in betas.items():
        if k >= 2 and bk is not None and np.isfinite(bk):
            D += bk * omega ** k / math.factorial(k)
    return 1j * D - alpha_p / 2


def gnlse(A0, dt, betas: dict, gamma, lam0_m, L_m, alpha_p=0.0,
          n_pasos=2000, n_guardar=100, self_steepening=True):
    """Integra la GNLSE desde A0(T) [√W] a lo largo de L_m.

    Devuelve z [m], A(z, T) y Ã(z, ω) guardados en n_guardar planos, y ω relativa.
    """
    n = len(A0)
    omega = 2 * np.pi * np.fft.fftfreq(n, dt)
    w0 = 2 * np.pi * C / lam0_m
    Lop = operador_lineal(omega, betas, alpha_p)
    W = (1 + omega / w0) if self_steepening else np.ones_like(omega)
    h = L_m / n_pasos
    eL = np.exp(Lop * h / 2)

    def N(At):
        A = np.fft.fft(At)
        return 1j * gamma * W * np.fft.ifft(np.abs(A) ** 2 * A)

    At = np.fft.ifft(A0.astype(complex))
    cada = max(1, n_pasos // n_guardar)
    zs, Az, Atz = [0.0], [A0.astype(complex)], [At.copy()]
    for paso in range(1, n_pasos + 1):
        AI = eL * At
        k1 = eL * (h * N(At))
        k2 = h * N(AI + k1 / 2)
        k3 = h * N(AI + k2 / 2)
        k4 = h * N(eL * (AI + k3))
        At = eL * (AI + k1 / 6 + k2 / 3 + k3 / 3) + k4 / 6
        if paso % cada == 0 or paso == n_pasos:
            zs.append(paso * h)
            Atz.append(At.copy())
            Az.append(np.fft.fft(At))
    return {"z_m": np.array(zs), "A_zt": np.array(Az), "At_zw": np.array(Atz),
            "omega": omega}


def pulso_sech(n_puntos, ventana_s, t_fwhm_s, energia_J):
    T = (np.arange(n_puntos) - n_puntos // 2) * (ventana_s / n_puntos)
    t0 = t_fwhm_s / 1.7627
    p0 = energia_J / (2 * t0)
    return T, np.sqrt(p0) / np.cosh(T / t0)


def ancho_espectral(lam_nm, S_db, nivel_db=-30.0):
    """(λ_min, λ_max) donde el espectro supera nivel_db respecto a su máximo."""
    s = S_db - np.nanmax(S_db)
    idx = np.where(s >= nivel_db)[0]
    if idx.size == 0:
        return (np.nan, np.nan)
    return float(np.min(lam_nm[idx])), float(np.max(lam_nm[idx]))
