# Capítulo 14 — Laser Amplifiers (Saleh & Teich, 2.ª ed.)

Páginas del libro 532–566 (PDF 554–588). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007,
cap. 14. Todas las páginas citadas abajo son páginas del libro (PDF = libro + 22).
Notación del libro: dependencia temporal $e^{j\omega t}$ (en este capítulo $\exp(j2\pi\nu t)$),
$j=\sqrt{-1}$, campos reales en caligráfica $\mathcal{E}(z)$, amplitud compleja $E(z)$,
unidades SI (el libro mezcla cm⁻¹ y cm² en los ejemplos numéricos; se indica cuando ocurre).
Las secciones marcadas con * son las que el libro señala como avanzadas/opcionales.

---

## Resumen del capítulo

El capítulo desarrolla la teoría del **amplificador láser** (amplificador óptico coherente):
un medio con inversión de población ($N = N_2 - N_1 > 0$) amplifica por emisión estimulada
un haz cuasi-monocromático conservando su fase. Se deducen el coeficiente de ganancia
$\gamma(\nu) = N\sigma(\nu)$, la ganancia total $G = \exp(\gamma d)$, el ancho de banda
(dado por la forma de línea $g(\nu)$) y el corrimiento de fase $\varphi(\nu)$ (ligado a
$\gamma(\nu)$ por la transformada de Hilbert, por causalidad). Luego se estudian las
**ecuaciones de tasa** con bombeo, que dan la diferencia de población en estado estacionario
$N = N_0/(1+\tau_s W_i)$ y los esquemas de bombeo de **cuatro y tres niveles**. En §14.3 se
describen amplificadores reales: rubí (3 niveles), vidrio dopado con Nd³⁺ (4 niveles; NIF),
**fibra de sílice dopada con erbio (EDFA)** y **amplificadores Raman de fibra (RFA)**, con
una tabla de parámetros de transiciones láser comunes. §14.4 trata la **no linealidad del
amplificador**: saturación de la ganancia, $\gamma = \gamma_0/(1+\phi/\phi_s)$, en medios
homogéneos e inhomogéneos (Doppler, *hole burning*), absorbedores saturables y la relación
no lineal entrada–salida. §14.5 trata el **ruido** por emisión espontánea amplificada (ASE)
y su estadística de fotones.

---

## Secciones

### Introducción del capítulo (pp. 533–534)

- **Amplificador óptico coherente** (p. 533): aumenta la amplitud de un campo óptico
  manteniendo su fase (o añadiendo un corrimiento fijo); un **amplificador incoherente** solo
  aumenta la intensidad sin conservar fase.
- Principio: **LASER** = *Light Amplification by Stimulated Emission of Radiation*. Un fotón
  induce a un átomo en el nivel superior a emitir un fotón *clon* (misma frecuencia,
  dirección, polarización y modo). Como la emisión estimulada solo ocurre si la energía del
  fotón ≈ diferencia de energía de la transición, el proceso está limitado a la banda
  determinada por el **ancho de línea atómico** (p. 533).
- En equilibrio térmico la luz se atenúa (más átomos abajo que arriba). Para amplificar se
  necesita una **inversión de población** (no equilibrio), lograda con una fuente de potencia
  externa: el **bombeo** (Fig. 14.0-1, p. 534). "Átomos" y "niveles atómicos" se entienden
  en sentido amplio: medio activo y niveles láser.
- **Fig. 14.0-2** (p. 534): (a) amplificador ideal: lineal, ganancia constante dentro de su
  ancho de banda, fase lineal en frecuencia (retardo); (b) amplificador real: ganancia y fase
  dependientes de la frecuencia (función de transferencia), **saturación** para entradas
  grandes (no linealidad, genera armónicos si el ancho de banda los deja pasar) y **ruido**.
- Características que caracterizan un amplificador (p. 534): ganancia, ancho de banda,
  corrimiento de fase, fuente de potencia (bombeo), no linealidad/saturación de ganancia,
  ruido. El capítulo se apoya en el cap. 13 (§13.3 en particular).

---

### 14.1 Theory of Laser Amplification (p. 535)

**Planteamiento** (p. 535): onda plana monocromática de frecuencia $\nu$ viajando en $z$,
campo $\mathcal{E}(z) = \mathrm{Re}\{E(z)\exp(j2\pi\nu t)\}$, amplitud compleja $E(z)$,
intensidad $I(z) = |E(z)|^2/2\eta$ ($\eta$ = impedancia del medio), **densidad de flujo de
fotones** $\phi(z) = I(z)/h\nu$ (fotones por segundo por unidad de área). El medio tiene dos
niveles de energía cuya diferencia ≈ $h\nu$; $N_1$, $N_2$ son los átomos por unidad de volumen
en los niveles inferior y superior. La onda se amplifica con **coeficiente de ganancia**
$\gamma(\nu)$ (por unidad de longitud) y sufre un **corrimiento de fase** $\varphi(\nu)$ (por
unidad de longitud). $\gamma(\nu)>0$ amplifica, $\gamma(\nu)<0$ atenúa.

#### 14.1A Gain and Bandwidth (p. 535)

Tres interacciones fotón–átomo (§13.3): absorción (átomo abajo), emisión estimulada (átomo
arriba) y emisión espontánea (independiente de los fotones presentes; es la fuente de ruido,
§14.5).

Probabilidad por unidad de tiempo (s⁻¹) de que un átomo no excitado absorba un fotón
[de (13.3-19) y (13.3-15)]:

$$W_i = \phi\,\sigma(\nu), \qquad (14.1\text{-}1)$$

con $\sigma(\nu) = (\lambda^2/8\pi t_{sp})\,g(\nu)$ la **sección eficaz de transición** a la
frecuencia $\nu$, $g(\nu)$ la **función de forma de línea normalizada**, $t_{sp}$ el tiempo de
vida espontáneo y $\lambda$ la longitud de onda *en el medio*. La probabilidad de emisión
estimulada es la misma que la de absorción (p. 535).

**Coeficiente de ganancia** (p. 535): densidad media de fotones absorbidos por unidad de
tiempo y volumen $N_1 W_i$; de clones generados $N_2 W_i$; neto $N W_i$ con
$N = N_2 - N_1$ la **diferencia de población**. $N>0$: **inversión de población**, el medio
amplifica; $N<0$ atenúa; $N=0$ transparente. Los fotones estimulados viajan en la misma
dirección que los incidentes (Fig. 14.1-1, p. 536). En un cilindro incremental de longitud
$dz$ y área unitaria:

$$d\phi = N W_i\, dz. \qquad (14.1\text{-}2)$$

Con (14.1-1):

$$\frac{d\phi(z)}{dz} = \gamma(\nu)\,\phi(z), \qquad (14.1\text{-}3)$$

$$\boxed{\gamma(\nu) = N\sigma(\nu) = N\frac{\lambda^2}{8\pi t_{sp}}\,g(\nu)} \qquad (14.1\text{-}4)\ \text{Gain Coefficient (p. 536)}$$

Solución:

$$\phi(z) = \phi(0)\exp[\gamma(\nu)z], \qquad (14.1\text{-}5)$$

$$I(z) = I(0)\exp[\gamma(\nu)z], \qquad (14.1\text{-}6)$$

(pues $I = h\nu\phi$). Así $\gamma(\nu)$ es también la ganancia de intensidad por unidad de
longitud. La deducción vale para cualquier signo de $N$: sin inversión ($N_2<N_1$) el medio
atenúa como $\phi(z) = \phi(0)\exp[-\alpha(\nu)z]$ con **coeficiente de atenuación**
$\alpha(\nu) = -\gamma(\nu) = -N\sigma(\nu)$. Un medio en equilibrio térmico no puede
amplificar (p. 536).

**Ganancia** (p. 536): para una región de longitud $d$, $G(\nu) = \phi(d)/\phi(0)$:

$$\boxed{G(\nu) = \exp[\gamma(\nu)\,d]} \qquad (14.1\text{-}7)\ \text{Amplifier Gain}$$

**Ancho de banda** (p. 537): la dependencia en frecuencia de $\gamma(\nu)$ está en
$g(\nu)$, de ancho $\Delta\nu$ centrada en $\nu_0 = (E_2 - E_1)/h$. El amplificador láser es
un **dispositivo resonante** con frecuencia y ancho de banda fijados por la transición
atómica. Relación entre anchos en frecuencia y en longitud de onda:
$\Delta\lambda = |\Delta(c_o/\nu)| = (c_o/\nu^2)\Delta\nu = (\lambda_o^2/c_o)\Delta\nu$.
Ejemplo: $\Delta\nu = 1$ THz a $\lambda_o = 0.6\ \mu$m ↔ $\Delta\lambda = 1.2$ nm.

Para forma de línea **lorentziana** [de (13.3-34)]:

$$g(\nu) = \frac{\Delta\nu/2\pi}{(\nu-\nu_0)^2 + (\Delta\nu/2)^2}, \qquad (14.1\text{-}8)$$

el coeficiente de ganancia también es lorentziano con el mismo ancho:

$$\gamma(\nu) = \gamma(\nu_0)\frac{(\Delta\nu/2)^2}{(\nu-\nu_0)^2 + (\Delta\nu/2)^2}, \qquad (14.1\text{-}9)$$

con $\gamma(\nu_0) = N\left(\lambda^2/4\pi^2 t_{sp}\Delta\nu\right)$ el coeficiente de
ganancia en el centro de línea (Fig. 14.1-2, p. 537).

