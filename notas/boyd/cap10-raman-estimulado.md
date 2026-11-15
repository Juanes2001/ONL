# Capítulo 10 — Stimulated Raman Scattering and Stimulated Rayleigh-Wing Scattering (Boyd, 3.ª ed.)

Páginas del libro 473–509 (PDF 491–527). Leído el 2026-11-14.

Fuente: R. W. Boyd, *Nonlinear Optics*, 3.ª ed., Academic Press (Elsevier), 2008, cap. 10.
Las citas de página son páginas del libro (sumar 18 para la página del PDF). La p. 472 está en
blanco (fin del cap. 9); el cap. 11 empieza en la p. 511.

**Convención del libro (SI).** $\tilde E(t)=E e^{-i\omega t}+\text{c.c.}$, $\tilde P(t)=\epsilon_0[\chi^{(1)}\tilde E+\chi^{(2)}\tilde E^2+\chi^{(3)}\tilde E^3+\cdots]$,
$I=2n\epsilon_0 c|E|^2$. En este capítulo las ondas se escriben como $A_j e^{i(k_jz-\omega_j t)}+\text{c.c.}$ y
la susceptibilidad Raman $\chi_R(\omega_S)$ es una abreviatura de $\chi^{(3)}(\omega_S=\omega_S+\omega_L-\omega_L)$.
Tratamiento escalar en todo el capítulo (salvo §10.6.1).

> **Lo esencial.** (i) Argumento de Hellwarth: tasa $\propto m_L(m_S+1)$, que da el régimen espontáneo
> (lineal en $z$) y el estimulado (exponencial, $G=Dm_L/(c/n)$); relación ganancia ↔ sección eficaz
> espontánea (10.2.19). (ii) Modelo clásico: polarizabilidad modulada por la coordenada vibracional,
> $\chi_R(\omega_S)$ lorentziana con parte imaginaria **negativa** en $\omega_S=\omega_L-\omega_v$ → ganancia
> Stokes con ajuste de fase automático; $\chi_R(\omega_a)=\chi_R(\omega_S)^*$ → atenuación anti-Stokes.
> (iii) Término de mezcla de cuatro ondas $\chi_F=2\chi_R$ acopla Stokes y anti-Stokes; con $\Delta k=0$ la
> ganancia acoplada se anula (supresión de ganancia). (iv) CARS: $\omega_a=2\omega_1-\omega_2$, fondo no
> resonante distorsiona la línea. (v) Rayleigh-wing: reorientación molecular con tiempo $\tau$ (ec. de
> Debye), ganancia máxima en $\Omega=1/\tau$.

---

## Resumen del capítulo

El capítulo trata la dispersión Raman estimulada (SRS) y la dispersión Rayleigh-wing estimulada
(SRWS), dos procesos de dispersión de luz estimulada en los que la excitación del material es,
respectivamente, una vibración molecular (o rotación) y la orientación de moléculas anisótropas.
Parte del efecto Raman espontáneo (Stokes y anti-Stokes, reglas de selección por paridad) y, con
el argumento de números de ocupación de Hellwarth, muestra que espontáneo y estimulado son dos
límites de la misma ecuación $dm_S/dz\propto m_L(m_S+1)$; de ahí obtiene la relación entre el
coeficiente de ganancia Raman $G$ y la sección eficaz diferencial espectral del proceso espontáneo,
con una tabla de parámetros (desplazamiento, ancho de línea, sección eficaz, $G/I_L$) para líquidos,
cristales y gases. Luego desarrolla el modelo clásico de Garmire *et al.*: la molécula es un
oscilador armónico amortiguado cuya polarizabilidad depende linealmente de la coordenada
internuclear; el batido de los campos láser y Stokes impulsa la vibración y la vibración modula el
índice, lo que produce la polarización no lineal Stokes $P(\omega_S)=6\epsilon_0\chi_R|A_L|^2A_S$, con
$\chi_R$ lorentziana cuya parte imaginaria negativa en resonancia da ganancia exponencial y ajuste
de fase automático (proceso de "ganancia pura"). La misma teoría predice atenuación para la onda
anti-Stokes, pero el término de mezcla de cuatro ondas $\chi_F=2\chi_R$ acopla las dos bandas: se
resuelve en general el sistema acoplado de dos ondas (valores propios $g_\pm$, modos propios,
soluciones con condiciones en $z=0$), se comprueban límites (medio sin pérdidas ni dispersión; medio
lineal) y se aplica a SRS, con el resultado notable de que con ajuste de fase perfecto la ganancia
acoplada se anula y la vibración molecular se extingue. Sigue una descripción de CARS (y CSRS) como
herramienta espectroscópica, con su línea distorsionada por el fondo no resonante. Por último, la
SRWS: la polarizabilidad no lineal de orientación obedece una ecuación de relajación tipo Debye con
tiempo $\tau$; la respuesta desfasada respecto al patrón de interferencia produce una ganancia
$g_{RW}=g_{RW}^{(\max)}\,2\Omega\tau/(1+\Omega^2\tau^2)$, y se resumen las propiedades de polarización
(Chiao y Godine), incluida la conjugación vectorial aproximada.

---

## Secciones

### 10.1 The Spontaneous Raman Effect (p. 473)

Descubierto por C. V. Raman en 1928. Un haz ilumina una muestra (sólido, líquido o gas) y la luz
dispersada se analiza espectroscópicamente (Fig. 10.1.1): contiene frecuencias nuevas, las
**Stokes** (desplazadas a frecuencias menores, $\omega_S$) y las **anti-Stokes** (mayores, $\omega_a$). Las
Stokes suelen ser órdenes de magnitud más intensas.

Fig. 10.1.2 (p. 474): diagramas de niveles. Stokes: transición del fundamental $g$ al estado final
$n$ a través de un nivel virtual asociado al estado excitado $n'$ (absorbe $\omega$, emite $\omega_S$).
Anti-Stokes: de $n$ a $g$ con $n'$ como intermedio (emite $\omega_a$). Las anti-Stokes son débiles
porque en equilibrio térmico la población de $n$ es menor que la de $g$ por el factor de Boltzmann
$\exp(-\hbar\omega_{ng}/kT)$.

Interés espectroscópico (p. 474): permite estudiar transiciones prohibidas a un fotón. La transición
Raman requiere $\langle g|\hat{\mathbf r}|n'\rangle\neq0$ y $\langle n'|\hat{\mathbf r}|n\rangle\neq0$; en un medio con simetría de
inversión (estados de paridad definida) esto implica que $g$ y $n$ tienen la **misma paridad**, y
entonces $\langle g|\hat{\mathbf r}|n\rangle=0$: la transición $g\to n$ está prohibida como transición dipolar
eléctrica a un fotón.

### 10.2 Spontaneous versus Stimulated Raman Scattering (p. 474)

**Órdenes de magnitud.** El Raman espontáneo es débil: incluso en materia condensada la sección
eficaz por unidad de volumen para Stokes es $\approx10^{-6}\ \text{cm}^{-1}$, de modo que en 1 cm solo
$\sim1$ parte en $10^6$ de la radiación incidente se dispersa a la frecuencia Stokes. Con un láser
intenso, el proceso **estimulado** es muy fuerte: a menudo $\geq10\%$ de la energía del láser se
convierte a Stokes. El espontáneo emite con patrón dipolar; el estimulado, en un cono estrecho hacia
adelante y hacia atrás (p. 475). SRS: descubierta por Woodbury y Ng (1962), descrita por Eckhardt
*et al.* (1962); revisiones: Bloembergen (1967), Kaiser y Maier (1972), Penzkofer *et al.* (1979),
Raymer y Walmsley (1990).

**Argumento de Hellwarth (1963)** (p. 475). Se postula que la probabilidad por unidad de tiempo de
emitir un fotón en el modo Stokes $S$ es

$$P_S=Dm_L(m_S+1), \qquad (10.2.1),\ \text{p. 475}$$

con $m_L$ el número medio de fotones por modo del láser, $m_S$ el del modo Stokes y $D$ una constante
del material. $m_L$ da la dependencia lineal con la intensidad láser; $m_S+1$ da el término
estimulado ($m_S$) y el espontáneo (1), como en los coeficientes $A$ y $B$ de Einstein. Consistente con
el tratamiento cuántico completo de Raymer y Mostowski (1981). Entonces

$$\frac{dm_S}{dt}=Dm_L(m_S+1), \qquad (10.2.2)$$

y para un modo Stokes que viaja en $+z$ a velocidad $c/n$ (Fig. 10.2.1, p. 476)

$$\frac{dm_S}{dz}=\frac{1}{c/n}\frac{dm_S}{dt}=\frac{1}{c/n}Dm_L(m_S+1). \qquad (10.2.3)$$

(10.2.3) vale para cualquier ángulo entre láser y Stokes si $z$ se mide a lo largo de la dirección
Stokes (p. 476).

