# Capítulo 3 — Quantum-Mechanical Theory of the Nonlinear Optical Susceptibility (Boyd, 3.ª ed.)

Páginas del libro 135–206 (PDF 153–224; p. 134 del libro está en blanco y el cap. 4 empieza en p. 207). Leído el 2026-11-14.

Fuente: R. W. Boyd, *Nonlinear Optics*, 3.ª ed., Academic Press, 2008, cap. 3.
Las citas de página son páginas del libro (sumar 18 para la página del PDF).

Convención (SI, la del libro): $\tilde E(t)=\sum_p \mathbf E(\omega_p)e^{-i\omega_p t}$ (suma sobre frecuencias
positivas y negativas, $\mathbf E(-\omega)=\mathbf E(\omega)^*$), equivalente a $\tilde E=Ee^{-i\omega t}+\text{c.c.}$;
$P_i(\omega_\sigma)=\epsilon_0\sum\chi^{(n)}_{i\dots}E\cdots E$; $I=2n\epsilon_0c|E|^2$. Frecuencias de transición
complejas $\omega_{mg}=(E_m-E_g)/\hbar-i\Gamma_m/2$ en §3.2; en §3.5–3.8 se usa
$\omega_{nm}=(E_n-E_m)/\hbar$ real y amortiguamiento $\gamma_{nm}$ explícito.

---

## Resumen del capítulo

Capítulo de fundamentos microscópicos: deduce, con mecánica cuántica, expresiones explícitas
("suma sobre estados") para $\chi^{(1)}$, $\chi^{(2)}$ y $\chi^{(3)}$ en función de frecuencias de transición
$\omega_{mg}$, momentos dipolares de transición $\boldsymbol\mu_{mg}$, poblaciones y tasas de amortiguamiento. Primero (§3.2)
con teoría de perturbaciones de la función de onda (Schrödinger, interacción dipolar $\hat V=-\hat{\boldsymbol\mu}\cdot\tilde{\mathbf E}$),
válida para respuesta no resonante: $\chi^{(2)}$ con 6 términos y $\chi^{(3)}$ con 24, que en el límite sin
pérdidas se escriben con el operador de permutación total $\mathcal P_F$, lo que demuestra la simetría de
permutación total; se ilustra con THG en vapor de sodio (Miles y Harris, 1973) y reglas de selección
$\Delta l=\pm1$. Luego (§3.3–3.4) introduce la matriz densidad $\rho_{nm}=\overline{C_m^*C_n}$, su ecuación de
movimiento $\dot\rho=-\frac i\hbar[\hat H,\hat\rho]$ con amortiguamiento fenomenológico ($\gamma_{nm}=\frac12(\Gamma_n+\Gamma_m)+\gamma^{(\rm col)}_{nm}$)
y su solución perturbativa orden por orden. Con ella recalcula (§3.5) $\chi^{(1)}$ —proporcional a la
diferencia de poblaciones, lorentziana de FWHM $2\gamma$—, conecta con fuerza de oscilador, modelo de
Lorentz, índice, coeficiente de absorción, polarizabilidad y sección eficaz máxima $3\lambda^2/2\pi$; deduce
(§3.6) $\chi^{(2)}$ con ocho términos (que se reducen a seis lejos de resonancia y coinciden con §3.2), su
estructura de resonancias y los diagramas de Feynman de doble lado; y (§3.7) $\chi^{(3)}$ con 48 términos,
con la noción de resonancias inducidas por colisiones. La §3.8 trata la transparencia inducida
electromagnéticamente: un campo de acoplamiento fuerte $\Omega_s$ abre una ventana de transparencia en
una transición resonante (doblete de Autler–Townes o hueco angosto) mientras $\chi^{(3)}$ de suma de
frecuencias sigue siendo grande. La §3.9 incorpora el campo local de Lorentz: $E_{\rm loc}=E+P/3\epsilon_0$,
ley de Lorentz–Lorenz, polarización fuente no lineal $P^{\rm NLS}=\frac{\epsilon+2}{3}P^{\rm NL}$ y factores de realce
$\mathcal L^{(2)}$, $\mathcal L^{(3)}$ (productos de $(\epsilon^{(1)}(\omega_i)+2)/3$), también desde el enfoque de Mizrahi y Sipe.
Cierra con 9 problemas.

---

## Secciones

### 3.1 Introducción (p. 135)

Motivación triple para calcular $\chi^{(n)}$ con mecánica cuántica: (1) muestra la forma funcional
de la susceptibilidad y su dependencia de parámetros materiales (momentos dipolares de transición,
niveles de energía); (2) muestra sus simetrías internas; (3) permite predicciones numéricas, muy
fiables en vapores atómicos (parámetros conocidos con precisión). Como los niveles de átomos libres
son muy angostos (en sólidos son bandas anchas), se logran $\chi$ enormes por **realce resonante**:
si un nivel atómico real casi coincide con uno virtual del proceso, el acoplamiento es fuerte.

- Fig. 3.1.1 (p. 136): THG con niveles virtuales (a) y con niveles reales indicados (b).
- Fig. 3.1.2 (p. 136): tres estrategias de realce de THG: resonancia de uno (a), dos (b) o tres
  fotones (c). Las fórmulas del capítulo muestran que las tres son igual de eficaces para aumentar
  $\chi^{(3)}$, pero se prefiere **(b), resonancia de dos fotones**, porque en (a) el haz incidente
  sufre absorción lineal y en (c) la sufre el armónico generado; en (b) no hay absorción lineal que
  limite la eficiencia.

### 3.2 Cálculo de la susceptibilidad no lineal con la ecuación de Schrödinger (p. 137)

Teoría de perturbaciones de la función de onda atómica. Da predicciones precisas de la respuesta
**no resonante** de átomos y moléculas; los procesos de relajación (importantes cerca de resonancia)
no se describen bien así, y se tratan después con la matriz densidad (más general pero más
engorrosa). Ecuación de Schrödinger y Hamiltoniano:

$$i\hbar\frac{\partial\psi}{\partial t}=\hat H\psi \quad (3.2.1),\qquad \hat H=\hat H_0+\hat V(t)\quad(3.2.2),\qquad \hat V(t)=-\hat{\boldsymbol\mu}\cdot\tilde{\mathbf E}(t)\quad(3.2.3),\ \text{p. 137}$$

con $\hat{\boldsymbol\mu}=-e\hat{\mathbf r}$ el operador momento dipolar eléctrico ($-e$ carga del electrón). El
acento circunflejo indica operador; se trabaja en la representación de coordenadas.

#### 3.2.1 Estados propios de energía (p. 138)

Sin campo, estados estacionarios
$\psi_n(\mathbf r,t)=u_n(\mathbf r)e^{-i\omega_n t}$ (3.2.4a), con $\hat H_0u_n=E_nu_n$ (3.2.4b), $E_n=\hbar\omega_n$;
base completa y ortonormal $\int u_m^*u_n\,d^3r=\delta_{mn}$ (3.2.5), p. 138.

#### 3.2.2 Solución perturbativa de la ecuación de Schrödinger (p. 138)

Se sustituye $\hat H=\hat H_0+\lambda\hat V(t)$ (3.2.6), $0\le\lambda\le1$ ($\lambda=1$ caso físico), y se busca
$\psi=\psi^{(0)}+\lambda\psi^{(1)}+\lambda^2\psi^{(2)}+\cdots$ (3.2.7); $\psi^{(N)}$ es de orden $N$ en $V$. Igualando
potencias de $\lambda$ (p. 139):

$$i\hbar\frac{\partial\psi^{(0)}}{\partial t}=\hat H_0\psi^{(0)}\ (3.2.8a),\qquad i\hbar\frac{\partial\psi^{(N)}}{\partial t}=\hat H_0\psi^{(N)}+\hat V\psi^{(N-1)},\ N=1,2,3,\dots\ (3.2.8b)$$

Átomo inicialmente en el estado $g$ (normalmente el fundamental): $\psi^{(0)}=u_g(\mathbf r)e^{-iE_gt/\hbar}$ (3.2.9).
Desarrollo $\psi^{(N)}(\mathbf r,t)=\sum_l a_l^{(N)}(t)u_l(\mathbf r)e^{-i\omega_lt}$ (3.2.10), donde $a_l^{(N)}$ es la amplitud
de probabilidad, a orden $N$, de estar en $l$. Sustituyendo:
$i\hbar\sum_l\dot a_l^{(N)}u_le^{-i\omega_lt}=\sum_la_l^{(N-1)}\hat Vu_le^{-i\omega_lt}$ (3.2.11); multiplicando por $u_m^*$ e
integrando:

$$\dot a_m^{(N)}(t)=(i\hbar)^{-1}\sum_l a_l^{(N-1)}(t)V_{ml}(t)e^{i\omega_{ml}t}\quad(3.2.12),\qquad V_{ml}\equiv\langle u_m|\hat V|u_l\rangle=\int u_m^*\hat Vu_l\,d^3r\quad(3.2.13)$$

con $\omega_{ml}\equiv\omega_m-\omega_l$. Integración directa (p. 140):

$$a_m^{(N)}(t)=(i\hbar)^{-1}\sum_l\int_{-\infty}^{t}dt'\,V_{ml}(t')a_l^{(N-1)}(t')e^{i\omega_{ml}t'}\quad(3.2.14)$$

**Primer orden:** $a_l^{(0)}=\delta_{lg}$; campo como suma discreta de componentes de frecuencia positiva y
negativa, $\tilde{\mathbf E}(t)=\sum_p\mathbf E(\omega_p)e^{-i\omega_pt}$ (3.2.15), de modo que
$V_{ml}(t')=-\sum_p\boldsymbol\mu_{ml}\cdot\mathbf E(\omega_p)e^{-i\omega_pt'}$, con $\boldsymbol\mu_{ml}=\int u_m^*\hat{\boldsymbol\mu}u_l\,d^3r$ el
**momento dipolar de transición**. Suponiendo que la contribución del límite inferior se anula
(encendido adiabático):

$$a_m^{(1)}(t)=\frac1\hbar\sum_p\frac{\boldsymbol\mu_{mg}\cdot\mathbf E(\omega_p)}{\omega_{mg}-\omega_p}e^{i(\omega_{mg}-\omega_p)t}\quad(3.2.16)$$

$$a_n^{(2)}(t)=\frac1{\hbar^2}\sum_{pq}\sum_m\frac{[\boldsymbol\mu_{nm}\cdot\mathbf E(\omega_q)][\boldsymbol\mu_{mg}\cdot\mathbf E(\omega_p)]}{(\omega_{ng}-\omega_p-\omega_q)(\omega_{mg}-\omega_p)}e^{i(\omega_{ng}-\omega_p-\omega_q)t}\quad(3.2.17)$$

$$a_\nu^{(3)}(t)=\frac1{\hbar^3}\sum_{pqr}\sum_{mn}\frac{[\boldsymbol\mu_{\nu n}\cdot\mathbf E(\omega_r)][\boldsymbol\mu_{nm}\cdot\mathbf E(\omega_q)][\boldsymbol\mu_{mg}\cdot\mathbf E(\omega_p)]}{(\omega_{\nu g}-\omega_p-\omega_q-\omega_r)(\omega_{ng}-\omega_p-\omega_q)(\omega_{mg}-\omega_p)}e^{i(\omega_{\nu g}-\omega_p-\omega_q-\omega_r)t}\quad(3.2.18)$$

#### 3.2.3 Susceptibilidad lineal (p. 141)

Valor esperado del dipolo $\langle\tilde{\mathbf p}\rangle=\langle\psi|\hat{\boldsymbol\mu}|\psi\rangle$ (3.2.19) con $\lambda=1$; la parte lineal es
$\langle\tilde{\mathbf p}^{(1)}\rangle=\langle\psi^{(0)}|\hat{\boldsymbol\mu}|\psi^{(1)}\rangle+\langle\psi^{(1)}|\hat{\boldsymbol\mu}|\psi^{(0)}\rangle$ (3.2.20). Resultado:

$$\langle\tilde{\mathbf p}^{(1)}\rangle=\frac1\hbar\sum_p\sum_m\left(\frac{\boldsymbol\mu_{gm}[\boldsymbol\mu_{mg}\cdot\mathbf E(\omega_p)]}{\omega_{mg}-\omega_p}e^{-i\omega_pt}+\frac{[\boldsymbol\mu_{mg}\cdot\mathbf E(\omega_p)]^*\boldsymbol\mu_{mg}}{\omega_{mg}^*-\omega_p}e^{i\omega_pt}\right)\quad(3.2.21)$$

Se permite formalmente $\omega_{mg}$ complejo: **forma cruda de incluir amortiguamiento**,
$\omega_{mg}=(E_m-E_g)/\hbar-i\Gamma_m/2$, $\Gamma_m$ tasa de decaimiento de población del nivel superior. No es
del todo aceptable: no describe la cascada de población entre estados excitados ni el desfase sin
transferencia de población; sirve solo como indicación. Cambiando $\omega_p\to-\omega_p$ en el segundo término:

$$\langle\tilde{\mathbf p}^{(1)}\rangle=\frac1\hbar\sum_p\sum_m\left(\frac{\boldsymbol\mu_{gm}[\boldsymbol\mu_{mg}\cdot\mathbf E(\omega_p)]}{\omega_{mg}-\omega_p}+\frac{[\boldsymbol\mu_{gm}\cdot\mathbf E(\omega_p)]\boldsymbol\mu_{mg}}{\omega_{mg}^*+\omega_p}\right)e^{-i\omega_pt}\quad(3.2.22)$$

Con $\tilde{\mathbf P}^{(1)}=N\langle\tilde{\mathbf p}^{(1)}\rangle$ ($N$ densidad de átomos), $\tilde{\mathbf P}^{(1)}=\sum_p\mathbf P^{(1)}(\omega_p)e^{-i\omega_pt}$ y
$P_i^{(1)}(\omega_p)=\epsilon_0\sum_j\chi^{(1)}_{ij}E_j(\omega_p)$ (p. 142):

$$\chi^{(1)}_{ij}(\omega_p)=\frac{N}{\epsilon_0\hbar}\sum_m\left(\frac{\mu^i_{gm}\mu^j_{mg}}{\omega_{mg}-\omega_p}+\frac{\mu^j_{gm}\mu^i_{mg}}{\omega_{mg}^*+\omega_p}\right)\quad(3.2.23)$$

Primer término: **resonante**; segundo: **antirresonante** (Fig. 3.2.1, p. 142: dónde tendría que
estar el nivel $m$ para que cada término resuene; si $g$ es el fundamental el segundo nunca resuena).

#### 3.2.4 Susceptibilidad de segundo orden (p. 142)

$\langle\tilde{\mathbf p}^{(2)}\rangle=\langle\psi^{(0)}|\hat{\boldsymbol\mu}|\psi^{(2)}\rangle+\langle\psi^{(1)}|\hat{\boldsymbol\mu}|\psi^{(1)}\rangle+\langle\psi^{(2)}|\hat{\boldsymbol\mu}|\psi^{(0)}\rangle$ (3.2.24). Explícitamente
(3.2.25), p. 142, tres términos con dependencias $e^{-i(\omega_p+\omega_q)t}$, $e^{-i(\omega_p-\omega_q)t}$ y $e^{+i(\omega_p+\omega_q)t}$
(ver erratas abajo). Reemplazando $\omega_q\to-\omega_q$ en el 2.º y $\omega_q\to-\omega_q,\ \omega_p\to-\omega_p$ en el 3.º (válido
porque se suma sobre todas las frecuencias), todos los términos quedan con la misma dependencia (p. 143):

$$\langle\tilde{\mathbf p}^{(2)}\rangle=\frac1{\hbar^2}\sum_{pq}\sum_{mn}\Bigg(\frac{\boldsymbol\mu_{gn}[\boldsymbol\mu_{nm}\cdot\mathbf E(\omega_q)][\boldsymbol\mu_{mg}\cdot\mathbf E(\omega_p)]}{(\omega_{ng}-\omega_p-\omega_q)(\omega_{mg}-\omega_p)}+\frac{[\boldsymbol\mu_{gn}\cdot\mathbf E(\omega_q)]\boldsymbol\mu_{nm}[\boldsymbol\mu_{mg}\cdot\mathbf E(\omega_p)]}{(\omega_{ng}^*+\omega_q)(\omega_{mg}-\omega_p)}+\frac{[\boldsymbol\mu_{gn}\cdot\mathbf E(\omega_q)][\boldsymbol\mu_{nm}\cdot\mathbf E(\omega_p)]\boldsymbol\mu_{mg}}{(\omega_{ng}^*+\omega_q)(\omega_{mg}^*+\omega_p+\omega_q)}\Bigg)e^{-i(\omega_p+\omega_q)t}\quad(3.2.26)$$

