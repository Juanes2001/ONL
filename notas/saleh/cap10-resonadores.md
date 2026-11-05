# Capítulo 10 — Resonator Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 365–402 (PDF 387–424). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 10.
Notación del libro: dependencia temporal $e^{j\omega t}$ con $j=\sqrt{-1}$; función de onda real
$u(\mathbf r,t)=\mathrm{Re}\{U(\mathbf r)\exp(j2\pi\nu t)\}$; $c=c_o/n$ es la velocidad de la luz
**en el medio** entre los espejos y las $\lambda_q$ son longitudes de onda **dentro del medio**
(p. 369). Las ecuaciones enmarcadas en recuadro por el libro se marcan aquí con **[recuadro]**.

---

## Resumen del capítulo

Un resonador óptico es el análogo óptico de un circuito resonante electrónico: confina y almacena
luz a frecuencias de resonancia fijadas por su configuración, y puede verse como un sistema de
transmisión con realimentación (p. 366). El capítulo construye la teoría en cuatro etapas:
(10.1) el resonador Fabry–Perot de espejos planos, del que salen los conceptos de modo,
frecuencias de resonancia $\nu_q = q\,c/2d$, espaciado $\nu_F = c/2d$, densidad de modos,
finura $\mathcal F$, ancho espectral $\delta\nu\approx\nu_F/\mathcal F$, coeficiente de pérdida
$\alpha_r$, tiempo de vida del fotón $\tau_p = 1/c\alpha_r$ y factor de calidad
$Q = \nu_0/\delta\nu = 2\pi\nu_0\tau_p$; (10.2) el resonador de espejos esféricos, analizado con
óptica de rayos (condición de confinamiento $0\le g_1g_2\le 1$) y con óptica de haces (los haces
gaussianos y Hermite–gaussianos son sus modos; las frecuencias se desplazan por la fase de Gouy
$\Delta\zeta/\pi$), más la pérdida por difracción en espejos finitos (número de Fresnel);
(10.3) resonadores rectangulares 2D y 3D, resonadores circulares y modos de galería de
susurros (whispering-gallery), y la densidad de modos $M(\nu)=8\pi\nu^2/c^3$ de Rayleigh–Jeans;
(10.4) microresonadores (caja rectangular, micropilar, microdisco, microtoroide, microesfera,
cristal fotónico) caracterizados por el volumen modal $V$ y el factor $Q$ (tabla 10.4-1). Los
parámetros clave de todo resonador son $V$ (confinamiento espacial) y $Q$ (confinamiento
temporal) (p. 366).

---

## Secciones

### Introducción (p. 365–367)

- **Definición** (p. 366): el resonador óptico confina y almacena luz a frecuencias de resonancia
  determinadas por su configuración; es un sistema de transmisión óptica con realimentación
  (la luz circula o se refleja repetidamente). Configuraciones (Fig. 10.0-1): Fabry–Perot de
  espejos planos, espejos esféricos, anillo de espejos, cavidad rectangular, anillo de fibra,
  anillo de óptica integrada, microdisco, microtoroide, microesfera, micropilar (con DBR),
  cristal fotónico con defecto.
- **Resonadores dieléctricos** (p. 366): usan reflexión total interna en la frontera entre dos
  dieléctricos de bajas pérdidas en lugar de espejos; los rayos rozan el borde interior con ángulo
  de incidencia siempre mayor que el crítico. En microdiscos, microtoroides y microesferas la luz
  circula reflejándose con incidencia casi rasante: **modos de galería de susurros**
  (whispering-gallery modes). Los **reflectores de Bragg distribuidos (DBR)** reemplazan espejos
  (micropilar). Cristales fotónicos 2D con un defecto hacen microcavidades.
- **Dos parámetros clave** (p. 366): **volumen modal $V$** (volumen ocupado por el modo confinado)
  y **factor de calidad $Q$** (proporcional al tiempo de almacenamiento en unidades de periodo
  óptico). Representan el confinamiento espacial y temporal, respectivamente.
- Usos (p. 367): filtros ópticos y analizadores de espectro (cap. 7) por su selectividad en
  frecuencia; sobre todo, el "contenedor" del láser (caps. 15 y 17): determina frecuencia y
  distribución espacial del haz; al almacenar energía permite generar pulsos.
- *This Chapter* (p. 367): herramientas usadas — óptica de rayos (cap. 1), óptica ondulatoria
  (cap. 2), óptica de haces (cap. 3), óptica de Fourier (cap. 4), óptica de cristales fotónicos
  (cap. 7), óptica de ondas guiadas (cap. 8: el resonador es una guía de ondas con reflectores
  en ambos extremos).

---

### 10.1 Planar-Mirror Resonators (p. 367)

#### 10.1A Resonator Modes (p. 367)

Dos espejos planos paralelos altamente reflectantes separados una distancia $d$: **etalón de
Fabry–Perot** (Fig. 10.1-1). Primero el caso idealizado sin pérdidas.

**Modos como ondas estacionarias (p. 368).** Onda monocromática de frecuencia $\nu$:
$$u(\mathbf r,t)=\mathrm{Re}\{U(\mathbf r)\exp(j2\pi\nu t)\}\qquad(10.1\text{-}1)$$
$U$ satisface Helmholtz, $\nabla^2U+k^2U=0$, $k=2\pi\nu/c$. Para el resonador plano sin pérdidas,
las componentes transversales del campo se anulan en los espejos: $U=0$ en $z=0$ y $z=d$. La onda
estacionaria $U=A\sin kz$ cumple esto si $kd=q\pi$:
$$k_q = q\frac{\pi}{d},\qquad q=1,2,\dots\qquad(10.1\text{-}2)$$
$$U(\mathbf r)=A_q\sin k_q z\qquad(10.1\text{-}3)$$
$q$ negativos no son modos independientes ($\sin k_{-q}z=-\sin k_qz$); $q=0$ no lleva energía.
El entero positivo $q$ es el **número de modo**. Una onda arbitraria dentro del resonador es
superposición de modos:
$$U(\mathbf r)=\sum_q A_q\sin k_q z\qquad(10.1\text{-}4)$$
Frecuencias de resonancia:
$$\nu_q = q\frac{c}{2d},\qquad q=1,2,\dots\qquad(10.1\text{-}5)$$
**[recuadro] Espaciado de frecuencias (Frequency Spacing of Resonator Modes):**
$$\nu_F=\frac{c}{2d}\qquad(10.1\text{-}6)$$
Longitudes de onda de resonancia $\lambda_q=c/\nu_q=2d/q$; el viaje de ida y vuelta es un número
entero de longitudes de onda:
$$2d=q\lambda_q,\qquad q=1,2,\dots\qquad(10.1\text{-}7)$$
Recordar: $c=c_o/n$ y $\lambda_q$ son dentro del medio (p. 369).

- Fig. 10.1-2 (p. 369): amplitud compleja e intensidad de un modo ideal; con 14 semilongitudes
  de onda en $d$, $q=d/(\lambda/2)=14$.
- Fig. 10.1-3 (p. 369): **ejemplos numéricos.** (a) Resonador de $d=30$ cm en aire:
  $\nu_F=500$ MHz. (b) Resonador de $d=3\ \mu$m: $\nu_F=50$ THz, el primer modo tiene
  $\lambda=6\ \mu$m y solo hay dos modos en la banda 700–900 nm (que ocupa 95 THz).

**Modos como ondas viajeras (p. 369–370).** Un modo es una onda que se reproduce tras un viaje
de ida y vuelta (round trip). Fase acumulada en un round trip (distancia $2d$):
$\varphi=k2d=4\pi\nu d/c$, que debe ser múltiplo de $2\pi$:
$$\varphi=k2d=q2\pi,\qquad q=1,2,\dots\qquad(10.1\text{-}8)$$
Un desfase adicional de $2\pi$ por las reflexiones no altera el resultado (§6.2). Es una condición
de **realimentación positiva** (Fig. 10.1-4b: la salida se realimenta *en fase* con la entrada).
Demostración por fasores (p. 370): onda inicial $U_0$ en el punto $P$, tras un round trip $U_1$,
luego $U_2$, …, todas de igual magnitud (sin pérdidas):
$$U=U_0+U_1+U_2+\cdots\qquad(10.1\text{-}9)$$
La suma infinita de fasores infinitesimales es infinitesimal salvo que estén alineados
($\varphi=q2\pi$); solo entonces una onda inicial infinitesimal acumula potencia finita
(Fig. 10.1-4c).

**Resonadores de onda viajera (p. 370).** El modo viaja en una dirección por un camino cerrado
sin invertir sentido: **resonador en anillo** (ring) y **bow-tie** (Fig. 10.1-5). Las frecuencias
se obtienen igualando la fase de round trip a $2\pi$. Los modos horario y antihorario de igual
frecuencia son **degenerados**.

> **EJERCICIO 10.1-1** (p. 370–371) *Resonance Frequencies of a Traveling-Wave Resonator.*
> Deducir $\nu_q$ y $\nu_F$ para el anillo de tres espejos (lados $d$) y el bow-tie de cuatro
> espejos de la Fig. 10.1-5, suponiendo que cada reflexión introduce desfase $\pi$. (No resuelto
> en el texto. Guía: para el anillo, perímetro $3d$ → $\nu_F=c/3d$, como confirma la p. 391;
> con tres reflexiones de $\pi$ el desfase total es $3\pi$, que desplaza las resonancias medio
> $\nu_F$.)

