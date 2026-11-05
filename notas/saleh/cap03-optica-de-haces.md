# Capítulo 3 — Beam Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 74–101 (PDF 96–123). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007,
cap. 3 "Beam Optics". Las páginas citadas son las del libro (PDF = libro + 22).

**Convenciones de notación del libro (heredadas del cap. 2):** dependencia temporal
$e^{j\omega t}$ con $j=\sqrt{-1}$, de modo que una onda plana que viaja en $+z$ es $e^{-jkz}$;
campos reales en caligráfica ($\mathcal{U}(\mathbf r,t)$), amplitudes complejas $U(\mathbf r)$
(en negrita cuando son vectoriales); número de onda $k = 2\pi/\lambda$ en el medio;
intensidad óptica $I = |U|^2$ (W/m²); $\rho = \sqrt{x^2+y^2}$ distancia radial al eje.
Unidades SI.

---

## Resumen del capítulo

El capítulo responde a la pregunta de si la luz puede confinarse espacialmente en el espacio
libre sin dispersión angular: la naturaleza ondulatoria lo impide, pero el **haz gaussiano** es
la solución de la ecuación paraxial de Helmholtz que más se acerca a una onda localizada y no
divergente (p. 75). La §3.1 obtiene la amplitud compleja del haz gaussiano a partir de la onda
paraboloidal desplazada a un punto imaginario $z = -jz_0$, y deriva todas sus propiedades:
intensidad, potencia, ancho $W(z)$, divergencia $\theta_0$, profundidad de foco $2z_0$, fase de
Gouy $\zeta(z)$, radio de curvatura $R(z)$, el parámetro complejo $q(z)$ y el factor de calidad
$M^2$. La §3.2 muestra que un haz gaussiano transmitido por componentes ópticos paraxiales y
circularmente simétricos (lente delgada, espejo esférico, sistema ABCD arbitrario) sigue siendo
gaussiano, con fórmulas de transformación de parámetros (enfoque, colimación, expansión,
*relaying*) y la **ley ABCD** $q_2 = (Aq_1+B)/(Cq_1+D)$. La §3.3 generaliza a los haces de
Hermite–Gauss $(l,m)$, modos de resonadores con los mismos frentes de onda que el gaussiano
pero fase de Gouy $(l+m+1)\zeta(z)$. La §3.4 (avanzada) presenta los haces de Laguerre–Gauss
(simetría cilíndrica, fase helicoidal $e^{-jl\phi}$, momento angular orbital) y los haces de
Bessel (solución exacta de Helmholtz, no divergente, pero con ancho RMS infinito) y
Bessel–Gauss.

---

## Secciones

### Introducción del capítulo (p. 75)

- Los dos extremos de confinamiento angular/espacial son la **onda plana** (sin dispersión
  angular, pero energía en todo el espacio) y la **onda esférica** (origen puntual, pero rayos
  que divergen en todas direcciones) (p. 75).
- Las **ondas paraxiales** son aquellas cuyas normales a los frentes de onda forman ángulos
  pequeños con el eje $z$; deben satisfacer la ecuación paraxial de Helmholtz (§2.2C). El haz
  gaussiano es una solución importante de ella (p. 75).
- Rasgos del haz gaussiano (p. 75): potencia concentrada en un cilindro delgado alrededor del
  eje; intensidad transversal gaussiana con simetría circular; ancho mínimo en la cintura
  (*waist*) y creciente a ambos lados; frentes de onda planos cerca de la cintura, curvos
  lejos, y aproximadamente esféricos muy lejos; la divergencia angular es la mínima que permite
  la ecuación de onda para un ancho dado. En condiciones ideales, la luz de muchos láseres es un
  haz gaussiano.

### 3.1 The Gaussian Beam (p. 75)

#### 3.1A Complex Amplitude (p. 75)

**Onda paraxial** (p. 75): onda plana $e^{-jkz}$ ($k = 2\pi/\lambda$) modulada por una
envolvente compleja $A(\mathbf r)$ que varía lentamente con la posición (aprox. constante en una
vecindad de tamaño $\lambda$):

$$U(\mathbf r) = A(\mathbf r)\exp(-jkz). \tag{3.1-1}$$

Para que $U$ satisfaga Helmholtz, $\nabla^2 U + k^2 U = 0$, la envolvente debe cumplir la
**ecuación paraxial de Helmholtz** (2.2-23) (p. 76):

$$\nabla_T^2 A - j\,2k\,\frac{\partial A}{\partial z} = 0, \qquad
\nabla_T^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}. \tag{3.1-2}$$

**Onda paraboloidal** (p. 76, solución simple de (3.1-2), Ejercicio 2.2-2):

$$A(\mathbf r) = \frac{A_1}{z}\exp\!\left(-jk\frac{\rho^2}{2z}\right), \qquad
\rho^2 = x^2 + y^2, \tag{3.1-3}$$

con $A_1$ constante. Es la aproximación paraxial de la onda esférica
$U(r) = (A_1/r)\exp(-jkr)$ cuando $x, y \ll z$ (§2.2B).

**Construcción del haz gaussiano** (p. 76): como (3.1-2) es invariante ante traslaciones en
$z$, la versión desplazada $z \to z - \xi$ también es solución:

$$A(\mathbf r) = \frac{A_1}{q(z)}\exp\!\left[-jk\frac{\rho^2}{2q(z)}\right], \qquad
q(z) = z - \xi. \tag{3.1-4}$$

Sigue siendo solución aun si $\xi$ es **complejo**, pero las propiedades cambian
drásticamente. Con $\xi = -jz_0$ ($z_0$ real) se obtiene la **envolvente compleja del haz
gaussiano** (recuadro, p. 76):

$$\boxed{A(\mathbf r) = \frac{A_1}{q(z)}\exp\!\left[-jk\frac{\rho^2}{2q(z)}\right], \qquad
q(z) = z + jz_0.} \tag{3.1-5}$$

- $q(z)$: **parámetro q** del haz; $z_0$: **rango de Rayleigh** (p. 76).

Para separar módulo y fase se escribe $1/q(z) = 1/(z + jz_0)$ en partes real e imaginaria
definiendo dos funciones reales $R(z)$ y $W(z)$ (recuadro, p. 76):

$$\boxed{\frac{1}{q(z)} = \frac{1}{R(z)} - j\,\frac{\lambda}{\pi W^2(z)}.} \tag{3.1-6}$$

$W(z)$ = ancho del haz; $R(z)$ = radio de curvatura del frente de onda (se demuestra más
adelante). Sustituyendo (3.1-6) en (3.1-5) y usando (3.1-1) se obtiene la **amplitud compleja
del haz gaussiano** (recuadro, p. 77):

$$\boxed{U(\mathbf r) = A_0\,\frac{W_0}{W(z)}\,
\exp\!\left[-\frac{\rho^2}{W^2(z)}\right]
\exp\!\left[-jkz - jk\frac{\rho^2}{2R(z)} + j\zeta(z)\right]} \tag{3.1-7}$$

con los **parámetros del haz** (recuadro, p. 77):

$$\boxed{\begin{aligned}
W(z) &= W_0\sqrt{1 + \left(\frac{z}{z_0}\right)^2} &&(3.1\text{-}8)\\
R(z) &= z\left[1 + \left(\frac{z_0}{z}\right)^2\right] &&(3.1\text{-}9)\\
\zeta(z) &= \tan^{-1}\frac{z}{z_0} &&(3.1\text{-}10)\\
W_0 &= \sqrt{\frac{\lambda z_0}{\pi}} &&(3.1\text{-}11)
\end{aligned}}$$

- $A_0 = A_1/jz_0$ (nueva constante, p. 77).
- El haz queda descrito por **dos parámetros independientes**, $A_0$ y $z_0$, fijados por las
  condiciones de frontera; todo lo demás se relaciona con $z_0$ y $\lambda$ por
  (3.1-8)–(3.1-11) (p. 77).
