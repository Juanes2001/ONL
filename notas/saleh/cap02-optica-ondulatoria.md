# Capítulo 2 — Wave Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 38–73 (PDF 60–95). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 2.
Notación del libro (se respeta en todo el archivo): dependencia temporal $e^{j\omega t}$ con
$j=\sqrt{-1}$; función de onda real $u(\mathbf r,t)$; función de onda compleja $U(\mathbf r,t)$;
amplitud compleja $U(\mathbf r)$ (independiente del tiempo); envolvente compleja $A$ (o $A(\mathbf r)$,
$\mathcal A(t)$ para pulsos); $c_o$ = velocidad de la luz en el vacío, $c=c_o/n$; $k_o=2\pi/\lambda_o$,
$k=nk_o$. Unidades SI (el libro expresa la intensidad en W/cm²; en estos apuntes se anota la unidad
del libro cuando aparece).

---

## Resumen del capítulo

El capítulo construye la **óptica ondulatoria escalar**: la luz se describe por una función de onda
real $u(\mathbf r,t)$ que satisface la ecuación de onda, y la intensidad óptica es proporcional al
promedio temporal de $u^2$ (§2.1, p. 40). Para ondas monocromáticas se introduce la representación
compleja $U(\mathbf r,t)=U(\mathbf r)e^{j2\pi\nu t}$, la ecuación de Helmholtz para la amplitud
compleja y la regla $I=|U|^2$ (§2.2A, p. 42); con ella se estudian la onda plana, la esférica, su
aproximación de Fresnel (paraboloidal) y las ondas paraxiales con la ecuación de Helmholtz paraxial
(§2.2B–C, pp. 44–48). La §2.3 (p. 49) muestra que la óptica de rayos es el límite
$\lambda_o\to 0$ de la óptica ondulatoria (ecuación eikonal). La §2.4 (p. 50) trata la reflexión y
refracción como *empate de fases* en la frontera (leyes de reflexión y Snell) y describe placas,
prismas, lentes delgadas, redes de difracción y componentes de índice gradual mediante la
transmitancia de amplitud compleja $\mathfrak t(x,y)$. La §2.5 (p. 58) desarrolla la interferencia
de dos ondas (ecuación de interferencia, interferómetros Mach–Zehnder, Michelson, Sagnac, ondas
planas oblicuas, patrones de Young) y de $M$ ondas e infinitas ondas (fórmula tipo Fabry–Perot,
finura $\mathcal F$, reflexión de Bragg). La §2.6 (p. 66) extiende el formalismo a luz
policromática y pulsada: señal analítica compleja, intensidad $I=|U(\mathbf r,t)|^2$ para luz
cuasi-monocromática, onda plana pulsada, batido óptico y generación de trenes de pulsos por
interferencia de $M$ modos equiespaciados (preludio al mode-locking).

---

## Secciones

### 2.0 Introducción (pp. 39–40)

- La luz se propaga como ondas; en el vacío con velocidad constante $c_o=3.0\times10^8$ m/s
  (30 cm/ns = 0.3 mm/ps = 0.3 μm/fs). (p. 39)
- **Rango óptico** (Fig. 2.0-1, p. 39): infrarrojo 0.76–300 μm (NIR, MIR, FIR); visible 390–760 nm;
  ultravioleta 10–390 nm (NUV, MUV, FUV, EUV = XUV = «soft X-rays»; VUV = FUV + EUV). En
  frecuencia: de 1 THz (FIR) a $3\times10^{16}$ Hz (EUV). Las tres regiones se llaman «ópticas»
  porque usan el mismo tipo de componentes (lentes, espejos).
- Límites de los colores en Fig. 2.0-1 (nm, en el vacío): rojo 760–622, naranja 622–597, amarillo
  597–577, verde 577–492, azul 492–455, violeta 455–390.
- **Fig. 2.0-2** (p. 40): la óptica ondulatoria *contiene* a la óptica de rayos; ésta es el límite
  de longitud de onda infinitesimal. Mientras los objetos sean mucho mayores que $\lambda$, los
  rayos bastan.
- Alcance y límites (p. 40): la óptica ondulatoria escalar explica interferencia y difracción, pero
  **no** da la imagen completa de reflexión/refracción en fronteras dieléctricas ni los efectos de
  polarización (requieren formulación vectorial, cap. 5). El significado físico de $u$ (componente
  del campo eléctrico o magnético) se difiere al cap. 5.

### 2.1 Postulados de la óptica ondulatoria (p. 40)

**La ecuación de onda.** Un medio homogéneo transparente se caracteriza por su índice de refracción
$n\ (\ge1)$; en él la luz viaja con velocidad reducida (recuadro, p. 40):

$$c=\frac{c_o}{n}. \tag{2.1-1}$$

La onda se describe por una función real de posición $\mathbf r=(x,y,z)$ y tiempo $t$,
$u(\mathbf r,t)$, la **función de onda** (*wavefunction*), que satisface la **ecuación de onda**
(recuadro, p. 40):

$$\nabla^2u-\frac{1}{c^2}\frac{\partial^2u}{\partial t^2}=0, \tag{2.1-2}$$

con $\nabla^2=\partial^2/\partial x^2+\partial^2/\partial y^2+\partial^2/\partial z^2$. Toda
función que satisfaga (2.1-2) es una onda óptica posible.

- **Principio de superposición** (p. 41): la ecuación es lineal, así que si $u_1$ y $u_2$ son ondas
  posibles, $u=u_1+u_2$ también lo es.
- En la frontera entre dos medios la función de onda cambia según los índices; las leyes de ese
  cambio dependen del significado físico de $u$ (cap. 5). El origen físico de $n$ viene de la óptica
  electromagnética (§5.5B). (p. 41)
- **Medios localmente homogéneos** (p. 41): si $n$ depende de la posición pero varía lentamente en
  distancias del orden de $\lambda$, la ecuación de onda sigue valiendo aproximadamente con
  $n(\mathbf r)$ y $c(\mathbf r)$.

**Intensidad, potencia y energía** (p. 41). La **intensidad óptica** $I(\mathbf r,t)$, potencia por
unidad de área (el libro la da en W/cm²), es proporcional al promedio del cuadrado de la función de
onda (recuadro):

$$I(\mathbf r,t)=2\langle u^2(\mathbf r,t)\rangle. \tag{2.1-3}$$

$\langle\cdot\rangle$ promedia sobre un intervalo mucho mayor que un ciclo óptico pero mucho menor
que cualquier otro tiempo de interés (p. ej. la duración de un pulso). Un ciclo óptico dura
$2\times10^{-15}$ s = 2 fs a 600 nm. El factor 2 es una convención (podría absorberse en $u$ con un
factor $\sqrt2$); resultará conveniente después. La **potencia óptica** $P(t)$ (W) que atraviesa un
área $A$ normal a la propagación es

$$P(t)=\int_A I(\mathbf r,t)\,dA, \tag{2.1-4}$$

y la **energía óptica** (J) recogida en un intervalo es la integral de $P$ sobre ese intervalo.

### 2.2 Ondas monocromáticas (p. 41) — tema 1 del curso de ONL

Una onda monocromática tiene dependencia temporal armónica (p. 41):

$$u(\mathbf r,t)=\mathfrak a(\mathbf r)\cos[2\pi\nu t+\varphi(\mathbf r)], \tag{2.2-1}$$

con (p. 42): $\mathfrak a(\mathbf r)$ = amplitud; $\varphi(\mathbf r)$ = fase; $\nu$ = frecuencia
(ciclos/s o Hz); $\omega=2\pi\nu$ = frecuencia angular (rad/s o s⁻¹); $T=1/\nu=2\pi/\omega$ =
período (s). Amplitud y fase dependen de la posición, pero la onda es armónica en $t$ con la misma
$\nu$ en todo punto. Frecuencias ópticas: $3\times10^{11}$ a $3\times10^{16}$ Hz.

**Fig. 2.2-1** (p. 42): (a) $u(t)$ en un punto fijo: sinusoide de período $T=1/\nu$, amplitud
$\mathfrak a$ y desplazamiento $\varphi/\omega$; (b) la amplitud compleja $U=\mathfrak a\,e^{j\varphi}$
como fasor fijo; (c) la función de onda compleja $U(t)=U e^{j2\pi\nu t}$ como fasor que gira con
velocidad angular $\omega=2\pi\nu$ rad/s.

#### 2.2A Representación compleja y ecuación de Helmholtz (p. 42)

**Función de onda compleja.** Se define

$$U(\mathbf r,t)=\mathfrak a(\mathbf r)\exp[j\varphi(\mathbf r)]\exp(j2\pi\nu t), \tag{2.2-2}$$

de modo que

$$u(\mathbf r,t)=\operatorname{Re}\{U(\mathbf r,t)\}=\tfrac12[U(\mathbf r,t)+U^*(\mathbf r,t)], \tag{2.2-3}$$

donde $^*$ es la conjugación compleja. $U(\mathbf r,t)$ describe la onda por completo; $u$ es su
parte real. $U$ también satisface la ecuación de onda (recuadro, p. 42):

$$\nabla^2U-\frac{1}{c^2}\frac{\partial^2U}{\partial t^2}=0, \tag{2.2-4}$$

y ambas funciones cumplen las mismas condiciones de frontera.

**Amplitud compleja** (p. 43). (2.2-2) se escribe

$$U(\mathbf r,t)=U(\mathbf r)\exp(j2\pi\nu t), \tag{2.2-5}$$

con $U(\mathbf r)=\mathfrak a(\mathbf r)\exp[j\varphi(\mathbf r)]$ la **amplitud compleja**
(independiente del tiempo). Entonces

$$u(\mathbf r,t)=\operatorname{Re}\{U(\mathbf r)\exp(j2\pi\nu t)\}=\tfrac12[U(\mathbf r)\exp(j2\pi\nu t)+U^*(\mathbf r)\exp(-j2\pi\nu t)]. \tag{2.2-6}$$

