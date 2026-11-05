# Apuntes del Saleh & Teich, *Fundamentals of Photonics*, 2.ª ed. (Wiley, 2007)

Lectura completa del libro (1177 páginas), capítulo por capítulo, hecha el 2026-11-05 a partir
del PDF escaneado de `bibliografia/`. El PDF **no tiene capa de texto**: se leyó renderizando
cada página como imagen. Regla de páginas: **página del PDF = página del libro + 22**.

Cada archivo `capNN-<tema>.md` contiene: mapa de secciones con páginas, resumen por sección con
las ecuaciones clave (numeradas como en el libro), definiciones, resultados destacados,
lista de problemas del capítulo y relación con el programa de Óptica No Lineal.

Convenciones del libro (válidas en todos los capítulos): unidades SI; dependencia temporal
$e^{j\omega t}$ con $j=\sqrt{-1}$, por lo que una onda que viaja en $+z$ es $e^{-jkz}$;
campos reales en caligráfica $\mathcal{E}(\mathbf r,t)$ y amplitudes complejas en negrita
$\mathbf{E}(\mathbf r)$; transformada de Fourier $F(\nu)=\int f(t)e^{-j2\pi\nu t}\,dt$.

## Mapa de capítulos

| Cap. | Título | Pág. libro | Pág. PDF | Apuntes | Programa ONL |
|---|---|---|---|---|---|
| 1 | Ray Optics | 1–37 | 23–59 | `cap01-optica-de-rayos.md` | — |
| 2 | Wave Optics | 38–73 | 60–95 | `cap02-optica-ondulatoria.md` | Tema 1 (§2.2) |
| 3 | Beam Optics | 74–101 | 96–123 | `cap03-optica-de-haces.md` | Tema 2 (§3.1) |
| 4 | Fourier Optics | 102–149 | 124–171 | `cap04-optica-de-fourier.md` | — |
| 5 | Electromagnetic Optics | 150–196 | 172–218 | `cap05-optica-electromagnetica.md` | Temas 1 y 2 (§5.1–5.6) |
| 6 | Polarization Optics | 197–242 | 219–264 | `cap06-optica-de-polarizacion.md` | Tema 3 |
| 7 | Photonic-Crystal Optics | 243–288 | 265–310 | `cap07-cristales-fotonicos.md` | — |
| 8 | Guided-Wave Optics | 289–324 | 311–346 | `cap08-optica-guiada.md` | proyecto final |
| 9 | Fiber Optics | 325–364 | 347–386 | `cap09-fibras-opticas.md` | Temas 7–8 (apoyo) |
| 10 | Resonator Optics | 365–402 | 387–424 | `cap10-resonadores.md` | proyecto final |
| 11 | Statistical Optics | 403–443 | 425–465 | `cap11-optica-estadistica.md` | — |
| 12 | Photon Optics | 444–481 | 466–503 | `cap12-optica-de-fotones.md` | — |
| 13 | Photons and Atoms | 482–531 | 504–553 | `cap13-fotones-y-atomos.md` | — |
| 14 | Laser Amplifiers | 532–566 | 554–588 | `cap14-amplificadores-laser.md` | — |
| 15 | Lasers | 567–626 | 589–648 | `cap15-laseres.md` | — |
| 16 | Semiconductor Optics | 627–679 | 649–701 | `cap16-optica-de-semiconductores.md` | — |
| 17 | Semiconductor Photon Sources | 680–747 | 702–769 | `cap17-fuentes-semiconductoras.md` | — |
| 18 | Semiconductor Photon Detectors | 748–803 | 770–825 | `cap18-detectores-semiconductores.md` | — |
| 19 | Acousto-Optics | 804–833 | 826–855 | `cap19-acustooptica.md` | — |
| 20 | Electro-Optics | 834–872 | 856–894 | `cap20-electrooptica.md` | — |
| 21 | Nonlinear Optics | 873–935 | 895–957 | `cap21-optica-no-lineal.md` | Temas 4–6, 9–10 |
| 22 | Ultrafast Optics | 936–1015 | 958–1037 | `cap22-optica-ultrarrapida.md` | Temas 7–9 |
| 23 | Optical Interconnects and Switches | 1016–1071 | 1038–1093 | `cap23-interconexiones-y-conmutadores.md` | — |
| 24 | Optical Fiber Communications | 1072–1121 | 1094–1143 | `cap24-comunicaciones-por-fibra.md` | — |
| A–C | Fourier Transform; Linear Systems; Modes of Linear Systems | 1122–1141 | 1144–1163 | `apendices.md` | apoyo |
| — | Symbols and Units | 1142–1158 | 1164–1180 | `apendices.md` | apoyo |