- Nota práctica: de (3.1-11), $z_0 = \pi W_0^2/\lambda$; en un medio de índice $n$ se usa
  $\lambda = \lambda_0/n$ (el libro lo aplica en Prob. 3.2-8 y 3.3-4).

#### 3.1B Properties (p. 77)

**Intensidad** (p. 77). $I(\mathbf r) = |U(\mathbf r)|^2$:

$$I(\rho, z) = I_0\left[\frac{W_0}{W(z)}\right]^2 \exp\!\left[-\frac{2\rho^2}{W^2(z)}\right],
\qquad I_0 = |A_0|^2. \tag{3.1-12}$$

Para cada $z$ la intensidad es gaussiana en $\rho$ (de ahí el nombre), con pico en $\rho = 0$;
$W(z)$ crece con $z$ (Fig. 3.1-1, p. 78: $I/I_0$ vs. $\rho$ en $z = 0,\ z_0,\ 2z_0$). En el eje:

$$I(0, z) = I_0\left[\frac{W_0}{W(z)}\right]^2 = \frac{I_0}{1 + (z/z_0)^2}, \tag{3.1-13}$$

máxima ($I_0$) en $z = 0$, cae a la **mitad en $z = \pm z_0$** (Fig. 3.1-2, p. 78). Para
$|z| \gg z_0$, $I(0,z) \approx I_0 z_0^2/z^2$: ley del inverso del cuadrado como las ondas
esférica y paraboloidal. El máximo absoluto es $I(0,0) = I_0$ (p. 78).

**Potencia** (p. 78). Integral de la intensidad sobre cualquier plano transversal:

$$P = \int_0^\infty I(\rho, z)\,2\pi\rho\,d\rho, \tag{3.1-14}$$

$$P = \tfrac{1}{2} I_0\,(\pi W_0^2). \tag{3.1-15}$$

La potencia es la mitad de la intensidad pico por el área del haz, independiente de $z$. Como
los haces suelen describirse por su potencia, se reescribe (3.1-12) (recuadro, p. 79):

$$\boxed{I(\rho, z) = \frac{2P}{\pi W^2(z)}\exp\!\left[-\frac{2\rho^2}{W^2(z)}\right].} \tag{3.1-16}$$

Fracción de potencia dentro de un círculo de radio $\rho_0$ en el plano $z$ (p. 79):

$$\frac{1}{P}\int_0^{\rho_0} I(\rho, z)\,2\pi\rho\,d\rho
= 1 - \exp\!\left[-\frac{2\rho_0^2}{W^2(z)}\right]. \tag{3.1-17}$$

- Dentro de $\rho_0 = W(z)$ hay $\approx 86\,\%$ de la potencia ($1 - e^{-2} = 0.865$);
  dentro de $1.5\,W(z)$, $\approx 99\,\%$ (p. 79).

**Ancho del haz** (p. 79). La intensidad cae al factor $1/e^2 \approx 0.135$ del pico en
$\rho = W(z)$; como el 86 % de la potencia está dentro de ese radio, $W(z)$ se toma como
**radio del haz** (*beam radius*). El ancho RMS de la distribución de intensidad es
$\sigma = \tfrac{1}{2}W(z)$ (Apéndice A, §A.2). Recuadro (p. 79):

$$\boxed{W(z) = W_0\sqrt{1 + \left(\frac{z}{z_0}\right)^2}.} \tag{3.1-18}$$

- Mínimo $W_0$ en $z = 0$: **cintura del haz** (*beam waist*); $W_0$ = **radio de la
  cintura** (*waist radius*); $2W_0$ = **tamaño de mancha** (*spot size*) (p. 79).
- $W(\pm z_0) = \sqrt{2}\,W_0$; para $z$ grande crece linealmente (Fig. 3.1-3, p. 79).

**Divergencia del haz** (p. 80). Para $z \gg z_0$:

$$W(z) \approx \frac{W_0}{z_0}z = \theta_0 z, \tag{3.1-19}$$

cono de semiángulo

$$\theta_0 = \frac{W_0}{z_0} = \frac{\lambda}{\pi W_0}, \tag{3.1-20}$$

que contiene $\approx 86\,\%$ de la potencia. En términos del *spot size* (recuadro, p. 80):

$$\boxed{2\theta_0 = \frac{4}{\pi}\frac{\lambda}{2W_0}.} \tag{3.1-21}$$

- Divergencia $\propto \lambda$ e $\propto 1/(2W_0)$: apretar la cintura aumenta la
  divergencia; un haz muy direccional requiere $\lambda$ corta y cintura gruesa (p. 80).

**Profundidad de foco** (p. 80). Distancia axial en la que el ancho no supera $\sqrt{2}$ veces
su mínimo (área dentro de un factor 2 del mínimo): **profundidad de foco** o **parámetro
confocal** = $2z_0$ (Fig. 3.1-4, p. 80). Recuadro:

$$\boxed{2z_0 = \frac{2\pi W_0^2}{\lambda}.} \tag{3.1-22}$$

- $\propto$ área de la cintura $\pi W_0^2$ e $\propto 1/\lambda$. Mancha pequeña ⇒ foco corto,
  localizar el plano focal exige más precisión. Mancha pequeña *y* foco largo solo con $\lambda$
  corta (p. 81).
- **Ejemplo numérico (p. 81):** He–Ne, $\lambda_0 = 633$ nm, $2W_0 = 2$ cm ⇒ $2z_0 \approx 1$ km;
  $2W_0 = 20\ \mu$m ⇒ $2z_0 \approx 1$ mm.

**Fase** (p. 81). De (3.1-7):

$$\varphi(\rho, z) = kz - \zeta(z) + \frac{k\rho^2}{2R(z)}. \tag{3.1-23}$$

En el eje ($\rho = 0$):

$$\varphi(0, z) = kz - \zeta(z). \tag{3.1-24}$$

- $kz$: fase de onda plana. $\zeta(z)$ (3.1-10): **retardo de fase** que va de $-\pi/2$ en
  $z = -\infty$ a $+\pi/2$ en $z = +\infty$ (Fig. 3.1-5, p. 81); corresponde a un retraso en
  exceso del frente de onda respecto a una onda plana o esférica. El retardo acumulado total
  de $-\infty$ a $+\infty$ es $\pi$: **efecto Gouy** (p. 81; cita Siegman, *Lasers*, 1986).
- Valores útiles: $\zeta(z_0) = \pi/4$, $\zeta(\pm\infty) = \pm\pi/2$.

**Frentes de onda** (p. 81). El tercer término de (3.1-23) curva el frente de onda. Superficies
de fase constante: $k[z + \rho^2/2R(z)] - \zeta(z) = 2\pi q$ ($q$ entero). Como $\zeta$ y $R$
varían lentamente, son casi constantes sobre un frente, y queda $z + \rho^2/2R \approx q\lambda
+ \zeta\lambda/2\pi$: ecuación de un **paraboloide de radio de curvatura $R$**. Luego $R(z)$
(3.1-9) es el radio de curvatura del frente de onda en $z$ (Fig. 3.1-6, p. 82).

- $R(0) = \infty$ (frente plano en la cintura); $R$ mínimo $= 2z_0$ en $z = z_0$ (máxima
  curvatura); luego $R(z) \approx z$ para $z \gg z_0$ (frentes ≈ esféricos) (p. 81–82).
- Patrón idéntico para $z < 0$ con cambio de signo. **Convención:** frente divergente ⇒
  $R > 0$; convergente ⇒ $R < 0$ (p. 82).
- Fig. 3.1-7 (p. 82): frentes de onda del haz gaussiano entre $-2z_0$ y $2z_0$. Fig. 3.1-8
  (p. 82): comparación de frentes de (a) onda plana, (b) onda esférica, (c) haz gaussiano: cerca
  del centro parece onda plana; lejos parece esférica pero con fase retrasada $\pi/2$ (un cuarto
  de la distancia entre frentes adyacentes).

