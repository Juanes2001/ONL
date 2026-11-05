# Capítulo 4 — Fourier Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 102–149 (PDF 124–171). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007,
cap. 4 "Fourier Optics". Todas las páginas citadas son páginas del libro (PDF = libro + 22).

Convención de notación del libro (mantenida aquí): dependencia temporal $e^{j\omega t}$ con
$j=\sqrt{-1}$; amplitudes complejas en mayúscula ($U$, $F$, $H$, $h$); la función armónica
**espacial** se define con signo menos en el exponente, $\exp[-j2\pi(\nu_x x+\nu_y y)]$, al
contrario de la temporal $\exp(j2\pi\nu t)$ — estos signos coinciden con los de una onda plana
que viaja hacia $+z$ (nota al pie, p. 103). Frecuencias espaciales $\nu_x,\nu_y$ en
ciclos/mm; frecuencias angulares espaciales $k_x,k_y$ en rad/mm. Unidades SI.

---

## Resumen del capítulo

La óptica de Fourier describe la propagación de la luz mediante análisis armónico
(transformada de Fourier) y teoría de sistemas lineales. El bloque de construcción es la
función armónica espacial $F(\nu_x,\nu_y)\exp[-j2\pi(\nu_x x+\nu_y y)]$, que corresponde
uno a uno con una onda plana de vector de onda $(k_x,k_y,k_z)=(2\pi\nu_x,2\pi\nu_y,k_z)$;
por tanto una onda arbitraria es una superposición de ondas planas y el espacio libre entre
dos planos $z=0$ y $z=d$ es un sistema lineal e invariante al desplazamiento, caracterizado
por su función de transferencia $H(\nu_x,\nu_y)=\exp(-j2\pi d\sqrt{\lambda^{-2}-\nu_x^2-\nu_y^2})$
(pasa-bajas con corte en $\lambda^{-1}$ y ondas evanescentes por encima) o por su respuesta
al impulso (onda paraboloidal, principio de Huygens–Fresnel). En la aproximación de Fresnel
la fase de $H$ es cuadrática; en la de Fraunhofer (campo lejano, $N_F\ll1$) la salida es
directamente la transformada de Fourier de la entrada, y una lente realiza esa misma
transformada en su plano focal sin necesidad de campo lejano (sistema 2-f). Con ello se
tratan la difracción (Fraunhofer: $|{\cal F}\{p\}|^2$; Fresnel: convolución con
$\exp[-j\pi(X^2+Y^2)]$), la formación de imágenes (sistema 4-f y filtrado espacial, lente
única, función pupila generalizada, radio de la mancha $1.22\lambda F_\#$, ancho de banda
espacial $1/2\lambda F_\#$, límite de difracción y SNOM) y la holografía (código holográfico
por interferencia con una onda de referencia, holografía fuera de eje, de Fourier, filtro
de Vander Lugt, hologramas de volumen y condición de Bragg).

---

## Secciones

### Introducción del capítulo (pp. 103–104)

- Análisis armónico temporal: $f(t)$ se expande como superposición de
  $F(\nu)\exp(j2\pi\nu t)$; $F(\nu)$ es la transformada de Fourier de $f(t)$ (Fig. 4.0-1,
  p. 103; Apéndice A §A.1; sistemas lineales en Apéndice B §B.1).
- Análisis armónico espacial 2D: $f(x,y)$ se expande en funciones
  $F(\nu_x,\nu_y)\exp[-j2\pi(\nu_x x+\nu_y y)]$, con $\nu_x,\nu_y$ las **frecuencias
  espaciales** (ciclos/mm) (Fig. 4.0-2, p. 103; Apéndice A §A.3).
- La onda plana $U(x,y,z)=A\exp[-j(k_xx+k_yy+k_zz)]$ evaluada en $z=0$ es la función
  armónica $f(x,y)=A\exp[-j2\pi(\nu_xx+\nu_yy)]$ con $\nu_x=k_x/2\pi$, $\nu_y=k_y/2\pi$
  (p. 103–104). Correspondencia uno a uno porque $k_z$ queda fijo por
  $k_x^2+k_y^2+k_z^2=\omega^2/c^2=(2\pi/\lambda)^2$ (p. 104). Restricción: $\nu_x,\nu_y$ no
  pueden superar $1/\lambda$.
- Principio de la óptica de Fourier: una onda arbitraria en espacio libre es una
  superposición de ondas planas (Fig. 4.0-3, p. 104).
- Enfoque de sistemas lineales (Fig. 4.0-4, p. 104): entrada $f(x,y)=U(x,y,0)$, salida
  $g(x,y)=U(x,y,d)$; el sistema se caracteriza por su **función de respuesta al impulso**
  $h(x,y)$ (respuesta a un punto) o por su **función de transferencia** $H(\nu_x,\nu_y)$
  (respuesta a funciones armónicas) — Apéndice B.

---

### 4.1 Propagation of Light in Free Space (p. 105)

#### 4.1A Spatial Harmonic Functions and Plane Waves (p. 105)

Onda plana $U(x,y,z)=A\exp[-j(k_xx+k_yy+k_zz)]$, $\mathbf k=(k_x,k_y,k_z)$,
$k=\sqrt{k_x^2+k_y^2+k_z^2}=2\pi/\lambda$, envolvente compleja $A$. Ángulos
$\theta_x=\sin^{-1}(k_x/k)$ y $\theta_y=\sin^{-1}(k_y/k)$ con los planos $y$–$z$ y $x$–$z$
(Fig. 4.1-1, p. 105). Ojo: la frecuencia espacial $\nu=k/2\pi$ va en ciclos/mm, mientras
que la frecuencia óptica $\nu=kc/2\pi$ va en Hz (§2.2).

**(4.1-1) Frecuencias espaciales y ángulos** (recuadro, p. 105):
$$\theta_x=\sin^{-1}\lambda\nu_x,\qquad \theta_y=\sin^{-1}\lambda\nu_y.$$
Con periodos $\Lambda_x=1/\nu_x$, $\Lambda_y=1/\nu_y$: $\theta_x=\sin^{-1}(\lambda/\Lambda_x)$
— los ángulos están gobernados por la razón longitud de onda / periodo (p. 105).

**(4.1-2) Aproximación paraxial** (recuadro, p. 105): si $k_x,k_y\ll k$,
$$\theta_x\approx\lambda\nu_x,\qquad\theta_y\approx\lambda\nu_y.$$

Dada $f(x,y)$, la onda se reconstruye como $U(x,y,z)=f(x,y)\exp(-jk_zz)$ con

**(4.1-3)** (p. 106):
$$k_z=\pm\sqrt{k^2-k_x^2-k_y^2},\qquad k=2\pi/\lambda.$$
Validez: $k_x^2+k_y^2<k^2$ ($k_z$ real), es decir $\lambda\nu_x<1$ y $\lambda\nu_y<1$. Signo
$+$: onda hacia adelante; $-$: hacia atrás (solo se consideran las que van hacia adelante).

**Análisis espectral espacial** (p. 106): un elemento delgado con transmitancia
$f(x,y)=\exp[-j2\pi(\nu_xx+\nu_yy)]$ iluminado por onda plana unitaria en $z$ convierte la
onda en una onda plana a ángulos $\theta_x=\sin^{-1}\lambda\nu_x$, $\theta_y=\sin^{-1}\lambda\nu_y$
— actúa como un prisma (Fig. 4.1-2, p. 106, **rejilla de fase**). Con signo $+$ en el
exponente la desviación es a $-\theta_x,-\theta_y$. Interpretación interferencial: dos
puntos separados por un periodo $\Lambda=1/\nu_x$ tienen diferencia de camino
$\Lambda\sin\theta_x=\lambda$ en la dirección $\theta_x$ → interferencia constructiva (p. 106).
Si $f$ es suma de armónicas, la onda transmitida es suma de igual número de ondas planas
dispersadas en direcciones distintas, con amplitudes proporcionales a los coeficientes.

**Ejemplos** (p. 107):
- $f(x,y)=\cos(2\pi\nu_xx)=\tfrac12\{\exp(-j2\pi\nu_xx)+\exp(+j2\pi\nu_xx)\}$ desvía la onda
  a $\pm\sin^{-1}(\lambda\nu_x)$ (arriba y abajo).
- $1+\cos(2\pi\nu_yy)$: rejilla de difracción (Ejercicio 2.4-5); componentes derecha,
  izquierda y una que sigue recta.
- $f(x,y)=\mathcal U[\cos(2\pi\nu_xx)]$ con $\mathcal U$ el escalón unitario: conjunto
  periódico de rendijas en pantalla opaca; serie de Fourier con frecuencias
  $0,\pm\nu_x,\pm2\nu_x,\dots$ → ondas a ángulos $0,\pm\sin^{-1}\lambda\nu_x,\pm\sin^{-1}2\lambda\nu_x,\dots$

Caso general (p. 107):

**(4.1-4)**
$$f(x,y)=\iint_{-\infty}^{\infty}F(\nu_x,\nu_y)\exp[-j2\pi(\nu_xx+\nu_yy)]\,d\nu_x\,d\nu_y,$$

**(4.1-5)**
$$U(x,y,z)=\iint_{-\infty}^{\infty}F(\nu_x,\nu_y)\exp[-j(2\pi\nu_xx+2\pi\nu_yy)]\exp(-jk_zz)\,d\nu_x\,d\nu_y,$$
con $k_z=\sqrt{k^2-k_x^2-k_y^2}=2\pi\sqrt{\lambda^{-2}-\nu_x^2-\nu_y^2}$. $F(\nu_x,\nu_y)$ es
la transformada de Fourier de $f(x,y)$ (Apéndice A §A.3). Válido si $\nu_x^2+\nu_y^2<\lambda^{-2}$
(Fig. 4.1-3, p. 107: un elemento delgado descompone una onda plana en muchas ondas planas).
El "análisis espectral espacial" es análogo a la dispersión angular de frecuencias
temporales por un prisma; el espacio libre es un "prisma espacial" natural (pp. 107–108).