$|U(\mathbf r)|=\mathfrak a(\mathbf r)$ es la amplitud y $\arg\{U(\mathbf r)\}=\varphi(\mathbf r)$ la
fase; $U(\mathbf r)$ es el valor inicial ($t=0$) del fasor rotante $U(\mathbf r,t)$.

**Ecuación de Helmholtz** (p. 43). Sustituyendo (2.2-5) en (2.2-4) (recuadro):

$$\nabla^2U+k^2U=0, \tag{2.2-7}$$

donde (recuadro)

$$k=\frac{2\pi\nu}{c}=\frac{\omega}{c} \tag{2.2-8}$$

es el **número de onda**. Distintas condiciones de frontera dan distintas soluciones.

**Intensidad óptica** (p. 43). Insertando (2.2-1) en (2.1-3):

$$2u^2(\mathbf r,t)=2\mathfrak a^2(\mathbf r)\cos^2[2\pi\nu t+\varphi(\mathbf r)]=|U(\mathbf r)|^2\{1+\cos(2[2\pi\nu t+\varphi(\mathbf r)])\}. \tag{2.2-9}$$

Promediando sobre un tiempo mayor que $1/\nu$ el segundo término se anula (recuadro):

$$I(\mathbf r)=|U(\mathbf r)|^2. \tag{2.2-10}$$

> *La intensidad óptica de una onda monocromática es el módulo al cuadrado de su amplitud
> compleja.* La intensidad de una onda monocromática **no** varía con el tiempo. (p. 43)

**Frentes de onda** (p. 44): superficies de fase constante, $\varphi(\mathbf r)=$ const,
usualmente $\varphi(\mathbf r)=2\pi q$ con $q$ entero. La normal al frente en $\mathbf r$ es
paralela a $\nabla\varphi(\mathbf r)$ (componentes $\partial\varphi/\partial x$, etc.): dirección
de máxima tasa de cambio de la fase.

**Recuadro «Summary»** (p. 44):
- Una onda monocromática de frecuencia $\nu$ se describe por la función de onda compleja
  $U(\mathbf r,t)=U(\mathbf r)\exp(j2\pi\nu t)$, que satisface la ecuación de onda.
- La amplitud compleja $U(\mathbf r)$ satisface la ecuación de Helmholtz; $|U(\mathbf r)|$ y
  $\arg\{U(\mathbf r)\}$ son la amplitud y la fase; $I(\mathbf r)=|U(\mathbf r)|^2$; los frentes de
  onda son $\varphi(\mathbf r)=\arg\{U(\mathbf r)\}=2\pi q$.
- $u(\mathbf r,t)=\operatorname{Re}\{U(\mathbf r,t)\}$ también satisface la ecuación de onda.

#### 2.2B Ondas elementales (p. 44)

Las soluciones más simples de Helmholtz en medio homogéneo: onda plana y onda esférica.

**Onda plana** (p. 44):

$$U(\mathbf r)=A\exp(-j\mathbf k\cdot\mathbf r)=A\exp[-j(k_xx+k_yy+k_zz)], \tag{2.2-11}$$

$A$ = constante compleja llamada **envolvente compleja**; $\mathbf k=(k_x,k_y,k_z)$ = **vector de
onda**. Sustituir en (2.2-7) da $k_x^2+k_y^2+k_z^2=k^2$: el módulo de $\mathbf k$ es el número de
onda $k$. La fase es $\arg\{A\}-\mathbf k\cdot\mathbf r$; los frentes de onda cumplen
$\mathbf k\cdot\mathbf r=2\pi q+\arg\{A\}$: planos paralelos perpendiculares a $\mathbf k$,
separados por $\lambda=2\pi/k$, es decir (recuadro):

$$\lambda=\frac{c}{\nu}, \tag{2.2-12}$$

la **longitud de onda**. La onda plana tiene intensidad constante $I(\mathbf r)=|A|^2$ en todo el
espacio, luego transporta potencia infinita: es una idealización. Con el eje $z$ a lo largo de
$\mathbf k$, $U(\mathbf r)=A\exp(-jkz)$ y, por (2.2-6),

$$u(\mathbf r,t)=|A|\cos[2\pi\nu t-kz+\arg\{A\}]=|A|\cos[2\pi\nu(t-z/c)+\arg\{A\}]. \tag{2.2-13}$$

Periódica en $t$ con período $1/\nu$ y en $z$ con período $2\pi/k=\lambda$ (**Fig. 2.2-2**, p. 45).
Como la fase $2\pi\nu(t-z/c)+\arg\{A\}$ depende de $t-z/c$, $c$ es la **velocidad de fase**.

En un medio de índice $n$ (p. 45): velocidad de fase $c=c_o/n$, $\lambda=c/\nu=c_o/n\nu=\lambda_o/n$
con $\lambda_o=c_o/\nu$ la longitud de onda en el vacío; el número de onda $k=2\pi/\lambda$ aumenta
en el factor $n$ respecto a $k_o=2\pi/\lambda_o$.

> *Al propagarse por medios de distinto índice, la frecuencia de la onda monocromática se
> conserva, pero velocidad, longitud de onda y número de onda cambian* (recuadro, p. 45):

$$c=\frac{c_o}{n},\qquad \lambda=\frac{\lambda_o}{n},\qquad k=nk_o. \tag{2.2-14}$$

Las longitudes de onda de la Fig. 2.0-1 son en el vacío ($n=1$).

**Onda esférica** (p. 45), solución de Helmholtz en coordenadas esféricas:

$$U(\mathbf r)=\frac{A_0}{r}\exp(-jkr), \tag{2.2-15}$$

$r$ = distancia al origen, $k=2\pi\nu/c=\omega/c$, $A_0$ constante. Intensidad
$I(\mathbf r)=|A_0|^2/r^2$ (inversa al cuadrado de la distancia). Con $\arg\{A_0\}=0$, los frentes
son $kr=2\pi q$, o $r=q\lambda$: esferas concéntricas separadas $\lambda=2\pi/k$ que avanzan
radialmente con velocidad $c$ (**Fig. 2.2-3**, p. 46). Onda esférica con origen en $\mathbf r_0$:
$U(\mathbf r)=(A_0/|\mathbf r-\mathbf r_0|)\exp(-jk|\mathbf r-\mathbf r_0|)$. La onda
$U(\mathbf r)=(A_0/r)\exp(+jkr)$ es esférica **entrante** (hacia el origen).

**Aproximación de Fresnel de la onda esférica: onda paraboloidal** (p. 46). Para puntos cerca del
eje $z$ y lejos del origen, $\sqrt{x^2+y^2}\ll z$; con $\theta^2=(x^2+y^2)/z^2\ll1$:

$$r=\sqrt{x^2+y^2+z^2}=z\sqrt{1+\theta^2}=z\Big(1+\frac{\theta^2}{2}-\frac{\theta^4}{8}+\cdots\Big)\approx z\Big(1+\frac{\theta^2}{2}\Big)=z+\frac{x^2+y^2}{2z}. \tag{2.2-16}$$

Esta expresión se sustituye en la **fase** de (2.2-15); en el **módulo** basta $r\approx z$ (menos
sensible a errores). Resultado (recuadro, p. 46):

$$U(\mathbf r)\approx\frac{A_0}{z}\exp(-jkz)\exp\Big[-jk\frac{x^2+y^2}{2z}\Big]. \tag{2.2-17}$$

Interpretación: onda plana $A_0\exp(-jkz)$ modulada por $(1/z)\exp[-jk(x^2+y^2)/2z]$; el factor
de fase $k(x^2+y^2)/2z$ curva los frentes planos en paraboloides ($(x^2+y^2)/z=$ const). Para $z$
muy grande el factor paraboloidal tiende a 0 y la onda esférica tiende a la plana $\exp(-jkz)$
(**Fig. 2.2-4**, p. 47: esférica → ≈ paraboloidal → ≈ plana). Clave para la difracción (cap. 4).

**Condición de validez** (pp. 46–47): no basta $\theta^2\ll1$; el término $\theta^4/8$,
multiplicado por $kz$, puede hacerse comparable a $\pi$. Se requiere $kz\theta^4/8\ll\pi$, es
decir $(x^2+y^2)^2\ll4z^3\lambda$. Para puntos dentro de un círculo de radio $a$ centrado en el
eje $z$: $a^4\ll4z^3\lambda$, o

$$\frac{N_F\theta_m^2}{4}\ll1, \tag{2.2-18}$$

con $\theta_m=a/z$ el ángulo máximo y (recuadro, p. 47)

$$N_F=\frac{a^2}{\lambda z} \tag{2.2-19}$$

el **número de Fresnel**.

**Ejercicio 2.2-1, Validez de la aproximación de Fresnel** (p. 47): hallar el radio del círculo
dentro del cual una onda esférica de $\lambda=633$ nm, originada a 1 m, puede aproximarse por una
paraboloidal; hallar $\theta_m$ y $N_F$. *Cálculo propio* (el libro no da la respuesta): la cota
$a^4=4z^3\lambda=4(1)^3(633\times10^{-9})=2.53\times10^{-6}$ m⁴ da $a\approx4.0$ cm, con lo que
$\theta_m=a/z\approx0.04$ rad y $N_F=a^2/\lambda z\approx2.5\times10^3$; para cumplir «$\ll$» hay que
tomar $a$ sensiblemente menor (p. ej. $a\approx1$–2 cm, $N_F\sim10^2$–$10^3$).

#### 2.2C Ondas paraxiales (p. 47)

Una onda es **paraxial** si las normales a sus frentes son rayos paraxiales. Se construye tomando
una onda plana portadora $A\exp(-jkz)$ y «modulando» su envolvente compleja para hacerla
lentamente variable con la posición:

