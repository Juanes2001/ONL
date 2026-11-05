# Capítulo 15 — Lasers (Saleh & Teich, 2.ª ed.)

Páginas del libro 567–626 (PDF 589–648). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 15.
Convención del libro: dependencia temporal $e^{j\omega t}$, $j=\sqrt{-1}$; $c = c_o/n$ es la velocidad
de la luz **en el medio**; $\lambda = \lambda_o/n$ es la longitud de onda en el medio; $\nu$ es la
frecuencia (Hz); $\phi$ es la densidad de flujo de fotones (fotones s⁻¹ m⁻²); $\mathfrak{n}$ es la
densidad de número de fotones (fotones m⁻³); $N$ es la diferencia de población por unidad de
volumen; $\mathcal{R}_i$ y $\mathcal{T}$ son reflectancia y transmitancia (en intensidad) de los
espejos; $\mathcal{F}$ es la fineza del resonador. Las ecuaciones enmarcadas en el libro se marcan
aquí con **[recuadro]**.

---

## Resumen del capítulo

El capítulo presenta el láser como un oscilador óptico: un amplificador resonante (medio activo
bombeado, cap. 14) con realimentación (resonador óptico, cap. 10) y un mecanismo de saturación de
ganancia que fija la amplitud en estado estacionario. La §15.1 resume ganancia, corrimiento de fase,
pérdidas y modos del resonador, y deduce las dos condiciones de oscilación: la de **ganancia**
(umbral, $N_0 > N_t$) y la de **fase** (frecuencias $\nu_q$, con *frequency pulling*). La §15.2
obtiene la potencia de salida (clampeo de ganancia, flujo interno y externo, transmitancia óptima,
eficiencias de extracción, de conversión y de pendiente), la distribución espectral (medios
homogéneos vs. inhomogéneos, *spatial* y *spectral hole burning*, Lamb dip), la distribución
espacial (modos TEM$_{l,m,q}$, polarización, resonadores inestables) y las técnicas de selección de
línea, de modo transversal, de polarización y de modo longitudinal (etalón, resonadores acoplados).
La §15.3 recorre los láseres comunes: de estado sólido (Nd:YVO₄, Nd:YAG, Yb:YAG, Ti:zafiro, láseres de
fibra, láseres Raman de fibra, láseres aleatorios), de gas (atómicos/iónicos, moleculares, excímeros,
químicos), otros (colorantes, EUV/rayos X, electrones libres) y una tabla de características
(Tabla 15.3-1). La §15.4 trata los láseres pulsados: métodos (conmutación de ganancia, Q-switching,
*cavity dumping*, mode locking), ecuaciones de tasa transitorias para $\mathfrak{n}(t)$ y $N(t)$,
análisis del Q-switching (potencia pico, energía, duración) y teoría del mode locking (tren de
pulsos de $M$ modos, $\tau_{\rm pulse}\approx 1/\Delta\nu$, métodos activo y pasivo: absorbedor
saturable, SESAM, Kerr-lens), con tabla de duraciones (Tabla 15.4-2) y ejemplos de Ti:zafiro (10 fs)
y fibra de Yb.

---

## Secciones

### Introducción (p. 568–569)

- Un láser es un **oscilador óptico**: amplificador óptico resonante cuya salida se realimenta a la
  entrada con fase coincidente (Fig. 15.0-1). El ruido a la entrada dentro del ancho de banda del
  amplificador inicia la oscilación; la **saturación de la ganancia** limita el crecimiento y fija el
  estado estacionario (Fig. 15.0-2: la ganancia cae con la potencia hasta igualar la pérdida).
- Dos condiciones para oscilar (p. 568): (i) ganancia del amplificador > pérdida del lazo de
  realimentación; (ii) desfase total en una vuelta = múltiplo de $2\pi$.
- Un oscilador consta de: amplificador con saturación de ganancia, sistema de realimentación,
  mecanismo de selección de frecuencia y esquema de acoplamiento de salida.
- En el láser (Fig. 15.0-3, p. 569): el amplificador es el medio activo bombeado (§14.1, 14.2),
  la saturación se trata en §14.4, la realimentación la da el resonador (cap. 10) y la salida se
  extrae por un espejo parcialmente transmisor. Precursor: el **máser** (microondas); análogo
  acústico: **sáser** (fonones).

### 15.1 Theory of Laser Oscillation (p. 569)

#### 15.1A Optical Amplification and Feedback (p. 569)

**Amplificación láser (p. 569–571).** Amplificador coherente de banda estrecha por emisión
estimulada en una transición con población invertida. El ancho de banda lo fija el ancho de línea
de la transición (o un ensanchamiento inhomogéneo, p. ej. Doppler en gases). Es un dispositivo de
ganancia distribuida con coeficiente de ganancia $\gamma(\nu)$ (ganancia por unidad de longitud),
que gobierna el crecimiento de $\phi$ (o de $I = h\nu\,\phi$).

- **Coeficiente de ganancia de señal pequeña [recuadro]** (p. 570):
  $$\gamma_0(\nu) = N_0\,\sigma(\nu) = N_0\,\frac{\lambda^2}{8\pi t_{\rm sp}}\,g(\nu) \qquad (15.1\text{-}1)$$
  con $N_0$ = diferencia de densidad de población en equilibrio (superior − inferior; crece con
  el bombeo), $\sigma(\nu) = (\lambda^2/8\pi t_{\rm sp})\,g(\nu)$ = sección eficaz de la transición,
  $t_{\rm sp}$ = tiempo de vida espontáneo, $g(\nu)$ = forma de línea, $\lambda = \lambda_o/n$.
- Saturación: $N = N_0/[1+\phi/\phi_s(\nu)]$ (medio homogéneo), con
  $\phi_s(\nu) = [\tau_s\,\sigma(\nu)]^{-1}$ = densidad de flujo de saturación y $\tau_s$ = constante
  de tiempo de saturación ($\tau_s \approx t_{\rm sp}$ en 4 niveles ideal; $\tau_s = 2t_{\rm sp}$ en
  3 niveles ideal).
- **Coeficiente de ganancia saturado [recuadro]** (p. 570):
  $$\gamma(\nu) = \frac{\gamma_0(\nu)}{1+\phi/\phi_s(\nu)} \qquad (15.1\text{-}2)$$
- **Coeficiente de desfase (forma de línea lorentziana) [recuadro]** (p. 570): con
  $g(\nu) = (\Delta\nu/2\pi)/[(\nu-\nu_0)^2 + (\Delta\nu/2)^2]$, el desfase por unidad de longitud
  que añade el amplificador es
  $$\varphi(\nu) = \frac{\nu-\nu_0}{\Delta\nu}\,\gamma(\nu) \qquad (15.1\text{-}3)$$
  (adicional al del medio huésped). Fig. 15.1-1 (p. 571): $\gamma(\nu)$ es un pico lorentziano de
  ancho $\Delta\nu$ en $\nu_0$; $\varphi(\nu)$ es antisimétrico (negativo bajo $\nu_0$, positivo
  encima).

**Realimentación y pérdidas: el resonador óptico (p. 571–572).** Fabry–Perot de dos espejos
separados $d$, medio de índice $n$.

- **Coeficiente de desfase del medio [recuadro]** (p. 571): $k = 2\pi\nu/c$ (15.1-4).
- Pérdidas: absorción y dispersión en el medio → $\alpha_s$ (pérdida por unidad de longitud). En
  una vuelta el flujo se reduce por $\mathcal{R}_1\mathcal{R}_2\exp(-2\alpha_s d)$. Se define el
  **coeficiente de pérdida distribuida efectivo** $\alpha_r$ por
  $\exp(-2\alpha_r d) = \mathcal{R}_1\mathcal{R}_2\exp(-2\alpha_s d)$ (15.1-5), de donde
  **[recuadro]** (p. 571):
  $$\alpha_r = \alpha_s + \alpha_{m1} + \alpha_{m2},\qquad
    \alpha_{m1} = \frac{1}{2d}\ln\frac{1}{\mathcal{R}_1},\qquad
    \alpha_{m2} = \frac{1}{2d}\ln\frac{1}{\mathcal{R}_2} \qquad (15.1\text{-}6)$$
  y la contribución de ambos espejos $\alpha_m = \alpha_{m1}+\alpha_{m2} = \frac{1}{2d}\ln\frac{1}{\mathcal{R}_1\mathcal{R}_2}$ (15.1-7).
- **Tiempo de vida del fotón** (p. 572): $\alpha_r c$ es la pérdida de fotones por segundo, luego
  $$\tau_p = \frac{1}{\alpha_r c} \qquad (15.1\text{-}8)$$
- Modos del resonador "frío" (sin átomos activos): desfase en una vuelta $k\,2d = 2\pi\nu d/c = q2\pi$
  → $\nu_q = q\,\nu_F$, $q=1,2,\dots$ (15.1-9), con $\nu_F = c/2d$ = separación entre modos
  ($c = c_o/n$). Ancho espectral FWHM de cada modo: $\delta\nu \approx \nu_F/\mathcal{F}$ (15.1-10),
  y con pérdidas pequeñas / fineza grande:
  $$\mathcal{F} \approx \frac{\pi}{\alpha_r d} = 2\pi\tau_p\,\nu_F \qquad (15.1\text{-}11)$$
  Fig. 15.1-2 (p. 572): peine de modos separados $\nu_F = c/2d$ con ancho
  $\delta\nu = \nu_F/\mathcal{F} = 1/2\pi\tau_p$.

#### 15.1B Conditions for Laser Oscillation (p. 572)

**Condición de ganancia: umbral láser (p. 572–574).**
- **[recuadro]** $\gamma_0(\nu) > \alpha_r$ (15.1-12), condición de ganancia umbral. Con
  $\gamma_0 = N_0\sigma$ se traduce a $N_0 > N_t$ (15.1-13), con la **diferencia de población umbral**
  $$N_t = \frac{\alpha_r}{\sigma(\nu)} \qquad (15.1\text{-}14) \qquad\Longleftrightarrow\qquad
    N_t = \frac{1}{c\,\tau_p\,\sigma(\nu)} \qquad (15.1\text{-}15)$$
  ($N_t \propto \alpha_r$, $\propto 1/\tau_p$: más pérdida ⇒ más bombeo). $N_t$ determina la tasa
  de bombeo mínima $R_t$.
- **[recuadro] Diferencia de población umbral** (p. 573), usando $\sigma = (\lambda^2/8\pi t_{\rm sp})g$:
  $$N_t = \frac{8\pi\,t_{\rm sp}}{\lambda^2\,\tau_p}\,\frac{1}{g(\nu)} \qquad (15.1\text{-}16)$$
  El umbral es mínimo donde $g(\nu)$ es máximo ($\nu=\nu_0$). Para lorentziana $g(\nu_0)=2/\pi\Delta\nu$:
  $$N_t = \frac{2\pi}{\lambda^2 c}\,\frac{2\pi\,\Delta\nu\,t_{\rm sp}}{\tau_p} \qquad (15.1\text{-}17)$$
  ($\propto \Delta\nu$). Si además el ensanchamiento es solo por tiempo de vida,
  $\Delta\nu = 1/2\pi t_{\rm sp}$ (§13.3D):
  $$N_t = \frac{2\pi}{\lambda^2 c\,\tau_p} = \frac{2\pi\alpha_r}{\lambda^2} \qquad (15.1\text{-}18)$$
  Oscilar es más difícil a $\lambda$ menores. Ejemplo numérico (p. 573): $\lambda_o = 1\ \mu$m,
  $\tau_p = 1$ ns, $n=1$ ⇒ $N_t \approx 2.1\times10^7$ cm⁻³.

**Ejercicio 15.1-1 — Umbral de un láser de rubí (p. 574).** (a) En el centro de la línea
$\lambda_o = 694.3$ nm, el coeficiente de absorción del rubí sin bombeo a $T=300$ K es
$\alpha(\nu_0) \equiv -\gamma(\nu_0) \approx 0.2$ cm⁻¹; con $N_a = 1.58\times10^{19}$ cm⁻³ de
Cr³⁺, hallar $\sigma_0 = \sigma(\nu_0)$. (b) Barra de rubí de 10 cm, $n = 1.76$, sección 1 cm²,
extremos pulidos con reflectancia 80 % cada uno, sin otras pérdidas: hallar $\alpha_r$ y $\tau_p$.
(c) Hallar $N_t$. (El libro no da la solución; con las fórmulas: $\sigma_0 = \alpha/N_a$,
$\alpha_r = \frac{1}{2d}\ln\frac{1}{0.8^2}$, $\tau_p = 1/\alpha_r c$ con $c = c_o/1.76$,
$N_t = \alpha_r/\sigma_0$.)

