# Capítulo 21 — Nonlinear Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 873–935 (PDF 895–957). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 21.
Las citas de página son páginas del libro (sumar 22 para la página del PDF).

Notación del libro (p. 874–879): campos reales en caligráfica, $\mathcal{E}(\mathbf r,t)$, $\mathcal{P}(\mathbf r,t)$;
amplitudes complejas $E(\omega)$, $E_q$, $A_q$ con dependencia temporal $\exp(j\omega t)$ y espacial
$\exp(-j\mathbf k\cdot\mathbf r)$, $j=\sqrt{-1}$; $\mathcal E(t)=\mathrm{Re}\{E(\omega)e^{j\omega t}\}=\tfrac12[E e^{j\omega t}+E^*e^{-j\omega t}]$,
de modo que $E(\omega)$ es la amplitud **de pico** del campo. Intensidad $I=|E|^2/2\eta$, con
$\eta=\eta_0/n$, $\eta_0=(\mu_0/\epsilon_0)^{1/2}\approx 377\ \Omega$. Unidades SI (MKS).
Las secciones con asterisco (21.4–21.7) son las que el libro marca como avanzadas.

---

## Resumen del capítulo

El capítulo construye la óptica no lineal a partir de la relación no lineal entre la densidad de
polarización $\mathcal P$ y el campo $\mathcal E$ en un medio dieléctrico, $\mathcal P=\epsilon_0\chi\mathcal E+2\mathrm d\mathcal E^2+4\chi^{(3)}\mathcal E^3+\cdots$
(p. 876), y de la ecuación de onda con fuente no lineal $\nabla^2\mathcal E-(1/c^2)\partial^2\mathcal E/\partial t^2=-\mathcal S$,
$\mathcal S=-\mu_0\partial^2\mathcal P_{\rm NL}/\partial t^2$ (p. 878). Con la **primera aproximación de Born** (el campo incidente
crea la fuente, la fuente radia) se derivan, para medios de segundo orden (21.2), la generación de
segundo armónico (SHG), la rectificación óptica, el efecto electroóptico (Pockels como caso límite de
$\chi^{(2)}$), la mezcla de tres ondas (OFC/SFG, DFG, OPA, OPO, SPDC), las condiciones de ajuste de
frecuencia y de fase, las curvas de sintonía por birrefringencia, la longitud de coherencia, el ancho
de banda de phase matching y el cuasi‑ajuste de fase (QPM, PPLN). Para medios de tercer orden (21.3):
THG, efecto Kerr óptico ($n=n+n_2I$), automodulación de fase (SPM), autoenfoque y lente Kerr,
solitones espaciales (ecuación de Schrödinger no lineal), ganancia Raman como parte imaginaria de
$\chi^{(3)}$, modulación de fase cruzada (XPM), mezcla de cuatro ondas (FWM), mezcla de tres ondas
degenerada en fibra y conjugación de fase (OPC) como holografía en tiempo real. Las secciones 21.4 y
21.5 repiten el análisis con **teoría de ondas acopladas** (envolventes lentamente variables,
variables $\mathfrak a_q$ normalizadas a flujo de fotones, relación de Manley–Rowe), resolviendo SHG
(tanh²), OFC (sin²), OPA (cosh²/sinh²), umbrales de OPO (SRO y DRO), FWM con Kerr, mezcla de tres
ondas en $\chi^{(3)}$ (amplificador sensible a fase), THG y OPC (espejo amplificador, oscilador).
La 21.6 introduce los tensores $\mathrm d_{ijk}$ y $\chi^{(3)}_{ijkl}$, la notación contraída
$\mathrm d_{iJ}$, tablas de simetría y valores, y el coeficiente efectivo $\mathrm d_{\rm eff}$; la 21.7
trata medios dispersivos (serie de Volterra, $\mathrm d(\omega_3;\omega_1,\omega_2)$, oscilador anarmónico, regla de
Miller, simetrías intrínsecas).

---

## Convenciones de este capítulo frente a Boyd

Saleh escribe (21.1-2), p. 876, siguiendo a Yariv (*Quantum Electronics*): 
$\mathcal P=\epsilon_0\chi\mathcal E+2\mathrm d\,\mathcal E^2+4\chi^{(3)}\mathcal E^3+\cdots$.
La nota al pie de la p. 876 dice explícitamente que otros libros (Shen, *Principles of Nonlinear
Optics*) usan $\mathcal P=\epsilon_0(\chi\mathcal E+\chi^{(2)}\mathcal E^2+\chi^{(3)}\mathcal E^3)$ — que es la convención de Boyd
(*Nonlinear Optics*, 3.ª ed., ec. (1.1.2), SI). Equivalencias (deducidas igualando término a término):

| Magnitud | Saleh & Teich (cap. 21) | Boyd (3.ª ed., SI) | Equivalencia |
|---|---|---|---|
| Polarización lineal | $\epsilon_0\chi\mathcal E$ | $\epsilon_0\chi^{(1)}\tilde E$ | $\chi=\chi^{(1)}$, $n^2=1+\chi$ |
| Término de 2.º orden | $2\mathrm d\,\mathcal E^2$ | $\epsilon_0\chi^{(2)}\tilde E^2$ | $\mathrm d_{\rm Saleh}=\tfrac12\epsilon_0\chi^{(2)}_{\rm Boyd}=\epsilon_0\, d_{\rm Boyd}$ (Boyd: $d=\chi^{(2)}/2$) |
| Unidades de 2.º orden | $\mathrm d$ en C/V² (10⁻²⁴–10⁻²¹, p. 877) | $\chi^{(2)}$, $d$ en m/V (pm/V) | $\mathrm d/\epsilon_0$ [pm/V] es el $d$ usual: dividir C/V² por $10^{-12}\epsilon_0\approx 8.85\times10^{-24}$ (p. 925, nota b de la tabla 21.6-3) |
| Término de 3.er orden | $4\chi^{(3)}\mathcal E^3$ | $\epsilon_0\chi^{(3)}\tilde E^3$ | $\chi^{(3)}_{\rm Saleh}=\tfrac14\epsilon_0\chi^{(3)}_{\rm Boyd}$ |
| Unidades de 3.er orden | $\chi^{(3)}$ en C·m/V³ (10⁻³⁴–10⁻²⁹, p. 877) | $\chi^{(3)}$ en m²/V² | $\chi^{(3)}_{\rm Boyd}[\mathrm{m^2/V^2}]=4\chi^{(3)}_{\rm Saleh}/\epsilon_0$ |
| Coeficiente de Kerr | $n_2=\dfrac{3\eta_0}{n^2\epsilon_0}\chi^{(3)}$ (21.3-6), $n(I)=n+n_2I$ | $n_2=\dfrac{3\chi^{(3)}}{4n_0^2\epsilon_0c}$ (Boyd 4.1.19), $n=n_0+n_2I$ | Idénticas al sustituir $\chi^{(3)}_{\rm S}=\epsilon_0\chi^{(3)}_{\rm B}/4$ y $\eta_0=1/(\epsilon_0c)$. Mismo $n_2$ [m²/W] |
| Variante de $n_2$ | nota p. 896: $n(I)=n+n_2|E|^2/2$, con $n_2$ distinto en un factor $\eta$ | Boyd $\bar n_2$ con $n=n_0+\bar n_2\langle\tilde E^2\rangle$ | cuidado al comparar tablas |
| Amplitud compleja | $\mathcal E=\mathrm{Re}\{Ee^{j\omega t}\}$ → $E$ = amplitud de pico; $I=|E|^2/2\eta$ | $\tilde E=Ee^{-i\omega t}+{\rm c.c.}$ → $E$ = mitad del pico; $I=2n\epsilon_0c|E|^2$ | $E_{\rm Saleh}=2E_{\rm Boyd}$; $j\leftrightarrow -i$ (Saleh $e^{j(\omega t-kz)}$, Boyd $e^{i(kz-\omega t)}$) |
| Amplitudes de $\mathcal P_{\rm NL}$ | $P_{\rm NL}(2\omega)=\mathrm d E^2$, $P_{\rm NL}(\omega_1+\omega_2)=2\mathrm d E_1E_2$, $P(\omega)=3\chi^{(3)}|E|^2E$ | $P(2\omega)=\epsilon_0\chi^{(2)}E^2$, $P(\omega_3)=2\epsilon_0\chi^{(2)}E_1E_2$, $P(\omega)=3\epsilon_0\chi^{(3)}|E|^2E$ | coinciden con los factores de degeneración de Boyd al hacer los reemplazos de las filas anteriores |
| Pockels | $\mathfrak r\approx-4\mathrm d/(\epsilon_0n^4)$ (21.2-11) | $r\sim -2\chi^{(2)}/n^4$ (Boyd cap. 11, con factores de dispersión) | mismas, salvo dispersión |
| Kerr DC | $\mathfrak s=-12\chi^{(3)}/(\epsilon_0n^4)$ (21.3-2) | — | — |
| Tensor contraído | $\mathrm d_{iJ}$, $J=1..6\leftrightarrow jk=11,22,33,23,31,12$ (p. 924) | $d_{il}$, mismo orden | misma convención; $\mathrm d_{iJ}$ es el "transpuesto" del tensor Pockels $\mathfrak r_{Ik}$ |
| Phase mismatch | $\Delta k=k_3-k_1-k_2$ (p. 890, 908); eficiencia $\propto\mathrm{sinc}^2(\Delta kL/2\pi)$ con $\mathrm{sinc}(x)=\sin(\pi x)/(\pi x)$ | $\Delta k=k_1+k_2-k_3$; $\mathrm{sinc}^2(\Delta kL/2)$ con sinc$(x)=\sin x/x$ | mismo resultado físico; signo y definición de sinc distintos |
| Longitud de coherencia | $L_c=2\pi/|\Delta k|$ (21.2-28) | $L_{\rm coh}=2/\Delta k$ (Boyd 2.2) | ¡difieren en factor $\pi$! citar siempre la definición |

---

## Secciones

### Introducción (p. 874–875)

Consecuencias de la hipótesis lineal (p. 874): índice y absorción independientes de la intensidad,
superposición válida, la frecuencia no cambia, dos haces no interactúan. Tras el láser (1960) se
observa lo contrario: $n$ depende de $I$, se viola la superposición, cambia la frecuencia (rojo→azul),
los fotones interactúan. La no linealidad reside en el **medio**, no en la luz. Se restringe al
principio a medio no dispersivo, homogéneo e isótropo ($\mathcal P\parallel\mathcal E$, análisis por componentes).
Dos niveles: simplificado (21.1–21.3, aproximación de Born) y ondas acopladas (21.4–21.5). Medios
anisótropos (21.6) y dispersivos (21.7).

Hipótesis central (p. 875): el medio es **pasivo** (no intercambia energía con la luz) → interacciones
**paramétricas**. Lo no paramétrico está en otros capítulos: interacciones láser (13.3, 14.4),
absorción multifotónica ($\propto I^k$, 13.5B), scattering no lineal Raman/Brillouin estimulado
(13.5C, 14.3D), pulsos en medios no lineales (22.5), solitones ópticos temporales (22.5B, 24.2E),
biestabilidad óptica (23.4).

### 21.1 Nonlinear Optical Media (p. 875)

**Resumen.** Medio lineal: $\mathcal P=\epsilon_0\chi\mathcal E$; no lineal: relación $\mathcal P$–$\mathcal E$ curva (Fig. 21.1-1,
p. 876). Origen microscópico: $\mathcal P=N\mathfrak p$; la relación $\mathfrak p$–$\mathcal E$ se vuelve no lineal cuando $\mathcal E$ es
comparable al campo interatómico ($\sim10^5$–$10^8$ V/m); modelo de Lorentz con fuerza restauradora no
lineal (oscilador anarmónico, desarrollado en 21.7). Otra fuente: dependencia de $N$ con el campo
(medios láser, saturación, 14.4). Como la no linealidad es débil se expande en Taylor.

**Ecuaciones.**

$$\mathcal P=a_1\mathcal E+\tfrac12 a_2\mathcal E^2+\tfrac16 a_3\mathcal E^3+\cdots \qquad (21.1\text{-}1),\ \text{p. 876}$$

con $a_1=\epsilon_0\chi$, $n^2=\epsilon/\epsilon_0=1+\chi$. Forma habitual (**recuadro**):

$$\boxed{\mathcal P=\epsilon_0\chi\mathcal E+2\mathrm d\,\mathcal E^2+4\chi^{(3)}\mathcal E^3+\cdots}\qquad(21.1\text{-}2),\ \text{p. 876}$$

donde $\mathrm d=\tfrac14a_2$ y $\chi^{(3)}=\tfrac1{24}a_3$ (p. 877).

- **Medios centrosimétricos** (invariantes bajo $\mathbf r\to-\mathbf r$): $\mathcal P(\mathcal E)$ impar ⇒ $\mathrm d=0$; la primera no
  linealidad es de tercer orden (p. 877).
- Valores típicos (p. 877): $\mathrm d=10^{-24}$–$10^{-21}$ C/V² (cristales dieléctricos, semiconductores,
  orgánicos); $\chi^{(3)}=10^{-34}$–$10^{-29}$ C·m/V³ (vidrios, cristales, semiconductores, vidrios dopados,
  orgánicos). Pozos cuánticos asimétricos o polarizados: no linealidades grandes en IR medio y lejano.

**EXERCISE 21.1-1 (p. 877) — Intensidad necesaria para efectos no lineales.** (a) Hallar la intensidad
(W/cm²) para la que el segundo término de (21.1-2) es el 1 % del primero en ADP (NH₄H₂PO₄), $n=1.5$,
$\mathrm d=6.8\times10^{-24}$ C/V² a $\lambda_0=1.06$ μm. (b) Intensidad para la que el tercer término es 1 % del
primero en CS₂, $n=1.6$, $\mathrm d=0$, $\chi^{(3)}=4.4\times10^{-32}$ C·m/V³ a 694 nm. Nota: $I=|E_0|^2/2\eta=\langle\mathcal E^2\rangle/\eta$,
$\eta=\eta_0/n$.
*Cálculo propio (no está en el libro):* (a) $2\mathrm dE/(\epsilon_0\chi)=0.01$, $\chi=1.25$ ⇒ $E\approx8.1\times10^9$ V/m,
$\eta=251\ \Omega$ ⇒ $I\approx1.3\times10^{17}$ W/m² $=1.3\times10^{13}$ W/cm². (b) $4\chi^{(3)}E^2/(\epsilon_0\chi)=0.01$, $\chi=1.56$
⇒ $E\approx8.9\times10^8$ V/m, $\eta=236\ \Omega$ ⇒ $I\approx1.7\times10^{15}$ W/m² $=1.7\times10^{11}$ W/cm².

#### La ecuación de onda no lineal (p. 877–878)

Ecuación de onda (5.2-25) para medio homogéneo e isótropo:

$$\nabla^2\mathcal E-\frac1{c_0^2}\frac{\partial^2\mathcal E}{\partial t^2}=\mu_0\frac{\partial^2\mathcal P}{\partial t^2}\qquad(21.1\text{-}3)$$

Separando $\mathcal P=\epsilon_0\chi\mathcal E+\mathcal P_{\rm NL}$ (21.1-4), $\mathcal P_{\rm NL}=2\mathrm d\mathcal E^2+4\chi^{(3)}\mathcal E^3+\cdots$ (21.1-5), y usando
$c=c_0/n$, $n^2=1+\chi$, $c_0=1/(\epsilon_0\mu_0)^{1/2}$ (**recuadro, p. 878**):

$$\boxed{\nabla^2\mathcal E-\frac1{c^2}\frac{\partial^2\mathcal E}{\partial t^2}=-\mathcal S,\qquad \mathcal S=-\mu_0\frac{\partial^2\mathcal P_{\rm NL}}{\partial t^2}}\qquad(21.1\text{-}6),(21.1\text{-}7)$$

Interpretación: $\mathcal S$ es una **fuente que radia en un medio lineal de índice $n$**; como $\mathcal S$ es función
no lineal de $\mathcal E$, es una EDP no lineal. Dos métodos: (i) iterativo (**aproximación de Born**, 21.2–21.3);
(ii) ondas acopladas (21.4–21.5).

#### Teoría de scattering: aproximación de Born (p. 878–879)

Se escribe $\mathcal S=\mathcal S(\mathcal E)$ (Fig. 21.1-2: lazo de realimentación fuente→radiación→campo). Campo
incidente $\mathcal E_0$ → fuente $\mathcal S(\mathcal E_0)$ → radia $\mathcal E_1$ → $\mathcal S(\mathcal E_1)$ → $\mathcal E_2$, etc. **Primera aproximación de Born**:
quedarse en $\mathcal E_1$; válida si la no linealidad es débil. Dos pasos: (1) con $\mathcal E_0$ se calcula $\mathcal P_{\rm NL}$
y $\mathcal S(\mathcal E_0)$; (2) $\mathcal E_1$ se obtiene sumando las ondas esféricas de cada punto fuente (como en la teoría
de difracción, 4.3). Como $\mathcal S(\mathcal E_0)$ es no lineal, aparecen frecuencias nuevas (p. 879).

### 21.2 Second-Order Nonlinear Optics (p. 879)

Se desprecia todo orden > 2 (**recuadro**): $\mathcal P_{\rm NL}=2\mathrm d\,\mathcal E^2$ (21.2-1). Con la primera aproximación de
Born, $\mathcal S$ y el campo emitido tienen las mismas componentes espectrales que $\mathcal P_{\rm NL}$.

#### 21.2A Second-Harmonic Generation (SHG) and Rectification (p. 879)

Campo armónico $\mathcal E(t)=\mathrm{Re}\{E(\omega)e^{j\omega t}\}=\tfrac12[E(\omega)e^{j\omega t}+E^*(\omega)e^{-j\omega t}]$ (21.2-2). Entonces

$$\mathcal P_{\rm NL}(t)=P_{\rm NL}(0)+\mathrm{Re}\{P_{\rm NL}(2\omega)e^{j2\omega t}\}\qquad(21.2\text{-}3)$$
$$P_{\rm NL}(0)=\mathrm d\,E(\omega)E^*(\omega)\qquad(21.2\text{-}4)\qquad\quad P_{\rm NL}(2\omega)=\mathrm d\,E^2(\omega)\qquad(21.2\text{-}5)$$

