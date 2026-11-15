# Capítulo 11 — The Electrooptic and Photorefractive Effects (Boyd, 3.ª ed.)

Páginas del libro 511–541 (PDF 529–559). Leído el 2026-11-14.

Fuente: R. W. Boyd, *Nonlinear Optics*, 3.ª ed., Academic Press (Elsevier), 2008, cap. 11.
Las citas de página son páginas del libro (sumar 18 para la página del PDF). La p. 510 y la p. 542
están en blanco; el cap. 12 empieza en la p. 543.

**Convención del libro (SI).** $\tilde E(t)=E e^{-i\omega t}+\text{c.c.}$, $\tilde P(t)=\epsilon_0[\chi^{(1)}\tilde E+\chi^{(2)}\tilde E^2+\chi^{(3)}\tilde E^3+\cdots]$,
$I=2n\epsilon_0 c|E|^2$. El efecto electroóptico (EO) se formula, como es tradición, con el **tensor de
impermeabilidad** $\eta_{ij}=(\epsilon^{-1})_{ij}$ y los coeficientes $r_{ij}$ (m/V) en notación contraída, no con
$\chi^{(2)}$; la relación entre ambos es el Problema 3. En §11.5–11.7 el tratamiento es escalar, con
$\Delta(1/\epsilon)=r_{\rm eff}|E|$.

> **Lo esencial.** (i) Pockels ($\propto E$, solo medios no centrosimétricos, $\chi^{(2)}(\omega=\omega+0)$) y Kerr EO
> ($\propto E^2$, $\chi^{(3)}(\omega=\omega+0+0)$). (ii) Elipsoide de índices, $\Delta(1/n^2)_i=\sum_jr_{ij}E_j$, formas de $r_{ij}$
> para $\bar42m$, $3m$, $4mm$. (iii) KDP con campo longitudinal: $n_{x,y}=n_0\mp\tfrac12n_0^3r_{63}E_z$, retardo
> $\Gamma=\pi V/V_{\lambda/2}$ con $V_{\lambda/2}=\pi c/\omega n_0^3r_{63}$ (independiente de $L$), modulador de intensidad
> $T=\sin^2(\Gamma/2)$ con sesgo $\pi/2$, modulador de fase. (iv) Fotorrefractividad: no es un $\chi^{(n)}$;
> ecuaciones de Kukhtarev; campo de carga espacial desfasado 90° (difusión) → acoplamiento de dos
> haces $dI_s/dz=\Gamma I_sI_p/(I_s+I_p)$, $\Gamma=(\omega/c)n^3r_{\rm eff}E_m$; espejos conjugadores autobombeados.

---

## Resumen del capítulo

El capítulo trata dos efectos en los que el índice de refracción cambia por un campo eléctrico
estático (o de baja frecuencia). El efecto electroóptico lineal (Pockels) se puede describir con
$\chi^{(2)}(\omega=\omega+0)$ y existe solo en cristales no centrosimétricos; el cuadrático (Kerr electroóptico)
con $\chi^{(3)}(\omega=\omega+0+0)$. Boyd desarrolla el formalismo cristalográfico clásico: tensor dieléctrico
real y simétrico, ejes principales, densidad de energía y elipsoide de índices (indicatriz), tensor de
impermeabilidad $\eta_{ij}$, su desarrollo en potencias del campo aplicado con los tensores $r_{ijk}$ y
$s_{ijkl}$, la notación contraída $r_{hk}$ y las formas impuestas por la simetría para las clases $\bar42m$
(KDP, ADP), $3m$ (LiNbO₃) y $4mm$ (BaTiO₃), con una tabla de coeficientes. Como aplicación analiza el
modulador EO longitudinal de KDP: rotación de 45° de los ejes principales, índices $n_0\mp\tfrac12n_0^3r_{63}E_z$,
retardo proporcional al voltaje e independiente de la longitud, voltaje de media onda (~10 kV en el
visible), estados de polarización de salida, modulador de intensidad con polarizadores cruzados y
lámina $\lambda/4$ de sesgo (respuesta lineal alrededor de $T=50\%$) y modulador de fase. La segunda mitad
trata el efecto fotorrefractivo (redistribución de carga fotoinducida + Pockels): es una no linealidad
fuerte (mW bastan) pero lenta (~0.1 s), y no descriptible por ningún $\chi^{(n)}$ porque en estado
estacionario $\Delta n$ no depende de la intensidad. Se presenta el modelo de bandas de Kukhtarev *et al.*
(ecuaciones de tasa, corriente de deriva, difusión y fotovoltaica, ley de Gauss, $\Delta\epsilon=-\epsilon^2r_{\rm eff}|E|$),
se resuelve linealizado para un patrón de franjas de baja modulación (campo de difusión $E_D$, campo
de carga espacial máximo $E_q$, densidad efectiva de trampas, $q_{\rm opt}$ y $E_{\rm opt}$), se obtiene la
ganancia del acoplamiento de dos haces, el $r_{\rm eff}$ de BaTiO₃ y la respuesta transitoria con el tiempo de
relajación dieléctrica, y se termina con la mezcla de cuatro ondas fotorrefractiva (ecuaciones de
Cronin-Golomb) y los espejos conjugadores de fase autobombeados externa e internamente y el doble
espejo conjugador.

---

## Secciones

### 11.1 Introduction to the Electrooptic Effect (p. 511)

Efecto electroóptico: cambio del índice de refracción inducido por un campo eléctrico estático o de
baja frecuencia. Si el cambio es lineal en el campo, es el **efecto electroóptico lineal o de Pockels**,
descrito por

$$P_i(\omega)=2\epsilon_0\sum_{jk}\chi^{(2)}_{ijk}(\omega=\omega+0)E_j(\omega)E_k(0). \qquad (11.1.1),\ \text{p. 511}$$

Por §1.5, solo ocurre en materiales **no centrosimétricos**. Históricamente se usa otro formalismo
(§11.2). En materiales centrosimétricos (líquidos, vidrios) el cambio de orden más bajo es cuadrático:
**efecto Kerr electroóptico** o efecto EO cuadrático (nota al pie: a menudo "efecto Kerr" a secas; se
dice "electroóptico" para distinguirlo del Kerr magnetoóptico):

$$P_i(\omega)=3\epsilon_0\sum_{jkl}\chi^{(3)}_{ijkl}(\omega=\omega+0+0)E_j(\omega)E_k(0)E_l(0). \qquad (11.1.2),\ \text{p. 512}$$

### 11.2 Linear Electrooptic Effect (p. 512)

Material anisótropo:
$$D_i=\epsilon_0\sum_j\epsilon_{ij}E_j, \qquad (11.2.1a)$$
o en forma matricial $3\times3$ (11.2.1b). Para un material sin pérdidas y sin actividad óptica, $\epsilon_{ij}$ es
real y simétrico (el texto lo llama "dielectric permeability tensor"), con seis elementos
independientes ($\epsilon_{xx},\epsilon_{yy},\epsilon_{zz},\epsilon_{xy}=\epsilon_{yx},\epsilon_{xz}=\epsilon_{zx},\epsilon_{yz}=\epsilon_{zy}$). Toda matriz real simétrica se
diagonaliza con una transformación ortogonal: existe un sistema rotado $(X,Y,Z)$, el de **ejes
principales**, en el que