**Densidad de modos (p. 371).** Número de modos por unidad de frecuencia $=1/\nu_F=2d/c$ en cada
una de las dos polarizaciones ortogonales. Por unidad de longitud y de frecuencia:
**[recuadro] Density of Modes (1D Resonator):**
$$M(\nu)=\frac{4}{c}\qquad(10.1\text{-}10)$$
El número de modos de un resonador de longitud $d$ en un intervalo $\Delta\nu$ es
$(4/c)d\,\Delta\nu$ (grados de libertad de la onda).

**Pérdidas y ancho espectral de resonancia (p. 371–373).** Fase por round trip:
$$\varphi=2kd=4\pi\nu d/c\qquad(10.1\text{-}11)$$
Con pérdidas, fasores sucesivos se relacionan por el factor complejo de atenuación de amplitud
por round trip $h=|\mathsf r|e^{-j\varphi}$ (pérdidas de los dos espejos + absorción en el medio);
el factor de atenuación de intensidad por round trip es $|\mathsf r|^2<1$. Entonces
$U=U_0(1+h+h^2+\cdots)=U_0/(1-h)$ (realimentación de la Fig. 10.1-4b). Intensidad:
$$I=|U|^2=\frac{|U_0|^2}{|1-|\mathsf r|e^{-j\varphi}|^2}=\frac{I_0}{1+|\mathsf r|^2-2|\mathsf r|\cos\varphi}\qquad(10.1\text{-}12)$$
$$I=\frac{I_{\max}}{1+(2\mathcal F/\pi)^2\sin^2(\varphi/2)},\qquad I_{\max}=\frac{I_0}{(1-|\mathsf r|)^2}\qquad(10.1\text{-}13)$$
con $I_0=|U_0|^2$ la intensidad de la onda inicial y
**[recuadro] finura (finesse):**
$$\mathcal F=\frac{\pi\sqrt{|\mathsf r|}}{1-|\mathsf r|}\qquad(10.1\text{-}14)$$
(p. 372: es el mismo tratamiento de §2.5B con $h=|h|e^{+j\varphi}$; el signo de la fase es
superficial. (10.1-13) es idéntica a (2.5-18), Fig. 2.5-9b. Para $\mathcal F$ grande, picos
agudos en $\varphi=q2\pi$ con FWHM $\Delta\varphi\approx2\pi/\mathcal F$, cf. (2.5-20).)
En función de la frecuencia, con $\varphi=4\pi\nu d/c$:
**[recuadro]**
$$I=\frac{I_{\max}}{1+(2\mathcal F/\pi)^2\sin^2(\pi\nu/\nu_F)},\qquad I_{\max}=\frac{I_0}{(1-|\mathsf r|)^2}\qquad(10.1\text{-}15)$$
con $\nu_F=c/2d$ (Fig. 10.1-6). Máximo en las resonancias
$$\nu=\nu_q=q\nu_F,\qquad q=1,2,\dots\qquad(10.1\text{-}16)$$
Mínimo a medio camino entre resonancias:
$$I_{\min}=\frac{I_{\max}}{1+(2\mathcal F/\pi)^2}\qquad(10.1\text{-}17)$$
Para $\mathcal F\gg1$: respuesta muy picada, $I_{\min}/I_{\max}$ pequeño, y FWHM
$\delta\nu\approx\nu_F/\mathcal F$ (porque $\delta\nu=(c/4\pi d)\Delta\varphi$ y
$\Delta\varphi\approx2\pi/\mathcal F$) (p. 373). **Los dos parámetros espectrales del
Fabry–Perot:**
**[recuadro] Frequency Spacing:**
$$\nu_F=\frac{c}{2d}\qquad(10.1\text{-}18)$$
**[recuadro] Spectral Width:**
$$\delta\nu\approx\frac{\nu_F}{\mathcal F}\qquad(10.1\text{-}19)$$
Válida para $\mathcal F\gg1$. Al aumentar la pérdida, $\mathcal F$ baja y $\delta\nu$ sube.
- Fig. 10.1-6 (p. 373): (a) resonador sin pérdidas ($\mathcal F=\infty$) solo sostiene las
  $\nu_q$ exactas; (b) con pérdidas, picos de ancho $\nu_F/\mathcal F$ centrados en $\nu_q$,
  pero también sostiene otras frecuencias.

**Fuentes de pérdida (p. 373–375).** Dos principales:
1. Reflexión imperfecta en los espejos: (1) espejo parcialmente transmisor (a propósito, para
   extraer luz láser); (2) tamaño finito de los espejos → luz que se fuga alrededor; además
   trunca la distribución espacial → patrón de difracción en el espejo opuesto, que se trunca de
   nuevo. La pérdida por difracción se modela como una reducción efectiva de la reflectancia
   (§10.2E).
2. Absorción y dispersión (scattering) en el medio: factor de atenuación de potencia por round
   trip $\exp(-2\alpha_s d)$, $\alpha_s$ = coeficiente de pérdida del medio.

Con reflectancias $\mathcal R_1=|\mathsf r_1|^2$ y $\mathcal R_2=|\mathsf r_2|^2$ (pérdidas
"concentradas", lumped) y pérdidas distribuidas:
$$|\mathsf r|^2=\mathcal R_1\mathcal R_2\exp(-2\alpha_s d)\qquad(10.1\text{-}20)$$
$$|\mathsf r|^2=\exp(-2\alpha_r d)\qquad(10.1\text{-}21)$$
**[recuadro] Loss Coefficient** (coeficiente efectivo global de pérdida distribuida):
$$\alpha_r=\alpha_s+\frac{1}{2d}\ln\frac{1}{\mathcal R_1\mathcal R_2}\qquad(10.1\text{-}22)$$
$$\alpha_r=\alpha_s+\alpha_{m1}+\alpha_{m2}\qquad(10.1\text{-}23)$$
$$\alpha_{m1}=\frac{1}{2d}\ln\frac{1}{\mathcal R_1},\qquad\alpha_{m2}=\frac{1}{2d}\ln\frac{1}{\mathcal R_2}\qquad(10.1\text{-}24)$$
Para espejos de alta reflectancia, $\ln(1/\mathcal R_1)=-\ln[1-(1-\mathcal R_1)]\approx1-\mathcal R_1$
(Taylor $\ln(1-\Delta)\approx-\Delta$, $|\Delta|\ll1$):
$$\alpha_{m1}\approx\frac{1-\mathcal R_1}{2d}\qquad(10.1\text{-}25)$$
y si $\mathcal R_1=\mathcal R_2=\mathcal R\approx1$:
$$\alpha_r\approx\alpha_s+\frac{1-\mathcal R}{d}\qquad(10.1\text{-}26)$$
Finura en función de $\alpha_r$ (sustituyendo (10.1-21) en (10.1-14)):
$$\mathcal F=\frac{\pi\exp(-\alpha_r d/2)}{1-\exp(-\alpha_r d)}\qquad(10.1\text{-}27)$$
(Fig. 10.1-7, p. 375: $\mathcal F$ vs. factor de pérdida $\alpha_r d$ de 0.01 a 1; decrece
monótonamente, ~300 en 0.01, ~30 en 0.1.) Si $\alpha_r d\ll1$, $\exp(-\alpha_r d)\approx1-\alpha_r d$:
**[recuadro] Finesse and Loss Factor:**
$$\mathcal F\approx\frac{\pi}{\alpha_r d}\qquad(10.1\text{-}28)$$

> **EJERCICIO 10.1-2** (p. 375) *Resonator Modes and Spectral Width.* Espaciado y ancho espectral
> de los modos de un Fabry–Perot con $\mathcal R_1=0.98$, $\mathcal R_2=0.99$, $d=100$ cm,
> $n=1$, pérdidas del medio despreciables. ¿Es apropiada la aproximación (10.1-28)?
> (No resuelto en el texto. Guía: $\nu_F=c_o/2d=150$ MHz; $\alpha_r d=\tfrac12\ln(1/0.9702)
> \approx0.0151\ll1$ → $\mathcal F\approx\pi/0.0151\approx208$; $\delta\nu\approx0.72$ MHz.
> La aproximación es apropiada porque $\alpha_r d\ll1$.)

**Tiempo de vida del fotón (p. 375–376).** Relación ancho de línea–pérdida como incertidumbre
tiempo–frecuencia. Sustituyendo (10.1-18) y (10.1-28) en (10.1-19):
$$\delta\nu\approx\frac{c/2d}{\pi/\alpha_r d}=\frac{c\alpha_r}{2\pi}\qquad(10.1\text{-}29)$$
$c\alpha_r$ es la pérdida por unidad de tiempo. **Tiempo de vida del resonador o del fotón**:
$$\tau_p=\frac{1}{c\alpha_r}\qquad(10.1\text{-}30)$$
$$\delta\nu=\frac{1}{2\pi\tau_p}\qquad(10.1\text{-}31)$$
Producto $\delta\nu\cdot\tau_p=1/2\pi$. Un campo que decae como $\exp(-t/2\tau_p)$ (energía
$\exp(-t/\tau_p)$) tiene transformada de Fourier $\propto1/(1+j4\pi\nu\tau_p)$, de FWHM
$\delta\nu=1/2\pi\tau_p$ (p. 376).

