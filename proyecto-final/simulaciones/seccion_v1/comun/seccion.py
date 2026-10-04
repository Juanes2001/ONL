"""
seccion.py — sección transversal de SiN en el FDE (MODE) y métricas modales por solve.

Geometría (FDE "2D X normal": propagación en x, y lateral, z vertical):

        cladding superior: SiO2 (encapsulado) o ANALITO (refractómetro de volumen)
        +-- núcleo SiN  W × H, centrado en (y, z) = (0, 0)
        ============ BOX SiO2 (desde z = −H/2 hasta el fondo del dominio) ============

Prioridad de solapamiento: gana el `mesh order` MÁS BAJO, fijado explícitamente
(lección de la tesis, geometria.py).

Por cada solve se extraen, para TE0 y TM0:
  n_eff, fracción TE, número de modos guiados,
  A_eff y γ no lineales (forma vectorial de Afshar y Monro, con S_x = Re(E×H*)·x̂),
  q_i = n_i ∫_i |E|² dA / ∫ n² |E|² dA por región. El factor de confinamiento
  para ABSORCIÓN es Γ_i = n_g · q_i (perdidas_v1 de la tesis). n_g se conoce
  después del barrido en λ, así que aquí se guarda solo q_i.
"""
from __future__ import annotations

import numpy as np

from . import materiales, modos
from . import plataforma as P

ORDEN_NUCLEO = 2
ORDEN_BOX = 5
ORDEN_FONDO = 6
REGIONES = ("nucleo", "sustrato", "clad")


def _dielectrico(app, n: float, orden: int) -> None:
    app.set("material", "<Object defined dielectric>")
    app.set("index", float(n))
    app.set("override mesh order from material database", True)
    app.set("mesh order", int(orden))


def _rect(app, nombre, y_ctr, y_span, z_ctr, z_span, n, orden):
    app.addrect()
    app.set("name", nombre)
    app.set("x", 0.0); app.set("x span", 1.0e-6)
    app.set("y", y_ctr * 1e-6); app.set("y span", y_span * 1e-6)
    app.set("z", z_ctr * 1e-6); app.set("z span", z_span * 1e-6)
    _dielectrico(app, n, orden)


def dominio_um(cfg: dict, W_um: float, H_um: float) -> dict:
    y_span = W_um + 2 * cfg["Y_MARGEN_UM"]
    z_abajo, z_arriba = cfg["Z_ABAJO_UM"], cfg["Z_ARRIBA_UM"]
    return {"y_span": y_span, "z_abajo": z_abajo, "z_arriba": z_arriba,
            "z_span": z_abajo + H_um + z_arriba,
            "z_ctr": (z_arriba - z_abajo) / 2.0}


