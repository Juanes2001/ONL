# Capítulo 7 — Processes Resulting from the Intensity-Dependent Refractive Index (Boyd, 3.ª ed.)

Páginas del libro 329–390 (PDF 347–408). Leído el 2026-11-14.

Fuente: R. W. Boyd, *Nonlinear Optics*, 3.ª ed., Academic Press, 2008, cap. 7. Las citas de página son páginas del
libro (sumar 18 para la página del PDF).

Convención (SI, la del libro): $\tilde E(t)=Ee^{-i\omega t}+{\rm c.c.}$, $\tilde P=\epsilon_0[\chi^{(1)}\tilde E+\chi^{(2)}\tilde E^2+\chi^{(3)}\tilde E^3+\dots]$,
$I=2n\epsilon_0c|E|^2$, $n=n_0+n_2I=n_0+2\bar n_2|E|^2$ con $\bar n_2=3\chi^{(3)}/4n_0$ y $n_2=3\chi^{(3)}/(4n_0^2\epsilon_0c)$ (§4.1).
Ondas $e^{i(kz-\omega t)}$. Los comentarios entre corchetes [ ] son míos (verificaciones o notas), no del libro.

Secciones: 7.1 autoenfoque y autoacción (p. 329); 7.2 conjugación de fase óptica (p. 342); 7.3 biestabilidad y
conmutación óptica (p. 359); 7.4 acoplamiento de dos haces (p. 369); 7.5 propagación de pulsos y solitones temporales
(p. 375); problemas (p. 383); referencias (p. 388).

---

## Resumen del capítulo

El capítulo estudia los procesos de importancia práctica que resultan del índice de refracción dependiente de la
intensidad, $n=n_0+n_2I$, introducido en el cap. 4. La §7.1 trata los **efectos de autoacción** de un haz en el
espacio: el **autoenfoque** (el medio con $n_2>0$ actúa como lente positiva; ángulo $\theta_{\rm sf}=\sqrt{2n_2I/n_0}$ y
distancia $z_{\rm sf}\propto1/\sqrt{P/P_{\rm cr}-1}$ obtenidos con el principio de Fermat), el **autoatrapamiento**, que exige que la
potencia sea igual a la potencia crítica $P_{\rm cr}=\pi(0.61)^2\lambda_0^2/8n_0n_2$ (balance difracción/autoenfoque, o
reflexión total interna en la guía autoinducida), el **solitón espacial** sech en una dimensión transversal como
solución exacta de la ecuación paraxial con $\chi^{(3)}$ (inestable en 2D en medios Kerr puros, estable en medios
saturables), la **ruptura del haz en filamentos** (análisis de Bespalov–Talanov: inestabilidad modulacional
espacial por mezcla de cuatro ondas hacia adelante, ganancia $\Lambda=\sqrt{\beta(2\gamma-\beta)}$ con máximo $\gamma$ en
$q_{\rm opt}=\sqrt{2k\gamma}$, filamentos de potencia $\sim P_{\rm cr}$, umbral $P\approx4G^2P_{\rm cr}$) y los efectos con pulsos
(foco móvil y autoenfoque transitorio). La §7.2 desarrolla la **conjugación de fase óptica**: el espejo conjugador
ideal produce $r\mathbf E_s^*$ (onda invertida en el tiempo), corrige aberraciones en doble paso (demostrado con la
ecuación paraxial y su conjugada), y se realiza por **mezcla de cuatro ondas degenerada** con bombeos
contrapropagantes, automáticamente en ajuste de fase, con reflectividad $\tan^2|\kappa|L$ que puede superar 100 %; se
discuten las propiedades de polarización (conjugación vectorial con $\chi_{1122}=0$ o con bombeos circulares
contrarrotantes). La §7.3 trata la **biestabilidad óptica** en un Fabry–Perot no lineal (absortiva, con número de
cooperación $C_0>8$, y refractiva) y la **conmutación totalmente óptica** en un Mach–Zehnder, que exige un desfase no
lineal de $\pi$ y está limitada por la absorción lineal ($L_{\rm eff}$) y la absorción de dos fotones. La §7.4 muestra que
el **acoplamiento de dos haces** requiere una respuesta no instantánea (relajación de Debye) y diferencia de
frecuencias, con ganancia $\propto\delta\tau/(1+\delta^2\tau^2)$. La §7.5 deriva la **automodulación de fase** (frecuencia
instantánea, corrimiento al rojo del flanco anterior y al azul del posterior con $n_2>0$), la **ecuación no lineal de
Schrödinger** para la envolvente en tiempo retardado y el **solitón temporal fundamental** sech, que exige $k_2n_2<0$
(dispersión anómala, $\lambda>1.3\ \mu$m en sílice).

---

## 7.1 Self-Focusing of Light and Other Self-Action Effects — autoenfoque y otros efectos de autoacción (p. 329)

**Definiciones (p. 329–330).** *Autoenfoque* (Kelly, 1965): un haz intenso modifica el medio de modo que
el propio haz se enfoca dentro del material. Con $n_2>0$ el índice es mayor en el centro del haz que en la
periferia y el medio actúa como lente positiva (Fig. 7.1.1a). *Efectos de autoacción*: el haz modifica su
propia propagación a través de la respuesta no lineal. *Autoatrapamiento* (self-trapping, Fig. 7.1.1b): el
haz se propaga con diámetro constante por balance exacto entre autoenfoque y difracción; ocurre solo si la
potencia es exactamente la **potencia crítica**

$$P_{\rm cr}=\frac{\pi(0.61)^2\lambda_0^2}{8n_0n_2},\qquad (7.1.1),\ \text{p. 329}$$

con $\lambda_0$ la longitud de onda en el vacío. El autoenfoque solo ocurre si $P>P_{\rm cr}$.
*Ruptura del haz* (laser beam breakup, Fig. 7.1.1c): para $P\gg P_{\rm cr}$ el haz se rompe en muchas
componentes (filamentos), cada una con potencia $\approx P_{\rm cr}$; se debe al crecimiento de las
imperfecciones del frente de onda por la amplificación de la **mezcla de cuatro ondas hacia adelante**.
Nota al pie (p. 330): "filamentación" se usa ambiguamente (haz autoatrapado o ruptura cuasi‑aleatoria); Boyd
evita la palabra y habla de *haces autoatrapados* y de *ruptura del haz*.

**Modelo simple sin difracción (p. 330–331).** Válido si el diámetro o la intensidad del haz (o ambos) son
suficientemente grandes. Haz colimado de radio $w_0$ e intensidad en el eje $I_0$ sobre un medio con $n_2>0$
(Fig. 7.1.2). Por el principio de Fermat (camino óptico $\int n(\mathbf r)\,dl$ igual para todos los rayos
entre el frente de onda de entrada y el autofoco), tomando $n_0$ en el rayo marginal y $n_0+n_2I_0$ en el
rayo central, y aproximando las trayectorias curvas por rectas:

$$(n_0+n_2I)z_{\rm sf}=n_0z_{\rm sf}/\cos\theta_{\rm sf}\qquad(7.1.2),\ \text{p. 331}$$

Con $\cos\theta_{\rm sf}\approx1-\tfrac12\theta_{\rm sf}^2$ se obtiene el **ángulo de autoenfoque**

$$\theta_{\rm sf}=\sqrt{2n_2I/n_0}.\qquad(7.1.3)$$

Se interpreta como el ángulo característico con que un haz se desvía por efectos de autoacción; como
$n_2I/n_0$ es siempre pequeño, la aproximación paraxial está justificada. La **distancia de autoenfoque**
$z_{\rm sf}=w_0/\theta_{\rm sf}$:

$$z_{\rm sf}=w_0\sqrt{\frac{n_0}{2n_2I}}=\frac{2n_0w_0^2}{\lambda_0}\frac{1}{\sqrt{P/P_{\rm cr}}}\qquad(P\gg P_{\rm cr}),\qquad(7.1.4)$$

donde la segunda forma usa (7.1.1). Al ignorar la difracción, (7.1.4) vale cuando la autoacción domina,
$P\gg P_{\rm cr}$. Para potencias menores, la difracción reduce el ángulo de convergencia a
$\theta=(\theta_{\rm sf}^2-\theta_{\rm dif}^2)^{1/2}$, con el ángulo de difracción de un haz de diámetro $d$

$$\theta_{\rm dif}=0.61\lambda_0/n_0d,\qquad(7.1.5),\ \text{p. 332}$$

y de nuevo con $z_{\rm sf}=w_0/\theta$:

$$z_{\rm sf}=\frac{2n_0w_0^2}{\lambda_0}\frac{1}{\sqrt{P/P_{\rm cr}-1}}.\qquad(7.1.6)$$

Yariv (1975): para potencia y posición de cintura arbitrarias,

$$z_{\rm sf}=\frac{\tfrac12kw^2}{(P/P_{\rm cr}-1)^{1/2}+2z_{\rm min}/kw_0^2},\qquad(7.1.7)$$

con $k=n_0\omega/c$; $w$ es el radio del haz en la cara de entrada, $w_0$ el radio en la cintura y $z_{\rm min}$
la distancia de la cara de entrada a la cintura (Fig. 7.1.3, rayos dibujados sin la interacción no lineal).

### 7.1.1 Self-Trapping of Light — autoatrapamiento (p. 332)

Condición: el ángulo de difracción iguala al de autoenfoque,

$$\theta_{\rm dif}=\theta_{\rm sf}.\qquad(7.1.8)$$

Con (7.1.3) y (7.1.5), la intensidad necesaria es

$$I=\frac{(0.61)^2\lambda_0^2}{2n_2n_0d^2},\qquad(7.1.9),\ \text{p. 333}$$

y como $P=(\pi/4)d^2I$, la potencia toma el valor crítico

$$P_{\rm cr}=\frac{\pi(0.61)^2\lambda_0^2}{8n_0n_2}\approx\frac{\lambda_0^2}{8n_0n_2}.\qquad(7.1.10)$$

(Esto demuestra (7.1.1).) En este modelo un haz autoatrapado puede tener **cualquier diámetro** $d$ y la
potencia del filamento es siempre la misma. El coeficiente numérico depende del modelo matemático detallado
(Fibich y Gaeta, 2000). [Nota: $\pi(0.61)^2=1.17\approx1$, de ahí la aproximación.]

**Argumento de Chiao et al. (1964), reflexión total interna (p. 333–334).** Haz de perfil plano ("flat-top")
de diámetro $d$ (Fig. 7.1.4a); el índice es $n_0+\delta n$ dentro del haz y $n_0$ fuera (Fig. 7.1.4b), formando
una guía de onda autoinducida. Un rayo queda atrapado si sufre reflexión total en la frontera, es decir si su
ángulo (medido respecto a la frontera) es menor que el ángulo crítico $\theta_0$:

$$\cos\theta_0=\frac{n_0}{n_0+\delta n}.\qquad(7.1.11)$$

Como $\delta n\ll n_0$, $\theta_0\ll1$ y $1-\tfrac12\theta_0^2=1-\delta n/n_0$, de donde

$$\theta_0=(2\delta n/n_0)^{1/2}.\qquad(7.1.12),\ \text{p. 334}$$

Un haz de diámetro $d$ contiene rayos en un cono de extensión $\sim\theta_{\rm dif}=0.61\lambda_0/n_0d$; hay
autoatrapamiento si todos sufren reflexión total, $\theta_{\rm dif}=\theta_0$:

$$\delta n=\tfrac12n_0(0.61\lambda_0/dn_0)^2,\qquad(7.1.13a)$$
$$d=0.61\lambda_0(2n_0\delta n)^{-1/2}.\qquad(7.1.13b)$$

Con $\delta n=n_2I$:

$$d=0.61\lambda_0(2n_0n_2I)^{-1/2},\qquad(7.1.14)$$

y la potencia del haz

$$P_{\rm cr}=\frac{\pi}{4}d^2I=\frac{\pi(0.61)^2\lambda_0^2}{8n_0n_2}.\qquad(7.1.15),\ \text{p. 335}$$

Lo crucial para que haya autoenfoque es la **potencia**, no la intensidad. Para $P\gg P_{\rm cr}$ el haz
usualmente se rompe en muchos filamentos de potencia $P_{\rm cr}$ cada uno (teoría de Bespalov y Talanov, 1966).

**Valores numéricos (p. 335).** CS₂: $n_2=3.2\times10^{-18}$ m²/W (luz linealmente polarizada), $n_0=1.7$,
$P_{\rm cr}=27$ kW a $\lambda=1\ \mu$m. Cristales y vidrios típicos: $n_2=5\times10^{-20}$ a $5\times10^{-19}$
m²/W y $P_{\rm cr}=0.2$ a 2 MW. Ejemplo: Nd:YAG con Q‑switch a 1.06 μm, pulso de 10 mJ y 10 ns (potencia de
pico $\sim1$ MW), $w_0=100\ \mu$m: (7.1.4) predice $z_{\rm sf}=1$ cm en CS₂.

### 7.1.2 Mathematical Description of Self-Action Effects — descripción matemática (p. 335)

Régimen estacionario (láser continuo). Ecuación de onda paraxial, según (2.10.3):

$$2ik_0\frac{\partial A}{\partial z}+\nabla_T^2A=-\frac{\omega^2}{\epsilon_0c^2}p_{\rm NL},\qquad(7.1.16)$$

con, para respuesta puramente de tercer orden,

$$p_{\rm NL}=3\epsilon_0\chi^{(3)}|A|^2A.\qquad(7.1.17)$$

**Caso 1D (guía plana), p. 336.** $A=A(x,z)$:

$$2ik_0\frac{\partial A}{\partial z}+\frac{\partial^2A}{\partial x^2}=-3\chi^{(3)}\frac{\omega^2}{c^2}|A|^2A,\qquad(7.1.18)$$

que admite la solución

$$A(x,z)=A_0\,{\rm sech}(x/x_0)\,e^{i\gamma z},\qquad(7.1.19)$$

con ancho y tasa de adquisición de fase no lineal

$$x_0=\frac{1}{k_0}\sqrt{n_0/2\bar n_2|A_0|^2},\qquad(7.1.20)$$
$$\gamma=k_0\bar n_2|A_0|^2/n_0,\qquad(7.1.21)$$

donde, como en la §4.1, $\bar n_2=3\chi^{(3)}/4n_0$ (índice definido por $n=n_0+2\bar n_2|E|^2$). Es el
**solitón espacial**: perfil transversal invariante a lo largo de grandes distancias; observado por Barthelemy
et al. (1985) y Aitchison et al. (1991). [Comprobación: sustituyendo (7.1.19) en (7.1.18) con
${\rm sech}''=\mathrm{sech}-2\,\mathrm{sech}^3$ se obtienen exactamente (7.1.20)–(7.1.21), usando $k_0=n_0\omega/c$.]

