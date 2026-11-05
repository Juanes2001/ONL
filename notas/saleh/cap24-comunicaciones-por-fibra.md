# Capítulo 24 — Optical Fiber Communications (Saleh & Teich, 2.ª ed.)

Páginas del libro 1072–1121 (PDF 1094–1143). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 24.
Convención del libro: dependencia temporal $e^{j\omega t}$ con $j=\sqrt{-1}$; campos reales en
caligráfica $\mathcal E(t)$, amplitudes complejas en negrita o con mayúscula ($A_s$, $A_L$);
potencias en dBm se escriben con tipografía sans ($\mathsf P$) en el libro y aquí como $\mathsf{P}$.
Los nombres de las secciones y los números de ecuaciones son los del libro. Las secciones
marcadas con `*` son las que el libro marca como avanzadas/opcionales.

---

## Resumen del capítulo

El capítulo es una introducción a los sistemas y redes de comunicación por fibra óptica, y
sirve de síntesis aplicada de los caps. 9 (fibras), 14 (amplificadores), 17 (fuentes), 18
(detectores), 22 (pulsos) y 23 (dispositivos). La §24.1 resume los componentes: fibras (MMF,
GRIN, SMF; atenuación y dispersión del sílice; fibras DSF/NZ-DSF/DCF; PMD; efectos no lineales
SPM/XPM/FWM/SRS/SBS), fuentes (LED, láseres DFB), amplificadores (EDFA, REFA, Raman, SOA, OPA) y
detectores (p-i-n, APD). La §24.2 modela el enlace punto a punto como un sistema lineal con
atenuación y tiempo de respuesta, introduce la tasa de error de bit y la sensibilidad del receptor,
y construye el **presupuesto de potencia** (enlace limitado por atenuación, $L = L_0 - (10/\alpha)\log B_0$)
y el **presupuesto de tiempo** (enlace limitado por dispersión, $LB_0 = c_1/2\Delta$ para MMF,
$LB_0 = 1/4|D_\lambda|\sigma_\lambda$ para SMF, $LB_0^2 = \pi c_o/4|D_\lambda|\lambda_o^2$ para pulsos
limitados por transformada); luego trata la compensación de atenuación con amplificadores, la
compensación de dispersión con fibras DCF ($D'_\lambda L' = -D_\lambda L$), la gestión de dispersión
para WDM y las comunicaciones con solitones (condición $2\pi n_2 I_0/\lambda_o = -\beta''/\tau_0^2$,
periodo de interacción $L_p = \pi e^{r/2} z_0$). La §24.3 cubre modulación (de campo vs. de
intensidad, OOK/FSK/PSK, PCM) y multiplexación (FDM, TDM, CDM, WDM, CWDM/DWDM). La §24.4 trata
las topologías de red, el acceso múltiple, SONET y las redes WDM (broadcast-and-select,
multi-hop, wavelength-routed con OADM y OXC). La §24.5 describe la detección coherente
(heterodina/homodina), la corriente de fotomezcla $\bar i \approx \bar i_L + 2\sqrt{\bar i_s\bar i_L}\cos[2\pi\nu_I t+(\varphi_s-\varphi_L)]$,
y la sensibilidad de receptores coherentes analógicos (SNR $=2\bar m$) y digitales (OOK homodino
18 fotones/bit, PSK homodino 9 fotones/bit).

---

## Secciones

### Introducción (p. 1073)

- Hasta mediados de los 70 la comunicación era por cable eléctrico o radio/microondas. Las dos
  invenciones que habilitaron la comunicación "lightwave" fueron el **LED** y la **fibra de bajas
  pérdidas**. Los primeros sistemas usaron LED; los de larga distancia usan láser (potencia, ancho
  de línea estrecho, directividad). La luz es poco apta para espacio libre (nubes, niebla) (p. 1073).
- Un enlace punto a punto tiene tres elementos (Fig. 24.0-1, p. 1074): fuente modulada (E/O),
  fibra de baja pérdida/baja dispersión, y fotodetector (O/E). Para fibras largas se insertan
  **amplificadores ópticos** (OA) o bien **regeneradores/repetidores** (amplificación eléctrica y
  regeneración de la señal entre enlaces).
- Plan del capítulo: §24.1 componentes; §24.2 diseño de sistemas digitales y analógicos con
  modulación de intensidad (longitud máxima a tasa dada); §24.3 modulación y multiplexación;
  §24.4 redes (incluyendo WDM); §24.5 sistemas coherentes (luz como onda EM de amplitud, fase o
  frecuencia controlable → mayor sensibilidad del receptor).

---

### 24.1 Fiber-Optic Components (p. 1074)

#### 24.1A Optical Fibers (p. 1074)

Fibra = guía de onda dieléctrica cilíndrica de sílice fundido de alta pureza; en la fibra de
índice escalonado el núcleo tiene índice ligeramente mayor que el revestimiento y guía por
reflexión total interna. Se caracteriza por el radio del núcleo $a$, los índices $n_1$ (núcleo) y
$n_2$ (cladding), y el cambio fraccional de índice $\Delta = (n_1-n_2)/n_1$, usualmente muy pequeño
($\Delta = 0.001$–$0.02$). Se guían los rayos con ángulo respecto al eje menor que el complemento del
ángulo crítico $\bar\theta_c = \cos^{-1}(n_2/n_1)$, lo que corresponde a un ángulo de aceptación
$\theta_a = \sin^{-1}(\mathrm{NA})$ desde el aire (p. 1074–1075).

**Apertura numérica** (recuadro, p. 1075):
$$\mathrm{NA} = \sin\theta_a = \sqrt{n_1^2 - n_2^2} \approx n_1\sqrt{2\Delta}. \tag{24.1-1}$$

**Fibras multimodo (MMF)** (p. 1075). El número de modos $M$ lo gobierna el parámetro
$V = 2\pi(a/\lambda_o)\,\mathrm{NA}$; para $V\gg 1$, $M\approx V^2/2$. Los modos viajan con distintas
velocidades de grupo → **dispersión modal**, que crece linealmente con $L$. El pulso compuesto
tiene anchura RMS aproximada (recuadro, "Response Time, Step-Index MMF"):
$$\sigma_{\text{fiber}} \approx \frac{\Delta}{2c_1}L, \qquad c_1 = c_o/n_1. \tag{24.1-2}$$
Ejemplo en el texto: $n_1 = 1.46$, $\Delta = 0.01$ → tiempo de respuesta por km $\approx \Delta/2c_1 \approx 24$ ns/km;
para 100 km un impulso se ensancha a 2.4 µs. En fibras de **índice gradual (GRIN)** el índice baja
de $n_1$ en el eje a $n_2$ en la frontera; los rayos oblicuos recorren más camino pero a mayor
velocidad de fase, lo que iguala los retardos. Con perfil óptimo (≈ parabólico) el ensanchamiento
(ps/km) es el de la fibra escalonada equivalente multiplicado por $\Delta/2$ (para $\Delta = 0.01$,
factor 500 de reducción; en la práctica no se alcanza por la dificultad de fabricar el perfil ideal).

**Fibras monomodo (SMF)** (p. 1075). Si $a$ y NA son tan pequeños que $V < 2.405$, solo se guía un
modo. Se elimina la dispersión modal, pero queda la **dispersión cromática** (velocidad de grupo
dependiente de $\lambda$, con fuente de ancho espectral finito), que tiene dos orígenes:
**dispersión del material** (índice dependiente de $\lambda$) y **dispersión de guía de onda**
(velocidad de grupo del modo depende de $a/\lambda$). La del material suele ser mayor.
Un pulso corto de ancho espectral $\sigma_\lambda$ se ensancha a (recuadro, "Response Time (SMF)", p. 1076):
$$\sigma_{\text{fiber}} = |D|\,\sigma_\lambda L, \tag{24.1-3}$$
con $L$ en km, $\sigma_\lambda$ en nm y $D$ el coeficiente de dispersión en ps/km-nm; para fibras
débilmente guiantes ($\Delta\ll1$), $D \approx D_\lambda + D_w$ (material + guía). Ejemplo: $\sigma_\lambda = 1$ nm,
$D = 1$ ps/km-nm (cerca de 1300 nm) → $\sigma_\tau/L = 1$ ps/km; 100 km → 100 ps.

Figura 24.1-1 (p. 1076): compara (a) MMF escalonada (núcleo grande, gran ensanchamiento modal),
(b) MMF GRIN (menos modos, menor ensanchamiento), (c) SMF (núcleo pequeño, solo dispersión material
y de guía), con sus perfiles de índice y respuestas al impulso $h(t)$.

**Material Attenuation and Dispersion** (p. 1076–1077). Atenuación del sílice (Fig. 24.1-2, p. 1077):
mínimo local ≈ 0.3 dB/km en $\lambda_o = 1300$ nm, pico de absorción OH⁻ en 1.4 µm, mínimo absoluto
≈ 0.16 dB/km en 1550 nm, luego sube abruptamente. Existen fibras con OH suprimido (línea punteada).
El coeficiente de dispersión $D_\lambda$ pasa de negativo (λ cortas) a positivo (λ largas) y se anula
en $\lambda_o \approx 1312$ nm. **Dispersión normal**: $D_\lambda<0$, las componentes de λ corta viajan
más lento que las de λ larga. **Dispersión anómala**: $D_\lambda>0$ (ver §5.6). El signo no afecta la
tasa de ensanchamiento pero sí importa en cascadas de materiales de signo distinto (§24.2D, §22.3).

Pie de la Fig. 24.1-2 (p. 1077): tres bandas históricas: 870 nm (primeros sistemas; $\alpha\approx1.5$ dB/km,
$D_\lambda\approx-80$ ps/km-nm); banda O (original) centrada en 1310 nm ($\alpha=0.3$ dB/km, dispersión
mínima); banda C (convencional) centrada en 1550 nm ($\alpha=0.16$ dB/km, $D_\lambda = +80$ ps/km-nm
— nota: en el pie dice +80, mientras en §24.2 se usa 17 ps/km-nm para la fibra convencional en 1550 nm;
el valor usual de la fibra estándar es ≈ 17 ps/km-nm). Bandas adicionales para WDM: E (extended),
S (short), L (long), U (ultra-long). Límites en nm leídos de la figura: O 1260–1360, E 1360–1460,
S 1460–1530, C 1530–1565, L 1565–1625, U 1625–1675.

**Dispersion-Modified Fibers (DSF)** (p. 1077–1078). Fibras monomodo con núcleo de índice gradual
y perfiles especiales (§9.3B) para que $D$ tome valores deseados:
- **Dispersion-shifted fibers (DSF)**: $D = 0$ en 1550 nm (donde la atenuación es mínima) en vez de
  1312 nm. **Non-zero dispersion-shifted (NZ-DSF)**: $D$ reducido pero no nulo en 1500–1600 nm;
  "una pequeña dispersión es útil para aliviar las distorsiones no lineales de pulsos intensos y
  estrechos" (p. 1077). Fig. 24.1-3 (p. 1078): $D(\lambda)$ de fibra convencional (cruza cero en
  ≈1310 nm y llega a ≈ 17–20 ps/km-nm en 1550–1600), DSF (G.653, cero en 1550) y NZ-DSF (G.655,
  pequeña pendiente positiva, cero cerca de 1500). G.653 y G.655 son especificaciones de la ITU.