**Factor de calidad $Q$ (p. 376).**
$$Q=2\pi\frac{\text{energía almacenada}}{\text{energía perdida por ciclo}}\qquad(10.1\text{-}32)$$
(Circuito RLC serie: $\nu_0\approx1/2\pi\sqrt{LC}$, $Q=2\pi\nu_0L/R$.) La energía se pierde a
razón $c\alpha_r$ por unidad de tiempo, es decir $c\alpha_r/\nu_0$ por ciclo:
$$Q=\frac{2\pi}{c\alpha_r/\nu_0}=\frac{2\pi\nu_0}{c\alpha_r}\qquad(10.1\text{-}33)$$
$$Q=\frac{\nu_0}{\delta\nu}\qquad(10.1\text{-}34)$$
$$Q=2\pi\nu_0\tau_p\qquad(10.1\text{-}35)$$
$$Q=\frac{\nu_0}{\nu_F}\mathcal F\qquad(10.1\text{-}36)$$
Como $\nu_0\gg\nu_F$, $Q\gg\mathcal F$; el $Q$ óptico es mucho mayor que el de microondas.

**Summary (recuadro, p. 377):**
- Dos parámetros para las pérdidas: coeficiente de pérdida $\alpha_r$ (cm⁻¹) y tiempo de vida
  del fotón $\tau_p=1/c\alpha_r$ (s).
- Dos adimensionales de calidad, para longitud $d$ y frecuencia $\nu_0$: finura
  $\mathcal F=\pi/\alpha_r d$ y factor de calidad $Q=2\pi\nu_0\tau_p$.
- Dos frecuencias espectrales: espaciado $\nu_F=c/2d$, llamado **rango espectral libre (FSR)**,
  y ancho espectral $\delta\nu=\nu_F/\mathcal F$.

#### 10.1B Off-Axis Resonator Modes (p. 377)

Espejos planos paralelos infinitos también soportan modos oblicuos: onda plana a ángulo $\theta$
respecto al eje $z$ que rebota como onda guiada en $x$ (Fig. 10.1-8a; cf. §8.1). Condición de
frontera: $k_z=k\cos\theta$ múltiplo entero de $\pi/d$; no hay condición sobre $k_x$ (abierto en
$x$). $k\cos\theta=q\pi/d$ se escribe
$$\nu=q\,\nu_F\sec\theta,\qquad q=1,2,\dots\qquad(10.1\text{-}37)$$
con $\nu_F=c/2d$. Equivale a la condición de autoconsistencia de modos guiados en guías de
espejos planos (§8.1) y a (7.1-41) (transmitancia pico de onda oblicua por Fabry–Perot). A
frecuencia fija hay modos en ángulos discretos $\theta_q$ con $\cos\theta_q=q\nu_F/\nu$ (ángulos
de rebote); a ángulo fijo, $\nu_q=q\nu_F/\cos\theta$: a mayor inclinación, mayor espaciado
(Fig. 10.1-8b–d).

---

### 10.2 Spherical-Mirror Resonators (p. 378)

Motivación (p. 378): el resonador plano es muy sensible a desalineación (rayos no normales se
desplazan lateralmente y escapan, Fig. 10.1-1b). Los espejos esféricos confinan de forma más
estable. Dos espejos de radios $R_1$, $R_2$ separados $d$; eje óptico $z$ por los centros;
simetría circular. Convención de signos: **cóncavo $R<0$, convexo $R>0$**; el plano es
$R_1=R_2=\infty$ (Fig. 10.2-1).

#### 10.2A Ray Confinement (p. 378)

Solo rayos meridionales y paraxiales; óptica matricial de §1.4 (sistemas periódicos §1.4D).
Posición e inclinación tras $m$ round trips, $(y_m,\theta_m)$:
$$\begin{bmatrix}y_{m+1}\\\theta_{m+1}\end{bmatrix}=\begin{bmatrix}A&B\\C&D\end{bmatrix}\begin{bmatrix}y_m\\\theta_m\end{bmatrix}\qquad(10.2\text{-}1)$$
Matriz de round trip (Fig. 10.2-2; de derecha a izquierda: propagación $d$, reflexión en $R_2$,
propagación $d$, reflexión en $R_1$):
$$\begin{bmatrix}A&B\\C&D\end{bmatrix}=\begin{bmatrix}1&0\\\frac{2}{R_1}&1\end{bmatrix}\begin{bmatrix}1&d\\0&1\end{bmatrix}\begin{bmatrix}1&0\\\frac{2}{R_2}&1\end{bmatrix}\begin{bmatrix}1&d\\0&1\end{bmatrix}\qquad(10.2\text{-}2)$$
Solución de §1.4D: $y_m=y_{\max}F^m\sin(m\varphi+\varphi_0)$, $F^2=AD-BC$,
$\varphi=\cos^{-1}(b/F)$, $b=(A+D)/2$. Aquí $F=1$:
$$y_m=y_{\max}\sin(m\varphi+\varphi_0)\qquad(10.2\text{-}3)$$
$$\varphi=\cos^{-1}b,\qquad b=2\left(1+\frac{d}{R_1}\right)\left(1+\frac{d}{R_2}\right)-1\qquad(10.2\text{-}4)$$
Armónica y acotada si $\varphi$ real, i.e. $-1\le b\le1$:
$$0\le\left(1+\frac{d}{R_1}\right)\left(1+\frac{d}{R_2}\right)\le1\qquad(10.2\text{-}5)$$
Con los **parámetros $g$**, $g_1=1+d/R_1$, $g_2=1+d/R_2$:
**[recuadro] Confinement Condition:**
$$0\le g_1g_2\le1\qquad(10.2\text{-}6)$$
Resonador **estable** si se cumple; si no, $\varphi$ imaginaria, $y_m$ crece como seno
hiperbólico: **inestable**; en la frontera (igualdades): **condicionalmente estable** (p. 379).
- Fig. 10.2-3 (p. 380): **diagrama de estabilidad** $g_2$ vs $g_1$; región estable = primer y
  tercer cuadrante bajo la hipérbola $g_1g_2=1$. Puntos marcados: (a) plano
  ($R_1=R_2=\infty$, $g=1$); (b) confocal simétrico ($R_1=R_2=-d$, $g=0$); (c) concéntrico
  simétrico ($R_1=R_2=-d/2$, $g=-1$); (d) confocal/plano ($R_1=d$ [sic en el libro],
  $R_2=\infty$); (e) cóncavo/convexo ($R_1<0$, $R_2>0$). Los simétricos están sobre $g_2=g_1$.

**Resonadores simétricos** ($R_1=R_2=R$, $g_1=g_2=g$): condición $g^2\le1$ ⇒ $-1\le1+d/R\le1$:
**[recuadro] Confinement Condition (Symmetric Resonator):**
$$0\le\frac{d}{(-R)}\le2\qquad(10.2\text{-}7)$$
Requiere espejos cóncavos ($R<0$) con radio mayor que la mitad de $d$. Casos: $d/(-R)=0,1,2$:
**plano, confocal, concéntrico**. En el confocal simétrico ($-R=d$, centro de curvatura de cada
espejo sobre el otro): $b=-1$, $\varphi=\pi$, $y_m=(-1)^my_0$: cada rayo paraxial se retraza tras
dos round trips, cualquiera que sea su posición e inclinación (Fig. 10.2-4, p. 381) — gran mejora
frente al plano, donde solo se retrazan los de inclinación cero.

**Summary (recuadro, p. 381):** condición de confinamiento paraxial $0\le g_1g_2\le1$,
$g_i=1+d/R_i$; para simétricos $0\le d/(-R)\le2$, que incluye plano, confocal y concéntrico.

> **EJERCICIO 10.2-1** (p. 381) *Maximum Resonator Length for Confined Rays.* Espejos cóncavos
> de radios 50 cm y 100 cm: longitud máxima que satisface el confinamiento. (No resuelto. Guía:
> $g_1g_2=(1-d/50)(1-d/100)\le1$ y $\ge0$; la región estable es $0\le d\le50$ cm o
> $100\le d\le150$ cm, de modo que $d_{\max}=150$ cm.)

#### 10.2B Gaussian Modes (p. 381)

La óptica de rayos no da frecuencias ni distribuciones de intensidad; hay que usar óptica
ondulatoria. Se muestra que los haces gaussianos (y Hermite–gaussianos) son soluciones de la
ecuación de Helmholtz paraxial con las condiciones de frontera de dos espejos esféricos.

