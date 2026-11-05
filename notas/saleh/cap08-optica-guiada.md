# Capítulo 8 — Guided-Wave Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 289–324 (PDF 311–346). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 8.
Todas las páginas citadas abajo son páginas **del libro** (PDF = libro + 22).

Convención de notación del libro (se respeta en estos apuntes): dependencia temporal
$e^{j\omega t}$, $j=\sqrt{-1}$; ondas que viajan en $+z$ como $\exp(-j\beta z)$; campos reales en
caligráfica ($\mathcal{E}$), amplitudes complejas en itálica/negrita ($E$, $\mathbf{T}$);
$k_o = 2\pi/\lambda_o$ número de onda en el vacío, $c_o$ velocidad de la luz en el vacío,
$c = c_o/n$, $\lambda = \lambda_o/n$ en el medio; $\eta_o=\sqrt{\mu_o/\epsilon_o}$ impedancia
del vacío. Unidades SI. El libro usa $\doteq$ con significado de "redondeado al entero" (al
inferior en 8.1, al superior en 8.2; ver cada sección).

---

## Resumen del capítulo

El capítulo presenta la teoría básica de las guías de onda ópticas rectangulares usadas en
óptica integrada (p. 290). Parte de la guía de espejos planos (§8.1), donde la condición de
autoconsistencia (una onda plana TEM que se refleja dos veces debe reproducirse a sí misma)
cuantiza los ángulos de rebote, las componentes transversales del vector de onda y las
constantes de propagación; de ahí salen las distribuciones de campo (modos TE y TM), el número
de modos, la frecuencia de corte, la relación de dispersión $\beta(\omega)$ y la velocidad de
grupo. Luego repite el análisis para la guía dieléctrica plana simétrica (§8.2), donde el
confinamiento es por reflexión interna total: la condición de autoconsistencia incluye la fase
de reflexión $\varphi_r$, el resultado es una ecuación trascendente (ec. de autovalores) cuyas
soluciones dan los modos; aparecen el campo evanescente, el coeficiente de extinción, el factor
de confinamiento, el índice efectivo $n$ con $n_2<n<n_1$, la dispersión de guía (GVD aun sin
dispersión material) y el efecto Goos–Hänchen. §8.3 generaliza a guías 2D (espejos y
dieléctricas), geometrías de canal (strip, rib, embedded, strip-loaded) y materiales
(Ti:LiNbO₃, GaAs/AlGaAs, InP, vidrio, polímeros, SOI). §8.4 trata guías por rejilla de Bragg
y cristales fotónicos (capa defecto, guía 2D por línea de agujeros faltantes). §8.5 cubre el
acoplamiento de luz a guías (excitación de modos por proyección sobre funciones ortogonales,
acopladores de extremo, prisma y rejilla), la **teoría de modos acoplados** para dos guías
paralelas (ecuaciones acopladas, matriz de transmisión, intercambio periódico de potencia,
longitud de acoplamiento $L_0=\pi/2\mathcal{C}$, acoplador 3 dB, conmutación por desajuste de
fase, con derivación perturbativa), y guías periódicas. §8.6 es una introducción cualitativa a
la plasmónica (SPP, guías MIM, metamateriales, nano-óptica, biosensado).

---

## Secciones

### Introducción del capítulo (p. 290–291)

- Idea central: un medio de índice $n_1$ embebido en otro de índice menor $n_2<n_1$ actúa como
  "trampa" de luz por reflexiones internas totales múltiples (p. 290; cita el Ejercicio 1.2-6).
- Definición: **guía de onda óptica** = conducto de luz consistente en una lámina (slab),
  tira (strip) o cilindro de dieléctrico embebido en otro dieléctrico de menor índice; la luz
  se transporta sin radiar al medio circundante (p. 290, Fig. 8.0-1: slab, strip, fibra).
- **Óptica integrada**: combinación en un solo sustrato ("chip") de dispositivos para generar,
  enfocar, dividir, combinar, aislar, polarizar, acoplar, conmutar, modular y detectar luz;
  las guías son los enlaces (p. 290; Fig. 8.0-2, p. 291: receptor/transmisor integrado con
  láser, modulador, acopladores, guía, fotodiodo, fibra).
- Mapa: cap. 8 guías rectangulares; cap. 9 fibras; cap. 10 resonadores (reflectores en los
  extremos de una guía corta); caps. 17, 20, 23, 24 componentes y sistemas (p. 290–291).

---

### 8.1 Planar-Mirror Waveguides (p. 291)

Dos espejos planos infinitos paralelos separados una distancia $d$, reflexión sin pérdidas; un
rayo en el plano $y$–$z$ a ángulo $\theta$ con el eje $z$ rebota y queda guiado (Fig. 8.1-1,
p. 291). No se usa en la práctica (espejos de baja pérdida difíciles y caros) pero es la
introducción pedagógica a la guía dieléctrica (§8.2) y al resonador (cap. 10).

#### Waveguide Modes (p. 291–293)

Análisis electromagnético: a cada rayo se le asocia una onda plana TEM; el campo total es la
suma de esas ondas planas. Onda monocromática de longitud de onda $\lambda=\lambda_o/n$, número
de onda $k=nk_o$, velocidad de fase $c=c_o/n$, polarizada en $x$, vector de onda en el plano
$y$–$z$ a ángulo $\theta$ con $z$. En un espejo perfecto cada reflexión introduce un **desfase
$\pi$** (campo paralelo al espejo), sin cambiar amplitud ni polarización; así el campo total
se anula en los espejos (p. 291–292).

**Condición de autoconsistencia** (p. 292, Fig. 8.1-2): tras reflejarse dos veces la onda debe
reproducirse a sí misma, de modo que solo hay dos ondas planas distintas. Los campos que la
cumplen son los **modos** (autofunciones) de la guía. *"Modes are fields that maintain the same
transverse distribution and polarization at all locations along the waveguide axis"* (p. 292).
Con $\overline{AC}-\overline{AB}=2d\sin\theta$ y un desfase $\pi$ por reflexión:
$\Delta\varphi = 2\pi\overline{AC}/\lambda - 2\pi - 2\pi\overline{AB}/\lambda = 2\pi q$,
$q=0,1,2,\dots$, es decir

$$\frac{2\pi}{\lambda}\,2d\sin\theta = 2\pi m,\qquad m=1,2,\dots \tag{8.1-1}$$

con $m=q+1$. De ahí los **ángulos de rebote** (recuadro, p. 292):

$$\boxed{\sin\theta_m = m\frac{\lambda}{2d},\qquad m=1,2,\dots} \tag{8.1-2}$$

Cada entero $m$ ↔ un ángulo $\theta_m$ ↔ el **modo $m$**. El modo $m=1$ tiene el ángulo más
pequeño, $\theta_1=\sin^{-1}(\lambda/2d)$; modos de mayor $m$ son más oblicuos (p. 292).
Cuando se cumple la autoconsistencia, las fases de las ondas ascendente y descendente sobre el
eje $z$ difieren en la mitad del desfase de ida y vuelta, $q\pi=(m-1)\pi$: se suman para $m$
impar y se restan para $m$ par (p. 293).

Como $k_y = nk_o\sin\theta$, queda cuantizada (recuadro, p. 293):

$$\boxed{k_{ym} = m\frac{\pi}{d},\qquad m=1,2,3,\dots} \tag{8.1-3}$$

(componente transversal del vector de onda, espaciadas en $\pi/d$). Interpretación: la fase
acumulada en una ida y vuelta $2d$ en $y$ con constante $k_{ym}$ debe ser múltiplo de $2\pi$.

#### Propagation Constants (p. 293)

La onda guiada son dos ondas planas con vectores $(0,k_y,k_z)$ y $(0,-k_y,k_z)$; su suma o
diferencia varía con $z$ como $\exp(-jk_z z)$, así que la **constante de propagación** es
$\beta\equiv k_z=k\cos\theta$, cuantizada a $\beta_m=k\cos\theta_m$, y con (8.1-2):

$$\boxed{\beta_m^2 = k^2 - \frac{m^2\pi^2}{d^2}} \tag{8.1-4}$$

Modos de orden superior (más oblicuos) tienen menor $\beta$. **Fig. 8.1-3** (p. 293): $\sin\theta$
vs. $\theta$ con los $\theta_m$ marcados (no equiespaciados), y diagrama $k_y$ vs. $\beta$: los
$k_{ym}$ sí son equiespaciados ($\pi/d$), los puntos caen sobre el círculo de radio $nk_o$;
$m=1$ tiene el menor ángulo y la mayor $\beta$.

#### Field Distributions (p. 294)

Onda ascendente $A_m\exp(-jk_{ym}y-j\beta_m z)$, descendente $e^{j(m-1)\pi}A_m\exp(+jk_{ym}y-j\beta_m z)$
(en $y=0$ difieren en $(m-1)\pi$). Modos simétricos (se suman) y antisimétricos (se restan):
$E_x(y,z)=2A_m\cos(k_{ym}y)\exp(-j\beta_m z)$ para $m$ impar y $2jA_m\sin(k_{ym}y)\exp(-j\beta_m z)$
para $m$ par. Se escribe

$$E_x(y,z) = \mathsf{a}_m u_m(y)\exp(-j\beta_m z), \tag{8.1-5}$$

$$u_m(y)=\begin{cases}\sqrt{\dfrac{2}{d}}\cos\!\left(m\pi\dfrac{y}{d}\right), & m=1,3,5,\dots\\[2ex]
\sqrt{\dfrac{2}{d}}\sin\!\left(m\pi\dfrac{y}{d}\right), & m=2,4,6,\dots\end{cases} \tag{8.1-6}$$