Con $\tilde{\mathbf P}^{(2)}=N\langle\tilde{\mathbf p}^{(2)}\rangle=\sum_r\mathbf P^{(2)}(\omega_r)e^{-i\omega_rt}$ y la definición estándar (1.3.13)
$P_i^{(2)}=\epsilon_0\sum_{jk}\sum_{(pq)}\chi^{(2)}_{ijk}(\omega_p+\omega_q,\omega_q,\omega_p)E_j(\omega_q)E_k(\omega_p)$:

$$\chi^{(2)}_{ijk}(\omega_p+\omega_q,\omega_q,\omega_p)=\frac{N}{\epsilon_0\hbar^2}\mathcal P_I\sum_{mn}\left(\frac{\mu^i_{gn}\mu^j_{nm}\mu^k_{mg}}{(\omega_{ng}-\omega_p-\omega_q)(\omega_{mg}-\omega_p)}+\frac{\mu^j_{gn}\mu^i_{nm}\mu^k_{mg}}{(\omega_{ng}^*+\omega_q)(\omega_{mg}-\omega_p)}+\frac{\mu^j_{gn}\mu^k_{nm}\mu^i_{mg}}{(\omega_{ng}^*+\omega_q)(\omega_{mg}^*+\omega_p+\omega_q)}\right)\quad(3.2.27)$$

$\mathcal P_I$ = **operador de permutación intrínseca**: promediar sobre las dos permutaciones de $\omega_p,\omega_q$
(permutando simultáneamente $j,k$); garantiza la simetría de permutación intrínseca (1.4.52), (1.5.6).
Fig. 3.2.2 (p. 144): estructura resonante de los tres términos (posiciones de $m$ y $n$ necesarias
para resonancia: el 1.º resuena con $m$ a $\omega_p$ y $n$ a $\omega_p+\omega_q$; el 2.º y 3.º involucran niveles
"por debajo" de $g$, antirresonantes si $g$ es el fundamental).

Es una expresión de **suma sobre estados** (*sum-over-states*); en realidad tiene seis términos (tres
explícitos gracias a $\mathcal P_I$). Para excitación muy **no resonante** ($\omega_{mg},\omega_{ng}$ reales):

$$\chi^{(2)}_{ijk}(\omega_\sigma,\omega_q,\omega_p)=\frac{N}{\epsilon_0\hbar^2}\mathcal P_F\sum_{mn}\frac{\mu^i_{gn}\mu^j_{nm}\mu^k_{mg}}{(\omega_{ng}-\omega_\sigma)(\omega_{mg}-\omega_p)}\quad(3.2.28),\ \text{p. 144}$$

con $\omega_\sigma=\omega_p+\omega_q$ y $\mathcal P_F$ el **operador de permutación total**: sumar sobre todas las permutaciones
de $\omega_p,\omega_q,-\omega_\sigma$ (con los índices cartesianos), y dividir por el número de permutaciones de las
frecuencias de entrada. Las seis permutaciones: $(-\omega_\sigma,\omega_q,\omega_p)\to(-\omega_\sigma,\omega_p,\omega_q)$, $(\omega_q,-\omega_\sigma,\omega_p)$,
$(\omega_q,\omega_p,-\omega_\sigma)$, $(\omega_p,-\omega_\sigma,\omega_q)$, $(\omega_p,\omega_q,-\omega_\sigma)$. Esto **prueba** la afirmación de §1.5: la
$\chi^{(2)}$ de un medio sin pérdidas tiene simetría de permutación total (p. 145).

#### 3.2.5 Susceptibilidad de tercer orden (p. 145)

$\langle\tilde{\mathbf p}^{(3)}\rangle=\langle\psi^{(0)}|\hat\mu|\psi^{(3)}\rangle+\langle\psi^{(1)}|\hat\mu|\psi^{(2)}\rangle+\langle\psi^{(2)}|\hat\mu|\psi^{(1)}\rangle+\langle\psi^{(3)}|\hat\mu|\psi^{(0)}\rangle$ (3.2.29).
La forma explícita (3.2.30), p. 145, tiene cuatro términos con dependencias
$e^{-i(\omega_p+\omega_q+\omega_r)t}$, $e^{-i(\omega_p+\omega_q-\omega_r)t}$, $e^{-i(\omega_p-\omega_q-\omega_r)t}$, $e^{+i(\omega_p+\omega_q+\omega_r)t}$. Cambiando de
signo las frecuencias de los campos conjugados:

$$\langle\tilde{\mathbf p}^{(3)}\rangle=\frac1{\hbar^3}\sum_{pqr}\sum_{mn\nu}\Bigg(\frac{\boldsymbol\mu_{g\nu}[\boldsymbol\mu_{\nu n}\cdot\mathbf E(\omega_r)][\boldsymbol\mu_{nm}\cdot\mathbf E(\omega_q)][\boldsymbol\mu_{mg}\cdot\mathbf E(\omega_p)]}{(\omega_{\nu g}-\omega_r-\omega_q-\omega_p)(\omega_{ng}-\omega_q-\omega_p)(\omega_{mg}-\omega_p)}+\frac{[\boldsymbol\mu_{g\nu}\cdot\mathbf E(\omega_r)]\boldsymbol\mu_{\nu n}[\boldsymbol\mu_{nm}\cdot\mathbf E(\omega_q)][\boldsymbol\mu_{mg}\cdot\mathbf E(\omega_p)]}{(\omega_{\nu g}^*+\omega_r)(\omega_{ng}-\omega_q-\omega_p)(\omega_{mg}-\omega_p)}$$
$$+\frac{[\boldsymbol\mu_{g\nu}\cdot\mathbf E(\omega_r)][\boldsymbol\mu_{\nu n}\cdot\mathbf E(\omega_q)]\boldsymbol\mu_{nm}[\boldsymbol\mu_{mg}\cdot\mathbf E(\omega_p)]}{(\omega_{\nu g}^*+\omega_r)(\omega_{ng}^*+\omega_r+\omega_q)(\omega_{mg}-\omega_p)}+\frac{[\boldsymbol\mu_{g\nu}\cdot\mathbf E(\omega_r)][\boldsymbol\mu_{\nu n}\cdot\mathbf E(\omega_q)][\boldsymbol\mu_{nm}\cdot\mathbf E(\omega_p)]\boldsymbol\mu_{mg}}{(\omega_{\nu g}^*+\omega_r)(\omega_{ng}^*+\omega_r+\omega_q)(\omega_{mg}^*+\omega_r+\omega_q+\omega_p)}\Bigg)e^{-i(\omega_p+\omega_q+\omega_r)t}\quad(3.2.31),\ \text{p. 146}$$

Con la definición (1.3.21), $P_k(\omega_p+\omega_q+\omega_r)=\epsilon_0\sum_{hij}\sum_{(pqr)}\chi^{(3)}_{kjih}(\omega_\sigma,\omega_r,\omega_q,\omega_p)E_j(\omega_r)E_i(\omega_q)E_h(\omega_p)$:

$$\chi^{(3)}_{kjih}(\omega_\sigma,\omega_r,\omega_q,\omega_p)=\frac{N}{\epsilon_0\hbar^3}\mathcal P_I\sum_{mn\nu}\Bigg[\frac{\mu^k_{g\nu}\mu^j_{\nu n}\mu^i_{nm}\mu^h_{mg}}{(\omega_{\nu g}-\omega_r-\omega_q-\omega_p)(\omega_{ng}-\omega_q-\omega_p)(\omega_{mg}-\omega_p)}+\frac{\mu^j_{g\nu}\mu^k_{\nu n}\mu^i_{nm}\mu^h_{mg}}{(\omega_{\nu g}^*+\omega_r)(\omega_{ng}-\omega_q-\omega_p)(\omega_{mg}-\omega_p)}$$
$$+\frac{\mu^j_{g\nu}\mu^i_{\nu n}\mu^k_{nm}\mu^h_{mg}}{(\omega_{\nu g}^*+\omega_r)(\omega_{ng}^*+\omega_r+\omega_q)(\omega_{mg}-\omega_p)}+\frac{\mu^j_{g\nu}\mu^i_{\nu n}\mu^h_{nm}\mu^k_{mg}}{(\omega_{\nu g}^*+\omega_r)(\omega_{ng}^*+\omega_r+\omega_q)(\omega_{mg}^*+\omega_r+\omega_q+\omega_p)}\Bigg]\quad(3.2.32)$$

$\mathcal P_I$ ahora promedia sobre las permutaciones de $\omega_p,\omega_q,\omega_r$. La expresión completa tiene **24
términos**, cuatro explícitos. Fig. 3.2.3 (p. 147): posiciones de las resonancias de cada término
(el primero resuena con $m,n,\nu$ en $\omega_p$, $\omega_p+\omega_q$, $\omega_p+\omega_q+\omega_r$). Caso muy no resonante
(se ignoran las partes imaginarias de $\omega_{lg}=(E_l-E_g)/\hbar-i\Gamma_l/2$):

$$\chi^{(3)}_{kjih}(\omega_\sigma,\omega_r,\omega_q,\omega_p)=\frac{N}{\epsilon_0\hbar^3}\mathcal P_F\sum_{mn\nu}\frac{\mu^k_{g\nu}\mu^j_{\nu n}\mu^i_{nm}\mu^h_{mg}}{(\omega_{\nu g}-\omega_\sigma)(\omega_{ng}-\omega_q-\omega_p)(\omega_{mg}-\omega_p)}\quad(3.2.33),\ \text{p. 147}$$

con $\omega_\sigma=\omega_p+\omega_q+\omega_r$.

#### 3.2.6 Generación de tercer armónico en vapores de metales alcalinos (p. 147)

Ejemplo de (3.2.33), siguiendo a Miles y Harris (1973): THG en vapor de **sodio**. Luz linealmente
polarizada en $z$ ⇒ $P^{\rm NL}$ solo tiene componente $z$ y se suprime la naturaleza tensorial.
$\tilde E(\mathbf r,t)=E_1(\mathbf r)e^{-i\omega t}+\text{c.c.}$ (3.2.34); $\tilde P(\mathbf r,t)=P_3(\mathbf r)e^{-3i\omega t}+\text{c.c.}$ (3.2.35),
$P_3(\mathbf r)=\epsilon_0\chi^{(3)}(3\omega)E_1^3$ (3.2.36), p. 148, con $\chi^{(3)}(3\omega)\equiv\chi^{(3)}(3\omega=\omega+\omega+\omega)$. Sin amortiguamiento:

$$\chi^{(3)}(3\omega)=\frac{N}{\epsilon_0\hbar^3}\sum_{mn\nu}\mu_{g\nu}\mu_{\nu n}\mu_{nm}\mu_{mg}\Bigg[\frac1{(\omega_{\nu g}-3\omega)(\omega_{ng}-2\omega)(\omega_{mg}-\omega)}+\frac1{(\omega_{\nu g}+\omega)(\omega_{ng}-2\omega)(\omega_{mg}-\omega)}$$
$$+\frac1{(\omega_{\nu g}+\omega)(\omega_{ng}+2\omega)(\omega_{mg}-\omega)}+\frac1{(\omega_{\nu g}+\omega)(\omega_{ng}+2\omega)(\omega_{mg}+3\omega)}\Bigg]\quad(3.2.37)$$

- Fig. 3.2.4 (p. 148): (a) diagrama de niveles del Na (3s fundamental en 0; 3p ≈ 2.1 eV; 4s ≈ 3.2 eV;
  3d ≈ 3.6 eV; 4p ≈ 3.75 eV; 5s, 4d, 4f ≈ 4.1–4.3 eV; 6s, 5p, 5d, 5f… hasta el límite de ionización
  ≈ 5.1 eV); (b) THG con niveles $m,n,\nu$.
- Solo el primer término puede ser totalmente resonante ($\omega\approx\omega_{mg}$, $2\omega\approx\omega_{ng}$, $3\omega\approx\omega_{\nu g}$).
  **Regla de selección dipolar** $\Delta l=\pm1$: como $g$ es un estado $s$, $m$ debe ser $p$; $n$ debe
  ser $s$ o $d$; $\nu$ debe ser $p$. Fig. 3.2.5 (p. 149): los dos esquemas de acoplamiento
  $s\to p\to s\to p\to s$ y $s\to p\to d\to p\to s$.
- Fig. 3.2.6 (p. 150): $|\chi^{(3)}|/N$ (esu) vs. longitud de onda incidente 0.55–2.6 μm (Miles y Harris,
  1973): fondo $\sim10^{-34}$ esu, picos hasta $\gtrsim10^{-32}$ esu en resonancias etiquetadas 3p(3ω),
  4p(3ω), 5p(3ω), 6p(3ω), 4s(2ω), 3d(2ω), 5s(2ω), 4d(2ω), 3p(ω); p. ej. 3p(3ω) es una resonancia de
  tres fotones con el nivel 3p. Hay mínimos profundos (interferencia destructiva) cerca de 0.6–0.8 μm.
  Miles y Harris confirmaron experimentalmente.
- Los vapores atómicos son centrosimétricos (sin respuesta de segundo orden), pero un campo eléctrico
  estático rompe la simetría de inversión y permite p. ej. SFG; efecto grande si se excitan niveles
  de Rydberg (Boyd y Xiang, 1982; experimentos de Gauthier et al., 1983 y Boyd et al., 1984).

### 3.3 Formulación de la matriz densidad (p. 150)

Las §3.3–3.7 usan matriz densidad porque permite tratar efectos como el **ensanchamiento colisional**,
que la función de onda no describe: el formalismo anterior no da el ancho de las resonancias, ni
cuán precisa debe ser la sintonía, ni cómo cambia la respuesta dentro del ancho de la resonancia.

Repaso: estado $s$ conocido, $i\hbar\partial_t\psi_s=\hat H\psi_s$ (3.3.1), $\hat H=\hat H_0+\hat V(t)$ (3.3.2),
$\psi_s=\sum_nC_n^s(t)u_n(\mathbf r)$ (3.3.3) (aquí las $C_n^s$ incluyen el factor de fase), $\hat H_0u_n=E_nu_n$ (3.3.4),
$\int u_m^*u_n\,d^3r=\delta_{mn}$ (3.3.5). Sustituyendo: $i\hbar\sum_n\dot C_n^su_n=\sum_nC_n^s\hat Hu_n$ (3.3.6), con
$H_{mn}=\int u_m^*\hat Hu_n\,d^3r$ (3.3.7):

$$i\hbar\frac{d}{dt}C_m^s(t)=\sum_nH_{mn}C_n^s(t)\quad(3.3.8),\ \text{p. 152}$$

Valor esperado: $\langle A\rangle=\int\psi_s^*\hat A\psi_s\,d^3r$ (3.3.9) $=\langle\psi_s|\hat A|\psi_s\rangle=\langle s|\hat A|s\rangle$ (3.3.10)
$=\sum_{mn}C_m^{s*}C_n^sA_{mn}$ (3.3.11), con $A_{mn}=\langle u_m|\hat A|u_n\rangle$ (3.3.12), p. 153.

Cuando el estado no se conoce con precisión (p. ej. vapor con colisiones débiles que solo cambian la
fase de cada átomo, imposible de seguir), se describe estadísticamente con $p(s)$, probabilidad
**clásica** (falta de conocimiento, no incertidumbre cuántica):

$$\rho_{nm}=\sum_sp(s)C_m^{s*}C_n^s\quad(3.3.13),\qquad \rho_{nm}=\overline{C_m^*C_n}\quad(3.3.14)$$

(barra = promedio de ensamble). $\rho_{nn}$: probabilidad de estar en $n$; $\rho_{nm}$ ($n\neq m$): "coherencia"
entre $n$ y $m$, no nula solo si el sistema está en una superposición coherente de $n$ y $m$; en
ciertas condiciones es proporcional al dipolo inducido. Valor esperado de ensamble (p. 154):

$$\overline{\langle A\rangle}=\sum_sp(s)\sum_{nm}C_m^{s*}C_n^sA_{mn}\ (3.3.15)=\sum_{nm}\rho_{nm}A_{mn}\ (3.3.16)=\operatorname{tr}(\hat\rho\hat A)\quad(3.3.17)$$

