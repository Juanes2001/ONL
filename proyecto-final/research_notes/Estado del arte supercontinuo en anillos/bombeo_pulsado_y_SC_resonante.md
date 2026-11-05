# Bombeo pulsado (sincrónico) de microresonadores Kerr y "supercontinuo resonante"

Notas de investigación (2026-10-29). Alcance: solitones de cavidad Kerr excitados con un tren de pulsos (o un peine electro‑óptico, EO) en vez de onda continua (CW), en cavidades de fibra, micro‑resonadores Fabry–Pérot y anillos/racetracks integrados (Si₃N₄, sílice, LiNbO₃). Periodo 2010–2026, énfasis 2017–2026.

**Convención de verificación de DOI.** Todos los DOI marcados ✔ fueron resueltos el 2026-10-29 vía `https://doi.org/<doi>` (redirección HTTP 302 al editor) **y** cotejados por título/revista/volumen con la API de Crossref. Lo que no pude verificar lleva la etiqueta "DOI sin verificar" o se declara como vacío (gap). Idea general de notación: FSR = rango espectral libre; κ = ancho de línea cargado (2π·Hz); D₂ = dispersión de segundo orden en el dominio de modos (D_int(μ) = D₂μ²/2 + D₃μ³/6 + …); β₂ en ps²/km o fs²/mm; f_rep = tasa de repetición del bombeo; Δ ≡ f_rep − FSR ("desincronización").

---

## P1. ¿Quién introdujo los solitones Kerr con bombeo pulsado y con qué parámetros? (Obrzud, Lecomte, Herr, Nat. Photon. 11, 600 (2017))

### Takeaway
Obrzud, Lecomte y Herr (CSEM/EPFL, 2017) demostraron por primera vez solitones disipativos de cavidad en un micro‑resonador (Fabry–Pérot de fibra, FSR ≈ 9.77 GHz) bombeado con pulsos de ~2 ps a f_rep = FSR; el solitón (137 fs) se forma "encima" del pulso de bombeo resonantemente amplificado, se engancha al pulso y aparece de forma determinista con potencias medias acopladas de solo 3–100 mW, muy por debajo del umbral paramétrico CW.

