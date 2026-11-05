# Capítulo 16 — Semiconductor Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 627–679 (PDF 649–701). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 16.
Convención del libro: dependencia temporal $e^{j\omega t}$, $j=\sqrt{-1}$; $k$ es la constante de
Boltzmann cuando aparece como $kT$ y el módulo del vector de onda $\mathbf{k}$ en las relaciones
$E$–$k$ (el libro usa el mismo símbolo; aquí se indica el sentido cuando pueda haber ambigüedad).
Unidades: el libro mezcla eV, cm⁻¹, cm⁻³ y µm en semiconductores; se transcriben tal cual y se
anotan las equivalencias SI cuando conviene. Constante de Planck reducida $\hbar = h/2\pi$;
masa del electrón libre $m_0 = 9.1\times10^{-31}$ kg; $kT = 0.026$ eV a $T = 300$ K.

---

## Resumen del capítulo

El capítulo repasa la física de semiconductores necesaria para la optoelectrónica (cap. 17, fuentes;
cap. 18, detectores) y construye una teoría simplificada de la absorción, la emisión espontánea y la
emisión estimulada por transiciones banda a banda, calcada de la teoría de transiciones atómicas de
la §13.3. La §16.1 (p. 629) cubre bandas de energía y portadores (masa efectiva, bandgap directo e
indirecto), materiales (Si, Ge, III–V binarios/ternarios/cuaternarios, II–VI, dopado, orgánicos),
concentraciones de electrones y huecos (densidad de estados $\varrho(E)\propto\sqrt{E-E_c}$, función de
Fermi, ley de acción de masas $np = n_i^2$, cuasi-niveles de Fermi), generación–recombinación e
inyección (tiempo de vida $\tau$, eficiencia cuántica interna $\eta_i$), uniones $p$–$n$ y $p$–$i$–$n$
(ecuación de Shockley), heterouniones y estructuras de confinamiento cuántico (pozos, hilos y puntos
cuánticos, con sus densidades de estados en escalera, $1/\sqrt{E}$ y deltas). La §16.2 (p. 660) trata
las interacciones fotón–portador: mecanismos de absorción (banda a banda, impureza–banda, portadores
libres, fonones, excitones), longitud de onda de bandgap $\lambda_g \approx 1.24/E_g$, conservación de
energía y momento (regla de selección $k$), densidad conjunta de estados óptica
$\varrho(\nu)\propto\sqrt{h\nu-E_g}$, probabilidades de ocupación con cuasi-niveles de Fermi, tasas de
emisión espontánea/estimulada/absorción, coeficiente de ganancia $\gamma_0(\nu)$ con el factor de
inversión de Fermi (condición de emisión neta $E_{fc}-E_{fv}>h\nu$), coeficiente de absorción en
equilibrio térmico $\alpha(\nu)\propto\sqrt{h\nu-E_g}/(h\nu)^2$, transiciones en pozos cuánticos y
superredes, y el índice de refracción de semiconductores (Kramers–Kronig, Sellmeier, Tabla 16.2-1).

---

## Secciones

### Introducción (p. 628)

- La fotónica controla fotones; la electrónica controla portadores. Ambas confluyen en la
  optoelectrónica de semiconductores: los fotones generan portadores móviles y los portadores generan
  y controlan fotones (fuentes LED/láser, amplificadores, detectores, guías, moduladores, sensores,
  elementos no lineales) (p. 628).
- Rasgos únicos del semiconductor frente a un conjunto de átomos independientes (p. 628): (i) los
  niveles pertenecen al sistema completo por la proximidad de los átomos en la red; (ii) los niveles
  densamente espaciados forman **bandas**; a $T = 0$ K la **banda de valencia** está llena y la **banda
  de conducción** vacía, separadas por la banda prohibida de energía $E_g$; (iii) una excitación
  externa (térmica, óptica o electrónica) sube un electrón a la banda de conducción dejando un
  **hueco**; la recombinación electrón–hueco libera un fotón y/o fonones.
- Dos procesos fundamentales (p. 628): (1) la absorción de un fotón crea un par electrón–hueco
  (fotodetectores fotoconductivos); (2) la recombinación de un par puede emitir un fotón: espontánea
  (LED) o estimulada (láser de diodo).
- Los capítulos 16, 17 y 18 forman una unidad (p. 628–629).

### 16.1 Semiconductors (p. 629)

Un semiconductor es un sólido cristalino o amorfo con conductividad intermedia entre metal y
aislante, modificable por temperatura, dopado o iluminación. Los dispositivos electrónicos se hacen
principalmente en Si; los optoelectrónicos usan a menudo compuestos ternarios o cuaternarios como
InGaAsP y AlInGaN (p. 629).

#### 16.1A Energy Bands and Charge Carriers (p. 629)

**Bandas de energía (p. 629–630).** La solución de la ecuación de Schrödinger para el potencial
periódico de la red divide los niveles atómicos en bandas, cada una un cuasi-continuo de niveles.
Bandas de valencia y conducción separadas por la **energía de bandgap** $E_g$: 1.12 eV (Si) y
1.42 eV (GaAs) a temperatura ambiente (Fig. 16.1-1, p. 629). El **modelo de Kronig–Penney**
(Fig. 16.1-2, p. 630) aproxima el potencial de la red por barreras rectangulares 1D de altura $V_0$ y
periodo $a$; la ecuación (13.1-3) da bandas permitidas con soluciones de onda viajera y bandas
prohibidas con soluciones que decaen exponencialmente. Es análogo a la óptica de medios periódicos 1D
(§7.2); las autofunciones son **modos de Bloch** con la periodicidad de la red [cf. (7.2-4)] (p. 630).

**Electrones y huecos (p. 630).** Por el principio de exclusión de Pauli, a $T = 0$ K la banda de
valencia (Si y Ge: 4 electrones de valencia por átomo en enlaces covalentes) está llena y la de
conducción vacía: no conduce. Al subir $T$, electrones excitados térmicamente pasan a la banda de
conducción y actúan como portadores; cada uno deja un **hueco** en la banda de valencia, que se
comporta como una carga $+e$ (Fig. 16.1-3, p. 630). La conductividad crece abruptamente con $T$.

**Relación energía–momento (p. 631).** Para un electrón libre $E = p^2/2m_0 = \hbar^2k^2/2m_0$,
$\mathbf{k} = \mathbf{p}/\hbar$: parábola. En el cristal la relación $E$–$k$ es periódica en
$(k_1,k_2,k_3)$ con periodos $(\pi/a_1,\pi/a_2,\pi/a_3)$ ($a_i$ constantes de red); el intervalo
$[-\pi/a,\pi/a]$ es la **primera zona de Brillouin**. La energía depende del módulo y de la
dirección de $\mathbf{k}$ (Fig. 16.1-4, p. 632, cortes para Si y GaAs en las direcciones [111] y
[100]). Analogía con el diagrama $\omega$–$K$ de cristales fotónicos (Fig. 7.3-5).

> **Ejercicio 16.1-1 — Relación energía–momento para un electrón libre (p. 631).**
> (a) Con la ecuación de Schrödinger 1D independiente del tiempo (13.1-3), $V=0$, masa $m_0$, y
> solución de prueba $\psi(x)\propto\exp(-jkx)$, mostrar que
> $$E = \frac{\hbar^2 k^2}{2m_0}, \qquad (16.1\text{-}1)$$
> de modo que la energía no está cuantizada. (b) El fotón libre tiene relación lineal [cf. (12.1-10)]
> $$E = pc = c\hbar k, \qquad (16.1\text{-}2)$$
> con $c$ la velocidad de la luz en el medio. ¿Cuál es el origen y significado de la diferencia?
> (Sin resultado explícito en el texto: el electrón es masivo y no relativista, el fotón no tiene masa.)

**Masa efectiva (p. 631–632).** Cerca del fondo de la banda de conducción
$$E = E_c + \frac{\hbar^2 k^2}{2m_c}, \qquad (16.1\text{-}3)$$
con $E_c$ la energía del fondo de la banda y $k$ medido desde el mínimo; $m_c$ es la **masa efectiva**
del electrón (banda de conducción), que contiene el efecto de los iones de la red. Cerca del tope de
la banda de valencia
$$E = E_v - \frac{\hbar^2 k^2}{2m_v}, \qquad (16.1\text{-}4)$$
con $E_v = E_c - E_g$ y $m_v$ la masa efectiva del hueco (Fig. 16.1-5, p. 632). La masa efectiva
depende de la estructura cristalina, la dirección y la banda; en la de valencia coexisten parábolas
de distinta curvatura: huecos pesados, ligeros y de la banda *split-off*. Valores típicos
$m_c/m_0$, $m_v/m_0$ en la **Tabla 16.1-1** (p. 632; ver sección de tablas).

**Bandgap directo e indirecto (p. 633).** Directo: el mínimo de la banda de conducción y el máximo
de la de valencia están en el mismo $k$ (GaAs). Indirecto: en distinto $k$ (Si). Una transición
fondo-de-conducción → tope-de-valencia en un material indirecto exige un cambio sustancial de momento;
por eso GaAs es un emisor eficiente y Si no lo es en condiciones ordinarias.

#### 16.1B Semiconductor Materials (p. 633)

Fig. 16.1-6 (p. 633): sección de la tabla periódica relevante (columnas II–VI, filas 2–6).

- **Elementales (p. 633):** Si y Ge (columna IV). Casi toda la electrónica integrada es de Si; en
  fotónica ambos se usan sobre todo como fotodetectores; por su bandgap indirecto no se usaban como
  emisores, aunque "algunas formas de Si son viables como emisores y la fotónica de silicio ha cobrado
  protagonismo". Propiedades en la Tabla 16.1-2.
- **Binarios III–V (p. 634):** Al, Ga, In con N, P, As, Sb: 12 compuestos (Tabla 16.1-2) con
  estructura zincblenda o wurtzita, tipo de bandgap, $E_g$ y longitud de onda de bandgap
  $\lambda_g = hc_0/E_g$. Fig. 16.1-7 (p. 637): $E_g$ frente a constante de red. GaAs fue el primero
  en fotónica; GaN es central por su bandgap en el UV cercano y su resistencia a altas temperaturas;
  AlN (aislante) tiene el mayor bandgap y emite en el UV medio.
- **Ternarios III–V (p. 634):** dos elementos de la columna III con uno de la V (o viceversa).
  (Al$_x$Ga$_{1-x}$)As interpola entre GaAs ($E_g = 1.42$ eV) y AlAs (2.16 eV) con $x$ (fracción de
  Ga sustituida por Al); como la línea GaAs–AlAs en la Fig. 16.1-7(a) es casi vertical, AlGaAs está
  **ajustado en red** a GaAs para cualquier $x$. Otros: Ga(As$_{1-x}$P$_x$); (In$_x$Ga$_{1-x}$)As
  (fuentes y detectores en IR cercano); (Al$_x$Ga$_{1-x}$)N e (In$_x$Ga$_{1-x}$)N (UV, violeta, azul,
  verde; Fig. 16.1-7(b)). Transistores bipolares (In$_x$Ga$_{1-x}$)As/InP conmutan cerca de 1 THz.