$$\begin{bmatrix}D_X\\D_Y\\D_Z\end{bmatrix}=\epsilon_0\begin{bmatrix}\epsilon_{XX}&0&0\\0&\epsilon_{YY}&0\\0&0&\epsilon_{ZZ}\end{bmatrix}\begin{bmatrix}E_X\\E_Y\\E_Z\end{bmatrix}. \qquad (11.2.2)$$

Densidad de energía de la onda:
$$U=\tfrac12\mathbf D\cdot\mathbf E=\tfrac12\epsilon_0\sum_{ij}\epsilon_{ij}E_iE_j, \qquad (11.2.3)$$
y en ejes principales (p. 513)
$$U=\frac{1}{2\epsilon_0}\left[\frac{D_X^2}{\epsilon_{XX}}+\frac{D_Y^2}{\epsilon_{YY}}+\frac{D_Z^2}{\epsilon_{ZZ}}\right]. \qquad (11.2.4)$$
Las superficies de $U$ constante en el espacio $\mathbf D$ son elipsoides. Con
$$X=\left(\frac{1}{2\epsilon_0U}\right)^{1/2}D_X,\quad Y=\left(\frac{1}{2\epsilon_0U}\right)^{1/2}D_Y,\quad Z=\left(\frac{1}{2\epsilon_0}\right)^{1/2}D_Z \qquad (11.2.5)$$
(*errata de lectura: en $Z$ falta la $U$; debe ser $(1/2\epsilon_0U)^{1/2}D_Z$*),
$$\frac{X^2}{\epsilon_{XX}}+\frac{Y^2}{\epsilon_{YY}}+\frac{Z^2}{\epsilon_{ZZ}}=1, \qquad (11.2.6)$$
la **indicatriz óptica** o **elipsoide de índices**. En un sistema cualquiera:
$$\left(\frac{1}{n^2}\right)_1x^2+\left(\frac{1}{n^2}\right)_2y^2+\left(\frac{1}{n^2}\right)_3z^2+2\left(\frac{1}{n^2}\right)_4yz+2\left(\frac{1}{n^2}\right)_5xz+2\left(\frac{1}{n^2}\right)_6xy=1. \qquad (11.2.7)$$
Uso (Born y Wolf 1975): para una dirección de propagación, el plano perpendicular al vector de
onda que pasa por el centro corta al elipsoide en una elipse; sus semiejes dan los dos índices
permitidos y sus orientaciones las direcciones de $\mathbf D$ correspondientes.

**Tensor de impermeabilidad** (p. 514):
$$E_i=\frac{1}{\epsilon_0}\sum_j\eta_{ij}D_j, \qquad (11.2.8)$$
inverso de (11.2.1a): $\eta_{ij}=(\epsilon^{-1})_{ij}$. Como $U=(1/2\epsilon_0)\sum_{ij}\eta_{ij}D_iD_j$, definiendo $x=D_x/(2\epsilon_0U)^{1/2}$, etc.:
$$1=\eta_{11}x^2+\eta_{22}y^2+\eta_{33}z^2+2\eta_{12}xy+2\eta_{23}yz+2\eta_{13}xz, \qquad (11.2.9)$$
y comparando con (11.2.7):
$$\Big(\tfrac{1}{n^2}\Big)_1=\eta_{11},\ \Big(\tfrac{1}{n^2}\Big)_2=\eta_{22},\ \Big(\tfrac{1}{n^2}\Big)_3=\eta_{33},\ \Big(\tfrac{1}{n^2}\Big)_4=\eta_{23}=\eta_{32},\ \Big(\tfrac{1}{n^2}\Big)_5=\eta_{13}=\eta_{31},\ \Big(\tfrac{1}{n^2}\Big)_6=\eta_{12}=\eta_{21}. \qquad (11.2.10)$$
Desarrollo en potencias del campo aplicado:
$$\eta_{ij}=\eta_{ij}^{(0)}+\sum_kr_{ijk}E_k+\sum_{kl}s_{ijkl}E_kE_l+\cdots, \qquad (11.2.11)$$
$r_{ijk}$: efecto EO lineal; $s_{ijkl}$: cuadrático. Como $\eta_{ij}$ es real y simétrico, $r_{ijk}$ es simétrico en sus dos
primeros índices → notación contraída $r_{hk}$ con
$$h=1\ (ij=11),\ 2\ (22),\ 3\ (33),\ 4\ (23\ \text{o}\ 32),\ 5\ (13\ \text{o}\ 31),\ 6\ (12\ \text{o}\ 21). \qquad (11.2.12)$$
Entonces (p. 515)
$$\Delta\left(\frac{1}{n^2}\right)_i=\sum_jr_{ij}E_j, \qquad (11.2.13a)$$
es decir, el vector columna $[\Delta(1/n^2)_1,\dots,\Delta(1/n^2)_6]^T$ es la matriz $6\times3$ de $r_{ij}$ por $[E_x,E_y,E_z]^T$ (11.2.13b).
Los $r_{ij}$ son los **coeficientes electroópticos**. Se anulan con simetría de inversión y, aun sin ella,
la simetría rotacional restringe su forma. En el sistema cristalográfico estándar ($Z$ = eje óptico):

- Clase $\bar42m$ (ADP, KDP): solo $r_{41}$ (fila 4, col. 1), $r_{52}=r_{41}$ y $r_{63}$:
$$r_{ij}=\begin{bmatrix}0&0&0\\0&0&0\\0&0&0\\r_{41}&0&0\\0&r_{41}&0\\0&0&r_{63}\end{bmatrix}\quad(\bar42m), \qquad (11.2.14)$$
15 coeficientes nulos y dos iguales: solo dos independientes.
- Clase $3m$ (niobato de litio), p. 516:
$$r_{ij}=\begin{bmatrix}0&-r_{22}&r_{13}\\0&r_{22}&r_{13}\\0&0&r_{33}\\0&r_{42}&0\\r_{42}&0&0\\r_{22}&0&0\end{bmatrix}\quad(3m). \qquad (11.2.15)$$
- Clase $4mm$ (titanato de bario):
$$r_{ij}=\begin{bmatrix}0&0&r_{13}\\0&0&r_{13}\\0&0&r_{33}\\0&r_{42}&0\\r_{42}&0&0\\0&0&0\end{bmatrix}\quad(4mm). \qquad (11.2.16)$$

Tabla 11.2.1 (p. 517): ver "Tablas y datos numéricos".

### 11.3 Electrooptic Modulators (p. 516)