$$U(\mathbf r)=A(\mathbf r)\exp(-jkz). \tag{2.2-20}$$

$A(\mathbf r)$ y su derivada deben variar lentamente en la distancia $\lambda=2\pi/k$ para que la
onda conserve su carácter de onda plana. Función de onda:
$u(\mathbf r,t)=|A(\mathbf r)|\cos[2\pi\nu t-kz+\arg\{A(\mathbf r)\}]$ (**Fig. 2.2-5**, p. 48: (a)
sinusoide en $z$ de amplitud y fase lentamente variables; (b) frentes ligeramente curvados cuyas
normales son rayos paraxiales).

**Ecuación de Helmholtz paraxial** (p. 48). La variación lenta en $\Delta z=\lambda$ significa
$\Delta A\ll A$ (aplicado por separado a partes real e imaginaria); como
$\Delta A=(\partial A/\partial z)\lambda$, se tiene $\partial A/\partial z\ll A/\lambda=Ak/2\pi$:

$$\frac{\partial A}{\partial z}\ll kA. \tag{2.2-21}$$

La derivada también debe variar lentamente en $\lambda$: $\partial^2A/\partial z^2\ll k\,\partial A/\partial z$, luego

$$\frac{\partial^2A}{\partial z^2}\ll k^2A. \tag{2.2-22}$$

Sustituyendo (2.2-20) en (2.2-7) y despreciando $\partial^2A/\partial z^2$ frente a
$k\,\partial A/\partial z$ o $k^2A$ (recuadro, p. 48):

$$\nabla_T^2A-j2k\frac{\partial A}{\partial z}=0, \tag{2.2-23}$$

con $\nabla_T^2=\partial^2/\partial x^2+\partial^2/\partial y^2$ el laplaciano transversal. Es la
**aproximación de envolvente lentamente variable** (*slowly varying envelope approximation*, SVEA)
de la ecuación de Helmholtz; se parece a la ecuación de Schrödinger [(13.1-1)]. Su solución más
simple es la onda paraboloidal (Ejercicio 2.2-2); la más útil, el **haz gaussiano** (cap. 3).

**Ejercicio 2.2-2, Onda paraboloidal y haz gaussiano** (pp. 48–49): verificar que
$A(\mathbf r)=(A_0/z)\exp[-jk(x^2+y^2)/2z]$ [de (2.2-17)] satisface (2.2-23); mostrar que
$A(\mathbf r)=[A_1/q(z)]\exp[-jk(x^2+y^2)/2q(z)]$ con $q(z)=z+jz_0$, $z_0$ constante, también la
satisface (haz gaussiano, cap. 3); bosquejar la intensidad del haz gaussiano en $z=0$.

### *2.3 Relación entre óptica ondulatoria y óptica de rayos (p. 49)

Se demuestra que la óptica de rayos emerge como límite $\lambda_o\to0$. Para un medio con
$n(\mathbf r)$ lentamente variable (localmente homogéneo) se escribe la amplitud compleja como

$$U(\mathbf r)=\mathfrak a(\mathbf r)\exp[-jk_oS(\mathbf r)], \tag{2.3-1}$$

$\mathfrak a(\mathbf r)$ = módulo, $-k_oS(\mathbf r)$ = fase, $k_o=2\pi/\lambda_o$; $\mathfrak a$ se
toma constante en la escala de $\lambda_o$. Los frentes son $S(\mathbf r)=$ const con normal
$\nabla S$. Cerca de $\mathbf r_0$ la onda es localmente plana con amplitud $\mathfrak a(\mathbf r_0)$
y vector de onda de módulo $k=n(\mathbf r_0)k_o$ paralelo a $\nabla S$. Los rayos de la óptica
geométrica son normales a las superficies de nivel del eikonal $S(\mathbf r)$ (§1.3C), así que los
vectores de onda locales se identifican con los rayos y $S(\mathbf r)$ (proporcional a la fase) con
el eikonal (**Fig. 2.3-1**, p. 49: (a) rayos ortogonales a frentes planos y esféricos; (b) efecto de
una lente sobre rayos y frentes).

**Ecuación eikonal** (pp. 49–50). Sustituyendo (2.3-1) en (2.2-7):

$$k_o^2\big[n^2-|\nabla S|^2\big]\mathfrak a+\nabla^2\mathfrak a-jk_o\big[2\nabla S\cdot\nabla\mathfrak a+\mathfrak a\nabla^2S\big]=0. \tag{2.3-2}$$

Parte real e imaginaria deben anularse por separado. De la parte real, con $k_o=2\pi/\lambda_o$:

$$|\nabla S|^2=n^2+\Big(\frac{\lambda_o}{2\pi}\Big)^2\frac{\nabla^2\mathfrak a}{\mathfrak a}. \tag{2.3-3}$$

Como $\mathfrak a$ varía lentamente en $\lambda_o$, $\lambda_o^2\nabla^2\mathfrak a/\mathfrak a\ll1$ y
en el límite $\lambda_o\to0$ (recuadro, p. 50):

$$|\nabla S|^2\approx n^2. \tag{2.3-4}$$

Es la ecuación eikonal (1.3-20), postulado principal de la óptica de rayos (equivalente al principio
de Fermat). $S(\mathbf r_B)-S(\mathbf r_A)$ es la longitud de camino óptico entre $\mathbf r_A$ y
$\mathbf r_B$. La parte imaginaria de (2.3-2) relaciona $\mathfrak a$ con $S$ y permite determinar la
función de onda.

### 2.4 Componentes ópticos simples (p. 50)

#### 2.4A Reflexión y refracción (p. 50)

**Reflexión en espejo plano** (p. 50). Onda plana $\mathbf k_1$ incide sobre un espejo en $z=0$ en
el vacío; se genera una reflejada $\mathbf k_2$; ángulos $\theta_1$, $\theta_2$ (**Fig. 2.4-1**,
p. 51). La suma satisface Helmholtz si $k_1=k_2=k_o$. Las condiciones de frontera son iguales en
todo $(x,y)$ del espejo, así que los frentes deben empatar:

$$\mathbf k_1\cdot\mathbf r=\mathbf k_2\cdot\mathbf r\quad\text{para todo }\mathbf r=(x,y,0). \tag{2.4-1}$$

Con $\mathbf k_1=(k_o\sin\theta_1,0,k_o\cos\theta_1)$ y $\mathbf k_2=(k_o\sin\theta_2,0,-k_o\cos\theta_2)$:
$k_ox\sin\theta_1=k_ox\sin\theta_2\Rightarrow\theta_1=\theta_2$ (ley de reflexión, ahora para
vectores de onda).

**Reflexión y refracción en frontera dieléctrica plana** (pp. 50–51). Medios $n_1$, $n_2$;
frontera $z=0$; ondas refractada $\mathbf k_2$ y reflejada $\mathbf k_3$ (**Fig. 2.4-2**, p. 51).
Helmholtz se cumple si $k_1=k_3=n_1k_o$ y $k_2=n_2k_o$. Empate de frentes:

$$\mathbf k_1\cdot\mathbf r=\mathbf k_2\cdot\mathbf r=\mathbf k_3\cdot\mathbf r\quad\text{para todo }\mathbf r=(x,y,0). \tag{2.4-2}$$

Con $\mathbf k_1=(n_1k_o\sin\theta_1,0,n_1k_o\cos\theta_1)$,
$\mathbf k_3=(n_1k_o\sin\theta_3,0,-n_1k_o\cos\theta_3)$,
$\mathbf k_2=(n_2k_o\sin\theta_2,0,n_2k_o\cos\theta_2)$ resulta $\theta_1=\theta_3$ y
$n_1\sin\theta_1=n_2\sin\theta_2$ (**ley de Snell**). Pie de Fig. 2.4-2: la distancia
$\overline{P_1P_2}$ sobre la frontera es $\lambda_1/\sin\theta_1=\lambda_o/n_1\sin\theta_1$ para la
incidente y $\lambda_2/\sin\theta_2=\lambda_o/n_2\sin\theta_2$ para la refractada; igualarlas da
Snell. **Las amplitudes** de las ondas reflejada y refractada **no** pueden obtenerse con óptica
escalar (condiciones de frontera incompletas): se hace en §6.2 con óptica electromagnética.

#### 2.4B Transmisión a través de componentes ópticos (p. 51)

Se ignoran las reflexiones en las superficies (no tratables en teoría escalar) y la absorción
(§5.5). El énfasis está en el **desfase** introducido y la curvatura de los frentes.

**Placa transparente** (p. 52). Placa de índice $n$, espesor $d$, entre $z=0$ y $z=d$, rodeada de
vacío; onda incidente a lo largo de $z$ (**Fig. 2.4-3**, p. 52: $\lambda_o$ fuera, $\lambda$ dentro).
$U(x,y,z)$ se supone continua en las fronteras. La razón
$\mathfrak t(x,y)=U(x,y,d)/U(x,y,0)$ es la **transmitancia de amplitud compleja**. Dentro, la onda
es plana con número de onda $nk_o$, $U\propto\exp(-jnk_oz)$, luego (recuadro):

$$\mathfrak t(x,y)=\exp(-jnk_od). \tag{2.4-3}$$

La placa introduce un desfase $nk_od=2\pi(d/\lambda)$. (Reflexión: §6.2; reflexiones múltiples
internas: §10.1.)

Incidencia oblicua a ángulo $\theta$ (**Fig. 2.4-4**, p. 53): dentro, ángulo $\theta_1$ con
$\sin\theta=n\sin\theta_1$ (Snell) y $U\propto\exp[-jnk_o(z\cos\theta_1+x\sin\theta_1)]$, así que

$$\mathfrak t(x,y)=\exp(-jnk_od\cos\theta_1). \tag{2.4-4}$$

