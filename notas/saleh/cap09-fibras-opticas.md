# Capítulo 9 — Fiber Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 325–364 (PDF 347–386). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 9.
Convención del libro: dependencia temporal $e^{j\omega t}$, $j=\sqrt{-1}$; campos reales en caligráfica
($\mathcal{E}$, $\mathcal{P}$), amplitudes complejas en negrita ($\mathbf{E}$, $\mathbf{H}$); $k_o = 2\pi/\lambda_o$ número de onda en vacío,
$c_o$ velocidad de la luz en vacío, $c_1 = c_o/n_1$. Unidades SI.

Portada (p. 325): Charles Kao (n. 1933) promovió el uso de fibras de bajas pérdidas en telecomunicaciones;
Philip St John Russell (n. 1953) inventó la fibra de cristal fotónico en 1991.

## Resumen del capítulo

Una fibra óptica es una guía de onda dieléctrica cilíndrica de bajas pérdidas (sílice) con un **núcleo** de índice $n_1$
rodeado de un **revestimiento** (cladding) de índice ligeramente menor $n_2$; la luz se guía por reflexión total interna
(p. 326). El capítulo primero describe las fibras de índice escalonado y de índice gradual con óptica de rayos (§9.1:
rayos meridionales y oblicuos, apertura numérica, perfil de ley de potencias), luego con óptica electromagnética (§9.2:
ecuación de Helmholtz en coordenadas cilíndricas, funciones de Bessel, parámetro $V$, modos $\mathrm{LP}_{lm}$, ecuación
característica, corte $V<2.405$ para operación monomodo, número de modos $M\approx 4V^2/\pi^2$, constantes de propagación y
velocidades de grupo para $V\gg1$, fibras monomodo y que mantienen la polarización, y método WKB/ondas cuasi-planas para
fibras de índice gradual con perfil óptimo $p=2$). Después trata la atenuación (§9.3A: dB/km, absorción IR/UV, dispersión
de Rayleigh $\propto 1/\lambda_o^4$, OH; mínimos de 0.3 dB/km a 1.3 μm y 0.15 dB/km a 1.55 μm) y los cinco mecanismos de
dispersión (§9.3B: modal, de material con $D_\lambda = -(\lambda_o/c_o)\,d^2n/d\lambda_o^2$ y cero en 1.312 μm, de guía
$D_w\propto V^2 d^2\beta/dV^2$, de modo de polarización $\sigma_{\rm PMD}=D_{\rm PMD}\sqrt{L}$ y no lineal/SPM/solitones), con
fibras de dispersión desplazada, aplanada y compensadora. Cierra con fibras agujereadas y de cristal fotónico (§9.4:
guiado por índice efectivo, monomodo sin fin, gran área modal, guiado por banda fotónica prohibida, núcleo hueco).

## Secciones

### Introducción (p. 326–327)

- **Definición** (p. 326): fibra óptica = guía dieléctrica cilíndrica de material de bajas pérdidas (vidrio de sílice),
  núcleo central de radio $a$ e índice $n_1$, revestimiento exterior de radio $b$ e índice $n_2<n_1$ (Fig. 9.0-1). Rayos que
  inciden en la frontera núcleo–revestimiento con ángulo mayor que el crítico sufren reflexión total interna y se guían;
  los de mayor inclinación pierden potencia en cada reflexión.
- Pérdida alcanzable: $\approx 0.15$ dB/km ($\approx 3.4\%$ por km) en la longitud de onda de máxima transparencia (p. 326).
- Principios iguales a los de la guía plana (cap. 8), pero con geometría cilíndrica. Cada modo viaja con constante de
  propagación y velocidad de grupo propias, manteniendo distribución transversal y polarización. Núcleo pequeño → un solo
  modo: **fibra monomodo (SMF)**; núcleo grande → **fibra multimodo (MMF)** (p. 326).
- **Dispersión modal** (p. 326): diferencia entre velocidades de grupo de los modos → ensanchamiento del pulso; limita la
  tasa de datos de sistemas multimodo. Se reduce con **fibra de índice gradual (GRIN)**: $n$ máximo en el eje y mínimo en la
  frontera, de modo que los rayos más inclinados viajan más rápido y se igualan los tiempos de tránsito. Fibras con $n$
  constante en núcleo y revestimiento: **índice escalonado (step-index)**.
- Fig. 9.0-2 (p. 327): geometría, perfil de índice y rayos típicos en MMF de índice escalonado, SMF y GRIN MMF.
- "This Chapter" (p. 327): §9.1 rayos; §9.2 ondas/modos; §9.3 atenuación y dispersión (material, modal, de guía, PMD) y
  propagación de pulsos; §9.4 fibras agujereadas y de cristal fotónico. Se retoma en caps. 22 (óptica ultrarrápida) y 24
  (comunicaciones por fibra).

### 9.1 Guided Rays (p. 327)

#### 9.1A Step-Index Fibers (p. 327)

- Fibra de índice escalonado: especificada por $n_1$, $n_2$ y radios $a$, $b$. Razones diámetro núcleo/revestimiento
  estándar $2a/2b$ (μm/μm): 8/125, 50/125, 62.5/125, 85/125, 100/140 (p. 327).
- **Cambio fraccional de índice** (p. 327):
  $$\Delta \equiv \frac{n_1^2-n_2^2}{2n_1^2} \approx \frac{n_1-n_2}{n_1} \ll 1. \tag{9.1-1}$$
- Material: sílice fundida (SiO₂) de alta pureza, dopada con Ti, Ge, B. $n_1$ entre 1.44 y 1.46 según $\lambda$;
  $\Delta$ típicamente entre 0.001 y 0.02 (p. 327).
- Condición de guiado (p. 328): ángulo de incidencia en la frontera núcleo–revestimiento mayor que el ángulo crítico
  $\theta_c = \sin^{-1}(n_2/n_1)$.
- **Rayos meridionales** (p. 328, Fig. 9.1-1): confinados a planos que pasan por el eje; se comportan como en guía plana.
  Guiados si el ángulo $\theta$ con el eje es menor que el complemento del crítico:
  $\theta < \bar\theta_c = \pi/2-\theta_c = \cos^{-1}(n_2/n_1)$. Como $n_1\approx n_2$, $\bar\theta_c$ es pequeño y los
  rayos guiados son aproximadamente paraxiales.
- **Rayos oblicuos (skewed)** (p. 328, Fig. 9.1-2): plano de incidencia paralelo al eje a distancia $R$; el rayo se
  identifica por $\theta$ (ángulo con el eje) y $\phi$ (ángulo del plano con la normal a la frontera). Meridional: $\phi=0$,
  $R=0$. El rayo oblicuo sigue trayectoria helicoidal confinada en una corona cilíndrica de radios $R$ y $a$; su proyección
  transversal es un polígono regular no necesariamente cerrado. Condición de reflexión total: $\theta<\bar\theta_c$.
- **Apertura numérica** (p. 329): un rayo desde el aire se guía si, tras refractarse, $\theta<\bar\theta_c$. Con Snell
  $1\cdot\sin\theta_a = n_1\sin\bar\theta_c$ → $\sin\theta_a = n_1\sqrt{1-(n_2/n_1)^2} = \sqrt{n_1^2-n_2^2}$. Ángulo de
  aceptación:
  $$\theta_a = \sin^{-1}\mathrm{NA}, \tag{9.1-2}$$
  $$\boxed{\mathrm{NA} = \sqrt{n_1^2-n_2^2} \approx n_1\sqrt{2\Delta}} \quad \text{(Numerical Aperture)} \tag{9.1-3}$$
  usando $n_1-n_2 = n_1\Delta$ y $n_1+n_2\approx 2n_1$. $\theta_a$ define el cono de rayos externos guiados (Fig. 9.1-3);
  NA describe la capacidad colectora de luz y es crucial para acoplar luz dentro y fuera de la fibra (p. 329).
- **Ejemplo 9.1-1, Cladded and Uncladded Fibers** (p. 329–330): fibra de sílice $n_1=1.46$, $\Delta = 0.01$ →
  $\bar\theta_c = \cos^{-1}(n_2/n_1) = 8.1°$, $\theta_a = 11.9°$, $\mathrm{NA}=0.206$. Núcleo $n_1=1.46$ con revestimiento
  $n_2=1.064$ → $\bar\theta_c = 43.2°$, $\theta_a=90°$, NA $=1$ (todas las direcciones se guían, cono interno de $43.2°$).
  Fibra sin revestimiento ($n_2=1$): $\bar\theta_c = 46.8°$, también guía todo rayo incidente desde el aire; pero no es
  útil como guía por el gran número de modos que soporta.

#### 9.1B Graded-Index Fibers (p. 330)

- Idea (p. 330): índice máximo en el centro y decreciente hasta la frontera; la velocidad de fase es mínima en el centro y
  crece con $r$. Los rayos axiales recorren la distancia más corta a la velocidad de fase más baja; los oblicuos recorren
  más pero en medio más rápido → se compensan los tiempos de tránsito.
- Perfil: $n(r)$ con $n(0)=n_1$, $n(a)=n_2$; revestimiento constante $n_2$ (Fig. 9.1-4).
- **Perfil de ley de potencias** (p. 330):
  $$n^2(r) = n_1^2\left[1-2\left(\frac{r}{a}\right)^p\Delta\right],\qquad r\le a, \tag{9.1-4}$$
  $$\Delta = \frac{n_1^2-n_2^2}{2n_1^2}\approx\frac{n_1-n_2}{n_1}. \tag{9.1-5}$$
  $p$ = **parámetro de perfil de gradación**: $n^2(r)$ lineal en $r$ para $p=1$, cuadrático para $p=2$; tiende a escalón
  para $p\to\infty$ (Fig. 9.1-5, p. 331). La fibra de índice escalonado es caso particular de la GRIN.
