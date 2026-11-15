# Capítulo 9 — Stimulated Brillouin and Stimulated Rayleigh Scattering (Boyd, 3.ª ed.)

Páginas del libro 429–471 (PDF 447–489; la p. 472 del libro, PDF 490, está en blanco). Leído el 2026-11-14.

Fuente: R. W. Boyd, *Nonlinear Optics*, 3.ª ed., Academic Press, 2008, cap. 9.
Las citas de página son páginas del libro (sumar 18 para la página del PDF).

Convención de Boyd (SI): $\tilde E(t)=Ee^{-i\omega t}+\text{c.c.}$, $I=2n\epsilon_0c|E|^2$, $\tilde P=\epsilon_0[\chi^{(1)}\tilde E+\chi^{(2)}\tilde E^2+\chi^{(3)}\tilde E^3+\dots]$.
Notación del capítulo: $\omega_1$ (láser/bombeo, viaja hacia $+z$) y $\omega_2$ (Stokes, viaja hacia $-z$), $\Omega=\omega_1-\omega_2$; $\epsilon$ = constante dieléctrica
relativa; $\gamma_e=\rho\,\partial\epsilon/\partial\rho$ constante electrostrictiva; $C$ compresibilidad ($C_T$ isotérmica, $C_s$ adiabática); $v$ velocidad del sonido;
$\Gamma_B$ ancho Brillouin (FWHM en rad/s), $\Gamma_R$ ancho Rayleigh; $\gamma=c_p/c_v$; $\alpha$ coeficiente de absorción óptica (no la polarizabilidad).

---

## Resumen del capítulo

