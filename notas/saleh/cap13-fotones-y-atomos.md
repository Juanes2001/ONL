# Capítulo 13 — Photons and Atoms (Saleh & Teich, 2.ª ed.)

Páginas del libro 482–531 (PDF 504–553). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007,
cap. 13 "Photons and Atoms". Notación del libro: dependencia temporal $e^{j\omega t}$ con
$j=\sqrt{-1}$; $h$ constante de Planck, $\hbar = h/2\pi$, $k$ constante de Boltzmann,
$c = c_o/n$ velocidad de la luz en el medio, $\lambda = \lambda_o/n$ longitud de onda en el
medio, $\nu$ frecuencia (Hz). Unidades SI, salvo donde el libro usa cm² para secciones
eficaces (se indica).

Secciones marcadas con * en el índice del libro (avanzadas): 13.3E y 13.3F.

---

## Resumen del capítulo

El capítulo presenta las leyes que gobiernan la interacción luz–materia a nivel de un átomo
y de colecciones de átomos, con miras a los amplificadores y osciladores láser de los
capítulos 14 y 15. Empieza con un repaso de los niveles de energía de átomos (hidrógeno,
multielectrónicos), moléculas (rotación, vibración, colorantes) y sólidos (bandas, medios
dieléctricos dopados con Cr³⁺ y Nd³⁺, semiconductores masivos, pozos, hilos y puntos
cuánticos) (§13.1); después la ocupación de esos niveles en equilibrio térmico mediante las
distribuciones de Boltzmann y de Fermi–Dirac (§13.2). El núcleo es §13.3: las tres formas de
interacción fotón–átomo (emisión espontánea, absorción y emisión estimulada) se describen
mediante una sección eficaz de transición $\sigma(\nu) = S\,g(\nu)$, que conduce a la vida
media espontánea $t_{sp}$, a la relación $\bar\sigma(\nu) = (\lambda^2/8\pi t_{sp})\,g(\nu)$,
a las tasas inducidas $W_i = \phi\sigma(\nu)$ y $W_i = \bar n/t_{sp}$, y a los coeficientes
A y B de Einstein; luego se discuten los mecanismos de ensanchamiento de línea (vida media,
colisiones, Doppler), el factor de Purcell y el enfriamiento láser. §13.4 deduce el espectro
de radiación de cuerpo negro (Planck) a partir de la ecuación de tasas de un sistema de dos
niveles en equilibrio. §13.5 cierra con las formas de luminiscencia (catodo-, sono-, quimio-,
bio-, electro- y fotoluminiscencia; fluorescencia y fosforescencia; fluorescencia
multifotónica y de conversión ascendente) y con la dispersión de luz: Rayleigh, Mie, Raman
(Stokes/anti-Stokes), Brillouin y sus versiones estimuladas (SRS, SBS, CARS, supercontinuo
por Raman en fibras).

---

## Secciones

### Introducción (p. 483)

- La luz interactúa con la materia porque ésta contiene cargas eléctricas; el campo
  eléctrico variable de la luz las acelera y las cargas vibrantes absorben y emiten luz
  (p. 483).
- Un fotón interactúa con un átomo si su energía coincide con la diferencia entre dos
  niveles: si el átomo está en el nivel inferior el fotón es **absorbido** (aniquilado); si
  está en el superior el fotón **estimula** la emisión de un segundo fotón de igual energía
  → base del láser (p. 483).
- Las excitaciones térmicas producen transiciones constantes; en equilibrio estacionario el
  conjunto fotones+átomos produce **luz térmica** con el espectro de cuerpo negro, cuyo pico
  se corre hacia frecuencias altas al subir T (p. 483).
- Otras fuentes de excitación (UV, sonido, corriente, reacciones químicas) producen
  **luminiscencia**; también hay radiación Cherenkov y Bremsstrahlung (p. 483).
- La **dispersión de luz** altera dirección y energía del fotón y revela niveles internos
  (p. ej. vibraciones moleculares) (p. 483).

### 13.1 Energy Levels (p. 483)

**Ecuación de Schrödinger** para una partícula no relativista de masa $m$ en un potencial
$V(\mathbf r, t)$ (p. 484):

$$-\frac{\hbar^2}{2m}\nabla^2\Psi(\mathbf r,t) + V(\mathbf r,t)\Psi(\mathbf r,t)
= -j\hbar\,\frac{\partial\Psi(\mathbf r,t)}{\partial t} \qquad (13.1\text{-}1)$$

(nótese el signo $-j\hbar$, coherente con la convención $e^{j\omega t}$ del libro). El
libro señala que (13.1-1) es matemáticamente análoga a la ecuación paraxial de Helmholtz
(2.2-23) y a la ecuación de envolvente lentamente variable de la óptica ultrarrápida
(22.1-24) (p. 484).

**Postulado de Born** (p. 484): probabilidad de hallar la partícula en $dV$ alrededor de
$\mathbf r$ entre $t$ y $t+dt$:

$$p(\mathbf r,t)\,dV\,dt = |\Psi(\mathbf r,t)|^2\,dV\,dt \qquad (13.1\text{-}2)$$

(análoga a (12.1-14) para la probabilidad de hallar un fotón).

Sin potencial dependiente del tiempo, separación de variables
$\Psi(\mathbf r,t) = \psi(\mathbf r)\exp[j(E/\hbar)t]$ lleva a la **ecuación de Schrödinger
independiente del tiempo** (p. 484):

$$-\frac{\hbar^2}{2m}\nabla^2\psi(\mathbf r) + V(\mathbf r)\psi(\mathbf r) = E\,\psi(\mathbf r)
\qquad (13.1\text{-}3)$$

Es un problema de autovalores (análogo a Helmholtz (2.2-7)): las energías permitidas $E$
son los autovalores y $\psi(\mathbf r)$ las autofunciones. Los niveles pueden ser discretos
(átomo), continuos (partícula libre) o bandas (semiconductor) (p. 484).

#### 13.1A Atoms (p. 484)

**Hidrógeno** (p. 485). Átomo hidrogenoide (núcleo $+Ze$, un electrón $-e$ de masa $m$),
potencial de Coulomb $V(r) = -Ze^2/r$ (el libro escribe el potencial sin el factor
$1/4\pi\epsilon_o$ pero lo incluye en la energía). Niveles discretos:

$$E_{\mathrm n} = -\frac{M_r Z^2 e^4}{(4\pi\epsilon_o)^2\,2\hbar^2}\,\frac{1}{\mathrm n^2},
\qquad \mathrm n = 1,2,3,\dots \qquad (13.1\text{-}4)$$

donde $M_r$ es la masa reducida (sustituye a $m$ por la masa finita del núcleo) y n es el
**número cuántico principal**. Mismo resultado con la **teoría de Bohr**: fuerza de Coulomb
= centrífuga con momento angular orbital cuantizado en múltiplos de $\hbar$; radios de
Bohr $r_{\mathrm n} = (4\pi\epsilon_o)\,\mathrm n^2\hbar^2/(mZe^2)$ (p. 485).

Autofunciones $\psi_{\mathrm n\ell\mathrm m}(r,\theta,\phi) = \mathbb R_{\mathrm n\ell}(r)\,
\Theta_{\ell\mathrm m}(\theta)\,\Phi_{\mathrm m}(\phi)$: $\ell = 0,\dots,\mathrm n-1$
**número cuántico azimutal**, $\mathrm m = 0,\pm1,\dots,\pm\ell$ **número cuántico
magnético**; $\mathbb R$ funciones de Laguerre asociadas, $\Theta$ de Legendre asociadas,
$\Phi$ funciones de fase (análogas al microcavidad esférica §10.4C) (p. 485). Espín
$s=\pm\tfrac12$ → interacción espín–órbita → **estructura fina**; interacción con el
momento magnético nuclear → **estructura hiperfina**; correcciones relativistas → "teoría
de Dirac" (pp. 485–486).

- **Fig. 13.1-1** (p. 485): niveles de H ($Z=1$, eje izquierdo, hasta ~13.6 eV) y de C⁵⁺
  (hidrogenoide $Z=6$, eje derecho, hasta ~504 eV); la transición n=3→2 de C⁵⁺ es el láser
  de UV extremo a 18.2 nm (§15.3C). Cero de energía en n=1.

**Átomos multielectrónicos** (p. 486). Núcleo $+Ze$ con $Z$ electrones. Se resuelve con el
**método de Hartree** (autoconsistente): cada electrón se mueve independientemente en un
potencial esféricamente simétrico neto $V(r)$ = atracción del núcleo + repulsión promedio de
los demás; la ecuación de $Z$ electrones se separa en $Z$ ecuaciones monoelectrónicas;
luego perturbaciones para la no esfericidad y el espín. Llenado por **principio de
exclusión de Pauli**: capas (n), **subcapas** $\mathrm n\ell$ con letras
$s,p,d,f,g,h,i \leftrightarrow \ell = 0,\dots,6$; **configuración electrónica** $\mathrm n\ell^u$
($u$ = número de electrones). Ejemplos: He $1s^2$; excitados $1s2s$, $1s2p$; Ne
$1s^22s^22p^6$ (p. 486).

Cada configuración forma un **multiplete** (manifold) de niveles de estructura fina, por
acoplamiento espín–órbita (acoplamiento Russell–Saunders o LS). **Símbolo de término**
$^{2\mathcal S+1}\mathcal L_{\mathcal J}$: $\mathcal S$ espín total ($2\mathcal S+1$
multiplicidad: singlete, triplete...), $\mathcal L$ momento angular orbital total con letras
mayúsculas $S,P,D,F,\dots \leftrightarrow 0,1,2,3,\dots$; $\mathcal J$ momento angular total.
Ej.: niveles singlete y triplete más bajos de He: $1s2s\,^1S_0$ y $1s2s\,^3S_1$. Capas
llenas (gases nobles, Ca, Cd, Yb, Hg en estado base) → $^1S_0$ (pp. 486–487).

Órdenes de magnitud (p. 487): corrimientos espín–órbita ≈ 1 parte en $10^4$ para H,
crecen con $Z$; relativistas ≈ 1 en $10^4$ independientes de $Z$; hiperfinos $10^3$ veces
menores; espín–espín despreciable.

- **Fig. 13.1-2** (p. 487): niveles de He (16–21 eV) y Ne ($2p^53s$, $2p^54s$, $2p^55s$,
  $2p^53p$; paridad impar/par). Transiciones del láser He–Ne: $2p^55s\to2p^53p$ a
  **3.39 µm** y $2p^54s\to2p^53p$ a **632.8 nm**. La cercanía energética entre los niveles
  excitados de He y de Ne permite excitar el Ne por colisiones en la descarga (de ahí
  "láser He–Ne").