- Rayos en GRIN parabólico (p. 331, Fig. 9.1-6; ver §1.3): meridionales → trayectorias planas oscilatorias dentro de un
  cilindro de radio $R_0$; oblicuos → hélices confinadas entre radios $r_l$ y $R_l$ (superficies cáusticas). Los rayos
  guiados no llegan al revestimiento.
- NA de la fibra GRIN: para rayos meridionales con perfil parabólico, la NA es la misma (9.1-3) (ver Ejercicio 1.3-2)
  (p. 331).

### 9.2 Guided Waves (p. 331)

- Objetivo (p. 331): campos de las ondas guiadas a partir de Maxwell y las condiciones de frontera; modos con constante de
  propagación, distribución transversal y dos polarizaciones independientes (Apéndice C). Solución exacta difícil → se
  usan aproximaciones.
- **Ecuación de Helmholtz** (p. 332): $n(r)=n_1$ ($r<a$), $n_2$ ($r>a$) en escalón; $n(r)$ continua en el núcleo para
  GRIN. Se asume $b\to\infty$. Cada componente de los campos monocromáticos obedece $\nabla^2U + n^2(r)k_o^2U = 0$,
  $k_o=2\pi/\lambda_o$ (exacta en cada región de la fibra escalonada; aproximada en el núcleo GRIN si $n(r)$ varía poco en
  una longitud de onda, §5.3). En cilíndricas (Fig. 9.2-1):
  $$\frac{\partial^2U}{\partial r^2}+\frac1r\frac{\partial U}{\partial r}+\frac1{r^2}\frac{\partial^2U}{\partial\phi^2}
  +\frac{\partial^2U}{\partial z^2}+n^2k_o^2U = 0, \tag{9.2-1}$$
  con $U=U(r,\phi,z)$. Modos guiados: dependencia $e^{-j\beta z}$ y periodicidad $2\pi$ en $\phi$ → $e^{-jl\phi}$:
  $$U(r,\phi,z) = u(r)\,e^{-jl\phi}e^{-j\beta z},\qquad l=0,\pm1,\pm2,\dots \tag{9.2-2}$$
  $$\frac{d^2u}{dr^2}+\frac1r\frac{du}{dr}+\left(n^2(r)k_o^2-\beta^2-\frac{l^2}{r^2}\right)u = 0. \tag{9.2-3}$$

#### 9.2A Step-Index Fibers (p. 332)

- Onda guiada (ligada) si $n_2k_o<\beta<n_1k_o$ (§8.2B). Se define (p. 332):
  $$k_T^2 = n_1^2k_o^2-\beta^2, \tag{9.2-4a}$$
  $$\gamma^2 = \beta^2-n_2^2k_o^2, \tag{9.2-4b}$$
  ambos positivos para ondas guiadas. Entonces (p. 333):
  $$\frac{d^2u}{dr^2}+\frac1r\frac{du}{dr}+\left(k_T^2-\frac{l^2}{r^2}\right)u=0,\quad r<a\ \text{(núcleo)}, \tag{9.2-5a}$$
  $$\frac{d^2u}{dr^2}+\frac1r\frac{du}{dr}-\left(\gamma^2+\frac{l^2}{r^2}\right)u=0,\quad r>a\ \text{(revestimiento)}. \tag{9.2-5b}$$
  Soluciones acotadas (excluyendo las que divergen en $r=0$ o $r\to\infty$):
  $$u(r)\propto\begin{cases}J_l(k_Tr), & r<a\ \text{(núcleo)}\\ K_l(\gamma r), & r>a\ \text{(revestimiento)}\end{cases} \tag{9.2-6}$$
  $J_l$: Bessel de primera especie de orden $l$ (oscila como seno/coseno con amplitud decreciente); $K_l$: Bessel
  modificada de segunda especie (decae exponencialmente). Fig. 9.2-2 (p. 333): $u(r)$ para $l=0$ ($J_0$, $K_0$) y $l=3$
  ($J_3$, $K_3$), con $u$ y $du/dr$ continuas en $r=a$.
- $k_T$ grande → más oscilaciones en el núcleo; $\gamma$ grande → decaimiento más rápido y menor penetración en el
  revestimiento. De (9.2-4):
  $$k_T^2+\gamma^2 = (n_1^2-n_2^2)k_o^2 = (\mathrm{NA})^2\cdot k_o^2, \tag{9.2-7}$$
  así que al crecer $k_T$ decrece $\gamma$ y el campo penetra más; si $k_T>\mathrm{NA}\cdot k_o$, $\gamma$ es imaginario
  y la onda deja de estar ligada (p. 333).
- **Parámetro V de la fibra** (p. 334):
  $$X = k_Ta,\qquad Y=\gamma a, \tag{9.2-8}$$
  $$X^2+Y^2 = V^2, \tag{9.2-9}$$
  $V=\mathrm{NA}\cdot k_oa$:
  $$\boxed{V = 2\pi\frac{a}{\lambda_o}\mathrm{NA}} \quad \text{(V Parameter)} \tag{9.2-10}$$
  Para que la onda sea guiada, $X<V$. $V$ gobierna el número de modos y sus constantes de propagación; proporcional a
  $a/\lambda_o$ y a NA; análogo a (8.2-7) de la guía plana.
- **Modos** (p. 334): se escriben $E_z$ y $H_z$ en la forma (9.2-2); continuidad en $r=a$ relaciona las constantes de
  proporcionalidad; con Maxwell ($j\omega\epsilon_on^2\mathbf{E}=\nabla\times\mathbf{H}$,
  $-j\omega\mu_o\mathbf{H}=\nabla\times\mathbf{E}$; (5.3-12), (5.3-13)) se obtienen $E_\phi,H_\phi,E_r,H_r$; la
  continuidad de $E_\phi$ y $H_\phi$ da dos ecuaciones más → **ecuación característica** o **relación de dispersión**
  para $\beta$ con $a/\lambda_o$, $n_1$, $n_2$ dados. Para cada $l$ hay soluciones discretas $\beta_{lm}$, $m=1,2,\dots$;
  cada una es un modo con $k_{Tlm}$, $\gamma_{lm}$ y $u_{lm}(r)$. $l$ caracteriza la distribución azimutal, $m$ la
  radial; $l=0$ ↔ rayos meridionales. Hay dos configuraciones independientes de $\mathbf{E}$, $\mathbf{H}$ por modo
  (dos polarizaciones).
- **Ecuación característica (fibra débilmente guiante)** (p. 334–335): $n_1\approx n_2$ ($\Delta\ll1$) → rayos
  paraxiales, componentes longitudinales mucho menores que las transversales, ondas aprox. TEM. Polarizaciones lineales
  en $x$ y $y$ son ortogonales. Modo $(l,m)$ linealmente polarizado: $\mathrm{LP}_{lm}$; sus dos polarizaciones tienen la
  misma $\beta$ y la misma distribución espacial. La ecuación característica equivale a exigir $u(r)$ y $u'(r)$
  continuas en $r=a$:
  $$\frac{(k_Ta)J_l'(k_Ta)}{J_l(k_Ta)} = \frac{(\gamma a)K_l'(\gamma a)}{K_l(\gamma a)}. \tag{9.2-11}$$
  Identidades:
  $$J_l'(x) = \pm J_{l\mp1}(x)\mp l\frac{J_l(x)}{x}, \tag{9.2-12}$$
  $$K_l'(x) = -K_{l\mp1}(x)\mp l\frac{K_l(x)}{x}. \tag{9.2-13}$$
  Con $X=k_Ta$, $Y=\gamma a$:
  $$\boxed{X\frac{J_{l\pm1}(X)}{J_l(X)} = \pm Y\frac{K_{l\pm1}(Y)}{K_l(Y)},\qquad Y=\sqrt{V^2-X^2}}\quad\text{(Characteristic Equation)} \tag{9.2-14}$$
  Dados $V$ y $l$, única incógnita $X$. Como $J_{-l}(x)=(-1)^lJ_l(x)$ y $K_{-l}=K_l$, la ecuación no cambia al sustituir
  $l\to-l$ (p. 335).
- Solución gráfica (p. 335–336, Fig. 9.2-3, caso $l=0$, $V=10$): el LHS tiene múltiples ramas; el RHS decrece
  monótonamente con $X$ y se anula en $X=V$ ($Y=0$). Intersecciones $X_{lm}$, $m=1,\dots,M_l$, en orden creciente;
  de ellas se obtienen $k_{Tlm}$, $\gamma_{lm}$, $\beta_{lm}$ y $u_{lm}(r)$. Análogo a Fig. 8.2-2.
- Ejemplos de distribuciones (p. 335–336): Fig. 9.2-2 corresponde a $\mathrm{LP}_{01}$ ($l=0,m=1$) con $V=5$ y
  $\mathrm{LP}_{34}$ con $V=25$. Superposición de $(l,m)$ y $(-l,m)$: amplitud $\propto u_{lm}(r)\cos l\phi\,e^{-j\beta_{lm}z}$,
  intensidad $\propto u_{lm}^2(r)\cos^2l\phi$ (Fig. 9.2-4). La distribución del $\mathrm{LP}_{01}$ es similar al haz
  gaussiano del cap. 3.
- **Corte de modos** (p. 336): el LHS de (9.2-14) no depende de $V$ y el RHS se desplaza a la derecha al crecer $V$.
  Con los signos menos, las ramas del LHS cortan la abscisa en $J_{l-1}(X)=0$, raíces $x_{lm}$. **Número de modos
  $M_l$ = número de raíces de $J_{l-1}(X)$ menores que $V$.** El modo $(l,m)$ está permitido si $V>x_{lm}$; corte en
  $V=x_{lm}$. Raíz más pequeña de $J_{-1}$: $x_{01}=0$ ($l=0$); siguiente $x_{11}=2.405$ ($l=1$).
