# Capítulo 12 — Photon Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 444–481 (PDF 466–503). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 12.
Notación del libro: dependencia temporal $e^{j\omega t}$ con $j=\sqrt{-1}$; campos reales en caligráfica
($\mathcal{E}(\mathbf{r},t)=\mathrm{Re}\{\mathbf{E}(\mathbf{r},t)\}$); amplitudes complejas en negrita ($\mathbf{E}$, $\mathbf{A}$);
$c_o$ = velocidad de la luz en el vacío, $c<c_o$ en un medio; $\lambda_o$ = longitud de onda en el vacío;
$\mathcal{T}$ y $\mathcal{R}$ = transmitancia y reflectancia de intensidad. Unidades SI, salvo que el libro
exprese flujos en photons/s·cm² (lo indico donde ocurre).

---

## Resumen del capítulo

El capítulo construye la **óptica de fotones**: un conjunto de reglas sencillas, extraídas de la
electrodinámica cuántica (QED), que se superponen a la óptica electromagnética para describir la
corpuscularidad, la localización y las fluctuaciones de la luz, conservando la óptica clásica como
caso límite (p. 445). La Sec. 12.1 introduce el fotón a partir de los modos de un resonador: la energía
de cada modo se cuantiza en unidades $h\nu$ (más la energía de punto cero $\tfrac12 h\nu$); el fotón
hereda del modo su frecuencia, polarización (vector de Jones interpretado como amplitudes de
probabilidad), distribución espacial (posición probabilística $p(\mathbf r)\,dA\propto I(\mathbf r)\,dA$),
momento ($\mathbf p=\hbar\mathbf k$), espín ($\pm\hbar$), momento angular orbital ($l\hbar$), interferencia
(Young con un solo fotón) y localización temporal (incertidumbre tiempo–energía $\sigma_E\sigma_t\ge\hbar/2$).
La Sec. 12.2 trata **flujos de fotones**: la conversión intensidad/potencia/energía ↔ densidad de flujo
de fotones/flujo/número medio de fotones (dividiendo por $h\bar\nu$), y la estadística del número de
fotones: Poisson para luz coherente ($\sigma_n^2=\bar n$, SNR $=\bar n$), Bose–Einstein para luz térmica
monomodo ($\sigma_n^2=\bar n+\bar n^2$, SNR $<1$), fórmula de Mandel para luz parcialmente coherente, y el
efecto de la partición aleatoria (divisor de haz, filtro absorbente, detector) sobre esas
estadísticas (distribución binomial; Poisson y Bose–Einstein conservan su forma). La Sec. 12.3
(avanzada) establece la analogía modo electromagnético ↔ oscilador armónico cuántico, define las
componentes en cuadratura $\mathbf x,\mathbf p$ con $\sigma_{\mathbf x}\sigma_{\mathbf p}\ge\tfrac14$, y presenta la luz en
estado coherente (círculo de incertidumbre, Poisson), el estado de vacío, la luz comprimida en
cuadratura, la luz comprimida en número de fotones (sub-Poisson, estados número) y la luz de haces
gemelos generada por conversión paramétrica descendente espontánea (SPDC), que es el puente directo
con la óptica no lineal.

---

## Secciones

### Introducción del capítulo (p. 445–446)

- Jerarquía de teorías (Fig. 12.0-1, p. 445): óptica de rayos ⊂ óptica de ondas ⊂ óptica
  electromagnética ⊂ óptica cuántica. La óptica electromagnética clásica (cap. 5) falla en ciertos
  fenómenos, lo que llevó a la **electrodinámica cuántica (QED)**, llamada *óptica cuántica* en el
  contexto óptico. En QED los campos $\mathbf E$ y $\mathbf H$ son operadores en un espacio de Hilbert con
  relaciones de conmutación. Ni siquiera QED es el árbitro final: la **teoría electrodébil** explica,
  p. ej., pequeñas rotaciones del plano de polarización que no conservan paridad (nota al pie:
  Vetter *et al.*, PRL 74, 2658, 1995).
- Definición (p. 445): la **óptica de fotones** es el conjunto de reglas que complementan la óptica
  electromagnética con relaciones simples tomadas de QED (corpuscularidad, localización,
  fluctuaciones). No pretende explicar todo lo que explica la óptica cuántica.
- Plan (p. 446): 12.1 el fotón; 12.2 flujos de fotones y estadística; 12.3 fluctuaciones de
  magnitud y fase del campo (luz coherente, comprimida, de haces gemelos). Interacción con átomos
  → cap. 13; con semiconductores → cap. 16.

### 12.1 THE PHOTON (p. 446)

**Idea central (p. 446).** La luz consiste en partículas, **fotones**, que llevan energía EM y momento,
momento angular intrínseco (espín, asociado a la polarización) y pueden llevar momento angular
orbital. Masa en reposo cero; velocidad $c_o$ en el vacío y $c<c_o$ en la materia. Tienen carácter
ondulatorio que fija su localización en espacio y tiempo y sus reglas de interferencia y difracción.
Historia: Planck (1900) cuantizó la energía de los modos de una cavidad para resolver el espectro
de cuerpo negro (cap. 13); Einstein (1905) consideró la luz misma como colección de fotones y
explicó el efecto fotoeléctrico (cap. 18).

#### Teoría electromagnética de la luz en un resonador (p. 446–447)

La luz en un resonador sin pérdidas de volumen $V$ es una superposición de modos ortogonales discretos
con distintas distribuciones espaciales, frecuencias y polarizaciones. El campo eléctrico es
$\mathcal E(\mathbf r,t)=\mathrm{Re}\{\mathbf E(\mathbf r,t)\}$ con

$$\mathbf E(\mathbf r,t)=\sum_{\mathbf q} A_{\mathbf q}\,U_{\mathbf q}(\mathbf r)\,\exp(j2\pi\nu_{\mathbf q}t)\,\hat{\mathbf e}_{\mathbf q}. \tag{12.1-1}$$

- $A_{\mathbf q}$: envolvente compleja del modo $\mathbf q$; $\nu_{\mathbf q}$: frecuencia; $\hat{\mathbf e}_{\mathbf q}$: vector
  unitario de polarización; $U_{\mathbf q}(\mathbf r)$: función espacial compleja normalizada,
  $\int_V |U_{\mathbf q}(\mathbf r)|^2\,d\mathbf r = 1$. La elección de funciones de expansión no es única (p. ej.,
  modos policromáticos).
- Resonador cúbico de lado $d$ (p. 447; ver Sec. 10.3 y Fig. 12.1-1a): ondas estacionarias

$$U_{\mathbf q}(\mathbf r)=\left(\frac{2}{d}\right)^{3/2}\sin\!\left(q_x\frac{\pi}{d}x\right)\sin\!\left(q_y\frac{\pi}{d}y\right)\sin\!\left(q_z\frac{\pi}{d}z\right), \tag{12.1-2}$$

con $\mathbf q=(q_x,q_y,q_z)$ enteros.
- Energía del modo (p. 447; densidad de energía $\tfrac12\epsilon|A_{\mathbf q}|^2|U_{\mathbf q}(\mathbf r)|^2$ según (5.4-9)):

$$E_{\mathbf q}=\tfrac12\epsilon\int_V |A_{\mathbf q}|^2|U_{\mathbf q}(\mathbf r)|^2\,d\mathbf r=\tfrac12\epsilon|A_{\mathbf q}|^2, \tag{12.1-3}$$

$V$ = volumen modal. Clásicamente $E_{\mathbf q}$ toma cualquier valor no negativo; la energía total es la
suma sobre modos.

#### Teoría de óptica de fotones de la luz en un resonador (p. 447)

Se mantiene la teoría anterior, pero la energía de cada modo se restringe a valores discretos
separados por una energía fija; cada unidad la lleva un fotón y un modo puede tener un número
arbitrario de fotones.

> **Recuadro (p. 447):** La luz en un resonador comprende un conjunto de modos, cada uno con un número
> entero de fotones idénticos. Las características del modo (frecuencia, distribución espacial,
> dirección de propagación, polarización) se asignan al fotón.

**Fig. 12.1-1 (p. 447):** (a) tres modos de distinta frecuencia y dirección en un resonador cúbico;
(b) energías permitidas de los modos de frecuencias $\nu_1,\nu_2,\nu_3$ (escaleras con peldaños
$h\nu_i$); los modos 1, 2 y 3 contienen 2, 0 y 3 fotones.

#### 12.1A Photon Energy (p. 448)

$$\boxed{E=h\nu=\hbar\omega} \tag{12.1-4}$$

$h=6.63\times10^{-34}$ J·s (constante de Planck), $\hbar\equiv h/2\pi$. La energía solo se añade o
quita a un modo en unidades de $h\nu$. Un modo con cero fotones tiene la **energía de punto cero**
$E_0=\tfrac12 h\nu$; con $n$ fotones:

$$E_n=\left(n+\tfrac12\right)h\nu,\qquad n=0,1,2,\dots \tag{12.1-5}$$

La energía de punto cero no suele observarse (se miden diferencias como $E_2-E_1$), pero se manifiesta
con campos estáticos y es crucial en la emisión espontánea (cap. 13).

Órdenes de magnitud (p. 448): fotón IR de $\lambda_o=1\ \mu$m → $\nu=3\times10^{14}$ Hz
($\lambda_o\nu=c_o$), $h\nu=1.99\times10^{-19}$ J $=1.24$ eV (energía cinética de un electrón acelerado
por 1.24 V). Fórmula de conversión:

$$E\,(\mathrm{eV})=\frac{1.24}{\lambda_o\,(\mu\mathrm{m})}. \tag{12.1-6}$$

Fotón de microondas de 1 cm → $h\nu=1.24\times10^{-4}$ eV. Número de onda recíproco (química):
1 cm⁻¹ ↔ $1.24/10000$ eV; 1 eV ↔ 8068.1 cm⁻¹.