### Cited Findings
- Artículo: E. Obrzud, S. Lecomte, T. Herr, "Temporal solitons in microresonators driven by optical pulses", *Nature Photonics* 11, 600–607 (2017). DOI ✔ 10.1038/nphoton.2017.140 — [Nature](https://www.nature.com/articles/nphoton.2017.140); preprint [arXiv:1612.08993](https://ar5iv.labs.arxiv.org/html/1612.08993). Versión de congreso: CLEO/Europe‑EQEC 2017, DOI ✔ 10.1109/CLEOE-EQEC.2017.8087533; ampliación SPIE 10518 (2018) "Temporal cavity solitons in synchronously driven Fabry‑Perot microresonators", DOI ✔ 10.1117/12.2289778 — [SPIE](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/10518/2289778/Temporal-cavity-solitons-in-synchronously-driven-Fabry-Perot-microresonators/10.1117/12.2289778.full).
- Resonador: Fabry–Pérot de fibra monomodo de longitud milimétrica con espejos de Bragg dieléctricos depositados en las caras de la fibra (dentro de una férula FC/PC). FSR = 9.77 GHz; ancho de línea 5.9 MHz (2.5 MHz en el experimento de baja potencia) → finesa ≈ 1650 y Q cargado ≈ 3×10⁷ a 1559 nm (derivados, no declarados en el texto); eficiencia de acoplo lineal 60 %; β₂ = −20 ps²/km (anómala), n₂ = 0.9×10⁻²⁰ m²/W, A_eff = 85 µm², dFSR/dν = 256 Hz/GHz — [arXiv:1612.08993](https://ar5iv.labs.arxiv.org/html/1612.08993).
- Bombeo: láser CW a 1559 nm + modulación de fase a 9.77 GHz + compresión en una red de Bragg chirpeada (GDD 10 ps/nm) + modulador de intensidad → pulsos de 2.4 ps (2.1 ps tras 10 m de fibra) con f_rep = 9.77 GHz = FSR; espectro casi plano de 30–50 líneas; 1.5 W a la salida del EDFA — [arXiv:1612.08993](https://ar5iv.labs.arxiv.org/html/1612.08993).
- Potencia acoplada: ≈100 mW (solitón único de 137 fs), 45 mW (dos solitones de 222 fs separados 943 fs), 3 mW (solitón único de 394 fs; energía de pulso ≈ 300 fJ → pico ≈ 140 W, derivado). Peine con >1000 líneas dentro de 25 dB y envolvente sech² — [arXiv:1612.08993](https://ar5iv.labs.arxiv.org/html/1612.08993).
- Desincronización: los "escalones" de solitón aparecen en un rango de ~100 kHz de f_rep; el solitón sigue adiabáticamente ~60 kHz; su frecuencia central se desplaza en Δ·(dFSR/dν)⁻¹, confirmado en cuatro valores de Δ; analogía explícita con los OPO χ⁽²⁾ bombeados sincrónicamente — [arXiv:1612.08993](https://ar5iv.labs.arxiv.org/html/1612.08993).
- Térmica: el corrimiento de resonancia al entrar al estado de solitón es de 10–100 MHz, que cambia el FSR solo unos kHz (dentro del rango tolerado); el "thermal locking" autoestabiliza la resonancia al láser; no se usó estabilización activa — [arXiv:1612.08993](https://ar5iv.labs.arxiv.org/html/1612.08993).
- Ventajas declaradas frente a CW: potencia media por debajo del umbral paramétrico y de la biestabilidad térmica CW; generación determinista de solitón único (sin escalones aleatorios); control totalmente óptico de f_rep y de f_ceo; sintonía manual lenta sin realimentación rápida — [Nature](https://www.nature.com/articles/nphoton.2017.140); [arXiv](https://ar5iv.labs.arxiv.org/html/1612.08993).
- Modelo: ecuaciones de modos acoplados no lineales en el dominio de la frecuencia (equivalente a la LLE), con el bombeo pulsado representado como modos en fase espaciados un FSR (31 líneas en la simulación); f_off/κ = 7.5 en el estado de solitón; reproducen el escalón y el enganche solitón–pulso — [arXiv:1612.08993](https://ar5iv.labs.arxiv.org/html/1612.08993).
- Aplicación directa (mismo grupo): "A microphotonic astrocomb", Obrzud et al., *Nat. Photon.* 13, 31–35 (2019), DOI ✔ 10.1038/s41566-018-0309-y — [Nature](https://www.nature.com/articles/s41566-018-0309-y); y filtrado no lineal del jitter de un tren de pulsos por solitones DKS: Brasch, Obrzud, Lecomte, Herr, *Optica* 6, 1386 (2019), DOI ✔ 10.1364/OPTICA.6.001386; el ancho de filtro es >10× más estrecho que el ancho de línea intrínseco de la cavidad — [arXiv:1907.09715](https://arxiv.org/abs/1907.09715v1).

### Inferences
- La "receta" de 2017 (CW → modulador de fase a f_rep → compresión dispersiva → EDFA) es la misma arquitectura de "peine EO como bombeo" que usan todos los trabajos integrados posteriores (Anderson 2021/2022, Xu 2020/2021); por eso los esquemas de bombeo pulsado se asocian siempre con f_rep en banda X/K (10–30 GHz), limitada por la electrónica de microondas.
- El rango de enganche (~10–100 kHz en f_rep) frente a FSR ≈ 10 GHz implica una tolerancia relativa ~10⁻⁵–10⁻⁶; eso fija el requisito de estabilidad térmica (ver P7).

### Gaps
- El artículo no da Q ni finesa explícitos (los valores anteriores son derivados de FSR/ancho de línea) ni potencia pico medida.
- No encontré el ancho de banda del peine en nm/THz para el estado de 137 fs (solo ">1000 líneas en 25 dB").

---

## P2. ¿Qué es el "supercontinuo resonante" (Anderson et al., Optica 8, 771 (2021))? Ancho de banda, potencia, geometría, FSR

### Takeaway
"Resonant supercontinuum" (Anderson, Bouchand, Liu, Weng, Obrzud, Herr, Kippenberg) es la fusión del supercontinuo en guía con el solitón de microresonador: un anillo de Si₃N₄ de 27.88 GHz de FSR y Q ≈ 1.8×10⁶ bombeado por pulsos EO de ~1 ps y 0.6–6 W de pico (18–180 mW medios efectivos) genera un peine de solitón de 64 THz (~600 nm, ≈2/3 de octava) con ~2200 líneas a 28 GHz, con 10× pulsos más largos y ~100× menos potencia pico que el SCG en guía de Si₃N₄, y filtra el ruido de frecuencia del bombeo hasta 100× por debajo de κ.

### Cited Findings
- Artículo: M. H. Anderson, R. Bouchand, J. Liu, W. Weng, E. Obrzud, T. Herr, T. J. Kippenberg, "Photonic chip-based resonant supercontinuum via pulse-driven Kerr microresonator solitons", *Optica* 8(6), 771–779 (2021). DOI ✔ 10.1364/OPTICA.403302 — [Optica](https://opg.optica.org/abstract.cfm?URI=optica-8-6-771); preprint [arXiv:1909.00022](https://ar5iv.labs.arxiv.org/html/1909.00022); PDF abierto en [DESY pubdb](https://bib-pubdb1.desy.de/record/459595/files/optica-8-6-771.pdf).
- Resonador: Si₃N₄ (proceso Damascene), sección 2350 × 770 nm², FSR = 27.88 GHz, κ = 2π·110 MHz, Q cargado = (1.8 ± 0.3)×10⁶; sección de acoplo recta (el texto no especifica "ring" vs "racetrack"); β₂ ≈ −11 fs²/mm (D₂ = 2π·7.2 kHz), β₃ ≈ −120 fs³/mm (D₃ ≈ 2π·15 Hz) inferida de la onda dispersiva en ~154 THz — [arXiv:1909.00022](https://ar5iv.labs.arxiv.org/html/1909.00022).
- Bombeo: peine EO de ~50 líneas (CW + modulador de intensidad + 3 moduladores de fase en cascada), f_rep = 13.94 GHz = FSR/2 (sub‑armónico por límite RF; bombea cada dos vueltas y reduce 2× la eficiencia); duración mínima ≈1 ps, estirada a ≈1.4 ps con chirp positivo pequeño (300 m SMF‑28 + 5 m DCF); energía efectiva por pulso 0.6–6 pJ, pico 0.6–6 W, potencia media efectiva 18–180 mW para estados de solitón único; pérdida de inserción 2.4 dB — [arXiv:1909.00022](https://ar5iv.labs.arxiv.org/html/1909.00022).
- Salida: estado de baja energía → 9.5 THz de ancho a 3 dB (≈55 fs), eficiencia de conversión 8 %; estado de alta energía → 64 THz (~600 nm, ≈2/3 de octava), ~2300 líneas medibles (1400 en 10 dB), eficiencia 2.8 %, onda dispersiva cerca de 1957 nm; duración simulada ≈24 fs; rango de enganche 30–50 kHz; el resumen cita "2200 líneas a 28 GHz" — [arXiv:1909.00022](https://ar5iv.labs.arxiv.org/html/1909.00022); [Optica](https://opg.optica.org/abstract.cfm?URI=optica-8-6-771).
- Comparaciones: SCG convencional en PCF usa ~100 fs y ~1 kW pico; frente al SCG en guía de Si₃N₄ este trabajo usa pulsos ~10× más largos y ~2 órdenes de magnitud menos potencia pico; el mismo pulso de 1 ps en la guía de 5 mm sin resonador solo da SPM leve; los peines de octava CW previos tenían ~1 THz de espaciado, por lo que los autores reclaman récord de "ancho × número de líneas" a espaciado de microondas — [arXiv:1909.00022](https://ar5iv.labs.arxiv.org/html/1909.00022).
- Coherencia/ruido: el solitón queda en un estado "débilmente ligado" al pulso (punto de atrapamiento a ~0.6 ps del centro); la transferencia de ruido de frecuencia del bombeo se suprime para offsets 100× menores que κ (esquina ≈2 MHz, bajando a ≈500 kHz en el borde del rango de enganche, frente a 110 MHz de κ); el bombeo asíncrono (Δ ≈ 50 kHz) da el ancho de línea más estrecho a 1908 nm (≈900 kHz con RF de bajo ruido vs 7.5 MHz con RF ruidosa) — [arXiv:1909.00022](https://ar5iv.labs.arxiv.org/html/1909.00022).
- Parámetros LLE de la simulación: κ = 2π·100 MHz, κ_ex = 2π·50 MHz, D₂ = 2π·28 kHz, g = 2π·0.054 Hz, P₀ = 900 mW (24× umbral paramétrico), δω = 6κ, 24 líneas, chirp +0.3 ps² — [arXiv:1909.00022](https://ar5iv.labs.arxiv.org/html/1909.00022).

### Inferences
- "Supercontinuo resonante" = ensanchamiento de solitón con onda dispersiva dentro de la cavidad: la cavidad aporta ganancia de potencia pico (finesa) y la estructura de solitón aporta la coherencia; por eso la salida es un peine de líneas resueltas a 28 GHz y no un continuo.
- La eficiencia de 2.8–8 % ya supera el ~1 % típico del solitón CW, pero el bombeo sub‑armónico (FSR/2) la limitó a la mitad; con f_rep = FSR se esperaría ~2× más.

### Gaps
- El texto no da un valor de potencia promedio equivalente para un peine CW de comparación directa en el mismo chip.
- No se reporta la potencia de salida del peine (mW) ni la potencia por línea en el extremo de 1957 nm.

---

## P3. Dispersión cero y normal con bombeo pulsado: solitones de dispersión cero, ondas de conmutación y pulsos oscuros

### Takeaway
Con bombeo pulsado el régimen de dispersión normal deja de necesitar cruces de modos para generar peines (ondas de conmutación / pulsos oscuros que se forman por rompimiento de onda sobre el pulso), y en el punto de dispersión cero aparecen los "zero‑dispersion solitons" (ZDS: dos ondas de conmutación moduladas que se enganchan, con n picos cuantizados) que en Si₃N₄ de 28 GHz dieron un peine de 136 THz (97 % de octava, Anderson et al. Nat. Commun. 2022); los experimentos de fibra de Auckland (Garbin 2017, Xu 2021, Macnaughtan 2023) establecen la fenomenología de las ondas de conmutación bajo bombeo pulsado.

### Cited Findings
- **Dispersión cero (Si₃N₄):** M. H. Anderson, W. Weng, G. Lihachev, A. Tikan, J. Liu, T. J. Kippenberg, "Zero dispersion Kerr solitons in optical microresonators", *Nat. Commun.* 13, 4764 (2022). DOI ✔ 10.1038/s41467-022-31916-x — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9376110/); [arXiv:2007.14507](https://arxiv.org/abs/2007.14507v1).
  - Resonadores Si₃N₄ 2350 × 770 nm²; MR1: FSR = 27.88 GHz, κ/2π = 208 MHz, κ_ex/2π = 155 MHz, D₂/2π = −3.17 kHz, D₃/2π = 13.8 Hz, D₄/2π = −15.9 mHz (d₃ = 0.38, Q cargado ≈ 0.9×10⁶ estimado); MR2: κ/2π = 150 MHz, D₂/2π = −848 Hz, D₃/2π = 12.8 Hz (d₃ = 2.11), punto de dispersión cero más cerca del bombeo de 1560 nm — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9376110/).
  - Bombeo: peine EO de 50 líneas, pulso mínimo 1 ps (FROG), f_rep = 13.944 GHz (FSR/2), óptimo 27.88888 GHz, rango de enganche ≈ ±10 kHz, 350 mW medios acoplados (MR1), 12 pJ por pulso a 28 GHz, pérdida de inserción 1.6 dB; simulación con T_p = 0.85 ps y P₀ = 1.8 W — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9376110/).
  - Resultado: peine total de 136 THz (97 % de octava); cuerpo central del ZDS(4) en MR1 >76 THz (≈1260–1830 nm), >2700 dientes a 28 GHz; pulso simulado ≈80 fs con cuatro picos; estados ZDS(n) con n = 5→4 (MR1) y 3→2 (MR2), n fijado por el número de periodos espectrales entre bombeo y onda dispersiva; siempre se formó un solo ZDS — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9376110/).
  - Mecanismo: dos frentes de onda de conmutación se forman por rompimiento de onda bajo el bombeo pulsado sincrónico y, al sintonizar, se enganchan en una estructura (en dispersión puramente normal se aniquilarían); DW1 ≈176–182 THz (TOD), DW2 ≈280 THz (D₄ normal), DWq cuasi‑ajustada por una sección de "mode stripping" que modula la dispersión; los autores argumentan que los ZDS dan peines más planos, sin fase caótica ni multisolitones — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9376110/).
- **Dispersión modulada (anómala y normal):** M. H. Anderson, A. Tikan, A. Tusnin, J. Riemensberger, R. N. Wang, T. J. Kippenberg, "Dissipative Solitons and Switching Waves in Dispersion-Modulated Kerr Cavities", *Phys. Rev. X* 13, 011040 (2023). DOI ✔ 10.1103/PhysRevX.13.011040 (nota: es 011040, no 021018) — [APS](https://link.aps.org/doi/10.1103/PhysRevX.13.011040); preprint [arXiv:2205.09957](https://arxiv.org/abs/2205.09957). Resonadores cuya dispersión integrada excede el FSR, accedidos con "la alta potencia pico del bombeo pulsado sincrónico"; en anómala: ondas dispersivas de orden superior tipo Kelly donde la dispersión plegada cruza la rejilla del peine; en normal: frentes de onda de conmutación coexistiendo con patrones de duplicación de periodo (inestabilidad de Faraday) que forman peines satélite a la misma f_rep — [arXiv:2205.09957](https://arxiv.org/abs/2205.09957).
- **Fibra, ondas de conmutación (Auckland):** B. Garbin et al., "Experimental and numerical investigations of switching wave dynamics in a normally dispersive fibre ring resonator", *Eur. Phys. J. D* 71, 240 (2017). DOI ✔ 10.1140/epjd/e2017-80133-7 — anillo de fibra bombeado sincrónicamente; se miden velocidades de las ondas de conmutación y se observa el enganche que forma pulsos oscuros persistentes — [Strathprints](https://strathprints.strath.ac.uk/62452).
- **Mini‑resonador de fibra en dispersión normal:** Y. Xu, A. Sharples, J. Fatome, S. Coen, M. Erkintalo, S. G. Murdoch, "Frequency comb generation in a pulse-pumped normal dispersion Kerr mini-resonator", *Opt. Lett.* 46(3), 512 (2021). DOI ✔ 10.1364/OL.413585 — [arXiv:2010.15228](https://arxiv.org/abs/2010.15228). Mini‑resonador de fibra de 6 cm de radio, FSR = 0.54 GHz; el bombeo pulsado elimina la necesidad de un cruce de modos; peine plano de 3 THz; la desincronización sintoniza el centro >2 THz; espaciado seleccionable 0.54–10.8 GHz bombeando en armónicos del FSR; además un solitón anómalo asistido por Raman a gran desincronización.
- **Estructura temporal de ondas de conmutación:** M. Macnaughtan, M. Erkintalo, S. Coen, S. Murdoch, Y. Xu, "Temporal characteristics of stationary switching waves in a normal dispersion pulsed-pump fiber cavity", *Opt. Lett.* 48(15), 4097 (2023). DOI ✔ 10.1364/OL.492998 — anillo de 230 m bombeado con pulsos de ns; se resuelven oscilaciones de ~10 ps; un potencial de atrapamiento por modulación de fase crea un pulso oscuro persistente (dos ondas enganchadas) — [Peeref](https://peeref.com/works/28627316).
- **Dispersión normal en anillo integrado con bombeo pulsado:** Xu et al., "Harmonic and rational harmonic driving…", *Optica* 7, 940 (2020), DOI ✔ 10.1364/OPTICA.392571 (ver P5), usa un microresonador integrado de 3.23 GHz de FSR — [arXiv:2003.05557](https://ar5iv.labs.arxiv.org/html/2003.05557).

### Inferences
- El bombeo pulsado "regala" la perturbación local que en CW debe proveer un cruce de modos: la envolvente del pulso es un gradiente de bombeo que fija dónde se nuclea y dónde se atrapa la onda de conmutación. Esto hace que los peines de dispersión normal con bombeo pulsado sean deterministas y sintonizables por Δ.
- Los ZDS son la ruta de "banda ancha a bajo FSR": 97 % de octava a 28 GHz con 350 mW medios, cifra fuera del alcance de los solitones brillantes CW en anillos de 28 GHz (los peines CW de octava están a ~1 THz).

### Gaps
- La Nat. Commun. 2022 no reporta eficiencia de conversión numérica del ZDS ni potencia pico medida.
- No pude acceder al texto completo de PRX 13, 011040 para extraer FSR, f_rep y ancho de banda de los peines satélite.
- No encontré un trabajo que etiquete explícitamente "temporal cavity solitons in normal dispersion" con bombeo pulsado; lo más cercano son los pulsos oscuros/ondas de conmutación enganchadas (Garbin 2017, Macnaughtan 2023) y los ZDS.

---

## P4. Comparación con peines CW de octava: ancho de banda, eficiencia y resultados pulsados de octava completa

### Takeaway
En eficiencia, el bombeo pulsado ha pasado del ~1 % del solitón CW convencional a 8 % (Anderson 2021), 34 % estacionario / 54 % con barrido (Li, Vahala et al., Optica 2022, cuña de sílice) y 43.9 % estacionario con fuente de pulsos integrada en LiNbO₃ + anillo Si₃N₄ (Niu et al., LPR 2026); en ancho de banda, EPFL reportó en CLEO 2025 un peine de solitón de octava completa a 15 GHz con ~8800 líneas por bombeo pulsado en un racetrack de Si₃N₄ (solo resumen de congreso), tras el 97 % de octava de los ZDS (2022). El CW mantiene la ventaja de simplicidad, y con "moléculas fotónicas" también alcanza >50 % de eficiencia.

### Cited Findings
- Límite CW: la eficiencia máxima CW (potencia de solitón / potencia de bombeo) de solitones brillantes queda en el rango de ~1 % — [Li et al., Optica 2022, texto NSF PAR](https://par.nsf.gov/servlets/purl/10342164); también "~1 % de la potencia del láser" como base de comparación en Helgason et al. — [arXiv:2202.09410](https://arxiv.org/abs/2202.09410).
- J. Li, C. Bao, Q.-X. Ji, … K. Vahala, "Efficiency of pulse pumped soliton microcombs", *Optica* 9(2), 231–239 (2022). DOI ✔ 10.1364/OPTICA.443060 — microcavidad de cuña de sílice bombeada con pulsos de ps; eficiencia de conversión de solitón único hasta 54 % con láser en barrido y 34 % en estado estacionario; marca previa del bombeo pulsado ≈ 8 %; expresiones analíticas (lagrangiano) de eficiencia y de posición del solitón en el pulso; dependencia con la sintonía no vista en CW — [Caltech Authors](https://authors.library.caltech.edu/records/2k024-tft08); [NSF PAR](https://par.nsf.gov/biblio/10369327).
- R. Niu, S. Wan, P.-Y. Wang, R. Ma, J. Li, F. Bo, Z. Shen, G.-C. Guo, F.-W. Sun, J. Liu, C.-H. Dong, "Photonic Chip-Based High-Efficiency Soliton Microcombs via Electro-Optic-Kerr Synergy", *Laser & Photonics Reviews*, e72005 (2026). DOI ✔ 10.1002/lpor.72005 — láser pulsado en chip (plataforma LNOI) a 35.5 GHz con frecuencia central ampliamente sintonizable, integrado con un microresonador de Si₃N₄; eficiencia bombeo→solitón 43.9 % en estado estacionario — [arXiv:2505.15001](https://arxiv.org/abs/2505.15001).
- Octava completa con bombeo pulsado (congresos): A. Davydova, M. H. Anderson, Z. Qiu, T. J. Kippenberg, "Octave-spanning soliton Kerr microcomb at electronically detectable repetition rate in a Si₃N₄ racetrack resonator", CLEO 2025, paper SS101_2. DOI ✔ 10.1364/CLEO_SI.2025.SS101_2 — solitón de octava a 15 GHz con ondas dispersivas de orden superior, ~8800 líneas, en un único resonador Si₃N₄ con bombeo pulsado — [Optica Publishing](https://opg.optica.org/abstract.cfm?URI=CLEO_SI-2025-SS101_2); versiones: CLEO/Europe‑EQEC 2025 "Octave-Spanning Kerr Frequency Comb in a Si₃N₄ Microresonator at Electronically Detectable Repetition Rate" (DOI ✔ 10.1109/CLEO/EUROPE-EQEC65582.2025.11109798), cuya sinopsis motiva el autorreferenciado f‑2f ("requiere un microcomb potente y de octava") — [búsqueda](https://infoscience.epfl.ch/entities/publication/e41e3b3c-4d91-4230-81b0-bb705a455283?ln=en); y SPIE PC14092 (2026) "Octave-spanning soliton Kerr microcomb with a record number of comb lines at an electronically detectable repetition rate" (DOI ✔ 10.1117/12.3099358).
- Peines de octava CW previos a espaciado ~1 THz (contexto citado por Anderson 2021) — [arXiv:1909.00022](https://ar5iv.labs.arxiv.org/html/1909.00022).
- Autorreferenciado en microcombs CW de Si₃N₄: 2f‑3f con 2/3 de octava (Brasch et al., arXiv:1605.02801 / *Light Sci. Appl.* 2017) — [arXiv:1605.02801](https://arxiv.org/pdf/1605.02801); el esquema f‑2f con pulso doble para atrapar el solitón en un pedestal es, hasta donde encontré, solo simulación (Xue, Zheng, Weiner, arXiv:1707.09116) — [ar5iv](https://ar5iv.arxiv.org/html/1707.09116).
- Alternativa CW de alta eficiencia: Ó. B. Helgason et al., "Surpassing the nonlinear conversion efficiency of soliton microcombs", *Nat. Photon.* 17, 992–999 (2023). DOI ✔ 10.1038/s41566-023-01280-3 — dos anillos acoplados ("molécula fotónica") con eficiencia >50 % y bombeo detuned al azul — [arXiv:2202.09410](https://arxiv.org/abs/2202.09410).
- Alternativa pulsada de bajo costo: W. Weng et al., "Gain-switched semiconductor laser driven soliton microcombs", *Nat. Commun.* 12, 1425 (2021). DOI ✔ 10.1038/s41467-021-21569-7 — láser semiconductor conmutado en ganancia (DFB/FP/DM) con inyección óptica; pulsos ≈10 ps a f_gs = 9.716 GHz (Si₃N₄, FSR 10 GHz, Q ≈ 10⁷, D₂/2π = 15 kHz) y 14.093 GHz (MgF₂, Q ≈ 10⁹, κ/2π = 200 kHz, D₂/2π ≈ 2 kHz); potencia media <10 mW del láser (<5 mW en chip), "un orden de magnitud" por debajo de CW; escalones de solitón >20 MHz (vs ~2 MHz sin inyección desplazada) con chirp óptimo de −18 ps/nm; 100/100 barridos exitosos — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7930029/).

### Inferences
- La ventaja de eficiencia del bombeo pulsado es estructural: la energía del bombeo se concentra en la ventana temporal donde vive el solitón, de modo que la fracción de bombeo "desperdiciada" en el fondo CW desaparece; las cifras 34–54 % (Vahala) y 43.9 % (Niu) son ~1–2 órdenes por encima del ~1 % CW.
- El récord de ancho de banda a espaciado detectable electrónicamente (octava a 15 GHz, ~8800 líneas) solo se ha mostrado en congresos (2025–2026); hasta octubre de 2026 no encontré la versión de revista, así que debe citarse como resultado preliminar.

### Gaps
- No hallé los parámetros de bombeo (potencia media, duración) del peine de octava a 15 GHz de Davydova et al. (solo resumen).
- No encontré una demostración experimental publicada de autorreferenciado f‑2f de un microcomb con bombeo pulsado (la EQEC 2025 lo plantea como motivación; no leí el texto completo).
- No pude extraer la fórmula analítica de eficiencia de Li et al. 2022 (PDF binario no legible por la herramienta); el texto completo está en [NSF PAR](https://par.nsf.gov/servlets/purl/10342164).

---

## P5. Teoría: LLE con bombeo pulsado, desincronización, atrapamiento y mapa de Ikeda

### Takeaway
El marco teórico es la LLE con término de bombeo dependiente del tiempo rápido S(τ) y un término convectivo −d ∂/∂τ que representa la desincronización f_rep − FSR; el solitón es atrapado por el gradiente del pulso (bifurcación de horquilla a dos posiciones simétricas cuando la amplitud pico supera un valor crítico), la desincronización rompe la simetría y desplaza el solitón hasta que se desengancha (saddle‑node, o Andronov‑Hopf para pulsos anchos), y Raman/TOD añaden derivas asimétricas; el bombeo armónico/racional (f_rep ≈ (p/q)·FSR) y la autoexcitación bajo pulsos desincronizados (2025) son extensiones recientes.

### Cited Findings
- **LLE con deriva (Hendry et al.):** I. Hendry, B. Garbin, S. G. Murdoch, S. Coen, M. Erkintalo, "Impact of desynchronization and drift on soliton-based Kerr frequency combs in the presence of pulsed driving fields", *Phys. Rev. A* 100, 023829 (2019). DOI ✔ 10.1103/PhysRevA.100.023829 — [APS](https://link.aps.org/doi/10.1103/PhysRevA.100.023829); [arXiv:1905.09810](https://ar5iv.labs.arxiv.org/html/1905.09810). Ecuación adimensional: ∂E/∂t = [−1 + i(|E|² − Δ) − d ∂/∂τ + i ∂²/∂τ²]E + S(τ), con d = Δt·√(2ℱ/(|β₂|Lπ)), Δt = t_R − t_P (desajuste de periodos), ℱ finesa; S(τ) = S₀ exp[−τ²/(2τ_g²)] con τ_g > Δ^(−1/2). Sin desincronización el solitón deriva a v₀ = a(S,Δ)·dS/dτ y se atrapa donde dS/dτ = 0 o donde S = S_c tal que a(S_c,Δ) = 0; si S₀ > S_c (caso habitual en microresonadores) el centro se desestabiliza por horquilla y aparecen dos posiciones simétricas fuera del pico (hasta tres configuraciones: un solitón a cada lado o dos). Con d ≠ 0 las posiciones cumplen a(S,Δ)·dS/dτ = −d: se rompe la simetría; a Δ ≳ 5 una pequeña d empuja un solitón bajo el umbral de existencia S_min ≈ (8Δ/π²)^(1/2) y queda una sola configuración; para |d| ≳ 0.14 los solitones se desenganchan. Rango de enganche: |d_max| = max|a(S,Δ)·dS/dτ| (Ec. 4), Δt_max = d_max·√(|β₂|Lπ/(2ℱ)), Δf_max = FSR²·Δt_max; el rango de inestabilidad crece al acortar el pulso (gradiente más fuerte). Sin Raman la existencia llega a Δ_max = π²S₀²/8 (≈18.5 para S₀ = √15); con Raman (f_R = 0.18, τ_s = 300 fs) los escalones son asimétricos, solo para d < 0 (la desincronización negativa compensa la deriva Raman: "balance asimétrico"), existencia hasta Δ ≈ 7.5; predicen 27 kHz de rango de desincronización frente a ~100 kHz medidos — [arXiv:1905.09810](https://ar5iv.labs.arxiv.org/html/1905.09810).
- **Atrapamiento y ruptura espontánea de simetría:** I. Hendry et al., "Spontaneous symmetry breaking and trapping of temporal Kerr cavity solitons by pulsed or amplitude-modulated driving fields", *Phys. Rev. A* 97, 053834 (2018). DOI ✔ 10.1103/PhysRevA.97.053834 — los solitones son atraídos a posiciones asociadas a valores específicos del campo de bombeo que dependen solo de los parámetros de la cavidad — [Strathprints](https://strathprints.strath.ac.uk/64362).
- **Bifurcación de desincronización (Andronov‑Hopf):** D. A. Dolinina, G. Huyet, D. Turaev, A. G. Vladimirov, "Desynchronization of temporal solitons in Kerr cavities with pulsed injection", *Opt. Lett.* 49(14), 4050 (2024). DOI ✔ 10.1364/OL.529083 — [arXiv:2404.14113](https://arxiv.org/html/2404.14113v1). LLE con inyección gaussiana η(ξ) = p₀ exp[−(d + ic)ξ²] y deriva V; para p₀ < p_c el solitón está centrado, para p₀ > p_c se desplaza a la periferia (horquilla); la desincronización ocurre típicamente por bifurcación de Andronov‑Hopf (oscilación de amplitud y posición en un rango pequeño) y no por saddle‑node como predice la ecuación de deriva, para pulsos suficientemente anchos (ejemplo: p₀ = 1.9, θ = 3.5: estable a V = 0.053, oscila a V = 0.0544); criterio simple: la AH ocurre cuando el desplazamiento del solitón es máximo, es decir cuando la amplitud local de inyección cae a η₀ (umbral saddle‑node de la inyección homogénea), de modo que solo se necesita el perfil del pulso y η₀; existe un punto de Bogdanov‑Takens que tiende a V = 0 al ensanchar el pulso. Trabajo relacionado del mismo grupo: "Synchronization Between Kerr Cavity Solitons and Broad Laser Pulse Injection", *Photonics* 11(11), 1050 (2024), DOI ✔ 10.3390/photonics11111050 (autores no confirmados por mí; WIAS Preprint 3140) — [MDPI](https://www.mdpi.com/2304-6732/11/11/1050).
- **LLE con bombeo pulsado y desajuste FSR/f_rep (WGM):** T. Daugey, C. Billet, J. Dudley, J.-M. Merolla, Y. K. Chembo, "Kerr optical frequency comb generation using whispering-gallery-mode resonators in the pulsed-pump regime", *Phys. Rev. A* 103, 023521 (2021). DOI ✔ 10.1103/PhysRevA.103.023521 — extiende la LLE para incluir el pulso y el desajuste; énfasis en el ensanchamiento asimétrico del peine por la desincronización; experimento con resonador de MgF₂ milimétrico con Q ≈ 10⁹ y pulsos por compresión de solitón con lente temporal — [UMD](https://ireap.umd.edu/node/2729); [PDF](https://chembolab.umd.edu/files/2021/08/2021_PRA_Pulsed_Pump_Kerr_Comb.pdf).
- **Bombeo armónico y racional:** Y. Xu, Y. Lin, A. Nielsen, I. Hendry, S. Coen, M. Erkintalo, H. Ma, S. G. Murdoch, "Harmonic and rational harmonic driving of microresonator soliton frequency combs", *Optica* 7(8), 940 (2020). DOI ✔ 10.1364/OPTICA.392571 — f_rep cerca de un armónico entero o de una fracción racional del FSR; microresonador integrado de FSR = 3.23 GHz con espaciados 3.23–19.38 GHz; peine a 2·FSR = 6.46 GHz bombeando a 2.15 GHz (= 2/3 FSR); sin ruido de supermodos — [ar5iv](https://ar5iv.labs.arxiv.org/html/2003.05557).
- **Autoexcitación bajo pulsos desincronizados:** M. Macnaughtan, Z. Li, Y. Xu, X. Wei, Z. Yang, S. Coen, M. Erkintalo, S. G. Murdoch, "Soliton self-excitation under pulsed driving in a Kerr resonator", *Phys. Rev. Research* 7, 043250 (3 dic. 2025). DOI ✔ 10.1103/v9wr-dv9y — [APS](https://journals.aps.org/prresearch/abstract/10.1103/v9wr-dv9y); [arXiv:2506.10307](https://arxiv.org/html/2506.10307v1). Fabry–Pérot de fibra: 0.29 m de fibra de dispersión desplazada entre espejos de 0.6 % de transmisión, L = 0.58 m, FSR = 350 MHz, finesa 180, γ = 2.6 W⁻¹km⁻¹, β₂ = −1.23 ps²/km, β₃ = 0.13 ps³/km; pulsos de 1.6 ps (EO desde CW a 1565 nm), ΔT = 2.1 fs de desincronización, 1.85–2.0 W de pico (X ≈ 3.2–3.5); el solitón se autoexcita al bajar la sintonía normalizada por debajo de Δ ≈ 2.45–2.49 porque el estado homogéneo inferior desaparece y el solitón es "el único estado disponible"; mecanismo de auto‑conmutación (no Hopf ni deriva); estados ligados de 2 y 3 solitones deterministas; la región de autoexcitación de solitón único es mayor a menor potencia y pulsos más cortos; proponen un microresonador bombeado EO completamente integrado (LiNbO₃/LiTaO₃) — [arXiv:2506.10307](https://arxiv.org/html/2506.10307v1).
- **Modulación del bombeo y sincronización:** Mizrahi et al., "Soliton synchronization in microresonators with a modulated pump", *Phys. Rev. E* 109, 064204 (2024). DOI ✔ 10.1103/PhysRevE.109.064204 — ancho del rango de enganche en función de amplitud, frecuencia y fase de la modulación — [MDSOAR](https://mdsoar.org/items/6ae5936f-abc1-471f-9535-35525ef365fc).
- **Pulsos chirpeados:** "Dynamics of cavity soliton driven by chirped optical pulses in Kerr resonators", *Front. Optoelectron.* 15, 14 (2022). DOI ✔ 10.1007/s12200-022-00018-3 — [Springer](https://journal.hep.com.cn/foe/EN/10.1007/s12200-022-00018-3); el chirp del pulso también fue clave en Weng 2021 (−18 ps/nm óptimo) — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7930029/).
- **Manipulación en fibra (2026):** Ji, Ren, Yu, Wang, "Manipulation of temporal cavity solitons in pulsed-driving Kerr fiber resonators", *Phys. Rev. A* 114, 023522 (2026). DOI ✔ 10.1103/4hf5-r4nc — [APS](https://link.aps.org/doi/10.1103/4hf5-r4nc) (solo verifiqué metadatos; no leí el contenido).
- **Revisión/tutorial 2026:** S. G. Murdoch, F. Leo, X. Xue, S. Coen, M. Erkintalo, "Temporal dissipative solitons and optical frequency combs in coherently driven Kerr resonators", arXiv:2606.20026 (18 jun. 2026, 124 pp., 58 figs.), revisión de solitones brillantes y ondas de conmutación con métodos numéricos y técnicas de laboratorio — [arXiv](https://arxiv.org/abs/2606.20026) (DOI sin verificar: preprint).

### Inferences
- "Mapa de Ikeda vs LLE": la LLE con bombeo S(τ) y deriva d es el límite de campo medio del mapa de Ikeda con inyección periódica; es la forma usada por todos los trabajos citados (Hendry, Dolinina, Daugey, Macnaughtan, Anderson). Ninguno de los textos revisados necesitó el mapa completo, lo cual sugiere que para finesas ≳100 y pulsos ≫ solitón la LLE basta.
- La desincronización no es solo una tolerancia: es un parámetro de control (desplaza el espectro del peine según Δ·(dFSR/dν)⁻¹, selecciona entre configuraciones de 1 o 2 solitones, compensa la deriva Raman y, en 2025, dispara la autoexcitación).

### Gaps
- No encontré un artículo que trate explícitamente el mapa de Ikeda con bombeo pulsado para microresonadores (los textos usan la LLE); si el curso lo exige, habrá que derivarlo desde la LLE (gap).
- No obtuve la expresión cerrada de la eficiencia pulsada (Li et al. 2022) ni la dependencia explícita del rango de enganche con la duración del pulso (Hendry 2019 solo da la expresión implícita Ec. 4).

---

## P6. Cavidades de fibra bombeadas sincrónicamente (Leo, Coen, Haelterman 2010 y seguidores): qué enseñan

### Takeaway
La observación de solitones temporales de cavidad en un anillo de fibra de sílice (Leo et al., Nat. Photon. 2010, solitones de ~4 ps almacenados >1 s como bits de un buffer óptico) estableció la fenomenología que luego se trasladó a los microresonadores: solitones sobre un fondo CW/pulsado, escritura por pulsos de direccionamiento, atrapamiento por modulación del bombeo, y más tarde (Auckland) el estudio sistemático del bombeo pulsado, la desincronización, las ondas de conmutación y la autoexcitación, en cavidades macroscópicas donde cada parámetro es accesible y medible con resolución de ps.

### Cited Findings
- F. Leo, S. Coen, P. Kockaert, S.-P. Gorza, Ph. Emplit, M. Haelterman, "Temporal cavity solitons in one-dimensional Kerr media as bits in an all-optical buffer", *Nat. Photon.* 4, 471–476 (2010). DOI ✔ 10.1038/nphoton.2010.120 — primera observación experimental de solitones temporales de cavidad en fibra de sílice estándar; solitones de ~4 ps; flujo de datos almacenado durante más de un segundo; capacidad potencial estimada de 45 000 bits a 25 Gb/s — [Nature](https://www.nature.com/articles/nphoton.2010.120); [Auckland ResearchSpace](https://researchspace.auckland.ac.nz/handle/2292/16149).
- Seguimiento: buffer de 4536 bits a 10 Gb/s almacenados un minuto, suprimiendo interacciones entre solitones vecinos mediante modulación de fase del láser de bombeo (arXiv:1607.07154, 2016) — [arXiv](https://arxiv.org/pdf/1607.07154) (DOI sin verificar).
- Ondas de conmutación en anillo de fibra en dispersión normal bombeado sincrónicamente: Garbin et al., EPJD 71, 240 (2017), DOI ✔ 10.1140/epjd/e2017-80133-7 — [Strathprints](https://strathprints.strath.ac.uk/62452).
- Mini‑resonador de fibra (FSR 0.54 GHz) con bombeo pulsado y dispersión normal: Xu et al., OL 46, 512 (2021), DOI ✔ 10.1364/OL.413585 — [arXiv:2010.15228](https://arxiv.org/abs/2010.15228).
- Fabry–Pérot de fibra de 0.58 m (FSR 350 MHz, finesa 180) con pulsos de 1.6 ps y autoexcitación: Macnaughtan et al., PRR 7, 043250 (2025), DOI ✔ 10.1103/v9wr-dv9y — [arXiv:2506.10307](https://arxiv.org/html/2506.10307v1).
- Anillo de 230 m con pulsos de ns para resolver la estructura fina (~10 ps) de ondas de conmutación: Macnaughtan et al., OL 48, 4097 (2023), DOI ✔ 10.1364/OL.492998 — [Peeref](https://peeref.com/works/28627316).
- Dual‑comb con bombeo pulsado sincrónico de dos polarizaciones en un anillo de sílice integrado (birrefringencia → dos f_rep): Y. Xu, M. Erkintalo, Y. Lin, S. Coen, H. Ma, S. G. Murdoch, "Dual-microcomb generation in a synchronously driven waveguide ring resonator", *Opt. Lett.* 46(23), 6002 (2021). DOI ✔ 10.1364/OL.443153 — [arXiv:2109.05393](https://arxiv.org/abs/2109.05393).
- Análogo en espacio libre: N. Lilienfein et al., "Temporal solitons in free-space femtosecond enhancement cavities", *Nat. Photon.* 13, 214–218 (2019). DOI ✔ 10.1038/s41566-018-0341-y — cavidad de realce con placa de zafiro y finesa espectralmente adaptada, bombeada con pulsos de 350 fs a 1035 nm y 100 MHz; ventajas: escalabilidad en potencia, realce de pico con compresión temporal y filtrado de ruido — [FAU CRIS](https://cris.fau.de/publications/296887122/); [MPQ](https://www.mpq.mpg.de/5795456/pr_2019-01-23_lap_solitonen_eng.pdf).

### Inferences
- Lección 1 (2010): el solitón de cavidad Kerr es un objeto robusto que vive sobre un fondo de bombeo y puede escribirse/borrarse localmente; el bombeo pulsado de microresonadores es, en cierto sentido, "escribir un único bit por vuelta" en el lugar donde el pulso de bombeo lo atrapa.
- Lección 2 (Auckland 2017–2025): los parámetros de tolerancia (Δ, detuning, chirp) escalan con la finesa y β₂ (fórmula de Hendry), de modo que los experimentos de fibra con FSR de MHz son bancos de prueba cuantitativos para los anillos de 10–30 GHz.

### Gaps
- No pude leer el texto completo de Leo 2010 (paywall/redirección); longitud del anillo, finesa y potencia CW de bombeo no verificados aquí.
- No verifiqué el DOI del buffer de 10 Gb/s (arXiv:1607.07154).

---

## P7. Requisitos de ingeniería: igualar f_rep al FSR, FSR de 10–30 GHz, racetracks, estabilidad térmica

### Takeaway
Todos los experimentos integrados usan FSR entre 3 y 28 GHz (límite de la electrónica de microondas y de los fotodetectores) con bombeo EO a f_rep = FSR o FSR/2, rangos de enganche de ±10 kHz a ~100 kHz, racetracks de Si₃N₄ para alcanzar FSR bajos, Q cargados de 10⁶–10⁷ y, en la práctica, sin estabilización activa gracias al "thermal locking" (el corrimiento térmico de 10–100 MHz solo cambia el FSR en kHz).

### Cited Findings
- FSR y f_rep en los trabajos revisados: 9.77 GHz (FP de fibra, Obrzud 2017) — [arXiv:1612.08993](https://ar5iv.labs.arxiv.org/html/1612.08993); 27.88 GHz con f_rep = 13.94 GHz (FSR/2) en Si₃N₄ (Anderson 2021, 2022) — [arXiv:1909.00022](https://ar5iv.labs.arxiv.org/html/1909.00022), [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9376110/); 3.23 GHz (anillo integrado, Xu 2020) — [ar5iv](https://ar5iv.labs.arxiv.org/html/2003.05557); 10 GHz Si₃N₄ y ~14 GHz MgF₂ (Weng 2021) — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7930029/); 15 GHz racetrack Si₃N₄ (Davydova 2025) — [Optica Publishing](https://opg.optica.org/abstract.cfm?URI=CLEO_SI-2025-SS101_2); 25 GHz racetrack de LiNbO₃ X‑cut con bombeo pulsado extendiendo el espectro a 350 nm — Nie et al., *eLight* 5, 15 (2025), DOI ✔ 10.1186/s43593-025-00093-x, [arXiv:2502.07180](https://arxiv.org/abs/2502.07180); 35.5 GHz (láser pulsado LNOI integrado, Niu 2026) — [arXiv:2505.15001](https://arxiv.org/abs/2505.15001).
- Rangos de enganche medidos: ~100 kHz (escalón) y ~60 kHz (seguimiento adiabático) a FSR 9.77 GHz — [arXiv:1612.08993](https://ar5iv.labs.arxiv.org/html/1612.08993); 30–50 kHz a 27.88 GHz — [arXiv:1909.00022](https://ar5iv.labs.arxiv.org/html/1909.00022); ≈ ±10 kHz para ZDS — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9376110/); fórmula Δf_max = FSR²·Δt_max con Δt_max = d_max·√(|β₂|Lπ/(2ℱ)) — [arXiv:1905.09810](https://ar5iv.labs.arxiv.org/html/1905.09810).
- Bombeo sub‑armónico: bombear a FSR/2 por límites de RF reduce la eficiencia de conversión a la mitad — [arXiv:1909.00022](https://ar5iv.labs.arxiv.org/html/1909.00022); el bombeo armónico/racional permite elegir el espaciado del peine con un f_rep menor — [ar5iv](https://ar5iv.labs.arxiv.org/html/2003.05557).
- Térmica: corrimiento de resonancia de 10–100 MHz al entrar al solitón → cambio de FSR de unos kHz, dentro del rango tolerado; "thermal locking" sin estabilización activa — [arXiv:1612.08993](https://ar5iv.labs.arxiv.org/html/1612.08993); menor potencia media → menor calentamiento como ventaja explícita — [Nature](https://www.nature.com/articles/nphoton.2017.140); Macnaughtan 2025 estabiliza el detuning con PDH en polarización ortogonal y argumenta mejor eficiencia térmica, de potencia y no lineal del bombeo pulsado, con ventana de operación amplia que permite componentes RF más baratos — [arXiv:2506.10307](https://arxiv.org/html/2506.10307v1).
- Ruido RF → peine: la transferencia de ruido del generador RF se filtra no linealmente (esquina ≈2 MHz ≪ κ = 110 MHz) y el bombeo asíncrono la reduce más — [arXiv:1909.00022](https://ar5iv.labs.arxiv.org/html/1909.00022); Brasch 2019 cuantifica el filtrado de jitter — [arXiv:1907.09715](https://arxiv.org/abs/1907.09715v1).
- Chirp/fase del pulso como grado de libertad de diseño: −18 ps/nm óptimo con pulsos de 10 ps (Weng 2021) — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7930029/); +0.3 ps² en la simulación de Anderson 2021 — [arXiv:1909.00022](https://ar5iv.labs.arxiv.org/html/1909.00022).
- Fuentes de pulsos integradas (2025–2026): láser pulsado LNOI de 35.5 GHz + anillo Si₃N₄ (Niu et al., LPR 2026, DOI ✔ 10.1002/lpor.72005) — [arXiv:2505.15001](https://arxiv.org/abs/2505.15001); peine EO resonante integrado en LiTaO₃ (Zhang et al., "Ultrabroadband integrated electro-optic frequency comb in lithium tantalate", *Nature* 637, 1096–1103 (2025), DOI ✔ 10.1038/s41586-024-08354-4): arquitectura triplemente resonante (microondas + óptica), >450 nm (>60 THz) y >2000 líneas, 16× menos potencia RF que el diseño no resonante, láser DFB híbrido, ~1 cm² — [EPFL](https://actu.epfl.ch/news/compact-comb-lights-the-way-for-next-gen-photoni-8/); [IDEAS/Nature](https://ideas.repec.org/a/nat/nature/v637y2025i8048d10.1038_s41586-024-08354-4.html). (Es un peine EO χ⁽²⁾ resonante, no un solitón Kerr; relevante como fuente de bombeo pulsado integrada.)
- Fabry–Pérot integrados (Herr, Hamburg/DESY): T. Wildi, M. A. Gaafar, T. Voumard, M. Ludwig, T. Herr, "Dissipative Kerr solitons in integrated Fabry–Perot microresonators", *Optica* 10(6), 650–656 (2023). DOI ✔ 10.1364/OPTICA.480789 — reflectores de cristal fotónico, Q intrínseco 4×10⁶ limitado por pérdidas de propagación; bombeo CW — [arXiv:2206.10410](https://arxiv.org/abs/2206.10410).

### Inferences
- Regla de diseño: elegir FSR en 10–30 GHz para que f_rep sea generable con moduladores EO y detectable; usar racetrack para FSR ≤ 15–30 GHz manteniendo radio de curvatura (y evitar pérdidas); tolerancia de FSR ~10⁻⁵–10⁻⁶ ⇒ control de temperatura a nivel de ~0.01–0.1 K (inferencia a partir de kHz/MHz de corrimiento; no cuantificado en las fuentes).
- Para un proyecto de supercontinuo en anillo de SiN (ONL), la ruta "pulsada" implica diseñar el anillo (D₂ pequeño o cero, D₃ fuerte para ondas dispersivas), el bombeo (peine EO de 10–30 GHz, 1 ps, 0.5–6 W pico) y el lazo de Δ (sintonizar f_rep en decenas de kHz).

### Gaps
- Ninguna fuente revisada cuantifica el requisito de estabilidad de temperatura en K para mantener el enganche; solo dan corrimientos (MHz) y rangos (kHz).
- No encontré trabajos pulsados de 2024–2026 de los grupos de Gaeta (Columbia) ni de Srinivasan (NIST) con bombeo pulsado de microresonadores; lo más cercano en NIST es la "Kerr‑induced synchronization" de un solitón a un láser de referencia CW (Moille et al., *Nature* 624, 267–274 (2023), DOI ✔ 10.1038/s41586-023-06730-0), que no es bombeo pulsado. Del grupo de Herr (DESY/Hamburgo) no hallé artículos pulsados posteriores a 2019 (su trabajo 2022–2023 en FP integrados es CW).

---

## P8. Grupos líderes y sus trabajos más recientes (2024–2026)

### Takeaway
EPFL (Kippenberg, con M. H. Anderson y A. Davydova) lidera el bombeo pulsado integrado en Si₃N₄ (octava a 15 GHz, 2025–2026); Auckland (Erkintalo, Coen, Murdoch, Xu, Macnaughtan) lidera la teoría/fibra (autoexcitación 2025, revisión 2026); Caltech (Vahala) aportó la teoría de eficiencia (2022); grupos chinos (USTC/Nankai/Pekín) introdujeron fuentes pulsadas LNOI integradas (2025–2026); Herr (DESY/Hamburgo) originó la técnica (2017–2019) pero su producción reciente en resonadores integrados es CW.

### Cited Findings
- EPFL/Kippenberg: Davydova, Anderson, Qiu, Kippenberg, CLEO 2025 SS101_2 (DOI ✔ 10.1364/CLEO_SI.2025.SS101_2), EQEC 2025 (DOI ✔ 10.1109/CLEO/EUROPE-EQEC65582.2025.11109798), SPIE PC14092 (2026, DOI ✔ 10.1117/12.3099358) — [Infoscience](https://infoscience.epfl.ch/entities/publication/e41e3b3c-4d91-4230-81b0-bb705a455283?ln=en); peine EO resonante en LiTaO₃, *Nature* 637, 1096 (2025), DOI ✔ 10.1038/s41586-024-08354-4 — [EPFL](https://actu.epfl.ch/news/compact-comb-lights-the-way-for-next-gen-photoni-8/).
- Auckland/Erkintalo–Coen–Murdoch: PRR 7, 043250 (2025), DOI ✔ 10.1103/v9wr-dv9y — [APS](https://journals.aps.org/prresearch/abstract/10.1103/v9wr-dv9y); OL 48, 4097 (2023), DOI ✔ 10.1364/OL.492998; revisión arXiv:2606.20026 (2026) — [arXiv](https://arxiv.org/abs/2606.20026).
- Caltech/Vahala: Optica 9, 231 (2022), DOI ✔ 10.1364/OPTICA.443060 — [Caltech](https://authors.library.caltech.edu/records/2k024-tft08).
- Herr (CSEM → DESY/Universität Hamburg): Nat. Photon. 11, 600 (2017); Nat. Photon. 13, 31 (2019); Optica 6, 1386 (2019); Optica 10, 650 (2023, CW) — DOI ✔ ver tabla.
- Grupos chinos: Niu … J. Liu, C.-H. Dong, LPR e72005 (2026), DOI ✔ 10.1002/lpor.72005 — [arXiv:2505.15001](https://arxiv.org/abs/2505.15001); Nie … F. Bo, Q.-F. Yang, *eLight* 5, 15 (2025), DOI ✔ 10.1186/s43593-025-00093-x — [arXiv:2502.07180](https://arxiv.org/abs/2502.07180); Ji, Ren, Yu, Wang, PRA 114, 023522 (2026), DOI ✔ 10.1103/4hf5-r4nc.
- WIAS Berlín/Vladimirov (teoría de bifurcaciones): OL 49, 4050 (2024), DOI ✔ 10.1364/OL.529083; *Photonics* 11, 1050 (2024), DOI ✔ 10.3390/photonics11111050.
- NIST/Srinivasan (relacionado, no pulsado): Moille et al., *Nature* 624, 267 (2023), DOI ✔ 10.1038/s41586-023-06730-0.

### Inferences
- La frontera 2025–2026 se mueve hacia (i) octava completa a f_rep detectable y (ii) integración de la fuente de pulsos (LNOI/LiTaO₃) con el anillo Kerr en un solo módulo con eficiencias ≥40 %.

### Gaps
- No encontré trabajos pulsados recientes de Gaeta (Columbia) ni Vahala (Caltech, después de 2022) ni Herr (después de 2019) en microresonadores; se declara como vacío, no como inexistencia.
- Los resultados de octava a 15 GHz de EPFL siguen sin versión de revista verificable a octubre de 2026 (según mis búsquedas).

---

## P9. Tabla de referencias con DOI verificado (resueltos por doi.org y Crossref el 2026-10-29)

### Takeaway
Treinta y seis DOI verificados; dos ítems quedan como "DOI sin verificar" (preprints arXiv sin versión de revista encontrada).

### Cited Findings
| Referencia | Revista, vol., pág. (año) | DOI |
|---|---|---|
| Obrzud, Lecomte, Herr — Temporal solitons in microresonators driven by optical pulses | Nat. Photon. 11, 600–607 (2017) | ✔ 10.1038/nphoton.2017.140 |
| Obrzud, Lecomte, Herr — Temporal dissipative solitons in a FP microresonator driven by optical pulses | CLEO/Europe‑EQEC 2017 | ✔ 10.1109/CLEOE-EQEC.2017.8087533 |
| Obrzud et al. — Temporal cavity solitons in synchronously driven FP microresonators | Proc. SPIE 10518 (2018) | ✔ 10.1117/12.2289778 |
| Obrzud et al. — A microphotonic astrocomb | Nat. Photon. 13, 31–35 (2019) | ✔ 10.1038/s41566-018-0309-y |
| Brasch, Obrzud, Lecomte, Herr — Nonlinear filtering of an optical pulse train using DKS | Optica 6, 1386 (2019) | ✔ 10.1364/OPTICA.6.001386 |
| Anderson et al. — Photonic chip-based resonant supercontinuum via pulse-driven Kerr microresonator solitons | Optica 8, 771 (2021) | ✔ 10.1364/OPTICA.403302 |
| Anderson et al. — Zero dispersion Kerr solitons in optical microresonators | Nat. Commun. 13, 4764 (2022) | ✔ 10.1038/s41467-022-31916-x |
| Anderson et al. — Dissipative solitons and switching waves in dispersion-modulated Kerr cavities | Phys. Rev. X 13, 011040 (2023) | ✔ 10.1103/PhysRevX.13.011040 |
| Davydova, Anderson, Qiu, Kippenberg — Octave-spanning soliton Kerr microcomb … Si₃N₄ racetrack | CLEO 2025, SS101_2 | ✔ 10.1364/CLEO_SI.2025.SS101_2 |
| Davydova et al. — Octave-spanning Kerr frequency comb in a Si₃N₄ microresonator at electronically detectable repetition rate | CLEO/Europe‑EQEC 2025 | ✔ 10.1109/CLEO/EUROPE-EQEC65582.2025.11109798 |
| Davydova et al. — Octave-spanning soliton Kerr microcomb with a record number of comb lines… | Proc. SPIE PC14092 (2026) | ✔ 10.1117/12.3099358 |
| Weng et al. — Gain-switched semiconductor laser driven soliton microcombs | Nat. Commun. 12, 1425 (2021) | ✔ 10.1038/s41467-021-21569-7 |
| Zhang et al. — Ultrabroadband integrated electro-optic frequency comb in lithium tantalate | Nature 637, 1096–1103 (2025) | ✔ 10.1038/s41586-024-08354-4 |
| Leo et al. — Temporal cavity solitons in one-dimensional Kerr media as bits in an all-optical buffer | Nat. Photon. 4, 471–476 (2010) | ✔ 10.1038/nphoton.2010.120 |
| Garbin et al. — Switching wave dynamics in a normally dispersive fibre ring resonator | Eur. Phys. J. D 71, 240 (2017) | ✔ 10.1140/epjd/e2017-80133-7 |
| Hendry et al. — Spontaneous symmetry breaking and trapping of temporal Kerr cavity solitons by pulsed or AM driving | Phys. Rev. A 97, 053834 (2018) | ✔ 10.1103/PhysRevA.97.053834 |
| Hendry et al. — Impact of desynchronization and drift on soliton-based Kerr combs with pulsed driving | Phys. Rev. A 100, 023829 (2019) | ✔ 10.1103/PhysRevA.100.023829 |
| Xu et al. — Harmonic and rational harmonic driving of microresonator soliton frequency combs | Optica 7, 940 (2020) | ✔ 10.1364/OPTICA.392571 |
| Xu et al. — Frequency comb generation in a pulse-pumped normal dispersion Kerr mini-resonator | Opt. Lett. 46, 512 (2021) | ✔ 10.1364/OL.413585 |
| Xu et al. — Dual-microcomb generation in a synchronously driven waveguide ring resonator | Opt. Lett. 46, 6002 (2021) | ✔ 10.1364/OL.443153 |
| Macnaughtan et al. — Temporal characteristics of stationary switching waves in a normal dispersion pulsed-pump fiber cavity | Opt. Lett. 48, 4097 (2023) | ✔ 10.1364/OL.492998 |
| Macnaughtan et al. — Soliton self-excitation under pulsed driving in a Kerr resonator | Phys. Rev. Research 7, 043250 (2025) | ✔ 10.1103/v9wr-dv9y |
| Daugey, Billet, Dudley, Merolla, Chembo — Kerr comb generation using WGM resonators in the pulsed-pump regime | Phys. Rev. A 103, 023521 (2021) | ✔ 10.1103/PhysRevA.103.023521 |
| Dolinina, Huyet, Turaev, Vladimirov — Desynchronization of temporal solitons in Kerr cavities with pulsed injection | Opt. Lett. 49, 4050 (2024) | ✔ 10.1364/OL.529083 |
| (Vladimirov group) — Synchronization between Kerr cavity solitons and broad laser pulse injection | Photonics 11, 1050 (2024) | ✔ 10.3390/photonics11111050 (autores no confirmados) |
| Mizrahi et al. — Soliton synchronization in microresonators with a modulated pump | Phys. Rev. E 109, 064204 (2024) | ✔ 10.1103/PhysRevE.109.064204 |
| Ji, Ren, Yu, Wang — Manipulation of temporal cavity solitons in pulsed-driving Kerr fiber resonators | Phys. Rev. A 114, 023522 (2026) | ✔ 10.1103/4hf5-r4nc |
| Li, Bao, Ji, …, Vahala — Efficiency of pulse pumped soliton microcombs | Optica 9, 231–239 (2022) | ✔ 10.1364/OPTICA.443060 |
| Helgason et al. — Surpassing the nonlinear conversion efficiency of soliton microcombs (CW, molécula fotónica) | Nat. Photon. 17, 992–999 (2023) | ✔ 10.1038/s41566-023-01280-3 |
| Niu et al. — Photonic chip-based high-efficiency soliton microcombs via electro-optic-Kerr synergy | Laser Photonics Rev. e72005 (2026) | ✔ 10.1002/lpor.72005 |
| Nie et al. — Soliton microcombs in X-cut LiNbO₃ microresonators | eLight 5, 15 (2025) | ✔ 10.1186/s43593-025-00093-x |
| Wildi, Gaafar, Voumard, Ludwig, Herr — Dissipative Kerr solitons in integrated Fabry–Perot microresonators (CW) | Optica 10, 650–656 (2023) | ✔ 10.1364/OPTICA.480789 |
| Lilienfein et al. — Temporal solitons in free-space femtosecond enhancement cavities | Nat. Photon. 13, 214–218 (2019) | ✔ 10.1038/s41566-018-0341-y |
| Moille et al. — Kerr-induced synchronization of a cavity soliton to an optical reference (NIST, no pulsado) | Nature 624, 267–274 (2023) | ✔ 10.1038/s41586-023-06730-0 |
| Herr et al. — Temporal solitons in optical microresonators (CW, referencia base) | Nat. Photon. 8, 145–152 (2014) | ✔ 10.1038/nphoton.2013.343 |
| Kang et al. — Deterministic generation of single soliton Kerr comb by a single shot pulsed trigger | Opt. Express 26, 18563 (2018) | ✔ 10.1364/OE.26.018563 |
| — Dynamics of cavity soliton driven by chirped optical pulses in Kerr resonators | Front. Optoelectron. 15, 14 (2022) | ✔ 10.1007/s12200-022-00018-3 |
| Murdoch, Leo, Xue, Coen, Erkintalo — Temporal dissipative solitons and optical frequency combs in coherently driven Kerr resonators (revisión) | arXiv:2606.20026 (2026) | DOI sin verificar (preprint) |
| — An all-optical buffer based on temporal cavity solitons operating at 10 Gb/s | arXiv:1607.07154 (2016) | DOI sin verificar |

### Inferences
- La numeración correcta del PRX de Anderson 2023 es **13, 011040** (no 021018, como sugería el enunciado de la tarea).

### Gaps
- No se verificó la versión de revista (si existe) de arXiv:2606.20026 ni de arXiv:1607.07154; el DOI de "Synchronization between Kerr cavity solitons and broad laser pulse injection" resuelve en MDPI pero no confirmé la lista de autores.
