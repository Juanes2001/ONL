# Capítulo 23 — Optical Interconnects and Switches (Saleh & Teich, 2.ª ed.)

Páginas del libro 1016–1071 (PDF 1038–1093). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 23.
Notación del libro: dependencia temporal $e^{j\omega t}$, $j=\sqrt{-1}$; campos reales en caligráfica
($\mathcal{E}$), amplitudes complejas en negrita ($\mathbf{T}$, $\mathbf{T}_{\ell m}$); transmitancia
de potencia $\mathcal{T}$, reflectancia $\mathcal{R}$, fineza $\mathcal{F}$, coeficiente de acoplamiento
$\mathcal{C}$. Unidades SI. Cada anotación cita la página del libro (p.). Las ecuaciones recuadradas por
el libro se marcan con **[recuadro]**.

---

## Resumen del capítulo

El capítulo presenta los tres bloques de "enrutamiento" de luz en sistemas distribuidos
(comunicaciones, procesamiento de información, cómputo): las **interconexiones ópticas** (conexiones
fijas e independientes de los atributos del haz, §23.1), los **enrutadores pasivos** (la salida la
dicta un atributo del haz: longitud de onda, polarización, fase o intensidad, §23.2) y los
**conmutadores fotónicos** (conexiones reconfigurables por una señal de control externa: conmutadores
espaciales, en el dominio de la longitud de onda, en el dominio del tiempo y de paquetes, §23.3).
Cierra con las **compuertas ópticas** basadas en biestabilidad (§23.4): un elemento no lineal más
realimentación produce histéresis entrada–salida, que sirve como memoria (flip-flop), umbral, amplificador
o compuerta AND. Hay un hilo claro de óptica no lineal: los enrutadores por intensidad y los conmutadores
todo-ópticos usan el efecto Kerr ($n=n_0+n_2 I$) en interferómetros Mach–Zehnder, lazos Sagnac (NOLM,
TOAD), acopladores direccionales no lineales y solitones; los convertidores de longitud de onda usan XGM,
XPM, SHG/DFG y FWM; y los dispositivos biestables dispersivos son Fabry–Perot o Mach–Zehnder con medio
Kerr. Los enrutadores por longitud de onda (FBG, filtros de película delgada, microanillos, MZI en
cascada, WGR/AWG) son la base de los multiplexores WDM y de los OADM, directamente relacionados con el
anillo add-drop del proyecto final.

---

## Secciones

### Introducción del capítulo (p. 1017–1018)

- Un haz óptico tiene varios **atributos**: posición (espacio), dirección, longitud de onda
  (frecuencia), intensidad, fase, polarización, tiempo (pulsos) y código (secuencia de pulsos)
  — Fig. 23.0-1 (p. 1017). Uno se modula para transportar la señal; otro (p. ej. λ) sirve para
  marcar señales distintas en el mismo haz (**multiplexación**).
- Fig. 23.0-2 (p. 1017): sistema que dirige cada uno de $M$ haces de entrada a uno o varios de $N$
  puertos de salida. Definiciones:
  - **Interconexión (interconnect)**: las conexiones son fijas e independientes de la naturaleza de
    los haces.
  - **Elemento de enrutamiento pasivo**: un atributo del haz (p. ej. λ) dicta el puerto de salida.
  - **Conmutador espacial (space switch)**: las conexiones se reconfiguran con una señal de control
    externa.
- Tipos de conmutadores (p. 1017): **space-domain switches**, **time-domain switches** (de una
  ranura temporal a otra), **wavelength-domain switches** (de un canal λ a otro), **packet
  switches** (controlados por una dirección incluida en cada paquete).
- Plan (p. 1017–1018): §23.1 interconexiones (espacio libre, PLC, fibra); §23.2 enrutadores pasivos
  (DEMUX/MUX/OADM); §23.3 conmutadores espaciales fotónicos (ON–OFF, 1×2, tecnologías
  electro-óptica, SOA, cristal líquido, MEMS, todo-óptica, más conmutadores temporales y de
  paquetes); §23.4 compuertas lógicas ópticas con dispositivos biestables (conmutadores con memoria).
- Nota histórica (p. 1016): el desarrollo de interconexiones y conmutadores fotónicos comenzó en los
  años 80 en Bell Laboratories (AT&T, 1925 → Lucent 1996 → Alcatel 2006). "Varias décadas de
  investigación en cómputo óptico digital no han dado productos competitivos con las computadoras
  electrónicas" (p. 1017), pero dejaron tecnologías de compuertas lógicas ópticas e interconexiones.

---

### 23.1 Optical Interconnects (p. 1018)

**Resumen.** En electrónica las interconexiones son cables, coaxiales o pistas; en fotónica son guías
de onda con acopladores integrados o de fibra, o haces en espacio libre dirigidos por microlentes o
elementos difractivos. Los haces de luz pueden cruzarse sin interferir mutuamente (en medio lineal),
cosa imposible con electrones (p. 1018). Fig. 23.1-1 (p. 1019) muestra configuraciones típicas:
(a) uno-a-uno: shift/Banyan, reversal/crossover, crossover, perfect shuffle; (b) uno-a-muchos o
muchos-a-uno: T-coupler, fan-out (multicast), fan-in; (c) muchos-a-muchos: acoplador 3 dB, star
coupler, projection.

**Matriz de interconexión (p. 1018–1019).** Para interconexiones lineales coherentes, el campo en el
puerto de salida $\ell$ ($\ell=1,\dots,N$) es una superposición de los campos de entrada
$U^{(i)}_m$, $m=1,\dots,M$:

$$U^{(o)}_\ell=\sum_{m=1}^{M} T_{\ell m}\,U^{(i)}_m \qquad (23.1\text{-}1)$$

con pesos complejos $\{T_{\ell m}\}$ que definen la **matriz de interconexión** $\mathbf{T}$.
Ejemplo: el acoplador 2×2 de 3 dB (Fig. 23.1-1c) es

$$\mathbf{T}=\frac{1}{\sqrt{2}}\begin{bmatrix}1 & j\\ j & 1\end{bmatrix} \qquad (23.1\text{-}2)$$

idéntico a un divisor de haz ideal (Sec. 7.1A). Interconexiones en cascada → producto de matrices
(Sec. 7.1A). Como la luz es coherente, las fases importan (efectos interferométricos redistribuyen
potencia). Si la luz es **incoherente**, se suman potencias (Sec. 11.3B):

$$P^{(o)}_\ell=\sum_{m=1}^{M}|\mathbf{T}_{\ell m}|^2 P^{(i)}_m \qquad (23.1\text{-}3)$$

(para el acoplador 3 dB todos los elementos de $|\mathbf{T}_{\ell m}|^2$ valen 1/2).

**Especificaciones de acopladores (p. 1019)**, razones de potencia en dB $[=-10\log(1/\text{razón})]$:
- **Pérdida de inserción**: transmitancia puerto a puerto; ideal 0 dB.
- **Razón de división (splitting ratio)**: potencia en un puerto de salida / potencia total de salida;
  3 dB para un acoplador 3 dB ideal.
- **Diafonía (crosstalk)**: potencia indeseada en un puerto / potencia de entrada dirigida a otro puerto.
- **Pérdida en exceso (excess loss)**: potencia total de salida / potencia total de entrada.

**Interconexiones no recíprocas: aisladores y circuladores (p. 1020).**
- Una interconexión es **recíproca** si al invertir el sentido de transmisión (salidas→entradas) la
  matriz es la misma; si no, es **no recíproca**.
- **Aislador**: enlace 1×1 unidireccional (Fig. 23.1-2a), como un diodo o válvula de una vía
  (Sec. 6.4B). Se especifica por pérdida de inserción (transmitancia directa, dB) y **aislamiento
  inverso** (transmitancia inversa, dB).
- Interconexiones multipuerto no recíprocas: cuando un puerto es a la vez transmisor y receptor, se
  designa por número de puertos. Fig. 23.1-2(b,c): 3 puertos con enlaces unidireccionales (para
  dúplex, Fig. 23.1-2e); Fig. 23.1-2(d): 4 puertos, paralelo hacia adelante y cruzado hacia atrás.
- **Circulador**: 3 o más puertos conectados por enlaces unidireccionales en el mismo sentido;
  el circulador de 4 puertos (Fig. 23.1-3) equivale a la interconexión de Fig. 23.1-2(d). Uso en
  OADM (Sec. 23.2A, Fig. 23.2-3).

#### 23.1A Free-Space Refractive and Diffractive Interconnects (p. 1021)

- Componentes convencionales (espejos, lentes, prismas) como interconexiones. Un sistema de imagen
  bien diseñado conecta hasta $1000\times1000$ puntos independientes por mm² del plano objeto con
  otros tantos en el plano imagen: eléctricamente harían falta un millón de canales conductores
  sin cruces por mm² (p. 1021).
- Fig. 23.1-4 (p. 1021): un prisma desvía rayos y produce reversal/crossover; dos prismas, perfect
  shuffle (usado en ordenamiento y en la FFT); una lente hace fan-in/fan-out/reversal; un divisor de
  haz con dos lentes = acoplador direccional; una varilla de vidrio = star coupler; óptica
  astigmática (lente cilíndrica) = projection (cada fila → un punto). Pueden miniaturizarse con
  **micro-óptica** (mini divisores de haz, lentes, varillas GRIN, prismas, filtros, redes).
- **Redes de fase (phase gratings) y hologramas** (p. 1021–1022). Una red de fase delgada tiene
  transmitancia periódica de módulo unidad; la más simple es
  $\mathrm{t}(x,y)=\exp[-j2\pi(\nu_x x+\nu_y y)]$ con frecuencias espaciales $\nu_x,\nu_y$. Un haz de
  longitud de onda λ se inclina ángulos $\sin^{-1}\lambda\nu_x\approx\lambda\nu_x$ y
  $\sin^{-1}\lambda\nu_y\approx\lambda\nu_y$ (con $\lambda\nu_x\ll1$, $\lambda\nu_y\ll1$; Secs. 2.4B,
  4.1A; Fig. 23.1-5). Un holograma generado por computadora con muchos segmentos de red de distintas
  frecuencias y orientaciones crea mapas de interconexión arbitrarios de alta densidad (Fig. 23.1-6).
- Si el segmento en $(x,y)$ tiene frecuencias $\nu_x(x,y)$, $\nu_y(x,y)$, el haz llega al plano de
  salida (a distancia $d$) en $(x',y')$ con

