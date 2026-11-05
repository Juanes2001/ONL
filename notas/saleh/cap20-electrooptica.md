# Capítulo 20 — Electro-Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 834–872 (PDF 856–894). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007,
cap. 20 "Electro-Optics". Las secciones marcadas con * son las que el libro señala como
avanzadas (20.2 y 20.4). Convención del libro: dependencia temporal $e^{j\omega t}$ con
$j=\sqrt{-1}$; campos reales en caligráfica, amplitudes complejas en negrita; unidades SI.
En este capítulo el campo eléctrico aplicado $E$ (o $\mathbf{E}$) es **estático o de baja
frecuencia**, distinto del campo óptico; $k_o = 2\pi/\lambda_o$ y $\lambda_o$ es la longitud
de onda en el vacío. El libro escribe los coeficientes electroópticos con letras fraktur
($\mathfrak{r}$, $\mathfrak{s}$); aquí los transcribo como $r$ y $s$ (y $r_{ijk}$, $s_{ijkl}$,
$r_{IK}$, $s_{IK}$ en forma tensorial/contraída). Toda referencia de página "p. N" es la
página del libro.

---

## Resumen del capítulo

El capítulo estudia cómo un campo eléctrico estático (o de baja frecuencia) aplicado a un
material transparente cambia su índice de refracción —el **efecto electroóptico**— y cómo
eso permite construir dispositivos ópticos controlados eléctricamente. La dependencia
$n(E)$ es lineal en el **efecto Pockels** (medios no centrosimétricos, coeficiente $r$,
$10^{-12}$–$10^{-10}$ m/V) y cuadrática en el **efecto Kerr** (cualquier medio, coeficiente
$s$). Aunque $\Delta n$ es diminuto ($10^{-6}$–$10^{-4}$), al acumularse sobre muchas
longitudes de onda produce desfases de orden $\pi$, lo que da lugar a moduladores de fase
(con el voltaje de media onda $V_\pi = (d/L)\lambda_o/(r n^3)$), retardadores dinámicos,
moduladores de intensidad (Mach–Zehnder y celda Pockels entre polarizadores cruzados),
escáneres de prisma, acopladores direccionales conmutables y moduladores espaciales de luz
(§20.1). La §20.2 hace el tratamiento tensorial: el campo deforma el elipsoide de índices
vía $\eta_{ij}(\mathbf{E}) = \eta_{ij} + \sum_k r_{ijk}E_k + \sum_{kl}s_{ijkl}E_kE_l$, con
tablas de $r_{IK}$ para cristales $\bar 4 3m$, $\bar 4 2m$ y $3m$, y ejemplos para
LiNbO$_3$, KDP, GaAs y un medio Kerr isótropo. La §20.3 trata los cristales líquidos
nemáticos (celdas retardadoras, celdas torcidas como rotadores de polarización,
ferroeléctricos y LCD). La §20.4 presenta la **fotorrefractividad**: la luz genera cargas
que difunden y crean un campo interno de carga espacial, el cual, por efecto Pockels,
graba una red de índice $\Delta n(x) = -\tfrac12 n^3 r (kT/e)(1/I)\,dI/dx$; base de la
holografía dinámica y de la mezcla de dos ondas. La §20.5 introduce la
**electroabsorción** (efecto Franz–Keldysh y efecto Stark de confinamiento cuántico, QCSE).
Es el puente natural hacia la óptica no lineal: Pockels es $\chi^{(2)}(\omega;\omega,0)$ y
Kerr es $\chi^{(3)}(\omega;\omega,0,0)$; si el "campo aplicado" es el propio campo óptico se
obtiene el índice dependiente de la intensidad $n = n_0 + n_2 I$ (cap. 21).

---

## Secciones

### Introducción del capítulo (p. 835–836)

- **Definición (p. 835):** el *efecto electroóptico* es un cambio del índice de refracción
  que resulta de aplicar un campo eléctrico estático o de baja frecuencia (Fig. 20.0-1:
  campo aplicado a un material electroóptico → cambia su índice → cambia el efecto sobre la
  luz; "el campo eléctrico controla la luz"). Es resultado de fuerzas que distorsionan
  posiciones, orientaciones o formas de las moléculas.
- Dos formas usuales de la dependencia (p. 835):
  - $n$ cambia **proporcionalmente** a $E$: efecto electroóptico lineal o **efecto Pockels**
    (Friedrich Pockels, 1893).
  - $n$ cambia proporcionalmente a **$E^2$**: efecto electroóptico cuadrático o **efecto
    Kerr** (John Kerr, 1875).
- Orden de magnitud (p. 835): $\Delta n$ es típicamente muy pequeño, pero si
  $\Delta n = 10^{-5}$ y la onda recorre $10^5$ longitudes de onda, acumula un desfase extra
  de $2\pi$.
- Dispositivos posibles (p. 835): lente de focal controlable; prisma de desviación
  controlable (escáner); lámina de fase controlable (modulador de fase); cristal
  anisótropo como retardador controlable (cambia el estado de polarización); retardador
  entre polarizadores cruzados → modulador de intensidad o interruptor (ref. §6.6B).
- **Electroabsorción (p. 835–836):** un campo eléctrico puede reducir el gap de un
  semiconductor y convertirlo de transparente en opaco para $\lambda$ > $\lambda_g$
  (ref. §16.2B). Sirve para moduladores e interruptores.
- "This Chapter" (p. 836): §20.1 principios (simplificados, sin anisotropía); §20.2
  medios anisótropos; §20.3 cristales líquidos (celda nemática torcida como rotador de
  polarización dinámico); §20.4 fotorrefractividad ("luz que controla luz"); §20.5
  electroabsorción.

---

### 20.1 Principles of Electro-Optics (p. 836)

#### 20.1A Pockels and Kerr Effects (p. 836–838)

**Desarrollo en serie de Taylor (p. 836).** El índice $n(E)$ varía poco con el campo
aplicado estático $E$, así que

$$
n(E) = n + a_1 E + \tfrac12 a_2 E^2 + \cdots, \tag{20.1-1}
$$

con $n = n(0)$, $a_1 = (dn/dE)|_{E=0}$, $a_2 = (d^2n/dE^2)|_{E=0}$. Por convención se
definen los **coeficientes electroópticos** $r = -2a_1/n^3$ y $s = -a_2/n^3$, de modo que

$$
n(E) = n - \tfrac12 r\,n^3 E - \tfrac12 s\,n^3 E^2 + \cdots . \tag{20.1-2}
$$

Los términos de segundo orden y superiores son muchos órdenes de magnitud menores que
$n$; los de orden superior al tercero se desprecian (p. 836).

**Impermeabilidad eléctrica (p. 836–837).** $\eta = \epsilon_o/\epsilon = 1/n^2$ es la
magnitud natural para describir medios anisótropos (§6.3A). Como
$\Delta\eta = (d\eta/dn)\Delta n = (-2/n^3)(-\tfrac12 r n^3 E - \tfrac12 s n^3 E^2) = rE + sE^2$,

$$
\eta(E) \approx \eta + r\,E + s\,E^2, \tag{20.1-3}
$$

con $\eta = \eta(0)$. Es decir, $r$ y $s$ son simplemente los coeficientes de
proporcionalidad de $\Delta\eta$ con $E$ y $E^2$; eso explica las definiciones "raras" de
(20.1-2). Los valores de $r$ y $s$ dependen de la dirección del campo aplicado y de la
polarización de la luz (§20.2).

**Efecto Pockels (p. 837, recuadro).** Cuando el tercer término de (20.1-2) es despreciable:

$$
\boxed{\,n(E) \approx n - \tfrac12 r\,n^3 E\,} \tag{20.1-4}
$$

- El medio es un *medio Pockels* o *celda Pockels*; $r$ es el **coeficiente Pockels**
  (coeficiente electroóptico lineal). Valores típicos: $r \sim 10^{-12}$ a $10^{-10}$ m/V
  (1 a 100 pm/V).
- Para $E = 10^6$ V/m (10 kV sobre 1 cm) el término $\tfrac12 r n^3 E \sim 10^{-6}$–$10^{-4}$.
- Cristales usuales: NH$_4$H$_2$PO$_4$ (ADP), KH$_2$PO$_4$ (KDP), LiNbO$_3$, LiTaO$_3$, CdTe.
- Fig. 20.1-1(a): $n(E)$ es una recta de pendiente negativa (medio Pockels); (b) parábola
  (medio Kerr).

**Efecto Kerr (p. 837–838, recuadro).** Si el material es **centrosimétrico** (gases,
líquidos y ciertos cristales), $n(E)$ debe ser función par de $E$ (invariante ante
$E \to -E$), luego $r = 0$ y

$$
\boxed{\,n(E) \approx n - \tfrac12 s\,n^3 E^2\,} \tag{20.1-5}
$$

- *Medio Kerr* / *celda Kerr*; $s$ es el **coeficiente Kerr** (electroóptico cuadrático).
  Valores típicos: $s \sim 10^{-18}$–$10^{-14}$ m$^2$/V$^2$ en cristales y
  $10^{-22}$–$10^{-19}$ m$^2$/V$^2$ en líquidos.
- Para $E = 10^6$ V/m, $\tfrac12 s n^3 E^2 \sim 10^{-6}$–$10^{-2}$ en cristales y
  $10^{-10}$–$10^{-7}$ en líquidos (p. 838).

#### 20.1B Electro-Optic Modulators and Switches (p. 838–842)

**Moduladores de fase (p. 838–839).** Un haz que recorre una celda Pockels de longitud $L$
con campo $E$ sufre un desfase $\varphi = n(E)k_oL = 2\pi n(E)L/\lambda_o$. Con (20.1-4):

$$
\varphi \approx \varphi_0 - \pi\frac{r\,n^3 E L}{\lambda_o}, \qquad \varphi_0 = \frac{2\pi n L}{\lambda_o}. \tag{20.1-6}
$$

Si el campo se obtiene aplicando un voltaje $V$ entre dos caras separadas una distancia
$d$, $E = V/d$ y

$$
\boxed{\,\varphi = \varphi_0 - \pi\frac{V}{V_\pi}\,} \tag{20.1-7}
$$

$$
\boxed{\,V_\pi = \frac{d}{L}\,\frac{\lambda_o}{r\,n^3}\,} \tag{20.1-8}
$$

- $V_\pi$ es el **voltaje de media onda** (*half-wave voltage*): el voltaje al que el
  desfase cambia en $\pi$. Depende del material ($n$, $r$), de $\lambda_o$ y de la relación
  de aspecto $d/L$. La relación fase–voltaje es lineal (Fig. 20.1-2 gráfica $\varphi$ vs $V$).