**Parámetros necesarios para caracterizar un haz gaussiano** (p. 82–83). Con $\lambda$
conocida: onda plana → amplitud compleja y dirección; onda esférica → amplitud y posición del
origen; haz gaussiano → amplitud pico ($A_0$), dirección (eje), posición de la cintura y **un
parámetro adicional** ($W_0$ o $z_0$). Es decir, conocidos amplitud y eje, faltan dos
parámetros.

- Si se conoce $q(z) = z + jz_0$ en un punto, la distancia a la cintura y $z_0$ son sus partes
  real e imaginaria. **Ejemplo (p. 83):** $q = 3 + j4$ cm ⇒ la cintura está 3 cm a la
  izquierda, $2z_0 = 8$ cm, y $W_0$ sale de (3.1-11). Como $q$ es lineal en $z$: si
  $q(z_1) = q_1$ entonces $q(z_1 + d) = q_1 + d$; en el ejemplo, a $z = 13$ cm, $q = 13 + j4$.
- Si se conocen $W(z)$ y $R(z)$ en un punto, se resuelven (3.1-8), (3.1-9), (3.1-11) para
  $z$, $z_0$, $W_0$; o se halla $q$ con (3.1-6) (p. 83).

**Recuadro resumen: propiedades en posiciones especiales** (p. 83):

- *En $z = z_0$:* intensidad en el eje $= \tfrac{1}{2}$ del pico; ancho $\sqrt{2}\,W_0$ (área
  doble); fase en el eje retrasada $\pi/4$ respecto a la onda plana; $R = 2z_0$ (mínimo, máxima
  curvatura).
- *Cerca del centro* ($|z| \ll z_0$, $\rho \ll W_0$): $\exp[-\rho^2/W^2(z)] \approx 1$,
  intensidad ≈ constante; $R(z) \approx z_0^2/z$ y $\zeta \approx 0$, de modo que la fase
  $k[z + \rho^2/2R] \approx kz(1 + \rho^2/2z_0^2) \approx kz$ porque $z_0 \gg \lambda$ por
  (3.1-11). El haz se aproxima a una **onda plana**.
- *Lejos de la cintura* ($z \gg z_0$, $\rho < W_0$): $W(z) \approx W_0 z/z_0 \gg W_0$,
  intensidad ≈ uniforme; $R(z) \approx z$ ⇒ frentes esféricos. Salvo el retardo Gouy
  $\zeta \approx \pi/2$, la amplitud tiende a la de la onda **paraboloidal** (≈ esférica
  paraxial).

**Ejercicios de la §3.1** (p. 84–85):

- **Ejercicio 3.1-1, Parámetros de un haz láser gaussiano (p. 84).** He–Ne de 1 mW,
  $\lambda = 633$ nm, $2W_0 = 0.1$ mm. (a) Divergencia angular, profundidad de foco y diámetro
  en $z = 3.5\times10^5$ km (≈ distancia a la Luna). (b) Radio de curvatura en $z = 0$, $z_0$ y
  $2z_0$. (c) Intensidad (W/cm²) en el centro ($z = 0, \rho = 0$) y en $z = z_0$; compararla
  con la de una onda esférica de 100 W emitida isotrópicamente desde $z = 0$ en $z = z_0$.
  *(Sin solución en el texto; con (3.1-20): $\theta_0 = \lambda/\pi W_0 \approx 4.0$ mrad;
  $2z_0 = 2\pi W_0^2/\lambda \approx 2.5$ cm; $I_0 = 2P/\pi W_0^2 \approx 25$ W/cm².)*
- **Ejercicio 3.1-2, Validez de la aproximación paraxial (p. 84).** La envolvente $A$ es
  solución exacta de (3.1-2) pero $U = A e^{-jkz}$ solo es solución aproximada de Helmholtz
  (2.2-7). Mostrar que si $\theta_0 \ll 1$ se cumple la condición (2.2-21) de validez de la
  ecuación paraxial de Helmholtz.
- **Ejercicio 3.1-3, Determinación de un haz dados ancho y curvatura (p. 84).** Conocidos
  $W$ y $R$ en un punto (Fig. 3.1-9), la cintura está a la izquierda a distancia

  $$z = \frac{R}{1 + (\lambda R/\pi W^2)^2} \tag{3.1-25}$$

  y el radio de la cintura es

  $$W_0 = \frac{W}{\sqrt{1 + (\pi W^2/\lambda R)^2}}. \tag{3.1-26}$$

- **Ejercicio 3.1-4, Ancho y curvatura en un punto dados los de otro (p. 84).**
  $\lambda = 1\ \mu$m, $W_1 = 1$ mm, $R_1 = 1$ m; hallar $W_2$, $R_2$ a $d = 10$ cm a la
  derecha (Fig. 3.1-10). *(Método: $q_1$ de (3.1-6), $q_2 = q_1 + d$, invertir (3.1-6).)*
- **Ejercicio 3.1-5, Identificación de un haz con curvaturas conocidas en dos puntos
  (p. 85).** Radios $R_1$, $R_2$ separados $d$ (Fig. 3.1-11); verificar que

  $$z_1 = \frac{-d\,(R_2 - d)}{R_2 - R_1 - 2d}, \tag{3.1-27}$$

  $$z_0^2 = \frac{-d\,(R_1 + d)(R_2 - d)(R_2 - R_1 - d)}{(R_2 - R_1 - 2d)^2}, \tag{3.1-28}$$

  y $W_0 = \sqrt{\lambda z_0/\pi}$.

#### 3.1C Beam Quality (p. 85)

El haz gaussiano es una idealización. La calidad de un haz real se mide por la desviación de
su perfil respecto al gaussiano mediante el **factor $M^2$**: razón entre el producto
diámetro de cintura × divergencia del haz real, $2W_m\cdot 2\theta_m$ (usualmente en mm·mrad),
y el del haz gaussiano, $2W_0\cdot 2\theta_0 = 4\lambda/\pi$ (p. 85):

$$M^2 = \frac{2W_m\cdot 2\theta_m}{4\lambda/\pi}. \tag{3.1-29}$$

Si ambos haces tienen el mismo diámetro de cintura,

$$M^2 = \theta_m/\theta_0, \tag{3.1-30}$$

con $\theta_0 = \lambda/\pi W_0 = \lambda/\pi W_m$. Como el gaussiano tiene la mínima
divergencia posible para un ancho dado, $M^2 \ge 1$: el haz real diverge $M^2$ veces más que
un gaussiano del mismo diámetro de cintura (p. 85).

- **Valores típicos (p. 85):** He–Ne $M^2 < 1.1$; láseres de iones $M^2 \approx 1.1$–$1.3$;
  diodos láser TEM$_{00}$ colimados $M^2 \approx 1.1$–$1.7$; láseres multimodo de alta
  energía $M^2$ hasta 3 o 4.
- **Medición de $M^2$ (p. 85–86):** con cámara CCD se mide el perfil de intensidad a lo largo
  del eje tras enfocar con una lente de buena calidad, foco largo y $F_\#$ grande, a un tamaño
  comparable al sensor. Se localiza el plano de mínimo *spot* (cintura, $2W_m$); la distancia
  axial a la que el diámetro crece $\sqrt{2}$ da el rango de Rayleigh $z_m$; la divergencia se
  estima con $\theta_m = \sqrt{\lambda/\pi z_m}$ (de (3.1-11) y (3.1-20)); se aplica (3.1-29).

### 3.2 Transmission Through Optical Components (p. 86)

Idea central: si un haz gaussiano atraviesa componentes ópticos circularmente simétricos
alineados con su eje, y el sistema mantiene la paraxialidad, **el haz sigue siendo gaussiano**;
solo cambian su cintura y curvatura (p. 86).

#### 3.2A Transmission Through a Thin Lens (p. 86)