Fig. 21.2-1 (p. 880): la parábola $\mathcal P$–$\mathcal E$ convierte una senoide en una componente DC más un segundo
armónico.

**SHG.** La fuente tiene componente a $2\omega$ con amplitud $S(2\omega)=4\mu_0\omega^2\,\mathrm d\,E(\omega)E(\omega)$ (p. 879),
que radia a $2\omega$ ($\lambda_0/2$). $I(2\omega)\propto|S(2\omega)|^2\propto\mathrm d^2 I^2(\omega)$, con $I(\omega)=|E(\omega)|^2/2\eta$. Como las
emisiones se suman coherentemente, $I(2\omega)\propto L^2$. Eficiencia $\eta_{\rm SHG}=I(2\omega)/I(\omega)\propto L^2I(\omega)$; con
$I=P/A$ (**recuadro, p. 880**):

$$\boxed{\eta_{\rm SHG}=C^2\frac{L^2}{A}P}\qquad(21.2\text{-}6)$$

$C^2$ [W⁻¹] $\propto\mathrm d^2\omega^2$ (expresión en (21.4-36)). Para maximizar: alta $P$ (láseres pulsados), $L^2/A$
grande. Con haz gaussiano enfocado a $W_0$: $A=\pi W_0^2$, $L=2z_0=2\pi W_0^2/\lambda$ ⇒ $L^2/A=2L/\lambda=4A/\lambda^2$;
así, si la difracción limita, $\eta\propto L$ y conviene el mayor spot que quepa. Fig. 21.2-2: (a) cristal
delgado (enfocar al mínimo $A$), (b) cristal grueso (spot más grande que quepa), (c) guía de onda
(confinamiento en $A$ pequeño a lo largo de $L$ grande ⇒ $\eta\propto L^2$, p. 881). En fibras de sílice,
aunque centrosimétricas, se observa SHG por cuadrupolo eléctrico, dipolo magnético y defectos/centros de
color. Fig. 21.2-3 (p. 881): (a) rubí 694 nm → 347 nm (UV) en KDP; (b) Nd³⁺:YAG 1.06 μm → 530 nm en
fibra de sílice dopada con Ge y P; (c) láser AlGaAs 790 nm → 395 nm dentro de la cavidad.

**Rectificación óptica (p. 881).** $P_{\rm NL}(0)$ es una polarización estática que crea una diferencia
de potencial DC entre las placas de un condensador que contiene el material (Fig. 21.2-4). Análogo al
rectificador electrónico. Un pulso de varios MW de pico genera varios cientos de μV.

#### 21.2B The Electro-Optic Effect (p. 882)

Campo óptico más campo estático: $\mathcal E(t)=E(0)+\mathrm{Re}\{E(\omega)e^{j\omega t}\}$ (21.2-7). Entonces (21.2-8)
$\mathcal P_{\rm NL}(t)=P_{\rm NL}(0)+\mathrm{Re}\{P_{\rm NL}(\omega)e^{j\omega t}\}+\mathrm{Re}\{P_{\rm NL}(2\omega)e^{j2\omega t}\}$ con

$$P_{\rm NL}(0)=\mathrm d\,[2E^2(0)+|E(\omega)|^2]\quad(21.2\text{-}9a),\qquad P_{\rm NL}(\omega)=4\mathrm d\,E(0)E(\omega)\quad(21.2\text{-}9b),\qquad P_{\rm NL}(2\omega)=\mathrm d\,E^2(\omega)\quad(21.2\text{-}9c)$$

Si $|E(\omega)|^2\ll|E(0)|^2$ se desprecia $P_{\rm NL}(2\omega)$: linealización de $\mathcal P_{\rm NL}$ alrededor de $E(0)$
(Fig. 21.2-5). De (21.2-9b), $P_{\rm NL}(\omega)=\epsilon_0\Delta\chi E(\omega)$ con $\Delta\chi=(4\mathrm d/\epsilon_0)E(0)$; de $n^2=1+\chi$,
$2n\Delta n=\Delta\chi$:

$$\Delta n=\frac{2\mathrm d}{n\epsilon_0}E(0)\qquad(21.2\text{-}10)$$

Comparando con el efecto Pockels $\Delta n=-\tfrac12n^3\mathfrak rE(0)$ (cap. 20):

$$\mathfrak r\approx-\frac{4}{\epsilon_0n^4}\mathrm d\qquad(21.2\text{-}11),\ \text{p. 883}$$

Advertencia del libro: (21.2-11) **no concuerda con los valores experimentales** de $\mathfrak r$ y $\mathrm d$
porque se supuso medio no dispersivo, y aquí una componente está a $\omega$ y la otra a 0 (ver 21.7).

#### 21.2C Three-Wave Mixing (p. 883)

$\mathcal E(t)=\mathrm{Re}\{E(\omega_1)e^{j\omega_1t}+E(\omega_2)e^{j\omega_2t}\}$ (21.2-12). $\mathcal P_{\rm NL}=2\mathrm d\mathcal E^2$ tiene cinco frecuencias:
$0,\ 2\omega_1,\ 2\omega_2,\ \omega_+=\omega_1+\omega_2,\ \omega_-=\omega_1-\omega_2$:

$$P_{\rm NL}(0)=\mathrm d[|E(\omega_1)|^2+|E(\omega_2)|^2]\ (21.2\text{-}13a),\quad P_{\rm NL}(2\omega_1)=\mathrm dE(\omega_1)E(\omega_1)\ (b),\quad P_{\rm NL}(2\omega_2)=\mathrm dE(\omega_2)E(\omega_2)\ (c)$$
$$P_{\rm NL}(\omega_+)=2\mathrm dE(\omega_1)E(\omega_2)\ (21.2\text{-}13d),\qquad P_{\rm NL}(\omega_-)=2\mathrm dE(\omega_1)E^*(\omega_2)\ (21.2\text{-}13e)$$

Diferencia → **frequency down‑conversion**; suma → **up‑conversion** o **sum‑frequency generation**.
Fig. 21.2-6: Nd:YAG 1.06 μm + CO₂ 10.6 μm en proustita → 0.96 μm ($\lambda_{03}^{-1}=\lambda_{01}^{-1}+\lambda_{02}^{-1}$).
No todas las frecuencias se generan: hace falta phase matching (p. 884).

**Ajuste de frecuencia y de fase (p. 884).** Ondas planas $E(\omega_1)=A_1e^{-j\mathbf k_1\cdot\mathbf r}$,
$E(\omega_2)=A_2e^{-j\mathbf k_2\cdot\mathbf r}$ ⇒ $P_{\rm NL}(\omega_3)=2\mathrm dA_1A_2e^{-j\mathbf k_3\cdot\mathbf r}$ con (**recuadros**)

$$\boxed{\omega_1+\omega_2=\omega_3}\ (21.2\text{-}14)\ \text{Frequency-Matching},\qquad \boxed{\mathbf k_1+\mathbf k_2=\mathbf k_3}\ (21.2\text{-}15)\ \text{Phase-Matching}$$

Fig. 21.2-7: triángulo de vectores de onda. Ambas condiciones aseguran el ajuste temporal y espacial
de las fases de las tres ondas para interacción sostenida.

**Modalidades de mezcla de tres ondas (p. 884–885).** Solo la componente que cumple phase matching
se sostiene. Generada la onda 3, interactúa con la 1 y genera la 2 ($\omega_2=\omega_3-\omega_1$, también con
phase matching), etc.: las tres ondas se acoplan mutuamente → **three‑wave mixing**. **Two‑wave
mixing no es posible** en general, salvo el caso degenerado $\omega_2=2\omega_1$. Proceso **paramétrico**:
- **OFC** (optical frequency conversion): 1 y 2 → $\omega_3=\omega_1+\omega_2$ (SFG; SHG es el caso degenerado); el
  inverso es **down‑conversion** / DFG ($\omega_2=\omega_3-\omega_1$). Uso: luz coherente donde no hay láseres,
  mezcladores ópticos.
- **OPA**: 1 (**señal**) y 3 (**bomba**) → crece 1, se crea 2 (**idler**). Ganancia depende de la bomba.
  Detección de señales débiles.
- **OPO**: OPA con realimentación; solo se suministra la bomba. Luz coherente sintonizable.
- **SPDC**: solo bomba; down‑conversion espontánea; múltiples soluciones de (21.2-14)/(21.2-15) → cono
  multiespectral. Fig. 21.2-8 (p. 885): esquemas OFC, OPA, OPO, SPDC.

**Mezcla como interacción de fotones (p. 886).** Dos fotones $\hbar\omega_1,\hbar\omega_2$ se aniquilan y se crea
$\hbar\omega_3$ (o al revés). Conservación de energía y momento:

$$\hbar\omega_1+\hbar\omega_2=\hbar\omega_3\ (21.2\text{-}16),\qquad \hbar\mathbf k_1+\hbar\mathbf k_2=\hbar\mathbf k_3\ (21.2\text{-}17)$$

Fig. 21.2-9: (a) aniquilación de dos fotones de baja frecuencia (nivel superior **virtual**, línea
discontinua); (b) fisión de un fotón; (c) láser de 3 niveles. Diferencias con el láser: una transición
láser es no radiativa; el láser intercambia energía con el medio; los niveles del láser son discretos
(atómicos) mientras que los del proceso paramétrico los dictan energía del fotón y phase matching
(sintonizables).

Conservación del número de fotones: $\Delta\phi_1=\Delta\phi_2=-\Delta\phi_3$. Para ondas colineales en $z$ (**recuadros,
p. 887**):

$$\boxed{\frac{d\phi_1}{dz}=\frac{d\phi_2}{dz}=-\frac{d\phi_3}{dz}}\ (21.2\text{-}18)\ \text{Photon-Number Conservation}$$
$$\boxed{\frac d{dz}\Big(\frac{I_1}{\omega_1}\Big)=\frac d{dz}\Big(\frac{I_2}{\omega_2}\Big)=-\frac d{dz}\Big(\frac{I_3}{\omega_3}\Big)}\ (21.2\text{-}19)\ \text{Manley–Rowe}$$

con $I_q=\hbar\omega_q\phi_q$ ($\phi_q$ en fotones/s·m²). Manley–Rowe viene de sistemas electrónicos no lineales;
se deriva sin fotones en el Ejercicio 21.4-2.

#### 21.2D Phase Matching and Tuning Curves (p. 887)

**Colineal.** Sin dispersión, $n\omega_1/c_0+n\omega_2/c_0=n\omega_3/c_0$ se cumple automáticamente. Con dispersión
(**recuadro**):

$$\boxed{\omega_1+\omega_2=\omega_3,\qquad \omega_1n_1+\omega_2n_2=\omega_3n_3}\qquad(21.2\text{-}20)\ \text{Matching Conditions}$$

Normalmente imposible en medio isótropo con dispersión normal → se usa **birrefringencia** para
compensar. Cristal uniáxico con $n_o(\omega)$, $n_e(\omega)$; cada onda es o (ordinaria) o e (extraordinaria),
y el proceso se etiqueta p. ej. e‑o‑o (ondas 1, 2, 3). Para onda e:

$$\frac1{n^2(\theta,\omega)}=\frac{\cos^2\theta}{n_o^2(\omega)}+\frac{\sin^2\theta}{n_e^2(\omega)}\qquad(21.2\text{-}21)$$

($\theta$: ángulo entre dirección de propagación y eje óptico; elipse (6.3-15), Fig. 6.3-7). **Tipo I**:
señal e idler con la misma polarización; **Tipo II**: ortogonales (p. 888).

**EXAMPLE 21.2-1 (p. 888) — SHG colineal Tipo I.** $\omega_1=\omega_2=\omega$, $\omega_3=2\omega$, $n_1=n_2$ ⇒ condición
$n_3=n_1$: el fundamental y el segundo armónico deben tener el mismo índice, lo que exige
polarizaciones distintas (o‑o‑e o e‑e‑o). Para e‑e‑o: $n_1=n(\theta,\omega)$, $n_3=n_o(2\omega)$ (**recuadro**):

$$\boxed{n(\theta,\omega)=n_o(2\omega)}\qquad(21.2\text{-}22)\ \text{SHG Type-I e-e-o}$$

Fig. 21.2-10: (a) curvas $n_o$, $n_e$ vs $\omega$; (b) superficies de índice a $\omega$ (sólidas) y $2\omega$ (discontinuas),
el ángulo $\theta$ donde el círculo a $2\omega$ corta la elipse a $\omega$; (c) cristal cortado a $\theta$. Datos KDP a
694 nm: $n_o(\omega)=1.506$, $n_e(\omega)=1.466$; a 347 nm: $n_o(2\omega)=1.534$, $n_e(2\omega)=1.490$ ⇒ $\theta=52°$ (ángulo de
corte). Para o‑o‑e en KDP a 1.06 μm, $\theta=41°$.

**EXAMPLE 21.2-2 (p. 888–889) — OPO colineal.** Tipo I o‑o‑e (**recuadro**):

$$\boxed{\omega_1+\omega_2=\omega_3,\quad \omega_1n_o(\omega_1)+\omega_2n_o(\omega_2)=\omega_3n(\theta,\omega_3)}\qquad(21.2\text{-}23)$$

Tipo II e‑o‑e (**recuadro**):

$$\boxed{\omega_1+\omega_2=\omega_3,\quad \omega_1n(\theta,\omega_1)+\omega_2n_o(\omega_2)=\omega_3n(\theta,\omega_3)}\qquad(21.2\text{-}24)$$

$n_o(\omega),n_e(\omega)$ por Sellmeier (5.5-28). Resolviendo para $\omega_1,\omega_2$ vs $\theta$ → **curva de sintonía**.
Fig. 21.2-11 (p. 889): OPO BBO colineal bombeado a 532 nm (Nd:YAG doblado): (a) Tipo I, señal e idler
(ambos o) entre ~0.6 y 1.6 μm para $\theta\approx22$–23°; (b) Tipo II, señal (e) e idler (o) para $\theta\approx20$–50°,
degenerado (~1.06 μm) cerca de $\theta\approx$ 35°.

**No colineal (p. 889).** $\mathbf k_1+\mathbf k_2=\mathbf k_3$ ⇔ $\omega_1n_1\hat u_1+\omega_2n_2\hat u_2=\omega_3n_3\hat u_3$ (**recuadro**):

$$\boxed{\omega_1+\omega_2=\omega_3,\quad \omega_1n_1\sin\theta_1=\omega_2n_2\sin\theta_2,\quad \omega_1n_1\cos\theta_1+\omega_2n_2\cos\theta_2=\omega_3n_3}\qquad(21.2\text{-}25)$$

($\theta_1,\theta_2$: ángulos de las ondas 1 y 2 con la onda 3.)

**EXERCISE 21.2-1 (p. 889–890) — SHG Tipo II no colineal.** Fig. 21.2-12: onda o y onda e a $\omega$ generan
onda e a $2\omega$; direcciones coplanares con el eje óptico, ángulos $\theta_1,\theta_2,\theta$ respecto a la dirección del
SH. $n_1=n_o(\omega)$, $n_2=n(\theta+\theta_2,\omega)$, $n_3=n(\theta,2\omega)$:

$$n_o(\omega)\sin\theta_1=n(\theta+\theta_2,\omega)\sin\theta_2,\qquad n_o(\omega)\cos\theta_1+n(\theta+\theta_2,\omega)\cos\theta_2=2n(\theta,2\omega)\qquad(21.2\text{-}26)$$

Para KDP y fundamental 1.06 μm (Nd:YAG), determinar la orientación del cristal y $\theta_1,\theta_2$.

**EXAMPLE 21.2-3 (p. 890) — SPDC.** Bomba $\omega_3$ crea pares $(\omega_1,\theta_1)$, $(\omega_2,\theta_2)$ que cumplen (21.2-25).
Tipo I o‑o‑e: $n_1=n_o(\omega_1)$, $n_2=n_o(\omega_2)$, $n_3=n(\theta,\omega_3)$ + Sellmeier → continuo de soluciones.
Fig. 21.2-13: BBO a $\theta=33.53°$, bomba 351.5 nm (Ar⁺); curva de sintonía ángulo (±6°) vs frecuencia
normalizada ($\omega_0=\omega_3/2$, 0.9–1.1); cada punto $(\omega_1,\theta_1)$ se empareja con $(\omega_3-\omega_1,\theta_2)$; por simetría
circular son anillos, y cada punto de un anillo se empareja con el diametralmente opuesto del otro.

**Desajuste de fase tolerable y longitud de coherencia (p. 890–891).** $\Delta\mathbf k=\mathbf k_3-\mathbf k_1-\mathbf k_2\ne0$:
$P_{\rm NL}(\omega_3)=2\mathrm dA_1A_2\exp(j\Delta\mathbf k\cdot\mathbf r)\exp(-j\mathbf k_3\cdot\mathbf r)$; fuente $2\omega_3^2\mu_0\mathrm dA_1A_2\exp(j\Delta\mathbf k\cdot\mathbf r)$
(Prob. 21.2-6):

$$I_3\propto\Big|\int_V\mathrm dA_1A_2\exp(j\Delta\mathbf k\cdot\mathbf r)\,d\mathbf r\Big|^2\qquad(21.2\text{-}27)$$

Caso 1D de ancho $L$: $I_3\propto|\int_0^L e^{j\Delta kz}dz|^2=L^2\,\mathrm{sinc}^2(\Delta kL/2\pi)$, sinc$(x)=\sin(\pi x)/(\pi x)$.
Factor de reducción $\mathrm{sinc}^2(\Delta kL/2\pi)$: 1 en $\Delta k=0$, $(2/\pi)^2\approx0.4$ en $|\Delta k|=\pi/L$, cero en
$|\Delta k|=2\pi/L$ (Fig. 21.2-14). Tolerancia $\propto1/L$. (**Recuadro**)

$$\boxed{L_c=2\pi/|\Delta k|}\qquad(21.2\text{-}28)\ \text{Coherence Length}$$