**Caso 2D (simetría cilíndrica).** No hay solución analítica, solo numérica. La solución de orden más bajo
(Chiao et al., 1964) es una campana aproximadamente gaussiana [conocida en la literatura como perfil de Townes; el nombre no aparece en el libro]. En dos dimensiones
transversales los solitones espaciales son **inestables en un medio Kerr puro** ($\bar n_2$), pero se propagan
de forma estable en un **medio no lineal saturable** (observado por Bjorkholm y Ashkin, 1974). Soluciones de
orden superior: Haus (1966).

### 7.1.3 Laser Beam Breakup into Many Filaments — ruptura en muchos filamentos (p. 336)

La ruptura se debe al crecimiento, por amplificación de mezcla de cuatro ondas hacia adelante, de las
irregularidades iniciales del frente de onda (Fig. 7.1.5: las perturbaciones del frente de onda crecen y el
haz se fragmenta). Normalmente da una distribución de intensidad aleatoria (Fig. 7.1.1c), pero en ciertas
condiciones produce patrones geométricos muy regulares (Bennink et al., 2002).

**Análisis de Bespalov y Talanov (1966), p. 337–339.** Campo

$$\tilde E(\mathbf r,t)=E(\mathbf r)e^{-i\omega t}+{\rm c.c.},\qquad(7.1.22)$$

con amplitud expresada como suma de tres ondas planas (Fig. 7.1.6):

$$E(\mathbf r)=E_0+E_1+E_{-1}=[A_0(z)+A_1(\mathbf r)+A_{-1}(\mathbf r)]e^{ikz}=[A_0(z)+a_1(z)e^{i\mathbf q\cdot\mathbf r}+a_{-1}(z)e^{-i\mathbf q\cdot\mathbf r}]e^{ikz},$$

$k=n_0\omega/c$; $E_0$ es la componente central intensa y $E_{\pm1}$ son modos laterales espaciales débiles,
simétricos, con vector de onda transversal $\pm\mathbf q$ (Fig. 7.1.6b: $\mathbf k_{\pm1}=\mathbf k_0\pm\mathbf q$).
Polarización no lineal:

$$P=3\epsilon_0\chi^{(3)}|E|^2E\equiv P_0+P_1+P_{-1},\qquad(7.1.23)$$

con la parte en fase con la componente central (a orden cero en los modos débiles)

$$P_0=3\epsilon_0\chi^{(3)}|E_0|^2E_0=3\epsilon_0\chi^{(3)}|A_0|^2A_0e^{ikz}\equiv p_0e^{ikz},\qquad(7.1.24)$$

y la parte que se acopla a los modos laterales (lineal en ellos)

$$P_{\pm1}=3\epsilon_0\chi^{(3)}\left(2|E_0|^2E_{\pm1}+E_0^2E_{\mp1}^*\right)\equiv p_{\pm1}e^{ikz}.\qquad(7.1.25)$$

El primer término es modulación cruzada (factor 2) y el segundo es el término de mezcla de cuatro ondas que
acopla $E_1$ y $E_{-1}^*$ (dos fotones del bombeo $\to$ un fotón en cada modo lateral).

Ecuación para $A_0$ (p. 338):

$$2ik\frac{\partial A_0}{\partial z}+\nabla_\perp^2A_0=-\frac{\omega^2}{\epsilon_0c^2}p_0.\qquad(7.1.26)$$

Como $\nabla_\perp^2A_0=0$:

$$A_0(z)=A_{00}e^{i\gamma z},\qquad(7.1.27)$$
$$\gamma=\frac{3\omega\chi^{(3)}}{2n_0c}|A_{00}|^2=n_2k_{\rm vac}I,\qquad(7.1.28)$$

tasa espacial de fase no lineal ($A_{00}$ real sin pérdida de generalidad): la componente central solo acumula
la fase de automodulación. Entonces

$$p_{\pm1}=3\epsilon_0\chi^{(3)}\left[2|A_{00}|^2A_{\pm1}+A_{00}^2e^{2i\gamma z}A_{\mp1}^*\right].\qquad(7.1.29)$$

Ecuación de los modos laterales

$$2ik\frac{\partial A_{\pm1}}{\partial z}+\nabla_\perp^2A_{\pm1}=-\frac{\omega^2}{\epsilon_0c^2}p_{\pm1},\qquad(7.1.30)$$

y con $A_{\pm1}=a_{\pm1}\exp(\pm i\mathbf q\cdot\mathbf r)$ ($\nabla_\perp^2\to-q^2$):

$$2ik\frac{\partial a_{\pm1}}{\partial z}-q^2a_{\pm1}=-\frac{\omega^2}{c^2}3\chi^{(3)}|A_{00}|^2\left[2a_{\pm1}+a_{\mp1}^*e^{2i\gamma z}\right].\qquad(7.1.31)$$

Reordenando e introduciendo (7.1.28) (p. 339):

$$\frac{da_{\pm1}}{dz}+\frac{iq^2}{2k}a_{\pm1}=i\gamma\left(2a_{\pm1}+a_{\mp1}^*e^{2i\gamma z}\right).\qquad(7.1.32)$$

Cambio de variables para eliminar el factor de fase:

$$a_{\pm1}=a'_{\pm1}e^{i\gamma z},\qquad(7.1.33)$$
$$\frac{d}{dz}a'_{\pm1}=i(\gamma-q^2/2k)a'_{\pm1}+i\gamma a'^*_{\mp1}.\qquad(7.1.34)$$

Sistema de coeficientes constantes; en forma matricial, con $\beta\equiv q^2/2k$:

$$\frac{d}{dz}\begin{bmatrix}a'_1\\a'^*_{-1}\end{bmatrix}=\begin{bmatrix}i(\gamma-\beta)&i\gamma\\-i\gamma&-i(\gamma-\beta)\end{bmatrix}\begin{bmatrix}a'_1\\a'^*_{-1}\end{bmatrix}.\qquad(7.1.35)$$

Autosoluciones $\propto e^{\Lambda z}$:

$$\begin{bmatrix}a'_1(z)\\a'^*_{-1}(z)\end{bmatrix}=\begin{bmatrix}a'_1(0)\\a'^*_{-1}(0)\end{bmatrix}e^{\Lambda z},\qquad(7.1.36)$$
$$\begin{bmatrix}i(\gamma-\beta)-\Lambda&i\gamma\\-i\gamma&-i(\gamma-\beta)-\Lambda\end{bmatrix}\begin{bmatrix}a'_1(0)\\a'^*_{-1}(0)\end{bmatrix}=0.\qquad(7.1.37)$$

Determinante nulo: $\Lambda^2+(\gamma-\beta)^2-\gamma^2=0$, es decir

$$\Lambda=\pm\sqrt{\beta(2\gamma-\beta)}.\qquad(7.1.38)$$

Hay ganancia (${\rm Re}\,\Lambda>0$) solo si $\gamma>\tfrac12\beta$, lo que exige $n_2>0$ para que haya ruptura.
Fig. 7.1.7 (p. 340): $\Lambda/\gamma$ vs $q/q_{\rm opt}$; crece casi linealmente desde 0, llega a un máximo
$\Lambda_{\max}=\gamma$ (la ganancia máxima es numéricamente igual al desfase no lineal por unidad de longitud
del bombeo) en $q=q_{\rm opt}$ y cae a cero abruptamente en $q_{\max}=2\sqrt{k\gamma}$ (es decir, en $\beta=2\gamma$);
el máximo ($\beta=\gamma$) está en $q_{\rm opt}=q_{\max}/\sqrt2=\sqrt{2k\gamma}$. Ángulo característico de la ruptura:

$$\theta_{\rm opt}=q_{\rm opt}/k.\qquad(7.1.39)$$

Interpretación (Chiao et al., 1966): $\theta_{\rm opt}$ es la dirección en que la mezcla de cuatro ondas
casi‑colineal queda en **ajuste de fase** cuando se incluyen las contribuciones no lineales a los vectores de
onda de las ondas en el eje y fuera de él.

**Potencia por filamento.** $P_{\rm fil}\sim I\times$ (área de un filamento); tomando $w_{\rm eff}^2=(\pi/q)^2$
(con $q=q_{\rm opt}$):

$$P_{\rm fil}=\frac{\lambda^2}{8n_0n_2},\qquad(7.1.40)$$

del mismo orden que $P_{\rm cr}$ de (7.1.1): el haz se rompe en muchos componentes, cada uno con potencia
$\sim P_{\rm cr}$. [Verificación: $q_{\rm opt}^2=2k\gamma=2kk_{\rm vac}n_2I$, luego
$\pi^2I/q_{\rm opt}^2=\pi^2/(2n_0k_{\rm vac}^2n_2)=\lambda^2/(8n_0n_2)$, con $\lambda$ la longitud de onda en el vacío.]

**Condiciones para que ocurra la ruptura (p. 340–341).** Cuestión sutil: (i) la ruptura crece de las
perturbaciones iniciales, así que un haz muy limpio tiene un umbral mucho mayor que uno "sucio"; (ii) la
ganancia de ruptura depende solo de la intensidad, mientras que el autoenfoque de todo el haz depende de
intensidad y tamaño del haz. Se define la distancia de ruptura $z_{\rm fil}$ por $n_2k_{\rm vac}Iz_{\rm fil}=G$,
con $G$ un factor numérico (del orden de 3 a 10) que fija la ganancia necesaria. En $q_{\rm opt}$,
$\Lambda=\gamma=n_2k_{\rm vac}I$, y

$$z_{\rm fil}=\frac{G}{n_2k_{\rm vac}I},\qquad(7.1.41)$$

a comparar con la distancia de autoenfoque

$$z_{\rm sf}=\frac{2n_0w_0^2}{\lambda_0}\frac{1}{\sqrt{P/P_{\rm cr}-1}},\qquad(7.1.42)$$

con $P_{\rm cr}=\pi(0.61)^2\lambda_0^2/8n_0n_2$. Condiciones: $z_{\rm fil}<L$ (longitud de interacción) y
$z_{\rm fil}<z_{\rm sf}$ (la ruptura ocurre dentro del medio y antes de que el haz entero se autoenfoque).
$z_{\rm fil}$ decrece con la potencia más rápido que $z_{\rm sf}$, así que con potencia suficiente siempre se
induce la ruptura. Igualando $z_{\rm fil}=z_{\rm sf}$ en el límite $P\gg P_{\rm cr}$:

$$P/P_{\rm cr}=4G^2.\qquad(7.1.43)$$

Para el valor representativo $G=5$, la ruptura se espera solo si $P>100P_{\rm cr}$.

*Lectura:* el texto dice que (7.1.42) es "Eq. (7.1.4) derived earlier", pero la forma con $\sqrt{P/P_{\rm cr}-1}$ es
la (7.1.6); (7.1.4) es su límite $P\gg P_{\rm cr}$, que es el que se usa para obtener (7.1.43). El factor 4 de
(7.1.43) depende de cómo se relacione $I$ con $P$ y $w_0$ (el libro no lo explicita).

### 7.1.4 Self-Action Effects with Pulsed Laser Beams — autoacción con pulsos (p. 341)

Con radiación pulsada los efectos de autoacción cambian de carácter; aquí solo comentarios generales (los
pulsos ultracortos se tratan en el cap. 13).

**Modelo de foco móvil (moving focus), p. 342.** Loy y Shen (1973), pulsos de nanosegundos. La distancia
$z_{\rm sf}$ de (7.1.4) depende de la intensidad instantánea $I(t)$ en la cara de entrada, por lo que el foco
barre el material siguiendo la evolución temporal del pulso. El daño suele ocurrir en el punto de intensidad
pico, de modo que las trazas de daño observadas en los primeros trabajos (Hercher, 1964) se interpretan como
el lugar geométrico de los focos para todos los valores de $I(t)$ (y no como filamentos autoatrapados). Por
efectos de tiempo de tránsito suele haber **dos** autofocos simultáneos: uno más cerca de la entrada, debido a
la luz intensa cerca del pico del pulso, y otro más adentro, debido a partes anteriores y más débiles del pulso.

**Autoenfoque transitorio, p. 342.** Ocurre si la duración del pulso $\tau_p$ es comparable o menor que el
tiempo de establecimiento de la respuesta del material. La respuesta no lineal crece durante el pulso y es más
fuerte para el flanco posterior que para el anterior: el flanco posterior se autoenfoca más, distorsionando la
distribución de intensidad en espacio y tiempo (Shen, 1975). Se observa con pulsos de picosegundos en líquidos
cuya no linealidad dominante es la orientación molecular.

## 7.2 Optical Phase Conjugation — conjugación de fase óptica (p. 342)

