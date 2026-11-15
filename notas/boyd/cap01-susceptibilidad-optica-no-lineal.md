# Capítulo 1 — The Nonlinear Optical Susceptibility (Boyd, 3.ª ed.)

Páginas del libro 1–67 (PDF 19–85; la p. 68/PDF 86 está en blanco y el cap. 2 empieza en la p. 69/PDF 87). Leído el 2026-11-14.

Fuente: R. W. Boyd, *Nonlinear Optics*, 3.ª ed., Academic Press (Elsevier), 2008, cap. 1.
Las citas de página son páginas del libro (sumar 18 para la página del PDF).

**Convención del libro (SI).** Campos reales con tilde: $\tilde E(t)=E e^{-i\omega t}+\text{c.c.}$
(la amplitud compleja $E$ es la **mitad** de la amplitud de pico real), polarización
$\tilde P(t)=\epsilon_0[\chi^{(1)}\tilde E+\chi^{(2)}\tilde E^2+\chi^{(3)}\tilde E^3+\cdots]$,
$\tilde P(t)=\sum_n P(\omega_n)e^{-i\omega_n t}$ (suma sobre frecuencias positivas y negativas),
intensidad $I=2n\epsilon_0 c|E|^2$. Sin tilde: constantes, cantidades lentamente variables y
amplitudes de Fourier (nota al pie, p. 2). Unidades: $\chi^{(1)}$ adimensional, $\chi^{(2)}$ en m/V,
$\chi^{(3)}$ en m²/V².

> **Para el examen (tema 4 del programa = Boyd cap. 1).** Lo esencial: (i) expansión de
> $\tilde P$ y órdenes de magnitud $\chi^{(2)}\sim 1/E_{\rm at}$, $\chi^{(3)}\sim 1/E_{\rm at}^2$;
> (ii) amplitudes $P(\omega_n)$ de SHG/SFG/DFG/OR y de los procesos de $\chi^{(3)}$ con sus
> factores de degeneración 1, 3, 6; (iii) oscilador anarmónico (centro y no centrosimétrico),
> regla de Miller; (iv) simetrías de $\chi^{(2)}$ (realidad, permutación intrínseca y total,
> Kleinman, espaciales), notación contraída $d_{il}$ y $d_{\rm eff}$; (v) $\chi^{(3)}$ isótropo,
> $\chi_{1122},\chi_{1212},\chi_{1221}$, coeficientes $A$, $B$ de Maker–Terhune; (vi) respuesta en el
> tiempo y Kramers–Kronig.

---

## Resumen del capítulo

El capítulo define la susceptibilidad óptica no lineal y sus propiedades. Parte de la expansión de la polarización en potencias del campo, $\tilde P=\epsilon_0[\chi^{(1)}\tilde E+\chi^{(2)}\tilde E^2+\chi^{(3)}\tilde E^3+\cdots]$, válida para un medio sin pérdidas ni dispersión, y estima los órdenes de magnitud $\chi^{(2)}\sim1/E_{\rm at}\approx2\times10^{-12}$ m/V y $\chi^{(3)}\sim1/E_{\rm at}^2\approx4\times10^{-24}$ m²/V² a partir del campo atómico $E_{\rm at}=5.14\times10^{11}$ V/m (§1.1). En §1.2 describe cualitativamente los procesos: SHG, SFG, DFG (amplificación paramétrica), OPO y rectificación óptica, que vienen de $\chi^{(2)}$; THG, índice dependiente de la intensidad $n=n_0+n_2I$ y autoenfoque, y mezcla general de tres frecuencias (44 componentes con factores de degeneración 1, 3 y 6), que vienen de $\chi^{(3)}$. Distingue procesos paramétricos (susceptibilidad real, sin transferencia de población) de no paramétricos (absorción saturable, biestabilidad, absorción de dos fotones, Raman estimulado). La §1.3 da la definición formal tensorial de $\chi^{(2)}_{ijk}(\omega_n+\omega_m,\omega_n,\omega_m)$ y $\chi^{(3)}_{ijkl}$ para medios dispersivos y con pérdidas, con el factor de degeneración $D$. La §1.4 calcula $\chi^{(1)}$, $\chi^{(2)}$ y $\chi^{(3)}$ con el oscilador de Lorentz anarmónico mediante teoría de perturbaciones: un potencial con término cúbico (medio no centrosimétrico) da $\chi^{(2)}\propto a/[D(\omega_3)D(\omega_1)D(\omega_2)]$, y de ahí la regla de Miller y $\chi^{(2)}\approx6.9\times10^{-12}$ m/V. Un potencial con término cuártico (centrosimétrico e isótropo) da $\tilde r^{(2)}=0$ y un $\chi^{(3)}_{ijkl}\propto(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})$, con $\chi^{(3)}\approx344$ pm²/V². La §1.5 estudia las propiedades formales: realidad de los campos, permutación intrínseca y, para medios sin pérdidas, $\chi$ real y permutación total (deducida también de la densidad de energía); además la simetría de Kleinman (sin dispersión), la notación contraída $d_{il}$ ($d=\chi^{(2)}/2$), $d_{\rm eff}$ (clase 3m, tipo I y II) y las restricciones de la simetría espacial: formas de $\chi^{(1)}$ por sistema cristalino (Tabla 1.5.1), anulación de $\chi^{(2)}$ en medios centrosimétricos, formas de $\chi^{(2)}$ para las 32 clases (Tabla 1.5.2, Fig. 1.5.3), valores medidos de $d$ (Tabla 1.5.3), cúbico no centrosimétrico (GaAs) y clases polares, y formas de $\chi^{(3)}$ (Tabla 1.5.4). La §1.6 formula la respuesta en el dominio del tiempo con funciones respuesta causales $R^{(n)}$, cuyas transformadas de Fourier son las $\chi^{(n)}$. La §1.7 deduce las relaciones de Kramers–Kronig lineales por integración de contorno y muestra que valen solo para algunos procesos no lineales (SHG, THG, índice inducido por un haz auxiliar), pero no para el cambio autoinducido del índice $\chi^{(3)}(\omega;\omega,\omega,-\omega)$.

---

## Secciones

### 1.1 Introduction to Nonlinear Optics (p. 1)

La óptica no lineal estudia los fenómenos que ocurren porque la luz modifica las propiedades
ópticas del material; típicamente solo la luz láser es suficientemente intensa. El campo nace con
la SHG de Franken *et al.* (1961), poco después del láser de Maiman (1960). (Nota al pie: efectos
no lineales anteriores al láser, p. ej. saturación en la luminiscencia de colorantes, G. N. Lewis
*et al.*, 1941.) "No lineal" = la respuesta depende no linealmente de la intensidad del campo; p. ej.
la intensidad de SHG crece como el cuadrado de la intensidad láser.

**Óptica lineal** (p. 2):
$$\tilde P(t)=\epsilon_0\chi^{(1)}\tilde E(t) \qquad (1.1.1),\ \text{p. 2}$$

**Expansión en serie de potencias**:
$$\tilde P(t)=\epsilon_0\left[\chi^{(1)}\tilde E(t)+\chi^{(2)}\tilde E^2(t)+\chi^{(3)}\tilde E^3(t)+\cdots\right]\equiv \tilde P^{(1)}(t)+\tilde P^{(2)}(t)+\tilde P^{(3)}(t)+\cdots \qquad (1.1.2),\ \text{p. 2}$$

- $\chi^{(2)}$, $\chi^{(3)}$: susceptibilidades no lineales de segundo y tercer orden. Aquí escalares;
  en §1.3 se ve que $\chi^{(1)}$ es tensor de rango 2, $\chi^{(2)}$ de rango 3, etc.
- Supuesto: respuesta **instantánea** (P en $t$ depende solo de $\tilde E$ en $t$). Por Kramers–Kronig
  esto implica medio **sin pérdidas y sin dispersión**; las $\chi$ son constantes. En §1.3 se
  generaliza a medios con dispersión y pérdidas.
- $\tilde P^{(2)}=\epsilon_0\chi^{(2)}\tilde E^2$ (polarización de 2.º orden), $\tilde P^{(3)}=\epsilon_0\chi^{(3)}\tilde E^3$.
- Las interacciones de 2.º orden **solo ocurren en cristales no centrosimétricos** (§1.5). Líquidos,
  gases, sólidos amorfos (vidrio) y muchos cristales tienen simetría de inversión ⇒ $\chi^{(2)}\equiv0$.
  Las de 3.er orden ocurren en medios centro y no centrosimétricos (p. 3).

**Estimación de órdenes de magnitud (no linealidad electrónica, no resonante)** (p. 3). Se espera
que $\tilde P^{(2)}$ sea comparable a $\tilde P^{(1)}$ cuando $\tilde E$ es del orden del campo atómico
característico
$$E_{\rm at}=\frac{e}{4\pi\epsilon_0 a_0^2},\qquad a_0=\frac{4\pi\epsilon_0\hbar^2}{me^2}\ (\text{radio de Bohr}),\qquad E_{\rm at}=5.14\times10^{11}\ \text{V/m}.$$
Entonces $\chi^{(2)}\sim\chi^{(1)}/E_{\rm at}$; con $\chi^{(1)}\sim1$ en materia condensada:
$$\chi^{(2)}\simeq 1.94\times10^{-12}\ \text{m/V} \qquad (1.1.3),\ \text{p. 3}$$
$$\chi^{(3)}\sim\chi^{(1)}/E_{\rm at}^2\simeq 3.78\times10^{-24}\ \text{m}^2/\text{V}^2 \qquad (1.1.4),\ \text{p. 3}$$
Estas predicciones concuerdan bien con valores medidos (Tabla 1.5.3 para $\chi^{(2)}$, Tabla 4.3.1 para
$\chi^{(3)}$). Justificación de $\chi^{(1)}\sim1$: $\chi^{(1)}$ = densidad atómica × polarizabilidad;
$N\sim a_0^{-3}$ y polarizabilidad no resonante $\sim a_0^{3}$. En constantes fundamentales:
$$\chi^{(2)}\simeq\frac{(4\pi\epsilon_0)^3\hbar^4}{m^2e^5},\qquad \chi^{(3)}\simeq\frac{(4\pi\epsilon_0)^6\hbar^8}{m^4e^{10}}$$
(ver Boyd, 1999). (Comprobación: $1/E_{\rm at}=1/5.14\times10^{11}=1.946\times10^{-12}$ m/V y
$1/E_{\rm at}^2=3.785\times10^{-24}$ m²/V², consistente con (1.1.3)–(1.1.4).) Nota al pie: el libro usa
SI salvo aviso; el apéndice da la conversión entre sistemas.

**Ecuación de onda con fuente no lineal** (p. 4; se deduce en §2.1):
$$\nabla^2\tilde E-\frac{n^2}{c^2}\frac{\partial^2\tilde E}{\partial t^2}=\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde P^{\rm NL}}{\partial t^2} \qquad (1.1.5),\ \text{p. 4}$$
Ecuación de onda inhomogénea: $\tilde P^{\rm NL}$ actúa como fuente; $\partial^2\tilde P^{\rm NL}/\partial t^2$ mide la
aceleración de las cargas (consistente con Larmor: cargas aceleradas radian).

**Validez de la serie.** La serie (1.1.2) no necesariamente converge: p. ej. excitación resonante
(saturación, cap. 6), o campos comparables a $E_{\rm at}$ (fotoionización fuerte). La intensidad
asociada a un campo de pico $E_{\rm at}$ es
$$I_{\rm at}=\tfrac12\epsilon_0 cE_{\rm at}^2=3.5\times10^{20}\ \text{W/m}^2=3.5\times10^{16}\ \text{W/cm}^2 \qquad (1.1.6),\ \text{p. 4}$$
(campos superintensos: cap. 13). Nota: aquí $E_{\rm at}$ es amplitud de pico real, de ahí el factor ½.

### 1.2 Descriptions of Nonlinear Optical Processes (p. 4)

Descripciones cualitativas de procesos no lineales; para los que ocurren en medios sin pérdidas se
indica cómo se describen con (1.1.2) (nota al pie: (1.1.2) solo vale sin pérdidas ni dispersión).

#### 1.2.1 Second-Harmonic Generation (p. 5)

Campo incidente
$$\tilde E(t)=Ee^{-i\omega t}+\text{c.c.} \qquad (1.2.1)$$
en un cristal con $\chi^{(2)}\neq0$:
$$\tilde P^{(2)}(t)=2\epsilon_0\chi^{(2)}EE^*+\left(\epsilon_0\chi^{(2)}E^2e^{-2i\omega t}+\text{c.c.}\right) \qquad (1.2.2),\ \text{p. 5}$$
(Paso: $\tilde E^2=E^2e^{-2i\omega t}+E^{*2}e^{2i\omega t}+2EE^*$.) Contribución a frecuencia cero
(**rectificación óptica**: crea un campo estático en el cristal; no radia porque su segunda derivada
temporal es nula) y a $2\omega$ (radia el segundo armónico según (1.1.5)). La SHG puede convertir casi
toda la potencia; uso típico: Nd:YAG 1.06 µm → 0.53 µm (p. 6). Fig. 1.2.1: (a) geometría ω → χ⁽²⁾ → ω, 2ω;
(b) diagrama de niveles: dos fotones ω se destruyen y se crea uno 2ω en un solo proceso cuántico; línea
continua = estado base, líneas discontinuas = **niveles virtuales** (no son autoestados del átomo sino
energía combinada de un autoestado y uno o más fotones). Teoría completa en §2.6.

#### 1.2.2 Sum- and Difference-Frequency Generation (p. 6)

$$\tilde E(t)=E_1e^{-i\omega_1t}+E_2e^{-i\omega_2t}+\text{c.c.} \qquad (1.2.3)$$
$$\tilde P^{(2)}(t)=\epsilon_0\chi^{(2)}\tilde E(t)^2 \qquad (1.2.4)$$
$$\tilde P^{(2)}(t)=\epsilon_0\chi^{(2)}\left[E_1^2e^{-2i\omega_1t}+E_2^2e^{-2i\omega_2t}+2E_1E_2e^{-i(\omega_1+\omega_2)t}+2E_1E_2^*e^{-i(\omega_1-\omega_2)t}+\text{c.c.}\right]+2\epsilon_0\chi^{(2)}\left[E_1E_1^*+E_2E_2^*\right] \qquad (1.2.5),\ \text{p. 6}$$
Notación
$$\tilde P^{(2)}(t)=\sum_nP(\omega_n)e^{-i\omega_nt} \qquad (1.2.6),\ \text{p. 7}$$
(suma sobre frecuencias positivas y negativas). Amplitudes:
$$\begin{aligned}
P(2\omega_1)&=\epsilon_0\chi^{(2)}E_1^2 &&(\text{SHG}),\\
P(2\omega_2)&=\epsilon_0\chi^{(2)}E_2^2 &&(\text{SHG}),\\
P(\omega_1+\omega_2)&=2\epsilon_0\chi^{(2)}E_1E_2 &&(\text{SFG}),\\
P(\omega_1-\omega_2)&=2\epsilon_0\chi^{(2)}E_1E_2^* &&(\text{DFG}),\\
P(0)&=2\epsilon_0\chi^{(2)}(E_1E_1^*+E_2E_2^*) &&(\text{OR}).
\end{aligned}\qquad (1.2.7),\ \text{p. 7}$$
Frecuencias negativas (complejos conjugados de las anteriores, no hace falta llevarlas aparte):
$$P(-2\omega_1)=\epsilon_0\chi^{(2)}E_1^{*2},\ P(-2\omega_2)=\epsilon_0\chi^{(2)}E_2^{*2},\ P(-\omega_1-\omega_2)=2\epsilon_0\chi^{(2)}E_1^*E_2^*,\ P(\omega_2-\omega_1)=2\epsilon_0\chi^{(2)}E_2E_1^* \qquad (1.2.8)$$

