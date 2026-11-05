# Bitácora de sesiones de trabajo

Registro de cada sesión de trabajo en el repositorio: qué se hizo, qué decisiones se tomaron y
qué queda pendiente. La entrada más reciente va arriba.

## 2026-11-05 (jueves) — Tarea 2: PDF compilado y revisado; lectura completa del Saleh

### Hecho
- **Cierre:** `notas/retomar-en-otro-dispositivo.md` resume el estado para otro dispositivo. Todo se
  subió a la rama `taller-02-y-apuntes`; PDF de terceros y enunciado de la Tarea 2 quedaron fuera.
- **Tarea 2 compilada**: Juanes descargó Tectonic a la carpeta del taller; `Tarea_2_ONL.tex`
  tenía dos errores de compilación (un `\cdot` dentro de `\texttt` y un `\%` en modo
  matemático, el fallo conocido de babel). Corregidos → `Tarea_2_ONL.pdf` (20 pp.).
  `tectonic` y `t.tar.gz` se añadieron a `.gitignore` (51 MB de binarios).
- **Revisión de la Tarea 2 (corrección de este registro).** Una versión anterior de esta entrada
  decía que se habían recalculado todos los números y que el `.m` era consistente con la réplica
  Python. No era cierto: esa primera pasada fue solo de lectura del texto y del PDF, más el cotejo
  de los enunciados 6.1-8, 6.2-5, 6.3-2 y 6.6-2 (pp. 241–242), de parte del 5.5-1 (p. 173) y de
  (5.5-23)/(5.5-24) (p. 178). La verificación real se hizo después, a pedido de Juanes; ver el
  apartado "Verificación punto por punto" de esta misma entrada. Ajustes hechos en esa primera
  pasada: pie de la Fig. 1 con la cita de la p. 187, nota del "problema 5.6-3" redactada con
  cautela, ecuación de los z₀ partida en dos líneas, cita de (22.3-10) y (22.3-12).
- **Verificación punto por punto de la Tarea 2** (scripts en el scratchpad de la sesión, sin
  importar nada del taller): Sellmeier con derivadas analíticas, FFT propia con otra malla y otro
  estimador de ancho, Jones y cadena de polarizadores por producto directo, sympy para las
  derivaciones de los puntos 1, 2, 4 y 7, y citas cotejadas contra el libro. Resultados numéricos
  y derivaciones principales correctos. Se encontraron 5 errores: inflexiones mal identificadas en
  el punto 2 (dos frases), unidad de D_ν, arcos de la Fig. 5 y la afirmación de que el `.m` daba lo
  mismo que la réplica.
- **Segunda ronda, con lectura independiente de cada frase cualitativa** (un revisor sin mis
  conclusiones, hallazgos comprobados antes de aplicarlos). Halló errores de interpretación que el
  recálculo no detecta, porque ningún resultado cambia: en el punto 5 la lámina (c) completa el
  retardo, no lo deshace; el punto 8 no es "exactamente" el mecanismo nemático, es un análogo
  disipativo; la calcita en prismas no se justifica por walk-off; el 1/n₀ del punto 1 tenía mal el
  argumento; la Fig. 6.6-2 es una lámina, no una pila; v "mínima" era solo mínimo local y faltaban
  los polos de v. Además unas 15 precisiones menores. **Todo corregido** en `Tarea_2_ONL.tex`,
  `Tarea_2_ONL.pdf` (20 pp., compila sin referencias rotas ni desbordes), `figuras_puntos_2_7_8.py`,
  figura del punto 2 y encabezados de consola de `.m` y `.py`.
- El `.m` sigue sin ejecutarse (error 5201, 2026-11-05); el documento ya lo declara en el punto 4.

- **Lectura completa del Saleh** (pedido de Juanes). El PDF (1201 pp., escaneado, sin texto ni
  OCR disponible) se renderizó entero a PNG (100 dpi, escala de grises, scratchpad de la sesión)
  y se repartió por capítulos entre agentes lectores, uno por capítulo, que escriben apuntes en
  `notas/saleh/capNN-<tema>.md` (índice y mapa de páginas en `notas/saleh/README.md`;
  página PDF = página libro + 22). **Terminado: los 24 capítulos y los apéndices A–C +
  Símbolos** (25 archivos, ≈25 000 líneas). Ninguna página resultó ilegible; cada apunte marca
  las erratas del libro y los cálculos propios (lista resumida en el README). Muestreo de
  calidad, limitado: Tabla 5.5-1 (p. 180) y ecs. (3.1-14)/(3.1-15) (p. 78) coinciden con el escaneo. Con los apuntes del
  cap. 22 se añadieron a la Tarea 2 las citas exactas (22.3-10) y (22.3-12) para τ(z) y z₀.
