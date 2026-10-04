"""
paso01_materiales.py — P1: modelos de material dispersivos y sus controles. Python puro.

Produce la tabla n(λ) de SiN, SiO2 y del analito (agua anclada a 1.33) en 1.0–2.2 µm,
la dispersión de MATERIAL de cada uno (β2_mat, D_mat) y la absorción del agua.

Controles (si alguno falla, el paso termina con error):
  * D_mat de la sílice en 1550 nm ≈ +21.9 ps/(nm·km) (valor de libro de la sílice
    fundida, Agrawal [A2]); tolerancia ±2.
  * Absorción del agua en 1550 nm ≈ 47.5 dB/cm (la que usa la tesis, de Segelstein);
    tolerancia ±2.
  * El ajuste polinómico del agua reproduce la tabla con residuo < 2e-3 en n.
"""
from __future__ import annotations

import numpy as np

import _ruta  # noqa: F401
from comun import almacen, entorno, graficas, materiales
from comun import plataforma as P

PASO = "paso01_materiales"
C = P.SPEED_OF_LIGHT
CONFIG = {"LAMBDA_MIN_UM": 1.0, "LAMBDA_MAX_UM": 2.2, "N_PUNTOS": 241,
          "ANCLAR_A_TESIS": True, "ANALITO_DISPERSIVO": True}


def d2n_dlam2(lam_um, n):
    return np.gradient(np.gradient(n, lam_um), lam_um)          # 1/µm²


def main():
    cfg = entorno.aplicar_perfil(CONFIG, {})
    almacen.abrir_paso(PASO, cfg)
    lam = np.linspace(cfg["LAMBDA_MIN_UM"], cfg["LAMBDA_MAX_UM"], cfg["N_PUNTOS"])
    tab = {k: np.array([materiales.indices(l, anclar=cfg["ANCLAR_A_TESIS"],
                                           analito_dispersivo=cfg["ANALITO_DISPERSIVO"])[k]
                        for l in lam]) for k in ("nucleo", "silice", "analito")}
    # β2_mat = λ³/(2πc²)·d²n/dλ²  y  D_mat = −(λ/c)·d²n/dλ²
    dmat = {}
    for k, n in tab.items():
        d2 = d2n_dlam2(lam, n) * 1e12                             # 1/m²
        lam_m = lam * 1e-6
        dmat[k] = {"beta2_ps2_km": (lam_m ** 3 / (2 * np.pi * C ** 2) * d2) * 1e27,
                   "D_ps_nm_km": (-(lam_m / C) * d2) * 1e12 / 1e9 * 1e3}
    i0 = int(np.argmin(np.abs(lam - 1.55)))
    D_sio2 = float(dmat["silice"]["D_ps_nm_km"][i0])
    a_agua = float(materiales.alpha_agua_dbcm(1.55))
    lt, nt, _k = materiales.tabla_agua()
    resid = float(np.max(np.abs(materiales.n_agua_suave(lt) - nt)))

    controles = {
        "D_mat_SiO2_1550": (D_sio2, abs(D_sio2 - 21.9) <= 2.0),
        "alpha_agua_1550_dBcm": (a_agua, abs(a_agua - 47.5) <= 2.0),
        "residuo_ajuste_agua": (resid, resid < 2e-3),
    }
    for k, (v, ok) in controles.items():
        print(f"[{PASO}] {k}: {v:.4g}  {'OK' if ok else 'FALLA'}", flush=True)
    print(f"[{PASO}] n(1550): SiN {tab['nucleo'][i0]:.5f}  SiO2 {tab['silice'][i0]:.5f}  "
          f"analito {tab['analito'][i0]:.5f}", flush=True)
    print(f"[{PASO}] D_mat(1550) [ps/nm/km]: SiN {dmat['nucleo']['D_ps_nm_km'][i0]:.1f}  "
          f"SiO2 {D_sio2:.1f}  agua {dmat['analito']['D_ps_nm_km'][i0]:.1f}", flush=True)

    graficas.aplicar_estilo()
    import matplotlib.pyplot as plt
    dfig = almacen.dir_figuras_paso(PASO)
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.8))
    for k, et in (("nucleo", "SiN (Luke 2015, anclado a 1.99)"),
                  ("silice", "SiO$_2$ (Malitson 1965, anclado a 1.4469)"),
                  ("analito", "analito: agua (Segelstein) anclada a 1.33")):
        ax[0].plot(lam, tab[k] - tab[k][i0], label=et)
        # Se recortan 3 puntos por lado: np.gradient pierde orden en los bordes.
        ax[1].plot(lam[3:-3], dmat[k]["D_ps_nm_km"][3:-3], label=et)
    ax[0].set_xlabel("Longitud de onda λ (µm)"); ax[0].set_ylabel("n(λ) − n(1550 nm)")
    ax[1].set_xlabel("Longitud de onda λ (µm)"); ax[1].set_ylabel("D$_{mat}$ (ps nm$^{-1}$ km$^{-1}$)")
    ax[1].axhline(0, color="k", lw=0.6); ax[0].legend(fontsize=8)
    graficas.guardar_fig(fig, "materiales_n_y_D", dfig)

    fig, ax = plt.subplots(figsize=(5, 3.6))
    ax.semilogy(lt, materiales.alpha_agua_dbcm(lt))
    ax.set_xlabel("Longitud de onda λ (µm)"); ax.set_ylabel("Absorción del agua (dB/cm)")
    graficas.guardar_fig(fig, "absorcion_agua", dfig)

    ok = all(v[1] for v in controles.values())
    almacen.escribir_contrato(PASO, {
        "controles": {k: {"valor": v[0], "ok": v[1]} for k, v in controles.items()},
        "valido": ok, "n_1550": {k: float(tab[k][i0]) for k in tab},
        "D_mat_1550_ps_nm_km": {k: float(dmat[k]["D_ps_nm_km"][i0]) for k in dmat}}, cfg)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
