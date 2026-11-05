# Herramientas de código abierto y flujo computacional: mode solver (Lumerical) → LLE (anillos) → GNLSE (guías)

Fecha de la investigación: 2026-10-26. La actividad de los repositorios se consultó en la API de GitHub (campo `pushed_at`) ese mismo día. Los DOI se verificaron en api.crossref.org, salvo los marcados.

## 1. pyLLE (NIST): qué hace, entradas y salidas, backend, add-drop y efectos térmicos, mantenimiento

### Takeaway
pyLLE resuelve la LLE en el dominio temporal con split-step Fourier. El núcleo numérico está en Julia y la interfaz en Python. Recibe como dispersión una tabla CSV de (número azimutal, frecuencia de resonancia), que puede venir de cualquier eigen-solver. Solo modela **un acoplamiento** (Qc, puerto de paso o *through*), sin puerto *drop*, sin efectos térmicos y sin Raman. Además, **su autor declaró en agosto de 2026 que ya no lo mantiene**.

### Cited Findings
- **Repositorio activo y estado.** El repo canónico es `gregmoille/pyLLE` (92 estrellas, último push 2026-08-26). El fork `usnistgov/pyLLE` está congelado desde 2023-09-16. El README dice textualmente: "Not maintained anymore, use it at your own risk and any bug fixing always welcome". Ese aviso se añadió en el commit del 2026-08-26 ("Update README with maintenance notice") — [GitHub gregmoille/pyLLE](https://github.com/gregmoille/pyLLE); [API GitHub](https://api.github.com/repos/gregmoille/pyLLE)
- **Versión publicada.** En PyPI, la última es `pyLLE 4.1.2` (2024-01-23). La v4.0.0 rehízo el núcleo: los parámetros pasan a ser atributos de objeto, el split-step se estabilizó para arrancar desde un solitón y se admite un número arbitrario de bombas — [PyPI pyLLE](https://pypi.org/pypi/pyLLE/json); [README](https://github.com/gregmoille/pyLLE)
- **Instalación.** Requiere Julia ≥ 1.8 con los paquetes HDF5, FFTW y LinearAlgebra; en Windows se instalan a mano con `Pkg.add`. Después se hace `pip install pyLLE`. Por defecto busca el binario de Julia en `/opt/bin/julia`; si está en otro sitio se indica con `solver.SolveTemporal(bin=...)` — [README](https://github.com/gregmoille/pyLLE)
- **Dependencias Python.** El código importa `h5py`, `plotly`, `prettytable`, `ipdb` y `matplotlib`, y lanza Julia mediante `subprocess`. El intercambio Python↔Julia se hace con archivos HDF5 (`ParamLLEJulia.h5`) — [código fuente _llesolver.py](https://github.com/gregmoille/pyLLE/blob/master/pyLLE/_llesolver.py)
- **Entradas del resonador (diccionario `res`).** `R` (radio), `Qi`, `Qc`, `γ` (W⁻¹m⁻¹) y `dispfile`, un CSV sin encabezado con columna 1 = orden azimutal entero y columna 2 = frecuencia de resonancia en Hz. Los números de modo solo tienen que ser monótonos con paso 1, porque la LLE trabaja en μ relativo a la bomba — [notebook TemporalDualPump.ipynb](https://github.com/gregmoille/pyLLE/blob/master/example/TemporalDualPump.ipynb); [Moille et al., J. Res. NIST 124, 124012 (2019), doi:10.6028/jres.124.012](https://pmc.ncbi.nlm.nih.gov/articles/PMC8325515/)
- **Entradas de la simulación (diccionario `sim`).**
  - `Pin` (lista, W) y `f_pmp` (lista, Hz).
  - `φ_pmp` y `δω` (`None` marca la bomba que se barre).
  - `Tscan` (duración en round-trips).
  - `μ_sim` (rango de modos, p. ej. [−220, 220]) y `μ_fit`.
  - `δω_init`, `δω_end` (rampa lineal de desintonía en rad/s) y `num_probe`.
  - `DKS_init` opcional, para sembrar un solitón.
  - Ejemplo del notebook: R = 23 µm, Qi = Qc = 1e6, γ = 3.2, Pin = 140 mW a 283 THz, Tscan = 0.7e6 round-trips, μ = ±220.
  - Fuente: [notebook](https://github.com/gregmoille/pyLLE/blob/master/example/TemporalDualPump.ipynb)
- **Tratamiento de la dispersión.** La dispersión se trata en el dominio de la frecuencia, sin truncarla en una serie de Taylor. `GetDint` ajusta D_int con un spline cúbico que se puede extrapolar. El artículo advierte: "Extrapolation can result in ripples in the integrated dispersion". Para obtener las frecuencias recomienda "a Maxwell's equation eigenvalue solver", sin nombrar uno en concreto — [Moille et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC8325515/)
- **Acoplamiento y salidas.** El backend de Julia calcula `κext = ω0/Qc·tR` y `κ0 = ω0/Q0·tR` y usa `dt = 1` round-trip, de modo que el número de pasos es Nt = Tscan. Las salidas, en `solver.sol`, son `Acav` (campo intracavidad), `Ewg` (campo en la guía), `Pcomb` y la desintonía en cada *probe*. Es decir, existe un único puerto de salida (bus/paso) — [ComputeLLE.jl](https://github.com/gregmoille/pyLLE/blob/master/pyLLE/ComputeLLE.jl); [notebook](https://github.com/gregmoille/pyLLE/blob/master/example/TemporalDualPump.ipynb)
- **Costo de referencia.** El artículo simula 244 modos (μ = −74…170) de un anillo de Si₃N₄ con R = 23 µm, Qi = Qc = 1e6, γ = 1.55 W⁻¹m⁻¹ y 150 mW a 191 THz. Los tiempos fueron 11 min con pyLLE, 19 min con Matlab 2018a y 45 min con Python puro, en un MacBook Pro 2017 (i5 a 3.1 GHz, 16 GB). Incluye también un solver estacionario Newton-Raphson cuya precisión "remains questionable" — [Moille et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC8325515/)
- **Lo que no cubre.** El artículo no trata efectos térmicos, Raman ni puerto *drop* — [Moille et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC8325515/)
- **Uso en investigación.** El grupo NIST lo ha usado en trabajos sobre Si₃N₄ con dispersión de banda ancha, entre ellos Moille et al., Nat. Commun. (2021), doi:10.1038/s41467-021-27469-0 (DOI verificado), y Nature 624 (2023) — [README, sección "Works using pyLLE"](https://github.com/gregmoille/pyLLE)

### Inferences
- **Usar pyLLE en un anillo add-drop.** La LLE de un solo acoplador sirve si se pone `Qc` = Q de acoplamiento del bus *through* y se absorbe el acoplamiento al *drop* en la pérdida efectiva (1/Qi_eff = 1/Qi + 1/Qc,drop). El espectro en el *drop* se obtiene después en post-proceso, a partir del campo intracavidad `Acav`, como E_drop = √κ_drop·A. Es la misma lógica que la del puerto de paso. Esto es una deducción del modelo de modos acoplados; pyLLE no lo hace por sí solo.
- **Entorno local (Windows/WSL con 7.4 GB).** Correr ~441 modos durante ~1e6 round-trips es viable: el caso de referencia, con 244 modos, tardó del orden de 10 min. El CSV de dispersión se escribe directamente desde Lumerical (§4).
- **Clúster.** Python 3.13 sin `h5py` no sirve para pyLLE tal cual. Habría que instalar `h5py` (`pip --user` o un venv), Julia y sus paquetes. Si no se puede, conviene una LLE propia en numpy, que es corta (véase §2).

### Gaps
- No encontré documentación HTML viva: https://gregmoille.github.io/pyLLE/ devuelve 404.
- No hay ningún benchmark de pyLLE con 1024–4096 modos.

## 2. Otros solvers LLE (Python/MATLAB/Julia): qué existe y si está mantenido

### Takeaway
No existe ningún solver LLE "estándar" que se mantenga activamente y que incluya add-drop y efectos térmicos. Lo que hay son códigos pequeños, mayormente académicos, de split-step Fourier. Varios siguen activos en 2025–2026, pero tienen pocas estrellas. En la práctica, la mayoría de los grupos escriben su propio split-step de unas 100 líneas sobre el formalismo de Chembo-Menyuk / Coen-Erkintalo.

### Cited Findings
- **`ElKosto/PyCORe`** (Python; rama PyCORe++ en C con FFTW o un solver adaptativo de Numerical Recipes). Simula un microresonador χ(3) simple, trae tests y tiene licencia MIT. Último push 2024-10-20, 15 estrellas — [GitHub PyCORe](https://github.com/ElKosto/PyCORe)
- **`LuisAngelMendozaVelasco/Lugiato-Lefever_Equation_Solver`** (Jupyter). Último push 2026-08-23, 29 estrellas — [GitHub](https://github.com/LuisAngelMendozaVelasco/Lugiato-Lefever_Equation_Solver)
- **`PIC-Group-Adelaide-University/pycombs`**, solver LLE interactivo en Python. Último push 2026-10-13, 2 estrellas — [GitHub](https://github.com/PIC-Group-Adelaide-University/pycombs)
- **`CaitlinEMurray/Microcomb-simulation-LLE-solver`**, split-step Fourier simétrico en MATLAB. Último push 2025-06-09 — [GitHub](https://github.com/CaitlinEMurray/Microcomb-simulation-LLE-solver)
- **`miceks/kerr_comb_simulator`**, aplicación gráfica en MATLAB con LLE y mapa de Ikeda. Último push 2022-12-13, 39 estrellas — [GitHub](https://github.com/miceks/kerr_comb_simulator)
- **`omelchert/pyGLLE`**, LLE generalizada en Python. Último push 2022-09-22 — [GitHub](https://github.com/omelchert/pyGLLE)
- **`ErwanLucas/inverseLLE`**, optimización genética de la dispersión del resonador sobre LLE, en MATLAB (grupo EPFL). Último push 2023-08-29 — [GitHub](https://github.com/ErwanLucas/inverseLLE)
- **`rox1k/comb`**, simulador de peines Kerr en MATLAB. Abandonado (2014) — [GitHub](https://github.com/rox1k/comb)
- **Formalismos de base:**
  - Coen, Randle, Sylvestre y Erkintalo modelan peines de una octava con una LLE generalizada de campo medio, con cálculos "much faster than with any other technique" — [Opt. Lett. 38, 37 (2013), doi:10.1364/OL.38.000037](https://arxiv.org/abs/1211.1697)
  - Chembo y Menyuk, LLE espaciotemporal para resonadores WGM — doi:10.1103/PhysRevA.87.053852 (verificado en Crossref)
  - Escalado universal: Coen y Erkintalo, Opt. Lett. 38, 1790 (2013), doi:10.1364/OL.38.001790 (verificado)
- **LLE frente a ecuaciones de modos acoplados.** En el modelo de modos acoplados, el término Kerr es una triple suma y el costo crece de forma cúbica con el número de modos. Un peine de unos cientos de modos ya exige mucho tiempo de cálculo. La LLE con FFT escala como N log N — [Hansson, Modotto y Wabnitz, arXiv:1307.3428](https://arxiv.org/pdf/1307.3428)
- **Efectos térmicos.** En la literatura se modelan acoplando a la LLE una ecuación térmica de primer orden, por ejemplo Joshi et al., "Thermally controlled comb generation and soliton modelocking in microresonators", Opt. Lett. 41, 2565 (2016), doi:10.1364/OL.41.002565 (verificado en Crossref). No encontré un paquete abierto mantenido que lo traiga integrado.
- **"gmmlle".** No encontré ningún repositorio con ese nombre.

### Inferences
- Para el proyecto (anillo add-drop de SiN, 1 bomba), lo más robusto y transparente es:
  - Escribir una LLE propia en numpy (split-step simétrico, D_int tabulado, rampa de desintonía), validada contra pyLLE o contra soluciones analíticas (umbral de MI en P_th; solitón sech²).
  - Añadir κ_drop y, si hace falta, una ecuación térmica.
  - Con eso corre en el clúster con Python 3.13 y solo numpy/scipy.

### Gaps
- No pude verificar el código MATLAB de los suplementos de Herr et al. (Nat. Photon. 8, 145 (2014), doi:10.1038/nphoton.2013.343, DOI verificado). No encontré un enlace público al código.
- No encontré ningún solver LLE en Julia publicado como paquete independiente.

## 3. Solvers GNLSE para guías bus/alimentación (supercontinuo): β(ω) arbitraria, A_eff(ω) y Raman

### Takeaway
- **gnlse-python (WUST-FOG)** es la opción más directa en Python. Acepta dispersión a partir de n_eff(λ) tabulado y γ(ω) a partir de A_eff(ω), y trae modelos Raman de fibra. Está estable pero inactivo desde 2023.
- **Luna.jl** es el más activo (push 2026-10-23). Su interfaz simple `prop_gnlse` usa coeficientes β_n; los modos y la dispersión personalizados requieren la interfaz de bajo nivel.
- **PyNLO (original)** está estancado. Su versión 0.1.2 en PyPI es de 2018 y el README dice que fue probado en Python 2.7.
- **Código del libro de Dudley y Taylor (RK4IP en MATLAB)**: es la referencia didáctica.

### Cited Findings
- **gnlse-python (WUST-FOG).**
  - Basado en el RK4IP en MATLAB de Dudley y Taylor, con integradores adaptativos de SciPy.
  - Dispersión: operador por expansión de Taylor o "computed from effective refractive indices".
  - γ: constante, o `NonlinearityFromEffectiveArea`, que modela A_eff dependiente de la frecuencia según Lægsgaard (2007).
  - Raman: modelos de Blow-Wood, Lin-Agrawal y Hollenbeck-Cantrell.
  - Extensión multimodo desde la versión 1.1.0.
  - Instalación: `pip install gnlse`. Documentación en https://gnlse.readthedocs.io.
  - Ejemplos: `test_Dudley.py`, `test_raman.py`, `test_dispersion.py`, `test_nonlinearity.py`.
  - Fuente: [GitHub WUST-FOG/gnlse-python](https://github.com/WUST-FOG/gnlse-python)
- **gnlse-python, estado.** PyPI tiene `gnlse 2.0.0` (2022-04-27, requires_python ≥ 3.7); el último push al repo es de 2023-01-13. Se cita como el preprint arXiv:2110.00298 [NO VERIFICADO en Crossref; el DOI de DataCite 10.48550/arXiv.2110.00298 resuelve en doi.org] y como el DOI de software Zenodo 10.5281/zenodo.6495720 (resuelve en doi.org; no está en Crossref) — [PyPI gnlse](https://pypi.org/pypi/gnlse/json); [API GitHub](https://api.github.com/repos/WUST-FOG/gnlse-python)
- **Base teórica de A_eff(ω) en la GNLSE.** Lægsgaard, "Mode profile dispersion in the generalised nonlinear Schrödinger equation", Opt. Express 15, 16110 (2007), doi:10.1364/OE.15.016110 (verificado en Crossref).
- **Luna.jl.**
  - Implementa la UPPE y sus aproximaciones (GNLSE).
  - `prop_gnlse(γ, flength, βs; λ0, τfwhm, power, pulseshape, λlims, trange)`, donde βs es un vector de coeficientes de Taylor.
  - Una "low-level interface" permite "custom waveguide modes". El README advierte que los ejemplos de bajo nivel "are not actively maintained and are not guaranteed to run".
  - Incluye Raman en gases moleculares y vidrios, e infraestructura de barridos de parámetros en serie o en paralelo.
  - Requiere Julia ≥ 1.9 (`] add Luna`).
  - Último push 2026-10-23, 134 estrellas.
  - Fuente: [GitHub LupoLab/Luna.jl](https://github.com/LupoLab/Luna.jl); [README](https://raw.githubusercontent.com/LupoLab/Luna.jl/master/README.md)
- **PyNLO (pyNLO/PyNLO).**
  - Incluye χ(3) con RK4IP adaptativo y χ(2) (DFG).
  - La dispersión de fibra se da por coeficientes β2…βn.
  - El README dice que "requires Python 2"; el soporte de Python 3 está "work-in-progress".
  - PyPI: 0.1.2 (2018-10-09). Último push 2023-10-17.
  - Fuente: [GitHub PyNLO](https://github.com/pyNLO/PyNLO); [PyPI](https://pypi.org/pypi/pynlo/json)
  - Hay forks recientes, como `peter-chang62/pynlo` (push 2026-10-11, 2 estrellas) y `julia-17-white/SiN_pynlo` ("Chi-3 soliton propagation through SiN waveguides", 2026-09-23), sin documentación propia verificada — [API GitHub](https://api.github.com/search/repositories?q=pynlo+in:name)
- **Código del libro de Dudley y Taylor.** Es el código MATLAB del capítulo 3 (Travers, Frosz y Dudley): una función GNLSE con RK4IP y un script de ejemplo. Está en `jtravs/SCGBookCode` (46 estrellas, 2020, "(un)maintained", escrito para docencia) — [GitHub jtravs/SCGBookCode](https://github.com/jtravs/SCGBookCode). Método RK4IP: Hult, J. Lightwave Technol. 25, 3770 (2007), doi:10.1109/JLT.2007.909373 (verificado). Caso de validación clásico: Dudley, Genty y Coen, Rev. Mod. Phys. 78, 1135 (2006), doi:10.1103/RevModPhys.78.1135 (verificado), que Luna reproduce en su ejemplo `prop_gnlse` — [README de Luna](https://github.com/LupoLab/Luna.jl)
- **GNLStools.py.** Melchert y Demircan, módulo Python de GNLSE con distintos modelos de ruido de entrada, SoftwareX (2022), doi:10.1016/j.softx.2022.101232 (verificado en Crossref).
- **Ejemplo de SC en SiN.** En arXiv:1606.00568 (SiN rico en silicio), la GVD se calcula con elementos finitos y el supercontinuo se promedia sobre 50 realizaciones de ruido — [arXiv:1606.00568](https://arxiv.org/pdf/1606.00568)

### Inferences
- **Lumerical → GNLSE.** gnlse-python acepta directamente n_eff(λ) y A_eff(λ), así que es la vía más corta para pasar de Lumerical a la GNLSE de la guía bus. Solo necesita numpy/scipy, por lo que corre en el clúster sin h5py.
- **Raman en SiN.** Los modelos Raman incluidos están parametrizados para sílice. Para Si₃N₄ (LPCVD), el Raman suele despreciarse en la literatura de peines y SC en SiN, o se pone f_R ≈ 0. No obstante, no encontré en esta búsqueda una fuente que lo cuantifique (véase Gaps).

### Gaps
- No verifiqué qué parámetros Raman se usan para Si₃N₄; hace falta una búsqueda específica, por ejemplo "silicon nitride Raman fraction f_R supercontinuum".
- No confirmé en la documentación de Luna.jl la API exacta para importar β(ω) tabulado; la documentación misma dice que "is not yet complete".
- No pude identificar el estado de un "PyNLO v1" mantenido por NIST.

## 4. Acoplamiento con Lumerical MODE/FDE: n_eff(λ) → β(ω), D_int(μ), A_eff, γ; cruces de modos

### Takeaway
En FDE, `frequencysweep` genera un D-card "frequencysweep" con n_eff, v_g, D, etc. en función de f, que se lee con `getdata` (también vía lumapi). Con n_eff(ω) de la sección **curvada** (radio de curvatura = R) se construyen las resonancias del anillo, ω_μ = m·c/(n_eff(ω_μ)·R), y con ellas D_int y el CSV que espera pyLLE. Los cruces de modos aparecen como saltos o ramas en n_eff(f). Se manejan con el seguimiento de modo (track selected mode), con un barrido fino y revisando la polarización y la fracción TE.

### Cited Findings
- **Barrido de frecuencia.** `frequencysweep` "Performs a frequency sweep using the current settings within the frequency analysis tab. Produces a D-CARD called 'frequencysweep' that contains dispersion, effective index, and other data as a function of frequency". El ejemplo oficial selecciona el modo 1 con `selectmode(1)`, activa el seguimiento y "detailed dispersion", y lee `D`/`f_D`. Para varios modos lee `neff` y `f` de `FDE::data::frequencysweep` — [Ansys Optics: frequencysweep](https://optics.ansys.com/hc/en-us/articles/360034925153-frequencysweep)
- **Recomendaciones de configuración.**
  - Para seguir un solo modo, "track selected mode" funciona mejor con unos 3 modos de prueba.
  - Ansys recomienda el ajuste multicoeficiente de materiales (MCM), porque las discontinuidades en el índice producen discontinuidades artificiales en las derivadas.
  - Un empleado de Ansys señala que el script de ejemplo antiguo calcula la derivada segunda con diferencias simples, y que las versiones nuevas de FDE la mejoraron.
  - Fuente: [foro Ansys Innovation Space](https://innovationspace.ansys.com/forum/?p=169850); [Ansys course: Special Script Commands for FDE Data](https://innovationspace.ansys.com/courses/courses/ansys-lumerical-fde-analyzing-results/lessons/special-script-commands-for-working-with-fde-data-lesson-4/)
- **Formato de entrada de pyLLE.** pyLLE requiere precisamente (m, f_m) en Hz y ajusta D_int con un spline, de modo que no hace falta truncar la dispersión en una serie de Taylor — [Moille et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC8325515/). Otro trabajo sobre peines visibles usa "the exact dispersion of the microring resonator instead of approximating dispersion with limited polynomial terms", con un split-step Fourier normalizado — [arXiv:1705.10848](https://arxiv.org/pdf/1705.10848)
- **Ansys no tiene ejemplo de peines Kerr.** No encontré ningún ejemplo oficial de Ansys "Kerr comb / LLE" ni "supercontinuum in SiN waveguide". Las búsquedas no devolvieron páginas de optics.ansys.com sobre esos temas.

### Inferences
Receta práctica, derivada de lo anterior y de la definición estándar de D_int:
1. **Barrido en FDE.** Hacer el barrido de frecuencia de la sección del anillo con *bend radius* = R activado, con MCM y unos 50–200 puntos en el rango espectral del peine (p. ej. 1.2–2.2 µm). Guardar `neff(f)`, `vg(f)` y, para cada f, A_eff (resultado `mode effective area` / `loss` del modo, o calculado desde E con la definición de Lin/Agrawal, A_eff = (∫|E|²)²/∫|E|⁴ sobre el núcleo).
2. **Resonancias del anillo.** Para cada entero m, resolver m = n_eff(ω)·ω·R/c por interpolación y obtener ω_m.
3. **D_int.** Calcular D1 = (ω_{m0+1} − ω_{m0−1})/2 y D_int(μ) = ω_{m0+μ} − ω_{m0} − D1·μ. Escribir el CSV (m, f_m) para pyLLE.
4. **Parámetro no lineal.** γ = n2·ω0/(c·A_eff(ω0)). Para Si₃N₄ se usa típicamente n2 ≈ 2.4×10⁻¹⁹ m²/W [valor típico de la literatura, no verificado en esta búsqueda].
5. **Para la GNLSE de la guía bus.** Usar la sección **recta**: β(ω) = n_eff·ω/c, y entregar n_eff(λ) y A_eff(λ) a gnlse-python.
6. **Cruces de modos.** Aparecen como saltos en n_eff o en D_int, o como cambios de la fracción de polarización. Conviene barrer con paso fino y modo seguido. Si se quiere estudiar su efecto en el peine, se puede añadir un desplazamiento local a D_int(μ) en los modos afectados.
- **Alternativa.** Obtener las frecuencias propias del anillo completo con FDTD 3D (apodización + *harminv*/FFT). Es mucho más caro y solo se justifica para validar unos pocos puntos de D_int.

### Gaps
- No obtuve la lista exacta de resultados del D-card "frequencysweep" en Lumerical 2026R1 (por ejemplo, si incluye A_eff por frecuencia); está por verificar en la documentación local.
- No encontré un tutorial público que muestre de principio a fin "Lumerical FDE → pyLLE".

## 5. Costo computacional: LLE en un portátil frente a clúster, y viabilidad de FDTD χ(3) del anillo completo

### Takeaway
- **LLE en un portátil.** Unos cientos de modos y unos 10⁵–10⁶ round-trips tardan del orden de 10 minutos (pyLLE: 244 modos, 11 min en un portátil de 2017).
- **Cuándo usar el clúster.** Para barridos de desintonía × potencia × geometría, que son trivialmente paralelos, o para modelos multimodo.
- **FDTD χ(3) del anillo completo.** Recién se demostró en 2026 con GPU: más de 1.3×10⁹ celdas y unos 6×10⁶ pasos para 400 ps, en un anillo de 50 µm con Q cargado de solo 1.8×10⁴. No es viable con Lumerical en CPU ni para los Q ~10⁵–10⁶ reales.

### Cited Findings
- **pyLLE.** 244 modos tardaron 11 min (Julia), 19 min (Matlab) y 45 min (Python puro) en un MacBook Pro 2017 con 16 GB — [Moille et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC8325515/). En el ejemplo actual, 441 modos y Tscan = 7×10⁵ round-trips con paso dt = 1 round-trip — [notebook](https://github.com/gregmoille/pyLLE/blob/master/example/TemporalDualPump.ipynb); [ComputeLLE.jl](https://github.com/gregmoille/pyLLE/blob/master/pyLLE/ComputeLLE.jl)
- **LLE generalizada.** Permite modelar peines de una octava "on a consumer grade computer", con cálculos mucho menos intensivos que los métodos previos — [Coen et al. 2013 (arXiv:1211.1697)](https://arxiv.org/abs/1211.1697)
- **Modos acoplados.** El costo crece de forma cúbica con el número de modos; con unos cientos de modos ya es muy lento — [arXiv:1307.3428](https://arxiv.org/pdf/1307.3428)
- **FDTD de onda completa (Tidy3D).**
  - Anillo de R = 50 µm con más de 1.3 mil millones de puntos de malla en 3D, unos 6 millones de pasos de tiempo y más de 400 ps simulados, con paso espacial mínimo de λ/30.
  - Unas 2 GPU-horas A100 por caso, aunque los tres regímenes comparados (solitón, solitón respirante y patrón de Turing) se corrieron en una configuración **2D**.
  - Q_loaded = 1.8×10⁴; validación cruzada contra la LLE.
  - Paper: Wang, Zhou y Yu, "Full-Wave Simulation of Kerr Comb Generation Using FDTD", IEEE JSTQE 32(3), 2100107 (2026), doi:10.1109/JSTQE.2026.3659816 (verificado en Crossref).
  - La fuente es un blog del proveedor y no da benchmark en CPU.
  - Fuente: [Flexcompute blog](https://hs.flexcompute.com/blog/acomputational-milestone-in-full-wave-kerr-comb-simulation-using-gpu-accelerated-fdtd)
- **Luna.jl.** Incluye una interfaz para barridos de parámetros en serie o en paralelo — [README de Luna](https://github.com/LupoLab/Luna.jl)

### Inferences
- **Tiempo de fotón.** Con Q ≈ 10⁶ a 1550 nm, τ_ph = Q/ω ≈ 0.8 ns. Para llegar al estado estacionario hacen falta varios ns a cientos de ns de evolución: ≥ 10³–10⁵ round-trips de un anillo de ~100 µm. Eso es órdenes de magnitud más que los 400 ps del FDTD de Tidy3D, que ya necesitó Q bajo (1.8×10⁴) y GPU. Por tanto, FDTD χ(3) del anillo completo **no es viable** en Lumerical local (7.4 GB) ni de forma práctica en el clúster CPU. En FDTD solo debe usarse la parte lineal: espectro add-drop, Q, FSR y validación de D_int.
- **Reparto de cargas sugerido.**
  - **Local:** FDE (barridos de frecuencia de una sección: minutos, pocos GB), LLE individual (128–1024 modos) y GNLSE de una guía (2¹²–2¹⁴ puntos espectrales, segundos a minutos).
  - **Clúster:** barridos de malla (desintonía × potencia × ancho/espesor de la guía), estadística de ruido (decenas de realizaciones de SC, como las 50 de arXiv:1606.00568) y FDTD 3D lineal del anillo completo.
- **Rejilla y precisión.** Un número de modos de potencia de 2 (512–4096) acelera la FFT. Para la LLE lo crítico es cubrir todo el ancho de banda del peine (incluida la onda dispersiva) con D_int bien muestreado en lugar de extrapolado (advertencia de pyLLE sobre ondulaciones).

### Gaps
- No encontré benchmarks publicados de LLE con 2048–4096 modos ni números de GNLSE en SiN (tiempo frente a N_t); son estimaciones propias.
- No encontré ninguna fuente que cuantifique la RAM o el tiempo de un FDTD χ(3) del anillo completo en Lumerical (CPU).
- No encontré cuadernos públicos con la cadena completa "mode solver → LLE → espectro del peine" o "mode solver → GNLSE → SC" para Si₃N₄ con Lumerical. Los ejemplos más cercanos son el CSV de dispersión de pyLLE (`RW1000_H430.csv`, un anillo de SiN cuyo origen en un mode solver no se documenta) y los `test_*.py` de gnlse-python.