(en adelante se omite la barra). Evolución: $\dot\rho_{nm}=\sum_s\frac{dp(s)}{dt}C_m^{s*}C_n^s+\sum_sp(s)\left(C_m^{s*}\frac{dC_n^s}{dt}+\frac{dC_m^{s*}}{dt}C_n^s\right)$ (3.3.18).
Con $p(s)$ constante y (3.3.8) (p. 155): $C_m^{s*}\dot C_n^s=-\frac i\hbar C_m^{s*}\sum_\nu H_{n\nu}C_\nu^s$,
$C_n^s\dot C_m^{s*}=\frac i\hbar C_n^s\sum_\nu H_{\nu m}C_\nu^{s*}$ (hermiticidad), luego
$\dot\rho_{nm}=\sum_sp(s)\frac i\hbar\sum_\nu(C_n^sC_\nu^{s*}H_{\nu m}-C_m^{s*}C_\nu^sH_{n\nu})$ (3.3.19), es decir

$$\dot\rho_{nm}=\frac i\hbar\sum_\nu(\rho_{n\nu}H_{\nu m}-H_{n\nu}\rho_{\nu m})\ (3.3.20)\ \Rightarrow\ \dot\rho_{nm}=\frac i\hbar(\hat\rho\hat H-\hat H\hat\rho)_{nm}=\frac{-i}\hbar[\hat H,\hat\rho]_{nm}\quad(3.3.21)$$

Interacciones no hamiltonianas (colisiones) cambian $p(s)$; se añaden términos fenomenológicos de
amortiguamiento:

$$\dot\rho_{nm}=\frac{-i}\hbar[\hat H,\hat\rho]_{nm}-\gamma_{nm}(\rho_{nm}-\rho^{(\rm eq)}_{nm})\quad(3.3.22)$$

$\rho_{nm}$ relaja a su valor de equilibrio con tasa $\gamma_{nm}=\gamma_{mn}$, y se supone
$\rho^{(\rm eq)}_{nm}=0$ para $n\neq m$ (3.3.23), p. 156: la excitación térmica (incoherente) puebla estados excitados
pero no crea superposiciones coherentes. Alternativa: amortiguar las coherencias igual, pero dejar
que la población decaiga en cascada de niveles altos a bajos:

$$\dot\rho_{nm}=-i\hbar^{-1}[\hat H,\hat\rho]_{nm}-\gamma_{nm}\rho_{nm},\ n\neq m\quad(3.3.24a)$$
$$\dot\rho_{nn}=-i\hbar^{-1}[\hat H,\hat\rho]_{nn}+\sum_{E_m>E_n}\Gamma_{nm}\rho_{mm}-\sum_{E_m<E_n}\Gamma_{mn}\rho_{nn}\quad(3.3.24b)$$

$\Gamma_{nm}$: tasa por átomo de decaimiento de población de $m$ a $n$. En general