Si $\theta$ es pequeño (onda paraxial), $\theta_1\approx\theta/n$ y $\cos\theta_1\approx1-\tfrac12\theta_1^2$
dan $\mathfrak t\approx\exp(-jnk_od)\exp(jk_o\theta^2d/2n)$. Si la placa es suficientemente
delgada y $\theta$ pequeño, de modo que $k_o\theta^2d/2n\ll2\pi$ [o $(d/\lambda_o)\theta^2/2n\ll1$],
vale (2.4-3): la transmitancia es aproximadamente independiente del ángulo.

**Placa delgada de espesor variable** (pp. 52–53). Espesor $d(x,y)$ suave, placa entre $z=0$ y
$z=d_0$ (**Fig. 2.4-5**, p. 53); onda incidente paraxial arbitraria. Localmente, la onda cruza
material de espesor $d(x,y)$ y aire de espesor $d_0-d(x,y)$; el producto de transmitancias
$\mathfrak t\approx\exp[-jnk_od(x,y)]\exp[-jk_o(d_0-d(x,y))]$ da (recuadro):

$$\mathfrak t(x,y)\approx h_0\exp[-j(n-1)k_od(x,y)], \tag{2.4-5}$$

con $h_0=\exp(-jk_od_0)$ factor de fase constante. Válida en la aproximación paraxial y para $d_0$
tan pequeño que $(d_0/\lambda_o)\theta^2/2n\ll1$.

**Ejercicio 2.4-1, Transmisión a través de un prisma** (p. 53, **Fig. 2.4-6**, p. 54): usar
(2.4-5) para mostrar que un prisma delgado invertido de ángulo de ápice $\alpha\ll1$ y espesor
$d_0$ tiene $\mathfrak t(x,y)=h_0\exp[-j(n-1)k_o\alpha x]$, $h_0=\exp(-jk_od_0)$. Efecto sobre una
onda plana en $z$: la fase lineal en $x$ la convierte en onda plana desviada un ángulo
$(n-1)\alpha$; comparar con el modelo de rayos (1.2-7).

**Lente delgada** (p. 54). Lente planoconvexa (**Fig. 2.4-7**, p. 55), casquete de esfera de
radio $R$: $d(x,y)=d_0-\overline{PQ}=d_0-(R-\overline{QC})$:

$$d(x,y)=d_0-\Big[R-\sqrt{R^2-(x^2+y^2)}\Big]. \tag{2.4-6}$$

Para $x^2+y^2\ll R^2$:

$$\sqrt{R^2-(x^2+y^2)}=R\sqrt{1-\frac{x^2+y^2}{R^2}}\approx R\Big(1-\frac{x^2+y^2}{2R^2}\Big) \tag{2.4-7}$$

(misma serie de Taylor de la aproximación de Fresnel), luego

$$d(x,y)\approx d_0-\frac{x^2+y^2}{2R}, \tag{2.4-8}$$

y sustituyendo en (2.4-5) (recuadro, p. 54):

$$\mathfrak t(x,y)\approx h_0\exp\Big[jk_o\frac{x^2+y^2}{2f}\Big], \tag{2.4-9}$$

con

$$f=\frac{R}{n-1} \tag{2.4-10}$$

la distancia focal (§1.2C) y $h_0=\exp(-jnk_od_0)$ otro factor de fase constante sin importancia.
Como la lente imprime una fase $\propto x^2+y^2$, convierte frentes planos en frentes paraboloidales
centrados a distancia $f$ (Ejercicio 2.4-3).

**Ejercicio 2.4-2, Lente doble-convexa** (p. 55, **Fig. 2.4-8**): mostrar que la lente esférica
tiene transmitancia (2.4-9) con

$$\frac1f=(n-1)\Big(\frac1{R_1}-\frac1{R_2}\Big) \tag{2.4-11}$$

(vía (2.4-5) o como cascada de dos planoconvexas; convención: radio positivo/negativo para
superficie convexa/cóncava; $R_1>0$, $R_2<0$ en la figura; cf. (1.2-12)).

**Ejercicio 2.4-3, Enfoque de una onda plana por una lente delgada** (p. 55, **Fig. 2.4-9**):
mostrar que una onda plana paralela al eje se convierte en onda paraboloidal (aproximación de
Fresnel de la esférica) centrada a distancia $f$; ¿qué pasa con una onda plana incidente a ángulo
pequeño $\theta$? (el foco se desplaza lateralmente $\approx f\theta$ en el plano focal).

**Ejercicio 2.4-4, Propiedad de formación de imágenes** (p. 55, **Fig. 2.4-10**): una onda
paraboloidal centrada en $P_1$ se convierte en otra centrada en $P_2$, con
$1/z_1+1/z_2=1/f$ (**ecuación de imagen**).

**Redes de difracción** (p. 56). Componente que modula periódicamente fase o amplitud: placa de
espesor periódico, índice periódico (§2.4C), arreglos de aperturas/obstáculos (§4.3), o película de
aluminio rayada sobre vidrio (red de reflexión). Placa delgada en $z=0$ con espesor periódico en
$x$ de período $\Lambda$ (**Fig. 2.4-11**, p. 56): convierte una onda plana de $\lambda\ll\Lambda$,
incidente a ángulo pequeño $\theta_i$, en varias ondas planas a ángulos (recuadro):

$$\theta_q=\theta_i+q\frac{\lambda}{\Lambda}, \tag{2.4-12}$$

$q=0,\pm1,\pm2,\dots$ = **orden de difracción**; ondas sucesivas separadas por $\theta=\lambda/\Lambda$.

**Ejercicio 2.4-5, Transmisión a través de una red de difracción** (p. 56): (a) placa con
$d(x,y)=\tfrac12d_0[1+\cos(2\pi x/\Lambda)]$: mostrar que
$\mathfrak t(x,y)=h_0\exp[-j\tfrac12(n-1)k_od_0\cos(2\pi x/\Lambda)]$ con
$h_0=\exp[-j\tfrac12(n+1)k_od_0]$; (b) mostrar que una onda plana a ángulo $\theta_i$ se transmite
como suma de ondas planas a ángulos (2.4-12). Pista: desarrollar $\mathfrak t(x,y)$ en serie de Fourier.

(2.4-12) solo vale en la aproximación paraxial ($\Lambda\gg\lambda$). El análisis general de redes
delgadas da (p. 56, con nota al pie a Hecht & Zajac, *Optics*, 2.ª ed. 1990):

$$\sin\theta_q=\sin\theta_i+q\frac{\lambda}{\Lambda}. \tag{2.4-13}$$

Como $\theta_q$ depende de $\lambda$ (de $\nu$), la red separa una onda policromática en sus
componentes espectrales (**Fig. 2.4-12**, p. 57: R+G+B → órdenes $\pm1$ dispersados en R, G, B;
orden 0 sin dispersar). Uso: filtros, analizadores de espectro, espectroscopía.

#### 2.4C Componentes ópticos de índice gradual (p. 57)

El efecto de prisma, lente o red es un desfase que curva el frente; se controla con la variación
del espesor (lineal, cuadrática, periódica). El mismo desfase se logra con una placa plana de
espesor fijo e índice variable, porque espesor e índice aparecen como producto en (2.4-3). Para
placa delgada de espesor $d_0$ e índice $n(x,y)$ (recuadro, p. 57):

$$\mathfrak t(x,y)=\exp[-jn(x,y)k_od_0]. \tag{2.4-14}$$

**Ejercicio 2.4-6, Lente de índice gradual** (p. 57, **Fig. 2.4-13**): mostrar que una placa de
espesor uniforme $d_0$ con $n(x,y)=n_0[1-\tfrac12\alpha^2(x^2+y^2)]$, $\alpha d_0\ll1$, actúa como
lente de distancia focal $f=1/n_0d_0\alpha^2$ (cf. Ejercicio 1.3-1).

### 2.5 Interferencia (p. 58)

La función de onda total es la suma de las individuales (linealidad de la ecuación de onda); para
ondas monocromáticas de la misma frecuencia la superposición vale para las amplitudes complejas
(linealidad de Helmholtz). **La superposición no aplica a la intensidad**: la intensidad de la suma
no es la suma de intensidades; la diferencia es la interferencia, que depende de la relación de
fase y no se explica con óptica de rayos. Aquí: ondas de igual frecuencia; distintas frecuencias
en §2.6.

#### 2.5A Interferencia de dos ondas (p. 58)

$$U(\mathbf r)=U_1(\mathbf r)+U_2(\mathbf r). \tag{2.5-1}$$

Con $I_1=|U_1|^2$, $I_2=|U_2|^2$ (dependencia en $\mathbf r$ omitida):

$$I=|U|^2=|U_1+U_2|^2=|U_1|^2+|U_2|^2+U_1^*U_2+U_1U_2^*. \tag{2.5-2}$$

Sustituyendo

$$U_1=\sqrt{I_1}\exp(j\varphi_1)\quad\text{y}\quad U_2=\sqrt{I_2}\exp(j\varphi_2) \tag{2.5-3}$$

se obtiene la **ecuación de interferencia** (recuadro, p. 58):

$$I=I_1+I_2+2\sqrt{I_1I_2}\cos\varphi, \tag{2.5-4}$$

$$\varphi=\varphi_2-\varphi_1. \tag{2.5-5}$$

Interpretación con el diagrama de fasores (**Fig. 2.5-1(a)**, p. 59): $|U|$ depende de los módulos y
de la diferencia de fase $\varphi$. **Fig. 2.5-1(b)**: $I$ vs. $\varphi$ oscila alrededor de
$I_1+I_2$. Si $I_1=I_2=I_0$: $I=2I_0(1+\cos\varphi)=4I_0\cos^2(\varphi/2)$; $\varphi=0\Rightarrow I=4I_0$;
$\varphi=\pi\Rightarrow I=0$ (cancelación completa solo con intensidades iguales);
$\varphi=\pi/2,3\pi/2\Rightarrow I=2I_0$ (el término de interferencia se anula). La fuerte
dependencia de $I$ con $\varphi$ permite **medir fases detectando intensidades** (p. 59).

