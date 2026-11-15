# Lista de lectura — estado del arte: no lineal y supercontinuo en microanillos (all-pass y add-drop)

> La lista unificada de descargas (anillos + SiN + Si) está en `referencias-a-descargar.md` (2026-11-14). Este archivo queda como guía de lectura por bloques.

Creada el 2026-11-12 a partir de `reports/Estado del arte supercontinuo en anillos.md` (118 refs)
y `reports/Simulación no lineal anillos add drop.md` (51 refs). Los DOI de esos informes se
verificaron el 2026-10-30 con `scripts/verificar_referencias.py`. Las marcadas con † (Bloque 1)
o ‡ (Bloque 0) se añadieron aquí y no han pasado por el verificador.

Acceso: **OA** = acceso abierto (Optica, Opt. Express, Nat. Commun., Sci. Adv., arXiv);
el resto se descarga por el proxy de la UNAL o desde su versión en arXiv.
Los PDF van en `bibliografia/` (ignorados por git) y se registran en `bibliografia/README.md`.

## Bloque 0 — Supercontinuo desde cero (fibra → guía en chip)

Agrawal, *Nonlinear Fiber Optics*, 4.ª ed. (en `bibliografia/`; página del PDF = página del libro + 4,
comprobado el 2026-11-12):
- [ ] Requisitos previos: §2.3, ecuación de propagación (GNLSE), p. 31; §3.3, dispersión de tercer orden, p. 62;
      §4.1–4.2, SPM y SPM con GVD, pp. 79 y 89; §5.2, solitones, p. 129; §5.5, efectos de orden superior
      (TOD, self-steepening, Raman), pp. 156–167.
- [ ] §11.1, parámetro no lineal γ y A_eff, p. 424 (lo que en chip sale del FDE).
- [ ] **§12.3, Supercontinuum Generation, pp. 469–477** (bombeo de ps, CW y fs).
- [ ] **§12.4, Temporal and Spectral Evolution, pp. 477–495**: 12.4.1 modelado numérico (p. 477), 12.4.2 fisión
      de solitones y radiación no solitónica (p. 480), 12.4.5 coherencia (p. 492).

Revisiones y artículos de supercontinuo en chip:
- [ ] Dudley, Genty & Coen, RMP 78, 1135 (2006). DOI 10.1103/RevModPhys.78.1135 — la revisión canónica (también en el Bloque 2).
- [ ] ‡Dudley & Taylor (eds.), *Supercontinuum Generation in Optical Fibers*, Cambridge UP (2010) — libro de consulta.
- [ ] ‡Heidt, JOSA B 27, 550 (2010) — supercontinuo coherente con dispersión totalmente normal (SPM + rompimiento de onda), que es el régimen de la guía de 400 nm.
- [ ] Halir et al., Opt. Lett. 37, 1685 (2012). DOI 10.1364/OL.37.001685 — primer supercontinuo en SiN, 665–2025 nm.
- [ ] Epping et al., Opt. Express 23, 19596 (2015). DOI 10.1364/OE.23.019596 **OA** — supercontinuo en SiN de 470 a 2130 nm.
- [ ] Johnson et al., Opt. Lett. 40, 5117 (2015). DOI 10.1364/OL.40.005117 — supercontinuo coherente de una octava en SiN.
- [ ] Porcel et al., Opt. Express 25, 1542 (2017). DOI 10.1364/OE.25.001542 **OA** — dos octavas en SiN bombeando a 1.56 µm (guía de 900 nm de espesor).
- [ ] **Rebolledo-Salgado et al., Opt. Express 30, 8641 (2022). DOI 10.1364/OE.450987 OA — supercontinuo coherente en Si₃N₄ con dispersión totalmente normal: el más cercano a la guía de 400 nm.**
- [ ] Ren et al., Opt. Express 32 (2024). DOI 10.1364/OE.509430 **OA** — supercontinuo plano en guía de SiN con dispersión totalmente normal.
- [ ] Grassani et al., Nat. Commun. 10 (2019). DOI 10.1038/s41467-019-09590-3 **OA** — supercontinuo en SiN en el IR medio, bombeado con láser de fibra.