**EJERCICIO 14.1-1 — Atenuación y ganancia en un amplificador de rubí** (p. 537):
(a) Cristal de rubí con dos niveles separados por $\lambda_o = 694.3$ nm, línea lorentziana
de $\Delta\nu = 330$ GHz, $t_{sp} = 3$ ms, $n = 1.76$. Si $N_1 + N_2 = N_a = 10^{22}$ cm⁻³,
determinar $N = N_2 - N_1$ y el coeficiente de atenuación $\alpha(\nu_0)$ en equilibrio
térmico a $T = 300$ K (distribución de Boltzmann, §13.2). (b) ¿Qué $N$ se necesita para
$\gamma(\nu_0) = 0.5$ cm⁻¹? (c) ¿Qué longitud de cristal da ganancia total 4 a $\nu_0$ con
$\gamma(\nu_0) = 0.5$ cm⁻¹? [El libro no da la solución; de (14.1-7): $d = \ln 4/0.5$ cm
$\approx 2.77$ cm.]

#### 14.1B Phase Shift (p. 538)

Como la ganancia depende de la frecuencia, el medio es **dispersivo** (§5.5) y hay un
corrimiento de fase asociado. Para medios **homogéneamente ensanchados**, el coeficiente de
fase $\varphi(\nu)$ está ligado a $\gamma(\nu)$ por la **transformada de Hilbert** (§B.1 del
Apéndice B): conocer $\gamma(\nu)$ a todas las frecuencias determina $\varphi(\nu)$.

De $I(z) = |E(z)|^2/2\eta$ y (14.1-6), la amplitud compleja cumple

$$E(z) = E(0)\exp\!\left[\tfrac12\gamma(\nu)z\right]\exp[-j\varphi(\nu)z], \qquad (14.1\text{-}10)$$

$$E(z+\Delta z) \approx E(z)\left[1 + \tfrac12\gamma(\nu)\Delta z - j\varphi(\nu)\Delta z\right], \qquad (14.1\text{-}11)$$

$$\frac{\Delta E(z)}{\Delta z} = E(z)\left[\tfrac12\gamma(\nu) - j\varphi(\nu)\right], \qquad (14.1\text{-}12)$$

de modo que el amplificador incremental es un sistema lineal con entrada $E(z)$, salida
$\Delta E(z)/\Delta z$ y función de transferencia

$$H(\nu) = \tfrac12\gamma(\nu) - j\varphi(\nu). \qquad (14.1\text{-}13)$$

Por causalidad, partes real e imaginaria de $H(\nu)$ se relacionan por Hilbert:
$-\varphi(\nu)$ es la transformada de Hilbert de $\tfrac12\gamma(\nu)$ (p. 538).

Para línea lorentziana estrecha ($\Delta\nu \ll \nu_0$), con (14.1-9) y (B.1-13):

$$\boxed{\varphi(\nu) = \frac{\nu-\nu_0}{\Delta\nu}\,\gamma(\nu)} \qquad (14.1\text{-}14)\ \text{Phase-Shift Coefficient (Lorentzian Lineshape), p. 538}$$

**Fig. 14.1-3** (p. 539): $\gamma(\nu)$ y $\varphi(\nu)$ lorentzianos. En resonancia la
ganancia es máxima y el corrimiento de fase es cero; $\varphi<0$ por debajo de $\nu_0$ y
$\varphi>0$ por encima (forma dispersiva, antisimétrica).

---

### 14.2 Amplifier Pumping (p. 539)

El bombeo aporta la potencia que aumenta la señal: excita electrones a niveles superiores
para lograr $N = N_2 - N_1 > 0$ en la transición de interés. Suele usar **niveles
auxiliares** (p. ej. bombear 1→3 y dejar que el decaimiento 3→2 pueble el nivel 2). Bombeo
óptico (flashlamp, láser), eléctrico (descarga en gas, haz de electrones/iones, inyección de
portadores) o químico. En operación **CW** (onda continua) las tasas de excitación y
decaimiento se equilibran para mantener una inversión estacionaria.

#### 14.2A Rate Equations (p. 539)

**Ecuaciones de tasa**: describen $dN_1/dt$ y $dN_2/dt$ por bombeo y transiciones
radiativas/no radiativas; parecidas a las de §13.4 pero con bombeo selectivo (ya no hay
equilibrio térmico).

Tiempos de vida (Fig. 14.2-1, p. 540): el nivel 2 decae a 1 con $\tau_{21}$ y a todos los
demás niveles con $\tau_{20}$; el nivel 1 tiene vida $\tau_1$. Las tasas se suman:

$$\tau_2^{-1} = \tau_{21}^{-1} + \tau_{20}^{-1}, \qquad (14.2\text{-}1)$$

$$\tau_{21}^{-1} = t_{sp}^{-1} + \tau_{nr}^{-1}, \qquad (14.2\text{-}2)$$

con $t_{sp}$ la componente radiativa (emisión espontánea) y $\tau_{nr}$ la no radiativa (p.
ej. colisiones con la pared). Sin bombeo, en estado estacionario $N_1, N_2 \to 0$.

Con bombeo (Figs. 14.2-2 y 14.2-3, p. 541): átomos llevados **fuera** del nivel 1 a tasa
$R_1$ y **hacia** el nivel 2 a tasa $R_2$ (por unidad de volumen y tiempo).

**Ecuaciones de tasa sin radiación amplificadora** (p. 540):

$$\frac{dN_2}{dt} = R_2 - \frac{N_2}{\tau_2}, \qquad (14.2\text{-}3)$$

$$\frac{dN_1}{dt} = -R_1 - \frac{N_1}{\tau_1} + \frac{N_2}{\tau_{21}}. \qquad (14.2\text{-}4)$$

Estado estacionario ($dN_1/dt = dN_2/dt = 0$):

$$\boxed{N_0 = R_2\tau_2\left(1 - \frac{\tau_1}{\tau_{21}}\right) + R_1\tau_1} \qquad (14.2\text{-}5)\ \text{Steady-State Population Difference (Absence of Amplifier Radiation), p. 541}$$

$N_0$ = diferencia de población estacionaria **sin** radiación amplificadora. Para $N_0$
grande (p. 541): $R_1$, $R_2$ grandes; $\tau_2$ largo (pero $t_{sp}$ corto para tasa
radiativa alta); $\tau_1$ corto, con $\tau_1 < (\tau_2/\tau_{21})R_2$ [así lo imprime el
libro]. Física: el nivel superior se bombea fuerte y decae lento (retiene población); el
inferior se vacía rápido. Ideal: $\tau_{21}\approx t_{sp} \ll \tau_{20}$ (⇒ $\tau_2\approx
t_{sp}$) y $\tau_1 \ll t_{sp}$, con lo que

$$N_0 \approx R_2 t_{sp} + R_1\tau_1, \qquad (14.2\text{-}6)$$

y sin despoblamiento ($R_1 = 0$) o si $R_1 \ll (t_{sp}/\tau_1)R_2$:

$$N_0 \approx R_2 t_{sp}. \qquad (14.2\text{-}7)$$

**EJERCICIO 14.2-1 — Bombeo óptico** (pp. 541–542): con $R_1 = 0$ y $R_2$ logrado
excitando átomos desde el estado base $E=0$ al nivel 2 con fotones de frecuencia $E_2/h$ y
probabilidad de transición $W$; $\tau_2\approx t_{sp}$, $\tau_1 \ll t_{sp}$ (⇒ $N_1\approx 0$,
$N_0\approx R_2 t_{sp}$). Si $N_a$ es la población total de los niveles 0, 1 y 2, mostrar que
$R_2 \approx (N_a - 2N_0)W$ y por tanto $N_0 \approx N_a t_{sp}W/(1+2t_{sp}W)$.

**Ecuaciones de tasa con radiación amplificadora** (p. 542): la radiación cerca de $\nu_0$
induce emisión estimulada y absorción con probabilidad $W_i = \phi\sigma(\nu)$ (Fig. 14.2-4):

$$\frac{dN_2}{dt} = R_2 - \frac{N_2}{\tau_2} - N_2 W_i + N_1 W_i, \qquad (14.2\text{-}8)$$

$$\frac{dN_1}{dt} = -R_1 - \frac{N_1}{\tau_1} + \frac{N_2}{\tau_{21}} + N_2 W_i - N_1 W_i. \qquad (14.2\text{-}9)$$

(La emisión espontánea está incluida en $\tau_{21}$.) En estado estacionario:

$$\boxed{N = \frac{N_0}{1 + \tau_s W_i}} \qquad (14.2\text{-}10)\ \text{Steady-State Population Difference (Presence of Amplifier Radiation), p. 542}$$

$$\boxed{\tau_s = \tau_2 + \tau_1\left(1 - \frac{\tau_2}{\tau_{21}}\right)} \qquad (14.2\text{-}11)\ \text{Saturation Time Constant, p. 542}$$

$\tau_s$ es siempre positivo (porque $\tau_2 \le \tau_{21}$). Si $W_i = 0$, $N = N_0$.
Con radiación, $|N| \le |N_0|$ siempre. Si $\tau_s W_i \ll 1$ (**aproximación de señal
pequeña**), $N\approx N_0$. Al crecer $W_i$, $N\to 0$ sea cual sea el signo de $N_0$ (emisión
estimulada y absorción dominan con igual probabilidad): la radiación, por intensa que sea,
**no** puede invertir el signo de $N$. $\tau_s$ actúa como **constante de tiempo de
saturación** (Fig. 14.2-5, p. 543: $N = N_0/2$ cuando $W_i = 1/\tau_s$).

**EJERCICIO 14.2-2 — Constante de tiempo de saturación** (p. 543): mostrar que si
$t_{sp} \ll \tau_{nr}$, $t_{sp} \ll \tau_{20}$ y $t_{sp} \gg \tau_1$, entonces
$\tau_s \approx t_{sp}$.

