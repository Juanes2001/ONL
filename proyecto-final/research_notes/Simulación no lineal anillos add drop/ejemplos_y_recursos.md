# Ejemplos publicados y recursos de aprendizaje: simulación de peines Kerr y supercontinuo en microanillos de Si3N4 (énfasis add-drop, Si3N4 delgado/dispersión normal, Lumerical)

Fecha de la búsqueda: 2026-10-26. Contexto: anillo add-drop de Si3N4 de 400 nm de espesor, 1550 nm, usado como refractómetro de volumen (cladding acuoso n = 1.33 → 1.37).

**Verificación de DOI.** Todos los DOI marcados [VERIFICADO] se resolvieron con `api.crossref.org/works/<doi>` el 2026-10-26, y Crossref devolvió el mismo primer autor, título, revista, volumen y página que se citan aquí. "NO VERIFICADO" = no se encontró DOI o el registro de Crossref no se comprobó. Los resúmenes del método ("qué da") salen de abstracts y fragmentos de búsqueda, o se conocen de antemano del artículo. Antes de citar un parámetro numérico concreto, revisar el texto completo.

Nota sobre los años: Crossref da 2013 para Herr et al. (Nat. Photon. **8**, 2014) y 2012 para Coen et al. (Opt. Lett. **38**, 2013), porque registra la fecha de publicación en línea. El volumen corresponde al año que se usa en la cita.

---

## 1. Artículos que simulan peines/solitones/pulsos oscuros en anillos de Si3N4 add-drop, o que extraen el peine por el puerto drop

### Takeaway
Hay pocos artículos centrados en simular peines con LLE en el puerto drop. La referencia experimental y de modelado de potencia es el trabajo de Purdue (Wang et al. 2013 y 2016, y la tesis de P.-H. Wang). Ahí se ve que el puerto drop entrega el campo intracavidad filtrado, con un bombeo mucho menos dominante que en el puerto through. Para simularlo basta la LLE estándar, sumando la pérdida del segundo acoplador al amortiguamiento total y tomando la salida drop como √κ_drop·ψ.

