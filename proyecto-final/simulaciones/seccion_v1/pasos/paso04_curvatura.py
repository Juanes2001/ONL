"""
paso04_curvatura.py — P4: el anillo. Pérdida por curvatura, n_eff/n_g/β2 del modo
CURVADO, y D1, D2 del anillo para varios radios.

Para cada ancho finalista W, cladding {SiO2, analito} y λ ∈ 1520–1580 nm:
  * guía recta (ancla del modo, lección de la tesis: en un bend el TE de mayor
    n_eff no siempre es el TE0);
  * guía curvada con R ∈ R_UM, bordes PML.
Salidas por (W, cladding, R): n_eff y n_g en 1550, α_bend [dB/cm] = 4π·Im(n_eff)/λ,
β2 local, FSR, D1, D2 y el régimen del anillo.

Anchos finalistas: W_UM_FINALISTAS si se da; si no, se eligen del contrato de
paso02 (TE0): el de mayor γ en SiO2, el de |D| mínimo en SiO2 y el de mayor S_bulk
con analito.
⚠ El FDE curvado es una aproximación (modo estacionario de la guía curva). Para
valores absolutos de FSR y Q, el anillo cerrado en FDTD 3D (P6) es la referencia
(tesis: el arco de 90° predice el FSR del anillo a ≤ 12 pm).
"""
from __future__ import annotations

import numpy as np

import _ruta  # noqa: F401
from comun import almacen, dispersion, entorno, graficas, seccion
from comun import plataforma as P

PASO = "paso04_curvatura"

CONFIG = {
    "W_UM_FINALISTAS": None,          # p. ej. [1.0, 1.8, 2.6]; None = elegir de paso02
    "H_UM": P.ALTURA_NUCLEO_UM,
    "CLADDINGS": ["sio2", "analito"],
    "R_UM": [20.0, 30.0, 50.0, 80.0, 120.0],
    "LAMBDA_UM": [round(1.52 + 0.01 * k, 3) for k in range(7)],
    "N_MODOS": 16,
    "Y_MARGEN_UM": 3.0, "Z_ABAJO_UM": 3.0, "Z_ARRIBA_UM": 3.0,
    "MALLA_Y": 140, "MALLA_Z": 100, "MALLA_FINA_NM": 10.0, "MALLA_FINA_PAD_UM": 0.50,
    "PML_EN_BEND": True,
    "MATERIALES_DISPERSIVOS": True, "ANCLAR_A_TESIS": True, "ANALITO_DISPERSIVO": True,
    "OCULTAR_GUI": True,
}
RAPIDO = {"R_UM": [30.0, 80.0], "LAMBDA_UM": [1.53, 1.54, 1.55, 1.56, 1.57],
          "MALLA_Y": 80, "MALLA_Z": 60, "MALLA_FINA_NM": 20.0}

CAMPOS = ["neff_te", "neffi_te", "tefrac_te", "neff_tm", "neffi_tm"]


def finalistas(cfg):
    if cfg["W_UM_FINALISTAS"]:
        return list(cfg["W_UM_FINALISTAS"])
    c = almacen.leer_contrato("paso02_dispersion_h400")["configuraciones"]
    te = [f for f in c.values() if f["pol"] == "te" and "ng_1550" in f]
    sio2 = [f for f in te if f["cladding"] == "sio2"]
    an = [f for f in te if f["cladding"] == "analito" and "S_bulk_nm_RIU" in f]
    ws = {max(sio2, key=lambda f: f["gamma_1550"])["W_um"],
          min(sio2, key=lambda f: abs(f["D_ps_nm_km_1550"]))["W_um"]}
    if an:
        ws.add(max(an, key=lambda f: f["S_bulk_nm_RIU"])["W_um"])
    return sorted(ws)


