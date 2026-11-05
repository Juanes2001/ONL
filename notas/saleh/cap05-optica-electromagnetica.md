# Capítulo 5 — Electromagnetic Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 150–196 (PDF 172–218). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 5.
Todas las páginas citadas abajo son **páginas del libro** (página del PDF = página del libro + 22).

**Notación del libro (se respeta en todo el archivo).** Dependencia temporal $e^{j\omega t}$ con
$j=\sqrt{-1}$. Campos reales en caligráfica: $\mathcal{E}(\mathbf r,t)$, $\mathcal{H}$, $\mathcal{D}$,
$\mathcal{B}$, $\mathcal{P}$, $\mathcal{M}$, $\mathcal{S}$, $\mathcal{W}$. Amplitudes complejas en
negrita: $\mathbf E(\mathbf r)$, $\mathbf H$, $\mathbf P$, $\mathbf D$, $\mathbf M$, $\mathbf B$,
$\mathbf S$. Constantes del vacío con subíndice $o$: $\epsilon_o$, $\mu_o$, $c_o$, $k_o$, $\eta_o$,
$\lambda_o$. La parte imaginaria de la susceptibilidad, $\chi''$, es **negativa** en un medio
absorbente (consecuencia de usar $e^{j\omega t}$ y $k=\beta-j\tfrac12\alpha$). Unidades SI (MKS).

---

## Resumen del capítulo

El capítulo presenta la óptica electromagnética como la teoría vectorial que engloba a la óptica
ondulatoria (escalar) y a la óptica de rayos (Fig. 5.0-2, p. 151). Parte de las ecuaciones de Maxwell
en el vacío y en medios sin fuentes (§5.1), introduce las relaciones constitutivas entre
$\mathcal{P}$ y $\mathcal{E}$ que definen el carácter del medio —lineal / no lineal, dispersivo / no
dispersivo, homogéneo / inhomogéneo, isótropo / anisótropo (§5.2)— y deduce la ecuación de onda
general con la polarización como fuente, $\nabla^2\mathcal{E}-c_o^{-2}\partial_t^2\mathcal{E}
=\mu_o\partial_t^2\mathcal{P}$ (5.2-25), punto de partida de la óptica no lineal. Para luz
monocromática (§5.3) las ecuaciones se reducen a relaciones algebraicas entre amplitudes complejas,
aparece la ecuación de Helmholtz y la susceptibilidad pasa a ser $\chi(\nu)$, compleja y dependiente
de la frecuencia. §5.4 construye las ondas elementales (plana TEM, esférica del dipolo, haz
gaussiano vectorial, haces vectoriales) y precisa cuándo basta la teoría escalar. §5.5 trata la
absorción y la dispersión: $\chi=\chi'+j\chi''$, $n$ y $\alpha$, relaciones de Kramers–Kronig,
oscilador de Lorentz (lorentziana, $Q$), ecuación de Sellmeier con la Tabla 5.5-1, y medios
conductores (permitividad efectiva, profundidad de penetración, modelo de Drude, frecuencia de
plasma). §5.6 analiza la propagación de pulsos: velocidad e índice de grupo, coeficientes de
dispersión $D_\nu$ y $D_\lambda$, dispersión normal/anómala, luz rápida y lenta, y el Ejemplo 5.6-1
de la sílice (cero de dispersión en 1,276 µm). §5.7 (avanzada) cubre materiales magnéticos y
metamateriales de índice negativo.

---

## Secciones

### Introducción del capítulo (p. 150–152)

- La óptica ondulatoria (caps. 2–4) explica interferencia y difracción pero **no** la fracción de
  luz reflejada en un divisor de haz, que depende de la polarización: hace falta una teoría
  **vectorial**. La luz es un fenómeno electromagnético con dos ondas vectoriales acopladas, el campo
  eléctrico y el magnético (p. 151).
- **Fig. 5.0-1** (p. 151): espectro electromagnético de 1 kHz a 1 ZHz; la banda óptica (sombreada)
  va de ~1 THz a ~1 PHz. **Fig. 5.0-2** (p. 151): jerarquía óptica electromagnética ⊃ óptica
  ondulatoria ⊃ óptica de rayos.
- Dominio óptico: longitudes de onda de **10 nm a 300 µm** (p. 152). El cap. 6 trata polarización y
  medios anisótropos; caps. 8–11 guías, fibras y resonadores; **cap. 21 la óptica de medios no
  lineales**; el cap. 22 retoma la dispersión (p. 152).

### 5.1 Electromagnetic Theory of Light (p. 152)

Un campo electromagnético se describe por dos campos vectoriales reales, el **campo eléctrico**
$\mathcal{E}(\mathbf r,t)$ y el **campo magnético** $\mathcal{H}(\mathbf r,t)$: seis funciones
escalares acopladas por las ecuaciones de Maxwell (p. 152).

**Ecuaciones de Maxwell en el vacío** (recuadro, p. 152):

$$\nabla\times\mathcal{H}=\epsilon_o\frac{\partial\mathcal{E}}{\partial t}\qquad(5.1\text{-}1)$$
$$\nabla\times\mathcal{E}=-\mu_o\frac{\partial\mathcal{H}}{\partial t}\qquad(5.1\text{-}2)$$
$$\nabla\cdot\mathcal{E}=0\qquad(5.1\text{-}3)$$
$$\nabla\cdot\mathcal{H}=0\qquad(5.1\text{-}4)$$

con $\epsilon_o\approx(1/36\pi)\times10^{-9}$ F/m (**permitividad eléctrica** del vacío) y
$\mu_o=4\pi\times10^{-7}$ H/m (**permeabilidad magnética** del vacío) (p. 153). Nota al pie:
$\nabla\cdot\mathcal{E}=\partial_x\mathcal{E}_x+\partial_y\mathcal{E}_y+\partial_z\mathcal{E}_z$ y
$\nabla\times\mathcal{E}$ tiene componentes $(\partial_y\mathcal{E}_z-\partial_z\mathcal{E}_y,\;
\partial_z\mathcal{E}_x-\partial_x\mathcal{E}_z,\;\partial_x\mathcal{E}_y-\partial_y\mathcal{E}_x)$.

**La ecuación de onda** (p. 153). Condición necesaria: cada componente de $\mathcal{E}$ y
$\mathcal{H}$ satisface

$$\nabla^2u-\frac{1}{c_o^2}\frac{\partial^2u}{\partial t^2}=0\qquad(5.1\text{-}5)\ \text{Wave Equation (Free Space)}$$
$$c_o=\frac{1}{\sqrt{\epsilon_o\mu_o}}\approx3\times10^8\ \text{m/s}\qquad(5.1\text{-}6)\ \text{Speed of Light (Free Space)}$$

donde $u(\mathbf r,t)$ es cualquiera de $(\mathcal{E}_x,\mathcal{E}_y,\mathcal{E}_z)$ o
$(\mathcal{H}_x,\mathcal{H}_y,\mathcal{H}_z)$. Derivación: se aplica $\nabla\times$ a (5.1-2), se usa
la identidad $\nabla\times(\nabla\times\mathcal{E})=\nabla(\nabla\cdot\mathcal{E})-\nabla^2\mathcal{E}$
y luego (5.1-1) y (5.1-3). Como Maxwell y la ecuación de onda son lineales, vale el **principio de
superposición** (p. 153). La ecuación de onda (2.1-2) de la óptica ondulatoria queda así embebida en
la teoría electromagnética; la función de onda escalar $u$ representa cualquiera de las seis
componentes (p. 153).

**Ecuaciones de Maxwell en un medio** (p. 153–154). En un medio sin cargas ni corrientes libres se
necesitan dos campos más: la **densidad de flujo eléctrico** (desplazamiento) $\mathcal{D}(\mathbf r,t)$
y la **densidad de flujo magnético** $\mathcal{B}(\mathbf r,t)$ (recuadro, p. 154):