**Condición de fase: frecuencias del láser (p. 574–575).** Desfase total en una vuelta:
$$2kd + 2\varphi(\nu)d = 2\pi q,\qquad q = 1,2,\dots \qquad (15.1\text{-}19)$$
Si $2\varphi(\nu)d$ es pequeño, $\nu = \nu_q = q(c/2d)$ (resonador frío). Con el medio activo se
obtienen frecuencias $\nu'_q$ ligeramente desplazadas, siempre **atraídas hacia $\nu_0$**.

**\*Frequency pulling (p. 574–575).** Con $k = 2\pi\nu/c$ y (15.1-3), la condición (15.1-19) da
$$\nu + \frac{c}{2\pi}\,\frac{\nu-\nu_0}{\Delta\nu}\,\gamma(\nu) = \nu_q \qquad (15.1\text{-}20)$$
Solución gráfica (Fig. 15.1-3, p. 575): el lado izquierdo $\psi(\nu)$ es una recta más la curva
antisimétrica $\varphi$; la intersección $\psi(\nu) = \nu_q$ da $\nu'_q$. Solución aproximada:
escribiendo $\nu = \nu_q - \frac{c}{2\pi}\frac{\nu-\nu_0}{\Delta\nu}\gamma(\nu)$ (15.1-21) y
sustituyendo $\nu\approx\nu_q$ en el término pequeño,
$$\nu'_q = \nu_q - \frac{c}{2\pi}\,\frac{\nu_q-\nu_0}{\Delta\nu}\,\gamma(\nu_q) \qquad (15.1\text{-}22)$$
En estado estacionario $\gamma(\nu_q) = \alpha_r \approx \pi/\mathcal{F}d = (2\pi/c)\,\delta\nu$, luego
**[recuadro] Frecuencias del láser** (p. 575):
$$\nu'_q \approx \nu_q - (\nu_q-\nu_0)\,\frac{\delta\nu}{\Delta\nu} \qquad (15.1\text{-}23)$$
El modo frío se atrae hacia $\nu_0$ una fracción $\delta\nu/\Delta\nu$ de su distancia a $\nu_0$:
modos más agudos (menor $\delta\nu$) ⇒ menos *pulling*; línea atómica más estrecha ⇒ más *pulling*.
Fig. 15.1-4 (p. 576): ganancia $\gamma(\nu)$, modos fríos, y modos de oscilación corridos hacia $\nu_0$.

### 15.2 Characteristics of the Laser Output (p. 575)

#### 15.2A Power (p. 575)

**Densidad de flujo de fotones interna (p. 575–577).** Con $N_0 > N_t$, $\phi$ crece y $\gamma(\nu)$
baja según (15.1-2) hasta que $\gamma = \alpha_r$ (equivalente a $N = N_t$): **gain clamping**, la
ganancia se "clampea" al valor de la pérdida (Fig. 15.2-1, p. 576). De
$\gamma_0(\nu)/[1+\phi/\phi_s(\nu)] = \alpha_r$:
$$\phi = \begin{cases}\phi_s(\nu)\left(\dfrac{\gamma_0(\nu)}{\alpha_r}-1\right), & \gamma_0(\nu) > \alpha_r\\[4pt] 0, & \gamma_0(\nu)\le\alpha_r\end{cases} \qquad (15.2\text{-}1)$$
Es el flujo medio total de fotones **en ambas direcciones** (los dos sentidos contribuyen a la
saturación); en un solo sentido es $\phi/2$. Se desprecia la emisión espontánea (fluctuaciones:
§12.2). **[recuadro] Densidad de flujo interna en estado estacionario** (p. 577):
$$\phi = \begin{cases}\phi_s(\nu)\left(\dfrac{N_0}{N_t}-1\right), & N_0 > N_t\\[4pt] 0, & N_0\le N_t\end{cases} \qquad (15.2\text{-}2)$$
Bajo umbral $\phi=0$ (solo crece la emisión espontánea); sobre umbral $\phi \propto N_0 - N_t$, es
decir, crece linealmente con el bombeo $R$ [(14.2-13), (14.2-27)]. Si $N_0 = 2N_t$, $\phi = \phi_s$.
Fig. 15.2-2 (p. 577): $N$ crece con $N_0$ hasta $N_t$ y se clampea; $\phi$ es cero hasta $N_t$ y
luego lineal (vale $\phi_s$ en $2N_t$).

**Densidad de flujo de salida (p. 577).** Si el espejo 1 tiene transmitancia $\mathcal{T}$:
$$\phi_o = \frac{\mathcal{T}\phi}{2}\quad(15.2\text{-}3),\qquad I_o = \frac{h\nu\,\mathcal{T}\phi}{2}\quad(15.2\text{-}4),\qquad P_o = I_o A$$
($A$ = área transversal del haz).

**Optimización de la salida (p. 578–579).** Subir $\mathcal{T}$ aumenta la fracción extraída pero
también $\alpha_r$ (baja $\phi$). Extremos: $\mathcal{T}=0$ ⇒ $\phi$ máximo, $\phi_o=0$;
$\mathcal{T}=1$ ⇒ $\alpha_r > \gamma_0$, no oscila. Con $\mathcal{T} = 1-\mathcal{R}_1$:
$\alpha_{m1} = \frac{1}{2d}\ln\frac{1}{\mathcal{R}_1} = -\frac{1}{2d}\ln(1-\mathcal{T})$ (15.2-5);
$\alpha_r = \alpha_s + \alpha_{m2} - \frac{1}{2d}\ln(1-\mathcal{T})$ (15.2-6);
$\alpha_{m2} = \frac{1}{2d}\ln\frac{1}{\mathcal{R}_2}$ (15.2-7). Combinando (15.2-1), (15.2-3) y (15.2-6):
$$\phi_o = \tfrac12\phi_s\,\mathcal{T}\left[\frac{g_0}{L - \ln(1-\mathcal{T})} - 1\right],\qquad
  g_0 = 2\gamma_0(\nu)d,\quad L = 2(\alpha_s+\alpha_{m2})d \qquad (15.2\text{-}8)$$
Derivando respecto a $\mathcal{T}$ y con $\ln(1-\mathcal{T})\approx-\mathcal{T}$ ($\mathcal{T}\ll1$):
$$\mathcal{T}_{\rm op} \approx \sqrt{g_0 L} - L \qquad (15.2\text{-}9)$$
Fig. 15.2-3 (p. 579): $\phi_o/\phi_s$ vs. $\mathcal{T}$ para $g_0 = 0.5$, $L = 0.02$ (2 %):
máximo en $\mathcal{T}_{\rm op} = 0.08$.

**Densidad de número de fotones interna (p. 578–580).** **[recuadro]** $\mathfrak{n} = \phi/c$
(15.2-10) (argumento del cilindro de longitud $c$ y área $A$: contiene $cA\mathfrak{n}$ fotones, la
mitad cruza la base por segundo en cada sentido ⇒ $\phi = c\mathfrak{n}$). **[recuadro]**
$$\mathfrak{n} = \mathfrak{n}_s\left(\frac{N_0}{N_t}-1\right),\quad N_0 > N_t \qquad (15.2\text{-}11)$$
con $\mathfrak{n}_s = \phi_s(\nu)/c$. Usando $\phi_s = [\tau_s\sigma]^{-1}$, $\alpha_r = 1/c\tau_p$,
$\alpha_r = N_t\sigma$: **[recuadro]**
$$\mathfrak{n} = (N_0 - N_t)\,\frac{\tau_p}{\tau_s},\quad N_0 > N_t \qquad (15.2\text{-}12)$$
Interpretación: $(N_0-N_t)/\tau_s$ es la tasa de generación de fotones, igual en estado
estacionario a la tasa de pérdida $\mathfrak{n}/\tau_p$. En 4 niveles ideal ($\tau_s\approx t_{\rm sp}$,
$N_0 \approx R\,t_{\rm sp}$, $R$ en s⁻¹cm⁻³):
$$\frac{\mathfrak{n}}{\tau_p} = R - R_t,\quad R > R_t,\qquad R_t = N_t/t_{\rm sp} \qquad (15.2\text{-}13)$$

**Flujo de fotones de salida y eficiencia (p. 580–581).** Si la única pérdida es el espejo de
salida, $\Phi_o = (R - R_t)V$ (15.2-14), $V$ = volumen del medio activo. En general
**[recuadro] Flujo de fotones de salida del láser**:
$$\Phi_o = \eta_e\,(R - R_t)\,V \qquad (15.2\text{-}15)$$
con $\eta_e$ = **eficiencia de extracción** = (pérdida por luz útil extraída)/(pérdidas totales $\alpha_r$).
Si la luz sale solo por el espejo 1:
$\eta_e = \alpha_{m1}/\alpha_r = \frac{c}{2d}\tau_p\ln\frac{1}{\mathcal{R}_1}$ (15.2-16), y si
$\mathcal{T} = 1-\mathcal{R}_1 \ll 1$ **[recuadro]**:
$$\eta_e \approx \frac{\tau_p}{T_F}\,\mathcal{T},\qquad \frac{1}{T_F} = \frac{c}{2d} \qquad (15.2\text{-}17)$$
(razón entre el tiempo de vida del fotón y el tiempo de ida y vuelta, por la transmitancia).
Potencia de salida: $P_o = h\nu\,\Phi_o = \eta_e\,h\nu\,(R-R_t)V$ (15.2-18) (coincide con 15.2-4).
**[recuadro] Eficiencia de conversión de potencia** (*overall / wall-plug efficiency*):
$$\eta_c = \frac{P_o}{P_p} \qquad (15.2\text{-}19)$$
($P_p$ = potencia de bombeo suministrada; valores en Tabla 15.3-1). **[recuadro] Eficiencia de pendiente**
(*differential power-conversion / slope efficiency*, p. 581):
$$\eta_s = \frac{dP_o}{dP_p} \qquad (15.2\text{-}20)$$
En general $\eta_s > \eta_c$.

#### 15.2B Spectral Distribution (p. 581)

- La distribución espectral la fijan la forma de línea atómica (homogénea/inhomogénea) y los modos
  del resonador: (1) condición de ganancia $\gamma_0(\nu) > \alpha_r$ ⇒ banda de ancho $B$ centrada en
  $\nu_0$ (Fig. 15.2-4a); $B$ crece con $\Delta\nu$ y con $\gamma_0(\nu_0)/\alpha_r$. (2) condición de
  fase ⇒ solo los modos $\nu_q$ (FWHM $\delta\nu\approx\nu_F/\mathcal{F}$, Fig. 15.2-4b).
- **[recuadro] Número de modos posibles** (p. 582):
  $$M \approx \frac{B}{\nu_F} \qquad (15.2\text{-}21)$$
  En medio inhomogéneo oscilan los $M$ (con distintas potencias); en homogéneo compiten.
- El ancho de línea real de cada modo láser es mucho menor que $\delta\nu$: lo limita el ancho
  **Schawlow–Townes** (∝ 1/potencia); en la práctica dominan fluctuaciones acústicas y térmicas
  (p. 582).

**Ejercicio 15.2-1 — Número de modos en un láser de gas (p. 582).** Perfil Doppler gaussiano
$\gamma_0(\nu) = \gamma_0(\nu_0)\exp[-(\nu-\nu_0)^2/2\sigma_D^2]$, $\Delta\nu_D = (8\ln2)^{1/2}\sigma_D$.
(a) Deducir $B$ en función de $\Delta\nu_D$ y de $\gamma_0(\nu_0)/\alpha_r$. (b) He–Ne:
$\Delta\nu_D = 1.5$ GHz, $\gamma_0(\nu_0) = 2\times10^{-3}$ cm⁻¹, $d = 100$ cm, reflectancias 100 % y
97 %, $n=1$: hallar $M$. (Guía: $B = \Delta\nu_D\sqrt{\ln[\gamma_0(\nu_0)/\alpha_r]/\ln 2}$;
$\alpha_r = \frac{1}{2d}\ln\frac{1}{0.97}$; $\nu_F = c/2d = 150$ MHz.)

