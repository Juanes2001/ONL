# Referencias a descargar — proyecto final (supercontinuo en SiN, Si y microanillos)

Lista única, sin duplicados, creada el 2026-11-14. Reúne:
`lectura-estado-del-arte.md` (anillos y supercontinuo de base),
`reports/Propiedades no lineales SiN y Si.md` (búsqueda nov-2021 → nov-2026) y
`referencias-no-lineal-SiN.txt`.

- **★ = prioritaria** (la lista corta: revisiones + artículos clave). Las demás son complementarias.
- Acceso: **OA** = acceso abierto · **arXiv** = versión gratuita en arXiv · **pago** = proxy de la UNAL.
- Todos los DOI están verificados en Crossref o con `scripts/verificar_referencias.py` (2026-10-30 y
  2026-11-14), salvo donde se indica.
- Los PDF van en `bibliografia/` (ignorados por git); al bajarlos, registrarlos en `bibliografia/README.md`.
- Ya en `bibliografia/`: Agrawal, *Nonlinear Fiber Optics* 4.ª ed. (supercontinuo en §12.3–12.4,
  pp. 469–495; PDF = libro + 4), Boyd 3.ª ed. y Saleh & Teich.

Resumen: 67 referencias, 22 prioritarias (★) y 45 complementarias.

---

## 0. Supercontinuo: bases (fibra → chip)

- [ ] ★ Dudley, Genty & Coen, "Supercontinuum generation in photonic crystal fiber", *Rev. Mod. Phys.* 78, 1135 (2006) — pago — https://doi.org/10.1103/RevModPhys.78.1135
- [ ] ★ Brès, Della Torre, Grassani et al., "Supercontinuum in integrated photonics: generation, applications, challenges, and perspectives", *Nanophotonics* 12, 1199 (2023) — **revisión** — OA — https://doi.org/10.1515/nanoph-2022-0749
- [ ] Skryabin & Gorbach, "Looking at a soliton through the prism of optical supercontinuum", *Rev. Mod. Phys.* 82, 1287 (2010) — pago — https://doi.org/10.1103/RevModPhys.82.1287
- [ ] Heidt, "Pulse preserving flat-top supercontinuum generation in all-normal dispersion photonic crystal fibers", *JOSA B* 27, 550 (2010) — pago — https://doi.org/10.1364/JOSAB.27.000550
- [ ] Dudley & Taylor (eds.), *Supercontinuum Generation in Optical Fibers*, Cambridge UP (2010) — libro (sin verificar)

## A. Nitruro de silicio (SiN): propiedades no lineales y supercontinuo en guía

Propiedades del material y γ
- [ ] ★ Gao et al., "Probing material absorption and optical nonlinearity of integrated photonic materials", *Nat. Commun.* 13, 3323 (2022) — OA — https://doi.org/10.1038/s41467-022-30966-5 — n₂ = 2.2×10⁻¹⁹ m²/W sin artefacto térmico
- [ ] ★ Tian et al., "Method for measuring the nonlinear index n₂ …", *Opt. Lett.* 51, 4424 (2026) — pago — https://doi.org/10.1364/OL.605726 — n₂ según la estequiometría
- [ ] ★ Afshar V. & Monro, "A full vectorial model for pulse propagation in emerging waveguides with subwavelength structures", *Opt. Express* 17, 2298 (2009) — OA — https://doi.org/10.1364/OE.17.002298 — γ y A_eff vectoriales
- [ ] Luke et al., "Broadband mid-infrared frequency comb generation in a Si₃N₄ microresonator", *Opt. Lett.* 40, 4823 (2015) — pago — https://doi.org/10.1364/OL.40.004823 — Sellmeier del Si₃N₄
- [ ] Moille et al., arXiv:2109.03291 (2021) — arXiv — https://arxiv.org/abs/2109.03291 — la estequiometría del proceso cambia la dispersión
- [ ] Ikeda et al., "Thermal and Kerr nonlinear properties of plasma-deposited silicon nitride/silicon dioxide waveguides", *Opt. Express* 16, 12987 (2008) — OA — https://doi.org/10.1364/OE.16.012987 — n₂ medido en anillos add-drop
- [ ] Moss, Morandotti, Gaeta & Lipson, "New CMOS-compatible platforms based on silicon nitride and Hydex for nonlinear optics", *Nat. Photon.* 7, 597 (2013) — **revisión** — pago — https://doi.org/10.1038/nphoton.2013.183
- [ ] Xiang, Jin & Bowers, *Photonics Res.* 10, A82 (2022) — **revisión** de SiN — OA — https://doi.org/10.1364/PRJ.452936 (DOI no re-verificado)

