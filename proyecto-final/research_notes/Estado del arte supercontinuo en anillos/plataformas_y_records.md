# Estado del arte experimental: peines Kerr de octava / clase supercontinuo en microanillos integrados — plataformas y récords (2007 – oct. 2026)

Fecha de consulta: 2026-10-29. **Verificación de DOI:** todos los DOI de este documento se resolvieron
en la sesión mediante la API de Crossref (`api.crossref.org/works/<doi>`) y devolvieron el título y
primer autor esperados; los que no pudieron verificarse se marcan explícitamente como
"DOI sin verificar". Los preprints de arXiv sin versión de revista se marcan como "arXiv (preprint)".
Los números provienen del resumen o del texto completo de acceso abierto (Europe PMC / arXiv);
cuando un dato de geometría o Q no se pudo recuperar, se indica "(no recuperado)" y queda como
brecha, no se rellena de memoria.

Convención: FSR = rango espectral libre; Q₀ = factor de calidad intrínseco; Q_L = cargado;
D₂ = dispersión de segundo orden del resonador (D₂ > 0 anómala); OD = onda dispersiva
(Cherenkov); DKS = solitón de Kerr disipativo; SIL = auto-inyección óptica (self-injection locking);
"octava" = f_max/f_min ≥ 2.

---

## P1. Récords de ancho de banda (octava y más allá) y de umbral / potencia de bombeo mínima

### Takeaway
En Si₃N₄ la octava con solitón único se logra desde 2017 con FSR ≈ 1 THz y ~100 mW; los récords de
ancho absoluto son 1.6 octavas (137–407 THz, traslación espectral con doble bombeo, Si₃N₄,
2021) y 1.5 octavas con OD duales en AlN (2021); en umbral, AlGaAs-on-insulator (36 µW, FSR 1 THz,
Q₀ 1.5×10⁶) y Si₃N₄ ultra-baja pérdida (330 µW con Q_L 35×10⁶) marcan el estado del arte, y en 2025
un solitón visible (632–950 nm) se generó con sólo 1.1 mW en sílice.

### Cited Findings

#### Tabla 1 — Línea de tiempo de hitos de ancho de banda (orden cronológico)