*Nota al pie (p. 7), otra convención común*: $\tilde E(t)=\tfrac12(E_1'e^{-i\omega_1t}+E_2'e^{-i\omega_2t}+\text{c.c.})$,
$\tilde P(t)=\tfrac12\sum_nP'(\omega_n)e^{i\omega_nt}$ [se lee $e^{i\omega_nt}$ en el escaneo; por consistencia con el
campo debería ser $e^{-i\omega_nt}$]. Con ella: $P'(2\omega_1)=\tfrac12\epsilon_0\chi^{(2)}E_1'^2$, $P'(2\omega_2)=\tfrac12\epsilon_0\chi^{(2)}E_2'^2$,
$P'(\omega_1+\omega_2)=\epsilon_0\chi^{(2)}E_1'E_2'$, $P'(\omega_1-\omega_2)=\epsilon_0\chi^{(2)}E_1'E_2'^*$, $P'(0)=\epsilon_0\chi^{(2)}(E_1'E_1'^*+E_2'E_2'^*)$:
difieren de (1.2.7) por factores ½. (Es la convención de Saleh y de muchos artículos, con $E'=2E$.)

Hay cuatro componentes no nulas en $P$, pero normalmente solo una radia con intensidad apreciable:
solo se puede satisfacer el **ajuste de fase** (§2.7) para una; se elige con la polarización de entrada
y la orientación del cristal (p. 8).

#### 1.2.3 Sum-Frequency Generation (p. 8)

$$P(\omega_1+\omega_2)=2\epsilon_0\chi^{(2)}E_1E_2 \qquad (1.2.9),\ \text{p. 8}$$
Análogo a SHG con dos ondas distintas. Aplicación: radiación UV sintonizable mezclando un láser visible
fijo con uno visible sintonizable. Fig. 1.2.2: $\omega_3=\omega_1+\omega_2$; niveles: suben $\omega_1$ y $\omega_2$, baja $\omega_3$.
Teoría en §§2.2 y 2.4.

#### 1.2.4 Difference-Frequency Generation (p. 9)

$$P(\omega_1-\omega_2)=2\epsilon_0\chi^{(2)}E_1E_2^* \qquad (1.2.10),\ \text{p. 9}$$
Produce IR sintonizable (visible sintonizable + visible fijo). Diferencia clave con SFG (Fig. 1.2.3b,
$\omega_3=\omega_1-\omega_2$): por conservación de energía, por cada fotón creado en $\omega_3$ se destruye uno en $\omega_1$ (la
mayor) **y se crea uno en $\omega_2$** (la menor) ⇒ la onda de entrada de menor frecuencia se **amplifica**:
DFG = **amplificación paramétrica óptica**. El átomo absorbe $\omega_1$, sube al nivel virtual más alto y decae
por emisión de dos fotones estimulada por el campo $\omega_2$. Sin $\omega_2$ aplicado también puede ocurrir emisión
espontánea de dos fotones desde el nivel virtual (campos mucho más débiles): **fluorescencia paramétrica**
(Byer y Harris, 1968; Harris *et al.*, 1967) (p. 10). Teoría en §2.5.

#### 1.2.5 Optical Parametric Oscillation (p. 10)

Si el cristal de DFG se pone en un resonador (Fig. 1.2.4; espejos de alta reflectividad en $\omega_2$ y/o
$\omega_3$), los campos $\omega_2$/$\omega_3$ crecen: **oscilador paramétrico óptico (OPO)**. Útil en el IR. Sintonizable
porque cualquier $\omega_2<\omega_1$ satisface $\omega_2+\omega_3=\omega_1$ para algún $\omega_3$; en la práctica se elige la salida
con el ajuste de fase (§2.7), p. ej. orientando el cristal. Terminología: $\omega_1$ **bombeo** (pump), salida
deseada **señal** (signal), la otra **idler**.

#### 1.2.6 Third-Order Nonlinear Optical Processes (p. 10)

$$\tilde P^{(3)}(t)=\epsilon_0\chi^{(3)}\tilde E(t)^3 \qquad (1.2.11)$$
Caso monocromático:
$$\tilde E(t)=\mathcal E\cos\omega t \qquad (1.2.12),\ \text{p. 11}$$
con $\cos^3\omega t=\tfrac14\cos3\omega t+\tfrac34\cos\omega t$:
$$\tilde P^{(3)}(t)=\tfrac14\epsilon_0\chi^{(3)}\mathcal E^3\cos3\omega t+\tfrac34\epsilon_0\chi^{(3)}\mathcal E^3\cos\omega t \qquad (1.2.13),\ \text{p. 11}$$
(Aquí $\mathcal E$ es amplitud real de pico: $\mathcal E=2|E|$.)

#### 1.2.7 Third-Harmonic Generation (p. 11)

Primer término de (1.2.13): respuesta a $3\omega$. Fig. 1.2.5: se destruyen tres fotones ω y se crea uno 3ω.

#### 1.2.8 Intensity-Dependent Refractive Index (p. 11)

Segundo término: contribución no lineal a la polarización en $\omega$ ⇒ índice dependiente de la intensidad
(§4.1):
$$n=n_0+n_2I \qquad (1.2.14\text{a}),\ \text{p. 11}$$
$$n_2=\frac{3}{2n_0^2\epsilon_0c}\chi^{(3)} \qquad (1.2.14\text{b}),\ \text{p. 12}$$
con $n_0$ índice lineal y $I=\tfrac12n_0\epsilon_0c\mathcal E^2$ la intensidad incidente.

*Derivación rápida (no está en el texto; se hace en §4.1):* con $\tilde E=\mathcal E\cos\omega t$, la polarización
total en $\omega$ es $\epsilon_0[\chi^{(1)}+\tfrac34\chi^{(3)}\mathcal E^2]\mathcal E\cos\omega t$ ⇒ $n^2=1+\chi^{(1)}+\tfrac34\chi^{(3)}\mathcal E^2$;
$n\simeq n_0+\tfrac{3\chi^{(3)}\mathcal E^2}{8n_0}$; sustituyendo $\mathcal E^2=2I/(n_0\epsilon_0c)$ se obtiene $n_2=3\chi^{(3)}/(4n_0^2\epsilon_0c)$.
[Duda de lectura: el escaneo dice claramente $3/(2n_0^2\epsilon_0c)$ en (1.2.14b) y $I=\tfrac12n_0\epsilon_0c\mathcal E^2$.
Con la amplitud compleja de Boyd, $I=2n_0\epsilon_0c|E|^2$, $\mathcal E=2|E|$, y la §4.1 (ec. 4.1.19) da
$n_2=3\chi^{(3)}/(4n_0^2\epsilon_0c)$. El factor 2 de diferencia en (1.2.14b) parece una errata del texto (ver
"Erratas"); usar $n_2=\dfrac{3}{4n_0^2\epsilon_0c}\chi^{(3)}$, y verificar con el cap. 4.]

**Autoenfoque** (Fig. 1.2.6): un haz con perfil transversal no uniforme en un medio con $n_2>0$ ve al
material como lente positiva; los rayos se curvan unos hacia otros. Importante porque la intensidad en el
foco suele dañar el material. §7.1.

#### 1.2.9 Third-Order Interactions (General Case) (p. 12)

$$\tilde P^{(3)}(t)=\epsilon_0\chi^{(3)}\tilde E^3(t) \qquad (1.2.15\text{a})$$
$$\tilde E(t)=E_1e^{-i\omega_1t}+E_2e^{-i\omega_2t}+E_3e^{-i\omega_3t}+\text{c.c.} \qquad (1.2.15\text{b})$$
$\tilde E^3$ contiene **44 componentes de frecuencia** distintas (contando positivas y negativas por separado):
$\omega_1,\omega_2,\omega_3,3\omega_1,3\omega_2,3\omega_3,(\omega_1+\omega_2+\omega_3),(\omega_1+\omega_2-\omega_3),(\omega_1+\omega_3-\omega_2),(\omega_2+\omega_3-\omega_1),(2\omega_1\pm\omega_2),(2\omega_1\pm\omega_3),
(2\omega_2\pm\omega_1),(2\omega_2\pm\omega_3),(2\omega_3\pm\omega_1),(2\omega_3\pm\omega_2)$ y la negativa de cada una (22 × 2 = 44).
Con
$$\tilde P^{(3)}(t)=\sum_nP(\omega_n)e^{-i\omega_nt} \qquad (1.2.16),\ \text{p. 13}$$
las amplitudes para frecuencias positivas son
$$\begin{aligned}
P(\omega_1)&=\epsilon_0\chi^{(3)}(3E_1E_1^*+6E_2E_2^*+6E_3E_3^*)E_1,\\
P(\omega_2)&=\epsilon_0\chi^{(3)}(6E_1E_1^*+3E_2E_2^*+6E_3E_3^*)E_2,\\
P(\omega_3)&=\epsilon_0\chi^{(3)}(6E_1E_1^*+6E_2E_2^*+3E_3E_3^*)E_3,\\
P(3\omega_1)&=\epsilon_0\chi^{(3)}E_1^3,\quad P(3\omega_2)=\epsilon_0\chi^{(3)}E_2^3,\quad P(3\omega_3)=\epsilon_0\chi^{(3)}E_3^3,\\
P(\omega_1+\omega_2+\omega_3)&=6\epsilon_0\chi^{(3)}E_1E_2E_3,\\
P(\omega_1+\omega_2-\omega_3)&=6\epsilon_0\chi^{(3)}E_1E_2E_3^*,\\
P(\omega_1+\omega_3-\omega_2)&=6\epsilon_0\chi^{(3)}E_1E_3E_2^*,\\
P(\omega_2+\omega_3-\omega_1)&=6\epsilon_0\chi^{(3)}E_2E_3E_1^*,\\
P(2\omega_1+\omega_2)&=3\epsilon_0\chi^{(3)}E_1^2E_2, \quad P(2\omega_1+\omega_3)=3\epsilon_0\chi^{(3)}E_1^2E_3,\\
P(2\omega_2+\omega_1)&=3\epsilon_0\chi^{(3)}E_2^2E_1, \quad P(2\omega_2+\omega_3)=3\epsilon_0\chi^{(3)}E_2^2E_3,\\
P(2\omega_3+\omega_1)&=3\epsilon_0\chi^{(3)}E_3^2E_1, \quad P(2\omega_3+\omega_2)=3\epsilon_0\chi^{(3)}E_3^2E_2,\\
P(2\omega_1-\omega_2)&=3\epsilon_0\chi^{(3)}E_1^2E_2^*, \quad P(2\omega_1-\omega_3)=3\epsilon_0\chi^{(3)}E_1^2E_3^*,\\
P(2\omega_2-\omega_1)&=3\epsilon_0\chi^{(3)}E_2^2E_1^*, \quad P(2\omega_2-\omega_3)=3\epsilon_0\chi^{(3)}E_2^2E_3^*,\\
P(2\omega_3-\omega_1)&=3\epsilon_0\chi^{(3)}E_3^2E_1^*, \quad P(2\omega_3-\omega_2)=3\epsilon_0\chi^{(3)}E_3^2E_2^*.
\end{aligned}\qquad (1.2.17),\ \text{p. 13}$$
Reglas: (i) el argumento de frecuencia de $P$ es la suma de las frecuencias de los campos del lado derecho,
asociando frecuencia negativa a la amplitud conjugada; (ii) el factor numérico (1, 3 o 6) es el **número de
permutaciones distintas** de las frecuencias de campo que contribuyen a ese término. (Ej.: en $P(\omega_1)$ el término
$|E_1|^2E_1$ viene de $(\omega_1,\omega_1,-\omega_1)$: 3 permutaciones; $|E_2|^2E_1$ de $(\omega_1,\omega_2,-\omega_2)$: 3! = 6.) Esto explica
que la XPM sea el doble de la SPM ($6$ vs $3$). Fig. 1.2.7: (a) $\omega_4=\omega_1+\omega_2+\omega_3$; (b) $\omega_4=\omega_1+\omega_2-\omega_3$ (suben
$\omega_1,\omega_2$; bajan $\omega_3,\omega_4$).

#### 1.2.10 Parametric versus Nonparametric Processes (p. 13)

**Paramétrico**: estados cuánticos inicial y final del sistema idénticos; la población sale del estado base
solo durante intervalos breves en un nivel virtual, de duración $\sim\hbar/\delta E$ ($\delta E$ = distancia del nivel
virtual al nivel real más cercano). **No paramétrico**: hay transferencia de población entre niveles reales.
Diferencias (p. 14): los paramétricos siempre pueden describirse con una susceptibilidad **real**; los no
paramétricos con una **compleja** (§1.3). En los paramétricos la energía de los fotones se conserva; en los
no paramétricos no necesariamente (se intercambia energía con el medio), por eso los diagramas de niveles
son menos definitorios para ellos. Ejemplo (p. 15): en el índice lineal, la parte real responde a procesos
paramétricos y la imaginaria (absorción: población del base al excitado) a no paramétricos. Todos los
procesos descritos hasta 1.2.9 son paramétricos; los de 1.2.11–1.2.14 son no paramétricos.

#### 1.2.11 Saturable Absorption (p. 15)

$$\alpha=\frac{\alpha_0}{1+I/I_s} \qquad (1.2.18),\ \text{p. 15}$$
$\alpha_0$: absorción a baja intensidad; $I_s$: intensidad de saturación (forma válida, p. ej., para ensanchamiento
homogéneo de una transición atómica simple).

**Biestabilidad óptica** (Figs. 1.2.8–1.2.9): absorbente saturable dentro de un Fabry–Perot. Al subir $I_{\rm in}$ el
campo interno crece, baja la absorción y crece aún más el campo; al bajar $I_{\rm in}$ el campo interno se mantiene
alto porque la absorción ya está reducida ⇒ curva $I_{\rm out}$ vs $I_{\rm in}$ con histéresis: en un rango de entradas
hay más de una salida posible (rama intermedia discontinua inestable). §7.3.

#### 1.2.12 Two-Photon Absorption (p. 16)

Transición del base a un excitado por absorción simultánea de dos fotones (Fig. 1.2.10). Sección eficaz
$$\sigma=\sigma^{(2)}I \qquad (1.2.19),\ \text{p. 16}$$
(en óptica lineal $\sigma$ es constante). Con $R=\sigma I/\hbar\omega$:
$$R=\frac{\sigma^{(2)}I^2}{\hbar\omega} \qquad (1.2.20),\ \text{p. 16}$$
la tasa de transición escala con el cuadrado de la intensidad.
Útil en espectroscopía para ubicar niveles no conectados al base por transición de un fotón (p. 17).
Observada por primera vez por Kaiser y Garrett (1961). (Relevante para Si a 1550 nm: TPA, ver
"Relación con el proyecto".)

#### 1.2.13 Stimulated Raman Scattering (p. 17)

Fig. 1.2.11: se aniquila un fotón $\omega$ y se crea uno en la frecuencia **Stokes** $\omega_s=\omega-\omega_v$, dejando la molécula
(o átomo) en un estado excitado de energía $\hbar\omega_v$ ($v$ por "vibracional": se estudió primero en moléculas).
Eficiencia alta: a menudo 10 % o más de la potencia pasa a Stokes; el Raman espontáneo es muchos órdenes de
magnitud menos eficiente. Cap. 10. Otros procesos estimulados (Brillouin, Rayleigh): cap. 9.

### 1.3 Formal Definition of the Nonlinear Susceptibility (p. 17)

(1.1.2) solo vale sin pérdidas ni dispersión; en general la susceptibilidad es **compleja** y relaciona
amplitudes complejas de campo y polarización.

Campo como suma discreta de componentes:
$$\tilde{\mathbf E}(\mathbf r,t)=\sum_n{}'\,\tilde{\mathbf E}_n(\mathbf r,t) \qquad (1.3.1),\ \text{p. 18}$$
$$\tilde{\mathbf E}_n(\mathbf r,t)=\mathbf E_n(\mathbf r)e^{-i\omega_nt}+\text{c.c.} \qquad (1.3.2)$$
(la prima: solo frecuencias positivas). Amplitud lentamente variable:
$$\mathbf E_n(\mathbf r)=\mathbf A_ne^{i\mathbf k_n\cdot\mathbf r} \qquad (1.3.3)$$
$$\tilde{\mathbf E}(\mathbf r,t)=\sum_n{}'\,\mathbf A_ne^{i(\mathbf k_n\cdot\mathbf r-\omega_nt)}+\text{c.c.} \qquad (1.3.4)$$
Notación alternativa:
$$\mathbf E_n=\mathbf E(\omega_n),\quad \mathbf A_n=\mathbf A(\omega_n) \qquad (1.3.5);\qquad \mathbf E(-\omega_n)=\mathbf E(\omega_n)^*,\quad \mathbf A(-\omega_n)=\mathbf A(\omega_n)^* \qquad (1.3.6)$$
$$\tilde{\mathbf E}(\mathbf r,t)=\sum_n\mathbf E(\omega_n)e^{-i\omega_nt}=\sum_n\mathbf A(\omega_n)e^{i(\mathbf k_n\cdot\mathbf r-\omega_nt)} \qquad (1.3.7)$$
(suma sin prima: frecuencias positivas y negativas). Ejemplo:
$$\tilde{\mathbf E}(\mathbf r,t)=\mathcal E\cos(\mathbf k\cdot\mathbf r-\omega t) \qquad (1.3.8)$$
$$\mathbf E(\omega)=\tfrac12\mathcal Ee^{i\mathbf k\cdot\mathbf r},\quad \mathbf E(-\omega)=\tfrac12\mathcal Ee^{-i\mathbf k\cdot\mathbf r} \qquad (1.3.9);\qquad \mathbf A(\omega)=\tfrac12\mathcal E,\quad \mathbf A(-\omega)=\tfrac12\mathcal E \qquad (1.3.10),\ \text{p. 19}$$
Los factores ½ aparecen porque la amplitud física $\mathcal E$ se reparte por igual entre frecuencias positivas y
negativas. Polarización:
$$\tilde{\mathbf P}(\mathbf r,t)=\sum_n\mathbf P(\omega_n)e^{-i\omega_nt} \qquad (1.3.11)$$

**Definición del tensor $\chi^{(2)}$**:
$$P_i(\omega_n+\omega_m)=\epsilon_0\sum_{jk}\sum_{(nm)}\chi^{(2)}_{ijk}(\omega_n+\omega_m,\omega_n,\omega_m)E_j(\omega_n)E_k(\omega_m) \qquad (1.3.12),\ \text{p. 19}$$
$ijk$: componentes cartesianas. $(nm)$: se suma sobre $n,m$ manteniendo fija la suma $\omega_n+\omega_m$ (cada una
puede variar). $E(\omega_n)E(\omega_m)\propto e^{-i(\omega_n+\omega_m)t}$, de ahí la frecuencia de la polarización. Por convención
$\chi^{(2)}$ lleva tres argumentos aunque el primero es la suma de los otros dos; a veces se escribe
$\chi^{(2)}(\omega_3;\omega_2,\omega_1)$ o $\chi^{(2)}(\omega_3=\omega_2+\omega_1)$.

**Ejemplo 1: SFG** ($\omega_3=\omega_1+\omega_2$). Sumando sobre $\omega_n,\omega_m$ (dos ordenamientos):
$$P_i(\omega_3)=\epsilon_0\sum_{jk}\left[\chi^{(2)}_{ijk}(\omega_3,\omega_1,\omega_2)E_j(\omega_1)E_k(\omega_2)+\chi^{(2)}_{ijk}(\omega_3,\omega_2,\omega_1)E_j(\omega_2)E_k(\omega_1)\right] \qquad (1.3.13),\ \text{p. 20}$$
$j,k$ mudos ⇒ se intercambian en el 2.º término; con la **simetría de permutación intrínseca** (ver (1.5.6))
$$\chi^{(2)}_{ijk}(\omega_m+\omega_n,\omega_m,\omega_n)=\chi^{(2)}_{ikj}(\omega_m+\omega_n,\omega_n,\omega_m) \qquad (1.3.14)$$
se obtiene
$$P_i(\omega_3)=2\epsilon_0\sum_{jk}\chi^{(2)}_{ijk}(\omega_3,\omega_1,\omega_2)E_j(\omega_1)E_k(\omega_2) \qquad (1.3.15)$$
y con ambos campos en $x$:
$$P_i(\omega_3)=2\epsilon_0\chi^{(2)}_{ixx}(\omega_3,\omega_1,\omega_2)E_x(\omega_1)E_x(\omega_2) \qquad (1.3.16)$$

**Ejemplo 2: SHG** ($\omega_3=2\omega_1$): un solo término en la suma,
$$P_i(\omega_3)=\epsilon_0\sum_{jk}\chi^{(2)}_{ijk}(\omega_3,\omega_1,\omega_1)E_j(\omega_1)E_k(\omega_1) \qquad (1.3.17)$$
$$P_i(\omega_3)=\epsilon_0\chi^{(2)}_{ixx}(\omega_3,\omega_1,\omega_1)E_x(\omega_1)^2 \qquad (1.3.18)$$
El factor 2 aparece en SFG y no en SHG, y persiste aunque $\omega_2\to\omega_1$, porque por convención
$\chi^{(2)}(\omega_3,\omega_1,\omega_2)\to\chi^{(2)}(\omega_3,\omega_1,\omega_1)$. (Igual en (1.2.7): $P(2\omega_2)$ vs $P(\omega_1+\omega_2)$.) Es razonable: dos campos
distintos (de igual amplitud) dan más polarización que uno solo porque la intensidad total es mayor (p. 21).

En general, con el **factor de degeneración** $D$ = número de permutaciones distintas de las frecuencias
aplicadas $\omega_n,\omega_m$:
$$P_i(\omega_n+\omega_m)=\epsilon_0D\sum_{jk}\chi^{(2)}_{ijk}(\omega_n+\omega_m,\omega_n,\omega_m)E_j(\omega_n)E_k(\omega_m) \qquad (1.3.19),\ \text{p. 21}$$
**Tercer orden**:
$$P_i(\omega_o+\omega_n+\omega_m)=\epsilon_0\sum_{jkl}\sum_{(mno)}\chi^{(3)}_{ijkl}(\omega_o+\omega_n+\omega_m,\omega_o,\omega_n,\omega_m)E_j(\omega_o)E_k(\omega_n)E_l(\omega_m) \qquad (1.3.20)$$
$$P_i(\omega_o+\omega_n+\omega_m)=\epsilon_0D\sum_{jkl}\chi^{(3)}_{ijkl}(\omega_o+\omega_n+\omega_m,\omega_o,\omega_n,\omega_m)E_j(\omega_o)E_k(\omega_n)E_l(\omega_m) \qquad (1.3.21)$$
con $D$ = número de permutaciones distintas de $\omega_m,\omega_n,\omega_o$ (1, 3 o 6, como en (1.2.17)).

### 1.4 Nonlinear Susceptibility of a Classical Anharmonic Oscillator (p. 21)

El modelo de Lorentz (átomo = oscilador armónico) describe muy bien las propiedades lineales de vapores
atómicos y sólidos no metálicos. Se extiende permitiendo una fuerza restauradora no lineal; el análisis
depende de si el medio tiene simetría de inversión (nota al pie: ver §1.5, (1.5.31)–(1.5.35)).
No centrosimétrico ⇒ no linealidad de 2.º orden; centrosimétrico ⇒ la mínima es de 3.er orden.
Tratamiento similar a Owyoung (1971). **Limitación** (p. 22): una sola frecuencia de resonancia $\omega_0$ por
átomo (la teoría cuántica del cap. 3 tiene muchas), así que no describe la estructura resonante completa
(p. ej. resonancias simultáneas de uno y dos fotones); sí describe bien el caso en que **todas las
frecuencias ópticas son mucho menores que la resonancia electrónica más baja**.

#### 1.4.1 Noncentrosymmetric Media (p. 22)

Ecuación de movimiento del electrón (posición $\tilde x$, carga $-e$):
$$\ddot{\tilde x}+2\gamma\dot{\tilde x}+\omega_0^2\tilde x+a\tilde x^2=-e\tilde E(t)/m \qquad (1.4.1),\ \text{p. 22}$$
Amortiguamiento $-2m\gamma\dot{\tilde x}$ (nota al pie: el 2 hace que $\gamma$ sea la tasa de amortiguamiento dipolar;
$2\gamma$ = FWHM en frecuencia angular del perfil de absorción en el límite lineal). Fuerza restauradora
$$\tilde F_{\rm restoring}=-m\omega_0^2\tilde x-ma\tilde x^2 \qquad (1.4.2)$$
($a$ = intensidad de la no linealidad; términos lineal y cuadrático de la serie de Taylor de la fuerza).
Potencial
$$U(\tilde x)=-\int\tilde F_{\rm restoring}\,d\tilde x=\tfrac12m\omega_0^2\tilde x^2+\tfrac13ma\tilde x^3 \qquad (1.4.3)$$
Fig. 1.4.1 (p. 23): potencial real asimétrico vs. parábola (más blando a un lado, más duro al otro). Solo
describe medios no centrosimétricos porque $U$ tiene potencias pares e impares; en uno centrosimétrico
$U(\tilde x)=U(-\tilde x)$ ⇒ solo potencias pares. Aproximación escalar (el carácter tensorial exige supuestos de simetría).

Campo aplicado:
$$\tilde E(t)=E_1e^{-i\omega_1t}+E_2e^{-i\omega_2t}+\text{c.c.} \qquad (1.4.4)$$
No hay solución general; si el campo es débil, $a\tilde x^2\ll\omega_0^2\tilde x$ y se usa perturbación (análogo a
Rayleigh–Schrödinger): $\tilde E\to\lambda\tilde E$, $0\le\lambda\le1$, $\lambda=1$ al final:
$$\ddot{\tilde x}+2\gamma\dot{\tilde x}+\omega_0^2\tilde x+a\tilde x^2=-\lambda e\tilde E(t)/m \qquad (1.4.5)$$
$$\tilde x=\lambda\tilde x^{(1)}+\lambda^2\tilde x^{(2)}+\lambda^3\tilde x^{(3)}+\cdots \qquad (1.4.6),\ \text{p. 24}$$
Igualando potencias de $\lambda$ (debe valer para todo $\lambda$):
$$\ddot{\tilde x}^{(1)}+2\gamma\dot{\tilde x}^{(1)}+\omega_0^2\tilde x^{(1)}=-e\tilde E(t)/m \qquad (1.4.7\text{a})$$
$$\ddot{\tilde x}^{(2)}+2\gamma\dot{\tilde x}^{(2)}+\omega_0^2\tilde x^{(2)}+a[\tilde x^{(1)}]^2=0 \qquad (1.4.7\text{b})$$
$$\ddot{\tilde x}^{(3)}+2\gamma\dot{\tilde x}^{(3)}+\omega_0^2\tilde x^{(3)}+2a\tilde x^{(1)}\tilde x^{(2)}=0,\quad\text{etc.} \qquad (1.4.7\text{c})$$
(Paso: $a\tilde x^2=a[\lambda^2\tilde x^{(1)2}+2\lambda^3\tilde x^{(1)}\tilde x^{(2)}+\dots]$.)

**Orden 1** = modelo de Lorentz lineal. Estado estacionario:
$$\tilde x^{(1)}(t)=x^{(1)}(\omega_1)e^{-i\omega_1t}+x^{(1)}(\omega_2)e^{-i\omega_2t}+\text{c.c.} \qquad (1.4.8)$$
$$x^{(1)}(\omega_j)=-\frac{e}{m}\frac{E_j}{D(\omega_j)} \qquad (1.4.9)$$
$$D(\omega_j)=\omega_0^2-\omega_j^2-2i\omega_j\gamma \qquad (1.4.10)$$
(Paso: sustituir $x e^{-i\omega_jt}$: $(-\omega_j^2-2i\gamma\omega_j+\omega_0^2)x=-eE_j/m$.)

**Orden 2.** $[\tilde x^{(1)}]^2$ contiene $\pm2\omega_1,\pm2\omega_2,\pm(\omega_1+\omega_2),\pm(\omega_1-\omega_2)$ y 0. Para $2\omega_1$:
$$\ddot{\tilde x}^{(2)}+2\gamma\dot{\tilde x}^{(2)}+\omega_0^2\tilde x^{(2)}=\frac{-a(eE_1/m)^2e^{-2i\omega_1t}}{D^2(\omega_1)} \qquad (1.4.11)$$
$$\tilde x^{(2)}(t)=x^{(2)}(2\omega_1)e^{-2i\omega_1t} \qquad (1.4.12)$$
$$x^{(2)}(2\omega_1)=\frac{-a(e/m)^2E_1^2}{D(2\omega_1)D^2(\omega_1)} \qquad (1.4.13),\ \text{p. 24}$$
(Paso: el término de $[\tilde x^{(1)}]^2$ en $e^{-2i\omega_1t}$ es $[x^{(1)}(\omega_1)]^2=(e/m)^2E_1^2/D^2(\omega_1)$; al sustituir (1.4.12) el
operador da $D(2\omega_1)x^{(2)}(2\omega_1)$.)
Análogamente (p. 25):
$$x^{(2)}(2\omega_2)=\frac{-a(e/m)^2E_2^2}{D(2\omega_2)D^2(\omega_2)} \qquad (1.4.14\text{a})$$
$$x^{(2)}(\omega_1+\omega_2)=\frac{-2a(e/m)^2E_1E_2}{D(\omega_1+\omega_2)D(\omega_1)D(\omega_2)} \qquad (1.4.14\text{b})$$
$$x^{(2)}(\omega_1-\omega_2)=\frac{-2a(e/m)^2E_1E_2^*}{D(\omega_1-\omega_2)D(\omega_1)D(-\omega_2)} \qquad (1.4.14\text{c})$$
$$x^{(2)}(0)=\frac{-2a(e/m)^2E_1E_1^*}{D(0)D(\omega_1)D(-\omega_1)}+\frac{-2a(e/m)^2E_2E_2^*}{D(0)D(\omega_2)D(-\omega_2)} \qquad (1.4.14\text{d})$$
(El 2 en (b)–(d) es el término cruzado de $[\tilde x^{(1)}]^2$; nótese $D(-\omega)=D(\omega)^*$ y $x^{(1)}(-\omega)=x^{(1)}(\omega)^*$.)

**Susceptibilidad lineal.** Definición y polarización ($N$ = densidad de átomos):
$$P^{(1)}(\omega_j)=\epsilon_0\chi^{(1)}(\omega_j)E(\omega_j) \qquad (1.4.15);\qquad P^{(1)}(\omega_j)=-Nex^{(1)}(\omega_j) \qquad (1.4.16)$$
$$\boxed{\chi^{(1)}(\omega_j)=\frac{N(e^2/m)}{\epsilon_0D(\omega_j)}} \qquad (1.4.17),\ \text{p. 25}$$

**SHG**:
$$P^{(2)}(2\omega_1)=\epsilon_0\chi^{(2)}(2\omega_1,\omega_1,\omega_1)E(\omega_1)^2 \qquad (1.4.18);\qquad P^{(2)}(2\omega_1)=-Nex^{(2)}(2\omega_1) \qquad (1.4.19)$$
[en el escaneo (1.4.19) se lee $x^{(2)}(2\omega_i)$; es $2\omega_1$.] Comparando con (1.4.13):
$$\chi^{(2)}(2\omega_1,\omega_1,\omega_1)=\frac{N(e^3/m^2)a}{\epsilon_0D(2\omega_1)D^2(\omega_1)} \qquad (1.4.20)$$
$$\boxed{\chi^{(2)}(2\omega_1,\omega_1,\omega_1)=\frac{\epsilon_0^2ma}{N^2e^3}\chi^{(1)}(2\omega_1)\left[\chi^{(1)}(\omega_1)\right]^2} \qquad (1.4.21),\ \text{p. 26}$$
(Paso: $1/D(\omega)=\epsilon_0m\chi^{(1)}(\omega)/(Ne^2)$; tres factores dan $(\epsilon_0m)^3/(N^3e^6)$, multiplicado por $Ne^3a/(\epsilon_0m^2)$ da
$\epsilon_0^2ma/(N^2e^3)$.) Para $\omega_2$: sustituir $\omega_1\to\omega_2$.

**SFG** (el 2 aparece en la definición porque los campos son distintos, ver (1.3.19)):
$$P^{(2)}(\omega_1+\omega_2)=2\epsilon_0\chi^{(2)}(\omega_1+\omega_2,\omega_1,\omega_2)E(\omega_1)E(\omega_2) \qquad (1.4.22);\qquad P^{(2)}(\omega_1+\omega_2)=-Nex^{(2)}(\omega_1+\omega_2) \qquad (1.4.23)$$
$$\chi^{(2)}(\omega_1+\omega_2,\omega_1,\omega_2)=\frac{N(e^3/m^2)a}{\epsilon_0D(\omega_1+\omega_2)D(\omega_1)D(\omega_2)} \qquad (1.4.24)$$
$$\chi^{(2)}(\omega_1+\omega_2,\omega_1,\omega_2)=\frac{\epsilon_0^2ma}{N^2e^3}\chi^{(1)}(\omega_1+\omega_2)\chi^{(1)}(\omega_1)\chi^{(1)}(\omega_2) \qquad (1.4.25)$$
Cuando $\omega_2\to\omega_1$, (1.4.24) → (1.4.20) (consistente con la convención de §1.3).

**DFG**:
$$\chi^{(2)}(\omega_1-\omega_2,\omega_1,-\omega_2)=\frac{N(e^3/\epsilon_0m^2)a}{D(\omega_1-\omega_2)D(\omega_1)D(-\omega_2)}=\frac{\epsilon_0^2ma}{N^2e^3}\chi^{(1)}(\omega_1-\omega_2)\chi^{(1)}(\omega_1)\chi^{(1)}(-\omega_2) \qquad (1.4.26)$$
**OR** (p. 27):
$$\chi^{(2)}(0,\omega_1,-\omega_1)=\frac{N(e^3/m^2)a}{\epsilon_0D(0)D(\omega_1)D(-\omega_1)}=\frac{\epsilon_0^2ma}{N^2e^3}\chi^{(1)}(0)\chi^{(1)}(\omega_1)\chi^{(1)}(-\omega_1) \qquad (1.4.27)$$
La mínima contribución no lineal en un medio no centrosimétrico es de 2.º orden; (1.4.7c) da $\chi^{(3)}$ y, en
general, el término $\lambda^n$ da $\chi^{(n)}$.

**Estructura general a recordar:** $\chi^{(2)}\propto a\times$ (producto de tres factores resonantes $1/D$), uno por
cada frecuencia (las dos de entrada y la generada); $\chi^{(2)}$ resuena si cualquiera de las frecuencias,
incluida la de salida, se acerca a $\omega_0$.

#### 1.4.2 Miller's Rule (p. 27)

Regla empírica de Miller (Miller, 1964; Garrett y Robinson, 1966): la cantidad
$$\frac{\chi^{(2)}(\omega_1+\omega_2,\omega_1,\omega_2)}{\chi^{(1)}(\omega_1+\omega_2)\chi^{(1)}(\omega_1)\chi^{(1)}(\omega_2)} \qquad (1.4.28)$$
es **casi constante para todos los cristales no centrosimétricos**. Por (1.4.25) eso ocurre si
$$\frac{ma\epsilon_0^2}{N^2e^3} \qquad (1.4.29)$$
es casi constante: $N$ es casi igual ($\sim10^{22}$ cm⁻³) para toda la materia condensada y $m$, $e$ son constantes
fundamentales. Estimación de $a$: las contribuciones lineal y no lineal a la fuerza restauradora (1.4.2) se
igualan cuando el desplazamiento es del orden del tamaño atómico ≈ constante de red $d$: $m\omega_0^2d=mad^2$ ⇒
$$a=\frac{\omega_0^2}{d} \qquad (1.4.30),\ \text{p. 27}$$
$\omega_0$ y $d$ son parecidos en la mayoría de sólidos ⇒ $a$ también (donde no se anula por simetría).

*Sobre "δ de Miller":* el texto de esta edición **no da un valor numérico** del cociente (1.4.28) (el llamado
"delta de Miller", $\delta$ o $\Delta$). En la literatura se define habitualmente con $d$ en lugar de $\chi^{(2)}$:
$d_{ijk}(\omega_3)=\epsilon_0\,\Delta_{ijk}\,\chi^{(1)}_{ii}(\omega_3)\chi^{(1)}_{jj}(\omega_1)\chi^{(1)}_{kk}(\omega_2)$ y para muchos cristales $\Delta$ varía
poco (aprox. un factor ~2–3 alrededor de $\sim$0.2–0.5 m²/C en SI; en gaussianas $\sim2\text{–}3\times10^{-6}$ esu).
[Estos valores NO están en el Boyd; son de la literatura general (Miller 1964; Yariv) y deben
verificarse antes de usarlos en el examen. Lo que sí da el Boyd es (1.4.28)–(1.4.32).]

**Estimación de $\chi^{(2)}$ no resonante** (p. 28): en (1.4.24) $D(\omega)\to\omega_0^2$, $N=1/d^3$, $a=\omega_0^2/d$:
$$\chi^{(2)}=\frac{e^3}{\epsilon_0m^2\omega_0^4d^4} \qquad (1.4.31)$$
(Paso: $\dfrac{N e^3a}{\epsilon_0m^2\omega_0^6}=\dfrac{e^3}{\epsilon_0m^2d^3}\dfrac{\omega_0^2}{d}\dfrac{1}{\omega_0^6}$.) Con $\omega_0=1\times10^{16}$ rad/s, $d=3$ Å, $e=1.6\times10^{-19}$ C,
$m=9.1\times10^{-31}$ kg:
$$\chi^{(2)}\simeq6.9\times10^{-12}\ \text{m/V} \qquad (1.4.32)$$
en buen acuerdo con la Tabla 1.5.3 (p. 50). (Verificado numéricamente: $6.9\times10^{-12}$ m/V.)

#### 1.4.3 Centrosymmetric Media (p. 28)

Fuerza restauradora
$$\tilde F_{\rm restoring}=-m\omega_0^2\tilde x+mb\tilde x^3 \qquad (1.4.33)$$
$$U(\tilde x)=-\int\tilde F_{\rm restoring}\,d\tilde x=\tfrac12m\omega_0^2\tilde x^2-\tfrac14mb\tilde x^4 \qquad (1.4.34)$$
Fig. 1.4.2 (p. 29; $b>0$, caso usual): potencial simétrico ante $\tilde x\to-\tilde x$, más blando que la parábola a
grandes desplazamientos. $-mb\tilde x^4/4$ es la corrección de menor orden a la parábola; se supone que $\tilde x$
nunca es tan grande como para requerir términos de orden superior. La respuesta no lineal mínima es de 3.er
orden ($\chi^{(3)}$). Caso importante: material **isótropo** (además de centrosimétrico), p. ej. vidrios y líquidos:
$$\tilde{\mathbf F}_{\rm restoring}=-m\omega_0^2\tilde{\mathbf r}+mb(\tilde{\mathbf r}\cdot\tilde{\mathbf r})\tilde{\mathbf r} \qquad (1.4.35)$$
(única forma cúbica en $\tilde{\mathbf r}$ dirigida según $\tilde{\mathbf r}$, la única dirección posible en un medio isótropo).
Ecuación de movimiento:
$$\ddot{\tilde{\mathbf r}}+2\gamma\dot{\tilde{\mathbf r}}+\omega_0^2\tilde{\mathbf r}-b(\tilde{\mathbf r}\cdot\tilde{\mathbf r})\tilde{\mathbf r}=-e\tilde{\mathbf E}(t)/m \qquad (1.4.36)$$
$$\tilde{\mathbf E}(t)=\mathbf E_1e^{-i\omega_1t}+\mathbf E_2e^{-i\omega_2t}+\mathbf E_3e^{-i\omega_3t}+\text{c.c.} \qquad (1.4.37)$$
(tres frecuencias: el caso más general de 3.er orden), escrito como
$$\tilde{\mathbf E}(t)=\sum_n\mathbf E(\omega_n)e^{-i\omega_nt} \qquad (1.4.38)$$
Perturbación $\tilde{\mathbf E}\to\lambda\tilde{\mathbf E}$:
$$\tilde{\mathbf r}(t)=\lambda\tilde{\mathbf r}^{(1)}(t)+\lambda^2\tilde{\mathbf r}^{(2)}(t)+\lambda^3\tilde{\mathbf r}^{(3)}(t)+\cdots \qquad (1.4.39),\ \text{p. 30}$$
$$\ddot{\tilde{\mathbf r}}^{(1)}+2\gamma\dot{\tilde{\mathbf r}}^{(1)}+\omega_0^2\tilde{\mathbf r}^{(1)}=-e\tilde{\mathbf E}(t)/m \qquad (1.4.40\text{a})$$
$$\ddot{\tilde{\mathbf r}}^{(2)}+2\gamma\dot{\tilde{\mathbf r}}^{(2)}+\omega_0^2\tilde{\mathbf r}^{(2)}=0 \qquad (1.4.40\text{b})$$
$$\ddot{\tilde{\mathbf r}}^{(3)}+2\gamma\dot{\tilde{\mathbf r}}^{(3)}+\omega_0^2\tilde{\mathbf r}^{(3)}-b(\tilde{\mathbf r}^{(1)}\cdot\tilde{\mathbf r}^{(1)})\tilde{\mathbf r}^{(1)}=0 \qquad (1.4.40\text{c})$$
Orden 1:
$$\tilde{\mathbf r}^{(1)}(t)=\sum_n\mathbf r^{(1)}(\omega_n)e^{-i\omega_nt} \qquad (1.4.41\text{a});\qquad \mathbf r^{(1)}(\omega_n)=\frac{-e\mathbf E(\omega_n)/m}{D(\omega_n)} \qquad (1.4.41\text{b})$$
con $D(\omega_n)=\omega_0^2-\omega_n^2-2i\omega_n\gamma$.
$$\mathbf P^{(1)}(\omega_n)=-Ne\mathbf r^{(1)}(\omega_n) \qquad (1.4.42);\qquad P_i^{(1)}(\omega_n)=\epsilon_0\sum_j\chi^{(1)}_{ij}(\omega_n)E_j(\omega_n) \qquad (1.4.43\text{a})$$
$$\chi^{(1)}_{ij}(\omega_n)=\chi^{(1)}(\omega_n)\delta_{ij} \qquad (1.4.43\text{b});\qquad \chi^{(1)}(\omega_n)=\frac{Ne^2/m}{\epsilon_0D(\omega_n)} \qquad (1.4.43\text{c})$$
Orden 2: (1.4.40b) es amortiguada y no forzada ⇒ en estado estacionario
$$\tilde{\mathbf r}^{(2)}=0 \qquad (1.4.44)$$
(**no hay respuesta de 2.º orden en un medio centrosimétrico**).

Orden 3 (p. 31): sustituyendo (1.4.41a) en (1.4.40c):
$$\ddot{\tilde{\mathbf r}}^{(3)}+2\gamma\dot{\tilde{\mathbf r}}^{(3)}+\omega_0^2\tilde{\mathbf r}^{(3)}=-\sum_{mnp}\frac{be^3[\mathbf E(\omega_m)\cdot\mathbf E(\omega_n)]\mathbf E(\omega_p)}{m^3D(\omega_m)D(\omega_n)D(\omega_p)}e^{-i(\omega_m+\omega_n+\omega_p)t} \qquad (1.4.45)$$
(Paso: $(\mathbf r^{(1)}\cdot\mathbf r^{(1)})\mathbf r^{(1)}$ con $\mathbf r^{(1)}\propto-e/m$ da $(-e/m)^3=-e^3/m^3$.) Con $\omega_q=\omega_m+\omega_n+\omega_p$:
$$\tilde{\mathbf r}^{(3)}(t)=\sum_q\mathbf r^{(3)}(\omega_q)e^{-i\omega_qt} \qquad (1.4.46)$$
$$(-\omega_q^2-i\omega_q2\gamma+\omega_0^2)\mathbf r^{(3)}(\omega_q)=-\sum_{(mnp)}\frac{be^3[\mathbf E(\omega_m)\cdot\mathbf E(\omega_n)]\mathbf E(\omega_p)}{m^3D(\omega_m)D(\omega_n)D(\omega_p)} \qquad (1.4.47)$$
(suma restringida a $\omega_m+\omega_n+\omega_p=\omega_q$); el coeficiente de la izquierda es $D(\omega_q)$:
$$\mathbf r^{(3)}(\omega_q)=-\sum_{(mnp)}\frac{be^3[\mathbf E(\omega_m)\cdot\mathbf E(\omega_n)]\mathbf E(\omega_p)}{m^3D(\omega_q)D(\omega_m)D(\omega_n)D(\omega_p)} \qquad (1.4.48)$$
$$\mathbf P^{(3)}(\omega_q)=-Ne\mathbf r^{(3)}(\omega_q) \qquad (1.4.49)$$
Definición (1.3.20):
$$P_i^{(3)}(\omega_q)=\epsilon_0\sum_{jkl}\sum_{(mnp)}\chi^{(3)}_{ijkl}(\omega_q,\omega_m,\omega_n,\omega_p)E_j(\omega_m)E_k(\omega_n)E_l(\omega_p) \qquad (1.4.50)$$
Como $[\mathbf E_m\cdot\mathbf E_n]E_{p,i}=\sum_{jkl}\delta_{jk}\delta_{il}E_{m,j}E_{n,k}E_{p,l}$, una elección obvia es (p. 32)
$$\chi^{(3)}_{ijkl}(\omega_q,\omega_m,\omega_n,\omega_p)=\frac{Nbe^4\delta_{jk}\delta_{il}}{\epsilon_0m^3D(\omega_q)D(\omega_m)D(\omega_n)D(\omega_p)} \qquad (1.4.51)$$
Correcta pero no muestra la **simetría de permutación intrínseca** (arbitrariedad de cuál campo es $E_j(\omega_m)$,
$E_k(\omega_n)$, $E_l(\omega_p)$). Convención: definir $\chi^{(3)}$ como 1/6 de la suma de las seis expresiones con los
campos en todos los órdenes; solo aparecen tres contribuciones distintas:
$$\boxed{\chi^{(3)}_{ijkl}(\omega_q,\omega_m,\omega_n,\omega_p)=\frac{Nbe^4[\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}]}{3\epsilon_0m^3D(\omega_q)D(\omega_m)D(\omega_n)D(\omega_p)}} \qquad (1.4.52),\ \text{p. 32}$$
En términos de susceptibilidades lineales (usando (1.4.43c)):
$$\chi^{(3)}_{ijkl}(\omega_q,\omega_m,\omega_n,\omega_p)=\frac{bm\epsilon_0^3}{3N^3e^4}\left[\chi^{(1)}(\omega_q)\chi^{(1)}(\omega_m)\chi^{(1)}(\omega_n)\chi^{(1)}(\omega_p)\right][\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}] \qquad (1.4.53)$$
(Análogo de la regla de Miller para $\chi^{(3)}$.) Estimación de $b$: lineal y no lineal comparables cuando
$\tilde x\sim d$: $m\omega_0^2d=mbd^3$ ⇒
$$b=\frac{\omega_0^2}{d^2} \qquad (1.4.54)$$
No resonante, $D(\omega)\approx\omega_0^2$; de (1.4.52) (p. 33), con $N=1/d^3$:
$$\chi^{(3)}\simeq\frac{Nbe^4}{\epsilon_0m^3\omega_0^8}=\frac{e^4}{\epsilon_0m^3\omega_0^6d^5} \qquad (1.4.55)$$
Con $d=3$ Å y $\omega_0=7\times10^{15}$ rad/s:
$$\chi^{(3)}\simeq344\ \text{pm}^2/\text{V}^2=3.44\times10^{-22}\ \text{m}^2/\text{V}^2 \qquad (1.4.56)$$
típico de muchos materiales (cap. 4). (Verificado numéricamente. Nótese que en (1.4.55) se omitió el factor
$3/3=1$ que resulta de la suma de deltas para, p. ej., $\chi_{1111}$: $[\,1+1+1\,]/3=1$.)

