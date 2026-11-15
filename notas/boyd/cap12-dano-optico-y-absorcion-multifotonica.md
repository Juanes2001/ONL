# Capítulo 12 — Optically Induced Damage and Multiphoton Absorption (Boyd, 3.ª ed.)

Páginas del libro 543–560 (PDF 561–578). Leído el 2026-11-14.

Fuente: R. W. Boyd, *Nonlinear Optics*, 3.ª ed., Academic Press/Elsevier, 2008, cap. 12.
Las citas de página son páginas del libro (sumar 18 para la página del PDF).

Convención del libro (SI): $\tilde E(t)=Ee^{-i\omega t}+\text{c.c.}$, $I=2n\epsilon_0c|E|^2$.

---

## Resumen del capítulo

Capítulo corto (nuevo desde la 2.ª ed.) sobre los dos procesos que limitan en la práctica la
intensidad utilizable en óptica no lineal: el **daño óptico inducido** y la **absorción
multifotónica**. Primero clasifica los mecanismos de daño según la duración del pulso y la
intensidad (absorción lineal y calentamiento para CW y pulsos $\gtrsim 1\ \mu$s; ruptura por
avalancha para pulsos $\lesssim 1\ \mu$s entre $10^9$ y $10^{12}$ W/cm²; ionización multifotónica entre
$10^{12}$ y $10^{16}$ W/cm²; ionización directa de campo por encima de $10^{20}$ W/cm²) y explica por qué
el daño ocurre preferentemente en la cara de **salida** de un componente. Desarrolla el modelo
cuantitativo de **avalancha** (calentamiento tipo Drude de electrones libres, crecimiento
exponencial de la densidad electrónica y criterio $N(T_p)>N_{\rm th}\sim10^{18}$ cm⁻³), que da un umbral
del orden de 40 GW/cm² para pulsos de ns. Discute la ley empírica $F_{\rm th}\propto T_p^{1/2}$ (10 ps–10 ns),
interpretada por difusión térmica $L=(DT_p)^{1/2}$, y la fotoionización directa a $E_{\rm at}=5\times10^{11}$ V/m.
La segunda mitad deriva, con teoría de perturbaciones dependiente del tiempo, la **regla de oro de
Fermi** para absorción de uno y dos fotones: tasa, sección eficaz $\sigma^{(1)}$, sección eficaz de dos
fotones $\sigma^{(2)}$ (también en unidades de fotones, $\bar\sigma^{(2)}$, con estimación numérica
$\approx2.5\times10^{-58}$ m⁴ s/fotón²) y la generalización a $N$ fotones.

---

## Secciones

### 12.1 Introduction to Optical Damage (p. 543)

El daño óptico limita la potencia máxima transmisible por un material y, por tanto, el campo $E$
con que se puede excitar la respuesta no lineal; la tecnología láser actual supera los umbrales de
daño de **todos** los materiales conocidos. Mecanismos y condiciones aproximadas (p. 543):

| Mecanismo | Régimen dominante |
|---|---|
| Absorción lineal → calentamiento local y fractura | CW y pulsos largos ($\gtrsim 1\ \mu$s) |
| Ruptura por avalancha (*avalanche breakdown*) | pulsos $\lesssim 1\ \mu$s, $I\sim10^{9}$–$10^{12}$ W/cm² |
| Ionización o disociación multifotónica | $I\sim10^{12}$–$10^{16}$ W/cm² |
| Ionización directa de campo (un ciclo) | $I>10^{20}$ W/cm² |

Observaciones empíricas (p. 544): con haz colimado el daño ocurre a umbral menor en las
**superficies** que en el volumen (grietas e imperfecciones aumentan el campo local o aportan
electrones casi libres que inician la avalancha). Además, el umbral es menor en la **superficie de
salida** que en la de entrada (Lowdermilk y Milam, 1981): por las condiciones de frontera en la
interfaz dieléctrico/aire, la onda reflejada interfiere destructivamente con la incidente en la cara
de entrada (deenhancement) y constructivamente en la de salida (enhancement). **Fig. 12.1.1**:
diagrama de vectores de campo incidente + reflejado en cada cara. Otro mecanismo de la asimetría:
difracción en defectos de la cara frontal que produce *hot spots* en la cara de salida (Genin *et
al.*, 2000).