$$\frac{x'-x}{d}\approx\lambda\nu_x,\qquad \frac{y'-y}{d}\approx\lambda\nu_y \qquad (23.1\text{-}4)$$

  (ángulos pequeños). Dado el mapa deseado $(x,y)\to(x',y')$ se obtienen $\nu_x,\nu_y$ en cada
  posición. Uno-a-muchos: el elemento central de Fig. 23.1-6 es la superposición de dos armónicos,
  $\mathrm{t}(x,y)=\exp[-j2\pi(\nu_{x1}x+\nu_{y1}y)]+\exp[-j2\pi(\nu_{x2}x+\nu_{y2}y)]$, que divide el
  haz en dos partes iguales inclinadas $(\lambda\nu_{x1},\lambda\nu_{y1})$ y
  $(\lambda\nu_{x2},\lambda\nu_{y2})$; pesos distintos → interconexiones ponderadas (p. 1022).

- **EJERCICIO 23.1-1, Capacidad de interconexión (p. 1022–1023).** El producto espacio–ancho de banda
  de un holograma cuadrado de lado $a$ es $(Ba)^2$, con $B$ la máxima frecuencia espacial
  (líneas/mm). Mostrar que si el holograma dirige $L$ haces entrantes a $M$ direcciones, el
  producto $ML$ no puede superar $(Ba)^2$: **[recuadro]** $ML\le(Ba)^2$. *Pista*: análisis
  análogo a la Sec. 19.2C sobre interconexiones acusto-ópticas, Ec. (19.2-9). Pregunta adicional:
  ¿máximo número de interconexiones por mm² si $B=1000$ líneas/mm y cada punto de entrada se
  conecta con cada punto de salida? (Con $M=L$: $M^2\le(Ba)^2$ → $M\le Ba$; para $a=1$ mm,
  $M\le1000$ y hay $ML=10^6$ interconexiones por mm². Cálculo propio a partir del recuadro.)

- **Mapa de interconexión continuo (p. 1023).** Si los elementos de red son infinitesimales, se
  tiene una transformación geométrica de coordenadas definida por dos funciones continuas
  **[recuadro]**:

$$x'=\psi_x(x,y),\qquad y'=\psi_y(x,y) \qquad (23.1\text{-}5)$$

  Las frecuencias de la red varían continuamente, como en una señal FM (Fig. 23.1-7). Con
  transmitancia $\mathrm{t}(x,y)=\exp[-j\varphi(x,y)]$, las frecuencias locales (instantáneas) son

$$2\pi\nu_x=\frac{\partial\varphi}{\partial x},\qquad 2\pi\nu_y=\frac{\partial\varphi}{\partial y} \qquad (23.1\text{-}6)$$

  Sustituyendo en (23.1-4) **[recuadro]**:

$$\frac{\psi_x(x,y)-x}{d}=\frac{\lambda}{2\pi}\frac{\partial\varphi}{\partial x},\qquad
\frac{\psi_y(x,y)-y}{d}=\frac{\lambda}{2\pi}\frac{\partial\varphi}{\partial y} \qquad (23.1\text{-}7)$$

  Dos EDP cuya solución es la función de fase $\varphi(x,y)$ del holograma.

- **EJEMPLO 23.1-1, Mapa fan-in (p. 1024).** Todos los puntos $(x,y)$ van a $(x',y')=(0,0)$:
  $\psi_x=\psi_y=0$ en (23.1-7) → $\varphi(x,y)=-\pi(x^2+y^2)/\lambda d$, exactamente el desfase de
  una lente de distancia focal $d$ (Sec. 2.4B).
- **EJERCICIO 23.1-2, Mapa logarítmico (p. 1024).** Mostrar que la transformación
  $x'=\psi_x(x,y)=\ln x$ (23.1-8), $y'=\psi_y(x,y)=\ln y$ (23.1-9) se realiza con el holograma de fase

$$\varphi(x,y)=\frac{2\pi}{\lambda d}\Big(x\ln x-x-\tfrac12x^2+y\ln y-y-\tfrac12y^2\Big) \qquad (23.1\text{-}10)$$

  (Verificación: $\partial\varphi/\partial x=(2\pi/\lambda d)(\ln x-x)$, y (23.1-7) da
  $(\ln x-x)/d=(\lambda/2\pi)\,\partial\varphi/\partial x$ ✓.)
- **Holografía generada por computadora (p. 1024):** $\exp[-j\varphi(x,y)]$ se codifica con una
  función binaria (1 y 0, o 1 y −1), como el semitono de un periódico; se imprime en una máscara
  (transparencia) o se graban surcos en un sustrato (**surface-relief holography**).
- **Interconexiones dinámicas (reconfigurables) (p. 1024):** dispositivos acusto-ópticos o
  magneto-ópticos (menos puntos que con hologramas), o procesos no lineales como **mezcla de cuatro
  ondas en materiales fotorrefractivos**: dos ondas interfieren y crean una red de la que se refleja
  una tercera; el ángulo entre las dos ondas fija la frecuencia espacial de la red y por tanto la
  inclinación de la onda reflejada (Secs. 20.4 y 21.3E).

#### 23.1B Guided-Wave Interconnects (p. 1024)

- Implementación en circuitos planares de ondas de luz (**PLC**) con guías en LiNbO₃ o silicio
  (Sec. 8.5B), como las pistas metálicas en un circuito impreso. Fig. 23.1-8 (p. 1025):
  (a) T-coupler, (b) acoplador 3 dB, (c) star coupler integrados.
- El acoplador de guías de Fig. 23.1-8(b) tiene matriz (Sec. 8.5B)

$$\mathbf{T}=\begin{bmatrix}\cos\mathcal{C}L & -j\sin\mathcal{C}L\\ -j\sin\mathcal{C}L & \cos\mathcal{C}L\end{bmatrix} \qquad (23.1\text{-}11)$$

  con $\mathcal{C}$ el coeficiente de acoplamiento y $L$ la longitud de interacción. La potencia
  entrante por el puerto 1 se reparte entre las salidas 1 y 2 con factores $\cos^2\mathcal{C}L$ y
  $\sin^2\mathcal{C}L$; para $\mathcal{C}L=\pi/4$ es un acoplador 3 dB (p. 1025).
- Acopladores de fibra (Fig. 23.1-9, p. 1025): (a) fibra de doble núcleo como T-coupler, splitter/TAP
  o combinador; (b) acoplador 3 dB de dos fibras fusionadas (fused taper) o de dos varillas GRIN con
  película divisora; (c) fan-in/fan-out; (d) star coupler con fibras fusionadas o con una varilla
  mezcladora (mixing rod). Los de (b) obedecen la misma matriz (23.1-11).

#### 23.1C Nonreciprocal Optical Interconnects (p. 1025)

- Se basan en el **rotador de Faraday**. Aislador: rotador de 45° entre dos polarizadores a 45°
  (Sec. 6.4B): transmite hacia adelante y bloquea hacia atrás.
- Rotador de Faraday de 45° seguido de **retardador de media onda** (eje rápido a 22.5° del plano de
  polarización): la luz linealmente polarizada hacia adelante no cambia; hacia atrás su polarización
  gira 90°. Con divisores de haz polarizantes (**PBS**) implementa interconexiones no recíprocas
  (Fig. 23.1-10a: 3 puertos, luz de 1→2 y de 2→3) y **circuladores** (Fig. 23.1-10b: 4 puertos
  1→2→3→4→1 con dos PBS, p. 1026).

#### 23.1D Optical Interconnects in Microelectronics (p. 1026)

- Enlaces de fibra procesador–procesador, backplane–backplane y tarjeta–tarjeta (Fig. 23.1-11a);
  enlaces libres micro-ópticos tarjeta–tarjeta (Fig. 23.1-11b) con chips optoelectrónicos con
  arreglos de **VCSEL** y fotodetectores. Prototipos chip-a-chip con guía dieléctrica planar y
  espejos (Fig. 23.1-12, p. 1027). Dentro del chip (VLSI), las interconexiones ocupan gran parte del
  área y sus retardos son comparables o mayores que los de las compuertas; la viabilidad comercial de
  la óptica intra-chip "no está establecida" (p. 1027).
- **Justificación (p. 1027–1028)**: la frecuencia portadora óptica (20–50 THz) es mucho mayor que
  el ancho de banda de los datos; la electrónica usa banda base (GHz).
  - *Densidad*: haces no guiados limitados solo por difracción (ancho × ángulo ~ λ); pueden
    cruzarse en 3D; guías dieléctricas de ancho ~λ con poca diafonía. Los conductores metálicos
    tienen pérdidas e interferencia electromagnética.
  - *Ancho de banda*: una línea de cinta de longitud $\ell$ y sección $A$ tiene $R\propto\ell/A$,
    $C\propto\ell$ → $RC\propto\ell^2/A$; ancho de banda $\propto A/\ell^2$, fijado por la razón
    de aspecto $\ell/\sqrt{A}$, invariante ante miniaturización (lo mismo para líneas $LC$). La
    óptica no sufre ese límite; además la diafonía entre líneas vecinas no crece con la tasa de
    datos (razón ancho de banda/portadora pequeña). Mayor producto densidad–ancho de banda.
  - *Retardo*: fotones a 0.3 mm/ps en vacío y ≈0.86 mm/ps en silicio → ≈3.3 ps/mm y ≈9.4 ps/mm;
    las líneas eléctricas en cerámica y poliimida tienen ≈10.2 y 6.8 ps/mm. El retardo óptico no
    depende del número de ramas (fan-out), a diferencia de las líneas eléctricas cuya velocidad
    cae con la carga capacitiva.
  - *Potencia*: las líneas eléctricas deben terminarse con impedancia acoplada (gasto de potencia);
    en óptica basta el antirreflejo; la potencia la fijan sensibilidad de detectores y eficiencias
    de conversión E/O y O/E.
- **Implementación intra-chip (p. 1028–1029)**: cada enlace = transductor E/O (transmisor) + haz +
  transductor O/E (receptor). Guías en silicio o enrutamiento externo con holograma (Fig. 23.1-13a);
  caso uno-a-muchos: **distribución de reloj óptico** con holograma de reflexión que difunde el
  reloj a muchos fotodetectores, eliminando el *clock skew* (Fig. 23.1-13b). Idealmente todo
  monolítico y compatible con CMOS: fotodiodos de Si y guías SOI (Sec. 8.3) son viables; el
  problema son las fuentes: el Si es de gap indirecto (Sec. 16.1D); AlGaAs/GaAs sobre Si no es
  confiable (desacople de red y térmico); moduladores todo-silicio demasiado grandes o lentos.
  Solución práctica: **integración híbrida** con **flip-chip bonding** (miles de dispositivos,
  alineación < 1 μm): p. ej. arreglo de VCSEL de GaAs a 850 nm a > 10 Gb/s con ~1 V; arreglos de
  moduladores por electroabsorción (Sec. 20.5); fuente InP pegada a chip de Si acoplada a guía
  SOI tipo ridge (Fig. 23.1-14, p. 1029).

