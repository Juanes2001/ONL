# Capítulo 6 — Polarization Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 197–242 (PDF 219–264). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007,
cap. 6 "Polarization Optics". Todas las páginas citadas abajo son **páginas del libro**
(página del PDF = página del libro + 22).

Convenciones de notación del libro que se respetan en estos apuntes:
- Dependencia temporal $e^{j\omega t}$, con $j=\sqrt{-1}$; la onda viajera es
  $\exp[j\omega(t - z/c)]$, es decir, un factor espacial $\exp(-jkz)$.
- Campos reales en caligráfica: $\mathcal{E}(\mathbf r,t)$; amplitudes/envolventes complejas en
  negrita: $\mathbf E(\mathbf r)$, $\mathbf A$, $\mathbf J$ (vector de Jones), $\mathbf T$ (matriz de Jones).
- $c_o$, $\epsilon_o$, $\mu_o$, $\eta_o$, $\lambda_o$, $k_o=\omega/c_o$: valores en el vacío; $n$ índice
  de refracción; $\eta=\eta_o/n$ impedancia; $\mathcal R$, $\mathcal T$ reflectancia y transmitancia
  de potencia; $\mathsf r$, $\mathsf t$ coeficientes de amplitud compleja.
- Ojo: el libro usa $\eta$ para dos cosas distintas: impedancia del medio (§6.2) y tensor de
  impermeabilidad eléctrica $\boldsymbol\eta=\epsilon_o\boldsymbol\epsilon^{-1}$ (§6.3, en negrita).
- Convención de "derecha/izquierda" para polarización circular (p. 201, nota al pie): el libro
  sigue la convención de la mayoría de textos de óptica; la literatura de ingeniería suele usar
  la opuesta.

---

## Resumen del capítulo

El capítulo describe la polarización de la luz y sus aplicaciones. Introduce la elipse de
polarización, la esfera de Poincaré y los parámetros de Stokes, y luego el formalismo matricial
de Jones (vectores y matrices 2×2) con el que se describen polarizadores, retardadores,
rotadores, cascadas y cambios de coordenadas, incluyendo el concepto de modos normales
(autovectores de la matriz de Jones). Con esa herramienta se tratan la reflexión y refracción en
una interfaz dieléctrica (ecuaciones de Fresnel, reflexión externa e interna, ángulo de
Brewster, reflexión total interna y sus fases, reflectancia y transmitancia de potencia), la
óptica de medios anisótropos (tensor de permitividad, ejes e índices principales, elipsoide de
índices, construcción geométrica de los modos normales, cristales uniaxiales con $n_o$ y $n_e$,
relación de dispersión y superficie $\mathbf k$, rayos vs. frentes de onda, doble refracción), la
actividad óptica y el efecto Faraday (vector de giro, potencia rotatoria, constante de Verdet),
los cristales líquidos nemáticos torcidos como rotadores de polarización y, por último, los
dispositivos de polarización: polarizadores (dicroicos, de Brewster, prismas birrefringentes),
láminas retardadoras, rotadores y dispositivos no recíprocos (aislador óptico).

---

## Secciones

### Introducción del capítulo (pp. 198–199)

- La polarización en un punto fijo queda determinada por la trayectoria temporal del vector
  campo eléctrico $\mathcal E(\mathbf r,t)$. Para luz monocromática el extremo del vector traza una
  **elipse** en el plano tangente al frente de onda; en general la elipse (plano, orientación y
  forma) cambia con la posición (Fig. 6.0-1a). Para una **onda plana** las elipses son iguales
  en todas partes (Fig. 6.0-1b): la onda está **elípticamente polarizada**; cuando degenera en
  una recta o un círculo, **linealmente** o **circularmente polarizada** (p. 198).
- En óptica paraxial (TEM aproximada) la polarización se describe con una sola elipse (p. 198).
- Importancia (pp. 198–199): la reflexión en una frontera, la absorción en ciertos materiales y
  el esparcimiento dependen de la polarización; en medios anisótropos el índice depende de la
  polarización (esto permite transformar lineal → circular, base de muchos dispositivos); los
  medios ópticamente activos, cristales líquidos y sustancias en campo magnético rotan el plano
  de polarización.
- Plan del capítulo (p. 199): §6.1 elipse y formalismo matricial; §6.2 reflexión/refracción;
  §6.3 cristales; §6.4 actividad óptica y magneto-óptica; §6.5 cristales líquidos; §6.6
  dispositivos.

### 6.1 Polarization of Light (p. 199)

#### 6.1A Polarization (p. 199)

Onda plana monocromática de frecuencia $\nu$, $\omega=2\pi\nu$, viajando en $z$ con velocidad $c$:

$$\mathcal E(z,t)=\operatorname{Re}\left\{\mathbf A\exp\left[j\omega\left(t-\frac zc\right)\right]\right\},\qquad (6.1\text{-}1)$$

con envolvente compleja

$$\mathbf A = A_x\hat{\mathbf x}+A_y\hat{\mathbf y},\qquad (6.1\text{-}2)$$

donde $A_x$, $A_y$ son complejos.

**Elipse de polarización (pp. 199–200).** Con $A_x=\mathsf a_x e^{j\varphi_x}$, $A_y=\mathsf a_y e^{j\varphi_y}$:

$$\mathcal E(z,t)=\mathcal E_x\hat{\mathbf x}+\mathcal E_y\hat{\mathbf y},\qquad (6.1\text{-}3)$$
$$\mathcal E_x=\mathsf a_x\cos\left[\omega\left(t-\tfrac zc\right)+\varphi_x\right],\qquad (6.1\text{-}4a)$$
$$\mathcal E_y=\mathsf a_y\cos\left[\omega\left(t-\tfrac zc\right)+\varphi_y\right].\qquad (6.1\text{-}4b)$$

Son las ecuaciones paramétricas de la elipse

$$\frac{\mathcal E_x^2}{\mathsf a_x^2}+\frac{\mathcal E_y^2}{\mathsf a_y^2}-2\cos\varphi\,\frac{\mathcal E_x\mathcal E_y}{\mathsf a_x\mathsf a_y}=\sin^2\varphi,\qquad \varphi=\varphi_y-\varphi_x.\qquad (6.1\text{-}5)$$

A $z$ fijo el extremo del campo rota periódicamente trazando la elipse; a $t$ fijo el lugar
geométrico es una hélice sobre un cilindro elíptico, que se repite cada $\lambda=c/\nu$
(Fig. 6.1-1, p. 200).

**Orientación y elipticidad (p. 200, Fig. 6.1-2).** El estado de polarización se caracteriza por
el ángulo $\psi$ (dirección del eje mayor) y el ángulo $\chi$ (elipticidad, $\tan\chi=b/a$, razón
eje menor/eje mayor). Dependen de $\mathsf r=\mathsf a_y/\mathsf a_x$ y de $\varphi$:

$$\tan 2\psi=\frac{2\mathsf r}{1-\mathsf r^2}\cos\varphi,\qquad \mathsf r=\frac{\mathsf a_y}{\mathsf a_x},\qquad (6.1\text{-}6)$$
$$\sin 2\chi=\frac{2\mathsf r}{1+\mathsf r^2}\sin\varphi,\qquad \varphi=\varphi_y-\varphi_x.\qquad (6.1\text{-}7)$$

Se obtienen rotando las coordenadas de (6.1-5) hasta eliminar el término cruzado. El tamaño de
la elipse lo fija la intensidad, $\propto |A_x|^2+|A_y|^2=\mathsf a_x^2+\mathsf a_y^2$.

**Luz linealmente polarizada (LP) (p. 200, Fig. 6.1-3).** Si una componente es nula
($\mathsf a_x=0$), o si $\varphi=0$ o $\pi$: entonces $\mathcal E_y=\pm(\mathsf a_y/\mathsf a_x)\mathcal E_x$, recta de
pendiente $\pm\mathsf a_y/\mathsf a_x$ (signo + para $\varphi=0$, − para $\pi$). También llamada
**polarización plana**. Si $\mathsf a_x=\mathsf a_y$, el plano de polarización está a 45° del eje $x$;
si $\mathsf a_x=0$, es el plano $y$–$z$.

**Luz circularmente polarizada (p. 201, Fig. 6.1-4).** Si $\varphi=\pm\pi/2$ y $\mathsf a_x=\mathsf a_y=\mathsf a_0$:
$\mathcal E_x=\mathsf a_0\cos[\omega(t-z/c)+\varphi_x]$, $\mathcal E_y=\mp\mathsf a_0\sin[\omega(t-z/c)+\varphi_x]$,
de modo que $\mathcal E_x^2+\mathcal E_y^2=\mathsf a_0^2$ (círculo).
- $\varphi=+\pi/2$: a $z$ fijo el campo rota en sentido **horario** visto desde la dirección hacia
  la que se aproxima la onda → **circular derecha (RCP)**.
- $\varphi=-\pi/2$: antihorario → **circular izquierda (LCP)**.
- Instantánea en $t$ fijo: la RCP describe una hélice derecha (como tornillo de rosca derecha
  apuntando en la dirección de la onda); la LCP una hélice izquierda. El sentido de rotación
  en (a) y (b) de la Fig. 6.1-4 es opuesto porque la onda depende de $t-z/c$.
- Nota al pie (p. 201): esta es la convención de la mayoría de textos de óptica; en la
  literatura de ingeniería suele usarse la contraria.

**Esfera de Poincaré y parámetros de Stokes (pp. 201–203, Fig. 6.1-5).**
- Dos reales ($\mathsf r,\varphi$) describen el estado; a veces se agrupan en el número complejo
  $\mathsf r\exp(j\varphi)$, la **razón de polarización compleja**. Equivalente: los ángulos $(\chi,\psi)$.
- **Esfera de Poincaré**: esfera de radio unidad; cada estado es un punto de coordenadas
  esféricas $(r=1,\ \theta=90^\circ-2\chi,\ \phi=2\psi)$. Ecuador ($\chi=0$): polarizaciones
  lineales; $2\psi=0^\circ$ y $180^\circ$ son LP a lo largo de $x$ y de $y$; polos
  $2\chi=\pm 90^\circ$: circular derecha (norte) e izquierda (sur). El resto: elípticas.
  Fig. 6.1-5(b): LP 0°, 45°, 90°, 135° sobre el ecuador.
- **Vector de Stokes** $(\mathsf S_0,\mathsf S_1,\mathsf S_2,\mathsf S_3)$: sí contiene la intensidad.
  $\mathsf S_0=\mathsf a_x^2+\mathsf a_y^2$ ∝ intensidad; $(\mathsf S_1,\mathsf S_2,\mathsf S_3)$ son las coordenadas
  cartesianas del punto en la esfera $(u_1,u_2,u_3)=(\cos2\chi\cos2\psi,\cos2\chi\sin2\psi,\sin2\chi)$
  multiplicadas por $\mathsf S_0$:

$$\mathsf S_1=\mathsf S_0\cos2\chi\cos2\psi,\quad \mathsf S_2=\mathsf S_0\cos2\chi\sin2\psi,\quad \mathsf S_3=\mathsf S_0\sin2\chi.\qquad (6.1\text{-}8a,b,c)$$

- En términos de los parámetros del campo (recuadro **Stokes Parameters**, p. 202):

$$\mathsf S_0=\mathsf a_x^2+\mathsf a_y^2=|A_x|^2+|A_y|^2\qquad (6.1\text{-}9a)$$
$$\mathsf S_1=\mathsf a_x^2-\mathsf a_y^2=|A_x|^2-|A_y|^2\qquad (6.1\text{-}9b)$$
$$\mathsf S_2=2\mathsf a_x\mathsf a_y\cos\varphi=2\operatorname{Re}\{A_x^*A_y\}\qquad (6.1\text{-}9c)$$
$$\mathsf S_3=2\mathsf a_x\mathsf a_y\sin\varphi=2\operatorname{Im}\{A_x^*A_y\}\qquad (6.1\text{-}9d)$$

- Como $\mathsf S_1^2+\mathsf S_2^2+\mathsf S_3^2=\mathsf S_0^2$, solo tres son independientes (p. 203). La
  generalización a luz parcialmente coherente está en la §11.4.
- Conclusión (p. 203): tres representaciones equivalentes del estado de polarización: (1)
  elipse, (2) esfera de Poincaré, (3) vector de Stokes; una cuarta es el vector de Jones.

#### 6.1B Matrix Representation (p. 203)

**Vector de Jones (p. 203).** Columna con las envolventes complejas de las componentes $x$ e $y$:

$$\mathbf J=\begin{bmatrix}A_x\\ A_y\end{bmatrix}.\qquad (6.1\text{-}10)$$