- **Tabla 9.2-1** (p. 336), $V$ de corte de modos $\mathrm{LP}_{lm}$ de bajo orden (cortes de $l=0$ en las raíces de
  $J_{-1}(X)=-J_1(X)$; de $l=1$ en las raíces de $J_0(X)$):

  | $l\backslash m$ | 1 | 2 | 3 |
  |---|---|---|---|
  | 0 | 0 | 3.832 | 7.016 |
  | 1 | 2.405 | 5.520 | 8.654 |

- Para $V<2.405$ sólo sobrevive el fundamental $\mathrm{LP}_{01}$ (p. 336–337):
  $$\boxed{V<2.405}\quad\text{(Single-Mode Condition)} \tag{9.2-15}$$
  Frecuencia de corte (p. 337), ya que $V\propto\nu$:
  $$\boxed{\nu_c = \omega_c/2\pi = \frac{1}{\mathrm{NA}}\frac{c_o}{2.61a}}\quad\text{(Cutoff Frequency)} \tag{9.2-16}$$
  Comparación: guía plana de ancho $d$ (8.2-9): $\nu_c = (1/\mathrm{NA})(c_o/2d)$.
- **Número de modos** (p. 337): $M_l(V)$ es una escalera que sube en cada raíz $x_{lm}$ de $J_{l-1}$. Conteo total $M$
  vs $V$ en Fig. 9.2-5: cada raíz se cuenta dos veces para $l>0$ (modo $-l$, hélices de sentido opuesto) y otra vez por
  las dos polarizaciones. Para $V<2.405$ sólo $\mathrm{LP}_{01}$ con dos polarizaciones. Curva punteada:
  $M=4V^2/\pi^2+2$, aproximación para $V\gg1$.
- **Número de modos, $V$ grande** (p. 337–338): $J_l(X)\approx(2/\pi X)^{1/2}\cos[X-(l+\tfrac12)\tfrac\pi2]$ para
  $X\gg1$, raíces $x_{lm}\approx(l+\tfrac12)\tfrac\pi2+(2m-1)\tfrac\pi2 = (l+2m-\tfrac12)\tfrac\pi2$. Cortes
  (raíces de $J_{l\pm1}$):
  $$x_{lm}\approx\left(l+2m-\tfrac12\pm1\right)\frac\pi2\approx(l+2m)\frac\pi2,\qquad l=0,1,\dots;\ m\gg1. \tag{9.2-17}$$
  Para $l$ fijo las raíces se separan $\pi$ → $(l+2M_l)\tfrac\pi2=V$ → $M_l\approx V/\pi-l/2$; $M_l=0$ en
  $l_{\max}=2V/\pi$ (Fig. 9.2-6). $M=\sum_{l=0}^{l_{\max}}(V/\pi-l/2)\approx\tfrac12(2V/\pi)(V/\pi)=V^2/\pi^2$ (área
  del triángulo); multiplicando por 2 ($\pm l$) y 2 (polarizaciones):
  $$\boxed{M\approx\frac{4}{\pi^2}V^2}\quad\text{(Number of Modes, } V\gg1) \tag{9.2-18}$$
  Equivalente: $M\approx(4a/\lambda_o)^2(\mathrm{NA})^2$; comparar con guía rectangular (8.3-3)
  $M\approx(\pi/4)(2d/\lambda_o)^2(\mathrm{NA})^2$ (p. 338).
- **Ejemplo 9.2-1, Approximate Number of Modes** (p. 338): $n_1=1.452$, $\Delta=0.01$ → $\mathrm{NA}\approx
  n_1\sqrt{2\Delta}\approx0.205$. Con $\lambda_o=0.85$ μm y $a=25$ μm: $V=2\pi(a/\lambda_o)\mathrm{NA}\approx37.9$ →
  $M\approx4V^2/\pi^2\approx585$ modos. Sin revestimiento ($n_2=1$, NA $=1$): $V=184.8$, más de 13 800 modos.
- **Constantes de propagación, $V\gg1$** (p. 338–339): de (9.2-4a) y (9.2-8), $\beta_{lm}=(n_1^2k_o^2-X_{lm}^2/a^2)^{1/2}$.
  Aproximación más cruda: $X_{lm}\approx x_{lm}$ (ramas del LHS verticales). Con (9.2-17):
  $$\beta_{lm}\approx\sqrt{n_1^2k_o^2-(l+2m)^2\frac{\pi^2}{4a^2}}. \tag{9.2-19}$$
  Como
  $$M\approx\frac4{\pi^2}V^2=\frac4{\pi^2}(\mathrm{NA})^2a^2k_o^2\approx\frac4{\pi^2}(2n_1^2\Delta)k_o^2a^2, \tag{9.2-20}$$
  $$\beta_{lm}\approx n_1k_o\sqrt{1-2\frac{(l+2m)^2}{M}\Delta}, \tag{9.2-21}$$
  y con $\sqrt{1+\delta}\approx1+\delta/2$:
  $$\boxed{\beta_{lm}\approx n_1k_o\left[1-\frac{(l+2m)^2}{M}\Delta\right]}\quad\text{(Propagation Constants, } V\gg1;\ l=0,1,\dots,\sqrt M;\ m=1,2,\dots,\tfrac12(\sqrt M-l)) \tag{9.2-22}$$
  $l+2m$ varía entre 2 y $\approx2V/\pi=\sqrt M$, así que $\beta_{lm}$ varía entre $n_1k_o$ y $n_1k_o(1-\Delta)\approx n_2k_o$
  (Fig. 9.2-7, p. 339).
- **Velocidades de grupo, $V\gg1$** (p. 339–340): $v_{lm}=d\omega/d\beta_{lm}$; se sustituye $n_1k_o=\omega/c_1$ y
  $M=(4/\pi^2)(2n_1^2\Delta)a^2\omega^2/c_o^2=(8/\pi^2)a^2\omega^2\Delta/c_1^2$ en (9.2-22), con $c_1$ y $\Delta$
  independientes de $\omega$:
  $$v_{lm}\approx c_1\left[1+\frac{(l+2m)^2}{M}\Delta\right]^{-1}, \tag{9.2-23}$$
  $$\boxed{v_{lm}\approx c_1\left[1-\frac{(l+2m)^2}{M}\Delta\right]}\quad\text{(Group Velocities, } V\gg1) \tag{9.2-24}$$
  Varía entre $c_1$ y $c_1(1-\Delta)=c_1(n_2/n_1)$: los modos de bajo orden viajan aprox. a la velocidad de fase del
  núcleo; los de alto orden más lento. El cambio fraccional de velocidad de grupo entre el modo más rápido y el más lento
  es $\approx\Delta$. Fibras con $\Delta$ grande (NA grande): muchos modos, gran dispersión modal, alto ensanchamiento;
  peor aún sin revestimiento (p. 340).

#### 9.2B Single-Mode Fibers (p. 340)

- Operación monomodo en $\mathrm{LP}_{01}$ si $V=2\pi(a/\lambda_o)\mathrm{NA}<2.405$: núcleo pequeño y NA pequeña
  ($n_2$ cercano a $n_1$), o frecuencia por debajo de $\nu_c=(1/\mathrm{NA})(c_o/2.61a)$. El modo fundamental tiene
  distribución acampanada similar a la gaussiana (Fig. 9.2-2 con $l=0$; Fig. 9.2-4(a)) y da el máximo confinamiento
  (p. 340).
- **Ejemplo 9.2-2, Single-Mode Operation** (p. 340): $n_1=1.447$, $\Delta=0.01$ (NA $=0.205$), $\lambda_o=1.3$ μm →
  monomodo si $2a<4.86$ μm. Si $\Delta=0.0025$, monomodo hasta $2a<9.72$ μm.
- **Índice efectivo** $n=\beta/k_o$ del modo fundamental vs $V$: Fig. 9.2-8(a) (p. 341) muestra $(n-n_2)/(n_1-n_2)$
  creciendo de 0 a 1 con $V$ (de 0 a 10); Fig. 9.2-8(b): relación de dispersión $\omega$ vs $\beta_{01}$ entre las
  líneas de luz $\omega=c_2\beta$ y $\omega=c_1\beta$. Al crecer $V$ (frecuencia o diámetro) el índice efectivo sube de
  $n_2$ a $n_1$: el modo se confina más en el núcleo a longitudes de onda cortas (p. 340).
- Ventajas de la SMF (p. 340–341): sin dispersión modal (sólo otros mecanismos, mucho menores, §9.3B); menor atenuación
  que las MMF (§9.3A); mayores tasas de datos (caps. 22 y 24). Las MMF sufren además **ruido modal** o **speckle**:
  interferencia aleatoria entre modos por imperfecciones, tensiones y temperatura, análogo al *fading* multitrayecto en
  radio; en SMF sólo hay un camino y no hay ruido modal (p. 341).
- **Fibras que mantienen la polarización** (p. 341–342): en fibra de sección circular el $\mathrm{LP}_{01}$ tiene dos
  polarizaciones ($x$, $y$) degeneradas (misma $\beta$ y misma velocidad de grupo). Imperfecciones y tensiones aleatorias
  transfieren potencia entre ellas, facilitado porque las fases están emparejadas; luz lineal a la entrada sale elíptica
  con elipticidad fluctuante (Fig. 9.2-9). No importa si sólo se transmite potencia total, pero sí en óptica integrada,
  sensores interferométricos y comunicaciones coherentes. Solución: romper la simetría circular (sección elíptica o
  anisotropía inducida por tensión) para eliminar la degeneración y desemparejar las fases, reduciendo el acoplamiento.