**Fig. 12.1-2 (p. 449):** relación entre $\lambda_o$ (10 nm–10 cm), $\nu$ (10 PHz–1 GHz), $E$ en eV
(100 eV–10 μeV), J ($10^{-17}$–$10^{-24}$) y cm⁻¹ ($10^6$–$10^{-1}$). Marca $kT=26$ meV y los dominios de
fotónica y electrónica. Un fotón de $\lambda_o=1\ \mu$m: 300 THz, 1.24 eV, $1.99\times10^{-19}$ J, $10^4$ cm⁻¹.

Observación (p. 448): a mayor frecuencia, mayor energía por fotón y más evidente la naturaleza
corpuscular (rayos X y γ: partículas; radio: ondas); en el óptico coexisten ambos comportamientos,
de ahí la necesidad de la óptica de fotones.

#### 12.1B Photon Polarization (p. 448–451)

Cada onda plana monocromática tiene dos modos de polarización; el fotón tiene la polarización del
modo que ocupa. Como los modos de polarización del espacio libre son degenerados, la base no es única
($x,y$; $x',y'$; circular derecha/izquierda). Si un fotón en un modo (lineal $x$) se observa en otra
base ($x',y'$), su energía no se puede dividir → interpretación probabilística (p. 449).

Clásicamente (Sec. 6.1A) el vector de Jones $(A_x,A_y)$ se transforma al sistema girado 45° como

$$A_{x'}=\tfrac{1}{\sqrt2}(A_x-A_y),\qquad A_{y'}=\tfrac{1}{\sqrt2}(A_x+A_y). \tag{12.1-7}$$

Una onda lineal en $x$: $(A_0,0)$ en $x$–$y$; $(\tfrac{1}{\sqrt2}A_0,\tfrac{1}{\sqrt2}A_0)$ en $x'$–$y'$.

> **Recuadro (p. 449):** En óptica de fotones, el estado de polarización de un fotón se describe por
> un vector de Jones de componentes complejas $(A_x,A_y)$ normalizado con $|A_x|^2+|A_y|^2=1$. $A_x$ y
> $A_y$ son amplitudes de probabilidad complejas; $|A_x|^2$ y $|A_y|^2$ son las probabilidades de
> observar el fotón en los modos lineales $x$ y $y$.

Las componentes se transforman como vectores de Jones ordinarios; un fotón puede existir
probabilísticamente en más de un modo.

- **Fotones linealmente polarizados (p. 449–450).** Fotón en $x$: $(1,0)$; en la base a 45°:
  $(\tfrac{1}{\sqrt2},\tfrac{1}{\sqrt2})$ → probabilidad $\tfrac12$ en $x'$ y $\tfrac12$ en $y'$.
  **Fig. 12.1-3 (p. 450):** un fotón $x$ = superposición de un fotón $x'$ (prob. ½) y uno $y'$ (prob. ½).
- **EJEMPLO 12.1-1 (p. 450). Transmisión de un fotón linealmente polarizado por un polarizador.**
  Fotón lineal en $x$; polarizador con eje $x'$ a ángulo $\theta$. Jones en $x'$–$y'$:
  $(\cos\theta,-\sin\theta)$ [ec. (6.1-21), (6.1-22)]. Probabilidad de paso $p(\theta)=\cos^2\theta$;
  de bloqueo $1-p(\theta)=\sin^2\theta$. Coincide con la transmitancia clásica (Sec. 6.1B):
  $p(\theta)=\mathcal T(\theta)$. **Fig. 12.1-4 (p. 450):** $p(\theta)$ vs $\theta$ (1 en 0, 0 en $\pi/2$, 1 en $\pi$).
- **Fotones circularmente polarizados (p. 450–451).** Jones $\tfrac{1}{\sqrt2}(1,\pm j)$ (+ derecha,
  − izquierda) en la base lineal $x$–$y$ → probabilidad ½ de pasar por un polarizador lineal en $x$ o
  en $y$ (y en cualquier dirección). Recíprocamente, un fotón lineal es superposición de RCP y LCP con
  probabilidad ½ cada uno. **Fig. 12.1-5 (p. 451):** un fotón LP = un fotón RCP (½) o un fotón LCP (½).

#### 12.1C Photon Position (p. 451–452)

A cada fotón de frecuencia $\nu$ se asocia la función de onda compleja $U(\mathbf r)\exp(j2\pi\nu t)$ del modo.
Al incidir sobre un detector de área $dA$ normal a la propagación en $\mathbf r$, su indivisibilidad hace
que se detecte entero o no se detecte. La posición es probabilística, gobernada por la intensidad
$I(\mathbf r)\propto|U(\mathbf r)|^2$:

> **Recuadro (p. 451) — Posición del fotón:** la probabilidad $p(\mathbf r)\,dA$ de observar un fotón en un
> punto $\mathbf r$ dentro de un área incremental $dA$, en cualquier instante, es proporcional a la
> intensidad óptica local,
> $$p(\mathbf r)\,dA\propto I(\mathbf r)\,dA. \tag{12.1-8}$$

Ejemplo: onda estacionaria $I\propto\sin^2(\pi z/d)$, $0\le z\le d$ → máxima probabilidad en $z=d/2$,
nunca en $z=0$ ni $z=d$. Los fotones ópticos son entidades extendidas *y* localizadas:
**dualidad onda–partícula**; la localización se manifiesta al detectar.

- **EJERCICIO 12.1-1 (p. 451). Fotones en un haz gaussiano.** (a) Fotón descrito por el modo
  TEM$_{0,0}$ (Secs. 3.1B, 5.4A, 10.2B): probabilidad de detectarlo dentro de un círculo de radio
  $W_0$ en la cintura, con $I(\rho,z=0)\propto\exp(-2\rho^2/W_0^2)$. (b) Con $n$ fotones independientes,
  número medio dentro del círculo. *(Cálculo propio, no del libro: integrando
  $\int_0^{W_0}e^{-2\rho^2/W_0^2}2\pi\rho\,d\rho$ y normalizando, $p=1-e^{-2}\approx0.865$; (b) $\bar n\approx0.865\,n$.)*

- **Transmisión de un solo fotón por un divisor de haz (p. 452).** Divisor ideal sin pérdidas con
  transmitancia $\mathcal T$ y reflectancia $\mathcal R=1-\mathcal T$; clásicamente $I_t=\mathcal T I$, $I_r=(1-\mathcal T)I$.
  Como el fotón es indivisible, elige un camino: probabilidad de transmisión $=\mathcal T=I_t/I$, de
  reflexión $=1-\mathcal T=I_r/I$ (regla (12.1-8)). Equivale a lanzar una moneda sesgada.
  **Fig. 12.1-6 (p. 452):** un fotón incidente → un fotón transmitido (prob. $\mathcal T$) o reflejado
  (prob. $\mathcal R=1-\mathcal T$).

#### 12.1D Photon Momentum (p. 452–454)

Clásicamente (Sec. 5.4A) una onda plana lleva densidad de momento lineal $(W/c)\hat{\mathbf k}$ ($W$
= densidad de energía). En óptica de fotones $\mathbf p=(E/c)\hat{\mathbf k}$ con $E=\hbar\omega=\hbar ck$:

> **Recuadro (p. 452):** El momento lineal de un fotón en un modo de onda plana de vector de onda $\mathbf k$ es
> $$\mathbf p=\hbar\mathbf k. \tag{12.1-9}$$
> Su magnitud es $p=\hbar k=\hbar\omega/c=\hbar2\pi/\lambda$, de modo que
> $$p=E/c=h/\lambda. \tag{12.1-10}$$

- ***Momento de una onda localizada (p. 452–453).** Una onda general $U(\mathbf r)\exp(j2\pi\nu t)$ se
  expande en ondas planas (óptica de Fourier, cap. 4); la componente de vector $\mathbf k$ es
  $A(\mathbf k)\exp(-j\mathbf k\cdot\mathbf r)\exp(j2\pi\nu t)$.

  > **Recuadro (p. 453):** El momento de un fotón descrito por una función de onda arbitraria
  > $U(\mathbf r)\exp(j2\pi\nu t)$ es incierto. Vale
  > $$\mathbf p=\hbar\mathbf k \tag{12.1-11}$$
  > con probabilidad proporcional a $|A(\mathbf k)|^2$, donde $A(\mathbf k)$ es la amplitud de la componente
  > de Fourier de onda plana de $U(\mathbf r)$ con vector de onda $\mathbf k$.

  Si $f(x,y)=U(x,y,0)$ en el plano $z=0$, $A(\mathbf k)=F(k_x/2\pi,k_y/2\pi)$ con $F(\nu_x,\nu_y)$ la
  transformada de Fourier 2D de $f$. Por la relación duración–ancho de banda (Apéndice A, (A.2-6)):
  con $\sigma_x$ la incertidumbre de posición en $x$ y
  $\sigma_\theta=\sin^{-1}(\sigma_{kx}/k)\approx(\lambda/2\pi)\sigma_{kx}$ la incertidumbre angular ($\ll1$),
  $\sigma_x\sigma_{kx}\ge\tfrac12$ equivale a $\sigma_x\sigma_\theta\ge\lambda/4\pi$ (p. 453).
  Onda plana: $\sigma_\theta=0$, $\sigma_x=\infty$; al pasar por una abertura se localiza a costa de un
  esparcimiento en dirección (paralelo a la difracción, cap. 4). Onda esférica: posición bien
  definida, dirección del momento totalmente incierta.
- **Presión de radiación (p. 453).** El átomo que emite un fotón retrocede con momento $h\nu/c$; el
  momento del fotón se transfiere a objetos de masa finita (fuerza, deflexión de haces atómicos);
  presión = fuerza/área.
- **EJERCICIO 12.1-2 (p. 453). Retroceso por momento de fotón.** Velocidad de retroceso de un átomo de
  $^{198}$Hg que emite un fotón de 4.88 eV; compararla con la velocidad térmica rms a $T=300$ K
  ($\tfrac12 m v^2=\tfrac32 kT$, $k=1.38\times10^{-23}$ J/K). *(Cálculo propio: $p=E/c_o=2.6\times10^{-27}$
  kg·m/s, $m=3.29\times10^{-25}$ kg → $v_{\rm rec}\approx7.9\times10^{-3}$ m/s; $v_{\rm rms}=\sqrt{3kT/m}\approx194$ m/s.)*
