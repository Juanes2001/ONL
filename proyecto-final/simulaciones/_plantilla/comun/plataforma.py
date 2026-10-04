"""
plataforma.py — constantes FISICAS del estudio. Sin resultados de simulacion.

Plantilla para el proyecto de ONL. Valores de partida tomados de la tesis
(fotonica-integrada, CLAUDE.md §2): SiN LPCVD 400 nm a 1550 nm.

⚠ Para supercontinuo / dispersion hay que pasar de indices CONSTANTES a
materiales DISPERSIVOS (Sellmeier o material de la base de Lumerical): con
n constante el beta2 solo contiene la dispersion de guia. Decidir por estudio.
"""
from __future__ import annotations

# Exacta. Usar 3e8 mete un sesgo de 0.07 % en n_g.
SPEED_OF_LIGHT = 299_792_458.0

LAMBDA0_NM = 1550.0
ALTURA_NUCLEO_UM = 0.400

N_SIN = 1.99
N_SIO2 = 1.4469
N_AGUA = 1.33
