"""
paso00_validacion.py — P0: reproducir con este montaje un resultado FDE de la tesis.

Guía strip de 800 × 400 nm en SiO2 SIMÉTRICO a 1550 nm, con índices CONSTANTES
(1.99 / 1.4469) y la misma malla y dominio del paso03 de la tesis
(fotonica-integrada/simulaciones/plataforma_v4_slot_1550, contrato paso03):

    n_eff = 1.5967283730674795,  n_g = 1.9797844874851565

Si no se reproducen dentro de la tolerancia, el constructor de comun/seccion.py
tiene un error y NADA de lo que sigue vale. Después repite el caso con la malla y
el dominio de PRODUCCIÓN (los de paso02): la diferencia es el error de
discretización que arrastran los barridos.

n_g por diferencia central de n_eff(λ ± DLAM), igual que la tesis.
"""
from __future__ import annotations

import _ruta  # noqa: F401
from comun import almacen, entorno, seccion
from comun import plataforma as P

PASO = "paso00_validacion"

REF_TESIS = {"neff": 1.5967283730674795, "ng": 1.9797844874851565}
TOL_REL = {"neff": 1e-3, "ng": 3e-3}

# Malla y dominio IDÉNTICOS al paso03 de la tesis: Y_SPAN 6 µm = W + 2·2.6.
CONFIG_TESIS = {
    "N_MODOS": 8, "Y_MARGEN_UM": 2.6, "Z_ABAJO_UM": 2.0, "Z_ARRIBA_UM": 2.0,
    "MALLA_Y": 80, "MALLA_Z": 60, "MALLA_FINA_NM": 10.0, "MALLA_FINA_PAD_UM": 0.30,
    "MATERIALES_DISPERSIVOS": False, "OCULTAR_GUI": True,
}
# Producción (paso02): dominio más grande, porque a 2.2 µm el modo se extiende más.
CONFIG_PROD = {**CONFIG_TESIS, "Y_MARGEN_UM": 3.0, "Z_ABAJO_UM": 3.0, "Z_ARRIBA_UM": 3.0,
               "MALLA_Y": 120, "MALLA_Z": 100}
CONFIG = {"W_UM": 0.8, "H_UM": P.ALTURA_NUCLEO_UM, "DLAM_NM": 5.0,
          "TESIS": CONFIG_TESIS, "PROD": CONFIG_PROD}


def medir(app, c, W, H):
    lam0 = P.LAMBDA0_NM * 1e-3
    dl = CONFIG["DLAM_NM"] * 1e-3
    vals = {}
    for et, lam in (("0", lam0), ("lo", lam0 - dl), ("hi", lam0 + dl)):
        n_idx, n2c = seccion.indices_caso(lam, "sio2", c)
        vals[et] = seccion.resolver(app, c, W, H, lam, n_idx, n2c)["neff_te"]
    ng = vals["0"] - lam0 * (vals["hi"] - vals["lo"]) / (2 * dl)
    return {"neff": vals["0"], "ng": ng}


def main():
    cfg = entorno.aplicar_perfil(CONFIG, {})
    almacen.abrir_paso(PASO, cfg)
    W, H = cfg["W_UM"], cfg["H_UM"]
    print(f"[{PASO}] abriendo sesion MODE (puede tardar; no es un cuelgue)", flush=True)
    app = entorno.abrir_mode(ocultar_gui=True)
    try:
        tes = medir(app, cfg["TESIS"], W, H)
        prod = medir(app, cfg["PROD"], W, H)
    finally:
        app.close()

    err = {k: (tes[k] - REF_TESIS[k]) / REF_TESIS[k] for k in REF_TESIS}
    ok = all(abs(err[k]) <= TOL_REL[k] for k in err)
    dprod = {k: (prod[k] - tes[k]) / tes[k] for k in tes}
    for k in ("neff", "ng"):
        print(f"[{PASO}] {k}: montaje tesis {tes[k]:.6f} | ref {REF_TESIS[k]:.6f} "
              f"({err[k]*100:+.3f} %) | produccion {prod[k]:.6f} ({dprod[k]*100:+.3f} %)",
              flush=True)
    print(f"[{PASO}] VALIDACION {'OK' if ok else 'FALLA — revisar comun/seccion.py'}", flush=True)
    almacen.escribir_contrato(PASO, {"valido": ok, "montaje_tesis": tes, "produccion": prod,
                                     "ref_tesis": REF_TESIS, "error_rel": err,
                                     "dif_rel_produccion": dprod}, cfg)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