Ejemplo con KDP (válido para toda la clase $\bar42m$). KDP es uniaxial; sin campo, en ejes cristalográficos,
$$\frac{X^2}{n_0^2}+\frac{Y^2}{n_0^2}+\frac{Z^2}{n_e^2}=1. \qquad (11.3.1)$$
Con campo, por (11.2.13b) y (11.2.14):
$$\frac{X^2}{n_0^2}+\frac{Y^2}{n_0^2}+\frac{Z^2}{n_e^2}+2r_{41}E_XYZ+2r_{41}E_YXZ+2r_{63}E_ZXY=1. \qquad (11.3.2)$$
Por los términos cruzados, $(X,Y,Z)$ ya no son ejes principales y el cristal deja de ser necesariamente
uniaxial (p. 517). Con campo solo en $Z$ (caso usual en dispositivos):
$$\frac{X^2}{n_0^2}+\frac{Y^2}{n_0^2}+\frac{Z^2}{n_e^2}+2r_{63}E_ZXY=1. \qquad (11.3.3)$$
Nuevos ejes principales $(x,y,z)$ por inspección (p. 518):
$$X=\frac{x-y}{\sqrt2},\quad Y=\frac{x+y}{\sqrt2},\quad Z=z, \qquad (11.3.4)$$
$$\left(\frac{1}{n_0^2}+r_{63}E_z\right)x^2+\left(\frac{1}{n_0^2}-r_{63}E_z\right)y^2+\frac{z^2}{n_e^2}=1, \qquad (11.3.5)$$
$$\frac{x^2}{n_x^2}+\frac{y^2}{n_y^2}+\frac{z^2}{n_e^2}=1, \qquad (11.3.6)$$
y en el límite realista $r_{63}E_z\ll1$ (desarrollando $(1/n_0^2\pm r_{63}E_z)^{-1/2}\approx n_0\mp\tfrac12n_0^3r_{63}E_z$):
$$n_x=n_0-\tfrac12n_0^3r_{63}E_z, \qquad (11.3.7a)$$
$$n_y=n_0+\tfrac12n_0^3r_{63}E_z. \qquad (11.3.7b)$$

Fig. 11.3.1 (p. 519): (a) cristal cortado con el eje óptico $Z$ perpendicular a la cara de entrada (que
contiene $X$ e $Y$); (b) campo longitudinal $E_z=V/L$ aplicado entre las caras frontal y trasera, con los
ejes principales $x,y$ girados 45°. Los electrodos son recubrimientos conductores delgados: históricamente
oro, más recientemente óxido de indio y estaño (ITO), transparente. (c) Intersección del elipsoide
con el plano $z=Z=0$: sin campo, un círculo (índice $n_0$ para toda polarización; la ausencia de
birrefringencia es una motivación principal para propagar a lo largo de $z$, nota al pie); con campo,
una elipse. En la figura se supuso $r_{63}E_z<0$, de modo que el semieje mayor está en $x$ ($n_x$) y el menor
en $y$ ($n_y<n_x$).

Para propagación en $z$, las componentes $x$ e $y$ acumulan la diferencia de fase (**retardo**)
$$\Gamma=(n_y-n_x)\frac{\omega L}{c}, \qquad (11.3.8)$$
y con (11.3.7), $\Gamma=n_0^3r_{63}E_z\omega L/c$. Como $E_z=V/L$, el retardo de un modulador longitudinal depende
solo del voltaje y no de la longitud (p. 520):
$$\Gamma=\frac{n_0^3r_{63}\omega V}{c}. \qquad (11.3.9)$$
**Voltaje de media onda**:
$$V_{\lambda/2}=\frac{\pi c}{\omega n_0^3r_{63}}, \qquad (11.3.10)$$
$$\Gamma=\pi\frac{V}{V_{\lambda/2}}. \qquad (11.3.11)$$
Para moduladores longitudinales, $V_{\lambda/2}$ típico ~10 kV en el visible.

Fig. 11.3.2 (estados de polarización de salida, entrada lineal vertical $X$): $\Gamma=0$ lineal vertical;
$\pi/4$ elipse vertical; $\pi/2$ circular; $3\pi/4$ elipse horizontal; $\pi$ lineal horizontal; $5\pi/4$ elipse horizontal
(sentido de giro opuesto); $3\pi/2$ circular (opuesto); $7\pi/4$ elipse vertical; $2\pi$ lineal vertical. Se puede
producir cualquier elipticidad controlando $V$ (p. 521; el texto dice "modular", errata por *modulator*).

**Modulador de intensidad** (Fig. 11.3.3): polarizador con eje en $X$ → cristal → lámina $\lambda/4$ con ejes
rápido y lento en $x$ e $y$ → polarizador en $Y$ (cruzado). La lámina añade el **retardo de sesgo**
$\Gamma_B=\pi/2$:
$$\Gamma=\pi\frac{V}{V_{\lambda/2}}+\frac{\pi}{2}. \qquad (11.3.12)$$
Campo tras el primer polarizador:
$$\tilde{\mathbf E}=\mathbf E_{\rm in}e^{-i\omega t}+\text{c.c.}, \qquad (11.3.13a)$$
$$\mathbf E_{\rm in}=E_{\rm in}\hat{\mathbf X}=\frac{E_{\rm in}}{\sqrt2}(\hat{\mathbf x}+\hat{\mathbf y}). \qquad (11.3.13b)$$
Tras cristal y lámina (salvo una fase global, p. 522):
$$\mathbf E=\frac{E_{\rm in}}{\sqrt2}(\hat{\mathbf x}+e^{i\Gamma}\hat{\mathbf y}). \qquad (11.3.14)$$
El polarizador final transmite $\hat{\mathbf Y}=(-\hat{\mathbf x}+\hat{\mathbf y})/\sqrt2$: $\mathbf E_{\rm out}=(\mathbf E\cdot\hat{\mathbf Y})\hat{\mathbf Y}$,
$$\mathbf E_{\rm out}=\frac{E_{\rm in}}{2}(-1+e^{i\Gamma})\hat{\mathbf Y}. \qquad (11.3.15)$$
$$T=\frac{|\mathbf E_{\rm out}|^2}{|\mathbf E_{\rm in}|^2}, \qquad (11.3.16)$$
$$T=\sin^2(\Gamma/2). \qquad (11.3.17)$$
(*Nota de lectura: $\hat{\mathbf X}=(\hat{\mathbf x}+\hat{\mathbf y})/\sqrt2$ y $\hat{\mathbf Y}=(-\hat{\mathbf x}+\hat{\mathbf y})/\sqrt2$ corresponden a la Fig. 11.3.1c; la transformación
(11.3.4) tal como está escrita daría $\hat{\mathbf X}=(\hat{\mathbf x}-\hat{\mathbf y})/\sqrt2$. Es una inconsistencia de signos sin efecto en $T$.*)

Fig. 11.3.4: $T$ frente a $\Gamma\in[0,\pi]$, sigmoide de 0 a 1 con tangente lineal en $\Gamma_B=\pi/2$. Con $V=0$, $T=50\%$ y
cerca de $\pi/2$ la transmisión varía casi linealmente con $V$. Con (p. 523)
$$V(t)=V_m\sin\omega_mt, \qquad (11.3.18)$$
$$\Gamma=\frac{\pi}{2}+\frac{\pi V_m}{V_{\lambda/2}}\sin\omega_mt, \qquad (11.3.19)$$
$$T=\sin^2\!\left(\frac{\pi}{4}+\frac{\pi V_m}{2V_{\lambda/2}}\sin\omega_mt\right)=\frac12\left[1+\sin\!\left(\frac{\pi V_m}{V_{\lambda/2}}\sin\omega_mt\right)\right],$$
y para $\pi V_m/V_{\lambda/2}\ll1$
$$T=\frac12\left(1+\frac{\pi V_m}{V_{\lambda/2}}\sin\omega_mt\right). \qquad (11.3.20)$$

**Modulador de fase.** Si la luz incide polarizada a lo largo de $x$ (o $y$), conserva su polarización y
solo adquiere una fase dependiente del voltaje:
$$\phi=(n_x-n_0)\frac{\omega L}{c}=-\frac{n_0^3r_{63}E_z\omega L}{2c}=\frac{n_0^3r_{63}V\omega}{2c}. \qquad (11.3.21)$$
(*Errata de lectura: el último miembro pierde el signo; debería ser $-n_0^3r_{63}V\omega/2c$.*)