Supercontinuo en guías de SiN
- [ ] ★ Rebolledo-Salgado et al., "Coherent supercontinuum generation in all-normal dispersion Si₃N₄ waveguides", *Opt. Express* 30, 8641 (2022) — OA — https://doi.org/10.1364/OE.450987 — el régimen de la guía de 400 nm
- [ ] ★ Mbonde et al., "Octave-spanning supercontinuum generation in a CMOS-compatible thin Si₃N₄ waveguide coated with highly nonlinear TeO₂" (2023) — arXiv — https://arxiv.org/abs/2309.08318 — única octava en 400 nm
- [ ] ★ Wang et al., "Octave-spanning supercontinuum generation in a wafer-scale, low loss deuterated silicon nitride waveguide", *Opt. Express* 34, 20843 (2026) — OA (revista) — https://doi.org/10.1364/OE.588127
- [ ] Ren et al., "On-chip octave-spanning flat supercontinuum in all-normal-dispersion silicon nitride waveguides", *Opt. Express* 32, 8527 (2024) — OA — https://doi.org/10.1364/OE.509430
- [ ] Halir et al., "Ultrabroadband supercontinuum generation in a CMOS-compatible platform", *Opt. Lett.* 37, 1685 (2012) — pago — https://doi.org/10.1364/OL.37.001685
- [ ] Epping et al., "On-chip visible-to-infrared supercontinuum generation with more than 495 THz spectral bandwidth", *Opt. Express* 23, 19596 (2015) — OA — https://doi.org/10.1364/OE.23.019596
- [ ] Johnson et al., "Octave-spanning coherent supercontinuum generation in a silicon nitride waveguide", *Opt. Lett.* 40, 5117 (2015) — pago — https://doi.org/10.1364/OL.40.005117
- [ ] Porcel et al., "Two-octave spanning supercontinuum generation in stoichiometric silicon nitride waveguides pumped at telecom wavelengths", *Opt. Express* 25, 1542 (2017) — OA — https://doi.org/10.1364/OE.25.001542
- [ ] Grassani et al., "Mid infrared gas spectroscopy using efficient fiber laser driven photonic chip-based supercontinuum", *Nat. Commun.* 10 (2019) — OA — https://doi.org/10.1038/s41467-019-09590-3
- [ ] Zhang et al. (2025), supercontinuo de 350–3280 nm con detección f-3f en el chip — arXiv — https://arxiv.org/abs/2509.23704 (sin verificar)

## B. Silicio (Si): propiedades no lineales y supercontinuo en guía

- [ ] ★ Lafforgue et al., "Supercontinuum generation in silicon photonics platforms", *Photonics Res.* 10, A43 (2022) — **revisión** — OA — https://doi.org/10.1364/PRJ.445304
- [ ] ★ Lin, Painter & Agrawal, "Nonlinear optical phenomena in silicon waveguides: modeling and applications", *Opt. Express* 15, 16604 (2007) — OA — https://doi.org/10.1364/OE.15.016604 — GNLSE con TPA y portadores libres
- [ ] ★ Sinclair et al., "Temperature dependence of the Kerr nonlinearity and two-photon absorption in a silicon waveguide", *Phys. Rev. Applied* 11, 044084 (2019) — pago / arXiv — https://doi.org/10.1103/PhysRevApplied.11.044084 · https://arxiv.org/abs/1809.00237
- [ ] ★ T. Wang et al., "Multi-photon absorption and third-order nonlinearity in silicon at mid-infrared wavelengths", *Opt. Express* 21, 32192 (2013) — OA — https://doi.org/10.1364/OE.21.032192
- [ ] ★ Nedeljković, Soref & Mashanovich, "Free-carrier electrorefraction and electroabsorption modulation predictions for silicon over the 1–14 µm infrared wavelength range", *IEEE Photon. J.* 3, 1171 (2011) — OA — https://doi.org/10.1109/JPHOT.2011.2171930
- [ ] ★ Calcaterra et al., "Low-power supercontinuum generation in Ge-rich SiGe waveguides from 4 to 13 µm wavelength", *APL Photonics* 10, 090804 (2025) — OA — https://doi.org/10.1063/5.0270228
- [ ] ★ Cao et al., "Supercontinuum generation in a nonlinear ultra-silicon-rich nitride waveguide", *Sci. Rep.* 12 (2022) — OA — https://doi.org/10.1038/s41598-022-13734-9 — puente entre Si y SiN
- [ ] Kuyken et al., *Nat. Commun.* 6, 6310 (2015) — OA — https://doi.org/10.1038/ncomms7310 — bombeo a 2.29 µm para evitar la TPA
- [ ] Della Torre et al., *APL Photonics* 6, 016102 (2021) — OA — supercontinuo en Ge-on-Si con 3PA y FCA (DOI no re-verificado)