**Medio ensanchado homogéneamente (p. 582–583).** Tras el encendido, todos los modos con ganancia
> pérdida crecen; los más cercanos a $\nu_0$ más rápido. La ganancia saturada es
$$\gamma(\nu) = \frac{\gamma_0(\nu)}{1+\sum_{j=1}^M \phi_j/\phi_s(\nu_j)} \qquad (15.2\text{-}22)$$
(se reduce uniformemente); los modos alejados quedan con pérdida > ganancia y se extinguen; sobrevive
un solo modo (o dos simétricos) (Fig. 15.2-5, p. 583). En la práctica oscilan varios modos por
**spatial hole burning**: los distintos modos ocupan distintas regiones espaciales del medio; en los
nulos de la onda estacionaria del modo central la ganancia no se satura y otro modo puede oscilar.

**Medio ensanchado inhomogéneamente (p. 583–585).** La ganancia $\bar\gamma_0(\nu)$ es la envolvente
de las líneas de distintas especies de átomos (Fig. 15.2-6). Si la separación entre modos supera
$\Delta\nu$ de las líneas constituyentes, cada modo interactúa con átomos distintos; los que coinciden
con modos se saturan y abren **agujeros espectrales** (*spectral hole burning*, Fig. 15.2-7a, p. 584)
de ancho $\Delta\nu_s = \Delta\nu(1+\phi/\phi_s)^{1/2}$ [(14.4-16)]. Los modos no compiten; los
centrales abren agujeros más profundos y llevan más potencia (espectro de gas multimodo,
Fig. 15.2-7b).

**\*Spectral hole burning en medio Doppler (p. 584–585).** Un átomo con velocidad $v$ hacia la
radiación interactúa a $\nu_0(1+v/c)$; alejándose, a $\nu_0(1-v/c)$. Como el modo $\nu_q$ viaja en
ambos sentidos, interactúa con las clases $\pm v$ tales que $\nu_q-\nu_0 = \pm\nu_0 v/c$ y abre **dos
agujeros** simétricos (Fig. 15.2-8, p. 585); si $\nu_q=\nu_0$, uno solo. La potencia de un modo vs.
$\nu_q$ es una campana con una depresión central: el **Lamb dip** (Fig. 15.2-9), porque en
$\nu_q\to\nu_0$ los dos agujeros colapsan en uno y hay menos átomos disponibles.

#### 15.2C Spatial Distribution and Polarization (p. 586)

**Distribución espacial (p. 586–587).** Con espejos esféricos (§10.2) el resonador soporta un haz
gaussiano (cap. 3) y la jerarquía de modos TEM$_{l,m,q}$: $(l,m)$ = modo transversal
(distribución espacial; $(0,0)$ = gaussiano; $l,m$ mayores = Hermite–Gauss, §3.3); $q$ = modo
longitudinal (frecuencias separadas $\nu_F = c/2d$). Las frecuencias de conjuntos longitudinales de
distintos modos transversales están desplazadas una fracción de $\nu_F$ [(10.2-34)]. Fig. 15.2-10:
salida gaussiana del modo $(0,0)$. Los modos transversales tienen ganancias y pérdidas distintas
(Fig. 15.2-11, p. 587): $(0,0)$ es el más confinado (menor pérdida por difracción); $(1,1)$ se anula
en el eje (insensible a una obstrucción central); los de orden alto ocupan más volumen (más ganancia).
Modos que no se solapan espacialmente coexisten sin competir; con solape parcial (y migración
atómica en gases) compiten. Se suele diseñar para $(0,0)$ (menor diámetro, enfoque mínimo, cap. 3);
los de orden alto dan más potencia.

**Polarización (p. 587).** Cada modo $(l,m,q)$ tiene dos polarizaciones ortogonales independientes
(mismas distribuciones espaciales por simetría circular). Con ganancias/pérdidas iguales oscilan ambas
con la misma intensidad ⇒ salida **no polarizada** (§11.4).

**Resonadores inestables (p. 587).** Ventajas en alta potencia: (1) mayor volumen modal; (2) mayor
potencia en el modo transversal de orden más bajo; (3) óptica puramente reflectiva (la luz sale por
los bordes de los espejos; se pueden refrigerar con agua).

#### 15.2D Mode Selection (p. 587)

Se inserta un elemento que introduzca pérdida suficiente en los modos no deseados.
- **Selección de línea (p. 588):** prisma intracavidad (Fig. 15.2-12); solo la $\lambda$ deseada incide
  normalmente al espejo de alta reflectancia. Ej.: Ar⁺ con 6 líneas de 488 nm a 514.5 nm. No sirve para
  separar modos longitudinales adyacentes.
- **Modo transversal (p. 588):** apertura intracavidad de forma y tamaño elegidos; o diseño de espejos.
- **Polarización (p. 588):** polarizador **dentro** del resonador (uno externo desperdicia la mitad de
  la potencia y sufre ruido por *mode hopping*). Se implementa con **ventanas de Brewster** (§6.2,
  Ej. 6.2-1): la onda TM (polarizada en el plano de incidencia) pasa sin pérdida; la TE sufre reflexión
  y no oscila (Fig. 15.2-13, p. 589).
- **Modo longitudinal (p. 588–590):** (1) subir pérdidas hasta que solo oscile el modo de mayor
  ganancia (débil); (2) acortar $d$ para que $\nu_F > B$: p. ej. Ar⁺ con $\Delta\nu_D = 3.5$ GHz,
  $M = \Delta\nu_D/(c/2d)$ ⇒ $d < 4.3$ cm (reduce el volumen activo). Técnicas con elementos selectivos:
  - **Etalón inclinado intracavidad** (Fig. 15.2-14, p. 589–590): Fabry–Perot de espesor $d_1 \ll d$ con
    separación de modos $c/2d_1 > B$; solo un modo del etalón cae en la banda de ganancia y debe
    coincidir con un modo del resonador. Se sintoniza por rotación, temperatura o piezoeléctrico; se
    inclina para no crear resonancias adicionales; estabilizado térmicamente.
  - **Resonadores de múltiples espejos** (Fig. 15.2-15, p. 590): (a) dos resonadores acoplados (uno
    pasivo, uno activo); (b) dos cavidades activas acopladas (láser semiconductor C³, cap. 17);
    (c) resonador acoplado a un interferómetro.

### 15.3 Common Lasers (p. 590)

Láseres en sólidos (cristales, vidrios, fibras, polvos), gases (atómicos, iónicos, moleculares,
excímeros), líquidos (colorantes), plasmas (EUV, rayos X) y electrones libres. Rango: tamaños de nm a
estadios; frecuencias de 1 GHz (máser) a 100 PHz (rayos X), > 18 órdenes; anchos de línea de Hz a
THz; pulsos de fs a CW; potencias pico de pW a PW (27 órdenes) (p. 590).

#### 15.3A Solid-State Lasers (p. 591)

**Generalidades (p. 591–592).** Niveles de energía en §13.1C (Figs. 13.1-8, 13.1-9); amplificadores
en §14.3 (Figs. 14.3-1, 14.3-3, 14.3-6); transiciones en Tabla 14.3-1. Huéspedes cristalinos:
óxidos, granates, fluoruros, vanadatos (Al₂O₃ zafiro, Y₃Al₅O₁₂ YAG, Gd₃Ga₅O₁₂ GGG, YLiF₄ YLF, YVO₄);
vidrios: silicatos (SiO₂ fundido), fosfatos (alta potencia y pulsados, §14.3B). Cristal vs. vidrio:
el cristal tiene líneas más estrechas (umbral menor), menor dopaje, más resistencia a solarización,
mejor conductividad térmica; el vidrio es isótropo, fácil de fabricar con dopaje homogéneo y gran
tamaño, pero mal conductor térmico (alta potencia y bajo ciclo de trabajo). Cristales ⇒
ensanchamiento homogéneo; vidrios ⇒ inhomogéneo (§13.3D). Dopantes: metales de transición y
lantánidos (tierras raras), ~1 % (0.01–50 %). Más comunes: Nd³⁺:YVO₄, Nd³⁺:YAG, Yb³⁺:YAG,
Ti³⁺:zafiro, Er³⁺:fibra de sílice, Yb³⁺:fibra de sílice; también Er:YAG, Ho:YAG, Tm:YAG, fibra de Tm.
Los niveles de las tierras raras son casi independientes del huésped (los 4f están apantallados por
5s y 5p). El rubí (primer láser, 1960) se usa poco hoy. **DPSS** (*diode-pumped solid-state*):
bombeo con diodos; compactos y eficientes; con doblado/triplicado/cuadruplicado de frecuencia
(cap. 21) cubren visible y UV.

**Nd³⁺:YVO₄ (p. 592).** $n\approx2.0$, transparente 0.3–2.5 μm. Bombeo con diodo a $\lambda_o = 808$ nm
puebla ⁴F₅/₂ (1.53 eV); transición principal ⁴F₃/₂ → ⁴I₁₁/₂ a **1.064 μm**; también ⁴F₃/₂ → ⁴I₁₃/₂
(1.34 μm) y ⁴F₃/₂ → ⁴I₉/₂ (914 nm, cuasi-3-niveles). Frente a Nd:vidrio: mayor $n$, ensanchamiento
homogéneo, línea más estrecha (Tabla 14.3-1). Sistema de 4 niveles ⇒ umbral mucho menor que el
rubí. Doblado a 532 nm (bombeo típico del Ti:zafiro); doblado intracavidad de 914 nm ⇒ 457 nm azul.
Fig. 15.3-1 (p. 592): (a) niveles (0: ⁴I₉/₂, 1: ⁴I₁₁/₂, 2: ⁴F₃/₂, 3: ⁴F₅/₂; $\tau_{32}$, $\tau_1$);
(b) cavidad con cristal LBO intracavidad para 532 nm (§21.2A).

**Nd³⁺:YAG (p. 592–593).** Desde los 1960. Niveles como Nd:vidrio y Nd:YVO₄. Bombeo por flashlamp o
diodo a 808 nm; cristales de cientos de μm = láseres de disco delgado monofrecuencia. Línea principal
$\lambda_o = 1.06415$ μm: entre el nivel superior del **manifold** ⁴F₃/₂ (1.4269 eV) y el tercero
desde abajo de ⁴I₁₁/₂ (0.2616 eV); doblada da **532 nm**. Fig. 15.3-2 (p. 593): estructura fina de
los manifolds ⁴I₉/₂, ⁴I₁₁/₂, ⁴F₃/₂, con $(2\mathcal{J}+1)/2 = 5, 6, 2$ niveles. El número de niveles
es $g/2$, $g = 2\mathcal{J}+1$ = parámetro de degeneración ($\mathcal{J}$ del símbolo de término
$^{2S+1}\mathcal{L}_\mathcal{J}$, §13.1A). Líneas posibles 1.052–1.122 μm; p. ej. 1.12238 μm
(1.4165 eV → 0.3117 eV) ⇒ doblada 561 nm; cuasi-3-niveles ⁴F₃/₂ → ⁴I₉/₂ a 946 nm ⇒ doblada 473 nm.
Desventajas vs. Nd:YVO₄: banda de absorción ⁴F₅/₂ más estrecha (sensible a la $\lambda$ del diodo),
mayor umbral, menor eficiencia de pendiente, salida no polarizada. Es el "caballo de batalla" DPSS.

**Yb³⁺:YAG (p. 593–594).** Disco delgado bombeado por diodo a **940 nm** (el bombeo pasa ~25 veces por
el medio con espejo parabólico y retrorreflector; dopaje ≈ 25 %) (Fig. 15.3-3). Transición
²F₅/₂ → ²F₇/₂ a **1.030 μm**; cuasi-3-niveles. Como $\lambda_{\rm bombeo}$ (940) ≈ $\lambda_{\rm láser}$
(1030), la carga térmica por fotón es pequeña (defecto cuántico bajo); el disco se refrigera por
*heat sink* y mantiene TEM₀₀. Cientos de W CW; doblado a 515 nm reemplaza al Ar⁺.

**Ti³⁺:zafiro (p. 594–595).** Sintonizable en un amplio rango; se puede hacer mode locking para
pulsos ultracortos (§15.4D). ~1 % de Al reemplazado por Ti; $n\approx1.76$. Bombeo con Nd:YVO₄ o
Nd:YAG doblado (532 nm), Ar⁺, Yb:YAG doblado (515 nm) o diodo verde. El Ti³⁺ (un electrón 3d¹) en
sitio octaédrico con 6 oxígenos ⇒ fuerte campo cristalino; niveles designados por teoría de grupos
(²T₂ fundamental, ²E excitado) fuertemente acoplados a vibraciones de red ⇒ bandas **vibrónicas**
anchas; la emisión estimulada va acompañada de fonones; la parte alta de ²T₂ está vacía (Boltzmann)
⇒ se comporta como 4 niveles (Fig. 15.3-4a, p. 595). Sintonía de decenas de nm con **filtro
birrefringente (BRF)** rotatorio en ángulo de Brewster (pasabanda para el haz polarizado); rangos
mayores ajustando la óptica interna, pues la **dispersión de velocidad de grupo de la cavidad cambia
con $\lambda$**. Rango total **700–1050 nm**. CW ≈ 5 W; mode-locked: pulsos de **10 fs, 50 nJ, ≈ 80 MHz,
pico ≈ 1 MW**. Fig. 15.3-4b: cavidad con par de prismas (compensación de dispersión intracavidad)
y BRF. Por el papel de los fonones se llama **láser vibrónico** (*phonon-terminated*); también la
alejandrita y los colorantes (vibraciones moleculares).