Para SHG: $|\Delta k|=2(2\pi/\lambda_0)|n_3-n_1|$ ⇒ $L_c=\lambda_0/2|n_3-n_1|$; con $|n_3-n_1|=10^{-2}$, $L_c=50\lambda$.
Interpretación: incertidumbre $\Delta k\propto1/L$ del confinamiento (A.2-6) ⇒ $\Delta p=\hbar\Delta k$: "violación
aparente" de la conservación del momento.

**Ancho de banda de phase matching (p. 891–892).** Tolerancia $|\Delta k|\le2\pi/L$. SHG: $\Delta k(\omega_0)=0$,
$|\Delta k(\omega_0+\Delta\omega)|=2\pi/L$, $\Delta k\approx\Delta k'\Delta\omega$ ⇒ $\Delta\omega=2\pi/|\Delta k'|L$ (**recuadros**):

$$\boxed{\Delta\nu=1/|\Delta k'|L}\qquad(21.2\text{-}29)$$

Como $\Delta k=k_3(2\omega)-2k_1(\omega)$, $\Delta k'=2[dk_3(2\omega)/d(2\omega)-dk_1(\omega)/d\omega]=2[1/v_3-1/v_1]$ (velocidades de grupo):

$$\boxed{\Delta\nu=\frac12\Big|\frac L{v_3}-\frac L{v_1}\Big|^{-1}=\frac{c_0}{2L}\frac1{|N_3-N_1|}}\qquad(21.2\text{-}30)$$

$N_1,N_3$ índices de grupo a $\omega$ y $2\omega$. SHG de banda ancha o de pulsos ultracortos (23.5): cristal
delgado (menor eficiencia) o **group‑velocity matching** $N_3\approx N_1$. En SPDC la tolerancia se ve en el
grosor de las curvas de la Fig. 21.2-13.

#### 21.2E Quasi-Phase Matching (p. 892)

Con $\Delta\mathbf k\ne0$, se compensa con un medio de no linealidad periódica en posición (**QPM**). Con
$\mathrm d(\mathbf r)$:

$$I_3\propto\Big|\int_V\mathrm d(\mathbf r)\exp(j\Delta\mathbf k\cdot\mathbf r)\,d\mathbf r\Big|^2\qquad(21.2\text{-}31)$$

Si $\mathrm d(\mathbf r)=\mathrm d_0\exp(-j\mathbf G\cdot\mathbf r)$ con $\mathbf G=\Delta\mathbf k$ se elimina el desajuste (**recuadro**):

$$\boxed{\mathbf k_1+\mathbf k_2+\mathbf G=\mathbf k_3}\qquad(21.2\text{-}32)$$

El medio actúa como red de fase (red de Bragg longitudinal) de vector $\mathbf G$. En la práctica (p. 893)
se fabrican estructuras periódicas (signo alterno); cualquier armónico de Fourier sirve.

**QPM colineal.** $\mathrm d(z)=\sum_{m=-\infty}^{\infty}\mathrm d_m\exp(-j2\pi mz/\Lambda)$; armónico $m$: $G=m2\pi/\Lambda=\Delta k$
(**recuadros**):

$$\boxed{\Lambda=m2\pi/\Delta k=mL_c}\qquad(21.2\text{-}33)\ \text{QPM Condition}$$
$$\boxed{\omega_1+\omega_2=\omega_3,\qquad \omega_1n_1+\omega_2n_2+2\pi mc/\Lambda=\omega_3n_3}\qquad(21.2\text{-}34)\ \text{QPM Tuning Curves}$$

(aquí $c$ debe leerse como $c_0$ para que $2\pi m/\Lambda$ sea un número de onda en vacío multiplicado por $c_0$).
Sustituyen a (21.2-20) y dan flexibilidad de diseño.

**Coeficiente periódicamente invertido (p. 893–894).** $\mathrm d(z)=\pm\mathrm d_0$ alternando cada $\Lambda/2$
(Fig. 21.2-15). Fig. 21.2-16: fasores de los elementos radiantes: (a) phase matched, todos alineados;
(b) desajustados, giran un círculo cada $2\pi/\Delta k$; (c) QPM con $m=1$, $\Lambda=L_c$: cada $\Lambda/2$ se invierte el
signo y se recupera parcialmente la eficiencia. Fourier: $\mathrm d_m=(2/m\pi)\mathrm d_0$ para $m$ impar, 0 si par.
Eficiencia con QPM de orden $m$ $\propto\mathrm d_m^2=(2/\pi m)^2\mathrm d_0^2$. Medio homogéneo con desajuste:
$\mathrm d_0^2\mathrm{sinc}^2(\Delta kL/2\pi)=\mathrm d_0^2\mathrm{sinc}^2(L/L_c)\approx(\mathrm d_0^2/\pi^2)(L_c/L)^2$ para $L\gg L_c$. Como $L_c=\Lambda/m$,
la **mejora es $4(L/\Lambda)^2$** (cuadrado del número de períodos). Fabricación: **poling** (campo eléctrico
periódico litográfico que invierte la polarización permanente) en ferroeléctricos LiTaO₃, KTP, LiNbO₃
→ **PPLN**; también GaAs.

### 21.3 Third-Order Nonlinear Optics (p. 894)

Medios centrosimétricos: $\mathrm d=0$ y (**recuadro**) $\mathcal P_{\rm NL}=4\chi^{(3)}\mathcal E^3$ (21.3-1), **medio Kerr**
(Fig. 21.3-1, p. 895, curva cúbica). Generan terceros armónicos y sumas/diferencias de tripletes.

**EXERCISE 21.3-1 (p. 895) — Medios de tercer orden exhiben el efecto electroóptico Kerr.** Campo
óptico $E(\omega)$ más estático $E(0)$, $|E(\omega)|^2\ll|E(0)|^2$. Mostrar que $P_{\rm NL}(\omega)\approx12\chi^{(3)}E^2(0)E(\omega)$ y que
equivale a $\Delta n=-\tfrac12\mathfrak sn^3E^2(0)$ con

$$\mathfrak s=-\frac{12}{\epsilon_0n^4}\chi^{(3)}\qquad(21.3\text{-}2)$$

(efecto Kerr electroóptico cuadrático, 20.1A; $\mathfrak s$ coeficiente de Kerr).

#### 21.3A Third-Harmonic Generation (THG) and Optical Kerr Effect (p. 895)

Campo monocromático ⇒ $\mathcal P_{\rm NL}$ con componentes a $\omega$ y $3\omega$:

$$P_{\rm NL}(\omega)=3\chi^{(3)}|E(\omega)|^2E(\omega)\quad(21.3\text{-}3a),\qquad P_{\rm NL}(3\omega)=\chi^{(3)}E^3(\omega)\quad(21.3\text{-}3b)$$

**THG**: eficiencia baja; en la práctica se hace SHG + SFG($\omega+2\omega$).

**Efecto Kerr óptico.** La componente a $\omega$ equivale a $\Delta\chi$:

$$\epsilon_0\Delta\chi=\frac{P_{\rm NL}(\omega)}{E(\omega)}=3\chi^{(3)}|E(\omega)|^2=6\chi^{(3)}\eta I\qquad(21.3\text{-}4)$$

con $I=|E(\omega)|^2/2\eta$; $2n\Delta n=\Delta\chi$ ⇒

$$\Delta n=\frac{3\eta}{\epsilon_0n}\chi^{(3)}I\equiv n_2I\qquad(21.3\text{-}5)$$

(**recuadros, p. 896**)

$$\boxed{n_2=\frac{3\eta_0}{n^2\epsilon_0}\chi^{(3)}}\quad(21.3\text{-}6)\ \text{Optical Kerr Coefficient},\qquad \boxed{n(I)=n+n_2I}\quad(21.3\text{-}7)\ \text{Optical Kerr Effect}$$

Efecto autoinducido: la velocidad de fase depende de la propia intensidad (**refracción no lineal**).
Órdenes de magnitud de $n_2$ [cm²/W]: vidrios $10^{-16}$–$10^{-14}$; vidrios dopados $10^{-14}$–$10^{-7}$;
orgánicos $10^{-10}$–$10^{-8}$; semiconductores $10^{-10}$–$10^{-2}$. Depende de la longitud de onda (21.7) y de la
polarización. Nota al pie p. 896: forma alternativa $n(I)=n+n_2|E|^2/2$ con $n_2$ distinto en un factor $\eta$.

#### 21.3B Self-Phase Modulation (SPM), Self-Focusing, and Spatial Solitons (p. 896)

**SPM.** Fase de un haz de potencia $P$, área $A$, distancia $L$: $\varphi=-n(I)k_0L=-2\pi n(I)L/\lambda_0=-2\pi(n+n_2P/A)L/\lambda_0$,
alterada en

$$\Delta\varphi=-2\pi n_2\frac L{\lambda_0A}P\qquad(21.3\text{-}8)$$

Útil para control de luz por luz. Conviene $L$ grande y $A$ pequeño → guías de onda. Potencia para
$\Delta\varphi=-\pi$: $P_\pi=\lambda_0A/2Ln_2$. Ejemplo: fibra de vidrio dopado $L=1$ m, $A=10^{-2}$ mm², $n_2=10^{-10}$ cm²/W,
$\lambda_0=1$ μm ⇒ $P_\pi=0.5$ W. Con guías de canal de cm y $n_2$ mayor, $\pi$ con pocos mW. Conversión fase→intensidad
(20.1B): interferómetro (Mach–Zehnder), birrefringencia entre polarizadores cruzados, acoplador
direccional (8.5B) → modulador todo‑óptico, conmutadores (23.3C).

**Autoenfoque (p. 897).** Lámina delgada de medio Kerr: $\Delta n$ reproduce el perfil de intensidad
transversal → medio GRIN → curvatura de frente de onda → **lente con focal dependiente de la potencia**
(Fig. 21.3-2). Kerr‑lens mode locking (15.4D).

**EXERCISE 21.3-2 (p. 897) — Lente Kerr.** Lámina de espesor $d$, transmitancia $\exp(-jnk_0d)$, frente plano,
$I\approx I_0[1-(x^2+y^2)/W^2]$ cerca del eje ($x,y\ll W$). Mostrar que actúa como lente delgada de focal
inversamente proporcional a $I_0$. Pista: lente de focal $f$ tiene transmitancia $\propto\exp[jk_0(x^2+y^2)/2f]$
(2.4-9), Ejercicio 2.4-6.

**Solitones espaciales (p. 897–898).** En medio grueso, el haz crea su propia guía GRIN; si su perfil
coincide con un modo de esa guía, se propaga sin cambiar: **difracción compensada por SPM**. Análogo
temporal: GVD compensada por SPM → solitones temporales (22.5B). Helmholtz no lineal
$\nabla^2E+n^2(I)k_0^2E=0$, $n(I)=n+n_2I$, $I=|E|^2/2\eta$, $k_0=\omega/c_0$. Con $E=A(x,z)e^{-jkz}$, $k=nk_0$, envolvente
lenta en $z$, sin variación en $y$:

$$\frac{\partial^2A}{\partial x^2}-2jk\frac{\partial A}{\partial z}+k_0^2[n^2(I)-n^2]A=0\qquad(21.3\text{-}9)$$
$$[n^2(I)-n^2]\approx[n_2I][2n]=\frac{2n_2n|A|^2}{2\eta}=\frac{n^2n_2}{\eta_0}|A|^2\qquad(21.3\text{-}10)$$
$$\frac{\partial^2A}{\partial x^2}+\frac{n_2}{\eta_0}k^2|A|^2A=2jk\frac{\partial A}{\partial z}\qquad(21.3\text{-}11)\ \textbf{(Nonlinear Schrödinger Equation)}$$

Una solución (**recuadro**):

$$\boxed{A(x,z)=A_0\,\mathrm{sech}\Big(\frac x{W_0}\Big)\exp\Big(-j\frac z{4z_0}\Big)}\qquad(21.3\text{-}12)\ \text{Spatial Soliton}$$

con $n_2(A_0^2/2\eta_0)=1/k^2W_0^2$ y $z_0=\tfrac12kW_0^2=\pi W_0^2/\lambda$ (rango de Rayleigh). Intensidad

$$I(x,z)=\frac{|A(x,z)|^2}{2\eta}=\frac{A_0^2}{2\eta}\mathrm{sech}^2\Big(\frac x{W_0}\Big)\qquad(21.3\text{-}13)$$

independiente de $z$, ancho $W_0$ (Fig. 21.3-3: gaussiano que difracta vs solitón). Es el modo de la guía
GRIN $n+n_2I=n[1+(1/k^2W_0^2)\mathrm{sech}^2(x/W_0)]$. Constante de propagación $k+1/4z_0=k(1+\lambda^2/8\pi^2W_0^2)$,
velocidad de fase $c/(1+\lambda^2/8\pi^2W_0^2)$ (< $c$, →$c$ si $W_0$ grande).

**Ganancia Raman (p. 898–899).** $\chi^{(3)}=\chi_R^{(3)}+j\chi_I^{(3)}$ complejo ⇒ SPM compleja:

$$\Delta\varphi=2\pi n_2\frac L{\lambda_0A}P=\frac{6\pi\eta_0}{\epsilon_0}\frac{\chi^{(3)}}{n^2}\frac L{\lambda_0A}P\qquad(21.3\text{-}14)$$

$\exp(-j\varphi)$ = fase $\Delta\varphi=(6\pi\eta_0/\epsilon_0)(\chi_R^{(3)}/n^2)(L/\lambda_0A)P$ × ganancia $\exp(\tfrac12\gamma_RL)$ (**recuadro**):

$$\boxed{\gamma_R=\frac{12\pi\eta_0}{\epsilon_0}\frac{\chi_I^{(3)}}{n^2}\frac1{\lambda_0}\frac PA}\qquad(21.3\text{-}15)\ \text{Raman Gain Coefficient}$$

Proporcional a $P$; origen en el acoplo con modos vibracionales (fuente de energía). Ganancia > pérdida
→ amplificador Raman (14.3D); con realimentación, láser Raman (15.3A). Análogo a la susceptibilidad
compleja lineal (5.5).

#### 21.3C Cross-Phase Modulation (XPM) (p. 899)

Dos ondas $\omega_1,\omega_2$:

$$P_{\rm NL}(\omega_1)=\chi^{(3)}[3|E(\omega_1)|^2+6|E(\omega_2)|^2]E(\omega_1)\qquad(21.3\text{-}16)$$

Con $P_{\rm NL}(\omega_1)=2\epsilon_0n\Delta nE(\omega_1)$ (**recuadro**):

$$\boxed{\Delta n=n_2(I_1+2I_2)}\qquad(21.3\text{-}17)\ \text{XPM}$$

$n_2=3\eta_0\chi^{(3)}/\epsilon_0n^2$, $I_q=|E(\omega_q)|^2/2\eta$. La onda 2 modula la fase de la 1 (factor 2 respecto a SPM).
Contaminación entre canales WDM (24.3C). Two‑wave mixing no es posible en $\chi^{(2)}$ salvo degenerado, pero
sí en medios fotorrefractivos (Fig. 20.4-3) (p. 900).

**EXERCISE 21.3-3 (p. 900) — Kerr con tres ondas.** Determinar $P_{\rm NL}(\omega_1)$ y mostrar que la onda 1
viaja a $c_0/(n+\Delta n)$ con

$$\Delta n=n_2(I_1+2I_2+2I_3)\qquad(21.3\text{-}18)$$

#### 21.3D Four-Wave Mixing (FWM) (p. 900)

Tres ondas $\omega_1,\omega_2,\omega_3$ (21.3-19); se escribe como suma de seis términos

$$\mathcal E(t)=\sum_{q=\pm1,\pm2,\pm3}\tfrac12E(\omega_q)\exp(j\omega_qt)\qquad(21.3\text{-}20),\quad \omega_{-q}=-\omega_q,\ E(-\omega_q)=E^*(\omega_q)$$

$$\mathcal P_{\rm NL}(t)=\tfrac12\chi^{(3)}\sum_{q,r,l=\pm1,\pm2,\pm3}E(\omega_q)E(\omega_r)E(\omega_l)\exp[j(\omega_q+\omega_r+\omega_l)t]\qquad(21.3\text{-}21)$$

($6^3=216$ términos). *Nota de lectura:* en el escaneo el prefactor de (21.3-21) parece "1/8"; por
consistencia con $4\chi^{(3)}(\tfrac12)^3=\tfrac12\chi^{(3)}$, con (21.3-22) y con (21.5-3) debe ser $\tfrac12\chi^{(3)}$.
Componentes a $\omega_1,\dots,3\omega_1,\dots,2\omega_1\pm\omega_2,\dots,\pm\omega_1\pm\omega_2\pm\omega_3$. Para $\omega_1+\omega_2-\omega_3$ hay seis permutaciones:

$$P_{\rm NL}(\omega_1+\omega_2-\omega_3)=6\chi^{(3)}E(\omega_1)E(\omega_2)E^*(\omega_3)\qquad(21.3\text{-}22)$$

Se mezclan cuatro ondas si $\omega_4=\omega_1+\omega_2-\omega_3$ (**recuadros**):

$$\boxed{\omega_1+\omega_2=\omega_3+\omega_4}\ (21.3\text{-}23)\ \text{Frequency-Matching},\qquad \boxed{\mathbf k_1+\mathbf k_2=\mathbf k_3+\mathbf k_4}\ (21.3\text{-}25)\ \text{Phase-Matching}$$

(de (21.3-24): $P_{\rm NL}(\omega_4)\propto\exp[-j(\mathbf k_1+\mathbf k_2-\mathbf k_3)\cdot\mathbf r]$, p. 901). Varios procesos FWM simultáneos:
p. ej. 3, 4 y 1 generan 2:

$$P_{\rm NL}(\omega_2)=6\chi^{(3)}E(\omega_3)E(\omega_4)E^*(\omega_1)\qquad(21.3\text{-}26)$$

Fotones: $\hbar\omega_3+\hbar\omega_4\to\hbar\omega_1+\hbar\omega_2$ (Fig. 21.3-4: paralelogramo de $\mathbf k$ y diagrama de fotones).

**Mezcla de tres ondas en $\chi^{(3)}$ (p. 901–902).** Parcialmente degenerado $\omega_3=\omega_4\equiv\omega_0$:

$$\omega_1+\omega_2=2\omega_0\qquad(21.3\text{-}27)$$

($\omega_1,\omega_2$ simétricas respecto a $\omega_0$, como bandas laterales AM o Stokes/anti‑Stokes).

$$P_{\rm NL}(\omega_1)=3\chi^{(3)}E^2(\omega_3)E^*(\omega_2)\ (21.3\text{-}28a),\quad P_{\rm NL}(\omega_2)=3\chi^{(3)}E^2(\omega_3)E^*(\omega_1)\ (b),\quad P_{\rm NL}(\omega_3)=6\chi^{(3)}E(\omega_1)E(\omega_2)E^*(\omega_3)\ (c)$$

Permiten OFC, OPA, OPO, SPDC en medios $\chi^{(3)}$ (señal, idler, bomba), pero con **cuatro fotones**
(dos de bomba $\omega_0$ → $\omega_1+\omega_2$). Fig. 21.3-5: OPA en fibra de sílice (señal $\omega_1$ + bomba $\omega_0$ → señal
amplificada + idler $\omega_2$).

#### 21.3E Optical Phase Conjugation (OPC) (p. 902)

**FWM degenerado**: $\omega_1=\omega_2=\omega_3=\omega_4=\omega$ (21.3-29). Ondas 3 y 4 planas contrapropagantes:
$E_3=A_3\exp(-j\mathbf k_3\cdot\mathbf r)$, $E_4=A_4\exp(-j\mathbf k_4\cdot\mathbf r)$ (21.3-30), $\mathbf k_4=-\mathbf k_3$ (21.3-31). En (21.3-26):
$P_{\rm NL}(2)=6\chi^{(3)}A_3A_4E_1^*(\mathbf r)$ (**recuadro**):

$$\boxed{E_2(\mathbf r)\propto A_3A_4E_1^*(\mathbf r)}\qquad(21.3\text{-}32)\ \text{Phase Conjugation}$$

Ondas 3, 4: **bombas**; 1: **sonda** (probe); 2: **conjugada**. Espejo especial que refleja la onda sobre sí
misma sin alterar sus frentes.

- **EXAMPLE 21.3-1 (p. 903) — Conjugada de onda plana.** $E_1=A_1e^{-j\mathbf k_1\cdot\mathbf r}$ ⇒ $E_2=A_1^*e^{+j\mathbf k_1\cdot\mathbf r}$:
  onda plana en dirección $\mathbf k_2=-\mathbf k_1$ (cumple (21.3-25)), cualquiera sea el ángulo de incidencia
  (Fig. 21.3-6: espejo ordinario vs conjugador).
- **EXAMPLE 21.3-2 (p. 903) — Conjugada de onda esférica.** $E_1\propto(1/r)e^{-jkr}$ ⇒ $E_2\propto(1/r)e^{+jkr}$:
  esférica que retrocede y converge al origen (Fig. 21.3-7).

Toda sonda = superposición de ondas planas ⇒ la conjugada retrocede sobre la original con los mismos
frentes. Equivale a **inversión temporal**: $\mathcal E_2(\mathbf r,t)\propto\mathrm{Re}\{E_1^*e^{j\omega t}\}=\mathrm{Re}\{E_1e^{-j\omega t}\}$, es
decir $t\to-t$. Puede llevar **más potencia** que la sonda ($I_2\propto I_3I_4$): "espejo amplificador".
Fig. 21.3-8 (p. 904): montaje con un láser, divisor de haz y dos espejos para las bombas 3 y 4
contrapropagantes, sonda 1, conjugada 2 generada en el cristal.

**FWM degenerado como holografía en tiempo real (p. 903–904).** Holografía (4.5): objeto $E_1$ +
referencia $E_3$ graban; $E_4$ reconstruye $E_2\propto E_4E_3E_1^*$ (conjugada) o $E_2\propto E_4E_1E_3^*$ (réplica).
En el medio no lineal (Kerr o fotorrefractivo, 20.4) grabación y lectura son simultáneas. Dos redes
(Fig. 21.3-9): (a) **red de transmisión**: 1 + 3 interfieren, 4 se refleja por Bragg → 2; (b) **red de
reflexión**: 1 + 4 interfieren, 3 se refleja → 2. Coexisten con eficiencias distintas.

**Restauración de frentes de onda (p. 904–905).** Reciprocidad (Fig. 21.3-10): los rayos recorren el
mismo camino en sentido inverso. Un conjugador refleja la onda distorsionada sobre sí misma y al
atravesar de nuevo el medio aberrante se corrige (Fig. 21.3-11). Resonador con un espejo conjugado
(Fig. 21.3-12): la distorsión se cancela en cada ida y vuelta y los modos salen sin aberrar por el espejo
ordinario.

### *21.4 Second-Order Nonlinear Optics: Coupled-Wave Theory (p. 905)

**Resumen.** Tres ondas en pie de igualdad (a diferencia de 21.2). Isotropía y no dispersión (ver 21.6, 21.7).

#### Ecuaciones de ondas acopladas (p. 905–907)

$\nabla^2\mathcal E-(1/c^2)\partial^2\mathcal E/\partial t^2=-\mathcal S$ (21.4-1), $\mathcal S=-\mu_0\partial^2\mathcal P_{\rm NL}/\partial t^2$ (21.4-2), $\mathcal P_{\rm NL}=2\mathrm d\mathcal E^2$ (21.4-3).

$$\mathcal E(t)=\sum_{q=1,2,3}\mathrm{Re}\{E_qe^{j\omega_qt}\}=\sum_{q=1,2,3}\tfrac12[E_qe^{j\omega_qt}+E_q^*e^{-j\omega_qt}]\ (21.4\text{-}4)=\sum_{q=\pm1,\pm2,\pm3}\tfrac12E_qe^{j\omega_qt}\ (21.4\text{-}5)$$

$\omega_{-q}=-\omega_q$, $E_{-q}=E_q^*$. $6\times6=36$ términos:

$$\mathcal P_{\rm NL}(t)=2\mathrm d\cdot\tfrac14\sum_{q,r=\pm1,\pm2,\pm3}E_qE_r\exp[j(\omega_q+\omega_r)t]\qquad(21.4\text{-}6)$$
$$\mathcal S=\tfrac12\mu_0\mathrm d\sum_{q,r}(\omega_q+\omega_r)^2E_qE_r\exp[j(\omega_q+\omega_r)t]\qquad(21.4\text{-}7)$$

Igualando términos de cada frecuencia (si son distintas): tres Helmholtz con fuente

$$(\nabla^2+k_1^2)E_1=-S_1,\quad(\nabla^2+k_2^2)E_2=-S_2,\quad(\nabla^2+k_3^2)E_3=-S_3\qquad(21.4\text{-}8a,b,c),\quad k_q=n\omega_q/c_0$$

Si $\mathrm d=0$ se desacoplan. Si las frecuencias **no son conmensurables** no hay componentes de $\mathcal S$ a
$\omega_1,\omega_2,\omega_3$ y no interactúan (p. 907). Con $\omega_1+\omega_2=\omega_3$ (21.4-9), de los 36 términos:

$$S_1=2\mu_0\omega_1^2\mathrm d\,E_3E_2^*\ (21.4\text{-}10),\quad S_2=2\mu_0\omega_2^2\mathrm d\,E_3E_1^*\ (21.4\text{-}11),\quad S_3=2\mu_0\omega_3^2\mathrm d\,E_1E_2\ (21.4\text{-}12)$$

(**recuadro**, 3‑Wave‑Mixing Coupled Equations):

$$\boxed{(\nabla^2+k_1^2)E_1=-2\mu_0\omega_1^2\mathrm d\,E_3E_2^*,\quad(\nabla^2+k_2^2)E_2=-2\mu_0\omega_2^2\mathrm d\,E_3E_1^*,\quad(\nabla^2+k_3^2)E_3=-2\mu_0\omega_3^2\mathrm d\,E_1E_2}\quad(21.4\text{-}13a,b,c)$$

**EXERCISE 21.4-1 (p. 907) — SHG como mezcla degenerada.** Con $\omega_1=\omega_2=\omega$, $\omega_3=2\omega$ hay dos ondas
$E_1,E_3$. Mostrar que $S_1=2\mu_0\omega_1^2\mathrm dE_3E_1^*$ (21.4-14), $S_3=\mu_0\omega_3^2\mathrm dE_1E_1$ (21.4-15) (**recuadro**):

$$\boxed{(\nabla^2+k_1^2)E_1=-2\mu_0\omega_1^2\mathrm d\,E_3E_1^*,\qquad(\nabla^2+k_3^2)E_3=-\mu_0\omega_3^2\mathrm d\,E_1E_1}\qquad(21.4\text{-}16a,b)$$

Nota: **no** se obtienen de (21.4-13) poniendo $E_1=E_2$ (falta el factor 2 en (21.4-16b)).

#### Mezcla de tres ondas planas colineales (p. 908)

$E_q=A_q\exp(-jk_qz)$, $k_q=\omega_q/c$. Variables normalizadas $\mathfrak a_q=A_q/(2\eta\hbar\omega_q)^{1/2}$:

$$E_q=\sqrt{2\eta\hbar\omega_q}\,\mathfrak a_q\exp(-jk_qz),\ q=1,2,3\qquad(21.4\text{-}17)$$
$$I_q=|E_q|^2/2\eta=\hbar\omega_q|\mathfrak a_q|^2,\qquad \phi_q=\frac{I_q}{\hbar\omega_q}=|\mathfrak a_q|^2\qquad(21.4\text{-}18)$$

$|\mathfrak a_q|^2$ = **densidad de flujo de fotones**. Aproximación de envolvente lentamente variable
($d^2\mathfrak a_q/dz^2\ll k_qd\mathfrak a_q/dz$):

$$(\nabla^2+k_q^2)[\mathfrak a_q\exp(-jk_qz)]\approx-j2k_q\frac{d\mathfrak a_q}{dz}\exp(-jk_qz)\qquad(21.4\text{-}19)$$

(**recuadro**, 3‑Wave‑Mixing Coupled Equations):

$$\boxed{\frac{d\mathfrak a_1}{dz}=-j\mathfrak g\,\mathfrak a_3\mathfrak a_2^*e^{-j\Delta kz},\quad\frac{d\mathfrak a_2}{dz}=-j\mathfrak g\,\mathfrak a_3\mathfrak a_1^*e^{-j\Delta kz},\quad\frac{d\mathfrak a_3}{dz}=-j\mathfrak g\,\mathfrak a_1\mathfrak a_2e^{j\Delta kz}}\quad(21.4\text{-}20a,b,c)$$
$$\mathfrak g^2=2\hbar\omega_1\omega_2\omega_3\eta^3\mathrm d^2\qquad(21.4\text{-}21),\qquad\Delta k=k_3-k_2-k_1\qquad(21.4\text{-}22)$$

**EXERCISE 21.4-2 (p. 909) — Conservación del número de fotones (Manley–Rowe).** Con (21.4-20) mostrar

$$\frac d{dz}|\mathfrak a_1|^2=\frac d{dz}|\mathfrak a_2|^2=-\frac d{dz}|\mathfrak a_3|^2\qquad(21.4\text{-}23)$$

de donde sale (21.2-19); $|\mathfrak a_1|^2+|\mathfrak a_3|^2$ y $|\mathfrak a_2|^2+|\mathfrak a_3|^2$ son invariantes.

**EXERCISE 21.4-3 (p. 909) — Conservación de energía.** Mostrar que $\sum I_q$, $I_q=\hbar\omega_q|\mathfrak a_q|^2$, es
invariante: $\frac d{dz}(I_1+I_2+I_3)=0$ (21.4-24).

#### 21.4A Second-Harmonic Generation (SHG) (p. 909)

$\omega_1=\omega_2=\omega$, $\omega_3=2\omega$ (21.4-25); momento: $2\mathbf k_1=\mathbf k_3$ (21.4-26).

**EXERCISE 21.4-4 (p. 909) — Ecuaciones acopladas de SHG.** Aplicar (21.4-19) a (21.4-16):

$$\frac{d\mathfrak a_1}{dz}=-j\mathfrak g\,\mathfrak a_3\mathfrak a_1^*e^{-j\Delta kz}\ (21.4\text{-}27a),\qquad\frac{d\mathfrak a_3}{dz}=-j\frac{\mathfrak g}2\mathfrak a_1\mathfrak a_1e^{j\Delta kz}\ (21.4\text{-}27b)$$

$\Delta k=k_3-2k_1$, $\mathfrak g^2=4\hbar\omega^3\eta^3\mathrm d^2$ (21.4-28).

Con $\Delta k=0$ (**recuadro, p. 910**):

$$\boxed{\frac{d\mathfrak a_1}{dz}=-j\mathfrak g\,\mathfrak a_3\mathfrak a_1^*,\qquad\frac{d\mathfrak a_3}{dz}=-j\frac{\mathfrak g}2\mathfrak a_1\mathfrak a_1}\qquad(21.4\text{-}29a,b)$$

Condiciones $\mathfrak a_3(0)=0$, $\mathfrak a_1(0)$ real; buscando $\mathfrak a_1$ real y usando $\mathfrak a_1^2(z)+2|\mathfrak a_3(z)|^2=\mathfrak a_1^2(0)$:
$d\mathfrak a_3/dz=-j(\mathfrak g/2)[\mathfrak a_1^2(0)-2|\mathfrak a_3|^2]$ (21.4-30) ⇒

$$\mathfrak a_1(z)=\mathfrak a_1(0)\,\mathrm{sech}\Big(\tfrac1{\sqrt2}\mathfrak g\mathfrak a_1(0)z\Big)\ (21.4\text{-}31a),\qquad\mathfrak a_3(z)=-\frac j{\sqrt2}\mathfrak a_1(0)\tanh\Big(\tfrac1{\sqrt2}\mathfrak g\mathfrak a_1(0)z\Big)\ (21.4\text{-}31b)$$

(**recuadro**)

$$\boxed{\phi_1(z)=\phi_1(0)\,\mathrm{sech}^2\frac{\gamma z}2,\qquad\phi_3(z)=\tfrac12\phi_1(0)\tanh^2\frac{\gamma z}2}\qquad(21.4\text{-}32a,b)$$

$\gamma/2=\mathfrak g\mathfrak a_1(0)/\sqrt2$:

$$\gamma^2=2\mathfrak g^2\mathfrak a_1^2(0)=2\mathfrak g^2\phi_1(0)=8\mathrm d^2\eta^3\hbar\omega^3\phi_1(0)=8\mathrm d^2\eta^3\omega^2I_1(0)\qquad(21.4\text{-}33)$$

$\phi_1+2\phi_3=\phi_1(0)$: cada dos fotones de $\omega$ dan uno de $2\omega$ (Fig. 21.4-1: esquema, curvas $\phi_1,\phi_3$ vs $\gamma z$,
fotones).

**Eficiencia de SHG (p. 910–911).**

$$\eta_{\rm SHG}=\frac{I_3(L)}{I_1(0)}=\frac{\hbar\omega_3\phi_3(L)}{\hbar\omega_1\phi_1(0)}=\frac{2\phi_3(L)}{\phi_1(0)}=\tanh^2\frac{\gamma L}2\qquad(21.4\text{-}34)$$

Para $\gamma L$ grande → 1 (toda la potencia a $2\omega$). Para $\gamma L$ pequeño, $\tanh x\approx x$:

$$\eta_{\rm SHG}\approx\tfrac14\gamma^2L^2=\tfrac12\mathfrak g^2L^2\phi_1(0)=2\mathrm d^2\eta^3\hbar\omega^3L^2\phi_1(0)=2\mathrm d^2\eta^3\omega^2L^2I_1(0)\qquad(21.4\text{-}35)$$

(**recuadro**)

$$\boxed{\eta_{\rm SHG}=C^2\frac{L^2}AP,\qquad C^2=2\omega^2\eta_0^3\frac{\mathrm d^2}{n^3}}\qquad(21.4\text{-}36)\ \text{SHG Efficiency}$$

$P=I_1(0)A$. Reproduce (21.2-6); **figura de mérito $\mathrm d^2/n^3$** para comparar materiales.

**EXAMPLE 21.4-1 (p. 911) — Eficiencia de SHG.** $\mathrm d^2/n^3=10^{-46}$ C²/V⁴ (Tabla 21.6-3), $\lambda=1$ μm ⇒
$C^2=38\times10^{-9}$ W⁻¹ $=0.038$ (MW)⁻¹. Eficiencia 10 % si $PL^2/A=2.63$ MW; con $L^2/A=10^6$ ($L=1$ cm,
$A=100$ μm²) se necesita $P=2.63$ W, $P/A=2.63\times10^6$ W/cm².

**Desajuste de fase en SHG (p. 911–912).** Acoplo débil $\gamma L\ll1$, $\mathfrak a_1\approx\mathfrak a_1(0)$:

$$\mathfrak a_3(L)=-j\frac{\mathfrak g}2\mathfrak a_1^2(0)\int_0^Le^{j\Delta kz}dz=-\Big(\frac{\mathfrak g}{2\Delta k}\Big)\mathfrak a_1^2(0)[e^{j\Delta kL}-1]\qquad(21.4\text{-}37)$$

$\phi_3(L)=(\mathfrak g/\Delta k)^2\phi_1^2(0)\sin^2(\Delta kL/2)$ ⇒

$$\eta_{\rm SHG}=\frac{I_3(L)}{I_1(0)}=\frac{2\phi_3(L)}{\phi_1(0)}=C^2\frac{L^2}AP\,\mathrm{sinc}^2(\Delta kL/2\pi)\qquad(21.4\text{-}38)$$

Confirma Fig. 21.2-14; eficiente para $L<L_c=2\pi/|\Delta k|$.

#### 21.4B Optical Frequency Conversion (OFC) (p. 912)

Up‑converter: $\omega_1$ (señal) + $\omega_2$ (bomba) → $\omega_3$. Con $\Delta k=0$ y bomba no agotada $\mathfrak a_2(z)\approx\mathfrak a_2(0)$
(**recuadro**):

$$\boxed{\frac{d\mathfrak a_1}{dz}=-j\frac\gamma2\mathfrak a_3,\qquad\frac{d\mathfrak a_3}{dz}=-j\frac\gamma2\mathfrak a_1}\qquad(21.4\text{-}39a,b),\qquad\gamma=2\mathfrak g\mathfrak a_2(0)$$

$$\mathfrak a_1(z)=\mathfrak a_1(0)\cos\frac{\gamma z}2\ (21.4\text{-}40a),\qquad\mathfrak a_3(z)=-j\mathfrak a_1(0)\sin\frac{\gamma z}2\ (21.4\text{-}40b)$$

(**recuadro**)

$$\boxed{\phi_1(z)=\phi_1(0)\cos^2\frac{\gamma z}2,\qquad\phi_3(z)=\phi_1(0)\sin^2\frac{\gamma z}2}\qquad(21.4\text{-}41a,b)$$

Intercambio periódico de fotones (Fig. 21.4-2, p. 913): en $0<z<\pi/\gamma$ la señal se convierte; en
$\pi/\gamma<z<2\pi/\gamma$ los fotones $\omega_3$ se desintegran en $\omega_1+\omega_2$.

$$\eta_{\rm OFC}=\frac{I_3(L)}{I_1(0)}=\frac{\omega_3}{\omega_1}\sin^2\frac{\gamma L}2\qquad(21.4\text{-}42)$$

Para $\gamma L\ll1$: $I_3/I_1\approx(\omega_3/\omega_1)(\gamma L/2)^2=(\omega_3/\omega_1)\mathfrak g^2L^2\phi_2(0)=2\omega_3^2L^2\mathrm d^2\eta^3I_2(0)$ (**recuadro**):

$$\boxed{\eta_{\rm OFC}=C^2\frac{L^2}AP_2,\qquad C^2=2\omega_3^2\eta_0^3\frac{\mathrm d^2}{n^3}}\qquad(21.4\text{-}43)\ \text{OFC Efficiency}$$

$P_2=I_2(0)A$ potencia de bomba.

**EXERCISE 21.4-5 (p. 913) — Up‑conversion infrarroja.** Proustita ($\mathrm d=1.5\times10^{-22}$ C/V², $n=2.6$,
$\mathrm d^2/n^3=1.3\times10^{-45}$ C²/V⁴); señal CO₂ 10.6 μm; bomba Nd³⁺:YAG 1 W a 1.06 μm enfocada a $10^{-2}$ mm².
Hallar la longitud de onda convertida y la eficiencia si colineales con $L=1$ cm.
*Cálculo propio:* $\lambda_3=(1/10.6+1/1.06)^{-1}=0.964$ μm; $\omega_3=1.95\times10^{15}$ s⁻¹; $C^2=2\omega_3^2\eta_0^3\mathrm d^2/n^3\approx5.3\times10^{-7}$ W⁻¹;
$L^2/A=10^{-4}/10^{-8}=10^4$ ⇒ $\eta_{\rm OFC}\approx5.3\times10^{-3}$ (≈0.5 %).

#### 21.4C Optical Parametric Amplification (OPA) and Oscillation (OPO) (p. 914)

**OPA.** Onda 1 = señal (débil, $I_1(0)$), 3 = bomba (intensa), 2 = idler (creada). Fig. 21.4-3. Con $\Delta k=0$
y $\mathfrak a_3\approx\mathfrak a_3(0)$ (**recuadro**):

$$\boxed{\frac{d\mathfrak a_1}{dz}=-j\frac\gamma2\mathfrak a_2^*,\qquad\frac{d\mathfrak a_2}{dz}=-j\frac\gamma2\mathfrak a_1^*}\qquad(21.4\text{-}44a,b),\qquad\gamma=2\mathfrak g\mathfrak a_3(0)$$

$$\mathfrak a_1(z)=\mathfrak a_1(0)\cosh\frac{\gamma z}2-j\mathfrak a_2^*(0)\sinh\frac{\gamma z}2\ (21.4\text{-}45a),\qquad\mathfrak a_2(z)=-j\mathfrak a_1^*(0)\sinh\frac{\gamma z}2+\mathfrak a_2(0)\cosh\frac{\gamma z}2\ (21.4\text{-}45b)$$

Con $\mathfrak a_2(0)=0$ (**recuadro**):

$$\boxed{\phi_1(z)=\phi_1(0)\cosh^2\frac{\gamma z}2,\qquad\phi_2(z)=\phi_1(0)\sinh^2\frac{\gamma z}2}\qquad(21.4\text{-}46a,b)$$

Ambas crecen monótonamente hasta que se agota la bomba. Ganancia $G=\phi_1(L)/\phi_1(0)=\cosh^2(\gamma L/2)$;
para $\gamma L\gg1$, $G\approx e^{\gamma L}/4$. $\gamma=2\mathfrak g\mathfrak a_3(0)=2\mathrm d\sqrt{2\hbar\omega_1\omega_2\omega_3\eta^3}\,\mathfrak a_3(0)$ (**recuadro, p. 915**):

$$\boxed{\gamma=2C\sqrt{I_3(0)}=2C\sqrt{P_3/A},\qquad C^2=2\omega_1\omega_2\eta_0^3\frac{\mathrm d^2}{n^3}}\qquad(21.4\text{-}47)\ \text{OPA Gain Coefficient}$$

Fotón de bomba $\hbar\omega_3$ → $\hbar\omega_1$ (amplifica la señal) + $\hbar\omega_2$ (idler).

**EXERCISE 21.4-6 (p. 915) — Ganancia de un OPA.** Amplificar 2.5 μm con KTP de 2 cm bombeado por Nd:YAG
1.064 μm. Hallar $\lambda$ del idler y $C$ de (21.4-47); elegir potencia de bomba y área tal que la ganancia total sea
3 dB. $n=1.75$, $\mathrm d=2.3\times10^{-23}$ C/V².
*Cálculo propio:* $\lambda_2=(1/1.064-1/2.5)^{-1}=1.85$ μm; $C^2\approx8\times10^{-9}$ W⁻¹, $C\approx9\times10^{-5}$ W^{-1/2};
$\cosh^2(\gamma L/2)=2$ ⇒ $\gamma L/2=0.881$ ⇒ $\gamma=88$ m⁻¹ ⇒ $P_3/A=(\gamma/2C)^2\approx2.4\times10^{11}$ W/m²; p. ej. $A=100$ μm² ⇒ $P_3\approx24$ W.

**OPO (p. 915–917).** Realimentación en señal (**SRO**, singly resonant) o en señal e idler (**DRO**, doubly
resonant), Fig. 21.4-4. Frecuencias: $\omega_1+\omega_2=\omega_3$, $n_1\omega_1+n_2\omega_2=n_3\omega_3$ (colineal) **y** coincidencia con
modos del resonador (15.1B): sistema sobredeterminado, sobre todo en DRO. Umbral: ganancia = pérdida
de espejos en un viaje de ida y vuelta.

*SRO (p. 916).* $\mathfrak a_1(L)\mathfrak r_1^2=\mathfrak a_1(0)$ ($\mathfrak r_1$ reflectancia de amplitud, espejos idénticos, fase múltiplo
de $2\pi$); con (21.4-45a) y $\mathfrak a_2(0)=0$: $\mathfrak r_1^2\cosh(\gamma L/2)=1$ ⇒

$$\mathcal R_1^2\cosh^2(\gamma L/2)=1\qquad(21.4\text{-}48),\qquad\mathcal R_1=\mathfrak r_1^2$$

Como $\mathcal R_1\lesssim1$, $\gamma L/2\ll1$, $\cosh^2x\approx1+x^2$ ⇒ $(\gamma L/2)^2\approx(1-\mathcal R_1^2)/\mathcal R_1^2$; con (21.4-47) (**recuadro**):

$$\boxed{P_3|_{\rm threshold}(0)\approx\frac1{C^2}\frac A{L^2}\frac{1-\mathcal R_1^2}{\mathcal R_1^2}}\qquad(21.4\text{-}49)\ \text{SRO Threshold Pump Power}$$

$C^2=2\omega_1\omega_2\eta_0^3\mathrm d^2/n^3$. Ejemplo: $L^2/A=10^6$, $C^2=10^{-7}$ W⁻¹, $\mathcal R_1=0.9$ ⇒ $P_3|_{\rm th}\approx2.3$ W.

*DRO (p. 916).* $\mathfrak a_1(L)\mathfrak r_1^2=\mathfrak a_1(0)$ y $\mathfrak a_2(L)\mathfrak r_2^2=\mathfrak a_2(0)$; con (21.4-45a,b) y conjugando la segunda
(tal como aparece en el libro, con $z=L$):

$$(1-\mathcal R_1)\cosh\frac{\gamma z}2\,\mathfrak a_1(0)+j\mathcal R_1\sinh\frac{\gamma z}2\,\mathfrak a_2^*(0)=0\ (21.4\text{-}50a),\qquad -j\mathcal R_2\sinh\frac{\gamma z}2\,\mathfrak a_1(0)+(1-\mathcal R_2)\cosh\frac{\gamma z}2\,\mathfrak a_2^*(0)=0\ (21.4\text{-}50b)$$

$\mathcal R_1=\mathfrak r_1^2$, $\mathcal R_2=\mathfrak r_2^2$ reflectancias de intensidad a señal e idler. Igualando $\mathfrak a_1(0)/\mathfrak a_2^*(0)$:

$$\tanh^2(\gamma L/2)=(1-\mathcal R_1)(1-\mathcal R_2)/(\mathcal R_1\mathcal R_2)\qquad(21.4\text{-}51)$$

$\tanh x\approx x$ ⇒ (**recuadro**):

$$\boxed{P_3|_{\rm threshold}(0)\approx\frac1{C^2}\frac A{L^2}\frac{(1-\mathcal R_1)(1-\mathcal R_2)}{\mathcal R_1\mathcal R_2}}\qquad(21.4\text{-}52)\ \text{DRO Threshold Pump Power}$$

Cociente DRO/SRO $=(\mathcal R_1/\mathcal R_2)(1-\mathcal R_2)/(1+\mathcal R_1)\approx(1-\mathcal R_2)/2$ (pequeño): el DRO tiene umbral mucho
menor, pero es más sensible a fluctuaciones de longitud (señal **e** idler deben coincidir con modos):
pobre estabilidad, espectros "con picos" (p. 917).

### *21.5 Third-Order Nonlinear Optics: Coupled-Wave Theory (p. 917)

#### 21.5A Four-Wave Mixing (FWM) (p. 917)

$$\mathcal E(t)=\sum_{q=1,2,3,4}\mathrm{Re}[E_qe^{j\omega_qt}]=\sum_{q=\pm1,\dots,\pm4}\tfrac12E_qe^{j\omega_qt}\ (21.5\text{-}1),\qquad\mathcal P_{\rm NL}=4\chi^{(3)}\mathcal E^3\ (21.5\text{-}2)$$
$$\mathcal S=\tfrac12\mu_0\chi^{(3)}\sum_{q,p,r=\pm1,\dots,\pm4}(\omega_q+\omega_p+\omega_r)^2E_qE_pE_r\exp[j(\omega_q+\omega_p+\omega_r)t]\qquad(21.5\text{-}3)$$

($8^3=512$ términos). $(\nabla^2+k_q^2)E_q=-S_q$, $q=1..4$ (21.5-4). Conmensurables: $\omega_1+\omega_2=\omega_3+\omega_4$ (21.5-5),
distintas. Fuentes (p. 918):

$$S_1=\mu_0\omega_1^2\chi^{(3)}\{6E_3E_4E_2^*+3E_1[|E_1|^2+2|E_2|^2+2|E_3|^2+2|E_4|^2]\}\qquad(21.5\text{-}6a)$$
$$S_2=\mu_0\omega_2^2\chi^{(3)}\{6E_3E_4E_1^*+3E_2[|E_2|^2+2|E_1|^2+2|E_3|^2+2|E_4|^2]\}\qquad(21.5\text{-}6b)$$
$$S_3=\mu_0\omega_3^2\chi^{(3)}\{6E_1E_2E_4^*+3E_3[|E_3|^2+2|E_1|^2+2|E_2|^2+2|E_4|^2]\}\qquad(21.5\text{-}6c)$$
$$S_4=\mu_0\omega_4^2\chi^{(3)}\{6E_1E_2E_3^*+3E_4[|E_4|^2+2|E_1|^2+2|E_2|^2+2|E_3|^2]\}\qquad(21.5\text{-}6d)$$

Primer término: mezcla de las otras tres (genera/amplifica); segundo $\propto E_q$: modulación del índice
(efecto Kerr, Ej. 21.3-3). Separación:

$$S_q=\overline S_q+(\omega_q/c_0)^2\Delta\chi_qE_q,\ q=1..4\qquad(21.5\text{-}7)$$
$$\overline S_1=6\mu_0\omega_1^2\chi^{(3)}E_3E_4E_2^*,\quad\overline S_2=6\mu_0\omega_2^2\chi^{(3)}E_3E_4E_1^*,\quad\overline S_3=6\mu_0\omega_3^2\chi^{(3)}E_1E_2E_4^*,\quad\overline S_4=6\mu_0\omega_4^2\chi^{(3)}E_1E_2E_3^*\qquad(21.5\text{-}8a\text{–}d)$$
$$\Delta\chi_q=6\frac\eta{\epsilon_0}\chi^{(3)}(2I-I_q),\qquad I=I_1+I_2+I_3+I_4\qquad(21.5\text{-}9)$$

($I$ total constante por conservación de energía.) Helmholtz modificadas:

$$(\nabla^2+\bar k_q^2)E_q=-\overline S_q\ (21.5\text{-}10),\quad\bar k_q=\bar n_q\frac{\omega_q}{c_0}\ (21.5\text{-}11),\quad\bar n_q^2=n^2+2nn_2(2I-I_q)\ (21.5\text{-}12),\quad n_2=\frac{3\eta_0}{\epsilon_0n^2}\chi^{(3)}\ (21.5\text{-}13)$$

(**recuadro, p. 919**)

$$\boxed{\bar n_q\approx n+n_2(2I-I_q)}\qquad(21.5\text{-}14)\ \text{Optical Kerr Effect}$$

Dos modificaciones: (1) fuente por mezcla de las otras tres (amplificación o generación); (2) índice
dependiente de las intensidades de las cuatro. Cuatro EDO no lineales acopladas.

#### 21.5B Three-Wave Mixing and Third-Harmonic Generation (THG) (p. 919)

**Mezcla de tres ondas** ($\omega_3=\omega_4\equiv\omega_0$, $\omega_1+\omega_2=2\omega_0$):

$$S_1=\mu_0\omega_1^2\chi^{(3)}\{3E_0^2E_2^*+3E_1[|E_1|^2+2|E_2|^2+2|E_0|^2]\}\qquad(21.5\text{-}15a)$$
$$S_2=\mu_0\omega_2^2\chi^{(3)}\{3E_0^2E_1^*+3E_2[|E_2|^2+2|E_1|^2+2|E_0|^2]\}\qquad(21.5\text{-}15b)$$
$$S_0=\mu_0\omega_0^2\chi^{(3)}\{6E_1E_2E_0^*+3E_0[|E_0|^2+2|E_1|^2+2|E_2|^2]\}\qquad(21.5\text{-}15c)$$

Colineales, SVEA, $A_q=\sqrt{2\eta\hbar\omega_q}\,\mathfrak a_q$, $\phi_q=|\mathfrak a_q|^2$, $\omega_1\approx\omega_2\approx\omega_0$ en los coeficientes:

$$\frac{d\mathfrak a_1}{dz}=-j\mathfrak g\big[\mathfrak a_0^2\mathfrak a_2^*e^{-j\Delta kz}+\mathfrak a_1(|\mathfrak a_1|^2+2|\mathfrak a_2|^2+2|\mathfrak a_0|^2)\big]\qquad(21.5\text{-}16a)$$
$$\frac{d\mathfrak a_2}{dz}=-j\mathfrak g\big[\mathfrak a_0^2\mathfrak a_1^*e^{-j\Delta kz}+\mathfrak a_2(|\mathfrak a_2|^2+2|\mathfrak a_1|^2+2|\mathfrak a_0|^2)\big]\qquad(21.5\text{-}16b)$$
$$\frac{d\mathfrak a_0}{dz}=-j\mathfrak g\big[2\mathfrak a_1\mathfrak a_2\mathfrak a_0^*e^{j\Delta kz}+\mathfrak a_0(|\mathfrak a_0|^2+2|\mathfrak a_1|^2+2|\mathfrak a_2|^2)\big]\qquad(21.5\text{-}16c)$$
$$\mathfrak g=\hbar\omega_0(\omega_0/c_0)n_2\qquad(21.5\text{-}17),\qquad\Delta k=2k_0-k_1-k_2\qquad(21.5\text{-}18)$$

Bomba no agotada ($|\mathfrak a_1|,|\mathfrak a_2|\ll|\mathfrak a_0|$), $\Delta k=0$:

$$\frac{d\mathfrak a_1}{dz}=-j\gamma(\mathfrak a_2^*+2\mathfrak a_1)\ (21.5\text{-}19a),\qquad\frac{d\mathfrak a_2}{dz}=-j\gamma(\mathfrak a_1^*+2\mathfrak a_2)\ (21.5\text{-}19b),\qquad\gamma=\mathfrak g\mathfrak a_0^2$$
$$\mathfrak a_1(z)=[(1-j\gamma z)\mathfrak a_1(0)-j\gamma z\,\mathfrak a_2^*(0)]e^{-j\gamma z}\ (21.5\text{-}20a),\qquad\mathfrak a_2(z)=[-j\gamma z\,\mathfrak a_1^*(0)+(1-j\gamma z)\mathfrak a_2(0)]e^{-j\gamma z}\ (21.5\text{-}20b)$$

Si $\mathfrak a_2(0)=0$: $\phi_1(z)=(1+\gamma^2z^2)\phi_1(0)$ (crecimiento **cuadrático**, no exponencial). Si $\mathfrak a_2(0)=\mathfrak re^{j\varphi}\mathfrak a_1(0)$:

$$\phi_1(z)=[1+(2\mathfrak r\sin\varphi)\gamma z+(1+\mathfrak r^2+2\mathfrak r\cos\varphi)\gamma^2z^2]\phi_1(0)\qquad(21.5\text{-}21)$$

máxima cuando $\tan\varphi=2/\gamma z$ (para $z$ pequeño, $\varphi=\pi/2$): **amplificador sensible a la fase**.

Con agotamiento y desajuste: $\mathfrak a_q=\mathfrak b_qe^{j\varphi_q}$, $\varphi=\Delta kz+\varphi_1+\varphi_2-2\varphi_0$:

$$\frac{d\mathfrak b_1}{dz}=\mathfrak g\mathfrak b_0^2\mathfrak b_2\sin\varphi\ (a),\quad\frac{d\mathfrak b_2}{dz}=\mathfrak g\mathfrak b_0^2\mathfrak b_1\sin\varphi\ (b),\quad\frac{d\mathfrak b_0}{dz}=-\mathfrak g\mathfrak b_0\mathfrak b_1\mathfrak b_2\sin\varphi\ (c)\qquad(21.5\text{-}22)$$
$$\frac{d\varphi}{dz}=\Delta k+\mathfrak g[2\mathfrak b_0^2-\mathfrak b_1^2-\mathfrak b_2^2]+\mathfrak g\big[\mathfrak b_0^2\mathfrak b_1/\mathfrak b_2+\mathfrak b_0^2\mathfrak b_2/\mathfrak b_1-4\mathfrak b_1\mathfrak b_2\big]\cos\varphi\qquad(21.5\text{-}22d)$$

Invariantes: $\mathfrak b_1^2+\mathfrak b_2^2+\mathfrak b_0^2$ (energía) y $\mathfrak b_1^2-\mathfrak b_2^2$ (Manley–Rowe). La señal crece inicialmente cuando
$\sin\varphi=0$… (el libro dice "cuando $\sin\varphi=0$, i.e. $\varphi=\pi/2$", p. 921; de (21.5-22a) el crecimiento
máximo es en $\sin\varphi=1$, $\varphi=\pi/2$; el "$=0$" parece errata). Ref.: Cappellini & Trillo, JOSA B 8, 824 (1991).

**THG (p. 921).** $\omega_1=\omega_2=\omega_4=\omega$, $\omega_3=3\omega$; ondas 1 y 3:

$$S_1=\mu_0\omega_1^2\chi^{(3)}\{3E_3E_1^*E_1^*+3E_1[|E_1|^2+2|E_3|^2]\}\ (21.5\text{-}23a),\qquad S_3=\mu_0\omega_3^2\chi^{(3)}\{E_1^3+3E_3[|E_3|^2+2|E_1|^2]\}\ (21.5\text{-}23b)$$

**EXERCISE 21.5-1 (p. 921) — THG con bomba no agotada.** Ondas planas en $z$, envolventes $A_q$, $q=1,3$; SVEA;
con $A_3\ll A_1$ y $A_1(z)\approx A_1(0)$ mostrar

$$\frac{d\mathfrak a_3}{dz}=-j\mathfrak g\,\mathfrak a_1^3\exp(-j\Delta kz)\qquad(21.5\text{-}24)$$

$A_q=\sqrt{2\eta\hbar\omega_q}\,\mathfrak a_q$, $\Delta k=3k_1-k_3$. Derivar $\mathfrak g$.

#### 21.5C Optical Phase Conjugation (OPC) (p. 921)

Totalmente degenerado $\omega_q=\omega$. Bombas 3, 4 planas contrapropagantes $E_3=A_3e^{-j\mathbf k_3\cdot\mathbf r}$,
$E_4=A_4e^{-j\mathbf k_4\cdot\mathbf r}$, $\mathbf k_4=-\mathbf k_3$, intensas y no agotadas ($A_3,A_4$ constantes). $I\approx[|A_3|^2+|A_4|^2]/2\eta$
constante; $2I-I_q\approx2I$ ⇒ Kerr = cambio constante de índice, se ignora. De (21.5-10) y (21.5-8)
(**recuadro, p. 922**):

$$\boxed{(\nabla^2+k^2)E_1=-\xi E_2^*,\qquad(\nabla^2+k^2)E_2=-\xi E_1^*}\qquad(21.5\text{-}25a,b)$$
$$\xi=6\mu_0\omega^2\chi^{(3)}E_3E_4=6\mu_0\omega^2\chi^{(3)}A_3A_4\qquad(21.5\text{-}26),\qquad k=\bar n\omega/c_0,\ \bar n\approx n+2n_2I$$

Dos ecuaciones **lineales** acopladas (fuente ∝ conjugado de la otra). Ondas 1, 2 contrapropagantes
en $z$: $E_1=A_1e^{-jkz}$, $E_2=A_2e^{jkz}$ (21.5-27) (consistente con $\mathbf k_1+\mathbf k_2=\mathbf k_3+\mathbf k_4=0$). Fig. 21.5-1:
sonda 1 entra en $z=-L$, conjugada 2 sale en $z=-L$, bombas 3 y 4 oblicuas; $A_1(z)$ decrece y $A_2(z)$
crece hacia $-L$… (ambas amplitudes crecen hacia la salida respectiva). SVEA (**recuadro**):

$$\boxed{\frac{dA_1}{dz}=-j\gamma A_2^*,\qquad\frac{dA_2}{dz}=j\gamma A_1^*}\qquad(21.5\text{-}28a,b)$$
$$\gamma=\frac\xi{2k}=3\omega\eta_0\frac{\chi^{(3)}}{\bar n}A_3A_4\qquad(21.5\text{-}29)$$

(**recuadro, p. 923**)

$$\boxed{|\gamma|=2C\sqrt{I_3I_4},\qquad C=3\omega\eta_0^2\frac{\chi^{(3)}}{\bar n^2}}\qquad(21.5\text{-}30)\ \text{Coupling Coefficient}$$

$I_3=|A_3|^2/2\eta$, $I_4=|A_4|^2/2\eta$, $\eta=\eta_0/\bar n$. Con $A_3A_4$ real, condiciones $A_1(-L)=A_i$, $A_2(0)=0$:

$$A_1(z)=\frac{A_i}{\cos\gamma L}\cos\gamma z\ (21.5\text{-}31),\qquad A_2(z)=j\frac{A_i^*}{\cos\gamma L}\sin\gamma z\ (21.5\text{-}32)$$

(**recuadros**)

$$\boxed{A_r=-jA_i^*\tan\gamma L}\ (21.5\text{-}33)\ \text{Reflected Wave Amplitude},\qquad\boxed{A_t=\frac{A_i}{\cos\gamma L}}\ (21.5\text{-}34)\ \text{Transmitted Wave Amplitude}$$

($A_r=A_2(-L)$, $A_t=A_1(0)$.) Aplicaciones (p. 923):
- Reflejada = conjugada de la incidente: **conjugador de fase**.
- Reflectancia $|A_r|^2/|A_i|^2=\tan^2\gamma L$, < 1 o > 1: **amplificador en reflexión** ("espejo amplificador").
- Transmitancia $1/\cos^2\gamma L>1$ siempre: **amplificador en transmisión**.
- $\gamma L=\pi/2$ (o múltiplos impares): reflectancia y transmitancia infinitas → **oscilador**.

### *21.6 Anisotropic Nonlinear Media (p. 924)

Cada componente $\mathcal P_i$ depende de $(\mathcal E_1,\mathcal E_2,\mathcal E_3)$ (**recuadro**):

$$\boxed{\mathcal P_i=\epsilon_0\sum_j\chi_{ij}\mathcal E_j+2\sum_{jk}\mathrm d_{ijk}\mathcal E_j\mathcal E_k+4\sum_{jkl}\chi^{(3)}_{ijkl}\mathcal E_j\mathcal E_k\mathcal E_l,\qquad i,j,k,l=1,2,3}\qquad(21.6\text{-}1)$$

Simetrías: $\mathrm d_{ijk}\propto\partial^2\mathcal P_i/\partial\mathcal E_j\partial\mathcal E_k$ ⇒ invariante bajo $j\leftrightarrow k$; $\chi^{(3)}_{ijkl}$ invariante
bajo permutaciones de $j,k,l$. Medio sin pérdidas y no dispersivo: $\chi_{ij}=\chi_{ji}$ y $\mathrm d_{ijk}$, $\chi^{(3)}_{ijkl}$
invariantes bajo **todas** las permutaciones de índices (simetría de permutación completa, no válida en
medios dispersivos). **Notación contraída**: $\mathrm d_{ijk}=\mathrm d_{ikj}$ → matriz $3\times6$ $\mathrm d_{iJ}$,
$(j,k)=11,22,33,23,31,12\leftrightarrow J=1,2,3,4,5,6$ (p. ej. $\mathrm d_{25}=\mathrm d_{231}=\mathrm d_{213}$; Tabla 20.2-1). $\chi^{(3)}_{ijkl}$
→ $6\times6$ $\chi^{(3)}_{IK}$ con $(i,j)\to I$, $(k,l)\to K$. La simetría cristalina anula o relaciona elementos
(Tablas 21.6-1, 21.6-2); valores en Tabla 21.6-3. Cristales cúbicos: lineal isótropo pero no lineal
anisótropo. $\mathrm d_{ijk}$ y $\chi^{(3)}_{ijkl}$ están relacionados con los tensores Pockels $\mathfrak r_{ijk}$ y Kerr $\mathfrak s_{ijkl}$
(Prob. 21.6-2) y tienen las mismas simetrías (Tablas 20.2-2, 20.2-3); $\mathrm d_{iJ}$ es análogo al
**transpuesto** de $\mathfrak r_{Ik}$ (p. 925).

**Mezcla de tres ondas anisótropa (p. 925–926).** Ondas linealmente polarizadas $\mathbf E(\omega_1)$, $\mathbf E(\omega_2)$:

$$P_i(\omega_3)=2\sum_{jk}\mathrm d_{ijk}E_j(\omega_1)E_k(\omega_2),\qquad i,j,k=1,2,3\qquad(21.6\text{-}2)$$

(generaliza (21.2-13d); componentes en ejes principales). Forma matricial (21.6-3):

$$\begin{bmatrix}P_1(\omega_3)\\P_2(\omega_3)\\P_3(\omega_3)\end{bmatrix}=2\begin{bmatrix}\mathrm d_{11}&\mathrm d_{12}&\cdots&\mathrm d_{16}\\\mathrm d_{21}&\mathrm d_{22}&\cdots&\mathrm d_{26}\\\mathrm d_{31}&\mathrm d_{32}&\cdots&\mathrm d_{36}\end{bmatrix}\begin{bmatrix}E_1(\omega_1)E_1(\omega_2)\\E_2(\omega_1)E_2(\omega_2)\\E_3(\omega_1)E_3(\omega_2)\\E_2(\omega_1)E_3(\omega_2)+E_3(\omega_1)E_2(\omega_2)\\E_3(\omega_1)E_1(\omega_2)+E_1(\omega_1)E_3(\omega_2)\\E_1(\omega_1)E_2(\omega_2)+E_2(\omega_1)E_1(\omega_2)\end{bmatrix}$$

**Valor efectivo de d.** $E_j(\omega_1)=E(\omega_1)\cos\theta_{1j}$, $E_k(\omega_2)=E(\omega_2)\cos\theta_{2k}$ (ángulos con los ejes principales):

$$P_i(\omega_3)=2\Big[\sum_{jk}\mathrm d_{ijk}\cos\theta_{1j}\cos\theta_{2k}\Big]E(\omega_1)E(\omega_2)\qquad(21.6\text{-}4)$$

Solo radia la componente $\mathbf P_\perp(\omega_3)$ ortogonal a $\mathbf k_3$ (TEM); con ángulos $\bar\theta_{3i}$:

$$P_\perp(\omega_3)=\sum_iP_i(\omega_3)\cos\bar\theta_{3i}\ (21.6\text{-}5)\quad\Rightarrow\quad P_\perp(\omega_3)=2\mathrm d_{\rm eff}E(\omega_1)E(\omega_2)\ (21.6\text{-}6)$$
$$\mathrm d_{\rm eff}=\sum_{ijk}\mathrm d_{ijk}\cos\bar\theta_{3i}\cos\theta_{1j}\cos\theta_{2k}\qquad(21.6\text{-}7)$$

$\mathrm d_{\rm eff}$ juega el papel de $\mathrm d$ en 21.2C y 21.4.

**EXAMPLE 21.6-1 (p. 926–927) — Mezcla colineal Tipo I en KDP.** Dirección $(\theta,\phi)$ esférica, eje óptico en
$z$ (Fig. 21.6-1). Ondas 1, 2 ordinarias, 3 extraordinaria ($\omega_3=\omega_1+\omega_2$). Con Tabla 21.6-1 ($\bar42m$):

$$P_1(\omega_3)=2\mathrm d_{14}[E_2(\omega_1)E_3(\omega_2)+E_3(\omega_1)E_2(\omega_2)],\quad P_2(\omega_3)=2\mathrm d_{14}[E_3(\omega_1)E_1(\omega_2)+E_1(\omega_1)E_3(\omega_2)],\quad P_3(\omega_3)=2\mathrm d_{36}[E_1(\omega_1)E_2(\omega_2)+E_2(\omega_1)E_1(\omega_2)]\quad(21.6\text{-}8)$$

Campos o: $E_1(\omega_q)=E(\omega_q)\sin\phi$, $E_2(\omega_q)=-E(\omega_q)\cos\phi$, $E_3(\omega_q)=0$ ⇒

$$P_1(\omega_3)=0,\quad P_2(\omega_3)=0,\quad P_3(\omega_3)=-4\mathrm d_{36}\sin\phi\cos\phi\,E(\omega_1)E(\omega_2)\qquad(21.6\text{-}9)$$

$P_\perp(\omega_3)=-P_3(\omega_3)\sin\theta$ ⇒ (**recuadro**)

$$\boxed{\mathrm d_{\rm eff}=-\mathrm d_{36}\sin\theta\sin2\phi}\qquad(21.6\text{-}10)$$

Máximo $|\mathrm d_{\rm eff}|=\mathrm d_{36}$ en $\theta=90°$, $\phi=45°$ (Fig. 21.6-1b).

### *21.7 Dispersive Nonlinear Media (p. 927)

Medio dispersivo = con memoria: $\mathcal P(t)$ depende de $\mathcal E(t')$, $t'\le t$ (5.2). Dos descripciones: (1) relación
integral fenomenológica (serie de **Volterra**); (2) ecuación diferencial no lineal (modelo de Lorentz
anarmónico).

**Descripción integral (p. 927–929).**

$$\mathcal P(t)=\epsilon_0\int_{-\infty}^\infty\mathsf x(t-t')\mathcal E(t')dt'\qquad(21.7\text{-}1)$$

(sistema lineal con respuesta impulsiva $\epsilon_0\mathsf x(t)$; (5.2-23), Apéndice B).

$$\mathcal P(t)=\epsilon_0\iint_{-\infty}^\infty\mathsf x^{(2)}(t-t',t-t'')\mathcal E(t')\mathcal E(t'')dt'dt''\qquad(21.7\text{-}2)$$

y análogo triple con $\mathsf x^{(3)}(t',t'',t''')$. Lineal: $P(\omega)=\epsilon_0\chi(\omega)E(\omega)$, $\chi(\omega)$ = TF de $\mathsf x(t)$ en
$\nu=\omega/2\pi$. Segundo orden con dos ondas $\mathcal E(t)=\mathrm{Re}\{E(\omega_1)e^{j\omega_1t}+E(\omega_2)e^{j\omega_2t}\}$ (21.7-3)
(**recuadro, p. 928**):

$$\boxed{P(\omega_3)=2\mathrm d(\omega_3;\omega_1,\omega_2)E(\omega_1)E(\omega_2)}\qquad(21.7\text{-}4)$$
$$\mathcal X^{(2)}(\omega_1,\omega_2)=\iint_{-\infty}^\infty\mathsf x^{(2)}(t',t'')\exp[-j(\omega_1t'+\omega_2t'')]dt'dt''\qquad(21.7\text{-}5)$$

(TF bidimensional evaluada en $\nu_1=-\omega_1/2\pi$, $\nu_2=-\omega_2/2\pi$, (A.3-2)).

$$\mathrm d(\omega_3;\omega_1,\omega_2)=\epsilon_0\mathcal X^{(2)}(\omega_1,\omega_2)\qquad(21.7\text{-}6a)$$
$$\mathrm d(2\omega;\omega,\omega)=\tfrac12\epsilon_0\mathcal X^{(2)}(\omega,\omega)\qquad(21.7\text{-}6b),\ \text{p. 929}$$

Electroóptico: $\omega_1=0$, $\omega_2=\omega$: $\mathrm d(\omega;0,\omega)=2\epsilon_0\mathcal X^{(2)}(\omega,0)$, que determina $\mathfrak r$ vía (21.2-11). Tercer
orden (**recuadro**):

$$\boxed{P(\omega_4)=6\chi^{(3)}(\omega_4;\omega_1,\omega_2,\omega_3)E(\omega_1)E(\omega_2)E(\omega_3)}\qquad(21.7\text{-}7)$$

Conclusión: por la dispersión, $\mathrm d$ y $\chi^{(3)}$ dependen de las frecuencias de las ondas que se mezclan.

**Descripción diferencial (p. 929–931).** Oscilador anarmónico:

$$\frac{d^2\mathcal P}{dt^2}+\sigma\frac{d\mathcal P}{dt}+\omega_0^2\mathcal P+\omega_0^2\epsilon_0\chi_0\mathsf b\,\mathcal P^2=\omega_0^2\epsilon_0\chi_0\mathcal E\qquad(21.7\text{-}8)$$

Sin $\mathsf b$: (5.5-15), Lorentz (masa $m$, carga $-e$, $-\kappa x$, fricción $m\sigma dx/dt$, $\omega_0=\sqrt{\kappa/m}$) con (**recuadro**)

$$\boxed{\chi(\omega)=\chi_0\frac{\omega_0^2}{\omega_0^2-\omega^2+j\omega\sigma}}\qquad(21.7\text{-}9)\ \text{Linear Susceptibility (Harmonic Oscillator)}$$

Fuerza restauradora $-\kappa x-\kappa_2x^2$ ⇒ (21.7-8) con $\mathsf b\propto\kappa_2$.

**EXERCISE 21.7-1 (p. 930) — Polarización de un medio de osciladores anarmónicos.** Mostrar que para $N$
átomos por unidad de volumen con fuerza $-\kappa x-\kappa_2x^2$ la relación $\mathcal P$–$\mathcal E$ es (21.7-8) con
$\chi_0=Ne^2/\epsilon_0m\omega_0^2$ y $\mathsf b=\kappa_2/e^3N^2$.

Solución iterativa: $\mathcal L\{\mathcal P\}=\mathcal E-\mathsf b\mathcal P^2$ (21.7-10), $\mathcal L=(\omega_0^2\epsilon_0\chi_0)^{-1}(d^2/dt^2+\sigma d/dt+\omega_0^2)$.
(1) $\mathcal L\{\mathcal P_1\}\approx\mathcal E$ (21.7-11); (2) calcular $\mathsf b\mathcal P_1^2$; (3) $\mathcal L\{\mathcal P_2\}=\mathcal E-\mathsf b\mathcal P_1^2$ (21.7-12); (4) iterar
(Fig. 21.7-1: lazo con sistema lineal $\epsilon_0\chi(\omega)$ y realimentación $-\mathsf b\mathcal P^2$). Monocromático:
$P_1(\omega)=\epsilon_0\chi(\omega)E(\omega)$; segunda iteración forzada por
$\mathcal E-\mathsf b\mathcal P_1^2=\mathrm{Re}\{Ee^{j\omega t}\}-\tfrac12\mathsf b\,\mathrm{Re}\{[\epsilon_0\chi(\omega)E(\omega)]^2e^{j2\omega t}\}-\tfrac12\mathsf b|\epsilon_0\chi(\omega)E(\omega)|^2$ (frecuencias $\omega,2\omega,0$;
responde con $\chi(\omega),\chi(2\omega),\chi(0)$). $P_2(2\omega)=\epsilon_0\chi(2\omega)\{-\tfrac12\mathsf b[\epsilon_0\chi(\omega)E(\omega)]^2\}$ ⇒ (**recuadro, p. 931**)

$$\boxed{\mathrm d(2\omega;\omega,\omega)=-\tfrac12\mathsf b\,\epsilon_0^3[\chi(\omega)]^2\chi(2\omega)}\qquad(21.7\text{-}13)$$

*Nota de lectura:* en el escaneo el exponente de $\epsilon_0$ en (21.7-13) parece 2; por la derivación anterior y por
coherencia con (21.7-14) debe ser 3.

**EXERCISE 21.7-2 (p. 931) — Regla de Miller.** Para (21.7-8) con dos ondas $\omega_1,\omega_2$, mostrar que la
segunda iteración da $P_2(\omega_3)=2\mathrm d(\omega_3;\omega_1,\omega_2)E(\omega_1)E(\omega_2)$ con (**recuadro**)

$$\boxed{\mathrm d(\omega_3;\omega_1,\omega_2)=-\tfrac12\mathsf b\,\epsilon_0^3\chi(\omega_1)\chi(\omega_2)\chi(\omega_3)}\qquad(21.7\text{-}14)\ \text{Miller's Rule}$$

**Regla de Miller**: $\mathrm d\propto\chi(\omega_1)\chi(\omega_2)\chi(\omega_3)$; las tres frecuencias deben estar en la ventana de
transparencia (lejos de resonancia). Si $\omega\ll\omega_0$, $\chi\approx\chi_0$ y $\mathrm d=-\tfrac12\mathsf b\epsilon_0^3\chi_0^3$ independiente de
la frecuencia (medio ≈ no dispersivo, valen las secciones anteriores). **Materiales con $n$ grande tienden a
tener $\mathrm d$ grande.**

**Medios anisótropos y dispersivos (p. 931–932).** (**recuadros**)

$$\boxed{P_i(\omega_3)=2\sum_{jk}\mathrm d_{ijk}(\omega_3;\omega_1,\omega_2)E_j(\omega_1)E_k(\omega_2)}\ (21.7\text{-}15),\qquad\boxed{P_i(\omega_4)=6\sum_{jkl}\chi^{(3)}_{ijkl}(\omega_4;\omega_1,\omega_2,\omega_3)E_j(\omega_1)E_k(\omega_2)E_l(\omega_3)}\ (21.7\text{-}16)$$

Simetrías intrínsecas (análogas a $\chi^*_{ij}(\omega)=\chi_{ij}(-\omega)$):

$$\mathrm d^*_{ijk}(\omega_3;\omega_1,\omega_2)=\mathrm d_{jki}(\omega_1;-\omega_2,\omega_3)=\mathrm d_{kij}(\omega_2;\omega_3,-\omega_1)\qquad(21.7\text{-}17)$$
$$\chi^{(3)*}_{ijkl}(\omega_4;\omega_1,\omega_2,\omega_3)=\chi^{(3)}_{ijkl}(\omega_1;-\omega_2,-\omega_3,\omega_4)=\cdots=\chi^{(3)}_{jikl}(\omega_3;\omega_4,-\omega_1,-\omega_2)\qquad(21.7\text{-}18)$$

(transcritas tal como se leen; el orden de índices del último miembro de (21.7-18) es el del escaneo).
Interpretación: $\mathrm d_{jki}(\omega_1;-\omega_2,\omega_3)$ es el down‑conversion en que $\omega_2$ (pol. $k$) y $\omega_3$ (pol. $i$)
generan $\omega_1=\omega_3-\omega_2$ (pol. $j$). A esto se suman las simetrías estructurales del cristal.

### Reading List (p. 932–934)

Libros (selección; ver también listas de caps. 5, 6, 15, 20 y 17): Agrawal, *Nonlinear Fiber Optics*
(4.ª ed. 2006); Menzel, *Photonics* (2006); Wegener, *Extreme Nonlinear Optics* (2005); Nikogosyan,
*Nonlinear Optical Crystals: A Complete Survey* (2005); Banerjee (2004); Brignon & Huignard, *Phase
Conjugate Laser Optics* (2004); **Boyd, *Nonlinear Optics* (2.ª ed. 2003)**; Suhara & Fujimura,
*Waveguide Nonlinear-Optic Devices* (2003); Sutherland, *Handbook of Nonlinear Optics* (2003); Risk,
Gosnell & Nurmikko, *Compact Blue-Green Lasers* (2003); Shen, *Principles of Nonlinear Optics* (1984/2002);
Miyata & Sasabe (2000); Robieux (2000); He & Liu (1999); Maimistov & Basharov (1999); Dmitriev,
Gurzadyan & Nikogosyan, *Handbook of Nonlinear Optical Crystals* (1999); Mills (1998); Kajzar &
Reinisch (1998); Nalwa & Miyata (1997); Bloembergen, *Nonlinear Optics* (1965/1996); Sauter (1996);
Tang & Cheng (1995); Zhang, Huang & Shen (1995); Zyss (1994); Hopf & Stegeman (1992); Prasad & Williams
(1991); Butcher & Cotter, *The Elements of Nonlinear Optics* (1990); Butylkin et al. (1989); Schubert &
Wilhelmi (1986); Zel'dovich, Pilipetsky & Shkunov, *Principles of Phase Conjugation* (1985); Fisher,
*Optical Phase Conjugation* (1983); Rabin & Tang (1975); Kaminow (1974).
Artículos: números especiales de IEEE JSTQE sobre óptica no lineal (2006, 2004, 2002, 2000); Gmachl,
Malis & Belyanin (2006); Saltiel, Sukhorukov & Kivshar, *Progress in Optics* 47 (2005); Gosnell
(2000); Byer, QPM, *J. Nonlinear Opt. Phys. Mater.* 6, 549 (1997); Hunt (1997); Roberts, convenciones
de cristales uniáxicos y biáxicos, *IEEE JQE* 28, 2057 (1992); Brandt (1991); Khoo (1988); Pepper,
*Sci. Am.* 254, 74 (1986); Shkunov & Zel'dovich, *Sci. Am.* 253, 54 (1985); Bloembergen, Nobel lecture,
*Rev. Mod. Phys.* 54, 685 (1982); Mikaelian (1980); Brunner & Paul (1977); Hellwarth, *Prog. Quantum
Electron.* 5, 1 (1977).

---

## Tablas y datos numéricos útiles

**Constantes y relaciones (cap. 21).**
- $\eta_0=(\mu_0/\epsilon_0)^{1/2}\approx377\ \Omega$; $\eta=\eta_0/n$; $I=|E|^2/2\eta$; $c_0=1/(\epsilon_0\mu_0)^{1/2}$; $c=c_0/n$; $n^2=1+\chi$.
- $\epsilon_0\approx8.85\times10^{-12}$ F/m; conversión $\mathrm d$ [C/V²] → $\mathrm d/\epsilon_0$ [pm/V]: dividir por $10^{-12}\epsilon_0\approx8.85\times10^{-24}$ (p. 925).
- Rangos típicos (p. 877): $\mathrm d=10^{-24}$–$10^{-21}$ C/V²; $\chi^{(3)}=10^{-34}$–$10^{-29}$ C·m/V³.
- $n_2$ [cm²/W] (p. 896): vidrios $10^{-16}$–$10^{-14}$; vidrios dopados $10^{-14}$–$10^{-7}$; orgánicos $10^{-10}$–$10^{-8}$;
  semiconductores $10^{-10}$–$10^{-2}$.
- Figura de mérito para SHG/OFC/OPA: $\mathrm d^2/n^3$ (p. 911); ejemplo $10^{-46}$ C²/V⁴ → $C^2=0.038$ MW⁻¹ a 1 μm.
- KDP (p. 888): 694 nm: $n_o=1.506$, $n_e=1.466$; 347 nm: $n_o=1.534$, $n_e=1.490$; SHG e‑e‑o $\theta=52°$; o‑o‑e a 1.06 μm $\theta=41°$.
- KDP (Prob. 21.2-4): 0.6 μm: $n_o=1.509$, $n_e=1.468$; 1.2 μm: $n_o=1.490$, $n_e=1.459$.
- Ejercicio 21.1-1: ADP $n=1.5$, $\mathrm d=6.8\times10^{-24}$ C/V² (1.06 μm); CS₂ $n=1.6$, $\chi^{(3)}=4.4\times10^{-32}$ C·m/V³ (694 nm).
- Proustita (Ej. 21.4-5): $\mathrm d=1.5\times10^{-22}$ C/V², $n=2.6$. KTP (Ej. 21.4-6): $n=1.75$, $\mathrm d=2.3\times10^{-23}$ C/V².
  KDP (Prob. 21.4-7): $n\approx1.49$, $\mathrm d=8.3\times10^{-24}$ C/V². LiNbO₃ (Prob. 21.4-9): $n=2.2$, $\mathrm d=4\times10^{-23}$ C/V².
- SPM: $P_\pi=\lambda_0A/2Ln_2$ (p. 896); ej. 0.5 W para $L=1$ m, $A=10^{-2}$ mm², $n_2=10^{-10}$ cm²/W, $\lambda_0=1$ μm.
- Umbral SRO ejemplo (p. 916): $L^2/A=10^6$, $C^2=10^{-7}$ W⁻¹, $\mathcal R_1=0.9$ → 2.3 W.

**Tabla 21.6-1 (p. 924) — $\mathrm d_{iJ}$ para grupos cristalinos representativos.**

Cúbico $\bar43m$ (GaAs, CdTe, InAs):
$$\begin{bmatrix}0&0&0&\mathrm d_{14}&0&0\\0&0&0&0&\mathrm d_{14}&0\\0&0&0&0&0&\mathrm d_{14}\end{bmatrix}$$
Tetragonal $\bar42m$ (KDP, ADP):
$$\begin{bmatrix}0&0&0&\mathrm d_{14}&0&0\\0&0&0&0&\mathrm d_{14}&0\\0&0&0&0&0&\mathrm d_{36}\end{bmatrix}$$
Trigonal $3m$ (BBO, LiNbO₃, LiTaO₃):
$$\begin{bmatrix}0&0&0&0&\mathrm d_{15}&-\mathrm d_{22}\\-\mathrm d_{22}&\mathrm d_{22}&0&\mathrm d_{15}&0&0\\\mathrm d_{31}&\mathrm d_{31}&\mathrm d_{33}&0&0&0\end{bmatrix}$$

**Tabla 21.6-2 (p. 925) — $\chi^{(3)}_{IK}$ para medio isótropo.**
$$\begin{bmatrix}\chi^{(3)}_{11}&\chi^{(3)}_{12}&\chi^{(3)}_{12}&0&0&0\\\chi^{(3)}_{12}&\chi^{(3)}_{11}&\chi^{(3)}_{12}&0&0&0\\\chi^{(3)}_{12}&\chi^{(3)}_{12}&\chi^{(3)}_{11}&0&0&0\\0&0&0&\chi^{(3)}_{44}&0&0\\0&0&0&0&\chi^{(3)}_{44}&0\\0&0&0&0&0&\chi^{(3)}_{44}\end{bmatrix},\qquad\chi^{(3)}_{44}=\tfrac12\big(\chi^{(3)}_{11}-\chi^{(3)}_{12}\big)$$

**Tabla 21.6-3 (p. 925) — Coeficientes $\mathrm d_{iJ}$ de segundo orden (Nikogosyan 2005; a $\lambda_0=1.06$ μm salvo Te a 10.6 μm).**

| Cristal | $\mathrm d_{iJ}$ (C/V²) | $\mathrm d_{iJ}/\epsilon_0$ (pm/V) |
|---|---|---|
| β‑BaB₂O₄ (BBO) | $\mathrm d_{22}=2.0\times10^{-23}$ | 2.2 |
| | $\mathrm d_{31}=3.5\times10^{-25}$ | 0.04 |
| LiB₃O₅ (LBO) | $\mathrm d_{31}=5.9\times10^{-24}$ | 0.67 |
| | $\mathrm d_{32}=7.5\times10^{-24}$ | 0.85 |
| | $\mathrm d_{33}=3.5\times10^{-25}$ | 0.04 |
| LiIO₃ | $\mathrm d_{31}=3.9\times10^{-23}$ | 4.4 |
| | $\mathrm d_{33}=4.1\times10^{-23}$ | 4.6 |
| LiNbO₃ | $\mathrm d_{22}=1.9\times10^{-23}$ | 2.1 |
| | $\mathrm d_{31}=4.1\times10^{-23}$ | 4.6 |
| | $\mathrm d_{33}=2.2\times10^{-22}$ | 25.2 |
| KNbO₃ | $\mathrm d_{31}=1.1\times10^{-22}$ | 11.9 |
| | $\mathrm d_{32}=1.2\times10^{-22}$ | 13.7 |
| KTiOPO₄ (KTP) | $\mathrm d_{31}=2.0\times10^{-23}$ | 2.2 |
| | $\mathrm d_{32}=3.3\times10^{-23}$ | 3.7 |
| | $\mathrm d_{33}=1.3\times10^{-22}$ | 14.6 |
| KH₂PO₄ (KDP) | $\mathrm d_{36}=3.1\times10^{-24}$ | 0.38 |
| NH₄H₂PO₄ (ADP) | $\mathrm d_{36}=4.2\times10^{-24}$ | 0.47 |
| α‑SiO₂ (cuarzo) | $\mathrm d_{11}=2.7\times10^{-24}$ | 0.30 |
| KBe₂BO₃F₂ (KBBF) | $\mathrm d_{11}=4.3\times10^{-24}$ | 0.49 |
| GaAs | $\mathrm d_{14}=1.5\times10^{-21}$ | 170 |
| Te | $\mathrm d_{11}=5.8\times10^{-21}$ | 650 |

Nota b de la tabla: los $\mathrm d/\epsilon_0$ en pm/V son los que se usan en la práctica (equivalen al $d_{il}$ de Boyd).

**Resumen de fórmulas de eficiencia/ganancia (todas con $C^2\propto\mathrm d^2/n^3$):**

| Proceso | Resultado exacto | Límite débil | $C^2$ |
|---|---|---|---|
| SHG (21.4-34/36) | $\eta=\tanh^2(\gamma L/2)$, $\gamma^2=8\mathrm d^2\eta^3\omega^2I_1(0)$ | $C^2(L^2/A)P$ | $2\omega^2\eta_0^3\mathrm d^2/n^3$ |
| SHG con $\Delta k$ (21.4-38) | — | $C^2(L^2/A)P\,\mathrm{sinc}^2(\Delta kL/2\pi)$ | ídem |
| OFC (21.4-42/43) | $\eta=(\omega_3/\omega_1)\sin^2(\gamma L/2)$, $\gamma=2\mathfrak g\mathfrak a_2(0)$ | $C^2(L^2/A)P_2$ | $2\omega_3^2\eta_0^3\mathrm d^2/n^3$ |
| OPA (21.4-46/47) | $G=\cosh^2(\gamma L/2)$, $\gamma=2C\sqrt{P_3/A}$ | $e^{\gamma L}/4$ | $2\omega_1\omega_2\eta_0^3\mathrm d^2/n^3$ |
| SRO (21.4-49) | $P_{\rm th}\approx(A/C^2L^2)(1-\mathcal R_1^2)/\mathcal R_1^2$ | | ídem |
| DRO (21.4-52) | $P_{\rm th}\approx(A/C^2L^2)(1-\mathcal R_1)(1-\mathcal R_2)/\mathcal R_1\mathcal R_2$ | | ídem |
| OPC $\chi^{(3)}$ (21.5-30/33/34) | $|A_r/A_i|^2=\tan^2\gamma L$, $|A_t/A_i|^2=1/\cos^2\gamma L$, $|\gamma|=2C\sqrt{I_3I_4}$ | | $C=3\omega\eta_0^2\chi^{(3)}/\bar n^2$ |
| OPA $\chi^{(3)}$ (21.5-20) | $\phi_1=(1+\gamma^2z^2)\phi_1(0)$, $\gamma=\mathfrak g\mathfrak a_0^2$, $\mathfrak g=\hbar\omega_0(\omega_0/c_0)n_2$ | | |

---

## Problemas al final del capítulo (p. 934–935)

(La numeración continúa la de los ejercicios de cada sección; los marcados con * son avanzados.)

**21.2-2 Power Exchange in Frequency Up-Conversion.** Un cristal de LiNbO₃ de índice $n=2.2$ se usa para
convertir luz de longitud de onda en vacío 1.3 μm en luz de 0.5 μm mediante un proceso de mezcla de tres
ondas. Las tres ondas son ondas planas colineales que viajan en la dirección $z$. Determine la longitud de
onda de la tercera onda (la bomba). Si la potencia de la onda de 1.3 μm cae 1 mW en una distancia
incremental $\Delta z$, ¿cuál es la ganancia de potencia de la onda convertida y la pérdida o ganancia de
potencia de la bomba en la misma distancia?

**21.2-3 Matching Conditions for Collinear Type-II SHG.** Determine el ángulo $\theta$ para un cristal de KDP
usado en generación de segundo armónico tipo II a $\lambda=1.06$ μm, para cada una de las configuraciones
o‑e‑o y o‑e‑e. Use las ecuaciones de Sellmeier de la Tabla 5.5-1 para determinar la dependencia con la
longitud de onda de los índices de refracción.

**21.2-4 Phase Matching in a Degenerate Parametric Down-Converter.** Un down‑converter paramétrico
degenerado usa un cristal de KDP para convertir luz de 0.6 μm a 1.2 μm. Si las dos ondas son colineales,
¿cuál debe ser la dirección de propagación de las ondas (en relación con el eje óptico del cristal) y sus
polarizaciones para que se satisfaga la condición de ajuste de fase? KDP es un cristal uniáxico con los
siguientes índices de refracción: a $\lambda_0=0.6$ μm, $n_o=1.509$ y $n_e=1.468$; a $\lambda_0=1.2$ μm, $n_o=1.490$ y
$n_e=1.459$.

**21.2-5 Matching Conditions for Three-Wave Mixing in a Dispersive Medium.** El índice de refracción de un
medio no lineal es función de la longitud de onda aproximada por $n(\lambda_0)\approx n_0-\xi\lambda_0$, donde $\lambda_0$ es la
longitud de onda en el vacío y $n_0$ y $\xi$ son constantes. Muestre que tres ondas de longitudes de onda
$\lambda_{01},\lambda_{02},\lambda_{03}$ viajando en la misma dirección no pueden acoplarse eficientemente por un efecto no
lineal de segundo orden. ¿Es posible el acoplamiento eficiente si una de las ondas viaja en la dirección
opuesta?

***21.2-6 Tolerance to Phase Mismatching.**
(a) La ecuación de Helmholtz con fuente, $\nabla^2E+k^2E=-S$, tiene la solución
$$E(\mathbf r)=\int_VS(\mathbf r')\frac{\exp(-jk_0|\mathbf r-\mathbf r'|)}{4\pi|\mathbf r-\mathbf r'|}d\mathbf r',$$
donde $V$ es el volumen de la fuente y $k_0=2\pi/\lambda_0$. Esta ecuación puede usarse para determinar el campo
emitido en un punto $\mathbf r$, dada la fuente en todos los puntos $\mathbf r'$ dentro del volumen fuente. Si la fuente
está confinada a una región pequeña centrada alrededor del origen $\mathbf r=0$, y $\mathbf r$ es un punto
suficientemente lejano de la fuente de modo que $r'\ll r$ para todo $\mathbf r'$ dentro de la fuente, entonces
$|\mathbf r-\mathbf r'|=(r^2+r'^2-2\mathbf r\cdot\mathbf r')^{1/2}\approx r(1-\mathbf r\cdot\mathbf r'/r^2)$ y
$$E(\mathbf r)\approx\frac{\exp(-jk_0r)}{4\pi r}\int_VS(\mathbf r')\exp(jk_0\hat{\mathbf r}\cdot\mathbf r')d\mathbf r',$$
donde $\hat{\mathbf r}$ es un vector unitario en la dirección de $\mathbf r$. Suponiendo que el volumen $V$ es un cubo de
lado $L$ y la fuente es una función armónica $S(\mathbf r)=\exp(-j\mathbf k_s\cdot\mathbf r)$, muestre que si $L\gg\lambda_0$, la luz
emitida es máxima cuando $k_0\hat{\mathbf r}=\mathbf k_s$ y cae bruscamente cuando no se cumple esta condición. Así, una
fuente armónica de dimensiones mucho mayores que una longitud de onda emite una onda plana con
aproximadamente el mismo vector de onda.
(b) Use la relación de (a) y la primera aproximación de Born para determinar el campo dispersado cuando
el campo incidente sobre un medio no lineal de segundo orden es la suma de dos ondas con vectores de
onda $\mathbf k_1$ y $\mathbf k_2$. Derive la condición de ajuste de fase $\mathbf k_3=\mathbf k_1+\mathbf k_2$ y determine la magnitud
mínima de $\Delta\mathbf k=\mathbf k_3-\mathbf k_1-\mathbf k_2$ a la cual el campo dispersado $E$ se anula.

**21.2-7 Backward SHG with QPM.** Muestre que un cristal periódicamente polarizado (poled) puede usarse
para generar una onda de segundo armónico viajando en dirección opuesta a la de la onda fundamental.
Escriba la ecuación de ajuste de fase para este proceso de cuasi‑ajuste de fase. Si la ecuación se satisface
para el 7.º armónico de la función periódica, determine la razón entre el período de poling y la longitud de
onda de la onda fundamental en el medio.

**21.3-4 Invariants in Four-Wave Mixing.** Derive las ecuaciones de conservación de energía y de número
de fotones (relación de Manley–Rowe) para la mezcla de cuatro ondas.

**21.3-5 Power of a Spatial Soliton.** Derive una expresión para la intensidad integrada del solitón espacial
descrito por (21.3-12) y muestre que es inversamente proporcional al ancho del haz $W_0$.

**21.3-6 An Opto-Optic Phase Modulator.** Diseñe un sistema para modular la fase de un haz óptico de longitud
de onda 546 nm y ancho $W=0.1$ mm usando una celda Kerr de CS₂ de longitud $L=10$ cm. El modulador se
controla con luz de un láser pulsado de longitud de onda 694 nm. CS₂ tiene índice $n=1.6$ y coeficiente de
no linealidad de tercer orden $\chi^{(3)}=4.4\times10^{-32}$ C·m/V³. Estime la potencia óptica $P_\pi$ de la luz de control
necesaria para modular la fase de la luz controlada en $\pi$.

**21.3-7 SHG in Third-Order Nonlinear Medium via a Static Electric Field.** Muestre que puede ocurrir SHG en
un medio no lineal de tercer orden con un campo eléctrico estático aplicado. ¿Qué parámetros físicos
determinan la eficiencia de este proceso de SHG?

***21.4-7 Gain of a Parametric Amplifier.** Un amplificador paramétrico usa un cristal de KDP de 4 cm de
largo ($n\approx1.49$, $\mathrm d=8.3\times10^{-24}$ C/V²) para amplificar luz de longitud de onda 550 nm. La longitud de onda de
la bomba es 335 nm y su intensidad es $10^6$ W/cm². Suponiendo que las ondas de señal, idler y bomba son
colineales, determine el coeficiente de ganancia del amplificador y la ganancia total.

***21.4-8 Degenerate Parametric Down-Converter.** Escriba y resuelva las ecuaciones acopladas que describen
la mezcla de ondas en un down‑converter paramétrico con bomba a frecuencia $\omega_3=2\omega$ y señales a
$\omega_1=\omega_2=\omega$. Todas las ondas viajan en la dirección $z$. Derive una expresión para las densidades de flujo
de fotones a $2\omega$ y $\omega$ y la eficiencia de conversión para una longitud de interacción $L$. Verifique la
conservación de energía y de fotones.

***21.4-9 Threshold Pump Intensity for Parametric Oscillation.** Un oscilador paramétrico usa un cristal de
LiNbO₃ de 5 cm de largo con coeficiente no lineal de segundo orden $\mathrm d=4\times10^{-23}$ C/V² e índice de refracción
$n=2.2$ (supuesto aproximadamente constante en todas las frecuencias de interés). La bomba se obtiene de un
láser Nd:YAG de 1.06 μm doblado en frecuencia con un generador de segundo armónico. El cristal se coloca en
un resonador con espejos idénticos de reflectancia 0.98. Se satisface el ajuste de fase cuando la señal y el
idler del amplificador paramétrico tienen frecuencias iguales. Determine la intensidad de bomba mínima para
oscilación paramétrica.

***21.5-1 Combined SHG and SFG.** Dos ondas de frecuencias angulares $\omega_1$ y $\omega_2$, sus ondas de segundo
armónico a $2\omega_1$ y $2\omega_2$, y su onda de suma de frecuencias a $\omega_1+\omega_2$ interactúan simultáneamente en un
medio no lineal de segundo orden. Suponiendo que se satisface el ajuste de fase para los dos procesos de SHG
y para el proceso de SFG, escriba las ecuaciones acopladas para este proceso de mezcla de cinco ondas.
Resuélvalas numéricamente y demuestre que la presencia de la segunda onda puede suprimir el proceso de SHG
de la primera.

***21.5-2 Coupled-Wave Equations for Degenerate Four-Wave Mixing.** Considere la mezcla colineal de cuatro
ondas en un medio no lineal de tercer orden en el caso degenerado $\omega_4=\omega_3$ y $\omega_1+\omega_2=2\omega_3$. Derive las
ecuaciones de ondas acopladas para las amplitudes $A_1$, $A_2$ y $A_3$ suponiendo que la condición de ajuste
de fase se cumple exactamente.

***21.6-1 Collinear Type-II Three-Wave Mixing in a BBO Crystal.** Repita el análisis del Ejemplo 21.6-1 para
mostrar que el coeficiente no lineal efectivo para la mezcla de tres ondas tipo II o‑e‑e en un cristal del
grupo $3m$, como BBO, es $\mathrm d_{\rm eff}=\mathrm d_{22}\cos^2\theta\cos3\phi$.

***21.6-2 Relation Between Nonlinear Optical Coefficients and Electro-Optic Coefficients.** Muestre que los
coeficientes electroópticos están relacionados con los coeficientes de no linealidad óptica por
$\mathfrak r_{ijk}=-4\epsilon_0\mathrm d_{ijk}/\epsilon_{ii}\epsilon_{jj}$ y $\mathfrak s_{ijkl}=-12\epsilon_0\chi^{(3)}_{ijkl}/\epsilon_{ii}\epsilon_{jj}$. Estas relaciones son
generalizaciones de (21.2-11) y (21.3-2), respectivamente. *Pista:* si dos matrices $\mathbf A$ y $\mathbf B$ están
relacionadas por $\mathbf B=\mathbf A^{-1}$, las matrices incrementales $\Delta\mathbf A$ y $\Delta\mathbf B$ están relacionadas por
$\Delta\mathbf B=-\mathbf A^{-1}\Delta\mathbf A\mathbf A^{-1}$.

---

## Relación con Óptica No Lineal

### Mapa temas del programa ↔ secciones de Saleh

| Tema del curso | Referencia principal | Sección(es) de Saleh cap. 21 | Qué aporta Saleh |
|---|---|---|---|
| 4. Introducción, susceptibilidades no lineales, descripción de procesos (SHG, SFG, DFG, OPA/OPO, THG, Kerr), oscilador anarmónico, propiedades de χ | Boyd cap. 1 | 21.1 (p. 875–879), 21.2A–C (879–887), 21.3A (895–896), 21.6 (924–927), 21.7 (927–932) | Expansión (21.1-2) y su conversión a Boyd; recuadro de la ecuación de onda (21.1-6/7); intuición de Born; fotones y Manley–Rowe (21.2-16…19); tensor $\mathrm d_{ijk}$, notación contraída y Tabla 21.6-3; oscilador anarmónico (21.7-8) y regla de Miller (21.7-14) (Boyd §1.4, §1.5) |
| 5. Ecuación de onda no lineal, SFG/SHG/DFG, phase matching, QPM, ondas acopladas, Manley–Rowe | Boyd cap. 2 | 21.1 (ec. de onda), 21.2D–E (887–894), 21.4 (905–917) | SHG exacto tanh² (21.4-32/34), eficiencia $C^2(L^2/A)P$ (21.4-36), sinc² con $\Delta k$ (21.4-38) — ojo con $L_c=2\pi/\Delta k$ vs Boyd $2/\Delta k$; curvas de sintonía por birrefringencia (21.2-21…25), ancho de banda por índices de grupo (21.2-30); QPM y PPLN (21.2-31…34, mejora $4(L/\Lambda)^2$); OFC (sin²), OPA (cosh²), umbrales SRO/DRO (21.4-49/52) |
| 6. Índice dependiente de la intensidad, $n_2$, autoenfoque, SPM, solitones espaciales | Boyd §4.1, §4.2, §7.1, §7.2 | 21.3A–C (895–900), 21.5A (917–919) | $n_2=3\eta_0\chi^{(3)}/n^2\epsilon_0$ (21.3-6) ≡ Boyd (4.1.19); XPM factor 2 (21.3-17) y con tres ondas (21.3-18); SPM $\Delta\varphi=-2\pi n_2LP/\lambda_0A$ (21.3-8); lente Kerr (Ej. 21.3-2); NLSE espacial (21.3-11) y solitón sech (21.3-12) con $z_0$ de Rayleigh; Kerr en FWM $\bar n_q=n+n_2(2I-I_q)$ (21.5-14); $\chi^{(3)}$ complejo → ganancia Raman (21.3-15) |
| 7–10. Propagación en fibra: dispersión, SPM, XPM, FWM, solitones temporales (NLSE) | Agrawal, *Nonlinear Fiber Optics* | 21.3B–E (896–905), 21.5 (917–923), 21.7 (927–932); remite a 22.5 (pulsos en medios NL), 22.5B (solitones temporales), 24.2E (solitones en comunicaciones), 24.3C (XPM en WDM) | FWM: condiciones (21.3-23/25), fuentes con términos Kerr (21.5-6), OPA en fibra con 4 fotones (Fig. 21.3-5, (21.5-16…21): crecimiento cuadrático y amplificador sensible a fase), ecuaciones en magnitud‑fase (21.5-22) con invariantes; conjugación de fase (21.3-32, 21.5-33/34) como holografía dinámica; la NLSE espacial (21.3-11) es el análogo exacto de la NLSE temporal de Agrawal con $\partial^2/\partial x^2\leftrightarrow-\beta_2\partial^2/\partial T^2$ |

### Para el proyecto final (anillos add‑drop en Si₃N₄, dispersión de guías, supercontinuo, sensado de índice)

- **Si₃N₄ es centrosimétrico (amorfo):** $\mathrm d=0$ (p. 877); la no linealidad relevante es $\chi^{(3)}$ (Kerr, FWM,
  Raman débil). El capítulo no da $n_2$ de Si₃N₄ (valor de literatura ≈ $2.4\times10^{-19}$ m²/W, fuera del libro);
  sí da el marco: $n(I)=n+n_2I$ (21.3-7), SPM (21.3-8), XPM (21.3-17), FWM (21.3-23/25) y el término Kerr
  en las ecuaciones acopladas (21.5-9…14).
- **Potencia para fase $\pi$ en guías:** $P_\pi=\lambda_0A/2Ln_2$ (p. 896) es la estimación directa para una guía de
  Si₃N₄ (con $A\to A_{\rm eff}$ y $L\to$ longitud efectiva en el anillo, multiplicada por el factor de
  realce de la cavidad). Sirve para decidir si el desplazamiento Kerr de la resonancia es despreciable
  frente al desplazamiento por índice del analito ($\Delta n_{\rm clad}$ 1.33→1.37) en el refractómetro de volumen.
- **Dispersión y phase matching de FWM:** la condición $\mathbf k_1+\mathbf k_2=\mathbf k_3+\mathbf k_4$ (21.3-25) con el término
  Kerr (21.5-14) es la base de la amplificación paramétrica en anillo (peines Kerr); el ancho de banda de
  phase matching en función de índices de grupo (21.2-29/30) muestra por qué la GVD de la guía
  ($\beta_2$, ingeniería de dispersión por sección transversal) decide qué procesos se sostienen. La
  tolerancia $|\Delta k|\le2\pi/L$ (p. 891) traduce la longitud del anillo en ancho espectral de FWM.
- **Supercontinuo:** combinación de SPM (21.3-8), XPM (21.3-17), FWM (21.3-22/26), Raman (21.3-15) y GVD;
  Saleh remite a 22.5 para pulsos y a 22.5B para solitones temporales (la fisión de solitones es el
  mecanismo dominante en SC con dispersión anómala). La NLSE espacial (21.3-11) con su solución sech
  (21.3-12) es la plantilla matemática: cambiar $x\to T$ y $1/k\to-\beta_2$.
- **Sensado de índice de refracción (bulk):** el capítulo no trata sensores, pero sí los dos efectos
  parásitos que compiten con el corrimiento de resonancia por el analito: Kerr (autodesplazamiento de la
  resonancia con la potencia, 21.3A) y XPM entre bomba y sonda (21.3C). Ambos escalan con $n_2I$; con $I$
  de sondeo baja (μW–mW en el anillo) son despreciables frente a $\Delta n_{\rm clad}\sim10^{-2}$.
- **Convenciones al cruzar con Boyd/Agrawal:** usar la tabla de la sección "Convenciones" de estas notas
  antes de mezclar $\chi^{(3)}$ de Saleh (C·m/V³) con $\chi^{(3)}$ de Boyd (m²/V²) o $\gamma=n_2\omega_0/(cA_{\rm eff})$ de Agrawal.
  El $n_2$ en m²/W es el mismo en los tres autores (salvo la variante $n_2|E|^2/2$ de la nota p. 896).