#### 14.2B Pumping Schemes (p. 543)

**Bombeo de cuatro niveles** (pp. 543–545, Fig. 14.2-6 p. 544): nivel 0 = base, nivel 1 por
encima del base con $E_1 \gg kT$ (casi vacío térmicamente), nivel 3 (o banda) por encima de
2. El bombeo lleva átomos 0→3 a tasa $R$; 3→2 decae rápido (sin acumulación en 3); el nivel 2
es de **vida larga** (acumula), el 1 de **vida corta** (se vacía). Con decaimiento 3→2
instantáneo, bombear a 3 equivale a bombear a 2 con $R_2 = R$; además $R_1 = 0$. Entonces
de (14.2-5):

$$N_0 = R\tau_2\left(1 - \frac{\tau_1}{\tau_{21}}\right). \qquad (14.2\text{-}12)$$

En la mayoría de sistemas de 4 niveles $t_{sp}\ll\tau_{nr}$ y $\tau_{20}\gg t_{sp}\gg\tau_1$:

$$N_0 \approx R t_{sp}, \qquad (14.2\text{-}13)$$
$$\tau_s \approx t_{sp}, \qquad (14.2\text{-}14)$$
$$N \approx \frac{R t_{sp}}{1 + t_{sp}W_i}. \qquad (14.2\text{-}15)$$

**Dependencia de $R$ con $N$** (pp. 544–545): la tasa de bombeo no es independiente de $N$.
Con $N_g + N_1 + N_2 + N_3 = N_a$ (14.2-16) y bombeo 0→3 con probabilidad $W$,
$R = (N_g - N_3)W$. Si 1 y 3 son de vida corta, $N_1\approx N_3\approx 0$, $N_g \approx N_a - N$:

$$R \approx (N_a - N)W, \qquad (14.2\text{-}17)$$

(decrece linealmente con $N$: la inversión reduce los átomos disponibles para bombear).
Sustituyendo en (14.2-15):

$$N \approx \frac{t_{sp}N_a W}{1 + t_{sp}W + t_{sp}W_i}, \qquad (14.2\text{-}18)$$

que se escribe en la forma genérica $N = N_0/(1+\tau_s W_i)$ (14.2-19) con

$$\boxed{N_0 \approx \frac{t_{sp}N_a W}{1 + t_{sp}W}} \qquad (14.2\text{-}20)$$

$$\boxed{\tau_s \approx \frac{t_{sp}}{1 + t_{sp}W}} \qquad (14.2\text{-}21)$$

Para bombeo débil ($W \ll 1/t_{sp}$): $N_0\approx t_{sp}N_a W \propto W$ y
$\tau_s\approx t_{sp}$. Al aumentar el bombeo $N_0$ **satura** (→ $N_a$) y $\tau_s$ decrece.

**Bombeo de tres niveles** (pp. 545–547, Fig. 14.2-7 p. 546): el **estado base** ($E_1=0$)
es el nivel láser inferior. Bombeo 1→3 a tasa $R$; decaimiento 3→2 rápido ($\tau_{32}\ll
\tau_{31}$) ⇒ $R_2 = R$; población térmica de 2 despreciable. Es un caso especial de
Fig. 14.2-4 con

$$R_1 = R_2 = R, \qquad \tau_1 = \infty, \qquad \tau_2 = \tau_{21}. \qquad (14.2\text{-}22)$$

Para evitar $\tau_1=\infty$ se vuelve a (14.2-8)–(14.2-9); en estado estacionario ambas dan

$$0 = R - \frac{N_2}{\tau_{21}} - N_2 W_i + N_1 W_i, \qquad (14.2\text{-}23)$$

y con la condición auxiliar (nivel 3 vacío)

$$N_1 + N_2 = N_a, \qquad (14.2\text{-}24)$$

se obtiene $N = N_0/(1+\tau_s W_i)$ con

$$N_0 = 2R\tau_{21} - N_a, \qquad (14.2\text{-}25)$$
$$\tau_s = 2\tau_{21}, \qquad (14.2\text{-}26)$$

y si $t_{sp}\ll\tau_{nr}$:

$$N_0 \approx 2Rt_{sp} - N_a, \qquad (14.2\text{-}27)$$
$$\tau_s \approx 2t_{sp}. \qquad (14.2\text{-}28)$$

**Comparación 3 vs 4 niveles** (p. 546): en 3 niveles, lograr $N_0>0$ exige $R > N_a/2t_{sp}$;
solo para llegar a $N_0 = 0$ ($N_2 = N_1$) se necesita una densidad de potencia de bombeo
$E_3 N_a/2t_{sp}$. La gran población del estado base es el obstáculo inherente, evitado en
4 niveles (nivel 1 vacío porque $\tau_1$ corto). $\tau_s\approx t_{sp}$ en 4 niveles es la
**mitad** que en 3 niveles. (Prob. 14.2-4: no se logra inversión estacionaria bombeando
ópticamente de forma directa entre 1 y 2.)

Con $R = (N_1 - N_3)W \approx \tfrac12(N_a - N)W$ (pues $N_3\approx 0$, $N_1 = \tfrac12(N_a-N)$):

$$N = \frac{N_0}{1+\tau_s W_i}, \qquad (14.2\text{-}29)$$

$$\boxed{N_0 = \frac{N_a(t_{sp}W - 1)}{1 + t_{sp}W}} \qquad (14.2\text{-}30)\ \text{(p. 547)}$$

$$\boxed{\tau_s = \frac{2t_{sp}}{1 + t_{sp}W}} \qquad (14.2\text{-}31)\ \text{(p. 547)}$$

$N_0$ y $\tau_s$ saturan al crecer $W$, como en 4 niveles.

**EJERCICIO 14.2-3 — Potencia de bombeo en sistemas de 3 y 4 niveles** (p. 547):
(a) Determinar la probabilidad de bombeo $W$ necesaria para $N_0 = 0$ en 3 y en 4 niveles.
[De (14.2-30): $W = 1/t_{sp}$ en 3 niveles; en 4 niveles $N_0 = 0$ con $W = 0$.]
(b) Con $W = 2/t_{sp}$ (3 niveles) y $W = 1/2t_{sp}$ (4 niveles), mostrar que $N_0 = N_a/3$
en ambos; comparar las potencias de bombeo necesarias.

**Métodos de bombeo** (p. 547, Fig. 14.2-8 p. 548): eléctrico, óptico, químico (§13.5A),
nuclear (partículas/rayos γ). Fig. 14.2-8: (a) descarga DC longitudinal o transversal en gas;
(b) descarga RF; (c) flashlamp helicoidal de Xe alrededor de una barra (rubí, tierras raras);
(d) diodo láser acoplado a fibra Er³⁺:sílice; (e) arreglo de diodos láser bombeando una barra
Nd³⁺:YVO₄. Importante: $R_1$, $R_2$ cuentan los átomos **efectivamente** bombeados; el proceso
puede ser muy ineficiente (muchos fotones de bombeo se pierden).

---

### 14.3 Common Laser Amplifiers (p. 547)

Los sistemas reales tienen muchos niveles interactuantes, pero los principios se codifican
con los esquemas de 3 y 4 niveles. Se ilustran tres: rubí (3 niveles), vidrio:Nd³⁺ (4 niveles)
y fibra de sílice:Er³⁺ (3 niveles), más el amplificador Raman (dispersión Raman estimulada).
Todos operan también como osciladores láser (§15.3A). Usos (p. 548): **amplificadores de
potencia** (aumentar la potencia de un oscilador de alta calidad y baja potencia),
**amplificadores en línea** (repetidores ópticos) y **preamplificadores ópticos** (antes de la
fotodetección, §24.1C). Los amplificadores ópticos de semiconductor van en §17.2. A menudo
operan en régimen de saturación (§14.4).

#### 14.3A Ruby (p. 548)

Rubí = Cr³⁺:Al₂O₃ (zafiro con una pequeña fracción de Al sustituido por Cr³⁺, §13.1C). Primer
material en que se observó acción láser (Maiman, 1960; p. 567 del cap. 15); hoy es sobre todo
didáctico. **Sistema de tres niveles** (Fig. 14.3-1, p. 549): nivel 1 = base $^4A_2$; nivel 2
= par de niveles discretos cercanos ($^2E$), el inferior $R_1$ da la transición roja
$\lambda_o = 694.3$ nm; nivel 3 = dos bandas anchas de absorción centradas en 550 nm (verde,
$^4F_2$) y 400 nm (violeta, $^4F_1$) — responsables del color rojizo del rubí.
Bombeo óptico 1→3 con flashlamp helicoidal o lineal en cilindro reflector de sección elíptica
(Fig. 14.3-2, p. 549; Fig. 1.2-3). Decaimiento 3→2 rápido ($\tau_{32}\sim$ ps); nivel 2 de
vida larga ($t_{sp}\approx 3$ ms); decaimiento no radiativo despreciable
($\tau_{21}\approx t_{sp}$). Línea **homogénea** $\Delta\nu\approx 330$ GHz por colisiones
elásticas con fonones de red. Parámetros en Tablas 14.3-1 y 15.3-1.

#### 14.3B Neodymium-Doped Glass (p. 549)

