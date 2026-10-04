"""
plataforma.py — constantes FÍSICAS del estudio seccion_v1. Sin resultados.

Estudio: sección transversal de SiN para excitar fenómenos χ(3) en un anillo
add-drop que funciona como REFRACTÓMETRO DE VOLUMEN (bulk). El cladding superior
es el analito líquido completo, n = 1.33 → 1.37, sin capa funcionalizada.
⚠ La detección SUPERFICIAL (funcionalización) queda para una fase posterior
del proyecto, mucho más adelante. Este estudio no la modela.

Unidades: lo que va a Lumerical, en SI. *_NM / *_UM solo para mostrar.
"""
from __future__ import annotations

# Exacta. Usar 3e8 mete un sesgo de 0.07 % en n_g.
SPEED_OF_LIGHT = 299_792_458.0

# ── Banda y bombeo ──────────────────────────────────────────────────────────
LAMBDA0_NM = 1550.0           # bombeo / operación del sensor (banda C del laboratorio)

# ── Apilamiento (foundry ANT, igual que la tesis) ──────────────────────────
ALTURA_NUCLEO_UM = 0.400      # SiN LPCVD; el único espesor que ofrece ANT
# Índices a 1550 nm usados por la tesis. Los modelos dispersivos de
# comun/materiales.py se ANCLAN a estos valores (ver ANCLAR_A_TESIS).
N_SIN_1550 = 1.99
N_SIO2_1550 = 1.4469
N_ANALITO_BASE = 1.33         # agua de referencia del refractómetro (como la tesis)
N_ANALITO_RANGO = (1.33, 1.37)  # barrido de volumen del refractómetro

# Para el filtro de modos espurios de comun/modos.py (Re(n_eff) < n_núcleo).
N_SIN = 2.05                  # cota superior del SiN dispersivo en 1.0–2.2 µm

# ── Índice no lineal n2 [m²/W] por región ──────────────────────────────────
# SiN: Ikeda et al. 2008 [B1] (PECVD); los reviews dan el mismo orden para LPCVD [A4].
# SiO2: valor estándar de la sílice fundida (Agrawal [A2]).
# Agua: orden de magnitud, SIN VERIFICAR (su peso en γ es pequeño: Γ_agua ~ 0.1–0.3).
N2_M2_W = {"nucleo": 2.4e-19, "sustrato": 2.6e-20, "silice": 2.6e-20, "agua": 2.7e-20}