### 12.2 Avalanche-Breakdown Model (p. 544)

Mecanismo dominante para la mayoría de los láseres pulsados. Un número pequeño $N_0$ de electrones
libres iniciales se acelera con el campo láser, ioniza por impacto otros átomos, y los nuevos
electrones repiten el proceso; parte de la energía calienta el material (fractura o fusión). Los
electrones iniciales provienen de excitación térmica, túnel (mecanismo de Keldysh; Ammosov *et al.*,
1986), excitación multifotónica o defectos del cristal (p. 545).

Energía entregada a un electrón inicialmente en reposo bajo un campo cuasiestático $\tilde E$ durante un
tiempo $t$:

$$Q=e\tilde E d,\qquad d=\tfrac12at^2=\tfrac12(e\tilde E/m)t^2 \qquad (12.2.1),\ \text{p. 545}$$

$$Q=e^2\tilde E^2t^2/2m\qquad\text{para } t\lesssim\tau, \qquad (12.2.2)$$

con $\tau$ el tiempo medio entre colisiones. Para $t>\tau$, la energía es la ganada en un intervalo
$\tau$ ($e^2\tilde E^2\tau^2/2m$) por el número de intervalos $t/\tau$:

$$Q=e^2\tilde E^2t\tau/2m\qquad\text{para } t>\tau, \qquad (12.2.3)$$

$$P=\frac{dQ}{dt}=e^2\tilde E^2\tau/2m. \qquad (12.2.4)$$

Nota al pie (p. 545): también se deduce del calentamiento Joule de un conductor, $NP=\tfrac12\sigma\tilde E^2$,
con la conductividad de Drude $\sigma=\dfrac{(Ne^2/m)\tau}{1+\omega^2\tau^2}$; esto generaliza (12.2.4) y se reduce a ella
para $\omega\tau\ll1$.

Evolución de la densidad de electrones libres (p. 546):

$$\frac{dN}{dt}=\frac{fNP}{W}, \qquad (12.2.5)$$

$W$ = umbral de ionización, $P$ dada por (12.2.4), $f$ = fracción de la potencia absorbida que produce
más ionización ($1-f$ va a calentamiento). Solución:

$$N(t)=N_0e^{gt},\qquad g=\frac{fe^2\tilde E^2\tau}{2Wm}. \qquad (12.2.6)$$

Criterio de daño: $N(T_p)$ al final del pulso de duración $T_p$ supera $N_{\rm th}$ (a menudo $\sim10^{18}$ cm⁻³):

$$\frac{fe^2\tilde E^2\tau T_p}{2mW}>\ln(N_{\rm th}/N_0). \qquad (12.2.7)$$

El lado derecho depende débilmente de $N_{\rm th}$ y $N_0$, y vale del orden de 30. Intensidad umbral:

$$I_{\rm th}=n\epsilon_0c\langle\tilde E^2\rangle=2n\epsilon_0c\,\frac{Wm}{fe^2\tau T_p}\ln(N_{\rm th}/N_0). \qquad (12.2.8)$$

**Ejemplo numérico (p. 546):** $n\approx1$, $W=5$ eV, $\tau\approx10^{-15}$ s, $T_p\approx10^{-9}$ s, $f\approx0.01$
→ $I_{\rm th}\simeq40$ GW/cm², en acuerdo razonable con las medidas. (Comprobación propia: con $\ln=30$ sale
$\approx4.5\times10^{10}$ W/cm².) El modelo predice que el daño depende **solo de la intensidad**.

### 12.3 Influence of Laser Pulse Duration (p. 546)

Ley de escala bien establecida para $T_p$ entre ~10 ps y 10 ns: la **fluencia** umbral crece como
$T_p^{1/2}$ y la **intensidad** umbral decrece como $T_p^{-1/2}$; es decir, el daño depende de la media
geométrica de fluencia e intensidad. Esto contradice (12.2.8). **Fig. 12.3.1** (Stuart *et al.*, 1995):
fluencia de daño (J/cm², escala log 1–50) contra ancho de pulso (0.1–1000 ps) para sílice fundida y
CaF₂; por encima de ~10 ps los datos siguen rectas $\tau^{1/2}$ (sílice ~ 2–3 J/cm² a ~1 ps, ~30–40
J/cm² a ~1 ns); por debajo de ~10 ps se apartan (saturan en ~2 J/cm²). Referencias: Lowdermilk y
Milam (1981), Du *et al.* (1994).