- **Fig. 13.1-3** (p. 488): tabla periódica; filas ↔ n; columnas ↔ mismo número de
  electrones de valencia. Columna VIII (gases nobles) inerte; columnas I y VII muy activas.
- Las diferencias de energía entre niveles excitados de Ne están en el IR y visible,
  típicamente hasta varios eV (p. 488; ver Fig. 12.1-2 para unidades de energía).

#### 13.1B Molecules (p. 488)

Enlaces **iónico** (HF: momento dipolar permanente) y **covalente** (H₂: sin dipolo
permanente). Tres tipos de transición con escalas de tiempo distintas: **rotacionales**
(microondas y IR lejano), **vibracionales** (IR), **electrónicas** (visible y UV); a primera
aproximación se analizan por separado (p. 488).

**Molécula diatómica rotante** (p. 489). Rotor rígido con momento de inercia $\mathcal J$;
$E_{\mathfrak r} = L^2/2\mathcal J$ con $L^2 = \mathfrak r(\mathfrak r+1)\hbar^2$:

$$E_{\mathfrak r} = \frac{1}{2\mathcal J}\,\mathfrak r(\mathfrak r+1)\hbar^2,
\qquad \mathfrak r = 0,1,2,\dots \qquad (13.1\text{-}5)$$

Separaciones $\hbar\omega$ típicas $10^{-4}$–$10^{-2}$ eV (microondas / IR lejano). El
espaciado **crece** con $\mathfrak r$ (al contrario que en H). Moléculas homonucleares (N₂)
no tienen dipolo permanente → sin espectro rotacional puro (p. 489).

**Molécula diatómica vibrante** (p. 489). Masas $M_1, M_2$, masa reducida
$M_r = M_1M_2/(M_1+M_2)$, constante de resorte $\kappa$, $V(x) = \tfrac12\kappa x^2$:

$$E_{\mathfrak v} = \left(\mathfrak v + \tfrac12\right)\hbar\omega,
\qquad \mathfrak v = 0,1,2,\dots \qquad (13.1\text{-}6)$$

con $\omega = \sqrt{\kappa/M_r}$ y $\tfrac12\hbar\omega$ energía de punto cero. Idéntica a
(12.1-5) para un modo del campo EM. $\hbar\omega$ típico **0.05–0.5 eV** (IR). Niveles
equiespaciados; en la práctica los potenciales son anarmónicos (§21.7) y el espaciado
disminuye al crecer $\mathfrak v$. Transiciones vibracionales–rotacionales cambian ambos
números (p. 489).

**Molécula triatómica vibrante — CO₂** (pp. 489–490). Lineal; tres modos normales
independientes: **estiramiento asimétrico (AS)**, **simétrico (SS)** y **flexión (B)**, cada
uno un oscilador armónico con su $\hbar\omega$; niveles etiquetados
$(\mathfrak v_1,\mathfrak v_2,\mathfrak v_3)$.

- **Fig. 13.1-4** (p. 490): niveles vibracionales más bajos de N₂ ($\mathfrak v=0,1$;
  ≈0.3 eV) y de CO₂; transiciones láser $(001)\to(100)$ a **10.6 µm** y $(001)\to(020)$ a
  **9.6 µm** (§14.3E, §15.3D). Cada nivel vibracional tiene un multiplete de niveles
  rotacionales (no mostrados).

**Molécula de colorante** (p. 490). Moléculas orgánicas grandes con transiciones
electrónicas, vibracionales y rotacionales; estados **singlete (S)** y **triplete (T)**
(espines antiparalelos / paralelos). Rodamina 6G ($\mathrm{C_{28}H_{31}N_2O_3^+}$ en
disolución) lasea en amarillo (§15.3C).

- **Fig. 13.1-5** (p. 491): estructura de niveles de Rodamina-6G: multipletes S₀, S₁ (láser
  S₁→S₀), T₁, T₂, en escala 0–5 eV; niveles vibracionales (líneas gruesas) y rotacionales
  (finas).

#### 13.1C Solids (p. 490)

Red cristalina; sólidos no cristalinos (vidrios, plásticos) tienen orden de corto alcance.
Tres tipos de enlace (p. 491): **iónicos** (CaF₂; aislantes, transparentes en visible,
bandgap en UV), **covalentes** (diamante transparente, grafito opaco; semiconductores como
GaAs opacos en visible y transparentes en IR), **metálicos** (electrones compartidos por
todos los iones → conductividad; reflejan fuertemente y son opacos en visible).

Formación de bandas (p. 491): al acercar átomos idénticos, las interacciones de intercambio
y los campos vecinos ensanchan los niveles de valencia en **bandas**; los niveles internos
siguen siendo agudos por apantallamiento.

- **Fig. 13.1-6** (p. 492): (a) dos átomos aislados, (b) molécula diatómica, (c) cristal 1D
  de cinco átomos.
- **Fig. 13.1-7** (p. 492): niveles $1s,2s,2p$ agudos y $3s,3p$ en bandas para átomo
  aislado, metal, semiconductor y aislante. **Banda de conducción** = más baja no ocupada o
  parcialmente ocupada; **banda de valencia** = más alta completamente ocupada; **banda
  prohibida** de ancho $E_g$ (**bandgap**). Conductividades típicas a temperatura
  ambiente: metales $10^8\ (\Omega\cdot\mathrm m)^{-1}$, semiconductores
  $10^{-4}$–$10^{5}\ (\Omega\cdot\mathrm m)^{-1}$, aislantes $10^{-10}\ (\Omega\cdot\mathrm m)^{-1}$.

Metales: banda de conducción parcialmente ocupada a toda T (§5.5D). Semimetales: bandas
solapadas. **Semiconductor intrínseco**: a $T=0$ K valencia llena, conducción vacía,
conductividad cero; al subir T, electrones térmicos pasan a conducción. **Aislantes**:
igual pero $E_g > 3$ eV típicamente. Ejemplos: Si $E_g \approx 1.1$ eV; diamante
$E_g \approx 5.5$ eV (pp. 492–493).

**Medios dieléctricos dopados** (p. 493). Sólidos iónicos o covalentes transparentes sirven
de anfitrión (host) de iones láser activos; el host se describe bien con el oscilador de
Lorentz (§5.5C) porque sus resonancias están fuera de la región de trabajo; las resonancias
de los dopantes se determinan empíricamente. Los dopantes más comunes son metales de
transición y lantánidos. Regla clave (p. 493): los niveles de los **metales de transición**
se modifican sustancialmente por el **campo cristalino**; los de los **lantánidos** apenas.

*Iones de metales de transición* (pp. 493–495): Cr³⁺ y Ti³⁺ (también Ni²⁺, Co²⁺).
**Rubí** Cr³⁺:Al₂O₃ (zafiro/alúmina/corindón con ≈0.05 % de Al³⁺ sustituidos por Cr³⁺),
$n\approx1.76$, uniaxial; primer láser. **Alexandrita** Cr³⁺:BeAl₂O₄ (≈0.1 % óxido de
cromo en crisoberilo), $n\approx1.74$, biaxial; sintonizable. Los electrones $3d$ del Cr³⁺
están expuestos a los iones vecinos → **teoría del campo cristalino (campo ligando)**;
niveles designados con símbolos de teoría de grupos ($^4A_2$, $^2E$, $^4T_2$, $^4F_1$,
$^4F_2$).

- **Tabla 13.1-1** (p. 494): configuraciones y términos (ver sección de tablas abajo).
- **Fig. 13.1-8** (p. 494): rubí: $^4F_1$, $^4F_2$ (bandas), $^2E$ → láser **694 nm** a
  $^4A_2$. Alexandrita: $^4T_2$/$^2E$ → láser **680 nm** y láser sintonizable hacia una
  banda $^4A_2$ **vibrónica** (acoplamiento electrónico–vibraciones de red, estados
  parecidos a los de un colorante); el sombreado oscuro→claro indica ocupación decreciente
  de la banda láser inferior (p. 495).

*Iones lantánidos* (p. 495): serie ⁵⁸Ce a ⁷¹Lu, "tierras raras" (no lo son); se llenan los
$4f$ dentro de las subcapas llenas $5s^25p^6$ y $6s^2$; cationes trivalentes $4f^u$, $u=1$
(Ce³⁺) a 14 (Lu³⁺). Nd³⁺, Er³⁺, Yb³⁺ son los dopantes principales (Nd³⁺:vidrio y
Er³⁺:fibra de sílice como amplificadores §14.3B–C; Nd³⁺:YAG, Nd³⁺:YVO₄, Yb³⁺:fibra como
osciladores §15.3A; también Tm³⁺, Ho³⁺). Los $4f$ están apantallados por $5s$ y $5p$ →
niveles casi independientes del host.

- **Fig. 13.1-9** (p. 495): Nd³⁺:YAG y Nd³⁺:vidrio; transición $^4F_{3/2}\to{}^4I_{11/2}$
  a **1.064 µm** (YAG) y **1.053 µm** (vidrio de fosfato); nivel base $^4I_{9/2}$.

*Actínidos* (p. 496): llenan el $5f$ dentro del $7s^2$; láseres como U³⁺:CaF₂, limitados
por radiactividad.

**Semiconductores** (pp. 496–499; más en cap. 16).

*Masivos (bulk)*: GaAs, estructura **zincblenda** (dos redes fcc, una de Ga y otra de As,
desplazadas ¼ de la diagonal del cubo; 4 moléculas por celda convencional; cada átomo
rodeado por 4 del otro tipo en tetraedro). $E_g = 1.42$ eV a temperatura ambiente.
Niveles de core Ga y As ($3d$) agudos; banda de valencia formada por $4s$ y $4p$.
- **Fig. 13.1-10** (p. 496): bandas de GaAs (cero en el tope de la valencia; conducción
  arriba de $E_g$; core levels Ga ≈ −20 eV, As ≈ −40 eV) y celda zincblenda.

*Pozos cuánticos* (p. 497): epitaxia de haces moleculares / fase vapor; **estructura de
pozos cuánticos múltiples**: capas ultradelgadas de GaAs (2–15 nm) alternadas con AlGaAs
(20 nm) de mayor bandgap; niveles discretos para el movimiento perpendicular a la capa
(pozo cuadrado, Ejercicio 16.1-5). Si las barreras son ultradelgadas (< 1 nm) hay
tunelamiento → **minibandas** → **superred** (superlattice).
- **Fig. 13.1-11** (p. 497): bandas de conducción y valencia de una estructura
  AlGaAs/GaAs multipozo con anchos arbitrarios, 0–120 nm.