## Secciones de cada capítulo (del índice del libro)

- **1** 1.1 Postulates of Ray Optics (3) · 1.2 Simple Optical Components (6) · 1.3 Graded-Index Optics (17) · 1.4 Matrix Optics (24) · Problems (35)
- **2** 2.1 Postulates of Wave Optics (40) · 2.2 Monochromatic Waves (41) · *2.3 Relation Between Wave Optics and Ray Optics (49) · 2.4 Simple Optical Components (50) · 2.5 Interference (58) · 2.6 Polychromatic and Pulsed Light (66) · Problems (73)
- **3** 3.1 The Gaussian Beam (75) · 3.2 Transmission Through Optical Components (86) · 3.3 Hermite–Gaussian Beams (94) · *3.4 Laguerre–Gaussian and Bessel Beams (97) · Problems (100)
- **4** 4.1 Propagation of Light in Free Space (105) · 4.2 Optical Fourier Transform (116) · 4.3 Diffraction of Light (121) · 4.4 Image Formation (127) · 4.5 Holography (138) · Problems (147)
- **5** 5.1 Electromagnetic Theory of Light (152) · 5.2 Electromagnetic Waves in Dielectric Media (156) · 5.3 Monochromatic Electromagnetic Waves (159) · 5.4 Elementary Electromagnetic Waves (164) · 5.5 Absorption and Dispersion (170) · 5.6 Pulse Propagation in Dispersive Media (184) · *5.7 Optics of Magnetic Materials and Metamaterials (190) · Problems (195)
- **6** 6.1 Polarization of Light (199) · 6.2 Reflection and Refraction (209) · 6.3 Optics of Anisotropic Media (215) · 6.4 Optical Activity and Magneto-Optics (228) · 6.5 Optics of Liquid Crystals (232) · 6.6 Polarization Devices (235) · Problems (240)
- **7** 7.1 Optics of Dielectric Layered Media (246) · 7.2 One-Dimensional Photonic Crystals (265) · 7.3 Two- and Three-Dimensional Photonic Crystals (279) · Problems (288)
- **8** 8.1 Planar-Mirror Waveguides (291) · 8.2 Planar Dielectric Waveguides (299) · 8.3 Two-Dimensional Waveguides (308) · 8.4 Photonic-Crystal Waveguides (311) · 8.5 Optical Coupling in Waveguides (313) · 8.6 Sub-Wavelength Metal Waveguides (Plasmonics) (321) · Problems (323)
- **9** 9.1 Guided Rays (327) · 9.2 Guided Waves (331) · 9.3 Attenuation and Dispersion (348) · 9.4 Holey and Photonic-Crystal Fibers (359) · Problems (363)
- **10** 10.1 Planar-Mirror Resonators (367) · 10.2 Spherical-Mirror Resonators (378) · 10.3 Two- and Three-Dimensional Resonators (390) · 10.4 Microresonators (394) · Problems (400)
- **11** 11.1 Statistical Properties of Random Light (405) · 11.2 Interference of Partially Coherent Light (419) · *11.3 Transmission of Partially Coherent Light Through Optical Systems (427) · 11.4 Partial Polarization (436) · Problems (442)
- **12** 12.1 The Photon (446) · 12.2 Photon Streams (458) · *12.3 Quantum States of Light (471) · Problems (478)
- **13** 13.1 Energy Levels (483) · 13.2 Occupation of Energy Levels (499) · 13.3 Interactions of Photons with Atoms (501) · 13.4 Thermal Light (517) · 13.5 Luminescence and Light Scattering (522) · Problems (530)
- **14** 14.1 Theory of Laser Amplification (535) · 14.2 Amplifier Pumping (539) · 14.3 Common Laser Amplifiers (547) · 14.4 Amplifier Nonlinearity (556) · *14.5 Amplifier Noise (562) · Problems (565)
- **15** 15.1 Theory of Laser Oscillation (569) · 15.2 Characteristics of the Laser Output (575) · 15.3 Common Lasers (590) · 15.4 Pulsed Lasers (605) · Problems (624)
- **16** 16.1 Semiconductors (629) · 16.2 Interactions of Photons with Charge Carriers (660) · Problems (677)
- **17** 17.1 Light-Emitting Diodes (682) · 17.2 Semiconductor Optical Amplifiers (702) · 17.3 Laser Diodes (716) · 17.4 Quantum-Confined and Microcavity Lasers (728) · Problems (745)
- **18** 18.1 Photodetectors (749) · 18.2 Photoconductors (758) · 18.3 Photodiodes (762) · 18.4 Avalanche Photodiodes (767) · 18.5 Array Detectors (775) · 18.6 Noise in Photodetectors (777) · Problems (800)
- **19** 19.1 Interaction of Light and Sound (806) · 19.2 Acousto-Optic Devices (819) · *19.3 Acousto-Optics of Anisotropic Media (828) · Problems (832)
- **20** 20.1 Principles of Electro-Optics (836) · *20.2 Electro-Optics of Anisotropic Media (849) · 20.3 Electro-Optics of Liquid Crystals (856) · *20.4 Photorefractivity (863) · 20.5 Electroabsorption (868) · Problems (871)
- **21** 21.1 Nonlinear Optical Media (875) · 21.2 Second-Order Nonlinear Optics (879) · 21.3 Third-Order Nonlinear Optics (894) · *21.4 Second-Order Nonlinear Optics: Coupled-Wave Theory (905) · *21.5 Third-Order Nonlinear Optics: Coupled-Wave Theory (917) · *21.6 Anisotropic Nonlinear Media (924) · *21.7 Dispersive Nonlinear Media (927) · Problems (934)
- **22** 22.1 Pulse Characteristics (938) · 22.2 Pulse Shaping and Compression (946) · 22.3 Pulse Propagation in Optical Fibers (960) · 22.4 Ultrafast Linear Optics (973) · 22.5 Ultrafast Nonlinear Optics (984) · 22.6 Pulse Detection (999) · Problems (1013)
- **23** 23.1 Optical Interconnects (1018) · 23.2 Passive Optical Routers (1030) · 23.3 Photonic Switches (1038) · 23.4 Optical Gates (1058) · Problems (1071)
- **24** 24.1 Fiber-Optic Components (1074) · 24.2 Optical Fiber Communication Systems (1084) · 24.3 Modulation and Multiplexing (1101) · 24.4 Fiber-Optic Networks (1106) · 24.5 Coherent Optical Communications (1112) · Problems (1120)
- **A** A.1 One-Dimensional Fourier Transform (1122) · A.2 Time Duration and Spectral Width (1124) · A.3 Two-Dimensional Fourier Transform (1128) · **B** B.1 One-Dimensional Linear Systems (1132) · B.2 Two-Dimensional Linear Systems (1135) · **C** Modes of Linear Systems (1137) · Symbols and Units (1142)