con $\mathsf{a}_m=\sqrt{2d}\,A_m$ ($m$ impar) y $j\sqrt{2d}\,A_m$ ($m$ par). Normalización y
ortogonalidad en $[-d/2,d/2]$:

$$\int_{-d/2}^{d/2}u_m^2(y)\,dy = 1, \tag{8.1-7}$$

$$\int_{-d/2}^{d/2}u_m(y)\,u_l(y)\,dy = 0,\qquad l\neq m. \tag{8.1-8}$$

$\mathsf{a}_m$ es la **amplitud del modo $m$**. Cada modo es una onda estacionaria en $y$ que
viaja en $z$; el campo se anula en $y=\pm d/2$ para todos los modos (Fig. 8.1-4, p. 294:
perfiles $m=1,2,3,6$). Como se supuso polarización en $x$, la onda guiada es **TE**
(transverse electric); TM se analiza después (p. 294).

**Ejercicio 8.1-1, Optical Power** (p. 295): mostrar que el flujo de potencia óptica en $z$ del
modo TE $E_x=\mathsf{a}_m u_m(y)\exp(-j\beta_m z)$ es $(|\mathsf{a}_m|^2/2\eta)\cos\theta_m$, con
$\eta=\eta_o/n$, $\eta_o=\sqrt{\mu_o/\epsilon_o}$.

#### Number of Modes (p. 295)

Con $\sin\theta_m=m\lambda/2d<1$, el máximo $m$ es el mayor entero menor que $1/(\lambda/2d)$:

$$\boxed{M \doteq \frac{2d}{\lambda}} \tag{8.1-9}$$

($\doteq$: reducido al entero más cercano por abajo; ejemplos: $2d/\lambda=0.9,\,1,\,1.1 \Rightarrow
M=0,\,0,\,1$). $M$ es el número máximo de modos; cuántos llevan potencia depende de la
excitación. Si $d\le\lambda/2$, $M=0$: no hay modos. $\lambda_c=2d$ es la **longitud de onda de
corte** (la mayor que la guía puede guiar). **Frecuencia de corte** (recuadro):

$$\boxed{\nu_c = \frac{c}{2d}} \tag{8.1-10}$$

$\omega_c=2\pi\nu_c=\pi c/d$. Si $1<2d/\lambda\le2$ (i.e. $d\le\lambda<2d$, $\nu_c\le\nu<2\nu_c$)
solo hay un modo: **guía monomodo**. Ejemplo numérico (p. 295): $d=5\,\mu$m ⇒ $\lambda_c=10\,\mu$m;
monomodo para $5\,\mu\text{m}\le\lambda<10\,\mu$m, multimodo para $\lambda<5\,\mu$m. También
$M\doteq\nu/\nu_c=\omega/\omega_c$: $M$ aumenta en 1 cada vez que $\omega$ crece $\omega_c$
(Fig. 8.1-5(a), p. 296).

#### Dispersion Relation (p. 295–296)

Relación $\beta$–$\omega$. Medio homogéneo: $\omega=c\beta$. Modo $m$ de la guía de espejos,
de (8.1-4):

$$\beta_m^2=(\omega/c)^2-m^2\pi^2/d^2, \tag{8.1-11}$$

y con $\omega_c=\pi c/d$ (recuadro, p. 296):

$$\boxed{\beta_m = \frac{\omega}{c}\sqrt{1-m^2\frac{\omega_c^2}{\omega^2}}} \tag{8.1-12}$$

$\beta_m=0$ en $\omega=m\omega_c$, crece monótonamente y tiende a la línea de luz $\beta=\omega/c$
para $\beta$ grande. **Fig. 8.1-5** (p. 296): (a) $M$ vs. $\omega$ (escalera); (b) relación de
dispersión con la "light line" $\omega=c\beta$ y la "forbidden band" bajo $\omega_c$; (c)
velocidad de grupo de cada modo vs. $\omega$.

#### Group Velocities (p. 296–297)

Un pulso centrado en $\omega$ viaja a $v=d\omega/d\beta$ (velocidad de grupo, §5.6). Derivando
(8.1-12) con $c$ independiente de $\omega$ (sin dispersión material): $2\beta_m\,d\beta_m/d\omega
= 2\omega/c^2$ ⇒ $d\omega/d\beta_m = c^2\beta_m/\omega = c\cos\theta_m$ (recuadro):

$$\boxed{v_m = c\cos\theta_m = c\sqrt{1-m^2\frac{\omega_c^2}{\omega^2}}} \tag{8.1-13}$$

Modos más oblicuos viajan más lento (camino en zigzag más largo); para cada modo $v$ crece
monótonamente de 0 a $c$ al subir $\omega$ por encima de su corte (Fig. 8.1-5(c)). Derivación
geométrica (Fig. 8.1-6, p. 297): en un tramo entre espejos avanza $d\cot\theta$ en $z$ en un
tiempo $d\csc\theta/c$:

$$v=\frac{\text{distancia}}{\text{tiempo}}=\frac{d\cot\theta}{d\csc\theta/c}=c\cos\theta. \tag{8.1-14}$$

#### TM Modes (p. 297–298)

Modos TM: campo magnético en $x$. Se analizan con una onda TEM con $H$ en $x$; el campo
eléctrico tiene componentes $y$ y $z$. La componente $z$ es paralela al espejo y se comporta
igual que la $x$ del caso TE (desfase $\pi$, se anula en los espejos), así que $\theta_m$,
$k_{ym}$ y $\beta_m$ de los modos TM son **idénticos** a los TE. Hay $M\doteq 2d/\lambda$ modos
TM (total $2M$ modos) (p. 297; Fig. 8.1-7: TE con $\mathbf{E}$ en $x$, TM con $\mathbf{H}$
en $x$).

$$E_z(y,z)=\begin{cases}\mathsf{a}_m\sqrt{\dfrac{2}{d}}\cos\!\left(m\pi\dfrac{y}{d}\right)\exp(-j\beta_m z), & m=1,3,5,\dots\\[2ex]
\mathsf{a}_m\sqrt{\dfrac{2}{d}}\sin\!\left(m\pi\dfrac{y}{d}\right)\exp(-j\beta_m z), & m=2,4,6,\dots\end{cases} \tag{8.1-15}$$

con $\mathsf{a}_m=\sqrt{2d}A_m$ y $j\sqrt{2d}A_m$ para $m$ impar/par. El campo E de una onda TEM
es normal a su propagación, luego forma ángulo $\pi/2+\theta_m$ ($\pi/2-\theta_m$) con $z$
para la onda ascendente (descendente). Componentes $y$ (p. 298):

$$A_m\cot\theta_m\exp(-jk_{ym}y)\exp(-j\beta_m z)\ \text{ y }\ e^{jm\pi}A_m\cot\theta_m\exp(jk_{ym}y)\exp(-j\beta_m z), \tag{8.1-16}$$

$$E_y(y,z)=\begin{cases}\mathsf{a}_m\sqrt{\dfrac{2}{d}}\cot\theta_m\cos\!\left(m\pi\dfrac{y}{d}\right)\exp(-j\beta_m z), & m=1,3,5,\dots\\[2ex]
\mathsf{a}_m\sqrt{\dfrac{2}{d}}\cot\theta_m\sin\!\left(m\pi\dfrac{y}{d}\right)\exp(-j\beta_m z), & m=2,4,6,\dots\end{cases} \tag{8.1-17}$$

Las condiciones de frontera se cumplen porque $E_z$ se anula en los espejos. $H_x(y,z)$ se
obtiene de que la razón E/H de una onda TEM es la impedancia $\eta$ del medio (p. 298).

#### Multimode Fields (p. 298–299)

Un campo que cumpla las condiciones de frontera pero con distribución transversal arbitraria
también se guía; la potencia se reparte entre modos que viajan con distintas $\beta$ y $v$, por
lo que la distribución transversal **cambia con $z$** (Fig. 8.1-8, p. 298: intensidad del modo 1
invariante; del modo 2 invariante; de la mezcla $u_1e^{-j\beta_1 z}+u_2e^{-j\beta_2 z}$ varía
con $z$ porque $\beta_1\ne\beta_2$). Campo TE arbitrario (p. 299):

$$E_x(y,z)=\sum_{m=0}^{M}\mathsf{a}_m u_m(y)\exp(-j\beta_m z), \tag{8.1-18}$$

(nota: el libro escribe el índice inferior de la suma como $m=0$ aunque los modos de la guía de
espejos empiezan en $m=1$; así aparece en la p. 299). $\mathsf{a}_m$ = pesos = amplitudes modales.

**Ejercicio 8.1-2, Optical Power in a Multimode Field** (p. 299): mostrar que la potencia en $z$
del campo (8.1-18) es la suma de las potencias $(|\mathsf{a}_m|^2/2\eta)\cos\theta_m$ de cada modo.

---

### 8.2 Planar Dielectric Waveguides (p. 299)

Lámina dieléctrica (slab) rodeada de medios de menor índice; guiado por reflexión interna
total. Nomenclatura de películas delgadas: "film", "cover", "substrate"; o "core" y
"cladding". Se estudia la guía **simétrica** de ancho $d$ e índice $n_1$ con cladding $n_2<n_1$,
todo sin pérdidas (Fig. 8.2-1, p. 299). Rayos con $\theta<\bar\theta_c=\pi/2-\sin^{-1}(n_2/n_1)
=\cos^{-1}(n_2/n_1)$ (complemento del ángulo crítico; ec. (1.2-5), Figs. 6.2-3 y 6.2-5) se
guían sin pérdida; rayos con ángulo mayor refractan, pierden potencia en cada rebote y
desaparecen (p. 299). En vez de resolver Maxwell con condiciones de frontera (Prob. 8.2-6) se
usan ondas planas TEM + autoconsistencia (p. 299–300).

