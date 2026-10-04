"""
paso02_dispersion_h400.py — P2: mapa de dispersión y no linealidad con H = 400 nm (ANT).

Barrido FDE de secciones rectas:
    W ∈ W_UM  ×  λ ∈ 1.0–2.2 µm  ×  cladding {SiO2, analito}  ×  {TE0, TM0}
con materiales dispersivos (paso01), más el sensado de volumen en λ0 con
n_analito = 1.33, 1.35, 1.37 (refractómetro bulk; sin funcionalización).

Salidas por (cladding, pol, W): n_eff, n_g, β2/β3/β4 y D en 1550 nm, β2(λ), ZDW,
A_eff, γ, Γ_abs (cladding y núcleo), número de modos guiados y, con analito,
S_bulk = λ0·(∂n_eff/∂n_analito)/n_g [nm/RIU].

Pregunta que responde: ¿existe con H = 400 nm alguna combinación (W, pol, cladding)
con dispersión ANÓMALA en 1550 nm? Si no, ¿cuál tiene la dispersión normal más
pequeña y plana (supercontinuo en dispersión normal [D9]) y cuál el mayor γ?

Coste: len(W)·len(λ)·len(cladding) solves FDE + len(W)·len(n_sens) de sensado.
Perfil completo ≈ 8·25·2 + 8·3 = 424 solves (orden 1–2 h en esta máquina).
Reanudable: relanzar con `python3 main.py --solo paso02_dispersion_h400 --reanudar`.
"""
from __future__ import annotations

import numpy as np

import _ruta  # noqa: F401
from comun import almacen, barrido, entorno, graficas
from comun import plataforma as P

PASO = "paso02_dispersion_h400"

CONFIG = {
    "H_UM": [P.ALTURA_NUCLEO_UM],
    "W_UM": [0.6, 0.8, 1.0, 1.2, 1.5, 1.8, 2.2, 2.6],
    "CLADDINGS": ["sio2", "analito"],
    # 25 puntos cada 50 nm; incluye 1.55 exacto (punto 11).
    "LAMBDA_UM": [round(1.0 + 0.05 * k, 3) for k in range(25)],
    "N_ANALITO_SENS": [1.33, 1.35, 1.37],
    # Modos de prueba: en guías anchas el TM0 queda por debajo de varios TE.
    "N_MODOS": 16,
    # Dominio: 3 µm de margen. A 2.2 µm la cola evanescente del TM0 en SiN de
    # 400 nm es larga; paso00 cuantifica el efecto de este dominio frente al de la tesis.
    "Y_MARGEN_UM": 3.0, "Z_ABAJO_UM": 3.0, "Z_ARRIBA_UM": 3.0,
    "MALLA_Y": 120, "MALLA_Z": 100,
    # 10 nm en el núcleo: resuelve la discontinuidad del campo TE en las paredes.
    "MALLA_FINA_NM": 10.0, "MALLA_FINA_PAD_UM": 0.30,
    "MATERIALES_DISPERSIVOS": True, "ANCLAR_A_TESIS": True, "ANALITO_DISPERSIVO": True,
    "OCULTAR_GUI": True,
}
RAPIDO = {"W_UM": [0.8, 1.6, 2.6], "LAMBDA_UM": [round(1.2 + 0.1 * k, 2) for k in range(9)],
          "N_ANALITO_SENS": [1.33, 1.37], "MALLA_Y": 70, "MALLA_Z": 60, "MALLA_FINA_NM": 20.0}