- **Momento angular de espín (p. 454).**

  $$\boxed{\mathbb S=\pm\hbar} \tag{12.1-12}$$

  + (−) para polarización circular derecha (izquierda); el vector de espín es paralelo (antiparalelo)
  al momento lineal/vector de onda. Los fotones lineales tienen igual probabilidad de espín paralelo
  o antiparalelo. Un fotón circular ejerce torque (p. ej., sobre una lámina de media onda).
- **Momento angular orbital (p. 454).** Un haz Laguerre–Gauss $U_{l,m}(\rho,\phi,z)$ [(3.4-1)] con fase
  azimutal $\exp(jl\phi)$ y frente helicoidal lleva momento angular independiente de la polarización:
  $L=l\hbar$ por fotón ($l\ne0$). Modo de galería de susurros (WGM) de un resonador cilíndrico
  (Sec. 10.3B): condición de resonancia $2\pi a=q\lambda$ ($a$ = radio, $q=1,2,\dots$); momento lineal
  $p=\hbar k=\hbar2\pi/\lambda=q\hbar/a$ → momento angular $ap=q\hbar$. En una microesfera (Sec. 10.4C)
  $L=\ell\hbar$ con $\ell$ el entero de la resonancia sobre un círculo máximo; número cuántico de
  momento angular análogo al del átomo de hidrógeno (Sec. 13.1A).

#### 12.1E Photon Interference (p. 454–456)

El experimento de Young (Ej. 2.5-2) puede hacerse con un solo fotón en el aparato. Se calcula la
intensidad con óptica ondulatoria y se convierte en densidad de probabilidad de posición. Para dos
pinholes iluminados por onda plana, en la aproximación paraboloidal:

$$I(x)\approx2I_0\left(1+\cos\frac{2\pi x\theta}{\lambda}\right), \tag{12.1-13}$$

$I_0$ = intensidad de cada onda en el plano de observación, $\theta$ = ángulo subtendido por los dos
pinholes desde el plano de observación ($\theta=2a/d$ en la Fig. 12.1-7), el eje $x$ une los agujeros.
**Fig. 12.1-7 (p. 455):** Young con un solo fotón; el patrón $I(x)$ (periodo $\lambda/\theta$) es la
densidad de probabilidad de detección en $x$.

Con un solo fotón: probabilidad $\propto I(x)$; nunca se detecta donde $I(x)=0$. El histograma de
muchas repeticiones (Taylor, 1909) reproduce el patrón clásico. La interferencia se debe a la
naturaleza extendida del fotón, que pasa por *ambos* agujeros; tapar uno destruye el patrón (p. 455).

- **EJERCICIO 12.1-3 (p. 455). Un solo fotón en un interferómetro de Mach–Zehnder.** Onda plana de
  longitud $\lambda$ dividida y recombinada (Fig. 12.1-8, p. 456; ver Fig. 2.5-3a), divisores con
  $\mathcal T=\mathcal R=\tfrac12$, sin pérdidas. Graficar la probabilidad de encontrar el fotón en el detector
  vs $d/\lambda$ ($0\le d/\lambda\le1$, $d$ = diferencia de caminos). ¿Dónde está el fotón cuando esa
  probabilidad no es 1? *(Cálculo propio: $p=\cos^2(\pi d/\lambda)$; el resto de la probabilidad sale
  por el otro puerto del segundo divisor.)*

#### 12.1F Photon Time (p. 456–457)

Los modos de (12.1-1) son monocromáticos, "eternos": un fotón en un modo monocromático se detecta con
igual probabilidad en cualquier instante. Una expansión en modos policromáticos (paquetes de onda
localizados en el tiempo) también es válida; la probabilidad de detectar el fotón de función de onda
$U(\mathbf r,t)$ (Sec. 2.6A) entre $t$ y $t+dt$ es $\propto I(\mathbf r,t)\,dt\propto|U(\mathbf r,t)|^2dt$.

> **Recuadro (p. 456) — Posición y tiempo del fotón:** la probabilidad de observar un fotón en $\mathbf r$
> dentro de $dA$ y durante $dt$ a partir de $t$ es proporcional a la intensidad del modo en $\mathbf r$ y $t$:
> $$\boxed{p(\mathbf r,t)\,dA\,dt\propto I(\mathbf r,t)\,dA\,dt\propto|U(\mathbf r,t)|^2dA\,dt.} \tag{12.1-14}$$

**Incertidumbre tiempo–energía (p. 456–457).** Un fotón monocromático tiene tiempo totalmente
incierto y energía $h\nu$ exacta; uno en un paquete de duración $\sigma_t$ es policromático. Con

$$U(t)=\int_{-\infty}^{\infty}V(\nu)\exp(j2\pi\nu t)\,d\nu, \tag{12.1-15}$$

$V(\nu)$ = transformada de Fourier de $U(t)$ (Sec. A.1); $\sigma_\nu$ = ancho de $|V(\nu)|^2$ (ancho
espectral); $\sigma_t$ = ancho rms de $|U(t)|^2$ (ancho rms de potencia). Relación de reciprocidad
duración–ancho de banda: $\sigma_\nu\sigma_t\ge1/4\pi$, o $\sigma_\omega\sigma_t\ge\tfrac12$ (Sec. A.2).
La energía $\hbar\omega$ no puede especificarse mejor que $\sigma_E=\hbar\sigma_\omega$, luego

$$\boxed{\sigma_E\,\sigma_t\ge\frac{\hbar}{2}} \tag{12.1-16}$$

**relación de incertidumbre tiempo–energía** (p. 457), análoga a la posición–momento. La energía media
del fotón policromático es $\bar E=h\bar\nu=\hbar\bar\omega$. Resumen: fotón monocromático
($\sigma_\nu\to0$) ↔ duración eterna ($\sigma_t\to\infty$); fotón de paquete de ondas = paquete
confinado y viajero de energía.

- **EJERCICIO 12.1-4 (p. 457). Un solo fotón en un paquete gaussiano.** Paquete de onda plana
  (Sec. 2.6A) con un fotón viajando en $z$:
  $$U(\mathbf r,t)=\mathfrak a\!\left(t-\frac zc\right), \tag{12.1-17}$$
  $$\mathfrak a(t)=\exp\!\left(-\frac{t^2}{4\tau^2}\right)\exp(j2\pi\nu_0t). \tag{12.1-18}$$
  (a) Mostrar que $\sigma_t=\tau$ y $\sigma_z=c\sigma_t$. (b) Mostrar que energía y momento cumplen las
  relaciones de incertidumbre mínima
  $$\sigma_E\sigma_t=\hbar/2, \tag{12.1-19}$$
  $$\sigma_z\sigma_p=\hbar/2. \tag{12.1-20}$$
  (12.1-20) es el límite mínimo de la **relación de incertidumbre posición–momento de Heisenberg**
  [(A.2-7)].

#### Summary de la Sec. 12.1 (recuadro, p. 457–458)

La radiación EM se describe como suma de modos, p. ej., ondas planas uniformes monocromáticas:

$$\mathbf E(\mathbf r,t)=\sum_{\mathbf q}A_{\mathbf q}\exp(-j\mathbf k_{\mathbf q}\cdot\mathbf r)\exp(j2\pi\nu_{\mathbf q}t)\,\hat{\mathbf e}_{\mathbf q}. \tag{12.1-21}$$

Cada onda plana tiene dos polarizaciones ortogonales $\hat{\mathbf e}_{\mathbf q}$. Al medir la energía de un modo
el resultado es un número entero (en general aleatorio) de cuantos. Cada fotón del modo $\mathbf q$ tiene:
- Energía $E=h\nu_{\mathbf q}$; momento $\mathbf p=\hbar\mathbf k_{\mathbf q}$; espín $\mathbb S=\pm\hbar$ si es circular;
- igual probabilidad de encontrarse en cualquier lugar y en cualquier instante (onda plana monocromática).

Expansión alternativa en modos no monocromáticos (cuasi-monocromáticos) y no planos:

$$\mathbf E(\mathbf r,t)=\sum_{\mathbf q}A_{\mathbf q}U_{\mathbf q}(\mathbf r,t)\,\hat{\mathbf e}_{\mathbf q}. \tag{12.1-22}$$

Entonces: posición y tiempo gobernados por $U_{\mathbf q}(\mathbf r,t)$ (probabilidad $\propto|U_{\mathbf q}(\mathbf r,t)|^2dA\,dt$);
si $U_{\mathbf q}$ tiene duración finita $\sigma_t$, la energía $h\nu_{\mathbf q}$ tiene incertidumbre
$h\sigma_\nu\ge h/4\pi\sigma_t$; si tiene extensión transversal finita, la dirección del momento es
incierta (se obtiene descomponiendo $U_{\mathbf q}$ en ondas planas, $\mathbf k\leftrightarrow\hbar\mathbf k$).

### 12.2 PHOTON STREAMS (p. 458)

El número de fotones en un modo es generalmente aleatorio (depende del proceso de creación, p. ej.,
emisión atómica, cap. 13) y su distribución la fija el estado cuántico (Sec. 12.3). Un flujo débil
sobre una superficie fotosensible registra fotones en instantes y puntos aleatorios según (12.1-14)
(visible con el ojo adaptado a la oscuridad). Se separan el patrón temporal (detector de buena
resolución temporal que integra sobre un área $A$: probabilidad en $[t,t+dt]$ proporcional a la
potencia $P(t)=\int_A I(\mathbf r,t)\,dA$; **Fig. 12.2-1, p. 459**: detector + osciloscopio con pulsos en
instantes aleatorios) y el patrón espacial (detector de buena resolución espacial que integra un
tiempo $T$, p. ej., película: probabilidad en $dA$ proporcional a $\int_0^T I(\mathbf r,t)\,dt$;
**Fig. 12.2-2, p. 459**: imagen granulada de Max Planck tomada con muy poca luz, cada punto blanco es
un registro de fotón cuya densidad sigue la intensidad local).

#### 12.2A Mean Photon Flux (p. 459–462)

**Densidad media de flujo de fotones (p. 460).** Luz monocromática de frecuencia $\nu$ e intensidad
$I(\mathbf r)$ (W/cm² en el libro):