**Idea (p. 342–343).** La conjugación de fase óptica (OPC) permite eliminar los efectos de las aberraciones en
ciertos sistemas ópticos (Zel'dovich et al., 1985; Boyd y Grynberg, 1992). Fig. 7.2.1: (a) en un espejo
metálico ordinario a incidencia normal, la parte más adelantada del frente de onda incidente sigue siendo la
más adelantada tras la reflexión; (b) en un **espejo conjugador de fase** (PCM) la parte más adelantada se
convierte en la más retrasada. Por eso se llama también *inversión del frente de onda* (wavefront reversal);
pero el frente está invertido solo respecto a la reflexión geométrica normal: de hecho el frente generado
replica exactamente al incidente pero se propaga en sentido opuesto, y por eso se habla también de generación
de un frente de onda *invertido en el tiempo* (7.2.5).

**Descripción matemática (p. 343).** Onda señal incidente sobre el PCM:

$$\tilde{\mathbf E}_s(\mathbf r,t)=\mathbf E_s(\mathbf r)e^{-i\omega t}+{\rm c.c.}\qquad(7.2.1)$$

Onda reflejada (onda conjugada):

$$\tilde{\mathbf E}_c(\mathbf r,t)=r\,\mathbf E_s^*(\mathbf r)e^{-i\omega t}+{\rm c.c.},\qquad(7.2.2)$$

con $r$ el coeficiente de reflexión en amplitud del PCM. Escribiendo

$$\mathbf E_s(\mathbf r)=\hat{\boldsymbol\epsilon}_sA_s(\mathbf r)e^{i\mathbf k_s\cdot\mathbf r},\qquad(7.2.3)$$

($\hat{\boldsymbol\epsilon}_s$ vector unitario de polarización, $A_s$ amplitud lentamente variable, $\mathbf k_s$
vector de onda medio), su conjugado es

$$\mathbf E_s^*(\mathbf r)=\hat{\boldsymbol\epsilon}_s^*A_s^*(\mathbf r)e^{-i\mathbf k_s\cdot\mathbf r}.\qquad(7.2.4)$$

La acción de un PCM **ideal** es triple (p. 344):
1. El vector de polarización complejo se reemplaza por su conjugado: luz circular derecha sigue siendo circular
   derecha tras reflejarse (en un espejo metálico a incidencia normal pasaría a circular izquierda).
2. $A_s(\mathbf r)\to A_s^*(\mathbf r)$: el frente de onda se invierte (Fig. 7.2.1b). (Nota al pie: por esta
   propiedad la conjugación de fase tiene características especiales de ruido cuántico; Gaeta y Boyd, 1988.)
3. $\mathbf k_s\to-\mathbf k_s$: la onda se refleja de vuelta en su dirección de incidencia; en óptica de rayos,
   cada rayo se refleja exactamente sobre sí mismo.

De (7.2.1)–(7.2.4):

$$\tilde{\mathbf E}_c(\mathbf r,t)=r\,\tilde{\mathbf E}_s(\mathbf r,-t),\qquad(7.2.5)$$

es decir, la conjugación de fase equivale a generar un frente de onda invertido en el tiempo. [Para $r$ real.]
(7.2.4) describe un PCM *ideal*; muchos dispositivos llamados PCM son imperfectos: no tienen las tres
propiedades o las tienen solo aproximadamente (p. ej., muchos son muy imperfectos en polarización aunque casi
perfectos en inversión del frente de onda).

### 7.2.1 Aberration Correction by Phase Conjugation — corrección de aberraciones (p. 344)

La OPC elimina aberraciones cuando el haz pasa **dos veces, en sentidos opuestos**, por el medio aberrante
(Fig. 7.2.2): un frente inicialmente plano atraviesa el medio aberrante (turbulencia atmosférica,
inhomogeneidades de índice en un vidrio, un sistema óptico mal diseñado) y sale distorsionado; el PCM genera
el frente conjugado, con el sentido de la distorsión invertido, y al volver a atravesar el medio emerge una
onda sin distorsión.

**Demostración (Yariv y Fisher, en Fisher 1983), p. 345–346.** Onda $\tilde E(\mathbf r,t)$ en un medio sin
pérdidas de índice no uniforme $n(\mathbf r)=[\epsilon(\mathbf r)]^{1/2}$ (Fig. 7.2.3), con variación espacial de
$\epsilon(\mathbf r)$ en escalas mucho mayores que la longitud de onda. Ecuación de onda:

$$\nabla^2\tilde E-\frac{\epsilon(\mathbf r)}{c^2}\frac{\partial^2\tilde E}{\partial t^2}=0.\qquad(7.2.6)$$

Onda hacia la derecha

$$\tilde E(\mathbf r,t)=A(\mathbf r)e^{i(kz-\omega t)}+{\rm c.c.},\qquad(7.2.7)$$

con $A(\mathbf r)$ lentamente variable y $z$ la dirección media de propagación;

$$\nabla^2=\frac{\partial^2}{\partial z^2}+\nabla_T^2,\qquad(7.2.8)$$

$\nabla_T^2=\partial^2/\partial x^2+\partial^2/\partial y^2$ (laplaciano transversal). Sustituyendo y despreciando
$\partial^2A/\partial z^2$ (amplitud lentamente variable):

$$\nabla_T^2A+\left[\frac{\omega^2\epsilon(\mathbf r)}{c^2}-k^2\right]A+2ik\frac{\partial A}{\partial z}=0.\qquad(7.2.9),\ \text{p. 346}$$

Como es válida en general, también lo es su conjugada ($\epsilon$ real, medio sin pérdidas):

$$\nabla_T^2A^*+\left[\frac{\omega^2\epsilon(\mathbf r)}{c^2}-k^2\right]A^*-2ik\frac{\partial A^*}{\partial z}=0,\qquad(7.2.10)$$

que es justamente la ecuación de la onda

$$\tilde E_c(\mathbf r,t)=A^*(\mathbf r)e^{i(-kz-\omega t)}+{\rm c.c.},\qquad(7.2.11)$$

que viaja en $-z$ con amplitud compleja que es **en todas partes** la conjugada de la onda hacia adelante.
Conclusión: si el PCM genera una onda de regreso cuya amplitud es la conjugada de la incidente en un solo plano
(p. ej., la cara de entrada del espejo), la onda de regreso será la conjugada de la incidente en **todos** los
puntos delante del espejo (por unicidad de la solución de la ecuación paraxial de primer orden en $z$). Si la
onda incidente era plana antes del medio aberrante, la conjugada que emerge de él también es plana. La OPC
sirve directamente para corrección en doble paso; en circunstancias especiales también en un solo paso
(MacDonald et al., 1988).

### 7.2.2 Phase Conjugation by Degenerate Four-Wave Mixing — conjugación por mezcla de cuatro ondas degenerada (p. 346)

Hellwarth (1977) y Yariv y Pepper (1977) mostraron que la conjugada de una onda incidente puede crearse por
**mezcla de cuatro ondas degenerada (DFWM)** con la geometría de la Fig. 7.2.4 (p. 347): medio sin pérdidas
con $\chi^{(3)}$ entre $z=0$ y $z=L$, iluminado por dos **bombeos contrapropagantes** intensos $A_1$ (entra por
$z=0$) y $A_2$ (entra por $z=L$) y por una señal $A_3$ que entra por $z=0$ hacia $+z$; se genera la conjugada
$A_4$, que sale por $z=0$ hacia $-z$. Degenerada: las cuatro ondas tienen la misma frecuencia. Los bombeos
suelen ser ondas planas, aunque basta con que sus amplitudes sean conjugadas entre sí; la señal tiene frente
arbitrario. La eficiencia se da en (7.2.37).

**Argumento simple (p. 347–348).** Cada onda:

$$\tilde E_i(\mathbf r,t)=E_i(\mathbf r)e^{-i\omega t}+{\rm c.c.}=A_i(\mathbf r)e^{i(\mathbf k_i\cdot\mathbf r-\omega t)}+{\rm c.c.},\quad i=1,2,3,4,\qquad(7.2.12)$$

($A_i$ lentamente variables). [*Errata tipográfica:* en el libro se lee $E^{i(\mathbf k_i\cdot\mathbf r-\omega t)}$ con $E$
mayúscula; debe ser la exponencial $e$.] Entre muchos términos, la polarización no lineal contiene

$$P^{\rm NL}=6\epsilon_0\chi^{(3)}E_1E_2E_3^*=6\epsilon_0\chi^{(3)}A_1A_2A_3^*e^{i(\mathbf k_1+\mathbf k_2-\mathbf k_3)\cdot\mathbf r}.\qquad(7.2.13)$$

Con bombeos contrapropagantes,

$$\mathbf k_1+\mathbf k_2=0,\qquad(7.2.14)$$
$$P^{\rm NL}=6\epsilon_0\chi^{(3)}A_1A_2A_3^*e^{-i\mathbf k_3\cdot\mathbf r},\qquad(7.2.15)$$

que es fuente en ajuste de fase para una onda $E_4$ con vector de onda $-\mathbf k_3$:

$$\mathbf k_3=-\mathbf k_4.\qquad(7.2.16),\ \text{p. 348}$$

La amplitud generada es $\propto A_1A_2A_3^*$: es la conjugada de $A_3$ siempre que la fase del producto $A_1A_2$
sea espacialmente invariante, ya sea porque ambos bombeos son ondas planas (constantes) o porque son conjugados
entre sí ($A_2\propto A_1^*\Rightarrow A_1A_2\propto|A_1|^2$ real).

*Visión de rejilla:* la señal $A_3$ interfiere con uno de los bombeos (p. ej., $A_1$) formando una distribución de
intensidad espacialmente variable; la respuesta no lineal la convierte en una variación de índice, que actúa
como **rejilla de difracción de volumen** y difracta el otro bombeo para formar la onda conjugada $A_4$
(holografía en tiempo real).

**Tratamiento riguroso (p. 348–352).** Campo total

$$E=E_1+E_2+E_3+E_4,\qquad(7.2.17)$$
$$P=3\epsilon_0\chi^{(3)}E^2E^*,\qquad(7.2.18)$$

con $\chi^{(3)}=\chi^{(3)}(\omega=\omega+\omega-\omega)$. De los muchos términos de $E^2E^*$, los importantes son los de
dependencia espacial

$$e^{i\mathbf k_i\cdot\mathbf r},\quad i=1,2,3,4,\qquad(7.2.19)$$

porque son fuentes en ajuste de fase para alguna de las cuatro ondas. Sus amplitudes (p. 349):

$$\begin{aligned}
P_1&=3\epsilon_0\chi^{(3)}[E_1^2E_1^*+2E_1E_2E_2^*+2E_1E_3E_3^*+2E_1E_4E_4^*+2E_3E_4E_2^*],\\
P_2&=3\epsilon_0\chi^{(3)}[E_2^2E_2^*+2E_2E_1E_1^*+2E_2E_3E_3^*+2E_2E_4E_4^*+2E_3E_4E_1^*],\\
P_3&=3\epsilon_0\chi^{(3)}[E_3^2E_3^*+2E_3E_1E_1^*+2E_3E_2E_2^*+2E_3E_4E_4^*+2E_1E_2E_4^*],\\
P_4&=3\epsilon_0\chi^{(3)}[E_4^2E_4^*+2E_4E_1E_1^*+2E_4E_2E_2^*+2E_4E_3E_3^*+2E_1E_2E_3^*].
\end{aligned}\qquad(7.2.20)$$

Suponiendo $E_3,E_4\ll E_1,E_2$ y despreciando los términos con más de una amplitud débil:

$$\begin{aligned}
P_1&=3\epsilon_0\chi^{(3)}[E_1^2E_1^*+2E_1E_2E_2^*],\\
P_2&=3\epsilon_0\chi^{(3)}[E_2^2E_2^*+2E_2E_1E_1^*],\\
P_3&=3\epsilon_0\chi^{(3)}[2E_3E_1E_1^*+2E_3E_2E_2^*+2E_1E_2E_4^*],\\
P_4&=3\epsilon_0\chi^{(3)}[2E_4E_1E_1^*+2E_4E_2E_2^*+2E_1E_2E_3^*].
\end{aligned}\qquad(7.2.21)$$

A este orden, $E_3$ y $E_4$ son impulsados por polarizaciones que dependen de todos los campos, pero las de $E_1$
y $E_2$ dependen solo de ellos mismos: se resuelven primero los bombeos. Cada onda obedece

$$\nabla^2\tilde E_i-\frac{\epsilon}{c^2}\frac{\partial^2\tilde E_i}{\partial t^2}=\frac{1}{\epsilon_0c^2}\frac{\partial^2}{\partial t^2}\tilde P_i.\qquad(7.2.22)$$

*Bombeos.* Con $z'$ medida en la dirección de propagación de $E_1$, bombeos de frente plano y aproximación de
amplitud lentamente variable:

$$\left[\left(-k_1^2+2ik_1\frac{d}{dz'}+\frac{\epsilon\omega^2}{c^2}\right)A_1\right]e^{i(k_1z'-\omega t)}=-\frac{\omega^2}{c^2}3\chi^{(3)}\left[|A_1|^2+2|A_2|^2\right]A_1e^{i(k_1z'-\omega t)},$$

que se simplifica (p. 350, usando $k_1^2=\epsilon\omega^2/c^2$, $k_1=n\omega/c$) a

$$\frac{dA_1}{dz'}=\frac{3i\omega}{2nc}\chi^{(3)}\left[|A_1|^2+2|A_2|^2\right]A_1\equiv i\kappa_1A_1,\qquad(7.2.23a)$$
$$\frac{dA_2}{dz'}=\frac{-3i\omega}{2nc}\chi^{(3)}\left[|A_2|^2+2|A_1|^2\right]A_2\equiv i\kappa_2A_2.\qquad(7.2.23b)$$

$\kappa_1,\kappa_2$ son reales: los bombeos solo sufren desfases, que dependen de su propia intensidad (SPM) y de la
del otro (XPM, con peso doble, como tras (4.1.14)). Estos desfases pueden introducir desajuste de fase en la
generación de la conjugada. Como las amplitudes no cambian, $|A_1|^2,|A_2|^2$ y por tanto $\kappa_{1,2}$ son
constantes:

$$A_1(z')=A_1(0)e^{i\kappa_1z'},\qquad(7.2.24a)$$
$$A_2(z')=A_2(0)e^{-i\kappa_2z'}.\qquad(7.2.24b)$$

*Errata (signo):* con la definición "$\equiv i\kappa_2A_2$" de (7.2.23b), $\kappa_2$ sería negativo y la solución sería
$e^{+i\kappa_2z'}$. Para que (7.2.24b)–(7.2.26) sean consistentes ($\kappa_2>0$ y $\kappa_1=\kappa_2$ con bombeos iguales),
la definición debe leerse $dA_2/dz'\equiv-i\kappa_2A_2$, con $\kappa_2=\frac{3\omega}{2nc}\chi^{(3)}[|A_2|^2+2|A_1|^2]$.

El producto que aparece en (7.2.15):

$$A_1(z')A_2(z')=A_1(0)A_2(0)e^{i(\kappa_1-\kappa_2)z'};\qquad(7.2.25)$$

el factor $e^{i(\kappa_1-\kappa_2)z'}$ es el desajuste de vector de onda. Con bombeos de igual intensidad,
$\kappa_1=\kappa_2$ y

$$A_1(z')A_2(z')=A_1(0)A_2(0),\qquad(7.2.26)$$

interacción perfectamente en ajuste de fase. Se supone en adelante que los bombeos tienen igual intensidad.

*Señal y conjugada.* Se supone señal de frente plano, sin pérdida de generalidad: una señal arbitraria se
descompone en ondas planas, cada una acoplada a una componente plana de $\tilde E_4$. De (7.2.22) (p. 351):

$$\frac{dA_3}{dz}=\frac{3i\omega}{nc}\chi^{(3)}\left[(|A_1|^2+|A_2|^2)A_3+A_1A_2A_4^*\right],\qquad(7.2.27a)$$
$$\frac{dA_4}{dz}=-\frac{3i\omega}{nc}\chi^{(3)}\left[(|A_1|^2+|A_2|^2)A_4+A_1A_2A_3^*\right],\qquad(7.2.27b)$$

o bien

$$\frac{dA_3}{dz}=i\kappa_3A_3+i\kappa A_4^*,\qquad(7.2.28a)$$
$$\frac{dA_4}{dz}=-i\kappa_3A_4-i\kappa A_3^*,\qquad(7.2.28b)$$

con los coeficientes de acoplamiento

$$\kappa_3=\frac{3\omega}{nc}\chi^{(3)}\left(|A_1|^2+|A_2|^2\right),\qquad(7.2.29a)$$
$$\kappa=\frac{3\omega}{nc}\chi^{(3)}A_1A_2.\qquad(7.2.29b)$$

Cambio de variables (las primadas coinciden con las no primadas en $z=0$):

$$A_3=A_3'e^{i\kappa_3z},\qquad(7.2.30a)$$
$$A_4=A_4'e^{-i\kappa_3z}.\qquad(7.2.30b)$$

Sustituyendo, $i\kappa_3A_3'e^{i\kappa_3z}+\frac{dA_3'}{dz}e^{i\kappa_3z}=i\kappa_3A_3'e^{i\kappa_3z}+i\kappa A_4'^*e^{i\kappa_3z}$, es decir

$$\frac{dA_3'}{dz}=i\kappa A_4'^*,\qquad(7.2.31a)$$
$$\frac{dA_4'}{dz}=-i\kappa A_3'^*.\qquad(7.2.31b)$$

Esto muestra por qué la DFWM produce conjugación de fase: el campo generado $A_4'$ es impulsado **solo por el
conjugado** de la amplitud de entrada. Estas ecuaciones son formalmente idénticas a las que se obtendrían
ignorando la modificación no lineal de los bombeos, es decir tomando (p. 352)

$$P_1=P_2=0,\qquad P_3=6\epsilon_0\chi^{(3)}E_1E_2E_4^*,\qquad P_4=6\epsilon_0\chi^{(3)}E_1E_2E_3^*.\qquad(7.2.32)$$

**Solución.** Derivando (7.2.31) respecto a $z$ y sustituyendo (nota al pie: se supone $\chi^{(3)}$ y por tanto
$\kappa$ reales; se escribe así por generalidad para casos con $\kappa$ complejo):

$$\frac{d^2A_4'}{dz^2}+|\kappa|^2A_4'=0,\qquad(7.2.33)$$
$$A_4'(z)=B\sin|\kappa|z+C\cos|\kappa|z.\qquad(7.2.34)$$

Condiciones de frontera en los planos de entrada de cada onda débil: $A_3'^*(0)$ y $A_4'(L)$ dados:

$$A_3'^*(z)=-\frac{i|\kappa|}{\kappa}\frac{\sin|\kappa|z}{\cos|\kappa|L}A_4'(L)+\frac{\cos[|\kappa|(z-L)]}{\cos|\kappa|L}A_3'^*(0),\qquad(7.2.35a)$$
$$A_4'(z)=\frac{\cos|\kappa|z}{\cos|\kappa|L}A_4'(L)-\frac{i\kappa}{|\kappa|}\frac{\sin[|\kappa|(z-L)]}{\cos|\kappa|L}A_3'^*(0).\qquad(7.2.35b)$$

Normalmente no se inyecta conjugada en $z=L$:

$$A_4'(L)=0,\qquad(7.2.36)$$

y las amplitudes de salida son (p. 353)

$$A_3'^*(L)=\frac{A_3'^*(0)}{\cos|\kappa|L},\qquad(7.2.37a)$$
$$A_4'(0)=\frac{i\kappa}{|\kappa|}\left(\tan|\kappa|L\right)A_3'^*(0).\qquad(7.2.37b)$$

[Reflectividad del PCM: $R=|A_4(0)|^2/|A_3(0)|^2=\tan^2|\kappa|L$; transmitancia de la señal $1/\cos^2|\kappa|L$.
Comprobado por sustitución directa en (7.2.31).] La señal transmitida $A_3'(L)$ es **siempre** más intensa que la
incidente; la conjugada de salida puede tener cualquier intensidad entre cero e infinito según $|\kappa|L$
(diverge para $|\kappa|L=\pi/2$: oscilación). La reflectividad de un PCM por DFWM **puede exceder 100 %** porque
el espejo es bombeado activamente por ondas externas que suministran energía.

**Energética y ajuste de fase (p. 353–354).** Se aniquila un fotón de cada bombeo y se añade uno a la señal y
otro a la conjugada (Fig. 7.2.5): se crea $A_4$ y se amplifica $A_3$. Fig. 7.2.5: (a) diagrama dominante si la
frecuencia es casi resonante con una transición de un fotón ($A_1$ arriba, $A_3$ abajo, $A_2$ arriba, $A_4$ abajo);
(b) dominante con excitación resonante a dos fotones ($A_1$ y $A_2$ suben, $A_3$ y $A_4$ bajan); (c) vectores de onda:
$\mathbf k_1+\mathbf k_2-\mathbf k_3-\mathbf k_4=0$. La DFWM con bombeos contrapropagantes está **automáticamente en
ajuste de fase** (con bombeos de igual intensidad, o si se desprecian los desfases no lineales): no aparecen
términos $e^{\pm i\Delta kz}$ en (7.2.31). Interpretación: energía de entrada $2\hbar\omega$ y momento
$\hbar(\mathbf k_1+\mathbf k_2)=0$; salida $2\hbar\omega$ y $\hbar(\mathbf k_3+\mathbf k_4)=0$. Si los bombeos no son exactamente
contrapropagantes, $\hbar(\mathbf k_1+\mathbf k_2)\ne0$ y el ajuste no es automático.

**Experimento de Bloom y Bjorklund (1977), Fig. 7.2.6 (p. 354).** Primera demostración de OPC por DFWM: celda de
CS₂ bombeada por un láser y retrorreflejado por un espejo (bombeos contrapropagantes); un haz débil atraviesa
un patrón de prueba, un divisor de haz, una lente y un vidrio aberrante antes de llegar a la celda; el haz
conjugado vuelve y va a una cámara. La placa aberrante no reducía la resolución cuando el espejo
retrorreflejaba el bombeo sobre sí mismo; al desalinearlo parcialmente, el haz de regreso pasaba por otra
parte del vidrio y la resolución se degradaba.

La DFWM suele hacerse con la geometría de la Fig. 7.2.4, pero también puede usarse la no linealidad
superficial de la interfaz entre un medio lineal y uno no lineal (Maki et al., 1992) (p. 355).

### 7.2.3 Polarization Properties of Phase Conjugation — propiedades de polarización (p. 355)

Hasta aquí, aproximación escalar. Es deseable que la OPC elimine también distorsiones de **polarización**
(Fig. 7.2.7): un haz linealmente polarizado atraviesa un componente óptico sometido a esfuerzo; la
birrefringencia inducida distorsiona la polarización de forma no uniforme sobre la sección del haz
(radiación despolarizada). Si el PCM es ideal ($\hat{\boldsymbol\epsilon}\to\hat{\boldsymbol\epsilon}^*$), en el segundo paso por
el componente se elimina la distorsión y el haz vuelve a su polarización lineal inicial (sale ortogonal por el
divisor de haz en la figura: "output polarization linear"). Un PCM que produce conjugado de frente de onda y de
polarización se llama **espejo conjugador de fase vectorial**.

**Geometría (Fig. 7.2.8, p. 356).** $\mathbf F$, $\mathbf B$ y $\mathbf S$: amplitudes del bombeo hacia adelante, del bombeo
hacia atrás y de la señal; el ángulo $\theta$ entre $\mathbf S$ y $\mathbf F$ es pequeño; medio no lineal isótropo.

$$\mathbf E=\mathbf F+\mathbf B+\mathbf S.\qquad(7.2.38)$$

Con $\theta\ll1$ solo importan las componentes $x,y$. Para un medio isótropo, según (4.2.5),

$$\chi^{(3)}_{ijkl}=\chi_{1122}(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl})+\chi_{1221}\delta_{il}\delta_{jk},\qquad(7.2.39)$$

($\chi^{(3)}_{ijkl}=\chi^{(3)}_{ijkl}(\omega=\omega+\omega-\omega)$), de modo que

$$\mathbf P=6\epsilon_0\chi_{1122}(\mathbf E\cdot\mathbf E^*)\mathbf E+3\epsilon_0\chi_{1221}(\mathbf E\cdot\mathbf E)\mathbf E^*=\epsilon_0A(\mathbf E\cdot\mathbf E^*)\mathbf E+\tfrac12\epsilon_0B(\mathbf E\cdot\mathbf E)\mathbf E^*$$

(ecuación sin número en el libro; $A=6\chi_{1122}$, $B=6\chi_{1221}$, coeficientes de Maker y Terhune de la §4.2). La
parte en ajuste de fase que actúa como fuente de la onda conjugada es

$$\begin{bmatrix}P_x\\P_y\end{bmatrix}=6\epsilon_0\begin{bmatrix}\chi_{1111}B_xF_x+\chi_{1221}B_yF_y&\chi_{1122}(B_xF_y+B_yF_x)\\\chi_{1122}(B_yF_x+B_xF_y)&\chi_{1111}B_yF_y+\chi_{1221}B_xF_x\end{bmatrix}\begin{bmatrix}S_x^*\\S_y^*\end{bmatrix},\qquad(7.2.40)$$

con $\chi_{1111}=2\chi_{1122}+\chi_{1221}$. [Se obtiene de los términos $\propto BFS^*$: $(\mathbf B\cdot\mathbf S^*)\mathbf F+(\mathbf F\cdot\mathbf S^*)\mathbf B$
del primer término y $2(\mathbf F\cdot\mathbf B)\mathbf S^*$ del segundo; verificado.] *Nota de numeración:* el texto dice
"introduce Eq. (7.2.38) into Eq. (7.2.40)" refiriéndose a la expresión sin número de $\mathbf P$; la etiqueta (7.2.40)
del libro está en la ecuación matricial.

La conjugación vectorial (ideal) se obtiene cuando la matriz de transferencia $2\times2$ es múltiplo de la
identidad: ambas componentes cartesianas se reflejan con igual eficiencia y sin acoplamiento entre ellas. Dos
maneras (p. 356–358):

1. **$A=6\chi_{1122}=0$ idénticamente.** Entonces (p. 357)
$$\begin{bmatrix}P_x\\P_y\end{bmatrix}=6\epsilon_0\chi_{1221}(B_xF_x+B_yF_y)\begin{bmatrix}1&0\\0&1\end{bmatrix}\begin{bmatrix}S_x^*\\S_y^*\end{bmatrix}=6\epsilon_0\chi_{1221}(B_xF_x+B_yF_y)\begin{bmatrix}S_x^*\\S_y^*\end{bmatrix},$$
   proporcional al conjugado de la señal para **cualquier** polarización de los bombeos ($\mathbf P$ tiene el carácter
   vectorial de $\mathbf E^*$). Pero $\chi_{1122}$ (o $A$) se anula solo en circunstancias muy inusuales; el único caso
   conocido es la DFWM en un sistema atómico con **resonancia a dos fotones** entre ciertos estados (análisis de
   Grynberg, 1984; experimento de Malcuit et al., 1988). Caso más simple: transición entre dos estados S de un
   átomo de espín electrónico nulo (Fig. 7.2.9: bombeo hacia adelante y hacia atrás suben de S a S; señal y
   conjugada bajan). Como ambos niveles tienen momento angular cero, la suma de los momentos angulares de los
   fotones señal y conjugado debe ser cero, lo que obliga a que sus vectores de polarización sean conjugados.
   Para la mayoría de mecanismos $A\neq0$: recordar $B/A=6$ para orientación molecular, $B/A=0$ para
   electrostricción y $B/A=1$ para respuesta electrónica no resonante.

2. **Bombeos circularmente polarizados y contrarrotantes** (caso general $A\neq0$). Si (p. 358)
$$\tilde{\mathbf F}(z,t)=F\frac{\hat x-i\hat y}{\sqrt2}e^{i(kz-\omega t)}+{\rm c.c.},\qquad(7.2.41a)$$
$$\tilde{\mathbf B}(z,t)=B\frac{\hat x+i\hat y}{\sqrt2}e^{i(-kz-\omega t)}+{\rm c.c.}\qquad(7.2.41b)$$
   Son contrarrotantes porque, a $z$ fijo, $\tilde{\mathbf F}$ gira en sentido horario en el plano $xy$ y $\tilde{\mathbf B}$ en
   sentido antihorario; pero **ambas son circulares derechas**, pues por convención la helicidad se define mirando
   hacia el haz. En la notación de (7.2.40):
$$F_x=\frac{F}{\sqrt2}e^{ikz},\quad F_y=-i\frac{F}{\sqrt2}e^{ikz},\quad B_x=\frac{B}{\sqrt2}e^{-ikz},\quad B_y=i\frac{B}{\sqrt2}e^{-ikz},\qquad(7.2.42)$$
   y (7.2.40) queda
$$\begin{bmatrix}P_x\\P_y\end{bmatrix}=3\epsilon_0FB(\chi_{1111}+\chi_{1221})\begin{bmatrix}1&0\\0&1\end{bmatrix}\begin{bmatrix}S_x^*\\S_y^*\end{bmatrix}.\qquad(7.2.43)$$
   [Pues $B_xF_x=B_yF_y=FB/2$ y $B_xF_y+B_yF_x=0$.] Matriz de nuevo múltiplo de la identidad: conjugación
   vectorial. Predicho por Zel'dovich y Shkunov (1979) y verificado por Martin et al. (1980).

*Interpretación* (p. 358–359): conservación de momento lineal y angular. Se aniquila un fotón de cada bombeo y
se crean un fotón señal y uno conjugado; con bombeos contrapropagantes y contrarrotantes el momento lineal y
angular totales de los dos fotones de entrada son nulos, así que la conjugada debe emitirse en dirección
opuesta a la señal y su vector de polarización debe rotar en sentido opuesto al de la señal.

## 7.3 Optical Bistability and Optical Switching — biestabilidad óptica y conmutación (p. 359)

**Definiciones.** *Biestabilidad óptica*: dos intensidades de salida posibles para una misma intensidad de
entrada; *multiestabilidad*: dos o más estados de salida estables. Interés: conmutadores para comunicaciones y
computación óptica. Primera descripción teórica y observación con no linealidad **absortiva**: Szöke et al.
(1969); con no linealidad **refractiva** ($\chi^{(3)}$ real): Gibbs et al. (1976). Dispositivo: medio no lineal
dentro de un **Fabry–Perot** (Fig. 7.3.1, p. 360): $A_1$ incidente, $A_1'$ reflejada, $A_2$ y $A_2'$ ondas hacia
adelante y hacia atrás dentro del interferómetro, $A_3$ transmitida; longitud $l$. Espejos idénticos y sin
pérdidas, con reflectancia y transmitancia de amplitud $\rho$, $\tau$:

$$R=|\rho|^2\quad\text{y}\quad T=|\tau|^2,\qquad(7.3.1a)$$
$$R+T=1.\qquad(7.3.1b)$$

Condiciones de frontera (amplitudes en la superficie interior del espejo izquierdo):

$$A_2'=\rho A_2e^{2ikl-\alpha l},\qquad(7.3.2a)$$
$$A_2=\tau A_1+\rho A_2'.\qquad(7.3.2b)$$

$k=n\omega/c$ y el coeficiente de absorción de intensidad $\alpha$ son reales e incluyen contribuciones lineales y no
lineales. **Aproximación de campo medio**: $k$ y $\alpha$ espacialmente invariantes; si no, el exponente se
reemplaza por $\int_0^ldz[2ik(z)-\alpha(z)]$. Se supone además igual índice lineal dentro y fuera. Eliminando $A_2'$
(p. 360):

$$A_2=\frac{\tau A_1}{1-\rho^2e^{2ikl-\alpha l}},\qquad(7.3.3)$$

la **ecuación de Airy** del Fabry–Perot. Si $k$ o $\alpha$ son funciones suficientemente no lineales de la
intensidad interna, predice biestabilidad en la intensidad transmitida. Se estudian por separado los límites
absortivo y refractivo.

### 7.3.1 Absorptive Bistability — biestabilidad absortiva (p. 360)

Solo $\alpha$ depende de la intensidad; $k$ constante. Cavidad sintonizada a resonancia ($\rho^2e^{2ikl}=R$ real) y
$\alpha l\ll1$ (intensidad interna casi uniforme, lo que justifica el campo medio):

$$A_2=\frac{\tau A_1}{1-R(1-\alpha l)}.\qquad(7.3.4)$$

En intensidades $I_i=2n\epsilon_0|A_i|^2$ (p. 361):

$$I_2=\frac{TI_1}{[1-R(1-\alpha l)]^2}.\qquad(7.3.5)$$

*Errata:* se lee $I_i=2n\epsilon_0|A_i|^2$; en la convención del libro debe ser $I_i=2n\epsilon_0c|A_i|^2$ (no afecta a
(7.3.5), que es un cociente). **Número de cooperación**

$$C=\frac{R\alpha l}{1-R};\qquad(7.3.6)$$

como $1+C=(1-R+R\alpha l)/(1-R)=[1-R(1-\alpha l)]/T$,

$$I_2=\frac1T\frac{I_1}{(1+C)^2}.\qquad(7.3.7)$$

Absorbente saturable de dos niveles:

$$\alpha=\frac{\alpha_0}{1+I/I_s},\qquad(7.3.8)$$

($\alpha_0$ coeficiente no saturado, $I_s$ intensidad de saturación). Se ignora el carácter de onda estacionaria y
se toma $I=I_2+I_2'\approx2I_2$; esto es solo aproximado en el Fabry–Perot de la Fig. 7.3.1, pero estrictamente
válido en el **interferómetro de onda viajera (anillo)** de la Fig. 7.3.2. Entonces (p. 362)

$$C=\frac{C_0}{1+2I_2/I_s},\qquad(7.3.9)$$

con $C_0=R\alpha_0l/(1-R)$, y

$$I_1=TI_2\left(1+\frac{C_0}{1+2I_2/I_s}\right)^2,\qquad(7.3.10)$$
$$I_3=TI_2.\qquad(7.3.11)$$

Fig. 7.3.3: $I_3/(TI_s/2)$ (0–100) vs $I_1/(TI_s/2)$ (0–150) para $C_0=0,5,10,15,20$; para $C_0>8$ la curva tiene
forma de S y hay varias intensidades de salida para ciertas entradas (soluciones múltiples).

**Histéresis y conmutación (Fig. 7.3.4, p. 362–364).** (a) Curva de entrada‑salida en S; el tramo de pendiente
negativa (línea discontinua, la salida crece cuando la entrada decrece) es **inestable** (intuitivamente y por
análisis de estabilidad lineal): el sistema conmuta rápidamente a una solución estable por crecimiento de
pequeñas perturbaciones. Histéresis: al subir $I_1$ desde cero hasta $I_h$ (punto de salto alto) la salida sigue
la rama inferior $a$–$b$; al seguir subiendo salta a $c$ y recorre $c$–$d$. Al bajar, permanece en la rama superior
($e$–$d$) hasta $I_l$ (punto de salto bajo), donde transita a $f$ y recorre $f$–$a$. (b) Uso como conmutador: con
$I_1$ fijo en $I_b$ (intensidad de polarización, *bias*) hay dos puntos estables (puntos llenos); el estado
almacena información binaria; se fuerza al estado superior inyectando un pulso que lleve la entrada total por
encima de $I_h$, y al inferior bloqueando momentáneamente el haz de entrada.

### 7.3.2 Refractive Bistability — biestabilidad refractiva (p. 364)

$\alpha=0$ y $n$ depende de la intensidad. (7.3.3) queda

$$A_2=\frac{\tau A_1}{1-\rho^2e^{2ikl}}=\frac{\tau A_1}{1-Re^{i\delta}},\qquad(7.3.12)$$

con

$$\rho^2=Re^{i\phi}\qquad(7.3.13)$$

y el desfase total en un viaje de ida y vuelta

$$\delta=\delta_0+\delta_2,\qquad(7.3.14)$$
$$\delta_0=\phi+2n_0\frac{\omega}{c}l\quad\text{(lineal)},\qquad(7.3.15)$$
$$\delta_2=2n_2I\frac{\omega}{c}l\quad\text{(no lineal)},\qquad(7.3.16)$$
$$I=I_2+I_2'\simeq2I_2.\qquad(7.3.17)$$

Con $I_i=2n\epsilon_0c|A_i|^2$:

$$I_2=\frac{TI_1}{(1-Re^{i\delta})(1-Re^{-i\delta})}=\frac{TI_1}{1+R^2-2R\cos\delta}=\frac{TI_1}{(1-R)^2+4R\sin^2\tfrac12\delta}=\frac{TI_1}{T^2+4R\sin^2\tfrac12\delta}=\frac{I_1/T}{1+(4R/T^2)\sin^2\tfrac12\delta},\qquad(7.3.18)$$

es decir (p. 365)

$$\frac{I_2}{I_1}=\frac{1/T}{1+(4R/T^2)\sin^2\tfrac12\delta},\qquad(7.3.19)$$

con, por (7.3.14)–(7.3.17),

$$\delta=\delta_0+(4n_2\omega l/c)I_2.\qquad(7.3.20)$$

Solución gráfica (Fig. 7.3.5): se grafican ambos lados de (7.3.19) frente a $I_2$; el lado derecho es una
sucesión de picos de Airy (función oscilatoria de $I_2$ vía $\delta$) y el izquierdo, $I_2/I_1$, son rectas por el
origen de pendiente $1/I_1$ (rectas a, b, c para $I_1$ creciente). Puede haber una, tres, cinco o más soluciones
según $I_1$. Con tres soluciones, $I_3$ vs $I_1$ se parece a la Fig. 7.3.4, y la discusión cualitativa anterior
vale también. Más detalles: Lugiato (1984) y Gibbs (1985).

### 7.3.3 Optical Switching — conmutación óptica (p. 365)

Dispositivo prototipo totalmente óptico (Fig. 7.3.6): **interferómetro de Mach–Zehnder** con un elemento no lineal
($n=n_0+n_2I$, longitud $L$) en un brazo y un elemento lineal ($n=n_0$, longitud $L$) en el otro; divisores de haz
con coeficientes $r,t$; campo de control opcional. La señal sale por el puerto 1 o el 2 según su intensidad (o la
del control). Fig. 7.3.7: uso sin control como **clasificador de pulsos**: los pulsos intensos salen por el
puerto 2 y los débiles por el puerto 1. Con señal y control el cálculo es similar y el control puede dirigir la
señal a cualquiera de los puertos.

Divisores simétricos (p. 367; nota al pie: esta forma garantiza unitariedad, es decir, las relaciones de Stokes):

$$r=i\sqrt R,\qquad t=\sqrt T,\qquad(7.3.21)$$
$$R+T=1.\qquad(7.3.22)$$

Campo en el puerto 1:

$$E_1=E_s\left(rt+rte^{i\phi_{\rm NL}}\right),\qquad(7.3.23)$$
$$\phi_{\rm NL}=n_2(\omega/c)IL=n_2(\omega/c)|t|^2(2n_0\epsilon_0c)|E_s|^2L.\qquad(7.3.24)$$

Intensidades:

$$|E_1|^2=|E_s|^2|r|^2|t|^2\left(1+e^{i\phi_{\rm NL}}\right)\left(1+e^{-i\phi_{\rm NL}}\right)=2|E_s|^2RT(1+\cos\phi_{\rm NL}),\qquad(7.3.25)$$
$$E_2=E_s\left(r^2+t^2e^{i\phi_{\rm NL}}\right),\qquad(7.3.26)$$
$$|E_2|^2=|E_s|^2\left[R^2+T^2-2RT\cos\phi_{\rm NL}\right],\qquad(7.3.27)$$
$$|E_1|^2+|E_2|^2=|E_s|^2,\qquad(7.3.28)$$

como exige la conservación de la energía. Fig. 7.3.8 (p. 368): transmisiones de los puertos 1 y 2 vs
$\phi_{\rm NL}$ de 0 a $4\pi$, sinusoides complementarias (puerto 1 máximo en $0,2\pi,4\pi$; puerto 2 máximo en $\pi,3\pi$,
con divisores 50/50). **Punto crucial**: para conmutación totalmente óptica de alto contraste se requiere un
**desfase no lineal de $\pi$ rad**; esto es genérico de una amplia clase de conmutadores ópticos.

**Desfase de $\pi$ con absorción lineal (p. 368).**

$$\phi_{\rm NL}=n_2(\omega/c)\int_0^LI(z)\,dz,\qquad(7.3.29)$$
$$I(z)=I_0e^{-\alpha z},\qquad(7.3.30)$$
$$\phi_{\rm NL}=n_2(\omega/c)I_0L_{\rm eff},\qquad(7.3.31a)$$
$$L_{\rm eff}=\frac{1-e^{-\alpha L}}{\alpha},\qquad(7.3.31b)$$
$$L_{\rm eff}\to L\quad\text{para }\alpha L\ll1,\qquad(7.3.32a)$$
$$L_{\rm eff}\to1/\alpha\quad\text{para }\alpha L\gg1.\qquad(7.3.32b)$$

En un material muy absorbente la longitud efectiva puede ser mucho menor que la física. El daño óptico (cap. 11)
limita $I_0$; por eso ciertos materiales no sirven, ni en principio, para conmutación totalmente óptica.

**Absorción de dos fotones (p. 368–369).** Con absorción lineal y de dos fotones:

$$\alpha=\alpha_0+\beta I,\qquad(7.3.33)$$

$\beta$: coeficiente de absorción de dos fotones. La TPA es a menudo un problema serio en conmutadores ópticos
porque es del mismo orden de no linealidad que $n_2$ (proporcionales a las partes imaginaria y real de $\chi^{(3)}$,
respectivamente). Se elimina por completo eligiendo un material cuyo estado excitado más bajo esté a más de
$2\hbar\omega$ del fundamental (Fig. 7.3.9: (a) TPA; (b) frecuencia por debajo de la mitad de la brecha; (c) esta
estrategia impide usar no linealidades resonantes a un fotón). Resumen de conmutación totalmente óptica:
Stegeman y Miller (1993).

## 7.4 Two-Beam Coupling — acoplamiento de dos haces (p. 369)

Dos haces (en general de frecuencias distintas, $\omega_1$ y $\omega_2$, que forman un ángulo $\theta$; Fig. 7.4.1, p. 370)
interactúan en un material no lineal de modo que se transfiere energía de uno a otro. Es un proceso
**automáticamente en ajuste de fase**, de modo que la eficiencia no depende críticamente de $\theta$; su origen es que
el índice que ve cada onda es modificado por la **intensidad** de la otra. Aparece en varios contextos:
amplificación de una sonda por un átomo de dos niveles (cap. 6), dispersión Brillouin y Raman estimuladas
(caps. 9 y 10), materiales fotorrefractivos (cap. 11). Análisis general similar a Silberberg y Bar‑Joseph
(1982, 1984).

Campo total:

$$\tilde E(\mathbf r,t)=A_1e^{i(\mathbf k_1\cdot\mathbf r-\omega_1t)}+A_2e^{i(\mathbf k_2\cdot\mathbf r-\omega_2t)}+{\rm c.c.},\qquad(7.4.1)$$

$k_i=n_0\omega_i/c$. Intensidad (promedio sobre muchos periodos ópticos):

$$I=n_0\epsilon_0c\langle\tilde E^2\rangle,\qquad(7.4.2)$$
$$I=2n_0\epsilon_0c\{A_1A_1^*+A_2A_2^*+[A_1A_2^*e^{i(\mathbf k_1-\mathbf k_2)\cdot\mathbf r-i(\omega_1-\omega_2)t}+{\rm c.c.}]\}=2n_0\epsilon_0c\{A_1A_1^*+A_2A_2^*+[A_1A_2^*e^{i(\mathbf q\cdot\mathbf r-\delta t)}+{\rm c.c.}]\},\qquad(7.4.3)$$

con el vector de onda de la rejilla y la diferencia de frecuencias

$$\mathbf q=\mathbf k_1-\mathbf k_2,\qquad(7.4.4a)$$
$$\delta=\omega_1-\omega_2.\qquad(7.4.4b)$$

Fig. 7.4.2 (p. 371): patrón de interferencia (franjas perpendiculares a $\mathbf q$), con $|\delta|\ll\omega_1$; se mueve hacia
arriba (a lo largo de $\mathbf q$) si $\delta>0$, hacia abajo si $\delta<0$, y es estacionario si $\delta=0$. Caso simple
$\theta=180^\circ$ (haces contrapropagantes, Fig. 7.4.3), con $|\delta|\ll\omega_1$:

$$\mathbf q\simeq-2\mathbf k_2,\qquad(7.4.5)$$
$$I=2n_0\epsilon_0c\{A_1A_1^*+A_2A_2^*+[A_1A_2^*e^{i(-2kz-\delta t)}+{\rm c.c.}]\}.\qquad(7.4.6)$$

El patrón se mueve a la izquierda si $\delta>0$ y a la derecha si $\delta<0$, con velocidad de fase $|\delta|/2k$.

La variación de intensidad induce una rejilla de índice que difracta cada onda. Para un material de **respuesta
instantánea no hay transferencia de energía**. Para permitirla, el índice no lineal obedece una ecuación de
relajación de Debye:

$$\tau\frac{dn_{\rm NL}}{dt}+n_{\rm NL}=n_2I,\qquad(7.4.7)$$

que en estado estacionario da $n_{\rm NL}=n_2I$ (consistente con (4.1.15)) y en régimen transitorio predice que la no
linealidad se establece en un tiempo $\sim\tau$. Solución (variación de parámetros o función de Green):

$$n_{\rm NL}=\frac{n_2}{\tau}\int_{-\infty}^tI(t')e^{(t'-t)/\tau}dt'.\qquad(7.4.8)$$

La parte de $I(t)$ que varía como $e^{-i\delta t}$ da (p. 372)

$$\int_{-\infty}^te^{-i\delta t'}e^{(t'-t)/\tau}dt'=e^{-t/\tau}\int_{-\infty}^te^{(-i\delta+1/\tau)t'}dt'=\frac{e^{-i\delta t}}{-i\delta+1/\tau},\qquad(7.4.9)$$

de modo que

$$n_{\rm NL}=2n_0n_2\epsilon_0c\left[(A_1A_1^*+A_2A_2^*)+\frac{A_1A_2^*e^{i(\mathbf q\cdot\mathbf r-\delta t)}}{1-i\delta\tau}+\frac{A_1^*A_2e^{-i(\mathbf q\cdot\mathbf r-\delta t)}}{1+i\delta\tau}\right].\qquad(7.4.10)$$

Por los denominadores complejos, la rejilla de índice no está en general en fase con la de intensidad.

Ecuación de onda

$$\nabla^2\tilde E-\frac{n^2}{c^2}\frac{\partial^2\tilde E}{\partial t^2}=0,\qquad(7.4.11)$$
$$n=n_0+n_{\rm NL},\qquad(7.4.12)$$

con $|n_{\rm NL}|\ll n_0$:

$$n^2=n_0^2+2n_0n_{\rm NL}.\qquad(7.4.13)$$

La parte de (7.4.11) con dependencia $\exp[i(\mathbf k_2\cdot\mathbf r-\omega_2t)]$ es (p. 373)

$$\frac{d^2A_2}{dz^2}+2ik_2\frac{dA_2}{dz}-k_2^2A_2+\frac{n_0^2\omega_2^2}{c^2}A_2=-\frac{4n_0^2n_2\omega_2^2\epsilon_0}{c}(|A_1|^2+|A_2|^2)A_2-\frac{4n_0^2n_2\omega_1^2\epsilon_0}{c}\frac{|A_1|^2A_2}{1+i\delta\tau}.\qquad(7.4.14)$$

El último término proviene de la difracción de $A_1\exp[i(\mathbf k_1\cdot\mathbf r-\omega_1t)]$ en la rejilla móvil
$(2n_0\epsilon_0n_2/c)A_1^*A_2e^{-i(\mathbf q\cdot\mathbf r-\delta t)}/(1+i\delta\tau)$; el primero, de la difracción de $A_2$ en la
variación estacionaria de índice $(2n_0\epsilon_0n_2/c)(A_1A_1^*+A_2A_2^*)$. [*Lectura:* estas dos expresiones del texto
llevan "$/c$", mientras que (7.4.10) lleva el factor $\epsilon_0c$; por consistencia con (7.4.10) deberían llevar
$\epsilon_0c$ en vez de $\epsilon_0/c$.] Con la aproximación de amplitud lentamente variable se elimina el primer término
y el tercero y cuarto se cancelan:

$$\frac{dA_2}{dz}=2in_0n_2(\omega/c)\left[(|A_1|^2+|A_2|^2)A_2+\frac{|A_1|^2A_2}{1+i\delta\tau}\right],\qquad(7.4.15)$$

con $\omega_1\simeq\omega_2\simeq\omega$. *Errata:* dividiendo (7.4.14) entre $2ik_2$ el prefactor resulta $2in_0n_2\epsilon_0\omega=2in_0n_2(\omega/c)\,\epsilon_0c$;
(7.4.15) omite el factor $\epsilon_0c$. Con él, (7.4.18) sale correcta. Intensidades

$$I_1=2n_0\epsilon_0cA_1A_1^*\quad\text{y}\quad I_2=2n_0\epsilon_0cA_2A_2^*,\qquad(7.4.16)$$
$$\frac{dI_2}{dz}=2n_0\epsilon_0c\left(A_2^*\frac{dA_2}{dz}+A_2\frac{dA_2^*}{dz}\right).\qquad(7.4.17)$$

Usando ${\rm Re}[i/(1+i\delta\tau)]=\delta\tau/(1+\delta^2\tau^2)$:

$$\frac{dI_2}{dz}=\frac{2n_2\omega}{c}\frac{\delta\tau}{1+\delta^2\tau^2}I_1I_2.\qquad(7.4.18)$$

Solo el último término de (7.4.15) produce transferencia de energía. Con $n_2>0$ (Kerr por orientación molecular,
electrostricción, átomo de dos niveles con frecuencias por encima de resonancia) hay **ganancia para $\delta>0$, es
decir $\omega_2<\omega_1$** (el haz de menor frecuencia gana). Fig. 7.4.4 (p. 374): $\delta\tau/(1+\delta^2\tau^2)$ vs
$\delta\tau=(\omega_1-\omega_2)\tau$ de $-20$ a $20$; curva dispersiva impar con extremos $\pm0.5$ en $\delta\tau=\pm1$.
Ganancia máxima para $\delta\tau=1$:

$$\frac{dI_2}{dz}=n_2\frac{\omega}{c}I_1I_2.\qquad(7.4.19)$$

Para no linealidad infinitamente rápida ($\tau\to0$) el acoplamiento se anula: solo la parte imaginaria del índice
(total) cambia la intensidad de la onda $\omega_2$, y según (7.4.10), para $n_2$ real, $n_{\rm NL}$ solo es complejo si
$\tau\neq0$ (la respuesta se retrasa en fase respecto al término que la impulsa). No hay acoplamiento si $\delta\tau=0$
(respuesta rápida o haces de igual frecuencia). Excepción: en ciertos **cristales fotorrefractivos** hay acoplamiento
incluso con frecuencias iguales (Feinberg, 1983), por un desfase **espacial** entre la rejilla de índice y la de
intensidad; la dirección del flujo de energía depende de la orientación de los vectores de onda respecto a un eje
de simetría del cristal (cap. 11).

## 7.5 Pulse Propagation and Temporal Solitons — propagación de pulsos y solitones temporales (p. 375)

Pulsos cortos en medios dispersivos no lineales: el contenido espectral cambia por **automodulación de fase (SPM)**,
importante para pulsos de alta intensidad pico; la forma cambia (aun en medios lineales) por **dispersión de la
velocidad de grupo (GVD)**, importante para pulsos muy cortos (espectro ancho). Normalmente ocurren a la vez; bajo
ciertas condiciones se compensan exactamente y un **solitón óptico** se propaga grandes distancias sin cambiar de forma.

### 7.5.1 Self-Phase Modulation — automodulación de fase (p. 375)

SPM: cambio de fase de un pulso óptico por la no linealidad del índice. Pulso

$$\tilde E(z,t)=\tilde A(z,t)e^{i(k_0z-\omega_0t)}+{\rm c.c.}\qquad(7.5.1)$$

en un medio con

$$n(t)=n_0+n_2I(t),\qquad(7.5.2)$$

$I(t)=2n_0\epsilon_0c|\tilde A(z,t)|^2$. Supuestos: respuesta esencialmente instantánea y medio suficientemente corto
para que el pulso no se redistribuya dentro de él; el único efecto es cambiar la fase del pulso transmitido en

$$\phi_{\rm NL}(t)=-n_2I(t)\omega_0L/c.\qquad(7.5.3)$$

(Signo: la fase se define en el factor $e^{-i\omega_0t-i\phi_{\rm NL}(t)}$, ver (7.5.4).) El espectro se modifica y en
general se ensancha. Espectro de energía (p. 376):

$$S(\omega)=\left|\int_{-\infty}^{\infty}\tilde A(t)e^{-i\omega_0t-i\phi_{\rm NL}(t)}e^{i\omega t}dt\right|^2.\qquad(7.5.4)$$

Más intuitivo: **frecuencia instantánea**

$$\omega(t)=\omega_0+\delta\omega(t),\qquad(7.5.5a)$$
$$\delta\omega(t)=\frac{d}{dt}\phi_{\rm NL}(t),\qquad(7.5.5b)$$

concepto bien definido si $\tilde A(t)$ varía lentamente frente a un periodo óptico. Ejemplo (Fig. 7.5.1a), pulso

$$I(t)=I_0\,{\rm sech}^2(t/\tau_0):\qquad(7.5.6)$$
$$\phi_{\rm NL}(t)=-n_2\frac{\omega_0}{c}LI_0\,{\rm sech}^2(t/\tau_0),\qquad(7.5.7)$$
$$\delta\omega(t)=2n_2\frac{\omega_0}{c\tau_0}LI_0\,{\rm sech}^2(t/\tau_0)\tanh(t/\tau_0).\qquad(7.5.8)$$

Con $n_2>0$ (Fig. 7.5.1b): el **flanco anterior se desplaza a frecuencias menores (rojo)** y el **posterior a
frecuencias mayores (azul)**; Fig. 7.5.1c: pulso a la salida del medio de longitud $L$ con $n_2>0$, "blue" atrás y
"red" adelante. Desplazamiento máximo del orden de

$$\delta\omega_{\max}\simeq\frac{\Delta\phi_{\rm NL}^{(\max)}}{\tau_0},\quad\text{donde}\quad\Delta\phi_{\rm NL}^{(\max)}\simeq n_2\frac{\omega_0}{c}I_0L.\qquad(7.5.9)$$

El ensanchamiento por SPM es importante cuando $\delta\omega_{\max}$ supera el ancho espectral del pulso incidente,
$\sim1/\tau_0$ para un pulso suave; se espera que la SPM sea importante cuando $\Delta\phi_{\rm NL}^{(\max)}\ge2\pi$ (p. 377).
[*Lectura:* con el criterio $\delta\omega_{\max}>1/\tau_0$ se obtendría $\Delta\phi^{(\max)}_{\rm NL}\gtrsim1$; el $2\pi$ del texto es
un criterio de orden de magnitud. Un resultado útil fuera del libro: el número de picos del espectro SPM es
$\approx\Delta\phi^{(\max)}_{\rm NL}/\pi$.] [Verificación: el máximo de ${\rm sech}^2x\tanh x$ es $2/(3\sqrt3)\approx0.385$ en
$x={\rm arctanh}(1/\sqrt3)\approx0.66$, de modo que $\delta\omega_{\max}=0.77\,\Delta\phi^{(\max)}_{\rm NL}/\tau_0$.]

Estudiada inicialmente por Brewer (1967), Shimizu (1967) y Cheung et al. (1968); su uso para medir el índice no
lineal de fibras ópticas: Kim et al. (1994).

### 7.5.2 Pulse Propagation Equation — ecuación de propagación de pulsos (p. 377)

Pulso

$$\tilde E(z,t)=\tilde A(z,t)e^{i(k_0z-\omega_0t)}+{\rm c.c.},\qquad(7.5.10)$$

con $k_0=n_{\rm lin}(\omega_0)\omega_0/c$, en medio dispersivo no lineal. Ecuación de onda (ver (2.1.9a)), p. 378:

$$\frac{\partial^2\tilde E}{\partial z^2}-\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde D}{\partial t^2}=0,\qquad(7.5.11)$$

$\tilde D$ desplazamiento total (lineal + no lineal). Transformadas de Fourier:

$$\tilde E(z,t)=\int_{-\infty}^{\infty}E(z,\omega)e^{-i\omega t}\frac{d\omega}{2\pi},\qquad\tilde D(z,t)=\int_{-\infty}^{\infty}D(z,\omega)e^{-i\omega t}\frac{d\omega}{2\pi},\qquad(7.5.12)$$
$$D(z,\omega)=\epsilon_0\epsilon(\omega)E(z,\omega),\qquad(7.5.13)$$

$\epsilon(\omega)$: constante dieléctrica efectiva (lineal + no lineal). Cada componente de Fourier cumple

$$\frac{\partial^2E(z,\omega)}{\partial z^2}+\epsilon(\omega)\frac{\omega^2}{c^2}E(z,\omega)=0.\qquad(7.5.14)$$

Transformada de la envolvente:

$$A(z,\omega')=\int_{-\infty}^{\infty}\tilde A(z,t)e^{i\omega't}dt,\qquad(7.5.15)$$
$$E(z,\omega)=A(z,\omega-\omega_0)e^{ik_0z}+A^*(z,\omega+\omega_0)e^{-ik_0z}\simeq A(z,\omega-\omega_0)e^{ik_0z},\qquad(7.5.16)$$

(la forma aproximada porque una envolvente lenta no tiene componentes de alta frecuencia). Sustituyendo en (7.5.14)
y despreciando $\partial^2A/\partial z^2$ (amplitud lentamente variable):

$$2ik_0\frac{\partial A}{\partial z}+(k^2-k_0^2)A=0,\qquad(7.5.17)$$
$$k(\omega)=\sqrt{\epsilon(\omega)}\,\omega/c.\qquad(7.5.18),\ \text{p. 379}$$

Como $k$ difiere poco de $k_0$, $k^2-k_0^2\simeq2k_0(k-k_0)$:

$$\frac{\partial A(z,\omega-\omega_0)}{\partial z}-i(k-k_0)A(z,\omega-\omega_0)=0.\qquad(7.5.19)$$

$k$ depende de la frecuencia y (vía $\epsilon$) de la intensidad; serie truncada:

$$k=k_0+\Delta k_{\rm NL}+k_1(\omega-\omega_0)+\tfrac12k_2(\omega-\omega_0)^2,\qquad(7.5.20)$$

con la contribución no lineal

$$\Delta k_{\rm NL}=\Delta n_{\rm NL}\omega_0/c=n_2I\omega_0/c,\qquad(7.5.21)$$

$I=2n_{\rm lin}(\omega_0)\epsilon_0c|\tilde A(z,t)|^2$, y

$$k_1=\left(\frac{dk}{d\omega}\right)_{\omega=\omega_0}=\frac1c\left[n_{\rm lin}(\omega)+\omega\frac{dn_{\rm lin}(\omega)}{d\omega}\right]_{\omega=\omega_0}\equiv\frac{1}{v_g(\omega_0)},\qquad(7.5.22)$$
$$k_2=\left(\frac{d^2k}{d\omega^2}\right)_{\omega=\omega_0}=\frac{d}{d\omega}\left[\frac{1}{v_g(\omega)}\right]_{\omega=\omega_0}=\left(-\frac{1}{v_g^2}\frac{dv_g}{d\omega}\right)_{\omega=\omega_0}.\qquad(7.5.23)$$

$k_1$ es el inverso de la velocidad de grupo y $k_2$ mide la GVD (en la notación de fibras, $k_2\equiv\beta_2$). Fig. 7.5.2
(p. 380): con $k_2>0$ (dispersión normal) las componentes de longitud de onda larga (rojo) van más rápido que las
cortas (azul), y el pulso sale con el rojo adelante; con $k_2<0$ (anómala) al revés, el azul adelante.

Sustituyendo (7.5.20) en (7.5.19):

$$\frac{\partial A}{\partial z}-i\Delta k_{\rm NL}A-ik_1(\omega-\omega_0)A-\tfrac12ik_2(\omega-\omega_0)^2A=0.\qquad(7.5.24)$$

Paso al dominio temporal: multiplicar por $\exp[-i(\omega-\omega_0)t]$ e integrar sobre $\omega-\omega_0$:

$$\int_{-\infty}^{\infty}A(z,\omega-\omega_0)e^{-i(\omega-\omega_0)t}\frac{d(\omega-\omega_0)}{2\pi}=\tilde A(z,t),\qquad(7.5.25a)$$
$$\int_{-\infty}^{\infty}(\omega-\omega_0)A(z,\omega-\omega_0)e^{-i(\omega-\omega_0)t}\frac{d(\omega-\omega_0)}{2\pi}=\frac{1}{-i}\frac{\partial}{\partial t}\int_{-\infty}^{\infty}A\,e^{-i(\omega-\omega_0)t}\frac{d(\omega-\omega_0)}{2\pi}=i\frac{\partial}{\partial t}\tilde A(z,t),\qquad(7.5.25b)$$
$$\int_{-\infty}^{\infty}(\omega-\omega_0)^2A(z,\omega-\omega_0)e^{-i(\omega-\omega_0)t}\frac{d(\omega-\omega_0)}{2\pi}=-\frac{\partial^2}{\partial t^2}\tilde A(z,t).\qquad(7.5.25c)$$

Resultado:

$$\frac{\partial\tilde A}{\partial z}+k_1\frac{\partial\tilde A}{\partial t}+\tfrac12ik_2\frac{\partial^2\tilde A}{\partial t^2}-i\Delta k_{\rm NL}\tilde A=0.\qquad(7.5.26)$$

**Tiempo retardado** (p. 381):

$$\tau=t-\frac{z}{v_g}=t-k_1z,\qquad(7.5.27)$$
$$\tilde A_s(z,\tau)=\tilde A(z,t).\qquad(7.5.28)$$

Regla de la cadena:

$$\frac{\partial\tilde A}{\partial z}=\frac{\partial\tilde A_s}{\partial z}+\frac{\partial\tilde A_s}{\partial\tau}\frac{\partial\tau}{\partial z}=\frac{\partial\tilde A_s}{\partial z}-k_1\frac{\partial\tilde A_s}{\partial\tau},\qquad(7.5.29a)$$
$$\frac{\partial\tilde A}{\partial t}=\frac{\partial\tilde A_s}{\partial z}\frac{\partial z}{\partial t}+\frac{\partial\tilde A_s}{\partial\tau}\frac{\partial\tau}{\partial t}=\frac{\partial\tilde A_s}{\partial\tau},\qquad(7.5.29b)$$

y $\partial^2\tilde A/\partial t^2=\partial^2\tilde A_s/\partial\tau^2$. Entonces

$$\frac{\partial\tilde A_s}{\partial z}+\tfrac12ik_2\frac{\partial^2\tilde A_s}{\partial\tau^2}-i\Delta k_{\rm NL}\tilde A_s=0.\qquad(7.5.30)$$

Con

$$\Delta k_{\rm NL}=n_2\frac{\omega_0}{c}I=2n_0\epsilon_0n_2\omega_0|\tilde A_s|^2\equiv\gamma|\tilde A_s|^2,\qquad(7.5.31)$$

$$\boxed{\frac{\partial\tilde A_s}{\partial z}+\tfrac12ik_2\frac{\partial^2\tilde A_s}{\partial\tau^2}=i\gamma|\tilde A_s|^2\tilde A_s.}\qquad(7.5.32)$$

Es la **ecuación no lineal de Schrödinger (NLSE)** para pulsos en medios dispersivos no lineales: el segundo término
del lado izquierdo describe la tendencia del pulso a ensancharse por GVD y el lado derecho, por SPM (el libro dice
"spread"; la SPM ensancha el espectro, no la envolvente temporal). [Nota: aquí $\gamma=2n_0\epsilon_0n_2\omega_0$ multiplica
$|\tilde A_s|^2$ en (V/m)²; equivale al $\gamma=n_2\omega_0/(cA_{\rm eff})$ de fibras (W⁻¹m⁻¹) cuando la amplitud se normaliza
a potencia.]

### 7.5.3 Temporal Optical Solitons — solitones ópticos temporales (p. 381)

Según (7.5.32), la GVD puede compensar la SPM; en condiciones apropiadas, por completo, y el pulso se propaga con
forma invariante: **solitón óptico temporal**. (7.5.32) se satisface idénticamente con (p. 382)

$$\tilde A_s(z,\tau)=A_s^0\,{\rm sech}(\tau/\tau_0)e^{i\kappa z},\qquad(7.5.33a)$$

si amplitud y ancho cumplen

$$|A_s^0|^2=\frac{-k_2}{\gamma\tau_0^2}=\frac{-k_2}{2n_0\epsilon_0n_2\omega_0\tau_0^2},\qquad(7.5.33b)$$

y

$$\kappa=-k_2/2\tau_0^2=\tfrac12\gamma|A_s^0|^2\qquad(7.5.33c)$$

es el desfase acumulado por el pulso al propagarse. [Verificación: con $\partial_\tau^2{\rm sech}(\tau/\tau_0)=\tau_0^{-2}({\rm sech}-2\,{\rm sech}^3)$,
el término constante da $\kappa=-k_2/2\tau_0^2$ y el término en ${\rm sech}^2$ da $-k_2/\tau_0^2=\gamma|A_s^0|^2$.] El libro remite
la verificación al "Problem 15", pero el problema correspondiente es el **16** (errata de referencia).

(7.5.33b) exige que **$k_2$ y $n_2$ tengan signos opuestos** para que $|A_s^0|^2$ y $\tau_0^2$ sean positivos. De (7.5.32): $k_2$ y
$\gamma$ deben tener signos opuestos para que la GVD compense la SPM, porque $\tilde A_s^{-1}(\partial^2\tilde A_s/\partial\tau^2)$ es negativo
cerca del pico del pulso, donde $|\tilde A_s|^2\tilde A_s$ es más importante. Es el **solitón fundamental**; hay solitones de
orden superior, obtenidos primero por dispersión inversa (Zakharov y Shabat, 1972), descritos en Agrawal (1989).

**Fibras de sílice.** La no linealidad es electrónica, $n_2>0$; $k_2>0$ en el visible y se vuelve **negativo para
$\lambda\gtrsim1.3\ \mu$m**. Fig. 7.5.3 (p. 383): $n_{\rm lin}$ y $n_g=c/v_g$ de la sílice fundida vs $\lambda$ (0.5–1.6 μm):
$n_{\rm lin}$ baja monótonamente de $\approx1.46$ a $\approx1.444$; $n_g$ baja de $\approx1.49$ a un mínimo $\approx1.462$ cerca
de 1.3 μm (dispersión cero de la GVD, $dn_g/d\lambda=0$) y luego sube ligeramente. Solitones observados por Mollenauer
et al. (1980) a 1.55 μm con un láser de centros de color.

---

## Tablas y datos numéricos útiles

| Magnitud | Valor | Fuente |
|---|---|---|
| $P_{\rm cr}$ (autoatrapamiento) | $\pi(0.61)^2\lambda_0^2/8n_0n_2\approx\lambda_0^2/8n_0n_2$ | (7.1.10), p. 333 |
| CS₂ | $n_2=3.2\times10^{-18}$ m²/W, $n_0=1.7$, $P_{\rm cr}=27$ kW a 1 μm | p. 335 |
| Cristales y vidrios típicos | $n_2=5\times10^{-20}$–$5\times10^{-19}$ m²/W; $P_{\rm cr}=0.2$–2 MW | p. 335 |
| Ejemplo Nd:YAG Q‑switch | 1.06 μm, 10 mJ, 10 ns ($\sim1$ MW), $w_0=100\ \mu$m → $z_{\rm sf}=1$ cm en CS₂ | p. 335 |
| Ruptura en filamentos | $q_{\max}=2\sqrt{k\gamma}$, $q_{\rm opt}=q_{\max}/\sqrt2$, $\Lambda_{\max}=\gamma=n_2k_{\rm vac}I$; $P_{\rm fil}=\lambda^2/8n_0n_2$ | p. 339–340 |
| Umbral de ruptura | $G\approx3$–10; $P/P_{\rm cr}=4G^2$; $G=5\Rightarrow P>100P_{\rm cr}$ | p. 341 |
| Reflectividad PCM por DFWM | $R=\tan^2|\kappa|L$, $\kappa=(3\omega/nc)\chi^{(3)}A_1A_2$ | (7.2.37), p. 353 |
| $B/A$ (Maker–Terhune) | orientación molecular 6; electrostricción 0; electrónica no resonante 1 | p. 357 |
| Biestabilidad absortiva | aparece para $C_0>8$ (curvas $C_0=0,5,10,15,20$) | Fig. 7.3.3, p. 362 |
| Conmutación MZI | requiere $\phi_{\rm NL}=\pi$; $L_{\rm eff}=(1-e^{-\alpha L})/\alpha$ | p. 367–368 |
| Acoplamiento de dos haces | ganancia máxima en $\delta\tau=1$: $dI_2/dz=n_2(\omega/c)I_1I_2$ | (7.4.19), p. 374 |
| SPM | $\delta\omega_{\max}\simeq\Delta\phi^{(\max)}_{\rm NL}/\tau_0$, importante si $\Delta\phi^{(\max)}_{\rm NL}\ge2\pi$ | p. 376–377 |
| Fibra de sílice (Prob. 17) | $k_2=-20$ ps²/km, $n_2=3\times10^{-16}$ cm²/W; solitón $\tau_0=10$ ps, núcleo 8 μm, 1.55 μm: $P=80$ mW, $Q=0.8$ pJ; FWHM $=1.76\tau_0$ | p. 387 |
| GVD cero de la sílice | $\approx1.3\ \mu$m | p. 382, Fig. 7.5.3 |

---

## Problemas del capítulo 7 (p. 383–388)

1. *Spatial solitons.* Verificar que (7.1.19)–(7.1.21) satisfacen (7.1.18).
2. *Self-focusing and beam breakup.* Leer con cuidado la subsección de (7.1.41)–(7.1.43) y escribir un ensayo corto
   (uno o dos párrafos) sobre cómo observar filamentación en el laboratorio con un pulso de 10 ns (supuesto de perfil
   temporal cuadrado) usando la respuesta no lineal del disulfuro de carbono. Discutir la energía de pulso necesaria,
   la longitud de la región de interacción y las características de enfoque del haz.
3. *Z-scan.* Desarrollar una descripción matemática del método z‑scan para medir el índice no lineal: la muestra se
   traslada longitudinalmente por la región de la cintura de un haz gaussiano enfocado y se mide la intensidad en el
   eje en campo lejano (potencia transmitida por una abertura pequeña en el eje) en función de la posición; la
   variación es proporcional al desfase no lineal, del que se obtiene $n_2$ conociendo el espesor $L$ y la intensidad.
   Derivar $\Delta I/I$ en el eje en función de la posición $z$ de la muestra respecto a la cintura $z_0$ (dependerá de
   $n_2$, $L$ y los parámetros del haz). Suponer muestra delgada: $L\ll b$ (parámetro confocal) y desfase no lineal
   máximo $\ll1$. Sugerencias: partir del haz gaussiano; el diámetro en la muestra no cambia pero la curvatura del
   frente sí (refracción no lineal); el haz modificado es aproximadamente gaussiano con otro radio de curvatura;
   propagarlo con las leyes del haz gaussiano y obtener la intensidad axial en campo lejano vs $z-z_0$. Un análisis
   más detallado (Sheik‑Bahae et al., 1990) da
   $$\frac{\Delta I}{I}=\frac{4\Phi_{\max}x}{(x^2+1)(x^2+9)},\qquad x=2(z-z_0)/b,\qquad(7.5.34)$$
   con $\Phi_{\max}$ el desfase no lineal en el eje con la muestra en la cintura. Graficar ambos resultados.
4. *Optical phase conjugation.* Resolver, con $A_3(0)$ y $A_4(L)$ arbitrarios,
   $$\frac{dA_3}{dz}=-\alpha_3A_3-i\kappa_4^*A_4^*,\qquad\frac{dA_4}{dz}=\alpha_4A_4+i\kappa_3^*A_3^*$$
   (generalizan (7.2.31) a mezcla de cuatro ondas en geometría de conjugación con medio con pérdidas).
5. *Optical phase conjugation.* Igual que el 4 pero con desajuste de fase:
   $$\frac{dA_3}{dz}=-\alpha_3A_3-i\kappa_4^*A_4^*e^{i\Delta kz},\qquad\frac{dA_4}{dz}=\alpha_4A_4+i\kappa_3^*A_3^*e^{-i\Delta kz},$$
   con $\Delta k=(\mathbf k_1+\mathbf k_2-\mathbf k_3-\mathbf k_4)\cdot\hat{\mathbf z}$, $\mathbf k_1,\mathbf k_2$ vectores de onda de los bombeos.
6. *Optical phase conjugation.* Derivar la reflectividad conjugada por DFWM usando la respuesta no lineal de un
   conjunto de átomos de "dos niveles" (aproximaciones de onda rotante y de amplitud lentamente variable; bombeos no
   modificados por la interacción). [Pista: formalismo de la §6.3; solución en Abrams y Lind, 1978.]
7. *Polarization properties of phase conjugation.* Verificar (7.2.40).
8. *Optical bistability.* Generalizar la biestabilidad absortiva a una cavidad desintonizada: $\rho^2e^{2ikl}=Re^{i\delta_0}$,
   con $\delta_0$ la desintonía en radianes. [Resp.: (7.3.10) se reemplaza por
   $$TI_1=I_2\left[1-2R\left(1-\frac{C_0T/R}{1+2I_2/I_s}\right)\cos\delta_0+R^2\left(1-\frac{C_0T/R}{1+2I_2/I_s}\right)^2\right].$$
   Se requieren valores mayores de $C_0$ e $I_2$ para obtener biestabilidad con $\delta_0\neq0$.]
9. *Optical bistability.* Muchos absorbentes saturables no saturan hasta cero: $\alpha=\alpha_0/(1+I/I_s)+\alpha_1$, con $\alpha_1$
   constante. ¿Qué tan grande puede ser $\alpha_1$ (dado $\alpha_0$) y aún permitir biestabilidad? Usar las aproximaciones
   del texto ("$\alpha\ll1$" [debe entenderse $\alpha l\ll1$] y cavidad en resonancia exacta). ¿Cómo cambian los requisitos
   de intensidad incidente con $\alpha_1\neq0$?
10. *Optical bistability.* Con un análisis gráfico como el de la Fig. 7.3.5, graficar $I_3$ vs $I_1$. Notar que en
    biestabilidad refractiva puede haber más de dos soluciones estables.
11. *Optical bistability.* Biestabilidad refractiva en un Fabry–Perot no lineal cuyo material tiene además absorción
    (lineal). ¿Cómo se modifican los requisitos de intensidad para conmutar y qué tan grande puede ser la absorción
    y aún existir biestabilidad?
12. *Optical switching.* Mostrar que cualquier divisor de haz físicamente realizable debe cumplir (7.3.21).
13. *Two-beam coupling.* Según la §7.4, $dI_1/dz=\beta I_1I_2$, $dI_2/dz=-\beta I_1I_2$. Resolver para $I_2(z)$ en términos de
    $I_2(0)$ y de la intensidad total $I=I_1+I_2$. Esbozar $I_2(z)$ para $\beta>0$ y $\beta<0$. ¿Qué es $\beta$, matemática y
    físicamente?
14. *Self-phase modulation.* El análisis de la Fig. 7.5.1 supuso respuesta instantánea y pulso simétrico (espectro
    ensanchado simétricamente). ¿Cómo cambia el espectro con un medio de respuesta lenta (p. ej., (7.4.7) con $\tau$
    mucho mayor que la duración del pulso)? ¿Y si el pulso no es simétrico (p. ej., diente de sierra)?
15. *Pulse propagation.* ¿Cómo se modifica (7.5.32) si $k^2-k_0^2$ no se aproxima por $2k_0(k-k_0)$, como se hizo al pasar
    de "(7.5.18) a (7.1.19)" [errata: debe ser de (7.5.17) a (7.5.19)]? [Resp.: $k_2$ en (7.5.32) se reemplaza por
    $(k_1^2+2k_0k_2)/2k_0$.] ¿Por qué esta nueva ecuación parece predecir que los pulsos se ensanchan aunque $k_2$ y
    $\gamma$ se anulen?
16. *Temporal solitons.* Verificar que (7.5.33) satisface (7.5.32).
17. *Temporal solitons.* Calcular la potencia pico y la energía de un solitón con $\tau_0=10$ ps en una fibra de núcleo de
    sílice de 8 μm de diámetro a 1.55 μm. [Solución: con $k_2=-20$ ps²/km y $n_2=3\times10^{-16}$ cm²/W, $P=80$ mW y
    $Q=0.8$ pJ. El ancho completo a media intensidad es $1.76\tau_0$.]
18. *Self-induced transparency.* Solitones por respuesta resonante de átomos de dos niveles. Mostrar que, sin
    amortiguamiento y en resonancia exacta, la propagación obedece (respuesta atómica como en la §6.4; *ecuaciones en
    unidades gaussianas*, nótese el $2\pi$)
    $$\frac{\partial\tilde A}{\partial z}+\frac1c\frac{\partial\tilde A}{\partial t}=\frac{2\pi i\omega N}{c}p,\qquad\frac{dp}{dt}=-\frac i\hbar|\mu|^2\tilde Aw,\qquad\frac{dw}{dt}=\frac{-4i}{\hbar}\tilde Ap,$$
    y que admiten soluciones tipo solitón
    $$\tilde A(z,t)=\frac{\hbar}{\mu\tau_0}{\rm sech}\left(\frac{t-z/v}{\tau_0}\right),\quad w(z,t)=-1+2\,{\rm sech}^2\left(\frac{t-z/v}{\tau_0}\right),\quad p(z,t)=-i\mu\,{\rm sech}\left(\frac{t-z/v}{\tau_0}\right)\tanh\left(\frac{t-z/v}{\tau_0}\right),$$
    siempre que $c/v=1+2\pi N\mu^2\omega\tau_0^2/\hbar$. ¿Cuál es el valor (y el significado) de $\int_{-\infty}^{\infty}(2\mu/\hbar)\tilde A(z,t)\,dt$?
    (Para un medio con ensanchamiento inhomogéneo las ecuaciones aún admiten un pulso sech, pero con otra relación
    entre $v$ y $\tau_0$; ver Allen y Eberly, 1975.) [El valor es $2\pi$: pulso de área $2\pi$.]
19. *Modulational instability.* Determinar cuándo la propagación de un campo monocromático en una fibra es inestable
    frente al crecimiento de nuevas frecuencias, a partir de la NLSE (7.5.32). La solución para una onda continua es
    el campo de entrada por un factor de fase no lineal. Estudiar su estabilidad con
    $A(z,\tau)=A_0(z)+A_1(z)e^{-i\delta\tau}+A_2(z)e^{i\delta\tau}$ (bombeo $A_0$ a $\omega$ y bandas laterales débiles a $\pm\delta$; se omiten
    la tilde y el subíndice $s$). Linealizar en $A_1,A_2$ (acoplados por mezcla de cuatro ondas), hallar la condición de
    crecimiento exponencial, ¿para qué signo relativo de $n_2$ y $k_2$ existe la inestabilidad?, esbozar la ganancia vs
    $\delta$ para varios $A_0$, hallar el "autovector" que crece y describir la modulación del campo transmitido.
    Pregunta conceptual: ¿por qué la solución depende de la velocidad de grupo y no de la de fase, si el análisis es en
    onda continua?

**Referencias principales (p. 388–390).** Autoenfoque: Kelly (1965) PRL 15, 1005; Chiao, Garmire y Townes (1964) PRL
13, 479; Bespalov y Talanov (1966) JETP Lett. 3, 471; Bjorkholm y Ashkin (1974) PRL 32, 129; Fibich y Gaeta (2000) Opt.
Lett. 25, 335; Loy y Shen (1973); Sheik‑Bahae et al. (1990) IEEE JQE 26, 760 (z‑scan); Marburger (1975) Prog. Quantum
Electron. 4, 35. Conjugación de fase: Hellwarth (1977) JOSA 67, 1; Yariv y Pepper (1977) Opt. Lett. 1, 16; Bloom y
Bjorklund (1977) APL 31, 592; Zel'dovich, Pilipetsky y Shkunov (1985) *Principles of Phase Conjugation*; Fisher (ed.)
(1983) *Optical Phase Conjugation*; Zel'dovich y Shkunov (1979); Martin et al. (1980). Biestabilidad: Szöke et al.
(1969) APL 15, 376; Gibbs, McCall y Venkatesan (1976) PRL 36, 1135; Gibbs (1985) *Optical Bistability*; Stegeman y Miller
(1993). Dos haces: Silberberg y Bar‑Joseph (1982, 1984). Pulsos y solitones: Agrawal (1989) *Nonlinear Fiber Optics*;
Mollenauer, Stolen y Gordon (1980) PRL 45, 1095; Zakharov y Shabat (1972) Sov. Phys. JETP 34, 63; Shimizu (1967) PRL 19,
1097; Kim et al. (1994).

---

## Relación con el curso y con el proyecto final

- **Tema 6 del programa (Boyd 4.1, 4.2, 7.1, 7.2).** Las §7.1 y §7.2 son materia del curso. Puntos clave para
  talleres y examen: (i) $\theta_{\rm sf}$, $z_{\rm sf}$ (7.1.3)–(7.1.7) y $P_{\rm cr}$ (7.1.10), con su doble derivación (difracción
  vs autoenfoque y reflexión total interna); (ii) el solitón espacial sech (7.1.19)–(7.1.21), que es la misma
  ecuación que la NLSE temporal (7.5.32) intercambiando $x\leftrightarrow\tau$ y difracción $\leftrightarrow$ GVD; (iii) el análisis
  de Bespalov–Talanov (7.1.22)–(7.1.43) como modelo de inestabilidad modulacional (su versión temporal es el
  Problema 19); (iv) la conjugación de fase: definición (7.2.2)–(7.2.5), corrección de aberraciones (7.2.9)–(7.2.11),
  DFWM (7.2.27)–(7.2.37) con $R=\tan^2|\kappa|L$ y polarización (7.2.40)–(7.2.43), que usa el tensor isótropo de la §4.2
  ($A=6\chi_{1122}$, $B=6\chi_{1221}$).
- **Equivalencia con Saleh.** Saleh & Teich cap. 21 (§21.3) trata autoenfoque, solitones espaciales, SPM y OPC con
  $\exp(j\omega t)$ y $\chi^{(3)}_{\rm S}=\epsilon_0\chi^{(3)}_{\rm B}/4$; ver la tabla de equivalencias en
  `notas/saleh/cap21-optica-no-lineal.md`. El $n_2$ en m²/W es el mismo en ambos.
- **Proyecto final (supercontinuo y no linealidades en guías de SiN/Si).** La §7.5 es la base: la NLSE (7.5.32) con
  $k_2\equiv\beta_2$ y $\gamma$ es la ecuación que, generalizada (dispersión de orden superior, Raman, *self-steepening*,
  TPA y portadores libres en Si), modela la generación de supercontinuo. Los ingredientes del libro que se usan
  directamente: SPM y el corrimiento rojo/azul (7.5.8) como mecanismo inicial de ensanchamiento; el solitón
  fundamental (7.5.33) y la condición $k_2\gamma<0$ (por eso las guías de SiN/Si se diseñan con dispersión anómala en
  el bombeo); la inestabilidad modulacional (Problema 19, análoga a 7.1.38) que siembra la fisión de solitones; la
  longitud efectiva $L_{\rm eff}$ (7.3.31) con pérdidas de propagación; y la absorción de dos fotones (7.3.33),
  $\alpha=\alpha_0+\beta I$, que es la limitación central del Si a 1.55 μm (el SiN, con brecha ancha, no tiene TPA allí,
  como en la Fig. 7.3.9b). El Problema 17 es un ejemplo numérico del orden de potencias de solitón; en guías de
  SiN/Si $A_{\rm eff}\sim0.1$–1 μm² y $n_2$ es 10–100 veces el de la sílice, de modo que $\gamma$ es miles de veces mayor.
- **Anillos (fotonica-integrada).** La biestabilidad refractiva (7.3.12)–(7.3.20) en un Fabry–Perot es la misma física
  que la biestabilidad térmica/Kerr de un microanillo (ecuación de Airy con desfase dependiente de la intensidad
  circulante); el interferómetro de onda viajera de la Fig. 7.3.2 es el análogo del anillo.

---

## Erratas y dudas de lectura

1. **(7.1.42), p. 341:** el texto dice "see Eq. (7.1.4)", pero la forma con $\sqrt{P/P_{\rm cr}-1}$ es la (7.1.6). El factor 4 de
   (7.1.43) depende de la relación entre $I$, $P$ y $w_0$, que el libro no explicita.
2. **(7.2.12), p. 347:** se lee $A_i(\mathbf r)E^{i(\mathbf k_i\cdot\mathbf r-\omega t)}$; la $E$ debe ser la exponencial $e$.
3. **(7.2.23b)–(7.2.24b), p. 350:** con la definición "$\equiv i\kappa_2A_2$" y el prefactor $-3i\omega/2nc$, $\kappa_2$ sería negativo y
   la solución $e^{+i\kappa_2z'}$; para que (7.2.24b) ($e^{-i\kappa_2z'}$) y $\kappa_1=\kappa_2$ con bombeos iguales sean consistentes,
   debe leerse $dA_2/dz'\equiv-i\kappa_2A_2$ con $\kappa_2>0$.
4. **Numeración p. 356:** la expresión $\mathbf P=6\epsilon_0\chi_{1122}(\mathbf E\cdot\mathbf E^*)\mathbf E+\dots$ no lleva número, pero el texto la
   cita como "Eq. (7.2.40)"; el número (7.2.40) está en la ecuación matricial.
5. **(7.3.5), p. 361:** se lee $I_i=2n\epsilon_0|A_i|^2$; en la convención del libro es $I_i=2n\epsilon_0c|A_i|^2$ (así aparece en la
   p. 364). No afecta los cocientes.
6. **(7.4.14)–(7.4.15), p. 373:** las rejillas se escriben con prefactor $2n_0\epsilon_0n_2/c$, mientras (7.4.10) tiene
   $2n_0n_2\epsilon_0c$; y (7.4.15) omite el factor $\epsilon_0c$ (al dividir (7.4.14) entre $2ik_2$ el prefactor es
   $2in_0n_2\epsilon_0\omega$). Con ese factor, (7.4.18) sale correcta.
7. **p. 377:** el criterio "$\delta\omega_{\max}$ mayor que $1/\tau_0$" daría $\Delta\phi^{(\max)}_{\rm NL}\gtrsim1$; el libro concluye $\ge2\pi$
   (criterio de orden de magnitud).
8. **p. 381:** el libro dice que la SPM hace que los pulsos "tiendan a ensancharse"; la SPM ensancha el espectro, no la
   envolvente temporal (en medio no dispersivo).
9. **p. 382:** remite al "Problem 15" para verificar el solitón; es el **Problema 16**.
10. **Problema 15, p. 386:** "de (7.5.18) a (7.1.19)" debe ser "de (7.5.17) a (7.5.19)".
11. **Problema 9, p. 386:** "$\alpha\ll1$" debe entenderse $\alpha l\ll1$.
12. **Problema 17, p. 387:** $P=80$ mW se reproduce con $P=|k_2|/(\gamma\tau_0^2)$, $\gamma=2\pi n_2/(\lambda A_{\rm eff})$, $A_{\rm eff}=\pi(4\ \mu{\rm m})^2$
    ($\gamma\approx2.4$ W⁻¹km⁻¹ → $P\approx83$ mW). Para un pulso ${\rm sech}^2$ la energía es $2P\tau_0\approx1.6$ pJ; el $Q=0.8$ pJ del
    libro corresponde a $P\tau_0$ (duda: posible factor 2).
13. **Problema 18:** las ecuaciones están en unidades gaussianas (factor $2\pi N$), no en SI como el resto del capítulo.
14. **Fig. 7.3.8:** en la imagen no queda claro qué curva (continua o discontinua) es cada puerto; según (7.3.25) el
    puerto 1 es máximo en $\phi_{\rm NL}=0$, coherente con la Fig. 7.3.7 (pulsos intensos al puerto 2).
