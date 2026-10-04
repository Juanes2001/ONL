# Contexto: proyecto `fotonica-integrada` (tesis) como base del proyecto final de ONL

Resumen hecho el 2026-10-04 leyendo `../fotonica-integrada` **en modo solo lectura**
(repo `github.com/Juanes2001/fotonica-integrada`, último commit leído `ae92e7e`).
Las cifras se copian de sus documentos; la fuente de cada una va entre paréntesis.
Si hay duda, **manda el repo de la tesis**, no este resumen.

---

## 1. Qué es

Tesis: **plataforma fotónica de anillos de Si₃N₄ en cascada para biosensado "power-only"**,
es decir, leer el índice de refracción del analito **sin láser sintonizable ni OSA**, solo con
fotodetectores de potencia.

- **RING_1 = anillo sensor (add-drop).** Cladding acuoso expuesto al analito
  (n = 1.33 → 1.37 en volumen; o capa funcionalizada de 10 nm en superficie). Su resonancia
  se desplaza con Δn_clad.
- **RING_2 … RING_14 = 13 anillos espectrómetro**, encapsulados en SiO₂, con resonancias
  escalonadas que tapizan un FSR (canal = FSR/13). Son una "regla espectral" en chip.
- **Cadena:** analito → Δn_clad → Δn_eff → Δλ_res → el **drop** del sensor (pasa-banda)
  barre el peine → vector de 13 potencias [dBm] → concentración.
- Asimetría intencional: el sensor entrega su **drop** a la cascada; cada espectrómetro pasa su
  **through** al siguiente y su drop a un detector.
- Polarización **TE₀** en los 14 anillos. Herramientas: Ansys Lumerical (MODE/FDE, varFDTD,
  FDTD 3D, INTERCONNECT), Python; FDTD caro en el cluster *wegener* (Lumerical 2026R1).

(`CLAUDE.md` §1; `docs/plataforma_referencia.md` §1–3)

## 2. Plataforma (decisión cerrada: banda C, 1550 nm)

| Parámetro | Valor |
|---|---|
| λ₀ | 1550 nm |
| Núcleo | Si₃N₄ LPCVD, **espesor 400 nm**, n = 1.99 |
| Cladding inferior (BOX) | SiO₂, n = 1.4469 (2 µm en el diseño; 4.5 µm en la foundry ANT) |
| Sensor strip (v2) | 850 × 400 nm, liner 10 nm, agua 1.33, R ≈ 18.2–19 µm |
| Sensor slot 1550 (v4) | rails 550 nm / slot 200 nm, R* = 41.18 µm, FSR 4.95 nm |
| Espectrómetros 1550 | strip 800 × 400 nm (referencia previa: 1000 nm) |
| Foundry objetivo | ANT (vía SiEPIC): EBL, mín. 120 nm, pared 90°, heaters TiW |

(`CLAUDE.md` §2; `docs/plan_prioridades.md` §0.4; `plataforma_v4_slot_1550/ESTADO.md`)

## 3. Resultados clave ya medidos

**Pérdidas** (`simulaciones/perdidas_v1`): el agua absorbe **~47 dB/cm a 1550 nm**; con el factor
de confinamiento de absorción (Γ_agua ≈ 0.195, lleva n_g delante) el sensor strip pierde
**9.3–12.3 dB/cm** en guía recta (9.21 dB/cm irreducibles por agua). Espectrómetros: 0.92–2.58 dB/cm.

**Anillo strip cerrado en agua a 1550** (FDTD 3D, job 3247, `cluster/strip_anillo_agua_1550`):

| | valor |
|---|---|
| FWHM · Q_L (1553.66 nm) | 163 pm · 9 536 |
| Pérdida de curva + acopladores | 7.0–8.7 dB/cm (además del agua) |
| Q_int con 12.31 dB/cm | 17 000 – 18 500 |
| FSR · n_g | 10.264 nm · 2.0389 |
| κ₁ · κ₂ | 0.21–0.23 · 0.16–0.18 |

**Tabla de cotas** (`docs/plan_prioridades.md` §0.1): Q_int slot 1550 en anillo: 5 900–6 600
(FWHM ≥ 470 pm); espectrómetro strip 800 a 1550 (en SiO₂): **Q_int ≈ 374 000** (FWHM ≈ 8 pm).

**Sensibilidad:** volumen S ≈ 198 nm/RIU (varFDTD) vs 153 nm/RIU (INTERCONNECT), discrepancia
no resuelta; superficie: strip 11.2 nm/RIU, slot 1550 22.75 nm/RIU. Resolución estimada con
lectura power-only: 3σ ≈ 3–4·10⁻⁴ RIU.

**Otros hallazgos:** la fabricación (ancho local) domina la posición del peine (~180–470 pm por
nm de ancho vs ~33 pm por nm de radio); se propone calibración por chip y heaters (15.5 pm/K).
El escalado de radios del `paso05` comprime el peine ×0.80 (confirmado en FDTD).

## 4. Lo que NO existe en la tesis (y por tanto aporta el proyecto de ONL)

Búsqueda en todo el repo (2026-10-04): **no hay ningún estudio no lineal** — ni n₂/Kerr, ni
GVD/β₂ como objetivo de diseño, ni SPM/FWM/supercontinuo. Todo el modelado es lineal
(modos, acoplo, transferencia de anillos). La dispersión solo aparece vía n_g y FSR, y el
modelo de INTERCONNECT tiene dispersión = 0.

## 5. Observaciones iniciales para el proyecto de ONL (por verificar)

1. **Régimen de dispersión.** SiN de 400 nm de espesor a 1550 nm (TE) suele quedar en
   **dispersión normal**; el supercontinuo por fisión de solitones y los microcombs de
   solitón brillante requieren dispersión anómala, que en SiN suele pedir núcleos más gruesos
   (≳ 700–800 nm). Primer cálculo necesario: β₂(λ), β₃ y A_eff de las secciones de la tesis
   (strip 800/850 × 400 nm, slot 550/200) con el solver de modos.
2. **Umbral paramétrico del anillo sensor.** Con Q_L ~ 10⁴ (agua) el umbral de oscilación
   paramétrica sale del orden de **decenas de W** (estimación de orden de magnitud con
   n₂(SiN) ≈ 2.4·10⁻¹⁹ m²/W, A_eff ~ 1 µm², L ≈ 115 µm; hay que rehacerla con los datos
   reales). Los espectrómetros (Q_int ~ 4·10⁵, en SiO₂) son mucho mejores candidatos para
   efectos no lineales en resonancia.
3. **Arquitectura alternativa coherente con "power-only":** generar el supercontinuo en una
   guía/espiral de SiN bombeada con pulsos (fs), y usarlo como **fuente de banda ancha en
   chip** que ilumina el anillo sensor add-drop; el drop selecciona la banda de resonancia y la
   cascada la lee. Esto reemplazaría el ONA / láser sintonizable de la tesis.
4. Temas del curso que encajan: GVD (Agrawal cap. 3), SPM y solitones (Agrawal 4–5), FWM
   y Raman (Agrawal 8, 10), índice dependiente de la intensidad (Boyd 4).