#### *9.2C Quasi-Plane Waves in Step- and Graded-Index Fibers (p. 342)

- Método WKB (Wentzel–Kramers–Brillouin), válido para fibras con muchos modos ($V$ grande): el campo se representa como
  **onda cuasi-plana** (localmente plana, dirección y amplitud varían lentamente) que viaja a lo largo de la trayectoria
  del rayo; se conserva la fase y se aplica la condición de autoconsistencia como en §8.2 (p. 342).
- **Ondas cuasi-planas** (p. 342–343): solución de (9.2-1) de la forma (ver §2.3)
  $$U(\mathbf r) = a(\mathbf r)\exp[-jk_oS(\mathbf r)], \tag{9.2-25}$$
  $a$, $S$ reales de variación lenta; $S$ cumple la ecuación eikonal $|\nabla S|^2\approx n^2$ (2.3-4), rayos en la
  dirección $\nabla S$. Con $k_oS(\mathbf r)=k_os(r)+l\phi+\beta z$:
  $$\left(k_o\frac{ds}{dr}\right)^2+\beta^2+\frac{l^2}{r^2} = n^2(r)k_o^2. \tag{9.2-26}$$
  Frecuencia espacial radial local:
  $$k_r = k_o\frac{ds}{dr}, \tag{9.2-27}$$
  $$\boxed{U(r) = a(r)\exp\!\left(-j\int_0^r k_r\,dr\right)e^{-jl\phi}e^{-j\beta z}}\quad\text{(Quasi-Plane Wave)} \tag{9.2-28}$$
  $$\boxed{k_r^2 = n^2(r)k_o^2-\beta^2-\frac{l^2}{r^2}} \tag{9.2-29}$$
  Con $k_\phi=l/r$ y $k_z=\beta$: $k_r^2+k_\phi^2+k_z^2=n^2(r)k_o^2$; vector de onda local $\mathbf k=(k_r,k_\phi,k_z)$ de
  módulo $n(r)k_o$, cuya dirección cambia lentamente con $r$ siguiendo una hélice (Fig. 9.2-10) (p. 343).
- Región de confinamiento (p. 343–344): donde $k_r$ es real ($k_r^2>0$). Construcción gráfica Fig. 9.2-11: se traza
  $n^2(r)k_o^2$, se resta $l^2/r^2$ (curva punteada) y se marca $\beta^2$; $k_r^2$ = diferencia (área sombreada).
  Fibra escalonada: confinamiento en $r_l<r<a$, con
  $$n_1^2k_o^2-\frac{l^2}{r_l^2}-\beta^2 = 0; \tag{9.2-30}$$
  la onda rebota helicoidalmente como el rayo oblicuo de Fig. 9.1-2; en $r>a$ y $r<r_l$, $k_r$ es imaginario y el campo
  decae. $r_l$ depende de $\beta$; para $\beta$ (o $l$) grande, $r_l$ es grande y la onda se confina en una corona
  delgada junto a la frontera. Fibra GRIN: $k_r$ real en $r_l<r<R_l$, raíces de
  $$n^2(r)k_o^2-\frac{l^2}{r^2}-\beta^2 = 0, \tag{9.2-31}$$
  corona cilíndrica como en Fig. 9.1-6(b).
- **Modos (condición de autoconsistencia)** (p. 344): recorrido azimutal $k_\phi2\pi r=2\pi l$ (se cumple con
  $k_\phi=l/r$); recorrido radial de ida y vuelta con fase múltiplo de $2\pi$:
  $$2\int_{r_l}^{R_l}k_r\,dr = 2\pi m,\qquad m=1,2,\dots,M_l, \tag{9.2-32}$$
  con $R_l=a$ en fibra escalonada. Análoga a (8.2-2); de ella salen los $\beta_{lm}$ (Fig. 9.2-12, p. 345, curvas para
  $l=0..6$ con los radios $r_l$, $R_l$). $m=1$ tiene $\beta$ máxima ($\approx n_1k_o$), $m=M_l$ mínima ($\approx n_2k_o$).
- **Número de modos** (p. 345–346): número de modos con constante de propagación mayor que $\beta$:
  $$M_l(\beta) = \frac1\pi\int_{r_l}^{R_l}k_r\,dr = \frac1\pi\int_{r_l}^{R_l}\sqrt{n^2(r)k_o^2-\frac{l^2}{r^2}-\beta^2}\,dr, \tag{9.2-33}$$
  $$q_\beta = 4\sum_{l=0}^{l_{\max}(\beta)}M_l(\beta), \tag{9.2-34}$$
  ($l_{\max}(\beta)$: máximo $l$ con modo ligado de $\beta$ mayor que la dada; factor 4 por polarizaciones y hélices $\pm$;
  total $M=q_\beta$ en $\beta=n_2k_o$)
  $$q_\beta\approx4\int_0^{l_{\max}(\beta)}M_l(\beta)\,dl. \tag{9.2-35}$$
  Para perfil de ley de potencias (9.1-4):
  $$q_\beta\approx M\left[\frac{1-(\beta/n_1k_o)^2}{2\Delta}\right]^{\frac{p+2}{p}}, \tag{9.2-36}$$
  $$M\approx\frac{p}{p+2}n_1^2k_o^2a^2\Delta = \frac{p}{p+2}\frac{V^2}{2}, \tag{9.2-37}$$
  con $\Delta=(n_1-n_2)/n_1$ y $V=2\pi(a/\lambda_o)\mathrm{NA}$. Para escalonada ($p\to\infty$):
  $$q_\beta\approx M\left[\frac{1-(\beta/n_1k_o)^2}{2\Delta}\right], \tag{9.2-38}$$
  $$\boxed{M\approx\frac12V^2}\quad\text{(Number of Modes, Step-Index)} \tag{9.2-39}$$
  Casi igual a (9.2-18): $4V^2/\pi^2\approx0.41V^2$ (p. 346).
- **Constantes de propagación** (p. 346): invirtiendo (9.2-36) con $q_\beta\to q$:
  $$\beta_q\approx n_1k_o\sqrt{1-2\left(\frac qM\right)^{p/(p+2)}\Delta},\qquad q=1,2,\dots,M, \tag{9.2-40}$$
  $$\boxed{\beta_q\approx n_1k_o\left[1-\left(\frac qM\right)^{p/(p+2)}\Delta\right]}\quad\text{(Propagation Constants)} \tag{9.2-41}$$
  decrece de $\approx n_1k_o$ ($q=1$) a $n_2k_o$ ($q=M$) (Fig. 9.2-13, p. 347). Escalonada:
  $$\boxed{\beta_q\approx n_1k_o\left(1-\frac qM\Delta\right)}\quad\text{(Propagation Constants, Step-Index)} \tag{9.2-42}$$
  idéntica a (9.2-22) si $q\to(l+2m)^2$.
- **Velocidades de grupo** (p. 347): sustituyendo (9.2-37) en (9.2-41), $n_1k_o=\omega/c_1$, $(1+\delta)^{-1}\approx1-\delta$,
  $c_1$ y $\Delta$ independientes de $\omega$ (sin dispersión de material):
  $$\boxed{v_q\approx c_1\left[1-\frac{p-2}{p+2}\left(\frac qM\right)^{p/(p+2)}\Delta\right]}\quad\text{(Group Velocities)} \tag{9.2-43}$$
  Escalonada:
  $$v_q\approx c_1\left(1-\frac qM\Delta\right), \tag{9.2-44}$$
  reproduce (9.2-24); varía de $c_1$ a $c_1(1-\Delta)$ (Fig. 9.2-14(a)).
- **Perfil óptimo** (p. 347–348): (9.2-43) da $v_q\approx c_1$ para todo $q$ si $p=2$ → todos los modos a la misma
  velocidad; ventaja de la GRIN para multimodo. Con un término más en Taylor
  ($\sqrt{1+\delta}\approx1+\tfrac12\delta-\tfrac18\delta^2$) para $p=2$:
  $$\boxed{v_q\approx c_1\left(1-\frac qM\frac{\Delta^2}{2}\right)}\quad\text{(Group Velocities, Graded-Index, } p=2) \tag{9.2-45}$$
  Varía de $c_1$ a $c_1(1-\Delta^2/2)$ (Fig. 9.2-14(b), p. 348): diferencia $\Delta^2/2$ frente a $\Delta$ en escalonada,
  es decir, reducción por factor $\Delta/2$ (estimación burda; no se alcanza en la práctica).
- Número de modos GRIN con $p=2$, de (9.2-37):
  $$\boxed{M\approx\frac14V^2}\quad\text{(Number of Modes, Graded-Index, } p=2) \tag{9.2-46}$$
  la mitad que en la escalonada con los mismos $n_1$, $n_2$, $a$ (p. 348).

### 9.3 Attenuation and Dispersion (p. 348)

- La atenuación (pérdidas) limita la potencia transmitida; la dispersión (ensanchamiento temporal) limita la tasa de
  pulsos (p. 348).

#### 9.3A Attenuation (p. 348)