*Límite $m_S\ll1$ (espontáneo):*
$$\frac{dm_S}{dz}=\frac{1}{c/n}Dm_L, \qquad (10.2.4)$$
$$m_S(z)=m_S(0)+\frac{1}{c/n}Dm_Lz\quad(m_S\ll1), \qquad (10.2.5)$$
suponiendo el láser no afectado ($m_L$ independiente de $z$). La intensidad Stokes crece
proporcionalmente a la longitud, es decir, al número de moléculas.

*Límite $m_S\gg1$ (estimulado):*
$$\frac{dm_S}{dz}=\frac{1}{c/n}Dm_Lm_S, \qquad (10.2.6)$$
$$m_S(z)=m_S(0)e^{Gz}, \qquad (10.2.7)$$
con el **coeficiente de ganancia Raman**
$$G=\frac{Dm_L}{c/n}. \qquad (10.2.8),\ \text{p. 476}$$
Si no se inyecta campo, $m_S(0)$ representa el ruido cuántico del vacío, equivalente a un fotón por
modo (p. 477).

**Relación entre $G$ y la sección eficaz espontánea** (p. 477–479). Como $D$ fija ambos regímenes,
se puede relacionar $G$ con la sección eficaz. Por cada Stokes creado se pierde un fotón láser; como
hay muchos modos Stokes, la pérdida total es

$$\frac{dm_L}{dz}=-Mb\frac{dm_S}{dz}=\frac{-Dm_LMb}{c/n}, \qquad (10.2.9)$$

con $M$ el número total de modos en que el sistema puede radiar y $b$ un factor geométrico (cociente
entre la tasa Stokes promediada en ángulo y la tasa en la dirección del modo $S$ considerado):

$$b=\frac{\int|f(\theta,\phi)|^2d\Omega/4\pi}{|f(\theta_S,\phi_S)|^2}. \qquad (10.2.10)$$

Número de modos (Boyd 1983, ec. 3.4.4), p. 478:
$$M=\frac{V\omega_S^2\Delta\omega}{\pi^2(c/n)^3}, \qquad (10.2.11)$$
con $V$ el volumen de cuantización y $\Delta\omega$ el ancho de la radiación Stokes. Definición de la
sección eficaz Raman ($N$ = densidad de moléculas):
$$\frac{dm_L}{dz}=-N\sigma m_L. \qquad (10.2.12)$$
Comparando (10.2.9) y (10.2.12):
$$D=\frac{N\sigma(c/n)}{Mb}. \qquad (10.2.13)$$
Sustituyendo en (10.2.8):
$$G=\frac{N\sigma\pi^2c^3m_L}{V\omega_S^2\Delta\omega\,bn^3}\equiv\frac{N\pi^2c^3m_L}{V\omega_S^2bn^3}\left(\frac{\partial\sigma}{\partial\omega}\right)_0, \qquad (10.2.14)$$
$$\sigma=\left(\frac{\partial\sigma}{\partial\omega}\right)_0\Delta\omega. \qquad (10.2.15)$$
Para pasar a intensidad (geometría de la Fig. 10.2.2: caja de longitud $L$ y área $A$, $V=AL$):
$$I_L=\frac{m_L\hbar\omega_L}{A(nL/c)}=\frac{m_L\hbar\omega_Lc}{Vn}, \qquad (10.2.16)$$
y entonces (p. 479)
$$G=\frac{N\pi^2c^2}{\omega_S^2bn^2\hbar\omega_L}\left(\frac{\partial\sigma}{\partial\omega}\right)_0I_L. \qquad (10.2.17)$$
Con la sección eficaz diferencial espectral,
$$\left(\frac{\partial\sigma}{\partial\omega}\right)_0=4\pi b\left(\frac{\partial^2\sigma}{\partial\omega\,\partial\Omega}\right)_0, \qquad (10.2.18)$$
$$\boxed{G=\frac{4\pi^3Nc^2}{\omega_S^2\hbar\omega_Ln_S^2}\left(\frac{\partial^2\sigma}{\partial\omega\,\partial\Omega}\right)_0I_L.} \qquad (10.2.19)$$
$G$ es proporcional a $I_L$; el cociente $G/I_L$ (en m/TW) es el "gain factor" que tabula la Tabla 10.2.1.

**Tabla 10.2.1** (p. 480), *Properties of stimulated Raman scattering for several materials* (según
Kaiser y Maier 1972 y Simon y Tittel 1994; todas vibracionales salvo la línea de H₂ de 450 cm⁻¹,
rotacional; ganancia medida a 694 nm salvo indicación; ᶜ medida a 500 nm). Ver la tabla completa
en la sección "Tablas y datos numéricos".

### 10.3 Stimulated Raman Scattering Described by the Nonlinear Polarization (p. 479)

Modelo clásico (no cuántico; ver también Garmire *et al.* 1963), escalar. El campo interactúa con un
modo vibracional (Fig. 10.3.1, p. 481) descrito como oscilador armónico de frecuencia $\omega_v$ y
amortiguamiento $\gamma$; $\tilde q(t)$ es la desviación de la distancia internuclear respecto al equilibrio $q_0$:

$$\frac{d^2\tilde q}{dt^2}+2\gamma\frac{d\tilde q}{dt}+\omega_v^2\tilde q=\frac{\tilde F(t)}{m}, \qquad (10.3.1),\ \text{p. 480}$$

con $m$ la masa nuclear reducida. **Hipótesis clave:** la polarizabilidad óptica (sobre todo
electrónica) depende de la separación internuclear,

$$\tilde\alpha(t)=\alpha_0+\left(\frac{\partial\alpha}{\partial q}\right)_0\tilde q(t). \qquad (10.3.2)$$

Una colección de moléculas que oscilan coherentemente modula el índice:
$$\tilde n(t)=\sqrt{\tilde\epsilon(t)}=[1+N\tilde\alpha(t)]^{1/2}, \qquad (10.3.3),\ \text{p. 481}$$
lo que imprime bandas laterales a $\pm\omega_v$ sobre el láser transmitido.

**Excitación coherente de la vibración.** Momento dipolar inducido y energía:
$$\tilde{\mathbf p}(z,t)=\epsilon_0\alpha\tilde{\mathbf E}(z,t), \qquad (10.3.4)$$
$$W=\tfrac12\langle\tilde{\mathbf p}\cdot\tilde{\mathbf E}\rangle=\tfrac12\epsilon_0\alpha\langle\tilde E^2(z,t)\rangle, \qquad (10.3.5)$$
(promedio sobre un periodo óptico), de donde la fuerza sobre la coordenada vibracional
$$\tilde F=\frac{dW}{dq}=\frac{\epsilon_0}{2}\left(\frac{d\alpha}{dq}\right)_0\langle\tilde E^2(z,t)\rangle. \qquad (10.3.6)$$
Si el campo tiene dos frecuencias, la fuerza oscila a la frecuencia de batido.

Fig. 10.3.2 (p. 482): (a) la vibración modula el índice e imprime bandas $\omega_S=\omega_L-\omega_v$ y
$\omega_a=\omega_L+\omega_v$; (b) Stokes y láser baten y modulan la intensidad total

$$\tilde I(t)=I_0+I_1\cos(\omega_L-\omega_S)t, \qquad (10.3.7)$$

que excita coherentemente la vibración a $\omega_L-\omega_S=\omega_v$. Los dos procesos se refuerzan
mutuamente (más vibración → más Stokes → más vibración).

**Cálculo.** Campo total
$$\tilde E(z,t)=A_Le^{i(k_Lz-\omega_Lt)}+A_Se^{i(k_Sz-\omega_St)}+\text{c.c.} \qquad (10.3.8)$$
Parte variable de la fuerza (10.3.6):
$$\tilde F(z,t)=\epsilon_0\left(\frac{\partial\alpha}{\partial q}\right)_0\left[A_LA_S^*e^{i(Kz-\Omega t)}+\text{c.c.}\right], \qquad (10.3.9)$$
$$K=k_L-k_S,\qquad \Omega=\omega_L-\omega_S. \qquad (10.3.10)$$
Solución de prueba
$$\tilde q=q(\Omega)e^{i(Kz-\Omega t)}+\text{c.c.} \qquad (10.3.11)$$
Al sustituir en (10.3.1) (p. 483) se obtiene

$$-\omega^2q(\Omega)-2i\omega\gamma q(\Omega)+\omega_v^2q(\Omega)=\frac{\epsilon_0}{m}\left(\frac{\partial\alpha}{\partial q}\right)_0A_LA_S^*$$

(ec. sin número; *errata de lectura: se lee $\omega$ donde por consistencia con (10.3.12) debe ser $\Omega$*), y

$$q(\Omega)=\frac{(\epsilon_0/m)(\partial\alpha/\partial q)_0A_LA_S^*}{\omega_v^2-\Omega^2-2i\Omega\gamma}. \qquad (10.3.12)$$

