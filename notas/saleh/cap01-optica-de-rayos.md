# Capítulo 1 — Ray Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 1–37 (PDF 23–59). Leído el 2026-11-05.

Convenciones del libro usadas aquí: unidades SI; $j=\sqrt{-1}$ (aparece en §1.4D, ec. (1.4-28));
índice de refracción $n = c_o/c \ge 1$ con $c_o$ la velocidad de la luz en el vacío. Las matrices
de rayos se escriben en negrita, $\mathbf M$. Todas las citas de página son de la numeración del
libro (sumar 22 para la página del PDF).

## Resumen del capítulo

La óptica de rayos (u óptica geométrica) es el modelo más simple de la luz: la luz viaja en
forma de rayos que obedecen reglas geométricas, y es el límite de la óptica ondulatoria cuando
la longitud de onda es infinitesimalmente pequeña (p. 2, Fig. 1.0-1). El capítulo parte de un
conjunto de postulados (§1.1, p. 3): existencia de rayos, índice de refracción $n = c_o/c$,
camino óptico $\int n\,ds$ y el principio de Fermat ($\delta\int n\,ds=0$), del que se deducen
la propagación rectilínea en medios homogéneos (principio de Herón), la ley de reflexión y la
ley de Snell. En §1.2 (p. 6) esas tres reglas se aplican a espejos (planos, paraboloidales,
elípticos, esféricos), fronteras planas (refracción externa/interna, reflexión interna total,
prismas, divisores de haz), fronteras esféricas y lentes delgadas (ecuación de imagen
$1/z_1+1/z_2=1/f$, aumento $-z_2/z_1$) y guías de luz (fibra óptica de salto de índice, apertura
numérica $\mathrm{NA}=\sqrt{n_1^2-n_2^2}$, atrapamiento de luz en medios de alto índice). En §1.3
(p. 17) se trata la óptica de índice graduado (GRIN): la ecuación del rayo
$\frac{d}{ds}(n\,d\mathbf r/ds)=\nabla n$, su versión paraxial, la lámina y la fibra SELFOC de
perfil parabólico (trayectorias sinusoidales de paso $2\pi/\alpha$, NA $\approx n_0 a\alpha$) y
la ecuación eikonal $|\nabla S|^2=n^2$. En §1.4 (p. 24) se desarrolla la óptica matricial: la
matriz de transferencia de rayos $ABCD$ de cada componente, la regla de cascada
$\mathbf M=\mathbf M_N\cdots\mathbf M_2\mathbf M_1$, y la teoría de sistemas periódicos
(relación de recurrencia $y_{m+2}=2by_{m+1}-F^2y_m$, solución armónica
$y_m=y_{\max}\sin(m\varphi+\varphi_0)$ y condición de estabilidad $|{\tfrac12}(A+D)|\le1$), con
aplicaciones a secuencias de lentes y resonadores ópticos.

## Secciones

### Introducción del capítulo (p. 2–3)

- **Jerarquía de teorías** (p. 2, Fig. 1.0-1): óptica cuántica ⊃ óptica electromagnética ⊃
  óptica ondulatoria (escalar) ⊃ óptica de rayos. La óptica de rayos es el límite de la
  ondulatoria cuando $\lambda\to0$; es válida cuando los objetos son mucho mayores que $\lambda$.
  Históricamente: rayos → ondas → EM → cuántica. Cada modelo del libro parte de postulados sin
  demostración, que luego se muestran como casos particulares del siguiente nivel.
- **Alcance** (p. 3): la óptica de rayos trata la *posición* y la *dirección* de los rayos;
  sirve para formación de imágenes y para condiciones de guiado (p. ej. en una fibra). En medios
  isótropos los rayos apuntan en la dirección del flujo de energía óptica; se pueden construir
  haces de rayos cuya densidad es proporcional a la densidad de energía (para una fuente puntual
  isótropa, la energía en un cono es proporcional a su ángulo sólido).
- **Rayos paraxiales** (p. 3): rayos que viajan a pequeñas inclinaciones respecto al eje óptico;
  base de la *óptica paraxial* y de la óptica matricial $2\times2$ (§1.4).

### 1.1 Postulados de la óptica de rayos (p. 3)

**Postulados (recuadro, p. 3–4):**

1. La luz viaja en forma de rayos, emitidos por fuentes y observables en detectores.
2. Un medio óptico se caracteriza por el **índice de refracción** $n\ge1$, $n=c_o/c$, con $c_o$
   la velocidad de la luz en el vacío y $c$ en el medio. El tiempo para recorrer una distancia
   $d$ es $d/c=nd/c_o$, proporcional al **camino óptico** $nd$.
3. En un medio inhomogéneo $n=n(\mathbf r)$, $\mathbf r=(x,y,z)$, y el camino óptico entre $A$ y
   $B$ es
   $$\text{Camino óptico}=\int_A^B n(\mathbf r)\,ds, \tag{1.1-1}$$
   con $ds$ el elemento diferencial de longitud a lo largo de la trayectoria. El tiempo de
   viaje es proporcional al camino óptico.
4. **Principio de Fermat** (p. 4): los rayos entre $A$ y $B$ siguen una trayectoria cuyo tiempo
   de viaje (camino óptico) es un *extremo* respecto a trayectorias vecinas:
   $$\delta\int_A^B n(\mathbf r)\,ds=0, \tag{1.1-2}$$
   donde $\delta$ ("la variación de") indica mínimo, máximo o punto de inflexión. Usualmente es
   un mínimo: *los rayos de luz viajan por el camino de menor tiempo*. Si varios caminos
   comparten el mínimo, todos se siguen simultáneamente. Un caso de máximo se da en el
   Prob. 1.1-2.

**Propagación en un medio homogéneo** (p. 4): $n$ constante ⇒ velocidad constante ⇒ el camino
de mínimo tiempo es el de mínima distancia (**principio de Herón**) ⇒ *en un medio homogéneo
los rayos viajan en línea recta* (Fig. 1.1-1: las sombras son proyecciones perfectas de las
aperturas).

