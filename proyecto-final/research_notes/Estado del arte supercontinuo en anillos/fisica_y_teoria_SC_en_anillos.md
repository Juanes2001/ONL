# Física y teoría de la generación espectral tipo supercontinuo en microanillos Kerr bombeados en CW

Notas de investigación (ronda 2, 2026-10-29). Alcance: micro-resonadores de anillo/disco con no linealidad Kerr
bombeados con láser continuo; cavidades de anillo de fibra solo como comparación conceptual. Período cubierto:
2007 (primer peine Kerr) a octubre de 2026, con énfasis 2014–2026.

**Verificación de DOI.** Todos los DOI de la lista final (§ Referencias) se resolvieron contra la API de Crossref
(`api.crossref.org/works/<doi>`) el 2026-10-29 y devolvieron el título/revista/año esperados. Los únicos ítems
sin DOI son preprints de arXiv de 2024–2026 todavía no publicados en revista; se indican como tales.

**Convención de notación usada en estas notas** (la de Kippenberg/Herr/Gorodetsky, que es la dominante en la
bibliografía de microresonadores): frecuencias de resonancia ω_μ = ω₀ + Σ_j D_j μ^j / j!, con μ el número de modo
relativo al modo bombeado, D₁/2π = FSR, D₂ = −(c/n) D₁² β₂ (D₂ > 0 ⇔ dispersión anómala), dispersión integrada
D_int(μ) ≡ ω_μ − (ω₀ + D₁ μ) = D₂ μ²/2 + D₃ μ³/6 + D₄ μ⁴/24 + …; κ = ancho de línea cargado (rad/s),
κ_ex = tasa de acoplamiento externo, η = κ_ex/κ; detuning normalizado ζ₀ = 2(ω₀ − ω_p)/κ (ζ₀ > 0 ⇔ bomba al rojo);
d₂ = 2D₂/κ (OJO: Herr 2014 usa d₂ = D₂/κ; ver §4); bomba normalizada f² = P_in/P_th. La convención de Coen &
Erkintalo (fibra) usa β₂, γ = 2πn₂/(λ A_eff), finesse 𝓕, Δ ≡ ζ₀ y X ≡ f² (ver §4).

---

## 1. ¿Qué entienden los autores por "supercontinuo" en un microresonador frente a "peine Kerr de octava"? ¿Se usan como sinónimos? ¿Quién usa "cavity-enhanced" o "resonant supercontinuum"?

### Takeaway
En la literatura de microresonadores el espectro ancho generado por un solitón Kerr disipativo (DKS) bombeado en
CW casi nunca se llama "supercontinuo": se llama "peine Kerr de octava", "soliton microcomb octave-spanning" o
"DKS con onda dispersiva". La palabra "supercontinuo" se reserva (i) para el ensanchamiento de un solo paso en una
guía/fibra externa que a veces se añade al microcomb, y (ii) para el término específico **"resonant
supercontinuum"** (Anderson, Kippenberg et al., Optica 2021) que designa un microresonador Kerr excitado con
*pulsos* de picosegundos, no con CW. No encontré ningún artículo revisado por pares que use exactamente
"cavity-enhanced supercontinuum" para microanillos.