$$\boxed{\phi(\mathbf r)=\frac{I(\mathbf r)}{h\nu}} \tag{12.2-1}$$

(fotones/s·cm²). Para luz cuasi-monocromática de frecuencia central $\bar\nu$:

$$\phi(\mathbf r)\approx\frac{I(\mathbf r)}{h\bar\nu}. \tag{12.2-2}$$

**Tabla 12.2-1 (p. 460)** — ver sección de tablas más abajo.

**Flujo medio de fotones (p. 460)**, fotones/s:

$$\boxed{\Phi=\int_A\phi(\mathbf r)\,dA=\frac{P}{h\bar\nu}} \tag{12.2-3}$$

$$P=\int_A I(\mathbf r)\,dA \tag{12.2-4}$$

(potencia óptica, W). Ejemplo: 1 nW a $\lambda_o=0.2\ \mu$m → $\Phi\approx10^9$ fotones/s:

$$\boxed{1\ \mathrm{nW\ a\ }\lambda_o=0.2\ \mu\mathrm m\ \rightarrow\ 1\ \mathrm{fotón/ns}.} \tag{12.2-5}$$

A $\lambda_o=1\ \mu$m cada fotón lleva 1/5 de la energía → 1 nW ↔ 5 fotones/ns (p. 461).

**Número medio de fotones (p. 461)** detectados en el área $A$ y el intervalo $T$:

$$\bar n=\Phi T=\frac{E}{h\bar\nu}, \tag{12.2-6}$$

$E=PT$ = energía óptica (J).

Resumen clásico ↔ cuántico (p. 461):

| Clásico | | Cuántico | |
|---|---|---|---|
| Intensidad óptica | $I(\mathbf r)$ | Densidad de flujo de fotones | $\phi(\mathbf r)=I(\mathbf r)/h\bar\nu$ |
| Potencia óptica | $P$ | Flujo de fotones | $\Phi=P/h\bar\nu$ |
| Energía óptica | $E$ | Número de fotones | $\bar n=E/h\bar\nu$ |

**Densidades espectrales de flujo de fotones (p. 461)**, para luz policromática de ancho no despreciable:

| Clásico | | Cuántico | |
|---|---|---|---|
| $I_\nu$ | (W/cm²·Hz) | $\phi_\nu=I_\nu/h\nu$ | (fotones/s·cm²·Hz) |
| $P_\nu$ | (W/Hz) | $\Phi_\nu=P_\nu/h\nu$ | (fotones/s·Hz) |
| $E_\nu$ | (J/Hz) | $\bar n_\nu=E_\nu/h\nu$ | (fotones/Hz) |

$P_\nu\,d\nu$ = potencia en $[\nu,\nu+d\nu]$; $\Phi_\nu\,d\nu$ = flujo de fotones con frecuencia en ese rango.

**Luz variable en el tiempo (p. 461–462):**

$$\phi(\mathbf r,t)=\frac{I(\mathbf r,t)}{h\bar\nu}, \tag{12.2-7}$$
$$\Phi(t)=\int_A\phi(\mathbf r,t)\,dA=\frac{P(t)}{h\bar\nu}, \tag{12.2-8}$$
$$P(t)=\int_A I(\mathbf r,t)\,dA, \tag{12.2-9}$$
$$\bar n=\int_0^T\Phi(t)\,dt=\frac{E}{h\bar\nu}, \tag{12.2-10}$$
$$E=\int_0^T P(t)\,dt=\int_0^T\!\!\int_A I(\mathbf r,t)\,dA\,dt. \tag{12.2-11}$$

#### 12.2B Randomness of Photon Flow (p. 462–463)

Con $I(\mathbf r,t)$ constante, (12.1-14) da la densidad de probabilidad de detección de un fotón en
$(\mathbf r,t)$. La misma $I(\mathbf r,t)$ gobierna flujos de fotones, pero con otra interpretación (p. 462, en
cursiva en el libro):

> *Para flujos de fotones, la intensidad clásica $I(\mathbf r,t)$ determina la densidad media de flujo de
> fotones $\phi(\mathbf r,t)$. Las propiedades de la fuente determinan las fluctuaciones de $\phi(\mathbf r,t)$.*

Ejemplo (p. 462): a $\lambda_o=1\ \mu$m, $P=1$ nW lleva en *promedio* $\Phi=5$ fotones/ns = 0.005
fotones/ps; en $10^5$ intervalos de 1 ps, la mayoría vacíos, ~500 con un fotón, muy pocos con dos o más.
Si $P(t)$ varía, la densidad media de detecciones sigue $P(t)$ ($\Phi(t)=P(t)/h\bar\nu$), además de las
fluctuaciones propias de la fuente. **Fig. 12.2-3 (p. 463):** (a) potencia constante y llegadas
aleatorias; (b) potencia variable y llegadas más densas donde $P(t)$ es mayor. En el dominio espacial
(Fig. 12.2-2) la granulosidad es ruido de fluctuación de posiciones; desaparece cuando la densidad
media de flujo es grande (foto de la p. 444) y se recupera la intensidad clásica.

#### 12.2C Photon-Number Statistics (p. 463–469)

Motivación (p. 463): reducir ruido en imágenes débiles y optimizar comunicaciones ópticas (cap. 24):
en un pulso solo se controla el número *medio* de fotones; el real varía de pulso a pulso → errores.
La distribución depende de la fuente; bajo ciertas condiciones las llegadas son eventos independientes
a tasa igual al flujo (potencia determinista: luz coherente; potencia aleatoria: luz parcialmente
coherente, cap. 11, donde las fluctuaciones correlacionadas alteran la estadística).

**Luz coherente (p. 463–465).** Potencia $P$ constante, flujo $\Phi=P/h\bar\nu$ constante, instantes
aleatorios (Fig. 12.2-3a y **Fig. 12.2-4, p. 464**: en intervalos sucesivos de duración $T$ se cuentan
$n=9,8,7,11$ fotones). Con $\bar n=\Phi T=PT/h\bar\nu$ y registros estadísticamente independientes:

$$\boxed{p(n)=\frac{\bar n^{\,n}\exp(-\bar n)}{n!},\qquad n=0,1,2,\dots} \tag{12.2-12}$$

**Distribución de Poisson.** **Fig. 12.2-5 (p. 464):** $p(n)$ en escala semilogarítmica para
$\bar n=0.1,1,5,10$; las curvas se ensanchan al crecer $\bar n$.

*Derivación (p. 464):* dividir $T$ en $N$ subintervalos de duración $T/N$ con probabilidad $p=\bar n/N$
de un fotón y $1-p$ de ninguno; binomial
$p(n)=\frac{N!}{n!(N-n)!}p^n(1-p)^{N-n}=\frac{N!}{n!(N-n)!}\left(\frac{\bar n}{N}\right)^n\left(1-\frac{\bar n}{N}\right)^{N-n}$;
con $N\to\infty$, $N!/(N-n)!N^n\to1$ y $[1-\bar n/N]^{N-n}\to\exp(-\bar n)$ → (12.2-12).

**Media y varianza (p. 464–465):**

$$\bar n=\sum_{n=0}^{\infty}n\,p(n), \tag{12.2-13}$$
$$\sigma_n^2=\sum_{n=0}^{\infty}(n-\bar n)^2p(n). \tag{12.2-14}$$

$p(n)$, $\bar n$, $\sigma_n$ = "estadística del número de fotones". Para Poisson:

$$\boxed{\sigma_n^2=\bar n} \tag{12.2-15}$$

Ej.: $\bar n=100$ → $\sigma_n=10$ (±10 fotones). Poisson aplica al láser ideal monomodo (cap. 15),
corresponde al **estado coherente** (Sec. 12.3A) y aproxima bien muchas fuentes, incluida luz térmica
multimodo (p. 465).

**Relación señal/ruido (p. 465):**

$$\mathrm{SNR}=\frac{(\text{media})^2}{\text{varianza}}=\frac{\bar n^2}{\sigma_n^2}. \tag{12.2-16}$$

Para Poisson:

$$\boxed{\mathrm{SNR}=\bar n} \tag{12.2-17}$$

(crece linealmente con el número medio de cuentas). Ejemplo: con $\bar n=20$, la probabilidad de no
recibir ningún fotón es $p(0)\approx2\times10^{-9}$ (probabilidad de error, cap. 24).

**Luz térmica (p. 465–467).** Resonador con paredes a temperatura $T$ (K); en equilibrio, la
ocupación del nivel $E_n$ de un modo sigue la **distribución de Boltzmann**

$$\boxed{P(E_n)\propto\exp\!\left(-\frac{E_n}{kT}\right)} \tag{12.2-18}$$

$k=1.38\times10^{-23}$ J/K (constante de Boltzmann; origen en Sec. 13.2). A $T=300$ K, $kT=0.026$ eV
≡ 208 cm⁻¹. **Fig. 12.2-6 (p. 466):** $P(E_n)$ vs $E_n$ para $T_2>T_1$ (decaimiento exponencial más
lento a mayor $T$). Con $E_n=(n+\tfrac12)h\nu$:

$$p(n)\propto\exp\!\left(-\frac{nh\nu}{kT}\right)=\left[\exp\!\left(-\frac{h\nu}{kT}\right)\right]^n,\quad n=0,1,2,\dots \tag{12.2-19}$$

Normalización $\sum_n p(n)=1$ → constante $[1-\exp(-h\nu/kT)]$; la energía de punto cero desaparece en
la normalización. En términos de la media:

$$\boxed{p(n)=\frac{1}{\bar n+1}\left(\frac{\bar n}{\bar n+1}\right)^n} \tag{12.2-20}$$

**Distribución de Bose–Einstein** (en probabilidad, *distribución geométrica*), con

$$\bar n=\frac{1}{\exp(h\nu/kT)-1} \tag{12.2-21}$$

(coincide con (13.4-7) para fotones en equilibrio con átomos). **Fig. 12.2-7 (p. 467):** $p(n)$
semilogarítmica para $\bar n=0.1,1,5,10$: rectas decrecientes; mucho más ancha y monótona decreciente
frente a Poisson (Fig. 12.2-5). Varianza:

$$\boxed{\sigma_n^2=\bar n+\bar n^2} \tag{12.2-22}$$

(mayor que Poisson: más fluctuación). SNR:

$$\mathrm{SNR}=\frac{\bar n}{\bar n+1}, \tag{12.2-23}$$

siempre $<1$ sin importar la potencia; amplitud y fase de la luz térmica son aleatorias (cap. 11), lo
que ensancha $p(n)$; demasiado ruidosa para transmisión de datos a alta tasa.

- **EJERCICIO 12.2-1 (p. 467). Energía media en un modo de resonador.** Mostrar que en equilibrio
  térmico a $T$ la energía media de un modo de frecuencia $\nu$ es
  $$\bar E=kT\,\frac{h\nu/kT}{\exp(h\nu/kT)-1}. \tag{12.2-24}$$
  Graficar $\bar E(\nu)$ para varios $kT/h$; con Taylor del denominador obtener la aproximación para
  $h\nu/kT\ll1$ y explicarla físicamente. *(Nota propia: $\bar E=\bar n\,h\nu$ sin punto cero; el límite
  da $\bar E\approx kT$, equipartición clásica.)*

***Otras fuentes de luz (p. 468–469).** Para luz coherente $P$ es determinista y $p(n)=w^ne^{-w}/n!$ con

$$w=\frac{1}{h\nu}\int_0^TP(t)\,dt=\frac{1}{h\nu}\int_0^T\!\!\int_AI(\mathbf r,t)\,dA\,dt, \tag{12.2-25}$$

el flujo integrado de fotones (potencia integrada normalizada) $=\bar n$. Si $I(\mathbf r,t)$ fluctúa
aleatoriamente, $w$ es aleatorio con densidad $p(w)$ y se promedia la Poisson condicional
$p(n|w)=w^ne^{-w}/n!$:

$$\boxed{p(n)=\int_0^\infty\frac{w^ne^{-w}}{n!}\,p(w)\,dw} \tag{12.2-26}$$

**Fórmula de Mandel** (distribución de conteo de Poisson *doblemente estocástica*): dos fuentes de
aleatoriedad, los fotones (Poisson localmente) y las fluctuaciones de intensidad. Solo aplica a
*luz clásica*; la teoría general requiere el estado cuántico (Sec. 12.3). Media y varianza:

$$\bar n=\bar w, \tag{12.2-27}$$
$$\sigma_n^2=\bar n+\sigma_w^2, \tag{12.2-28}$$

$\sigma_w^2$ = varianza de $w$ (término de Poisson + término de fluctuaciones clásicas de potencia).
Ejemplo importante: $w$ con densidad exponencial

$$p(w)=\begin{cases}\dfrac{1}{\bar w}\exp\!\left(-\dfrac{w}{\bar w}\right), & w\ge0\\[6pt] 0, & w<0,\end{cases} \tag{12.2-29}$$

apropiada para luz cuasi-monocromática espacialmente coherente con partes real e imaginaria de la
amplitud compleja independientes y gaussianas, cuando el tiempo de coherencia $\tau_c\gg T$ y el área de
coherencia $A_c\gg A$ (cap. 11). Sustituida en (12.2-26) da exactamente Bose–Einstein (12.2-20): el
campo gaussiano tiene la misma estadística que la luz térmica monomodo. Si $A$ y $T$ no son pequeños,
luz térmica multimodo (Probs. 12.2-6 a 12.2-8).

#### 12.2D Random Partitioning of Photon Streams (p. 469–471)

Un flujo se **particiona** cuando se le quitan fotones: *partición aleatoria* si se desvían (divisor
de haz sin pérdidas, **Fig. 12.2-8, p. 469**), *selección aleatoria* si se destruyen (filtro absorbente:
pasan o se convierten en calor). Se supone que cada fotón sufre un ensayo de Bernoulli independiente
(válido si el flujo entra por un solo puerto del divisor, lo que elimina interferencia). Resultados
aplicables a ambos casos.

Divisor con $\mathcal T$ y $\mathcal R=1-\mathcal T$: números medios transmitido y reflejado $\mathcal T\bar n$ y
$(1-\mathcal T)\bar n$. Con exactamente $n$ fotones incidentes, el número transmitido $m$ es binomial:

$$p(m)=\binom nm\mathcal T^m(1-\mathcal T)^{n-m},\qquad m=0,1,\dots,n, \tag{12.2-30}$$

$\binom nm=n!/m!(n-m)!$;

$$\bar m=\mathcal Tn, \tag{12.2-31}$$
$$\sigma_m^2=\mathcal T(1-\mathcal T)n=(1-\mathcal T)\bar m. \tag{12.2-32}$$

SNR $=\bar m^2/\sigma_m^2=\bar m/(1-\mathcal T)$ crece con $\bar m$: a altas intensidades la partición sigue
$\mathcal T$ y $1-\mathcal T$ (se recupera la óptica clásica). Si el número incidente es aleatorio con
distribución $p_0(n)$, $p(m)=\sum_np(m|n)p_0(n)$:

$$\boxed{p(m)=\sum_{n=m}^{\infty}\binom nm\mathcal T^m(1-\mathcal T)^{n-m}p_0(n).} \tag{12.2-33}$$

**Estadística del número de fotones bajo partición aleatoria.** Si $p_0(n)$ es Poisson (coherente) o
Bose–Einstein (térmica monomodo), $p(m)$ tiene la misma forma con media reducida por $\mathcal T$ (ambas
distribuciones *conservan su forma*). La luz con número determinista de fotones (Sec. 12.3B) no la
conserva → falta de robustez (p. 470). SNR tras partición:

$$\mathrm{SNR}=\begin{cases}\mathcal T\bar n & \text{luz coherente} \qquad (12.2\text{-}34)\\[4pt] \dfrac{\mathcal T\bar n}{\mathcal T\bar n+1} & \text{luz térmica.} \qquad (12.2\text{-}35)\end{cases}$$

Como $\mathcal T\le1$, la partición reduce la SNR (introduce ruido), más severamente para luz de número
determinista. Lo mismo aplica a la *detección*: de $n$ incidentes se detectan $m$ con $p(m)$ dada por
(12.2-33) (teoría de fotodetección, cap. 18) (p. 471).

### *12.3 QUANTUM STATES OF LIGHT (p. 471)

En óptica cuántica también el campo eléctrico es aleatorio. Modo de onda plana monocromático en
volumen $V$, $\mathcal E(\mathbf r,t)=\mathrm{Re}\{\mathbf E(\mathbf r,t)\}$:

$$\mathbf E(\mathbf r,t)=A\exp(-j\mathbf k\cdot\mathbf r)\exp(j2\pi\nu t)\,\hat{\mathbf e}. \tag{12.3-1}$$

Energía clásica $\tfrac12\epsilon|A|^2V$ [de (12.1-3)]. Se define la variable compleja $\mathbf a$ tal que
$\tfrac12\epsilon|A|^2V=h\nu|\mathbf a|^2$ ($|\mathbf a|^2$ = energía en unidades de número de fotones):

$$\mathbf E(\mathbf r,t)=\sqrt{\frac{2h\nu}{\epsilon V}}\;\mathbf a\exp(-j\mathbf k\cdot\mathbf r)\exp(j2\pi\nu t)\,\hat{\mathbf e}. \tag{12.3-2}$$

$\mathbf a\exp(j2\pi\nu t)$ es un fasor rotatorio cuya proyección real es el campo sinusoidal
(**Fig. 12.3-1, p. 472**). Sus partes real e imaginaria $\mathbf x=\mathrm{Re}\{\mathbf a\}$,
$\mathbf p=\mathrm{Im}\{\mathbf a\}$, $\mathbf a=\mathbf x+j\mathbf p$, son las **componentes en cuadratura** (desfasadas 90°);
determinan amplitud y fase. El fasor describe también un oscilador armónico ($\mathbf x\propto$ posición,
$\mathbf p\propto$ momento): modo clásico y oscilador clásico se comportan idénticamente; lo mismo ocurre en
la versión cuántica (p. 471).

#### Teoría cuántica del oscilador armónico (p. 471–473)

Partícula de masa $m$, posición $x$, momento $p$, $V(x)=\tfrac12\kappa x^2$, energía $\tfrac12p^2/m+\tfrac12\kappa x^2$,
$\omega=\sqrt{\kappa/m}$; con $m=1$, energía $\tfrac12(p^2+\omega^2x^2)$. Ecuación de Schrödinger independiente del tiempo:

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}+V(x)\psi(x)=E\psi(x). \tag{12.3-3}$$

Energías discretas:

$$E_n=\left(n+\tfrac12\right)h\nu,\qquad n=0,1,2,\dots \tag{12.3-4}$$

(niveles separados por $h\nu=\hbar\omega$). Funciones propias Hermite–Gauss normalizadas:

$$\psi_n(x)=\frac{1}{\sqrt{2^nn!}}\left(\frac{\omega}{\pi\hbar}\right)^{1/4}\mathbb H_n\!\left[\sqrt{\frac{\omega}{\hbar}}\,x\right]\exp\!\left(-\frac{\omega x^2}{2\hbar}\right), \tag{12.3-5}$$

$\mathbb H_n$ = polinomio de Hermite de orden $n$ [(3.3-6)–(3.3-8), (3.3-11)]. Una $\psi(x)$ arbitraria se
expande como $\psi(x)=\sum_nc_n\psi_n(x)$ y entonces (p. 472):
- la probabilidad $p(n)$ de $n$ cuantos es $|c_n|^2$;
- la densidad de probabilidad de posición es $|\psi(x)|^2$;
- la densidad de probabilidad de momento es $|\phi(p)|^2$, con

$$\phi(p)=\frac{1}{\sqrt h}\int_{-\infty}^{\infty}\psi(x)\exp\!\left(j2\pi\frac phx\right)dx. \tag{12.3-6}$$

Por la relación de Fourier (Sec. A.2):

$$\frac{\sigma_x\sigma_p}{h}\ge\frac{1}{4\pi}\qquad\text{o}\qquad\sigma_x\sigma_p\ge\frac\hbar2, \tag{12.3-7}$$

la relación de incertidumbre posición–momento de Heisenberg (p. 473).