La transmitancia de amplitud compleja de una lente delgada de focal $f$ es $\propto
\exp(jk\rho^2/2f)$ (2.4-9). Multiplica la amplitud (3.1-7): el ancho no cambia ($W' = W$) pero
el frente de onda sí. Fase incidente en el plano de la lente: $kz + k\rho^2/2R - \zeta$;
emergente (p. 86):

$$kz + k\frac{\rho^2}{2R} - \zeta - k\frac{\rho^2}{2f} = kz + k\frac{\rho^2}{2R'} - \zeta,
\tag{3.2-1}$$

$$\frac{1}{R'} = \frac{1}{R} - \frac{1}{f}. \tag{3.2-2}$$

El haz transmitido es gaussiano con $W' = W$ y $R'$ dado por la ecuación de imagen
$1/R - 1/R' = 1/f$; $R > 0$ (divergente) y $R' < 0$ (convergente) (p. 86). Con el
Ejercicio 3.1-3 se obtienen los nuevos parámetros:

$$W_0' = \frac{W}{\sqrt{1 + (\pi W^2/\lambda R')^2}}, \tag{3.2-3}$$

$$-z' = \frac{R'}{1 + (\lambda R'/\pi W^2)^2} \tag{3.2-4}$$

(el signo menos indica que la nueva cintura queda a la **derecha** de la lente, p. 87).
Sustituyendo $W = W_0\sqrt{1 + (z/z_0)^2}$ y $R = z[1 + (z_0/z)^2]$ (haz incidente con cintura
en $z = 0$, lente en $z$; Fig. 3.2-1, p. 87) se obtiene la **transformación de parámetros por
una lente** (recuadro, p. 87):

$$\boxed{\begin{aligned}
\text{Radio de cintura} &\quad W_0' = M\,W_0 &&(3.2\text{-}5)\\
\text{Posición de cintura} &\quad (z' - f) = M^2 (z - f) &&(3.2\text{-}6)\\
\text{Profundidad de foco} &\quad 2z_0' = M^2 (2z_0) &&(3.2\text{-}7)\\
\text{Divergencia} &\quad 2\theta_0' = \frac{2\theta_0}{M} &&(3.2\text{-}8)\\
\text{Aumento} &\quad M = \frac{M_r}{\sqrt{1 + r^2}} &&(3.2\text{-}9)\\
&\quad r = \frac{z_0}{z - f}, \qquad M_r = \left|\frac{f}{z - f}\right|. &&(3.2\text{-}9a)
\end{aligned}}$$

- $z$ = distancia de la cintura incidente a la lente; $z'$ = distancia de la lente a la nueva
  cintura. El aumento $M$ multiplica la cintura por $M$, la profundidad de foco por $M^2$ y
  divide la divergencia por $M$ (p. 87).

**Límite de óptica de rayos** (p. 87–88). Si $(z - f) \gg z_0$ (lente fuera de la
profundidad de foco; Fig. 3.2-2, p. 88), el haz se aproxima a una onda esférica, $r \ll 1$,
$M \approx M_r$:

$$W_0' \approx M W_0, \tag{3.2-10}$$
$$\frac{1}{z'} + \frac{1}{z} \approx \frac{1}{f}, \tag{3.2-11}$$
$$M \approx M_r = \left|\frac{f}{z - f}\right|. \tag{3.2-12}$$

Son las relaciones de óptica de rayos para un objeto de diámetro $2W_0$ a distancia $z$ de la
lente (§1.2C). Como $M < M_r$ por (3.2-9), **el aumento máximo alcanzable es el límite de
rayos $M_r$**; al crecer $r$ el aumento disminuye. También coinciden con la óptica ondulatoria
del enfoque de una onda esférica paraxial (§2.4B) (p. 88).

#### 3.2B Beam Shaping (p. 88)

Una lente o secuencia de lentes (o componentes de índice gradual) reconfigura un haz
gaussiano sin perder su carácter gaussiano.

**Enfoque del haz** (p. 88). Lente en la cintura ($z = 0$ en (3.2-5)–(3.2-9); Fig. 3.2-3,
p. 89). Recuadro:

$$\boxed{W_0' = \frac{W_0}{\sqrt{1 + (z_0/f)^2}}, \qquad
z' = \frac{f}{1 + (f/z_0)^2}.} \tag{3.2-13, 3.2-14}$$

Caso especial $2z_0 \gg f$ (haz incidente colimado, Fig. 3.2-4, p. 89): con
$z_0 = \pi W_0^2/\lambda$ y (3.1-20),

$$W_0' \approx \frac{\lambda}{\pi W_0}f = \theta_0 f, \tag{3.2-15}$$
$$z' \approx f. \tag{3.2-16}$$

- El haz se enfoca en el plano focal, como un haz de rayos paralelos; la cintura enfocada es
  $\propto \lambda$, $\propto f$ y $\propto 1/W_0$. La óptica de rayos daría mancha cero,
  recuperada cuando $\lambda \to 0$ (p. 89).
- Mancha mínima (escaneo láser, impresión, grabado de CD, fusión láser): $\lambda$ corta,
  haz incidente grueso, focal corta. Como el diámetro de la lente debe ser $D \ge 2W_0$,
  tomando $D = 2W_0$ (recuadro, p. 89):

  $$\boxed{2W_0' \approx \frac{4}{\pi}\lambda F_\#, \qquad F_\# = \frac{f}{D}.} \tag{3.2-17}$$

  Se usan objetivos de microscopio de $F_\#$ pequeño. Advertencia: (3.2-15) y (3.2-16) son
  aproximadas; verificar su validez antes de usarlas (p. 89).

**Ejercicio 3.2-1, Beam Relaying (p. 89).** Haz de radio $W_0$ y longitud de onda $\lambda$
reenfocado por una secuencia de lentes idénticas de focal $f$ separadas $d$ (Fig. 3.2-5,
p. 90). Mostrar con (3.2-6), (3.2-9), (3.2-9a) que $W_0' = W_0$ solo si $d \le 4f$, la misma
condición de confinamiento de rayos del Ejemplo 1.4-1.

**Ejercicio 3.2-2, Colimación del haz (p. 90).** (a) Mostrar que las posiciones de las
cinturas incidente y transmitida cumplen

$$\frac{z'}{f} - 1 = \frac{z/f - 1}{(z/f - 1)^2 + (z_0/f)^2} \tag{3.2-18}$$

(Fig. 3.2-6, p. 90: $z'/f - 1$ vs. $z/f - 1$ para $z_0/f = 0, 0.25, 0.5, 1$). (b) Colimar =
poner la nueva cintura lo más lejos posible; con $z_0/f$ pequeño (foco corto y $f$ larga),
mostrar que el $z$ óptimo es $z = f + z_0$. (c) Con $\lambda = 1\ \mu$m, $z_0 = 1$ cm,
$f = 50$ cm, hallar $z$ óptimo, $M$, $z'$ y $W_0'$.

**Ejercicio 3.2-3, Expansión del haz (p. 90–91).** Dos lentes $f_1$ (corta) y $f_2$ (larga)
(Fig. 3.2-7, p. 91): $(W_0, z_0) \to (W_0'', z_0'')$ por la primera lente, $\to (W_0', z_0')$
por la segunda; telescopio kepleriano inverso. (a) Con $f_1 \ll z$ y $z - f_1 \gg z_0$, hallar
la distancia $d$ entre lentes que maximiza $z'$. (b) Aumento total $M = W_0'/W_0$.

#### 3.2C Reflection from a Spherical Mirror (p. 91)

Reflectancia de amplitud compleja del espejo $\propto \exp(-jk\rho^2/R)$ (Prob. 2.4-10), con
convención **$R > 0$ convexo, $R < 0$ cóncavo**. El espejo deja el ancho igual y modifica la
fase; el haz reflejado sigue siendo gaussiano (p. 91):

$$W_2 = W_1, \tag{3.2-19}$$
$$\frac{1}{R_2} = \frac{1}{R_1} + \frac{2}{R}. \tag{3.2-20}$$

(3.2-20) es idéntica a (3.2-2) con $f = -R/2$: el espejo actúa como una lente de focal $-R/2$
salvo por la inversión del sentido de propagación. Tres casos (Fig. 3.2-8, p. 91–92):

- Espejo plano ($R = \infty$): $R_2 = R_1$; invierte la dirección sin alterar la curvatura.
- Cintura sobre el espejo ($R_1 = \infty$): $R_2 = R/2$; si es cóncavo ($R < 0$), $R_2 < 0$ y
  el haz converge hacia una mancha más pequeña.
- $R_1 = -R$ (el haz tiene la misma curvatura que el espejo): $R_2 = R$; los frentes de onda
  incidente y reflejado coinciden con el espejo y la onda **retraza su camino** (las normales
  al frente son normales al espejo). En la figura: espejo cóncavo, incidente divergente
  ($R_1 > 0$), reflejado convergente ($R_2 < 0$). *(Base de los resonadores esféricos, cap. 10.)*

**Ejercicio 3.2-4, Espejos de reflectancia variable (p. 92).** Espejo esférico de radio $R$
con reflectancia de intensidad $\mathcal R(\rho) = |r(\rho)|^2 = \exp(-2\rho^2/W_m^2)$
(gaussiana, unidad en el eje, cae $1/e^2$ en $\rho = W_m$). Hallar su efecto sobre un haz
gaussiano con $R_1$ y $W_1$ en el espejo.

#### *3.2D Transmission Through an Arbitrary Optical System (p. 92)

En óptica de rayos paraxial, un sistema se caracteriza por la matriz 2×2
$\mathbf M = (A, B, C, D)$ que relaciona posición e inclinación del rayo transmitido con las
del incidente (§1.4). Fig. 3.2-9 (p. 92): haz $(W_1, R_1, q_1)$ → sistema ABCD → $(W_2, R_2,
q_2)$.

**Ley ABCD** (recuadro, p. 92):

$$\boxed{q_2 = \frac{Aq_1 + B}{Cq_1 + D}.} \tag{3.2-21}$$

Como $q$ determina $W$ y $R$ (Ej. 3.1-3), esta ley gobierna el efecto de cualquier sistema
paraxial sobre un haz gaussiano. Se verifica en casos especiales y se generaliza por
inducción (p. 93):

- **Espacio libre** (o medio homogéneo) de longitud $d$: $A = 1, B = d, C = 0, D = 1$
  (1.4-4). Como $q = z + jz_0$, $q_2 = q_1 + d = (1\cdot q_1 + d)/(0\cdot q_1 + 1)$ ✓ (p. 93).
- **Componente óptico delgado** (Fig. 3.2-10, p. 94): no altera la posición del rayo,
  $y_2 = y_1$ (3.2-22), pero sí la inclinación, $\theta_2 = Cy_1 + D\theta_1$ (3.2-23); así
  $A = 1$, $B = 0$, $C$ y $D$ arbitrarios. En los componentes delgados de §1.4B,
  $D = n_1/n_2$. Por el grosor nulo, $W_2 = W_1$ (3.2-24). Aproximando los haces por ondas
  esféricas de radios $R_1, R_2$ ($\theta_1 \approx y_1/R_1$, $\theta_2 \approx y_2/R_2$):

  $$\frac{1}{R_2} = C + \frac{D}{R_1}. \tag{3.2-25}$$

  Con (3.1-6) y $D = n_1/n_2 = \lambda_2/\lambda_1$, (3.2-24) y (3.2-25) se combinan en

  $$\frac{1}{q_2} = C + \frac{D}{q_1}, \tag{3.2-26}$$

  es decir $q_2 = (1\cdot q_1 + 0)/(Cq_1 + D)$ ✓ (p. 93).
- **Invariancia ante cascada** (p. 93): si la ley vale para $\mathbf M_1$ y $\mathbf M_2$,
  vale para $\mathbf M = \mathbf M_2\mathbf M_1$ (sustitución directa).
- **Generalidad** (p. 94): todo sistema paraxial de interés es combinación de componentes
  delgados y propagación en medios homogéneos; un medio inhomogéneo de variación continua es
  una cascada de elementos delgados y tramos incrementales. Por tanto la ley ABCD se aplica a
  todos ellos mientras los rayos (normales a los frentes de onda) sean paraxiales.

**Ejercicio 3.2-5, Transmisión por una placa transparente (p. 94).** Usar la ley ABCD para
un haz gaussiano que va de aire a una placa de índice $n$ y espesor $d$ y vuelve al aire, con
eje normal a la placa.

### 3.3 Hermite–Gaussian Beams (p. 94)

El haz gaussiano no es la única solución tipo haz de (3.1-2). Interesan soluciones con
intensidad no gaussiana pero con los **mismos frentes de onda paraboloidales**: ajustan las
curvaturas de espejos esféricos de radio grande (resonadores) y se reflejan entre ellos sin
alterarse: son los **modos** del resonador (cap. 9) (p. 94).

Envolvente del haz gaussiano (3.1-5):

$$A_G(x, y, z) = \frac{A_1}{q(z)}\exp\!\left[-jk\frac{x^2 + y^2}{2q(z)}\right],
\qquad q(z) = z + jz_0. \tag{3.3-1}$$

Se busca una segunda onda, versión modulada de la gaussiana (p. 94):

$$A(x, y, z) = \mathcal X\!\left[\sqrt2\frac{x}{W(z)}\right]
\mathcal Y\!\left[\sqrt2\frac{y}{W(z)}\right]\exp[j\mathcal Z(z)]\,A_G(x, y, z), \tag{3.3-2}$$

con $\mathcal X(\cdot)$, $\mathcal Y(\cdot)$, $\mathcal Z(\cdot)$ reales. Propiedades (p. 95):

1. La fase es la del haz gaussiano más un exceso $\mathcal Z(z)$ independiente de $x, y$; si
   $\mathcal Z$ varía lentamente, ambos haces tienen frentes paraboloidales con el mismo $R(z)$
   y se enfocan/reflejan igual.
2. El módulo es

   $$A_0\,\mathcal X\!\left[\sqrt2\frac{x}{W(z)}\right]\mathcal Y\!\left[\sqrt2\frac{y}{W(z)}\right]
   \left[\frac{W_0}{W(z)}\right]\exp\!\left[-\frac{x^2 + y^2}{W^2(z)}\right], \tag{3.3-3}$$

   ($A_0 = A_1/jz_0$): función de $x/W(z)$ y $y/W(z)$; la distribución transversal mantiene su
   forma al variar $z$ salvo el factor de escala $W(z)$. Es una gaussiana modulada por
   $\mathcal X^2$ y $\mathcal Y^2$.

El haz modulado tiene intensidad no gaussiana pero comparte frentes de onda y divergencia
angular con el gaussiano. Sustituyendo (3.3-2) en (3.1-2), con $u = \sqrt2 x/W(z)$,
$v = \sqrt2 y/W(z)$ (p. 95):

$$\frac{1}{\mathcal X}\left(\frac{\partial^2\mathcal X}{\partial u^2} - 2u\frac{\partial\mathcal X}{\partial u}\right)
+ \frac{1}{\mathcal Y}\left(\frac{\partial^2\mathcal Y}{\partial v^2} - 2v\frac{\partial\mathcal Y}{\partial v}\right)
+ kW^2(z)\frac{\partial\mathcal Z}{\partial z} = 0. \tag{3.3-4}$$

Separación de variables (cada término constante: $-2\mu_1$, $-2\mu_2$, $2(\mu_1 + \mu_2)$):

$$-\frac12\frac{d^2\mathcal X}{du^2} + u\frac{d\mathcal X}{du} = \mu_1\mathcal X, \tag{3.3-5a}$$
$$-\frac12\frac{d^2\mathcal Y}{dv^2} + v\frac{d\mathcal Y}{dv} = \mu_2\mathcal Y, \tag{3.3-5b}$$
$$z_0\left[1 + \left(\frac{z}{z_0}\right)^2\right]\frac{d\mathcal Z}{dz} = \mu_1 + \mu_2, \tag{3.3-5c}$$

usando $W(z)$ de (3.1-8) y (3.1-11). (3.3-5a) es un problema de autovalores con $\mu_1 = l$,
$l = 0, 1, 2, \ldots$ y autofunciones los **polinomios de Hermite** $\mathcal X(u) =
\mathbb H_l(u)$ (p. 95), con recurrencia

$$\mathbb H_{l+1}(u) = 2u\,\mathbb H_l(u) - 2l\,\mathbb H_{l-1}(u), \tag{3.3-6}$$
$$\mathbb H_0(u) = 1, \qquad \mathbb H_1(u) = 2u, \tag{3.3-7}$$
$$\mathbb H_2(u) = 4u^2 - 2, \qquad \mathbb H_3(u) = 8u^3 - 12u, \ldots \tag{3.3-8}$$

Análogamente $\mu_2 = m$, $\mathcal Y(v) = \mathbb H_m(v)$. Integrando (3.3-5c) (p. 96):

$$\mathcal Z(z) = (l + m)\,\zeta(z), \tag{3.3-9}$$

con $\zeta(z) = \tan^{-1}(z/z_0)$: el exceso de fase varía lentamente entre
$-(l+m)\pi/2$ y $+(l+m)\pi/2$.

**Amplitud compleja del haz de Hermite–Gauss** (recuadro, p. 96):

$$\boxed{\begin{aligned}
U_{l,m}(x, y, z) = A_{l,m}\left[\frac{W_0}{W(z)}\right]
\mathbb G_l\!\left[\frac{\sqrt2 x}{W(z)}\right]\mathbb G_m\!\left[\frac{\sqrt2 y}{W(z)}\right]
\times\exp\!\left[-jkz - jk\frac{x^2 + y^2}{2R(z)} + j(l + m + 1)\zeta(z)\right]
\end{aligned}} \tag{3.3-10}$$

donde

$$\mathbb G_l(u) = \mathbb H_l(u)\exp\!\left(-\frac{u^2}{2}\right), \qquad l = 0, 1, 2, \ldots \tag{3.3-11}$$

es la **función de Hermite–Gauss** de orden $l$ y $A_{l,m}$ una constante (p. 96).

- $\mathbb G_0(u)$ es la gaussiana; $\mathbb G_1(u) = 2u\,e^{-u^2/2}$ impar;
  $\mathbb G_2(u) = (4u^2 - 2)e^{-u^2/2}$ par; $\mathbb G_3(u) = (8u^3 - 12u)e^{-u^2/2}$ impar
  (Fig. 3.3-1, p. 96).
- El haz de orden $(l, m)$ es el **haz de Hermite–Gauss**; el de orden $(0, 0)$ es el
  gaussiano simple (p. 97).
- **Nota:** la fase de Gouy del modo $(l,m)$ es $(l + m + 1)\zeta(z)$: esto es lo que separa
  en frecuencia los modos transversales de un resonador (Prob. 3.3-4, §10.2D).

**Distribución de intensidad** (p. 97):

$$I_{l,m}(x, y, z) = |A_{l,m}|^2\left[\frac{W_0}{W(z)}\right]^2
\mathbb G_l^2\!\left[\frac{\sqrt2 x}{W(z)}\right]\mathbb G_m^2\!\left[\frac{\sqrt2 y}{W(z)}\right]. \tag{3.3-12}$$

Fig. 3.3-2 (p. 97): intensidades transversales de los órdenes $(0,0)$, $(0,1)$, $(0,2)$,
$(1,1)$, $(1,2)$, $(2,2)$. Los órdenes altos son más anchos; el ancho escala con $W(z)$ en
todos los casos y el patrón se magnifica por $W(z)/W_0$ sin cambiar de forma. **El único
miembro circularmente simétrico de la familia es el gaussiano elemental** (p. 97).

**Ejercicio 3.3-1, El haz dona (p. 97).** Superposición de los haces $(1,0)$ y $(0,1)$ con
igual intensidad y fases aleatorias independientes (las intensidades se suman sin
interferencia). Mostrar que la intensidad total tiene forma de dona circularmente simétrica;
con $W_0 = 1$ mm, hallar el radio de intensidad máxima y los radios de los círculos de $1/e^2$
en la cintura.

### *3.4 Laguerre–Gaussian and Bessel Beams (p. 97)

#### Haces de Laguerre–Gauss (p. 97)

Los haces de Hermite–Gauss forman un **conjunto completo** de soluciones de la ecuación
paraxial de Helmholtz: cualquier otra solución es superposición de ellos. Otro conjunto
completo, los **haces de Laguerre–Gauss**, surge de resolver (3.1-2) en coordenadas cilíndricas
separando variables en $\rho$ y $\phi$ (p. 97). Amplitud compleja (p. 98):

$$\begin{aligned}
U_{l,m}(\rho, \phi, z) = A_{l,m}\left[\frac{W_0}{W(z)}\right]\left(\frac{\rho}{W(z)}\right)^l
\mathbb L_m^l\!\left(\frac{2\rho^2}{W^2(z)}\right)\exp\!\left(-\frac{\rho^2}{W^2(z)}\right)
\times\exp\!\left[-jkz - jk\frac{\rho^2}{2R(z)} - jl\phi + j(l + 2m + 1)\zeta(z)\right],
\end{aligned} \tag{3.4-1}$$

con $\mathbb L_m^l(\cdot)$ el polinomio generalizado de Laguerre, y $W(z)$, $R(z)$, $\zeta(z)$,
$W_0$ de (3.1-8)–(3.1-11). Nota al pie (p. 98), fórmula de Rodrigues:
$\mathbb L_m^l(x) = (x^{-l}e^x/m!)\,(d^m/dx^m)(x^{l+m}e^{-x})$; p. ej. $\mathbb L_0^l(x) = 1$,
$\mathbb L_1^0(x) = 1 - x$, $\mathbb L_2^0(x) = 1 - 2x + x^2/2$.

- El orden más bajo $l = m = 0$ es de nuevo el gaussiano.
- La intensidad depende solo de $\rho, z$: **circularmente simétrica**. Para $l \ne 0$ la
  intensidad es **cero en el eje** y anular (Fig. 3.4-1a, p. 98).
- Fase: igual dependencia en $\rho, z$ que el gaussiano, más el término azimutal $-jl\phi$ y
  una fase de Gouy mayor por el factor $(l + 2m + 1)$. Por la dependencia lineal en $\phi$
  ($l \ne 0$) el frente de onda se **inclina helicoidalmente** al propagarse (Fig. 3.4-1b,
  p. 98, con $l = 1$). Estos haces de fase espiral llevan **momento angular orbital** y pueden
  ejercer torque sobre el sistema iluminado (§5.1 y §12.1D) (p. 98).

#### Haces de Bessel y Bessel–Gauss (p. 98)

Se buscan ondas con frentes **planos** pero intensidad transversal no uniforme (p. 98):

$$U(\mathbf r) = A(x, y)\,e^{-j\beta z}. \tag{3.4-2}$$

Para satisfacer Helmholtz (2.2-7), $\nabla^2 U + k^2 U = 0$, se requiere

$$\nabla_T^2 A + k_T^2 A = 0, \tag{3.4-3}$$

con $k_T^2 + \beta^2 = k^2$ (**ecuación de Helmholtz bidimensional**, p. 99). En coordenadas
polares ($x = \rho\cos\phi$, $y = \rho\sin\phi$), por separación de variables:

$$A(x, y) = A_m\,J_m(k_T\rho)\,e^{jm\phi}, \qquad m = 0, \pm1, \pm2, \ldots, \tag{3.4-4}$$

con $J_m(\cdot)$ la función de Bessel de primera especie y orden $m$ (se excluyen las
soluciones singulares en $\rho = 0$). Para $m = 0$:

$$U(\mathbf r) = A_0\,J_0(k_T\rho)\,e^{-j\beta z}, \tag{3.4-5}$$

el **haz de Bessel**: frentes de onda planos (normales paralelas a $z$), intensidad
$I(\rho, \phi, z) = |A_0|^2 J_0^2(k_T\rho)$ circularmente simétrica e **independiente de $z$**,
sin dispersión de la potencia (Fig. 3.4-2, p. 99).

**Comparación Bessel vs. gaussiano** (p. 99; Fig. 3.4-3, p. 100, con igual pico e igual
ancho $1/e^2$):

- El haz de Bessel es solución **exacta** de Helmholtz; el gaussiano solo aproximada (su
  envolvente es solución exacta de la ecuación *paraxial*).
- Asintóticamente en $\rho$: gaussiano $\sim \exp[-2\rho^2/W^2(z)]$; Bessel
  $J_0^2(k_T\rho) \approx (2/\pi k_T\rho)\cos^2(k_T\rho - \pi/4)$, oscilación sobre una ley de
  potencia inversa lenta.
- Ancho RMS transversal: gaussiano $\sigma = \tfrac12 W(z)$ finito; Bessel **infinito** para
  todo $z$, y la potencia que transporta es infinita. Hay un compromiso entre tamaño mínimo y
  divergencia: el de Bessel no diverge pero su ancho RMS es infinito.
- Generar haces de Bessel exige esquemas especiales (Milonni & Eberly, *Lasers*, 1988,
  §14.14); los gaussianos son modos de resonadores esféricos y los producen naturalmente los
  láseres.
- **Haces de Bessel–Gauss** (Gori, Guattari, Padovani, *Opt. Commun.* 64, 491–495, 1987):
  haz de Bessel modulado por una gaussiana en $\rho$, que actúa como ventana y acelera el
  decaimiento radial (p. 99).

### Reading List (p. 100)

Libros: Dickey, Holswade & Shealy, *Laser Beam Shaping Applications* (CRC, 2006); Dickey &
Holswade (eds.), *Laser Beam Shaping: Theory and Techniques* (Marcel Dekker, 2000); Goldsmith,
*Quasioptical Systems* (Wiley, 1998); Oraevskiy, *Gaussian Beams and Optical Resonators* (Nova,
1996); Arnaud, *Beam and Fiber Optics* (Academic, 1976). Ver también los libros de láseres del
cap. 15. Artículos: número especial *J. Opt. Soc. Am. A* 3(4), 1986; Kogelnik & Li, "Laser
Beams and Resonators", *Proc. IEEE* 54, 1312–1329 (1966); Boyd & Gordon, *Bell Syst. Tech. J.*
40, 489–508 (1961); Fox & Li, *Bell Syst. Tech. J.* 40, 453–488 (1961).

---

## Tablas y datos numéricos útiles

| Dato | Valor | Página |
|---|---|---|
| Fracción de potencia dentro de $\rho_0 = W(z)$ | $1 - e^{-2} \approx 86\,\%$ | 79 |
| Fracción de potencia dentro de $\rho_0 = 1.5\,W(z)$ | $\approx 99\,\%$ | 79 |
| Intensidad relativa en $\rho = W(z)$ | $1/e^2 \approx 0.135$ | 79 |
| Ancho RMS del haz gaussiano | $\sigma = \tfrac12 W(z)$ | 79 |
| Intensidad pico vs. potencia | $I_0 = 2P/\pi W_0^2$ | 78–79 |
| Intensidad en el eje en $z = \pm z_0$ | $I_0/2$ | 78 |
| Ancho en $z = \pm z_0$ | $\sqrt2\,W_0$ | 79 |
| Radio de curvatura mínimo | $R = 2z_0$ en $z = z_0$ | 81 |
| Fase de Gouy en $z_0$ / total acumulada | $\pi/4$ / $\pi$ | 81 |
| Producto cintura–divergencia gaussiano | $2W_0\cdot 2\theta_0 = 4\lambda/\pi$ | 85 |
| He–Ne, $\lambda_0 = 633$ nm, $2W_0 = 2$ cm | $2z_0 \approx 1$ km | 81 |
| He–Ne, $\lambda_0 = 633$ nm, $2W_0 = 20\ \mu$m | $2z_0 \approx 1$ mm | 81 |
| $M^2$ He–Ne | $< 1.1$ | 85 |
| $M^2$ láseres de iones | 1.1–1.3 | 85 |
| $M^2$ diodos láser TEM$_{00}$ colimados | 1.1–1.7 | 85 |
| $M^2$ láseres multimodo de alta energía | hasta 3–4 | 85 |
| Mancha enfocada mínima (lente llena) | $2W_0' \approx (4/\pi)\lambda F_\#$ | 89 |
| Espejo esférico ≡ lente | $f = -R/2$ ($R>0$ convexo, $R<0$ cóncavo) | 91 |
| Condición de *relaying* con lentes idénticas | $d \le 4f$ | 89 |
| Nd:YAG (Prob. 3.1-6) | $\lambda = 1.06\ \mu$m | 100 |
| CO$_2$ (Prob. 3.1-7) | $\lambda_0 = 10.6\ \mu$m | 100 |
| Argón-ión (Probs. 3.2-6, 3.2-7) | $\lambda = 488$ nm | 100–101 |

Relaciones de conversión rápidas (todas de la p. 77 y 80):
$z_0 = \pi W_0^2/\lambda$; $\theta_0 = \lambda/\pi W_0 = W_0/z_0$; $2z_0 = 2\pi W_0^2/\lambda$;
$W_0\theta_0 = \lambda/\pi$; $q(z) = z + jz_0$; $1/q = 1/R - j\lambda/\pi W^2$.

---

## Problemas al final del capítulo (p. 100–101)

Numeración del libro (los problemas de cada sección continúan la numeración de los
ejercicios de esa sección).

- **3.1-6 Beam Parameters.** Nd:YAG, $\lambda = 1.06\ \mu$m, $P = 1$ W, $2\theta_0 = 1$ mrad.
  Hallar $W_0$, profundidad de foco, intensidad máxima e intensidad en el eje a $z = 100$ cm.
- **3.1-7 Beam Identification by Two Widths.** CO$_2$, $\lambda_0 = 10.6\ \mu$m, anchos
  $W_1 = 1.699$ mm y $W_2 = 3.380$ mm en dos puntos separados $d = 10$ cm. Localizar la cintura
  y hallar $W_0$.
- **3.1-8 The Elliptic Gaussian Beam.** Haz con $I(x,y,0) = |A_0|^2\exp[-2(x^2/W_{0x}^2 +
  y^2/W_{0y}^2)]$ (contornos elípticos). Escribir profundidad de foco, divergencia y radios de
  curvatura en $x$ y $y$ en función de $W_{0x}$, $W_{0y}$, $\lambda$. Si $W_{0x} = 2W_{0y}$,
  dibujar la mancha en $z = 0$ y en campo lejano.
- **3.2-6 Beam Focusing.** Argón-ión, $\lambda = 488$ nm, $W_0 = 0.5$ mm. Diseñar un sistema de
  una lente que enfoque a una mancha de 100 $\mu$m de diámetro; ¿cuál es la focal más corta
  admisible?
- **3.2-7 Spot Size.** Haz con $z_0 = 50$ cm, $\lambda = 488$ nm, lente $f = 5$ cm a distancia
  $z$ de la cintura (Fig. 3.2-2). Programar $W_0'$ vs. $z$; verificar que para $z - f \gg z_0$
  valen (3.2-10) y (3.2-12), y que para $z \ll z_0$ vale (3.2-13).
- **3.2-8 Beam Refraction.** Haz de aire ($n = 1$) a un medio de $n = 1.5$ con frontera plana
  normal al eje y cintura en la frontera. Dibujar el haz transmitido; si la divergencia en aire
  es 1 mrad, ¿cuál es en el medio? *(Pista: $\lambda = \lambda_0/n$, $W_0$ no cambia.)*
- ***3.2-9 Transmission Through a Graded-Index Slab.** Placa SELFOC con $n(y) \approx
  n_0(1 - \tfrac12\alpha^2 y^2)$, longitud $d$, matriz $A = \cos\alpha d$, $B = (1/\alpha)
  \sin\alpha d$, $C = -\alpha\sin\alpha d$, $D = \cos\alpha d$ (§1.3B). Haz de $\lambda_0$,
  $W_0$ en espacio libre, entra en su cintura con eje en $z$. Usar la ley ABCD para el ancho en
  $y$ en función de $d$ y dibujar la forma del haz en el medio.
- **3.3-2 Power Confinement in Hermite–Gaussian Beams.** Fracción de potencia dentro de un
  círculo de radio $W(z)$ para los órdenes $(0,0)$, $(1,0)$, $(0,1)$, $(1,1)$; y dentro de
  $\tfrac{1}{10}W(z)$ para $(0,0)$ y $(1,1)$.
- **3.3-3 Superposition of Two Beams.** Dibujar la intensidad de la superposición de $(1,0)$ y
  $(0,1)$ con coeficientes $A_{1,0} = A_{0,1}$ en (3.3-10) (superposición coherente, a
  diferencia del Ej. 3.3-1).
- **3.3-4 Axial Phase.** Modos de Hermite–Gauss de todos los órdenes $(l,m)$ con $z_0 = 30$ cm
  en $n = 1$. Hallar las frecuencias en la banda $\nu = 10^{14} \pm 2\times10^9$ Hz para las
  cuales el retardo de fase entre $z = -z_0$ y $z = z_0$ en el eje es múltiplo entero de $\pi$:
  son los modos de un resonador de dos espejos esféricos en $z = \pm z_0$ (§10.2D).

Ejercicios dentro del texto (ya resumidos arriba): 3.1-1 a 3.1-5 (p. 84–85), 3.2-1 a 3.2-5
(p. 89–94), 3.3-1 (p. 97).

---

## Relación con Óptica No Lineal

**Para el curso (tema 2: haz gaussiano, y temas conexos):**

- *Ondas EM y haz gaussiano.* La §3.1 es la referencia directa del tema 2: deducción desde la
  ecuación paraxial de Helmholtz (3.1-2) y el conjunto (3.1-7)–(3.1-11). Al citar: "Saleh &
  Teich, 2.ª ed., §3.1A, p. 76–77". Las propiedades (intensidad p. 77, potencia p. 78, ancho
  p. 79, divergencia y profundidad de foco p. 80, fase de Gouy p. 81, frentes de onda p. 81–82)
  son el material estándar de taller.
- *Intensidad y potencia para procesos no lineales.* (3.1-16) da $I$ a partir de $P$ y $W(z)$;
  es la fórmula que se usa para estimar $I_0 = 2P/\pi W_0^2$ en el foco y, con ella, el índice
  no lineal $n = n_0 + n_2 I$, la eficiencia de SHG ($\propto I$), la fase SPM, etc. La
  profundidad de foco $2z_0$ (3.1-22) fija la longitud de interacción efectiva en un cristal
  enfocado ("enfoque confocal", $L \approx 2z_0$), y el compromiso mancha pequeña / foco corto
  (p. 80–81) es el que optimiza la conversión de frecuencia (criterio de Boyd–Kleinman).
- *Fase de Gouy.* El desfase $\pi$ total (p. 81) y su generalización $(l+m+1)\zeta$ (p. 96)
  afectan el ajuste de fase en SHG/THG con haces enfocados (el término de Gouy reduce la
  eficiencia de los procesos de orden alto en gas, THG en haz enfocado) y la separación de modos
  transversales en cavidades.
- *Índice dependiente de la intensidad (autoenfoque).* Un perfil gaussiano de intensidad
  (3.1-12) con $n_2 > 0$ produce una lente de Kerr: el formalismo de lente delgada sobre un haz
  gaussiano (3.2-1)–(3.2-9) y la ley ABCD (3.2-21) son exactamente lo que se usa para modelar
  autoenfoque, *Z-scan* (medida de $n_2$ y $\beta$ con un haz enfocado: se necesita $z_0$, $W_0$,
  $W(z)$, $R(z)$) y el *Kerr-lens mode-locking*. El radio de curvatura (3.1-9) y la convención
  de signos (p. 82) son necesarios para esas cuentas.
- *Calidad de haz $M^2$* (p. 85): relevante al reportar divergencia medida y al comparar con
  un haz ideal en el laboratorio; la fórmula de medición (p. 85–86) es un protocolo práctico.
- *Haces de Hermite–Gauss, Laguerre–Gauss y Bessel* (§3.3–3.4): base de modos de resonadores,
  modos transversales de láseres (relación con el tema de cavidades), momento angular orbital
  (interacciones no lineales con vórtices ópticos) y haces de Bessel para generación de
  filamentos y THG con larga longitud de interacción sin divergencia.
- *Ley ABCD* (p. 92–94): se usa para propagar $q$ a través de lentes, placas (Ej. 3.2-5) y
  medios GRIN (Prob. 3.2-9), y en cristales no lineales de longitud finita (placa de índice $n$:
  la cintura efectiva se desplaza $d(1 - 1/n)$).
- *Pulsos en medios dispersivos / GVD / SPM / solitones / Raman / FWM en fibras:* este
  capítulo no los trata directamente, pero el parámetro confocal y la analogía
  espacio–tiempo (difracción paraxial $\leftrightarrow$ dispersión GVD; la ecuación paraxial
  (3.1-2) tiene la misma forma que la ecuación de propagación de pulsos con GVD) permiten
  trasladar los resultados: el "rango de Rayleigh temporal" es la longitud de dispersión
  $L_D$, el autoenfoque espacial es análogo al solitón temporal.
- *Polarización y cristales, χ⁽²⁾, χ⁽³⁾:* el haz gaussiano aquí es escalar; la polarización se
  trata en el cap. 6 y la óptica no lineal en el cap. 21 del mismo libro.

**Para el proyecto final (anillos add-drop en Si₃N₄, dispersión, supercontinuo, sensado):**

- *Acoplamiento a la guía.* El modo fundamental de una guía o fibra se aproxima por un haz
  gaussiano con cierto $W_0$ (radio de campo modal); el acoplamiento desde un láser o fibra a
  la guía de Si₃N₄ se estima con el solapamiento de dos gaussianos y las fórmulas de enfoque
  (3.2-13)–(3.2-17) dan el tamaño de mancha que logra un objetivo o una fibra lente.
- *Intensidad en la guía.* La relación $I_0 = 2P/\pi W_0^2$ (p. 79) es el análogo escalar del
  área efectiva $A_{\rm eff}$ del modo: $\gamma = n_2\omega/(cA_{\rm eff})$ para el
  supercontinuo. El perfil gaussiano es la primera aproximación a $A_{\rm eff}$ antes de usar
  el modo real de MODE/FDE.
- *Modos transversales y resonadores.* Los haces de Hermite–Gauss como modos de cavidades de
  espejos (p. 94, Prob. 3.3-4) son el análogo de espacio libre de los modos del anillo; el
  concepto de retardo de fase por vuelta que fija las frecuencias resonantes es el mismo que se
  usa para el FSR del anillo.
- *Sensado de índice.* Las dependencias con $\lambda = \lambda_0/n$ ($z_0$, $\theta_0$,
  Prob. 3.2-8) ilustran cómo un cambio de índice del medio cambia la propagación; en el anillo
  el efecto equivalente es el cambio de $n_{\rm eff}$ que desplaza la resonancia.
- *Medición de haz y Z-scan en laboratorio.* Si en el proyecto se caracteriza un láser de
  bombeo (divergencia, $M^2$, cintura), el procedimiento de la p. 85–86 y los ejercicios
  3.1-3 a 3.1-5 (identificar un haz a partir de $W$ y $R$ en uno o dos puntos) son las
  herramientas.