Nd³⁺:vidrio: se fabrica en tamaños muy grandes ⇒ pulsos extremadamente potentes, aunque a
bajo ciclo de trabajo (baja conductividad térmica del vidrio). Alta calidad óptica, isótropo,
dopaje homogéneo. **Sistema de cuatro niveles** (Fig. 14.3-3, p. 550): transición
$^4F_{3/2}\to{}^4I_{11/2}$ a $\lambda_o = 1.053\ \mu$m en vidrio fosfato (Schott LG-770, el
del NIF). Nivel 1 a 0.24 eV sobre el base ($\gg kT\approx 0.026$ eV a temperatura ambiente
⇒ población térmica despreciable). Nivel 3 = cuatro bandas de absorción de ~30 nm centradas
en 805, 745, 585 y 520 nm (color púrpura). $\tau_{32}$ muy corto; $t_{sp} = 375\ \mu$s;
$\tau_1\approx 300$ ps. Transición 2→1 **inhomogénea** (vidrio amorfo: cada ion ve un entorno
distinto) con $\Delta\nu\approx 7$ THz a temperatura ambiente. La ganancia es sustancialmente
mayor que la del rubí por su carácter de 4 niveles. Fig. 14.3-3 (izq.) muestra también el
espectro del flashlamp de Xe.

**EJEMPLO 14.3-1 — Amplificadores de vidrio:Nd en el National Ignition Facility (NIF)**
(pp. 550–551): NIF (LLNL, Livermore) y Laser MegaJoule (LMJ, Francia) para fusión por
confinamiento inercial. Diseño: 4 *clusters* × 6 *bundles* × 8 placas de vidrio láser
apiladas en una cavidad bombeada por flashlamps (Fig. 14.3-4, p. 551): placas de vidrio
fosfato con ≈ 2 mol % Nd (Schott LG-770 o Hoya LHG-8), 46 cm × 81 cm × 4 cm, montadas en
**ángulo de Brewster** (minimiza reflexión de Fresnel y mejora el acoplamiento del bombeo);
haces cuadrados para empaquetado compacto; bundle de ≈ 2 m de alto; 192 líneas de haz; cada
línea con 16 etapas ⇒ 3072 placas en total. Pulsos de **1.8 MJ en 3.5 ns** (pico 500 TW);
máximo 5 disparos por 24 h (enfriamiento). Semilla: láser de fibra dopada con Yb³⁺ (§15.3A).
La salida se **triplica en frecuencia a 351 nm** (UV): SHG a 526 nm en KDP + SFG
(fundamental + segundo armónico) en DKDP (cap. 21); luego se enfoca a puntos de mm sobre un
blanco de deuterio–tritio. El edificio es del tamaño de un estadio.

#### 14.3C Erbium-Doped Silica Fiber (p. 551)

**Amplificadores de fibra óptica (OFA)**: ventajas de la óptica guiada monomodo (cap. 9).
**Amplificadores de fibra dopada con tierras raras (REFA)**: señal y bombeo se introducen en
la fibra dopada; la señal se amplifica por emisión estimulada en los iones bombeados.
Dopantes: Er³⁺, Pr³⁺, Tm³⁺, Nd³⁺, Yb³⁺, Ho³⁺; operan principalmente en el IR cercano, pero
todos excepto Er³⁺ solo funcionan eficientemente en la banda de telecomunicaciones usual en
vidrios huéspedes distintos de sílice.

**EDFA** (Er³⁺:sílice, pp. 551–553): muy usado en comunicaciones por fibra, a menudo en
concatenación (cap. 24). Ganancia **independiente de la polarización**, baja pérdida de
inserción, transición ancha cerca de $\lambda = 1550$ nm (mínimo de pérdida de la fibra de
sílice, Fig. 9.3-2).

- **Bombeo** (p. 552): longitudinal con diodos láser InGaAs de pozo cuántico tensionado a
  $\lambda_o = 980$ nm. Configuraciones (Fig. 14.3-5, p. 552): (a) **copropagante**
  (*forward*), (b) **contrapropagante** (*backward*), (c) **bidireccional** — la preferida:
  distribución de potencia de bombeo más uniforme a lo largo de la fibra, mayor eficiencia y
  menor ruido. Las **fibras de doble revestimiento** (*double-clad*) evitan efectos no
  lineales en el núcleo cuando el bombeo es alto (osciladores de fibra, Fig. 15.3-5).
  Codopantes Yb o Tm: extienden la longitud de onda, permiten más potencia (transferencia de
  energía) y evitan el *clustering* de Er.
- **Niveles** (Fig. 14.3-6, p. 553): transición $^4I_{13/2}\to{}^4I_{15/2}$ a ~1550 nm;
  bombeo a $^4I_{11/2}$ (980 nm), decaimiento rápido 3→2. Se comporta como **3 niveles a
  $T = 300$ K** y como 4 niveles enfriado a $T = 77$ K. Er³⁺ es lantánido: el huésped influye
  poco en los niveles. Ensanchamiento **mixto**: homogéneo (fonones) + inhomogéneo (variación
  local del campo en el vidrio) ⇒ perfil de ganancia dependiente de λ que requiere
  **ecualización de ganancia** en algunas aplicaciones. Características favorables: larga
  vida espontánea del estado excitado, ausencia de niveles intermedios entre base y excitado,
  ausencia de absorción de estado excitado. También puede hacerse de 4 niveles en la
  transición $^4I_{11/2}\to{}^4I_{13/2}$ cerca de 2.9 µm.
- **Cifras** (p. 552): ganancias > 50 dB con decenas de mW de bombeo. Ejemplo: ≈ 30 dB con
  ≈ 5 mW a 980 nm en ≈ 50 m de fibra con ≈ 300 ppm de Er₂O₃. Mejores eficiencias de ganancia
  ≈ 10 dB/mW. Potencias de salida > 100 W (la salida crece en proporción al bombeo). Ancho de
  banda $\Delta\lambda\approx 40$ nm ↔ $\Delta\nu\approx 5.3$ THz: cubre la **banda C**
  (1530–1565 nm, §24.1A); la **banda L** (1565–1625 nm) también se acomoda con otros
  parámetros de optimización. El gran producto ganancia–ancho de banda los hace idóneos para
  **WDM** (§24.3). Con realimentación se convierte en oscilador (§15.3A).
- **Bombeo a 1.48 µm** (p. 553): directamente en la transición $^4I_{13/2}\to{}^4I_{15/2}$
  con diodos InGaAsP (esquema **cuasi-dos-niveles**): menos eficiente que a 980 nm (menor
  ganancia por unidad de bombeo, más ruido), pero mayor ancho de línea de bombeo y mayor
  potencia de saturación de señal ⇒ se usa en amplificadores de alta potencia; a veces se
  bombea a ambas longitudes de onda.
- Otros REFA (p. 553): Tm³⁺ en fluoruro o silicato multicomponente para la **banda S**
  (1460–1530 nm); Pr³⁺ en 1300 nm; Yb³⁺:sílice en 1050–1120 nm. Otras clases de OFA: Raman
  (§14.3D) y amplificadores ópticos de semiconductor (SOA, §17.2); comparación en §17.2D y
  §24.1C.

**Recuadro — Summary (p. 553).** El EDFA se usa ampliamente por: alta ganancia, alta
potencia de salida, ancho de banda amplio, insensibilidad a la polarización, alta
eficiencia, baja pérdida de inserción, bajo ruido.

#### 14.3D Raman Fiber Amplifiers (p. 553)

Los OFA también pueden basarse en principios distintos de la emisión estimulada: el
**amplificador de fibra Raman (RFA)** se basa en la **dispersión Raman estimulada (SRS)**
(§13.5C, p. 554): un fotón de bombeo $h\nu_p$ junto con un fotón de señal de menor energía
$h\nu_s$ entra en un medio no lineal (fibra); el fotón de señal estimula la emisión de un
fotón clon obtenido al desplazar (Stokes) el fotón de bombeo en $h\nu_R$, de modo que su
energía coincide exactamente con la del fotón de señal; el exceso de energía se transfiere a
los **modos vibracionales** del vidrio (línea discontinua en el inset de Fig. 14.3-7 = estado
virtual). Es análogo a la emisión estimulada en un EDFA, pero el **ancho de banda lo fija el
espectro vibracional del vidrio huésped**, no el ancho de línea del dopante. La intensidad
del efecto está en el **coeficiente de ganancia Raman $\gamma_R$**, que depende de las
propiedades no lineales de la fibra y es **proporcional a la intensidad de bombeo**
$I_p = P/A$ ($P$ potencia de bombeo, $A$ área de interacción) [ver (21.3-15)].

**Fig. 14.3-7** (p. 554): coeficiente de ganancia Raman relativo vs. corrimiento Stokes
$\nu_R$ (THz) en sílice dopada con germanio: pico a ≈ 13 THz por debajo del bombeo, ancho
$\Delta\nu\approx 12.5$ THz; sílice, germanio, fósforo y borato tienen espectros SRS muy
distintos (curva adaptada de Stolen, Lee y Jain, *JOSA B* 1, 652–657, 1984).

- **Distribuido vs. concentrado** (p. 554): en el **RFA distribuido** señal y bombeo viajan
  por la propia fibra de transmisión (que es el medio de ganancia); en el **RFA concentrado**
  (*lumped*) se usa un tramo corto de fibra muy no lineal dedicada, con núcleo pequeño para
  aumentar $I_p$ y acortar la longitud necesaria (que puede ser considerable). Bombeo
  co-, contra- o bidireccional (Fig. 14.3-5); se prefiere **contrapropagante** porque reduce el
  ruido transferido del bombeo a la señal.