---

### 23.2 Passive Optical Routers (p. 1030)

**Resumen.** Enrutamiento por un atributo físico $X_\ell$ (λ, intensidad, fase, polarización o
tiempo): el componente con atributo $X_\ell$ va al puerto $\ell$, $\ell=1,\dots,N$ (Fig. 23.2-1a).
- **Demultiplexor (DEMUX)**: enrutador 1×N que separa los componentes $X_1,\dots,X_N$ de un haz. Puede
  hacerse con **broadcast-and-select**: fan-out 1×N + banco de filtros.
- **Multiplexor (MUX)**: inverso del DEMUX (Fig. 23.2-1c).
- **Optical add-drop multiplexer (OADM)** (Fig. 23.2-1d): demultiplexa, extrae ("drop") el componente
  de atributo elegido (p. ej. $X_2$), agrega nuevos datos ("add") y vuelve a multiplexar.

#### 23.2A Wavelength-Based Routers (p. 1030)

Usados en redes WDM (Sec. 24.3C): multiplexores y demultiplexores por división de longitud de onda.

**Implementaciones de MUX/DEMUX de λ (Fig. 23.2-2, p. 1030–1031):**
- (a) **Prisma**: dispersión angular limitada por $dn/d\lambda$, insuficiente para separar λ
  cercanas; los **superprismas** de cristal fotónico (cap. 7) tienen 2–3 órdenes de magnitud más
  poder dispersivo.
- (b) **Red de difracción** (Sec. 2.4B) con lente o varilla GRIN: resuelve diferencias de λ
  equivalentes a unos pocos GHz.
- (c) Banco de filtros (broadcast a todos) o secuencia de **filtros dieléctricos de película
  delgada (TFF)** de banda estrecha, cada uno transmite un canal y refleja los demás; varilla GRIN
  para guiar los rayos.
- (d) **Fiber Bragg grating (FBG)** (Sec. 7.1C): refleja la componente en $\lambda_B=\Lambda/2$ ($\Lambda$
  período de la red; expresión tal como aparece en el libro, p. 1031, es decir, en términos de la
  longitud de onda en el medio) y transmite las demás; varias FBG separan varias λ.
- (e) **Filtros de microanillos resonantes (microring resonators)**, cada uno sintonizado a una λ,
  en secuencia a lo largo de una guía bus: cada anillo extrae su λ hacia una guía de salida.
- Otros: **interferómetro de Mach–Zehnder** y **waveguide grating routers**.

**OADM (p. 1031–1032).** Extrae datos de canales seleccionados (con detectores) y añade datos
nuevos (con fuentes moduladas), o separa el canal con un componente sensible a λ:
- Fig. 23.2-3 (p. 1032): **OADM con FBG y circuladores**. Entran $\lambda_1,\lambda_2,\lambda_3$ por
  un circulador; la FBG refleja $\lambda_1$, que el circulador dirige al puerto *drop*; $\lambda_2,\lambda_3$
  pasan; un segundo circulador agrega una nueva $\lambda_1$ (la FBG refleja hacia atrás cualquier
  $\lambda_1$ contrapropagante).
- Fig. 23.2-4 (p. 1032): **OADM con múltiples microanillos** apilados entre dos guías (bus
  Input→Output arriba y Add→Drop abajo): $\lambda_1$ se extrae del haz de entrada hacia *Drop* y
  nuevos datos en $\lambda_1$ entran por *Add* hacia *Output*; $\lambda_2,\lambda_3$ pasan. **"Múltiples
  microanillos tienen mayor selectividad en λ (ancho espectral más angosto y mayor razón de
  rechazo) que un microanillo simple"** (p. 1032). ← Relevante para el anillo add-drop del proyecto.

**El Mach–Zehnder como demultiplexor (p. 1032–1033).** MZI integrado (Fig. 23.2-5) con diferencia
de caminos $\Delta d$ tal que $\phi=2\pi\Delta d/\lambda$ sea múltiplo par de π en $\lambda_1$ e
impar en $\lambda_2$: $\Delta d=q_1\lambda_1/2$ y $\Delta d=q_2\lambda_2/2$, $q_1$ par, $q_2$ impar.
Resolución: $1/\lambda_1-1/\lambda_2=(q_1-q_2)/2\Delta d$; con $|q_1-q_2|=1$,
$|1/\lambda_1-1/\lambda_2|=1/2\Delta d$, de modo que

$$\Delta\nu=\frac{c}{2\Delta d} \qquad (23.2\text{-}1)$$

Ejemplo del libro: $\Delta d=1$ mm y $n=1.5$ → $\Delta\nu=100$ GHz (p. 1033). (Aquí $c$ se toma como
la velocidad en el medio, $c_0/n$: $3\times10^8/1.5/(2\times10^{-3})=100$ GHz.) Separaciones menores
requieren $\Delta d$ proporcionalmente mayores.

Matriz de interconexión del MZI (3 dB · desfase · 3 dB):

$$\mathbf{T}=\begin{bmatrix}1 & j\\ j & 1\end{bmatrix}
\begin{bmatrix}\exp[-j2\pi(d_0+\Delta d)/\lambda] & 0\\ 0 & \exp(-j2\pi d_0/\lambda)\end{bmatrix}
\begin{bmatrix}1 & j\\ j & 1\end{bmatrix} \qquad (23.2\text{-}2)$$

($d_0$ y $d_0+\Delta d$ longitudes de los brazos; el libro omite el factor $1/\sqrt2$ de cada
acoplador en esta expresión). Para campo unidad en el puerto 1, $P_1=|T_{21}|^2$ y $P_2=|T_{22}|^2$:

$$P_1=\cos^2(\pi\Delta d/\lambda),\qquad P_2=\sin^2(\pi\Delta d/\lambda) \qquad (23.2\text{-}3)$$

Cuanto menor $\lambda/\Delta d$, más rápido alternan estas funciones → λ más cercanas se separan.
Fig. 23.2-6 (p. 1033): **MZI en cascada** separan 4 λ: el primero separa impares de pares y los
siguientes afinan (es el objeto del Problema 23.2-1).

**Waveguide Grating Routers (WGR) / Arrayed Waveguides (AWG) (p. 1033–1035).**
- *Interferómetro multicamino* (Sec. 2.5B): $L$ caminos cuyas longitudes crecen linealmente con
  diferencia $\Delta d$ entre adyacentes. La salida es la suma de $L$ ondas de igual amplitud y
  desfase $\phi=2\pi\Delta d/\lambda$:

$$\mathcal{T}=\frac{\sin^2(L\varphi/2)}{\sin^2(\varphi/2)}=\frac{\sin^2(L\pi\Delta d/\lambda)}{\sin^2(\pi\Delta d/\lambda)} \qquad (23.2\text{-}4)$$

  (el libro escribe $\varphi$ en la primera forma y $\phi$ en el texto). Periódica en $\phi$ con picos
  en múltiplos de $2\pi$ (Fig. 2.5-7); en λ no es periódica: picos en $\lambda=\Delta d$ y fracciones
  enteras ($\Delta d/2$, $\Delta d/3$, …), Fig. 23.2-7. Más caminos $L$ → picos más agudos.
- *WGR como DEMUX 1×N* (Fig. 23.2-8, p. 1034–1035): $N$ interferómetros multicamino, uno por puerto de
  salida, con $\Delta d_m$ múltiplo entero de $\lambda_m$ pero no de las otras λ. Con canales
  uniformes decrecientes $\lambda_m=\lambda_0-m\Delta\lambda$ y $\lambda_0=\lambda_1-\Delta\lambda$,
  condición necesaria:

$$\Delta d_m=\lambda_m=\lambda_0-m\Delta\lambda,\quad m=1,2,\dots,N \qquad (23.2\text{-}5)$$

  (la diferencia de caminos decrece linealmente con $m$). La condición de que $\Delta d_m$ no sea
  múltiplo de $\lambda_\ell$, $\ell\ne m$, se cumple automáticamente si $\lambda_N>\lambda_1/2$.
  Implementación: dos **star couplers** y un arreglo de guías cuyas longitudes crecen en $\Delta d_w$;
  para un star coupler de fronteras circulares la diferencia de caminos es aproximadamente lineal
  decreciente en $m$:

$$\Delta d_m=\Delta d_w+(\Delta d_a-m\,\Delta d_b) \qquad (23.2\text{-}6)$$

  con $\Delta d_a,\Delta d_b$ constantes geométricas. (23.2-5) se cumple si $\Delta d_w+\Delta d_a=\lambda_0$
  y $\Delta d_b=\Delta\lambda$. La resolución (mínimo $\Delta\lambda$) la limita el mínimo $\Delta d_b$
  realizable (p. 1035). Es el objeto del Problema 23.2-2.
- *WGR como enrutador N×N* (p. 1035): entre la entrada $\ell$ y la salida $m$ hay un interferómetro
  con $\Delta d_{\ell m}=\lambda_{00}-(\ell+m)\Delta\lambda$; se transmite la λ que iguale
  $\Delta d_{\ell m}$ **[recuadro, "WGR Equation"]**:

$$\lambda_{\ell m}=\lambda_{00}-(\ell+m)\Delta\lambda,\qquad \ell,m=1,2,\dots,N \qquad (23.2\text{-}7)$$

  Generaliza (23.2-6). No implementa enrutamiento arbitrario, pero sirve para multiplexación
  simultánea (Problema 23.2-3).

#### 23.2B Polarization-, Phase-, and Intensity-Based Routers (p. 1035)

- **Por polarización (p. 1035):** un PBS separa las componentes paralela y ortogonal (DEMUX de
  izquierda a derecha; MUX de derecha a izquierda), Fig. 23.2-9.
- **Por fase (p. 1035–1036):** secuencia de pulsos con fases 0 o π se ordena en dos puertos con un
  interferómetro simple contra un haz de referencia (Fig. 23.2-10).