Interpretación: la avalancha atribuye el daño al calentamiento localizado; la temperatura obedece la
ecuación de transporte de calor (ver (4.5.2)):

$$(\rho C)\frac{\partial\tilde T}{\partial t}-\kappa\nabla^2\tilde T=N(1-f)\tilde P, \qquad (12.3.1),\ \text{p. 547}$$

$\kappa$ = conductividad térmica, $(\rho C)$ = capacidad calorífica por unidad de volumen. Ignorando la
fuente y estimando la distancia de difusión $L$ en un tiempo $T_p$ en 1D (**Fig. 12.3.2**), reemplazando
derivadas por cocientes:

$$(\rho C)\frac{\Delta T}{T_p}=\kappa\frac{\Delta T}{L^2}, \qquad (12.3.2),\ \text{p. 548}$$

$$L=(DT_p)^{1/2},\qquad D=\kappa/\rho c\ \text{(constante de difusión)}. \qquad (12.3.3)$$

El calor se reparte sobre una región $\propto T_p^{1/2}$ y el umbral se eleva en ese factor. Bloembergen
(1997) dudó de que $D$ típico sea suficientemente grande; aun así, cálculos numéricos detallados
(Stuart *et al.*, 1995, 1996) con ionización multifotónica, calentamiento Joule y avalancha
concuerdan con los experimentos.

### 12.4 Direct Photoionization (p. 548)

El campo arranca electrones del núcleo; domina si el campo pico supera el campo atómico

$$E_{\rm at}=e/4\pi\epsilon_0a_0^2=5\times10^{11}\ \text{V/m},$$

que se alcanza a

$$I_{\rm at}=\tfrac12n\epsilon_0cE_{\rm at}^2\approx4\times10^{16}\ \text{W/cm}^2=4\times10^{20}\ \text{W/m}^2.$$

(El factor ½ corresponde a tomar $E_{\rm at}$ como amplitud **pico** del campo real, $=2|E|$, con lo que
coincide con $I=2n\epsilon_0c|E|^2$.) Para pulsos de 100 fs o más, el daño ocurre a intensidades mucho
menores por los otros procesos. Se amplía en el cap. 13 (p. 549).

**Duda de lectura:** en 12.1 (p. 543) la ionización directa de campo se asocia a $I>10^{20}$ W/cm²,
mientras que aquí $I_{\rm at}\approx4\times10^{16}$ W/cm² ($=4\times10^{20}$ W/m²). Probablemente el "$10^{20}$" de la
p. 543 está en W/m² y no en W/cm²; se deja anotado.

### 12.5 Multiphoton Absorption and Multiphoton Ionization (p. 549)

**Fig. 12.5.1**: diagramas de absorción de uno, dos, tres y $N$ fotones. La absorción de dos fotones
fue observada por primera vez por Kaiser y Garrett (1961). Motivos de interés (p. 549–550):

1. Espectroscopía multifotónica: estados altos y estados prohibidos por reglas de selección desde
   el fundamental.
2. Microscopía de dos fotones (Denk *et al.*, 1990; Xu y Webb, 1997): menos fondo en medios muy
   dispersivos (se dispersa menos a $\lambda$ larga y la excitación solo ocurre en el volumen focal).
   **Fig. 12.5.2**: fluorescencia de fluoresceína 20 μM en agua con excitación (a) de un fotón (todo
   el cono) y (b) de dos fotones (solo el foco). Fotos de W. Webb.
3. La absorción e ionización multifotónicas causan daño y permiten escribir estructuras
   permanentes de índice en el interior de materiales (escritura con fs).
4. Es un mecanismo de pérdida no lineal que limita dispositivos como los conmutadores ópticos
   (ver §7.3).

En principio ya se sabe calcularlo (cap. 3): absorción lineal $\propto\text{Im}\,\chi^{(1)}(\omega)$; dos
fotones $\propto\text{Im}\,\chi^{(3)}(\omega=\omega+\omega-\omega)$. Pero el método se vuelve tedioso para órdenes
superiores ($\chi^{(5)}$ para tres fotones, etc.), así que se desarrolla un enfoque más simple (p. 550).

