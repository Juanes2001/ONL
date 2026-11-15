# Propiedades ópticas no lineales del silicio (c-Si, SOI, a-Si:H, SiGe) para modelar GNLSE/supercontinuo

> Notas de investigación, 2026-11-14. Ventana pedida: nov 2021 – nov 2026; los valores anteriores a 2021
> van marcados **[PRE-2021, línea base]**.
>
> **Advertencia de cobertura (leer primero):** el buscador web usado en esta sesión devolvió casi solo
> literatura anterior a 2021, aun con consultas explícitas por 2022–2025. Los trabajos *dentro de la
> ventana* que se pudieron verificar son pocos (sobre todo reseñas y un par de preprints). Muchos de los
> números de la tabla son por eso de línea base clásica. Si un valor viene de mi conocimiento del artículo
> original y **no** se releyó en esta sesión, va marcado **[no re-verificado]**: hay que comprobarlo en el
> PDF antes de usarlo en el informe.
>
> Convenciones: SI. n₂ en m²/W (1 cm²/W = 10⁻⁴ m²/W). β_TPA en m/W (1 cm/GW = 10⁻¹¹ m/W). 3PA γ₃ (o α₃)
> en m³/W² (1 cm³/GW² = 10⁻²⁴ m³/W²). σ_FCA en m². FOM = n₂/(λ β_TPA), adimensional.

---

## Tabla resumen de parámetros (para elegir números de entrada)