- **Por intensidad (p. 1036–1038):** separar pulsos de alta y baja intensidad requiere **elementos
  no lineales**; normalmente se convierte la variación de intensidad en cambio de fase con una
  **celda Kerr** (Sec. 21.3A).
  - *MZI no lineal*: MZI con celda Kerr en un brazo; desfase $\propto$ intensidad; se ajusta para
    que la diferencia de fase sea múltiplo impar de π para una intensidad y par para la otra →
    pulsos altos a un puerto, bajos al otro (Fig. 23.2-11a en óptica de volumen; 23.2-11b en fibra).
  - *Sagnac asimétrico no lineal* (Fig. 23.2-12): la luz entra por la fibra 1, se divide en onda
    horaria y antihoraria; si los caminos son iguales (fibra lineal, o no lineal con intensidades
    iguales) interfieren constructivamente y regresan por la fibra 1 (espejo). Si el acoplador es
    asimétrico, las intensidades difieren, los desfases Kerr difieren, y para diferencia π la luz
    sale por la fibra 2: enrutador 1×2 autocontrolado por intensidad. Alternativa: un **EDFA** en
    posición asimétrica dentro del lazo amplifica una onda en la primera mitad de su recorrido
    (viaja más de media vuelta a alta intensidad) y la otra en la segunda mitad (menos desfase):
    **nonlinear optical loop mirror (NOLM)** (p. 1037).
  - *Acoplador direccional no lineal (NLDC)* (Fig. 23.2-13): acoplador de guías o fibra de material
    Kerr. A baja intensidad es lineal: la luz pasa periódicamente de una guía a otra (Fig. 8.3-4);
    si la longitud es la de transferencia $L_0$, pasa por completo a la otra guía. A alta
    intensidad el Kerr altera las constantes de propagación y crea un desacople de fase dependiente
    de la intensidad y de $z$. Ecuaciones acopladas no lineales:

$$\frac{da_1}{dz}=-j\mathcal{C}\exp(j\Delta\beta z)\,a_2(z)-j\gamma|a_1|^2a_1 \qquad (23.2\text{-}8)$$
$$\frac{da_2}{dz}=-j\mathcal{C}\exp(-j\Delta\beta z)\,a_1(z)-j\gamma|a_2|^2a_2 \qquad (23.2\text{-}9)$$

    generalizan las ecuaciones lineales (8.5-4). $\mathcal{C}=\pi/2L_0$ es el coeficiente de
    acoplamiento y $\gamma$ es proporcional al coeficiente Kerr $n_2$ (Sec. 21.3A y Ec. (22.5-16)).
    Se diseña para que los pulsos intensos salgan por la misma guía y los débiles por la otra.
  - *Acoplador direccional de solitones* (p. 1037): el NLDC sufre **ruptura de pulsos** porque la
    intensidad varía dentro del pulso y distintas fracciones cruzan entre fibras (reshaping). No
    ocurre si el pulso es un **solitón** (Sec. 22.5B): su desfase no lineal es constante sobre la
    envolvente y el pulso se mantiene intacto; además la transición entre puertos es una función
    mucho más abrupta de la potencia.

---

### 23.3 Photonic Switches (p. 1038)

#### 23.3A Architectures of Space Switches (p. 1038)

- Un **conmutador** establece y libera conexiones; una unidad de control procesa órdenes y envía
  la señal de control. Fig. 23.3-1 (p. 1038): (a) 1×1 ON–OFF; (b) 1×2; (c) 2×2 **crossbar** con
  estados *bar* y *cross* (acoplador direccional controlable); (d) 1×N; (e) N×N crossbar — toda
  entrada puede conectarse a cualquier salida libre sin bloqueo.
- Un N×N crossbar se construye con $N^2$ conmutadores 1×1 en una matriz (crosspoint); el 1×3 y el
  3×3 **broadcast-and-select** de Fig. 23.3-2 (p. 1039). Con 2×2: 4×4 con cinco 2×2 (Fig. 23.3-3a;
  entrada 1 → salida 3 si A y C en cross y E en bar) y 8×8 con 28 conmutadores 2×2 (Fig. 23.3-3b).
- **Parámetros de un conmutador (p. 1039):** tamaño y dirección(es); tiempo de conmutación
  (reconfiguración); retardo de propagación; throughput (tasa máxima); energía de conmutación;
  disipación de potencia; pérdida de inserción; diafonía; probabilidad de bloqueo; dimensiones
  físicas.

#### 23.3B Implementations of Optical Space Switches (p. 1039)

- **Conmutadores optoelectrónicos (p. 1039–1040):** compuertas CMOS nanométricas con tiempos < 0.1 ns
  y energías < 1 fJ; MOSFET avanzados a tiempos subpicosegundo; chips crossbar de 128×128. Usarlos
  para luz exige conversión O/E a la entrada y E/O a la salida (Fig. 23.3-4: fotodetectores,
  crossbar electrónico, VCSEL). Las conversiones añaden retardo y pérdida → interés en conmutadores
  fotónicos "transparentes".
- **Configuraciones básicas (p. 1040):** escáner (1×N, Fig. 23.3-5a); modulador ON–OFF (1×1), directo
  o interferométrico (modulador de fase en un brazo de un interferómetro, Fig. 23.3-5b); acoplador
  direccional o interferómetro con modulador de fase en uno o ambos brazos como 2×2 (Fig. 23.3-5c);
  los brazos pueden ser dos polarizaciones ortogonales con un retardador como modulador. Un arreglo
  planar de 16 moduladores (1×1) forma un crossbar 4×4 broadcast-and-select (Fig. 23.3-6, p. 1041).
- **Diagrama de tiempos de conmutación (p. 1041)** (escala de 1 fs a 1 ms): all-optical ≈ fs…ns;
  electrónica ≈ ps…μs; electro-óptico ≈ 10 ps…μs; SOA ≈ 100 ps…ns; acusto-óptico ≈ ns…μs;
  magneto-óptico ≈ 10 ns…μs; LC (cristal líquido) ≈ μs…ms; MEMS ≈ 10 μs…ms; mecano-óptico y
  termo-óptico ≈ ms. (Lectura aproximada del diagrama de barras.)
- **Mecano-ópticos (p. 1041–1042):** espejo o prisma rotatorio, disco holográfico rotatorio
  (cada sector una red con orientación y período que fijan el plano y ángulo de barrido), rueda con
  fibras en V-grooves y líquido de acople (Fig. 23.3-7); piezoeléctricos para más velocidad.
  **MEMS**: actuadores electrostáticos en grandes arreglos con procesos de microelectrónica;
  velocidades 10 ms–10 μs; crossbar con espejos popup o móviles (Fig. 23.3-8). Limitación: lentos
  (ms); ventajas: baja pérdida de inserción y baja diafonía.
- **Electro-ópticos (p. 1042–1043):** material EO (Sec. 20.1) como modulador de fase o retardador;
  en interferómetro o entre polarizadores cruzados es un 1×1. Óptica integrada en LiNbO₃ (guías por
  difusión de Ti). 1×1 con MZI integrado (Fig. 23.3-9a, Sec. 20.1B); 2×2 con MZI (Fig. 23.3-9b) o
  con acoplador direccional (Fig. 23.3-9c, Sec. 20.1D): pocos voltios, > 20 GHz. 4×4 con cinco
  acopladores en un sustrato (Fig. 23.3-10); se han fabricado hasta 32×32 en LiNbO₃. Límites:
  tamaño de cada acoplador y planaridad (se usan guías que se cruzan); pérdidas de inserción altas
  al acoplar fibras; el coeficiente de acoplamiento depende de la polarización → fibras
  mantenedoras de polarización (Sec. 9.2B) o esquemas elaborados.
- **Semiconductores (p. 1043–1044):** electroabsorción por efecto **Franz–Keldysh** y **QCSE** en
  MQW (Sec. 20.5): moduladores 1×1 con tiempos < 20 ps, en arreglos surface-normal sobre Si
  (Fig. 23.3-11). **SOA** (Sec. 17.2A) como 1×1 encendiendo/apagando la corriente: tiempos de ns;
  sin ganancia es absorbedor fuerte, con ganancia amplifica → extinción > 40 dB; a 1.55 y 1.3 μm en
  InGaAsP/InP (DH y MQW). Arreglos de SOA en broadcast-and-select (Fig. 23.3-12, 2×2 con cuatro 1×1
  más pre/postamplificadores) compensan pérdidas de división. Integración híbrida con PLC de sílice
  demostrada; la gran escala "sigue siendo un reto". Los SOA también sirven como convertidores de λ
  y, por su no linealidad, como conmutadores todo-ópticos ultrarrápidos (Sec. 23.3C).
- **Cristal líquido (p. 1044–1045):** celda LC como retardador o rotador controlado (Sec. 20.3),
  con polarizadores cruzados → modulación; o reflexión total interna solo con campo aplicado.
  Panel con muchos electrodos = modulador espacial digital = conjunto de 1×1 para crossbar N×N.
  2×2 crossbar con dos PBS y un rotador LC de π/2 (Fig. 23.3-13; independiente de la polarización).
  Lentos → protección ante fallas y OADM reconfigurable (Sec. 24.4B).
- **Acusto-ópticos (p. 1045):** deflexión de Bragg por sonido (cap. 19); la potencia difractada la
  controla la intensidad acústica y el ángulo la frecuencia. Modulador = 1×1; escáner = 1×N con
  $N$ = número de puntos resolubles (Sec. 19.2B); celdas con $N=2000$; $N\times M$ con varias
  frecuencias simultáneas (límite de $NM$: Sec. 19.2C). Fig. 23.3-14.
- **Magneto-ópticos (p. 1045):** efecto Faraday, poder rotatorio $\rho\propto B$; entre polarizadores
  cruzados $\mathcal{T}=\sin^2\theta$ con $\theta=\rho d$ → 1×1 controlado por campo magnético.
  Películas de granate de hierro con bismuto; conmutación binaria invirtiendo la magnetización
  con conductores cruzados; celdas de 10×10 μm; arreglos 1024×1024; tiempos de 100 ns. (También
  usados en discos magneto-ópticos por efecto termomagnético.)
- **Termo-ópticos (p. 1046):** $dn/dT\approx10^{-5}$ /°C en sílice (polímeros mayor); por ser pequeño
  se usa en interferómetros: MZI en sílice sobre Si (SOS) con calentador de película delgada
  (Fig. 23.3-15). Desfase $(2\pi L/\lambda_o)\Delta n=(2\pi L/\lambda_o)(dn/dT)\Delta T$; con
  $L/\lambda_o=2\times10^3$, un desfase de π requiere $\Delta T=25$ °C. También AWG termo-ópticos.
  Lentos (ms) → reconfiguración de redes. **Bubble jet switch** (Fig. 23.3-16): microcalentadores
  generan burbujas en un fluido de índice $n$ en la intersección de guías, que actúan de espejo.