- **Cuaternarios III–V (p. 635):** In$_{1-x}$Ga$_x$As$_{1-y}$P$_y$: $E_g$ de 0.36 eV (InAs) a
  2.26 eV (GaP); la constante de red varía linealmente con la composición (**ley de Vegard**); con
  $y = 2.16(1-x)$ se ajusta en red a InP (sustrato) → LED, láseres y fotodiodos en 1550 nm.
  (Al$_x$In$_y$Ga$_{1-x-y}$)P sobre GaAs: rojo, naranja, amarillo. (Al$_x$In$_y$Ga$_{1-x-y}$)N:
  verde, azul, violeta, UV; sustratos zafiro y SiC.
- **Columna IV compuestos (p. 635):** SiC (carborundo; bandgap indirecto; fotodetectores UV y
  sustrato de nitruros); Si$_{1-x}$Ge$_x$ (fotodetector IR); Si$_{1-x-y}$Ge$_x$C$_y$,
  Si$_{1-x-y-z}$Ge$_x$C$_y$Sn$_z$.
- **II–VI (p. 635):** Zn, Cd, Hg con S, Se, Te (Fig. 16.1-8, p. 637): zincblenda, bandgap directo
  salvo HgSe y HgTe (semimetales con bandgap pequeño negativo). ZnSe crece sobre GaAs con pocos
  defectos; Hg$_x$Cd$_{1-x}$Te sobre CdTe → fotodetectores IR medio (cap. 18). Fuentes II–VI tienen
  vida limitada; se usan como puntos cuánticos con emisión sintonizable (Fig. 13.1-12).
- **IV–VI (p. 635):** Pb$_x$Sn$_{1-x}$Te, Pb$_x$Sn$_{1-x}$Se (IR); respuesta lenta por su gran
  constante dieléctrica y alto coeficiente de expansión térmica.
- **Estructuras cristalinas (p. 636, margen de Tabla 16.1-2):** diamante (D), zincblenda (Z; dos
  redes fcc interpenetradas desplazadas 1/4 de la diagonal del cubo; Brillouin en Fig. 7.3-4),
  wurtzita (W; dos redes hexagonales compactas desplazadas 3/8 del eje $c$). Todos los átomos con
  enlace tetraédrico.