Polarización:
$$\tilde P(z,t)=N\tilde p=\epsilon_0N\tilde\alpha\tilde E=\epsilon_0N\left[\alpha_0+\left(\frac{\partial\alpha}{\partial q}\right)_0\tilde q(z,t)\right]\tilde E(z,t), \qquad (10.3.13)$$
$$\tilde P^{\rm NL}(z,t)=\epsilon_0N\left(\frac{\partial\alpha}{\partial q}\right)_0\left[q(\Omega)e^{i(Kz-\Omega t)}+\text{c.c.}\right]\times\left[A_Le^{i(k_Lz-\omega_Lt)}+A_Se^{i(k_Sz-\omega_St)}+\text{c.c.}\right]. \qquad (10.3.14)$$
Componente a $\omega_S$ (polarización Stokes):
$$\tilde P_S^{\rm NL}(z,t)=P(\omega_S)e^{-i\omega_St}+\text{c.c.}, \qquad (10.3.15)$$
$$P(\omega_S)=N\epsilon_0\left(\frac{\partial\alpha}{\partial q}\right)_0q^*(\Omega)A_Le^{ik_Sz}, \qquad (10.3.16)$$
$$P(\omega_S)=\frac{(\epsilon_0^2N/m)(\partial\alpha/\partial q)_0^2|A_L|^2A_S}{\omega_v^2-\Omega^2+2i\Omega\gamma}e^{ik_Sz}. \qquad (10.3.17)$$
Definición de la **susceptibilidad Raman** ($\chi_R(\omega_S)\equiv\chi^{(3)}(\omega_S=\omega_S+\omega_L-\omega_L)$):
$$P(\omega_S)=6\epsilon_0\chi_R(\omega_S)|A_L|^2A_Se^{ik_Sz}, \qquad (10.3.18)$$
de donde (p. 484)
$$\chi_R(\omega_S)=\frac{\epsilon_0(N/6m)(\partial\alpha/\partial q)_0^2}{\omega_v^2-(\omega_L-\omega_S)^2+2i(\omega_L-\omega_S)\gamma}. \qquad (10.3.19a)$$
Cerca de la resonancia:
$$\chi_R(\omega_S)=\frac{(\epsilon_0N/12m\omega_v)(\partial\alpha/\partial q)_0^2}{[\omega_S-(\omega_L-\omega_v)]+i\gamma}. \qquad (10.3.19b)$$
Fig. 10.3.3: $\chi_R'$ dispersiva y $\chi_R''$ con un pico **negativo** en $\omega_S=\omega_L-\omega_v$. En la resonancia
exacta $\chi_R$ es imaginario negativo, lo que da amplificación.

**Propagación Stokes.** Con (10.3.8), (10.3.15), (10.3.18) y (9.3.19) en la ecuación de onda (2.1.17) y la
aproximación de amplitud lentamente variable:
$$\frac{dA_S}{dz}=-\alpha_SA_S, \qquad (10.3.20)$$
$$\alpha_S=-3i\frac{\omega_S}{n_Sc}\chi_R(\omega_S)|A_L|^2, \qquad (10.3.21)$$
coeficiente de "absorción" Stokes. Como $\text{Im}\,\chi_R(\omega_S)<0$, $\text{Re}\,\alpha_S<0$: crecimiento
exponencial. $\alpha_S$ depende solo de $|A_L|$: **la condición de ajuste de fase se satisface
automáticamente**; la amplificación Raman Stokes es un proceso de *ganancia pura* (p. 485).

**Anti-Stokes** (p. 485). En (10.3.19a) no se supuso signo de $\omega_L-\omega_S$, así que
$$\chi_R(\omega_a)=\frac{\epsilon_0(N/6m)(\partial\alpha/\partial q)_0^2}{\omega_v^2-(\omega_L-\omega_a)^2+2i(\omega_L-\omega_a)\gamma}. \qquad (10.3.22)$$
Como
$$\omega_L-\omega_S=-(\omega_L-\omega_a), \qquad (10.3.23)$$
$$\chi_R(\omega_a)=\chi_R(\omega_S)^*. \qquad (10.3.24)$$
Cerca de resonancia
$$\chi_R(\omega_a)=\frac{-(\epsilon_0N/12m\omega_v)(\partial\alpha/\partial q)_0^2}{[\omega_a-(\omega_L+\omega_v)]+i\gamma}, \qquad (10.3.25)$$
imaginario **positivo** en resonancia (Fig. 10.3.4: $\chi_R''(\omega_S)$ negativo en $\omega_L-\omega_v$, $\chi_R''(\omega_a)$
positivo en $\omega_L+\omega_v$). Entonces
$$\frac{dA_a}{dz}=-\alpha_aA_a, \qquad (10.3.26)$$
$$\alpha_a=-3i\frac{\omega_a}{n_ac}\chi_R(\omega_a)|A_L|^2, \qquad (10.3.27),\ \text{p. 486}$$
real positivo: la anti-Stokes se **atenúa**.

**Contribución de mezcla de cuatro ondas.** Experimentalmente (Terhune 1963) la anti-Stokes se
genera con eficiencia apreciable en ciertas direcciones. Origen: otro término de (10.3.14),
$$\tilde P_a^{\rm NL}(z,t)=P(\omega_a)e^{-i\omega_at}+\text{c.c.}, \qquad (10.3.28)$$
$$P(\omega_a)=N\epsilon_0\left(\frac{\partial\alpha}{\partial q}\right)_0q(\Omega)A_L=\frac{(N\epsilon_0^2/m)(\partial\alpha/\partial q)_0^2A_L^2A_S^*}{\omega_v^2-\Omega^2-2i\Omega\gamma}e^{i(2k_L-k_S)z}, \qquad (10.3.29)$$
con $\Omega\equiv\omega_L-\omega_S=\omega_a-\omega_L$. Se define $\chi_F(\omega_a)\equiv\chi^{(3)}(\omega_a=\omega_L+\omega_L-\omega_S)$ por
$$P(\omega_a)=3\epsilon_0\chi_F(\omega_a)A_L^2A_S^*e^{i(2k_L-k_S)z}, \qquad (10.3.30)$$
$$\chi_F(\omega_a)=\frac{(N\epsilon_0/3m)(\partial\alpha/\partial q)_0^2}{\omega_v^2-(\omega_L-\omega_a)^2+2i(\omega_L-\omega_a)\gamma}, \qquad (10.3.31)$$
$$\chi_F(\omega_a)=2\chi_R(\omega_a). \qquad (10.3.32)$$
Polarización total anti-Stokes:
$$P(\omega_a)=6\epsilon_0\chi_R(\omega_a)|A_L|^2A_ae^{ik_az}+3\epsilon_0\chi_F(\omega_a)A_L^2A_S^*e^{i(2k_L-k_S)z}. \qquad (10.3.33)$$
Análogamente para Stokes:
$$\chi_F(\omega_S)=\frac{(N\epsilon_0/3m)(\partial\alpha/\partial q)_0^2}{\omega_v^2-(\omega_L-\omega_a)^2+2i(\omega_L-\omega_S)\gamma} \qquad (10.3.34)$$
(*duda de lectura: el denominador mezcla $(\omega_L-\omega_a)^2$ con $(\omega_L-\omega_S)\gamma$; como
$(\omega_L-\omega_a)^2=(\omega_L-\omega_S)^2$ el valor no cambia, pero por consistencia debería escribirse $(\omega_L-\omega_S)^2$*),
$$P(\omega_S)=6\epsilon_0\chi_R(\omega_S)|A_L|^2A_Se^{ik_Sz}+3\epsilon_0\chi_F(\omega_S)A_L^2A_a^*e^{i(2k_L-k_a)z}, \qquad (10.3.35),\ \text{p. 487}$$
$$\chi_F(\omega_S)=2\chi_R(\omega_S), \qquad (10.3.36)$$
$$\chi_F(\omega_S)=\chi_F(\omega_a)^*. \qquad (10.3.37)$$