### 1.5 Properties of the Nonlinear Susceptibility (p. 33)

Motivación: tres ondas $\omega_1,\omega_2,\omega_3=\omega_1+\omega_2$ en un medio de 2.º orden sin pérdidas (Fig. 1.5.1). Con
$$P_i(\omega_n+\omega_m)=\epsilon_0\sum_{jk}\sum_{(nm)}\chi^{(2)}_{ijk}(\omega_n+\omega_m,\omega_n,\omega_m)E_j(\omega_n)E_k(\omega_m) \qquad (1.5.1),\ \text{p. 33}$$
hacen falta seis tensores $\chi^{(2)}_{ijk}(\omega_1,\omega_3,-\omega_2)$, $\chi^{(2)}_{ijk}(\omega_1,-\omega_2,\omega_3)$, $\chi^{(2)}_{ijk}(\omega_2,\omega_3,-\omega_1)$, $\chi^{(2)}_{ijk}(\omega_2,-\omega_1,\omega_3)$,
$\chi^{(2)}_{ijk}(\omega_3,\omega_1,\omega_2)$, $\chi^{(2)}_{ijk}(\omega_3,\omega_2,\omega_1)$ y otros seis con frecuencias negativas: 12 tensores × 27 componentes =
**324 números complejos**. Las simetrías reducen mucho ese número (p. 34). Lo que sigue es para $\chi^{(2)}$ pero
se extiende a $\chi^{(3)}$ y superiores.