#### 23.3C All-Optical Space Switches (p. 1046)

Una luz de control altera una propiedad de un material no lineal, cambiando un atributo de la luz
controlada (fase en medio Kerr → cambia el puerto de salida de un interferómetro; también retardo
o absorción sensibles a la luz; colisión de solitones con retardo o corrimiento de frecuencia).

- **MZI no lineal (p. 1046–1047):** elemento no lineal en un brazo (Fig. 23.3-17a volumen, 17b fibra).
  Sin control, balanceado → salida 1; el control induce $\Delta n$ y un desfase incremental de π →
  salida 2. Un filtro bloquea el control (de distinta λ). Es 1×2; ignorando un puerto, 1×1.
- **Sagnac asimétrico no lineal ultrarrápido — TOAD (p. 1047–1048):** (El texto menciona antes que
  con SOA se han demostrado conmutaciones de varios cientos de Gb/s pese a la lenta recuperación de
  portadores.) La velocidad de un conmutador todo-óptico la limita el tiempo de respuesta del
  efecto: subida corta y decaimiento más largo al retirar el control; con Kerr la limita la
  respuesta Kerr. Mayor velocidad: ambos brazos comparten el **mismo** elemento no lineal pero el
  pulso lo cruza en instantes distintos → lazo Sagnac de fibra con el elemento en posición
  asimétrica (Fig. 23.3-18). El pulso de entrada (fibra 1) se divide en horario y antihorario; si
  sufren el mismo desfase, regresan por la fibra 1 (salida 1); si difieren en π salen por la fibra 2
  (salida 2). Un pulso de control corto induce $\Delta n$ con subida $\tau_i$ y relajación larga
  $\tau_r$; los pulsos cruzan el elemento en $\tau_1$ y $\tau_2$. Si ambos lo cruzan activo (o ambos
  inactivo) → salida 1; si uno antes y otro después del encendido → diferencia π → salida 2. La
  conmutación la gobierna $\tau_1-\tau_2$ (∝ distancia del elemento al punto medio del lazo); si es
  apenas mayor que $\tau_i$, la precisión la fija el tiempo de subida y no $\tau_r$. Tiempos de
  femtosegundos → operación a THz: **Terahertz Optical Asymmetric Demultiplexer (TOAD)** [Sokoloff,
  Prucnal, Glesk, Kane, IEEE Photon. Technol. Lett. 5, 787 (1993)]. Usado para demultiplexación TDM.
- **Conmutador de retardo no lineal (p. 1048–1049):** Kerr en medio **anisótropo**: el control cambia
  los índices principales de forma distinta → retardador controlado ópticamente. Entre polarizadores
  cruzados (Fig. 23.3-19, cristal o fibra birrefringente no lineal): retardo 0 → OFF; retardo π →
  polarización gira 90° → ON. Filtro para bloquear el control.
- **Conmutadores de solitones (p. 1048–1049):** solitones = pulsos ultracortos que se propagan sin
  ensancharse en fibras no lineales dispersivas (Sec. 22.5B). Un solitón controla el enrutamiento
  de otro por colisión o recombinación en un solitón vectorial. Velocidades subpicosegundo con
  energías de decenas de pJ.
  - *Colisión*: dos solitones con frecuencias (y velocidades de grupo) ligeramente distintas se
    atraviesan; se alteran el tiempo de llegada y la fase de cada uno. Enrutamiento temporal con una
    compuerta que abre en una ventana; por fase, con un interferómetro.
  - *Solitón vectorial*: dos pulsos ortogonalmente polarizados copropagantes en fibra birrefringente
    no lineal; se separan en el tiempo por **walk-off** (Sec. 22.5A); la **XPM** (Sec. 21.3C) sube
    la frecuencia de uno y baja la del otro; con **GVD** esos corrimientos cambian las velocidades
    de grupo; cuando la diferencia por birrefringencia se compensa exactamente con la de GVD vía
    XPM, viajan juntos: **soliton trapping**. Conmutador 1×1 (Fig. 23.3-20): control y señal en la
    misma λ forman un solitón vectorial con componentes a $\lambda\pm\delta\lambda$; un filtro
    selecciona una; sin control no hay corrimiento y el filtro bloquea.

**Límites fundamentales de los conmutadores todo-ópticos (p. 1050–1051).**
- *Fluctuaciones del número de fotones*: en principio basta un fotón, pero la emisión de un láser o
  LED es Poisson, $p(n)=\bar n^n\exp(-\bar n)/n!$ (Sec. 12.2C). Con $\bar n=21$, $p(0)=e^{-21}\approx10^{-9}$:
  21 fotones garantizan al menos uno con 1 error en $10^9$ → $E=21h\nu$; para $\lambda_o=1$ μm,
  $E=21\times1.24\approx26$ eV $=4.2$ aJ. Cota práctica (no fundamental: con luz comprimida en número
  de fotones, Sec. 12.3B, podría ser menor). Referencia pesimista: 1000 fotones → 20 aJ a 1 μm.
  Nótese $h\nu\gg kT=0.026$ eV a 300 K.
- *Incertidumbre energía–tiempo*: $\sigma_E\sigma_T\ge h/4\pi$ (12.1-16) → $ET\ge h/4\pi$, es decir
  $E\ge h/4\pi T=h\nu/4\pi\nu T$; como $T$ no es menor que un ciclo óptico $1/\nu$, $4\pi\nu T>1$ y
  esta cota es menor que $h\nu$: eligiendo $E>h\nu$ se satisface siempre.
- *Tiempo de conmutación*: solo lo limita energía–tiempo; pulsos de pocos fs (pocos ciclos) ya
  existen; inalcanzable por semiconductores o Josephson; demostraciones subpicosegundo.
- *Tamaño*: limitado por difracción (difícil acoplar luz a dispositivos < λ).
- *Limitaciones prácticas*: debilidad de las no linealidades disponibles → energías grandes;
  disipación térmica: potencia $E/T$ por operación repetitiva; tiempos muy cortos con energías
  altas son insostenibles, salvo a tasas de repetición menores que la máxima.

#### 23.3D Wavelength-Domain Switches (p. 1051)

- **EJEMPLO 23.3-1, Selector de λ reconfigurable (p. 1051):** DEMUX + $N$ conmutadores 1×1 + MUX
  (Fig. 23.3-21): combinación de enrutadores pasivos y conmutadores espaciales.
- **EJEMPLO 23.3-2, ROADM (p. 1051):** OADM reconfigurable con opción add/drop/pass-through:
  DEMUX, MUX, un 1×2 y un 2×1 por canal (Fig. 23.3-22).
- **EJEMPLO 23.3-3, Wavelength-Channel Interchange (WCI, "λ switch") (p. 1051–1052):** enruta datos
  entre canales λ del mismo haz: DEMUX → banco de $N$ **convertidores de longitud de onda (WC)** →
  acoplador N×1 (Fig. 23.3-23). Un WC cambia la λ sin alterar los datos ("copia").
- **Conmutadores multidimensionales espacio–λ (p. 1052):** $N$ haces con $N$ canales cada uno.
  (a) broadcast-and-select: star coupler + filtros sintonizables + WC (reconfigurable, pero
  desperdicia potencia en los filtros); (b) WC → **WGR** → WC, con el primer WC llevando cada canal a
  la λ que satisface (23.2-7) para el destino deseado (más eficiente). Fig. 23.3-24.
- **Convertidores de longitud de onda (p. 1052–1053):** no lineales, paramétricos o no paramétricos.
  - *No paramétricos*: el haz 1 (modulado) altera ganancia, absorción o índice de un semiconductor
    en proporción a la intensidad ("escribe"); el haz 2 lo "lee". **XGM** (cross-gain modulation):
    ganancia saturada del SOA decrece con la intensidad → el haz leído sale modulado en forma
    invertida (Fig. 23.3-25a). **XPM**: en SOA no saturado el índice depende de la densidad de
    portadores → modulación de fase, que un MZI convierte en intensidad (Fig. 23.3-25b).
  - *Paramétricos* (cap. 21): en medio χ⁽²⁾, $\omega_2=\omega_3-\omega_1$ con auxiliar $\omega_3$;
    problema: si $\omega_1\approx\omega_2$, $\omega_3$ debe ser ≈ el doble. Alternativa en cascada:
    SHG $\omega_1\to2\omega_1$ y luego $\omega_2=2\omega_1-\omega_3$ (todas de frecuencia similar).
    O **FWM** en χ⁽³⁾ (fibra, Sec. 21.3): $\omega_1+\omega_2=\omega_3+\omega_4$; caso parcialmente
    degenerado $\omega_3=\omega_4=\omega_0$ → $\omega_2=2\omega_0-\omega_1$ (Fig. 23.3-25c, con
    $\omega_0=\tfrac12(\omega_1+\omega_2)$).

#### 23.3E Time-Domain Switches (p. 1053)

- Enruta entre ranuras temporales (time slots) de tramas de $N$ slots. **Time-slot interchange
  (TSI)**: datos del slot $\ell$ al slot $m$ de la misma trama; es el homólogo temporal del WCI
  (Fig. 23.3-26). **Time-space-time (TST)**: TSI – conmutador espacial – TSI (Fig. 23.3-27).
- **Demultiplexor por división de tiempo (p. 1054–1055):** 1 entrada, $N$ salidas; el slot $\ell$ va a
  la línea $\ell$ (mapa tiempo→espacio), equivalente a un 1×N recorriendo secuencialmente sus
  salidas (Fig. 23.3-28, $N=4$). **TDM** (multiplexor) es el inverso. Con $N$ conmutadores 1×1
  (Fig. 23.3-2a) encendidos secuencialmente por un reloj.
- **TDM óptico (p. 1055):** (a) copias del haz por star coupler a $N$ conmutadores 1×1 controlados
  por pulsos de reloj retardados múltiplos de $T/N$ ($T$ = período de trama); (b) las copias se
  retardan sucesivamente múltiplos de $T/N$ y un mismo reloj controla todos (similar a la medición
  del perfil temporal de un pulso, Fig. 22.6-5). Retardos con fibra (≈ 5 ns/m en sílice).
  1×1 todo-ópticos interferométricos, p. ej. TOAD. Fig. 23.3-29.
- **TSI óptico (p. 1056):** DEMUX tiempo→espacio, retardos para sincronizar en un slot $T/N$, crossbar
  N×N, retardos para restaurar los slots, MUX espacio→tiempo (Fig. 23.3-30; Problema 23.3-3).