- **Ancho de banda** (p. 554): mucho mayor que el EDFA. En sílice:Ge el pico está ≈ 13 THz
  (≈ 100 nm a $\lambda_o = 1550$ nm) por debajo del bombeo; fibras de fosfosilicato tienen
  corrimientos Stokes mucho mayores (Ejemplo 15.3-1). Bombeo con diodos láser con diversidad
  de polarización, láseres de fibra o láseres Raman de fibra ≈ 100 nm por debajo de la λ a
  amplificar. Ancho de ganancia sustancial ≈ 12.5 THz ≈ 100 nm a 1550 nm; **combinando
  bombeos a distintas frecuencias** se amplía mucho más (el corrimiento Stokes está ligado a
  la λ del bombeo): en principio toda la región de transparencia de la fibra (p. 555).
- **Ganancia y eficiencia** (p. 555): ganancias cercanas a 20 dB; eficiencia de ganancia en
  sílice:Ge ≈ 0.02 dB/mW (vs ≈ 10 dB/mW del EDFA) ⇒ bombeos de cientos de mW en distribuidos
  y > 1 W en concentrados (donde no hay problemas de seguridad). A diferencia del EDFA, se
  requiere **bombeo con diversidad de polarización** (la ganancia Raman es máxima cuando
  señal y bombeo tienen la misma polarización). La eficiencia mejora con **fibra
  compensadora de dispersión**; a veces se usan junto con EDFA. Con compensación de dispersión
  y arreglos de diodos de alta potencia, los RFA son competitivos conforme el ancho de banda
  requerido crece hacia decenas de THz.

**Recuadro — Summary (p. 555).** Ventajas del RFA sobre el EDFA: mayor ancho de banda;
ancho de banda extensible con múltiples bombeos; operación en un amplio rango de λ;
huésped de fibra arbitrario; compatible con enlaces existentes. Desventajas: menor
ganancia; mayor potencia de bombeo y menor eficiencia; mayores longitudes de fibra;
sensibilidad a la polarización de la señal.

#### 14.3E Tabulation of Selected Laser Transitions (p. 555)

Los más usados son los de §14.3B y C, pero hay amplificación láser en gases, colorantes,
sistemas de electrones libres y semiconductores. La **Tabla 14.3-1** (p. 556; transcrita más
abajo) da $\lambda_o$, $\sigma_0$, $t_{sp}$, $\Delta\nu$ y $n$ de transiciones
representativas del visible e IR (el principio máser va del microondas a rayos X). $\sigma_0$,
$t_{sp}$ y $\Delta\nu$ varían en rangos enormes.

---

### 14.4 Amplifier Nonlinearity (p. 556)

#### 14.4A Saturated Gain in Homogeneously Broadened Media (p. 556)

**Coeficiente de ganancia saturado.** Cadena de dependencias: $\gamma(\nu)$ depende de $N$
(14.1-4); $N$ depende del bombeo y de $W_i$ (14.2-10); $W_i$ depende de $\phi$ (14.1-1) ⇒
$\gamma$ depende de la **propia densidad de flujo de fotones que amplifica**: origen de la
**saturación de ganancia** y la no linealidad. Sustituyendo (14.1-1) en (14.2-10):

$$N = \frac{N_0}{1 + \phi/\phi_s(\nu)}, \qquad (14.4\text{-}1)$$

$$\boxed{\frac{1}{\phi_s(\nu)} = \tau_s\sigma(\nu) = \frac{\lambda^2}{8\pi}\frac{\tau_s}{t_{sp}}\,g(\nu)} \qquad (14.4\text{-}2)\ \text{Saturation Photon-Flux Density, p. 556}$$

Sustituyendo (14.4-1) en (14.1-4):

$$\boxed{\gamma(\nu) = \frac{\gamma_0(\nu)}{1 + \phi/\phi_s(\nu)}} \qquad (14.4\text{-}3)\ \text{Saturated Gain Coefficient, p. 557}$$

$$\boxed{\gamma_0(\nu) = N_0\sigma(\nu) = N_0\frac{\lambda^2}{8\pi t_{sp}}\,g(\nu)} \qquad (14.4\text{-}4)\ \text{Small-Signal Gain Coefficient, p. 557}$$

$\gamma$ decrece con $\phi$ (Fig. 14.4-1, p. 557). $\phi_s(\nu) = 1/\tau_s\sigma(\nu)$ es la
**densidad de flujo de fotones de saturación**: aquella para la cual $\gamma$ cae a la mitad.
Si $\tau_s\approx t_{sp}$: aproximadamente un fotón puede emitirse por cada tiempo de vida
espontáneo en cada área de sección eficaz [$\sigma(\nu)\phi_s(\nu)t_{sp} = 1$]. La
**intensidad de saturación** correspondiente es $I_s = h\nu\,\phi_s$.

**EJERCICIO 14.4-1 — Densidad de flujo de saturación del rubí** (p. 557): determinar
$\phi_s$ y la intensidad de saturación para la transición de rubí a $\lambda_o = 694.3$ nm en
$\nu = \nu_0$, con los parámetros de la Tabla 14.3-1 y $\tau_s\approx 2t_{sp}$ (14.2-28).
[Orientación: $\phi_s(\nu_0) = 1/(2t_{sp}\sigma_0)$ con $\sigma_0 = 2\times10^{-20}$ cm²,
$t_{sp} = 3$ ms ⇒ $\phi_s \approx 8.3\times10^{21}$ fotones/cm²·s; $I_s = h\nu\phi_s$ con
$h\nu = 2.86\times10^{-19}$ J ⇒ $I_s\approx 2.4$ kW/cm². Cálculo propio, no del libro.]

**EJERCICIO 14.4-2 — Ensanchamiento espectral de un amplificador saturado** (p. 557):
medio homogéneo con línea lorentziana de ancho $\Delta\nu$ (14.1-8). Mostrar que para una
densidad de flujo $\phi$ el coeficiente de ganancia $\gamma(\nu)$ sigue siendo lorentziano
con ancho

$$\boxed{\Delta\nu_s = \Delta\nu\sqrt{1 + \frac{\phi}{\phi_s(\nu_0)}}} \qquad (14.4\text{-}5)\ \text{Linewidth of Saturated Amplifier, p. 557}$$

⇒ la saturación de ganancia viene acompañada de un **aumento del ancho de banda** (menor
selectividad en frecuencia; Fig. 14.4-2, p. 558, para $\phi = 2\phi_s(\nu_0)$).

**Ganancia saturada de un amplificador de longitud $d$** (pp. 558–559, Fig. 14.4-3(a)). Se
suprime la dependencia en $\nu$ ($\gamma$, $\phi_s$). Con $d\phi = \gamma\phi\,dz$ y (14.4-3):

$$\frac{d\phi}{dz} = \frac{\gamma_0\phi}{1 + \phi/\phi_s}. \qquad (14.4\text{-}6)$$

Reescribiendo $(1/\phi + 1/\phi_s)\,d\phi = \gamma_0\,dz$ e integrando:

$$\ln\frac{\phi(z)}{\phi(0)} + \frac{\phi(z) - \phi(0)}{\phi_s} = \gamma_0 z. \qquad (14.4\text{-}7)$$

Entre entrada y salida, con $X = \phi(0)/\phi_s$ e $Y = \phi(d)/\phi_s$ (flujos normalizados):

$$[\ln(Y) + Y] = [\ln(X) + X] + \gamma_0 d. \qquad (14.4\text{-}8)$$

Casos límite de la ganancia $G = \phi(d)/\phi(0) = Y/X$:

1. $X, Y \ll 1$ (flujos ≪ saturación): $\ln Y\approx\ln X + \gamma_0 d$ ⇒

   $$Y \approx X\exp(\gamma_0 d), \qquad (14.4\text{-}9)$$

   relación lineal, $G\approx\exp(\gamma_0 d)$ (coincide con (14.1-7), $\gamma\approx\gamma_0$).

2. $X \gg 1$: se desprecian los logaritmos ⇒

   $$Y \approx X + \gamma_0 d, \qquad (14.4\text{-}10)$$

   $$\phi(d) \approx \phi(0) + \gamma_0\phi_s d \approx \phi(0) + \frac{N_0 d}{\tau_s}. \qquad (14.4\text{-}11)$$

   Muy saturado: los átomos están "ocupados" emitiendo un flujo constante $N_0 d/\tau_s$;
   los fotones de entrada simplemente atraviesan, más una contribución constante
   independiente de la entrada.

Para valores intermedios (14.4-8) se resuelve numéricamente (Fig. 14.4-3(b), p. 559: curva
sólida entre las asíntotas $Y = X e^{\gamma_0 d}$ e $Y = X + \gamma_0 d$). **Fig. 14.4-3(c)**:
$G = Y/X$ vs $X$ para $\gamma_0 d = 2$: máximo $\exp(\gamma_0 d)\approx 7.4$ para $X\ll 1$,
decrece hacia 1 cuando $X\to\infty$.

**Absorbedores saturables** (pp. 559–560): si $\gamma_0 < 0$ ($N_0<0$, población normal), el
medio atenúa y el coeficiente de atenuación $\alpha(\nu) = -\gamma(\nu)$ también satura:

$$\alpha(\nu) = \frac{\alpha_0(\nu)}{1 + \phi/\phi_s(\nu)},$$

menos absorción a flujos altos ⇒ **absorbedor saturable**. La relación $\phi(d)$ vs
$\phi(0)$ sigue (14.4-8) con $\gamma_0<0$. La transmitancia $Y/X = \phi(d)/\phi(0)$ crece con
$\phi(0)$ y tiende a 1 (Fig. 14.4-4, p. 560, para $\gamma_0 d = -2$: transmitancia parte de
$\exp(\gamma_0 d)\approx 0.135$ y sube hacia 1), porque $N\to 0$ y no hay absorción neta.