(Las secciones marcadas con * son las de nivel avanzado según el prefacio.)

## Erratas y dudas de lectura señaladas en los apuntes

Cada archivo marca explícitamente lo que no se leyó con certeza o parece errata del libro, en vez
de corregirlo en silencio. Las más relevantes:

- Cap. 1, ec. (1.3-13): el escaneo se lee f ≈ 1/(n₀ d α sin α); lo dimensionalmente consistente es 1/(n₀ α sin αd).
- Cap. 4, p. 141: escribe U₀ = f(x/λf, y/λf) donde por contexto es F(x/λf, y/λf).
- Cap. 5: no existe problema 5.5-1 (la numeración salta de 5.4-1 a 5.5-2); el 5.5-1 es el *Exercise* del
  texto (p. 172–173), que es el que pide la Tarea 2. Las fórmulas cuantitativas del pulso gaussiano
  (z₀, τ(z), chirp) no están en el cap. 5 sino en §22.3.
- Cap. 7: p. 256 t₁t₂ = 4n₁n₂/(n₁+n₂) (falta el cuadrado); ec. (7.3-2) con x en vez de y; p. 283 G·R = 2π
  (en general múltiplo entero de 2π).
- Cap. 8: p. 311 "silica ~3.5" (es silicio); signo en (8.5-18); el problema sobre acoplamiento va numerado 8.4-1 aunque es de §8.5.
- Cap. 10, ec. (10.4-2): argumento de la Hankel impreso como nk₀r (fuera de la esfera se esperaría k₀r).
- Cap. 11: p. 430 "shift variant" (debe ser *invariant*); p. 431 remite a (11.1-36) cuando corresponde (11.3-10).
- Cap. 12, p. 473: "(12.3-9) se deriva de (12.3-9)" (debe ser de (12.3-6)).
- Cap. 21: prefactor de (21.3-21) (se lee 1/8, por consistencia debe ser ½χ⁽³⁾); exponente de ε₀ en (21.7-13);
  p. 921 "sin φ = 0, i.e. φ = π/2".