- **Retardos programables y buffers (p. 1056):** lazo de fibra + crossbar 2×2 (Fig. 23.3-31): en
  $t=0$ el conmutador en *cross* admite el pulso; en *bar* el pulso recircula con retardo $T$ por
  vuelta; en $t=mT$ se cambia a *cross* y se libera.

#### 23.3F Packet Switches (p. 1056)

- Los anteriores son conmutadores relacionales (**circuit switching**: la configuración la fijan
  señales externas). En **packet switching**, la configuración la fija la dirección de destino en
  la cabecera (header) de cada paquete; una unidad de reconocimiento de cabecera lee la dirección
  (Fig. 23.3-32, p. 1057).
- *Reconocimiento por correlación*: correlación de la secuencia de bits de la dirección $(a_1,\dots,a_N)$
  con cada entrada de la tabla $(b_1,\dots,b_N)$: $a_1b_1+a_2b_2+\dots+a_Nb_N$; la mayor correlación
  identifica la dirección. Implementación óptica: fibra con $N$ **FBG** equiespaciadas de
  reflectancias $(b_1,\dots,b_N)$ (multiplicadores); los retardos de ida y vuelta sincronizan los bits
  para que se sumen (Fig. 23.3-33).
- *Conmutadores autoenrutados*: 2×2 que envían el paquete al puerto superior o inferior según un bit
  (o que ordenan por número de dirección). **Banyan 8×8** (Fig. 23.3-34, p. 1058): tres etapas, doce
  2×2; dirección binaria $(x_1,x_2,x_3)$; etapa $k$ usa el bit $x_k$: bit 1 → puerto inferior, 0 →
  superior. Ejemplo: entrada 2 con destino 6=(110) sigue inferior, inferior, superior. Puede haber
  **bloqueo interno** (dos paquetes al mismo puerto de un 2×2); redes con ordenamiento + enrutamiento
  lo evitan. **Contención** (paquetes de distintas entradas al mismo puerto de salida): enrutar por
  otro camino, retardar con buffer, o convertir a otra λ (Sec. 23.3D).

---

### 23.4 Optical Gates (p. 1058)

#### 23.4A Bistable Systems (p. 1058)

- Un sistema **biestable** tiene salida con solo dos valores estables; se conmuta con un cambio
  temporal del nivel de entrada. Fig. 23.4-1 (p. 1059): al subir la entrada por encima del umbral
  $\vartheta_2$ la salida salta de bajo a alto; al bajar por debajo de $\vartheta_1<\vartheta_2$ vuelve
  a bajo: **lazo de histéresis**. Entre $\vartheta_1$ y $\vartheta_2$ la salida depende de la historia
  ("sube y baja", *seesaw*). Un pico positivo la lleva a alto, uno negativo a bajo: **flip-flop**
  (Fig. 23.4-2): conmutador con enganche (latching) o elemento de memoria.
- Si los umbrales coalescen en un solo valor $\vartheta$: relación S muy abrupta → **amplificador**
  de gran ganancia diferencial (como un transistor), **umbralizador**, **conformador de pulsos** o
  **limitador** (Fig. 23.4-3, p. 1060). Requiere umbral y polarización (bias) estables.
- **Compuerta AND** (Fig. 23.4-4): la entrada es la suma de pulsos $I_i=I_1+I_2$; con alturas
  adecuadas respecto al umbral, la salida es alta solo si ambos pulsos están presentes. Usando una
  entrada como control, la compuerta AND es un 1×1 ON–OFF (p. 1059).

#### 23.4B Principle of Optical Bistability (p. 1060)

- Dos ingredientes: **no linealidad** y **realimentación**. (En electrónica: dos transistores con
  salida de cada uno a la entrada del otro.) Ópticamente: elemento no lineal cuya salida controla la
  transmisión de luz a través del mismo elemento.
- Sistema genérico (Fig. 23.4-5): la salida $I_o$ controla la transmitancia $\mathcal{T}=\mathcal{T}(I_o)$;
  como $I_o=\mathcal{T}I_i$ **[recuadro, "Input–Output Relation for a Bistable System"]**:

$$I_i=\frac{I_o}{\mathcal{T}(I_o)} \qquad (23.4\text{-}1)$$

- Si $\mathcal{T}(I_o)$ es no monótona (campana, Fig. 23.4-6a), $I_i(I_o)$ es no monótona (Fig. 23.4-6b)
  y $I_o(I_i)$ es multivaluada (Fig. 23.4-6c): para $I_i<\vartheta_1$ o $I_i>\vartheta_2$ un solo valor;
  para $\vartheta_1<I_i<\vartheta_2$ tres valores: superior e inferior estables, intermedio
  (segmento entre los puntos 1 y 2) inestable. En Fig. 23.4-6(b): para $I_o<a$ o $I_o>b$,
  $\mathcal{T}=\mathcal{T}_1$ y $I_i=I_o/\mathcal{T}_1$ es lineal con pendiente $1/\mathcal{T}_1$; en el
  máximo $\mathcal{T}_2$ (punto 2) $I_i$ cae a la recta $I_o/\mathcal{T}_2$. La curva (c) es (b) con ejes
  intercambiados. Subiendo desde entradas pequeñas, al superar $\vartheta_2$ salta a la rama
  superior sin pasar por la intermedia; bajando sigue la rama superior hasta $\vartheta_1$ y salta a
  la inferior (Fig. 23.4-7, p. 1061).
- Inestabilidad del estado intermedio (punto $P$ en Fig. 23.4-7, p. 1061): un pequeño aumento de
  $I_o$ eleva mucho $\mathcal{T}(I_o)$ (pendiente positiva y grande entre los puntos 1 y 2) → $I_o$
  crece más → transición al estado superior; análogamente hacia abajo. Otras funciones no lineales
  dan biestabilidad y hasta **multiestabilidad** (más de dos valores estables).
- **EJERCICIO 23.4-1, Funciones no lineales con biestabilidad (p. 1062):** graficar por computadora
  $I_o$ vs $I_i=I_o/\mathcal{T}(I_o)$ para
  (a) $\mathcal{T}(x)=1/[(x-1)^2+a^2]$;
  (b) $\mathcal{T}(x)=1/[1+a^2\sin^2(x+\theta)]$;
  (c) $\mathcal{T}(x)=\tfrac12+\tfrac12\cos(x+\theta)$;
  (d) $\mathcal{T}(x)=\mathrm{sinc}^2\sqrt{a^2+x^2}$;
  (e) $\mathcal{T}(x)=(x+1)^2/(x+a)^2$.
  Elegir $a$ y $\theta$ para que haya biestabilidad. (b)–(e) corresponden a los sistemas de §23.4C:
  (b) Fabry–Perot Kerr, (c) MZI Kerr, (d) acoplador direccional EO, (e) absorbedor saturable.

#### 23.4C Bistable Optical Devices (p. 1062)

Dos tipos de elementos no lineales (Fig. 23.4-8): (1) **dispersivos**: $n$ función de la intensidad;
(2) **disipativos**: $\alpha$ función de la intensidad. El elemento está en un sistema cuya
transmitancia $\mathcal{T}(I_o)$ controla $I_o$ (realimentación externa con divisor de haz y espejo
en la figura).

**Elementos dispersivos no lineales (p. 1062–1064).** Interferómetros (MZ, Fabry–Perot) con medio
Kerr:

$$n=n_0+n_2I_o \qquad (23.4\text{-}2)$$

- *Mach–Zehnder* (Fig. 23.4-9): medio de longitud $d$ en un brazo; transmitancia (Sec. 2.5A)

$$\mathcal{T}=\frac12+\frac12\cos\Big(2\pi\frac{d}{\lambda_o}n+\varphi_0\Big) \qquad (23.4\text{-}3)$$

  ($\lambda_o$ en el vacío, $\varphi_0$ constante). Con (23.4-2) **[recuadro]**:

$$\mathcal{T}(I_o)=\frac12+\frac12\cos\Big(2\pi\frac{d}{\lambda_o}n_2I_o+\varphi\Big) \qquad (23.4\text{-}4)$$

  con $\varphi=\varphi_0+(2\pi d/\lambda_o)n_0$. Repetición periódica de la campana genérica, con
  período en $I_o$ igual a $\lambda_o/n_2d$ (Fig. 23.4-9). → Problema 23.4-3.
- *Fabry–Perot* con separación $d$ (Sec. 2.5B):

$$\mathcal{T}=\frac{\mathcal{T}_{\max}}{1+(2\mathcal{F}/\pi)^2\sin^2[(2\pi d/\lambda_o)n+\varphi_0]} \qquad (23.4\text{-}5)$$

  ($\mathcal{T}_{\max}$, fineza $\mathcal{F}$, $\varphi_0$ constantes). Con (23.4-2) **[recuadro]**:

$$\mathcal{T}(I_o)=\frac{\mathcal{T}_{\max}}{1+(2\mathcal{F}/\pi)^2\sin^2[(2\pi d/\lambda_o)n_2I_o+\varphi]} \qquad (23.4\text{-}6)$$

  Secuencia periódica de campanas agudas (período $\lambda_o/2n_2d$ en $I_o$, Fig. 23.4-10) → biestable.

- **Dispositivos biestables intrínsecos (p. 1064):** la realimentación puede ser interna: resonador
  con medio no lineal cuyo índice lo controla la intensidad **interna** $I$ (Fig. 23.4-11). Como
  $I_o=\mathcal{T}_oI$ ($\mathcal{T}_o$ transmitancia del espejo de salida), es equivalente salvo una
  constante. Con Kerr $n=n_0+n_2I$:

$$\mathcal{T}(I_o)=\frac{\mathcal{T}_{\max}}{1+(2\mathcal{F}/\pi)^2\sin^2[(2\pi d/\lambda_o)n_2I_o/\mathcal{T}_o+\varphi]} \qquad (23.4\text{-}7)$$

  Sistema "autosintonizado" (self-tuning); período en $I_o$: $\lambda_o\mathcal{T}_o/2n_2d$.

**Elementos disipativos no lineales (p. 1064–1065).** Absorbedor saturable (Sec. 14.4A):

$$\alpha=\frac{\alpha_0}{1+I/I_s} \qquad (23.4\text{-}8)$$

($\alpha_0$ absorción de señal pequeña, $I_s$ intensidad de saturación). Dentro de un Fabry–Perot de
longitud $d$ sintonizado al pico de transmisión (Fig. 23.4-12):

$$\mathcal{T}=\frac{\mathcal{T}_1}{(1-\mathcal{R}e^{-\alpha d})^2} \qquad (23.4\text{-}9)$$