#### Analogía entre un modo óptico y un oscilador armónico (p. 473)

Energía del modo $h\nu|\mathbf a|^2=h\nu(\mathbf x^2+\mathbf p^2)$. Con las sustituciones

$$\mathbf x=\left(1/\sqrt{2\hbar\omega}\right)\omega x\qquad\text{y}\qquad\mathbf p=\left(1/\sqrt{2\hbar\omega}\right)p, \tag{12.3-8}$$

$h\nu(\mathbf x^2+\mathbf p^2)=\tfrac12(p^2+\omega^2x^2)$: analogía completa → la energía del modo cuántico se
cuantiza en $(n+\tfrac12)h\nu$ y $x,p$ del oscilador describen las cuadraturas $\mathbf x,\mathbf p$ del campo.

> **Recuadro "Properties" (p. 473):** Un modo EM de frecuencia $\nu$ se describe por una función de onda
> compleja $\psi(\mathbf x)$ que gobierna las incertidumbres de las cuadraturas $\mathbf x$ y $\mathbf p$ y la
> estadística del número de fotones.
> - $p(n)=|c_n|^2$ con $\psi(\mathbf x)=\sum_nc_n\psi_n(\mathbf x)$.
> - Las densidades de probabilidad de $\mathbf x$ y $\mathbf p$ son $|\psi(\mathbf x)|^2$ y $|\phi(\mathbf p)|^2$, con
> $$\phi(\mathbf p)=\frac{1}{\sqrt\pi}\int_{-\infty}^{\infty}\psi(\mathbf x)\exp(j2\mathbf p\mathbf x)\,d\mathbf x. \tag{12.3-9}$$
> (El libro dice que "se deriva de (12.3-9)" usando (12.3-8) y la normalización de $|\psi|^2$ y
> $|\phi|^2$; por el contexto debe leerse "de (12.3-6)": probable errata.)
> - Relación de incertidumbre entre los anchos rms de potencia de las cuadraturas:
> $$\boxed{\sigma_{\mathbf x}\sigma_{\mathbf p}\ge\tfrac14} \tag{12.3-10}$$
> (**incertidumbre de cuadratura**): no se pueden determinar ambas simultáneamente con precisión arbitraria.

#### 12.3A Coherent-State Light (p. 474)

El producto $\sigma_{\mathbf x}\sigma_{\mathbf p}$ alcanza su mínimo $\tfrac14$ cuando $\psi(\mathbf x)$ es gaussiana (Sec. A.2):

$$\psi(\mathbf x)\propto\exp\!\left[-(\mathbf x-\alpha_{\mathbf x})^2\right], \tag{12.3-11}$$
$$\phi(\mathbf p)\propto\exp\!\left[-(\mathbf p-\alpha_{\mathbf p})^2\right], \tag{12.3-12}$$

$\alpha_{\mathbf x},\alpha_{\mathbf p}$ = medias de $\mathbf x$ y $\mathbf p$;

$$\sigma_{\mathbf x}=\sigma_{\mathbf p}=\tfrac12. \tag{12.3-13}$$

Es el **estado coherente**. **Fig. 12.3-2 (p. 474):** círculo de incertidumbre de diámetro
$2\sigma_{\mathbf x}=2\sigma_{\mathbf p}=1$ en el plano $(\mathbf x,\mathbf p)$ girando a $\omega$, y la banda de
incertidumbre (ancho 1) de $\mathcal E(t)$. $|c_n|^2=\bar n^ne^{-\bar n}/n!$ con
$\bar n=\alpha_{\mathbf x}^2+\alpha_{\mathbf p}^2$ → $p(n)$ Poisson. En óptica cuántica la luz coherente *no* es
determinista. Con $\alpha_{\mathbf x}=\alpha_{\mathbf p}=0$: cero fotones, solo energía de punto cero $\tfrac12h\nu$:
**estado de vacío** (**Fig. 12.3-3, p. 475**: disco de incertidumbre centrado en el origen y $\mathcal E(t)$
con fase totalmente aleatoria dentro de una banda).

#### 12.3B Squeezed-State Light (p. 474–476)

- **Luz comprimida en cuadratura (p. 474–475).** $\sigma_{\mathbf x}\sigma_{\mathbf p}$ no baja de $\tfrac14$, pero una
  cuadratura puede comprimirse por debajo de $\tfrac12$ a costa de la otra: luz **quadrature squeezed**,
  claramente no clásica. Ej.: $\psi(\mathbf x)$ gaussiana de ancho $\sigma_{\mathbf x}=s/2$ ($s>1$) ↔ $\phi(\mathbf p)$ de
  ancho $\sigma_{\mathbf p}=1/2s$; el círculo de incertidumbre se vuelve elipse (**Fig. 12.3-4, p. 475**:
  $2\sigma_{\mathbf x}=1/s$, $2\sigma_{\mathbf p}=s$; $\mathcal E(t)$ con incertidumbre que alterna entre grande y
  pequeña cada cuarto de ciclo). Midiendo solo en los instantes de incertidumbre mínima (heterodinaje
  con un campo coherente de fase adecuada, Sec. 24.5) el ruido baja del nivel coherente. Útil en
  medidas de precisión; no robusta ante pérdidas.
- **Luz comprimida en número de fotones (p. 475–476).** Luz **photon-number-squeezed** o
  **sub-Poisson**: $\sigma_n^2<\bar n$. No clásica porque (12.2-28) no puede cumplirse. Aplicaciones en
  precisión; afectada por pérdidas. Se genera con un punto cuántico en una microcavidad (Ej. 17.4-3) o
  con luz de haces gemelos. Descripción esencial: modo en el estado propio $\psi(\mathbf x)=\psi_{n_0}(\mathbf x)$,
  **estado número**: $p(n)=|c_n|^2=1$ para $n=n_0$, $c_n=0$ si $n\ne n_0$; $\bar n=n_0$, varianza cero.
  $n_0=1$ = exactamente un fotón. **Fig. 12.3-5 (p. 476):** anillo de incertidumbre (cuadraturas,
  magnitud y fase inciertas; número de fotones exacto).
- **Luz de haces gemelos (p. 476).** Seleccionar intervalos de una fuente coherente observando los
  fotones falla porque observarlos los aniquila. Con óptica no lineal y **twin-beam light** sí se puede:
  en la **conversión paramétrica descendente espontánea** (SPDC) una fracción de los fotones incidentes
  sobre un cristal se divide en pares de fotones conservando energía y momento (Secs. 21.2C y 21.4C).
  Como cada haz recibe el mismo número de fotones, la distribución conjunta tiene un ancho comprimido
  bajo el valor clásico: luz **comprimida en número de dos modos**. Midiendo un haz (lo que aniquila sus
  fotones) se obtiene información para controlar el número de fotones (y otras propiedades) del haz
  gemelo superviviente.

### Reading List (p. 476–478)

Libros de óptica cuántica y mecánica cuántica: Fox (2006); Vogel & Welsch (2006); Klauder & Sudarshan
(1968/2006); Walls & Milburn (1995/2006); Vedral (2006); Feynman *QED* (1985/2006); Feynman Lectures
vol. 3 y 1; Sergienko ed. (2006); Planck *Columbia Lectures* (2005); Ficek & Swain (2005); Gerry &
Knight (2005); Paul (2004); Bachor & Ralph (2004); Carmichael (2003); Nielsen & Chuang (2002); Baierlein
(2001); Kim, Somani & Yamamoto (2001); Schleich (2001); Loudon 3.ª ed. (2000); Yamamoto, Tassone & Cao
(2000); Mead (2000); Meystre & Sargent (1999); Yamamoto & Imamoglu (1999); Feynman *Quantum
Electrodynamics* (1998); Peřinová, Lukš & Peřina (1998); Barnett & Radmore (1997); Scully & Zubairy
(1997); **Mandel & Wolf, *Optical Coherence and Quantum Optics* (1995)**; Peřina (1991); Louisell (1973/1990);
Pike & Walther (1988); Peřina (1985); Heitler (1954/1984); Goldin (1982); Haken (1981); Saleh,
*Photoelectron Statistics* (1978); Louisell (1964/1977); ter Haar (1967); DeWitt, Blandin &
Cohen-Tannoudji (1965).
Física estadística y térmica: Blundell & Blundell (2006); Plischke & Bergersen (2006); Kittel
(1958/2004); Reif (1998).
Artículos: Glauber (Nobel 2005); Jacques *et al.*, interferencia de un solo fotón (EPJD 35, 561, 2005);
J. Opt. B 6(3) 2004; Roychoudhuri & Roy, *The Nature of Light: What Is a Photon?* (2003); Regelman *et
al.* PRL 87, 257401 (2001); Agarwal ed. SPIE MS 103 (1995); Mandel & Wolf eds. SPIE MS 19 (1990); Teich &
Saleh, *Squeezed and Antibunched Light*, Physics Today 43(6), 26 (1990); Teich & Saleh, *Squeezed States
of Light*, Quantum Optics 1, 153 (1989); Teich & Saleh, *Photon Bunching and Antibunching*, Prog. Opt. 26,
1 (1988); JOSA B 4(10) 1987 (squeezed states); J. Mod. Opt. 34(6/7) 1987; JOSA A 3(10) 1986; Teich &
Saleh, sub-Poisson Franck–Hertz light at 253.7 nm, JOSA B 2, 275 (1985); Wolf (1979); Weinberg (1975);
Mandel & Wolf eds. Dover (1970); Mandel & Wolf, Rev. Mod. Phys. 37, 231 (1965); Mandel, Prog. Opt. 2 (1963).

---

## Tablas y datos numéricos útiles

Constantes (valores tal como los da el libro):
- $h=6.63\times10^{-34}$ J·s (p. 448); $\hbar=h/2\pi$.
- $k=1.38\times10^{-23}$ J/K (p. 453, 466).
- $1$ eV $=1.6\times10^{-19}$ J (p. 448).
- $kT$ a 300 K $=0.026$ eV $=26$ meV $\equiv208$ cm⁻¹ (p. 449, 466).