### 11.4 Introduction to the Photorefractive Effect (p. 523)

El efecto fotorrefractivo es el cambio de índice debido a la redistribución ópticamente inducida de
electrones y huecos (nota al pie: Boyd usa el término en este sentido específico; en otras comunidades
designa cualquier cambio de índice inducido por luz). No puede describirse con un $\chi^{(n)}$ para ningún
$n$ (p. 524): en un amplio rango de condiciones, el cambio de índice en estado estacionario **no
depende de la intensidad** de la luz que lo induce. Por eso requiere métodos especiales. Da una no
linealidad fuerte (experimentos rutinarios con milivatios) pero lenta (tiempos de respuesta típicos de
0.1 s).

Origen (Fig. 11.4.1): dos haces de igual frecuencia se cruzan en el cristal y forman un patrón de
intensidad $I(x)$. Se generan portadores libres (electrones) por fotoionización a una tasa proporcional
a la intensidad local (p. 525). Pueden difundir o derivar con un campo estático; en la figura domina la
difusión, así que la densidad electrónica es mínima donde la intensidad es máxima. La densidad de
carga $\rho(x)$ crea un campo $E(x)$ cuyos máximos están desplazados 90° respecto a los de $\rho(x)$, porque
$\nabla\cdot\mathbf D=\rho$ da $dE/dx=\rho/\epsilon$. El cambio de índice $\Delta n(x)$ por Pockels (nota al pie: se supuso coeficiente
EO positivo; $\Delta(1/n^2)=r_{\rm eff}E$ implica $\Delta n=-\tfrac12n^3r_{\rm eff}E$) está desplazado 90° respecto a $I(x)$, lo que
permite la **transferencia de energía entre los haces** (§11.6). Tabla 11.4.1: ver "Tablas".

### 11.5 Photorefractive Equations of Kukhtarev *et al.* (p. 526)

Modelo de Kukhtarev y colaboradores (Kukhtarev *et al.* 1977, 1979; también en Günter y Huignard 1988),
Fig. 11.5.1. Un solo tipo de portador (electrón). El cristal tiene $N_A$ aceptores y $N_D^0$ donores por
unidad de volumen, $N_A\ll N_D^0$. Los aceptores están completamente llenos con electrones caídos de los
donores y no pueden ionizarse térmica ni ópticamente. A $T=0$ y sin luz hay $N_A$ donores ionizados,
$N_A$ electrones ligados a aceptores y $N_D^0-N_A$ donores neutros que participan en el efecto. Los
electrones pueden excitarse térmica u ópticamente del donor a la banda de conducción. $n_e$, $N_D^+$, $N_D$:
densidades de electrones de conducción, donores ionizados y donores sin ionizar; $N_D+N_D^+=N_D^0$, pero
$N_D^+\neq n_e$ en general (aceptores; migración → regiones no neutras).

Ecuaciones de tasa (p. 527):
$$\frac{\partial N_D^+}{\partial t}=(sI+\beta)(N_D^0-N_D^+)-\gamma n_eN_D^+, \qquad (11.5.1)$$
$$\frac{\partial n_e}{\partial t}=\frac{\partial N_D^+}{\partial t}+\frac1e(\nabla\cdot\mathbf j), \qquad (11.5.2)$$
con $s$ proporcional a la sección eficaz de fotoionización de un donor, $\beta$ la tasa de generación térmica,
$\gamma$ el coeficiente de recombinación, $-e$ la carga del electrón y $\mathbf j$ la densidad de corriente. (11.5.1):
los donores ionizados aumentan por ionización térmica u óptica y disminuyen por recombinación;
(11.5.2): los electrones móviles aumentan por ionización o por flujo hacia la región. Corriente:
$$\mathbf j=n_ee\mu\mathbf E+eD\nabla n_e+\mathbf j_{\rm ph}, \qquad (11.5.3)$$
$\mu$ movilidad, $D=k_BT\mu/e$ (relación de Einstein), $\mathbf j_{\rm ph}$ contribución **fotovoltaica** (o fotogalvánica):
la fotoionización expulsa el electrón en una dirección preferente en cristales anisótropos. Despreciable
en BaTiO₃ y en óxido de bismuto y silicio; muy importante en LiNbO₃, donde $\mathbf j_{\rm ph}=pI\hat{\mathbf c}$ ($\hat{\mathbf c}$ eje óptico, $p$
constante) (Glass 1978; Glass *et al.* 1974). El campo estático (aplicado o por separación de carga) cumple
$$\epsilon_{dc}\nabla\cdot\mathbf E=-e(n_e+N_A-N_D^+), \qquad (11.5.4)$$
$\epsilon_{dc}$ constante dieléctrica estática. Cambio de la constante dieléctrica óptica:
$$\Delta\epsilon=-\epsilon^2r_{\rm eff}|E|, \qquad (11.5.5)$$
en aproximación escalar (p. 528): la forma escalar de (11.2.13a) es $\Delta(1/\epsilon)=r_{\rm eff}|\mathbf E|$, de donde
$\Delta\epsilon=-\epsilon^2\Delta(1/\epsilon)$ da (11.5.5). El campo óptico cumple
$$\nabla^2\tilde E_{\rm opt}+\frac{1}{c^2}\frac{\partial^2}{\partial t^2}(\epsilon+\Delta\epsilon)\tilde E_{\rm opt}=0. \qquad (11.5.6)$$
(*Errata de lectura: se lee "+" ante el término temporal; la ecuación de onda es
$\nabla^2\tilde E-(1/c^2)\partial^2[(\epsilon+\Delta\epsilon)\tilde E]/\partial t^2=0$.*) Las ecs. (11.5.1)–(11.5.6) son las **ecuaciones fotorrefractivas de
Kukhtarev**, que describen adecuadamente la mayoría de los fenómenos fotorrefractivos.

### 11.6 Two-Beam Coupling in Photorefractive Materials (p. 528)

Dos haces pueden intercambiar energía en un cristal fotorrefractivo; sirve, p. ej., para amplificar
una señal débil portadora de imagen con un bombeo intenso. Ganancias exponenciales de 10 cm⁻¹ son
rutinarias. Geometría (Fig. 11.6.1, p. 529): señal $A_s$ y bombeo $A_p$ entran a ángulos $\pm\theta$ respecto a $z$, eje
$c$ a lo largo de $x$; la red de índice está desplazada respecto a la intensidad en la dirección $+c$ (o $-c$,
según el signo del portador dominante y de $r_{\rm eff}$), de modo que la luz dispersada de $A_p$ interfiere
constructivamente con $A_s$ y la de $A_s$ hacia $A_p$ destructivamente: la señal se amplifica y el bombeo se
atenúa. Campo:
$$\tilde E_{\rm opt}(\mathbf r,t)=\left[A_p(z)e^{i\mathbf k_p\cdot\mathbf r}+A_s(z)e^{i\mathbf k_s\cdot\mathbf r}\right]e^{-i\omega t}+\text{c.c.} \qquad (11.6.1)$$
Con $A_p$, $A_s$ lentamente variables, $I=n_0\epsilon_0c\langle\tilde E_{\rm opt}^2\rangle$:
$$I=I_0+(I_1e^{iqx}+\text{c.c.}), \qquad (11.6.2a)$$
$$I_0=2n_0\epsilon_0c(|A_p|^2+|A_s|^2),\quad I_1=2n_0\epsilon_0c(A_pA_s^*)(\hat{\mathbf e}_p\cdot\hat{\mathbf e}_s),\quad\mathbf q\equiv q\hat{\mathbf x}=\mathbf k_p-\mathbf k_s, \qquad (11.6.2b)$$
($\hat e_p$, $\hat e_s$ vectores de polarización lineal; $\mathbf q$ = **vector de red**). Equivalentemente
$$I=I_0[1+m\cos(qx+\phi)], \qquad (11.6.3)$$
con **índice de modulación** $m=2|I_1|/I_0$ y $\phi=\tan^{-1}(\text{Im}\,I_1/\text{Re}\,I_1)$.

