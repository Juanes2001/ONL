# Lumerical diseña la guía, la LLE simula el anillo

Ninguna versión de Ansys Lumerical, ni la v202 (2020 R2) local ni la v261 (2026 R1) del cluster, simula peines de Kerr, solitones disipativos ni pulsos oscuros en un microanillo realista. No trae un solver de la ecuación de Lugiato-Lefever (LLE): la búsqueda de "Lugiato" y "microcomb" en su Knowledge Base devuelve 0 artículos, y la propia Ansys reconoce que el FDTD 3D directo de anillos grandes "is not practical" ([Ansys SFWM](https://optics.ansys.com/hc/en-us/articles/15100783091731-Spontaneous-Four-Wave-Mixing-SFWM-Microring-Resonator-Photon-Source)). Lumerical sí cubre con solvencia la parte lineal de la que depende todo lo demás. El FDE de MODE da n_eff(λ), n_g, D y A_eff, y de ahí salen β₂, γ y D_int(μ). FDTD y varFDTD traen materiales χ⁽³⁾ para demostraciones cortas (biestabilidad y FWM, con χ⁽³⁾ inflado a propósito). INTERCONNECT tiene GNLSE de guía (FIBER y NLSE_WGD) y un anillo no lineal de un solo modo (NL_RING), que solo existe en versiones posteriores a la v202. La dinámica del anillo se resuelve fuera de Lumerical, con una LLE add-drop en Python que suma κ_ex2 al amortiguamiento y toma la salida del drop como √κ_ex2·A, y la del supercontinuo con una GNLSE (la RK4IP propia del repo, contrastada con gnlse-python). Para el anillo sensor del proyecto (SiN de 400 nm, cladding acuoso, Q_L ≈ 10⁴) los números son contundentes. **El umbral paramétrico estimado ronda los 130 W**, la deriva Kerr a 1 mW es unas 10⁵ veces menor que el ancho de línea y el efecto térmico del agua domina. Además, la dispersión normal esperada solo admite pulsos oscuros con un mecanismo de arranque adicional. La no linealidad que el proyecto sí puede estudiar con realismo es la SPM y el supercontinuo en una guía recta de dispersión normal. La LLE queda como herramienta para acotar la potencia de operación del sensor y para un anillo comparativo de alto Q.

## Lumerical resuelve lo lineal y lo no lineal "corto", pero no tiene LLE

### FDTD y varFDTD: cuatro modelos χ⁽³⁾, pensados para demostraciones

FDTD y el propagador 2.5D de MODE (varFDTD) comparten cuatro modelos de material de tercer orden ([Ansys, materiales avanzados](https://optics.ansys.com/hc/en-us/articles/360034394734-Advanced-and-custom-optical-material-models-in-FDTD-and-MODE)):

- **"Chi3/Chi2"**: parámetros χ⁽¹⁾, χ⁽²⁾ [m/V] y χ⁽³⁾ [m²/V²], con material base dispersivo opcional. Ansys advierte que el algoritmo puede introducir "some artificial asymmetry".
- **"Chi3 Raman Kerr"**: P = ε₀χ⁽¹⁾E + ε₀αχ⁽³⁾E³ + ε₀(1−α)E(χ_R ∗ E²), con un peso α entre Kerr y Raman y un Raman lorentziano. Admite material base.
- **"Kerr nonlinear"**: P = ε₀(χ⁽¹⁾ + χ⁽³⁾|E|²)E. No admite material base ("This is not a plugin material"), así que ignora la dispersión del SiN.
- **"Chi2"**.

Hay que tener en cuenta varias consecuencias prácticas:

- χ⁽³⁾ se ingresa en m²/V², no como n₂, y la amplitud de la fuente se fija en V/m.
- El mallado automático y el Material Explorer ven solo el índice del material base (o n = 1 si no hay base), así que hace falta un mesh override.
- El conformal mesh no se aplica salvo que se active "revert to base material for conformal mesh cells".
- La estabilidad exige χ⁽³⁾E² ≪ χ⁽¹⁾.
- La "CW normalization" no vale en simulaciones no lineales. Hay que usar `nonorm` e integrar el vector de Poynting a mano. También conviene desactivar "use source limits", fijar "set simulation bandwidth" y vigilar el aliasing de los monitores de tiempo ([Ansys, metodología no lineal](https://optics.ansys.com/hc/en-us/articles/360041727474-Nonlinear-and-gain-methodology)).
- El FDTD en GPU no admite estos materiales ([Ansys, FDTD en GPU](https://optics.ansys.com/hc/en-us/articles/17518942465811-Getting-started-with-running-FDTD-on-GPU)).

Para un anillo de SiN, la elección más defendible es **"Chi3 Raman Kerr" con α = 1 y base Si₃N₄**. Así se conserva la dispersión del material y se evita la ambigüedad de "Chi3/Chi2". Esa recomendación es una inferencia de las notas. La ambigüedad viene del foro de Ansys, donde un empleado afirmó que Chi3/Chi2 "needs non-zero chi2" y que para χ⁽³⁾ puro se use el modelo Kerr ([foro Ansys](https://innovationspace.ansys.com/forum/?p=295376)). Esa afirmación contradice el ejemplo oficial de biestabilidad, que usa justamente Chi3/Chi2 con χ⁽²⁾ = 0. Solo se vio el fragmento del buscador, no el hilo completo, así que la contradicción queda **sin resolver**.

Los ejemplos oficiales cuelgan de la lista [Nonlinear optics – list of examples](https://optics.ansys.com/hc/en-us/articles/360043165194-Nonlinear-optics-list-of-examples). Los más cercanos al proyecto son dos:

- **Ring resonator – optical bistability** ([enlace](https://optics.ansys.com/hc/en-us/articles/360041723954-Ring-resonator-optical-bistability)): un racetrack plasmónico en FDTD 2D o varFDTD, con un χ⁽³⁾ **10 veces el de la referencia** para bajar la intensidad necesaria. Usa rampas de potencia de subida y bajada de 15 500 fs (forward.fsp, reverse.fsp, set_source.lsf, bistability_results.lsf).
- **Four wave mixing (varFDTD)** ([enlace](https://optics.ansys.com/hc/en-us/articles/360041718794-Four-wave-mixing-varFDTD)): un anillo SOI add-drop con material "Raman Kerr" sobre "Si (Silicon) – Palik". El bombeo está en 1.534 µm, la señal en 1.561 µm y el idler aparece en ≈1.508 µm. La simulación dura 50 000 fs, con PML "stabilized" porque la estándar diverge. Los archivos son ring_resonator_FWM.lms y ring_nonlinear_FWM.lsf. Ansys aclara que su χ⁽³⁾ "is more for demonstration purpose".

Completan la familia varios ejemplos más:

- [Kerr en haz gaussiano](https://optics.ansys.com/hc/en-us/articles/360041718634-Kerr-effect-on-Gaussian-beam-propagation) (autoenfoque 3D).
- [FWM en medio Kerr en bloque](https://optics.ansys.com/hc/en-us/articles/360041718694-Four-wave-mixing-with-Kerr-nonlinear-material), con THG.
- [Solitón en medio homogéneo](https://optics.ansys.com/hc/en-us/articles/360041718614-Soliton-propagation-in-a-homogeneous-medium).
- **[Soliton in an SOI waveguide](https://optics.ansys.com/hc/en-us/articles/360042190173-Soliton-in-an-SOI-waveguide)**, que trae el truco oficial para meter la dispersión de la guía en un modelo temporal. El GVD sale de FDE (waveguide_neff_sweep.lms, D_to_GVD.lsf); luego n_eff(λ) se exporta como material "Sampled data" y sirve de base a "Chi3 Raman Kerr" en un varFDTD 1D.

No hay ejemplo oficial de SPM en guía integrada con FDTD, ni de peine de Kerr, ni de THG en guía o anillo de SiN.

El coste explica por qué Ansys infla χ⁽³⁾. El tiempo de vida del fotón, τ = Q/ω₀, vale **≈8 ps para Q = 10⁴, ≈82 ps para 10⁵ y ≈0.82 ns para 10⁶** (cálculo propio a 1550 nm). Un barrido de biestabilidad necesita rampas mucho más largas que τ, y un peine necesita miles de τ. La referencia de que la simulación de onda completa de un peine es posible pero carísima llegó apenas en 2026, y con otro software (Tidy3D en GPU). Usó un anillo de R = 50 µm, más de 1.3×10⁹ celdas, unos 6×10⁶ pasos, 400 ps simulados y **un Q cargado de solo 1.8×10⁴**. Además, los tres regímenes comparados se corrieron en 2D, con unas 2 GPU-horas A100 por caso ([Flexcompute](https://hs.flexcompute.com/blog/acomputational-milestone-in-full-wave-kerr-comb-simulation-using-gpu-accelerated-fdtd); [Wang, Zhou y Yu, IEEE JSTQE 2026](https://doi.org/10.1109/JSTQE.2026.3659816)). Con 7.4 GB de RAM y CPU, el FDTD χ⁽³⁾ del anillo completo queda descartado. varFDTD puede servir para biestabilidad con Q ≲ 10⁴ si se escala χ⁽³⁾ o la potencia (inferencia de las notas).

### MODE FDE: el origen de β₂, A_eff, γ y D_int

El FDE es la pieza de Lumerical que más rinde en este problema. La Mode List reporta n_eff, pérdidas y **effective area** con la definición de Agrawal, A_eff = (∫|E|²dA)²/∫|E|⁴dA ([Ansys FDE Mode List](https://optics.ansys.com/hc/en-us/articles/360034396734)). La pestaña Frequency analysis calcula n_eff, v_g y D en un rango de frecuencias. Ansys recomienda el ajuste *Multi-Coefficient Model* y activar "detailed dispersion calculation", porque con datos muestreados aparecen picos espurios en D ([Ansys, dispersión SOI](https://optics.ansys.com/hc/en-us/articles/360042304954-Dispersion-analysis-of-SOI-waveguide)). Por script, el comando `frequencysweep` genera la D-card "frequencysweep", que se lee con `getdata` también desde lumapi. "Track selected mode" funciona mejor con unos tres modos de prueba ([Ansys frequencysweep](https://optics.ansys.com/hc/en-us/articles/360034925153-frequencysweep); [foro Ansys](https://innovationspace.ansys.com/forum/?p=169850)).

**γ no es un resultado nativo**: se calcula a mano como γ = n₂ω₀/(cA_eff). Así lo hace el ejemplo oficial de [supercontinuo en fibra de cristal fotónico](https://optics.ansys.com/hc/en-us/articles/27638850917267-Supercontinuum-generation-in-photonic-crystal-fiber) (2024). Su cadena es la plantilla del flujo MODE → INTERCONNECT:

1. PCF.lms y Design.lsf ajustan el cero de dispersión cerca de 835 nm.
2. Dispersion_export.lsf exporta A_eff, n_g, D y la pendiente de D.
3. nonlinear_NLSE.icp los carga en el elemento NLSE Waveguide, con n₂ = 2.7×10⁻²⁰ m²/W, un sech de 50.1 fs y 10 kW de pico. El espectro sale de ≈580 a >1150 nm.

El ejemplo de [SFWM en microanillo de Si₃N₄](https://optics.ansys.com/hc/en-us/articles/15100783091731-Spontaneous-Four-Wave-Mixing-SFWM-Microring-Resonator-Photon-Source) muestra el reparto que Ansys considera razonable para un anillo:

- FDTD solo para la región del acoplador.
- FDE para las guías recta y curva, exportadas como .ldf.
- INTERCONNECT para el racetrack y el Q.
- Un script para el área de traslape de cuatro ondas (0.59 µm²).

### INTERCONNECT: GNLSE de guía y un anillo no lineal de un solo modo

INTERCONNECT tiene un GNLSE real (split-step simétrico) en dos elementos:

- **Optical Fiber (FIBER)**: CGNLSE con "nonlinear index", "effective area", Raman y PMD ([Ansys FIBER](https://optics.ansys.com/hc/en-us/articles/360036108194-Optical-Fiber-FIBER-INTERCONNECT-Element)).
- **NLSE Waveguide (NLSE_WGD)**: GNLSE acopladas con β_n, pérdidas, γ, TPA, Raman, absorción y dispersión por portadores. Los ejemplos son NLSE_WGD_Yin2007.icp y NLSE_WGD_Daniel2010_Fig9.icp ([Ansys NLSE_WGD](https://optics.ansys.com/hc/en-us/articles/7945837183763-NLSE-Waveguide-NLSE-WGD-INTERCONNECT-Element)).

El ejemplo de [SPM, GVD y self-steepening](https://optics.ansys.com/hc/en-us/articles/360042819393-Pulse-broadening-from-linear-and-nonlinear-dispersion-in-an-optical-fiber) reproduce las figuras 3.1 y 4.21(a) de Agrawal. Sirve como banco de pruebas para la GNLSE propia del repo. Una limitación importa para el supercontinuo: NLSE_WGD expande la dispersión solo hasta D y su pendiente (β₂, β₃). Eso no basta para ubicar ondas dispersivas en un espectro de una octava (inferencia de las notas).

Para anillos, el elemento relevante es el **Optical Nonlinear Ring Modulator (NL_RING)** ([Ansys NL_RING](https://optics.ansys.com/hc/en-us/articles/43036851200403-Optical-Nonlinear-Ring-Modulator-NL-RING-INTERCONNECT-Element)):

- Es add-drop (puertos input, output 1 through y output 2 drop).
- Incluye efectos térmicos, TPA y portadores libres. Llegó en **2025 R2.1** ([notas 2025 R2.1](https://optics.ansys.com/hc/en-us/articles/43598583744915-2025-R2-1-Release-Notes)).
- Desde **2026 R1.3** también incluye Kerr, Δn_Kerr = n₂P_circ/A_eff ([notas 2026 R1.3](https://optics.ansys.com/hc/en-us/articles/53916763140499-2026-R1-3-Release-Notes)).
- Es "inherently 0-D": supone temperatura y potencia uniformes en el anillo. Con no linealidades activas no admite el ONA.

Sirve para la biestabilidad y la autopulsación de un modo, pero **no para peines**: no resuelve el campo a lo largo del anillo ni la dispersión modo a modo. Los anillos lineales Single/Double Bus Ring Resonator no tienen ninguna propiedad no lineal ([Ansys RING](https://optics.ansys.com/hc/en-us/articles/360036618833-Double-Bus-Ring-Resonator-RING-INTERCONNECT-Element)). La lista alfabética de elementos no contiene ningún elemento de peine ni de LLE ([Ansys, lista de elementos](https://optics.ansys.com/hc/en-us/articles/360036106974-Alphabetical-list-of-all-primitive-elements)).

### Qué cambia entre la v202 local y la v261 del cluster

Casi todo el flujo χ⁽³⁾ de FDTD, varFDTD y FDE ya existe en 2020 R2. Lo posterior es sobre todo INTERCONNECT. La tabla resume las notas. Las fechas salen de la API de la Knowledge Base y de las notas de versión. Las celdas marcadas "probable" no se verificaron archivo por archivo.

| Capacidad | v202 = 2020 R2 (local) | v261 = 2026 R1 (cluster) |
|---|---|---|
| FDTD/varFDTD con Chi3/Chi2, Chi3 Raman Kerr y Kerr nonlinear | Sí. Ejemplos migrados a la KB el 2020-01-22, presentes desde ≥2020a (probable) | Sí, pero no en GPU |
| FDE: n_eff, n_g, D, A_eff y export a INTERCONNECT | Sí | Sí. Desde 2022 R1.2, FEEM también da A_eff |
| INTERCONNECT FIBER (GNLSE, SPM, Raman) | Probable | Sí |
| INTERCONNECT NLSE_WGD | No (artículo creado el 2022-07-20) | Sí |
| SHG_WGD y SFWM/qINTERCONNECT | No (2023 R1.1) | Sí |
| NL_RING térmico/TPA/FCA | No (2025 R2.1) | Sí |
| NL_RING con Kerr | No | Solo si el cluster tiene el service pack **R1.3 o posterior**: hay que comprobarlo en la lista de propiedades del elemento |
| Peine de Kerr / LLE nativo | No | No |

En la v202, la única forma de imitar un anillo Kerr en INTERCONNECT es armar el lazo a mano con acopladores, Straight Waveguide y Nonlinear Waveguide (WGD) ([Ansys WGD](https://optics.ansys.com/hc/en-us/articles/360036618713-Nonlinear-Waveguide-WGD-INTERCONNECT-Element)), con tablas Δn(P) construidas como n₂P/A_eff. Es una aproximación propia de las notas, no un flujo oficial.

## La LLE add-drop suma κ_ex2 y convierte el drop en una ventana intracavidad

**Advertencia.** Las ecuaciones de esta sección son las formas estándar de Herr 2014 y Kippenberg 2018 ([Herr et al., Nat. Photon. 8, 145](https://doi.org/10.1038/nphoton.2013.343); [Kippenberg et al., Science 361, eaan8083](https://doi.org/10.1126/science.aan8083)). Las notas las escribieron **de memoria** y solo comprobaron su consistencia dimensional: no se leyeron los textos completos. Los factores numéricos (el 8 de f², el argumento del sech, el 1.54 del umbral) deben cotejarse con el suplemento de Herr 2014 o con Kippenberg 2018 antes de implementarlos.

El espectro de modos del anillo se escribe como ω_μ = ω₀ + D₁μ + D₂μ²/2 + …, con D_int(μ) = ω_μ − ω₀ − D₁μ, D₁ = 2πc/(n_g L) y L = 2πR. Desde el FDE, D₂ ≈ −(c/n_g)D₁²β₂: la dispersión anómala (β₂ < 0) corresponde a D₂ > 0. En la convención de modos acoplados, la LLE add-drop dimensional es

∂A/∂t = −[(κ₀ + κ_ex1 + κ_ex2)/2 + iδω]A + i(D₂/2)∂²A/∂φ² + i g₀|A|²A + √κ_ex1·s_in,

con |A|² = número de fotones intracavidad, s_in = √(P_in/ħω₀), δω = ω₀ − ω_p y g₀ = ħω₀²c n₂/(n₀²V_eff), donde V_eff = A_eff·L.

Las salidas son s_thr = s_in − √κ_ex1·A en el through y **s_drop = √κ_ex2·A en el drop**. Por modo, P_drop,μ = ħω_μ κ_ex2|A_μ|². El drop no contiene el bombeo transmitido que interfiere en el through, así que su espectro es el intracavidad multiplicado por una constante. Eso lo convierte en el puerto natural para validar una simulación. Para dispersión de orden superior, el término D₂ se sustituye por el D_int(μ) completo en el espacio de Fourier. La normalización usada es Ψ = √(2g₀/κ)A, ζ₀ = 2δω/κ, f² = 8ηg₀P_in/(κ²ħω₀) y η = κ_ex1/κ. Con ella, la MI arranca en |Ψ|² = 1 y aparece biestabilidad para ζ₀ > √3. El solitón brillante aproximado es Ψ ≈ Ψ_cw + √(2ζ₀)·sech(√(ζ₀/d₂)φ) y existe para √3 ≲ ζ₀ < π²f²/8, con d₂ = D₂/κ.

Ningún artículo revisado escribe esta receta add-drop de forma explícita. Las notas la deducen del acoplamiento de modos, y es consistente con los experimentos de Purdue:

- Wang et al. 2013 muestran que el drop entrega espectros suaves, con potencias comparables entre el bombeo y las líneas vecinas ([Opt. Express 21, 22441](https://doi.org/10.1364/OE.21.022441)).
- Wang et al. 2016 ven que, en régimen de solitón único, el bombeo es >99 % de la potencia del through, mientras que dentro de la cavidad "la mayor parte de la potencia está en el solitón" ([Opt. Express 24, 10890](https://doi.org/10.1364/OE.24.010890)).

**Corrección a las notas.** Una de ellas atribuye el estudio del drop a la DOI 10.1364/OE.22.012148. Crossref la registra como la **fe de erratas** de ese artículo. El artículo original es 10.1364/OE.21.022441.

**Umbral con drop.** Esta derivación es propia de las notas y debe tratarse como inferencia. En resonancia, |A₀|² = 4κ_ex1P_in/(κ²ħω₀), y el umbral g₀|A₀|² = κ/2 da

P_th = κ³ħω₀/(8g₀κ_ex1) = π n₀²V_eff/(4ηλn₂Q_L²).

Fijados κ₀ y κ_ex2, el mínimo está en κ_ex1 = (κ₀ + κ_ex2)/2. En un anillo simétrico el óptimo es κ_ex1 = κ_ex2 = κ₀/4, y el drop siempre sube el umbral respecto del mismo anillo con un solo bus. La fórmula clásica de Kippenberg, Spillane y Vahala (2004), P_th ≈ 1.54(π/2)(Q_ex/2Q_L)n²V_eff/(n₂λQ_L²) ([PRL 93, 083904](https://doi.org/10.1103/PhysRevLett.93.083904)), también se citó de memoria. En acoplamiento crítico difiere de la anterior en un factor ~1.5 y en cómo depende de η. Esa discrepancia es otro punto a cerrar con las fuentes originales.

**Validez.** La LLE supone alta finesse: pérdida y acoplo por vuelta pequeños, y desintonía total y fase no lineal por vuelta pequeñas. Cuando eso falla se usa el mapa de Ikeda, que propaga una NLSE por vuelta y aplica la condición de contorno del acoplador ([Ikeda 1979](https://doi.org/10.1016/0030-4018(79)90090-7); [Hansson y Wabnitz, JOSA B 2015](https://doi.org/10.1364/JOSAB.32.001259); [Hansson y Wabnitz, Nanophotonics 2016](https://doi.org/10.1515/nanoph-2016-0012)). No hay un umbral de finesse publicado y universal. Para el sensor, con Q_L ≈ 10⁴ y FSR ≈ 230 GHz, la finesse ronda 12 y la pérdida por vuelta es ~25 %. La LLE vale como primera aproximación, pero conviene contrastarla con un mapa de Ikeda (inferencia de las notas).

**Dispersión normal.** No hay solitones brillantes. Hay pulsos oscuros y platicones, que necesitan un mecanismo de arranque:

- Un cruce evitado de modos, modelado en la LLE como un desplazamiento de fase en un modo vecino ([Xue et al., Nat. Photon. 2015](https://doi.org/10.1038/nphoton.2015.137); [Liu et al., Optica 2014](https://doi.org/10.1364/OPTICA.1.000137)).
- Bombeo modulado ([Lobanov et al., Opt. Express 2015](https://doi.org/10.1364/OE.23.007713)).
- Anillos acoplados ([Helgason et al., Nat. Photon. 2021](https://doi.org/10.1038/s41566-020-00757-9)).
- Bombeo pulsado ([Xu et al., Opt. Lett. 2021](https://doi.org/10.1364/OL.413585)).

El mapa de estabilidad en ambos regímenes está en [Godey et al., PRA 2014](https://doi.org/10.1103/PhysRevA.89.063814).

**Supercontinuo dentro del anillo.** Dentro de la cavidad, el supercontinuo coherente es un solitón más ondas dispersivas emitidas donde D_int(μ) ≈ 0 ([Brasch et al., Science 2016](https://doi.org/10.1126/science.aad4811)). Se modela con la LLE generalizada y el D_int completo ([Coen et al., Opt. Lett. 2013](https://doi.org/10.1364/OL.38.000037)). Con bombeo pulsado sincronizado al FSR, la LLE lleva una fuerza que depende de τ ([Obrzud, Lecomte y Herr, Nat. Photon. 2017](https://doi.org/10.1038/nphoton.2017.140); [Anderson et al., Optica 2021](https://doi.org/10.1364/OPTICA.403302)).

**Efectos térmicos.** Se añaden con una ecuación de primer orden que desplaza δω ([Carmon, Yang y Vahala, Opt. Express 2004](https://doi.org/10.1364/OPEX.12.004742); [Stone et al., PRL 2018](https://doi.org/10.1103/PhysRevLett.121.063902)).

## Herramientas externas: una LLE propia en numpy gana a pyLLE en este proyecto

**pyLLE** es la referencia abierta: núcleo en Julia e interfaz en Python, con split-step Fourier ([Moille et al., J. Res. NIST 2019](https://doi.org/10.6028/jres.124.012); [GitHub gregmoille/pyLLE](https://github.com/gregmoille/pyLLE)). Sus ventajas:

- La dispersión entra como un CSV con dos columnas, orden azimutal y frecuencia de resonancia en Hz. Puede venir directamente de Lumerical.
- Ajusta D_int con un spline, sin truncarlo en una serie de Taylor. El artículo advierte, eso sí, que la extrapolación produce ondulaciones.
- El caso de referencia, 244 modos de un anillo de Si₃N₄, tardó **11 min** en un portátil de 2017.

Tres razones lo descartan como herramienta principal aquí:

- **Su autor declaró en agosto de 2026 que ya no lo mantiene** ("Not maintained anymore").
- Modela un único acoplamiento: no tiene puerto drop, ni efectos térmicos, ni Raman.
- Intercambia datos con Julia mediante HDF5 (`h5py`), que el cluster no tiene, y además exige instalar Julia.

Se puede usar en un anillo add-drop absorbiendo κ_ex2 en una pérdida efectiva, 1/Q_i,eff = 1/Q_i + 1/Q_c,drop, y reconstruyendo el drop desde `Acav` (inferencia de las notas). Pero eso lo vuelve más útil como validador local que como motor.

No existe un solver LLE estándar, mantenido, que traiga add-drop y efectos térmicos. Lo que hay son códigos académicos pequeños:

- [PyCORe](https://github.com/ElKosto/PyCORe), con licencia MIT.
- [Lugiato-Lefever_Equation_Solver](https://github.com/LuisAngelMendozaVelasco/Lugiato-Lefever_Equation_Solver), activo en 2026.
- [pycombs](https://github.com/PIC-Group-Adelaide-University/pycombs).
- [kerr_comb_simulator](https://github.com/miceks/kerr_comb_simulator), en MATLAB, con LLE y mapa de Ikeda.
- [pyGLLE](https://github.com/omelchert/pyGLLE).
- [inverseLLE](https://github.com/ErwanLucas/inverseLLE), del grupo de la EPFL.

El modelo de modos acoplados escala de forma cúbica con el número de modos, frente a N log N de la LLE con FFT ([Hansson, Modotto y Wabnitz](https://arxiv.org/pdf/1307.3428)). La conclusión de las notas es escribir **una LLE add-drop propia en numpy**. Basta un split-step simétrico de ~100 líneas con D_int tabulado, rampa de desintonía, κ_ex2 y, si hace falta, una ecuación térmica. Se valida contra el umbral de MI, el solitón sech y pyLLE, y corre en el cluster con Python 3.13 y solo numpy/scipy (guardando en .npz, sin h5py).

Para la GNLSE de la guía, la herramienta propia del repo es una RK4IP que, según `seccion_v1/ESTADO.md`, pasó 6/6 pruebas sin Lumerical. Esa RK4IP expande la dispersión en Taylor hasta β₄. Tres alternativas sirven para contrastarla:

- **gnlse-python** (WUST-FOG) ([GitHub](https://github.com/WUST-FOG/gnlse-python)): acepta la dispersión "computed from effective refractive indices" y γ(ω) a partir de A_eff(ω) según [Lægsgaard 2007](https://doi.org/10.1364/OE.15.016110). Trae Raman de fibra y solo depende de numpy/scipy. Está inactivo desde 2023 (gnlse 2.0.0 en PyPI, de 2022).
- **Luna.jl** ([GitHub](https://github.com/LupoLab/Luna.jl)): es el más activo (push del 2026-10-23). Su `prop_gnlse` usa coeficientes β_n, y los modos personalizados requieren la interfaz de bajo nivel, que su README advierte que no se mantiene.
- **Código del libro de Dudley y Taylor** ([jtravs/SCGBookCode](https://github.com/jtravs/SCGBookCode)): la referencia didáctica del RK4IP ([Hult 2007](https://doi.org/10.1109/JLT.2007.909373)). El caso de validación clásico es [Dudley, Genty y Coen 2006](https://doi.org/10.1103/RevModPhys.78.1135).

PyNLO original sigue declarando "requires Python 2" ([GitHub](https://github.com/pyNLO/PyNLO)). Para Si₃N₄ la literatura suele despreciar el Raman, pero las notas no encontraron una fuente que lo cuantifique.

| Herramienta | Qué resuelve | Add-drop / térmico | Estado (oct. 2026) | Encaje en el proyecto |
|---|---|---|---|---|
| pyLLE | LLE, D_int tabulado, varias bombas | No / No | Sin mantenimiento; necesita Julia y h5py | Validador local |
| LLE propia (numpy) | LLE o Ikeda con D_int completo | Sí / Sí (se escriben) | — | Motor principal, local y cluster |
| gnlse-python | GNLSE con n_eff(λ) y A_eff(ω) | — | Estable, inactivo desde 2023 | Contraste de la RK4IP propia |
| Luna.jl | UPPE/GNLSE, barridos paralelos | — | Muy activo | Opcional (requiere Julia) |
| INTERCONNECT FIBER / NLSE_WGD | GNLSE dentro de Lumerical | — | NLSE_WGD solo en la v261 | Contraste oficial |

## Flujo en ocho pasos: FDE en local, dinámica en Python, barridos al cluster

El flujo recomendado combina la receta de acoplamiento de las notas (§4 de herramientas) con los pasos que `seccion_v1` ya tiene escritos. Según su `ESTADO.md`, los pasos FDE (paso02 a paso04) **todavía no se han corrido** porque el Lumerical local estaba ocupado por la tesis. Antes de cualquier ejecución de Lumerical rige la regla del repo: se comprueba el turno y la RAM con `scripts/ram_lumerical.py`, y solo se lanza si no hay nada de fotonica-integrada vivo. Lo mismo vale en el cluster.

| Paso | Qué produce | Herramienta | Dónde |
|---|---|---|---|
| 1. Guía recta | n_eff(λ), n_g, D, β₂…β₄, A_eff(λ) para TE₀ y TM₀; cladding de SiO₂ y analito a n = 1.33, 1.35 y 1.37 | FDE `frequencysweep` (MCM, detailed dispersion, track selected mode) | Local v202 (paso02) |
| 2. Guía curva | Resonancias ω_m que cumplen m = n_eff(ω)ωR/c, D₁, D₂, D_int(μ), CSV (m, f_m); cruces de modos (saltos en n_eff o en la fracción TE) | FDE con bend radius = R | Local v202 (paso04) |
| 3. Acoplos y Q | κ_ex1, κ_ex2, Q₀ y espectro lineal add-drop | FDTD 3D del acoplador o EME; anillo en INTERCONNECT Double Bus Ring con .ldf; FDTD 3D lineal del anillo completo solo para validar | Acoplador en local si cabe; anillo completo en el cluster v261 |
| 4. Cifras no lineales | γ = n₂ω₀/(cA_eff), g₀, P_th (all-pass y add-drop), L_D, L_NL, N | Python | Local (paso05) |
| 5. Calibración de χ⁽³⁾ | Factor n₂↔χ⁽³⁾ de Lumerical; GNLSE propia contrastada | varFDTD 1D con base "Sampled data", como en el ejemplo del solitón SOI, o guía recta corta; INTERCONNECT FIBER | Local v202 (corridas cortas) |
| 6. GNLSE de la guía | SPM/SC en dispersión normal (SPM más optical wave breaking) | RK4IP propia y gnlse-python con n_eff(λ) completo | Local; los ensambles de ruido van al cluster |
| 7. LLE add-drop | Espectros through y drop, umbral de MI, pulsos oscuros con AMX o bombeo pulsado, deriva Kerr y térmica del sensor | LLE numpy (+ Ikeda si la finesse es baja); pyLLE como validador | Una corrida en local; barridos de desintonía × potencia × geometría × n_analito en el cluster |
| 8. Opcional | Biestabilidad térmica + Kerr de un modo | NL_RING (si la v261 tiene R1.3) o varFDTD con χ⁽³⁾ escalado y Q ≲ 10⁴ | Cluster (NL_RING) o local (varFDTD pequeño) |

Tres decisiones sostienen la tabla:

- **D_int sale de la sección curva, no de un Taylor de la recta.** Así lo consume pyLLE y así lo recomiendan Coen et al. y el trabajo de peines visibles que usa "the exact dispersion of the microring resonator" ([arXiv:1705.10848](https://arxiv.org/pdf/1705.10848)). Para la GNLSE de la guía, en cambio, se usa la sección recta.
- **El cluster no aporta nada al FDE de una sección**, que tarda minutos u horas en local. Su valor está en dos lugares: los barridos trivialmente paralelos de la LLE y la GNLSE, y el FDTD 3D lineal del anillo completo, que no cabe en 7.4 GB.
- **Primero hay que fijar la conversión n₂↔χ⁽³⁾.** Es lo primero que se mide en Lumerical antes de confiar en cualquier varFDTD no lineal (paso 5, detallado en la sección de pendientes).

## Con agua y Q ≈ 10⁴, el umbral Kerr sube a unos 130 W

Las notas calculan valores de referencia con n₂ = 2.4×10⁻¹⁹ m²/W, n₀ = 1.8, R = 100 µm, A_eff = 1 µm², n_g = 2.1 y η = 1/3. Ese n₂ coincide con la medida de [Ikeda et al. 2008](https://doi.org/10.1364/OE.16.012987) para SiN PECVD, hecha precisamente en anillos add-drop con Q ≈ 12 900 separando el efecto térmico del Kerr (según la lista previa de referencias del proyecto). Para la guía de 400 nm, las tres incógnitas son D₂, A_eff y n₀. Saldrán del paso02, así que los valores de la tabla son de orden de magnitud. La fila con β₂ normal es un ejemplo de este informe, no un resultado.

| Magnitud | Valor | Fórmula u origen |
|---|---|---|
| FSR | ≈ 227 GHz | c/(n_g·2πR) |
| κ/2π para Q_L = 10⁴ / 10⁶ | 19.3 GHz / 193 MHz | f₀/Q_L |
| τ_ph para Q_L = 10⁴ / 10⁶ | 8.2 ps / 0.82 ns | Q/ω₀ |
| Finesse para Q_L = 10⁴ | ≈ 12 | FSR/(κ/2π) |
| γ | ≈ 0.97 W⁻¹m⁻¹ | n₂ω₀/(cA_eff). Tan et al. midieron 1.4 W⁻¹m⁻¹ en guías de SiN ([APL 2010](https://doi.org/10.1063/1.3299008)) |
| g₀ | ≈ 5.5 rad/s (g₀/2π ≈ 0.9 Hz) | ħω₀²cn₂/(n₀²V_eff) |
| **P_th para Q_L = 10⁶ / 10⁵ / 10⁴** | **13 mW / 1.3 W / 130 W** | πn₀²V_eff/(4ηλn₂Q_L²) |
| D₂/2π con β₂ = −50 ps²/km (anómala) | ≈ +2.3 MHz | −(c/n_g)D₁²β₂ |
| D₂/2π con β₂ = +500 ps²/km (normal, ejemplo) | ≈ −23 MHz (d₂ = D₂/κ ≈ −1.2×10⁻³ con Q = 10⁴) | Cálculo propio |
| Deriva Kerr con P_in = 1 mW, Q_L = 10⁴ | ≈ 0.08 MHz, frente a κ/2π = 19 GHz | g₀|A|², con |A|² ≈ 9×10⁴ fotones |

El signo de la dispersión es casi seguro normal, aunque no está calculado para esta geometría. En una guía de Si₃N₄ de 300 nm, Kim et al. reportan D ≈ −1200 ps/(nm·km), dispersión normal fuerte que impide el peine ([Nat. Commun. 2017](https://doi.org/10.1038/s41467-017-00491-x); la cifra viene de un fragmento de ResearchGate). Tan et al. midieron GVD entre −0.57 y +0.86 ps²/m según la geometría. Un preprint con películas de 400 nm necesitó cladding de aire para abrir una ventana anómala, y en el visible ([arXiv:2404.01577](https://arxiv.org/pdf/2404.01577)). El cladding de agua además cambia la dispersión, el acople y el Q ([Choi, Gin y Su, Opt. Express 2022](https://doi.org/10.1364/OE.451631)). Por eso D_int debe recalcularse para cada n del analito.

La lectura física para el refractómetro es clara.

**Primero, los peines no son accesibles.** Con Q_L ≈ 10⁴, los ~130 W de umbral CW (y más si se carga el drop) hacen inalcanzable la dinámica Kerr CW en el chip. Aun sin ese problema, la dispersión normal exigiría AMX o anillos acoplados.

**Segundo, el sesgo Kerr del sensor es despreciable.** La deriva de ~0.08 MHz a 1 mW es unas 10⁵ veces menor que el ancho de línea. El sesgo relevante es el térmico, por la absorción del agua, que las notas de `seccion_v1` estiman en 47 dB/cm. El agua tiene dn/dT ≈ −1.12×10⁻⁴ K⁻¹ ([arXiv:1710.03605](https://arxiv.org/pdf/1710.03605)) y el SiN ≈ +2.45×10⁻⁵ K⁻¹ ([Arbabi y Goddard 2013](https://doi.org/10.1364/OL.38.003878), valor recordado, no extraído). Con una fracción de confinamiento en el agua Γ ≳ 0.2, ∂n_eff/∂T puede volverse negativo. El anillo quedaría casi atérmico, o con el triángulo térmico invertido. Es una inferencia que el FDE puede comprobar directamente.

**Tercero, el bombeo pulsado no rescata el anillo sensor.** Con finesse ~12 el realce intracavidad es pequeño, y el sistema se parece más a una guía con retroalimentación débil. Se modela con un mapa de Ikeda, no con la LLE.

Lo que sí funciona con 400 nm es el supercontinuo coherente en guía de dispersión normal, por SPM y optical wave breaking ([Rebolledo-Salgado et al., Opt. Express 2022](https://doi.org/10.1364/OE.450987)). Encaja con el paso06 que el repo ya prepara.

## Ejemplos publicados y ruta de aprendizaje

No apareció ningún artículo con la combinación exacta del proyecto: SiN de 400 nm, add-drop, pulsos oscuros a 1550 nm y cladding acuoso. Tampoco se confirmó en texto completo ninguno que diga "Lumerical MODE/FDE + LLE". El indicio más fuerte es Kim et al. 2017, que según un fragmento calcularon los índices modales con Lumerical, sin verificar en el texto completo. Los ejemplos útiles se agrupan en cinco frentes:

- **Puerto drop:** [Wang et al. 2013](https://doi.org/10.1364/OE.21.022441) y [2016](https://doi.org/10.1364/OE.24.010890), con la [tesis de P.-H. Wang (Purdue, 2016)](https://engineering.purdue.edu/~fsoptics/thesis/Wang__Pei-Hsun_PhD.pdf).
- **Dispersión normal y pulsos oscuros:** [Xue et al. 2015](https://doi.org/10.1038/nphoton.2015.137) (con LLE + AMX), [Xue et al. 2017](https://doi.org/10.1002/lpor.201600276) (eficiencia de conversión de ~30 % con pulsos oscuros), [Fülöp et al. 2018](https://doi.org/10.1038/s41467-018-04046-6), [Nazemosadat et al. 2021](https://doi.org/10.1103/PhysRevA.103.013513), [Kim et al. 2019](https://doi.org/10.1364/OL.44.004475) y [Lihachev et al. 2022](https://doi.org/10.1038/s41467-022-29431-0). [Anderson et al. 2022](https://doi.org/10.1038/s41467-022-31916-x) cubre el caso β₂ ≈ 0.
- **SiN delgado:** [Kim et al. 2017](https://doi.org/10.1038/s41467-017-00491-x) y [Sabouri et al. 2019](https://doi.org/10.1109/CLEOE-EQEC.2019.8872841).
- **Bombeo pulsado:** [Obrzud 2017](https://doi.org/10.1038/nphoton.2017.140), [Malinowski 2017](https://doi.org/10.1063/1.4983113), [Anderson 2021](https://doi.org/10.1364/OPTICA.403302) y [Xu 2021](https://doi.org/10.1364/OL.413585).
- **Supercontinuo en guía de SiN:** [Johnson 2015](https://doi.org/10.1364/OL.40.005117), [Epping 2015](https://doi.org/10.1364/OE.23.019596), [Porcel 2017](https://doi.org/10.1364/OE.25.001542) y [Rebolledo-Salgado 2022](https://doi.org/10.1364/OE.450987).

En sensado, la refractometría de volumen con un solitón Kerr en SiN acuoso no tiene antecedente publicado encontrado. Lo más cercano es interrogar un MZI con un peine externo, con un límite de detección de 3.70×10⁻⁷ RIU ([Knoerzer et al. 2019](https://doi.org/10.1364/OE.27.021532)), y el peine en un microtoroide sumergido en agua ([Choi, Gin y Su 2022](https://doi.org/10.1364/OE.451631)).

Para aprender, la ruta de las notas avanza de lo general a lo práctico:

1. [Kippenberg et al. 2018](https://doi.org/10.1126/science.aan8083).
2. [Pasquazi et al. 2018](https://doi.org/10.1016/j.physrep.2017.08.004), la revisión más completa.
3. [Chembo 2016](https://doi.org/10.1515/nanoph-2016-0013) y [Hansson y Wabnitz 2016](https://doi.org/10.1515/nanoph-2016-0012), ambos de acceso abierto y comparando LLE e Ikeda.
4. [Coen et al. 2013](https://doi.org/10.1364/OL.38.000037), [Coen y Erkintalo 2013](https://doi.org/10.1364/OL.38.001790) y [Chembo y Menyuk 2013](https://doi.org/10.1103/PhysRevA.87.053852), para la derivación.
5. pyLLE como práctica ([artículo](https://arxiv.org/pdf/1903.10441)).
6. [Gaeta et al. 2019](https://doi.org/10.1038/s41566-019-0358-x), [Chang et al. 2022](https://doi.org/10.1038/s41566-021-00945-1) y [Kovach et al. 2020](https://doi.org/10.1364/AOP.376924), con tablas de n₂ por material.

Para la GNLSE, Dudley RMP 2006 y el [libro de Dudley y Taylor](https://doi.org/10.1017/CBO9780511750465). Las tesis más alineadas son la de [Helgason (Chalmers, 2020, licenciatura)](https://research.chalmers.se/en/publication/519027), sobre dispersión normal en Si₃N₄, y la de [J. Liu (EPFL, 2020)](https://infoscience.epfl.ch/record/279965). No se encontró ningún curso abierto estructurado sobre microcombs, ni ningún webinar de Ansys sobre el tema.

## Lo que no está verificado y cómo cerrarlo

| Punto | Estado en las notas | Cómo cerrarlo |
|---|---|---|
| Factores de la LLE normalizada (8 en f², argumento del sech, ζ_max = π²f²/8) | Escritos de memoria | Cotejar con el suplemento de Herr 2014 y con Kippenberg 2018 |
| Umbral add-drop P_th = κ³ħω₀/(8g₀κ_ex1) y su discrepancia ~1.5 con Kippenberg 2004 | Derivación propia; fórmula de 2004 citada de memoria | Cotejar con Kippenberg 2004/2018 y comprobar con la LLE numérica (inicio de la MI) |
| Conversión n₂↔χ⁽³⁾ | **Inferencia:** Lumerical usa n₂ = χ⁽³⁾Z₀/(2n₀²) ([Ansys, Kerr](https://optics.ansys.com/hc/en-us/articles/360041718634-Kerr-effect-on-Gaussian-beam-propagation)); Boyd da n₂ = 3χ⁽³⁾/(4n₀²ε₀c). Con n₂ = 2.4×10⁻¹⁹ y n₀ = 1.99 salen 5.0×10⁻²¹ y 3.4×10⁻²¹ m²/V²: **factor 3/2** | Medir la fase no lineal frente a la potencia en una guía recta corta en varFDTD |
| "Chi3/Chi2 needs non-zero chi2" | Foro, solo fragmento; contradice el ejemplo oficial | Usar Chi3 Raman Kerr con α = 1, o probar Chi3/Chi2 con χ⁽²⁾ = 0 frente a un χ⁽²⁾ mínimo |
| Kerr en NL_RING del cluster | Requiere 2026 R1.3 | Inspeccionar las propiedades del elemento en la v261 instalada |
| NLSE_WGD y FIBER en la v202 | NLSE_WGD ausente; FIBER probable | Abrir la librería de elementos de INTERCONNECT v202 |
| n₂ del SiN y del agua, dn/dT | n₂ = 2.4×10⁻¹⁹ coincide con Ikeda 2008; agua 2.7×10⁻²⁰ sin verificar; dn/dT recordados | Extraerlos de Ikeda 2008, Arbabi 2013 y Kovach 2020 |
| Kim 2017 "usó Lumerical" | Fragmento de ResearchGate | Leer la sección de métodos |
| Cifras del preprint 2604.19913 y 85 % de transferencia en Wang 2016 | Solo fragmentos de búsqueda | Leer el texto completo |

## Conclusión

La pregunta "¿cómo simulo χ⁽³⁾ en mi anillo con Lumerical?" se responde mejor invirtiéndola. Lumerical es el **generador de parámetros** (D_int, γ, κ, Q) y el **banco de calibración** (varFDTD corto, FIBER y NLSE_WGD). La física dinámica vive en dos códigos Python de un centenar de líneas cada uno: una LLE add-drop y la GNLSE ya escrita. Esa arquitectura hace casi irrelevante la diferencia entre la v202 y la v261. Lo único que el cluster añade de verdad es la verificación de Kerr en NL_RING y el FDTD 3D lineal del anillo completo. El cuello de botella real no es el software, sino que los pasos FDE de `seccion_v1` todavía no se han corrido.

La implicación más útil es de diseño. El mismo anillo no puede ser a la vez un buen refractómetro acuoso (Q ≈ 10⁴) y una fuente de peine Kerr: el umbral escala como 1/Q², y entre Q = 10⁴ y Q = 10⁶ hay un factor 10⁴. Un proyecto coherente separa las dos funciones. El anillo sensor se estudia en régimen lineal, con la LLE como cota de potencia y con el efecto térmico del agua como el verdadero sesgo no lineal. La no linealidad demostrable se lleva a una guía recta de dispersión normal (supercontinuo por SPM más wave breaking) o a un anillo comparativo de alto Q con cladding de óxido. Usar el peine para sensar en volumen sería original, porque no se encontró ningún antecedente, pero hoy no es viable con este dispositivo.

## Referencias

Estado: [VERIFICADO] = DOI comprobado en Crossref según las notas, la lista previa del proyecto (`referencias-no-lineal-SiN.txt`) o una consulta hecha para este informe; [NO VERIFICADO] = sin DOI o sin comprobación en Crossref.

**Páginas oficiales de Ansys Optics (Knowledge Base)**

- Advanced and custom optical material models in FDTD and MODE — https://optics.ansys.com/hc/en-us/articles/360034394734
- Nonlinear and gain methodology — https://optics.ansys.com/hc/en-us/articles/360041727474
- Flexible Material Plugin Framework — https://optics.ansys.com/hc/en-us/articles/360034915213
- Nonlinear optics – list of examples — https://optics.ansys.com/hc/en-us/articles/360043165194
- Ring resonator – optical bistability — https://optics.ansys.com/hc/en-us/articles/360041723954
- Four wave mixing (varFDTD) — https://optics.ansys.com/hc/en-us/articles/360041718794
- Four wave mixing with Kerr nonlinear material — https://optics.ansys.com/hc/en-us/articles/360041718694
- Kerr effect on Gaussian beam propagation — https://optics.ansys.com/hc/en-us/articles/360041718634
- Soliton propagation in a homogeneous medium — https://optics.ansys.com/hc/en-us/articles/360041718614
- Soliton in an SOI waveguide — https://optics.ansys.com/hc/en-us/articles/360042190173
- Spontaneous Four-Wave Mixing (SFWM) Microring Resonator Photon Source — https://optics.ansys.com/hc/en-us/articles/15100783091731
- Supercontinuum generation in photonic crystal fiber — https://optics.ansys.com/hc/en-us/articles/27638850917267
- FDE Mode List and Deck — https://optics.ansys.com/hc/en-us/articles/360034396734
- Dispersion analysis of SOI waveguide — https://optics.ansys.com/hc/en-us/articles/360042304954
- Sweep analysis for dispersion calculations — https://optics.ansys.com/hc/en-us/articles/1500006208582
- frequencysweep (script) — https://optics.ansys.com/hc/en-us/articles/360034925153
- NLSE Waveguide (NLSE_WGD) — https://optics.ansys.com/hc/en-us/articles/7945837183763
- Optical Fiber (FIBER) — https://optics.ansys.com/hc/en-us/articles/360036108194
- Pulse broadening from linear and nonlinear dispersion in an optical fiber — https://optics.ansys.com/hc/en-us/articles/360042819393
- Optical Nonlinear Ring Modulator (NL_RING) — https://optics.ansys.com/hc/en-us/articles/43036851200403
- Nonlinear Waveguide (WGD) — https://optics.ansys.com/hc/en-us/articles/360036618713
- Double Bus Ring Resonator (RING) — https://optics.ansys.com/hc/en-us/articles/360036618833
- Alphabetical list of all primitive elements — https://optics.ansys.com/hc/en-us/articles/360036106974
- Getting started with running FDTD on GPU — https://optics.ansys.com/hc/en-us/articles/17518942465811
- Notas de versión: 2025 R2.1 — https://optics.ansys.com/hc/en-us/articles/43598583744915 · 2026 R1.3 — https://optics.ansys.com/hc/en-us/articles/53916763140499 · 2023 R1.1 — https://optics.ansys.com/hc/en-us/articles/13659084854163 · 2022 R1.2 — https://optics.ansys.com/hc/en-us/articles/5218682727827
- Foro Ansys Learning Forum (no oficial; solo fragmentos): hilos 295376, 367386, 422961 y 169850 — https://innovationspace.ansys.com/forum/?p=295376

**Repositorios y software**

- pyLLE — https://github.com/gregmoille/pyLLE (sin mantenimiento desde 2026-08-26) · PyPI pyLLE 4.1.2
- PyCORe — https://github.com/ElKosto/PyCORe · Lugiato-Lefever_Equation_Solver — https://github.com/LuisAngelMendozaVelasco/Lugiato-Lefever_Equation_Solver · pycombs — https://github.com/PIC-Group-Adelaide-University/pycombs · Microcomb-simulation-LLE-solver — https://github.com/CaitlinEMurray/Microcomb-simulation-LLE-solver · kerr_comb_simulator — https://github.com/miceks/kerr_comb_simulator · pyGLLE — https://github.com/omelchert/pyGLLE · inverseLLE — https://github.com/ErwanLucas/inverseLLE
- gnlse-python — https://github.com/WUST-FOG/gnlse-python (docs: https://gnlse.readthedocs.io; arXiv:2110.00298 y Zenodo 10.5281/zenodo.6495720 [NO VERIFICADO en Crossref])
- Luna.jl — https://github.com/LupoLab/Luna.jl · PyNLO — https://github.com/pyNLO/PyNLO · SCGBookCode — https://github.com/jtravs/SCGBookCode

**Teoría LLE, Ikeda y revisiones**

- Lugiato & Lefever, PRL 58, 2209 (1987). doi:10.1103/PhysRevLett.58.2209 [VERIFICADO]
- Ikeda, Opt. Commun. 30, 257 (1979). doi:10.1016/0030-4018(79)90090-7 [VERIFICADO]
- Herr et al., Nat. Photon. 8, 145 (2014). doi:10.1038/nphoton.2013.343 [VERIFICADO]
- Herr et al., Nat. Photon. 6, 480 (2012). doi:10.1038/nphoton.2012.127 [VERIFICADO]
- Coen, Randle, Sylvestre, Erkintalo, Opt. Lett. 38, 37 (2013). doi:10.1364/OL.38.000037 [VERIFICADO]
- Coen & Erkintalo, Opt. Lett. 38, 1790 (2013). doi:10.1364/OL.38.001790 [VERIFICADO]
- Chembo & Menyuk, PRA 87, 053852 (2013). doi:10.1103/PhysRevA.87.053852 [VERIFICADO]
- Chembo & Yu, PRA 82, 033801 (2010). doi:10.1103/PhysRevA.82.033801 [VERIFICADO]
- Chembo, Nanophotonics 5, 214 (2016). doi:10.1515/nanoph-2016-0013 [VERIFICADO]
- Godey et al., PRA 89, 063814 (2014). doi:10.1103/PhysRevA.89.063814 [VERIFICADO]
- Hansson & Wabnitz, JOSA B 32, 1259 (2015). doi:10.1364/JOSAB.32.001259 [VERIFICADO]
- Hansson & Wabnitz, Nanophotonics 5, 231 (2016). doi:10.1515/nanoph-2016-0012 [VERIFICADO]
- Hansson, Modotto & Wabnitz, Opt. Commun. 312, 134 (2014). doi:10.1016/j.optcom.2013.09.017 [VERIFICADO]
- Barashenkov & Smirnov, PRE 54, 5707 (1996). doi:10.1103/PhysRevE.54.5707 [VERIFICADO]
- Kippenberg, Gaeta, Lipson, Gorodetsky, Science 361, eaan8083 (2018). doi:10.1126/science.aan8083 [VERIFICADO]
- Pasquazi et al., Phys. Rep. 729, 1 (2018). doi:10.1016/j.physrep.2017.08.004 [VERIFICADO]
- Gaeta, Lipson, Kippenberg, Nat. Photon. 13, 158 (2019). doi:10.1038/s41566-019-0358-x [VERIFICADO]
- Chang, Liu, Bowers, Nat. Photon. 16, 95 (2022). doi:10.1038/s41566-021-00945-1 [VERIFICADO]
- Kovach et al., Adv. Opt. Photon. 12, 135 (2020). doi:10.1364/AOP.376924 [VERIFICADO]
- Lugiato, Prati, Gorodetsky, Kippenberg, Phil. Trans. R. Soc. A 376, 20180113 (2018). doi:10.1098/rsta.2018.0113 [VERIFICADO]
- Herr, Gorodetsky, Kippenberg, cap. en *Nonlinear Optical Cavity Dynamics* (Wiley, 2015). doi:10.1002/9783527686476.ch6 [VERIFICADO]; Coen, Erkintalo et al., mismo libro. doi:10.1002/9783527686476.ch2 [VERIFICADO]

**Umbral, dinámica de solitones y efectos térmicos**

- Kippenberg, Spillane, Vahala, PRL 93, 083904 (2004). doi:10.1103/PhysRevLett.93.083904 [VERIFICADO]
- Matsko et al., PRA 71, 033804 (2005). doi:10.1103/PhysRevA.71.033804 [VERIFICADO]
- Ji et al., Optica 4, 619 (2017). doi:10.1364/OPTICA.4.000619 [VERIFICADO]
- Ji et al., APL Photonics 6, 071101 (2021). doi:10.1063/5.0057881 [VERIFICADO]
- Levy et al., Nat. Photon. 4, 37 (2010). doi:10.1038/nphoton.2009.259 [VERIFICADO]
- Guo et al., Nat. Phys. 13, 94 (2017). doi:10.1038/nphys3893 [VERIFICADO]
- Jaramillo-Villegas et al., Opt. Express 23, 9618 (2015). doi:10.1364/OE.23.009618 [VERIFICADO]
- Lucas et al., Nat. Commun. 8, 736 (2017). doi:10.1038/s41467-017-00719-w [VERIFICADO]
- Carmon, Yang, Vahala, Opt. Express 12, 4742 (2004). doi:10.1364/OPEX.12.004742 [VERIFICADO]
- Stone et al., PRL 121, 063902 (2018). doi:10.1103/PhysRevLett.121.063902 [VERIFICADO]
- Joshi et al., Opt. Lett. 41, 2565 (2016). doi:10.1364/OL.41.002565 [VERIFICADO]
- Li et al., Optica 4, 193 (2017). doi:10.1364/OPTICA.4.000193 [VERIFICADO]
- Arbabi & Goddard, Opt. Lett. 38, 3878 (2013). doi:10.1364/OL.38.003878 [VERIFICADO]
- Ikeda et al., Opt. Express 16, 12987 (2008). doi:10.1364/OE.16.012987 [VERIFICADO]
- Tan et al., Appl. Phys. Lett. 96, 061101 (2010). doi:10.1063/1.3299008 [VERIFICADO]
- Moss et al., Nat. Photon. 7, 597 (2013). doi:10.1038/nphoton.2013.183 [VERIFICADO]
- Liu et al., Nat. Commun. 12, 2236 (2021). doi:10.1038/s41467-021-21973-z [VERIFICADO]
- Helgason et al., Nat. Photon. 17, 992 (2023). doi:10.1038/s41566-023-01280-3 [VERIFICADO]
- Bao et al., Opt. Lett. 39, 6126 (2014). doi:10.1364/OL.39.006126 [VERIFICADO]; Yi et al., Opt. Lett. 41, 3419 (2016). doi:10.1364/OL.41.003419 [VERIFICADO]
- Agua dn/dT y absorción, arXiv:1710.03605 [NO VERIFICADO, sin DOI de revista]

**Add-drop, dispersión normal, SiN delgado y bombeo pulsado**

- Wang et al., "Drop-port study…", Opt. Express 21, 22441 (2013). doi:10.1364/OE.21.022441 [VERIFICADO]. (La DOI 10.1364/OE.22.012148 que citaba una de las notas es la fe de erratas.)
- Wang et al., Opt. Express 24, 10890 (2016). doi:10.1364/OE.24.010890 [VERIFICADO]
- Xue et al., Nat. Photon. 9, 594 (2015). doi:10.1038/nphoton.2015.137 [VERIFICADO]
- Xue et al., Laser Photon. Rev. 9, L23 (2015). doi:10.1002/lpor.201500107 [VERIFICADO]
- Xue et al., Laser Photon. Rev. 11, 1600276 (2017). doi:10.1002/lpor.201600276 [VERIFICADO]
- Xue, Qi, Weiner, Nanophotonics 5, 244 (2016). doi:10.1515/nanoph-2016-0016 [VERIFICADO]
- Liu et al., Optica 1, 137 (2014). doi:10.1364/OPTICA.1.000137 [VERIFICADO]
- Lobanov et al., Opt. Express 23, 7713 (2015). doi:10.1364/OE.23.007713 [VERIFICADO]
- Parra-Rivas et al., PRA 93, 063839 (2016). doi:10.1103/PhysRevA.93.063839 [VERIFICADO]
- Helgason et al., Nat. Photon. 15, 305 (2021). doi:10.1038/s41566-020-00757-9 [VERIFICADO]
- Fülöp et al., Nat. Commun. 9, 1598 (2018). doi:10.1038/s41467-018-04046-6 [VERIFICADO]
- Nazemosadat et al., PRA 103, 013513 (2021). doi:10.1103/PhysRevA.103.013513 [VERIFICADO]
- Kim, B. Y. et al., Opt. Lett. 44, 4475 (2019). doi:10.1364/OL.44.004475 [VERIFICADO]
- Lihachev et al., Nat. Commun. 13, 1771 (2022). doi:10.1038/s41467-022-29431-0 [VERIFICADO]
- Anderson et al., Nat. Commun. 13, 4764 (2022). doi:10.1038/s41467-022-31916-x [VERIFICADO]
- Kim, S. et al., Nat. Commun. 8, 372 (2017). doi:10.1038/s41467-017-00491-x [VERIFICADO] (el uso de Lumerical [NO VERIFICADO])
- Sabouri et al., CLEO/Europe-EQEC 2019. doi:10.1109/CLEOE-EQEC.2019.8872841 [VERIFICADO]
- Obrzud, Lecomte, Herr, Nat. Photon. 11, 600 (2017). doi:10.1038/nphoton.2017.140 [VERIFICADO]
- Malinowski et al., APL Photonics 2, 066101 (2017). doi:10.1063/1.4983113 [VERIFICADO]
- Anderson et al., Optica 8, 771 (2021). doi:10.1364/OPTICA.403302 [VERIFICADO] (la DOI .418848 no existe)
- Xu et al., Opt. Lett. 46, 512 (2021). doi:10.1364/OL.413585 [VERIFICADO]
- Brasch et al., Science 351, 357 (2016). doi:10.1126/science.aad4811 [VERIFICADO]
- Jang et al., Opt. Lett. 39, 5503 (2014). doi:10.1364/OL.39.005503 [VERIFICADO]
- Pfeiffer et al., Optica 4, 684 (2017). doi:10.1364/OPTICA.4.000684 [VERIFICADO]
- Okawachi et al., Opt. Lett. 36, 3398 (2011). doi:10.1364/OL.36.003398 [VERIFICADO]
- Karpov et al., PRL 116, 103902 (2016). doi:10.1103/PhysRevLett.116.103902 [VERIFICADO]
- Erkintalo & Coen, Opt. Lett. 39, 283 (2014). doi:10.1364/OL.39.000283 [VERIFICADO]
- Wang, Zhou, Yu, IEEE JSTQE 32(3), 2100107 (2026). doi:10.1109/JSTQE.2026.3659816 [VERIFICADO]
- Grudinin et al., arXiv:1612.00820 [NO VERIFICADO] · Wang et al., arXiv:2604.19913 [NO VERIFICADO] · arXiv:2404.01577 y arXiv:2601.04047 [NO VERIFICADO]

**Software (artículos), GNLSE y supercontinuo**

- Moille, Li, Lu, Srinivasan, J. Res. NIST 124, 124012 (2019). doi:10.6028/jres.124.012 [VERIFICADO]
- Moille et al., Nat. Commun. (2021). doi:10.1038/s41467-021-27469-0 [VERIFICADO]
- Hult, J. Lightwave Technol. 25, 3770 (2007). doi:10.1109/JLT.2007.909373 [VERIFICADO]
- Lægsgaard, Opt. Express 15, 16110 (2007). doi:10.1364/OE.15.016110 [VERIFICADO]
- Melchert & Demircan, SoftwareX (2022). doi:10.1016/j.softx.2022.101232 [VERIFICADO]
- Dudley, Genty, Coen, Rev. Mod. Phys. 78, 1135 (2006). doi:10.1103/RevModPhys.78.1135 [VERIFICADO]
- Dudley & Taylor (eds.), *Supercontinuum Generation in Optical Fibers* (CUP, 2010). doi:10.1017/CBO9780511750465 [VERIFICADO]
- Johnson et al., Opt. Lett. 40, 5117 (2015). doi:10.1364/OL.40.005117 [VERIFICADO]
- Epping et al., Opt. Express 23, 19596 (2015). doi:10.1364/OE.23.019596 [VERIFICADO]
- Porcel et al., Opt. Express 25, 1542 (2017). doi:10.1364/OE.25.001542 [VERIFICADO]
- Rebolledo-Salgado et al., Opt. Express 30, 8641 (2022). doi:10.1364/OE.450987 [VERIFICADO]

**Sensado**

- Choi, Gin, Su, Opt. Express 30, 8690 (2022). doi:10.1364/OE.451631 [VERIFICADO]
- Knoerzer et al., Opt. Express 27, 21532 (2019). doi:10.1364/OE.27.021532 [VERIFICADO]
- Diakonov et al., npj Nanophotonics 1 (2024). doi:10.1038/s44310-024-00047-0 [VERIFICADO]
- Suh et al., Science 354, 600 (2016). doi:10.1126/science.aah6516 [VERIFICADO]; Dutt et al., Sci. Adv. 4, e1701858 (2018). doi:10.1126/sciadv.1701858 [VERIFICADO]; Yu et al., Nat. Commun. 9, 1869 (2018). doi:10.1038/s41467-018-04350-1 [VERIFICADO]
- Tan, T. et al., Nat. Commun. 12, 6716 (2021). doi:10.1038/s41467-021-26740-8 [VERIFICADO]
- Sun et al., Adv. Opt. Photon. 15, 86 (2023). doi:10.1364/AOP.470264 [VERIFICADO]; Yao et al., eLight 4, 19 (2024). doi:10.1186/s43593-024-00071-9 [VERIFICADO]; Shu et al., Photonics Insights 3, R09 (2024). doi:10.3788/PI.2024.R09 [VERIFICADO]
- Tomasetig et al., ACS Meas. Sci. Au (2025) [NO VERIFICADO] — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12921590/
- arXiv:2603.10273 (2026, sensado con el estado del peine) [NO VERIFICADO] · SPIE Proc. 12871, 1287109 (2024), doi:10.1117/12.3003240 [NO VERIFICADO]