- **Coeficiente de atenuación** (p. 348): la potencia decrece exponencialmente por absorción y dispersión (scattering);
  se define en dB/km:
  $$\alpha = \frac1L10\log_{10}\frac1{\mathcal T}, \tag{9.3-1}$$
  $\mathcal T=P(L)/P(0)$ razón de transmisión de potencia para longitud $L$ km. Fig. 9.3-1 (p. 349): 3 dB ↔
  $\mathcal T=0.5$; 10 dB ↔ 0.1; 20 dB ↔ 0.01. Ej.: 3 dB/km ↔ $\mathcal T=0.5$ en 1 km. En cascada las razones se
  multiplican y los dB se suman. Para $z$ km la pérdida es $\alpha z$ dB:
  $$\frac{P(z)}{P(0)} = 10^{-\alpha z/10}\approx e^{-0.23\alpha z},\qquad\alpha\text{ en dB/km}. \tag{9.3-2}$$
  Si $\alpha$ se da en km⁻¹:
  $$P(z)/P(0) = e^{-\alpha z},\qquad\alpha\text{ en km}^{-1}, \tag{9.3-3}$$
  con $\alpha[\text{km}^{-1}]\approx0.23\,\alpha[\text{dB/km}]$. Para componentes distintos de fibras se suele dar
  $\alpha$ en cm⁻¹ con $z$ en cm (p. 349).
- **Absorción** (p. 349): sílice fundida tiene dos bandas fuertes: infrarrojo medio (transiciones vibracionales) y
  ultravioleta (transiciones electrónicas y moleculares); sus colas dejan una ventana en el IR cercano con poca
  absorción intrínseca (Fig. 9.3-2).
- **Dispersión de Rayleigh** (p. 349–350): variaciones aleatorias locales de la posición molecular en el vidrio →
  inhomogeneidades de índice que actúan como centros dispersores. Amplitud dispersada $\propto\omega^2$ (la densidad de
  polarización $\mathcal P$ radia $\propto d^2\mathcal P/dt^2=-\omega^2\mathcal P$, (5.2-25)); intensidad $\propto\omega^4$
  o $1/\lambda_o^4$: **ley inversa de la cuarta potencia de Rayleigh** (azul se dispersa más que rojo; cielo azul).
  En el visible domina sobre la cola UV; es despreciable frente a la absorción IR para $\lambda>1.6$ μm. La ventana
  transparente está acotada por Rayleigh (cortas) y absorción IR (largas) (p. 350).
- **Fig. 9.3-2** (p. 350): $\alpha$ de sílice vs $\lambda_o$ (0.6–1.8 μm), con Rayleigh, cola UV, pico OH (~1.39 μm) y
  absorción IR. **Mínimo local en 1.3 μm ($\alpha\approx0.3$ dB/km) y mínimo absoluto en 1.55 μm
  ($\alpha\approx0.15$ dB/km).**
- **Efectos extrínsecos** (p. 350): impurezas, sobre todo iones metálicos y radicales OH (vapor de agua); los metales se
  eliminan fácilmente, el OH es más difícil (hay fibras con OH suprimido). Los dopantes para gradar el índice aumentan la
  dispersión de luz. La atenuación depende del modo (distinta penetración en el revestimiento; mayor para modos de alto
  orden), por lo que las SMF tienen menos atenuación que las MMF (Fig. 9.3-3, p. 351: rangos de $\alpha$ para SMF y MMF).
  También hay pérdidas por variaciones geométricas y curvaturas.
- **Alternativas a la sílice** (p. 350–351): vidrios de fluoruros de metales pesados, germanatos de metales pesados,
  calcogenuros; banda IR más lejana → operación a $\lambda$ mayor con menos Rayleigh. Predicción para fluoruros:
  ~10 veces menos pérdida que la sílice, mínimo $\approx0.01$ dB/km en $\lambda_o\approx2.5$ μm; pero dominan pérdidas
  extrínsecas, son menos durables y faltan fotodetectores eficientes en el IR medio (los láseres de cascada cuántica
  sí operan a temperatura ambiente).

#### 9.3B Dispersion (p. 351)

Cinco fuentes principales de dispersión (p. 351): **modal**, **de material**, **de guía de onda**, **de modo de
polarización** y **no lineal**. Sus contribuciones no son necesariamente aditivas.

- **Dispersión modal** (p. 351–352): un impulso en fibra de $M$ modos se reparte en $M$ pulsos con retardos
  $\tau_q=L/v_q$, $q=1,\dots,M$. Ensanchamiento $L/v_{\min}-L/v_{\max}$; envolvente suave (Fig. 9.3-4). Estimación con
  envolvente triangular y FWHM: $\sigma_\tau=\tfrac12(L/v_{\min}-L/v_{\max})$ = tiempo de respuesta por dispersión modal.
  Escalonada con muchos modos: $v_{\min}\approx c_1(1-\Delta)$, $v_{\max}\approx c_1$, $(1-\Delta)^{-1}\approx1+\Delta$:
  $$\boxed{\sigma_\tau\approx\frac L{c_1}\cdot\frac\Delta2}\quad\text{(Response Time, Multimode Step-Index)} \tag{9.3-4}$$
  GRIN óptima con muchos modos ($v_{\min}\approx c_1(1-\Delta^2/2)$):
  $$\boxed{\sigma_\tau\approx\frac L{c_1}\cdot\frac{\Delta^2}4}\quad\text{(Response Time, Graded-Index)} \tag{9.3-5}$$
  (factor $\Delta/2$ menor que en escalonada.)
- **Ejemplo 9.3-1, Multimode Pulse Broadening Rate** (p. 352): escalonada con $\Delta=0.01$ y $n=1.46$:
  $\sigma_\tau/L\approx\Delta/2c_1=n_1\Delta/2c_o\approx24$ ns/km; en 100 km el impulso se ensancha a $\approx2.4$ μs.
  Con gradación óptima: $n_1\Delta^2/4c_o\approx122$ ps/km.
- Acoplamiento modal (p. 352): el ensanchamiento modal es $\propto L$, pero por acoplamiento entre modos de $\beta$
  cercanas (irregularidades, inhomogeneidades) a partir de una longitud crítica pasa a ser $\propto\sqrt L$ (nota:
  Midwinter, *Optical Fibers for Transmission*, Wiley 1979).
- **Dispersión de material** (p. 352–353): el vidrio es dispersivo, $n=n(\lambda)$; un pulso viaja con velocidad de grupo
  $v=c_o/N$, $N=n-\lambda_o\,dn/d\lambda_o$ (índice de grupo, §5.6). El pulso es un paquete de componentes de distinta
  $\lambda$ con distinta $v$. Para anchura espectral $\sigma_\lambda$ (nm) y distancia $L$:
  $\sigma_\tau=|(d/d\lambda_o)(L/v)|\sigma_\lambda=|(d/d\lambda_o)(LN/c_o)|\sigma_\lambda$ [(5.6-2), (5.6-7), (5.6-8)]:
  $$\boxed{\sigma_\tau = |D_\lambda|\sigma_\lambda L}\quad\text{(Response Time, Material Dispersion)} \tag{9.3-6}$$
  $$D_\lambda = -\frac{\lambda_o}{c_o}\frac{d^2n}{d\lambda_o^2}. \tag{9.3-7}$$
  Unidades habituales: $L$ en km, $\sigma_\tau$ en ps, $\sigma_\lambda$ en nm → $D_\lambda$ en ps/km·nm.
- **Fig. 9.3-5** (p. 353): $D_\lambda$ de fibra de sílice vs $\lambda_o$ (0.6–1.6 μm), de −200 a +40 ps/km·nm (similar
  pero distinta de la sílice fundida de Fig. 5.6-5). Para $\lambda_o<1.3$ μm, $D_\lambda<0$ (**dispersión normal**: los
  paquetes de $\lambda$ larga viajan más rápido que los de corta); $D_\lambda\approx-80$ ps/km·nm en 0.87 μm;
  $D_\lambda\approx+17$ ps/km·nm en 1.55 μm (**dispersión anómala**); **$D_\lambda=0$ en $\lambda_o\approx1.312$ μm**
  (allí $\sigma_\tau$ de (9.3-6) se anula; una expresión más precisa que incluya la dispersión de $\sigma_\lambda$ en
  torno a 1.312 μm da un ancho pequeño pero no nulo).
- **Ejemplo 9.3-2, Pulse Broadening Associated with Material Dispersion** (p. 353–354): $D_\lambda\approx-80$ ps/km·nm
  en 0.87 μm; fuente LED con $\sigma_\lambda=50$ nm → tasa de ensanchamiento $|D_\lambda|\sigma_\lambda=4$ ns/km; en
  $L=100$ km, $\sigma_\tau=0.4$ μs. Diodo láser con $\sigma_\lambda=2$ nm cerca de 1.3 μm donde $D_\lambda=1$ ps/km·nm →
  2 ps/km; en 100 km, $\sigma_\tau=0.2$ ns.
- **Dispersión modal + de material** (p. 354): se regresa a $\beta_q$ con $n_1$, $n_2$ funciones de $\omega$ y
  $v_q=(d\beta_q/d\omega)^{-1}$. Para GRIN con muchos modos ((9.2-41), (9.2-37)), suponiendo $\Delta$ independiente de
  $\omega$:
  $$v_q\approx\frac{c_o}{N_1}\left[1-\frac{p-2}{p+2}\left(\frac qM\right)^{p/(p+2)}\Delta\right], \tag{9.3-8}$$
  $N_1=(d/d\omega)(\omega n_1)=n_1-\lambda_o(dn_1/d\lambda_o)$ índice de grupo del núcleo: (9.2-43) con $n_1\to N_1$.
  Escalonada: $v_q$ de $c_o/N_1$ a $(c_o/N_1)(1-\Delta)$:
  $$\boxed{\sigma_\tau\approx\frac{L}{(c_o/N_1)}\cdot\frac\Delta2}\quad\text{(Response Time, Multimode Step-Index, Material Dispersion)} \tag{9.3-9}$$
  (comparar con (9.3-4) sin dispersión de material.)