- La interferencia **redistribuye** espacialmente la intensidad sin violar la conservación de
  potencia: la potencia total (integral de $I$) se conserva. (p. 59)
- Con iluminación ordinaria no se observa: las fases fluctúan al azar, $\varphi$ uniforme en
  $[0,2\pi)$, $\cos\varphi$ promedia a 0. Esa luz es *parcialmente coherente* (cap. 11); aquí se
  trata luz *coherente*. (p. 59)

**Interferómetros** (p. 59). Dos ondas planas de intensidad $I_0$ en $z$, una retrasada una
distancia $d$: $U_1=\sqrt{I_0}\exp(-jkz)$, $U_2=\sqrt{I_0}\exp[-jk(z-d)]$; con
$\varphi=kd=2\pi d/\lambda$ en (2.5-4):

$$I=2I_0\Big[1+\cos\Big(2\pi\frac{d}{\lambda}\Big)\Big]. \tag{2.5-6}$$

**Fig. 2.5-2** (p. 60): $I$ vs. $d$; $d=$ múltiplo entero de $\lambda\Rightarrow I=4I_0$
(constructiva); $d=$ múltiplo impar de $\lambda/2\Rightarrow I=0$ (destructiva); promedio $2I_0$.

Un **interferómetro** divide una onda con un divisor de haz, retrasa las partes distancias
distintas, las redirige con espejos, las recombina y detecta la intensidad. **Fig. 2.5-3** (p. 60):
(a) **Mach–Zehnder** (dos divisores, dos brazos separados); (b) **Michelson** (un divisor, dos
espejos, retorno por el mismo divisor); (c) **Sagnac** (mismo camino en sentidos opuestos).

Sensibilidad (p. 60): $\varphi=2\pi d/\lambda=2\pi nd/\lambda_o=2\pi n\nu d/c_o$, así que el
interferómetro mide cambios pequeños de $d$, de $n$ o de $\lambda_o$ ($\nu$). Ejemplo: si
$d/\lambda_o=10^4$, un cambio de índice $\Delta n=10^{-4}$ produce $\Delta\varphi=2\pi$,
fácilmente observable; lo mismo un cambio de $d$ en $\lambda$ o un cambio de frecuencia
$\Delta\nu=c/d$. Aplicaciones: metrología (deformaciones, perfilometría), medida de índice de
refracción, espectrometría de luz policromática (§11.2B), giróscopo (Sagnac: la rotación da
$\varphi\propto$ velocidad angular), detección de ondas gravitacionales.

**Conservación de energía y fase del divisor de haz** (pp. 60–61): cada interferómetro tiene dos
salidas, $U=U_1+U_2$ y $U'=U_1'+U_2'$; la suma de sus intensidades debe igualar la incidente, luego
si una es alta (constructiva) la otra es baja (destructiva): las diferencias de fase $\varphi$ y
$\varphi'$ difieren en $\pi$. Como los caminos y el número de reflexiones en espejos son iguales,
la diferencia proviene del divisor: en una salida cada componente se transmite una vez y se refleja
una vez; en la otra, una se transmite dos veces y la otra se refleja dos veces. Conclusión: **las
fases de las ondas reflejada y transmitida en un divisor de haz difieren en $\pi/2$** (§7.1,
Ejemplo 7.1-2).

**Interferencia de dos ondas planas oblicuas** (p. 61). $U_1=\sqrt{I_0}\exp(-jkz)$ y
$U_2=\sqrt{I_0}\exp[-j(k\cos\theta\,z+k\sin\theta\,x)]$; en $z=0$, $\varphi=k\sin\theta\,x$ y

$$I=2I_0[1+\cos(k\sin\theta\,x)]. \tag{2.5-7}$$

Patrón sinusoidal en $x$ de período $2\pi/k\sin\theta=\lambda/\sin\theta$ (**Fig. 2.5-4**, p. 61);
$\theta=30°\Rightarrow$ período $2\lambda$. Aplicaciones: grabar redes sinusoidales de alta
resolución; medir el ángulo de llegada mezclando con una onda de referencia (principio de la
**holografía**, §4.5).

**Ejercicio 2.5-1, Interferencia de onda plana y onda esférica** (p. 61, **Fig. 2.5-5**, p. 62):
onda plana $A_1\exp(-jkz)$ y paraboloidal $(A_2/z)\exp(-jkz)\exp[-jk(x^2+y^2)/2z]$ interfieren en
$z=d$; derivar $I(x,y,d)$; con intensidades iguales en ese plano, verificar que los ceros de
intensidad son anillos concéntricos.

**Ejercicio 2.5-2, Interferencia de dos ondas esféricas** (p. 62, **Fig. 2.5-6**): dos ondas
esféricas de igual intensidad $I_0$ desde $(-a,0,0)$ y $(a,0,0)$ interfieren en $z=d$ (sistema de
dos pinholes, análogo al experimento de doble rendija de Young); con la aproximación paraboloidal
mostrar que

$$I(x,y,d)\approx2I_0\Big(1+\cos\frac{2\pi x\theta}{\lambda}\Big), \tag{2.5-8}$$

con $\theta\approx2a/d$ el ángulo subtendido por las fuentes desde el plano de observación; patrón
periódico de período $\lambda/\theta$.

#### 2.5B Interferencia de múltiples ondas (p. 62)

$M$ ondas monocromáticas de la misma frecuencia, $U=U_1+U_2+\cdots+U_M$; conocer $I_1,\dots,I_M$
no basta: hacen falta las fases relativas.

**$M$ ondas de igual amplitud e igual diferencia de fase** (p. 63):

$$U_m=\sqrt{I_0}\exp[j(m-1)\varphi],\qquad m=1,2,\dots,M. \tag{2.5-9}$$

Con $h=\exp(j\varphi)$, $U_m=\sqrt{I_0}h^{m-1}$ y

$$U=\sqrt{I_0}(1+h+h^2+\cdots+h^{M-1})=\sqrt{I_0}\frac{1-h^M}{1-h}=\sqrt{I_0}\frac{1-\exp(jM\varphi)}{1-\exp(j\varphi)}, \tag{2.5-10}$$

$$I=|U|^2=I_0\left|\frac{\exp(-jM\varphi/2)-\exp(jM\varphi/2)}{\exp(-j\varphi/2)-\exp(j\varphi/2)}\right|^2, \tag{2.5-11}$$

de donde (recuadro, p. 63):

$$I=I_0\frac{\sin^2(M\varphi/2)}{\sin^2(\varphi/2)}. \tag{2.5-12}$$

**Fig. 2.5-7** (p. 63): (a) suma de $M$ fasores de igual módulo y fase sucesiva $\varphi$ (arco
poligonal); (b) $I$ vs. $\varphi$ para $M=5$: picos de altura $M\bar I=M^2I_0$ en $\varphi=2\pi q$,
período $2\pi$, ancho $\approx2\pi/M$, ceros en $\varphi=2\pi/M$. Intensidad media sobre $\varphi$
uniforme: $\bar I=(1/2\pi)\int_0^{2\pi}I\,d\varphi=MI_0$ (igual que sin interferencia); el pico es
$M$ veces la media. La sensibilidad a la fase es dramática para $M$ grande (p. 64). Comparar con
Fig. 2.5-2 ($M=2$).

**Ejercicio 2.5-3, Reflexión de Bragg** (p. 64, **Fig. 2.5-8**): luz reflejada a ángulo $\theta$
(respecto a los planos) desde $M$ planos paralelos separados $\Lambda$, cada uno reflejando una
pequeña fracción (amplitudes ≈ iguales). Mostrar que la diferencia de fase es
$\varphi=k(2\Lambda\sin\theta)$ y que el máximo de intensidad reflejada ocurre en (recuadro)

$$\sin\theta=\frac{\lambda}{2\Lambda}. \tag{2.5-13}$$

Define el **ángulo de Bragg**. Aparece en multicapas (§7.1), rayos X en cristales, y reflexión en
redes creadas por ondas acústicas (cap. 19). Tratamiento exacto: §7.1C.

**Infinitas ondas de amplitudes progresivamente menores e igual diferencia de fase** (p. 64):

$$U_1=\sqrt{I_0},\quad U_2=hU_1,\quad U_3=hU_2=h^2U_1,\ \dots, \tag{2.5-14}$$

con $h=|h|e^{j\varphi}$, $|h|<1$. Cada onda es $|h|$ veces menor que la anterior y desfasada
$\varphi$ (**Fig. 2.5-9(a)**, p. 65: espiral de fasores). Suma geométrica:

$$U=U_1+U_2+U_3+\cdots=\sqrt{I_0}(1+h+h^2+\cdots)=\frac{\sqrt{I_0}}{1-h}=\frac{\sqrt{I_0}}{1-|h|e^{j\varphi}}. \tag{2.5-15}$$

$$I=|U|^2=\frac{I_0}{|1-|h|e^{j\varphi}|^2}=\frac{I_0}{(1-|h|\cos\varphi)^2+|h|^2\sin^2\varphi}, \tag{2.5-16}$$

$$I=\frac{I_0}{(1-|h|)^2+4|h|\sin^2(\varphi/2)}. \tag{2.5-17}$$

Forma conveniente (recuadro, p. 65):

$$I=\frac{I_{\max}}{1+(2\mathcal F/\pi)^2\sin^2(\varphi/2)},\qquad I_{\max}=\frac{I_0}{(1-|h|)^2}, \tag{2.5-18}$$

donde (recuadro)

$$\mathcal F=\frac{\pi\sqrt{|h|}}{1-|h|} \tag{2.5-19}$$