- **Dispersion-flattened**: $D=0$ en dos longitudes de onda y pequeño entre ellas [Fig. 9.3-6(b)].
- **Dispersion compensating (DCF)**: $D$ proporcional al de la fibra convencional en una banda
  extendida pero de signo opuesto; un tramo corto con $|D|$ grande compensa el ensanchamiento de
  un tramo largo convencional [Fig. 9.3-6(c)].
- **Holey fibers** y **photonic-crystal fibers (PCF)** (§9.4): la dispersión cromática está dominada
  por la dispersión de guía, que depende fuertemente de la geometría de los huecos; permiten
  aplanar la dispersión en bandas anchas y correr el cero a λ menores que el cero del material.
  Pueden ser "endlessly single-mode". Las de núcleo hueco con cladding de cristal fotónico guían
  por reflexión del cladding: menores pérdidas y **menores efectos no lineales** (p. 1078).

**Polarization-Mode Dispersion (PMD)** (p. 1078). Cambios anisotrópicos aleatorios de la
birrefringencia a lo largo de la fibra (factores ambientales) producen retardos diferenciales entre
los dos modos de polarización (§9.3B). El valor RMS del ensanchamiento crece con la raíz de la
longitud (recuadro):
$$\sigma_{\text{PMD}} = D_{\text{PMD}}\sqrt{L}, \tag{24.1-4}$$
con $D_{\text{PMD}}$ típicamente 0.1–1 ps/√km. Importa a altas tasas cuando las otras dispersiones
ya se compensaron.

**Nonlinear Optical Effects** (p. 1078–1079). El sílice presenta dos tipos de no linealidad:
**de tercer orden** (efecto Kerr óptico) y **dispersión inelástica estimulada** (Raman y Brillouin).
Con pulsos de alta potencia en SMF (área transversal pequeña) la intensidad es suficiente para
que aparezcan efectos que degradan la señal:
- **Self-phase modulation (SPM)**: dispersión no lineal causada por el efecto Kerr (índice, y por
  tanto velocidad de fase, dependiente de la intensidad, §21.3A). Distintos segmentos del pulso
  viajan a distinta velocidad → ensanchamiento (§22.3B). El Kerr también produce crosstalk entre
  ondas contrapropagantes en sistemas bidireccionales.
- **Cross-phase modulation (XPM)**: la velocidad de fase de una onda depende de las intensidades
  de ondas de otras λ en la misma fibra (§21.3C); en WDM causa crosstalk serio entre canales.
- **Four-wave mixing (FWM)**: también de tercer orden (§21.3D); crosstalk entre cuatro ondas de
  distinta λ que intercambian energía → ganancia/pérdida dependiente de la intensidad en canales WDM.
- **Stimulated Raman (SRS)** y **Brillouin (SBS)**: dispersión inelástica con vibraciones
  moleculares (SRS) o acústicas (SBS) del medio; dos ondas de distinta λ interactúan vía la onda
  de vibración (§13.5C, 14.3D, 15.3A). Crosstalk indeseado entre canales WDM.

Las no linealidades también se aprovechan: la SPM puede ajustarse para compensar la dispersión
cromática → **solitones ópticos** (§22.5B); FWM o SRS dan ganancia útil (amplificadores Raman, §14.3D).

#### 24.1B Sources for Optical Transmitters (p. 1079)

Requisitos: **potencia** (señal detectable tras la fibra), **velocidad** de modulación, **ancho de
línea** estrecho (minimizar dispersión cromática), bajo **ruido** (crítico en coherente), y
robustez, insensibilidad térmica, fiabilidad, bajo costo, larga vida (p. 1079).

- **LED** (cap. 17): de superficie (robustos, baratos, fiables; ancho de línea muy grande, > 100 nm
  en 1300–1600 nm, Fig. P17.1-5; modulación hasta 100 Mb/s a potencia máxima, hasta 500 Mb/s a
  potencia reducida) y de borde (estructura tipo láser sin realimentación; más potencia y ancho
  de línea algo menor, más complejos) (p. 1079–1080).
- **Diodos láser**: alta potencia (decenas de W), alta velocidad (muchos Gb/s), ancho de línea
  estrecho (decenas de MHz), fácil acoplamiento a SMF; sensibles a temperatura. Los multimodo
  sufren **ruido de partición** (distribución aleatoria de potencia entre modos → con dispersión
  cromática, fluctuaciones de intensidad). **Chirp de frecuencia**: cambio de la frecuencia del
  láser al modular la potencia, por el cambio del índice con la concentración de portadores (p. 1080).
- Materiales: AlInGaP/InGaP (LED 600–650 nm, fibra plástica); In$_{1-x}$Ga$_x$As$_{1-y}$P$_y$
  (gap directo sintonizable, casado a InP) para LED y LD en el IR cercano; InGaAsP a 1.3 µm para
  cortas distancias; a 1.55 µm sistemas de larga distancia con LD acoplado a SMF (p. 1080).
- Configuración más común: **láser DFB** (Fig. 24.1-4, p. 1080: heteroestructura enterrada con pozos
  cuánticos múltiples InGaAsP/InGaAs sobre InP, rejilla DFB adyacente a la región activa). Emite en
  un solo modo espacial, potencia de salida de 1 W o más; umbral $i_t<10$ mA y responsividad
  diferencial $\mathfrak R_d\approx0.4$ W/A. Anchos espectrales estrechos, críticos para WDM a 1.3 y 1.55 µm.

#### 24.1C Optical Amplifiers (p. 1080)

Usos (Fig. 24.1-5, p. 1081): **postamplificador** (de potencia, antes de lanzar a la fibra),
**amplificador de línea** (repetidor), **preamplificador** (antes del fotodetector).
Tres clases: **OFA** (fibra: EDFA, REFA, RFA), **SOA** (semiconductor, §17.2) y **OPA** (paramétrico,
§21.4C). Salvo el OPA, todos son no paramétricos (intercambio de energía con el medio).

- **EDFA** (§14.3C): ganancia independiente de la polarización, alta potencia de salida, baja
  pérdida de inserción, bajo ruido, transición ancha en 1.55 µm. Bombeo longitudinal con LD de
  InGaAs a 980 nm (co-, contra- o bidireccional). Ganancias > 50 dB con decenas de mW de bombeo;
  salidas > 100 W. Ancho de banda $\Delta\lambda\approx40$ nm ↔ $\Delta\nu\approx5.3$ THz (cubre la banda C;
  la L también con optimización distinta). Ideal para WDM (p. 1081).
- **REFA** (Pr³⁺, Tm³⁺, Nd³⁺): cubren bandas O/E/S/U, extienden más allá de los 60 nm (7.5 THz)
  que dan EDFA C+L. Funcionan mejor en vidrios fluoruro/telurito (problemas: matriz de sílice
  dominante, cada REFA necesita su propia fibra, empalmes difíciles, cada uno su bombeo). Mezclando
  Er³⁺ y Tm³⁺, $\Delta\lambda\approx150$ nm ↔ $\Delta\nu\approx18.8$ THz en 1550 nm (p. 1081–1082).
- **Raman (RFA)** (§14.3D): basado en SRS (§13.5C). **Distribuido** (la fibra de transmisión es el
  medio de ganancia) o **concentrado** (tramo corto de fibra muy no lineal). Ancho de banda de
  ganancia Raman ≈ 100 nm (≈ 12.5 THz en 1550 nm); con múltiples bombeos puede cubrir toda la
  región de transparencia. Ganancia ≈ 20 dB (menor que EDFA), eficiencia menor (se mejora con DCF);
  requiere bombeo con diversidad de polarización (p. 1082).
- **SOA** (§17.3): cualquier región espectral eligiendo el material; compactos, integrables,
  bombeo eléctrico; InGaAsP/InGaAs/InP; $\Delta\lambda\approx50$ nm ($\Delta\nu\approx6.5$ THz) con pozos
  cuánticos, ≈ 200 nm con puntos cuánticos. Baja ganancia (≈ 15 dB) → redes metropolitanas
  (compensar pérdidas de nodos add-drop). Desventajas: incompatibilidad con la geometría de la fibra,
  interferencia intercanal e intersímbolo, alto ruido, sensibilidad a temperatura y polarización;
  más útiles para conmutación toda-óptica y conversión de longitud de onda (p. 1082).
- **OPA** (§21.2C, 21.4C): ganancia grande y sintonía amplia (IR–visible), pero limitado en WDM:
  requiere **phase matching** de las señales WDM con el bombeo (necesita aplanamiento de dispersión);
  el FWM impide WDM con canales equiespaciados; sensible a polarización (p. 1082–1083).
  Conclusión del libro: SOA y OPA son menos útiles que los OFA.

#### 24.1D Detectors for Optical Receivers (p. 1083)

Dos tipos: fotodiodo **p-i-n** y **APD** (cap. 18). El APD da ganancia antes de la primera etapa
electrónica (reduce el efecto del ruido de circuito), pero su mecanismo de ganancia añade ruido y
tiene tiempo de respuesta finito; requiere más voltaje y circuitería (compensación térmica). SNR y
sensibilidad en §18.6.
- **870 nm**: Si p-i-n y APD. Los APD de Si tienen ventaja de 10–15 dB en sensibilidad (p. 1083).
- **1300–1600 nm**: Si es transparente (gap por debajo). Se usan InGaAs y Ge; InGaAs preferido
  (menor corriente oscura, estabilidad térmica). InGaAs p-i-n típicos: $\eta\approx0.8$,
  $\mathfrak R\approx1$ A/W, ancho de banda ≈ 10 GHz en 50 Ω, corriente oscura ≈ 0.1 nA (guías de onda
  dan más ancho de banda). APD de InGaAs: corrientes de fuga por túnel a campo alto → heteroestructura
  con absorción en InGaAs y multiplicación en InP (SAM APD) y versión con capa de gradación InGaAsP
  (**SAGM APD**, Fig. 24.1-6, p. 1084). Como multiplican huecos, el cociente de ionización relevante
  es $1/k$ (≈ 0.5 en InP con $\bar G = 10$): ruido de ganancia mayor que en Si. Típicos: $\eta\approx0.8$,
  $\mathfrak R\approx10$ A/W, ancho de banda ≈ 10 GHz, producto ganancia-ancho de banda ≈ 100 GHz,
  corriente oscura ≈ 0.1 nA (p. 1083).

---

### 24.2 Optical Fiber Communication Systems (p. 1084)

Enlace punto a punto: la información es un **señal** (variable física) *modulada* en un punto y
observada en otro. Multiplexación: varias señales en el mismo enlace distinguidas por un atributo
(tiempo, frecuencia, longitud de onda) o código. En fibra, la variable modulada puede ser
intensidad, amplitud, frecuencia, fase o polarización; el ejemplo más simple es la **modulación de
intensidad** (Fig. 24.2-1, p. 1084: analógica — potencia proporcional a la señal; digital ON–OFF
keying — "1" y "0" por presencia/ausencia de pulso). El ejemplo más simple de multiplexación óptica
es **WDM** (Fig. 24.2-2, p. 1084).

Medidas de desempeño (p. 1084–1085): para sistema analógico, el **ancho de banda** $B$ (Hz) (máxima
frecuencia de modulación tal que la señal recibida es detectable con SNR prescrita); para digital,
la **tasa de bits** máxima $B_0$ (b/s) con tasa de error bajo un valor prescrito. Ambas dependen de
atenuación, ensanchamiento de pulso y ruido en el receptor.

