# Rutas hacia peines Kerr de banda ancha en anillos con dispersión NORMAL y en Si₃N₄ delgado (≈ 400 nm, 1550 nm)

Notas de investigación (2026-10-29). Alcance: peines de pulso oscuro/platicones en dispersión normal; ingeniería de dispersión en Si₃N₄ delgado; plataformas de película delgada con peines demostrados; física del umbral de grosor; comparación de ancho de banda normal vs. anómala. Marco temporal 2012–2026, énfasis 2020–2026.

**Convención de signos.** En estas notas "dispersión normal" = β₂ > 0 ⇔ D < 0 ps/(nm·km) ⇔ D₂ < 0 (D₂ es el término cuadrático de la expansión de resonancias ω_μ = ω₀ + D₁μ + D₂μ²/2 + …). Conversión a 1550 nm (cálculo propio, D = −2πc β₂/λ²): **1 ps²/km ≈ −0,78 ps/(nm·km)**; es decir, D = −1200 ps/(nm·km) ⇔ β₂ ≈ +1530 ps²/km.

**Verificación de DOI.** Todos los DOI marcados "✔" fueron resueltos el 2026-10-29 con `curl https://doi.org/<doi>` (HTTP 302 hacia la página del editor correspondiente, listada al final). Los no resueltos se marcan "DOI sin verificar".

---

## P1. ¿Hay algún peine Kerr o generación de banda ancha publicada en un anillo de Si₃N₄ de 400 nm? Si no, ¿cuál es el grosor mínimo demostrado?

### Takeaway
No encontré ningún peine Kerr publicado en un anillo de Si₃N₄ de exactamente 400 nm bombeado a 1550 nm. Lo más cercano: (a) peines (MI y octava) en anillos **air-clad de 410–430 nm** pero bombeados en el visible/NIR (283–384 THz ≈ 780–1060 nm), donde la película delgada sí es anómala (Moille et al., LPR 2025); (b) peines mode-locked en **300 nm** con anillos concéntricos (Kim et al., Nat. Commun. 2017) y peines de **pulso oscuro en 300 nm** de fundición (6 pulgadas) bombeados a 780 nm vía self-injection locking (Long et al., arXiv 2025). El grosor mínimo demostrado para un peine coherente en Si₃N₄ es por tanto **300 nm** (a 1550 nm sólo con anillos concéntricos; en dispersión normal "pura" como pulso oscuro, a 780 nm).