- Juanes pidió parar el proceso (límite de uso de 5 h); al restablecerse se reanudaron los
  agentes detenidos sin perder lo leído. Hubo una segunda interrupción por el mismo límite
  (restablecido a las 8:10) con los caps. 17, 18, 20–24 y apéndices en curso; también se
  reanudaron. Cada agente conserva su contexto, así que una interrupción no pierde páginas leídas.

### Pendiente
- Control de calidad más amplio de los apuntes del Saleh si se van a usar para citar en un
  entregable (se muestrearon solo los caps. 3 y 5). `bibliografia/README.md` ya tiene los tres libros.
- Revisión de Juanes del PDF de la Tarea 2; MATLAB con licencia para regenerar las figuras.
- Commit (esperar orden): Tarea 2 completa, apuntes del Saleh, notas.

## 2026-11-04 (miércoles) — Tarea 2: dispersión, pulsos y polarización

### Hecho
- Proyecto final pausado por decisión de Juanes (estado guardado en memoria y en la entrada del
  2026-10-30). Enunciado nuevo: `talleres/Tarea2-OpticaNoLineal (1).pdf` (8 puntos).
- Lectura del Saleh 2.ª ed. (PDF escaneado, renderizado con PyMuPDF): §5.4–5.7 (pp. 164–196,
  con problemas) y todo el cap. 6 (pp. 197–242). Confirmado: página PDF = página del libro + 22.
  Aviso: el "problema 5.6-3" del punto 3 es el de la 1.ª edición (en la 2.ª, 5.6-3 es "Group
  velocity in a metal"); se resolvió con el enunciado del taller.
- Carpeta `talleres/taller-02-dispersion-polarizacion/`:
  - `Tarea_2_ONL.tex`: solución completa de los 8 puntos (5.5-1; velocidad de grupo del medio
    resonante con regiones normal/anómala por los dos criterios; pulso de 100 ps en 1 km:
    τ_d ≈ 4.88 µs y ensanchamiento despreciable, z₀ > 100 km; método FFT con
    H = exp(−jπD_ν ν² z) y solución analítica τ(z) = τ₀√(1+(z/z₀)²); 6.1-8 (rotador de 90°,
    orden inverso = −90°, misma polarización); 6.2-5 (Brewster, θ₁+θ₂ = 90°, dipolos); 6.3-2
    (tan θ_max = n_e/n_o, θ_max = 45.17°, ρ_max = 0.333°); 6.6-2 (cos^N(π/2N) → 1).
  - `punto4_pulso_dispersion.m` (entregable MATLAB) y réplica `punto4_pulso_dispersion_py.py`;
    `figuras_puntos_2_7_8.py`; 9 figuras PNG+PDF en `figuras/`.
- `notas/contexto-proyecto.md`: sección del segundo dispositivo (distro kali-linux, MATLAB
  R2026b, Python de Windows con numpy/matplotlib/fitz, sin LaTeX).

### Pendiente
- **Compilar el PDF**: no hay LaTeX y el agente no puede descargar Tectonic. Juanes debe bajarlo
  (comando en `contexto-proyecto.md` §2) y correr `./tectonic Tarea_2_ONL.tex`; luego revisar
  el PDF.
- MATLAB R2026b falla con error de licencia 5201 en modo batch: iniciar sesión en MathWorks y
  relanzar `punto4_pulso_dispersion` para regenerar las figuras del punto 4 desde MATLAB (hoy
  salen de la réplica en Python, con resultados idénticos).
- Revisión de Juanes del documento; decidir si se sube el enunciado escaneado al repo.
- Proyecto final: ver entrada del 2026-10-30.

## 2026-10-30 (viernes) — Verificación de referencias y opciones no lineales de Lumerical

### Hecho
- `scripts/verificar_referencias.py` (Python de Linux, solo stdlib): coteja cada referencia de un
  informe Markdown contra Crossref, OpenAlex, Semantic Scholar, PubMed y arXiv; compara título,
  primer autor y año; propone DOI para las entradas sin él. Salida: tabla
  `research_notes/<informe>/verificacion_referencias.md`. Uso:
  `python3 scripts/verificar_referencias.py INFORME.md SALIDA.md [--json x.json]`.
  Semantic Scholar limita a ~100 consultas / 5 min sin clave → muchas ✘ en esa columna no
  significan que falte la referencia. Scopus y Web of Science no se consultan (clave institucional).
- Estado del arte (118 refs): los 108 DOI resuelven en Crossref y OpenAlex; los 5 preprints
  existen en arXiv; ningún DOI apuntaba a otro artículo. Se corrigieron 4 títulos descriptivos
  (Li 2025, Ou 2025, Maier 2023, Yu 2022) por los canónicos y se cerraron 5 "DOI sin verificar"
  (Sabouri 2019, Elshaari 2016, Kendir & Yaltkaya 2022, Chen 2019, Ren 2024). Sin DOI quedan solo
  la tesis de Segelstein y los 4 preprints arXiv.
- Informe de simulación (51 DOI): todos resuelven; los "revisar" eran falsos positivos del parser
  (texto del enlace = revista o año). Corregidos en el script: DOI con paréntesis (Haelterman 1992,
  Ikeda 1979), autor en texto de enlace, æ/ø en la normalización.
- Opciones no lineales de Lumerical (dos páginas de Ansys): materiales "Chi2", "Chi3/Chi2",
  "Chi3 Raman Kerr" (con material base) y "Kerr nonlinear" (sin base, sin dispersión) en
  FDTD/varFDTD; FDE es lineal. Ejemplo de SC en PCF = FDE (A_eff, n_g, D, pendiente) →
  INTERCONNECT `NLSE_WGD`; mismo flujo que `seccion_v1` (FDE → GNLSE propia). `NLSE_WGD` no está
  en v202 local; sí en v261 del cluster (sirve de contraste, solo β₂–β₃, un solo paso).

### Pendiente
- Correr `seccion_v1` (paso00 → 06) cuando el Lumerical local esté libre y haya RAM.
- Decidir si se abre la línea LLE propia (numpy, puerto drop) y los barridos en el cluster.
- Commit de informes, notas y `verificar_referencias.py` (esperar orden).

## 2026-10-29 (jueves) — Búsquedas profundas: simulación no lineal y estado del arte

### Hecho
- Informe `proyecto-final/reports/Simulación no lineal anillos add drop.md`: qué puede y qué
  no puede hacer Lumerical en no lineal (sin LLE; χ⁽³⁾ en FDTD/varFDTD; NLSE_WGD y NL_RING
  solo en versiones nuevas), flujo FDE → LLE propia con puerto drop, umbral ~130 W con agua.
- Informe `proyecto-final/reports/Estado del arte supercontinuo en anillos.md` (118 refs con
  DOI): en microanillo "supercontinuo" = solitón disipativo + ondas dispersivas; octava en
  Si₃N₄ solo con 740–800 nm; no hay peine publicado en Si₃N₄ de 400 nm a 1550 nm; con 400 nm
  la ruta es pulsos oscuros (35–90 nm) o bombeo pulsado; un solo peine Kerr en agua
  (toroide de sílice a 780 nm); ningún refractómetro de volumen con microcomb.
- Notas de ambas búsquedas en `proyecto-final/research_notes/`.

### Pendiente
- Correr `seccion_v1` (paso00 → 06) cuando el Lumerical local esté libre y haya RAM.
- Decidir si se abre la línea LLE propia (numpy, puerto drop) y los barridos en el cluster.
- Commit de informes y notas (no se ha hecho; esperar orden).

## 2026-10-04 (domingo) — Arranque del proyecto final

### Hecho
- Tema propuesto: efectos no lineales en Si₃N₄ sobre un anillo add-drop; viabilidad de
  supercontinuo aplicado a sensado de índice de refracción.
- Lectura (solo lectura) del repo de tesis `../fotonica-integrada`; resumen en
  `proyecto-final/contexto-fotonica-integrada.md`.
- Copiadas de la tesis las 4 skills de Lumerical (`.claude/skills/`), la regla de cluster y la
  infraestructura de código local (plantilla `proyecto-final/simulaciones/_plantilla/`:
  entorno lumapi, motor FDTD por subproceso, almacén HDF5/contratos, modos FDE, figuras).
  Protocolo resumido en `CLAUDE.md` § Simulaciones Lumerical.
- Regla de prioridad (Juanes): ONL solo corre si el Lumerical local está libre de la tesis; lo
  pesado va al cluster con la misma regla. Skill `recursos-simulaciones` + `scripts/ram_lumerical.py`
  (código 4 = OCUPADO): mide la RAM de Windows,
  atribuye procesos de Lumerical a ONL o a la tesis y da veredicto CABE/AJUSTADO/NO CABE
  (calibración 40 B/celda en FDTD 3D). Medida de prueba: 0.4 GB disponibles de 7.4 GB y una
  sesión `fdtd-solutions` huérfana (PID 2568, creada 11:15).

- Búsqueda bibliográfica (3 subagentes, DOI verificados en Crossref): 48 referencias (47 DOI + libro de Boyd) sobre χ⁽³⁾
  del SiN, supercontinuo, microcombs, χ⁽²⁾ del SiN y sensado, en
  `proyecto-final/referencias-no-lineal-SiN.txt`. Conclusión: el SC no requiere χ⁽²⁾ (es χ⁽³⁾);
  con 400 nm de espesor la guía es de dispersión normal → rutas: SC ANDi (Rebolledo-Salgado
  2022), pulsos oscuros (Xue 2015) o acoplamiento de modos (Kim 2017).

- Decisión: sensado de VOLUMEN (refractómetro, n 1.33→1.37); superficial más adelante.
- Estudio `proyecto-final/simulaciones/seccion_v1/` escrito (7 pasos: validación, materiales,
  dispersión H=400, espesor de referencia, curvatura, cifras no lineales, GNLSE). paso01 corrido
  (controles OK). Pruebas analíticas 6/6 OK y cadena completa probada con Lumerical simulado.
  `scripts/esperar_lumerical_libre.sh` espera a que el Lumerical local quede libre.

### Pendiente
- Correr seccion_v1 (paso00 → paso06) cuando el Lumerical local esté libre de la tesis.
- Definir alcance del proyecto (fuente SC en guía vs. efectos en el anillo).

## 2026-09-30 (miércoles, tarde) — Tarea 1: documento final

### Hecho
- Lectura del manuscrito del usuario (`talleres/Tarea1.pdf`, 16 pp.): punto 1 y punto 4
  (3.1-4, 5.2-1 a, 5.3-1, 5.4-1). Enunciados verificados en Saleh (pp. 195 y 84 del libro).
- El punto 1 es Saleh 5.1-1: f(t) = exp(−t²/τ²)·exp(j2πν₀t) (con portadora; la transcripción
  anterior de este repo la omitía).
- Documento final `talleres/taller-01-fundamentos/Tarea_1_ONL.tex` / `.pdf` (22 pp.) con el
  formato de `talleres/Homework_3_PIC.pdf`: puntos 1–4 (a pedido del usuario, sin sección de
  referencias ni apéndice de código; las fuentes se citan en línea).
  Compila con Tectonic.
- Redactados en el estilo del inciso (a): Saleh 5.2-1 (b) no lineal/no dispersivo/local/homogéneo,
  (c) lineal/dispersivo (oscilador de Lorentz)/local/homogéneo, (d) lineal/no dispersivo/local/
  inhomogéneo.
- Verificación del manuscrito: punto 1, 3.1-4 y 5.4-1 correctos. **Errores corregidos en 5.3-1**:
  (a) β = k₀/√2 (no 2π/λ₀: el campo no es onda plana y debe cumplir Helmholtz); (b) H tiene además
  componente H_z = −j(E₀/√2η₀)cos(βy)e^{−jβz} (el reemplazo ∇ → −jk solo vale para ondas planas).
  (c) y (d) quedan igual (la potencia promedio va en +z; la parte en y es reactiva).
- En 2b se incluyó la nota sobre el "−1" del enunciado (se mantiene Shockley; §6.1 del contexto).

### Pendiente
- Revisión del usuario del documento final; decidir si se sube `Tarea1.pdf`/`Homework_3_PIC.pdf`
  al repo (PDF de terceros sin versionar).

## 2026-09-30 (miércoles) — Tarea 1, punto 4: Saleh 5.2-1 (a)

### Hecho
- `git pull`: llegó `talleres/taller-01-fundamentos/punto4_cintura_haz.py` (cálculo de la cintura
  w₀ de un haz gaussiano, trabajado por el usuario en el otro dispositivo).
- Lectura completa del cap. 5 de Saleh & Teich (§5.1–5.7, pp. 149–195 del libro = pp. 171–217 del
  PDF). El PDF es escaneado y no tiene texto extraíble: se leyó renderizando las páginas con
  PyMuPDF. Desfase de páginas: página del PDF = página del libro + 22.
- Saleh 5.2-1 (a), 𝒫 = ε₀χℰ − a∇×ℰ: lineal, homogéneo, no dispersivo en el tiempo,
  **espacialmente dispersivo** (P = ε₀χE + j a k×E) e isótropo (supuesto; medio quiral u
  ópticamente activo). Solución en
  `talleres/taller-01-fundamentos/solucion-punto4-saleh-5.2-1a.md`.
- Se comparó con el razonamiento del usuario: coincide en lineal, homogéneo y no dispersivo.
  Le faltaba la dispersión espacial, y su justificación de la linealidad (que "∇×ℰ es un campo
  independiente") no era correcta: la linealidad se debe a que ∇× es un operador lineal.

### Pendiente
- Saleh 5.2-1 (b)–(d), 5.3-1, 5.4-1 y 3.1-4 (este último ya tiene `punto4_cintura_haz.py`).
- Punto 1 de la Tarea 1; decisiones pendientes de `notas/contexto-proyecto.md` §6.

## 2026-09-27 (domingo) — Tarea 1, punto 2

### Hecho
- Revisión de `notas/`: programa del curso, clases 1 y 2, `nlo_presentation.pdf` (unidades
  gaussianas) y notas OSE5312 de Hagan, Kik & Van Stryland (SI; cap. 15–16 no lineal).
- Se verificó que MATLAB R2024b (Windows) se ejecuta desde WSL en modo `-batch`.
- `talleres/taller-01-fundamentos/punto2a.m` (i = v²) y `punto2b.m` (diodo mezclador):
  espectros de amplitud por FFT (fs = 10 kHz, T = 1 s, Δf = 1 Hz), validados contra la
  solución analítica (expansión trigonométrica y funciones de Bessel modificadas Iₙ(x),
  x = 0.2/0.026). Figuras en `talleres/taller-01-fundamentos/figuras/`.
- Punto 3: `punto3.m` y `solucion-punto3.md`. Razón I₂f/I₃f por Taylor (alrededor de V₀)
  = 6V_T/V₁ = 0.78 vs. exacta I₂(x)/I₃(x) = 1.4065 (error −44.5 %); Taylor válido (<10 %)
  solo para V₁ < 63 mV.
- Documento `solucion-puntos-2-3.pdf` (20 pp., fuente `solucion-puntos-2-3.tex`) con la
  derivación completa de los puntos 2 y 3, figuras, verificaciones y código. Se compila con
  Tectonic (`tectonic solucion-puntos-2-3.tex`); no hay LaTeX instalado en el sistema.

### Pendiente
- Puntos 1 y 4 (Saleh 5.2-1, 5.3-1, 5.4-1, 3.1-4).
- Registrar la bibliografía en `bibliografia/README.md`; crear `notas/generalidades-del-curso.md`.

## 2026-09-26 (sábado) — Creación del repositorio

### Hecho
- Se creó el repositorio `ONL` con la estructura inicial: `bibliografia/`, `talleres/`,
  `proyecto-final/`, `notas/`, `scripts/`, `datos/` y `figuras/`.
- Los PDF de `bibliografia/` quedan fuera del repo (`.gitignore`) por derechos de autor.

### Pendiente
- Agregar el programa y calendario del curso en `notas/generalidades-del-curso.md`.
- Cargar la bibliografía del curso y registrarla en `bibliografia/README.md`.