**Tabla 24.2-1** (p. 1085) — tasas aproximadas del estándar SONET:

| OC-1 | OC-3 | OC-12 | OC-24 | OC-48 | OC-192 | OC-768 |
|---|---|---|---|---|---|---|
| 52 Mb/s | 156 Mb/s | 622 Mb/s | 1.25 Gb/s | 2.5 Gb/s | 10 Gb/s | 40 Gb/s |

#### 24.2A Evolution of Optical Fiber Communication Systems (p. 1085)

Mínimo de atenuación en ≈ 1550 nm; mínimo de dispersión del material en ≈ 1312 nm. Los primeros
sistemas operaron en ≈ 870 nm (LED y LD de AlGaAs) con atenuación y dispersión altas. Fig. 24.2-3
(p. 1086): mapa de fuentes (AlGaAs 800–900 nm; InGaAsP 1100–1650), detectores (Si < 1000 nm; Ge e
InGaAs 1000–1650), amplificadores (SOA AlGaAs ~870, InGaAsP 1300–1600; OFA: EDFA ~1530–1620, REFA,
RFA más anchos) y fibras (MMF SI/GRIN de sílice 870–1600; SMF; DSF en 1550). La evolución ha sido
MMF→SMF, LED→LD, p-i-n→APD, SOA→OFA. Medida de progreso: el producto **$LB_0$** (km-b/s) (tasa ×
separación de repetidores). Las tres primeras generaciones aumentaron $LB_0$ ×1000 entre 1974 y los 90;
luego otros cinco órdenes de magnitud de 1990 a 2005: "×10 cada 4 años", la **"ley de Moore óptica"**
(p. 1085; Fig. 24.2-4, p. 1087).

Sistemas (p. 1086–1087):
1. **MMF a 870 nm** (años 70): LED o láser AlGaAs, Si p-i-n/APD; limitado por atenuación y
   dispersión modal. Típico $B_0 = 100$ Mb/s, $L = 10$ km, $LB_0 = 1$ km-Gb/s.
2. **SMF a 1310 nm**: dispersión del material mínima; limitado por atenuación. Láser InGaAsP, InGaAs
   p-i-n/APD (o Ge APD). OC-12 (622 Mb/s) con $L = 40$ km, $LB_0\approx25$ km-Gb/s.
3. **SMF a 1550 nm**: atenuación mínima; limitado por dispersión del material, reducida con DFB de
   bajo chirp y luego DSF. Ejemplo: 2.5 Gb/s (OC-48) a 100 km, $LB_0 = 250$ km-Gb/s; con OC-192
   (10 Gb/s), $LB_0\approx1$ km-Tb/s.
4. **Coherente**: mezcla con oscilador local (§24.5); mayor sensibilidad → mayores distancias;
   mayor complejidad; su comercialización se rezagó por la aparición de los OFA.
5. **Enlace con amplificadores ópticos**: compensan atenuación entre repetidores electrónicos.
   TPC-5 transpacífico: $B_0 = 10$ Gb/s, $L = 20\,000$ km, $LB_0 = 200$ km-Tb/s.
6. **Solitones**: pulsos cortos (1–50 ps) que viajan sin cambiar su envolvente porque dispersión
   y SPM (Kerr) se cancelan (§22.5B); los EDFA compensan pérdidas. Experimentales: 10 Gb/s sobre
   > 12 000 km ($LB_0 = 1200$ km-Tb/s).
7. **WDM**: múltiples canales por fibra con amplificadores de banda ancha. TPC-6: $B_0 = 100$ Gb/s,
   $L = 9000$ km, $LB_0 = 900$ km-Tb/s. Con gestión de dispersión y corrección de errores (FEC):
   5–10 Tbit/s por fibra sobre 10 000 km.

#### 24.2B Performance of Optical Fiber Systems (p. 1087)

**Modelo lineal de la fibra** (p. 1088): respuesta al impulso $h(t)$ y función de transferencia
$H(f)$, con $f$ la frecuencia de modulación. Tres parámetros:
- *Transmisión de potencia*: $H(0) = \int h(t)\,dt$. Para fibra de longitud $L$ y atenuación $\alpha$
  (dB/km), $H(0) = \exp[-\alpha L]$ donde $\alpha\approx0.23\alpha$ es la atenuación en km⁻¹ (el libro
  usa el mismo símbolo; $0.23 = \ln 10/10$). Pérdidas localizadas en acopladores pueden incluirse en
  $\alpha$ como dB/km distribuidos.
- *Tiempo de respuesta* $\sigma_\tau$: anchura de $h(t)$; fija la tasa máxima en sistemas digitales;
  proporcional a $L$. En SMF, $\sigma_\tau = |D|\sigma_\lambda L$.
- *Ancho de banda* $\sigma_f$: anchura de $|H(f)|$; inversamente proporcional a $\sigma_\tau$; el
  libro usa $\sigma_f = 1/2\pi\sigma_\tau$ a modo ilustrativo (Apéndice A, §A.2).

**Impedimentos** que fijan la longitud máxima (p. 1088–1089; Fig. 24.2-5):
- *Atenuación*: caída exponencial de la potencia con la distancia; límite cuando cae bajo la
  **sensibilidad del receptor** [Fig. 24.2-5(a)].
- *Dispersión*: la anchura del pulso crece con la distancia; cuando supera el intervalo de bit
  hay **interferencia intersímbolo (ISI)**; en analógico, lava las altas frecuencias y reduce el
  ancho de banda [Fig. 24.2-5(b)].
- *Ruido* de amplificadores ópticos y de efectos aleatorios de propagación (PMD).
- *Distorsión no lineal* de pulsos intensos: mezcla de componentes espectrales e interferencia
  entre señales WDM.

Por qué el sistema es más sensible a altas tasas (p. 1089; Fig. 24.2-6): (a) a potencia media fija,
mayor tasa = menos fotones por bit → más ruido fotónico → la sensibilidad del receptor crece con $B_0$;
(b) pulsos más cortos tienen espectro más ancho → más ensanchamiento → más ISI;
(c) a energía por bit fija, mayor tasa requiere más potencia pico → interacciones no lineales
("ISI no lineal"). Diseño de un enlace de larga distancia: elegir fibras de menor atenuación y/o
dispersión, presupuestar potencia y anchura de pulso, y evitar los efectos no lineales de pulsos
ultraintensos.

**Bit-Error Rates** (p. 1089–1090). Desempeño digital medido por la probabilidad de error por bit
(**BER**). Con OOK, $p_1$ = prob. de confundir "1" por "0", $p_0$ la inversa; con bits equiprobables
$\mathrm{BER} = \tfrac12 p_1 + \tfrac12 p_0$. Valor aceptable típico: $10^{-9}$. Errores por ruido o
por ensanchamiento hacia bits vecinos (ISI). **Diagrama de ojo** (Fig. 24.2-7, p. 1090): realizaciones
aleatorias superpuestas del "1" y del "0"; cuanto más abierto el ojo, menos probable el error; el ojo
se cierra con ruido y ensanchamiento.

**Receiver Sensitivity** (p. 1090). Sensibilidad de un receptor digital = mínimo número de fotones
(o energía) por bit que garantiza BER menor que la prescrita (p. ej. $10^{-9}$). Con láser
estabilizado, $\eta=1$ y sin ruido de circuito, se requieren $\bar n_0 = 10$ fotones por bit en promedio
para BER $\le 10^{-9}$: *la sensibilidad del receptor ideal es 10 fotones/bit* (el "1" lleva ≥ 20
fotones, el "0" ninguno). Sensibilidad $\bar n_0$ ↔ energía $h\nu\bar n_0$ por bit ↔ potencia
$$P_r = h\nu\,\bar n_0 B_0, \tag{24.2-1}$$
proporcional a la tasa. Cuando importa el ruido de circuito, $\bar n_0$ depende del ancho de banda
del receptor (de $B_0$); el libro supone $\bar n_0$ independiente de $B_0$ por simplicidad.

#### 24.2C Attenuation- and Dispersion-Limited Systems (p. 1090)

Sistema OOK digital de intensidad, sin efectos no lineales ni ruido de la fibra. Datos: tasa $B_0$,
distancia $L$ (km), fuente de potencia $P_s$ (mW), $\lambda$ (nm), ancho espectral $\sigma_\lambda$ (nm);
fibra con $\alpha$ (dB/km) y $D_\lambda$ (ps/km-nm); receptor con sensibilidad $\bar n_0$ (fotones/bit) ↔
$P_r = (hc/\lambda)\bar n_0 B_0$ (mW). Se busca la máxima $L$ a $B_0$ dada (o la máxima $B_0$ a $L$ dada):
el producto $LB_0$ describe la capacidad del enlace (p. 1090–1091).

Dos condiciones (p. 1091): (1) potencia recibida ≥ sensibilidad $P_r$ (**presupuesto de potencia**;
margen usual de 6 dB sobre $P_r$); (2) anchura del pulso recibido no mucho mayor que el bit
$1/B_0$ (**presupuesto de tiempo/dispersión**). Si al alargar $L$ falla primero (1) el enlace está
*limitado por atenuación*; si falla (2), *limitado por dispersión*.

**Attenuation-Limited Performance: Power Budget** (p. 1091–1092). Unidades dBm (recuadro):
$$\mathsf P = 10\log_{10}P, \qquad P \text{ en mW},\ \mathsf P \text{ en dBm}. \tag{24.2-2}$$
($P = 0.1$, 1, 10 mW ↔ $-10$, 0, 10 dBm). Con $\mathsf P_s$ potencia de la fuente (dBm), $\alpha$ pérdida
(dB/km), $\mathsf P_c$ pérdidas de empalme y acoplamiento (dB), $\mathsf P_m$ margen de seguridad:
$$\mathsf P_s - \mathsf P_c - \mathsf P_m - \alpha L = \mathsf P_r \quad(\text{dB}). \tag{24.2-3}$$
(Fig. 24.2-8, p. 1092: potencia vs. $z$ con escalones por conectores y pendiente $\alpha$.)
La sensibilidad en dBm, de (24.2-1):
$$\mathsf P_r = 10\log\frac{\bar n_0 h\nu B_0}{10^{-3}}\ \text{dBm}, \tag{24.2-4}$$
crece logarítmicamente con $B_0$ (Fig. 24.2-9, p. 1092). Longitud máxima:
$$L = \frac1\alpha\left(\mathsf P_s - \mathsf P_c - \mathsf P_m - 10\log\frac{\bar n_0 h\nu B_0}{10^{-3}}\right), \tag{24.2-5}$$
de donde (recuadro, "Attenuation-Limited Fiber"):
$$L = L_0 - \frac{10}{\alpha}\log B_0, \qquad L_0 = \frac{\mathsf P_s - \mathsf P_c - \mathsf P_m - 30 - 10\log(\bar n_0 h\nu)}{\alpha}. \tag{24.2-6}$$
$L$ cae logarítmicamente con $B_0$ con pendiente $10/\alpha$. Fig. 24.2-10 (p. 1093): $L$ vs $B_0$ para
870 nm ($\alpha=2.5$ dB/km), 1300 nm (0.35 dB/km) y 1550 nm (0.16 dB/km), con $P_s = 1$ mW (0 dBm),
$\bar n_0 = 300$ fotones/bit (870 y 1300) y $\bar n_0 = 1000$ (1550), $\mathsf P_c = \mathsf P_m = 0$; se compara
con cable coaxial (mucho peor). Lectura: a 1550 nm $L\approx 300$–100 km de 100 kb/s a 10 Gb/s;
a 870 nm ≈ 30–10 km.