| Parámetro | Valor | λ | Fuente | Estado |
|---|---|---|---|---|
| n₂ (c-Si, guía) | 5.2×10⁻¹⁸ m²/W (300 K); 3.9×10⁻¹⁸ m²/W (5.5 K) | 1.55 µm | Sinclair et al., *Phys. Rev. Applied* 11, 044084 (2019), doi:10.1103/PhysRevApplied.11.044084; arXiv:1809.00237 | PRE-2021; verificado; arXiv OA |
| β_TPA (c-Si, guía) | 0.76 cm/GW = 7.6×10⁻¹² m/W (300 K); 0.42 cm/GW (5.5 K) | 1.55 µm | Sinclair 2019 (ídem) | PRE-2021; verificado |
| FOM c-Si | ≈0.44 (calculado con los valores de Sinclair a 300 K: 5.2e-18/(1.55e-6·7.6e-12)) | 1.55 µm | cálculo propio con Sinclair 2019 | inferencia |
| n₂, β_TPA (c-Si, guía; otra medición) | n₂ = 0.7×10⁻¹³ cm²/W = 7×10⁻¹⁸ m²/W; β = 0.9 cm/GW | 1.54 µm | resultado citado en la búsqueda (artículo de guías Si, PRE-2021) vía [ResearchGate/OE](https://opg.optica.org/oe/fulltext.cfm?uri=oe-21-26-32192&id=276254) | PRE-2021; fuente primaria no identificada con certeza |
| β_TPA "bulk" típico NIR | ≈2.5 cm/GW (valor citado de mediciones en volumen, mayor que el de guías) | ~1.2–1.5 µm | mismo resumen de búsqueda | PRE-2021; el rango 0.5–2.5 cm/GW es la dispersión clásica entre autores |
| n₂ pico (c-Si, Z-scan) | 1.65×10⁻¹³ cm²/W = 1.65×10⁻¹⁷ m²/W, luego decae hasta 2.6 µm; medido hasta 6 µm | pico en 2.1 µm | Gai et al., "Multi-photon absorption and third-order nonlinearity in silicon at mid-infrared wavelengths", *Opt. Express* 21, 32192 (2013), doi:10.1364/OE.21.032192 | PRE-2021; OA (Optica) |
| n₂ en 2.75–5.5 µm | casi constante con λ; la absorción no lineal "nunca desaparece" | 2.75–5.5 µm | Wang et al., "Nonlinear absorption and refraction in crystalline silicon in the mid-infrared", *Laser Photon. Rev.* (2013), [ResearchGate](https://www.researchgate.net/publication/259539774) | PRE-2021; de pago (DOI no re-verificado) |
| Borde de TPA | β_TPA → 0 para λ > ~2.2 µm (E_g ≈ 1.12 eV) | — | [Gai 2013](https://opg.optica.org/oe/fulltext.cfm?uri=oe-21-26-32192&id=276254) | PRE-2021 |
| 3PA c-Si | ≈0.035 cm³/GW² = 3.5×10⁻²⁶ m³/W² | ~2.6 µm | citado en [core.ac.uk 55732839](https://core.ac.uk/download/55732839.pdf), con origen en Pearl, Rotenberg & van Driel, "Three photon absorption in silicon for 2300–3300 nm", *Appl. Phys. Lett.* 93, 131102 (2008) | PRE-2021; DOI de Pearl no re-verificado |
| 3PA: no se anula por debajo de 2.2 µm | γ₃ ≠ 0 para λ < 2200 nm | 2.3–3.3 µm | [Pearl 2008 (resumen)](https://www.researchgate.net/publication/224406602_Three_photon_absorption_in_silicon_for_2300-3300_nm) | PRE-2021 |
| 3PA vs FCA | Δα por 3PA ≈ 0.84 cm⁻¹ en su experimento; la FCA aporta solo ≈10 % de la absorción no lineal total | hasta 6 µm | [Gai 2013](https://opg.optica.org/oe/fulltext.cfm?uri=oe-21-26-32192&id=276254) | PRE-2021 |
| 3PA Ge-on-Si (comparación) | 1.1×10⁻²⁶ m³/W² | mid-IR | Della Torre et al., "Mid-infrared supercontinuum generation in a low-loss germanium-on-silicon waveguide", *APL Photonics* 6, 016102 (2021), [AIP](https://pubs.aip.org/aip/app/article/6/1/016102/1024066) | ene-2021 (justo antes de la ventana); OA |
| β_TPA a-Si:H / n₂ a-Si:H | FOM ≈ 5; Re(γ) = 1200 W⁻¹m⁻¹; estable con 2 W pico acoplados | 1.55 µm | arXiv:1405.2904, "High Kerr nonlinearity hydrogenated amorphous silicon nanowires with low two photon absorption and high optical stability" | PRE-2021; arXiv OA |
| n₂ a-Si:H | 7.43×10⁻¹³ cm²/W = 7.43×10⁻¹⁷ m²/W (~10× c-Si) | 1.55 µm | Wang & Foster, "Ultralow power continuous-wave frequency conversion in hydrogenated amorphous silicon waveguides", *Opt. Lett.* 37, 1331 (2012), [OL](https://opg.optica.org/ol/abstract.cfm?uri=ol-37-8-1331) | PRE-2021; de pago |
| FOM a-Si:H (otras) | > 2 (Kuyken et al., OE 2011), con degradación temporal reversible por recocido; F ≈ 0.35 con β ≈ 0.8 cm/GW, n₂ ≈ 4×10⁻¹⁴ cm²/W (otra muestra) | 1.54–1.55 µm | resultados de la búsqueda: [DTU Orbit](https://orbit.dtu.dk/en/publications/nonlinear-properties-of-and-nonlinear-processing-in-hydrogenated-/), [ResearchGate](https://www.researchgate.net/publication/43134607) | PRE-2021 |
| σ_FCA (Soref–Bennett, a 1.55 µm) | 1.45×10⁻²¹ m², ∝ λ² | 1.55 µm | Lin, Painter & Agrawal, *Opt. Express* 15, 16604 (2007), doi:10.1364/OE.15.016604; Soref & Bennett, *IEEE JQE* 23, 123 (1987) | PRE-2021; **[no re-verificado]**; Lin 2007 OA |
| Coef. FCD k_c | 1.35×10⁻²⁷ m³ (Δn = −k_c N, versión lineal simplificada a 1.55 µm) | 1.55 µm | Lin 2007 (ídem) | PRE-2021; **[no re-verificado]** |
| FCA/FCD 1–14 µm | relaciones ajustadas Δα(ΔN,ΔP), Δn(ΔN,ΔP) por λ, a partir de espectros de dopaje + Kramers–Kronig | 1–14 µm | Nedeljković, Soref & Mashanovich, "Free-carrier electrorefraction and electroabsorption modulation predictions for silicon over the 1–14 µm infrared wavelength range", *IEEE Photon. J.* 3, 1171 (2011), doi:10.1109/JPHOT.2011.2171930 ([DOAJ](https://doaj.org/article/273a4816f7434e2ba39ad23e93877445)) | PRE-2021; OA |
| FCA/FCD medido en guías | expresiones Drude por λ, 1.31–2.02 µm | 1.31–2.02 µm | Hagan et al., *Opt. Express* 27, 166 (2019), [Soton eprint](https://eprints.soton.ac.uk/427548/1/oe_27_1_166.pdf) | PRE-2021; OA |
| Vida media de portadores, alambre sin polarizar | ~0.5–varios ns (orden ns; ≤1 ns en guías submicrométricas según modelo) | — | [ResearchGate, "Lifetime of photogenerated carriers in SOI rib waveguides"](https://www.researchgate.net/publication/234899063) | PRE-2021 |
| Vida media con PIN inverso | ~1 ns a 25 V (rib grande, amplificador Raman) | 1.55 µm | Rong et al., *Opt. Express* 13, 519 (2005), [OE](https://opg.optica.org/oe/fulltext.cfm?uri=oe-13-2-519&id=82390) | PRE-2021; OA |
| Vida media con MSM | 55 ps | 1.55 µm | "Effective carrier sweepout in a silicon waveguide by a metal-semiconductor-metal structure", CLEO 2015 SM1I.5, [Optica](https://opg.optica.org/abstract.cfm?URI=CLEO_SI-2015-SM1I.5) | PRE-2021 |
| Vida media en nanoalambre con PIN | ~12 ps (Turner-Foster et al., *Opt. Express* 18, 3582 (2010)) | 1.55 µm | **[no re-verificado]** | PRE-2021 |
| Raman c-Si | Ω_R/2π = 15.6 THz; Γ_R ≈ 105 GHz (FWHM ~3.5 cm⁻¹); g_R ≈ 10–20 cm/GW a 1.55 µm; f_R ≈ 0.043; τ₁ ≈ 10 fs, τ₂ ≈ 3 ps | 1.55 µm | Lin, Painter & Agrawal 2007 (ídem), Claps et al. *Opt. Express* 11, 1731 (2003) | PRE-2021; **[no re-verificado]** |
| Índice lineal Si | modelo de Li, *J. Phys. Chem. Ref. Data* 9, 561 (1980) (T y λ); n ≈ 3.476 a 1.55 µm | 1.2–14 µm | **[no re-verificado]** | PRE-2021 |
| Termoóptico | dn/dT ≈ 1.8×10⁻⁴ K⁻¹ a 1.55 µm (Komma et al., *APL* 101, 041905 (2012)) | 1.55 µm | **[no re-verificado]** | PRE-2021 |
| Absorción del SiO₂ (BOX del SOI) | fuerte por encima de ~3.6–4 µm → motiva Si-on-sapphire, Si suspendido, SiGe/Ge | — | [Nanophotonics 2018 (perspectiva mid-IR)](https://www.degruyterbrill.com/document/doi/10.1515/nanoph-2017-0085/html?lang=en); [JLT 2017 (Ge suspendido)](https://opg.optica.org/jlt/abstract.cfm?uri=jlt-35-14-2994) | PRE-2021 |
| Ventana útil sin TPA | Si: 2.2–8.5 µm ("casi dos octavas") | — | Zhang et al., "Nonlinear Group IV photonics based on silicon and germanium: from near-infrared to mid-infrared", *Nanophotonics* 3, 247 (2014), doi:10.1515/nanoph-2013-0020 ([MIT OA](https://dspace.mit.edu/bitstream/handle/1721.1/101975/Kimerling_Nonlinear%20group%20IV.pdf)) | PRE-2021; OA |

---

## 1. Kerr n₂ y TPA β_TPA vs λ; 3PA; FOM; anisotropía

### Takeaway
Los números de referencia para c-Si siguen siendo los de 2007–2019: a 1.55 µm, n₂ ≈ (4.5–7)×10⁻¹⁸ m²/W y
β_TPA ≈ (0.5–0.9)×10⁻¹¹ m/W en guías (FOM ≈ 0.3–0.45); n₂ tiene un pico de ≈1.65×10⁻¹⁷ m²/W cerca de 2.1 µm
y β_TPA se anula por encima de ~2.2 µm, donde manda la 3PA (≈3.5×10⁻²⁶ m³/W² cerca de 2.6 µm). En esta
sesión no encontré ninguna medición de 2021–2026 que reemplace a Bristow 2007, Gai 2013 o Wang 2013 en el
rango de 1.2–8 µm.

### Cited Findings
- A 1.55 µm, en una guía de Si: β_TPA = 0.76 cm/GW y n₂ = 5.2×10⁻¹⁸ m²/W a 300 K; a 5.5 K bajan a 0.42 cm/GW y
  3.9×10⁻¹⁸ m²/W. La razón Kerr/absorción aumenta al enfriar — [Sinclair et al., PR Applied 11, 044084 (2019), arXiv:1809.00237](https://arxiv.org/abs/1809.00237)
- Otra medición en guía a 1.54 µm da β = 0.9 cm/GW y n₂ = 0.7×10⁻¹³ cm²/W (= 7×10⁻¹⁸ m²/W); en volumen el β_TPA
  del NIR se acerca a 2.5 cm/GW. Esto muestra la dispersión entre autores — [Resumen de búsqueda; ver Gai 2013 y sus refs.](https://opg.optica.org/oe/fulltext.cfm?uri=oe-21-26-32192&id=276254)
- Z-scan en Si de volumen: n₂ con pico de 1.65×10⁻¹³ cm²/W en 2.1 µm, que decae hasta 2.6 µm; n₂ medido hasta 6 µm.
  La TPA se anula por encima de ~2.2 µm (E_g = 1.12 eV) y aparece la 3PA. Δα por 3PA ≈ 0.84 cm⁻¹ en su
  experimento; la FCA aporta solo ≈10 % — [Gai et al., Opt. Express 21, 32192 (2013), OA](https://opg.optica.org/oe/fulltext.cfm?uri=oe-21-26-32192&id=276254)
- En 2.75–5.5 µm n₂ cambia muy poco con λ, pero "la absorción no lineal nunca desaparece" — [Wang et al., Laser Photon. Rev. 2013 (de pago)](https://www.researchgate.net/publication/259539774_Nonlinear_absorption_and_refraction_in_crystalline_silicon_in_the_mid-infrared)
- Coeficientes de tercer orden de Si, Ge y Si₁₋ₓGeₓ en el infrarrojo medio y lejano (MWIR/LWIR): artículo de
  referencia para comparar con SiGe — [Hon, Soref, Jalali, J. Appl. Phys. 110, 011301 (2011) (ResearchGate)](https://www.researchgate.net/publication/234852568_The_third-order_nonlinear_optical_coefficients_of_Si_Ge_and_Si1-xGex_in_the_midwave_and_longwave_infrared)
- 3PA en Si en 2300–3300 nm (wafer, pulsos de 200 fs): el coeficiente de 3PA no se anula por debajo de 2200 nm — [Pearl, Rotenberg & van Driel, APL 93, 131102 (2008) (resumen)](https://www.researchgate.net/publication/224406602_Three_photon_absorption_in_silicon_for_2300-3300_nm)
- Valor de 3PA usado en la literatura de supercontinuo: ≈0.035 cm³/GW² cerca de 2.6 µm (= 3.5×10⁻²⁶ m³/W²); por
  encima de ~2.2 µm la 3PA pasa a ser la pérdida limitante — [core.ac.uk 55732839](https://core.ac.uk/download/55732839.pdf)
- Ge-on-Si: 3PA = 1.1×10⁻²⁶ m³/W²; el borde largo del supercontinuo queda limitado sobre todo por los
  portadores libres que genera la 3PA — [Della Torre et al., APL Photonics 6, 016102 (2021), OA](https://pubs.aip.org/aip/app/article/6/1/016102/1024066/Mid-infrared-supercontinuum-generation-in-a-low)
- **Dentro de la ventana:** Cruz, Stephenson & Wahlstrand (NIST) miden el n₂ y el β complejos del Si en volumen
  por interferometría espectral en reflexión, a través del borde directo E₁ = 3.4 eV (energía de dos fotones).
  Es la primera observación del inicio de la TPA fuerte en ese borde. Su relevancia es baja para bombeo en
  1.55 µm o en el IR medio — [Cruz et al., Optica 11 (2024); arXiv:2405.19512 (OA)](https://arxiv.org/abs/2405.19512)
- **Dentro de la ventana (preprints, sin parámetros extraídos):** simulación de la TPA femtosegundo realzada en
  guías rib de Si — [arXiv:2506.18098 (2025)](https://arxiv.org/abs/2506.18098); dinámica rápida de la TPA en
  nanoalambres de Si — [arXiv:2606.29127 (2026)](https://arxiv.org/abs/2606.29127); TPA no degenerada de banda
  ancha entre la banda C y 2 µm en guías multimodo de bajas pérdidas — [ResearchGate (≈2025)](https://www.researchgate.net/publication/387915825)

### Inferences
- Para el GNLSE a 1550 nm, un juego defendible es n₂ = 5×10⁻¹⁸ m²/W, β_TPA = 7.5×10⁻¹² m/W (Sinclair 2019, en
  guía), con barrido de sensibilidad n₂ ∈ [4.5, 7]×10⁻¹⁸ y β ∈ [5, 9]×10⁻¹² m/W. FOM ≈ 0.4 frente a FOM ≫ 1 en
  Si₃N₄ (sin TPA en 1.55 µm): ese es el argumento central de la comparación.
- Para bombeo en 2.2–3.3 µm: β_TPA = 0, γ₃ ≈ 3.5×10⁻²⁶ m³/W², n₂ ≈ (1–1.65)×10⁻¹⁷ m²/W. FOM₂ efectivo ≫ 1.
- Anisotropía: en el χ⁽³⁾ cúbico del Si se usa el parámetro ρ = 2χ₁₁₂₂/χ₁₁₁₁ ≈ 1.27 (Zhang et al., APL 91,
  071113 (2007)). Por eso el γ efectivo del modo TE en guías orientadas según [110] (el estándar en obleas (001))
  difiere en unos pocos a ~20 % del caso [100] **[no re-verificado; ver Lin 2007 §2 y Osgood 2009]**.

### Gaps
- No encontré una nueva medición o modelo de dispersión de n₂(λ) y β_TPA(λ) para c-Si publicada en 2021–2026.
  Hay que buscar directamente en Optica/OE (p. ej. "silicon Kerr dispersion 2023") o en Google Scholar.
- No recuperé el número de Bristow, Rotenberg & van Driel, APL 90, 191104 (2007) (n₂ y β de 1.2 a 2.4 µm) ni el
  de Zhang 2007 (anisotropía) de la fuente primaria en esta sesión.
- La 3PA a 3.3–6 µm (Gai, Wang) no se extrajo numéricamente; solo se tiene Δα = 0.84 cm⁻¹ de un experimento.

---

## 2. Portadores libres: FCA, FCD, vida media y ecuaciones acopladas

### Takeaway
El modelo estándar sigue siendo Soref–Bennett en 1.3/1.55 µm y Nedeljković–Soref–Mashanovich (2011) para
1–14 µm, validado en guías entre 1.31 y 2.02 µm (Hagan 2019). La vida media es de ~ns en alambres sin
polarizar y baja a decenas de ps con barrido de portadores (PIN o MSM). No encontré revisiones de estos
coeficientes en 2021–2026.

### Cited Findings
- Relaciones de electroabsorción y electrorrefracción para c-Si en 1–14 µm, a partir de espectros de dopaje y
  Kramers–Kronig. Refinan además las ecuaciones de 1.3 y 1.55 µm con datos de absorción en THz — [Nedeljković, Soref & Mashanovich, IEEE Photon. J. 3, 1171 (2011), doi:10.1109/JPHOT.2011.2171930, OA](https://doaj.org/article/273a4816f7434e2ba39ad23e93877445)
- Comprobación experimental en guías de Si entre 1.31 y 2.02 µm con expresiones tipo Drude por longitud de onda — [Hagan et al., Opt. Express 27, 166 (2019), OA](https://eprints.soton.ac.uk/427548/1/oe_27_1_166.pdf)
- Validación en el IR medio: moduladores de portadores libres en SOI a 3.8 µm, profundidad de 34 dB por
  electroabsorción — [Nedeljković et al., Opt. Lett. 2019 (resumen de búsqueda)](https://eprints.soton.ac.uk/471874/1/84310D.pdf)
- La FCA del Ge es sustancialmente mayor que la del Si (2–16 µm) — [Nedeljković et al. 2015 (Ge)](https://openaccess.library.uitm.edu.my/Record/soton_385690/Details)
- Un PIN en inversa reduce la vida media efectiva a ~1 ns con 25 V (rib grande) — [Rong et al., Opt. Express 13, 519 (2005), OA](https://opg.optica.org/oe/fulltext.cfm?uri=oe-13-2-519&id=82390)
- Una estructura metal-semiconductor-metal (MSM) barre los portadores con polarización y deja una vida media de 55 ps — [CLEO 2015 SM1I.5](https://opg.optica.org/abstract.cfm?URI=CLEO_SI-2015-SM1I.5)
- Modelo: en guías submicrométricas se alcanzan vidas medias efectivas ≤1 ns, que dependen de la geometría y de
  la eficacia del barrido — [ResearchGate](https://www.researchgate.net/publication/234899063_Lifetime_of_photogenerated_carriers_in_silicon-on-insulator_rib_waveguides)
- El apantallamiento del campo de la unión por los portadores generados dispara la figura de ruido a alta
  potencia de bombeo — [Raman-based silicon photonics (UCI)](https://apdsl.eng.uci.edu/RecentJournals/Raman-based%20silicon%20photonics.pdf)
- En la propagación de solitones de alto orden, la FCA pesa menos que la pérdida multifotónica instantánea — [PMC6249288](https://pmc.ncbi.nlm.nih.gov/articles/PMC6249288)

### Inferences
- **Modelo GNLSE + portadores estándar** (Lin, Painter & Agrawal 2007, doi:10.1364/OE.15.016604, OA;
  [PRE-2021, forma de memoria, no re-verificada]):
  ∂A/∂z = −(α_l/2)A + Σ_{k≥2} i^{k+1}β_k/k! ∂ᵏA/∂tᵏ + i(γ_R + iβ_TPA/(2A_eff))(1 + iτ_shock ∂/∂t)[A ∫R(t′)|A(t−t′)|²dt′] − (γ₃/(2A_eff²))|A|⁴A − (σ/2)(1 + iμ)N_c A,
  con μ = 2k₀k_c/σ (FCD), y la ecuación de portadores dN_c/dt = β_TPA|A|⁴/(2hν₀A_eff²) + γ₃|A|⁶/(3hν₀A_eff³) − N_c/τ_c.
  γ complejo: γ = k₀n₂/A_eff + iβ_TPA/(2A_eff) (y A_eff calculado con la integral de campo vectorial del FDE).
- Para pulsos de fs a 1550 nm (≤100 fs, energía de pJ), N_c es pequeño y τ_c casi no influye. La FCA importa con
  pulsos de ps o tasas de repetición altas. Para el supercontinuo de fs basta un τ_c de 1 ns, con un barrido de
  10 ps a 3 ns como verificación.
- En el IR medio, σ_FCA crece aproximadamente como λ² (Drude). Con la 3PA de bombeo a 3–4 µm, la FCA puede volver
  a limitar el borde largo del espectro, como se vio en Ge-on-Si (Della Torre 2021).

### Gaps
- No verifiqué los valores numéricos σ = 1.45×10⁻²¹ m² y k_c = 1.35×10⁻²⁷ m³ ni las fórmulas de Soref–Bennett
  (ΔN, ΔP^0.8) en la fuente primaria en esta sesión. Comprobarlos en Lin 2007 (OA).
- No encontré trabajos de 2021–2026 sobre reducción de la vida media (implantación iónica, PIN) en guías
  no lineales; queda pendiente una búsqueda dirigida.

---

## 3. Raman en silicio

### Takeaway
Para el GNLSE se usa la línea de fonón óptico a 15.6 THz, muy angosta (~105 GHz). Con f_R ≈ 0.043 la
respuesta es de tipo oscilador amortiguado, con τ₁ ≈ 10 fs y τ₂ ≈ 3 ps. La ganancia es alta (~10–20 cm/GW) pero
de banda estrecha, y en supercontinuo de fs su contribución es menor que la de SPM o la emisión de onda
dispersiva. Todos estos valores son de línea base pre-2021 **[no re-verificado]**.

### Cited Findings
- Ganancia Raman neta en onda continua en una guía SOI de bajas pérdidas (contexto del g_R y del papel de la
  FCA inducida por TPA) — [Rong et al., Opt. Express 13, 519 (2005), OA](https://opg.optica.org/oe/fulltext.cfm?uri=oe-13-2-519&id=82390)
- Reseña de fotónica Raman en Si (UCI/Jalali): física, ganancia, problema de FCA y barrido con PIN — [Raman-based silicon photonics (PDF)](https://apdsl.eng.uci.edu/RecentJournals/Raman-based%20silicon%20photonics.pdf)

### Inferences
- Valores a usar (de Lin, Painter & Agrawal 2007, OA, **verificarlos**): Ω_R/2π = 15.6 THz, Γ_R/π ≈ 105 GHz,
  f_R ≈ 0.043, h_R(t) = (τ₁²+τ₂²)/(τ₁τ₂²) e^{−t/τ₂} sin(t/τ₁) con τ₁ = 1/Ω_R ≈ 10.2 fs y τ₂ = 1/Γ_R ≈ 3 ps.
- Diferencia con el Si₃N₄: este es amorfo, con una respuesta Raman ancha y débil (f_R pequeño, tipo sílice).
  El Raman del Si es estrecho, depende de la polarización y la orientación (regla de selección: el modo TE en
  [110] lo acopla) y se modela por separado.

### Gaps
- No re-verifiqué g_R, Γ_R ni f_R en las fuentes primarias (Claps 2003, Lin 2007) en esta sesión.
- No encontré mediciones de Raman en guías de Si en el IR medio publicadas en 2021–2026.

---

## 4. Entradas lineales: índice, termoóptico, pérdidas, absorción del óxido y plataformas mid-IR

### Takeaway
El SOI estándar sirve hasta ~3.6–4 µm porque el BOX de SiO₂ absorbe más allá. Por eso para el IR medio
se usan Si-on-sapphire, Si suspendido (o en pedestal), SiGe/Si y Ge-on-Si. El Si en sí es transparente hasta
~8 µm, y la ventana sin TPA va de 2.2 a 8.5 µm.

### Cited Findings
- Para Si se dispone de casi dos octavas (2.2–8.5 µm) para aplicaciones no lineales sin TPA; los portadores
  libres generados por TPA hacen lenta la respuesta de los dispositivos — [Zhang et al., Nanophotonics 3, 247 (2014), OA](https://www.degruyterbrill.com/document/doi/10.1515/nanoph-2013-0020/html)
- En el IR medio la TPA disminuye al bajar la energía del fotón. Por encima de 3 µm conviene modular por FCA, y
  entre 2 y 3 µm la electrorrefracción sigue siendo eficaz — [Mid-infrared integrated photonics on silicon: a perspective, Nanophotonics 7, 393 (2018), OA](https://www.degruyterbrill.com/document/doi/10.1515/nanoph-2017-0085/html?lang=en)
- Los medios no lineales dominados por Si o por SiO₂ absorben fuerte en el IR medio, lo que motiva las
  membranas suspendidas — [JLT 35, 2994 (2017), Ge suspendido (simulación 1.96–12 µm)](https://opg.optica.org/jlt/abstract.cfm?uri=jlt-35-14-2994)
- Demostraciones de supercontinuo en el IR medio con Si y SiGe [PRE-2021 salvo indicación]:
  - Si suspendido: 2–5 µm (1.32 octavas), bombeo a 4 µm — [Opt. Lett. 43, 1387 (2018), PDF HKU](https://xlab.hku.hk/pdf/10.1364_OL.43.001387.pdf)
  - SOI: 1.53–2.55 µm, bombeo de ps a 2.12 µm — [Kuyken et al. 2011 (core.ac.uk)](https://core.ac.uk/download/55822593.pdf)
  - Guías de Si: 2.0–7.5 µm con bombeo a 3.1 µm (peines espectralmente diseñados, 2.0–8.5 µm) — [arXiv:1906.07831](https://arxiv.org/abs/1906.07831)
  - Si-on-sapphire: de 1.9 µm a más de 6 µm (más de una octava) — [resumen citado en la búsqueda (Singh et al.)](https://www.researchgate.net/publication/319163949_Waveguides_for_Nonlinear_Optics_in_the_Mid-Infrared)
  - SiGe/Si: supercontinuo coherente de más de una octava con pulsos de ~200 fs a 4 µm; hasta 8.5 µm (Sinobad et al., Optica 5, 360 (2018)) — [ResearchGate (SiGe ANDi)](https://www.researchgate.net/publication/343436416)
  - Ge-on-Si: supercontinuo en el IR medio con pérdidas bajas — [Della Torre 2021, APL Photonics 6, 016102, OA](https://pubs.aip.org/aip/app/article/6/1/016102/1024066)
  - Fibra de núcleo de Si: 1.6–5.3 µm — [Nat. Commun. / PMC6872570](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6872570/)
- **Dentro de la ventana:** la reseña "Mid-infrared silicon photonics: From benchtop to real-world applications"
  (APL Photonics 9(8), 080901, 2024) cubre las plataformas Si y Ge y los éxitos en FWM, supercontinuo y peines — [AIP](https://pubs.aip.org/aip/app/article/9/8/080901/3308304/Mid-infrared-silicon-photonics-From-benchtop-to)
- **Dentro de la ventana:** Marris-Morini et al., "Germanium-Based Mid-Infrared Integrated Photonics", Laser
  Photon. Rev. (2026), doi:10.1002/lpor.202501738: dispositivos pasivos y activos en SiGe y supercontinuo en
  plataformas de Ge — [Wiley](https://onlinelibrary.wiley.com/doi/10.1002/lpor.202501738)

### Inferences
- Valores a verificar: índice de Si según Li (1980) [n(1.55 µm) ≈ 3.476], dn/dT ≈ 1.8×10⁻⁴ K⁻¹ (Komma 2012) y
  pérdidas en alambres SOI de ~1–3 dB/cm a 1550 nm. **[no re-verificado]**
- Para la comparación con Si₃N₄ de 400 nm: el SiN tiene n₂ ~10× menor que el Si, no presenta TPA en 1.55 µm y
  es transparente hasta ~6–7 µm si está revestido de aire. El Si (FOM ≈ 0.4 en 1.55 µm) solo compite de verdad
  bombeando por encima de 2.2 µm.

### Gaps
- No obtuve en esta sesión ninguna Sellmeier nueva (2021–2026) para c-Si; tampoco el autor ni el DOI de la
  reseña de APL Photonics 2024 (la página redirigió y no se pudo leer).

---

## 5. a-Si:H y materiales ricos en Si como alternativas de alto FOM en 1550 nm

### Takeaway
El a-Si:H ofrece n₂ ≈ 10× el del c-Si (≈7×10⁻¹⁷ m²/W en el mejor caso) y FOM de 2 a 5. La variabilidad entre
depósitos es grande (hay muestras con FOM ≈ 0.35) y hubo problemas de degradación que se revierten con recocido.
Lo que encontré dentro de 2021–2026 se limita a fuentes cuánticas (pares de fotones en CW, CLEO 2023) y a
citas secundarias. No apareció una nueva caracterización de n₂/β.

### Cited Findings
- Nanoalambres de a-Si:H ópticamente estables: FOM ≈ 5 y Re(γ) = 1200 W⁻¹m⁻¹, sin degradación con 2 W de
  potencia pico acoplada — [arXiv:1405.2904 (OA)](https://arxiv.org/abs/1405.2904)
- Conversión de frecuencia en CW con potencia ultrabaja: n₂ = 7.43×10⁻¹³ cm²/W, aproximadamente un orden de
  magnitud mayor que el del c-Si — [Wang & Foster, Opt. Lett. 37, 1331 (2012), de pago](https://opg.optica.org/ol/abstract.cfm?uri=ol-37-8-1331)
- FOM > 2; las propiedades no lineales se degradan con el tiempo y la degradación se revierte con recocido — [Kuyken et al. 2011 (DTU Orbit)](https://orbit.dtu.dk/en/publications/nonlinear-properties-of-and-nonlinear-processing-in-hydrogenated-/)
- Otra caracterización: β ≈ 0.8 cm/GW, n₂ ≈ 4×10⁻¹⁴ cm²/W, F ≈ 0.35 a 1.54 µm — [ResearchGate](https://www.researchgate.net/publication/43134607_Ultrafast_nonlinear_effects_in_hydrogenated_amorphous_silicon_wire_waveguide)
- Supercontinuo de la banda telecom al IR medio en guías de a-Si:H (OE 2013, grupo de Gante); fibra de a-Si:H de
  núcleo pequeño con supercontinuo de una octava bombeada en el IR medio (Opt. Lett. 39, 2014) — [Southampton eprints](https://eprints.soton.ac.uk/367781)
- **Dentro de la ventana:** pares de fotones por SFWM con bombeo CW en una guía de a-Si:H, CAR = 106.2 ± 1.3 (CLEO 2023) — [DTU Orbit](https://orbit.dtu.dk/en/publications/continuous-wave-photon-pair-generation-in-amorphous-hydrogenated-/)
- **Dentro de la ventana (cita secundaria):** se ha demostrado amplificación paramétrica rápida en guías de a-Si:H
  con mejor FOM que el c-Si en la banda C — [arXiv:2402.02846 (2024)](https://arxiv.org/html/2402.02846)
- Nitruro ultra-rico en Si (USRN), caracterizado por Z-scan: otro material del grupo IV con alto FOM — [PMC6637241](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6637241/); supercontinuo de una octava en nitruro rico en Si — [arXiv:1606.00568](https://arxiv.org/abs/1606.00568)
- Reseña de interacciones no lineales en nanodispositivos de a-Si:H — [NSF PAR](https://par.nsf.gov/servlets/purl/10066345)

### Inferences
- Para el modelo, un juego representativo de a-Si:H a 1550 nm sería n₂ ≈ (2–7)×10⁻¹⁷ m²/W y β_TPA ≈ (0.1–0.8)
  cm/GW. La dependencia del proceso de depósito es tan fuerte que hay que reportar una banda y no un único valor.

### Gaps
- No encontré mediciones de n₂ y β de a-Si:H publicadas en 2021–2026 ni estudios recientes de estabilidad.
- No busqué específicamente SiN rico en Si ni USRN de 2021–2026 (probablemente lo cubra otra nota del proyecto
  sobre SiN).

---

## 6. Reseñas 2021–2026 y lista corta de lectura

### Takeaway
Encontré y verifiqué tres reseñas dentro de la ventana que cubren el supercontinuo y la fotónica no lineal en
Si: Lafforgue et al. 2022 (Photonics Research, OA), Brès et al. 2023 (Nanophotonics, OA) y la reseña de
fotónica de Si en el IR medio de APL Photonics 2024 (OA). Además está Marris-Morini et al. 2026 (Laser Photon.
Rev., plataformas de Ge/SiGe).

### Cited Findings
- C. Lafforgue et al., "Supercontinuum generation in silicon photonics platforms", *Photonics Research* 10(3),
  A43 (2022), doi:10.1364/PRJ.445304. Cubre las plataformas Si, SiGe y SiN más la teoría; fue Editors' Pick y es
  OA. Los PDF y las tablas de researching.cn no se pudieron abrir (error de certificado) — [researching.cn](https://m.researching.cn/articles/OJd675b7dbd09eecdb); [EPFL Infoscience](https://infoscience.epfl.ch/handle/20.500.14299/196855)
- C.-S. Brès, A. Della Torre, D. Grassani et al., "Supercontinuum in integrated photonics: generation,
  applications, challenges, and perspectives", *Nanophotonics* 12 (2023), doi:10.1515/nanoph-2022-0749, OA. Según
  la reseña, el Si es el material que se usa en general para supercontinuo en el IR medio — [De Gruyter](https://www.degruyterbrill.com/document/doi/10.1515/nanoph-2022-0749/html?lang=en)
- "Mid-infrared silicon photonics: From benchtop to real-world applications", *APL Photonics* 9(8), 080901
  (2024). Autores y DOI no verificados; probablemente es de Southampton (Mashanovich/Nedeljković) — [AIP](https://pubs.aip.org/aip/app/article/9/8/080901/3308304/Mid-infrared-silicon-photonics-From-benchtop-to)
- D. Marris-Morini et al., "Germanium-Based Mid-Infrared Integrated Photonics", *Laser Photon. Rev.* (2026), doi:10.1002/lpor.202501738 — [Wiley](https://onlinelibrary.wiley.com/doi/10.1002/lpor.202501738)
- Línea base [PRE-2021]: Lin, Painter & Agrawal, *Opt. Express* 15, 16604 (2007), doi:10.1364/OE.15.016604 (OA);
  Leuthold, Koos & Freude, *Nat. Photon.* 4, 535 (2010), doi:10.1038/nphoton.2010.185 (de pago); Osgood et al.,
  *Adv. Opt. Photon.* 1, 162 (2009), doi:10.1364/AOP.1.000162 (de pago). Los DOI vienen de mi conocimiento y no se
  re-verificaron en esta sesión.

### Inferences — lista corta (máx. 7)
1. **Lafforgue et al., Photon. Res. 10, A43 (2022)**, doi:10.1364/PRJ.445304, OA. Reseña de supercontinuo en Si,
   SiGe y SiN dentro de la ventana; es directamente la comparación Si vs SiN del proyecto.
2. **Brès et al., Nanophotonics (2023)**, doi:10.1515/nanoph-2022-0749, OA. Reseña general de supercontinuo
   integrado, con tablas comparativas entre plataformas.
3. **Lin, Painter & Agrawal, Opt. Express 15, 16604 (2007)**, OA, PRE-2021. Fuente canónica de las ecuaciones
   GNLSE + portadores y de los parámetros n₂, β, σ, k_c, Raman y anisotropía.
4. **Gai et al., Opt. Express 21, 32192 (2013)**, OA, PRE-2021. Dispersión de n₂ y absorción multifotónica (3PA)
   de Si en el IR medio, hasta 6 µm.
5. **Nedeljković, Soref & Mashanovich, IEEE Photon. J. 3, 1171 (2011)**, OA, PRE-2021. FCA y FCD de 1 a 14 µm.
6. **Sinclair et al., PR Applied 11, 044084 (2019) / arXiv:1809.00237**, OA, PRE-2021. Medición limpia en guía de
   n₂ y β_TPA a 1.55 µm.
7. (Opcional, IR medio) **Della Torre et al., APL Photonics 6, 016102 (2021)**, OA. Supercontinuo en Ge-on-Si con
   3PA y portadores; es el modelo de referencia para bombeo en el IR medio.

### Gaps
- La ventana 2021–2026 queda sub-representada por las limitaciones del buscador. Pendiente: buscar en Google
  Scholar/Optica con filtro de año ≥ 2022 "silicon supercontinuum mid-infrared", "silicon nonlinear coefficients
  2 µm", "a-Si:H nonlinear 2023" y "silicon pin junction four-wave mixing 2023".