def figuras(res: dict, cfg: dict):
    import matplotlib.pyplot as plt
    graficas.aplicar_estilo()
    dfig = almacen.dir_figuras_paso(PASO)
    cmap = plt.get_cmap("viridis")
    for H in cfg["H_UM"]:
        for clad in cfg["CLADDINGS"]:
            fig, axs = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
            for ax, pol in zip(axs, ("te", "tm")):
                filas = [f for f in res.values() if f["H_um"] == H and f["cladding"] == clad
                         and f["pol"] == pol]
                for j, f in enumerate(sorted(filas, key=lambda f: f["W_um"])):
                    ax.plot(f["lambda_nm"], f["D_ps_nm_km"], color=cmap(j / max(1, len(filas) - 1)),
                            label=f"W = {f['W_um']:.2f} µm")
                ax.axhline(0, color="k", lw=0.7)
                ax.axvline(P.LAMBDA0_NM, color="0.5", ls="--", lw=0.7)
                ax.set_title(f"{pol.upper()}0 · H = {H*1e3:.0f} nm · cladding {clad}")
                ax.set_xlabel("Longitud de onda λ (nm)")
            axs[0].set_ylabel("D (ps nm$^{-1}$ km$^{-1}$)   [D > 0: anómala]")
            axs[1].legend(fontsize=7, ncol=2)
            graficas.guardar_fig(fig, f"D_vs_lambda_H{H*1e3:.0f}_{clad}", dfig)

        fig, axs = plt.subplots(2, 2, figsize=(10, 7))
        for clad, ls in (("sio2", "-"), ("analito", "--")):
            for pol, mk in (("te", "o"), ("tm", "s")):
                filas = sorted([f for f in res.values() if f["H_um"] == H and f["cladding"] == clad
                                and f["pol"] == pol and "ng_1550" in f], key=lambda f: f["W_um"])
                if not filas:
                    continue
                W = [f["W_um"] for f in filas]
                et = f"{pol.upper()}0, {clad}"
                axs[0, 0].plot(W, [f["D_ps_nm_km_1550"] for f in filas], ls, marker=mk, label=et)
                axs[0, 1].plot(W, [f["gamma_1550"] for f in filas], ls, marker=mk, label=et)
                axs[1, 0].plot(W, [f["Gamma_abs_clad"] for f in filas], ls, marker=mk, label=et)
                if clad == "analito":
                    axs[1, 1].plot(W, [f.get("S_bulk_nm_RIU", np.nan) for f in filas], ls,
                                   marker=mk, label=et)
        axs[0, 0].axhline(0, color="k", lw=0.7)
        axs[0, 0].set_ylabel("D(1550 nm) (ps nm$^{-1}$ km$^{-1}$)")
        axs[0, 1].set_ylabel("γ(1550 nm) (W$^{-1}$ m$^{-1}$)")
        axs[1, 0].set_ylabel("Γ$_{abs}$ del cladding")
        axs[1, 1].set_ylabel("S$_{bulk}$ (nm/RIU)")
        for a in axs.flat:
            a.set_xlabel("Ancho W (µm)")
        axs[0, 1].legend(fontsize=7)
        graficas.guardar_fig(fig, f"resumen_1550_H{H*1e3:.0f}", dfig)


def main():
    cfg = entorno.aplicar_perfil(CONFIG, RAPIDO)
    almacen.abrir_paso(PASO, cfg)
    n = len(cfg["W_UM"]) * len(cfg["LAMBDA_UM"]) * len(cfg["CLADDINGS"]) * len(cfg["H_UM"])
    print(f"[{PASO}] {n} solves de dispersion + sensado", flush=True)
    barrido.barrer(cfg, PASO)
    res = barrido.procesar(cfg, PASO)
    anom = [k for k, f in res.items() if f.get("regimen_1550") == "anomalo"]
    print(f"[{PASO}] configuraciones ANOMALAS en 1550 nm: {anom or 'ninguna'}", flush=True)
    for k, f in sorted(res.items()):
        if "ng_1550" in f:
            print(f"  {k:28s} ng {f['ng_1550']:.4f}  D {f['D_ps_nm_km_1550']:8.1f}  "
                  f"gamma {f['gamma_1550']:.3f}  Aeff {f['aeff_um2_1550']:.3f} um2  "
                  f"Gclad {f.get('Gamma_abs_clad', np.nan):.3f}  "
                  f"S {f.get('S_bulk_nm_RIU', np.nan):.1f}", flush=True)
    figuras(res, cfg)
    almacen.escribir_contrato(PASO, {"configuraciones": res, "anomalas_1550": anom}, cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