**Dispersion-Limited Performance: Time Budget** (p. 1092–1094). El pulso final de anchura $\sigma_r$
resulta de la anchura original $\sigma_s$, el tiempo de respuesta del transmisor $\sigma_{\rm tx}$, de
la fibra $\sigma_\tau$ y del receptor $\sigma_{\rm rx}$ (convolución). Si todas son gaussianas:
$$\sigma_o^2 = \sigma_s^2 + \sigma_{\rm sys}^2, \tag{24.2-7}$$
$$\sigma_{\rm sys}^2 = \sigma_{\rm tx}^2 + \sigma_{\rm rx}^2 + \sigma_\tau^2, \tag{24.2-8}$$
usadas en la práctica aunque las respuestas no sean gaussianas. Condición de diseño: la anchura
recibida no excede una fracción prescrita del periodo de bit $T = 1/B_0$ (Fig. 24.2-11, p. 1094,
presupuesto de anchura temporal). Reglas ad hoc: $\sigma_{\rm sys}\le 70\%$ de $T$ para NRZ y 35 % para
RZ. El libro adopta, solo para comparar fibras, que la fibra aporte como máximo el 25 % del bit:
$$\sigma_\tau = \tfrac14 T = \frac{1}{4B_0}. \tag{24.2-9}$$

Casos (p. 1094–1096; Fig. 24.2-12, p. 1095):
- *MMF* escalonada: de (24.1-2) y (24.2-9) (recuadro, "Step-Index MMF"):
  $$LB_0 = \frac{c_1}{2\Delta}. \tag{24.2-10}$$
  Para GRIN parabólica óptima, $LB_0$ mayor por $2/\Delta$. Con $n_1 = 1.46$, $\Delta = 0.01$:
  $LB_0\approx10$ km-Mb/s (escalonada) y ≈ 2 km-Gb/s (GRIN).
- *SMF* con solo dispersión del material, de (24.1-3) (recuadro, "SMF"):
  $$LB_0 = \frac{1}{4|D_\lambda|\sigma_\lambda}. \tag{24.2-11}$$
  Cerca de 1300 nm, $|D_\lambda|$ puede ser 1 ps/km-nm; con $\sigma_\lambda = 1$ nm → $LB_0\approx250$ km-Gb/s.
  A 1550 nm, $D_\lambda = 17$ ps/km-nm → $LB_0\approx15$ km-Gb/s.
- *SMF con pulsos limitados por transformada* (p. 1094–1096): con láseres monofrecuencia y
  moduladores externos $\sigma_\lambda\ll1$ nm, pero un ancho espectral muy estrecho es incompatible con
  un pulso muy corto (Fourier). Los pulsos gaussianos tienen el mínimo producto tiempo-ancho de
  banda y sufren la mínima dispersión. Un gaussiano limitado por transformada de ancho $\tau_0$,
  envolvente $\exp(-t^2/\tau_0^2)$, tiene espectro de intensidad gaussiano de FWHM $\sigma_\nu = 0.375/\tau_0$
  (§22.1B), es decir $\sigma_\lambda = |\partial\lambda/\partial\nu|\sigma_\nu = (\lambda_o^2/c_o)\sigma_\nu = 0.375\lambda_o^2/c_o\tau_0$.
  Si el pulso ocupa medio bit, $\tau_0 = T/2 = 1/2B_0$:
  $$\sigma_\lambda = 0.75\frac{\lambda_o^2}{c_o}B_0, \tag{24.2-12}$$
  proporcional a $B_0$ (ej.: 1550 nm, 10 Gb/s → $\sigma_\lambda = 0.06$ nm). Por §22.3B, el gaussiano se
  ensancha √2 a la distancia característica $z_0 = \pi\tau_0^2/D_\nu$; allí un pulso $\tau_0 = T/2$
  crece $(\sqrt2-1)T/2\approx0.21T$. Tomando $L = z_0$, con $\tau_0 = 1/2B_0$ y $D_\nu = D_\lambda\lambda_o^2/c_o$
  (recuadro, "SMF, Transform-Limited Pulse"):
  $$LB_0^2 = \frac\pi4\frac{c_o}{|D_\lambda|\lambda_o^2}. \tag{24.2-13}$$
  Ahora $L\propto1/B_0^2$ y $B_0L\propto1/B_0$. Ej.: 1550 nm, $D_\lambda = 17$ ps/km-nm: $L = 64$ km a 10 Gb/s
  pero 4 km a 40 Gb/s. Extiende mucho el límite por dispersión, aunque cae más rápido con la tasa.
- *SMF compensada en dispersión (DSF) con pulsos limitados por transformada* (p. 1096): la única
  mejora restante es reducir $D$; bajar de 17 a 4 ps/km-nm (NZ-DSF) sube $L$ de 64 a 272 km a 10 Gb/s.
  Las DSF tienen atenuación algo mayor.

Pie de la Fig. 24.2-12 (p. 1095) — seis rectas (de izquierda a derecha): (a) MMF escalonada
($n_1 = 1.46$, $\Delta = 0.01$), $LB_0 = 10$ km-Mb/s; (b) MMF GRIN parabólica, 2 km-Gb/s; (c) SMF por
dispersión del material a 1550 nm con $D_\lambda = 17$ ps/km-nm y $\sigma_\lambda = 1$ nm, 15 km-Gb/s;
(d) SMF a 1300 nm con $|D_\lambda| = 1$, $\sigma_\lambda = 1$ nm, 250 km-Gb/s; (e) SMF con pulsos limitados por
transformada a 1550 nm, $|D_\lambda| = 17$; (f) igual que (e) con NZ-DSF, $D_\lambda = 4$ ps/km-nm.

**Combined Attenuation- and Dispersion-Limited Performance** (p. 1096–1097; Fig. 24.2-13):
se superponen las Figs. 24.2-10 y 24.2-12 y se toma la menor $L$. Conclusiones:
- A bajas tasas el enlace está limitado por atenuación ($L$ cae logarítmicamente con $B_0$); a altas
  tasas, por dispersión ($L\propto1/B_0$ con fuente de ancho de línea dado, $L\propto1/B_0^2$ con pulsos
  limitados por transformada).
- Para alta tasa y larga distancia la SMF es esencial. 1300 vs 1550 nm no es obvio para fibra
  convencional (dispersión mínima en 1300, atenuación mínima en 1550): las curvas $L$–$B_0$ se cruzan.
- Con DSF se reduce la dispersión en 1550 nm y ese régimen resulta generalmente superior.

**Performance of Analog Communication System** (p. 1097–1098). Igual que en digital, limitado por
atenuación (señal bajo el ruido) y dispersión (ancho de banda $\sigma_f = 1/2\pi\sigma_\tau$ limitado:
atenúa las altas frecuencias). Potencia recibida cae exponencialmente con $L$; el ancho de banda
$\propto1/L$. **Los efectos no lineales no juegan papel en sistemas analógicos** (potencia distribuida,
no concentrada en pulsos estrechos). Condiciones: potencia recibida > $\mathsf P_r$; ancho de banda
$\sigma_f$ > ancho espectral $B$ de la señal. Para receptor ideal, SNR $=\bar n = (P/h\nu)/2B$ con $\bar n$
el número medio de fotones en el tiempo de resolución $1/2B$; con SNR mínimo SNR$_0$, la sensibilidad es
$\bar n_0 = \mathrm{SNR}_0$ fotones por tiempo de resolución y
$$P_r = h\nu\,\bar n_0(2B). \tag{24.2-14}$$
Idéntica a (24.2-1) si $1/2B \leftrightarrow 1/B_0$: las relaciones $L$–$B_0$ digitales se aplican al
analógico con $B_0\to2B$, si SNR$_0 = 10$ es aceptable (ej.: un enlace de 1 km a 2 Gb/s con BER $10^{-9}$
sirve para analógico de 1 GHz con SNR ≥ 10). Pero el analógico suele requerir SNR mucho mayor
(audio/video de calidad: 60 dB → SNR$_0 = 10^6$ → $\bar n_0 = 10^6$ fotones por tiempo de resolución).
Además, la no linealidad de fuente y detector limita el rango dinámico (p. 1098).

#### 24.2D Attenuation and Dispersion Compensation and Management (p. 1098)

**Attenuation Compensation** (p. 1098; Fig. 24.2-14): amplificadores de fibra a intervalos elevan la
potencia (diente de sierra de potencia vs. $z$). Límite último: el ruido que introducen los
amplificadores (a diferencia del repetidor, no regeneran la señal digital). Antes de ese límite la
dispersión suele dominar → la compensación de dispersión es indispensable en enlaces largos con OA.