**Láseres de fibra (p. 595–596).** Fibras dopadas con tierras raras con realimentación por **redes
de Bragg en fibra (FBG)**; bombeo por diodos acoplados a la fibra (Fig. 15.3-5a). Configuraciones
**double-clad** (núcleo interno monomodo dopado + núcleo externo multimodo para el bombeo; el núcleo
interno puede ir descentrado o el externo ser rectangular, octogonal o en D para mejorar el solape
con los rayos oblicuos, Fig. 15.3-5b) para evitar los efectos no lineales de concentrar bombeo alto
en un núcleo pequeño.
- **Yb:sílice**: > 1 kW CW en 1070–1080 nm, FWHM ≈ 1 THz, núcleo de pocos μm, $M^2 < 1.1$,
  $\eta_c > 25$ %; polarización lineal y menor ancho de línea a menor potencia; multimodo hasta 50 kW
  (soldadura, corte).
- **Er:sílice**: cientos de W CW en 1550–1570 nm, FWHM < 400 GHz, $M^2 < 1.1$, $\eta_c > 10$ %;
  polarización aleatoria, lineal o circular; 1530–1620 nm a decenas de W.
- **Tm:fibra**: 150 W en 1.8–2.1 μm, FWHM ≈ 75 GHz, $\eta_c\approx5$ %, $M^2 < 1.05$; a 1.94 μm
  coincide con la absorción del agua (medicina).
- Aplicaciones: procesado de materiales, cirugía, semilla de los amplificadores de vidrio del
  National Ignition Facility (§14.3B); operan también Q-switched y mode-locked (§15.4). **Láseres de
  fibra de bandgap fotónico**: emisión radial por la superficie (nota al pie: Shapira *et al.*,
  *Opt. Express* 14, 3929, 2006). Comparación con diodos: §17.3C.

**Láseres Raman de fibra, RFL (p. 597–598).** Basados en **dispersión Raman estimulada (SRS)**
(§13.5C, §14.3D, Fig. 14.3-7): un fotón de señal $h\nu_s$ estimula la emisión de un clon obtenido
desplazando Stokes al fotón de bombeo por la energía vibracional $h\nu_R$. La ganancia la gobierna el
coeficiente Raman $\gamma_R$ [(21.3-15)]; el ancho de banda lo fija el espectro vibracional del
vidrio. Realimentación con FBG a la frecuencia deseada; $\nu = \nu_p - \nu_R$, con $\nu_R$ cualquiera
dentro del espectro vibracional. Como el Stokes está ligado al bombeo, la oscilación Stokes puede a su
vez bombear un segundo orden ($\nu_{p1} = \nu_p - \nu_R$ → $\nu_{p2}$) con otro par de FBG, etc.:
**láseres Raman de fibra en cascada** (Fig. 15.3-6a). Fig. 15.3-6b: bombeo Yb:sílice double-clad
(FBG 1064 nm, 100 % y 20 %) → fibra de fosfosilicato con FBG1 (1239 nm, 100 %/100 %) y FBG2
(1484 nm, 100 %/50 %). Fuentes monomodo de alta potencia; útiles para bombear amplificadores Raman
en DWDM y para bombeo remoto de EDFA; con señal inyectada el RFL actúa como RFA.

**Ejemplo 15.3-1 — Láser Raman de fibra de fosfosilicato (p. 598).** Bombeo Yb double-clad
(1050–1120 nm) a 1064 nm sobre 1 km de fibra de fosfosilicato; se quiere 1484 nm (bombeo de un
amplificador Raman). Corrimiento necesario ≈ 80 THz; el fosfosilicato tiene $\nu_R\approx40$ THz ⇒
**dos** órdenes Stokes (con sílice-germanio, $\nu_R\approx13$ THz, harían falta **seis**). FBG1 a
1239 nm (−40 THz), FBG2 a 1484 nm (−40 THz más); FBG1 100 %/100 %; FBG2 100 %/50 % para acoplar la
salida. Decenas de W CW, ancho de pocos nm, cualquier $\lambda$ en 1200–1700 nm. $\eta_c$ del
bombeo Yb ≈ 25 %; eficiencia de pendiente del convertidor Raman ≈ 0.25 W/W.

Notas (p. 598): la fibra favorece el Raman por longitud, confinamiento monomodo, bombeo DPSS y FBG;
también hay **láseres Brillouin de fibra** (SBS). El láser Raman **no requiere inversión de
población** (ganancia Raman, no emisión estimulada entre niveles poblados). **Lasing without inversion
(LWI)**: con un campo auxiliar se crea una segunda vía del nivel inferior al superior y la
interferencia cuántica destructiva elimina la absorción.

**Láseres aleatorios (p. 598–600).** Realimentación por dispersión múltiple en un medio de ganancia
desordenado (caminata aleatoria 3D, Fig. 15.3-7a); también *powder lasers* o *plasers*. Realimentación
incoherente, basada en intensidad (no en campo) ⇒ la frecuencia la fija el perfil de ganancia; más
dispersión ⇒ más realimentación ⇒ menor umbral. Relevante en máseres astronómicos (H₂O, OH, SiO) y para
rayos X (sin reflexión especular). Sin direccionalidad ni coherencia espacial (emisión como LED,
Fig. 17.1-12a). Bombeo óptico, eléctrico o por haz de electrones; volúmenes de 1 μm³ a cm³. Medios: polvos
de rubí, Nd:YAG, Nd:vidrio, Ti:zafiro, GaAs; rodamina 6G + micropartículas de Al₂O₃ en metanol;
polímeros, líquidos, cristales líquidos dopados, nanoestructuras semiconductoras, tejidos
biológicos. Si los dispersores soportan modos de resonador ⇒ colección de microláseres; con dispersión
**recurrente** (lazos que se recorren repetidamente) y ganancia > pérdidas en el lazo ⇒ **láseres
aleatorios coherentes** con emisión en frecuencias de cavidad fortuitas. **Microláseres aleatorios**:
clústeres de dispersores que confinan la luz a ~λ³.

**Ejemplo 15.3-2 — Microláser aleatorio de ZnO (p. 600).** Varios miles de nanocristalitos de ZnO
(decenas de nm) forman un microclúster ≈ 1 μm; son a la vez medio de ganancia y dispersores;
$\lambda_o\approx380$ nm (cerca del bandgap del ZnO); no necesitan forma regular ni superficies lisas.

#### 15.3B Gas Lasers (p. 600)

- **Atómicos e iónicos (p. 600):** He–Ne, Ar⁺, Kr⁺ (Tabla 15.3-1). Kr⁺: cientos de mW de 350 nm a 676 nm;
  operado simultáneamente en varias líneas da "luz láser blanca". Hoy relegados a aplicaciones
  especializadas frente a DPSS y diodos.
- **Moleculares (p. 600):** CO₂ (Fig. 13.1-4) a 9.6 y 10.6 μm; miles de W CW con alta eficiencia
  (corte, soldadura, marcado). Metanol en el IR lejano (119 y 124 μm); incluso vapor de agua.
- **Excímeros (p. 600–601):** en UV. *Excimer* = "excited dimer" (dos átomos ligados solo en estado
  excitado); *exciplex* si son distintos (haluros de gases nobles, p. ej. XeCl: el gas noble excitado
  se comporta como un alcalino y reacciona con el halógeno, Fig. 13.1-3). El nivel inferior se
  disocia ⇒ inversión incorporada. Líneas: **F₂ 153 nm, ArF 193 nm, KrF 248 nm, XeCl 308 nm, XeF
  351 nm**. Bombeo por descarga eléctrica en mezcla Xe/Cl₂. La luz de $\lambda$ corta no penetra y corta
  sin calor: microlitografía, micromecanizado, fotoquímica, cirugía refractiva; litografía a 193 nm.
- **Químicos (p. 601):** bombeo por la energía de una reacción (quimioluminiscencia, §13.5A). HF:
  2.7–3.1 μm; descarga en H₂ + F₂ produce HF* vibracionalmente excitado; reacción en cadena. Alta
  potencia; interés militar.

**Ejemplo 15.3-3 — Láser químico de DF en White Sands (p. 601).** MIRACL (Mid-Infrared Advanced
Chemical Laser, U.S. Army): quema etileno C₂H₄ con NF₃; el F libre reacciona con deuterio ⇒ DF*;
lasea en varias líneas en 3.5–4.0 μm (menos absorbidas por la atmósfera que las del HF); MW de CW
durante ≈ 1 min, haz de ≈ 4 cm de diámetro.

#### 15.3C Other Lasers (p. 601)

**Colorantes (p. 601–602).** Sintonizables; solución de colorante orgánico en alcohol o agua
(≈ 10⁻⁴ M), o en polímero/vidrio/cristal (**láser de colorante de estado sólido**); 4 niveles
(Fig. 13.1-5). Polimetinas: 0.7–1.5 μm; xantenos: 500–700 nm; cumarinas: 400–500 nm; escintiladores:
< 400 nm. Rodamina 6G: 560–640 nm. Alto mantenimiento (vida química corta) ⇒ reemplazados por DPSS;
Ti:zafiro es más sintonizable en torno a 800 nm; doblado da ~400 nm; cerca de 600 nm se dobla un OPO
de 1–2 μm (§21.2C, §21.4C).

**EUV y rayos X (p. 602–604).** Difícil por (15.1-16): a $t_{\rm sp}$ fijo, $N_t\propto1/\tau_p\lambda^2 g(\nu)$;
con Doppler, $g(\nu)\propto\lambda$ [(13.3-42)] ⇒ potencia umbral de bombeo $\propto 1/\tau_p\lambda^4$.
Además, óptica difícil: absorción grande (reduce $\tau_p$, sube $N_t$) e índice ≈ 1. Dos enfoques:
**óptica de incidencia rasante** (sobre la frecuencia de plasma el índice de los metales es < 1,
Fig. 5.5-10, §5.5D ⇒ reflexión total interna a incidencia rasante) y **óptica multicapa** (p. ej. Si/Mo,
> 70 % en EUV; también placas zonales). Primer láser de rayos X: LLNL 1980 con detonación nuclear
subterránea. Hoy: recombinación en plasma caliente ionizado por un láser de bombeo enfocado en un
blanco sólido con pulsos cortos; **ASE** (§14.5) sin resonador; coherencia espacial por propagación
(§11.3C). Ejemplo (p. 603): CO₂ 10.6 μm, 50 ns, 300 J sobre disco de carbono ⇒ plasma de C⁵⁺
(hidrogenoide) confinado magnéticamente; al enfriarse, electrones capturados en n = 3 y vacío de
n = 2 (decaimiento radiativo rápido) ⇒ inversión; transición 3d → 2p con energía
$$E = \frac{M_r Z^2 e^4}{(4\pi\epsilon_o)^2\,2\hbar^2}\left(\frac{1}{2^2}-\frac{1}{3^2}\right) \qquad (15.3\text{-}1)$$
con $Z=6$: 68 eV, $\lambda_o = 18.2$ nm; $t_{\rm sp}\approx12$ ps; $\gamma d\approx6$ ⇒ $G\approx e^6$
[(14.1-7)]; salida: 20 ns, 100 kW, 2 mJ, 5 mrad. Medios actuales: iones tipo Ne, Ni, Pd; bombeo con
Ti:zafiro o armónicos de Nd:vidrio; pulsos secuenciales de bombeo e incidencia rasante del bombeo
principal mejoran la eficiencia. **Láser de rayos X de descarga capilar** (bombeo eléctrico; "tabletop
X-ray lasers"). **Láseres de ionización por campo óptico** (ionización multifotónica/de campo;
electrones fríos). **Láseres fotobombeados de capa interna** (vacantes de vida muy corta; óptica
ultrarrápida, cap. 22). **Generación de armónicos de orden alto (HHG)** (p. 604): interacción no lineal
extrema de pulsos de fs intensos con un gas; el campo ioniza la molécula, acelera el electrón y, al
invertirse, lo devuelve al ion emitiendo armónicos altos; pulsos ultracortos en 5–30 nm. También FEL.
Aplicaciones: nanolitografía, nanoimagen, diagnóstico de plasmas, imagen y holografía dinámica.