**Haces gaussianos (p. 381–382, repaso del cap. 3).** Intensidad
$I=I_0[W_0/W(z)]^2\exp[-2(x^2+y^2)/W^2(z)]$,
$$W(z)=W_0\sqrt{1+\left(\frac{z}{z_0}\right)^2}\qquad(10.2\text{-}8)$$
$$R(z)=z\left[1+\left(\frac{z_0}{z}\right)^2\right]\qquad(10.2\text{-}9)$$
$$z_0=\frac{\pi W_0^2}{\lambda}\qquad(10.2\text{-}10)$$
$z_0$ = rango de Rayleigh (donde los frentes son más curvos); $W_0$ = cintura; $R$ pasa de $\infty$
en $z=0$ a un mínimo en $z=z_0$ y luego crece $\sim z$; $R>0$ para $z>0$ (diverge), $R<0$ para
$z<0$ (converge). Profundidad de foco $2z_0$ (Fig. 10.2-5).

**El haz gaussiano es modo del resonador esférico (p. 382–384).** Un haz gaussiano reflejado por
un espejo esférico se retraza si el radio de curvatura del frente coincide con el del espejo
(§3.2C). Si los radios de los frentes en dos planos separados $d$ igualan los de los espejos, el
haz existe autoconsistentemente; si además la fase se retraza (§10.2C), es modo. Geometría
(Fig. 10.2-6): centro del haz en $z=0$, espejos en $z_1$ y
$$z_2=z_1+d\qquad(10.2\text{-}11)$$
($z_1<0$: el centro del haz está a la derecha del espejo 1). Emparejando radios con cuidado de
signos (espejos cóncavos tienen $R<0$, pero $R(z)>0$ en $z>0$): $R_1=R(z_1)$ y $-R_2=R(z_2)$:
$$R_1=z_1+z_0^2/z_1\qquad(10.2\text{-}12)$$
$$-R_2=z_2+z_0^2/z_2\qquad(10.2\text{-}13)$$
Solución:
$$z_1=\frac{-d(R_2+d)}{R_2+R_1+2d},\qquad z_2=z_1+d\qquad(10.2\text{-}14)$$
$$z_0^2=\frac{-d(R_1+d)(R_2+d)(R_2+R_1+d)}{(R_2+R_1+2d)^2}\qquad(10.2\text{-}15)$$
(coinciden con (3.1-27) y (3.1-28) con $R_2\to-R_2$). Cintura $W_0=\sqrt{\lambda z_0/\pi}$ y
radios del haz en los espejos:
$$W_i=W_0\sqrt{1+\left(\frac{z_i}{z_0}\right)^2},\qquad i=1,2\qquad(10.2\text{-}16)$$
$z_0$ debe ser real ($z_0$ imaginario = onda paraboloidal no confinada, §3.1A). De (10.2-15),
$z_0^2>0$ equivale a
$$0\le\left(1+\frac{d}{R_1}\right)\left(1+\frac{d}{R_2}\right)\le1\qquad(10.2\text{-}17)$$
que es exactamente la condición de confinamiento de rayos (10.2-5) (p. 384).

> **EJERCICIO 10.2-2** (p. 384) *A Plano-Concave Resonator.* Con espejo 1 plano ($R_1=\infty$):
> condición de confinamiento, profundidad de foco, radio del haz en la cintura y en cada espejo
> en función de $d/|R_2|$. (No resuelto en el texto.)

**Modo gaussiano del resonador esférico simétrico (p. 384–385).** Con $R_1=R_2=-|R|$ en
(10.2-14): $z_1=-d/2$, $z_2=d/2$ (el centro del haz está en el centro del resonador) y
$$z_0=\frac{d}{2}\sqrt{\frac{2|R|}{d}-1}\qquad(10.2\text{-}18)$$
$$W_0^2=\frac{\lambda d}{2\pi}\sqrt{\frac{2|R|}{d}-1}\qquad(10.2\text{-}19)$$
$$W_1^2=W_2^2=\frac{\lambda d/\pi}{\sqrt{(d/|R|)\,[2-(d/|R|)]}}\qquad(10.2\text{-}20)$$
Condición de confinamiento:
$$0\le\frac{d}{|R|}\le2\qquad(10.2\text{-}21)$$
Fig. 10.2-7 (p. 385): $W_0$ y $W_1=W_2$ vs $d/|R|$. Para $d/|R|=0$ (plano): $W_0$, $W_1$
infinitos (onda plana). Al crecer $d/|R|$, $W_0$ baja hasta anularse en el concéntrico
($d/|R|=2$), donde $W_1=W_2=\infty$ (onda esférica). El ancho en los espejos es mínimo,
$W_1=W_2=\sqrt{\lambda d/\pi}$, en el **confocal simétrico** ($d/|R|=1$):
$$z_0=d/2\qquad(10.2\text{-}22)$$
$$W_0=\sqrt{\lambda d/2\pi}\qquad(10.2\text{-}23)$$
$$W_1=W_2=\sqrt2\,W_0\qquad(10.2\text{-}24)$$
Profundidad de foco $2z_0=d$ ("parámetro confocal"). **Ejemplo numérico (p. 385):** He–Ne
$\lambda_0=633$ nm, $d=100$ cm → $W_0=\sqrt{\lambda d/2\pi}=0.32$ mm; con $d=25$ cm,
$W_0=0.16$ mm (la cintura escala con $\sqrt d$). Fig. 10.2-8.

#### 10.2C Resonance Frequencies (p. 385)

Fase del haz gaussiano (3.1-23):
$$\varphi(\rho,z)=kz-\zeta(z)+\frac{k\rho^2}{2R(z)}\qquad(10.2\text{-}25)$$
$\zeta(z)=\tan^{-1}(z/z_0)$ (fase de Gouy), $\rho^2=x^2+y^2$. En el eje, el retardo relativo a
la onda plana es $\zeta(z)$. En los espejos:
$$\varphi(0,z_1)=kz_1-\zeta(z_1)\qquad(10.2\text{-}26)$$
$$\varphi(0,z_2)=kz_2-\zeta(z_2)\qquad(10.2\text{-}27)$$
Como los espejos coinciden con los frentes, todos los puntos de cada espejo comparten fase.
Cambio de fase de espejo 1 a 2:
$$\varphi(0,z_2)-\varphi(0,z_1)=k(z_2-z_1)-[\zeta(z_2)-\zeta(z_1)]=kd-\Delta\zeta\qquad(10.2\text{-}28)$$
$$\Delta\zeta=\zeta(z_2)-\zeta(z_1)\qquad(10.2\text{-}29)$$
Round trip: $2kd-2\Delta\zeta=2\pi q$, $q=0,\pm1,\pm2,\dots$ Con $k=2\pi\nu/c$, $\nu_F=c/2d$:
**[recuadro] Resonance Frequencies, Gaussian Modes:**
$$\nu_q=q\nu_F+\frac{\Delta\zeta}{\pi}\nu_F\qquad(10.2\text{-}30)$$
El espaciado sigue siendo $\nu_F=c/2d$, **independiente de la curvatura**; el segundo término
(que sí depende de las curvaturas) es un desplazamiento global de todas las resonancias (p. 386).

> **EJERCICIO 10.2-3** (p. 386) *Resonance Frequencies of a Confocal Resonator.* Confocal
> simétrico, $d=30$ cm, $n=1$: hallar $\nu_F$ y el desplazamiento $(\Delta\zeta/\pi)\nu_F$;
> listar las resonancias en la banda $5\times10^{14}\pm2\times10^9$ Hz. (No resuelto. Guía:
> $\nu_F=500$ MHz; confocal: $z_{1,2}=\mp d/2=\mp z_0$ ⇒ $\Delta\zeta=\pi/2$, desplazamiento
> $\nu_F/2=250$ MHz; resonancias en $(q+\tfrac12)\cdot500$ MHz dentro de la banda: 9 valores.)

#### 10.2D Hermite–Gaussian Modes (p. 386)

Los haces Hermite–gaussianos de orden $(l,m)$ (§3.3) tienen los mismos frentes de onda que el
gaussiano, así que un resonador que "ajusta" un gaussiano ajusta toda la familia: **todos los
Hermite–gaussianos son modos** del resonador esférico. Pero sus frecuencias dependen de $(l,m)$
por la fase de Gouy. Fase en el eje (3.3-10):
$$\varphi(0,z)=kz-(l+m+1)\zeta(z)\qquad(10.2\text{-}31)$$
$$2kd-2(l+m+1)\Delta\zeta=2\pi q,\qquad q=0,\pm1,\pm2,\dots\qquad(10.2\text{-}32)$$
**[recuadro] Resonance Frequencies, Hermite–Gaussian Modes:**
$$\nu_{l,m,q}=q\nu_F+(l+m+1)\frac{\Delta\zeta}{\pi}\nu_F\qquad(10.2\text{-}33)$$
Modos de distinto $q$ e igual $(l,m)$: misma distribución de intensidad (3.3-12) —
**modos longitudinales o axiales**. $(l,m)$ etiqueta la dependencia transversal — **modos
transversales** (Fig. 3.3-2). Propiedades (p. 387):
- Los modos longitudinales de un transversal dado están espaciados $\nu_F=c/2d$.
- Todos los transversales con igual $l+m$ tienen las mismas frecuencias.
- Dos transversales $(l,m)$, $(l',m')$ del mismo $q$ difieren en
$$\nu_{l,m,q}-\nu_{l',m',q}=[(l+m)-(l'+m')]\frac{\Delta\zeta}{\pi}\nu_F\qquad(10.2\text{-}34)$$

