"""
barrido.py — motor de barrido FDE de secciones RECTAS: H × cladding × W × λ,
y de los puntos de sensado de volumen (n_analito) en λ0.

Un HDF5 por (H, cladding), con índice plano i = iW·nλ + iλ, `flags/computed`
y flush por punto (almacen.init_h5 / escribir_punto). Un barrido interrumpido
se reanuda donde quedó (salvo que preparar_paso borre la carpeta de la firma:
se relanza con los MISMOS parámetros y `--continuar`, ver main.py).

Una sola sesión MODE para todo el barrido: el FDE resuelve en proceso y no
necesita el directorio de motor nativo que exige el FDTD.
"""
from __future__ import annotations

import time

import numpy as np

from . import almacen, dispersion, entorno, seccion
from . import plataforma as P

POLS = ("te", "tm")
CAMPOS = ["n_te_guiados", "n_tm_guiados"] + [
    f"{c}_{pol}" for pol in POLS for c in (
        "neff", "neffi", "tefrac", "aeff_um2", "gamma",
        "q_nucleo", "q_sustrato", "q_clad", "pot_nucleo", "pot_sustrato", "pot_clad")]


def _ruta(dirc, H_um, clad, sufijo=""):
    return dirc / f"seccion_H{H_um*1e3:.0f}nm_{clad}{sufijo}.h5"


def barrer(cfg: dict, paso: str) -> list:
    """Corre (o reanuda) el barrido. Devuelve las rutas de los HDF5."""
    dirc = almacen.dir_cache(paso)
    W_list = list(cfg["W_UM"])
    lam_list = list(cfg["LAMBDA_UM"])
    nl = len(lam_list)
    rutas = []
    app = None
    t0 = time.time()
    try:
        for H in cfg["H_UM"]:
            for clad in cfg["CLADDINGS"]:
                ruta = _ruta(dirc, H, clad)
                cfg_h5 = {**cfg, "H_ACTUAL_UM": H, "CLAD_ACTUAL": clad}
                almacen.init_h5(ruta, cfg_h5, {"W_um": W_list, "lambda_um": lam_list},
                                CAMPOS, len(W_list) * nl)
                rutas.append(ruta)
                for iw, W in enumerate(W_list):
                    guess = None
                    for il, lam in enumerate(lam_list):
                        i = iw * nl + il
                        if almacen.ya_calculado(ruta, i):
                            continue
                        if app is None:
                            print(f"[{paso}] abriendo sesion MODE (puede tardar; no es un cuelgue)",
                                  flush=True)
                            app = entorno.abrir_mode(ocultar_gui=cfg.get("OCULTAR_GUI", True))
                        n_idx, n2c = seccion.indices_caso(lam, clad, cfg)
                        r = seccion.resolver(app, cfg, W, H, lam, n_idx, n2c, neff_guess=guess)
                        almacen.escribir_punto(ruta, i, {k: r.get(k, np.nan) for k in CAMPOS})
                        guess = {p: r[f"neff_{p}"] for p in POLS if np.isfinite(r[f"neff_{p}"])} or None
                        print(f"[{paso}] H={H*1e3:.0f} {clad:7s} W={W:.2f} lam={lam:.3f} "
                              f"TE {r['neff_te']:.5f} TM {r['neff_tm']:.5f} "
                              f"gTE {r['gamma_te']:.3f}  ({time.time()-t0:.0f} s)", flush=True)

        # Sensado de volumen: n_eff en λ0 para varios n_analito (solo cladding analito).
        if cfg.get("N_ANALITO_SENS") and "analito" in cfg["CLADDINGS"]:
            for H in cfg["H_UM"]:
                ruta = _ruta(dirc, H, "analito", "_sensado")
                nsens = list(cfg["N_ANALITO_SENS"])
                almacen.init_h5(ruta, {**cfg, "H_ACTUAL_UM": H},
                                {"W_um": W_list, "n_analito": nsens},
                                ["neff_te", "neff_tm"], len(W_list) * len(nsens))
                rutas.append(ruta)
                lam0 = P.LAMBDA0_NM * 1e-3
                for iw, W in enumerate(W_list):
                    for jn, na in enumerate(nsens):
                        i = iw * len(nsens) + jn
                        if almacen.ya_calculado(ruta, i):
                            continue
                        if app is None:
                            app = entorno.abrir_mode(ocultar_gui=cfg.get("OCULTAR_GUI", True))
                        n_idx, n2c = seccion.indices_caso(lam0, "analito", cfg, n_analito=na)
                        r = seccion.resolver(app, cfg, W, H, lam0, n_idx, n2c)
                        almacen.escribir_punto(ruta, i, {"neff_te": r["neff_te"],
                                                         "neff_tm": r["neff_tm"]})
                        print(f"[{paso}] sensado H={H*1e3:.0f} W={W:.2f} n={na:.3f} "
                              f"TE {r['neff_te']:.6f} TM {r['neff_tm']:.6f}", flush=True)
    finally:
        if app is not None:
            try:
                app.close()
            except Exception:  # noqa: BLE001
                pass
    return rutas