#### 12.5.1 Theory of Single- and Multiphoton Absorption and Fermi's Golden Rule (p. 550)

Mismo procedimiento que §3.2. Ecuación de Schrödinger:

$$i\hbar\frac{\partial\psi(\mathbf r,t)}{\partial t}=\hat H\psi(\mathbf r,t), \qquad (12.5.1),\ \text{p. 551}$$

$$\hat H=\hat H_0+\hat V(t), \qquad (12.5.2)$$

$$\hat V(t)=-\hat\mu\tilde E(t),\qquad \hat\mu=-e\hat r, \qquad (12.5.3)$$

$$\tilde E(t)=Ee^{-i\omega t}+\text{c.c.}\ \text{(encendido súbitamente en } t=0), \qquad (12.5.4)$$

$$\psi_n(\mathbf r,t)=u_n(\mathbf r)e^{-i\omega_nt},\qquad \omega_n=E_n/\hbar, \qquad (12.5.5)$$

$$\hat H_0u_n(\mathbf r)=E_nu_n(\mathbf r), \qquad (12.5.6)$$

$$i\hbar\frac{\partial\psi}{\partial t}=(\hat H_0+\hat V(t))\psi, \qquad (12.5.7)$$

$$\psi(\mathbf r,t)=\sum_la_l(t)u_l(\mathbf r)e^{-i\omega_lt}. \qquad (12.5.8)$$

Sustituyendo:

$$i\hbar\sum_l\frac{da_l}{dt}u_le^{-i\omega_lt}+i\hbar\sum_l(-i\omega_l)a_lu_le^{-i\omega_lt}=\sum_la_lE_lu_le^{-i\omega_lt}+\sum_la_l\hat Vu_le^{-i\omega_lt}. \qquad (12.5.9)$$

El 2.º y 3.er término se cancelan ($E_l=\hbar\omega_l$). Multiplicando por $u_m^*$ e integrando, con la
ortonormalidad

$$\int u_m^*u_l\,d^3r=\delta_{ml}, \qquad (12.5.10),\ \text{p. 552}$$

$$i\hbar\frac{da_m}{dt}=\sum_la_l(t)V_{ml}e^{-i\omega_{lm}t},\qquad \omega_{lm}=\omega_l-\omega_m, \qquad (12.5.11)$$

$$V_{ml}=\int u_m^*\hat Vu_l\,d^3r. \qquad (12.5.12)$$

Perturbaciones: $V_{ml}\to\lambda V_{ml}$, $\lambda\in[0,1]$,

$$a_m=a_m^{(0)}+\lambda a_m^{(1)}+\lambda^2a_m^{(2)}+\cdots \qquad (12.5.13)$$

$$\frac{da_m^{(N)}}{dt}=(i\hbar)^{-1}\sum_la_l^{(N-1)}V_{ml}e^{-i\omega_{lm}t},\qquad N=1,2,3,\dots \qquad (12.5.14)$$

#### 12.5.2 Linear Absorption (p. 552)

$N=1$, átomo inicialmente en $g$:

$$a_g^{(0)}(t)=1,\qquad a_l^{(0)}(t)=0\ \ (l\ne g), \qquad (12.5.15)$$

$$V_{mg}=-\mu_{mg}(Ee^{-i\omega t}+E^*e^{i\omega t}). \qquad (12.5.16)$$

Entonces $da_m^{(1)}/dt=-(i\hbar)^{-1}\mu_{mg}[Ee^{i(\omega_{mg}-\omega)t}+E^*e^{i(\omega_{mg}+\omega)t}]$ (p. 553), que integrada da

$$a_m^{(1)}(t)=\frac{\mu_{mg}E}{\hbar(\omega_{mg}-\omega)}\left[e^{i(\omega_{mg}-\omega)t}-1\right]+\frac{\mu_{mg}E^*}{\hbar(\omega_{mg}+\omega)}\left[e^{i(\omega_{mg}+\omega)t}-1\right]. \qquad (12.5.17)$$

**Fig. 12.5.3**: (a) el primer término es resonante para absorción de un fotón; (b) el segundo (si
$m$ está por debajo de $g$) para emisión estimulada. Se descarta el segundo: **aproximación de onda
rotante**. Probabilidad:

$$p_m^{(1)}(t)=|a_m^{(1)}|^2=\frac{|\mu_{mg}E|^2}{\hbar^2}\left|\frac{e^{i(\omega_{mg}-\omega)t}-1}{\omega_{mg}-\omega}\right|^2=\frac{|\mu_{mg}E|^2}{\hbar^2}\frac{4\sin^2[(\omega_{mg}-\omega)t/2]}{(\omega_{mg}-\omega)^2}\equiv\frac{|\mu_{mg}E|^2}{\hbar^2}f(t), \qquad (12.5.18)$$

$$f(t)=\frac{4\sin^2[(\omega_{mg}-\omega)t/2]}{(\omega_{mg}-\omega)^2}. \qquad (12.5.19)$$

Para $t$ grande (p. 554):

$$f(t)=t^2\left(\frac{\sin^2x}{x^2}\right),\qquad x\equiv(\omega_{mg}-\omega)t/2. \qquad (12.5.20)$$

Pico $t^2$, ancho del lóbulo central del orden de $2\pi/t$ (**Fig. 12.5.4**: $f$ contra $x$ y contra
$\omega_{mg}-\omega$, con marcas en $x=\pm2\pi$ ↔ $\omega_{mg}-\omega=\pm4\pi/t$), área $\sim2\pi t$, de modo que

$$\lim_{t\to\infty}f(t)=2\pi t\,\delta(\omega_{mg}-\omega), \qquad (12.5.21)$$

$$p_m^{(1)}(t)=\frac{|\mu_{mg}E|^2t}{\hbar^2}2\pi\delta(\omega_{mg}-\omega). \qquad (12.5.22)$$

(**Duda de lectura, Fig. 12.5.4**: las marcas $x=\pm2\pi$ y $\omega_{mg}-\omega=\pm4\pi/t$ son consistentes entre sí,
pero los primeros ceros de $\sin^2x/x^2$ están en $x=\pm\pi$ ($\omega_{mg}-\omega=\pm2\pi/t$); el dibujo es solo
esquemático. Además, el pie de figura remite a "Eq. (12.5.20)".)

Físicamente $\omega_{mg}$ está ensanchada (**Fig. 12.5.5**): densidad de estados finales (forma de línea
atómica) $\rho_f(\omega_{mg})$, normalizada

$$\int_0^\infty\rho_f(\omega_{mg})\,d\omega_{mg}=1, \qquad (12.5.23),\ \text{p. 555}$$

p. ej. la lorentziana

$$\rho_f(\omega_{mg})=\frac1\pi\frac{\Gamma/2}{(\bar\omega_{mg}-\omega_{mg})^2+(\Gamma/2)^2}, \qquad (12.5.24)$$

$\bar\omega_{mg}$ = centro de línea, $\Gamma$ = FWHM en frecuencia angular (para ensanchamiento por vida media,
$\Gamma$ = tasa de decaimiento de población del nivel superior). Promediando:

$$p_m^{(1)}(t)=\frac{|\mu_{mg}E|^2t}{\hbar^2}\int_0^\infty\rho_f(\omega_{mg})2\pi\delta(\omega_{mg}-\omega)d\omega_{mg}=\frac{2\pi|\mu_{mg}E|^2t}{\hbar^2}\rho_f(\omega_{mg}=\omega). \qquad (12.5.25)$$

Crece linealmente con $t$ → tasa de absorción lineal (caso especial de la **regla de oro de Fermi**):

$$R_{mg}^{(1)}=\frac{p_m^{(1)}(t)}{t}=\frac{2\pi|\mu_{mg}E|^2}{\hbar^2}\rho_f(\omega_{mg}=\omega). \qquad (12.5.26)$$

Sección eficaz de absorción (p. 556):

$$R_{mg}^{(1)}=\sigma_{mg}^{(1)}(\omega)I,\qquad I=2n\epsilon_0c|E|^2, \qquad (12.5.27)$$

$$\sigma_{mg}^{(1)}(\omega)=\frac{\pi}{n\epsilon_0c}\frac{|\mu_{mg}|^2}{\hbar^2}\rho_f(\omega_{mg}=\omega). \qquad (12.5.28)$$

#### 12.5.3 Two-Photon Absorption (p. 556)