## C. Microanillos all-pass y add-drop: no lineal, peines y supercontinuo

Fundamentos (anillo lineal, umbral, LLE)
- [ ] ★ Kippenberg, Gaeta, Lipson & Gorodetsky, "Dissipative Kerr solitons in optical microresonators", *Science* 361, eaan8083 (2018) — **revisión** — pago — https://doi.org/10.1126/science.aan8083
- [ ] ★ Herr, Tikan & Kippenberg, "Frequency combs and coherent dissipative structures in nonlinear optical microresonators" (2026) — **revisión** — arXiv — https://arxiv.org/abs/2604.05897
- [ ] ★ Coen, Randle, Sylvestre & Erkintalo, "Modeling of octave-spanning Kerr frequency combs using a generalized mean-field Lugiato–Lefever model", *Opt. Lett.* 38, 37 (2013) — pago — https://doi.org/10.1364/OL.38.000037
- [ ] Bogaerts et al., "Silicon microring resonators", *Laser Photon. Rev.* 6, 47 (2012) — pago — https://doi.org/10.1002/lpor.201100017 — transferencia all-pass/add-drop
- [ ] Kippenberg, Spillane & Vahala, "Kerr-nonlinearity optical parametric oscillation in an ultrahigh-Q toroid microcavity", *PRL* 93, 083904 (2004) — pago — https://doi.org/10.1103/PhysRevLett.93.083904
- [ ] Haelterman, Trillo & Wabnitz, "Dissipative modulation instability in a nonlinear dispersive ring cavity", *Opt. Commun.* 91, 401 (1992) — pago — https://doi.org/10.1016/0030-4018(92)90367-Z
- [ ] Coen & Erkintalo, "Universal scaling laws of Kerr frequency combs", *Opt. Lett.* 38, 1790 (2013) — pago — https://doi.org/10.1364/OL.38.001790
- [ ] Herr et al., "Temporal solitons in optical microresonators", *Nat. Photon.* 8, 145 (2014) — pago — https://doi.org/10.1038/nphoton.2013.343

Solitón + ondas dispersivas (el "supercontinuo" del anillo)
- [ ] Brasch et al., "Photonic chip-based optical frequency comb using soliton Cherenkov radiation", *Science* 351, 357 (2016) — pago — https://doi.org/10.1126/science.aad4811
- [ ] Cherenkov, Lobanov & Gorodetsky, *PRA* 95, 033810 (2017) — pago — https://doi.org/10.1103/PhysRevA.95.033810
- [ ] Li et al., "Stably accessing octave-spanning microresonator frequency combs in the soliton regime", *Optica* 4, 193 (2017) — OA — https://doi.org/10.1364/OPTICA.4.000193
- [ ] Pfeiffer et al., "Octave-spanning dissipative Kerr soliton frequency combs in Si₃N₄ microresonators", *Optica* 4, 684 (2017) — OA — https://doi.org/10.1364/OPTICA.4.000684
- [ ] Okawachi et al., "Octave-spanning frequency comb generation in a silicon nitride chip", *Opt. Lett.* 36, 3398 (2011) — pago — https://doi.org/10.1364/OL.36.003398