**Modulación de amplitud** (p. 108): si $F_0(\nu_x,\nu_y)$ ocupa anchos $\pm\Delta\nu_x$,
$\pm\Delta\nu_y$, la transparencia desvía en el rango $\pm\sin^{-1}(\lambda\Delta\nu_x)$, etc.
$f(x,y)=f_0(x,y)\exp[-j2\pi(\nu_{x0}x+\nu_{y0}y)]$ con $f_0$ lentamente variable
($\Delta\nu_x\ll\nu_{x0}$): función modulada en amplitud con portadora $\nu_{x0},\nu_{y0}$;
su TF es $F_0(\nu_x-\nu_{x0},\nu_y-\nu_{y0})$ (propiedad de desplazamiento en frecuencia);
desvía a direcciones centradas en $\theta_{x0}=\sin^{-1}\lambda\nu_{x0}$ (Fig. 4.1-4, p. 108).
**Multiplexado por frecuencia espacial**: dos imágenes $f_1,f_2$ en una transparencia
$f=f_1\exp[-j2\pi(\nu_{x1}x+\nu_{y1}y)]+f_2\exp[-j2\pi(\nu_{x2}x+\nu_{y2}y)]$ se separan al
iluminar con onda plana (útil en holografía §4.5).

**Modulación de frecuencia** (pp. 108–109): "collage" de regiones con rejillas de distinta
frecuencia → mapa de interconexiones ópticas (Fig. 4.1-5, p. 109). Transparencia de fase
$f(x,y)=\exp[-j2\pi\phi(x,y)]$ con $\phi$ lentamente variable: Taylor
$\phi\approx\phi(x_0,y_0)+(x-x_0)\nu_x+(y-y_0)\nu_y$ con $\nu_x=\partial\phi/\partial x$,
$\nu_y=\partial\phi/\partial y$ → frecuencia espacial local; desviación dependiente de la
posición $\theta_x=\sin^{-1}(\lambda\,\partial\phi/\partial x)$,
$\theta_y=\sin^{-1}(\lambda\,\partial\phi/\partial y)$ (p. 109).

**Ejemplo 4.1-1 Scanning** (p. 109): $f(x,y)=\exp(j\pi x^2/\lambda f)$ introduce fase
$2\pi\phi$ con $\phi=-x^2/2\lambda f$, de modo que $\theta_x=\sin^{-1}(-x/f)\approx-x/f$
para $|x/f|\ll1$, $\theta_y=0$: desviación proporcional a $x$. Moviendo la transparencia a
velocidad uniforme se barre el haz linealmente (Fig. 4.1-6, p. 109).

**Ejemplo 4.1-2 Imaging** (p. 109): la misma transparencia iluminada por onda plana: todos
los vectores de onda convergen a un punto a distancia $f$ → **lente cilíndrica** de focal $f$
(Fig. 4.1-7). $f(x,y)=\exp[j\pi(x^2+y^2)/\lambda f]$ es una lente esférica de focal $f$
[transmitancia de lente delgada, (2.4-9)].

**Ejercicio 4.1-1 Binary-Plate Cylindrical Lens** (p. 110): mostrar con análisis armónico
local que la transparencia binaria

**(4.1-6)** $f(x,y)=\mathcal U[\cos(\pi x^2/\lambda f)]$

actúa como lente cilíndrica con focales múltiples $\infty,\pm f,\pm f/2,\dots$ (Fig. 4.1-8).

**Placa zonal de Fresnel** (p. 110): generalización 2D,

**(4.1-7)** $f(x,y)=\mathcal U[\cos(\pi(x^2+y^2)/\lambda f)]$.

Anillos de radios crecientes, anchos decrecientes y áreas iguales (Fig. 4.1-9); lente
esférica con focales $\pm f,\pm f/2,\dots$ más componente sin desviar. Interpretación
interferencial (§2.5B): el centro del anillo $m$ está en $\pi\rho_m^2/\lambda f=2\pi m$;
distancia al foco $R_m=\sqrt{f^2+\rho_m^2}=\sqrt{f^2+2m\lambda f}\approx f+m\lambda$ → anillos
consecutivos difieren en una longitud de onda, interferencia constructiva en el foco.

#### 4.1B Transfer Function of Free Space (p. 111)

Sistema: planos $z=0$ (entrada $f(x,y)=U(x,y,0)$) y $z=d$ (salida $g(x,y)=U(x,y,d)$),
Fig. 4.1-10 (p. 111). Es lineal (ecuación de Helmholtz lineal) e invariante al
desplazamiento (invariancia del espacio libre ante traslaciones), luego se caracteriza por
$h(x,y)$ o $H(\nu_x,\nu_y)$ (Apéndice B §B.2).

Entrada armónica $f=A\exp[-j2\pi(\nu_xx+\nu_yy)]$ ↔ onda plana con $k_x=2\pi\nu_x$,
$k_y=2\pi\nu_y$ y

**(4.1-8)** $k_z=\sqrt{k^2-k_x^2-k_y^2}=2\pi\sqrt{\lambda^{-2}-\nu_x^2-\nu_y^2}$.

Salida $g=A\exp[-j(k_xx+k_yy+k_zd)]$, de modo que $H=g/f=\exp(-jk_zd)$:

**(4.1-9) Función de transferencia del espacio libre** (recuadro, p. 111):
$$H(\nu_x,\nu_y)=\exp\!\left(-j2\pi d\sqrt{\lambda^{-2}-\nu_x^2-\nu_y^2}\right).$$

Función compleja circularmente simétrica (Fig. 4.1-11, p. 112). Para $\nu_x^2+\nu_y^2\le\lambda^{-2}$
(dentro del círculo de radio $1/\lambda$): $|H|=1$ y la fase depende de $\nu_x,\nu_y$ —
una armónica solo sufre desplazamiento de fase. Para $\nu_x^2+\nu_y^2>\lambda^{-2}$ el
radicando es negativo, el exponente es real y $\exp[-2\pi d(\nu_x^2+\nu_y^2-\lambda^{-2})^{1/2}]$
es un factor de **atenuación**: **onda evanescente** (p. 112; nota al pie: se usa el signo
$-$ de (4.1-3) porque el $+$ daría crecimiento exponencial, inaceptable en sistema pasivo).

Caída abrupta: con $\nu_\rho=(\nu_x^2+\nu_y^2)^{1/2}\approx\lambda^{-1}$, atenuación
$\approx\exp[-2\pi d(\nu_\rho-\lambda^{-1})^{1/2}(2\lambda^{-1})^{1/2}]$, que vale
$\exp(-2\pi)$ cuando $(\nu_\rho-\lambda^{-1})\approx\lambda/2d^2$, es decir
$(\nu_\rho-1/\lambda)/(1/\lambda)\approx\tfrac12(\lambda/d)^2$. Para $d\gg\lambda$ el corte
es nítido: $\lambda^{-1}$ es la frecuencia espacial de corte (**ancho de banda espacial**).

> Resultado destacado (cursiva, p. 112): *el ancho de banda espacial de la propagación de
> luz en espacio libre es aproximadamente $\lambda^{-1}$ ciclos/mm.* Detalles más finos que
> $\lambda$ no se transmiten a distancias mucho mayores que $\lambda$.

**Aproximación de Fresnel** (pp. 112–113): si $\nu_x^2+\nu_y^2\ll\lambda^{-2}$ (rayos
paraxiales, $\theta_x\approx\lambda\nu_x$). Con $\theta^2=\theta_x^2+\theta_y^2\approx\lambda^2(\nu_x^2+\nu_y^2)$:

**(4.1-10)**
$$2\pi d\sqrt{\lambda^{-2}-\nu_x^2-\nu_y^2}=2\pi\frac d\lambda\sqrt{1-\theta^2}=2\pi\frac d\lambda\left(1-\frac{\theta^2}2+\frac{\theta^4}8-\cdots\right).$$

Despreciando el tercer término y superiores:

**(4.1-11) Función de transferencia del espacio libre (aprox. de Fresnel)** (recuadro, p. 113):
$$H(\nu_x,\nu_y)\approx H_0\exp\!\left[j\pi\lambda d\,(\nu_x^2+\nu_y^2)\right],\qquad H_0=\exp(-jkd).$$
Fase cuadrática en $\nu_x,\nu_y$; magnitud constante (Fig. 4.1-12, p. 113).

Condición de validez: tercer término de (4.1-10) $\ll\pi$ para todo $\theta$:

**(4.1-12)** $\dfrac{\theta^4d}{4\lambda}\ll1.$

Con $a$ la mayor distancia radial en el plano de salida, $\theta_m\approx a/d$ [ver (2.2-18)]:

**(4.1-13) Condición de validez de la aprox. de Fresnel** (recuadro, p. 113):
$N_F\,\theta_m^2/4\ll1$,

**(4.1-14) Número de Fresnel** (recuadro, p. 113): $N_F=\dfrac{a^2}{\lambda d}$.

Ejemplo numérico (p. 113): $a=1$ cm, $d=100$ cm, $\lambda=0.5\,\mu$m → $\theta_m=10^{-2}$ rad,
$N_F=200$, $N_F\theta_m^2/4=5\times10^{-3}$: Fresnel aplicable.

**Relación entrada–salida** (p. 114): (1) TF de la entrada

**(4.1-15)**
$$F(\nu_x,\nu_y)=\iint_{-\infty}^{\infty}f(x,y)\exp[j2\pi(\nu_xx+\nu_yy)]\,dx\,dy$$
(envolventes complejas de las ondas planas en la entrada); (2) $H\cdot F$ son las
envolventes en la salida; (3) suma de contribuciones:

**(4.1-16)**
$$g(x,y)=\iint_{-\infty}^{\infty}H(\nu_x,\nu_y)F(\nu_x,\nu_y)\exp[-j2\pi(\nu_xx+\nu_yy)]\,d\nu_x\,d\nu_y.$$

Con Fresnel:

**(4.1-17)** (recuadro, p. 114)
$$g(x,y)=H_0\iint_{-\infty}^{\infty}F(\nu_x,\nu_y)\exp\!\left[j\pi\lambda d(\nu_x^2+\nu_y^2)\right]\exp[-j2\pi(\nu_xx+\nu_yy)]\,d\nu_x\,d\nu_y.$$

#### 4.1C Impulse Response Function of Free Space (p. 114)

$h(x,y)$ = respuesta a un punto en el origen = TF inversa de $H$. Usando Tabla A.2-1 del
Apéndice A y $k=2\pi/\lambda$, la inversa de (4.1-11) es

**(4.1-18) Respuesta al impulso del espacio libre (aprox. Fresnel)** (recuadro, p. 114):
$$h(x,y)\approx h_0\exp\!\left[-jk\frac{x^2+y^2}{2d}\right],\qquad h_0=\frac{j}{\lambda d}\exp(-jkd).$$
Proporcional a la amplitud compleja en $z=d$ de una **onda paraboloidal** centrada en el
origen [ver (2.2-17)]: cada punto de entrada genera una onda paraboloidal; todas se
superponen en la salida.

