"""
paso05_cifras_no_lineales.py — P5: ¿dónde conviene poner la no linealidad? Python puro.

Lee paso02 (y paso04 si existe) y calcula, por (cladding, pol, W):

  ANILLO  Q_int con α = Γ_abs,clad·α_agua(λ0) + α_extra(cladding) + α_bend(R),
          y el umbral de oscilación paramétrica P_th (LLE) en dos acoplos:
            all-pass crítico   Q_c = Q_int        (η = 1/2)
            add-drop simétrico Q_c1 = Q_c2 = Q_int (η = 1/3: el drop también extrae)
  SENSOR  (solo analito) S_bulk, FWHM = λ/Q_L y S/FWHM [1/RIU] (refractómetro de
          volumen; la detección superficial queda para más adelante).
  PULSO   L_D, L_NL, N y la escala ~L_D/N para pulsos sech² de T_FWHM y energía dados,
          comparadas con la longitud de pérdida 1/α.

Pérdidas extra (sin la absorción del agua, que se calcula):
  SiO2:    1.0 dB/cm (ANT reporta 1.2 dB/cm en strip de 0.75 µm a 1550; la tesis
           calcula 0.92–2.58 dB/cm para los espectrómetros).
  analito: 7.0 dB/cm (tesis, anillo strip cerrado en agua, FDTD 3D job 3247: curva +
           acopladores 7.0–8.7 dB/cm, además del agua).

Además elige el CANDIDATO para la GNLSE (paso06): si existe dispersión anómala en
1550 nm con cladding SiO2, la de mayor γ; si no, la normal de |D| mínimo (ruta de
supercontinuo en dispersión normal [D9]).
"""
from __future__ import annotations

import math

import numpy as np

import _ruta  # noqa: F401
from comun import almacen, entorno, materiales, no_lineal
from comun import plataforma as P

PASO = "paso05_cifras_no_lineales"

CONFIG = {
    "R_UM": [20.0, 50.0, 100.0],
    "ALPHA_EXTRA_DBCM": {"sio2": 1.0, "analito": 7.0},
    "T_FWHM_FS": [100.0, 200.0],
    "ENERGIA_PJ": [10.0, 100.0, 1000.0],
    "POL": ["te", "tm"],
}


def alpha_bend(c4, W, clad, R):
    if not c4:
        return 0.0
    f = c4["configuraciones"].get(f"W{W*1e3:.0f}_{clad}_R{R:.0f}")
    return f["alpha_bend_dbcm"] if f else 0.0