def construir(app, cfg: dict, W_um: float, H_um: float, lam_um: float,
              n_idx: dict, radio_um: float | None = None) -> None:
    """Monta el FDE de una sección con los índices `n_idx` a la λ dada.

    n_idx: {"nucleo", "box", "clad"}. clad es SiO2 o el analito según el caso.
    radio_um: si se da, guía CURVADA (FDE de bend); si no, recta.
    """
    d = dominio_um(cfg, W_um, H_um)
    app.switchtolayout()
    app.selectall()
    app.delete()

    app.addfde()
    app.set("solver type", "2D X normal")
    app.set("x", 0.0)
    app.set("y", 0.0); app.set("y span", d["y_span"] * 1e-6)
    app.set("z", d["z_ctr"] * 1e-6); app.set("z span", d["z_span"] * 1e-6)
    app.set("wavelength", lam_um * 1e-6)
    app.set("number of trial modes", int(cfg["N_MODOS"]))
    # Malla de fondo gruesa + caja fina sobre el núcleo: a 10 nm se resuelven las
    # paredes del SiN, donde el campo TE es discontinuo y concentra la A_eff.
    app.set("mesh cells y", int(cfg["MALLA_Y"]))
    app.set("mesh cells z", int(cfg["MALLA_Z"]))
    if radio_um:
        # Bend: el FDE resuelve el modo de la guía curvada en coordenadas
        # cilíndricas. Mismo ajuste que la tesis (paso09).
        app.set("bent waveguide", 1)
        app.set("bend radius", float(radio_um) * 1e-6)
        app.set("bend orientation", 0)
        if cfg.get("PML_EN_BEND", True):
            # Con bordes metálicos la radiación de la curva se refleja y vuelve:
            # Im(n_eff) no mediría la pérdida por curvatura. Con PML sale del dominio.
            # (`set` sobre una propiedad inexistente lanza error: no falla en silencio.)
            for b in ("y min bc", "y max bc", "z min bc", "z max bc"):
                app.set(b, "PML")

    # Fondo = cladding superior, prioridad más baja; BOX debajo del núcleo.
    _rect(app, "fondo", 0.0, d["y_span"], d["z_ctr"], d["z_span"], n_idx["clad"], ORDEN_FONDO)
    _rect(app, "box", 0.0, d["y_span"], -(H_um / 2 + d["z_abajo"] / 2), d["z_abajo"],
          n_idx["box"], ORDEN_BOX)
    _rect(app, "nucleo", 0.0, W_um, 0.0, H_um, n_idx["nucleo"], ORDEN_NUCLEO)

    paso = cfg["MALLA_FINA_NM"] * 1e-9
    pad = cfg["MALLA_FINA_PAD_UM"]
    app.addmesh()
    app.set("name", "malla_nucleo")
    app.set("x", 0.0); app.set("x span", 1.0e-6)
    app.set("y", 0.0); app.set("y span", (W_um + 2 * pad) * 1e-6)
    app.set("z", 0.0); app.set("z span", (H_um + 2 * pad) * 1e-6)
    app.set("override x mesh", False)
    app.set("override y mesh", True); app.set("dy", paso)
    app.set("override z mesh", True); app.set("dz", paso)


def _campos(app, k: int):
    """(y, z, dict de componentes) del modo k, todo (ny, nz)."""
    grp = f"FDE::data::mode{k}"
    y = np.asarray(app.getdata(grp, "y")).flatten()
    z = np.asarray(app.getdata(grp, "z")).flatten()

    def comp(nombre):
        return np.squeeze(np.asarray(app.getdata(grp, nombre))).reshape(len(y), len(z))

    return y, z, {c: comp(c) for c in ("Ex", "Ey", "Ez", "Hx", "Hy", "Hz")}


def mascaras(y_m, z_m, W_um, H_um):
    Y, Z = np.meshgrid(np.asarray(y_m) * 1e6, np.asarray(z_m) * 1e6, indexing="ij")
    nucleo = (np.abs(Y) <= W_um / 2) & (np.abs(Z) <= H_um / 2)
    sustrato = (Z < -H_um / 2) & ~nucleo
    clad = ~nucleo & ~sustrato
    return {"nucleo": nucleo, "sustrato": sustrato, "clad": clad}


def metricas_modo(app, k: int, W_um, H_um, lam_um, n_idx: dict, n2_clad: float) -> dict:
    """A_eff, γ y q_i del modo k (ver cabecera)."""
    y, z, F = _campos(app, k)
    peso = np.outer(np.gradient(y), np.gradient(z))
    m = mascaras(y, z, W_um, H_um)
    n_map = (m["nucleo"] * n_idx["nucleo"] + m["sustrato"] * n_idx["box"]
             + m["clad"] * n_idx["clad"])
    E2 = np.abs(F["Ex"]) ** 2 + np.abs(F["Ey"]) ** 2 + np.abs(F["Ez"]) ** 2
    Sx = 0.5 * np.real(F["Ey"] * np.conj(F["Hz"]) - F["Ez"] * np.conj(F["Hy"]))

    den_eps = float(np.sum(n_map ** 2 * E2 * peso))
    q = {r: float(np.sum(n_map * E2 * peso * m[r]) / den_eps) for r in REGIONES}

    sx_tot = float(np.sum(Sx * peso))
    n2 = {"nucleo": P.N2_M2_W["nucleo"], "sustrato": P.N2_M2_W["sustrato"], "clad": n2_clad}
    num = sum(n2[r] * float(np.sum(Sx ** 2 * peso * m[r])) for r in REGIONES)
    k0 = 2 * np.pi / (lam_um * 1e-6)
    gamma = k0 * num / sx_tot ** 2                                   # 1/(W·m)
    aeff = sx_tot ** 2 / float(np.sum(Sx ** 2 * peso * m["nucleo"]))  # m², sobre el SiN
    fr_pot = {r: float(np.sum(Sx * peso * m[r]) / sx_tot) for r in REGIONES}
    return {"aeff_um2": aeff * 1e12, "gamma": gamma,
            **{f"q_{r}": q[r] for r in REGIONES},
            **{f"pot_{r}": fr_pot[r] for r in REGIONES}}