def main():
    cfg = entorno.aplicar_perfil(CONFIG, RAPIDO)
    Ws = finalistas(cfg)
    cfg["W_UM_ELEGIDOS"] = Ws
    almacen.abrir_paso(PASO, cfg)
    H = cfg["H_UM"]
    radios = [0.0] + list(cfg["R_UM"])            # 0 = recta (ancla)
    lams = list(cfg["LAMBDA_UM"])
    nl = len(lams)
    print(f"[{PASO}] anchos {Ws}, {len(Ws)*len(cfg['CLADDINGS'])*len(radios)*nl} solves", flush=True)
    dirc = almacen.dir_cache(PASO)
    app = None
    rutas = {}
    try:
        for W in Ws:
            for clad in cfg["CLADDINGS"]:
                ruta = dirc / f"bend_W{W*1e3:.0f}_{clad}.h5"
                rutas[(W, clad)] = ruta
                almacen.init_h5(ruta, {**cfg, "W_ACTUAL": W, "CLAD_ACTUAL": clad},
                                {"R_um": radios, "lambda_um": lams}, CAMPOS, len(radios) * nl)
                for il, lam in enumerate(lams):
                    n_idx, n2c = seccion.indices_caso(lam, clad, cfg)
                    ancla = None
                    for ir, R in enumerate(radios):
                        i = ir * nl + il
                        if almacen.ya_calculado(ruta, i):
                            if ir == 0:
                                d = almacen.leer_resultados(ruta)
                                ancla = {"te": d["neff_te"][i], "tm": d["neff_tm"][i]}
                            continue
                        if app is None:
                            print(f"[{PASO}] abriendo sesion MODE (puede tardar)", flush=True)
                            app = entorno.abrir_mode(ocultar_gui=cfg["OCULTAR_GUI"])
                        r = seccion.resolver(app, cfg, W, H, lam, n_idx, n2c,
                                             radio_um=(R or None), neff_guess=ancla)
                        if ir == 0:
                            ancla = {p: r[f"neff_{p}"] for p in ("te", "tm")
                                     if np.isfinite(r[f"neff_{p}"])}
                        almacen.escribir_punto(ruta, i, {k: r.get(k, np.nan) for k in CAMPOS})
                        print(f"[{PASO}] W={W:.2f} {clad:7s} lam={lam:.3f} R={R:6.1f} "
                              f"neffTE {r['neff_te']:.6f} imag {r['neffi_te']:.2e}", flush=True)
    finally:
        if app is not None:
            try:
                app.close()
            except Exception:  # noqa: BLE001
                pass

    lam0_m = P.LAMBDA0_NM * 1e-9
    res = {}
    for (W, clad), ruta in rutas.items():
        d = almacen.leer_resultados(ruta)
        lam_m = d["eje_lambda_um"] * 1e-6
        il0 = int(np.argmin(np.abs(lam_m - lam0_m)))
        for ir, R in enumerate(d["eje_R_um"]):
            sl = slice(ir * nl, (ir + 1) * nl)
            neff = d["neff_te"][sl]
            b = dispersion.betas_en(lam_m, neff, lam0_m, grado=3, ventana_thz=6.0)
            ni = float(d["neffi_te"][ir * nl + il0])
            fila = {"W_um": float(W), "cladding": clad, "R_um": float(R),
                    "neff_1550": float(neff[il0]),
                    "alpha_bend_dbcm": float(4 * np.pi * abs(ni) / lam0_m * 10 / np.log(10) / 100)}
            if b:
                fila.update({"ng_1550": b["ng"], "beta2_ps2_km": b["beta2"] * 1e27,
                             "D_ps_nm_km": float(dispersion.D_ps_nm_km(lam0_m, b["beta2"]))})
                if R > 0:
                    a = dispersion.anillo(b["beta1"], b["beta2"], R)
                    fila.update({"FSR_nm": lam0_m ** 2 / (b["ng"] * a["L_m"]) * 1e9,
                                 "D1_2pi_GHz": a["D1"] / (2 * np.pi) / 1e9,
                                 "D2_2pi_kHz": a["D2"] / (2 * np.pi) / 1e3,
                                 "regimen_anillo": a["regimen"]})
            res[f"W{W*1e3:.0f}_{clad}_R{R:.0f}"] = fila
    for k, f in sorted(res.items()):
        print(f"  {k:24s} ng {f.get('ng_1550', np.nan):.4f}  a_bend {f['alpha_bend_dbcm']:.3g} dB/cm  "
              f"D {f.get('D_ps_nm_km', np.nan):8.1f}  FSR {f.get('FSR_nm', np.nan):.3f} nm  "
              f"{f.get('regimen_anillo', '')}", flush=True)

    import matplotlib.pyplot as plt
    graficas.aplicar_estilo()
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    for W in Ws:
        for clad, ls in (("sio2", "-"), ("analito", "--")):
            fs = sorted([f for f in res.values() if f["W_um"] == W and f["cladding"] == clad
                         and f["R_um"] > 0], key=lambda f: f["R_um"])
            if not fs:
                continue
            R = [f["R_um"] for f in fs]
            ax[0].semilogy(R, [max(f["alpha_bend_dbcm"], 1e-6) for f in fs], ls, marker="o",
                           label=f"W={W:.2f} µm, {clad}")
            ax[1].plot(R, [f.get("D_ps_nm_km", np.nan) for f in fs], ls, marker="o")
    ax[0].set_xlabel("Radio R (µm)"); ax[0].set_ylabel("α$_{bend}$ (dB/cm)"); ax[0].legend(fontsize=7)
    ax[1].axhline(0, color="k", lw=0.7)
    ax[1].set_xlabel("Radio R (µm)"); ax[1].set_ylabel("D(1550 nm) del modo curvado (ps nm$^{-1}$ km$^{-1}$)")
    graficas.guardar_fig(fig, "curvatura", almacen.dir_figuras_paso(PASO))
    almacen.escribir_contrato(PASO, {"anchos": Ws, "configuraciones": res}, cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