> **EJERCICIO 10.2-4** (p. 387) *Resonance Frequencies of the Symmetric Confocal Resonator.*
> Mostrar que en el confocal simétrico los modos longitudinales de distintos transversales
> coinciden o están desplazados $\nu_F/2$ (Fig. 10.2-9). (Guía: $\Delta\zeta=\pi/2$ ⇒
> desplazamiento $(l+m+1)\nu_F/2$: coincide si $l+m$ cambia en par, se desplaza $\nu_F/2$ si
> cambia en impar.)

#### *10.2E Finite Apertures and Diffraction Loss (p. 388)

Los haces gaussianos y H-G tienen extensión transversal infinita; los espejos son finitos, por lo
que parte de la potencia se fuga en cada paso. Estimación: haz gaussiano de ancho $W$ y espejo
circular de radio $a=2W$ → fracción $\exp(-2a^2/W^2)\approx3.35\times10^{-4}$ por paso escapa
(3.1-17); los modos de orden superior pierden más. Si $a<2W$ los haces gaussianos dejan de ser
buenas aproximaciones de los modos.

Método (p. 388): seguir una onda en round trips sucesivos hasta que converja a un modo. Si $U_1(x,y)$
es la amplitud justo a la derecha del espejo 1 y $U_2$ tras un round trip, $U_1$ es modo si
$U_2=\mu U_1$ con $\arg\{\mu\}$ múltiplo de $2\pi$ ($\mu$ real positivo); la intensidad se atenúa
$\mu^2$ por round trip. Sistema lineal con respuesta al impulso $h(x,y;x',y')$:
$$U_2(x,y)=\iint_{-\infty}^{\infty}h(x,y;x',y')\,U_1(x',y')\,dx'dy'\qquad(10.2\text{-}35)$$
Problema de autovalores (Apéndice C):
$$\iint_{-\infty}^{\infty}h(x,y;x',y')\,U(x',y')\,dx'dy'=\mu\,U(x,y)\qquad(10.2\text{-}36)$$
Autofunciones $U_{l,m}$ = modos; autovalores $\mu_{l,m}$; $|\mu_{l,m}|^2$ = factor de reducción
de intensidad por round trip del modo $(l,m)$. Con espejos infinitos y paraxialidad se recuperan
los H-G. $h$ se obtiene por difracción de Fresnel (§4.3B) (un paso = propagación $d$ +
truncamiento por la apertura + reflexión); en general hay que resolver numéricamente, iterando
desde un $U_1$ inicial (Fig. 10.2-10, p. 389).

Resultados para el confocal simétrico con aperturas circulares de radio $a$ (Fig. 10.2-11,
p. 389, adaptada de Siegman, *Lasers*, 1986, Fig. 19.19): la pérdida depende de un solo parámetro,
el **número de Fresnel** $N_F=a^2/\lambda d$. Como en el confocal $W=\sqrt{\lambda d/\pi}$,
$\lambda d=\pi W^2$ y $N_F=a^2/\pi W^2$: mayor $N_F$ → menor pérdida. La pérdida por paso del
modo $(0,0)$ es ≈ 0.1 % cuando $N_F\approx0.94$ (⇔ $a/W=1.72$); un gaussiano de ancho $W$ tendría
fuera de $a=1.72W$ una fracción $\exp(-2a^2/W^2)\approx0.27\%$, mayor que el 0.1 % del modo real.
Los modos superiores ((1,0), (2,0)) pierden más por su mayor extensión espacial.

---

### 10.3 Two- and Three-Dimensional Resonators (p. 390)

#### 10.3A Two-Dimensional Rectangular Resonators (p. 390)

Dos pares ortogonales de espejos planos paralelos (normales a $z$ y a $y$), luz confinada en el
plano $z$–$y$ (Fig. 10.3-1). Con separación $d$, ondas estacionarias con $\mathbf k=(k_y,k_z)$:
$$k_y=q_y\frac{\pi}{d},\qquad k_z=q_z\frac{\pi}{d},\qquad q_y=1,2,\dots,\ q_z=1,2,\dots\qquad(10.3\text{-}1)$$
Modo $U(\mathbf r)\propto\sin(q_y\pi y/d)\sin(q_z\pi z/d)$; el de orden más bajo es $(1,1)$
(los $(q_y,0)$ y $(0,q_z)$ tienen amplitud cero). Los modos son puntos de una red de paso $\pi/d$
en el espacio $k$ (Fig. 10.3-2); el número de onda es la distancia al origen y $\nu=ck/2\pi$:
$$k^2=k_y^2+k_z^2=\left(\frac{2\pi\nu}{c}\right)^2\qquad(10.3\text{-}2)$$
**[recuadro] Resonance Frequencies:**
$$\nu_{\mathbf q}=\nu_F\sqrt{q_y^2+q_z^2},\quad q_y,q_z=1,2,\dots,\qquad\nu_F=\frac{c}{2d}\qquad(10.3\text{-}3)$$
con $\mathbf q=(q_y,q_z)$. El número de modos en $\nu_1<\nu<\nu_2$ se cuenta como los puntos en
el anillo entre círculos de radios $k_1=2\pi\nu_1/c$ y $k_2=2\pi\nu_2/c$ (p. 391).

> **EJERCICIO 10.3-1** (p. 391) *Density of Modes in a Two-Dimensional Resonator.* (a) Número
> aproximado de modos entre 0 y $\nu$ si $2\pi\nu/c\gg\pi/d$ ($d\gg\lambda/2$), con dos
> polarizaciones. (b) Mostrar que la densidad de modos por unidad de área y de frecuencia es
> **[recuadro] Density of Modes (2D Resonator):**
> $$M(\nu)=\frac{4\pi\nu}{c^2}\qquad(10.3\text{-}4)$$
> (Guía: cuarto de círculo de radio $k$ con área $(\pi/d)^2$ por punto y factor 2 de
> polarización: $N=2\cdot\tfrac14\pi k^2/(\pi/d)^2=2\pi\nu^2d^2/c^2$; $dN/d\nu/d^2=4\pi\nu/c^2$.)

Modos fuera del plano (p. 391): tienen componente $k_x$ continua (el resonador es abierto en
$x$) y son modos guiados a lo largo del eje de una guía 2D (§8.3).

#### 10.3B Circular Resonators and Whispering-Gallery Modes (p. 391)

Resonador circular 2D de radio $a$: un rayo que se autorreproduce tras $N$ reflexiones recorre
un camino de round trip $Nd$, con $d=2a\sin(\pi/N)$ (Fig. 10.3-3). Para onda viajera, la
condición es $Nd=q\lambda=qc/\nu$ (ignorando el desfase de cada reflexión), de modo que
$\nu_q=qc/Nd$, $q=1,2,\dots$ y $\nu_F=c/Nd$. Casos: $N=2$: $\nu_F=c/2d=c/4a$ (igual que
(10.1-5)); $N=3$: $\nu_F=c/3d=c/3\sqrt3a$ (el anillo de tres espejos del ejercicio 10.1-1).
En el límite $N\to\infty$, $Nd\to2\pi a$ (circunferencia):
**[recuadro] Spacing of Resonance Frequencies:**
$$\nu_F=\frac{c}{2\pi a}\qquad(10.3\text{-}5)$$
Los rayos abrazan la frontera interior con incidencia casi rasante: **modos de galería de
susurros (WGM)**, análogos a los acústicos de la galería de una cúpula (p. 392). Fig. 10.3-3:
resonador de espejos vs. resonador dieléctrico (reflexión total interna). Otras secciones 2D:
estadio ("stadium") que soporta modos bow-tie con reflexiones localizadas en cuatro puntos del
perímetro que imitan la curvatura de un confocal (p. 392).

#### 10.3C Three-Dimensional Rectangular Cavity Resonators (p. 392)

Caja cerrada de dimensiones $d_x,d_y,d_z$ (Fig. 10.3-4a):
$$k_x=q_x\frac{\pi}{d_x},\quad k_y=q_y\frac{\pi}{d_y},\quad k_z=q_z\frac{\pi}{d_z},\qquad q_x,q_y,q_z=1,2,\dots\qquad(10.3\text{-}6)$$
Cada modo $\mathbf q=(q_x,q_y,q_z)$ es un punto en el espacio $k$; el espaciado en cada dirección
es inversamente proporcional al ancho en esa dirección (Fig. 10.3-4b para el cubo).
$$k^2=k_x^2+k_y^2+k_z^2=\left(\frac{2\pi\nu}{c}\right)^2\qquad(10.3\text{-}7)$$
La superficie de frecuencia constante es una esfera de radio $k=2\pi\nu/c$.
**[recuadro] Resonance Frequencies:**
$$\nu_{\mathbf q}=\sqrt{q_x^2\nu_{Fx}^2+q_y^2\nu_{Fy}^2+q_z^2\nu_{Fz}^2},\qquad q_x,q_y,q_z=1,2,\dots\qquad(10.3\text{-}8)$$
$$\nu_{Fx}=\frac{c}{2d_x},\quad\nu_{Fy}=\frac{c}{2d_y},\quad\nu_{Fz}=\frac{c}{2d_z}\qquad(10.3\text{-}9)$$
**Ejemplo (p. 393):** $d=1$ cm, $n=1$ → $\nu_F=15$ GHz, mucho menor que la frecuencia óptica
(no así en microresonadores, §10.4).