- **Moduladores transversales**: campo perpendicular a la propagación; **longitudinales**:
  campo paralelo, en cuyo caso $d = L$ (Fig. 20.1-2: (a) longitudinal, con electrodos en
  forma de arandela/banda o conductores transparentes; (b) transversal; (c) transversal de
  onda viajera). $V_\pi$ típico: 1 a unos pocos kV (longitudinales), cientos de V
  (transversales) (p. 838).
- El valor de $r$ depende de las direcciones de propagación y de campo (cristal anisótropo,
  §20.2).
- **Velocidad (p. 838–839):** limitada por la capacitancia y por el tiempo de tránsito $T$
  de la luz. Si $E(t)$ varía durante $T$, la fase es proporcional al campo promedio entre
  $t-T$ y $t$; el ancho de banda limitado por tránsito es $\approx 1/T$. Solución: aplicar
  $V$ en un extremo con los electrodos como línea de transmisión (onda viajera,
  Fig. 20.1-2c); si la velocidad de la onda eléctrica iguala a la óptica, el efecto de
  tránsito se elimina en principio. Moduladores comerciales en bulk: cientos de MHz; posibles
  varios GHz.
- **Moduladores integrados (p. 839, Fig. 20.1-3):** guía de onda en sustrato electroóptico
  (usualmente LiNbO$_3$ con Ti indifundido para subir el índice) con electrodos sobre la
  guía (configuración transversal, $d \ll L$) → $V_\pi$ de unos pocos voltios; se han operado
  a > 100 GHz; acoplo por fibra.

**Retardadores de onda dinámicos (p. 839–840).** Un medio anisótropo tiene dos modos
normales linealmente polarizados con velocidades $c_o/n_1$ y $c_o/n_2$ (§6.3B). Con efecto
Pockels,

$$
n_1(E) \approx n_1 - \tfrac12 r_1 n_1^3 E, \tag{20.1-9}
$$
$$
n_2(E) \approx n_2 - \tfrac12 r_2 n_2^3 E, \tag{20.1-10}
$$

con $r_1$, $r_2$ los coeficientes Pockels apropiados. Tras una distancia $L$ el retardo de
fase relativo es

$$
\Gamma = k_o[n_1(E) - n_2(E)]L = k_o(n_1 - n_2)L - \tfrac12 k_o(r_1 n_1^3 - r_2 n_2^3)EL. \tag{20.1-11}
$$

Con $E = V/d$:

$$
\boxed{\,\Gamma = \Gamma_0 - \pi\frac{V}{V_\pi}\,} \tag{20.1-12}
$$

donde $\Gamma_0 = k_o(n_1 - n_2)L$ es el retardo sin campo y

$$
\boxed{\,V_\pi = \frac{d}{L}\,\frac{\lambda_o}{r_1 n_1^3 - r_2 n_2^3}\,} \tag{20.1-13}
$$

es el **voltaje de media onda de retardo** (el que produce $\Gamma = \pi$). El medio es un
retardador controlado eléctricamente, con $\Gamma$ lineal en $V$.

**Moduladores de intensidad: modulador de fase en un interferómetro (p. 840–841).** El
retardo de fase solo no cambia la intensidad, pero sí lo hace en un brazo de un
Mach–Zehnder (Fig. 20.1-4). Con divisores 50/50,

$$
I_o = \tfrac12 I_i + \tfrac12 I_i\cos\varphi = I_i\cos^2(\varphi/2), \tag{20.1-14}
$$

$\varphi = \varphi_1 - \varphi_2$ (§2.5A); transmitancia $\mathcal{T} = I_o/I_i = \cos^2(\varphi/2)$.
Con el modulador en el brazo 1, $\varphi_1 = \varphi_{10} - \pi V/V_\pi$, de modo que
$\varphi = \varphi_0 - \pi V/V_\pi$ con $\varphi_0 = \varphi_{10} - \varphi_2$ (depende de la
diferencia de camino óptico):

$$
\boxed{\,\mathcal{T}(V) = \cos^2\!\left(\frac{\varphi_0}{2} - \frac{\pi}{2}\frac{V}{V_\pi}\right)\,} \tag{20.1-15}
$$

- Fig. 20.1-4: $\mathcal{T}(V)$ es periódica en $V$. Con $\varphi_0 = \pi/2$ y operando cerca
  de $\mathcal{T} = 0.5$ (punto B) → modulador lineal de intensidad. Con $\varphi_0$ múltiplo
  de $2\pi$: $\mathcal{T}(0) = 1$, $\mathcal{T}(V_\pi) = 0$ → **interruptor** (puntos A y C).
- Versión integrada (Fig. 20.1-5): Mach–Zehnder con guías en Y sobre LiNbO$_3$; comerciales
  a pocos GHz, demostrados > 25 GHz (p. 841).

**Moduladores de intensidad: retardador entre polarizadores cruzados (p. 841–842).** Un
retardador $\Gamma$ entre polarizadores cruzados a 45° de sus ejes (§6.6B, Fig. 6.6-4) tiene
$\mathcal{T} = \sin^2(\Gamma/2)$. Si el retardador es una celda Pockels, (20.1-12) da

$$
\boxed{\,\mathcal{T}(V) = \sin^2\!\left(\frac{\Gamma_0}{2} - \frac{\pi}{2}\frac{V}{V_\pi}\right)\,} \tag{20.1-16}
$$

(Fig. 20.1-6). $\mathcal{T}$ varía entre 0 (obturador cerrado) y 1 (abierto). Para operación
lineal cerca de $\mathcal{T} = 0.5$, con $\Gamma_0 = \pi/2$ y $V \ll V_\pi$:

$$
\mathcal{T}(V) = \sin^2\!\left(\frac{\pi}{4} - \frac{\pi}{2}\frac{V}{V_\pi}\right) \approx \mathcal{T}(0) + \left.\frac{d\mathcal{T}}{dV}\right|_{V=0}V = \frac12 - \frac{\pi}{2}\frac{V}{V_\pi}, \tag{20.1-17}
$$

con pendiente $\pi/2V_\pi$ = **sensibilidad** del modulador. $\Gamma_0$ se ajusta ópticamente
(con un compensador) o eléctricamente (voltaje de polarización constante).

- En la práctica $\mathcal{T}_{\max} < 1$ (reflexión, absorción, dispersión) y
  $\mathcal{T}_{\min} > 0$ (desalineaciones). La razón $\mathcal{T}_{\max}/\mathcal{T}_{\min}$
  es la **razón de extinción**; son posibles > 30 dB (1000:1) (p. 842).

#### 20.1C Scanners (p. 842–843)

- Un prisma de ángulo de ápice pequeño $\alpha$ e índice $n$ desvía $\theta \approx (n-1)\alpha$
  [ec. (1.2-7)]. Un $\Delta n$ por campo aplicado produce

$$
\Delta\theta = \alpha\,\Delta n = -\tfrac12\alpha\,r\,n^3 E = -\tfrac12\alpha\,r\,n^3 V/d, \tag{20.1-18}
$$

  con $d$ el ancho del prisma (Fig. 20.1-7a). $\Delta\theta \propto V$ → barrido. Es más
  práctico poner electrodos triangulares sobre un cristal rectangular; se pueden cascadear
  prismas alternando la dirección del campo (prisma doble, Fig. 20.1-7b).
- **Resolución** (número de puntos independientes): un haz de ancho $D$ tiene divergencia
  $\delta\theta \approx \lambda_o/D$ [ec. (4.3-7)]; conviene que el haz cubra todo el prisma.

$$
N \approx \frac{|\Delta\theta|}{\delta\theta} = \frac{\tfrac12\alpha\,r\,n^3 V/d}{(\lambda_o/D)}. \tag{20.1-19}
$$

  Con $\alpha \approx L/D$ y $V_\pi = (d/L)(\lambda_o/r n^3)$:

$$
N \approx \frac{V}{2V_\pi}, \tag{20.1-20}
$$

  es decir $V \approx 2NV_\pi$: resultado "desalentador" (p. 843) — para $N \gg 1$ se
  requieren voltajes inaceptables; por eso se usan más los escáneres mecánicos y
  acustoópticos (§19.2B y §23.3B).
- **Conmutador de posición (p. 843, Fig. 20.1-8):** la doble refracción (§6.3E) desplaza
  lateralmente un haz para una polarización y no para la otra. Un retardador electroóptico
  actuando como rotador de polarización + cristal birrefringente → interruptor entre dos
  posiciones paralelas.

#### 20.1D Directional Couplers (p. 843–846)

- Dos guías planas monomodo paralelas intercambian potencia periódicamente en $z$ (§8.5B).
  Parámetros: coeficiente de acoplo $\mathcal{C}$ y desajuste
  $\Delta\beta = \beta_1 - \beta_2 = 2\pi\Delta n/\lambda_o$. Si son idénticas
  ($\Delta\beta = 0$, $P_2(0) = 0$), a la **distancia de transferencia** (longitud de
  acoplo) $L_0 = \pi/2\mathcal{C}$ la potencia pasa completamente de la guía 1 a la 2:
  $P_1(L_0) = 0$, $P_2(L_0) = P_1(0)$ (Fig. 20.1-9a).
- Para una guía de longitud $L_0$ y $\Delta\beta \neq 0$, la razón de transferencia
  $\mathcal{T} = P_2(L_0)/P_1(0)$ es [ec. (8.5-12a)]:

$$
\mathcal{T} = \frac{\pi^2}{4}\,\mathrm{sinc}^2\!\left[\frac12\sqrt{1 + \left(\frac{\Delta\beta\,L_0}{\pi}\right)^2}\,\right], \qquad \mathrm{sinc}(x) \equiv \frac{\sin(\pi x)}{\pi x}. \tag{20.1-21}
$$

  Máximo $\mathcal{T} = 1$ en $\Delta\beta L_0 = 0$; se anula en $\Delta\beta L_0 = \sqrt3\,\pi$
  (Fig. 20.1-9b): la potencia *no* se transfiere.
- **Control electroóptico (p. 845):** un campo $E$ en una guía cambia
  $\Delta n = -\tfrac12 n^3 r E$ y produce
  $\Delta\beta L_0 = \Delta n(2\pi L_0/\lambda_o) = -(\pi/\lambda_o)n^3 r L_0 E$. En la geometría
  de la Fig. 20.1-10 (electrodos sobre las dos guías separadas $d$) el voltaje $V$ crea
  $E \approx V/d$ en una guía y $-V/d$ en la otra ($d$ es una distancia efectiva que sale de
  la electrostática; las líneas de campo van hacia abajo en una guía y hacia arriba en la
  otra). Diferencia neta $2\Delta n = -n^3 r(V/d)$, de donde
  $\Delta\beta L_0 = -(2\pi/\lambda_o)n^3 r(L_0/d)V \propto V$.
- **Voltaje de conmutación** $V_0$: aquel para el que $|\Delta\beta L_0| = \sqrt3\pi$:

$$
V_0 = \sqrt3\,\frac{d}{L_0}\,\frac{\lambda_o}{2n^3 r} = \frac{\sqrt3\,\mathcal{C}\lambda_o d}{\pi n^3 r}, \tag{20.1-22}
$$

  con $L_0 = \pi/2\mathcal{C}$. Como $|\Delta\beta L_0| = \sqrt3\pi V/V_0$:

$$
\boxed{\,\mathcal{T} = \frac{\pi^2}{4}\,\mathrm{sinc}^2\!\left[\frac12\sqrt{1 + 3\left(\frac{V}{V_0}\right)^2}\,\right]\,} \tag{20.1-23}
$$

  (eficiencia de acoplo, Fig. 20.1-11: en $V = 0$ toda la potencia pasa a la guía 2; en
  $V = V_0$ permanece en la guía 1).
- El acoplador queda caracterizado por $L_0 \propto 1/\mathcal{C}$ y $V_0 \propto \mathcal{C}$;
  el parámetro clave es $\mathcal{C}$ (geometría e índices). Realización: Ti difundido en
  LiNbO$_3$; $V_0 < 10$ V, > 10 GHz, haces enfocados a pocos μm, fibras PM pegadas (§9.1C);
  versión de onda viajera para más ancho de banda (p. 845–846).

**EJERCICIO 20.1-1 — Coupling-Efficiency Spectral Response (p. 846).** Como $V_0 \propto
\lambda_o$ según (20.1-22), si se aplica $V = V_0$ para $\bar\lambda_o$ (de modo que
$\mathcal{T} = 0$ ahí) y la onda incidente tiene $\lambda_o$, graficar $\mathcal{T}$ en
función de $\lambda_o - \bar\lambda_o$, suponiendo $\mathcal{C}$, $n$ y $r$ independientes de
$\lambda$. (Sin solución en el texto; se resuelve sustituyendo $V/V_0(\lambda_o) =
\bar\lambda_o/\lambda_o$ en (20.1-23).)

#### 20.1E Spatial Light Modulators (p. 846–848)

- Un **modulador espacial de luz** (SLM) es un elemento plano de transmitancia controlable
  $\mathcal{T}(x,y)$: $I_o(x,y) = I_i(x,y)\mathcal{T}(x,y)$ (Fig. 20.1-12). Con iluminación
  uniforme, la "imagen" $\mathcal{T}(x,y)$ se imprime en la luz transmitida.
- **Direccionamiento eléctrico (p. 846–847, Fig. 20.1-13):** matriz de electrodos
  transparentes sobre placas de material electroóptico entre polarizadores cruzados; el
  voltaje en $(x_i, y_i)$ se hace proporcional al $\mathcal{T}(x_i,y_i)$ deseado (como
  Fig. 20.1-6). Es una matriz de moduladores longitudinales de intensidad. No es práctico
  direccionar muchos electrodos, salvo en cristal líquido (voltajes bajos, §20.3B).
- **Direccionamiento óptico (p. 847, Fig. 20.1-14):** capa fotoconductora cuya conductancia
  $G(x,y) \propto I_W(x,y)$ (intensidad de "escritura", §18.2) entre dos electrodos que
  forman un capacitor cargado; la fuga local $\propto G$ reduce la carga donde $G$ es alta,
  así $E(x,y) \propto 1/G(x,y) \propto 1/I_W(x,y)$. La transmitancia (o reflectancia
  $\mathcal{R}$) resulta inversamente proporcional a $I_W$.
- **PROM — Pockels Readout Optical Modulator (p. 848, Fig. 20.1-15):** cristal de óxido de
  bismuto-silicio Bi$_{12}$SiO$_{20}$ (BSO), que (1) tiene efecto Pockels, (2) es
  fotoconductor para luz azul pero no roja, (3) es buen aislante en la oscuridad. Ciclo:
  *Priming* (≈ 4 kV a los electrodos, capacitor cargado); *Writing* (luz azul $I_W(x,y)$ →
  $G \propto I_W$ → $E \propto 1/I_W$ → $\Delta n(x,y) \propto 1/I_W(x,y)$ almacenado);
  *Reading* (luz roja uniforme, con un divisor de haz polarizante como polarizadores
  cruzados; reflector dicroico que refleja rojo y transmite azul); *Erasing* (destello
  azul uniforme; se vuelve a cebar a 4 kV).
- **Convertidores incoherente→coherente (p. 848):** la escritura puede ser con luz
  incoherente (el fotoconductor responde a intensidad) y la lectura con luz coherente;
  útil en procesamiento óptico de datos e imágenes.

---

### *20.2 Electro-Optics of Anisotropic Media (p. 849)

**Repaso de óptica de cristales (p. 849, recuadro).** El medio anisótropo se describe con
el **elipsoide de índices**

$$
\sum_{ij}\eta_{ij}x_ix_j = 1, \qquad i,j = 1,2,3,
$$

con $\eta_{ij} = \eta_{ji}$ elementos del tensor de impermeabilidad
$\boldsymbol\eta = \epsilon_o\boldsymbol\epsilon^{-1}$. En los ejes principales:
$x_1^2/n_1^2 + x_2^2/n_2^2 + x_3^2/n_3^2 = 1$ (Fig. 20.2-1). Para una onda que viaja en
dirección $\mathbf{k}$, el plano perpendicular a $\mathbf{k}$ por el centro corta al
elipsoide en una elipse cuyos semiejes son los índices $n_a$, $n_b$ de los dos modos
normales, y sus direcciones son las polarizaciones (§6.3C).

#### 20.2A Pockels and Kerr Effects (p. 849–854)

Con un campo $\mathbf{E} = (E_1, E_2, E_3)$ cada $\eta_{ij}$ se vuelve función
$\eta_{ij}(\mathbf{E})$ y el elipsoide se modifica (Fig. 20.2-2). Desarrollo de Taylor
alrededor de $\mathbf{E} = 0$:

$$
\boxed{\,\eta_{ij}(\mathbf{E}) = \eta_{ij} + \sum_k r_{ijk}E_k + \sum_{kl}s_{ijkl}E_kE_l, \qquad i,j,k,l = 1,2,3\,} \tag{20.2-1}
$$

con $\eta_{ij} = \eta_{ij}(0)$, $r_{ijk} = \partial\eta_{ij}/\partial E_k$,
$s_{ijkl} = \tfrac12\,\partial^2\eta_{ij}/\partial E_k\partial E_l$, derivadas en
$\mathbf{E} = 0$. Generaliza (20.1-3): $r$ → $3^3 = 27$ coeficientes $\{r_{ijk}\}$
(**tensor Pockels, de tercer rango**) y $s$ → $3^4 = 81$ coeficientes $\{s_{ijkl}\}$
(**tensor Kerr, de cuarto rango**) (p. 850).

**Simetría (p. 850).** Como $\eta_{ij} = \eta_{ji}$: $r_{ijk} = r_{jik}$,
$s_{ijkl} = s_{jikl}$; además $s_{ijkl} = s_{ijlk}$ (orden de derivación). Las 9
combinaciones $(i,j)$ se reducen a 6 → $r_{ijk}$ tiene $6\times3$ elementos independientes
y $s_{ijkl}$ tiene $6\times6$. **Índice contraído** $I = 1,\dots,6$ para $(i,j)$ y $K$ para
$(k,l)$ (Tabla 20.2-1):

| $j\backslash i$ | 1 | 2 | 3 |
|---|---|---|---|
| 1 | 1 | 6 | 5 |
| 2 | 6 | 2 | 4 |
| 3 | 5 | 4 | 3 |

Ejemplo: $(i,j) = (3,2) \to I = 4$; $r_{12k} \to r_{6k}$; $s_{1231} \to s_{65}$. El tensor
$r$ se escribe como matriz $6\times3$ ($r_{Ik}$) y $s$ como $6\times6$ ($s_{IK}$).

**Simetría cristalina (p. 850–851).** Impone ceros e igualdades en $r$ y $s$. En materiales
**centrosimétricos $r = 0$** y solo hay Kerr. Listas completas para los 32 grupos puntuales
en la bibliografía; ejemplos en Tablas 20.2-2 y 20.2-3 (transcritas abajo en "Tablas").

**Procedimiento para el efecto Pockels (p. 851):**
1. Ejes principales e índices $n_1, n_2, n_3$ sin campo.
2. Coeficientes $\{r_{ijk}\}$ de la matriz $r_{Ik}$ apropiada (Tabla 20.2-2) usando la regla
   $I \leftrightarrow (i,j)$ de la Tabla 20.2-1.
3. Tensor de impermeabilidad

$$
\eta_{ij}(\mathbf{E}) = \eta_{ij}(0) + \sum_k r_{ijk}E_k, \tag{20.2-2}
$$

   con $\eta_{ij}(0)$ diagonal con elementos $1/n_1^2$, $1/n_2^2$, $1/n_3^2$.
4. Elipsoide modificado

$$
\sum_{ij}\eta_{ij}(\mathbf{E})x_ix_j = 1. \tag{20.2-3}
$$

5. Diagonalizar → nuevos ejes principales e índices $n_1(\mathbf{E})$, $n_2(\mathbf{E})$,
   $n_3(\mathbf{E})$.
6. Dada la dirección de propagación, hallar modos normales e índices con el elipsoide.

**EJEMPLO 20.2-1 — Cristales trigonales 3m (LiNbO$_3$ y LiTaO$_3$) (p. 851–852).**
Uniaxiales ($n_1 = n_2 = n_o$, $n_3 = n_e$). Con $\mathbf{E} = (0,0,E)$ (a lo largo del eje
óptico, Fig. 20.2-3):

$$
\left(\frac{1}{n_o^2} + r_{13}E\right)(x_1^2 + x_2^2) + \left(\frac{1}{n_e^2} + r_{33}E\right)x_3^2 = 1. \tag{20.2-4}
$$

Elipsoide de revolución; los ejes principales no cambian:

$$
\frac{1}{n_o^2(E)} = \frac{1}{n_o^2} + r_{13}E, \tag{20.2-5}
$$
$$
\frac{1}{n_e^2(E)} = \frac{1}{n_e^2} + r_{33}E. \tag{20.2-6}
$$

Con $(1+\Delta)^{-1/2} \approx 1 - \tfrac12\Delta$ ($|\Delta| \ll 1$):

$$
\boxed{\begin{aligned}
n_o(E) &\approx n_o - \tfrac12 n_o^3 r_{13}E \quad &(20.2\text{-}7)\\
n_e(E) &\approx n_e - \tfrac12 n_e^3 r_{33}E \quad &(20.2\text{-}8)
\end{aligned}}
$$

El cristal sigue siendo uniaxial con los mismos ejes; obsérvese la similitud con (20.1-4).