*Hilos cuánticos* (p. 497): confinamiento en dos direcciones laterales (InP, CdSe);
**nanotubos de carbono** (diámetro 1–varios nm) se comportan como semiconductores o
metales según su estructura.

*Puntos cuánticos* (pp. 498–499): nanocristales/cajas cuánticas de 1–10 nm (hasta µm);
"**átomos artificiales**" (niveles agudos de los excitones confinados); un cubo de GaAs de
10 nm tiene ≈ 40 000 átomos. Niveles fuertemente dependientes del tamaño: CdSe emite en
rojo con 5 nm de diámetro y en violeta con 1.5 nm; InP en IR cercano; InAs en
1300–1600 nm (ventana de telecom); Si fotoexcitado emite de IR a visible. Variantes:
core–shell, quantum-well–quantum dots, sólidos de puntos cuánticos, superredes de
nanocristales. Aplicaciones: láseres, LEDs, fuentes de fotón único, detectores, celdas
solares, pantallas, absorbedores UV, etiquetas biológicas.
- **Fig. 13.1-12** (p. 498): fotoluminiscencia de puntos cuánticos coloidales de CdSe en
  n-hexano excitados a $\lambda_o = 365$ nm; color sintonizado por tamaño.

### 13.2 Occupation of Energy Levels (p. 499)

La temperatura determina el comportamiento promedio y las fluctuaciones de la ocupación
(p. 499).

#### 13.2A Boltzmann Distribution (p. 499)

Objetos distinguibles (gas diluido) en equilibrio térmico con un baño a $T$:

$$P(E_m) \propto \exp(-E_m/kT), \qquad m = 1,2,3,\dots \qquad (13.2\text{-}1)$$

normalizada con $\sum_m P(E_m) = 1$. Origen: muchas entidades idénticas que comparten una
energía total fija y divisiones igualmente probables; para dos entidades independientes,
$P(E_1)P(E_2)$ debe ser función de $E_1+E_2$ → exponencial; la energía de equipartición
$kT$ para dos grados de libertad de un modo armónico da directamente Boltzmann (p. 500).

- **Fig. 13.2-1** (p. 499): niveles $E_1, E_2, \dots, E_m$ y ocupación decreciente
  exponencial.

Para $N$ átomos con $N_m$ en el nivel $m$, $N_m/N \approx P(E_m)$; **razón de poblaciones**
(p. 500):

$$\frac{N_2}{N_1} = \exp\!\left(-\frac{E_2-E_1}{kT}\right) \qquad (13.2\text{-}2)$$

A $T=0$ K todo en el estado base; en equilibrio el nivel inferior siempre está más poblado.
Fuera del equilibrio puede haber **inversión de población** (base del láser, caps. 14–15).
Con **degeneraciones** $g_1, g_2$ (número de estados por nivel):

$$\frac{N_2}{N_1} = \frac{g_2}{g_1}\exp\!\left(-\frac{E_2-E_1}{kT}\right) \qquad (13.2\text{-}3)$$

#### 13.2B Fermi–Dirac Distribution (p. 500)

Sistemas con funciones de onda solapadas (átomos multielectrónicos, semiconductores):
Pauli → cada estado con 0 o 1 electrón. Probabilidad de ocupación de un estado de energía
$E$ (**función de Fermi**):

$$f(E) = \frac{1}{\exp[(E-E_f)/kT] + 1} \qquad (13.2\text{-}4)$$

$E_f$ = **energía de Fermi**; $f(E)\le1$, decrece monótonamente, $f(E_f) = \tfrac12$.
$f(E)$ no es densidad de probabilidad ni distribución acumulada, sino una secuencia de
probabilidades (p. 501). Para $E \gg E_f$ (y $E\gg kT$) se reduce a Boltzmann:

$$P(E) \propto \exp(-E/kT) \qquad (13.2\text{-}5)$$

Por eso los niveles de transiciones ópticas (electrones externos, $E\gg E_f$) se tratan con
Boltzmann (p. 501).

- **Fig. 13.2-2** (p. 501): comparación de $f(E)$ (Fermi–Dirac) con $P(E_m)$ (Boltzmann)
  para $E \gg E_f$.

### 13.3 Interactions of Photons with Atoms (p. 501)

#### 13.3A Interaction of Single-Mode Light with an Atom (p. 501)

Átomo con niveles $E_1, E_2$ en un resonador de volumen $V$; modo de radiación *prescrito*
de frecuencia $\nu \approx \nu_0$ con $h\nu_0 = E_2 - E_1$. Los resultados vienen de la
electrodinámica cuántica y se presentan sin demostración. Tres interacciones: emisión
espontánea, absorción, emisión estimulada (p. 501).

**Emisión espontánea** (pp. 501–502). Decaimiento 2→1 con emisión de un fotón $h\nu$ al
modo, independiente del número de fotones ya presentes. Densidad de probabilidad (por
segundo), **en recuadro**:

$$p_{sp} = \frac{c}{V}\,\sigma(\nu) \qquad (13.3\text{-}1)\quad
\text{(Spontaneous Emission into a Prescribed Mode)}$$

$\sigma(\nu)$ = **sección eficaz de transición** (unidades de área, cm² en el libro),
centrada en $\nu_0$; usualmente se mide experimentalmente. Depende del ángulo $\theta$
entre el dipolo del átomo y el campo del modo:

$$\sigma = \sigma_{\max}\cos^2\theta \qquad (13.3\text{-}2)$$

"Densidad de probabilidad": probabilidad de emisión en $[t, t+\Delta t]$ es
$p_{sp}\Delta t$ ($p_{sp}$ puede superar 1 s⁻¹, pero $p_{sp}\Delta t<1$). Para $N$ átomos,
$dN/dt = -p_{sp}N$ → $N(t) = N(0)\exp(-p_{sp}t)$ (p. 502).
- **Fig. 13.3-1** (p. 502): diagrama de emisión espontánea. **Fig. 13.3-2**: decaimiento
  exponencial de $N(t)$ con constante $1/p_{sp}$.

**Absorción** (p. 503). Solo si el modo contiene un fotón (proceso **inducido**). Misma ley:

$$p_{ab} = \frac{c}{V}\,\sigma(\nu) \qquad (13.3\text{-}3)$$

Con $n$ fotones en el modo (eventos mutuamente excluyentes), **en recuadro**:

$$P_{ab} = n\,\frac{c}{V}\,\sigma(\nu) \qquad (13.3\text{-}4)\quad
\text{(Absorption of One Photon from a Mode with } n \text{ Photons)}$$

- **Fig. 13.3-3** (p. 503): absorción 1→2.

**Emisión estimulada** (pp. 503–504). Átomo en nivel superior + fotón en el modo → emisión
de un fotón "clon" (misma frecuencia, dirección, polarización); inverso de la absorción;
base de la amplificación láser.

$$p_{st} = \frac{c}{V}\,\sigma(\nu) \qquad (13.3\text{-}5)$$

$$P_{st} = n\,\frac{c}{V}\,\sigma(\nu) \qquad (13.3\text{-}6)\quad
\text{(Stimulated Emission of One Photon into a Mode with } n \text{ Photons)}$$

Como $P_{st} = P_{ab}$, se usa la notación común $W_i$. Total emisión (espontánea +
estimulada): $p_{sp} + P_{st} = (n+1)(c/V)\sigma(\nu)$; desde la QED la emisión espontánea
es emisión estimulada por las fluctuaciones de punto cero del modo (§12.1A), que no
aplican a la absorción (∝ $n$, no $n+1$) (p. 504).
- **Fig. 13.3-4** (p. 503): emisión estimulada.

**Función de forma de línea** (pp. 504–505). Área de la sección eficaz:

$$S = \int_0^\infty \sigma(\nu)\,d\nu \qquad (13.3\text{-}7)$$

(unidades cm²·Hz) = **fuerza de transición** o **fuerza de oscilador**. **Función de forma
de línea** (lineshape) normalizada $g(\nu) = \sigma(\nu)/S$, unidades Hz⁻¹,
$\int_0^\infty g(\nu)\,d\nu = 1$:

$$\sigma(\nu) = S\,g(\nu) \qquad (13.3\text{-}8)$$

**Ancho de línea** $\Delta\nu$ = FWHM de $g(\nu)$; como su área es 1:

$$\Delta\nu \propto 1/g(\nu_0) \qquad (13.3\text{-}9)$$

Sección eficaz pico $\sigma_0 = \sigma(\nu_0)$. $\sigma(\nu)$ queda caracterizada por
altura $\sigma_0$, ancho $\Delta\nu$, área $S$ y perfil $g(\nu)$.
- **Fig. 13.3-5** (p. 505): $\sigma(\nu)$ (área $S$, altura $\sigma_0$, ancho $\Delta\nu$)
  y $g(\nu)$ (área 1).

#### 13.3B Spontaneous Emission (p. 505)

**Emisión espontánea total en todos los modos.** Densidad de modos de una cavidad 3D
(10.3-10): $M(\nu) = 8\pi\nu^2/c^3$ (modos por unidad de volumen y de ancho de banda). Un
átomo emite *un* fotón en *cualquiera* de los modos con $\nu\approx\nu_0$ (Fig. 13.3-6,
p. 505). Promedio sobre direcciones isótropas (dos polarizaciones) con
$\langle\cos^2\theta\rangle = \tfrac13$:

$$\bar\sigma(\nu) = \tfrac13\,\sigma_{\max} \qquad (13.3\text{-}10)$$

$$P_{sp} = \int_0^\infty \left[\frac{c}{V}\bar\sigma(\nu)\right][V M(\nu)]\,d\nu
= c\int_0^\infty \bar\sigma(\nu)\,M(\nu)\,d\nu \qquad (13.3\text{-}11)$$

Como $\bar\sigma$ es estrecha frente a $M(\nu)$, $M(\nu)\approx M(\nu_0)$ sale de la
integral (p. 506):

$$P_{sp} = M(\nu_0)\,c\,\bar S = \frac{8\pi\bar S}{\lambda^2} \qquad (13.3\text{-}12)$$

con $\lambda = c/\nu_0$ en el medio y $\bar S = \int_0^\infty\bar\sigma(\nu)\,d\nu$.
Definiendo la **vida media espontánea** $t_{sp}$ de la transición 2→1 por
$1/t_{sp} \equiv P_{sp} = M(\nu_0)c\bar S$, **en recuadro**:

$$P_{sp} = \frac{1}{t_{sp}} \qquad (13.3\text{-}13)\quad
\text{(Spontaneous Emission of One Photon into Any Mode)}$$