Conversiones (p. 448–449):
- $E\,(\mathrm{eV})=1.24/\lambda_o\,(\mu\mathrm m)$ (12.1-6).
- $\lambda_o=1\ \mu$m ↔ 300 THz ↔ 1.24 eV ↔ $1.99\times10^{-19}$ J ↔ $10^4$ cm⁻¹.
- 1 cm⁻¹ ↔ $1.24\times10^{-4}$ eV; 1 eV ↔ 8068.1 cm⁻¹.
- $\lambda_o=1$ cm (microondas) ↔ $1.24\times10^{-4}$ eV.
- $p=E/c=h/\lambda$ (12.1-10).
- 1 nW a 0.2 μm ↔ 1 fotón/ns; 1 nW a 1 μm ↔ 5 fotones/ns (p. 461–462).
- *(Cálculo propio para el proyecto: a $\lambda_o=1.55\ \mu$m, $h\nu=0.80$ eV $=1.28\times10^{-19}$ J;
  1 mW ↔ $7.8\times10^{15}$ fotones/s; 1 nW ↔ $7.8\times10^6$ fotones/s.)*

**Tabla 12.2-1 (p. 460).** Densidad media de flujo de fotones de fuentes comunes (fotones/s·cm²):

| Fuente | $\phi$ (fotones/s·cm²) |
|---|---|
| Luz de estrellas | $10^6$ |
| Luz de luna | $10^8$ |
| Crepúsculo | $10^{10}$ |
| Luz interior | $10^{12}$ |
| Luz solar | $10^{14}$ |
| Luz láser (He–Ne 10 mW, 633 nm, enfocado a 20 μm de diámetro) | $10^{22}$ |

Resumen de estadísticas de número de fotones (p. 465–471):

| Luz | $p(n)$ | $\sigma_n^2$ | SNR | Tras partición $\mathcal T$ |
|---|---|---|---|---|
| Coherente (láser ideal, estado coherente) | Poisson (12.2-12) | $\bar n$ | $\bar n$ | Poisson, SNR $=\mathcal T\bar n$ |
| Térmica monomodo (campo gaussiano) | Bose–Einstein (12.2-20) | $\bar n+\bar n^2$ | $\bar n/(\bar n+1)<1$ | B–E, SNR $=\mathcal T\bar n/(\mathcal T\bar n+1)$ |
| Parcialmente coherente (clásica) | Mandel (12.2-26) | $\bar n+\sigma_w^2$ | — | — |
| Estado número $n_0$ (sub-Poisson) | $\delta_{n,n_0}$ | 0 | ∞ | binomial; pierde su forma |
| $n$ fijo → transmitidos $m$ | binomial (12.2-30) | $(1-\mathcal T)\bar m$ | $\bar m/(1-\mathcal T)$ | — |

Incertidumbres (p. 453, 457, 473–475): $\sigma_x\sigma_{kx}\ge\tfrac12$; $\sigma_x\sigma_\theta\ge\lambda/4\pi$;
$\sigma_\nu\sigma_t\ge1/4\pi$; $\sigma_\omega\sigma_t\ge\tfrac12$; $\sigma_E\sigma_t\ge\hbar/2$; $\sigma_z\sigma_p\ge\hbar/2$;
$\sigma_{\mathbf x}\sigma_{\mathbf p}\ge\tfrac14$ (coherente: $\sigma_{\mathbf x}=\sigma_{\mathbf p}=\tfrac12$; comprimida:
$\sigma_{\mathbf x}=s/2$, $\sigma_{\mathbf p}=1/2s$).

---

## Problemas al final del capítulo (p. 478–481)

La numeración continúa la de los ejercicios del texto (12.1-1 a 12.1-4 y 12.2-1 son ejercicios).
Los marcados con * son avanzados.

- **12.1-5 Photon Energy.** (a) Voltaje para que un electrón desde el reposo adquiera la energía de un
  fotón de $\lambda_o=0.87\ \mu$m. (b) Un fotón de 1.06 μm se combina con uno de 10.6 μm en un fotón cuya
  energía es la suma; hallar su longitud de onda (interacciones de este tipo: cap. 21).
- **12.1-6 Position of a Single Photon at a Screen.** Haz monocromático sobre pantalla infinita en
  $z=0$ con $I(\rho)=I_0\exp(-\rho/\rho_0)$, $\rho=\sqrt{x^2+y^2}$, intensidad tan baja que llega un solo
  fotón. (a) Probabilidad de que caiga dentro de un radio $\rho_0$. (b) Con exactamente $10^6$ fotones,
  cuántos caen en promedio dentro de ese círculo.
- **12.1-7 Momentum of a Free Photon.** Comparar el momento total de los fotones de un pulso láser de
  10 J con el de una masa de 1 g a 1 cm/s y con el de un electrón a $c_o/10$.
- ***12.1-8 Momentum of a Photon in a Gaussian Beam.** (a) Probabilidad de que el vector momento de
  un fotón de un haz gaussiano de cintura $W_0$ esté dentro del ángulo de divergencia $\theta_0$
  (Sec. 3.1). (b) ¿Vale $p=E/c_o$ en este caso?
- **12.1-9 Levitation by Light Pressure.** Átomo de hidrógeno aislado, $m=1.66\times10^{-27}$ kg.
  (a) Fuerza gravitacional ($g=9.8$ m/s²). (b) Haz láser vertical de fotones de 1 eV cuyo momento se
  transfiere totalmente; fuerza media por un fotón por segundo. (c) Fotones/s y potencia óptica para
  que no caiga (vacío). (d) Fotones/s si el átomo fuera perfectamente reflectante.
- ***12.1-10 Single Photon in a Fabry–Perot Resonator.** Resonador de $d=1$ cm, $n=1.5$, espejos
  perfectos, un fotón en el modo $\sin(10^5\pi x/d)$. (a) Longitud de onda y energía (eV) del fotón.
  (b) Estimar la incertidumbre de posición y momento (magnitud y dirección); comparar con $\sigma_x\sigma_p=\hbar/2$.
- **12.1-11 Single-Photon Beating (Time Interference).** Detector iluminado por la superposición de
  dos ondas planas monocromáticas $U_1(t)=\sqrt{I_1}\exp(j2\pi\nu_1t)$ y $U_2(t)=\sqrt{I_2}\exp(j2\pi\nu_2t)$;
  $I(t)=I_1+I_2+2\sqrt{I_1I_2}\cos[2\pi(\nu_2-\nu_1)t]$ (Sec. 2.6B); $I_1=I_2$, un solo fotón
  policromático en $T=1/|\nu_2-\nu_1|$. (a) Graficar $p(t)$ para $0\le t\le1/|\nu_2-\nu_1|$; ¿en qué instante
  es cero? (b) Descubrir de cuál onda proviene el fotón requiere medir la energía con precisión
  $\sigma_E<h|\nu_2-\nu_1|$; usar la incertidumbre tiempo–energía para mostrar que el tiempo necesario es
  del orden del periodo de batido (la medición borra la interferencia).
- **12.1-12 Photon Momentum Exchange at a Beamsplitter.** Fotón en onda plana sobre un divisor sin
  pérdidas: momento antes; valores posibles y probabilidades del momento después.
- **12.2-2 Photon Flux.** Mostrar que la potencia de un haz monocromático con un promedio de un fotón
  por ciclo óptico es inversamente proporcional a $\lambda^2$.
- **12.2-3 The Poisson Distribution.** Verificar que (12.2-12) está normalizada, tiene media $\bar n$
  y varianza $\sigma_n^2=\bar n$.
- **12.2-4 Photon Statistics of a Coherent Gaussian Beam.** He–Ne monomodo de 100 pW a 633 nm en
  TEM$_{0,0}$. (a) Número medio de fotones que cruzan un círculo de radio $W_0$ en $T=100$ ns.
  (b) Valor rms del número de cuentas. (c) Probabilidad de no contar fotones.
- **12.2-5 The Bose–Einstein Distribution.** (a) Verificar normalización, media $\bar n$ y varianza
  $\bar n+\bar n^2$ de (12.2-20). (b) Con $\Phi=1$ fotón/ns y estadística B–E, probabilidad de cero
  fotones en 20 ns.
- ***12.2-6 The Negative-Binomial Distribution.** La suma de $\mathcal M$ variables geométricas (B–E)
  idénticas sigue $p(n)=\binom{n+\mathcal M-1}{n}\dfrac{(\bar n/\mathcal M)^n}{(1+\bar n/\mathcal M)^{n+\mathcal M}}$.
  Verificar que se reduce a B–E para $\mathcal M=1$ y a Poisson para $\mathcal M\to\infty$.
- ***12.2-7 Photon Statistics for Multimode Thermal Light in a Cavity.** $\mathcal M$ modos térmicos
  de frecuencias cercanas, cada uno B–E con media $1/[\exp(h\nu/kT)-1]$. Mostrar que la varianza del
  total es $\sigma_n^2=\bar n+\bar n^2/\mathcal M$ (menos varianza que monomodo: promediado entre modos).
- ***12.2-8 Photon Statistics for a Beam of Multimode Thermal Light.** $\mathcal M$ modos con tasa
  integrada exponencial → $w$ con densidad gamma
  $p(w)=\dfrac{1}{(\mathcal M-1)!}\left(\dfrac{\mathcal M}{\langle w\rangle}\right)^{\mathcal M}w^{\mathcal M-1}\exp\!\left(-\dfrac{\mathcal Mw}{\langle w\rangle}\right)$, $w\ge0$.
  Con la fórmula de Mandel mostrar que $p(n)$ es la binomial negativa del Prob. 12.2-6.
- ***12.2-9 Mean and Variance of the Doubly Stochastic Poisson Distribution.** Probar (12.2-27) y (12.2-28).
- ***12.2-10 Random Partitioning of Coherent Light.** (a) Con (12.2-33) mostrar que la luz coherente
  particionada sigue siendo Poisson. (b) Media reflejada $(1-\mathcal T)\bar n$. (c) Probar (12.2-34).
- **12.2-11 Random Partitioning of Single-Mode Thermal Light.** (a) Con (12.2-33) mostrar que la luz
  térmica monomodo particionada sigue siendo B–E. (b) Media reflejada $(1-\mathcal T)\bar n$. (c) Probar (12.2-35).