**Ecuaciones acopladas** (medio ópticamente isótropo, SVA, bombeo constante), p. 487:
$$\frac{dA_S}{dz}=-\alpha_SA_S+\kappa_SA_a^*e^{i\Delta kz}, \qquad (10.3.38a)$$
$$\frac{dA_a}{dz}=-\alpha_aA_a+\kappa_aA_S^*e^{i\Delta kz}, \qquad (10.3.38b)$$
$$\alpha_j=\frac{-3i\omega_j}{n_jc}\chi_R(\omega_j)|A_L|^2,\qquad j=S,a, \qquad (10.3.39a)$$
$$\kappa_j=\frac{3i\omega_j}{2n_jc}\chi_F(\omega_j)A_L^2,\qquad j=S,a, \qquad (10.3.39b)$$
$$\Delta k=\Delta\mathbf k\cdot\hat{\mathbf z}=(2\mathbf k_L-\mathbf k_S-\mathbf k_a)\cdot\hat{\mathbf z}. \qquad (10.3.40)$$
Cada amplitud tiene un término de ganancia/pérdida Raman y uno de mezcla de cuatro ondas que solo
es eficaz si $\Delta k$ es pequeño. En un material con dispersión normal, $n_L<\tfrac12(n_S+n_a)$
(Fig. 10.3.5a, p. 488), de modo que el ajuste de fase $\Delta k=0$ siempre puede lograrse con el Stokes
propagándose a un ángulo $\theta\neq0$ respecto al láser (Fig. 10.3.5b: triángulo $\mathbf k_S+\mathbf k_a=2\mathbf k_L$).
Lejos de ese ángulo, $\Delta k$ grande: las ecuaciones se desacoplan, Stokes gana y anti-Stokes pierde
(el texto dice "experiences lose", errata tipográfica por *loss*). Cerca, deben resolverse juntas y
ambas bandas pueden generarse en direcciones de $\Delta k$ pequeño (conos).

### 10.4 Stokes–Anti-Stokes Coupling in Stimulated Raman Scattering (p. 488)

Ecuaciones genéricas (válidas también para cualquier mezcla de cuatro ondas hacia adelante con
bombeo constante):
$$\frac{dA_1}{dz}=-\alpha_1A_1+\kappa_1A_2^*e^{i\Delta kz}, \qquad (10.4.1a)$$
$$\frac{dA_2^*}{dz}=-\alpha_2^*A_2^*+\kappa_2^*A_1e^{-i\Delta kz}. \qquad (10.4.1b)$$
Reescritura (p. 489):
$$e^{-i\Delta kz/2}\left(\frac{dA_1}{dz}+\alpha_1A_1\right)=\kappa_1A_2^*e^{i\Delta kz/2}, \qquad (10.4.2a)$$
$$e^{i\Delta kz/2}\left(\frac{dA_2^*}{dz}+\alpha_2^*A_2^*\right)=\kappa_2^*A_1e^{-i\Delta kz/2}, \qquad (10.4.2b)$$
$$\left(\frac{d}{dz}+\alpha_1+\frac{i\Delta k}{2}\right)A_1e^{-i\Delta kz/2}=\kappa_1A_2^*e^{i\Delta kz/2}, \qquad (10.4.3a)$$
$$\left(\frac{d}{dz}+\alpha_2^*-\frac{i\Delta k}{2}\right)A_2^*e^{i\Delta kz/2}=\kappa_2^*A_1e^{-i\Delta kz/2}. \qquad (10.4.3b)$$
Variables nuevas
$$F_1=A_1e^{-i\Delta kz/2},\qquad F_2^*=A_2^*e^{i\Delta kz/2}, \qquad (10.4.4)$$
$$\left(\frac{d}{dz}+\alpha_1+i\frac{\Delta k}{2}\right)F_1=\kappa_1F_2^*, \qquad (10.4.5a)$$
$$\left(\frac{d}{dz}+\alpha_2^*-i\frac{\Delta k}{2}\right)F_2^*=\kappa_2^*F_1. \qquad (10.4.5b)$$
Eliminando $F_2^*$:
$$\left(\frac{d}{dz}+\alpha_2^*-i\frac{\Delta k}{2}\right)\left(\frac{d}{dz}+\alpha_1+i\frac{\Delta k}{2}\right)F_1=\kappa_1\kappa_2^*F_1. \qquad (10.4.6)$$
Con $F_1(z)=F_1(0)e^{gz}$ (10.4.7):
$$\left(g+\alpha_2^*-\frac{i\Delta k}{2}\right)\left(g+\alpha_1+\frac{i\Delta k}{2}\right)=\kappa_1\kappa_2^*, \qquad (10.4.8)$$
$$g_\pm=-\tfrac12(\alpha_1+\alpha_2^*)\pm\tfrac12\left[(\alpha_1-\alpha_2^*+i\Delta k)^2+4\kappa_1\kappa_2^*\right]^{1/2}. \qquad (10.4.9)$$

Solución general (p. 490), si $g_+\neq g_-$:
$$F_1=F_1^+(0)e^{g_+z}+F_1^-(0)e^{g_-z}, \qquad (10.4.10)$$
$$A_1(z)=\left(A_1^+e^{g_+z}+A_1^-e^{g_-z}\right)e^{i\Delta kz/2}. \qquad (10.4.11)$$
Sustituyendo en (10.4.3a):
$\left(g_++\alpha_1+i\frac{\Delta k}{2}\right)A_1^+e^{g_+z}+\left(g_-+\alpha_1+i\frac{\Delta k}{2}\right)A_1^-e^{g_-z}=\kappa_1A_2^*e^{i\Delta kz/2}$, de donde
$$A_2^*(z)=\left[\left(\frac{g_++\alpha_1+i\Delta k/2}{\kappa_1}\right)A_1^+e^{g_+z}+\left(\frac{g_-+\alpha_1+i\Delta k/2}{\kappa_1}\right)A_1^-e^{g_-z}\right]e^{-i\Delta kz/2}. \qquad (10.4.12)$$
Con
$$A_2^*(z)=\left(A_2^{+*}e^{g_+z}+A_2^{-*}e^{g_-z}\right)e^{-i\Delta kz/2}, \qquad (10.4.13)$$
$$\frac{A_2^{\pm*}}{A_1^\pm}=\frac{g_\pm+\alpha_1+i\Delta k/2}{\kappa_1}, \qquad (10.4.14)$$
que define los **modos propios** de propagación de las ondas Stokes y anti-Stokes. La asimetría
entre $\omega_1$ y $\omega_2$ es solo aparente. Relaciones útiles (p. 491):
$$\left(g_++\alpha_1+\frac{i\Delta k}{2}\right)\left(g_-+\alpha_1+\frac{i\Delta k}{2}\right)=-\kappa_1\kappa_2^*, \qquad (10.4.15)$$
$$g_+-g_-=\left[(\alpha_1-\alpha_2^*+i\Delta k)^2+4\kappa_1\kappa_2^*\right]^{1/2}, \qquad (10.4.16a)$$
$$g_+-g_-=\pm\left[2g_\pm+(\alpha_1+\alpha_2^*)\right], \qquad (10.4.16b)$$
(ambos signos superiores o ambos inferiores),
$$g_++g_-=-(\alpha_1+\alpha_2^*), \qquad (10.4.16c)$$
$$\left(g_\pm+\alpha_1+\frac{i\Delta k}{2}\right)=-\left(g_\mp+\alpha_2^*-\frac{i\Delta k}{2}\right), \qquad (10.4.17a)$$
$$\left(g_\pm+\alpha_2^*+\frac{i\Delta k}{2}\right)=-\left(g_\mp+\alpha_1+\frac{i\Delta k}{2}\right). \qquad (10.4.17b)$$
*Errata de lectura en (10.4.17b):* de (10.4.16c), $g_\pm+\alpha_2^*=-(g_\mp+\alpha_1)$; restando $i\Delta k/2$ a ambos
lados, el lado izquierdo debería ser $(g_\pm+\alpha_2^*-i\Delta k/2)$, no $+i\Delta k/2$ (así es como se usa en la ec.
siguiente). Con (10.4.15) y (10.4.17a) (ec. sin número; la numeración salta de 10.4.17 a 10.4.19,
de modo que esta sería la 10.4.18):
$$\frac{A_2^{\pm*}}{A_1^\pm}=\frac{g_\pm+\alpha_1+i\Delta k/2}{\kappa_1}=\frac{-\kappa_2^*}{g_\mp+\alpha_1+i\Delta k/2}=\frac{\kappa_2^*}{g_\pm+\alpha_2^*-i\Delta k/2}.$$
Media geométrica de la primera y la última forma (forma simétrica):
$$\frac{A_2^{\pm*}}{A_1^\pm}=\left[\frac{\kappa_2^*(g_\pm+\alpha_1+i\Delta k/2)}{\kappa_1(g_\pm+\alpha_2^*-i\Delta k/2)}\right]^{1/2}. \qquad (10.4.19)$$