- **Ejercicio 9.3-1, Optimal Grade Profile Parameter** (p. 354): usar (9.2-41) y (9.2-37) para deducir, con $n_1$ y
  $\Delta$ dependientes de $\lambda$,
  $$v_q\approx\frac{c_o}{N_1}\left[1-\frac{p-2-p_s}{p+2}\left(\frac qM\right)^{p/(p+2)}\Delta\right],\qquad q=1,\dots,M, \tag{9.3-10}$$
  con $p_s=2(n_1/N_1)(\omega/\Delta)\,d\Delta/d\omega$. ¿Cuál es el $p$ óptimo que minimiza la dispersión modal?
  (Por inspección de (9.3-10): $p=2+p_s$.)
- **Dispersión de guía de onda** (p. 354–355): las velocidades de grupo dependen de $\lambda$ aun sin dispersión de
  material, porque la distribución del campo depende de $a/\lambda_o$: cambian las fracciones de potencia en núcleo y
  revestimiento, de velocidades de fase distintas. Importante en SMF (sin dispersión modal) y donde la de material es
  pequeña (cerca de 1.3 μm en sílice), pues entonces domina. Con $V=2\pi(a/\lambda_o)\mathrm{NA}=(a\cdot\mathrm{NA}/c_o)\omega$
  y NA independiente de $\omega$:
  $$\frac1v=\frac{d\beta}{d\omega}=\frac{d\beta}{dV}\frac{dV}{d\omega}=\frac{a\cdot\mathrm{NA}}{c_o}\frac{d\beta}{dV}. \tag{9.3-11}$$
  $$\sigma_\tau = |D_w|\sigma_\lambda L, \tag{9.3-12}$$
  $$D_w = \frac{d}{d\lambda_o}\left(\frac1v\right) = -\frac{\omega}{\lambda_o}\frac{d}{d\omega}\left(\frac1v\right). \tag{9.3-13}$$
  $$D_w = -\left(\frac1{2\pi c_o}\right)V^2\frac{d^2\beta}{dV^2}. \tag{9.3-14}$$
  $D_w\propto V^2d^2\beta/dV^2$; como $\beta(V)$ es no lineal (Fig. 9.2-8(a)), $D_w$ depende de $V$ y por tanto de
  $\lambda$; se controla con el radio del núcleo o el perfil de gradación (nota al pie: artículos de Gloge).
- **Dispersión de material + de guía = dispersión cromática** (p. 355–356): se obtiene incluyendo $n_1(\lambda)$,
  $n_2(\lambda)$ y NA$(\lambda)$ al calcular $d\beta/d\omega$ de la ecuación característica. La de guía, aunque menor,
  desplaza la $\lambda$ de dispersión cromática total mínima. **Fibras de dispersión desplazada (DSF)**: núcleo de índice
  gradado linealmente (perfil triangular) y radio reducido, mueven el cero de dispersión cromática de 1.3 μm a 1.55 μm,
  donde la atenuación es mínima (Fig. 9.3-6(a)). **Fibras de dispersión aplanada (DFF)**: gradación cuádruple en capas
  (quadruple-clad), dispersión nula en dos longitudes de onda y reducida entre ellas (Fig. 9.3-6(b)); el dopado introduce
  pérdidas. **Fibras compensadoras de dispersión (DCF)**: dispersión combinada de magnitud proporcional y signo opuesto
  a la de la fibra convencional en una banda amplia (Fig. 9.3-6(c)); un tramo corto de DCF compensa un tramo largo
  convencional.
- **Dispersión de modo de polarización (PMD)** (p. 356–358): las dos polarizaciones del $\mathrm{LP}_{01}$ son
  degeneradas sólo con simetría circular perfecta y material isótropo; en condiciones reales hay birrefringencia pequeña
  que varía aleatoriamente a lo largo (índices, elipticidad). Modelo simple: medio anisótropo homogéneo con ejes
  principales $x$, $y$, índices $n_x$, $n_y$ (dispersivos), ejes independientes de la frecuencia. Retardos de grupo
  $\tau_x=N_xL/c_o$, $\tau_y=N_yL/c_o$ ($N_x$, $N_y$ índices de grupo, §5.6). Pulso con ambas polarizaciones: **retardo
  de grupo diferencial (DGD)** $\delta\tau=|\tau_y-\tau_x|$:
  $$\boxed{\delta\tau = \Delta N\,L/c_o}\quad\text{(Differential Group Delay)} \tag{9.3-15}$$
  $\Delta N=|N_y-N_x|$. El pulso se divide en dos componentes ortogonales separadas en el tiempo (Fig. 9.3-7); PMD crece
  linealmente con $L$ a tasa $\Delta N/c_o$ (ps/km).
  Modelo realista (p. 357): secuencia de segmentos homogéneos cortos con ejes rotados; matriz de Jones $2\times2$
  $\mathbf T$ producto de las individuales (§6.1B); modos de polarización = autovectores (no necesariamente lineales);
  sin pérdidas, $\mathbf T$ unitaria con autovalores $e^{j\varphi_1}$, $e^{j\varphi_2}$ = $e^{jn_1k_oL}$, $e^{jn_2k_oL}$
  ($n_1$, $n_2$ índices efectivos de los dos modos de polarización). Con dispersión, $\mathbf T$, $n_1$, $n_2$ y los
  índices de grupo $N_1$, $N_2$ dependen de $\omega$; un pulso con componentes en ambos modos sufre DGD (9.3-15) con
  $\Delta N=|N_1-N_2|$ (p. 358).
  Modelo estadístico de variaciones aleatorias de magnitud y orientación de la birrefringencia: RMS del ensanchamiento
  $\propto\sqrt L$:
  $$\boxed{\sigma_{\rm PMD} = D_{\rm PMD}\sqrt L}\quad\text{(Polarization-Mode Dispersion)} \tag{9.3-16}$$
  $D_{\rm PMD}$ típicamente de 0.1 a 1 ps/√km (p. 358). Efectos de orden superior: GVD de cada modo de polarización
  (segunda derivada de su índice, §5.6); dependencia de los autovectores con la frecuencia (para pulsos ultracortos se
  requiere análisis combinado polarización–espectro; existen estados con retardo insensible a la frecuencia, GVD mínima,
  pero no son autovectores de la Jones: entrada y salida difieren; ref. Poole y Wagner, *Electron. Lett.* 22, 1029, 1986).
- **Ejercicio 9.3-2, Differential Group Delay in a Two-Segment Fiber** (p. 358, Fig. 9.3-8): fibra de 1 km con dos
  segmentos iguales, cada uno anisótropo monomodo con índices de grupo principales $N_x=1.462$, $N_y=1.463$ y
  $D_x=D_y=20$ ps/km·nm; ejes de un segmento a 45° respecto al otro. (a) Pulso de entrada de 100 ps, lineal a 45° de
  $x$ y $y$, ancho espectral 50 nm: bosquejar el perfil temporal de salida. (b) Determinar los modos de polarización de
  la fibra completa y el perfil temporal de salida si la entrada está en uno de ellos.
- **Dispersión no lineal** (p. 359): a alta intensidad el índice depende de la intensidad; las porciones de alta
  intensidad del pulso sufren corrimientos de fase distintos de las de baja → frecuencias instantáneas desplazadas:
  **automodulación de fase (SPM)**. Bajo ciertas condiciones la SPM compensa la GVD de material y el pulso viaja sin
  alterar su perfil: **solitón**. Óptica no lineal en cap. 21, solitones en cap. 22.
- **Resumen (recuadro, p. 359)**: la propagación de pulsos está gobernada por atenuación y varios tipos de dispersión
  (Fig. 9.3-9, p. 360: (a) MMF dispersión modal, (b) SMF dispersión material+guía, (c) SMF con PMD, (d) SMF no lineal
  con solitón que conserva $\tau_0$).
  - MMF: domina la dispersión modal; ancho dado por la disparidad de retardos de grupo de los modos.
  - SMF: sin dispersión modal; limitada por dispersión cromática (material + guía); ancho de salida gobernado por la GVD.
  - La de material suele ser mucho mayor que la de guía; donde la de material es pequeña, la de guía importa; perfiles
    especiales → fibras aplanadas, desplazadas y compensadoras.
  - En SMF largas con dispersión cromática despreciable domina la PMD: cambios anisótropos pequeños hacen que el pulso
    viaje en dos modos de polarización con índices de grupo distintos (DGD).
  - Un pulso intenso (solitón) puede hacer la fibra no lineal y viajar sin ensancharse: balance entre dispersión de
    material y SPM (cap. 22).

### 9.4 Holey and Photonic-Crystal Fibers (p. 359)

- **Fibra agujereada (holey fiber)** (p. 359–360): sílice pura con múltiples agujeros de aire cilíndricos paralelos al
  eje, en patrón periódico; el núcleo es un **defecto** (agujero faltante, de distinto tamaño o extra). Parámetros:
  separación entre centros $\Lambda$ (**pitch**, típicamente 1–10 μm) y diámetro $d$. No se requieren dopantes.
  Fig. 9.4-1: (a) núcleo sólido con revestimiento de agujeros mucho menores que $\lambda$; (b) PCF con agujeros grandes
  y núcleo sólido; (c) PCF con núcleo que es un agujero de distinto tamaño. Dos mecanismos de guiado: **índice
  efectivo** y **banda fotónica prohibida** (p. 360).