def main():
    cfg = entorno.aplicar_perfil(CONFIG, {})
    almacen.abrir_paso(PASO, cfg)
    c2 = almacen.leer_contrato("paso02_dispersion_h400")["configuraciones"]
    c4 = almacen.leer_contrato("paso04_curvatura", requerido=False)
    lam0 = P.LAMBDA0_NM * 1e-9
    a_agua = float(materiales.alpha_agua_dbcm(P.LAMBDA0_NM * 1e-3))

    anillo, pulsos = {}, {}
    for k, f in c2.items():
        if f["pol"] not in cfg["POL"] or "ng_1550" not in f or not np.isfinite(f["gamma_1550"]):
            continue
        clad, W = f["cladding"], f["W_um"]
        a_base = cfg["ALPHA_EXTRA_DBCM"][clad]
        a_abs = f["Gamma_abs_clad"] * a_agua if clad == "analito" else 0.0
        for R in cfg["R_UM"]:
            a_tot = a_base + a_abs + alpha_bend(c4, W, clad, R)
            qi = no_lineal.q_intrinseco(f["ng_1550"], a_tot, lam0)
            ap = no_lineal.umbral_opo_W(f["ng_1550"], f["aeff_um2_1550"], f["gamma_1550"],
                                        lam0, R, qi, qi)
            ad = no_lineal.umbral_opo_W(f["ng_1550"], f["aeff_um2_1550"], f["gamma_1550"],
                                        lam0, R, qi, qi, qi)
            fila = {**{x: f[x] for x in ("cladding", "pol", "W_um", "ng_1550", "gamma_1550",
                                         "aeff_um2_1550", "D_ps_nm_km_1550")},
                    "R_um": R, "alpha_total_dbcm": a_tot, "alpha_agua_modal_dbcm": a_abs,
                    "Q_int": qi, "P_th_allpass_W": ap["P_th_W"], "Q_L_allpass": ap["Q_L"],
                    "P_th_adddrop_W": ad["P_th_W"], "Q_L_adddrop": ad["Q_L"],
                    "FWHM_adddrop_pm": ad["FWHM_pm"],
                    "FSR_nm": lam0 ** 2 / (f["ng_1550"] * 2 * math.pi * R * 1e-6) * 1e9}
            if clad == "analito" and "S_bulk_nm_RIU" in f:
                fila["S_bulk_nm_RIU"] = f["S_bulk_nm_RIU"]
                fila["S_sobre_FWHM_1_RIU"] = f["S_bulk_nm_RIU"] / (ad["FWHM_pm"] * 1e-3)
            anillo[f"{k}_R{R:.0f}"] = fila
        for t in cfg["T_FWHM_FS"]:
            for e in cfg["ENERGIA_PJ"]:
                esc = no_lineal.escalas_pulso(f["beta2_ps2_km_1550"] * 1e-27, f["gamma_1550"],
                                              t * 1e-15, e * 1e-12, a_base + a_abs)
                pulsos[f"{k}_T{t:.0f}fs_E{e:.0f}pJ"] = {"cladding": clad, "pol": f["pol"],
                                                        "W_um": W, **esc}

    sio2 = [f for f in c2.values() if f["cladding"] == "sio2" and "ng_1550" in f
            and np.isfinite(f.get("beta2_ps2_km_1550", np.nan))]
    anom = [f for f in sio2 if f["beta2_ps2_km_1550"] < 0]
    if anom:
        cand = max(anom, key=lambda f: f["gamma_1550"]); motivo = "anomala, mayor gamma"
    else:
        cand = min(sio2, key=lambda f: abs(f["D_ps_nm_km_1550"])); motivo = "normal, |D| minimo"
    candidato = {"cladding": cand["cladding"], "pol": cand["pol"], "W_um": cand["W_um"],
                 "H_um": cand["H_um"], "motivo": motivo}

    print(f"[{PASO}] alpha_agua(1550) = {a_agua:.1f} dB/cm", flush=True)
    print(f"[{PASO}] ANILLO (mejor P_th add-drop por cladding):", flush=True)
    for clad in ("sio2", "analito"):
        fs = [f for f in anillo.values() if f["cladding"] == clad]
        if fs:
            b = min(fs, key=lambda f: f["P_th_adddrop_W"])
            print(f"  {clad:7s} {b['pol'].upper()} W={b['W_um']:.2f} R={b['R_um']:.0f}: "
                  f"Q_int {b['Q_int']:.3g}  P_th {b['P_th_adddrop_W']:.3g} W "
                  f"(all-pass {b['P_th_allpass_W']:.3g} W)", flush=True)
    sens = [f for f in anillo.values() if "S_sobre_FWHM_1_RIU" in f]
    if sens:
        b = max(sens, key=lambda f: f["S_sobre_FWHM_1_RIU"])
        print(f"[{PASO}] SENSOR: mejor S/FWHM {b['S_sobre_FWHM_1_RIU']:.0f} /RIU "
              f"({b['pol'].upper()} W={b['W_um']:.2f} R={b['R_um']:.0f}, S {b['S_bulk_nm_RIU']:.0f} nm/RIU)",
              flush=True)
    print(f"[{PASO}] candidato GNLSE: {candidato}", flush=True)
    almacen.escribir_contrato(PASO, {"anillo": anillo, "pulsos": pulsos,
                                     "candidato_gnlse": candidato,
                                     "alpha_agua_1550_dbcm": a_agua}, cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