Como (11.5.1)–(11.5.4) son no lineales (productos de $n_e$, $N_D^+$, $\mathbf j$, $\mathbf E$), se supone $m$ pequeño ($|I_1|\ll I_0$) y
se busca la solución estacionaria aproximada (p. 530)
$$E=E_0+(E_1e^{iqx}+\text{c.c.}),\quad j=j_0+(j_1e^{iqx}+\text{c.c.}),\quad n_e=n_{e0}+(n_{e1}e^{iqx}+\text{c.c.}),\quad N_D^+=N_{D0}^++(N_{D1}^+e^{iqx}+\text{c.c.}), \qquad (11.6.4)$$
con $\mathbf E=E\hat{\mathbf x}$, $\mathbf j=j\hat{\mathbf x}$, despreciando productos de cantidades de primer orden (en la última se lee
"$d^{iqx}$", errata por $e^{iqx}$). Orden cero (en el orden de (11.5.1)–(11.5.4)):
$$(sI_0+\beta)(N_D^0-N_{D0}^+)=\gamma n_{e0}N_{D0}^+, \qquad (11.6.5a)$$
$$j_0=\text{constante}, \qquad (11.6.5b)$$
$$j_0=n_{e0}e\mu E_0+j_{\rm ph,0}, \qquad (11.6.5c)$$
$$N_{D0}^+=n_{e0}+N_A. \qquad (11.6.5d)$$
Con $n_{e0}\ll N_A$ (caso realista):
$$N_{D0}^+=N_A, \qquad (11.6.6a)$$
$$n_{e0}=\frac{(sI_0+\beta)(N_D^0-N_A)}{\gamma N_A}. \qquad (11.6.6b)$$
Despreciando $j_{\rm ph}$, $E_0$ depende del circuito externo; sin voltaje aplicado, $E_0=j_0=0$. Primer orden
(con $E_0=0$), p. 531:
$$sI_1(N_D^0-N_A)-(sI_0+\beta)N_{D1}^+=\gamma n_{e0}N_{D1}^++\gamma n_{e1}N_A, \qquad (11.6.7a)$$
$$j_1=0, \qquad (11.6.7b)$$
$$-n_{e0}eE_1=iqk_BTn_{e1}, \qquad (11.6.7c)$$
$$iq\epsilon_0\epsilon_{dc}E_1=-e(n_{e1}-N_{D1}^+). \qquad (11.6.7d)$$
Resolviendo (con $n_{e0}\ll N_A$):
$$E_1=-i\left(\frac{sI_1}{sI_0+\beta}\right)\left(\frac{E_D}{1+E_D/E_q}\right), \qquad (11.6.8)$$
$$E_D=\frac{qk_BT}{e},\qquad E_q=\frac{e}{\epsilon_0\epsilon_{dc}q}N_{\rm eff}, \qquad (11.6.9)$$
con $N_{\rm eff}=N_A(N_D^0-N_A)/N_D^0$ (**densidad efectiva de trampas**; $\simeq N_A$ si $N_A\ll N_D^0$). $E_D$ = **campo de
difusión** (el necesario para inhibir la separación de carga por agitación térmica); $E_q$ = **campo de
carga espacial máximo** (el máximo que puede crear la redistribución de una carga de densidad media
$eN_{\rm eff}$ sobre la distancia $2\pi/q$). El factor $-i$ indica que $E_1$ está desfasado respecto a $I_1$; $E_1\propto m$ si
$\beta\ll sI_0$. Para maximizar $E_1$ (y $\Delta\epsilon$): aumentar $m$ (nota: la derivación vale solo para $m\ll1$) y elegir
$q$ óptimo:
$$E_1=-i\left(\frac{sI_1}{sI_0+\beta}\right)E_{\rm opt}\frac{2(q/q_{\rm opt})}{1+(q/q_{\rm opt})^2}, \qquad (11.6.10a)$$
$$q_{\rm opt}=\left(\frac{N_{\rm eff}e^2}{k_BT\epsilon_0\epsilon_{dc}}\right)^{1/2},\qquad E_{\rm opt}=\left(\frac{N_{\rm eff}k_BT}{4\epsilon_0\epsilon_{dc}}\right)^{1/2}. \qquad (11.6.10b),\ \text{p. 532}$$
$q_{\rm opt}$ es del orden del inverso de la longitud de apantallamiento de Debye. Fig. 11.6.2: $|E_1|$ frente a
$q/q_{\rm opt}$, crece linealmente, máximo en 1 y decae lentamente. $q$ se controla con el ángulo entre haces:
$$q=2n\frac{\omega}{c}\sin\theta, \qquad (11.6.11)$$
y midiendo el $q$ óptimo se obtiene $N_{\rm eff}$ con (11.6.10b).

**Ganancia.** Con $sI_0\gg\beta$ (caso usual) y (11.6.2):
$$E_1=-i\frac{A_pA_s^*}{|A_s|^2+|A_p|^2}(\hat e_p\cdot\hat e_s)E_m, \qquad (11.6.12a)$$
$$E_m=\frac{E_D}{1+E_D/E_q}. \qquad (11.6.12b)$$
Por (11.5.5), $\Delta\epsilon=-\epsilon^2r_{\rm eff}E_1$. Para la geometría de la Fig. 11.6.1 (Feinberg *et al.* 1980; Feinberg y MacDonald
1989), p. 533:
$$\epsilon^2r_{\rm eff}=\sum_{ijklm}r_{ijk}(\epsilon_{il}\hat e_l^s)(\epsilon_{jm}\hat e_m^p)\hat q_k, \qquad (11.6.13)$$
con $\hat e_l^s$, $\hat e_m^p$ componentes de las polarizaciones de señal y bombeo y $\hat q_k$ del vector unitario de la red.
Para la clase $4mm$ (BaTiO₃), ondas **ordinarias**:
$$r_{\rm eff}=r_{13}\sin\left(\frac{\alpha_s+\alpha_p}{2}\right), \qquad (11.6.14a)$$
y **extraordinarias**:
$$r_{\rm eff}=n^{-4}\left[n_0^4r_{13}\cos\alpha_s\cos\alpha_p+2n_e^2n_0^2r_{42}\cos\tfrac12(\alpha_s+\alpha_p)+n_e^4r_{33}\sin\alpha_s\sin\alpha_p\right]\sin\tfrac12(\alpha_s+\alpha_p), \qquad (11.6.14b)$$
$\alpha_s$, $\alpha_p$: ángulos entre los vectores de onda y el eje $+c$; $n$: índice del haz que se dispersa en la red.
Como en BaTiO₃ $r_{42}\gg r_{13},r_{33}$ (Tabla 11.2.1), solo con polarización extraordinaria se aprovecha $r_{42}$.

