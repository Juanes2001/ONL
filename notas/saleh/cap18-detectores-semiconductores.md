# Capítulo 18 — Semiconductor Photon Detectors (Saleh & Teich, 2.ª ed.)

Páginas del libro 748–803 (PDF 770–825). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007,
cap. 18. Todas las páginas citadas son páginas del libro (página PDF = libro + 22).

Notación del libro usada aquí: η eficiencia cuántica, 𝕽 responsividad (A/W), Φ flujo de
fotones (fotones/s), P potencia óptica (W), λ_o longitud de onda en el vacío, G ganancia,
Ḡ ganancia media, k razón de ionización, F factor de exceso de ruido, B ancho de banda
eléctrico (Hz), T = 1/2B tiempo de resolución, m̄ número medio de fotoelectrones en T,
σ_q parámetro de ruido de circuito (adimensional). Unidades SI; λ_o en µm cuando se
usa la regla 𝕽 = ηλ_o/1.24.

---

## Resumen del capítulo

El capítulo describe los fotodetectores que convierten flujo de fotones en corriente
eléctrica. Distingue el fotoefecto externo (fotoemisión: fototubos, PMT, placas
microcanal) del interno (fotoconductividad: fotoconductores, fotodiodos p–n y p–i–n,
fotodiodos de avalancha) y define las figuras de mérito comunes: eficiencia cuántica η,
responsividad 𝕽 = ηeG/hν (A/W) y tiempo de respuesta (dispersión del tiempo de
tránsito según el teorema de Ramo, constante RC, tiempo de formación de avalancha).
Trata la ganancia de fotoconductores (G = τ/τ_e), los modos de operación del fotodiodo,
las heteroestructuras y los fotodiodos Schottky, y deduce la ganancia del APD
(18.4-8) a partir de los coeficientes de ionización. Describe brevemente los SPAD y los
detectores matriciales (FPA, CCD, CMOS). La sección 18.6, la más extensa, construye
la teoría del ruido: ruido de fotones y fotoelectrones (Poisson, SNR = m̄), ruido de
disparo de la fotocorriente σ_i² = 2eīB, ruido de ganancia con factor de exceso F
(para APD, F = kḠ + (1−k)(2−1/Ḡ)), ruido térmico 4kTB/R, el parámetro σ_q, la SNR
del receptor óptico (18.6-34)/(18.6-36), cuándo conviene un APD y su ganancia óptima,
la sensibilidad del receptor (18.6-45)–(18.6-47) y la tasa de error de bit (10 fotones/bit
ideal; m̄_a ≈ 18F para APD con aproximación gaussiana).

---

## Secciones

### Introducción (p. 749)

- Un fotodetector mide flujo de fotones o potencia óptica convirtiendo la energía de los
  fotones absorbidos en una forma medible. Dos clases: **detectores fotoeléctricos**
  (fotoefecto) y **detectores térmicos** (conversión a calor; lentos e ineficientes, aunque
  los arreglos térmicos han mejorado mucho para imagen en el IR medio). (p. 749)
- El fotoefecto tiene dos formas: **externo** (fotoemisión: los electrones escapan del
  material) e **interno** (fotoconductividad: los portadores quedan dentro del material y
  aumentan su conductividad). (p. 749)
- Fuentes de ruido anunciadas para §18.6: ruido de fotones, ruido de fotoelectrones,
  ruido de ganancia, ruido de circuito del receptor. (p. 749)

### 18.1 Photodetectors (p. 749)

#### 18.1A External and Internal Photoeffects (p. 749)

**Emisión fotoeléctrica (p. 749–751).** En un metal, los electrones emitidos desde el nivel
de Fermi tienen energía cinética máxima (ecuación de Einstein)

$$E_{\max} = h\nu - \mathbb{W} \qquad (18.1\text{-}1)$$

donde 𝕎 es la **función de trabajo fotoeléctrica** (diferencia entre el nivel de vacío y el
nivel de Fermi). La menor 𝕎 metálica (Cs) es ≈ 2 eV → detectores de fotoefecto externo con
metales puros sirven en el visible y UV. (p. 750)

En un semiconductor intrínseco (Fig. 18.1-1b) los fotoelectrones salen de la banda de valencia:

$$E_{\max} = h\nu - \mathbb{W} = h\nu - (E_g + \chi) \qquad (18.1\text{-}2)$$

con E_g energía de banda prohibida y χ **afinidad electrónica** (vacío − fondo de la banda de
conducción). E_g + χ puede ser tan pequeño como 1.4 eV (NaKCsSb, fotocátodo S-20) → IR
cercano. Semiconductores de **afinidad electrónica negativa (NEA)** (p. ej. GaAs:Cs): el borde
de la banda de conducción queda por encima del nivel de vacío en el bulk, así que basta hν > E_g;
mejor η y menor corriente oscura. Fotocátodo S-1 (inhomogéneo/óxidos): hasta λ ≈ 1 µm. (p. 750)

Dispositivos (p. 751): **fotodiodo de vacío / fototubo** (fotocátodo + ánodo; el fotocátodo
puede ser opaco en modo reflexión o semitransparente en modo transmisión);
**tubo fotomultiplicador (PMT)**: cascada de **emisión secundaria** en **dínodos** a potenciales
crecientes, amplificación hasta 10⁸, detecta y cuenta fotones individuales con gran rango
dinámico, pero es voluminoso y requiere alta tensión; **placa microcanal**: millones de
capilares (∅ ≈ 10 µm) en una placa de vidrio de ≈ 1 mm, cada pared actúa como dínodo
continuo; con fósforo en la salida forma un **intensificador de imagen** (Fig. 18.1-2).

**Fotoconductividad (p. 752).** El fotón absorbido *genera* un par electrón–hueco (Fig.
18.1-3); un campo eléctrico aplicado los *transporta* y produce corriente. El **fotodiodo**
semiconductor es una unión p–n: los fotones absorbidos en la capa de agotamiento generan
pares que derivan en sentidos opuestos por el campo local. Los **APD** añaden *ganancia*
por ionización por impacto. Tres procesos básicos (recuadro, p. 752):
1. *Generación*: fotones absorbidos generan portadores libres.
2. *Transporte*: el campo aplicado los mueve y produce corriente en el circuito.
3. *Ganancia*: en APD el campo intenso libera más portadores por ionización por impacto.

#### 18.1B General Properties (p. 752)

Los detectores de fotones y las fuentes semiconductoras son dispositivos inversos; comparten
materiales (cap. 16) y todas las medidas de desempeño tienen contraparte en las fuentes
(cap. 17). (p. 753)

**Eficiencia cuántica (p. 753).** η (0 ≤ η ≤ 1): probabilidad de que un fotón incidente genere
un par fotoportador que contribuya a la corriente; con muchos fotones, flujo de pares útiles
dividido por flujo de fotones incidentes. Recuadro:

$$\eta = (1-\mathcal{R})\,\zeta\,[1-\exp(-\alpha d)] \qquad (18.1\text{-}3)\ \text{Quantum Efficiency}$$

- 𝓡: reflectancia de potencia en la superficie (reducible con capas antirreflejo; algunas
  definiciones de η la excluyen).
- ζ: fracción de pares que evitan recombinarse en la superficie y contribuyen a la
  fotocorriente.
- α: coeficiente de absorción (cm⁻¹, §16.2C); d: profundidad del detector. El tercer factor
  es ∫₀ᵈ e^{−αx}dx / ∫₀^∞ e^{−αx}dx = 1 − e^{−αd}, la fracción absorbida en el volumen
  (Fig. 18.1-4, p. 754).

*Dependencia con la longitud de onda (p. 753–754):* η depende de λ principalmente vía α(λ)
(Fig. 16.2-3). Para λ_o ≥ λ_g = hc_o/E_g no hay absorción: λ_g es el **límite de longitud de
onda larga**. Para λ_o muy corta, η también cae porque α es grande (α = 10⁴ cm⁻¹ → casi toda
la luz se absorbe en 1/α = 1 µm, cerca de la superficie, donde la vida de recombinación es
corta). Valores de E_g y λ_g: Tabla 16.1-2 y Figs. 16.1-7/16.1-8.

*Fotodetectores de cavidad resonante (p. 754):* colocar el detector dentro de una cavidad
hace que la luz lo atraviese varias veces; equivale a aumentar d y sube η.

**Responsividad (p. 754–755).** Relaciona la corriente i_p con la potencia óptica P. Si cada
fotón generara un par, Φ (fotones/s) daría i_p = eΦ, y P = hνΦ daría i_p = eP/hν. Con η:

$$i_p = \eta e \Phi = \frac{\eta e P}{h\nu} \equiv \mathfrak{R} P \qquad (18.1\text{-}4)$$

Recuadro:

$$\mathfrak{R} = \frac{\eta e}{h\nu} = \eta\,\frac{\lambda_o}{1.24} \qquad (18.1\text{-}5)\ \text{Photodetector Responsivity (A/W; } \lambda_o \text{ en µm)}$$

Distinguir de la responsividad del LED (W/A) de (17.1-28). 𝕽 ∝ η y ∝ λ_o: para η = 1 y
λ_o = 1.24 µm, 𝕽 = 1 A/W = 1 nA/nW (Fig. 18.1-5, p. 755: 𝕽 vs λ_o con η como parámetro).
La proporcionalidad a λ_o surge porque 𝕽 se define respecto a potencia, mientras el detector
responde al flujo de fotones Φ = P/hν = Pλ_o/hc_o (los detectores térmicos responden a
potencia y su 𝕽 es independiente de λ_o). La región de crecimiento con λ_o está limitada por
η(λ). Con potencia excesiva el detector se **satura**: límite del **rango dinámico lineal**.
(p. 755)

**Dispositivos con ganancia (p. 755).** Si cada par produce una carga q ≠ e en el circuito:

$$G \equiv q/e \qquad (18.1\text{-}6)$$

(puede ser > 1 o < 1). Recuadros:

$$i_p = \eta q \Phi = \eta G e \Phi = \frac{\eta G e P}{h\nu} \qquad (18.1\text{-}7)\ \text{Photocurrent with Gain}$$

$$\mathfrak{R} = \frac{\eta G e}{h\nu} = \eta G \frac{\lambda_o}{1.24} \qquad (18.1\text{-}8)\ \text{Responsivity with Gain (A/W; } \lambda_o \text{ en µm)}$$

G (ganancia del dispositivo) ≠ η (probabilidad de que un fotón produzca un par detectable).
(p. 755–756)

**Tiempo de respuesta (p. 756–758).**

*Dispersión del tiempo de tránsito.* Con campo E constante, los portadores aceleran y
chocan con la red (aceleración a = eE/m, tiempo medio entre colisiones τ_col = tiempo de
relajación), de modo que derivan con **velocidad de deriva** v = eτ_col E/m:

$$v = \mu E \qquad (18.1\text{-}9)$$

con μ = eτ_col/m la **movilidad**. Para un par generado en x en un material de longitud w con
tensión V (campo E = V/w), el trabajo −QE dx hecho por el campo iguala la energía del
circuito i(t)V dt, de donde el **teorema de Ramo** (recuadro):

$$i(t) = -\frac{Q}{w}\,v(t) \qquad (18.1\text{-}10)\ \text{Ramo's Theorem}$$

Hueco hacia la izquierda con v_h: i_h = −e(−v_h)/w = ev_h/w; electrón hacia la derecha:
i_e = −(−e)v_e/w = ev_e/w. Cada portador contribuye mientras se mueve: el hueco durante
x/v_h, el electrón durante (w−x)/v_e. En semiconductores v_e > v_h ⇒ anchura total ≈ x/v_h.
Esta duración finita es la **dispersión del tiempo de tránsito**. La carga total inducida es e
(no 2e):

$$q = e\frac{v_h}{w}\frac{x}{v_h} + e\frac{v_e}{w}\frac{w-x}{v_e} = e\left(\frac{x}{w} + \frac{w-x}{w}\right) = e \qquad (18.1\text{-}11)$$

independiente de x (Fig. 18.1-6, p. 757). Con generación uniforme en todo el material (Fig.
18.1-7, p. 757; Prob. 18.1-4), para v_h < v_e la anchura total es w/v_h; i(t) es la respuesta al
impulso de un detector iluminado uniformemente (Apéndice B, §B.1). Interpretación (p. 757):
la carga se "jala" lentamente del alambre de un lado y se "empuja" en el otro.

*Ley de Ohm (p. 757–758).* Con densidad de carga uniforme ϱ en volumen Aw, (18.1-10) da
i(t) = −ϱAv(t) y J = ϱv. Recuadros:

$$\mathcal{J} = \varrho\,\mathbf{v} \qquad (18.1\text{-}12)\ \text{Current Density}$$

$$\sigma = \varrho\mu = e\varrho\,\tau_{\rm col}/m = N e^2 \tau_{\rm col}/m \qquad (18.1\text{-}13)$$

(N portadores por unidad de volumen, §5.5D); en general σ es un tensor:

$$\mathcal{J} = \boldsymbol{\sigma}\,\mathcal{E} \qquad (18.1\text{-}14)\ \text{Ohm's Law}$$

Para un conductor homogéneo de área A y longitud w: i = (σA/w)V = GV = V/R, es decir
V = iR (18.1-15).

*Constante RC (p. 758).* R y C del detector y su circuito dan la constante τ_RC = RC, que
integra la corriente y alarga la respuesta al impulso. La respuesta al impulso con tránsito *y*
RC es la convolución de i(t) de la Fig. 18.1-7 con (1/RC)exp(−t/RC). Los detectores suelen
tener un **producto ganancia–ancho de banda** fijo: más ganancia ⇒ menos ancho de banda.

### 18.2 Photoconductors (p. 758)

La conductividad σ aumenta en proporción a Φ; un campo externo transporta los portadores.
Se registra la fotocorriente i_p ∝ Φ o la caída de tensión en una resistencia de carga R en
serie (Fig. 18.2-1a, p. 759). (p. 758)

#### 18.2A Intrinsic Materials (p. 759)

Absorción banda a banda si hν > E_g. Forma de losa o película delgada; contactos
**interdigitados** en la misma cara para maximizar la luz que llega y minimizar el tiempo de
tránsito (Fig. 18.2-1b). Cálculo del aumento de conductividad en un volumen wA: tasa de
generación de pares por unidad de volumen R = ηΦ/wA; en estado estacionario R = Δn/τ
(τ: vida de recombinación de portadores en exceso), así Δn = ητΦ/wA, Δϱ = eΔn,
Δσ = Δϱμ = eΔnμ:

$$\Delta\sigma = \frac{\eta e \tau(\mu_e + \mu_h)}{wA}\,\Phi \qquad (18.2\text{-}1)$$

Con J_p = ΔσE, v_e = μ_eE, v_h = μ_hE: i_p = AJ_p = [ηeτ(v_e+v_h)/w]Φ; para v_h ≪ v_e y
definiendo el tiempo de tránsito del electrón τ_e = w/v_e:

$$i_p \approx \eta\,(\tau/\tau_e)\,e\,\Phi \qquad (18.2\text{-}2)$$

Comparando con (18.1-7), la razón τ/τ_e es la ganancia G. (p. 759)

**Ganancia (p. 760).** Si los electrones son más rápidos y τ es larga, el electrón sale por el
contacto antes de que el hueco llegue al otro; la continuidad de corriente obliga al circuito a
inyectar otro electrón, y así hasta que el hueco se recombina. Número esperado de viajes:

$$G = \tau/\tau_e \qquad (18.2\text{-}3)$$

y q = Ge > e. Si τ < τ_e, G < 1 (cada par aporta una fracción de e; la carga total se conserva
sobre muchos pares). Valores típicos: w = 1 mm, v_e ≈ 10⁷ cm/s ⇒ τ_e ≈ 10⁻⁸ s; τ va de 10⁻¹³ s
a muchos segundos, así G va de ≪ 1 a ≫ 1, pero en general **no supera ≈ 10⁶** (corriente
limitada por carga espacial, ionización por impacto, ruptura dieléctrica). (p. 760)

**Respuesta espectral (p. 760).** Gobernada por η(λ); operan en el IR por transiciones banda
a banda; más allá de ≈ 2 µm hay que enfriar para evitar excitación térmica.

**Tiempo de respuesta (p. 760–761).** Limitado por tránsito y RC; el tiempo de respuesta de
transporte ≈ τ, así el ancho de banda B ∝ 1/τ mientras G ∝ τ: el producto **GB es
aproximadamente independiente de τ**, con valores típicos hasta ≈ 10⁹. (p. 761)

#### 18.2B Extrinsic Materials (p. 761)

Semiconductores dopados: el fotón libera un electrón ligado a un donante (hacia la banda de
conducción) o un hueco ligado a un aceptor (hacia la banda de valencia), Fig. 16.2-1(b). Las
energías de activación E_A son muy bajas ⇒ límites λ_A = hc_o/E_A grandes; hay que enfriar
(He líquido, 4 K). Tabla 18.2-1 (ver sección de tablas). La responsividad crece ≈ linealmente
con λ_o según (18.1-8), alcanza un máximo justo por debajo de λ_A y cae rápido después
(Fig. 18.2-2, Ge:Hg, Ge:Cu, Ge:Zn, Ge:Ga, Ge:Ga tensionado). η puede ser alta (≈ 0.5 para
Ge:Cu) aunque la ganancia sea baja (G ≈ 0.03 para Ge:Hg). (p. 761)

#### 18.2C Heterostructures (p. 762)

**QWIP (quantum-well infrared photodetector)**: el fotón IR libera el electrón del nivel ligado
de un pozo cuántico al continuo (Fig. 18.2-3: barreras AlGaAs, pozos GaAs tipo n). Alta
responsividad en λ_o ≈ 4–20 µm, alta velocidad, requieren enfriamiento. **QDIP** (puntos
cuánticos): detección IR multibanda vía transiciones intersubbanda. (p. 762)

### 18.3 Photodiodes (p. 762)

#### 18.3A The p–n Photodiode (p. 762)

Unión p–n (§16.1E) cuya corriente inversa aumenta al absorber fotones. Sin ganancia, pero
más rápidos que los fotoconductores. Solo donde hay campo (capa de agotamiento) los
portadores se transportan de manera dirigida. Tres regiones de generación (Fig. 18.3-1, p.
762; lista p. 763):
1. **Capa de agotamiento (región 1)**: deriva rápida en sentidos opuestos (campo n→p;
   electrones al lado n, huecos al lado p); fotocorriente externa en sentido inverso (n→p);
   cada par genera un pulso de área e (G = 1), sin recombinación.
2. **Lejos de la capa de agotamiento (región 3)**: no hay campo, se recombinan sin aportar.
3. **Cerca de la capa de agotamiento (región 2)**: pueden entrar por difusión y aportar e.

Materiales: los de la Tabla 16.1-2 más compuestos binarios, ternarios y cuaternarios (SiC,
InGaAs, InGaAsP). Iluminación normal a la unión (en lugar de paralela): la corriente de
difusión adicional sube η, contrarrestada por el menor espesor. (p. 763)

**Tiempo de respuesta (p. 763).** Tránsito en la capa de agotamiento (w_d/v_e, w_d/v_h) y RC
como en §18.1B; además la **difusión** (lenta) de portadores generados fuera pero cerca de la
capa de agotamiento, limitada por las vidas τ_p (electrones en p) y τ_n (huecos en n); el p–i–n
la reduce. Los fotodiodos no sufren los efectos de atrapamiento de los fotoconductores.

**Polarización (p. 763–765).** Relación i–V:

$$i = i_s\left[\exp\left(\frac{eV}{kT}\right) - 1\right] - i_p \qquad (18.3\text{-}1)$$

(la i–V usual de (16.1-32) con fotocorriente −i_p ∝ Φ; Fig. 18.3-2). Tres modos (p. 764):
- **Circuito abierto (fotovoltaico)** (Fig. 18.3-3): aparece una fotovoltaje V_p que crece con Φ;
  modo de las celdas solares; responsividad en V/W.
- **Cortocircuito** (V = 0, Fig. 18.3-4): la corriente es i_p.
- **Polarización inversa (fotoconductivo)** (Fig. 18.3-5a sin carga, 18.3-5b con R_L: punto de
  operación sobre la recta de carga que pasa por −V_B y −V_B/R_L).

Razones para polarizar fuertemente en inversa (p. 764): mayor campo ⇒ mayor velocidad de
deriva ⇒ menor tiempo de tránsito; capa de agotamiento más ancha ⇒ menor capacidad de
unión ⇒ mejor respuesta temporal; mayor área fotosensible.

#### 18.3B The p–i–n Photodiode (p. 765)

Capa intrínseca (ligeramente dopada) entre p y n (§16.1E), Fig. 18.3-6 (bandas, carga fija,
campo: el campo es uniforme en la región i). Ventajas (p. 765): mayor anchura de la región
con campo (más área para capturar luz); menor capacidad de unión y por tanto menor RC
(aunque el tiempo de tránsito crece con la anchura); menor razón longitud de difusión /
longitud de deriva ⇒ más corriente transportada por deriva rápida.

Fig. 18.3-7 (p. 766): responsividad de p–i–n de Si comerciales vs ideal (η = 1); el máximo
está a λ más corta que λ_g porque el Si es de banda indirecta (transiciones desde la banda de
valencia hacia estados bien por encima del borde de la banda de conducción, Fig. 16.2-8).
Con buen antirreflejo η → 1.

#### 18.3C Heterostructures (p. 766)

Heterouniones de dos semiconductores de distinto E_g. El material de banda ancha (E_g > hν)
es transparente y actúa como **capa ventana**, minimizando absorción fuera de la región de
agotamiento. Sistemas (p. 766):
- Al_xGa_{1−x}As/GaAs: 0.7–0.87 µm.
- In_xGa_{1−x}As/InP: 1300–1600 nm (comunicaciones, §24.1D). **p–i–n de InGaAs típico a
  1550 nm: η ≈ 0.75, 𝕽 ≈ 0.9 A/W.**
- Hg_xCd_{1−x}Te/CdTe: IR medio, 3–17 µm (visión nocturna, imagen térmica).
- Cuaternarios In_{1−x}Ga_xAs_{1−y}P_y/InP y Ga_{1−x}Al_xAs_ySb_{1−y}/GaSb: 0.92–1.7 µm; el
  cuarto elemento permite ajustar E_g manteniendo el acople de red.

**Fotodiodos de barrera Schottky (p. 766–767).** Metal–semiconductor: película metálica
semitransparente (o aleación metal-semiconductor) en lugar de la capa p (o n). Responden a
hν > 𝕎 − χ (altura de la barrera Schottky), Fig. 18.3-8 (p. 767); ejemplos Au sobre Si-n
(visible), PtSi sobre Si-p (UV al IR). Ventajas: materiales que no se pueden dopar de ambos
tipos; para UV/visible con α alto la capa de agotamiento está justo en la superficie, eliminando
la recombinación superficial; mayor velocidad al no requerir capas gruesas (la baja
resistencia del metal evita subir RC); dispositivos de portadores mayoritarios ⇒ respuesta en
ps, **anchos de banda ≈ 100 GHz**. Fig. 18.3-9 (p. 768): 𝕽 vs λ_o para p–i–n (Ag-ZnS, SiC,
GaAs, Si, Ge, InGaAs/InP) y Schottky (Au-InGaAs); respuestas en decenas de ps, B ≈ 50 GHz.

### 18.4 Avalanche Photodiodes (p. 767)

Un APD convierte cada fotón detectado en una *cascada* de pares; fotodiodo con fuerte
polarización inversa en el que el campo de la unión imparte energía suficiente para
**ionización por impacto**. (p. 767)

#### 18.4A Principles of Operation (p. 768)

Fig. 18.4-1 (p. 768): el fotón se absorbe (punto 1); el electrón acelera, choca con la red y
alcanza una velocidad de saturación media; si acumula energía > E_g puede ionizar (punto 2);
los huecos generados viajan hacia la izquierda y también pueden ionizar (punto 3).

**Coeficientes de ionización (p. 769).** α_e, α_h: probabilidades de ionización por unidad de
longitud (cm⁻¹); 1/α_e, 1/α_h: distancia media entre ionizaciones. Crecen con el campo y
decrecen con la temperatura. **Razón de ionización**:

$$\mathbb{k} = \frac{\alpha_h}{\alpha_e} \qquad (18.4\text{-}1)$$

Si k ≪ 1 solo ionizan electrones: el proceso avanza de p a n y termina cuando todos los
electrones llegan al lado n. Si k ≈ 1 hay realimentación (huecos generan electrones y
viceversa), que aumenta la ganancia pero es indeseable: consume tiempo (reduce B), es
aleatoria (más ruido), y puede ser inestable (ruptura de avalancha). Regla: inyectar el
portador con mayor coeficiente de ionización en el borde correspondiente (electrón en el
borde p con k lo más pequeño posible; hueco en el borde n con k lo más grande posible); el
caso ideal de multiplicación de un solo portador es k = 0 o ∞. (p. 769)

**Diseño (p. 769–770).** Conflicto: región de absorción gruesa (tipo p–i–n) vs región de
multiplicación delgada (campo uniforme, evita microplasmas). Solución: **APD de absorción y
multiplicación separadas (SAM APD)**; p. ej. estructura **reach-through** p⁺–π–p–n⁺ (Fig.
18.4-2, p. 770): absorción en la región π (p muy ligera) ancha, multiplicación en la unión
p–n⁺ delgada; la polarización inversa hace que la capa de agotamiento alcance el contacto p⁺.

#### 18.4B Gain and Responsivity (p. 770)

*Un solo portador (α_h = 0, k = 0):* dJ_e(x) = α_e J_e(x) dx (18.4-2), dJ_e/dx = α_e J_e (18.4-3),
J_e(x) = J_e(0)exp(α_e x), y la ganancia G = J_e(w)/J_e(0):

$$G = \exp(\alpha_e w) \qquad (18.4\text{-}4)$$

(análoga al amplificador láser (14.1-7); Fig. 18.4-3, p. 771).

*Dos portadores (inyección solo de electrones):*

$$\frac{dJ_e}{dx} = \alpha_e J_e(x) + \alpha_h J_h(x) \qquad (18.4\text{-}5)$$

Por neutralidad de carga dJ_e/dx = −dJ_h/dx ⇒ J_e(x) + J_h(x) constante (Fig. 18.4-4). Sin
inyección de huecos en x = w, J_h(w) = 0:

$$J_e(x) + J_h(x) = J_e(w) \qquad (18.4\text{-}6)$$

$$\frac{dJ_e}{dx} = (\alpha_e - \alpha_h)J_e(x) + \alpha_h J_e(w) \qquad (18.4\text{-}7)$$

Solución para α_e ≠ α_h: G = (α_e − α_h)/{α_e exp[−(α_e − α_h)w] − α_h}, es decir (recuadro):

$$G = \frac{1-\mathbb{k}}{\exp[-(1-\mathbb{k})\alpha_e w] - \mathbb{k}} \qquad (18.4\text{-}8)\ \text{APD Gain}$$

Casos (p. 772): k = 0 recupera (18.4-4); k = ∞ da G = 1 (los electrones inyectados no
multiplican); k = 1 (indeterminada; de (18.4-7)) G = 1/(1 − α_e w), inestable en α_e w = 1.
Fig. 18.4-5: J_e(x) crece y J_h(x) decrece con x; Fig. 18.4-6: G vs α_e w para k = 0, 0.5, 1. La
responsividad se obtiene de (18.4-8) en (18.1-8).

Materiales (p. 772): los de la Fig. 18.3-9 con k mínimo (inyección de electrones) o máximo
(huecos). Si: k ≈ 0.1–0.2, con dispositivos de k ≈ 0.006; excelentes en 700–900 nm. InGaAs:
k mayor, pero alta responsividad y ruido moderado en 1300–1600 nm. Campos ≈ 10⁵ V/cm
(decenas de voltios). Al subir la tensión suben ganancia y corriente oscura (Fig. 18.4-7, p.
773: característica I–V de un SAM APD de InGaAs con tensión de *punchthrough* ≈ 18 V,
región de ganancia y tensión de ruptura ≈ 30 V; fotocorriente 10⁻⁸→10⁻⁴ A, corriente oscura
≈ 10⁻¹¹–10⁻⁹ A).

**EJEMPLO 18.4-1 (p. 772) — Ganancia en un APD de InGaAs.** Para 1300–1600 nm; operan
entre las tensiones de punchthrough y ruptura; **ganancias óptimas ≈ 10, corrientes oscuras
≈ 10⁻¹¹ A**. II–VI (HgCdTe) y IV–VI (PbSnTe) para λ más largas.

#### 18.4C Response Time (p. 773)

Además de tránsito, difusión y RC, el **tiempo de formación de la avalancha** (*avalanche
buildup time*). Fig. 18.4-8 (p. 774): región de absorción w_d y de multiplicación w_m; el
fotoelectrón (1) deriva con v_e hasta (2), ioniza en (3) y (4), los huecos (v_h) ionizan en (5) y
(6), el último hueco sale de la multiplicación en (7) y cruza la deriva hasta (8). Tiempo total:

$$\tau = \frac{w_d}{v_e} + \frac{w_d}{v_h} + \tau_m \qquad (18.4\text{-}9)$$

τ_m aleatorio; máximo para k = 0:

$$\tau_m = \frac{w_m}{v_e} + \frac{w_m}{v_h} \qquad (18.4\text{-}10)$$

Para G grande y 0 < k < 1 (inyección de electrones), orden de magnitud del promedio:

$$\tau_m \approx \frac{G\mathbb{k}\,w_m}{v_e} + \frac{w_m}{v_h} \qquad (18.4\text{-}11)$$

La carga total inducida (área bajo i_e + i_h) es Ge.

**EJEMPLO 18.4-2 (p. 774) — Tiempo de formación en un APD de Si.** w_d = 50 µm, w_m =
0.5 µm, v_e = 10⁷ cm/s, v_h = 5×10⁶ cm/s, G = 100, k = 0.1. (18.4-10): τ_m = 5 + 10 = 15 ps ⇒
(18.4-9): τ = 1020 ps = 1.02 ns. (18.4-11): τ_m = 60 ps ⇒ τ = 1065 ps = 1.07 ns. Un p–i–n con
los mismos w_d, v_e, v_h tiene tránsito w_d/v_e + w_d/v_h ≈ 1 ns: en Si τ_m es pequeño.

#### 18.4D Single-Photon Avalanche Diodes (SPADs) (p. 774)

**Conteo de fotones** mitiga el ruido de ganancia y de circuito porque la respuesta es binaria.
**SPAD** (APD en **modo Geiger**): polarizado de modo que un fotón precipita la ruptura de
avalancha, dando un gran pulso de corriente; luego hay que **apagar** (*quench*) la avalancha
(pasiva o activamente; la activa es más compleja pero permite tasas de conteo mucho
mayores). Parámetros (p. 774–775):
- Si: λ_o = 400–1000 nm, **η ≈ 75 %, cuentas oscuras ≈ 75 /s, resolución temporal ≈ 100 ps**.
- InGaAs/InP (1300–1600 nm): **η ≈ 20 %, cuentas oscuras ≈ 5000 /s, resolución ≈ 500 ps**;
  también Ge y Si–Ge.
- λ_o < 4 µm: absorción InAsSb + multiplicación AlGaAsSb sobre GaSb. UV: GaN y SiC (SiC
  tolera alta temperatura y ambientes hostiles).
- Compromiso general entre eficiencia y ancho de banda.
- **SSPD** (detectores superconductores de un fotón): banda ancha, bajo ruido, rápidos; un
  fotón crea un punto caliente no superconductor; requieren enfriamiento. (p. 775)

### 18.5 Array Detectors (p. 775)

Un arreglo registra simultáneamente los flujos de fotones de muchos puntos espaciales ⇒
versión electrónica de una imagen. Elementos = **píxeles** (fotoconductores, fotodiodos, APD
o bolómetros). **Arreglo de plano focal (FPA)**: arreglo 2D en el plano focal de un sistema
de imagen; **FPA híbrido**: la electrónica de lectura va en una capa bajo los elementos. Dos
tecnologías de lectura: **CCD** y **CMOS**. (p. 775)

Materiales y estructuras (p. 775–776):
- Microbolómetros (VOx, cientos de miles de píxeles de ≈ 25 µm, IR medio, a temperatura
  ambiente) para cámaras térmicas.
- Fotoconductores (InSb, HgCdTe) en IR medio; extrínsecos (Ge:Ga) en IR lejano.
- QWIP megapíxel: LWIR con GaAs/AlGaAs y MWIR con GaAs/InGaAs/AlGaAs; filtros
  espectrales estrechos para cientos de bandas.
- p–i–n de compuestos (InGaAs, HgCdTe) en visible e IR.
- Schottky (PtSi: desde el UV cercano hasta ≈ 6 µm, bajo η en el IR pero fáciles de fabricar y
  estables).
- APD en arreglos: pulsos sub-ns de varios voltios que disparan directamente el circuito CMOS
  digital (sin conversión A/D).
- SPAD en modo Geiger.
- Arreglos como detectores heterodinos con oscilador local (§24.5).

Circuitería de lectura (p. 776–777): **CCD** transfiere la carga de cada elemento a un canal
enterrado y la desplaza secuencialmente hasta una esquina del chip; **CMOS**: cada elemento
tiene varios MOSFET que amplifican y leen su señal; lectura individual; bajo consumo y bajo
costo (producción masiva de FPA).

### 18.6 Noise in Photodetectors (p. 777)

La corriente i es aleatoria con media ī = i_p = ηeΦ = 𝕽P; sus fluctuaciones se caracterizan
por σ_i² = ⟨(i − ī)²⟩ (para media cero, σ_i = ⟨i²⟩^{1/2}, valor rms). Fuentes (p. 777):
- *Ruido de fotones*: llegada aleatoria de los fotones (Poisson, §12.2).
- *Ruido de fotoelectrones*: con η < 1 cada fotón genera un par con probabilidad η.
- *Ruido de ganancia*: G aleatoria con media Ḡ (fotoconductores, APD, PMT).
- *Ruido de circuito del receptor*: resistencias y transistores.

Fig. 18.6-1 (p. 778): señal de entrada y detectada con las capas de ruido, (a) sin ganancia
(p–i–n) y (b) con ganancia (APD). Medidas de desempeño (p. 777–778):
- **SNR** de una variable aleatoria: media al cuadrado / varianza. SNR de i: ī²/σ_i²; del número
  de fotones: n̄²/σ_n².
- **Señal mínima detectable**: la media que da SNR = 1.
- **Factor de exceso de ruido** F: cuadrado medio / media al cuadrado; para la ganancia,
  F = ⟨G²⟩/⟨G⟩².
- **BER**: probabilidad de error por bit en un receptor digital.
- **Sensibilidad del receptor**: señal que da un SNR prescrito SNR₀ (SNR₀ = 1 ⇒ señal mínima
  detectable; se suele exigir SNR₀ = 10–10³, 10–30 dB). Para sistemas digitales: energía óptica
  mínima (número medio de fotones) por bit para un BER dado, a menudo 10⁻⁹.

No se incluyen explícitamente (p. 778): **ruido de fondo** (luz extraña: sol, luz ambiente;
grave en IR medio y lejano por la radiación térmica a temperatura ambiente, Fig. 13.4-4),
**ruido de corriente oscura** (pares generados térmicamente o por túnel, presentes sin luz),
corrientes de fuga y ruido 1/f.

#### 18.6A Photoelectron Noise (p. 778)

**Ruido de fotones (p. 778–779).** Φ = P/hν es la media; el número n de fotones en T es
aleatorio con media n̄ = ΦT. Para un láser ideal o una fuente térmica de ancho espectral
≫ 1/T, n es Poisson: σ_n² = n̄ (100 fotones ⇒ 100 ± 10). Recuadro:

$$\mathrm{SNR} = \bar n \qquad (18.6\text{-}1)\ \text{Photon-Number SNR}$$

Número mínimo detectable: n̄ = 1 fotón. Con T = 1 µs y λ_o = 1.24 µm ⇒ potencia mínima
detectable 0.16 pW; sensibilidad para SNR₀ = 10³ (30 dB): 1000 fotones ⇒ con T = 10 ns,
10¹¹ fotones/s = 16 nW a 1.24 µm. (p. 779)

**Ruido de fotoelectrones (p. 779).** Cada fotón produce un fotoevento con probabilidad η
(selección aleatoria del flujo). Número m de fotoelectrones en T:

$$\bar m = \eta \bar n \qquad (18.6\text{-}2)$$

Si n es Poisson, m también (argumento paralelo a §12.2D):

$$\sigma_m^2 = \bar m = \eta \bar n \qquad (18.6\text{-}3)$$

El ruido de fotoelectrones no es aditivo con el de fotones. Recuadro:

$$\mathrm{SNR} = \bar m = \eta \bar n \qquad (18.6\text{-}4)\ \text{Photoelectron-Number SNR}$$

Mínimo detectable: m̄ = 1 fotoelectrón = 1/η fotones; sensibilidad para SNR₀ = 10³: 1000
fotoelectrones = 1000/η fotones.

**Ruido de fotocorriente (p. 779–782).** Cada par genera un pulso de carga e y duración τ_p;
la corriente es la superposición de pulsos (Fig. 18.6-2, p. 780). Si los fotones son Poisson,
las fluctuaciones son **ruido de disparo** (*shot noise*). Con ganancia G, q = Ge. Vista
simplificada: m fotoelectrones en T = 1/2B (tiempo de resolución del circuito), pulsos
rectangulares de duración T ⇒ i = (e/T)m:

$$\bar\imath = \frac{e}{T}\bar m \qquad (18.6\text{-}5), \qquad \sigma_i^2 = \left(\frac{e}{T}\right)^2 \sigma_m^2 \qquad (18.6\text{-}6)$$

con m̄ = ηΦT = ηΦ/2B y σ_m² = m̄ (Poisson). Recuadros:

$$\bar\imath = e\eta\Phi \qquad (18.6\text{-}7)\ \text{Photocurrent Mean}$$

$$\sigma_i^2 = 2e\bar\imath B \qquad (18.6\text{-}8)\ \text{Photocurrent Variance}$$

$$\mathrm{SNR} = \frac{\bar\imath}{2eB} = \frac{\eta\Phi}{2B} = \bar m \qquad (18.6\text{-}9)\ \text{Photocurrent SNR}$$

SNR ∝ Φ y ∝ 1/B; igual al SNR del número de fotoelectrones (el circuito no añade
aleatoriedad). (p. 781)

**EJEMPLO 18.6-1 (p. 781) — SNR y sensibilidad del receptor.** ī = 10 nA, B = 100 MHz ⇒
σ_i ≈ 0.57 nA, SNR = 310 = 25 dB; 310 fotoelectrones por T = 1/2B = 5 ns. Flujo mínimo
detectable Φ = 2B/η; sensibilidad para SNR₀ = 10³: Φ = 1000·(2B/η) = 2×10¹¹/η fotones/s.

*Deducción general de la media y la varianza (p. 781–782, sección marcada con □).*
Fotoevento en t = 0 ⇒ pulso h(t) de área e. Intervalos Δt con probabilidad p = ηΦΔt:

$$i(t) = \sum_l X_l\,h(t - l\Delta t) \qquad (18.6\text{-}10)$$

X_l ∈ {0,1}, ⟨X_l⟩ = p, ⟨X_l²⟩ = p, ⟨X_lX_k⟩ = p² (l ≠ k). Entonces

$$\bar\imath = \sum_l p\,h(t-l\Delta t) \qquad (18.6\text{-}11)$$

$$\langle i^2\rangle = \sum_{l\ne k}\sum p^2 h(t-l\Delta t)h(t-k\Delta t) + \sum_l p\,h^2(t-l\Delta t) \qquad (18.6\text{-}12)$$

En el límite Δt → 0:

$$\bar\imath = \eta\Phi\int_0^\infty h(t)\,dt = e\eta\Phi \qquad (18.6\text{-}13)$$

$$\langle i^2\rangle = (e\eta\Phi)^2 + \eta\Phi\int_0^\infty h^2(t)\,dt \qquad (18.6\text{-}14)$$

$$\sigma_i^2 = \eta\Phi\int_0^\infty h^2(t)\,dt \qquad (18.6\text{-}15)$$

Definiendo

$$B = \frac{1}{2e^2}\int_0^\infty h^2(t)\,dt = \frac{\int_0^\infty h^2(t)\,dt}{2\left[\int_0^\infty h(t)\,dt\right]^2} \qquad (18.6\text{-}16)$$

se obtienen (18.6-7) y (18.6-8). Con H(ν) la transformada de Fourier de h(t), H(0) = e, y por
Parseval (A.1-7):

$$B = \int_0^\infty \left|\frac{H(\nu)}{H(0)}\right|^2 d\nu \qquad (18.6\text{-}17)$$

B es el **ancho de banda equivalente de potencia** (A.2-10) del sistema dispositivo + circuito;
si H(ν) = 1 en −ν_c < ν < ν_c, B = ν_c. Aplicable a todos los detectores sin ganancia (fototubos,
fotodiodos de unión). (p. 782)

#### 18.6B Gain Noise (p. 782)

*Ganancia determinista G* (reemplazar e por q = Ge):

$$\bar\imath = eG\eta\Phi = \frac{eG\eta P}{h\nu} \qquad (18.6\text{-}18), \qquad \sigma_i^2 = 2eG\bar\imath B = 2e^2G^2\eta B\Phi \qquad (18.6\text{-}19)$$

$$\mathrm{SNR} = \frac{\bar\imath}{2eGB} = \frac{\eta\Phi}{2B} = \bar m \qquad (18.6\text{-}20)$$

Independiente de G (media y rms se multiplican por el mismo factor). No aplica a PMT,
fotoconductores y APD, cuya ganancia es aleatoria (Fig. 18.6-3, p. 782: cada fotoevento
genera G_l portadores, pulso de área eG_l).

*Ganancia aleatoria G_l* con ⟨G⟩ = Ḡ y ⟨G²⟩:

$$i(t) = \sum_l X_l G_l\,h(t-l\Delta t) \qquad (18.6\text{-}21)$$

Recuadros (p. 783):

$$\bar\imath = e\bar G\eta\Phi \qquad (18.6\text{-}22)\ \text{Photocurrent Mean (Random Gain)}$$

$$\sigma_i^2 = 2e\bar G\bar\imath BF \qquad (18.6\text{-}23)\ \text{Photocurrent Variance (Random Gain)}$$

$$F = \frac{\langle G^2\rangle}{\langle G\rangle^2} \qquad (18.6\text{-}24)\ \text{Excess Noise Factor}$$

F = 1 + σ_G²/⟨G⟩²; ganancia determinista ⇒ F = 1 y (18.6-23) → (18.6-19). Con F > 1 las
fluctuaciones superan el ruido de disparo. Recuadro:

$$\mathrm{SNR} = \frac{\bar\imath}{2e\bar G BF} = \frac{\eta\Phi/2B}{F} = \frac{\bar m}{F} \qquad (18.6\text{-}25)\ \text{SNR (Random Gain)}$$

**EJEMPLO 18.6-2 (p. 783) — Factor de exceso de ruido de un PMT.** Típicamente F ≈ 1.2.
Como F = 1 + σ_G²/⟨G⟩², SNR de la ganancia = 1/(F − 1) ≈ 5; con Ḡ = 10⁸, σ_G = 10⁸/√5.

**Factor de exceso de ruido de un APD (p. 784–785).** Análisis más complejo que (18.4-8)
(incluye ⟨G²⟩; la media Ḡ coincide con (18.4-8)). Recuadro:

$$F = \mathbb{k}\bar G + (1-\mathbb{k})\left(2 - \frac{1}{\bar G}\right) \qquad (18.6\text{-}26)\ \text{Excess Noise Factor (Conventional APD)}$$

Fig. 18.6-4 (p. 784): F vs Ḡ (1–1000) para k = 0, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50 (inyección de
electrones; para huecos, 1/k reemplaza a k). Válida para inyección de electrones con
**multiplicación de dos portadores iniciada por un solo portador**; si se inyectan ambos, el
resultado es la suma de los parciales. Minimizar el ruido: inyectar el portador de mayor
coeficiente y k lo más pequeño (electrones) o grande (huecos) posible. Dos fuentes del ruido
de ganancia (p. 785): aleatoriedad en la posición de las ionizaciones (da F → 2 para k = 0 y
Ḡ grande) y la realimentación de los dos portadores (puede elevar F mucho más).

**EJEMPLO 18.6-3 (p. 785) — Factor de exceso de ruido de un APD de Si.** Inyección de
electrones, Ḡ = 100, k = 0.1 ⇒ (18.6-26): **F = 11.8**: la corriente media se multiplica por 100,
el SNR se reduce por 11.8. Con ruido de circuito el APD puede sin embargo mejorar el SNR
global (§18.6D).

**APD con coeficientes de ionización dependientes de la historia (p. 785–786).** Un portador
recién generado solo puede ionizar tras recorrer el **espacio muerto** (*dead space*) necesario
para acumular energía; esto ordena las ionizaciones y reduce el ruido de ganancia, sobre
todo con w < 400 nm y pocas multiplicaciones. Reducciones adicionales: *efectos de energía
inicial* (gradiente de campo antes de la región de multiplicación) y *efectos de umbral de
ionización* (cambio brusco de umbral al pasar de una capa a otra). Fig. 18.6-5 (p. 786):
heteroestructura de bajo ruido con dos capas delgadas de bajo umbral alrededor de una de
alto umbral. Teoría: relaciones de recurrencia para momentos y distribución (Hayat, Kwon,
Wang, Campbell, Saleh, Teich, *IEEE Trans. Electron Devices* 49, 2114, 2002).

**EJEMPLO 18.6-4 (p. 786) — Factor de exceso de ruido de un APD de GaAs muy delgado.**
Dos capas de 50 nm de GaAs alrededor de 85 nm de Al_{0.6}Ga_{0.4}As: **F ≈ 2.5 medido a Ḡ = 20**,
frente a F ≈ 15.5 que predice (18.6-26) para GaAs bulk (k ≈ 0.75). Configuraciones con pozo
centrado dan F aún menor a Ḡ pequeña.

#### 18.6C Circuit Noise (p. 786)

Ruido térmico en resistencias y otros elementos disipativos, y fluctuaciones de carga en
transistores del amplificador.

**Ruido térmico (Johnson, Nyquist) (p. 786–787).** Corriente aleatoria i(t) en una resistencia R
a temperatura T, media cero, varianza creciente con T. Densidad espectral de potencia
(§11.1B):

$$S_i(f) = \frac{4}{R}\,\frac{hf}{\exp(hf/kT) - 1} \qquad (18.6\text{-}27)$$

Para f ≪ kT/h (= 6.24 THz a temperatura ambiente), exp(hf/kT) ≈ 1 + hf/kT:

$$S_i(f) \approx 4kT/R \qquad (18.6\text{-}28)$$

$$\sigma_i^2 = \int_0^B S_i(f)\,df \qquad (18.6\text{-}29)$$

Recuadro (B ≪ kT/h):

$$\sigma_i^2 \approx 4kTB/R \qquad (18.6\text{-}30)\ \text{Thermal Noise Current Variance (Resistance R)}$$

Fig. 18.6-6: R a temperatura T ≡ resistor sin ruido en paralelo con fuente de corriente de
ruido de media cero y rms σ_i.

**EJEMPLO 18.6-5 (p. 787) — Ruido térmico en una resistencia.** R = 1 kΩ, T = 300 K,
B = 100 MHz ⇒ **σ_i ≈ 41 nA**.

*Deducción de la densidad espectral del ruido térmico (p. 787, sección *□).* hf/[exp(hf/kT)−1]
es la energía media Ē de un modo EM a frecuencia f en equilibrio térmico a T (13.4-8), así que
S_i(f) = 4Ē/R y la potencia disipada por Hz, S_i(f)R = 4Ē, es la potencia radiada por un cuerpo
negro unidimensional: densidad de modos en una dimensión M(f) = 4/c (10.1-10) ⇒ densidad
de energía ϱ(f) = 4Ē/c y potencia radiada cϱ(f) = 4Ē.

**Parámetro de ruido de circuito; receptores limitados por resistencia y por amplificador
(p. 788–789).** Todas las fuentes de ruido de circuito se agrupan en una corriente aleatoria i_r
en la entrada del receptor (media cero, varianza σ_r²; Fig. 18.6-7). Parámetro adimensional:

$$\sigma_q = \frac{\sigma_r T}{e} = \frac{\sigma_r}{2Be} \qquad (18.6\text{-}31)$$

= número rms de electrones de ruido de circuito recolectados en T = 1/2B; figura de mérito
del circuito receptor.

*Receptor limitado por resistencia* (fotodiodo + R_L + amplificador sin ruido, Fig. 18.6-8, p.
789): σ_r² = 4kTB/R_L ⇒

$$\sigma_q = \sqrt{\frac{kT}{e^2 R_L B}} \qquad (18.6\text{-}32)$$

∝ 1/√B.

**EJEMPLO 18.6-6 (p. 788) — Parámetro de ruido de circuito.** R_L = 50 Ω, B = 100 MHz,
temperatura ambiente ⇒ σ_r = 0.18 µA, **σ_q ≈ 5700**.

*Amplificador FET con ecualizador* (compensa las altas frecuencias atenuadas por la
impedancia capacitiva de entrada), a temperatura ambiente y valores típicos (recuadro):

$$\sigma_q \approx \frac{\sqrt B}{100} \quad (B \text{ en Hz}) \qquad (18.6\text{-}33)\ \text{Circuit-Noise Parameter (FET Amplifier Receiver)}$$

B = 100 MHz ⇒ σ_q = 100 (≪ 5700 del caso 50 Ω). σ_q crece con B por el ecualizador (nota al
pie: Personick, *Optical Fiber Transmission Systems*, 1981, §3.4; σ_q ≡ Z/2 allí).

*Amplificador bipolar*: σ_q independiente de B en un amplio rango; para 100 MHz–2 GHz,
**σ_q ≈ 500** típicamente.

#### 18.6D Signal-to-Noise Ratio and Receiver Sensitivity (p. 789)

Recuadro:

$$\mathrm{SNR} = \frac{\bar\imath^2}{2e\bar G\bar\imath BF + \sigma_r^2} = \frac{(e\bar G\eta\Phi)^2}{2e^2\bar G^2\eta B\Phi F + \sigma_r^2} \qquad (18.6\text{-}34)\ \text{SNR for an Optical Receiver}$$

Primer término del denominador: ruido de fotoelectrones y de ganancia (18.6-23); segundo:
ruido de circuito. Sin ganancia Ḡ = 1 y F = 1. Un circuito sin ruido no altera el SNR aunque
amplifique.

**EJERCICIO 18.6-1 (p. 790) — SNR del receptor limitado por resistencia.** p–i–n ideal (η = 1),
R_L = 50 Ω, T = 300 K, B = 100 MHz. ¿Para qué Φ la varianza del ruido de fotoelectrones
iguala la del ruido térmico de la resistencia? ¿Potencia óptica correspondiente a λ_o = 1550
nm? (Igualar 2eīB = 4kTB/R_L con ī = eΦ.)

Con el número medio de fotones detectados en T = 1/2B,

$$\bar m = \eta\Phi T = \frac{\eta\Phi}{2B} \qquad (18.6\text{-}35)$$

y σ_q = σ_r/2Be, recuadros:

$$\mathrm{SNR} = \frac{\bar G^2\bar m^2}{\bar G^2 F\bar m + \sigma_q^2} \qquad (18.6\text{-}36)\ \text{SNR for an Optical Receiver}$$

$$\mathrm{SNR} = \frac{\bar m^2}{\bar m + \sigma_q^2} \qquad (18.6\text{-}37)\ \text{SNR (Optical Receiver in Absence of Gain)}$$

Interpretación: numerador = cuadrado del número medio de fotoelectrones multiplicados en
T; denominador = suma de varianzas del número de fotoelectrones y del número de electrones
de ruido de circuito en T. Si σ_q = 100, el ruido de circuito domina mientras m̄ < 10 000. (p. 790)

**Dependencia del SNR con el flujo de fotones (p. 790–791).** Sin ganancia:
1. *Límite de ruido de circuito* (m̄ ≪ σ_q², Φ ≪ 2Bσ_q²/η): SNR ≈ m̄²/σ_q² (18.6-38) ∝ Φ².
2. *Límite de ruido de fotones* (m̄ ≫ σ_q²): SNR ≈ m̄ (18.6-39) ∝ Φ.
Fig. 18.6-9 (p. 791): SNR vs m̄ para σ_q = 10 y 100; más luz siempre mejora el SNR.

**Cuándo conviene un APD (p. 791).** Comparando (18.6-36) con (18.6-37): el APD gana si
m̄ < σ_q²(1 − 1/Ḡ²)/(F − 1); para Ḡ ≫ 1, **m̄ < σ_q²/(F − 1)**. Con Φ pequeño (ruido de circuito
dominante) el APD mejora el SNR; con Φ grande (ruido de fotones) el ruido de ganancia lo
empeora (SNR_APD = m̄/F < m̄). Fig. 18.6-10 (p. 792): fotodiodo vs APD (Ḡ = 100, F = 2,
σ_q = 100); transición en m̄ ≈ σ_q²/(F − 1) = 10⁴.

**Dependencia del SNR con la ganancia del APD (p. 791–792).**

$$\mathrm{SNR} = \frac{\bar G^2\bar m}{\bar G^2 F + \sigma_q^2/\bar m} \qquad (18.6\text{-}40)$$

Sustituyendo F de (18.6-26):

$$\mathrm{SNR} = \frac{\bar G^2\bar m}{\mathbb{k}\bar G^3 + (1-\mathbb{k})(2\bar G^2 - \bar G) + \sigma_q^2/\bar m} \qquad (18.6\text{-}41)$$

Fig. 18.6-11 (p. 792): SNR vs Ḡ para m̄ = 1000, σ_q = 500 y k = 0, 0.1, 1.0. Para k = 0 el SNR
crece y satura; para k > 0 hay un **máximo a una ganancia óptima**, tras el cual el ruido de
ganancia lo degrada.

**Dependencia del SNR con el ancho de banda (p. 792–793).** Según σ_r²(B):
1. Limitado por resistencia: σ_r² ∝ B ⇒ SNR ∝ 1/B (18.6-42).
2. Amplificador FET: σ_q ∝ B^{1/2}, σ_r = 2Beσ_q ∝ B^{3/2} ⇒ SNR ∝ 1/(B + sB³) (18.6-43).
3. Amplificador bipolar: σ_q ≈ constante ⇒ σ_r ∝ B ⇒ SNR ∝ 1/(B + s′B²) (18.6-44).
Fig. 18.6-12 (p. 793): a B pequeño los tres van como 1/B; a B grande FET y bipolar caen más
rápido.

**Sensibilidad del receptor (p. 793–794).** Flujo mínimo Φ₀ (potencia P₀ = hνΦ₀, m̄₀ =
ηΦ₀/2B) que da SNR = SNR₀. Resolviendo (18.6-37) (receptor sin ganancia):

$$\bar m_0 = \tfrac12\left[\mathrm{SNR}_0 + \sqrt{\mathrm{SNR}_0^2 + 4\sigma_q^2\,\mathrm{SNR}_0}\right] \qquad (18.6\text{-}45)$$

Recuadro:

$$\text{Límite de ruido de fotones } (\sigma_q^2 \ll \tfrac14\mathrm{SNR}_0):\ \bar m_0 = \mathrm{SNR}_0 \qquad (18.6\text{-}46)$$

$$\text{Límite de ruido de circuito } (\sigma_q^2 \gg \tfrac14\mathrm{SNR}_0):\ \bar m_0 = \sqrt{\mathrm{SNR}_0}\,\sigma_q \qquad (18.6\text{-}47)\ \text{Receiver Sensitivity}$$

**EJEMPLO 18.6-7 (p. 794) — Sensibilidad del receptor.** SNR₀ = 10⁴ (40 dB). Si σ_q ≪ 50:
m̄₀ = 10 000 fotoelectrones por T. Si σ_q ≫ 50: m̄₀ ≈ 100σ_q; con σ_q = 500, m̄₀ = 50 000 ⇒
2Bm̄₀ = 10⁵B fotoelectrones/s; P₀ = 2Bm̄₀hν/η = 10⁵Bhν/η ∝ B. Con B = 100 MHz, η = 0.8,
λ_o = 1550 nm: **P₀ ≈ 1.6 µW**.

Dependencia de σ_q con B (p. 794): limitado por resistencia σ_q ∝ 1/√B; FET σ_q ∝ √B;
bipolar independiente de B. Fig. 18.6-13 (p. 794): m̄₀ vs B para los tres receptores, con el
límite de ruido de fotones m̄₀ = SNR₀ como piso (resistor decrece con B, bipolar plano, FET
crece).

**EJERCICIO 18.6-2 (p. 794) — Sensibilidad del receptor con APD.** Deducir el análogo de
(18.6-45) para un APD de ganancia Ḡ y factor F; mostrar que con ruido de circuito despreciable

$$\bar m_0 = F\cdot\mathrm{SNR}_0 \qquad (18.6\text{-}48)$$

#### 18.6E Bit Error Rate and Receiver Sensitivity (p. 795)

Para un receptor digital, sensibilidad = energía óptica mínima (número medio de fotones) por
bit para un BER prescrito.

**Sensibilidad del receptor ideal (p. 795).** ON–OFF keying: bit "1" = n̄ fotones en promedio,
bit "0" = ninguno; bits equiprobables ⇒ n̄_a = ½n̄ fotones/bit. Con n Poisson, p(n) = n̄ⁿ
exp(−n̄)/n!, el receptor decide "1" si detecta ≥ 1 fotón: p₁ = p(0) = exp(−n̄) (confundir 1 por
0), p₀ = 0. BER = ½(p₁ + p₀):

$$\mathrm{BER} = \tfrac12\exp(-\bar n) = \tfrac12\exp(-2\bar n_a) \qquad (18.6\text{-}49)$$

Fig. 18.6-14 (p. 795): esquema de errores y BER vs n̄_a (semilogarítmico, 10⁻⁹ en n̄_a ≈ 10).
Resultado enmarcado en cursiva: *la sensibilidad del receptor (BER = 10⁻⁹) de un sistema
digital ideal es 10 fotones por bit.* Solo para luz Poisson; con luz de número de fotones
comprimido (§12.3B) se puede mejorar. (p. 796)

**EJERCICIO 18.6-3 (p. 796) — Efecto de η y del ruido de fondo.** (a) Con η < 1 pero ideal en
lo demás, BER = ½exp(−2ηn̄_a) ⇒ n̄_a = 10/η fotones/bit = m̄_a = ηn̄_a = 10 fotoelectrones/bit.
(b) Con fondo Poisson n̄_B (bit 1: n̄ + n̄_B, bit 0: n̄_B), obtener BER(n̄, n̄_B), graficar BER vs
n̄_a = ½n̄ para varios n̄_B y la sensibilidad n̄_a(n̄_B). [Suma de Poisson es Poisson.]

**Sensibilidad con ruido de circuito y de ganancia (p. 796–798).** Carga total por bit (en
unidades de electrones) s = m + q, con m Poisson (media m̄ = ηn̄, varianza m̄) y q gaussiana
de media cero y varianza σ_q² (σ_q = σ_rT/e):

$$\mu = \bar m = \eta\bar n \qquad (18.6\text{-}50), \qquad \sigma^2 = \bar m + \sigma_q^2 \qquad (18.6\text{-}51)$$

Para m̄ grande se aproxima todo por una gaussiana (μ, σ²). Con APD:

$$\mu = \bar m\bar G \qquad (18.6\text{-}52), \qquad \sigma^2 = \bar m\bar G^2 F + \sigma_q^2 \qquad (18.6\text{-}53)$$

Umbral ϑ sobre s (integrador): s > ϑ ⇒ "1". Dos gaussianas:

$$\text{bit "0": } \mu_0 = 0,\ \sigma_0^2 = \sigma_q^2; \qquad \text{bit "1": } \mu_1 = \bar m\bar G,\ \sigma_1^2 = \bar m\bar G^2F + \sigma_q^2 \qquad (18.6\text{-}54)$$

p₀ = integral de la gaussiana "0" de ϑ a ∞; p₁ = integral de la gaussiana "1" de −∞ a ϑ; ϑ se
elige minimizando BER = ½(p₀ + p₁). Si σ₀, σ₁ ≪ μ₁ − μ₀, para el umbral óptimo:

$$\mathrm{BER} \approx \tfrac12[1 - \mathrm{erf}(Q/\sqrt2)] \qquad (18.6\text{-}55), \qquad Q = \frac{\mu_1 - \mu_0}{\sigma_0 + \sigma_1} \qquad (18.6\text{-}56)$$

$$\mathrm{erf}(z) = \frac{2}{\sqrt\pi}\int_0^z \exp(-x^2)\,dx \qquad (18.6\text{-}57)$$

BER = 10⁻⁹ ⇔ Q ≈ 6. Recuadro:

$$\mu_1 - \mu_0 \approx 6(\sigma_0 + \sigma_1) \qquad (18.6\text{-}58)\ \text{Condition for BER} = 10^{-9}\ \text{(Gaussian Approximation)}$$

Sustituyendo (18.6-54) y definiendo m̄_a = ½m̄ (fotoelectrones medios por bit):

$$\bar m_a \approx 18F + 6\sigma_q/\bar G \qquad (18.6\text{-}59)$$

Si 3ḠF ≫ σ_q, recuadro:

$$\bar m_a \approx 18F \qquad (18.6\text{-}60)\ \text{APD Receiver Sensitivity (Absence of Circuit Noise)}$$

Sin ganancia (Ḡ = 1, F = 1) y sin ruido de circuito: m̄_a = 18 fotoelectrones/bit, frente a los
10 del análisis Poisson exacto (Ejercicio 18.6-3): la aproximación gaussiana es inapropiada
para conteos tan bajos. Tabla 18.6-1 (p. 798). Los valores reales dependen de σ_q, que depende
de la tasa de bits B₀ ≡ 1/T.

### Reading List (p. 798–800)

Libros (selección): Becker, *Advanced Time-Correlated Single Photon Counting Techniques*
(2005); Johnson, *Photodetection and Measurement* (2003); Osche, *Optical Detection Theory
for Laser Applications* (2002); Henini & Razeghi, *Handbook of Infrared Detection
Technologies* (2002); Donati, *Photodetectors: Devices, Circuits, and Applications* (1999);
Choi, *The Physics of Quantum Well Infrared Photodetectors* (1997); Dereniak & Boreman,
*Infrared Detectors and Systems* (1996); Rieke, *Detection of Light* (1994); Bube,
*Photoelectronic Properties of Semiconductors* (1992); Saleh, *Photoelectron Statistics*
(1978); Boyd, *Radiometry and the Detection of Optical Radiation* (1983); van der Ziel,
*Noise in Solid State Devices and Circuits* (1986); Rose, *Concepts in Photoconductivity*
(1963). Artículos (selección): Ramirez et al., *IEEE JQE* 42, 137 (2006) (SPAD); Rogalski,
*Rep. Prog. Phys.* 68, 2267 (2005) (HgCdTe); Hayat et al., *IEEE TED* 49, 2114 (2002)
(ruido en APD delgados); Teich & Saleh, *IEEE JSTQE* 6, 1450 (2000) (procesos de
ramificación); Hayat, Saleh & Teich, *IEEE TED* 39, 546 (1992) (espacio muerto); Teich,
Matsuo & Saleh, *IEEE JQE* QE-22, 1184 (1986) (F para APD y PMT); Spicer & Wooten,
*Proc. IEEE* 51, 1119 (1963) (fotoemisión); Shockley & Pierce, *Proc. IRE* 26, 321 (1938)
(ruido de multiplicadores de electrones). Ver también las listas de los caps. 16 y 17.

---

## Tablas y datos numéricos útiles

**Reglas y constantes.**
- 𝕽 = ηGλ_o/1.24 A/W con λ_o en µm (18.1-8); η = 1 y λ_o = 1.24 µm ⇒ 𝕽 = 1 A/W = 1 nA/nW
  (p. 754).
- kT/h = 6.24 THz a temperatura ambiente (p. 787); límite clásico del ruido térmico
  S_i ≈ 4kT/R.
- Fotón de λ_o = 1.24 µm: 1 eV. Potencia mínima detectable (1 fotón en T = 1 µs a 1.24 µm):
  0.16 pW; 1000 fotones en T = 10 ns ⇒ 16 nW (p. 779).

**Funciones de trabajo y afinidades (p. 750).** 𝕎 mínima en metales (Cs) ≈ 2 eV; E_g + χ ≈ 1.4
eV para NaKCsSb (fotocátodo S-20); fotocátodo S-1 hasta λ ≈ 1 µm; GaAs:Cs (NEA).

**Tabla 18.2-1 (p. 761) — Semiconductores extrínsecos: energía de activación y límite de λ.**

| Semiconductor:dopante | E_A (eV) | λ_A (µm) |
|---|---|---|
| Ge:Hg | 0.088 | 14 |
| Ge:Cu | 0.041 | 30 |
| Ge:Zn | 0.033 | 38 |
| Ge:Ga | 0.010 | 115 |
| Si:B | 0.044 | 23 |

η ≈ 0.5 (Ge:Cu); G ≈ 0.03 (Ge:Hg) (p. 761).

**Fotoconductores (p. 760–761).** τ_e ≈ 10⁻⁸ s para w = 1 mm, v_e ≈ 10⁷ cm/s; τ ∈ [10⁻¹³ s,
muchos s]; G ≲ 10⁶; GB ≲ 10⁹; enfriar para λ > 2 µm.

**Fotodiodos y materiales (p. 766–768).**

| Sistema | Rango | Observación |
|---|---|---|
| Al_xGa_{1−x}As/GaAs | 0.7–0.87 µm | |
| In_xGa_{1−x}As/InP | 1300–1600 nm | p–i–n a 1550 nm: η ≈ 0.75, 𝕽 ≈ 0.9 A/W |
| Hg_xCd_{1−x}Te/CdTe | 3–17 µm | IR medio |
| InGaAsP/InP, GaAlAsSb/GaSb | 0.92–1.7 µm | cuaternarios |
| Schottky (Au/Si-n, PtSi/Si-p) | visible; UV–IR | B ≈ 100 GHz |
| p–i–n/Schottky (Fig. 18.3-9) | | respuestas de decenas de ps, B ≈ 50 GHz |

**APD (p. 772–775).** k(Si) ≈ 0.1–0.2 (hasta 0.006); campos ≈ 10⁵ V/cm; InGaAs APD: Ḡ
óptima ≈ 10, corriente oscura ≈ 10⁻¹¹ A, punchthrough ≈ 18 V, ruptura ≈ 30 V (Fig. 18.4-7).
Ej. 18.4-2 (Si): v_e = 10⁷ cm/s, v_h = 5×10⁶ cm/s, τ ≈ 1.02–1.07 ns. F (Si, Ḡ = 100, k = 0.1) =
11.8; F(PMT) ≈ 1.2; F(GaAs delgado, Ḡ = 20) ≈ 2.5 vs 15.5 bulk (k ≈ 0.75).

**SPAD (p. 774–775).** Si: η ≈ 75 %, ≈ 75 cuentas oscuras/s, ≈ 100 ps. InGaAs/InP: η ≈ 20 %,
≈ 5000 cuentas oscuras/s, ≈ 500 ps.

**Arreglos (p. 775).** Microbolómetros VOx: cientos de miles de píxeles de ≈ 25 µm. PtSi: UV
cercano hasta ≈ 6 µm.

**Ruido de circuito (p. 787–789).** σ_i(1 kΩ, 300 K, 100 MHz) ≈ 41 nA. σ_r(50 Ω, 100 MHz,
ambiente) = 0.18 µA ⇒ σ_q ≈ 5700. FET con ecualizador: σ_q ≈ √B/100 (B = 100 MHz ⇒ 100).
Bipolar: σ_q ≈ 500 (100 MHz–2 GHz).

**Receptores (p. 781, 794).** ī = 10 nA, B = 100 MHz ⇒ σ_i ≈ 0.57 nA, SNR = 310 (25 dB).
SNR₀ = 10⁴, σ_q = 500, B = 100 MHz, η = 0.8, 1550 nm ⇒ P₀ ≈ 1.6 µW. Transición
fotodiodo/APD en m̄ ≈ σ_q²/(F − 1).

**Tabla 18.6-1 (p. 798) — Sensibilidades típicas (fotones medios por bit) de receptores a
1 Mb/s–2.5 Gb/s.**

| Receptor | Sensibilidad (fotones/bit) |
|---|---|
| Detector ideal limitado por fotones | 10 |
| APD de Si | 125 |
| Preamplificador de fibra dopada con Er³⁺ + p–i–n de InGaAs | 215 |
| APD de InGaAs | 500 |
| Fotodiodo p–i–n | 6000 |

BER = 10⁻⁹ ⇔ Q ≈ 6 (aprox. gaussiana); m̄_a ≈ 18F + 6σ_q/Ḡ.

---

## Problemas al final del capítulo (p. 800–803)

Nota: el libro numera los problemas de ruido como 18.5-x aunque corresponden a la sección
18.6. Se respeta la numeración impresa.

- **18.1-1 Effect of Reflectance on Quantum Efficiency.** Calcular 1 − 𝓡 para incidencia
  normal y a 45°, luz no polarizada desde aire, sobre Si, GaAs e InSb (§6.2, Tabla 16.2-1).
- **18.1-2 Responsivity.** Máxima responsividad de un fotodetector ideal (η = 1, G = 1) de
  (a) Si, (b) GaAs, (c) InSb.
- **18.1-3 Transit Time.** Par generado en x = w/3 con v_e = 3v_h (Fig. 18.1-6); hallar i_h, i_e y
  sus duraciones τ_h, τ_e en función de e, w, v_e; verificar carga total e; esbozar para v_e = 6×10⁷
  cm/s y w = 10 µm.
- **18.1-4 Current Response with Uniform Illumination.** Impulso de luz que genera N pares
  uniformes entre 0 y w; demostrar
  i_h(t) = −(Nev_h²/w²)t + Nev_h/w para 0 ≤ t ≤ w/v_h (0 fuera),
  i_e(t) = −(Nev_e²/w²)t + Nev_e/w para 0 ≤ t ≤ w/v_e (0 fuera), y
  i(t) = (Ne/w)[(v_h + v_e) − (1/w)(v_h² + v_e²)t] para 0 ≤ t ≤ w/v_e,
  i(t) = (Nev_h/w)[1 − (v_h/w)t] para w/v_e ≤ t ≤ w/v_h (Fig. 18.1-7); cada tipo de portador
  aporta Ne/2 y la carga total es Ne.
- ***18.1-5 Two-Photon Detectors.** Haz de fotones hν con flujo φ (fotones/cm²·s) sobre un
  semiconductor con hν < E_g < 2hν; con J_p = ζφ², demostrar 𝕽 = [ζ/(hc_o)²]λ_o²P/A y
  explicar la proporcionalidad con P/A.
- **18.2-1 Photoconductor Circuit.** Fotoconductor en serie con R y fuente V; si la
  conductancia ∝ P, esbozar V_p(P) y decir cuándo es lineal.
- **18.2-2 Photoconductivity.** Si intrínseco con n_i = 1.5×10¹⁰ cm⁻³, τ = 10 µs; potencia
  absorbida 1 mW/cm³ a λ_o = 1 µm, η = ½: aumento porcentual de conductividad.
- **18.3-1 Quantum Efficiency of a Photodiode Detector.** Pulso de 6×10¹² fotones a 1550 nm
  produce en promedio 2×10¹² electrones: hallar η y 𝕽.
- **18.4-1 Quantum Efficiency of an APD.** APD con Ḡ = 20 y 𝕽 = 12 A/W a 1550 nm: hallar η y
  la fotocorriente para Φ = 10¹⁰ fotones/s.
- **18.4-2 Gain of an APD.** Demostrar que para k = 1 (p. ej. Ge) G = 1/(1 − α_e w)
  [(18.4-8) no es directamente aplicable].
- **18.5-1 Excess Noise Factor for a Single-Carrier APD.** Con k = 0 demostrar F ≈ 2 para
  toda ganancia apreciable; con (18.4-8) mostrar Ḡ = exp(α_e w); 𝕽 de un APD de Si con
  hν = E_g, η = 0.8, Ḡ = 70; F para Si de dos portadores con k = 0.01 y comparar con 2.
- ***18.5-2 Gain of a Multilayer APD.** Con la ley de Bernoulli, Ḡ = (1 + P)^l para un APD
  multicapa de un solo portador (P probabilidad de ionización por etapa, l etapas); recuperar
  el APD convencional cuando P → 0, l → ∞.
- ***18.5-3 Excess Noise Factor for a One-Stage Photomultiplier Tube.** Deducir F de un PMT
  de un dínodo con número de secundarios Poisson de media δ.
- ***18.5-4 Excess Noise Factor for a Photoconductive Detector.** Con G = τ/τ_e y τ aleatoria
  exponencial P(τ) = (1/τ̄)exp(−τ/τ̄), mostrar F = 2 (ruido de generación–recombinación, GR,
  reduce el SNR en 2).
- **18.5-5 Bandwidth of an RC Circuit.** Con (18.6-16), h(t) = (e/τ)exp(−t/τ) tiene B = 1/4τ;
  ancho de banda de un circuito RC; corriente de ruido térmico de R = 1 kΩ a 300 K
  conectada a C = 5 pF.
- **18.5-6 Signal-to-Noise Ratio of an APD Receiver.** Cambio del SNR (Ḡ = 100, sin ruido
  de circuito) al pasar k de 0.1 a 0.2; mostrar que si Ḡ ≫ 1 y ≫ 2(1 − k)/k, SNR ∝ 1/Ḡ.
- **18.5-7 Noise in an APD Receiver.** η = 0.8, Ḡ = 100, k = 0.5, R_L = 1 kΩ, B = 100 kHz,
  corriente oscura + fugas 1 nA, P = 10 nW a 0.87 µm: rms de cada ruido y SNR (ruido oscuro
  con la misma ley que la fotocorriente; receptor limitado por resistencia).
- **18.5-8 Optimal Gain in an APD.** Receptor p–i–n con σ_q²/σ_m² = 100; con APD de k = 0.2,
  hallar la ganancia óptima y la mejora de SNR.
- **18.5-9 Receiver Sensitivity.** Potencia para SNR = 10³ con η = 0.8 a 1300 nm, B = 100 MHz,
  sin ruido de circuito, midiendo la corriente i.
- **18.5-10 Noise Comparison of Three Photodetectors.** Carga 50 Ω a 77 K, λ = 1 µm, B =
  1 GHz: (a) p–i–n η = 0.9; (b) APD η = 0.6, Ḡ = 100, k = 0; (c) PMT de 10 etapas η = 0.3,
  Ḡ = 4¹⁰, σ_G² = Ḡ²/4. Hallar SNR para Φ = 10¹⁰ s⁻¹ y decir cuáles hacen detectable la señal.
- **18.5-11 Dependence of Receiver Sensitivity on Wavelength.** Receptor ideal con −76 dBm
  a 870 nm: sensibilidad a 1300 nm a la misma tasa de datos.
- **18.5-12 Bit Error Rates.** p–i–n limitado por fotones, η = 1, 870 nm, BER = 10⁻¹⁰;
  nueva BER si (a) λ_o = 1300 nm, (b) potencia doble, (c) η = 0.5, (d) APD ideal η = 1, G = 100
  sin ruido de ganancia, (e) como (d) pero F = 2.
- **18.5-13 Sensitivity of an AM Receiver.** Detector de responsividad 𝕽, ancho B, sin ruido de
  circuito, mide P(t) = P₀ + P_s cos(2πft), f < B, P₀ ≫ P_s: mínima P_s medible con SNR₀ = 30 dB
  y efecto de P₀.
- **18.5-14 Sensitivity of a Photon-Counting Receiver.** η = 0.5, T = 1 µs: fotones medios para
  SNR = 10³ (Poisson); potencia a 870 nm; probabilidad de cero cuentas con esa potencia.
- ***18.5-15 A Single-Dynode Photomultiplier Tube.** η = 1, un dínodo, T = 1.3 ns; fotones
  p(n) = ½ para n = 0, 1; ganancia P(G) = ⅓ (G = 2), ⅔ (G = 3). (a) SNR del número de fotones
  vs Poisson de igual media; (b) p(m) y su SNR; (c) ⟨G⟩ y ⟨G²⟩; (d) F; (e) ī con B = 1/2T;
  (f) 𝕽 a 1550 nm; (g) por qué (18.6-23) no aplica.

---

## Relación con Óptica No Lineal

**Con los temas del curso.**
- *Ondas EM y absorción/dispersión*: la eficiencia cuántica (18.1-3) depende de la
  reflectancia 𝓡 (Fresnel, cap. 6) y del coeficiente de absorción α(λ) (§16.2C); el límite de
  longitud de onda larga λ_g = hc_o/E_g (p. 753) fija qué detector sirve para cada región del
  espectro. El Prob. 18.1-1 conecta directamente con las fórmulas de Fresnel y la polarización.
- *Pulsos y respuesta temporal*: el teorema de Ramo (18.1-10) y la respuesta al impulso
  (Fig. 18.1-7, convolución con el RC) dicen qué tan rápido puede seguir un detector un pulso;
  los detectores p–i–n y Schottky llegan a B ≈ 50–100 GHz (p. 767–768), pero ningún detector
  resuelve pulsos de fs o ps de ONL (SPM, solitones): esos se miden por autocorrelación o
  FROG (ópticas no lineales, χ⁽²⁾) y el detector solo integra la energía. Para efectos de
  intensidad (índice no lineal, Kerr) importa distinguir potencia pico de media: el detector
  responde a Φ = P/hν promediado sobre T = 1/2B.
- *χ⁽²⁾ y detección de dos fotones*: el Prob. 18.1-5 (detector de dos fotones, J_p = ζφ², 𝕽 ∝
  λ_o²P/A) es un proceso de absorción de dos fotones (χ⁽³⁾ imaginario): la respuesta cuadrática
  en la intensidad es la base de los autocorreladores de dos fotones usados para medir pulsos
  ultracortos.
- *Raman, FWM, generación de armónicos*: medir señales débiles generadas por procesos no
  lineales (SHG, Raman espontáneo, FWM a baja potencia) requiere PMT, APD o SPAD
  (§18.1A, §18.4D); las cifras de η, cuentas oscuras y resolución temporal de p. 774–775 son las
  que fijan el tiempo de integración necesario.
- *Estadística de fotones (relación con cap. 12)*: SNR = n̄ para luz Poisson (18.6-1); el libro
  advierte que luz con número de fotones comprimido (squeezed, §12.3B) supera el límite de 10
  fotones/bit (p. 796), conexión con óptica cuántica no lineal (OPA/OPO degenerados).

**Con el proyecto final (anillos add-drop en Si₃N₄, refractómetro de volumen, supercontinuo).**
- *Límite de detección del refractómetro*: la resonancia se lee con un fotodiodo (InGaAs p–i–n
  a 1550 nm: η ≈ 0.75, 𝕽 ≈ 0.9 A/W, p. 766) en el puerto drop o through. El desplazamiento
  mínimo detectable Δλ_min se traduce en Δn_min = Δλ_min/S (S sensibilidad en nm/RIU). El ruido
  de la lectura de potencia viene de (18.6-34)/(18.6-37): SNR = m̄²/(m̄ + σ_q²) con m̄ = ηΦ/2B.
  Con potencia suficiente se está en el límite de ruido de disparo, SNR = ηΦ/2B = 𝕽P/2eB
  (18.6-9), y la incertidumbre relativa de potencia es δP/P = 1/√SNR = √(2eB/𝕽P). Para un
  barrido de láser, el error en la posición del mínimo (o máximo) de la lorentziana se
  estima como δλ ≈ (FWHM) · (δP/P) /(pendiente normalizada), de modo que Δn_min ∝
  FWHM/(S·√SNR): el **Q del anillo y la SNR del detector entran juntos** en el límite de
  detección. Las fórmulas de sensibilidad (18.6-45)–(18.6-47) dan la potencia mínima que
  necesita un SNR₀ dado; p. ej. el Ej. 18.6-7 (B = 100 MHz, σ_q = 500, 1550 nm) requiere
  P₀ ≈ 1.6 µW, pero para un sensor con B de kHz la potencia necesaria baja en proporción a
  B (P₀ ∝ B en el límite de circuito con σ_q constante; P₀ ∝ √B si el receptor está limitado
  por resistencia, ver (18.6-32) y (18.6-47)).
- *NEP*: el libro no usa el término NEP, pero su equivalente es la "señal mínima detectable"
  (SNR = 1): P_min = hν·2B/η en el límite de fotones (p. 781) o P_min = hν·2Bσ_q/η en el límite
  de circuito (de (18.6-47) con SNR₀ = 1). Con ruido térmico de la resistencia de carga,
  igualar σ_i² = 4kTB/R_L a (𝕽P)² da P_min = √(4kTB/R_L)/𝕽, de donde NEP = P_min/√B =
  √(4kT/R_L)/𝕽 (W/√Hz); este es el cálculo del Ejercicio 18.6-1 reinterpretado.
- *Elección de detector según potencia*: con la potencia de salida del anillo (decenas de µW
  o menos tras pérdidas de acople), m̄ ≫ σ_q² y un p–i–n basta (límite de fotones, Fig. 18.6-9);
  un APD solo ayuda si m̄ < σ_q²/(F − 1) (p. 791), es decir, con potencias de nW en anchos de
  banda grandes. Para el refractómetro con lock-in o promediado (B pequeño), el p–i–n es la
  opción; para contar fotones de señales no lineales débiles, SPAD (η ≈ 20 % en 1550 nm).
- *Corriente oscura y fondo*: el libro no las incluye en (18.6-34) pero advierte (p. 778) que la
  corriente oscura y el ruido de fondo añaden varianza; el Prob. 18.5-7 muestra cómo
  incluirlas (misma ley 2eI_dB). Para un sensor en el laboratorio: tapar luz ambiente y restar
  la corriente oscura del InGaAs (≈ nA).
- *Detección de espectros anchos (supercontinuo)*: 𝕽 ∝ ηλ_o (18.1-5) ⇒ la responsividad no es
  plana: un espectro ancho se pesa por 𝕽(λ) del detector (Fig. 18.1-5, 18.3-7, 18.3-9). Para un
  supercontinuo en Si₃N₄ de ≈ 0.8–2.4 µm hace falta más de un detector: Si (0.4–1.1 µm,
  máximo ≈ 0.5 A/W a ≈ 0.9 µm), InGaAs (0.9–1.7 µm; extendido hasta ≈ 2.6 µm en
  composiciones sin acople de red), y para λ > 2 µm HgCdTe o InSb enfriados (p. 766, 775). Al
  medir con un OSA o un espectrómetro con arreglo (CCD de Si / InGaAs lineal, §18.5) hay que
  corregir la respuesta espectral η(λ)λ para obtener la densidad espectral de potencia real;
  los detectores térmicos (bolómetros, p. 775) tienen 𝕽 independiente de λ_o (p. 755) y sirven
  como referencia de potencia total.
- *Pulsos del supercontinuo*: el detector integra sobre T = 1/2B; con tasas de repetición de
  decenas de MHz y B de kHz, la fotocorriente es ī = 𝕽·P_media; la potencia pico no se ve, y
  hay que vigilar la saturación (rango dinámico lineal, p. 755) si se mide con un detector
  rápido pulso a pulso.
- *Lumerical/INTERCONNECT*: los elementos "photodetector" de INTERCONNECT usan
  exactamente 𝕽 (A/W), corriente oscura, ruido térmico 4kTB/R y ruido de disparo 2eīB,
  es decir (18.1-5), (18.6-8) y (18.6-30); estos apuntes dan las fórmulas y los valores típicos
  para parametrizarlos (InGaAs: 𝕽 ≈ 0.9 A/W, I_d ≈ 10⁻¹¹–10⁻⁹ A, R_L = 50 Ω ⇒ σ_q ≈ 5700 a
  100 MHz).