**Dispersion Compensation** (p. 1098–1099). El ensanchamiento de una fibra $(L, D_\lambda)$ se revierte
con una fibra compensadora $(L', D'_\lambda)$ de signo opuesto tal que
$$D'_\lambda L' = -D_\lambda L. \tag{24.2-15}$$
(Fig. 24.2-15, p. 1099: dispersión acumulada y anchura de pulso en diente de sierra, con tramos
cortos de $D'_\lambda<0$.) La fibra compensadora suele ser corta → $|D'_\lambda|$ grande. Como la fibra
convencional tiene $D>0$ sobre 1310 nm, la compensadora debe tener $D<0$ en esa banda (DSF).
Interpretación con el cap. 22: la propagación dispersiva equivale a un **filtro de chirp cuadrático**
(fase ∝ frecuencia²) con coeficiente $b = D_\lambda L$; se cancela con un filtro inverso $b' = -b$. Puede
hacerse también con redes de Bragg o interferómetros (§22.2). Ubicación: en el transmisor
(precompensación), en el receptor (postcompensación) o, más común, distribuida periódicamente. En
régimen lineal la ubicación no importa; **para evitar efectos no lineales se colocan de modo que
no haya pulsos cortos durante tramos largos** (p. 1099).

**Broadband Dispersion Compensation: Dispersion Management** (p. 1099–1100). En WDM, (24.2-15)
debe cumplirse en toda la banda: el error $e_\lambda = D'_\lambda L' - D_\lambda L$ debe anularse en todas las λ.
Fig. 24.2-16 (p. 1099): compensación perfecta en $\lambda_1$ (centro), dispersión neta positiva en
$\lambda_2$ y negativa en $\lambda_3$; $e_\lambda$ se anula en toda la banda si las pendientes de $D_\lambda$ y
$D'_\lambda$ son iguales. Si ambas son ≈ lineales en λ con la misma pendiente y $e_\lambda = 0$ en $\lambda_1$,
entonces $e_\lambda\approx0$ en todas partes. Diseñar el filtro compensador con el valor y la **pendiente**
adecuados de $D$ = **gestión de dispersión** (p. 1100).

#### 24.2E Soliton Optical Communications (p. 1100)

La compensación última ocurre naturalmente en los **solitones**: pulsos no dispersivos cuya
intensidad es suficiente para que la no linealidad juegue un papel principal; la dispersión no
lineal (velocidad de fase dependiente de la intensidad por Kerr) compensa exactamente la dispersión
cromática lineal (§22.5B). Un amplificador de fibra compensa la atenuación para que el pulso mantenga
su intensidad pico y siga siendo solitón. Condición de formación, de (22.5-13), para ancho $\tau_0$,
intensidad pico $I_0$ y longitud de onda $\lambda_o$ (recuadro, "Soliton Condition"):
$$\frac{2\pi}{\lambda_o}n_2 I_0 = -\frac{\beta''}{\tau_0^2}, \tag{24.2-16}$$
con $n_2$ el coeficiente Kerr y $-\beta'' = (\lambda_o^2/2\pi c_o)D_\lambda$ proporcional a $D_\lambda$ (se necesita
$D_\lambda>0$, dispersión anómala). Perfil $I(t) = I_0\,\mathrm{sech}^2(t/\tau_0)$, FWHM $= 1.76\,\tau_0$.
En digital: solitón de ancho $\tau_0\ll T$ = "1", ausencia = "0": formato necesariamente **RZ**.

Los sistemas de solitones no están limitados ni por atenuación ni por dispersión, sino por la
**ISI no lineal** entre colas de solitones vecinos: dos solitones idénticos separados $T$ se atraen,
colapsan en un solo pulso y vuelven a separarse, periódicamente con periodo [ver (22.5-32)]
$$L_p = \pi e^{r/2}z_0, \tag{24.2-17}$$
con $r = T/\tau_0$ la relación separación/anchura y $2z_0 = -\tau_0^2/\beta'' = 2\pi c_o\tau_0^2/\lambda_o^2D_\lambda$ la
distancia de dispersión. $L_p$ crece exponencialmente con $r$; si $r\gg1$, $L_p\gg z_0$. Con $L\ll L_p$ la
interacción es mínima. Con $B_0 = 1/T$, la condición $L\ll L_p$ se escribe
$$LB_0^2 \ll \frac{\pi^2c_o}{\lambda_o^2D_\lambda}\frac{e^{r/2}}{r^2}, \tag{24.2-18}$$
que limita distancias y tasas últimas (p. 1100).

**EJEMPLO 24.2-1 — Soliton Communication System** (p. 1100–1101). 10 Gb/s por SMF-DSF a
$\lambda_o = 1550$ nm con solitones de 10 ps (FWHM); $D_\lambda = 1$ ps/nm-km, $n_2 = 2.6\times10^{-20}$ m²/W,
$A_{\rm eff} = 60$ µm². Resultado: $\tau_0 = 10/1.76 = 5.7$ ps; de (24.2-16), $I_0 = 3.75\times10^8$ W/m² ↔
potencia pico $I_0A_{\rm eff} = 22.5$ mW (que debe entregar la fuente); distancia de dispersión
$2z_0 = (2\pi c_o/\lambda_o^2)\tau_0^2/D_\lambda\approx25$ km; bit $T = 100$ ps, $r = T/\tau_0 = 17.6$, periodo de
interacción $L_p\approx2.1\times10^4z_0$; la fibra debe ser mucho más corta; (24.2-18) da
$LB_0^2\ll26$ (Tb/s)² km.

---

### 24.3 Modulation and Multiplexing (p. 1101)

#### 24.3A Modulation (p. 1101)

Dos tipos: **modulación de campo** y **modulación de intensidad**.

**Field modulation** (p. 1101). El campo de una onda monocromática es una portadora sinusoidal de
frecuencia altísima (200 THz a 1500 nm); se modula amplitud (AM), fase (PM) o frecuencia (FM)
(Fig. 24.3-1). Banda espectral enorme disponible, pero difícil de implementar: requiere fuente
estable en amplitud, frecuencia y fase (láser muy coherente); la modulación directa de fase/frecuencia
es difícil (modulador externo electroóptico); fibra multimodo da gran ruido modal → SMF necesaria;
hay que monitorear/controlar la polarización salvo fibra PM; el receptor debe medir magnitud y fase
del campo → detección heterodina. Por la coherencia requerida se llaman **sistemas de comunicación
coherente** (§24.5) (p. 1101–1102).

**Intensity modulation** (p. 1102; Fig. 24.3-2). La intensidad (potencia) es proporcional a la señal o
a una versión codificada. Es la mayoría de sistemas comerciales: se modula la corriente de un LED o
LD; fibra SMF o MMF; **receptor de detección directa** (solo potencia; las oscilaciones del campo no
juegan papel). La λ puede identificar señales en el mismo enlace → WDM.

**Modulation format** (p. 1102). Elegida la variable, se usa cualquier formato (analógico, de pulsos,
digital). **PCM**: se muestrea la señal, se cuantiza en niveles discretos y se codifica en binario.
Fig. 24.3-3: voz de 4 kHz muestreada a $8\times10^3$ muestras/s (cada 125 µs), 256 niveles = 8 bits
(15.625 µs por bit) → 64 kb/s. En intensidad, cada bit = presencia/ausencia de pulso: **ON–OFF keying
(OOK)**; en frecuencia o fase: **FSK** y **PSK** (Fig. 24.3-4, p. 1103: OOK NRZ y RZ; FSK; PSK). También
puede modularse la intensidad con una subportadora armónica modulada a su vez en AM/FM/PM/FSK/PSK.

#### 24.3B Multiplexing (p. 1103)

Transmitir y recuperar más de una señal por el mismo enlace marcándolas con una etiqueta física o
código (Fig. 24.3-5: MUX/DMUX). Tres sistemas: **FDM**, **TDM**, **CDM**.
- **FDM**: portadoras de distintas frecuencias moduladas por distintas señales; en recepción, filtros
  sintonizados [Fig. 24.3-6(a)].
- **TDM**: tramas temporales con ranuras asignadas a bits/bytes de las distintas señales, sincronizadas
  a un mismo reloj [Fig. 24.3-6(b)]. Ejemplo jerárquico: **sistema T** (Fig. 24.3-7, p. 1104): 24 señales
  de 4 kb/s → T1 1.544 Mb/s; ×4 → T2 6.312 Mb/s; ×6 → T3 44.736 Mb/s; ×7 → T4 274.176 Mb/s.
- **CDM** (p. 1104; Fig. 24.3-8): a cada señal un código (función de tiempo única dentro del bit, p.
  ej. secuencia binaria a tasa mucho mayor); códigos ortogonales separables con un correlador; cada
  "1" se reemplaza por la secuencia-código.

Multiplexación **electrónica** (FDM o TDM eléctrico generan una señal compuesta que modula la fuente;
p. ej. subportadoras FDM en IM, o la señal T4 en IM, demultiplexación electrónica tras detectar) u
**óptica** (etiquetas ópticas: en FDM óptico distintas frecuencias ópticas separadas con filtros
ópticos). Cuando las portadoras del FDM óptico están muy separadas (> 20 GHz) se habla de **WDM**;
populares porque amplían la capacidad de una red existente sin tender más fibra (p. 1104).

#### 24.3C Wavelength-Division Multiplexing (WDM) (p. 1104)

Fuentes de distintas λ, cada una modulada en intensidad por una señal eléctrica, mezcladas con un
**multiplexor óptico (OMUX)**; en recepción un **ODMUX** separa las λ hacia detectores distintos
(§23.2A). Cada canal suele llevar a su vez un conjunto multiplexado electrónicamente (Fig. 24.3-9,
p. 1105). Fig. 24.3-10 (p. 1105): bandas O/E/S/C/L/U sobre la curva de atenuación; ejemplo de 40
canales WDM en la banda C con separación de 100 GHz. La separación entre canales debe ser mucho mayor
que el ancho espectral de la luz modulada (ancho de línea de la fuente + ancho de los datos) y
suficiente para (de)multiplexar con mínimo crosstalk.
- **CWDM** (coarse): pocos canales muy separados (≥ 20 nm). Ejemplos: 1310 + 1550 nm (TV por cable,
  downstream/upstream); Ethernet LX-4: cuatro λ cerca de 1310 nm con 3.125 Gb/s cada una; redes
  metropolitanas con 20 nm de separación (p. 1105–1106).
- **DWDM** (dense): muchos canales (> 8) muy juntos. A 1550 nm (banda C), $\Delta\nu = 200$ GHz ↔
  $\Delta\lambda = (\lambda_o^2/c_o)\Delta\nu = 1.6$ nm; separaciones de 100 GHz (0.8 nm), 50 GHz (0.4 nm) e incluso
  25 GHz (0.2 nm). La banda C tiene 35 nm ≈ 4.4 THz: 40 canales a 100 GHz. Se usa en la jerarquía
  alta (backbone de Internet); láseres mucho más estables y control térmico de precisión (p. 1106).

---

### 24.4 Fiber-Optic Networks (p. 1106)

Red = conjunto de enlaces que conectan múltiples usuarios (terminales) en un área; mensajes por uno o
varios enlaces según rutas controladas por routers y switches. LAN (edificio, campus), redes mayores
(telefónica, Telex, Internet). Las redes de fibra usan enlaces de fibra con routers/switches
electrónicos u ópticos (cap. 23).

#### 24.4A Network Topologies and Multiple Access (p. 1106)

Red de $N$ nodos con enlaces dedicados: $N(N-1)$ enlaces dúplex y $2N(N-1)$ transmisores y receptores.
Topologías con menos enlaces (Fig. 24.4-1, p. 1106): **estrella** (acoplador en estrella central
reparte la potencia de cada nodo por igual entre los demás), **anillo** y **bus** (la fibra pasa por
los nodos, que extraen/añaden datos; los receptores necesitan gran rango dinámico), **malla** (más
general). Solo $N$ transmisores y $N$ receptores. Fig. 24.4-2 (p. 1107): red de anillos backbone y
anillos de acceso conectados por cross-connects digitales (XC) en oficinas centrales.

**Interface** (p. 1107; Fig. 24.4-3): la interfaz nodo-red tiene receptor, transmisor y un
**add-drop multiplexer (ADM)** electrónico. Interfaz **opaca** (a): O/E, el ADM extrae/añade datos y
E/O regenera (la luz se detecta y regenera). Interfaz **transparente** (b): acoplada ópticamente con
un acoplador direccional (§23.1, 23.3). (c) Interfaz a fibra bidireccional (dúplex) con dos
acopladores direccionales.

**Multiple Access** (p. 1108): los nodos comparten el medio. **TDMA** (ranuras entrelazadas; buffers;
tiempos de guarda porque no se puede sincronizar todos los nodos), **FDMA** (bandas preasignadas, sin
sincronizar relojes; en óptica **WDMA**, contraparte de WDM), **CDMA** (cada nodo con código-dirección
único; cada nodo correlaciona su código con la señal entrante; paquetes con dirección de destino,
§23.3F).

**SONET** (p. 1108) [y su versión internacional **SDH**]: estándar TDM para fibra que resuelve el
multiplexado de señales con relojes ligeramente distintos embebiéndolas en tramas más largas (la carga
"flota" dentro de la trama, las tramas son síncronas). Unidad básica STS-1 / **OC-1** a 51.84 Mb/s;
$N$ de ellas forman **OC-N**.

**Tabla 24.4-1** (p. 1108) — tasas (Mb/s) de la jerarquía STS en SONET:

| OC-1 | OC-3 | OC-12 | OC-24 | OC-48 | OC-192 | OC-768 |
|---|---|---|---|---|---|---|
| 51.84 | 155.52 | 622.08 | 1 244.16 | 2 488.32 | 9 995.33 | 39 813.12 |

**EJEMPLO 24.4-1 — Ring Network** (p. 1109; Fig. 24.4-4). Anillo de 4 nodos; cada nodo transmite a
los otros tres a OC-12 (≈ 622 Mb/s) u OC-24 (≈ 1.24 Gb/s). El segmento 1–2 lleva el tráfico más
pesado: OC-12+OC-12+OC-24 = OC-48 (≈ 2.5 Gb/s); los segmentos 2–3 y 3–4 llevan OC-24.

#### 24.4B Wavelength-Division Multiplexing (WDM) Networks (p. 1109)

Red WDM: CWDM o DWDM en los enlaces y WDMA como acceso al medio; cualquier topología; cada nodo
transmite y recibe en uno o varios canales de λ. Añade una dimensión y flexibilidad, con complejidad.

**Broadcast-and-Select WDM Network** (p. 1109–1110). Cada nodo transmite en una λ fija única y
*difunde* a todos vía acopladores pasivos; cada receptor *selecciona* la λ que le interesa con un
filtro sintonizable. Fig. 24.4-5: 5 nodos en $\lambda_1\ldots\lambda_5$ con acoplador en estrella; estado
mostrado: nodo 1 sintonizado a $\lambda_5$, nodos 2, 3, 4 a $\lambda_1$, nodo 5 a $\lambda_2$ → nodo 2 transmite a 5,
nodo 5 a 1, nodo 1 multidifunde a 2, 3, 4. Fig. 24.4-6 (p. 1110): si cada receptor sintoniza la λ de
su vecino, la estrella física equivale a un **anillo lógico**. Se requiere coordinación dinámica para
evitar conflictos y colisiones.

**Multi-Hop Broadcast-and-Select** (p. 1110; Fig. 24.4-7). Para no exigir que cada nodo detecte
cualquier λ, se asignan a cada nodo dos λ de transmisión y dos de recepción; cualquier par se comunica
en uno o dos saltos (p. ej. 1→3 en $\lambda_1$, 3→2 en $\lambda_6$). Limitación de broadcast-and-select
(single- o multi-hop): la potencia de cada nodo debe llegar a todos (ineficiente con muchos nodos) y
el número de canales ≥ número de nodos (prohibitivo para redes grandes).

**Wavelength-Routed Networks** (p. 1111). Un par de nodos usa un canal de λ en una ruta; otro par puede
reusar la misma λ si sus rutas no comparten enlace. Fig. 24.4-8: anillo de 5 nodos y 3 canales (1↔2 y
2↔3 en $\lambda_1$; 1↔3 en $\lambda_2$ porque pasa por 2; 4↔1 en $\lambda_3$ porque su ruta usa enlaces con $\lambda_1$ y
$\lambda_2$). Cada enlace lleva una o más λ (no todas); el enlace 4–5 lleva tres. Componente clave: el
**optical add-drop multiplexer (OADM)** (§23.2A) = ODMUX + ADM + OMUX [Fig. 24.4-8(c)]: extrae (drop)
ciertos canales, añade otros y deja pasar el resto sin cambio. Redes ágiles usan **ROADM**
(reconfigurables). En topologías no-anillo, nodos con varias fibras entrantes/salientes usan un
**optical cross-connect (OXC)** (Fig. 24.4-9, p. 1112: dos fibras de entrada y dos de salida, cuatro
canales; switch + ADM; §23.3D) y un nodo hub con servidor que procesa todos los canales.

**EJEMPLO 24.4-2 — WDM Upgrade of a Ring Network** (p. 1112; Fig. 24.4-10). Anillo de 4 nodos con 3
canales $\lambda_1,\lambda_2,\lambda_3$, mejora del anillo del Ejemplo 24.4-1. Nodos 1 y 3 acceden a $\lambda_1,\lambda_2$;
nodo 4 a $\lambda_1,\lambda_3$; nodo 2 a las tres. Los nodos se comunican al doble de tasa que antes sin que
ningún canal supere la tasa original: el segmento 1–2 lleva OC-96 combinado (≈ 5 Gb/s), pero la tasa
máxima por λ es OC-48 (≈ 2.5 Gb/s).

---

### 24.5 Coherent Optical Communications (p. 1112)

Usan modulación de campo (amplitud, fase o frecuencia), fuentes coherentes, SMF y receptores
heterodinos.

**Heterodyne and Homodyne Receivers** (p. 1112–1114). Los fotodetectores responden al flujo de fotones
y son insensibles a la fase; pero se puede medir la amplitud compleja mezclando la señal con un campo
de referencia coherente estable, el **oscilador local (LO)**, y detectando la superposición
(Fig. 24.5-1, p. 1113, con divisor de haz o acoplador). Nombres: **heterodinaje óptico**, mezcla
óptica, fotomezcla, batido de luz (§2.6B), **detección coherente** (frente a **detección directa**).
Si $\nu_s\ne\nu_L$: heterodino; si $\nu_s = \nu_L$: **homodino**.

Sea $\mathcal E_s = \mathrm{Re}\{A_s\exp(j2\pi\nu_st)\}$ el campo de la señal con $A_s = |A_s|\exp(j\varphi_s)$;
$|A_s|$ o $\varphi_s$ se modulan lentamente. Análogo para el LO: $\mathcal E_L, A_L, \nu_L, \varphi_L$. Para ondas
planas paralelas con la misma polarización, $\mathcal E = \mathcal E_s + \mathcal E_L$ y
$$|A_s\exp(j2\pi\nu_st) + A_L\exp(j2\pi\nu_Lt)|^2 = |A_s|^2 + |A_L|^2 + 2|A_s||A_L|\cos[2\pi(\nu_s-\nu_L)t + (\varphi_s-\varphi_L)]. \tag{24.5-1}$$
En intensidades:
$$I = I_s + I_L + 2\sqrt{I_sI_L}\cos[2\pi\nu_It + (\varphi_s-\varphi_L)], \tag{24.5-2}$$
con $\nu_I = \nu_s - \nu_L$ la **frecuencia intermedia** (de diferencia). En potencias sobre el detector:
$$P = P_s + P_L + 2\sqrt{P_sP_L}\cos[2\pi\nu_It + (\varphi_s-\varphi_L)]. \tag{24.5-3}$$
$\nu_I$ puede ser muchos órdenes menor que las frecuencias ópticas. Un desalineamiento angular lava el
término de interferencia (la fase varía con la posición en el detector); se evita si $\theta\ll\lambda/a$ con
$a$ el tamaño de la apertura (Fig. 2.5-4) (p. 1113–1114).

Fotocorriente: $\bar i = \eta e\Phi = (\eta e/h\bar\nu)P$ con $\bar\nu = \tfrac12(\nu_s+\nu_L)$ (luz cuasi-monocromática,
$\nu_I\ll\nu_s,\nu_L$):
$$\bar i = \bar i_s + \bar i_L + 2\sqrt{\bar i_s\bar i_L}\cos[2\pi\nu_It + (\varphi_s-\varphi_L)], \tag{24.5-4}$$
con $\bar i_s = \eta eP_s/h\bar\nu$, $\bar i_L = \eta eP_L/h\bar\nu$. Como el LO es mucho más fuerte que la señal
(recuadro, "Photomixing Current"):
$$\bar i \approx \bar i_L + 2\sqrt{\bar i_s\bar i_L}\cos[2\pi\nu_It + (\varphi_s-\varphi_L)]. \tag{24.5-5}$$
El segundo término (a $\nu_I$) lleva la información: conocidos $\bar i_L$ y $\varphi_L$ se estiman $\bar i_s$ y
$\varphi_s$ (intensidad y fase → amplitud compleja). Como $\bar i_s$, $\varphi_s$ varían lentamente frente a $\nu_I$,
son modulaciones lentas de $2\sqrt{\bar i_L}\cos(2\pi\nu_It-\varphi_L)$, demodulables con técnicas AM/FM de
radio (Fig. 24.5-2, p. 1114). Desde la óptica de fotones: detección de fotones policromáticos (de dos
frecuencias) (Prob. 12.1-11). **Homodino**: $\nu_I = 0$; un lazo de enganche de fase fija $\varphi_L = 0$ y
$$\bar i = \bar i_L + 2\sqrt{\bar i_s\bar i_L}\cos\varphi_s. \tag{24.5-6}$$
La modulación de amplitud y de fase se logra variando $\bar i_s$ y $\varphi_s$.

**Advantages of Heterodyne/Homodyne Receivers** (p. 1115): mide fase y frecuencia ópticas; permite WDM
con separación de canales mucho menor (≈ 100 MHz frente a ≈ 100 GHz en detección directa); permite
ecualización electrónica del ensanchamiento por dispersión (el desfase entre componentes de λ puede
removerse por filtrado electrónico porque se monitorea la fase); con LO fuerte hay conversión con
ganancia sin ruido que levanta la señal sobre el ruido de circuito; ventaja de 3 dB en SNR incluso
sobre el receptor directo sin ruido; insensible a luz de fondo que no se mezcla con el LO (detección
limitada por ruido fotónico en el IR). Costo: complejidad (LO estable, acoplador con campos alineados,
circuitos de enganche de fase).

**Coherent Systems** (p. 1115–1116). Condición esencial: LO y señal en fase, paralelos y con la misma
polarización. Láseres monofrecuencia con mínimas fluctuaciones; LO enganchado en fase al campo
recibido (PLL adaptativo); fibra monomodo (sin ruido modal) y mantenedora de polarización, o
compensación adaptativa de polarización en el receptor. Fig. 24.5-3 (p. 1116): láser DFB + modulador
de fase → SMF → controlador de polarización → acoplador con DFB sintonizable (LO, con lazo de
frecuencia) → **mezclador balanceado** (dos fotodetectores) → amplificador → detector de fase. Las dos
salidas del acoplador contienen suma y diferencia de los campos; por (24.5-4) las corrientes
$$\bar i_\pm = \bar i_s + \bar i_L \pm 2\sqrt{\bar i_s\bar i_L}\cos[2\pi\nu_It + (\varphi_s-\varphi_L)] \tag{24.5-7}$$
se restan electrónicamente dando $4\sqrt{\bar i_s\bar i_L}\cos[2\pi\nu_It+(\varphi_s-\varphi_L)]$, que se demodula;
ventaja: cancela las fluctuaciones de intensidad del LO. Ejemplo experimental (p. 1115): sistema a
≈ 4 Gb/s en 1550 nm, DFB de 15 MHz de ancho de línea modulado directamente en FSK, LO = DBR sintonizable
(§17.3C), sensibilidad ≈ 190 fotones/bit, 160 km de fibra.

#### *Performance of Analog Coherent Communication Systems (p. 1116)

La detección heterodina es necesaria para medir fase, pero también es útil para medir intensidad
porque da ganancia por el LO fuerte: alternativa a la amplificación óptica (cap. 14, §17.2) y a la
ganancia del APD (§18.4). Ruido de la fotocorriente media $\bar i$:
$$\sigma_i^2 = 2e\bar iB + \sigma_r^2, \tag{24.5-8}$$
($B$ ancho de banda del receptor; primer término ruido fotónico, segundo ruido de circuito, §18.6).
Con LO intenso, $\bar i_L\gg\bar i_s$ y $2e\bar i_LB\gg\sigma_r^2$:
$$\bar i\approx\bar i_L + 2\sqrt{\bar i_s\bar i_L}\cos[2\pi\nu_It+(\varphi_s-\varphi_L)], \tag{24.5-9a}$$
$$\sigma_i^2\approx2e\bar i_LB. \tag{24.5-9b}$$
Para AM, la señal es el RMS de la sinusoide: potencia eléctrica $\tfrac12[2\sqrt{\bar i_s\bar i_L}]^2 = 2\bar i_s\bar i_L$;
ruido $2e\bar i_LB$:
$$\mathrm{SNR} = \frac{2\bar i_s\bar i_L}{2e\bar i_LB} = \frac{\bar i_s}{eB}. \tag{24.5-10}$$
Con $\bar m = \bar i/2Be$ el número medio de fotoelectrones en el tiempo de resolución $T = 1/2B$ (recuadro,
"Signal-to-Noise Ratio, Heterodyne Receiver"):
$$\mathrm{SNR} = 2\bar m. \tag{24.5-11}$$
Comparación con detección directa de la misma $\bar i_s$ (p. 1117):
$$\mathrm{SNR} = \frac{\bar i_s^2}{2e\bar i_sB+\sigma_r^2} = \frac{\bar m^2}{\bar m+\sigma_q^2}, \tag{24.5-12}$$
con $\sigma_q^2 = (\sigma_r/2Be)^2$ el parámetro de ruido de circuito (§18.6C). Para luz intensa o bajo ruido de
circuito ($\bar m\gg\sigma_q^2$), directa da SNR $=\bar m$; heterodina da $2\bar m$: **ventaja de 3 dB**. Para luz
débil la ventaja es mayor (directa se reduce a $\bar m/(1+\sigma_q^2/\bar m)$). El APD en detección directa,
con ganancia suficiente para vencer el ruido de circuito, da por (18.6-36)
$$\mathrm{SNR} = \frac{\bar m}{F}, \tag{24.5-13}$$
con $F>1$ el factor de exceso de ruido: incluso un APD sin ruido ($F = 1$) es un factor 2 peor que el
heterodino.

#### *Performance of Digital Coherent Communication Systems (p. 1117)

**OOK homodino** (p. 1117). Tasa $B_0$; bits "1"/"0" = presencia/ausencia de $\bar i_s$ en el bit
$T = 1/B_0$; $\varphi_s = \varphi_L = 0$, $\nu_I = 0$. De (24.5-9):
$$\text{media }\mu_1\approx\bar i_L + 2\sqrt{\bar i_L\bar i_s},\ \text{varianza }\sigma_1^2\approx2\bar i_LeB\ (\text{bit "1"});\qquad
\mu_0\approx\bar i_L,\ \sigma_0^2\approx2\bar i_LeB\ (\text{bit "0"}). \tag{24.5-14}$$
Ancho de banda $B = B_0/2$ (el bit $T = 1/B_0$ es el tiempo de muestreo $1/2B$). Con la aproximación
gaussiana (§18.6, (18.6-55)):
$$Q = \frac{\mu_1-\mu_0}{\sigma_1+\sigma_0} = \sqrt{\frac{\bar i_s}{2eB}} = \sqrt{\bar m}, \tag{24.5-15}$$
con $\bar m = \bar i_s/2eB$ fotoelectrones detectados en el bit "1". Para BER $=10^{-9}$, $Q\approx6$ → $\bar m = 36$ →
sensibilidad $\bar m_a = \tfrac12\bar m = 18$ fotoelectrones/bit (promedio sobre ambos bits).

**PSK homodino** (p. 1118). "1"/"0" = $\varphi_s = 0$ / $\pi$, con $\varphi_L = 0$: medias
$\mu_1 = \bar i_L + 2\sqrt{\bar i_L\bar i_s}$, $\mu_0 = \bar i_L - 2\sqrt{\bar i_L\bar i_s}$, varianzas $2e\bar i_LB$ ambas:
$$Q = \frac{\mu_1-\mu_0}{\sigma_1+\sigma_0} = 2\sqrt{\frac{\bar i_s}{2eB}} = 2\sqrt{\bar m}. \tag{24.5-16}$$
Para BER $=10^{-9}$, $Q = 6$ → $\bar m = 9$; como *ambos* bits llevan 9 fotoelectrones, $\bar m_a = \bar m = 9$
fotoelectrones/bit: el PSK homodino es dos veces más sensible que el OOK homodino.

**Tabla 24.5-1** (p. 1118) — sensibilidad de receptores (fotones por bit) en condiciones ideales,
$\eta = 1$:

| Formato | Detección directa | Homodino | Heterodino |
|---|---|---|---|
| OOK | 10 | 18 | 36 |
| PSK | — | 9 | 18 |
| FSK | — | — | 36 |

**Comparison** (p. 1118): aunque parece que la detección directa OOK (10) iguala al mejor coherente
(PSK homodino, 9), en la práctica no: en homodino se vence el ruido de circuito, mientras en directa
no puede ignorarse salvo con APD, cuyo ruido de ganancia eleva la sensibilidad de 10 a al menos $10F$.
Solo un APD perfecto ($F = 1$) igualaría a la detección coherente.

---

### Reading List (p. 1118–1120)

Libros sobre comunicaciones por fibra (ver también listas de caps. 8, 9, 17, 18, 22 y 23). Destacan
para el curso: G. P. Agrawal, *Nonlinear Fiber Optics*, Academic Press, 4.ª ed. 2006;
S. Ramachandran, *Fiber-Based Dispersion Compensation*, Springer 2006; J. N. Damask, *Polarization
Optics in Telecommunications*, Springer 2005; K.-P. Ho, *Phase-Modulated Optical Communication
Systems*, Springer 2005; T. Schneider, *Nonlinear Optics in Telecommunications*, Springer 2004;
A. Galtarossa y C. R. Menyuk (eds.), *Polarization Mode Dispersion*, Springer 2005; G. P. Agrawal,
*Fiber-Optic Communication Systems*, Wiley, 3.ª ed. 2002; Kaminow y Li (eds.), *Optical Fiber
Telecommunications IV A/B*, Academic 2002; R. Ramaswami y K. N. Sivarajan, *Optical Networks: A
Practical Perspective*, Morgan Kaufmann, 2.ª ed. 2002; B. Mukherjee, *Optical WDM Networks*,
Springer 2006; S. E. Miller y I. P. Kaminow (eds.), *Optical Fiber Telecommunications II*, Academic
1988; B. E. A. Saleh, *Photoelectron Statistics…*, Springer 1978. Artículos: números especiales de
*IEEE J. Sel. Top. Quantum Electron.* 12(4) 2006, 10(2) 2004 y 6(6) 2000; S. F. Jacobs, "Optical
Heterodyne (Coherent) Detection", *Am. J. Phys.* 56, 235–245 (1988); M. C. Teich, "Laser
Heterodyning", *Optica Acta* 32, 1015–1021 (1985); Prucnal, Santoro y Fan, *IEEE J. Lightwave
Technol.* LT-4, 547–554 (1986).

---

## Tablas y datos numéricos útiles

**Fibra de sílice** (Fig. 24.1-2, p. 1077; Fig. 24.2-10, p. 1093):
| Magnitud | Valor |
|---|---|
| Atenuación a 870 nm | ≈ 1.5 dB/km (fig. 24.1-2); 2.5 dB/km usado en Fig. 24.2-10 |
| Atenuación a 1300 nm | ≈ 0.3 dB/km (0.35 en Fig. 24.2-10) |
| Atenuación a 1550 nm | ≈ 0.16 dB/km (mínimo absoluto); pico OH⁻ en 1.4 µm |
| $D_\lambda$ a 870 nm | ≈ −80 ps/km-nm |
| Cero de dispersión del material | $\lambda_o\approx1312$ nm |
| $D_\lambda$ fibra convencional a 1550 nm | 17 ps/km-nm (§24.2; el pie de Fig. 24.1-2 dice +80) |
| $D_\lambda$ NZ-DSF a 1550 nm | ≈ 4 ps/km-nm (Fig. 24.2-12); DSF: ≈ 0–1 |
| $D_{\rm PMD}$ | 0.1–1 ps/√km |
| $n_2$ (Kerr, sílice) | $2.6\times10^{-20}$ m²/W (Ej. 24.2-1) |
| $A_{\rm eff}$ (DSF) | 60 µm² (Ej. 24.2-1) |
| $\alpha$ (km⁻¹) ↔ $\alpha$ (dB/km) | $\alpha_{\rm km^{-1}} = 0.23\,\alpha_{\rm dB/km}$ |
| MMF escalonada $n_1 = 1.46$, $\Delta = 0.01$ | 24 ns/km de ensanchamiento; $LB_0\approx10$ km-Mb/s |
| MMF GRIN óptima | ensanchamiento ×$\Delta/2$; $LB_0\approx2$ km-Gb/s |
| Monomodo | $V = 2\pi(a/\lambda_o)\mathrm{NA} < 2.405$ |

**Bandas de telecomunicaciones** (Figs. 24.1-2, 24.3-10; Prob. 24.3-1):
| Banda | λ (nm) | Comentario |
|---|---|---|
| (histórica) | 870 | AlGaAs; primeros sistemas |
| O (original) | 1260–1360 | centrada en 1310; dispersión mínima |
| E (extended) | 1360–1460 | pico OH⁻ |
| S (short) | 1460–1530 | |
| C (conventional) | 1530–1565 | 35 nm ≈ 4.4 THz; atenuación mínima; EDFA; 40 canales a 100 GHz |
| L (long) | 1565–1625 | EDFA optimizados |
| U (ultra-long) | 1625–1675 | |

**Conversiones WDM** (p. 1106): $\Delta\lambda = (\lambda_o^2/c_o)\Delta\nu$; a 1550 nm: 200 GHz ↔ 1.6 nm,
100 GHz ↔ 0.8 nm, 50 GHz ↔ 0.4 nm, 25 GHz ↔ 0.2 nm. CWDM ≥ 20 nm; DWDM > 8 canales.

**Amplificadores** (§24.1C):
| Tipo | Ganancia | Ancho de banda | Notas |
|---|---|---|---|
| EDFA | > 50 dB | ≈ 40 nm ≈ 5.3 THz (C; también L) | bombeo 980 nm; salida > 100 W |
| EDFA C+L | — | 60 nm ≈ 7.5 THz | |
| REFA Er+Tm | — | ≈ 150 nm ≈ 18.8 THz | vidrios fluoruro/telurito |
| Raman | ≈ 20 dB | ≈ 100 nm ≈ 12.5 THz por bombeo | distribuido o concentrado |
| SOA | ≈ 15 dB | ≈ 50 nm ≈ 6.5 THz (QW); ≈ 200 nm (QD) | ruido, polarización |

**Fuentes y detectores**: LED de superficie: ancho de línea > 100 nm, hasta 100 Mb/s (500 Mb/s a
potencia reducida). LD: decenas de W, muchos Gb/s, decenas de MHz de ancho de línea. DFB
(Fig. 24.1-4): $i_t<10$ mA, $\mathfrak R_d\approx0.4$ W/A, hasta 1 W. InGaAs p-i-n: $\eta\approx0.8$,
$\mathfrak R\approx1$ A/W, 10 GHz en 50 Ω, 0.1 nA oscura. InGaAs/InP SAGM APD: $\eta\approx0.8$,
$\mathfrak R\approx10$ A/W, 10 GHz, GBP ≈ 100 GHz, 0.1 nA, $1/k\approx0.5$ para $\bar G = 10$. Si APD: ventaja de
10–15 dB sobre Si p-i-n a 870 nm.

**Receptores**: sensibilidad ideal OOK directa = 10 fotones/bit (BER $10^{-9}$); Tabla 24.5-1 (arriba).
BER aceptable típica $10^{-9}$; $Q\approx6$. Margen de potencia usual 6 dB. Reglas de presupuesto de tiempo:
$\sigma_{\rm sys}\le0.7T$ (NRZ), $\le0.35T$ (RZ); el libro usa $\sigma_\tau = T/4$ para la fibra.

**Sistemas históricos** (§24.2A): $LB_0$ = 1 km-Gb/s (MMF 870, 1970s), 25 km-Gb/s (SMF 1310, OC-12,
40 km), 250 km-Gb/s (SMF 1550, OC-48, 100 km) → 1 km-Tb/s (OC-192), 200 km-Tb/s (TPC-5, 10 Gb/s,
20 000 km), 1200 km-Tb/s (solitones, 10 Gb/s, > 12 000 km), 900 km-Tb/s (TPC-6 WDM, 100 Gb/s, 9000 km);
5–10 Tb/s sobre 10 000 km con gestión de dispersión y FEC. "Ley de Moore óptica": ×10 cada 4 años.

**Tasas SONET** (Tablas 24.2-1 y 24.4-1): OC-1 51.84, OC-3 155.52, OC-12 622.08, OC-24 1244.16,
OC-48 2488.32, OC-192 9995.33, OC-768 39 813.12 Mb/s. Sistema T: T1 1.544, T2 6.312, T3 44.736,
T4 274.176 Mb/s. PCM de voz: 8 kmuestras/s × 8 bits = 64 kb/s.

**Ejemplo 24.2-1 (solitón)**: 10 Gb/s, 1550 nm, FWHM 10 ps → $\tau_0 = 5.7$ ps; $D_\lambda = 1$ ps/nm-km;
$I_0 = 3.75\times10^8$ W/m²; $P_{\rm pico} = 22.5$ mW; $2z_0\approx25$ km; $r = 17.6$; $L_p\approx2.1\times10^4z_0$;
$LB_0^2\ll26$ (Tb/s)² km.

---

## Problemas al final del capítulo (p. 1120–1121)

- **24.1-1 Optical Fiber Systems.** Discutir la validez y condiciones de aplicabilidad de: (a) 1300 nm
  se prefiere a 870 nm en todos los sistemas; (b) 1550 nm se prefiere a 1300 nm en todos; (c) las SMF son
  superiores a las MMF porque tienen menor atenuación; (d) no hay ensanchamiento de pulso en
  $\lambda_o\approx1312$ nm en sílice; (e) se requieren semiconductores compuestos; (f) los APD son más
  ruidosos que los p-i-n y por tanto no son útiles.
- **24.1-2 Components for Optical Fiber Systems.** Elegir fuente, fibra, amplificador y detector (Fig.
  24.2-3) para: (a) cable transoceánico a 2.5 Gb/s con repetidores cada 100 km; (b) cable de 1 m con
  datos analógicos de un sensor a 1 kHz; (c) LAN a 500 Mb/s; (d) enlace de 1 km a 100 Mb/s con
  variaciones de ±50 °C.
- **24.2-1 Performance of a Plastic Fiber Link.** Fibra plástica 0.5 dB/m, LED 1 mW a 870 nm,
  sensibilidad −20 dBm, 3 dB en cada acoplador; longitud máxima (sin dispersión).
- **24.2-2 Maximum Length of Attenuation-Limited System.** 10 Mb/s; LED 100 µW a 870 nm; 3.5 dB/km;
  segmentos de 1 km con conectores de 1 dB; acopladores 2 dB c/u; margen 6 dB; receptores Si p-i-n
  (5000 fotones/bit) y Si APD (125 fotones/bit). Hallar $\mathsf P_r$ (dBm) y $L$ máxima para cada uno.
- **24.2-3 Maximum Data Rate of Attenuation-Limited System.** 50 km a 1550 nm; láser InGaAsP 2 mW;
  0.2 dB/km; pérdidas 8 dB; margen 6 dB; InGaAs APD 1000 fotones/bit a BER $10^{-9}$. Tasa máxima;
  repetir para BER $10^{-11}$.
- **24.2-4 Maximum Length of an Analog Link.** IM analógica, $B = 10$ MHz, SNR 40 dB; LED 870 nm 100 µW
  medios, índice de modulación 0.5; MMF escalonada 2.5 dB/km; APD $\bar G = 100$, $F = 5$, 0.5 A/W; sin
  ruido de circuito (teoría §18.6D). Sensibilidad en potencia y $L$ máxima.
- **24.2-5 Time Budget for Dispersion-Limited System.** 100 km SMF a 1550 nm; LD InGaAsP de 0.2 nm y
  tiempo de respuesta 20 ps; 17 ps/km-nm; APD InGaAs con 0.1 ns. Tasa máxima con $\sigma_\tau\le25\%$ del bit
  y con $\sigma_{\rm sys}\le70\%$; repetir con DSF de 1 ps/km-nm.
- **24.3-1 Number of WDM Channels.** Cuántos canales caben en la banda C (1530–1565 nm) y en la O
  (1260–1360 nm) con separación de 75 GHz.
- **24.3-2 Number of Nodes in a Broadcast-and-Select WDM Network.** $N$ máximo limitado por potencia:
  estrella con fibras de 2 km (0.3 dB/km), 1 dB de conector, acoplador que reparte por igual más 3 dB de
  pérdida, fuentes de 1 mW, sensibilidad −35 dBm, margen 5 dB.
- **24.3-3 Wavelength-Routed WDM Ring Network.** Anillo de 4 nodos y 6 canales; cada nodo añade/extrae
  en 3 λ y deja pasar las otras 3 (nodo 1: $\lambda_1,\lambda_2,\lambda_3$). Asignar ternas a los nodos 2, 3, 4 tal
  que cada nodo comparta exactamente un canal con cada otro nodo, sin que ese canal sea común con
  los nodos intermedios.

(El capítulo no marca ningún problema con asterisco; las subsecciones marcadas * son las de desempeño
de sistemas coherentes analógicos y digitales en §24.5.)

---

## Relación con Óptica No Lineal

**Para el curso (temas del programa):**
- *Absorción/dispersión y pulsos en medios dispersivos*: la Fig. 24.1-2 (p. 1077) es la referencia
  rápida de $\alpha(\lambda)$ y $D_\lambda(\lambda)$ del sílice (cero en 1312 nm, normal/anómala), y (24.1-3)
  $\sigma = |D|\sigma_\lambda L$ es la forma práctica del ensanchamiento por GVD. La equivalencia fibra ↔ filtro
  de chirp cuadrático con $b = D_\lambda L$ (p. 1098) enlaza con §22.2–22.3 y con $z_0 = \pi\tau_0^2/D_\nu$,
  $D_\nu = D_\lambda\lambda_o^2/c_o$ (p. 1095). El límite por pulsos limitados por transformada (24.2-12)–(24.2-13)
  es un ejercicio directo de producto tiempo–ancho de banda gaussiano ($\sigma_\nu = 0.375/\tau_0$).
- *Polarización*: PMD (24.1-4) como dispersión por birrefringencia aleatoria ($\propto\sqrt L$); requisito
  de polarización común en detección coherente (§24.5) y fibras PM.
- *Índice dependiente de la intensidad, SPM/XPM/FWM, Raman, Brillouin*: la lista de p. 1078–1079 es
  el catálogo de efectos χ⁽³⁾ vistos como **limitaciones** de sistemas (crosstalk WDM por XPM y FWM,
  SRS/SBS) y como **recursos** (solitones, amplificación Raman, OPA). Importante: en el libro el OPA
  (χ⁽³⁾ en fibra, §21.4C) necesita phase matching y aplanamiento de dispersión, y el FWM impide
  canales WDM equiespaciados (p. 1083). Los sistemas analógicos no sufren no linealidades porque la
  potencia no se concentra en pulsos (p. 1097).
- *Solitones*: (24.2-16) es la condición de equilibrio SPM–GVD con la notación del libro ($n_2$, $I_0$,
  $\beta''$, $\tau_0$, $\mathrm{sech}^2$, FWHM $=1.76\tau_0$); (24.2-17)–(24.2-18) tratan la interacción entre
  solitones vecinos ($L_p = \pi e^{r/2}z_0$) y el Ejemplo 24.2-1 da un cálculo numérico completo con
  $n_2$ y $A_{\rm eff}$ reales. Útil como problema tipo de "propagación de pulsos en fibras".
- *Gestión de dispersión*: (24.2-15) y la Fig. 24.2-16 muestran por qué en WDM hay que compensar
  también la **pendiente** de $D$, y por qué, en régimen no lineal, la ubicación de los compensadores sí
  importa (evitar pulsos cortos durante tramos largos, p. 1099).
- *Detección coherente* (§24.5): la fotomezcla (24.5-1)–(24.5-5) es el mismo álgebra de interferencia
  de dos ondas de frecuencias distintas (batido) que aparece en la mezcla de ondas; útil para entender
  medidas heterodinas de fase/frecuencia.

**Para el proyecto final (anillos add-drop en Si₃N₄, dispersión de guías, supercontinuo, sensado):**
- Las fibras de cristal fotónico/holey (p. 1078) ilustran que la dispersión de **guía de onda** puede
  dominar y desplazar/aplanar el cero de dispersión según la geometría: es la misma ingeniería de
  dispersión que se hace en guías de Si₃N₄ para supercontinuo (dispersión anómala a la λ de bombeo).
  Una fibra de núcleo hueco reduce la no linealidad; al contrario, confinar en un núcleo pequeño
  ($A_{\rm eff}$ pequeña) la aumenta: $P_{\rm pico} = I_0A_{\rm eff}$ en el Ejemplo 24.2-1.
- Los números del Ejemplo 24.2-1 ($n_2 = 2.6\times10^{-20}$ m²/W, $A_{\rm eff} = 60$ µm², 22.5 mW de pico
  para un solitón de 10 ps) sirven de comparación con Si₃N₄ ($n_2$ ≈ 10× mayor y $A_{\rm eff}$ ≈ 100×
  menor), que explica por qué el umbral de efectos no lineales en guías integradas es mucho menor.
- OADM/ROADM (p. 1111) y la interfaz transparente con acoplador direccional (Fig. 24.4-3) son la
  función de red que cumple un anillo add-drop: el filtro add-drop de microanillo es la implementación
  integrada del OADM (§23.2A). La separación de canales DWDM (100 GHz = 0.8 nm; 50 GHz = 0.4 nm en 1550
  nm, p. 1106) fija el FSR y la anchura (Q) que debe tener un anillo para filtrar un canal sin crosstalk.
- Sensado de índice: el anillo add-drop del proyecto desplaza su resonancia con el índice del cladding;
  los requisitos de estabilidad en λ de los láseres DWDM (control térmico, p. 1106) y la relación
  $\Delta\lambda = (\lambda_o^2/c_o)\Delta\nu$ son las mismas herramientas para traducir corrimientos de
  resonancia a frecuencia.
- Bandas y amplificadores (EDFA en C/L, Raman en 100 nm) ayudan a justificar operar el sensor y el
  supercontinuo alrededor de 1550 nm y a entender qué ancho de banda cubre la instrumentación.