De $\mathbf J$ se obtiene la intensidad total $I=(|A_x|^2+|A_y|^2)/2\eta$, la razón
$\mathsf r=\mathsf a_y/\mathsf a_x=|A_y|/|A_x|$ y la fase $\varphi=\varphi_y-\varphi_x=\arg\{A_y\}-\arg\{A_x\}$, y
con ellas la elipse, el punto en Poincaré y los parámetros de Stokes.

**Tabla 6.1-1 (p. 203)** — vectores de Jones normalizados ($|A_x|^2+|A_y|^2=1$, $\varphi_x=0$):

| Estado | $\mathbf J$ |
|---|---|
| LP en dirección $x$ | $\begin{bmatrix}1\\0\end{bmatrix}$ |
| LP a ángulo $\theta$ | $\begin{bmatrix}\cos\theta\\ \sin\theta\end{bmatrix}$ |
| RCP (circular derecha) | $\dfrac{1}{\sqrt2}\begin{bmatrix}1\\ j\end{bmatrix}$ |
| LCP (circular izquierda) | $\dfrac{1}{\sqrt2}\begin{bmatrix}1\\ -j\end{bmatrix}$ |

**Polarizaciones ortogonales (pp. 203–204).** $\mathbf J_1$ y $\mathbf J_2$ son ortogonales si su
producto interno es cero:

$$(\mathbf J_1,\mathbf J_2)=A_{1x}A_{2x}^*+A_{1y}A_{2y}^*.\qquad (6.1\text{-}11)$$

Ejemplos: LP en $x$ y en $y$ (o cualquier par de direcciones ortogonales); RCP y LCP.

**Expansión en dos polarizaciones ortogonales (p. 204).** $\mathbf J=\alpha_1\mathbf J_1+\alpha_2\mathbf J_2$; si
la base está normalizada, $\alpha_1=(\mathbf J,\mathbf J_1)$, $\alpha_2=(\mathbf J,\mathbf J_2)$.

**EJEMPLO 6.1-1 — Expansiones en bases lineal y circular (p. 204).** Con $|A_x|^2+|A_y|^2=1$:
- Base $x$, $y$: $\alpha_1=A_x$, $\alpha_2=A_y$.
- Base lineal a 45° y 135°, $\mathbf J_1=\tfrac{1}{\sqrt2}\begin{bmatrix}1\\1\end{bmatrix}$,
  $\mathbf J_2=\tfrac{1}{\sqrt2}\begin{bmatrix}-1\\1\end{bmatrix}$:

$$A_{45}=\frac{1}{\sqrt2}(A_x+A_y),\qquad A_{135}=\frac{1}{\sqrt2}(A_y-A_x).\qquad (6.1\text{-}12)$$

- Base circular $\tfrac{1}{\sqrt2}\begin{bmatrix}1\\ j\end{bmatrix}$, $\tfrac{1}{\sqrt2}\begin{bmatrix}1\\ -j\end{bmatrix}$:

$$A_R=\frac{1}{\sqrt2}(A_x-jA_y),\qquad A_L=\frac{1}{\sqrt2}(A_x+jA_y).\qquad (6.1\text{-}13)$$

- Consecuencia: una onda LP a ángulo $\theta$ ($A_x=\cos\theta$, $A_y=\sin\theta$) equivale a la
  superposición de RCP y LCP con coeficientes $\tfrac{1}{\sqrt2}e^{-j\theta}$ y
  $\tfrac{1}{\sqrt2}e^{j\theta}$. Toda LP es suma ponderada de RCP y LCP.

**EJERCICIO 6.1-1 — Medición de los parámetros de Stokes (p. 204).** Mostrar que, para luz con
componentes de Jones $A_x$, $A_y$,

$$\mathsf S_0=|A_x|^2+|A_y|^2,\quad \mathsf S_1=|A_x|^2-|A_y|^2,\quad \mathsf S_2=|A_{45}|^2-|A_{135}|^2,\quad \mathsf S_3=|A_R|^2-|A_L|^2,\qquad (6.1\text{-}14a\text{–}d)$$

con $A_{45},A_{135}$ de (6.1-12) y $A_R,A_L$ de (6.1-13). Sugerir un método para medir los
parámetros de Stokes de luz con polarización arbitraria. (Idea: medir intensidades tras
polarizadores lineales a 0°, 90°, 45°, 135° y tras analizadores circulares R y L.)

**Representación matricial de dispositivos de polarización (p. 205, Fig. 6.1-6).** Sistema
lineal que mantiene la naturaleza de onda plana pero altera su polarización (ejemplos:
reflexión en una frontera plana; transmisión por una lámina anisótropa). Relación general:

$$A_{2x}=T_{11}A_{1x}+T_{12}A_{1y},\qquad A_{2y}=T_{21}A_{1x}+T_{22}A_{1y},\qquad (6.1\text{-}15)$$
$$\begin{bmatrix}A_{2x}\\A_{2y}\end{bmatrix}=\begin{bmatrix}T_{11}&T_{12}\\T_{21}&T_{22}\end{bmatrix}\begin{bmatrix}A_{1x}\\A_{1y}\end{bmatrix},\qquad (6.1\text{-}16)$$
$$\mathbf J_2=\mathbf T\mathbf J_1.\qquad (6.1\text{-}17)$$

$\mathbf T$ es la **matriz de Jones** del sistema.

**Polarizador lineal (p. 205, recuadro; Fig. 6.1-7 p. 206).** Eje de transmisión en $x$:

$$\mathbf T=\begin{bmatrix}1&0\\0&0\end{bmatrix}\qquad (6.1\text{-}18)\ \text{Linear Polarizer Along } x$$

Transforma $(A_{1x},A_{1y})\to(A_{1x},0)$: elimina la componente $y$.

**Retardador de onda (p. 206, recuadro; Fig. 6.1-8).** Eje rápido en $x$:

$$\mathbf T=\begin{bmatrix}1&0\\0&e^{-j\Gamma}\end{bmatrix}\qquad (6.1\text{-}19)\ \text{Wave Retarder (Fast Axis Along } x)$$

Transforma $(A_{1x},A_{1y})\to(A_{1x},e^{-j\Gamma}A_{1y})$: retrasa la componente $y$ una fase $\Gamma$
dejando $x$ intacta. Los ejes $x$ e $y$ son los ejes **rápido** (F) y **lento** (S).
- $\Gamma=\pi/2$ (**retardador de cuarto de onda**, p. 207): convierte LP $\begin{bmatrix}1\\1\end{bmatrix}$
  en LCP $\begin{bmatrix}1\\-j\end{bmatrix}$, y RCP $\begin{bmatrix}1\\j\end{bmatrix}$ en LP $\begin{bmatrix}1\\1\end{bmatrix}$.
- $\Gamma=\pi$ (**retardador de media onda**, p. 207): convierte LP $\begin{bmatrix}1\\1\end{bmatrix}$
  en LP $\begin{bmatrix}1\\-1\end{bmatrix}$ (rota el plano 90°), y RCP $\begin{bmatrix}1\\j\end{bmatrix}$ en
  LCP $\begin{bmatrix}1\\-j\end{bmatrix}$.
- Fig. 6.1-8 (p. 206): operaciones de $\pi/2$ y $\pi$ sobre LP a 45° y sobre circular.

**Rotador de polarización (p. 207, recuadro).** Mantiene la polarización lineal y rota el plano
un ángulo $\theta$:

$$\mathbf T=\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}\qquad (6.1\text{-}20)\ \text{Polarization Rotator}$$

Convierte $\begin{bmatrix}\cos\theta_1\\ \sin\theta_1\end{bmatrix}$ en $\begin{bmatrix}\cos\theta_2\\ \sin\theta_2\end{bmatrix}$
con $\theta_2=\theta_1+\theta$.

**Dispositivos en cascada (p. 207).** Sistema $\mathbf T_1$ seguido de $\mathbf T_2$ equivale a
$\mathbf T=\mathbf T_2\mathbf T_1$: la matriz del primer sistema atravesado va **a la derecha** del producto.

**EJERCICIO 6.1-2 — Retardadores en cascada (p. 207).** Mostrar que dos retardadores de cuarto
de onda en cascada con ejes rápidos paralelos equivalen a un retardador de media onda. ¿Cuál es
el resultado si los ejes rápidos son ortogonales? (Resultado: con ejes ortogonales,
$\operatorname{diag}(1,e^{-j\pi/2})\cdot\operatorname{diag}(e^{-j\pi/2},1)=e^{-j\pi/2}\mathbf I$: fase global, sin
efecto sobre la polarización.)

