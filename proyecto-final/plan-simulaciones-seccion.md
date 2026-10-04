# Plan de simulación v1 — sección transversal para no linealidades en un anillo add-drop de SiN

Creado el 2026-10-04. Implementado en `simulaciones/seccion_v1/` (ver su `ESTADO.md`).

**Sensado de VOLUMEN (decisión de Juanes, 2026-10-04):** el anillo sensor es un
refractómetro, sin foco en sustancias específicas. El cladding superior es el analito
completo, n = 1.33 → 1.37, **sin funcionalización**. La detección superficial se abordará
**mucho más adelante**.
Contexto de partida: `contexto-fotonica-integrada.md` (plataforma de la tesis) y
`referencias-no-lineal-SiN.txt` (las etiquetas [A3], [D9]… remiten a ese archivo).

---

## 1. Pregunta

¿Qué sección transversal de Si₃N₄ (ancho W, espesor H, cladding, polarización)
hace que el anillo add-drop pueda excitar los fenómenos χ⁽³⁾ que interesan, con la
potencia de bombeo de un laboratorio de banda C? Esos fenómenos son:

- supercontinuo (SC) en una guía de entrada, que haría de fuente de banda ancha para el sensor;
- un peine Kerr o pulsos oscuros dentro del anillo.

Y de ahí: ¿cuáles son los primeros parámetros W, H, R y gaps del anillo?

Supuestos de partida (de la tesis y de la foundry ANT):

- H = 400 nm (LPCVD, el único espesor de ANT); λ_bombeo = 1550 nm; TE₀ como en la tesis.
- Dos claddings posibles: SiO₂ arriba (como los espectrómetros: Q_int ~ 3.7·10⁵) o
  agua arriba (como el sensor: Q_int ~ 1.7–1.85·10⁴, agua ~47 dB/cm).
- n₂(SiN) ≈ 2.4·10⁻¹⁹ m²/W [B1]. En SiN la absorción de dos fotones a 1550 nm es
  despreciable [B2].

## 2. Qué hace "adecuada" a una sección (figuras de mérito)

| magnitud | cómo se obtiene | qué se busca |
|---|---|---|
| β₂(λ), D(λ) | `β₂ = (λ³/2πc²)·d²n_eff/dλ²`, `D = −(λ/c)·d²n_eff/dλ²` | **signo en 1550 nm**: anómalo (D > 0) para solitones brillantes y SC por fisión; normal pequeño y plano para SC coherente por dispersión normal [D9] o pulsos oscuros [E4] |
| β₃, β₄, ZDW | ajuste polinómico de β(ω) alrededor de ω₀ | posición de las longitudes de onda de dispersión cero (ondas dispersivas) y planitud de la curva |
| A_eff no lineal | vectorial (Afshar–Monro): `A_eff = \|∫(E×H*)·ẑ dA\|² / ∫\|(E×H*)·ẑ\|² dA` | pequeña, para tener γ alto |
| γ | `γ = 2π·n₂_eff / (λ·A_eff)`, con n₂ ponderado por región | lo más alto posible; referencia SiN: γ ≈ 1.2–1.4 W⁻¹m⁻¹ [D1, B2] |
| Γ_agua, Γ_SiN | integral de \|E\|² por región (factor de absorción con n_g, como en `perdidas_v1`) | Γ_agua fija la pérdida (y el Q), pero también la sensibilidad. **Es el compromiso central del proyecto** |
| α_bend(R) | Im(n_eff) del FDE curvado | R mínimo sin fuga al BOX |
| N.º de modos guiados | n_eff > n_clad, fracción TE | monomodo o con cruces de modos controlados (estos ayudan a los pulsos oscuros [E4] y estorban a los solitones) |
| D₂ del anillo | `D₂ = −(c/n_g)·D₁²·β₂`, `D_int(μ) ≈ D₂μ²/2 + D₃μ³/6` | signo y magnitud del peine |
| P_umbral OPO | `P_th ≈ 1.54·(π/2)·(Q_c/2Q_L)·n_g²·A_eff·L / (n₂·λ·Q_L²)` [A7] | < ~1 W (amplificador EDFA de laboratorio) |
| N, L_D, L_NL, L_WB | `L_D = T₀²/\|β₂\|`, `L_NL = 1/(γP₀)`, `N² = L_D/L_NL`; rotura de onda óptica según Agrawal [A2] | para la guía de SC: longitud y energía de pulso necesarias |

## 3. Pruebas propuestas (en orden)

### P0 — Validación del montaje (FDE, minutos)
Guía strip de 800 × 400 nm en SiO₂ simétrico a 1550 nm, **con índices constantes**
(1.99 / 1.4469), igual que la tesis. Hay que reproducir el n_eff ≈ 1.597 y el n_g del
espectrómetro de la tesis (contrato del `paso05` de v4) dentro de ~0.2 %.
Si no se reproducen, todo lo demás queda en duda.

### P1 — Modelos de material dispersivos (Python, sin Lumerical)
Para β₂ hace falta la dispersión de MATERIAL, que la tesis no usa (n constante).
- SiN LPCVD: Sellmeier de Luke et al., Opt. Lett. 40, 4823 (2015) (**por verificar**,
  no salió en la búsqueda); SiO₂: Malitson (1965); agua: Hale & Querry (1973) o
  Segelstein (ya usado en la tesis para la absorción).