**EJEMPLO 20.2-2 — Cristales tetragonales $\bar 4 2m$ (KDP y ADP) (p. 852–853).** Campo a
lo largo del eje óptico (Fig. 20.2-4):

$$
\frac{x_1^2 + x_2^2}{n_o^2} + \frac{x_3^2}{n_e^2} + 2r_{63}E\,x_1x_2 = 1. \tag{20.2-9}
$$

Los nuevos ejes principales se obtienen rotando 45° alrededor de $z$:
$x_1' = (x_1 + x_2)/\sqrt2$, $x_2' = (x_1 - x_2)/\sqrt2$, $x_3' = x_3$; renombrando,

$$
\frac{x_1^2}{n_1^2(E)} + \frac{x_2^2}{n_2^2(E)} + \frac{x_3^2}{n_3^2(E)} = 1, \tag{20.2-10}
$$
$$
\frac{1}{n_1^2(E)} = \frac{1}{n_o^2} + r_{63}E, \qquad \frac{1}{n_2^2(E)} = \frac{1}{n_o^2} - r_{63}E, \qquad n_3(E) = n_e. \tag{20.2-11}
$$

Con la aproximación de Taylor:

$$
\boxed{\begin{aligned}
n_1(E) &\approx n_o - \tfrac12 n_o^3 r_{63}E \quad &(20.2\text{-}12)\\
n_2(E) &\approx n_o + \tfrac12 n_o^3 r_{63}E \quad &(20.2\text{-}13)\\
n_3(E) &= n_e \quad &(20.2\text{-}14)
\end{aligned}}
$$

El cristal uniaxial **se vuelve biaxial** con campo a lo largo de su eje óptico.

**EJEMPLO 20.2-3 — Cristales cúbicos $\bar 4 3m$ (GaAs, CdTe, InAs) (p. 853).** Campo a lo
largo de un eje cúbico ($z$), $n_1 = n_2 = n_3 = n$ (isótropo):

$$
\frac{x_1^2 + x_2^2 + x_3^2}{n^2} + 2r_{41}E\,x_1x_2 = 1, \tag{20.2-15}
$$

($r_{63}$ toma el valor $r_{41}$, Tabla 20.2-2). Ejes rotados 45° alrededor de $z$:

$$
n_1(E) \approx n - \tfrac12 n^3 r_{41}E, \tag{20.2-16}
$$
$$
n_2(E) \approx n + \tfrac12 n^3 r_{41}E, \tag{20.2-17}
$$
$$
n_3(E) \approx n. \tag{20.2-18}
$$

El cristal isótropo se comporta como biaxial (Fig. 20.2-5). Comentario (p. 854): los
cúbicos tienen ejes cristalinos definidos pero óptica lineal isótropa; el campo rompe la
simetría. Para materiales que no cambian de ejes (Ej. 20.2-1), las polarizaciones de los
modos normales se conservan pero sus índices dependen de $E$ → modulador de fase, retardador
o modulador de intensidad según §20.1B.

**Efecto Kerr (p. 854).** Mismo procedimiento con

$$
\eta_{ij}(\mathbf{E}) = \eta_{ij}(0) + \sum_{kl}s_{ijkl}E_kE_l. \tag{20.2-19}
$$

**EJEMPLO 20.2-4 — Efecto Kerr en un medio isótropo (p. 854).** Campo $E$ a lo largo de
$z$, con los $s_{IK}$ de la Tabla 20.2-3:

$$
\left(\frac{1}{n^2} + s_{12}E^2\right)(x_1^2 + x_2^2) + \left(\frac{1}{n^2} + s_{11}E^2\right)x_3^2 = 1. \tag{20.2-20}
$$

Elipsoide de revolución con eje $z$ (dirección del campo):

$$
\frac{1}{n_o^2(E)} = \frac{1}{n^2} + s_{12}E^2, \tag{20.2-21}
$$
$$
\frac{1}{n_e^2(E)} = \frac{1}{n^2} + s_{11}E^2, \tag{20.2-22}
$$

$$
\boxed{\begin{aligned}
n_o(E) &\approx n - \tfrac12 n^3 s_{12}E^2 \quad &(20.2\text{-}23)\\
n_e(E) &\approx n - \tfrac12 n^3 s_{11}E^2 \quad &(20.2\text{-}24)
\end{aligned}}
$$

Un medio inicialmente isótropo se vuelve **uniaxial con eje óptico a lo largo de $E$**;
ambos índices decrecen cuadráticamente con $E$. (Esta es la birrefringencia inducida por
Kerr: $n_e - n_o \approx \tfrac12 n^3(s_{12} - s_{11})E^2 = -n^3 s_{44}E^2$.)

#### 20.2B Modulators (p. 854–856)

Solo se discuten moduladores Pockels (el mismo enfoque vale para Kerr). Hipótesis: la
dirección del campo no cambia los ejes principales y la onda está orientada de modo que las
polarizaciones de los modos normales tampoco cambian (p. 855).

**Moduladores de fase (p. 855).** Un modo normal tiene $n(E) \approx n - \tfrac12 r n^3 E$
con $n$ y $r$ los apropiados, $E = V/d$:

$$
\varphi = \varphi_o - \pi\frac{V}{V_\pi}, \qquad \varphi_o = \frac{2\pi nL}{\lambda_o}, \tag{20.2-25}
$$
$$
V_\pi = \frac{d}{L}\,\frac{\lambda_o}{r\,n^3}. \tag{20.2-26}
$$

**EJEMPLO 20.2-5 — Trigonales 3m (LiNbO$_3$, LiTaO$_3$) como moduladores de fase (p. 855).**
Campo a lo largo del eje óptico (sigue uniaxial, mismos ejes, Fig. 20.2-3).
- *Longitudinal:* onda linealmente polarizada que viaja a lo largo del eje óptico
  (paralela al campo): $n = n_o$, $r = r_{13}$, $d = L$. LiNbO$_3$ a $\lambda_o = 633$ nm:
  $r_{13} = 9.6$ pm/V, $n_o = 2.3$ → (20.2-26) da **$V_\pi = 5.41$ kV**.
- *Transversal:* onda que viaja en $x$ y polarizada en $z$: $n = n_e$, $r = r_{33}$.
  LiNbO$_3$ a 633 nm: $r_{33} = 30.9$ pm/V, $n_e = 2.2$ → **$V_\pi = 1.9\,(d/L)$ kV**; con
  $d/L = 0.1$, $V_\pi \approx 190$ V, mucho menor que en el longitudinal.

**Moduladores de intensidad (p. 855–856).** Los dos modos normales de una celda Pockels
tienen índices con distinta dependencia de $E$ → retardo dependiente del voltaje:

$$
\Gamma = \Gamma_0 - \pi\frac{V}{V_\pi}, \tag{20.2-27}
$$
$$
\Gamma_0 = \frac{2\pi(n_1 - n_2)L}{\lambda_o}, \tag{20.2-28}
$$
$$
V_\pi = \frac{(d/L)\lambda_o}{r_1 n_1^3 - r_2 n_2^3}. \tag{20.2-29}
$$

Entre polarizadores cruzados → modulador de intensidad (§20.1B).

**EJEMPLO 20.2-6 — Tetragonales $\bar 4 2m$ (KDP y ADP) (p. 856).** Campo a lo largo del
eje óptico → biaxial con ejes rotados 45°. Configuración longitudinal ($d/L = 1$), onda a lo
largo del eje óptico: los dos modos normales tienen (20.2-12) y (20.2-13), es decir
$n_1 = n_2 = n_o$, $r_1 = r_{63}$, $r_2 = -r_{63}$, $d = L$, luego $\Gamma_0 = 0$ y

$$
V_\pi = \frac{\lambda_o}{2r_{63}n_o^3}. \tag{20.2-30}
$$

Para KDP a $\lambda_o = 633$ nm: **$V_\pi = 8.4$ kV**.

**EJERCICIO 20.2-1 — Intensity Modulation Using the Kerr Effect (p. 856).** Usar (20.2-23)
y (20.2-24) para obtener el desfase $\varphi$ y el retardo $\Gamma$ de un modulador Kerr
longitudinal de medio isótropo en función de $V$, y deducir los voltajes de media onda
$V_\pi$ en cada caso. (Sin solución en el texto. Guía: en el longitudinal el campo es
paralelo a $\mathbf{k}$, así que ambas polarizaciones transversales ven $n_o(E)$ y
$\varphi = \varphi_o - \pi n^3 s_{12}(V/d)^2 L/\lambda_o$, es decir $\varphi$ cuadrático en
$V$ con $V_\pi = d\sqrt{\lambda_o/(L\,n^3 s_{12})}$; el retardo entre modos ortogonales es
nulo en esa geometría — para obtener $\Gamma \neq 0$ se necesita propagación transversal al
campo, con $\Gamma = -\pi n^3(s_{11} - s_{12})E^2L/\lambda_o$.)

---

### 20.3 Electro-Optics of Liquid Crystals (p. 856)

Las moléculas alargadas de los cristales líquidos nemáticos tienen orientaciones ordenadas
que se alteran con fuerzas mecánicas o eléctricas (§6.5). Por su anisotropía sirven como
retardadores o rotadores de polarización; con campo eléctrico, como retardadores,
moduladores e interruptores controlados eléctricamente, muy usados en pantallas (p. 856).

#### 20.3A Wave Retarders and Modulators (p. 856–861)

**Propiedades eléctricas de los nemáticos (p. 856–857).** Conductividad baja (dieléctricos
ideales). Permitividad anisótropa uniaxial: $\epsilon_\parallel$ (campo paralelo a las
moléculas) y $\epsilon_\perp$; se usan los de $\epsilon_\parallel > \epsilon_\perp$
(**uniaxial positivo**). Un campo estático induce dipolos y torques; las moléculas rotan
para minimizar la energía electrostática libre
$-\tfrac12\mathbf{E}\cdot\mathbf{D} = -\tfrac12[\epsilon_\perp E_1^2 + \epsilon_\perp E_2^2 + \epsilon_\parallel E_3^2]$
(componentes en los ejes principales). Como $\epsilon_\parallel > \epsilon_\perp$, el mínimo
se alcanza con las moléculas alineadas con el campo ($E_1 = E_2 = 0$, energía
$-\tfrac12\epsilon_\parallel E^2$) (Fig. 20.3-1). Invertir el campo produce la misma
rotación → sirve un campo AC.

**Retardadores y moduladores nemáticos (p. 857–859).** Celda: capa delgada entre dos
vidrios paralelos frotados para alinear las moléculas en paralelo → cristal uniaxial con
eje óptico a lo largo de las moléculas. Para ondas en $z$ (normal a los vidrios) los modos
normales están polarizados en $x$ (paralelo a las moléculas, índice $n_e$) y $y$ ($n_o$)
(Fig. 20.3-2a). Retardo de una celda de espesor $d$: $\Gamma = 2\pi(n_e - n_o)d/\lambda_o$.