‡ = citada de memoria el 2026-11-12, **sin DOI y sin verificar**; pasarla por `scripts/verificar_referencias.py` antes de citarla. Las demás de este bloque están verificadas en `referencias-no-lineal-SiN.txt` (búsqueda del 2026-10-04).

## Bloque 1 — Fundamentos: anillo lineal, umbral y LLE (leer primero)

- [ ] †Bogaerts et al., "Silicon microring resonators", Laser Photon. Rev. 6, 47 (2012). DOI 10.1002/lpor.201100017 — funciones de transferencia all-pass/add-drop, Q, FSR, acoplo crítico.
- [ ] †Kippenberg, Spillane & Vahala, "Kerr-nonlinearity optical parametric oscillation in an ultrahigh-Q toroid microcavity", PRL 93, 083904 (2004). DOI 10.1103/PhysRevLett.93.083904 — umbral paramétrico P_th ∝ 1/Q².
- [ ] Haelterman, Trillo & Wabnitz, Opt. Commun. 91, 401 (1992). DOI 10.1016/0030-4018(92)90367-Z — MI en cavidad anular (origen de la LLE en óptica).
- [ ] Coen, Randle, Sylvestre & Erkintalo, Opt. Lett. 38, 37 (2013). DOI 10.1364/OL.38.000037 — LLE generalizada para peines de octava (el modelo que vamos a programar).
- [ ] Coen & Erkintalo, Opt. Lett. 38, 1790 (2013). DOI 10.1364/OL.38.001790 — leyes de escala del ancho del peine.
- [ ] Herr et al., Nat. Photon. 8, 145 (2014). DOI 10.1038/nphoton.2013.343 — solitones disipativos (DKS) en microrresonadores.
- [ ] Kippenberg, Gaeta, Lipson & Gorodetsky, Science 361, eaan8083 (2018). DOI 10.1126/science.aan8083 — revisión de referencia.
- [ ] Herr, Tikan & Kippenberg, arXiv:2604.05897 (2026) **OA** — revisión más reciente (70 pp.); sirve de mapa.

## Bloque 2 — "Supercontinuo" en el anillo = solitón + ondas dispersivas

- [ ] Dudley, Genty & Coen, RMP 78, 1135 (2006). DOI 10.1103/RevModPhys.78.1135 — supercontinuo en fibra (conecta con Agrawal).
- [ ] Skryabin & Gorbach, RMP 82, 1287 (2010). DOI 10.1103/RevModPhys.82.1287 — radiación Cherenkov del solitón.
- [ ] Brasch et al., Science 351, 357 (2016). DOI 10.1126/science.aad4811 — DKS con onda dispersiva en Si₃N₄.
- [ ] Cherenkov, Lobanov & Gorodetsky, PRA 95, 033810 (2017). DOI 10.1103/PhysRevA.95.033810 — teoría de la onda dispersiva con D₃.
- [ ] Li et al., Optica 4, 193 (2017). DOI 10.1364/OPTICA.4.000193 **OA** — octava en Si₃N₄, acceso térmico.
- [ ] Pfeiffer et al., Optica 4, 684 (2017). DOI 10.1364/OPTICA.4.000684 **OA** — octava con D₄ < 0 y dos ondas dispersivas.
- [ ] Okawachi et al., Opt. Lett. 36, 3398 (2011). DOI 10.1364/OL.36.003398 — primera octava (MI, incoherente).

## Bloque 3 — Si₃N₄ delgado y dispersión normal (el caso de la guía de 400 nm)