independiente de $V$. Entonces

$$\bar S = \frac{\lambda^2}{8\pi t_{sp}} \qquad (13.3\text{-}14)$$

permite obtener la fuerza de transición de una medida de $t_{sp}$ (el cálculo analítico de
$\bar S$ requiere conocimiento cuántico detallado). Típicamente $t_{sp}\approx10^{-8}$ s
(primer excitado de H), pero va de sub-ps a minutos (p. 506).

> **Ejercicio 13.3-1** (p. 506) *Frequency of Spontaneously Emitted Photons.* Mostrar
> que la densidad de probabilidad de emitir un fotón entre $\nu$ y $\nu+d\nu$ es
> $P_{sp}(\nu)\,d\nu = (1/t_{sp})\,g(\nu)\,d\nu$, y explicar por qué el espectro de la
> emisión espontánea es proporcional a $g(\nu)$ tras muchos fotones emitidos.

**Relación sección eficaz – vida media** (p. 506). Con (13.3-14) y
$\bar\sigma(\nu) = \bar S g(\nu)$, **en recuadro**:

$$\bar\sigma(\nu) = \frac{\lambda^2}{8\pi t_{sp}}\,g(\nu) \qquad (13.3\text{-}15)\quad
\text{(Average Transition Cross Section)}$$

$$\bar\sigma_0 \equiv \bar\sigma(\nu_0) = \frac{\lambda^2}{8\pi t_{sp}}\,g(\nu_0) \qquad (13.3\text{-}16)$$

Como $g(\nu_0)\propto1/\Delta\nu$, $\bar\sigma_0 \propto 1/\Delta\nu$ para $t_{sp}$ dado.
Para la emisión estimulada en un modo particular valen las mismas relaciones con un
$t_{sp}$ efectivo reducido por (13.3-2) y (13.3-10); el libro no distingue en adelante
(p. 507).

#### 13.3C Stimulated Emission and Absorption (p. 507)

**Transiciones inducidas por luz monocromática.** Luz de frecuencia $\nu$, intensidad $I$,
**densidad de flujo de fotones** media (fotones/cm²·s):

$$\phi = \frac{I}{h\nu} \qquad (13.3\text{-}17)$$

Cilindro de base $A$ y altura $c$ ($V = cA$) paralelo a $\mathbf k$: flujo
$\Phi = \phi A$ fotones/s; contiene $n = \phi A = \phi V/c$ fotones:

$$\phi = n\,\frac{c}{V} \qquad (13.3\text{-}18)$$

Sustituyendo en (13.3-4), **en recuadro**:

$$W_i = \phi\,\sigma(\nu) \qquad (13.3\text{-}19)$$

Interpretación: $\sigma(\nu)$ es el área efectiva con que el átomo "captura" el flujo de
fotones para absorción o emisión estimulada. La emisión espontánea se refuerza por los
muchos modos disponibles; la estimulada por los muchos fotones en pocos modos (p. 507).

**Transiciones inducidas por luz de banda ancha** (pp. 507–508). Cavidad $V$ con luz
multimodo de densidad espectral de energía $\varrho(\nu)$ (energía por unidad de ancho de
banda y de volumen), ancha frente a la línea atómica. Fotones en $[\nu,\nu+d\nu]$:
$\varrho(\nu)V\,d\nu/h\nu$, cada uno con probabilidad $(c/V)\sigma(\nu)$:

$$W_i = \int_0^\infty \frac{\varrho(\nu)V}{h\nu}\left[\frac{c}{V}\sigma(\nu)\right]d\nu
\qquad (13.3\text{-}20)$$

$$W_i = \frac{\varrho(\nu_0)}{h\nu_0}\,c\int_0^\infty\sigma(\nu)\,d\nu
= \frac{\varrho(\nu_0)}{h\nu_0}\,cS \qquad (13.3\text{-}21)$$

Con (13.3-14):

$$W_i = \frac{\lambda^3}{8\pi h t_{sp}}\,\varrho(\nu_0) \qquad (13.3\text{-}22)$$

($\lambda = c/\nu_0$ en el medio). Definiendo el **número medio de fotones por modo**

$$\bar n = \frac{\lambda^3}{8\pi h}\,\varrho(\nu_0) \qquad (13.3\text{-}23)$$

**en recuadro**:

$$W_i = \frac{\bar n}{t_{sp}} \qquad (13.3\text{-}24)$$

Justificación de $\bar n$:

$$\frac{W_i}{P_{sp}} = \frac{\lambda^3\varrho(\nu_0)}{8\pi h t_{sp}}\,\frac{1}{M(\nu_0)cS}
= \frac{\varrho(\nu_0)}{h\nu_0 M(\nu_0)} \qquad (13.3\text{-}25)$$

$\varrho(\nu_0)/h\nu_0$ = fotones por unidad de volumen; $M(\nu_0)$ = modos por unidad de
volumen → $W_i$ es $\bar n$ veces $P_{sp}$ (p. 508).

**Coeficientes de Einstein** (pp. 508–509). Einstein, con radiación de banda ancha en
equilibrio térmico, postuló (**en recuadro**):