**Densidad de modos (p. 393–394).** Si todas las dimensiones $\gg\lambda$, aproximación
continua. Número de modos entre 0 y $\nu$ = puntos en el octante positivo de la esfera de radio
$k$: $2(\tfrac18)(\tfrac43\pi k^3)/(\pi/d)^3=(k^3/3\pi^2)d^3$ (factor 2 por las dos
polarizaciones; $(\pi/d)^3$ = volumen por punto). Con $k=2\pi\nu/c$:
$[(2\pi\nu/c)^3/3\pi^2]d^3=(8\pi\nu^3/3c^3)d^3$; entre $\nu$ y $\nu+\Delta\nu$:
$(8\pi\nu^2/c^3)d^3\Delta\nu$. Densidad por unidad de volumen y de frecuencia:
**[recuadro] Density of Modes (3D Resonator):**
$$M(\nu)=\frac{8\pi\nu^2}{c^3}\qquad(10.3\text{-}10)$$
Deducida por Rayleigh y Jeans para el cuerpo negro (§13.4B). Crece cuadráticamente (Fig. 10.3-5).
**Ejemplo numérico (p. 394):** a $\nu=3\times10^{14}$ Hz ($\lambda_0=1\ \mu$m),
$M(\nu)=0.08$ modos/(cm³·Hz); en una banda de 1 GHz hay $\approx8\times10^7$ modos/cm³.
Número de modos por volumen en $\nu_1<\nu<\nu_2$: $\int_{\nu_1}^{\nu_2}M(\nu)\,d\nu$.
Los resultados 2D/3D valen para geometrías arbitrarias grandes frente a $\lambda$. La
enumeración es matemáticamente idéntica a la de estados cuánticos de electrones en paredes
perfectamente reflectantes (densidad de estados en semiconductores, §16.1C).

---

### 10.4 Microresonators (p. 394)

**Definiciones (p. 394):** **microresonador** = resonador en el que una o más dimensiones son de
unas pocas longitudes de onda o menos. **Microcavidad** (microcavity resonator) = microresonador
con todas las dimensiones pequeñas, de modo que los modos están muy espaciados en todas las
direcciones de $k$ y las resonancias son escasas (sparse); en la práctica ambos términos se usan
indistintamente. La ausencia de modos en bandas extensas **inhibe** la emisión de fuentes dentro
de la microcavidad; a la vez, la emisión en modos particulares de una microcavidad de alto $Q$ y
pequeño volumen se **realza** respecto a modos ordinarios (§13.3E; láseres de microcavidad,
§17.4B) (p. 395).

Geometrías dieléctricas (p. 395): (1) micropilares con reflectores de Bragg; (2) microdiscos y
microesferas (WGM cerca de la superficie); (3) microtoroides (parecidos a anillos de fibra);
(4) cristales fotónicos 2D con defectos. Dos objetivos de diseño:
- **Reducir el volumen modal $V$**, definido como la integral espacial de la densidad de energía
  óptica $\tfrac12\epsilon\,\mathcal E^2$ del modo, normalizada a su valor máximo.
- **Aumentar el factor de calidad $Q$.**

**Tabla 10.4-1 (p. 395).** Volumen modal normalizado $V/\lambda^3$ y $Q$ típicos:

| | Micropilar | Microdisco | Microtoroide | Microesfera | Cristal fotónico |
|---|---|---|---|---|---|
| $V/\lambda^3$ | 5 | 5 | $10^3$ | $10^3$ | 1 |
| $Q$ | $10^3$ | $10^4$ | $10^8$ | $10^{10}$ | $10^4$ |

El análisis exacto exige resolver Helmholtz vectorial con condiciones de frontera planas,
cilíndricas o esféricas; en la práctica, soluciones numéricas (p. 395).

#### 10.4A Rectangular Microresonators (p. 395)

Caja de espejos planos: ondas estacionarias en las tres direcciones, frecuencias por (10.3-8).
Si la caja es pequeña solo los modos de orden más bajo caen en la banda óptica. Para un cubo,
tabla 10.4-2 en unidades de $\nu_F=c/2d$. **Ejemplo (p. 395):** $d=1\ \mu$m, $n=1.5$ →
$\nu_F=100$ THz; los modos de orden más bajo corresponden a longitudes de onda en vacío
$\lambda_o=2.13,\ 1.73,\ 1.34,\ 1.22,\ 1.06,\ 1.00,\ 0.87\ \mu$m, muy espaciadas.

**Tabla 10.4-2 (p. 396).** Frecuencias de los modos de orden más bajo de una microcavidad
cúbica (superíndice = degeneración, número de modos con esa frecuencia; p. ej. $1.41\nu_F$:
(011), (101), (110)):

| Modo $(q_xq_yq_z)$ | $(011)^{(3)}$ | $(111)^{(1)}$ | $(012)^{(6)}$ | $(112)^{(3)}$ | $(022)^{(3)}$ | $(122)^{(3)}$ | $(222)^{(1)}$ |
|---|---|---|---|---|---|---|---|
| Frecuencia (unid. de $\nu_F$) | 1.41 | 1.73 | 2.24 | 2.45 | 2.83 | 3 | 3.46 |

Cajas con dimensiones mixtas (gran relación de aspecto): red anisótropa en $k$, fina en las
direcciones grandes y gruesa en las pequeñas; se cuenta de forma continua solo en las finas.
Fig. 10.4-1 (p. 396), densidad modal $M(\nu)$ con (a) una, (b) dos, (c) tres dimensiones pequeñas
$d_s\ll d$ y $\nu_F=c/2d_s$: (c) todas pequeñas → frecuencias discretas de la tabla 10.4-2;
(b) discretos del microresonador 2D + continuo de un resonador 1D grande (densidad uniforme,
(10.1-10)) → escalera; (a) discretos 1D + continuo 2D (densidad lineal en $\nu$, (10.3-4)) →
tramos lineales.

#### 10.4B Micropillar, Microdisk, and Microtoroid Microresonators (p. 396)

Fig. 10.4-2 (p. 397). Confinamiento por reflexión total interna.
- **Micropilar (micropost)** (p. 396–397): cilindro de material de alto índice entre DBR. Axial:
  reflexión en los DBR como en un Fabry–Perot; lateral: reflexión total interna en las paredes.
  Semiconductores compuestos por litografía y grabado; DBR de AlAs/GaAs o AlGaAs/GaAs; el pilar
  puede contener una región activa de pozos cuánticos múltiples con ganancia (§17.4).
- **Microdisco** (p. 397): resonador circular con luz a incidencia casi rasante en WGM, confinada
  por reflexión total en la frontera circular (§10.3B). Tamaños de pocos a decenas de $\mu$m; $Q$
  mucho mayor que en resonadores de espejos (pérdidas mucho menores, tabla 10.4-1), limitado por la
  **calidad de la superficie** porque la luz viaja cerca del borde.
- **Microtoroide** (p. 397): similar a un anillo de fibra; modos = ondas guiadas circulantes.
  Fabricados en sílice sobre chip de silicio, sostenidos por un pilar de silicio; el toroide se
  forma por tensión superficial en estado fundido → acabado de escala atómica, pérdidas de
  scattering mucho menores que el microdisco. $Q>10^8$.

#### 10.4C Microsphere Microcavities (p. 397)

Esferas dieléctricas como microcavidades 3D; ciertos modos siguen órbitas confinadas cerca de un
círculo máximo: WGM. Se resuelve Helmholtz (5.3-16) vectorial con condiciones de frontera; los
modos se parecen a las funciones de onda del átomo de hidrógeno (§13.1A), con diferencias por el
carácter vectorial. Campos derivados de un potencial escalar $U$ que satisface Helmholtz (nota al
pie: Oraevsky, *Quantum Electronics* 32, 377–400, 2002). Esfera de radio $a$, índice $n$ en aire,
separación de variables en $(r,\theta,\phi)$:
$$U(r,\theta,\phi)\propto\sqrt r\,J_{\ell+1/2}(nk_or)\,P_{\mathsf m}^{\ell}(\cos\theta)\exp(\pm j\mathsf m\phi),\qquad r\le a\qquad(10.4\text{-}1)$$
$$\propto\sqrt r\,\mathcal H^{(1)}_{\ell+1/2}(nk_or)\,P_{\mathsf m}^{\ell}(\cos\theta)\exp(\pm j\mathsf m\phi),\qquad r>a\qquad(10.4\text{-}2)$$
$J_\ell$ = Bessel de primera especie de orden $\ell$; $\mathcal H^{(1)}_\ell$ = Hankel de primera
especie; $P_{\mathsf m}^{\ell}$ = función de Legendre asociada ("adjoint Legendre"); $\mathsf m,\ell$
enteros no negativos. (Nota de transcripción: en (10.4-2) el argumento de la Hankel aparece impreso
como $nk_or$; físicamente, fuera de la esfera el argumento debería ser $k_or$ — se transcribe
como está.) Las condiciones de frontera en $r=a$ dan una ecuación característica con valores
discretos de $k_o$ (resonancias), indexadas por un tercer entero $\mathsf n$. Dos polarizaciones:
**modo E** ($H_r=0$) y **modo H** ($E_r=0$) (p. 398).