**Solución con condiciones en $z=0$** ($A_1(0)$, $A_2^*(0)$ dados), p. 492:
$$A_1(0)=A_1^++A_1^-, \qquad (10.4.20a)$$
$$A_2^*(0)=\left(\frac{g_++\alpha_1+i\Delta k/2}{\kappa_1}\right)A_1^++\left(\frac{g_-+\alpha_1+i\Delta k/2}{\kappa_1}\right)A_1^-. \qquad (10.4.20b)$$
Eliminando $A_1^-=A_1(0)-A_1^+$: $A_2^*(0)=\frac{g_+-g_-}{\kappa_1}A_1^++\frac{g_-+\alpha_1+i\Delta k/2}{\kappa_1}A_1(0)$, y
$$A_1^+=\left(\frac{\kappa_1}{g_+-g_-}\right)A_2^*(0)-\left(\frac{g_-+\alpha_1+i\Delta k/2}{g_+-g_-}\right)A_1(0), \qquad (10.4.21a)$$
$$A_1^-=-\left(\frac{\kappa_1}{g_+-g_-}\right)A_2^*(0)+\left(\frac{g_++\alpha_1+i\Delta k/2}{g_+-g_-}\right)A_1(0). \qquad (10.4.21b)$$
Entonces
$$A_1(z)=\frac{1}{g_+-g_-}\Big\{\Big[\kappa_1A_2^*(0)-\Big(g_-+\alpha_1+\frac{i\Delta k}{2}\Big)A_1(0)\Big]e^{g_+z}-\Big[\kappa_1A_2^*(0)-\Big(g_++\alpha_1+\frac{i\Delta k}{2}\Big)A_1(0)\Big]e^{g_-z}\Big\}e^{i\Delta kz/2}, \qquad (10.4.22)$$
$$A_2^*(z)=\frac{1}{g_+-g_-}\Big\{\Big[\Big(g_++\alpha_1+\frac{i\Delta k}{2}\Big)A_2^*(0)+\kappa_2^*A_1(0)\Big]e^{g_+z}-\Big[\Big(g_-+\alpha_1+\frac{i\Delta k}{2}\Big)A_2^*(0)+\kappa_2^*A_1(0)\Big]e^{g_-z}\Big\}e^{-i\Delta kz/2}, \qquad (10.4.23)$$
y, usando (10.4.17), en términos de $\alpha_2$ (p. 493):
$$A_2^*(z)=\frac{1}{g_+-g_-}\Big\{\Big[-\Big(g_-+\alpha_2^*-\frac{i\Delta k}{2}\Big)A_2^*(0)+\kappa_2^*A_1(0)\Big]e^{g_+z}+\Big[\Big(g_++\alpha_2^*-\frac{i\Delta k}{2}\Big)A_2^*(0)-\kappa_2^*A_1(0)\Big]e^{g_-z}\Big\}e^{-i\Delta kz/2}. \qquad (10.4.24)$$

#### 10.4.1 Dispersionless, Nonlinear Medium without Gain or Loss (p. 493)

$\alpha_1=\alpha_2=0$; sin pérdidas ni dispersión, $\chi^{(3)}(\omega_1=2\omega_0-\omega_2)=\chi^{(3)}(\omega_2=2\omega_0-\omega_1)$, y
$$\kappa_1\kappa_2^*=\frac{9\omega_1\omega_2}{4n_1n_2c^2}|\chi^{(3)}(\omega_1=2\omega_0-\omega_2)|^2|A_0|^4, \qquad (10.4.25)$$
real y positivo ($A_0$ = bombeo). Con $\Delta k$ arbitrario:
$$g_\pm=\pm\left[\kappa_1\kappa_2^*-(\Delta k/2)^2\right]^{1/2}. \qquad (10.4.26)$$
Si $\Delta k$ no es muy grande, $g_+>0$ (amplificación) y $g_-<0$ (atenuación); si $\Delta k^2>4\kappa_1\kappa_2^*$,
ambas raíces son imaginarias puras (comportamiento oscilatorio). Cociente de amplitudes (p. 494):
$$\frac{A_2^{\pm*}}{A_1^\pm}=\frac{g_\pm+i\Delta k/2}{\kappa_1}. \qquad (10.4.27)$$
Con $\Delta k=0$ vale $\pm(\kappa_2^*/\kappa_1)^{1/2}$ y, eligiendo $A_0$ real,
$$\frac{A_2^{\pm*}}{A_1^\pm}=\pm i\left(\frac{n_1\omega_2}{n_2\omega_1}\right)^{1/2}\simeq\pm i, \qquad (10.4.28)$$
las dos bandas están desfasadas $\pm\pi/2$ en cada modo propio.

#### 10.4.2 Medium without a Nonlinearity (p. 494)

$\kappa_1=\kappa_2=0$ y $\Delta k=0$ en (10.4.9):
$$g_+=-\alpha_2^*\quad\text{y}\quad g_-=-\alpha_1^*. \qquad (10.4.29)$$
(*Duda de lectura: de (10.4.9) con $\kappa=0$ resulta $g_-=-\alpha_1$, sin conjugado, que es lo que usa
(10.4.31b); se lee $-\alpha_1^*$.*) Si $\kappa_1,\kappa_2\to0$ con $\kappa_2^*/\kappa_1$ finito, de (10.4.19):
$$\frac{A_2^{+*}}{A_1^+}=\infty,\qquad\frac{A_2^{-*}}{A_1^-}=0. \qquad (10.4.30)$$
La raíz positiva es la onda $\omega_2$ y la negativa la onda $\omega_1$:
$$A_2^*(z)=A_2^*(0)e^{g_+z}=A_2^*(0)e^{-\alpha_2^*z}, \qquad (10.4.31a)$$
$$A_1(z)=A_1(0)e^{g_-z}=A_1(0)e^{-\alpha_1z}. \qquad (10.4.31b)$$
(En (10.4.31a) se lee "$e^{-\alpha_2^*(z)}$", errata tipográfica.) Propagación libre, como debe ser.

#### 10.4.3 Stokes–Anti-Stokes Coupling in Stimulated Raman Scattering (p. 495)

(Ver también Bloembergen y Shen 1964.) $\omega_1=\omega_S$, $\omega_2=\omega_a$; $\alpha_{S,a}$ y $\kappa_{S,a}$ de (10.3.39) con
(10.3.19b), (10.3.25), (10.3.31), (10.3.34). Como
$$\chi_F(\omega_S)=\chi_F(\omega_a)^*=2\chi_R(\omega_S)=2\chi_R(\omega_a)^*, \qquad (10.4.32)$$
$$\alpha_a=-\alpha_S^*\left(\frac{n_S\omega_a}{n_a\omega_S}\right), \qquad (10.4.33a)$$
$$\kappa_S=-\alpha_Se^{2i\phi_L}, \qquad (10.4.33b)$$
$$\kappa_a=\alpha_S^*\left(\frac{n_S\omega_a}{n_a\omega_S}\right)e^{2i\phi_L}, \qquad (10.4.33c)$$
$$A_L=|A_L|e^{i\phi_L}, \qquad (10.4.34)$$
$$\alpha_S=\frac{-i\omega_SN\epsilon_0^2(\partial\alpha/\partial q)_0^2|A_L|^2}{4mn_Sc\omega_v[\omega_S-(\omega_L-\omega_v)+i\gamma]}. \qquad (10.4.35)$$
Valores propios:
$$g_\pm=-\tfrac12\alpha_S\left(1-\frac{n_S\omega_a}{n_a\omega_S}\right)\pm\tfrac12\left\{\left[\alpha_S\left(1+\frac{n_S\omega_a}{n_a\omega_S}\right)+i\Delta k\right]^2-4\alpha_S^2\frac{n_S\omega_a}{n_a\omega_S}\right\}^{1/2}. \qquad (10.4.36)$$
Suele ser excelente aproximación tomar el factor igual a la unidad (*el texto escribe
"$n_S\omega_L/n_a\omega_S$"; por consistencia con (10.4.36) debe ser $n_S\omega_a/n_a\omega_S$*), y entonces
$$g_\pm=\pm\left[i\alpha_S\Delta k-(\Delta k/2)^2\right]^{1/2}. \qquad (10.4.37)$$

Fig. 10.4.1 (p. 496): $\text{Re}\,g_\pm$ frente a $\Delta k$; una rama ($g_-$) positiva y otra ($g_+$) negativa, ambas
tienden a cero en una cúspide en $\Delta k=0$ (mismo aspecto con la forma exacta). **Resultado
sorprendente: la ganancia acoplada se anula con ajuste de fase perfecto**: para $\Delta k$ pequeño la
anti-Stokes (que normalmente se atenúa) está tan acoplada a la Stokes que le impide crecer.

Límite $|\Delta k|\gg|\alpha_S|$:
$$g_\pm=\pm i\frac{\Delta k}{2}\left(1-\frac{4i\alpha_S}{\Delta k}\right)\simeq\pm\left(\alpha_S+\tfrac12i\Delta k\right) \qquad (10.4.38)$$
(*errata de lectura: falta el exponente $1/2$ sobre el paréntesis, $(1-4i\alpha_S/\Delta k)^{1/2}$, que es lo
que da el resultado aproximado*). Con (10.4.14):
$$\frac{A_a^{+*}}{A_S^+}=-2-i\frac{\Delta k}{\alpha_S}\simeq i\frac{\Delta k}{\alpha_S}, \qquad (10.4.39a)$$
$$\frac{A_a^{-*}}{A_S^-}=0. \qquad (10.4.39b)$$
(*Duda: el término dominante de la expresión exacta es $-i\Delta k/\alpha_S$; el signo de la forma aproximada
no coincide; se transcribe tal cual.*) El modo + es principalmente anti-Stokes y el − principalmente
Stokes. Nota al pie: en resonancia $\alpha_S$ es real y **negativo**, así que $g_-=-\alpha_S-\tfrac12i\Delta k$ tiene parte
real positiva (amplificación).