#### *14.4B Saturated Gain in Inhomogeneously Broadened Media (p. 560)

**Coeficiente de ganancia.** Medio inhomogéneo (§13.3D): colección de átomos con distintas
propiedades; el subconjunto $\beta$ tiene línea homogénea $g_\beta(\nu)$ y la forma de línea
promedio es $\bar g(\nu) = \langle g_\beta(\nu)\rangle$ ($\langle\cdot\rangle$ = promedio
sobre $\beta$). Coeficiente de ganancia de señal pequeña promedio:

$$\bar\gamma_0(\nu) = N_0\frac{\lambda^2}{8\pi t_{sp}}\,\bar g(\nu). \qquad (14.4\text{-}12)$$

El saturado es más sutil porque $\phi_s(\nu)\propto 1/g(\nu)$ depende del subconjunto.
Se define

$$\bar\gamma(\nu) = \langle\gamma_\beta(\nu)\rangle, \qquad (14.4\text{-}13)$$

$$\gamma_\beta(\nu) = \frac{\gamma_{0\beta}(\nu)}{1 + \phi/\phi_{s\beta}(\nu)} = b\,\frac{g_\beta(\nu)}{1 + \phi\,a^2 g_\beta(\nu)}, \qquad (14.4\text{-}14)$$

con $b = N_0(\lambda^2/8\pi t_{sp})$ y $a^2 = (\lambda^2/8\pi)(\tau_s/t_{sp})$. El promedio
de un cociente no es el cociente de los promedios (p. 560).

**Medio ensanchado por Doppler** (p. 561): todos los átomos comparten la misma forma
$g(\nu)$ pero el centro del subconjunto $\beta$ está desplazado $\nu_\beta\propto$ velocidad
$v_\beta$. Con $g(\nu)$ lorentziana (14.1-8) y $g_\beta(\nu) = g(\nu - \nu_\beta)$:

$$\gamma_\beta(\nu) = \frac{b\,(\Delta\nu/2\pi)}{(\nu - \nu_\beta - \nu_0)^2 + (\Delta\nu_s/2)^2}, \qquad (14.4\text{-}15)$$

$$\Delta\nu_s = \Delta\nu\sqrt{1 + \frac{\phi}{\phi_s(\nu_0)}}, \qquad (14.4\text{-}16)$$

$$\phi_s^{-1}(\nu_0) = \frac{2a^2}{\pi\Delta\nu} = \frac{\lambda^2}{8\pi}\frac{\tau_s}{t_{sp}}\frac{2}{\pi\Delta\nu} = \frac{\lambda^2}{8\pi}\frac{\tau_s}{t_{sp}}\,g(\nu_0). \qquad (14.4\text{-}17)$$

(14.4-16) es la misma del Ejercicio 14.4-2: cada subconjunto de velocidad tiene ganancia
saturada lorentziana de ancho $\Delta\nu_s$ que crece con $\phi$. Los corrimientos $\nu_\beta$
siguen una gaussiana de media cero
$p(\nu_\beta) = (2\pi\sigma_D^2)^{-1/2}\exp(-\nu_\beta^2/2\sigma_D^2)$ (Ejercicio 13.3-2):

$$\bar\gamma(\nu) = \int_{-\infty}^{\infty}\gamma_\beta(\nu)\,p(\nu_\beta)\,d\nu_\beta. \qquad (14.4\text{-}18)$$

Si $p(\nu_\beta)$ es mucho más ancha que $\gamma_\beta(\nu)$ (Doppler ≫ $\Delta\nu_s$) se
saca $p$ de la integral; en $\nu = \nu_0$, $\nu_\beta = 0$:

$$\bar\gamma(\nu_0) = \frac{b\,p(0)}{\sqrt{1 + 2\phi a^2/\pi\Delta\nu}} = \frac{\bar\gamma_0}{\sqrt{1 + \phi/\phi_s(\nu_0)}}, \qquad (14.4\text{-}19)$$

$$\bar\gamma_0 = N_0\frac{\lambda^2}{8\pi t_{sp}}\frac{1}{\sqrt{2\pi\sigma_D^2}}. \qquad (14.4\text{-}20)$$

Resultado clave: en un medio inhomogéneo (Doppler) la ganancia en $\nu_0$ **satura con ley
de raíz cuadrada**, más lentamente que en el homogéneo (14.4-3). **Fig. 14.4-5** (p. 562):
$\bar\gamma(\nu_0)/\bar\gamma_0$ vs $\phi/\phi_s$, curvas homogénea e inhomogénea.

**Hole burning** (p. 562): un flujo grande de fotones monocromáticos a $\nu_1$ satura solo
los átomos cuya línea solapa $\nu_1$; los demás quedan sin saturar. Sondeando con una fuente
débil de frecuencia variable, el perfil de ganancia muestra un **agujero** centrado en
$\nu_1$ (Fig. 14.4-6, p. 562), de ancho $\Delta\nu_s$ (14.4-16): al crecer el flujo saturante
crecen la profundidad y el ancho del agujero.

---

### *14.5 Amplifier Noise (p. 562)

El medio resonante que amplifica también genera **emisión espontánea**, independiente de la
entrada: fuente fundamental de ruido. La señal amplificada tiene frecuencia, dirección y
polarización definidas; el ruido de **emisión espontánea amplificada (ASE)** es de banda
ancha, multidireccional y no polarizado ⇒ puede filtrarse parcialmente con un filtro óptico
estrecho, una apertura colectora y un polarizador (Fig. 14.5-1, p. 563).

Densidad de probabilidad (por segundo) de que un átomo en el nivel superior emita
espontáneamente un fotón entre $\nu$ y $\nu + d\nu$ (Ejercicio 13.3-1):

$$P_{sp}(\nu)\,d\nu = \frac{1}{t_{sp}}\,g(\nu)\,d\nu. \qquad (14.5\text{-}1)$$

Para cualquier frecuencia $P_{sp} = 1/t_{sp}$. Densidad media de fotones espontáneos
$N_2 P_{sp}(\nu)$; potencia espontánea por unidad de volumen y frecuencia
$h\nu N_2 P_{sp}(\nu)$, emitida uniformemente en todas direcciones y repartida por igual entre
dos polarizaciones. Recogiendo en ángulo sólido $d\Omega$ y una polarización se capta la
fracción $\tfrac12 d\Omega/4\pi$; con filtro de ancho $B$ centrado en $\nu$, el número de
fotones añadidos por emisión espontánea en un volumen de área unitaria y longitud $dz$ es
$\xi_{sp}(\nu)\,dz$:

$$\xi_{sp}(\nu) = N_2\frac{1}{t_{sp}}\,g(\nu)\,B\,\frac{d\Omega}{8\pi}, \qquad (14.5\text{-}2)$$

**densidad de flujo de fotones de ruido por unidad de longitud** (p. 563).

El ruido no se multiplica simplemente por la longitud: la emisión espontánea generada cerca de
la entrada **se amplifica** más que la generada cerca de la salida. Se incorpora en (14.1-3):

$$\frac{d\phi}{dz} = \gamma(\nu)\,\phi + \xi_{sp}(\nu), \qquad (14.5\text{-}3)$$

que incluye tanto la señal amplificada como el ruido ASE.

**EJERCICIO 14.5-1 — Emisión espontánea amplificada (ASE)** (pp. 563–564):
(a) Con (14.5-3), mostrar que sin señal de entrada y amplificador no saturado
[$\gamma(\nu)\approx\gamma_0(\nu)$] de longitud $d$, la emisión espontánea produce a la
salida $\phi(d) = \phi_{sp}\{\exp[\gamma_0(\nu)d] - 1\}$, con
$\phi_{sp} = \xi_{sp}(\nu)/\gamma_0(\nu)$.
(b) Como $\xi_{sp}(\nu)$ y $\gamma_0(\nu)$ son ∝ $g(\nu)$, $\phi_{sp}$ no depende de $g(\nu)$,
y la dependencia en frecuencia de $\phi(d)$ la gobierna $\{\exp[\gamma_0(\nu)d] - 1\}$. Si
$\gamma_0(\nu)$ es lorentziana de ancho $\Delta\nu$, mostrar que el ancho de ese factor es
**menor** que $\Delta\nu$: la amplificación de la emisión espontánea produce **estrechamiento
espectral** (p. 564).

**Estadística de fotones** (p. 564; §12.2C): la amplificación altera la estadística de
fotones. Señal coherente de entrada: Poisson, varianza $\sigma_s^2 = \bar n_s$. Fotones ASE:
Bose–Einstein, $\sigma_{ASE}^2 = \bar n_{ASE} + \bar n_{ASE}^2$ (mucho más ruidosos). A la
salida (señal + ASE) la ley es intermedia; con tiempo de conteo corto y luz linealmente
polarizada, se aproxima bien por la **distribución de fotones de polinomios de Laguerre**
(Prob. 14.5-3), de varianza

$$\sigma_n^2 = \bar n_s + \left(\bar n_{ASE} + \bar n_{ASE}^2\right) + 2\bar n_s\bar n_{ASE}. \qquad (14.5\text{-}4)$$

Contribuciones: señal, emisión espontánea y un **término cruzado** señal–ASE.

---

### Reading List (pp. 564–565)