**Ejemplo 15.3-4 — Láser EUV de Ag¹⁹⁺ tipo Ni (p. 603).** Transición 4d ¹S₀ → 4p ¹P₁. Prepulso de
1.5 J (4 ps) y, 1.2 ns después, pulso principal de 10.5 J ⇒ ASE de 25 μJ a $\lambda_o = 13.9$ nm;
$\gamma = 35$ cm⁻¹, $\gamma d\approx13.6$; divergencia 6 mrad.

**Láser de electrones libres, FEL (p. 604–605).** Medio activo: haz de electrones relativista en el
campo **wiggler** periódico de un **ondulador** (imanes de polaridad alternante, Fig. 15.3-8):
periodo $\Lambda$ de pocos cm, ~100 periodos, pocos m; espejos separados ≈ 2× la longitud; campo pico
de pocos kG; corriente de A a kA; energía de MeV a GeV (típico 50 MeV); radio del haz ≈ 1 mm, cintura
óptica ≈ 3 mm; pulsos de ps a μs. Sintonizable por energía del haz, campo e $\Lambda$: desde ondas mm
hasta EUV; en vacío ⇒ potencias pico altas sin daño ni lente térmica. LCLS (SLAC, 1 km): paquetes de
10¹⁰ electrones ⇒ 10¹² fotones en pulsos de 100 fs a 1.5 Å.

#### 15.3D Tabulation of Selected Characteristics (p. 605)

Tabla 15.3-1 (p. 606; transcrita más abajo) en orden de $\lambda$ creciente. Sección eficaz,
$t_{\rm sp}$ y $\Delta\nu$ atómico: Tabla 14.3-1. El ancho de línea del láser es muchos órdenes menor
que el atómico por la selectividad del resonador. Algunos sistemas no sostienen inversión continua
⇒ solo pulsados.

### 15.4 Pulsed Lasers (p. 605)

Pulsar permite potencias pico enormes: duraciones hasta fs (attosegundos con técnicas no lineales);
repetición de horas⁻¹ (EUV) a > 100 GHz; energías de fJ a MJ (> 20 órdenes); potencias pico > 10 MW;
intensidades pico 10 TW/cm². Algunos láseres solo pulsados (Tabla 15.3-1).

#### 15.4A Methods of Pulsing Lasers (p. 605)

- **Modulador externo** sobre un láser CW (Fig. 15.4-1a): ineficiente (bloquea energía) y la potencia
  pico no supera la CW. **Modulación interna** (Fig. 15.4-1b): se almacena energía en el *off-time*
  (fotones en el resonador o inversión en los átomos) y se libera en el *on-time* ⇒ potencia pico ≫ CW.
  Cuatro métodos: conmutación de ganancia, Q-switching, *cavity dumping*, mode locking (p. 606).
- **Gain switching (p. 606–607, Fig. 15.4-2):** se enciende y apaga el bombeo (flashlamp en rubí;
  corriente en diodos, cap. 17). Tiempos de subida/bajada en §15.4B.
- **Q-switching (p. 607, Fig. 15.4-3):** se apaga la salida aumentando periódicamente la pérdida
  (arruinando el $Q$) con un absorbedor modulado intracavidad = *loss switching*. El bombeo es
  constante; la inversión se acumula en el *off-time* (alta pérdida) y se libera en pulsos intensos y
  cortos. Análisis en §15.4C.
- **Cavity dumping (p. 608, Fig. 15.4-4):** se almacenan **fotones** (no inversión) en el resonador y
  se liberan modulando la **transmitancia del espejo** (analogía del balde). En el *off-time* no se
  permite fuga (ni útil) ⇒ pérdidas despreciables, la potencia interna crece; luego se "quita" el
  espejo (transmitancia 100 %) y salen todos los fotones; el salto de pérdida detiene la oscilación.
  No se analiza (similar al Q-switching).
- **Mode locking (p. 608):** proceso dinámico de **estado estacionario** (no transitorio): se acoplan
  los modos longitudinales (separados $c/2d$) fijando sus fases ⇒ componentes de Fourier de una
  función periódica ⇒ tren de pulsos. Técnica principal para pulsos ultracortos. Se logra modulando
  periódicamente las pérdidas. §15.4D.

#### \*15.4B Analysis of Transient Effects (p. 608)

Variables: $\mathfrak{n}(t)$ (fotones por unidad de volumen) y $N(t) = N_2(t) - N_1(t)$.

**Ecuación de tasa del número de fotones (p. 609).**
$$\frac{d\mathfrak{n}}{dt} = -\frac{\mathfrak{n}}{\tau_p} + N W_i \qquad (15.4\text{-}1)$$
(pérdida por fuga del resonador + ganancia neta por emisión estimulada − absorción;
$W_i = \phi\sigma(\nu) = c\mathfrak{n}\sigma(\nu)$ = densidad de probabilidad de transición inducida;
se desprecia la espontánea). Con $N_t = \alpha_r/\sigma = 1/c\tau_p\sigma$ ⇒ $\sigma = 1/c\tau_pN_t$:
$$W_i = \frac{\mathfrak{n}}{N_t\,\tau_p} \qquad (15.4\text{-}2)$$
**[recuadro] Ecuación de tasa de fotones:**
$$\frac{d\mathfrak{n}}{dt} = -\frac{\mathfrak{n}}{\tau_p} + \frac{N}{N_t}\frac{\mathfrak{n}}{\tau_p} \qquad (15.4\text{-}3)$$
Si $N > N_t$, $\mathfrak{n}$ crece; en estado estacionario $N = N_t$.

**Ecuación de tasa de la diferencia de población (p. 609–610).** Esquema de **3 niveles** (§14.2B),
con $\tau_2 = t_{\rm sp}$ y $R$ independiente de $N$ [(14.2-8)]:
$$\frac{dN_2}{dt} = R - \frac{N_2}{t_{\rm sp}} - W_i(N_2 - N_1) \qquad (15.4\text{-}4)$$
Con $N_a = N_2 + N_1$, $N_1 = (N_a-N)/2$, $N_2 = (N_a+N)/2$:
$$\frac{dN}{dt} = \frac{N_0}{t_{\rm sp}} - \frac{N}{t_{\rm sp}} - 2W_iN \qquad (15.4\text{-}5)$$
con $N_0 = 2Rt_{\rm sp} - N_a$ [(14.2-27)]. Sustituyendo (15.4-2), **[recuadro] Ecuación de tasa de la
diferencia de población (3 niveles)**:
$$\frac{dN}{dt} = \frac{N_0}{t_{\rm sp}} - \frac{N}{t_{\rm sp}} - 2\frac{N}{N_t}\frac{\mathfrak{n}}{\tau_p} \qquad (15.4\text{-}6)$$
El factor 2: cada fotón generado baja $N_2$ en 1 y sube $N_1$ en 1 ⇒ $N$ baja en 2. (15.4-3) y (15.4-6)
son ecuaciones no lineales acopladas. Estado estacionario ($dN/dt = d\mathfrak{n}/dt = 0$): $N = N_t$ y
$\mathfrak{n} = (N_0-N_t)(\tau_p/2t_{\rm sp})$, consistente con (15.2-12) con $\tau_s = 2t_{\rm sp}$ (14.2-28).

**Ejercicio 15.4-1 (p. 610).** Obtener la ecuación de tasa de $N$ para un sistema de **4 niveles**
con $\tau_1 \ll t_{\rm sp}$ y explicar por qué desaparece el factor 2 de (15.4-6). (Idea: el nivel
inferior se vacía inmediatamente, así que $N\approx N_2$ y cada fotón reduce $N$ solo en 1.)

**Gain switching (p. 610–611).** Se modula $R$, equivalente a modular $N_0 = 2Rt_{\rm sp} - N_a$.
Fig. 15.4-5: bombeo escalón de $N_{0a}$ (bajo umbral) a $N_{0b}$ (sobre umbral). Regímenes:
- $t<0$: $N = N_{0a} < N_t$, no oscila.
- $t = 0$: $N_0 \to N_{0b}$; mientras $N < N_t$, $\mathfrak{n} = 0$ y $dN/dt = (N_0-N)/t_{\rm sp}$ ⇒
  $N$ crece exponencialmente hacia $N_{0b}$ con constante $t_{\rm sp}$.
- $t = t_1$: $N$ cruza $N_t$, empieza la oscilación, $\mathfrak{n}$ crece; la inversión se agota, $N$
  decae hacia $N_t$ y $\mathfrak{n}$ llega a su valor estacionario $(N_{0b}-N_t)\tau_p/2t_{\rm sp}$.
- $t = t_2$: se apaga el bombeo ($N_0\to N_{0a}$); $N$ y $\mathfrak{n}$ decaen a $N_{0a}$ y 0.
El perfil exacto requiere resolver numéricamente (15.4-3) y (15.4-6); depende de $t_{\rm sp}$,
$\tau_p$, $N_t$, $N_{0a}$, $N_{0b}$ (Prob. 15.4-4).

#### \*15.4C Q-Switching (p. 611)

Se conmuta $\alpha_r$ de alto (*off*) a bajo (*on*), p. ej. con un modulador intracavidad. Como
$N_t\propto\alpha_r$ [(15.1-14), (15.1-6)], equivale a conmutar $N_t$ de $N_{ta}$ (alto) a $N_{tb}$
(bajo); $N_0$ fijo (en gain switching es al revés). Fig. 15.4-6 (p. 611):
- $t=0$: bombeo encendido, $N_t = N_{ta} > N_0$ ⇒ no oscila; $N(t)$ crece (constante $t_{\rm sp}$) hacia
  $N_0$ aunque el medio sea un amplificador de alta ganancia.
- $t = t_1$: la pérdida baja ⇒ $N_t = N_{tb} < N_0$; oscila; $\mathfrak{n}$ sube bruscamente; la
  saturación agota $N$; cuando $N < N_{tb}$ la pérdida vuelve a superar la ganancia y $\mathfrak{n}$
  cae rápidamente (tiempo ~ $\tau_p$).
- $t = t_2$: se restaura la pérdida alta y se repite periódicamente ⇒ tren de pulsos.

**Análisis del pulso (p. 612).** En el *on-time* $t_i$–$t_f$ se desprecian bombeo y emisión espontánea
(los dos primeros términos de 15.4-6), válido si el pulso es ≪ $t_{\rm sp}$. **[recuadro]**:
$$\frac{d\mathfrak{n}}{dt} = \left(\frac{N}{N_t}-1\right)\frac{\mathfrak{n}}{\tau_p} \qquad (15.4\text{-}7)$$
$$\frac{dN}{dt} = -2\frac{N}{N_t}\frac{\mathfrak{n}}{\tau_p} \qquad (15.4\text{-}8)$$
con $\mathfrak{n}=0$, $N = N_i$ en $t = t_i$ y $N_t = N_{tb}$ fijo. Dividiendo:
$$\frac{d\mathfrak{n}}{dN} \approx \frac12\left(\frac{N_t}{N}-1\right) \qquad (15.4\text{-}9)$$
⇒ $\mathfrak{n}\approx\frac12N_t\ln N - \frac12N + $ const. (15.4-10); con la condición inicial
**[recuadro]**:
$$\mathfrak{n} \approx \tfrac12 N_t\ln\frac{N}{N_i} - \tfrac12(N - N_i) \qquad (15.4\text{-}11)$$

**Ejemplo 15.4-1 — Microchip Nd:YAG Q-switched (p. 613).** Lámina de Nd:YAG + absorbedor saturable +
cristal doblador intracavidad, cavidad de 1 mm; bombeo 1 W a 808 nm por diodo acoplado a fibra;
pulsos Q-switched a 532 nm de **30 μJ, 250 ps, ≈ 10 kHz, 300 mW** medios.

**Potencia del pulso (p. 613).** $\phi = \mathfrak{n}c$ (ambos sentidos), $\phi_o = \frac12\mathcal{T}\mathfrak{n}c$:
$$P_o = h\nu\,A\,\phi_o = \tfrac12 h\nu\,c\,\mathcal{T}A\mathfrak{n} = h\nu\,\mathcal{T}\frac{c}{2d}V\mathfrak{n} \qquad (15.4\text{-}12)$$
($V = Ad$). Con $\eta_e\approx\mathcal{T}(c/2d)\tau_p$ (15.2-17):
$$P_o = \eta_e\,h\nu\,\frac{\mathfrak{n}V}{\tau_p} \qquad (15.4\text{-}13)$$
($\mathfrak{n}V/\tau_p$ = fotones perdidos por el resonador por unidad de tiempo).