#### 1.5.1 Reality of the Fields (p. 34)

$$\tilde P_i(\mathbf r,t)=P_i(\omega_n+\omega_m)e^{-i(\omega_n+\omega_m)t}+P_i(-\omega_n-\omega_m)e^{i(\omega_n+\omega_m)t} \qquad (1.5.2)$$
$\tilde P$ es medible ⇒ real ⇒
$$P_i(-\omega_n-\omega_m)=P_i(\omega_n+\omega_m)^* \qquad (1.5.3)$$
$$E_j(-\omega_n)=E_j(\omega_n)^* \qquad (1.5.4\text{a});\qquad E_k(-\omega_m)=E_k(\omega_m)^* \qquad (1.5.4\text{b})$$
y por (1.5.1):
$$\boxed{\chi^{(2)}_{ijk}(-\omega_n-\omega_m,-\omega_n,-\omega_m)=\chi^{(2)}_{ijk}(\omega_n+\omega_m,\omega_n,\omega_m)^*} \qquad (1.5.5),\ \text{p. 34}$$

#### 1.5.2 Intrinsic Permutation Symmetry (p. 34)

En (1.5.1) $j,k,n,m$ son mudos: el término $\chi^{(2)}_{ijk}(\omega_n+\omega_m,\omega_n,\omega_m)E_j(\omega_n)E_k(\omega_m)$ también puede escribirse
$\chi^{(2)}_{ikj}(\omega_n+\omega_m,\omega_m,\omega_n)E_k(\omega_m)E_j(\omega_n)$. Son iguales si se exige que $\chi$ no cambie al intercambiar
simultáneamente los dos últimos argumentos de frecuencia y los dos últimos índices cartesianos:
$$\boxed{\chi^{(2)}_{ijk}(\omega_n+\omega_m,\omega_n,\omega_m)=\chi^{(2)}_{ikj}(\omega_n+\omega_m,\omega_m,\omega_n)} \qquad (1.5.6),\ \text{p. 35}$$
Físicamente: no importa cuál campo es el "primero" en $E_j(\omega_n)E_k(\omega_m)$. Es **pura convención** (podría
anularse un miembro del par y duplicar el otro sin cambiar $P$). Se deduce también desde la función respuesta no
lineal (Butcher, 1965; Flytzanis, 1975). Vale siempre (con o sin pérdidas).

#### 1.5.3 Symmetries for Lossless Media (p. 35)

Dos simetrías adicionales **solo para medios sin pérdidas**:

1. **$\chi^{(2)}$ real**: todas las componentes $\chi^{(2)}_{ijk}(\omega_n+\omega_m,\omega_n,\omega_m)$ son reales. Se cumple en el oscilador anarmónico
   si todas las frecuencias (y sumas/diferencias) están lejos de la resonancia (entonces $D$ real); prueba general
   con la expresión cuántica del cap. 3.
2. **Simetría de permutación total (full permutation symmetry)**: todos los argumentos de frecuencia se pueden
   intercambiar libremente si se intercambian a la vez los índices cartesianos correspondientes; al intercambiar el
   primero con uno de los dos últimos, hay que invertir signos (el primero es siempre la suma de los otros dos). Ej.:
$$\chi^{(2)}_{ijk}(\omega_3=\omega_1+\omega_2)=\chi^{(2)}_{jki}(-\omega_1=\omega_2-\omega_3) \qquad (1.5.7)$$
   Por (1.5.5) el lado derecho es $\chi^{(2)}_{jki}(\omega_1=-\omega_2+\omega_3)^*$ y, por realidad, $=\chi^{(2)}_{jki}(\omega_1=-\omega_2+\omega_3)$ (p. 36):
$$\chi^{(2)}_{ijk}(\omega_3=\omega_1+\omega_2)=\chi^{(2)}_{jki}(\omega_1=-\omega_2+\omega_3) \qquad (1.5.8)$$
$$\chi^{(2)}_{ijk}(\omega_3=\omega_1+\omega_2)=\chi^{(2)}_{kij}(\omega_2=\omega_3-\omega_1) \qquad (1.5.9)$$
   Prueba general: la expresión cuántica (cap. 3) la cumple cuando todas las frecuencias están desintonizadas
   muchos anchos de línea de las resonancias. También se deduce de la densidad de energía (siguiente).

#### 1.5.4 Field Energy Density for a Nonlinear Medium (p. 36)