Polarización no lineal:
$$P^{\rm NL}=(\Delta\epsilon\,e^{i\mathbf q\cdot\mathbf r}+\text{c.c.})(A_se^{i\mathbf k_s\cdot\mathbf r}+A_pe^{i\mathbf k_p\cdot\mathbf r}). \qquad (11.6.15)$$
Con $\mathbf q=\mathbf k_p-\mathbf k_s$, los términos con ajuste de fase son
$$P_s^{\rm NL}=\Delta\epsilon^*A_pe^{i\mathbf k_s\cdot\mathbf r}=-i\epsilon^2r_{\rm eff}E_m\frac{|A_p|^2A_s}{|A_p|^2+|A_s|^2}e^{i\mathbf k_s\cdot\mathbf r}, \qquad (11.6.16a)$$
$$P_p^{\rm NL}=\Delta\epsilon A_se^{i\mathbf k_p\cdot\mathbf r}=i\epsilon^2r_{\rm eff}E_m\frac{|A_s|^2A_p}{|A_p|^2+|A_s|^2}e^{i\mathbf k_p\cdot\mathbf r}. \qquad (11.6.16b)$$
(Aquí $P^{\rm NL}$ aparece sin el factor $\epsilon_0$, con $\Delta\epsilon$ adimensional.) Ecuaciones acopladas (§2.1), con $z_s$, $z_p$
distancias a lo largo de cada haz, en SVA (p. 534):
$$2ik\frac{dA_s}{dz_s}e^{i\mathbf k_s\cdot\mathbf r}=-\frac{\omega^2}{c^2}P_s^{\rm NL}, \qquad (11.6.17a)$$
$$\frac{dA_s}{dz_s}=\frac{\omega}{2c}n^3r_{\rm eff}E_m\frac{|A_p|^2A_s}{|A_p|^2+|A_s|^2}. \qquad (11.6.17b)$$
Con $I_s=2n\epsilon_0c|A_s|^2$, $dI_s/dz_s=n\epsilon_0c(A_s^*dA_s/dz_s+\text{c.c.})$:
$$\boxed{\frac{dI_s}{dz_s}=\Gamma\frac{I_sI_p}{I_s+I_p},} \qquad (11.6.18a)$$
$$\Gamma=\frac{\omega}{c}n^3r_{\rm eff}E_m, \qquad (11.6.18b)$$
$$\frac{dI_p}{dz_p}=-\Gamma\frac{I_sI_p}{I_s+I_p}. \qquad (11.6.18c)$$
(Nota al pie: por convención se usa el mismo símbolo $\Gamma$ para la ganancia fotorrefractiva y el retardo
de §11.3.) Si $I_s\ll I_p$, la señal crece exponencialmente. Nota al pie: se supuso $\Gamma>0$; si $\Gamma<0$ se amplifica
la onda llamada "bombeo". El signo de $\Gamma$ depende del de $r_{\rm eff}$ y del de $E_m$, que según (11.6.9) y
(11.6.12b) depende del signo del portador dominante (aquí electrones) y de $q$ (componente $x$ de $\mathbf k_p-\mathbf k_s$).
En BaTiO₃ los portadores dominantes suelen ser huecos y se amplifica la onda con componente positiva
del vector de onda a lo largo de $+c$. Aplicación a polarizadores eficientes: Heebner *et al.* (2000).

**Régimen transitorio** (p. 535). Con las ecuaciones de Kukhtarev (Kukhtarev *et al.* 1977; Refrégier
*et al.* 1985; Valley 1987), suponiendo $n_e\ll N_D^+$, $N_D^+\ll N_D^0$ y $\beta\ll sI_0$:
$$\tau\frac{\partial E_1}{\partial t}+E_1=-iE_m\frac{A_pA_s^*}{|A_p|^2+|A_s|^2}(\hat e_p\cdot\hat e_s), \qquad (11.6.19)$$
$$\tau=\tau_d\frac{1+E_D/E_M}{1+E_D/E_q}, \qquad (11.6.20a)$$
$$\tau_d=\frac{\epsilon_0\epsilon_{dc}}{e\mu n_{e0}},\qquad E_M=\frac{\gamma N_A}{q\mu}. \qquad (11.6.20b)$$
$\tau$ escala con el **tiempo de relajación dieléctrica** $\tau_d$; como $n_{e0}$ crece linealmente con la intensidad
((11.6.6b)), la respuesta es más rápida a alta intensidad. Nota al pie (derivación de $\tau_d$): continuidad
$\partial\rho/\partial t=-\nabla\cdot\mathbf j$ con $\mathbf j=\sigma\mathbf E$ da $\partial\rho/\partial t=-\sigma\nabla\cdot\mathbf E=-(\sigma/\epsilon_0\epsilon_{dc})\nabla\cdot\mathbf D=-(\sigma/\epsilon_0\epsilon_{dc})\rho\equiv-\rho/\tau_d$,
con $\sigma=n_{e0}e\mu$. Ecuaciones acopladas en términos de $E_1$:
$$\frac{\partial A_p}{\partial x_p}=\frac{-\omega}{2n_pc}r_{\rm eff}A_sE_1, \qquad (11.6.21a)$$
$$\frac{\partial A_s}{\partial x_s}=\frac{-\omega}{2n_sc}r_{\rm eff}A_pE_1. \qquad (11.6.21b)$$
(*Duda de lectura: ambas se leen con $E_1$; por consistencia con (11.6.16), la ecuación de la señal
debería contener $E_1^*$. Las variables de propagación se escriben $x_p$, $x_s$ aunque antes eran $z_p$, $z_s$.*)
Las ecs. (11.6.19)–(11.6.21) describen el acoplamiento de dos haces transitorio.

### 11.7 Four-Wave Mixing in Photorefractive Materials (p. 536)

Geometría de la Fig. 11.7.1: bombeos 1 y 2 contrapropagantes, haces 3 y 4 contrapropagantes, ángulos
$\theta_1$, $\theta_4$, cristal entre $z=0$ y $z=l$, eje $c$ transversal. El haz 4 puede generarse como el **conjugado de
fase** del 3. En general hay cuatro redes: 1–3 junto con 2–4; 1–4 junto con 2–3; 1–2; y 3–4 (el texto dice
"inference", errata por *interference*). Si las polarizaciones, direcciones y coherencia se eligen de modo
que solo importe la red 1–3/2–4 (Cronin-Golomb *et al.* 1984; ver también Fischer *et al.* 1981):
$$\frac{dA_1}{dz}=-\frac{\gamma}{S_0}(A_1A_3^*+A_2^*A_4)A_3-\alpha A_1, \qquad (11.7.1a)$$
$$\frac{dA_2}{dz}=-\frac{\gamma}{S_0}(A_1^*A_3+A_2A_4^*)A_4+\alpha A_2, \qquad (11.7.1b)$$
$$\frac{dA_3}{dz}=\frac{\gamma}{S_0}(A_1^*A_3+A_2A_4^*)A_1-\alpha A_3, \qquad (11.7.1c),\ \text{p. 537}$$
$$\frac{dA_4}{dz}=\frac{\gamma}{S_0}(A_1A_3^*+A_2^*A_4)A_2+\alpha A_4, \qquad (11.7.1d)$$
$$\gamma=\frac{\omega r_{\rm eff}n_0^3E_m}{2c\cos\theta}, \qquad (11.7.2a)$$
$$S_0=\sum_{i=1}^4|A_i|^2, \qquad (11.7.2b)$$
con $E_m$ de (11.6.12b), $\alpha=\tfrac12\alpha_0/\cos\theta$ ($\alpha_0$ coeficiente de absorción de intensidad) y $\theta=\theta_1=\theta_4$. Aquí
$\gamma$ es el acoplamiento (no el coeficiente de recombinación). Cronin-Golomb *et al.* (1984) las resolvieron
para muchos casos: reflexión amplificada, autooscilación y biestabilidad.