Libros (ver también la lista del cap. 15): Headley & Agrawal (eds.), *Raman Amplification in
Fiber Optical Communication Systems*, Elsevier 2005; Islam (ed.), *Raman Amplifiers for
Telecommunications*, vols. 1 y 2, Springer 2004; Desurvire, Bayart, Desthieux & Bigo,
*Erbium-Doped Fiber Amplifiers: Device and System Developments*, Wiley 2002; Digonnet (ed.),
*Rare-Earth-Doped Fiber Lasers and Amplifiers*, Dekker 2.ª ed. 2001; Becker, Olsson & Simpson,
*Erbium-Doped Fiber Amplifiers: Fundamentals and Technology*, Academic 1999; Sudo et al.,
*Optical Fiber Amplifiers*, Artech 1997; Desurvire, *Erbium-Doped Fiber Amplifiers:
Principles and Applications*, Wiley 1994; Shimada & Ishio (eds.), *Optical Amplifiers and
Their Applications*, Wiley 1994; Bjarklev, *Optical Fiber Amplifiers*, Artech 1993.
Artículos: Bibeau, Rhodes & Atherton, *Photonics Spectra* 40(6), 50–60, 2006 (NIF); número
sobre amplificadores y láseres de fibra, *IEEE JSTQE* 7(1), 2001; número del milenio *IEEE
JSTQE* 6(6), 2000; Campbell & Suratwala, *J. Non-Crystalline Solids* 263/264, 318–341, 2000
(vidrios fosfato:Nd); Li & Teich, *IEEE JQE* 29, 2568–2578, 1993 (proceso puntual de
fotones en amplificadores de onda viajera); Digonnet (ed.), *Selected Papers on Rare
Earth-Doped Fiber Laser Sources and Amplifiers*, SPIE Milestone 37, 1992.

---

## Tablas y datos numéricos útiles

### Tabla 14.3-1 — Características de transiciones láser comunes (p. 556)

| Medio láser | $\lambda_o$ (nm)ᵃ | $\sigma_0$ (cm²) | $t_{sp}$ | $\Delta\nu$ᵇ | Tipo | $n$ |
|---|---|---|---|---|---|---|
| C⁵⁺ | 18.2 | 5×10⁻¹⁶ | 12 ps | 1 THz | I | ≈ 1 |
| Excímero ArF | 193 | 3×10⁻¹⁶ | 10 ns | 10 THz | I | ≈ 1 |
| Ar⁺ | 515 | 3×10⁻¹² | 10 ns | 3.5 GHz | I | ≈ 1 |
| Colorante Rodamina-6G | 560–640 | 2×10⁻¹⁶ | 5 ns | 40 THz | H/I | 1.40 |
| He–Ne | 633 | 3×10⁻¹³ | 150 ns | 1.5 GHz | I | ≈ 1 |
| Cr³⁺:Al₂O₃ (rubí) | 694 | 2×10⁻²⁰ | 3 ms | 330 GHz | H | 1.76 |
| Cr³⁺:BeAl₂O₄ (alejandrita) | 700–820 | 1×10⁻²⁰ | 260 µs | 25 THz | H | 1.74 |
| Ti³⁺:Al₂O₃ | 700–1050 | 3×10⁻¹⁹ | 3.9 µs | 100 THz | H | 1.76 |
| Yb³⁺:YAG | 1030 | 2×10⁻²⁰ | 1 ms | 1 THz | H | 1.82 |
| Nd³⁺:vidrio (fosfato) | 1053 | 4×10⁻²⁰ | 370 µs | 7 THz | I | 1.50 |
| Nd³⁺:YAG | 1064 | 3×10⁻¹⁹ | 230 µs | 150 GHz | H | 1.82 |
| Nd³⁺:YVO₄ | 1064 | 8×10⁻¹⁹ | 100 µs | 210 GHz | H | 2.0 |
| InGaAsPᶜ | 1300–1600 | 2×10⁻¹⁶ | 2.5 ns | 10 THz | H | 3.54 |
| Er³⁺:fibra de sílice | 1550 | 6×10⁻²¹ | 10 ms | 5 THz | H/I | 1.46 |
| CO₂ | 10 600 | 3×10⁻¹⁸ | 3 s | 60 MHz | I | ≈ 1 |

Notas de la tabla (p. 556): ᵃ longitud de onda en el espacio libre de la transición más
usada (He–Ne: 633 nm; también 543, 1150 y 3390 nm y cientos de otras). ᵇ para gases (p. ej.
CO₂) los valores son típicos de baja presión (el ancho depende de la presión por
ensanchamiento colisional, homogéneo). H = homogéneo, I = inhomogéneo. ᶜ para
In₀.₇₂Ga₀.₂₈As₀.₆P₀.₄ con concentración de portadores inyectados Δn = 1.8×10¹⁸ cm⁻³
(Ejemplos 17.2-1 a 17.2-3).

### Otros datos numéricos del capítulo

- Conversión de anchos: $\Delta\lambda = (\lambda_o^2/c_o)\Delta\nu$; 1 THz a 0.6 µm ↔ 1.2 nm
  (p. 537). A 1550 nm: 5.3 THz ↔ 40 nm; 12.5 THz ↔ ≈ 100 nm (pp. 552, 554).
- Rubí (p. 549, Ej. 14.1-1): $\lambda_o = 694.3$ nm, $\Delta\nu\approx 330$ GHz (homogéneo,
  fonones), $t_{sp}\approx 3$ ms, $\tau_{21}\approx t_{sp}$, $\tau_{32}\sim$ ps, $n = 1.76$,
  bandas de bombeo 550 nm y 400 nm; $N_a = 10^{22}$ cm⁻³ en el ejercicio.
- Nd³⁺:vidrio fosfato (p. 550): $\lambda_o = 1.053$ µm, $E_1 = 0.24$ eV sobre el base
  ($kT\approx 0.026$ eV), bandas de absorción de ~30 nm en 805, 745, 585, 520 nm,
  $t_{sp} = 375$ µs, $\tau_1\approx 300$ ps, $\Delta\nu\approx 7$ THz (inhomogéneo).
- NIF (p. 551): placas 46 × 81 × 4 cm, ≈ 2 mol % Nd, 192 haces × 16 etapas = 3072 placas,
  1.8 MJ en 3.5 ns (500 TW), ≤ 5 disparos/24 h, triplicado a 351 nm (KDP + DKDP).
- EDFA (pp. 552–553): bombeo 980 nm (InGaAs) o 1480 nm (InGaAsP); ejemplo 30 dB con 5 mW
  en 50 m y 300 ppm Er₂O₃; eficiencia ≈ 10 dB/mW; ganancia > 50 dB; salida > 100 W;
  $\Delta\lambda\approx 40$ nm ($\approx 5.3$ THz); banda C 1530–1565 nm, banda L
  1565–1625 nm, banda S 1460–1530 nm (Tm³⁺); 4 niveles a 77 K; transición 2.9 µm.
- RFA (pp. 554–555): corrimiento Stokes pico ≈ 13 THz (≈ 100 nm a 1550 nm) en sílice:Ge,
  ancho ≈ 12.5 THz; ganancia ≈ 20 dB; eficiencia ≈ 0.02 dB/mW; bombeo de cientos de mW
  (distribuido) a > 1 W (concentrado), ≈ 100 nm por debajo de la señal.
- Problema 14.4-7 (p. 566): $d = 10$ cm, $\phi_s = 4\times10^{18}$ fotones/cm²·s,
  $\phi(0) = 4\times10^{15}$ → $\phi(d) = 4\times10^{16}$ fotones/cm²·s.
- Problema 14.4-6 (p. 565): $N_a = 10^{23}$ átomos en 1 cm³, $E_2 - E_1 = 2.48$ eV
  ($\lambda_o = 0.5$ µm), $t_{sp} = 1$ ms, $\Delta\nu = 1$ GHz, $kT_1 = 0.026$ eV,
  $kT_2 = 0.26$ eV.

---

## Problemas al final del capítulo (pp. 565–566)

- **14.1-2 Amplifier Gain and Rod Length.** Amplificador de rubí con barra de 15 cm y
  ganancia de señal pequeña 12; hallar la ganancia de una barra de 20 cm (sin saturación).
- **14.1-3 Laser Amplifier Gain and Population Difference.** Barra de Nd³⁺:vidrio de 15 cm
  con ganancia total de señal pequeña 10 a $\lambda_o = 1.06$ µm; con la Tabla 14.3-1 hallar
  la diferencia de población $N$ (iones Nd³⁺/cm³) necesaria.
- **14.1-4 Amplification of a Broadband Signal.** Transición lorentziana con
  $\nu_0 = 5\times10^{14}$ Hz, $\Delta\nu = 1$ THz, invertida con $\gamma(\nu_0) = 0.1$ cm⁻¹,
  pérdida adicional $\alpha_s = 0.05$ cm⁻¹ independiente de $\nu$. Estimar pérdida o ganancia
  en 1 cm para luz de densidad espectral uniforme centrada en $\nu_0$ con ancho $2\Delta\nu$.
- **14.2-4 The Two-Level Pumping System.** Escribir las ecuaciones de tasa de un sistema de
  dos niveles y mostrar que no se logra inversión estacionaria bombeando ópticamente de forma
  directa entre 1 y 2.
- **14.2-5 Two Laser Lines.** Sistema de cuatro niveles 0, 1, 2, 3 con dos bombeos ($R_3$:
  0→3; $R_2$: 0→2). Posible inversión 3→1 y/o 2→1. Sin decaimiento 3→2 y con decaimiento de 3
  y 2 al base despreciable, escribir las ecuaciones de tasa en función de $\tau_1$,
  $\tau_{31}$, $\tau_{21}$; hallar $N_1$, $N_2$, $N_3$ estacionarias y discutir inversiones
  simultáneas 3→1 y 2→1. Mostrar que la presencia de radiación en 2→1 reduce la diferencia
  de población de 3→1.