#### A. Waveguide Modes (p. 300–303)

Onda TEM de $\lambda=\lambda_o/n_1$, velocidad de fase $c_1=c_o/n_1$, número de onda $n_1k_o$,
componentes $k_x=0$, $k_y=n_1k_o\sin\theta$, $k_z=n_1k_o\cos\theta$, a ángulo $\theta<\bar\theta_c$.
En una ida y vuelta la onda dos veces reflejada se retrasa $\overline{AC}-\overline{AB}=2d\sin\theta$
y además hay una fase $\varphi_r$ por cada reflexión interna total (§6.2). Autoconsistencia:

$$\frac{2\pi}{\lambda}2d\sin\theta-2\varphi_r=2\pi m,\qquad m=0,1,2,\dots \tag{8.2-1}$$

$$2k_yd-2\varphi_r=2\pi m. \tag{8.2-2}$$

Única diferencia con (8.1-1), (8.1-3): el desfase $\pi$ del espejo se reemplaza por $\varphi_r$.
Nótese que aquí **$m$ empieza en 0**. $\varphi_r$ depende de $\theta$ y de la polarización.
Caso **TE** (E en $x$): sustituyendo $\theta_1=\pi/2-\theta$ y $\theta_c=\pi/2-\bar\theta_c$ en
(6.2-11) (p. 300–301):

$$\tan\frac{\varphi_r}{2}=\sqrt{\frac{\sin^2\bar\theta_c}{\sin^2\theta}-1}, \tag{8.2-3}$$

de modo que $\varphi_r$ va de $\pi$ a 0 cuando $\theta$ va de 0 a $\bar\theta_c$. Escribiendo
(8.2-1) como $\tan(\pi d\sin\theta/\lambda-m\pi/2)=\tan(\varphi_r/2)$ (recuadro, p. 301):

$$\boxed{\tan\!\left(\pi\frac{d}{\lambda}\sin\theta-m\frac{\pi}{2}\right)=\sqrt{\frac{\sin^2\bar\theta_c}{\sin^2\theta}-1}} \tag{8.2-4}$$

**Condición de autoconsistencia / ecuación de autovalores (modos TE).** Ecuación
trascendente en $\sin\theta$; sus soluciones son los ángulos de rebote $\theta_m$. **Solución
gráfica (Fig. 8.2-2, p. 300)**: se grafican RHS y LHS vs. $\sin\theta$. RHS $=\tan(\varphi_r/2)$
decrece monótonamente y se anula en $\sin\theta=\sin\bar\theta_c$; LHS genera dos familias de
curvas, $\tan[(\pi d/\lambda)\sin\theta]$ y $\cot[(\pi d/\lambda)\sin\theta]$, para $m$ par e
impar; las intersecciones (círculos llenos) dan los $\theta_m$. Los de la guía de espejos
(círculos vacíos, $\sin\theta_m=m\lambda/2d$) se obtienen con $\varphi_r=\pi$,
$\tan(\varphi_r/2)=\infty$. En esa figura $\sin\bar\theta_c=8(\lambda/2d)$ y $M=9$.

Los $\theta_m\in(0,\bar\theta_c)$; vectores de onda $(0,n_1k_o\sin\theta_m,n_1k_o\cos\theta_m)$;
**constantes de propagación** (recuadro, p. 301):

$$\boxed{\beta_m=n_1k_o\cos\theta_m} \tag{8.2-5}$$

Como $\cos\theta_m\in(\cos\bar\theta_c,1)=(n_2/n_1,1)$: **$n_2k_o<\beta_m<n_1k_o$** (Fig. 8.2-3,
p. 301: diagrama $k_y$–$k_z$ con los modos entre los círculos de radio $n_2k_o$ y $n_1k_o$;
comparar con Fig. 8.1-3). Los modos **TM** usan (8.2-1) con $\varphi_r$ de (6.2-13); resultados
similares (p. 302).

**Number of Modes** (p. 302). En la Fig. 8.2-2 la abscisa se divide en intervalos de ancho
$\lambda/2d$, cada uno con un modo, hasta $\sin\theta\le\sin\bar\theta_c$. El número de modos TE
es el menor entero mayor que $\sin\bar\theta_c/(\lambda/2d)$:

$$M\doteq\frac{\sin\bar\theta_c}{\lambda/2d}, \tag{8.2-6}$$

($\doteq$ aquí: **aumentado** al entero más cercano; ejemplos $0.9,1,1.1\Rightarrow M=1,2,2$).
Con $\cos\bar\theta_c=n_2/n_1$ (recuadros, p. 302):

$$\boxed{M\doteq\frac{2d}{\lambda_o}\,\mathrm{NA}} \tag{8.2-7}$$

$$\boxed{\mathrm{NA}=\sqrt{n_1^2-n_2^2}} \tag{8.2-8}$$

NA = apertura numérica = seno del ángulo de aceptación de rayos desde el aire a la lámina
(Ejercicio 1.2-5). Ejemplo en texto (p. 302): $d/\lambda_o=10$, $n_1=1.47$, $n_2=1.46$ ⇒
$\bar\theta_c=6.7^\circ$, NA $=0.171$, $M=4$ modos TE.

**Guía monomodo**: cuando $\lambda/2d>\sin\bar\theta_c$ o $(2d/\lambda_o)\mathrm{NA}<1$ (lámina
suficientemente delgada o longitud de onda suficientemente larga). A diferencia de la guía de
espejos, **no hay longitud de onda de corte absoluta**: el modo fundamental $m=0$ siempre
existe; cada modo $m=1,2,\dots$ tiene su propio corte (p. 302). En frecuencia, monomodo si
$\nu>\nu_c$ ($\omega>\omega_c$) con (recuadro, p. 302):

$$\boxed{\nu_c=\omega_c/2\pi=\frac{1}{\mathrm{NA}}\frac{c_o}{2d}} \tag{8.2-9}$$

**Mode cutoff frequency.** $M\doteq\nu/\nu_c=\omega/\omega_c$ (Fig. 8.2-4, p. 303: escalera
que empieza en $M=1$ en $\omega=0$; "no hay banda prohibida"). Para TM, expresiones idénticas.

**Ejemplo 8.2-1, Modes in an AlGaAs Waveguide** (p. 303): capa de Al$_x$Ga$_{1-x}$As entre
dos capas de Al$_y$Ga$_{1-y}$As (índices controlados por la concentración de Al). Con
$\lambda_o=0.9\,\mu$m, $n_1=3.5$, $n_1-n_2=0.05$: para $d=10\,\mu$m hay $M=14$ modos TE; para
$d<0.76\,\mu$m, un solo modo. (Comprobación: NA $=\sqrt{3.5^2-3.45^2}\approx0.589$;
$2d\,\mathrm{NA}/\lambda_o=13.1\Rightarrow M=14$; monomodo si $2d\,\mathrm{NA}/\lambda_o<1
\Rightarrow d<0.764\,\mu$m.)

#### B. Field Distributions (p. 303–305)

**Internal Field** (p. 303). Dentro de la lámina: dos ondas TEM a $\pm\theta_m$ con componentes
$(0,\pm n_1k_o\sin\theta_m,n_1k_o\cos\theta_m)$, igual amplitud y desfase $m\pi$ (mitad del de
ida y vuelta) en el centro. $E_x(y,z)=\mathsf{a}_mu_m(y)\exp(-j\beta_m z)$, $\beta_m=n_1k_o\cos\theta_m$:

$$u_m(y)\propto\begin{cases}\cos\!\left(2\pi\dfrac{\sin\theta_m}{\lambda}y\right), & m=0,2,4,\dots\\[2ex]
\sin\!\left(2\pi\dfrac{\sin\theta_m}{\lambda}y\right), & m=1,3,5,\dots\end{cases}\qquad -\frac{d}{2}\le y\le\frac{d}{2}, \tag{8.2-10}$$

$\lambda=\lambda_o/n_1$. Aunque es armónico, **no se anula en la frontera**. Modos superiores
varían más rápido en $y$. (Ojo: aquí los **pares** son coseno — al revés que en la guía de
espejos, porque $m$ empieza en 0.)

**External Field** (p. 303–304). Debe empalmar con el interno en $y=\pm d/2$, luego varía en
$z$ como $\exp(-j\beta_m z)$. Sustituyendo en la ec. de Helmholtz $(\nabla^2+n_2^2k_o^2)E_x=0$:

$$\frac{d^2u_m}{dy^2}-\gamma_m^2u_m=0, \tag{8.2-11}$$

$$\gamma_m^2=\beta_m^2-n_2^2k_o^2. \tag{8.2-12}$$

Como $\beta_m>n_2k_o$ para modos guiados, $\gamma_m^2>0$; se elige la solución que decae:

$$u_m(y)\propto\begin{cases}\exp(-\gamma_my), & y>d/2\\ \exp(\gamma_my), & y<-d/2.\end{cases} \tag{8.2-13}$$

$\gamma_m$ = **coeficiente de extinción**; la onda es **evanescente**. Con $\beta_m=n_1k_o\cos\theta_m$
y $\cos\bar\theta_c=n_2/n_1$ (recuadro, p. 304):

$$\boxed{\gamma_m=n_2k_o\sqrt{\frac{\cos^2\theta_m}{\cos^2\bar\theta_c}-1}} \tag{8.2-14}$$