$$P_{sp} = \mathbb A \qquad (13.3\text{-}26)$$
$$W_i = \mathbb B\,\varrho(\nu_0) \qquad (13.3\text{-}27)\quad\text{(Einstein's Postulates)}$$

Comparando con (13.3-13) y (13.3-22), **en recuadro**:

$$\mathbb A = \frac{1}{t_{sp}} \qquad (13.3\text{-}28)$$
$$\mathbb B = \frac{\lambda^3}{8\pi h t_{sp}} \qquad (13.3\text{-}29)$$

$$\frac{\mathbb B}{\mathbb A} = \frac{\lambda^3}{8\pi h} \qquad (13.3\text{-}30)$$

La relación A–B resulta de las leyes microscópicas de interacción átomo–modo; en §13.4 se
hace un análisis tipo Einstein.

> **Ejemplo 13.3-1** (p. 509) *Comparison Between Rates of Spontaneous and Stimulated
> Emission.* Tasa espontánea constante $\mathbb A = 1/t_{sp}$; estimulada
> $\mathbb B\varrho(\nu_0)$. Son iguales cuando $\varrho(\nu_0) = \mathbb A/\mathbb B =
> 8\pi h/\lambda^3$. Para $\lambda = 1$ µm: $\mathbb A/\mathbb B = 1.66\times10^{-14}$
> J/m³·Hz, i.e. densidad espectral de intensidad $c\varrho(\nu_0) \approx 5\times10^{-6}$
> W/m²·Hz en el vacío; con $\Delta\nu = 10^7$ Hz, la intensidad a la que ambas tasas se
> igualan es **50 W/m² = 5 mW/cm²**.

**Resumen del libro (recuadro gris, pp. 509–510).** Una transición se caracteriza por
$\nu_0 = (E_2-E_1)/h$, $t_{sp}$ y $g(\nu)$ de ancho $\Delta\nu$; sección eficaz media
$\bar\sigma(\nu) = \bar S g(\nu) = (\lambda^2/8\pi t_{sp})g(\nu)$ (13.3-15).
- *Emisión espontánea:* en un modo prescrito $p_{sp} = (c/V)\sigma(\nu)$ (13.3-1); en
  cualquier modo $P_{sp} = 8\pi\bar S/\lambda^2 = 1/t_{sp}$ (13.3-13); en modos entre
  $\nu$ y $\nu+d\nu$: $P_{sp}\,d\nu = (1/t_{sp})g(\nu)\,d\nu$.
- *Emisión estimulada y absorción:* modo con $n$ fotones $W_i = n(c/V)\sigma(\nu)$
  (13.3-6); haz monocromático $W_i = \phi\sigma(\nu)$ (13.3-19); luz policromática pero
  **estrecha** frente a la línea, con densidad espectral de flujo $\phi_\nu$:
  $$W_i = \int\phi_\nu\,\sigma(\nu)\,d\nu \qquad (13.3\text{-}31)$$
  luz de **banda ancha** $W_i = \mathbb B\varrho(\nu_0)$ (13.3-27) con
  $\mathbb B = \lambda^3/8\pi h t_{sp}$.
- En todas: $c = c_o/n$, $\lambda = \lambda_o/n$, $n$ índice de refracción del medio.

#### 13.3D Line Broadening (p. 511)

La misma $g(\nu)$ aplica a emisión espontánea, absorción y emisión estimulada.

**Ensanchamiento por vida media (lifetime broadening)** (pp. 511–512). Cada nivel tiene vida
media $\tau$ (inverso de la tasa total de decaimiento, radiativo + no radiativo, a todos los
niveles inferiores). $\tau_2$ del nivel 2: $1/\tau_2 \ge 1/t_{sp}$ (i.e. $\tau_2\le t_{sp}$);
si 1 es el estado base, $\tau_1 = \infty$. Es un efecto de transformada de Fourier
(Apéndice A.1): la TF de $e^{-t/2\tau}e^{j2\pi\nu_0 t}$ (energía $\propto e^{-t/\tau}$) es
$\propto 1/[1 + j4\pi(\nu-\nu_0)\tau]$, lorentziana con FWHM $\Delta\nu = 1/2\pi\tau$;
incertidumbre de energía $\Delta E = h\Delta\nu = h/2\pi\tau$ (oscilador armónico
amortiguado, Lorentz §5.5C). Para la transición:

$$\Delta E = \Delta E_1 + \Delta E_2 = \frac{h}{2\pi}\left(\frac1{\tau_1}+\frac1{\tau_2}\right)
= \frac{h}{2\pi}\,\frac1\tau \qquad (13.3\text{-}32)$$

con $\tau^{-1} = \tau_1^{-1}+\tau_2^{-1}$. **En recuadro**:

$$\Delta\nu = \frac{1}{2\pi}\left(\frac1{\tau_1}+\frac1{\tau_2}\right) \qquad (13.3\text{-}33)
\quad\text{(Lifetime-Broadening Linewidth)}$$

$$g(\nu) = \frac{\Delta\nu/2\pi}{(\nu-\nu_0)^2 + (\Delta\nu/2)^2} \qquad (13.3\text{-}34)
\quad\text{(Lorentzian Lineshape Function)}$$

Modelo: cada fotón emitido es un paquete de ondas de frecuencia central $\nu_0$ y
envolvente con tiempo de decaimiento $2\tau$, emitidos a tiempos aleatorios → luz
parcialmente coherente (Ejemplo 11.1-1) con espectro lorentziano de ancho
$\Delta\nu = 1/2\pi\tau$ (**Fig. 13.3-7**, p. 512).

Como $g(\nu_0) = 2/\pi\Delta\nu$, la sección eficaz pico (13.3-16) queda, **en recuadro**:

$$\bar\sigma_0 = \frac{\lambda^2}{2\pi}\,\frac{1}{2\pi t_{sp}\Delta\nu} \qquad (13.3\text{-}35)$$

Máxima cuando el decaimiento es totalmente radiativo ($\tau_2 = t_{sp}$, $1/\tau_1 = 0$):
$\Delta\nu = 1/2\pi t_{sp}$ y

$$\bar\sigma_0 = \frac{\lambda^2}{2\pi} \qquad (13.3\text{-}36)$$

(del orden de una longitud de onda al cuadrado). Para $\lambda = 0.1$–10 µm,
$\lambda^2/2\pi \approx 10^{-11}$–$10^{-7}$ cm²; valores observados de $\sigma_0$ caen en
$10^{-20}$–$10^{-11}$ cm² (Tabla 14.3-1) porque $\Delta\nu \gg 1/t_{sp}$ (p. 512).

**Ensanchamiento por colisiones** (pp. 512–513). Colisiones **inelásticas** (intercambio
de energía) cambian tasas y vidas medias. Colisiones **elásticas** imparten saltos de
fase aleatorios al campo radiado (**Fig. 13.3-8**, p. 513); el espectro es de nuevo
lorentziano con $\Delta\nu = f_{col}/\pi$, $f_{col}$ = tasa de colisiones (Siegman,
*Lasers*, §3.2). Lorentziana combinada, **en recuadro**:

$$\Delta\nu = \frac{1}{2\pi}\left(\frac1{\tau_1}+\frac1{\tau_2}+2f_{col}\right) \qquad (13.3\text{-}37)$$

**Ensanchamiento inhomogéneo** (pp. 513–515). Vida media y colisiones son
**homogéneos** (todos los átomos idénticos, misma $g(\nu)$). Si los átomos tienen
distintas formas de línea o frecuencias centrales (parámetro $\beta$):

$$\bar g(\nu) = \langle g_\beta(\nu)\rangle \qquad (13.3\text{-}38)$$

promedio ponderado por la fracción de átomos con cada $\beta$ (**Fig. 13.3-9**, p. 513).

*Ensanchamiento Doppler*: átomo con velocidad $v$ → frecuencia observada desplazada
$\pm(v/c)\nu_0$ (+ si se acerca); en general $\pm(v_\parallel/c)\nu_0$ (**Fig. 13.3-10**,
p. 514). Con $p(v)\,dv$ la probabilidad de velocidad en $[v, v+dv]$:

$$\bar g(\nu) = \int_{-\infty}^{\infty} g\!\left(\nu - \nu_0\frac{v}{c}\right) p(v)\,dv
\qquad (13.3\text{-}39)$$

(**Fig. 13.3-11**, p. 514: $p(v)$ gaussiana y $\bar g(\nu)$ como envolvente de
lorentzianas desplazadas $\nu_0 v/c$).

> **Ejercicio 13.3-2** (pp. 514–515) *Doppler-Broadened Lineshape Function.*
> (a) Velocidad con densidad gaussiana
> $$p(v) = \frac{1}{\sqrt{2\pi}\,\sigma_v}\exp\!\left(-\frac{v^2}{2\sigma_v^2}\right),
> \qquad \sigma_v^2 = \frac{kT}{M} \qquad (13.3\text{-}40)$$
> ($M$ masa atómica); cada átomo lorentziano natural de ancho $\Delta\nu$ centrado en
> $\nu_0$: hallar $\bar g(\nu)$.
> (b) Si $\Delta\nu \ll \nu_0\sigma_v/c$, aproximar por la gaussiana
> $$\bar g(\nu) = \frac{1}{\sqrt{2\pi}\,\sigma_D}\exp\!\left[-\frac{(\nu-\nu_0)^2}{2\sigma_D^2}\right]
> \qquad (13.3\text{-}41)$$
> $$\sigma_D = \nu_0\frac{\sigma_v}{c} = \frac1\lambda\sqrt{\frac{kT}{M}} \qquad (13.3\text{-}42)$$
> con **ancho Doppler** FWHM
> $$\Delta\nu_D = \sqrt{8\ln2}\,\sigma_D \approx 2.35\,\sigma_D \qquad (13.3\text{-}43)$$
> (c) Calcular $\Delta\nu_D$ para la transición de Ne a $\lambda_o = 632.8$ nm y la de
> CO₂ a 10.6 µm a temperatura ambiente (láseres He–Ne y CO₂).
> (d) Mostrar que el máximo de la sección eficaz con la gaussiana (13.3-41) es
> $$\sigma_0 = \frac{\lambda^2}{8\pi}\sqrt{\frac{4\ln2}{\pi}}\,\frac{1}{t_{sp}\Delta\nu_D}
> \approx 0.94\,\frac{\lambda^2}{8\pi}\,\frac{1}{t_{sp}\Delta\nu_D} \qquad (13.3\text{-}44)$$
> y comparar con (13.3-35).

Ensanchamiento mixto homogéneo/inhomogéneo → perfil de **Voigt** (p. 515).

#### *13.3E Enhanced Spontaneous Emission (p. 515)

Todo lo anterior supone $\Delta\nu \gg \delta\nu$ (línea atómica mucho más ancha que el
modo EM). En el límite opuesto, $\Delta\nu \ll \delta\nu$ (microcavidades de alto $Q$),
la emisión espontánea se **realza** (útil para fuentes de fotones, §17.4). Modo de cavidad
con forma lorentziana normalizada $\rho(\nu)$ centrada en $\nu_q$, ancho
$\delta\nu = \nu_q/Q$, altura $2Q/\pi\nu_q$; átomo con $g(\nu)$ centrada en $\nu_0 = \nu_q$
(**Fig. 13.3-12**, p. 515). Con dipolo alineado al campo:

$$P_{sp}^{\max} = \int_0^\infty\frac{c}{V}\sigma_{\max}(\nu)\rho(\nu)\,d\nu
\approx \frac{c}{V}\frac{3\lambda^2}{8\pi t_{sp}}\rho(\nu_0)\int_0^\infty g(\nu)\,d\nu
\qquad (13.3\text{-}45)$$

(usando $\sigma_{\max} = 3\bar\sigma$ (13.3-10) y $\bar\sigma = \lambda^2g/8\pi t_{sp}$
(13.3-15)):

$$P_{sp}^{\max} = \frac{1}{t_{sp}}\,\frac{3c\lambda^2}{8\pi V}\,\frac{2Q}{\pi\nu_q}
= \frac{1}{t_{sp}}\cdot\frac{3}{4\pi^2}\,\frac{\lambda^3}{V}\,Q \qquad (13.3\text{-}46)$$

**Factor de Purcell**, **en recuadro**:

$$\frac{P_{sp}^{\max}}{P_{sp}} = \frac{3}{4\pi^2}\,\frac{\lambda^3}{V}\,Q \qquad (13.3\text{-}47)$$

Rasgos (p. 516): el 3 viene de la alineación dipolo–campo; $\lambda^3/V$ es grande en
microcavidades; $Q$ alto realza, pero al crecer $Q$ baja $\delta\nu = \nu_q/Q$ y
eventualmente se viola $\Delta\nu\ll\delta\nu$. Si $\nu_0$ se aleja de $\nu_q$, la emisión
espontánea se **suprime**.

#### *13.3F Laser Cooling and Trapping of Atoms (p. 516)

**Enfriamiento láser** (frenar átomos neutros) y **atrapamiento** (confinarlos). Átomos
ultrafríos: relojes atómicos, **óptica atómica** (manipulación de **ondas de materia**:
reflexión, refracción, difracción, interferencia, dispersión; interferometría de ondas de
materia para gravimetría), **condensados de Bose–Einstein**. Esquema básico (pp. 516–517):
láser de línea estrecha sintonizado ligeramente por debajo del centro de línea, haz de
átomos que se mueve hacia el láser; se absorben los fotones cuyo Doppler los pone en
resonancia; si el retorno es por emisión estimulada no hay cambio neto de momento; si es
por emisión espontánea (dirección aleatoria) hay pérdida neta de momento en la dirección
del láser → disminuye la velocidad; se barre la frecuencia para compensar la salida de
resonancia (**Fig. 13.3-13**, p. 517: distribución de velocidades antes y después).
Múltiples haces → trampa óptica; temperaturas de µK (velocidades ~cm/s); "evaporative
cooling" (bajar la profundidad de la trampa) y "subrecoil cooling" (estadística de Lévy)
(p. 517).

### 13.4 Thermal Light (p. 517)

Luz **térmica** emitida por cuerpos negros (absorben toda la luz incidente) en equilibrio
térmico sin otras fuentes externas.

#### 13.4A Thermal Equilibrium Between Photons and Atoms (p. 517)

Ecuaciones de tasas macroscópicas (basadas en (13.3-13) y (13.3-24)). Cavidad de volumen
unidad a temperatura $T$, paredes con átomos de dos niveles separados $h\nu$; $N_1(t)$,
$N_2(t)$ átomos por unidad de volumen en cada nivel; $\bar n$ fotones por modo dentro de
la línea (p. 518).

Solo emisión espontánea: en $\Delta t$ emiten $N_2\Delta t/t_{sp}$ átomos:

$$\frac{dN_2}{dt} = -\frac{N_2}{t_{sp}} \qquad (13.4\text{-}1)$$

$N_2(t) = N_2(0)\exp(-t/t_{sp})$ (**Fig. 13.4-1**, p. 518).

Absorción (por (13.3-24)):

$$\frac{dN_2}{dt} = N_1W_i = \frac{\bar n N_1}{t_{sp}} \qquad (13.4\text{-}2)$$

Emisión estimulada:

$$\frac{dN_2}{dt} = -N_2W_i = -\frac{\bar n N_2}{t_{sp}} \qquad (13.4\text{-}3)$$

**Ecuación de tasas**, **en recuadro** (p. 519):

$$\frac{dN_2}{dt} = -\frac{N_2}{t_{sp}} + \frac{\bar nN_1}{t_{sp}} - \frac{\bar nN_2}{t_{sp}}
\qquad (13.4\text{-}4)\quad\text{(Rate Equation)}$$

(ignora otras transiciones, procesos no radiativos y bombeo externo). Estado estacionario
$dN_2/dt = 0$:

$$\frac{N_2}{N_1} = \frac{\bar n}{1+\bar n} \qquad (13.4\text{-}5)$$

($N_2/N_1\le1$). Con Boltzmann (13.2-2):

$$\frac{N_2}{N_1} = \exp\!\left(-\frac{E_2-E_1}{kT}\right) = \exp\!\left(-\frac{h\nu}{kT}\right)
\qquad (13.4\text{-}6)$$

→ **número medio de fotones por modo** cerca de $\nu$:

$$\bar n = \frac{1}{\exp(h\nu/kT)-1} \qquad (13.4\text{-}7)$$

Aunque se dedujo con dos niveles, aplica a todas las $\nu$ si las paredes son sólidos con
un continuo de niveles. (13.4-7) es idéntica a (12.2-21) (luz térmica con ocupación
$p(n)\propto\exp(-nh\nu/kT)$): autoconsistencia; los fotones en equilibrio con átomos a
$T$ están a la misma $T$ → "gas de fotones" (§12.2C) (p. 519).

#### 13.4B Blackbody Radiation Spectrum (p. 519)

Energía media de un modo $\bar E = \bar n h\nu$, **en recuadro**:

$$\bar E = \frac{h\nu}{\exp(h\nu/kT)-1} \qquad (13.4\text{-}8)\quad
\text{(Average Energy of a Mode in Thermal Equilibrium)}$$

(idéntica a (12.2-24); **Fig. 13.4-2**, p. 520, semilogarítmica: $\bar E\to kT$ para
$\nu\ll kT/h$ y cae a cero para $\nu\gg kT/h$; a $T = 300$ K, $kT/h = 6.25$ THz ↔ 48 µm).
Multiplicando por $M(\nu) = 8\pi\nu^2/c^3$ (10.3-10), $\varrho(\nu) = M(\nu)\bar E$,
**en recuadro**:

$$\varrho(\nu) = \frac{8\pi h\nu^3}{c^3}\,\frac{1}{\exp(h\nu/kT)-1} \qquad (13.4\text{-}9)
\quad\text{(Spectral Energy Density for Blackbody Radiation)}$$

= **espectro de radiación de cuerpo negro** (energía por unidad de ancho de banda y de
volumen). Potencia total radiada $\propto T^4$ (**ley de Stefan–Boltzmann**) (p. 520).
- **Fig. 13.4-3** (p. 520): $\bar E(\nu)$, $M(\nu)$ y $\varrho(\nu)$ en ejes lineales.
- **Fig. 13.4-4** (p. 520): $\varrho(\nu)$ en J·s/m³ vs $\nu$ (10¹²–10¹⁶ Hz), log-log,
  para $T = 77, 300, 1000, 6000$ K; la línea punteada une los máximos; eje superior en
  $\lambda_o$ (100–0.1 µm) con la banda visible marcada.

Historia (p. 521): clásicamente $M(\nu) = 8\pi\nu^2/c^3$ con equipartición
$\bar E = kT$ da la fórmula de **Rayleigh–Jeans** $\varrho\approx8\pi\nu^2kT/c^3$, que
diverge; Planck (1900) cuantizó la energía de cada modo → (13.4-8). Para $h\nu\ll kT$,
$\exp(h\nu/kT)\approx1+h\nu/kT$ y se recupera Rayleigh–Jeans.

> **Ejercicio 13.4-1** (p. 521) *Frequency of Maximum Blackbody Energy Density.* Mostrar
> que la frecuencia $\nu_p$ de máxima $\varrho(\nu)$ satisface $3(1-e^{-x}) = x$ con
> $x = h\nu_p/kT$; hallar $x$ aproximadamente y $\nu_p$ a $T = 300$ K.

**Termografía** (pp. 521–522). Imágenes de temperatura usando la emisión térmica propia
(13.4-9) con cámaras sensibles en la banda adecuada: objetos calientes (sol) emiten en
visible, tierra/humanos en IR medio, objetos fríos en IR lejano. Banda usual
$0.7\ \mu\mathrm m \le \lambda_o \le 300\ \mu\mathrm m$ ↔ $12\ \mathrm K \le T \le 5200$ K.
Aplicaciones: circuitos, derrames de petróleo, búsqueda y rescate, medicina (bloqueos de
flujo, tumores), incendios, astronomía/cosmología (**Fig. 13.4-5**, p. 521).

### 13.5 Luminescence and Light Scattering (p. 522)

Radiadores no térmicos = **radiadores luminiscentes**; el proceso es **luminiscencia**
(excitación por impacto electrónico, sonido, fotones…). Además la luz puede **dispersarse**
de forma resonante o no resonante; Rayleigh (lineal) y Raman (no lineal) son importantes en
fotónica (p. 522).

#### 13.5A Forms of Luminescence (p. 522)

Clasificación por fuente de excitación (**Fig. 13.5-1**, p. 523, con fotografías de cada
tipo):
- **Catodoluminiscencia** (p. 522): excitación por electrones energéticos (tubos de rayos
  catódicos, intensificadores de imagen); se usa para analizar composición variando la
  energía de los electrones (profundidad de penetración).
- **Sonoluminiscencia** (p. 522): cavitación acústica en líquidos (formación, crecimiento y
  colapso de burbujas con ultrasonido); destellos de ps al alcanzar tamaño mínimo;
  también de burbuja única estable.
- **Quimioluminiscencia** (pp. 522–523): reacción química que puebla un estado excitado de
  un producto (lightsticks; color dado por el colorante).
- **Bioluminiscencia** (p. 523): quimioluminiscencia en organismos vivos (luciérnagas,
  organismos marinos en azul, proteínas marcadoras en biología).
- **Electroluminiscencia** (p. 523): campo eléctrico aplicado; **electroluminiscencia por
  inyección** en uniones semiconductoras polarizadas en directa (LED, cap. 17):
  recombinación de electrones de conducción con huecos de valencia.
- **Fotoluminiscencia** (p. 523): emisión tras absorción de fotones ópticos (brillo tras
  exposición UV; herramienta para semiconductores); **radioluminiscencia** si los fotones
  son X o gamma.

**Fluorescencia vs. fosforescencia** (p. 524): transiciones radiativas **permitidas por
espín** (singlete→singlete, triplete→triplete) = **fluorescencia**, vidas cortas
(0.1–20 ns); transiciones **prohibidas por espín** (triplete→singlete) =
**fosforescencia**, vidas largas (1 ms–10 s). La amplificación de la fluorescencia por
emisión estimulada es la base del láser (caps. 14, 15).

#### 13.5B Photoluminescence (p. 524)

Excitación por absorción de un fotón y decaimiento espontáneo; por conservación de
energía el fotón emitido no puede tener más energía que el excitante (en un solo fotón).
Variantes (**Fig. 13.5-2**, p. 524): (a) emisión directa; (b),(c) con transiciones no
radiativas intermedias (líneas punteadas) → conversión UV→visible; almacenamiento en
trampas → luminiscencia retardada; (d) descenso no radiativo seguido de ascenso no
radiativo; "**quantum cutting**": un fotón UV → dos fotones visibles.

**Fotoluminiscencia multifotónica** (pp. 524–526). Excitación por absorción de más de un
fotón; el fotón emitido puede tener más energía que cada excitante.
- *Fluorescencia multifotónica* (**Fig. 13.5-3(a),(b)**, p. 525): dos (o tres) fotones
  de la misma energía $h\nu_1$ elevan el sistema, que emite $h\nu_2 > h\nu_1$. Base de la
  **microscopía de fluorescencia de barrido láser de dos fotones (TPLSM)**: la probabilidad
  de dos fotones en un punto es el cuadrado de la de uno (§12.2C, (12.1-14)) → tasa de
  absorción y de emisión $\propto I^2(\mathbf r,t)$; la absorción se localiza en el foco
  (mejor resolución, menos fondo), y la excitación con el doble de longitud de onda
  penetra más en tejido biológico; se usan láseres mode-locked de fs (alta potencia pico,
  baja media). Con $k$ fotones: tasa $\propto I^k(\mathbf r,t)$.
- *Microlitografía multifotónica 3D* (p. 525): polimerización localizada en el foco de
  pulsos intensos en un polímero transparente; el umbral de la no linealidad mejora la
  resolución.
- *Fluorescencia de conversión ascendente (upconversion)* (**Fig. 13.5-3(c)**,
  pp. 525–526): dos fotones de energías distintas; un fotón IR $h\nu_1$ más uno auxiliar
  $h\nu_2$ excitan un ion y se emite $h\nu_3 = h\nu_1 + h\nu_2$. Con trampas (fósforos
  dopados con Er³⁺) cargadas por luz diurna o fluorescente; **tarjeta sensora de
  infrarrojo** (≈5 cm × 5 cm) para ver haces IR (**Fig. 13.5-4**, p. 526: sensibilidad
  IR ≈ 800–1600 nm con máximo cerca de 1100–1200 nm, emisión visible ≈ 550 nm).

#### 13.5C Light Scattering (p. 526)

Fotoluminiscencia = absorción **resonante** hacia un estado real y re-emisión
(luminiscencia, fluorescencia, fosforescencia). **Dispersión de luz** = transiciones vía
**estados virtuales**, no resonantes → luz dispersada en un rango amplio de frecuencias.
Tres procesos: Rayleigh, Raman y Brillouin (**Fig. 13.5-5**, p. 527: (a) Rayleigh,
(b) Raman Stokes, (c) Raman anti-Stokes, (d) Brillouin; las líneas horizontales punteadas
son estados virtuales). La dispersión es inherente e inevitable, pero también informa sobre
materiales y permite construir fuentes (p. 526).

**Dispersión Rayleigh** (pp. 526–527): cambia la dirección del fotón conservando su
energía (elástica). Ocurre en gases, líquidos y sólidos, por variaciones del medio
(inhomogeneidades aleatorias del índice en vidrio, §9.3A) o por partículas mucho menores
que $\lambda$ (electrones, átomos, moléculas, nanopartículas). Intensidad dispersada
$\propto\nu^4\propto1/\lambda_o^4$ → el azul se dispersa más (cielo azul). Partículas
mayores que $\approx\lambda_o/10$ → **dispersión Mie**, poco dependiente de $\lambda$
(halo blanco de las luces en niebla).

**Dispersión Raman** (p. 527): el fotón $h\nu_1$ sale con menor frecuencia
$h\nu_S = h\nu_1 - h\nu_R$ (**Stokes**) o mayor $h\nu_A = h\nu_1 + h\nu_R$
(**anti-Stokes**). Inelástica: intercambio de energía $h\nu_R$ con un modo rotacional y/o
vibracional de una molécula o sólido. Stokes: el fotón cede energía al material;
anti-Stokes: la recibe. El espectro dispersado contiene la componente Rayleigh (en la
frecuencia incidente) más bandas laterales corridas al rojo (Stokes) y al azul
(anti-Stokes). La potencia de las bandas laterales es típicamente **~10⁻⁷** de la
incidente (no resonante), pero sirve para caracterizar materiales: cristales → espectro
vibracional discreto, líneas Raman estrechas; vidrios → espectros vibracionales anchos →
líneas Raman anchas. **Dispersión Brillouin** (Fig. 13.5-5(d)): igual que Raman pero el
intercambio $h\nu_B$ es con modos **acústicos** del medio.

**Dispersión Raman estimulada (SRS)** (pp. 527–528): un fotón de señal entra en un medio
óptico no lineal junto con un fotón de bombeo de mayor frecuencia; la señal estimula la
emisión de un segundo fotón de señal obtenido por corrimiento Stokes del bombeo (su
frecuencia coincide exactamente con la de la señal); el exceso de energía va a los modos
vibracionales. Parecido a la emisión estimulada, pero es un **proceso paramétrico no
lineal de tercer orden** (§21.3B; recuadro en Fig. 14.3-7).
- Aplicaciones: **amplificadores Raman** (§14.3D) y **láseres Raman** (§15.3A); su ancho de
  banda lo fija el espectro vibracional del material, no el ancho de una transición de
  emisión estimulada; el vidrio tiene espectro vibracional muy ancho → una fibra puede
  amplificar sobre **cientos de nm**; amplificadores de fibra Raman y láseres de fibra
  Raman en sistemas DWDM (§24.3C).
- Espectroscopía: SRS revela características vibracionales; sensibilidad mejorada con
  **CARS** (coherent anti-Stokes Raman scattering): dos láseres de bombeo cuya diferencia
  de frecuencias resuena con la vibración del material → mayor eficiencia de mezcla de
  ondas.
- **Supercontinuo** (p. 528): en fibras, un bombeo genera emisión Raman espontánea que se
  amplifica por SRS al propagarse; con fibra suficientemente larga y bombeo suficiente, el
  espectro Raman resultante inicia nuevas conversiones Raman en cascada → luz de banda
  ancha (supercontinuo) (§22.5C). Se estabiliza con un resonador.
- **Dispersión Brillouin estimulada (SBS)**: igual pero con vibraciones acústicas en vez
  de moleculares.

### Reading List (pp. 528–530)

Libros de física atómica, molecular y del estado sólido (Haroche & Raimond 2006; Demtröder
2005; Feynman vol. 3; Cohen-Tannoudji *Atoms in Electromagnetic Fields* 2004 y
*Atom–Photon Interactions* 1992; Foot 2004; Kittel; Lorentz 1906; Henderson & Bartram
2000; Powell 1998; Allen & Eberly 1975; Breene *Theories of Spectral Line Shape* 1981;
Herzberg; Dirac; Landau & Lifshitz; Condon & Shortley 1935; ter Haar *The Old Quantum
Theory* 1967 con traducciones de Planck, Einstein, Rutherford, Bohr), de enfriamiento y
atrapamiento láser (Letokhov 2007; Ashkin 2006; Bardou et al. 2002; Metcalf & van der
Straten 1999) y de termografía, luminiscencia y dispersión (Lakowicz *Principles of
Fluorescence Spectroscopy* 2006; Young *Sonoluminescence* 2005; Long *The Raman Effect*
2002; Damzen et al. *Stimulated Brillouin Scattering* 2002; Berne & Pecora *Dynamic Light
Scattering* 1976; Bohren & Huffman *Absorption and Scattering of Light by Small Particles*
1983). Artículos: Purcell 1946 (emisión espontánea en cavidades); Göppert-Mayer 1931
(procesos de dos cuantos); Einstein 1917 (*Zur Quantentheorie der Strahlung*); van Vleck &
Huber 1977 (absorción, emisión y anchos de línea); Weisskopf 1968; Kerker (ed.) *Selected
Papers on Light Scattering* 1988; Masters (ed.) *Multiphoton Excitation Microscopy* 2003.

---

## Tablas y datos numéricos útiles

**Tabla 13.1-1** (p. 494) — Dopantes de metales de transición y lantánidos para láseres de
estado sólido (configuraciones de subcapas llenas omitidas; en lantánidos también se
omiten $5s^25p^6$):

| Z | Elemento | Config. átomo | Término átomo | Ion | Config. ion | Término ion |
|---|---|---|---|---|---|---|
| 22 | Ti | $3d^2 4s^2$ | $^3F_2$ | Ti³⁺ | $3d^1$ | $^2D_{3/2}$ |
| 24 | Cr | $3d^5 4s^1$ | $^7S_3$ | Cr³⁺ | $3d^3$ | $^4F_{3/2}$ |
| 60 | Nd | $4f^4 6s^2$ | $^5I_4$ | Nd³⁺ | $4f^3$ | $^4I_{9/2}$ |
| 68 | Er | $4f^{12} 6s^2$ | $^3H_6$ | Er³⁺ | $4f^{11}$ | $^4I_{15/2}$ |
| 70 | Yb | $4f^{14} 6s^2$ | $^1S_0$ | Yb³⁺ | $4f^{13}$ | $^2F_{7/2}$ |

**Niveles y transiciones** (todas con página):
- H: niveles (13.1-4), ionización ≈ 13.6 eV (Fig. 13.1-1, p. 485); C⁵⁺ hidrogenoide,
  ionización ≈ 504 eV, láser 18.2 nm (n=3→2) (p. 485).
- Radio de Bohr $r_n = (4\pi\epsilon_o)n^2\hbar^2/(mZe^2)$ (p. 485).
- Corrimientos espín–órbita y relativistas ≈ $10^{-4}$ relativos; hiperfinos $10^{-7}$
  (p. 487).
- He–Ne: 3.39 µm ($2p^55s\to2p^53p$) y 632.8 nm ($2p^54s\to2p^53p$); niveles de He
  $1s2s\,^1S_0\approx20.6$ eV y $1s2s\,^3S_1\approx19.8$ eV (Fig. 13.1-2, p. 487).
- Rotacional: $\hbar\omega\sim10^{-4}$–$10^{-2}$ eV (p. 489). Vibracional:
  $\hbar\omega\sim0.05$–0.5 eV (p. 489); N₂ $\mathfrak v=1$ ≈ 0.29 eV (Fig. 13.1-4).
- CO₂: láser 10.6 µm (001→100) y 9.6 µm (001→020); nivel (001) ≈ 0.29 eV (p. 490).
- Rodamina 6G: $\mathrm{C_{28}H_{31}N_2O_3^+}$, S₀–S₁ ≈ 2.3 eV (Fig. 13.1-5, p. 491).
- Conductividades: metal $10^8$, semiconductor $10^{-4}$–$10^5$, aislante $10^{-10}$
  $(\Omega\cdot\mathrm m)^{-1}$ (Fig. 13.1-7, p. 492).
- $E_g$: Si ≈ 1.1 eV; diamante ≈ 5.5 eV; aislantes típicamente $E_g>3$ eV (p. 493);
  GaAs 1.42 eV a temperatura ambiente (p. 496).
- Rubí Cr³⁺:Al₂O₃: $n\approx1.76$, ~0.05 % Cr, láser 694 nm, uniaxial (pp. 493–494).
- Alexandrita Cr³⁺:BeAl₂O₄: $n\approx1.74$, ~0.1 % Cr₂O₃, 680 nm + sintonizable, biaxial
  (p. 494).
- Nd³⁺:YAG 1.064 µm; Nd³⁺:vidrio (fosfato) 1.053 µm ($^4F_{3/2}\to{}^4I_{11/2}$)
  (pp. 495–496).
- Pozos cuánticos GaAs 2–15 nm / AlGaAs 20 nm; barreras < 1 nm → superred (p. 497).
- Puntos cuánticos 1–10 nm; CdSe: 5 nm rojo → 1.5 nm violeta; InAs 1300–1600 nm; cubo
  GaAs de 10 nm ≈ 40 000 átomos (p. 498).

**Interacción fotón–átomo:**
- $t_{sp}\approx10^{-8}$ s para el primer excitado del H; rango sub-ps a minutos (p. 506).
- $\bar\sigma_0^{\max} = \lambda^2/2\pi \approx 10^{-11}$–$10^{-7}$ cm² para
  $\lambda = 0.1$–10 µm; valores observados $\sigma_0\sim10^{-20}$–$10^{-11}$ cm²
  (p. 512; Tabla 14.3-1).
- Ejemplo 13.3-1: a $\lambda=1$ µm, $\mathbb A/\mathbb B = 8\pi h/\lambda^3 =
  1.66\times10^{-14}$ J/m³·Hz; $c\varrho\approx5\times10^{-6}$ W/m²·Hz; con
  $\Delta\nu = 10^7$ Hz, $I = 50$ W/m² = 5 mW/cm² iguala tasas espontánea y estimulada
  (p. 509).
- Ancho Doppler: $\sigma_D = (1/\lambda)\sqrt{kT/M}$, $\Delta\nu_D = 2.35\,\sigma_D$
  (p. 515).
- Lorentziana: $g(\nu_0) = 2/\pi\Delta\nu$ (p. 512). Gaussiana: $\sigma_0\approx0.94\,
  \lambda^2/(8\pi t_{sp}\Delta\nu_D)$ (p. 515).
- Fluorescencia: 0.1–20 ns; fosforescencia: 1 ms–10 s (p. 524).

**Luz térmica:**
- $kT/h = 6.25$ THz ↔ 48 µm a $T = 300$ K (Fig. 13.4-2, p. 520).
- $M(\nu) = 8\pi\nu^2/c^3$ (p. 505, (10.3-10)).
- Termografía: $0.7\le\lambda_o\le300$ µm ↔ $12\le T\le5200$ K (p. 521).
- Potencia total $\propto T^4$ (Stefan–Boltzmann); $\int_0^\infty x^3/(e^x-1)\,dx =
  \pi^4/15$ (Problema 13.4-7, p. 531).

**Dispersión:**
- Rayleigh $\propto\nu^4\propto\lambda_o^{-4}$; Mie para tamaños $\gtrsim\lambda_o/10$
  (p. 527).
- Potencia de bandas Raman espontáneas ≈ $10^{-7}$ de la incidente (p. 527).
- Ganancia Raman en fibra de vidrio: cientos de nm de ancho de banda (p. 528).
- Tarjeta IR: sensibilidad ≈ 800–1600 nm, emisión visible ≈ 550 nm (Fig. 13.5-4, p. 526).

---

## Problemas al final del capítulo (pp. 530–531)

(La numeración salta porque los ejercicios 13.3-1, 13.3-2 y 13.4-1 están en el texto.)

- **13.3-3 Comparison of Stimulated and Spontaneous Emission.** Átomo de dos niveles con
  $\lambda_o = 0.7$ µm, $t_{sp} = 3$ ms, $\Delta\nu = 50$ GHz, lorentziana, en resonador
  de $V = 100$ cm³ y $n = 1$; dos modos (uno en $\nu_0$, otro en $\nu_0+\Delta\nu$)
  excitados con 1000 fotones cada uno. Hallar la densidad de probabilidad de emisión
  estimulada (o absorción); con $N_2$ átomos excitados, la constante de tiempo de
  decaimiento de $N_2$ por emisión estimulada *y* espontánea; cuántos fotones (en vez de
  1000) harían iguales las tasas estimulada y espontánea.
- **13.3-4 Spontaneous Emission into Prescribed Modes.** (a) Cavidad cúbica de 1 µm³ con
  $n = 1$: números de modo $(q_1,q_2,q_3)$ de los modos de menor y siguiente frecuencia
  (cap. 10); mostrar que son 260 y 367 THz. (b) Un átomo excitado en la cavidad sin
  fotones: razón $p_{sp2}/p_{sp1}$ entre la emisión en un modo de 367 THz y en el modo
  (2,1,1).
- **13.4-2 Rate Equations for Broadband Radiation.** Resonador de volumen unidad, átomos
  de dos niveles ($\nu_0$, $\Delta\nu$), $N_1$, $N_2$, $\bar n$ fotones por modo en una
  banda ancha alrededor de $\nu_0$; fotones perdidos a tasa $1/\tau_p$ por reflexión
  imperfecta; sin transiciones no radiativas. Escribir las ecuaciones de tasas para $N_2$
  y $\bar n$.
- **13.4-3 Inhibited Spontaneous Emission.** Radiador de cuerpo negro bidimensional
  (placa cuadrada de área $A$) a $T$. (a) Densidad de modos $M(\nu)$ y densidad espectral
  de energía $\varrho(\nu)$ (§10.3). (b) $P_{sp}$ para un átomo en una cavidad que solo
  permite radiación en 2D (p. ej. reflectores omnidireccionales fotónicos arriba y abajo
  de una lámina).
- **13.4-4 Comparison of Stimulated and Spontaneous Emission in Blackbody Radiation.**
  Temperatura de una cavidad de cuerpo negro para la cual las tasas estimulada y
  espontánea de los átomos de las paredes son iguales a $\lambda_o = 1$ µm.
- **13.4-5 Wien's Law.** Deducir $\varrho_\lambda(\lambda)$ (energía por unidad de volumen
  en $[\lambda,\lambda+d\lambda]$); mostrar que $\lambda_p$ de máxima densidad satisface
  $5(1-e^{-y}) = y$ con $y = hc/\lambda_pkT$ → $\lambda_pT$ = const (ley de Wien); hallar
  $\lambda_pT$ aproximadamente; mostrar que $\lambda_p\ne c/\nu_p$ (Ejercicio 13.4-1) y
  explicar.
- **13.4-6 Spectral Energy Density of One-Dimensional Blackbody Radiation.** Radiador 1D
  de longitud $L$ a $T$. (a) $M(\nu)$ en 1D. (b) Con $\bar E$, hallar y graficar
  $\varrho(\nu)$ 1D.
- **13.4-7 Stefan–Boltzmann Law.** Con (13.4-9), confirmar que la potencia total radiada
  $\propto T^4$ y hallar la constante de proporcionalidad.
  Pista: $\int_0^\infty x^3\,dx/(e^x-1) = \pi^4/15$.
- ***13.5-1 Statistics of Cathodoluminescence Light.** Haz de electrones sobre un fósforo;
  $\bar m$ electrones por unidad de área y tiempo con distribución de Poisson; fotones por
  electrón también Poisson con media $\bar G$. Hallar la distribución global $p(n)$ de los
  fotones (distribución **Neyman tipo A**), su media $\bar n$ y varianza $\sigma_n^2$.
  Pista: probabilidad condicional.

---

## Relación con Óptica No Lineal

**Para el curso (temas del programa):**

- *Absorción y dispersión / oscilador de Lorentz.* La forma de línea lorentziana (13.3-34)
  y el ensanchamiento por vida media (13.3-33) son la contraparte cuántica del oscilador
  de Lorentz (§5.5C) que se usó en los talleres 1–2 para la susceptibilidad lineal
  $\chi^{(1)}(\omega)$; el libro mismo lo señala (p. 511). La sección eficaz
  $\sigma(\nu) = S g(\nu)$ y la relación $\bar\sigma_0 = \lambda^2/2\pi$ (13.3-36) dan
  el orden de magnitud máximo de la absorción resonante por átomo, útil para
  estimar coeficientes de absorción $\alpha = N\sigma$ (Boyd §2 y cap. 6, absorción
  saturable). El ensanchamiento Doppler (13.3-41)–(13.3-43) es el ejemplo canónico de
  ensanchamiento inhomogéneo (relevante para saturación y hole burning).
- *Susceptibilidad no lineal, χ⁽²⁾ y χ⁽³⁾.* La estructura de niveles (§13.1) y los estados
  virtuales de la Fig. 13.5-5 (p. 527) son el lenguaje con que Boyd (cap. 3) construye
  $\chi^{(2)}$ y $\chi^{(3)}$ por teoría de perturbaciones: los denominadores resonantes
  son diferencias de niveles atómicos y los anchos $\Delta\nu$ (13.3-37) son las tasas de
  relajación $\gamma$. La emisión estimulada $W_i = \phi\sigma$ (13.3-19) y la ecuación
  de tasas (13.4-4) son la base del modelo de dos niveles con saturación
  ($\chi^{(3)}$ resonante, índice dependiente de la intensidad en medios con absorción
  saturable).
- *Raman (tema 10, Raman estimulado).* §13.5C (pp. 526–528) da la descripción
  fenomenológica que Boyd formaliza en cap. 10: Stokes $\nu_S = \nu_1-\nu_R$, anti-Stokes
  $\nu_A = \nu_1+\nu_R$, el intercambio con modos vibracionales/rotacionales, la
  debilidad ($\sim10^{-7}$) del proceso espontáneo, el espectro Raman ancho de los
  vidrios (clave para la ganancia Raman en sílice y en Si₃N₄), SRS como proceso
  paramétrico de tercer orden (§21.3B del propio Saleh), amplificadores y láseres Raman
  (§14.3D, §15.3A), CARS como mezcla de cuatro ondas resonante con la vibración, y la
  cascada Raman que origina el supercontinuo (§22.5C). Brillouin (acústico) y SBS siguen
  el mismo esquema con $\nu_B$ mucho menor.
- *FWM.* CARS (p. 528) y la conversión ascendente (Fig. 13.5-3(c)) ilustran procesos de
  mezcla de frecuencias; la absorción de dos fotones ($\propto I^2$, p. 525) es la parte
  imaginaria de $\chi^{(3)}$ (Boyd §4; absorción de dos fotones como límite de potencia en
  guías de Si, no en Si₃N₄).
- *Ondas EM, pulsos en medios dispersivos, GVD, SPM/solitones/XPM, propagación en fibras.*
  Apoyo indirecto: la Ec. de Schrödinger (13.1-1) es formalmente la ecuación paraxial y la
  SVEA (22.1-24), de donde sale la NLSE; la relación "espectro = TF de la envolvente"
  (lifetime broadening, pp. 511–512) es la misma herramienta de los pulsos. La fluorescencia
  de dos fotones con láseres de fs (p. 525) motiva los pulsos ultracortos.
- *Polarización y cristales.* §13.1C aporta la clasificación de sólidos (iónicos,
  covalentes, metálicos), rubí uniaxial vs. alexandrita biaxial (p. 494), y la noción de
  campo cristalino que determina la simetría de los centros activos.
- *Haz gaussiano.* Sin contenido directo; solo la geometría del "cilindro de fotones"
  (13.3-18) para pasar de intensidad a flujo de fotones $\phi = I/h\nu$.

**Para el proyecto final (anillos add-drop en Si₃N₄, dispersión de guías, supercontinuo,
sensado de índice):**

- *Supercontinuo.* El mecanismo Raman en cascada de p. 528 (bombeo → emisión Raman
  espontánea amplificada por SRS → nuevas conversiones) es uno de los ingredientes del
  supercontinuo junto con SPM/FWM/solitones; en Si₃N₄ la ganancia Raman es ancha y débil
  (vidrio amorfo, p. 527), lo que justifica que en el modelado de SC en guías cortas el
  término Raman sea secundario frente a Kerr. Citar: Saleh §13.5C, pp. 527–528 y §22.5C.
- *Anillos / microcavidades.* El factor de Purcell (13.3-47) $\propto Q\lambda^3/V$ y la
  condición $\Delta\nu\ll\delta\nu = \nu_q/Q$ (pp. 515–516) conectan el $Q$ y el volumen
  modal del anillo con el realce de procesos espontáneos (Raman espontáneo, emisión de
  dopantes como Er³⁺ en Si₃N₄). Útil si en el futuro se evalúa el anillo como fuente.
- *Pérdidas y dispersión Rayleigh.* La dispersión Rayleigh por inhomogeneidades del
  índice en vidrio (p. 526–527, §9.3A) con dependencia $\lambda^{-4}$ es el límite
  intrínseco de las pérdidas de propagación en guías de Si₃N₄ (junto con la rugosidad de
  paredes); relevante para el $Q$ intrínseco del anillo.
- *Sensado de índice (bulk).* No hay material directo; sí la distinción entre interacción
  resonante (absorción real) y no resonante (dispersión por estados virtuales, p. 526):
  un analito transparente actúa solo a través de $n$ real (sin $\sigma(\nu)$ en la banda
  de trabajo), que es la hipótesis del refractómetro de volumen.
- *Luz térmica y ruido.* $\bar n = 1/(e^{h\nu/kT}-1)$ (13.4-7) a 1550 nm y 300 K es
  $\sim10^{-14}$: el ruido térmico óptico es despreciable frente al shot noise y al ASE en
  las medidas del anillo.
- *Materiales de referencia.* Tabla 13.1-1 y Fig. 13.1-9 (Er³⁺, Yb³⁺, Nd³⁺) y
  Figs. 13.1-11/12 (pozos y puntos cuánticos, InAs 1300–1600 nm) por si el proyecto
  integra ganancia o fuentes en la banda C.