Con $\Delta k=0$ en la forma exacta (p. 497):
$$g_+=0,\qquad g_-=-\alpha_S\left(1-\frac{n_S\omega_a}{n_a\omega_S}\right). \qquad (10.4.40)$$
$|g_-|\ll|\alpha_S|$ pero no nulo; con esta convención, en resonancia $g_-$ es negativo. De (10.4.14), en
buena aproximación
$$\frac{A_a^{\pm*}}{A_S^\pm}=-1, \qquad (10.4.41)$$
cada modo propio es una combinación igual de Stokes y anti-Stokes. Evolución con $\Delta k=0$ y valores
en $z=0$, de (10.4.22)–(10.4.23):
$$A_S(z)=\frac{-1}{1-n_S\omega_a/n_a\omega_S}\left\{\left[A_a^*(0)e^{2i\phi_L}+\frac{n_S\omega_a}{n_a\omega_S}A_S(0)\right]-\left[A_a^*(0)e^{2i\phi_L}+A_S(0)\right]e^{g_-z}\right\}, \qquad (10.4.42a)$$
$$A_a^*(z)=\frac{1}{1-n_S\omega_a/n_a\omega_S}\left\{\left[A_a^*(0)+\frac{n_S\omega_a}{n_a\omega_S}A_S(0)e^{-2i\phi_L}\right]-\frac{n_S\omega_a}{n_a\omega_S}\left[A_a^*(0)+A_S(0)e^{-2i\phi_L}\right]e^{g_-z}\right\}. \qquad (10.4.42b)$$
Como $g_-<0$, el segundo término decae y
$$A_S(z\to\infty)=\frac{-1}{1-n_S\omega_a/n_a\omega_S}\left[A_a^*(0)e^{2i\phi_L}+\frac{n_S\omega_a}{n_a\omega_S}A_S(0)\right], \qquad (10.4.43a)$$
$$A_a^*(z\to\infty)=\frac{1}{1-n_S\omega_a/n_a\omega_S}\left[A_a^*(0)+\frac{n_S\omega_a}{n_a\omega_S}A_S(0)e^{-2i\phi_L}\right]. \qquad (10.4.43b)$$
Cada campo se amplifica por el factor $(1-n_S\omega_a/n_a\omega_S)^{-1}$ y, tras varias longitudes $1/g_-$, deja de
cambiar (Fig. 10.4.2a, p. 498).

Interpretación (p. 498): con el campo
$$\tilde E(z,t)=A_Le^{i(k_Lz-\omega_Lt)}+A_Se^{i(k_Sz-\omega_St)}+A_ae^{i(k_az-\omega_at)}+\text{c.c.}, \qquad (10.4.44)$$
con $k_L-k_S=k_a-k_L\equiv K$ y $\omega_L-\omega_S=\omega_a-\omega_L\equiv\Omega$, la vibración es $\tilde q(z,t)=q(\Omega)e^{i(Kz-\Omega t)}+\text{c.c.}$ con
$$q(\Omega)=\frac{(\epsilon_0/m)(\partial\alpha/\partial q)_0(A_LA_S^*+A_aA_L^*)}{\omega_v^2-\Omega^2-2i\Omega\gamma}. \qquad (10.4.45)$$
(El lado izquierdo se lee "$g(\Omega)$", errata por $q(\Omega)$.) Con (10.4.43), en el régimen asintótico
$A_LA_S^*+A_aA_L^*\to0$: la vibración molecular se anula (Fig. 10.4.2b, $q$ decae con $z$), por eso los
campos dejan de crecer.

### 10.5 Coherent Anti-Stokes Raman Scattering (p. 499)

Fig. 10.5.1: (a) Raman espontáneo; (b) SRS, descrito por $\chi_R^{(3)}(\omega_S=\omega_S+\omega_L-\omega_L)$, con crecimiento
Stokes cuya tasa escala como $I_L\times\text{Im}\,\chi_R^{(3)}$; (c) **CARS**: dos láseres $\omega_1$ y $\omega_2<\omega_1$ generan
$2\omega_1-\omega_2$ vía $\chi_F^{(3)}(\omega_a=\omega_1-\omega_2+\omega_1)$; (d) **CSRS** (coherent Stokes Raman scattering): salida a
$2\omega_2-\omega_1$ vía $\chi_F^{(3)}(\omega_S=\omega_2+\omega_2-\omega_1)$. Se estudia CARS, el más usado. De (10.3.25) y (10.3.32):
$$\chi_F^{(3)}(\omega_a=\omega_1-\omega_2+\omega_1)=\frac{-(\epsilon_0N/6m\omega_v)(\partial\alpha/\partial q)_0^2}{[(\omega_1-\omega_2)-\omega_v]+i\gamma}. \qquad (10.5.1)$$
Resonancia cuando $\omega_1-\omega_2=\omega_v$ (p. 500): herramienta diagnóstica para detectar especies químicas por
sus modos vibracionales, y sonda de estructura molecular ($\omega_v$ y $\gamma$ dependen del entorno).
Generación de la anti-Stokes, de (10.3.38b):
$$\frac{dA_a}{dz}=-\alpha_aA_a+\kappa_aA_2^*e^{i\Delta kz}, \qquad (10.5.2)$$
$$\alpha_a=\frac{-3i\omega_a}{n_ac}\chi_R(\omega_a)|A_1|^2,\qquad\kappa_a=\frac{3i\omega_a}{2n_ac}\chi_F(\omega_a)A_1^2, \qquad (10.5.3)$$
$$\Delta k=\Delta\mathbf k\cdot\hat{\mathbf z}=(2\mathbf k_1-\mathbf k_2-\mathbf k_a)\cdot\hat{\mathbf z}. \qquad (10.5.4)$$
Normalmente domina el segundo término (ganancia SRS pequeña); con $\Delta k=0$:
$$A_a(z)=\frac{3i\omega_a}{2n_ac}\chi_F(\omega_a)A_1^2A_2^*z. \qquad (10.5.5)$$
Variación espectral $\propto|\chi_F(\omega_a)|^2$: se esperaría una lorentziana, pero la línea medida suele estar muy
distorsionada (Fig. 10.5.2, p. 501: escala logarítmica 0.01–100 frente a $(\omega_1-\omega_2)-\omega_v$, con un máximo
seguido de un mínimo profundo, tipo Levenson y Bloembergen 1974). Causa: además de la respuesta
resonante hay una **susceptibilidad de fondo no resonante** $\chi_{\rm NR}^{(3)}$ (respuesta electrónica y modos
vibracionales no resonantes); la línea es $|\chi_{\rm NR}^{(3)}+\chi_F^{(3)}(\omega_a)|^2$ (interferencia). Primera observación:
Maker y Terhune (1965); estudios tempranos: Levenson *et al.* (1972), Levenson y Bloembergen (1974);
libro de Levenson y Kano (1988); CARS para imagen y microscopía: Volkmer (2005).

### 10.6 Stimulated Rayleigh-Wing Scattering (p. 501)