def procesar(cfg: dict, paso: str) -> dict:
    """Del HDF5 a las cifras por (H, cladding, pol, W). Python puro."""
    dirc = almacen.dir_cache(paso)
    lam0_m = P.LAMBDA0_NM * 1e-9
    out = {}
    for H in cfg["H_UM"]:
        sens = None
        rs = _ruta(dirc, H, "analito", "_sensado")
        if rs.exists():
            sens = almacen.leer_resultados(rs)
        for clad in cfg["CLADDINGS"]:
            ruta = _ruta(dirc, H, clad)
            if not ruta.exists():
                continue
            d = almacen.leer_resultados(ruta)
            W_list = d["eje_W_um"]
            lam_m = d["eje_lambda_um"] * 1e-6
            nl = len(lam_m)
            il0 = int(np.argmin(np.abs(lam_m - lam0_m)))
            for pol in POLS:
                for iw, W in enumerate(W_list):
                    sl = slice(iw * nl, (iw + 1) * nl)
                    neff = d[f"neff_{pol}"][sl]
                    clave = f"H{H*1e3:.0f}_{clad}_{pol}_W{W*1e3:.0f}"
                    b = dispersion.betas_en(lam_m, neff, lam0_m)
                    lam_b, b2_b, ng_b = dispersion.beta2_banda(lam_m, neff)
                    D_b = dispersion.D_ps_nm_km(lam_b, b2_b)
                    fila = {"H_um": H, "cladding": clad, "pol": pol, "W_um": float(W),
                            "lambda_nm": (lam_b * 1e9).tolist(),
                            "beta2_ps2_km": (b2_b * 1e27).tolist(),
                            "D_ps_nm_km": D_b.tolist(), "ng_banda": ng_b.tolist(),
                            "ZDW_nm": dispersion.ceros(lam_b, b2_b),
                            "n_te_guiados_1550": float(d["n_te_guiados"][iw * nl + il0]),
                            "n_tm_guiados_1550": float(d["n_tm_guiados"][iw * nl + il0])}
                    for k in ("neff", "aeff_um2", "gamma", "tefrac", "q_nucleo",
                              "q_sustrato", "q_clad", "pot_clad"):
                        fila[f"{k}_1550"] = float(d[f"{k}_{pol}"][iw * nl + il0])
                    if b:
                        fila.update({"ng_1550": b["ng"],
                                     "beta2_ps2_km_1550": b["beta2"] * 1e27,
                                     "beta3_ps3_km_1550": b["beta3"] * 1e39,
                                     "beta4_ps4_km_1550": b["beta4"] * 1e51,
                                     "D_ps_nm_km_1550": float(dispersion.D_ps_nm_km(lam0_m, b["beta2"])),
                                     "regimen_1550": "anomalo" if b["beta2"] < 0 else "normal",
                                     "betas_SI": {k: b[k] for k in ("beta2", "beta3", "beta4")}})
                        # Factor de confinamiento de ABSORCIÓN (lleva n_g delante).
                        fila["Gamma_abs_clad"] = b["ng"] * fila["q_clad_1550"]
                        fila["Gamma_abs_nucleo"] = b["ng"] * fila["q_nucleo_1550"]
                    if clad == "analito" and sens is not None and b:
                        ns = sens["eje_n_analito"]
                        y = sens[f"neff_{pol}"][iw * len(ns):(iw + 1) * len(ns)]
                        ok = np.isfinite(y)
                        if ok.sum() >= 2:
                            pend = np.polyfit(ns[ok], y[ok], 1)[0]
                            fila["dneff_dn_analito"] = float(pend)
                            fila["S_bulk_nm_RIU"] = float(P.LAMBDA0_NM * pend / b["ng"])
                    out[clave] = fila
    return out