**Potencia pico (p. 613).** $\mathfrak{n}$ es máximo cuando $N = N_t = N_{tb}$ ($d\mathfrak{n}/dt=0$ en 15.4-7):
$$\mathfrak{n}_p = \tfrac12 N_i\left(1 + \frac{N_t}{N_i}\ln\frac{N_t}{N_i} - \frac{N_t}{N_i}\right) \qquad (15.4\text{-}14)$$
$$P_p = h\nu\,\mathcal{T}\frac{c}{2d}V\mathfrak{n}_p \qquad (15.4\text{-}15)$$
Si $N_i\gg N_t$: $\mathfrak{n}_p\approx\frac12N_i$ (15.4-16) (la mitad de la inversión inicial), y
**[recuadro] Potencia pico del pulso**:
$$P \approx \tfrac12 h\nu\,\mathcal{T}\frac{c}{2d}\,V N_i \qquad (15.4\text{-}17)$$

**Energía del pulso (p. 614).** $E = \int_{t_i}^{t_f}P_o\,dt$ (15.4-18)
$= h\nu\mathcal{T}\frac{c}{2d}V\int_{N_i}^{N_f}\mathfrak{n}\frac{dt}{dN}dN$ (15.4-19); con (15.4-8):
$E = \frac12h\nu\mathcal{T}\frac{c}{2d}VN_t\tau_p\int_{N_f}^{N_i}\frac{dN}{N}$ (15.4-20)
$= \frac12h\nu\mathcal{T}\frac{c}{2d}VN_t\tau_p\ln\frac{N_i}{N_f}$ (15.4-21). $N_f$ se obtiene de
$\mathfrak{n}=0$ en (15.4-11):
$$\ln\frac{N_i}{N_f} = \frac{N_i - N_f}{N_t} \qquad (15.4\text{-}22)$$
**[recuadro] Energía del pulso Q-switched**:
$$E = \tfrac12 h\nu\,\mathcal{T}\frac{c}{2d}V\tau_p\,(N_i - N_f) \qquad (15.4\text{-}23)$$
Si $N_i\gg N_f$: $E\approx\frac12h\nu\mathcal{T}(c/2d)V\tau_pN_i$. Para resolver (15.4-22) se escribe
$Y e^{-Y} = X e^{-X}$ con $X = N_i/N_t$, $Y = N_f/N_t$ (numéricamente o con la gráfica de $Xe^{-X}$,
Fig. 15.4-7, p. 614: $X_1$ y $Y_1$ tienen la misma ordenada).

**Duración del pulso (p. 615).** Estimación $E/P_p$ con (15.4-14), (15.4-15), (15.4-23) **[recuadro]**:
$$\tau_{\rm pulse} = \tau_p\,\frac{N_i/N_t - N_f/N_t}{N_i/N_t - \ln(N_i/N_t) - 1} \qquad (15.4\text{-}24)$$
Si $N_i\gg N_t$ y $N_i\gg N_f$: $\tau_{\rm pulse}\approx\tau_p$.

**Forma del pulso (p. 615).** Integración numérica de (15.4-7)–(15.4-8). Fig. 15.4-8: $\mathfrak{n}(t)/N_t$
vs. $t/\tau_p$ para $N_i/N_t = 2, 4, 6, 8, 10$: el pulso se estrecha y crece con $N_i/N_t$; el pico tiende
a $\frac12N_i$ (para $N_i/N_t = 10$, pico ≈ $3.1N_t$ hacia $t\approx1.2\tau_p$; para 2, pico bajo y ancho).

**Ejercicio 15.4-2 — Láser de rubí pulsado (p. 615).** Con el rubí del Ej. 15.1-1, Q-switched con
$N_i = 6N_t$ al final del bombeo ($t = t_i$): usar la Fig. 15.4-8 para estimar forma, duración, potencia
pico y energía del pulso.

#### 15.4D Mode Locking (p. 615)

Modos longitudinales separados $\nu_F = c/2d$; normalmente independientes (*free-running*). Al fijar
sus fases se convierten en componentes de Fourier de una función periódica de periodo
$T_F = 1/\nu_F = 2d/c$ (cf. §2.6B, interferencia de $M$ ondas).

**Propiedades del tren de pulsos (p. 616–618).** Cada modo como onda plana en $z$ con velocidad $c = c_o/n$:
$$U(z,t) = \sum_q A_q\exp\left[j2\pi\nu_q\left(t - \frac{z}{c}\right)\right] \qquad (15.4\text{-}25)$$
$$\nu_q = \nu_0 + q\nu_F,\qquad q = 0,\pm1,\pm2,\dots \qquad (15.4\text{-}26)$$
($A_q$ = envolvente compleja; $|A_q|$ del perfil espectral de ganancia y pérdida, §15.2B; en medio
inhomogéneo las fases $\arg\{A_q\}$ son aleatorias e independientes). Sustituyendo:
$$U(z,t) = \mathcal{A}\!\left(t-\frac{z}{c}\right)\exp\left[j2\pi\nu_0\left(t-\frac{z}{c}\right)\right] \qquad (15.4\text{-}27)$$
$$\mathcal{A}(t) = \sum_q A_q\exp\left(\frac{jq2\pi t}{T_F}\right) \qquad (15.4\text{-}28),\qquad
  T_F = \frac{1}{\nu_F} = \frac{2d}{c} \qquad (15.4\text{-}29)$$
$\mathcal{A}(t)$ es periódica con periodo $T_F$; $\mathcal{A}(t - z/c)$ periódica en $z$ con periodo
$cT_F = 2d$. Con $M = 2S+1$ modos ($q = 0,\pm1,\dots,\pm S$) de coeficientes iguales $A_q = A$:
$$\mathcal{A}(t) = A\sum_{q=-S}^{S}\exp\left(\frac{jq2\pi t}{T_F}\right) = A\sum_{q=-S}^{S}x^q
  = A\frac{x^{S+1}-x^{-S}}{x-1} = A\frac{x^{S+\frac12}-x^{-S-\frac12}}{x^{\frac12}-x^{-\frac12}} \qquad (15.4\text{-}30)$$
con $x = \exp(j2\pi t/T_F)$, de donde
$$\mathcal{A}(t) = A\,\frac{\sin(M\pi t/T_F)}{\sin(\pi t/T_F)} \qquad (15.4\text{-}31)$$
$$I(t,z) = |A|^2\,\frac{\sin^2[M\pi(t - z/c)/T_F]}{\sin^2[\pi(t-z/c)/T_F]} \qquad (15.4\text{-}32)$$
periódica en $t$ (Fig. 15.4-9, p. 617): pulsos de periodo $T_F$, duración $T_F/M$ y pico $M\bar I$
($\bar I$ = intensidad media). Como $M\propto\Delta\nu$: si $M\approx\Delta\nu/\nu_F$ entonces
$\tau_{\rm pulse} = T_F/M\approx1/\Delta\nu$ ⇒ **la duración es inversa al ancho de línea atómico**;
razón pico/media = $M$. El periodo $T_F = 2d/c$ es el tiempo de ida y vuelta: la luz es un único pulso
estrecho que rebota entre los espejos (Fig. 15.4-10, p. 618) y en cada reflexión en el espejo de
salida transmite un pulso; separación espacial $2d$, longitud espacial $d_{\rm pulse} = c\tau_{\rm pulse} = 2d/M$.

**Tabla 15.4-1 — Propiedades del tren mode-locked (p. 617):**

| Propiedad | Valor | Propiedad | Valor |
|---|---|---|---|
| Periodo temporal | $T_F = 2d/c$ | Duración del pulso | $\tau_{\rm pulse} = T_F/M = 1/\Delta\nu$ |
| Periodo espacial | $2d$ | Longitud del pulso | $d_{\rm pulse} = 2d/M$ |
| Intensidad media | $\bar I$ | Intensidad pico | $I_p = M\bar I$ |

Ejemplo numérico (p. 618): Nd³⁺:vidrio a $\lambda_o = 1.05$ μm, $n = 1.5$, $\Delta\nu = 7$ THz
(Tabla 14.3-1) ⇒ $\tau_{\rm pulse} = 1/\Delta\nu\approx140$ fs, $d_{\rm pulse}\approx42$ μm; con
$d = 15$ cm, $\nu_F = c/2d = 1$ GHz ⇒ $M = \Delta\nu/\nu_F = 7000$ modos, pico 7000× la media. Medios
de línea ancha ⇒ mode locking mejor que Q-switching para pulsos cortos; gases (líneas estrechas) no dan
pulsos ultracortos. Con amplitudes/fases realistas los resultados son similares.

**Ejercicio 15.4-3 — Demostración por computador (p. 618).** Programar $I(t) = |\mathcal{A}(t)|^2$ con
(15.4-28), $M = 11$: (a) magnitudes y fases iguales (reproduce lo anterior); (b) magnitudes con perfil
gaussiano $|A_q| = \exp[-\frac12(q/5)^2]$ y fases iguales; (c) magnitudes iguales y fases aleatorias
uniformes en $[0, 2\pi)$.

**Métodos de mode locking (p. 618–619).**
- **Activo**: conmutador óptico controlado externamente (acusto-óptico o electro-óptico, caps. 19, 20)
  intracavidad que bloquea la luz salvo cuando pasa el pulso (Fig. 15.4-10). Si las fases son iguales
  (por "accidente afortunado"), el pulso pasa sin pérdida y se perpetúa; cualquier otra combinación
  se bloquea total o parcialmente ⇒ solo oscila la combinación de fases iguales. Matemáticamente: el
  campo multimodal (15.4-25) satisface la ecuación de onda para cualquier fase, pero solo las fases
  iguales cumplen las condiciones de contorno del conmutador ⇒ solución única.
- **Pasivo** con **absorbedor saturable** (§14.4A): transmite pulsos intensos y absorbe los débiles ⇒
  solo oscila la configuración de fases que forma un pulso intenso. **SESAM** (*semiconductor
  saturable-absorber mirror*): absorbedores saturables en reflexión; 800–1600 nm, pulsos de fs a ns,
  mW a cientos de W; también permiten **Q-switched mode locking** (ráfagas de pulsos mode-locked bajo
  una envolvente Q-switched).
- **Kerr-lens mode locking (KLM)**: usa el índice dependiente de la intensidad (§21.3): un medio Kerr
  (el propio medio de ganancia u otro) actúa como lente de distancia focal inversamente proporcional
  a la intensidad (Ej. 21.3-2); una apertura en posición adecuada deja pasar solo el modo de alta
  intensidad (reducido por la lente Kerr), o bien se aprovecha el menor tamaño modal para aumentar el
  solape con el bombeo enfocado (ganancia efectiva mayor). Es intrínsecamente de banda ancha (proceso
  paramétrico). La recuperación rápida del mode locking pasivo da pulsos más cortos que el activo.
  Ambos sirven para medios homogéneos e inhomogéneos.

**Ejemplos de láseres mode-locked (p. 619–620).** Tabla 15.4-2 (transcrita abajo). Las duraciones
observadas dependen del método y están limitadas por **no linealidades y dispersión** en el medio.
Ti:zafiro: sintonizable 700–1050 nm, pulsos de 10 fs; comercial: 50 nJ, 10 fs, 1 MW pico, 80 MHz;
más corto con compresión de pulsos (§22.2A); su $\Delta\nu$ se puede restringir para pulsos de ps.
Aplicaciones: medidas resueltas en tiempo, imagen, metrología, comunicaciones, materiales, medicina.

**Ejemplo 15.4-2 — Mode locking en láser de fibra de Yb (p. 620).** Fibra de sílice dopada con Yb,
mode locking pasivo, $\lambda_o = 1070$ nm: 10 W medios, pulsos de **200 nJ, 40 kW pico, 5 ps, 50 MHz**.
Como $\Delta\nu = 5$ THz, se esperaría $\tau_{\rm pulse} = 1/\Delta\nu = 200$ fs; la discrepancia se debe
a la **dispersión de velocidad de grupo**, que ensancha y *chirpea* el pulso (Fig. 5.6-3). La
dispersión normal de la sílice cerca de 1 μm se cancela con dispersión anómala de una FBG o una
fibra de cristal fotónico ⇒ 200 fs.