Dispersión debida a la tendencia de moléculas **anisótropas** a alinearse con el campo eléctrico de la
onda. Teoría: Bloembergen y Lallemand (1966), Chiao *et al.* (1966); observación: Mash *et al.* (1965),
Cho *et al.* (1967); además Denariez y Bret (1968), Foltz *et al.* (1968). Recordando §4.4 (orientación
molecular con un solo campo monocromático):
$$\langle\alpha\rangle=\alpha_0+\alpha_{\rm NL}, \qquad (10.6.1)$$
$$\alpha_0=\tfrac13\alpha_\parallel+\tfrac23\alpha_\perp, \qquad (10.6.2)$$
con $\alpha_\parallel$, $\alpha_\perp$ las polarizabilidades paralela y perpendicular al eje de simetría (Fig. 10.6.1, p. 502:
elipsoide con $\alpha_\parallel>\alpha_\perp$), y la contribución no lineal de orden más bajo
$$\alpha_{\rm NL}=\bar\alpha_2\langle\tilde E^2\rangle, \qquad (10.6.3)$$
$$\bar\alpha_2=\frac{2}{45n_0}\frac{(\alpha_\parallel-\alpha_\perp)^2}{kT}. \qquad (10.6.4)$$
Campo con láser y Stokes, **misma polarización lineal y contrapropagantes**:
$$\tilde E(\mathbf r,t)=A_Le^{i(k_Lz-\omega_Lt)}+A_Se^{i(-k_Sz-\omega_St)}+\text{c.c.} \qquad (10.6.5)$$
Como $\langle\tilde E^2\rangle$ tiene ahora una componente a $\omega_L-\omega_S$, (10.6.3) ya no vale y se supone una respuesta
de relajación
$$\tau\frac{d\alpha_{\rm NL}}{dt}+\alpha_{\rm NL}=\bar\alpha_2\overline{\tilde E^2}, \qquad (10.6.6)$$
con $\tau$ el **tiempo de relajación de la orientación molecular** (Tabla 10.6.1). Es una ecuación de Debye,
como las de acoplamiento de dos haces de §7.4 (p. 503). En estado estacionario con (10.6.5):
$$\alpha_{\rm NL}(z,t)=2\bar\alpha_2(A_LA_L^*+A_SA_S^*)+\left(\frac{2\bar\alpha_2A_LA_S^*e^{i(qz-\Omega t)}}{1-i\Omega\tau}\right)+\text{c.c.}, \qquad (10.6.7)$$
(se lee $e^{iqz-\Omega t}$, falta el paréntesis), con
$$q=k_L+k_S,\qquad\Omega=\omega_L-\omega_S. \qquad (10.6.8)$$
El denominador complejo desfasa la respuesta respecto al patrón de interferencia: **origen de la
ganancia**. Como en §7.4, se necesitan $n_0$ y $n_2$. Lorentz–Lorenz (ver (3.8.8a)):
$$\frac{n_0^2-1}{n_0^2+2}=\tfrac13N\alpha_0, \qquad (10.6.9a)$$
y (ver (4.1.18) y (4.4.26)), p. 504:
$$n_2=\left(\frac{n_0^2+2}{3}\right)^4\frac{1}{2n_0^2\epsilon_0c}N\bar\alpha_2. \qquad (10.6.9b)$$
Como en (7.4.15):
$$\frac{dA_S}{dz}=\frac{2in_0n_2\omega_S}{c}(A_LA_L^*+A_SA_S^*)A_S+\frac{2in_0n_2\omega_S}{c}\frac{A_LA_L^*A_S}{1+i\Omega\tau}. \qquad (10.6.10)$$
El primer término solo cambia la fase; el segundo da fase y amplificación. Con
$$I_j=2n_0\epsilon_0c|A_j|^2,\quad j=L,S, \qquad (10.6.11)$$
$$\frac{dI_S}{dz}=2n_0\epsilon_0c\left[A_S\frac{dA_S^*}{dz}+A_S^*\frac{dA_S}{dz}\right], \qquad (10.6.12)$$
$$\frac{dI_S}{dz}=g_{RW}I_LI_S, \qquad (10.6.13)$$
(el texto dice "estimated Raleigh-wing", errata por *stimulated Rayleigh-wing*), con
$$g_{RW}=g_{RW}^{(\max)}\left(\frac{2\Omega\tau}{1+\Omega^2\tau^2}\right), \qquad (10.6.14a)$$
$$g_{RW}^{(\max)}=\frac{n_2\omega_S}{c}=\left(\frac{n_0^2+2}{3}\right)^4\frac{2\omega_SN(\alpha_\parallel-\alpha_\perp)^2}{45kTn_0^2\epsilon_0c^2}, \qquad (10.6.14b)$$
usando (10.6.4) y (10.6.9b).

Fig. 10.6.2 (p. 505): $g_{RW}$ frente a $\omega_S-\omega_L\equiv-\Omega$, forma dispersiva: **amplificación para
$\omega_S<\omega_L$, atenuación para $\omega_S>\omega_L$; máximo en $\Omega=1/\tau$**. Fig. 10.6.3: la interferencia entre el
láser (hacia adelante, $k_L$) y el Stokes (hacia atrás, $k_S$) forma franjas que se mueven lentamente hacia
adelante con velocidad de fase $v=\Omega/q$; planos de máxima y mínima alineación molecular, desfasados
respecto a los máximos y mínimos de intensidad; la dispersión del láser en esta red produce el
Stokes, desplazado al rojo porque la perturbación se mueve hacia adelante. Hay ganancia porque el
Stokes refuerza la parte modulada del patrón → más alineación → más dispersión (p. 506). (*La
Fig. 10.6.3 rotula $q=k_L-k_S$, inconsistente con (10.6.8) $q=k_L+k_S$ para ondas contrapropagantes en
módulo; se lee así.*)

#### 10.6.1 Polarization Properties of Stimulated Rayleigh-Wing Scattering (p. 506)

Análisis de Chiao y Godine (1969); solo resultados. Ecuación de movimiento tensorial para la
contribución no lineal a la susceptibilidad:
$$\tau\frac{d}{dt}\Delta\chi_{ik}+\Delta\chi_{ik}=C\left(\langle\tilde E_i\tilde E_k\rangle-\tfrac13\delta_{ik}\langle\tilde{\mathbf E}\cdot\tilde{\mathbf E}\rangle\right), \qquad (10.6.15)$$
con (sin correcciones de campo local)
$$C=\frac{N\epsilon_0^2(\alpha_\parallel-\alpha_\perp)^2}{15kT}. \qquad (10.6.16)$$
La traza del lado derecho es nula: Rayleigh-wing se describe con un tensor de permitividad simétrico y
sin traza. Imponiendo la ecuación de onda al Stokes y teniendo en cuenta la rotación de la
polarización del bombeo (§4.2), se obtiene la ganancia para polarizaciones arbitrarias (Tabla 10.6.2).
Para cualquier polarización del bombeo, alguna polarización del Stokes tiene ganancia máxima; como
para observar dispersión estimulada se necesita $g_{RW}I_LL\simeq25$, la luz generada tiene casi esa
polarización (Tabla 10.6.3). La onda generada es casi, pero no exactamente, el **conjugado de
polarización** (conjugación vectorial, §7.2) del láser: su elipse es más redonda e inclinada. Zel'dovich
y Yakovleva (1980): con bombeo completamente despolarizado (polarización aleatoria en la sección
transversal) la conjugación vectorial es esencialmente perfecta. Reconstrucción de frente de onda:
Kudriavtseva *et al.* (1978); conjugación vectorial: Miller *et al.* (1990), p. 507.

El SRWS hacia adelante o casi adelante es mucho más complicado porque hay que incluir el acople
Stokes–anti-Stokes (§10.4): Chiao *et al.* (1966), Chiao y Godine (1969), p. 508.

---

## Tablas y datos numéricos útiles

**Tabla 10.2.1** (p. 480). Propiedades de SRS. $\nu_0$: desplazamiento (cm⁻¹); $\Delta\nu$: ancho de línea (cm⁻¹);
$N(d\sigma/d\Omega)_0$ en $10^{-6}$ m⁻¹ s⁻¹ (unidades tal como se leen; ver dudas); $G/I_L$ en m/TW, medido a 694 nm
salvo ᶜ (500 nm). Entre paréntesis, presión del gas.

| Sustancia | $\nu_0$ (cm⁻¹) | $\Delta\nu$ (cm⁻¹) | $N(d\sigma/d\Omega)_0$ | $G/I_L$ (m/TW) |
|---|---|---|---|---|
| O₂ líquido | 1552 | 0.117 | 0.48 ± 0.14 | 145 ± 40 |
| N₂ líquido | 2326.5 | 0.067 | 0.29 ± 0.09 | 160 ± 50 |
| Benceno | 992 | 2.15 | 3.06 | 28 |
| CS₂ | 655.6 | 0.50 | 7.55 | 240 |
| Nitrobenceno | 1345 | 6.6 | 6.4 | 21 |
| Bromobenceno | 1000 | 1.9 | 1.5 | 15 |
| Clorobenceno | 1002 | 1.6 | 1.5 | 19 |
| Tolueno | 1003 | 1.94 | 1.1 | 12 |
| "NiNbO₃" (LiNbO₃) | 256 | 23 | 381 | 89 |
|  | 637 | 20 | 231 | 94 |
| Ba₂NaNb₅O₁₅ | 650 | — | — | 67 |
| LiTaO₃ | 201 | 22 | 238 | 44 |
| SiO₂ | 467 | — | — | "08" (¿0.8?) |
| Metano (gas) | 2916 | — | (10 atm)ᶜ | 6.6 |
| H₂ (gas) | 4155 | — | (>10 atm) | 15 |
| H₂ (gas, rotacional) | 450 | — | (>0.5 atm) | 5 |
| Deuterio (gas) | 2991 | — | (>10 atm) | 11 |
| N₂ (gas) | 2326 | — | (10 atm)ᶜ | 0.71 |
| O₂ (gas) | 1555 | — | (10 atm)ᶜ | 0.16 |

**Tabla 10.6.1** (p. 503). Propiedades de SRWS.