#### 11.7.1 Externally Self-Pumped Phase-Conjugate Mirror (p. 537)

Fig. 11.7.2: solo la señal $A_3$ se aplica desde fuera; $A_1$ y $A_2$ crecen desde el ruido en un resonador
(dos espejos) que rodea el cristal. Oscila porque $A_1$ se amplifica a costa de $A_3$ por acoplamiento de dos
haces; la salida $A_4$ (conjugado de $A_3$) se genera por mezcla de cuatro ondas con $A_1$, $A_2$ y $A_3$ (p. 538).
Construido por White *et al.* (1982); descrito por Cronin-Golomb *et al.* (1984).

#### 11.7.2 Internally Self-Pumped Phase-Conjugate Mirror (p. 538)

Fig. 11.7.3: solo $A_3$ se aplica; por un proceso no lineal complicado, análogo al autoenfoque, se crean
$A_1$ y $A_2$, que se reflejan en la esquina del cristal y vuelven al camino de $A_3$; la mezcla de cuatro ondas
genera $A_4$, conjugado de $A_3$. Demostrado por Feinberg (1982), analizado por MacDonald y Feinberg (1983).
Puede mostrar dinámica complicada, incluido caos determinista (Gauthier *et al.* 1987). Por la facilidad
para producir una señal conjugada, se usa en nuevos tipos de interferómetros (Gauthier *et al.* 1989).

#### 11.7.3 Double Phase-Conjugate Mirror (p. 538)

Fig. 11.7.4 (p. 539): $A_2$ y $A_3$ se aplican desde fuera y son mutuamente **incoherentes** (no forman red entre
ellas). Se generan $A_1$, conjugado de $A_2$, y $A_4$, conjugado de $A_3$; pero $A_1$ es coherente en fase con $A_3$ y
$A_4$ con $A_2$. Propiedad notable: una salida puede ser una onda conjugada amplificada aunque las entradas
sean incoherentes. Con $\alpha$ despreciable y $A_2$, $A_3$ sin modificar, basta con (11.7.1a) y (11.7.1d): cada salida
tiene un término de acoplamiento de dos haces (que la amplifica) y otro de mezcla de cuatro ondas
(que la hace conjugada de su entrada). Condición para generar las dos salidas: $|\gamma|l>2$ (Cronin-Golomb
*et al.* 1984; Weiss *et al.* 1987). Demostrado experimentalmente por Weiss *et al.* (1987).

#### 11.7.4 Other Applications of Photorefractive Nonlinear Optics (p. 539)

Revisiones de aplicaciones: Günter y Huignard (1988, 1989), Boyd y Grynberg (1992). Solitones espaciales
fotorrefractivos: Królikowski *et al.* (2003).

---

## Tablas y datos numéricos útiles

**Tabla 11.2.1** (p. 517). Propiedades de materiales electroópticos (varias fuentes, p. ej. Thompson y
Hartfield 1978, Cook y Jaffe 1979). Coeficientes en $10^{-12}$ m/V (MKS); para pasar a cgs (cm/statvolt)
multiplicar por $3\times10^4$.

| Material | Grupo puntual | Coeficientes EO ($10^{-12}$ m/V) | Índices |
|---|---|---|---|
| KH₂PO₄ (KDP) | $\bar42m$ | $r_{41}=8.77$, $r_{63}=10.5$ | $n_0=1.514$, $n_e=1.472$ (0.5461 µm) |
| KD₂PO₄ (KD*P) | $\bar42m$ | $r_{41}=8.8$, $r_{63}=26.4$ | $n_0=1.508$, $n_e=1.468$ (0.5461 µm) |
| LiNbO₃ | $3m$ | $r_{13}=9.6$, $r_{22}=6.8$, $r_{33}=30.9$, $r_{42}=32.6$ | $n_0=2.3410$, $n_e=2.2457$ (0.5 µm) |
| LiTaO₃ | $3m$ | $r_{13}=8.4$, $r_{22}=-0.2$, $r_{33}=30.5$, $r_{51}=20$ | $n_0=2.176$, $n_e=2.180$ ("0.633 nm", errata por µm) |
| BaTiO₃ ᵇ | $4mm$ | $r_{13}=19.5$, $r_{33}=97$, $r_{42}=1640$ | $n_0=2.488$, $n_e=2.424$ (514 nm) |
| Sr₀.₆Ba₀.₄NbO₆ (SBN:60) | $4mm$ | $r_{13}=55$, $r_{33}=224$, $r_{42}=80$ | $n_0=2.367$, $n_e=2.337$ (514 nm) |
| ZnTe | $\bar43m$ | $r_{41}=4.0$ | $n_0=2.99$ (0.633 µm) |

ᵇ $\epsilon_{dc}^\parallel=135$, $\epsilon_{dc}^\perp=3700$. (La fórmula de SBN se lee "Sr₀.₆Ba₀.₄NbO₆"; la habitual es Sr₀.₆Ba₀.₄Nb₂O₆.)

**Tabla 11.4.1** (p. 525). Propiedades de cristales fotorrefractivos (adaptada de Glass *et al.* 1984; $\tau$:
tiempo de recombinación de portadores; $\tau_d$: tiempo de relajación dieléctrica en oscuridad).

| Material | λ útil (µm) | Deriva $\mu\tau E$ a $E=2$ kV/cm (µm) | $\tau_d$ (s) | $n^3r_{\rm eff}$ (pm/V) | $n^3r_{\rm eff}/\epsilon_{dc}$ (pm/V) |
|---|---|---|---|---|---|
| InP:Fe | 0.85–1.3 | 3 | $10^{-4}$ | 52 | 4.1 |
| GaAs:Cr | 0.8–1.8 | 3 | $10^{-4}$ | 43 | 3.3 |
| LiNbO₃:Fe³⁺ | 0.4–0.7 | $<10^{-4}$ | 300 | 320 | 11 |
| Bi₁₂SiO₂₀ | 0.4–0.7 | 3 | $10^{5}$ | 82 | 1.8 |
| Sr₀.₄Ba₀.₆Nb₂O₆ | 0.4–0.6 | — | $10^{2}$ | 2460 | 4.0 |
| BaTiO₃ | 0.4–0.9 | 0.1 | $10^{2}$ | 11 300 | 4.9 |
| "KNbBO₃" (KNbO₃) | 0.4–0.7 | 0.3 | $10^{-3}$ | 690 | 14 |

**Otros números:** $V_{\lambda/2}$ de moduladores longitudinales ~10 kV en el visible (p. 520); respuesta
fotorrefractiva típica ~0.1 s y potencias de mW (p. 524); ganancia de dos haces ~10 cm⁻¹ (p. 528); umbral
del doble espejo conjugador $|\gamma|l>2$ (p. 539).

