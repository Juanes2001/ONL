"""
paso03_espesor_referencia.py — P3: dónde está la frontera normal/anómala si el espesor
fuese libre. REFERENCIA, no diseño: ANT solo ofrece 400 nm.

Mismo motor que paso02, pero H = 400–900 nm, tres anchos, cladding SiO2 y λ en
1.3–1.9 µm (basta para β2 en 1550 nm y la ZDW cercana). Se compara con la
literatura: Porcel et al. 2017 usan 0.9 µm para tener dispersión anómala en
1.5 µm [D4].
"""
from __future__ import annotations

import _ruta  # noqa: F401
from comun import almacen, barrido, entorno, graficas
from comun import plataforma as P

PASO = "paso03_espesor_referencia"

CONFIG = {
    "H_UM": [0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
    "W_UM": [1.0, 1.6, 2.2],
    "CLADDINGS": ["sio2"],
    "LAMBDA_UM": [round(1.3 + 0.05 * k, 3) for k in range(13)],
    "N_ANALITO_SENS": [],
    "N_MODOS": 16,
    "Y_MARGEN_UM": 3.0, "Z_ABAJO_UM": 3.0, "Z_ARRIBA_UM": 3.0,
    "MALLA_Y": 120, "MALLA_Z": 100, "MALLA_FINA_NM": 10.0, "MALLA_FINA_PAD_UM": 0.30,
    "MATERIALES_DISPERSIVOS": True, "ANCLAR_A_TESIS": True, "ANALITO_DISPERSIVO": True,
    "OCULTAR_GUI": True,
}
RAPIDO = {"H_UM": [0.4, 0.7, 0.9], "W_UM": [1.6], "MALLA_Y": 70, "MALLA_Z": 60,
          "MALLA_FINA_NM": 20.0}


def main():
    cfg = entorno.aplicar_perfil(CONFIG, RAPIDO)
    almacen.abrir_paso(PASO, cfg)
    barrido.barrer(cfg, PASO)
    res = barrido.procesar(cfg, PASO)

    import matplotlib.pyplot as plt
    graficas.aplicar_estilo()
    fig, axs = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
    for ax, pol in zip(axs, ("te", "tm")):
        for W in cfg["W_UM"]:
            filas = sorted([f for f in res.values() if f["pol"] == pol and abs(f["W_um"] - W) < 1e-9
                            and "D_ps_nm_km_1550" in f], key=lambda f: f["H_um"])
            ax.plot([f["H_um"] * 1e3 for f in filas], [f["D_ps_nm_km_1550"] for f in filas],
                    marker="o", label=f"W = {W:.1f} µm")
        ax.axhline(0, color="k", lw=0.7)
        ax.set_title(f"{pol.upper()}0 · cladding SiO$_2$ · λ = {P.LAMBDA0_NM:.0f} nm")
        ax.set_xlabel("Espesor H (nm)")
    axs[0].set_ylabel("D (ps nm$^{-1}$ km$^{-1}$)   [D > 0: anómala]")
    axs[1].legend()
    graficas.guardar_fig(fig, "D_vs_espesor", almacen.dir_figuras_paso(PASO))

    frontera = {}
    for pol in ("te", "tm"):
        for W in cfg["W_UM"]:
            filas = sorted([f for f in res.values() if f["pol"] == pol and abs(f["W_um"] - W) < 1e-9
                            and "D_ps_nm_km_1550" in f], key=lambda f: f["H_um"])
            hs = [f["H_um"] for f in filas if f["D_ps_nm_km_1550"] > 0]
            frontera[f"{pol}_W{W*1e3:.0f}"] = min(hs) if hs else None
    print(f"[{PASO}] menor H con D>0 en 1550 nm (por pol/W): {frontera}", flush=True)
    almacen.escribir_contrato(PASO, {"configuraciones": res, "H_min_anomalo_um": frontera}, cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