Medio lineal, campo
$$\tilde E_i(t)=\sum_nE_i(\omega_n)e^{-i\omega_nt} \qquad (1.5.10)$$
Por Poynting (⟨ ⟩ = promedio temporal):
$$U=\tfrac12\langle\tilde{\mathbf D}\cdot\tilde{\mathbf E}\rangle=\tfrac12\sum_i\langle\tilde D_i\tilde E_i\rangle \qquad (1.5.11)$$
$$\tilde D_i(t)=\epsilon_0\sum_j\epsilon_{ij}\tilde E_j(t)=\epsilon_0\sum_j\sum_n\epsilon_{ij}(\omega_n)E_j(\omega_n)e^{-i\omega_nt} \qquad (1.5.12)$$
$$\epsilon_{ij}(\omega_n)=\delta_{ij}+\chi^{(1)}_{ij}(\omega_n) \qquad (1.5.13)$$
$$U=\frac{\epsilon_0}{2}\sum_i\sum_nE_i^*(\omega_n)E_i(\omega_n)+\frac{\epsilon_0}{2}\sum_{ij}\sum_nE_i^*(\omega_n)\chi^{(1)}_{ij}(\omega_n)E_j(\omega_n) \qquad (1.5.14),\ \text{p. 37}$$
(1.er término: energía del campo en vacío; 2.º: energía almacenada en la polarización.) Medio no lineal (Armstrong
*et al.*, 1962; Kleinman, 1962; Pershan, 1963), parte asociada a la polarización:
$$\begin{aligned}U={}&\frac{\epsilon_0}{2}\sum_{ij}\sum_n\chi^{(1)}_{ij}(\omega_n)E_i^*(\omega_n)E_j(\omega_n)
+\frac{\epsilon_0}{3}\sum_{ijk}\sum_{mn}\chi^{(2)\prime}_{ijk}(-\omega_n-\omega_m,\omega_m,\omega_n)E_i^*(\omega_m+\omega_n)E_j(\omega_m)E_k(\omega_n)\\
&+\frac{\epsilon_0}{4}\sum_{ijkl}\sum_{mno}\chi^{(3)\prime}_{ijkl}(-\omega_o-\omega_n-\omega_m,\omega_m,\omega_n,\omega_o)E_i^*(\omega_m+\omega_n+\omega_o)E_j(\omega_m)E_k(\omega_n)E_l(\omega_o)+\cdots\end{aligned} \qquad (1.5.15)$$
Las $\chi^{(n)\prime}$ son por ahora coeficientes de la serie de $U$; como el orden de los factores es irrelevante,
**tienen simetría de permutación total**. Con (Landau y Lifshitz, 1960; Pershan, 1963)
$$P_i(\omega_n)=\frac{\partial U}{\partial E_i^*(\omega_n)} \qquad (1.5.16)$$
se obtiene
$$P_i^{(1)}(\omega_m)=\epsilon_0\sum_j\chi^{(1)}_{ij}(\omega_m)E_j(\omega_m) \qquad (1.5.17\text{a})$$
$$P_i^{(2)}(\omega_m+\omega_n)=\epsilon_0\sum_{jk}\sum_{(mn)}\chi^{(2)\prime}_{ijk}(-\omega_m-\omega_n,\omega_m,\omega_n)E_j(\omega_m)E_k(\omega_n) \qquad (1.5.17\text{b}),\ \text{p. 38}$$
$$P_i^{(3)}(\omega_m+\omega_n+\omega_o)=\epsilon_0\sum_{jkl}\sum_{(mno)}\chi^{(3)\prime}_{ijkl}(-\omega_m-\omega_n-\omega_o,\omega_m,\omega_n,\omega_o)E_j(\omega_m)E_k(\omega_n)E_l(\omega_o) \qquad (1.5.17\text{c})$$
(nota al pie: los prefactores ½, ⅓, ¼ desaparecen porque al derivar aparecen 2, 3, 4 términos equivalentes de las
sumas). Son idénticas a (1.3.12) y (1.3.20) (salvo la convención opuesta de signo del primer argumento) ⇒ como las
$\chi^{(n)\prime}$ tienen permutación total, **las $\chi^{(n)}$ también**. Válido solo sin pérdidas: solo entonces la energía
interna es función de estado.

#### 1.5.5 Kleinman's Symmetry (p. 38)

Si todas las $\omega_i\ll$ la resonancia más baja, $\chi$ es esencialmente independiente de la frecuencia (p. ej. (1.4.24)
cuando $\omega\ll\omega_0$) y la respuesta es instantánea:
$$\tilde P(t)=\epsilon_0\chi^{(2)}\tilde E^2(t) \qquad (1.5.18)$$
con $\chi^{(2)}$ constante. El medio es necesariamente sin pérdidas ⇒ vale la permutación total (1.5.7) (p. 39):
$$\chi^{(2)}_{ijk}(\omega_3=\omega_1+\omega_2)=\chi^{(2)}_{jki}(\omega_1=-\omega_2+\omega_3)=\chi^{(2)}_{kij}(\omega_2=\omega_3-\omega_1)=\chi^{(2)}_{ikj}(\omega_3=\omega_2+\omega_1)=\chi^{(2)}_{kji}(\omega_2=-\omega_1+\omega_3)=\chi^{(2)}_{jik}(\omega_1=\omega_3-\omega_2)$$
Como $\chi^{(2)}$ no depende de las frecuencias, se pueden **permutar los índices sin permutar las frecuencias**:
$$\boxed{\chi^{(2)}_{ijk}=\chi^{(2)}_{jki}=\chi^{(2)}_{kij}=\chi^{(2)}_{ikj}=\chi^{(2)}_{jik}=\chi^{(2)}_{kji}\quad(\omega_3=\omega_1+\omega_2)} \qquad (1.5.19),\ \text{p. 39}$$
**Condición de simetría de Kleinman**: válida siempre que pueda despreciarse la dispersión de la susceptibilidad.

#### 1.5.6 Contracted Notation (p. 39)

Se usa cuando vale Kleinman. Tensor
$$\boxed{d_{ijk}=\tfrac12\chi^{(2)}_{ijk}} \qquad (1.5.20)$$
(½ por convención histórica; se suprimen los argumentos de frecuencia).
$$P_i(\omega_n+\omega_m)=\epsilon_0\sum_{jk}\sum_{(nm)}2d_{ijk}E_j(\omega_n)E_k(\omega_m) \qquad (1.5.21)$$
Si $d_{ijk}$ es simétrico en sus dos últimos índices (vale con Kleinman, y **siempre para SHG** porque $\omega_n=\omega_m$),
matriz contraída $d_{il}$:
$$\begin{array}{c|cccccc} jk: & 11 & 22 & 33 & 23,32 & 31,13 & 12,21\\ \hline l: & 1 & 2 & 3 & 4 & 5 & 6\end{array} \qquad (1.5.22)$$
$$d_{il}=\begin{bmatrix} d_{11}&d_{12}&d_{13}&d_{14}&d_{15}&d_{16}\\ d_{21}&d_{22}&d_{23}&d_{24}&d_{25}&d_{26}\\ d_{31}&d_{32}&d_{33}&d_{34}&d_{35}&d_{36}\end{bmatrix} \qquad (1.5.23),\ \text{p. 40}$$
Imponiendo **explícitamente** Kleinman (índices de $d_{ijk}$ libremente permutables), p. ej.
$$d_{12}\equiv d_{122}=d_{212}\equiv d_{26} \qquad (1.5.24\text{a});\qquad d_{14}\equiv d_{123}=d_{213}\equiv d_{25} \qquad (1.5.24\text{b})$$
y sistemáticamente: **solo 10 elementos independientes**:
$$d_{il}=\begin{bmatrix} d_{11}&d_{12}&d_{13}&d_{14}&d_{15}&d_{16}\\ d_{16}&d_{22}&d_{23}&d_{24}&d_{14}&d_{12}\\ d_{15}&d_{24}&d_{33}&d_{23}&d_{13}&d_{14}\end{bmatrix} \qquad (1.5.25)$$
(Truco: $d_{il}=d_{ijk}$; por ejemplo $d_{21}=d_{211}=d_{112}=d_{16}$, $d_{31}=d_{311}=d_{113}=d_{15}$, $d_{32}=d_{322}=d_{223}=d_{24}$, $d_{34}=d_{323}=d_{233}=d_{23}$.)

**SHG en notación matricial**:
$$\begin{bmatrix}P_x(2\omega)\\P_y(2\omega)\\P_z(2\omega)\end{bmatrix}=2\epsilon_0\begin{bmatrix} d_{11}&\cdots&d_{16}\\ d_{21}&\cdots&d_{26}\\ d_{31}&\cdots&d_{36}\end{bmatrix}\begin{bmatrix}E_x(\omega)^2\\E_y(\omega)^2\\E_z(\omega)^2\\2E_y(\omega)E_z(\omega)\\2E_x(\omega)E_z(\omega)\\2E_x(\omega)E_y(\omega)\end{bmatrix} \qquad (1.5.26),\ \text{p. 40}$$
**SFG** ($\omega_3=\omega_1+\omega_2$), con Kleinman (p. 41):
$$\begin{bmatrix}P_x(\omega_3)\\P_y(\omega_3)\\P_z(\omega_3)\end{bmatrix}=4\epsilon_0\,[d_{il}]\begin{bmatrix}E_x(\omega_1)E_x(\omega_2)\\E_y(\omega_1)E_y(\omega_2)\\E_z(\omega_1)E_z(\omega_2)\\E_y(\omega_1)E_z(\omega_2)+E_z(\omega_1)E_y(\omega_2)\\E_x(\omega_1)E_z(\omega_2)+E_z(\omega_1)E_x(\omega_2)\\E_x(\omega_1)E_y(\omega_2)+E_y(\omega_1)E_x(\omega_2)\end{bmatrix} \qquad (1.5.27)$$
El 2 extra (4 en vez de 2) viene de la suma sobre $n,m$ en (1.5.21), como en (1.3.16).

#### 1.5.7 Effective Value of d ($d_{\rm eff}$) (p. 41)

Para geometría fija (direcciones de propagación y polarización fijas), relación escalar:
$$P(\omega_3)=4\epsilon_0d_{\rm eff}E(\omega_1)E(\omega_2) \qquad (1.5.28)$$
$$P(2\omega)=2\epsilon_0d_{\rm eff}E(\omega)^2 \qquad (1.5.29)$$
con $E(\omega)=|\mathbf E(\omega)|$, $P(\omega)=|\mathbf P(\omega)|$. $d_{\rm eff}$ se obtiene calculando $\mathbf P$ con (1.5.26) o (1.5.27) (y proyectando
sobre la polarización de la onda generada). Prescripción general por clase: Midwinter y Warner (1965); Tabla 3.1 de
Zernike y Midwinter (1973). Ejemplo: **cristal uniáxico negativo de clase 3m**:
$$d_{\rm eff}=d_{31}\sin\theta-d_{22}\cos\theta\sin3\phi \qquad (1.5.30\text{a})\quad\text{(tipo I: las dos ondas de menor frecuencia con igual polarización)}$$
$$d_{\rm eff}=d_{22}\cos^2\theta\cos3\phi \qquad (1.5.30\text{b})\quad\text{(tipo II: polarizaciones ortogonales)}$$
$\theta$: ángulo entre $\mathbf k$ y el eje óptico $z$; $\phi$: ángulo azimutal entre $\mathbf k$ y el plano cristalino $xz$ (p. 42).
(Ej. LiNbO₃, BBO son 3m. Para la clase 32 —cuarzo— y otras, el texto no da la fórmula; remite a Midwinter y
Warner. Fórmulas estándar de la literatura, **no del Boyd**, a verificar: clase 32 tipo I (uniáxico negativo)
$d_{\rm eff}=d_{11}\cos^2\theta\cos3\phi$, tipo II $d_{\rm eff}=d_{11}\cos\theta\sin3\phi$; clase $\bar42m$ (KDP) tipo I $d_{\rm eff}=-d_{36}\sin\theta\sin2\phi$, tipo II
$d_{\rm eff}=d_{36}\sin2\theta\cos2\phi$.)

#### 1.5.8 Spatial Symmetry of the Nonlinear Medium (p. 42)

La forma de los tensores está restringida por la simetría del medio. Ejemplo: si $x$ e $y$ son equivalentes (rotar 90°
alrededor de $z$ deja el cristal idéntico: $z$ es **eje cuádruple**), la respuesta es igual para campo según $x$ o $y$ ⇒
p. ej. $\chi^{(2)}_{zxx}=\chi^{(2)}_{zyy}$. Por teoría de grupos todos los cristales pertenecen a una de **32 clases cristalinas**
(grupos puntuales) (detalles: Buerger, 1963). Ej.: grupo 4 = solo eje cuádruple; grupo 3 = solo eje ternario; 3m = eje
ternario más un plano espejo [el texto dice "perpendicular to this axis"; en la notación estándar el plano espejo de
3m **contiene** al eje ternario —un plano perpendicular sería $\bar6$—; posible imprecisión del texto].

#### 1.5.9 Influence of Spatial Symmetry on the Linear Optical Properties (p. 42)

Para $\chi^{(1)}$ hay cinco casos (Tabla 1.5.1). Siete **sistemas cristalinos** según la red (la Tabla 1.5.2, p. 47, da la
correspondencia con los 32 grupos puntuales). Cúbico e isótropo: $\chi^{(1)}$ diagonal con elementos iguales ⇒ ópticamente
isótropos. Los demás son anisótropos ($\mathbf P$ no necesariamente ∥ $\mathbf E$) ⇒ birrefringencia. Tetragonal, trigonal y hexagonal:
**uniáxicos** (simetría rotacional alrededor de $z$); triclínico, monoclínico y ortorrómbico: **biáxicos**.

**Tabla 1.5.1** (p. 43). Forma de $\chi^{(1)}$ (elementos no nulos por índices cartesianos):

| Sistema | Forma de $\chi^{(1)}_{ij}$ |
|---|---|
| Triclínico | todos: $xx,xy,xz;\ yx,yy,yz;\ zx,zy,zz$ |
| Monoclínico | $xx,0,xz;\ 0,yy,0;\ zx,0,zz$ |
| Ortorrómbico | diagonal $xx,yy,zz$ |
| Tetragonal, trigonal, hexagonal | diagonal $xx,xx,zz$ |
| Cúbico, isótropo | diagonal $xx,xx,xx$ |

#### 1.5.10 Influence of Inversion Symmetry on the Second-Order Nonlinear Response (p. 44)

En un medio **centrosimétrico** $\chi^{(2)}\equiv0$. 11 de las 32 clases tienen inversión ⇒ quedan excluidas para procesos de
2.º orden. Demostración (caso SHG, respuesta instantánea):
$$\tilde P(t)=\epsilon_0\chi^{(2)}\tilde E^2(t) \qquad (1.5.31);\qquad \tilde E(t)=\mathcal E\cos\omega t \qquad (1.5.32)$$
Si cambia el signo de $\tilde E$, por simetría de inversión cambia el de $\tilde P$:
$$-\tilde P(t)=\epsilon_0\chi^{(2)}[-\tilde E(t)]^2 \qquad (1.5.33)\ \Rightarrow\ -\tilde P(t)=\epsilon_0\chi^{(2)}\tilde E^2(t) \qquad (1.5.34)$$
Comparando con (1.5.31), $\tilde P=-\tilde P$ ⇒ $\tilde P\equiv0$:
$$\chi^{(2)}=0 \qquad (1.5.35),\ \text{p. 44}$$
Interpretación intuitiva (pp. 44–46, Fig. 1.5.2): electrón en un pozo no parabólico ⇒ distorsión armónica. (a) campo
aplicado; (b) respuesta lineal sin distorsión; (c) medio no lineal **centrosimétrico** (potencial de la Fig. 1.4.2):
distorsión con **solo armónicos impares**, promedio temporal nulo; (d) **no centrosimétrico** (Fig. 1.4.1): armónicos
pares e impares, promedio temporal no nulo (responde distinto a campo "hacia arriba" que "hacia abajo"). (Nota al
pie: (a),(b) = $\sin\omega t$; (c) = $\sin\omega t-0.25\sin3\omega t$; (d) = $-0.2+\sin\omega t+0.2\cos2\omega t$.)

#### 1.5.11 Influence of Spatial Symmetry on the Second-Order Susceptibility (p. 46)

Cada simetría adicional restringe la forma de $\chi^{(2)}$. El cálculo para las 32 clases (Butcher, 1965) está en la
**Tabla 1.5.2**; en notación contraída se muestra gráficamente en la **Fig. 1.5.3** (de Zernike y Midwinter, 1973),
que también indica el efecto de Kleinman. Ejemplo: **clase 3m**:
$$d_{il}=\begin{bmatrix}0&0&0&0&d_{31}&-d_{22}\\-d_{22}&d_{22}&0&d_{31}&0&0\\d_{31}&d_{31}&d_{33}&0&0&0\end{bmatrix}\qquad\text{(p. 46)}$$
(con Kleinman $d_{15}=d_{31}$; sin Kleinman $d_{15}=d_{24}$ y $d_{31}=d_{32}$ independientes.) La Tabla 1.5.3 debe usarse
con cautela: hay dispersión en los valores publicados (dependencia con la longitud de onda e imprecisión de
medidas); análisis detallado de medidas en Shoji *et al.* (1997).

**Tabla 1.5.2** (p. 47). Elementos no nulos de $\chi^{(2)}_{ijk}$ para las 32 clases (índices cartesianos):