### Cited Findings
- Brasch et al. (Science 2016) describen el resultado como "fully coherent optical frequency comb spanning two-thirds
  of an octave" generado por "soliton Cherenkov radiation"; presentan la emisión de ondas dispersivas como "one of
  the key nonlinear frequency conversion mechanisms of coherent supercontinuum generation" en fibras de cristal
  fotónico, y afirman que en el microresonador "this regime therefore makes external broadening superfluous" —
  es decir, el proceso físico es el del supercontinuo pero no llaman "supercontinuo" al espectro del anillo —
  [Brasch et al. 2016, Science 351, 357](https://doi.org/10.1126/science.aad4811) (texto vía
  [arXiv:1410.8598](https://arxiv.org/abs/1410.8598)).
- Pfeiffer et al. (Optica 2017), el primer DKS de octava completa en Si₃N₄, **no usa la palabra "supercontinuum"**
  en todo el texto; usa "nonlinear spectral broadening" y "Kerr frequency comb" —
  [Pfeiffer et al. 2017, Optica 4, 684](https://doi.org/10.1364/OPTICA.4.000684) (texto vía
  [arXiv:1701.08594](https://arxiv.org/abs/1701.08594)).
- La revisión 2026 de Herr, Tikan y Kippenberg (70 páginas) usa "supercontinuum" **una sola vez y por contraste**:
  las ondas dispersivas de la NLS generalizada no resonante describen "supercontinua in single-pass waveguides",
  a diferencia de la onda dispersiva co-propagante del resonador —
  [Herr, Tikan & Kippenberg 2026, arXiv:2604.05897](https://arxiv.org/abs/2604.05897) (preprint, sin DOI de revista).
- El término **"resonant supercontinuum"** lo introducen Anderson et al. (Optica 2021) para un microresonador de
  Si₃N₄ (FSR 27.88 GHz, Q cargado 1.8±0.3×10⁶, κ/2π = 110 MHz, sección 2350×770 nm²) excitado con pulsos de ~1 ps y
  potencia pico de 0.6–6 W (energía 0.6–6 pJ), definido como "a synthesis between conventional SCG and soliton
  microcombs": 2200 líneas, 2/3 de octava (64 THz, ~600 nm), onda dispersiva en 1957 nm, eficiencia 8 % (estado de
  9.5 THz) y 2.8 % (estado ancho); potencia pico ~100× menor que el SC convencional en Si₃N₄ (~100 fs, ~1 kW) —
  [Anderson et al. 2021, Optica 8, 771](https://doi.org/10.1364/OPTICA.403302) (texto vía
  [arXiv:1909.00022](https://arxiv.org/abs/1909.00022)).
- Precedente directo del bombeo pulsado: Obrzud, Lecomte & Herr, "Temporal solitons in microresonators driven by
  optical pulses" — [Nat. Photon. 11, 600 (2017)](https://doi.org/10.1038/nphoton.2017.140).
- El uso de "supercontinuo" como **etapa externa** de ensanchamiento del microcomb: Lamb et al., "Optical-frequency
  measurements with a Kerr microcomb and photonic-chip supercontinuum", donde una guía de Si₃N₄ ensancha el
  microcomb a 700–2100 nm — [Phys. Rev. Applied 9, 024030 (2018)](https://doi.org/10.1103/PhysRevApplied.9.024030);
  Herr et al. 2014 ya hacían lo mismo con 2 m de fibra altamente no lineal tras amplificar a 3.2 W un peine de
  14.1 GHz, obteniendo "close to two thirds of an octave" —
  [Herr et al. 2014, Nat. Photon. 8, 145](https://doi.org/10.1038/nphoton.2013.343).
- Un preprint de 2025 sobre microanillos de SiC separa explícitamente "waveguide-based supercontinuum generation
  (SCG)" de "microresonator-based Kerr comb generation (KCG)" como dos rutas distintas —
  [arXiv:2512.16588](https://arxiv.org/abs/2512.16588) (preprint; sin DOI de revista; no leí el texto completo).
- Uso temprano, antes de los solitones: Del'Haye et al. 2011 "Octave spanning tunable frequency comb from a
  microresonator" (MgF₂/sílice, FSR 850 GHz) y Okawachi et al. 2011 "Octave-spanning frequency comb generation in
  a silicon nitride chip" (FSR 226 GHz) — ambos con peines de octava **incoherentes/no solitónicos** (ver §3) —
  [PRL 107, 063901](https://doi.org/10.1103/PhysRevLett.107.063901);
  [Opt. Lett. 36, 3398](https://doi.org/10.1364/OL.36.003398).
- Puente conceptual: Skryabin & Gorbach, "Looking at a soliton through the prism of optical supercontinuum", RMP
  2010, establece que la radiación Cherenkov del solitón es el mecanismo central del SC de fibra —
  [Rev. Mod. Phys. 82, 1287](https://doi.org/10.1103/RevModPhys.82.1287).

### Inferences
- Para la bitácora y el informe del proyecto: lo correcto es escribir "peine de solitón Kerr disipativo de banda
  ancha (de octava) asistido por ondas dispersivas" y, si se usa "supercontinuo", aclarar que se emplea por analogía
  con el mecanismo (solitón + radiación Cherenkov) y no como el término estándar del campo. Si el bombeo fuera
  pulsado, el término normalizado es "resonant supercontinuum" (Anderson 2021).
- La ausencia de "cavity-enhanced supercontinuum" en la literatura de microanillos indica que el concepto de
  "realce por cavidad" aparece en la literatura con otras palabras: "finesse", "cavity enhancement of the pump" y
  el hecho de que la condición de fase de la onda dispersiva incluya el detuning (ver §2 y §5).

### Gaps
- No pude confirmar si alguna conferencia (CLEO, etc.) ha usado literalmente "cavity-enhanced supercontinuum" para
  microanillos; la búsqueda con la frase exacta no devolvió ninguna fuente revisada.
- No leí el texto completo de arXiv:2512.16588; su clasificación SCG/KCG viene del resumen de búsqueda.

---

## 2. ¿Cómo extiende el espectro la radiación Cherenkov del solitón / emisión de ondas dispersivas? Condiciones de ajuste de fase en términos de D_int(μ)

### Takeaway
Un DKS con dispersión puramente anómala (solo D₂) tiene un espectro sech² y no puede radiar; cuando D₃, D₄ o un
cruce de modos hacen que D_int(μ) vuelva a cruzar la "línea del solitón", el solitón se ajusta en fase con un modo
lineal lejano y transfiere energía a una onda dispersiva (OD) co-propagante que aparece como un pico local en el
espectro cerca de D_int(μ) ≈ 0 (más exactamente, D_int(μ) ≈ ω₀ − ω_p + corrección de velocidad de grupo). Con D₄ < 0
dominante hay dos raíces y por tanto dos OD (una por lado), que es la receta estándar para el peine de octava
autorreferenciable (f–2f).

### Cited Findings
- Definición: D_int(μ) ≡ ω_μ − (ω₀ + D₁μ) = D₂μ²/2! + D₃μ³/3! + …, "la desviación de las frecuencias de los modos
  respecto a una rejilla equidistante definida por ω₀ y D₁"; D₂ = −(c/n) D₁² β₂ —
  [Brasch et al. 2016](https://doi.org/10.1126/science.aad4811).
- Ajuste de fase lineal (D₄ = 0): la OD está donde D_int(μ) = 0, i.e. μ_DW = −3D₂/D₃; el punto de dispersión cero
  (D″_int = 0) es μ_ZDP = −D₂/D₃. Con D₄: μ_DW ≈ −2D₃/D₄ ± √((2D₃/D₄)² − 12D₂/D₄). Medido: OD en μ = 195 frente al
  estimado lineal μ_DW ≈ 200 — [Brasch et al. 2016](https://doi.org/10.1126/science.aad4811).
- Números de Brasch 2016 (Si₃N₄, 800 nm de espesor, anillo de 238 µm de diámetro): FSR 189.2 GHz; κ/2π ≈ 300 MHz;
  D₂/2π = 2.4±0.1 MHz (medido), D₃/2π ≈ 24.5 kHz y D₄/2π ≈ −290 Hz (FEM); bomba 1560 nm, ~2 W en la guía de bus para
  solitón único (umbral paramétrico 300 mW; simulación con 1 W y ζ = 12); peine 150–225 THz (2/3 de octava); OD en
  ~155 THz (~1930 nm); ancho a 3 dB del sech² 10.8 THz; duración < 30 fs (≈ 6 ciclos ópticos); energía del solitón
  0.1 nJ dentro del resonador — [Brasch et al. 2016](https://doi.org/10.1126/science.aad4811).
- Teoría analítica con D₃ (Cherenkov, Lobanov & Gorodetsky, PRA 2017), válida para ζ₀ ≫ 1 y f/ζ₀ ≪ 1:
  - posición de la OD: μ_d = −3D₂/D₃ − (D₃κ/(3D₂²))·[2ζ₀ − 2(f/ζ₀)² − i]; corrimiento respecto al punto de
    dispersión cero δμ_d ≈ −(2D₃κ/(3D₂²)) ζ₀; ancho de línea lorentziano Δ_d = 2D₃κ/(3D₂²);
  - intensidad de la OD: |a_d|² ≈ 2D₃ ζ₀^{3/2} / (3π² √(κD₂));
  - retroceso espectral (recoil) del solitón: μ_r = ζ₀ D₃κ/(3D₂²), con |a_{μ_r}|² ≈ D₂/(2κ);
  - cambio de velocidad de grupo / tasa de repetición: Ω_DW = ζ₀ κ D₃/(6D₂) (según la revisión 2026, Eq. 87) —
  [Cherenkov, Lobanov & Gorodetsky 2017, PRA 95, 033810](https://doi.org/10.1103/PhysRevA.95.033810) (texto vía
  [arXiv:1702.08750](https://arxiv.org/abs/1702.08750)); reproducido en
  [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897).
- Revisión 2026: "A DW forms when the DKS becomes phase-matched to a resonance, i.e., when the soliton line crosses
  the dispersion profile. This cannot happen with pure anomalous D2"; efectos: realce local de potencia de las
  líneas en el cruce y desplazamiento del centro espectral del DKS lejos de la OD ("spectral recoil"); en el dominio
  temporal la OD es "an oscillatory tail that co-moves with the soliton"; la TOD además reduce la región de
  inestabilidad dinámica del DKS; D₄ negativa "reduces D_int in the comb wings, which flattens the spectrum or
  produces dual DWs" — [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897).
- Pfeiffer 2017: "the spectral positions of DWs are thus approximately given by the linear phase matching criterion
  D_int = 0"; "For dominant, negative fourth-order dispersion D4 two DW positions can be engineered, causing dual
  dispersive wave emission"; sensibilidad: "a waveguide height deviation of only 10 nm causes a shift of the low
  frequency dispersive wave position by 5 THz" — [Pfeiffer et al. 2017](https://doi.org/10.1364/OPTICA.4.000684).
- Números de Pfeiffer 2017 (Si₃N₄, guía 1.425 µm × ~0.74 µm, FSR ≈ 1 THz, κ₀/2π = 100 MHz, 𝓕 ≈ 10⁴, D₂/2π ∼ 20 MHz):
  solitón único a 1.55 µm con 455 mW en el bus, ancho a 3 dB 24.85 THz (pulso 12.7 fs), detuning ≈ 7 GHz; a 1.3 µm
  con 245 mW, peine > 200 THz (OD de alta frecuencia en 850 nm), ancho a 3 dB 19.9 THz; ambos "excited in direct
  vicinity of an avoided modal crossing" — [Pfeiffer et al. 2017](https://doi.org/10.1364/OPTICA.4.000684).
- Li et al. 2017 (Si₃N₄ sin revestimiento superior, radio 23 µm, FSR ≈ 1 THz, Q_c/Q_i ≈ 6×10⁵/1×10⁶): dispositivo 1
  (1760×603 nm, D₂/2π = 25±2 MHz) con OD en ~1.06 µm y ~2.06 µm → una octava con ~40 mW (estado multisolitón);
  dispositivo 2 (1750×623 nm, D₂/2π = 53±2 MHz) con una sola OD larga en ~2.27 µm → más de una octava, solitón único
  con ~120 mW — [Li et al. 2017, Optica 4, 193](https://doi.org/10.1364/OPTICA.4.000193).
- Primera teoría de OD de solitones de cavidad en microanillos cerca de GVD cero (Milián & Skryabin 2014), y la
  extensión con Raman + dispersión de orden superior en anillos de sílice (Milián, Gorbach & Skryabin 2015), que
  afirma que "both types of solitons can emit resonant radiation contributing into shaping of frequency combs" —
  [Opt. Express 22, 3732 (2014)](https://doi.org/10.1364/OE.22.003732);
  [Phys. Rev. A 92, 033851 (2015)](https://doi.org/10.1103/PhysRevA.92.033851).
- Ondas dispersivas inducidas por **cruce de modos espaciales** (no por D₃/D₄): Yang, Yi, Yang & Vahala 2016, en
  sílice (diámetro 3 mm, FSR 22 GHz, Q_int > 3×10⁸, D₂A/2π = 15.2 kHz, D₃A/2π = −14.7 Hz, acoplamiento intermodal
  G/2π = 106.5 MHz, cruce fuerte cerca de μ = 165): OD con máximo en 198.62 THz (μ = 235); el retroceso por la OD es
  despreciable (potencia de la OD < 0.2 % de la del solitón) y el ajuste fino de la OD lo da el SSFS Raman —
  [Optica 3, 1132 (2016)](https://doi.org/10.1364/OPTICA.3.001132).
- Estado del arte 2024–2026 de OD duales de diseño: Zang, Liu, Briles & Papp 2024 (fundición Ligentec, Si₃N₄
  760 nm, FSR ≈ 1 THz, Q_i ≈ 1.4×10⁶ en el modelo, bomba C ~150 mW en chip): OD en 145.43 THz y 290.92 THz (f–2f),
  D_int definido como ν_μ − (ν₀ + FSR·μ) con "DWs appear at D_int ≈ 0"; las OD se sintonizan con el ancho del anillo
  y f_ceo con el radio ("1 nm uncertainty in t_h requires 5 nm sweep in RW to compensate") —
  [Opt. Lett. 49, 5143 (2024)](https://doi.org/10.1364/OL.527540) (texto vía
  [arXiv:2404.13472](https://arxiv.org/abs/2404.13472)). Li et al. 2026 (Xue group): resonadores
  heteroestructurados de Si₃N₄ (secciones de guía distintas unidas adiabáticamente) para "synthesize the global
  effective dispersion coefficients", peines de octava con f_rep tan baja como 118 GHz y OD sintonizable de forma
  determinista en 290–310 THz — [arXiv:2608.09005](https://arxiv.org/abs/2608.09005) (preprint, sin DOI de revista).
- Vía alternativa no dispersiva de extensión: Moille et al. 2021, "soliton spectral translation" por FWM-Bragg con un
  segundo bombeo (1063 y 1557 nm) → 137–407 THz (1.6 octavas en la versión publicada; "approaching two octaves" en
  el preprint) — [Nat. Commun. 12, 7275 (2021)](https://doi.org/10.1038/s41467-021-27469-0).
- Origen en fibra del concepto: Akhmediev & Karlsson 1995, "Cherenkov radiation emitted by solitons in optical
  fibers" — [Phys. Rev. A 51, 2602](https://doi.org/10.1103/PhysRevA.51.2602).

### Inferences
- La condición práctica de diseño es D_int(μ_DW) ≈ 0 corregida por el detuning (≈ ω₀ − ω_p en unidades angulares) y
  por la inclinación de la línea del solitón: Cherenkov et al. muestran que para ζ₀ ≫ 1 la OD se desplaza del cero
  de D_int en δμ ≈ −(2D₃κ/3D₂²)ζ₀, es decir, la OD se mueve con el detuning (y por tanto con la potencia del
  solitón). Esto es exactamente lo que no existe en el SC de un solo paso, donde la condición solo involucra β(ω) y
  la velocidad de grupo del solitón.
- La fuerte dependencia de la OD con la geometría (5 THz por 10 nm de espesor en Pfeiffer; 1 nm de espesor ⇔ 5 nm
  de ancho en Zang) implica que, para el anillo del proyecto, un barrido de D_int(μ) con FDE sobre tolerancias de
  fabricación es un entregable necesario antes de prometer una posición de OD.

### Gaps
- No obtuve los valores numéricos de D₃ y D₄ de Pfeiffer 2017 ni los de Zang 2024 (no los reportan explícitamente
  en el texto consultado).
- Zang 2024 (Opt. Lett. 49, 5143; DOI verificado) no reporta en el texto consultado el Q cargado medido ni el
  número total de dispositivos probados.

---

## 3. Leyes de escala que ligan el ancho de banda del solitón (sech², 3 dB) con β₂/D₂, γ, detuning y Q

### Takeaway
El solitón único de la LLE tiene envolvente de campo Ψ ≃ √(2ζ₀) sech(√(2ζ₀/d₂)·φ) y espectro sech² cuyo ancho
crece como √(ζ₀/D₂): más detuning rojo y menos dispersión ⇒ más ancho. Como el detuning máximo es ζ₀^max = π²f²/8,
el ancho máximo escala como √(P_in·𝓕·γ/|β₂|) y es **independiente del FSR** (Coen & Erkintalo 2013); el Q entra solo
a través de la finesse/potencia intracavidad. El límite superior lo pone la dispersión de orden superior (OD), no
la fórmula sech².

### Cited Findings
- Herr et al. 2014 (ec. 1 del texto principal): Ψ(φ) ≃ C₁ + C₂ Σ_j sech(√(2(ω₀ − ω_p)/D₂) (φ − φ_j)); en forma
  adimensional Ψ ≃ Ψ₀ + B e^{iφ₀} sech(Bθ), B ≃ √(2ζ₀), cos φ₀ ≃ √(8ζ₀)/(πf); existencia hasta ζ₀^max = π²f²/8.
  Espectro: Ψ(ω − ω_p) = √(d₂/2) sech((ω − ω_p)/Δω), Δω = (2D₁/π)√(ζ₀/d₂) (con d₂ = D₂/κ en ese artículo); perfil
  temporal Ψ(t) = √(2ζ₀) sech(t/Δt), Δt = (1/D₁)√(d₂/ζ₀); Δt·Δω = 2/π; para FWHM multiplicar Δt y Δω por
  2 arccosh(√2) ≈ 1.763; TBP(FWHM) = 0.315. Duración mínima: Δt_min = (1/(πD₁))√(κD₂n₀²V_eff/(ηP_in ω₀ c n₂))
  ≈ (2/√π)√(−β₂/(γ𝓕P_in)) (SI) ≈ 2√(−β₂/(γ𝓕P_in)) (texto principal; prefactores no reconciliados en el artículo) —
  [Herr et al. 2014, Nat. Photon. 8, 145](https://doi.org/10.1038/nphoton.2013.343) (texto vía
  [arXiv:1211.0733](https://arxiv.org/abs/1211.0733)).
- Números de Herr 2014 (MgF₂): FSR 35.2 GHz, κ/2π = 450 kHz, Q ≈ 4×10⁸, 𝓕 ≈ 7.8×10⁴, D₂/2π = 16 kHz
  (β₂ = −9.39 ps²/km), n₂ = 0.9×10⁻²⁰ m²/W, γ = 4.1×10⁻⁴ m⁻¹W⁻¹, A_eff = 90 µm², P_in = 5–30 mW acoplados (potencia
  circulante "several hundreds of Watts"), ancho a 3 dB 1.6 THz (> 45 modos), pulso ≈ 200 fs (FROG), TBP 0.315 —
  [Herr et al. 2014](https://doi.org/10.1038/nphoton.2013.343).
- Revisión 2026 (misma física, normalización d₂ = 2D₂/κ): ψ_μ = √(D₂/2κ) sech[(πμ/2)√(D₂/(ζ₀κ))]; potencia por modo
  P(μ) ≈ (κ_ex D₂ ħω₀/(4g_K)) sech²[(πμ/2)√(D₂/(2(ω₀ − ω_p)))]; Δω = (2D₁/π)√(ζ₀κ/D₂); Δt = (1/D₁)√(D₂/(ζ₀κ));
  Δω_max = 2/(πΔt_min). Nota: la amplitud y el ancho "both grow with detuning, reaching their maximum at the end of
  the existence range" — [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897).
- Coen & Erkintalo 2013, LLE normalizada ∂E/∂t = [−1 + i(|E|² − Δ) − iη∂²/∂τ²]E + S con η = sgn(β₂), Δ = δ₀/α,
  X = |S|², "Δ is formally identical to the ζ₀ parameter" de Herr: E_CS ≃ √(2Δ) sech(√Δ τ), Y_peak ≃ 2Δ,
  Δτ_FWHM ≃ 1.763/√Δ, existencia hasta "about π²X/8"; ancho a 3 dB (bomba en resonancia Δ = X, acoplamiento
  crítico): **Δf_theo = (0.315/1.763)·√(2γP_in Q λ_p FSR/(π c|β₂|)) = (0.315/1.763)·√(2γP_in𝓕/(π|β₂|))**, con
  𝓕 = π/α; conclusión: la aptitud de un resonador para peines anchos "is determined solely by its finesse (or
  losses), nonlinearity, and GVD coefficient" y es "independent of its FSR". Límite por D₃:
  Δf_DW = 3|β₂|/(2πβ₃) y Δf_lim = 2Δf_DW —
  [Coen & Erkintalo 2013, Opt. Lett. 38, 1790](https://doi.org/10.1364/OL.38.001790) (texto vía
  [arXiv:1303.7078](https://arxiv.org/abs/1303.7078)).
- Validación de la ley (Tabla 1 de Coen & Erkintalo): Herr 2014 (MgF₂, 35.2 GHz, Q 4×10⁸) 1.6 THz medido /
  1.59 THz teórico; Del'Haye 2007 (sílice toroide, 882 GHz, Q 10⁸) 31 / 36.4 THz; Okawachi 2011 (Si₃N₄, 226 GHz,
  Q 3×10⁵, 𝓕 350) 10 / 15.6 THz; Grudinin (18.2 GHz, Q 1.9×10⁹) 0.6 / 0.71 THz; Del'Haye 2011 (850 GHz, Q 2.7×10⁸)
  40 THz medido / 388 THz teórico — el último es una sobreestimación atribuida a la dispersión de orden superior
  (el valor observado cae sobre el límite Δf_lim) — [Coen & Erkintalo 2013](https://doi.org/10.1364/OL.38.001790).
- Lucas et al. 2017 verifican experimentalmente τ ≈ (1/D₁)√(D₂/(2δω)) (δω detuning efectivo) con acuerdo al 1 %,
  "the comb bandwidth depends only on the free spectral range, dispersion, and detuning"; también observan
  respiración (breathing) en cruces de modos — [Phys. Rev. A 95, 043822 (2017)](https://doi.org/10.1103/PhysRevA.95.043822)
  (texto vía [arXiv:1609.02723](https://arxiv.org/abs/1609.02723)).
- Umbral y escalado del bombeo: la revisión 2026 da g_K = ħω₀²cn₂/(n_eff²V_eff), f² = |s_in|²(8ηg_K/κ²) con
  |s_in|² = P_in/(ħω_p), 𝓕 = 2πFSR/κ; y las relaciones de umbral paramétrico γ/κ > f²/8 y f²_th = 4γ/κ + κ/γ (allí γ es
  la tasa de ganancia paramétrica) — [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897). Brasch
  2016: umbral paramétrico 300 mW en la guía para κ/2π ≈ 300 MHz, 189 GHz —
  [Brasch et al. 2016](https://doi.org/10.1126/science.aad4811).
- Anchos a 3 dB reportados en Si₃N₄ (comparar con MgF₂): 5.5 THz (Karpov 2016, FSR 100 GHz, D₂/2π = 1–2 MHz,
  bomba 1–3 W) — [PRL 116, 103902](https://doi.org/10.1103/PhysRevLett.116.103902); 10.8 THz (Brasch 2016, 189 GHz,
  D₂/2π = 2.4 MHz, ~2 W); 24.85 THz / 12.7 fs (Pfeiffer 2017, 1 THz, D₂/2π ∼ 20 MHz, 455 mW); 9.5 THz y 64 THz
  (Anderson 2021, 28 GHz, pulsado).
- Eficiencia de conversión bomba→peine en DKS CW: "1–5 %", porque la bomba está muy desintonizada —
  [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897); teoría: Bao et al., "Nonlinear conversion
  efficiency in Kerr frequency comb generation" — [Opt. Lett. 39, 6126 (2014)](https://doi.org/10.1364/OL.39.006126);
  Xue et al. (dispersión normal, alta eficiencia) — [Laser Photon. Rev. 11, 1600276 (2017)](https://doi.org/10.1002/lpor.201600276).

### Inferences
- Combinando Δω ∝ √(ζ₀κ/D₂) con ζ₀^max = π²f²/8 y f² ∝ ηP_in/κ², el ancho máximo escala como √(ηP_in/(κD₂)) ∝
  √(P_in·Q/D₂) para FSR fijo: duplicar Q o P_in da solo √2 más ancho; reducir D₂ (dispersión casi plana) es la
  palanca más fuerte, pero D₂ muy pequeña hace dominar D₃/D₄ y la OD (límite Δf_lim de Coen & Erkintalo, y la
  condición de Herr 2014 PRL de que "nonzero values of D3 require a minimal magnitude of the coefficient D2").
- Los sistemas de octava reales (Li, Pfeiffer, Zang) tienen FSR ≈ 1 THz no porque el ancho sech² dependa del FSR
  (no depende), sino porque (a) el número de líneas necesario es menor, (b) con pocos modos la potencia por línea
  en las OD es detectable y (c) la eficiencia CW cae al bajar f_rep (Anderson 2021: "good conversion efficiency
  only at vastly higher repetition rates close to 1 THz").

### Gaps
- Herr 2014 no reporta el valor numérico del detuning experimental de sus estados de solitón; Brasch 2016 solo da
  ζ = 12 en simulación.
- El prefactor de Δt_min difiere entre el texto principal y el SI de Herr 2014 (2 vs 2/√π); no encontré una errata.

---

## 4. Normalizaciones de la LLE, mapa de Ikeda y ecuaciones de modos acoplados; papel de la dispersión normal vs anómala en la extensión espectral

### Takeaway
Los tres marcos son equivalentes en el límite de campo medio: las ecuaciones de modos acoplados (CME) en el
dominio de μ son la transformada de Fourier de la LLE en φ; la LLE se obtiene promediando el mapa de Ikeda sobre una
vuelta (válido para alta finesse y pequeño cambio por vuelta); el mapa de Ikeda es necesario para finesse baja o
detuning grande. En dispersión anómala el estado localizado es el DKS brillante (espectro sech², el más ancho); en
dispersión normal son ondas de conmutación / pulsos oscuros (platicones), con mayor eficiencia pero "generally not
the wide spectral span" del DKS; en dispersión cero aparecen los solitones de dispersión cero (ZDS) y en D₂ ≈ 0 con
D₄ los solitones cuárticos puros con espectro plano.

### Cited Findings
- LLE dimensional (revisión 2026, Eq. 50): ∂A/∂t = −(κ/2 + i(ω₀ − ω_p))A + i(D₂/2)∂²A/∂φ² + i g_K|A|²A + √κ_ex s_in;
  adimensional (Eq. 53): ∂Ψ/∂τ = −(1 + iζ₀)Ψ + i(d₂/2)∂²Ψ/∂φ² + i|Ψ|²Ψ + f, con τ = κt/2, d₂ = 2D₂/κ,
  ζ₀ = 2(ω₀ − ω_p)/κ, f = √(P_in/P_th), A = √(κ/2g_K) Ψ; con θ = φ/√|d₂| queda ∂Ψ/∂τ = −(1 + iζ₀)Ψ +
  i(sgn d₂/2)∂²Ψ/∂θ² + i|Ψ|²Ψ + f. Los DKS aparecen para bomba efectivamente al rojo: ζ₀ − Σ_μ|ψ_μ|² > 0 —
  [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897).
- Forma de Herr 2014 (SI Eq. 8): i∂Ψ/∂τ + ½∂²Ψ/∂θ² + |Ψ|²Ψ = (−i + ζ₀)Ψ + if, con θ = φ√(1/(2d₂)) y d₂ = D₂/κ
  (factor 2 distinto respecto a la revisión 2026) — [Herr et al. 2014](https://doi.org/10.1038/nphoton.2013.343).
- CME (Herr 2014 SI Eq. 3): ∂A_μ/∂t = −(κ/2)A_μ + δ_{μ0}√(ηκ) s_in e^{−i(ω_p−ω₀)t} + ig Σ A_μ'A_μ''A*_μ''' e^{−i(ω_μ'+ω_μ''−ω_μ'''−ω_μ)t},
  g = ħω₀²cn₂/(n₀²V_eff); normalizadas: ∂a_μ/∂τ = −[1 + iζ_μ]a_μ + iΣ_{μ'≤μ''}(2 − δ_{μ'μ''}) a_μ'a_μ''a*_{μ'+μ''−μ} +
  δ_{0μ}f, con ζ_μ = 2(ω_μ − ω_p − μD₁)/κ (es decir, ζ_μ = ζ₀ + 2D_int(μ)/κ) — [Herr et al. 2014](https://doi.org/10.1038/nphoton.2013.343).
- Términos de orden superior en la LLE (Cherenkov et al. 2017, Eq. 1): iΨ_T + ½Ψ_zz + |Ψ|²Ψ − ζ₀Ψ = −iΨ +
  Σ_{k>2}(−i)^k d_k ∂^kΨ/∂z^k + if, con d_k = D_k·(2/(κk!))·(κ/(2D₂))^{k/2}, z = φ√(κ/(2D₂)) —
  [PRA 95, 033810](https://doi.org/10.1103/PhysRevA.95.033810).
- Convención de fibra (Coen & Erkintalo 2013): t → αt/t_R, τ → τ(2α/|β₂|L)^{1/2}, E → E(γL/α)^{1/2}, t_R = 1/FSR,
  α = (α_iL + θ)/2, S = E_in(γLθ/α³)^{1/2}, Δ = δ₀/α; biestabilidad X = Y³ − 2ΔY² + (Δ² + 1)Y; umbral MI X = 1;
  Δ_MI = 1 − √(X − 1); punto de conmutación Δ↑ ≃ 3(X/4)^{1/3} — [Opt. Lett. 38, 1790](https://doi.org/10.1364/OL.38.001790).
- Formalismo LLE espaciotemporal para peines Kerr en WGM (Chembo & Menyuk 2013) y equivalencia con las CME —
  [Phys. Rev. A 87, 053852](https://doi.org/10.1103/PhysRevA.87.053852). Primera predicción de solitones
  (peines "mode-locked") en microresonadores: Matsko et al. 2011 —
  [Opt. Lett. 36, 2845](https://doi.org/10.1364/OL.36.002845).
- LLE generalizada con dispersión de orden superior para peines de octava, resuelta por Newton–Raphson; "Kerr
  combs are associated with temporal cavity solitons and dispersive waves" (Coen, Randle, Sylvestre & Erkintalo) —
  [Opt. Lett. 38, 37 (2013)](https://doi.org/10.1364/OL.38.000037) (Crossref registra fecha en línea de 2012).
- Mapa de Ikeda vs LLE: la LLE "can be derived by averaging the Ikeda map over one roundtrip" y "is not valid for
  large parameter regimes, where the full Ikeda map is needed" (resumen de búsqueda de trabajos del grupo
  Erkintalo/Murdoch, p. ej. [arXiv:1702.00782](https://arxiv.org/abs/1702.00782)); origen histórico de la LLE para
  anillos de fibra: Haelterman, Trillo & Wabnitz 1992 — [Opt. Commun. 91, 401](https://doi.org/10.1016/0030-4018(92)90367-Z).
- Dispersión normal: pulsos oscuros mode-locked (Xue et al. 2015) — [Nat. Photon. 9, 594](https://doi.org/10.1038/nphoton.2015.137);
  revisión 2026: las ondas de conmutación conectan los dos estados homogéneos, se estabilizan por oscilaciones
  interlocked cerca del punto de Maxwell, tienen eficiencia "much higher" que el DKS pero "do generally not achieve
  the wide spectral span" del DKS; solitones de dispersión cero (ZDS) con pico de potencia menor y estructuras
  multipico; solitones cuárticos puros (PQS, D₂ = 0, D₄ ≠ 0) con A₀ = √((8√2/7)(ω₀ − ω_p)/g_K) y
  w = ½·⁴√((7/2)D₄/(ω₀ − ω_p)), espectro plano "over many modes" —
  [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897); ZDS experimentales: Anderson et al. 2022 —
  [Nat. Commun. 13, 4764](https://doi.org/10.1038/s41467-022-31916-x).
- Criterio experimental Herr et al. PRL 2014: "the decisive requirement for the generation of solitons is the
  anomalous resonator dispersion"; "higher order dispersion can be tolerated as long as it does not dominate" —
  [PRL 113, 123901](https://doi.org/10.1103/PhysRevLett.113.123901).
- Breathers: la respiración nace en una bifurcación de Hopf y "breathers periodically radiate dispersive waves" —
  [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897); dinámica de solitones de cavidad 1D (Leo et al.
  2013) — [Opt. Express 21, 9180](https://doi.org/10.1364/OE.21.009180).

### Inferences
- Para el anillo del proyecto, el modelo mínimo que captura la extensión espectral es la LLE con D_int(μ) completo
  (D₂…D₄ o directamente la curva FDE de ω_μ) en el dominio de μ, porque ζ_μ = ζ₀ + 2D_int(μ)/κ hace inmediato el
  criterio de la OD (ζ_μ ≈ 0 para algún μ ≠ 0). El mapa de Ikeda solo sería necesario si κ/FSR dejara de ser ≪ 1
  (finesse baja), lo que no ocurre en Si₃N₄ con 𝓕 ~ 10³–10⁴.
- Cuidado con el factor 2 en d₂ entre Herr 2014 (d₂ = D₂/κ) y la revisión 2026 / Cherenkov 2017 (d₂ = 2D₂/κ) al
  reutilizar fórmulas de ancho; las fórmulas dimensionales (Δω = (2D₁/π)√(2(ω₀ − ω_p)/D₂)) son las seguras.

### Gaps
- No leí el texto completo de Chembo & Menyuk 2013 ni de Xue 2015; solo verifiqué su existencia y DOI.
- No obtuve del texto consultado de Coen 2013 (OL 38, 37) la condición explícita de validez del campo medio.

---

## 5. Supercontinuo realzado por cavidad en anillos de fibra y cavidades Kerr pasivas (Coen, Erkintalo, Haelterman): qué enseñan y qué se transfiere a los microanillos

### Takeaway
Las cavidades de fibra pasiva son el laboratorio "a escala" de la LLE: con 𝓕 ~ 20, β₂, β₃ y γ de fibra, mostraron
primero (i) la inestabilidad de modulación disipativa (Haelterman 1992), (ii) los solitones de cavidad temporales
(Leo 2010), (iii) la emisión de OD por solitones de cavidad con una condición de fase que **incluye el detuning y la
potencia de fondo** (Jang 2014), (iv) la coherencia de los peines Kerr evaluada con g⁽¹⁾ (Erkintalo & Coen 2014) y
(v) el límite Raman al ancho de banda (Wang 2018). Todo ello se transfiere a microanillos vía las mismas ecuaciones
normalizadas (Δ ≡ ζ₀, X ≡ f²).

### Cited Findings
- Jang, Erkintalo, Murdoch & Coen 2014: primera observación directa de OD emitidas por solitones de cavidad
  temporales, en un anillo de fibra con 94.5 m de DSF + 10.4–16.0 m de SMF, 𝓕 ≈ 18 (α = 0.176), bomba CW 1550 nm a
  1–1.3 W, fondo P₀ ≈ 500–600 mW, δ₀ = 0.5–0.56 rad, ⟨β₂⟩ de −0.23 a −1.23 ps²/km, ⟨β₃⟩ ≈ 0.19 ps³/km, γ ≈ 1.9 W⁻¹km⁻¹,
  solitón ≈ 650 fs. Condición de fase (Eq. 2): β₃L/3!·Q³ + β₂L/2!·Q² − VQ + [(2γLP₀ − δ₀) + iα] = 0 — el detuning
  entra vía (2γLP₀ − δ₀), "the peak power of the temporal CS does not play any direct role", Re(Q) da el
  desplazamiento de la OD e Im(Q) el decaimiento de su cola; OD medida ~1541.1–1541.4 nm vs predicción 1540.9–1541.3 nm;
  "our results are likely to explain the origins of spectral features observed in broadband Kerr frequency combs" —
  [Opt. Lett. 39, 5503 (2014)](https://doi.org/10.1364/OL.39.005503) (texto vía [arXiv:1406.2046](https://arxiv.org/abs/1406.2046)).
- Haelterman, Trillo & Wabnitz 1992: "Dissipative modulation instability in a nonlinear dispersive ring cavity" —
  deducción de la LLE para el anillo de fibra — [Opt. Commun. 91, 401](https://doi.org/10.1016/0030-4018(92)90367-Z).
- Leo et al. 2010: solitones de cavidad temporales en fibra como bits de un buffer todo óptico —
  [Nat. Photon. 4, 471](https://doi.org/10.1038/nphoton.2010.120).
- Erkintalo & Coen 2014: coherencia de peines Kerr cuantificada con el grado complejo de coherencia de primer orden
  calculado como promedio de conjunto sobre campos de salida separados por un número fijo de vueltas, en el marco de
  la LLE — [Opt. Lett. 39, 283 (2014)](https://doi.org/10.1364/OL.39.000283); confirmación experimental por
  interferometría espectral en microresonador: Webb et al. 2016 — [Opt. Lett. 41, 277](https://doi.org/10.1364/OL.41.000277).
- Wang, Anderson, Coen, Murdoch & Erkintalo 2018: el SRS "imposes fundamental limits to the duration and bandwidth
  of temporal cavity solitons": introduce una bifurcación de Hopf que desestabiliza el solitón a detunings grandes
  y recorta el rango de existencia; verificado en anillos de fibra con bombeo sincrónico; relevante para
  "amorphous microresonators" como sílice — [PRL 120, 053902](https://doi.org/10.1103/PhysRevLett.120.053902).
- Coen & Erkintalo 2013 muestran que la *misma* LLE normalizada describe desde fibra (𝓕 ~ 20) hasta cristalinos
  (𝓕 ~ 10⁶) y que la predicción de ancho solo depende de 𝓕, γ, β₂ y P_in —
  [Opt. Lett. 38, 1790](https://doi.org/10.1364/OL.38.001790).
- Referencia de comparación para el SC de un solo paso (fibra PCF): Dudley, Genty & Coen 2006 —
  [Rev. Mod. Phys. 78, 1135](https://doi.org/10.1103/RevModPhys.78.1135).

### Inferences
- Lo que "realza la cavidad" no es la potencia pico del solitón sino tres cosas: (a) la bomba CW de mW se convierte
  en un fondo intracavidad de W (P_circ ≈ 𝓕P_in/π), (b) el solitón se reconstruye cada vuelta (estado estacionario,
  disipativo), y (c) la condición de fase de la OD depende del detuning/fondo, lo que permite **sintonizar la OD
  con el láser** (confirmado en microanillos por Yang 2016 y Cherenkov 2017). En el SC de un solo paso la OD está
  fijada por β(ω) y por el solitón, y decae con la fisión.
- La lección de Wang 2018 para el proyecto: si el material tiene Raman fuerte (sílice, LiNbO₃), hay un detuning
  máximo menor que π²f²/8 y por tanto un ancho máximo menor que el de la ley sech²; en Si₃N₄ el efecto es débil
  (ver §6).

### Gaps
- No encontré un artículo de Coen/Erkintalo/Haelterman que use el título "cavity-enhanced supercontinuum"; los
  trabajos de MI de Coen & Haelterman (1997, 2001) no se verificaron en esta ronda y por eso no se citan.

---

## 6. ¿Qué limita el ancho de banda? (Raman, térmico, cruces de modos evitados, Q dependiente de modo, agotamiento de bomba)

### Takeaway
En Si₃N₄ el límite práctico no es Raman (tiempo de choque 2πτ_R ~ 20 fs frente a 2π×89 fs en sílice) sino la
geometría de D_int(μ) (D₃/D₄ y cruces de modos) y el acceso térmico al estado de solitón; en sílice y LiNbO₃ el
SSFS Raman sí recorta el rango de detuning y el ancho. Los cruces de modos evitados cerca de la bomba impiden el
solitón, lejos de ella producen OD estrechas y rasgos "up-down"; los modos de orden superior que cruzan pueden
bajar el Q de la familia útil; la eficiencia bomba→peine en CW es 1–5 %.

### Cited Findings
- Raman en Si₃N₄ (Karpov et al. 2016): LLE con término Raman ∂Ã/∂t = √κ_ex s_in|_{μ=0} − (κ/2 + i2πδ)Ã − iD_intÃ +
  ig̃F[(1 − f_R)|A|²A + f_R(h_R⊗|A|²)A], aproximación de choque h_R⊗|A|² ≈ |A|² − (2πτ_R/t_R)∂|A|²/∂φ; inferido
  2πτ_R ∼ 20 fs para SiN amorfo (sílice: 2πτ_R ≈ 2π×89 fs), f_R = 20 %; corrimiento al rojo medido de ~0.5 THz
  (~5 FSR) a 1.75 THz (~17.5 FSR), casi lineal en el detuning, con rango de existencia 2πδ = 6–11κ; FSR 75–100 GHz,
  Q ≈ 10⁶ (κ/2π ≈ 200 MHz), D₂/2π = 1–2 MHz, núcleo 0.9×1.65 µm, bomba 1550 nm 1–3 W en chip, pico intracavidad
  ~3 kW; ancho a 3 dB ~5.5 THz ≪ 12 THz del pico Raman; en muestras de 190 GHz una OD coherente cerca de 195 THz
  extiende el peine a ~75 THz y el Raman cancela o sobrecompensa el retroceso azul de la OD —
  [PRL 116, 103902](https://doi.org/10.1103/PhysRevLett.116.103902) (texto vía [arXiv:1506.08767](https://arxiv.org/abs/1506.08767)).
- Fórmula del SSFS (revisión 2026, Eq. 99): Ω_Raman = −8D₂τ_R D₁²/(15κ φ_s⁴), con φ_s la duración angular del
  solitón y f_Rφ_R = D₁τ_R; "the Raman shift in dielectrics is on the order of 10 THz"; Raman "limits DKS existence
  range and duration" y la OD puede compensar el corrimiento —
  [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897). La forma Ω ∝ τ_R D₂ Q/τ_s⁴ está derivada y
  medida en sílice por Yi, Yang, Yang & Vahala 2016 (Lagrangiano perturbado) —
  [Opt. Lett. 41, 3419](https://doi.org/10.1364/OL.41.003419) (no pude leer el texto; fórmula tomada de la revisión
  2026 y de una cita secundaria en [arXiv:1812.09610](https://arxiv.org/abs/1812.09610), que ajusta τ_R = 6.3 fs para
  LiNbO₃). Solitones Stokes (Raman) en sílice: Yang et al. 2016 — [Nat. Phys. 13, 53](https://doi.org/10.1038/nphys3875).
- Pfeiffer 2017: "The Raman self-frequency shift is absent in the uMI comb state, but can be masked in the DKS
  state" por el retroceso del solitón — [Optica 4, 684](https://doi.org/10.1364/OPTICA.4.000684).
- Cruces de modos evitados (Herr et al. PRL 2014, MgF₂ FSR 14.09 GHz, > 600 FSR y decenas de familias medidas):
  "avoided mode-crossings too close to the pumped mode" impiden el solitón; cruces lejanos se toleran; cuanto más
  lejos (b) mayor magnitud a tolerable; un cruce produce el rasgo "up-down" asimétrico en el espectro; "nonzero
  values of D3 require a minimal magnitude of the coefficient D2 to allow for soliton formation"; "A low number of
  avoided mode crossings can be achieved by reducing mode coupling"; familias con solitón: D₂/2π = 1.9 kHz (D₃ ≈ 0)
  y 21 kHz (D₃/2π = 90 Hz) — [PRL 113, 123901](https://doi.org/10.1103/PhysRevLett.113.123901).
- Revisión 2026: "the coupling higher order mode may have a lower Q-factor", reduciendo el Q de la familia que
  genera el peine; el acoplamiento transversal es menos probable con FSR mayor, Q mayor y menos modos transversales;
  las OD inducidas por AMX "are usually narrow, even single-mode"; AMX fuertes en resonadores de dispersión normal
  los causan "lower-Q higher-order transverse modes" — [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897).
- Térmico — física: Carmon, Yang & Vahala 2004, comportamiento térmico dinámico y auto-estabilidad térmica —
  [Opt. Express 12, 4742](https://doi.org/10.1364/OPEX.12.004742). Revisión 2026 (Tabla 3, dn/dT ×10⁻⁵ K⁻¹): Si 5.2,
  LiNbO₃(e) 1.6, Si₃N₄ 1.2, AlN 1.1, SiO₂ 0.6, Ta₂O₅ 0.3; el precursor del DKS (MI caótica) tiene más potencia
  intracavidad, al entrar al DKS el resonador se enfría y "once the system reaches thermal equilibrium ζ0T can
  exceed the DKS existence range" (thermal shadowing); métodos de acceso: barrido rápido, modulación de potencia o
  calentadores, láser auxiliar, self-injection locking, bombeo pulsado/subarmónico, fotorrefracción en LiNbO₃,
  backward tuning — [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897).
- Térmico — números en Si₃N₄ de octava (Li et al. 2017): vida térmica ≈ 3.4 µs (γ_T ≈ 2.9×10⁵ s⁻¹), K_c ≈ 2.86×10⁻⁴ W/K,
  triángulo térmico ~120 pm a 40 mW, corrimiento máximo tolerable ~25 pm para el solitón único a 80 mW; "the
  transition from modulation-instability combs to solitons causes a large drop in intracavity power"; los estados
  multisolitón tienen menor caída y son más fáciles de alcanzar; barrido lento (−100 GHz/s) a potencia fija y un modo
  TM adyacente ayudan — [Optica 4, 193](https://doi.org/10.1364/OPTICA.4.000193). Otros métodos: "power kicking"
  (Brasch et al. 2016b) — [Opt. Express 24, 29312](https://doi.org/10.1364/OE.24.029312); backward tuning
  determinista (Guo et al. 2017) — [Nat. Phys. 13, 94](https://doi.org/10.1038/nphys3893); láser auxiliar
  (Zhang et al. 2019) — [Optica 6, 206](https://doi.org/10.1364/OPTICA.6.000206).
- Agotamiento de bomba / eficiencia: eficiencia bomba→bandas laterales del DKS "1–5 %" por la bomba muy
  desintonizada; mejora con dispersión normal, bombeo pulsado o moléculas fotónicas (hibridación del modo bombeado
  ~50 % en una molécula de 100 GHz) — [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897);
  Anderson 2021: la eficiencia CW cae al bajar f_rep "because of reduced overlap between the soliton and the
  background pump" — [Optica 8, 771](https://doi.org/10.1364/OPTICA.403302).
- Límite por dispersión de orden superior al ancho sech²: Δf_lim = 2Δf_DW = 3|β₂|/(πβ₃) (Coen & Erkintalo 2013) —
  [Opt. Lett. 38, 1790](https://doi.org/10.1364/OL.38.001790); la TOD "reduces the dynamical instability region of
  the DKS" — [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897).

### Inferences
- Jerarquía de límites para un anillo de Si₃N₄ bombeado en CW en 1550 nm: (1) acceso térmico al estado de solitón
  único (decide si se llega siquiera al DKS); (2) D_int(μ): D₂ pequeño con D₃/D₄ controlados para que la OD caiga
  donde se quiere y haya potencia detectable en las alas; (3) cruces de modos — diseñar con pocas familias
  transversales (guías monomodo o casi) y lejos de la bomba; (4) Raman, despreciable como límite duro en Si₃N₄
  pero visible como corrimiento al rojo de 0.5–2 THz; (5) la eficiencia del 1–5 % fija la potencia por línea en
  las alas, no el ancho.
- La afirmación "Raman en SiN es débil" está cuantificada: 2πτ_R ≈ 20 fs vs 2π×89 fs en sílice (Karpov), y el pico
  Raman de SiN (~12 THz) está fuera del ancho sech² típico (5–25 THz a 3 dB) salvo en los peines más anchos.

### Gaps
- No encontré una cuantificación directa de la "mode-dependent Q" (κ(μ) espectral) como límite del ancho de banda
  más allá de la observación cualitativa de la revisión 2026 y de que Anderson 2021 omite "the spectral response of
  κ" en su modelo; falta un estudio dedicado.
- No pude leer el texto de Yi et al. 2016 (PDF no accesible); la fórmula del SSFS se cita vía la revisión 2026.

---

## 7. ¿En qué difiere el "supercontinuo en cavidad" del supercontinuo de un solo paso? (coherencia, f_rep = FSR, energía, térmico, umbrales) — síntesis y tabla de números

### Takeaway
En un microanillo CW el espectro ancho es un **estado estacionario disipativo** (un DKS que se regenera cada vuelta
desde un fondo de mW) con f_rep = FSR (10 GHz–1 THz) fijada por la geometría, energía por pulso de ~0.1 nJ o menos,
coherencia garantizada en el régimen de solitón (líneas de batido limitadas por resolución, < 1 kHz) y umbral de
cientos de mW en Si₃N₄; el SC de un solo paso es un **transitorio** de fisión de solitones de orden alto que exige
~kW de pico y ~100 fs, cuya coherencia se degrada al aumentar el orden del solitón y cuya f_rep es la del láser de
semilla. Los peines Kerr anteriores a 2014 (MI caótica) eran de octava pero no coherentes; la coherencia llegó con
el DKS.

### Cited Findings
- Diferencia de régimen de bombeo: SC convencional en guía/fibra "typically needs ~100 fs pulses with ~1 kW peak
  power to reach soliton fission"; el microresonador pulsado de Anderson usa ~1 ps y 0.6–6 W de pico (~100× menos);
  "coherent octave-spanning spectra have been hard to get at line spacings above 10 GHz" en SC convencional —
  [Anderson et al. 2021](https://doi.org/10.1364/OPTICA.403302). Brasch 2016: "conventional soliton broadening
  becomes inefficient at multi-GHz repetition rates because pulse energy drops" —
  [Brasch et al. 2016](https://doi.org/10.1126/science.aad4811).
- Repetición y energía: la revisión 2026 — "the repetition rate of microcombs is very high and usually in the
  range from 10 to 1000 GHz"; "microcombs exhibit lower per-pulse energy, but relatively high power per comb line";
  equidistancia verificada a 1 parte en 10¹⁷ — [Herr, Tikan & Kippenberg 2026](https://arxiv.org/abs/2604.05897).
  Energía del solitón en Brasch 2016: 0.1 nJ intracavidad — [Brasch et al. 2016](https://doi.org/10.1126/science.aad4811).
- Coherencia: Herr 2014 — batido RF limitado por la resolución a 1 kHz con SNR > 60 dB —
  [Herr et al. 2014](https://doi.org/10.1038/nphoton.2013.343); Brasch 2016 — peine 2/3 de octava "fully coherent",
  fase estabilizada a nivel sub-Hz — [Brasch et al. 2016](https://doi.org/10.1126/science.aad4811); Anderson 2021 —
  batido de f_rep con ancho limitado a 1 Hz y filtrado no lineal del ruido de la bomba hasta ~100× por debajo del
  ancho de la cavidad — [Anderson et al. 2021](https://doi.org/10.1364/OPTICA.403302); marco teórico de coherencia
  g⁽¹⁾ — [Erkintalo & Coen 2014](https://doi.org/10.1364/OL.39.000283).
- Hito histórico: primer peine Kerr (Del'Haye et al. 2007, microtoroide de sílice) —
  [Nature 450, 1214](https://doi.org/10.1038/nature06401); primer solitón temporal en microresonador (Herr 2014);
  primer DKS en chip con OD (Brasch 2016); primeros DKS de octava en Si₃N₄ (Li 2017; Pfeiffer 2017); sintetizador
  óptico con dos microcombs, uno de ellos de octava con FSR 1 THz (Spencer et al. 2018) —
  [Nature 557, 81](https://doi.org/10.1038/s41586-018-0065-7); solitón a tasas de microondas en sílice (Yi et al.
  2015) — [Optica 2, 1078](https://doi.org/10.1364/OPTICA.2.001078).
- Revisiones de referencia: Kippenberg, Gaeta, Lipson & Gorodetsky 2018 (DKS como "stationary localized states of a
  driven, damped, detuned nonlinear Schrödinger equation", plataformas, solitones Raman-Stokes, cristales de
  solitones, aplicaciones) — [Science 361, eaan8083](https://doi.org/10.1126/science.aan8083) (texto completo
  bloqueado; resumen vía Semantic Scholar; PDF abierto en infoscience.epfl.ch/record/258703); Pasquazi et al. 2018 —
  [Phys. Rep. 729, 1](https://doi.org/10.1016/j.physrep.2017.08.004); Gaeta, Lipson & Kippenberg 2019 —
  [Nat. Photon. 13, 158](https://doi.org/10.1038/s41566-019-0358-x); Herr, Tikan & Kippenberg 2026 —
  [arXiv:2604.05897](https://arxiv.org/abs/2604.05897).

### Tabla de números de referencia (todos tomados de los artículos citados arriba)

| Artículo | Plataforma | FSR | Q o κ/2π | D₂/2π | Bomba | Ancho 3 dB / span | OD |
|---|---|---|---|---|---|---|---|
| Herr 2014 Nat. Photon. | MgF₂ | 35.2 GHz | Q 4×10⁸ (450 kHz) | 16 kHz | 5–30 mW, 1553 nm | 1.6 THz, ~200 fs | — |
| Herr 2014 PRL | MgF₂ | 14.09 GHz | 72–173 kHz | 1.9–21 kHz | ~30 mW, 1552 nm | 1.62 THz, 194 fs | — |
| Yang 2016 Optica | sílice | 22 GHz | Q_int > 3×10⁸ | 15.2 kHz | < 1 mW en solitón | — | 198.62 THz (AMX) |
| Karpov 2016 PRL | Si₃N₄ | 75–100 GHz | Q ~10⁶ (200 MHz) | 1–2 MHz | 1–3 W, 1550 nm | 5.5 THz; SSFS 0.5–1.75 THz | ~195 THz (190 GHz) |
| Brasch 2016 Science | Si₃N₄ | 189.2 GHz | 300 MHz | 2.4 MHz (D₃ 24.5 kHz, D₄ −290 Hz) | ~2 W bus, 1560 nm | 10.8 THz; 150–225 THz (2/3 oct.), <30 fs | 155 THz (1930 nm) |
| Li 2017 Optica | Si₃N₄ (aire) | ~1 THz | Q_i 1×10⁶, Q_c 6×10⁵ | 25 / 53 MHz | 40 / 120 mW, 1550 nm | > 1 octava | 1.06 + 2.06 µm; 2.27 µm |
| Pfeiffer 2017 Optica | Si₃N₄ | ~1 THz | κ₀ 100 MHz, 𝓕 ~10⁴ | ~20 MHz | 455 mW (1.55 µm); 245 mW (1.3 µm) | 24.85 THz (12.7 fs); > 200 THz | hasta 850 nm |
| Anderson 2021 Optica | Si₃N₄, pulsado | 27.88 GHz | Q 1.8×10⁶ (110 MHz) | 7.2 kHz | 18–180 mW prom., 0.6–6 W pico | 9.5 / 64 THz (2/3 oct.), 2200 líneas | 1957 nm |
| Moille 2021 Nat. Commun. | Si₃N₄, 2 bombas | — | — | — | 1063 + 1557 nm | 137–407 THz (1.6 oct.) | traslación FWM-BS |
| Zang 2024 OL | Si₃N₄ fundición | ~1 THz | Q_i ~1.4×10⁶ (modelo) | — | ~150 mW, banda C | 1 octava | 145.43 + 290.92 THz |
| Li 2026 arXiv | Si₃N₄ heteroestructurado | 118 GHz | — | — | — | 1 octava | 290–310 THz sintonizable |

### Inferences
- La frase "supercontinuo en cavidad" debe entenderse, en microanillos CW, como "DKS + OD en estado estacionario":
  la diferencia operativa clave para el proyecto es que la coherencia no es un problema a resolver (viene con el
  solitón) pero el acceso al solitón (térmico) y la ingeniería de D_int(μ) sí lo son.
- Un anillo add-drop de Si₃N₄ como el del estudio seccion_v1 tendrá κ/2π ~ 10²–10³ MHz; con FSR de 100–200 GHz las
  cifras de Brasch/Karpov (1–2 W en el bus, D₂/2π ~ MHz) son la referencia realista para solitón único con OD, y las
  de Li/Pfeiffer (40–450 mW, D₂/2π ~ 20–50 MHz) solo se alcanzan con FSR ~ 1 THz.

### Gaps
- No encontré una comparación cuantitativa publicada, cara a cara, de la coherencia (g⁽¹⁾ o ruido de fase por
  línea) entre un SC de un solo paso y un DKS de octava con la misma anchura; las comparaciones son cualitativas.
- El texto completo de la revisión de Science 2018 no fue accesible (HTTP 403); las afirmaciones atribuidas a ella
  se limitan a su resumen.

---

## Referencias (DOI verificados en Crossref el 2026-10-29)

1. Del'Haye et al., "Optical frequency comb generation from a monolithic microresonator", Nature 450, 1214 (2007). DOI 10.1038/nature06401
2. Del'Haye et al., "Octave spanning tunable frequency comb from a microresonator", PRL 107, 063901 (2011). DOI 10.1103/PhysRevLett.107.063901
3. Okawachi et al., "Octave-spanning frequency comb generation in a silicon nitride chip", Opt. Lett. 36, 3398 (2011). DOI 10.1364/OL.36.003398
4. Matsko et al., "Mode-locked Kerr frequency combs", Opt. Lett. 36, 2845 (2011). DOI 10.1364/OL.36.002845
5. Herr et al., "Temporal solitons in optical microresonators", Nat. Photon. 8, 145 (2014). DOI 10.1038/nphoton.2013.343
6. Herr et al., "Mode spectrum and temporal soliton formation in optical microresonators", PRL 113, 123901 (2014). DOI 10.1103/PhysRevLett.113.123901
7. Brasch et al., "Photonic chip-based optical frequency comb using soliton Cherenkov radiation", Science 351, 357 (2016). DOI 10.1126/science.aad4811
8. Li et al., "Stably accessing octave-spanning microresonator frequency combs in the soliton regime", Optica 4, 193 (2017). DOI 10.1364/OPTICA.4.000193
9. Pfeiffer et al., "Octave-spanning dissipative Kerr soliton frequency combs in Si₃N₄ microresonators", Optica 4, 684 (2017). DOI 10.1364/OPTICA.4.000684
10. Karpov et al., "Raman self-frequency shift of dissipative Kerr solitons in an optical microresonator", PRL 116, 103902 (2016). DOI 10.1103/PhysRevLett.116.103902
11. Yi, Yang, Yang & Vahala, "Theory and measurement of the soliton self-frequency shift and efficiency in optical microcavities", Opt. Lett. 41, 3419 (2016). DOI 10.1364/OL.41.003419
12. Yang, Yi, Yang & Vahala, "Spatial-mode-interaction-induced dispersive waves and their active tuning in microresonators", Optica 3, 1132 (2016). DOI 10.1364/OPTICA.3.001132
13. Yang et al., "Stokes solitons in optical microcavities", Nat. Phys. 13, 53 (2017; en línea 2016). DOI 10.1038/nphys3875
14. Lucas et al., "Detuning-dependent properties and dispersion-induced instabilities of temporal dissipative Kerr solitons in optical microresonators", PRA 95, 043822 (2017). DOI 10.1103/PhysRevA.95.043822
15. Cherenkov, Lobanov & Gorodetsky, "Dissipative Kerr solitons and Cherenkov radiation in optical microresonators with third-order dispersion", PRA 95, 033810 (2017). DOI 10.1103/PhysRevA.95.033810
16. Milián & Skryabin, "Soliton families and resonant radiation in a micro-ring resonator near zero group-velocity dispersion", Opt. Express 22, 3732 (2014). DOI 10.1364/OE.22.003732
17. Milián, Gorbach & Skryabin, "Solitons and frequency combs in silica microring resonators: interplay of the Raman and higher-order dispersion effects", PRA 92, 033851 (2015). DOI 10.1103/PhysRevA.92.033851
18. Coen, Randle, Sylvestre & Erkintalo, "Modeling of octave-spanning Kerr frequency combs using a generalized mean-field Lugiato–Lefever model", Opt. Lett. 38, 37 (2013). DOI 10.1364/OL.38.000037
19. Coen & Erkintalo, "Universal scaling laws of Kerr frequency combs", Opt. Lett. 38, 1790 (2013). DOI 10.1364/OL.38.001790
20. Erkintalo & Coen, "Coherence properties of Kerr frequency combs", Opt. Lett. 39, 283 (2014). DOI 10.1364/OL.39.000283
21. Webb et al., "Measurement of microresonator frequency comb coherence by spectral interferometry", Opt. Lett. 41, 277 (2016). DOI 10.1364/OL.41.000277
22. Jang, Erkintalo, Murdoch & Coen, "Observation of dispersive wave emission by temporal cavity solitons", Opt. Lett. 39, 5503 (2014). DOI 10.1364/OL.39.005503
23. Leo et al., "Temporal cavity solitons in one-dimensional Kerr media as bits in an all-optical buffer", Nat. Photon. 4, 471 (2010). DOI 10.1038/nphoton.2010.120
24. Leo et al., "Dynamics of one-dimensional Kerr cavity solitons", Opt. Express 21, 9180 (2013). DOI 10.1364/OE.21.009180
25. Haelterman, Trillo & Wabnitz, "Dissipative modulation instability in a nonlinear dispersive ring cavity", Opt. Commun. 91, 401 (1992). DOI 10.1016/0030-4018(92)90367-Z
26. Chembo & Menyuk, "Spatiotemporal Lugiato-Lefever formalism for Kerr-comb generation in whispering-gallery-mode resonators", PRA 87, 053852 (2013). DOI 10.1103/PhysRevA.87.053852
27. Kippenberg, Gaeta, Lipson & Gorodetsky, "Dissipative Kerr solitons in optical microresonators", Science 361, eaan8083 (2018). DOI 10.1126/science.aan8083
28. Pasquazi et al., "Micro-combs: A novel generation of optical sources", Phys. Rep. 729, 1 (2018). DOI 10.1016/j.physrep.2017.08.004
29. Gaeta, Lipson & Kippenberg, "Photonic-chip-based frequency combs", Nat. Photon. 13, 158 (2019). DOI 10.1038/s41566-019-0358-x
30. Anderson et al., "Photonic chip-based resonant supercontinuum via pulse-driven Kerr microresonator solitons", Optica 8, 771 (2021). DOI 10.1364/OPTICA.403302
31. Obrzud, Lecomte & Herr, "Temporal solitons in microresonators driven by optical pulses", Nat. Photon. 11, 600 (2017). DOI 10.1038/nphoton.2017.140
32. Moille et al., "Ultra-broadband Kerr microcomb through soliton spectral translation", Nat. Commun. 12, 7275 (2021). DOI 10.1038/s41467-021-27469-0
33. Anderson et al., "Zero dispersion Kerr solitons in optical microresonators", Nat. Commun. 13, 4764 (2022). DOI 10.1038/s41467-022-31916-x
34. Xue et al., "Mode-locked dark pulse Kerr combs in normal-dispersion microresonators", Nat. Photon. 9, 594 (2015). DOI 10.1038/nphoton.2015.137
35. Wang, Anderson, Coen, Murdoch & Erkintalo, "Stimulated Raman scattering imposes fundamental limits to the duration and bandwidth of temporal cavity solitons", PRL 120, 053902 (2018). DOI 10.1103/PhysRevLett.120.053902
36. Carmon, Yang & Vahala, "Dynamical thermal behavior and thermal self-stability of microcavities", Opt. Express 12, 4742 (2004). DOI 10.1364/OPEX.12.004742
37. Guo et al., "Universal dynamics and deterministic switching of dissipative Kerr solitons in optical microresonators", Nat. Phys. 13, 94 (2017; en línea 2016). DOI 10.1038/nphys3893
38. Brasch et al., "Bringing short-lived dissipative Kerr soliton states in microresonators into a steady state", Opt. Express 24, 29312 (2016). DOI 10.1364/OE.24.029312
39. Zhang et al., "Sub-milliwatt-level microresonator solitons with extended access range using an auxiliary laser", Optica 6, 206 (2019). DOI 10.1364/OPTICA.6.000206
40. Bao et al., "Nonlinear conversion efficiency in Kerr frequency comb generation", Opt. Lett. 39, 6126 (2014). DOI 10.1364/OL.39.006126
41. Xue et al., "Microresonator Kerr frequency combs with high conversion efficiency", Laser Photon. Rev. 11, 1600276 (2017). DOI 10.1002/lpor.201600276
42. Yi et al., "Soliton frequency comb at microwave rates in a high-Q silica microresonator", Optica 2, 1078 (2015). DOI 10.1364/OPTICA.2.001078
43. Lamb et al., "Optical-frequency measurements with a Kerr microcomb and photonic-chip supercontinuum", Phys. Rev. Applied 9, 024030 (2018). DOI 10.1103/PhysRevApplied.9.024030
44. Spencer et al., "An optical-frequency synthesizer using integrated photonics", Nature 557, 81 (2018). DOI 10.1038/s41586-018-0065-7
45. Zang, Liu, Briles & Papp, "Foundry manufacturing of octave-spanning microcombs", Opt. Lett. 49, 5143 (2024). DOI 10.1364/OL.527540
46. Skryabin & Gorbach, "Colloquium: Looking at a soliton through the prism of optical supercontinuum", Rev. Mod. Phys. 82, 1287 (2010). DOI 10.1103/RevModPhys.82.1287
47. Dudley, Genty & Coen, "Supercontinuum generation in photonic crystal fiber", Rev. Mod. Phys. 78, 1135 (2006). DOI 10.1103/RevModPhys.78.1135
48. Akhmediev & Karlsson, "Cherenkov radiation emitted by solitons in optical fibers", PRA 51, 2602 (1995). DOI 10.1103/PhysRevA.51.2602

**Preprints sin DOI de revista (arXiv, verificados por URL):**
- Herr, Tikan & Kippenberg, "Frequency combs and coherent dissipative structures in nonlinear optical microresonators", arXiv:2604.05897 (abril 2026, revisión de 70 pp.).
- Li et al. (grupo Xue), "Dispersion-managed octave soliton microcombs in heterostructured microresonators", arXiv:2608.09005 (agosto 2026).
- arXiv:2512.16588 (SiC, 2025; solo resumen consultado) — DOI sin verificar.
- "Communication-ready high-power soliton microcombs in highly-dispersive Fabry-Pérot microresonators", arXiv:2512.02876 (dic. 2025; autores no consultados; solo título visto en búsqueda; no citado en el cuerpo).