$$\nabla\times\mathcal{H}=\frac{\partial\mathcal{D}}{\partial t}\qquad(5.1\text{-}7)$$
$$\nabla\times\mathcal{E}=-\frac{\partial\mathcal{B}}{\partial t}\qquad(5.1\text{-}8)$$
$$\nabla\cdot\mathcal{D}=0\qquad(5.1\text{-}9)$$
$$\nabla\cdot\mathcal{B}=0\qquad(5.1\text{-}10)\ \text{Maxwell's Equations (Source-Free Medium)}$$

La relación $\mathcal{D}$–$\mathcal{E}$ depende de las propiedades eléctricas del medio, resumidas en
la **densidad de polarización** $\mathcal{P}$ (suma macroscópica de los momentos dipolares eléctricos
inducidos); la relación $\mathcal{B}$–$\mathcal{H}$ en la **densidad de magnetización** $\mathcal{M}$
(p. 154):

$$\mathcal{D}=\epsilon_o\mathcal{E}+\mathcal{P}\qquad(5.1\text{-}11)$$
$$\mathcal{B}=\mu_o\mathcal{H}+\mu_o\mathcal{M}\qquad(5.1\text{-}12)$$

Las relaciones $\mathcal{P}$–$\mathcal{E}$ y $\mathcal{M}$–$\mathcal{H}$ se fijan al especificar el
medio (§5.2); al sustituirlas, las densidades de flujo desaparecen. En el vacío
$\mathcal{P}=\mathcal{M}=0$ y se recuperan (5.1-1)–(5.1-4) (p. 154).

**Condiciones de frontera** (p. 154–155, Fig. 5.1-1). En un medio homogéneo todas las componentes son
continuas. En la frontera entre dos dieléctricos sin cargas ni corrientes libres: las **componentes
tangenciales de $\mathcal{E}$ y $\mathcal{H}$** y las **componentes normales de $\mathcal{D}$ y
$\mathcal{B}$** son continuas. En la frontera con un conductor perfecto la componente tangencial de
$\mathcal{E}$ se anula: en un espejo perfecto a incidencia normal la onda reflejada tiene igual
magnitud y un desfase de $\pi$ (p. 155). Estas condiciones determinan reflectancia/transmitancia
(§6.2), medios periódicos (§7.1) y guías (§8.2).

**Intensidad, potencia y energía** (p. 155). El flujo de potencia lo gobierna el **vector de
Poynting**

$$\mathcal{S}=\mathcal{E}\times\mathcal{H}\qquad(5.1\text{-}13)$$

ortogonal a $\mathcal{E}$ y $\mathcal{H}$. La **intensidad óptica** $I(\mathbf r,t)$ (potencia por
unidad de área normal a $\mathcal{S}$) es la magnitud del promedio temporal $\langle\mathcal{S}\rangle$,
promediado sobre tiempos largos frente al ciclo óptico pero cortos frente a los demás tiempos de
interés (equivalente escalar: (2.1-3)). Con la identidad
$\nabla\cdot(\mathcal{E}\times\mathcal{H})=(\nabla\times\mathcal{E})\cdot\mathcal{H}-(\nabla\times\mathcal{H})\cdot\mathcal{E}$
y (5.1-7)–(5.1-8), (5.1-11)–(5.1-12):

$$\nabla\cdot\mathcal{S}=-\frac{\partial}{\partial t}\Big(\tfrac12\epsilon_o\mathcal{E}^2+\tfrac12\mu_o\mathcal{H}^2\Big)+\mathcal{E}\cdot\frac{\partial\mathcal{P}}{\partial t}+\mu_o\mathcal{H}\cdot\frac{\partial\mathcal{M}}{\partial t}\qquad(5.1\text{-}14)$$

**Teorema de Poynting**: los dos primeros términos son las densidades de energía eléctrica y
magnética; el tercero y cuarto, la potencia por unidad de volumen entregada a los dipolos eléctricos y
magnéticos del material. Expresa conservación de energía (p. 155).

**Momento** (p. 155). Densidad de momento lineal (por unidad de volumen) en el vacío:

$$\epsilon_o\mathcal{E}\times\mathcal{B}=\frac{1}{c^2}\mathcal{S}\qquad(5.1\text{-}15)\ \text{Linear Momentum Density}$$

El momento medio en un cilindro de longitud $c$ y área unidad es $\langle\mathcal{S}\rangle/c$, que
es la tasa de flujo de momento por unidad de área (presión de radiación). La tasa media de momento
angular transportado es $\mathbf r\times\langle\mathcal{S}\rangle/c$; los haces Laguerre–Gauss
(§3.4) con frentes helicoidales llevan momento angular orbital (p. 155).

### 5.2 Electromagnetic Waves in Dielectric Media (p. 156)

El carácter del medio está en la **relación constitutiva** entre $(\mathcal{P},\mathcal{M})$ y
$(\mathcal{E},\mathcal{H})$. El libro se concentra en la relación $\mathcal{P}$–$\mathcal{E}$
(propiedades dieléctricas), vista como un sistema con entrada $\mathcal{E}(\mathbf r,t)$ y salida
$\mathcal{P}(\mathbf r,t)$ (**Fig. 5.2-1**, p. 156). Salvo §5.7 y §6.4, se ignoran las propiedades
magnéticas.

**Definiciones** (recuadro sombreado, p. 156) — clasificación de medios:

- **Lineal**: $\mathcal{P}(\mathbf r,t)$ está relacionada linealmente con $\mathcal{E}(\mathbf r,t)$.
  Aplica superposición.
- **No dispersivo**: la respuesta es instantánea; $\mathcal{P}$ en $t$ depende solo de $\mathcal{E}$
  en el mismo $t$, no de valores previos. Es una idealización: todo sistema físico tiene tiempo de
  respuesta finito.
- **Homogéneo**: la relación $\mathcal{P}$–$\mathcal{E}$ no depende de la posición $\mathbf r$.
- **Isótropo**: la relación no depende de la dirección de $\mathcal{E}$; $\mathcal{P}$ y $\mathcal{E}$
  son entonces paralelos.
- **Espacialmente no dispersivo**: la relación es local; $\mathcal{P}$ en $\mathbf r$ depende solo
  de $\mathcal{E}$ en el mismo $\mathbf r$. Se supone en todo el capítulo (los medios ópticamente
  activos, §6.4A, son espacialmente dispersivos).

#### 5.2A Linear, Nondispersive, Homogeneous, and Isotropic Media (p. 156)

$\mathcal{P}$ y $\mathcal{E}$ son paralelos y proporcionales:

$$\mathcal{P}=\epsilon_o\chi\mathcal{E}\qquad(5.2\text{-}1)$$

donde el escalar $\chi$ es la **susceptibilidad eléctrica** (**Fig. 5.2-2**, p. 157: el medio queda
caracterizado por una sola constante). Sustituyendo en (5.1-11):

$$\mathcal{D}=\epsilon\mathcal{E},\qquad(5.2\text{-}2)\qquad\epsilon=\epsilon_o(1+\chi)\qquad(5.2\text{-}3)$$

$\epsilon$ es la **permitividad eléctrica** del medio; $\epsilon/\epsilon_o=1+\chi$ es la
**permitividad relativa** o **constante dieléctrica**. Análogamente $\mathcal{B}=\mu\mathcal{H}$
(5.2-4), con $\mu$ la **permeabilidad magnética** (p. 157). Maxwell queda (recuadro, p. 157):

$$\nabla\times\mathcal{H}=\epsilon\frac{\partial\mathcal{E}}{\partial t}\ (5.2\text{-}5),\quad
\nabla\times\mathcal{E}=-\mu\frac{\partial\mathcal{H}}{\partial t}\ (5.2\text{-}6),\quad
\nabla\cdot\mathcal{E}=0\ (5.2\text{-}7),\quad\nabla\cdot\mathcal{H}=0\ (5.2\text{-}8)$$

idénticas en forma a las del vacío con $\epsilon\to\epsilon_o$, $\mu\to\mu_o$. Cada componente
satisface

$$\nabla^2u-\frac{1}{c^2}\frac{\partial^2u}{\partial t^2}=0\qquad(5.2\text{-}9)\ \text{Wave Equation (In a Medium)}$$
$$c=\frac{1}{\sqrt{\epsilon\mu}}\qquad(5.2\text{-}10)\ \text{Speed of Light (In a Medium)}$$

**Índice de refracción** (recuadros, p. 158):

$$n=\frac{c_o}{c}=\sqrt{\frac{\epsilon}{\epsilon_o}\frac{\mu}{\mu_o}}\qquad(5.2\text{-}11)\qquad c_o=\frac{1}{\sqrt{\epsilon_o\mu_o}}\qquad(5.2\text{-}12)$$

Para material **no magnético** ($\mu=\mu_o$):

$$n=\sqrt{\frac{\epsilon}{\epsilon_o}}=\sqrt{1+\chi}\qquad(5.2\text{-}13)\ \text{Refractive Index (Nonmagnetic Media)}$$

"el índice de refracción es la raíz cuadrada de la constante dieléctrica" (p. 158). El teorema de
Poynting toma forma de ecuación de continuidad:

$$\nabla\cdot\mathcal{S}=-\frac{\partial\mathcal{W}}{\partial t}\qquad(5.2\text{-}14),\qquad
\mathcal{W}=\tfrac12\epsilon\mathcal{E}^2+\tfrac12\mu\mathcal{H}^2\qquad(5.2\text{-}15)$$

con $\mathcal{W}$ la densidad de energía almacenada en el medio (p. 158).

#### 5.2B Nonlinear, Dispersive, Inhomogeneous, or Anisotropic Media (p. 158)

Medios no magnéticos en los que falla al menos una de las cuatro propiedades.

**Medios inhomogéneos** (p. 158–159; **Fig. 5.2-3**: susceptibilidad $\chi(\mathbf r)$). Se mantienen
$\mathcal{P}=\epsilon_o\chi\mathcal{E}$ y $\mathcal{D}=\epsilon\mathcal{E}$ con $\chi=\chi(\mathbf r)$,
$\epsilon=\epsilon(\mathbf r)$, $n=n(\mathbf r)$ (p. ej. medio de índice gradual). Aplicando
$\nabla\times$ a (5.1-8) y usando (5.1-7):

$$\frac{\epsilon_o}{\epsilon}\nabla\times(\nabla\times\mathcal{E})=-\frac{1}{c_o^2}\frac{\partial^2\mathcal{E}}{\partial t^2}\qquad(5.2\text{-}16)\ \text{Wave Equation (Inhomogeneous Medium)}$$
$$\nabla\times\Big(\frac{\epsilon_o}{\epsilon}\nabla\times\mathcal{H}\Big)=-\frac{1}{c_o^2}\frac{\partial^2\mathcal{H}}{\partial t^2}\qquad(5.2\text{-}17)$$

(5.2-16) también se escribe

$$\nabla^2\mathcal{E}+\nabla\Big(\frac1\epsilon\nabla\epsilon\cdot\mathcal{E}\Big)-\mu_o\epsilon\frac{\partial^2\mathcal{E}}{\partial t^2}=0\qquad(5.2\text{-}18)$$

(se usa $\nabla\cdot\epsilon\mathcal{E}=0$ y $\nabla\cdot\epsilon\mathcal{E}=\epsilon\nabla\cdot\mathcal{E}+\nabla\epsilon\cdot\mathcal{E}$,
de donde $\nabla\cdot\mathcal{E}=-(1/\epsilon)\nabla\epsilon\cdot\mathcal{E}$). Si $\epsilon(\mathbf r)$
varía lentamente (constante en distancias del orden de $\lambda$), el segundo término es despreciable:

$$\nabla^2\mathcal{E}-\frac{1}{c^2(\mathbf r)}\frac{\partial^2\mathcal{E}}{\partial t^2}\approx0\qquad(5.2\text{-}19)$$

con $c(\mathbf r)=1/\sqrt{\mu_o\epsilon}=c_o/n(\mathbf r)$ y $n(\mathbf r)=\sqrt{\epsilon(\mathbf r)/\epsilon_o}$
(relación invocada sin prueba en el cap. 2). Para un medio homogéneo de índice $n$ perturbado por un
cambio lento $\Delta n$ (p. 159):

$$\nabla^2\mathcal{E}-\frac{1}{c^2}\frac{\partial^2\mathcal{E}}{\partial t^2}\approx-\mathcal{S},\qquad
\mathcal{S}=-\mu_o\frac{\partial^2\Delta\mathcal{P}}{\partial t^2},\qquad
\Delta\mathcal{P}=2\epsilon_on\,\Delta n\,\mathcal{E}\qquad(5.2\text{-}20)$$

con $c=c_o/n$: $\mathcal{E}$ satisface la ecuación de onda con una **fuente de radiación** creada por
la perturbación $\Delta\mathcal{P}$ de la polarización, proporcional a $\Delta n$ y a $\mathcal{E}$.
Se verifica expandiendo $1/c^2(\mathbf r)=(n+\Delta n)^2/c_o^2\approx(n^2+2n\Delta n)/c_o^2$ y notando
que $\mathcal{P}=\epsilon_o(n^2-1)\mathcal{E}$, de modo que
$\Delta\mathcal{P}=\epsilon_o\Delta(n^2-1)\mathcal{E}=2\epsilon_on\Delta n\mathcal{E}$ (p. 159).

**Medios anisótropos** (p. 160; **Fig. 5.2-4**: nueve constantes $\chi_{ij}$). $\mathcal{P}$ y
$\mathcal{E}$ dejan de ser paralelos; si el medio es lineal, no dispersivo y homogéneo:

$$\mathcal{P}_i=\sum_j\epsilon_o\chi_{ij}\mathcal{E}_j\qquad(5.2\text{-}21),\qquad
\mathcal{D}_i=\sum_j\epsilon_{ij}\mathcal{E}_j\qquad(5.2\text{-}22)$$

$i,j=1,2,3$ ↔ $x,y,z$; $\{\chi_{ij}\}$ es el **tensor de susceptibilidad eléctrica** $\boldsymbol\chi$
y $\{\epsilon_{ij}\}$ el **tensor de permitividad eléctrica** $\boldsymbol\epsilon$ (cap. 6).

**Medios dispersivos** (p. 160–161; **Fig. 5.2-5**). La relación es dinámica: $\mathcal{E}(t)$ hace
oscilar los electrones ligados, que colectivamente producen $\mathcal{P}(t)$ con retardo → el sistema
tiene **memoria**. Solo si ese tiempo es corto frente a los demás tiempos de interés el medio es
aproximadamente no dispersivo. Para medios dispersivos lineales, homogéneos e isótropos la relación
puede ser una EDO lineal, p. ej. la de un oscilador armónico forzado
$a_1\,d^2\mathcal{P}/dt^2+a_2\,d\mathcal{P}/dt+a_3\mathcal{P}=\mathcal{E}$ (ver §5.5C). En general
(Apéndice B): un impulso de campo $\delta(t)$ induce una polarización $\epsilon_o\mathrm{x}(t)$
(respuesta impulsiva, de duración finita, que empieza en $t=0$), y por linealidad

$$\mathcal{P}(t)=\epsilon_o\int_{-\infty}^{\infty}\mathrm{x}(t-t')\,\mathcal{E}(t')\,dt'\qquad(5.2\text{-}23)$$

(convolución; causalidad: contribuyen solo $t'\le t$). El medio queda descrito por su **respuesta
impulsiva** $\epsilon_o\mathrm{x}(t)$ o por su **función de transferencia** $\epsilon_o\chi(\nu)$, con
$\chi(\nu)$ la transformada de Fourier de $\mathrm{x}(t)$: **susceptibilidad dependiente de la
frecuencia** (p. 161).

**Medios no lineales** (p. 161–162). La relación $\mathcal{P}$–$\mathcal{E}$ es no lineal y (5.2-9) ya
no aplica. Derivación general para medios homogéneos, isótropos y no magnéticos: $\nabla\times$ sobre
(5.1-8), $\mathcal{B}=\mu_o\mathcal{H}$ y (5.1-7) dan
$\nabla\times(\nabla\times\mathcal{E})=-\mu_o\partial^2\mathcal{D}/\partial t^2$; con la identidad
vectorial y $\mathcal{D}=\epsilon_o\mathcal{E}+\mathcal{P}$:

$$\nabla(\nabla\cdot\mathcal{E})-\nabla^2\mathcal{E}=-\epsilon_o\mu_o\frac{\partial^2\mathcal{E}}{\partial t^2}-\mu_o\frac{\partial^2\mathcal{P}}{\partial t^2}\qquad(5.2\text{-}24)$$

Para medios homogéneos e isótropos $\nabla\cdot\mathcal{D}=0\Rightarrow\nabla\cdot\mathcal{E}=0$, y con
$\epsilon_o\mu_o=1/c_o^2$:

$$\boxed{\nabla^2\mathcal{E}-\frac{1}{c_o^2}\frac{\partial^2\mathcal{E}}{\partial t^2}=\mu_o\frac{\partial^2\mathcal{P}}{\partial t^2}}\qquad(5.2\text{-}25)\ \text{Wave Equation (Homogeneous and Isotropic Medium)}$$

**Válida para todo medio dieléctrico homogéneo e isótropo: lineal o no lineal, dispersivo o no**
(p. 161). Si el medio es no lineal, no dispersivo y no magnético, $\mathcal{P}=\Psi(\mathcal{E})$
(función sin memoria; el ejemplo más simple es $\mathcal{P}=a_1\mathcal{E}+a_2\mathcal{E}^2$), y

$$\nabla^2\mathcal{E}-\frac{1}{c_o^2}\frac{\partial^2\mathcal{E}}{\partial t^2}=\mu_o\frac{\partial^2\Psi(\mathcal{E})}{\partial t^2}\qquad(5.2\text{-}26)$$

EDP no lineal para $\mathcal{E}(\mathbf r,t)$: **ya no aplica la superposición**. La mayoría de los
medios son aproximadamente lineales salvo a intensidades altas (haces láser enfocados); la óptica no
lineal se trata en el cap. 21 (p. 162).

### 5.3 Monochromatic Electromagnetic Waves (p. 162)

Todas las componentes son armónicas con la misma frecuencia $\nu$, $\omega=2\pi\nu$. Representación
compleja (§2.2A):

$$\mathcal{E}(\mathbf r,t)=\mathrm{Re}\{\mathbf E(\mathbf r)\exp(j\omega t)\},\qquad
\mathcal{H}(\mathbf r,t)=\mathrm{Re}\{\mathbf H(\mathbf r)\exp(j\omega t)\}\qquad(5.3\text{-}1)$$

con $\mathbf E(\mathbf r)$, $\mathbf H(\mathbf r)$ los vectores de **amplitud compleja**; análogamente
$\mathbf P,\mathbf D,\mathbf M,\mathbf B$ (p. 162).

**Maxwell en un medio** (recuadro, p. 162; con $\partial_t e^{j\omega t}=j\omega e^{j\omega t}$):

$$\nabla\times\mathbf H=j\omega\mathbf D\ (5.3\text{-}2),\quad\nabla\times\mathbf E=-j\omega\mathbf B\ (5.3\text{-}3),\quad
\nabla\cdot\mathbf D=0\ (5.3\text{-}4),\quad\nabla\cdot\mathbf B=0\ (5.3\text{-}5)$$
$$\mathbf D=\epsilon_o\mathbf E+\mathbf P\ (5.3\text{-}6),\qquad\mathbf B=\mu_o\mathbf H+\mu_o\mathbf M\ (5.3\text{-}7)$$

**Intensidad y potencia** (p. 162–163). Escribiendo $\mathcal{S}=\mathcal{E}\times\mathcal{H}$ con
amplitudes complejas:

$$\mathcal{S}=\mathrm{Re}\{\mathbf Ee^{j\omega t}\}\times\mathrm{Re}\{\mathbf He^{j\omega t}\}
=\tfrac14\big(\mathbf E\times\mathbf H^*+\mathbf E^*\times\mathbf H+e^{j2\omega t}\mathbf E\times\mathbf H+e^{-j2\omega t}\mathbf E^*\times\mathbf H^*\big)\qquad(5.3\text{-}8)$$

Los términos en $e^{\pm j2\omega t}$ se promedian a cero:

$$\langle\mathcal{S}\rangle=\tfrac14(\mathbf E\times\mathbf H^*+\mathbf E^*\times\mathbf H)=\tfrac12(\mathbf S+\mathbf S^*)=\mathrm{Re}\{\mathbf S\}\qquad(5.3\text{-}9)$$
$$\boxed{\mathbf S=\tfrac12\mathbf E\times\mathbf H^*}\qquad(5.3\text{-}10)\ \text{Complex Poynting Vector}$$

La intensidad óptica es la magnitud de $\mathrm{Re}\{\mathbf S\}$ (p. 163).

**Medios lineales, no dispersivos, homogéneos e isótropos** (p. 163). **Ecuaciones materiales**
$\mathbf D=\epsilon\mathbf E$, $\mathbf B=\mu\mathbf H$ (5.3-11); Maxwell (recuadro):

$$\nabla\times\mathbf H=j\omega\epsilon\mathbf E\ (5.3\text{-}12),\quad\nabla\times\mathbf E=-j\omega\mu\mathbf H\ (5.3\text{-}13),\quad
\nabla\cdot\mathbf E=0\ (5.3\text{-}14),\quad\nabla\cdot\mathbf H=0\ (5.3\text{-}15)$$

Sustituyendo (5.3-1) en (5.2-9) se obtiene la **ecuación de Helmholtz** (recuadro, p. 163):

$$\nabla^2U+k^2U=0,\qquad k=nk_o=\omega\sqrt{\epsilon\mu}\qquad(5.3\text{-}16)$$

$U(\mathbf r)$ es la amplitud compleja de cualquiera de $(E_x,E_y,E_z)$ o $(H_x,H_y,H_z)$;
$n=\sqrt{(\epsilon/\epsilon_o)(\mu/\mu_o)}$, $k_o=\omega/c_o$, $c=c_o/n$. (Es (2.2-7) de la óptica
ondulatoria.)

**Medios inhomogéneos** (p. 164): (5.3-12)–(5.3-15) siguen valiendo con $\epsilon=\epsilon(\mathbf r)$;
si $\epsilon(\mathbf r)$ varía lentamente respecto a $\lambda$ (medio localmente homogéneo), Helmholtz
sigue siendo aproximadamente válida con $k=n(\mathbf r)k_o$, $n(\mathbf r)=\sqrt{\epsilon(\mathbf r)/\epsilon_o}$.

**Medios dispersivos** (p. 164). Sustituyendo (5.3-1) en (5.2-23):

$$\boxed{\mathbf P=\epsilon_o\chi(\nu)\mathbf E}\qquad(5.3\text{-}17)$$
$$\chi(\nu)=\int_{-\infty}^{\infty}\mathrm{x}(t)\exp(-j2\pi\nu t)\,dt\qquad(5.3\text{-}18)$$

(transformada de Fourier de $\mathrm{x}(t)$; teorema de convolución: convolución en $t$ ↔ producto en
$\nu$). $\epsilon_o\chi(\nu)$ es la función de transferencia del sistema $\mathcal{E}(t)\to\mathcal{P}(t)$.

$$\mathbf D=\epsilon(\nu)\mathbf E\qquad(5.3\text{-}19),\qquad\epsilon(\nu)=\epsilon_o[1+\chi(\nu)]\qquad(5.3\text{-}20)$$

**En medios dispersivos $\chi$ y $\epsilon$ dependen de la frecuencia y son, en general,
complejos.** Helmholtz se adapta tomando

$$k=\omega\sqrt{\epsilon(\nu)\mu_o}\qquad(5.3\text{-}21)$$

Si $\chi(\nu)$, $\epsilon(\nu)$ son aproximadamente constantes en la banda de interés, el medio se
trata como no dispersivo (p. 164).

### 5.4 Elementary Electromagnetic Waves (p. 164)

#### 5.4A Plane, Spherical, and Gaussian Electromagnetic Waves (p. 164)

Medio lineal, homogéneo, no dispersivo e isótropo; ondas monocromáticas.

**Onda plana transversal electromagnética (TEM)** (p. 165). Amplitudes complejas de onda plana con
vector de onda $\mathbf k$:

$$\mathbf H(\mathbf r)=\mathbf H_0\exp(-j\mathbf k\cdot\mathbf r)\ (5.4\text{-}1),\qquad
\mathbf E(\mathbf r)=\mathbf E_0\exp(-j\mathbf k\cdot\mathbf r)\ (5.4\text{-}2)$$

con envolventes complejas $\mathbf H_0$, $\mathbf E_0$ constantes. Satisfacen Helmholtz si $k=nk_o$.
Sustituyendo en (5.3-12) y (5.3-13):

$$\mathbf k\times\mathbf H_0=-\omega\epsilon\mathbf E_0\ (5.4\text{-}3),\qquad\mathbf k\times\mathbf E_0=\omega\mu\mathbf H_0\ (5.4\text{-}4)$$

(las divergencias se anulan idénticamente). $\mathbf E\perp\mathbf k,\mathbf H$ y
$\mathbf H\perp\mathbf k,\mathbf E$: **$\mathbf E$, $\mathbf H$, $\mathbf k$ mutuamente ortogonales**
(**Fig. 5.4-1**, p. 165); como $\mathbf E$ y $\mathbf H$ están en un plano normal a $\mathbf k$, la onda
es **TEM**. Magnitudes: $H_0=(\omega\epsilon/k)E_0$ y $H_0=(k/\omega\mu)E_0$; consistencia ⇒
$k=\omega\sqrt{\epsilon\mu}=\omega/c=n\omega/c_o=nk_o$ (misma condición que Helmholtz). Cociente
$E_0/H_0=\omega\mu/k=c\mu=\sqrt{\mu/\epsilon}$: la **impedancia** del medio (recuadro, p. 165):

$$\eta=\frac{E_0}{H_0}=\sqrt{\frac{\mu}{\epsilon}}\qquad(5.4\text{-}5)\ \text{Impedance}$$

Para medios no magnéticos (recuadro, p. 166):

$$\eta=\frac{\eta_o}{n}\qquad(5.4\text{-}6),\qquad\eta_o=\sqrt{\frac{\mu_o}{\epsilon_o}}\approx120\pi\approx377\ \Omega\qquad(5.4\text{-}7)$$

El vector de Poynting complejo $\mathbf S=\tfrac12\mathbf E\times\mathbf H^*$ es paralelo a $\mathbf k$
(la potencia fluye normal a los frentes), de magnitud $\tfrac12E_0H_0^*=|E_0|^2/2\eta$ (recuadro, p. 166):

$$I=\frac{|E_0|^2}{2\eta}\qquad(5.4\text{-}8)\ \text{Intensity}$$

Ejemplo numérico del texto: **10 W/cm² en el vacío ↔ $E_0\approx87$ V/cm** (p. 166). Compárese con
$I=|U|^2$ de la óptica escalar. Densidad de energía promedio $W=\langle\mathcal{W}\rangle$:

$$W=\tfrac12\epsilon|E_0|^2\qquad(5.4\text{-}9)$$

(las contribuciones eléctrica y magnética son iguales: $\tfrac12\epsilon|E_0|^2/2=\tfrac12\mu|H_0|^2/2$), y

$$I=cW\qquad(5.4\text{-}10)$$

la potencia por unidad de área es la energía por unidad de volumen transportada a velocidad $c$
(cilindro de área $A$ y longitud $c$: energía $cAW$ cruza $A$ en 1 s). Densidad de momento lineal:
$(1/c^2)\mathcal{S}=(1/c^2)I\hat{\mathbf k}=(W/c)\hat{\mathbf k}$ (p. 166).

**Onda esférica** (p. 166–168). Un dipolo eléctrico oscilante radia una onda parecida a la esférica
escalar. Se construye con el **potencial vectorial**

$$\mathbf A(\mathbf r)=A_0U(\mathbf r)\hat{\mathbf x}\qquad(5.4\text{-}11),\qquad U(\mathbf r)=\frac1r\exp(-jkr)\qquad(5.4\text{-}12)$$

$\mathbf A$ satisface Helmholtz $\nabla^2\mathbf A+k^2\mathbf A=0$. Se definen

$$\mathbf H=\frac1\mu\nabla\times\mathbf A\qquad(5.4\text{-}13),\qquad\mathbf E=\frac{1}{j\omega\epsilon}\nabla\times\mathbf H\qquad(5.4\text{-}14)$$

(garantizan $\nabla\cdot\mathbf E=\nabla\cdot\mathbf H=0$; la restante $\nabla\times\mathbf E=-j\omega\mu\mathbf H$
se cumple porque $\mathbf A$ satisface Helmholtz). En coordenadas esféricas $(r,\theta,\phi)$
(**Fig. 5.4-2(a)**, p. 168; eje polar = $x$), para $r\gg\lambda$ ($kr\gg2\pi$):

$$\mathbf E(\mathbf r)\approx E_0\sin\theta\,U(\mathbf r)\hat{\boldsymbol\theta}\ (5.4\text{-}15),\qquad
\mathbf H(\mathbf r)\approx H_0\sin\theta\,U(\mathbf r)\hat{\boldsymbol\phi}\ (5.4\text{-}16)$$

con $H_0=(jk/\mu)A_0$, $E_0=\eta H_0$, $\theta=\cos^{-1}(x/r)$. Frentes esféricos; $\mathbf E$ y
$\mathbf H$ ortogonales entre sí y a $\hat{\mathbf r}$ (**Fig. 5.4-2(b)**); a diferencia de la escalar,
la magnitud varía como $\sin\theta$. Cerca del eje $z$ y lejos del origen, $\theta\approx\pi/2$,
$\phi\approx\pi/2$, $\sin\theta\approx1$ (rayos paraxiales). Con
$\hat{\boldsymbol\theta}=-\sin\theta\hat{\mathbf x}+\cos\theta\cos\phi\hat{\mathbf y}+\cos\theta\sin\phi\hat{\mathbf z}
\approx-\hat{\mathbf x}+(x/z)(y/z)\hat{\mathbf y}+(x/z)\hat{\mathbf z}\approx-\hat{\mathbf x}+(x/z)\hat{\mathbf z}$:

$$\mathbf E(\mathbf r)\approx E_0\Big(-\hat{\mathbf x}+\frac{x}{z}\hat{\mathbf z}\Big)U(\mathbf r)\qquad(5.4\text{-}17)$$

con $U(\mathbf r)$ la onda paraboloidal (aproximación paraxial de la esférica, §2.2B). Para $z$ grande
se desprecia $x/z$:

$$\mathbf E(\mathbf r)\approx-E_0U(\mathbf r)\hat{\mathbf x}\ (5.4\text{-}18),\qquad\mathbf H(\mathbf r)\approx H_0U(\mathbf r)\hat{\mathbf y}\ (5.4\text{-}19)$$

y como $U\to(1/z)e^{-jkz}$, emerge una onda plana TEM (p. 167).

**Haz gaussiano** (p. 168). Como en §3.1, el haz gaussiano escalar se obtiene de la onda paraboloidal
sustituyendo $z\to z+jz_0$, con $z_0$ real (parámetro de Rayleigh). Aplicando lo mismo a (5.4-17):

$$\mathbf E(\mathbf r)=E_0\Big(-\hat{\mathbf x}+\frac{x}{z+jz_0}\hat{\mathbf z}\Big)U(\mathbf r)\qquad(5.4\text{-}20)$$

donde $U(\mathbf r)$ es ahora la amplitud compleja escalar del haz gaussiano (3.1-7). **Fig. 5.4-3**
(p. 168): (a) frentes de onda del haz gaussiano escalar en el plano $x$–$z$ (marcas en $\pm z_0$,
$\pm2z_0$); (b) líneas de campo $\mathbf E$ del haz gaussiano electromagnético: la dirección de
$\mathbf E$ **no es espacialmente uniforme** (tiene componente $z$ fuera del eje).

#### 5.4B Relation Between Electromagnetic Optics and Scalar Wave Optics (p. 169)

Una onda paraxial electromagnética se aproxima localmente por una onda plana TEM: en cada punto
$\mathbf E$ y $\mathbf H$ están en el plano tangente al frente, normal a $\mathbf k$ (**Fig. 5.4-4**,
p. 169); la potencia fluye a lo largo de $\mathbf E\times\mathbf H\parallel\mathbf k\approx\hat{\mathbf z}$.
Una onda escalar paraxial de intensidad $I=|U|^2$ se asocia a una onda EM de igual intensidad
$I=|E|^2/2\eta$ poniendo

$$U=\frac{E}{\sqrt{2\eta}}$$

y emparejando frentes. La descripción escalar basta para interferencia, difracción, propagación e
imagen de ondas paraxiales (haz gaussiano de baja divergencia, enfoque por lentes, espejos). **Cuando
entra la polarización, la óptica ondulatoria "es muda"** y hay que usar la electromagnética (p. 169).
Observación importante: $U$ y $E$ **no cumplen las mismas condiciones de frontera**: $E$ tangencial
es continuo en la interfaz entre dos dieléctricos, pero $U=E/\sqrt{2\eta}$ es discontinuo porque
$\eta$ cambia. Por eso reflexión/refracción (reflectancia, transmitancia dependientes de
polarización, §6.2) y guías dieléctricas (caps. 8 y 9) exigen teoría electromagnética; el empate de
fase que da la ley de Snell sí se logra en teoría escalar (§2.4) (p. 169).

#### 5.4C Vector Beams (p. 169)

Maxwell en aproximación paraxial admite otros haces con simetría cilíndrica y dirección de $\mathbf E$
no uniforme. Haz con campo eléctrico **azimutal**:

$$\mathbf E(\mathbf r)=U(\rho,z)\exp(-jkz)\hat{\boldsymbol\phi}\qquad(5.4\text{-}21)$$

con $U(\rho,z)$ la solución Bessel–Gauss de Helmholtz (§3.4): se anula en el eje ($\rho=0$),
distribución tipo dona, diverge como el gaussiano (nota: D. G. Hall, *Opt. Lett.* 21, 9–11, 1996).
Otro haz tiene $\mathbf H$ azimutal y $\mathbf E$ **radial** (**Fig. 5.4-5(b)**, p. 170), también con
nulo en el eje, parecido al campo radiado por un dipolo alineado con el eje. Un haz de $\mathbf E$
radial enfocado con una lente de gran NA produce un foco **significativamente menor** que un haz
gaussiano escalar (Dorn, Quabis, Leuchs, *PRL* 91, 233901, 2003): útil en microscopía de alta
resolución (p. 170). **Fig. 5.4-5** (p. 170): (a) vectores azimutales, (b) radiales; sombreado =
intensidad transversal.

### 5.5 Absorption and Dispersion (p. 170)

Medios no magnéticos.

#### 5.5A Absorption (p. 170)

Los dieléctricos vistos hasta aquí se supusieron transparentes. El vidrio lo es en el visible pero
absorbe en UV e IR; para esas bandas se usan cuarzo y MgF₂ (UV), Ge y BaF₂ (IR). **Fig. 5.5-1**
(p. 171): ventanas espectrales de transmisión (eje 0,1–20 µm) de fluoruros (MgF₂, CaF₂, BaF₂), vidrios
(cuarzo SiO₂, UV fused silica, IR fused silica, BK-7) y semiconductores (Si, Ge, GaAs, ZnS, ZnSe,
CdTe) (ver §13.1C).

Enfoque fenomenológico en medios lineales: **susceptibilidad compleja**

$$\chi=\chi'+j\chi''\qquad(5.5\text{-}1)$$

con permitividad compleja $\epsilon=\epsilon_o(1+\chi)$ y constante dieléctrica compleja
$\epsilon/\epsilon_o=1+\chi$. Helmholtz $\nabla^2U+k^2U=0$ sigue valiendo pero $k$ es complejo
(p. 171):

$$k=\omega\sqrt{\epsilon\mu_o}=k_o\sqrt{1+\chi}=k_o\sqrt{1+\chi'+j\chi''}\qquad(5.5\text{-}2)$$

$k_o=\omega/c_o$. Escribiendo $k=\beta-j\tfrac12\alpha$:

$$\beta-j\tfrac12\alpha=k_o\sqrt{1+\chi'+j\chi''}\qquad(5.5\text{-}3)$$

Una onda plana $U=A\exp(-jkz)$ se vuelve $U=A\exp(-\tfrac12\alpha z)\exp(-j\beta z)$: para $\alpha>0$
la envolvente se atenúa como $\exp(-\tfrac12\alpha z)$ y la intensidad $\propto|U|^2$ como
$\exp(-\alpha z)$. $\alpha$ es el **coeficiente de absorción** (también **de atenuación** o **de
extinción**); esta ley exponencial justifica escribir $\mathrm{Im}\{k\}=-\tfrac12\alpha$. Medios
láser (§14.1A) tienen $\alpha<0$: $\gamma\equiv-\alpha$ es el **coeficiente de ganancia** (p. 171).
$\beta$ (tasa de cambio de fase con $z$) es la **constante de propagación**; define el índice
efectivo

$$\beta=nk_o\qquad(5.5\text{-}4)$$

y la velocidad de fase $c=c_o/n$ (p. 172). Sustituyendo en (5.5-3) (recuadro, p. 172):

$$\boxed{n-j\frac12\frac{\alpha}{k_o}=\sqrt{\epsilon/\epsilon_o}=\sqrt{1+\chi'+j\chi''}}\qquad(5.5\text{-}5)\ \text{Absorption Coefficient and Refractive Index}$$

**Elección del signo de la raíz** (p. 172): las dos raíces difieren en $\pi$. Se elige de modo que si
$\chi''<0$ (medio absorbente) entonces $\alpha>0$. Si $1+\chi'>0$, $1+\chi'+j\chi''$ está en el cuarto
cuadrante y su raíz puede estar en el segundo o cuarto; se toma el **cuarto** → $\alpha>0$ y $n>0$.
Si $1+\chi'<0$, el número está en el tercer cuadrante y de nuevo se toma la raíz del cuarto cuadrante,
así $\alpha$ y $n$ positivos. Impedancia compleja (recuadro, p. 172):

$$\eta=\sqrt{\frac{\mu_o}{\epsilon}}=\frac{\eta_o}{\sqrt{1+\chi}}\qquad(5.5\text{-}6)$$

*"En general, por tanto, $\chi$, $k$, $\epsilon$ y $\eta$ son complejos mientras que $\alpha$,
$\beta$ y $n$ son reales."* (p. 172, en cursiva en el libro).

**Medios débilmente absorbentes** (p. 172). Si $\chi''\ll1+\chi'$:
$\sqrt{1+\chi'+j\chi''}=\sqrt{1+\chi'}\sqrt{1+j\delta}\approx\sqrt{1+\chi'}(1+j\tfrac12\delta)$, con
$\delta=\chi''/(1+\chi')$; de (5.5-5) (recuadro):

$$n\approx\sqrt{1+\chi'}\qquad(5.5\text{-}7)$$
$$\alpha\approx-\frac{k_o}{n}\chi''\qquad(5.5\text{-}8)\ \text{Weakly Absorbing Medium}$$

El índice lo fija la parte real de $\chi$ y la absorción es proporcional a la parte imaginaria.
**Medio absorbente: $\chi''<0$, $\alpha>0$; medio amplificador: $\chi''>0$, $\alpha<0$** (p. 172).

**EXERCISE 5.5-1 — Dilute Absorbing Medium** (p. 172–173). Un medio no absorbente de índice $n_0$
aloja una suspensión diluida de impurezas de susceptibilidad $\chi=\chi'+j\chi''$ con $\chi'\ll1$ y
$\chi''\ll1$. Determinar la susceptibilidad total del medio y demostrar que el índice y el
coeficiente de absorción son aproximadamente

$$n\approx n_0+\frac{\chi'}{2n_0}\qquad(5.5\text{-}9)$$
$$\alpha\approx-\frac{k_o\chi''}{n_0}\qquad(5.5\text{-}10)$$

(Guía: $\chi_{tot}=(n_0^2-1)+\chi$; $n^2-jn\alpha/k_o-\alpha^2/4k_o^2=n_0^2+\chi'+j\chi''$; a primer
orden $2n_0\Delta n=\chi'$ y $-n_0\alpha/k_o=\chi''$.)

**Medios fuertemente absorbentes** (p. 173). Si $|\chi''|\gg|1+\chi'|$, (5.5-5) da
$n-j\alpha/2k_o\approx\sqrt{j\chi''}=\sqrt{-j}\sqrt{(-\chi'')}=\pm\tfrac{1}{\sqrt2}(1-j)\sqrt{(-\chi'')}$,
de donde (recuadro):

$$n\approx\sqrt{(-\chi'')/2}\qquad(5.5\text{-}11)$$
$$\alpha\approx2k_o\sqrt{(-\chi'')/2}\qquad(5.5\text{-}12)\ \text{Strongly Absorbing Medium}$$

Con $\chi''<0$ se toma el signo + para que $\alpha>0$, y entonces $n>0$.

#### 5.5B Dispersion (p. 173)

Medio dispersivo: $\chi(\nu)$, $\epsilon(\nu)$, $n(\nu)$ y velocidad $c_o/n(\nu)$ dependen de la
frecuencia (y de $\lambda$). Como el ángulo de refracción de Snell depende de $n$, prismas y lentes
desvían colores distintos en ángulos distintos (capacidad de resolución espectral; aberración
cromática). **Fig. 5.5-2** (p. 173): $n$ decreciente con $\lambda$ (B, G, R) y refracción de luz
blanca en una interfaz, un prisma y una lente. Además, cada componente de frecuencia de un pulso
sufre un retardo distinto: tras una distancia grande (fibra), el pulso se **ensancha** en el tiempo
(**Fig. 5.5-3**, p. 174: en la ilustración la componente de baja frecuencia R viaja más rápido que la
B y llega antes). **Fig. 5.5-4** (p. 174): $n(\lambda)$ de 0,1 a 10 µm para vidrios y cristales
(As₂S₃, SrTiO₃, AgCl, MgO, CsBr, cuarzo, F. Silica, BK7, calcita, CaF₂, NaF, LiF) y para
semiconductores/cristales no lineales (Ge, Si, GaAs, TiO₂, ZnSe, GaN, LiNbO₃, KTP, BBO, KDP; con
índices o/e).

**Medidas de dispersión** (p. 175).
- **Número de Abbe** $\mathbb V=(n_d-1)/(n_F-n_C)$, con $n_F$, $n_d$, $n_C$ los índices en azul
  **486,1 nm**, amarillo **587,6 nm** y rojo **656,3 nm**. Vidrio flint $\mathbb V\approx38$; sílice
  fundida $\mathbb V\approx68$.
- Cerca de una $\lambda_o$ dada: la magnitud de $dn/d\lambda_o$ (prismas: dispersión angular
  $d\theta_d/d\lambda_o=(d\theta_d/dn)(dn/d\lambda_o)$, ver (1.2-6)).
- Para pulsos: también interviene la **segunda derivada** $d^2n/d\lambda_o^2$ (§5.6 y §22.3).

**Absorción y dispersión: relaciones de Kramers–Kronig** (p. 175). Un material dispersivo **debe**
ser absorbente, con $\alpha$ también dependiente de $\lambda$. Las relaciones conectan $\chi'(\nu)$
y $\chi''(\nu)$ (recuadro):

$$\chi'(\nu)=\frac2\pi\int_0^\infty\frac{s\chi''(s)}{s^2-\nu^2}\,ds\qquad(5.5\text{-}13)$$
$$\chi''(\nu)=\frac2\pi\int_0^\infty\frac{\nu\chi'(s)}{\nu^2-s^2}\,ds\qquad(5.5\text{-}14)\ \text{Kramers–Kronig Relations}$$

Conocida una componente para todo $\nu$, se obtiene la otra; vía (5.5-5) se traducen en relaciones
entre $\alpha(\nu)$ y $n(\nu)$. Son un par de transformadas de Hilbert (Apéndice B, §B.1), válidas para
todo sistema **lineal, invariante, causal y con respuesta impulsiva real**. Como $\mathcal{E}(t)$ y
$\mathcal{P}(t)$ son reales, $\epsilon_o\mathrm{x}(t)$ es real y la función de transferencia tiene
**simetría hermítica** $\chi(-\nu)=\chi^*(\nu)$ (§A.1); se cumplen todas las condiciones; ver
(B.1-6), (B.1-7) (p. 175).

#### 5.5C The Resonant Medium (p. 176)

Teoría clásica microscópica → susceptibilidad compleja: **modelo del oscilador de Lorentz** (más en
cap. 13). Colección de átomos resonantes, una sola polarización (recuadro, p. 176):

$$\frac{d^2\mathcal{P}}{dt^2}+\sigma\frac{d\mathcal{P}}{dt}+\omega_0^2\mathcal{P}=\omega_0^2\epsilon_o\chi_0\mathcal{E}\qquad(5.5\text{-}15)\ \text{Resonant Dielectric Medium}$$

con $\sigma$, $\omega_0$, $\chi_0$ constantes. Surge de modelar la carga ligada como oscilador
armónico clásico, desplazamiento $x(t)$ y fuerza $\mathcal{F}(t)$:

$$\frac{d^2x}{dt^2}+\sigma\frac{dx}{dt}+\omega_0^2x=\frac{\mathcal{F}}{m}\qquad(5.5\text{-}16)$$

$m$ masa de la carga, $\omega_0=\sqrt{\kappa/m}$ frecuencia angular de resonancia, $\kappa$ constante
elástica, $\sigma$ coeficiente de amortiguamiento. Con momento dipolar por átomo $\mathrm p=-ex$,
$\mathcal{P}=N\mathrm p=-Nex$ ($N$ átomos por unidad de volumen, $-e$ carga del electrón) y
$\mathcal{E}=\mathcal{F}/(-e)$, comparando (5.5-15) y (5.5-16):

$$\chi_0=\frac{Ne^2}{\epsilon_om\omega_0^2}\qquad(5.5\text{-}17)$$

**Fig. 5.5-5** (p. 176): $\mathcal{E}(t)$ senoidal induce dipolos oscilantes en átomos de Lorentz. El
medio queda caracterizado por su respuesta impulsiva $\epsilon_o\mathrm{x}(t)$ (armónica
exponencialmente amortiguada) o por su función de transferencia $\epsilon_o\chi(\nu)$ (p. 176).
Sustituyendo $\mathcal{E}=\mathrm{Re}\{Ee^{j\omega t}\}$, $\mathcal{P}=\mathrm{Re}\{Pe^{j\omega t}\}$:

$$(-\omega^2+j\sigma\omega+\omega_0^2)P=\omega_0^2\epsilon_o\chi_0E\qquad(5.5\text{-}18)$$

$P=\epsilon_o[\chi_0\omega_0^2/(\omega_0^2-\omega^2+j\sigma\omega)]E\equiv\epsilon_o\chi(\nu)E$, con
$\omega=2\pi\nu$ (recuadro, p. 177):

$$\boxed{\chi(\nu)=\chi_0\frac{\nu_0^2}{\nu_0^2-\nu^2+j\nu\,\Delta\nu}}\qquad(5.5\text{-}19)\ \text{Susceptibility (Resonant Medium)}$$

$\nu_0=\omega_0/2\pi$ frecuencia de resonancia, $\Delta\nu=\sigma/2\pi$. Partes real e imaginaria:

$$\chi'(\nu)=\chi_0\frac{\nu_0^2(\nu_0^2-\nu^2)}{(\nu_0^2-\nu^2)^2+(\nu\Delta\nu)^2}\qquad(5.5\text{-}20)$$
$$\chi''(\nu)=-\chi_0\frac{\nu_0^2\,\nu\Delta\nu}{(\nu_0^2-\nu^2)^2+(\nu\Delta\nu)^2}\qquad(5.5\text{-}21)$$

**Fig. 5.5-6** (p. 177): $\chi'(\nu)$ positiva bajo resonancia, cero en $\nu_0$, negativa arriba;
$\chi''(\nu)$ negativa, $-\chi''$ positiva con pico $\chi_0Q$ en $\nu_0$, $Q=\nu_0/\Delta\nu$
(dibujada con $Q=10$).

Comportamiento (p. 177–178):
- $\nu\ll\nu_0$: $\chi'\approx\chi_0$, $\chi''\approx0$ → susceptibilidad de baja frecuencia $\chi_0$.
- $\nu\gg\nu_0$: $\chi'\approx\chi''\approx0$ → se comporta como el vacío.
- $\nu=\nu_0$: $\chi'(\nu_0)=0$ y $-\chi''(\nu_0)=\chi_0Q$. Como $\nu_0\gg\Delta\nu$, $Q\gg1$ y el pico
  de $-\chi''$ es mucho mayor que $\chi_0$.
- Máximo y mínimo de $\chi'$: $\pm\chi_0Q/(2\mp1/Q)$ en $\nu_0\sqrt{1\mp1/Q}$; para $Q$ grande $\chi'$
  oscila entre $\pm\chi_0Q/2$, la mitad del pico de $\chi''$.
- Los signos de $\chi'$ y $\chi''$ fijan la fase de $\chi$ = ángulo entre los fasores $P$ y $E$.

**Cerca de resonancia** ($\nu\sim\nu_0$; $\nu_0^2-\nu^2\approx2\nu_0(\nu_0-\nu)$, $\nu\to\nu_0$ en la
parte imaginaria) (p. 178):

$$\chi(\nu\sim\nu_0)\approx\chi_0\frac{\nu_0/2}{(\nu_0-\nu)+j\Delta\nu/2}\qquad(5.5\text{-}22)$$
$$\chi''(\nu)\approx-\chi_0\frac{\nu_0\Delta\nu}{4}\frac{1}{(\nu_0-\nu)^2+(\Delta\nu/2)^2}\qquad(5.5\text{-}23)$$
$$\chi'(\nu)\approx2\frac{\nu-\nu_0}{\Delta\nu}\chi''(\nu)\qquad(5.5\text{-}24)\ \text{Susceptibility (Near Resonance)}$$

(5.5-23) es la **función lorentziana**: cae a la mitad cuando $|\nu-\nu_0|=\Delta\nu/2$; $\Delta\nu$ es
la **anchura total a media altura (FWHM)** de $\chi''$. **Lejos de resonancia** ($|\nu-\nu_0|\gg\Delta\nu$)
la susceptibilidad es aproximadamente real (recuadro, p. 178):

$$\chi(\nu)\approx\chi_0\frac{\nu_0^2}{\nu_0^2-\nu^2}\qquad(5.5\text{-}25)\ \text{Susceptibility (Far from Resonance)}$$

absorción despreciable. Para $\alpha$ y $n$ en general se sustituye (5.5-23)–(5.5-24) en (5.5-5); si
los átomos resonantes están diluidos en un huésped no dispersivo de índice $n_0$ con $\chi',\chi''\ll1$
(Ejercicio 5.5-1):

$$\alpha(\nu)\approx-\Big(\frac{2\pi\nu}{n_0c_o}\Big)\chi''(\nu)\qquad(5.5\text{-}26)$$
$$n(\nu)\approx n_0+\frac{\chi'(\nu)}{2n_0}\qquad(5.5\text{-}27)$$

**Fig. 5.5-7** (p. 179): $\alpha(\nu)$ lorentziana de anchura $\Delta\nu$ centrada en $\nu_0$;
$n(\nu)$ con forma dispersiva alrededor de $n_0$, excursión $\chi_0/2n_0$ a baja frecuencia.

**Medios con múltiples resonancias** (p. 178–179). Un dieléctrico típico tiene varias resonancias
(vibraciones de red y electrónicas); la susceptibilidad total es la superposición. La parte
imaginaria se confina cerca de cada resonancia; la parte real contribuye en todas las frecuencias
cercanas y **por debajo** de la resonancia (**Fig. 5.5-8**, p. 179: $\alpha(\nu)$ y $n(\nu)$ con tres
resonancias $\nu_1,\nu_2,\nu_3$). Lejos de las resonancias el medio es aproximadamente no dispersivo
y no absorbente, pero cada resonancia aporta un valor constante a $n$ por debajo de su frecuencia.
**Fig. 5.5-9** (p. 180): dependencia con $\lambda_o$ (0,01–100 µm) de $\alpha$ y $n$ para un
dieléctrico transparente en el visible, con absorción resonante en UV e IR: en el visible $n$
decrece con $\lambda$ por la resonancia UV cercana; mayor dispersión a $\lambda$ cortas (coherente con
Figs. 5.5-1 y 5.5-4).

**Ecuación de Sellmeier** (p. 179–180). Con resonancias $i=1,2,\dots$, lejos de todas ellas
$\chi\approx\sum_i$ términos tipo (5.5-25), y con $n^2=1+\chi$ (5.2-13) (recuadro, p. 180):

$$\boxed{n^2\approx1+\sum_i\chi_{0i}\frac{\nu_i^2}{\nu_i^2-\nu^2}=1+\sum_i\chi_{0i}\frac{\lambda^2}{\lambda^2-\lambda_i^2}}\qquad(5.5\text{-}28)\ \text{Sellmeier Equation}$$

La **Tabla 5.5-1** (p. 180, transcrita abajo) da ecuaciones de Sellmeier ajustadas por mínimos
cuadrados a datos medidos; describen bien el índice de la mayoría de los materiales transparentes.
Para $\lambda\ll\lambda_i$ el término $i$ es $\propto\lambda^2$; para $\lambda\gg\lambda_i$ es
aproximadamente constante. La sílice fundida (Ejemplo 5.6-1) se describe bien con tres resonancias.
Algunos materiales se aproximan con una serie de potencias (p. 181).

#### 5.5D Optics of Conductive Media (p. 181)

Metales, semiconductores, dieléctricos dopados y gases ionizados tienen cargas libres y densidad de
corriente $\mathcal{J}$; (5.1-7) se modifica:

$$\nabla\times\mathcal{H}=\frac{\partial\mathcal{D}}{\partial t}+\mathcal{J}\qquad(5.5\text{-}29)$$

(las otras tres no cambian). Monocromática: $\nabla\times\mathbf H=j\omega\mathbf D+\mathbf J$
(5.5-30). Con $\mathbf D=\epsilon\mathbf E=\epsilon_o(1+\chi)\mathbf E$ y **conductividad** $\sigma$
(ley de Ohm, ver (18.1-13), (18.1-14)):

$$\mathbf J=\sigma\mathbf E\qquad(5.5\text{-}31)$$

el lado derecho de (5.5-30) es $(j\omega\epsilon+\sigma)\mathbf E=j\omega(\epsilon+\sigma/j\omega)\mathbf E$:

$$\nabla\times\mathbf H=j\omega\epsilon_e\mathbf E\qquad(5.5\text{-}32),\qquad
\boxed{\epsilon_e=\epsilon+\frac{\sigma}{j\omega}}\qquad(5.5\text{-}33)\ \text{Effective Permittivity}$$

$\epsilon_e$ compleja y dependiente de la frecuencia; la contribución conductiva decae con $\omega$.
Como (5.5-32) tiene la forma dieléctrica, valen §5.3–5.5 con $k=\beta-j\tfrac12\alpha=\omega\sqrt{\epsilon_e\mu_o}$,
$\eta=\sqrt{\mu_o/\epsilon_e}$, y $n-j\alpha/2k_o=\sqrt{\epsilon_e/\epsilon_o}$. Si $\sigma/\omega\gg\epsilon$
(dominan los efectos conductivos), $\epsilon_e\approx\sigma/j\omega$, $n-j\alpha/2k_o\approx\sqrt{\sigma/j\omega\epsilon_o}$,
$\eta\approx\sqrt{j\omega\mu_o/\sigma}$ (recuadro, p. 182):

$$n\approx\sqrt{\sigma/2\omega\epsilon_o}\qquad(5.5\text{-}34)$$
$$\alpha\approx\sqrt{2\omega\mu_o\sigma}\qquad(5.5\text{-}35)$$
$$\eta\approx(1+j)\sqrt{\omega\mu_o/2\sigma}\qquad(5.5\text{-}36)\ \text{Conductive Medium}$$

(usando $k_o=\omega/c_o=\omega\sqrt{\epsilon_o\mu_o}$). La intensidad cae a $e^{-1}$ a la
**profundidad de penetración** o **skin depth** $d_p=1/\alpha=1/\sqrt{2\omega\mu_o\sigma}$ (nota al
pie: a veces se define con el campo en vez de la intensidad). $d_p$ y $n$ varían como $1/\sqrt\omega$.
En metales $\sigma$ y $\alpha$ son muy grandes (fuerte atenuación superficial) pero $\eta$ es muy
pequeña → **altamente reflectantes** (Ejercicio 6.2-2) (p. 182).

**EXAMPLE 5.5-1 — Penetration Depth and Refractive Index of Copper** (p. 182). Cobre:
$\sigma=0{,}58\times10^8\ (\Omega\cdot\text{m})^{-1}$; a $\lambda_o=1$ µm la profundidad de penetración
es **$d_p=1{,}9$ nm**. Por (5.5-34)–(5.5-35), $n=\sigma\eta_od_p$, que da **$n=41{,}6$**.

**Modelo de Drude** (p. 182–184). Como la relación $\mathcal{J}$–$\mathcal{E}$ es dinámica, $\sigma$
depende de la frecuencia. Electrones de conducción como gas ideal entre colisiones:

$$\sigma=\frac{\sigma_0}{1+j\omega\tau}\qquad(5.5\text{-}37)$$

$\sigma_0$ conductividad de baja frecuencia, $\tau$ tiempo de relajación. De (5.5-33):

$$\epsilon_e=\epsilon+\frac{\sigma_0}{j\omega(1+j\omega\tau)}\qquad(5.5\text{-}38)$$

Para $\omega\gg1/\tau$: $\epsilon_e\approx\epsilon-\sigma_0/\omega^2\tau$: la conductividad **reduce la
parte real de la permitividad** (contribución negativa $\propto1/\omega^2$). Si $\epsilon=\epsilon_o$:

$$\epsilon_e=\epsilon_o\Big(1-\frac{\omega_p^2}{\omega^2}\Big)\qquad(5.5\text{-}39)$$

con $\omega_p=\sqrt{\sigma_0/\epsilon_o\tau}$ la **frecuencia de plasma**. Teoría microscópica: como
Lorentz pero con electrones libres ($\kappa=0$, $\sigma=0$): $m\,d^2x/dt^2=-e\mathcal{E}$,
$d^2\mathcal{P}/dt^2=(Ne^2/m)\mathcal{E}$, a frecuencia $\omega$: $-\omega^2P=(Ne^2/m)E$, es decir una
reducción de la constante dieléctrica $P/\epsilon_oE=-(Ne^2/\epsilon_om)/\omega^2$, consistente con
(5.5-39) y

$$\omega_p=\sqrt{\frac{Ne^2}{\epsilon_om}}\qquad(5.5\text{-}40)$$

Combinando con Drude: $\sigma_0=Ne^2\tau/m$ (coincide con (18.1-13)) (p. 183). **Fig. 5.5-10**
(p. 183): dependencia en $\omega$ de $\epsilon_e/\epsilon_o$, $\beta$ (con las rectas
$\omega=c_o\beta$ y la curva $\omega=\sqrt{\omega_p^2+c_o^2\beta^2}$), $n$ y $\alpha$; banda
prohibida bajo $\omega_p$, banda plasmónica sobre $\omega_p$. Tres regímenes (p. 183–184):
- $\omega<\omega_p$: $\epsilon_e<0$, $k=\omega\sqrt{\epsilon_e\mu_o}$ imaginario → atenuación sin
  propagación (**banda prohibida**); $\alpha=2k_o(\omega_p^2/\omega^2-1)^{1/2}$ decrece con $\omega$ y
  se anula en $\omega_p$; impedancia imaginaria → en la frontera con un medio ordinario la luz se
  refleja totalmente (**espejo perfecto**, §6.2).
- $\omega>\omega_p$: $\epsilon_e>0$ real → dieléctrico sin pérdidas con dispersión peculiar:
  $\beta=(\omega^2-\omega_p^2)^{1/2}/c_o$, $n=(1-\omega_p^2/\omega^2)^{1/2}<1$ (muy pequeño cerca de
  $\omega_p$): **banda plasmónica**.
- $\omega=\omega_p$: $\beta=0$, la onda no viaja; los electrones libres oscilan longitudinalmente; el
  cuasi-partícula asociado es el **plasmón**.
En la mayoría de los metales $\omega_p$ está en el UV (reflectantes y brillantes en el visible);
en el cobre está en el visible (color propio); en semiconductores dopados, en el IR (p. 184).

### 5.6 Pulse Propagation in Dispersive Media (p. 184)

Un pulso es suma de ondas monocromáticas, cada una con su velocidad y atenuación: el pulso se retarda,
se ensancha y en general cambia de forma. Análisis simplificado aquí; detalle en el cap. 22 (p. 184).

**Velocidad de grupo** (p. 184–185). Onda plana pulsada en $z$ en un medio sin pérdidas de índice
$n(\omega)$; en $z=0$: $U(0,t)=\mathcal{A}(t)\exp(j\omega_0t)$ ($\omega_0$ frecuencia central,
$\mathcal{A}(t)$ envolvente compleja). Si la dispersión es débil ($n$ varía lentamente en el ancho de
banda), a distancia $z$: $U(z,t)=\mathcal{A}(t-z/v)\exp[j\omega_0(t-z/c)]$, con $c=c_o/n(\omega_0)$ y
$v$ la **velocidad de grupo** (recuadro, p. 184):

$$\frac1v=\beta'=\frac{d\beta}{d\omega}\qquad(5.6\text{-}1)\ \text{Group Velocity}$$

$\beta=\omega n(\omega)/c_o$ constante de propagación; $\beta'$ evaluada en $\omega_0$. $v$ depende en
general de la frecuencia central. **Retardo de grupo** $\tau_d=z/v$. El factor $\exp[j\omega_0(t-z/c)]$
viaja a la **velocidad de fase** $c$, $1/c=\beta(\omega_0)/\omega_0$. Medio no dispersivo:
$\beta=\omega/c$, $v=c$ (p. 184). **Fig. 5.6-1** (p. 185): la envolvente viaja a $v$, la portadora a $c$.

*Derivación* (p. 184–185): descomponiendo $\mathcal{A}(t)$ en armónicos $A(\Omega)$, cada componente
$\omega=\omega_0+\Omega$ viaja como $A(\Omega)\exp\{-j[\beta(\omega_0+\Omega)]z\}\exp[j(\omega_0+\Omega)t]$;
con Taylor $\beta(\omega_0+\Omega)\approx\beta(\omega_0)+\Omega\,d\beta/d\omega=\omega_0/c+\Omega/v$,
la componente es $A(\Omega)\exp[j\Omega(t-z/v)]\exp[j\omega_0(t-z/c)]$; la envolvente se vuelve
$\mathcal{A}(t-z/v)$. ∎

En función de $\lambda$ (con $\beta=\omega n(\lambda_o)/c_o=2\pi n(\lambda_o)/\lambda_o$,
$\lambda_o=2\pi c_o/\omega$ y regla de la cadena) (recuadros, p. 185):

$$v=\frac{c_o}{N},\qquad N=n-\lambda_o\frac{dn}{d\lambda_o}\qquad(5.6\text{-}2)\ \text{Group Velocity and Group Index}$$

$N$ es el **índice de grupo** (p. 185).

**Dispersión de velocidad de grupo (GVD)** (p. 185–186). Como $v=1/(d\beta/d\omega)$ depende de la
frecuencia, distintas componentes sufren distintos retardos $\tau_d=z/v$ → el pulso se ensancha. Dos
pulsos idénticos de frecuencias $\nu$ y $\nu+\delta\nu$ tienen un retardo de grupo diferencial

$$\delta\tau=\frac{d\tau_d}{d\nu}\delta\nu=\frac{d}{d\nu}\Big(\frac zv\Big)\delta\nu=D_\nu\,z\,\delta\nu\qquad(5.6\text{-}3)$$
$$\boxed{D_\nu=\frac{d}{d\nu}\Big(\frac1v\Big)=2\pi\beta''}\qquad(5.6\text{-}4)\ \text{Dispersion Coefficient}$$

$\beta''\equiv d^2\beta/d\omega^2|_{\omega_0}$: términos de orden superior del Taylor despreciados antes
(cap. 22). Para un pulso de ancho espectral inicial $\sigma_\nu$ (Hz) (recuadro, p. 186):

$$\sigma_\tau=|D_\nu|\sigma_\nu z\qquad(5.6\text{-}5)\ \text{Pulse Spread}$$

$D_\nu$: ensanchamiento temporal por unidad de distancia y de ancho espectral (**s/m-Hz**).
**Fig. 5.6-2** (p. 186): el pulso se ensancha a una tasa $\propto D_\nu\sigma_\nu z$. Con $n(\lambda_o)$,
de (5.6-2) y (5.6-4):

$$D_\nu=\frac{\lambda_o^3}{c_o^2}\frac{d^2n}{d\lambda_o^2}\qquad(5.6\text{-}6)\ \text{Dispersion Coefficient (s/m-Hz)}$$

Coeficiente en longitud de onda: $D_\lambda d\lambda=D_\nu d\nu$ ⇒ $D_\lambda=D_\nu\,d\nu/d\lambda_o=D_\nu(-c_o/\lambda_o^2)$:

$$D_\lambda=-\frac{\lambda_o}{c_o}\frac{d^2n}{d\lambda_o^2}\qquad(5.6\text{-}7)\ \text{Dispersion Coefficient (s/m-nm)}$$
$$\sigma_\tau=|D_\lambda|\sigma_\lambda z\qquad(5.6\text{-}8)\ \text{Pulse Spread}$$

En fibras (§9.3, §24.1, §22.3) $D_\lambda$ se da en **ps/km-nm**. Nota al pie: en la literatura también
se usa $M=-D_\lambda$ (p. 186).

**Dispersión normal y anómala** (p. 187). El signo de $D_\nu$ (o $D_\lambda$) no afecta la tasa de
ensanchamiento, pero sí la fase de la envolvente, y es crucial en cascadas de materiales (cap. 22).
- $D_\nu>0$ ($D_\lambda<0$): **dispersión normal**; las altas frecuencias (λ cortas) viajan más
  despacio y llegan después.
- $D_\nu<0$ ($D_\lambda>0$): **dispersión anómala**; las λ cortas viajan más rápido y llegan antes.
La mayoría de los vidrios tienen dispersión normal en el visible; a λ mayores suele ser anómala.
**Fig. 5.6-3** (p. 187): normal ($\beta''>0$, $D_\nu>0$, $D_\lambda<0$): llega R y luego B; anómala
($\beta''<0$, $D_\nu<0$, $D_\lambda>0$): llega B y luego R. *"Los pulsos se dice que tienen chirp porque
la frecuencia instantánea varía en el tiempo."* (Este es el único tratamiento del chirp en el
capítulo; el análisis cuantitativo del pulso gaussiano con chirp se difiere al cap. 22, §22.3.)

**Medio de una sola resonancia** (p. 187–188). Sustituyendo (5.5-20), (5.5-21) en (5.5-5) y usando
(5.6-2), (5.6-7), la **Fig. 5.6-4** (p. 188) muestra $n$, $N$ y $D_\lambda$ vs. $\lambda/\lambda_0$
(0,5–1,5) para $\chi_0=0{,}05$, $\Delta\nu/\nu_0=0{,}1$. Cerca de la resonancia (zona sombreada)
$n$ varía tan rápido que $N$ y $D_\lambda$ (definidos con pocos términos de Taylor) pierden sentido.
Lejos, a ambos lados, $n$ decrece monótonamente con $\lambda$ y tiene puntos de inflexión (puntos):
allí $dn/d\lambda$ tiene máximos locales → $N$ es máximo; la segunda derivada se anula → $D_\lambda$
cambia de signo. Al acercarse a la resonancia desde abajo la dispersión pasa de anómala a normal; desde
arriba, lo contrario.

**Luz rápida y lenta en medios resonantes** (p. 188–189). Cerca de la resonancia $n$ y $N$ cambian
rápido y pueden ser mucho mayores o menores que 1; $N$ y $v=c_o/N$ pueden incluso ser **negativos**.
No hay conflicto con la relatividad: ni la velocidad de grupo ni la de fase son la **velocidad de la
información** (velocidad de un punto no analítico del pulso, p. ej. el frente de un pulso
rectangular), que nunca excede $c_o$. En un medio débilmente dispersivo ($\beta$ lineal cerca de
$\omega_0$) la envolvente conserva su forma y $v$ aproxima bien la velocidad de información (lejos de
resonancia, $N>1$, $v<c_o$). Más cerca, con GVD de segundo orden, un **pulso gaussiano sigue siendo
gaussiano, con mayor anchura**, y su pico viaja a $v$; pero por tener soporte infinito, la velocidad
del pico no es la de información y puede superar $c_o$. En la vecindad inmediata de la resonancia
intervienen órdenes superiores, la forma cambia y $v$ deja de ser candidata; en distancias cortas el
pulso puede viajar casi sin deformarse a velocidad de grupo mucho mayor que $c_o$ o **negativa** (el
pico sale antes de que el correspondiente del pulso de entrada haya entrado). En el límite de luz
lenta, resonancias especiales permiten reducir $v$ enormemente o incluso detener la luz. Como estos
fenómenos solo se observan cerca de resonancia (absorción grande), se necesita amplificación óptica
y a menudo se explotan efectos no lineales (p. 189).

**EXAMPLE 5.6-1 — Dispersion in a Multi-Resonance Medium: Fused Silica** (p. 189). Entre 0,21 y
3,71 µm la sílice fundida a temperatura ambiente se describe con la Sellmeier (5.5-28) de tres
resonancias: $\lambda_1=0{,}06840$ µm, $\lambda_2=0{,}1162$ µm, $\lambda_3=9{,}8962$ µm, con pesos
$\chi_{01}=0{,}6962$, $\chi_{02}=0{,}4079$, $\chi_{03}=0{,}8975$. De ahí, con (5.6-2) y (5.6-7), $N$ y
$D_\lambda$. **Fig. 5.6-5** (p. 189), 600–1600 nm: $n$ decrece monótonamente de ~1,458 a ~1,443
(punto de inflexión); $N$ baja de ~1,48 hasta un mínimo ≈1,462 y vuelve a subir; $D_\lambda$ va de
≈ −200 ps/km-nm en 0,6 µm, cruza cero y llega a ≈ +20 ps/km-nm en 1,6 µm. Resultado: punto de
inflexión de $n$ en **$\lambda_o=1{,}276$ µm**, donde $N$ es mínimo ($v$ máxima) y
**$D_\lambda=0$** (longitud de onda de dispersión cero → ensanchamiento mínimo). Para
$\lambda<1{,}276$ µm, $D_\lambda<0$ (normal); para $\lambda>1{,}276$ µm, $D_\lambda>0$ (anómala). Las
fibras de sílice dopada usadas en comunicaciones tienen dispersión cero cerca de **1,312 µm**
(§9.3, §24.1, §22.3).

### *5.7 Optics of Magnetic Materials and Metamaterials (p. 190)

Medios con absorción y dispersión eléctrica **y** magnética: $\epsilon$ y $\mu$ complejos y
dependientes de la frecuencia. Onda plana $\mathbf E=\mathbf E_0e^{-j\mathbf k\cdot\mathbf r}$,
$\mathbf H=\mathbf H_0e^{-j\mathbf k\cdot\mathbf r}$:

$$\mathbf k\times\mathbf H_0=-\omega\epsilon\mathbf E_0\ (5.7\text{-}1),\qquad\mathbf k\times\mathbf E_0=\omega\mu\mathbf H_0\ (5.7\text{-}2)$$
$$k=\omega\sqrt{\epsilon\mu}\ (5.7\text{-}3),\qquad\eta=\frac{E_0}{H_0}=\frac{\omega\mu}{k}\ (5.7\text{-}4)$$

Si $\epsilon,\mu$ reales, $k=nk_o$ con

$$n=\sqrt{\frac{\epsilon}{\epsilon_o}\frac{\mu}{\mu_o}}=c_o\sqrt{\epsilon\mu}\qquad(5.7\text{-}5)$$

Si son complejos, $k=nk_o-j\tfrac12\alpha$ (recuadro, p. 190):

$$nk_o-j\tfrac12\alpha=\omega\sqrt{\epsilon\mu}\qquad(5.7\text{-}6)$$

Las partes imaginarias de $\epsilon$ y $\mu$ contribuyen a $\alpha$. **Metamateriales**: compuestos
estructurados artificialmente (cap. 7) con $\epsilon(\nu)$ y $\mu(\nu)$ a medida (matrices de hilos
conductores o anillos metálicos resonantes). Ejemplo: matriz doblemente periódica de pares de
nanovarillas de oro con **$n\approx-0{,}3$ en $\lambda=1{,}5$ µm** (Shalaev et al., *Opt. Lett.* 30,
3356, 2005) por resonancias plasmónicas eléctricas y magnéticas (p. 190–191).

**Metamateriales doblemente negativos** (p. 191–192). En medios absorbentes las partes imaginarias
son siempre positivas (causalidad). Si $\epsilon$ y $\mu$ son reales y **ambos negativos**
($\epsilon=-|\epsilon|$, $\mu=-|\mu|$):

$$\mathbf k\times\mathbf H_0=\omega|\epsilon|\mathbf E_0\ (5.7\text{-}7),\qquad\mathbf k\times\mathbf E_0=-\omega|\mu|\mathbf H_0\ (5.7\text{-}8)$$

equivale a intercambiar los papeles de $\mathbf E$ y $\mathbf H$: $\mathbf E_0,\mathbf H_0,\mathbf k$
forman una terna **levógira** (left-handed), y $\mathbf S=\tfrac12\mathbf E_0\times\mathbf H_0^*$ es
**antiparalelo a $\mathbf k$**: los frentes viajan en sentido opuesto al flujo de energía
(**Fig. 5.7-1**, p. 191). Ejemplo: $\mathbf E=E_0e^{-jkz}\hat{\mathbf x}$ (5.7-9),
$\mathbf H=H_0e^{-jkz}\hat{\mathbf y}$ (5.7-10); $\mathbf S=\tfrac12E_0H_0^*\hat{\mathbf z}=(|E_0|^2/2\eta)\hat{\mathbf z}$
con $\eta=\sqrt{|\mu|/|\epsilon|}>0$ ⇒ $\mathbf k$ en $-z$ ⇒ $k<0$: se elige la raíz negativa en
(5.7-6), **índice de refracción negativo**:

$$n=-c_o\sqrt{|\epsilon||\mu|}\qquad(5.7\text{-}11)$$

Que ambos sean reales y negativos es remoto (en un modelo resonante, donde la parte real es negativa
la imaginaria no es nula). Pero esa condición es *suficiente, no necesaria*: con $\epsilon,\mu$
complejos y partes reales negativas el medio sigue siendo levógiro (p. ej. sobre ambas resonancias
de modelos resonantes; la onda se atenúa en la dirección de $\mathbf S$). Condición **necesaria y
suficiente** de levogiria (McCall, Lakhtakia, Weiglhofer, *Eur. J. Phys.* 23, 353, 2002):

$$(|\epsilon|-\mathrm{Re}\{\epsilon\})(|\mu|-\mathrm{Re}\{\mu\})>\mathrm{Im}\{\epsilon\}\,\mathrm{Im}\{\mu\}\qquad(5.7\text{-}12)$$

Si solo uno es negativo (ambos reales) no se cumple: ondas atenuadas. Si uno es real y positivo, no
puede ser levógiro cualquiera que sea el otro: **los materiales no magnéticos no pueden ser
levógiros** (p. 192).

**Óptica de materiales de índice negativo** (p. 192–193). Ley de Snell con $n_2<0$:

$$n_1\sin\theta_1=-|n_2|\sin\theta_2\qquad(5.7\text{-}13)$$

$\theta_2<0$: rayo refractado del mismo lado de la normal que el incidente (**Fig. 5.7-2**, p. 193;
$\mathbf S_2$ y $\mathbf k_2$ opuestos). Una lente convexa de índice negativo actúa como cóncava y
viceversa; una **lámina plana** actúa como lente (**Fig. 5.7-3**, p. 193: lámina $n_2=-1$ en el vacío,
imágenes dentro y fuera); transmitancia unidad para ondas planas a cualquier inclinación y
polarización, incluidas las evanescentes: "lente perfecta" más allá del límite de difracción (Pendry,
*PRL* 85, 3966, 2000).

### Reading List (p. 193–195)

Grupos: *General* (Hayt & Buck; Sadiku; Kong; Lucarini et al., *Kramers–Kronig Relations in Optical
Materials Research*, 2005; Narayana Rao; Ida; Lorrain, Corson & Lorrain; Jackson; Landau & Lifshitz
*Classical Theory of Fields* y *Electrodynamics of Continuous Media*; Ramo, Whinnery & Van Duzer;
Staelin et al.; Sarwate; Hopf & Stegeman; Kriezis et al.; Cheng; Haus & Melcher; Haus *Waves and
Fields in Optoelectronics*, 1984); *Optical Constants* (Bass et al. *Handbook of Optics*; Wolfe &
Zissis *Infrared Handbook*; Palik *Handbook of Optical Constants of Solids II*; Kingery et al.);
*Plasmons* (Brongersma & Kik; Tominaga & Tsai; Jutamulia; Kawata, Ohtsu & Irie; Pines; Liebsch;
Raether); *Fast and Slow Light* (Milonni, *Fast Light, Slow Light and Left-Handed Light*, 2005;
Stenner, Gauthier & Neifeld *PRL* 94, 053902, 2005; Brunner et al. *PRL* 93, 203902, 2004; Boyd &
Gauthier, "Slow" and "Fast" Light, *Prog. Opt.* 43, 497–530, 2002; Chiao & Steinberg, *Prog. Opt.*
37, 1997; Oughstun & Sherman; Brillouin, *Wave Propagation and Group Velocity*, 1960); *Doubly
Negative Materials* (Eleftheriades & Balmain; Pendry & Smith *Physics Today* 57(6), 37, 2004; McCall
et al. 2002; Pendry *PRL* 85, 3966, 2000; Veselago, *Sov. Phys. Uspekhi* 10, 509–514, 1968).

---

## Tablas y datos numéricos útiles

**Constantes** (p. 153, 166):
| Magnitud | Valor |
|---|---|
| $\epsilon_o$ | $\approx(1/36\pi)\times10^{-9}$ F/m $=8{,}854\times10^{-12}$ F/m |
| $\mu_o$ | $4\pi\times10^{-7}$ H/m |
| $c_o=1/\sqrt{\epsilon_o\mu_o}$ | $\approx3\times10^8$ m/s |
| $\eta_o=\sqrt{\mu_o/\epsilon_o}$ | $\approx120\pi\approx377\ \Omega$ |
| Dominio óptico | 10 nm – 300 µm (p. 152) |
| $I=10$ W/cm² en el vacío | $E_0\approx87$ V/cm (p. 166) |

**Dispersión** (p. 175, 182, 189):
| Dato | Valor |
|---|---|
| Líneas de Abbe F, d, C | 486,1 nm; 587,6 nm; 656,3 nm |
| Número de Abbe vidrio flint | $\mathbb V\approx38$ |
| Número de Abbe sílice fundida | $\mathbb V\approx68$ |
| Cobre: $\sigma$ | $0{,}58\times10^8\ (\Omega\cdot m)^{-1}$ |
| Cobre a 1 µm: $d_p$, $n$ | 1,9 nm; 41,6 |
| Sílice fundida: $\lambda$ de dispersión cero | 1,276 µm |
| Fibras de sílice dopada: dispersión cero | ≈1,312 µm |
| Sílice a 0,6 µm / 1,6 µm: $D_\lambda$ (Fig. 5.6-5) | ≈ −200 / ≈ +20 ps/km-nm |
| Metamaterial de nanovarillas de Au (1,5 µm) | $n\approx-0{,}3$ |
| Fig. 5.6-4 (una resonancia) | $\chi_0=0{,}05$, $\Delta\nu/\nu_0=0{,}1$ |
| Fig. 5.5-6 | $Q=\nu_0/\Delta\nu=10$ |

**Tabla 5.5-1 — Ecuaciones de Sellmeier** (p. 180; $\lambda$ en µm, temperatura ambiente; $n_o$, $n_e$
índices ordinario y extraordinario de materiales anisótropos, §6.3; última columna = rango de
validez). Transcrita de la página escaneada (resolución baja pero legible; los coeficientes de la
sílice coinciden con el Ejemplo 5.6-1):

| Material | Ecuación de Sellmeier | Rango (µm) |
|---|---|---|
| Sílice fundida | $n^2=1+\dfrac{0{,}6962\lambda^2}{\lambda^2-(0{,}06840)^2}+\dfrac{0{,}4079\lambda^2}{\lambda^2-(0{,}1162)^2}+\dfrac{0{,}8975\lambda^2}{\lambda^2-(9{,}8962)^2}$ | 0,21–3,71 |
| Si | $n^2=1+\dfrac{10{,}6684\lambda^2}{\lambda^2-(0{,}3015)^2}+\dfrac{0{,}0030\lambda^2}{\lambda^2-(1{,}1347)^2}+\dfrac{1{,}5413\lambda^2}{\lambda^2-(1104{,}0)^2}$ | 1,36–11 |
| GaAs | $n^2=3{,}5+\dfrac{7{,}4969\lambda^2}{\lambda^2-(0{,}4082)^2}+\dfrac{1{,}9347\lambda^2}{\lambda^2-(37{,}17)^2}$ | 1,4–11 |
| BBO | $n_o^2=2{,}7359+\dfrac{0{,}01878}{\lambda^2-0{,}01822}-0{,}01354\lambda^2$ ; $n_e^2=2{,}3753+\dfrac{0{,}01224}{\lambda^2-0{,}01667}-0{,}01516\lambda^2$ | 0,22–1,06 |
| KDP | $n_o^2=1+\dfrac{1{,}2566\lambda^2}{\lambda^2-(0{,}09191)^2}+\dfrac{33{,}8991\lambda^2}{\lambda^2-(33{,}3752)^2}$ ; $n_e^2=1+\dfrac{1{,}1311\lambda^2}{\lambda^2-(0{,}09026)^2}+\dfrac{5{,}7568\lambda^2}{\lambda^2-(28{,}4913)^2}$ | 0,4–1,06 |
| LiNbO₃ | $n_o^2=2{,}3920+\dfrac{2{,}5112\lambda^2}{\lambda^2-(0{,}217)^2}+\dfrac{7{,}1333\lambda^2}{\lambda^2-(16{,}502)^2}$ ; $n_e^2=2{,}3247+\dfrac{2{,}2565\lambda^2}{\lambda^2-(0{,}210)^2}+\dfrac{14{,}503\lambda^2}{\lambda^2-(25{,}915)^2}$ | 0,4–3,1 |

Nota: en el formato $\chi_{0i}\lambda^2/(\lambda^2-\lambda_i^2)$ de (5.5-28), para la sílice
$\chi_{0i}=\{0{,}6962,\,0{,}4079,\,0{,}8975\}$ y $\lambda_i=\{0{,}06840,\,0{,}1162,\,9{,}8962\}$ µm.
Para GaAs la constante 3,5 equivale a un término con $\lambda_i=0$ (Problema 5.6-1c).

**Fórmulas de uso frecuente (resumen de bolsillo)**:
- $n=\sqrt{1+\chi}$ (5.2-13); $\eta=\eta_o/n$ (5.4-6); $I=|E_0|^2/2\eta$ (5.4-8); $I=cW$ (5.4-10).
- $n-j\alpha/2k_o=\sqrt{1+\chi'+j\chi''}$ (5.5-5); débil: $n\approx\sqrt{1+\chi'}$, $\alpha\approx-(k_o/n)\chi''$;
  diluido en $n_0$: $n\approx n_0+\chi'/2n_0$, $\alpha\approx-k_o\chi''/n_0$.
- Lorentz: $\chi(\nu)=\chi_0\nu_0^2/(\nu_0^2-\nu^2+j\nu\Delta\nu)$, $\chi_0=Ne^2/\epsilon_om\omega_0^2$,
  $Q=\nu_0/\Delta\nu$, pico $-\chi''(\nu_0)=\chi_0Q$.
- $N=n-\lambda_o\,dn/d\lambda_o$; $v=c_o/N$; $D_\nu=\frac{\lambda_o^3}{c_o^2}\frac{d^2n}{d\lambda_o^2}=2\pi\beta''$;
  $D_\lambda=-\frac{\lambda_o}{c_o}\frac{d^2n}{d\lambda_o^2}$; $\sigma_\tau=|D_\lambda|\sigma_\lambda z$.
- Normal: $\beta''>0$, $D_\nu>0$, $D_\lambda<0$. Anómala: $\beta''<0$, $D_\nu<0$, $D_\lambda>0$.
- Conductor: $\epsilon_e=\epsilon+\sigma/j\omega$; $d_p=1/\sqrt{2\omega\mu_o\sigma}$; Drude
  $\epsilon_e=\epsilon_o(1-\omega_p^2/\omega^2)$, $\omega_p=\sqrt{Ne^2/\epsilon_om}$.

---

## Problemas al final del capítulo (p. 195–196)

Lista completa transcrita. Ninguno está marcado con * en el libro (solo la sección 5.7 es avanzada;
no tiene problemas). Nótese que **no existe problema 5.5-1**: la numeración salta de 5.4-1 a 5.5-2
porque el 5.5-1 es el *Exercise* del texto (p. 172).

**5.1-1 An Electromagnetic Wave.** An electromagnetic wave in free space has an electric-field
vector $\mathcal{E}=f(t-z/c_o)\hat{\mathbf x}$, where $\hat{\mathbf x}$ is a unit vector in the $x$
direction and $f(t)=\exp(-t^2/\tau^2)\exp(j2\pi\nu_0t)$, where $\tau$ is a constant. Describe the
physical nature of this wave and determine an expression for the magnetic-field vector.

**5.2-1 Dielectric Media.** Identify the media described by the following equations, regarding
linearity, dispersiveness, spatial dispersiveness, and homogeneity. Assume that all media are
isotropic.
(a) $\mathcal{P}=\epsilon_o\chi\mathcal{E}-a\nabla\times\mathcal{E}$,
(b) $\mathcal{P}+a\mathcal{P}^2=\epsilon_o\mathcal{E}$,
(c) $a_1\,\partial^2\mathcal{P}/\partial t^2+a_2\,\partial\mathcal{P}/\partial t+\mathcal{P}=\epsilon_o\chi\mathcal{E}$,
(d) $\mathcal{P}=\epsilon_o\{a_1+a_2\exp[-(x^2+y^2)]\}\mathcal{E}$,
where $\chi$, $a$, $a_1$, and $a_2$ are constants.

**5.3-1 Traveling Standing Wave.** The electric-field complex-amplitude vector for a monochromatic
wave of wavelength $\lambda_o$ traveling in free space is $\mathbf E(\mathbf r)=E_0\sin\beta y\,\exp(-j\beta z)\hat{\mathbf x}$.
(a) Determine a relation between $\beta$ and $\lambda_o$.
(b) Derive an expression for the magnetic-field complex-amplitude vector $\mathbf H(\mathbf r)$.
(c) Determine the direction of the flow of optical power.
(d) This wave may be regarded as the sum of two TEM plane waves. Determine their directions of
propagation.

**5.4-1 Electric Field of Focused Light.**
(a) 1 W of optical power is focused uniformly on a flat target of size $0.1\times0.1$ mm² placed in
free space. Determine the peak value of the electric field $E_0$ (V/m). Assume that the optical wave
is approximated as a TEM plane wave within the area of the target.
(b) Determine the electric field at the center of a Gaussian beam (a point on the beam axis at the
beam waist) if the beam power is 1 W and the beam waist radius $W_0=0.1$ mm. Refer to Sec. 3.1.

**5.5-2 Amplitude-Modulated Wave in a Dispersive Medium.** An amplitude-modulated wave whose complex
wavefunction takes the form $\mathcal{A}(t)=[1+m\cos(2\pi f_st)]\exp(j2\pi\nu_0t)$ at $z=0$, where
$f_s\ll\nu_0$, travels a distance $z$ through a dispersive medium of propagation constant
$\beta(\nu)$ and negligible attenuation. If $\beta(\nu_0)=\beta_0$, $\beta(\nu_0-f_s)=\beta_1$, and
$\beta(\nu_0+f_s)=\beta_2$, derive an expression for the complex envelope of the transmitted wave as
a function of $\beta_0$, $\beta_1$, $\beta_2$, and $z$. Show that at certain distances $z$ the wave is
amplitude modulated with no phase modulation.

**5.6-1 Group Velocity Dispersion in a Medium Described by the Sellmeier Equation.**
(a) Derive expressions for the group index $N$ and the group velocity dispersion coefficient
$D_\lambda$ for a medium whose refractive index is described by the Sellmeier equation (5.5-28).
(b) Use a computer to plot the wavelength dependence of $n$, $N$, and $D_\lambda$ for fused silica
in the region between 0.25 and 3.5 µm. Make use of the parameters provided in Table 5.5-1 (and
Example 5.6-1). Verify the curves provided in Fig. 5.6-5.
(c) Construct a similar collection of plots for GaAs in the region between 1.5 and 10.5 µm. As
indicated in Table 5.5-1, GaAs is characterized by a 3-term Sellmeier equation with resonance
wavelengths 0 µm, 0.4082 µm, and 37.17 µm, whose weights are 3.5, 7.4969, and 1.9347, respectively,
in the wavelength region between 1.4 and 11 µm at room temperature. Compare and contrast the
behavior of the dispersion properties of fused silica and GaAs.

**5.6-2 Refractive Index of Air.** The refractive index of air can be precisely measured with the
help of a Michelson interferometer and a tunable light source. At atmospheric pressure and a
temperature of 20 °C, the refractive index of air differs from unity by $n-1=2.672\times10^{-4}$ at
a wavelength of 0.76 µm, by $n-1=2.669\times10^{-4}$ at a wavelength of 0.81 µm, and by
$n-1=2.665\times10^{-4}$ at a wavelength of 0.86 µm.
(a) Using a quadratic fit to these data, determine the wavelength dependence of the group velocity.
(b) Obtain an expression for the dispersion coefficient $D_\lambda$ in ps/km-nm and compare your
result with that for a silica optical fiber.

**5.6-3 Group Velocity in a Metal.** Show that for a medium described by the Drude model, (5.5-39),
the product of the phase velocity and the group velocity is equal to $c_o^2$.

**Ejercicio dentro del texto** (para completar la lista de enunciados):
**EXERCISE 5.5-1 Dilute Absorbing Medium** (p. 172–173): ver §5.5A arriba; resultado (5.5-9), (5.5-10).

---

## Relación con Óptica No Lineal

### Con los temas del curso

- **Ondas EM y ecuación de onda con $\mathcal{P}$ como fuente (temas 1–2).** La ecuación (5.2-25),
  $\nabla^2\mathcal{E}-c_o^{-2}\partial_t^2\mathcal{E}=\mu_o\partial_t^2\mathcal{P}$ (p. 161), es
  exactamente el punto de partida de Boyd (*Nonlinear Optics*, 3.ª ed., §2.1) cuando se separa
  $\mathcal{P}=\mathcal{P}^{(1)}+\mathcal{P}^{NL}$: el término lineal se absorbe en $n^2/c_o^2$ y
  $\mathcal{P}^{NL}$ queda como fuente, $\nabla^2\mathcal{E}-\frac{n^2}{c_o^2}\partial_t^2\mathcal{E}
  =\mu_o\partial_t^2\mathcal{P}^{NL}$. Saleh ya lo anticipa con (5.2-26) y con la forma perturbativa
  (5.2-20), $\Delta\mathcal{P}=2\epsilon_on\Delta n\,\mathcal{E}$ (p. 159), que es la misma álgebra que
  lleva al índice dependiente de la intensidad $n=n_0+n_2I$ (Kerr óptico, $\Delta n\propto\chi^{(3)}|E|^2$).
- **Clasificación de medios (tema 1).** El recuadro de definiciones (p. 156) —lineal, no
  dispersivo, homogéneo, isótropo, espacialmente no dispersivo— es la base para enunciar las
  hipótesis de cada modelo no lineal (p. ej. $\chi^{(2)}$ solo en medios **anisótropos sin centro de
  inversión**; la respuesta instantánea de Kerr es la idealización "no dispersiva"; la convolución
  (5.2-23) es el caso lineal del tensor de respuesta $R^{(n)}(t_1,\dots,t_n)$ de Boyd §1.3). El
  Problema 5.2-1 entrena justamente esa clasificación.
- **Susceptibilidad compleja, $n$ y $\alpha$ (tema 2).** (5.5-5), (5.5-7)–(5.5-10) y la convención
  $\chi''<0$ ↔ absorción (por $e^{j\omega t}$). Al pasar a Boyd (convención $e^{-i\omega t}$,
  $\chi''>0$ absorbe) hay que **cambiar el signo de la parte imaginaria**; es la trampa habitual al
  comparar fórmulas de absorción de dos fotones o de $\mathrm{Im}\,\chi^{(3)}$.
- **Kramers–Kronig (5.5-13)–(5.5-14).** Mismo formalismo que se usa en ONL para relacionar
  $n_2$ con el coeficiente de absorción de dos fotones $\beta_{TPA}$ (Sheik-Bahae et al.): el índice
  no lineal es la transformada de Hilbert de la absorción no lineal (ver cap. 21 de Saleh y Boyd
  §4.x). Condición: sistema lineal, causal, invariante, respuesta real.
- **Oscilador de Lorentz (5.5-15)–(5.5-21).** Es la versión lineal del **oscilador anarmónico** de
  Boyd §1.4: añadiendo un término $a x^2$ (medio no centrosimétrico) o $b x^3$ (centrosimétrico) a
  (5.5-16) se obtienen $\chi^{(2)}(\omega_1+\omega_2)$ y $\chi^{(3)}$ con los mismos denominadores
  resonantes $D(\omega)=\omega_0^2-\omega^2+j\sigma\omega$. Los límites $\nu\ll\nu_0$ ($\chi\to\chi_0$),
  $\nu\gg\nu_0$ (vacío) y la lorentziana con $Q=\nu_0/\Delta\nu$ reaparecen en la regla de Miller y en
  el realce resonante de $\chi^{(n)}$.
- **Sellmeier (5.5-28) y Tabla 5.5-1.** Imprescindible para **phase matching**: $\Delta k=k_3-k_1-k_2$
  en SHG/SFG se calcula con $n(\lambda)$ de Sellmeier; la tabla trae BBO, KDP y LiNbO₃ (índices
  $n_o$, $n_e$) que son los cristales $\chi^{(2)}$ típicos, además de sílice, Si y GaAs. Y para
  comparar con el Problema 5.6-1 (GaAs vs sílice).
- **Velocidad de grupo, índice de grupo, $D_\nu$, $D_\lambda$ (5.6-1)–(5.6-8).** Todo el formalismo
  de **GVD** del curso: $\beta''=D_\nu/2\pi$, $D_\lambda=-\frac{\lambda_o}{c_o}d^2n/d\lambda_o^2$, y la
  relación $D_\lambda=-\frac{2\pi c_o}{\lambda_o^2}\beta_2$ (Agrawal) se obtiene de (5.6-4) y (5.6-7).
  La dispersión anómala ($\beta''<0$, $D_\lambda>0$) es el requisito para **solitones** (SPM + GVD
  anómala se compensan) y para generación de supercontinuo por fisión de solitones; la dispersión
  normal da ensanchamiento y chirp positivo que se suma al de SPM (compresión por rejillas). El
  **group-velocity mismatch** (walk-off temporal) entre fundamental y armónico en SHG de pulsos cortos
  se calcula con $N=n-\lambda\,dn/d\lambda$ (5.6-2) para cada onda.
- **Pulsos gaussianos, $z_0$, chirp.** Este capítulo solo trata cualitativamente el chirp
  (Fig. 5.6-3, p. 187) y menciona que un gaussiano bajo GVD sigue siendo gaussiano más ancho (p. 188);
  las fórmulas cuantitativas ($\tau(z)=\tau_0\sqrt{1+(z/z_0)^2}$ con $z_0=\tau_0^2/|D_\nu|$ en forma
  análoga al haz gaussiano espacial, chirp lineal, factor de chirp) están en **§22.3** y no se
  transcribieron aquí porque no están en el cap. 5. El $z_0$ que sí aparece es el **parámetro de
  Rayleigh espacial** del haz gaussiano (5.4-20), que es el que entra en la longitud de interacción
  efectiva en SHG con haces enfocados (Boyd–Kleinman, $L/b$ con $b=2z_0$).
- **Haz gaussiano vectorial (5.4-20) y relación escalar/vectorial (§5.4B).** Justifica usar la
  teoría escalar (envolvente lentamente variable, SVEA) en la mayoría de los cálculos de ONL con haces
  paraxiales, y la conversión $U=E/\sqrt{2\eta}$, $I=|E_0|^2/2\eta$ (5.4-8) con $\eta=\eta_o/n$ para
  pasar de intensidad a amplitud de campo — paso obligado al evaluar $n_2I$ o $\chi^{(3)}|E|^2$.
  El Problema 5.4-1 (campo de 1 W enfocado en 0,1 mm) es el cálculo típico de "¿cuánto campo hay?".
- **Polarización y cristales.** §5.2B (tensor $\chi_{ij}$, (5.2-21)–(5.2-22)) y las condiciones de
  frontera (p. 154) preparan el cap. 6 (birrefringencia, phase matching tipo I/II, walk-off espacial).
- **Raman, FWM, XPM.** La convolución (5.2-23) generaliza a la respuesta Raman retardada
  $h_R(t)$ en la ecuación de Schrödinger no lineal generalizada; la figura de múltiples resonancias
  (Fig. 5.5-8) ilustra por qué $\chi^{(3)}$ tiene parte electrónica instantánea y parte vibracional
  (Raman) con retardo. La GVD y $D_\lambda$ de (5.6-7) fijan el phase matching de FWM ($\Delta k=
  \beta_2\Omega^2+\dots+2\gamma P$) y la ganancia paramétrica en fibras.
- **Medios conductores, Drude, plasmones (§5.5D).** Útil para la óptica no lineal plasmónica y para
  entender los límites de metales como electrodos/calentadores; el Problema 5.6-3 (v·v_fase = c_o²)
  es un ejercicio de velocidad de grupo con dispersión de plasma.

### Con el proyecto final (anillos add-drop en Si₃N₄, dispersión de guías, supercontinuo, sensado)

- **FSR y Q de anillos**: $\mathrm{FSR}=\lambda^2/(N_{g}L)$ requiere el **índice de grupo** (5.6-2)
  del modo guiado, no el efectivo; Saleh define $N$ exactamente con la derivada $dn/d\lambda$, que
  en la guía se reemplaza por $dn_{\rm eff}/d\lambda$ (FDE/MODE lo reporta como $n_g$). La
  **sensibilidad de volumen** $S=\partial\lambda_{res}/\partial n_{clad}=(\lambda/N_g)\,\partial n_{\rm eff}/\partial n_{clad}$
  también lleva $N_g$ en el denominador.
- **Dispersión de la guía**: $D_\lambda$ (5.6-7) con $n\to n_{\rm eff}(\lambda)$ da la dispersión
  total (material + geométrica). La convención de signos de Saleh (normal $D_\lambda<0$, anómala
  $D_\lambda>0$, p. 187) coincide con la de fibras (ps/km-nm → en guías integradas ps/nm-km o
  $\beta_2$ en ps²/m); para **supercontinuo** y peines Kerr en Si₃N₄ se busca $\beta_2<0$
  (anómala) cerca de 1550 nm, lo que exige ingeniería geométrica porque la sílice (cladding) y el
  Si₃N₄ masivo tienen dispersión normal allí (sílice: cero en 1,276 µm, Ejemplo 5.6-1).
- **Materiales**: la Sellmeier de la **sílice** (Tabla 5.5-1) es la del cladding/BOX; la de **Si**
  (válida 1,36–11 µm) sirve para el sustrato. La tabla **no** incluye Si₃N₄ ni agua; para el
  analito ($n=1{,}33$–$1{,}37$) y para Si₃N₄ (Luke et al. 2015) hay que tomar las Sellmeier de la
  bibliografía del proyecto (`proyecto-final/contexto-fotonica-integrada.md`).
- **Pérdidas y absorción**: (5.5-8) y (5.5-10) relacionan $\alpha$ con $\mathrm{Im}\,\chi$ o con
  $\mathrm{Im}\,n_{\rm eff}$: $\alpha=2k_o\,\mathrm{Im}\{n_{\rm eff}\}$ (potencia); se usa para
  convertir el $\kappa$ que entrega el solver de modos en dB/cm ($\alpha_{dB}=4{,}343\,\alpha$) y para
  estimar el $Q$ intrínseco. El agua absorbe en el IR cercano: su $\chi''$ (negativo en esta
  convención) limita el $Q$ del anillo sensor con cladding líquido.
- **Kramers–Kronig** recuerda que cualquier cambio de absorción del analito (p. ej. una banda de
  absorción en la ventana de trabajo) va acompañado de un cambio de índice: relevante al interpretar
  corrimientos de resonancia en sensado de volumen.
- **Metamateriales/plasmones (§5.7, §5.5D)**: no entran en los estudios actuales (sensado de volumen
  sin funcionalización); quedan como referencia para una eventual etapa de sensado superficial.