Con campo en $z$ (voltaje $V$ en electrodos transparentes interiores), las moléculas se
inclinan hacia $z$ (Fig. 20.3-2b), salvo las adyacentes a los vidrios (fuerzas elásticas).
Ángulo de inclinación de equilibrio (de Gennes, *The Physics of Liquid Crystals*):

$$
\theta = \begin{cases} 0, & V \le V_c \\[4pt] \dfrac{\pi}{2} - 2\tan^{-1}\exp\!\left(-\dfrac{V - V_c}{V_o}\right), & V > V_c, \end{cases} \tag{20.3-1}
$$

$V$ = voltaje RMS, $V_c$ = voltaje crítico donde empieza la inclinación, $V_o$ = constante.
Cuando $V - V_c = V_o$, $\theta \approx 50°$; para $V - V_c \gg V_o$, $\theta \to 90°$
(Fig. 20.3-3a). Al quitar el campo las moléculas vuelven a su orientación original (el
material es un "líquido con memoria", p. 858).

Con inclinación $\theta$, los modos normales en $z$ siguen polarizados en $x$ y $y$, con
índices $n(\theta)$ y $n_o$:

$$
\frac{1}{n^2(\theta)} = \frac{\cos^2\theta}{n_e^2} + \frac{\sin^2\theta}{n_o^2}, \tag{20.3-2}
$$

y el retardo es $\Gamma = 2\pi[n(\theta) - n_o]d/\lambda_o$ (§6.3C), máximo
$\Gamma_{\max} = 2\pi(n_e - n_o)d/\lambda_o$ en $\theta = 0$ y decreciente a 0 en
$\theta = 90°$ (Fig. 20.3-3b, calculada con (20.3-1) y (20.3-2), $n_o = 1.5$,
$\Delta n = 0.1, 0.2, 0.3$). Nota: el ángulo entre eje óptico y propagación es $90° - \theta$,
por eso (20.3-2) difiere de (6.3-15).

- Usos (p. 858): **modulador de fase** para luz polarizada en $x$:
  $\varphi = 2\pi n(\theta)d/\lambda_o$; **retardador** para polarización a 45°; **modulador
  de intensidad**: retardador de media onda entre polarizadores cruzados a ±45°, o de
  cuarto de onda con espejo y polarizador a 45° (Fig. 20.3-4: $\Gamma = \pi/2$ en "off" → la
  polarización rota 90° en el viaje de ida y vuelta y la luz se bloquea; $\Gamma = 0$ en
  "on" → pasa).
- Datos prácticos (p. 858–859): celda sellada entre ventanas con antirreflejo; espesor
  típico $d = 10$ μm, $\Delta n = n_e - n_o = 0.1$ a $0.3$. **Retardancia**
  $\varrho = (n_e - n_o)d$, $\Gamma = 2\pi\varrho/\lambda_o$; típicas de cientos de nm
  (300 nm → $\Gamma = \pi$ a $\lambda_o = 600$ nm). Voltaje de onda cuadrada entre decenas de
  Hz y pocos kHz (más bajo: efectos electroquímicos; > 100 Hz: más consumo). $V_c$ típico:
  pocos V RMS. **Lentos**: subida de decenas de ms cerca de $V_c$, pocos ms a voltajes
  mayores; la caída no depende del voltaje, se reduce con celdas más delgadas.

**Moduladores nemáticos torcidos (p. 859–860).** Celda frotada de modo que la orientación
molecular rota helicoidalmente sobre el eje normal (eje de torsión); con torsión de 90°, las
moléculas apuntan en $x$ en una placa y en $y$ en la otra (Fig. 20.3-5a). Las capas actúan
como cristales uniaxiales con eje óptico rotando helicoidalmente; el plano de polarización
de luz linealmente polarizada que viaja a lo largo del eje de torsión rota con las
moléculas (§6.5): la celda es un **rotador de polarización**. Con campo en $z$ las
moléculas se inclinan y, a 90°, pierden el carácter torcido (salvo las junto al vidrio),
desactivándose el poder rotatorio (Fig. 20.3-5b); al quitar el campo vuelven.
- **Obturador (Fig. 20.3-6):** celda con torsión de 90° entre polarizadores cruzados:
  transmite sin campo ("bright"), bloquea con campo ("dark").
- **Modo reflectivo (Fig. 20.3-7):** torsión de 45°, espejo a un lado y polarizador al otro;
  sin campo la rotación total en ida y vuelta es 90° → bloqueado; con campo → transmitido.
- Como modulador analógico (p. 860): a inclinaciones intermedias hay combinación de rotación
  y retardo; transmitancia parcial, aprox. lineal entre totalmente torcido (transmisión
  total) y totalmente inclinado (cero), pero rango dinámico limitado.

**Cristales líquidos ferroeléctricos (p. 860–861).** Esmécticos en capas (Fig. 6.5-1b);
en fase esméctica-C la orientación molecular está inclinada un ángulo $\theta$ respecto a la
normal a las capas (eje $x$) (Fig. 20.3-8). Entre dos vidrios cercanos solo son estables
los ángulos $\pm\theta$; un campo $+E$ en $z$ conmuta a $+\theta$ y $-E$ a $-\theta$ → cristal
uniaxial cuyo eje óptico conmuta entre dos orientaciones. Con luz polarizada a $\theta$
respecto a $x$: en el estado $+\theta$ ve $n_e$ sin retardo; en $-\theta$ el plano de
polarización forma $2\theta$ con el eje óptico; si $2\theta = 45°$ el retardo es
$\Gamma = 2\pi(n_e - n_o)d/\lambda_o$ y, eligiendo $d$ para $\Gamma = \pi$, la polarización
rota 90°. Entre polarizadores cruzados → modulador de intensidad. **Tiempo de respuesta
< 20 μs** a temperatura ambiente (mucho más rápido que nemáticos); voltaje de conmutación
típico ±10 V.

#### 20.3B Spatial Light Modulators (p. 861–863)

- **LCD (p. 861–862):** electrodos transparentes con distintos patrones sobre los vidrios
  de una celda reflectiva (nemática, nemática torcida o ferroeléctrica); al aplicar voltaje
  a electrodos seleccionados se crean patrones de reflexión/no reflexión. Fig. 20.3-9:
  display de siete segmentos (0–9). Muchos electrodos se direccionan secuencialmente (p. ej.
  con CCD). Ventaja principal frente a LED: bajo consumo. Desventajas: pasivos (no sirven en
  la oscuridad); nemáticos lentos; polarizadores absorben ≥ 50 % de luz no polarizada;
  ángulo de visión limitado.
- **SLM direccionados ópticamente (p. 862–863):** la imagen de escritura $I_W(x,y)$ se
  convierte (sensor optoelectrónico) en $E(x,y)$ que controla la reflectancia
  $\mathcal{R}(x,y)$ de una celda reflectiva; una onda uniforme la lee:
  $I(x,y) \propto \mathcal{R}(x,y)$ (cf. Fig. 20.1-14). Con escritura incoherente y lectura
  coherente → convertidor incoherente-coherente (como el PROM); longitudes de onda de
  escritura y lectura pueden diferir; lectura más intensa → **intensificador de imagen**.
  Conversión $I_W \to E$: capa fotoconductora (CdS) en un capacitor → $E \propto 1/I_W$
  (negativo de la imagen); o fotodiodo $p$-$i$-$n$ de silicio amorfo hidrogenado
  ($\alpha$-Si:H) polarizado en inversa, que conduce con luz y crea un voltaje
  $\propto$ intensidad local.
- **PAL-SLM de Hamamatsu (p. 863, Fig. 20.3-10):** *Parallel Aligned Spatial Light
  Modulator*: $\alpha$-Si:H como medio de escritura + cristal líquido nemático alineado en
  paralelo como modulador de fase; capas separadas por un bloqueador de luz dieléctrico y un
  espejo dieléctrico. La luz de lectura sufre un desfase proporcional a la intensidad de
  escritura. Modulador continuo (no pixelado), resolución 480×480 puntos sobre 2×2 cm²,
  tiempos de subida/caída 30/40 ms.

---

### *20.4 Photorefractivity (p. 863)

**Idea (p. 863–864).** Los materiales fotorrefractivos tienen comportamiento fotoconductor
*y* electroóptico: detectan y almacenan patrones espaciales de intensidad como patrones de
índice de refracción. Las cargas fotoinducidas crean una distribución de carga espacial que
produce un campo eléctrico interno, el cual altera el índice vía efecto Pockels.
- Fotoconductor ordinario: aislante en la oscuridad; con luz se generan pares electrón-hueco
  y sube la conductividad; al apagar la luz vuelve al valor oscuro (detectores, §18.2).
- Fotorrefractivo: la luz excita portadores desde niveles de impureza a una banda (como
  fotoconductor extrínseco, §18.2B); los portadores **difunden** desde las zonas
  brillantes dejando cargas fijas de signo opuesto (iones de impureza) y son **atrapados**
  en otras impurezas ionizadas. Resulta una **carga espacial inhomogénea** que persiste tras
  apagar la luz y crea un campo interno que modula el índice (Pockels). Se lee con una onda
  de prueba; se borra con luz uniforme o calor. Fig. 20.4-1 (LiNbO$_3$ dopado): (1)
  fotoionización Fe$^{2+}$ → Fe$^{3+}$ (donadores), (2) difusión en banda de conducción,
  (3) recombinación en Fe$^{3+}$ (trampas) → Fe$^{2+}$, (4) formación de carga espacial,
  (5) generación de campo.
- **Materiales (p. 864):** BaTiO$_3$, Bi$_{12}$SiO$_{20}$ (BSO), LiNbO$_3$, KNbO$_3$, GaAs,
  niobato de estroncio-bario (SBN).

**Teoría simplificada (p. 864–866).** Iluminación $I(x)$ que varía en $x$ produce
$\Delta n(x)$. Pasos y ecuaciones:

- *Fotogeneración.* Tasa de fotoionización en $x$ proporcional a la intensidad y a la
  densidad de donadores no ionizados:

$$
G(x) = s\,(N_D - N_D^+)\,I(x), \tag{20.4-1}
$$

  $N_D$ = densidad de donadores, $N_D^+$ = densidad de donadores ionizados, $s$ = **sección
  eficaz de fotoionización** (constante; no confundir con el coeficiente Kerr).
- *Difusión.* Como $I(x)$ no es uniforme, la densidad de electrones excitados $n(x)$
  tampoco; difunden de alta a baja concentración. (Aquí $n(x)$ en el libro es una "n"
  sans-serif: densidad de electrones, no índice.)
- *Recombinación.* Tasa proporcional a $n(x)$ y a $N_D^+$:

$$
R(x) = \gamma_R\,n(x)\,N_D^+, \tag{20.4-2}
$$

  ($\gamma_R$ constante). En equilibrio $R(x) = G(x)$:

$$
s\,I(x)\,(N_D - N_D^+) = \gamma_R\,n(x)\,N_D^+, \tag{20.4-3}
$$
$$
n(x) = \frac{s}{\gamma_R}\,\frac{N_D - N_D^+}{N_D^+}\,I(x). \tag{20.4-4}
$$

- *Carga espacial.* Cada electrón fotogenerado deja un ion positivo; al atraparse deposita
  su carga negativa en otro sitio → distribución de carga espacial no uniforme.
- *Campo eléctrico.* En estado estacionario las densidades de corriente de deriva y de
  difusión se cancelan:

$$
J = e\mu_e\,n(x)\,E(x) - kT\mu_e\,\frac{dn}{dx} = 0, \tag{20.4-5}
$$

  ($\mu_e$ movilidad electrónica, $k$ constante de Boltzmann, $T$ temperatura), luego

$$
E(x) = \frac{kT}{e}\,\frac{1}{n(x)}\,\frac{dn}{dx}. \tag{20.4-6}
$$

- *Índice de refracción.* El campo interno modifica localmente el índice [cf. (20.1-4)]:

$$
\Delta n(x) = -\tfrac12 n^3 r\,E(x), \tag{20.4-7}
$$

  con $n$ y $r$ los valores apropiados del material.

Si $(N_D/N_D^+ - 1)$ en (20.4-4) es aproximadamente constante (independiente de $x$),
$n(x) \propto I(x)$ y

$$
E(x) = \frac{kT}{e}\,\frac{1}{I(x)}\,\frac{dI}{dx}, \tag{20.4-8}
$$

$$
\boxed{\,\Delta n(x) = -\tfrac12 n^3 r\,\frac{kT}{e}\,\frac{1}{I(x)}\,\frac{dI}{dx}\,} \tag{20.4-9}
$$

(**cambio de índice fotorrefractivo**; se generaliza a 2D → almacenamiento de imágenes).

**Supuestos (p. 866):** razón de donadores no ionizados/ionizados uniforme (válido si la
ionización la dominan otros procesos independientes de la posición); se desprecian
conductividad oscura, efectos fotovoltaicos de volumen y huecos; sin campo externo (aunque
en aplicaciones puede ser útil); solo estado estacionario (la dinámica temporal determina
la velocidad de respuesta). Aun así, captura la esencia.

**EJEMPLO 20.4-1 — Detección de un patrón sinusoidal de intensidad (p. 866–867).**

$$
I(x) = I_0\left(1 + m\cos\frac{2\pi x}{\Lambda}\right), \tag{20.4-10}
$$

(periodo $\Lambda$, contraste $m$, intensidad media $I_0$). Sustituyendo en (20.4-8) y
(20.4-9):

$$
E(x) = E_{\max}\,\frac{-\sin(2\pi x/\Lambda)}{1 + m\cos(2\pi x/\Lambda)}, \qquad \Delta n(x) = \Delta n_{\max}\,\frac{\sin(2\pi x/\Lambda)}{1 + m\cos(2\pi x/\Lambda)}, \tag{20.4-11}
$$

con $E_{\max} = 2\pi(kT/e\Lambda)\,m$ y $\Delta n_{\max} = \tfrac12 n^3 r E_{\max}$.
- Números: $\Lambda = 1$ μm, $m = 1$, $T = 300$ K → $E_{\max} = 1.6\times10^5$ V/m,
  equivalente a 1.6 kV sobre un cristal de 1 cm (p. 867).
- $\Delta n_{\max} \propto m$ y $r$, $\propto 1/\Lambda$, **independiente de $I_0$**.
- Para $m$ pequeño se desprecia el segundo término del denominador y los patrones son
  sinusoidales **desfasados 90°** respecto al patrón de luz:

$$
\Delta n(x) \approx \Delta n_{\max}\sin\frac{2\pi x}{\Lambda}. \tag{20.4-12}
$$

- Fig. 20.4-2: cadena luz no uniforme → fotoionización → difusión → campo → red de índice,
  con las curvas de $I(x)$, densidad de portadores libres, carga fija, $E(x)$ y
  $\Delta n(x)$ vs $x$.

**Aplicaciones (p. 867).**
- Almacenamiento de imágenes $I(x,y) \to \Delta n(x,y)$; lectura como modulador espacial de
  fase sobre una onda plana uniforme; conversión fase→intensidad con interferómetro.
- **Holografía en tiempo real** (§4.5): objeto + referencia forman un patrón de
  interferencia sinusoidal que se graba como variación de índice; el cristal es un holograma
  de fase de volumen (Fig. 4.5-10); iluminando con la referencia, difracta y reproduce la
  onda objeto.
- **Mezcla de dos ondas** (*two-wave mixing*, Fig. 20.4-3): grabación y reconstrucción
  simultáneas; la onda 1 se refleja en la red y se suma a la 2 y viceversa → acoplamiento;
  la transmisión de la onda 1 queda controlada por la 2 (p. ej. amplificación de 1 a costa
  de 2). También ocurre en otros medios no lineales (cap. 21). Aplicaciones (caps. 21 y 23):
  amplificación de imágenes, eliminación de aberraciones, correlación cruzada,
  interconexiones ópticas.

---

### 20.5 Electroabsorption (p. 868–869)

- **Definición (p. 868):** cambio de la absorción por campo externo. En semiconductor
  masivo, el campo produce *tunelamiento* de electrones que extiende el borde de absorción
  dentro del gap: la energía efectiva de gap se reduce por debajo de la cola de banda y la
  cola de Urbach, de modo que $h\nu_2 < h\nu_1$ con el campo ON — **efecto Franz–Keldysh**
  (Fig. 20.5-1a, b: el espectro de absorción se corre a longitudes de onda mayores). El
  campo también ensancha y acaba borrando los picos excitónicos (§16.2C).
- **Moduladores/interruptores de electroabsorción (p. 868):** a la longitud de onda de
  operación (mayor que la del gap) el haz pasa sin absorción (OFF) y se absorbe con campo
  (ON). Suelen ser guías de onda con campo perpendicular a la propagación (Fig. 20.5-1c).
  Frente a los electroópticos (índice): más rápidos y menor voltaje; integrables en un chip
  con la fuente semiconductora; menos chirp que los diodos láser modulados directamente
  (§22.1).
- **Pozos cuánticos múltiples (MQW) (p. 868–869, §16.1G y §17.2D):** campo en el plano del
  pozo → comportamiento tipo Franz–Keldysh. Campo en la dirección de confinamiento →
  **efecto Stark de confinamiento cuántico (QCSE)** (Fig. 20.5-2): (i) la diferencia de
  energía conducción–valencia disminuye con el campo ($h\nu_2 < h\nu_1$); (ii) la
  inclinación de bandas desplaza las funciones de onda hacia los bordes del pozo; (iii) la
  ionización del excitón se inhibe y sus niveles no se ensanchan ni a campos altos (el
  electrón y el hueco siguen próximos por el confinamiento). Fig. 20.5-2b: espectro de
  absorción de MQW AlGaAs/GaAs para 2, 4, 8 y 12 V (pico excitónico se mueve de ~850 a
  ~860 nm; datos de Miller *et al.*, IEEE JQE 21, 1462, 1985).
- Consecuencias: mayor corrimiento del pico y borde más abrupto que en bulk. Moduladores
  QCSE: alta velocidad, gran razón de extinción, bajo voltaje, bajo chirp. Implementación
  más simple: MQW intrínseco entre regiones $p$ y $n$ con voltaje conmutado; también en guía
  e integrado con láser DFB; o matrices en arquitectura de doble paso normal a la
  superficie (Fig. 20.5-2c).

---

### Reading List (p. 869–870)

General (ver también listas de caps. 6, 21 y 17): Lines & Glass, *Principles and
Applications of Ferroelectrics* (Clarendon 1977 / OUP 2001); Chigrinov, *Liquid Crystal
Devices* (Artech 1999); Boreman, *Basic Electro-Optics for Electrical Engineers* (SPIE
1998); Efron (ed.), *Spatial Light Modulator Technology* (Dekker 1995); Agulló-López,
Cabrera & Agulló-Rueda, *Electrooptics* (Academic 1994); Karim, *Electro-Optical Displays*
(Dekker 1992); Tamir (ed.), *Guided-Wave Optoelectronics* (Springer 1988/1990); Hutcheson
(ed.), *Integrated Optical Circuits and Components* (Dekker 1987); Gottlieb, Ireland & Ley,
*Electro-Optic and Acousto-Optic Scanning and Deflection* (Dekker 1983); Narasimhamurty,
*Photoelastic and Electro-Optic Properties of Crystals* (Plenum 1981); Pankove (ed.),
*Display Devices* (Springer 1980); Elion & Elion, *Electro-Optics Handbook* (Dekker 1979);
Nelson, *Electric, Optic, and Acoustic Interactions in Dielectrics* (Wiley 1979); Kaminow,
*An Introduction to Electrooptic Devices* (Academic 1974).

Materiales fotorrefractivos: Frejlich (Wiley 2006); Günter & Huignard (eds.),
*Photorefractive Materials and Their Applications* vols. 1–3 (Springer 2005–2006); Yu & Yin,
*Photorefractive Optics* (Academic 2000); Davidson (ed.), SPIE Milestone 86 (1994); Yeh,
*Introduction to Photorefractive Nonlinear Optics* (Wiley 1993); número especial JOSA B 7(12)
1990; Pepper, Feinberg & Kukhtarev, *Sci. Am.* 263(4), 62–74, 1990; Feinberg, *Physics Today*
41(10), 46–52, 1988; Zel'dovich, Pilipetsky & Shkunov, *Principles of Phase Conjugation*
(Springer 1985); Fisher (ed.), *Optical Phase Conjugation* (Academic 1983).

Artículos: número especial IEEE JQE QE-23(12), 1987; Miller *et al.*, "The Quantum Well
Self-Electrooptic Effect Device", IEEE JQE 21, 1462–1476, 1985; Wemple & DiDomenico,
"Electro-Optical and Nonlinear Optical Properties of Crystals", *Applied Solid State Science*
vol. 3, 263–383, 1972.

---

## Tablas y datos numéricos útiles

### Órdenes de magnitud (p. 837–838)