Estructura de los modos (p. 398): $\mathsf n$ máximos radiales dentro de la esfera; $2\ell$
máximos azimutales; $\ell-\mathsf m+1$ máximos polares. El **modo fundamental** ($\mathsf n=1$,
$\mathsf m=\ell$) tiene un pico radial y uno polar en $\theta=\pi/2$. Para $\mathsf m=\ell$
grandes, confinamiento fuerte en el ecuador: $P_\ell^\ell(\cos\theta)\approx\sin^\ell\theta$ se
anula rápidamente fuera de $\theta=\pi/2$ y $J_\ell(nk_or)$ es pequeña salvo un pico cerca de
$r=a$: haz que viaja por el ecuador (Fig. 10.4-3a), como los WGM del disco. Para $\ell=\mathsf m$
suficientemente grande, **$\nu_\ell\approx\ell c/2\pi a$**: $\ell$ ≈ número de longitudes de onda
que caben en la longitud óptica del ecuador (comparar con (10.3-5)). Visión de rayos
(Fig. 10.4-3b): ondas cuasi-planas con vectores de onda que zigzaguean cerca del ecuador;
$|\mathbf k|=\sqrt{\ell(\ell+1)}/a$, componente azimutal $k_\phi=\mathsf m/a$; inclinación del
zigzag $\approx1/\sqrt\ell$ para el fundamental $\mathsf m=\ell$, y 90° para $\mathsf m=0$.

Microesferas de sílice fundida de bajas pérdidas: $Q>10^{10}$ (tabla 10.4-1) gracias al acabado
casi atómico por tensión superficial. **Acoplamiento**: fibra óptica con el cladding localmente
retirado (Fig. 10.4-4, p. 399).

#### 10.4D Photonic-Crystal Microcavities (p. 399)

Cristales fotónicos (cap. 7): dieléctricos periódicos con bandas prohibidas fotónicas. El
reflector de Bragg (BGR) es un cristal fotónico 1D. El micropilar con una altura de una o pocas
periodicidades del BGR es un cristal fotónico extendido con la cavidad como **defecto**:
**resonador de cristal fotónico** (Fig. 10.4-5a). En 2D (Fig. 10.4-5b): agujero faltante en una
red periódica (hexagonal) de agujeros de aire en una lámina; en la banda prohibida la luz queda
atrapada en el defecto, como un electrón/hueco en un defecto de un semiconductor; el defecto crea
nuevas resonancias dentro del gap con modos centrados en la microcavidad que decaen rápidamente
en el cristal circundante. Fabricación por litografía e-beam y grabado iónico reactivo en
semiconductores. Volúmenes modales tan pequeños como $\lambda^3$ (los más pequeños, tabla
10.4-1) y $Q$ hasta $10^4$.

---

### Reading List (p. 400)

Libros: Hodgson & Weber, *Laser Resonators and Beam Propagation* (2.ª ed. 2005); Vahala (ed.),
*Optical Microcavities* (2004); Staliūnas & Sánchez-Morcillo, *Transverse Patterns in Nonlinear
Optical Resonators* (2003); Chang & Campillo (eds.), *Optical Processes in Microcavities* (1996);
Oraevskiy, *Gaussian Beams and Optical Resonators* (1996); Anan'ev (1992); Vaughan, *The
Fabry–Perot Interferometer* (1989); Hernandez, *Fabry–Perot Interferometers* (1988); Siegman,
*Lasers* (1986); Weinstein, *Open Resonators and Open Waveguides* (1969).
Artículos: IEEE JSTQE 12(1), 2006 (microresonadores); Vahala, *Nature* 424, 839–846 (2003);
IEEE JSTQE 6(6), 2000; Nöckel & Stone, *Nature* 385, 45–47 (1997); Yamamoto & Slusher, *Physics
Today* 46(6), 66–73 (1993); Yokoyama, *Science* 256, 66–70 (1992); Siegman, *Appl. Opt.* 13,
353–367 (1974); Kogelnik & Li, *Appl. Opt.* 5, 1550–1567 (1966); Fox & Li, *BSTJ* 40, 453–488
(1961); Boyd & Gordon, *BSTJ* 40, 489–508 (1961).

---

## Tablas y datos numéricos útiles

| Dato | Valor | Página |
|---|---|---|
| $\nu_F$ de un resonador de 30 cm en aire | 500 MHz | 369 |
| $\nu_F$ de un resonador de 3 µm | 50 THz (primer modo a 6 µm; 2 modos en 700–900 nm, banda de 95 THz) | 369 |
| Fig. 10.1-7: $\mathcal F$ vs $\alpha_rd$ | $\alpha_rd=0.01\to\mathcal F\approx300$; $0.1\to\approx30$; $1\to\approx2$ | 375 |
| Cintura del confocal He–Ne, $\lambda_0=633$ nm | $d=100$ cm → $W_0=0.32$ mm; $d=25$ cm → $0.16$ mm | 385 |
| Pérdida de potencia por paso, gaussiano con $a=2W$ | $\exp(-2a^2/W^2)\approx3.35\times10^{-4}$ | 388 |
| Confocal: pérdida 0.1 %/paso del (0,0) | $N_F=a^2/\lambda d\approx0.94$, $a/W=1.72$ (gaussiano puro daría 0.27 %) | 389 |
| $\nu_F$ de cubo de $d=1$ cm, $n=1$ | 15 GHz | 393 |
| $M(\nu)$ 3D a $\nu=3\times10^{14}$ Hz ($\lambda_0=1$ µm) | 0.08 modos/(cm³·Hz); $\approx8\times10^7$ modos/cm³ en 1 GHz | 394 |
| Microcavidad cúbica $d=1$ µm, $n=1.5$ | $\nu_F=100$ THz; $\lambda_o$ = 2.13, 1.73, 1.34, 1.22, 1.06, 1.00, 0.87 µm | 395 |
| Tabla 10.4-1 ($V/\lambda^3$; $Q$) | micropilar 5; $10^3$ · microdisco 5; $10^4$ · microtoroide $10^3$; $10^8$ · microesfera $10^3$; $10^{10}$ · cristal fotónico 1; $10^4$ | 395 |
| Tabla 10.4-2 (cubo, unidades de $\nu_F$) | 1.41, 1.73, 2.24, 2.45, 2.83, 3, 3.46 (degeneraciones 3,1,6,3,3,3,1) | 396 |
| Materiales mencionados | DBR de AlAs/GaAs o AlGaAs/GaAs (micropilar); sílice (toroide, esfera); silicio (chip/pilar de soporte) | 397 |
| Problemas: GaAs $n=3.6$, $\alpha_s=1$ cm⁻¹; AlAs $n=3.2$ | — | 400–401 |

**Fórmulas de bolsillo (Fabry–Perot, §10.1):** $\nu_F=c/2d$ (FSR) · $\mathcal F=\pi\sqrt{|\mathsf r|}/(1-|\mathsf r|)\approx\pi/\alpha_rd$ ·
$\delta\nu=\nu_F/\mathcal F=c\alpha_r/2\pi=1/2\pi\tau_p$ · $\tau_p=1/c\alpha_r$ ·
$Q=\nu_0/\delta\nu=2\pi\nu_0\tau_p=(\nu_0/\nu_F)\mathcal F$ ·
$\alpha_r=\alpha_s+\frac{1}{2d}\ln\frac{1}{\mathcal R_1\mathcal R_2}\approx\alpha_s+(1-\mathcal R)/d$.
**Anillo/WGM (§10.3B):** $\nu_F=c/2\pi a$ con $c=c_o/n$ (para una guía, $n\to n_g$ índice de grupo,
que el libro no introduce aquí pero es la corrección estándar).

---

## Problemas al final del capítulo (p. 400–402)

(Numeración del libro; los ejercicios dentro del texto ocupan los números faltantes.
`*` = avanzado según el libro.)

- **10.1-3 Resonance Frequencies of a Resonator with an Etalon.** (a) Espaciado de resonancias
  de dos espejos planos a $d=15$ cm en aire. (b) Se inserta una placa de $d_1=2.5$ cm, $n=1.5$,
  ligeramente inclinada: nuevo espaciado.
- **10.1-4 Mirrorless Resonators.** Cristal semiconductor con caras clivadas como espejos
  (reflectancia por (6.2-15)); $n=3.6$, $\alpha_s=1$ cm⁻¹, $d=0.2$ mm, en aire: hallar $\nu_F$,
  $\alpha_r$, $\mathcal F$, $\delta\nu$, $Q$; con $\lambda_o=1.55$ µm estimar el número de modo $q$.
- **10.1-5 Fabry–Perot Etalon with Bragg Grating Reflectors.** Capa de GaAs entre dos reflectores
  de Bragg GaAs/AlAs (Prob. 7.1-2): hallar $\mathcal F$ y $Q$; transmitancia de un reflector de
  $N=10$ capas alternadas GaAs ($n_1=3.6$)/AlAs ($n_2=3.2$) de cuarto de onda, incidencia desde
  GaAs extendido.