- [ ] Kim et al., Nat. Commun. 8, 372 (2017). DOI 10.1038/s41467-017-00491-x **OA** — SiN de 300 nm, anillos concéntricos.
- [ ] Xue et al., Nat. Photon. 9, 594 (2015). DOI 10.1038/nphoton.2015.137 — pulsos oscuros en dispersión normal.
- [ ] Liu et al., Optica 1, 137 (2014). DOI 10.1364/OPTICA.1.000137 **OA** — los cruces de modos cambian el signo local de la dispersión.
- [ ] Lobanov et al., Opt. Express 23, 7713 (2015). DOI 10.1364/OE.23.007713 **OA** — platicones (teoría).
- [ ] Kim et al., Opt. Lett. 44, 4475 (2019). DOI 10.1364/OL.44.004475 — fuente turn-key con anillos acoplados, 40 % de eficiencia.
- [ ] Lihachev et al., Nat. Commun. 13, 1771 (2022). DOI 10.1038/s41467-022-29431-0 **OA** — platicones con self-injection locking.
- [ ] Helgason et al., Nat. Photon. 15, 305 (2021). DOI 10.1038/s41566-020-00757-9 — moléculas fotónicas.
- [ ] Moille et al., Laser Photon. Rev. (2025). DOI 10.1002/lpor.202401746 — SiN de 410–430 nm con cladding de aire.
- [ ] Luke et al., Opt. Lett. 40, 4823 (2015). DOI 10.1364/OL.40.004823 — Sellmeier del Si₃N₄ (lo usa `paso01`).
- [ ] Ren et al., Opt. Express 32 (2024). DOI 10.1364/OE.509430 **OA** — supercontinuo plano en guía de SiN all-normal (referencia para la GNLSE).

## Bloque 4 — Bombeo pulsado y "supercontinuo resonante"

- [ ] Obrzud, Lecomte & Herr, Nat. Photon. 11, 600 (2017). DOI 10.1038/nphoton.2017.140
- [ ] Anderson et al., Optica 8, 771 (2021). DOI 10.1364/OPTICA.403302 **OA** — término "resonant supercontinuum".
- [ ] Anderson et al., Nat. Commun. 13, 4764 (2022). DOI 10.1038/s41467-022-31916-x **OA** — solitones a dispersión cero.
- [ ] Hendry et al., PRA 100, 023829 (2019). DOI 10.1103/PhysRevA.100.023829 — LLE con bombeo pulsado y desincronización.
- [ ] Xu et al., Opt. Lett. 46, 512 (2021). DOI 10.1364/OL.413585 — bombeo pulsado en dispersión normal.

## Bloque 5 — Add-drop, Kerr en SiN, agua y sensado

- [ ] Wang et al., Opt. Express 21, 22441 (2013). DOI 10.1364/OE.21.022441 **OA** — peines vistos por el puerto drop (no la DOI de la fe de erratas, OE.22.012148).
- [ ] Wang et al., Opt. Express 24, 10890 (2016). DOI 10.1364/OE.24.010890 **OA** — solitón único dentro de la cavidad, visto por el drop.
- [ ] Ikeda et al., Opt. Express 16, 12987 (2008). DOI 10.1364/OE.16.012987 **OA** — n₂ de SiN medido en anillos add-drop.
- [ ] Choi, Gin & Su, Opt. Express 30, 8690 (2022). DOI 10.1364/OE.451631 **OA** — el único peine generado dentro de agua.
- [ ] Diakonov et al., npj Nanophotonics 1, 47 (2024). DOI 10.1038/s44310-024-00047-0 **OA** — peine + anillo objetivo (precedente más cercano).
- [ ] Castelló-Pedrero et al., Biomed. Opt. Express 12, 7244 (2021). DOI 10.1364/BOE.437823 **OA** — Q de un anillo SiN en agua a 1550 y 1310 nm.
- [ ] Bryan et al., ACS Sensors 8, 739 (2023). DOI 10.1021/acssensors.2c02276 — Q ≈ 1.3×10⁴ en agua.
- [ ] Jin, Li & He, Opt. Lett. 36, 1128 (2011). DOI 10.1364/OL.36.001128 — sensor Vernier de doble anillo con fuente de banda ancha.
- [ ] Voronkov et al., Sensors 22, 9553 (2022). DOI 10.3390/s22239553 **OA** — sistema add-drop + interrogador para refractometría.
- [ ] Knoerzer et al., Opt. Express 27, 21532 (2019). DOI 10.1364/OE.27.021532 **OA** — interrogación de un sensor de índice con un peine.

Las demás referencias (umbrales récord, fundiciones, aplicaciones dual-comb, Raman) están en
la bibliografía completa de los informes; se consultan cuando el texto lo pida.