| Magnitud | Valor típico | Página |
|---|---|---|
| Coeficiente Pockels $r$ | $10^{-12}$–$10^{-10}$ m/V (1–100 pm/V) | 837 |
| $\tfrac12 r n^3 E$ con $E = 10^6$ V/m (10 kV / 1 cm) | $10^{-6}$–$10^{-4}$ | 837 |
| Coeficiente Kerr $s$, cristales | $10^{-18}$–$10^{-14}$ m²/V² | 837 |
| Coeficiente Kerr $s$, líquidos | $10^{-22}$–$10^{-19}$ m²/V² | 837 |
| $\tfrac12 s n^3 E^2$ con $E = 10^6$ V/m | $10^{-6}$–$10^{-2}$ (cristales); $10^{-10}$–$10^{-7}$ (líquidos) | 838 |
| $V_\pi$ longitudinal (bulk) | 1 a unos pocos kV | 838 |
| $V_\pi$ transversal (bulk) | cientos de V | 838 |
| $V_\pi$ integrado (Ti:LiNbO$_3$) | unos pocos V; > 100 GHz | 839 |
| Modulador MZ integrado | pocos GHz comerciales; > 25 GHz | 841 |
| Razón de extinción | > 30 dB (1000:1) posible | 842 |
| Acoplador direccional Ti:LiNbO$_3$ | $V_0 < 10$ V; > 10 GHz | 845–846 |
| PROM: voltaje de cebado | ≈ 4 kV | 848 |

### Coeficientes electroópticos de materiales citados en el texto y problemas

| Material | Parámetros | Página |
|---|---|---|
| LiNbO$_3$ (3m), $\lambda_o = 633$ nm | $r_{13} = 9.6$ pm/V, $r_{33} = 30.9$ pm/V, $n_o = 2.3$, $n_e = 2.2$ | 855 |
| LiNbO$_3$, $\lambda_o = 633$ nm (Prob. 20.2-6) | $n_e = 2.17$, $n_o = 2.29$, $r_{33} = 30.9$, $r_{13} = 8.6$ pm/V | 872 |
| LiNbO$_3$, $\lambda_o = 0.85$ μm (Prob. 20.2-5) | $n_o = 2.29$, $n_e = 2.17$, $r_{33} = 30.9$, $r_{13} = 8.6$, $r_{22} = 3.4$, $r_{42} = 28$ pm/V | 872 |
| KDP ($\bar 4 2m$), $\lambda_o = 633$ nm (Prob. 20.2-3) | $r_{41} = 8$ pm/V, $r_{63} = 11$ pm/V, $n_o = 1.507$, $n_e = 1.467$ | 871 |
| GaAs ($\bar 4 3m$), $\lambda_o = 1.3$ μm (Prob. 20.1-2) | $n = 3.6$, $r = 1.6$ pm/V, $\epsilon/\epsilon_o = 13.5$ | 871 |
| Sílice polada (Prob. 20.2-2), $\lambda = 1.55$ μm | $n = 1.445$, $r_{13} = 0.15$ pm/V | 871 |

### Voltajes de media onda calculados en el texto

| Configuración | $V_\pi$ | Ecuación | Página |
|---|---|---|---|
| LiNbO$_3$ longitudinal, 633 nm ($n_o$, $r_{13}$) | 5.41 kV | (20.2-26) | 855 |
| LiNbO$_3$ transversal, 633 nm ($n_e$, $r_{33}$) | $1.9\,(d/L)$ kV; 190 V si $d/L = 0.1$ | (20.2-26) | 855 |
| KDP longitudinal (intensidad), 633 nm | 8.4 kV | (20.2-30) | 856 |

### Tabla 20.2-1 — Índice contraído $I \leftrightarrow (i,j)$ (p. 850)

$(1,1)\to1$, $(2,2)\to2$, $(3,3)\to3$, $(2,3)=(3,2)\to4$, $(1,3)=(3,1)\to5$, $(1,2)=(2,1)\to6$.

### Tabla 20.2-2 — Coeficientes Pockels $r_{Ik}$ (matrices 6×3, filas $I = 1..6$, columnas $k = 1,2,3$) (p. 851)

Cúbico $\bar 4 3m$ (GaAs, CdTe, InAs):

$$
\begin{bmatrix} 0&0&0\\ 0&0&0\\ 0&0&0\\ r_{41}&0&0\\ 0&r_{41}&0\\ 0&0&r_{41}\end{bmatrix}
$$

Tetragonal $\bar 4 2m$ (KDP, ADP):

$$
\begin{bmatrix} 0&0&0\\ 0&0&0\\ 0&0&0\\ r_{41}&0&0\\ 0&r_{41}&0\\ 0&0&r_{63}\end{bmatrix}
$$

Trigonal $3m$ (LiNbO$_3$, LiTaO$_3$):

$$
\begin{bmatrix} 0&-r_{22}&r_{13}\\ 0&r_{22}&r_{13}\\ 0&0&r_{33}\\ 0&r_{51}&0\\ r_{51}&0&0\\ -r_{22}&0&0\end{bmatrix}
$$

### Tabla 20.2-3 — Coeficientes Kerr $s_{IK}$ de un medio isótropo (6×6) (p. 851)

$$
\begin{bmatrix}
s_{11}&s_{12}&s_{12}&0&0&0\\
s_{12}&s_{11}&s_{12}&0&0&0\\
s_{12}&s_{12}&s_{11}&0&0&0\\
0&0&0&s_{44}&0&0\\
0&0&0&0&s_{44}&0\\
0&0&0&0&0&s_{44}
\end{bmatrix}, \qquad s_{44} = \tfrac12(s_{11} - s_{12}).
$$

### Cristales líquidos (p. 858–861, 863)

| Magnitud | Valor | Página |
|---|---|---|
| Espesor típico de celda nemática | $d = 10$ μm | 858 |
| $\Delta n = n_e - n_o$ | 0.1–0.3 | 858 |
| Retardancia $\varrho = (n_e - n_o)d$ | cientos de nm (300 nm → $\Gamma = \pi$ a 600 nm) | 859 |
| Voltaje de excitación | onda cuadrada, decenas de Hz a pocos kHz; $V_c$ pocos V RMS | 859 |
| Tiempo de subida nemático | decenas de ms (cerca de $V_c$) a pocos ms | 859 |
| Ángulo de inclinación con $V - V_c = V_o$ | $\theta \approx 50°$ | 858 |
| Ferroeléctrico: respuesta / voltaje | < 20 μs / ±10 V | 861 |
| PAL-SLM Hamamatsu | 480×480 puntos, 2×2 cm², subida 30 ms, caída 40 ms | 863 |

### Fotorrefractividad (p. 864–867)

- Materiales: BaTiO$_3$, Bi$_{12}$SiO$_{20}$, LiNbO$_3$, KNbO$_3$, GaAs, SBN (p. 864).
- $E_{\max} = 2\pi(kT/e\Lambda)m$; para $\Lambda = 1$ μm, $m = 1$, $T = 300$ K:
  $E_{\max} = 1.6\times10^5$ V/m (≈ 1.6 kV sobre 1 cm) (p. 867). ($kT/e \approx 25.9$ mV a
  300 K.)
- $\Delta n_{\max} = \tfrac12 n^3 r E_{\max}$, independiente de $I_0$ (p. 867).

---

## Problemas al final del capítulo (p. 871–872)

La numeración salta 20.1-1 y 20.2-1 porque esos números corresponden a los ejercicios del
texto (Ejercicio 20.1-1, p. 846; Ejercicio 20.2-1, p. 856). Los marcados con * son
avanzados.

- **20.1-2 Response Time of a Phase Modulator (p. 871).** Cristal de GaAs ($n = 3.6$,
  $r = 1.6$ pm/V) como modulador de fase a $\lambda_o = 1.3$ μm en configuración
  longitudinal; 1 cm de largo y 1 cm² de sección. Hallar $V_\pi$, el tiempo de tránsito de la
  luz y la capacitancia eléctrica ($\epsilon/\epsilon_o = 13.5$ a baja frecuencia). Con una
  fuente de 50 Ω, ¿qué limita la velocidad: el tránsito o el tiempo de respuesta del
  circuito?
- **20.1-3 Sensitivity of an Interferometric Electro-Optic Intensity Modulator (p. 871).**
  Modulador MZ integrado (Fig. 20.1-5) como modulador lineal; si $V_\pi = 10$ V, hallar la
  sensibilidad (cambio de transmitancia por cambio unitario de voltaje).
- **20.1-4 An Elasto-Optic Strain Sensor (p. 871).** Material cuyo índice cambia
  proporcionalmente a la deformación; diseñar un sensor de deformación (versión integrada);
  si además es electroóptico, diseño que compense el cambio elastoóptico con el
  electroóptico y mida el campo que anula la lectura del fotodetector en un MZ.
- **20.1-5 Magneto-Optic Modulators (p. 871).** Describir cómo usar un rotador de Faraday
  (§6.4B) como modulador de intensidad.
- ***20.2-2 Silica Integrated-Optic Phase Modulator (p. 871).** Sílice polada térmicamente
  (la sílice masiva es centrosimétrica, sin Pockels). Modulador de fase como el de la
  Fig. 20.1-3 con $L = 25$ mm, $d = 30$ μm, $\lambda = 1.55$ μm, $V = 400$ V; onda polarizada en
  $y$, campo en $y$, propagación en $z$ (entre los electrodos); ejes principales
  $(x_1,x_2,x_3)$ en $z, x, y$; $n = 1.445$; matriz Pockels con filas
  $[0,0,r_{13}]$, $[0,0,r_{13}]$, $[0,0,r_{33}]$, $[0,r_{13},0]$, $[r_{13},0,0]$, $[0,0,0]$ y
  $r_{13} = 0.15$ pm/V. Hallar el desfase introducido.
- ***20.2-3 Cascaded Phase Modulators (p. 871).** (a) KDP ($r_{41} = 8$ pm/V,
  $r_{63} = 11$ pm/V; $n_o = 1.507$, $n_e = 1.467$ a 633 nm) como modulador de fase
  longitudinal con la orientación de los Ejemplos 20.2-2 y 20.2-6: hallar $V_\pi$.
  (b) Modulador compuesto por 9 cristales KDP separados por electrodos alternados
  (Fig. P20.2-3): cómo orientar las placas para maximizar la modulación total y calcular el
  $V_\pi$ compuesto.
- ***20.2-4 The "Push–Pull" Intensity Modulator (p. 872).** Dos moduladores de fase
  integrados (voltajes $+V$ y $-V$) y un acoplador direccional de 3 dB (Fig. P20.2-4); la
  entrada se divide en dos ondas de igual amplitud, cada una modulada en fase, reflejada en
  un espejo, modulada de nuevo y recombinada. Deducir la transmitancia de intensidad en
  función de voltaje, longitud de onda, dimensiones y parámetros físicos.
- ***20.2-5 A LiNbO$_3$ Integrated-Optic Intensity Modulator (p. 872).** Diseñar un
  modulador MZ en LiNbO$_3$ (Fig. 20.1-5) eligiendo orientación del cristal y polarización
  de la onda guiada para el menor $V_\pi$. Región activa $L = 1$ mm, $d = 5$ μm,
  $\lambda_o = 0.85$ μm, $n_o = 2.29$, $n_e = 2.17$, $r_{33} = 30.9$, $r_{13} = 8.6$,
  $r_{22} = 3.4$, $r_{42} = 28$ pm/V.