**Transformación de coordenadas (pp. 207–208, recuadro).** Si $\mathbf J$ es el vector de Jones en
$x$–$y$, en un sistema $x'$–$y'$ rotado un ángulo $\theta$ (eje $x'$ a $\theta$ del eje $x$):

$$\mathbf J'=\mathbf R(\theta)\mathbf J,\qquad (6.1\text{-}21)$$
$$\mathbf R(\theta)=\begin{bmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{bmatrix}.\qquad (6.1\text{-}22)\ \text{Coordinate Transformation}$$

La matriz de Jones se transforma como

$$\mathbf T'=\mathbf R(\theta)\,\mathbf T\,\mathbf R(-\theta),\qquad (6.1\text{-}23)$$
$$\mathbf T=\mathbf R(-\theta)\,\mathbf T'\,\mathbf R(\theta),\qquad (6.1\text{-}24)$$

con $\mathbf R(-\theta)=\mathbf R(\theta)^{-1}$ ($\mathbf R(-\theta)\mathbf R(\theta)=\mathbf I$). Demostración:
$\mathbf J_2'=\mathbf R(\theta)\mathbf J_2=\mathbf R(\theta)\mathbf T\mathbf J_1$ y $\mathbf J_1=\mathbf R(-\theta)\mathbf J_1'$, luego
$\mathbf J_2'=\mathbf R(\theta)\mathbf T\mathbf R(-\theta)\mathbf J_1'$.

**EJERCICIO 6.1-3 — Matriz de Jones de un polarizador (p. 208, recuadro).** Mostrar que la
matriz de Jones de un polarizador lineal con eje de transmisión a ángulo $\theta$ del eje $x$ es

$$\mathbf T=\begin{bmatrix}\cos^2\theta&\sin\theta\cos\theta\\ \sin\theta\cos\theta&\sin^2\theta\end{bmatrix}.\qquad (6.1\text{-}25)\ \text{Linear Polarizer at Angle }\theta$$

Derivar (6.1-25) usando (6.1-18), (6.1-22) y (6.1-24).

**Modos normales (p. 208).** Son los estados de polarización que no cambian al atravesar el
sistema (Apéndice C):

$$\mathbf T\mathbf J=\mu\mathbf J,\qquad (6.1\text{-}26)$$

es decir, los **autovectores** de $\mathbf T$, con autovalores $\mu$. Al ser 2×2 hay dos modos
normales $\mathbf T\mathbf J_1=\mu_1\mathbf J_1$, $\mathbf T\mathbf J_2=\mu_2\mathbf J_2$. Si $\mathbf T$ es hermítica
($T_{12}=T_{21}^*$), los modos son ortogonales. Usados como base: $\mathbf J=\alpha_1\mathbf J_1+\alpha_2\mathbf J_2$
⇒ $\mathbf T\mathbf J=\alpha_1\mu_1\mathbf J_1+\alpha_2\mu_2\mathbf J_2$.

**EJERCICIO 6.1-4 — Modos normales de sistemas simples (p. 209).**
(a) Mostrar que los modos normales del polarizador lineal son ondas linealmente polarizadas.
(b) Mostrar que los modos normales del retardador son ondas linealmente polarizadas.
(c) Mostrar que los modos normales del rotador de polarización son ondas circularmente
polarizadas derecha e izquierda. ¿Cuáles son los autovalores de cada sistema?
(Resultados: polarizador: $\mu=1,0$; retardador: $\mu=1,e^{-j\Gamma}$; rotador: $\mu=e^{\mp j\theta}$
para RCP/LCP.)

### 6.2 Reflection and Refraction (p. 209)

**Planteamiento (pp. 209–210, Fig. 6.2-1).** Onda plana monocromática de polarización
arbitraria incidente en una frontera plana entre dos medios lineales, homogéneos e isótropos
con impedancias $\eta_1,\eta_2$ e índices $n_1,n_2$. Subíndices 1, 2, 3 = incidente, refractada,
reflejada. Los frentes de onda se acoplan en la frontera si $\theta_3=\theta_1$ y se cumple la ley
de Snell:

$$n_1\sin\theta_1=n_2\sin\theta_2.\qquad (6.2\text{-}1)$$

A cada onda se le asocia un sistema $x$–$y$ en el plano normal a su propagación; vectores de Jones

$$\mathbf J_1=\begin{bmatrix}A_{1x}\\A_{1y}\end{bmatrix},\quad \mathbf J_2=\begin{bmatrix}A_{2x}\\A_{2y}\end{bmatrix},\quad \mathbf J_3=\begin{bmatrix}A_{3x}\\A_{3y}\end{bmatrix},\qquad (6.2\text{-}2)$$

con $\mathbf J_2=\mathbf t\mathbf J_1$, $\mathbf J_3=\mathbf r\mathbf J_1$ ($\mathbf t$, $\mathbf r$ matrices de Jones 2×2 de
transmisión y reflexión). Se obtienen de las condiciones de frontera (continuidad de las
componentes tangenciales de $\mathbf E$ y $\mathbf H$ y normales de $\mathbf D$ y $\mathbf B$); $E/H=\eta$
($\eta_1$ para incidente y reflejada, $\eta_2$ para transmitida).

Los modos normales son LP a lo largo de $x$ y de $y$ (desacoplados):
- Modo polarizado en $x$ (campo $\mathcal E$ **ortogonal al plano de incidencia**): **TE**
  (transversal eléctrico), polarización **ortogonal** o **s** (*senkrecht*).
- Modo polarizado en $y$ (campo $\mathcal E$ **paralelo al plano de incidencia**, $\mathcal H$
  ortogonal): **TM** (transversal magnético), polarización **paralela** o **p**.
- Los ejes $y$ de la Fig. 6.2-1 se definen de modo que sus componentes paralelas a la frontera
  apuntan en la misma dirección.

Matrices diagonales (p. 210):

$$\mathbf t=\begin{bmatrix}\mathsf t_x&0\\0&\mathsf t_y\end{bmatrix},\qquad \mathbf r=\begin{bmatrix}\mathsf r_x&0\\0&\mathsf r_y\end{bmatrix},\qquad (6.2\text{-}3)$$
$$E_{2x}=\mathsf t_xE_{1x},\quad E_{2y}=\mathsf t_yE_{1y},\qquad (6.2\text{-}4)$$
$$E_{3x}=\mathsf r_xE_{1x},\quad E_{3y}=\mathsf r_yE_{1y}.\qquad (6.2\text{-}5)$$

$\mathsf t_x,\mathsf t_y$: transmitancias de amplitud compleja TE y TM; $\mathsf r_x,\mathsf r_y$: reflectancias.

**Coeficientes en términos de impedancias (p. 210, recuadro):**

$$\mathsf r_x=\frac{\eta_2\sec\theta_2-\eta_1\sec\theta_1}{\eta_2\sec\theta_2+\eta_1\sec\theta_1},\qquad \mathsf t_x=1+\mathsf r_x,\qquad (6.2\text{-}6)\ \text{TE}$$
$$\mathsf r_y=\frac{\eta_2\cos\theta_2-\eta_1\cos\theta_1}{\eta_2\cos\theta_2+\eta_1\cos\theta_1},\qquad \mathsf t_y=(1+\mathsf r_y)\frac{\cos\theta_1}{\cos\theta_2}.\qquad (6.2\text{-}7)\ \text{TM}$$

$\eta=\sqrt{\mu/\epsilon}$ es compleja si $\epsilon$ y/o $\mu$ lo son (medios con pérdidas o
conductores). Para dieléctricos sin pérdidas y no magnéticos, $\eta=\eta_o/n$ con
$\eta_o=\sqrt{\mu_o/\epsilon_o}$ real.

**Ecuaciones de Fresnel (p. 211, recuadro):**

$$\mathsf r_x=\frac{n_1\cos\theta_1-n_2\cos\theta_2}{n_1\cos\theta_1+n_2\cos\theta_2},\qquad \mathsf t_x=1+\mathsf r_x,\qquad (6.2\text{-}8)\ \text{TE}$$
$$\mathsf r_y=\frac{n_1\sec\theta_1-n_2\sec\theta_2}{n_1\sec\theta_1+n_2\sec\theta_2},\qquad \mathsf t_y=(1+\mathsf r_y)\frac{\cos\theta_1}{\cos\theta_2}.\qquad (6.2\text{-}9)\ \text{TM}$$

Dados $n_1,n_2,\theta_1$ se determina $\theta_2$ por Snell:

$$\cos\theta_2=\sqrt{1-\sin^2\theta_2}=\sqrt{1-(n_1/n_2)^2\sin^2\theta_1}.\qquad (6.2\text{-}10)$$

El radicando puede ser negativo ⇒ coeficientes en general complejos. Magnitudes $|\mathsf r_x|$,
$|\mathsf r_y|$ y fases $\varphi_x=\arg\{\mathsf r_x\}$, $\varphi_y=\arg\{\mathsf r_y\}$ en Figs. 6.2-2 a 6.2-5
(todas con razón de índices 1.5), para reflexión **externa** ($n_1<n_2$) e **interna** ($n_1>n_2$).

**Polarización TE (pp. 211–212).**
- *Reflexión externa* ($n_1<n_2$), Fig. 6.2-2: $\mathsf r_x$ siempre real y negativo ⇒ $\varphi_x=\pi$.
  $|\mathsf r_x|=(n_2-n_1)/(n_1+n_2)$ en $\theta_1=0$ y crece hasta 1 en $\theta_1=90^\circ$ (incidencia rasante).
- *Reflexión interna* ($n_1>n_2$), Fig. 6.2-3: para $\theta_1$ pequeño, real y positivo, magnitud
  $(n_1-n_2)/(n_1+n_2)$ en 0°, crece hasta 1 en el **ángulo crítico** $\theta_c=\sin^{-1}(n_2/n_1)$.
  Para $\theta_1>\theta_c$, $|\mathsf r_x|=1$: **reflexión total interna**. Se demuestra escribiendo
  (nota al pie: el signo − de la raíz es el consistente con la derivación de Fresnel)
  $\cos\theta_2=-\sqrt{1-\sin^2\theta_1/\sin^2\theta_c}=-j\sqrt{\sin^2\theta_1/\sin^2\theta_c-1}$ y
  sustituyendo en (6.2-8). La fase de la reflexión total es (recuadro, p. 212):

$$\tan\frac{\varphi_x}{2}=\sqrt{\frac{\cos^2\theta_c}{\cos^2\theta_1}-1}\qquad (6.2\text{-}11)\ \text{TE-Reflection Phase Shift}$$

  $\varphi_x$ crece de 0 en $\theta_1=\theta_c$ a $\pi$ en $\theta_1=90^\circ$. Esta fase es clave en las
  guías de onda dieléctricas (§8.2).

**Polarización TM (pp. 212–213).**
- *Reflexión externa* ($n_1<n_2$), Fig. 6.2-4: $\mathsf r_y$ siempre real; vale
  $(n_1-n_2)/(n_1+n_2)<0$ en incidencia normal; su magnitud decrece hasta anularse cuando
  $n_1\sec\theta_1=n_2\sec\theta_2$, en el **ángulo de Brewster** (recuadro):

$$\theta_B=\tan^{-1}(n_2/n_1).\qquad (6.2\text{-}12)\ \text{Brewster Angle}$$

  Para $\theta_1>\theta_B$, $\mathsf r_y$ cambia de signo ($\varphi_y$ pasa de $\pi$ a 0) y su magnitud
  crece hasta 1 en 90°. La ausencia de reflexión TM en Brewster sirve para hacer polarizadores
  (§6.6). Otras propiedades: Prob. 6.2-5.
- *Reflexión interna* ($n_1>n_2$), Fig. 6.2-5: en $\theta_1=0$, $\mathsf r_y>0$ de magnitud
  $(n_1-n_2)/(n_1+n_2)$; decrece hasta 0 en $\theta_B=\tan^{-1}(n_2/n_1)$; luego negativa, magnitud
  creciente hasta 1 en $\theta_c$; para $\theta_1>\theta_c$ reflexión total interna con fase (recuadro):

$$\tan\frac{\varphi_y}{2}=\frac{-1}{\sin^2\theta_c}\sqrt{\frac{\cos^2\theta_c}{\cos^2\theta_1}-1}.\qquad (6.2\text{-}13)\ \text{TM-Reflection Phase Shift}$$

- En incidencia normal, $\mathsf r=(n_1-n_2)/(n_1+n_2)$ sea TE o TM, externa o interna (p. 213).

**EJERCICIO 6.2-1 — Ventanas de Brewster (p. 213, Fig. 6.2-6).** ¿A qué ángulo se transmite un
haz TM a través de una lámina de vidrio $n=1.5$ en aire ($n=1$) sin pérdidas por reflexión en
ninguna de las dos superficies? Tales láminas (ventanas de Brewster) se usan en láseres
(§15.2D). (Resultado: $\theta_B=\tan^{-1}1.5\approx 56.3^\circ$ en la primera cara; en la segunda
cara, interna, $\theta_B'=\tan^{-1}(1/1.5)\approx 33.7^\circ=\theta_2$, también sin reflexión.)

**Reflectancia y transmitancia de potencia (pp. 213–214).** $\mathcal R$ y $\mathcal T$ son razones de
flujo de potencia **normal a la frontera**. Como incidente y reflejada están en el mismo medio y
con el mismo ángulo,

$$\mathcal R=|\mathsf r|^2.\qquad (6.2\text{-}14)$$

En incidencia normal (TE o TM, externa o interna; recuadro):

$$\mathcal R=\left(\frac{n_1-n_2}{n_1+n_2}\right)^2.\qquad (6.2\text{-}15)\ \text{Power Reflectance at Normal Incidence}$$

Ejemplos (p. 214): vidrio ($n=1.5$)/aire: $\mathcal R=0.04$ (4 %); GaAs ($n=3.6$)/aire:
$\mathcal R\approx0.32$ (32 %); a ángulos oblicuos puede ser mucho mayor o menor (Fig. 6.2-7:
$\mathcal R$ TE y TM vs. $\theta$ para aire/GaAs; TM se anula en Brewster ≈ 74°).

Por conservación de potencia (sin absorción):

$$\mathcal T=1-\mathcal R.\qquad (6.2\text{-}16)$$

**Importante:** en general $\mathcal T\neq|\mathsf t|^2$, porque la potencia viaja con ángulos e impedancias
distintas en los dos medios. El flujo normal a la frontera es
$(|\mathcal E|^2/2\eta)\cos\theta=(|\mathcal E|^2/2\eta_o)\,n\cos\theta$, de donde

$$\mathcal T=\frac{n_2\cos\theta_2}{n_1\cos\theta_1}|\mathsf t|^2.\qquad (6.2\text{-}17)$$

**Reflectancia de una lámina (p. 214).** Con dos superficies, en incidencia normal:
$\mathcal R(1+\mathcal T^2)$ (la potencia reflejada en la cara lejana atraviesa dos veces la cercana).
Vidrio en aire: $0.04[1+(0.96)^2]\approx0.077$ (7.7 %). No incluye interferencia (se promedia
con luz incoherente, §11.2) ni reflexiones múltiples; medios estratificados en §7.1.

**EJERCICIO 6.2-2 — Reflectancia de un medio conductor (p. 215).** Las ecuaciones (6.2-6) y
(6.2-7) sirven para la reflectancia $\mathcal R$ en la frontera dieléctrico–conductor.
(a) Mostrar que $\mathcal R\approx1$ si la conductividad $\sigma$ es infinita.
(b) Mostrar que en incidencia normal y para $\sigma\gg\epsilon_o\omega$ emerge la relación
$\mathcal R=1-2\sqrt{2\epsilon_o\omega/\sigma}$, conocida como **relación de Hagen–Rubens**. Usarla para
la reflectancia del cobre a $\lambda_o=1.06\ \mu$m y $10.6\ \mu$m, con
$\sigma=0.58\times10^8\ (\Omega\cdot\mathrm m)^{-1}$.
(c) Mostrar que si el conductor sigue el modelo de Drude (5.5-39), $\mathcal R=1$ a frecuencias
por debajo de la frecuencia de plasma.

### 6.3 Optics of Anisotropic Media (p. 215)

**Introducción (pp. 215–216, Fig. 6.3-1).** Un dieléctrico es anisótropo si sus propiedades
ópticas macroscópicas dependen de la dirección. Tipos de orden:
- Posiciones y orientaciones moleculares aleatorias → isótropo: gases, líquidos, sólidos amorfos.
- Granos cristalinos desunidos con orientación aleatoria → **policristalino**: granos anisótropos
  pero promedio isótropo.
- Patrón periódico y orientación común → **cristal**: en general anisótropo.
- Moléculas anisótropas con orientación no aleatoria aunque posiciones aleatorias →
  **cristal líquido**: anisótropo (orden orientacional sin orden posicional completo).

#### 6.3A Refractive Indexes (p. 216)

**Tensor de permitividad (p. 216).** En un medio anisótropo lineal cada componente de $\mathbf D$ es
combinación lineal de las tres de $\mathbf E$:

$$D_i=\sum_j\epsilon_{ij}E_j,\qquad (6.3\text{-}1)$$
$$\mathbf D=\boldsymbol\epsilon\mathbf E.\qquad (6.3\text{-}2)$$

$i,j=1,2,3\leftrightarrow x,y,z$. $\{\epsilon_{ij}\}$ es el **tensor de permitividad eléctrica**
(rango 2, nueve coeficientes). Para la mayoría de los dieléctricos es **simétrico**
($\epsilon_{ij}=\epsilon_{ji}$): relación D–E recíproca. Vale para dieléctricos no magnéticos sin
actividad óptica y sin campo magnético externo (ver §6.4). Con simetría: seis números
independientes; con simetrías cristalinas, aún menos.

**Representación geométrica de vectores y tensores (pp. 216–217, Fig. 6.3-2).** Un vector
(tensor de rango 1) es una flecha; un escalar es rango 0. Un tensor de rango 2 simétrico se
representa por la superficie cuádrica (elipsoide)

$$\sum_{ij}\epsilon_{ij}x_ix_j=1,\qquad (6.3\text{-}3)$$

la **representación cuádrica**, invariante ante cambios de coordenadas (6 grados de libertad).
En el sistema principal, $\epsilon_{ij}$ es diagonal:

$$\epsilon_1x_1^2+\epsilon_2x_2^2+\epsilon_3x_3^2=1,\qquad (6.3\text{-}4)$$

con semiejes $1/\sqrt{\epsilon_1}$, $1/\sqrt{\epsilon_2}$, $1/\sqrt{\epsilon_3}$.

**Ejes principales e índices principales (p. 217).** Siempre existe un sistema donde los
elementos no diagonales se anulan:

$$D_1=\epsilon_1E_1,\quad D_2=\epsilon_2E_2,\quad D_3=\epsilon_3E_3,\qquad (6.3\text{-}5)$$

$\epsilon_1=\epsilon_{11}$, etc. A lo largo de estas direcciones $\mathbf E\parallel\mathbf D$. Son los **ejes
principales** (y planos principales). En adelante $x,y,z\equiv x_1,x_2,x_3$ son los ejes
principales. Los **índices de refracción principales**:

$$n_1=\sqrt{\epsilon_1/\epsilon_o},\qquad n_2=\sqrt{\epsilon_2/\epsilon_o},\qquad n_3=\sqrt{\epsilon_3/\epsilon_o}.\qquad (6.3\text{-}6)$$

**Cristales biaxiales, uniaxiales e isótropos (p. 217).**
- Tres índices distintos → **biaxial**.
- Un eje de simetría de orden 3, 4 o 6 → dos índices iguales ($n_1=n_2$) → **uniaxial**:
  $n_1=n_2=n_o$ (**ordinario**), $n_3=n_e$ (**extraordinario**). **Uniaxial positivo** si $n_e>n_o$;
  **negativo** si $n_e<n_o$. El eje $z$ es el **eje óptico**.
- Simetría cúbica → tres índices iguales → isótropo.

**Tensor de impermeabilidad (p. 218).** $\mathbf E=\boldsymbol\epsilon^{-1}\mathbf D$; se define el **tensor de
impermeabilidad eléctrica** $\boldsymbol\eta=\epsilon_o\boldsymbol\epsilon^{-1}$ (no confundir con la impedancia
$\eta$), tal que $\epsilon_o\mathbf E=\boldsymbol\eta\mathbf D$. Simétrico, con los mismos ejes principales que
$\boldsymbol\epsilon$; valores principales $\epsilon_o/\epsilon_1=1/n_1^2$, $1/n_2^2$, $1/n_3^2$. Cualquiera de los
dos tensores describe por completo al cristal.

**Elipsoide de índices (p. 218, recuadro; Fig. 6.3-3).** También llamado **indicatriz óptica**:
representación cuádrica de $\boldsymbol\eta$:

$$\sum_{ij}\eta_{ij}x_ix_j=1,\qquad i,j=1,2,3,\qquad (6.3\text{-}7)$$

que en ejes principales es

$$\frac{x_1^2}{n_1^2}+\frac{x_2^2}{n_2^2}+\frac{x_3^2}{n_3^2}=1,\qquad (6.3\text{-}8)\ \text{Index Ellipsoid}$$

con valores principales $1/n_1^2,1/n_2^2,1/n_3^2$ y **semiejes $n_1,n_2,n_3$**. Describe por completo
las propiedades ópticas (ejes principales e índices). Uniaxial → elipsoide de revolución;
isótropo → esfera.

#### 6.3B Propagation Along a Principal Axis (p. 218)

**Modos normales (pp. 218–219, Fig. 6.3-4).** Onda plana en dirección $z$ (eje principal),
LP en $x$: viaja con velocidad de fase $c_o/n_1$ ($k=n_1k_o$) sin cambiar su polarización, porque
$\mathbf E$ solo tiene $E_1$ y $D_1=\epsilon_1E_1$ ⇒ $\mathbf D\parallel\mathbf E$ y la ecuación de onda da
$1/\sqrt{\mu_o\epsilon_1}=c_o/n_1$. LP en $y$: velocidad $c_o/n_2$. Los modos normales para propagación
en $z$ son las LP en $x$ y en $y$ (velocidad y polarización se mantienen). Fig. 6.3-4:
$k=n_1k_o$, $n_2k_o$, $n_3k_o$ cuando $\mathbf E$ apunta en $x$, $y$, $z$.

**Polarización en dirección arbitraria (p. 219, Fig. 6.3-5).** Onda en $z$ LP en dirección
arbitraria del plano $x$–$y$: se descompone en los modos normales $x$ e $y$, que viajan con
$c_o/n_1$ y $c_o/n_2$ y acumulan fases $\varphi_x=n_1k_od$, $\varphi_y=n_2k_od$ tras la distancia $d$.
**Retardo de fase:**

$$\varphi=\varphi_y-\varphi_x=(n_2-n_1)k_od.$$

La recombinación da una onda elípticamente polarizada: el cristal actúa como **retardador de
onda** (dos polarizaciones ortogonales con distinta velocidad). La LP inicial a 45° **no** es un
modo normal.

#### 6.3C Propagation in an Arbitrary Direction (p. 220)

Onda plana en dirección $\hat{\mathbf u}$ arbitraria. Los dos modos normales son LP; sus índices
$n_a$, $n_b$ y direcciones se hallan con el elipsoide de índices.

**Construcción del elipsoide de índices para los modos normales (p. 220, recuadro gris;
Fig. 6.3-6).** Dado el elipsoide $x_1^2/n_1^2+x_2^2/n_2^2+x_3^2/n_3^2=1$:
1. Trazar el plano que pasa por el origen normal a $\hat{\mathbf u}$. Su intersección con el elipsoide
   es la **elipse de índices**.
2. Los semiejes mayor y menor de la elipse de índices son los índices $n_a$ y $n_b$ de los dos
   modos normales.
3. Las direcciones de esos ejes son las direcciones de $\mathbf D_a$ y $\mathbf D_b$ (ortogonales).
4. $\mathbf E_a$, $\mathbf E_b$ se obtienen de $\mathbf D_a$, $\mathbf D_b$ con (6.3-5).

**Demostración (pp. 220–221).** Con campos $\propto\exp(-j\mathbf k\cdot\mathbf r)$, $\mathbf k=k\hat{\mathbf u}$,
las ecuaciones de Maxwell (5.4-3), (5.4-4) se reducen a

$$\mathbf k\times\mathbf H=-\omega\mathbf D,\qquad (6.3\text{-}9)$$
$$\mathbf k\times\mathbf E=\omega\mu_o\mathbf H.\qquad (6.3\text{-}10)$$

Sustituyendo:

$$\mathbf k\times(\mathbf k\times\mathbf E)=-\omega^2\mu_o\mathbf D,\qquad (6.3\text{-}11)$$
$$\mathbf k\times(\mathbf k\times\boldsymbol\epsilon^{-1}\mathbf D)=-\omega^2\mu_o\mathbf D.\qquad (6.3\text{-}12)$$

Ecuación de autovalores para $\mathbf D$ (conveniente porque $\mathbf D\perp\hat{\mathbf u}$). Con
$\boldsymbol\eta=\epsilon_o\boldsymbol\epsilon^{-1}$, $\mathbf k=k\hat{\mathbf u}$, $n=k/k_o$, $k_o^2=\omega^2\mu_o\epsilon_o$:

$$-\hat{\mathbf u}\times(\hat{\mathbf u}\times\boldsymbol\eta\mathbf D)=\frac{1}{n^2}\mathbf D.\qquad (6.3\text{-}13)$$

$-\hat{\mathbf u}\times(\hat{\mathbf u}\times\cdot)$ es la proyección sobre el plano normal a $\hat{\mathbf u}$:

$$\mathbf P_u\boldsymbol\eta\mathbf D=\frac{1}{n^2}\mathbf D.\qquad (6.3\text{-}14)$$

Autovalores $1/n_a^2$, $1/n_b^2$; autovectores $\mathbf D_a$, $\mathbf D_b$. Geométricamente: $\boldsymbol\eta$ ↔
elipsoide de índices; $\mathbf P_u$ ↔ proyección sobre el plano normal a $\hat{\mathbf u}$; resolver
(6.3-14) ≡ hallar los ejes principales de la elipse de intersección. ∎

**Caso especial: cristales uniaxiales (p. 221, recuadro; Fig. 6.3-7 p. 222).** Con
$n_1=n_2=n_o$, $n_3=n_e$, el elipsoide es de revolución. Para $\hat{\mathbf u}$ a ángulo $\theta$ del eje
óptico, la elipse de índices tiene semiejes $n_o$ y $n(\theta)$:

$$\frac{1}{n^2(\theta)}=\frac{\cos^2\theta}{n_o^2}+\frac{\sin^2\theta}{n_e^2}.\qquad (6.3\text{-}15)\ \text{Refractive Index of Extraordinary Wave}$$

- Modo $n_b=n_o$: **onda ordinaria**, índice $n_o$ independiente de $\theta$. Su $\mathbf D$ es normal
  al plano definido por el eje óptico ($z$) y $\mathbf k$; $\mathbf E\parallel\mathbf D$.
- Modo $n_a=n(\theta)$: **onda extraordinaria**, índice que va de $n_o$ ($\theta=0$) a $n_e$
  ($\theta=90^\circ$). Su $\mathbf D$ es normal a $\mathbf k$ y está en el plano $k$–$z$; $\mathbf E$ **no** es
  paralelo a $\mathbf D$ (Fig. 6.3-7: para la onda e, $\mathbf E$ y $\mathbf D$ forman un ángulo; para la o,
  $\mathbf E,\mathbf D$ salen del plano del papel).

#### 6.3D Dispersion Relation, Rays, Wavefronts, and Energy Transport (p. 221)

**Geometría de los vectores (p. 222, Fig. 6.3-8).** La onda se caracteriza por $\mathbf k$, los
campos $\mathbf E,\mathbf D,\mathbf H,\mathbf B$ y el vector de Poynting complejo $\mathbf S=\tfrac12\mathbf E\times\mathbf H^*$
(dirección del flujo de potencia). De (6.3-9): $\mathbf D\perp\mathbf k$ y $\mathbf D\perp\mathbf H$; de (6.3-10):
$\mathbf H\perp\mathbf k$ y $\mathbf H\perp\mathbf E$; $\mathbf S\perp\mathbf E,\mathbf H$. Así **$\mathbf D,\mathbf E,\mathbf k,\mathbf S$ están en un
plano** normal a $\mathbf H,\mathbf B$; en él $\mathbf D\perp\mathbf k$ y $\mathbf S\perp\mathbf E$, pero $\mathbf D\not\parallel\mathbf E$ y
$\mathbf S\not\parallel\mathbf k$ en general.

**Relación de dispersión (pp. 222–223).** Con $\mathbf D=\boldsymbol\epsilon\mathbf E$ en (6.3-11):

$$\mathbf k\times(\mathbf k\times\mathbf E)+\omega^2\mu_o\boldsymbol\epsilon\mathbf E=0.\qquad (6.3\text{-}16)$$

En componentes sobre los ejes principales:

$$\begin{bmatrix}n_1^2k_o^2-k_2^2-k_3^2 & k_1k_2 & k_1k_3\\ k_2k_1 & n_2^2k_o^2-k_1^2-k_3^2 & k_2k_3\\ k_3k_1 & k_3k_2 & n_3^2k_o^2-k_1^2-k_2^2\end{bmatrix}\begin{bmatrix}E_1\\E_2\\E_3\end{bmatrix}=\begin{bmatrix}0\\0\\0\end{bmatrix},\qquad (6.3\text{-}17)$$

con $(k_1,k_2,k_3)$ componentes de $\mathbf k$, $k_o=\omega/c_o$. Determinante nulo ⇒
$\omega=\omega(k_1,k_2,k_3)$ (función no lineal): la **relación de dispersión**, ecuación de una
superficie en el espacio $k$ llamada **superficie normal** o **superficie $\mathbf k$**. La
intersección de $\hat{\mathbf u}$ con ella da $k=n\omega/c_o$ y por tanto $n$; hay dos intersecciones
(dos modos normales).

**Superficie $\mathbf k$ (p. 223, Fig. 6.3-9).** Centrosimétrica, de dos hojas (una por modo).
Corta cada plano principal en una elipse y un círculo. Biaxial ($n_1<n_2<n_3$): las hojas se
tocan en cuatro puntos que definen **dos ejes ópticos**. Uniaxial: esfera + elipsoide de
revolución que se tocan en dos puntos → **un** eje óptico ($z$). Isótropo: una sola esfera.
Para $\hat{\mathbf u}=(u_1,u_2,u_3)$, el número de onda satisface

$$\sum_{j=1,2,3}\frac{u_j^2k^2}{k^2-n_j^2k_o^2}=1.\qquad (6.3\text{-}18)$$

Ecuación de 4.º orden en $k$ (2.º en $k^2$): soluciones $\pm k_a$, $\pm k_b$; solo las positivas
tienen sentido. $n_a=k_a/k_o$, $n_b=k_b/k_o$. Para las polarizaciones: sustituir
$(k_1,k_2,k_3)=(ku_1,ku_2,ku_3)$ en (6.3-17) para cada $k$ y resolver dos de las tres ecuaciones
para $E_1/E_3$ y $E_2/E_3$.

**Velocidad de fase, rayos y velocidad de grupo (pp. 223–224).** La distancia del origen a la
superficie $\mathbf k$ en la dirección $\hat{\mathbf u}$ es inversamente proporcional a la velocidad de
fase $c=\omega/k$. La velocidad de grupo para rayos (haces localizados, paquetes espaciales) es
$\mathbf v=\nabla_k\omega(\mathbf k)$, normal a la superficie $\mathbf k$ (que es $\omega=$ const.) ⇒ **los rayos
viajan normales a la superficie $\mathbf k$**. Los frentes de onda son perpendiculares a $\mathbf k$ (fase
$\mathbf k\cdot\mathbf r$). El vector de Poynting $\mathbf S$ también es normal a la superficie $\mathbf k$
(tomando diferenciales de (6.3-9) y (6.3-10) se muestra $\Delta\mathbf k\cdot\mathbf S=0$) ⇒
$\mathbf S\parallel\mathbf v$.
- Superficie esférica (isótropo): $\mathbf v,\mathbf S,\mathbf k$ paralelos (Fig. 6.3-10a).
- Superficie no esférica: rayos y energía **no** son ortogonales a los frentes de onda: los rayos
  viajan oblicuos a sus frentes de onda (propiedad "extraordinaria", Fig. 6.3-10b).

**Caso especial: cristales uniaxiales (pp. 224–225, Figs. 6.3-11 y 6.3-12).** La superficie
$\mathbf k$ se factoriza:

$$(k^2-n_o^2k_o^2)\left(\frac{k_1^2+k_2^2}{n_e^2}+\frac{k_3^2}{n_o^2}-k_o^2\right)=0.\qquad (6.3\text{-}19)$$

Esfera (onda ordinaria):

$$k=n_ok_o,\qquad (6.3\text{-}20)$$

y elipsoide de revolución (onda extraordinaria):

$$\frac{k_1^2+k_2^2}{n_e^2}+\frac{k_3^2}{n_o^2}=k_o^2.\qquad (6.3\text{-}21)$$

Por simetría en torno al eje óptico basta tomar $\mathbf k$ en el plano $y$–$z$, a ángulo $\theta$
del eje óptico; se dibujan un círculo (radio $n_o$) y una elipse (semiejes $n_o$ en $k_3/k_o$ y
$n_e$ en $k_2/k_o$) (Fig. 6.3-11, uniaxial positivo). Dado $\hat{\mathbf u}$: onda ordinaria
$k=n_ok_o$ para toda dirección; onda extraordinaria $k=n(\theta)k_o$ con $n(\theta)$ de (6.3-15),
confirmando la construcción del elipsoide de índices.
- Fig. 6.3-12(a), **ordinaria**: índice $n_o$, polarizada normal al plano $k$–$z$;
  $\mathbf E\parallel\mathbf D$, $\mathbf S\parallel\mathbf k$.
- Fig. 6.3-12(b), **extraordinaria**: índice $n(\theta)$; polarizada en el plano $k$–$z$, con
  $\mathbf D$ tangente a la elipse (superficie $\mathbf k$) en el punto de intersección con $\mathbf k$.
  "Extraordinaria" porque $\mathbf D\not\parallel\mathbf E$ (ambos en el plano $k$–$z$) y
  $\mathbf S\not\parallel\mathbf k$: la potencia no fluye a lo largo de $\mathbf k$; los rayos no son normales a
  los frentes de onda; la onda viaja "de lado" (**walk-off**; el ángulo entre $\mathbf S$ y
  $\mathbf k$ es el ángulo de walk-off, tema del Prob. 6.3-2).

#### 6.3E Double Refraction (p. 225)

**Refracción de ondas planas (pp. 225–226, Fig. 6.3-13).** Frontera entre medio isótropo (aire,
$n=1$) y cristal. Principio: los frentes de onda incidente y refractados deben acoplarse en la
frontera. Como el cristal soporta dos modos con distinta velocidad de fase, una onda incidente
produce **dos ondas refractadas** con direcciones y polarizaciones distintas: **doble refracción**
o **birrefringencia**. Condición de acoplamiento de fase (Snell):

$$k_o\sin\theta_1=k\sin\theta,\qquad (6.3\text{-}22)$$

con $\theta_1$, $\theta$ ángulos de incidencia y refracción. Como $k=n(\theta)k_o$ depende de $\theta$:

$$\sin\theta_1=n(\theta_a+\theta)\sin\theta,\qquad (6.3\text{-}23)$$

donde $\theta_a$ es el ángulo entre el eje óptico y la normal a la superficie, de modo que
$\theta_a+\theta$ es el ángulo del rayo refractado con el eje óptico (Snell modificado). Se
resuelve gráficamente: intersección de la superficie $\mathbf k$ con el plano de incidencia y
búsqueda del $\theta$ que satisface (6.3-22); dos soluciones. La polarización incidente reparte
la energía entre las dos ondas refractadas.

Uniaxial con plano de incidencia paralelo al eje óptico (círculo + elipse, Fig. 6.3-13):
- Onda **ordinaria** (polarización ortogonal, TE) a $\theta=\theta_o$:

$$\sin\theta_1=n_o\sin\theta_o;\qquad (6.3\text{-}24)$$

- Onda **extraordinaria** (polarización paralela, TM) a $\theta=\theta_e$:

$$\sin\theta_1=n(\theta_a+\theta_e)\sin\theta_e,\qquad (6.3\text{-}25)$$

con $n(\theta)$ de (6.3-15). Si la onda incidente lleva ambas polarizaciones emergen las dos.

**Refracción de rayos (p. 227, Figs. 6.3-14 y 6.3-15).** Los rayos en un medio anisótropo no
viajan normales a los frentes de onda. La onda refractada debe cumplir el acoplamiento de fase,
así que Snell (6.3-23) se aplica a $\mathbf k$; pero como $\mathbf k$ no es la dirección del rayo,
**Snell no se aplica a los rayos** en medios anisótropos. Ejemplo dramático: **incidencia normal**
sobre un cristal uniaxial con eje óptico ni paralelo ni perpendicular a la superficie. El $\mathbf k$
refractado es normal a la frontera para ambas ondas; el rayo ordinario es paralelo a $\mathbf k$,
pero el rayo extraordinario apunta en la normal a la superficie $\mathbf k$, a un ángulo $\theta_s$
con la normal a la frontera (Fig. 6.3-14): **la incidencia normal produce refracción oblicua**;
los frentes de onda de ambos rayos refractados siguen paralelos a la frontera. En una lámina,
los dos rayos se refractan de nuevo en la segunda cara y salen **separados lateralmente** con
polarizaciones ortogonales (Fig. 6.3-15): la lámina es un **divisor de haz polarizador**.

### 6.4 Optical Activity and Magneto-Optics (p. 228)

#### 6.4A Optical Activity (p. 228)

Ciertos materiales actúan como rotadores naturales de polarización: **actividad óptica**. Sus
modos normales son ondas **circularmente** polarizadas; RCP y LCP viajan con velocidades
distintas $c_o/n_+$ y $c_o/n_-$. El medio rota el plano de polarización un ángulo
$\pi(n_--n_+)d/\lambda_o$ proporcional al espesor $d$. **Potencia rotatoria** (ángulo por unidad de
longitud; recuadro p. 228):

$$\rho=\frac{\pi}{\lambda_o}(n_--n_+).\qquad (6.4\text{-}1)\ \text{Rotatory Power}$$

El sentido de rotación es el de la componente circular más rápida (menor índice). Si $n_+<n_-$,
$\rho>0$ y la rotación sigue el sentido del campo de la RCP (horario visto desde donde llega la
onda, Fig. 6.4-1a): material **dextrógiro** (*dextrorotatory*); si $n_+>n_-$: **levógiro**
(*levorotatory*). Fig. 6.4-1(b): si la onda se refleja y vuelve, el plano rota en sentido
opuesto y la onda **retraza** su polarización (dispositivo recíproco).

**Derivación de la potencia rotatoria (p. 228).** LP a ángulo $\theta$ como suma de RCP y LCP de
igual amplitud (Ejercicio/Ejemplo 6.1-1):

$$\begin{bmatrix}\cos\theta\\ \sin\theta\end{bmatrix}=\tfrac12e^{-j\theta}\begin{bmatrix}1\\ j\end{bmatrix}+\tfrac12e^{j\theta}\begin{bmatrix}1\\ -j\end{bmatrix}.\qquad (6.4\text{-}2)$$

Tras $d$, fases $\varphi_+=2\pi n_+d/\lambda_o$ y $\varphi_-=2\pi n_-d/\lambda_o$:

$$\tfrac12e^{-j\theta}e^{-j\varphi_+}\begin{bmatrix}1\\ j\end{bmatrix}+\tfrac12e^{j\theta}e^{-j\varphi_-}\begin{bmatrix}1\\ -j\end{bmatrix}=e^{-j\varphi_o}\begin{bmatrix}\cos(\theta-\varphi/2)\\ \sin(\theta-\varphi/2)\end{bmatrix},\qquad (6.4\text{-}3)$$

con $\varphi_o=\tfrac12(\varphi_++\varphi_-)$ y $\varphi=\varphi_--\varphi_+=2\pi(n_--n_+)d/\lambda_o$: LP rotada un
ángulo $\varphi/2=\pi(n_--n_+)d/\lambda_o$, como en (6.4-1). ∎

Materiales (p. 228): estructura intrínsecamente helicoidal: selenio, telurio, TeO$_2$, cuarzo
($\alpha$-SiO$_2$), cinabrio (HgS). Líquidos ópticamente activos: moléculas **quirales** (formas
especulares izquierda/derecha): aminoácidos (casi todos levógiros), azúcares (dextrosa
dextrógira, levulosa/fructosa levógira). La potencia rotatoria de soluciones depende de la
concentración y la estructura → **sacarímetro** (concentración de azúcar).

**Ecuaciones materiales (p. 229).** Un $\mathbf B$ variable aplicado a una estructura helicoidal
induce corriente circulante → momento dipolar eléctrico ∝ $j\omega\mathbf B=-\nabla\times\mathbf E$. El
medio es **espacialmente dispersivo** (relación D–E no local; $\mathbf D(\mathbf r)$ depende de
$\nabla\times\mathbf E$). Para onda plana $\mathbf E(\mathbf r)=\mathbf E\exp(-j\mathbf k\cdot\mathbf r)$,
$\nabla\times\mathbf E=-j\mathbf k\times\mathbf E$ ⇒ permitividad dependiente de $\mathbf k$ (análogo a la
dispersión temporal, que depende de $\omega$, §5.2). Ecuación material dependiente de $\mathbf k$:

$$\mathbf D=\boldsymbol\epsilon\mathbf E+j\epsilon_o\xi\,\mathbf k\times\mathbf E,\qquad (6.4\text{-}4)$$

con $\xi$ un **pseudoescalar** (cambia de signo con la quiralidad del sistema de coordenadas);
aproximación de primer orden en $\mathbf k$ (nota: Landau, Lifshitz y Pitaevskii, *Electrodynamics
of Continuous Media*, cap. 12). Forma habitual:

$$\mathbf D=\boldsymbol\epsilon\mathbf E+j\epsilon_o\mathbf G\times\mathbf E,\qquad (6.4\text{-}5)$$

con $\mathbf G=\xi\mathbf k$ el **vector de giro** (*gyration vector*). $\mathbf D\not\parallel\mathbf E$ porque
$\mathbf G\times\mathbf E\perp\mathbf E$.

**Modos normales del medio ópticamente activo (pp. 229–230).** Onda en $z$: $\mathbf k=(0,0,k)$,
$\mathbf G=(0,0,G)$, $G=\xi k$:

$$\begin{bmatrix}D_1\\D_2\\D_3\end{bmatrix}=\epsilon_o\begin{bmatrix}n^2&-jG&0\\ jG&n^2&0\\ 0&0&n^2\end{bmatrix}\begin{bmatrix}E_1\\E_2\\E_3\end{bmatrix},\qquad n^2=\epsilon/\epsilon_o.\qquad (6.4\text{-}6)$$

Diagonal: medio isótropo de índice $n$; fuera de la diagonal (∝ $G$): actividad óptica. Para
$\mathbf E=(E_0,\pm jE_0,0)$ (+ RCP, − LCP): $\mathbf D=(D_0,\pm jD_0,0)$ con $D_0=\epsilon_o(n^2\pm G)E_0$, es
decir $\mathbf D=\epsilon_on_\pm^2\mathbf E$ con (recuadro p. 230)

$$n_\pm=\sqrt{n^2\pm G}.\qquad (6.4\text{-}7)$$

Para cada onda circular $\mathbf D\parallel\mathbf E$; (6.3-11) se cumple con $k=n_\pm k_o$. RCP y LCP se
propagan sin cambiar su estado, con índices $n_+$ y $n_-$: son los modos normales.

**EJERCICIO 6.4-1 — Potencia rotatoria de un medio ópticamente activo (p. 230).** Mostrar que
si $G\ll n$, la potencia rotatoria es aproximadamente

$$\rho\approx-\frac{\pi G}{\lambda_on}.\qquad (6.4\text{-}8)$$

Dependencia con la longitud de onda (p. 230): $G\propto k\propto1/\lambda_o$ ⇒ $\rho\propto1/\lambda_o^2$
(además $n=n(\lambda_o)$). Ejemplos: cuarzo $\rho\approx31$ °/mm a 500 nm y ≈ 22 °/mm a 600 nm;
tiogalato de plata (AgGaS$_2$) ≈ 700 °/mm a 490 nm y ≈ 500 °/mm a 500 nm.

#### 6.4B Magneto-Optics: The Faraday Effect (p. 230)

Muchos materiales rotan la polarización en presencia de un campo magnético **estático**:
**efecto Faraday**. Ángulo ∝ espesor; potencia rotatoria ∝ componente de $B$ en la dirección de
propagación:

$$\rho=\mathfrak VB,\qquad (6.4\text{-}9)$$

$\mathfrak V$ = **constante de Verdet** (p. 231). Para $\mathfrak V>0$ la rotación sigue un tornillo de
rosca derecha apuntando en la dirección del campo magnético (Fig. 6.4-2a). A diferencia de la
actividad óptica, **el sentido de rotación no se invierte al invertir la propagación**: una
onda que atraviesa el rotador, se refleja y vuelve sufre **el doble** de rotación
(Fig. 6.4-2b). Materiales: vidrios, YIG (granate de itrio y hierro), TGG (granate de terbio y
galio), TbAlG (granate de terbio y aluminio); $\mathfrak V_{\rm TbAlG}\approx-1.16$ min/(Oe·cm) a
500 nm. Películas delgadas ferrimagnéticas → dispositivos compactos.

**Ecuaciones materiales (p. 231).** $\boldsymbol\epsilon=\boldsymbol\epsilon(\mathbf H)$ por la interacción del campo
estático con el movimiento electrónico inducido por el campo óptico. Para el efecto Faraday:

$$\mathbf D=\boldsymbol\epsilon\mathbf E+j\epsilon_o\mathbf G\times\mathbf E,\qquad (6.4\text{-}10)$$
$$\mathbf G=\gamma\mathbf B,\qquad (6.4\text{-}11)$$

$\mathbf B=\mu\mathbf H$ flujo magnético estático, $\gamma$ **coeficiente de magnetogiro**. Idéntica a
(6.4-5) con $\mathbf G=\gamma\mathbf B$ en lugar de $\xi\mathbf k$; como $\mathbf G$ no depende de $\mathbf k$, invertir
la propagación no invierte la rotación → **aisladores ópticos** (§6.6C/D). Con (6.4-8):
$\rho\approx-\pi G/\lambda_on=-\pi\gamma B/\lambda_on$, de donde (recuadro p. 231)

$$\mathfrak V\approx-\frac{\pi\gamma}{\lambda_on}.\qquad (6.4\text{-}12)$$

La constante de Verdet depende de $\lambda_o$.

### 6.5 Optics of Liquid Crystals (p. 232)

**Cristales líquidos (p. 232, Fig. 6.5-1).** Moléculas orgánicas alargadas (forma de cigarro),
sin orden posicional (líquido) pero con orden orientacional (cristal). Tres fases:
- **Nemático**: orientaciones iguales, posiciones aleatorias.
- **Esméctico**: orientaciones iguales, centros apilados en capas paralelas (orden posicional
  en una dimensión).
- **Colestérico**: nemático distorsionado con rotación helicoidal de la orientación.

Son fluidos: las moléculas se reorientan ante una fuerza (p. ej., se alinean con la dirección de
frotado de las placas de vidrio). **Nemático torcido** (*twisted nematic*): nemático entre dos
placas pulidas en direcciones perpendiculares (Fig. 6.5-2) → torsión impuesta. Base de las
pantallas LCD; electro-óptica en el cap. 20.

**Propiedades ópticas del nemático torcido (p. 233, Fig. 6.5-3).** Medio **inhomogéneo** y
**anisótropo** que actúa localmente como cristal uniaxial con el eje óptico paralelo a la
dirección molecular. Se analiza como capas delgadas perpendiculares al eje de torsión ($z$),
cada una un cristal uniaxial cuyo eje óptico rota helicoidalmente. Ángulo de torsión lineal en $z$:

$$\theta=\alpha z,\qquad (6.5\text{-}1)$$

$\alpha$ = coeficiente de torsión (grados por unidad de longitud); eje óptico en el plano $x$–$y$ a
ángulo $\theta$ del eje $x$. Índices $n_o$, $n_e$ (típicamente $n_e>n_o$); **coeficiente de retardo
de fase** (retardo por unidad de longitud):

$$\beta=(n_e-n_o)k_o.\qquad (6.5\text{-}2)$$

La celda queda caracterizada por $\alpha$ y $\beta$. En la práctica $\beta\gg\alpha$ (muchos ciclos de
retardo antes de que el eje rote apreciablemente); entonces, si la onda incidente en $z=0$ es
LP en $x$, se mantiene LP y su plano rota siguiendo la torsión: ángulo $\theta=\alpha z$, total
$\alpha d$ para longitud $d$. La celda es un **rotador de polarización** con potencia rotatoria
$\alpha$ (uso en pantallas, §20.3).

**Demostración (p. 234).** Se divide $d$ en $N$ capas de ancho $\Delta z=d/N$; la capa $m$ en
$z_m=m\Delta z$ es un retardador con eje lento (eje óptico) a $\theta_m=m\Delta\theta$,
$\Delta\theta=\alpha\Delta z$; por (6.1-24):

$$\mathbf T_m=\mathbf R(-\theta_m)\,\mathbf T_r\,\mathbf R(\theta_m),\qquad (6.5\text{-}3)$$
$$\mathbf T_r=\begin{bmatrix}\exp(-jn_ek_o\Delta z)&0\\0&\exp(-jn_ok_o\Delta z)\end{bmatrix}\qquad (6.5\text{-}4)$$

(retardador con eje en $x$; $\mathbf R(\theta)$ de (6.1-22)). En términos de $\beta$:

$$\mathbf T_r=\exp(-j\varphi\Delta z)\begin{bmatrix}\exp(-j\beta\Delta z/2)&0\\0&\exp(j\beta\Delta z/2)\end{bmatrix},\qquad \varphi=(n_o+n_e)k_o/2,\qquad (6.5\text{-}5)$$

y se ignora el prefactor de fase global. Matriz total:

$$\mathbf T=\prod_{m=N}^{1}\mathbf T_m=\prod_{m=N}^{1}\mathbf R(-\theta_m)\mathbf T_r\mathbf R(\theta_m).\qquad (6.5\text{-}6)$$

Con $\mathbf R(\theta_m)\mathbf R(-\theta_{m-1})=\mathbf R(\Delta\theta)$:

$$\mathbf T=\mathbf R(-\theta_N)\,[\mathbf T_r\mathbf R(\Delta\theta)]^{N-1}\,\mathbf T_r\,\mathbf R(\theta_1),\qquad (6.5\text{-}7)$$
$$\mathbf T_r\mathbf R(\Delta\theta)=\begin{bmatrix}\exp(-j\beta\Delta z/2)&0\\0&\exp(j\beta\Delta z/2)\end{bmatrix}\begin{bmatrix}\cos\alpha\Delta z&\sin\alpha\Delta z\\-\sin\alpha\Delta z&\cos\alpha\Delta z\end{bmatrix}.\qquad (6.5\text{-}8)$$

En principio $\mathbf T$ se determina con $\alpha,\beta,d=N\Delta z$. Para $\alpha\ll\beta$,
$\mathbf R(\Delta\theta)\approx\mathbf I$:

$$\mathbf T\approx\mathbf R(-\theta_N)[\mathbf T_r]^N\mathbf R(\theta_1)=\mathbf R(-\alpha N\Delta z)\begin{bmatrix}\exp(-j\beta N\Delta z/2)&0\\0&\exp(j\beta N\Delta z/2)\end{bmatrix},\qquad (6.5\text{-}9)$$
$$\mathbf T=\mathbf R(-\alpha d)\begin{bmatrix}\exp(-j\beta d/2)&0\\0&\exp(j\beta d/2)\end{bmatrix}.\qquad (6.5\text{-}10)$$

Esto es un retardador de retardo $\beta d$ (eje lento en $x$) seguido de un rotador de ángulo
$\alpha d$. Para entrada LP en $x$ el retardador solo añade fase ⇒ el dispositivo rota la
polarización el ángulo de torsión $\alpha d$; LP en $y$ rota lo mismo. ∎

### 6.6 Polarization Devices (p. 235)

#### 6.6A Polarizers (p. 235)

Un polarizador lineal transmite la componente del campo a lo largo de su eje de transmisión y
bloquea la ortogonal, por absorción selectiva, reflexión selectiva en medios isótropos o
reflexión/refracción selectiva en medios anisótropos.

- **Absorción selectiva (dicroísmo) (p. 235, Fig. 6.6-1).** Materiales **dicroicos**: absorción
  dependiente de la dirección del campo (estructuras moleculares anisótropas). El más común:
  **Polaroid H-sheet** (1938): lámina de alcohol polivinílico impregnada de yodo, calentada y
  estirada. Análogo IR: **polarizador de rejilla de alambres** (*wire-grid*): la componente del
  campo paralela a los alambres se absorbe, la perpendicular pasa. Fig. 6.6-1: transmitancias
  máxima (~0.8–0.9) y mínima (~0 hasta ~1000 nm, luego crece) de un polarizador dicroico típico
  entre 400 y 1200 nm.
- **Reflexión selectiva (p. 235, Fig. 6.6-2 p. 236).** En el ángulo de Brewster la reflectancia
  TM se anula (toda la TM se refracta): solo se refleja TE, el reflector actúa como polarizador
  (**polarizador de ángulo de Brewster**).
- **Refracción selectiva — divisores de haz polarizadores (pp. 235–236, Fig. 6.6-3).** En un
  cristal anisótropo las ondas o y e se refractan a ángulos distintos y se separan (§6.3E,
  Fig. 6.3-15). Dispositivos de dos prismas uniaxiales cementados con orientaciones distintas:
  **prisma de Wollaston**, **prisma de Rochon**, **prisma de Glan–Thompson** (este último da
  gran separación angular). En la figura los cristales son uniaxiales negativos (p. ej., calcita).

#### 6.6B Wave Retarders (p. 236)

Convierte una polarización en otra; caracterizado por su retardo $\Gamma$ y sus ejes rápido y
lento (§6.1B). Modos normales: LP a lo largo de los ejes, con velocidades distintas ⇒ fase
relativa $\Gamma$. Construcción típica: lámina de cristal anisótropo; luz a lo largo del eje
principal $z$, modos LP en $x$ e $y$ con índices $n_1$, $n_2$ (velocidades $c_o/n_1$, $c_o/n_2$); si
$n_1<n_2$ el eje $x$ es el rápido. Para espesor $d$:

$$\Gamma=(n_2-n_1)k_od=2\pi(n_2-n_1)d/\lambda_o,$$

proporcional a $d$ e inversamente a $\lambda_o$ (y $n_2-n_1$ depende de $\lambda_o$). Ejemplo (p. 236):
**mica** con índices 1.599 y 1.594 a 633 nm ⇒ $\Gamma/d\approx15.8\pi$ rad/mm; espesor 63.3 µm ⇒
$\Gamma\approx\pi$ (media onda).

**Control de intensidad con un retardador entre dos polarizadores (p. 237, Fig. 6.6-4).**
Retardador de retardo $\Gamma$ entre dos polarizadores **cruzados** con ejes a 45° de los del
retardador. Transmitancia de potencia:

$$\mathcal T=\sin^2(\Gamma/2).\qquad (6.6\text{-}1)$$

(Se obtiene con matrices de Jones o viendo la elipse de la luz retardada y su proyección en el
segundo polarizador.) $\Gamma=0$: nada se transmite (polarizadores ortogonales); $\Gamma=\pi$: todo
(el retardador rota 90° el plano). Fig. 6.6-4: elipses para $\Gamma=0,\pi/4,\pi/2,3\pi/4,\pi$ y
curva $\mathcal T(\Gamma)$ periódica. Aplicaciones: modular $n_1,n_2$ con un campo eléctrico DC →
**moduladores electro-ópticos** (cap. 20); monitorear variaciones de espesor; como $\Gamma$ depende
de $\lambda_o$, filtro (poco selectivo; con otras configuraciones, filtros de banda estrecha).

#### 6.6C Polarization Rotators (p. 237)

Rota el plano de LP un ángulo fijo manteniendo la linealidad. Realizaciones: medios ópticamente
activos, efecto Faraday (§6.4), nemático torcido (§6.5). Entre dos polarizadores, la luz
transmitida depende del ángulo de rotación → modulación de intensidad variando $B$ (Faraday) o
la orientación molecular del cristal líquido con un campo eléctrico (cap. 20).

#### 6.6D Nonreciprocal Polarization Devices (p. 238)

Un dispositivo es **recíproco** si su efecto sobre la polarización es invariante ante la
inversión del sentido de propagación (la onda que vuelve retraza los cambios y llega al estado
inicial); si no, **no recíproco**. Todos los sistemas del capítulo son recíprocos salvo el
**rotador de Faraday** (§6.4B).

**Aislador óptico (p. 238, Fig. 6.6-5).** "Válvula de un solo sentido": evita que la luz
reflejada vuelva a la fuente (p. ej., láseres semiconductores). Rotador de Faraday entre dos
polarizadores con ejes a 45°; $B$ ajustado para rotar 45° (tornillo derecho en $z$). Hacia
adelante: cruza el polarizador A, rota 45°, pasa B. Hacia atrás: LP a 45° pasa B, el rotador
añade otros 45° (90° total) y A la bloquea. El rotador de Faraday es **necesario**: un rotador
ópticamente activo o de cristal líquido (recíprocos) devolvería la luz a la fuente. Aisladores
YIG o TGG: atenuación de la onda de retorno hasta 90 dB en un rango amplio de $\lambda$; películas
delgadas en imanes permanentes → aisladores muy compactos.

**Rotación de polarización no recíproca (p. 239, Fig. 6.6-6).** Rotador de Faraday de 45°
seguido de un retardador de media onda. Onda LP hacia adelante a 22.5° del eje rápido del
retardador: +45° (Faraday) y −45° (retardador) ⇒ conserva su estado. Hacia atrás:
$45^\circ+45^\circ=90^\circ$. Combinado con un divisor de haz polarizador, desvía la onda de
retorno lejos de la fuente → **circuladores ópticos** (§23.1).

### Reading List (pp. 239–240)

Generales: Damask (*Polarization Optics in Telecommunications*, 2004); Goldstein (*Polarized
Light*, 2003); Yariv & Yeh (*Optical Waves in Crystals*, 2003); Nye (*Physical Properties of
Crystals*, 1957/2001); Sugano & Kojima (*Magneto-Optics*, 2000); Brosseau (1998); Clarke &
Grainger (1971/1996); Huard (1996); Collett (1993); Kliger, Lewis & Randall (1990); Azzam &
Bashara (*Ellipsometry and Polarized Light*, 1977/1989); Gay (1967/1982); Robson (1974);
Shurcliff (1962/1966); Velluz, Le Grand & Grosjean (1965); Shurcliff & Ballard (1964).
Cristales líquidos: Oswald & Pieranski (2005); Vicari (2003); Collings (2002); Yeh & Gu (*Optics
of Liquid Crystal Displays*, 1999); Chigrinov (1999); de Gennes (1974/1995); Chandrasekhar
(1992); Ericksen & Kinderlehrer (1987); Blinov (1983); de Jeu (1980); Meier, Sackmann &
Grabmaier (1975). Artículos: Ando et al. (MRS 834, 2005); Mansuripur, "The Faraday Effect"
(OPN 10(11), 1999); Billings (SPIE MS 57, 1992; MS 23, 1990); Jacobs (SPIE MS 46, 1992);
Lakhtakia (SPIE MS 15, 1990); Ginzburg, "On Crystal Optics with Spatial Dispersion" (Phys. Rep.
194, 1990); Bennett & Bennett (Handbook of Optics, 1978); Swindell (1975); Agranovich &
Ginzburg (Progress in Optics 9, 1971).

---

## Tablas y datos numéricos útiles

**Vectores de Jones normalizados (Tabla 6.1-1, p. 203):** LP$_x$ $[1,0]^T$; LP$_\theta$
$[\cos\theta,\sin\theta]^T$; RCP $\tfrac1{\sqrt2}[1,j]^T$; LCP $\tfrac1{\sqrt2}[1,-j]^T$.

**Matrices de Jones (recuadros §6.1B):**

| Dispositivo | $\mathbf T$ | Ec. |
|---|---|---|
| Polarizador lineal en $x$ | $\begin{bmatrix}1&0\\0&0\end{bmatrix}$ | (6.1-18) |
| Retardador, eje rápido $x$, retardo $\Gamma$ | $\begin{bmatrix}1&0\\0&e^{-j\Gamma}\end{bmatrix}$ | (6.1-19) |
| Rotador de polarización, ángulo $\theta$ | $\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}$ | (6.1-20) |
| Cambio de coordenadas $\mathbf R(\theta)$ | $\begin{bmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{bmatrix}$ | (6.1-22) |
| Polarizador lineal a ángulo $\theta$ | $\begin{bmatrix}\cos^2\theta&\sin\theta\cos\theta\\ \sin\theta\cos\theta&\sin^2\theta\end{bmatrix}$ | (6.1-25) |
| Retardador con eje a $\theta$ (derivable) | $\mathbf R(-\theta)\operatorname{diag}(1,e^{-j\Gamma})\mathbf R(\theta)$ | (6.1-24) |

**Reflectancias en incidencia normal (p. 214):** vidrio/aire ($n=1.5$): $\mathcal R=0.04$;
lámina de vidrio en aire (dos caras, sin interferencia): ≈ 0.077; GaAs/aire ($n=3.6$):
$\mathcal R\approx0.32$.

**Ángulos de Brewster y críticos (derivables de (6.2-12) y $\theta_c=\sin^{-1}(n_2/n_1)$):**
vidrio 1.5 en aire: $\theta_B=56.3^\circ$ (externa), $33.7^\circ$ (interna), $\theta_c=41.8^\circ$.
Aire → GaAs: $\theta_B\approx74.5^\circ$ (Fig. 6.2-7).

**Índices de cristales uniaxiales que aparecen en el capítulo:**

| Material | $n_o$ | $n_e$ | Tipo | Dónde |
|---|---|---|---|---|
| Cuarzo (SiO$_2$) | 1.544 | 1.553 | positivo | Probs. 6.3-1, 6.3-2, 6.3-3 (a 633 nm) |
| LiNbO$_3$ | 2.20 | 2.29 | positivo | Prob. 6.3-5 (633 nm) |
| Mica (lámina) | 1.594 | 1.599 | — ($n_2-n_1=0.005$) | p. 236 (633 nm): $\Gamma/d\approx15.8\pi$ rad/mm; 63.3 µm → $\lambda/2$ |
| Calcita | — | — | negativo | Fig. 6.6-3 (ejemplo de uniaxial negativo) |

**Potencia rotatoria (p. 230):** cuarzo ≈ 31 °/mm (500 nm), ≈ 22 °/mm (600 nm); AgGaS$_2$
≈ 700 °/mm (490 nm), ≈ 500 °/mm (500 nm). $\rho\propto1/\lambda_o^2$ aproximadamente.

**Constante de Verdet (p. 231):** TbAlG $\mathfrak V\approx-1.16$ min/(Oe·cm) a 500 nm. Materiales
Faraday: vidrios, YIG, TGG, TbAlG. Aisladores YIG/TGG: hasta 90 dB de aislamiento (p. 238).

**Conductividad del cobre (Ej. 6.2-2):** $\sigma=0.58\times10^8\ (\Omega\cdot\mathrm m)^{-1}$;
Hagen–Rubens: $\mathcal R=1-2\sqrt{2\epsilon_o\omega/\sigma}$.

**Materiales ópticamente activos (p. 228):** Se, Te, TeO$_2$, $\alpha$-SiO$_2$, HgS; líquidos
quirales (aminoácidos levógiros; dextrosa dextrógira, fructosa levógira).

**Fórmulas de uso frecuente en talleres:**
- Retardo de una lámina: $\Gamma=2\pi(n_2-n_1)d/\lambda_o$ (p. 236); cuarto de onda:
  $d=\lambda_o/[4(n_e-n_o)]$ (+ múltiplos de $\lambda_o/(n_e-n_o)$ … ver Prob. 6.3-1).
- Índice extraordinario: $1/n^2(\theta)=\cos^2\theta/n_o^2+\sin^2\theta/n_e^2$ (6.3-15).
- Ángulo de walk-off (no está escrito explícitamente en el texto; se deduce de que $\mathbf S$ es
  normal a la elipse (6.3-21)): $\tan\theta_S=(n_o^2/n_e^2)\tan\theta$ para el ángulo del rayo con el
  eje óptico, de modo que el walk-off es $\theta_S-\theta$ (necesario para el Prob. 6.3-2).
- Transmitancia retardador entre polarizadores cruzados a 45°: $\mathcal T=\sin^2(\Gamma/2)$ (6.6-1).

---

## Problemas al final del capítulo (pp. 240–242)

Los ejercicios intercalados en el texto (6.1-1 a 6.1-4, 6.2-1, 6.2-2, 6.4-1) están transcritos
arriba en su sección. Los problemas de final de capítulo numeran a continuación de los
ejercicios; se marcan con * los avanzados (el libro solo marca 6.3-6).

**6.1-5 Orthogonal Polarizations (p. 240).** Mostrar que si dos estados elípticamente polarizados
son ortogonales, los ejes mayores de sus elipses son perpendiculares y los sentidos de rotación
son opuestos.

**6.1-6 Rotating a Polarization Rotator (p. 240).** Mostrar que la matriz de Jones de un
rotador de polarización es invariante ante rotaciones del sistema de coordenadas.

**6.1-7 Half-Wave Retarder (p. 241).** Considere luz linealmente polarizada que pasa por un
retardador de media onda. Si el plano de polarización forma un ángulo $\theta$ con el eje rápido
del retardador, mostrar que la luz transmitida está linealmente polarizada a un ángulo $-\theta$,
es decir, se rota un ángulo $2\theta$. ¿Por qué el retardador de media onda no es equivalente a
un rotador de polarización?

**6.1-8 Wave Retarders in Tandem (p. 241).** Escriba las matrices de Jones para:
(a) un retardador $\pi/2$ con eje rápido a lo largo de $x$;
(b) un retardador $\pi$ con eje rápido a 45° de $x$;
(c) un retardador $\pi/2$ con eje rápido a lo largo de $y$.
Si los tres retardadores se colocan en tándem, con (c) después de (b) después de (a), mostrar
que el dispositivo resultante introduce una rotación de 90°. ¿Qué ocurre si se invierte el
orden de los tres retardadores? *(Usado en la Tarea 2.)*

**6.1-9 Reflection of Circularly Polarized Light (p. 241).** Mostrar que la luz circularmente
polarizada cambia de quiralidad (derecha se vuelve izquierda y viceversa) al reflejarse en un
espejo.

**6.1-10 Anti-Glare Screen (p. 241).** Un objeto autoluminoso se observa a través de una
ventana de vidrio. Se usa una pantalla antirreflejo para eliminar el deslumbramiento causado por
la reflexión de la luz de fondo en las superficies de la ventana. Mostrar que tal pantalla puede
construirse con la combinación de un polarizador lineal y un retardador de cuarto de onda cuyos
ejes están a 45° del eje de transmisión del polarizador. ¿Puede considerarse la pantalla un
aislador óptico?

**6.2-3 Derivation of Fresnel Equations (p. 241).** Derivar la ecuación de reflexión (6.2-6),
que se usa para obtener la ecuación de Fresnel (6.2-8) para polarización TE. ¿Cómo obtendría el
coeficiente de reflexión si la luz incidente fuera un haz en lugar de una onda plana?

**6.2-4 Reflectance of Glass (p. 241).** Una onda plana incide desde aire ($n=1$) sobre una
lámina de vidrio ($n=1.5$) a un ángulo de incidencia de 45°. Determinar las reflectancias de
potencia de las ondas TE y TM. ¿Cuál es la reflectancia promedio para luz no polarizada (luz
con ondas TE y TM de igual intensidad)?

**6.2-5 Refraction at the Brewster Angle (p. 241).** Usar la condición
$n_1\sec\theta_1=n_2\sec\theta_2$ y la ley de Snell $n_1\sin\theta_1=n_2\sin\theta_2$ para derivar
(6.2-12) para el ángulo de Brewster. Mostrar también que en el ángulo de Brewster
$\theta_1+\theta_2=90^\circ$, de modo que las direcciones de las ondas reflejada y refractada son
ortogonales y, por tanto, el campo eléctrico de la onda TM refractada es paralelo a la dirección
de la onda reflejada. La reflexión puede verse como un proceso de esparcimiento en el que la
onda refractada actúa como fuente de radiación que genera la onda reflejada. En el ángulo de
Brewster esta fuente oscila en una dirección paralela a la de propagación de la onda reflejada,
así que no puede radiar y no se refleja luz TM. *(Usado en la Tarea 2.)*

**6.2-6 Retardation Associated with Total Internal Reflection (p. 241).** Determinar el
retardo de fase entre las ondas TE y TM introducido por la reflexión total interna en la
frontera vidrio ($n=1.5$)–aire ($n=1$) a un ángulo de incidencia $\theta=1.2\,\theta_c$, con
$\theta_c$ el ángulo crítico.

**6.2-7 Goos–Hänchen Shift (p. 241).** Considere dos ondas planas TE que sufren reflexión total
interna a ángulos $\theta$ y $\theta+d\theta$, con $d\theta$ incremental. Si el retardo de fase entre
las ondas reflejadas se escribe $d\varphi=\xi\,d\theta$, hallar una expresión para el coeficiente
$\xi$. Esbozar los patrones de interferencia de las dos ondas incidentes y de las dos reflejadas
y verificar que están desplazados una distancia lateral proporcional a $\xi$. Cuando la onda
incidente es un haz (compuesto de muchas ondas planas), el haz reflejado se desplaza
lateralmente una distancia proporcional a $\xi$: **efecto Goos–Hänchen**.

**6.2-8 Reflection from an Absorptive Medium (p. 241).** Usar las ecuaciones de Maxwell y las
condiciones de frontera apropiadas para mostrar que la reflectancia de amplitud compleja en la
frontera entre el vacío y un medio de índice $n$ y coeficiente de absorción $\alpha$, en
incidencia normal, es $\mathsf r=[(n-j\alpha c/2\omega)-1]/[(n-j\alpha c/2\omega)+1]$.

**6.3-1 Maximum Retardation in Quartz (p. 241).** El cuarzo es un cristal uniaxial positivo con
$n_e=1.553$ y $n_o=1.544$. (a) Determinar el retardo por mm a $\lambda_o=633$ nm cuando el cristal
se orienta de modo que el retardo sea máximo. (b) ¿A qué espesor(es) actúa el cristal como
retardador de cuarto de onda?

**6.3-2 Maximum Extraordinary Effect (p. 241).** Determinar la dirección de propagación en
cuarzo ($n_e=1.553$, $n_o=1.544$) para la cual el ángulo entre el vector de onda $\mathbf k$ y el
vector de Poynting $\mathbf S$ (que es también la dirección de propagación del rayo) es máximo.
*(Usado en la Tarea 2; es el ángulo de walk-off máximo.)*

**6.3-3 Double Refraction (p. 242).** Una onda plana no polarizada incide desde el vacío sobre
un cristal de cuarzo ($n_e=1.553$, $n_o=1.544$) a un ángulo de incidencia de 30°. El eje óptico
está en el plano de incidencia y es perpendicular a la dirección de la onda incidente antes de
entrar al cristal. Determinar las direcciones de los vectores de onda y de los rayos de las dos
componentes refractadas.

**6.3-4 Lateral Shift in Double Refraction (p. 242).** ¿Cuál es la geometría óptima para
maximizar el desplazamiento lateral entre los haces refractados ordinario y extraordinario en un
cristal uniaxial positivo? Indicar todos los ángulos y direcciones pertinentes.

**6.3-5 Transmission Through a LiNbO$_3$ Plate (p. 242).** Examinar la transmisión de un haz
láser He–Ne no polarizado ($\lambda_o=633$ nm) incidente normalmente sobre una lámina de LiNbO$_3$
($n_e=2.29$, $n_o=2.20$) de 1 cm de espesor, cortada de modo que su eje óptico forma 45° con la
normal a la lámina. Determinar el desplazamiento lateral a la salida de la lámina y el retardo
entre los haces ordinario y extraordinario.

**\*6.3-6 Conical Refraction (p. 242).** Cuando el vector de onda $\mathbf k$ apunta a lo largo de un
eje óptico de un cristal biaxial ocurre una situación inusual: las dos hojas de la superficie
$\mathbf k$ se encuentran y la superficie puede aproximarse por un cono. Considere un rayo
incidente normalmente sobre la superficie de un cristal biaxial para el cual uno de sus ejes
ópticos es también normal a la superficie. Mostrar que ocurre refracción múltiple con los rayos
refractados formando un cono (**refracción cónica**). ¿Qué ocurre cuando los rayos cónicos se
refractan desde la superficie paralela del cristal hacia el aire?

**6.6-1 Circular Dichroism (p. 242).** Ciertos materiales tienen coeficientes de absorción
distintos para luz circular derecha e izquierda, propiedad conocida como **dicroísmo circular**.
Determinar la matriz de Jones de un dispositivo que convierte luz de cualquier estado de
polarización en luz circularmente polarizada derecha.

**6.6-2 Polarization Rotation by a Sequence of Linear Polarizers (p. 242).** Una onda
linealmente polarizada en la dirección $x$ se transmite a través de una secuencia de $N$
polarizadores lineales cuyos ejes de transmisión están inclinados ángulos $m\theta$
($m=1,2,\dots,N$; $\theta=\pi/2N$) respecto al eje $x$. Mostrar que la luz transmitida está
linealmente polarizada en la dirección $y$ pero su amplitud se reduce por el factor $\cos^N\theta$.
¿Qué ocurre en el límite $N\to\infty$? *Pista:* usar matrices de Jones y notar que

$$\mathbf R[(m+1)\theta]\,\mathbf R(-m\theta)=\mathbf R(\theta),$$

donde $\mathbf R(\theta)$ es la matriz de transformación de coordenadas. *(Usado en la Tarea 2.)*

---

## Relación con Óptica No Lineal

**Con los temas del curso:**
- *Ondas EM y polarización (tema 3, central):* todo §6.1 (elipse, Stokes, Jones) es el
  lenguaje con el que se escriben los campos en los tensores no lineales: en
  $P_i^{(2)}=\epsilon_o\sum_{jk}\chi^{(2)}_{ijk}E_jE_k$ los índices $i,j,k$ son componentes de
  polarización sobre los ejes principales del cristal definidos en §6.3A (ecs. 6.3-5, 6.3-6).
  La descomposición en modos normales (6.1-26) y la regla de cascada $\mathbf T=\mathbf T_2\mathbf T_1$ se
  usan para cualquier montaje con láminas y polarizadores en el laboratorio.
- *Cristales y birrefringencia:* el elipsoide de índices (6.3-8) y $n(\theta)$ (6.3-15) son la
  base del **ajuste de fase por birrefringencia** (phase matching) en SHG/SFG/DFG/OPO: se
  busca $\theta$ tal que $n_e(\theta,2\omega)=n_o(\omega)$ (tipo I en uniaxial negativo) usando
  exactamente (6.3-15). El ángulo de walk-off (§6.3D, Fig. 6.3-12b, Prob. 6.3-2) limita la
  longitud efectiva de interacción y la calidad del haz armónico. Las superficies $\mathbf k$
  (6.3-18 a 6.3-21) son el punto de partida para entender la relación de dispersión
  $\omega(\mathbf k)$ y el desajuste $\Delta k$.
- *Susceptibilidad no lineal y tensores:* la discusión de tensores de rango 2, su
  representación cuádrica y la reducción por simetría (pp. 216–217) prepara la generalización
  a $\chi^{(2)}_{ijk}$ (rango 3) y $\chi^{(3)}_{ijkl}$ (rango 4), con las mismas ideas de ejes
  principales y reducción de coeficientes independientes por simetría cristalina
  (notación contraída $d_{il}$).
- *Índice dependiente de la intensidad / χ⁽³⁾:* el efecto Kerr óptico induce
  birrefringencia ($\Delta n\propto I$) — un retardador (6.1-19) controlado por la luz misma;
  la ec. (6.6-1) $\mathcal T=\sin^2(\Gamma/2)$ describe el "Kerr shutter" y, con $\Gamma$ inducido
  eléctricamente, los moduladores electro-ópticos (Pockels) que se usan como referencia.
  La rotación no lineal de polarización (elíptica) en fibras es el análogo χ⁽³⁾ de la actividad
  óptica (§6.4A, modos circulares con $n_\pm$).
- *Absorción y dispersión:* las ecuaciones de Fresnel con $\eta$ compleja (6.2-6/7),
  el Ejercicio 6.2-2 (Hagen–Rubens, Drude) y el Prob. 6.2-8 conectan con el tema de absorción y
  dispersión lineal (índice complejo $n-j\alpha c/2\omega$) que precede a la óptica no lineal.
- *Reflexión total interna y fases (6.2-11), (6.2-13):* fundamentan las guías de onda
  dieléctricas (§8.2) y los efectos de fase en acopladores; el Goos–Hänchen (Prob. 6.2-7) es un
  precursor de los efectos no lineales de superficie.
- *Pulsos en medios dispersivos, GVD, SPM, solitones, XPM, Raman, FWM:* la noción de velocidad
  de grupo $\mathbf v=\nabla_k\omega(\mathbf k)$ (p. 224) es la misma que gobierna $\beta_1=1/v_g$ y
  $\beta_2$ (GVD); en fibras birrefringentes (dos modos normales LP con $n_x\neq n_y$, §6.3B) la
  XPM entre polarizaciones y el FWM vectorial dependen del retardo $(n_2-n_1)k_od$ (p. 219), y
  la dispersión de modo de polarización (PMD) es birrefringencia residual. Los solitones
  vectoriales y la inestabilidad de modulación por polarización requieren el formalismo de
  Jones de §6.1B.
- *Dispositivos de laboratorio:* polarizadores de Brewster (§6.6A, Ej. 6.2-1: ventanas de
  Brewster en láseres), láminas λ/2 y λ/4 (§6.6B), aisladores de Faraday (§6.6D) para
  proteger el láser de bombeo: todo montaje de SHG o de supercontinuo los usa.

**Con el proyecto final (anillos add-drop en Si₃N₄, dispersión de guías, supercontinuo,
sensado de índice):**
- Los modos TE/TM de una guía Si₃N₄ son los "modos normales" de polarización de la
  estructura; su definición (campo $\mathcal E$ ortogonal/paralelo al plano de incidencia,
  p. 210) y las fases de reflexión total interna (6.2-11), (6.2-13) son el origen físico de la
  diferencia de $n_{\rm eff}$ y de dispersión entre TE y TM en la sección transversal
  (estudio `seccion_v1`).
- Las reflectancias de Fresnel (6.2-15), (6.2-17) y la reflectancia de lámina
  $\mathcal R(1+\mathcal T^2)$ (p. 214) sirven para estimar reflexiones en facetas de chip y en
  interfaces cladding/analito; la condición de Brewster y el carácter TM explican la
  sensibilidad distinta de cada polarización al índice del cladding (sensado volumétrico
  $n=1.33\to1.37$).
- La velocidad de grupo como gradiente de la relación de dispersión (p. 224) y la superficie
  $\mathbf k$ son la versión 3D de lo que, en la guía, se calcula como $n_g$, $\beta_2$ y el
  FSR del anillo; el supercontinuo depende de $\beta_2(\lambda)$ y de la polarización del modo
  bombeado, por lo que conviene fijar la polarización TE con los dispositivos de §6.6.
- Si el proyecto incorpora un modulador o un filtro de polarización, la ec. (6.6-1) y el
  rotador Faraday (aislador para el láser de bombeo) son las referencias de diseño.