- **14.4-3 Significance of the Saturation Photon-Flux Density.** En el sistema de dos
  niveles de Fig. 14.2-3, $\tau_2$ es la vida del nivel 2 sin emisión estimulada; con ella la
  tasa de decaimiento crece. Hallar $\phi$ para el cual la vida efectiva se reduce a la mitad
  y relacionarlo con $\phi_s$.
- **14.4-4 Saturation Optical Intensity.** Determinar $\phi_s(\nu_0)$ e $I_s(\nu_0)$ para las
  transiciones homogéneas de rubí y Nd³⁺:YAG de la Tabla 14.3-1.
- **14.4-5 Growth of the Photon-Flux Density in a Saturated Amplifier.** Graficar
  $\phi(z)/\phi_s$ vs $\gamma_0 z$ según (14.4-7) para $\phi(0)/\phi_s = 0.05$; identificar el
  inicio de la saturación.
- **14.4-6 Resonant Absorption of a Medium in Thermal Equilibrium.** Medio de $n = 1$,
  1 cm³, $N_a = 10^{23}$ átomos, nivel 2 a 2.48 eV ($\lambda_o = 0.5$ µm), $t_{sp} = 1$ ms,
  lorentziana $\Delta\nu = 1$ GHz, a $kT_1 = 0.026$ eV y $kT_2 = 0.26$ eV: (a) $N_1$, $N_2$;
  (b) fotones emitidos espontáneamente por segundo; (c) coeficiente de atenuación a 0.5 µm
  para flujo pequeño; (d) esbozo de $\alpha(\nu)$ con sus parámetros; (e) $\phi_s$ (flujo que
  reduce $\alpha$ a la mitad); (f) esbozo de $\phi(d)$ vs $\phi(0)$ en $\nu_0$ y $\nu_0 +
  \Delta\nu$ cuando $\phi(0)/\phi_s \ll 1$.
- **14.4-7 Gain in a Saturated Amplifying Medium.** Medio homogéneo, $d = 10$ cm,
  $\phi_s = 4\times10^{18}$ fotones/cm²·s; $\phi(0) = 4\times10^{15}$ produce
  $\phi(d) = 4\times10^{16}$. (a) Ganancia de señal pequeña $G_0$; (b) $\gamma_0$; (c) flujo
  para el cual $\gamma$ cae por un factor 5; (d) ganancia con $\phi(0) = 4\times10^{19}$:
  ¿mayor, menor o igual que $G_0$?
- ***14.5-2 Ratio of Signal Power to ASE Power.** Amplificador no saturado de longitud $d$
  y $\gamma_0(\nu)$ amplifica $\phi_S(\nu)$ e introduce ASE a tasa $\xi_{sp}$ por unidad de
  longitud. Salidas $\phi_S(d)$ y $\phi_{ASE}$; esbozar $\phi_S(d)/\phi_{ASE}$ en función de
  $\gamma_0(\nu)d$.
- ***14.5-3 Photon-Number Distribution for Amplified Coherent Light.** Superposición de luz
  térmica y coherente linealmente polarizada como modelo de la salida de un amplificador:
  fluctuaciones de energía $w$ con densidad chi-cuadrado no central
  $p(w) = (1/\bar w_{ASE})\exp[-(w + w_s)/\bar w_{ASE}]\,I_0[2\sqrt{w_s w}/\bar w_{ASE}]$
  ($I_0$ Bessel modificada de orden 0, $\bar w_{ASE}$ energía media de ASE, $w_s$ energía
  constante de la señal coherente amplificada). (a) Media y varianza de $w$; (b) con
  (12.2-27) y (12.2-28) hallar $\bar n$ y $\sigma_n^2$ y confirmar (14.5-4); (c) con
  (12.2-26) mostrar que
  $p(n) = \dfrac{\bar n_{ASE}^{\,n}}{(1+\bar n_{ASE})^{n+1}}\exp\!\left(-\dfrac{\bar n_s}{1+\bar n_{ASE}}\right)L_n\!\left(-\dfrac{\bar n_s/\bar n_{ASE}}{1+\bar n_{ASE}}\right)$,
  con $L_n(-x) = \sum_{k=0}^{n}\binom{n}{k}\dfrac{x^k}{k!}$ el polinomio de Laguerre;
  (d) graficar $p(n)$ para $\bar n_s/\bar n = 0, 0.5, 0.8, 1$ con $\bar n = 5$: se reduce a
  Bose–Einstein para $\bar n_s/\bar n = 0$ y a Poisson para $\bar n_s/\bar n = 1$.
  (Nota al pie: B. E. A. Saleh, *Photoelectron Statistics*, Springer 1978.)

(No existe un problema 14.1-1 ni 14.2-1/2/3 ni 14.4-1/2 ni 14.5-1 en la lista: esos números
corresponden a los ejercicios dentro del texto.)

---

## Relación con Óptica No Lineal

### Para el curso

- **Absorción/dispersión y causalidad (Kramers–Kronig).** §14.1B es un caso concreto de la
  relación entre parte real e imaginaria de la respuesta de un medio: $\varphi(\nu)$ es la
  transformada de Hilbert de $\tfrac12\gamma(\nu)$ (p. 538), y la forma dispersiva de
  (14.1-14) (Fig. 14.1-3) es exactamente la de $\mathrm{Re}\,\chi$ frente a $\mathrm{Im}\,\chi$
  de un oscilador lorentziano. Útil para entender por qué un medio con ganancia o absorción
  resonante tiene índice dependiente de la frecuencia (GVD cerca de resonancias).
- **Índice dependiente de la intensidad y saturación.** La saturación (14.4-3) es una no
  linealidad de **tipo poblacional** (resonante), distinta de la de $\chi^{(3)}$ (Kerr,
  no resonante): aquí el coeficiente de ganancia/absorción depende de $I$ como
  $\gamma_0/(1+I/I_s)$, y por Kramers–Kronig también lo hace el índice. Para $I\ll I_s$,
  $\gamma\approx\gamma_0(1 - I/I_s)$: en el límite de señal pequeña se comporta como un
  término cúbico efectivo (absorción saturable ↔ $\mathrm{Im}\,\chi^{(3)}$ resonante). Los
  **absorbedores saturables** (p. 559) son la base del *mode-locking* pasivo (cap. 15).
- **Raman (SRS) y FWM en fibras.** §14.3D presenta el amplificador Raman como amplificación
  por un proceso $\chi^{(3)}$ con ganancia $\gamma_R\propto I_p$ y espectro de ganancia fijado
  por los fonones del vidrio (pico ≈ 13 THz, ancho ≈ 12.5 THz en sílice; Fig. 14.3-7). Es la
  misma física que aparece en la propagación de pulsos en fibras (autodesplazamiento Raman
  de solitones, *Raman-induced frequency shift*) y en la generación de supercontinuo. La
  preferencia por bombeo contrapropagante y la dependencia con la polarización relativa
  bombeo–señal son también relevantes para XPM/FWM.
- **Propagación de pulsos / fibras.** EDFA y RFA son los amplificadores de los enlaces
  donde se estudian GVD, SPM y solitones; los parámetros (ganancia, banda C/L, ruido ASE,
  ecualización de ganancia) son el contexto experimental de esos temas. El ruido ASE
  (§14.5) es el límite fundamental de la relación señal/ruido en cadenas de amplificadores.
- **Haz gaussiano / ondas EM.** Las magnitudes $I = |E|^2/2\eta$, $\phi = I/h\nu$ y las
  relaciones $\Delta\lambda = (\lambda_o^2/c_o)\Delta\nu$ (p. 537) se usan continuamente para
  pasar de anchos espectrales en nm a THz.
- **Pulsos en medios dispersivos / amplificación de pulsos.** El NIF (Ejemplo 14.3-1) es el
  ejemplo canónico de cadena de amplificadores + conversión de frecuencia $\chi^{(2)}$ (SHG en
  KDP y SFG en DKDP, p. 551), enlazando este capítulo con $\chi^{(2)}$ y ajuste de fase (cap. 21).

### Para el proyecto final (anillos add-drop en Si₃N₄, dispersión, supercontinuo, sensado)

- **Supercontinuo en SiN.** La ganancia Raman (§14.3D) es un ingrediente del modelo de
  propagación (NLSE generalizada con respuesta Raman); en Si₃N₄ la respuesta Raman es
  débil comparada con la sílice, pero el formalismo "ganancia proporcional a $I_p$ con
  espectro fijado por el material" es el que se adapta. Los datos de la sílice (13 THz,
  12.5 THz) sirven como referencia de comparación.
- **Fuentes de bombeo.** Los sistemas de bombeo típicos (EDFA a 1550 nm en banda C,
  semilla + amplificador de potencia, ASE como ruido de fondo) son los que alimentan un
  experimento de supercontinuo o de sensado en resonadores; el ruido ASE del amplificador fija
  el piso de ruido espectral y afecta la resolución del sensado por corrimiento de resonancia.
- **Anillos add-drop / sensado.** La relación entre $\Delta\nu$ y $\Delta\lambda$ y la noción
  de ancho de línea lorentziano (14.1-8) son las mismas que describen la resonancia de un
  anillo (FWHM, $Q$); el modelo de "sistema resonante con fase dispersiva" de Fig. 14.1-3 es
  análogo a la respuesta de fase de un anillo cerca de resonancia.
- **Dispersión de guías.** La parte "corrimiento de fase ↔ ganancia por Hilbert" (14.1B)
  recuerda que cualquier pérdida o ganancia dependiente de λ en la guía (p. ej. absorción
  del cladding/analito) contribuye a la dispersión efectiva del modo; conviene tenerlo
  presente al interpretar barridos de $n_{eff}(\lambda)$ con pérdidas.
