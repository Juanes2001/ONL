# Propiedades ópticas no lineales (y lineales asociadas) del nitruro de silicio para modelar supercontinuo (ventana nov-2021 – nov-2026)

> Notas de investigación (agente de búsqueda, 2026-11-14). Convención SI: n2 en m²/W, β_TPA en m/W, γ en W⁻¹m⁻¹.
> Etiquetas de acceso: **OA** = acceso abierto; **arXiv** = preprint gratuito; **PAY** = de pago.
> Los valores marcados **[pre-2021]** son solo línea base. Los marcados **[memoria, verificar]** NO se
> verificaron en esta sesión contra la fuente y hay que cotejarlos antes de usarlos.

## Tabla resumen de parámetros (para el protocolo FDE → γ, β2..βn → GNLSE)

| Parámetro | Material / película | Valor | λ | Método | Fuente (acceso) |
|---|---|---|---|---|---|
| n2 | Si3N4 LPCVD (Damascene, recocido) | (2.2 ± 0.1)×10⁻¹⁹ m²/W | 1550 nm | Espectroscopía fototérmica en cavidad (separa Kerr de térmico), TE (suma) + bomba TE/sonda TM (cociente) | Gao et al., Nat. Commun. 13, 3323 (2022), doi:10.1038/s41467-022-30966-5 (**OA**) |
| n2 | SiN, 4 estequiometrías (n0 = 1.907–1.995) | 1.62×10⁻¹⁹ (n0=1.907); 2.25×10⁻¹⁹ (1.978); 2.35×10⁻¹⁹ (1.988); 2.44×10⁻¹⁹ (1.995) m²/W, incertidumbre ±1.3–2 % | 1544–1551 nm (bomba), ~1525 nm (sonda) | Corrimiento inducido de dos modos de la misma familia (sin efecto térmico); cumple la regla de Miller | Tian et al., Opt. Lett. 51(15), 4424 (2026), doi:10.1364/OL.605726 (**PAY**) |
| n2 [pre-2021] | SiN PECVD/Si3N4 | 2.4×10⁻¹⁹ m²/W | 1550 nm | SPM en guía | Ikeda et al., Opt. Express 16, 12987 (2008), doi:10.1364/OE.16.012987 (**OA**) [DOI de memoria, verificar] |
| n2 [pre-2021] | Si3N4 (guía rib) | 2.4×10⁻¹⁹ m²/W (=2.4×10⁻¹⁵ cm²/W) | 1550 nm | — | Tan et al., Opt. Commun. (2010), [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0030401810013738) (**PAY**) |
| n2 | SRN deuterado (n = 2.46) | 9.8×10⁻¹⁸ m²/W; γ = 95 W⁻¹m⁻¹ | 1550 nm | Caracterización no lineal en guía | Chia et al., Sci. Rep. 12, 12697 (2022), doi:10.1038/s41598-022-16889-7 (**OA**, arXiv:2202.10023) |
| n2 | SRN (en función del índice) | ≈ (1.26 ± 0.14)×10⁻¹⁷ m²/W (snippet parcialmente ilegible; verificar) | telecom | FWM | Belogolovskii et al., Adv. Photonics Res. (2024), doi:10.1002/adpr.202400017 (OA probable, no verificado: 403 al leerlo) |
| n2 [pre-2021] | USRN (Si7N3, n≈3.1) | 2.8×10⁻¹⁷ m²/W; TPA solo para λ < 1.2 µm; pico anómalo de n2 cerca de 1.45 µm | 0.8–1.6 µm | Z-scan | Sohn et al., Sci. Rep. 9, 10364 (2019), doi:10.1038/s41598-019-46865-7 (**OA**) |
| Q_abs, pérdida por absorción del material | Si3N4 LPCVD | Q_abs = (290 ± 50)×10⁶ → σ_abs = (0.12 ± 0.02) dB/m (Q0 medido del dispositivo 30.5×10⁶, dominado por dispersión/rugosidad) | 1550 nm | Fototérmico | Gao 2022 (**OA**) |
| Sintonización térmica de resonancia | Si3N4 LPCVD en anillo | −2.84 GHz/K (SiO2: −1.83 GHz/K) | 1550 nm | Barrido TEC | Gao 2022 (**OA**) |
| dn/dT | Si3N4 LPCVD | ≈ 2.51×10⁻⁵ K⁻¹ a 300 K (medido 300–460 K) | telecom | Anillo vs. T | [NSF PAR 10385367](https://par.nsf.gov/biblio/10385367) (fecha no confirmada) |
| dn/dT [pre-2021] | SiN PECVD / SiO2 | 2.51×10⁻⁵ / 0.96×10⁻⁵ K⁻¹ a temp. ambiente; cae ~10× a 18 K | telecom | Anillo criogénico | Elshaari et al., IEEE Photonics J. (2016), [DOAJ](https://doaj.org/article/d3d67ea41c3e4629955b3c7b90436e94) (**OA**) |
| dn/dT | SRN PECVD | 3.28×10⁻⁵ °C⁻¹ (anillo); otros trabajos SRN hasta (1.65 ± 0.08)×10⁻⁴ K⁻¹ (crece con el contenido de Si) | telecom | Anillo vs. T | Appl. Opt. 62(14), 3703 (2023), [eprints IISc](https://eprints.iisc.ac.in/82491/1/app_opt_62-14_3703-3709_2023.pdf) (**OA** copia); [arXiv:2005.13348](https://arxiv.org/abs/2005.13348) [pre-2021] |
| Dispersión de dn/dT | Si3N4 y SiO2 | ~7 % de variación del TRC del material entre telecom y visible (una octava) | 0.78–1.6 µm aprox. | Anillo + modelo de Lorentz dependiente de T | Ou, Moille, Srinivasan, arXiv:2606.05673 (2026) (**arXiv**) |
| Respuesta Raman | Si3N4 amorfo | Tiempo de choque Raman τ_R ≈ 20 fs (inferido del corrimiento de frecuencia del solitón); en la práctica de GNLSE para SiN suele ponerse f_R ≈ 0 | 1550 nm | Corrimiento Raman de solitón (DKS) | Karpov et al., PRL 116, 103902 (2016), doi:10.1103/PhysRevLett.116.103902 [pre-2021] (**arXiv** disponible) |
| Pérdida de propagación | SiN depositado a baja T, compatible con fundición | 42 dB/m (sin recocer) → 28 dB/m (RTA) → 6 dB/m (recocido en horno) | 1550 nm | Anillo | Ji et al., Laser Photonics Rev. (2023), doi:10.1002/lpor.202200544 (**PAY**; arXiv:2301.03053) |
| Pérdida de propagación | SiN PECVD deuterado sin recocer (SiD4 + N2, sin NH3) | mín. 1.77 dB/m; Q_i máx. 14.9×10⁶; la pérdida sube hacia 1520 nm por H residual en el SiD4 | 1550 nm | Anillo | "Anneal-free ultra-low loss silicon nitride integrated photonics", Light Sci. Appl. (2024), doi:10.1038/s41377-024-01503-4 (**OA**) [autores no verificados; probablemente grupo Blumenthal, UCSB] |
| Pérdida de propagación | SiN pulverizado (sputtered) a temp. ambiente | 32 dB/m recién depositado → 5.4 dB/m tras recocer a 400 °C | 1550 nm | Anillo | arXiv:2301.10758 (2023) (**arXiv**) |
| Absorción N–H en cladding | sobretono SiN–H a 1520 nm | > 50 dB/m → ~1 dB/m con cladding de SiO2 deuterado | 1520 nm | — | UCSB, Opt. Lett. 45(12), 3340 (2020) [pre-2021] ([PDF OA](https://optoelectronics.ece.ucsb.edu/sites/default/files/2020-06/ol-45-12-3340.pdf)) |
| Índice lineal (Sellmeier) [pre-2021] | Si3N4 LPCVD | n²−1 = 3.0249 λ²/(λ²−0.1353406²) + 40314 λ²/(λ²−1239.842²), λ en µm, válido 0.31–5.5 µm | — | Elipsometría + prisma | Luke et al., Opt. Lett. 40, 4823 (2015), doi:10.1364/OL.40.004823 **[coeficientes de memoria, verificar]** |
| Índice lineal | SiN LPCVD "estequiométrico", distintas razones NH3/DCS | El índice baja al subir NH3/DCS; cambia la dispersión del material lo bastante como para mover la dispersión del resonador | NIR/telecom | Elipsometría → Sellmeier | Moille et al., arXiv:2109.03291 (2021) (**arXiv**) |
| Índice lineal | SiN PECVD (Ji/Lipson) | Sellmeier ajustado a elipsometría en 200–1690 nm y 1.7–34 µm (ajuste 300–2000 nm) | — | Elipsometría | Ji et al. 2023 (arXiv:2301.03053) |

## 1. Kerr n2: valores 2021–2026, método, dispersión y anisotropía

### Takeaway
Las dos mediciones "sin contaminación térmica" más limpias del periodo dan, para Si3N4 LPCVD a 1550 nm, n2 = (2.2 ± 0.1)×10⁻¹⁹ m²/W (Gao 2022) y n2 = 2.25–2.44×10⁻¹⁹ m²/W para películas casi estequiométricas, que baja a 1.6×10⁻¹⁹ m²/W cuando el índice baja a 1.91 (Tian 2026). El valor clásico 2.4–2.5×10⁻¹⁹ m²/W sigue siendo defendible; una banda de ±10 % (2.2–2.5×10⁻¹⁹) cubre la dispersión entre laboratorios. El SRN da 10⁻¹⁸–10⁻¹⁷ m²/W. No encontré ninguna medición de n2(λ) para Si3N4 estequiométrico en el rango 800–2500 nm.

### Cited Findings
- Si3N4 LPCVD (Damascene fotónico, recocido, n0 = 2.00): n2 = (22 ± 1)×10⁻²⁰ m²/W a 1550 nm (error = desviación estándar), medido por espectroscopía fototérmica con realce de cavidad. El método separa la contribución Kerr de la térmica con una medida de "suma" (modo TE fundamental) y otra de "cociente" (bomba TE, sonda TM). Es un 8 % menor que el valor de Ikeda 2008 (24×10⁻²⁰). — [Gao et al., Nat. Commun. 2022, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9184588/)
- En el mismo trabajo, Ta2O5 sale con n2 = 27×10⁻²⁰ m²/W frente a 62×10⁻²⁰ reportado antes, y AlGaAs con 1700 frente a 2600×10⁻²⁰. Esto sugiere que los valores históricos medidos con métodos sensibles a efectos térmicos pueden estar sobreestimados. — [Gao 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9184588/)
- Cuatro microanillos de SiN con distinta razón Si/N y la misma geometría: n2 = (1.6227 ± 0.0213)×10⁻¹⁹ m²/W (n0 = 1.9071), (2.2515 ± 0.0327)×10⁻¹⁹ (n0 = 1.9782), (2.3523 ± 0.0484)×10⁻¹⁹ (n0 = 1.9884) y (2.4390 ± 0.0463)×10⁻¹⁹ (n0 = 1.9948), con bomba a ~1545–1551 nm. El método compara los corrimientos de resonancia inducidos ópticamente en dos modos de la misma familia, y la relación χ⁽³⁾–χ⁽¹⁾ sigue la regla de Miller. — [Tian et al., Opt. Lett. 51, 4424 (2026), doi:10.1364/OL.605726](https://opg.optica.org/ol/abstract.cfm?uri=ol-51-15-4424) (PAY)
- Línea base [pre-2021]: 2.4×10⁻¹⁹ m²/W a 1.55 µm en guías rib de Si3N4 (Tan 2010) — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0030401810013738). En SC con SiN se sigue citando n2 = 2.4×10⁻¹⁹ m²/W (por ejemplo, en un trabajo de SC coherente ANDi en SiN, Opt. Express 2022) — [resumen de búsqueda, OUCI](https://ouci.dntb.gov.ua/works/4VERgYm7)
- SRN deuterado (n = 2.46): n2 = 9.8×10⁻¹⁸ m²/W, γ = 95 W⁻¹m⁻¹. Los autores señalan que una banda prohibida ancha reduce la absorción pero también n2, de modo que hay un compromiso entre ambos. — [Chia et al., Sci. Rep. 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9325772/)
- SRN, n2 en función del índice por FWM: ≈ (1.26 ± 0.14)×10⁻¹⁷ m²/W en el rango de índices de interés (snippet parcialmente ilegible). — [Belogolovskii et al., Adv. Photonics Res. 2024](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adpr.202400017)
- USRN [pre-2021]: n2 = 2.8×10⁻¹⁷ m²/W (n = 3.1). En la dispersión 0.8–1.6 µm, Kramers–Kronig predice una meseta a λ larga, pero se observa un pico adicional de n2 cerca de 1.45 µm (los autores lo atribuyen a un término n4). — [Sohn et al., Sci. Rep. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6637241)

### Inferences
- Para el Si3N4 LPCVD del proyecto (400 nm, cercano a la estequiometría), un valor central n2 = 2.4×10⁻¹⁹ m²/W con barrido de sensibilidad 2.2–2.5×10⁻¹⁹ es defendible. Si la película tiene un índice medido menor que 2.0 (rica en N), conviene bajar n2 según la tendencia de Tian 2026 (regla de Miller: ~1.6×10⁻¹⁹ para n0 ≈ 1.91).
- Para extrapolar a 1064, 1300 y 780 nm, a falta de una medición directa de n2(λ), lo razonable es suponer n2 casi constante. La banda prohibida del Si3N4 (~5 eV) queda muy lejos de 2ħω incluso a 780 nm (3.2 eV), así que el modelo de Sheik-Bahae predice una dispersión débil y ligeramente creciente hacia λ cortas. Esto es una inferencia teórica, no una medición.
- Anisotropía TE/TM: el material es amorfo e isótropo. Las diferencias TE/TM en γ se deben al área efectiva y al solapamiento modal, no a n2. Gao 2022 usa modos TE y TM en el mismo análisis con un único n2.

### Gaps
- No encontré ninguna medición publicada entre 2021 y 2026 de n2(λ) para Si3N4 estequiométrico en 800–2500 nm, ni de n2 TE frente a TM a nivel de material.
- No encontré mediciones de n2 de SiN PECVD (no rico en Si) ni de SiN pulverizado posteriores a 2021.

## 2. Absorción de dos y tres fotones, banda prohibida y figura de mérito

### Takeaway
En Si3N4 estequiométrico la TPA a 1550 nm es despreciable, y las revisiones recientes lo dan por hecho. El SRN abre una ventana de diseño: al subir el contenido de Si baja la banda prohibida y suben tanto n2 como la TPA. En USRN (Si7N3) la TPA solo aparece para λ < 1.2 µm.

### Cited Findings
- La revisión de 2024 atribuye el liderazgo del SiN en fotónica no lineal integrada a su Kerr fuerte y a la ausencia de TPA en la banda telecom. — [Buzaverov et al., arXiv:2405.10038](https://arxiv.org/abs/2405.10038)
- La banda prohibida del SRN baja con el contenido de Si, hacia la del Si (1.11 eV). La FOM se define como n2/(β_TPA·λ). Los SRN se diseñan para eliminar la TPA en telecom con parámetros no lineales entre 5 y 500 veces mayores que los del Si3N4. — [Ooi/Tan et al., Photonics Res. 6(5), B50 (2018) [pre-2021]](https://opg.optica.org/prj/fulltext.cfm?uri=prj-6-5-B50&id=385631) (OA)
- USRN (Si7N3): TPA solo para λ < 1.2 µm y despreciable a 1.55 µm. — [Sohn 2019](https://www.nature.com/articles/s41598-019-46865-7)
- Si-rich SiN sin efectos de TPA en telecom (Lacava et al. 2017) [pre-2021] — [Sci. Rep. 2017](https://www.nature.com/articles/s41598-017-00062-6)
- Compromiso entre n2 alto y pérdida baja en SRN deuterado — [Chia 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9325772/)

### Inferences
- Bombeo a 780 nm (2ħω = 3.18 eV): sigue sin haber TPA en Si3N4 estequiométrico (banda prohibida ≫ 3.2 eV), pero sí la habría en SRN de banda estrecha (λ < 1.2 µm). En la GNLSE para el Si3N4 del proyecto se puede poner β_TPA = 0 y no incluir portadores libres en todas las bandas de bombeo consideradas.

### Gaps
- No encontré una fuente 2021–2026 con un valor numérico de la banda prohibida óptica del Si3N4 LPCVD (en la literatura clásica suele darse ~5 eV), ni una tabla β_TPA(contenido de Si) para SRN en la ventana. Tampoco encontré mediciones de 3PA en Si3N4.

## 3. Respuesta Raman (f_R, τ_R) y Brillouin

### Takeaway
El Si3N4 amorfo tiene una respuesta Raman débil y ancha. La única cifra cuantitativa usada en la literatura de microcombs es un tiempo de choque Raman τ_R ≈ 20 fs (Karpov 2016, pre-2021). La mayoría de los modelos GNLSE/LLE de SC en SiN fijan f_R = 0 o lo desprecian. El Brillouin también se considera despreciable.

### Cited Findings
- Corrimiento Raman de frecuencia de solitones DKS en Si3N4. Se describe con el término de choque de primer orden de la respuesta Raman, con τ_R ≈ 20 fs para SiN amorfo, y simulaciones LLE con ese término reproducen las observaciones. — [Karpov et al., PRL 116, 103902 (2016)](https://infoscience.epfl.ch/record/218209)
- El Si3N4 tiene un Kerr dominante, casi un orden de magnitud mayor que el de la SiO2, con efectos Raman y Brillouin despreciables. — [revisión de SiN de ultrabaja pérdida, researching.cn](https://www.researching.cn/articles/OJ60ef7ae2921f02f) (no se confirmó la revista ni el año)
- Varios trabajos de SC en Si3N4 tratan el término Raman como despreciable. f_R = 0.18 corresponde a sílice y vidrio dopado, no a SiN. — resumen de búsqueda ([arXiv:2410.06817](https://arxiv.org/pdf/2410.06817), SC en sílice dopada de alto índice)
- Emisión Raman ancha en SiN en 2100–2400 cm⁻¹ con pico ~2330 cm⁻¹ (asociada a enlaces N–H/N2, no a la ganancia útil para SC) — resumen de búsqueda (Raman en guías SiN para espectroscopía)

### Inferences
- Para la GNLSE: caso base con f_R = 0 (solo Kerr instantáneo más choque óptico τ_shock = 1/ω0 y la corrección por dispersión de A_eff). Caso de sensibilidad: añadir un término Raman de primer momento con T_R = f_R·∫t h_R(t)dt ≈ 20 fs (equivalente al τ_R de Karpov), o una respuesta de tipo Lorentz con f_R pequeño ajustada para reproducir ese primer momento. Esto es una elección de modelado, no un valor medido.

### Gaps
- No encontré ninguna medición 2021–2026 del espectro de ganancia Raman g_R(Ω) ni de f_R para Si3N4 LPCVD. Tampoco encontré datos de ganancia Brillouin.

## 4. Datos de dispersión lineal: Sellmeier, dn/dT, pérdidas y bandas N–H

### Takeaway
El Sellmeier de Luke 2015 sigue siendo la referencia por defecto para Si3N4 LPCVD. Moille et al. (2021) muestran que, incluso dentro del régimen "estequiométrico", la razón NH3/DCS cambia la dispersión del material lo bastante como para mover la dispersión del resonador, así que conviene usar elipsometría de la película real. dn/dT ≈ 2.5×10⁻⁵ K⁻¹ (SiN) frente a ~1×10⁻⁵ K⁻¹ (SiO2), con ~7 % de dispersión entre telecom y visible. La pérdida limitada por el material en LPCVD es ~0.12 dB/m. Las vías de baja temperatura (PECVD deuterado, pulverizado) llegan a 1.8–6 dB/m, con un remanente N–H/Si–H hacia 1520 nm.

### Cited Findings
- Moille, Westly, Simelgor, Srinivasan, arXiv:2109.03291 (2021): la razón de precursores en LPCVD cambia significativamente la dispersión del material; la geometría puede compensarlo. — [arXiv](https://arxiv.org/abs/2109.03291)
- Ji et al. (Lipson/Gaeta), Laser Photonics Rev. 2023, doi:10.1002/lpor.202200544: SiN depositado a baja temperatura con 42 → 28 (RTA) → 6 dB/m (horno), Sellmeier por elipsometría en 200–1690 nm y 1.7–34 µm. — [arXiv:2301.03053](https://arxiv.org/abs/2301.03053)
- Índice LPCVD de 2.0115 a 632.8 nm (TE), de un Sellmeier ajustado por elipsometría — [arXiv:2406.14222](https://arxiv.org/pdf/2406.14222)
- dn/dT de Si3N4 LPCVD ≈ 2.51×10⁻⁵ K⁻¹ a 300 K (rango 300–460 K) — [NSF PAR](https://par.nsf.gov/biblio/10385367)
- TRC de Si3N4 y SiO2 con ~7 % de variación en una octava (telecom → visible). La sensibilidad térmica debida al TRC del material es 1.3 veces la debida al confinamiento modal. — [Ou, Moille, Srinivasan, arXiv:2606.05673 (2026)](https://arxiv.org/abs/2606.05673)
- Pérdida limitada por absorción del material: 0.12 ± 0.02 dB/m (Si3N4 LPCVD); el Q0 del dispositivo (30.5×10⁶) está limitado por la rugosidad. — [Gao 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9184588/)
- PECVD deuterado sin recocer: 1.77 dB/m, Q_i = 14.9×10⁶. El H residual en el SiD4 hace subir la pérdida hacia 1520 nm. — [Light Sci. Appl. 2024, s41377-024-01503-4](https://www.nature.com/articles/s41377-024-01503-4)
- SiN pulverizado a temperatura ambiente: 32 dB/m recién depositado → 5.4 dB/m tras recocer a 400 °C — [arXiv:2301.10758](https://arxiv.org/pdf/2301.10758)
- SiN deuterado de baja temperatura (pre-2021/2021): 0.17 dB/cm en 1460–1610 nm al eliminar N–H. El cladding de SiO2 deuterado reduce el sobretono SiN–H a 1520 nm de > 50 dB/m a ~1 dB/m. — [ResearchGate, Kerr combs con SiN deuterado](https://www.researchgate.net/publication/354033107_Low-noise_Kerr_frequency_comb_generation_with_low_temperature_deuterated_silicon_nitride_waveguides); [OL 45, 3340 (2020)](https://optoelectronics.ece.ucsb.edu/sites/default/files/2020-06/ol-45-12-3340.pdf)
- SRN deuterado: sustituir Si–H/N–H por Si–D/N–D desplaza los sobretonos fuera de 1.55 µm; mejora de 2 dB/cm frente a SiH4 — [Chia 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9325772/)

### Inferences
- Para el anillo/guía del proyecto con cladding de agua: el dn/dT del agua (≈ −1×10⁻⁴ K⁻¹, valor de libro, no verificado aquí) es de signo opuesto y mayor que el del SiN. Para GNLSE esto no importa, pero sí para el sensor.
- En el SC bombeado a 1550 nm, la absorción N–H a ~1520 nm (si la película no está recocida o deuterada) cae dentro del espectro generado. En una película LPCVD recocida se puede despreciar (≤ 0.1 dB/m material).

### Gaps
- No verifiqué los coeficientes de Luke 2015 contra el artículo (están transcritos de memoria). Tampoco obtuve los coeficientes Sellmeier de Moille 2021 ni los de Ji 2023 (no aparecen en los resúmenes).

## 5. γ y A_eff en guías de alto contraste: definición vectorial y ponderación de n2 entre núcleo y cladding

### Takeaway
Para núcleos de SiN sub-µm hay que usar la definición vectorial completa de Afshar & Monro (2009). Esta difiere de la escalar ∫|E|²…/∫|E|⁴ por la componente longitudinal E_z y por normalizar con el flujo de Poynting, y en guías de muy alto contraste puede dar γ hasta ~2× mayor. Con cladding de SiO2 o agua, n2 debe ponderarse campo a campo (n2 del cladding ≈ 2.2×10⁻²⁰ m²/W para SiO2, ~10× menor que el del núcleo). No encontré ningún artículo de 2021–2026 dedicado específicamente a qué definición usar en SiN.

### Cited Findings
- Modelo vectorial generalizado de propagación no lineal: la componente z de los modos es significativa, lo que lleva a definiciones generalizadas de γ, A_eff y ortogonalidad modal. γ puede ser ~2× mayor que con las definiciones estándar en guías emergentes y fibras microestructuradas. — [Afshar & Monro, Opt. Express 17, 2298 (2009), doi:10.1364/OE.17.002298; arXiv:0812.1824](https://www.arxiv.org/abs/0812.1824) [pre-2021] (OA)
- Validación experimental en fibra de núcleo suspendido de bismuto con núcleo de ~500 nm: γ medido = (5400 ± 200) W⁻¹km⁻¹, que coincide con la expresión vectorial dentro del error — [Adelaide repository](https://digital.library.adelaide.edu.au/dspace/handle/2440/56352)
- n2 de la SiO2 = 2.2×10⁻²⁰ m²/W (valor usado por Gao 2022) — [Gao 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9184588/)

### Inferences (fórmulas de trabajo para el protocolo)
- Definición vectorial (Afshar & Monro 2009), con k0 = 2π/λ:
  γ = k0 · [ ∫ n²(x,y) n2(x,y) ( 2|E|⁴ + |E·E|² ) dA ] / [ 3 Z0² · ( ∫ Re(E×H*)·ẑ dA )² ] · (factor según la normalización del artículo).
  Copiar la expresión exacta de la Ec. (37)–(40) del artículo; aquí se da solo como estructura y no se verificó término a término.
- Forma escalar habitual (Lumerical/FDE): A_eff = (∫|E|²dA)² / ∫|E|⁴dA, con γ = 2π n2,eff/(λ A_eff) y n2,eff = Σ_i n2,i ∫_i|E|⁴dA / ∫|E|⁴dA. En guías de Si3N4 de 400 nm × ~1–2 µm a 1550 nm, una fracción no despreciable del campo va al cladding, así que la ponderación baja el n2 efectivo frente a n2 del núcleo.
- Recomendación: calcular γ con ambas definiciones desde los campos FDE (E y H vectoriales) y reportar la diferencia. Con cladding de agua, usar n2(agua) ≈ 2.7×10⁻²⁰ m²/W (valor de libro, no verificado en esta sesión).

### Gaps
- No encontré artículos de 2021–2026 que comparen las definiciones de γ específicamente para SiN.

## 6. Revisiones 2021–2026 y lista corta de lectura

### Takeaway
Revisiones útiles del periodo: Xiang, Jin & Bowers (Photonics Res. 2022, OA), Buzaverov et al. (arXiv 2024, visible a MIR) y una revisión de SC en plataformas de silicio (Photonics Res. 10(3), A43, 2022, OA). No hay una revisión reciente centrada solo en los parámetros de material no lineal del SiN; la tabla de arriba la sustituye.

### Cited Findings
- Xiang, Jin, Bowers, "Silicon nitride passive and active photonic integrated circuits: trends and prospects", Photonics Res. 10(6), A82 (2022), doi:10.1364/PRJ.452936 — **OA** ([PDF](https://www.researching.cn/ArticlePdf/m00072/2022/10/6/06000A82.pdf))
- Buzaverov et al., "Silicon nitride integrated photonics from visible to mid-infrared spectra", arXiv:2405.10038 (2024), 62 pp. — **arXiv** (no se confirmó la publicación en revista) ([arXiv](https://arxiv.org/abs/2405.10038))
- Revisión de SC en Si, SiGe y SiN con elementos teóricos: Photonics Res. 10(3), A43 (2022) — **OA** ([PDF](https://www.researching.cn/ArticlePdf/m00072/2022/10/3/03000A43.pdf)) (autores y DOI no verificados; probablemente Lafforgue et al., C2N)
- "On-Chip Supercontinuum Generation Pumped by Short Wavelength Fiber Lasers", Photonics 11(5), 440 (2024), doi:10.3390/photonics11050440 — **OA**; cubre SiN, SiO2, Al2O3/AlN, TeO2, Ta2O5, TiO2, calcogenuros y LiNbO3 ([MDPI](https://mdpi.com/2304-6732/11/5/440))
- Introducción a dispositivos no lineales integrados (efectos y materiales), PMC10058895 — **OA** ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10058895/))

### Lista corta (imprescindibles, 6)
1. **Gao et al., Nat. Commun. 13, 3323 (2022)**, doi:10.1038/s41467-022-30966-5 — **OA**. Da n2 del Si3N4 LPCVD sin artefactos térmicos y la absorción del material.
2. **Tian et al., Opt. Lett. 51, 4424 (2026)**, doi:10.1364/OL.605726 — **PAY**. Da n2 en función de la estequiometría (regla de Miller).
3. **Afshar & Monro, Opt. Express 17, 2298 (2009)**, doi:10.1364/OE.17.002298 — **OA** [pre-2021]. Definición vectorial de γ y A_eff.
4. **Luke et al., Opt. Lett. 40, 4823 (2015)**, doi:10.1364/OL.40.004823 [pre-2021, DOI de memoria; verificar acceso]. Sellmeier del Si3N4. Complementar con **Moille et al., arXiv:2109.03291** (efecto de NH3/DCS en la dispersión).
5. **Xiang, Jin & Bowers, Photonics Res. 10, A82 (2022)**, doi:10.1364/PRJ.452936 — **OA**. Revisión de la plataforma.
6. **Revisión de SC en plataformas de silicio, Photonics Res. 10(3), A43 (2022)** — **OA**. Revisión con la teoría de la GNLSE aplicada a SiN. Para la parte Raman, añadir Karpov et al., PRL 116, 103902 (2016) (τ_R ≈ 20 fs).

### Gaps
- No verifiqué los DOI de: Ikeda 2008, Luke 2015, la revisión de Photonics Res. 10(3) A43 ni la lista de autores del artículo de Light Sci. Appl. 2024. Están marcados en el texto.