| Sistema | Clase | Elementos no nulos |
|---|---|---|
| Triclínico | $1=C_1$ | Todos independientes y no nulos |
| | $\bar1=S_2$ | Todos nulos |
| Monoclínico | $2=C_2$ | $xyz,xzy,xxy,xyx,yxx,yyy,yzz,yzx,yxz,zyz,zzy,zxy,zyx$ (eje binario ∥ $\hat y$) |
| | $m=C_{1h}$ | $xxx,xyy,xzz,xzx,xxz,yyz,yzy,yxy,yyx,zxx,zyy,zzz,zzx,zxz$ (plano espejo ⊥ $\hat y$) |
| | $2/m=C_{2h}$ | Todos nulos |
| Ortorrómbico | $222=D_2$ | $xyz,xzy,yzx,yxz,zxy,zyx$ |
| | $mm2=C_{2v}$ | $xzx,xxz,yyz,yzy,zxx,zyy,zzz$ |
| | $mmm=D_{2h}$ | Todos nulos |
| Tetragonal | $4=C_4$ | $xyz=-yxz,\ xzy=-yzx,\ xzx=yzy,\ xxz=yyz,\ zxx=zyy,\ zzz,\ zxy=-zyx$ |
| | $\bar4=S_4$ | $xyz=yxz,\ xzy=yzx,\ xzx=-yzy,\ xxz=-yyz,\ zxx=-zyy,\ zxy=zyx$ |
| | $422=D_4$ | $xyz=-yxz,\ xzy=-yzx,\ zxy=-zyx$ |
| | $4mm=C_{4v}$ | $xzx=yzy,\ xxz=yyz,\ zxx=zyy,\ zzz$ |
| | $\bar42m=D_{2d}$ | $xyz=yxz,\ xzy=yzx,\ zxy=zyx$ |
| | $4/m=C_{4h}$, $4/mmm=D_{4h}$ | Todos nulos |
| Cúbico | $432=O$ | $xyz=-xzy=yzx=-yxz=zxy=-zyx$ |
| | $\bar43m=T_d$ | $xyz=xzy=yzx=yxz=zxy=zyx$ |
| | $23=T$ | $xyz=yzx=zxy,\ xzy=yxz=zyx$ |
| | $m3=T_h$, $m3m=O_h$ | Todos nulos |
| Trigonal | $3=C_3$ | $xxx=-xyy=-yyz=-yxy$ [*], $xyz=-yxz,\ xzy=-yzx,\ xzx=yzy,\ xxz=yyz,\ yyy=-yxx=-xxy=-xyx,\ zxx=zyy,\ zzz,\ zxy=-zyx$ |
| | $32=D_3$ | $xxx=-xyy=-yyx=-yxy,\ xyz=-yxz,\ xzy=-yzx,\ zxy=-zyx$ |
| | $3m=C_{3v}$ | $xzx=yzy,\ xxz=yyz,\ zxx=zyy,\ zzz,\ yyy=-yxx=-xxy=-xyx$ (plano espejo ⊥ $\hat x$) |
| | $\bar3=S_6$, $\bar3m=D_{3d}$ | Todos nulos |
| Hexagonal | $6=C_6$ | $xyz=-yxz,\ xzy=-yzx,\ xzx=yzy,\ xxz=yyz,\ zxx=zyy,\ zzz,\ zxy=-zyx$ |
| | $\bar6=C_{3h}$ | $xxx=-xyy=-yxy=-yyx,\ yyy=-yxx=-xyx=-xxy$ |
| | $622=D_6$ | $xyz=-yxz,\ xzy=-yxz$ [**], $zxy=-zyx$ |
| | $6mm=C_{6v}$ | $xzx=yzy,\ xxz=yyz,\ zxx=zyy,\ zzz$ |
| | $\bar6m2=D_{3h}$ | $yyy=-yxx=-xxy=-xyx$ |
| | $6/m=C_{6h}$, $6/mmm=D_{6h}$ | Todos nulos |

[*] Se lee "$-yyz$" en la clase 3; por consistencia con la clase 32 debería ser $-yyx$. [**] Se lee "$xzy=-yxz$" en la
clase 622; por consistencia con 422 y 6 debería ser $xzy=-yzx$.

**Fig. 1.5.3** (pp. 48–49): forma de $d_{il}$ para las **21 clases sin inversión** (puntos pequeños = 0; grandes = no nulo;
cuadrado = coeficiente que se anula si vale Kleinman; símbolos unidos = numéricamente iguales; símbolo abierto = signo
opuesto al cerrado al que se une; uniones discontinuas = solo bajo Kleinman). Biaxiales: 1, 2, m, 222, mm2. Uniáxicas:
3, 3m, $\bar6$, $\bar6m2$, 6 y 4, 6mm y 4mm, 622 y 422, $\bar4$, 32, $\bar42m$. "Isótropas" (cúbicas): $\bar43m$ y 23 (solo
$d_{14}=d_{25}=d_{36}$), 432 (todos nulos bajo Kleinman; nótese que 432 no tiene inversión pero su $d$ se anula —los
elementos $xyz=-xzy$ son antisimétricos en los dos últimos índices y desaparecen para SHG/Kleinman). Ejemplos útiles
(leídos de la figura): 32 (cuarzo): $d_{11}$, $d_{12}=-d_{11}$, $d_{26}=-d_{11}$, $d_{14}$, $d_{25}=-d_{14}$ (con Kleinman $d_{14}=0$);
$\bar42m$ (KDP): $d_{14}$, $d_{25}=d_{14}$, $d_{36}$ (con Kleinman $d_{14}=d_{36}$); 4mm/6mm: $d_{15}=d_{24}$, $d_{31}=d_{32}$, $d_{33}$.

#### 1.5.12 Number of Independent Elements of $\chi^{(2)}_{ijk}(\omega_3,\omega_2,\omega_1)$ (p. 48)

Cuenta en cascada: 324 números complejos (general) → realidad de los campos (1.5.5): la mitad → permutación intrínseca
(1.5.6): **81** parámetros → sin pérdidas (reales + permutación total): **27** (p. 49) → SHG (notación contraída):
**18** → Kleinman: **10** → simetrías cristalinas: menos aún.

#### 1.5.13 Distinction between Noncentrosymmetric and Cubic Crystal Classes (p. 49)

Un material puede tener red cúbica y ser no centrosimétrico: **GaAs** (estructura de **zincblenda**, grupo $\bar43m$) tiene
$\chi^{(2)}\neq0$, de hecho inusualmente grande (Tabla 1.5.3: $d_{36}=370$ pm/V), pero al ser cúbico **no es birrefringente** y
no puede, normalmente, satisfacer el ajuste de fase por birrefringencia (cap. 2) (p. 50). Fig. 1.5.4 (p. 51): diamante
($m3m$, C) vs. zincblenda ($\bar43m$, Ga/Zn y As/S): misma red; el diamante tiene centro de inversión a mitad de camino
entre dos C vecinos; en la zincblenda los vecinos son de especies distintas y no hay inversión. (Por eso **Si**, con
estructura de diamante, tiene $\chi^{(2)}_{\rm bulk}=0$.)

**Tabla 1.5.3** (p. 50). Susceptibilidades de 2.º orden ($d_{il}$ en pm/V):

| Material | Grupo puntual | $d_{il}$ (pm/V) |
|---|---|---|
| Ag₃AsS₃ (proustita) | $3m=C_{3v}$ | $d_{22}=18$, $d_{15}=11$ |
| AgGaSe₂ | $\bar42m=D_{2d}$ | $d_{36}=33$ |
| AgSbS₃ (pirargirita) | $3m=C_{3v}$ | $d_{15}=8$, $d_{22}=9$ |
| β-BaB₂O₄ (BBO) | $3m=C_{3v}$ | $d_{22}=2.2$ |
| CdGeAs₂ | $\bar42m=D_{2d}$ | $d_{36}=235$ |
| CdS | $6mm=C_{6v}$ | $d_{33}=78$, $d_{31}=-40$ |
| GaAs | $\bar43m$ | $d_{36}=370$ |
| KH₂PO₄ (KDP) | "2m" [*] | $d_{36}=0.43$ |
| KD₂PO₄ (KD*P) | "2m" [*] | $d_{36}=0.42$ |
| LiIO₃ | $6=C_6$ | $d_{15}=-5.5$, $d_{31}=-7$ |
| LiNbO₃ | $3m=C_{3v}$ | "$d_{32}=-30$" [**], $d_{31}=-5.9$ |
| Cuarzo | $32=D_3$ | $d_{11}=0.3$, $d_{14}=0.008$ |

Notas de la tabla: valores de diversas fuentes (tabulaciones más completas: R. L. Sutherland, 1996; A. V. Smith;
hojas de datos de Cleveland Crystals). **Conversión a gaussianas**: multiplicar por $(3\times10^{-8})/4\pi=2.386\times10^{-9}$ para
obtener $d$ en esu (cm/statvolt). **En cualquier sistema de unidades, $\chi^{(2)}=2d$ por convención.**
[*] Se lee "2m"; KDP y KD*P son de clase $\bar42m$ (así lo exige además que el coeficiente listado sea $d_{36}$).
[**] Se lee "$d_{32}=-30$"; en la clase 3m $d_{32}=d_{31}$, así que debe ser $d_{33}=-30$ pm/V (el coeficiente grande del LiNbO₃).

#### 1.5.14 Distinction between Noncentrosymmetric and Polar Crystal Classes (p. 51)

De las 32 clases, **21 son no centrosimétricas** (pueden tener $\chi^{(2)}\neq0$). Más restrictivo: cristales con momento
dipolar permanente = **polares** (o ferroeléctricos; distinciones finas entre polar, piroeléctrico, piezoeléctrico y
ferroeléctrico en Nye, 1985, pp. 78–81). Consecuencias: efecto piroeléctrico (cambio del dipolo con la temperatura;
detectores, ver §13.3 de Boyd 1983) y efecto fotorrefractivo (cap. 11). Clases polares (p. 52):
$$1,\ 2,\ 3,\ 4,\ 6,\ m,\ mm2,\ 3m,\ 4mm,\ 6mm$$
Todas las polares son no centrosimétricas, pero no al revés: p. ej. la molécula tetraédrica CCl₄ no tiene dipolo
permanente y sin embargo no es centrosimétrica.

#### 1.5.15 Influence of Spatial Symmetry on the Third-Order Nonlinear Response (p. 52)

Forma permitida de $\chi^{(3)}$: Butcher (1965), resumida por Hellwarth (1977), con una corrección menor de Shang y Hsu
(1987): **Tabla 1.5.4**. Para el caso isótropo coincide con lo derivado en §4.2 (índice no lineal).

**Tabla 1.5.4** (pp. 53–55). Forma de $\chi^{(3)}_{ijkl}$:

- **Isótropo**: 21 elementos no nulos, solo **3 independientes**:
  $yyzz=zzyy=zzxx=xxzz=xxyy=yyxx$; $yzyz=zyzy=zxzx=xzxz=xyxy=yxyx$; $yzzy=zyyz=zxxz=xzzx=xyyx=yxxy$; y
  $$xxxx=yyyy=zzzz=xxyy+xyxy+xyyx.$$
- **Cúbico, clases 23 y m3**: 21 no nulos, **7 independientes**: $xxxx=yyyy=zzzz$; $yyzz=zzxx=xxyy$; $zzyy=xxzz=yyxx$;
  $yzyz=zxzx=xyxy$; $zyzy=xzxz=yxyx$; $yzzy=zxxz=xyyx$; $zyyz=xzzx=yxxy$.
- **Cúbico, clases 432, $\bar43m$, m3m**: 21 no nulos, **4 independientes**: $xxxx=yyyy=zzzz$;
  $yyzz=zzyy=zzxx=xxzz=xxyy=yyxx$; $yzyz=zyzy=zxzx=xzxz=xyxy=yxyx$; $yzzy=zyyz=zxxz=xzzx=xyyx=yxxy$.
  (A diferencia del isótropo, $xxxx$ es independiente: anisotropía de $\chi^{(3)}$ en Si y GaAs.)
- **Hexagonal 6, $\bar6$, 6/m**: 41 no nulos, 19 independientes: $zzzz$; $xxxx=yyyy=xxyy+xyyx+xyxy$ con $xxyy=yyxx$,
  $xyyx=yxxy$, $xyxy=yxyx$; $yyzz=xxzz$, $xyzz=-yxzz$; $zzyy=zzxx$, $zzxy=-zzyx$; $zyyz=zxxz$, $zxyz=-zyxz$; $yzzy=xzzx$,
  $xzzy=-yzzx$; $yzyz=xzxz$, $xzyz=-yzxz$; $zyzy=zxzx$, $zxzy=-zyzx$; $xxxy=-yyyx=yyxy+yxyy+xyyy$ con $yyxy=-xxyx$,
  $yxyy=-xyxx$, $xyyy=-yxxx$.
- **Hexagonal 622, 6mm, 6/mmm, $\bar6m2$**: 21 no nulos, 10 independientes: $zzzz$; $xxxx=yyyy=xxyy+xyyx+xyxy$ (con
  $xxyy=yyxx$, $xyyx=yxxy$, $xyxy=yxyx$); $yyzz=xxzz$; $zzyy=zzxx$; $zyyz=zxxz$; $yzzy=xzzx$; $yzyz=xzxz$; $zyzy=zxzx$.
- **Trigonal 3, $\bar3$**: 73 no nulos, 27 independientes: todos los del grupo hexagonal 6 (lista anterior) más
  $yyyz=-yxxz=-xyxz=-xxyz$; $yyzy=-yxzx=-xyzx=-xxzy$; $yzyy=-yzxx=-xzyx=-xzxy$; $zyyy=-zyxx=-zxyx=-zxxy$;
  $xxxz=-xyyz=-yxyz=-yyxz$; $xxzx=-xyzy=-yxzy=-yyzx$; $xzxx=-yzxy=-yzyx=-xzyy$; $zxxx=-zxyy=-zyxy=-zyyx$.
- **Trigonal 3m, $\bar3m$, 32**: 37 no nulos, 14 independientes: $zzzz$; $xxxx=yyyy=xxyy+xyyx+xyxy$ (con las tres
  igualdades); $yyzz=xxzz$; $zzyy=zzxx$; $zyyz=zxxz$; $yzzy=xzzx$; $xxxz=-xyyz=-yxyz=-yyxz$; $xxzx=-xyzy=-yxzy=-yyzx$;
  $xzxx=-xzyy=-yzxy=-yzyx$; $zxxx=-zxyy=-zyxy=-zyyx$; $yzyz=xzxz$; $zyzy=zxzx$.
- **Tetragonal 4, $\bar4$, 4/m**: 41 no nulos, 21 independientes: $xxxx=yyyy$, $zzzz$; $zzxx=zzyy$, "$xxzz=zzyy$" [se lee
  así; por consistencia debería ser $xxzz=yyzz$], $zxzx=zyzy$, $xzxz=yzyz$, $zxxz=zyyz$, $xzzx=yzzy$; $xyzz=-yxzz$,
  $zzxy=-zzyx$, $xzyz=-yzxz$, $zxzy=-zyzx$, $zxyz=-zyxz$, $xzzy=-yzzx$; $xxyy=yyxx$, $xyxy=yxyx$, $xyyx=yxxy$;
  $xxxy=-yyyx$, $xxyx=-yyxy$, $xyxx=-yxyy$, $yxxx=-xyyy$.
- **Tetragonal 422, 4mm, 4/mmm, $\bar42m$**: 21 no nulos, 11 independientes: $xxxx=yyyy$, $zzzz$; $yyzz=xxzz$, $zzyy=zzxx$,
  $zyyz=zxxz$; $yzzy=xzzx$, $yzyz=xzxz$, $zyzy=zxzx$; $xxyy=yyxx$, $xyxy=yxyx$, $xyyx=yxxy$.
- **Monoclínico 2, m, 2/m**: 41 elementos independientes no nulos: 3 con los cuatro índices iguales; 18 con índices
  iguales por pares; 12 con dos $y$, una $x$ y una $z$; 4 con tres $x$ y una $z$; 4 con tres $z$ y una $x$.
- **Ortorrómbico 222, mm2, mmm**: 21 independientes no nulos: 3 con índices todos iguales, 18 con índices iguales por pares.
- **Triclínico 1, $\bar1$**: 81 independientes no nulos.

(Nota: $\chi^{(3)}$ existe en las 32 clases, incluidas las centrosimétricas.)

### 1.6 Time-Domain Description of Optical Nonlinearities (p. 52)

Hasta aquí: respuesta en el dominio de la frecuencia a campos casi monocromáticos (suma discreta de componentes en
armónicos, sumas y diferencias). Alternativa equivalente: describir $\tilde P(t)$ producido por un campo arbitrario
$\tilde E(t)$; más cómoda para **pulsos cortos**; la de frecuencia, para campos casi monocromáticos (pp. 55–56).

**Respuesta lineal**:
$$\tilde P^{(1)}(t)=\epsilon_0\int_0^\infty R^{(1)}(\tau)\tilde E(t-\tau)\,d\tau \qquad (1.6.1),\ \text{p. 56}$$
$R^{(1)}(\tau)$: función respuesta lineal (contribución a $P$ en $t$ del campo aplicado en $t-\tau$). El límite inferior 0
expresa **causalidad**: $R^{(1)}(\tau)=0$ para $\tau<0$ ($\tilde P$ depende solo del pasado de $\tilde E$).
Transformada de Fourier (convención del libro):
$$E(\omega)=\int_{-\infty}^{\infty}\tilde E(t)e^{i\omega t}\,dt \qquad (1.6.2\text{a});\qquad \tilde E(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}E(\omega)e^{-i\omega t}\,d\omega \qquad (1.6.2\text{b})$$
Sustituyendo (1.6.2b) en (1.6.1):
$$\tilde P^{(1)}(t)=\epsilon_0\int_0^\infty d\tau\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}R^{(1)}(\tau)E(\omega)e^{-i\omega(t-\tau)}=\epsilon_0\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\left[\int_0^\infty d\tau\,R^{(1)}(\tau)e^{i\omega\tau}\right]E(\omega)e^{-i\omega t} \qquad (1.6.3)$$
$$\tilde P^{(1)}(t)=\epsilon_0\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\chi^{(1)}(\omega;\omega)E(\omega)e^{-i\omega t} \qquad (1.6.4)$$
$$\boxed{\chi^{(1)}(\omega;\omega)=\int_0^\infty d\tau\,R^{(1)}(\tau)e^{i\omega\tau}} \qquad (1.6.5)$$
Escribiendo el lado izquierdo como $\int P^{(1)}(\omega)e^{-i\omega t}d\omega/2\pi$ e igualando para cada $\omega$ (p. 57):
$$P^{(1)}(\omega)=\epsilon_0\chi^{(1)}(\omega;\omega)E(\omega) \qquad (1.6.6)$$