- **10.1-6 Resonator Spectral Response.** Transmitancia medida de un Fabry–Perot simétrico con
  láser sintonizable: picos periódicos cada 150 MHz, FWHM 5 MHz, gas $n=1$: longitud y finura;
  si la única pérdida es la de los espejos, hallar sus reflectancias.
- **10.1-7 Optical Energy Decay Time.** Resonador con $\mathcal F=100$, $d=50$ cm, $n=1$: tiempo
  para que la energía almacenada caiga a la mitad.
- **10.2-5 Stability of Spherical-Mirror Resonators.** (a) ¿Puede ser estable un resonador con
  dos espejos convexos? (b) ¿Y uno convexo + uno cóncavo?
- **10.2-6 A Planar-Mirror Resonator Containing a Lens.** Lente de focal $f$ a $d/2$ entre dos
  espejos planos separados $d$: (a) matriz de round trip; (b) condición de estabilidad;
  (c) esbozar el haz gaussiano que se ajusta.
- **10.2-7 Self-Reproducing Rays in a Symmetric Resonator.** Espejos cóncavos de radio $R$ a
  $d=3|R|/2$: ¿tras cuántos round trips se retraza un rayo?
- **10.2-8 Ray Position in Unstable Resonators.** Mostrar que para un resonador inestable
  $y_m=\alpha_1h_1^m+\alpha_2h_2^m$ con $h_{1,2}=b\pm\sqrt{b^2-1}$, $b=2(1+d/R_1)(1+d/R_2)-1$
  (pista: §1.4D).
- **10.2-9 Ray Position in Unstable Symmetric Resonators.** Verificar que $R=-30$ cm, $d=65$ cm
  es inestable; con $y_0=0$, $\theta_0=0.1°$, hallar $y_1$ tras un round trip; con aperturas de
  5 cm de diámetro, ¿cuántos round trips hasta que el rayo escapa? Programa para graficar $y_m$
  con $d=50$ cm y $d=65$ cm (usar 10.2-8).
- **10.2-10 Gaussian-Beam Standing Waves.** Suma de dos gaussianos idénticos en $\pm z$ es onda
  estacionaria; con espejos ideales sobre los frentes deducir (10.2-30).
- **10.2-11 Gaussian Beam in a Symmetric Confocal Resonator.** $d=16$ cm, $\mathcal R=0.995$,
  $n=1$, $\lambda_o=1$ µm: (a) radios de los espejos; (b) cintura del (0,0); (c) intensidad del
  (1,0) en un espejo y distancia entre picos; (d) frecuencias de (0,0) y (1,0); (e) $\alpha_r$
  solo por espejos.
- **\*10.2-12 Diffraction Loss in a Symmetric Confocal Resonator.** Con Fig. 10.2-11
  ($N_F=a^2/\lambda d$) y los parámetros de 10.2-11, radio de espejo para que la pérdida por
  paso del modo (1,0) sea 1 %.
- **10.3-2 Number of Modes in Resonators of Different Dimensions.** $\lambda_o=1.06$ µm,
  $\Delta\nu=120$ GHz, $n=1$: número de modos en (a) resonador 1D de $d=10$ cm; (b) 2D de
  10 cm × 10 cm; (c) 3D de 10 cm × 10 cm × 10 cm.

---

## Relación con Óptica No Lineal

### Para el curso

- **Ondas EM y modos (§10.1A, §10.3):** el modo como solución de Helmholtz con condiciones de
  frontera, y la cuantización $k_q=q\pi/d$, son la base para describir cavidades láser y para la
  descomposición modal que se usa al tratar generación de armónicos o mezcla de ondas dentro de
  cavidades (OPO, SHG intracavidad). La densidad de modos $8\pi\nu^2/c^3$ (10.3-10) entra en la
  emisión espontánea y en el ruido cuántico que siembra procesos paramétricos y Raman.
- **Haz gaussiano (§10.2B–D):** parámetros $W_0$, $z_0$, $R(z)$, fase de Gouy; necesario para
  calcular intensidades pico (y por tanto $n_2I$, $\Delta n$ Kerr) en el foco de un haz enfocado,
  y para el acoplamiento de fase en SHG con haces enfocados (teoría de Boyd–Kleinman usa
  $b=2z_0$, el parámetro confocal de la p. 385).
- **Absorción y dispersión (§10.1, pérdidas):** el coeficiente $\alpha_s$ entra en $\alpha_r$
  (10.1-22); la absorción no lineal (dos fotones, saturable) modifica $\alpha_r$ con la
  intensidad y por tanto $\mathcal F$, $\delta\nu$ y $Q$: fundamento de la biestabilidad óptica
  en Fabry–Perot (dispersiva vía $n_2$: desplazamiento de $\nu_q$ con $d\to nd$; absorptiva vía
  $\alpha$).
- **Índice dependiente de la intensidad / $\chi^{(3)}$:** la condición de resonancia
  $2d=q\lambda_q$ con $\lambda_q$ en el medio implica $\nu_q=qc_o/2nd$; un cambio $\Delta n=n_2I$
  desplaza las resonancias en $\Delta\nu/\nu=-\Delta n/n$. Con $\mathcal F$ alta, la intensidad
  intracavidad $I_{\max}=I_0/(1-|\mathsf r|)^2$ (10.1-13) amplifica el efecto Kerr (realce
  resonante de SPM/XPM/FWM, peines de Kerr).
- **Pulsos y GVD:** el espaciado $\nu_F$ y el tiempo de round trip $2d/c$ fijan la tasa de
  repetición de un láser de modos bloqueados; la dispersión del medio hace que $\nu_F$ dependa
  de $\nu$ (a través de $n_g$), lo que importa para solitones de cavidad y peines.
- **FWM, Raman:** en microresonadores de alto $Q$ (microtoroides, microesferas, §10.4) la
  potencia circulante es tan alta que aparecen FWM degenerado (peines) y láseres Raman de umbral
  muy bajo; la ecuación $Q=2\pi\nu_0\tau_p$ permite convertir $Q$ en tiempo de almacenamiento.

### Para el proyecto final (anillo add-drop en Si₃N₄, sensado de índice de volumen)

- **FSR del anillo:** (10.3-5) $\nu_F=c/2\pi a$ con $c=c_o/n$; para la guía hay que usar el
  índice de grupo $n_g$ del modo (dispersión de la guía): $\mathrm{FSR}_\lambda=\lambda^2/(n_gL)$,
  $L=2\pi a$. El libro deduce el caso $N\to\infty$ del polígono de $N$ reflexiones (p. 391–392).
- **$Q$, finura y ancho de línea:** $Q=\nu_0/\delta\nu$ (10.1-34), $\mathcal F=\nu_F/\delta\nu$
  (10.1-19), $Q=(\nu_0/\nu_F)\mathcal F$ (10.1-36); $\tau_p=Q/2\pi\nu_0$ (10.1-35). Para el
  anillo, $\alpha_r$ (10.1-22/23) se reparte en pérdida distribuida de la guía $\alpha_s$ y
  pérdidas "concentradas" por los acopladores (análogo a $1-\mathcal R$ en (10.1-26) con
  $\kappa^2$ de acoplamiento): $Q_{\text{total}}^{-1}=Q_i^{-1}+Q_c^{-1}$ en la nomenclatura
  usual; útil para interpretar los resultados de la skill `lumerical-analisis-resultados`
  (λ de resonancia, extinción, FWHM, Q, FSR, $n_g$).
- **Sensado refractométrico:** el analito como cladding cambia $n_{\text{eff}}$ y desplaza la
  resonancia ($\Delta\lambda=\lambda\,\Delta n_{\text{eff}}/n_g$); el límite de detección
  depende de $\delta\nu$ (⇔ $Q$), por lo que las secciones 10.1 (ancho espectral vs. pérdida) y
  10.4B (Q de microdisco limitado por rugosidad superficial; toroide con acabado atómico,
  $Q>10^8$) justifican perseguir bajas pérdidas de scattering en la guía de Si₃N₄.
- **Modos de galería (§10.3B, §10.4C):** en anillos anchos aparecen modos radiales de orden
  superior (análogos a $\mathsf n>1$ en la esfera) con distinto $n_{\text{eff}}$ y FSR; el
  recuento de máximos radiales/azimutales de la p. 398 ayuda a etiquetar modos en simulaciones
  FDTD/MODE. La relación $\nu_\ell\approx\ell c/2\pi a$ identifica el número azimutal $\ell$ con
  el número de longitudes de onda en el perímetro.
- **Supercontinuo y dispersión de guías:** aunque el capítulo no trata dispersión, el tiempo de
  vida y la intensidad intracavidad $I_{\max}$ (10.1-13) cuantifican el realce resonante que
  convierte un anillo de Si₃N₄ en fuente de peines de Kerr; la tabla 10.4-1 da el orden de
  magnitud de $Q$ y $V$ de las plataformas competidoras (toroides/esferas de sílice vs. anillos
  integrados).
- **Acoplamiento (Fig. 10.4-4):** el libro solo muestra acoplamiento evanescente fibra–esfera;
  el acoplador guía–anillo del add-drop es el equivalente integrado (cap. 8/9 del libro), no
  tratado aquí.
