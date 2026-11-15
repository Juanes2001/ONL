# Supercontinuo (SCG) en guías integradas de SiN (Si3N4 / SiN / SiN rico en Si), nov 2021 – nov 2026

> Notas de investigación (agente, 2026-11-14). Cada afirmación lleva su fuente. Estado de acceso: **OA** = acceso abierto; **arXiv** = hay preprint libre; **Paywall** = suscripción.
> Límites: se hicieron unas 20 consultas y lecturas. Varios PDF no se pudieron leer completos (el PDF de arXiv llegó binario, PubMed bloqueado, nature.com sin resolver DNS). Por eso, muchas dimensiones de guía (ancho, largo) quedan como **vacío** en vez de inventarse. Las referencias marcadas «sin verificar en esta sesión» vienen de conocimiento previo y deben comprobarse antes de citarlas.

---

## P1. Resultados de referencia en SCG con SiN, 2021–2026 (espectros, octava, IR medio, visible/UV, ANDi coherente, ondas dispersivas, baja energía para f-2f, oblea/foundry, bombeo compacto)

### Takeaway
La tendencia 2022–2026 va hacia (i) SC multi-octava con láseres de fibra compactos a 1.55 µm y baja energía (≈ 75–110 pJ), con detección de f_ceo en el chip (f-2f con LN heterogéneo, o f-3f); (ii) películas SiN de baja temperatura o deuteradas, a escala de oblea, sin recocido; y (iii) ingeniería de ondas dispersivas hacia el UV (guías de doble núcleo). Los resultados más anchos usan películas gruesas (≈ 700–800 nm) en dispersión anómala. Lo «delgado» (400 nm) solo llega a una octava con recubrimientos de alto n₂ (TeO2, GO) o con SiN rico en Si.