Se resuelve (12.5.14) para $N=1$ (igual a (12.5.17), conservando solo el primer término) y luego
$N=2$. Niveles (**Fig. 12.5.6**): $g\to$ (virtual, cerca de $m$) $\to n$, dos fotones $\omega$. Se toma

$$V_{nm}=-\mu_{nm}(Ee^{-i\omega t}+E^*e^{i\omega t})\simeq-\mu_{nm}Ee^{-i\omega t}, \qquad (12.5.29)$$

(se descarta la contribución de frecuencia negativa, igual que en (12.5.17)). Entonces (p. 557)

$$\frac{d}{dt}a_n^{(2)}(t)=(i\hbar)^{-1}\sum_ma_m^{(1)}V_{nm}e^{-i\omega_{mn}t}=-(i\hbar)^{-1}\sum_m\frac{\mu_{nm}\mu_{mg}E^2}{\hbar(\omega_{mg}-\omega)}\left[e^{i(\omega_{ng}-2\omega)t}-e^{i(\omega_{nm}-\omega)t}\right]. \qquad (12.5.30)$$

Se descarta el segundo término (respuesta transitoria, no lleva a absorción de dos fotones) y se
integra:

$$a_n^{(2)}(t)=\sum_m\frac{\mu_{nm}\mu_{mg}E^2}{\hbar^2(\omega_{mg}-\omega)}\left[\frac{e^{i(\omega_{ng}-2\omega)t}-1}{\omega_{ng}-2\omega}\right]. \qquad (12.5.31)$$

**Errata:** en el libro el exponente se lee $e^{i(\omega_{mg}-2\omega)t}$ en (12.5.31) y (12.5.32); por
consistencia con (12.5.30) y con el denominador debe ser $e^{i(\omega_{ng}-2\omega)t}$ (verificado a 200 dpi).

$$p_n^{(2)}(t)=|a_n^{(2)}|^2=\left|\sum_m\frac{\mu_{nm}\mu_{mg}E^2}{\hbar^2(\omega_{mg}-\omega)}\right|^2\left|\frac{e^{i(\omega_{ng}-2\omega)t}-1}{\omega_{ng}-2\omega}\right|^2. \qquad (12.5.32)$$

Para $t$ grande (como en (12.5.18)–(12.5.22)):

$$p_n^{(2)}(t)=\left|\sum_m\frac{\mu_{nm}\mu_{mg}E^2}{\hbar^2(\omega_{mg}-\omega)}\right|^22\pi t\,\delta(\omega_{ng}-2\omega), \qquad (12.5.33)$$

y con densidad de estados del nivel $n$:

$$p_n^{(2)}(t)=\left|\sum_m\frac{\mu_{nm}\mu_{mg}E^2}{\hbar^2(\omega_{mg}-\omega)}\right|^22\pi t\,\rho_f(\omega_{ng}=2\omega). \qquad (12.5.34)$$

Tasa y sección eficaz de dos fotones:

$$R_{ng}^{(2)}=\frac{p_n^{(2)}(t)}{t}, \qquad (12.5.35)$$

$$R_{ng}^{(2)}=\sigma_{ng}^{(2)}(\omega)I^2,\qquad I=2n\epsilon_0c|E|^2, \qquad (12.5.36)$$

$$\sigma_{ng}^{(2)}(\omega)=\frac{1}{4n^2\epsilon_0^2c^2}\left|\sum_m\frac{\mu_{nm}\mu_{mg}}{\hbar^2(\omega_{mg}-\omega)}\right|^22\pi\rho_f(\omega_{ng}=2\omega). \qquad (12.5.37),\ \text{p. 558}$$

Con intensidades en fotones cm⁻² s⁻¹ (convención experimental habitual):

$$R_{ng}^{(2)}=\bar\sigma_{ng}^{(2)}(\omega)\bar I^2,\qquad \bar I=\frac{2n\epsilon_0c}{\hbar\omega}|E|^2, \qquad (12.5.38)$$

$$\bar\sigma_{ng}^{(2)}(\omega)=\frac{\omega^2}{4n^2\epsilon_0^2c^2}\left|\sum_m\frac{\mu_{nm}\mu_{mg}}{\hbar(\omega_{mg}-\omega)}\right|^22\pi\rho_f(\omega_{ng}=2\omega). \qquad (12.5.39)$$

