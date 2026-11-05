# Modelos teóricos para simular dinámica χ⁽³⁾ en microanillos (énfasis en configuración ADD-DROP)

> Notas de investigación (2026-10-26). Convención: SI. Todas las DOI se comprobaron contra la API de Crossref
> (api.crossref.org/works/<doi>) en esta sesión; se marcan [VERIFICADO] cuando Crossref devolvió título/revista/año
> coincidentes. **Advertencia de honestidad:** de la mayoría de artículos solo se pudo leer el resumen (los PDF no se
> pudieron extraer en esta máquina). Las ecuaciones de las secciones 1–4 son las formas estándar de la literatura
> (Herr 2014, Kippenberg 2018, Coen 2013, Chembo 2013) escritas de memoria y revisadas por consistencia
> dimensional; se marcan como «forma estándar» y conviene cotejar factores de 2 contra el suplemento de Herr 2014
> o la revisión de Kippenberg 2018 antes de implementar. Las derivaciones propias se marcan como **Inferencia**.

## 1. LLE dimensional y normalizada; cuándo vale la LLE y cuándo hace falta Ikeda / modelo de ida y vuelta

### Takeaway
La LLE (modelo de campo medio) es la herramienta estándar para combs Kerr, solitones y pulsos oscuros en anillos de
alta finesse; deja de ser válida cuando la pérdida/acoplo por vuelta o el desfase no lineal por vuelta no son
pequeños (baja finesse, potencias muy altas, multiestabilidad), y entonces se usa el mapa de Ikeda (ida y vuelta con
condición de contorno del acoplador) o la expansión modal acoplada.