con $\mathcal{R}=\sqrt{\mathcal{R}_1\mathcal{R}_2}$ (reflectancias de los espejos) y $\mathcal{T}_1$
constante (Secs. 2.5B y 10.1A). Si $\alpha d\ll1$ (medio ópticamente delgado), $e^{-\alpha d}\approx1-\alpha d$:

$$\mathcal{T}\approx\frac{\mathcal{T}_1}{[1-(1-\alpha d)\mathcal{R}]^2} \qquad (23.4\text{-}10)$$

Con $I=I_o/\mathcal{T}_o$ y (23.4-8):

$$\mathcal{T}(I_o)=\mathcal{T}_2\left[\frac{I_o+I_{s1}}{I_o+(1+a)I_{s1}}\right]^2 \qquad (23.4\text{-}11)$$

con $\mathcal{T}_2=\mathcal{T}_1/(1-\mathcal{R})^2$, $a=\alpha_0d\mathcal{R}/(1-\mathcal{R})$,
$I_{s1}=I_s\mathcal{T}_o$. Para ciertos $a$ es biestable (Ejercicio 23.4-1e).

- Si el absorbedor se sustituye por un **medio amplificador con ganancia saturable**

$$\gamma=\frac{\gamma_0}{1+I/I_s} \qquad (23.4\text{-}12)$$

  el sistema es un amplificador con realimentación: un **láser**. Si $\mathcal{R}\exp(\gamma_0d)<1$
  está bajo umbral; si $>1$ es inestable y oscila. Los láseres exhiben biestabilidad (fuera del
  alcance del libro). "**El sistema biestable dispersivo es el análogo de índice no lineal (en vez
  de ganancia no lineal) del láser**" (p. 1065).

**Materiales (p. 1065–1066).**
- Kerr en vapor de sodio, disulfuro de carbono, nitrobenceno: $n_2$ muy pequeño → $d$ largo,
  respuesta lenta (ns), potencia alta.
- Semiconductores (GaAs, InSb, InAs, CdS): fuerte no linealidad excitónica cerca del gap; una capa
  con caras parcialmente reflectoras es un Fabry–Perot (Fig. 23.4-13): delgada, respuesta rápida.
  GaAs: encendido en pocos ps; apagado dominado por recombinación (ns); 200 ps con recombinación
  superficial reforzada; energía 1–10 pJ (en principio fJ). InAs e InSb: apagado hasta 200 ns.
  MQW (Secs. 16.1G, 17.2D) y materiales orgánicos también biestables.
- Arreglos: $100\times100$ píxeles en 1 cm² de GaAs; con $E=1$ pJ, $T=100$ ps y $N=10^4$ píxeles/cm²,
  carga térmica $NE/T=100$ W/cm² (manejable); $10^{14}$ operaciones/s (vs ≈ $10^{10}$ bit-ops/s de
  supercomputadoras electrónicas de la época).

**Dispositivos biestables híbridos (p. 1066–1067, Fig. 23.4-14).**
- (a) **Fabry–Perot con celda Pockels**: se detecta $I_o$ y se aplica un voltaje proporcional a la
  celda (LiNbO₃: 1 ns, ≈ 1 μW, ≈ 1 fJ). (b) Versión integrada.
- (c) Modulador EO con **celda Pockels entre polarizadores cruzados** (Sec. 20.1B), $V\propto I_o$:

$$\mathcal{T}=\sin^2(\Gamma_0/2-\pi V/2V_\pi) \qquad (23.4\text{-}13)$$

  ($\Gamma_0$, $V_\pi$ constantes) → no monótona → biestable.
- (d) **Acoplador direccional integrado**, $\mathcal{T}=I_o/I_i$ = eficiencia de acople (Sec. 20.1D),
  de (20.1-23):

$$\mathcal{T}=\Big(\frac{\pi}{2}\Big)^2\mathrm{sinc}^2\Big[\tfrac12\sqrt{1+3(V/V_0)^2}\Big] \qquad (23.4\text{-}14)$$

  con $V\propto I_o$ (Ejercicio 23.4-1d).
- **SLM direccionado ópticamente** (Fig. 23.4-15): reflectancia $\mathcal{R}=\mathcal{R}(I_o)$ del lado de
  lectura controlada por la intensidad del lado de escritura; $I_o=I_i\mathcal{R}(I_o)$ → arreglo de
  elementos biestables (cada punto independiente); decenas de ms, < 1 μW.
- Amplificadores láser de InGaAsP como biestables: < 1 fJ, < 1 ns (no linealidad por saturación de
  ganancia).

**Self-Electro-Optic-Effect Device (SEED) (p. 1067–1068).** Fotodiodo p–i–n con MQW en la región
intrínseca, polarizado en inversa (Fig. 23.4-16a). Por el **QCSE** (Sec. 20.5), $\alpha(V)$ es no
lineal en el voltaje (Fig. 23.4-16b) y $\mathcal{T}(V)$ la refleja (c). Realimentación eléctrica: la luz
absorbida genera fotocorriente $i_p=\mathfrak{R}(V)P_i$ ($\mathfrak{R}$ responsividad $\propto\alpha$)
que cae sobre $R_L$: $V=V_0-i_pR_L=V_0-R_L\mathfrak{R}(V)P_i$. Ecuaciones:

$$P_o=\mathcal{T}(V)P_i \qquad (23.4\text{-}15)$$
$$P_i=\frac{1}{\mathfrak{R}(V)}\frac{V_0-V}{R_L} \qquad (23.4\text{-}16)$$

Relación paramétrica $P_o(P_i)$ biestable (Fig. 23.4-16d). La resistencia puede ser un FET u otro
SEED. Dependencia fuerte con λ (QCSE). Sin resonador; no es todo-óptico (circuito eléctrico y fuente
externa); arreglos a velocidades moderadas (decenas de ns) y muy baja potencia.

---

### Reading List (p. 1069–1071)

Libros (selección): El-Bawab, *Optical Switching* (2006); Pavesi & Guillot, *Optical Interconnects:
The Silicon Approach* (2006); Ukita, *Micromechanical Photonics* (2006); Kabacinski, *Nonblocking
Electronic and Photonic Switching Fabrics* (2005); Kawai, *Handbook of Optical Interconnects* (2005);
Ramaswami & Sivarajan, *Optical Networks* (2002); Hinton, *An Introduction to Photonic Switching
Fabrics* (1993); Midwinter, *Photonics in Switching* I y II (1993); Islam, *Ultrafast Fiber Switching
Devices and Systems* (1992); Gibbs, *Optical Bistability: Controlling Light with Light* (1985);
Bowden, Cifton & Roble, *Optical Bistability* (1981).
Artículos (selección): Miller, "Rationale and challenges for optical interconnects to electronic
chips", Proc. IEEE 88, 728 (2000); Miller, "Physical reasons for optical interconnection", Int. J.
Optoelectron. 11, 155 (1997); Glesk et al., "Ultra-fast all-optical switching in optical networks",
Prog. Opt. 45 (2003); Stegeman & Wright, "All-optical waveguide switching", Opt. Quantum Electron. 22,
95 (1990); Reinisch & Vitrant, "Optical bistability", Prog. Quantum Electron. 18, 1 (1994); Lugiato,
"Theory of optical bistability", Prog. Opt. 21 (1984); Miller et al., "The quantum well self-electro-
optic effect device", IEEE J. Quantum Electron. 21, 1462 (1985); Smith & Tomlinson, "Bistable
optical devices promise subpicosecond switching", IEEE Spectrum 18(6), 26 (1981); número especial
sobre AWG/WDM MUX-DEMUX, IEEE JSTQE 8(6) (2002); Cutrona et al., IRE Trans. Inf. Theory IT-6, 386
(1960).

---

## Tablas y datos numéricos útiles

| Magnitud | Valor | Página |
|---|---|---|
| Densidad de puntos conectables por un sistema de imagen | $1000\times1000$ puntos/mm² | 1021 |
| Capacidad de un holograma de interconexión | $ML\le(Ba)^2$ (Ej. 23.1-1); con $B=1000$ líneas/mm → $10^6$ interconexiones/mm² | 1023 |
| Frecuencia portadora óptica vs electrónica | 20–50 THz vs GHz (banda base) | 1027 |
| Velocidad de fotones | 0.3 mm/ps (vacío), ≈0.86 mm/ps (Si) → ≈3.3 y ≈9.4 ps/mm | 1028 |
| Retardo de líneas eléctricas (stripline) | 10.2 ps/mm (cerámica), 6.8 ps/mm (poliimida) | 1028 |
| VCSEL GaAs flip-chip | 850 nm, > 10 Gb/s, ≈ 1 V | 1029 |
| Resolución MZI DEMUX | $\Delta\nu=c/2\Delta d$; $\Delta d=1$ mm, $n=1.5$ → 100 GHz | 1033 |
| Resolución de redes de difracción | diferencias de λ de "unos pocos GHz" | 1031 |
| Superprismas de cristal fotónico | 2–3 órdenes de magnitud más dispersión que un prisma | 1031 |
| Compuertas CMOS | < 0.1 ns, < 1 fJ; MOSFET subpicosegundo; crossbars 128×128 | 1039 |
| MEMS | 10 ms – 10 μs | 1042 |
| Conmutador EO LiNbO₃ (acoplador direccional) | pocos V, > 20 GHz; hasta 32×32 | 1042–1043 |
| Moduladores QCSE/Franz–Keldysh | < 20 ps | 1043 |
| SOA como 1×1 | ns; extinción > 40 dB; 1.3 y 1.55 μm (InGaAsP/InP) | 1043–1044 |
| Acusto-óptico | celdas con $N=2000$ puntos resolubles | 1045 |
| Magneto-óptico | celdas 10×10 μm; arreglos 1024×1024; 100 ns | 1045 |
| Termo-óptico sílice | $dn/dT\approx10^{-5}$ /°C; $L/\lambda_o=2\times10^3$ → $\Delta T=25$ °C para π; ms | 1046 |
| Conmutación con SOA (todo-óptica) | varios cientos de Gb/s | 1047 |
| Solitones | subpicosegundo, decenas de pJ | 1048 |
| Energía mínima (Poisson, BER $10^{-9}$) | 21 fotones; a 1 μm: 26 eV = 4.2 aJ; pesimista 1000 fotones = 20 aJ | 1050 |
| $kT$ a 300 K | 0.026 eV | 1050 |
| Incertidumbre energía–tiempo | $ET\ge h/4\pi$ | 1050 |
| Retardo en fibra de sílice | ≈ 5 ns/m | 1055, 1056 |
| Biestable GaAs | ON pocos ps; OFF ns (200 ps optimizado); 1–10 pJ | 1065–1066 |
| InAs, InSb | OFF hasta 200 ns | 1066 |
| Arreglo biestable 100×100 en 1 cm² GaAs | $E=1$ pJ, $T=100$ ps → 100 W/cm²; $10^{14}$ op/s | 1066 |
| Supercomputadoras electrónicas (2007) | ≈ $10^{10}$ bit-ops/s | 1066 |
| Híbrido Fabry–Perot + Pockels LiNbO₃ | 1 ns, ≈ 1 μW, ≈ 1 fJ | 1066 |
| SLM LC direccionado ópticamente | decenas de ms, < 1 μW | 1067 |
| Amplificador láser InGaAsP biestable | < 1 fJ, < 1 ns | 1067 |
| SEED | decenas de ns, muy baja potencia | 1068 |
| Rango de tiempos (diagrama p. 1041) | all-optical fs–ns; electro-óptico 10 ps–μs; LC μs–ms; termo/mecánico ms | 1041 |