Al crecer $m$, crece $\theta_m$ y **decrece $\gamma_m$**: los modos de orden superior penetran
más en cover y sustrato. Las constantes de (8.2-10) y (8.2-13) se fijan empalmando en $y=d/2$
y normalizando:

$$\int_{-\infty}^{\infty}u_m^2(y)\,dy=1, \tag{8.2-15}$$

$$\int_{-\infty}^{\infty}u_m(y)\,u_l(y)\,dy=0,\qquad l\neq m. \tag{8.2-16}$$

(Fig. 8.2-5, p. 304: perfiles TE $m=0,1,2,3,8$ con colas evanescentes; comparar con 8.1-4.)
Campo TE arbitrario (p. 305):

$$E_x(y,z)=\sum_m\mathsf{a}_mu_m(y)\exp(-j\beta_mz). \tag{8.2-17}$$

**Ejercicio 8.2-1, Confinement Factor** (p. 305): el factor de confinamiento de potencia es

$$\Gamma_m=\frac{\int_0^{d/2}u_m^2(y)\,dy}{\int_0^{\infty}u_m^2(y)\,dy}. \tag{8.2-18}$$

Derivar $\Gamma_m$ en función de $\theta_m$ y $d/\lambda$; demostrar que el modo de menor
orden (menor $\theta_m$) tiene el mayor confinamiento.

Modos **TM** (p. 305, Fig. 8.2-6): la componente $z$ de E (paralela a la frontera) se comporta
como la $x$ del TE; se parte de $E_z(y,z)$ y de ahí $E_y$, $H_x$ (o directamente de Maxwell).

Comparación con el **haz gaussiano** (p. 305, Fig. 8.2-7): el modo TE$_0$ tiene forma parecida
a la gaussiana, pero la luz guiada **no se ensancha** al propagarse: la tendencia a difractar
se compensa con el guiado.

#### C. Dispersion Relation and Group Velocities (p. 306–308)

Se escribe (8.2-2) en términos de $\beta$ y $\omega$ con $k_y^2=(\omega/c_1)^2-\beta^2$:

$$2d\sqrt{\frac{\omega^2}{c_1^2}-\beta^2}=2\varphi_r+2\pi m. \tag{8.2-19}$$

Con $\cos\theta=\beta/(\omega/c_1)$ y $\cos\bar\theta_c=n_2/n_1=c_1/c_2$, (8.2-3) queda

$$\tan^2\frac{\varphi_r}{2}=\frac{\beta^2-\omega^2/c_2^2}{\omega^2/c_1^2-\beta^2}. \tag{8.2-20}$$

Sustituyendo (recuadro, p. 306), **relación de dispersión**:

$$\boxed{\tan^2\!\left(\frac{d}{2}\sqrt{\frac{\omega^2}{c_1^2}-\beta^2}-m\frac{\pi}{2}\right)=\frac{\beta^2-\omega^2/c_2^2}{\omega^2/c_1^2-\beta^2}} \tag{8.2-21}$$

Forma paramétrica en términos del **índice efectivo $n$** ($\beta=n\omega/c_o$):

$$\frac{\omega}{\omega_c}=\frac{\sqrt{n_1^2-n_2^2}}{\sqrt{n_1^2-n^2}}\left(m+\frac{2}{\pi}\tan^{-1}\sqrt{\frac{n^2-n_2^2}{n_1^2-n^2}}\right),\qquad\beta=n\omega/c_o, \tag{8.2-22}$$

con $\omega_c/2\pi=c_o/2d\,\mathrm{NA}$ la frecuencia angular de corte modal. **Fig. 8.2-8(a)**
(p. 307): las curvas de dispersión de los modos TE $m=0,1,2,3$ están entre las **líneas de luz**
$\omega=c_2\beta$ y $\omega=c_1\beta$; cada modo $m$ nace sobre la línea $\omega=c_2\beta$ en
$\omega=m\omega_c$ y al subir la frecuencia se acerca a $\omega=c_1\beta$: **el índice efectivo
$n$ crece de $n_2$ a $n_1$** (mayor confinamiento a longitudes de onda cortas) (p. 306).

**Velocidad de grupo** $v=d\omega/d\beta$ = pendiente de la curva. **Fig. 8.2-8(b)** (p. 307):
al subir $\omega$ sobre el corte de cada modo, $v$ **decrece** desde su máximo $c_2$, alcanza
un mínimo ligeramente por debajo de $c_1$ y vuelve asintóticamente a $c_1$. Rango: de $c_2$ a
algo menos que $c_1$ (p. 306).

- **Dispersión modal**: en guía multimodo, los pulsos se ensanchan porque los modos tienen
  distintas velocidades (p. 306).
- **GVD (group velocity dispersion)**: en guía monomodo el pulso se ensancha por la
  dependencia de $v$ con la frecuencia. *"GVD occurs in waveguides even in the absence of
  material dispersion"*: es consecuencia de la dependencia de $\beta$ con la frecuencia,
  determinada por cómo el confinamiento depende de $\lambda$ (p. 306). Cada modo tiene una
  frecuencia donde $v$ es mínima ($dv/d\omega=0$): allí el **coeficiente de GVD es cero** y el
  ensanchamiento es despreciable (p. 307).

Expresión aproximada de $v$: derivada total de (8.2-19) respecto a $\beta$ (p. 307):

$$\frac{2d}{2k_y}\left(\frac{2\omega}{c_1^2}\frac{d\omega}{d\beta}-2\beta\right)=2\frac{\partial\varphi_r}{\partial\beta}+2\frac{\partial\varphi_r}{\partial\omega}\frac{d\omega}{d\beta}. \tag{8.2-23}$$

Con $d\omega/d\beta=v$, $k_y/(\omega/c_1)=\sin\theta$, $k_y/\beta=\tan\theta$ y los parámetros

$$\Delta z=\frac{\partial\varphi_r}{\partial\beta},\qquad\Delta\tau=-\frac{\partial\varphi_r}{\partial\omega}, \tag{8.2-24}$$

$$v=\frac{d\cot\theta+\Delta z}{d\csc\theta/c_1+\Delta\tau}. \tag{8.2-25}$$

Interpretación (p. 307–308, Fig. 8.2-9): frente a la guía de espejos ($v=c_1\cos\theta$), el
rayo recorre una distancia adicional $\Delta z=\partial\varphi_r/\partial\beta$ que tarda
$\Delta\tau=-\partial\varphi_r/\partial\omega$: penetración efectiva en el cladding o
desplazamiento lateral del rayo = **efecto Goos–Hänchen** (Prob. 6.2-7). Se puede mostrar que
$\Delta z/\Delta\tau=\omega/\beta=c_1/\cos\theta$.

**Ejercicio 8.2-2, The Asymmetric Planar Waveguide** (p. 308, Fig. 8.2-10): lámina de ancho
$d$ e índice $n_1$ sobre sustrato $n_2$ y cubierta $n_3<n_2<n_1$. (a) Ángulo máximo de
inclinación con reflexión interna total y la NA correspondiente; (b) condición de
autoconsistencia análoga a (8.2-4); (c) expresión aproximada de $M$ (válida para $M$ grande).

---

### 8.3 Two-Dimensional Waveguides (p. 308)

Las guías planas confinan en una dirección transversal ($y$); las 2D confinan en $x$ y $y$.
Mismo principio y estructura modal, descripción matemática más larga; detalles en libros
especializados; cap. 9 = fibra (ejemplo 2D cilíndrico).

#### Rectangular Mirror Waveguide (p. 308–309)

Sección cuadrada de lado $d$ con paredes espejo. Onda plana $(k_x,k_y,k_z)$ autoconsistente si

$$2k_xd=2\pi m_x,\quad m_x=1,2,\dots;\qquad 2k_yd=2\pi m_y,\quad m_y=1,2,\dots \tag{8.3-1}$$

(generalización de (8.1-3)). $\beta=k_z$ de $k_x^2+k_y^2+\beta^2=n^2k_o^2$; cada modo tiene dos
índices $(m_x,m_y)$, permitidos mientras $k_x^2+k_y^2\le n^2k_o^2$ (Fig. 8.3-1, p. 309: retícula
de puntos espaciados $\pi/d$ dentro del cuarto de círculo de radio $nk_o$). Contando puntos
(área $\pi(nk_o)^2/4$ sobre celda $(\pi/d)^2$):

$$M\approx\frac{\pi}{4}\left(\frac{2d}{\lambda}\right)^2. \tag{8.3-2}$$

Con dos polarizaciones, total $2M$. Frente al caso 1D ($M\approx2d/\lambda$), añadir una
dimensión eleva al cuadrado el número de modos (= grados de libertad, se multiplican). Las
distribuciones de campo son productos de patrones tipo Fig. 8.1-4 en $x$ y en $y$ (p. 309).

#### Rectangular Dielectric Waveguide (p. 309–310)

Cilindro dieléctrico $n_1$ de sección cuadrada $d$ en medio $n_2$ ligeramente menor. Condición
$k_x^2+k_y^2\le n_1^2k_o^2\sin^2\bar\theta_c$, $\bar\theta_c=\cos^{-1}(n_2/n_1)$ (Fig. 8.3-2,
p. 310). Los $k_x,k_y$ no son uniformes pero su separación *promedio* es $\pi/d$;
$M\approx(\pi/4)(n_1k_o\sin\bar\theta_c)^2/(\pi/d)^2$ (recuadro, p. 310):

$$\boxed{M\approx\frac{\pi}{4}\left(\frac{2d}{\lambda_o}\right)^2(\mathrm{NA})^2} \tag{8.3-3}$$