| Sustancia | $G$ (m/TW) | $\tau$ (ps) | $\Delta\nu=1/2\pi\tau$ (GHz) |
|---|---|---|---|
| CS₂ | 30 | 2 | 80 |
| Nitrobenceno | 30 | 48 | 3.3 |
| Bromobenceno | 14 | 15 | 10 |
| Clorobenceno | 10 | 8 | 20 |
| Tolueno | 10 | 2 | 80 |
| Benceno | 6 | 3 | 53 |

**Tabla 10.6.2** (p. 507). Ganancia de SRWS hacia atrás según polarizaciones, relativa al caso lineal
paralelo (la nota remite a "Eqs. (10.5.14)", errata por (10.6.14)). Las flechas en los círculos indican el
sentido de rotación temporal del campo en una posición fija.

| Láser | Stokes | Ganancia relativa |
|---|---|---|
| lineal | lineal paralelo | 1 |
| lineal | lineal perpendicular | 3/4 |
| circular | circular, sentido de rotación opuesto | 3/2 |
| circular | circular, mismo sentido de rotación | 1/6 |

**Tabla 10.6.3** (p. 507). Polarización Stokes de ganancia máxima en SRWS hacia atrás: lineal → lineal
paralela; elíptica → elíptica (más redonda, inclinada y con sentido de rotación opuesto); circular →
circular con sentido opuesto.

**Otros números:** sección eficaz Raman espontánea por unidad de volumen $\sim10^{-6}$ cm⁻¹ en materia
condensada (1 parte en $10^6$ por cm); SRS convierte ≥10 % del láser; umbral de dispersión estimulada
observable $g I_L L\simeq25$ (p. 506).

---

## Problemas al final del capítulo (p. 508)

1. *Estimation of the properties of stimulated Raman scattering.* Haciendo suposiciones razonables
   sobre el valor del parámetro $(d\alpha/dq)$, estimar en orden de magnitud el factor de ganancia de la
   dispersión Raman estimulada para materia condensada y comparar con los valores medidos de la
   Tabla 10.2.1.
2. *Polarization properties of stimulated Rayleigh-wing scattering.* Siguiendo la prescripción descrita
   en el primer párrafo completo después de la ec. (10.6.16), verificar que las entradas de la
   Tabla 10.6.2 son correctas.

## Referencias principales (p. 508–509)

- *SRS:* Bloembergen y Shen (1964) PRL 12, 504; Bloembergen (1967) Am. J. Phys. 35, 989; Boyd (1983)
  *Radiometry and the Detection of Optical Radiation*; Eckhardt *et al.* (1962) PRL 9; Garmire, Pandarese y
  Townes (1963) PRL 11, 160; Hellwarth (1963) Phys. Rev. 130, 1850; Kaiser y Maier (1972), *Laser Handbook*;
  Penzkofer, Laubereau y Kaiser (1979) Prog. Quantum Electron. 6, 55; Raymer y Mostowski (1981) PRA 24, 1980;
  Raymer y Walmsley (1990) Progress in Optics 28; Simon y Tittel (1994); Terhune (1963); Woodbury y Ng
  (1962) Proc. IRE 50, 2367.
- *Propiedades tensoriales de SRS:* Happer (1972) RMP 44, 169; Holmes y Flusberg (1988) PRA 37, 1588;
  Landau y Lifshitz (1960); Pritchett *et al.* (1999) J. Mod. Opt. 46, 949; Venkin *et al.* (1985).
- *CARS:* Levenson, Flytzanis y Bloembergen (1972) PRB 6, 3962; Levenson y Bloembergen (1974) PRB 10, 4447;
  Levenson y Kano (1988) *Introduction to Nonlinear Laser Spectroscopy*; Maker y Terhune (1965) Phys. Rev.
  137, A801; Volkmer (2005) J. Phys. D 38, R59.
- *SRWS:* Bloembergen y Lallemand (1966) PRL 16, 81; Chiao y Godine (1969) Phys. Rev. 185, 430; Chiao, Kelley y
  Garmire (1966) PRL 17, 1158; Cho *et al.* (1967); Denariez y Bret (1968); Foltz *et al.* (1968); Kudriavtseva
  *et al.* (1978); Mash *et al.* (1965); Miller, Malcuit y Boyd (1990) Opt. Lett. 15, 1189; Zel'dovich y
  Yakovleva (1980).

---

## Relación con Óptica No Lineal

- **Programa del curso.** El cap. 10 no está entre los temas 4–6 explícitos (Boyd caps. 1, 2, 4.1–4.2,
  7.1–7.2), pero usa directamente sus herramientas: $\chi^{(3)}$ y factores de degeneración (cap. 1: el 6 de
  $\chi_R$ y el 3 de $\chi_F$), ecuaciones de amplitud acoplada con SVA (cap. 2), índice no lineal y orientación
  molecular (cap. 4: (4.1.18), (4.4.26) en §10.6) y conjugación de fase (cap. 7.2, para SRWS). La relación
  $\chi_R(\omega_a)=\chi_R(\omega_S)^*$ y el signo de $\text{Im}\,\chi^{(3)}$ ilustran bien la parte imaginaria de $\chi^{(3)}$ como
  ganancia/pérdida (paralelo a la Raman gain de Saleh §21.3).
- **Proyecto final (supercontinuo en guías de SiN y Si).** La SRS es uno de los mecanismos de
  ensanchamiento en supercontinuo (autodesplazamiento de frecuencia de solitones, generación Stokes
  en cascada). La Tabla 10.2.1 da $G/I_L\approx0.8$ m/TW (si "08" es 0.8) para SiO₂ con desplazamiento
  de 467 cm⁻¹ (≈ 14 THz), del orden de los $g_R\sim10^{-13}$ m/W de la sílice. En Si cristalino la línea
  Raman (≈ 15.6 THz, estrecha) es mucho más fuerte, mientras que en Si₃N₄ amorfo la ganancia Raman es
  débil y ancha; esto debe sacarse de la bibliografía del proyecto, no de esta tabla. La supresión de
  ganancia por acople Stokes–anti-Stokes con $\Delta k\approx0$ (§10.4.3) es relevante en guías con
  dispersión diseñada cerca de cero (ver literatura de "Raman gain suppression" en fibras/guías).
  Las ecuaciones (10.4.1)–(10.4.9) son además el modelo genérico de mezcla de cuatro ondas con bombeo
  constante (ganancia paramétrica $g=[\kappa_1\kappa_2^*-(\Delta k/2)^2]^{1/2}$, (10.4.26)) que se usa para FWM/MI en
  guías.

---

## Erratas y dudas de lectura (resumen)

1. Ec. sin número de p. 483: se lee $-\omega^2q(\Omega)-2i\omega\gamma q(\Omega)$; por consistencia con (10.3.12) debe ser $\Omega$.
2. (10.3.34), p. 486: denominador $\omega_v^2-(\omega_L-\omega_a)^2+2i(\omega_L-\omega_S)\gamma$; numéricamente igual, pero debería
   ser $(\omega_L-\omega_S)^2$.
3. p. 488: "experiences lose" → *loss*.
4. (10.4.17b), p. 491: lado izquierdo con $+i\Delta k/2$; por consistencia debe ser $-i\Delta k/2$. La ec. que sigue no
   tiene número (sería la 10.4.18).
5. (10.4.29), p. 494: $g_-=-\alpha_1^*$; de (10.4.9) resulta $g_-=-\alpha_1$, que es lo usado en (10.4.31b). En (10.4.31a)
   se lee $e^{-\alpha_2^*(z)}$ por $e^{-\alpha_2^*z}$.
6. p. 495: "set the factor $n_S\omega_L/n_a\omega_S$ equal to unity"; debe ser $n_S\omega_a/n_a\omega_S$.
7. (10.4.38), p. 496: falta el exponente $1/2$ en $(1-4i\alpha_S/\Delta k)$.
8. (10.4.39a), p. 496: $-2-i\Delta k/\alpha_S\simeq i\Delta k/\alpha_S$; el signo del término dominante no coincide (duda).
9. (10.4.45), p. 498: lado izquierdo "$g(\Omega)$" → $q(\Omega)$; el texto escribe $q(\omega)$.
10. (10.6.7), p. 503: $e^{iqz-\Omega t}$ → $e^{i(qz-\Omega t)}$. Fig. 10.6.3 rotula $q=k_L-k_S$ frente a (10.6.8) $q=k_L+k_S$.
11. p. 504: "estimated Raleigh-wing scattering" → *stimulated Rayleigh-wing*.
12. Tabla 10.6.2: la nota remite a "Eqs. (10.5.14)" → (10.6.14).
13. Tabla 10.2.1: "NiNbO₃" es casi seguro LiNbO₃; la ganancia de SiO₂ se lee "08" (probablemente 0.8);
    el valor de O₂ líquido (145 ± 40) está impreso encima del rótulo de unidades (m/TW); las unidades de
    la sección eficaz se leen "$10^{-6}$ m⁻¹ sec⁻¹" (dimensionalmente sería m⁻¹ sr⁻¹; probable errata).