**Ejemplo numérico propio (no del libro), para fijar órdenes:** KDP, $\lambda=546$ nm, $n_0=1.514$,
$r_{63}=10.5$ pm/V: $V_{\lambda/2}=\pi c/(\omega n_0^3r_{63})=\lambda/(2n_0^3r_{63})=546\times10^{-9}/(2\times3.47\times10.5\times10^{-12})\approx7.5$ kV,
consistente con el "~10 kV" del texto.

---

## Problemas al final del capítulo (p. 540)

1. *Numerical evaluation of photorefractive quantities.* Considere el acoplamiento de dos haces en titanato
   de bario en la geometría de la Fig. 11.6.1. Estime los valores numéricos de $E_D$, $E_q$, $E_{\rm opt}$, $E_1$, $r_{\rm eff}$,
   $\Delta\epsilon$ y $\Gamma$. Suponga que la densidad efectiva de trampas $N_{\rm eff}$ es $10^{12}$ cm⁻³, que la tasa de generación
   térmica es despreciable, que el índice de modulación $m$ es $10^{-3}$ y que $\theta_s=\theta_p=5$ grados.
2. *Transient two-beam coupling.* Verifique la ec. (11.6.19).
3. *Relation between electrooptic and nonlinear optics tensors.* Determine la relación matemática entre la
   susceptibilidad de segundo orden $\chi^{(2)}_{ijk}$ y el coeficiente electroóptico lineal $r_{ijk}$. Análogamente,
   determine la relación entre la susceptibilidad de tercer orden $\chi^{(3)}_{ijkl}$ y el coeficiente electroóptico
   cuadrático $s_{ijkl}$.

## Referencias principales (p. 540–541)

- *Efecto EO:* Born y Wolf (1975) *Principles of Optics*; Cook y Jaffe (1979), Landolt–Börnstein, New Series,
  Vol. II, pp. 552–651; Thompson y Hartfield (1978), *Handbook of Optics*. Lecturas: Kaminow (1974) *An
  Introduction to Electrooptic Devices*; Yariv y Yeh (1984) *Optical Waves in Crystals*.
- *Fotorrefractivo:* Boyd y Grynberg (1992), *Contemporary Nonlinear Optics*; Cronin-Golomb, Fischer, White y
  Yariv (1984) IEEE JQE 20, 12; Feinberg (1982) Opt. Lett. 7, 486; Feinberg y MacDonald (1989), en Günter y
  Huignard, Vol. II; Feinberg, Heiman, Tanguay y Hellwarth (1980) J. Appl. Phys. 5[1], 1297; Fischer *et al.*
  (1981) Opt. Lett. 6, 519; Gauthier, Narum y Boyd (1987) PRL 58, 16; Gauthier *et al.* (1989) Opt. Lett. 14,
  325; Glass (1978) Opt. Eng. 17, 470; Glass *et al.* (1984) APL 44, 948; Glass, von der Linde y Negran (1974)
  APL 25, 233; Günter y Huignard (Eds.) (1988, 1989) *Photorefractive Materials and Their Applications*
  I y II; Heebner, Bennink, Boyd y Fisher (2000) Opt. Lett. 25, 257; Królikowski, Luther-Davies y Denz (2003)
  IEEE JQE 39, 3; Kukhtarev, Markov y Odulov (1977) Opt. Commun. 23, 338; Kukhtarev *et al.* (1979)
  Ferroelectrics 22, 949–960, 961–964; MacDonald y Feinberg (1983) JOSA 73, 548; Refrégier *et al.* (1985)
  J. Appl. Phys. 58, 45; Valley (1987) JOSA B 4, 14, 934; Weiss, Sternklar y Fischer (1987) Opt. Lett. 12, 114;
  White, Cronin-Golomb, Fischer y Yariv (1982) APL 40, 450.

---

## Relación con Óptica No Lineal

- **Programa del curso.** Conecta con el tema 5 (Boyd cap. 2 y §1.5, simetría y $\chi^{(2)}$): el Pockels es el
  caso límite $\chi^{(2)}(\omega=\omega+0)$ de la mezcla de tres ondas (rectificación óptica y Pockels como pares de
  procesos) y requiere no centrosimetría; el Problema 3 pide la relación $\chi^{(2)}\leftrightarrow r$ (resultado
  esperado, deducción propia no del libro: de $\Delta\epsilon_{ij}=-\sum_k n_i^2n_j^2r_{ijk}E_k(0)$ en ejes principales y
  $P_i=\epsilon_0\Delta\epsilon_{ij}E_j(\omega)$ comparado con (11.1.1) sale $\chi^{(2)}_{ijk}(\omega=\omega+0)=-\tfrac12n_i^2n_j^2r_{ijk}$; en otros textos aparece
  $-\tfrac14$ según cómo se defina la amplitud del campo estático, así que hay que revisar factores y signos). El Kerr EO es el análogo estático del índice no lineal $n_2$ del tema 6 (Boyd 4.1). La mezcla de
  cuatro ondas fotorrefractiva y los espejos conjugadores enlazan con Boyd 7.1–7.2 (conjugación de fase),
  también del tema 6.
- **Proyecto final (SiN/Si).** Si y Si₃N₄ amorfo son centrosimétricos: no tienen Pockels intrínseco (el
  Si se modula por dispersión de plasma y efectos térmicos; el SiN muestra $\chi^{(2)}$ efectivo solo por
  campos congelados, interfaces o poling inducido por luz, lo que se usa para SHG en microanillos). El
  formalismo de §11.3 (retardo, $V_{\lambda/2}$, $T=\sin^2(\Gamma/2)$) es el mismo que se usa para moduladores de LiNbO₃
  en película delgada y para sintonizar anillos con $V_\pi L$; la ecuación de transferencia es directamente
  análoga a la de un interferómetro Mach–Zehnder. El refractómetro del proyecto (anillo add-drop) no usa
  efectos EO, pero la Tabla 11.2.1 sirve como referencia de órdenes de magnitud si se compara con
  sintonía EO.

---

## Erratas y dudas de lectura (resumen)

1. (11.2.5), p. 513: en $Z=(1/2\epsilon_0)^{1/2}D_Z$ falta $U$.
2. p. 512: "dielectric permeability tensor" para $\epsilon_{ij}$ (se refiere a la permitividad).
3. (11.3.4) vs. (11.3.13b), p. 518/521: signos de la rotación de 45° inconsistentes entre la ecuación y
   la figura/vectores unitarios (sin efecto en $T$).
4. p. 520: "modular" → *modulator*.
5. (11.3.21), p. 523: último miembro sin el signo menos.
6. (11.5.6), p. 528: signo "+" ante el término $\partial^2/\partial t^2$; debería ser "−".
7. (11.6.4), p. 530: "$N_{D1}^+d^{iqx}$" → $e^{iqx}$.
8. (11.6.21), p. 535: ambas ecuaciones con $E_1$; la de la señal debería llevar $E_1^*$ (duda); variables $x_p$, $x_s$
   en lugar de $z_p$, $z_s$.
9. p. 536: "inference" → *interference*.
10. Tabla 11.2.1: LiTaO₃ "at 0.633 nm" → µm; SBN "NbO₆" → Nb₂O₆. Tabla 11.4.1: "KNbBO₃" → KNbO₃.
11. Referencias: Feinberg *et al.* (1980) J. Appl. Phys. se lee volumen "5" (probablemente 51).