**Propagación en espacio libre como convolución** (pp. 114–115): $f$ como superposición de
deltas; la onda que nace en $(x',y')$ tiene amplitud $f(x',y')h(x-x',y-y')$ en $(x,y)$:

**(4.1-19)**
$$g(x,y)=\iint_{-\infty}^{\infty}f(x',y')\,h(x-x',y-y')\,dx'\,dy',$$

**(4.1-20)** (recuadro, p. 115)
$$g(x,y)=h_0\iint_{-\infty}^{\infty}f(x',y')\exp\!\left[-j\pi\frac{(x-x')^2+(y-y')^2}{\lambda d}\right]dx'\,dy',\qquad h_0=\frac j{\lambda d}e^{-jkd}.$$

Resumen (p. 115): dos vías dentro de Fresnel — (1) (4.1-20) dominio espacial (expansión en
ondas paraboloidales); (2) (4.1-17) dominio de frecuencia (expansión en ondas planas).

**Ejercicio 4.1-2 Gaussian Beams Revisited** (p. 115): si $f(x,y)=A\exp[-(x^2+y^2)/W_0^2]$
en $z=0$, mostrar que $U(x,y,z)$ es el haz gaussiano del cap. 3, (3.1-7), por ambos métodos
(espacial y de frecuencia).

#### 4.1D Huygens–Fresnel Principle (p. 115)

Cada punto de un frente de onda genera una onda esférica (Fig. 4.1-13, p. 115); la
envolvente de las secundarias es el nuevo frente y su superposición es la onda en otro plano.
Respuesta al impulso entre $z=0$ y $z=d$:

**(4.1-21)** $h(x,y)\propto\dfrac1r\exp(-jkr),\qquad r=\sqrt{x^2+y^2+d^2}.$

En la aproximación paraxial la esférica (4.1-21) se aproxima por la paraboloidal (4.1-18)
(§2.2B): la derivación de $h$ es consistente con Huygens–Fresnel.

---

### 4.2 Optical Fourier Transform (p. 116)

Idea: la onda plana a $\theta_x=\sin^{-1}\lambda\nu_x$, $\theta_y=\sin^{-1}\lambda\nu_y$ tiene
amplitud $F(\nu_x,\nu_y)$ → la luz puede calcular la TF 2D de $f(x,y)$ con una transparencia
de transmitancia $f$ iluminada por onda plana unitaria. Problema: las ondas planas se
solapan; hay que separarlas, sea por propagación a distancia larga, sea con una lente.

#### 4.2A Fourier Transform in the Far Field (p. 116)

Si $d$ es suficientemente grande, la única onda plana que contribuye en $(x,y)$ es la de
dirección $\theta_x\approx x/d$, $\theta_y\approx y/d$, es decir $k_x\approx(x/d)k$,
$\nu_x=x/\lambda d$, $\nu_y=y/\lambda d$ (Fig. 4.2-1, p. 116):

**(4.2-1) Propagación en espacio libre como TF (aprox. de Fraunhofer)** (recuadro, p. 116):
$$g(x,y)\approx h_0\,F\!\left(\frac x{\lambda d},\frac y{\lambda d}\right),\qquad h_0=\frac j{\lambda d}e^{-jkd}.$$
Las demás ondas se cancelan por interferencia destructiva. **Aproximación de Fraunhofer**.

**(4.2-2) Condición de validez de Fraunhofer** (recuadro, p. 117):
$$N_F\ll1\quad\text{y}\quad N_F'\ll1,\qquad N_F=a^2/\lambda d,\quad N_F'=b^2/\lambda d,$$
con $b$ el radio del área de entrada y $a$ el radio del área de salida. Fraunhofer es más
restrictiva que Fresnel ($N_F\theta_m^2/4\ll1$): como $\theta_m\ll1$, Fresnel se cumple
con $N_F$ no necesariamente $\ll1$ (p. 117).

**Demostraciones** (p. 117, sección □): partiendo de (4.1-20), la fase es
$(\pi/\lambda d)[(x^2+y^2)+(x'^2+y'^2)-2(xx'+yy')]$. Si $N_F'=b^2/\lambda d$ es pequeño, el
término $(\pi/\lambda d)(x'^2+y'^2)\le\pi b^2/\lambda d$ es despreciable:

**(4.2-3)**
$$g(x,y)=h_0\exp\!\left(-j\pi\frac{x^2+y^2}{\lambda d}\right)\iint_{-\infty}^{\infty}f(x',y')\exp\!\left(j2\pi\frac{xx'+yy'}{\lambda d}\right)dx'\,dy',$$

**(4.2-4)**
$$g(x,y)=h_0\exp\!\left(-j\pi\frac{x^2+y^2}{\lambda d}\right)F\!\left(\frac x{\lambda d},\frac y{\lambda d}\right).$$
El factor de fase restante se desprecia si $\pi a^2/\lambda d\ll\pi$, es decir $N_F\ll1$,
y se obtiene (4.2-1). Segunda demostración: con (4.1-17) y el **método de fase estacionaria**
(Born & Wolf, Apéndice III), solo contribuye el $\nu_x$ donde
$d(\pi\lambda d\nu_x^2-2\pi\nu_xx)/d\nu_x=0$, o sea $\nu_x=x/\lambda d$.

**Ejercicio 4.2-1** (p. 117): comparar Fresnel vs Fraunhofer con $\lambda=0.5\,\mu$m,
objeto en círculo de radio $b=1$ cm, observación en radio $a=2$ cm; determinar los rangos de
$d$ donde cada aproximación aplica.

> **Summary** (recuadro gris, p. 118): en Fraunhofer, $g(x,y)$ en $z=d$ es proporcional a la
> TF $F(\nu_x,\nu_y)$ de $f(x,y)$ en $z=0$ evaluada en $\nu_x=x/\lambda d$, $\nu_y=y/\lambda d$;
> válido si $f$ está confinada a un círculo de radio $b$ con $b^2/\lambda d\ll1$ y en la
> salida dentro de radio $a$ con $a^2/\lambda d\ll1$.

#### 4.2B Fourier Transform Using a Lens (p. 118)

Una lente esférica delgada transforma una onda plana en una paraboloidal enfocada en un
punto del plano focal (§2.4, Ejercicio 2.4-3); si llega a ángulos pequeños $(\theta_x,\theta_y)$,
el foco está en $(\theta_xf,\theta_yf)$ (Fig. 4.2-2, p. 118). La lente mapea direcciones a
puntos y separa las ondas planas. Con $\theta_x=\lambda\nu_x$: $x=\theta_xf=\lambda f\nu_x$
(Fig. 4.2-3, p. 119: transparencia en $z=0$, lente a distancia $d$, plano focal a $f$):

**(4.2-5)** $g(x,y)\propto F\!\left(\dfrac x{\lambda f},\dfrac y{\lambda f}\right).$

Con Fresnel y ondas paraxiales (recuadro, p. 118):

**(4.2-6)**
$$g(x,y)=h_l\exp\!\left[j\pi\frac{(x^2+y^2)(d-f)}{\lambda f^2}\right]F\!\left(\frac x{\lambda f},\frac y{\lambda f}\right),\qquad h_l=H_0h_0=\frac j{\lambda f}\exp[-jk(d+f)].$$
Como $|h_l|=1/\lambda f$, la intensidad en el plano focal posterior es

**(4.2-7)** $I(x,y)=\dfrac1{(\lambda f)^2}\left|F\!\left(\dfrac x{\lambda f},\dfrac y{\lambda f}\right)\right|^2,$

**independiente de la distancia $d$** (p. 119). Si $d=f$ el factor de fase desaparece:

**(4.2-8) Propiedad de transformada de Fourier de una lente** (recuadro, p. 119):
$$g(x,y)=h_l\,F\!\left(\frac x{\lambda f},\frac y{\lambda f}\right),\qquad h_l=\frac j{\lambda f}\exp(-j2kf).$$
Geometría **2-f** (Fig. 4.2-4, p. 119): planos focales anterior y posterior relacionados por
TF en magnitud y fase.

> **Summary** (recuadro gris, p. 120): la amplitud compleja en el plano focal posterior de una
> lente de focal $f$ es proporcional a la TF de la amplitud en el plano focal anterior,
> evaluada en $\nu_x=x/\lambda f$, $\nu_y=y/\lambda f$. Válido en Fresnel. Sin lente, la TF
> solo se obtiene en Fraunhofer, más restrictiva.

**\*Demostración en cuatro pasos** (p. 120):
1. Onda plana a $\theta_x=\lambda\nu_x$: $U(x,y,0)=F\exp[-j2\pi(\nu_xx+\nu_yy)]$;
   $U(x,y,d)=H(\nu_x,\nu_y)F\exp[\dots]$ con $H=H_0\exp[j\pi\lambda d(\nu_x^2+\nu_y^2)]$,
   $H_0=\exp(-jkd)$.
2. Cruce de la lente: multiplicar por $\exp[j\pi(x^2+y^2)/\lambda f]$ (se ignora
   $\exp(-jk\Delta)$, $\Delta$ espesor de la lente):
   **(4.2-9)** $U(x,y,d+\Delta)=H_0\exp(j\pi\tfrac{x^2+y^2}{\lambda f})\exp[j\pi\lambda d(\nu_x^2+\nu_y^2)]F\exp[-j2\pi(\nu_xx+\nu_yy)]$.
   Completando cuadrados con $x_0=\lambda\nu_xf$, $y_0=\lambda\nu_yf$:
   **(4.2-10)** $U(x,y,d+\Delta)=A(\nu_x,\nu_y)\exp[j\pi\tfrac{(x-x_0)^2+(y-y_0)^2}{\lambda f}]$,
   **(4.2-11)** $A(\nu_x,\nu_y)=H_0\exp[j\pi\lambda(d-f)(\nu_x^2+\nu_y^2)]F(\nu_x,\nu_y)$:
   onda paraboloidal convergente hacia $(x_0,y_0)$ en $z=d+\Delta+f$.