def resolver(app, cfg, W_um, H_um, lam_um, n_idx, n2_clad, radio_um=None,
             neff_guess=None) -> dict:
    """Construye, resuelve y devuelve TE0 y TM0 con sus métricas.

    TE0 = TE (fracción > 0.5) de mayor n_eff; TM0 igual entre los TM. En guía curva
    se ancla con `neff_guess` (n_eff de la recta), lección de la tesis
    (modos.ng_estencil): en un bend el TE de mayor n_eff no siempre es el TE0.
    Un modo con n_eff ≤ max(n_box, n_clad) se marca como no guiado (NaN).
    """
    construir(app, cfg, W_um, H_um, lam_um, n_idx, radio_um)
    app.run()
    app.findmodes()
    lista = modos.recoger_modos(app, int(cfg["N_MODOS"]))
    n_clad_max = max(n_idx["box"], n_idx["clad"])
    n_te, n_tm = modos.contar_guiados(lista, n_clad_max, P.N_SIN)
    out = {"n_te_guiados": n_te, "n_tm_guiados": n_tm}
    for pol, cond in (("te", lambda t: t >= modos.TE_FRAC_MIN),
                      ("tm", lambda t: t < modos.TE_FRAC_MIN)):
        cand = [m for m in lista if cond(m[2]) and n_clad_max < m[1].real < P.N_SIN]
        guess = (neff_guess or {}).get(pol)
        if cand and guess is not None:
            sel = min(cand, key=lambda m: abs(m[1].real - guess))
        elif cand:
            sel = max(cand, key=lambda m: m[1].real)
        else:
            sel = None
        if sel is None:
            out.update({f"neff_{pol}": np.nan, f"neffi_{pol}": np.nan,
                        f"tefrac_{pol}": np.nan, f"aeff_um2_{pol}": np.nan,
                        f"gamma_{pol}": np.nan,
                        **{f"q_{r}_{pol}": np.nan for r in REGIONES},
                        **{f"pot_{r}_{pol}": np.nan for r in REGIONES}})
            continue
        k, nc, te = sel
        met = metricas_modo(app, k, W_um, H_um, lam_um, n_idx, n2_clad)
        out.update({f"neff_{pol}": nc.real, f"neffi_{pol}": nc.imag, f"tefrac_{pol}": te,
                    **{f"{a}_{pol}": b for a, b in met.items()}})
    return out


def indices_caso(lam_um: float, cladding: str, cfg: dict,
                 n_analito: float = P.N_ANALITO_BASE) -> tuple[dict, float]:
    """(n_idx, n2 del cladding) para cladding 'sio2' o 'analito'."""
    n = materiales.indices(lam_um, n_analito=n_analito,
                           anclar=cfg.get("ANCLAR_A_TESIS", True),
                           analito_dispersivo=cfg.get("ANALITO_DISPERSIVO", True))
    if not cfg.get("MATERIALES_DISPERSIVOS", True):
        n = {"nucleo": P.N_SIN_1550, "silice": P.N_SIO2_1550, "analito": n_analito}
    if cladding == "sio2":
        return {"nucleo": n["nucleo"], "box": n["silice"], "clad": n["silice"]}, P.N2_M2_W["silice"]
    if cladding == "analito":
        return {"nucleo": n["nucleo"], "box": n["silice"], "clad": n["analito"]}, P.N2_M2_W["agua"]
    raise ValueError(f"cladding desconocido: {cladding!r}")