es la **finura** (*finesse*). $I$ es periódica en $\varphi$ con período $2\pi$ (**Fig. 2.5-9(b)**,
p. 65, curvas para $\mathcal F=2$ y $10$), máximo $I_{\max}$ en $\varphi=2\pi q$ (fasores alineados).
Para $\mathcal F$ grande ($|h|\to1$) los picos son agudos. Cerca de $\varphi=0$, con
$\sin(\varphi/2)\approx\varphi/2$ (p. 66):

$$I\approx\frac{I_{\max}}{1+(\mathcal F/\pi)^2\varphi^2}. \tag{2.5-20}$$

$I$ cae a la mitad en $\varphi=\pi/\mathcal F$, así que el ancho total a media altura (FWHM) del
pico es (recuadro, p. 66):

$$\Delta\varphi\approx\frac{2\pi}{\mathcal F}. \tag{2.5-21}$$

Para $\mathcal F\gg1$, $\Delta\varphi\ll2\pi$ y vale $\varphi\ll1$. **La finura es la razón entre
el período $2\pi$ y el FWHM**: mide la agudeza del patrón (sensibilidad de $I$ a desviaciones de
$\varphi$ respecto a $2\pi q$).

**Interferómetro Fabry–Perot** (p. 66): dos espejos paralelos con reflexiones múltiples. Por
vuelta completa la amplitud se reduce $|h|=|\mathfrak r|$ (pérdidas en los espejos) y la fase
avanza $\varphi=k2d=4\pi\nu d/c=2\pi\nu/(c/2d)$, $d$ = separación de espejos. $I$ sigue (2.5-18),
máximos cuando $\varphi/2$ es múltiplo entero de $\pi$. Como $\varphi\propto\nu$, la transmisión
tiene picos separados en frecuencia $c/2d$ (rango espectral libre) con ancho $(c/2d)/\mathcal F$,
donde $\mathcal F$ está fijada por las pérdidas vía (2.5-19). Usos: analizador de espectro (§7.1B),
resonador de láseres (§10.1, §15.1A).

### 2.6 Luz policromática y pulsada (p. 66)

La onda monocromática (armónica de $-\infty$ a $\infty$) es una idealización. Aquí se tratan ondas
con dependencia temporal arbitraria, incluidos pulsos de duración finita: luz **policromática**
(más en cap. 22).

#### 2.6A Descripción temporal y espectral (p. 66)

Una onda policromática $u(\mathbf r,t)$ se expande como superposición de armónicos (cada uno una
onda monocromática) y se usa superposición para obtener el efecto de un sistema óptico. En un
punto fijo (p. 67):

$$u(t)=\int_{-\infty}^{\infty}v(\nu)\exp(j2\pi\nu t)\,d\nu, \tag{2.6-1}$$

con $v(\nu)$ la **transformada de Fourier**

$$v(\nu)=\int_{-\infty}^{\infty}u(t)\exp(-j2\pi\nu t)\,dt. \tag{2.6-2}$$

(Repaso en Apéndice A, §A.1.) Como $u(t)$ es real, $v(-\nu)=v^*(\nu)$: las componentes de
frecuencia negativa no son independientes.

**Representación compleja** (p. 67):

$$U(t)=2\int_0^{\infty}v(\nu)\exp(j2\pi\nu t)\,d\nu, \tag{2.6-3}$$

solo frecuencias positivas (multiplicadas por 2); su transformada es $V(\nu)=2v(\nu)$ para
$\nu\ge0$ y $0$ para $\nu<0$. Se recupera $u$ con

$$u(t)=\operatorname{Re}\{U(t)\}=\tfrac12[U(t)+U^*(t)]. \tag{2.6-4}$$

$U(t)$ es la **señal analítica compleja**. Verificación: la integral (2.6-1) de $0$ a $\infty$ vale
$\tfrac12U(t)$ y la de $-\infty$ a $0$,

$$\int_{-\infty}^{0}v(\nu)e^{j2\pi\nu t}d\nu=\int_0^{\infty}v(-\nu)e^{-j2\pi\nu t}d\nu=\int_0^{\infty}v^*(\nu)e^{-j2\pi\nu t}d\nu=\tfrac12U^*(t) \tag{2.6-5}$$

(cambio $\nu\to-\nu$ y simetría $v(-\nu)=v^*(\nu)$). Ejemplo: $u(t)=\cos(\omega t)\to U(t)=\exp(j\omega t)$,
la representación de §2.2A. La representación compleja de una onda policromática es la
superposición de las representaciones complejas de sus componentes de Fourier.

La señal analítica de $u(\mathbf r,t)$ es la **función de onda compleja** $U(\mathbf r,t)$; como cada
componente satisface la ecuación de onda, también ella (recuadro, p. 68):

$$\nabla^2U-\frac1{c^2}\frac{\partial^2U}{\partial t^2}=0. \tag{2.6-6}$$

**Fig. 2.6-1** (p. 68): (a) $|v(\mathbf r,\nu)|$ con picos simétricos en $\pm\nu_0$;
(b) $|V(\mathbf r,\nu)|$ solo en $\nu_0$ (doble altura). Luz **cuasi-monocromática**: componentes
confinadas a una banda $\Delta\nu$ alrededor de $\nu_0$ con $\Delta\nu\ll\nu_0$.

**Intensidad de una onda policromática** (p. 68). De (2.1-3):

$$I(\mathbf r,t)=2\langle u^2(\mathbf r,t)\rangle=2\Big\langle\{\tfrac12[U(\mathbf r,t)+U^*(\mathbf r,t)]\}^2\Big\rangle=\tfrac12\langle U^2(\mathbf r,t)\rangle+\tfrac12\langle U^{*2}(\mathbf r,t)\rangle+\langle U(\mathbf r,t)U^*(\mathbf r,t)\rangle. \tag{2.6-7}$$

Para luz cuasi-monocromática el promedio se toma sobre un tiempo $\gg1/\nu_0$ pero $\ll1/\Delta\nu$.
$U^2$ oscila a $\approx2\nu_0$ y $U^{*2}$ a $\approx-2\nu_0$: se promedian a cero. El tercer
término contiene solo diferencias de frecuencia ($\sim\Delta\nu\ll\nu_0$), varía lentamente y
sobrevive (recuadro, p. 68):

$$I(\mathbf r,t)=|U(\mathbf r,t)|^2. \tag{2.6-8}$$

> *La intensidad óptica de una onda cuasi-monocromática es el módulo al cuadrado de su función de
> onda compleja.* La simplicidad de este resultado justifica el concepto de función de onda
> compleja (p. 69).

**Onda plana pulsada** (p. 69):

$$U(\mathbf r,t)=\mathcal A\Big(t-\frac zc\Big)\exp\Big[j2\pi\nu_0\Big(t-\frac zc\Big)\Big], \tag{2.6-9}$$

$\mathcal A(t)$ = envolvente compleja (función del tiempo), $\nu_0$ = frecuencia central. Caso
monocromático: $\mathcal A$ constante, $U=\mathcal A\exp(-jk_0z)\exp(j\omega_0t)$ con $k_0=\omega_0/c$,
$\omega_0=2\pi\nu_0$. Al ser función de $t-z/c$, (2.6-9) satisface (2.6-6) para cualquier
$\mathcal A(\cdot)$ (con $d^2\mathcal A/dt^2$ existente). Si $\mathcal A$ dura $\tau$, en cada $z$ la
onda dura $\tau$ y en cada $t$ ocupa una longitud $c\tau$: **paquete de ondas** (*wavepacket*) de
extensión fija viajando en $z$ (**Fig. 2.6-2**, p. 69). Ejemplo: $\tau=1$ ps $\to c\tau=0.3$ mm en
el vacío. Transformada de Fourier:

$$V(\mathbf r,\nu)=A(\nu-\nu_0)\exp(-j2\pi\nu z/c), \tag{2.6-10}$$

$A(\nu)$ = transformada de $\mathcal A(t)$ (propiedad de traslación en frecuencia, §A.1). Si
$\mathcal A$ varía lentamente frente al ciclo óptico, $\Delta\nu\ll\nu_0$. **$\Delta\nu$ es
inversamente proporcional a $\tau$**; si $\mathcal A(t)$ es gaussiana, $A(\nu)$ también lo es, y con
anchos rms de potencia el producto es $1/4\pi$ (§A.2). Ejemplo: $\tau=1$ ps $\Rightarrow\Delta\nu=80$
GHz; con $\nu_0=5\times10^{14}$ Hz ($\lambda_o=0.6$ μm), $\Delta\nu/\nu_0=1.6\times10^{-4}$:
cuasi-monocromática. **Fig. 2.6-2**: (a) $|\mathcal A(t)|$ de duración $\tau$; (b) la onda en $z$ a
tiempos $t$ y $t+T$ (se desplaza $cT$, ocupa $c\tau$); (c) $|A(\nu)|$ centrada en 0 con ancho
$\Delta\nu$; (d) $|V(\nu)|$ centrada en $\nu_0$.

La propagación de un pulso en un medio con índice dependiente de la frecuencia ($c=c_o/n(\nu)$)
se trata en §5.5B; otros aspectos de óptica de pulsos, cap. 22. (p. 70)

#### 2.6B Batido de luz (p. 70)

La dependencia temporal de la intensidad de una onda policromática se atribuye a la interferencia
entre sus componentes monocromáticas.

**Dos ondas monocromáticas de distinta frecuencia** (p. 70). Frecuencias $\nu_1,\nu_2$,
intensidades $I_1,I_2$, fases cero:

$$U(t)=\sqrt{I_1}\exp(j2\pi\nu_1t)+\sqrt{I_2}\exp(j2\pi\nu_2t), \tag{2.6-11}$$

y por (2.5-4):

$$I(t)=I_1+I_2+2\sqrt{I_1I_2}\cos[2\pi(\nu_2-\nu_1)t]. \tag{2.6-12}$$

