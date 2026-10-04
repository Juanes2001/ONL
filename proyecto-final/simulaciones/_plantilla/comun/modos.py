"""
modos.py — extraccion y clasificacion de modos del solver FDE.

Concentra las tres trampas que tiene leer modos de Lumerical:
  1. `getdata` devuelve arrays de forma variable segun el tipo de solver; hay
     que aplanar antes de convertir a escalar.
  2. Un modo con Re(n_eff) >= n_nucleo es un artefacto numerico, no un modo:
     el indice efectivo nunca alcanza el del nucleo.
  3. Sin anclar el modo entre soluciones consecutivas, el estencil de n_g puede
     saltar de modo a mitad de la derivada y dar un n_g sin sentido fisico.
"""
from __future__ import annotations

import numpy as np

from . import plataforma as P

TE_FRAC_MIN = 0.5


def recoger_modos(app, n_intentos: int):
    """[(k, n_eff complejo, fraccion TE)] leyendo mode1..modeN hasta el primero
    que no exista."""
    out = []
    for k in range(1, n_intentos + 1):
        try:
            nc = complex(np.asarray(app.getdata(f"FDE::data::mode{k}", "neff")).flat[0])
            te = float(np.asarray(
                app.getdata(f"FDE::data::mode{k}", "TE polarization fraction")).flat[0])
        except Exception:
            break
        out.append((k, nc, te))
    return out


def seleccionar_te0(modos, n_clad_max: float, n_nucleo: float, neff_guess=None):
    """Devuelve (k, n_eff complejo, fraccion TE) del TE0.

    Filtra primero los espurios (n_clad < Re(neff) < n_nucleo), luego se queda
    con los TE. Con neff_guess elige el TE mas cercano a la estimacion (misma
    rama fisica); sin ella, el TE de Re(neff) mas alto = fundamental.
    """
    if not modos:
        return None
    fisicos = [m for m in modos if n_clad_max < m[1].real < n_nucleo]
    pool = fisicos or modos
    te = [m for m in pool if m[2] >= TE_FRAC_MIN] or pool
    if neff_guess is not None:
        return min(te, key=lambda m: abs(m[1].real - neff_guess))
    return max(te, key=lambda m: m[1].real)


def contar_guiados(modos, n_clad_max: float, n_nucleo: float):
    """(n_TE, n_TM) modos guiados y fisicos."""
    n_te = n_tm = 0
    for _k, nc, te in modos:
        if not (n_clad_max < nc.real < n_nucleo):
            continue
        if te >= TE_FRAC_MIN:
            n_te += 1
        else:
            n_tm += 1
    return n_te, n_tm


def resolver(app, n_intentos: int, n_clad_max: float, neff_guess=None):
    """run + findmodes + seleccion del TE0. Devuelve dict o None si no hay modos."""
    app.run()
    app.findmodes()
    modos = recoger_modos(app, n_intentos)
    sel = seleccionar_te0(modos, n_clad_max, P.N_SIN, neff_guess)
    if sel is None:
        return None
    k, nc, te = sel
    n_te, n_tm = contar_guiados(modos, n_clad_max, P.N_SIN)
    return {"k": k, "neff": nc.real, "neff_imag": nc.imag, "te_frac": te,
            "n_te": n_te, "n_tm": n_tm, "n_modos": len(modos)}


def ng_estencil(app, construir, cfg, dlam_nm: float, n_clad_max: float,
                neff_guess=None):
    """n_g por diferencia central de n_eff(lambda), anclando las tres
    soluciones al MISMO modo fisico.

    n_g = n_eff(l0) - l0 * [n_eff(l0+dl) - n_eff(l0-dl)] / (2 dl)

    `neff_guess` ancla TAMBIEN la primera solucion, no solo las dos laterales.
    Es imprescindible en guia CURVADA: sin ancla, `seleccionar_te0` se queda con
    el modo TE de mayor n_eff, y en un bend ese no tiene por que ser el TE0 del
    nucleo. Medido a 1550 nm sobre la seccion del sensor de 850 nm con
    R = 18.2372 um: el solver devuelve un modo a 1.590738 (TE = 1.000) que
    apenas toca la capa funcionalizada (S_neff = 0.00014 /RIU) por delante del
    TE0 real a 1.581938 (S_neff = 0.0152 /RIU, el mismo que da la guia recta).
    Con la geometria anterior (950 nm, R = 17.1650 um) el orden salia al reves
    y el modo correcto ganaba por casualidad. Pasa como ancla el n_eff de la
    seccion RECTA equivalente.
    """
    lam0_nm = cfg["LAMBDA_NM"]
    resultados = {}
    base = neff_guess
    for etiqueta, lam_nm in (("0", lam0_nm),
                             ("lo", lam0_nm - dlam_nm),
                             ("hi", lam0_nm + dlam_nm)):
        c = dict(cfg); c["LAMBDA_M"] = lam_nm * 1e-9
        construir(app, c)
        r = resolver(app, cfg["N_MODOS"], n_clad_max, neff_guess=base)
        if r is None:
            return None
        if base is None:
            base = r["neff"]
        resultados[etiqueta] = r

    lam0_m = lam0_nm * 1e-9
    dlam_m = 2.0 * dlam_nm * 1e-9
    ng = resultados["0"]["neff"] - lam0_m * (
        resultados["hi"]["neff"] - resultados["lo"]["neff"]) / dlam_m
    return {**resultados["0"], "ng": float(ng),
            "neff_lo": resultados["lo"]["neff"], "neff_hi": resultados["hi"]["neff"]}


def campos_seccion(app, k: int):
    """Malla (y, z) y componentes del modo k, todo aplanado a 2D (ny, nz)."""
    grp = f"FDE::data::mode{k}"
    y = np.asarray(app.getdata(grp, "y")).flatten()
    z = np.asarray(app.getdata(grp, "z")).flatten()

    def comp(nombre):
        a = np.asarray(app.getdata(grp, nombre))
        return np.squeeze(a).reshape(len(y), len(z))

    return y, z, {c: comp(c) for c in ("Ey", "Ez", "Hy", "Hz")}


def flujo_potencia(campos):
    """Sx = 0.5 * Re(Ey*conj(Hz) - Ez*conj(Hy)): potencia que se propaga.

    Se integra Sx y no |E|^2 porque el factor de confinamiento relevante para
    un sensor evanescente es la fraccion de POTENCIA que viaja por cada region.
    """
    return 0.5 * np.real(campos["Ey"] * np.conj(campos["Hz"])
                         - campos["Ez"] * np.conj(campos["Hy"]))


def integrar_regiones(y_um, z_um, Sx, mascaras):
    """Fraccion de potencia en cada region. Integra con el paso real de la
    malla (no uniforme), asi que no se puede usar una suma simple."""
    dy = np.gradient(np.asarray(y_um))
    dz = np.gradient(np.asarray(z_um))
    peso = np.outer(dy, dz)
    total = float(np.sum(Sx * peso))
    if total == 0.0 or not np.isfinite(total):
        return {k: float("nan") for k in mascaras}
    return {k: float(np.sum(Sx * peso * m) / total) for k, m in mascaras.items()}
