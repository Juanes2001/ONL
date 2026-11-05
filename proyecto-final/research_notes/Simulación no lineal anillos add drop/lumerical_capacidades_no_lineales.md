# Capacidades de Ansys Lumerical para óptica no lineal de tercer orden (χ⁽³⁾/Kerr) en microanillos

Investigación del 2026-10-26. Fuente principal: la Knowledge Base oficial `optics.ansys.com`, consultada por su API
Zendesk (`/api/v2/help_center/...`) porque las páginas HTML devuelven 403 a clientes automáticos. Las fechas
"creado/actualizado" provienen de esa API. Versiones del usuario: **v202 = 2020 R2** (local) y **v261 = 2026 R1** (cluster).

## 1. FDTD / varFDTD: modelos de material no lineal, unidades, límites y ejemplos oficiales

### Takeaway
FDTD y el varFDTD (2.5D) de MODE traen cuatro modelos χ⁽³⁾ de fábrica: "Chi3/Chi2", "Chi3 Raman Kerr" (plugin, admite
material base dispersivo), "Kerr nonlinear" (no es plugin, no admite base) y "Chi2". χ⁽³⁾ se ingresa en m²/V² (no n₂) y la
amplitud de la fuente en V/m. Hay ejemplos oficiales de biestabilidad en un anillo (2D) y de FWM en un anillo (varFDTD),
pero con χ⁽³⁾ inflado a propósito y anillos de Q bajo. Ansys reconoce que el FDTD 3D directo de anillos grandes no es
práctico. FDTD en GPU no admite estos materiales.