**Estimación numérica (p. 558):** un solo nivel domina, transición de un fotón muy no resonante
($\omega_{mg}-\omega\approx\omega$), láser en el pico de la resonancia de dos fotones,
$\rho_f(\omega_{ng}=2\omega)\approx(2\pi\Gamma_n)^{-1}$ ($\Gamma_n$ = ancho del nivel $n$); con $n=1$:

$$\bar\sigma_{ng}^{(2)}\approx\frac{|\mu_{nm}\mu_{mg}|^2}{4\epsilon_0^2\hbar^2c^2\Gamma_n}. \qquad (12.5.40)$$

Con $\mu_{nm}\sim\mu_{mg}\sim ea_0=8\times10^{-30}$ C m y $\Gamma_n=2\pi(1\times10^{13})$ rad/s:

$$\bar\sigma_{ng}^{(2)}\approx2.5\times10^{-58}\ \frac{\text{m}^4\,\text{s}}{\text{fotón}^2}. \qquad (12.5.41)$$

(Comprobación propia: sale $\approx2.1\times10^{-58}$, consistente con el orden.) Acuerdo en orden de
magnitud con Xu y Webb (1996) para fluoróforos moleculares; Drobizhev *et al.* (2001) reportan
$1.1\times10^{-54}$ m⁴ s/fotón² en un dendrímero. (Equivalencia útil, no del libro: 1 GM = $10^{-50}$ cm⁴ s/fotón
$=10^{-58}$ m⁴ s/fotón, así que (12.5.41) ≈ 2.5 GM.)

#### 12.5.4 Multiphoton Absorption (p. 559)

Generalización a órdenes superiores:

$$R_{mg}^{(1)}=\left|\frac{\mu_{mg}E}{\hbar}\right|^22\pi\rho_f(\omega_{mg}-\omega),$$

$$R_{ng}^{(2)}=\left|\sum_m\frac{\mu_{nm}\mu_{mg}E^2}{\hbar^2(\omega_{mg}-\omega)}\right|^22\pi\rho_f(\omega_{ng}-2\omega),$$

$$R_{og}^{(3)}=\left|\sum_{mn}\frac{\mu_{on}\mu_{nm}\mu_{mg}E^3}{\hbar^3(\omega_{ng}-2\omega)(\omega_{mg}-\omega)}\right|^22\pi\rho_f(\omega_{og}-3\omega),$$

$$R_{pg}^{(4)}=\left|\sum_{omn}\frac{\mu_{po}\mu_{on}\mu_{nm}\mu_{mg}E^4}{\hbar^4(\omega_{og}-3\omega)(\omega_{ng}-2\omega)(\omega_{mg}-\omega)}\right|^22\pi\rho_f(\omega_{pg}-4\omega),$$

y así sucesivamente. (Nota: aquí $\rho_f(\omega_{mg}-\omega)$ denota lo mismo que antes $\rho_f(\omega_{mg}=\omega)$, la
forma de línea evaluada a la desintonía; cambio de notación del libro. La tasa de $N$ fotones va
como $|E|^{2N}\propto I^N$.)

---

## Tablas y datos numéricos útiles

| Magnitud | Valor | Página |
|---|---|---|
| Rangos de intensidad por mecanismo de daño | ver tabla de §12.1 | 543 |
| $N_{\rm th}$ típico para daño por avalancha | $\sim10^{18}$ cm⁻³ | 546 |
| $\ln(N_{\rm th}/N_0)$ | $\sim30$ | 546 |
| $I_{\rm th}$ avalancha ($W=5$ eV, $\tau=1$ fs, $T_p=1$ ns, $f=0.01$) | $\simeq40$ GW/cm² | 546 |
| Ley de escala (10 ps–10 ns) | $F_{\rm th}\propto T_p^{1/2}$, $I_{\rm th}\propto T_p^{-1/2}$ | 546 |
| Campo atómico $E_{\rm at}=e/4\pi\epsilon_0a_0^2$ | $5\times10^{11}$ V/m | 548 |
| Intensidad atómica $I_{\rm at}$ | $4\times10^{16}$ W/cm² | 548 |
| $ea_0$ | $8\times10^{-30}$ C m | 558 |
| $\bar\sigma^{(2)}$ típico (estimación) | $2.5\times10^{-58}$ m⁴ s/fotón² | 558 |
| $\bar\sigma^{(2)}$ dendrímero (Drobizhev 2001) | $1.1\times10^{-54}$ m⁴ s/fotón² | 558 |

