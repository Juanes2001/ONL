"""
paso06_gnlse.py — P6: primer espectro de supercontinuo con la GNLSE (RK4IP). Python puro.

Toma la sección CANDIDATA de paso05 (o la de CONFIG["CASO"]) con su β(ω) de paso02
(β2, β3, β4 en 1550 nm, expansión de Taylor) y su γ, y propaga un pulso sech² de
T_FWHM y energía dados a lo largo de L, con la pérdida del cladding.

Salidas: mapa espectral en z (dB), espectro final, forma temporal final y el ancho
a −30 dB. Los arrays van a un .npz en resultados/ (no se versionan).

⚠ Limitaciones de esta primera versión: dispersión por Taylor hasta β4, ajustada en
±40 THz alrededor de 1550 nm. Fuera de esa ventana el espectro es EXTRAPOLADO, y se
avisa si el espectro final se sale de ella. Sin Raman (débil en SiN), γ constante con
término de auto-empinamiento (self-steepening).
"""
from __future__ import annotations

import numpy as np

import _ruta  # noqa: F401
from comun import almacen, entorno, graficas, no_lineal
from comun import plataforma as P

PASO = "paso06_gnlse"
C = P.SPEED_OF_LIGHT

CONFIG = {
    "CASO": None,                 # p. ej. {"cladding": "sio2", "pol": "te", "W_um": 1.8, "H_um": 0.4}
    "T_FWHM_FS": 100.0,
    "ENERGIA_PJ": 100.0,
    "LONGITUD_MM": 10.0,
    "N_PUNTOS": 2 ** 14,
    "VENTANA_PS": 20.0,
    "N_PASOS": 4000,
    "N_GUARDAR": 100,
    "SELF_STEEPENING": True,
    "ALPHA_EXTRA_DBCM": {"sio2": 1.0, "analito": 7.0},
}
RAPIDO = {"N_PUNTOS": 2 ** 12, "N_PASOS": 800, "N_GUARDAR": 40}


def main():
    cfg = entorno.aplicar_perfil(CONFIG, RAPIDO)
    caso = cfg["CASO"] or almacen.leer_contrato("paso05_cifras_no_lineales")["candidato_gnlse"]
    cfg["CASO_RESUELTO"] = caso
    almacen.abrir_paso(PASO, cfg)
    c2 = almacen.leer_contrato("paso02_dispersion_h400")["configuraciones"]
    clave = f"H{caso['H_um']*1e3:.0f}_{caso['cladding']}_{caso['pol']}_W{caso['W_um']*1e3:.0f}"
    f = c2[clave]
    betas = {2: f["betas_SI"]["beta2"], 3: f["betas_SI"]["beta3"], 4: f["betas_SI"]["beta4"]}
    gamma = f["gamma_1550"]
    lam0 = P.LAMBDA0_NM * 1e-9
    a_db = cfg["ALPHA_EXTRA_DBCM"][caso["cladding"]]
    if caso["cladding"] == "analito":
        from comun import materiales
        a_db += f["Gamma_abs_clad"] * float(materiales.alpha_agua_dbcm(1.55))
    ap = no_lineal.dbcm_a_alpha_p(a_db)

    T, A0 = no_lineal.pulso_sech(cfg["N_PUNTOS"], cfg["VENTANA_PS"] * 1e-12,
                                 cfg["T_FWHM_FS"] * 1e-15, cfg["ENERGIA_PJ"] * 1e-12)
    dt = T[1] - T[0]
    esc = no_lineal.escalas_pulso(betas[2], gamma, cfg["T_FWHM_FS"] * 1e-15,
                                  cfg["ENERGIA_PJ"] * 1e-12, a_db)
    print(f"[{PASO}] caso {clave}: beta2 {betas[2]*1e27:.1f} ps2/km, gamma {gamma:.3f} /W/m, "
          f"alpha {a_db:.2f} dB/cm, N {esc['N']:.2f}, L_D {esc['L_D_mm']:.2f} mm, "
          f"L_NL {esc['L_NL_mm']:.3f} mm", flush=True)

    r = no_lineal.gnlse(A0, dt, betas, gamma, lam0, cfg["LONGITUD_MM"] * 1e-3, ap,
                        cfg["N_PASOS"], cfg["N_GUARDAR"], cfg["SELF_STEEPENING"])
    w0 = 2 * np.pi * C / lam0
    omega = np.fft.fftshift(r["omega"])
    lam_nm = 2 * np.pi * C / (w0 + omega) * 1e9
    S = np.abs(np.fft.fftshift(r["At_zw"], axes=1)) ** 2
    S_db = 10 * np.log10(S / S.max() + 1e-30)
    l_min, l_max = no_lineal.ancho_espectral(lam_nm, S_db[-1], -30.0)
    ventana_ok = (2 * np.pi * C / (w0 + 2 * np.pi * 40e12) * 1e9 <= l_min
                  and l_max <= 2 * np.pi * C / (w0 - 2 * np.pi * 40e12) * 1e9)
    print(f"[{PASO}] espectro final a -30 dB: {l_min:.0f}–{l_max:.0f} nm"
          f"{'' if ventana_ok else '  ⚠ se sale de la ventana del ajuste de beta (extrapolado)'}",
          flush=True)

    np.savez_compressed(almacen.dir_paso(PASO) / "gnlse.npz", z_m=r["z_m"], lam_nm=lam_nm,
                        S_db=S_db, T_s=T, A_final=r["A_zt"][-1])
    import matplotlib.pyplot as plt
    graficas.aplicar_estilo()
    o = np.argsort(lam_nm)
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.2), layout="constrained")
    m = ax[0].pcolormesh(lam_nm[o], r["z_m"] * 1e3, S_db[:, o], vmin=-50, vmax=0, shading="auto")
    fig.colorbar(m, ax=ax[0], label="Densidad espectral (dB)")
    ax[0].set_xlabel("Longitud de onda λ (nm)"); ax[0].set_ylabel("Propagación z (mm)")
    ax[0].set_xlim(lam_nm[o][S_db[-1, o] > -60].min(), lam_nm[o][S_db[-1, o] > -60].max())
    ax[1].plot(lam_nm[o], S_db[0, o], label="entrada")
    ax[1].plot(lam_nm[o], S_db[-1, o], label=f"z = {cfg['LONGITUD_MM']:.0f} mm")
    ax[1].set_ylim(-60, 2); ax[1].set_xlim(ax[0].get_xlim())
    ax[1].set_xlabel("Longitud de onda λ (nm)"); ax[1].set_ylabel("Densidad espectral (dB)")
    ax[1].legend()
    ax[2].plot(T * 1e12, np.abs(A0) ** 2, label="entrada")
    ax[2].plot(T * 1e12, np.abs(r["A_zt"][-1]) ** 2, label="salida")
    ax[2].set_xlim(-2, 2); ax[2].set_xlabel("Tiempo T (ps)"); ax[2].set_ylabel("Potencia (W)")
    ax[2].legend()
    fig.suptitle(f"{clave} · {cfg['T_FWHM_FS']:.0f} fs · {cfg['ENERGIA_PJ']:.0f} pJ")
    graficas.guardar_fig(fig, "gnlse_supercontinuo", almacen.dir_figuras_paso(PASO))
    almacen.escribir_contrato(PASO, {"caso": clave, "escalas": esc, "alpha_dbcm": a_db,
                                     "ancho_30dB_nm": [l_min, l_max],
                                     "dentro_de_ventana_beta": bool(ventana_ok)}, cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