**Número de modos TE** (aprox. válida si $M$ grande); igual número $M$ de modos TM; es
aproximadamente el cuadrado de (8.2-7).

#### Geometries of Channel Waveguides (p. 310–311)

Fig. 8.3-3 (p. 310): **embedded strip**, **strip**, **rib or ridge**, **strip loaded** (más
oscuro = mayor índice). El análisis exacto no es fácil; se usan aproximaciones. Fig. 8.3-4
(p. 311) configuraciones: straight, **S bend** (desplaza el eje), **Y branch** (divisor/combinador;
dos Y = **Mach–Zehnder**), **directional coupler** (dos guías próximas intercambian potencia,
§8.5), **intersection**.

#### Materials (p. 311)

- **Ti:LiNbO₃**: tecnología más avanzada; strip embebido por difusión de Ti en niobato de
  litio (sube el índice localmente). Fig. 8.3-5.
- **GaAs/AlGaAs**: strips de GaAs con capas de AlGaAs de menor índice. **InP** gana
  importancia. Vidrio: intercambio iónico. Polímeros: tecnología emergente.
- **SOI (silicon-on-insulator, Si–SiO₂)**, también llamada *silica-on-silicon*: índice del
  silicio ~3.5 y de la sílice <1.5 ⇒ gran $\Delta n$. Típico: rib de Si sobre capa de sílice
  (cladding) sobre sustrato de Si (Fig. 8.3-5). Compatibilidad CMOS = ventaja clave. (El libro
  dice textualmente "the refractive index of silica is ~3.5 and that of silica is less than
  1.5" — errata evidente: el primero es *silicon*.)
- Modular el índice (electro-óptica) es requisito para moduladores y conmutadores (caps. 20,
  23).

---

### 8.4 Photonic-Crystal Waveguides (p. 311)

#### Bragg-Grating Waveguide (p. 311–312)

Alternativa a espejos y a RIT: **reflectores de rejilla de Bragg (BGR)** (§7.1C): pila de
capas dieléctricas alternadas con reflectancia dependiente de ángulo y frecuencia (≈1 dentro
de una banda prohibida / rango angular; también reflexión omnidireccional). Dentro del rango
angular, la autoconsistencia se cumple en un conjunto discreto de ángulos = modos. El campo se
confina principalmente a la lámina con colas evanescentes en las capas (Fig. 8.4-1, p. 312).

#### Bragg-Grating Waveguide as a Photonic Crystal with a Defect Layer (p. 312)

Si las rejillas superior e inferior son idénticas y el espesor de la lámina es comparable al
de las capas, todo es un cristal fotónico 1D con un **defecto** (la lámina, de espesor y/o
índice distinto). Un cristal perfecto tiene bandgaps sin modos propagantes (§7.2); con el
defecto aparece un modo con frecuencia dentro del bandgap, confinado a la capa (Fig. 8.4-2,
p. 312: "defect level" dentro del "photonic bandgap"), análogo a un nivel de defecto en el gap
de un semiconductor.

#### 2D Photonic-Crystal Waveguides (p. 312–313)

Camino de defectos en un cristal 2D: cristal de agujeros cilíndricos en red triangular con
bandgap completo para propagación en el plano de periodicidad; la guía es una línea de
agujeros ausentes. Luz a frecuencias del bandgap no se fuga al medio periódico (Fig. 8.4-3(a),
p. 313). Por la omnidireccionalidad del bandgap, se guía con **curvas y esquinas abruptas** sin
perder energía (guía en L, Fig. 8.4-3(b)), imposible con guías por RIT (p. 313).

---

### 8.5 Optical Coupling in Waveguides (p. 313)

#### A. Input Couplers (p. 313–315)

**Mode Excitation** (p. 313–314). Campo general:

$$E(y,z)=\sum_m\mathsf{a}_mu_m(y)\exp(-j\beta_mz), \tag{8.5-1}$$

$u_m(y)$ real. Las amplitudes dependen de la fuente: si su distribución $s(y)$ coincide con un
modo, solo ese modo se excita; en general excita varios. Expansión en las funciones ortogonales:

$$s(y)=\sum_m\mathsf{a}_mu_m(y), \tag{8.5-2}$$

$$\mathsf{a}_l=\int_{-\infty}^{\infty}s(y)\,u_l(y)\,dy. \tag{8.5-3}$$

(Se obtiene multiplicando (8.5-2) por $u_l$, integrando y usando ortogonalidad +
normalización.) $\mathsf{a}_l$ = grado de similitud (correlación) entre $s(y)$ y $u_l(y)$ (p. 314).

**Input Couplers** (p. 314–315). Enfoque directo en el extremo (Fig. 8.5-1): la distribución
transversal y la polarización de la luz incidente deben coincidir con las del modo; por las
dimensiones pequeñas, enfoque y alineación son difíciles y el acoplamiento es ineficiente. En
guía multimodo, visión de rayos (Fig. 8.5-2): los rayos guiados están dentro de
$\bar\theta_c=\cos^{-1}(n_2/n_1)$; por refracción en la entrada corresponde al ángulo externo
$\theta_a$ con $\mathrm{NA}=\sin\theta_a=n_1\sin\bar\theta_c=n_1\sqrt{1-(n_2/n_1)^2}=\sqrt{n_1^2-n_2^2}$
(Ejercicio 1.2-5); enfocar dentro de $\theta_a$ para máxima eficiencia. **Acoplamiento a tope
(end butt coupling)** desde LED o diodo láser alineando los extremos con un pequeño espacio
(Fig. 8.5-3, p. 315); el LED emite en todas direcciones, el láser ya está confinado en su
propia guía (cap. 17).

**Prism and Grating Side Couplers** (p. 315, Fig. 8.5-4). Para acoplar una onda que entra por el
costado a ángulo $\theta_i$ en el cladding se requiere que la componente axial del vector de
onda $n_2k_o\cos\theta_i$ iguale a $\beta_m$ (**phase matching**). Como $\beta_m>n_2k_o$, es
imposible directamente (la componente axial es demasiado pequeña).
- **Prisma** de índice $n_p>n_2$ a distancia $d_p$ de la lámina: la onda refracta al prisma,
  sufre RIT a ángulo $\theta_p$; incidente + reflejada forman una onda en $z$ con
  $\beta_p=n_pk_o\cos\theta_p$ cuyo campo evanescente llena el espacio prisma–lámina; si $d_p$
  es pequeño se acopla al modo con $\beta_m\approx\beta_p=n_pk_o\cos\theta_p$ (posible porque
  $n_p>n_2$). Reversible como acoplador de salida.
- **Rejilla** de periodo $\Lambda$: modula la onda con factores de fase $2\pi qz/\Lambda$,
  $q=\pm1,\pm2,\dots$ (cambios $2\pi q/\Lambda$ en la componente axial). Condición:
  $n_2k_o\cos\theta_i+2\pi q/\Lambda=\beta_m$, p. ej. $q=1$; la rejilla puede diseñarse para
  realzar $q=1$.

#### B. Coupled Waveguides (p. 315–320)

Dos guías suficientemente próximas (campos solapados) intercambian potencia → acopladores y
conmutadores (caps. 23, 24). Sistema (Fig. 8.5-5, p. 316): dos láminas de ancho $d$, separación
$2a$, índices $n_1$ y $n_2$, en medio de índice $n$ ligeramente menor; cada guía monomodo; el
campo externo de una solapa ligeramente la otra. El enfoque exacto (modos del sistema completo,
distintos de los de cada guía) está fuera del alcance; para acoplamiento débil se usa la
**teoría de modos acoplados**: los modos de cada guía son los que tendrían aisladas,
$u_1(y)\exp(-j\beta_1z)$ y $u_2(y)\exp(-j\beta_2z)$; el acoplamiento solo modifica las
**amplitudes** $\mathsf{a}_1(z)$, $\mathsf{a}_2(z)$, no las distribuciones ni las $\beta$.
Visión de dispersión: el campo de la guía 1 se dispersa en la guía 2 creando una fuente que
cambia la amplitud allí, y viceversa (p. 316). **Ecuaciones de modos acoplados** (recuadro,
p. 316):

$$\boxed{\begin{aligned}\frac{d\mathsf{a}_1}{dz}&=-j\mathcal{C}_{21}\exp(j\,\Delta\beta\,z)\,\mathsf{a}_2(z)\\
\frac{d\mathsf{a}_2}{dz}&=-j\mathcal{C}_{12}\exp(-j\,\Delta\beta\,z)\,\mathsf{a}_1(z)\end{aligned}} \tag{8.5-4a,b}$$

$$\Delta\beta=\beta_1-\beta_2 \tag{8.5-5}$$

= desajuste de fase por unidad de longitud. **Coeficientes de acoplamiento** (p. 317):

$$\mathcal{C}_{21}=\tfrac12\left(n_2^2-n^2\right)\frac{k_o^2}{\beta_1}\int_a^{a+d}u_1(y)\,u_2(y)\,dy,\qquad
\mathcal{C}_{12}=\tfrac12\left(n_1^2-n^2\right)\frac{k_o^2}{\beta_2}\int_{-a-d}^{-a}u_2(y)\,u_1(y)\,dy. \tag{8.5-6}$$

(La integral se extiende sobre la lámina de la *otra* guía: $\mathcal{C}_{21}$ sobre la lámina
2 en $[a,a+d]$, $\mathcal{C}_{12}$ sobre la lámina 1 en $[-a-d,-a]$.) La tasa de variación de
$\mathsf{a}_1$ es proporcional a $\mathsf{a}_2$ y viceversa; el factor es coeficiente de
acoplamiento × factor de desajuste $\exp(j\Delta\beta z)$.

**Solución** (multiplicar (8.5-4a) por $\exp(-j\Delta\beta z)$, derivar, sustituir (8.5-4b),
resolver la EDO de 2.º orden) (p. 317):

$$\mathsf{a}_1(z)=A(z)\mathsf{a}_1(0)+B(z)\mathsf{a}_2(0),\qquad\mathsf{a}_2(z)=C(z)\mathsf{a}_1(0)+D(z)\mathsf{a}_2(0), \tag{8.5-7a,b}$$

$$A(z)=D^*(z)=\exp\!\left(\frac{j\,\Delta\beta\,z}{2}\right)\left(\cos\gamma z-j\frac{\Delta\beta}{2\gamma}\sin\gamma z\right) \tag{8.5-8a}$$

$$B(z)=\frac{\mathcal{C}_{21}}{j\gamma}\exp\!\left(j\frac{\Delta\beta\,z}{2}\right)\sin\gamma z \tag{8.5-8b}$$

$$C(z)=\frac{\mathcal{C}_{12}}{j\gamma}\exp\!\left(-j\frac{\Delta\beta\,z}{2}\right)\sin\gamma z \tag{8.5-8c}$$

elementos de la **matriz de transmisión $\mathbf{T}$** (salida en función de la entrada), con

$$\gamma^2=\left(\frac{\Delta\beta}{2}\right)^2+\mathcal{C}^2,\qquad\mathcal{C}=\sqrt{\mathcal{C}_{12}\mathcal{C}_{21}}. \tag{8.5-9}$$

Si $\mathsf{a}_2(0)=0$ (no entra luz por la guía 2), con $P_1\propto|\mathsf{a}_1|^2$,
$P_2\propto|\mathsf{a}_2|^2$ (recuadro, p. 317):

$$\boxed{\begin{aligned}P_1(z)&=P_1(0)\left[\cos^2\gamma z+\left(\frac{\Delta\beta}{2\gamma}\right)^2\sin^2\gamma z\right]\\
P_2(z)&=P_1(0)\frac{|\mathcal{C}_{21}|^2}{\gamma^2}\sin^2\gamma z\end{aligned}} \tag{8.5-10a,b}$$

La potencia se intercambia **periódicamente** con periodo $\pi/\gamma$ (Fig. 8.5-6(a), p. 318:
caso desajustado, transferencia incompleta).

**Guías idénticas / phase matched** ($n_1=n_2$, $\beta_1=\beta_2$, $\Delta\beta=0$): $\gamma=\mathcal{C}$,
$\mathcal{C}_{12}=\mathcal{C}_{21}=\mathcal{C}$ (p. 318):

$$\mathbf{T}=\begin{bmatrix}A(z)&B(z)\\C(z)&D(z)\end{bmatrix}=\begin{bmatrix}\cos\mathcal{C}z&-j\sin\mathcal{C}z\\-j\sin\mathcal{C}z&\cos\mathcal{C}z\end{bmatrix}, \tag{8.5-11}$$

$$\boxed{P_1(z)=P_1(0)\cos^2\mathcal{C}z,\qquad P_2(z)=P_1(0)\sin^2\mathcal{C}z} \tag{8.5-12a,b}$$

Intercambio **completo** (Fig. 8.5-6(b)). Resultados clave (p. 318, Fig. 8.5-7):
- **Longitud de acoplamiento / distancia de transferencia**: $L_0=\pi/2\mathcal{C}$ — toda la
  potencia pasa de la guía 1 a la 2.
- A $L_0/2$ se transfiere la mitad: **acoplador 3 dB** (divisor 50/50).
- Se puede acoplar cualquier fracción deseada eligiendo la longitud.

**Switching by Control of Phase Mismatch** (p. 319). Acoplador de longitud fija $L_0=\pi/2\mathcal{C}$;
con desajuste $\Delta\beta$, usando (8.5-10b) y (8.5-9), la **razón de transferencia de potencia**
$\mathcal{T}=P_2(L_0)/P_1(0)$ (recuadro):

$$\boxed{\mathcal{T}=\frac{\pi^2}{4}\,\mathrm{sinc}^2\!\left[\frac12\sqrt{1+\left(\frac{\Delta\beta\,L_0}{\pi}\right)^2}\right]} \tag{8.5-13}$$

con $\mathrm{sinc}(x)=\sin(\pi x)/(\pi x)$. $\mathcal{T}=1$ en $\Delta\beta L_0=0$, decrece y se
**anula en $\Delta\beta L_0=\sqrt{3}\,\pi$** (Fig. 8.5-8, p. 319). Conmutando $\Delta\beta L_0$
entre 0 y $\sqrt3\pi$ la luz pasa de la guía 2 a la 1 → **acoplador direccional activado
eléctricamente** si el material es electro-óptico (caps. 20, 23).

**\*Derivation of the Coupled Wave Equations** (p. 319–320, sección avanzada). Sin interacción:

$$E_1(y,z)=\mathsf{a}_1u_1(y)\exp(-j\beta_1z),\qquad E_2(y,z)=\mathsf{a}_2u_2(y)\exp(-j\beta_2z). \tag{8.5-14a,b}$$

Con acoplamiento, $\mathsf{a}_1,\mathsf{a}_2$ dependen de $z$ (lentamente respecto a $\beta^{-1}$,
~longitud de onda), $u_{1,2}$ y $\beta_{1,2}$ no cambian. La guía 2 se ve como perturbación del
medio fuera de la guía 1: lámina de índice $n_2-n$, ancho $d$, a distancia $2a$. El exceso de
índice y el campo $E_2$ dan una **polarización en exceso** $P=(\epsilon_2-\epsilon)E_2=\epsilon_o(n_2^2-n^2)E_2$
que es fuente de radiación en la guía 1 [ec. (5.2-25)] $\mathcal{S}_1=-\mu_o\partial^2\mathcal{P}/\partial t^2$,
de amplitud compleja

$$S_1=\mu_o\omega^2P=\mu_o\omega^2\epsilon_o(n_2^2-n^2)E_2=(n_2^2-n^2)k_o^2E_2=(k_2^2-k^2)E_2, \tag{8.5-15}$$

$k_2=n_2k_o$; fuente presente solo en la lámina 2. Helmholtz con fuente:

$$\nabla^2E_1+k_1^2E_1=-S_1=-(k_2^2-k^2)E_2, \tag{8.5-16a}$$

$$\nabla^2E_2+k_2^2E_2=-S_2=-(k_1^2-k^2)E_1, \tag{8.5-16b}$$

$k_1=n_1k_o$. Válido solo para **acoplamiento débil**. Con $E_1=\mathsf{a}_1(z)e_1(y,z)$,
$E_2=\mathsf{a}_2(z)e_2(y,z)$, $e_1=u_1(y)\exp(-j\beta_1z)$, $e_2=u_2(y)\exp(-j\beta_2z)$, que cumplen

$$\nabla^2e_1+k_1^2e_1=0,\qquad\nabla^2e_2+k_2^2e_2=0, \tag{8.5-17a,b}$$

($k_1=n_1k_o$, $k_2=n_2k_o$ dentro de cada lámina, $k_1=k_2=nk_o$ fuera). Sustituyendo en (8.5-16a):

$$\frac{d^2\mathsf{a}_1}{dz^2}e_1+2\frac{d\mathsf{a}_1}{dz}\frac{de_1}{dz}=-(k_2^2-k^2)\mathsf{a}_2e_2. \tag{8.5-18}$$

(Así aparece impreso en p. 320: el signo "=" entre el primer y el segundo término es una
errata evidente por "+".) **Aproximación de amplitud lentamente variable**: se desprecia
$d^2\mathsf{a}_1/dz^2\,e_1$ frente a $2(d\mathsf{a}_1/dz)(de_1/dz)$; el cociente es
$j(d\Psi/\Psi)/2\beta_1dz$ con $\Psi=d\mathsf{a}_1/dz$, válido si $d\Psi/\Psi\ll\beta_1dz$. Queda

$$2\frac{d\mathsf{a}_1}{dz}(-j\beta_1)u_1(y)e^{-j\beta_1z}=-(k_2^2-k^2)\mathsf{a}_2u_2(y)e^{-j\beta_2z}. \tag{8.5-19}$$

Multiplicando por $u_1(y)$, integrando en $y$ y usando $\int u_1^2=1$:

$$\frac{d\mathsf{a}_1}{dz}e^{-j\beta_1z}=-j\mathcal{C}_{21}\mathsf{a}_2(z)e^{-j\beta_2z}, \tag{8.5-20}$$

con $\mathcal{C}_{21}$ de (8.5-6). Repitiendo para la guía 2 se obtienen (8.5-4). ■

#### C. Periodic Waveguides (p. 320–321)

La teoría de dos guías acopladas se generaliza en principio a múltiples guías (ecuaciones
difíciles). En el límite de muchas láminas idénticas equiespaciadas se aplica la teoría de
medios periódicos (§7.2). **Fig. 8.5-9** (p. 321) compara: (a) guía de lámina simple, con
frecuencia angular de corte $\omega_c=(\pi/d)(c_o/\mathrm{NA})$, modos como líneas entre
$\omega=c_1\beta$ y $\omega=c_2\beta$, siempre al menos un modo; (b) guía periódica con
frecuencia angular de Bragg $\omega_\mathcal{B}=(\pi/\Lambda)(c_o/\bar n)$, líneas de dispersión
rotas en bandas separadas por bandgaps fotónicos (modos propagándose paralelos a las capas,
también entre las líneas de luz).

---

### 8.6 Sub-Wavelength Metal Waveguides (Plasmonics) (p. 321–322)

Es difícil confinar luz a dimensiones ≪ λ con dieléctricos (ver §4.4D): la guía de espejos no
guía si $d<\lambda/2$ (frecuencia bajo el corte $c/2d$); la lámina dieléctrica con $d<\lambda/2$
es monomodo y al reducir más $d$ hay fuga sustancial al cladding. Con estructuras metálicas
sub-λ (películas delgadas, nanopartículas en dieléctrico) sí se puede: **plasmónica** (p. 321).

- Metal bulk (§5.5D): bajo la frecuencia de plasma la onda decae con atenuación que disminuye
  con la frecuencia y se anula en la frecuencia de plasma; los electrones libres oscilan
  longitudinalmente (**plasmones**). El metal bulk no guía.
- Interfaz metal–dieléctrico: Maxwell admite ondas de densidad de carga acopladas a ondas
  ópticas = **plasmones-polaritones de superficie (SPP)**; campo confinado a dimensiones sub-λ
  cerca de la superficie; se excitan bajo la frecuencia de plasma y se localizan más cerca
  de ella. Permiten controlar luz a escala nanométrica conservando la frecuencia óptica
  (p. 322).
- **Guías SPP**: lámina dieléctrica con claddings metálicos, suficientemente delgada para que
  los SPP de ambas interfaces se solapen; relación de dispersión por condiciones de frontera
  con modelo de Drude (§5.5D). Láminas delgadas ⇒ $\beta$ grandes aun muy por debajo de la
  frecuencia de plasma. Heteroestructuras **MIM (metal/insulator/metal)** submicrométricas;
  modos en IR cercano localizados a escala nm, pero **la longitud de propagación es limitada**.
- **Metamateriales** (§5.7): arreglos de nanopartículas metálicas próximas con campos
  plasmónicos solapados; modos guiados de tamaño submicrométrico a la frecuencia del plasmón
  de partícula o de la resonancia del gap entre partículas.
- Plasmónica une la electrónica integrada (<100 nm) con la fotónica óptica (>100 THz).
  Aplicaciones en **nano-óptica**: interconexiones intra-chip, transmisión por agujeros
  nano en objetos opacos, fuentes puntuales distribuidas en superficies metalizadas,
  nanoantenas, nanoresonadores, nanoguías análogas a circuitos eléctricos a frecuencias
  visibles. **Biosensado**: la sensibilidad de las excitaciones plasmónicas a las propiedades
  del dieléctrico que rodea la nanoestructura metálica permite medir espesor de películas
  coloidales y detectar/cuantificar unión de proteínas (p. 322).

---

### Reading List (p. 322–323)

Libros (selección): C.-L. Chen, *Foundations for Guided Wave Optics* (Wiley 2006); Iga &
Kokubun, *Encyclopedic Handbook of Integrated Optics* (CRC 2006); K. Okamoto, *Fundamentals of
Optical Waveguides* (Elsevier, 2.ª ed. 2005); B. P. Pal (ed.), *Guided Wave Optical Components
and Devices* (Academic 2005); Reed & Knights, *Silicon Photonics* (Wiley 2004); G. Lifante,
*Integrated Photonics: Fundamentals* (Wiley 2003); Pollock & Lipson, *Integrated Photonics*
(Kluwer 2003); Barybin & Dmitriev, *Modern Electrodynamics and Coupled-Mode Theory* (Rinton
2002); Hunsperger, *Integrated Optics: Theory and Technology* (Springer, 5.ª ed. 2002);
Iizuka, *Elements of Photonics*, vol. 2 (Wiley 2002); Coldren & Corzine, *Diode Lasers and
Photonic Integrated Circuits* (Wiley 1995); Marcuse, *Theory of Dielectric Optical Waveguides*
(Academic, 2.ª ed. 1991); Tamir (ed.), *Guided-Wave Optoelectronics* (Springer, 2.ª ed. 1990);
Nishihara, Haruna & Suhara, *Optical Integrated Circuits* (McGraw-Hill 1989), entre otros.
Artículos: números especiales de *IEEE J. Sel. Top. Quantum Electron.* (nanofotónica 2006;
óptica integrada 2005, 2000); Paniccia & Koehl, "The Silicon Solution", *IEEE Spectrum* 42(10),
38–43 (2005); D. G. Hall (ed.), *Selected Papers on Coupled Mode Theory in Guided-Wave Optics*,
SPIE Milestone 84 (1993).

---

## Tablas y datos numéricos útiles

| Magnitud | Valor / expresión | Página |
|---|---|---|
| Desfase por reflexión en espejo perfecto (E paralelo) | $\pi$ | 292 |
| Guía de espejos: $\lambda_c=2d$, $\nu_c=c/2d$, $\omega_c=\pi c/d$ | ejemplo $d=5\,\mu$m ⇒ $\lambda_c=10\,\mu$m | 295 |
| Guía de espejos: monomodo si $d\le\lambda<2d$ | — | 295 |
| Guía dieléctrica: $\bar\theta_c=\cos^{-1}(n_2/n_1)$, NA $=\sqrt{n_1^2-n_2^2}$ | — | 299, 302 |
| Ejemplo vidrio: $d/\lambda_o=10$, $n_1=1.47$, $n_2=1.46$ | $\bar\theta_c=6.7^\circ$, NA $=0.171$, $M=4$ TE | 302 |
| Ejemplo 8.2-1 AlGaAs: $\lambda_o=0.9\,\mu$m, $n_1=3.5$, $n_1-n_2=0.05$ | $d=10\,\mu$m ⇒ $M=14$; monomodo si $d<0.76\,\mu$m | 303 |
| Fig. 8.2-2: $\sin\bar\theta_c=8(\lambda/2d)$ | $M=9$ | 300 |
| Rango de $\beta_m$ en guía dieléctrica | $n_2k_o<\beta_m<n_1k_o$; índice efectivo $n_2<n<n_1$ | 301, 306 |
| Rango de $v$ (grupo) en guía dieléctrica | de $c_2$ (en el corte) a algo < $c_1$; vuelve a $c_1$ | 306 |
| Guía 2D de espejos / dieléctrica | $M\approx(\pi/4)(2d/\lambda)^2$ ; $M\approx(\pi/4)(2d/\lambda_o)^2\mathrm{NA}^2$ | 309, 310 |
| Índices SOI | Si ≈ 3.5, sílice < 1.5 | 311 |
| Longitud de acoplamiento | $L_0=\pi/2\mathcal{C}$; 3 dB en $L_0/2$ | 318 |
| Periodo de intercambio de potencia (desajustado) | $\pi/\gamma$, $\gamma=\sqrt{(\Delta\beta/2)^2+\mathcal{C}^2}$ | 317 |
| Apagado total de transferencia | $\Delta\beta L_0=\sqrt3\,\pi$ | 319 |
| Plasmónica: escalas | electrónica < 100 nm; fotónica > 100 THz | 322 |
| Problemas: $\lambda_o=0.633$, 0.85, 0.87, 1.3 $\mu$m; $n$ = 1.46, 1.48, 1.50, 1.6, 1.4 | ver lista | 324 |

Ángulos de corte de modos de la guía dieléctrica (de (8.2-22) con $n\to n_2$): el modo $m$
aparece en $\omega=m\omega_c$, $\omega_c=2\pi c_o/(2d\,\mathrm{NA})$ (p. 306–307).

---

## Problemas al final del capítulo (p. 323–324)

Ninguno está marcado con * en el libro; el único material marcado como avanzado (*) en el
capítulo es la "Derivation of the Coupled Wave Equations" (p. 319). Los ejercicios dentro del
texto (8.1-1, 8.1-2, 8.2-1, 8.2-2) están listados en sus secciones.

- **8.1-3 Field Distribution.** (a) Demostrar que una sola onda plana TEM
  $E_x(y,z)=A\exp(-jk_yy)\exp(-j\beta z)$ no puede cumplir $E_x(\pm d/2,z)=0$ en la guía de
  espejos. (b) Mostrar que la suma de dos ondas TEM $A_1\exp(-jk_{y1}y)\exp(-j\beta_1z)+A_2\exp(-jk_{y2}y)\exp(-j\beta_2z)$
  no cumple las condiciones de frontera si $A_1=\pm A_2$, $\beta_1=\beta_2$, $k_{y1}=-k_{y2}=m\pi/d$,
  $m=1,2,\dots$ (p. 323–324).
- **8.1-4 Modal Dispersion.** $\lambda_o=0.633\,\mu$m en guía de espejos con $d=10\,\mu$m,
  $n=1$: número de modos TE y TM; velocidades de grupo del modo más rápido y más lento;
  ensanchamiento de un pulso estrecho tras 1 m si se excitan todos los modos.
- **8.2-3 Parameters of a Dielectric Waveguide.** $\lambda_o=0.87\,\mu$m, $d=2\,\mu$m,
  $n_1=1.6$, $n_2=1.4$: (a) $\theta_c$, $\bar\theta_c$, NA y ángulo máximo de aceptación desde
  aire; (b) número de modos TE; (c) ángulo de rebote $\theta$ y velocidad de grupo $v$ del
  modo TE $m=0$.
- **8.2-4 Effect of Cladding.** Repetir 8.2-3 con la película suspendida en aire ($n_2=1$);
  comparar.
- **8.2-5 Field Distribution.** Con (8.2-10) y (8.2-13), derivar la razón de las constantes de
  proporcionalidad; graficar $u_0(y)$ para $n_1=1.48$, $n_2=1.46$, $d=0.5\,\mu$m,
  $\lambda_o=0.85\,\mu$m, y hallar su factor de confinamiento (porcentaje de potencia en la
  lámina).
- **8.2-6 Derivation of the Field Distributions Using Maxwell's Equations.** Con
  $E_x=u(y)e^{-j\beta z}$, $u(y)=A\cos(k_yy+\varphi)$ en $|y|\le d/2$, $B\exp(\mp\gamma y)$ fuera;
  $k_y^2+\beta^2=n_1^2k_o^2$, $-\gamma^2+\beta^2=n_2^2k_o^2$. Derivar $H_y$, $H_z$ con Maxwell;
  mostrar que las condiciones de frontera se cumplen si $\beta,\gamma,k_y$ toman los valores
  $\beta_m,\gamma_m,k_{ym}$ del texto y verificar (8.2-4).
- **8.2-7 Single-Mode Waveguide.** Mayor espesor $d$ de una guía simétrica con $n_1=1.50$,
  $n_2=1.46$ para un solo modo TE a $\lambda_o=1.3\,\mu$m; número de modos de esa guía a
  $\lambda_o=0.85\,\mu$m.
- **8.2-8 Mode Cutoff.** Mostrar que la condición de corte del modo TE $m>0$ en guía simétrica
  con $n_1\approx n_2$ es aproximadamente $\lambda_c^2\approx8n_1\Delta n\,d^2/m^2$,
  $\Delta n=n_1-n_2$.
- **8.2-9 TM Modes.** Derivar la ecuación de ángulos de rebote de los modos TM (análoga a
  (8.2-4)); graficar con computador (tipo Fig. 8.2-2) para $\sin\bar\theta_c=0.3$ y
  $\lambda/2d=0.1$; número de modos TM.
- **8.3-1 Modes of a Rectangular Dielectric Waveguide.** Sección $10^{-2}$ mm², NA $=0.1$:
  usar (8.3-3) para graficar el número de modos TE vs. frecuencia $\nu$; comparar con
  Fig. 8.2-4.
- **8.4-1 Coupling Coefficient Between Two Slabs.** (a) Con (8.5-6), coeficiente de
  acoplamiento entre dos guías idénticas de $d=0.5\,\mu$m, separación $2a=1.0\,\mu$m,
  $n_1=n_2=1.48$, medio $n=1.46$, $\lambda_o=0.85\,\mu$m, ambas en el modo $m=0$ (usar los
  resultados de 8.2-5 para los perfiles). (b) Longitud para que el dispositivo sea un
  acoplador 3 dB. (Numerado "8.4-1" en el libro aunque corresponde a §8.5.)

---

## Relación con Óptica No Lineal

### Para el curso

- **Ondas EM y Helmholtz.** Todo el capítulo es aplicación de la ecuación de Helmholtz
  $(\nabla^2+n^2k_o^2)E=0$ con condiciones de frontera (p. 303, 320); la derivación de modos
  acoplados usa Helmholtz **con fuente** $\nabla^2E+k^2E=-S$, $S=\mu_o\omega^2P$, que es
  exactamente la estructura de la ecuación de onda no lineal del curso (la polarización no
  lineal $P_{NL}$ como término fuente, ec. (5.2-25) del libro). La aproximación de **amplitud
  lentamente variable** (despreciar $d^2\mathsf{a}/dz^2$, p. 320) es la misma SVEA que se usa
  para derivar las ecuaciones de ondas acopladas de SHG/SFG/DFG y la NLSE.
- **Phase matching.** Aparece dos veces: acopladores de prisma/rejilla
  ($n_2k_o\cos\theta_i+2\pi q/\Lambda=\beta_m$, p. 315: la rejilla aporta un vector $2\pi q/\Lambda$,
  idéntico en espíritu al **quasi-phase-matching** con $K=2\pi/\Lambda$ en χ⁽²⁾) y en modos
  acoplados: $\Delta\beta=\beta_1-\beta_2$ y la razón de transferencia (8.5-13) con
  $\mathrm{sinc}^2$ es el mismo tipo de dependencia que la eficiencia de SHG con
  $\mathrm{sinc}^2(\Delta kL/2)$.
- **Haz gaussiano.** El modo TE$_0$ se parece a una gaussiana pero no difracta (p. 305,
  Fig. 8.2-7): el guiado compensa la difracción; útil para contrastar con el auto-enfoque Kerr
  (donde la compensación es no lineal, por $n_2I$).
- **Pulsos en medios dispersivos / GVD.** Relación de dispersión $\beta(\omega)$ y velocidad de
  grupo $v=d\omega/d\beta$ (p. 296, 306); **la GVD existe aun sin dispersión material**
  (dispersión de guía, p. 306) y cada modo tiene una frecuencia de **GVD cero** (p. 307).
  Esto es la base para diseñar dispersión anómala/normal en guías para solitones y SPM.
- **Polarización TE/TM.** Las fases de reflexión interna total $\varphi_r$ distintas para TE y
  TM (ecs. (6.2-11) y (6.2-13)) hacen que $\beta_m^{TE}\ne\beta_m^{TM}$: **birrefringencia de
  guía**, relevante para XPM entre polarizaciones y para phase matching por birrefringencia
  modal.
- **Índice efectivo** $n$ con $n_2<n<n_1$ y $\beta=n\omega/c_o$ (p. 306): generaliza el índice
  del medio; el índice dependiente de la intensidad en guías se formula como $n_{eff}(I)$.
- **Factor de confinamiento** $\Gamma_m$ (8.2-18, p. 305) y área efectiva: la intensidad
  efectiva para SPM/XPM/FWM/Raman en guías depende del solape modal; los coeficientes de
  acoplamiento (8.5-6) son integrales de solape $\int u_1u_2\,dy$, mismo tipo que los solapes
  modales en FWM y Raman intermodal.
- **Modos acoplados.** El formalismo (8.5-4)–(8.5-12) (matriz $\mathbf{T}$ unitaria,
  intercambio periódico, $L_0=\pi/2\mathcal{C}$) es el prototipo de todas las ecuaciones de
  ondas acopladas del curso (SHG, OPA, Raman).
- **Plasmónica** (p. 321–322): confinamiento sub-λ ⇒ intensidades locales muy altas, realce de
  efectos no lineales en superficies (relevante como contexto de SERS/Raman).

### Para el proyecto final (anillos add-drop en Si₃N₄, sensado de índice de refracción)

- **Guía de canal y modos.** Las guías de Si₃N₄ son strip/rib embebidas en SiO₂ (Fig. 8.3-3,
  p. 310); su análisis es el 2D de §8.3 (sin solución cerrada ⇒ solvers como MODE/FDE). La
  intuición de §8.2 sirve directa: $n_2k_o<\beta<n_1k_o$; **$n_{eff}$ crece con la frecuencia y
  con $d$**; los modos de orden alto penetran más en el cladding ($\gamma_m$ menor, (8.2-14)).
- **Sensado bulk.** La cola evanescente $\exp(-\gamma_my)$ en el cladding (8.2-13) es lo que
  "ve" el analito ($n=1.33\to1.37$ como cladding completo): la sensibilidad
  $\partial n_{eff}/\partial n_{clad}$ crece con la fracción de potencia en el cladding
  ($1-\Gamma_m$, Ejercicio 8.2-1) ⇒ guías delgadas / modos cercanos al corte sensan más, a
  costa de pérdidas por fuga. Condición de **monomodo** (8.2-7) para evitar dispersión modal
  en el anillo.
- **Acoplador bus–anillo.** La región de acoplamiento del add-drop es un acoplador direccional:
  $P_2/P_1(0)=\sin^2\mathcal{C}z$, $L_0=\pi/2\mathcal{C}$, acoplador 3 dB en $L_0/2$ (p. 318).
  El coeficiente de acoplamiento $\kappa$ y la transmisión $t$ del modelo de anillo salen de
  $\mathbf{T}$ (8.5-11): $t=\cos\mathcal{C}L$, $\kappa=\sin\mathcal{C}L$. $\mathcal{C}$ decae con
  el gap porque es integral de solape de colas evanescentes (8.5-6); desajuste $\Delta\beta$
  (guías de distinto ancho o radio) reduce la transferencia según (8.5-13).
- **FSR y $n_g$ del anillo.** $n_g=c_o/v$ con $v=d\omega/d\beta$ de la curva de dispersión
  (8.2-21)–(8.2-22): la velocidad de grupo del modo (no la de fase) fija el FSR; el libro
  muestra que $v$ tiene un mínimo y que $n_g>n_{eff}$ cerca del corte (Fig. 8.2-8(b), p. 307).
- **Dispersión de guía y supercontinuo.** El punto de GVD cero de cada modo (p. 307) se mueve
  con la geometría: es el principio de ingeniería de dispersión en Si₃N₄ para solitones y SC;
  $\beta_2=d^2\beta/d\omega^2$ se obtiene de la relación de dispersión del modo.
- **Entrada de luz.** Acoplamiento por rejilla con $n_2k_o\cos\theta_i+2\pi/\Lambda=\beta_m$
  (p. 315) y por extremo con empalme modal $\mathsf{a}_l=\int s\,u_l\,dy$ (8.5-3, p. 314): base
  de grating couplers y edge couplers que se usarán en el chip.
- **Modos acoplados vs. simulación.** La teoría es válida solo para acoplamiento débil
  (p. 316, 320); para gaps pequeños o guías de alto contraste (Si₃N₄/SiO₂, y más aún SOI) hay
  que comparar con FDTD/varFDTD; el libro mismo señala que los modos del sistema compuesto
  difieren de los de cada guía aislada.