### Cited Findings
**Revisiones con marco general**
- Brès et al., «Supercontinuum in integrated photonics: generation, applications, challenges, and perspectives», *Nanophotonics* (2023), DOI 10.1515/nanoph-2022-0749, **OA** (De Gruyter, CC-BY). Cubre teoría y plataformas. Señala que el Si3N4, a diferencia del Si (limitado a dispersión anómala), «also shows excellent performance in terms of ANDi SCG» — [De Gruyter](https://www.degruyterbrill.com/document/doi/10.1515/nanoph-2022-0749/html?lang=en); [Wiley mirror](https://onlinelibrary.wiley.com/doi/10.1515/nanoph-2022-0749)
- La misma revisión indica que un contenido de Si ligeramente mayor mejoró el desempeño: menores pérdidas, mejor dispersión y fabricación más simple por menor esfuerzo tensil, lo que permitió SC de una octava — [resumen vía búsqueda, Brès 2023](https://www.degruyterbrill.com/document/doi/10.1515/nanoph-2022-0749/html?lang=en)

**SC multi-octava con bombeo compacto y baja energía (1.55 µm)**
- Zhang, Wang, Xu, …, Guo, Xing, «1-GHz VIS-to-MIR frequency combs enabled by CMOS-compatible nanophotonic waveguides», arXiv:2509.23704 (sep 2025, v2 ene 2026), **arXiv** (sin revista registrada). Usa guías Si3N4 de baja pérdida con dispersión diseñada. El bombeo es un láser de fibra todo-PM a **1556 nm, 73 fs, 1 GHz, 110 pJ inyectados**. El SC va de **350 a 3280 nm** (> 3 octavas, ≈ 0.76 PHz coherentes). La THG en el chip da un batido f-3f de f_ceo con **SNR 43 dB**. No se reportan espesor ni geometría en el resumen — [arXiv](https://arxiv.org/abs/2509.23704)
- Fan, Ruhnke, Op de Beeck, Tavani, Vasiliev, Kärtner, Herr, «f-2f self-referencing for silicon nitride photonics via a heterogeneously integrated lithium niobate layer», arXiv:2609.23328 (sep–oct 2026), **arXiv**. SC en Si3N4 con láser de modos amarrados a **1560 nm** y **75 pJ en el chip**. La SHG ocurre en una capa de LiNbO3 heterogénea unida por «escalator couplers» adiabáticos. f_ceo detectada con **30 dB SNR @ 300 kHz RBW** — [arXiv](https://arxiv.org/abs/2609.23328)

**Oblea / foundry / baja temperatura**
- Wang, Cao, Tobing, …, Luo, Tan, «Octave-spanning supercontinuum generation in a wafer-scale, low loss deuterated silicon nitride waveguide», *Opt. Express* **34**(11), 20843–20853 (2026), DOI 10.1364/OE.588127, **Paywall** según Europe PMC. Película de **800 nm** de SiN deuterado depositada en un paso a < 400 °C en oblea de 8″, con **0.54 dB/cm**. Bombeo de **500 fs, 1700 pJ, 1555 nm**. SC de **587–1883 nm a −30 dB**. Las simulaciones NLSE concuerdan con la medición. Coherencia **|g12| > 0.81** en todo el espectro a energías bajas; a energías altas se degrada, y los autores proponen optimizar la longitud — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42271881&resultType=core&format=json)
- Bose, Harrington, Isichenko, Liu, Wang, Newman, Blumenthal, «Anneal-free ultra-low loss silicon nitride integrated photonics», *Light Sci. Appl.* (2024), DOI 10.1038/s41377-024-01503-4, **OA** (LSA) + arXiv:2309.04070. Proceso con silano deuterado a ≤ 250 °C, sin recocido. Pérdidas: 1.77 dB/m (núcleo de 80 nm) y 8.66 dB/m (nitruro de 800 nm). SC de «más de dos octavas» — [arXiv](https://arxiv.org/abs/2309.04070). Un resumen de búsqueda da **≈ 650 nm – 2.7 µm**, bombeo a 1550 nm y **≈ 200–400 pJ en el chip** — [búsqueda (snippet arXiv 2309.04070)](https://arxiv.org/pdf/2309.04070). Nota: el resumen de arXiv dice «thick nitride micro-resonator»; conviene verificar en el PDF si el SC es en guía recta.

**ANDi coherente (dispersión normal)**
- Rebolledo-Salgado, Ye, Christensen, Lei, Twayana, Schröder, Zelan, Torres-Company, «Coherent supercontinuum generation in all-normal dispersion Si3N4 waveguides», *Opt. Express* **30**(6), 8641–8651 (2022), DOI 10.1364/OE.450987. Europe PMC lo marca «subscription» pero con licencia «cc by»: **probablemente OA en Optica**, verificar. Ensanchamiento coherente con pulsos de **picosegundos** a alta tasa de repetición. Con más energía aparece **optical wave breaking (OWB)**, que da un espectro **coherente de una octava**. Los autores dicen que la dispersión normal en SiN es difícil por exigencias de longitud y pérdidas — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:35299311%20OR%20EXT_ID:38571110&resultType=core&format=json); [ResearchGate](https://www.researchgate.net/publication/358754228_Coherent_supercontinuum_generation_in_all-normal_dispersion_Si3N4_waveguides)
- Ren, Guo, Zhai, Zhang, «On-chip octave-spanning flat supercontinuum in all-normal-dispersion silicon nitride waveguides», *Opt. Express* **32**(6), 8527–8536 (2024), DOI 10.1364/OE.509430, **Paywall**. **Propuesta numérica**: dispersión ANDi plana «en silla de montar». Con **250 fs y 30 kW** de pico logra SC ultraplano (−6 dB) de **638–1477 nm**. La longitud de onda de bombeo se puede elegir dentro de la región plana — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:35299311%20OR%20EXT_ID:38571110&resultType=core&format=json)

**Ondas dispersivas / visible-UV**
- Xia, van der Slot, Timmerkamp, Fallnich, Boller, «Blue-shifted dispersive waves and broadband UV emission using dual-core SiN waveguides», *Opt. Express* **34**, 9113–9128 (2026), DOI 10.1364/OE.587973, **arXiv:2512.14572**. Bombeo de pulsos IR ultracortos a **~1 µm**. La onda dispersiva (DW) en la guía de doble núcleo está en **540 nm**, desplazada **80 nm (70 THz)** hacia el azul frente a un núcleo simple. La emisión llega por debajo de **350 nm** (≈ 25 dB bajo la densidad de la DW). Los supermodos se excitan con tapers adiabáticos. Modelo numérico concordante — [arXiv](https://arxiv.org/abs/2512.14572)
- Lin & Li, «Enhanced supercontinuum generation and dispersive wave emission in a silicon nitride waveguide pumped at 1550 nm telecom wavelength», *JOSA B* **39**(7), 1792–1798 (2022), DOI 10.1364/JOSAB.454673, **Paywall**. **Numérico**: un disparador CW débil aumenta el ancho, la coherencia y la conversión a DW. La potencia CW necesaria baja hasta **10⁻⁵ de la potencia pico** del bombeo — [Optica](https://opg.optica.org/josab/abstract.cfm?uri=josab-39-7-1792)

**IR medio**
- La búsqueda devolvió SC IR medio en SiN cargado sobre LiNbO3-on-sapphire (ResearchGate, ≈ 2024; no se leyó) y una simulación de guía SRN con taper de 2 mm hasta **5.66 µm con 25 W de pico** (*JOSA B* 2021, IEEE 9642601) — [ResearchGate](https://www.researchgate.net/publication/380481446_Mid-IR_Supercontinuum_Generation_in_a_Silicon_Nitride_loaded_Lithium_Niobate_on_Sapphire_Waveguide); [IEEE](https://ieeexplore.ieee.org/document/9642601/)

**Línea base pre-2021 (contexto; el usuario ya la tiene)**
- SC de 1.6 octavas, **665–2025 nm, 160 pJ, guía de 4.3 cm** (Johnson et al. 2015) — [ResearchGate](https://www.researchgate.net/publication/283323553_Octave-spanning_coherent_supercontinuum_generation_in_a_silicon_nitride_waveguide)
- SC de 650 nm – 2.6 µm en SiN con revestimiento de aire, ≈ 150 mW acoplados (Carlson et al. 2017/2018, NIST) — [arXiv 1702.03269](https://arxiv.org/abs/1702.03269); [arXiv 1710.02872](https://arxiv.org/abs/1710.02872)
- Plataforma industrial de 300 mm con SiN rico en N: SC de **700–2400 nm** bombeando en régimen anómalo a 1200, 1300 y 1550 nm (≈ 2020) — [ResearchGate](https://www.researchgate.net/publication/338414533_Broadband_supercontinuum_generation_in_nitrogen-rich_silicon_nitride_waveguides_using_a_300_mm_industrial_platform)

### Inferences
- Los anchos «récord» recientes (350–3280 nm) vienen del bombeo con fibras de ~70–100 fs y ~100 pJ en guías gruesas de dispersión anómala. La energía para una octava bajó de ~160 pJ (2015) a ~75–110 pJ (2025–26), junto con la integración de f-2f/f-3f en el chip.
- La línea «ANDi coherente» en SiN tiene pocos trabajos experimentales en la ventana (Rebolledo-Salgado 2022 es el principal). El resto son propuestas numéricas (Ren 2024).

### Gaps
- No se obtuvieron ancho, longitud, β2/ZDW ni γ de Rebolledo-Salgado 2022, Zhang 2025 ni Fan 2026: los resúmenes no los dan y los PDF no fueron legibles. Hay que leer los textos completos.
- No se encontró en esta sesión un SC en SiN bombeado por un láser integrado en el chip (sin fibra), ni por un peine electroóptico o un microcomb como bombeo directo.
- Faltan trabajos 2022–26 de grupos señalados (Kippenberg/EPFL, Gaeta/Lipson, Kuyken/Ghent, Twente/LioniX salvo Boller, NIST) que no aparecieron en las búsquedas. Hay que revisar Google Scholar.

---

## P2. SC en SiN delgado (< 500 nm) o en dispersión normal: ancho y energías necesarias; qué limita el espectro (fisión de solitones vs. SPM + OWB, longitud, pérdidas)

### Takeaway
Con **400 nm de Si3N4 estequiométrico** la guía suele estar en dispersión normal a 1550 nm (TE). Los trabajos de la ventana que logran una octava en 400 nm lo hacen **añadiendo un recubrimiento de alto n₂ (TeO2)**, que eleva γ unas 2.5 veces y ajusta la dispersión: octava con **258–482 W de pico (≈ 29 pJ, 100 fs, 1565 nm)**. En ANDi pura, el ensanchamiento por SPM + OWB es coherente pero estrecho por unidad de energía. Necesita guías largas y de baja pérdida, o potencias de decenas de kW en propuestas numéricas.

### Cited Findings
- Mbonde, Singh, Segat Frare, Sinobad, Torab Ahmadi, Hashemi, Bonneville, Mascher, Kärtner, Bradley, «Octave-spanning supercontinuum generation in a CMOS-compatible thin Si3N4 waveguide coated with highly nonlinear TeO2», arXiv:2309.08318 (sep 2023), **arXiv** (no se encontró revista). Película de **400 nm** de Si3N4 («moderate-confinement»), recubierta con TeO2. γ aumenta **×2.5**. Octava con **258 W de pico** y láser de **100 fs a 1565 nm**. Simulación concordante — [arXiv](https://arxiv.org/abs/2309.08318). Otra búsqueda atribuye a este preprint una oblea sin grietas y **29.3 pJ** — [snippet búsqueda arXiv 2309.08318](https://arxiv.org/pdf/2309.08318)
- Versión de conferencia: «Octave-Spanning Supercontinuum Generation in a Thin Si3N4 Waveguide Coated with Highly Nonlinear TeO2», *Frontiers in Optics* 2022, FW7E.3. Guía de **400 nm**, octava con **482 W de pico**, **100 fs @ 1565 nm** — [Optica](https://opg.optica.org/abstract.cfm?uri=FiO-2022-FW7E.3) (**Paywall**/resumen libre)
- SiN «ultra-rico en Si» (USRN), *Sci. Rep.* (2022), DOI 10.1038/s41598-022-13734-9, **OA**. Guía de **3 mm**, bombeo de **500 fs @ 1555 nm**, **17 pJ**. Los autores destacan la baja energía y la buena coherencia para auto-referenciado — [Nature/Sci. Rep.](https://www.nature.com/articles/s41598-022-13734-9) (no se pudo abrir; datos tomados del resumen de búsqueda)
- Recubrimiento de óxido de grafeno 2D sobre SiN: hasta **×2.4 de ancho espectral** frente a la guía sin GO, con potencias pico > 1000 W. D. J. Moss et al., *Adv. Mater. Technol.* **8**, 2201796 (2023), DOI 10.1002/admt.202201796; arXiv:2603.07440. **arXiv** — [arXiv](https://arxiv.org/abs/2603.07440)
- ANDi en Si3N4: con ps a alta tasa el ensanchamiento es coherente. **Con más energía, el OWB da una octava coherente**. La implementación es difícil por la **longitud de propagación y las pérdidas** exigidas — [Rebolledo-Salgado 2022 vía Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:35299311%20OR%20EXT_ID:38571110&resultType=core&format=json)
- ANDi plana optimizada (numérico): 638–1477 nm a −6 dB, pero con **30 kW de pico y 250 fs** (≈ 7.5 nJ, estimación propia) — [Ren 2024 vía Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:35299311%20OR%20EXT_ID:38571110&resultType=core&format=json)
- SiN rico en Si en ANDi: peine de **1100–2200 nm** en guía SRN de dispersión totalmente normal (resultado citado en la búsqueda; fecha y autores no verificados) — [búsqueda: ResearchGate ANDi Si3N4](https://www.researchgate.net/publication/358754228_Coherent_supercontinuum_generation_in_all-normal_dispersion_Si3N4_waveguides)
- Línea base: en SRN (2016), el continuo del modo TM, con dispersión normal en el bombeo, se generó por OWB — [arXiv 1606.00568](https://arxiv.org/abs/1606.00568)
- Coherencia vs. energía en anómala (película de 800 nm): |g12| > 0.81 a baja energía, degradación a alta energía, mitigable con la longitud — [Wang 2026, Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42271881&resultType=core&format=json)

### Inferences
- Para la guía del proyecto (400 nm de Si3N4, SiO2 abajo, SiO2 o agua arriba, 1550 nm), lo esperable **sin recubrimiento no lineal** es SPM + OWB en ANDi: espectro coherente y plano, pero de ancho sub-octava a energías de pJ–decenas de pJ. La octava en 400 nm se ha mostrado solo con TeO2 (γ ×2.5 y ajuste de dispersión). Esto es inferencia y debe verificarse simulando con la β(ω) real del proyecto.
- En ANDi el límite práctico es el producto L_eff·γ·P₀ frente a las pérdidas (L_eff = (1 − e^{−αL})/α) y la distancia de OWB. En anómala, el límite lo ponen el orden del solitón N y la decoherencia por inestabilidad de modulación (MI) cuando N es grande (≳ 10, criterio de Dudley 2006, línea base).
- Un cladding de agua (n ≈ 1.33) aumenta el contraste índice frente al SiO2 superior. Eso tiende a desplazar la dispersión hacia lo anómalo y a reducir el área efectiva, pero suma absorción del agua > 1.4 µm. Inferencia sin fuente en la ventana.

### Gaps
- Faltan la β2 o los ZDW de la guía TeO2/SiN de 400 nm, el espesor de TeO2, el ancho y el largo (PDF no legible).
- Falta la composición (índice) y el espesor de la película USRN de Sci. Rep. 2022.
- No se encontró ningún trabajo experimental 2022–26 de SC en SiN estequiométrico **≤ 400 nm sin recubrimiento** en dispersión normal a 1550 nm con fs y pJ. Puede que no exista o que no haya aparecido en la búsqueda.

---

## P3. SC con revestimientos líquidos/agua o polímero, guías ranura (slot) o suspendidas

### Takeaway
En la ventana 2021–2026 **no se encontraron** trabajos de SC en SiN con cladding de agua o líquido, ni en SiN suspendido. Lo más cercano son recubrimientos funcionales sólidos (TeO2, GO, monocapas TMD) y el aire como cladding superior (línea base NIST).

### Cited Findings
- TeO2 sobre SiN de 400 nm (γ ×2.5) — [arXiv 2309.08318](https://arxiv.org/abs/2309.08318)
- GO 2D en ventanas abiertas del cladding superior de sílice (ancho ×2.4) — [arXiv 2603.07440](https://arxiv.org/abs/2603.07440)
- Monocapas de dicalcogenuros de metales de transición (TMD) sobre SiN para reforzar la no linealidad (2021, en el límite de la ventana) — [arXiv 2105.01467](https://arxiv.org/abs/2105.01467)
- Slot de SiN para dispersión ANDi aplanada (línea base, ≈ 2011) — [ResearchGate fig.](https://www.researchgate.net/figure/Silicon-nitride-slot-waveguide-for-dispersion-flattening-and-supercontinuum-generation-A_fig2_51887880)
- SiN con revestimiento de aire (línea base NIST 2017) — [arXiv 1702.03269](https://arxiv.org/abs/1702.03269)
- La búsqueda dirigida «suspended / liquid cladding SiN supercontinuum 2022–2026» no devolvió resultados pertinentes — [búsqueda del 2026-11-14, sin enlace primario]

### Inferences
- Un SC con cladding de agua sobre SiN de 400 nm parece un nicho poco explorado. Se puede plantear como aporte modesto del proyecto (cambio de dispersión al pasar de SiO2 a agua), con la salvedad de la absorción del agua alrededor de 1.45 µm y por encima de 1.9 µm.

### Gaps
- Faltan trabajos de SC en guías optofluídicas o con cladding líquido en SiN. Sugerencia: buscar «optofluidic supercontinuum», «liquid-clad silicon nitride nonlinear».

---

## P4. Práctica de modelado numérico (forma de GNLSE, Raman, auto-empinamiento, dispersión de alto orden, solvers modales; valores de β_n, γ, f_R, pérdidas) y códigos abiertos

### Takeaway
Los trabajos usan la GNLSE escalar estándar con dispersión completa β(ω), interpolada de un solver modal (FDE/FEM), con término de choque y, a menudo, Raman. En Si3N4 amorfo la fracción Raman reportada es **f_R ≈ 0.2**, para un modo Si-N centrado en ~410 cm⁻¹ con ancho de ~70 cm⁻¹. Su efecto en el SC suele ser **menor**. No se verificó en esta sesión qué paquete abierto usa cada trabajo.

### Cited Findings
- Modelo extendido (NAEE) con Raman: modo Si-N asimétrico a **410 cm⁻¹**, ancho **70 cm⁻¹**, **f_R = 0.2** («typical of amorphous materials»). «Generally, the Raman effect gave minor contributions» (SRN, línea base 2016) — [arXiv 1606.00568](https://arxiv.org/abs/1606.00568)
- SiN rico en N en plataforma de 300 mm: GNLSE con una contribución de ganancia Raman nueva, pero el término Raman de primer orden se trata como despreciable frente a la escala de auto-empinamiento — [ResearchGate](https://www.researchgate.net/publication/338414533_Broadband_supercontinuum_generation_in_nitrogen-rich_silicon_nitride_waveguides_using_a_300_mm_industrial_platform)
- Forma general de la respuesta: R(T) = (1 − f_R)δ(T) + f_R h_R(T). El auto-empinamiento entra por la dependencia en frecuencia del operador no lineal — [arXiv 1902.02385](https://arxiv.org/abs/1902.02385); [APL Photonics 8, 036114 (2023), «Simulating supercontinua from mixed and cascaded nonlinearities»](https://pubs.aip.org/aip/app/article/8/3/036114/2879065/Simulating-supercontinua-from-mixed-and-cascaded) (**OA**)
- Las simulaciones NLSE/GNLSE concuerdan con los experimentos en: Wang 2026 (SiN deuterado) — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42271881&resultType=core&format=json); Mbonde 2023 (TeO2) — [arXiv](https://arxiv.org/abs/2309.08318); Xia 2026 (doble núcleo) — [arXiv](https://arxiv.org/abs/2512.14572)
- Tesis doctoral DTU (S. Christensen, coautor de Rebolledo-Salgado 2022) sobre SC en guías nanofotónicas de SiN: fuente probable de detalles de modelado ANDi — [DTU Orbit PDF](https://backend.orbit.dtu.dk/ws/files/247994731/Thesis_Simon_Christensen.pdf) (**OA**, no leída en esta sesión)
- La coherencia se cuantifica con |g12| a partir de conjuntos de simulaciones con ruido de un fotón por modo — [Wang 2026](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42271881&resultType=core&format=json)
- Disparador CW en la GNLSE como herramienta de control (numérico) — [Lin & Li 2022](https://opg.optica.org/josab/abstract.cfm?uri=josab-39-7-1792)

### Inferences
- Protocolo de cálculo recomendado, consistente con las fuentes:
  1. β(ω) y A_eff(ω) desde FDE (Lumerical MODE), con índices de Sellmeier de Si3N4, SiO2 y agua.
  2. γ(ω) = n₂ω/(c·A_eff), con n₂(Si3N4) ≈ 2.4×10⁻¹⁹ m²/W, valor típico que debe verificarse con las notas de propiedades del repo.
  3. GNLSE en el dominio de la frecuencia (RK4IP) con dispersión completa (no truncada en β_n), choque τ_sh = 1/ω₀ más la corrección por dispersión de A_eff, Raman con f_R ≈ 0.2 (prueba de sensibilidad con f_R = 0) y pérdida α.
  4. Coherencia |g12| con ≥ 20 realizaciones de ruido.

### Gaps
- **Códigos abiertos**: la búsqueda no devolvió documentación de gnlse-python, PyNLO ni Laserfun aplicada a SiN. Por conocimiento previo (sin verificar en esta sesión): *gnlse-python* (Wrocław, implementa Dudley/Taylor con Raman y choque), *PyNLO* (NIST/Boulder) y *laserfun* (D. Hickstein, usado en trabajos de SC en SiN de NIST). Hay que verificar los repositorios en GitHub y su uso citado.
- Faltan valores publicados de β2, β3, γ de la ventana para guías SiN de 400 nm. No se extrajeron porque los PDF no fueron legibles.

---

## P5. Revisiones y tutoriales 2021–2026 sobre SC en guías integradas (SiN)

### Takeaway
La revisión central es **Brès et al., *Nanophotonics* 2023 (OA)**. La complementan Geng et al. 2024 (OA, panorama no lineal integrado) y Buzaverov et al. 2024 (*LPR*, plataforma SiN de visible a IR medio).

### Cited Findings
- Brès et al., *Nanophotonics* (2023), DOI 10.1515/nanoph-2022-0749, **OA** — [De Gruyter](https://www.degruyterbrill.com/document/doi/10.1515/nanoph-2022-0749/html?lang=en)
- Geng et al., «Nonlinear photonics on integrated platforms», *Nanophotonics* (2024), DOI 10.1515/nanoph-2024-0149, **OA**. Se centra en SC y peines; Si3N4 y calcogenuros como plataformas versátiles — [DOI](https://dx.doi.org/10.1515/nanoph-2024-0149)
- Buzaverov et al., «Silicon Nitride Integrated Photonics from Visible to Mid-Infrared Spectra», *Laser Photon. Rev.* (2024), DOI 10.1002/lpor.202400508, **Paywall** (hay versión en ResearchGate) — [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1002/lpor.202400508); [ADS](https://ui.adsabs.harvard.edu/abs/2024LPRv...1800508B/abstract)
- «Supercontinuum generation in silicon photonics platforms» (2022, revista china; PDF en researching.cn), **OA** — [PDF](https://www.researching.cn/ArticlePdf/m00072/2022/10/3/03000A43.pdf) (autores no verificados)

### Inferences
- Para el tutorial de modelado, Brès 2023 basta como puente entre Dudley 2006 (línea base) y la práctica integrada.

### Gaps
- Faltan volumen y páginas de Brès 2023 y Geng 2024 (la página De Gruyter devolvió HTTP 405).

---

## Lista corta de lectura obligatoria (proyecto: SiN de 400 nm, 1550 nm, ANDi, cladding SiO2/agua)

1. **Brès et al., *Nanophotonics* 2023**, DOI 10.1515/nanoph-2022-0749 — revisión (OA).
2. **Rebolledo-Salgado et al., *Opt. Express* 30, 8641 (2022)**, DOI 10.1364/OE.450987 — ANDi coherente en Si3N4, OWB, límites de longitud y pérdida (probablemente OA, CC-BY).
3. **Mbonde et al., arXiv:2309.08318 (2023)** — octava en Si3N4 de **400 nm** recubierto con TeO2, 258 W, 100 fs @ 1565 nm (arXiv). Es el análogo más directo a la guía del proyecto.
4. **Ren et al., *Opt. Express* 32, 8527 (2024)**, DOI 10.1364/OE.509430 — diseño numérico ANDi plano, metodología de dispersión (Paywall).
5. **Wang et al., *Opt. Express* 34, 20843 (2026)**, DOI 10.1364/OE.588127 — SC a escala de oblea con coherencia |g12| medida y simulada, NLSE validada (Paywall).
6. **Zhang et al., arXiv:2509.23704 (2025)** — estado del arte en ancho (350–3280 nm, 110 pJ, 1 GHz) (arXiv).
7. *(Tutorial de modelado, línea base)* Dudley, Genty & Coen, *Rev. Mod. Phys.* 78, 1135 (2006) — el usuario ya la tiene; complementar con la tesis DTU de Christensen (OA).