Periodos en $I_o$ de las transmitancias biestables: MZI Kerr $\lambda_o/n_2d$ (p. 1063); Fabry–Perot
Kerr $\lambda_o/2n_2d$ (p. 1064); FP intrínseco $\lambda_o\mathcal{T}_o/2n_2d$ (p. 1064).

---

## Problemas al final del capítulo (p. 1071)

No hay problemas marcados con * en este capítulo.

- **23.1-3 Interconnection Hologram for a Conformal Map.** Diseñar el holograma que realiza
  $x'=\psi_x(x,y)=\ln\sqrt{x^2+y^2}$, $y'=\psi_y(x,y)=\tan^{-1}(y/x)$ (cartesiano→polar seguido de
  logaritmo de $r$). Determinar la función de fase $\varphi(x,y)$ (usar (23.1-7)).
- **23.2-1 Cascaded MZI MUX/DEMUX.** Tres MZI en cascada como en Fig. 23.2-6 para 4 canales con
  $\Delta\lambda=0.2$ nm y λ central 1550 nm; determinar los $\Delta d$ de cada interferómetro si
  $n=2.3$.
- **23.2-2 WGR DEMUX.** WGR (Fig. 23.2-8) para 4 canales con $\Delta\lambda=0.2$ nm y 1550 nm central;
  determinar el parámetro $\Delta d_b$ que debe introducir el star coupler si $n=2.3$.
- **23.2-3 WGR as a 2×2 Wavelength Router.** Entrada 1 con $\lambda_1,\lambda_2$ y entrada 2 con
  $\lambda_3,\lambda_4$; diseñar un enrutador que transponga ($\lambda_1,\lambda_3$ → salida 1;
  $\lambda_2,\lambda_4$ → salida 2). Escribir las condiciones en términos de
  $\Delta d_{11},\Delta d_{12},\Delta d_{21},\Delta d_{22}$.
- **23.3-1 Power Loss and Crosstalk.** 4×4 con cinco 2×2 (Fig. 23.3-3a); cada uno con 0.5 dB de
  pérdida y −30 dB de diafonía; determinar la pérdida y diafonía del peor caso.
- **23.3-2 MZI Crossbar Switch.** MZI electro-óptico como crossbar; $V=V_\pi$ introduce π; bar en
  $V=0$: ¿qué $V$ para cross? Determinar la diafonía (dB) causada por un error del 1 % en el voltaje.
- **23.3-3 TSI Switch.** Implementar el TSI de Fig. 23.3-30 (tiempo→espacio, retardos, conmutación
  espacial, retardos, espacio→tiempo) con las líneas de retardo programables de Fig. 23.3-31.
- **23.4-2 Optical Logic.** A partir de la compuerta AND (Fig. 23.4-4), mostrar cómo hacer NAND, OR
  y NOR; ¿es posible XOR? ¿Sirve el mismo sistema para OR de $N$ entradas?
- **23.4-3 Bistable Interferometer.** Cristal Kerr en un brazo de un MZI; $I_o$ realimentada ilumina
  el cristal. Mostrar que $\mathcal{T}(I_o)=I_o/I_i=\tfrac12+\tfrac12\cos(\pi I_o/I_\pi+\varphi)$
  ($I_\pi$, $\varphi$ constantes). Con $\varphi=0$, graficar $I_o$ vs $I_i$ y obtener la máxima
  ganancia diferencial $dI_o/dI_i$.

(La numeración salta: 23.1-3 sigue a los Ejercicios 23.1-1 y 23.1-2 del texto; 23.4-2 y 23.4-3
siguen al Ejercicio 23.4-1.)

---

## Relación con Óptica No Lineal

**Con los temas del curso:**

- *Ondas EM, haz gaussiano, difracción*: las interconexiones holográficas usan redes de fase
  $\exp[-j2\pi(\nu_xx+\nu_yy)]$ y la relación ángulo–frecuencia espacial $\theta\approx\lambda\nu$
  (p. 1021–1023); el límite de tamaño de conmutadores lo fija la difracción (p. 1050). El
  Ejemplo 23.1-1 identifica la fase de fan-in con la de una lente, $-\pi(x^2+y^2)/\lambda d$ (p. 1024).
- *Absorción y dispersión*: el absorbedor saturable $\alpha=\alpha_0/(1+I/I_s)$ (23.4-8) y la ganancia
  saturable (23.4-12) son no linealidades disipativas; la biestabilidad disipativa (23.4-11) y la
  analogía con el láser (p. 1065).
- *Polarización y cristales*: PBS, rotador de Faraday + λ/2 para circuladores (p. 1025–1026);
  conmutadores EO en LiNbO₃ (p. 1042); celda Pockels entre polarizadores, $\mathcal{T}=\sin^2(\Gamma_0/2-\pi V/2V_\pi)$
  (23.4-13); Kerr anisótropo como retardador controlado por luz (p. 1048).
- *Susceptibilidad no lineal, χ⁽²⁾ y χ⁽³⁾*: convertidores de λ paramétricos: DFG
  $\omega_2=\omega_3-\omega_1$, cascada SHG+DFG, y FWM parcialmente degenerada $\omega_2=2\omega_0-\omega_1$
  en fibra (p. 1053, Fig. 23.3-25c). Interconexiones dinámicas por FWM en fotorrefractivos (p. 1024).
- *Índice dependiente de la intensidad (Kerr)*: $n=n_0+n_2I$ (23.4-2) es el núcleo de: MZI no lineal
  (Fig. 23.2-11, 23.3-17), NOLM/Sagnac asimétrico (p. 1036–1037), TOAD (p. 1047–1048), NLDC con
  ecuaciones acopladas (23.2-8)–(23.2-9) con $\gamma\propto n_2$, y de los biestables dispersivos
  (23.4-4), (23.4-6), (23.4-7). El desfase Kerr $2\pi d\,n_2I/\lambda_o$ aparece explícito.
- *Propagación de pulsos, GVD, SPM/XPM, solitones*: ruptura de pulsos en el NLDC por variación de
  intensidad dentro del pulso y su solución con solitones (fase no lineal constante sobre la
  envolvente, p. 1037); conmutadores por colisión de solitones (corrimiento temporal y de fase);
  solitón vectorial: walk-off por birrefringencia compensado por GVD + XPM → soliton trapping
  (p. 1049). XPM también en SOA para conversión de λ (p. 1053).
- *Raman*: no aparece en este capítulo.
- *Límites físicos*: energía mínima de conmutación por estadística de Poisson (21 fotones, 4.2 aJ a
  1 μm), cota $ET\ge h/4\pi$, y limitación práctica por la debilidad de $n_2$ y la disipación
  térmica (p. 1050–1051): argumentos útiles para discutir por qué el Kerr en Si₃N₄ necesita
  resonadores (realce de intensidad) o longitudes largas.

**Con el proyecto final (anillos add-drop en Si₃N₄, sensado de índice, dispersión, supercontinuo):**

- El **OADM con microanillos** (Fig. 23.2-4, p. 1032) es exactamente la topología add-drop del
  proyecto (bus input→output, add→drop); el libro afirma que anillos múltiples acoplados dan menor
  ancho espectral y mayor rechazo que uno solo, lo que da un argumento de diseño (y un posible
  estudio comparativo) para la selectividad del sensor. El DEMUX con anillos en serie (Fig. 23.2-2e)
  es el mismo principio con varias λ.
- El **sensado refractométrico** se apoya en que la resonancia depende del índice efectivo: el
  capítulo muestra la misma física (corrimiento de la transmitancia por $\Delta n$) en los
  conmutadores termo-ópticos (desfase $(2\pi L/\lambda_o)\Delta n$, p. 1046) y en los Fabry–Perot
  Kerr (23.4-6): sustituir $n_2I$ por $\partial n_{\rm eff}/\partial n_{\rm clad}\,\Delta n_{\rm clad}$ da la
  sensibilidad espectral del anillo.
- Las **transmitancias de interferómetros** (23.2-3), (23.2-4), (23.4-5) y su dependencia en λ
  (resolución $\Delta\nu=c/2\Delta d$, picos del multicamino) son el lenguaje para FSR, fineza y Q del
  anillo (ver skill `lumerical-analisis-resultados`).
- Para **supercontinuo y Kerr en el anillo**: el análisis de biestabilidad del Fabry–Perot Kerr
  intrínseco (23.4-7) es el modelo mínimo de la biestabilidad térmica/Kerr que aparece en
  microanillos bombeados; el periodo $\lambda_o\mathcal{T}_o/2n_2d$ indica cuánta potencia
  intracavidad desplaza la resonancia un FSR. Las ecuaciones del NLDC (23.2-8)–(23.2-9) son el
  punto de partida para un acoplador anillo–bus con Kerr.
- **Dispersión de guías**: el soliton trapping (GVD compensando birrefringencia vía XPM, p. 1049)
  y la dependencia $\Delta d_m$ vs λ del WGR (23.2-5) ilustran cómo la dispersión de la guía
  (de material y geométrica) entra en el diseño; para Si₃N₄ el mismo cálculo de $n_{\rm eff}(\lambda)$
  que hace el estudio `seccion_v1` alimenta tanto el FSR del anillo como la GVD para el supercontinuo.
- Referencias citadas para profundizar: Stegeman & Wright (1990) sobre conmutación todo-óptica en
  guías; Islam (1992) sobre conmutación ultrarrápida en fibra; Gibbs (1985) sobre biestabilidad;
  número especial de IEEE JSTQE 8(6) (2002) sobre AWG/WDM.