### Cited Findings
- Origen: Lugiato & Lefever introdujeron la ecuación para estructuras disipativas en cavidades pasivas Kerr — [Lugiato & Lefever, PRL 58, 2209 (1987), doi:10.1103/PhysRevLett.58.2209 [VERIFICADO]](https://doi.org/10.1103/PhysRevLett.58.2209). El mapa de Ikeda (estados estacionarios multivaluados de una cavidad en anillo) es el modelo «exacto» de ida y vuelta — [Ikeda, Opt. Commun. 30, 257 (1979), doi:10.1016/0030-4018(79)90090-7 [VERIFICADO]](https://doi.org/10.1016/0030-4018(79)90090-7).
- Los solitones disipativos en microresonadores son soluciones de la LLE sobre un fondo CW; se generan al barrer el láser a través del punto de desintonía efectiva cero hacia el rojo; el número de solitones se controla con la desintonía y las transiciones producen escalones discontinuos en la transmisión — [Herr et al., Nat. Photon. 8, 145 (2014), doi:10.1038/nphoton.2013.343 [VERIFICADO]](https://doi.org/10.1038/nphoton.2013.343) (resumen leído en [arXiv:1211.0733](http://arxiv.org/abs/1211.0733)).
- Coen et al. resuelven una LLE generalizada (dispersión de orden superior) con Newton–Raphson y split-step, reproducen combs de una octava y muestran que los combs Kerr corresponden a solitones de cavidad + ondas dispersivas; mucho más rápido que modelos modales — [Coen, Randle, Sylvestre, Erkintalo, Opt. Lett. 38, 37 (2013), doi:10.1364/OL.38.000037 [VERIFICADO]](https://doi.org/10.1364/OL.38.000037) (resumen: [arXiv:1211.1697](http://arxiv.org/abs/1211.1697)).
- Formalismo espaciotemporal LLE para resonadores WGM, equivalente a la expansión modal — [Chembo & Menyuk, PRA 87, 053852 (2013), doi:10.1103/PhysRevA.87.053852 [VERIFICADO]](https://doi.org/10.1103/PhysRevA.87.053852); modelo modal original (ecuaciones acopladas por modo) — [Chembo & Yu, PRA 82, 033801 (2010), doi:10.1103/PhysRevA.82.033801 [VERIFICADO]](https://doi.org/10.1103/PhysRevA.82.033801).
- Análisis de estabilidad de la LLE en dispersión anómala y normal (diagramas de bifurcación: patrones de Turing, solitones, respiradores, caos) — [Godey et al., PRA 89, 063814 (2014), doi:10.1103/PhysRevA.89.063814 [VERIFICADO]](https://doi.org/10.1103/PhysRevA.89.063814).
- Hansson & Wabnitz tratan la generación de combs sin aproximación de campo medio (mapa de Ikeda): a potencia intracavidad alta aparecen regímenes (estados multivaluados, «super cavity solitons») que la LLE no captura; la LLE supone que la desintonía total (lineal + no lineal) por vuelta permanece pequeña — [Hansson & Wabnitz, JOSA B 32, 1259 (2015), doi:10.1364/JOSAB.32.001259 [VERIFICADO]](https://doi.org/10.1364/JOSAB.32.001259) (resumen vía [Chalmers](https://research.chalmers.se/en/publication/221149)); revisión de los tres formalismos (Ikeda, modal, LLE) — [Hansson & Wabnitz, Nanophotonics 5, 231 (2016), doi:10.1515/nanoph-2016-0012 [VERIFICADO]](https://doi.org/10.1515/nanoph-2016-0012).
- Revisiones de referencia: [Kippenberg, Gaeta, Lipson, Gorodetsky, Science 361, eaan8083 (2018), doi:10.1126/science.aan8083 [VERIFICADO]](https://doi.org/10.1126/science.aan8083); [Pasquazi et al., Phys. Rep. 729, 1 (2018), doi:10.1016/j.physrep.2017.08.004 [VERIFICADO]](https://doi.org/10.1016/j.physrep.2017.08.004); [Gaeta, Lipson, Kippenberg, Nat. Photon. 13, 158 (2019), doi:10.1038/s41566-019-0358-x [VERIFICADO]](https://doi.org/10.1038/s41566-019-0358-x); capítulo con descripción analítica/numérica de DKS — [Herr, Gorodetsky, Kippenberg, arXiv:1508.04989](http://arxiv.org/abs/1508.04989).
- Leyes de escala universales de la LLE (normalización) — [Coen & Erkintalo, Opt. Lett. 38, 1790 (2013), doi:10.1364/OL.38.001790 [VERIFICADO]](https://doi.org/10.1364/OL.38.001790). Existencia/estabilidad de solitones del NLS amortiguado y forzado (equivalente a la LLE) — [Barashenkov & Smirnov, PRE 54, 5707 (1996), doi:10.1103/PhysRevE.54.5707 [VERIFICADO]](https://doi.org/10.1103/PhysRevE.54.5707).

**Ecuaciones (forma estándar, convención de modos acoplados de Herr 2014 / Kippenberg 2018):**

1. Espectro de modos: ω_μ = ω₀ + D₁μ + D₂μ²/2 + D₃μ³/6 + … ; D_int(μ) ≡ ω_μ − (ω₀ + D₁μ). μ = número de modo relativo al bombeo.
   - D₁/2π = FSR [Hz]; D₁ = 2π·v_g/L = 2πc/(n_g L), L = 2πR.
   - Conversión desde β₂ (FDE): D₂ ≈ −(c/n_g)·D₁²·β₂ [rad/s] (β₂ en s²/m). β₂ < 0 (anómala) ⇔ D₂ > 0.
   - D₂ también se obtiene numéricamente: D₂ = d²ω_μ/dμ² con ω_μ de las resonancias (n_eff(λ) del FDE + condición n_eff·L = mλ).
2. LLE dimensional (A = amplitud de la envolvente, |A|² = número de fotones intracavidad; φ ∈ [0,2π) coordenada angular en el marco que rota a D₁):

   ∂A/∂t = −(κ/2 + iδω)A + i(D₂/2)∂²A/∂φ² + i g₀|A|²A + √κ_ex · s_in

   - κ = κ₀ + κ_ex [rad/s] (tasa total de decaimiento de energía; Q_L = ω₀/κ); δω = ω₀ − ω_p (δω > 0: bombeo al rojo).
   - s_in = √(P_in/ħω₀) [s⁻¹ᐟ²]; P_in potencia en la guía de bus.
   - Coeficiente Kerr por fotón: g₀ = ħω₀²c n₂/(n₀² V_eff) [rad/s], n₂ [m²/W], V_eff = A_eff·L [m³].
   - Para orden superior se reemplaza i(D₂/2)∂²_φ por i Σ_{k≥2} (D_k/k!)(−i∂_φ)^k (equivalente a sumar D_int(μ) en el espacio de Fourier).
3. Forma de ida y vuelta (Coen 2013, campo E en √W, tiempo lento t, tiempo rápido τ):

   t_R ∂E/∂t = [−α − iδ₀ + iL Σ_{k≥2} (β_k/k!)(i∂_τ)^k + iγL|E|²]E + √θ · E_in

   - t_R = 1/FSR; α = (α_i L + θ)/2 pérdida total por vuelta (α_i [1/m] pérdida de potencia, θ = transmisión de potencia del acoplador); δ₀ = desfase de desintonía por vuelta; γ = n₂ω₀/(cA_eff) [W⁻¹m⁻¹].
   - Validez: α ≪ 1, θ ≪ 1, |δ₀| ≪ 1, γL|E|² ≪ 1 (alta finesse F = π/α ≫ 1). Si no, usar el mapa de Ikeda: E^{(m+1)}(0,τ) = √(1−θ) e^{iφ₀} E^{(m)}(L,τ) + √θ E_in, con propagación NLSE (split-step) entre acopladores.
4. LLE normalizada (Herr 2014 / Kippenberg 2018): τ' = κt/2, Ψ = √(2g₀/κ) A, ζ₀ = 2δω/κ, d₂ = D₂/κ,

   ∂Ψ/∂τ' = −(1 + iζ₀)Ψ + i(d₂/2)∂²Ψ/∂φ² + i|Ψ|²Ψ + f,   f² = 8 η g₀ P_in/(κ² ħω₀),  η = κ_ex/κ.

   Equivalente en notación Coen/Leo: ∂E/∂t' = [−1 − iΔ + i|E|² − iη_s ∂²_τ]E + S con Δ = δ₀/α, S² = γLθP_in/α³ (η_s = signo de β₂). Umbral de MI: |Ψ|² = 1 (i.e. f² = 1 con ζ₀ = 1… mínimo de umbral en Δ=1); biestabilidad para ζ₀ > √3.
5. Soliton brillante aproximado (Herr 2014): Ψ(φ) ≈ Ψ_cw + √(2ζ₀)·sech(√(ζ₀/d₂)·φ); existencia para √3 ≲ ζ₀ < ζ_max = π²f²/8. Duración dimensional ≈ (1/D₁)√(D₂/(2δω)) (en tiempo). La desintonía máxima en unidades físicas: δω_max = (κ/2)·π²f²/8.

### Inferences
- Para un anillo de Si₃N₄ con Q_L ~10⁶ (κ/2π ≈ 190 MHz) y FSR ~200 GHz la finesse es ~10³ → LLE sobradamente válida. Con Q_L ~10⁴ (κ/2π ≈ 19 GHz) y FSR ~230 GHz la finesse es ~12: la LLE aún es razonable como primera aproximación, pero conviene contrastar con un mapa de Ikeda (pérdida por vuelta ~25 %).
- Para simulaciones octava/supercontinuo intracavidad: misma LLE con D_int completo (tabla de ω_μ del FDE) y, si se requiere, término Raman y dispersión de n₂ / A_eff(ω) (LLE generalizada, Coen 2013).

### Gaps
- No se pudo leer el texto completo de Herr 2014 ni de Kippenberg 2018; los factores numéricos (p.ej. el argumento exacto del sech y el 8 en f²) se escribieron de memoria y deben cotejarse con los suplementos.
- No se encontró un criterio numérico publicado universal (finesse mínima) para la validez de la LLE; Hansson & Wabnitz solo lo formulan cualitativamente (desintonía total por vuelta pequeña).

## 2. Especificidades ADD-DROP (dos buses): Q cargado, umbral, salidas through y drop, filtrado del bombeo

### Takeaway
El puerto drop agrega una tasa κ_ex2 al decaimiento total (κ = κ₀ + κ_ex1 + κ_ex2), lo que sube el umbral (∝ κ³/κ_ex1) pero entrega en el drop una réplica del campo intracavidad ∝ √κ_ex2·A, con el bombeo no amplificado ausente: espectros planos y pulsos visibles sin filtrar. Experimentalmente el drop muestra que la mayor parte de la potencia intracavidad está en el solitón, mientras en el through >99 % es bombeo.

### Cited Findings
- Puerto drop en microanillo de Si₃N₄ (Purdue/Weiner): espectros de salida suaves con potencias comparables entre el bombeo y líneas adyacentes; se observa saturación de la potencia en el drop, explicada semiempíricamente añadiendo saturación del bombeo a un modelo de acoplamiento de modos; la autocorrelación en el drop funciona sin filtrar el bombeo; pulsos mode-locked en dispersión normal — [Wang et al., Opt. Express 22, 12148 (2014), doi:10.1364/OE.22.012148 [VERIFICADO]](https://doi.org/10.1364/OE.22.012148) (resumen en [arXiv:1305.7420](https://arxiv.org/abs/1305.7420)). Un resumen secundario menciona que gran parte del ruido ASE se filtra al transmitirse al drop — [Purdue e-Pubs](https://docs.lib.purdue.edu/nanopub/1463).
- Solitón único caracterizado en el drop: en el through el bombeo es >99 % de la potencia, pero dentro de la cavidad «la mayor parte de la potencia está en el solitón»; en el drop se ve un tren de pulsos brillantes casi limitados por transformada con un fondo CW débil con pequeño desfase — [Wang et al., Opt. Express 24, 10890 (2016), doi:10.1364/OE.24.010890 [VERIFICADO]](https://doi.org/10.1364/OE.24.010890) ([arXiv:1603.03154](https://arxiv.org/abs/1603.03154)). Un resumen de búsqueda atribuye a este trabajo ~85 % de transferencia del bombeo a otras líneas intracavidad vs <1 % en el through — no confirmado en el texto completo.
- Combs de pulsos oscuros (dispersión normal) con alta eficiencia: ~30 % de conversión (~200 mW de comb on-chip sin bombeo); la eficiencia la determinan la condición de acoplo efectiva para el bombeo y el ciclo de trabajo de la estructura temporal — [Xue et al., Laser Photon. Rev. 11, 1600276 (2017), doi:10.1002/lpor.201600276 [VERIFICADO]](https://doi.org/10.1002/lpor.201600276). (Un resumen de búsqueda menciona además 5.2 % en through y comb comparable en drop, total 10.6 %, en un dispositivo de ese trabajo — no confirmado.)
- Eficiencia de conversión de solitones CW típica ~1 % de la potencia del láser; superable (>50 %) desplazando la resonancia de bombeo con dos anillos acoplados — [Helgason et al., Nat. Photon. 17, 992 (2023), doi:10.1038/s41566-023-01280-3 [VERIFICADO]](https://doi.org/10.1038/s41566-023-01280-3). Teoría de eficiencia no lineal de combs Kerr — [Bao et al., Opt. Lett. 39, 6126 (2014), doi:10.1364/OL.39.006126 [VERIFICADO]](https://doi.org/10.1364/OL.39.006126); eficiencia y autodesplazamiento de solitones — [Yi et al., Opt. Lett. 41, 3419 (2016), doi:10.1364/OL.41.003419 [VERIFICADO]](https://doi.org/10.1364/OL.41.003419).
- Láseres de solitón de cavidad en anillo de cuatro puertos (no LLE pura): 45 % (drop) y 25 % (through) de eficiencia de un solitón en anillo de 48.9 GHz — solo resumen de catálogo, sin DOI verificada — [Loughborough repository](https://vufind.lboro.ac.uk/Record/rr-article-21334410/Details) [NO VERIFICADO].
- Transmisión lineal del drop en resonancia: D = 4κ_ex1κ_ex2/(κ₀+κ_ex1+κ_ex2)², máxima con acoplos balanceados — (resultado estándar de modos acoplados, resumido en [búsqueda sobre conversión adiabática en add-drop](https://li01.tci-thaijo.org/index.php/cast/article/view/263506) [fuente secundaria]).

**Ecuaciones add-drop (forma estándar de acoplamiento de modos aplicada a la LLE):**

∂A/∂t = −[(κ₀ + κ_ex1 + κ_ex2)/2 + iδω]A + i(D₂/2)∂²_φA + i g₀|A|²A + √κ_ex1·s_in (+ √κ_ex2·s_add, normalmente 0)

- Through: s_thr(t,φ) = s_in − √κ_ex1·A  →  por modo: s_thr,0 = s_in − √κ_ex1 A₀, s_thr,μ≠0 = −√κ_ex1 A_μ.
- Drop: s_drop = √κ_ex2·A  (convención de signo/fase arbitraria) → P_drop,μ = ħω_μ κ_ex2|A_μ|².
- Normalización: igual que §1 con κ = κ₀+κ_ex1+κ_ex2, η = κ_ex1/κ (solo el bus 1 inyecta), f² = 8ηg₀P_in/(κ²ħω₀).
- Q: 1/Q_L = 1/Q₀ + 1/Q_ex1 + 1/Q_ex2 (Q_i = ω₀/κ_i).

### Inferences
- **Umbral con drop (derivación propia):** en resonancia |A₀|² = 4κ_ex1 P_in/(κ²ħω₀) y el umbral es g₀|A₀|² = κ/2, de donde P_th = κ³ħω₀/(8g₀κ_ex1). Fijados κ₀ y κ_ex2, el mínimo está en κ_ex1 = (κ₀+κ_ex2)/2 (reduce a κ_ex = κ₀/2, η = 1/3 en un solo bus). Para anillo simétrico (κ_ex1 = κ_ex2 = κ_x) el óptimo es κ_x = κ₀/4. El drop siempre sube el umbral respecto al mismo anillo de un bus.
- Las líneas generadas (μ ≠ 0) se reparten entre through y drop en proporción κ_ex1:κ_ex2; el bombeo en el drop solo aparece como κ_ex2|A₀|² (el bombeo transmitido no interfiere), por eso el drop «filtra» el bombeo y el ASE fuera de las resonancias.
- Medir en drop es esencialmente medir el campo intracavidad → ideal para validar simulaciones LLE (espectro intracavidad = espectro drop × constante).

### Gaps
- No se encontró un artículo que optimice teóricamente la eficiencia de solitón en el drop con LLE completa (búsqueda dirigida sin resultados claros).
- No se pudieron extraer del PDF de Wang 2016 los valores Q₀, κ_ex1, κ_ex2, D₂ del dispositivo.

## 3. Umbral paramétrico, D₁/D₂/D_int, regímenes de dispersión, pulsos oscuros/platicones, mode-crossings, existencia del solitón y efectos térmicos

### Takeaway
P_th ∝ n₀²V_eff/(n₂λQ_L²)·(1/η) se calcula directamente de n_eff, A_eff y n_g del FDE más Q₀ y acoplos. En dispersión anómala los solitones existen en √3 ≲ ζ₀ < π²f²/8 y se acceden por barrido rojo (escalones), con el triángulo térmico como obstáculo; en dispersión normal se necesitan mode-crossings o bombeo modulado para pulsos oscuros/platicones.

### Cited Findings
- Fórmula de umbral OPO Kerr (toroide): P_th ≈ 1.54 (π/2)(Q_ex/(2Q_L))·n²V_eff/(n₂λQ_L²) — [Kippenberg, Spillane, Vahala, PRL 93, 083904 (2004), doi:10.1103/PhysRevLett.93.083904 [VERIFICADO]](https://doi.org/10.1103/PhysRevLett.93.083904) (fórmula citada de memoria); análisis de umbral y difusión de fase — [Matsko et al., PRA 71, 033804 (2005), doi:10.1103/PhysRevA.71.033804 [VERIFICADO]](https://doi.org/10.1103/PhysRevA.71.033804).
- Anillos Si₃N₄ de ultra baja pérdida con umbral sub-mW — [Ji et al., Optica 4, 619 (2017), doi:10.1364/OPTICA.4.000619 [VERIFICADO]](https://doi.org/10.1364/OPTICA.4.000619) (valores exactos no leídos).
- Primer oscilador multilongitud de onda CMOS en Si₃N₄ — [Levy et al., Nat. Photon. 4, 37 (2010), doi:10.1038/nphoton.2009.259 [VERIFICADO]](https://doi.org/10.1038/nphoton.2009.259).
- Dinámica universal de formación de combs (MI → caos → solitones) y ruido — [Herr et al., Nat. Photon. 6, 480 (2012), doi:10.1038/nphoton.2012.127 [VERIFICADO]](https://doi.org/10.1038/nphoton.2012.127). Conmutación determinista de solitones (reducción hacia atrás del número de solitones) — [Guo et al., Nat. Phys. 13, 94 (2017), doi:10.1038/nphys3893 [VERIFICADO]](https://doi.org/10.1038/nphys3893). Generación determinista de un solitón evitando la región caótica (rampa de bombeo/desintonía) — [Jaramillo-Villegas et al., Opt. Express 23, 9618 (2015), doi:10.1364/OE.23.009618 [VERIFICADO]](https://doi.org/10.1364/OE.23.009618). Solitones respiradores — [Lucas et al., Nat. Commun. 8, 736 (2017), doi:10.1038/s41467-017-00719-w [VERIFICADO]](https://doi.org/10.1038/s41467-017-00719-w).
- Dispersión normal: combs de pulso oscuro mode-locked en anillos de Si₃N₄ de dispersión normal (iniciados por interacción de modos) — [Xue et al., Nat. Photon. 9, 594 (2015), doi:10.1038/nphoton.2015.137 [VERIFICADO]](https://doi.org/10.1038/nphoton.2015.137); platicones: pulsos de techo plano en GVD normal, generables desde bombeo CW (con desplazamiento de un modo), duración ajustable con la desintonía; el espectro discreto de solitones oscuros de la LLE se vuelve cuasicontinuo — [Lobanov et al., Opt. Express 23, 7713 (2015), doi:10.1364/OE.23.007713 [VERIFICADO]](https://doi.org/10.1364/OE.23.007713) (resumen en [arXiv:1501.07450](http://arxiv.org/abs/1501.07450)); solitones oscuros de la LLE (snaking) — [Parra-Rivas et al., PRA 93, 063839 (2016), doi:10.1103/PhysRevA.93.063839 [VERIFICADO]](https://doi.org/10.1103/PhysRevA.93.063839); revisión — [Xue, Qi, Weiner, Nanophotonics 5, 244 (2016), doi:10.1515/nanoph-2016-0016 [VERIFICADO]](https://doi.org/10.1515/nanoph-2016-0016); acoplamiento de modos en Si₃N₄ de dispersión normal — [Liu et al., Optica 1, 137 (2014), doi:10.1364/OPTICA.1.000137 [VERIFICADO]](https://doi.org/10.1364/OPTICA.1.000137).
- Efectos térmicos: comportamiento térmico dinámico y autoestabilidad térmica («triángulo térmico») — [Carmon, Yang, Vahala, Opt. Express 12, 4742 (2004), doi:10.1364/OPEX.12.004742 [VERIFICADO]](https://doi.org/10.1364/OPEX.12.004742); dinámica térmica + no lineal de DKS y su acoplo con potencia/desintonía (PDH lock) — [Stone et al., PRL 121, 063902 (2018), doi:10.1103/PhysRevLett.121.063902 [VERIFICADO]](https://doi.org/10.1103/PhysRevLett.121.063902) ([arXiv:1708.08405](http://arxiv.org/abs/1708.08405)); control térmico con calentador integrado para acceder a solitones — [Joshi et al., Opt. Lett. 41, 2565 (2016), doi:10.1364/OL.41.002565 [VERIFICADO]](https://doi.org/10.1364/OL.41.002565); acceso estable a solitones de octava (técnica de «power kicking») — [Li et al., Optica 4, 193 (2017), doi:10.1364/OPTICA.4.000193 [VERIFICADO]](https://doi.org/10.1364/OPTICA.4.000193).
- dn/dT: Si₃N₄ y SiOₓ medidos con microanillos — [Arbabi & Goddard, Opt. Lett. 38, 3878 (2013), doi:10.1364/OL.38.003878 [VERIFICADO]](https://doi.org/10.1364/OL.38.003878) (valores recordados: Si₃N₄ ≈ 2.45×10⁻⁵ K⁻¹; SiO₂ ≈ 1×10⁻⁵ K⁻¹ — cotejar). Agua desionizada a 1550 nm: ≈ −1.12×10⁻⁴ °C⁻¹ medido con microanillo de Si; la absorción del agua a 1550 nm ensancha las resonancias — [arXiv:1710.03605](https://arxiv.org/pdf/1710.03605) [sin DOI de revista verificada]. Kerr y propiedades térmicas de guías SiN/SiO₂ PECVD — [Ikeda et al., Opt. Express 16, 12987 (2008), doi:10.1364/OE.16.012987 [VERIFICADO]](https://doi.org/10.1364/OE.16.012987).

**Ecuaciones de umbral (forma estándar):**

P_th = κ²n₀²V_eff/(8ηω₀c n₂) = κ³ħω₀/(8g₀κ_ex1)  ≡  π n₀² V_eff/(4 η λ n₂ Q_L²)  (con κ = ω₀/Q_L).

Desde FDE: n₀ ≈ n_eff (o n_g según convención; diferencias ~10–20 % → reportar cuál), A_eff = (∫|E|²dA)²/∫|E|⁴dA (sobre materiales no lineales; n₂ ponderado si el modo invade el agua), V_eff = A_eff·2πR, D₁ = 2πc/(n_g·2πR), D₂ = −(c/n_g)D₁²β₂.

**Modelo térmico mínimo (forma estándar, Carmon 2004 / Stone 2018):** añadir a la LLE una desintonía térmica δω → δω + Δω_T, con dΔT/dt = −ΔT/τ_th + (κ_abs/C_p)·ħω₀|A|²·… y Δω_T = −ω₀(1/n_g)(∂n_eff/∂T)ΔT, ∂n_eff/∂T = Σ_i Γ_i (dn_i/dT) (Γ_i: fracciones de confinamiento).

### Inferences
- **Números de ejemplo (cálculo propio, λ = 1550 nm, n₂ = 2.4×10⁻¹⁹ m²/W, n₀ = 1.8, R = 100 µm, A_eff = 1 µm² → V_eff = 6.3×10⁻¹⁶ m³, η = 1/3):** P_th ≈ 13 mW (Q_L = 10⁶), ≈ 1.3 W (Q_L = 10⁵), ≈ 130 W (Q_L = 10⁴). Con Q ~10⁴ (cladding de agua + pérdidas), la dinámica Kerr CW es inalcanzable on-chip; incluso con drop el umbral sube más.
- **Agua como cladding:** ∂n_eff/∂T = Γ_core(2.45e-5) + Γ_agua(−1.1e-4) + …; con Γ_agua ≳ 0.2 el coeficiente neto puede hacerse negativo (anillo casi atérmico o con triángulo térmico invertido: la autoestabilidad térmica pasaría del lado azul al rojo). Es una inferencia a verificar con FDE para la sección de seccion_v1.
- En dispersión normal (frecuente en guías SiN gruesas con agua? depende de la geometría) solo pulsos oscuros/platicones, que requieren mode-crossing o bombeo modulado; para un sensor de volumen esto es irrelevante salvo como fenómeno a evitar.

### Gaps
- No se leyeron los valores numéricos de Ji 2017 (umbral sub-mW, Q_int) ni de Arbabi 2013; los valores de dn/dT de SiN y SiO₂ citados son recordados, no extraídos.
- n₂ efectivo con agua (n₂,agua ~ 10⁻²⁰ m²/W, no verificado) no se buscó.

## 4. Supercontinuo vs comb dentro del anillo: ondas dispersivas, ingeniería de D_int, bombeo pulsado

### Takeaway
Dentro del anillo el «supercontinuo» coherente es un solitón disipativo + ondas dispersivas (radiación Cherenkov) donde D_int(μ) = 0; se modela con la LLE generalizada con D_int completo. El bombeo pulsado síncrono (LLE con fuerza dependiente de τ) da solitones con energías de pulso de fJ por debajo del umbral CW.

### Cited Findings
- Solitones sub-30 fs en anillos de Si₃N₄ con ingeniería de dispersión; la radiación Cherenkov inducida por dispersión de orden superior extiende el comb a 2/3 de octava, coherente y estabilizable — [Brasch et al., Science 351, 357 (2016), doi:10.1126/science.aad4811 [VERIFICADO]](https://doi.org/10.1126/science.aad4811) ([arXiv:1410.8598](http://arxiv.org/abs/1410.8598)).
- Observación de emisión de ondas dispersivas por solitones de cavidad temporal — [Jang et al., Opt. Lett. 39, 5503 (2014), doi:10.1364/OL.39.005503 [VERIFICADO]](https://doi.org/10.1364/OL.39.005503).
- Combs DKS de una octava en Si₃N₄ — [Pfeiffer et al., Optica 4, 684 (2017), doi:10.1364/OPTICA.4.000684 [VERIFICADO]](https://doi.org/10.1364/OPTICA.4.000684); comb de una octava en chip de Si₃N₄ (no solitónico) — [Okawachi et al., Opt. Lett. 36, 3398 (2011), doi:10.1364/OL.36.003398 [VERIFICADO]](https://doi.org/10.1364/OL.36.003398).
- Bombeo pulsado: pulsos ps periódicos generan solitones fs deterministas sobre el pulso de bombeo resonante; el solitón se engancha al pulso (control de f_rep y f_ceo); comb ancho con energías de fJ y potencias medias muy por debajo del umbral CW; «une la óptica no lineal resonante y el supercontinuo no resonante» — [Obrzud, Lecomte, Herr, Nat. Photon. 11, 600 (2017), doi:10.1038/nphoton.2017.140 [VERIFICADO]](https://doi.org/10.1038/nphoton.2017.140) ([arXiv:1612.08993](http://arxiv.org/abs/1612.08993)).
- Desplazamiento Raman de DKS (término a añadir para combs anchos) — [Karpov et al., PRL 116, 103902 (2016), doi:10.1103/PhysRevLett.116.103902 [VERIFICADO]](https://doi.org/10.1103/PhysRevLett.116.103902). Coherencia de combs Kerr (MI vs solitón) — [Erkintalo & Coen, Opt. Lett. 39, 283 (2014), doi:10.1364/OL.39.000283 [VERIFICADO]](https://doi.org/10.1364/OL.39.000283). Modelocking fs en chip — [Saha et al., Opt. Express 21, 1335 (2013), doi:10.1364/OE.21.001335 [VERIFICADO]](https://doi.org/10.1364/OE.21.001335). Bombeo bicromático — [Hansson & Wabnitz, PRA 90, 013811 (2014), doi:10.1103/PhysRevA.90.013811 [VERIFICADO]](https://doi.org/10.1103/PhysRevA.90.013811). Solitón de microondas en sílice — [Yi et al., Optica 2, 1078 (2015), doi:10.1364/OPTICA.2.001078 [VERIFICADO]](https://doi.org/10.1364/OPTICA.2.001078).

**LLE con bombeo pulsado (forma estándar):** se sustituye √κ_ex·s_in por √κ_ex·s_in(τ) con s_in(τ) periódica de período t_R (o desintonía de sincronía Δf_rep → término −Δ·∂_φA de deriva). Ondas dispersivas: fase emparejada donde D_int(μ_DW) ≈ 0 (con corrección no lineal pequeña).

### Inferences
- Para Q ~10⁴ el bombeo pulsado (mayor potencia pico con baja potencia media) es la única vía realista a fenómenos Kerr en el anillo; aun así, con finesse ~10 el realce es pequeño y el sistema se parece más a supercontinuo en guía con retroalimentación débil → usar mapa de Ikeda / NLSE por vuelta.

### Gaps
- No se extrajeron parámetros cuantitativos (D₂, D₃) del dispositivo de Brasch 2016.

## 5. Tabla de parámetros típicos Si₃N₄ (1550 nm) y efecto de agua / Q bajo

### Takeaway
Rangos reportados: Q_int ~10⁶ (estándar) hasta >3×10⁷ (ultra baja pérdida), FSR ~0.1–1 THz, D₂/2π ~ MHz, κ/2π ~ 10–200 MHz, γ ~ 1 W⁻¹m⁻¹, P_th de sub-mW a decenas de mW. Con agua y Q ~10⁴ el umbral CW pasa a ~10² W: inviable.

### Cited Findings
- Q medio > 30×10⁶ (1.0 dB/m) en obleas de 4", confirmado por ringdown con 19 ns de almacenamiento — [Liu et al., Nat. Commun. 12, 2236 (2021), doi:10.1038/s41467-021-21973-z [VERIFICADO]](https://doi.org/10.1038/s41467-021-21973-z) (abstract leído vía Crossref).
- Umbral sub-mW con anillos de ultra baja pérdida — [Ji et al. 2017, doi:10.1364/OPTICA.4.000619 [VERIFICADO]](https://doi.org/10.1364/OPTICA.4.000619).
- Plataformas SiN/Hydex para óptica no lineal (n₂, γ, pérdidas) — [Moss et al., Nat. Photon. 7, 597 (2013), doi:10.1038/nphoton.2013.183 [VERIFICADO]](https://doi.org/10.1038/nphoton.2013.183); n₂ de SiN PECVD — [Ikeda et al. 2008, doi:10.1364/OE.16.012987 [VERIFICADO]](https://doi.org/10.1364/OE.16.012987).
- Agua: dn/dT ≈ −1.12×10⁻⁴ °C⁻¹ y absorción a 1550 nm que ensancha resonancias — [arXiv:1710.03605](https://arxiv.org/pdf/1710.03605).

Tabla orientativa (cálculo propio con las fórmulas de §1–3; n₂ = 2.4×10⁻¹⁹ m²/W valor típico de la literatura citada, no extraído):

| Magnitud | Valor típico | Cómo se obtiene |
|---|---|---|
| FSR (R = 100 µm, n_g = 2.1) | ≈ 227 GHz | c/(n_g·2πR) |
| κ/2π (Q_L = 10⁶ / 10⁴) | 193 MHz / 19 GHz | f₀/Q_L |
| γ (A_eff = 1 µm²) | ≈ 0.97 W⁻¹m⁻¹ | n₂ω₀/(cA_eff) |
| g₀/2π (V_eff = 6.3×10⁻¹⁶ m³, n₀=1.8) | ≈ 0.9 Hz (g₀ ≈ 5.5 rad/s) | ħω₀²cn₂/(n₀²V_eff)/2π |
| P_th (η = 1/3; Q_L = 10⁶/10⁵/10⁴) | 13 mW / 1.3 W / 130 W | π n₀²V_eff/(4ηλn₂Q_L²) |
| D₂/2π (β₂ = −50 ps²/km, FSR 227 GHz) | ≈ +2.3 MHz | −(c/n_g)D₁²β₂/2π |

### Inferences
- D₂/2π ∝ FSR²·|β₂|: con FSR ~230 GHz, |β₂| ~ decenas de ps²/km ya da D₂/2π ~ MHz; reportar siempre FSR junto con D₂.
- Con Q ~10⁴, D₂/κ ~10⁻⁴–10⁻⁵: solitones (si existieran) abarcarían muchos modos, pero el problema es la potencia, no la dispersión.

### Gaps
- No se obtuvieron D₂/2π publicados exactos para dispositivos concretos (PDF no legibles); verificar con Brasch 2016 / Pfeiffer 2017.
- Valor de n₂ del agua y su contribución a g₀ no verificados.

## 6. Relación con sensado de índice: corrimientos Kerr/térmicos como ruido o sesgo; uso de estados de comb/solitón para sensar

### Takeaway
En un refractómetro de anillo los corrimientos Kerr (∝ g₀|A|²) y térmicos (∝ potencia absorbida × ∂n_eff/∂T) sesgan la longitud de onda de resonancia y deforman la línea (triángulo); con agua el término térmico domina y puede invertir su signo. Hay propuestas recientes (no revisadas por pares) de usar el estado dinámico del comb como observable de sensado.

### Cited Findings
- Medir el TOC de la muestra y la temperatura on-chip permite compensar el ruido térmico en refractometría con sensores integrados — [arXiv:1710.03605](https://arxiv.org/pdf/1710.03605).
- Propuesta de sensado de nanopartículas usando el estado macroscópico del comb (caos/Turing/solitón/respirador) en vez de pequeños corrimientos; un corrimiento al rojo inducido disminuye la desintonía normalizada, y los puntos de operación preferidos están en solitón/respirador cerca de las fronteras de bifurcación — [arXiv:2603.10273 (2026, preprint)](https://arxiv.org/html/2603.10273v1) [sin DOI; NO VERIFICADO].
- La pequeña V de los microresonadores los hace muy susceptibles a efectos termo-refractivos; se proponen dos resonadores acoplados para mitigarlo — [SPIE Proc. 12871, 1287109 (2024)](https://biomedicaloptics.spiedigitallibrary.org/conference-proceedings-of-spie/12871/1287109/Mitigation-of-thermal-instabilities-in-Kerr-microcombs/10.1117/12.3003240.full) [DOI 10.1117/12.3003240 NO VERIFICADO en Crossref].
- Autoestabilidad térmica y distorsión triangular — [Carmon 2004, doi:10.1364/OPEX.12.004742 [VERIFICADO]](https://doi.org/10.1364/OPEX.12.004742).

### Inferences
- Sesgo Kerr en un sensor lineal: Δω_Kerr = −g₀|A|² (rad/s). Con Q_L ~10⁴, η = 1/3 y P_in = 1 mW: |A|² = 4κ_ex1P/(κ²ħω₀) ≈ 9×10⁴ fotones → Δω_Kerr/2π ≈ 0.08 MHz ≪ κ/2π = 19 GHz: despreciable. El sesgo térmico (absorción del agua) será mucho mayor y es el relevante.
- Para el sensor de volumen del proyecto (n = 1.33→1.37), los estados de comb no son necesarios ni accesibles con Q ~10⁴; la LLE sirve aquí principalmente para acotar potencias máximas de operación lineal (P_in ≪ P_th y Δω_T ≪ κ).

### Gaps
- No se encontraron trabajos experimentales revisados por pares que usen solitones/combs Kerr para refractometría de volumen en líquidos.