Extensión de longitudes de onda (p. 620): la potencia del Ti:zafiro mode-locked permite **generación de
armónicos** (cap. 21): SHG ⇒ 350–525 nm; THG ⇒ 230–350 nm; hacia el IR (> 1 μm) con láseres Raman de
fibra o **conversión paramétrica descendente** (§21.4C): OPO bombeado sincrónicamente con LBO o
cristal periódicamente polarizado ⇒ señal e idler mode-locked en 1.0–3.3 μm.

### Reading List (p. 621–624)

Libros sobre láseres (Koechner, Quimby, Yariv & Yeh, Band, Noginov *Solid-State Random Lasers*,
Rullière *Femtosecond Laser Pulses*, Silfvast, Svelto, Siegman *Lasers*, Milonni & Eberly, etc.);
libros y artículos sobre UV y rayos X (Jaeglé, Rocca, Attwood, Kapteyn-Murnane-Christov *Extreme
Nonlinear Optics*…); artículos (feature issue on fiber lasers *JOSA B* 24(8) 2007; Cao sobre láseres
aleatorios; Keller *Nature* 424, 831, 2003 sobre láseres ultrarrápidos compactos; Kim *et al.* sobre
RFL 1239/1484 nm; Perry & Mourou *Science* 264, 917, 1994); históricos (Hecht *Beam*; Schawlow &
Townes *Phys. Rev.* 112, 1940, 1958; Maiman *Nature* 187, 493, 1960; Stolen, Ippen & Tynes, Raman
oscillation in glass waveguide, *Appl. Phys. Lett.* 20, 62, 1972; Letokhov 1968 sobre generación de
luz por medio dispersor con absorción negativa; Lamb *Phys. Rev.* 134, A1429, 1964; Gordon, Zeiger &
Townes 1955; Basov & Prokhorov 1955; Fabrikant 1940).

---

## Tablas y datos numéricos útiles

**Tabla 15.3-1 — Características típicas de láseres conocidos (p. 606).** (g) gas, (s) sólido,
(l) líquido, (p) plasma; S/M = monomodo o multimodo; $\eta_c$ = eficiencia de conversión (potencia
óptica / potencia eléctrica; para pulsados, energías); potencias/energías representativas.

| Medio | $\lambda_o$ | S/M | CW/Pulsado | $\eta_c$ (%) | Potencia / energía | Diagrama |
|---|---|---|---|---|---|---|
| Ag¹⁹⁺ (p) | 13.9 nm | M | Pulsado | 0.0002 | 25 μJ | |
| C⁵⁺ (p) | 18.2 nm | M | Pulsado | 0.0005 | 2 mJ | Fig. 13.1-1 |
| ArF excímero (g) | 193 nm | M | Pulsado | 1 | 200 mJ | |
| KrF excímero (g) | 248 nm | M | Pulsado | 1 | 500 mJ | |
| He–Cd (g) | 442 nm | S/M | CW | 0.1 | 100 mW | |
| Ar⁺ (g) | 515 nm | S/M | CW | 0.05 | 10 W | |
| Rodamina-6G (l) | 560–640 nm | S/M | CW | 0.005 | 100 mW | Fig. 13.1-5 |
| He–Ne (g) | 633 nm | S/M | CW | 0.05 | 10 mW | Fig. 13.1-2 |
| Kr⁺ (g) | 647 nm | S/M | CW | 0.01 | 1 W | |
| Rubí (s) | 694 nm | M | CW | 0.1 | 5 W | Fig. 14.3-1 |
| Alejandrita (s) | 700–820 nm | M | CW | 0.1 | 1 W | Fig. 13.1-8 |
| Ti:zafiro (s) | 700–1050 nm | M | CW | 0.1 | 5 W | Fig. 15.3-4 |
| Yb³⁺:YAG (s) | 1030 nm | S/M | CW | 5 | 100 W | Fig. 15.3-3 |
| Nd³⁺:vidrio (s) | 1053 nm | M | Pulsado | 1 | 50 J | Fig. 14.3-3 |
| Nd³⁺:YAG (s) | 1064 nm | S/M | CW | 5 | 50 W | Fig. 13.1-9 |
| Nd³⁺:YVO₄ (s) | 1064 nm | S/M | CW | 10 | 30 W | Fig. 15.3-1 |
| Yb³⁺:fibra de sílice (s) | 1075 nm | S/M | CW | 20 | 1500 W | |
| Er³⁺:fibra de sílice (s) | 1550 nm | S/M | CW | 10 | 100 W | Fig. 14.3-6 |
| Tm³⁺:fibra de fluoruro (s) | 1.8–2.1 μm | S/M | CW | 5 | 150 W | |
| He–Ne (g) | 3.39 μm | S/M | CW | 0.05 | 20 mW | Fig. 13.1-2 |
| CO₂ (g) | 10.6 μm | S/M | CW | 10 | 500 W | Fig. 13.1-4 |
| H₂O (g) | 28 μm | S/M | CW | 0.02 | 100 mW | |
| FEL en UCSB | 60 μm – 2.5 mm | M | Pulsado | 0.5 | 5 mJ | |
| H₂O (g) | 118.7 μm | S/M | CW | 0.01 | 50 mW | |
| CH₃OH (g) | 118.9 μm | S/M | CW | 0.02 | 100 mW | |
| HCN (g) | 336.8 μm | S/M | CW | 0.01 | 20 mW | |

Notas de la tabla: los diodos láser tienen las mayores eficiencias (> 50 %, §17.4C); "CW" puede
operar pulsado; "Pulsado" suele operarse solo así.

**Tabla 15.4-2 — Duraciones de pulso mode-locked (p. 620)** (H homogéneo, I inhomogéneo; $\Delta\nu$ de
Tabla 14.3-1):

| Medio | H/I | $\Delta\nu$ | $\tau_{\rm pulse} = 1/\Delta\nu$ calculada | Observada |
|---|---|---|---|---|
| Ti³⁺:Al₂O₃ | H | 100 THz | 10 fs | 10 fs |
| Rodamina-6G | H/I | 40 THz | 25 fs | 27 fs |
| Nd³⁺:vidrio (fosfato) | I | 7 THz | 140 fs | 150 fs |
| Er³⁺:fibra de sílice | H/I | 5 THz | 200 fs | 200 fs |
| Nd³⁺:YAG | H | 150 GHz | 7 ps | 7 ps |
| Ar⁺ | I | 3.5 GHz | 286 ps | 150 ps |
| He–Ne | I | 1.5 GHz | 667 ps | 600 ps |
| CO₂ | I | 60 MHz | 16 ns | 20 ns |

**Otros datos numéricos dispersos:**
- Ejemplo p. 573: $\lambda_o = 1$ μm, $\tau_p = 1$ ns, $n = 1$ ⇒ $N_t\approx2.1\times10^7$ cm⁻³ (solo
  ensanchamiento por tiempo de vida).
- Rubí (Ej. 15.1-1, p. 574): $\lambda_o = 694.3$ nm, $\alpha(\nu_0)\approx0.2$ cm⁻¹ a 300 K sin bombeo,
  $N_a = 1.58\times10^{19}$ cm⁻³ de Cr³⁺, $n = 1.76$.
- He–Ne (Ej. 15.2-1, p. 582; Prob. 15.2-3, 15.2-5): $\Delta\nu_D = 1.5$ GHz, $\gamma_0(\nu_0) = 2\times10^{-3}$ cm⁻¹
  (2.5×10⁻³ en Prob. 15.2-3), $\lambda_o = 632.8$ nm.
- Ar⁺ (p. 589): $\Delta\nu_D = 3.5$ GHz ⇒ $d < 4.3$ cm para monomodo longitudinal; líneas 488–514.5 nm.
- Fig. 15.2-3 (p. 579): $g_0 = 2\gamma_0 d = 0.5$, $L = 0.02$ ⇒ $\mathcal{T}_{\rm op} = 0.08$.
- Nd:YVO₄ (p. 592): $n\approx2.0$; bombeo 808 nm (⁴F₅/₂ a 1.53 eV); líneas 1.064 μm, 1.34 μm, 914 nm;
  doblados 532 nm y 457 nm.
- Nd:YAG (p. 593): $\lambda_o = 1.06415$ μm (1.4269 eV → 0.2616 eV); 1.12238 μm (1.4165 → 0.3117 eV);
  946 nm; doblados 532, 561, 473 nm; rango 1.052–1.122 μm.
- Yb:YAG (p. 594): bombeo 940 nm, láser 1030 nm, doblado 515 nm; dopaje ≈ 25 %, ~25 pasos de bombeo.
- Ti:zafiro (p. 594–595): $n\approx1.76$, ~1 % Ti; 700–1050 nm; CW ≈ 5 W; 10 fs, 50 nJ, 80 MHz, 1 MW
  pico; bombeo 532 nm (Nd doblado), 515 nm (Yb:YAG doblado) o Ar⁺.
- Fibras (p. 596): Yb 1070–1080 nm > 1 kW, $\Delta\nu\approx1$ THz, $M^2 < 1.1$, $\eta_c > 25$ %; Er
  1550–1570 nm, cientos de W, < 400 GHz, $\eta_c > 10$ %; Tm 1.8–2.1 μm, 150 W, ≈ 75 GHz, $\eta_c\approx5$ %.
- Raman en fibra (p. 598): $\nu_R\approx40$ THz (fosfosilicato), $\approx13$ THz (sílice-germanio);
  RFL 1064 → 1239 → 1484 nm; pendiente ≈ 0.25 W/W.
- Excímeros (p. 601): F₂ 153, ArF 193, KrF 248, XeCl 308, XeF 351 nm. HF 2.7–3.1 μm; DF 3.5–4.0 μm.
- EUV de C⁵⁺ (p. 603): 68 eV, 18.2 nm, $t_{\rm sp}\approx12$ ps, $\gamma d\approx6$, 100 kW, 2 mJ, 20 ns,
  5 mrad; Ag¹⁹⁺: 13.9 nm, 25 μJ, $\gamma = 35$ cm⁻¹, $\gamma d\approx13.6$, 6 mrad. Multicapas Si/Mo > 70 %.
- FEL (p. 604–605): $\Lambda$ ~ cm, ~100 periodos, campo ~ kG, 50 MeV típico; LCLS 100 fs a 1.5 Å.
- Microchip Nd:YAG Q-switched (p. 613): cavidad 1 mm, 1 W a 808 nm ⇒ 30 μJ, 250 ps, 10 kHz, 300 mW a 532 nm.
- Nd:vidrio mode-locked (p. 618): $n = 1.5$, $\Delta\nu = 7$ THz, 140 fs, 42 μm, $d = 15$ cm, $\nu_F = 1$ GHz,
  $M = 7000$.
- Fibra Yb mode-locked (p. 620): 1070 nm, 10 W, 200 nJ, 40 kW, 5 ps (→ 200 fs con compensación), 50 MHz,
  $\Delta\nu = 5$ THz.
- SESAM (p. 619): 800–1600 nm, fs–ns, mW–cientos de W. SHG de Ti:zafiro: 350–525 nm; THG: 230–350 nm;
  OPO sincrónico: 1.0–3.3 μm (p. 620).

---

## Problemas al final del capítulo (p. 624–626)

(La numeración salta porque 15.1-1, 15.2-1, 15.4-1, 15.4-2 y 15.4-3 son los ejercicios del texto.
Los marcados con * son avanzados.)

- **15.2-2 Número de modos longitudinales.** Ar⁺ con resonador de 100 cm, $n=1$: (a) $\nu_F$; (b) número
  de modos si $\Delta\nu_D = 3.5$ GHz y la pérdida es la mitad de la ganancia pico; (c) $d$ para
  monomodo, y lo mismo para CO₂ con $\Delta\nu_D = 60$ MHz.
- **15.2-3 Deriva de frecuencia de los modos.** He–Ne con espejos 97 %/100 %, $\Delta\nu_D = 1.5$ GHz,
  $\gamma_0(\nu_0) = 2.5\times10^{-3}$ cm⁻¹; la longitud deriva térmicamente: hallar el rango de $d$ tal
  que oscilen uno o dos (no más) modos longitudinales.
- **15.2-4 Control de modos con etalón.** Gas a 515 nm, espejos a 50 cm, $\tau_p = 0.33$ ns, $B = 1.5$ GHz,
  $n = 1$; etalón pasivo de separación $d$ y fineza $\mathcal{F}$: sugerir $d$ y $\mathcal{F}$; ¿mejor
  dentro o fuera del resonador?