El capítulo estudia la dispersión **estimulada** por variaciones de densidad inducidas por la luz. Primero (§9.2) deduce la
**electrostricción**: un campo $E$ produce una presión estrictiva $p_{\rm st}=-\frac12\epsilon_0\gamma_eE^2$ que densifica el material
($\Delta\rho=\frac12\epsilon_0\rho C\gamma_eE^2$), lo que da una contribución a la no linealidad de tercer orden
$\chi^{(3)}=\frac13\epsilon_0C_T\gamma_e^2$ ($\sim3\times10^{-21}$ m²/V² en materia condensada; ≈ 20 % del $\chi^{(3)}$ de fibras de sílice). En §9.3 el
batido láser–Stokes impulsa por electrostricción una onda acústica a $\Omega_B=2nv\omega/c$ con $q=2k$, que a su vez dispersa el láser
hacia la Stokes: el **SBS** es un proceso de ganancia pura con ajuste de fase automático, descrito por $dI_1/dz=dI_2/dz=-gI_1I_2$ con una
ganancia lorentziana de ancho $\Gamma_B$ y pico $g_0=\gamma_e^2\omega^2/(nvc^3\rho_0\Gamma_B)$ independiente de $\omega$ (Tabla 9.3.1:
CS₂ 1.5 m/GW, SiO₂ 0.045 m/GW, $\Omega_B/2\pi$ de algunos GHz en líquidos y ≈ 26 GHz en sílice a 694 nm). Resuelve el amplificador con
agotamiento del bombeo y el **generador** iniciado por ruido térmico, con umbral $G_{\rm th}=gI_1L\approx25$–30, reflectividad que tiende a
1 y anclaje de la intensidad transmitida; da la potencia umbral mínima con enfoque ($P_{\rm th}=G_{\rm th}\lambda/2g$ ≈ 9 kW en CS₂) y el
aumento del umbral con pulsos cortos frente a la vida del fonón. §9.4 explica la **conjugación de fase por SBS** (experimento de
Zel'dovich *et al.* 1972) por la ganancia doble ($C=2$) que experimenta la componente de ruido cuyo patrón de speckle coincide con el del
láser. §9.5 trata SBS en **gases** comprimidos (ganancia $\propto N^2$ frente a $N$ del SRS). §9.6 construye la teoría general desde las
ecuaciones hidrodinámicas linealizadas (continuidad, Navier–Stokes, calor) con acoplamiento electrostrictivo y absortivo, y obtiene las
ganancias de **SBS** y **dispersión Rayleigh estimulada (SRLS)** electrostrictivas y térmicas, sus formas espectrales (Fig. 9.6.1) y sus
escalamientos con la frecuencia; el apéndice define los coeficientes de viscosidad y la relación de Stokes.

---

## Secciones

### 9.1 Stimulated Scattering Processes (p. 429)

La dispersión es **espontánea** si las fluctuaciones (de la constante dieléctrica) que la causan son
excitadas térmicamente o por efectos cuánticos de punto cero; es **estimulada** si las induce el propio campo
luminoso. La estimulada es mucho más eficiente: en 1 cm de agua líquida la dispersión espontánea saca del haz
≈ 1 parte en $10^5$ de la potencia visible (nota al pie: $R\sim10^{-6}$ cm⁻¹ en agua), mientras que con intensidad
suficiente la dispersión estimulada puede dispersar ≈ 100 % del haz en 1 cm.

El capítulo trata dispersión estimulada por **variaciones de densidad inducidas**. Ejemplo principal: **SBS**
(Fig. 9.1.1, p. 430): láser $\omega_L$ que se dispersa en la variación de índice asociada a una onda de sonido de
frecuencia $\Omega$; como los frentes acústicos se alejan del láser, la luz dispersada baja a la frecuencia Stokes
$\omega_S=\omega_L-\Omega$. Mecanismo de realimentación: la interferencia láser–Stokes contiene la componente
$\omega_L-\omega_S=\Omega$; la respuesta del material a ese batido refuerza la onda acústica, y el batido láser–sonido
refuerza la Stokes → crecimiento exponencial. Primera observación: Chiao *et al.* (1964).

Dos mecanismos de acoplamiento: (1) **electrostricción** (los materiales se densifican donde la intensidad es
alta; §9.2–9.3); (2) **absorción** óptica (el calentamiento dilata el material en las zonas de alta intensidad;
solo en medios con pérdidas, menos usada; §9.6).

Dos configuraciones (Fig. 9.1.2, p. 431): (a) **generador SBS**: solo se aplica el láser; Stokes y onda acústica crecen
desde el ruido (dispersión en fonones térmicos), a la frecuencia de máxima ganancia (§9.3); (b) **amplificador
SBS**: se inyectan láser y una semilla Stokes débil; el acoplamiento es fuerte solo si la frecuencia inyectada es
aproximadamente la que crearía el generador. SBS amplifica Stokes en cualquier dirección excepto la del láser
(nota: ondas copropagantes solo interactuarían mediante ondas acústicas de longitud de onda infinita, imposibles
en un medio finito; §9.3), pero se observa usualmente **hacia atrás**, porque ahí el traslape espacial es máximo.

### 9.2 Electrostriction (p. 431)

**Electrostricción**: tendencia de los materiales a comprimirse en presencia de un campo eléctrico. Interesa como
mecanismo de respuesta de tercer orden y como acoplamiento del SBS. Ilustración (Fig. 9.2.1, p. 432): (a) una
placa dieléctrica cerca del campo de borde de un capacitor de placas paralelas es atraída hacia la zona de campo
máximo; (b) una molécula en el campo de borde, con dipolo $\mathbf p$, también es atraída.

*Visión global*: el cambio de energía potencial por unidad de volumen de un material en el campo $E$ es
$$u=\tfrac12\epsilon\epsilon_0E^2, \qquad\text{(9.2.1, p. 431)}$$
($\epsilon$ relativa); la energía total $\int u\,dV$ se maximiza dejando entrar la placa a la zona de campo máximo.

*Visión microscópica*: con $\mathbf p=\epsilon_0\alpha\mathbf E$,
$$U=-\int_0^{\mathbf E}\mathbf p\cdot d\mathbf E'=-\int_0^{\mathbf E}\epsilon_0\alpha\mathbf E'\cdot d\mathbf E'=-\tfrac12\epsilon_0\alpha\mathbf E\cdot\mathbf E\equiv-\tfrac12\epsilon_0\alpha E^2, \qquad\text{(9.2.2, p. 432)}$$
$$\mathbf F=-\nabla U=\tfrac12\epsilon_0\alpha\nabla(E^2). \qquad\text{(9.2.3)}$$
Cada molécula es atraída hacia el campo creciente.

Capacitor sumergido en un líquido dieléctrico (Fig. 9.2.2, p. 433): entran moléculas, la densidad aumenta $\Delta\rho$ y
$$\Delta\epsilon=\left(\frac{\partial\epsilon}{\partial\rho}\right)\Delta\rho, \qquad\text{(9.2.4, p. 432)}$$
$$\Delta u=\tfrac12\epsilon_0E^2\Delta\epsilon=\tfrac12\epsilon_0E^2\left(\frac{\partial\epsilon}{\partial\rho}\right)\Delta\rho. \qquad\text{(9.2.5, p. 433)}$$
Por la primera ley de la termodinámica, $\Delta u$ = trabajo de compresión por unidad de volumen:
$$\Delta w=p_{\rm st}\frac{\Delta V}{V}=-p_{\rm st}\frac{\Delta\rho}{\rho}, \qquad\text{(9.2.6)}$$
con $p_{\rm st}$ la **presión estrictiva** (contribución del campo a la presión). Igualando:
$$p_{\rm st}=-\tfrac12\epsilon_0\rho\left(\frac{\partial\epsilon}{\partial\rho}\right)E^2\equiv-\tfrac12\epsilon_0\gamma_eE^2, \qquad\text{(9.2.7, p. 433)}$$
$\gamma_e=\rho(\partial\epsilon/\partial\rho)$ (cf. (8.3.6)). Como $p_{\rm st}<0$, la presión total baja donde el campo es alto, el fluido es
atraído allí y la densidad sube: $\Delta\rho=-(\partial\rho/\partial p)\Delta p$ con $\Delta p=p_{\rm st}$,
$$\Delta\rho=-\rho\left(\frac1\rho\frac{\partial\rho}{\partial p}\right)p_{\rm st}\equiv-\rho Cp_{\rm st}, \qquad\text{(9.2.8)}$$
($C=\rho^{-1}\partial\rho/\partial p$ compresibilidad), y
$$\Delta\rho=\tfrac12\epsilon_0\rho C\gamma_eE^2. \qquad\text{(9.2.9, p. 433)}$$
Para campo estático las derivadas en $C$ y $\gamma_e$ son a $T$ constante. Para campos ópticos:
$$\Delta\rho=\tfrac12\epsilon_0\rho C\gamma_e\langle\tilde{\mathbf E}\cdot\tilde{\mathbf E}\rangle, \qquad\text{(9.2.10, p. 434)}$$
promedio sobre un período óptico. Si $\langle\tilde{\mathbf E}\cdot\tilde{\mathbf E}\rangle$ tiene componentes estáticas e hipersónicas (caso SBS), $C$ y
$\gamma_e$ se evalúan a **entropía constante** para las hipersónicas y a **temperatura constante** para las estáticas.

Cambio de susceptibilidad, $\Delta\chi=\Delta\epsilon=(\partial\epsilon/\partial\rho)\Delta\rho$:
$$\Delta\chi=\tfrac12\epsilon_0C\gamma_e^2\langle\tilde{\mathbf E}\cdot\tilde{\mathbf E}\rangle. \qquad\text{(9.2.11)}$$
Campo monocromático
$$\tilde{\mathbf E}(t)=\mathbf Ee^{-i\omega t}+\text{c.c.}; \qquad\text{(9.2.12)}$$
(el caso de dos frecuencias separadas ≈ la frecuencia Brillouin es el del SBS, §9.3). Con $\langle\tilde{\mathbf E}\cdot\tilde{\mathbf E}\rangle=2\mathbf E\cdot\mathbf E^*$:
$$\Delta\chi=\epsilon_0C_T\gamma_e^2\mathbf E\cdot\mathbf E^*. \qquad\text{(9.2.13, p. 434)}$$
Polarización no lineal, $\mathbf P=\Delta\chi\mathbf E$ (así en el libro):
$$\mathbf P=\epsilon_0C_T\gamma_e^2|\mathbf E|^2\mathbf E. \qquad\text{(9.2.14)}$$
Con la definición convencional
$$\mathbf P=3\epsilon_0\chi^{(3)}(\omega=\omega+\omega-\omega)|\mathbf E|^2\mathbf E, \qquad\text{(9.2.15)}$$
$$\chi^{(3)}(\omega=\omega+\omega-\omega)=\tfrac13\epsilon_0C_T\gamma_e^2. \qquad\text{(9.2.16, p. 434)}$$
(Ver *Erratas*: falta un $\epsilon_0$ en $\mathbf P=\Delta\chi\mathbf E$ y en (9.2.14) para que (9.2.16) sea consistente.)

Para un material isótropo, en términos de los coeficientes de Maker y Terhune (Ec. (4.2.10)): $A=C_T\gamma_e^2$ y $B=0$
(p. 435).

**Estimación numérica.** Gas diluido: $\gamma_e=n^2-1$ (8.3.12). En general, por la ley de Lorentz–Lorenz (Ec. (3.8.8a)):
$$\gamma_e=(n^2-1)(n^2+2)/3, \qquad\text{(9.2.17, p. 435)}$$
del orden de la unidad en materia condensada. $C_T\approx10^{-9}$ m²/N para CS₂ (mismo orden para toda la materia
condensada) → $\chi^{(3)}\sim3\times10^{-21}$ m²/V². Gases ideales: $C_T=1/p$, con $p=10^5$ N/m² a 1 atm, y $\gamma_e=n^2-1\approx6\times10^{-4}$
para aire → $\chi^{(3)}\sim1\times10^{-23}$ m²/V².

Expresión alternativa usando (9.2.17), $C_s=1/v^2\rho$ (8.3.21) y $C_T=\gamma C_s$ ($\gamma$ = índice adiabático):
$$\chi^{(3)}(\omega=\omega+\omega-\omega)=\frac{\epsilon_0\gamma}{3v^2\rho}\left[\frac{(n^2-1)(n^2+2)}{3}\right]^2. \qquad\text{(9.2.18, p. 435)}$$
Para pulsos tan cortos que el flujo de calor es despreciable, el factor $\gamma$ se reemplaza por 1. El $n_2$ electrostrictivo
sale de $n_2=(3/4n_0^2\epsilon_0c)\chi^{(3)}$ (Ec. (4.1.19)). La electrostricción no suele dar un $\chi^{(3)}$ grande, pero contribuye
apreciablemente en algunos materiales: en **fibras ópticas** ≈ 20 % del $\chi^{(3)}$ total (Buckland y Boyd, 1996, 1997). Y es el
acoplamiento del SBS, a menudo un proceso extremadamente fuerte.

### 9.3 Stimulated Brillouin Scattering (Induced by Electrostriction) (p. 436)

En el cap. 8 el campo no alteraba las propiedades acústicas (dispersión por ondas térmicas). Con un láser
intenso, incluso la luz espontánea se vuelve intensa; láser y dispersada baten y por electrostricción generan
variaciones de densidad y presión; el láser se dispersa en ellas hacia la frecuencia Stokes, sumándose en fase a
la Stokes que creó la perturbación → crecimiento mutuo. Fig. 9.3.1 (p. 436): onda incidente $E_1,\omega_1,\mathbf k_1$ (hacia $+z$) que se
dispersa en una onda sonora que se aleja ($\rho,\Omega,\mathbf q$, hacia $+z$) produciendo $E_2,\omega_2,\mathbf k_2$ (hacia $-z$); medio de
$z=0$ a $z=L$. (Notas: SBS absortivo en §9.6; se usan $\omega_1,\omega_2$ en lugar de $\omega_L,\omega_S$ para poder aplicar los resultados al
anti‑Stokes identificando $\omega_1\to\omega_{aS}$ y $\omega_2\to\omega_L$; solo se supone $\omega_2<\omega_1$.)

**Frecuencia Stokes en el generador.** Dispersión en una onda que se aleja:
$$\omega_2=\omega_1-\Omega_B, \qquad\text{(9.3.1, p. 437)}$$
$\Omega_B$ = **frecuencia Brillouin**, dada por la relación de dispersión del fonón
$$\Omega_B=|\mathbf q_B|v, \qquad\text{(9.3.2)}$$
con el vector de onda impuesto por el batido
$$\mathbf q_B=\mathbf k_1-\mathbf k_2. \qquad\text{(9.3.3)}$$
Con $|\mathbf k_i|=n\omega_i/c$ y ondas contrapropagantes:
$$\Omega_B=\frac{v}{c/n}(\omega_1+\omega_2). \qquad\text{(9.3.4)}$$
Eliminando $\omega_2$ con (9.3.1):
$$\Omega_B=\frac{\frac{2v}{c/n}\omega_1}{1+\frac{v}{c/n}}. \qquad\text{(9.3.5, p. 437)}$$
Como $v\ll c/n$ en todos los materiales conocidos:
$$\Omega_B=\frac{2v}{c/n}\omega_1, \qquad\text{(9.3.6)}\qquad \mathbf q_B=2\mathbf k_1. \qquad\text{(9.3.7, p. 437)}$$
**Amplificador**: $\omega_2$ se conoce a priori y la onda acústica forzada tiene
$$\Omega=\omega_1-\omega_2, \qquad\text{(9.3.8, p. 437)}$$
en general distinta de $\Omega_B$; la excitación es eficiente solo si $|\Omega-\Omega_B|\lesssim\Gamma_B$ (ancho Brillouin, (9.3.14b)).

**Ecuaciones acopladas.** $\tilde E(z,t)=\tilde E_1+\tilde E_2$:
$$\tilde E_1(z,t)=A_1(z,t)e^{i(k_1z-\omega_1t)}+\text{c.c.}, \qquad\text{(9.3.9a, p. 438)}$$
$$\tilde E_2(z,t)=A_2(z,t)e^{i(-k_2z-\omega_2t)}+\text{c.c.}, \qquad\text{(9.3.9b)}$$
$$\tilde\rho(z,t)=\rho_0+[\rho(z,t)e^{i(qz-\Omega t)}+\text{c.c.}], \qquad\text{(9.3.10)}$$
con $\Omega=\omega_1-\omega_2$, $q=2k_1$. Ecuación de onda acústica con fuente (cf. (8.3.17)):
$$\frac{\partial^2\tilde\rho}{\partial t^2}-\Gamma'\nabla^2\frac{\partial\tilde\rho}{\partial t}-v^2\nabla^2\tilde\rho=\nabla\cdot\mathbf f, \qquad\text{(9.3.11, p. 438)}$$
($\Gamma'$ de (8.3.23)), con la fuerza por unidad de volumen
$$\mathbf f=\nabla p_{\rm st},\qquad p_{\rm st}=-\tfrac12\epsilon_0\gamma_e\langle\tilde E^2\rangle. \qquad\text{(9.3.12)}$$
Para los campos (9.3.9):
$$\nabla\cdot\mathbf f=\epsilon_0\gamma_eq^2[A_1A_2^*e^{i(qz-\Omega t)}+\text{c.c.}]. \qquad\text{(9.3.13, p. 438)}$$
Sustituyendo (9.3.10) y (9.3.13) en (9.3.11) con amplitud acústica lentamente variable:
$$-2i\Omega\frac{\partial\rho}{\partial t}+(\Omega_B^2-\Omega^2-i\Omega\Gamma_B)\rho-2iqv^2\frac{\partial\rho}{\partial z}=\epsilon_0\gamma_eq^2A_1A_2^*, \qquad\text{(9.3.14a)}$$
con el **ancho de línea Brillouin**
$$\Gamma_B=q^2\Gamma'; \qquad\text{(9.3.14b, p. 438)}$$
$\tau_p=\Gamma_B^{-1}$ es el tiempo de vida del fonón.

**Aproximación de fonón no propagante.** El último término de (9.3.14a) describe la propagación de fonones; los fonones
hipersónicos están fuertemente amortiguados y recorren distancias muy cortas antes de absorberse, pequeñas frente a la
escala de variación de la fuente, así que se suele despreciar $\partial\rho/\partial z$ (puede fallar: Chiao 1965; Kroll y Kelley 1971).
Nota al pie (p. 439): $\alpha_s=\Gamma_B/v$ con $\Gamma_B\sim\eta_sq^2/\rho_0$; con $v=1\times10^3$ m/s, $\eta_s=10^{-9}$ "N m/s²", $q=4\pi\times10^6$ m⁻¹ y
$\rho_0=10$ kg m⁻³ (así impreso; ver *Erratas*) → $\Gamma_B=1.6\times10^8$ s⁻¹ y $\alpha_s^{-1}=6.3\ \mu$m. En estado estacionario ($\partial\rho/\partial t=0$):
$$\rho(z,t)=\epsilon_0\gamma_eq^2\frac{A_1A_2^*}{\Omega_B^2-\Omega^2-i\Omega\Gamma_B}. \qquad\text{(9.3.15, p. 439)}$$

Evolución de los campos ópticos:
$$\frac{\partial^2\tilde E_i}{\partial z^2}-\frac{1}{(c/n)^2}\frac{\partial^2\tilde E_i}{\partial t^2}=\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde P_i}{\partial t^2},\qquad i=1,2, \qquad\text{(9.3.16)}$$
con la polarización no lineal total
$$\tilde P=\epsilon_0\Delta\chi\tilde E=\epsilon_0\Delta\epsilon\tilde E=\epsilon_0\rho_0^{-1}\gamma_e\tilde\rho\tilde E. \qquad\text{(9.3.17, p. 439)}$$
Partes con ajuste de fase:
$$\tilde P_1=p_1e^{i(k_1z-\omega_1t)}+\text{c.c.},\qquad \tilde P_2=p_2e^{i(k_2z-\omega_2t)}+\text{c.c.}, \qquad\text{(9.3.18)}$$
$$p_1=\epsilon_0\gamma_e\rho_0^{-1}\rho A_2,\qquad p_2=\epsilon_0\gamma_e\rho_0^{-1}\rho^*A_1. \qquad\text{(9.3.19)}$$
(En (9.3.18) $\tilde P_2$ está impreso con $e^{i(k_2z-\omega_2t)}$; por (9.3.9b) debería ser $e^{i(-k_2z-\omega_2t)}$; ver *Erratas*.) Con SVEA:
$$\frac{\partial A_1}{\partial z}+\frac{1}{c/n}\frac{\partial A_1}{\partial t}=\frac{i\omega\gamma_e}{2nc\rho_0}\rho A_2, \qquad\text{(9.3.20a, p. 439)}$$
$$-\frac{\partial A_2}{\partial z}+\frac{1}{c/n}\frac{\partial A_2}{\partial t}=\frac{i\omega\gamma_e}{2nc\rho_0}\rho^*A_1, \qquad\text{(9.3.20b)}$$
con $\rho$ solución de (9.3.14a) y $\omega=\omega_1\simeq\omega_2$ (p. 440).

**Estado estacionario**: con (9.3.15),
$$\frac{dA_1}{dz}=\frac{i\epsilon_0\omega q^2\gamma_e^2}{2nc\rho_0}\frac{|A_2|^2A_1}{\Omega_B^2-\Omega^2-i\Omega\Gamma_B}, \qquad\text{(9.3.21a, p. 440)}$$
$$\frac{dA_2}{dz}=\frac{-i\epsilon_0\omega q^2\gamma_e^2}{2nc\rho_0}\frac{|A_1|^2A_2}{\Omega_B^2-\Omega^2+i\Omega\Gamma_B}. \qquad\text{(9.3.21b)}$$
El SBS es un **proceso de ganancia pura**, con **ajuste de fase automático**; por eso se pueden escribir ecuaciones para
las intensidades $I_i=2n\epsilon_0cA_iA_i^*$:
$$\frac{dI_1}{dz}=-gI_1I_2, \qquad\text{(9.3.22a)}\qquad \frac{dI_2}{dz}=-gI_1I_2, \qquad\text{(9.3.22b, p. 440)}$$
con el **factor de ganancia SBS** (lorentziano, buena aproximación cerca de resonancia):
$$g=g_0\frac{(\Gamma_B/2)^2}{(\Omega_B-\Omega)^2+(\Gamma_B/2)^2}, \qquad\text{(9.3.23)}$$
$$g_0=\frac{\gamma_e^2\omega^2}{nvc^3\rho_0\Gamma_B}. \qquad\text{(9.3.24, p. 440)}$$
(Paso intermedio implícito: $\Omega_B^2-\Omega^2\simeq2\Omega_B(\Omega_B-\Omega)$, $q=2n\omega/c$, $\Omega_B=qv$.) Con bombeo constante ($I_1$ = cte):
$$I_2(z)=I_2(L)e^{gI_1(L-z)}, \qquad\text{(9.3.25, p. 440)}$$
la Stokes inyectada en $z=L$ crece exponencialmente al propagarse hacia $-z$.

$g_0$ **no depende de $\omega$** porque $\Gamma_B\propto q^2\propto\omega^2$ (8.3.28). **Estimación para CS₂ a 1 µm** (p. 441): $\omega=2\pi\times3\times10^{14}$ rad/s,
$n=1.67$, $v=1.1\times10^3$ m/s, $\rho_0=1.26$ g/cm³ $=1.26\times10^3$ kg/m³, $\gamma_e=2.4$, $\tau_p=\Gamma_B^{-1}=4\times10^{-9}$ s → $g_0=1.5$ m/GW $=0.15$ cm/MW.

**Tabla 9.3.1** (p. 441) — propiedades del SBS (valores a $\lambda=0.694\ \mu$m; $\Gamma_B/2\pi$ = FWHM del espectro de ganancia en Hz; la
última columna es el parámetro del SBS absortivo, §9.6; al cambiar de frecuencia: $\Omega_B\propto\omega$, $\Gamma_B\propto\omega^2$, $g_0$ independiente
de $\omega$, $g_B^a(\max)\propto\omega^{-3}$):

| Sustancia | $\Omega_B/2\pi$ (MHz) | $\Gamma_B/2\pi$ (MHz) | $g_0$ (m/GW) | $g_B^a(\max)/\alpha$ (cm²/MW) |
|---|---|---|---|---|
| CS₂ | 5850 | 52.3 | 1.5 | 0.14 |
| Acetona | 4600 | 224 | 0.2 | 0.022 |
| Tolueno | 5910 | 579 | 0.13 | — |
| CCl₄ | 4390 | 520 | 0.06 | 0.013 |
| Metanol | 4250 | 250 | 0.13 | 0.013 |
| Etanol | 4550 | 353 | 0.12 | 0.010 |
| Benceno | 6470 | 289 | 0.18 | 0.024 |
| H₂O | 5690 | 317 | 0.048 | 0.0008 |
| Ciclohexano | 5550 | 774 | 0.068 | — |
| CH₄ (1400 atm) | 150 | 10 | 1 | — |
| Vidrios ópticos | 15 000–26 000 | 10–106 | 0.04–0.25 | — |
| SiO₂ | 25 800 | 78 | 0.045 | — |

**Anti‑Stokes** ($\omega_{aS}=\omega_L+\Omega_B$): identificando $\omega_1\to\omega_{aS}$, $\omega_2\to\omega_S$ [sic; por la nota de la p. 436 debería ser $\omega_L$], el
bombeo constante corresponde a $I_2$ = cte y (9.3.22a) da $I_1(z)=I_1(0)e^{-gI_2z}$: la onda anti‑Stokes, que viaja hacia $+z$, es
**atenuada** por el SBS.

#### 9.3.1 Pump Depletion Effects in SBS (p. 442)

Cuando la Stokes es comparable al bombeo, hay que resolver (9.3.22) simultáneamente. Como $dI_1/dz=dI_2/dz$:
$$I_1(z)=I_2(z)+C, \qquad\text{(9.3.26, p. 442)}$$
$$\frac{dI_2}{I_2(I_2+C)}=-g\,dz, \qquad\text{(9.3.27)}\qquad \int_{I_2(0)}^{I_2(z)}\frac{dI_2}{I_2(I_2+C)}=-\int_0^zg\,dz', \qquad\text{(9.3.28)}$$
$$\ln\left\{\frac{I_2(z)[I_2(0)+C]}{I_2(0)[I_2(z)+C]}\right\}=-gCz. \qquad\text{(9.3.29)}$$
Con $C=I_1(0)-I_2(0)$:
$$I_2(z)=\frac{I_2(0)[I_1(0)-I_2(0)]}{I_1(0)\exp\{gz[I_1(0)-I_2(0)]\}-I_2(0)}, \qquad\text{(9.3.30a, p. 442)}$$
$$I_1(z)=I_2(z)+I_1(0)-I_2(0). \qquad\text{(9.3.30b)}$$
Pero las condiciones de frontera físicamente conocidas son $I_1(0)$ e $I_2(L)$ (Fig. 9.3.2, p. 443). Evaluando en $z=L$:
$$I_2(L)=\frac{I_1(0)[I_2(0)/I_1(0)][1-I_2(0)/I_1(0)]}{\exp\{gI_1(0)L[1-I_2(0)/I_1(0)]\}-I_2(0)/I_1(0)}, \qquad\text{(9.3.31, p. 442)}$$
ecuación trascendente para la incógnita $I_2(0)/I_1(0)$.

Fig. 9.3.3 (p. 443): **características de transferencia del amplificador SBS**: fracción transferida $[I_2(0)-I_2(L)]/I_1(0)$ vs.
$G=gI_1(0)L$ (ganancia exponencial de una señal débil), de 0 a 100, para $I_2(L)/I_1(0)=1,10^{-2},10^{-4},10^{-8},10^{-12}$; todas tienden a 1:
con $G$ suficientemente grande la transferencia de energía del bombeo a la Stokes es prácticamente completa (curvas
más a la derecha para semillas más débiles; para $10^{-12}$ la transferencia empieza hacia $G\approx25$–30).

#### 9.3.2 SBS Generator (p. 443)

Sin Stokes inyectada, el proceso se inicia con fotones Stokes de dispersión Brillouin espontánea cerca del plano de salida
$z=L$; se espera
$$I_2(L)=fI_1(L). \qquad\text{(9.3.32, p. 444)}$$
Bajo umbral (reflectividad $R=I_2(0)/I_1(0)\ll1$), $I_1$ ≈ constante, $I_2(0)=I_2(L)e^G$ con $G=gI_1(0)L$ e $I_2(L)=fI_1(0)$:
$$R\equiv\frac{I_2(0)}{I_1(0)}=fe^G. \qquad\text{(9.3.33, p. 444)}$$
Umbral aparente: se define como $R=R_{\rm th}$, típicamente $R_{\rm th}=0.01$, que ocurre en $G_{\rm th}$; para muchos materiales y longitudes de
onda **$G_{\rm th}\approx25$–30** (cálculo teórico desde las fluctuaciones térmicas: Boyd *et al.* 1990). Así
$f\sim\exp(-G_{\rm th})\approx10^{-12}$–$10^{-11}$ (estimación análoga de Zel'dovich *et al.* 1985).

Sobre umbral ($G>G_{\rm th}$), (9.3.31) se escribe
$$\frac{I_2(L)}{I_1(0)}=\frac{R(1-R)}{\exp[G(1-R)]-R}; \qquad\text{(9.3.34, p. 444)}$$
se puede despreciar el $-R$ del denominador. De (9.3.30b), $I_1(L)-I_2(L)=I_1(0)-I_2(0)$; con (9.3.32) y $f$ pequeño, el lado izquierdo
≈ $f^{-1}I_2(L)$, y multiplicando por $f/I_1(0)$: $I_2(L)/I_1(0)=f(1-R)$. Sustituyendo en (9.3.34) y despejando $G$, con $G_{\rm th}=-\ln f$:
$$\frac{G}{G_{\rm th}}=\frac{G_{\rm th}^{-1}\ln R+1}{1-R}. \qquad\text{(9.3.35, p. 445)}$$
Fig. 9.3.4 (p. 445): $R$ vs. $G/G_{\rm th}$ (0–10) para $G_{\rm th}=25$: casi nula para $G<G_{\rm th}$, sube rápidamente justo encima y tiende a
100 % para $G\gg G_{\rm th}$. Muy por encima del umbral ($G\gtrsim3G_{\rm th}$), $G/G_{\rm th}\simeq1/(1-R)$:
$$R=1-\frac{1}{G/G_{\rm th}}\qquad(G\gg G_{\rm th}). \qquad\text{(9.3.36, p. 445)}$$
Como $I_1(L)=I_1(0)(1-R)$, la intensidad transmitida queda
$$I_1(L)=\frac{G_{\rm th}}{gL}; \qquad\text{(9.3.37, p. 446)}$$
$G_{\rm th}/gL$ es la intensidad de entrada en el umbral: la transmitida queda **"anclada" (clamped)** en el valor umbral.
Fig. 9.3.5 (p. 446): $I_1(z)/I_1(0)$ e $I_2(z)/I_1(0)$ dentro de un generador SBS (graficado para $G_{\rm th}=10$; con el realista 25 la
variación se concentra cerca de $z=0$): ambas decaen desde $z=0$ y se aplanan.

**Potencia umbral mínima** (p. 446): haz gaussiano enfocado fuertemente en la celda; intensidad en la cintura
$I=P/\pi w_0^2$; longitud de interacción limitada a la longitud de difracción $b=2\pi w_0^2/\lambda$. Así $G=gIL=2gP/\lambda$
(independiente de $w_0$) e igualando a $G_{\rm th}$:
$$P_{\rm th}=\frac{G_{\rm th}\lambda}{2g}. \qquad\text{(9.3.38, p. 447)}$$
**Ejemplo**: $\lambda=1.06\ \mu$m, $G_{\rm th}=25$, $g=0.15$ cm/MW (CS₂) → $P_{\rm th}=9$ kW; para otros líquidos orgánicos ≈ 10 veces más.

#### 9.3.3 Transient and Dynamical Features of SBS (p. 447)

El tiempo de vida del fonón en líquidos es de varios ns, comparable a pulsos Q‑switched (y mayor que pulsos
mode‑locked): los experimentos de SBS suelen estar en **régimen transitorio** (Kroll 1965; Pohl *et al.* 1968; Pohl y Kaiser
1970). Solución transitoria (Carman *et al.* 1970; resumida por Zel'dovich *et al.* 1985):
$$I_S(L,T)\simeq\begin{cases}I_N\exp\left(-2\Gamma_BT+2\sqrt{2(gIL)(\Gamma_BT)}\right) & \Gamma_BT<gIL/2,\\ I_N\exp(gIL) & \Gamma_BT>gIL/2,\end{cases} \qquad\text{(9.3.39, p. 447)}$$
$I_N$ = entrada efectiva de ruido, $gIL$ = ganancia de paso simple, $\Gamma_B$ = tasa de amortiguamiento del fonón, $T$ = duración
del pulso. Exigiendo que la amplificación sea igual al umbral $e^{25}$:
$$gI_{\rm th}l=\begin{cases}(12.5+2\Gamma_BT)^2/2\Gamma_BT & \Gamma_BT<12.5,\\ 25 & \Gamma_BT>12.5\end{cases}\quad\text{(tal como está impreso; ver Erratas)} \qquad\text{(9.3.40)}$$
Fig. 9.3.6 (p. 448): $gI_{\rm th}L$ vs. $\Gamma_BT$ (0–12): diverge para pulsos cortos y tiende a 25. Incluso con pulsos de dos veces el tiempo
de vida del fonón, el umbral sube un factor ≈ 2.

Dinámica rica (tiempos de tránsito, duración del pulso, vida del fonón): **compresión de pulsos** (el pulso Stokes puede ser mucho
más corto que el láser; Problema 5); láseres multimodo longitudinal (batido de modos; Narum *et al.* 1986); propiedades
**estocásticas** (SBS iniciado por fonones térmicos, amplificación no lineal por agotamiento y respuesta efectivamente no local por la
contrapropagación; Gaeta y Boyd 1991); con dos bombeos contrapropagantes, **inestabilidad y caos** (Narum *et al.* 1988; Gaeta *et al.* 1989;
Kulagin *et al.* 1991).

### 9.4 Phase Conjugation by Stimulated Brillouin Scattering (p. 448)

Desde los primeros experimentos se vio que la Stokes salía muy colimada hacia atrás y se realimentaba en el láser (Goldblatt y
Hercher 1968), lo que se atribuyó inicialmente a la geometría larga y delgada. Primera evidencia de **conjugación de fase**:
Zel'dovich *et al.* (1972). Montaje (Fig. 9.4.1, p. 449): láser de rubí monomodo enfocado en una celda de metano a 125 atm con
forma de guía de onda cilíndrica multimodo; aberrador (placa de vidrio atacada con HF) en el haz incidente; cámaras 1 y 2 registran el
láser y el retorno Stokes. Fig. 9.4.2 (p. 450, fotos de V. V. Ragulsky): (a) láser (cámara 1) y (b) Stokes (cámara 2) con tamaños y formas
similares (alargadas por el patrón modal del láser) → el retorno es el conjugado de fase; (c) con un espejo convencional en lugar de la
celda, mancha mucho mayor (escala 2 mrad) → severidad de la aberración; (d) sin aberrador, mancha del retorno mayor que en (b): el
SBS conjuga mejor un haz muy distorsionado (nota: no es cierto en general; depende de la geometría del experimento).

¿Por qué? En FWM degenerado la fuente de $A_4$ es $\propto A_3^*$ (Ec. (7.2.31b)), pero en SBS (9.3.21b) $A_2$ es impulsado por $|A_1|^2A_2$, sin
información de la fase de $A_1$. Explicación (Zel'dovich *et al.* 1972; Sidorovich 1976; Fig. 9.4.3, p. 451): un frente muy aberrado enfocado
crea un patrón de **speckle volumétrico** → distribución de ganancia no uniforme. El ruido Stokes inicial contiene todas las componentes
de Fourier espaciales, pero la más amplificada es la que mejor coincide con la distribución de ganancia, es decir, la de frentes iguales a
los del láser: el conjugado de fase.

Formalización con (9.3.22b):
$$\frac{dI_S}{dz}=-gI_LI_S. \qquad\text{(9.4.1, p. 451)}$$
Potencias (a $z$ fijo):
$$P_L=\int I_L\,dA,\qquad P_S=\int I_S\,dA, \qquad\text{(9.4.2)}$$
$$\frac{dP_S}{dz}=-g\frac{P_LP_S}{A}C, \qquad\text{(9.4.3)}$$
$A=\int dA$ y la **correlación cruzada espacial normalizada**
$$C=\frac{\langle I_LI_S\rangle}{\langle I_L\rangle\langle I_S\rangle}, \qquad\text{(9.4.4, p. 451)}$$
con $\langle x\rangle=\int x\,dA/A$. $C=1$ si $I_L$ e $I_S$ no están correlacionadas o son uniformes; $C>1$ si están correlacionadas (p. ej. conjugadas).
Láser tan aberrado que la amplitud compleja sigue estadística gaussiana (Goodman 1985):
$$P(I)=\frac{1}{I_0}e^{-I/I_0}, \qquad\text{(9.4.5, p. 452)}$$
con momentos $\langle I^n\rangle=n!\langle I\rangle^n$ (el libro imprime "$n\langle I\rangle^n$"; ver *Erratas*), en particular
$$\langle I^2\rangle=2\langle I\rangle^2. \qquad\text{(9.4.6)}$$
Para la parte conjugada $I_S\propto I_L$ y $C=2$: la ganancia exponencial $G\equiv gP_LCL/A$ de esa parte es el doble que la de cualquier otro modo
del ruido. Con umbral $G\sim30$, en el umbral la parte conjugada es ≈ $e^{15}$ veces mayor que cualquier otra componente.

Condiciones para muchos speckles: irregularidades de escala $a$ difractan en un cono $\theta=\lambda/a$; el speckle cambia apreciablemente tras
$\Delta z$ con $\theta\Delta z=a$, es decir $\Delta z=a^2/\lambda$. Conjugación de alta calidad solo si la extensión transversal ≫ $a$ y la longitudinal ≫ $\Delta z$
(p. 453). También se degrada si las componentes de gran divergencia no se traslapan con la parte central intensa → por eso se usa la
geometría de **guía de onda** (Fig. 9.4.1). Aplicación: láseres de alta potencia, corrigiendo aberraciones (p. ej. por tensiones térmicas en el
medio de ganancia); Bowers *et al.* (1997) lo usan además para controlar la polarización de la salida.

### 9.5 Stimulated Brillouin Scattering in Gases (p. 453)

Ganancia de línea central estacionaria (9.3.24):
$$g_0=\frac{\gamma_e^2\omega^2}{\rho_0nvc^3\Gamma_B}, \qquad\text{(9.5.1, p. 453)}$$
con $\gamma_e$ de (8.3.12) y
$$\Gamma_B=(2\eta_s+\eta_d)q^2/\rho_0. \qquad\text{(9.5.2)}$$
Gas ideal (Loeb 1961): relación de Stokes $\eta_d=-\tfrac23\eta_s$ (Apéndice 9.6.1):
$$\Gamma_B=\tfrac43\eta_sq^2/\rho_0. \qquad\text{(9.5.3, p. 453)}$$
Teoría cinética:
$$\eta_s=\tfrac13Nm\bar vL, \qquad\text{(9.5.4, p. 454)}$$
($N$ densidad numérica, $m$ masa molecular, $\bar v=(8kT/\pi m)^{1/2}$ velocidad media, $L=(\sqrt2\pi d^2N)^{-1}$ recorrido libre medio, $d$ diámetro
molecular):
$$\eta_s=\frac{2}{3\pi^{3/2}}\frac{\sqrt{kTm}}{d^2}, \qquad\text{(9.5.5)}$$
independiente de $N$. Valor medido (y teórico) para N₂ en TPE: $\eta_s=1.8\times10^{-4}$ dina s/cm². Con (9.5.5) en (9.5.2) y $q=2n\omega/c$:
$$\Gamma_B=\frac{32}{9\pi^{3/2}}\frac{n^2\omega^2}{c^2}\frac{\sqrt{kT/m}}{d^2N}. \qquad\text{(9.5.6, p. 454)}$$
Para $\lambda=1.06\ \mu$m, N₂ en TPE: $\Gamma_B=2.77\times10^9$ rad/s, $\delta\nu$(FWHM) $=\Gamma_B/2\pi=440$ MHz. Velocidad del sonido $v=(\gamma kT/m)^{1/2}$, $\gamma=5/3$
(monoatómico) o $7/5$ (diatómico); $\gamma_e=\rho(\partial\epsilon/\partial\rho)$ con $\partial\epsilon/\partial\rho\approx(\epsilon-1)/\rho$. Combinando:
$$g_0=\frac{9\pi^{3/2}N^2m^2d^2(\partial\epsilon/\partial\rho)^2}{32\gamma^{1/2}n^3ckT}. \qquad\text{(9.5.7, p. 454)}$$
Numéricamente es más cómodo usar (9.5.1) con $\Gamma_B$ de (9.5.6). N₂ en TPE a 1.06 µm: $\omega=1.8\times10^{15}$ rad/s, $n=1.0003$, $v=330$ m/s,
$\gamma_e=n^2-1=6\times10^{-4}$, …, y se obtiene
$$g_0=0.038\ \frac{\text{m}}{\text{TW}}. \qquad\text{(9.5.8, p. 455)}$$
$g_0\propto N^2$: a 100 atm, N₂ tiene $g_0=0.38$ m/GW, comparable a líquidos orgánicos. Ventaja de los gases: la ganancia SBS escala como $N^2$ y la
Raman estimulada (proceso competidor) como $N$ (el libro remite a "Eqs. (9.3.19a), (9.3.19b), and (9.3.20)"; ver *Erratas*). Por encima de 10 atm el
SBS suele superar al SRS, y con gases nobles (sin modos vibracionales) se suprime el SRS por completo. Datos para 249 nm (KrF; Damzen y
Hutchinson 1983):

**Tabla 9.5.1** (p. 455) — gases comprimidos a 249 nm ($g_R$ = ganancia Raman estimulada hacia adelante, para comparar):

| Gas | $p$ (atm) | $g_0$ (m/GW) | $\tau$ (ns) | $\Omega_B/2\pi$ (GHz) | $g_R$ (m/GW) |
|---|---|---|---|---|---|
| SF₆ | 15.5 | $2.5\times10^{-1}$ | 1 | 0.9 | $3\times10^{-3}$ |
| SF₆ | 10 | $0.9\times10^{-1}$ | 0.6 | | $2\times10^{-3}$ |
| Xe | 39 | $4.4\times10^{-1}$ | 2 | 1.4 | 0 |
| Xe | 10 | $1.8\times10^{-2}$ | 0.4 | | |
| Ar | 10 | $1.5\times10^{-3}$ | 0.1 | 3 | 0 |
| N₂ | 10 | $1.7\times10^{-3}$ | 0.2 | 3 | $3\times10^{-4}$ |
| CH₄ | 10 | $8\times10^{-3}$ | 0.1 | 3 | $1\times10^{-2}$ |

### 9.6 General Theory of Stimulated Brillouin and Stimulated Rayleigh Scattering (p. 455)

Modelo que trata juntos SBS y dispersión Rayleigh estimulada (SRLS): ambos son dispersión por inhomogeneidades termodinámicas. Variables
independientes $T$ y $\rho$; acoplamiento electrostrictivo y absortivo → cuatro procesos (p. 456):
1. **SBS electrostrictivo**: ondas de sonido impulsadas por la interferencia láser–Stokes vía electrostricción.
2. **SBS térmico**: ondas de sonido impulsadas por absorción y termalización (variaciones de $T$ y por tanto de $\rho$).
3. **SRLS electrostrictivo**: fluctuaciones isobáricas de densidad impulsadas por electrostricción.
4. **SRLS térmico**: fluctuaciones isobáricas impulsadas por absorción óptica.

Las tres ecuaciones de la hidrodinámica (Hunt 1955; Kaiser y Maier 1972); subíndice $t$ = cantidad total:
continuidad
$$\frac{\partial\tilde\rho_t}{\partial t}+\tilde{\mathbf u}_t\cdot\nabla\tilde\rho_t+\tilde\rho_t\nabla\cdot\tilde{\mathbf u}_t=0, \qquad\text{(9.6.1, p. 456)}$$
transporte de momento (Navier–Stokes generalizada)
$$\tilde\rho_t\frac{\partial\tilde{\mathbf u}_t}{\partial t}+\tilde\rho_t(\tilde{\mathbf u}_t\cdot\nabla)\tilde{\mathbf u}_t=\tilde{\mathbf f}-\nabla\tilde p_t+(2\eta_s+\eta_d)\nabla(\nabla\cdot\tilde{\mathbf u}_t)-\eta_s\nabla\times(\nabla\times\tilde{\mathbf u}_t), \qquad\text{(9.6.2)}$$
con la fuerza electrostrictiva (cf. (9.3.12))
$$\tilde{\mathbf f}=-\tfrac12\epsilon_0\gamma_e\nabla\langle\tilde{\mathbf E}\cdot\tilde{\mathbf E}\rangle, \qquad\text{(9.6.3, p. 456)}$$
$$\gamma_e=\rho\frac{\partial\epsilon}{\partial\rho}. \qquad\text{(9.6.4, p. 457)}$$
$\eta_s$ = viscosidad de cizalla, $\eta_d$ = viscosidad de dilatación; si vale la relación de Stokes (p. ej. gas ideal)
$$\eta_d=-\tfrac23\eta_s. \qquad\text{(9.6.5)}$$
Transporte de calor:
$$\tilde\rho_tc_v\frac{\partial\tilde T_t}{\partial t}+\tilde\rho_tc_v(\tilde{\mathbf u}\cdot\nabla\tilde T_t)+\tilde\rho_tc_v\left(\frac{\gamma-1}{\beta_p}\right)(\nabla\cdot\tilde{\mathbf u}_t)=-\nabla\cdot\tilde{\mathbf Q}+\tilde\phi_\eta+\tilde\phi_{\rm ext}, \qquad\text{(9.6.6, p. 457)}$$
($c_v$ calor específico a volumen constante, $\gamma=c_p/c_v$, $\beta_p=-\tilde\rho^{-1}(\partial\tilde\rho/\partial\tilde T)_p$ coeficiente de expansión térmica, $\tilde{\mathbf Q}$ flujo de calor):
$$\nabla\cdot\tilde{\mathbf Q}=-\kappa\nabla^2\tilde T_t, \qquad\text{(9.6.7)}$$
$$\tilde\phi_\eta=\sum_{ij}(2\eta_sd_{ij}d_{ji}+\eta_dd_{ii}d_{jj}), \qquad\text{(9.6.8a)}\qquad d_{ij}=\frac12\left(\frac{\partial\tilde u_i}{\partial x_j}+\frac{\partial\tilde u_j}{\partial x_i}\right) \qquad\text{(9.6.8b)}$$
(energía viscosa depositada; tensor de tasa de dilatación), y la potencia externa por absorción óptica
$$\tilde\phi_{\rm ext}=\alpha n\epsilon_0c\langle\tilde E^2\rangle, \qquad\text{(9.6.9, p. 457)}$$
$\alpha$ = coeficiente de absorción óptica.

**Linealización** (p. 458):
$$\tilde\rho_t=\rho_0+\tilde\rho\ (|\tilde\rho|\ll\rho_0), \qquad\text{(9.6.10a)}\qquad \tilde T_t=T_0+\tilde T\ (|\tilde T|\ll T_0), \qquad\text{(9.6.10b)}\qquad \tilde{\mathbf u}_t=\tilde{\mathbf u}\ (|\tilde{\mathbf u}|\ll v), \qquad\text{(9.6.10c)}$$
(medio en reposo sin la perturbación acústica). Quitando términos de orden superior y la solución no perturbada:
$$\frac{\partial\tilde\rho}{\partial t}+\rho_0\nabla\cdot\tilde{\mathbf u}=0. \qquad\text{(9.6.11, p. 458)}$$
Presión $\tilde p_t=p_0+\tilde p$ ($|\tilde p|\ll p_0$) (9.6.12), con
$$\tilde p=\left(\frac{\partial p}{\partial\rho}\right)_T\tilde\rho+\left(\frac{\partial p}{\partial T}\right)_\rho\tilde T, \qquad\text{(9.6.13)}$$
$$\tilde p=\frac{v^2}{\gamma}(\tilde\rho+\beta_p\rho_0\tilde T), \qquad\text{(9.6.14)}$$
usando $(\partial p/\partial\rho)_T=\gamma^{-1}(\partial p/\partial\rho)_s=v^2/\gamma$ y $(\partial p/\partial T)_\rho=\gamma^{-1}(\partial p/\partial\rho)_s(\partial\rho/\partial T)_p=v^2\beta_p\rho_0/\gamma$ [así en el libro; la
expresión intermedia necesita un signo menos, $-(\partial p/\partial\rho)_T(\partial\rho/\partial T)_p$ por la regla cíclica, y entonces con $\beta_p=-\rho^{-1}(\partial\rho/\partial T)_p$ el
resultado final $+v^2\beta_p\rho_0/\gamma$ es correcto]. Momento linealizado:
$$\rho_0\frac{\partial\tilde{\mathbf u}}{\partial t}+\frac{v^2}{\gamma}\nabla\tilde\rho+\frac{v^2\beta_p\rho_0}{\gamma}\nabla\tilde T-(2\eta_s+\eta_d)\nabla(\nabla\cdot\tilde{\mathbf u})+\eta_s\nabla\times(\nabla\times\tilde{\mathbf u})=\tilde{\mathbf f}. \qquad\text{(9.6.15, p. 458)}$$
Energía linealizada ($\tilde\phi_\eta$ no contribuye en orden lineal):
$$\rho_0c_v\frac{\partial\tilde T}{\partial t}+\frac{\rho_0c_v(\gamma-1)}{\beta_p}(\nabla\cdot\tilde{\mathbf u})-\kappa\nabla^2\tilde T=\tilde\phi_{\rm ext}. \qquad\text{(9.6.16, p. 459)}$$
Divergencia de (9.6.15) y eliminación de $\nabla\cdot\tilde{\mathbf u}$ con (9.6.11):
$$-\frac{\partial^2\tilde\rho}{\partial t^2}+\frac{v^2}{\gamma}\nabla^2\tilde\rho+\frac{v^2\beta_p\rho_0}{\gamma}\nabla^2\tilde T+\frac{2\eta_s+\eta_d}{\rho_0}\frac{\partial}{\partial t}(\nabla^2\tilde\rho)=\tfrac12\epsilon_0\gamma_e\nabla^2\langle\tilde E^2\rangle, \qquad\text{(9.6.17, p. 459)}$$
$$\rho_0c_v\frac{\partial\tilde T}{\partial t}-\frac{c_v(\gamma-1)}{\beta_p}\frac{\partial\tilde\rho}{\partial t}-\kappa\nabla^2\tilde T=n\epsilon_0c\alpha\langle\tilde E^2\rangle. \qquad\text{(9.6.18)}$$
Dos ecuaciones acopladas para $\tilde\rho$, $\tilde T$ impulsadas por el campo. Sin fuentes admiten ondas acústicas amortiguadas
$$\tilde F(z,t)=Fe^{-i\Omega(t-z/v)}e^{-\alpha_sz}+\text{c.c.} \qquad\text{(9.6.19)}$$
($F=\rho$ o $T$), con, a bajas frecuencias ($\Omega\ll\rho_0v^2/(2\eta_s+\eta_d)$; Sette 1961),
$$\alpha_s=\frac{\Omega^2}{2\rho_0v^3}\left[(2\eta_s+\eta_d)+(\gamma-1)\frac{\kappa}{c_p}\right]. \qquad\text{(9.6.20, p. 459)}$$

**Respuesta forzada.** Campo total
$$\tilde E(z,t)=A_1e^{i(k_1z-\omega_1t)}+A_2e^{i(-k_2z-\omega_2t)}+\text{c.c.}, \qquad\text{(9.6.21, p. 460)}$$
perturbación a
$$\Omega=\omega_1-\omega_2, \qquad\text{(9.6.22)}\qquad q=k_1+k_2, \qquad\text{(9.6.23)}$$
$$\tilde\rho(z,t)=\rho e^{i(qz-\Omega t)}+\text{c.c.}, \qquad\text{(9.6.24)}\qquad \tilde T(z,t)=Te^{i(qz-\Omega t)}+\text{c.c.} \qquad\text{(9.6.25)}$$
En estado estacionario, las partes a frecuencia $\Omega$ de (9.6.17) y (9.6.18):
$$-\left(\Omega^2+i\Omega\Gamma_B-\frac{v^2q^2}{\gamma}\right)\rho+\frac{v^2\beta_p\rho_0q^2}{\gamma}T=\epsilon_0\gamma_eq^2A_1A_2^*, \qquad\text{(9.6.26, p. 460)}$$
$$-\left(i\Omega-\tfrac12\gamma\Gamma_R\right)T+\frac{i(\gamma-1)\Omega}{\beta_p\rho_0}\rho=\frac{2n\epsilon_0c\alpha}{c_v\rho_0}A_1A_2^*, \qquad\text{(9.6.27)}$$
con el ancho Brillouin y el ancho Rayleigh
$$\Gamma_B=(2\eta_s+\eta_d)q^2/\rho_0, \qquad\text{(9.6.28)}\qquad \Gamma_R=\frac{2\kappa q^2}{\rho_0c_p}, \qquad\text{(9.6.29, p. 460)}$$
($\tau_p=\Gamma_B^{-1}$ vida del fonón; $\tau_R=\Gamma_R^{-1}$ tiempo de decaimiento de las perturbaciones isobáricas). Se desprecian derivadas espaciales de $\rho$ y $T$
(excitaciones fuertemente amortiguadas), válido si (p. 461)
$$q\gg\left|\frac1\rho\frac{\partial\rho}{\partial z}\right|,\left|\frac1T\frac{\partial T}{\partial z}\right|\quad\text{y}\quad q^2\gg\left|\frac1\rho\frac{\partial^2\rho}{\partial z^2}\right|,\left|\frac1T\frac{\partial^2T}{\partial z^2}\right|$$
(misma aproximación que en (9.3.15)). Despejando $T$ de (9.6.27) y sustituyendo en (9.6.26):
$$\left[-\left(\Omega^2+i\Omega\Gamma_B-\frac{v^2q^2}{\gamma}\right)+\frac{v^2q^2\Omega(\gamma-1)}{(\Omega+\frac12i\gamma\Gamma_R)\gamma}\right]\rho=\left[\epsilon_0\gamma_e-\frac{i\gamma_aqv}{\Omega+\frac12i\gamma\Gamma_R}\right]q^2A_1A_2^*, \qquad\text{(9.6.30, p. 461)}$$
con la **constante de acoplamiento absortiva**
$$\gamma_a=\frac{8\pi\alpha nv^2\epsilon_0c\beta_p}{c_p\Omega_B}\quad\text{(impreso; ver Erratas)},\qquad \Omega_B=qv. \qquad\text{(9.6.31)}$$
Empíricamente los espectros Brillouin y Rayleigh no se traslapan (Fig. 8.1.1), así que se tratan por separado.

*SBS*: $\Omega^2\approx\Omega_B^2=v^2q^2$, el denominador $\Omega+\frac12i\gamma\Gamma_R$ no es resonante y se desprecia $\frac12i\gamma\Gamma_R$:
$$\rho_B=\frac{-(\epsilon_0\gamma_e-i\gamma_a)q^2}{4\pi(\Omega^2+i\Omega\Gamma_B-v^2q^2)}A_1A_2^*\quad\text{(impreso; ver Erratas)}. \qquad\text{(9.6.32, p. 461)}$$
*SRLS*: resonancia en $\Omega=0$; para $|\Omega|\lesssim\Gamma_R$ el denominador Brillouin se aproxima por $-v^2q^2/\gamma$:
$$\rho_R=\left[\frac{\epsilon_0\gamma_e(\Omega+\frac12i\gamma\Gamma_R)-i\gamma_a\Omega_B}{\Omega+\frac12i\Gamma_R}\right]\frac{1}{4\pi v^2}A_1A_2^*\quad\text{(impreso; ver Erratas)}. \qquad\text{(9.6.33, p. 461)}$$

**Polarización no lineal**:
$$\tilde p^{\rm NL}=\epsilon_0\Delta\chi\tilde E=\epsilon_0\Delta\epsilon\tilde E=\epsilon_0\left(\frac{\partial\epsilon}{\partial\rho}\right)_T\tilde\rho\tilde E=\frac{\epsilon_0\gamma_e}{\rho_0}\tilde\rho\tilde E, \qquad\text{(9.6.34, p. 462)}$$
$$\tilde P^{\rm NL}=p_1e^{i(k_1z-\omega_1t)}+p_2e^{i(-k_2z-\omega_2t)}+\text{c.c.}, \qquad\text{(9.6.35)}\qquad p_1=\frac{\epsilon_0\gamma_e}{\rho_0}\rho A_2,\quad p_2=\frac{\epsilon_0\gamma_e}{\rho_0}\rho^*A_1. \qquad\text{(9.6.36)}$$
Ecuación de onda (cf. (2.1.22)):
$$\nabla^2[A_n(\mathbf r)e^{i\mathbf k_n\cdot\mathbf r}]+\frac{\epsilon(\omega_n)\omega_n^2}{c^2}A_n(\mathbf r)e^{i\mathbf k_n\cdot\mathbf r}=-\frac{\omega_n^2}{\epsilon_0c^2}p_ne^{i\mathbf k_n\cdot\mathbf r}. \qquad\text{(9.6.37, p. 462)}$$
(El libro imprime el lado derecho sin el signo menos; con el signo de (2.1.22) se obtiene (9.6.38a); ver *Erratas*.)
Con SVEA, $n=\mathrm{Re}\sqrt\epsilon$ y $\alpha=(2\omega/c)\,\mathrm{Im}\sqrt\epsilon$:
$$\left(\frac{d}{dz}+\tfrac12\alpha\right)A_1=\frac{i\omega}{2n\epsilon_0c}p_1, \qquad\text{(9.6.38a)}\qquad \left(\frac{d}{dz}-\tfrac12\alpha\right)A_2=\frac{-i\omega}{2n\epsilon_0c}p_2. \qquad\text{(9.6.38b)}$$
Valen para SBS o SRLS según se use (9.6.32) o (9.6.33) (el libro dice "the expression (9.3.36) for the nonlinear polarization"; por contexto es
(9.6.34)–(9.6.36)). Como $\rho\propto A_1A_2^*$:
$$\frac{dA_1}{dz}=\kappa|A_2|^2A_1-\tfrac12\alpha A_1, \qquad\text{(9.6.39a)}\qquad \frac{dA_2}{dz}=\kappa^*|A_1|^2A_2+\tfrac12\alpha A_2, \qquad\text{(9.6.39b, p. 462)}$$
$$\kappa_B=-\frac{q^2\omega}{2\rho_0nc}\frac{i\gamma_e(\epsilon_0\gamma_e-i\gamma_a)}{(\Omega^2+i\Omega\Gamma_B-v^2q^2)}, \qquad\text{(9.6.40a)}$$
$$\kappa_R=\frac{i\gamma_e\omega}{2\rho_0ncv^2}\left[\frac{\gamma_e(\Omega+\frac12i\gamma\Gamma_R)-i\gamma_a\Omega_B}{\Omega+\frac12i\Gamma_R}\right]. \qquad\text{(9.6.40b, p. 463)}$$
Intensidades
$$I_i=2n\epsilon_0c|A_i|^2, \qquad\text{(9.6.41)}$$
$$\frac{dI_1}{dz}=-gI_1I_2-\alpha I_1, \qquad\text{(9.6.42a)}\qquad \frac{dI_2}{dz}=-gI_1I_2+\alpha I_2, \qquad\text{(9.6.42b)}$$
$$g=-\frac{1}{n\epsilon_0c}\mathrm{Re}\,\kappa. \qquad\text{(9.6.43, p. 463)}$$

**Ganancia SBS**:
$$g_B=g_B^e+g_B^a, \qquad\text{(9.6.44a)}$$
$$g_B^e=\frac{\omega^2\gamma_e^2}{\rho_0nvc^2\Gamma_B}\frac{1}{1+(2\Delta\Omega/\Gamma_B)^2}, \qquad\text{(9.6.44b)}\qquad g_B^a=\frac{-\omega^2\gamma_e\gamma_a}{2\rho_0nvc^2\Gamma_B}\frac{4\Delta\Omega/\Gamma_B}{1+(2\Delta\Omega/\Gamma_B)^2} \qquad\text{(9.6.44c)}$$
(impresas con $c^2$; deben llevar $c^3$, ver *Erratas*), con $\Delta\Omega=\Omega_B-\Omega$, $\Omega_B=qv=(k_1+k_2)v$, $\Omega=\omega_1-\omega_2$. Máximo electrostrictivo en $\Delta\Omega=0$:
$$g_B^e(\max)=\frac{\omega^2\gamma_e^2}{\rho_0nvc^3\Gamma_B} \qquad\text{(9.6.45, p. 463)}$$
(independiente de $\omega$ porque $\Gamma_B\propto q^2\propto\omega^2$; es el $g_0$ de la Tabla 9.3.1). Máximo absortivo en $\Delta\Omega=-\Gamma_B/2$ (Stokes desplazada medio
ancho hacia el lado de baja frecuencia de la resonancia):
$$g_B^a(\max)=\frac{\omega^2\gamma_e\gamma_a}{2\rho_0nvc^3\Gamma_B}. \qquad\text{(9.6.46, p. 464)}$$
El libro afirma que, como $\Gamma_B\propto q^2$ y $\gamma_a\propto q^{-1}$, $g_B^a$ es "proporcional a $q^3$" y varía como $\omega^{-3}$ (ver *Erratas*: con (9.6.31) y (9.6.46) resulta $\omega^{-1}$). $g_B^a\propto\alpha$: añadiendo un absorbente
(colorante) el SBS térmico supera al electrostrictivo, aproximadamente para $\alpha>1$ cm⁻¹ (Tabla 9.3.1).

Fig. 9.6.1 (p. 465): arriba, espectro espontáneo (Rayleigh en $\omega_L$ de ancho $\Gamma_R$; Brillouin a $\pm\Omega_B$ de ancho $\Gamma_B$); en medio, ganancia electrostrictiva
$g^e$: pico positivo en el Stokes Brillouin, curva dispersiva en $\omega_L$ (ganancia del lado Stokes, pérdida del lado anti‑Stokes) y pico negativo en el
anti‑Stokes; abajo, ganancia absortiva $g^a$: dispersiva en cada resonancia, con signo opuesto en el centro (ganancia anti‑Stokes).

**Ganancia SRLS** (de (9.6.40b) y (9.6.43)):
$$g_R=g_R^e+g_R^a, \qquad\text{(9.6.47, p. 464)}$$
$$g_R^e=\frac{-\omega\gamma_e^2(\gamma-1)}{4\rho_0n^2c^2v^2}\left[\frac{4\Omega/\Gamma_R}{1+(2\Omega/\Gamma_R)^2}\right], \qquad\text{(9.6.48)}\qquad
g_R^a=\frac{\omega\gamma_e\gamma_a\Omega_B}{2\rho_0n^2c^2v^2\Gamma_R}\left[\frac{4\Omega/\Gamma_R}{1+(2\Omega/\Gamma_R)^2}\right]. \qquad\text{(9.6.49)}$$
SRLS electrostrictivo: máximo en $\Omega=-\Gamma_R/2$,
$$g_R^e(\max)=\frac{\omega\gamma_e^2(\gamma-1)}{4\rho_0n^2c^2v^2}, \qquad\text{(9.6.50, p. 464)}$$
lineal en la frecuencia del láser. SRLS térmico: máximo en $\Omega=\Gamma_R/2$,
$$g_R^a(\max)=\frac{\omega\gamma_e\gamma_a\Omega_B}{2\rho_0n^2c^2v^2\Gamma_R}; \qquad\text{(9.6.51, p. 465)}$$
como $\Gamma_R\propto\omega^2$, $\gamma_a\propto1/\omega$, $\Omega_B\propto\omega$, escala como $1/\omega$. $\Gamma_R$ ~ 10 MHz (Tabla 9.6.1), mucho menor que el ancho de láseres pulsados:
se convoluciona la ganancia con el perfil del láser; si $\Gamma_L\gg\Gamma_R$, el máximo de SRLS absortivo es (9.6.51) con $\Gamma_R\to\Gamma_L$, independiente de la
frecuencia del láser.

**Tabla 9.6.1** (p. 466) — SRLS a 694 nm (Kaiser y Maier 1972):

| Sustancia | $g_e(\max)$ (cm/MW) | $g_a(\max)/\alpha$ (cm²/MW) | $\delta\nu_R$ (MHz) |
|---|---|---|---|
| CCl₄ | $2.6\times10^{-4}$ | 0.82 | 17 |
| Metanol | $8.4\times10^{-4}$ | 0.32 | 20 |
| CS₂ | $6.0\times10^{-4}$ | 0.62 | 36 |
| Benceno | $2.2\times10^{-4}$ | 0.57 | 24 |
| Acetona | $2.0\times10^{-4}$ | 0.47 | 21 |
| H₂O | $0.02\times10^{-4}$ | 0.019 | 27.5 |
| Etanol | — | 0.38 | 18 |

$g_R^a(\max)\gg g_R^e(\max)$ salvo para absorción extremadamente pequeña; se igualan para $\alpha\simeq10^{-3}$ cm⁻¹ (solo materiales muy puros). Cociente de las
ganancias térmicas:
$$\frac{g_R^a(\max)}{g_B^a(\max)}=\frac{2\Gamma_B}{\Gamma_R}; \qquad\text{(9.6.52, p. 466)}$$
$\Gamma_B/\Gamma_R\sim100$ típicamente → cuando hay dispersión estimulada térmica domina el SRLS térmico. **El SRLS electrostrictivo da ganancia al Stokes y el
térmico al anti‑Stokes** (Herman y Gray 1967): $n_2>0$ para electrostricción y $n_2<0$ para calentamiento/expansión térmica, y en el acoplamiento
de dos haces (§7.4) la onda de menor frecuencia gana si $n_2>0$ y pierde si $n_2<0$.

#### 9.6.1 Appendix: Definition of the Viscosity Coefficients (p. 466)

Tensor de esfuerzos ($t_{ij}$ = componente $i$ de la fuerza por unidad de área sobre un elemento de normal $j$):
$t_{ij}=-p\delta_{ij}+\sigma_{ij}$, con $\sigma_{ij}$ la contribución viscosa. Si $\sigma_{ij}$ es lineal en la tasa de deformación $d_{ij}=\frac12[\partial\tilde u_i/\partial x_j+\partial\tilde u_j/\partial x_i]$:
$$\sigma_{ij}=2\eta_sd_{ij}+\eta_d\delta_{ij}\sum_kd_{kk},\qquad \sum_kd_{kk}=\sum_k\frac{\partial\tilde u_k}{\partial x_k}=\nabla\cdot\tilde{\mathbf u}$$
($\eta_s$ cizalla, $\eta_d$ dilatación; en general independientes). **Relación de Stokes**: si $\sigma_{ij}$ tiene traza nula (la presión media $-\frac13\sum_it_{ii}$ no se
ve afectada por la viscosidad), $\sum_i\sigma_{ii}=(2\eta_s+3\eta_d)\sum_kd_{kk}=0$, de donde $\eta_d=-\frac23\eta_s$, y $2\eta_s+\eta_d=\frac43\eta_s$. En general se define la viscosidad
volumétrica $\eta_b=\frac23\eta_s+\eta_d$, con lo que $2\eta_s+\eta_d=\frac43\eta_s+\eta_b$; $\eta_b=0$ si vale Stokes (gas ideal). Así, ignorando la conducción térmica (p. 468):
$$\Gamma_B=(2\eta_s+\eta_d)q^2/\rho_0=\left(\tfrac43\eta_s+\eta_b\right)q^2/\rho_0,$$
consistente con (8.3.23), (9.5.2) y (9.6.28).

---

## Tablas y datos numéricos útiles

- **Tabla 9.3.1** (p. 441): SBS a 694 nm — $\Omega_B/2\pi$, $\Gamma_B/2\pi$, $g_0$, $g_B^a(\max)/\alpha$ para 12 medios (arriba). Escalado con la frecuencia:
  $\Omega_B\propto\omega$, $\Gamma_B\propto\omega^2$, $g_0$ independiente, $g_B^a\propto\omega^{-3}$. Destacan CS₂ (5850 MHz, 52.3 MHz, 1.5 m/GW), H₂O (5690, 317, 0.048)
  y SiO₂ (25 800 MHz, 78 MHz, 0.045 m/GW).
- **Tabla 9.5.1** (p. 455): SBS en gases comprimidos a 249 nm (SF₆, Xe, Ar, N₂, CH₄), con $g_R$ de Raman para comparar.
- **Tabla 9.6.1** (p. 466): SRLS a 694 nm — $g_e(\max)$ ~ $10^{-4}$ cm/MW, $g_a(\max)/\alpha$ ~ 0.02–0.8 cm²/MW, $\delta\nu_R$ ≈ 17–36 MHz.
- Electrostricción: $\chi^{(3)}\sim3\times10^{-21}$ m²/V² (materia condensada, $C_T\approx10^{-9}$ m²/N), $\sim1\times10^{-23}$ m²/V² (gases a 1 atm,
  $\gamma_e\approx6\times10^{-4}$); ≈ 20 % del $\chi^{(3)}$ en fibras (p. 435).
- CS₂ a 1 µm: $g_0=1.5$ m/GW $=0.15$ cm/MW ($n=1.67$, $v=1.1\times10^3$ m/s, $\rho_0=1.26\times10^3$ kg/m³, $\gamma_e=2.4$, $\tau_p=4$ ns) (p. 441).
- Umbral del generador: $G_{\rm th}\approx25$–30, $R_{\rm th}=0.01$, $f\approx10^{-12}$–$10^{-11}$ (p. 444); $P_{\rm th}=9$ kW en CS₂ a 1.06 µm con enfoque
  óptimo (p. 447).
- N₂ en TPE a 1.06 µm: $\eta_s=1.8\times10^{-4}$ dina s/cm², $\Gamma_B=2.77\times10^9$ rad/s ($\Gamma_B/2\pi=440$ MHz), $g_0=0.038$ m/TW; a 100 atm,
  0.38 m/GW (pp. 454–455).
- Fonones hipersónicos: $\Gamma_B\approx1.6\times10^8$ s⁻¹, $\alpha_s^{-1}\approx6.3\ \mu$m (nota p. 439).
- $\Gamma_B/\Gamma_R\sim100$; SRLS electrostrictivo ≈ absortivo para $\alpha\simeq10^{-3}$ cm⁻¹ (p. 466).

---

## Problemas (pp. 468–470)

1. *Lorentz–Lorenz prediction of the electrostrictive constant.* Verificar la Ec. (9.2.17).
2. *Angular dependence of SBS.* Generalizar la discusión de §9.3 para un ángulo $\theta$ arbitrario entre las direcciones de propagación del
   láser y de la Stokes. En particular, determinar cómo dependen de $\theta$ la frecuencia Brillouin $\Omega_B$, la ganancia de línea central
   estacionaria $g_0$ y el tiempo de vida del fonón $\tau_p$. [Resp.: $\Omega_B(\theta)=\Omega_B(\theta=180°)\sin(\tfrac12\theta)$;
   $g_0(\theta)=g_0(\theta=180°)/\sin(\tfrac12\theta)$; $\tau_p(\theta)=\tau_p(\theta=180°)/\sin^2(\tfrac12\theta)$.]
3. *Transverse SBS.* Considerar la posibilidad de excitar SBS en la dirección transversal con un haz láser que atraviesa una ventana de sílice
   fundida a incidencia casi normal, en condiciones de láser de alta energía: ventana de 70 cm de diámetro, llenada uniformemente por un pulso
   de 10 ns a 350 nm. ¿Cuál es la mínima energía del pulso con la que puede excitarse SBS? (Se ha observado SBS transversal en condiciones
   similares; ver Murray *et al.*, 1989.) [Resp.: ~2 kJ.]
4. *Optical damage considerations and the study of SBS.* El umbral de daño óptico de la sílice fundida es ≈ 3 GW/cm², del mismo orden para la
   mayoría de los materiales ópticos (Lowdermilk y Milam, 1981). Con este dato y la ganancia de línea central de la Tabla 9.3.1, determinar la
   longitud mínima de una celda con ventanas de sílice fundida que permita excitar SBS en acetona con un haz colimado, suponiendo que la
   intensidad se limita al 50 % del umbral de daño como factor de seguridad. Si el pulso dura 20 ns, ¿cuál es la mínima energía por unidad de
   área del pulso que puede excitar SBS? (Por eso el SBS suele excitarse con haces fuertemente enfocados y no colimados, para no dañar las
   ventanas.)
5. *Pulse compression by SBS.* Explicar cualitativamente por qué la radiación Stokes excitada por SBS hacia atrás puede ser considerablemente
   más corta que la radiación excitadora. ¿Cómo debe relacionarse la longitud física de la región de interacción con la duración del pulso láser
   para observar el efecto? Escribir las ecuaciones de amplitudes acopladas necesarias y, si se desea, resolverlas numéricamente. ¿Qué determina
   la duración mínima del pulso de salida? [Pista: Hon (1980) y Gulidov *et al.* (1988).]
6. *Brillouin-enhanced four-wave mixing (BEFWM).* Además del SBS, los haces pueden interactuar en un medio Brillouin por mezcla de cuatro ondas
   reforzada por Brillouin (figura: bombeo $A_1$ a $\omega$ hacia adelante; bombeo $A_2$ a $\omega-2\Omega$ hacia atrás; señal $A_3$ a $\omega-\Omega$ entrante y
   conjugada $A_4$ a $\omega-\Omega$ saliente). La señal $A_3$ interfiere con el bombeo contrapropagante $A_2$ y genera una onda acústica que viaja hacia
   adelante; el bombeo $A_1$ se dispersa en ella generando la onda conjugada $A_4$, que por estar en la banda Stokes de $A_1$ también se amplifica por
   SBS ordinario. Se han observado reflectividades conjugadas muy superiores al 100 %. Con el formalismo de §9.3, deducir las cuatro ecuaciones de
   amplitudes acopladas del BEFWM en estado estacionario y resolverlas analíticamente con bombeo constante. [Pista: Skeldon *et al.* (1987).]

## Referencias principales (pp. 470–471)

Revisiones: Kaiser y Maier (1972) en *Laser Handbook*; Zel'dovich, Pilipetsky y Shkunov (1985) *Principles of Phase Conjugation*.
Lecturas: Fabelinskii (1968, 1975); Fisher (1983) *Optical Phase Conjugation* (caps. 6–7); Shen (1984) *Principles of Nonlinear Optics*.
SBS: Chiao, Townes y Stoicheff (1964) PRL 12, 592 (primera observación); Buckland y Boyd (1996) OL 21, 1117 y (1997) OL 22, 676
(electrostricción en fibras); Boyd, Rzążewski y Narum (1990) PRA 42, 5514 (umbral desde ruido térmico); Carman *et al.* (1970) PRA 2, 60
(transitorio); Damzen y Hutchinson (1983) IEEE JQE 19, 7; Gaeta y Boyd (1991) PRA 44, 3205 (estocástico); Zel'dovich *et al.* (1972) JETP Lett.
15, 109 (conjugación de fase); Herman y Gray (1967) PRL 19, 824 (SRLS térmico anti‑Stokes); Kroll (1965), Kroll y Kelley (1971); Hunt (1955);
Loeb (1961); Sette (1961); Murray *et al.* (1989); Skeldon, Narum y Boyd (1987) OL 12, 1211; Bowers, Boyd y Hankla (1997) OL 22, 360.

---

## Relación con el curso y con el proyecto final

- **Curso (tema 6: Boyd 4.1, 4.2, 7.1, 7.2).** La electrostricción de §9.2 es uno de los mecanismos de $n_2$ que lista Boyd §4.1 (Tabla 4.1.1):
  $\chi^{(3)}=\frac13\epsilon_0C_T\gamma_e^2$ con $n_2=(3/4n_0^2\epsilon_0c)\chi^{(3)}$ (4.1.19), de respuesta lenta (~ns, tiempo de tránsito acústico) y nula para
  pulsos ultracortos; en la notación de Maker–Terhune $A=C_T\gamma_e^2$, $B=0$ (4.2.10). La conjugación de fase por SBS (§9.4) contrasta con la de
  FWM degenerado (§7.2, Ec. (7.2.31b)). El signo de la ganancia SRLS se relaciona con el acoplamiento de dos haces (§7.4).
- **Proyecto final (SC en guías de SiN/Si).** (i) El SBS tiene la mayor ganancia de los procesos estimulados (Tabla 8.1.1) pero ancho de
  banda estrecho (decenas de MHz): para el supercontinuo con pulsos de fs–ps, $\Gamma_BT\ll1$ y por (9.3.39)–(9.3.40) el SBS queda fuertemente
  suprimido; sí importa para bombeo CW o de ns (p. ej. microcombs/anillos bombeados en CW). (ii) Los datos de SiO₂ ($\Omega_B/2\pi=25.8$ GHz a
  694 nm, $g_0=0.045$ m/GW) escalan a 1.55 µm como $\Omega_B/2\pi\approx11.6$ GHz (cálculo propio con $\Omega_B\propto\omega$, no del libro), escala típica
  del revestimiento de SiO₂ de las guías. (iii) La contribución electrostrictiva a $n_2$ (≈ 20 % en fibras) recuerda que el $n_2$ medido con pulsos
  largos puede diferir del medido con pulsos cortos; al tomar $n_2$ de SiN/Si de la literatura conviene revisar la duración de pulso usada.
  (iv) En guías integradas la ganancia Brillouin depende además del confinamiento acústico (no tratado en el libro, que solo cubre medios
  volumétricos).
- **Proyecto (anillo sensor de volumen).** No hay relación directa; la dispersión Rayleigh estimulada térmica es relevante solo con
  analitos absorbentes y potencias altas.

---

## Erratas o dudas de lectura

1. **(9.2.14), p. 434.** Se lee $\mathbf P=\Delta\chi\mathbf E=\epsilon_0C_T\gamma_e^2|\mathbf E|^2\mathbf E$. Para que (9.2.15) dé (9.2.16), $\chi^{(3)}=\frac13\epsilon_0C_T\gamma_e^2$ (que es
   dimensionalmente correcto, m²/V²), debe ser $\mathbf P=\epsilon_0\Delta\chi\mathbf E=\epsilon_0^2C_T\gamma_e^2|\mathbf E|^2\mathbf E$ (falta un $\epsilon_0$).
2. **(9.3.18), p. 439.** $\tilde P_2$ impreso con $e^{i(k_2z-\omega_2t)}$; como $\tilde E_2\propto e^{i(-k_2z-\omega_2t)}$ (9.3.9b) y $\rho^*A_1e^{i[(k_1-q)z-\omega_2t]}$ con $q=2k_1$,
   debería ser $e^{i(-k_2z-\omega_2t)}$ (como en (9.6.35)).
3. **Nota al pie p. 439.** Con $\eta_s=10^{-9}$ "N m/s²" y $\rho_0=10$ kg/m³, $\eta_sq^2/\rho_0\approx1.6\times10^4$ s⁻¹, no $1.6\times10^8$. El resultado $\Gamma_B=1.6\times10^8$ s⁻¹ (y
   $\alpha_s^{-1}=v/\Gamma_B=6.3\ \mu$m) corresponde a $\eta_s/\rho_0=10^{-6}$ m²/s, p. ej. $\eta_s=10^{-3}$ N s/m² y $\rho_0=10^3$ kg/m³ (valores del agua). Los datos impresos
   tienen errores de exponente y de unidades.
4. **p. 441 (anti‑Stokes).** Se lee "identifying $\omega_1$ with $\omega_{aS}$ and $\omega_2$ with $\omega_S$"; según la nota de la p. 436 y la física ($\omega_{aS}-\omega_L=\Omega_B$),
   debería ser $\omega_2\to\omega_L$.
5. **(9.3.40), p. 447.** Se lee $gI_{\rm th}l=(12.5+2\Gamma_BT)^2/2\Gamma_BT$. Igualando el exponente de (9.3.39) a 25,
   $2\sqrt{2x\Gamma_BT}=25+2\Gamma_BT$ ⇒ $x=(12.5+\Gamma_BT)^2/(2\Gamma_BT)$. Con esta forma la curva es continua en $\Gamma_BT=12.5$ ($x=25$) y en $\Gamma_BT=2$
   da $x\approx52.6\approx2\times25$, como dice el texto; la forma impresa da 56 en $\Gamma_BT=12.5$ (discontinua) y 68 en $\Gamma_BT=2$. Además "$l$" debería
   ser $L$.
6. **p. 446.** "the distributions of the intensities ... can be obtained from Eqs. (9.3.20)": por contexto (estado estacionario con $I_2(0)$
   conocido) debería ser (9.3.30).
7. **p. 452.** Se lee $\langle I^n\rangle=n\langle I\rangle^n$; para la distribución exponencial (9.4.5) es $\langle I^n\rangle=n!\langle I\rangle^n$ (coincide para $n=2$, (9.4.6)).
8. **p. 455.** Remite a "Eqs. (9.3.19a), (9.3.19b), and (9.3.20)" para la ganancia Raman $\propto N$; esas ecuaciones del cap. 9 no tratan Raman
   (y (9.3.19) no tiene partes a/b). Probablemente se refiere a ecuaciones del cap. 10.
9. **Signo de la fuerza electrostrictiva, (9.3.12) y (9.6.3).** En §9.3 se define $\mathbf f=\nabla p_{\rm st}$ y en (9.6.3) $\tilde{\mathbf f}=-\frac12\epsilon_0\gamma_e\nabla\langle\tilde E^2\rangle$, que apunta
   hacia campo *decreciente*, al contrario que (9.2.3). En (9.6.2) $\tilde{\mathbf f}$ entra como fuerza física; tomando la divergencia con (9.6.11), el
   resultado (9.6.17) con lado derecho $+\frac12\epsilon_0\gamma_e\nabla^2\langle\tilde E^2\rangle$ requiere $\tilde{\mathbf f}=+\frac12\epsilon_0\gamma_e\nabla\langle\tilde E^2\rangle$ (física de §9.2). Así,
   (9.6.17) es correcto y (9.6.3) tiene el signo cambiado. En §9.3 el signo se compensa porque se usa directamente $\nabla\cdot\mathbf f=\nabla^2p_{\rm st}$ como
   fuente.
10. **(9.6.31)–(9.6.33), p. 461: factores $4\pi$ y $8\pi$ (probables restos de unidades gaussianas).** Despejando $T$ de (9.6.27) y sustituyendo
    en (9.6.26) tal como están impresas, se obtiene $\gamma_a=2\alpha nv^2\epsilon_0c\beta_p/(c_p\Omega_B)$ (en lugar de $8\pi\dots$),
    $\rho_B=-(\epsilon_0\gamma_e-i\gamma_a)q^2A_1A_2^*/(\Omega^2+i\Omega\Gamma_B-v^2q^2)$ y $\rho_R=[\dots]A_1A_2^*/v^2$ (sin el $4\pi$). Las expresiones posteriores
    (9.6.40a,b) corresponden a $\rho_B$, $\rho_R$ **sin** el $4\pi$, lo que confirma la errata.
11. **(9.6.37), p. 462.** El lado derecho está impreso sin signo menos; con la forma de (2.1.22), $-(\omega_n^2/\epsilon_0c^2)p_n$, se obtienen los signos de
    (9.6.38a,b). También en p. 462: "the expression (9.3.36) for the nonlinear polarization" debería ser (9.6.34)–(9.6.36).
12. **(9.6.40b), p. 463.** Dentro del corchete se lee $\gamma_e(\Omega+\frac12i\gamma\Gamma_R)$; por (9.6.33) y por coherencia con (9.6.40a) debería ser $\epsilon_0\gamma_e(\dots)$.
13. **(9.6.44b,c), p. 463.** Impresas con $c^2$ en el denominador; deben llevar $c^3$. Verificado con $g=-\mathrm{Re}\,\kappa_B/(n\epsilon_0c)$, $q=2n\omega/c$,
    $\Omega_B=qv$: $g_B^e=\omega^2\gamma_e^2/[\rho_0nvc^3\Gamma_B(1+(2\Delta\Omega/\Gamma_B)^2)]$, coherente con (9.3.24), (9.6.45) y (9.6.46).
14. **p. 464 y nota de la Tabla 9.3.1: escalamiento de $g_B^a$.** Se lee que $g_B^a$ es "proporcional a $q^3$" y que depende de la frecuencia como
    $\omega^{-3}$. Con las propias fórmulas del libro, $\gamma_a\propto1/\Omega_B\propto\omega^{-1}$ (9.6.31) y $\Gamma_B\propto\omega^2$, de modo que
    $g_B^a(\max)\propto\omega^2\gamma_a/\Gamma_B\propto\omega^{-1}$ (9.6.46). Esto coincide con el $1/\omega$ que el libro sí da para $g_R^a$ (9.6.51) y con que el cociente
    (9.6.52), $2\Gamma_B/\Gamma_R$, no depende de la frecuencia. Así que, dentro del libro, $g_B^a\propto\omega^{-1}$; el "$q^3$" y el "$\omega^{-3}$" no se reproducen.
    Queda como duda (puede haber una dependencia adicional, p. ej. de $\alpha(\omega)$, que el libro no explica).
15. **Apéndice 9.6.1, p. 467.** En $d_{ij}$ el segundo término está impreso $\partial\tilde u_j/\partial x_j$; debe ser $\partial\tilde u_j/\partial x_i$ (como en (9.6.8b)). P. 468: "$\eta_B$
    vanishes" debería ser $\eta_b$.
16. **(9.6.14), p. 458.** La expresión intermedia $(\partial p/\partial T)_\rho=\gamma^{-1}(\partial p/\partial\rho)_s(\partial\rho/\partial T)_p$ omite el signo menos de la regla cíclica; el resultado
    $+v^2\beta_p\rho_0/\gamma$ es correcto con $\beta_p=-\rho^{-1}(\partial\rho/\partial T)_p$.