| Año | Grupo | Plataforma | Geometría / FSR | Q | Dispersión / OD | Bombeo (λ, potencia) | Ancho espectral | Régimen | Fuente (DOI verificado) |
|---|---|---|---|---|---|---|---|---|---|
| 2007 | Kippenberg (MPQ) | SiO₂ microtoroide | monolítico | ultra-alto Q (sin cifra en resumen) | — | 1550 nm | 500 nm (≈70 THz) | peine paramétrico (no solitón) | [Del'Haye et al., Nature 2007](https://doi.org/10.1038/nature06401) |
| 2009/10 | Lipson/Gaeta (Cornell) | Si₃N₄ anillo | (no recuperado) | (no recuperado) | — | 1550 nm | oscilador multi-λ CMOS-compatible | peine FWM | [Levy et al., Nat. Photon. 2010](https://doi.org/10.1038/nphoton.2009.259) |
| 2009/10 | Moss/Morandotti | Hydex anillo | (no recuperado) | (no recuperado) | — | 1550 nm | oscilador hiper-paramétrico | peine FWM | [Razzari et al., Nat. Photon. 2010](https://doi.org/10.1038/nphoton.2009.236) |
| 2011 | Gaeta/Lipson | Si₃N₄ anillo | FSR 226 GHz | alto Q | — | 1562 nm | **octava**, 128 THz | peine (estado de bajo ruido, no solitón) | [Okawachi et al., Opt. Lett. 2011](https://doi.org/10.1364/OL.36.003398) |
| 2011 | Kippenberg | SiO₂ microtoroide | — | — | — | CW | **octava** 990–2170 nm, sintonizable > 1 FSR | peine (no solitón) | [Del'Haye et al., PRL 2011](https://doi.org/10.1103/PhysRevLett.107.063901) |
| 2013 | Kippenberg | MgF₂ cristalino | ∅ 700 µm, 107 GHz | Q₀ > 10⁹ (a 1.55 µm) | D₂ fuertemente anómala en MIR | 2.45 µm, ~600 mW (umbral est. 4 mW) | 200 nm (≈10 THz) a 2.5 µm | peine de bajo ruido | [Wang et al., Nat. Commun. 2013](https://doi.org/10.1038/ncomms2335) |
| 2014 | Kippenberg | MgF₂ cristalino | — | ultra-alto | anómala | 1550 nm | sech² | **primer DKS temporal en microresonador** | [Herr et al., Nat. Photon. 2014](https://doi.org/10.1038/nphoton.2013.343) |
| 2015 | Vahala (Caltech) | SiO₂ wedge | tasas de microondas | alto Q | anómala | 1550 nm | — | DKS a tasa de microondas | [Yi et al., Optica 2015](https://doi.org/10.1364/OPTICA.2.001078) |
| 2015 | Weiner/Qi (Purdue) | Si₃N₄ (dispersión normal) | — | — | **normal**, interacción de modos | 1550 nm | — | **pulsos oscuros mode-locked** | [Xue et al., Nat. Photon. 2015](https://doi.org/10.1038/nphoton.2015.137) |
| 2015 | Gaeta/Lipson | Si (SOI) | — | — | anómala > 2 µm | ~2.5 µm | 2.1–3.5 µm | peine MIR (chaótico) | [Griffith et al., Nat. Commun. 2015](https://doi.org/10.1038/ncomms7299) |
| 2016 | Kippenberg (EPFL) | Si₃N₄ (Damascene) | (no recuperado) | (no recuperado) | D₃: OD roja (Cherenkov) | CW | **2/3 de octava**, pulsos < 30 fs (6 ciclos), fase estabilizada sub-Hz | DKS único + OD | [Brasch et al., Science 2016](https://doi.org/10.1126/science.aad4811) |
| 2016 | Gaeta/Lipson | Si (SOI) | — | — | — | ~3 µm | MIR | **DKS mode-locked en Si** | [Yu et al., Optica 2016](https://doi.org/10.1364/OPTICA.3.000854) |
| 2017 | Srinivasan/Papp (NIST) | Si₃N₄ | (no recuperado) | — | OD duales | 1550 nm; **40 mW multi-solitón, ~120 mW solitón único** | **octava** | DKS, acceso por sintonía lenta (sin control rápido) | [Li et al., Optica 2017](https://doi.org/10.1364/OPTICA.4.000193) |
| 2017 | Kippenberg (EPFL) | Si₃N₄ (Damascene) | **FSR 1 THz** | κ₀/2π ≈ 100 MHz (⇒ Q₀ ≈ 1.9×10⁶ a 193 THz, inferido), finesse ≈ 10⁴ | D₄ < 0 ⇒ OD duales diseñadas en ~1 µm y ~2 µm | 1.3 µm o 1.55 µm; LLE a 75 mW | **> 1 octava** | DKS único | [Pfeiffer et al., Optica 2017](https://doi.org/10.1364/OPTICA.4.000684) |
| 2017 | Vahala | SiO₂ wedge | ∅ 3.2 mm, 20 GHz; espesor 3.4 µm (1064 nm) y 1.5 µm (778 nm) | 90×10⁶ (1064 nm), 80×10⁶ (778 nm) | TM anómala + hibridación TM1–TE2 | 1064 nm y **778 nm**; umbral 5.4 mW (778) / 2.5 mW (1550) | pulsos 44–52 fs | DKS "casi visible" | [Lee et al., Nat. Commun. 2017](https://doi.org/10.1038/s41467-017-01473-9) |
| 2017 | Vahala | SiO₂ wedge | ∅ 3 mm, 22 GHz | Q₀ ≈ 250×10⁶ | D₂/2π = 17 kHz; OD monomodo | 1550 nm | — | DKS con OD de un solo modo (estados "quietos") | [Yi et al., Nat. Commun. 2017](https://doi.org/10.1038/ncomms14869) |
| 2017 | Papp (NIST) | SiO₂ | — | — | — | — | — | **cristales de solitones** descubiertos | [Cole et al., Nat. Photon. 2017](https://doi.org/10.1038/s41566-017-0009-z) |
| 2018 | Kippenberg | Si₃N₄ (Damascene) | **1 THz, R ≈ 23 µm, 1.30 × 0.74 µm** | Q_L 0.55–0.75×10⁶ | TM₀₀ anómala a 1060 nm; OD a 800 nm | **1060 nm**, ~800 mW en chip | **octava 776–1630 nm (> 200 THz)**, 18 fs | DKS único (y cristales con η ≈ 50 %) | [Karpov et al., Nat. Commun. 2018](https://doi.org/10.1038/s41467-018-03471-x) |
| 2018 | Papp/NIST | Si₃N₄ + SiO₂ (par entrelazado) | 1 THz (periodo 1 ps) | — | OD | 1 laser | 170 THz (realzado por OD), solitones de 3 ciclos | DKS; enlace óptico-microondas | [Briles et al., Opt. Lett. 2018](https://doi.org/10.1364/OL.43.002933) |
| 2018 | Gaeta/Lipson | Si (SOI) dual-comb | R 100 µm, **127 GHz** | ~10⁵ | anómala > 3 µm | **3 µm**, 80 y 50 mW; η > 30 % | **2.6–4.1 µm**, 305 líneas | DKS mode-locked (multi-solitón) | [Yu et al., Nat. Commun. 2018](https://doi.org/10.1038/s41467-018-04350-1) |
| 2019 | Lončar (Harvard) | LiNbO₃ película delgada (x-cut, 600 nm, grabado 350 nm) | R 80 µm, 250 GHz, ancho 1.3 µm | Q₀ 1.1×10⁶ (TE), Q_L 6.6×10⁵ | anómala (requiere aire como cladding a 600 nm) | ~1556 nm, 300 mW en bus; umbral est. ~80 mW | **1400–2100 nm (> 2/3 octava)** TE; ~300 nm TM | peine Kerr (no solitón) + filtro EO | [Wang et al., Nat. Commun. 2019](https://doi.org/10.1038/s41467-019-08969-6) |
| 2019 | Vahala + Tang | LiNbO₃ | — | alto Q | — | — | — | **DKS auto-arrancado** (fotorefractivo), SHG del solitón | [He et al., Optica 2019](https://doi.org/10.1364/OPTICA.6.001138) |
| 2020 | Tang (Yale) | LiNbO₃ | **FSR hasta 335 GHz** | — | **OD duales separadas 2/3 octava** | — | **4/5 de octava** | DKS (supresión de SRS) | [Gong et al., Optica 2020](https://doi.org/10.1364/optica.400994) |
| 2020 | Xiao/Gong (Pekín) | SiO₂ microtoroide deformado | ∅ 75 µm | 1.6×10⁷ | — | 1550 nm, 1.6 W en fibra | **> 2 octavas, 450–2008 nm** (χ⁽²⁾+χ⁽³⁾, con huecos) | peine (pasos de solitón ~1 µs) | [Chen et al., Nat. Commun. 2020](https://doi.org/10.1038/s41467-020-15914-5) |
| 2020 | Bowers/Vahala (UCSB) | AlGaAs-OI (400 nm) | **R 12 µm, 1 THz**, 700 nm ancho | **Q₀ 1.53×10⁶** (0.4 dB/cm) | anómala en banda C | 1550 nm; **umbral 36 µW**; > 250 nm con 300 µW | > 250 nm | peine + paso de solitón | [Chang et al., Nat. Commun. 2020](https://doi.org/10.1038/s41467-020-15005-5) |
| 2020 | Srinivasan (NIST) | AlGaAs-OI | — | — | — | criogénico 4–20 K | — | **DKS en III-V** (apagando termo-refracción) | [Moille et al., LPR 2020](https://doi.org/10.1002/lpor.202000022) |
| 2020 | Kippenberg (EPFL) | GaP-OI | — | Q > 10⁵ (1.2 dB/cm) | diseñada | umbral **3 mW** | > 100 nm, sub-THz | peine Kerr; n₂ = 1.2×10⁻¹⁷ m²/W | [Wilson et al., Nat. Photon. 2020](https://doi.org/10.1038/s41566-019-0537-9) |
| 2021 | Tang (Yale) | **AlN** sobre zafiro | R 50 / 60 / 100 µm → **f_rep 433 / 360 / 220 GHz** | Q₀ 1–3×10⁶ | OD duales por diseño de D_int | ~1.55 µm (no recuperado) | **1.05–2.4 µm; hasta 1.5 octavas** (Δf/f₁) | DKS; **f–2f en chip con SHG de AlN** | [Liu et al., Nat. Commun. 2021](https://doi.org/10.1038/s41467-021-25751-9) |
| 2021 | Weng/Tang-colab. | AlN | FSR 374 GHz | Q_L 5×10⁵ | TE00 + TE10 casi degenerados (modo auxiliar térmico) | 340 mW en chip | **octava 1100–2300 nm** | DKS, paso de solitón récord 80 pm (10.4 GHz) | [Weng et al., Photon. Res. 2021](https://doi.org/10.1364/PRJ.427567) |
| 2021 | Srinivasan (NIST) | Si₃N₄ **775 nm (Ligentec)**, cladding SiO₂ | **R 23 µm**, ancho 1088–1140 nm, pulley 550 nm | — | "dispersión sintética" (FWM-BS) | **doble bombeo 1063 + 1557 nm** | **1.6 octavas, 137–407 THz**, 16 fs, sin huecos | DKS + traslación espectral | [Moille et al., Nat. Commun. 2021](https://doi.org/10.1038/s41467-021-27469-0) |
| 2021 | Papp/NIST + Bowers | Si₃N₄ + láser InP DFB (híbrido) | — | — | — | SIL, bombeo eléctrico, empaquetado en fibra | **octava** | DKS de octava vía SIL | [Briles et al., APL Photonics 2021](https://doi.org/10.1063/5.0035452) |
| 2021 | Papp (NIST) | Si₃N₄ **cristal fotónico (PhCR)** | — | — | defecto de D₂ en un solo modo azimutal | CW | — | **solitón espontáneo** en lugar de Turing | [Yu et al., Nat. Photon. 2021](https://doi.org/10.1038/s41566-021-00800-3) |
| 2022 | Ou/Li (Cai) | **4H-SiC-OI** | R 36 µm | Q₀ > 10⁶ | TE₀₀ por ancho | ~120 mW en chip | **octava 1100–2400 nm** | **caótico (no solitón)**; cristal de solitones en TM | [Cai et al., Photon. Res. 2022](https://doi.org/10.1364/prj.449267) |
| 2022 | Ou/Li (Wang) | 4H-SiC-OI 800 nm | microdisco R 98 µm, 208 GHz | **Q₀ 4×10⁶**, Q_L 3.1×10⁶ | TM anómala (< 1 µm espesor) | 1550 nm; umbral 12.9 mW; n₂ 6×10⁻¹⁹ | > 350 nm; traslación χ⁽²⁾ al visible (~770 nm) | **DKS único a T ambiente** | [Wang et al., Light Sci. Appl. 2022](https://doi.org/10.1038/s41377-022-01042-w) |
| 2022 | Vučković (Stanford) | 4H-SiC-OI | — | — | — | 4 K | — | DKS; óptica cuántica de peines | [Guidry et al., Nat. Photon. 2022](https://doi.org/10.1038/s41566-021-00901-z) |
| 2021 | Papp (NIST) | **Ta₂O₅** (> 800 nm, IBS) | — | **Q 3.8×10⁶** | diseñable; estrés 38 MPa | bajo umbral | "ultra-ancho" (sin cifra) | DKS; n₂ 6.2×10⁻¹⁹ (≈3× SiN) | [Jung et al., Optica 2021](https://doi.org/10.1364/OPTICA.411968) |
| 2022/23 | Xia/Zhang | **GeSbS** calcogenuro | — | **Q₀ ≈ 1.97×10⁶** | litográfica (modos TE/TM) | decenas de mW | 240 nm (1440–1680) brillante; 80 nm oscuro | DKS y pulso oscuro | [Xia et al., LPR 2023](https://doi.org/10.1002/lpor.202200219) |
| 2023 | Srinivasan/Lucas | Si₃N₄ PhCR "meta-dispersión" | — | — | **diseño inverso** (algoritmo genético + LLE) | — | peines planos / pulsos gaussianos | DKS a medida | [Lucas et al., Nat. Photon. 2023](https://doi.org/10.1038/s41566-023-01252-7) |
| 2023 | Torres-Company (Chalmers) | Si₃N₄ **anillos acoplados** 1800 × 740 nm | FSR 99.79 GHz (R 227 µm) + aux. 967 GHz; 49.85 GHz | Q₀ ≈ 14×10⁶ | β₂ = −81 ps²/km | 1565 nm | — | DKS con **η > 50 %** (vs 1–8 % típico) | [Helgason et al., Nat. Photon. 2023](https://doi.org/10.1038/s41566-023-01280-3) |
| 2023 | Srinivasan (NIST) | Si₃N₄ | — | — | OD opuesta realzada por KIS | láser de referencia inyectado | octava | **Sincronización inducida por Kerr (KIS)** pasiva | [Moille et al., Nature 2023](https://doi.org/10.1038/s41586-023-06730-0) |
| 2024 | Lončar (Harvard) | **LiNbO₃ z-cut 600 nm** | R 30–60 µm; **658.89 GHz** y **491.85 GHz** | Q₀ 1–2×10⁶ | OD duales; SRS suprimido (Γ_Raman = 558 GHz) | **363 mW** (octava 131–263 THz) / 375 mW (126–252 THz) en chip; 100 mW → 110 THz | **octava conectada** | DKS único; rendimiento 88–96 % | [Song et al., Light Sci. Appl. 2024](https://doi.org/10.1038/s41377-024-01546-7) |
| 2024 | Dong (USTC) | LiNbO₃ z-cut | — | — | OD duales | **340 mW en chip** | **octava** | DKS; f_rep medido con peine EO en TFLN | [Wang et al., Opt. Lett. 2024](https://doi.org/10.1364/ol.514893) |
| 2024 | Zhao et al. | LiNbO₃ película delgada | — | — | diseñada | — | 0.7 octava, estable > 3 h | DKS único pasivo | [Zhao et al., Chin. Opt. Lett. 2024](https://doi.org/10.3788/col202422.051301) |
| 2024 | Kippenberg (EPFL) | **LiTaO₃** (DUV, 4") | 81 GHz y 30.1 GHz | κ₀/2π 26.8 MHz (5.6 dB/m) | anómala, sin mezcla de modos 185–240 THz | 90 mW en chip | FWHM 4.9 THz, 63 fs | DKS único (material Raman-activo) | [Wang et al., Nature 2024](https://doi.org/10.1038/s41586-024-07369-1) |
| 2024 | Kippenberg/Clementi | Si₃N₄ | — | alto Q | — | **1.97 µm**, bombeo de mW | **422 nm, hasta 2.25 µm** | DKS único (doble bombeo) | [Karunakaran et al., Opt. Express 2024](https://doi.org/10.1364/oe.515225) |
| 2024 | Ou/Li | 4H-SiC-OI | 100 GHz | Q₀ hasta 5.7×10⁶ | — | **6 mW** para solitón (vía Raman) | > −20 dBm/línea | DKS | [Li et al., IEEE JSTQE 2024](https://doi.org/10.1109/jstqe.2024.3455548) |
| 2024 | Srinivasan (NIST) | Si₃N₄ | — | — | **OD sintética** por multi-bombeo | multi-color | — | KIS de color + división de frecuencia óptica | [Moille et al., Nat. Photon. 2024](https://doi.org/10.1038/s41566-024-01540-w) |
| 2025 | Srinivasan (NIST) | Si₃N₄ **air-clad** | FSR 280 GHz (según resumen de búsqueda) | — | air-clad ⇒ anómala en visible | **1060 nm → 680 nm (440 THz); 780 nm → 630 nm (475 THz)**; sim. hasta 461 nm | hasta ~220 THz | peines visibles | [Moille et al., LPR 2025](https://doi.org/10.1002/lpor.202401746) |
| 2025 | Vahala/Bowers (Caltech-UCSB) | Si₃N₄ **ULL 100 nm / 50 nm**, anillos acoplados | FSR 20/25/35/25/65 GHz a 1550/1064/780/680/532 nm; guía 3200 × 100 nm | Q₀ 47 / 28 / 31 / 9.7 / 1.4 ×10⁶ | anómala por acoplo (Moiré) hasta 532 nm | umbrales < 10 mW | **2/3 octava multiplexado (1064 + 1560 nm)** | DKS (pares de pulsos) a 1550, 1064, **780 nm** | [Liu et al., Nat. Commun. 2025](https://doi.org/10.1038/s41467-025-60157-x) |
| 2025 | Li et al. | **SiO₂ microdisco** | — | alto Q a λ corta | OD duales (D alto orden + interacción de modos) | **1.1 mW** | **632.5–950.1 nm (2/3 octava)**, OD en transición de Sr⁺ | **DKS único visible** | [Li et al., Adv. Photon. 2025](https://doi.org/10.1117/1.AP.7.5.056002) |
| 2025 | Kippenberg (EPFL) | Si₃N₄ pista (racetrack) | **15 GHz** | — | OD de alto orden | **bombeo pulsado** | **octava, ~8800 líneas** | DKS (un solo resonador) | [Davydova et al., CLEO 2025](https://doi.org/10.1364/cleo_si.2025.ss101_2); [SPIE 2026](https://doi.org/10.1117/12.3099358) |
| 2025 | Srinivasan (NIST) + AIM Photonics | Si₃N₄ **PECVD ≈ 700 nm, obleas 300 mm** | — | alto Q₀ | litográficamente sintonizable | ~1060 nm | hasta transiciones alcalinas | DKS | [Ou et al., Opt. Lett. 2025](https://doi.org/10.1364/ol.571893) |
| 2026 | Cheng et al. | 4H-SiC | 108 GHz | — | — | control de polarización dinámico | **> 450 nm** (DKS único) | DKS | [arXiv:2603.14044](https://arxiv.org/abs/2603.14044) (preprint, sin DOI de revista) |
| 2026 | (heteroestructurado, fundición comercial) | Si₃N₄ "heterostructured" | **118 GHz** | — | OD sintonizables 290–310 THz | — | **octava** a f_rep detectable | DKS | [arXiv:2608.09005](https://arxiv.org/abs/2608.09005) (preprint, sin DOI de revista) |

#### Tabla 2 — Umbrales de OPO y potencia mínima de bombeo (ordenados por umbral)

| Plataforma | Q (tipo) | FSR | Umbral OPO | Potencia para solitón | Fuente |
|---|---|---|---|---|---|
| AlGaAs-OI (400 nm) | Q₀ 1.53×10⁶ | 1 THz | **36 µW** | > 250 nm con 300 µW (no solitón) | [Chang 2020](https://doi.org/10.1038/s41467-020-15005-5) |
| Si₃N₄ 730 × 2500 nm, R 115 µm | Q₀ 37±6×10⁶, Q_L 35×10⁶ (0.8 dB/m) | — | **330 ± 70 µW** a 1557 nm; P_th ∝ 1/Q_L² confirmado | — | [Ji 2017](https://doi.org/10.1364/OPTICA.4.000619) |
| SiO₂ microdisco (visible) | alto | — | — | **1.1 mW** (solitón 632–950 nm) | [Li 2025](https://doi.org/10.1117/1.AP.7.5.056002) |
| SiO₂ wedge | 80–280×10⁶ | 20 GHz | 2.5 mW (1550), 5.4 mW (778 nm) | — | [Lee 2017](https://doi.org/10.1038/s41467-017-01473-9) |
| GaP-OI | > 10⁵ | sub-THz | 3 mW | — | [Wilson 2020](https://doi.org/10.1038/s41566-019-0537-9) |
| MgF₂ (2.5 µm) | > 10⁹ | 107 GHz | 4 mW (est.) | — | [Wang 2013](https://doi.org/10.1038/ncomms2335) |
| 4H-SiC-OI | Q₀ 5.7×10⁶ | 100 GHz | — | **6 mW** | [Li 2024](https://doi.org/10.1109/jstqe.2024.3455548) |
| Si₃N₄ Damascene (EPFL) | Q₀ 30×10⁶ (1.0 dB/m) | 40 GHz | — | **10 mW** (solitón sin EDFA) | [Liu 2021](https://doi.org/10.1038/s41467-021-21973-z) |
| Si₃N₄ ULL 100 nm acoplado | Q₀ 20–80×10⁶ | 20–35 GHz | < 10 mW (1550/1064/780 nm) | — | [Liu 2025](https://doi.org/10.1038/s41467-025-60157-x) |
| 4H-SiC-OI microdisco | Q₀ 4×10⁶ | 208 GHz | 12.9 mW | — | [Wang 2022](https://doi.org/10.1038/s41377-022-01042-w) |
| Si₃N₄ 1 THz (NIST) | — | 1 THz | — | 40 mW multi / 120 mW solitón único de octava | [Li 2017](https://doi.org/10.1364/OPTICA.4.000193) |
| LiNbO₃ 600 nm x-cut | Q₀ 1.1×10⁶ | 250 GHz | ~80 mW (estimado) | 300 mW (peine) | [Wang 2019](https://doi.org/10.1038/s41467-019-08969-6) |
| Si₃N₄ 300 nm concéntrico | Q₀ 1–2×10⁶ | 152.4 GHz | ~0.1 W (bicromático) / ~0.2 W (un bombeo) | 0.55–0.7 W | [Kim 2017](https://doi.org/10.1038/s41467-017-00491-x) |
| LiNbO₃ z-cut octava | Q₀ 1–2×10⁶ | 492–659 GHz | — | 363–375 mW (octava) | [Song 2024](https://doi.org/10.1038/s41377-024-01546-7) |

- Fórmula de umbral citada en Chang 2020: P_th ≈ 1.54·(π/2)·(1/η)·(n/(n₂ ω))·(D₁ A/Q_T²), con η = κ_e/κ, A área modal, Q_T Q total; para AlGaAs (n = 2.9, A = 0.28 µm²) el umbral es ~270× menor que un diseño estándar de Si₃N₄ a igual Q — [Chang et al. 2020](https://doi.org/10.1038/s41467-020-15005-5).
- Ji 2017 (texto arXiv): pérdida limitada por absorción del film 0.13 ± 0.05 dB/m ⇒ Q limitado por absorción ≥ 170×10⁶; rugosidad RMS reducida de 0.38 a 0.08 nm por CMP; anillo de 10 µm de ancho alcanzó Q₀ 67 ± 7×10⁶ — [Ji et al. 2017](https://doi.org/10.1364/OPTICA.4.000619).
- Liu 2021: Q limitado por absorción > 2×10⁸; espiral de 1 m con 2.4 dB/m; umbral de solitón escala como 1/Q² — [Liu et al. 2021](https://doi.org/10.1038/s41467-021-21973-z).

### Inferences
- Para una octava con solitón único en Si₃N₄ el "sweet spot" experimental sigue siendo FSR ≈ 1 THz (R ≈ 23 µm) con h ≈ 0.74–0.8 µm y ~100 mW; bajar la f_rep a valores detectables (15–118 GHz) exige bombeo pulsado (Davydova 2025) o gestión de dispersión por heteroestructura (arXiv 2608.09005).
- El récord de ancho "sin huecos" (1.6 octavas) no viene de dispersión sola sino de doble bombeo (FWM-BS); los > 2 octavas de Chen 2020 incluyen armónicos χ⁽²⁾ con huecos y no son metrológicos.
- Q₀ ≈ 1.9×10⁶ para Pfeiffer 2017 es un cálculo propio a partir de κ₀/2π ≈ 100 MHz a 193 THz.

### Gaps
- Geometría (R, W×H), Q y potencia de Brasch 2016 no se recuperaron (PDF arXiv no extraíble; Science sin resumen numérico).
- Yu 2016 (Optica, DKS MIR en Si): sólo se verificó el DOI; no se obtuvieron cifras.
- Detalles numéricos de Gong 2020 más allá de 4/5 octava y 335 GHz (Q, potencia) no recuperados.
- Hausmann 2014 (diamante): DOI verificado, sin cifras recuperadas.
- No se encontró ningún microcomb integrado de solitón único que supere 1 octava **sin** segundo bombeo o χ⁽²⁾ entre 2024 y oct-2026 más allá de los listados (AlN 1.5 octavas de 2021 sigue siendo el mayor Δf/f₁ con un solo bombeo).

---

## P2. Restricción espesor/dispersión en Si₃N₄: cuán delgado puede ser el film y qué trucos se usan

### Takeaway
Con geometría rectangular convencional, la dispersión anómala a 1550 nm en Si₃N₄ requiere espesor
≳ 600–700 nm (las fundiciones típicas ofrecen < 400 nm y el LPCVD agrieta por encima de ~500 nm);
los trucos demostrados son anillos concéntricos/pistas acopladas (300 nm, Kim 2017), anillos
acoplados ULL de 100 nm y 50 nm (Liu 2025), modos de orden superior (Zhao 2020), modo TM
(Karpov 2018 a 1 µm), cristales fotónicos en el anillo (PhCR) y, alternativamente, aceptar
dispersión normal y usar pulsos oscuros/platicones.

### Cited Findings

#### Tabla 3 — Espesor de Si₃N₄ usado en demostraciones de peines y forma de obtener dispersión anómala

| Espesor | Sección (W×H) | Cómo se obtiene D₂ > 0 | Proceso | Resultado | Fuente |
|---|---|---|---|---|---|
| 1.35 µm | — | geometría (núcleo grueso) | **Damascene fotónico** (topografía de sustrato para estrés, sin grietas, rendimiento ≈ 1) | Q 3.7×10⁶, DKS único | [Pfeiffer 2016](https://doi.org/10.1364/OPTICA.3.000020) |
| film LPCVD 1000 nm → guía 950 nm | 2200 × 950 nm | geometría | Damascene + DUV 248 nm + relleno anti-grietas + recocido 1200 °C; rendimiento sin grietas 100 % (> 30 obleas) | Q₀ 30×10⁶ medio; solitón 40 GHz con 10 mW | [Liu 2021](https://doi.org/10.1038/s41467-021-21973-z) |
| > 800 nm | — | geometría | fundición 6" (Qaleido), 2.6 dB/m, rendimiento ≈ 100 % | solitones de bajo umbral | [Ye 2023](https://doi.org/10.1364/PRJ.486379) |
| 800 nm | 1600 × 800 nm, R 75 µm | geometría; D₂/2π ≈ 9 MHz | PhCR + SIL | DKS 300 GHz, Q 1.5×10⁶, estabilizado en fase | [Wildi 2024](https://doi.org/10.1038/s41467-024-50842-8) |
| 0.8 µm | 1.55 × 0.8 µm, R 228 µm | geometría | — | DKS 100 GHz, Q₀ 4.3×10⁶ (OFD) | [Sun 2024](https://doi.org/10.1038/s41586-024-07057-0) |
| 775 nm | ancho 1088–1140 nm, R 23 µm | geometría + dispersión sintética | **Ligentec** | 1.6 octavas | [Moille 2021](https://doi.org/10.1038/s41467-021-27469-0) |
| 750 ± 20 nm | — | geometría, D₂/2π ≈ 1.56 MHz (92.4 GHz) | Damascene reflow, CMP | DKS por SIL, < 1 W eléctrico | [Raja 2019](https://doi.org/10.1038/s41467-019-08498-2) |
| 740 nm | 1.30 × 0.74 µm, R 23 µm | **modo TM₀₀** (TE normal) a 1060 nm | Damascene | octava 776–1630 nm | [Karpov 2018](https://doi.org/10.1038/s41467-018-03471-x) |
| 740 nm | 1800 × 740 nm | geometría (β₂ = −81 ps²/km) + anillo auxiliar | subtractivo Chalmers | η > 50 % | [Helgason 2023](https://doi.org/10.1038/s41566-023-01280-3) |
| 730 nm | 2500 × 730 nm, R 115 µm | geometría | subtractivo con CMP + litografía multipaso + HTO 500 nm + PECVD | Q₀ 37×10⁶, umbral 330 µW | [Ji 2017](https://doi.org/10.1364/OPTICA.4.000619) |
| ≈ 700 nm (PECVD) | — | geometría, litográficamente sintonizable | **AIM Photonics, obleas 300 mm**, variación ±2 % | DKS hasta λ alcalinas | [Ou 2025](https://doi.org/10.1364/ol.571893) |
| 530 nm | 2.00 µm × 530 nm, R 900 µm | **no**: dispersión normal → platicón | — | platicón 26.2 GHz, Q₀ 10⁷, η 40 % | [Lihachev 2022](https://doi.org/10.1038/s41467-022-29431-0) |
| **300 nm** | w_in 2750 / w_out 1200 nm, gap 900 nm, R 50 µm, L_st 300 µm | **pista concéntrica**: acoplo resonante simétrico/antisimétrico; TE₁ normal −1200 ps/nm/km convertido en anómalo local | LPCVD 300 nm + LTO 3 µm | Q₀ 1–2×10⁶, peine mode-locked 152.4 GHz, ~180 nm | [Kim 2017](https://doi.org/10.1038/s41467-017-00491-x) |
| **100 nm (NIR) y 50 nm (visible)** | 3200 × 100 nm | **anillos acoplados** (dispersión de acoplo, efecto Moiré) | fundición CMOS ULL | DKS a 1550/1064/780 nm; anómala hasta 532 nm | [Liu 2025](https://doi.org/10.1038/s41467-025-60157-x) |
| delgado (alto aspecto) | — | **no** (SIL relaja requisito de dispersión) | fundición CMOS | Q > 260×10⁶, peine con requisitos de dispersión relajados | [Jin 2021](https://doi.org/10.1038/s41566-021-00761-7) |
| — | — | **modos de orden superior** | — | peine mode-locked casi-visible | [Zhao 2020](https://doi.org/10.1364/optica.7.000135) |
| — | — | **PhCR** (defecto de D₂ monomodo / meta-dispersión / síntesis de Fourier) | NIST | solitón espontáneo; peines a medida | [Yu 2021](https://doi.org/10.1038/s41566-021-00800-3); [Lucas 2023](https://doi.org/10.1038/s41566-023-01252-7); [Moille 2023](https://doi.org/10.1038/s42005-023-01253-6) |

- "Las guías de núcleo delgado (h < 100 nm) ... no son adecuadas para fotónica no lineal; sólo recientemente guías de núcleo grueso (h > 700 nm) ... han sido demostradas" — [Liu et al. 2021](https://doi.org/10.1038/s41467-021-21973-z).
- "La GVD anómala exige espesor de Si₃N₄ > 600 nm en bandas de telecomunicación ... con LPCVD aparecen grietas por encima de 500 nm ... la mayoría de fundiciones comerciales ofrecen LPCVD < 400 nm" — [Lihachev et al. 2022](https://doi.org/10.1038/s41467-022-29431-0).
- Luke 2013: trincheras mecánicas aíslan las grietas en films de alto estrés; Q₀ 7×10⁶ (4.2 dB/m), el más alto de alto confinamiento a 1550 nm en 2013 — [Luke et al. 2013](https://doi.org/10.1364/OE.21.022829).
- Reflow Damascene: Q medio > 5×10⁶ en guías de confinamiento fuerte con dispersión anómala — [Pfeiffer et al. 2018](https://doi.org/10.1364/OPTICA.5.000884) (resumen arXiv 1802.08315).
- Subtractivo Chalmers: Q₀ medio ≈ 11×10⁶; dispersión normal o anómala por geometría; pulsos oscuros y solitones de 100 GHz — [Ye et al. 2019](https://doi.org/10.1364/OE.27.035719).
- Purdue "finger-shaped": Q₀ hasta 17×10⁶ a FSR 24.7 GHz con iniciación de peine a baja potencia — [Xuan et al. 2016](https://doi.org/10.1364/OPTICA.3.001171).
- Liu 2025: las guías ULL de alto Q usan Si₃N₄ "típicamente de 100 nm o menos", lo que produce dispersión normal incluso en telecom; se resolvió con anillos acoplados — [Liu et al. 2025](https://doi.org/10.1038/s41467-025-60157-x).
- Sílice (referencia): a 778 nm la GVD de SiO₂ es 38 ps²/km, > 5× menor que la de Si₃N₄ (> 200 ps²/km) — [Lee et al. 2017](https://doi.org/10.1038/s41467-017-01473-9).
- Dispersión normal como alternativa: pulsos oscuros mode-locked en Si₃N₄ de dispersión normal por interacción de modos — [Xue et al. 2015](https://doi.org/10.1038/nphoton.2015.137).

### Inferences
- No se encontró ninguna demostración con film "≈ 400 nm" rectangular simple con D₂ > 0 a 1550 nm; el récord de delgadez con dispersión anómala efectiva es 300 nm (acoplo resonante) y, por acoplo de anillos, 100/50 nm — en todos los casos la anomalía es "de acoplo" (localizada en ancho de banda) y no de guía.
- Para el proyecto (plataforma de ~400 nm de fundición), las rutas realistas son (i) anillos acoplados/concéntricos, (ii) pulsos oscuros/platicones con SIL, o (iii) modo TM / modos superiores; una octava con un solo bombeo no está demostrada en < 700 nm.

### Gaps
- No se recuperó el espesor exacto de Jin 2021 (texto parcial); se infiere "delgado de alto aspecto" por el propio artículo y por Liu 2025 (≤ 100 nm).
- Luke 2013: espesor del film no recuperado del resumen.

---

## P3. Frontera 2023–2026: diseño inverso, traslación espectral, KIS, anillos acoplados, visible/UV, 2 µm y MIR, peines turnkey con láser integrado, > 1 octava

### Takeaway
La frontera reciente se mueve de "más ancho" a "más controlable y más barato": sincronización
Kerr pasiva a una referencia (KIS, 2023/2024), eficiencia > 50 % con anillos acoplados (2023),
peines visibles por air-clad y anillos ULL acoplados (2025), solitones a 2 µm en Si₃N₄ (2024),
octava en LiNbO₃ con rendimiento ≈ 90 % (2024), LiTaO₃ (2024), turnkey a < 10 GHz en obleas de
4" (2025) y octava a 15–118 GHz (2025–2026); ningún trabajo integrado supera 1.6 octavas sin
segundo bombeo.

### Cited Findings

#### Tabla 4 — Resultados 2020–2026 que empujan la frontera (por tema)

| Tema | Año | Resultado clave | Fuente |
|---|---|---|---|
| Turnkey con láser | 2018 | Si₃N₄ + láser integrado en doble cavidad; 194 GHz; **98 mW eléctricos** | [Stern et al., Nature 2018](https://doi.org/10.1038/s41586-018-0598-9) |
| Turnkey con láser | 2019 | Diodo InP FP + Si₃N₄ Damascene (Q₀ > 10⁷), SIL; FSR 149 y 92.4 GHz; < 1 W eléctrico, ~1 cm³ | [Raja et al., Nat. Commun. 2019](https://doi.org/10.1038/s41467-019-08498-2) |
| Turnkey con láser | 2020 | Régimen "turnkey": solitón al encender; **15 GHz** en paquete butterfly | [Shen et al., Nature 2020](https://doi.org/10.1038/s41586-020-2358-x) |
| Turnkey con láser | 2021 | Láser InP/Si + Si₃N₄ **heterogéneo en una oblea de Si**; solitón único 100 GHz; miles de dispositivos/oblea | [Xiang et al., Science 2021](https://doi.org/10.1126/science.abh2076) |
| Turnkey + octava | 2021 | DFB InP híbrido + SiN, SIL, octava, empaquetado en fibra; retro-dispersión acopla fuertemente la sintonía | [Briles et al., APL Photon. 2021](https://doi.org/10.1063/5.0035452) |
| Platicón SIL | 2022 | DFB + Si₃N₄ normal (530 nm), 26.2 GHz, η 40 %, Q₀ 10⁷ | [Lihachev et al., Nat. Commun. 2022](https://doi.org/10.1038/s41467-022-29431-0) |
| SIL estabilizado | 2024 | Microcomb SIL con **estabilización de fase completa** (f_off y f_rep) con < 1.57 V, > 100 kHz; PhCR 300 GHz, 25 mW en chip | [Wildi et al., Nat. Commun. 2024](https://doi.org/10.1038/s41467-024-50842-8) |
| OFD integrado | 2024 | Cavidad de bobina Si₃N₄ 6 µm × 80 nm (Q₀ 41×10⁶) + DKS 100 GHz (Q₀ 4.3×10⁶): **−114 dBc/Hz @ 10 kHz a 100 GHz** | [Sun et al., Nature 2024](https://doi.org/10.1038/s41586-024-07057-0) |
| Turnkey a tasa microondas | 2025 | Obleas 4", geometrías dedo/espiral, **Q > 10⁷, f_rep < 10 GHz turnkey**, −130 dBc/Hz @ 100 kHz (10 GHz) | [Wang et al., LPR 2025](https://doi.org/10.1002/lpor.202501659) |
| Más allá del límite turnkey | 2026 | Anillo auxiliar hibrida el modo de bombeo: 25 GHz, BW 3 dB 17.1 → 26.8 nm manteniendo SIL | [Wang et al., PRL 2026](https://doi.org/10.1103/r8fh-vtps) |
| Diseño inverso | 2023 | Meta-dispersión en PhCR por algoritmo genético + LLE; división de modos programable | [Lucas et al., Nat. Photon. 2023](https://doi.org/10.1038/s41566-023-01252-7) |
| Diseño de dispersión | 2023 | Síntesis de Fourier de PhCR (TM) para corrimientos modo a modo | [Moille et al., Commun. Phys. 2023](https://doi.org/10.1038/s42005-023-01253-6) |
| Traslación espectral | 2021 | 1.6 octavas (137–407 THz) con doble bombeo | [Moille et al., Nat. Commun. 2021](https://doi.org/10.1038/s41467-021-27469-0) |
| KIS | 2023 | Sincronización pasiva de DKS a un láser de referencia; control directo de f_rep; OD opuesta realzada en DKS de octava | [Moille et al., Nature 2023](https://doi.org/10.1038/s41586-023-06730-0) |
| KIS de color | 2024 | OD sintética por multi-bombeo permite KIS en modos arbitrarios; OFD desacoplada del bombeo principal | [Moille et al., Nat. Photon. 2024](https://doi.org/10.1038/s41566-024-01540-w) |
| Anillos acoplados / eficiencia | 2021 | "Moléculas fotónicas": DKS en anillos acoplados | [Helgason et al., Nat. Photon. 2021](https://doi.org/10.1038/s41566-020-00757-9) |
| Anillos acoplados / eficiencia | 2023 | η > 50 % (anómalo + anillo auxiliar que desplaza una resonancia) | [Helgason et al., Nat. Photon. 2023](https://doi.org/10.1038/s41566-023-01280-3) |
| Cristales de solitones | 2019 | Generación determinista de cristales perfectos (potencia crítica) | [Karpov et al., Nat. Phys. 2019](https://doi.org/10.1038/s41567-019-0635-0) |
| Cristales de solitones (Hydex) | 2020 | 3 × 2 µm, R ≈ 592 µm, 48.9 GHz, Q > 1.5×10⁶, 1.8 W, > 80 nm, η 42 %; **44.2 Tb/s** | [Corcoran et al., Nat. Commun. 2020](https://doi.org/10.1038/s41467-020-16265-x) |
| Visible | 2017 | DKS a 778 nm en sílice (Q 80×10⁶) | [Lee et al., Nat. Commun. 2017](https://doi.org/10.1038/s41467-017-01473-9) |
| Visible | 2018 | Octava 776–1630 nm bombeando a 1060 nm (Si₃N₄, TM) | [Karpov et al., Nat. Commun. 2018](https://doi.org/10.1038/s41467-018-03471-x) |
| Visible | 2020 | Modos de orden superior en Si₃N₄: peine casi-visible + pares de fotones en Rb | [Zhao et al., Optica 2020](https://doi.org/10.1364/optica.7.000135) |
| Visible | 2025 | Air-clad Si₃N₄: 1060 → 680 nm; 780 → 630 nm; sim. 461 nm | [Moille et al., LPR 2025](https://doi.org/10.1002/lpor.202401746) |
| Visible | 2025 | ULL 50/100 nm acoplado: DKS a 780 nm, anómalo hasta 532 nm | [Liu et al., Nat. Commun. 2025](https://doi.org/10.1038/s41467-025-60157-x) |
| Visible | 2025 | **DKS único 632.5–950.1 nm** en microdisco de sílice con 1.1 mW; OD en Sr⁺ | [Li et al., Adv. Photon. 2025](https://doi.org/10.1117/1.AP.7.5.056002) |
| 2 µm | 2024 | Si₃N₄, bombeo 1.97 µm, 422 nm hasta 2.25 µm, mW | [Karunakaran et al., Opt. Express 2024](https://doi.org/10.1364/oe.515225) |
| MIR | 2015 | Si₃N₄ 2.3–3.5 µm, Q 1.0×10⁶ (ciclos depósito-recocido) | [Luke et al., Opt. Lett. 2015](https://doi.org/10.1364/OL.40.004823) |
| MIR | 2018 | Si dual-comb 2.6–4.1 µm, 127 GHz | [Yu et al., Nat. Commun. 2018](https://doi.org/10.1038/s41467-018-04350-1) |
| MIR (simulación) | 2024 | Calcogenuro GeSbSe, anillo doble concéntrico con slot, bombeo 2 µm 60 mW: solitón de dos colores **1156–5055 nm (200 THz) — numérico (LLE), no experimental** | [Cheng et al., Front. Optoelectron. 2024](https://doi.org/10.1007/s12200-024-00139-x) |
| Octava a f_rep detectable | 2025 | Si₃N₄ pista, **15 GHz, ~8800 líneas**, bombeo pulsado | [Davydova et al., CLEO 2025](https://doi.org/10.1364/cleo_si.2025.ss101_2) |
| Octava a f_rep detectable | 2026 | Heteroestructura Si₃N₄ (fundición comercial), **118 GHz**, OD 290–310 THz | [arXiv:2608.09005](https://arxiv.org/abs/2608.09005) (preprint) |
| Octava LiNbO₃ | 2024 | 658.89 GHz, 131–263 THz, 363 mW; rendimiento 88–96 % | [Song et al., LSA 2024](https://doi.org/10.1038/s41377-024-01546-7) |
| LiTaO₃ | 2024 | DKS 81 y 30.1 GHz, 90 mW, 63 fs | [Wang et al., Nature 2024](https://doi.org/10.1038/s41586-024-07369-1) |
| SiC | 2026 | DKS único 108 GHz, > 450 nm | [arXiv:2603.14044](https://arxiv.org/abs/2603.14044) (preprint) |
| Pulsos como bombeo (contexto) | 2017 | DKS en microresonadores bombeados por pulsos | [Obrzud et al., Nat. Photon. 2017](https://doi.org/10.1038/nphoton.2017.140) |

- Reseñas de referencia (DOI verificados): [Kippenberg et al., Science 2018](https://doi.org/10.1126/science.aan8083); [Gaeta, Lipson, Kippenberg, Nat. Photon. 2019](https://doi.org/10.1038/s41566-019-0358-x); [Chang, Liu, Kippenberg, Nat. Photon. 2022](https://doi.org/10.1038/s41566-021-00945-1); [Pasquazi et al., Phys. Rep. 2018](https://doi.org/10.1016/j.physrep.2017.08.004); [Moss et al., Nat. Photon. 2013 (Hydex/SiN)](https://doi.org/10.1038/nphoton.2013.183); [Sun et al., Adv. Opt. Photon. 2023](https://doi.org/10.1364/AOP.470264); [Shekhar et al., Nat. Commun. 2024](https://doi.org/10.1038/s41467-024-44750-0); [Ji et al., APL Photonics 2021 (tutorial de Q ultra-alto en SiN)](https://doi.org/10.1063/5.0057881); [Lu et al., Nat. Photon. 2024 (láseres integrados visibles)](https://doi.org/10.1038/s41566-024-01529-5).
- Sistemas: sintetizador óptico integrado [Spencer et al., Nature 2018](https://doi.org/10.1038/s41586-018-0065-7); reloj con par de peines Kerr (22 GHz) [Newman et al., Optica 2019](https://doi.org/10.1364/OPTICA.6.000680); 50 Tb/s con dos DKS [Marin-Palomo et al., Nature 2017](https://doi.org/10.1038/nature22387); Q 422×10⁶ en Si₃N₄ delgado (no peine) [Puckett et al., Nat. Commun. 2021](https://doi.org/10.1038/s41467-021-21205-4).

### Inferences
- "Visible" hoy significa 630–680 nm por OD en Si₃N₄ air-clad y 632 nm con solitón único en sílice; nadie ha reportado solitón integrado en Si₃N₄ bombeado por debajo de 780 nm.
- El multi-octava de Cheng 2024 es sólo simulación; el único > 2 octavas experimental (Chen 2020) depende de χ⁽²⁾ en sílice deformada.

### Gaps
- No se encontró un peine integrado de solitón que alcance el UV; el 461 nm de Moille 2025 es simulado.
- No se halló evidencia de peines de octava con láser heterogéneo totalmente integrado y auto-referenciado (f–2f) en chip en 2024–2026, salvo el f–2f en chip de AlN (2021) y las propuestas en LiNbO₃.

---

## P4. Plataformas compatibles con fundición (Ligentec, LioniX TriPleX, ANT, imec, CNM, Tower, AIM) y espesores demostrados con peines

### Takeaway
Hay demostraciones verificadas con chips de Ligentec (775 nm, Moille 2021; AN800 en otros
trabajos), LioniX TriPleX (peine de solitón bombeado por ECL híbrido, Maier 2023), fundición
CMOS ULL de Si₃N₄ delgado (≤ 100 nm, Jin 2021 / Liu 2025), AIM Photonics (PECVD ≈ 700 nm,
obleas 300 mm, Ou 2025) y una fundición de 6" con > 800 nm (Ye 2023); no se encontró evidencia de
peines Kerr en ANT (400 nm), imec BioPIX ni CNM.

### Cited Findings

| Fundición / proceso | Espesor Si₃N₄ | Demostración de peine | Fuente |
|---|---|---|---|
| **Ligentec SA** | 775 nm (anillos R 23 µm), cladding SiO₂ | 1.6 octavas por traslación espectral (NIST) | [Moille et al. 2021](https://doi.org/10.1038/s41467-021-27469-0) |
| Ligentec (lista de publicaciones del fabricante) | "AN800" (800 nm) citado en varios trabajos no-peine | Página lista como hechos con su tecnología: KIS [Moille 2023](https://doi.org/10.1038/s41586-023-06730-0), OFD [Sun 2024](https://doi.org/10.1038/s41586-024-07057-0), DKS de octava por modo dual [Weng et al., APL Photon. 2022](https://doi.org/10.1063/5.0089036) | [Ligentec, publicaciones](https://www.ligentec.com/technology/publications-using-our-technology/) |
| **LioniX TriPleX** | no indicado en la nota | Primer DKS único bombeado por ECL híbrido (SOA InP + Si₃N₄ TriPleX + photonic wire bonds; 12 dBm, 90 nm de sintonía, 979 Hz) — KIT | [Maier et al., J. Lightwave Technol. 2023](https://doi.org/10.1109/JLT.2023.3243471); [nota LioniX](https://www.lionix-international.com/about-us/news/integrated-tunable-laser-generates-kerr-frequency-comb-for-the-first-time/) |
| **Fundición CMOS (ULL, Si₃N₄ delgado)** | "≤ 100 nm típico"; 100 nm (NIR) y 50 nm (visible) como espesores estándar | Q > 260×10⁶ y peine con requisitos de dispersión relajados; DKS a 1550/1064/780 nm en anillos acoplados | [Jin et al. 2021](https://doi.org/10.1038/s41566-021-00761-7); [Liu et al. 2025](https://doi.org/10.1038/s41467-025-60157-x) |
| **AIM Photonics (300 mm, PECVD)** | ≈ 700 nm, ±2 % | DKS de banda ancha hasta λ de alcalinos | [Ou et al. 2025](https://doi.org/10.1364/ol.571893) |
| Fundición 6" (proceso estándar) | > 800 nm, 2.6 dB/m | solitones de bajo umbral | [Ye et al. 2023](https://doi.org/10.1364/PRJ.486379) |
| Proceso de oblea 4" (Damascene, DUV) | 950 nm | solitón 40 GHz con 10 mW; rendimiento 89 % | [Liu et al. 2021](https://doi.org/10.1038/s41467-021-21973-z) |
| Obleas 4" (turnkey microondas) | — | Q > 10⁷, turnkey < 10 GHz | [Wang et al. 2025](https://doi.org/10.1002/lpor.202501659) |
| Fundición comercial (no nombrada) | heteroestructura | octava a 118 GHz | [arXiv:2608.09005](https://arxiv.org/abs/2608.09005) |
| Heterogéneo InP/Si + Si₃N₄ en oblea de Si (UCSB) | — | DKS 100 GHz con láser integrado | [Xiang et al. 2021](https://doi.org/10.1126/science.abh2076) |
| Fundición CMOS (300 nm LPCVD, Purdue) | 300 nm | peine mode-locked en pista concéntrica ("más amigable que 700–1000 nm para fundición CMOS") | [Kim et al. 2017](https://doi.org/10.1038/s41467-017-00491-x) |

- Lihachev 2022: "la mayoría de los procesos comerciales de fundición de Si₃N₄ ofrecen LPCVD < 400 nm", por lo que proponen platicones (dispersión normal) como ruta de fundición — [Lihachev et al. 2022](https://doi.org/10.1038/s41467-022-29431-0).

### Inferences
- Para una fundición de 400 nm (tipo ANT) no hay precedente publicado de peine Kerr; los precedentes más cercanos son 300 nm (Purdue, concéntrico) y 530 nm (EPFL, platicón) — ambos en procesos propios, no de fundición abierta.

### Gaps
- **Applied Nanotools (ANT)**: ninguna búsqueda devolvió un peine Kerr en su plataforma de 400 nm.
- **imec (BioPIX) y IMB-CNM**: ninguna demostración de peine encontrada.
- El espesor TriPleX usado en Maier 2023 no está en la nota de LioniX (el artículo JLT no se consultó).
- "Tower Semiconductor" no aparece nombrado en los resúmenes verificados; Jin 2021 sólo dice "fundición CMOS".

---

## Anexo — DOI que resultaron erróneos en esta sesión (para no repetirlos)
10.1038/s41467-018-07016-0 (no es de peines: artículo de inmunología); 10.1364/OPTICA.393810,
10.1364/OPTICA.384282, 10.1364/OPTICA.510427, 10.1021/acsphotonics.8b00219,
10.1038/s41377-022-00868-5, 10.1038/s41377-024-01622-2, 10.1038/s41467-020-18654-y,
10.1038/s41586-021-03624-5 (no resuelven en Crossref). Los correctos son: Gong 2020 =
10.1364/optica.400994; Zhao 2020 = 10.1364/optica.7.000135; Liu (AlN) 2018 =
[10.1021/acsphotonics.7b01254](https://doi.org/10.1021/acsphotonics.7b01254) (ACS Photonics, "Integrated High-Q Crystalline AlN
Microresonators for Broadband Kerr and Raman Frequency Combs", verificado; cifras no recuperadas).