### Cited Findings
- **Wang, P.-H. et al., "Drop-port study of microresonator frequency combs: power transfer, spectra and time-domain characterization", *Opt. Express* 21, 22441 (2013).** DOI 10.1364/OE.21.022441 [VERIFICADO]. Es un anillo de Si3N4 con puerto drop. Analiza la transferencia de potencia entre through y drop y compara espectros y dominio temporal. Es la referencia directa para el diseño add-drop: muestra qué se mide en cada puerto. PDF del grupo: [Purdue fsoptics](https://engineering.purdue.edu/~fsoptics/articles/Drop-Port_Study-Wang.pdf)
- **Wang, P.-H. et al., "Intracavity characterization of micro-comb generation in the single-soliton regime", *Opt. Express* 24, 10890 (2016).** DOI 10.1364/OE.24.010890 [VERIFICADO]. Mide el campo intracavidad del solitón a través del puerto drop. La mayor parte de la potencia intracavidad está en el solitón, mientras que el through queda dominado por el bombeo. Sirve para validar una simulación LLE del puerto drop. PDF: [Purdue fsoptics](https://engineering.purdue.edu/~fsoptics/articles/Intracavity_characterization-Wang.pdf); resumen del hallazgo en la [búsqueda](https://engineering.purdue.edu/~fsoptics/articles/Intracavity_characterization-Wang.pdf)
- **Tesis doctoral de Pei-Hsun Wang (Purdue, 2016, director A. M. Weiner), "On-chip microresonator frequency combs: Generation dynamics, power transfer, and time-domain characterization".** Tiene capítulos sobre generación de peines en Si3N4, puerto drop y transferencia de potencia, y caracterización temporal. Sin DOI. Disponible en [PDF](https://engineering.purdue.edu/~fsoptics/thesis/Wang__Pei-Hsun_PhD.pdf) y en el [registro de Purdue](https://docs.lib.purdue.edu/dissertations/AAI10149180)
- **Grudinin, I. S. et al., "High-contrast Kerr frequency combs", arXiv:1612.00820 (2016).** DOI de arXiv 10.48550/arXiv.1612.00820 [NO VERIFICADO en Crossref]. Usa MgF2 y no Si3N4. Explica en teoría y muestra en experimento que, con acopladores add-drop, el armónico del bombeo queda deprimido en el drop. Sirve como argumento físico para preferir el drop como salida del peine — [arXiv](https://arxiv.org/abs/1612.00820)
- **Wang, Y. et al. (grupo de Q.-F. Yang, PKU), "Program gain and loss for broadband soliton microcombs", arXiv:2604.19913 (abril de 2026).** Preprint sin DOI de revista. Trabaja con microrresonadores de Si3N4 con un "meta-coupler" programado litográficamente. Según el fragmento de búsqueda, modela espectros through y drop con una ecuación tipo LLE que incluye dispersión, Raman y acoplamiento dependiente de λ obtenido por elementos finitos (Q₀ = 1.0×10⁷, 261 mW). La página del abstract no confirma esos detalles — [arXiv](https://arxiv.org/abs/2604.19913)
- **Helgason, Ó. B. et al., "Dissipative solitons in photonic molecules", *Nat. Photon.* 15, 305–310 (2021).** DOI 10.1038/s41566-020-00757-9 [VERIFICADO]. Usa dos anillos de Si3N4 acoplados linealmente (dispersión normal). El acoplamiento entre anillos crea la condición de arranque de pulsos oscuros, y el artículo incluye modelado LLE acoplado. Sirve de análogo cercano para una arquitectura de varios puertos o anillos.

### Inferences
- En un anillo add-drop basta añadir κ_drop al amortiguamiento total de la LLE: α_total = α_i + κ_bus + κ_drop. El campo drop es √κ_drop·ψ y no lleva el término de interferencia con el bombeo. Este planteamiento es consistente con Wang 2013/2016, pero ninguno de los artículos revisados lo escribe como receta explícita.
- Para el refractómetro, el puerto drop da un pico lorentziano sin fondo. Si en algún momento se bombea por encima del umbral, ese mismo puerto da un espectro de peine sin el bombeo dominante.

### Gaps
- No encontré un artículo dedicado *exclusivamente* a la simulación LLE del puerto drop en Si3N4 de 400 nm.
- No verifiqué en texto completo los parámetros del preprint 2604.19913.

---

## 2. Peines/supercontinuo en Si3N4 de dispersión normal o delgado (≤ 400–500 nm), y anillos bombeados con pulsos

### Takeaway
Un Si3N4 de 400 nm a 1550 nm con cladding de óxido o agua tiene típicamente dispersión normal. En ese régimen no hay solitones brillantes. Hay pulsos oscuros/platicones, que requieren un mecanismo de arranque: cruce evitado de modos (AMX), anillos acoplados o autoinyección. También se puede bombear con pulsos. Las referencias base son Xue 2015 (Nat. Photon.), Liu 2014 (Optica), Lobanov 2015, Godey 2014 (teoría), Helgason/Fülöp (Chalmers), Kim 2017 (Si3N4 delgado concéntrico) y Obrzud/Anderson (bombeo pulsado).

### Cited Findings
**Dispersión normal / pulsos oscuros**
- **Xue, X. et al., "Mode-locked dark pulse Kerr combs in normal-dispersion microresonators", *Nat. Photon.* 9, 594–600 (2015).** DOI 10.1038/nphoton.2015.137 [VERIFICADO]. Es el trabajo de referencia sobre pulsos oscuros en Si3N4 de dispersión normal con interacción de modos. Incluye simulación LLE con un desplazamiento de fase en el modo vecino que modela el AMX.
- **Liu, Y. et al., "Investigation of mode coupling in normal-dispersion silicon nitride microresonators for Kerr frequency comb generation", *Optica* 1, 137 (2014).** DOI 10.1364/OPTICA.1.000137 [VERIFICADO]. Estudia anillos de Si3N4 pocos-modo con dispersión normal. Muestra que el acoplamiento de modos modifica la dispersión local, incluso cambiándole el signo, y que la LLE con un término de desplazamiento de fase reproduce peines coherentes tipo I. Ver el [preprint arXiv 1405.6225](https://arxiv.org/pdf/1405.6225) y el [PDF de Purdue](https://engineering.purdue.edu/~fsoptics/articles/Investigation_of_Mode_Coupling-Liu.pdf)
- **Xue, X. et al., "Normal-dispersion microcombs enabled by controllable mode interactions", *Laser Photon. Rev.* 9, L23 (2015).** DOI 10.1002/lpor.201500107 [VERIFICADO]. Controla la interacción de modos con anillos acoplados (Si3N4).
- **Xue, X. et al., "Microresonator Kerr frequency combs with high conversion efficiency", *Laser Photon. Rev.* 11, 1600276 (2017).** DOI 10.1002/lpor.201600276 [VERIFICADO]. Mide y simula la eficiencia de conversión de pulsos oscuros frente a solitones brillantes. Sirve para estimar la potencia por línea.
- **Lobanov, V. E. et al., "Frequency combs and platicons in optical microresonators with normal GVD", *Opt. Express* 23, 7713 (2015).** DOI 10.1364/OE.23.007713 [VERIFICADO]. Teoría y simulación LLE de platicones con bombeo modulado o AMX.
- **Godey, C. et al., "Stability analysis of the spatiotemporal Lugiato-Lefever model for Kerr optical frequency combs in the anomalous and normal dispersion regimes", *Phys. Rev. A* 89, 063814 (2014).** DOI 10.1103/PhysRevA.89.063814 [VERIFICADO]. Mapa de estabilidad (desintonía–bombeo) en ambos regímenes. Sirve para ubicar los parámetros normalizados del anillo.
- **Fülöp, A. et al., "High-order coherent communications using mode-locked dark-pulse Kerr combs from microresonators", *Nat. Commun.* 9, 1598 (2018).** DOI 10.1038/s41467-018-04046-6 [VERIFICADO]. Pulsos oscuros en Si3N4 (Chalmers). Ver también el [registro de Chalmers](https://research.chalmers.se/en/publication/?id=501179)
- **Nazemosadat, E. et al., "Switching dynamics of dark-pulse Kerr frequency comb states in optical microresonators", *Phys. Rev. A* 103, 013513 (2021).** DOI 10.1103/PhysRevA.103.013513 [VERIFICADO]. Simulación LLE con AMX de la conmutación determinista entre estados oscuros. Hay [texto completo en Chalmers](https://research.chalmers.se/publication/522243/file/522243_Fulltext.pdf)
- **Kim, B. Y. et al., "Turn-key, high-efficiency Kerr comb source", *Opt. Lett.* 44, 4475 (2019).** DOI 10.1364/OL.44.004475 [VERIFICADO]. Pulsos oscuros en Si3N4 con arranque "turn-key" por anillos acoplados.
- **Lihachev, G. et al., "Platicon microcomb generation using laser self-injection locking", *Nat. Commun.* 13, 1771 (2022).** DOI 10.1038/s41467-022-29431-0 [VERIFICADO]. Platicones en Si3N4 de dispersión normal por autoinyección.
- **Anderson, M. H. et al., "Zero dispersion Kerr solitons in optical microresonators", *Nat. Commun.* 13, 4764 (2022).** DOI 10.1038/s41467-022-31916-x [VERIFICADO]. Aplica cuando β2 ≈ 0 y domina la dispersión de 3.er orden, un caso posible al variar el ancho en 400 nm.

**Si3N4 delgado**
- **Kim, S. et al., "Dispersion engineering and frequency comb generation in thin silicon nitride concentric microresonators", *Nat. Commun.* 8, 372 (2017).** DOI 10.1038/s41467-017-00491-x [VERIFICADO]. **Es el más cercano a 400 nm.** Usa anillos concéntricos de Si3N4 delgado para obtener dispersión anómala en el supermodo antisimétrico. Según el fragmento de [ResearchGate](https://www.researchgate.net/publication/319337561_Dispersion_engineering_and_frequency_comb_generation_in_thin_silicon_nitride_concentric_microresonators), el índice de cada modo se calculó con **Lumerical**, y una guía de Si3N4 de 300 nm tiene D ≈ −1200 ps/(nm·km), lo que impide el peine. No pude abrir el texto completo (Nature redirige a login).
- **Sabouri, S. et al., "Dark frequency comb formation in thin silicon nitride normal dispersion microresonator", CLEO/Europe-EQEC 2019.** DOI 10.1109/CLEOE-EQEC.2019.8872841 [VERIFICADO]. Estudio numérico de un anillo de Si3N4 delgado monomodo con GVD normal. Obtiene pulsos oscuros, breathers y "complex solitons". Ver el [portal de TU Dresden](https://fis.tu-dresden.de/portal/en/publications/dark-frequency-comb-formation-in-thin-silicon-nitride-normal-dispersion-microresonator(afbf9ea1-64cf-4768-a5e5-f178dfbb78fc).html)
- **Liu, J. et al., "High-yield, wafer-scale fabrication of ultralow-loss, dispersion-engineered silicon nitride photonic circuits", *Nat. Commun.* 12, 2236 (2021).** DOI 10.1038/s41467-021-21973-z [VERIFICADO]. Trabaja con Si3N4 grueso (anómalo). Sirve como contraste y para ver cómo reportan D_int y Q.
- **Ji, X. et al., "Ultra-low-loss on-chip resonators with sub-milliwatt parametric oscillation threshold", *Optica* 4, 619 (2017).** DOI 10.1364/OPTICA.4.000619 [VERIFICADO]. Fórmulas y valores del umbral OPO en función de Q y V_eff en Si3N4.
- **Ji, X. et al., "Methods to achieve ultra-high quality factor silicon nitride resonators", *APL Photonics* 6, 071101 (2021).** DOI 10.1063/5.0057881 [VERIFICADO]. Tutorial de pérdidas en Si3N4. Útil para fijar α_i en la LLE.
- **Preprint (2024), "Broadband visible wavelength microcomb generation in silicon nitride microrings through air-clad dispersion engineering", arXiv:2404.01577.** Película de 400 nm con cladding de aire: abre ventana anómala en el visible. El fragmento recuerda que con dispersión normal no hay excitación suave del peine — [arXiv](https://arxiv.org/pdf/2404.01577)
- **Preprint arXiv:2601.04047 (2026).** Según el fragmento, parte de películas de Si3N4 de 400 nm sin grietas y genera peines de una octava visible–NIR bombeados con pulsos fs de Ti:zafiro. No obtuve el título ni los autores (la API de arXiv no respondió) — [arXiv](https://arxiv.org/pdf/2601.04047)

**Bombeo pulsado / supercontinuo resonante**
- **Obrzud, E., Lecomte, S., Herr, T., "Temporal solitons in microresonators driven by optical pulses", *Nat. Photon.* 11, 600–607 (2017).** DOI 10.1038/nphoton.2017.140 [VERIFICADO]. Es la LLE con bombeo pulsado, con la tasa de pulsos igual al FSR (o un múltiplo).
- **Malinowski, M. et al., "Optical frequency comb generation by pulsed pumping", *APL Photonics* 2, 066101 (2017).** DOI 10.1063/1.4983113 [VERIFICADO]. Teoría y simulación de peines con bombeo pulsado.
- **Anderson, M. H. et al., "Photonic chip-based resonant supercontinuum via pulse-driven Kerr microresonator solitons", *Optica* 8, 771 (2021).** DOI 10.1364/OPTICA.403302 [VERIFICADO]. Supercontinuo resonante en Si3N4 bombeado con pulsos. **Nota:** el DOI 10.1364/OPTICA.418848 que tenía de memoria NO existe en Crossref; el correcto es .403302.
- **Xu, Y. et al., "Frequency comb generation in a pulse-pumped normal dispersion Kerr mini-resonator", *Opt. Lett.* 46, 512 (2021).** DOI 10.1364/OL.413585 [VERIFICADO]. Peine con bombeo pulsado en dispersión normal. Es el caso más análogo a un Si3N4 de 400 nm normal.

**Supercontinuo en guías de Si3N4 (GNLSE)**
- **Johnson, A. R. et al., "Octave-spanning coherent supercontinuum generation in a silicon nitride waveguide", *Opt. Lett.* 40, 5117 (2015).** DOI 10.1364/OL.40.005117 [VERIFICADO].
- **Epping, J. P. et al., "On-chip visible-to-infrared supercontinuum generation with more than 495 THz spectral bandwidth", *Opt. Express* 23, 19596 (2015).** DOI 10.1364/OE.23.019596 [VERIFICADO]. Si3N4 (TriPleX); GNLSE con dispersión calculada por modos.
- **Porcel, M. A. G. et al., "Two-octave spanning supercontinuum generation in stoichiometric silicon nitride waveguides pumped at telecom wavelengths", *Opt. Express* 25, 1542 (2017).** DOI 10.1364/OE.25.001542 [VERIFICADO]. Bombeo a 1.56 µm; GNLSE.

### Inferences
- Con un Si3N4 de 400 nm, una simulación realista a 1550 nm debe empezar por la D_int de MODE/FDE. Si D2 < 0 (normal), hay tres caminos: (i) modelar un AMX con un desplazamiento de fase en un modo (Xue 2015; Liu 2014), (ii) anillos acoplados (Helgason; Kim 2019) o (iii) bombeo pulsado (Xu 2021; Obrzud 2017).
- Cambiar el cladding de óxido a agua (n ≈ 1.33) modifica la dispersión. Choi & Su 2022 (sección 3) reportan que en agua cambian la dispersión, el acople y el Q. Hay que recalcular D_int con cladding de agua para cada n del analito.

### Gaps
- No verifiqué en texto completo que Kim 2017 diga literalmente "Lumerical MODE/FDE". La afirmación viene de un fragmento de ResearchGate.
- No encontré un artículo con la combinación exacta "Si3N4 de 400 nm + add-drop + pulsos oscuros a 1550 nm + cladding acuoso".

---

## 3. Artículos que dicen explícitamente "dispersión calculada con Lumerical MODE/FDE" + LLE

### Takeaway
La evidencia directa es escasa. Muchos trabajos usan FEM (COMSOL) o "un solver de modos" sin nombrarlo, y en los abstracts revisados no hallé un artículo de Si3N4 que diga "Lumerical MODE + LLE". El indicio más fuerte es Kim et al. 2017 (Lumerical para índices modales, según un fragmento). El flujo estándar es: FDE → n_eff(λ) → D_int(μ) = ω_μ − ω_0 − D1·μ → LLE (pyLLE o un código propio split-step).

### Cited Findings
- Kim et al. 2017 (Nat. Commun. 8, 372): calcularon con Lumerical el índice de cada modo del anillo concéntrico y de ahí la dispersión — [ResearchGate (fragmento)](https://www.researchgate.net/publication/319337561_Dispersion_engineering_and_frequency_comb_generation_in_thin_silicon_nitride_concentric_microresonators)
- **Moille, G., Li, Q., Lu, X., Srinivasan, K., "pyLLE: A fast and user friendly Lugiato-Lefever equation solver", *J. Res. NIST* 124, 124012 (2019).** DOI 10.6028/jres.124.012 [VERIFICADO]. Es un solver abierto (Python + Julia) que acepta como entrada la dispersión (frecuencias de resonancia por modo) de un solver externo, como Lumerical o COMSOL. Recursos: [PDF NIST](https://nvlpubs.nist.gov/nistpubs/jres/124/jres.124.012.pdf), docs en usnistgov.github.io/pyLLE y código en github.com/gregmoille/pylle (la v4.0.0 puede diferir de la 2.1 del artículo, según el [listado de búsqueda](https://awesome.ecosyste.ms/projects/github.com%2Fgregmoille%2Fpylle))
- Otros artículos de Si3N4 calculan la dispersión con métodos numéricos que el fragmento no nombra y la alimentan a la LLE. Por ejemplo, el estudio sobre condiciones de crecimiento del Si3N4 muestra que el espesor y la razón de gases desplazan los cruces por cero de la dispersión y el espectro LLE — [arXiv 2109.03291](https://arxiv.org/html/2109.03291)

### Inferences
- Para el proyecto: (1) Lumerical FDE (ya en el pipeline de `seccion_v1`) con barrido en λ y en el n del cladding; (2) exportar n_eff(λ) o D_int(μ); (3) pyLLE o un split-step propio. Así el uso de Lumerical queda justificado aunque no haya un artículo "plantilla" exacto.

### Gaps
- No encontré ningún artículo revisado por pares que nombre explícitamente "Lumerical MODE (FDE)" junto a LLE en Si3N4 y cuyo texto completo haya podido confirmar. Haría falta una búsqueda en texto completo (Google Scholar: "Lumerical" "Lugiato-Lefever" silicon nitride).

---

## 4. Microcombs/supercontinuo + sensado (índice, bio, gas), en particular en cladding acuoso

### Takeaway
El sensado con microcombs está dominado por la espectroscopía dual-comb de gases y por el sensado de gases con funcionalización (grafeno). Hay un solo trabajo de peines en entorno acuoso (Choi & Su 2022, microtoroide) y uno de refractometría interrogada con un peine (Knoerzer 2019, peine no Kerr con MZI de Si). No hallé refractometría de volumen con un solitón Kerr en Si3N4 acuoso: es un hueco que el proyecto podría señalar.

### Cited Findings
- **Suh, M.-G. et al., "Microresonator soliton dual-comb spectroscopy", *Science* 354, 600–603 (2016).** DOI 10.1126/science.aah6516 [VERIFICADO]. Es la demostración base de espectroscopía dual-comb con solitones.
- **Dutt, A. et al., "On-chip dual-comb source for spectroscopy", *Sci. Adv.* 4, e1701858 (2018).** DOI 10.1126/sciadv.1701858 [VERIFICADO]. Fuente dual-comb en un chip de Si3N4.
- **Yu, M. et al., "Silicon-chip-based mid-infrared dual-comb spectroscopy", *Nat. Commun.* 9, 1869 (2018).** DOI 10.1038/s41467-018-04350-1 [VERIFICADO].
- **Tan, T. et al., "Multispecies and individual gas molecule detection using Stokes solitons in a graphene over-modal microresonator", *Nat. Commun.* 12, 6716 (2021).** DOI 10.1038/s41467-021-26740-8 [VERIFICADO]. Usa una microesfera con grafeno depositado de forma asimétrica. Los batidos entre solitones de Stokes dan una detección de gas muy sensible. Requiere funcionalización, fuera del alcance actual — [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8602637/)
- **Knoerzer, M. et al., "Optical frequency comb based system for photonic refractive index sensor interrogation", *Opt. Express* 27, 21532 (2019).** DOI 10.1364/OE.27.021532 [VERIFICADO]. Un peine muestrea un MZI a 120° y recupera la fase con tres líneas. El límite de detección del sensor, 3.70×10⁻⁷ RIU, no se degrada — [CQU](https://acquire.cqu.edu.au/articles/journal_contribution/Optical_frequency_comb_based_system_for_photonic_refractive_index_sensor_interrogation/13454297/2). Es el antecedente más cercano a "refractometría con peine".
- **Choi, H., Su, J. et al., "Optical frequency combs in aqueous and air environments at visible to near-IR wavelengths", *Opt. Express* 30, 8690 (2022).** DOI 10.1364/OE.451631 [VERIFICADO]. Microtoroide de sílice en agua. Señala que en entorno acuoso cambian la dispersión, la estabilidad del acople y el Q. Usa acoplamiento intermodal para obtener dispersión anómala local — [Arizona](https://experts.arizona.edu/en/publications/optical-frequency-comb-generation-using-a-microtoroid-resonator-i/). Es la referencia clave para el "cladding acuoso".
- **Diakonov, A. et al., "Broadband cavity-enhanced Kerr comb spectroscopy on chip", *npj Nanophotonics* 1 (2024).** DOI 10.1038/s44310-024-00047-0 [VERIFICADO]. Acopla un microcomb a una microcavidad para hacer espectroscopía en chip potenciada por cavidad. Propone acoplar el analito evanescentemente al modo guiado (como guía, no como medida acuosa demostrada) — [arXiv 2403.11235](https://arxiv.org/html/2403.11235v1)
- **Tomasetig et al., "Si3N4 microring resonator-based refractive index sensing for liquid samples: comparing wavelength scanning and fixed-wavelength probing", *ACS Meas. Sci. Au* (2025).** DOI NO VERIFICADO (Crossref no respondió). Es un anillo de Si3N4 con microfluídica y láser convencional, sin peine. Sirve de referencia lineal del refractómetro — [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12921590/)
- **Revisiones de aplicaciones:** Sun, Y. et al., "Applications of optical microcombs", *Adv. Opt. Photon.* 15, 86 (2023), DOI 10.1364/AOP.470264 [VERIFICADO]. Yao, B. et al., "Interdisciplinary advances in microcombs: bridging physics and information technology", *eLight* 4, 19 (2024), DOI 10.1186/s43593-024-00071-9 [VERIFICADO], que cita a Knoerzer y señala que los materiales inertes (sílice, Si3N4) dificultan el sensado por adsorción — [eLight](https://link.springer.com/article/10.1186/s43593-024-00071-9). Shu, H. et al., "Microcomb technology: from principles to applications", *Photonics Insights* 3, R09 (2024), DOI 10.3788/PI.2024.R09 [VERIFICADO].

### Inferences
- Para un refractómetro de volumen sin funcionalizar, los únicos mecanismos con antecedente son: (a) seguir el corrimiento de resonancia (lineal) y (b) interrogar con un peine externo (Knoerzer). Usar el propio peine Kerr del anillo como sonda de n (por ejemplo, vía el corrimiento de D1/FSR o de la repetición) sería original, pero no tiene un antecedente publicado que yo haya encontrado.

### Gaps
- No encontré trabajos de "soliton microcomb refractometry" de volumen en Si3N4 con cladding de agua. Un artículo de modelado de un biosensor de *Salmonella* con "pulso solitón" en un microanillo ([MDPI Sensors 14, 12885](https://mdpi.com/1424-8220/14/7/12885/htm)) da cifras simuladas que parecen poco realistas (95 500 nm/RIU). No se recomienda como referencia.

---

## 5. Revisiones, tutoriales, libros, cursos y tesis para aprender simulación no lineal integrada

### Takeaway
La ruta de lectura recomendada es: Kippenberg 2018 (Science) → Pasquazi 2018 (Phys. Rep., la más completa) → Chembo 2016 y Hansson & Wabnitz 2016 (modelos LLE, abiertos en Nanophotonics) → Coen 2013 / Chembo & Menyuk 2013 (derivación de la LLE) → pyLLE (práctica) → Gaeta 2019 / Chang 2022 / Kovach 2020 (plataformas y estado del arte). Para supercontinuo: Dudley RMP 2006 y Dudley & Taylor 2010. Tesis abiertas: P.-H. Wang (Purdue), Helgason (Chalmers, licenciatura) y J. Liu (EPFL).

### Cited Findings
**Revisiones**
- Pasquazi, A. et al., "Micro-combs: A novel generation of optical sources", *Phys. Rep.* 729, 1–81 (2018). DOI 10.1016/j.physrep.2017.08.004 [VERIFICADO]. Según la búsqueda, describe la LLE como el modelo de campo medio más usado — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0370157317303253)
- Kippenberg, T. J., Gaeta, A. L., Lipson, M., Gorodetsky, M. L., "Dissipative Kerr solitons in optical microresonators", *Science* 361, eaan8083 (2018). DOI 10.1126/science.aan8083 [VERIFICADO].
- Gaeta, A. L., Lipson, M., Kippenberg, T. J., "Photonic-chip-based frequency combs", *Nat. Photon.* 13, 158–169 (2019). DOI 10.1038/s41566-019-0358-x [VERIFICADO].
- Chang, L., Liu, S., Bowers, J. E., "Integrated optical frequency comb technologies", *Nat. Photon.* 16, 95–108 (2022). DOI 10.1038/s41566-021-00945-1 [VERIFICADO].
- Kovach, A. et al., "Emerging material systems for integrated optical Kerr frequency combs", *Adv. Opt. Photon.* 12, 135 (2020). DOI 10.1364/AOP.376924 [VERIFICADO]. Tablas de n2, pérdidas y dispersión por material.
- Chembo, Y. K., "Kerr optical frequency combs: theory, applications and perspectives", *Nanophotonics* 5, 214–230 (2016). DOI 10.1515/nanoph-2016-0013 [VERIFICADO]. Acceso abierto, con orientación de tutorial.
- Hansson, T., Wabnitz, S., "Dynamics of microresonator frequency comb generation: models and stability", *Nanophotonics* 5, 231–243 (2016). DOI 10.1515/nanoph-2016-0012 [VERIFICADO]. Compara los modelos LLE e Ikeda y su estabilidad. Acceso abierto.
- Lugiato, L. A., Prati, F., Gorodetsky, M. L., Kippenberg, T. J., "From the Lugiato–Lefever equation to microresonator-based soliton Kerr frequency combs", *Phil. Trans. R. Soc. A* 376, 20180113 (2018). DOI 10.1098/rsta.2018.0113 [VERIFICADO]. Historia y derivación de la LLE.

**Modelado (artículos base de la LLE)**
- Lugiato, L. A., Lefever, R., "Spatial dissipative structures in passive optical systems", *Phys. Rev. Lett.* 58, 2209 (1987). DOI 10.1103/PhysRevLett.58.2209 [VERIFICADO]. Artículo original.
- Coen, S., Randle, H. G., Sylvestre, T., Erkintalo, M., "Modeling of octave-spanning Kerr frequency combs using a generalized mean-field Lugiato–Lefever model", *Opt. Lett.* 38, 37 (2013). DOI 10.1364/OL.38.000037 [VERIFICADO]. LLE generalizada con dispersión de orden alto, resuelta con Newton–Raphson y split-step — [ar5iv](https://ar5iv.labs.arxiv.org/html/1211.1697)
- Coen, S., Erkintalo, M., "Universal scaling laws of Kerr frequency combs", *Opt. Lett.* 38, 1790 (2013). DOI 10.1364/OL.38.001790 [VERIFICADO]. Leyes de escala del ancho del peine y de la potencia.
- Chembo, Y. K., Menyuk, C. R., "Spatiotemporal Lugiato-Lefever formalism for Kerr-comb generation in whispering-gallery-mode resonators", *Phys. Rev. A* 87, 053852 (2013). DOI 10.1103/PhysRevA.87.053852 [VERIFICADO]. Equivalencia entre la LLE y el modelo de modos acoplados.
- Hansson, T., Modotto, D., Wabnitz, S., "On the numerical simulation of Kerr frequency combs using coupled mode equations", *Opt. Commun.* 312, 134–136 (2014). DOI 10.1016/j.optcom.2013.09.017 [VERIFICADO]. Implementación numérica eficiente.
- Herr, T. et al., "Temporal solitons in optical microresonators", *Nat. Photon.* 8, 145–152 (2014). DOI 10.1038/nphoton.2013.343 [VERIFICADO].
- Guo, H. et al., "Universal dynamics and deterministic switching of dissipative Kerr solitons in optical microresonators", *Nat. Phys.* 13, 94–102 (2017). DOI 10.1038/nphys3893 [VERIFICADO].
- Brasch, V. et al., "Photonic chip–based optical frequency comb using soliton Cherenkov radiation", *Science* 351, 357–360 (2016). DOI 10.1126/science.aad4811 [VERIFICADO]. Si3N4 con dispersión de orden alto y onda dispersiva.
- Li, Q. et al., "Stably accessing octave-spanning microresonator frequency combs in the soliton regime", *Optica* 4, 193 (2017). DOI 10.1364/OPTICA.4.000193 [VERIFICADO]. Diseño de dispersión en Si3N4 (NIST) con simulación LLE.
- Okawachi, Y. et al., "Octave-spanning frequency comb generation in a silicon nitride chip", *Opt. Lett.* 36, 3398 (2011). DOI 10.1364/OL.36.003398 [VERIFICADO]. Anterior a 2013, pero es el trabajo clásico.
- Capítulos de libro: Herr, T., Gorodetsky, M. L., Kippenberg, T. J., "Dissipative Kerr solitons in optical microresonators", en *Nonlinear Optical Cavity Dynamics* (Wiley, 2015), pp. 129–162, DOI 10.1002/9783527686476.ch6 [VERIFICADO]. Coen, S., Erkintalo, M. et al., "Temporal cavity solitons in Kerr media", mismo libro, pp. 11–40, DOI 10.1002/9783527686476.ch2 [VERIFICADO].

**Supercontinuo (GNLSE)**
- Dudley, J. M., Genty, G., Coen, S., "Supercontinuum generation in photonic crystal fiber", *Rev. Mod. Phys.* 78, 1135–1184 (2006). DOI 10.1103/RevModPhys.78.1135 [VERIFICADO]. Incluye el código GNLSE (RK4IP) en el apéndice. Anterior a 2013, pero es indispensable.
- Dudley, J. M., Taylor, J. R. (eds.), *Supercontinuum Generation in Optical Fibers*, Cambridge Univ. Press (2010). DOI 10.1017/CBO9780511750465 [VERIFICADO].

**Tesis abiertas**
- Pei-Hsun Wang, PhD, Purdue (2016): ver la sección 1 — [PDF](https://engineering.purdue.edu/~fsoptics/thesis/Wang__Pei-Hsun_PhD.pdf)
- Óskar B. Helgason, *Dissipative Kerr solitons in normal dispersion waveguides*, tesis de **licenciatura** (Chalmers, 2020). Explora numéricamente la potencia por línea de microcombs de pulsos oscuros y su arranque en microcavidades de Si3N4 acopladas linealmente. Es la más alineada con Si3N4 de dispersión normal — [registro](https://research.chalmers.se/en/publication/519027), [PDF](https://research.chalmers.se/publication/519027/file/519027_Fulltext.pdf)
- Junqiu Liu, *Silicon Nitride Integrated Nonlinear Photonics*, tesis EPFL n.º 10343 (2020, dir. T. J. Kippenberg). Fabricación de Si3N4 de baja pérdida (Q > 30 millones) y microcombs solitónicos — [Infoscience](https://infoscience.epfl.ch/record/279965)
- Raja Arslan Sajid, tesis EPFL (2023), sobre usos lineales y no lineales de microrresonadores de Si3N4 miniaturizados. Infoscience la lista, pero no revisé el contenido — [Infoscience](https://infoscience.epfl.ch/entities/publication/5e19c56f-6049-4e95-bc9f-b50a030fbdd4/files) (enlace devuelto por la búsqueda; la correspondencia exacta autor–enlace no está confirmada)
- Cong Wang, PhD, Purdue ("Device design and characterization for silicon ..."). Posiblemente trate de diseño de microrresonadores para peines; no lo revisé — [PDF](https://engineering.purdue.edu/~fsoptics/thesis/CongWang_PhD.pdf)
- Kyunghun Han, PhD, Purdue, *Efficient On-chip Optical Microresonator for Optical Comb Generation: Design and Fabrication* — [registro](https://docs.lib.purdue.edu/dissertations/AAI10268259)
- Nora Dzieia, tesis de **maestría** (Chalmers, 2025), sobre microcombs de molécula fotónica con baja tasa de repetición — [ODR Chalmers](https://odr.chalmers.se/bitstreams/b45f06cc-a820-41cc-950f-3bf784208b70/download)
- La lista completa de tesis del grupo de Weiner está en [engineering.purdue.edu/~fsoptics/thesis/](https://engineering.purdue.edu/~fsoptics/thesis/). Solo da nombres de archivo, sin títulos.

**Cursos y charlas**
- T. J. Kippenberg, "Photonic chip based frequency combs", Distinguished Lecturer Series del MPL (enero de 2021, virtual). La página indica que está grabada en YouTube, pero no obtuve la URL del video — [MPL](https://mpl.mpg.de/events/event/photonic-chip-based-frequency-combs)
- Charla pública EPFL "Light in Motion: Microresonators, Quantum Optomechanics, and On-Chip Frequency Combs" (11-may-2026). No confirmé que haya grabación — [EPFL memento](https://memento.epfl.ch/event/light-in-motion-microresonators-quantum-optomechan)
- La documentación de pyLLE (usnistgov.github.io/pyLLE) funciona en la práctica como tutorial con ejemplos ejecutables de Si3N4 — [artículo](https://arxiv.org/pdf/1903.10441)

### Inferences
- Para un estudiante, lo que más rinde es combinar pyLLE con la tesis de Helgason (dispersión normal) y con Wang 2013/2016 (puerto drop): cubren las tres particularidades del proyecto.

### Gaps
- No encontré un curso abierto estructurado (EPFL, Caltech, Chalmers o nanoHUB) sobre microcombs ni un "Tutorial:" en APL Photonics o JOSA B dedicado a la simulación LLE. Hay un "tutorial" de Kippenberg y colaboradores (2019) mencionado en la búsqueda que no pude identificar con DOI.
- Las tesis doctorales de T. Herr, V. Brasch y M. Karpov (EPFL) y de A. Fülöp (Chalmers) probablemente están en Infoscience o research.chalmers.se, pero no verifiqué sus URL.
- No hallé notas de clase de Erkintalo ni de Coen.