**Segundo orden**:
$$\tilde P^{(2)}(t)=\epsilon_0\int_0^\infty d\tau_1\int_0^\infty d\tau_2\,R^{(2)}(\tau_1,\tau_2)\tilde E(t-\tau_1)\tilde E(t-\tau_2) \qquad (1.6.7)$$
(causalidad: $R^{(2)}=0$ si $\tau_1$ o $\tau_2$ es negativo). Con (1.6.2b):
$$\tilde P^{(2)}(t)=\epsilon_0\int\frac{d\omega_1}{2\pi}\int\frac{d\omega_2}{2\pi}\int_0^\infty d\tau_1\int_0^\infty d\tau_2R^{(2)}(\tau_1,\tau_2)E(\omega_1)e^{-i\omega_1(t-\tau_1)}E(\omega_2)e^{-i\omega_2(t-\tau_2)}=\epsilon_0\int_{-\infty}^{\infty}\frac{d\omega_1}{2\pi}\int_{-\infty}^{\infty}\frac{d\omega_2}{2\pi}\chi^{(2)}(\omega_\sigma;\omega_1,\omega_2)E(\omega_1)E(\omega_2)e^{-i\omega_\sigma t} \qquad (1.6.8)$$
con $\omega_\sigma=\omega_1+\omega_2$ y
$$\chi^{(2)}(\omega_\sigma;\omega_1,\omega_2)=\int_0^\infty d\tau_1\int_0^\infty d\tau_2\,R^{(2)}(\tau_1,\tau_2)e^{i(\omega_1\tau_1+\omega_2\tau_2)} \qquad (1.6.9)$$
**Tercer orden**:
$$\tilde P^{(3)}(t)=\epsilon_0\int\frac{d\omega_1}{2\pi}\int\frac{d\omega_2}{2\pi}\int\frac{d\omega_3}{2\pi}\chi^{(3)}(\omega_\sigma;\omega_1,\omega_2,\omega_3)E(\omega_1)E(\omega_2)E(\omega_3)e^{-i\omega_\sigma t} \qquad (1.6.10)$$
$\omega_\sigma=\omega_1+\omega_2+\omega_3$ (p. 58),
$$\chi^{(3)}(\omega_\sigma;\omega_1,\omega_2,\omega_3)=\int_0^\infty d\tau_1\int_0^\infty d\tau_2\int_0^\infty d\tau_3\,R^{(3)}(\tau_1,\tau_2,\tau_3)e^{i(\omega_1\tau_1+\omega_2\tau_2+\omega_3\tau_3)} \qquad (1.6.11)$$
(Observación: en esta sección $E(\omega)$ es una transformada de Fourier —densidad espectral—, no la amplitud discreta
de §1.3; la respuesta instantánea corresponde a $R^{(n)}\propto\delta(\tau_1)\cdots\delta(\tau_n)$, que da $\chi^{(n)}$ constante.)

### 1.7 Kramers–Kronig Relations in Linear and Nonlinear Optics (p. 58)

KK relacionan partes real e imaginaria de cantidades dependientes de la frecuencia; permiten obtener $\mathrm{Re}\,\chi$ a
partir del espectro de absorción (más fácil de medir que $n(\omega)$). Siempre válidas en óptica lineal; solo para
algunos procesos no lineales.

#### 1.7.1 Kramers–Kronig Relations in Linear Optics (p. 58)

$$\chi^{(1)}(\omega)\equiv\chi^{(1)}(\omega;\omega)=\int_0^\infty R^{(1)}(\tau)e^{i\omega\tau}\,d\tau \qquad (1.7.1)$$
(límite 0 por causalidad). $R^{(1)}(\tau)$ es **real** (relaciona dos cantidades reales $\tilde P$, $\tilde E$) ⇒
$$\chi^{(1)}(-\omega)=\chi^{(1)}(\omega)^* \qquad (1.7.2)$$
Tratando $\omega=\mathrm{Re}\,\omega+i\,\mathrm{Im}\,\omega$ como complejo: $\chi(\omega)$ es **analítica** (univaluada, derivadas continuas) en el
semiplano superior, $\mathrm{Im}\,\omega\ge0$ (p. 59). Prueba: el integrando es $R^{(1)}(\tau)e^{i(\mathrm{Re}\,\omega)\tau}e^{-(\mathrm{Im}\,\omega)\tau}$; con $R^{(1)}$ finita,
el factor $e^{-(\mathrm{Im}\,\omega)\tau}$ asegura convergencia para $\mathrm{Im}\,\omega>0$; en el eje real converge porque $R^{(1)}$ es de cuadrado
integrable (o porque $\chi(\omega)$ real-ω es medible y finita).