$$\gamma_{nm}=\tfrac12(\Gamma_n+\Gamma_m)+\gamma_{nm}^{(\rm col)}\quad(3.3.25),\qquad \Gamma_n=\sum_{n'(E_{n'}<E_n)}\Gamma_{n'n}\quad(3.3.26)$$

$\gamma^{(\rm col)}_{nm}$: tasa de desfase dipolar por procesos sin transferencia de población (colisiones
elásticas), "proper dephasing rate". Justificación (p. 157): con vida media $\tau_n=1/\Gamma_n$,
$|C_n(t)|^2=|C_n(0)|^2e^{-\Gamma_nt}$ (3.3.27), $C_n(t)=C_n(0)e^{-i\omega_nt}e^{-\Gamma_nt/2}$ (3.3.28), igual para $m$ (3.3.29);
$C_n^*C_m=C_n^*(0)C_m(0)e^{-i\omega_{mn}t}e^{-(\Gamma_n+\Gamma_m)t/2}$ (3.3.30) ⇒ $\gamma_{mn}=\frac12(\Gamma_n+\Gamma_m)$ (3.3.31) (sin colisiones).

#### 3.3.1 Ejemplo: átomo de dos niveles (p. 157)

Solo dos estados $a$, $b$ interactúan (Fig. 3.3.1). $\psi_s=C_a^su_a+C_b^su_b$ (3.3.32);
$\begin{bmatrix}\rho_{aa}&\rho_{ab}\\\rho_{ba}&\rho_{bb}\end{bmatrix}=\begin{bmatrix}\overline{C_aC_a^*}&\overline{C_aC_b^*}\\\overline{C_bC_a^*}&\overline{C_bC_b^*}\end{bmatrix}$ (3.3.33);
$\hat\mu\Rightarrow\begin{bmatrix}0&\mu_{ab}\\\mu_{ba}&0\end{bmatrix}$ (3.3.34), con $\mu_{ij}=\mu_{ji}^*=-e\langle i|\hat z|j\rangle$; diagonales nulos
por paridad definida de $a$, $b$. $\hat\rho\hat\mu=\begin{bmatrix}\rho_{ab}\mu_{ba}&\rho_{aa}\mu_{ab}\\\rho_{bb}\mu_{ba}&\rho_{ba}\mu_{ab}\end{bmatrix}$ (3.3.35), p. 158, y

$$\langle\mu\rangle=\operatorname{tr}(\hat\rho\hat\mu)=\rho_{ab}\mu_{ba}+\rho_{ba}\mu_{ab}\quad(3.3.36)$$

el dipolo depende solo de los elementos fuera de la diagonal. Tratamiento completo en el cap. 6.

### 3.4 Solución perturbativa de la ecuación de movimiento de la matriz densidad (p. 158)

Partida: $\dot\rho_{nm}=\frac{-i}\hbar[\hat H,\hat\rho]_{nm}-\gamma_{nm}(\rho_{nm}-\rho^{(\rm eq)}_{nm})$ (3.4.1), $\hat H=\hat H_0+\hat V(t)$ (3.4.2), con
$\hat V$ débil (elementos de matriz $\ll\langle\hat H_0\rangle$) y en aproximación dipolar eléctrica
$\hat V=-\hat{\boldsymbol\mu}\cdot\tilde{\mathbf E}(t)$ (3.4.3), $\hat{\boldsymbol\mu}=-e\hat{\mathbf r}$. Como $\hat H_0$ es diagonal en la base $u_n$,
$H_{0,nm}=E_n\delta_{nm}$ (3.4.4) (p. 159):

$$[\hat H_0,\hat\rho]_{nm}=\sum_\nu(H_{0,n\nu}\rho_{\nu m}-\rho_{n\nu}H_{0,\nu m})=(E_n-E_m)\rho_{nm}\quad(3.4.5),\qquad \omega_{nm}=\frac{E_n-E_m}{\hbar}\quad(3.4.6)$$

$$\dot\rho_{nm}=-i\omega_{nm}\rho_{nm}-\frac i\hbar[\hat V,\hat\rho]_{nm}-\gamma_{nm}(\rho_{nm}-\rho^{(\rm eq)}_{nm})\quad(3.4.7)$$
$$\dot\rho_{nm}=-i\omega_{nm}\rho_{nm}-\frac i\hbar\sum_\nu(V_{n\nu}\rho_{\nu m}-\rho_{n\nu}V_{\nu m})-\gamma_{nm}(\rho_{nm}-\rho^{(\rm eq)}_{nm})\quad(3.4.8),\ \text{p. 160}$$

(Nota al pie, p. 159: esto es imagen de Schrödinger; en imagen de interacción, con
$\rho_{nm}=\sigma_{nm}e^{-i\omega_{nm}t}$, $\rho^{(\rm eq)}_{nm}=\sigma^{(\rm eq)}_{nm}e^{-i\omega_{nm}t}$:
$\dot\sigma_{nm}=-\frac i\hbar\sum_\nu[V_{n\nu}\sigma_{\nu m}e^{i\omega_{n\nu}t}-\sigma_{n\nu}e^{i\omega_{\nu m}t}V_{\nu m}]-\gamma_{nm}(\sigma_{nm}-\sigma^{(\rm eq)}_{nm})$.)

Expansión $V_{ij}\to\lambda V_{ij}$, $\rho_{nm}=\rho^{(0)}_{nm}+\lambda\rho^{(1)}_{nm}+\lambda^2\rho^{(2)}_{nm}+\cdots$ (3.4.9):

$$\dot\rho^{(0)}_{nm}=-i\omega_{nm}\rho^{(0)}_{nm}-\gamma_{nm}(\rho^{(0)}_{nm}-\rho^{(\rm eq)}_{nm})\ (3.4.10a),\quad \dot\rho^{(1)}_{nm}=-(i\omega_{nm}+\gamma_{nm})\rho^{(1)}_{nm}-i\hbar^{-1}[\hat V,\hat\rho^{(0)}]_{nm}\ (3.4.10b),$$
$$\dot\rho^{(2)}_{nm}=-(i\omega_{nm}+\gamma_{nm})\rho^{(2)}_{nm}-i\hbar^{-1}[\hat V,\hat\rho^{(1)}]_{nm}\ (3.4.10c),\ \dots$$

Cada ecuación es lineal con términos inhomogéneos ya conocidos. Estado estacionario sin campo:
$\rho^{(0)}_{nm}=\rho^{(\rm eq)}_{nm}$ (3.4.11a), $\rho^{(\rm eq)}_{nm}=0$ para $n\neq m$ (3.4.11b). Cambio de variable
$\rho^{(1)}_{nm}=S^{(1)}_{nm}e^{-(i\omega_{nm}+\gamma_{nm})t}$ (3.4.12), $\dot\rho^{(1)}_{nm}=-(i\omega_{nm}+\gamma_{nm})S^{(1)}_{nm}e^{-(\cdot)t}+\dot S^{(1)}_{nm}e^{-(\cdot)t}$ (3.4.13);
$\dot S^{(1)}_{nm}=\frac{-i}\hbar[\hat V,\hat\rho^{(0)}]_{nm}e^{(i\omega_{nm}+\gamma_{nm})t}$ (3.4.14), $S^{(1)}_{nm}=\int_{-\infty}^t\frac{-i}\hbar[\hat V(t'),\hat\rho^{(0)}]_{nm}e^{(i\omega_{nm}+\gamma_{nm})t'}dt'$ (3.4.15) (p. 161):

$$\rho^{(1)}_{nm}(t)=\int_{-\infty}^t\frac{-i}\hbar[\hat V(t'),\hat\rho^{(0)}]_{nm}e^{(i\omega_{nm}+\gamma_{nm})(t'-t)}dt'\quad(3.4.16)$$

y $\rho^{(N)}$ se obtiene igual reemplazando $\hat\rho^{(0)}\to\hat\rho^{(N-1)}$.

### 3.5 Cálculo de la susceptibilidad lineal con la matriz densidad (p. 161)

$\rho^{(1)}_{nm}(t)=e^{-(i\omega_{nm}+\gamma_{nm})t}\int_{-\infty}^tdt'\frac{-i}\hbar[\hat V(t'),\hat\rho^{(0)}]_{nm}e^{(i\omega_{nm}+\gamma_{nm})t'}$ (3.5.1),
$\hat V(t')=-\hat{\boldsymbol\mu}\cdot\tilde{\mathbf E}(t')$ (3.5.2), $\rho^{(0)}_{nm}=0$ para $n\neq m$ (3.5.3), $\tilde{\mathbf E}(t)=\sum_p\mathbf E(\omega_p)e^{-i\omega_pt}$ (3.5.4).
Conmutador (p. 162):

$$[\hat V(t),\hat\rho^{(0)}]_{nm}=-\sum_\nu[\boldsymbol\mu_{n\nu}\rho^{(0)}_{\nu m}-\rho^{(0)}_{n\nu}\boldsymbol\mu_{\nu m}]\cdot\tilde{\mathbf E}(t)=-(\rho^{(0)}_{mm}-\rho^{(0)}_{nn})\boldsymbol\mu_{nm}\cdot\tilde{\mathbf E}(t)\quad(3.5.5)$$

$\rho^{(1)}_{nm}=\frac i\hbar(\rho^{(0)}_{mm}-\rho^{(0)}_{nn})\boldsymbol\mu_{nm}\cdot e^{-(i\omega_{nm}+\gamma_{nm})t}\int_{-\infty}^t\tilde{\mathbf E}(t')e^{(i\omega_{nm}+\gamma_{nm})t'}dt'$ (3.5.6);
con (3.5.4), integral $\int_{-\infty}^te^{[i(\omega_{nm}-\omega_p)+\gamma_{nm}]t'}dt'$ (3.5.7), que da
$e^{-i\omega_pt}/[i(\omega_{nm}-\omega_p)+\gamma_{nm}]$ (3.5.8):

$$\rho^{(1)}_{nm}=\hbar^{-1}(\rho^{(0)}_{mm}-\rho^{(0)}_{nn})\sum_p\frac{\boldsymbol\mu_{nm}\cdot\mathbf E(\omega_p)e^{-i\omega_pt}}{(\omega_{nm}-\omega_p)-i\gamma_{nm}}\quad(3.5.9)$$

Dipolo (p. 163; se omite la barra de promedio de ensamble en el resto del capítulo):
$\langle\tilde{\boldsymbol\mu}(t)\rangle=\operatorname{tr}(\hat\rho^{(1)}\hat{\boldsymbol\mu})=\sum_{nm}\rho^{(1)}_{nm}\boldsymbol\mu_{mn}=\sum_{nm}\hbar^{-1}(\rho^{(0)}_{mm}-\rho^{(0)}_{nn})\sum_p\frac{\boldsymbol\mu_{mn}[\boldsymbol\mu_{nm}\cdot\mathbf E(\omega_p)]e^{-i\omega_pt}}{(\omega_{nm}-\omega_p)-i\gamma_{nm}}$ (3.5.10);
$\langle\tilde{\boldsymbol\mu}(t)\rangle=\sum_p\langle\boldsymbol\mu(\omega_p)\rangle e^{-i\omega_pt}$ (3.5.11); $\mathbf P(\omega_p)=N\langle\boldsymbol\mu(\omega_p)\rangle=\epsilon_0\boldsymbol\chi^{(1)}(\omega_p)\cdot\mathbf E(\omega_p)$ (3.5.12):

$$\boldsymbol\chi^{(1)}(\omega_p)=\frac{N}{\epsilon_0\hbar}\sum_{nm}(\rho^{(0)}_{mm}-\rho^{(0)}_{nn})\frac{\boldsymbol\mu_{mn}\boldsymbol\mu_{nm}}{(\omega_{nm}-\omega_p)-i\gamma_{nm}}\ (3.5.13),\qquad \chi^{(1)}_{ij}(\omega_p)=\frac{N}{\epsilon_0\hbar}\sum_{nm}(\rho^{(0)}_{mm}-\rho^{(0)}_{nn})\frac{\mu^i_{mn}\mu^j_{nm}}{(\omega_{nm}-\omega_p)-i\gamma_{nm}}\ (3.5.15)$$

con $P_i(\omega_p)=N\langle\mu_i(\omega_p)\rangle=\sum_j\epsilon_0\chi^{(1)}_{ij}E_j$ (3.5.14). $\chi^{(1)}$ es proporcional a la **diferencia de
poblaciones**: si $m$ y $n$ tienen igual población, la transición no contribuye.

Forma expandida (p. 164): separando (3.5.16), intercambiando índices mudos en la segunda suma
(3.5.17) y usando $\omega_{mn}=-\omega_{nm}$, $\gamma_{nm}=\gamma_{mn}$:

$$\chi^{(1)}_{ij}(\omega_p)=\frac{N}{\epsilon_0\hbar}\sum_{nm}\rho^{(0)}_{mm}\left[\frac{\mu^i_{mn}\mu^j_{nm}}{(\omega_{nm}-\omega_p)-i\gamma_{nm}}+\frac{\mu^i_{nm}\mu^j_{mn}}{(\omega_{nm}+\omega_p)+i\gamma_{nm}}\right]\quad(3.5.18)$$

Toda la población en $a$: $\rho^{(0)}_{aa}=1$, $\rho^{(0)}_{mm}=0$ ($m\neq a$) (3.5.19):

$$\chi^{(1)}_{ij}(\omega_p)=\frac{N}{\epsilon_0\hbar}\sum_n\left[\frac{\mu^i_{an}\mu^j_{na}}{(\omega_{na}-\omega_p)-i\gamma_{na}}+\frac{\mu^i_{na}\mu^j_{an}}{(\omega_{na}+\omega_p)+i\gamma_{na}}\right]\quad(3.5.20)$$

Para $\omega_p>0$ solo resuena el primero; el segundo es el término **antirresonante o
contrarrotante**, despreciable cerca de resonancia. Cerca de $\omega_{na}$:

$$\chi^{(1)}_{ij}(\omega_p)=\frac{N}{\epsilon_0\hbar}\frac{\mu^i_{an}\mu^j_{na}}{(\omega_{na}-\omega_p)-i\gamma_{na}}=\frac{N}{\epsilon_0\hbar}\mu^i_{an}\mu^j_{na}\frac{(\omega_{na}-\omega_p)+i\gamma_{na}}{(\omega_{na}-\omega_p)^2+\gamma_{na}^2}\quad(3.5.21)$$

Fig. 3.5.1 (p. 165): Im $\chi$ lorentziana con FWHM $=2\gamma_{na}$; Re $\chi$ dispersiva (positiva bajo
resonancia, negativa encima, cruza cero en $\omega_{na}$).

#### 3.5.1 Teoría de respuesta lineal (p. 165)

Medio isótropo ⇒ $\mathbf P\parallel\mathbf E$, $\mathbf P(\omega)=\epsilon_0\chi^{(1)}(\omega)\mathbf E(\omega)$:

$$\chi^{(1)}(\omega)=\frac{N}{\epsilon_0\hbar}\sum_n\tfrac13|\boldsymbol\mu_{na}|^2\left[\frac1{(\omega_{na}-\omega)-i\gamma_{na}}+\frac1{(\omega_{na}+\omega)+i\gamma_{na}}\right]\quad(3.5.22)$$

Fundamental $J=0$ (no degenerado), excitados $J=1$; el factor $\frac13$ porque la suma incluye todos los
subniveles magnéticos y en promedio solo un tercio de las transiciones tiene el dipolo paralelo a la
polarización. **Fuerza de oscilador** (p. 166):

$$f_{na}=\frac{2m\omega_{na}|\boldsymbol\mu_{na}|^2}{3\hbar e^2}\quad(3.5.23),\qquad \sum_nf_{na}=1\quad(3.5.24)\ \text{(regla de suma; Bethe y Salpeter, 1977)}$$

Si $a$ es el fundamental, $\omega_{na}>0$ y $0\le f_{na}\le1$. Entonces

$$\chi^{(1)}(\omega)=\sum_n\frac{Nf_{na}e^2}{2\epsilon_0m\omega_{na}}\left[\frac1{(\omega_{na}-\omega)-i\gamma_{na}}+\frac1{(\omega_{na}+\omega)+i\gamma_{na}}\right]\simeq\sum_nf_{na}\left[\frac{Ne^2/\epsilon_0m}{\omega_{na}^2-\omega^2-2i\omega_{na}\gamma_{na}}\right]\quad(3.5.25)$$

El corchete es idéntico al **modelo de Lorentz** clásico (1.4.17); la diferencia cuántica es que hay
varias resonancias, cada una pesada por su fuerza de oscilador.

Índice y absorción: $n(\omega)=\sqrt{\epsilon^{(1)}(\omega)}=\sqrt{1+\chi^{(1)}(\omega)}\simeq1+\frac12\chi^{(1)}(\omega)$ (3.5.26) (medio diluido,
$\chi^{(1)}\ll1$; también permite ignorar correcciones de campo local, §3.9). Onda plana
$\tilde E(z,t)=E_0e^{i(kz-\omega t)}+\text{c.c.}$ (3.5.27), $k=n(\omega)\omega/c$ (3.5.28) (p. 167); intensidad
$I=nc\epsilon_0\langle\tilde E(z,t)^2\rangle$, $I(z)=I_0e^{-\alpha z}$ (3.5.29),

$$\alpha=2n''\omega/c\quad(3.5.30),\qquad \alpha=\chi^{(1)''}\omega/c\quad(3.5.31a),\qquad \alpha\approx\sum_n\frac{f_{na}Ne^2}{2m\epsilon_0c\gamma_{na}}\left[\frac{\gamma_{na}^2}{(\omega_{na}-\omega)^2+\gamma_{na}^2}\right]\quad(3.5.31b)$$

con $n=n'+in''$, $\chi^{(1)}=\chi^{(1)'}+i\chi^{(1)''}$; en (3.5.31b) se reemplazó $\omega\to\omega_{na}$ (resonancia angosta).

**Polarizabilidad atómica** $\gamma^{(1)}$ (no se usa $\alpha$ para no confundir con absorción):
$\langle\boldsymbol\mu(\omega)\rangle=\gamma^{(1)}(\omega)\mathbf E(\omega)$ (3.5.32), $\chi^{(1)}(\omega)=N\gamma^{(1)}(\omega)$ (3.5.33) (sin campo local), y (p. 168)

$$\gamma^{(1)}(\omega)=\frac1{\epsilon_0\hbar}\sum_n\tfrac13|\boldsymbol\mu_{na}|^2\left[\frac1{(\omega_{na}-\omega)-i\gamma_{na}}+\frac1{(\omega_{na}+\omega)+i\gamma_{na}}\right]\quad(3.5.34)$$

(Nota de convención: con (3.5.32) tal cual, $P=N\langle\mu\rangle=\epsilon_0\chi E$ implicaría $\chi=N\gamma^{(1)}/\epsilon_0$; la
pareja (3.5.33)–(3.5.34) es consistente si (3.5.32) se lee $\langle\boldsymbol\mu\rangle=\epsilon_0\gamma^{(1)}\mathbf E$, es decir, $\gamma^{(1)}$ tiene
unidades de volumen. Ver erratas.)

**Sección eficaz de absorción** $\alpha=N\sigma$ (3.5.35): área efectiva del átomo para quitar radiación;
$\sigma=\gamma^{(1)''}\omega/c$ (3.5.36). $\omega_{na}$ y $\boldsymbol\mu_{na}$ son propiedades intrínsecas; $\gamma_{na}$ depende también
del entorno: $\gamma_{nm}=\frac12(\Gamma_n+\Gamma_m)+\gamma^{(\rm col)}_{nm}$ (3.5.37).

Valores máximos: en resonancia ($\omega=\omega_{na}$), sin término no resonante,
$\gamma^{(1)}_{\rm res}=\dfrac{i|\boldsymbol\mu_{n'a}|^2}{\epsilon_0\hbar\gamma_{n'a}}$ (3.5.38) ($n'$ = subnivel concreto excitado, por eso no aparece $\frac13$).
Máximo si $\gamma^{(\rm col)}_{n'a}=0$ y, con $a$ fundamental ($\Gamma_a=0$), $\gamma_{n'a}=\frac12\Gamma_{n'}$ (p. 169). Si $n'$ solo decae
al fundamental por emisión espontánea, coeficiente $A$ de Einstein:

$$\Gamma_{n'}=\frac{\omega_{na}^3|\boldsymbol\mu_{n'a}|^2}{3\pi\epsilon_0\hbar c^3}\quad(3.5.39),\qquad \gamma^{(1)}_{\max}=i6\pi\left(\frac{\lambda}{2\pi}\right)^3\quad(3.5.40),\qquad \sigma_{\max}=\frac{3\lambda^2}{2\pi}\quad(3.5.41)$$

En resonancia el átomo tiene una dimensión lineal efectiva del orden de la longitud de onda. En
general ($J_a$ abajo, $J_b$ arriba): $\sigma_{\max}=\dfrac{g_b}{g_a}\dfrac{\lambda^2}{2\pi}$ (3.5.42), $g=2J+1$, suponiendo subniveles
inferiores igualmente poblados; con bombeo óptico se multiplica por un factor entre 0 y 3 (0 si el
dipolo es ⟂ al campo, máximo si es paralelo); ver Siegman (1986).

### 3.6 Cálculo de la susceptibilidad de segundo orden con la matriz densidad (p. 170)

Se hace con detalle porque $\chi^{(2)}$ es importante en sí y porque sirve de plantilla para $\chi^{(3)}$
(que tiene **48 términos**, imposible de mostrar paso a paso). De (3.4.16):

$$\rho^{(2)}_{nm}=e^{-(i\omega_{nm}+\gamma_{nm})t}\int_{-\infty}^t\frac{-i}\hbar[\hat V,\hat\rho^{(1)}]_{nm}e^{(i\omega_{nm}+\gamma_{nm})t'}dt'\quad(3.6.1),\qquad [\hat V,\hat\rho^{(1)}]_{nm}=-\sum_\nu(\boldsymbol\mu_{n\nu}\rho^{(1)}_{\nu m}-\rho^{(1)}_{n\nu}\boldsymbol\mu_{\nu m})\cdot\tilde{\mathbf E}(t)\quad(3.6.2)$$

Con (3.5.9) reetiquetado: $\rho^{(1)}_{\nu m}=\hbar^{-1}(\rho^{(0)}_{mm}-\rho^{(0)}_{\nu\nu})\sum_p\frac{\boldsymbol\mu_{\nu m}\cdot\mathbf E(\omega_p)}{(\omega_{\nu m}-\omega_p)-i\gamma_{\nu m}}e^{-i\omega_pt}$ (3.6.3),
$\rho^{(1)}_{n\nu}=\hbar^{-1}(\rho^{(0)}_{\nu\nu}-\rho^{(0)}_{nn})\sum_p\frac{\boldsymbol\mu_{n\nu}\cdot\mathbf E(\omega_p)}{(\omega_{n\nu}-\omega_p)-i\gamma_{n\nu}}e^{-i\omega_pt}$ (3.6.4), $\tilde{\mathbf E}(t)=\sum_q\mathbf E(\omega_q)e^{-i\omega_qt}$ (3.6.5). Así (p. 171):

$$[\hat V,\hat\rho^{(1)}]_{nm}=-\hbar^{-1}\sum_\nu(\rho^{(0)}_{mm}-\rho^{(0)}_{\nu\nu})\sum_{pq}\frac{[\boldsymbol\mu_{n\nu}\cdot\mathbf E(\omega_q)][\boldsymbol\mu_{\nu m}\cdot\mathbf E(\omega_p)]}{(\omega_{\nu m}-\omega_p)-i\gamma_{\nu m}}e^{-i(\omega_p+\omega_q)t}+\hbar^{-1}\sum_\nu(\rho^{(0)}_{\nu\nu}-\rho^{(0)}_{nn})\sum_{pq}\frac{[\boldsymbol\mu_{n\nu}\cdot\mathbf E(\omega_p)][\boldsymbol\mu_{\nu m}\cdot\mathbf E(\omega_q)]}{(\omega_{n\nu}-\omega_p)-i\gamma_{n\nu}}e^{-i(\omega_p+\omega_q)t}\quad(3.6.6)$$

Integrando:

$$\rho^{(2)}_{nm}=\sum_\nu\sum_{pq}e^{-i(\omega_p+\omega_q)t}\left\{\frac{\rho^{(0)}_{mm}-\rho^{(0)}_{\nu\nu}}{\hbar^2}\frac{[\boldsymbol\mu_{n\nu}\cdot\mathbf E(\omega_q)][\boldsymbol\mu_{\nu m}\cdot\mathbf E(\omega_p)]}{[(\omega_{nm}-\omega_p-\omega_q)-i\gamma_{nm}][(\omega_{\nu m}-\omega_p)-i\gamma_{\nu m}]}-\frac{\rho^{(0)}_{\nu\nu}-\rho^{(0)}_{nn}}{\hbar^2}\frac{[\boldsymbol\mu_{n\nu}\cdot\mathbf E(\omega_p)][\boldsymbol\mu_{\nu m}\cdot\mathbf E(\omega_q)]}{[(\omega_{nm}-\omega_p-\omega_q)-i\gamma_{nm}][(\omega_{n\nu}-\omega_p)-i\gamma_{n\nu}]}\right\}\equiv\sum_\nu\sum_{pq}K_{nm\nu}e^{-i(\omega_p+\omega_q)t}\quad(3.6.7)$$

(en el segundo numerador el libro imprime $[\boldsymbol\mu_{n\nu}\cdot\mathbf E(\omega_q)][\boldsymbol\mu_{\nu m}\cdot\mathbf E(\omega_q)]$; ver erratas). Dipolo
$\langle\tilde{\boldsymbol\mu}\rangle=\sum_{nm}\rho_{nm}\boldsymbol\mu_{mn}$ (3.6.8), $\langle\tilde{\boldsymbol\mu}\rangle=\sum_r\langle\boldsymbol\mu(\omega_r)\rangle e^{-i\omega_rt}$ (3.6.9).

Componente a $\omega_p+\omega_q$ (p. 172): $\langle\boldsymbol\mu(\omega_p+\omega_q)\rangle=\sum_{nm\nu}\sum_{(pq)}K_{nm\nu}\boldsymbol\mu_{mn}$ (3.6.10),
$\mathbf P^{(2)}(\omega_p+\omega_q)=N\langle\boldsymbol\mu(\omega_p+\omega_q)\rangle=N\sum_{nm\nu}\sum_{(pq)}K_{nm\nu}\boldsymbol\mu_{mn}$ (3.6.11), y con
$P_i^{(2)}(\omega_p+\omega_q)=\epsilon_0\sum_{jk}\sum_{(pq)}\chi^{(2)}_{ijk}(\omega_p+\omega_q,\omega_q,\omega_p)E_j(\omega_q)E_k(\omega_p)$ (3.6.12) se obtiene la expresión tentativa

$$\chi^{(2)'}_{ijk}(\omega_p+\omega_q,\omega_q,\omega_p)=\frac{N}{\epsilon_0\hbar^2}\sum_{mn\nu}\left\{(\rho^{(0)}_{mm}-\rho^{(0)}_{\nu\nu})\frac{\mu^i_{mn}\mu^j_{n\nu}\mu^k_{\nu m}}{[(\omega_{nm}-\omega_p-\omega_q)-i\gamma_{nm}][(\omega_{\nu m}-\omega_p)-i\gamma_{\nu m}]}\ (a)-(\rho^{(0)}_{\nu\nu}-\rho^{(0)}_{nn})\frac{\mu^i_{mn}\mu^j_{\nu m}\mu^k_{n\nu}}{[(\omega_{nm}-\omega_p-\omega_q)-i\gamma_{nm}][(\omega_{n\nu}-\omega_p)-i\gamma_{n\nu}]}\ (b)\right\}\quad(3.6.13)$$

Predice bien $P$, pero no tiene simetría de permutación intrínseca (§1.5); se define $\chi^{(2)}$ como la
mitad de (3.6.13) más la expresión con $\omega_p\leftrightarrow\omega_q$, $j\leftrightarrow k$ (p. 173):

$$\chi^{(2)}_{ijk}(\omega_p+\omega_q,\omega_q,\omega_p)=\frac{N}{2\epsilon_0\hbar^2}\sum_{mn\nu}\Bigg\{(\rho^{(0)}_{mm}-\rho^{(0)}_{\nu\nu})\Bigg[\frac{\mu^i_{mn}\mu^j_{n\nu}\mu^k_{\nu m}}{[(\omega_{nm}-\omega_p-\omega_q)-i\gamma_{nm}][(\omega_{\nu m}-\omega_p)-i\gamma_{\nu m}]}\,(a_1)+\frac{\mu^i_{mn}\mu^k_{n\nu}\mu^j_{\nu m}}{[(\omega_{nm}-\omega_p-\omega_q)-i\gamma_{nm}][(\omega_{\nu m}-\omega_q)-i\gamma_{\nu m}]}\,(a_2)\Bigg]$$
$$-(\rho^{(0)}_{\nu\nu}-\rho^{(0)}_{nn})\Bigg[\frac{\mu^i_{mn}\mu^j_{\nu m}\mu^k_{n\nu}}{[(\omega_{nm}-\omega_p-\omega_q)-i\gamma_{nm}][(\omega_{n\nu}-\omega_p)-i\gamma_{n\nu}]}\,(b_1)+\frac{\mu^i_{mn}\mu^k_{\nu m}\mu^j_{n\nu}}{[(\omega_{nm}-\omega_p-\omega_q)-i\gamma_{nm}][(\omega_{n\nu}-\omega_q)-i\gamma_{n\nu}]}\,(b_2)\Bigg]\Bigg\}\quad(3.6.14)$$

Ciertas contribuciones se anulan si dos niveles tienen igual población; las diferencias de población
siempre corresponden a los dos niveles separados por una resonancia de **un fotón**. Renombrando
$\nu,n,m\to m,\nu,n$ en los dos últimos términos, para que la diferencia de población sea la misma
(3.6.15, pp. 173–174: los términos $b_1$, $b_2$ pasan a $-\mu^i_{n\nu}\mu^j_{mn}\mu^k_{\nu m}/\{[(\omega_{\nu n}-\omega_p-\omega_q)-i\gamma_{\nu n}][(\omega_{\nu m}-\omega_p)-i\gamma_{\nu m}]\}$
y lo mismo con $j\leftrightarrow k$, $\omega_p\leftrightarrow\omega_q$). Otro cambio, $m,\nu,n\to l,m,n$, usando $\omega_{lm}=-\omega_{ml}$, etc., y
encadenando los subíndices $n,m,l$:

$$\chi^{(2)}_{ijk}(\omega_p+\omega_q,\omega_q,\omega_p)=\frac{N}{2\epsilon_0\hbar^2}\sum_{lmn}(\rho^{(0)}_{ll}-\rho^{(0)}_{mm})\Bigg\{\frac{\mu^i_{ln}\mu^j_{nm}\mu^k_{ml}}{[(\omega_{nl}-\omega_p-\omega_q)-i\gamma_{nl}][(\omega_{ml}-\omega_p)-i\gamma_{ml}]}\,(a_1)+\frac{\mu^i_{ln}\mu^k_{nm}\mu^j_{ml}}{[(\omega_{nl}-\omega_p-\omega_q)-i\gamma_{nl}][(\omega_{ml}-\omega_q)-i\gamma_{ml}]}\,(a_2)$$
$$+\frac{\mu^j_{ln}\mu^i_{nm}\mu^k_{ml}}{[(\omega_{nm}+\omega_p+\omega_q)+i\gamma_{nm}][(\omega_{ml}-\omega_p)-i\gamma_{ml}]}\,(b_1)+\frac{\mu^k_{ln}\mu^i_{nm}\mu^j_{ml}}{[(\omega_{nm}+\omega_p+\omega_q)+i\gamma_{nm}][(\omega_{ml}-\omega_q)-i\gamma_{ml}]}\,(b_2)\Bigg\}\quad(3.6.16),\ \text{p. 174}$$

Fig. 3.6.1 (p. 175): posiciones de $l,m,n$ para resonancia de cada término ($\omega_p,\omega_q>0$); cada
contribución ∝ diferencia de población entre $l$ y $m$.

**Ejemplo, sistema de tres niveles** (Fig. 3.6.2, p. 175): solo $a,b,c$; $\omega_1\approx\omega_{ba}$, $\omega_2\approx\omega_{cb}$,
$\omega_3=\omega_1+\omega_2\approx\omega_{ca}$. Reteniendo solo términos con ambos factores del denominador resonantes:

$$\chi^{(2)}_{ijk}(\omega_3,\omega_2,\omega_1)=\frac{N}{2\epsilon_0\hbar^2}\left\{(\rho^{(0)}_{aa}-\rho^{(0)}_{bb})\left[\frac{\mu^i_{ac}\mu^j_{cb}\mu^k_{ba}}{[(\omega_{ca}-\omega_3)-i\gamma_{ca}][(\omega_{ba}-\omega_1)-i\gamma_{ba}]}\right]+(\rho^{(0)}_{cc}-\rho^{(0)}_{bb})\left[\frac{\mu^i_{ac}\mu^j_{cb}\mu^k_{ba}}{[(\omega_{ca}-\omega_3)-i\gamma_{ca}][(\omega_{cb}-\omega_2)-i\gamma_{cb}]}\right]\right\}\quad(3.6.17)$$

El primer término viene del 1.º de (3.6.16) y el segundo del 4.º; se anulan si $\rho_{aa}=\rho_{bb}$ y si
$\rho_{bb}=\rho_{cc}$ respectivamente: **con las tres poblaciones iguales la contribución resonante se anula**.

**Forma como suma sobre poblaciones** (p. 176): cambiando $l,m,n\to n,l,m$ en la suma con $\rho^{(0)}_{mm}$:

$$\chi^{(2)}_{ijk}(\omega_p+\omega_q,\omega_q,\omega_p)=\frac{N}{2\epsilon_0\hbar^2}\sum_{lmn}\rho^{(0)}_{ll}\Bigg\{\frac{\mu^i_{ln}\mu^j_{nm}\mu^k_{ml}}{[(\omega_{nl}-\omega_p-\omega_q)-i\gamma_{nl}][(\omega_{ml}-\omega_p)-i\gamma_{ml}]}(a_1)+\frac{\mu^i_{ln}\mu^k_{nm}\mu^j_{ml}}{[(\omega_{nl}-\omega_p-\omega_q)-i\gamma_{nl}][(\omega_{ml}-\omega_q)-i\gamma_{ml}]}(a_2)$$
$$+\frac{\mu^k_{ln}\mu^i_{nm}\mu^j_{ml}}{[(\omega_{mn}-\omega_p-\omega_q)-i\gamma_{mn}][(\omega_{nl}+\omega_p)+i\gamma_{nl}]}(a_1')+\frac{\mu^j_{ln}\mu^i_{nm}\mu^k_{ml}}{[(\omega_{mn}-\omega_p-\omega_q)-i\gamma_{mn}][(\omega_{nl}+\omega_q)+i\gamma_{nl}]}(a_2')$$
$$+\frac{\mu^j_{ln}\mu^i_{nm}\mu^k_{ml}}{[(\omega_{nm}+\omega_p+\omega_q)+i\gamma_{nm}][(\omega_{ml}-\omega_p)-i\gamma_{ml}]}(b_1)+\frac{\mu^k_{ln}\mu^i_{nm}\mu^j_{ml}}{[(\omega_{nm}+\omega_p+\omega_q)+i\gamma_{nm}][(\omega_{ml}-\omega_q)-i\gamma_{ml}]}(b_2)$$
$$+\frac{\mu^k_{ln}\mu^j_{nm}\mu^i_{ml}}{[(\omega_{ml}+\omega_p+\omega_q)+i\gamma_{ml}][(\omega_{nl}+\omega_p)+i\gamma_{nl}]}(b_1')+\frac{\mu^j_{ln}\mu^k_{nm}\mu^i_{ml}}{[(\omega_{ml}+\omega_p+\omega_q)+i\gamma_{ml}][(\omega_{nl}+\omega_q)+i\gamma_{nl}]}(b_2')\Bigg\}\quad(3.6.18)$$

Fig. 3.6.3 (p. 177): resonancias de (3.6.18); los diagramas sin prima coinciden con la Fig. 3.6.1;
$b_1'$ y $b_2'$ son resonancias nuevas (con $l$ arriba, niveles $n,m$ por debajo). Origen de cada tipo en
la cadena perturbativa: (a) $\rho^{(0)}_{mm}\to\rho^{(1)}_{\nu m}\to\rho^{(2)}_{nm}$, (a′) $\rho^{(0)}_{\nu\nu}\to\rho^{(1)}_{\nu m}\to\rho^{(2)}_{nm}$, (b) $\rho^{(0)}_{\nu\nu}\to\rho^{(1)}_{n\nu}\to\rho^{(2)}_{nm}$,
(b′) $\rho^{(0)}_{nn}\to\rho^{(1)}_{n\nu}\to\rho^{(2)}_{nm}$; con los índices nuevos:

$$(a):\ \rho^{(0)}_{ll}\to\rho^{(1)}_{ml}\to\rho^{(2)}_{nl},\quad (a'):\ \rho^{(0)}_{ll}\to\rho^{(1)}_{ln}\to\rho^{(2)}_{mn},\quad (b):\ \rho^{(0)}_{ll}\to\rho^{(1)}_{ml}\to\rho^{(2)}_{mn},\quad (b'):\ \rho^{(0)}_{ll}\to\rho^{(1)}_{ln}\to\rho^{(2)}_{lm}\quad(3.6.19)$$

Difieren en si cada interacción cambia el índice izquierdo o el derecho y en qué orden.

**Diagramas de Feynman de doble lado** (Fig. 3.6.4, p. 178): $\hat\rho=\overline{|\psi\rangle\langle\psi|}$ (3.6.20),
$\rho_{nm}=\langle n|\hat\rho|m\rangle$ (3.6.21). Lado izquierdo: evolución del ket $|\psi\rangle$; derecho: del bra $\langle\psi|$; el tiempo
crece hacia arriba; cada interacción con el campo es una flecha sólida etiquetada con su frecuencia;
la traza (cálculo del campo de salida) es la flecha ondulada. Hay varias convenciones (Boyd y
Mukamel, 1984; Prior, 1984; Yee y Gustafson, 1978). En la Fig. 3.6.4 todas las frecuencias se suponen
positivas (absorción de un fotón); una frecuencia negativa (emisión) se dibuja a veces con la flecha
apuntando hacia arriba y alejándose de la doble línea (nota, p. 179).

#### 3.6.1 $\chi^{(2)}$ en el límite de excitación no resonante (p. 179)

Si $\omega_p$, $\omega_q$, $\omega_p+\omega_q$ están lejos de resonancia se desprecian las partes imaginarias; los términos
($a_2'$) y ($b_1$) se combinan (numeradores idénticos):

$$\frac1{(\omega_{mn}-\omega_p-\omega_q)(\omega_{nl}+\omega_q)}+\frac1{(-\omega_{mn}+\omega_p+\omega_q)(\omega_{ml}-\omega_p)}=\frac1{(\omega_{mn}-\omega_p-\omega_q)}\left[\frac{\omega_{ml}-\omega_p-\omega_{nl}-\omega_q}{(\omega_{nl}+\omega_q)(\omega_{ml}-\omega_p)}\right]=\frac1{(\omega_{nl}+\omega_q)(\omega_{ml}-\omega_p)}\quad(3.6.22)$$

(usando $\omega_{ml}-\omega_{nl}=\omega_{mn}$); igual ($a_1'$)+($b_2$) da $\dfrac1{(\omega_{nl}+\omega_p)(\omega_{ml}-\omega_q)}$ (3.6.23). Resultado (p. 180):

$$\chi^{(2)}_{ijk}(\omega_p+\omega_q,\omega_q,\omega_p)=\frac{N}{2\epsilon_0\hbar^2}\sum_{lmn}\rho^{(0)}_{ll}\Bigg\{\frac{\mu^i_{ln}\mu^j_{nm}\mu^k_{ml}}{(\omega_{nl}-\omega_p-\omega_q)(\omega_{ml}-\omega_p)}(a_1)+\frac{\mu^i_{ln}\mu^k_{nm}\mu^j_{ml}}{(\omega_{nl}-\omega_p-\omega_q)(\omega_{ml}-\omega_q)}(a_2)+\frac{\mu^j_{ln}\mu^i_{nm}\mu^k_{ml}}{(\omega_{nl}+\omega_q)(\omega_{ml}-\omega_p)}(b_1,a_2')$$
$$+\frac{\mu^k_{ln}\mu^i_{nm}\mu^j_{ml}}{(\omega_{nl}+\omega_p)(\omega_{ml}-\omega_q)}(b_2,a_1')+\frac{\mu^k_{ln}\mu^j_{nm}\mu^i_{ml}}{(\omega_{ml}+\omega_p+\omega_q)(\omega_{nl}+\omega_p)}(b_1')+\frac{\mu^j_{ln}\mu^k_{nm}\mu^i_{ml}}{(\omega_{ml}+\omega_p+\omega_q)(\omega_{nl}+\omega_q)}(b_2')\Bigg\}\quad(3.6.24)$$

Seis términos (frente a ocho en el caso general); cumple **simetría de permutación total** (1.5.7) y es
idéntica a (3.2.27) de la teoría de función de onda. Los diagramas de niveles dan exactamente los de
la Fig. 3.6.3; también puede entenderse con el método diagramático de Ward (1965).

### 3.7 Cálculo de la susceptibilidad de tercer orden con la matriz densidad (p. 180)

$\rho^{(3)}_{nm}=e^{-(i\omega_{nm}+\gamma_{nm})t}\int_{-\infty}^t\frac{-i}\hbar[\hat V,\hat\rho^{(2)}]_{nm}e^{(i\omega_{nm}+\gamma_{nm})t'}dt'$ (3.7.1),
$[\hat V,\hat\rho^{(2)}]_{nm}=-\sum_\nu(\boldsymbol\mu_{n\nu}\rho^{(2)}_{\nu m}-\rho^{(2)}_{n\nu}\boldsymbol\mu_{\nu m})\cdot\tilde{\mathbf E}(t)$ (3.7.2), con (3.6.7) abreviado
$\rho^{(2)}_{\nu m}=\sum_l\sum_{pq}K_{\nu ml}e^{-i(\omega_p+\omega_q)t}$ (3.7.3) y $\tilde{\mathbf E}(t)=\sum_r\mathbf E(\omega_r)e^{-i\omega_rt}$ (3.7.4) (p. 181):

$$[\hat V,\hat\rho^{(2)}]_{nm}=-\sum_{\nu l}\sum_{pqr}[\boldsymbol\mu_{n\nu}\cdot\mathbf E(\omega_r)]K_{\nu ml}e^{-i(\omega_p+\omega_q+\omega_r)t}+\sum_{\nu l}\sum_{pqr}[\boldsymbol\mu_{\nu m}\cdot\mathbf E(\omega_r)]K_{n\nu l}e^{-i(\omega_p+\omega_q+\omega_r)t}\quad(3.7.5)$$

$$\rho^{(3)}_{nm}=\frac1\hbar\sum_{\nu l}\sum_{pqr}\left\{\frac{[\boldsymbol\mu_{n\nu}\cdot\mathbf E(\omega_r)]K_{\nu ml}}{(\omega_{nm}-\omega_p-\omega_q-\omega_r)-i\gamma_{nm}}-\frac{[\boldsymbol\mu_{\nu m}\cdot\mathbf E(\omega_r)]K_{n\nu l}}{(\omega_{nm}-\omega_p-\omega_q-\omega_r)-i\gamma_{nm}}\right\}e^{-i(\omega_p+\omega_q+\omega_r)t}\quad(3.7.6)$$

$\mathbf P(\omega_p+\omega_q+\omega_r)=N\langle\boldsymbol\mu(\omega_p+\omega_q+\omega_r)\rangle$ (3.7.7), $\langle\tilde{\boldsymbol\mu}\rangle=\sum_{nm}\rho_{nm}\boldsymbol\mu_{mn}\equiv\sum_s\langle\boldsymbol\mu(\omega_s)\rangle e^{-i\omega_st}$ (3.7.8),
$P_k(\omega_p+\omega_q+\omega_r)=\epsilon_0\sum_{hij}\sum_{(pqr)}\chi^{(3)}_{kjih}(\omega_p+\omega_q+\omega_r,\omega_r,\omega_q,\omega_p)E_j(\omega_r)E_i(\omega_q)E_h(\omega_p)$ (3.7.9) (p. 182). Resultado:

$$\chi^{(3)}_{kjih}(\omega_p+\omega_q+\omega_r,\omega_r,\omega_q,\omega_p)=\frac{N}{\epsilon_0\hbar^3}\mathcal P_I\sum_{nm\nu l}\Bigg\{\frac{(\rho^{(0)}_{mm}-\rho^{(0)}_{ll})\mu^k_{mn}\mu^j_{n\nu}\mu^i_{\nu l}\mu^h_{lm}}{[(\omega_{nm}-\omega_p-\omega_q-\omega_r)-i\gamma_{nm}][(\omega_{\nu m}-\omega_p-\omega_q)-i\gamma_{\nu m}][(\omega_{lm}-\omega_p)-i\gamma_{lm}]}\,(a)$$
$$-\frac{(\rho^{(0)}_{ll}-\rho^{(0)}_{\nu\nu})\mu^k_{mn}\mu^j_{n\nu}\mu^i_{lm}\mu^h_{\nu l}}{[(\omega_{nm}-\omega_p-\omega_q-\omega_r)-i\gamma_{nm}][(\omega_{\nu m}-\omega_p-\omega_q)-i\gamma_{\nu m}][(\omega_{\nu l}-\omega_p)-i\gamma_{\nu l}]}\,(b)$$
$$-\frac{(\rho^{(0)}_{\nu\nu}-\rho^{(0)}_{ll})\mu^k_{mn}\mu^j_{\nu m}\mu^i_{nl}\mu^h_{l\nu}}{[(\omega_{nm}-\omega_p-\omega_q-\omega_r)-i\gamma_{nm}][(\omega_{n\nu}-\omega_p-\omega_q)-i\gamma_{n\nu}][(\omega_{l\nu}-\omega_p)-i\gamma_{l\nu}]}\,(c)$$
$$+\frac{(\rho^{(0)}_{ll}-\rho^{(0)}_{nn})\mu^k_{mn}\mu^j_{\nu m}\mu^i_{l\nu}\mu^h_{nl}}{[(\omega_{nm}-\omega_p-\omega_q-\omega_r)-i\gamma_{nm}][(\omega_{n\nu}-\omega_p-\omega_q)-i\gamma_{n\nu}][(\omega_{nl}-\omega_p)-i\gamma_{nl}]}\,(d)\Bigg\}\quad(3.7.10)$$

$\mathcal P_I$: promediar sobre todas las permutaciones de $\omega_p,\omega_q,\omega_r$ con $h,i,j$ simultáneamente. Reescrito en
ocho términos con $l$ siempre índice de $\rho^{(0)}_{ll}$, solo frecuencias de resonancia positivas si
$E_\nu>E_n>E_m>E_l$ y elementos de matriz en orden "natural" $l\to m\to n\to\nu$ (de derecha a izquierda),
p. 183:

$$\chi^{(3)}_{kjih}(\omega_p+\omega_q+\omega_r,\omega_r,\omega_q,\omega_p)=\frac{N}{\epsilon_0\hbar^3}\mathcal P_I\sum_{\nu nml}\rho^{(0)}_{ll}\Bigg\{\frac{\mu^k_{l\nu}\mu^j_{\nu n}\mu^i_{nm}\mu^h_{ml}}{[(\omega_{\nu l}-\omega_p-\omega_q-\omega_r)-i\gamma_{\nu l}][(\omega_{nl}-\omega_p-\omega_q)-i\gamma_{nl}][(\omega_{ml}-\omega_p)-i\gamma_{ml}]}(a_1)$$
$$+\frac{\mu^h_{l\nu}\mu^k_{\nu n}\mu^j_{nm}\mu^i_{ml}}{[(\omega_{n\nu}-\omega_p-\omega_q-\omega_r)-i\gamma_{n\nu}][(\omega_{m\nu}-\omega_p-\omega_q)-i\gamma_{m\nu}][(\omega_{\nu l}+\omega_p)+i\gamma_{\nu l}]}(a_2)
+\frac{\mu^i_{l\nu}\mu^k_{\nu n}\mu^j_{nm}\mu^h_{ml}}{[(\omega_{n\nu}-\omega_p-\omega_q-\omega_r)-i\gamma_{n\nu}][(\omega_{\nu m}+\omega_p+\omega_q)+i\gamma_{\nu m}][(\omega_{ml}-\omega_p)-i\gamma_{ml}]}(b_1)$$
$$+\frac{\mu^h_{l\nu}\mu^i_{\nu n}\mu^k_{nm}\mu^j_{ml}}{[(\omega_{mn}-\omega_p-\omega_q-\omega_r)-i\gamma_{mn}][(\omega_{nl}+\omega_p+\omega_q)+i\gamma_{nl}][(\omega_{\nu l}+\omega_p)+i\gamma_{\nu l}]}(b_2)
+\frac{\mu^j_{l\nu}\mu^k_{\nu n}\mu^i_{nm}\mu^h_{ml}}{[(\omega_{\nu n}+\omega_p+\omega_q+\omega_r)+i\gamma_{\nu n}][(\omega_{nl}-\omega_p-\omega_q)-i\gamma_{nl}][(\omega_{ml}-\omega_p)-i\gamma_{ml}]}(c_1)$$
$$+\frac{\mu^h_{l\nu}\mu^j_{\nu n}\mu^k_{nm}\mu^i_{ml}}{[(\omega_{nm}+\omega_p+\omega_q+\omega_r)+i\gamma_{nm}][(\omega_{m\nu}-\omega_p-\omega_q)-i\gamma_{m\nu}][(\omega_{\nu l}+\omega_p)+i\gamma_{\nu l}]}(c_2)
+\frac{\mu^i_{l\nu}\mu^j_{\nu n}\mu^k_{nm}\mu^h_{ml}}{[(\omega_{nm}+\omega_p+\omega_q+\omega_r)+i\gamma_{nm}][(\omega_{\nu m}+\omega_p+\omega_q)+i\gamma_{m\nu}][(\omega_{ml}-\omega_p)-i\gamma_{ml}]}(d_1)$$
$$+\frac{\mu^h_{l\nu}\mu^i_{\nu n}\mu^j_{nm}\mu^k_{ml}}{[(\omega_{ml}+\omega_p+\omega_q+\omega_r)+i\gamma_{ml}][(\omega_{nl}+\omega_p+\omega_q)+i\gamma_{nl}][(\omega_{\nu l}+\omega_p)+i\gamma_{\nu l}]}(d_2)\Bigg\}\quad(3.7.11)$$

(transcrita tal como está impresa; los subíndices de algunos denominadores, p. ej. $\omega_{n\nu}$, $\omega_{mn}$, no
siguen exactamente el "orden natural" anunciado — conviene verificar contra la fuente original si se
usa numéricamente). Con $\omega_p,\omega_q,\omega_r$ distintos hay seis permutaciones ⇒ **48 términos**.
Estructura resonante: Fig. 3.7.1; diagramas de Feynman de doble lado: Fig. 3.7.2.

- Fig. 3.7.1 (p. 184): resonancias de los ocho términos de (3.7.11) ($a_1$: escalera $l\to m\to n\to\nu$
  con $\omega_p,\omega_q,\omega_r$; los demás tienen uno o más niveles "por debajo" de $l$; $d_2$ con $l$ arriba).
- Fig. 3.7.2 (p. 185): diagramas de Feynman de doble lado de cada término.

Relación con §3.2: la expresión de función de onda tenía 24 términos ((3.2.32) muestra cuatro; el
texto, p. 184, dice "(3.2.33)"). (3.7.11) se reduce a (3.2.33) en el límite no resonante (despreciando
los $i\gamma_{\alpha\beta}$), con un cálculo análogo al de (3.6.23) (Problema 5). Incluso reteniendo los $i\gamma_{\alpha\beta}$, la expresión
de 48 términos puede reescribirse como la de 24 con coeficientes débilmente dependientes de la
frecuencia; estos muestran resonancias nuevas que solo aparecen si el ensanchamiento es colisional
(no radiativo): **resonancias inducidas por colisiones** (Bloembergen et al., 1978; Prior, 1984;
Rothberg, 1987).

### 3.8 Transparencia inducida electromagnéticamente (EIT) (p. 185)

EIT vuelve transparente un sistema a radiación resonante conservando su gran respuesta no lineal
resonante. Propuesta teórica: Harris et al. (1990); relacionada con Gray et al. (1978), Tewari y
Agarwal (1986) y con láser sin inversión (Harris, 1989; Kocharovskaya y Khanin, 1988; Scully et al.,
1989). Observada en átomos (Boller et al., 1991; Field et al., 1991) y sólidos (Ham et al., 1997;
Zhao et al., 1997). Mejora la conversión de frecuencia (Hakuta et al., 1991; Jain et al., 1996) y la
conjugación de fase (Hemmer et al., 1995; Li y Xiao, 1996); clave en la **luz lenta** (Budker et al.,
1999; Boyd y Gauthier, 2002; Hau et al., 1999; Inouye et al., 2000; Kash et al., 1999); predicha para
luz comprimida (Lukin et al., 1999) y conmutación fotónica a bajo nivel de luz (Harris y Yamamoto,
1998; Imamoğlu et al., 1997).

Prototipo (Fig. 3.8.1, p. 186): (a) campos $\omega$ y $\omega_s$ para generar $\omega_4=2\omega+\omega_s$ (niveles $a$, $b$, $c$, $d$;
$2\omega\approx\omega_{ca}$, $\omega_s$ acopla $c\leftrightarrow d$, $\omega_4\approx\omega_{da}$). La fuerte absorción a $\omega_4$ limitaría la SFG, pero un
campo $\omega_s$ fuerte y saturante elimina la absorción en $a\to d$ manteniendo una gran susceptibilidad de
mezcla de cuatro ondas. (b) Subproblema: absorción a $\omega_4$ modificada por el campo saturante $E_s$.

**Absorción lineal a $\omega_4$ con campo de acoplamiento** (p. 187). En lugar de
$\psi=C_a'u_ae^{-i\omega_at}+C_d'u_de^{-i\omega_dt}+C_c'u_ce^{-i\omega_ct}$ (3.8.1), se usa la **imagen de interacción**:

$$\psi(\mathbf r,t)=C_a(t)u_a(\mathbf r)+C_d(t)u_d(\mathbf r)e^{-i\omega_4t}+C_c(t)u_c(\mathbf r)e^{-i(\omega_4-\omega_s)t}\quad(3.8.2)$$

(en un sistema forzado los coeficientes oscilan a la frecuencia de forzamiento). $i\hbar\partial_t\psi=\hat H\psi$,
$\hat H=\hat H_0+\hat V$ (3.8.3), en aproximación de onda rotante y dipolar $\hat V=-\hat\mu(E_4e^{-i\omega_4t}+E_s^*e^{i\omega_st})$ (3.8.4).
Sustituyendo (3.8.5) y proyectando (3.8.6, p. 188): $i\hbar\dot C_a=\hbar\omega_aC_a+V_{ad}C_de^{-i\omega_4t}$, etc. Con
$V_{ad}^*=V_{da}=-\mu_{da}E_4e^{-i\omega_4t}$, $V_{dc}^*=V_{cd}=-\mu_{cd}E_s^*e^{i\omega_st}$ (3.8.7), energías relativas al fundamental
$\hbar\omega_a\to0$, $\hbar\omega_d\to\hbar\omega_{da}$, $\hbar\omega_c\to\hbar\omega_{ca}$ (3.8.8), y frecuencias de Rabi

$$\Omega=\mu_{da}E_4/\hbar,\qquad \Omega_s^*=\mu_{cd}E_s^*/\hbar\quad(3.8.9)$$

$$\dot C_a=iC_d\Omega^*,\qquad \dot C_d-i\delta C_d=iC_a\Omega+iC_c\Omega_s,\qquad \dot C_c-i(\delta-\Delta)C_c=iC_d\Omega_s^*\quad(3.8.10)$$

con $\delta\equiv\omega_4-\omega_{da}$, $\Delta\equiv\omega_s-\omega_{dc}$ (3.8.11). Se resuelve a todo orden en $\Omega_s$ y a orden más bajo en
$\Omega$: $\Omega\to\lambda\Omega$, $C_j=C_j^{(0)}+\lambda C_j^{(1)}+\lambda^2C_j^{(2)}+\cdots$ (3.8.12); sustituyendo (3.8.13, p. 189) y separando
potencias: orden 0 (3.8.14) con solución $C_a^{(0)}=1$, $C_d^{(0)}=C_c^{(0)}=0$ (3.8.15); orden 1 (3.8.16):
$\dot C_a^{(1)}=0$ ⇒ $C_a^{(1)}=0$, y (quitando el superíndice)

$$\dot C_d-i\delta C_d=i\Omega+i\Omega_sC_c,\qquad \dot C_c-i(\delta-\Delta)C_c=i\Omega_s^*C_d\quad(3.8.17)$$

coeficientes independientes del tiempo (razón de usar la imagen de interacción). Estado estacionario
(p. 190): $0=\Omega+\delta C_d+\Omega_sC_c$, $0=\Omega_s^{2}C_d+(\delta-\Delta)C_c$ (3.8.18) [debería ser $\Omega_s^*$], de donde

$$C_d=\frac{\Omega(\delta-\Delta)}{|\Omega_s|^2-\delta(\delta-\Delta)}\quad(3.8.19)$$

Dipolo: $\tilde p=\langle\psi|\hat\mu|\psi\rangle=\langle\psi^{(0)}|\hat\mu|\psi^{(1)}\rangle+\langle\psi^{(1)}|\hat\mu|\psi^{(0)}\rangle=\langle a|\hat\mu|d\rangle C_de^{-i\omega_4t}+\text{c.c.}=\mu_{ad}C_de^{-i\omega_4t}+\text{c.c.}$ (3.8.20);
el libro imprime $p=\dfrac{\mu_{ad}\Omega(\delta+\Delta)}{|\Omega_s|^2-(\delta+\Delta)\delta}$ (3.8.21) (por consistencia con (3.8.19) y (3.8.23) debería ser
$\delta-\Delta$); $P=Np\equiv\epsilon_0\chi^{(1)}E$ (3.8.22):

$$\chi^{(1)}=\frac{N|\mu_{da}|^2}{\epsilon_0\hbar}\frac{(\delta-\Delta)}{|\Omega_s|^2-(\delta-\Delta)\delta}\quad(3.8.23)$$

Amortiguamiento fenomenológico: $\gamma_d$, $\gamma_c$ tasas de decaimiento de las amplitudes de $d$ y $c$ (el
texto dice "d and e"); en (3.8.17) basta $\delta\to\delta+i\gamma_d$, $\Delta\to\Delta+i(\gamma_c-\gamma_d)$:

$$p=\frac{\mu_{ad}\Omega(\delta-\Delta+i\gamma_c)}{|\Omega_s|^2-(\delta+i\gamma_d)(\delta-\Delta+i\gamma_c)}\quad(3.8.24),\qquad \chi^{(1)}=\frac{N}{\hbar}\frac{|\mu_{da}|^2(\delta-\Delta+i\gamma_c)}{|\Omega_s|^2-(\delta+i\gamma_d)(\delta-\Delta+i\gamma_c)}\quad(3.8.25)$$

(falta $\epsilon_0$ en el denominador respecto de (3.8.23)). En resonancia exacta $\delta=\Delta=0$ (p. 191):

$$\chi^{(1)}=\frac{N}{\hbar}\frac{|\mu_{da}|^2i\gamma_c}{|\Omega_s|^2+\gamma_c\gamma_d}\quad(3.8.26)$$

puramente imaginaria; la absorción a $\omega_4$ se hace arbitrariamente pequeña con $\Omega_s$ saturante (si
$\gamma_c\ll\gamma_d$). Fig. 3.8.2 (p. 191), con $\Delta=0$ y $\gamma_c/\gamma_d=0.01$: (a) Im $\chi^{(1)}$ vs $\delta/\gamma_d\in[-10,10]$ para
$\Omega_s=0$ (una lorentziana) y $\Omega_s=5\gamma_d$ (doblete de Autler–Townes: dos componentes separadas del centro
por $|\Omega_s|$); (b) $\delta/\gamma_d\in[-4,4]$, $\Omega_s=0.4\gamma_d$: un hueco angosto y pronunciado en el centro de la línea;
en ambos casos la absorción cae casi a cero en resonancia. (c), (d): $|\chi^{(3)}|$ de la SFG para
$\Omega_s=5\gamma_d$ y $0.4\gamma_d$: la respuesta no lineal sigue siendo apreciable donde hay casi transparencia (y
en (d) incluso tiene un pico).

**Respuesta de suma de frecuencias** (p. 192). Imagen de interacción:
$\psi=C_au_a+C_bu_be^{-i\omega t}+C_cu_ce^{-2i\omega t}+C_du_de^{-i(2\omega+\omega_s)t}$ (3.8.27) (el libro escribe $\omega_c$ en algunos
exponentes donde corresponde $\omega_s$). Sustituyendo (3.8.28) y proyectando (3.8.29); elementos de matriz
$V_{ba}=V_{ab}^*=-\mu_{ba}Ee^{-i\omega t}=-\hbar\Omega_{ba}e^{-i\omega t}$, $V_{cb}=V_{bc}^*=-\mu_{cb}Ee^{-i\omega t}=-\hbar\Omega_{cb}e^{-i\omega t}$,
$V_{dc}=V_{cd}^*=-\mu_{dc}E_se^{-i\omega_st}=-\hbar\Omega_{dc}e^{-i\omega_st}$ (3.8.30); desintonías
$\delta_1=\omega-\omega_{ba}$, $\delta_2=2\omega-\omega_{ca}$, $\Delta=\omega_s-\omega_{dc}$ (3.8.31). Resultado (p. 193):

$$\dot C_a=iC_b\Omega_{ba}^*\ (3.8.32a),\quad \dot C_b-iC_b\delta_1=iC_a\Omega_{ba}+iC_c\Omega_{cb}^*\ (3.8.32b),\quad \dot C_c-iC_c\delta_2=iC_b\Omega_{cb}+iC_d\Omega_{dc}^*\ (3.8.32c),\quad \dot C_d-iC_d(\delta_2+\Delta)=iC_c\Omega_{dc}\ (3.8.32d)$$

Perturbativo en $\Omega_{ba}$, $\Omega_{cb}$, a todo orden en $\Omega_{dc}$: se ignora (3.8.32a) ($|C_b|\ll|C_a|$, $C_a\approx1$); en
(3.8.32b) se desprecia el último término ($|C_c|\ll|C_b|$); estacionario:
$C_b=-\Omega_{ba}/\delta_1$ (3.8.33). De (3.8.32c,d) estacionarios: $-C_c=\dfrac{C_b\Omega_{cb}}{\delta_2}+\dfrac{C_d\Omega_{dc}^*}{\delta_2}$, $C_d=\dfrac{-C_c\Omega_{dc}}{\delta_2+\Delta}$ (3.8.34);
$C_d=\dfrac{-\Omega_{ba}\Omega_{cb}\Omega_{dc}}{\delta_1\delta_2(\delta_2+\Delta)}+C_d\dfrac{|\Omega_{dc}|^2}{(\delta_2+\Delta)\delta_2}$ (3.8.35), y

$$C_d=-\frac{\Omega_{dc}\Omega_{cb}\Omega_{ba}}{\delta_1\delta_2(\delta_2+\Delta)}\left[1-\frac{|\Omega_{dc}|^2}{\delta_2(\delta_2+\Delta)}\right]^{-1}\ (3.8.36)=-\frac{\Omega_{dc}\Omega_{cb}\Omega_{ba}}{\delta_1[\delta_2(\delta_2+\Delta)-|\Omega_{dc}|^2]}\quad(3.8.37)$$

(el libro imprime el corchete de (3.8.36) como $\left[\frac{|\Omega_{dc}|^2}{\delta_2(\delta_2+\Delta)}\right]^{-1}$, sin el "1 −"; la forma (3.8.37) es la
correcta). Dipolo a la frecuencia suma: $\tilde p=\langle\psi|\hat\mu|\psi\rangle=\langle u_a|\hat\mu|C_du_d\rangle+\text{c.c.}=\mu_{ad}C_d+\text{c.c.}$ (3.8.38) (p. 194):

$$p=\frac{-\mu_{ad}\Omega_{dc}\Omega_{cb}\Omega_{ba}}{\delta_1[\delta_2(\delta_2+\Delta)-|\Omega_{dc}|^2]}=\frac{-\mu_{ad}\mu_{dc}\mu_{cb}\mu_{ba}E^2E_s}{\hbar^3\delta_1[\delta_2(\delta_2+\Delta)-|\Omega_{dc}|^2]}\equiv\frac{3\epsilon_0\chi^{(3)}E^2E_s}{N}\quad(3.8.39)$$

(impreso con $\mu_{bc}$ en vez de $\mu_{dc}$ y $E_c$ en vez de $E_s$; el denominador sale muy tenue en el escaneo).
El factor 3 es la degeneración de la SFG $\omega+\omega+\omega_s$.

$$\chi^{(3)}=\frac{-N\mu_{ad}\mu_{dc}\mu_{cb}\mu_{ba}}{3\epsilon_0\hbar\,\delta_1[\delta_2(\delta_2+\Delta)-|\Omega_{dc}|^2]}\quad(3.8.40)\qquad\to\qquad \chi^{(3)}=\frac{-N\mu_{ad}\mu_{dc}\mu_{cb}\mu_{ba}}{3\epsilon_0\hbar\,\delta_1[(\delta_2+i\gamma_c)(\delta_2+\Delta+i\gamma_d)-|\Omega_{dc}|^2]}\quad(3.8.41)$$

(amortiguamiento: $\delta_2\to\delta_2+i\gamma_c$, $\delta_2+\Delta\to\delta_2+\Delta+i\gamma_d$). [Dimensionalmente, con $\delta$ en rad/s, el
prefactor debería ser $\hbar^3$ y no $\hbar$; ver erratas.] Con $|\Omega_{dc}|\to0$ se recupera la contribución resonante
usual de $\chi^{(3)}$. Fig. 3.8.2(c,d): la respuesta no lineal sigue siendo apreciable en la posición de la
resonancia original.

### 3.9 Correcciones de campo local a la susceptibilidad no lineal (p. 194)

Hasta aquí se supuso que el campo que actúa sobre cada átomo es el campo macroscópico de Maxwell. En
general hay que distinguir el campo macroscópico del **campo local de Lorentz**; la distinción importa
salvo en medios tan diluidos que $\epsilon^{(1)}\approx1$.

#### 3.9.1 Efectos de campo local en óptica lineal (p. 194)

El campo de Maxwell (Ecs. (2.1.1)–(2.1.8)) es un promedio espacial del campo microscópico sobre
regiones de varios diámetros atómicos; incluye fuentes externas y todas las moléculas. Medio sin
pérdidas ni dispersión. Dipolo molecular (aquí $\alpha$ es la polarizabilidad, no la absorción):

$$\tilde{\mathbf p}=\epsilon_0\alpha\tilde E_{\rm loc}\quad(3.9.1),\ \text{p. 195}$$

$\tilde E_{\rm loc}$: campo de todas las fuentes y moléculas **excepto** la considerada. Procedimiento de Lorentz
(1952), Fig. 3.9.1: esfera pequeña centrada en la molécula, con muchas moléculas; sus campos en el
centro se cancelan (exacto en líquido, gas o cristal cúbico); queda una cavidad esférica en un medio
uniformemente polarizado (Born y Wolf, 1975, §2.3; Jackson, 1975, §4.5), p. 196:

$$\tilde{\mathbf E}_{\rm loc}=\tilde{\mathbf E}+\frac1{3\epsilon_0}\tilde{\mathbf P}\quad(3.9.2),\qquad \tilde{\mathbf P}=N\tilde{\mathbf p}\quad(3.9.3),\qquad \tilde{\mathbf P}=N\epsilon_0\alpha\left(\tilde{\mathbf E}+\frac1{3\epsilon_0}\tilde{\mathbf P}\right)\quad(3.9.4)$$

Con $\tilde{\mathbf P}=\epsilon_0\chi^{(1)}\tilde{\mathbf E}$ (3.9.5):

$$\chi^{(1)}=\frac{N\alpha}{1-\frac13N\alpha}\quad(3.9.6)$$

Para $\alpha>0$, $\chi^{(1)}$ es mayor que $N\alpha$ y crece más rápido que linealmente con $N$. Con $\epsilon^{(1)}=1+\chi^{(1)}$
(3.9.7), **ley de Lorentz–Lorenz** (a menudo con $n^2$ en lugar de $\epsilon^{(1)}$):

$$\frac{\epsilon^{(1)}-1}{\epsilon^{(1)}+2}=\tfrac13N\alpha\quad(3.9.8a),\qquad \frac{\epsilon^{(1)}+2}{3}=\frac1{1-\frac13N\alpha}\quad(3.9.8b),\qquad \chi^{(1)}=\frac{\epsilon^{(1)}+2}{3}N\alpha\quad(3.9.8c),\ \text{p. 197}$$

$(\epsilon^{(1)}+2)/3$ = **factor de realce de campo local** de la susceptibilidad lineal.

#### 3.9.2 Efectos de campo local en óptica no lineal (p. 197)

$E_{\rm loc}$ sigue dado por (3.9.2), pero $\tilde{\mathbf P}=\tilde{\mathbf P}^{\rm L}+\tilde{\mathbf P}^{\rm NL}$ (3.9.9), con $\tilde{\mathbf P}^{\rm L}=N\epsilon_0\gamma^{(1)}\tilde{\mathbf E}_{\rm loc}$ (3.9.10)
(lineal en el campo local, no necesariamente en el macroscópico; el libro escribe $\gamma^{(1)}$ aquí y $\alpha$ en la
ecuación siguiente para la misma polarizabilidad). Así
$\tilde{\mathbf P}^{\rm L}=N\epsilon_0\alpha\left(\tilde{\mathbf E}+\frac1{3\epsilon_0}\tilde{\mathbf P}^{\rm L}+\frac1{3\epsilon_0}\tilde{\mathbf P}^{\rm NL}\right)$ (3.9.11); resolviendo con (3.9.6), (3.9.7):

$$\tilde{\mathbf P}^{\rm L}=[\epsilon^{(1)}-1]\left(\epsilon_0\tilde{\mathbf E}+\tfrac13\tilde{\mathbf P}^{\rm NL}\right)\quad(3.9.12)$$

Desplazamiento $\tilde{\mathbf D}=\epsilon_0\tilde{\mathbf E}+\tilde{\mathbf P}=\epsilon_0\tilde{\mathbf E}+\tilde{\mathbf P}^{\rm L}+\tilde{\mathbf P}^{\rm NL}$ (3.9.13), luego (p. 198)

$$\tilde{\mathbf D}=\epsilon_0\epsilon^{(1)}\tilde{\mathbf E}+\left(\frac{\epsilon^{(1)}+2}{3}\right)\tilde{\mathbf P}^{\rm NL}\quad(3.9.14)$$

El término fuente de la ecuación de onda (que sale de $\partial_t^2\tilde{\mathbf D}$, Ec. (2.1.9a)) es $\tilde{\mathbf P}^{\rm NL}$ multiplicado por
$(\epsilon^{(1)}+2)/3$. Bloembergen (1965): **polarización fuente no lineal**

$$\tilde{\mathbf P}^{\rm NLS}=\left(\frac{\epsilon^{(1)}+2}{3}\right)\tilde{\mathbf P}^{\rm NL}\quad(3.9.15),\qquad \tilde{\mathbf D}=\epsilon_0\epsilon^{(1)}\tilde{\mathbf E}+\tilde{\mathbf P}^{\rm NLS}\quad(3.9.16)$$

$$\nabla\times\nabla\times\tilde{\mathbf E}+\frac{\epsilon^{(1)}}{c^2}\frac{\partial^2\tilde{\mathbf E}}{\partial t^2}=-\frac1{\epsilon_0c^2}\frac{\partial^2\tilde{\mathbf P}^{\rm NLS}}{\partial t^2}\quad(3.9.17)$$

Además, el campo que induce el dipolo es el local, mientras que $\chi$ relaciona $P^{\rm NLS}$ con el campo
macroscópico. Aproximando $\tilde{\mathbf P}\to\tilde{\mathbf P}^{\rm L}$ en (3.9.2):
$\tilde{\mathbf E}_{\rm loc}=\tilde{\mathbf E}+\frac13\chi^{(1)}\tilde{\mathbf E}=[1+\frac13(\epsilon^{(1)}-1)]\tilde{\mathbf E}$, o sea

$$\tilde{\mathbf E}_{\rm loc}=\left(\frac{\epsilon^{(1)}+2}{3}\right)\tilde{\mathbf E}\quad(3.9.18)$$

Segundo orden (p. 199): $P_i^{\rm NLS}(\omega_m+\omega_n)=\epsilon_0\sum_{jk}\sum_{(mn)}\chi^{(2)}_{ijk}(\omega_m+\omega_n,\omega_m,\omega_n)E_j(\omega_m)E_k(\omega_n)$ (3.9.19) con $E$
macroscópicos, $P_i^{\rm NLS}(\omega_m+\omega_n)=\left(\frac{\epsilon^{(1)}(\omega_m+\omega_n)+2}{3}\right)P_i^{\rm NL}(\omega_m+\omega_n)$ (3.9.20), y

$$P_i^{\rm NL}(\omega_m+\omega_n)=N\epsilon_0\sum_{jk}\sum_{(mn)}\beta_{ijk}(\omega_m+\omega_n,\omega_m,\omega_n)E_j^{\rm loc}(\omega_m)E_k^{\rm loc}(\omega_n)\quad(3.9.21)$$

$\beta_{ijk}$: **hiperpolarizabilidad de segundo orden**; $E_j^{\rm loc}(\omega_m)=\left(\frac{\epsilon^{(1)}(\omega_m)+2}{3}\right)E_j(\omega_m)$ (3.9.22). Resultado:

$$\chi^{(2)}_{ijk}(\omega_m+\omega_n,\omega_m,\omega_n)=\mathcal L^{(2)}(\omega_m+\omega_n,\omega_m,\omega_n)N\beta_{ijk}(\omega_m+\omega_n,\omega_m,\omega_n)\quad(3.9.23)$$
$$\mathcal L^{(2)}(\omega_m+\omega_n,\omega_m,\omega_n)=\left(\frac{\epsilon^{(1)}(\omega_m+\omega_n)+2}{3}\right)\left(\frac{\epsilon^{(1)}(\omega_m)+2}{3}\right)\left(\frac{\epsilon^{(1)}(\omega_n)+2}{3}\right)\quad(3.9.24)$$

factor de realce de campo local de $\chi^{(2)}$: p. ej. (3.6.18) debe multiplicarse por él. Tercer orden (p. 200):

$$\mathcal L^{(3)}(\omega_l+\omega_m+\omega_n,\omega_l,\omega_m,\omega_n)=\left(\frac{\epsilon^{(1)}(\omega_l+\omega_m+\omega_n)+2}{3}\right)\left(\frac{\epsilon^{(1)}(\omega_l)+2}{3}\right)\left(\frac{\epsilon^{(1)}(\omega_m)+2}{3}\right)\left(\frac{\epsilon^{(1)}(\omega_n)+2}{3}\right)\quad(3.9.25)$$

**Punto de vista de Mizrahi y Sipe (1986)** (no requiere la distinción algo arbitraria entre $P^{\rm NL}$ y
$P^{\rm NLS}$); THG en aproximación escalar. Polarización total a $3\omega$:

$$P(3\omega)=N\epsilon_0\alpha(3\omega)E_{\rm loc}(3\omega)+N\epsilon_0\gamma(3\omega,\omega,\omega,\omega)E^3_{\rm loc}(\omega)\quad(3.9.26)$$

($\gamma$: hiperpolarizabilidad de THG). Con (3.9.2) y (3.9.18):
$P(3\omega)=N\epsilon_0\alpha(3\omega)\left[E(3\omega)+\frac1{3\epsilon_0}P(3\omega)\right]+N\epsilon_0\gamma\left(\frac{\epsilon^{(1)}(\omega)+2}{3}\right)^3E(\omega)^3$ (3.9.27); despejando:

$$P(3\omega)=\frac{N\alpha(3\omega)E(3\omega)}{1-\frac13N\alpha(3\omega)}+\frac{N\gamma(3\omega,\omega,\omega,\omega)}{1-\frac13N\alpha(3\omega)}\left(\frac{\epsilon^{(1)}(\omega)+2}{3}\right)^3E(\omega)^3\quad(3.9.28)$$

(el primer término debería llevar $\epsilon_0$ para ser dimensionalmente coherente con (3.9.29)). Identificando
$P(3\omega)=\epsilon_0\chi^{(1)}(3\omega)E(3\omega)+\epsilon_0\chi^{(3)}(3\omega,\omega,\omega,\omega)E(\omega)^3$ (3.9.29), con
$\chi^{(1)}(3\omega)=\dfrac{N\alpha(3\omega)}{1-\frac13N\alpha(3\omega)}$ (3.9.30) (Lorentz–Lorenz; el texto dice "unusual", por "usual"), p. 201, y con (3.9.8b):

$$\chi^{(3)}(3\omega,\omega,\omega,\omega)=\left(\frac{\epsilon^{(1)}(\omega)+2}{3}\right)^3\left(\frac{\epsilon^{(1)}(3\omega)+2}{3}\right)N\gamma(3\omega,\omega,\omega,\omega)\quad(3.9.31)$$

que concuerda con (3.9.25). Experimentos: Maki et al. (1991). En materiales compuestos el campo local
varía mucho en el espacio y puede realzar la respuesta no lineal global (Fischer et al., 1995; Nelson
y Boyd, 1999).

---

## Tablas y datos numéricos útiles

| Magnitud | Expresión / valor | Ec., p. |
|---|---|---|
| Fuerza de oscilador | $f_{na}=2m\omega_{na}|\mu_{na}|^2/(3\hbar e^2)$, $\sum_nf_{na}=1$ | (3.5.23–24), p. 166 |
| Ancho de línea de Im $\chi^{(1)}$ | FWHM $=2\gamma_{na}$ (en frecuencia angular) | (3.5.21), p. 165 |
| Tasa de desfase | $\gamma_{nm}=\frac12(\Gamma_n+\Gamma_m)+\gamma^{(\rm col)}_{nm}$ | (3.3.25), p. 156 |
| Coeficiente $A$ de Einstein | $\Gamma=\omega^3|\mu|^2/(3\pi\epsilon_0\hbar c^3)$ | (3.5.39), p. 169 |
| Polarizabilidad máxima | $\gamma^{(1)}_{\max}=i6\pi(\lambda/2\pi)^3$ | (3.5.40), p. 169 |
| Sección eficaz máxima | $\sigma_{\max}=3\lambda^2/2\pi$ ($J=0\to1$); $\frac{g_b}{g_a}\frac{\lambda^2}{2\pi}$ en general | (3.5.41–42), p. 169 |
| Absorción ↔ susceptibilidad | $\alpha=2n''\omega/c=\chi^{(1)''}\omega/c$ (medio diluido); $\alpha=N\sigma$ | (3.5.30–35) |
| THG en Na (Miles y Harris) | $|\chi^{(3)}|/N\sim10^{-34}$ esu fuera de resonancia, $\gtrsim10^{-32}$ esu en picos (0.55–2.6 μm) | Fig. 3.2.6, p. 150 |
| Nº de términos | $\chi^{(2)}$: 6 (función de onda), 8 (matriz densidad, con $\gamma$); $\chi^{(3)}$: 24 y 48 | pp. 144, 147, 176, 183 |
| EIT en resonancia | $\chi^{(1)}=\frac{N}{\hbar}\frac{|\mu_{da}|^2i\gamma_c}{|\Omega_s|^2+\gamma_c\gamma_d}$ | (3.8.26), p. 191 |
| Campo local | $E_{\rm loc}=\frac{\epsilon^{(1)}+2}{3}E$; $\mathcal L^{(2)}$, $\mathcal L^{(3)}$ = productos de factores $(\epsilon^{(1)}(\omega_i)+2)/3$ | (3.9.18), (3.9.24–25) |
| Prob. 1 (respuesta) | vapor con $N=10^{17}$ cm⁻³, $\mu=2.5ea_0$, $\lambda=0.6$ μm, FWHM 10 GHz: $\alpha=8\times10^4$ cm⁻¹, $n^{(\max)}=1.2$ | p. 201 |

---

## Problemas del capítulo (pp. 201–204)

1. *Estimate of the refractive index of an atomic vapor.* Partiendo (por ejemplo) de (3.5.20), estimar
   la magnitud del coeficiente de absorción en resonancia de un vapor atómico denso con densidad
   $N=10^{17}$ cm⁻³, $\mu=2.5\,ea_0$, longitud de onda de vacío de la transición 0.6 μm y ensanchamiento
   homogéneo con ancho (FWHM) de 10 GHz. En las mismas condiciones, calcular el valor máximo de la
   parte real del índice cerca del pico de absorción (valores realistas en laboratorio; ver Maki et al.,
   1991). [Resp.: $\alpha=8\times10^4$ cm⁻¹, $n^{(\max)}=1.2$.]
2. *Estimate of the refractive index of glass.* Partiendo (por ejemplo) de (3.5.20), estimar la magnitud
   de la parte real del índice del vidrio en el visible, eligiendo valores realistas de densidad
   atómica, momento dipolar de transición y desintonía de la resonancia.
3. *Maximum value of the on-resonance cross section.* Verificar la Ec. (3.5.42).
4. *Permutation symmetry of the nonlinear susceptibility.* Mostrar que (3.6.24) tiene simetría de
   permutación total.
5. *Resonant nonlinear optical response.* Deducir con matriz densidad la contribución resonante a
   $\chi^{(3)}$ de THG en el esquema de cuatro niveles $a\to b\to c\to d$ con tres fotones $\omega$ y emisión a $3\omega$
   (figura: $b$, $c$, $d$ casi resonantes a $\omega$, $2\omega$, $3\omega$). Toda la población en el fundamental en
   equilibrio térmico. Como las frecuencias de entrada son iguales y solo se pide la parte resonante,
   la respuesta es un término (no 48). Partir de la expansión (3.4.16) y especializar.
   [Resp.: $\chi^{(3)}_{kjih}(3\omega,\omega,\omega,\omega)=\dfrac{N}{\epsilon_0\hbar^3}\dfrac{\mu^k_{ad}\mu^j_{dc}\mu^i_{cb}\mu^h_{ba}}{[(\omega_{da}-3\omega)-i\gamma_{da}][(\omega_{ca}-2\omega)-i\gamma_{ca}][(\omega_{ba}-\omega)-i\gamma_{ba}]}$.]
6. *Model calculation of the nonlinear susceptibility.* Cuatro campos con la misma polarización lineal
   (figura: $\omega_1$ casi resonante con $a\to b$, $\omega_2$ con $b\to c$, $\omega_3$ baja de $c$ a $d$, $\omega_4$ de $d$ a $a$); toda la
   población en $a$; solo las contribuciones resonantes indicadas. Puede especializarse (3.7.11) o
   repetir la derivación. (a) Calcular las cuatro susceptibilidades $\chi^{(3)}(\omega_4=\omega_1+\omega_2-\omega_3)$,
   $\chi^{(3)}(\omega_3=\omega_1+\omega_2-\omega_4)$, $\chi^{(3)}(\omega_1=\omega_3+\omega_4-\omega_2)$, $\chi^{(3)}(\omega_2=\omega_3+\omega_4-\omega_1)$ del proceso de mezcla de cuatro
   ondas y determinar cuándo son iguales. (b) Calcular $\chi^{(3)}(\omega_1=\omega_1+\omega_2-\omega_2)$ y
   $\chi^{(3)}(\omega_2=\omega_2+\omega_1-\omega_1)$ (impreso "$\omega_2+\omega_-\omega_1$"), que describen la absorción de dos fotones de $\omega_1$ y
   $\omega_2$, y cuándo son iguales. [Experimentos: Malcuit et al., 1985.]
7. *Generalization of Problems 4 and 5.* Repetir el cálculo de las contribuciones resonantes a $\chi^{(3)}$ de
   los casos de los Problemas 4 y 5 cuando cada nivel puede tener población en equilibrio térmico.
   Interpretar. [Nota: solución muy larga.] (Probablemente debería decir "Problemas 5 y 6", que son los
   de $\chi^{(3)}$ resonante.)
8. *Pressure-induced resonances in nonlinear optics.* Verificar que (3.7.11) se reduce a (3.2.33) cuando
   el amortiguamiento es despreciable. Mostrar también que, aun con amortiguamiento, la expresión
   general de 48 términos puede escribirse con 24 términos, 12 de los cuales contienen resonancias
   "inducidas por presión".
9. *Electromagnetically induced transparency.* Determinar cómo se modifican $\chi^{(1)}(2\omega_1+\omega_s)$ y
   $\chi^{(3)}(\omega_{\rm sum}=\omega_1+\omega_1+\omega_s)$ cuando el campo $\omega_s$ es fuerte y saturante; en condiciones adecuadas el
   campo fuerte reduce mucho la absorción lineal (indeseada) del campo suma sin afectar mucho la
   respuesta no lineal. En el texto se hizo con función de onda; aquí hacerlo con **matriz densidad**,
   con el esquema de la figura ($a\xrightarrow{\omega_1}b\xrightarrow{\omega_1}c\xleftrightarrow{\omega_s}d$, salida $2\omega_1+\omega_s$). El nivel $b$ está
   apreciablemente desintonizado de la resonancia de un fotón; los demás estados excitados se excitan
   casi en resonancia.

## Referencias principales (pp. 204–206)

- Mecánica cuántica: Bethe y Salpeter (1977); Merzbacher (1970); Sargent, Scully y Lamb (1974),
  *Laser Physics*.
- Teorías cuánticas de $\chi^{(n)}$: Bloembergen (1965), *Nonlinear Optics*; Bloembergen, Lotem y Lynch
  (1978); Boyd y Mukamel (1984) *Phys. Rev.* A29, 1973; Miles y Harris (1973) *IEEE JQE* 9, 470;
  Prior (1984); Rothberg (1987); Siegman (1986), *Lasers*; Ward (1965) *Rev. Mod. Phys.* 37, 1;
  Yee y Gustafson (1978). Lectura adicional: Armstrong, Bloembergen, Ducuing y Pershan (1962)
  *Phys. Rev.* 127, 1918; Butcher (1965); Hanna, Yuratich y Cotter (1979); Orr y Ward (1971)
  *Mol. Phys.* 20, 513; Shen (1984), *Principles of Nonlinear Optics*.
- EIT: Harris, Field e Imamoğlu (1990) *PRL* 64, 1107; Boller, Imamoğlu y Harris (1991) *PRL* 66, 2593;
  Hau et al. (1999) *Nature* 397, 594; Kash et al. (1999); revisiones: Fleischhauer, Imamoğlu y
  Marangos (2005) *Rev. Mod. Phys.* 77, 633; Harris (1997) *Physics Today*.
- Campo local: Born y Wolf (1975); Jackson (1975); Lorentz (1952); Maki et al. (1991) *PRL* 68, 972;
  Mizrahi y Sipe (1986) *Phys. Rev.* B34, 3700; Fischer et al. (1995); Nelson y Boyd (1999).

---

## Relación con el curso y con el proyecto final

- **Curso.** El cap. 3 no está en la lista explícita del programa (tema 4 = Boyd cap. 1; tema 5 = cap. 2;
  tema 6 = 4.1, 4.2, 7.1, 7.2), pero da el fundamento microscópico de lo que allí se usa: el origen de
  la simetría de permutación total de $\chi^{(2)}$ en medios sin pérdidas (§1.5, demostrada aquí con
  (3.2.28) y (3.6.24)), la regla de Miller y el modelo de Lorentz del cap. 1 (el cuántico (3.5.25) es
  Lorentz con varias resonancias pesadas por $f_{na}$), y el $\chi^{(3)}$ no resonante que define $n_2$ en §4.1.
  El factor de campo local $\mathcal L^{(3)}$ (3.9.25) aparece cuando se estiman $n_2$ de sólidos densos (§4.3).
- **Proyecto final (supercontinuo en guías de SiN / Si).** (i) En SiN y Si a 1.55 μm se trabaja lejos
  de resonancias electrónicas: vale el límite no resonante (3.2.33), con $\chi^{(3)}$ real, casi instantáneo y
  con simetría total — justificación de usar un $n_2$ constante en la NLSE. (ii) La resonancia de dos
  fotones (Fig. 3.1.2b; términos con $\omega_{ng}-2\omega$) es la que da la parte imaginaria de $\chi^{(3)}$, es decir la
  **absorción de dos fotones (TPA)**: en Si ($E_g\approx1.12$ eV $<2\hbar\omega$ a 1.55 μm) es fuerte; en SiN
  ($E_g\sim5$ eV) es despreciable — una de las razones de preferir SiN para SC. (iii) El análisis de
  los 48 términos muestra que la dispersión de $\chi^{(3)}$ viene de las desintonías respecto de las
  resonancias; para un SC que abarca una octava, la dependencia en frecuencia de $n_2$ (y de $\mathcal L^{(3)}$)
  puede no ser despreciable. (iv) Las nociones de matriz densidad ($\gamma_{nm}$, $T_2$) reaparecen en el cap. 6
  y en la respuesta Raman retardada del cap. 10.

---

## Erratas y dudas de lectura

1. p. 142, (3.2.25), 2.º término: se lee $[\boldsymbol\mu_{mg}\cdot\mathbf E(\omega_q)]$; por consistencia (y con (3.2.26)) debería ser
   $\mathbf E(\omega_p)$. 3.er término: denominador $(\omega^*_{mg}-\omega_q-\omega_q)$; debería ser $(\omega^*_{mg}-\omega_p-\omega_q)$.
2. p. 143, (3.2.26): exponente impreso $e^{-i(\omega_p+\omega_qt)}$ (debe ser $e^{-i(\omega_p+\omega_q)t}$) y 3.er denominador
   $(\omega^*_{mg}+\omega_q+\omega_q)$; por consistencia con (3.2.27) debería ser $(\omega^*_{mg}+\omega_p+\omega_q)$. En el apunte se
   escribió la forma corregida.
3. p. 147: "only four are displayed explicitly in Eq. (3.2.33)" y p. 184 "Equation (3.2.33) shows four
   of these terms": los cuatro términos explícitos están en (3.2.32); (3.2.33) es la forma compacta.
4. p. 164, (3.5.16): el segundo sumando tiene prefactor $N/\hbar$; debería ser $N/(\epsilon_0\hbar)$.
5. p. 167, (3.5.32)–(3.5.34): con $\langle\mu\rangle=\gamma^{(1)}E$ y $P=\epsilon_0\chi E$ resultaría $\chi^{(1)}=N\gamma^{(1)}/\epsilon_0$; la pareja
   $\chi^{(1)}=N\gamma^{(1)}$ y (3.5.34) (con $1/\epsilon_0$) requiere $\langle\mu\rangle=\epsilon_0\gamma^{(1)}E$, consistente con (3.9.1). Con esa
   lectura (3.5.40) da $\gamma^{(1)}$ en m³ y $\sigma_{\max}=3\lambda^2/2\pi$ cuadra.
6. p. 171, (3.6.7), 2.º término: numerador impreso $[\boldsymbol\mu_{n\nu}\cdot\mathbf E(\omega_q)][\boldsymbol\mu_{\nu m}\cdot\mathbf E(\omega_q)]$; de (3.6.6) debería ser
   $[\boldsymbol\mu_{n\nu}\cdot\mathbf E(\omega_p)][\boldsymbol\mu_{\nu m}\cdot\mathbf E(\omega_q)]$ (consistente con el término (b) de (3.6.13)).
7. p. 172, (3.6.12): aparece "[lll]" antes de $P_i^{(2)}$ (resto de composición tipográfica).
8. p. 178, tras (3.6.20): "$\langle\psi|$ represents the Hermitian adjoint of $\langle\psi|$"; debería ser "of $|\psi\rangle$".
9. p. 183, (3.7.11): algunos subíndices de los denominadores ($\omega_{n\nu}$ en $a_2$, $b_1$; $\omega_{mn}$ en $b_2$; $\gamma_{m\nu}$
   con $\omega_{\nu m}$ en $d_1$) no siguen el orden "natural" anunciado; se transcribió tal cual. Verificar contra
   otra fuente antes de usarla numéricamente.
10. p. 184: "see Problem 5" para la reducción de (3.7.11) a (3.2.33); el problema correspondiente es el 8.
11. p. 190, (3.8.18): "$\Omega_s^2C_d$" debería ser $\Omega_s^*C_d$. (3.8.21) imprime $(\delta+\Delta)$ en numerador y
    denominador; por (3.8.19) y (3.8.23) debería ser $(\delta-\Delta)$. "levels d and e" → "d and c".
    (3.8.25)–(3.8.26): falta $\epsilon_0$ en $N/\hbar$ (comparar con (3.8.23)).
12. p. 192, (3.8.27)–(3.8.29): mezcla de $\omega_c$ y $\omega_s$ en los exponentes del nivel $d$ (debe ser $\omega_s$), y en
    (3.8.29) falta una $i$ en algunos exponentes $e^{-(2\omega+\omega_s)t}$.
13. p. 193, (3.8.36): el corchete se imprime $\left[\frac{|\Omega_{dc}|^2}{\delta_2(\delta_2+\Delta)}\right]^{-1}$; debe ser $\left[1-\frac{|\Omega_{dc}|^2}{\delta_2(\delta_2+\Delta)}\right]^{-1}$
    para dar (3.8.37), que es correcta.
14. p. 194, (3.8.39): se lee $\mu_{bc}$ y $E_c$ donde corresponde $\mu_{dc}$ y $E_s$ (el denominador sale casi ilegible
    en el escaneo; se reconstruyó de (3.8.37)). (3.8.40)–(3.8.41): prefactor $3\epsilon_0\hbar$; dimensionalmente,
    con $p$ de (3.8.39) que lleva $\hbar^3$, debería ser $3\epsilon_0\hbar^3$.
15. p. 197, (3.9.10) usa $\gamma^{(1)}$ y (3.9.11) $\alpha$ para la misma polarizabilidad.
16. p. 200, (3.9.28): el primer término no lleva $\epsilon_0$ (sí lo lleva (3.9.29)). p. 201: "unusual
    Lorentz Lorenz law" debería ser "usual".
17. p. 203, Problema 6(b): "$\chi^{(3)}(\omega_2=\omega_2+\omega_-\omega_1)$" → $\omega_2+\omega_1-\omega_1$. Problema 7: dice "Problems 4 and
    5"; el contexto (contribuciones resonantes a $\chi^{(3)}$) sugiere 5 y 6.
18. p. 148, Fig. 3.2.4: las energías de los niveles del Na citadas arriba son lecturas aproximadas de la
    figura (no hay tabla en el texto).