- Se cargan en Lumerical como materiales de muestras (n, k) entre 0.8 y 2.4 µm.
- Control: n_SiN(1550) frente al 1.99 de la tesis. Si difieren, se documenta qué usa
  cada estudio.

### P2 — Mapa de dispersión con H = 400 nm (FDE con barrido en frecuencia; ~1–2 h)
El estudio central.
- W = 0.6, 0.8, 1.0, 1.2, 1.5, 1.8, 2.2, 2.6 µm.
- λ de 1.0 a 2.2 µm (≥ 25 puntos, o el *frequency analysis* del FDE con *track modes*).
- **Dos claddings** (SiO₂ y agua, con BOX de SiO₂ abajo).
- **TE₀ y TM₀**. El TM₀ en SiN delgado y ancho tiene otra dispersión de guía, y sale
  en la misma corrida sin costo extra. No sé de antemano si alguna combinación da
  dispersión anómala, y P2 está para responderlo.

Salidas: n_eff, n_g, β₂, β₃, β₄, ZDW, A_eff, γ, Γ_agua y número de modos; mapas β₂(W, λ)
y γ(W).

### P3 — Espesor de referencia (FDE; ~1 h)
H = 400, 500, 600, 700, 800, 900 nm, con 3 anchos (1.0, 1.6, 2.2 µm), TE₀ y cladding SiO₂.
Sirve para ubicar la frontera normal/anómala y comparar con la literatura (Porcel: 900 nm
[D4]). Así se cuantifica cuánto nos aleja ANT de la dispersión anómala. No es diseño,
porque ANT no ofrece ese espesor.

### P4 — Anillo: curvatura y dispersión integrada (FDE curvado; ~1 h)
Para las 2–3 secciones finalistas de P2: R = 20, 30, 50, 80, 120 µm.
Salidas: α_bend, desplazamiento de n_eff y β₂ por la curvatura, D₁ (FSR), D₂ y D_int(μ).
FSR objetivo: el que pida el peine (más grande da menos líneas pero un umbral más bajo,
porque P_th ∝ L).

### P5 — Cifras no lineales derivadas (Python, segundos)
Con los resultados de P2 a P4 y los Q medidos en la tesis:
- **Anillo**: P_th para el cladding de agua (Q_L ~ 9.5·10³) y el de SiO₂ (Q_int ~ 3.7·10⁵,
  Q_L según el acoplo). Esta prueba decide si las no linealidades van en el anillo
  sensor, en un anillo encapsulado o en una guía aparte.
- **Guía de SC**: N, L_D, L_NL y L_WB para pulsos de 100–200 fs a 1560 nm y 10–1000 pJ
  (rango de Mayer [D5], Carlson [D6] y Porcel [D4]). Con la pérdida de cada cladding,
  qué longitud de guía hace falta y si cabe en el chip (espiral).
- Ecuación no lineal de Schrödinger generalizada (GNLSE, split-step, [A3]) con β(ω) y γ
  de P2. Es el primer espectro de SC simulado.

### P6 — Después, cuando haya sección elegida (FDTD 3D; local o cluster)
Anillo add-drop lineal con la sección elegida: Q, FSR, D_int real y gaps. Va antes de
cualquier simulación no lineal en el tiempo. El peine en el anillo se simula con la
ecuación de Lugiato-Lefever (LLE) en Python, no en FDTD (un χ⁽³⁾ en FDTD 3D durante
miles de vueltas es inviable).

## 4. Hipótesis de trabajo (a confirmar o descartar con P2–P5)

1. Con H = 400 nm y TE₀, la guía es de **dispersión normal** a 1550 nm en todo el rango
   de W (como sugiere la literatura: el régimen anómalo pide unos 700–900 nm).
2. Si es así, las rutas son: (a) **SC coherente en dispersión normal** en una guía
   larga de SiO₂ [D9], que alimenta al anillo sensor; (b) **pulsos oscuros** en un
   anillo encapsulado en SiO₂ con cruce de modos [E4]; (c) dispersión anómala por
   **anillos concéntricos** [C1] (más complejo).
3. El anillo sensor con agua no es buen generador no lineal (umbral de decenas de W por
   su Q ~ 10⁴). **La no linealidad y el sensado probablemente van en elementos
   distintos del mismo chip**: generador en SiO₂, sensor en agua. P5 debe confirmarlo
   con números.

## 5. Implementación

- Estudio `proyecto-final/simulaciones/seccion_v1/`, copiado de `_plantilla/`. Pasos:
  `paso00_validacion`, `paso01_materiales`, `paso02_dispersion_h400`,
  `paso03_espesor_referencia`, `paso04_curvatura`, `paso05_cifras_no_lineales`.
- P0, P2, P3 y P4 usan MODE/FDE **local** (sesiones de ~1 GB). Antes de cada uno se usa la
  skill `recursos-simulaciones`: el Lumerical local debe estar libre de la tesis y tener
  RAM. Hoy está OCUPADO por la sesión huérfana PID 2568 y tiene ~0.4 GB libres.
- P1 y P5 son Python puro y se pueden avanzar ya. Alternativa de respaldo sin Lumerical:
  el solver semivectorial quasi-TE de la tesis (`pruebas/tolerancia_fab_v1/modos_fd.py`).
  Sirve solo como contraste de tendencias: la segunda derivada que pide β₂ es exigente
  para un semivectorial.