- ***20.2-6 Double Refraction in an Electro-Optic Crystal (p. 872).** (a) Haz He–Ne
  ($\lambda_o = 633$ nm) no polarizado a través de una placa de LiNbO$_3$ de 1 cm
  ($n_e = 2.17$, $n_o = 2.29$, $r_{33} = 30.9$, $r_{13} = 8.6$ pm/V); haz normal a la placa,
  eje óptico en el plano de incidencia a 45° del haz; doble refracción (§6.3E). Hallar el
  desplazamiento lateral y el retardo entre haces ordinario y extraordinario. (b) Con
  $E = 30$ V/m paralelo al eje óptico, ¿qué efecto tiene sobre los haces transmitidos y qué
  aplicaciones tiene el dispositivo?

---

## Relación con Óptica No Lineal

### Pockels ↔ $\chi^{(2)}$ y Kerr ↔ $\chi^{(3)}$, $n_2$

- El capítulo es, en esencia, óptica no lineal con **una de las ondas a frecuencia cero**.
  Con la convención del curso, $\tilde P = \epsilon_0[\chi^{(1)}\tilde E + \chi^{(2)}\tilde E^2 + \chi^{(3)}\tilde E^3 + \cdots]$,
  si el campo total es óptico + estático, el término $\chi^{(2)}\tilde E^2$ contiene un
  producto cruzado $2\chi^{(2)}E_{\rm opt}E_{\rm dc}$ que oscila a $\omega$ y actúa como una
  susceptibilidad lineal extra: $n^2(E) = 1 + \chi^{(1)} + 2\chi^{(2)}E_{\rm dc}$, luego
  $n(E) \approx n + \chi^{(2)}E_{\rm dc}/n$. Comparando con (20.1-4), $\Delta n = -\tfrac12 r n^3 E$:

$$
r \;\leftrightarrow\; -\frac{2\chi^{(2)}(\omega;\omega,0)}{n^4}, \qquad\text{(forma escalar)}
$$

  y en forma tensorial $r_{ijk} \leftrightarrow -2\chi^{(2)}_{ijk}(\omega;\omega,0)/(n_i^2 n_j^2)$,
  porque $\Delta\eta_{ij} = -\Delta\epsilon_{ij}/(\epsilon_0 n_i^2 n_j^2)$. **Aviso:** el
  prefactor exacto (2, 1 o ½) depende de la convención de factores de degeneración de
  $\chi^{(2)}$ (Boyd, *Nonlinear Optics*, 3.ª ed., cap. 11 "The Electrooptic and
  Photorefractive Effects" y §1.5 para las propiedades de simetría); al citar, fijar la
  convención. Lo que sí es independiente de convención: Pockels **solo existe en medios
  no centrosimétricos**, exactamente como $\chi^{(2)}$ (p. 837 ↔ Boyd §1.5.1); por eso el
  Prob. 20.2-2 necesita *sílice polada*, que es también lo que se hace para obtener SHG en
  fibras y en Si$_3$N$_4$.
- La simetría $r_{ijk} = r_{jik}$ y el índice contraído $I \leftrightarrow (i,j)$ (Tabla 20.2-1)
  son la **misma contracción** usada para $d_{il}$ en SHG (Boyd §1.5.9, notación $d_{il}$ con
  $l = 1..6$). La diferencia: en $r_{Ik}$ el par simétrico son los índices del elipsoide
  $(i,j)$ y el índice libre es el del campo estático $k$; en $d_{il}$ el par simétrico son
  los dos campos ópticos. Las matrices de la Tabla 20.2-2 tienen la misma estructura de
  ceros que las de $d$ para los grupos $\bar 4 3m$, $\bar 4 2m$ y $3m$ (la transpuesta,
  por el intercambio de papeles).
- **Kerr DC ↔ $\chi^{(3)}$:** el término $\chi^{(3)}\tilde E^3$ con dos factores estáticos
  da $n^2(E) = n^2 + 3\chi^{(3)}E_{\rm dc}^2$, $\Delta n = 3\chi^{(3)}E_{\rm dc}^2/(2n)$;
  comparando con (20.1-5), $s \leftrightarrow -3\chi^{(3)}(\omega;\omega,0,0)/n^4$ (misma
  salvedad de convención). Kerr existe en **todos** los medios, incluidos los
  centrosimétricos, como $\chi^{(3)}$ (p. 837).
- **Kerr óptico e índice dependiente de la intensidad:** si el "campo aplicado" es el
  propio campo óptico, el promedio temporal de $E^2$ es $\propto I$ y (20.1-5) se convierte en
  $n = n_0 + n_2 I$, con $n_2 = 3\chi^{(3)}/(4n_0^2\epsilon_0 c)$ en SI (Boyd §4.1,
  ec. (4.1.19)). Ese es el origen de SPM, XPM, autoenfoque, solitones y FWM en fibras y
  guías. El Ejemplo 20.2-4 (medio isótropo se vuelve uniaxial con eje óptico a lo largo de
  $E$, con $n_e - n_o = -n^3 s_{44}E^2$) es el análogo estático de la **birrefringencia
  inducida por un haz intenso** y de la rotación de polarización no lineal (Boyd §4.2).
- **Signo de la convención:** Saleh define $r$ y $s$ para que $\Delta\eta = rE + sE^2$ sea
  positivo con coeficientes positivos (20.1-3), luego $\Delta n < 0$ para $r, s > 0$. En ONL
  se habla de $n_2 > 0$ (autoenfoque) para la mayoría de vidrios; el signo no se mapea
  directamente porque $\chi^{(3)}$ incluye contribuciones electrónicas y de otros orígenes.

### Temas del curso

- **Ondas EM, absorción y dispersión:** el capítulo asume $n$ real; la electroabsorción
  (§20.5) es el caso en que el campo cambia la parte imaginaria (Kramers–Kronig liga ese
  cambio de absorción con un cambio de índice, útil para discutir Franz–Keldysh/QCSE).
- **Polarización y cristales (taller 02):** la §20.2 es la aplicación directa del elipsoide
  de índices, impermeabilidad $\eta = \epsilon_o\epsilon^{-1}$, modos normales y retardo
  $\Gamma = k_o(n_1 - n_2)L$ (§6.3). Los ejemplos 20.2-1/2/3 muestran los tres casos
  canónicos: uniaxial que sigue uniaxial (LiNbO$_3$), uniaxial → biaxial con ejes rotados 45°
  (KDP), isótropo → biaxial (GaAs). Los retardadores dinámicos (20.1-12)–(20.1-13) y los
  moduladores entre polarizadores cruzados (20.1-16) son el formalismo de Jones de §6.6B.
- **Susceptibilidad no lineal, $\chi^{(2)}$ y $\chi^{(3)}$:** ver arriba. Además el método
  de los 6 pasos (p. 851) es exactamente lo que se hace para $d_{\rm eff}$ en un cristal
  para SHG: elegir ejes, contraer índices, proyectar sobre polarizaciones.
- **Índice dependiente de la intensidad, SPM/XPM/solitones, FWM, Raman:** Kerr óptico;
  la fotorrefractividad (§20.4) es *otro* mecanismo de "luz controla luz" (lento, de
  carga espacial, no instantáneo), con su propia mezcla de dos ondas y conjugación de fase
  (cap. 21 de Saleh; Boyd cap. 11). Útil para contrastar con el Kerr electrónico
  instantáneo de los solitones.
- **Pulsos en medios dispersivos, GVD:** la limitación por tiempo de tránsito y el
  modulador de onda viajera (p. 838–839) es un problema de **ajuste de velocidades** entre
  onda eléctrica y óptica, el mismo tipo de condición que el ajuste de fase/velocidad de
  grupo en SHG y en generación de supercontinuo.

### Proyecto final (anillos add-drop en Si$_3$N$_4$, dispersión de guías, supercontinuo, sensado)

- **Si$_3$N$_4$ es centrosimétrico (amorfo):** no tiene Pockels ni $\chi^{(2)}$ nativos (solo
  Kerr/$\chi^{(3)}$, p. 837 ↔ 20.1-5); cualquier modulación electroóptica en la plataforma
  requeriría poling (Prob. 20.2-2 muestra que el $r_{13}$ de sílice polada es ~0.15 pm/V,
  200× menor que el $r_{33}$ de LiNbO$_3$) o calentadores térmicos. El supercontinuo en SiN
  se apoya exclusivamente en $\chi^{(3)}$ (SPM, FWM, solitones), que es la versión óptica
  de (20.1-5).
- **Anillo add-drop como sensor:** el mismo principio que los moduladores: un $\Delta n$
  pequeño ($10^{-6}$–$10^{-4}$) acumulado sobre muchas longitudes de onda produce un
  desfase medible (p. 835). En el anillo el "modulador" es el cambio de índice del cladding
  ($n = 1.33 \to 1.37$) y la lectura es el corrimiento de la resonancia; la sensibilidad
  $\partial\mathcal{T}/\partial V$ de (20.1-17) tiene su análogo en $\partial\lambda_{\rm res}/\partial n_{\rm clad}$.
  La Fig. 20.1-4 (MZ con punto de polarización en $\mathcal{T} = 0.5$ para respuesta lineal)
  es el mismo criterio de operar el anillo en el flanco de la resonancia.
- **Acoplador direccional (20.1D):** las ecuaciones (20.1-21)–(20.1-23) con $\mathcal{C}$,
  $L_0 = \pi/2\mathcal{C}$ y $\Delta\beta$ son el modelo de **teoría de modos acoplados**
  del acoplador bus–anillo del add-drop (coeficiente de acoplo $\kappa$ y transmisión $t$ de
  la región de acoplo). La dependencia espectral del Ejercicio 20.1-1 ($V_0 \propto
  \lambda_o$) recuerda que $\mathcal{C}(\lambda)$ varía con la longitud de onda — relevante
  al diseñar el gap para acoplo crítico en todo el rango del supercontinuo.
- **Modulador MZ integrado (Fig. 20.1-5) y modulador de fase integrado (Fig. 20.1-3):**
  si en el futuro se quiere un lazo de realimentación o un interrogador para el sensor, la
  solución integrada estándar es un MZ en LiNbO$_3$ con $V_\pi$ de pocos voltios.
- **Fotorrefractividad (§20.4):** no aplica directamente a SiN, pero el formalismo de
  "red de índice grabada por un patrón de intensidad desfasada 90°" (20.4-12) es el mismo
  que aparece en mezcla de dos ondas y en redes de Bragg fotoinducidas; sirve de contraste
  con las redes de índice **instantáneas** creadas por Kerr en FWM.