La intensidad oscila a la **frecuencia de batido** $|\nu_2-\nu_1|$: *light beating*, *optical
mixing*, *photomixing*, *optical heterodyning*. Análogo temporal de (2.5-7) (interferencia espacial
de dos ondas en direcciones distintas); en el diagrama de fasores (Fig. 2.5-1) los fasores giran a
$\omega_1$ y $\omega_2$ y $\varphi=2\pi(\nu_2-\nu_1)t$. Ondas de distintas frecuencias y
direcciones: interferencia espaciotemporal. En electrónica, el batido requiere un mezclador no
lineal (cuadrático); en óptica el fotodetector responde a la intensidad (cap. 18) $=|U|^2$, de
modo que **los detectores ópticos son sensibles solo a la frecuencia diferencia**. (2.6-12) permite
medir la frecuencia de una onda (receptores heterodinos, §24.5). Otras formas de mezcla usan
**medios no lineales** para generar sumas y diferencias de frecuencias ópticas (cap. 21).

**Ejercicio 2.6-1, Radar Doppler óptico** (pp. 70–71): por efecto Doppler, una onda de frecuencia
$\nu$ reflejada por un objeto con velocidad $v$ en la línea de visión sufre $\Delta\nu=\pm(2v/c)\nu$
(+ acercándose, − alejándose). Con onda original y reflejada superpuestas, derivar la intensidad
resultante y proponer un método para medir la velocidad; si un espejo de un Michelson
[Fig. 2.5-3(b)] se mueve con velocidad $\pm v$, usar (2.5-6) para mostrar que la frecuencia de
batido es $\pm(2v/c)\nu$.

**$M$ ondas monocromáticas de igual intensidad y frecuencias equiespaciadas** (p. 71). $M=2L+1$
ondas, intensidad $I_0$, fase cero, frecuencias

$$\nu_q=\nu_0+q\nu_F,\qquad q=-L,\dots,0,\dots,L, \tag{2.6-13}$$

centradas en $\nu_0$ y espaciadas $\nu_F\ll\nu_0$:

$$U(t)=\sqrt{I_0}\sum_{q=-L}^{L}\exp[j2\pi(\nu_0+q\nu_F)t]. \tag{2.6-14}$$

Suma de $M$ fasores de igual módulo y fases sucesivas que difieren en $\varphi=2\pi\nu_Ft$:
matemáticamente idéntico a §2.5B. De (2.5-12) con $\varphi=2\pi t/T_F$, $T_F=1/\nu_F$:

$$I(t)=|U(t)|^2=I_0\frac{\sin^2(M\pi t/T_F)}{\sin^2(\pi t/T_F)}. \tag{2.6-15}$$

**Fig. 2.6-3** (p. 71): $I(t)$ es un tren periódico de pulsos de período $T_F=1/\nu_F$, pico
$M^2I_0$ ($M$ veces la media $\bar I=MI_0$), duración de cada pulso $\approx T_F/M$; el espectro
$|V(\nu)|$ son $M$ líneas espaciadas $\nu_F$ alrededor de $\nu_0$ (ejemplo con $M=5$). Si $\nu_F=1$
GHz, $T_F=1$ ns; con $M=1000$ se generan pulsos de 1 ps. Los modos de un láser pueden quedar
**enganchados en fase** (*phase locked*, §15.4D) para producir pulsos ultracortos (p. 72).

### Reading List (p. 72)

Libros de óptica ondulatoria e interferometría: Pierce, *Almost All About Waves* (MIT 1974/Dover
2006); Pain, *The Physics of Vibrations and Waves* (Wiley, 6.ª ed. 2005); Webb, *Elementary Wave
Optics* (1969/Dover 2005); Hariharan, *Optical Interferometry* (Academic, 2.ª ed. 2003);
Mansuripur, *Classical Optics and Its Applications* (CUP 2002); Lipson, Lipson & Tannhauser,
*Optical Physics* (CUP, 3.ª ed. 1998); Akhmanov & Nikitin, *Physical Optics* (OUP 1997); Mickelson,
*Physical Optics* (1992); Vaughan, *The Fabry–Perot Interferometer* (1989); Young, *Fundamentals
of Waves, Optics, and Modern Physics* (1976); Tolansky, *An Introduction to Interferometry* (1973);
Françon et al., *Experiments in Physical Optics* (1970); Françon, *Optical Interferometry* (1966).
Espectroscopía: Hollas, *Modern Spectroscopy* (2004); Kauppinen & Partanen, *Fourier Transforms in
Spectroscopy* (2001); Christy, Ozaki & Gregoriou, *Modern FTIR Spectroscopy* (2001); Pavia, Lampman
& Kriz (2000); Smith, *Fundamentals of FTIR Spectroscopy* (1996). Redes de difracción: Palmer,
*Diffraction Grating Handbook* (4.ª ed. 2000); Loewen & Popov, *Diffraction Gratings and
Applications* (1997). Histórico/popular: Buchwald, *The Rise of the Wave Theory of Light* (1989);
Kock, *Sound Waves and Light Waves* (1965); Huygens, *Treatise on Light* (1690/1945). Artículos:
Bell, «Waiting for Gravity», *IEEE Spectrum* 43(7), 40–46 (2006); Kamerman (ed.), *Selected Papers
on Laser Radar* (SPIE MS 133, 1997); Maystre (ed.), *Selected Papers on Diffraction Gratings* (SPIE
MS 83, 1993); Hariharan (ed.), *Selected Papers on Interferometry* (SPIE MS 28, 1991).

---

## Tablas y datos numéricos útiles

| Magnitud | Valor | Página |
|---|---|---|
| $c_o$ | $3.0\times10^8$ m/s = 30 cm/ns = 0.3 mm/ps = 0.3 μm/fs | 39 |
| Infrarrojo | 0.76–300 μm (NIR 0.76–2, MIR 2–20, FIR 20–300 μm) | 39 |
| Visible | 390–760 nm | 39 |
| Ultravioleta | 10–390 nm (NUV 390–300, MUV 300–200, FUV 200–100, EUV 100–10 nm) | 39 |
| Frecuencias ópticas | 1 THz (FIR) – $3\times10^{16}$ Hz (EUV); equivalentemente $3\times10^{11}$–$3\times10^{16}$ Hz | 39, 42 |
| Colores (nm) | rojo 760–622; naranja 622–597; amarillo 597–577; verde 577–492; azul 492–455; violeta 455–390 | 39 |
| Duración de un ciclo óptico a 600 nm | $2\times10^{-15}$ s = 2 fs | 41 |
| Unidad de intensidad en el libro | W/cm² | 41 |
| Relaciones en medio de índice $n$ | $c=c_o/n$, $\lambda=\lambda_o/n$, $k=nk_o$ (frecuencia invariante) | 45 |
| Ejercicio 2.2-1 | $\lambda=633$ nm, $z=1$ m | 47 |
| Sensibilidad interferométrica | $d/\lambda_o=10^4\Rightarrow\Delta n=10^{-4}$ da $\Delta\varphi=2\pi$; $\Delta\nu=c/d$ da lo mismo | 60 |
| Dos ondas oblicuas | $\theta=30°\Rightarrow$ período de franjas $2\lambda$ | 61 |
| Fabry–Perot | picos separados $c/2d$ en frecuencia, FWHM $(c/2d)/\mathcal F$ | 66 |
| Pulso de 1 ps | ocupa $c\tau=0.3$ mm en el vacío | 69 |
| Pulso gaussiano | producto de anchos rms $\sigma_t\sigma_\nu=1/4\pi$; $\tau=1$ ps $\Rightarrow\Delta\nu=80$ GHz | 69 |
| $\nu_0=5\times10^{14}$ Hz | $\lambda_o=0.6$ μm; $\Delta\nu/\nu_0=1.6\times10^{-4}$ para $\Delta\nu=80$ GHz | 69 |
| Tren de pulsos | $\nu_F=1$ GHz $\Rightarrow T_F=1$ ns; $M=1000\Rightarrow$ pulsos de 1 ps | 71 |
| Divisor de haz | reflejada y transmitida difieren en fase $\pi/2$ | 61 |
| Problema 2.6-2(b) | $\lambda_o=585$ nm, $\sigma_t=6$ fs | 73 |

No aparecen en este capítulo índices de refracción ni parámetros de materiales concretos (el
capítulo es escalar y genérico).

---

## Problemas al final del capítulo (p. 73)

La numeración continúa la de los ejercicios del texto (por eso 2.2-3 sigue a los Ejercicios 2.2-1
y 2.2-2, etc.). En la 2.ª ed. **ningún problema de esta lista lleva asterisco**; el único asterisco
del capítulo marca la §2.3 como sección avanzada (pp. 38, 49). Se señalan con «(§2.3*)» los que
dependen de esa sección.