- Cap. 22: N = 3.11 del BK7 (p. 956), |z₀| = 0.5 mm (Ej. 22.3-2), 77 fs (Ej. 22.3-3), ∂²/∂x² en (22.5-35), numerador de (22.4-32).
- Cap. 23: λ_B = Λ/2 (p. 1031) y (23.2-2) sin el factor 1/√2, transcritos tal cual.
- Cap. 24: pie de la Fig. 24.1-2 (D_λ = +80 ps/km·nm en banda C) frente a 17 ps/km·nm en §24.2.
- Apéndice A, Tabla A.2-1: fila "Chirp" con F(ν) = e^{jπ/4}exp(jπt²) (debería ser exp(−jπν²)).

## Convenciones Saleh ↔ Boyd/Agrawal (resumen; detalle en `cap21-optica-no-lineal.md` y `apendices.md`)

- Tiempo: Saleh e^{jωt} (onda en +z: e^{−jkz}); Boyd/Agrawal e^{−iωt} (e^{+ikz}). Al pasar de una a otra,
  j → −i y la parte imaginaria de χ cambia de signo (Saleh: χ'' < 0 para absorción).
- Amplitudes: Saleh ℰ = Re{E e^{jωt}} ⇒ E_Saleh = 2E_Boyd (Boyd usa Ẽ = E e^{−iωt} + c.c.).
- No lineal: Saleh P_NL = 2d ℰ² + 4χ⁽³⁾ℰ³ (d en C/V², χ⁽³⁾ en C·m/V³); Boyd P = ε₀[χ⁽¹⁾E + χ⁽²⁾E² + χ⁽³⁾E³]
  (la convención del curso, CLAUDE.md). Equivalencias: d_Saleh = ε₀χ⁽²⁾_Boyd/2 = ε₀d_Boyd;
  χ⁽³⁾_Saleh = ε₀χ⁽³⁾_Boyd/4; n₂ es el mismo.
- Dispersión: Saleh D_ν = 2πβ'' (s/m·Hz), D_λ = −(λ₀/c₀)d²n/dλ₀² (ps/km·nm), z₀ = πτ₀²/D_ν = τ₀²/2β''
  con τ₀ la semianchura a 1/e de la amplitud; Agrawal β₂ = β'', L_D = T₀²/|β₂| (difieren en el factor 2 y
  en la definición del ancho).