**Semiconductores dopados (p. 636–638).** **Dopantes**: **donores** (exceso de electrones de
valencia) → tipo **$n$** (columna V en Si/Ge; columna VI reemplazando columna V en III–V);
**aceptores** → tipo **$p$** (columna III en Si/Ge; columna II reemplazando columna III en III–V).
Los átomos de columna IV son donores para la columna III y aceptores para la V. La neutralidad de
carga no cambia. **Intrínseco** (sin dopar): $n = p = n_i$, con $n_i$ creciendo exponencialmente con
$T$. **Extrínseco**: en tipo $n$, $n \gg p$ (**portadores mayoritarios**/**minoritarios**); la
concentración de mayoritarios ≈ concentración de dopante a temperatura ambiente (p. 638).
Implantación de un solo ion → materiales deterministas (p. 638).

> **Ejemplo 16.1-1 — Energía de ionización del electrón donor (p. 638).** Ge ($\epsilon/\epsilon_0 = 16$,
> Tabla 16.2-1) dopado con As. El electrón donor ($m_c = 0.2m_0$) se mueve en el campo del ion As$^+$
> como en un átomo de hidrógeno; en (13.1-4) con $n=1$, $Z=1$, $\epsilon_0\to\epsilon$ y $M_r\to m_c$:
> $$E_D = -\left(\frac{1}{4\pi\epsilon}\right)^2 \frac{m_c e^4}{2\hbar^2}. \qquad (16.1\text{-}5)$$
> Como el estado fundamental del hidrógeno está a $-13.6$ eV,
> $E_D = -(m_c/m_0)(\epsilon_0/\epsilon)^2\times 13.6\ \text{eV} \approx -0.01$ eV: el nivel donor está
> ≈ 0.01 eV por debajo de la banda de conducción. Como $kT \approx 0.026$ eV a 300 K, prácticamente
> todos los donores están ionizados y la concentración de electrones de conducción iguala a la de
> impurezas.

**Semiconductores orgánicos (p. 638–639).** Fotovoltaica, LED y pantallas; lentos y grandes pero
baratos y flexibles, imprimibles por inyección de tinta. Dos variedades (Fig. 16.1-9, p. 639):
(1) moléculas pequeñas (pentaceno, 5 anillos de benceno); (2) polímeros conjugados (poliacetileno).
La **conjugación** (enlaces C–C simples y dobles alternados) deslocaliza los electrones sobre
~10 unidades repetidas y forma bandas. Sin dopar, el polímero es aislante; Na (donor) → tipo $n$,
I (aceptor) → tipo $p$. Las moléculas pequeñas suelen conducir puras.

#### 16.1C Electron and Hole Concentrations (p. 639)

Se necesitan dos cosas: la densidad de estados y la probabilidad de ocupación.

**Densidad de estados (p. 639–640).** Electrón cerca del borde de la banda de conducción ≈ partícula
de masa $m_c$ en caja cúbica de lado $d$ con paredes perfectamente reflectoras:
$\mathbf{k} = (q_1\pi/d, q_2\pi/d, q_3\pi/d)$, $q_i$ enteros positivos (generalización 3D del pozo
infinito, Ej. 16.1-5). Hay $(d/\pi)^3$ puntos por unidad de volumen en el espacio $k$; contando el
octante positivo de la esfera de radio $k$ (volumen $\pi k^3/6$) y las dos orientaciones de espín:
$2(\pi k^3/6)/(\pi/d)^3 = (k^3/3\pi^2)d^3$ estados. La densidad de estados por unidad de volumen con
número de onda entre $k$ y $k+\Delta k$ es $\varrho(k)\Delta k = (k^2/\pi^2)\Delta k$:
$$\boxed{\varrho(k) = \frac{k^2}{\pi^2}} \qquad (16.1\text{-}6)\ \text{Density of States}$$
Idéntica al conteo de modos de un resonador EM 3D (§10.3): allí 2 polarizaciones, aquí 2 espines;
allí $\nu = ck/2\pi$ (lineal), aquí (16.1-3)/(16.1-4) (cuadráticas). Con
$\varrho_c(E)\,dE = \varrho(k)\,dk$ y $dE/dk$ de las parábolas:
$$\boxed{\varrho_c(E) = \frac{(2m_c)^{3/2}}{2\pi^2\hbar^3}\sqrt{E-E_c},\quad E\ge E_c \qquad (16.1\text{-}7)}$$
$$\boxed{\varrho_v(E) = \frac{(2m_v)^{3/2}}{2\pi^2\hbar^3}\sqrt{E_v-E},\quad E\le E_v \qquad (16.1\text{-}8)}$$
(Density of States Near Band Edges, p. 640). Nula en el borde de banda y creciente como raíz
cuadrada (Fig. 16.1-10, p. 640). Las $m_c$, $m_v$ de la Tabla 16.1-1 son valores promediados aptos
para calcular la densidad de estados.

**Probabilidad de ocupación (p. 640–642).** En equilibrio térmico a $T$, la probabilidad de que un
estado de energía $E$ esté ocupado por un electrón es la **función de Fermi** (Fermi–Dirac):
$$\boxed{f(E) = \frac{1}{\exp[(E-E_f)/kT] + 1}} \qquad (16.1\text{-}9)\ \text{Fermi Function}$$
$E_f$ = **energía (nivel) de Fermi**; $f(E_f) = 1/2$ a cualquier $T$. No es una densidad de
probabilidad (no integra a 1). A $T = 0$ K: $f = 1$ para $E\le E_f$, $f = 0$ para $E > E_f$.
$f(E)$ = prob. de ocupación por electrón; $1-f(E)$ = prob. de ocupación por hueco (banda de
valencia). Simétricas respecto a $E_f$ (Fig. 16.1-11, p. 641). Para $E - E_f \gg kT$,
$f(E)\approx\exp[-(E-E_f)/kT]$ (cola de Boltzmann, §13.2); para $E_f - E\gg kT$,
$1-f(E)\approx\exp[-(E_f-E)/kT]$ (p. 641–642).

**Concentraciones de portadores en equilibrio térmico (p. 642).** Con $n(E)\Delta E$ y
$p(E)\Delta E$ el número de electrones y huecos por unidad de volumen entre $E$ y $E+\Delta E$:
$$n(E) = \varrho_c(E)f(E), \qquad p(E) = \varrho_v(E)[1-f(E)], \qquad (16.1\text{-}10)$$
$$n = \int_{E_c}^{\infty} n(E)\,dE, \qquad p = \int_{-\infty}^{E_v} p(E)\,dE. \qquad (16.1\text{-}11)$$
Intrínseco: $n = p$ a cualquier $T$; si $m_v = m_c$, $E_f$ está exactamente en el centro del gap
(Fig. 16.1-12); en la mayoría de los intrínsecos está cerca del centro. Tipo $n$ (Fig. 16.1-13,
p. 643): nivel donor $E_D$ justo debajo de $E_c$ (p. ej. 0.01 eV), $E_f$ sobre el centro del gap.
Tipo $p$ (Fig. 16.1-14): nivel aceptor $E_A$ justo encima de $E_v$, $E_f$ bajo el centro. Neutralidad:
$n + N_A = p + N_D$ con $N_A$, $N_D$ aceptores y donores ionizados por unidad de volumen (p. 643).

> **Ejercicio 16.1-2 — Aproximación exponencial de la función de Fermi (p. 643).** Cuando
> $E - E_f \gg kT$ y $E_f - E \gg kT$ (nivel de Fermi dentro del gap y a varios $kT$ de los bordes;
> $kT\approx 0.026$ eV frente a $E_g = 1.12$ eV Si, 1.42 eV GaAs), mostrar que
> $$n = N_c\exp\!\left(-\frac{E_c - E_f}{kT}\right) \qquad (16.1\text{-}12)$$
> $$p = N_v\exp\!\left(-\frac{E_f - E_v}{kT}\right) \qquad (16.1\text{-}13)$$
> $$np = N_cN_v\exp\!\left(-\frac{E_g}{kT}\right), \qquad (16.1\text{-}14)$$
> con $N_c = 2(2\pi m_c kT/h^2)^{3/2}$ y $N_v = 2(2\pi m_v kT/h^2)^{3/2}$. Verificar que si $E_f$ está
> más cerca de la banda de conducción y $m_v = m_c$, entonces $n > p$; si más cerca de la de valencia,
> $p > n$.

**Ley de acción de masas (p. 644).** De (16.1-14):
$$np = 4\left(\frac{2\pi kT}{h^2}\right)^3 (m_cm_v)^{3/2}\exp\!\left(-\frac{E_g}{kT}\right) \qquad (16.1\text{-}15)$$
es independiente de la posición de $E_f$ y del dopado (mientras valga la aproximación exponencial).
Con $n = p = n_i$:
$$\boxed{n_i \approx \sqrt{N_cN_v}\,\exp\!\left(-\frac{E_g}{2kT}\right)} \qquad (16.1\text{-}16)\ \text{Intrinsic Carrier Concentration}$$
$$\boxed{np = n_i^2} \qquad (16.1\text{-}17)\ \text{Law of Mass Action}$$
Valores de $n_i$ a 300 K en la **Tabla 16.1-3** (p. 644). Uso: en tipo $n$ moderado $n\approx N_D$,
$p = n_i^2/N_D$, y de $n$ o $p$ se obtiene $E_f$ con (16.1-12)/(16.1-13). **Semiconductor
degenerado**: $E_f$ dentro de una banda; no vale la aproximación exponencial, $np\neq n_i^2$, hay que
integrar (16.1-11) numéricamente. Dopado muy fuerte: la banda de impurezas se funde con la banda
(**band tail**), reduciendo efectivamente el bandgap (p. 644).

**Concentraciones en cuasi-equilibrio (p. 645).** Cuando una corriente o un flujo de fotones induce
transiciones interbanda demasiado rápidas para el equilibrio, pero cada banda está en equilibrio
interno (relajación intrabanda $< 10^{-12}$ s frente a recombinación radiativa $\approx 10^{-9}$ s):
**cuasi-equilibrio**. Se usa una función de Fermi por banda con **cuasi-niveles de Fermi** $E_{fc}$ y
$E_{fv}$ (Fig. 16.1-15, p. 645): $f_c(E)$ con $E_{fc}$ para la banda de conducción, $1-f_v(E)$ con
$E_{fv}$ para la de valencia. Si ambos están bien dentro de sus bandas, $n$ y $p$ pueden ser grandes
simultáneamente.

> **Ejercicio 16.1-3 — Cuasi-niveles de Fermi dadas $n$ y $p$ (p. 645).** (a) A $T=0$ K, con
> (16.1-10) y (16.1-11),
> $$E_{fc} = E_c + (3\pi^2)^{2/3}\frac{\hbar^2}{2m_c}\,n^{2/3} \qquad (16.1\text{-}18a)$$
> $$E_{fv} = E_v - (3\pi^2)^{2/3}\frac{\hbar^2}{2m_v}\,p^{2/3}. \qquad (16.1\text{-}18b)$$
> (b) Mostrar que valen aproximadamente a cualquier $T$ si $E_{fc}-E_c\gg kT$ y $E_v - E_{fv}\gg kT$
> (cuasi-niveles profundos en las bandas).

#### 16.1D Generation, Recombination, and Injection (p. 646)

**Generación y recombinación en equilibrio térmico (p. 646–647).** Generación electrón–hueco
térmica (Fig. 16.1-16) equilibrada por **recombinación**; si emite fotón, **recombinación
radiativa**. **Recombinación no radiativa**: fonones, Auger (energía a otro electrón), superficies,
trampas/defectos en el gap (Fig. 16.1-17; puede ser radiativa o no). Como requiere electrón *y*
hueco:
$$\text{tasa de recombinación} = r\,np, \qquad (16.1\text{-}19)$$
con **coeficiente de recombinación** $r$ (cm³/s), dependiente de composición, defectos y $T$,
débilmente del dopado. En equilibrio, con $G_0$ la tasa de generación térmica,
$$G_0 = r\,n_0p_0, \qquad (16.1\text{-}20)$$
y $n_0p_0 = G_0/r \approx$ igual para $n$, $p$ o intrínseco → $n_i^2 = G_0/r$: la ley de acción de masas
es consecuencia del balance generación–recombinación (p. 647).

**Inyección electrón–hueco (p. 647–648).** Con una inyección externa (no térmica, p. ej. luz) a tasa
$R$ (pares por unidad de volumen y tiempo): $n = n_0+\Delta n$, $p = p_0+\Delta p$, $\Delta n = \Delta p$.
$$G_0 + R = r\,np \qquad (16.1\text{-}21)$$
$$R = r(np - n_0p_0) = r(n_0\Delta n + p_0\Delta n + \Delta n^2) = r\Delta n(n_0+p_0+\Delta n) \qquad (16.1\text{-}22)$$
$$R = \frac{\Delta n}{\tau}, \qquad (16.1\text{-}23)$$
$$\tau = \frac{1}{r[(n_0+p_0)+\Delta n]}. \qquad (16.1\text{-}24)$$
Para $\Delta n\ll n_0+p_0$:
$$\boxed{\tau \approx \frac{1}{r(n_0+p_0)}} \qquad (16.1\text{-}25)\ \text{Excess-Carrier Recombination Lifetime}$$
Tipo $n$ ($n_0\gg p_0$): $\tau\approx 1/rn_0$; tipo $p$: $\tau\approx 1/rp_0$. No aplica si dominan
trampas. $\tau$ es el **tiempo de vida de recombinación electrón–hueco** de los pares inyectados:
$$\frac{d(\Delta n)}{dt} = R - \frac{\Delta n}{\tau}, \qquad (16.1\text{-}26)$$
similar a (14.2-3). Estado estacionario → (16.1-23); si se apaga $R$ en $t_0$,
$\Delta n(t) = \Delta n(t_0)\exp[-(t-t_0)/\tau]$. Con inyección fuerte, $\tau$ depende de $\Delta n$
(16.1-24) y el decaimiento no es exponencial (p. 648). Si se conoce $R$:
$$\boxed{\Delta n = R\tau} \qquad (16.1\text{-}27)$$
y luego, suponiendo cuasi-equilibrio, (16.1-11) da los cuasi-niveles de Fermi. Base de la teoría de
LED y láser de diodo (cap. 17).

> **Ejercicio 16.1-4 — Inyección de pares en GaAs (p. 648).** GaAs tipo $n$ ($E_g = 1.42$ eV,
> $m_c\approx 0.07m_0$, $m_v\approx 0.50m_0$), inyección $R = 10^{23}$ /cm³·s, $n_0 = 10^{16}$ /cm³,
> $r = 10^{-11}$ cm³/s, $T = 300$ K. Determinar: (a) $p_0$ de equilibrio; (b) $\tau$; (c) $\Delta n$
> estacionario; (d) $E_{fc}-E_{fv}$ suponiendo $T = 0$ K. (Sin solución en el texto. Con los datos:
> $p_0 = n_i^2/n_0 = (1.8\times10^6)^2/10^{16}\approx 3.2\times10^{-4}$ cm⁻³;
> $\tau\approx 1/(rn_0) = 10^{-5}$ s; $\Delta n = R\tau = 10^{18}$ cm⁻³; (d) con (16.1-18).)

**Eficiencia cuántica interna (p. 648–649).** $\eta_i$ = cociente entre el coeficiente de
recombinación radiativa y el total, $r = r_r + r_{nr}$:
$$\eta_i = \frac{r_r}{r} = \frac{r_r}{r_r + r_{nr}}. \qquad (16.1\text{-}28)$$
Con tiempos de vida radiativo y no radiativo $\tau_r$, $\tau_{nr}$ (ya que $\tau\propto 1/r$):
$$\frac{1}{\tau} = \frac{1}{\tau_r} + \frac{1}{\tau_{nr}}, \qquad (16.1\text{-}29)$$
$$\boxed{\eta_i = \frac{\tau}{\tau_r} = \frac{\tau_{nr}}{\tau_r + \tau_{nr}}} \qquad (16.1\text{-}30)\ \text{Internal Quantum Efficiency}$$
Para inyección baja o moderada,
$$\tau_r \approx \frac{1}{r_r(n_0+p_0)}. \qquad (16.1\text{-}31)$$
$\tau_{nr}$ es más sensible a la concentración de centros de defecto que a $n$, $p$. Valores
representativos en la **Tabla 16.1-4** (p. 649). En Si volumétrico $\tau_r$ es órdenes de magnitud
mayor que $\tau$ (bandgap indirecto) → $\eta_i$ pequeña; en GaAs y GaN (directos) $\eta_i$ grande.

#### 16.1E Junctions (p. 649)

**Homouniones**: entre regiones de distinto dopado del mismo material (la unión $p$–$n$).
**Heterouniones**: entre materiales distintos (§16.1F).

**La unión $p$–$n$ (p. 650–651).** Diodo: rectificador, puerta lógica, regulador (Zener), varactor;
en optoelectrónica LED, láser de diodo, fotodetector, celda solar. Antes del contacto (Fig. 16.1-18):
región $p$ con huecos mayoritarios, región $n$ con electrones. Al unirlas (Fig. 16.1-19, p. 651):
- Difusión de electrones hacia $p$ y de huecos hacia $n$, dejando iones donores (+) y aceptores (−)
  fijos; los que cruzan se recombinan con los mayoritarios.
- Se forma la **capa de agotamiento (depletion layer)**, sin portadores móviles, solo cargas fijas;
  su espesor en cada lado es inversamente proporcional al dopado.
- El **campo interno (built-in field)** apunta de $n$ a $p$ y frena la difusión.
- Diferencia de potencial interna $V_0$ (lado $n$ a mayor potencial); las bandas se curvan; en
  equilibrio hay una sola función de Fermi, los $E_f$ de ambos lados se alinean.
- No hay corriente neta: difusión y arrastre (drift) se cancelan para electrones y huecos.

**Unión polarizada (p. 651–652).** **Directa** (+$V$ en $p$, Fig. 16.1-20): campo externo opuesto al
interno; desequilibrio, $E_f$ desalineados, cuasi-niveles $E_{fc}$, $E_{fv}$ en la capa de
agotamiento; la barrera baja en $eV$, la corriente de mayoritarios crece como $\exp(eV/kT)$:
$i = i_s\exp(eV/kT) - i_s$. Los mayoritarios que cruzan se vuelven minoritarios y se recombinan,
decayendo con la distancia (**inyección de portadores minoritarios**). **Inversa** ($V<0$): barrera
sube $e|V|$, corriente $\approx -i_s$ para $|V|\gg kT/e$. Característica del diodo ideal
(**ecuación de Shockley**, Fig. 16.1-21):
$$\boxed{i = i_s\left[\exp\!\left(\frac{eV}{kT}\right) - 1\right]} \qquad (16.1\text{-}32)\ \text{Ideal Diode Characteristic}$$
Respuesta dinámica (p. 652): dos capacitancias en paralelo con el diodo ideal. **Capacitancia de
unión**: cargas fijas; espesor de la capa $l\propto\sqrt{V_0 - V}$, $C = \epsilon A/l\propto
1/\sqrt{V_0-V}$ (menor en inversa → constante $RC$ más corta; base del varactor). **Capacitancia de
difusión**: inyección de minoritarios en directa; depende del tiempo de vida de los minoritarios y la
corriente.

**Diodo $p$–$i$–$n$ (p. 653).** Capa intrínseca (o poco dopada) entre $p$ y $n$ (Fig. 16.1-22): la
capa de agotamiento abarca toda la región $i$ (campo eléctrico uniforme en $i$, cargas fijas en los
bordes). Ventajas: capacitancia pequeña → respuesta rápida; más luz capturada → mayor eficiencia de
fotodetección (§18.3B). Preferido para fotodetectores.

#### 16.1F Heterojunctions (p. 653)

Uniones entre materiales distintos; se usan como regiones activas, capas de contacto y guías. Las
afinidades electrónicas fijan la alineación de los bordes de banda; conviene ajustar en red y usar
uniones graduales. Ventajas (p. 653–654):
- Saltos localizados en el diagrama de bandas (**band offsets**) que actúan como barreras para
  portadores seleccionados; p. ej. en una $p$–$n$ reducen la corriente de minoritarios y aumentan la
  eficiencia de inyección (Fig. 16.1-23).
- **Doble heteroestructura (DH)** $p$–$p$–$n$ (Fig. 16.1-23, p. 654): capa central de bandgap
  estrecho entre dos de bandgap ancho; en directa, las discontinuidades confinan electrones y huecos
  inyectados en una región común estrecha → LED, amplificadores ópticos y láseres de diodo (cap. 17).
- Discontinuidades que aceleran portadores: mejoran la ionización por impacto en fotodiodos de
  avalancha multicapa (§18.4A).
- Mezclar bandgap directo e indirecto para elegir dónde se emite luz; solo los directos emiten
  eficientemente.
- Elegir dónde se absorbe: un material con $E_g$ mayor que $h\nu$ es transparente → **capa ventana**.
- Distintos índices de refracción → estructuras fotónicas y guías de onda (caps. 7 y 8).

#### 16.1G Quantum-Confined Structures (p. 654)

**Crecimiento epitaxial (p. 654–655):** MBE (haces moleculares en alto vacío), LPE (enfriamiento de
solución saturada), VPE (gases en reactor; variantes MOCVD y HVPE). **Homoepitaxia**: misma
composición que el sustrato; **heteroepitaxia**: distinta. Capas de hasta monocapas.
Cuando el espesor es comparable o menor que la longitud de onda de de Broglie de un electrón
termalizado, $\lambda = h/p$ ($\approx 50$ nm en GaAs), hay que cuantizar la energía: pozos, hilos y
puntos cuánticos (§13.1C).

**Pozos cuánticos (p. 655–657).** Doble heteroestructura con capa ultrafina ($\lesssim 50$ nm) de
bandgap menor (p. ej. GaAs entre AlGaAs, Fig. 13.1-11): pozos rectangulares 1D para electrones (banda
de conducción) y huecos (valencia) (Fig. 16.1-24, p. 656). Pozo infinito de ancho $d$ (Ej. 16.1-5):
$$E_q = \frac{\hbar^2(q\pi/d)^2}{2m}, \qquad q = 1,2,3,\dots \qquad (16.1\text{-}33)$$
Ejemplo: GaAs ($m_c = 0.07m_0$), $d = 10$ nm: $E_q = 54, 216, 486$ meV (vs. $kT = 26$ meV a 300 K).
Pozo más angosto → mayor separación de niveles.

> **Ejercicio 16.1-5 — Niveles de un pozo cuántico (p. 655).** Resolver (13.1-3) para un pozo 1D
> infinito [$V(x) = 0$ en $0<x<d$, $\infty$ fuera] confirmando $E_q = \hbar^2(q\pi/d)^2/2m$
> (Fig. 16.1-25(a)). Comparar con el pozo finito de la Fig. 16.1-25(b).
> Fig. 16.1-25 (p. 656): pozo infinito: $E_1 = 4.9\,\hbar^2/md^2$, $E_2 = 19.7$, $E_3 = 44.4$,
> $E_4 = 78.9$ (todos en unidades $\hbar^2/md^2$). Pozo finito con $V_0 = 32\hbar^2/md^2$:
> $E_1 = 3.2\,\hbar^2/md^2 = 0.10V_0$, $E_2 = 11.9 = 0.37V_0$, $E_3 = 25.9 = 0.81V_0$; continuo por
> encima de $V_0$.

Los pozos son 3D: confinamiento en $x$ (espesor $d_1$) pero libres en $y$–$z$ ($d_2,d_3\gg d_1$):
$$E = E_c + \frac{\hbar^2k_1^2}{2m_c} + \frac{\hbar^2k_2^2}{2m_c} + \frac{\hbar^2k_3^2}{2m_c}, \qquad (16.1\text{-}34)$$
$k_i = q_i\pi/d_i$. Como $d_1\ll d_2,d_3$, $k_1$ toma valores discretos bien separados y $k_2,k_3$ se
aproximan por un continuo:
$$E = E_c + E_{q1} + \frac{\hbar^2k^2}{2m_c}, \qquad q_1 = 1,2,3,\dots \qquad (16.1\text{-}35)$$
con $k = |(k_2,k_3)|$ en el plano $y$–$z$; cada $q_1$ es una **subbanda** con mínimo $E_c + E_{q1}$
(p. 657). Comparación con el volumen (3D): $\varrho(k) = k^2/\pi^2$ y
$$\varrho_c(E) = \frac{\sqrt2\,m_c^{3/2}}{\pi^2\hbar^3}\sqrt{E-E_c}, \qquad E>0. \qquad (16.1\text{-}36)$$
En el pozo (2D): $\varrho(k) = k/\pi$ por unidad de área → $k/\pi d_1$ por unidad de volumen; con
$dE/dk = \hbar^2k/m_c$:
$$\varrho_c(E) = \begin{cases} \dfrac{m_c}{\pi\hbar^2 d_1}, & E > E_c + E_{q1} \\[4pt] 0, & E < E_c + E_{q1} \end{cases} \qquad q_1 = 1,2,3,\dots \qquad (16.1\text{-}37)$$
Constante por subbanda → **escalera** (Fig. 16.1-26, p. 658); en $E = E_c + E_{q1}$ coincide con la
densidad de estados del volumen. A diferencia del volumen, el pozo tiene densidad de estados
sustancial en su nivel más bajo permitido → efecto importante en las propiedades ópticas (§17.2D).

**Pozos múltiples y superredes (p. 657–658).** **MQW**: capas alternadas (p. ej. 100 capas de 10 nm,
≈ 40 planos atómicos cada una, ≈ 1 µm total). Si las barreras son tan delgadas que hay tunelamiento,
los niveles discretos se ensanchan en **minibandas** → **superred** (análogo a la formación de bandas
al acercar átomos, Figs. 13.1-6/7). También se pueden crear por dopado espacial (campos de carga
espacial). Fig. 16.1-27 (p. 658): MQW AlGaAs/GaAs (ajuste de red en amplio rango de composiciones y
gran diferencia de bandgap); otros: AlInAs/InGaAs, AlInGaP/InGaP, GaN/InGaN,
Al$_x$Ga$_{1-x}$N/Al$_y$Ga$_{1-y}$N. **MQW polarizados** (Fig. 16.1-28, p. 659): el campo inclina
los pozos y altera los niveles; en superredes, los niveles se difuminan en minibandas. Usos: LED
(§17.1C), amplificadores (§17.2D), láseres (§17.4), fotodetectores (§18.2C), moduladores (§20.5).

**Hilos cuánticos (p. 659–660).** Hilo delgado rodeado de material de bandgap mayor; confinamiento en
$x$ e $y$ (sección $d_1d_2$):
$$E = E_c + E_{q1} + E_{q2} + \frac{\hbar^2k^2}{2m_c}, \qquad (16.1\text{-}38)$$
$$E_{q1} = \frac{\hbar^2(q_1\pi/d_1)^2}{2m_c}, \qquad E_{q2} = \frac{\hbar^2(q_2\pi/d_2)^2}{2m_c}, \qquad q_1,q_2 = 1,2,3,\dots \qquad (16.1\text{-}39)$$
$k$ en $z$ (eje del hilo). Cada $(q_1,q_2)$ es una subbanda con $\varrho(k) = 1/\pi$ por unidad de
longitud → $1/\pi d_1d_2$ por unidad de volumen:
$$\varrho_c(E) = \begin{cases} \dfrac{(1/d_1d_2)(\sqrt{m_c}/\sqrt2\,\pi\hbar)}{\sqrt{E - E_c - E_{q1} - E_{q2}}}, & E > E_c + E_{q1} + E_{q2} \\[6pt] 0, & \text{en otro caso} \end{cases} \qquad q_1,q_2 = 1,2,3,\dots \qquad (16.1\text{-}40)$$
Decreciente con $E$ (Fig. 16.1-29, p. 659).

**Puntos cuánticos (p. 660).** Confinamiento en las tres direcciones (caja $d_1d_2d_3$):
$$E = E_c + E_{q1} + E_{q2} + E_{q3}, \qquad (16.1\text{-}41)$$
$$E_{q1} = \frac{\hbar^2(q_1\pi/d_1)^2}{2m_c},\quad E_{q2} = \frac{\hbar^2(q_2\pi/d_2)^2}{2m_c},\quad E_{q3} = \frac{\hbar^2(q_3\pi/d_3)^2}{2m_c},\quad q_1,q_2,q_3 = 1,2,3,\dots \qquad (16.1\text{-}42)$$
Niveles discretos, densidad de estados = secuencia de deltas (Fig. 16.1-29). "Átomos artificiales"
(§13.1C): niveles elegibles por diseño.

**Fig. 16.1-29 (p. 659)**, resumen: densidad de estados en volumen ($\sqrt{E}$), pozo (escalera),
hilo ($1/\sqrt{E}$ por subbanda) y punto (deltas): las bandas se dividen en subbandas que se estrechan
al aumentar el número de dimensiones confinadas.

### 16.2 Interactions of Photons with Charge Carriers (p. 660)

Propiedades ópticas básicas de semiconductores, con énfasis en absorción y emisión: **óptica de
semiconductores**.

#### 16.2A Photon Interactions in Bulk Semiconductors (p. 660)

Mecanismos de absorción y emisión en volumen (p. 660–661; Fig. 16.2-1, p. 661):
- **Transiciones banda a banda (interbanda)**: absorción crea un par e–h [Fig. 16.2-1(a), GaAs:
  $\lambda_0<\lambda_g = hc_0/E_g = 0.87$ µm]; la recombinación emite un fotón. Pueden estar
  asistidas por fonones (cuantos de vibración de la red).
- **Impureza–banda**: entre nivel donor/aceptor y una banda en material dopado. En tipo $p$ un fotón
  de baja energía sube un electrón de la banda de valencia al nivel aceptor [Fig. 16.2-1(b): Ge:Hg,
  $E_A = 0.088$ eV, $\lambda_A = hc_0/E_A = 14$ µm]. Un hueco puede quedar atrapado por un aceptor
  ionizado y el electrón decae radiativa o no radiativamente. También vía trampas (Fig. 16.1-17).
- **Portadores libres (intrabanda)**: el fotón lleva un electrón a un nivel superior de la misma
  banda [Fig. 16.2-1(c), Ge]; sigue **termalización** (relajación al fondo de la banda liberando
  fonones). La absorción por portadores libres es **proporcional a la concentración de portadores y
  decrece con la energía del fotón como una ley de potencias** (p. 661).
- **Fonones**: fotones de longitud de onda larga excitan directamente vibraciones de la red.
- **Excitónicos**: el fotón forma un **excitón** (par e–h ligado por Coulomb, análogo al átomo de
  hidrógeno); su aniquilación puede emitir un fotón.

Todos contribuyen al coeficiente de absorción $\alpha$: **Fig. 16.2-2** (p. 662), $\alpha$ (cm⁻¹)
frente a $h\nu$ (0.01–10 eV) y $\lambda_0$ para Si y GaAs a 300 K: pico de fonones ≈ 0.03–0.1 eV
($10^4$ cm⁻¹), caída de portadores libres, mínimo ≈ 1 eV (transparencia), borde banda a banda
abrupto en GaAs (1.42 eV, hasta $10^4$–$10^6$ cm⁻¹) y gradual en Si (1.12 eV), pico de excitón
libre en GaAs. Si es relativamente transparente en $\lambda_0\approx 1.1$–$12$ µm; GaAs intrínseco en
$\lambda_0\approx 0.87$–$12$ µm (cf. Fig. 5.5-1). **Fig. 16.2-3** (p. 662): $\alpha$ en escala
ampliada para InSb, InAs, Ge, Si, InP, GaAs, GaP, GaN (0–4.5 eV, $10$–$10^5$ cm⁻¹). Para
$h\nu > E_g$ domina banda a banda. **Borde de absorción**: región donde el material pasa de
transparente ($h\nu<E_g$) a fuertemente absorbente ($h\nu>E_g$); más abrupto en bandgap directo.

#### 16.2B Band-to-Band Transitions in Bulk Semiconductors (p. 662)

Teoría simplificada de absorción y emisión banda a banda directa, ignorando los demás mecanismos.

**Longitud de onda de bandgap (p. 662–663).** Absorción/emisión directa solo si $h\nu > E_g$;
frecuencia mínima $\nu_g = E_g/h$, longitud de onda máxima $\lambda_g = c_0/\nu_g = hc_0/E_g$. Con
$E_g$ en eV y $\lambda_g = hc_0/eE_g$ en µm:
$$\boxed{\lambda_g \approx \frac{1.24}{E_g}} \qquad (16.2\text{-}1)\ \text{Bandgap Wavelength } \lambda_g\ (\mu\text{m}),\ E_g\ (\text{eV})$$
(**longitud de onda de bandgap** o **de corte**). Valores en Tabla 16.1-2 y Figs. 16.1-7/8.
**Fig. 16.2-4** (p. 663): $\lambda_g$ y $E_g$ (0–6 eV) para AlInGaN, AlGaN, InGaN, InGaAsP, AlInGaP,
InGaP, GaAsP, AlGaAs, InGaAs, GaAsSb (sombreado = composiciones de bandgap directo), del IR medio al
UV medio.

**Condiciones de absorción y emisión (p. 663–664).** Absorción ($h\nu>E_g$, $\lambda<\lambda_g$)
genera un par [Fig. 16.2-5(a)]: fotoconductor con conductividad ∝ flujo de fotones (cap. 18).
Desexcitación → emisión espontánea [Fig. 16.2-5(b), base del LED, §17.1] o estimulada
[Fig. 16.2-5(c), base de amplificadores y láseres, §17.2–17.4].
- *Conservación de energía*: estados $E_1$ (valencia) y $E_2$ (conducción):
  $$E_2 - E_1 = h\nu. \qquad (16.2\text{-}2)$$
- *Conservación de momento*: $p_2 - p_1 = h\nu/c = h/\lambda$, o $k_2 - k_1 = 2\pi/\lambda$. Como el
  diagrama $E$–$k$ llega hasta $k\sim 2\pi/a$ con $a\ll\lambda$, $2\pi/\lambda\ll 2\pi/a$ y los
  momentos de electrón y hueco son aproximadamente iguales: **regla de selección $k$**, $k_2\approx k_1$
  → transiciones verticales en el diagrama $E$–$k$ (Fig. 16.2-5).
- *Energías y momentos con los que interactúa el fotón*: con las parábolas (16.1-3), (16.1-4) y
  $E_c - E_v = E_g$:
  $$E_2 - E_1 = \frac{\hbar^2k^2}{2m_v} + E_g + \frac{\hbar^2k^2}{2m_c} = h\nu, \qquad (16.2\text{-}3)$$
  $$k^2 = \frac{2m_r}{\hbar^2}(h\nu - E_g), \qquad (16.2\text{-}4)$$
  $$\frac{1}{m_r} = \frac{1}{m_v} + \frac{1}{m_c}. \qquad (16.2\text{-}5)$$
  Sustituyendo en (16.1-3):
  $$E_2 = E_c + \frac{m_r}{m_c}(h\nu - E_g) \qquad (16.2\text{-}6)$$
  $$E_1 = E_v - \frac{m_r}{m_v}(h\nu - E_g) = E_2 - h\nu. \qquad (16.2\text{-}7)$$
  Si $m_c = m_v$: $E_2 = E_c + \tfrac12(h\nu - E_g)$ (p. 665).
- *Densidad conjunta de estados óptica* (p. 665): densidad de estados $\varrho(\nu)$ con los que
  interactúa un fotón de energía $h\nu$ cumpliendo energía y momento. De $\varrho_c(E_2)dE_2 =
  \varrho(\nu)d\nu$:
  $$\varrho(\nu) = \frac{hm_r}{m_c}\varrho_c(E_2). \qquad (16.2\text{-}8)$$
  Con (16.1-7) y (16.2-6), estados por unidad de volumen y de frecuencia:
  $$\boxed{\varrho(\nu) = \frac{(2m_r)^{3/2}}{\pi\hbar^2}\sqrt{h\nu - E_g}, \qquad h\nu\ge E_g} \qquad (16.2\text{-}9)\ \text{Optical Joint Density of States}$$
  (Fig. 16.2-6, p. 665: ley de raíz cuadrada desde $E_g$). Usando $E_1$ y $\varrho_v(E_1)$ se obtiene la
  misma expresión.
- *La emisión es improbable en bandgap indirecto* (p. 665–666): la recombinación desde el fondo de
  conducción al tope de valencia (donde están los portadores) exige un cambio de momento que el fotón
  no puede dar; lo aportan fonones (momento grande, energía pequeña ≈ 0.01–0.1 eV; transiciones
  horizontales en $E$–$k$, Fig. 16.2-7). Proceso de tres cuerpos (electrón, fotón, fonón) → poco
  probable; Si tiene $r_r$ mucho menor que GaAs (Tabla 16.1-4): no es buen emisor.
- *La absorción no es improbable en bandgap indirecto* (p. 666): proceso secuencial de dos pasos
  (Fig. 16.2-8): transición vertical ($k$ conservado) a un nivel alto de la banda de conducción y
  luego termalización al fondo cediendo momento a fonones; el hueco igual. Si es un detector
  eficiente, como GaAs.

#### 16.2C Absorption, Emission, and Gain in Bulk Semiconductors (p. 666)

Densidades de probabilidad de emisión/absorción de un fotón $h\nu$ en transición directa banda a
banda. Tres factores: (1) probabilidades de ocupación, (2) probabilidades de transición, (3)
densidad conjunta de estados óptica (p. 667).

**Probabilidades de ocupación (p. 667).**
- *Condición de emisión*: estado $E_2$ (conducción) lleno **y** estado $E_1$ (valencia) vacío.
- *Condición de absorción*: $E_2$ vacío **y** $E_1$ lleno.
Con las funciones de Fermi $f_c(E)$, $f_v(E)$ del cuasi-equilibrio (eventos independientes):
$$\boxed{f_e(\nu) = f_c(E_2)[1 - f_v(E_1)]} \qquad (16.2\text{-}10)$$
$$\boxed{f_a(\nu) = [1 - f_c(E_2)]f_v(E_1)} \qquad (16.2\text{-}11)$$
con $E_1$, $E_2$ dadas por (16.2-6), (16.2-7).

> **Ejercicio 16.2-1 — Condición para que la emisión supere a la absorción (p. 667).** (a) En
> equilibrio térmico, mostrar que $f_e(\nu) < f_a(\nu)$ siempre: la emisión no puede superar a la
> absorción. (b) En cuasi-equilibrio ($E_{fc}\neq E_{fv}$), con transiciones radiativas entre $E_2$ y
> $E_1$ al mismo $k$, mostrar que la emisión es más probable que la absorción si
> $$\boxed{E_{fc} - E_{fv} > h\nu} \qquad (16.2\text{-}12)\ \text{Condition for Net Emission}$$
> ¿Qué implica sobre $E_{fc}$ respecto a $E_c$ y $E_{fv}$ respecto a $E_v$? (Como $h\nu>E_g$, al menos
> uno de los cuasi-niveles debe estar dentro de su banda: inversión de población.)

**Probabilidades de transición (p. 668).** Leyes de §13.3A–C (y Ej. 13.3-1), expresadas para
emisión/absorción en banda estrecha $\nu$ a $\nu+d\nu$. **Resumen (recuadro, p. 668):** una
transición radiativa entre $E_1$ y $E_2$ tiene sección eficaz $\sigma(\nu) = (\lambda^2/8\pi t_{sp})g(\nu)$,
con $g(\nu)$ la función de forma de línea (ancho $\Delta\nu$, centro $\nu_0 = (E_2-E_1)/h$, área
unidad). En semiconductores $\tau_r$ hace el papel de $t_{sp}$:
$$\sigma(\nu) = \frac{\lambda^2}{8\pi\tau_r}g(\nu). \qquad (16.2\text{-}13)$$
- Si se cumple la condición de ocupación para emisión, la densidad de probabilidad (por unidad de
  tiempo) de emisión espontánea en cualquiera de los modos en $[\nu,\nu+d\nu]$ es
  $$P_{sp}(\nu)\,d\nu = \frac{1}{\tau_r}g(\nu)\,d\nu. \qquad (16.2\text{-}14)$$
- Si se cumple la condición de emisión **y** hay densidad espectral media de flujo de fotones
  $\phi_\nu$ (fotones por unidad de tiempo, área y frecuencia), la densidad de probabilidad de emisión
  estimulada de un fotón en $[\nu,\nu+d\nu]$ es
  $$W_i(\nu)\,d\nu = \phi_\nu\sigma(\nu)\,d\nu = \phi_\nu\frac{\lambda^2}{8\pi\tau_r}g(\nu)\,d\nu. \qquad (16.2\text{-}15)$$
- Si se cumple la condición de absorción y hay $\phi_\nu$, la densidad de probabilidad de absorción
  también es (16.2-15).
Como cada transición tiene distinto $\nu_0$, se escribe $g_{\nu_0}(\nu)$. El ensanchamiento homogéneo
proviene de colisiones electrón–fonón: Lorentziana [cf. (13.3-34)–(13.3-37)] con
$\Delta\nu\approx 1/\pi T_2$, $T_2$ ~ ps; p. ej. $T_2 = 1$ ps → $\Delta\nu = 318$ GHz,
$h\Delta\nu\approx 1.3$ meV. El ensanchamiento por vida radiativa es despreciable frente al colisional
(p. 668).

**Tasas totales de emisión y absorción (p. 669).** Tasas (fotones/s·Hz·cm³) a frecuencia $\nu$: se
multiplica la densidad de probabilidad de transición [(16.2-14) o (16.2-15)] por la probabilidad de
ocupación [(16.2-10) o (16.2-11)] y por la densidad de estados $\varrho(\nu_0)$ (16.2-9), e integra
sobre $\nu_0$:
$$r_{sp}(\nu) = \int[(1/\tau_r)g_{\nu_0}(\nu)]f_e(\nu_0)\varrho(\nu_0)\,d\nu_0. \qquad (16.2\text{-}16)$$
Si $\Delta\nu$ (colisional) es mucho menor que el ancho de $f_e(\nu_0)\varrho(\nu_0)$ (lo usual),
$g_{\nu_0}(\nu)\approx\delta(\nu-\nu_0)$ y:
$$\boxed{\begin{aligned} r_{sp}(\nu) &= \frac{1}{\tau_r}\varrho(\nu)f_e(\nu) & (16.2\text{-}17)\\ r_{st}(\nu) &= \phi_\nu\frac{\lambda^2}{8\pi\tau_r}\varrho(\nu)f_e(\nu) & (16.2\text{-}18)\\ r_{ab}(\nu) &= \phi_\nu\frac{\lambda^2}{8\pi\tau_r}\varrho(\nu)f_a(\nu) & (16.2\text{-}19)\end{aligned}}\ \text{Emission and Absorption Rates}$$
Los productos $\varrho(\nu)f_e(\nu)$ y $\varrho(\nu)f_a(\nu)$ son análogos a $g(\nu)N_2$ y $g(\nu)N_1$
de los sistemas atómicos (caps. 13–15). $f_e$, $f_a$ requieren $E_{fc}$, $E_{fv}$, que se controlan
p. ej. con la polarización de una unión $p$–$n$. (16.2-17) describe el LED (§17.1); (16.2-18)
amplificadores y láseres (§17.2–17.4); (16.2-19) detectores (§18.1B).

**Intensidad espectral de emisión espontánea en equilibrio térmico (p. 669–670).** Una sola
función de Fermi: $f_e(\nu) = f(E_2)[1-f(E_1)]$. Si $E_f$ está en el gap a varios $kT$ de los bordes,
con $f(E_2)\approx\exp[-(E_2-E_f)/kT]$ y $1-f(E_1)\approx\exp[-(E_f-E_1)/kT]$:
$$f_e(\nu)\approx\exp\!\left(-\frac{h\nu}{kT}\right). \qquad (16.2\text{-}20)$$
Con (16.2-9) y (16.2-17):
$$\boxed{r_{sp}(\nu)\approx D_0\sqrt{h\nu - E_g}\,\exp\!\left(-\frac{h\nu - E_g}{kT}\right), \qquad h\nu\ge E_g} \qquad (16.2\text{-}21)$$
$$D_0 = \frac{(2m_r)^{3/2}}{\pi\hbar^2\tau_r}\exp\!\left(-\frac{E_g}{kT}\right) \qquad (16.2\text{-}22)$$
($D_0$ crece exponencialmente con $T$). Fig. 16.2-9 (p. 670): $r_{sp}(\nu)$ frente a $h\nu$: corte
inferior en $\nu = E_g/h$, raíz cuadrada creciente × exponencial decreciente, ancho aproximado
$2kT/h$. Para aumentar la emisión se saca al material del equilibrio de modo que $f_c(E_2)$ sea
grande y $f_v(E_1)$ pequeño (abundancia de electrones *y* huecos: LED, §17.1).

**Coeficiente de ganancia en cuasi-equilibrio (p. 670–671).** Cilindro de área unidad y longitud
$dz$ con flujo espectral medio $\phi_\nu(z)$ a lo largo del eje (Fig. 14.1-1); el incremento es
$[r_{st}(\nu) - r_{ab}(\nu)]dz$:
$$\frac{d\phi_\nu(z)}{dz} = \frac{\lambda^2}{8\pi\tau_r}\varrho(\nu)[f_e(\nu) - f_a(\nu)]\phi_\nu(z) = \gamma_0(\nu)\phi_\nu(z). \qquad (16.2\text{-}23)$$
$$\boxed{\gamma_0(\nu) = \frac{\lambda^2}{8\pi\tau_r}\varrho(\nu)f_g(\nu)} \qquad (16.2\text{-}24)\ \text{Gain Coefficient}$$
con el **factor de inversión de Fermi**
$$f_g(\nu)\equiv f_e(\nu) - f_a(\nu) = f_c(E_2) - f_v(E_1), \qquad (16.2\text{-}25)$$
($E_1$, $E_2$ de (16.2-6)/(16.2-7)). Comparando con (14.1-4), $\varrho(\nu)f_g(\nu)$ hace el papel de
$Ng(\nu)$ del sistema atómico. Con (16.2-9):
$$\gamma_0(\nu) = D_1\sqrt{h\nu - E_g}\,f_g(\nu), \qquad h\nu > E_g \qquad (16.2\text{-}26a)$$
$$D_1 = \frac{\sqrt2\,m_r^{3/2}\lambda^2}{h^2\tau_r}. \qquad (16.2\text{-}26b)$$
El signo y la forma espectral de $f_g(\nu)$ los fijan $E_{fc}$, $E_{fv}$ (estado de excitación de los
portadores); $f_g>0$ (inversión, ganancia neta) solo si $E_{fc} - E_{fv} > h\nu$ (Ej. 16.2-1). Se
logra bombeando suficientemente (§17.2): física de amplificadores y láseres de semiconductor.

**Coeficiente de absorción en equilibrio térmico (p. 671–672).** Un solo nivel de Fermi
$E_f = E_{fc} = E_{fv}$:
$$f_c(E) = f_v(E) = f(E) = \frac{1}{\exp[(E-E_f)/kT]+1}. \qquad (16.2\text{-}27)$$
Entonces $f_g(\nu) = f(E_2) - f(E_1) < 0$ (pues $E_2>E_1$ y $f$ decrece): $\gamma_0(\nu)<0$ siempre,
sea cual sea $E_f$: un semiconductor en equilibrio térmico, intrínseco o dopado, **siempre atenúa**.
Coeficiente de atenuación (absorción) $\alpha(\nu) = -\gamma_0(\nu)$:
$$\boxed{\alpha(\nu) = D_1\sqrt{h\nu - E_g}\,[f(E_1) - f(E_2)]} \qquad (16.2\text{-}28)\ \text{Absorption Coefficient}$$
con $E_2$, $E_1$ de (16.2-6), (16.2-7) y $D_1$ de (16.2-26b). Si $E_f$ está en el gap a varios $kT$
de los bordes, $f(E_1)\approx 1$, $f(E_2)\approx 0$, $[f(E_1)-f(E_2)]\approx 1$, y la contribución
directa banda a banda es
$$\alpha(\nu)\approx\frac{\sqrt2\,c^2m_r^{3/2}}{\tau_r}\frac{1}{(h\nu)^2}\sqrt{h\nu - E_g}. \qquad (16.2\text{-}29)$$
(Se obtiene de (16.2-28) con $\lambda = c/\nu$ y $h^2\nu^2 = (h\nu)^2$; $c$ = velocidad de la luz en
el medio, $c = c_0/n$.) **Fig. 16.2-10** (p. 672): (16.2-29) para GaAs con $n = 3.6$, $m_c = 0.07m_0$,
$m_v = 0.50m_0$, $m_0 = 9.1\times10^{-31}$ kg, dopado tal que $\tau_r = 0.4$ ns (distinto de la
Tabla 16.1-4 por el dopado), $T$ tal que $[f(E_1)-f(E_2)]\approx1$: $\alpha$ sube desde 0 en
$h\nu = E_g$ hasta ≈ $10^4$ cm⁻¹ cerca de $h\nu - E_g\approx 0.5$ eV y luego decae suavemente
(por el $1/(h\nu)^2$). Al subir $T$, $f(E_1) - f(E_2)$ baja de 1 y $\alpha$ se reduce. Comparar con la
Fig. 16.2-3 experimental (todos los mecanismos).

Según (16.2-29), cerca del borde de un bandgap directo $\alpha\propto\sqrt{h\nu - E_g}$; el inicio
abrupto en $h\nu = E_g$ es una idealización: hay una **cola de Urbach** exponencial de ancho
característico $\approx kT$ que entra en el gap (absorción asistida por fonones, aleatoriedad del
dopado, variaciones de composición, desorden térmico y estático). En bandgap indirecto (Ge, Si, GaP)
la absorción cerca del borde sigue $(h\nu - E_g)^2$ en vez de la raíz cuadrada (p. 672).

> **Ejercicio 16.2-2 — Longitud de onda de máxima absorción banda a banda (p. 672).** Con (16.2-29),
> hallar la longitud de onda en el vacío $\lambda_p$ a la que $\alpha$ es máximo en equilibrio
> térmico; calcular para GaAs. Solo aplica a transiciones directas banda a banda. (Sin solución en el
> texto. Maximizando $\sqrt{x - E_g}/x^2$ con $x = h\nu$: $d/dx \Rightarrow x = \tfrac43E_g$, así
> $h\nu_p = 4E_g/3$ y $\lambda_p = \tfrac34\lambda_g$; para GaAs $\lambda_g\approx 0.873$ µm →
> $\lambda_p\approx 0.65$ µm. Consistente con el máximo de la Fig. 16.2-10 en
> $h\nu - E_g\approx E_g/3\approx 0.47$ eV.)

#### 16.2D Photon Interactions in Quantum-Confined Structures (p. 673)

Mecanismos en MQW y superredes (Fig. 16.2-11, p. 673):
- **Interbanda (banda a banda)** [Fig. 16.2-11(a)]: como en volumen, pero la densidad conjunta de
  estados (16.2-9) se reemplaza por (17.2-11). Responsables de LED MQW, diodos superluminiscentes,
  láseres (Figs. 17.1-20, 17.2-11, 17.4-8) y moduladores de electroabsorción MQW (Fig. 20.5-2).
- **Excitónicas** [Fig. 16.2-11(b)]: el confinamiento 1D aumenta la energía de ligadura del excitón →
  transiciones excitónicas fuertes incluso a 300 K; importantes en moduladores de electroabsorción.
- **Intersubbanda** [Fig. 16.2-11(c)]: entre niveles de una misma banda del MQW; base del láser de
  cascada cuántica de pozo [Fig. 17.4-6(a)] y del fotodetector IR de pozo cuántico (Fig. 18.2-3: de
  nivel ligado al continuo). Dinámica de portadores en picosegundos → gran ancho de banda.
- **Minibanda** [Fig. 16.2-11(d)]: en superredes, niveles ensanchados en minibandas separadas por
  minigaps; láser de cascada cuántica de superred [Fig. 17.4-6(b)]. Relajación rápida y **grandes no
  linealidades** (intersubbanda y minibanda) → conmutación y demultiplexación totalmente ópticas.

#### 16.2E Refractive Index (p. 674)

Controlar el índice es clave en guías de onda, óptica integrada y láseres de diodo. Los
semiconductores son dispersivos: $n$ depende de $\lambda$. El índice está ligado al coeficiente de
absorción $\alpha(\nu)$ porque las partes real e imaginaria de la susceptibilidad deben satisfacer
las **relaciones de Kramers–Kronig** (§5.5B y §B.1 del Apéndice B). **Fig. 16.2-12** (p. 674): índice
$n$ y índice de grupo $N$ para GaAs frente a $\lambda_0$ (1–4 µm) calculados con la ecuación de
Sellmeier (§5.5C, Tabla 5.5-1): $n$ baja de ≈ 3.55 a ≈ 3.45 entre 1 y 4 µm; $N$ baja de ≈ 3.8 a
≈ 3.5 y siempre $N > n$ (dispersión normal). El índice depende de la temperatura y del dopado.
**Tabla 16.2-1** (p. 674): índices de semiconductores elementales y III–V binarios cerca de
$h\nu\approx E_g$ y 300 K; para ternarios y cuaternarios se interpola linealmente entre los
componentes.

*Nota:* el capítulo no da fórmulas para el cambio de índice por portadores libres ni para la
absorción de dos fotones; solo la relación cualitativa con K–K y Sellmeier.

### Reading List (p. 675–677)

Libros de física, dispositivos y óptica de semiconductores (Sze & Ng 2006; Kasap & Capper 2006;
Streetman & Banerjee 2005; Klingshirn 1997; Kittel 2004; Haug & Koch 2004; Singh 2003; Landsberg 2003;
Basu 2003; Fox 2001; Chow & Koch 1999; Peyghambarian, Koch & Mysyrowicz 1993; Ashcroft & Mermin 1976;
Pankove 1971, entre otros), libros de nanoestructuras y confinamiento cuántico (Paiella 2006; Harrison
2000; Gaponenko 1998; Bányai & Koch 1993, etc.) y artículos (IEEE JSTQE números especiales; Wu et al.
2003 sobre *bandgap bowing* en nitruros; Miller 1990; Schmitt-Rink, Chemla & Miller 1989, *Linear and
Nonlinear Optical Properties of Semiconductor Quantum Wells*; Esaki 1986).

---

## Tablas y datos numéricos útiles

**Constantes usadas en el capítulo**
- $m_0 = 9.1\times10^{-31}$ kg (p. 631); $kT = 0.026$ eV a $T = 300$ K (p. 641); $-13.6$ eV = estado
  fundamental del hidrógeno (p. 638); longitud de de Broglie de un electrón termalizado en GaAs
  ≈ 50 nm (p. 655); relajación intrabanda $<10^{-12}$ s, recombinación radiativa ≈ $10^{-9}$ s (p. 645);
  $T_2\sim$ ps → $\Delta\nu = 318$ GHz, $h\Delta\nu\approx 1.3$ meV para $T_2 = 1$ ps (p. 668);
  energías de fonones ≈ 0.01–0.1 eV (p. 666); nivel donor típico $E_D\approx 0.01$ eV bajo $E_c$ (p. 638);
  Ge:Hg $E_A = 0.088$ eV, $\lambda_A = 14$ µm (p. 661).
- Conversión: $\lambda_g\ [\mu\text{m}] \approx 1.24/E_g\ [\text{eV}]$ (16.2-1, p. 663).

**Tabla 16.1-1 — Masas efectivas (p. 632)**

| Material | $m_c/m_0$ | $m_v/m_0$ |
|---|---|---|
| Si | 0.98 | 0.49 |
| GaAs | 0.07 | 0.50 |
| GaN | 0.20 | 0.80 |

**Tabla 16.1-2 — Semiconductores elementales y III–V binarios (p. 636; $T = 300$ K)**
Estructura: D = diamante, Z = zincblenda, W = wurtzita. Tipo: I = indirecto, D = directo.

| Material | Estructura | Tipo | $E_g$ (eV) | $\lambda_g$ (µm) |
|---|---|---|---|---|
| Si | D | I | 1.12 | 1.11 |
| Ge | D | I | 0.66 | 1.88 |
| AlN | W | D | 6.20 | 0.200 |
| AlP | Z | I | 2.45 | 0.506 |
| AlAs | Z | I | 2.16 | 0.574 |
| AlSb | Z | I | 1.58 | 0.785 |
| GaN | W | D | 3.39 | 0.366 |
| GaP | Z | I | 2.26 | 0.549 |
| GaAs | Z | D | 1.42 | 0.873 |
| GaSb | Z | D | 0.73 | 1.70 |
| InN | W | D | 0.65 | 1.91 |
| InP | Z | D | 1.35 | 0.919 |
| InAs | Z | D | 0.36 | 3.44 |
| InSb | Z | D | 0.17 | 7.29 |

**Tabla 16.1-3 — Concentración intrínseca de portadores a 300 K (p. 644)**

| Material | $n_i$ (cm⁻³) |
|---|---|
| Si | $1.5\times10^{10}$ |
| GaAs | $1.8\times10^{6}$ |
| GaN | $1.9\times10^{-10}$ |

Nota del libro: sustituir las masas de la Tabla 16.1-1 y $E_g$ de la 16.1-2 en (16.1-16) no
reproduce exactamente estos valores por la sensibilidad de la fórmula a los parámetros.

**Tabla 16.1-4 — Coeficientes y tiempos de recombinación, $\eta_i$ (p. 649)**
Material tipo $n$ con $n_0 = 10^{17}$ cm⁻³, centros de defecto $10^{15}$ cm⁻³, $T = 300$ K.

| Material | $r_r$ (cm³/s) | $\tau_r$ | $\tau_{nr}$ | $\tau$ | $\eta_i$ |
|---|---|---|---|---|---|
| Si | $10^{-15}$ | 10 ms | 100 ns | 100 ns | $10^{-5}$ |
| GaAs | $10^{-10}$ | 100 ns | 100 ns | 50 ns | 0.5 |
| GaN | $10^{-8}$ | 20 ns | 0.1 ns | 0.1 ns | 0.005 (InGaN en la práctica: ≈ 0.3) |

**Tabla 16.2-1 — Índices de refracción (p. 674; $h\nu\approx E_g$, 300 K)**

| Material | $n$ | Material | $n$ |
|---|---|---|---|
| Ge | 4.0 | GaN | 2.5 |
| Si | 3.5 | GaP | 3.3 |
| AlN | 2.2 | GaAs | 3.6 |
| AlP | 3.0 | GaSb | 4.0 |
| AlAs | 3.2 | InN | 3.0 |
| AlSb | 3.8 | InP | 3.5 |
| | | InAs | 3.8 |
| | | InSb | 4.2 |

Ternarios y cuaternarios: interpolación lineal entre componentes.

**Constantes dieléctricas citadas** (Ej. 16.1-1 y Prob. 16.1-6, p. 638, 677): Ge $\epsilon/\epsilon_0 = 16$;
Si 12.3; GaAs 13; GaN 6.25; poliacetileno ≈ 3 (con $m_c\approx m_0$).

**Otros datos**
- GaAs: $E_g = 1.42$ eV, $m_c = 0.07m_0$, $m_v = 0.50m_0$, $n = 3.6$, $\tau_r = 0.4$ ns (dopado de la
  Fig. 16.2-10, p. 672); $\tau_r = 0.4$ ns también en Probs. 16.2-4 y 16.2-5.
- AlGaAs: $E_g$ de 1.42 eV (GaAs) a 2.16 eV (AlAs); ajustado en red a GaAs (p. 634). Prob. 16.1-10:
  $E_g$ sube ≈ 12.47 meV por cada 1 % de Al; el pozo de conducción es ≈ 60 % de la discontinuidad
  total.
- InGaAsP: $E_g$ de 0.36 eV (InAs) a 2.26 eV (GaP); ajuste a InP con $y = 2.16(1-x)$ (p. 635).
- Pozo GaAs 10 nm infinito: $E_1 = 54$, $E_2 = 216$, $E_3 = 486$ meV (p. 655).
- Transparencia: Si ≈ 1.1–12 µm; GaAs intrínseco ≈ 0.87–12 µm (Fig. 16.2-2, p. 662).
- $\alpha$ típicos: borde banda a banda $10^4$–$10^6$ cm⁻¹; mínimo entre portadores libres y borde
  ≈ 1–10 cm⁻¹ (Fig. 16.2-2).

---

## Problemas al final del capítulo (p. 677–679)

La numeración continúa la de los ejercicios del texto (16.1-1 a 16.1-5 y 16.2-1, 16.2-2 están
resueltos/propuestos dentro de las secciones).

- **16.1-6 Donor-Electron Ionization Energies and Radii (p. 677).** Estimar $E_D$ y el radio de
  Bohr $r_1$ del electrón donor (§13.1A, Ej. 16.1-1) para: (a) Si, $m_c = 0.98m_0$,
  $\epsilon/\epsilon_0 = 12.3$; (b) GaAs, $0.07m_0$, 13; (c) GaN, $0.20m_0$, 6.25; (d) poliacetileno
  dopado con Na⁺, $m_c = m_0$, $\epsilon/\epsilon_0 = 3$. Comentar el papel de la excitación térmica y
  de la constante dieléctrica (los LED orgánicos operan por recombinación de excitones ligados).
- **16.1-7 Fermi Level of an Intrinsic Semiconductor (p. 677–678).** (a) Con (16.1-12) y
  (16.1-13), expresión de $E_f$ intrínseco; mostrar que cae exactamente en el centro del gap solo si
  $m_c = m_v$. (b) Expresión de $E_f$ de un semiconductor dopado en función del dopado y del $E_f$
  intrínseco de (a).
- **16.1-8 Electron–Hole Recombination Under Strong Injection (p. 678).** Con
  $\tau = 1/r\Delta n$ (inyección fuerte), si $R = 0$ para $t\ge t_0$, hallar $\Delta n(t)$ y mostrar
  que decae como ley de potencias, no exponencial.
- **16.1-9 Bowing Parameters for Ternary Semiconductors (p. 678).** La constante de red varía
  linealmente (Vegard) pero $E_g$ se curva:
  $E_g^{ABC}(x) = E_g^{AC}x + E_g^{BC}(1-x) - bx(1-x)$, $b$ = **parámetro de bowing**. Con las
  Figs. 16.1-7/8, estimar $b$ para Al$_x$Ga$_{1-x}$As, GaAs$_{1-x}$P$_x$, Al$_x$Ga$_{1-x}$N,
  In$_x$Ga$_{1-x}$N, Al$_x$In$_{1-x}$N, Hg$_x$Cd$_{1-x}$Te. ¿Qué significa $b$ para el ajuste de red a un
  sustrato?
- **\*16.1-10 Energy Levels in a GaAs/AlGaAs Quantum Well (p. 678).** (a) Dibujar a escala el
  diagrama de bandas de un MQW GaAs/Al$_{0.3}$Ga$_{0.7}$As: $E_g$(GaAs) = 1.42 eV, +12.47 meV por
  1 % de Al; el pozo de conducción es ≈ 60 % de la profundidad total. (b) Con esa profundidad y los
  niveles del pozo finito de la Fig. 16.1-25(b) [$(mV_0d^2/2\hbar^2)^{1/2} = 4$], hallar el ancho
  $d$ del pozo de conducción de GaAs, con $m_c\approx 0.07m_0 = 0.64\times10^{-31}$ kg.
- **16.2-3 Validity of the Approximation for Absorption/Emission Rates (p. 678).** La tasa
  $r_{sp}(\nu) = \int[(1/\tau_r)g_{\nu_0}(\nu)]f_e(\nu_0)\varrho(\nu_0)d\nu_0$ se aproximó con
  $g_{\nu_0}(\nu)\approx\delta(\nu-\nu_0)$. (a) Mostrar que es satisfactoria para GaAs graficando
  $g_{\nu_0}(\nu)$, $f_e(\nu_0)$ y $\varrho(\nu_0)$ a 300 K y comparando anchos ($T_2\approx 1$ ps).
  (b) Repetir para la tasa de absorción en equilibrio térmico.
- **16.2-4 Peak Spontaneous Emission Rate in Thermal Equilibrium (p. 678).** (a) Energía $h\nu_p$ de
  máxima emisión espontánea directa banda a banda en equilibrio ($E_f$ en el gap, lejos de los bordes).
  (b) Mostrar que la tasa pico (fotones/s·Hz·cm³) es
  $r_{sp}(\nu_p) = \dfrac{D_0}{\sqrt{2e}}\sqrt{kT} = \dfrac{2(m_r)^{3/2}}{\sqrt e\,\pi\hbar^2\tau_r}\sqrt{kT}\exp(-E_g/kT)$
  (aquí $e$ es la base de los logaritmos naturales). (c) Efecto del dopado. (d) Valor en GaAs a
  300 K con $\tau_r = 0.4$ ns, $m_c = 0.07m_0$, $m_v = 0.50m_0$, $E_g = 1.42$ eV.
  (Para (a): maximizar $\sqrt{x}\,e^{-x/kT}$ con $x = h\nu - E_g$ → $h\nu_p = E_g + kT/2$.)
- **16.2-5 Radiative Recombination Rate in Thermal Equilibrium (p. 679).** (a) Mostrar que
  $\int_0^\infty r_{sp}(\nu)d\nu = D_0\dfrac{\sqrt\pi}{2h}(kT)^{3/2} = \dfrac{(m_r)^{3/2}}{\sqrt2\,\pi^{3/2}\hbar^3\tau_r}(kT)^{3/2}\exp(-E_g/kT)$
  (fotones/s·cm³), con $E_f$ en el gap lejos de los bordes; usar
  $\int_0^\infty x^{1/2}e^{-\mu x}dx = (\sqrt\pi/2)\mu^{-3/2}$. (b) Comparar con la tasa pico del
  Prob. 16.2-4 × el ancho $2kT/h$ de la Fig. 16.2-9. (c) Igualando a $r_r np = r_r n_i^2$ (§16.1D) y
  con (16.1-15), obtener
  $r_r = \dfrac{\sqrt2\,\pi^{3/2}\hbar^3}{(m_c+m_v)^{3/2}(kT)^{3/2}\tau_r}$. (d) Evaluar $r_r$ para GaAs
  a 300 K ($m_c = 0.07m_0$, $m_v = 0.5m_0$, $\tau_r = 0.4$ ns) y comparar con la Tabla 16.1-4
  ($r_r\approx 10^{-10}$ cm³/s).

---

## Relación con Óptica No Lineal

**Para el curso (temas de ONL):**
- *Absorción y dispersión; Kramers–Kronig.* La §16.2E (p. 674) es el nexo directo: el índice del
  semiconductor sigue de $\alpha(\nu)$ por K–K (§5.5B, Ap. B). El borde de absorción
  $\alpha\propto\sqrt{h\nu-E_g}/(h\nu)^2$ (16.2-29) y la cola de Urbach (p. 672) fijan la dispersión
  fuerte cerca de $E_g$ y explican por qué $n$ es grande y decrece con $\lambda$ (Fig. 16.2-12). El
  **índice de grupo** $N > n$ de GaAs (Fig. 16.2-12) es el mismo $n_g$ que entra en la GVD de pulsos
  en medios dispersivos.
- *Susceptibilidad resonante y ganancia.* Las tasas (16.2-17)–(16.2-19) y el coeficiente de ganancia
  (16.2-24) son la versión semiconductor de $\gamma_0(\nu) = N\sigma(\nu)$ de los láseres (cap. 14):
  $\varrho(\nu)f_g(\nu)$ reemplaza a $Ng(\nu)$. Ganancia requiere $E_{fc}-E_{fv}>h\nu$ (16.2-12). Es la
  base de los amplificadores ópticos de semiconductor (SOA), cuyas no linealidades de ganancia
  (saturación, XGM, XPM, FWM en SOA) se citan en el curso.
- *Absorción de dos fotones (TPA) y $\chi^{(3)}$ imaginario.* El capítulo **no** trata la TPA
  (Saleh la aborda en el cap. 21, Óptica no lineal); pero da los ingredientes: para TPA hace falta
  $2h\nu > E_g$ con $h\nu < E_g$. Con la Tabla 16.1-2: Si ($E_g = 1.12$ eV, $\lambda_g = 1.11$ µm)
  tiene TPA en toda la banda telecom (1.55 µm → $2h\nu = 1.6$ eV > 1.12 eV), y los portadores
  generados por TPA producen a su vez **absorción por portadores libres** (FCA, mecanismo intrabanda
  de la p. 661: ∝ concentración de portadores, decreciente con $h\nu$ como ley de potencias) y cambio
  de índice por portadores (dispersión de portadores libres, por K–K). Esto limita la potencia en
  guías de Si. GaAs ($E_g = 1.42$ eV) también tiene TPA a 1.55 µm ($2h\nu = 1.6$ eV > 1.42 eV).
- *Índice dependiente de la intensidad y relajación.* Los tiempos del capítulo son los que fijan la
  dinámica de las no linealidades de portadores: relajación intrabanda $<1$ ps (p. 645; $T_2\sim 1$ ps
  → ensanchamiento colisional de 318 GHz, p. 668) frente a recombinación $\tau\sim$ ns (Tabla 16.1-4;
  en Si $\tau\approx 100$ ns). Esto distingue el Kerr electrónico (fs) de los efectos por portadores
  (ns), importantes al interpretar SPM/XPM en guías de semiconductor.
- *Pozos cuánticos y no linealidades grandes.* §16.2D (p. 673): transiciones intersubbanda y de
  minibanda tienen relajación rápida y **grandes no linealidades** → conmutación totalmente óptica;
  excitones estables a 300 K en MQW (moduladores de electroabsorción). Referencia útil de la lista:
  Schmitt-Rink, Chemla & Miller 1989, *Linear and Nonlinear Optical Properties of Semiconductor
  Quantum Wells*.
- *Cristales y simetría.* Zincblenda (GaAs, InP…) no es centrosimétrica → tiene $\chi^{(2)}$
  (base de SHG/DFG en GaAs); diamante (Si, Ge) es centrosimétrica → $\chi^{(2)} = 0$ en volumen, solo
  $\chi^{(3)}$ (Kerr, TPA, Raman, FWM). Wurtzita (GaN, AlN) tampoco es centrosimétrica. El capítulo
  da las estructuras (Tabla 16.1-2, p. 636) pero no discute $\chi^{(2)}$; conviene cruzarlo con el
  cap. 21 y con Boyd.
- *Raman.* Los fonones (p. 660–661, 666) que asisten las transiciones indirectas son los mismos
  fonones ópticos del Raman estimulado en Si (15.6 THz) y de la banda Raman en fibras.
- *Haz gaussiano, ondas EM, polarización.* Sin contenido directo; solo el paralelismo de la densidad
  de estados electrónica con el conteo de modos del resonador EM (§10.3, p. 639–640).

**Para el proyecto final (anillos add-drop en Si₃N₄, dispersión, supercontinuo, sensado):**
- *Silicio frente a Si₃N₄ como plataforma.* Del capítulo: Si tiene $E_g = 1.12$ eV, $n\approx 3.5$
  cerca del gap (Tabla 16.2-1), es transparente en ≈ 1.1–12 µm (Fig. 16.2-2) **pero** sufre TPA a
  1.55 µm (por $2h\nu > E_g$) y FCA por los portadores generados (p. 661), con tiempo de vida de
  portadores ~100 ns (Tabla 16.1-4) que limita la potencia circulante en un anillo de alto $Q$ y
  frena la generación de supercontinuo. Si₃N₄ no es un semiconductor del capítulo (es un dieléctrico
  con $E_g\approx 5$ eV, $n\approx 2.0$; dato externo, no de Saleh cap. 16): no tiene TPA ni FCA en
  telecom, por eso se prefiere para supercontinuo y Kerr aunque su $n_2$ sea menor. El argumento
  de "por qué Si₃N₄" del informe puede citar Saleh §16.2A (p. 661–662, mecanismos y Fig. 16.2-2) y
  Tabla 16.1-2 (p. 636).
- *Dispersión de guías.* El índice de grupo $N$ de GaAs (Fig. 16.2-12, p. 674) y la relación K–K
  (§16.2E) justifican que la dispersión del material cerca del gap sea grande; para Si₃N₄, lejos de
  su gap, la dispersión del material es pequeña y la geométrica domina (lo que se ingenieriza en las
  guías del proyecto).
- *Sensado de índice de refracción.* El capítulo recuerda que $n$ depende de $T$ y del dopado
  (p. 674) → en una plataforma de Si el efecto termoóptico y de portadores compite con la señal de
  sensado; en Si₃N₄ el coeficiente termoóptico es menor (dato externo).
- *Detección.* Los fotodiodos $p$–$i$–$n$ (§16.1E, p. 653) y la absorción en Si/Ge (Fig. 16.2-3)
  son lo que se usa para leer el espectro de salida del anillo; InGaAs (ajustado en red a InP,
  p. 635) para 1.55 µm.