### Cited Findings
- Kim et al. 2017: "We demonstrate anomalous dispersion in a 300 nm thick silicon nitride film" mediante racetracks concéntricos acoplados resonantemente; acoplamiento tapered selecciona el supermodo anómalo y se obtienen "coherent mode-locked frequency combs". DOI ✔ 10.1038/s41467-017-00491-x — [Nature Communications 8, 372 (2017)](https://doi.org/10.1038/s41467-017-00491-x); texto completo vía [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5575100/fullTextXML).
- Kim et al. 2017, geometría del dispositivo de peine (Fig. 3): Si₃N₄ estequiométrico de 300 nm sobre 3 µm de SiO₂ térmico y 3 µm de SiO₂ LPCVD encima; R_out = 100 µm, gap inner/outer = 600 nm, w_in = 3000 nm, w_out = 2000 nm; FSR = 152,4 GHz; Q intrínseco 1–2×10⁶; potencias de bombeo en el bus 425–495 mW a 1535–1560 nm; con bombeo bicromático (1542,2 + 1543,4 nm) potencia total ≈ 0,55 W y umbral ≈ 0,1 W; el peine "type-II" alcanza ≈ 180 nm de ancho; el modo TE₁ del anillo interior solo tiene dispersión normal "around −1200 ps nm⁻¹ km⁻¹", descrita como típica de Si₃N₄ de 300 nm — [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5575100/fullTextXML).
- Kim et al. 2017 no clasifica el estado como solitón brillante u oscuro: bajo bombeo único "a discrete jump in transmitted power suggests soliton formation, possibly multi-soliton"; bajo bombeo bicromático la autocorrelación indica un único pulso de período 6,56 ps — [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5575100/fullTextXML).
- Moille, Westly, Shrestha, Hoang, Srinivasan, "Broadband visible wavelength microcomb generation in silicon nitride microrings through air-clad dispersion engineering": H = 430 nm (dispositivos TE/TM) y 410 nm (dispositivo de 305 THz), RW = 980 nm (TE, bombeo 283 THz), 875 nm (305 THz, R = 82 µm), 625 nm (TM, bombeo 384 THz); cladding aire arriba y a los lados; peine MI de 125 THz, peine de octava de 220 THz (bombeo 305 THz, 400 mW), peine dual-DW de ~130 THz (TM, 384 THz); Q ≈ 1×10⁵ (Q₀ = 3,3×10⁵ medido a 780 nm); ~150 mW de bombeo. Publicado en Laser & Photonics Reviews 2025, DOI ✔ 10.1002/lpor.202401746 — [arXiv 2404.01577](https://arxiv.org/abs/2404.01577); [texto HTML](https://arxiv.org/html/2404.01577).
- Moille et al. 2025: con cladding de aire el régimen anómalo se extiende a > 500 THz (TE) y ≈ 390 THz (TM); con cladding de óxido se limita a ≈ 315 THz "regardless of polarization", porque el SiO₂ se vuelve cada vez más normal a longitudes de onda cortas mientras que el aire es no dispersivo — [arXiv 2404.01577 HTML](https://arxiv.org/html/2404.01577).
- Long et al. 2025 (arXiv 2505.00352, sin DOI de revista): "Hybrid-integrated dark-pulse microcombs towards visible light spectrum": Si₃N₄ de 300 nm, proceso sustractivo de fundición en obleas de 6 pulgadas (stepper DUV ASML PAS850C, 110 nm), FSR 100,704 GHz y 20,358 GHz, GVD normal, bombeo a 780 nm con diodo Fabry-Pérot (90 mW a 120 mA, 32 % de eficiencia de acoplamiento por faceta), iniciación por self-injection locking — [arXiv 2505.00352](https://arxiv.org/html/2505.00352).
- Zhang et al. 2024, "300-nm-thick, ultralow-loss silicon nitride photonic integrated circuits by 8-in. foundry production", APL 125, 121111, DOI ✔ 10.1063/5.0221409: Q intrínseco hasta 15×10⁶ (2,2 dB/m) en 300 nm — [AIP](https://doi.org/10.1063/5.0221409). Un fragmento de la búsqueda atribuye a este trabajo la frase: "Dark pulse microcombs generated in normal-dispersion microresonators can relieve the need for thick-film Si₃N₄ and offer high conversion efficiency, but they are constrained by limited bandwidth and uneven spectra" con objetivo en banda O — [ResearchGate listing](https://www.researchgate.net/publication/384097443_300-nm-thick_ultralow-loss_silicon_nitride_photonic_integrated_circuits_by_8-in_foundry_production) (fragmento; el resumen en AIP sólo menciona el láser híbrido).
- Lihachev et al. 2022 (platicones, DOI ✔ 10.1038/s41467-022-29431-0): "reaching the anomalous-GVD regime for DKS generation at telecom bands requires film thickness above 600 nm" y los platicones "can be built on thin-film Si₃N₄ typically below 300 nm" (plataformas CMOS estándar); su dispositivo tiene ~530 nm × 2,00 µm — [ar5iv 2103.07795](https://ar5iv.labs.arxiv.org/html/2103.07795).
- Sabouri, Riaz, Catuneanu, Jamshidi (TU Dresden), "Dark Frequency Comb Formation in Thin Silicon Nitride Normal Dispersion Microresonator", CLEO/Europe-EQEC 2019, paper ef_p_3: estudio **numérico** (LLE) de pulsos oscuros en una guía monomodo de Si₃N₄ "thin"; sin grosor, Q ni potencias en el resumen. DOI sin verificar — [Optica abstract](https://opg.optica.org/abstract.cfm?uri=eqec-2019-ef_p_3); [IEEE Xplore 8872841](https://ieeexplore.ieee.org/document/8872841).
- Proceso de Applied Nanotools (ANT) vía CMC: Si₃N₄ de 400 nm sobre 4,5 µm de óxido enterrado, litografía e-beam de 100 keV con features ≥ 120 nm, dispositivos **totalmente grabados** (ICP-RIE anisotrópico), opción de calefactores TiW — [CMC: ANT SiN fabrication process](https://www.cmc.ca/ant-sin-fabrication-process/).

### Inferences
- El vacío es real: no hay peine Kerr reportado en 400 nm de Si₃N₄ a 1550 nm. Las demostraciones delgadas cierran el problema o bien bombeando donde la película delgada ya es anómala (visible/NIR, Moille 2025) o bien aceptando dispersión normal e iniciando con mode-crossing (Kim 2017) o self-injection locking (Long 2025).
- Para 400 nm a 1550 nm en óxido, el valor −1200 ps/(nm·km) de 300 nm es una cota superior de "normalidad"; 400 nm estará menos normal pero, según Lihachev 2022, lejos del cruce a anómalo (> 600 nm). Un modo TE0 a 1550 nm en 400 nm con cladding SiO₂ se espera del orden de varios cientos de ps/(nm·km) normales (estimación propia por interpolación; debe calcularse con FDE).
- El proceso ANT (400 nm, un solo grabado completo, calefactores disponibles) es compatible con las dos rutas de iniciación demostradas en dispersión normal: anillos acoplados con calefactores (Xue 2015 LPR, Kim 2019) y self-injection locking (Lihachev 2022, Long 2025).

### Gaps
- No se encontró ningún artículo con peine en Si₃N₄ de 400 nm a 1550 nm (búsquedas: "400 nm thick", "thin silicon nitride normal dispersion", "coupled thin silicon nitride microresonators"). Un listado de ResearchGate ("Kerr-comb generation in a dispersion engineered coupled thin silicon nitride microresonators", 2018) y un fragmento que menciona películas de 400 nm con Q_int ≈ 6×10⁶ (R = 60 µm) y ≈ 2×10⁷ (R = 240 µm) no pudieron verificarse (sin acceso al texto; sin DOI).
- No se obtuvo la cifra de ancho de banda ni la eficiencia del peine de pulso oscuro de Long et al. 2025 (solo figuras).

---

## P2. ¿Cómo cambia un cladding de agua (n ≈ 1,32, ~47 dB/cm ponderado por confinamiento) la dispersión y la factibilidad? ¿Hay peines o efectos no lineales en microresonadores con cladding líquido/acuoso?

### Takeaway
No encontré ningún artículo que reporte un peine Kerr (ni OPO/FWM resonante) en un microresonador con cladding de agua o líquido; la literatura de microanillos de Si₃N₄ en agua es de sensado lineal con Q bajos (~10⁴). Con los datos tabulados de Hale & Querry, la absorción del agua a 1550 nm es α ≈ 10–12 cm⁻¹ (≈ 45–50 dB/cm), lo que confirma la cifra de 47 dB/cm; incluso con confinamiento del 10 % en el agua la pérdida (~4–5 dB/cm) limita Q a ~10⁵, insuficiente para umbrales Kerr razonables en Si₃N₄ delgado. En cuanto a dispersión, la evidencia indirecta (Moille 2025: aire vs. óxido) indica que bajar el índice del cladding desplaza la dispersión hacia lo anómalo, pero no hay datos publicados para agua.

### Cited Findings
- Hale & Querry 1973 (tabla original, DOI ✔ 10.1364/AO.12.000555): absorción del agua 17,59 cm⁻¹ a 1500 nm, 11,83 cm⁻¹ a 1540 nm, 9,67 cm⁻¹ a 1560 nm, 6,72 cm⁻¹ a 1600 nm — [tabla WaterAbsorptionOrig.txt (Oxford)](https://users.physics.ox.ac.uk/~pierrehumbert/PrinciplesPlanetaryClimate/Data/WorkbookDatasets/Chapter4Data/AbsorptionData/WaterAbsorptionOrig.txt); cita en [OMLC](https://omlc.org/spectra/water/abs/hale73.html). Cálculo propio: interpolando ≈ 10,7 cm⁻¹ a 1550 nm ⇒ 10·log₁₀(e)·10,7 ≈ **46,6 dB/cm**.
- Kedenburg, Vieweg, Gissibl, Giessen 2012 (DOI ✔ 10.1364/OME.2.001588): índice de refracción del agua a 20 °C medido entre 500 y 1600 nm y absorción entre 500 y 1750 nm, con fórmulas de dispersión; datos tabulados en "Media 6" (CSV) — [Optical Materials Express 2, 1588 (2012)](https://doi.org/10.1364/OME.2.001588); [CSV en figshare](https://osapublishing.figshare.com/articles/Media_6_Linear_refractive_index_and_absorption_measurements_of_nonlinear_optical_liquids_in_the_visible_and_near-infrared_spectral_region/4921181).
- Un trabajo de 2012 señala "obvious errors" en los datos tempranos integrados por Hale & Querry y que el resultado más aceptado en NIR es Palmer & Williams 1974 (fragmento de búsqueda) — [ygxb.ac.cn PDF](https://ygxb.ac.cn/rc-pub/front/front-article/download/10656868/lowqualitypdf/%E8%BF%91%E7%BA%A2%E5%A4%96%E6%B3%A2%E6%AE%B5%EF%BC%88900%E2%80%942500nm%EF%BC%89%E6%B0%B4%E5%90%B8%E6%94%B6%E7%B3%BB%E6%95%B0%E6%B5%8B%E9%87%8F.pdf).
- Sensado con agua como cladding: un microanillo de Si₃N₄ integrado con microfluídica para índice de refracción de líquidos reporta Q ≈ 9,4×10³ a 1575 nm con cladding de agua (sensor de desplazamiento de resonancia, no de peine) — [ACS Materials Au / PMC12921590](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12921590/).
- Moille et al. 2025 (DOI ✔ 10.1002/lpor.202401746): el cladding de aire amplía el rango anómalo frente al óxido (> 500 THz vs ≈ 315 THz) y "increased mode confinement, owing to a greater refractive index contrast" aumenta la no linealidad efectiva — [arXiv 2404.01577](https://arxiv.org/html/2404.01577).
- Revisión de plataformas: en resonadores integrados "the resonator is embedded into a cladding material (mostly silicon dioxide)" y en WGM de vidrio el cladding es la atmósfera (aire) — [kerrfrequencycombs.org](https://www.kerrfrequencycombs.org/?page_id=471).
- Uso de microcombs con líquidos sólo como muestra externa (cubeta), no como cladding: espectroscopía directa de líquidos con un microcomb de Si₃N₄ — fragmento en [Nature review s44310-024-00030-9](https://www.nature.com/articles/s44310-024-00030-9) (contexto; la demostración concreta no fue abierta).

### Inferences
- Dispersión: el agua (n ≈ 1,32) está entre el aire (1,0) y el SiO₂ (1,44); por la tendencia aire→óxido de Moille 2025, sustituir el óxido superior por agua debería desplazar el TE0 de Si₃N₄ delgado ligeramente hacia lo anómalo (mayor contraste ⇒ mayor dispersión de guía de onda negativa en β₂), pero el agua es dispersiva en el NIR (índice y absorción fuertemente crecientes hacia 1450 nm), lo que añade dispersión material del cladding. Sin cálculo publicado; requiere FDE con n(λ) del agua (Kedenburg 2012).
- Factibilidad: con α_agua ≈ 10,7 cm⁻¹ y una fracción de potencia Γ en el agua, la pérdida añadida es ≈ 46,6·Γ dB/cm. Para Γ = 5 % ⇒ 2,3 dB/cm ⇒ Q_abs ≈ 2πn_g/(λ α) ≈ 2π·2,0/(1,55 µm · 0,054 /cm·… ) ~ 1–2×10⁵ (orden de magnitud; cálculo propio). Un Q ~ 10⁵ eleva el umbral de OPO/MI en Si₃N₄ delgado (A_eff grande) a centenares de mW–W, y la absorción además genera calentamiento térmico fuerte en el agua. Esto hace improbable un peine en agua a 1550 nm; a 780 nm (α_agua ≈ 0,02–0,03 cm⁻¹, dos a tres órdenes menos) o en banda O (~1300 nm) la situación cambia radicalmente.
- Para el proyecto (refractómetro bulk n = 1,33–1,37): la ruta realista es un peine generado en una sección del anillo/segundo anillo con cladding de óxido y una ventana de sensado, o un peine en un dispositivo separado que ilumina el sensor; no hay precedente publicado de peine en el propio anillo acuoso.

### Gaps
- No se encontró ningún artículo de peine Kerr, OPO ni FWM resonante en microresonador con cladding líquido/acuoso (4 búsquedas distintas: "water cladding", "liquid-clad", "optofluidic Kerr", "aqueous soliton microcomb biosensing"). Es un hueco de literatura, no sólo de búsqueda.
- No se extrajo el valor numérico de n del agua a 1550 nm de la tabla de Kedenburg (CSV no leído); el valor n ≈ 1,318 del enunciado no fue confirmado de fuente primaria aquí.
- No se encontró ningún cálculo publicado de D₂/β₂ de Si₃N₄ con cladding de agua.

---

## P3. Números típicos de peines de pulso oscuro / platicón (Q, D₂ < 0, detuning, potencia, eficiencia, ancho de banda)

### Takeaway
Los pulsos oscuros se obtienen en Si₃N₄ de 530–730 nm de grosor y 2–3 µm de ancho, β₂ ≈ +36 … +350 ps²/km (D₂/2π ≈ −60 kHz a 26 GHz de FSR), Q intrínseco 1–10×10⁶, bombeos en chip de 20–180 mW (hasta 0,4–0,7 W en los primeros trabajos), eficiencias de conversión 20–41 % (vs. ~1 % en solitones brillantes convencionales), y anchos de banda de **≈ 35–90 nm (4–11 THz)** en banda C/L; el detuning efectivo es del lado azul de la resonancia (estado térmicamente estable).

### Cited Findings
- Xue et al. 2015, Nat. Photon. 9, 594 (DOI ✔ 10.1038/nphoton.2015.137): peines de pulso oscuro en microresonadores de dispersión normal con excitación asistida por interacción modal; la excitación es difícil por "the lack of modulational instability in the effective blue-detuned pumping region"; primera transición a mode-locking observada en dispersión normal — [arXiv 1404.2865](https://arxiv.org/abs/1404.2865).
- Dispositivo de Xue 2015 según trabajos posteriores del mismo grupo: anillo de Si₃N₄ de R = 100 µm (FSR ≈ 230–231 GHz), guía de 2 µm × 600 nm con dispersión normal en banda C; Q cargado 7,7×10⁵ (sobreacoplado); 40 líneas de 1513 a 1586 nm (≈ 73 nm) con 209 mW de potencia de peine en chip para 656 mW de bombeo en chip; en otro experimento ~1,7 W para un peine ancho mode-locked — [Xue et al., Opt. Express 24, 687 (2016), thermal tuning](https://opg.optica.org/oe/fulltext.cfm?uri=oe-24-1-687&id=335412); [Xue et al., LPR 2017 arXiv 1610.00958](https://arxiv.org/pdf/1610.00958).
- Xue, Xuan, Wang, Wang, Liu, Niu, Leaird, Qi, Weiner 2015, LPR 9, L23 (DOI ✔ 10.1002/lpor.201500107): dos anillos de Si₃N₄ acoplados, radios 60 µm y 58 µm (FSR 378 y 391 GHz), **β₂ ≈ 130 ps²/km** (normal), interacción modal introducida y controlada térmicamente con un microcalefactor en el anillo auxiliar; permite selección de la tasa de repetición y mode-locking — [arXiv 1503.06142](https://arxiv.org/pdf/1503.06142).
- Xue et al. 2017, LPR 11, 1600276 (DOI ✔ 10.1002/lpor.201600276): la eficiencia se define η = P_out,otras líneas / P_in; "the dark pulses can be much wider than the bright solitons" bajo iguales dispersión, Kerr, bombeo y Q, lo que explica la mayor eficiencia predicha — [arXiv 1610.00958](https://arxiv.org/pdf/1610.00958).
- Fülöp et al. 2018, Nat. Commun. 9, 1598 (DOI ✔ 10.1038/s41467-018-04046-6): anillo de 100 µm (FSR ≈ 230 GHz), guía 2 µm × 600 nm, dispersión normal en banda C, Q intrínseco ≈ 1,6×10⁶; bombeo ≈ 1540 nm, 25,6 dBm (≈ 363 mW) fuera del chip (< 400 mW), ≈ 5 dB/faceta; eficiencia de conversión en chip > 20 %; 20 líneas usadas (1531–1566 nm, ≈ 35 nm ≈ 4,4 THz), ≈ 28 mW totales en la salida y ≈ 8,6 mW en líneas nuevas; iniciación barriendo el bombeo desde el lado azul (térmicamente estable) con realimentación sobre una línea a 1536 nm; 2 de 3 dispositivos similares produjeron pulso oscuro; el diseño optimizado simulado usa β₂ = 350 ps²/km; "the limits in this study are not fundamental" — [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5913129/fullTextXML).
- Kim, Okawachi, Jang, Yu, Ji, Zhao, Joshi, Lipson, Gaeta 2019, Opt. Lett. 44, 4475 (DOI ✔ 10.1364/OL.44.004475): Si₃N₄ 730 nm × 1000 nm, TE fundamental en GVD normal; anillo principal FSR 200 GHz y auxiliar 206 GHz (Vernier ⇒ cruces cada ≈ 50 nm); gap 525 nm ⇒ splitting 7,1 GHz; bombeo 1559,79 nm, 180 mW en el bus (funciona 115–200 mW); líneas de 1495 a 1583 nm (≈ 88 nm ≈ 11 THz), 51 líneas > 50 µW, 18 líneas > 1 mW; **eficiencia 40,6 %** ("hasta 41 %", récord para GVD normal); calefactores de Pt (principal 28→16 mW, auxiliar 82 mW); el estado de bajo ruido se mantiene en un rango de ~4 mW de calefactor, por lo que la velocidad de barrido es arbitraria, a diferencia del solitón brillante — [ar5iv 1907.07164](https://ar5iv.labs.arxiv.org/abs/1907.07164).
- Lihachev et al. 2022, Nat. Commun. 13, 1771 (DOI ✔ 10.1038/s41467-022-29431-0): platicón por self-injection locking de un DFB a 1556 nm; Si₃N₄ ~530 nm × 2,00 µm, R = 900 µm, FSR 26,2 GHz, Q₀ ≈ 10⁷ (κ₀/2π = 19 MHz), **D₂/2π = −59,9 kHz**, ~20 mW en el bus, ~1,5 mW de potencia de platicón, eficiencia CW→platicón ≈ 30 % frente a 0,4 % para un DKS brillante de 20 GHz — [ar5iv 2103.07795](https://ar5iv.labs.arxiv.org/html/2103.07795). (Cálculo propio con β₂ = −D₂ n_g/(c D₁²), n_g ≈ 2: β₂ ≈ +93 ps²/km.)
- Helgason et al. 2021, Nat. Photon. 15, 305 (DOI ✔ 10.1038/s41566-020-00757-9): "photonic diatomic molecules" (dos microresonadores linealmente acoplados); las ondas solitarias se forman al sintonizar el láser a través de un nivel desdoblado; peine coherente, reproducible, con alta eficiencia y planitud espectral "at laser powers of a few milliwatts" — [Chalmers](https://research.chalmers.se/en/publication/522149); [arXiv 2007.02608](https://arxiv.org/abs/2007.02608). Un resumen de CLEO 2020 del mismo grupo reporta 36 % de conversión con 2,5 mW de bombeo en anillos acoplados con pulso oscuro — fragmento en [Chalmers 537297](https://research.chalmers.se/en/publication/537297).
- Helgason et al. 2023, Nat. Photon. 17, 992 (DOI ✔ 10.1038/s41566-023-01280-3): usa dos anillos **anómalos** acoplados para desplazar la frecuencia de bombeo y superar el límite de ~1 % de los solitones brillantes, con eficiencia > 50 %; el artículo cita a los pulsos oscuros, cristales de solitones y rollos de Turing como estados de "much higher conversion efficiency ... with other caveats" — [arXiv 2202.09410](https://arxiv.org/abs/2202.09410); [Nature PDF](https://www.nature.com/articles/s41566-023-01280-3.pdf).
- Lobanov, Lihachev, Kippenberg, Gorodetsky 2015, Opt. Express 23, 7713 (DOI ✔ 10.1364/OE.23.007713): predicen "platicons" (pulsos disipativos de cima plana) en GVD normal; su duración se controla con el detuning del bombeo; el espectro discreto de solitones oscuros de la LLE se transforma en cuasicontinuo de platicones — [arXiv 1501.07450](https://arxiv.org/pdf/1501.07450). Generación con bombeo modulado/biarmónico: Lobanov et al., EPL 112, 54008 (2015), DOI ✔ 10.1209/0295-5075/112/54008 — [arXiv 1508.06850](https://arxiv.org/abs/1508.06850v3).
- Yu, Lucas, Zang, Papp 2022, Nat. Commun. 13 (DOI ✔ 10.1038/s41467-022-30774-x): en un PhCR de tantalio (570 nm Ta₂O₅) con dispersión normal, un PhCR de 200 GHz bombeado con 33 mW da 7 mW de peine (≈ 180–210 THz, es decir ≈ 30 THz), eficiencia hasta 21 %; el lóbulo central se estrecha de 1,58 a 0,45 THz al aumentar el detuning α — [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9170700/fullTextXML).

### Inferences
- Tabla de órdenes de magnitud para diseño (de las fuentes anteriores): Q_int 1–10×10⁶; β₂ +40…+350 ps²/km (D ≈ −30…−270 ps/(nm·km)); P_bombeo 20–200 mW en chip (con Q ~10⁶–10⁷); η 20–41 %; ancho 35–90 nm (4–11 THz) en telecom; detuning efectivo azul.
- El espectro del pulso oscuro es típicamente "plano con hombros" y su ancho se controla con la fuerza del acoplamiento modal/detuning, no con D₂ (Jang 2016, Yu 2022); de ahí los anchos modestos pero la alta eficiencia.

### Gaps
- No pude extraer del texto primario de Xue 2015 (Nature Photonics, no OA) sus cifras de Q, D₂ y ancho; las anteriores provienen de artículos posteriores del grupo sobre el mismo anillo.
- Nazemosadat et al., "Switching dynamics of dark-pulse Kerr frequency comb states in optical microresonators", PRA 103, 013513 (2021): el DOI 10.1103/PhysRevA.103.013513 resuelve en APS, pero no confirmé el emparejamiento título–DOI ni leí sus cifras — [Chalmers listing](https://research.chalmers.se/en/publication/522243).
- Helgason 2021: no se obtuvieron grosor, FSR, D₂ ni ancho del texto (PDF no legible con las herramientas disponibles).

---

## P4. ¿Qué enfoque de ingeniería de dispersión es más compatible con una película fija de 400 nm y un proceso de fundición de un solo grabado?

### Takeaway
Con grosor fijo y un solo grabado completo, los grados de libertad son el **ancho, la geometría en el plano (anillos acoplados/concéntricos, modulación tipo cristal fotónico de la pared) y el cladding**. Las tres rutas demostradas sin cambiar el grosor son: (1) anillos acoplados con calefactores que colocan un cruce evitado junto al bombeo (Xue 2015 LPR, Kim 2019; Helgason 2021) — iniciación determinista y hasta 41 % de eficiencia en dispersión normal; (2) anillos concéntricos cuyo supermodo antisimétrico es anómalo (Kim 2017, en 300 nm); (3) PhCR con un solo modo desplazado (Yu 2022; Moille 2023 "Fourier synthesis", Lucas 2023) — todo litográfico. Slot y multicapa requieren pasos de proceso no disponibles en un solo grabado de 400 nm; el cladding de aire (Moille 2025) es viable si la fundición permite abrir ventanas.

### Cited Findings
- Moille, Lu, Stone, Westly, Srinivasan 2023, Commun. Phys. 6, 144 (DOI ✔ 10.1038/s42005-023-01253-6): "Conventional microrings offer only two geometric knobs, width and thickness"; la modulación de la pared interna del anillo (cristal fotónico) sintoniza frecuencias de resonancia individuales mediante una relación de Fourier entre el perfil espacial y los desplazamientos modales deseados; permite tallar arbitrariamente la envolvente del peine — [arXiv 2210.14108](https://arxiv.org/abs/2210.14108).
- Lucas, Yu, Briles, Carlson, Papp 2023, Nat. Photon. 17, 943 (DOI ✔ 10.1038/s41566-023-01252-7): diseño inverso de una "meta-dispersión" arbitraria implementada con PhCR, resolviendo la "inverse LLE" con algoritmo genético; varios generadores fabricados — [Nature](https://www.nature.com/articles/s41566-023-01252-7); [arXiv 2209.10294](https://arxiv.org/pdf/2209.10294).
- Yu, Cole, Jung, Moille, Srinivasan, Papp 2021, Nat. Photon. 15, 461 (DOI ✔ 10.1038/s41566-021-00800-3): PhCR "edgeless" cuyo nanopatrón desplaza un único modo azimutal, suprime el patrón de Turing y hace que el solitón se forme espontáneamente bajo excitación constante — [arXiv 2002.12502](https://pdf.arxiv.org/pdf/2002.12502).
- Yu et al. 2022 (DOI ✔ 10.1038/s41467-022-30774-x): en dispersión normal, el modo desplazado por el PhC "unconditionally satisfies phase matching for four-wave mixing"; desplazamientos ε = 4,5κ y 5,9κ con amplitudes de modulación pico-a-pico de 8 y 12 nm; continuo de estados oscuros→brillantes (platicones) controlado por detuning; dispositivos de 200 y 500 GHz, ~5 dB/faceta — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9170700/fullTextXML).
- Kim et al. 2017 (DOI ✔): acoplamiento resonante entre racetracks interior y exterior cuando sus caminos ópticos coinciden → supermodos simétrico (normal) y antisimétrico (anómalo); sensibilidad del punto de cruce a la longitud recta Δλ_c/ΔL_st ≈ −0,0029 (nm/µm según el contexto); acoplador tapered selecciona el modo antisimétrico — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5575100/fullTextXML).
- Kim et al. 2019 (DOI ✔ 10.1364/OL.44.004475): anillos acoplados con FSR 200/206 GHz (Vernier), gap 525 nm → splitting 7,1 GHz, calefactores de Pt en ambos anillos, procedimiento turn-key automatizado — [ar5iv 1907.07164](https://ar5iv.labs.arxiv.org/abs/1907.07164).
- Xue et al. 2015 LPR (DOI ✔ 10.1002/lpor.201500107): "may make it possible to generate microcombs in an extended wavelength range (e.g. in the visible) where material dispersion is likely to dominate" — [arXiv 1503.06142](https://arxiv.org/pdf/1503.06142).
- Slot: Zhang, Yue, Xiao-Li, Wang, Beausoleil, Willner, "Flat and low dispersion in highly nonlinear slot waveguides", Opt. Express 18, 13187 (2010), DOI ✔ 10.1364/OE.18.013187 (no confundir con "Flattened dispersion in silicon slot waveguides", OE 18, 20529); un supercontinuo de dos octavas en guía slot de Si₃N₄ reporta dispersión plana sobre 500 nm — [arXiv 1104.2954](https://arxiv.org/pdf/1104.2954).
- Air-clad: Moille et al. 2025 (DOI ✔ 10.1002/lpor.202401746): anillos de 410–430 nm con aire arriba y a los lados; facetas con óxido PECVD a baja temperatura por lift-off para acoplamiento; un cambio de ~25 nm en el ancho desplaza la onda dispersiva hasta ~10 THz — [arXiv 2404.01577](https://arxiv.org/html/2404.01577).
- Lihachev et al. 2022 (DOI ✔): "Compared with DKS microcombs that require specific designs and fabrication techniques for dispersion engineering, platicon microcombs can be readily built using CMOS-compatible platforms" y podrían facilitar la adopción "via commercial foundry service" — [ar5iv 2103.07795](https://ar5iv.labs.arxiv.org/html/2103.07795).
- TriPleX (LioniX): apilado de capas LPCVD de Si₃N₄ (p. ej. 220 nm) y TEOS-SiO₂ (250 nm) para evitar estrés de monocapas gruesas — [LioniX blog](https://www.lionix-international.com/about-us/blog/triplex-invention/).

### Inferences
- Para ANT (400 nm, grabado completo, calefactores TiW): la ruta de menor riesgo es **dos anillos acoplados con Vernier + calefactores** (Kim 2019), que no exige dispersión anómala, tolera errores de fabricación (el cruce se ajusta térmicamente) y da la mayor eficiencia; segunda opción, **PhCR** (modulación de pared de ~10 nm, por debajo del feature mínimo de 120 nm en cuanto a amplitud pero no en periodo: el periodo es ~λ/(2n_eff) ≈ 400–450 nm, compatible), con iniciación determinista pero mayor sensibilidad litográfica. Los anillos concéntricos (Kim 2017) producen dispersión anómala pero requieren acopladores tapered y bombeos de ~0,5 W.
- Si la aplicación es sensado bulk con ventana acuosa, la ruta de anillos acoplados permite separar físicamente el anillo generador (óxido) del anillo sensor; y la dispersión del anillo sensor es irrelevante para el peine si el acoplamiento solo sirve para el cruce evitado.
- El TM0 en 400 nm a 1550 nm no aparece en la literatura como ruta anómala: Moille 2025 solo logra anómalo TM a ≥ 384 THz (≈ 780 nm) y con aire. En óxido a 1550 nm el TM0 de 400 nm está aún más débilmente confinado que el TE0, lo que sugiere dispersión normal fuerte (inferencia; sin dato publicado).

### Gaps
- No se encontró ningún artículo de Si₃N₄ parcialmente grabado (rib) o multicapa aplicado a peines en dispersión normal; tampoco de slot con resonador (solo guías rectas).
- No se encontraron datos de TM0 en Si₃N₄ de 400 nm a 1550 nm.
- Grosor de Ligentec (800 nm) y de Hydex (1,45 µm) no confirmados en fuentes abiertas durante esta ronda (Razzari 2010, DOI ✔ 10.1038/nphoton.2009.236, confirmado como primer OPO en Hydex con umbral 54 mW, pero sin leer el grosor).

---

## P5. ¿Cómo permiten los cruces evitados (AMX) TE0–TM0, TE0–TE1 o entre anillos la iniciación del peine en dispersión normal?

### Takeaway
En dispersión normal no hay inestabilidad modulacional (MI) con bombeo CW porque la fase Kerr y la fase de dispersión tienen el mismo signo. Un AMX desplaza localmente una o pocas resonancias; (i) si el modo desplazado es el **bombeado** (Jang 2016, Yu 2022), la resonancia se alinea con el láser, la potencia intracavidad sube por encima del umbral de MI y se satisface fase para FWM "incondicionalmente"; (ii) si el modo desplazado es un **vecino** (Liu 2014, Xue 2015), cambia localmente el signo de la dispersión y una banda lateral inicial queda "anclada" al cruce, sembrando el peine que luego evoluciona a pulso oscuro. El ancho del peine escala aproximadamente linealmente con la fuerza del acoplamiento (Jang 2016).

### Cited Findings
- Liu, Xuan, Xue, Wang, Niu, Leaird, Qi, Weiner 2014, Optica 1, 137 (DOI ✔ 10.1364/OPTICA.1.000137): en anillos de Si₃N₄ de pocos modos con dispersión normal, el acoplamiento modal "can strongly modify the local dispersion, even changing its sign"; se observa el "pinning of one of the initial comb sidebands near a mode-crossing frequency", vinculando acoplamiento e iniciación — [arXiv 1405.6225](https://arxiv.org/pdf/1405.6225); [Purdue PDF](https://engineering.purdue.edu/~fsoptics/articles/Investigation_of_Mode_Coupling-Liu.pdf).
- Xue et al. 2015 Nat. Photon. (DOI ✔ 10.1038/nphoton.2015.137): "Dark pulse combs are formed in normal-dispersion microresonators with mode-interaction-assisted excitation"; la excitación parece determinista, en contraste con solitones brillantes — [ADS](https://ui.adsabs.harvard.edu/abs/2015NaPho...9..594X); [peeref](https://www.peeref.com/works/1117578).
- Jang, Okawachi, Yu, Luke, Ji, Lipson, Gaeta 2016, Opt. Express 24, 28794 (DOI ✔ 10.1364/OE.24.028794): Si₃N₄ 730 nm × 3000 nm (TE fundamental en GVD normal), FSR 200 GHz, L = 810 µm; β₂ = 36 ps²/km (1,8 ps²/km en el caso de banda ancha); el acoplamiento modal desplaza la resonancia bombeada ≈ 0,064 % del FSR (≈ 130 MHz a 1541,2 nm), lo que "boosts intracavity power above the MI threshold and seeds modulation-instability sidebands" incluso fuera de la región de biestabilidad Kerr; bombeo típico 5–10 mW en el bus (50 mW en la simulación de > 300 nm de ancho); relación aproximadamente lineal entre fuerza de acoplamiento y ancho del peine; extiende la analogía acoplamiento modal ↔ dispersión de orden alto al régimen normal — [ar5iv 1610.01143](https://ar5iv.labs.arxiv.org/html/1610.01143).
- Kim et al. 2019 (DOI ✔): el punto de degeneración entre anillos se coloca "a few modes above the pump wavelength" para compensar el corrimiento azul durante la sintonía; el bombeo se sitúa en la resonancia corrida al rojo del modo desdoblado; la secuencia observada es MI → llenado de líneas → estados multi-peine → estado ruidoso ancho → estado de bajo ruido con alta eficiencia — [ar5iv 1907.07164](https://ar5iv.labs.arxiv.org/abs/1907.07164).
- Yu et al. 2022 (DOI ✔): el término del PhC entra en la LLE como "effective pump contribution" (F′ > F en el nivel de alta intensidad), lo que cambia el balance energético entre los dos niveles de la onda de conmutación y permite el continuo oscuro↔brillante; los solitones de GVD normal "arise spontaneously from instability of the flat state" — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9170700/fullTextXML).
- Helgason et al. 2021 (DOI ✔): el desdoblamiento entre anillos acoplados ("split energy level") se cruza con el láser y forma ondas solitarias de manera reproducible — [Chalmers](https://research.chalmers.se/en/publication/522149).
- Fülöp et al. 2018 (DOI ✔): la generación "depends on modal coupling, so the spectral envelope is sensitive to fabrication variation"; 2 de 3 dispositivos similares funcionaron — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5913129/fullTextXML).
- Lihachev et al. 2022 (DOI ✔): alternativa sin AMX: el self-injection locking (retrodispersión Rayleigh hacia el DFB) excita directamente platicones "without sophisticated active control" — [ar5iv 2103.07795](https://ar5iv.labs.arxiv.org/html/2103.07795).

### Inferences
- Un AMX accidental TE0–TE1 o TE0–TM0 en un anillo monolítico (Liu 2014, Xue 2015, Fülöp 2018) funciona pero es poco reproducible (depende de la fabricación); el AMX entre anillos con calefactores (Xue 2015 LPR, Kim 2019, Helgason 2021) o la modulación PhC (Yu 2022) lo hacen determinista. En una guía de 400 nm × ~1–1,5 µm (prácticamente monomodo TE a 1550 nm) habrá pocos cruces intramodales accidentales, por lo que la ruta de dos anillos o PhC es casi obligatoria.
- El bombeo pulsado/biarmónico (Lobanov EPL 2015; Kim 2017 bicromático) es la tercera ruta de iniciación y no requiere AMX, a costa de un segundo láser.

### Gaps
- No pude leer el texto completo de Liu 2014 (grosor del anillo, valores de dispersión medidos, qué familias de modos cruzan); sólo el resumen.

---

## P6. Física del umbral de grosor (dispersión geométrica vs. material) y valores representativos de β₂/D₂ frente a grosor y ancho

### Takeaway
El Si₃N₄ tiene dispersión material normal en el NIR (Sellmeier de Luke 2015, n ≈ 1,996 a 1550 nm); sólo la dispersión de guía de onda (confinamiento fuerte, núcleo grueso y estrecho) puede compensarla, y eso ocurre para grosores > 600–700 nm a 1550 nm con cladding de óxido. Valores reportados: 300 nm → D ≈ −1200 ps/(nm·km) (muy normal); 530 nm × 2 µm → D₂/2π = −59,9 kHz a 26,2 GHz (β₂ ≈ +93 ps²/km); 600 nm × 2 µm → β₂ ≈ +130 ps²/km; 730 nm × 3 µm → β₂ ≈ +36 ps²/km; 730 nm × 1,0–1,5 µm → anómalo bajo. El grosor determina si existe un ancho que cruce a β₂ < 0; el ancho ajusta la magnitud.

### Cited Findings
- Luke, Okawachi, Lamont, Gaeta, Lipson 2015, Opt. Lett. 40, 4823 (DOI ✔ 10.1364/OL.40.004823): Sellmeier de Si₃N₄, n² − 1 = 3,0249 λ²/(λ² − 0,1353406²) + 40314 λ²/(λ² − 1239,842²) (λ en µm), rango 0,310–5,504 µm; n(1,55 µm) ≈ 1,996 — [refractiveindex.info](https://refractiveindex.info/?shelf=main&book=Si3N4&page=Luke).
- Kim et al. 2017 (DOI ✔): TE₁ en Si₃N₄ de 300 nm "around −1200 ps nm⁻¹ km⁻¹", típico de esa película; trabajos previos de peines usaron películas de "700–1,000 nm", propensas a grietas — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5575100/fullTextXML).
- Lihachev et al. 2022 (DOI ✔): anómalo a telecom requiere > 600 nm; dispositivo 530 nm × 2,00 µm con D₂/2π = −59,9 kHz (FSR 26,2 GHz) — [ar5iv 2103.07795](https://ar5iv.labs.arxiv.org/html/2103.07795).
- Xue et al. 2015 LPR (DOI ✔): anillos de ~600 nm × 2 µm (grosor según Fülöp 2018 para el mismo tipo de anillo) con β₂ ≈ 130 ps²/km — [arXiv 1503.06142](https://arxiv.org/pdf/1503.06142); [Fülöp Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5913129/fullTextXML).
- Jang et al. 2016 (DOI ✔): 730 nm × 3000 nm → β₂ = 36 ps²/km (normal) — [ar5iv 1610.01143](https://ar5iv.labs.arxiv.org/html/1610.01143). Kim et al. 2019 (DOI ✔): 730 nm × 1000 nm → TE fundamental también normal cerca de 1560 nm — [ar5iv 1907.07164](https://ar5iv.labs.arxiv.org/abs/1907.07164).
- Revisión (Si₃N₄ del visible al MIR): las guías canal necesitan "thicker than about 700 nm to get anomalous dispersion at 1550 nm" — [arXiv 2405.10038](https://arxiv.org/pdf/2405.10038); lo mismo en [SiNOS, ResearchGate](https://www.researchgate.net/publication/384109737_Thick_waveguides_of_low-stress_stoichiometric_silicon_nitride_on_sapphire_SiNOS).
- Un estudio experimental reporta GVD de −0,57 ps²/m (anómalo) a +0,86 ps²/m (normal) según la geometría de Si₃N₄ — [Academia.edu](https://www.academia.edu/51173682/Group_velocity_dispersion_and_self_phase_modulation_in_silicon_nitride_waveguides); un diseño de 730 nm × 1500 nm da GVD anómala baja cerca de 1561 nm — [ResearchGate](https://www.researchgate.net/publication/266261994_Dispersion_engineered_silicon_nitride_waveguides_by_geometrical_and_refractive-index_optimization).
- Moille et al. 2025 (DOI ✔): para H = 430 nm (TM, aire) la dispersión es anómala para RW entre 575 y 775 nm; ancho y grosor fijan la dispersión geométrica que compensa la material; el límite anómalo depende de ambos y del cladding (óxido: ≈ 315 THz) — [arXiv 2404.01577](https://arxiv.org/html/2404.01577).
- Moss, Morandotti, Gaeta, Lipson 2013, Nat. Photon. 7, 597 (DOI ✔ 10.1038/nphoton.2013.183): revisión de Si₃N₄ y Hydex como plataformas CMOS para óptica no lineal; Hydex con dispersión anómala en la mayor parte de la banda C, cero de GVD en 1600 nm (TE) y 1560 nm (TM) — [arXiv 1404.7619](https://arxiv.org/pdf/1404.7619); [RMIT](https://research-repository.rmit.edu.au/articles/journal_contribution/New_CMOS-compatible_platforms_based_on_silicon_nitride_and_hydex_for_nonlinear_optics/27466647).

### Inferences
- Tabla resumen (cladding SiO₂, TE0, ~1550 nm; mezcla de valores citados y conversión propia 1 ps²/km ≈ −0,78 ps/(nm·km)):

  | Grosor × ancho | β₂ (ps²/km) | D (ps/(nm·km)) | Fuente |
  |---|---|---|---|
  | 300 nm (TE₁, anillo interior) | ≈ +1500 | ≈ −1200 | Kim 2017 |
  | 530 nm × 2,0 µm | ≈ +93 (calc.) | ≈ −73 | Lihachev 2022 (D₂/2π = −59,9 kHz) |
  | 600 nm × 2,0 µm | ≈ +130 | ≈ −100 | Xue 2015 LPR |
  | 730 nm × 3,0 µm | +36 | ≈ −28 | Jang 2016 |
  | 730 nm × 1,0 µm | > 0 (normal, pequeño) | — | Kim 2019 |
  | 730 nm × 1,5 µm | < 0 (anómalo bajo) | — | ResearchGate 2014 |
  | 410–430 nm, aire, 780–1060 nm | < 0 | — | Moille 2025 |

- Para 400 nm × (1–2) µm con óxido a 1550 nm, interpolando entre 300 nm (−1200) y 530 nm (−73) se espera D ≈ −300 … −600 ps/(nm·km) (β₂ ≈ +400…+800 ps²/km), fuertemente normal; D₂ para FSR ~100 GHz sería del orden de −(1–3) MHz. **Debe verificarse con FDE** (Lumerical MODE) usando el Sellmeier de Luke 2015.
- Físicamente: la dispersión de guía de onda es negativa (anómala) cuando el modo está cerca del corte lateral/vertical en un núcleo de alto contraste; en películas delgadas el modo se extiende al óxido, la n_eff sigue al cladding y domina la dispersión material (normal) del Si₃N₄ y del SiO₂. Bajar el índice del cladding (aire, agua) aumenta el contraste y recupera parte de la dispersión geométrica (Moille 2025).

### Gaps
- No se encontró una tabla publicada de β₂ vs. grosor a 1550 nm que incluya 400 nm; los valores para 400 nm son extrapolación propia.
- Grosor de Hydex (1,45 µm) y TriPleX total no confirmados en fuente primaria en esta ronda.

---

## P7. Ancho de banda alcanzable en dispersión normal (pulsos oscuros) frente a anómala

### Takeaway
Los pulsos oscuros/platicones demostrados en telecom cubren ≈ 35–90 nm (4–11 THz); el PhCR de tantalio de Yu 2022 llega a ≈ 30 THz con 21 % de eficiencia; en anómala, el mismo Si₃N₄ delgado air-clad da 125–220 THz (octava) a 400 mW. Los artículos de plataforma reconocen que los pulsos oscuros están "constrained by limited bandwidth and uneven spectra", aunque Fülöp 2018 afirma que los límites observados "are not fundamental". El "supercontinuo en dispersión normal" de guías rectas (ensanchamiento por SPM/OWB con pulsos fs) es un mecanismo distinto que no aplica a bombeo CW en un anillo.

### Cited Findings
- Kim 2019: 1495–1583 nm (≈ 88 nm) con 41 % — [ar5iv 1907.07164](https://ar5iv.labs.arxiv.org/abs/1907.07164). Fülöp 2018: 20 líneas usadas 1531–1566 nm, > 20 % — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5913129/fullTextXML). Xue 2015/2017: 40 líneas 1513–1586 nm — [arXiv 1610.00958](https://arxiv.org/pdf/1610.00958). Kim 2017 (300 nm concéntrico, anómalo por acoplamiento): peine type-II ≈ 180 nm; mode-locked más estrecho — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5575100/fullTextXML).
- Yu 2022 (PhCR Ta₂O₅, normal): ≈ 180–210 THz (≈ 30 THz), 33 mW → 7 mW, 21 % — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9170700/fullTextXML).
- Moille 2025 (Si₃N₄ 410–430 nm, aire, anómalo en visible/NIR): 125 THz (MI), 220 THz (octava, 400 mW), ~130 THz (dual-DW TM) — [arXiv 2404.01577](https://arxiv.org/html/2404.01577).
- Jang 2016: ancho de peine ∝ fuerza de acoplamiento (≈ lineal); simulación con 260 MHz de desplazamiento y 50 mW abarca > 300 nm — [ar5iv 1610.01143](https://ar5iv.labs.arxiv.org/html/1610.01143).
- Helgason 2023: solitones brillantes convencionales ≈ 1 % de eficiencia ("fundamental limitation"); con anillos acoplados > 50 % — [arXiv 2202.09410](https://arxiv.org/abs/2202.09410).
- Zhang 2024 (APL, fragmento): pulsos oscuros "constrained by limited bandwidth and uneven spectra" — [ResearchGate](https://www.researchgate.net/publication/384097443_300-nm-thick_ultralow-loss_silicon_nitride_photonic_integrated_circuits_by_8-in_foundry_production).
- Xue 2017 LPR: los pulsos oscuros "can be much wider than the bright solitons" (en el dominio temporal), lo que implica espectros más estrechos pero más eficientes — [arXiv 1610.00958](https://arxiv.org/pdf/1610.00958).

### Inferences
- Para una guía de 400 nm fuertemente normal (β₂ ~ +500 ps²/km) el ancho de un pulso oscuro escalará aún menos que en los dispositivos de 600–730 nm (β₂ ~ +40…+130 ps²/km): a igual potencia y acoplamiento modal se esperan decenas de nm como máximo. El PhCR (Yu 2022) es la única ruta normal que mostró decenas de THz, pero en tantalio de 570 nm, no en Si₃N₄ delgado.
- Si el objetivo del proyecto es "supercontinuo-like" (≥ 100 THz) en 400 nm de Si₃N₄, la literatura indica que hay que mover el bombeo al visible/NIR con cladding de aire (Moille 2025) o usar bombeo pulsado; a 1550 nm con óxido la expectativa realista es un peine de pulso oscuro de 20–80 nm.

### Gaps
- No se investigó en esta ronda la literatura específica de supercontinuo en dispersión normal en guías rectas (SPM/optical wave breaking con pulsos fs); se menciona sólo como mecanismo distinto.
- No se encontró un trabajo que cuantifique el ancho máximo teórico de un pulso oscuro en función de β₂ y del acoplamiento modal, salvo la tendencia lineal de Jang 2016.

---

## Lista de referencias con DOI verificado (resueltos en doi.org el 2026-10-29)

| Ref. | DOI | Redirige a |
|---|---|---|
| Xue et al., Nat. Photon. 9, 594 (2015) | 10.1038/nphoton.2015.137 ✔ | nature.com/articles/nphoton.2015.137 |
| Xue et al., LPR 9, L23 (2015) | 10.1002/lpor.201500107 ✔ | onlinelibrary.wiley.com |
| Xue et al., LPR 11, 1600276 (2017) | 10.1002/lpor.201600276 ✔ | onlinelibrary.wiley.com |
| Lobanov et al., Opt. Express 23, 7713 (2015) | 10.1364/OE.23.007713 ✔ | opg.optica.org oe-23-6-7713 |
| Lobanov et al., EPL 112, 54008 (2015) | 10.1209/0295-5075/112/54008 ✔ | iopscience.iop.org |
| Liu et al., Optica 1, 137 (2014) | 10.1364/OPTICA.1.000137 ✔ | opg.optica.org optica-1-3-137 |
| Jang et al., Opt. Express 24, 28794 (2016) | 10.1364/OE.24.028794 ✔ | opg.optica.org oe-24-25-28794 |
| Fülöp et al., Nat. Commun. 9, 1598 (2018) | 10.1038/s41467-018-04046-6 ✔ | nature.com |
| Kim et al., Opt. Lett. 44, 4475 (2019) | 10.1364/OL.44.004475 ✔ | opg.optica.org ol-44-18-4475 |
| Helgason et al., Nat. Photon. 15, 305 (2021) | 10.1038/s41566-020-00757-9 ✔ | nature.com |
| Helgason et al., Nat. Photon. 17, 992 (2023) | 10.1038/s41566-023-01280-3 ✔ | nature.com |
| Lihachev et al., Nat. Commun. 13, 1771 (2022) | 10.1038/s41467-022-29431-0 ✔ | nature.com |
| Kim et al., Nat. Commun. 8, 372 (2017) | 10.1038/s41467-017-00491-x ✔ | nature.com |
| Yu et al., Nat. Photon. 15, 461 (2021) | 10.1038/s41566-021-00800-3 ✔ | nature.com |
| Yu et al., Nat. Commun. 13 (2022) | 10.1038/s41467-022-30774-x ✔ | nature.com |
| Moille et al., Commun. Phys. 6, 144 (2023) | 10.1038/s42005-023-01253-6 ✔ | nature.com |
| Lucas et al., Nat. Photon. 17, 943 (2023) | 10.1038/s41566-023-01252-7 ✔ | nature.com |
| Moille et al., LPR (2025) | 10.1002/lpor.202401746 ✔ | onlinelibrary.wiley.com |
| Zhang et al., APL 125, 121111 (2024) | 10.1063/5.0221409 ✔ | pubs.aip.org |
| Luke et al., Opt. Lett. 40, 4823 (2015) | 10.1364/OL.40.004823 ✔ | opg.optica.org ol-40-21-4823 |
| Moss et al., Nat. Photon. 7, 597 (2013) | 10.1038/nphoton.2013.183 ✔ | nature.com |
| Razzari et al., Nat. Photon. 4, 41 (2010) | 10.1038/nphoton.2009.236 ✔ | nature.com |
| Zhang et al., Opt. Express 18, 13187 (2010) | 10.1364/OE.18.013187 ✔ | opg.optica.org oe-18-12-13187 |
| Kedenburg et al., Opt. Mater. Express 2, 1588 (2012) | 10.1364/OME.2.001588 ✔ | opg.optica.org ome-2-11-1588 |
| Hale & Querry, Appl. Opt. 12, 555 (1973) | 10.1364/AO.12.000555 ✔ | opg.optica.org ao-12-3-555 |
| Nazemosadat et al., PRA 103, 013513 (2021) | 10.1103/PhysRevA.103.013513 (resuelve en APS; emparejamiento título–DOI **sin verificar**) | link.aps.org |
| Long et al., arXiv 2505.00352 (2025) | sin DOI de revista (preprint) | arxiv.org |
| Sabouri et al., CLEO/Europe-EQEC 2019 ef_p_3 | DOI sin verificar | opg.optica.org / IEEE 8872841 |