### Cited Findings
**Modelos de material (página "Advanced and custom optical material models in FDTD and MODE")**
- Lista oficial de modelos avanzados, implementados en su mayoría con el *Flexible material plugin framework* e incluidos en la instalación estándar de FDTD y MODE: Chi2, Chi3/Chi2, Chi3 Raman Kerr, Four-Level Two-Electron, Kerr nonlinear, Paramagnetic, Magnetic Electric Lorentz, Index Perturbation; como plugins con código fuente: Lorentz example, Two-level one-electron, Step index, Chi 2 anisotropic. — [Advanced and custom optical material models](https://optics.ansys.com/hc/en-us/articles/360034394734-Advanced-and-custom-optical-material-models-in-FDTD-and-MODE)
- **"Chi3/Chi2"**: parámetros χ⁽¹⁾ [adimensional], χ⁽²⁾ [m/V], χ⁽³⁾ [m²/V²], con material base dispersivo opcional (la polarización no lineal se suma a la del base). Su ejemplo enlazado es *Optical bistability*. Código fuente: chi3.h/chi3.cpp. Advertencia: "Some artificial asymmetry can be introduced by the algorithm." — [misma página](https://optics.ansys.com/hc/en-us/articles/360034394734-Advanced-and-custom-optical-material-models-in-FDTD-and-MODE)
- **"Chi3 Raman Kerr"**: P(t) = ε₀χ⁽¹⁾E + ε₀αχ₀⁽³⁾E³ + ε₀(1−α)E(χ_Raman⁽³⁾(t) ∗ E²), con χ_Raman⁽³⁾(ω) lorentziano. Parámetros: χ⁽¹⁾, χ⁽³⁾ [m²/V²], α ∈ [0,1] (peso Kerr/Raman), ω_Raman [Hz], δ_Raman [Hz]. Admite material base (dispersión lineal). Implementado según Goorjian y Taflove (Opt. Lett. 1992). — [misma página](https://optics.ansys.com/hc/en-us/articles/360034394734-Advanced-and-custom-optical-material-models-in-FDTD-and-MODE)
- **"Kerr nonlinear"**: P = ε₀(χ⁽¹⁾ + χ⁽³⁾|E(t)|²)E(t); parámetros ε_r y χ⁽³⁾ [m²/V²]. "This material model does not support the option to select a base material"; el mallado y el Material Explorer suponen n = 1. "This is not a plugin material." — [misma página](https://optics.ansys.com/hc/en-us/articles/360034394734-Advanced-and-custom-optical-material-models-in-FDTD-and-MODE)
- Para todos estos materiales, el mallado automático usa solo el índice del *Base Material* (o n = 1 si no hay base), así que hay que forzar mesh override. El Material Explorer no muestra sus propiedades. — [misma página](https://optics.ansys.com/hc/en-us/articles/360034394734-Advanced-and-custom-optical-material-models-in-FDTD-and-MODE)
- El conformal mesh no se aplica a los materiales plugin (caen en staircasing) salvo que se active "revert to base material for conformal mesh cells". — [Nonlinear and gain methodology](https://optics.ansys.com/hc/en-us/articles/360041727474-Nonlinear-and-gain-methodology)
- Con el *Flexible Material Plugin Framework* se escriben modelos propios en C++. Ansys advierte que el soporte técnico no cubre desarrollar ni depurar modelos propios y que la documentación "may be incomplete". — [Flexible Material Plugin Framework](https://optics.ansys.com/hc/en-us/articles/360034915213-Flexible-Material-Plugin-Framework)
- Conversión según Lumerical (página del efecto Kerr): n₂ = ½·χ⁽³⁾/n₀²·√(μ₀/ε₀), con I = n₀√(ε₀/μ₀)|E|². Ejemplo: n₂ = 6×3e-16 cm²/W y n₀ = 1.455 dan χ⁽³⁾ = 2.0e-21 m²/V²; amplitud de fuente 1e9 V/m. — [Kerr effect on Gaussian beam propagation](https://optics.ansys.com/hc/en-us/articles/360041718634-Kerr-effect-on-Gaussian-beam-propagation)

**Estabilidad, fuentes y monitores (metodología oficial)**
- Estabilidad: se exige χ⁽³⁾E² ≪ χ⁽¹⁾. Ejemplo: E ~ 1e9 V/m con χ⁽³⁾ ~ 5e-18 da χ⁽³⁾E² ~ 5, inestable; con E = 1e7 V/m da ~5e-4. La amplitud se fija en "General" de la fuente, en V/m. — [Nonlinear and gain methodology](https://optics.ansys.com/hc/en-us/articles/360041727474-Nonlinear-and-gain-methodology)
- La CW normalization supone un sistema lineal y no vale en simulaciones no lineales: hay que usar `nonorm` e integrar el vector de Poynting a mano (la página trae el script). `transmission()` divide por la potencia de la fuente y falla fuera de su espectro. Otros puntos: desactivar "use source limits" en los monitores, revisar el muestreo de los time monitors (aliasing de armónicos), usar "set simulation bandwidth" en Advanced, y probar convergencia también en dt. — [Nonlinear and gain methodology](https://optics.ansys.com/hc/en-us/articles/360041727474-Nonlinear-and-gain-methodology)
- FDTD GPU no admite "Other advanced permittivity models" ni materiales del Flexible Material Plugin Framework (da error). Los checkpoints tampoco funcionan en GPU. — [Getting started with running FDTD on GPU](https://optics.ansys.com/hc/en-us/articles/17518942465811-Getting-started-with-running-FDTD-on-GPU)

**Ejemplos oficiales χ⁽³⁾ en FDTD/varFDTD** (lista madre: [Nonlinear optics - list of examples](https://optics.ansys.com/hc/en-us/articles/360043165194-Nonlinear-optics-list-of-examples))
- **Ring resonator – optical bistability**: racetrack plasmónico metal-dieléctrico-metal en FDTD 2D ("or MODE 2.5D FDTD Propagator") con material "Kerr" del tipo Chi3/Chi2. El χ⁽³⁾ es 10 veces el de la referencia "so that the field intensity required to observe the bistability effect is smaller". Fuente CW personalizada (`setsourcesignal`) desintonizada de la resonancia, con rampa de intensidad de subida (forward.fsp) y de bajada (reverse.fsp) de 15500 fs. Archivos: forward.fsp, reverse.fsp, set_source.lsf, bistability_results.lsf. Lazos a 1578, 1580 y 1582 nm. — [Ring resonator - optical bistability](https://optics.ansys.com/hc/en-us/articles/360041723954-Ring-resonator-optical-bistability)
- **Four wave mixing (varFDTD)**: anillo SOI con bus through/drop, es decir add-drop (basado en Koos et al., IEEE JQE 2006), material "Raman Kerr" con base "Si (Silicon) - Palik" y conformal revert. Fuentes de modo pump (1.534 µm) y signal (1.561 µm); onda convertida en ≈1.508 µm. Simulación de 50000 fs, ancho de banda fijado en 1.45–1.6 µm, mesh overrides en los gaps, PML "stabilized" en x (con la estándar diverge). Archivos: ring_resonator_FWM.lms, ring_resonator_linear.lsf, ring_nonlinear_FWM.lsf. Advierte que el χ⁽³⁾ "is more for demonstration purpose". — [Four wave mixing (varFDTD)](https://optics.ansys.com/hc/en-us/articles/360041718794-Four-wave-mixing-varFDTD)
- **Four wave mixing with Kerr nonlinear material**: medio en bloque (no guía), χ⁽³⁾ = 3e-18, tres ondas planas a 100, 120 y 140 THz; muestra el tercer armónico (THG) con una sola fuente y los productos de mezcla con las tres. Script fourwave.lsf. — [FWM with Kerr nonlinear material](https://optics.ansys.com/hc/en-us/articles/360041718694-Four-wave-mixing-with-Kerr-nonlinear-material)
- **Kerr effect on Gaussian beam propagation**: autoenfoque en un vidrio en 3D, kerr1_linear.fsp, kerr1_nonlinear.fsp y kerr1.lsf. — [enlace](https://optics.ansys.com/hc/en-us/articles/360041718634-Kerr-effect-on-Gaussian-beam-propagation)
- **Soliton propagation in a homogeneous medium** (1D con el propagador 2.5D de MODE, base Lorentz + Chi3 Raman Kerr). — [enlace](https://optics.ansys.com/hc/en-us/articles/360041718614-Soliton-propagation-in-a-homogeneous-medium). **Soliton in an SOI waveguide**: el GVD sale de FDE (waveguide_neff_sweep.lms, D_to_GVD.lsf); n_eff(λ) se exporta como material "Sampled data" "TM_like_neff" y se usa como base de "Chi3 Raman Kerr" en varFDTD 1D. Es el truco oficial para meter la dispersión de la guía en el modelo temporal. — [enlace](https://optics.ansys.com/hc/en-us/articles/360042190173-Soliton-in-an-SOI-waveguide)
- Otros ejemplos de la familia: *Spatial soliton in a graphene-embedded waveguide*, [enlace](https://optics.ansys.com/hc/en-us/articles/360042732313-Spatial-soliton-in-a-graphene-embedded-waveguide); *Harmonic generation with a chi2 material* (SHG, χ⁽²⁾), [enlace](https://optics.ansys.com/hc/en-us/articles/360042190413-Harmonic-generation-with-a-chi2-material).
- Postura oficial sobre anillos: "Direct simulation of large rings using 3D FDTD is not practical due to the large memory and time requirements, although it may be possible for some small rings." — [SFWM Microring Resonator Photon Source](https://optics.ansys.com/hc/en-us/articles/15100783091731-Spontaneous-Four-Wave-Mixing-SFWM-Microring-Resonator-Photon-Source)
- Foro (Ansys Learning Forum, respuestas de empleados; no es documentación oficial y solo se vio el fragmento del buscador, porque el foro redirige al pedirlo directamente):
  - Un empleado dijo que Chi3/Chi2 "needs non-zero chi2" y que para χ⁽³⁾ puro se use el modelo Kerr. Esto **contradice** el ejemplo oficial de biestabilidad, que usa Chi3/Chi2 para Kerr puro.
  - Solo algunos modelos no lineales admiten dispersión.
  - "FDTD cannot simulate non-3*3 diagonal tensor nonlinear material."
  - Un usuario con un anillo en varFDTD y χ⁽³⁾ = 1e-18 no vio efecto hasta subirlo a 1e-6; la respuesta fue que la intensidad de campo era demasiado baja.
  - Fuentes: [hilo 295376](https://innovationspace.ansys.com/forum/?p=295376), [367386](https://innovationspace.ansys.com/forum/?p=367386), [422961](https://innovationspace.ansys.com/forum/?p=422961).

### Inferences
- **Factor 3/2 en la conversión n₂ ↔ χ⁽³⁾.** Los modelos Chi3/Chi2 y Chi3 Raman Kerr usan P = ε₀χ⁽³⁾E³ con campo real. Para una onda CW, esa forma da n₂ = 3χ⁽³⁾/(4n₀²ε₀c), que es la convención de Boyd y la del curso. La fórmula de la página del efecto Kerr, n₂ = χ⁽³⁾Z₀/(2n₀²), sale de usar |E|² instantáneo y da un χ⁽³⁾ 1.5 veces mayor. Para Si₃N₄ con n₂ ≈ 2.4e-19 m²/W (valor de literatura no verificado en esta búsqueda) y n₀ ≈ 1.99, Boyd da χ⁽³⁾ ≈ 3.4e-21 m²/V² y la fórmula de la página da ≈ 5.0e-21 m²/V². **Recomendación:** calibrar con una guía recta corta en varFDTD, midiendo la fase no lineal frente a la potencia antes de confiar en cualquiera de las dos.
- **Coste de un anillo de alto Q.** El tiempo de vida del fotón es τ = Qλ/(2πc): ≈8 ps para Q = 1e4, ≈82 ps para 1e5 y ≈0.82 ns para 1e6. Un barrido de biestabilidad necesita rampas mucho más largas que τ; el ejemplo oficial usa 15.5 ps con un racetrack plasmónico de Q muy bajo. En FDTD 3D eso son millones a decenas de millones de pasos (dt ~ 0.05 fs) sobre un anillo de decenas de µm, lo que no cabe en los 7.4 GB locales. En varFDTD puede llegar a ser viable para Q ≲ 1e4, con χ⁽³⁾ o potencia inflados como hace Ansys. La generación de un peine de Kerr (≫1000 τ, soliton step) queda fuera del alcance práctico de FDTD/varFDTD.
- Como "Kerr nonlinear" no admite material base, ignora la dispersión del Si₃N₄. Para un anillo de SiN conviene "Chi3 Raman Kerr" con α = 1 (solo Kerr) y base Si₃N₄, o "Chi3/Chi2" con base.

### Gaps
- No hay ejemplo oficial de SPM en guía integrada con FDTD, de peine de Kerr ni de THG en guía o anillo de SiN.
- No se pudo leer el foro completo (redirige) para confirmar en contexto la afirmación "Chi3/Chi2 needs non-zero chi2".
- No se encontró documentación oficial de qué versión introdujo cada modelo. Los ejemplos de biestabilidad y FWM figuran como creados en 2020-01-22 al migrar la KB, así que existen al menos desde 2020a y deberían estar en v202, pero no está verificado archivo por archivo.

## 2. MODE (FDE/EME/varFDTD): dispersión, A_eff, γ y propagación no lineal

### Takeaway
FDE es la herramienta oficial para el lado lineal del flujo no lineal. Da n_eff, n_g, D (dispersión) y A_eff (definición
de Agrawal) por modo y en barrido de frecuencia, y lo exporta a INTERCONNECT. γ = n₂ω₀/(cA_eff) se calcula a mano en un
script; no hay un resultado "γ" nativo. MODE no tiene un solver NLSE propio y EME es lineal. La única propagación no
lineal dentro de MODE es el varFDTD (2.5D FDTD Propagator) con materiales χ⁽³⁾.

### Cited Findings
- La Mode List de FDE reporta n_eff, loss, **effective area** y TE fraction. A_eff sigue la definición de Agrawal (*Nonlinear Fiber Optics*, 4.ª ed.): A_eff = (∫|E|²dA)²/∫|E|⁴dA. Los resultados de la frequency analysis quedan en el grupo "data" del Eigenmode Solver. — [FDE solver analysis - Mode List and Deck](https://optics.ansys.com/hc/en-us/articles/360034396734)
- La pestaña "Frequency analysis" calcula loss, n_eff, velocidad de grupo y **dispersión** en un rango de frecuencias. Recomendaciones: usar el ajuste *Multi-Coefficient Model* (con datos muestreados aparecen picos espurios en D) y activar "detailed dispersion calculation" (más lento y más exacto). Archivo: waveguide_dispersion.lms. — [Dispersion analysis of SOI waveguide](https://optics.ansys.com/hc/en-us/articles/360042304954-Dispersion-analysis-of-SOI-waveguide)
- La alternativa por script es sweep_frequency_dispersion.lsf, con un "sweep" sobre frecuencia, seguimiento de modo por overlap con la d-card y posibilidad de distribuir. — [Sweep analysis for dispersion calculations](https://optics.ansys.com/hc/en-us/articles/1500006208582-Sweep-analysis-for-dispersion-calculations)
- Otra definición de área, por energía (Landau-Lifshitz), en un analysis group de FDTD: usr_effective_mode_area.fsp. — [Calculating the effective mode area of a waveguide mode](https://optics.ansys.com/hc/en-us/articles/360034395354-Calculating-the-effective-mode-area-of-a-waveguide-mode)
- **Ejemplo oficial con γ, MODE → INTERCONNECT**, *Supercontinuum generation in photonic crystal fiber* (creado 2024-03-21):
  1. PCF.lms + Design.lsf barren el pitch para fijar el ZDW cerca de 835 nm.
  2. Dispersion_export.lsf calcula A_eff, n_g, D y la pendiente de D (ventana ±5 nm) y los exporta.
  3. nonlinear_NLSE.icp + nonlinear_NLSE.lsf cargan esos datos en el elemento **NLSE Waveguide**: n₂ = 2.7e-20 m²/W, sech de 50.1 fs FWHM, 10 kW de pico; el espectro sale de ≈580 a >1150 nm.

  El texto define γ = n₂ω₀/(cA_eff). — [Supercontinuum generation in photonic crystal fiber](https://optics.ansys.com/hc/en-us/articles/27638850917267-Supercontinuum-generation-in-photonic-crystal-fiber)
- **SFWM en microanillo de Si₃N₄** (MODE + FDTD + INTERCONNECT + qINTERCONNECT):
  - FDTD solo para el acoplador (coupler_region.fsp, coupling_coefficient_step1.lsf).
  - FDE para la guía recta y la curva (waveguide.lms, botón "Export for INTERCONNECT", archivos straight_wg.ldf y bent_wg.ldf).
  - INTERCONNECT para el racetrack y el Q (ring_resonator.icp, ring_resonator_step3.lsf).
  - mode_area_step4.lsf calcula el área de traslape de cuatro ondas A_eff = 1/∬u_p u_p u_s* u_i* (resultado 0.59 µm² frente a 0.5 µm² de la referencia).
  - generate_biphoton_wavefunction_mrr.py calcula la tasa de pares.
  - Advierte que "it can be difficult to achieve phase matching with a high-Q cavity".

  — [SFWM Microring Resonator Photon Source](https://optics.ansys.com/hc/en-us/articles/15100783091731-Spontaneous-Four-Wave-Mixing-SFWM-Microring-Resonator-Photon-Source)
- El ejemplo de solitón SOI usa FDE → D_to_GVD.lsf para el GVD y luego varFDTD no lineal. — [Soliton in an SOI waveguide](https://optics.ansys.com/hc/en-us/articles/360042190173-Soliton-in-an-SOI-waveguide)
- En 2022 R1.2 el solver FEEM pasó a reportar el "effective area" de los modos. — [2022 R1.2 Release Notes](https://optics.ansys.com/hc/en-us/articles/5218682727827-2022-R1-2-Release-Notes)
- Las búsquedas en la KB de "Lugiato" y "microcomb" dieron 0 artículos. — API de búsqueda de optics.ansys.com (consulta `search.json?query=Lugiato` / `microcomb`, 2026-10-26).

### Inferences
- Flujo nativo recomendado para el anillo de SiN de 400 nm:
  1. FDE con el modo TE₀ en guía recta y en guía curva ("bent waveguide", radio R).
  2. Frequency analysis en 1.2–2.0 µm para n_eff(λ), n_g, D y la pendiente de D, y de ahí β₂ = −λ²D/(2πc) y D_int(μ) (por script).
  3. A_eff de la Mode List y γ = n₂ω₀/(cA_eff), calculado en un .lsf o en Python.
  4. Export a INTERCONNECT (.ldf).

  Los pasos 1–3 funcionan en v202.
- Para estudiar peines de Kerr, el reparto realista es: Lumerical FDE da D_int, γ, FSR y κ (estos dos con FDTD o EME), y un solver LLE externo en Python resuelve la dinámica. Ese acoplamiento no tiene ejemplo oficial de Ansys.

### Gaps
- No se encontró un script oficial que calcule γ "nativo" (por ejemplo con integral ponderada por n₂(x,y) para guías con varios materiales). Solo existe la fórmula con A_eff.
- No se verificó si la definición de A_eff de la Mode List usa solo el núcleo o toda la sección. Según la fórmula, integra sobre todo el plano.

## 3. INTERCONNECT: elementos no lineales; Kerr, peine y biestabilidad en anillos

### Takeaway
INTERCONNECT tiene un solver GNLSE de verdad (split-step simétrico) en los elementos **Optical Fiber (FIBER)** y
**NLSE Waveguide (NLSE_WGD)**: SPM, autoinclinación, Raman, TPA y portadores, más dispersión β₂/β₃ y γ (a partir de n₂ y
A_eff o tabulado). Para anillos está el **Optical Nonlinear Ring Modulator (NL_RING)**, un modelo concentrado (0-D) add-drop
con efectos térmicos, TPA y FCA, y desde 2026 R1.3 también **Kerr** (Δn = n₂P_circ/A_eff). Sirve para biestabilidad o
autopulsación de un modo, pero **no** para peines: no hay elemento de peine de Kerr ni solver LLE.

### Cited Findings
- **NLSE Waveguide (NLSE_WGD)**, elemento creado en la KB el 2022-07-20:
  - Resuelve un par de GNLSE acopladas con β_n, pérdidas, γ₁₁/γ₂₂/γ₁₂, TPA (vía r = β_TPA c/(2ω₀n₂)), Raman (T_R), FCA/FCD y ecuación de tasa de portadores, por el método "Symmetrized Split-Step Fourier Method (SSSFM)" en *block mode*.
  - Propiedades: "reference frequency", "length", "loss 1" [dB/m], "group index 1", "dispersion 1" [s/m/m], "dispersion slope 1" [s/m²/m], "nonlinear coefficient 11" [1/m/W], "nonlinear specification" [parameters, table], "nonlinear index" [m²/W], "effective area" [m²], "self-steepening effects", "raman effects", "tpa effects", "free carriers effects", "coupled mode".
  - Sin "coupled mode", γ = n₂ω₀/(cA).
  - Ejemplos: NLSE_WGD_Yin2007.icp (SPM + TPA + FC en Si) y NLSE_WGD_Daniel2010_Fig9.icp.

  — [NLSE Waveguide (NLSE_WGD)](https://optics.ansys.com/hc/en-us/articles/7945837183763-NLSE-Waveguide-NLSE-WGD-INTERCONNECT-Element)
- **Optical Fiber (FIBER)**: CGNLSE con SSSFM y PMD. Propiedades "nonlinear index" [m²/W], "effective area" [m²], "nonlinear specification", Raman y "nonlinear phase change" (0.05 rad por paso). γ = n₂ω₀/(cA_eff). — [Optical Fiber (FIBER)](https://optics.ansys.com/hc/en-us/articles/360036108194-Optical-Fiber-FIBER-INTERCONNECT-Element)
- Ejemplo de **SPM, GVD y self-steepening** con el GNLSE de INTERCONNECT, que reproduce las figuras 3.1 y 4.21(a) de Agrawal (N = 10, s = 0.1). Archivos: AgrawalFig3_1.icp, AgrawalFig4_21a.icp, calculateParms*.lsf, plotResult*.lsf, smf28_qpsk.icp. — [Pulse broadening from linear and nonlinear dispersion in an optical fiber](https://optics.ansys.com/hc/en-us/articles/360042819393-Pulse-broadening-from-linear-and-nonlinear-dispersion-in-an-optical-fiber)
- **Optical Nonlinear Ring Modulator (NL_RING)**:
  - Puertos: input, output 1 (through), output 2 (drop), modulation 1 y modulation 2.
  - Guía: "effective index", "group index", "dispersion", "dispersion slope", "coupling coefficient 1/2", "nonabsorption loss", "linear absorption loss".
  - Waveguide/Nonlinearities: "thermal effects", "effective index temperature sensitivity" (1.86e-4 /K), "thermal time constant", "heat capacity", "free carrier effects", "two-photon absorption coefficient" (8.4e-12 m/W), "two-photon absorption effective area", "free carrier absorption coefficient", etc.
  - Kerr: Δn_Kerr(t) = n₂·P_circ(t−τ)/A_eff-Kerr, con las propiedades "Kerr coefficient n2" y "Kerr effective area". La tabla de propiedades de la página todavía no las lista; aparecen en Implementation Details.
  - Limitaciones: es un modelo "inherently 0-D, with an assumption of uniform temperature inside the ring, and uniform power". Con no linealidades activadas no admite ONA ("will result in an error"). El paso temporal debe ser menor que medio round-trip.
  - Diagnósticos: "record temperature profile", "record carrier density profile" y "record circulating power profile".
  - Ejemplos: nonlinearRing_ONA_samplerate_example.icp y nonlinearRing_diagnostic_example.icp.
  - Referencia: Johnson et al., Opt. Express 14, 817 (2006).

  — [Optical Nonlinear Ring Modulator (NL_RING)](https://optics.ansys.com/hc/en-us/articles/43036851200403-Optical-Nonlinear-Ring-Modulator-NL-RING-INTERCONNECT-Element)
- NL_RING se añadió en **2025 R2.1** ("incorporates nonlinear behaviors arising from free carriers and self-heating effects"). — [2025 R2.1 Release Notes](https://optics.ansys.com/hc/en-us/articles/43598583744915-2025-R2-1-Release-Notes)
- Kerr en NL_RING llegó en **2026 R1.3**: "The Kerr non-linearity effect is added to the Nonlinear Ring Modulator model… This enables you to more effectively model high-Q rings to accurately predict dynamic processes such as self-pulsation." — [2026 R1.3 Release Notes](https://optics.ansys.com/hc/en-us/articles/53916763140499-2026-R1-3-Release-Notes)
- **Nonlinear Waveguide (WGD)**: tablas de perturbación de índice por portadores y por efecto térmico, en función de la potencia, con constantes de tiempo. Se usa junto a un Straight Waveguide. Archivos: nonlinear_waveguide.icp, free_carrier.txt, thermal.txt. — [Nonlinear Waveguide (WGD)](https://optics.ansys.com/hc/en-us/articles/360036618713-Nonlinear-Waveguide-WGD-INTERCONNECT-Element)
- **Optical Nonlinear S-Parameter (SPAR)**: S-parámetros dependientes de la potencia óptica de entrada (por ejemplo, un absorbedor saturable). Solo 1×1. — [Optical Nonlinear S-Parameter (SPAR)](https://optics.ansys.com/hc/en-us/articles/360036107954-Optical-Nonlinear-S-Parameter-SPAR-INTERCONNECT-Element)
- **SHG Waveguide (SHG_WGD)**, de χ⁽²⁾, añadido en 2023 R1.1, que también trae el ejemplo SFWM con qINTERCONNECT. — [SHG_WGD](https://optics.ansys.com/hc/en-us/articles/13534783507219-SHG-Waveguide-SHG-WGD-INTERCONNECT-Element); [2023 R1.1 Release Notes](https://optics.ansys.com/hc/en-us/articles/13659084854163-2023-R1-1-Release-Notes)
- Los anillos lineales **Single/Double Bus Ring Resonator (RING)** tienen n_eff, n_g y dispersión, pero ninguna propiedad no lineal (0 coincidencias de "nonlinear" o "Kerr" en su página). — [Double Bus Ring Resonator (RING)](https://optics.ansys.com/hc/en-us/articles/360036618833-Double-Bus-Ring-Resonator-RING-INTERCONNECT-Element)
- La lista alfabética de elementos primitivos solo tiene como no lineales EDF, NLSE_WGD, WGD, FIBER, NL_RING, SPAR y SHG_WGD. Ninguno es de peine ni LLE. — [Alphabetical list of all primitive elements](https://optics.ansys.com/hc/en-us/articles/360036106974-Alphabetical-list-of-all-primitive-elements)

### Inferences
- **Biestabilidad Kerr en el add-drop de SiN:**
  - En v261 solo es posible si el cluster tiene el service pack 2026 R1.3 o posterior; la v261 base (R1.0) probablemente no trae Kerr en NL_RING. Hay que verificarlo en la lista de propiedades del elemento.
  - Con NL_RING y R1.3: barrido temporal lento de la potencia o del detuning, con un CW laser y un medidor de potencia. El ONA no sirve si hay no linealidades.
  - En SiN, el efecto termo-óptico (dn/dT ≈ 2.5e-5 /K para SiN, valor de literatura no verificado aquí) suele dominar sobre Kerr en CW. NL_RING permite activarlos por separado y compararlos.
  - En v202 no existe NL_RING. La alternativa es armar el lazo a mano (acopladores + Straight Waveguide + Nonlinear Waveguide (WGD) con tablas Δn(P) construidas como n₂P/A_eff). Es una aproximación propia, no un flujo oficial.
- **Peine de Kerr:** NL_RING usa potencia uniforme y una sola fase por vuelta, sin un campo resuelto en z ni dispersión intracavidad por modo. No puede reproducir MI ni solitones. Meter NLSE_WGD dentro de un lazo con acopladores (mapa de Ikeda) es en teoría posible, pero no hay ningún ejemplo oficial. Además requiere ventanas de tiempo de miles de round-trips con la resolución de banda ancha del peine, así que sería muy costoso o inviable. La herramienta adecuada es un LLE externo (pyLLE, código propio) alimentado con datos de FDE.
- **SPM y supercontinuo en guía recta de SiN:** NLSE_WGD (desde ~2022) o FIBER (ya en v202) con β₂, β₃, γ y pérdidas sacados de FDE reproducen el flujo oficial del ejemplo de la PCF. Ojo: NLSE_WGD expande la dispersión solo hasta D y su pendiente (β₂, β₃), insuficiente para ondas dispersivas en un supercontinuo de una octava.

### Gaps
- No se confirmó en qué versión exacta apareció NLSE_WGD: no figura en las notas de 2022 R2 ni R2.1–R2.4 revisadas por grep; el artículo se creó el 2022-07-20. Hay que tratarlo como posterior a 2020 R2.
- No se pudo verificar si el FIBER de v202 ya tenía todas las propiedades actuales. El ejemplo de ensanchamiento de pulsos existía en la KB en 2020.
- No se encontraron webinars, blogs ni app notes de Ansys sobre microcombs ni acoplamiento con LLE. Las búsquedas web y de la KB no dieron nada.

## 4. Inventario por versión y producto (v202 frente a v261) y literatura externa

### Takeaway
Casi todo el flujo χ⁽³⁾ clásico de FDTD/varFDTD/FDE ya está en 2020 R2. Lo posterior a v202 es NLSE_WGD (~2022),
SHG_WGD y SFWM/qINTERCONNECT (2023 R1.1), el ejemplo del supercontinuo en PCF (2024), NL_RING (2025 R2.1) y Kerr en NL_RING
(2026 R1.3). No apareció ningún paper en el que Lumerical simule directamente un peine de Kerr. Los papers usan
mode-solvers para la dispersión y LLE aparte.

### Cited Findings
- **Producto FDTD** (FDTD 3D/2D): modelos Chi2, Chi3/Chi2, Chi3 Raman Kerr, Kerr nonlinear y plugins. **Producto MODE**: FDE (dispersión, A_eff), EME y varFDTD ("2.5D FDTD Propagator"), con los mismos materiales en varFDTD. — [Advanced material models "in FDTD and MODE"](https://optics.ansys.com/hc/en-us/articles/360034394734-Advanced-and-custom-optical-material-models-in-FDTD-and-MODE); [FWM varFDTD](https://optics.ansys.com/hc/en-us/articles/360041718794-Four-wave-mixing-varFDTD)
- **Producto INTERCONNECT**: FIBER, NLSE_WGD, WGD, NL_RING, SPAR, SHG_WGD. qINTERCONNECT para estados cuánticos: en Linux necesita dos licencias GUI para correrlo desde script. — [SFWM example](https://optics.ansys.com/hc/en-us/articles/15100783091731-Spontaneous-Four-Wave-Mixing-SFWM-Microring-Resonator-Photon-Source)
- La lista oficial de features de licencia por producto existe; no se revisó en detalle. — [List of Lumerical license features by product](https://optics.ansys.com/hc/en-us/articles/360052724713-List-of-Lumerical-license-features-by-product)
- Fechas por la API de la KB: NLSE_WGD creado 2022-07-20, SFWM 2023-03-22, supercontinuo PCF 2024-03-21, NL_RING 2025-07-16 (actualizado 2026-07-28). Los ejemplos de biestabilidad, FWM y solitones se migraron el 2020-01-22.
- En la literatura, el modelado de peines de octava se hace con un LLE generalizado. — [Coen et al., arXiv:1211.1697](https://arxiv.org/pdf/1211.1697)
- Hay un paper de un simulador de micro-peines en Si₃N₄ basado en LLE (Photonics 2025: FSR 7.24 nm, A_eff 1.0829 µm²). No se pudo abrir (403) para ver si usa Lumerical. — [MDPI Photonics 12(7):661](https://www.mdpi.com/2304-6732/12/7/661)

### Inferences
- Tabla de disponibilidad (✔ = confirmado o muy probable, ✘ = no existe, ? = sin verificar):

| Capacidad | v202 (2020 R2, local) | v261 (2026 R1, cluster) |
|---|---|---|
| FDTD/varFDTD con Chi3/Chi2, Chi3 Raman Kerr, Kerr nonlinear | ✔ | ✔ (no en GPU) |
| FDE: n_eff, n_g, D, A_eff, export a INTERCONNECT | ✔ | ✔ |
| INTERCONNECT FIBER (GNLSE, SPM/Raman) | ✔ (probable) | ✔ |
| INTERCONNECT NLSE_WGD (GNLSE + TPA/FCA) | ✘ | ✔ |
| NL_RING (térmico, FCA/TPA) | ✘ | ✔ |
| NL_RING con Kerr | ✘ | ? (requiere R1.3) |
| Peine de Kerr / LLE nativo | ✘ | ✘ |

- Los ejemplos oficiales de biestabilidad y FWM usan χ⁽³⁾ inflado y Q bajo. Para el proyecto, lo pedagógicamente honesto es reproducirlos tal cual para aprender el flujo, luego hacer una versión SiN en varFDTD con χ⁽³⁾ real y potencia escalada (n₂I constante), y comparar con el modelo analítico de biestabilidad o con el LLE.

### Gaps
- No se encontraron tesis o artículos que describan explícitamente simulación no lineal de anillos o peines hecha con Lumerical (más allá de los ejemplos de Ansys). Las búsquedas web no devolvieron nada concluyente.
- No se encontraron webinars de Ansys sobre microcombs.