- **15.2-5 Potencias modales en láser multimodo.** He–Ne a 632.8 nm, 50 mW multimodo, $\Delta\nu_D = 1.5$ GHz,
  $n=1$, $d = 30$ cm: (a) número de modos si $\gamma_0$ máx = 2× pérdida; (b) potencia del modo más
  fuerte si se maximiza su intensidad.
- **15.2-6 Salida de un láser de gas monomodo.** 10 cm, línea de 600 nm, $\mathcal{R}_1 = 99$ %,
  $\mathcal{R}_2 = 100$ %, $n = 1$, área 1 mm², $\gamma_0(\nu_0) = 0.1$ cm⁻¹, $\phi_s = 1.43\times10^{19}$
  fotones/cm²·s: (a) $\alpha_{m1}$, $\alpha_{m2}$, $\alpha_r$ (con $\alpha_s = 0$); (b) $\tau_p$;
  (c) $\phi_o$ y $P_o$.
- **15.2-7 Transmitancia de un resonador láser.** Dada la transmitancia medida (Fig. P15.2-7: picos
  separados 200 MHz, ancho 2 MHz, alrededor de 5×10¹⁴ Hz), $n=1$: (a) longitud del resonador, $\tau_p$ y
  ganancia umbral; (b) esbozar la transmitancia con bombeo insuficiente para oscilar, con $\nu_0 = 5\times10^{14}$ Hz.
- **15.2-8 Ecuaciones de tasa en 4 niveles.** $V = 1$ cm³; escribir las ecuaciones de tasa de $N_2$,
  $N_1$, $N$ y $\mathfrak{n}$ en función de $N_0$, $\sigma(\nu)$, $t_{\rm sp}$, $\tau_1$, $\tau_2$,
  $\tau_{21}$, $\tau_p$; hallar los valores estacionarios de $N$ y $\mathfrak{n}$.
- **15.3-1 Operación de un láser Yb:YAG.** Transición ²F₅/₂ → ²F₇/₂ a 1.030 μm, bombeo con diodo InGaAs,
  3 niveles: (a) $\lambda$ y ancho (nm) de la banda de bombeo (1.31915 eV, ancho 0.02475 eV);
  (b) con $\sigma_0 = 2\times10^{-20}$ cm² y $N_a = 1.4\times10^{20}$ cm⁻³, $\alpha(\nu_0)$ y $\gamma(\nu_0)$
  en equilibrio térmico a 300 K; (c) barra de 6 cm × 2 mm, $\mathcal{R}_1 = 0.8$, $\mathcal{R}_2 = 1.0$:
  $\alpha_r$ y $\tau_p$; (d) $N_t$; (e) ventaja de que el nivel 3 esté cerca del 2; (f) qué cambiaría con
  YVO₄ como huésped.
- **15.3-2 Diferencia de población umbral de un láser de Ar⁺.** Resonador de 1 m, espejos 98 %/100 %,
  $\lambda_o = 515$ nm, $t_{\rm sp} = 10$ ns, $\Delta\lambda = 0.003$ nm, nivel inferior vacío, diámetro
  1 mm: (a) $\tau_p$; (b) $N_t$.
- **15.3-3 Tiempo de vida espontáneo de una transición EUV.** Si a 500 nm $t_{\rm sp} = 10$ ns, estimar
  $t_{\rm sp}$ a 18.2 nm con la misma fuerza de transición $S$; comparar con la Tabla 14.3-1.
- **\*15.4-4 Transitorios en láser gain-switched.** (a) Con $X = \mathfrak{n}/\tau_p$, $Y = N/N_t$,
  $s = t/\tau_p$, mostrar que (15.4-3) y (15.4-6) se vuelven $dX/ds = -X + XY$,
  $dY/ds = a(Y_0 - Y) - 2XY$, con $a = \tau_p/t_{\rm sp}$, $Y_0 = N_0/N_t$. (b) Programar la solución
  para encendido ($Y_0$: 0 → 2) y apagado (2 → 0), con $X = 10^{-5}$ inicial; tiempos de transición para
  $a = 10^{-3}, 1, 10^3$; comentar.
- **\*15.4-5 Potencia de un láser de rubí Q-switched.** Barra de 15 cm, 1 cm², resonador 20 cm,
  $\mathcal{R}_1 = 0.95$, $\mathcal{R}_2 = 0.7$, Cr³⁺ $1.58\times10^{19}$ cm⁻³, $\sigma(\nu_0) = 2\times10^{-20}$
  cm², población inicial en nivel 2 de 10¹⁹ cm⁻³, bombeo a ≈ 450 nm, vida del nivel 2 ≈ 3 ms:
  (a) potencia de bombeo para mantener 10¹⁹ cm⁻³; (b) potencia radiada espontáneamente antes del
  Q-switch; (c) potencia pico, energía y duración del pulso.
- **\*15.4-6 Operación de un láser cavity-dumped.** Esbozar $N_t(t)$, $N(t)$, $\mathfrak{n}(t)$ y
  $\phi_o(t)$ durante dos ciclos.
- **15.4-7 Mode locking con amplitudes lorentzianas.** $A_q = \sqrt{P}\,\frac{(\Delta\nu/2)^2}{(q\nu_F)^2+(\Delta\nu/2)^2}$,
  $q = -\infty\dots\infty$, fases iguales: (a) potencia media; (b) potencia pico; (c) duración FWHM.
- **15.4-8 Generación de segundo armónico.** Cristal no lineal dentro del resonador con ganancia en
  $\nu$; conversión a $2\nu$ a tasa $\zeta\mathfrak{n}$ (s⁻¹m⁻³) y producción de fotones por el láser a
  tasa $\xi\mathfrak{n}$; tiempos de vida $\tau_p$ y $\tau_{p2}$: escribir las ecuaciones de tasa de
  $\mathfrak{n}$ y $\mathfrak{n}_2$ y hallar sus valores estacionarios.

---

## Relación con Óptica No Lineal

**Con los temas del curso:**
- *Ondas EM y haz gaussiano*: la salida TEM₀₀ de un resonador de espejos esféricos es un haz gaussiano
  (§15.2C, p. 586; Fig. 15.2-10); los modos Hermite–Gauss de orden superior tienen distinta pérdida por
  difracción. Esto fija el perfil espacial que se usa en SHG, enfoque y en el cálculo de intensidades
  pico para efectos no lineales ($I_p = M\bar I$ en mode locking, Tabla 15.4-1).
- *Absorción y dispersión; índice complejo*: el amplificador láser es una lorentziana de ganancia con un
  desfase antisimétrico asociado, (15.1-3) y Fig. 15.1-1 (p. 570–571) — la misma relación
  Kramers–Kronig que liga $\chi'$ y $\chi''$; el *frequency pulling* (15.1-23) es su consecuencia
  directa en la cavidad.
- *Pulsos en medios dispersivos, GVD*: el Ej. 15.4-2 (p. 620) muestra que un láser de fibra de Yb con
  $\Delta\nu = 5$ THz da 5 ps en vez de 200 fs por la GVD de la sílice (dispersión normal a 1 μm), y que
  se corrige con dispersión anómala (FBG o fibra de cristal fotónico); el Ti:zafiro usa un par de
  prismas intracavidad para compensar dispersión (Fig. 15.3-4b, p. 595). La Tabla 15.4-2 (p. 620) dice
  explícitamente que las duraciones están limitadas por "nonlinearities and dispersion in the medium".
- *Polarización y cristales*: ventanas de Brewster (Fig. 15.2-13, p. 589) y filtro birrefringente del
  Ti:zafiro (p. 595) como ejemplos de selección de polarización y sintonía; relevante para cumplir
  ajuste de fase y polarizaciones en cristales χ⁽²⁾.
- *χ⁽²⁾ (SHG, OPO)*: doblado intracavidad de Nd:YVO₄/Nd:YAG con LBO (Fig. 15.3-1b, p. 592; 532 nm) y de
  Yb:YAG (515 nm); SHG/THG del Ti:zafiro (350–525 y 230–350 nm) y OPO bombeado sincrónicamente con LBO o
  cristales periódicamente polarizados (1.0–3.3 μm) (p. 620); Prob. 15.4-8 plantea las ecuaciones de tasa
  de un láser con SHG intracavidad; OPO de 1–2 μm doblado para cubrir 600 nm (p. 602).
- *χ⁽³⁾, índice dependiente de la intensidad*: el **Kerr-lens mode locking** (p. 619) es una aplicación
  directa de $n = n_0 + n_2 I$ (§21.3, Ej. 21.3-2: lente Kerr con $f\propto1/I$); los absorbedores
  saturables (SESAM) son no linealidades de absorción. **HHG** (p. 604) como no linealidad extrema para
  EUV.
- *Raman y Brillouin estimulados*: láseres Raman de fibra en cascada (p. 597–598; $\nu_R\approx13$ THz en
  sílice-Ge, 40 THz en fosfosilicato; Ej. 15.3-1); láseres Brillouin de fibra (p. 598); ganancia Raman
  sin inversión de población.
- *Propagación de pulsos en fibras, SPM, solitones*: la configuración double-clad (p. 595–596) existe
  precisamente para evitar los efectos no lineales de concentrar bombeo en un núcleo pequeño; los
  láseres de fibra mode-locked (Ej. 15.4-2) son el punto de partida de los estudios de solitones y de
  supercontinuo.
- *Mode locking como base de los pulsos ultracortos*: §15.4D da el formalismo (suma de $M$ modos
  equiespaciados, 15.4-25 a 15.4-32) y la relación $\tau_{\rm pulse}\approx1/\Delta\nu$ (p. 617): es el
  "límite de transformada" que luego la óptica no lineal (SPM) y la dispersión modifican; el Ej. 15.4-3
  (programa con fases aleatorias/gaussianas) es un buen taller numérico.
- *Fuentes típicas del laboratorio de ONL*: Ti:zafiro (700–1050 nm, 10 fs, 50 nJ, 80 MHz, 1 MW pico,
  p. 595 y 619), fibras de Yb/Er mode-locked (p. 620), Nd:YAG/Nd:YVO₄ Q-switched y doblados (p. 592–593,
  613), con sus parámetros en Tablas 15.3-1 y 15.4-2.

**Con el proyecto final (anillos add-drop en Si₃N₄, dispersión de guías, supercontinuo, sensado):**
- *Resonador Fabry–Perot ↔ anillo*: las fórmulas de modos, FSR ($\nu_F = c/2d$), fineza
  ($\mathcal{F}\approx\pi/\alpha_r d = 2\pi\tau_p\nu_F$), ancho de modo ($\delta\nu = \nu_F/\mathcal{F} = 1/2\pi\tau_p$)
  y tiempo de vida del fotón ($\tau_p = 1/\alpha_r c$) (p. 571–572) son las mismas que se usan para el
  anillo (con $2d$ → perímetro $L$ y $\alpha_r$ → pérdidas de propagación + acoplamiento); de aquí
  salen $Q = \nu/\delta\nu = 2\pi\nu\tau_p$ y la relación entre pérdidas de acoplamiento y extinción
  (análogo de $\alpha_{m1}$, $\alpha_{m2}$ y de la transmitancia óptima (15.2-9)).
- *Frequency pulling y Lamb dip* (p. 574–576, 585) como ejemplos de corrimiento de resonancia por la
  respuesta del medio: el sensado de índice de refracción es el mismo mecanismo (cambio de $n$ del
  cladding ⇒ desplazamiento de $\nu_q$), y la distinción entre $\delta\nu$ (ancho del modo) y el
  desplazamiento determina el límite de detección.
- *Etalón intracavidad y resonadores acoplados* (Fig. 15.2-14, 15.2-15, p. 589–590): selección de un
  modo por coincidencia de dos peines de FSR distinto es el efecto Vernier que se usa en anillos
  acoplados; útil para pensar la lectura de resonancias en el add-drop.
- *Supercontinuo y dispersión de guías*: la lección del Ej. 15.4-2 (compensar GVD normal con dispersión
  anómala diseñada en la guía/FBG/PCF, p. 620) es exactamente el problema de ingeniería de dispersión de
  la guía de Si₃N₄ para operar en régimen anómalo y generar supercontinuo; las fuentes de bombeo
  candidatas (Ti:zafiro, fibra de Yb a 1 μm, fibra de Er a 1.55 μm) y sus energías/duraciones están
  en §15.3A y §15.4D.
- *Raman en cascada* (p. 597–598) como referencia para el corrimiento Raman de solitones y la
  extensión espectral hacia el IR en el supercontinuo.