- **Guiado por índice efectivo** (p. 361): si $d\ll\lambda$ el revestimiento periódico se comporta como medio homogéneo
  con **índice efectivo** $n_2$ = promedio; guiado por reflexión total con núcleo sólido $n_1>n_2$; los agujeros actúan
  como "dopantes negativos" distribuidos (pueden ser aleatorios y no continuos axialmente). Si $d$ no es $\ll\lambda$,
  el revestimiento es un medio periódico 2D; $n_2$ es el promedio ponderado por la intensidad, fuertemente dependiente
  de $\lambda$ y de la geometría: las ondas más cortas se confinan más en el medio de mayor índice → $n_2(\lambda)$
  decreciente con $\lambda$ (análogo al cristal fotónico 1D, Fig. 7.2-6) → fuerte **dispersión de guía de onda**, muy
  útil.
  - **Monomodo sin fin (endless single-mode guidance)**: $V=(2\pi a/\lambda)\sqrt{n_1^2-n_2^2(\lambda)}$ aprox.
    independiente de $\lambda$ cuando $\sqrt{n_1^2-n_2^2(\lambda)}\propto\lambda$; la fibra puede ser monomodo desde
    el IR hasta el UV (ref. Birks, Knight, Russell, *Opt. Lett.* 22, 961, 1997). En fibra convencional $V\propto1/\lambda$
    y al bajar $\lambda$ pasa a multimodo ($V>2.405$).
  - **Gran área modal (LMA)** monomodo: útil para alta potencia. En convencional, $V<2.405$ con $2a$ grande exige NA
    pequeña; en agujereadas, $\Lambda$ grande (núcleo mayor) y $d$ pequeño (menor NA, campo penetra más); áreas modales
    varios órdenes de magnitud mayores que en fibras convencionales.
- **Guiado por banda fotónica prohibida** (p. 361–362): el revestimiento es un **cristal fotónico** 2D (p. ej.
  microestructura triangular de Fig. 9.4-1(b)) con diagrama de dispersión con bandas prohibidas (Fig. 7.3-3, §7.3A);
  si la frecuencia cae en la banda prohibida, la propagación en el revestimiento está prohibida y la fibra es una guía de
  cristal fotónico (§8.5). **Fibra de cristal fotónico (PCF)**: núcleo sólido o hueco (Fig. 9.4-1(b),(c)). El núcleo
  hueco no puede guiar por índice efectivo (no hay reflexión total); la PCF de núcleo de aire tiene menores pérdidas,
  menores efectos no lineales y transporta más potencia. Permiten: aplanamiento de dispersión en bandas amplias,
  desplazamiento de dispersión a $\lambda$ menores que el cero de dispersión del material, láseres de fibra de banda
  ancha, análisis de gases introducidos en el núcleo (p. 362).

### Reading List (p. 362–363)

Libros (selección): DeCusatis, *Fiber Optic Essentials* (2005); Hecht, *Understanding Fiber Optics* (5.ª ed., 2005);
Zolla et al., *Foundations of Photonic Crystal Fibres* (2005); Galtarossa & Menyuk, *Polarization Mode Dispersion* (2005);
Buck, *Fundamentals of Optical Fibers* (2.ª ed., 2004); Bjarklev, Broeng & Bjarklev, *Photonic Crystal Fibers* (2003);
Kaminow & Li, *Optical Fiber Telecommunications IVA* (2002); Othonos & Kalli, *Fiber Bragg Gratings* (1999); Ghatak &
Thyagarajan, *An Introduction to Fiber Optics* (1998); Sanghera & Aggarwal, *Infrared Fiber Optics* (1998); Dyott,
*Elliptical Fiber Waveguides* (1995); Midwinter, *Optical Fibers for Transmission* (1979/1992); Marcuse, *Light
Transmission Optics* (1982) y *Principles of Optical Fiber Measurements* (1981); Kao, *Optical Fiber Systems* (1982).
Artículos: Bayindir et al., *IEEE JSTQE* 12, 1202 (2006); Russell, *Photonic Crystal Fibers*, *Science* 299, 358 (2003);
Gordon & Kogelnik, PMD fundamentals, *PNAS* 97, 4541 (2000); Birks, Knight & Russell, Endlessly single-mode PCF, *Opt.
Lett.* 22, 961 (1997); Clarricoats, Optical fibre waveguides — a review, *Progress in Optics* 14 (1977); **Gloge, Weakly
Guiding Fibers, *Appl. Opt.* 10, 2252 (1971)** y **Gloge, Dispersion in Weakly Guiding Fibers, *Appl. Opt.* 10, 2442
(1971)**.

## Tablas y datos numéricos útiles

| Magnitud | Valor | Página |
|---|---|---|
| Pérdida mínima alcanzable en fibra de sílice | $\approx0.15$ dB/km ($\approx3.4\%$/km) en 1.55 μm | 326, 350 |
| Mínimo local de atenuación | $\approx0.3$ dB/km en 1.3 μm | 350 |
| Diámetros estándar núcleo/revestimiento (μm) | 8/125, 50/125, 62.5/125, 85/125, 100/140 | 327 |
| Índice del núcleo de sílice $n_1$ | 1.44–1.46 (según $\lambda$); dopantes Ti, Ge, B | 327 |
| $\Delta$ típico | 0.001–0.02 | 327 |
| Ej. 9.1-1: $n_1=1.46$, $\Delta=0.01$ | $\bar\theta_c=8.1°$, $\theta_a=11.9°$, NA $=0.206$ | 329 |
| Fibra sin revestimiento $n_1=1.46$, $n_2=1$ | $\bar\theta_c=46.8°$, NA $=1$ | 330 |
| Corte monomodo | $V<2.405$; $\nu_c=c_o/(2.61a\cdot\mathrm{NA})$ | 337 |
| Tabla 9.2-1, cortes $V$ de $\mathrm{LP}_{lm}$ | $l=0$: 0, 3.832, 7.016; $l=1$: 2.405, 5.520, 8.654 | 336 |
| Número de modos ($V\gg1$) | $4V^2/\pi^2\approx0.41V^2$ (Bessel); $V^2/2$ (WKB escalonada); $V^2/4$ (GRIN $p=2$) | 338, 346, 348 |
| Ej. 9.2-1: $n_1=1.452$, $\Delta=0.01$, $a=25$ μm, $\lambda_o=0.85$ μm | NA $\approx0.205$, $V\approx37.9$, $M\approx585$ (sin revestimiento: $V=184.8$, $M>13\,800$) | 338 |
| Ej. 9.2-2: $n_1=1.447$, $\Delta=0.01$, $\lambda_o=1.3$ μm | monomodo si $2a<4.86$ μm; con $\Delta=0.0025$, $2a<9.72$ μm | 340 |
| Conversión de atenuación | $\alpha[\text{km}^{-1}]\approx0.23\,\alpha[\text{dB/km}]$; 3 dB ↔ $\mathcal T=0.5$; 10 dB ↔ 0.1; 20 dB ↔ 0.01 | 349 |
| Fluoruros de metales pesados (predicción) | $\alpha_{\min}\approx0.01$ dB/km en 2.5 μm | 351 |
| Ej. 9.3-1: ensanchamiento modal, $\Delta=0.01$, $n=1.46$ | escalonada $\approx24$ ns/km (2.4 μs en 100 km); GRIN óptima $\approx122$ ps/km | 352 |
| $D_\lambda$ de fibra de sílice | $-80$ ps/km·nm en 0.87 μm; $0$ en 1.312 μm; $+17$ ps/km·nm en 1.55 μm; $\approx1$ ps/km·nm cerca de 1.3 μm | 353 |
| Ej. 9.3-2: LED $\sigma_\lambda=50$ nm en 0.87 μm | 4 ns/km; 0.4 μs en 100 km. Láser $\sigma_\lambda=2$ nm cerca de 1.3 μm: 2 ps/km; 0.2 ns en 100 km | 353–354 |
| $D_{\rm PMD}$ típico | 0.1–1 ps/√km | 358 |
| Ejercicio 9.3-2 | $N_x=1.462$, $N_y=1.463$, $D_x=D_y=20$ ps/km·nm, $L=1$ km | 358 |
| Pitch $\Lambda$ de fibras agujereadas | 1–10 μm | 360 |

Fórmulas útiles agrupadas:
- NA $=\sqrt{n_1^2-n_2^2}\approx n_1\sqrt{2\Delta}$; $V=2\pi(a/\lambda_o)\mathrm{NA}$; $k_T^2+\gamma^2=\mathrm{NA}^2k_o^2$.
- $\beta_{lm}\approx n_1k_o[1-(l+2m)^2\Delta/M]$; $v_{lm}\approx c_1[1-(l+2m)^2\Delta/M]$ ($V\gg1$).
- $D_\lambda=-(\lambda_o/c_o)\,d^2n/d\lambda_o^2$; $\sigma_\tau=|D_\lambda|\sigma_\lambda L$;
  $D_w=-(1/2\pi c_o)V^2d^2\beta/dV^2$; $\delta\tau=\Delta N L/c_o$; $\sigma_{\rm PMD}=D_{\rm PMD}\sqrt L$.

## Problemas al final del capítulo (p. 363–364)

Ninguno está marcado con asterisco en el libro (la única sección con asterisco es §9.2C).

- **9.1-1 Coupling Efficiency.** (a) Fuente con potencia $P_0$ y distribución $I(\theta)=(1/\pi)P_0\cos\theta$ (potencia
  por unidad de ángulo sólido); demostrar que la potencia acoplada a la fibra es $P=(\mathrm{NA})^2P_0$, eficiencia
  $(\mathrm{NA})^2$. (b) LED plano de índice $n_s$ pegado a la fibra (área emisora menor que la sección de la fibra):
  calcular la NA y la eficiencia con $n_1=1.46$, $n_2=1.455$, $n_s=3.5$.
- **9.1-2 Numerical Aperture of a Graded-Index Fiber.** Comparar las NA de una fibra escalonada ($n_1=1.45$,
  $\Delta=0.01$) y una GRIN parabólica ($p=2$) con $n_1=1.45$, $\Delta=0.01$ (ver Ejercicio 1.3-2).