---

## Problemas (p. 559)

1. ***Relation between the two-photon absorption cross section and $\chi^{(3)}$.*** Derivar una
   expresión que relacione la sección eficaz de absorción de dos fotones $\sigma^{(2)}$ con la
   susceptibilidad de tercer orden $\chi^{(3)}$. Indicar la dependencia en frecuencia de $\chi^{(3)}$.
2. ***Multiphoton absorption coefficients.*** A partir de las expresiones de las tasas de absorción de
   uno, dos y tres fotones citadas arriba, deducir expresiones para los coeficientes de absorción de
   uno, dos y tres fotones $\alpha$, $\beta$ y $\gamma$ definidos por
   $$\frac{dI}{dz}=-\alpha I-\beta I^2-\gamma I^3.$$
   Hacer estimaciones de orden de magnitud de $\beta$ y $\gamma$ para materia condensada y compararlas con
   valores medidos típicos tabulados en la literatura científica.

(2 problemas.)

---

## Referencias principales (p. 559–560)

- *Optical Damage*: Ammosov, Delone y Krainov (1986) *Sov. Phys. JETP* **64**, 1191 (ADK);
  Bloembergen (1997) *J. Nonlinear Opt. Phys. Materials* **6**, 377; Du *et al.* (1994) *APL* **64**,
  3071; Genin *et al.* (2000) *Appl. Opt.* **39**, 3654; Lowdermilk y Milam (1981) *IEEE JQE* **17**,
  1888; Stuart *et al.* (1995) *PRL* **74**, 2248; Stuart *et al.* (1996) *PRB* **53**, 1749.
- *Reviews of Optical Damage*: Bloembergen (1974) *IEEE JQE* **10**, 375; Manenkov y Prokhorov
  (1986) *Sov. Phys. Usp.* **29**, 104; Raizer (1965) *Sov. Phys. JETP* **21**, 1009; Wood (1986)
  *Laser Damage in Optical Materials*, Adam Hilger.
- *Optical Damage with Femtosecond Laser Pulses*: Davis *et al.* (1996) *Opt. Lett.* **21**, 1729;
  Glezer *et al.* (1996) *Opt. Lett.* **21**, 2023; Pronko *et al.* (1995) *Opt. Commun.* **114**, 106.
- *Multiphoton Absorption*: Denk, Strickler y Webb (1990) *Science* **248**, 73; Drobizhev *et al.*
  (2001) *Opt. Lett.* **26**, 1081; Kaiser y Garrett (1961) *PRL* **7**, 229; Xu y Webb (1997), en
  Lakowicz (ed.), *Topics in Fluorescence Spectroscopy* vol. 5, cap. 11; Xu y Webb (1996) *JOSA B*
  **13**, 481.

---

## Relación con el curso y con el proyecto final

- **Curso:** no está en los temas 4–6 del programa, pero conecta con el tema 6 (Boyd 4.1: la parte
  imaginaria de $\chi^{(3)}$ da la absorción de dos fotones, $\beta$) y con el cálculo cuántico de $\chi^{(3)}$ del
  cap. 3. El problema 2 es justamente la definición de $\beta$ que aparece como $\alpha_2$ en 4.1.
- **Proyecto final (supercontinuo en SiN vs Si):** la absorción de dos fotones (TPA) es *el*
  factor que distingue Si de SiN en el infrarrojo cercano. En Si ($E_g\approx1.12$ eV) dos fotones a
  1550 nm (0.8 eV c/u) superan el gap → TPA fuerte ($\beta\sim0.5$–0.9 cm/GW) y absorción por portadores
  libres generados; en SiN ($E_g\sim5$ eV) la TPA es despreciable en el NIR. Las tasas $R^{(N)}\propto I^N$
  explican por qué en guías de alto confinamiento (intensidades de GW/cm²) la TPA limita el
  ensanchamiento espectral. Los umbrales de daño por avalancha (~10–40 GW/cm² para ns) y la ley
  $T_p^{1/2}$ son relevantes para elegir la potencia pico de bombeo en las simulaciones.
- La regla de oro de Fermi de §12.5 es la misma que en Saleh (cap. 14, interacción luz–átomo).