**Reflexión en un espejo** (p. 5). Ley de reflexión: *el rayo reflejado está en el plano de
incidencia y el ángulo de reflexión es igual al de incidencia* ($\theta'=\theta$). El plano de
incidencia lo forman el rayo incidente y la normal al espejo en el punto de incidencia
(Fig. 1.1-2a). Demostración por Herón (Fig. 1.1-2b): para ir de $A$ a $C$ vía el espejo,
$\overline{AB}+\overline{BC}$ mínimo; con $C'$ imagen especular de $C$, $\overline{BC}=\overline{BC'}$,
y $\overline{AB}+\overline{BC'}$ es mínimo cuando $ABC'$ es recta, es decir $\theta=\theta'$.

**Reflexión y refracción en la frontera entre dos medios** (p. 5–6, Fig. 1.1-3). El rayo
incidente se divide en uno reflejado (ley de reflexión) y uno refractado o transmitido, que
obedece la ley de refracción: *el rayo refractado está en el plano de incidencia y el ángulo de
refracción $\theta_2$ se relaciona con el de incidencia $\theta_1$ por la ley de Snell*:
$$n_1\sin\theta_1=n_2\sin\theta_2. \tag{1.1-3}$$
**(Recuadro: Ley de Snell.)** La *proporción* en que la luz se refleja y se refracta **no** la
describe la óptica de rayos (p. 5; eso lo dan las ecuaciones de Fresnel, cap. 6).

**Ejercicio 1.1-1 — Demostración de la ley de Snell** (p. 6, Fig. 1.1-4): minimizar
$n_1\overline{AB}+n_2\overline{BC}=n_1d_1\sec\theta_1+n_2d_2\sec\theta_2$ respecto a
$\theta_1,\theta_2$ con la restricción $d_1\tan\theta_1+d_2\tan\theta_2=d$; la solución es la ley
de Snell.

Las tres reglas (propagación rectilínea, reflexión, refracción) bastan para todo §1.2 sin
volver a invocar a Fermat (p. 6).

### 1.2 Componentes ópticos simples (p. 6)

#### 1.2A Espejos (p. 6)

- **Espejo plano** (p. 6, Fig. 1.2-1): los rayos desde $P_1$ se reflejan como si vinieran de la
  imagen $P_2$ detrás del espejo.
- **Espejo paraboloidal** (p. 6–7, Fig. 1.2-2): paraboloide de revolución; enfoca todos los
  rayos paralelos al eje en el **foco** $F$; $\overline{PF}=f$ es la **distancia focal**. Usos:
  colectores en telescopios, colimadores en linternas.
- **Espejo elíptico** (p. 7, Fig. 1.2-3): refleja todos los rayos de un foco $P_1$ al otro $P_2$;
  por Herón, todas las trayectorias $P_1\to P_2$ tienen igual longitud.
- **Espejo esférico** (p. 7, Fig. 1.2-4): más fácil de fabricar, pero no tiene ni la propiedad
  focalizadora del paraboloide ni la de imagen del elíptico; los rayos paralelos cortan el eje
  en puntos distintos y su envolvente es la **cáustica**. Los rayos cercanos al eje se enfocan
  aproximadamente en $F$ a distancia $(-R)/2$ del centro $C$. **Convención: $R<0$ para espejo
  cóncavo, $R>0$ para convexo.**
- **Rayos paraxiales en espejos esféricos** (p. 7–9): rayos con $\sin\theta\approx\theta$. En la
  **aproximación paraxial** un espejo esférico enfoca como el paraboloidal *y* forma imágenes
  como el elíptico; el conjunto de reglas resultante es la **óptica paraxial** (óptica de primer
  orden, óptica gaussiana). Un espejo esférico de radio $R$ actúa como paraboloidal de
  $f=R/2$ (Fig. 1.2-5: cerca del eje la parábola se aproxima por un círculo de radio igual a su
  radio de curvatura).
  Deducción (p. 8, Fig. 1.2-6): rayo desde $P_1$ (distancia $z_1$) con ángulo $\theta_1$ se
  refleja en altura $y$ y corta el eje en $P_2$ (distancia $z_2$) con ángulo $\theta_2<0$. De la
  geometría $\theta_1=\theta_0-\theta$ y $(-\theta_2)=\theta_0+\theta$, luego
  $(-\theta_2)+\theta_1=2\theta_0$, y con $\theta_0\approx y/(-R)$:
  $$(-\theta_2)+\theta_1\approx\frac{2y}{(-R)}, \tag{1.2-1}$$
  y con $\theta_1\approx y/z_1$, $(-\theta_2)\approx y/z_2$:
  $$\frac1{z_1}+\frac1{z_2}\approx\frac{2}{(-R)}. \tag{1.2-2}$$
  Vale para todo $y$ (todo $\theta_1$) mientras la aproximación sea válida ⇒ todos los rayos
  paraxiales desde $P_1$ llegan a $P_2$. El eje $z$ apunta hacia la izquierda; $z<0$ queda a la
  derecha del espejo. Con $z_1=\infty$, $z_2=(-R)/2$:
  $$f=\frac{(-R)}{2}, \tag{1.2-3}$$
  **(Recuadro: distancia focal, espejo esférico.)**
  $$\frac1{z_1}+\frac1{z_2}=\frac1f, \tag{1.2-4}$$
  **(Recuadro: ecuación de imagen, rayos paraxiales.)** Incidente y reflejado deben ser
  paraxiales.

- **Ejercicio 1.2-1 — Formación de imagen por un espejo esférico** (p. 9, Fig. 1.2-7): mostrar
  que en la aproximación paraxial los rayos desde $P_1=(y_1,z_1)$ van a $P_2=(y_2,z_2)$ con
  $z_1,z_2$ satisfaciendo (1.2-4) y $y_2=-y_1z_2/z_1$: el espejo forma imágenes con aumento
  $-z_2/z_1$ (negativo ⇒ imagen invertida).

#### 1.2B Fronteras planas (p. 9)

Ley de Snell (1.1-3) graficada en Fig. 1.2-8 (p. 10; curvas $\theta_2$ vs $\theta_1$ para
$n_2/n_1=2/3,\,1,\,3/2$):

- **Refracción externa** ($n_1<n_2$): $\theta_2<\theta_1$, el rayo refractado se aleja de la
  frontera (se acerca a la normal).
- **Refracción interna** ($n_1>n_2$): $\theta_2>\theta_1$, el rayo refractado se acerca a la
  frontera.

Los rayos se doblan para minimizar el camino óptico: alargan el trayecto en el medio de menor
índice a costa del de mayor índice (p. 10). Para ángulos pequeños la relación es lineal:
$n_1\theta_1\approx n_2\theta_2$, $\theta_2\approx(n_1/n_2)\theta_1$.

**Reflexión interna total (TIR)** (p. 10): con $n_1>n_2$, $\theta_2$ alcanza $90°$ primero,
cuando $\theta_1=\theta_c$ (**ángulo crítico**), $n_1\sin\theta_c=n_2\sin(\pi/2)=n_2$:
$$\theta_c=\sin^{-1}\frac{n_2}{n_1}. \tag{1.2-5}$$
**(Recuadro: ángulo crítico.)** Si $\theta_1>\theta_c$ Snell no puede satisfacerse, no hay
refracción y el rayo se refleja totalmente como en un espejo perfecto (Fig. 1.2-9a). Base de
prismas reflectores (Fig. 1.2-9b: si $n_1>\sqrt2$ y $n_2=1$, $\theta_c<45°$, y un rayo a $45°$
se refleja totalmente) y de fibras ópticas (Fig. 1.2-9c, §1.2D). Por Fresnel (cap. 6) toda la
energía va al rayo reflejado: el proceso es muy eficiente.

**Prismas** (p. 11, Fig. 1.2-10): prisma de ángulo de vértice $\alpha$ e índice $n$ desvía un
rayo incidente con ángulo $\theta$ un ángulo
$$\theta_d=\theta-\alpha+\sin^{-1}\!\left[\sqrt{n^2-\sin^2\theta}\,\sin\alpha-\sin\theta\cos\alpha\right], \tag{1.2-6}$$
(aplicando Snell dos veces). Para $\alpha$ pequeño (prisma delgado) y $\theta$ pequeño
(paraxial):
$$\theta_d\approx(n-1)\alpha, \tag{1.2-7}$$
aproximadamente independiente de $\theta$. Fig. 1.2-10 grafica $\theta_d(\theta)$ para
$n=1.5$ y $\alpha=10°,30°,45°$; con $\alpha=45°$ o $\theta=0°$ ocurre TIR (como en
Fig. 1.2-9b).

**Divisores de haz** (p. 11, Fig. 1.2-11): dividen el haz incidente en uno reflejado y uno
transmitido; también sirven para combinar dos haces en uno (c). Se construyen con una película
metálica o dieléctrica semitransparente sobre vidrio, o con una lámina delgada de vidrio o un
prisma. (a) espejo parcialmente reflector, (b) lámina delgada, (c) combinador.

#### 1.2C Fronteras esféricas y lentes (p. 12)

**Frontera esférica** de radio $R$ entre $n_1$ y $n_2$. **Convención: $R>0$ convexa, $R<0$
cóncava.** Snell se aplica respecto a la normal (radio vector desde el centro $C$); los ángulos
$\theta_1,\theta_2$ se definen respecto al eje $z$. Con $\sin\theta\approx\theta$,
$\tan\theta\approx\theta$ (Fig. 1.2-12, $R>0$):

- Un rayo con ángulo $\theta_1$ que toca la frontera a altura $y$ (ángulo $\theta_0$ con el
  radio vector) sale con ángulo $\theta_2$ respecto a $z$ y $\theta_3$ respecto al radio vector;
  el ángulo de incidencia es $\theta_1$ más el ángulo del radio vector con el eje
  ($\approx y/R$) y el de refracción es $\theta_3$ [en el escaneo la frase se lee
  "$(\theta_1+\theta_2)$"; la lectura geométrica consistente con (1.2-8) y la Fig. 1.2-12a,
  donde el ángulo de salida se marca $(-\theta_2)$, es la indicada]:
  $$\theta_2\approx\frac{n_1}{n_2}\theta_1-\frac{n_2-n_1}{n_2}\frac yR. \tag{1.2-8}$$
- Todos los rayos paraxiales desde $P_1=(y_1,z_1)$ se encuentran en $P_2=(y_2,z_2)$ con
  $$\frac{n_1}{z_1}+\frac{n_2}{z_2}\approx\frac{n_2-n_1}{R} \tag{1.2-9}$$
  y
  $$y_2=-\frac{n_1}{n_2}\frac{z_2}{z_1}y_1. \tag{1.2-10}$$
  Los planos $z=z_1$ y $z=z_2$ son **planos conjugados**; aumento $-(n_1/n_2)(z_2/z_1)$
  (negativo ⇒ invertida). $P_1$ se mide con eje hacia la izquierda y $P_2$ con eje hacia la
  derecha ($z_2<0$ si $P_2$ queda a la izquierda de la frontera) (p. 13).
- Estas propiedades son aproximadas (solo rayos paraxiales); la desviación para ángulos grandes
  se llama **aberración** (p. 13).

- **Ejercicio 1.2-2 — Formación de imagen** (p. 13): deducir (1.2-8); probar que los rayos
  paraxiales desde $P_1$ pasan por $P_2$ si se cumplen (1.2-9) y (1.2-10).
- **Ejercicio 1.2-3 — Superficie de imagen sin aberración** (p. 13): hallar la ecuación de una
  superficie asférica convexa entre $n_1$ y $n_2$ tal que *todos* los rayos (no solo paraxiales)
  desde un punto axial $P_1$ a distancia $z_1$ a la izquierda se enfoquen en $P_2$ a $z_2$ a la
  derecha. Pista: por Fermat, los caminos ópticos de todas las trayectorias deben ser iguales.

**Lentes** (p. 13–15, Fig. 1.2-13): lente esférica definida por los radios $R_1,R_2$, el espesor
$\Delta$ y el índice $n$; una lente de vidrio en aire es la combinación de dos fronteras
esféricas (aire-vidrio y vidrio-aire). Se traza aplicando (1.2-8) en cada superficie; en
general complicado. **Lente delgada**: el rayo sale a la misma altura $y$ a la que entra. Entonces
(Fig. 1.2-14):

- $$\theta_2=\theta_1-\frac yf, \tag{1.2-11}$$
  con la **distancia focal**
  $$\frac1f=(n-1)\left(\frac1{R_1}-\frac1{R_2}\right). \tag{1.2-12}$$
  **(Recuadro: distancia focal, lente esférica delgada.)**
- Todos los rayos desde $P_1=(y_1,z_1)$ se juntan en $P_2=(y_2,z_2)$ con
  $$\frac1{z_1}+\frac1{z_2}=\frac1f, \tag{1.2-13}$$
  **(Recuadro: ecuación de imagen)** y
  $$y_2=-\frac{z_2}{z_1}y_1. \tag{1.2-14}$$
  **(Recuadro: aumento.)** Idénticas a las del espejo esférico [(1.2-4) y Ej. 1.2-1].
- Aumento $-z_2/z_1$; es unidad cuando $z_1=z_2=2f$. $f$ determina completamente el efecto sobre
  rayos paraxiales. $P_1$ y $P_2$ se miden con ejes hacia la izquierda y la derecha,
  respectivamente; $R_1,R_2$ positivos para superficies convexas, negativos para cóncavas. Para
  la biconvexa de Fig. 1.2-13, $R_1>0$ y $R_2<0$, luego los dos términos de (1.2-12) se suman y
  $f>0$ (p. 14).
- **Ejercicio 1.2-4 — Demostración de las fórmulas de lente delgada** (p. 15): con (1.2-8) y la
  definición (1.2-12), probar (1.2-11) y (1.2-13).
- Fig. 1.2-15 (p. 15): los rayos no paraxiales no pasan por el foco paraxial; la envolvente de
  los refractados es la **cáustica** (aberración).

#### 1.2D Guías de luz (p. 15)

- La luz se puede guiar con una serie de lentes o espejos (Fig. 1.2-16a,b), pero las lentes
  reflejan parcialmente y los espejos absorben parcialmente: la pérdida acumulada es grande con
  muchos elementos; hay componentes mejorados (lentes con antirreflejo) pero el sistema es
  engorroso y caro. El mecanismo ideal es la **reflexión interna total** en la frontera entre
  dos medios de distinto índice (Fig. 1.2-16c): reflexiones repetidas sin refracción; fibras de
  vidrio de alta pureza guían luz decenas de kilómetros con baja pérdida.
- **Fibra óptica** (p. 15–16, Fig. 1.2-17): dos cilindros concéntricos de vidrio (o plástico);
  el **núcleo** (core) con $n_1$ y el **revestimiento** (cladding) con $n_2<n_1$ ligeramente
  menor. Los rayos del núcleo se reflejan totalmente si el ángulo de incidencia
  $\bar\theta>\theta_c=\sin^{-1}(n_2/n_1)$. Con $\theta=90°-\bar\theta$ el ángulo respecto al
  eje, los rayos quedan confinados si $\theta<\bar\theta_c=90°-\theta_c=\cos^{-1}(n_2/n_1)$.
  (Comunicaciones: caps. 9 y 24.)
- **Ejercicio 1.2-5 — Apertura numérica y ángulo de aceptación de una fibra óptica** (p. 16,
  Fig. 1.2-18): fibra iluminada desde el aire ($n=1$) por una fuente (p. ej. un LED). Mostrar que
  el semiángulo $\theta_a$ del cono de rayos aceptados (transmitidos sin refractarse al
  revestimiento) cumple
  $$\mathrm{NA}=\sin\theta_a=\sqrt{n_1^2-n_2^2}. \tag{1.2-15}$$
  **(Recuadro: apertura numérica, fibra óptica.)** $\theta_a$ es el **ángulo de aceptación** y
  $\mathrm{NA}\equiv\sin\theta_a$ la **apertura numérica**. Calcular NA y $\theta_a$ para una
  fibra de sílice con $n_1=1.475$, $n_2=1.460$. [Resultado, calculado aquí:
  $\mathrm{NA}=\sqrt{1.475^2-1.460^2}\approx0.210$, $\theta_a\approx12.1°$.]
- **Atrapamiento de luz en medios de alto índice** (p. 16): es difícil extraer al aire la luz
  generada dentro de un medio de índice alto, sobre todo con caras paralelas, porque ciertos
  rayos sufren TIR múltiple sin refractarse nunca.
- **Ejercicio 1.2-6 — Luz atrapada en un diodo emisor de luz** (p. 17, Fig. 1.2-19):
  (a) luz generada en todas direcciones dentro de un paralelepípedo de índice $n$ rodeado de aire
  (como en un LED, cap. 17): ¿cuál es el ángulo del cono de rayos (dentro del material) que
  emerge por cada cara? ¿Qué pasa con los demás? Valor numérico para GaAs ($n=3.6$).
  [Cono de semiángulo $\theta_c=\sin^{-1}(1/n)\approx16.1°$; los demás quedan atrapados por
  TIR.]
  (b) Si la potencia en un cono es proporcional a su ángulo sólido, mostrar que la fracción de
  potencia extraída respecto a la generada es $3\left(1-\sqrt{1-1/n^2}\right)$, válido si
  $n>\sqrt2$. Valor para GaAs. [$\approx3(1-\sqrt{1-1/12.96})\approx0.118$, es decir
  $\approx12\%$.]

### 1.3 Óptica de índice graduado (p. 17)

Un material **GRIN** tiene índice que varía continuamente con la posición, $n(\mathbf r)$;
se fabrica con dopantes de concentración controlada. Los rayos siguen trayectorias curvas; con
$n(\mathbf r)$ adecuado una lámina GRIN hace lo mismo que un prisma o una lente (p. 17).

#### 1.3A La ecuación del rayo (p. 17)

Del principio de Fermat
$$\delta\int_A^B n(\mathbf r)\,ds=0, \tag{1.3-1}$$
con la trayectoria descrita por $x(s),y(s),z(s)$ ($s$ = longitud de arco, Fig. 1.3-1), el
cálculo de variaciones (fuera del alcance del libro; cita Weinstock, *Calculus of Variations*,
Dover 1974) da
$$\frac{d}{ds}\!\left(n\frac{dx}{ds}\right)=\frac{\partial n}{\partial x},\quad
\frac{d}{ds}\!\left(n\frac{dy}{ds}\right)=\frac{\partial n}{\partial y},\quad
\frac{d}{ds}\!\left(n\frac{dz}{ds}\right)=\frac{\partial n}{\partial z}, \tag{1.3-2}$$
o en forma vectorial, con $\mathbf r(s)=(x(s),y(s),z(s))$:
$$\frac{d}{ds}\!\left(n\frac{d\mathbf r}{ds}\right)=\nabla n, \tag{1.3-3}$$
**(Recuadro: ecuación del rayo.)** $\nabla n$ = gradiente de $n$ (componentes
$\partial n/\partial x$, etc.). (p. 18)

Una forma de resolverla: describir la trayectoria por $x(z),y(z)$ con
$ds=dz\sqrt{1+(dx/dz)^2+(dy/dz)^2}$; el álgebra se simplifica en la aproximación paraxial.

**Ecuación paraxial del rayo** (p. 18, Fig. 1.3-2): trayectoria casi paralela a $z$,
$ds\approx dz$:
$$\frac{d}{dz}\!\left(n\frac{dx}{dz}\right)\approx\frac{\partial n}{\partial x},\qquad
\frac{d}{dz}\!\left(n\frac{dy}{dz}\right)\approx\frac{\partial n}{\partial y}. \tag{1.3-4}$$
**(Recuadro: ecuaciones paraxiales del rayo.)** Dado $n(x,y,z)$ se resuelven para $x(z),y(z)$.
Medio homogéneo ⇒ $d^2x/dz^2=d^2y/dz^2=0$ ⇒ rectas.

#### 1.3B Componentes ópticos de índice graduado (p. 19)

**Lámina de índice graduado** (p. 19, Fig. 1.3-3): $n=n(y)$, uniforme en $x$ y $z$. En el plano
$y$–$z$:
$$\frac{d}{dz}\!\left(n\frac{dy}{dz}\right)=\frac{dn}{dy}, \tag{1.3-5}$$
de donde
$$\frac{d^2y}{dz^2}=\frac1{n(y)}\frac{dn(y)}{dy}. \tag{1.3-6}$$
Con $n(y)$ y condiciones iniciales ($y$ y $dy/dz$ en $z=0$) se obtiene $y(z)$.

*Deducción de (1.3-6) con la ley de Snell* (p. 19, recuadro ☐): con $\theta(y)\approx dy/dz$ el
ángulo con el eje $z$ en $(y,z)$ (complemento del ángulo de incidencia), tras una capa de
espesor $\Delta y$ Snell da
$$n(y)\cos\theta(y)=n(y+\Delta y)\cos\theta(y+\Delta y)
=\left[n(y)+\frac{dn}{dy}\Delta y\right]\left[\cos\theta(y)-\frac{d\theta}{dy}\Delta y\sin\theta(y)\right], \tag{1.3-7}$$
(expansión $f(y+\Delta y)=f(y)+(df/dy)\Delta y$). En el límite $\Delta y\to0$, eliminando el
término en $(\Delta y)^2$:
$$\frac{dn}{dy}=n\frac{d\theta}{dy}\tan\theta. \tag{1.3-8}$$
Para rayos paraxiales $\tan\theta\approx\theta$ y $\theta=dy/dz$ ⇒ (1.3-6). ∎

**Ejemplo 1.3-1 — Lámina con perfil de índice parabólico** (p. 20):
$$n^2(y)=n_0^2\left(1-\alpha^2y^2\right). \tag{1.3-9}$$
Simétrica en $y$, máxima en $y=0$ (Fig. 1.3-4); nombre comercial **SELFOC**. Se elige
$\alpha$ tal que $\alpha^2y^2\ll1$ para todo $y$ de interés ⇒
$n(y)=n_0\sqrt{1-\alpha^2y^2}\approx n_0(1-\tfrac12\alpha^2y^2)$ (parabólico); además
$n(y)-n_0\ll n_0$. Derivando (1.3-9), $(1/n)dn/dy=-(n_0/n)^2\alpha^2y\approx-\alpha^2y$:
$$\frac{d^2y}{dz^2}\approx-\alpha^2y. \tag{1.3-10}$$
Soluciones armónicas de periodo $2\pi/\alpha$. Con $y(0)=y_0$, $dy/dz=\theta_0$ en $z=0$:
$$y(z)=y_0\cos\alpha z+\frac{\theta_0}{\alpha}\sin\alpha z, \tag{1.3-11}$$
$$\theta(z)=\frac{dy}{dz}=-y_0\alpha\sin\alpha z+\theta_0\cos\alpha z. \tag{1.3-12}$$
El rayo oscila alrededor del centro con periodo (distancia) $2\pi/\alpha$ llamado **paso**
(pitch). Excursión máxima $y_{\max}=\sqrt{y_0^2+(\theta_0/\alpha)^2}$, ángulo máximo
$\theta_{\max}=\alpha y_{\max}$; validez del análisis si $\theta_{\max}\ll1$. Si $2y_{\max}$ es
menor que el espesor, el rayo queda confinado y la lámina es una guía de luz. Fig. 1.3-5: rayos
desde una fuente puntual externa en una lámina SELFOC de longitud $d$; *todos tienen el mismo
paso* (se reenfocan cada $\pi/\alpha$).

- **Ejercicio 1.3-1 — La lámina GRIN como lente** (p. 21, Fig. 1.3-6): mostrar que una lámina
  SELFOC de longitud $d<\pi/2\alpha$ con (1.3-9) actúa como lente cilíndrica (poder focal en el
  plano $y$–$z$) de distancia focal
  $$f\approx\frac1{n_0d\alpha\sin\alpha}\quad\text{[así impreso; léase } f\approx 1/(n_0\,\alpha\sin\alpha d)\text{]}, \tag{1.3-13}$$
  y que el punto principal $H$ está a $\overline{AH}\approx(1/n_0\alpha)\tan(\alpha d/2)$ del
  borde. Bosquejar trayectorias para $d=\pi/\alpha$ y $\pi/2\alpha$.
  *Nota de transcripción:* en el escaneo (1.3-13) se lee literalmente
  $f\approx1/(n_0\,d\,\alpha\sin\alpha)$; dimensionalmente la expresión consistente con
  (1.3-11)–(1.3-12) y con $\overline{AH}$ es $f\approx1/(n_0\alpha\sin(\alpha d))$. Se anota la
  duda en lugar de corregir sin verificar.

**Fibras de índice graduado** (p. 21–22): cilindro de vidrio con $n$ función de la distancia
radial. Con
$$n^2=n_0^2\left[1-\alpha^2\left(x^2+y^2\right)\right], \tag{1.3-14}$$
en (1.3-4), con $\alpha^2(x^2+y^2)\ll1$:
$$\frac{d^2x}{dz^2}\approx-\alpha^2x,\qquad\frac{d^2y}{dz^2}\approx-\alpha^2y. \tag{1.3-15}$$
$x$ e $y$ son armónicas en $z$ con periodo $2\pi/\alpha$; posiciones iniciales $(x_0,y_0)$ y
ángulos $\theta_{x0}=dx/dz$, $\theta_{y0}=dy/dz$ fijan amplitudes y fases. Por simetría
circular, sin pérdida de generalidad $x_0=0$ [impreso "$x_y=0$"]:
$$x(z)=\frac{\theta_{x0}}{\alpha}\sin\alpha z,\qquad y(z)=\frac{\theta_{y0}}{\alpha}\sin\alpha z+y_0\cos\alpha z. \tag{1.3-16}$$
- $\theta_{x0}=0$: rayo **meridional** (plano que contiene el eje), trayectoria sinusoidal como
  en la lámina (Fig. 1.3-7a).
- $\theta_{y0}=0$, $\theta_{x0}=\alpha y_0$:
  $$x(z)=y_0\sin\alpha z,\qquad y(z)=y_0\cos\alpha z, \tag{1.3-17}$$
  rayo **helicoidal** sobre un cilindro de radio $y_0$ (Fig. 1.3-7b). En ambos casos el rayo
  queda confinado: la fibra es guía de luz. (Caps. 9 y 24.)

- **Ejercicio 1.3-2 — Apertura numérica de la fibra de índice graduado** (p. 22, Fig. 1.3-8):
  fibra con perfil (1.3-14) y radio $a$; rayo desde el aire que entra por el centro y hace
  ángulo $\theta_0$ con el eje dentro del medio. Mostrar, en aproximación paraxial, que
  $$\mathrm{NA}\equiv\sin\theta_a\approx n_0a\alpha, \tag{1.3-18}$$
  **(Recuadro: apertura numérica, fibra de índice graduado)** con $\theta_a$ el máximo ángulo de
  aceptación para el que el rayo queda confinado. Comparar con la fibra de salto de índice
  (Ej. 1.2-5) tomando $n_1=n_0$ y $n_2=n_0\sqrt{1-\alpha^2a^2}\approx n_0(1-\tfrac12\alpha^2a^2)$.

#### *1.3C La ecuación eikonal (p. 23) — sección avanzada

Sea $S(\mathbf r)$ una función escalar cuyas superficies de nivel $S(\mathbf r)=$ const. son
normales a los rayos en todas partes (Fig. 1.3-9). Conocida $S$, los rayos se construyen pues su
dirección en $\mathbf r$ es la del gradiente $\nabla S(\mathbf r)$. $S$ se llama **eikonal**;
es análoga al potencial $V(\mathbf r)$ en electrostática, con los rayos en el papel de las líneas
de campo $\mathbf E=-\nabla V$. Para satisfacer Fermat, $S$ cumple la **ecuación eikonal**
$$\left(\frac{\partial S}{\partial x}\right)^2+\left(\frac{\partial S}{\partial y}\right)^2+\left(\frac{\partial S}{\partial z}\right)^2=n^2, \tag{1.3-19}$$
$$|\nabla S|^2=n^2, \tag{1.3-20}$$
**(Recuadro: ecuación eikonal)**, con $|\nabla S|^2=\nabla S\cdot\nabla S$. La demostración
desde Fermat está fuera del alcance (cita Born & Wolf, 7.ª ed. 2002); Fermat (y la ecuación del
rayo) también se deducen de la eikonal, así que *cualquiera de las dos puede tomarse como
postulado principal de la óptica de rayos*. Integrando (1.3-20) a lo largo de un rayo:
$$S(\mathbf r_B)-S(\mathbf r_A)=\int_A^B|\nabla S|\,ds=\int_A^Bn\,ds=\text{camino óptico entre }A\text{ y }B. \tag{1.3-21}$$
En la analogía electrostática, el camino óptico es la diferencia de potencial. Para hallar
trayectorias en un medio inhomogéneo se resuelve la ecuación del rayo (1.3-3) o la eikonal para
$S$ y se calcula $\nabla S$. Medio homogéneo ⇒ $|\nabla S|$ constante ⇒ rayos rectos; las
superficies $S=$ const. pueden ser planos paralelos o esferas concéntricas (Fig. 1.3-10, p. 24).
La eikonal se retoma en §2.3 (relación óptica de rayos ↔ óptica ondulatoria).

### 1.4 Óptica matricial (p. 24)

Técnica para trazar rayos paraxiales. Los rayos viajan en un solo plano: aplica a sistemas con
geometría plana y a rayos meridionales en sistemas de simetría circular. Un rayo se describe por
su posición y su ángulo respecto al eje óptico; en la aproximación paraxial, entrada y salida
están relacionadas por dos ecuaciones *lineales* ⇒ matriz $2\times2$ (**matriz de transferencia
de rayos**). La matriz de una cascada es el producto de las matrices individuales (p. 24).

#### 1.4A La matriz de transferencia de rayos (p. 24)

Sistema de simetría circular, eje $z$ en la dirección general de viaje; rayos en el plano
$y$–$z$. Un rayo que cruza el plano transversal en $z$ queda caracterizado por $y$ y $\theta$
(Fig. 1.4-1). Un sistema óptico está entre planos de entrada $z_1$ y salida $z_2$ (Fig. 1.4-2);
lleva $(y_1,\theta_1)$ a $(y_2,\theta_2)$. Con $\sin\theta\approx\theta$:
$$y_2=Ay_1+B\theta_1, \tag{1.4-1}$$
$$\theta_2=Cy_1+D\theta_1, \tag{1.4-2}$$
$$\begin{bmatrix}y_2\\\theta_2\end{bmatrix}=\begin{bmatrix}A&B\\C&D\end{bmatrix}\begin{bmatrix}y_1\\\theta_1\end{bmatrix}. \tag{1.4-3}$$
$\mathbf M$ (elementos reales $A,B,C,D$) caracteriza completamente el sistema: **matriz de
transferencia de rayos**. Convenciones (p. 25): ángulos negativos apuntan hacia abajo desde el
eje $z$ en su dirección de viaje; radios negativos = superficies cóncavas, positivos = convexas.

- **Ejercicio 1.4-1 — Formas especiales de la matriz** (p. 25): (a) si $A=0$, todos los rayos
  que entran con el mismo ángulo salen en la misma posición (rayos paralelos se enfocan en un
  punto: plano de salida = plano focal). (b) ¿Qué caracteriza a los sistemas con $B=0$ (plano
  de salida imagen del de entrada), $C=0$ (rayos paralelos salen paralelos: sistema afocal),
  $D=0$ (rayos desde un punto salen paralelos: entrada en plano focal)? [Interpretaciones
  entre paréntesis añadidas aquí.]

#### 1.4B Matrices de componentes ópticos simples (p. 26)

| Componente | Relaciones | Matriz | Ec. |
|---|---|---|---|
| Propagación libre, distancia $d$ (índice uniforme) | $y_2=y_1+\theta_1d$, $\theta_2=\theta_1$ | $\mathbf M=\begin{bmatrix}1&d\\0&1\end{bmatrix}$ | (1.4-4) |
| Refracción en frontera plana $n_1\to n_2$ | $n_1\theta_1\approx n_2\theta_2$, $y_2=y_1$ | $\mathbf M=\begin{bmatrix}1&0\\0&\dfrac{n_1}{n_2}\end{bmatrix}$ | (1.4-5) |
| Refracción en frontera esférica de radio $R$ (de (1.2-8); convexa $R>0$, cóncava $R<0$) | $y_2\approx y_1$ | $\mathbf M=\begin{bmatrix}1&0\\-\dfrac{(n_2-n_1)}{n_2R}&\dfrac{n_1}{n_2}\end{bmatrix}$ | (1.4-6) |
| Lente delgada de focal $f$ (de (1.2-11); convexa $f>0$, cóncava $f<0$) | $y_2=y_1$ | $\mathbf M=\begin{bmatrix}1&0\\-\dfrac1f&1\end{bmatrix}$ | (1.4-7) |
| Reflexión en espejo plano ($z$ sigue la dirección de viaje: hacia el espejo antes, alejándose después) | $y_2=y_1$, $\theta_2=\theta_1$ | $\mathbf M=\begin{bmatrix}1&0\\0&1\end{bmatrix}$ | (1.4-8) |
| Reflexión en espejo esférico (de (1.2-1); cóncavo $R<0$, convexo $R>0$) | — | $\mathbf M=\begin{bmatrix}1&0\\\dfrac2R&1\end{bmatrix}$ | (1.4-9) |

Nota (p. 27): el espejo esférico (1.4-9) dobla los rayos exactamente como una lente delgada
(1.4-7) de $f=-R/2$.

#### 1.4C Matrices de componentes en cascada (p. 27)

Una cascada de $N$ componentes con matrices $\mathbf M_1,\mathbf M_2,\dots,\mathbf M_N$ equivale
a un sistema de matriz
$$\mathbf M=\mathbf M_N\cdots\mathbf M_2\mathbf M_1. \tag{1.4-10}$$
**Orden:** la matriz del primer sistema atravesado va a la derecha (opera primero sobre el
vector columna del rayo incidente). El producto no es conmutativo en general, pero sí asociativo.

- **Ejercicio 1.4-2 — Conjunto de láminas transparentes paralelas** (p. 27): $N$ láminas planas
  de índices $n_1,\dots,n_N$ y espesores $d_1,\dots,d_N$ en aire ($n=1$) normales a $z$. Por
  inducción,
  $$\mathbf M=\begin{bmatrix}1&\sum_{i=1}^N\dfrac{d_i}{n_i}\\0&1\end{bmatrix}. \tag{1.4-11}$$
  El orden de las láminas no afecta. ¿Cuál es la matriz de una lámina inhomogénea de espesor
  $d_0$ e índice $n(z)$? [Por extensión: $B=\int_0^{d_0}dz/n(z)$.]
- **Ejercicio 1.4-3 — Un espacio seguido de una lente delgada** (p. 28): distancia $d$ de
  espacio libre seguida de lente $f$:
  $$\mathbf M=\begin{bmatrix}1&d\\-\dfrac1f&1-\dfrac df\end{bmatrix}. \tag{1.4-12}$$
- **Ejercicio 1.4-4 — Formación de imagen con lente delgada** (p. 28, Fig. 1.4-3): sistema
  espacio $d_1$ / lente $f$ / espacio $d_2$. Mostrar que si $1/d_1+1/d_2=1/f$ todos los rayos de
  un punto del plano de entrada llegan a un solo punto $y_2$ del de salida (independiente del
  ángulo), y que si $d_2=f$ los rayos paralelos se enfocan en un punto del plano de salida.
- **Ejercicio 1.4-5 — Formación de imagen con lente gruesa** (p. 28–29, Fig. 1.4-4): lente de
  índice $n$, espesor $d$, dos superficies esféricas de igual radio $R$, en aire. Hallar la
  matriz entre planos a $d_1$ y $d_2$ de los vértices. Es sistema formador de imagen (planos
  conjugados) si
  $$\frac1{z_1}+\frac1{z_2}=\frac1f\qquad\text{o}\qquad s_1s_2=f^2, \tag{1.4-13}$$
  con
  $$z_1=d_1+h,\quad s_1=z_1-f, \tag{1.4-14}$$
  $$z_2=d_2+h,\quad s_2=z_2-f, \tag{1.4-15}$$
  $$h=\frac{(n-1)fd}{nR}, \tag{1.4-16}$$
  $$\frac1f=\frac{(n-1)}{R}\left[2-\frac{n-1}{n}\frac dR\right]. \tag{1.4-17}$$
  $F_1,F_2$: **puntos focales** delantero y trasero; $P_1,P_2$: **puntos principales** primero
  y segundo (a distancia $h$ hacia dentro de cada vértice). Mostrar su importancia trazando
  rayos incidentes paralelos al eje.

#### 1.4D Sistemas ópticos periódicos (p. 29)

Cascada de sistemas unitarios idénticos: secuencia de lentes relé equiespaciadas (Fig. 1.2-16a),
reflexión entre dos espejos de un **resonador óptico** (§10.2A; el rayo recorre repetidamente el
mismo sistema unitario = un viaje de ida y vuelta), e incluso un medio homogéneo (fibra de
vidrio) dividido en segmentos iguales.

**Ecuación en diferencias para la posición del rayo** (p. 29–30, Fig. 1.4-5). Sistema unitario
$(A,B,C,D)$; rayo inicial $(y_0,\theta_0)$. A la salida de la etapa $m$:
$$\begin{bmatrix}y_m\\\theta_m\end{bmatrix}=\begin{bmatrix}A&B\\C&D\end{bmatrix}^m\begin{bmatrix}y_0\\\theta_0\end{bmatrix}. \tag{1.4-18}$$
Iterativamente:
$$y_{m+1}=Ay_m+B\theta_m, \tag{1.4-19}$$
$$\theta_{m+1}=Cy_m+D\theta_m. \tag{1.4-20}$$
Eliminando $\theta_m$: de (1.4-19)
$$\theta_m=\frac{y_{m+1}-Ay_m}{B}, \tag{1.4-21}$$
$$\theta_{m+1}=\frac{y_{m+2}-Ay_{m+1}}{B}, \tag{1.4-22}$$
y sustituyendo en (1.4-20):
$$y_{m+2}=2by_{m+1}-F^2y_m, \tag{1.4-23}$$
**(Recuadro: relación de recurrencia para la posición del rayo)**, donde
$$b=\frac{A+D}{2}, \tag{1.4-24}$$
$$F^2=AD-BC=\det[\mathbf M]. \tag{1.4-25}$$
(1.4-23) es una ecuación en diferencias lineal; se resuelve iterativamente ($y_1$ a partir de
$y_0,\theta_0$ con (1.4-19), $m=0$). Solución explícita: ensayo geométrico
$$y_m=y_0h^m, \tag{1.4-26}$$
que requiere
$$h^2-2bh+F^2=0, \tag{1.4-27}$$
$$h=b\pm j\sqrt{F^2-b^2}. \tag{1.4-28}$$
Definiendo
$$\varphi=\cos^{-1}(b/F), \tag{1.4-29}$$
$b=F\cos\varphi$, $\sqrt{F^2-b^2}=F\sin\varphi$, $h=F(\cos\varphi\pm j\sin\varphi)=F\exp(\pm j\varphi)$,
y $y_m=y_0F^m\exp(\pm jm\varphi)$. La combinación lineal de las dos soluciones es armónica:
$$y_m=y_{\max}F^m\sin(m\varphi+\varphi_0), \tag{1.4-30}$$
con $y_{\max}$, $\varphi_0$ fijados por $y_0$ y $y_1$; en $m=0$, $y_{\max}=y_0/\sin\varphi_0$
(p. 31).

**Determinante** (p. 31): $F=\sqrt{\det[\mathbf M]}$. Para cualquier sistema unitario
$\det[\mathbf M]=n_1/n_2$, con $n_1,n_2$ los índices de las secciones inicial y final
(verificable en todas las matrices de §1.4B; y como $\det$ de un producto es el producto de los
$\det$, vale para cualquier cascada: $\det[\mathbf M_2\mathbf M_1]=(n_2/n_3)(n_1/n_2)=n_1/n_3$).
En la mayoría de aplicaciones la primera y última etapa son aire ⇒ $\det[\mathbf M]=1$, $F=1$:
$$y_m=y_{\max}\sin(m\varphi+\varphi_0). \tag{1.4-31}$$
**(Recuadro: posición del rayo, sistema periódico.)** En adelante $F=1$. El ángulo se obtiene de
$\theta_m=(y_{m+1}-Ay_m)/B$.

**Condición para trayectoria armónica** (p. 31): $\varphi=\cos^{-1}b$ debe ser real:
$$|b|\le1\qquad\text{o}\qquad\tfrac12|A+D|\le1. \tag{1.4-32}$$
**(Recuadro: condición de estabilidad.)** Si $|b|>1$, $\varphi$ es imaginario y la solución es
hiperbólica (cosh o sinh), crece sin cota (Fig. 1.4-6a). La solución armónica garantiza $y_m$
acotado (máximo $y_{\max}$): $|b|\le1$ es la condición de **estabilidad** (acotación). El
ángulo también es armónico: $\theta_m=\theta_{\max}\sin(m\varphi+\varphi_1)$; $\theta_{\max}$
debe ser pequeño para que valga la aproximación paraxial.

**Condición para trayectoria periódica** (p. 31): $y_{m+s}=y_m$ para algún entero $s$ (el menor
es el periodo; el rayo repite su camino tras $s$ etapas) ⇔ $s\varphi=2\pi q$, $q$ entero ⇔
$\varphi/2\pi$ racional $q/s$. Ej.: $\varphi=6\pi/11$ ⇒ $\varphi/2\pi=3/11$, periodo $s=11$
(Fig. 1.4-6b). Fig. 1.4-6c: $\varphi=1.5$ rad, estable pero no periódica. (Cap. 7 retoma
sistemas periódicos.)

**Resumen (recuadro, p. 32):** un rayo paraxial ($\theta_{\max}\ll1$) en una cascada de
sistemas unitarios idénticos $(A,B,C,D)$ con $AD-BC=1$ sigue una trayectoria armónica (acotada)
si $|\tfrac12(A+D)|\le1$ (condición de estabilidad). Entonces $y_m=y_{\max}\sin(m\varphi+\varphi_0)$,
$m=0,1,2,\dots$, con $\varphi=\cos^{-1}[\tfrac12(A+D)]$; $y_{\max},\varphi_0$ se determinan de
$y_0$ y $y_1=Ay_0+B\theta_0$. Los ángulos cumplen $\theta_m=(y_{m+1}-Ay_m)/B$ y
$\theta_m=\theta_{\max}\sin(m\varphi+\varphi_1)$. La trayectoria es periódica con periodo $s$
si $\varphi/2\pi$ es racional $q/s$.

**Ejemplo 1.4-1 — Secuencia de lentes idénticas equiespaciadas** (p. 32–33, Fig. 1.4-7):
lentes de focal $f$ separadas $d$ (relé de luz). Sistema unitario = espacio $d$ + lente,
matriz (1.4-12): $A=1$, $B=d$, $C=-1/f$, $D=1-d/f$; $b=\tfrac12(A+D)=1-d/2f$, $\det=1$. La
condición $-1\le b\le1$ da
$$0\le d\le4f, \tag{1.4-33}$$
(la separación debe ser menor que cuatro veces la focal). Entonces
$$y_m=y_{\max}\sin(m\varphi+\varphi_0),\qquad\varphi=\cos^{-1}\!\left(1-\frac d{2f}\right). \tag{1.4-34}$$
Casos (p. 33, Fig. 1.4-8): $d=2f$ ⇒ $\varphi=\pi/2$, $\varphi/2\pi=1/4$, periodo 4 etapas;
$d=f$ ⇒ $\varphi=\pi/3$, $\varphi/2\pi=1/6$, periodo 6 etapas.

- **Ejercicio 1.4-6 — Conjunto periódico de pares de lentes distintas** (p. 33, Fig. 1.4-9):
  secuencia de pares de lentes con focales alternas $f_1$, $f_2$ separadas $d$. Mostrar que la
  trayectoria es acotada (estable) si
  $$0\le\left(1-\frac d{2f_1}\right)\left(1-\frac d{2f_2}\right)\le1. \tag{1.4-35}$$
- **Ejercicio 1.4-7 — Un resonador óptico** (p. 33, Fig. 1.4-10): rayos paraxiales reflejados
  repetidamente entre dos espejos esféricos de radios $R_1$, $R_2$ separados $d$. Tomando como
  sistema unitario un viaje de ida y vuelta, determinar la condición de estabilidad.
  (Resonadores: cap. 10.) [Resultado esperado, consistente con (1.4-35) y la equivalencia
  espejo ↔ lente $f=-R/2$: $0\le(1+d/R_1)(1+d/R_2)\le1$ con la convención de signos del libro,
  es decir $0\le g_1g_2\le1$.]

### Reading List (p. 34–35)

Bibliografía agrupada en *General* (Pedrotti; Sharma; Walther; Moeller; Poon & Kim; Siciliano;
Chartier; Strong; Brooker; **Born & Wolf**, *Principles of Optics*, 7.ª ed. 2002; **Hecht**,
*Optics*, 4.ª ed. 2002; Mansuripur; Keating; Young; Meyer-Arendt; Blaker & Rosenblum; Moore
(GRIN, SPIE Milestone 67); Jenkins & White; Banerjee & Poon; Guenther; Hecht & Zajac; Welford;
Wood; Klein & Furtak; Marchand, *Gradient-Index Optics*, 1978; Carlson; Ditchburn; Hecht
Schaum; Rossi; Stone; Sommerfeld), *Geometrical Optics* (Kravtsov; Greivenkamp; Wolf; Katz;
Ditteon; Colombini & Lerner; Mouroulis & Macdonald; Loshin; Fry; Welford & Winston; Stavroudis;
Zimmer; Nussbaum; Luneburg & Herzberger), *Optical System Design* (Gross; Malacara; Fischer &
Tadic-Galeb; Smith; Nussbaum; O'Shea; Kingslake; Levi), *Matrix Optics* (**Gerrard & Burch**,
*Introduction to Matrix Methods in Optics*, Dover 1994; Blaker; Brouwer) y *Popular and
Historical* (Weiss; Hall; Kingslake; Sobel; Sabra; Newton, *Opticks*; van Heel & Velze; Ronchi;
Tolansky ×2; Bragg; Rüchardt).

## Tablas y datos numéricos útiles

| Dato | Valor | Dónde |
|---|---|---|
| Índice de refracción | $n=c_o/c\ge1$; tiempo de viaje $nd/c_o$ | p. 3 |
| Fibra de sílice (ejemplo) | núcleo $n_1=1.475$, revestimiento $n_2=1.460$ ⇒ NA $\approx0.210$, $\theta_a\approx12.1°$ | Ej. 1.2-5, p. 16 |
| Fibra sin revestimiento | $n_1=1.46$, $n_2\approx1$ (aire) | Prob. 1.2-9, p. 36 |
| GaAs | $n=3.6$ ⇒ cono de escape $\theta_c\approx16.1°$, fracción extraída $\approx12\%$ (todas las caras) | Ej. 1.2-6, p. 17 |
| Material tipo LED | $n=3.7$; capa de $n=1.4$ en la cara frontal | Prob. 1.2-11, p. 36 |
| Agua | $n=4/3$ | Prob. 1.2-8, p. 36 |
| Vidrio típico | $n=1.5$ (lente, prisma de Fig. 1.2-10) | p. 11, p. 36 |
| Esfera de acoplamiento a fibra | $a=1$ mm, $n=1.8$, $y=0.7$ mm | Prob. 1.2-10, p. 36 |
| Prisma reflector a $45°$ | funciona si $n_1>\sqrt2$ ($\theta_c<45°$) | Fig. 1.2-9b, p. 10 |
| Extracción LED | fracción $3(1-\sqrt{1-1/n^2})$ para $n>\sqrt2$ | Ej. 1.2-6b, p. 17 |
| SELFOC | $n^2(y)=n_0^2(1-\alpha^2y^2)$; paso $2\pi/\alpha$; reenfoque cada $\pi/\alpha$; $f\approx1/(n_0\alpha\sin\alpha d)$ (ver nota en Ej. 1.3-1) | p. 20–21 |
| Fibra GRIN | NA $\approx n_0a\alpha$ | (1.3-18), p. 22 |
| Determinante de matriz de rayos | $\det[\mathbf M]=n_1/n_2$ (=1 si entra y sale en aire) | p. 31 |
| Relé de lentes | estable si $0\le d\le4f$; $d=2f$ periodo 4, $d=f$ periodo 6 | p. 32–33 |
| Espejo esférico ↔ lente | $f=-R/2$ (convención $R<0$ cóncavo) | p. 9, 27 |

Convenciones de signo del capítulo (recopiladas): espejo cóncavo $R<0$, convexo $R>0$ (p. 7);
frontera esférica/lente: $R>0$ convexa, $R<0$ cóncava vista desde donde llega el rayo (p. 12,
14); lente convexa $f>0$, cóncava $f<0$ (p. 26); $z_1$ se mide hacia la izquierda y $z_2$ hacia
la derecha del componente (p. 9, 13); ángulos negativos apuntan hacia abajo en la dirección de
viaje (p. 25); tras una reflexión el eje $z$ se invierte para seguir al rayo (p. 26–27).

## Problemas al final del capítulo (p. 35–37)

Los problemas se numeran a continuación de los ejercicios del texto de cada sección. No hay
problemas marcados con asterisco en este capítulo; se marca con * el único que extiende el
formalismo más allá de lo visto (matriz $4\times4$).

- **1.1-2 Fermat's Principle with Maximum Time** (p. 35, Fig. P1.1-2). Espejo elíptico con
  focos $A$, $B$; $\overline{APB}=\overline{AP'B}=\overline{AP''B}$. (a) Para otro espejo de
  menor radio de curvatura tangente a la elipse en $P$, mostrar que $APB$ es un camino de
  tiempo *máximo* (mayor que $AQ'B$ y $AQ''B$). (b) Para un espejo que cruza la elipse tangente
  en $P$ (curvatura cambia de cóncava a convexa), mostrar que los caminos presentan un punto de
  inflexión.
- **1.2-7 Transmission through Planar Plates** (p. 36). (a) Con Snell, un rayo (no
  necesariamente paraxial) que entra a una lámina plana de espesor $d$ e índice $n_1$ en aire
  sale paralelo a su dirección inicial; deducir el desplazamiento lateral en función de $\theta$
  y explicarlo con Fermat. (b) Para una pila de $N$ capas $(d_i,n_i)$, mostrar que el rayo
  transmitido es paralelo al incidente y que $n_m\sin\theta_m=\sin\theta$, $m=1,2,\dots$
- **1.2-8 Lens in Water** (p. 36). Focal $f$ de una lente biconvexa con radios 20 cm y 30 cm y
  $n=1.5$; focal cuando se sumerge en agua ($n=4/3$).
- **1.2-9 Numerical Aperture of a Cladless Fiber** (p. 36). NA y ángulo de aceptación de una
  fibra con núcleo $n_1=1.46$ sin revestimiento ($n_2\approx1$).
- **1.2-10 Fiber Coupling Spheres** (p. 36, Fig. P1.2-10). Esfera de vidrio de radio $a=1$ mm
  e índice $n=1.8$ como lente de acoplamiento; hallar la distancia $f$ esfera–fibra tal que un
  rayo paralelo al eje a altura $y=0.7$ mm se enfoque en la fibra.
- **1.2-11 Extraction of Light from a High-Refractive-Index Medium** (p. 36). Paralelepípedo de
  $n=3.7$ en aire (cf. Ej. 1.2-6). (a) Si todas las caras menos la frontal son espejos perfectos,
  porcentaje de luz extraíble por la cara frontal. (b) ¿Ayuda poner un material transparente de
  $n=1.4$ en la cara frontal?
- **1.3-3 Axially Graded Plate** (p. 36). Lámina de espesor $d$ normal a $z$ con $n(z)$.
  Mostrar que un rayo que entra desde el aire con $\theta_0$ en el plano $y$–$z$ cumple
  $n(z)\sin\theta(z)=\sin\theta_0$, que sale paralelo al incidente (pista: Prob. 1.2-7), y que
  $y(z)$ obedece $(dy/dz)^2=(n^2/\sin^2\theta-1)^{-1}$ [así impreso; con $\theta=\theta_0$].
- **1.3-4 Ray Trajectories in GRIN Fibers** (p. 36). Fibra GRIN con simetría cilíndrica,
  $n(\rho)$, $\rho=\sqrt{x^2+y^2}$. Reescribir las ecuaciones paraxiales (1.3-4) en coordenadas
  cilíndricas $(\rho,\phi,z)$ y deducir ecuaciones diferenciales para $\rho$ y $\phi$ en
  función de $z$.
- **1.4-8 Ray-Transfer Matrix of a Lens System** (p. 37). Matriz de una lente convexa delgada
  $f$ y una cóncava delgada $-f$ separadas $f$; discutir sus propiedades de imagen.
- **1.4-9 Ray-Transfer Matrix of a GRIN Plate** (p. 37). Matriz de una lámina SELFOC
  [$n(y)\approx n_0(1-\tfrac12\alpha^2y^2)$] de espesor $d$.
- **1.4-10 The GRIN Plate as a Periodic System** (p. 37). La lámina SELFOC como sistema
  periódico de láminas contiguas idénticas de espesor $d$; con el resultado de 1.4-9, hallar la
  condición de estabilidad; ¿depende de $d$?
- **1.4-11 Recurrence Relation for a Planar-Mirror Resonator** (p. 37). Resonador de espejos
  planos separados $d$ como sistema periódico: matriz unitaria, mostrar $b=1$ y $F=1$; hay una
  sola raíz de (1.4-27), así que $y_m=\alpha+m\beta$ con $\alpha,\beta$ constantes.
- ***1.4-12 4 × 4 Ray-Transfer Matrix for Skewed Rays** (p. 37). Generalización a rayos
  sesgados en sistemas de simetría circular y a sistemas astigmáticos: el rayo en $z=0$ se
  caracteriza por $(x,y)$ y $(\theta_x,\theta_y)$ ⇒ matriz $4\times4$. (a) Matriz de una
  distancia $d$ en espacio libre. (b) Matriz de una lente cilíndrica delgada de focal $f$
  orientada en $y$ (focal $f$ en el plano $y$–$z$, sin potencia en $x$–$z$).

## Relación con Óptica No Lineal

El capítulo no toca ningún fenómeno no lineal, pero fija conceptos y herramientas que el curso y
el proyecto reutilizan:

**Para el curso (temas del programa):**

- *Ondas EM y haz gaussiano (temas 1–2):* la óptica de rayos es el límite $\lambda\to0$ de la
  ondulatoria (p. 2); la ecuación eikonal $|\nabla S|^2=n^2$ (1.3-20) es el puente con la fase de
  una onda ($S$ = camino óptico, §2.3). La óptica matricial $ABCD$ (§1.4) es *la* herramienta para
  propagar haces gaussianos: en el cap. 3 el parámetro $q$ se transforma como
  $q_2=(Aq_1+B)/(Cq_1+D)$ con las mismas matrices (1.4-4)–(1.4-9). Las condiciones de
  estabilidad de resonadores (1.4-32), Ej. 1.4-7 y la equivalencia espejo ↔ lente $f=-R/2$
  reaparecen en cavidades láser y en la elección de cinturas de haz para experimentos no
  lineales (enfocar para alcanzar intensidades altas: $z_1=z_2=2f$, aumento unidad, etc.).
- *Absorción y dispersión (tema 3):* aquí $n$ es un número real $\ge1$, independiente de $\lambda$
  e intensidad; el curso lo generaliza a $n(\omega)$ complejo y luego a $n=n_0+n_2I$. La dispersión
  del prisma (1.2-6)–(1.2-7), $\theta_d\approx(n-1)\alpha$, es la base de los compresores de
  prismas para pulsos ultracortos (compensación de GVD con pares de prismas, cap. 22).
- *Índice dependiente de la intensidad, autoenfoque (temas 5–6, χ⁽³⁾):* el medio GRIN parabólico
  (1.3-9)–(1.3-12) es el modelo geométrico del **autoenfoque Kerr**: un haz gaussiano intenso
  induce $n(y)\approx n_0+n_2I_0(1-2y^2/w^2)$, es decir, una lámina SELFOC con
  $\alpha^2=4n_2I_0/(n_0w^2)$; la "lente Kerr" tiene focal dada por Ej. 1.3-1 /
  Prob. 1.4-9. La ecuación del rayo (1.3-3) describe la curvatura de rayos en cualquier $n(\mathbf r)$,
  incluido el inducido por la luz (lentes térmicas, autodesenfoque).
- *Propagación de pulsos en fibras, GVD, SPM, solitones, Raman, FWM (temas 7–10):* el guiado por
  TIR (1.2-5), la apertura numérica de salto de índice (1.2-15) y GRIN (1.3-18), y los rayos
  meridionales/helicoidales (Fig. 1.3-7) son la imagen geométrica de los modos de fibra que el
  curso trata después con óptica guiada; la diferencia de caminos entre rayos explica la
  dispersión intermodal (que no es la GVD cromática, pero conviene distinguirlas).
- *Polarización y cristales (tema 3):* fuera del alcance de este capítulo (el libro advierte que
  la fracción reflejada/refractada —Fresnel— y la polarización no las da la óptica de rayos,
  p. 5 y 10).

**Para el proyecto final (anillos add-drop en Si₃N₄, dispersión, supercontinuo, sensado de índice):**

- La condición de confinamiento por TIR, $\theta<\cos^{-1}(n_2/n_1)$ (p. 16), y la NA
  $\sqrt{n_1^2-n_2^2}$ dan la intuición de por qué el contraste Si₃N₄ ($n\approx2.0$) / SiO₂
  ($\approx1.45$) / analito ($1.33$–$1.37$) determina el confinamiento: al subir $n$ del cladding
  (analito) baja el contraste, el modo se extiende más al cladding y cambia $n_{\mathrm{eff}}$ —
  que es exactamente el mecanismo del **sensado de índice de volumen**. El cálculo riguroso
  requiere los modos de la guía (cap. 8, FDE en Lumerical), no rayos.
- El resonador como **sistema periódico** (§1.4D, Ej. 1.4-7, Prob. 1.4-11): un anillo es la
  versión en guía de onda de un viaje de ida y vuelta repetido; la idea de "trayectoria
  periódica si $\varphi/2\pi$ es racional" es el antecedente geométrico de la condición de
  resonancia (fase de ida y vuelta múltiplo de $2\pi$) que da el FSR del anillo add-drop.
- Guías y fibras GRIN (§1.3B): modelo geométrico de dispersión intermodal; útil como contraste
  cuando se discuta la dispersión de guía (GVD, $\beta_2$) de la sección Si₃N₄ para el
  supercontinuo, que es un efecto ondulatorio/cromático y no de rayos.
- Óptica matricial: útil en el montaje experimental (acoplar luz a la guía con lentes/esferas,
  Prob. 1.2-10; relés de lentes estables, (1.4-33)).