- **9.2-1 Modes.** Fibra escalonada con $a=5$ μm, $n_1=1.45$, $\Delta=0.002$: hallar la $\lambda_c$ más corta para
  operación monomodo; si $\lambda=\lambda_c/2$, identificar los índices $(l,m)$ de todos los modos guiados.
- **9.2-2 Modal Dispersion.** Fibra escalonada NA $=0.16$, $a=45$ μm, $n_1=1.45$, $\lambda_o=1.3$ μm, sin dispersión de
  material; impulso muy corto en $t=0$ tras 1 km: bosquejar el pulso recibido (a) con óptica de rayos, sólo rayos
  meridionales; (b) con óptica de ondas, sólo modos meridionales ($l=0$).
- **9.2-3 Propagation Constants and Group Velocities.** Fibra escalonada $n_1=1.444$, $n_2=1.443$, $\lambda_o=1.55$ μm:
  radio de núcleo para $V=10$; con Fig. 9.2-3 estimar las $\beta$ de todos los modos $l=0$; si el radio cambia para
  $V=4$, usar Fig. 9.2-8(a) para hallar velocidad de fase, $\beta$ y velocidad de grupo del $\mathrm{LP}_{01}$ (sin
  dispersión de material).
- **9.2-4 Propagation Constants and Wavevector (Step-Index Fiber).** $a=20$ μm, $n_1=1.47$, $n_2=1.46$, $\lambda_o=1.55$
  μm, teoría de ondas cuasi-planas, modos con $l=1$: (a) menor y mayor constante de propagación; (b) para el modo de
  menor $\beta$, radios de la corona de confinamiento y componentes de $\mathbf k$ en $r=5$ μm.
- **9.2-5 Propagation Constants and Wavevector (Graded-Index Fiber).** Lo mismo que 9.2-4 para GRIN parabólica ($p=2$).
- **9.3-3 Scattering Loss.** En 820 nm absorción 0.25 dB/km y scattering 2.25 dB/km; en 600 nm la calorimetría da 2
  dB/km de absorción: estimar la atenuación total en 600 nm (usar Rayleigh $\propto1/\lambda^4$).
- **9.3-4 Modal Dispersion in Step-Index Fibers.** Radio de núcleo de una MMF escalonada con NA $=0.1$ si $M=5000$ en
  0.87 μm; con $n_1=1.445$, $N_1=1.456$ y $\Delta$ independiente de $\lambda$, tiempo de respuesta modal $\sigma_\tau$
  para 2 km.
- **9.3-5 Modal Dispersion in Graded-Index Fibers.** GRIN con $a/\lambda_o=10$, $n_1=1.45$, $\Delta=0.01$, perfil de
  ley de potencias $p$: número de modos $M$ y tasa de ensanchamiento modal $\sigma_\tau/L$ para $p=1.9$, 2, 2.1 e $\infty$.
- **9.3-6 Pulse Propagation.** Pulso de ancho inicial $\tau_0$ en GRIN de $L$ km, perfil $p$, $n_1$ dependiente de
  $\lambda$ con $D_\lambda=-(\lambda_o/c_o)d^2n_1/d\lambda_o^2$, $\Delta$ aprox. independiente de $\lambda$, fuente de
  ancho $\sigma_\lambda$: discutir el efecto sobre el ancho temporal recibido de aumentar $L$, $\tau_0$, $p$, $|D_\lambda|$,
  $\sigma_\lambda$ y $\lambda_o$.

Ejercicios dentro del texto: **9.3-1** (p. 354, perfil óptimo con dispersión de material) y **9.3-2** (p. 358, DGD en
fibra de dos segmentos); ver sus enunciados arriba.

## Relación con Óptica No Lineal

**Temas del curso.**
- *Ondas EM y modos:* la ecuación de Helmholtz cilíndrica (9.2-1)–(9.2-6), la ecuación característica (9.2-14) y el
  parámetro $V$ (9.2-10) dan el marco modal (modos $\mathrm{LP}_{lm}$, $\beta$, índice efectivo $n=\beta/k_o$,
  Fig. 9.2-8) sobre el que se formulan las ecuaciones de propagación no lineal en fibras: el perfil $u_{01}(r)$ fija el
  área efectiva $A_{\rm eff}$ que entra en $\gamma=n_2\omega/(cA_{\rm eff})$ (Boyd/Agrawal), y la condición $V<2.405$ es
  la que garantiza operar en un solo modo transversal para SPM, solitones y supercontinuo.
- *Haz gaussiano:* el $\mathrm{LP}_{01}$ es aproximadamente gaussiano (p. 336, Fig. 9.2-4(a)); se usa esa aproximación
  para estimar el radio modal y el acoplamiento (NA, ángulo de aceptación (9.1-2)–(9.1-3)).
- *Absorción y dispersión (lineal):* §9.3A da la atenuación en dB/km, la conversión (9.3-2)–(9.3-3) y el origen físico
  de la ventana de transparencia (Rayleigh $\propto1/\lambda^4$, bandas IR/UV, OH); las longitudes de pérdida
  $L_\alpha=1/\alpha$ se comparan con las longitudes no lineal y de dispersión en los temas 7–8.
- *Pulsos en medios dispersivos y GVD:* §9.3B define el índice de grupo $N=n-\lambda\,dn/d\lambda$, el coeficiente
  $D_\lambda=-(\lambda_o/c_o)d^2n/d\lambda_o^2$ (9.3-7) en ps/km·nm, el ensanchamiento $\sigma_\tau=|D_\lambda|\sigma_\lambda L$
  (9.3-6), los regímenes **normal** ($D<0$, $\lambda<1.312$ μm) y **anómalo** ($D>0$, $\lambda>1.312$ μm) y la
  **longitud de onda de dispersión cero** (Fig. 9.3-5). Relación con el $\beta_2$ del curso: $D=-(2\pi c/\lambda^2)\beta_2$,
  de modo que dispersión anómala ↔ $\beta_2<0$, requisito de los solitones brillantes. La dispersión de guía (9.3-14) y
  las fibras DSF/DFF/DCF (Fig. 9.3-6) muestran cómo la geometría desplaza o aplana $D(\lambda)$.
- *Polarización y cristales:* la PMD ((9.3-15)–(9.3-16)), la birrefringencia residual y las fibras que mantienen la
  polarización (p. 341) conectan con el tema de polarización/matrices de Jones y son relevantes para XPM entre
  polarizaciones y para la elección de fibras en experimentos de FWM (conservación de polarización).
- *Índice dependiente de la intensidad, SPM, solitones, XPM, Raman, FWM:* el libro sólo esboza (p. 359) la dispersión no
  lineal: SPM por $n(I)$ y su compensación con la GVD en el solitón (caps. 21–22). Los apuntes del cap. 9 aportan los
  parámetros lineales ($\beta$, $D_\lambda$, $A_{\rm eff}$ vía $u_{01}$, $\alpha$) que entran en la NLSE; la
  longitud de onda de dispersión cero es también el punto donde FWM y la generación de supercontinuo son más eficientes
  por ajuste de fase.
- *Susceptibilidad no lineal, χ⁽²⁾ y χ⁽³⁾:* la sílice es centrosimétrica (sin χ⁽²⁾ volumétrico); los efectos no lineales
  en fibra son χ⁽³⁾ (Kerr, Raman, FWM). El capítulo no lo discute, pero la nota de p. 349 (polarización $\mathcal P$ como
  fuente de radiación $\propto-\omega^2\mathcal P$) es el mismo mecanismo que se extiende a $\mathcal P_{\rm NL}$.

**Proyecto final (anillos add-drop en Si₃N₄, dispersión de guías, supercontinuo, sensado de índice).**
- La dependencia del índice efectivo con $V$ (Fig. 9.2-8(a)) y la expresión $D_w=-(1/2\pi c_o)V^2d^2\beta/dV^2$
  (9.3-14) son el modelo escalar más simple de la **dispersión de guía de onda**; en la guía Si₃N₄/SiO₂ la ingeniería de
  dispersión (anchura y altura) juega el papel que aquí juegan $a$ y el perfil de gradación (DSF/DFF, p. 355–356) para
  llevar el cero de dispersión a la banda de bombeo y obtener $\beta_2<0$ para solitones/supercontinuo.
- Las fibras agujereadas/PCF (§9.4) ilustran que un revestimiento con $n_2(\lambda)$ fuertemente dependiente de $\lambda$
  produce dispersión de guía intensa, desplazamiento del cero de dispersión a $\lambda$ menores que el del material y
  **supercontinuo** y láseres de banda ancha (p. 362); es el antecedente directo de las guías de alto contraste de índice.
- Sensado refractométrico: la fracción de potencia en el revestimiento y el índice efectivo dependen de $n_2$ a través
  de NA y $V$ ((9.2-7), (9.2-10), Fig. 9.2-8(a)); un cambio de índice del analito ($n=1.33\to1.37$ como cladding) cambia
  $n_{\rm eff}$ y por tanto la resonancia del anillo. El guiado por índice efectivo (p. 361) da también la intuición del
  promedio ponderado por intensidad del índice del revestimiento.
- Pérdidas: la conversión dB/km ↔ km⁻¹ (9.3-2)–(9.3-3) y la dependencia modal de la atenuación (p. 350) se aplican a la
  estimación de $Q$ intrínseco y pérdidas de propagación en dB/cm de las guías del proyecto.
- Polarización: la degeneración de las dos polarizaciones del $\mathrm{LP}_{01}$ se rompe en guías no circulares
  (p. 341); en las guías rectangulares de Si₃N₄ los modos TE/TM tienen $n_{\rm eff}$ y dispersión distintos, lo que hay
  que fijar al simular.