SiN delgado y dispersión normal (pulsos oscuros)
- [ ] ★ Lihachev et al., "Platicon microcomb generation using laser self-injection locking", *Nat. Commun.* 13, 1771 (2022) — OA — https://doi.org/10.1038/s41467-022-29431-0
- [ ] Xue et al., "Mode-locked dark pulse Kerr combs in normal-dispersion microresonators", *Nat. Photon.* 9, 594 (2015) — pago — https://doi.org/10.1038/nphoton.2015.137
- [ ] Kim et al., "Dispersion engineering and frequency comb generation in thin silicon nitride concentric microresonators", *Nat. Commun.* 8, 372 (2017) — OA — https://doi.org/10.1038/s41467-017-00491-x
- [ ] Liu et al., *Optica* 1, 137 (2014) — OA — https://doi.org/10.1364/OPTICA.1.000137 — cruces de modos en dispersión normal
- [ ] Lobanov et al., "Frequency combs and platicons in optical microresonators with normal GVD", *Opt. Express* 23, 7713 (2015) — OA — https://doi.org/10.1364/OE.23.007713
- [ ] Kim et al., "Turn-key, high-efficiency Kerr comb source", *Opt. Lett.* 44, 4475 (2019) — pago — https://doi.org/10.1364/OL.44.004475
- [ ] Helgason et al., "Dissipative solitons in photonic molecules", *Nat. Photon.* 15, 305 (2021) — pago — https://doi.org/10.1038/s41566-020-00757-9
- [ ] Moille et al., *Laser Photon. Rev.* (2025) — pago — https://doi.org/10.1002/lpor.202401746 — SiN de 410–430 nm con cladding de aire

Bombeo pulsado y supercontinuo resonante
- [ ] ★ Anderson et al., "Photonic chip-based resonant supercontinuum via pulse-driven Kerr microresonator solitons", *Optica* 8, 771 (2021) — OA — https://doi.org/10.1364/OPTICA.403302
- [ ] Obrzud, Lecomte & Herr, "Temporal solitons in microresonators driven by optical pulses", *Nat. Photon.* 11, 600 (2017) — pago — https://doi.org/10.1038/nphoton.2017.140
- [ ] Anderson et al., "Zero dispersion Kerr solitons in optical microresonators", *Nat. Commun.* 13, 4764 (2022) — OA — https://doi.org/10.1038/s41467-022-31916-x
- [ ] Hendry et al., *PRA* 100, 023829 (2019) — pago — https://doi.org/10.1103/PhysRevA.100.023829
- [ ] Xu et al., "Frequency comb generation in a pulse-pumped normal dispersion Kerr mini-resonator", *Opt. Lett.* 46, 512 (2021) — pago — https://doi.org/10.1364/OL.413585

Add-drop, agua y sensado
- [ ] ★ P.-H. Wang et al., "Drop-port study of microresonator frequency combs", *Opt. Express* 21, 22441 (2013) — OA — https://doi.org/10.1364/OE.21.022441 (no la fe de erratas OE.22.012148)
- [ ] ★ Choi, Gin & Su, "Optical frequency combs in aqueous and air environments at visible to near-IR wavelengths", *Opt. Express* 30, 8690 (2022) — OA — https://doi.org/10.1364/OE.451631
- [ ] P.-H. Wang et al., *Opt. Express* 24, 10890 (2016) — OA — https://doi.org/10.1364/OE.24.010890 — solitón único visto por el drop
- [ ] Diakonov et al., "Broadband cavity-enhanced Kerr comb spectroscopy on chip", *npj Nanophotonics* 1, 47 (2024) — OA — https://doi.org/10.1038/s44310-024-00047-0
- [ ] Castelló-Pedrero et al., *Biomed. Opt. Express* 12, 7244 (2021) — OA — https://doi.org/10.1364/BOE.437823 — Q de un anillo de SiN en agua
- [ ] Bryan et al., *ACS Sensors* 8, 739 (2023) — pago — https://doi.org/10.1021/acssensors.2c02276
- [ ] Jin, Li & He, *Opt. Lett.* 36, 1128 (2011) — pago — https://doi.org/10.1364/OL.36.001128 — sensor Vernier con fuente ancha
- [ ] Voronkov et al., *Sensors* 22, 9553 (2022) — OA — https://doi.org/10.3390/s22239553
- [ ] Knoerzer et al., *Opt. Express* 27, 21532 (2019) — OA — https://doi.org/10.1364/OE.27.021532

---

Agua (datos para el FDE; no son artículos para leer completos): Kedenburg et al., *Opt. Mater. Express* 2, 1588 (2012), OA, https://doi.org/10.1364/OME.2.001588; tabla de Segelstein en https://omlc.org/spectra/water/data/segelstein81.txt.