- **2.2-3 Spherical Waves.** Verificar en coordenadas esféricas que (2.2-15) satisface Helmholtz (2.2-7).
- **2.2-4 Intensity of a Spherical Wave.** Expresar $I$ a distancia $r$ en función de la potencia $P$; calcular $I$ en $r=1$ m para $P=100$ W.
- **2.2-5 Cylindrical Waves.** Derivar amplitud compleja e intensidad de una onda monocromática con frentes cilíndricos centrados en el eje $y$.
- **2.2-6 Paraxial Helmholtz Equation.** Derivar (2.2-23) usando las aproximaciones (2.2-21) y (2.2-22).
- **2.2-7 Conjugate Waves.** Comparar $U(\mathbf r)$ con $U^*(\mathbf r)$ (intensidad, frentes, normales) usando la onda plana $U=A\exp[-jk(x+y)/\sqrt2]$ y la esférica $U=(A/r)\exp(-jkr)$.
- **2.3-1 Wave in a GRIN Slab.** (§2.3*) Bosquejar los frentes de onda en la lámina SELFOC de índice gradual del Ejemplo 1.3-1.
- **2.4-7 Reflection of a Spherical Wave from a Planar Mirror.** Con la onda esférica vista localmente como plana (aproximación de Fresnel válida), usar la ley de reflexión para determinar la onda reflejada.
- **2.4-8 Optical Path Length.** Placa de $N$ capas delgadas ($d_q$, $n_q$); hallar $\mathfrak t$ ignorando reflexiones; hallar la distancia $d$ de vacío que da la misma $\mathfrak t$ y mostrar que es la longitud de camino óptico de §1.1.
- **2.4-9 Diffraction Grating.** Repetir el Ejercicio 2.4-5 con espesor periódico cuadrado de período $\Lambda\gg\lambda$; mostrar que $\theta\approx\lambda/\Lambda$; con incidencia normal, hallar las amplitudes de los órdenes difractados.
- **2.4-10 Reflectance of a Spherical Mirror.** Mostrar que la reflectancia de amplitud compleja de un espejo esférico delgado de radio $R$ es $\mathfrak r(x,y)=h_0\exp[-jk_o(x^2+y^2)/R]$; comparar con la transmitancia de una lente con $f=-R/2$.
- **2.5-4 Standing Waves.** Intensidad de dos ondas planas de longitud de onda $\lambda$ contrapropagantes en $z$; bosquejar $I$ vs. $z$.
- **2.5-5 Fringe Visibility.** Visibilidad $\mathcal V=(I_{\max}-I_{\min})/(I_{\max}+I_{\min})$ del patrón (2.5-4) en función de $I_1/I_2$; hallar la razón que maximiza $\mathcal V$.
- **2.5-6 Michelson Interferometer.** Con un espejo desalineado un ángulo pequeño $\Delta\theta$, describir el patrón en el plano del detector y su evolución al mover el otro espejo.
- **2.6-2 Pulsed Spherical Wave.** (a) Mostrar que una onda esférica pulsada tiene $U(\mathbf r,t)=(1/r)\mathfrak a(t-r/c)$ con $\mathfrak a(t)$ arbitraria. (b) Pulso ultracorto con $\lambda_o=585$ nm y envolvente gaussiana de ancho rms $\sigma_t=6$ fs: ¿cuántos ciclos ópticos contiene? Si se propaga como onda esférica desde el origen en $t=0$, describir la distribución radial de intensidad en $t=1$ ps.

---

## Relación con Óptica No Lineal

**Con el curso (temas del programa):**

- **Ondas EM / tema 1 (ondas monocromáticas):** la representación compleja (2.2-2)–(2.2-6), la
  ecuación de Helmholtz (2.2-7) y la regla $I=|U|^2$ (2.2-10) son la base de todo el formalismo del
  curso. Ojo con la convención: Saleh usa $e^{+j\omega t}$ y ondas $\exp(-jkz)$, mientras Boyd
  (*Nonlinear Optics*) usa $e^{-i\omega t}$ y $\exp(+ikz)$; al mezclar fuentes hay que conjugar.
  La descomposición $u=\tfrac12[Ue^{j\omega t}+\text{c.c.}]$ (2.2-6) es exactamente la que se usa
  para escribir $\tilde E(t)=E e^{-i\omega t}+\text{c.c.}$ y derivar los términos de $\chi^{(2)}$ y
  $\chi^{(3)}$ (SHG, suma/diferencia de frecuencias, rectificación óptica): el producto de dos
  campos de esta forma genera $2\omega$, $0$, $\omega_1\pm\omega_2$. El mismo mecanismo aparece ya
  en (2.6-7): $U^2$ oscila a $2\nu_0$ y $UU^*$ a frecuencia cero.
- **Aproximación de envolvente lentamente variable (SVEA):** (2.2-20)–(2.2-23) es la SVEA
  espacial; es idéntica a la aproximación que lleva a las ecuaciones acopladas de amplitud en
  $\chi^{(2)}$ (SHG, OPA) y a la ecuación no lineal de Schrödinger (NLSE) en fibras, donde además
  se desprecia $\partial^2A/\partial z^2$ frente a $k\,\partial A/\partial z$. El libro señala la
  semejanza con la ecuación de Schrödinger (p. 48).
- **Haz gaussiano:** el Ejercicio 2.2-2 (p. 48) introduce $q(z)=z+jz_0$ y anticipa el cap. 3;
  esencial para calcular intensidades de pico, longitud de Rayleigh y eficiencias de conversión no
  lineal (SHG con haces enfocados, Z-scan, $n_2$). El ancho de la Tarea 1 (cintura $w_0$) sale de ahí.
- **Absorción y dispersión:** el capítulo las excluye explícitamente (pp. 51–52, 70) y remite a
  §5.5 (índice complejo, $n(\nu)$) y §5.5B (pulsos en medios dispersivos). Pero fija el lenguaje:
  $k=nk_o$, velocidad de fase $c=c_o/n$, invariancia de $\nu$ (2.2-14). La medida interferométrica
  de $\Delta n$ (p. 60) es la base de técnicas para medir $n_2$ (índice dependiente de la intensidad)
  y birrefringencia inducida.
- **Pulsos en medios dispersivos, GVD, SPM/solitones/XPM:** §2.6A da el formalismo de la onda plana
  pulsada (2.6-9), su espectro (2.6-10), la relación $\Delta\nu\propto1/\tau$ y el producto
  tiempo–ancho de banda gaussiano $1/4\pi$ (rms). Un pulso de 1 ps tiene 80 GHz de ancho (p. 69):
  base para estimar cuándo importa la GVD y cuánto ensancha el espectro la SPM. La NLSE se escribe
  para la envolvente $\mathcal A(t-z/v_g)$ en este mismo esquema.
- **Polarización y cristales, χ⁽²⁾:** fuera del alcance escalar (p. 40); cap. 5–6 y 21. Sin embargo
  el empate de fases en fronteras (2.4-1)–(2.4-2) es el prototipo de *phase matching*: igualar la
  dependencia espacial de las fases de las ondas que interactúan.
- **FWM, Raman, batido:** (2.6-11)–(2.6-12) muestran que la superposición de dos frecuencias
  produce una modulación de intensidad a $\nu_2-\nu_1$; en un medio con $\chi^{(3)}$ esa modulación
  del índice (SPM/XPM) genera bandas laterales: es el punto de partida de la mezcla de cuatro ondas
  y de la inestabilidad modulacional. El propio libro remite a los medios no lineales para generar
  sumas y diferencias (p. 70, cap. 21). Para Raman estimulado la diferencia $\nu_P-\nu_S$ es la
  frecuencia vibracional: mismo esquema de batido.
- **Interferencia de $M$ modos y mode-locking:** (2.6-13)–(2.6-15) explican cómo $M$ frecuencias
  equiespaciadas con fase fija dan un tren de pulsos de duración $T_F/M$ (p. 71): es el modelo de un
  láser de modos enganchados y de un **peine de frecuencias**; conecta con la generación de
  supercontinuo por pulsos ultracortos.
- **Fabry–Perot, finura, Bragg:** (2.5-18)–(2.5-21) y (2.5-13) son la herramienta para resonadores
  (cavidades de láseres, OPOs, realce de campo intracavidad) y para redes de Bragg (reflectores,
  FBG, phase matching cuasi-periódico).

**Con el proyecto final (anillos add-drop en Si₃N₄, dispersión de guías, supercontinuo, sensado de
índice):**

- **Anillo resonador ≡ Fabry–Perot de ondas viajeras:** la suma de infinitas vueltas con atenuación
  $|h|$ y fase $\varphi=k\cdot L_{\text{vuelta}}=2\pi n_{\text{eff}}L/\lambda_o$ es exactamente
  (2.5-14)–(2.5-18). De ahí salen directamente: **FSR** (análogo de $c/2d$ → $c/n_gL$ en el anillo),
  **FWHM** $=\text{FSR}/\mathcal F$, **finura** (2.5-19) en función de pérdidas y acoplamiento, y
  **Q** $=\nu_0/\Delta\nu$. Estas son las magnitudes que mide la skill
  `lumerical-analisis-resultados`; citar Saleh §2.5B, pp. 64–66.
- **Sensado de índice de refracción (bulk):** el argumento de sensibilidad de la p. 60
  ($\varphi=2\pi n\nu d/c_o$; $d/\lambda_o=10^4$ y $\Delta n=10^{-4}$ dan $\Delta\varphi=2\pi$)
  es el mismo que gobierna el corrimiento de resonancia del anillo con el cladding
  ($n=1.33\to1.37$): $\Delta\lambda/\lambda\approx\Delta n_{\text{eff}}/n_g$. La agudeza del pico
  (finura/Q) fija el límite de detección.
- **Dispersión de guías:** el capítulo fija $k=n k_o$ y la velocidad de fase; la velocidad de
  grupo y la GVD ($n(\nu)$) vienen de §5.5B y del cap. 22, pero la descripción espectral de pulsos
  de §2.6A es la que se usa para interpretar el barrido de $n_{\text{eff}}(\lambda)$ de MODE/FDE.
- **Supercontinuo:** combina SPM/XPM/FWM/Raman (ver arriba) con pulsos descritos por (2.6-9); el
  tren de pulsos (2.6-15) y la relación $\tau$–$\Delta\nu$ son el punto de partida para elegir
  duración y energía del pulso de bombeo.
- **Conservación de energía en acopladores/divisores:** el argumento de la p. 60–61 (salidas
  complementarias, desfase $\pi/2$ en el divisor) es el que justifica la matriz de acoplamiento
  $\begin{pmatrix}t & j\kappa\\ j\kappa & t\end{pmatrix}$ del acoplador direccional del anillo add-drop.
- **Redes y Bragg:** (2.4-12)/(2.4-13) y (2.5-13) sirven para acopladores de red (grating couplers)
  de entrada/salida y para posibles reflectores de Bragg en la plataforma.