- ***12.2-12 Exponential Decay of Mean Photon Number in an Absorber.** Material absorbente de
  espesor $d$ y coeficiente $\alpha$ (cm⁻¹), $\bar n_0$ fotones entrantes. (a) Ecuación diferencial para
  $\bar n(x)$, $0\le x\le d$. (b) Resolverla y explicar por qué coincide con la ley exponencial de la
  óptica EM (Sec. 5.5A). (c) $p(n)$ a profundidad $x$ con luz coherente incidente. (d) Probabilidad de
  que un fotón sobreviva al absorbente.
- ***12.3-1 Statistics of the Binomial Photon-Number Distribution.**
  $p(n)=\dfrac{M!}{(M-n)!n!}p^n(1-p)^{M-n}$ (estadística de ciertas fuentes sub-Poisson). (a) Mecanismo
  para convertir luz de estado número en luz binomial. (b) Normalización. (c) Media y varianza en
  función de $p$ y $M$. (d) SNR en función de $\bar n$ y $p$; límites $p\to0$ y $p\to1$ y a qué luz corresponden.
- ***12.3-2 Noisiness of a Hypothetical Photon Source.** Fuente con $p(n)=1/(2\bar n+1)$ para
  $0\le n\le2\bar n$, 0 en otro caso. (a) Normalización, media $\bar n$, varianza y SNR; comparar con B–E
  y Poisson de igual media. (b) ¿Más silenciosa o más ruidosa que un láser monomodo ideal para
  $\bar n<2$, $=2$, $>2$? (c) Factor por el que su SNR supera a la térmica monomodo.
  Fórmulas útiles: $\sum_1^j i=j(j+1)/2$, $\sum_1^j i^2=j(j+1)(2j+1)/6$.

---

## Relación con Óptica No Lineal

**Para el curso (temas del programa):**

- **Ondas EM y modos.** La expansión modal (12.1-1)/(12.1-21) y la energía por modo (12.1-3)
  (p. 446–447) son el punto de partida para cuantizar el campo; en ONL la polarización no lineal
  acopla modos de distinta frecuencia y el balance de energía entre ellos se lee directamente en
  fotones: cada fotón aniquilado/creado en un modo cambia su energía en $h\nu_{\mathbf q}$ (p. 448).
- **Conservación de energía y momento en SHG/SFG/DFG (χ⁽²⁾) y FWM (χ⁽³⁾).** Con $E=\hbar\omega$ (12.1-4) y
  $\mathbf p=\hbar\mathbf k$ (12.1-9), p. 448 y 452: la generación de suma de frecuencias es la fusión de dos
  fotones, $\hbar\omega_3=\hbar\omega_1+\hbar\omega_2$, y el ajuste de fase $\Delta\mathbf k=\mathbf k_3-\mathbf k_1-\mathbf k_2=0$ es
  la conservación del momento fotónico; SHG es el caso $\omega_1=\omega_2$; en FWM
  $\hbar\omega_1+\hbar\omega_2=\hbar\omega_3+\hbar\omega_4$ y $\mathbf k_1+\mathbf k_2=\mathbf k_3+\mathbf k_4$. El Prob. 12.1-5(b)
  (p. 479) es exactamente SFG: 1.06 μm + 10.6 μm → *(cálculo propio)* $\lambda_3=(1/1.06+1/10.6)^{-1}=0.964\ \mu$m.
  La relación (12.1-11) (p. 453) recuerda que en haces enfocados el momento del fotón tiene una
  distribución $|A(\mathbf k)|^2$: base fotónica del ajuste de fase no colineal y de la tolerancia angular.
- **Raman.** Misma contabilidad: $\hbar\omega_p=\hbar\omega_s+\hbar\Omega$ (fonón) para Stokes; la
  "fluorescencia" Raman espontánea es un proceso de creación de fotones en modos vacíos cuya tasa
  depende de la energía de punto cero (12.1-5) del modo Stokes (p. 448: papel del punto cero en la
  emisión espontánea, cap. 13).
- **SPDC y fotones gemelos (p. 476).** El libro remite a las Secs. 21.2C y 21.4C: un fotón de bombeo
  se divide en señal + ocioso conservando energía y momento; la estadística conjunta es sub-Poisson
  (luz comprimida en número de dos modos). Es la versión cuántica de la amplificación paramétrica (DFG).
- **Luz comprimida (Sec. 12.3B, p. 474–476).** Los estados comprimidos en cuadratura se generan con
  procesos χ⁽²⁾ (amplificación paramétrica degenerada) y χ⁽³⁾ (efecto Kerr en fibras); la figura de
  mérito del libro es $\sigma_{\mathbf x}=s/2$, $\sigma_{\mathbf p}=1/2s$ manteniendo $\sigma_{\mathbf x}\sigma_{\mathbf p}=\tfrac14$
  (12.3-10). Nota del libro: no es robusta ante pérdidas (relevante si se quisiera medir ruido
  cuántico en guías con pérdidas de propagación).
- **Índice dependiente de la intensidad, SPM/XPM.** Aquí la conversión $\phi=I/h\nu$ (12.2-1) permite
  traducir la intensidad del curso ($n=n_0+n_2I$) a flujo de fotones; la relación de incertidumbre
  $\sigma_{\mathbf x}\sigma_{\mathbf p}\ge\tfrac14$ (p. 473) y las cuadraturas $\mathbf a=\mathbf x+j\mathbf p$ (p. 471) son el
  lenguaje con que se describe el "Kerr squeezing" por SPM.
- **Pulsos en medios dispersivos, GVD, solitones.** La reciprocidad duración–ancho de banda
  $\sigma_\nu\sigma_t\ge1/4\pi$ y $\sigma_E\sigma_t\ge\hbar/2$ (p. 456–457, (12.1-16)) es la misma que limita un
  pulso al transformado (*transform-limited*); el Ejercicio 12.1-4 (paquete gaussiano $\exp(-t^2/4\tau^2)$,
  p. 457) es el pulso gaussiano de referencia de los capítulos de propagación. Un pulso con chirp
  (por GVD o SPM) excede el producto mínimo.
- **Polarización y cristales.** La interpretación del vector de Jones como amplitudes de probabilidad
  (p. 449–451, Ej. 12.1-1) y el espín $\pm\hbar$ (12.1-12) dan la lectura fotónica de polarizadores y
  láminas retardadoras; útil al pensar en la selección de polarizaciones tipo I/II en ajuste de fase.
- **Absorción.** Prob. 12.2-12 (p. 481): la ley de Beer $\bar n(x)=\bar n_0e^{-\alpha x}$ como selección
  aleatoria de fotones; la luz coherente sigue siendo Poisson tras absorber (p. 470), con media reducida.
- **Ruido y detección.** SNR $=\bar n$ para Poisson (12.2-17) es el límite de ruido de disparo (shot
  noise); la partición y la detección con eficiencia $\eta$ obedecen (12.2-33)–(12.2-35) (p. 470–471).

**Para el proyecto final (anillos add-drop en Si₃N₄, dispersión de guías, supercontinuo, sensado de índice):**

- **Resonancias del anillo como modos WGM (p. 454).** El libro da la condición $2\pi a=q\lambda$ y el
  momento angular $L=q\hbar$ por fotón en un modo de galería de susurros; para el anillo
  $2\pi R\,n_{\rm eff}=q\lambda_o$ (misma condición con $\lambda=\lambda_o/n_{\rm eff}$). El número de modo azimutal
  $q$ (≈ $m$ en la notación de resonadores) es un número cuántico de momento angular: cada resonancia
  del add-drop corresponde a un valor de $q$, y el FSR es el cambio de $\lambda$ al pasar de $q$ a $q+1$.
- **Sensado de índice y límite de detección.** El desplazamiento de resonancia se mide por un cambio
  de potencia transmitida; la Tabla 12.2-1 y (12.2-3) dicen cuántos fotones hay por segundo
  (*cálculo propio*: 1 mW a 1550 nm ↔ $7.8\times10^{15}$ fotones/s). Con detección limitada por disparo,
  SNR $=\bar n=\Phi T$ (12.2-17): el ruido relativo cae como $1/\sqrt{\bar n}$, lo que fija el mínimo
  $\Delta n$ detectable para un tiempo de integración $T$ y una pendiente $dP/d\lambda$ dada. Si la fuente
  es térmica/ASE, SNR $<1$ (12.2-23): hay que usar láser (Poisson). Las pérdidas del anillo y el
  acoplamiento son particiones aleatorias (12.2-33): no cambian la forma Poisson, solo la media.
- **Supercontinuo y pulsos.** La relación $\sigma_\nu\sigma_t\ge1/4\pi$ (p. 456) y el paquete gaussiano del
  Ej. 12.1-4 (p. 457) son la referencia para el pulso de bombeo; la energía por pulso $E=PT$ se
  convierte en fotones por pulso con $\bar n=E/h\bar\nu$ (12.2-6), útil para estimar cuántos fotones se
  redistribuyen espectralmente (FWM/SPM) en la guía de Si₃N₄. Las densidades espectrales
  $\Phi_\nu=P_\nu/h\nu$ (p. 461) son la forma natural de reportar un espectro de supercontinuo en
  fotones/s·Hz.
- **Dispersión de guías.** Entra indirectamente: el ajuste de fase de FWM en la guía (conservación
  de $\hbar\mathbf k$, p. 452) depende de $\beta(\omega)$; la conservación de energía fija las frecuencias
  señal/ociosa alrededor del bombeo.
- **Páginas a citar en el informe:** fotón y energía $h\nu$, p. 448 (12.1-4); momento $\hbar\mathbf k$,
  p. 452 (12.1-9); WGM y momento angular, p. 454; incertidumbre tiempo–energía, p. 457 (12.1-16);
  flujo de fotones, p. 460 (12.2-1), (12.2-3); Poisson y SNR, p. 463–465 (12.2-12), (12.2-15), (12.2-17);
  Bose–Einstein, p. 466–467 (12.2-20)–(12.2-23); partición, p. 470 (12.2-33); estados coherente y
  comprimido, p. 474–475; haces gemelos/SPDC, p. 476.