Integral
$$\mathrm{Int}=\int_{-\infty}^{\infty}\frac{\chi^{(1)}(\omega')\,d\omega'}{\omega'-\omega} \qquad (1.7.3)$$
en **valor principal de Cauchy**:
$$\int_{-\infty}^{\infty}\frac{\chi^{(1)}(\omega')d\omega'}{\omega'-\omega}\equiv\lim_{\delta\to0}\left[\int_{-\infty}^{\omega-\delta}\frac{\chi^{(1)}(\omega')d\omega'}{\omega'-\omega}+\int_{\omega+\delta}^{\infty}\frac{\chi^{(1)}(\omega')d\omega'}{\omega'-\omega}\right] \qquad (1.7.4)$$
Integración de contorno (Fig. 1.7.1, p. 60: (a) plano $\omega'$ con polo P en $\omega'=\omega$ sobre el eje real; (b) camino deseado;
(c) camino A cerrado: eje real con semicírculo pequeño $r_2$ sobre el polo y semicírculo grande $r_1$; (d) camino B =
semicírculo grande; (e) camino C = semicírculo pequeño; límites $r_1\to\infty$, $r_2\to0$):
$\mathrm{Int}=\mathrm{Int}(A)-\mathrm{Int}(B)-\mathrm{Int}(C)$. $\mathrm{Int}(A)=0$ (Cauchy: no encierra polos, $\chi$ analítica arriba); $\mathrm{Int}(B)=0$ (el
integrando va como $\chi(\omega')/|\omega'|\to0$ si $\chi\to0$ para $\omega'$ grande); $\mathrm{Int}(C)=-\pi i\chi(\omega)$ (residuo, medio círculo recorrido
en sentido horario). Entonces $\mathrm{Int}=\pi i\chi(\omega)$:
$$\chi^{(1)}(\omega)=\frac{-i}{\pi}\int_{-\infty}^{\infty}\frac{\chi^{(1)}(\omega')\,d\omega'}{\omega'-\omega} \qquad (1.7.5)$$
Separando $\chi^{(1)}=\mathrm{Re}\,\chi^{(1)}+i\,\mathrm{Im}\,\chi^{(1)}$:
$$\mathrm{Re}\,\chi^{(1)}(\omega)=\frac1\pi\int_{-\infty}^{\infty}\frac{\mathrm{Im}\,\chi^{(1)}(\omega')\,d\omega'}{\omega'-\omega} \qquad (1.7.6\text{a})$$
$$\mathrm{Im}\,\chi^{(1)}(\omega)=-\frac1\pi\int_{-\infty}^{\infty}\frac{\mathrm{Re}\,\chi^{(1)}(\omega')\,d\omega'}{\omega'-\omega} \qquad (1.7.6\text{b})$$
Solo frecuencias positivas (p. 61): de (1.7.2),
$$\mathrm{Re}\,\chi^{(1)}(-\omega)=\mathrm{Re}\,\chi^{(1)}(\omega),\qquad \mathrm{Im}\,\chi^{(1)}(-\omega)=-\mathrm{Im}\,\chi^{(1)}(\omega) \qquad (1.7.7)$$
$$\mathrm{Im}\,\chi^{(1)}(\omega)=-\frac1\pi\int_{-\infty}^{0}\frac{\mathrm{Re}\,\chi^{(1)}(\omega')d\omega'}{\omega'-\omega}-\frac1\pi\int_0^\infty\frac{\mathrm{Re}\,\chi^{(1)}(\omega')d\omega'}{\omega'-\omega}=\frac1\pi\int_0^\infty\frac{\mathrm{Re}\,\chi^{(1)}(\omega')d\omega'}{\omega'+\omega}-\frac1\pi\int_0^\infty\frac{\mathrm{Re}\,\chi^{(1)}(\omega')d\omega'}{\omega'-\omega} \qquad (1.7.8)$$
[En el escaneo, el primer término de la 2.ª línea aparece con signo "+": $\frac1\pi\int_0^\infty\frac{\mathrm{Re}\chi d\omega'}{\omega'+\omega}$. Comprobación: con $\omega'\to-\omega'$,
$-\frac1\pi\int_{-\infty}^0\frac{\mathrm{Re}\chi(\omega')}{\omega'-\omega}d\omega'=-\frac1\pi\int_0^\infty\frac{\mathrm{Re}\chi(\omega')}{-\omega'-\omega}d\omega'=+\frac1\pi\int_0^\infty\frac{\mathrm{Re}\chi(\omega')}{\omega'+\omega}d\omega'$: correcto.] Combinando
$\frac{1}{\omega'+\omega}-\frac{1}{\omega'-\omega}=\frac{-2\omega}{\omega'^2-\omega^2}$:
$$\boxed{\mathrm{Im}\,\chi^{(1)}(\omega)=\frac{-2\omega}{\pi}\int_0^\infty\frac{\mathrm{Re}\,\chi^{(1)}(\omega')}{\omega'^2-\omega^2}\,d\omega'} \qquad (1.7.9\text{a})$$
$$\boxed{\mathrm{Re}\,\chi^{(1)}(\omega)=\frac{2}{\pi}\int_0^\infty\frac{\omega'\,\mathrm{Im}\,\chi^{(1)}(\omega')}{\omega'^2-\omega^2}\,d\omega'} \qquad (1.7.9\text{b})$$
(Para (1.7.9b), $\mathrm{Im}\chi$ impar: $\frac{1}{\omega'-\omega}+\frac{1}{\omega'+\omega}=\frac{2\omega'}{\omega'^2-\omega^2}$.)

#### 1.7.2 Kramers–Kronig Relations in Nonlinear Optics (p. 61)

Para $\chi^{(3)}(\omega_\sigma;\omega_1,\omega_2,\omega_3)$ con $\omega_\sigma=\omega_1+\omega_2+\omega_3$ y $\omega_1,\omega_2,\omega_3$ **positivas y distintas**, hay una relación KK en cada
frecuencia de entrada, p. ej.
$$\chi^{(3)}(\omega_\sigma;\omega_1,\omega_2,\omega_3)=\frac{1}{i\pi}\int_{-\infty}^{\infty}\frac{\chi^{(3)}(\omega_\sigma';\omega_1,\omega_2',\omega_3)}{\omega_2'-\omega_2}\,d\omega_2' \qquad (1.7.10)$$
con $\omega_\sigma'=\omega_1+\omega_2'+\omega_3$ (análogo para $\omega_1'$, $\omega_3'$). Prueba igual a la lineal: por (1.6.11), $\chi^{(3)}$ es transformada de Fourier de
una respuesta causal ⇒ analítica en $\mathrm{Im}\,\omega_1,\mathrm{Im}\,\omega_2,\mathrm{Im}\,\omega_3\ge0$ (p. 62); se cierra el contorno en el semiplano superior de
$\omega_2$. No sorprende: $\chi^{(3)}E(\omega_1)E(\omega_2)E(\omega_3)$ es **lineal en $E(\omega_2)$** y el sistema es causal.

Caso más general (Hutchings *et al.*, 1992, §6.2):
$$\chi^{(n)}(\omega_\sigma;\omega_1+p_1\omega,\omega_2+p_2\omega,\dots,\omega_n+p_n\omega)=\frac{1}{i\pi}\int_{-\infty}^{\infty}\frac{\chi^{(n)}(\omega_\sigma';\omega_1+p_1\omega',\omega_2+p_2\omega',\dots,\omega_n+p_n\omega')}{\omega'-\omega}\,d\omega' \qquad (1.7.11)$$
con $p_i\ge0$ para todo $i$ y al menos un $p_i\neq0$. Casos especiales: SHG
$$\chi^{(2)}(2\omega;\omega,\omega)=\frac{1}{i\pi}\int_{-\infty}^{\infty}\frac{\chi^{(2)}(2\omega';\omega',\omega')}{\omega'-\omega}\,d\omega' \qquad (1.7.12)$$
THG
$$\chi^{(3)}(3\omega;\omega,\omega,\omega)=\frac{1}{i\pi}\int_{-\infty}^{\infty}\frac{\chi^{(3)}(3\omega';\omega',\omega',\omega')}{\omega'-\omega}\,d\omega' \qquad (1.7.13)$$
Cambio de índice inducido por un **haz auxiliar** (no degenerado, $\chi^{(3)}(\omega;\omega,\omega_1,-\omega_1)$; Hutchings *et al.*, 1992):
$$\chi^{(3)}(\omega;\omega,\omega_1,-\omega_1)=\frac{1}{i\pi}\int_{-\infty}^{\infty}\frac{\chi^{(3)}(\omega';\omega',\omega_1,-\omega_1)\,d\omega'}{\omega'-\omega} \qquad (1.7.14)$$
**No hay relación KK** para el proceso más importante: el **cambio autoinducido del índice**, $\chi^{(3)}(\omega;\omega,\omega,-\omega)$: no tiene la
forma de (1.7.10)/(1.7.11) porque las dos primeras frecuencias son iguales y la tercera es negativa (p. 63); además, en
modelos concretos, Re e Im de $\chi^{(3)}$ no están relacionadas como exige KK (ver problemas). **Resumen**: KK siempre vale
en óptica lineal; en óptica no lineal solo para algunos procesos. (Por eso, para $n_2$ y TPA en guías se usan KK
**no degeneradas** —(1.7.14), Sheik-Bahae/Hutchings— y no la forma degenerada.)

---

## Complemento para el examen: $\chi^{(3)}$ en medios isótropos y coeficientes $A$, $B$ de Maker–Terhune

**Lo que está en este capítulo:** (i) Tabla 1.5.4, caso isótropo: 21 elementos no nulos, 3 independientes,
$\chi_{1111}=\chi_{1122}+\chi_{1212}+\chi_{1221}$ (p. 53); (ii) el oscilador centrosimétrico isótropo (1.4.52) da
$\chi_{ijkl}\propto\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}$, es decir $\chi_{1122}=\chi_{1212}=\chi_{1221}=\tfrac13\chi_{1111}$ (Problema 4). En general, para un medio
isótropo:
$$\chi_{ijkl}=\chi_{1122}\delta_{ij}\delta_{kl}+\chi_{1212}\delta_{ik}\delta_{jl}+\chi_{1221}\delta_{il}\delta_{jk}.$$

**Lo que NO está en este capítulo** (se desarrolla en Boyd §4.2, "Tensor nature of the third-order susceptibility";
se resume aquí por pedido, **a verificar contra el apunte del cap. 4**): para el índice no lineal, $\chi_{ijkl}(\omega=\omega+\omega-\omega)$,
la permutación intrínseca da $\chi_{1122}=\chi_{1212}$, y
$$\mathbf P^{\rm NL}(\omega)=\epsilon_0A(\mathbf E\cdot\mathbf E^*)\mathbf E+\tfrac12\epsilon_0B(\mathbf E\cdot\mathbf E)\mathbf E^*,\qquad A=6\chi_{1122},\quad B=6\chi_{1221}$$
(notación de Maker y Terhune, 1965). Valores típicos de $B/A$: 0 para no linealidad electrostrictiva, 1 para
no linealidad electrónica no resonante (Kleinman: $\chi_{1122}=\chi_{1212}=\chi_{1221}$), 6 para orientación molecular (efecto Kerr de
líquidos). Para luz linealmente polarizada en un medio isótropo, $\chi^{(3)}_{\rm eff}=\chi_{1111}$ y $n_2^{\rm circ}/n_2^{\rm lin}=A/(A+B)$.
[Estas relaciones provienen de mi conocimiento de §4.2, no de la lectura de este tramo.]

---

## Tablas y datos numéricos útiles

| Cantidad | Valor | Ec./pág. |
|---|---|---|
| Campo atómico $E_{\rm at}=e/(4\pi\epsilon_0a_0^2)$ | $5.14\times10^{11}$ V/m | p. 3 |
| $\chi^{(2)}\sim1/E_{\rm at}$ | $1.94\times10^{-12}$ m/V | (1.1.3) |
| $\chi^{(3)}\sim1/E_{\rm at}^2$ | $3.78\times10^{-24}$ m²/V² | (1.1.4) |
| $I_{\rm at}=\tfrac12\epsilon_0cE_{\rm at}^2$ | $3.5\times10^{20}$ W/m² $=3.5\times10^{16}$ W/cm² | (1.1.6) |
| $\chi^{(2)}=e^3/(\epsilon_0m^2\omega_0^4d^4)$, $\omega_0=10^{16}$ rad/s, $d=3$ Å | $6.9\times10^{-12}$ m/V | (1.4.32) |
| $\chi^{(3)}=e^4/(\epsilon_0m^3\omega_0^6d^5)$, $\omega_0=7\times10^{15}$ rad/s, $d=3$ Å | $344$ pm²/V² $=3.44\times10^{-22}$ m²/V² | (1.4.56) |
| Densidad atómica de materia condensada | $\sim10^{22}$ cm⁻³ | p. 27 |
| Conversión $d$: pm/V → esu (cm/statvolt) | × $3\times10^{-8}/4\pi=2.386\times10^{-9}$ | Tabla 1.5.3 |
| $\chi^{(2)}=2d$ | en cualquier sistema | Tabla 1.5.3 |
| Clases cristalinas: total / no centrosimétricas / con inversión / polares | 32 / 21 / 11 / 10 | pp. 44, 51–52 |
| Nº de elementos independientes de $\chi^{(2)}$ | 324 → 81 → 27 → 18 (SHG) → 10 (Kleinman) | pp. 33, 48–49 |
| Nº de componentes de frecuencia en $\tilde E^3$ con 3 frecuencias | 44 | p. 12 |

[Comprobación de la conversión: $\chi^{(2)}_{\rm esu}=\frac{3\times10^4}{4\pi}\chi^{(2)}_{\rm SI}$ (Problema 1: $5.4\times10^{-11}$ m/V ↔ $1.3\times10^{-7}$ esu). Con la entrada en pm/V se
multiplica además por $10^{-12}$: $d_{\rm esu}=d[\text{pm/V}]\times2.387\times10^{-9}$, que coincide con la nota de la tabla.]

**Valores de $d$** (Tabla 1.5.3, pm/V): GaAs $d_{36}=370$; CdGeAs₂ $d_{36}=235$; CdS $d_{33}=78$, $d_{31}=-40$; AgGaSe₂ $d_{36}=33$;
LiNbO₃ $d_{33}\approx-30$ (impreso $d_{32}$), $d_{31}=-5.9$; proustita $d_{22}=18$, $d_{15}=11$; pirargirita $d_{15}=8$, $d_{22}=9$; LiIO₃
$d_{15}=-5.5$, $d_{31}=-7$; BBO $d_{22}=2.2$; KDP $d_{36}=0.43$; KD*P $d_{36}=0.42$; cuarzo $d_{11}=0.3$, $d_{14}=0.008$.

---

## Problemas del final del capítulo (pp. 63–65)

1. **Conversion from Gaussian to SI units.** Para la proustita, $\chi^{(2)}_{yyy}$ vale $1.3\times10^{-7}$ cm/statvolt en unidades gaussianas.
   ¿Cuál es su valor en unidades MKS? [Resp.: $5.4\times10^{-11}$ m/V.]

2. **Numerical estimate of nonlinear optical quantities.** Un haz láser de frecuencia $\omega$ que lleva 1 W de potencia se
   enfoca a una mancha de 30 µm de diámetro en un cristal de índice $n=2$ y susceptibilidad de segundo orden
   $\chi^{(2)}=4\times10^{-11}$ m/V. Calcule numéricamente la amplitud $P(2\omega)$ de la componente de la polarización no lineal que
   oscila a $2\omega$. Estime numéricamente la amplitud del momento dipolar por átomo $\mu(2\omega)$ que oscila a $2\omega$. Compare
   este valor con la unidad atómica de momento dipolar ($ea_0$, con $a_0$ el radio de Bohr) y con la respuesta lineal del
   átomo, es decir, con la componente $\mu(\omega)$ del momento dipolar que oscila a $\omega$. Se verá en el próximo capítulo que,
   en estas condiciones, casi toda la potencia incidente puede convertirse al segundo armónico en un cristal de 1 cm.
   [Resp.: $P(2\omega)=4.7\times10^{-11}$ C/m³. Suponiendo $N=10^{28}$ átomos/m³, $\mu(2\omega)=4.7\times10^{-39}$ C·m $=5.56\times10^{-10}\,ea_0$, con
   $ea_0=8.5\times10^{-30}$ C·m. En comparación, $P(\omega)=9.7\times10^{-6}$ C/m³ y $\mu(\omega)=9.7\times10^{-34}$ C·m $=1.14\times10^{-4}\,ea_0$, de modo que
   $\mu(2\omega)/\mu(\omega)=4.9\times10^{-6}$.] [Las unidades de $P$ se leen "C/m³"; para una polarización deberían ser C/m².]

3. **Perturbation expansion.** Explique por qué no es necesario incluir el término $\lambda^0\tilde x^{(0)}$ en la serie de potencias
   de la Ec. (1.4.6).

4. **Tensor properties of the anharmonic oscillator model.** Partiendo de la Ec. (1.4.52), relevante para un conjunto de
   osciladores anarmónicos isótropos y centrosimétricos, demuestre que la susceptibilidad no lineal tiene las propiedades
   tensoriales
   $$\chi_{1122}=\chi_{1212}=\chi_{1221}=\chi_{1133}=\chi_{1313}=\chi_{1331}=\chi_{2233}=\chi_{2323}=\chi_{2332}=\chi_{2211}=\chi_{2121}=\chi_{2112}=\chi_{3311}=\chi_{3131}=\chi_{3113}=\chi_{3322}=\chi_{3232}=\chi_{3223}=\tfrac13\chi_{1111}=\tfrac13\chi_{2222}=\tfrac13\chi_{3333},$$
   y que todos los demás elementos se anulan. Dé un argumento físico simple que explique por qué se anulan los elementos
   nulos. Dé también un argumento físico simple que explique por qué $\chi_{ijkl}$ tiene componentes tensoriales fuera de la
   diagonal, aunque el medio sea isótropo.

5. **Comparison of the centrosymmetric and noncentrosymmetric models.** Para el oscilador anarmónico no centrosimétrico
   descrito por la Ec. (1.4.1), deduzca una expresión para el desplazamiento de tercer orden $\tilde x^{(3)}$ y, en consecuencia,
   para la susceptibilidad de tercer orden $\chi^{(3)}_{1111}(\omega_q,\omega_m,\omega_n,\omega_p)$. Compare este resultado con el dado por la Ec. (1.4.52)
   para un medio puramente centrosimétrico. Note que para un medio no centrosimétrico ambas contribuciones pueden estar
   presentes. Estime el tamaño de cada contribución para ver cuál es mayor.

6. **Determination of $d_{\rm eff}$.** Verifique las Ecs. (1.5.30a) y (1.5.30b).

7. **Formal properties of the third-order response.** La Sección 1.5 describe algunas propiedades matemáticas formales de
   la susceptibilidad de segundo orden. En este problema debe determinar las propiedades de simetría análogas de la
   susceptibilidad de tercer orden $\chi^{(3)}$. Incluya las ecuaciones análogas a las Ecs. (1.5.1), (1.5.2), (1.5.5), (1.5.6),
   (1.5.8), (1.5.9) y (1.5.19).

8. **Consequences of crystalline symmetry.** Mediante la consideración explícita de las propiedades de simetría de cada uno
   de los 32 grupos puntuales, verifique los resultados de las Tablas 1.5.2 y 1.5.4 y de la Fig. 1.5.3. [Notas: el problema
   es largo y requiere más conocimiento de teoría de grupos y simetría cristalina que el presentado en el texto; ver las
   lecturas recomendadas en la lista de referencias del capítulo y la discusión en Butcher (1965).]

9. **Subtlety regarding crystal class 432.** Según la Tabla 1.5.2, $\chi^{(2)}$ tiene elementos no nulos para la clase 432, pero
   según la Fig. 1.5.3 $d_{il}$ para esta clase se anula idénticamente. Justifique ambas afirmaciones teniendo en cuenta
   explícitamente las restricciones adicionales implícitas en la definición de la matriz $d_{il}$.

10. **Kramers–Kronig relations.** Muestre por cálculo explícito que la susceptibilidad lineal de una transición óptica
    modelada en la aproximación de dos niveles obedece las relaciones de Kramers–Kronig, pero que ni la susceptibilidad
    total $\chi$ ni la de tercer orden $\chi^{(3)}$ las obedecen. Explique el resultado hallando la ubicación de los polos de $\chi$ y de
    $\chi^{(3)}$. [Pistas: $\chi^{(1)}$ y $\chi^{(3)}$ están dadas por las Ecs. (6.3.33) y $\chi$ por la Ec. (6.3.23).]

11. **Kramers–Kronig relations.** Para el modelo del oscilador anarmónico clásico de la Ec. (1.4.20), muestre por cálculo
    explícito que $\chi^{(2)}(2\omega;\omega,\omega)$ obedece las relaciones de Kramers–Kronig en la forma (1.7.12). Muestre también que
    $\chi^{(2)}(\omega_1;\omega_3,-\omega_2)$ no satisface relaciones de Kramers–Kronig.

12. **Example of the third-order response.** La polarización de tercer orden incluye un término que oscila a la frecuencia
    fundamental, dado por
    $$P^{(3)}(\omega)=3\epsilon_0\chi^{(3)}|E(\omega)|^2E(\omega).$$
    Suponga que el campo a frecuencia $\omega$ incluye dos contribuciones que se propagan en las direcciones de los vectores de
    onda $\mathbf k_1$ y $\mathbf k_2$. Suponga también que la segunda contribución es lo bastante débil para tratarse linealmente. Calcule
    la polarización no lineal a la frecuencia fundamental y dé la interpretación física de sus distintos términos.

*Pistas propias (no del libro):* P3: $\tilde x^{(0)}$ solo podría ser una solución estática sin campo; el equilibrio es
$\tilde x=0$ (o se redefine el origen), y además $\tilde x^{(0)}$ satisfaría la ecuación homogénea amortiguada, que decae. P9: en
432, $\chi_{xyz}=-\chi_{xzy}$ es antisimétrico en los dos últimos índices; $d_{il}$ presupone simetría en ellos (SHG o Kleinman),
así que la parte simétrica que sobrevive, $\tfrac12(\chi_{xyz}+\chi_{xzy})$, es cero y $d_{14}=0$. P12: con $E=E_1e^{i\mathbf k_1\cdot\mathbf r}+E_2e^{i\mathbf k_2\cdot\mathbf r}$, a primer orden en $E_2$:
$3\epsilon_0\chi^{(3)}[|E_1|^2E_1e^{i\mathbf k_1\cdot\mathbf r}+2|E_1|^2E_2e^{i\mathbf k_2\cdot\mathbf r}+E_1^2E_2^*e^{i(2\mathbf k_1-\mathbf k_2)\cdot\mathbf r}]$: SPM del haz fuerte, XPM (factor 2) sobre el débil, y
una onda en la dirección $2\mathbf k_1-\mathbf k_2$ (mezcla de cuatro ondas / rejilla).

---

## Referencias principales del capítulo (pp. 65–67)

- Armstrong, Bloembergen, Ducuing, Pershan, *Phys. Rev.* **127**, 1918 (1962) — teoría de interacciones no lineales.
- Franken, Hill, Peters, Weinreich, *Phys. Rev. Lett.* **7**, 118 (1961) — primera SHG.
- Kaiser y Garrett, *Phys. Rev. Lett.* **7**, 229 (1961) — primera TPA.
- Kleinman, *Phys. Rev.* **126**, 1977 (1962) — simetría de Kleinman.
- Miller, *Appl. Phys. Lett.* **5**, 17 (1964) — regla de Miller; Garrett y Robinson, *IEEE JQE* **2**, 328 (1966).
- Midwinter y Warner, *Brit. J. Appl. Phys.* **16**, 1135 (1965) — $d_{\rm eff}$ por clase.
- Butcher (1965), *Nonlinear Optical Phenomena* — tablas de simetría; Hellwarth, *Prog. Quantum Electron.* **5**, 1 (1977);
  Shang y Hsu, *IEEE JQE* **23**, 177 (1987).
- Owyoung (1971), tesis Caltech — oscilador anarmónico; Boyd, *J. Mod. Opt.* **46**, 367 (1999) — órdenes de magnitud.
- Shoji *et al.*, *JOSA B* **14**, 2268 (1997) — medidas de $d$; Smith, SNLO; Sutherland (1996), *Handbook of NLO*.
- Hutchings, Sheik-Bahae, Hagan, Van Stryland, *Opt. Quantum Electron.* **24**, 1 (1992) — KK no lineales.
- Byer y Harris, *Phys. Rev.* **168**, 1064 (1968); Harris, Oshman, Byer, *PRL* **18**, 732 (1967) — fluorescencia paramétrica.
- Libros: Bloembergen (1964), Shen (1984), Yariv (1975), Zernike y Midwinter (1973), Agrawal (1989), Butcher y Cotter
  (1990), Nye (1985), Buerger (1963), Landau y Lifshitz (1960).

---

## Relación con el curso y con el proyecto final

- **Curso:** este capítulo es el **tema 4** del programa (examen). Lo central: (1.1.2), (1.1.3)–(1.1.6), (1.2.7), (1.2.13)–(1.2.14),
  (1.2.17) con factores de degeneración, (1.3.12)/(1.3.19)/(1.3.21), oscilador anarmónico completo (1.4.1)–(1.4.27) y
  (1.4.33)–(1.4.56), Miller (1.4.28)–(1.4.32), simetrías (1.5.5), (1.5.6), (1.5.7)–(1.5.9), (1.5.19), notación contraída
  (1.5.20)–(1.5.27), $d_{\rm eff}$ (1.5.28)–(1.5.30), inversión (1.5.31)–(1.5.35), tablas 1.5.2–1.5.4, (1.6.5), (1.6.9), (1.6.11), KK (1.7.5)–(1.7.14).
  El tema 5 (cap. 2) usa $d_{\rm eff}$ y la convención de factores 2/4 de (1.5.28)–(1.5.29).
- **Proyecto final (SC en SiN / Si):**
  - Si (diamante, $m3m$) y SiN amorfo son **centrosimétricos** ⇒ $\chi^{(2)}_{\rm bulk}=0$ (§1.5.10, 1.5.13); la no linealidad dominante
    es $\chi^{(3)}$: Kerr ($n_2$, (1.2.14)), SPM/XPM (factores 3 y 6 de (1.2.17)), FWM, TPA en Si (§1.2.12), Raman (§1.2.13).
    (Los efectos de $\chi^{(2)}$ observados en SiN/Si strained provienen de ruptura de simetría superficial o por tensión.)
  - Si es cúbico $m3m$: $\chi^{(3)}$ con **4 elementos independientes** (Tabla 1.5.4) ⇒ $n_2$ y TPA dependen de la orientación
    de la guía respecto a los ejes cristalinos (anisotropía, $\chi_{xxxx}\neq\chi_{xxyy}+\chi_{xyxy}+\chi_{xyyx}$). SiN amorfo: isótropo, 3 independientes.
  - El orden de magnitud $\chi^{(3)}\sim10^{-22}$–$10^{-24}$ m²/V² (1.1.4), (1.4.56) es el que se espera para SiN ($n_2\sim2.4\times10^{-19}$ m²/W);
    ver relación $n_2\leftrightarrow\chi^{(3)}$ (atención a la errata de (1.2.14b)).
  - La descripción temporal §1.6 (función respuesta $R^{(3)}$) es la base de la respuesta Raman retardada en la GNLSE
    del supercontinuo; KK no degeneradas (1.7.14) conectan TPA y $n_2$ dispersivos.

---

## Erratas y dudas de lectura

1. **(1.2.14b), p. 12**: se lee $n_2=\dfrac{3}{2n_0^2\epsilon_0c}\chi^{(3)}$ con $I=\tfrac12n_0\epsilon_0c\mathcal E^2$. Derivando con esas mismas definiciones se
   obtiene $n_2=\dfrac{3}{4n_0^2\epsilon_0c}\chi^{(3)}$, que es la forma de la §4.1 (ec. 4.1.19). Por consistencia debería ser $3/(4n_0^2\epsilon_0c)$
   [verificar en el apunte del cap. 4].
2. **Nota al pie p. 7**: se lee $\tilde P(t)=\tfrac12\sum_nP'(\omega_n)e^{i\omega_nt}$; por consistencia con el campo debería ser $e^{-i\omega_nt}$.
3. **(1.4.19), p. 25**: se lee $x^{(2)}(2\omega_i)$; debería ser $x^{(2)}(2\omega_1)$.
4. **§1.5.8, p. 42**: "3m … plano de simetría especular perpendicular a este eje"; en la notación estándar, en 3m los
   planos espejo **contienen** el eje ternario (la Tabla 1.5.2 lo confirma: "plano espejo ⊥ $\hat x$").
5. **Tabla 1.5.2, clase 3**: se lee $xxx=-xyy=-yyz=-yxy$; por consistencia debería ser $-yyx$.
6. **Tabla 1.5.2, clase 622**: se lee $xzy=-yxz$; por consistencia (422, 6) debería ser $xzy=-yzx$.
7. **Tabla 1.5.3**: KDP y KD*P aparecen con grupo "2m"; deberían ser $\bar42m$. LiNbO₃: se lee $d_{32}=-30$; en 3m $d_{32}=d_{31}$, así que
   debería ser $d_{33}=-30$ pm/V.
8. **Tabla 1.5.4, tetragonal 4, $\bar4$, 4/m**: se lee $xxzz=zzyy$; por consistencia debería ser $xxzz=yyzz$.
9. **Problema 2**: unidades de $P(2\omega)$ y $P(\omega)$ impresas como C/m³; deberían ser C/m².
10. **(1.7.8)**: verificado, el signo "+" del primer término de la segunda línea es correcto (no es errata).
11. **Regla de Miller**: el libro no da valor numérico del "delta de Miller"; los valores citados en §1.4.2 de este apunte
    son de literatura externa y deben verificarse.