3. Propagación $f$ con (4.1-20) y $\int\exp[j2\pi(x-x_0)x'/\lambda f]dx'=\lambda f\delta(x-x_0)$:
   **(4.2-12)** $U(x,y,d+\Delta+f)=h_0(\lambda f)^2A(\nu_x,\nu_y)\delta(x-x_0)\delta(y-y_0)$,
   $h_0=(j/\lambda f)e^{-jkf}$.
4. Integrar sobre todas las ondas planas usando $\delta(x-\lambda f\nu_x)=(1/\lambda f)\delta(\nu_x-x/\lambda f)$:
   $g(x,y)=h_0A(x/\lambda f,y/\lambda f)$ → (4.2-6).

**Ejercicio 4.2-2 The Inverse Fourier Transform** (p. 120): en el sistema de Fig. 4.2-4 el
campo en el plano focal anterior ($z=2f$) es versión escalada de la TF del campo en $z=0$;
verificar que invirtiendo coordenadas $(x,y)\to(-x,-y)$ se obtiene la TF inversa.

---

### 4.3 Diffraction of Light (p. 121)

Patrón de difracción = distribución de intensidad tras una abertura en pantalla opaca y
propagación en espacio libre; con óptica de rayos sería la sombra; con ondas se desvía poco o
mucho según $d$, $\lambda$ y dimensiones de la abertura (Fig. 4.3-1, p. 121: dientes de una
sierra, Cagnet–Françon–Thrierr). Teoría más simple: la onda pasa sin cambio dentro de la
abertura y se anula fuera (Fig. 4.3-2, p. 121):

**(4.3-1)** $f(x,y)=U(x,y)\,p(x,y)$, con la **función de abertura**

**(4.3-2)** $p(x,y)=\begin{cases}1&\text{dentro de la abertura}\\0&\text{fuera}\end{cases}$

$I(x,y)=|g(x,y)|^2$ se llama **difracción de Fraunhofer** o **de Fresnel** según la
aproximación usada (pp. 121–122). Advertencia (p. 122): la hipótesis no es exacta ni
autoconsistente (la onda transmitida llega también detrás de la pantalla); la teoría
rigurosa (Helmholtz con condiciones de frontera) solo tiene soluciones exactas para pocas
geometrías y queda fuera del libro.

#### 4.3A Fraunhofer Diffraction (p. 122)

Válida si $N_F'=b^2/\lambda d\ll1$, $b$ = mayor distancia radial dentro de la abertura.
Onda plana incidente de intensidad $I_i$: $U=\sqrt{I_i}$, $f=\sqrt{I_i}\,p$, y por (4.2-1):

**(4.3-3)** $g(x,y)\approx\sqrt{I_i}\,h_0\,P\!\left(\dfrac x{\lambda d},\dfrac y{\lambda d}\right),$

**(4.3-4)** $P(\nu_x,\nu_y)=\iint_{-\infty}^{\infty}p(x,y)\exp[j2\pi(\nu_xx+\nu_yy)]\,dx\,dy,$

**(4.3-5)** (recuadro, p. 122)
$$I(x,y)=\frac{I_i}{(\lambda d)^2}\left|P\!\left(\frac x{\lambda d},\frac y{\lambda d}\right)\right|^2.$$
El patrón de Fraunhofer es proporcional al módulo cuadrado de la TF de la función de
abertura evaluada en $\nu_x=x/\lambda d$, $\nu_y=y/\lambda d$.

**Ejercicio 4.3-1 Abertura rectangular** (pp. 122–123), alto $D_x$, ancho $D_y$:

**(4.3-6)** $I(x,y)=I_o\,\mathrm{sinc}^2\dfrac{D_xx}{\lambda d}\,\mathrm{sinc}^2\dfrac{D_yy}{\lambda d}$,
con $I_o=(D_xD_y/\lambda d)^2I_i$ y $\mathrm{sinc}(x)=\sin(\pi x)/(\pi x)$. Primeros ceros en
$x=\pm\lambda d/D_x$, $y=\pm\lambda d/D_y$; divergencia angular

**(4.3-7)** (recuadro, p. 123) $\theta_x=\dfrac\lambda{D_x},\qquad\theta_y=\dfrac\lambda{D_y}.$
Si $D_y<D_x$ el patrón es más ancho en $y$ (Fig. 4.3-3, p. 123).

**Ejercicio 4.3-2 Abertura circular** de diámetro $D$ (p. 123, Fig. 4.3-4):

**(4.3-8)** $I(x,y)=I_o\left[\dfrac{2J_1(\pi D\rho/\lambda d)}{\pi D\rho/\lambda d}\right]^2,\quad\rho=\sqrt{x^2+y^2}$,
$I_o=(\pi D^2/4\lambda d)^2I_i$, $J_1$ Bessel de orden 1 (TF de funciones circularmente
simétricas: Apéndice A §A.3). **Patrón de Airy**: disco central + anillos. Radio del
**disco de Airy** $\rho_s=1.22\lambda d/D$ y semiángulo

**(4.3-9) Semiángulo del disco de Airy** (recuadro, p. 123): $\theta=1.22\dfrac\lambda D.$

Fraunhofer exige $d$ muy grande (lidar, comunicación satelital) pero con una lente de focal
$f$ el patrón en el plano focal es idéntico a (4.3-5) con $d\to f$ (p. 124).

**Ejercicio 4.3-3 Spot Size of a Focused Optical Beam** (p. 124, Fig. 4.3-5): lente de
focal $f$ con abertura circular $D$ iluminada por onda plana:

**(4.3-10)** $I(x,y)=I_o\left[\dfrac{2J_1(\pi D\rho/\lambda f)}{\pi D\rho/\lambda f}\right]^2$,

**(4.3-11)** $\rho_s=1.22\lambda\dfrac fD$;
comparar con el spot de un haz gaussiano de cintura $W_0$ enfocado por lente ideal de
abertura infinita [(3.2-15)].

#### \*4.3B Fresnel Diffraction (p. 124)

Onda plana $\times p(x,y)$, propagación con (4.1-20):

**(4.3-12)**
$$I(x,y)=\frac{I_i}{(\lambda d)^2}\left|\iint_{-\infty}^{\infty}p(x',y')\exp\!\left[-j\pi\frac{(x-x')^2+(y-y')^2}{\lambda d}\right]dx'\,dy'\right|^2.$$

Normalizando distancias con $\sqrt{\lambda d}$: $X=x/\sqrt{\lambda d}$, $X'=x'/\sqrt{\lambda d}$ (p. 125):

**(4.3-13)**
$$I(X,Y)=I_i\left|\iint_{-\infty}^{\infty}p(X',Y')\exp\{-j\pi[(X-X')^2+(Y-Y')^2]\}\,dX'\,dY'\right|^2,$$
convolución de $p(X,Y)$ con $\exp[-j\pi(X^2+Y^2)]$. Partes real e imaginaria $\cos\pi X^2$ y
$\sin\pi X^2$ (Fig. 4.3-6, p. 125): oscilan con frecuencia creciente; primeros lóbulos en
$|X|<1/\sqrt2$ y $|X|<1$; área total de $\exp(-j\pi X^2)$ es 1 (dominada por los primeros
lóbulos). Radio normalizado de la abertura $a/\sqrt{\lambda d}$ → el resultado lo gobierna
$N_F=a^2/\lambda d$. Si $N_F$ es grande, la convolución ≈ $p$ (sombra, óptica de rayos:
$\lambda\to0$ ⇔ $N_F\to\infty$); si $N_F$ pequeño, Fraunhofer.

**Ejemplo 4.3-1 Fresnel Diffraction from a Slit** (pp. 125–126), rendija de ancho $D=2a$:

**(4.3-14)** $P(X,Y)=\begin{cases}1,&|X|\le a/\sqrt{\lambda d}=\sqrt{N_F}\\0,&\text{otro}\end{cases}$,
$I(X,Y)=I_i|g(X)|^2$ con

**(4.3-15)** $g(X)=\int_{-\sqrt{N_F}}^{\sqrt{N_F}}\exp[-j\pi(X-X')^2]\,dX'=\int_{X-\sqrt{N_F}}^{X+\sqrt{N_F}}\exp(-j\pi X'^2)\,dX'$,
escrito usualmente con las **integrales de Fresnel**

**(4.3-16)** $C(x)=\int_0^x\cos\dfrac{\pi\alpha^2}2\,d\alpha,\qquad S(x)=\int_0^x\sin\dfrac{\pi\alpha^2}2\,d\alpha.$
Alternativa por TF: $G(\nu_x)\propto\mathrm{sinc}(\sqrt{N_F}\nu_x)\exp(j\pi\nu_x^2)$ (Tabla A.2-1);
si $N_F\gg1$, $G\approx\mathrm{sinc}(\sqrt{N_F}\nu_x)$ y $g(X)$ es el rectángulo (sombra).
Fig. 4.3-7 (p. 126): patrones para $N_F=10,1,0.5,0.1$; a $N_F$ grande sombra perfecta, luego
oscilaciones en los bordes, y para $N_F$ muy pequeño el sinc de Fraunhofer con primer cero a
$\lambda/D=\lambda/2a$. Las líneas $|x|=(\lambda/D)d$ coinciden con la sombra geométrica
cuando $N_F=0.5$.

**Ejemplo 4.3-2 Fresnel Diffraction from a Gaussian Aperture** (pp. 126–127):
$p(x,y)=\exp[-(x^2+y^2)/W_0^2]$; convolución exacta con $h_0\exp[-j\pi(x^2+y^2)/\lambda d]$:

**(4.3-17)** $I(x,y)=I_i\left[\dfrac{W_0}{W(d)}\right]^2\exp\!\left[-2\dfrac{x^2+y^2}{W^2(d)}\right]$,
$W^2(d)=W_0^2+\theta_0^2d^2$, $\theta_0=\lambda/\pi W_0$. Gaussiana de semiancho $1/e^2$
$W(d)$; $W(d)\approx W_0$ para $d$ pequeño y $W(d)\approx\theta_0d$ en Fraunhofer. Es el haz
gaussiano del cap. 3. Fig. 4.3-8 (p. 127): parámetro $(\pi/2)W_0^2/\lambda d$ (análogo a
$N_F$) $=10,1,0.5,0.1$ ↔ $W(d)/W_0=1.001,1.118,1.414,5.099$; el patrón es gaussiano a toda
distancia.

> **Summary** (recuadro gris, p. 127): al alejarse de la abertura el patrón es (1) una
> sombra de la abertura; (2) un patrón de Fresnel = convolución de la abertura normalizada
> con $\exp[-j\pi(X^2+Y^2)]$; (3) un patrón de Fraunhofer = módulo cuadrado de la TF de la
> abertura, con divergencia angular $\propto\lambda/D$.

---

### 4.4 Image Formation (p. 127)

Sistema ideal de imagen: replica la distribución de luz del plano objeto en el plano
imagen; nunca es perfecto: aumento + desenfoque (blur) por enfoque imperfecto y difracción.
Se usa $h$ y $H$ (Apéndice B); primero óptica de rayos, luego ondas.

#### 4.4A Ray-Optics of a Single-Lens Imaging System (p. 128)

Lente de focal $f$ a distancias $d_1$ (objeto) y $d_2$ (imagen). Enfocado si
$1/d_1+1/d_2=1/f$ (Fig. 4.4-1): respuesta al impulso = impulso. Desenfocado (Fig. 4.4-2):

**(4.4-1) Error de enfoque** (recuadro, p. 128): $\epsilon=\dfrac1{d_1}+\dfrac1{d_2}-\dfrac1f.$

Un punto objeto genera una mancha = sombra de la abertura de la lente. Con la imagen
enfocada en $d_{2o}$ ($1/d_{2o}+1/d_1=1/f$), un punto del borde de la abertura a radio $\rho$
cae en $\rho_s$ con $\rho_s/\rho=(d_{2o}-d_2)/d_{2o}=1-d_2(1/f-1/d_1)=\epsilon d_2$. Con
$p(x,y)$ la **función pupila** (1 dentro de la abertura):

**(4.4-2) Respuesta al impulso (óptica de rayos)** (recuadro, p. 129):
$h(x,y)\propto p\!\left(\dfrac x{\epsilon d_2},\dfrac y{\epsilon d_2}\right).$

**(4.4-3) Radio de la mancha de desenfoque** (recuadro, p. 129): $\rho_s=\tfrac12\epsilon d_2D$
para abertura circular de diámetro $D$. $\rho_s$ es medida inversa del poder de resolución;
abertura pequeña → menor sensibilidad al error de enfoque → mayor "profundidad de foco".

#### 4.4B Wave-Optics of a 4-f Imaging System (p. 129)

Sistema **4-f** (Fig. 4.4-3): dos lentes de focal $f$ separadas $2f$, objeto a $f$ de la
primera, imagen a $f$ de la segunda; aumento unidad (con coordenadas invertidas en la
imagen). Cascada de dos subsistemas de TF: el primero hace la TF (plano de Fourier), el
segundo la TF inversa (coordenadas invertidas, Ejercicio 4.2-2) → sin abertura, réplica
perfecta (Fig. 4.4-4, p. 130).

**Filtrado espacial** (p. 130, Fig. 4.4-5): una máscara en el plano de Fourier ajusta
selectivamente las componentes. La componente de frecuencia $(\nu_x,\nu_y)$ está en
$x=\lambda f\nu_x$, $y=\lambda f\nu_y$; para implementar $H$ la máscara debe ser
$p(x,y)\propto H(x/\lambda f,y/\lambda f)$:

**(4.4-4) Función de transferencia del sistema 4-f** (recuadro, p. 130):
$$H(\nu_x,\nu_y)=p(\lambda f\nu_x,\lambda f\nu_y),$$
(ignorando el factor $j\exp(-j2kf)$ de cada TF). $G=HF$. *La función de transferencia tiene la
misma forma que la función pupila.*

**(4.4-5) Respuesta al impulso del sistema 4-f** (recuadro, p. 130):
$$h(x,y)=\frac1{(\lambda f)^2}P\!\left(\frac x{\lambda f},\frac y{\lambda f}\right),$$
$P$ = TF de $p$.

**Ejemplos de filtros espaciales** (p. 131, Fig. 4.4-6 p. 132):
- **Pasa-bajas** ideal circular: $H=1$ si $\nu_x^2+\nu_y^2<\nu_s^2$, 0 si no; máscara =
  abertura circular de diámetro $D$ con $D/2=\nu_s\lambda f$. Ejemplo: $D=2$ cm, $\lambda=1\,\mu$m,
  $f=100$ cm → $\nu_s=D/2\lambda f=10$ líneas/mm; detalle mínimo discernible ≈ 0.1 mm.
- **Pasa-altas**: transparencia clara con círculo central opaco; resalta bordes.
- **Pasa-vertical**: rendija vertical de ancho $D$ bloquea frecuencias horizontales; máxima
  transmitida $\nu_y=(D/2)/\lambda f$.

#### 4.4C Wave Optics of a Single-Lens Imaging System (p. 132)

Fig. 4.4-7 (p. 132). Determinadas por el error $\epsilon$ y la pupila $p(x,y)$ (que juega el
papel de la máscara del 4-f).

**Respuesta al impulso** (p. 133): impulso en $(0,0)$ del plano objeto → en el plano de la
abertura, onda esférica [por (4.1-18)]

**(4.4-6)** $U(x,y)\approx h_1\exp\!\left[-jk\dfrac{x^2+y^2}{2d_1}\right]$, $h_1=(j/\lambda d_1)e^{-jkd_1}$.

**(4.4-7)** $U_1(x,y)=U(x,y)\exp\!\left(jk\dfrac{x^2+y^2}{2f}\right)p(x,y)$.

**(4.4-8)** $h(x,y)=h_2\iint U_1(x',y')\exp\!\left[-j\pi\dfrac{(x-x')^2+(y-y')^2}{\lambda d_2}\right]dx'dy'$,
$h_2=(j/\lambda d_2)e^{-jkd_2}$. Reescrito como TF:

**(4.4-9)** $h(x,y)=h_1h_2\exp\!\left(-j\pi\dfrac{x^2+y^2}{\lambda d_2}\right)P_1\!\left(\dfrac x{\lambda d_2},\dfrac y{\lambda d_2}\right)$,
donde $P_1$ es la TF de la

**(4.4-10) Función pupila generalizada** (recuadro, p. 133):
$$p_1(x,y)=p(x,y)\exp\!\left(-j\pi\epsilon\frac{x^2+y^2}\lambda\right).$$
Para un sistema de alta calidad $h$ es estrecha y si $\pi(x^2+y^2)/\lambda d_2\ll1$ en ese
rango:

**(4.4-11) Respuesta al impulso** (recuadro, p. 133):
$$h(x,y)=h_0P_1\!\left(\frac x{\lambda d_2},\frac y{\lambda d_2}\right),\qquad h_0=h_1h_2,\ |h_0|=\frac1{\lambda d_1}\frac1{\lambda d_2}.$$
Si está enfocado ($\epsilon=0$), $p_1=p$ y

**(4.4-12)** $h(x,y)\approx h_0P\!\left(\dfrac x{\lambda d_2},\dfrac y{\lambda d_2}\right)$ (p. 134), análogo a (4.4-5).

**Ejemplo 4.4-1 Impulse Response Function of a Focused Imaging System with a Circular
Aperture** (p. 134): $p=1$ si $\rho\le D/2$:

**(4.4-13)** $h(x,y)=h(0,0)\dfrac{2J_1(\pi D\rho/\lambda d_2)}{\pi D\rho/\lambda d_2}$, $\rho=\sqrt{x^2+y^2}$,
$|h(0,0)|=\pi D^2/4\lambda^2d_1d_2$. Cae a cero en

**(4.4-14)** $\rho_s=1.22\lambda\dfrac{d_2}D$ (Fig. 4.4-8). Si enfocado a $\infty$ ($d_1=\infty$, $d_2=f$):

**(4.4-15) Radio de la mancha** (recuadro, p. 134): $\rho_s=1.22\lambda F_\#$, con
$F_\#=f/D$ el número F de la lente. Menor $F_\#$ (abertura mayor) → mejor calidad (si no hay
aberraciones geométricas).

**Función de transferencia** (p. 135): el sistema de lente única no es invariante al
desplazamiento (un desplazamiento $\Delta$ del objeto produce $M\Delta$ en la imagen,
$M=-d_2/d_1$ el aumento). Se ve como cascada: aumento ideal (variante) seguido de desenfoque
(blur) aproximadamente invariante cerca del eje (Fig. 4.4-9, p. 135). TF del sistema de
desenfoque (TF de (4.4-11)):

**(4.4-16) Función de transferencia** (recuadro, p. 135):
$$H(\nu_x,\nu_y)\approx p_1(\lambda d_2\nu_x,\lambda d_2\nu_y)$$
(ignorando $\exp(-jkd_1)\exp(-jkd_2)$). Enfocado:

**(4.4-17)** $H(\nu_x,\nu_y)\approx p(\lambda d_2\nu_x,\lambda d_2\nu_y)$, idéntico al 4-f [(4.4-4)].
Abertura circular de diámetro $D$: $H$ constante dentro del círculo de radio

**(4.4-18)** $\nu_s=\dfrac D{2\lambda d_2}$ (Fig. 4.4-10, p. 136). Enfocada a infinito ($d_2=f$):

**(4.4-19) Ancho de banda espacial** (recuadro, p. 136): $\nu_s=\dfrac1{2\lambda F_\#}$.
Ejemplo: lente F-2 ($F_\#=2$), $\lambda=0.5\,\mu$m → $\nu_s=500$ líneas/mm. $\nu_s$ es la
máxima frecuencia espacial que el sistema puede transmitir.

#### 4.4D Near-Field Imaging (p. 136)

Ancho de banda del espacio libre $\lambda^{-1}$ (§4.1B): frecuencias mayores → ondas
evanescentes que decaen en distancias del orden de $\lambda$; detalles menores que $\lambda$
no se transmiten. Un sistema con lente de $F_\#$ dado tiene $h$ de radio $1.22\lambda F_\#$
(Fig. 4.4-11(a)); un sistema de barrido con láser enfocado tiene spot de radio
$1.22\lambda F_\#$ (Fig. 4.4-11(b)): **límite de difracción**. Se puede sortear: la luz
*sí* puede localizarse en un spot sub-λ *dentro de un plano*; las evanescentes decaen
en distancia corta, el spot diverge y luego se vuelve esférico. Solución: poner el objeto
muy cerca del spot sub-λ, iluminando a través de una abertura de diámetro ≪ λ
(Fig. 4.4-11(c), p. 137). El objeto se coloca a distancia sub-λ (usualmente < mitad del
diámetro de la abertura); las componentes propagantes forman una onda esférica de amplitud
∝ transmitancia local; resolución ≈ tamaño de la abertura; se construye la imagen barriendo
(raster) y registrando con un sistema convencional de campo lejano: **near-field optical
imaging / SNOM (scanning near-field optical microscopy)**, dentro de la **nanofotónica**
(p. 137). Implementación: fibra con punta cónica recubierta de aluminio (Fig. 4.4-12,
p. 137); la luz se guía por reflexión interna total, luego por el recubrimiento metálico
(espejo cónico), y cuando el diámetro es muy pequeño la onda ya no se guía (§8.1) y se vuelve
evanescente; la distribución al final de la punta se calcula numéricamente. Aberturas y
resoluciones de decenas de nm con luz visible; se requiere realimentación para mantener la
distancia a pocos nm. Aplicaciones: caracterización no destructiva de materiales
inorgánicos, orgánicos, compuestos y biológicos y nanoestructuras.

---

### 4.5 Holography (p. 138)

**Holografía**: registro y reconstrucción de ondas ópticas. Un **holograma** es una
transparencia con un registro codificado de la onda (amplitud y fase). Si existiera una
transparencia con $\mathsf t(x,y)=U_o(x,y)$, al iluminarla con onda plana unitaria en $z$ se
reproduciría $U(x,y)=1\cdot\mathsf t=U_o$ en $z=0$ y por tanto en todo $z>0$. Ejemplo: onda
plana oblicua $U_o=\exp[-jkx\sin\theta]$ → transparencia-prisma que desvía en $\theta$
(§2.4B). Problema: los detectores (emulsiones) responden a $|U_o|^2$ y son insensibles a
$\arg\{U_o\}$; hay que codificar la fase en intensidad.

**El código holográfico** (p. 138): mezclar la **onda objeto** $U_o$ con una **onda de
referencia** $U_r$ conocida y registrar su interferencia en $z=0$ [Fig. 4.5-1(a), p. 139]:

**(4.5-1)**
$$\mathsf t\propto|U_o+U_r|^2=|U_r|^2+|U_o|^2+U_r^*U_o+U_rU_o^*=I_r+I_o+U_r^*U_o+U_rU_o^*=I_r+I_o+2\sqrt{I_rI_o}\cos[\arg\{U_r\}-\arg\{U_o\}].$$
El holograma es sensible a la diferencia de fases (§2.5; análogo temporal: heterodinaje,
§2.6). Reconstrucción: iluminar con $U_r$ [Fig. 4.5-1(b)]:

**(4.5-2)** $U=\mathsf tU_r\propto U_rI_r+U_rI_o+I_rU_o+U_r^2U_o^*$

en $z=0$. Tercer término: onda original × $I_r$ (si $I_r$ uniforme, es la reconstrucción
deseada); cuarto: conjugada modulada por $U_r^2$; dos primeros: referencia modulada por la
suma de intensidades. Con referencia plana uniforme $\sqrt{I_r}\exp(-jkz)$, $U_r=\sqrt{I_r}$ en
$z=0$ y dividiendo por $U_r$:

**(4.5-3) Onda reconstruida en el plano del holograma** (recuadro, p. 139):
$$U(x,y)\propto I_r+I_o(x,y)+\sqrt{I_r}\,U_o(x,y)+\sqrt{I_r}\,U_o^*(x,y).$$

**Ejemplo 4.5-1 Hologram of an Oblique Plane Wave** (p. 139): $U_o=\sqrt{I_o}\exp(-jkx\sin\theta)$
→ $U\propto I_r+I_o+\sqrt{I_rI_o}\exp(-jkx\sin\theta)+\sqrt{I_rI_o}\exp(+jkx\sin\theta)$: dos
términos constantes (continuación de la referencia en $z$), la onda objeto a $\theta$ y la
**onda conjugada** a $-\theta$. El holograma es el patrón de interferencia de dos ondas
planas (§2.5A): rejilla de difracción sinusoidal que divide la referencia en tres ondas a
$0,\theta,-\theta$ (Fig. 4.5-2, p. 140; §2.4B).

**Ejemplo 4.5-2 Hologram of a Point Source** (p. 139, Fig. 4.5-3 p. 140): onda esférica
desde $\mathbf r_0=(0,0,-d)$, $U_o\propto\exp(-jk|\mathbf r-\mathbf r_0|)/|\mathbf r-\mathbf r_0|$,
$\mathbf r=(x,y,0)$. Tercer término: la esférica original desde $(0,0,-d)$; cuarto: conjugada
$\propto\exp(+jk|\mathbf r-\mathbf r_0|)/|\mathbf r-\mathbf r_0|$, esférica convergente a
$(0,0,d)$ (imagen real del punto); segundo $\propto1/|\mathbf r-\mathbf r_0|^2$, viaja en $z$
con dispersión angular muy pequeña.

**Holografía fuera de eje (off-axis)** (pp. 140–141): separar las cuatro componentes por
multiplexado en frecuencia espacial (§4.1A), haciendo que objeto y referencia lleguen de
direcciones bien separadas. $U_o=f(x,y)\exp(-jkx\sin\theta)$, con $f$ lentamente variable de
frecuencia máxima $\nu_s$ ↔ ángulo $\theta_s=\sin^{-1}\lambda\nu_s\ll\theta$:

**(4.5-4)**
$$U(x,y)\propto I_r+|f(x,y)|^2+\sqrt{I_r}f(x,y)\exp(-jkx\sin\theta)+\sqrt{I_r}f^*(x,y)\exp(+jkx\sin\theta).$$
Tercer término: réplica del objeto a $\theta$; cuarto: conjugada a $-\theta$; primero: plana
en $z$; segundo: **término de ambigüedad**, onda no uniforme en un cono de ángulo $2\theta_s$
alrededor de $z$ (Fig. 4.5-4, p. 141). Separación angular natural si $\theta>3\theta_s$
(p. 141). Alternativa: hacer $I_r\gg I_o$ para que la ambigüedad sea despreciable.

**Holografía de transformada de Fourier** (p. 141): $F(x/\lambda f,y/\lambda f)$ (amplitud
en el otro plano focal de una lente) es compleja y no puede registrarse directamente; se
registra como objeto $U_o=f(x/\lambda f,y/\lambda f)$ [el libro escribe así; se refiere a la
TF] mezclado con referencia $U_f(x,y)$ [Fig. 4.5-5(a), p. 142]; reconstrucción con la
referencia y TF inversa con una lente recupera $f(x,y)$ [Fig. 4.5-5(b)].

**Filtros espaciales holográficos** (pp. 141–142): un filtro de $H(\nu_x,\nu_y)$ se
implementa en un 4-f con máscara $p(x,y)=H(x/\lambda f,y/\lambda f)$ (§4.4B), pero $H$ es
compleja y difícil de fabricar. Si $h(x,y)$ es real, se registra holográficamente
$U_o=H(x/\lambda f,y/\lambda f)$; usando como referencia la TF de la entrada,
$U_r=F(x/\lambda f,y/\lambda f)$, el holograma construye

**(4.5-5)** $U_r(x,y)U_o(x,y)=F(x/\lambda f,y/\lambda f)\,H(x/\lambda f,y/\lambda f).$
TF inversa con lente [Fig. 4.5-6(b)] → $g$ con $G=HF$: convolución de $f$ con $h$. **Filtro
de Vander Lugt** (p. 142). Si en cambio se transforma la conjugada $U_rU_o^*=FH^*$ se
obtiene la **correlación** (reconocimiento de patrones).

**El aparato holográfico** (pp. 142–143): fuente monocromática con mínimas fluctuaciones de
fase (láser; coherencia en cap. 10). Fig. 4.5-7 (p. 143): divisor de haz, referencia y haz
dispersado por el objeto; la diferencia de camino debe ser mínima para mantener
$\arg\{U_r\}-\arg\{U_o\}$ no aleatoria. Las franjas están separadas ~$\lambda/\sin\theta$:
película de alta resolución y sin vibraciones; mayor $\theta$ → requisitos más estrictos. Al
reconstruir, el observador ve el objeto con su carácter tridimensional.

**Holografía de volumen** (pp. 143–145): medio grueso entre $z=0$ y $z=\Delta$; referencia y
objeto planas con $\mathbf k_r$, $\mathbf k_o$ (Fig. 4.5-8, p. 144):

**(4.5-6)**
$$I(x,y,z)=\left|\sqrt{I_r}e^{-j\mathbf k_r\cdot\mathbf r}+\sqrt{I_o}e^{-j\mathbf k_o\cdot\mathbf r}\right|^2=I_r+I_o+2\sqrt{I_rI_o}\cos(\mathbf k_o\cdot\mathbf r-\mathbf k_r\cdot\mathbf r)=I_r+I_o+2\sqrt{I_rI_o}\cos(\mathbf k_g\cdot\mathbf r),$$
$\mathbf k_g=\mathbf k_o-\mathbf k_r$ (**vector de rejilla**); periodo $\Lambda=2\pi/|\mathbf k_g|$,
superficies de intensidad constante normales a $\mathbf k_g$. Si la referencia va en $z$ y el
objeto a $\theta$: $|\mathbf k_g|=2k\sin(\theta/2)$ y

**(4.5-7)** $\Lambda=\dfrac\lambda{2\sin(\theta/2)}.$

Registrado en emulsión → rejilla gruesa, **holograma de volumen**. Reconstrucción
(Fig. 4.5-9, p. 144): los planos de la rejilla reflejan solo si se cumple la **condición de
Bragg** $\sin\phi=\lambda/2\Lambda$, con $\phi$ el ángulo entre los planos y la referencia
(Ejercicio 2.5-3); aquí $\phi=\theta/2$ y por (4.5-7) se cumple: la onda reflejada es una
extensión de la onda objeto. Con otra longitud de onda $\lambda'$, $\sin(\theta/2)=\lambda'/2\Lambda$
no se cumple y no hay reflexión → el objeto se reconstruye solo con la $\lambda$ de registro;
con luz blanca solo la $\lambda$ "correcta" se refleja: **la reconstrucción puede hacerse con
luz blanca** aunque el registro sea monocromático (p. 144). Fig. 4.5-10 (p. 145): holograma
de transmisión (ondas del mismo lado; reconstrucción con referencia invertida da la
conjugada) y de reflexión (ondas de lados opuestos; reconstrucción por reflexión).

**Holograma arcoíris (rainbow)** (pp. 144–145): registrado a través de una rendija
estrecha; con otra $\lambda$ la imagen parece venir de una rendija desplazada (aumento); con
luz blanca, arcoíris de imágenes vistas por rendijas paralelas, con paralaje solo en la
dirección de la rendija. Usos comerciales como displays.

---

### Reading List (pp. 145–147)

Agrupada en *Fourier Optics and Optical Signal Processing* (Goodman 3.ª ed. 2005; Steward;
Lauterborn & Kurz; O'Neill; Papoulis; Gaskill; Duffieux; Cagnet–Françon–Thrierr *Atlas of
Optical Phenomena* 1962; etc.), *Diffraction* (Ersoy 2007; Nieto-Vesperinas; Sommerfeld
1896; O'Shea et al. *Diffractive Optics*; Cowley; Nussenzveig; Solimeno–Crosignani–Di Porto
1986; Françon), *Imaging* (Novotny & Hecht *Principles of Nano-Optics* 2006; Barrett & Myers;
Courjon; Williams & Becklund *Optical Transfer Function*; Kawata; de Fornel *Evanescent
Waves*; Gu; Herzig; Fillard; Françon; Dainty & Shaw; Barnes) y *Holography* (Saxby; Schnars
& Jueptner *Digital Holography*; Yaroslavsky; Hariharan 2002 y 1996; Bjelkhagen & Caulfield;
Kasper & Feller; Sirohi & Hinsch; Soifer & Golub; Smith; Schumann et al.; Abramson;
Ostrovsky et al.; Soroko; Caulfield *Handbook*; Vest; Collier–Burckhardt–Lin; Françon;
Caulfield & Sun).

---

## Tablas y datos numéricos útiles

| Cantidad | Valor / expresión | Página |
|---|---|---|
| Ancho de banda espacial del espacio libre | $\nu_{\max}\approx\lambda^{-1}$ ciclos/mm | 112 |
| Caída de la evanescente a $e^{-2\pi}$ | $(\nu_\rho-1/\lambda)/(1/\lambda)\approx\tfrac12(\lambda/d)^2$ | 112 |
| Número de Fresnel | $N_F=a^2/\lambda d$ | 113 |
| Validez Fresnel | $N_F\theta_m^2/4\ll1$, $\theta_m\approx a/d$ | 113 |
| Validez Fraunhofer | $N_F=a^2/\lambda d\ll1$ y $N_F'=b^2/\lambda d\ll1$ | 117 |
| Ejemplo Fresnel: $a=1$ cm, $d=100$ cm, $\lambda=0.5\,\mu$m | $\theta_m=10^{-2}$ rad, $N_F=200$, $N_F\theta_m^2/4=5\times10^{-3}$ | 113 |
| Ejercicio 4.2-1 | $\lambda=0.5\,\mu$m, $b=1$ cm, $a=2$ cm | 117 |
| $h_0$ espacio libre | $(j/\lambda d)\exp(-jkd)$ | 114 |
| $h_l$ lente 2-f | $(j/\lambda f)\exp(-j2kf)$; $|h_l|=1/\lambda f$ | 119 |
| Divergencia abertura rectangular | $\theta_x=\lambda/D_x$ | 123 |
| Disco de Airy | $\rho_s=1.22\lambda d/D$; $\theta=1.22\lambda/D$ | 123 |
| Spot enfocado con lente | $\rho_s=1.22\lambda f/D=1.22\lambda F_\#$ | 124, 134 |
| Primeros lóbulos de $\cos\pi X^2$, $\sin\pi X^2$ | $|X|<1/\sqrt2$, $|X|<1$ | 125 |
| Haz gaussiano (Fresnel) | $W^2(d)=W_0^2+\theta_0^2d^2$, $\theta_0=\lambda/\pi W_0$ | 126 |
| Fig. 4.3-8: $(\pi/2)W_0^2/\lambda d=10,1,0.5,0.1$ | $W(d)/W_0=1.001,1.118,1.414,5.099$ | 127 |
| Sombra geométrica = ancho Fraunhofer | $N_F=0.5$ | 126 |
| Radio mancha desenfoque (rayos) | $\rho_s=\tfrac12\epsilon d_2D$ | 129 |
| Filtro pasa-bajas 4-f: $D=2$ cm, $\lambda=1\,\mu$m, $f=100$ cm | $\nu_s=D/2\lambda f=10$ líneas/mm; detalle ≈ 0.1 mm | 131 |
| Ancho de banda lente única | $\nu_s=D/2\lambda d_2$; a infinito $\nu_s=1/2\lambda F_\#$ | 135–136 |
| Lente F-2, $\lambda=0.5\,\mu$m | $\nu_s=500$ líneas/mm | 136 |
| SNOM | aberturas/resoluciones de decenas de nm con visible; distancia punta–objeto de pocos nm | 137 |
| Separación franjas del holograma | $\sim\lambda/\sin\theta$ | 143 |
| Periodo rejilla de volumen | $\Lambda=\lambda/2\sin(\theta/2)$; Bragg $\sin\phi=\lambda/2\Lambda$ | 143–144 |
| Separación en holografía fuera de eje | $\theta>3\theta_s$ | 141 |

No aparecen en este capítulo índices de refracción ni parámetros de materiales; los datos
numéricos son solo los ejemplos de arriba.

---

## Problemas al final del capítulo (pp. 147–149)

Los asteriscos (*) marcan los que el libro señala como avanzados.

- **4.1-3 Correspondence Between Harmonic Functions and Plane Waves** (p. 147). Con
  $d=10^4\lambda$, hallar $g(x,y)$ en $z=d$ por análisis armónico para (a) $f=1$;
  (b) $f=\exp[(-j\pi/\lambda)(x+y)]$; (c) $f=\cos(\pi x/2\lambda)$; (d) $f=\cos^2(\pi y/2\lambda)$;
  (e) $f=\sum_m\mathrm{rect}[(x/10\lambda)-2m]$. Describir la naturaleza física de la onda.
- **4.1-4** (p. 147). Si $f$ es circularmente simétrica con frecuencia máxima 200 líneas/mm y
  $\lambda=633$ nm, hallar el ángulo del cono de direcciones de la onda.
- **4.1-5 Logarithmic Interconnection Map** (p. 147). $\mathsf t=\exp[-j2\pi\phi(x)]$,
  $\lambda=1\,\mu$m, lente adyacente $f=100$ cm; hallar $\phi(x)$ tal que el rayo en $x$ se
  enfoque en $x'=\ln(x)$ (mm); cómo modificar $\phi$ sin la lente (transformación logarítmica
  de coordenadas, cap. 21).
- **4.2-3 Proof of the Lens Fourier-Transform Property** (pp. 147–148). (a) Mostrar que la
  convolución de $f(x)$ con $\exp(-j\pi x^2/\lambda d)$ se hace en tres pasos (multiplicar por
  $\exp(-j\pi x^2/\lambda d)$, TF evaluada en $\nu_x=x/\lambda d$, multiplicar por
  $\exp(-j\pi x^2/\lambda d)$); (b) derivar (4.2-8) como cascada espacio $f$ – lente – espacio $f$.
- **4.2-4 Fourier Transform of the Line Functions** (p. 148). $\lambda=1\,\mu$m, $f=100$ cm;
  bosquejar la intensidad en la transparencia y en el plano focal para (a) $\mathsf t=\delta(x-y)$;
  (b) $\delta(x+a)+\delta(x-a)$, $a=1$ mm; (c) $\delta(x+a)+j\delta(x-a)$.
- **4.2-5 Design of an Optical Fourier-Transform System** (p. 148). Frecuencias entre 20 y
  200 líneas/mm, $\lambda=488$ nm; focal para que estén separadas 9 cm en el plano de Fourier.
- **4.3-4 Fraunhofer Diffraction from a Diffraction Grating** (p. 148). $M=2L+1$ rendijas
  infinitesimales separadas $a=10\lambda$: $p(x,y)=\sum_{m=-L}^L\delta(x-ma)$ (4.5-8); bosquejar
  en función de $\theta=x/d$.
- **4.3-5 Fraunhofer Diffraction with an Oblique Incident Wave** (p. 148). Patrón cuando la
  onda incide a ángulo pequeño $\theta_x\ll1$ en el plano $x$–$z$.
- ***4.3-6 Fresnel Diffraction from Two Pinholes** (p. 148). Mostrar que para
  $p=[\delta(x-a)+\delta(x+a)]\delta(y)$ el patrón es $I=(2/\lambda d)^2\cos^2(2\pi ax/\lambda d)$.
- ***4.3-7 Relation Between Fresnel and Fraunhofer Diffraction** (p. 148). Mostrar que el
  patrón de Fresnel de $p$ es el de Fraunhofer de $p\exp[-j\pi(x^2+y^2)/\lambda d]$.
- **4.4-1 Blurring a Sinusoidal Grating** (p. 148). $f=\cos^2(2\pi x/a)$ con $h=1$ en un
  cuadrado de ancho $D$; hallar $g(x,0)$ y el contraste $(\max-\min)/(\max+\min)$ en función
  de $D/a$.
- **4.4-2 Image of a Phase Object** (p. 148). $h=\mathrm{rect}(x)\delta(y)$, entrada
  $f=\exp(j\pi/2)$ para $x>0$ y $\exp(-j\pi/2)$ para $x\le0$ (4.5-9); hallar y bosquejar
  $|g|^2$ y verificar que no es uniforme aunque $|f|^2=1$.
- **4.4-3 Optical Spatial Filtering** (p. 149). Sistema de Fig. 4.4-5 con $f=1000$ mm,
  $\lambda=10^{-3}$ mm; relación $g\leftrightarrow f,p$; bosquejar $g(x,0)$ para
  (a) $f=\delta(x-5)$, $p=\mathrm{rect}(x)$; (b) $f=\mathrm{rect}(x)$, $p=\mathrm{sinc}(x)$.
  Hallar $p$ tal que $g=\nabla_T^2f$ (laplaciano transversal).
- **4.4-4 Optical Cross-Correlation** (p. 149). Filtro espacial para correlación cruzada de
  $f_1,f_2$ reales; condiciones para que máscaras y transparencias sean reales.
- ***4.4-5 Impulse Response Function of a Severely Defocused System** (p. 149). Mostrar con
  ondas (fase estacionaria, p. 117, con (4.4-11) y (4.4-10)) que
  $h\approx p(x/\epsilon d_2,y/\epsilon d_2)$, igual al resultado de rayos (4.4-2).
- **4.4-6 Two-Point Resolution** (p. 149). (a) $h$ para abertura cuadrada de ancho $D$,
  aumento 1, foco perfecto; (b) respuesta a $f=\delta(x)\delta(y)+\delta(x-b)\delta(y)$ (4.5-10);
  (c) con $\lambda d_2/D=0.1$ mm, bosquejar $|g(x,0)|$ para $b=0.5,1,2$ mm; separación mínima
  para ver dos picos.
- **4.4-7 Ring Aperture** (p. 149). (a) Sistema enfocado $M=1$, $f=100$ cm, abertura anular
  $a\le\rho\le b$ (4.5-11) con $a=5$ mm, $b=6$ mm, $\lambda=1\,\mu$m: hallar $H$ y bosquejar
  $H(\nu_x,0)$; (b) con $d_2=25$ cm, hallar $h$ por óptica de rayos y bosquejar $h(x,0)$.
- **4.5-1 Holography with a Spherical Reference Wave** (p. 149). Referencia esférica centrada
  en $(0,0,-d)$; hologramas y reconstrucción para (a) objeto onda plana a $\theta_x$;
  (b) objeto esférica centrada en $(-x_0,0,-d_1)$. Aproximar esféricas por paraboloidales.
- **4.5-2 Optical Correlation** (p. 149). $f=f_1(x-a,y)+f_2(x+a,y)$ se transforma con lente,
  se registra la intensidad (holograma), se ilumina con referencia y se transforma de nuevo:
  relación $g\leftrightarrow f_1,f_2$ y cómo obtener su correlación.

(Nota: la numeración de los problemas salta — 4.1-3, 4.1-4, 4.1-5, 4.2-3, … — porque los
ejercicios 4.1-1, 4.1-2, 4.2-1, 4.2-2, 4.3-1, 4.3-2, 4.3-3 están dentro del texto.)

---

## Relación con Óptica No Lineal

### Analogía difracción (transformada espacial) ↔ dispersión de pulsos (transformada temporal)

Es la conexión central de este capítulo con el curso. El libro mismo la sugiere en p. 107–108
("el espacio libre es un *prisma espacial* natural, sensible a las frecuencias espaciales y
no a las temporales") y en p. 138 ("el análogo temporal de la holografía es el heterodinaje").

| Espacio (cap. 4) | Tiempo (pulsos en medios dispersivos, Saleh §5.6 / Agrawal) |
|---|---|
| $f(x,y)=U(x,y,0)$, $F(\nu_x,\nu_y)$ | envolvente $A(0,t)$, espectro $\tilde A(0,\omega)$ |
| onda plana $\exp[-j2\pi(\nu_xx+\nu_yy)]$ | armónica temporal $\exp(j\omega t)$ (signo opuesto, nota p. 103) |
| $H(\nu_x,\nu_y)=\exp(-jk_zd)$, (4.1-9) | $H(\omega)=\exp[-j\beta(\omega)z]$ |
| Fresnel: $k_z\approx k-\pi\lambda(\nu_x^2+\nu_y^2)$ → fase $j\pi\lambda d(\nu_x^2+\nu_y^2)$, (4.1-11) | Taylor: $\beta\approx\beta_0+\beta_1\Omega+\tfrac12\beta_2\Omega^2$ → fase $-\tfrac12j\beta_2z\Omega^2$ (GVD) |
| $h(x,y)\propto\exp[-jk(x^2+y^2)/2d]$, (4.1-18) | $h(t)\propto\exp(jt^2/2\beta_2z)$ (chirp cuadrático) |
| $g=f*h$, (4.1-20) | $A(z,t)=A(0,t)*h(t)$ |
| Fraunhofer $g\propto F(x/\lambda d,y/\lambda d)$, (4.2-1) | campo lejano temporal: $A(z,t)\propto\tilde A(0,\,\Omega=t/\beta_2z)$ — el pulso adopta la forma de su espectro |
| número de Fresnel $N_F=a^2/\lambda d$ | $\tau_0^2/|\beta_2|z=L_D/z$ (longitud de dispersión $L_D=\tau_0^2/|\beta_2|$) |
| haz gaussiano $W^2(d)=W_0^2+\theta_0^2d^2$, (4.3-17) | pulso gaussiano $\tau^2(z)=\tau_0^2[1+(z/L_D)^2]$ |
| lente $\exp[j\pi(x^2+y^2)/\lambda f]$, Ej. 4.1-2 | "lente temporal": modulación de fase cuadrática (p. ej. SPM aproximada cerca del pico, o modulador electro-óptico) |
| sistema 2-f / 4-f, filtrado espacial (§4.2B, §4.4B) | conformador de pulsos 4-f (rejilla–lente–máscara–lente–rejilla): la máscara actúa sobre el espectro |
| multiplexado por frecuencia espacial (p. 108) | portadora óptica y bandas laterales (modulación) |
| onda evanescente: $\nu>1/\lambda$ (p. 112) | no hay análogo directo; sí lo hay la idea de ancho de banda del sistema |
| holograma (interferencia con referencia, p. 138) | heterodinaje (§2.6), detección coherente de fase |

Consecuencias prácticas para el curso: (i) la **función de transferencia del espacio libre**
(4.1-9)/(4.1-11) es el mismo objeto matemático que la del medio dispersivo; la expansión
(4.1-10) en potencias de $\theta^2$ es el equivalente de la expansión de $\beta(\omega)$ en
$\beta_2,\beta_3,\dots$, y el criterio (4.1-12)–(4.1-13) de despreciar el término $\theta^4$ es
el análogo de despreciar $\beta_3$ (TOD); (ii) la **aproximación de Fraunhofer** es el "campo
lejano temporal": tras mucha dispersión ($z\gg L_D$) la forma temporal del pulso reproduce
su espectro, lo que se usa en medidas de espectro vía dispersión y en el análisis de
supercontinuo; (iii) la relación $\theta_x\approx\lambda\nu_x$ y $\theta=1.22\lambda/D$ es el
análogo de $\Delta\omega\sim1/\tau_0$ (producto tiempo–ancho de banda).

### Otros temas del curso

- **Ondas EM y haz gaussiano**: Ejercicio 4.1-2 (p. 115) y Ejemplo 4.3-2 (p. 126) derivan el
  haz gaussiano del cap. 3 desde la óptica de Fourier (espacial y de frecuencia); útil para
  justificar los parámetros $W(z)$, $\theta_0=\lambda/\pi W_0$ al acoplar luz a una guía o
  estimar el spot enfocado ($\rho_s=1.22\lambda F_\#$ vs. gaussiano, Ejercicio 4.3-3).
- **Absorción/dispersión y pulsos**: ver tabla anterior; la noción de sistema LTI con $H$ y
  $h$ (Apéndice B) es la base del tratamiento de GVD.
- **Susceptibilidad no lineal, $\chi^{(2)}$, $\chi^{(3)}$, índice dependiente de la
  intensidad**: la transparencia de fase $\exp[-j2\pi\phi(x,y)]$ con frecuencia espacial
  local $\partial\phi/\partial x$ (p. 109) es el modelo de un medio Kerr: un haz intenso
  induce $n=n_0+n_2I$ y por tanto una fase $\phi\propto n_2I(x,y)$ que desvía/enfoca el propio
  haz (**autoenfoque** = lente inducida, Ej. 4.1-2) — análogo espacial exacto de **SPM**
  (fase $\propto I(t)$ con frecuencia instantánea $\propto\partial I/\partial t$). La condición
  de Bragg y los hologramas de volumen (4.5-6)–(4.5-7) son la base de las rejillas
  fotorrefractivas y del **mezclado de cuatro ondas degenerado** (conjugación de fase: el
  cuarto término $U_o^*$ en (4.5-3) es exactamente la onda conjugada que produce FWM).
- **Raman, FWM**: la selección de direcciones por "phase matching" espacial (interferencia
  constructiva cuando $\Lambda\sin\theta=\lambda$, p. 106; Bragg p. 144) es el mismo argumento
  de conservación de $\mathbf k$ que fija el ajuste de fases $\Delta\mathbf k=0$ en FWM y SHG.
- **Polarización y cristales**: no se trata en este capítulo (tratamiento escalar).

### Proyecto final (anillos add-drop en Si₃N₄, dispersión de guías, supercontinuo, sensado)

- **Dispersión de guías / supercontinuo**: la formulación $H(\omega)=\exp[-j\beta(\omega)z]$ y
  la aproximación cuadrática son la plantilla para construir, a partir del $n_{\rm eff}(\lambda)$
  que se obtenga con MODE, $\beta_2(\lambda)$ y la longitud de dispersión; la discusión de
  Fresnel vs Fraunhofer (cuándo se puede truncar la expansión) da el criterio de cuándo
  incluir $\beta_3$ en la simulación del supercontinuo (ancho de banda muy grande ⇒ hay que
  retener órdenes altos, igual que a ángulos grandes hay que retener $\theta^4$).
- **Ondas evanescentes y sensado de índice**: la onda evanescente (p. 112) y la sección de
  campo cercano/SNOM (pp. 136–137) explican por qué el modo de la guía "siente" el cladding:
  las componentes con $k_\perp$ mayor que el de propagación en el analito decaen en una
  distancia ~λ, que es exactamente la región donde el cambio de $n$ (1.33→1.37) desplaza
  $n_{\rm eff}$ y la resonancia del anillo. Útil para justificar en el informe la
  sensibilidad bulk y la profundidad de penetración.
- **Anillos add-drop**: el acoplador direccional es un acoplamiento por evanescentes; la
  condición de Bragg (4.5-7) es la referencia si se consideran rejillas o reflectores
  distribuidos. La idea de función de transferencia $H$ del sistema lineal (Apéndice B) es
  la misma con la que se describe el anillo en INTERCONNECT (respuesta espectral = $H(\omega)$).
- **Figuras de mérito ópticas**: límite de difracción $\theta=1.22\lambda/D$ y ancho de banda
  $1/2\lambda F_\#$ (pp. 123, 136) para estimar spots de acoplamiento por objetivo a la guía o
  a la fibra con punta cónica (Fig. 4.4-12).

---

## Páginas ilegibles o dudosas

Ninguna página ilegible. Las páginas 111, 135 y 137 del libro (PDF 133, 157, 159) se
renderizaron a menor resolución pero el texto y las ecuaciones se leyeron sin problema.
Una sola observación de redacción del libro: en p. 141 ("Fourier-Transform Holography")
el texto define $U_o(x,y)=f(x/\lambda f,y/\lambda f)$ cuando por el contexto se refiere a la
TF $F(x/\lambda f,y/\lambda f)$; se transcribe tal cual y se anota la discrepancia.
