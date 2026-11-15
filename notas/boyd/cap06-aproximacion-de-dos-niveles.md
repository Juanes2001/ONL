# Capítulo 6 — Nonlinear Optics in the Two-Level Approximation (Boyd, 3.ª ed.)

Páginas del libro 277–328 (PDF 295–346; la p. 276 del libro está en blanco y el cap. 7 empieza en la p. 329). Leído el 2026-11-14.

Fuente: R. W. Boyd, *Nonlinear Optics*, 3.ª ed., Academic Press, 2008, cap. 6. Las citas de página son páginas del libro
(sumar 18 para la página del PDF).

Convención (la del libro, SI): $\tilde E(t)=Ee^{-i\omega t}+{\rm c.c.}$, $\tilde P(t)=Pe^{-i\omega t}+{\rm c.c.}$, $P=\epsilon_0\chi E$,
$I=2n\epsilon_0c|E|^2$; nivel inferior $a$, superior $b$; $\omega_{ba}=(E_b-E_a)/\hbar$; desintonía $\Delta=\omega-\omega_{ba}$ (algunos autores usan el signo
opuesto, nota p. 294); frecuencia de Rabi $\Omega=2|\mu_{ba}||E|/\hbar$ (o compleja $2\mu_{ba}E/\hbar$); inversión $w=\rho_{bb}-\rho_{aa}$.

---

## Resumen del capítulo

Cuando la excitación es resonante, la serie de potencias $\tilde P=\epsilon_0[\chi^{(1)}\tilde E+\chi^{(2)}\tilde E^2+\chi^{(3)}\tilde E^3+\cdots]$ deja de
converger (ejemplo: absorbente saturable $\alpha=\alpha_0/(1+I/I_s)$, cuya serie solo converge para $I<I_s$), pero en compensación basta
retener los dos niveles conectados por el campo. El capítulo plantea las ecuaciones de movimiento de la matriz densidad para un
átomo de dos niveles, primero sin relajación y luego con modelos fenomenológicos de relajación (átomo cerrado con $T_1$ y $T_2$,
átomo abierto con bombeo y reservorios, y átomo con un tercer nivel trampa acoplado no radiativamente). Con la aproximación de onda
rotante obtiene la solución estacionaria exacta para un campo monocromático: una susceptibilidad total
$\chi\propto(\Delta T_2-i)/(1+\Delta^2T_2^2+\Omega^2T_1T_2)$ que muestra **saturación** y **ensanchamiento por potencia**, define el campo y la
intensidad de saturación ($E_s^0$, $I_s^0$, $I_s^\Delta$) y, al desarrollar en $|E|^2/|E_s^0|^2$, recupera $\chi^{(1)}$ y $\chi^{(3)}$ (con
$\chi^{(3)}=-\chi^{(1)}/3|E_s^\Delta|^2$: la no linealidad resonante es una saturación), con estimaciones numéricas para el sodio
($I_s^0\sim5$ mW/cm², $\chi^{(3)}\sim10^{-16}$ m²/V²). Luego reescribe la dinámica como **ecuaciones ópticas de Bloch** ($u,v,w$, con
$u^2+v^2+w^2\le1$), como un **oscilador armónico** forzado paramétricamente por la inversión (origen de la no linealidad), y resuelve el
límite de **seguimiento adiabático** (pulso corto y desintonía grande), que da $\chi^{(3)}=2N|\mu|^4/(3\epsilon_0\hbar^3\Delta^3)$ en acuerdo con el
estado estacionario. Con la ecuación de Schrödinger obtiene las **oscilaciones de Rabi** a la frecuencia generalizada
$\Omega'=(|\Omega|^2+\Delta^2)^{1/2}$, las bandas laterales $\omega\pm\Omega'$ en el dipolo, los **estados vestidos** (Autler–Townes) y su límite de
campo débil (niveles virtuales), y el amortiguamiento de las oscilaciones de Rabi con $T_1=T_2$. Finalmente trata la **mezcla de ondas
bombeo–sonda**: la inversión oscila a la frecuencia de batido $\delta$ (oscilaciones coherentes de población), las respuestas tienen
resonancias en $\delta=0,\pm\Omega'$ con anchos $\Gamma_0$ y $\Gamma_\pm$, se definen $\chi^{(1)}_{\rm eff}$ y $\chi^{(3)}_{\rm eff}$ dependientes de la intensidad
del bombeo, ecuaciones de amplitudes acopladas para la mezcla de cuatro ondas hacia adelante, y el espectro de absorción de la sonda
con sus tres rasgos (resonancia de tres fotones con ganancia, resonancia de Rayleigh y resonancia Stark ac), con la conexión a luz
lenta y rápida.

---

## Secciones

### 6.1 Introducción (p. 277–278)

Los capítulos anteriores relacionan la respuesta del material con el campo mediante series de potencias,
$$\tilde P(t)=\epsilon_0\chi^{(1)}\tilde E(t)+\epsilon_0\chi^{(2)}\tilde E(t)^2+\epsilon_0\chi^{(3)}\tilde E(t)^3+\cdots \qquad (6.1.1),\ \text{p. 277}$$
pero hay situaciones en que la serie **no converge**. Ejemplo: el absorbente saturable, con $I=2n\epsilon_0c|E|^2$,
$$\alpha=\frac{\alpha_0}{1+I/I_s}\qquad(6.1.2),\ \text{p. 277}$$
($\alpha_0$ = coeficiente de absorción a campo débil, $I_s$ = intensidad de saturación). Su desarrollo
$$\alpha=\alpha_0\left[1-(I/I_s)+(I/I_s)^2-(I/I_s)^3+\cdots\right]\qquad(6.1.3),\ \text{p. 277}$$
converge solo para $I<I_s$. Es sobre todo bajo **excitación resonante** cuando falla la teoría de perturbaciones;
pero entonces basta con los dos niveles conectados resonantemente por el campo, lo que compensa la complejidad del
tratamiento no perturbativo (no hay que sumar sobre todos los estados como en las expresiones de $\chi^{(3)}$ del cap. 3).
El capítulo trata un haz monocromático de frecuencia $\omega$ sobre un conjunto de átomos de dos niveles (extensión del
cap. 4, que usaba $\chi^{(3)}(\omega=\omega+\omega-\omega)$); las dos últimas secciones generalizan a mezcla de cuatro ondas
no degenerada. Procesos descritos: saturación, ensanchamiento por potencia, oscilaciones de Rabi, corrimientos Stark
ópticos. Tratamientos paralelos: Allen y Eberly (1975), Cohen-Tannoudji *et al.* (1989), Sargent (1978), Boyd y Sargent (1988) (p. 278).

### 6.2 Ecuaciones de movimiento de la matriz densidad para un átomo de dos niveles (p. 278–285)

Primero sin amortiguamiento (no hay forma *única* de incluirlo; esto es punto de partida). Nivel inferior $a$,
superior $b$ (Fig. 6.2.1, p. 279: excitación casi resonante de un átomo de dos niveles, flecha $\omega$ de $a$ hacia
una línea punteada cerca de $b$).
$$\hat H=\hat H_0+\hat V(t)\qquad(6.2.1),\ \text{p. 278}$$
$$E_a=\hbar\omega_a,\quad E_b=\hbar\omega_b\qquad(6.2.2);\qquad H_{0,nm}=E_n\delta_{nm}\qquad(6.2.3),\ \text{p. 279}$$
Aproximación dipolar eléctrica:
$$\hat V(t)=-\hat\mu\tilde E(t)\qquad(6.2.4)$$
Estados de paridad definida $\Rightarrow\mu_{aa}=\mu_{bb}=0$:
$$V_{aa}=V_{bb}=0\qquad(6.2.5);\qquad V_{ba}=V_{ab}^*=-\mu_{ba}\tilde E(t)\qquad(6.2.6),\ \text{p. 279}$$
$$\hat\rho=\begin{bmatrix}\rho_{aa}&\rho_{ab}\\ \rho_{ba}&\rho_{bb}\end{bmatrix}\qquad(6.2.7),\ \text{p. 279}$$
con $\rho_{ba}=\rho_{ab}^*$. Evolución (ec. (3.3.21)):
$$\dot\rho_{nm}=\frac{-i}{\hbar}[\hat H,\hat\rho]_{nm}=\frac{-i}{\hbar}\sum_\nu(H_{n\nu}\rho_{\nu m}-\rho_{n\nu}H_{\nu m})\qquad(6.2.8),\ \text{p. 280}$$
$$\dot\rho_{nm}=-i\omega_{nm}\rho_{nm}-\frac{i}{\hbar}\sum_\nu(V_{n\nu}\rho_{\nu m}-\rho_{n\nu}V_{\nu m}),\qquad \omega_{nm}=(E_n-E_m)/\hbar\qquad(6.2.9)$$
Para dos niveles:
$$\dot\rho_{ba}=-i\omega_{ba}\rho_{ba}+\frac{i}{\hbar}V_{ba}(\rho_{bb}-\rho_{aa})\qquad(6.2.10a)$$
$$\dot\rho_{bb}=\frac{i}{\hbar}(V_{ba}\rho_{ab}-\rho_{ba}V_{ab})\qquad(6.2.10b)$$
$$\dot\rho_{aa}=\frac{i}{\hbar}(V_{ab}\rho_{ba}-\rho_{ab}V_{ba})\qquad(6.2.10c),\ \text{p. 280}$$
Por inspección $\dot\rho_{bb}+\dot\rho_{aa}=0$ (6.2.11): población total conservada, $\rho_{aa}+\rho_{bb}=1$ (6.2.12). No hace
falta ecuación para $\rho_{ab}=\rho_{ba}^*$. Las (6.2.10) bastan cuando la relajación es despreciable, p. ej. pulsos mucho
más cortos que los tiempos de relajación del material.

#### 6.2.1 Átomo de dos niveles cerrado (p. 281–283)

Fig. 6.2.2 (p. 281): $b$ decae a $a$ con tasa $\Gamma_{ba}=1/T_1$ (tiempo de vida $T_1$, típicamente emisión espontánea);
el dipolo se desfasa en $T_2$, ancho de línea (campo débil) $\gamma_{ba}=1/T_2$ (en la figura, $2\gamma_{ba}=2/T_2$).
"Cerrado": toda la población que sale de $b$ entra a $a$. Nota al pie: por (6.3.25) el FWHM (en frecuencia angular) de la
línea de absorción a campo débil es $2\gamma_{ba}$. Términos de decaimiento fenomenológicos:
$$\dot\rho_{ba}=-\left(i\omega_{ba}+\frac1{T_2}\right)\rho_{ba}+\frac{i}{\hbar}V_{ba}(\rho_{bb}-\rho_{aa})\qquad(6.2.13a)$$
$$\dot\rho_{bb}=-\frac{\rho_{bb}}{T_1}-\frac{i}{\hbar}(V_{ba}\rho_{ab}-\rho_{ba}V_{ab})\qquad(6.2.13b)$$
$$\dot\rho_{aa}=\frac{\rho_{bb}}{T_1}+\frac{i}{\hbar}(V_{ba}\rho_{ab}-\rho_{ba}V_{ab})\qquad(6.2.13c),\ \text{p. 281}$$
Sigue cumpliéndose $\dot\rho_{bb}+\dot\rho_{aa}=0$ (6.2.14).

> **Errata (p. 280 vs. p. 281):** (6.2.10b) y (6.2.13b) traen el término de interacción con signos opuestos. Aplicando
> (6.2.9) con $n=m=b$ (solo contribuye $\nu=a$, porque $V_{bb}=0$) resulta
> $\dot\rho_{bb}=-\frac{i}{\hbar}(V_{ba}\rho_{ab}-\rho_{ba}V_{ab})$, que es el signo de (6.2.13b). Por tanto la errata está
> en (6.2.10b) (se lee $+\frac{i}{\hbar}$; debería ser $-\frac{i}{\hbar}$) y en (6.2.10c) (se lee
> $+\frac{i}{\hbar}(V_{ab}\rho_{ba}-\rho_{ab}V_{ba})$; debería ser $-\frac{i}{\hbar}(V_{ab}\rho_{ba}-\rho_{ab}V_{ba})=+\frac{i}{\hbar}(V_{ba}\rho_{ab}-\rho_{ba}V_{ab})$,
> como en (6.2.13c)). (6.2.10a) sí es correcta. (6.2.13)–(6.2.17) son consistentes con el cálculo directo.

Restando (6.2.13c) de (6.2.13b):
$$\frac{d}{dt}(\rho_{bb}-\rho_{aa})=\frac{-2\rho_{bb}}{T_1}-\frac{2i}{\hbar}(V_{ba}\rho_{ab}-\rho_{ba}V_{ab})\qquad(6.2.15),\ \text{p. 282}$$
Con $2\rho_{bb}=(\rho_{bb}-\rho_{aa})+1$:
$$\frac{d}{dt}(\rho_{bb}-\rho_{aa})=-\frac{(\rho_{bb}-\rho_{aa})+1}{T_1}-\frac{2i}{\hbar}(V_{ba}\rho_{ab}-\rho_{ba}V_{ab})\qquad(6.2.16)$$
Generalización a una diferencia de equilibrio térmico $(\rho_{bb}-\rho_{aa})^{(\rm eq)}\neq-1$:
$$\frac{d}{dt}(\rho_{bb}-\rho_{aa})=-\frac{(\rho_{bb}-\rho_{aa})-(\rho_{bb}-\rho_{aa})^{(\rm eq)}}{T_1}-\frac{2i}{\hbar}(V_{ba}\rho_{ab}-\rho_{ba}V_{ab})\qquad(6.2.17),\ \text{p. 282}$$
El sistema cerrado se reduce a dos ecuaciones acopladas, (6.2.13a) y (6.2.17). Justificación de los términos: sin campo,
$$\rho_{bb}(t)-\rho_{aa}(t)=(\rho_{bb}-\rho_{aa})^{(\rm eq)}+\{[\rho_{bb}(0)-\rho_{aa}(0)]-(\rho_{bb}-\rho_{aa})^{(\rm eq)}\}e^{-t/T_1}\qquad(6.2.18)$$
($T_1$ = tiempo de relajación de población) y
$$\rho_{ba}(t)=\rho_{ba}(0)e^{-(i\omega_{ba}+1/T_2)t}\qquad(6.2.19),\ \text{p. 282}$$
$$\langle\tilde\mu(t)\rangle=\mu_{ab}\rho_{ba}(t)+\mu_{ba}\rho_{ab}(t)=[\mu_{ab}\rho_{ba}(0)e^{-i\omega_{ba}t}+{\rm c.c.}]e^{-t/T_2}\qquad(6.2.20),\ \text{p. 283}$$
El dipolo oscila a $\omega_{ba}$ y decae en $T_2$ (tiempo de desfase dipolar). Relación con la tasa de desfase colisional $\gamma_c$ (cf. (3.3.25)):
$$\frac1{T_2}=\frac1{2T_1}+\gamma_c\qquad(6.2.21a);\qquad \gamma_c=C_sN+C_fN_f\qquad(6.2.21b),\ \text{p. 283}$$
$N$: densidad de átomos resonantes a $\omega_{ba}$; $N_f$: átomos "extranjeros"; $C_s$, $C_f$: coeficientes de autoensanchamiento
y de ensanchamiento por gas extranjero. **Ejemplo numérico** (línea de resonancia 3s→3p del sodio): $T_1=16$ ns,
$C_s=1.50\times10^{-7}$ cm³/s; con argón como gas extranjero $C_f=2.53\times10^{-9}$ cm³/s. Tablas: Miles y Harris (1973).

#### 6.2.2 Átomo de dos niveles abierto (p. 283–284)

Fig. 6.2.3 (p. 284): los niveles $a$ y $b$ intercambian población con niveles reservorio (subniveles magnéticos o
hiperfinos), con tasas $\Gamma_a$, $\Gamma_b$, y se bombean a tasas $\lambda_a$, $\lambda_b$ (modelo típico de teoría del láser).
La población que sale de $b$ no necesariamente llega a $a$.
$$\dot\rho_{ba}=-\left(i\omega_{ba}+\frac1{T_2}\right)\rho_{ba}+\frac{i}{\hbar}V_{ba}(\rho_{bb}-\rho_{aa})\qquad(6.2.22a)$$
$$\dot\rho_{bb}=\lambda_b-\Gamma_b(\rho_{bb}-\rho_{bb}^{(\rm eq)})-\frac{i}{\hbar}(V_{ba}\rho_{ab}-\rho_{ba}V_{ab})\qquad(6.2.22b)$$
$$\dot\rho_{aa}=\lambda_a-\Gamma_a(\rho_{aa}-\rho_{aa}^{(\rm eq)})+\frac{i}{\hbar}(V_{ba}\rho_{ab}-\rho_{ba}V_{ab})\qquad(6.2.22c),\ \text{p. 284}$$
La población total en $a$ y $b$ no se conserva: hay que usar las tres ecuaciones.
$$\frac1{T_2}=\tfrac12(\Gamma_b+\Gamma_a)+\gamma_c\qquad(6.2.23),\ \text{p. 284}$$

#### 6.2.3 Átomo de dos niveles con un tercer nivel acoplado no radiativamente (p. 284–285)

Modelo usual de absorbente saturable (Fig. 6.3.1, p. 285): $b$ decae a $a$ con $\Gamma_{ba}$ y a un nivel trampa $c$ con
$\Gamma_{bc}$; $c$ vuelve a $a$ con $\Gamma_{ca}$; el dipolo $a$–$b$ se amortigua a tasa $\gamma_{ba}$.
$$\dot\rho_{ba}=-(i\omega_{ba}+\gamma_{ba})\rho_{ba}+\frac{i}{\hbar}V_{ba}(\rho_{bb}-\rho_{aa})\qquad(6.2.24a)$$
$$\dot\rho_{bb}=-(\Gamma_{ba}+\Gamma_{bc})\rho_{bb}-\frac{i}{\hbar}(V_{ba}\rho_{ab}-\rho_{ba}V_{ab})\qquad(6.2.24b)$$
$$\dot\rho_{cc}=\Gamma_{bc}\rho_{bb}-\Gamma_{ca}\rho_{cc}\qquad(6.2.24c)$$
$$\dot\rho_{aa}=\Gamma_{ba}\rho_{bb}+\Gamma_{ca}\rho_{cc}+\frac{i}{\hbar}(V_{ba}\rho_{ab}-\rho_{ba}V_{ab})\qquad(6.2.24d),\ \text{p. 285}$$
Se conserva la población de los tres niveles: $\dot\rho_{aa}+\dot\rho_{bb}+\dot\rho_{cc}=0$ (sin número, p. 285).

### 6.3 Respuesta estacionaria de un átomo de dos niveles a un campo monocromático (p. 285–293)

Se trata el átomo cerrado (resultados cualitativamente similares para los otros modelos; Problema 1). Ecuaciones:
$$\frac{d}{dt}\rho_{ba}=-\left(i\omega_{ba}+\frac1{T_2}\right)\rho_{ba}+\frac{i}{\hbar}V_{ba}(\rho_{bb}-\rho_{aa})\qquad(6.3.1)$$
$$\frac{d}{dt}(\rho_{bb}-\rho_{aa})=-\frac{(\rho_{bb}-\rho_{aa})-(\rho_{bb}-\rho_{aa})^{(\rm eq)}}{T_1}-\frac{2i}{\hbar}(V_{ba}\rho_{ab}-\rho_{ba}V_{ab})\qquad(6.3.2),\ \text{p. 285}$$
Interacción con onda monocromática:
$$\hat V=-\hat\mu\tilde E(t)=-\hat\mu(Ee^{-i\omega t}+E^*e^{i\omega t})\qquad(6.3.3);\qquad V_{ba}=-\mu_{ba}(Ee^{-i\omega t}+E^*e^{i\omega t})\qquad(6.3.4),\ \text{p. 286}$$
No se resuelven exactamente. **Aproximación de onda rotante (RWA):** como sin campo $\rho_{ba}\propto e^{-i\omega_{ba}t}$, para
$\omega\approx\omega_{ba}$ la parte $e^{-i\omega t}$ de $V_{ba}$ es un forzamiento mucho más eficaz que la parte $e^{i\omega t}$; se toma
$$V_{ba}=-\mu_{ba}Ee^{-i\omega t}\qquad(6.3.5),\ \text{p. 286}$$
$$\frac{d}{dt}\rho_{ba}=-\left(i\omega_{ba}+\frac1{T_2}\right)\rho_{ba}-\frac{i}{\hbar}\mu_{ba}Ee^{-i\omega t}(\rho_{bb}-\rho_{aa})\qquad(6.3.6)$$
$$\frac{d}{dt}(\rho_{bb}-\rho_{aa})=-\frac{(\rho_{bb}-\rho_{aa})-(\rho_{bb}-\rho_{aa})^{(\rm eq)}}{T_1}+\frac{2i}{\hbar}\left(\mu_{ba}Ee^{-i\omega t}\rho_{ab}-\mu_{ab}E^*e^{i\omega t}\rho_{ba}\right)\qquad(6.3.7),\ \text{p. 286}$$
En RWA $\rho_{ba}$ se excita solo cerca de su frecuencia natural $\omega_{ba}$, y $\rho_{bb}-\rho_{aa}$ solo cerca de frecuencia cero.
Variable lentamente variable:
$$\rho_{ba}(t)=\sigma_{ba}(t)e^{-i\omega t}\qquad(6.3.8),\ \text{p. 286}$$
$$\frac{d}{dt}\sigma_{ba}=\left[i(\omega-\omega_{ba})-\frac1{T_2}\right]\sigma_{ba}-\frac{i}{\hbar}\mu_{ba}E(\rho_{bb}-\rho_{aa})\qquad(6.3.9)$$
$$\frac{d}{dt}(\rho_{bb}-\rho_{aa})=-\frac{(\rho_{bb}-\rho_{aa})-(\rho_{bb}-\rho_{aa})^{(\rm eq)}}{T_1}+\frac{2i}{\hbar}(\mu_{ba}E\sigma_{ab}-\mu_{ab}E^*\sigma_{ba})\qquad(6.3.10),\ \text{p. 287}$$
Estado estacionario (derivadas = 0), resolviendo el sistema algebraico:
$$\rho_{bb}-\rho_{aa}=\frac{(\rho_{bb}-\rho_{aa})^{(\rm eq)}[1+(\omega-\omega_{ba})^2T_2^2]}{1+(\omega-\omega_{ba})^2T_2^2+(4/\hbar^2)|\mu_{ba}|^2|E|^2T_1T_2}\qquad(6.3.11)$$
$$\rho_{ba}=\sigma_{ba}e^{-i\omega t}=\frac{\mu_{ba}Ee^{-i\omega t}(\rho_{bb}-\rho_{aa})}{\hbar(\omega-\omega_{ba}+i/T_2)}\qquad(6.3.12),\ \text{p. 287}$$
Polarización ($N$ = densidad de átomos):
$$\tilde P(t)=N\langle\tilde\mu\rangle=N\,{\rm Tr}(\hat\rho\hat\mu)=N(\mu_{ab}\rho_{ba}+\mu_{ba}\rho_{ab})\qquad(6.3.13)$$
$$\tilde P(t)=Pe^{-i\omega t}+{\rm c.c.}\qquad(6.3.14);\qquad P=\epsilon_0\chi E\qquad(6.3.15),\ \text{p. 287}$$
$$\chi=\frac{N|\mu_{ba}|^2(\rho_{bb}-\rho_{aa})}{\epsilon_0\hbar(\omega-\omega_{ba}+i/T_2)}\qquad(6.3.16)$$
Sustituyendo (6.3.11) y racionalizando:
$$\chi=\frac{N(\rho_{bb}-\rho_{aa})^{(\rm eq)}|\mu_{ba}|^2(\omega-\omega_{ba}-i/T_2)T_2^2/\epsilon_0\hbar}{1+(\omega-\omega_{ba})^2T_2^2+(4/\hbar^2)|\mu_{ba}|^2|E|^2T_1T_2}\qquad(6.3.17),\ \text{p. 287}$$

Esta $\chi$ es la susceptibilidad **total** (lineal + no lineal) (p. 288). Notación:
$$\Omega=2|\mu_{ba}||E|/\hbar\quad\text{(frecuencia de Rabi en resonancia)}\qquad(6.3.18);\qquad \Delta=\omega-\omega_{ba}\quad\text{(desintonía)}\qquad(6.3.19),\ \text{p. 288}$$
$$\chi=\left[N(\rho_{bb}-\rho_{aa})^{(\rm eq)}|\mu_{ba}|^2\frac{T_2}{\epsilon_0\hbar}\right]\frac{\Delta T_2-i}{1+\Delta^2T_2^2+\Omega^2T_1T_2}\qquad(6.3.20),\ \text{p. 288}$$
Coeficiente de absorción:
$$\alpha=\frac{2\omega}{c}{\rm Im}\,n=\frac{2\omega}{c}{\rm Im}[(1+\chi)^{1/2}]\qquad(6.3.21a);\qquad \alpha=\frac{\omega}{c}{\rm Im}\,\chi\quad(|\chi|\ll1)\qquad(6.3.21b)$$
Para una onda débil (despreciando $\Omega^2T_1T_2$):
$$\alpha_0(\Delta)=\frac{\alpha_0(0)}{1+\Delta^2T_2^2}\qquad(6.3.22a);\qquad \alpha_0(0)=-\frac{\omega_{ba}}{c}\left[N(\rho_{bb}-\rho_{aa})^{(\rm eq)}|\mu_{ba}|^2\frac{T_2}{\epsilon_0\hbar}\right]\qquad(6.3.22b)$$
(coeficiente de absorción no saturado en el centro de línea; positivo porque $(\rho_{bb}-\rho_{aa})^{(\rm eq)}<0$).
$$\chi=-\frac{\alpha_0(0)}{\omega_{ba}/c}\,\frac{\Delta T_2-i}{1+\Delta^2T_2^2+\Omega^2T_1T_2}\qquad(6.3.23),\ \text{p. 288}$$
Partes real e imaginaria, $\chi=\chi'+i\chi''$:
$$\chi'=-\frac{\alpha_0(0)}{\omega_{ba}/c}\frac{1}{\sqrt{1+\Omega^2T_1T_2}}\frac{\Delta T_2/\sqrt{1+\Omega^2T_1T_2}}{1+\Delta^2T_2^2/(1+\Omega^2T_1T_2)}\qquad(6.3.24a)$$
$$\chi''=\frac{\alpha_0(0)}{\omega_{ba}/c}\left(\frac{1}{1+\Omega^2T_1T_2}\right)\frac{1}{1+\Delta^2T_2^2/(1+\Omega^2T_1T_2)}\qquad(6.3.24b),\ \text{p. 289}$$
Aun con campo intenso, $\chi'$ tiene forma dispersiva y $\chi''$ lorentziana, pero ensanchadas por $(1+\Omega^2T_1T_2)^{1/2}$:
$$\Delta\omega_{\rm FWHM}=\frac{2}{T_2}(1+\Omega^2T_1T_2)^{1/2}\qquad(6.3.25),\ \text{p. 289}$$
→ **ensanchamiento por potencia**. El valor en el centro de línea de $\chi''$ (y de $\alpha$) disminuye → **saturación**.

> **Errata (p. 289):** el texto dice que el valor de $\chi''$ en el centro de línea disminuye "por el factor $(1+\Omega^2T_1T_2)^{1/2}$".
> Según (6.3.24b) con $\Delta=0$, $\chi''\propto 1/(1+\Omega^2T_1T_2)$: el factor de reducción es $(1+\Omega^2T_1T_2)$, sin raíz
> (consistente con que $\alpha$ cae a la mitad cuando $|E|=|E_s^0|$, p. 289–290). El factor $(1+\Omega^2T_1T_2)^{1/2}$ es el del ancho.

Fig. 6.3.2 (p. 290): Re $\chi$ y Im $\chi$ (en unidades de $\alpha_0c/\omega_{ba}$) frente a $\Delta T_2=(\omega-\omega_{ba})T_2\in[-10,10]$ para
$\Omega^2T_1T_2\ll1$, $=2$ y $=4$: Im $\chi$ pico 1.0 → ≈0.33 → 0.2 y más ancho; Re $\chi$ dispersiva con extremos ±0.5 que se aplanan.

Campo de saturación en el centro de línea $E_s^0$:
$$\Omega^2T_1T_2=\frac{|E|^2}{|E_s^0|^2}\qquad(6.3.26);\qquad |E_s^0|^2=\frac{\hbar^2}{4|\mu_{ba}|^2T_1T_2}\qquad(6.3.27),\ \text{p. 289}$$
$$\chi=\frac{-\alpha_0(0)}{\omega_{ba}/c}\frac{\Delta T_2-i}{1+\Delta^2T_2^2+|E|^2/|E_s^0|^2}\qquad(6.3.28),\ \text{p. 289}$$
La absorción en el centro de línea cae a la mitad cuando $|E|=|E_s^0|$. Para desintonía arbitraria:
$$|E_s^\Delta|^2=|E_s^0|^2(1+\Delta^2T_2^2)\qquad(6.3.29),\ \text{p. 290}$$
Intensidades de saturación (con $|n-1|\ll1$):
$$I_s^0=2\epsilon_0c|E_s^0|^2\qquad(6.3.30);\qquad I_s^\Delta=2\epsilon_0c|E_s^\Delta|^2=I_s^0(1+\Delta^2T_2^2)\qquad(6.3.31),\ \text{p. 290}$$
**Conexión con la teoría perturbativa** (p. 290–291): desarrollando (6.3.28) en $|E|^2/|E_s^0|^2$ a primer orden,
$$\chi\simeq\frac{-\alpha_0(0)}{\omega_{ba}/c}\left(\frac{\Delta T_2-i}{1+\Delta^2T_2^2}\right)\left(1-\frac{1}{1+\Delta^2T_2^2}\frac{|E|^2}{|E_s^0|^2}\right)\qquad(6.3.32),\ \text{p. 291}$$
e igualando con $\chi=\chi^{(1)}+3\chi^{(3)}|E|^2$, con $\chi^{(3)}\equiv\chi^{(3)}(\omega=\omega+\omega-\omega)$ (el libro escribe "$|E^2|$"):
$$\chi^{(1)}=\frac{-\alpha_0(0)}{\omega_{ba}/c}\frac{\Delta T_2-i}{1+\Delta^2T_2^2}\qquad(6.3.33a)$$
$$\chi^{(3)}=\frac{\alpha_0(0)}{3\omega_{ba}/c}\left[\frac{\Delta T_2-i}{(1+\Delta^2T_2^2)^2}\right]\frac{1}{|E_s^0|^2}\qquad(6.3.33b),\ \text{p. 291}$$
El signo de $\chi^{(3)}$ es opuesto al de $\chi^{(1)}$: $\chi^{(3)}$ representa la **saturación** de la respuesta (Fig. 6.3.3).
En términos de intensidad de saturación:
$$\chi^{(3)}=\frac{\alpha_0(0)}{3\omega_{ba}/c}\left[\frac{\Delta T_2-i}{(1+\Delta^2T_2^2)^2}\right]\frac{2\epsilon_0c}{I_s^0}\qquad(6.3.34a);\qquad \chi^{(3)}=\frac{\alpha_0(\Delta)(\Delta T_2-i)}{3\omega_{ba}/c}\frac{2\epsilon_0c}{I_s^\Delta}\qquad(6.3.34b)$$
$$\chi^{(3)}=\frac{-\chi^{(1)}}{3(1+\Delta^2T_2^2)|E_s^0|^2}=\frac{-\chi^{(1)}}{3|E_s^\Delta|^2}\qquad(6.3.35),\ \text{p. 291}$$

Fig. 6.3.3 (p. 292): (a) Re $\chi^{(3)}$ y (b) Im $\chi^{(3)}$ frente a $\Delta T_2\in[-5,5]$ (para medio absorbente): Re $\chi^{(3)}$ es
negativa para $\Delta<0$ y positiva para $\Delta>0$ (forma dispersiva con signo opuesto a Re $\chi^{(1)}$); Im $\chi^{(3)}$ es un
pozo negativo centrado en $\Delta=0$, más estrecho que la lorentziana lineal (cuadrado de lorentziana).

En términos microscópicos (con (6.3.22b) y (6.3.27)):
$$\chi^{(1)}=\left[N(\rho_{bb}-\rho_{aa})^{(\rm eq)}|\mu_{ba}|^2\frac{T_2}{\epsilon_0\hbar}\right]\frac{\Delta T_2-i}{1+\Delta^2T_2^2}\qquad(6.3.36a)$$
$$\chi^{(3)}=-\tfrac43N(\rho_{bb}-\rho_{aa})^{(\rm eq)}|\mu_{ba}|^4\frac{T_1T_2^2}{\epsilon_0\hbar^3}\frac{\Delta T_2-i}{(1+\Delta^2T_2^2)^2}\qquad(6.3.36b),\ \text{p. 292}$$
Límite $\Delta T_2\gg1$:
$$\chi^{(3)}=-\tfrac43N(\rho_{bb}-\rho_{aa})^{(\rm eq)}|\mu_{ba}|^4\frac{1}{\hbar^3\Delta^3}\frac{T_1}{T_2}\qquad(6.3.37),\ \text{p. 292}$$

> **Errata (p. 292):** a (6.3.37) le falta el factor $1/\epsilon_0$ que sí aparece en (6.3.36b); el límite correcto es
> $\chi^{(3)}=-\frac43N(\rho_{bb}-\rho_{aa})^{(\rm eq)}|\mu_{ba}|^4T_1/(\epsilon_0\hbar^3\Delta^3T_2)$ (necesario para obtener m²/V² y el valor numérico del texto).

**Órdenes de magnitud** (p. 292–293). Con $n=1$, $I=2\epsilon_0c|E|^2$:
$$\Omega=\frac{2|\mu_{ba}|}{\hbar}\left(\frac{I}{2\epsilon_0c}\right)^{1/2}\qquad(6.3.38),\ \text{p. 293}$$
Con $|\mu_{ba}|=2.5ea_0=2.0\times10^{-29}$ C·m (transición 3s→3p del sodio) e $I$ en W/cm²:
$$\Omega\,[\mathrm{rad/s}]=2\pi(1\times10^9)\left(\frac{I\,[\mathrm{W/cm^2}]}{127}\right)^{1/2}\qquad(6.3.39),\ \text{p. 293}$$
Para $I>127$ W/cm², $\Omega/2\pi>1$ GHz (ancho Doppler típico); alcanzable con láseres cw de baja potencia enfocados.
Intensidad de saturación con $T_1=16$ ns y $T_2/T_1=2$ (transición ensanchada radiativamente, (6.2.21a)):
$$I_s^0=5.27\ \mathrm{mW/cm^2}=52.7\ \mathrm{W/m^2}\qquad(6.3.40),\ \text{p. 293}$$
$\chi^{(3)}$ casi resonante con $N=10^{14}$ cm⁻³, $(\rho_{bb}-\rho_{aa})^{(\rm eq)}=-1$, $\mu_{ba}=2.0\times10^{-29}$ C·m,
$\Delta=2\pi c\,(1\ \mathrm{cm^{-1}})=6\pi\times10^{10}$ rad/s, $T_2/T_1=2$: de (6.3.37) $\chi^{(3)}=2.1\times10^{-16}$ m²/V², mucho mayor que
los valores no resonantes del cap. 4.

> **Duda numérica (p. 293):** recalculando con las constantes CODATA, $|\mu_{ba}|=2.5ea_0=2.12\times10^{-29}$ C·m da
> $\Omega/2\pi\approx0.99$ GHz a 127 W/cm² y $\chi^{(3)}\approx1.9\times10^{-16}$ m²/V² (con $2.0\times10^{-29}$: $0.93$ GHz y
> $1.5\times10^{-16}$ m²/V²), compatibles con el texto; pero $I_s^0=2\epsilon_0c\hbar^2/(4|\mu_{ba}|^2T_1T_2)$ da ≈64 W/m² (con
> $2.12\times10^{-29}$) o ≈72 W/m² (con $2.0\times10^{-29}$), no 52.7 W/m². No se identificó el origen de la diferencia (¿otro valor de
> $\mu_{ba}$ o de $T_2$?); usar (6.3.40) con cautela.

### 6.4 Ecuaciones ópticas de Bloch (p. 293–301)

Los formalismos (matriz densidad, ecuaciones de Bloch, etc.) son equivalentes en sus predicciones pero dan intuiciones
distintas. Campo
$$\tilde E(t)=E(t)e^{-i\omega t}+{\rm c.c.}\qquad(6.4.1),\ \text{p. 294}$$
Ecuaciones en RWA (iguales a (6.3.9)–(6.3.10)), (6.4.2a,b), con $\rho_{ba}(t)=\sigma_{ba}(t)e^{-i\omega t}$ (6.4.3), p. 294. Definiciones:
$$w=\rho_{bb}-\rho_{aa},\quad w^{(\rm eq)}=(\rho_{bb}-\rho_{aa})^{(\rm eq)}\qquad(6.4.4a);\qquad \Delta=\omega-\omega_{ba}\qquad(6.4.4b);\qquad \kappa=2\mu_{ba}/\hbar\qquad(6.4.4c),\ \text{p. 294}$$
(nota al pie: algunos autores usan el signo opuesto para $\Delta$). Quitando subíndices de $\sigma_{ba}$:
$$\frac{d\sigma}{dt}=\left(i\Delta-\frac1{T_2}\right)\sigma-\tfrac12i\kappa Ew\qquad(6.4.5a)$$
$$\frac{dw}{dt}=-\frac{w-w^{(\rm eq)}}{T_1}+i(\kappa E\sigma^*-\kappa^*E^*\sigma)\qquad(6.4.5b),\ \text{p. 295}$$
Amplitud compleja del dipolo:
$$\langle\hat\mu\rangle=\rho_{ba}\mu_{ab}+\rho_{ab}\mu_{ba}=\sigma_{ba}\mu_{ab}e^{-i\omega t}+\sigma_{ab}\mu_{ba}e^{i\omega t}\qquad(6.4.6);\qquad \langle\hat\mu\rangle=pe^{-i\omega t}+{\rm c.c.}\qquad(6.4.7);\qquad p=\sigma_{ba}\mu_{ab}\qquad(6.4.8)$$
$$\frac{dp}{dt}=\left(i\Delta-\frac1{T_2}\right)p-\frac{\hbar}{4}i|\kappa|^2Ew\qquad(6.4.9a);\qquad \frac{dw}{dt}=-\frac{w-w^{(\rm eq)}}{T_1}-\frac4\hbar{\rm Im}(Ep^*)\qquad(6.4.9b),\ \text{p. 295}$$
Son lineales en $p$, $w$ y en $E$, pero el acoplamiento es **paramétrico**: $p$ es forzado por $E\cdot w$ y $w$ por $E\cdot p$.

**Variables de Bloch.** Si $E$ es real y la fase de los estados se elige con $\mu_{ba}$ (y $\kappa$) reales:
$$\sigma=\tfrac12(u-iv)\qquad(6.4.10),\ \text{p. 295}$$
(el ½ y el signo menos siguen a Allen y Eberly, 1975). Sustituyendo en (6.4.5a) [el texto dice "(6.4.5b)", ver errata]:
$\frac{d}{dt}(u-iv)=(i\Delta-1/T_2)(u-iv)-i\kappa Ew$; separando partes real e imaginaria:
$$\frac{du}{dt}=\Delta v-\frac{u}{T_2}\qquad(6.4.11a);\qquad \frac{dv}{dt}=-\Delta u-\frac{v}{T_2}+\kappa Ew\qquad(6.4.11b);\qquad \frac{dw}{dt}=-\frac{w-w^{(\rm eq)}}{T_1}-\kappa Ev\qquad(6.4.11c),\ \text{p. 296}$$
= **ecuaciones ópticas de Bloch**. Sin relajación ($T_1,T_2\to\infty$) se conserva
$$u^2+v^2+w^2=1\qquad(6.4.12)$$
pues $\frac{d}{dt}(u^2+v^2+w^2)=2u\Delta v-2v\Delta u+2v\kappa Ew-2w\kappa Ev=0$ (6.4.13), y antes de aplicar el campo el átomo está
en el fundamental ($w=-1$, $u=v=0$). Como todos los amortiguamientos tienen signo negativo, en general
$$u^2+v^2+w^2\le1\qquad(6.4.14),\ \text{p. 296}$$

> **Errata menor (p. 296):** "This definition is introduced into Eq. (6.4.5b)" debería decir (6.4.5a) (la ecuación que resulta es la de $\sigma$);
> la siguiente mención "Similarly, Eq. (6.4.5b) becomes" sí es correcta.

#### 6.4.1 Forma de oscilador armónico de las ecuaciones de la matriz densidad (p. 297–299)

Se trabaja con el valor esperado real del dipolo (oscila a frecuencia óptica):
$$\tilde M\equiv\langle\hat\mu\rangle=\rho_{ba}\mu_{ab}+{\rm c.c.}\qquad(6.4.15),\ \text{p. 297}$$
Ecuaciones **sin RWA** ($\tilde E$ real y dependiente del tiempo), de (6.2.6), (6.2.13a), (6.2.17):
$$\dot\rho_{ba}=-\left(i\omega_{ba}+\frac1{T_2}\right)\rho_{ba}-\frac{i}{\hbar}\mu_{ba}\tilde Ew\qquad(6.4.16a);\qquad \dot w=-\frac{w-w^{(\rm eq)}}{T_1}+\frac{4\tilde E}{\hbar}{\rm Im}(\mu_{ab}\rho_{ba})\qquad(6.4.16b)$$
Derivando:
$$\dot{\tilde M}=\dot\rho_{ba}\mu_{ab}+{\rm c.c.}=-\left(i\omega_{ba}+\frac1{T_2}\right)\rho_{ba}\mu_{ab}+{\rm c.c.}\qquad(6.4.17),\ \text{p. 297}$$
(el término $-\frac{i}{\hbar}|\mu_{ba}|^2\tilde Ew$ es imaginario puro y se cancela con su c.c.). Segunda derivada:
$$\ddot{\tilde M}=\left(-\omega_{ba}^2+\frac{2i\omega_{ba}}{T_2}+\frac1{T_2^2}\right)\rho_{ba}\mu_{ab}-\frac{\omega_{ba}}{\hbar}|\mu_{ba}|^2\tilde Ew+{\rm c.c.}\qquad(6.4.18),\ \text{p. 298}$$
$$\ddot{\tilde M}+\frac2{T_2}\dot{\tilde M}+\omega_{ba}^2\tilde M=\frac{-\tilde M}{T_2^2}-\frac{2\omega_{ba}}{\hbar}|\mu_{ba}|^2\tilde Ew\qquad(6.4.19)$$
Como $\omega_{ba}^2\gg1/T_2^2$:
$$\ddot{\tilde M}+\frac2{T_2}\dot{\tilde M}+\omega_{ba}^2\tilde M=-\frac{2\omega_{ba}}{\hbar}|\mu_{ba}|^2\tilde Ew\qquad(6.4.20),\ \text{p. 298}$$
**Oscilador armónico amortiguado y forzado**, con forzamiento proporcional a $\tilde E(t)\,w$. Para la inversión:
$$\dot{\tilde M}=-i\omega_{ba}(\rho_{ba}\mu_{ab}-{\rm c.c.})-\frac1{T_2}(\rho_{ba}\mu_{ab}+{\rm c.c.})=2\omega_{ba}{\rm Im}(\rho_{ba}\mu_{ab})-\frac{\tilde M}{T_2}\qquad(6.4.21)$$
$${\rm Im}(\rho_{ba}\mu_{ab})=\frac1{2\omega_{ba}}\left(\dot{\tilde M}+\frac{\tilde M}{T_2}\right)\qquad(6.4.22);\qquad \dot w=-\frac{w-w^{(\rm eq)}}{T_1}+\frac{2\tilde E}{\hbar\omega_{ba}}\left(\dot{\tilde M}+\frac{\tilde M}{T_2}\right)\qquad(6.4.23),\ \text{p. 298}$$
Como $\dot{\tilde M}$ oscila a frecuencia óptica $\gg1/T_2$, se omite $\tilde M/T_2$:
$$\dot w=-\frac{w-w^{(\rm eq)}}{T_1}+\frac{2}{\hbar\omega_{ba}}\tilde E\dot{\tilde M}\qquad(6.4.24),\ \text{p. 299}$$
$w$ es forzada por $\tilde E$ por la parte de $\tilde M$ en cuadratura (90°) con $\tilde E$, y relaja a $w^{(\rm eq)}$ (típicamente $-1$) en ~$T_1$.
(6.4.20) y (6.4.24) son lineales en $\tilde M$ y $w$; la no linealidad viene de que el acoplamiento depende **paramétricamente**
de las variables atómicas: un oscilador lineal sería (6.4.20) con $w$ fija en $-1$.

#### 6.4.2 Límite de seguimiento adiabático (p. 299–301)

Otro límite con solución sencilla (Grischkowsky, 1970). Pulso de duración $\tau_p$ con
$$\tau_p\ll T_1,T_2\qquad(6.4.25),\ \text{p. 299}$$
(sin relajación durante el pulso) y desintonía grande:
$$|\omega-\omega_{ba}|\gg T_2^{-1},\ \tau_p^{-1},\ \mu_{ba}E/\hbar\qquad(6.4.26)$$
(desintonía mayor que el ancho de línea, ninguna componente de Fourier del pulso alcanza la resonancia y no hay
ensanchamiento por potencia hasta la resonancia) → no se excita población apreciable. Frecuencia de Rabi compleja
$$\Omega(t)=2\mu_{ba}E(t)/\hbar\qquad(6.4.27),\ \text{p. 300}$$
($E(t)$ = envolvente del pulso). Con $T_1,T_2\to\infty$, (6.4.5) da
$$\frac{d\sigma}{dt}=i\Delta\sigma-\tfrac12i\Omega w\qquad(6.4.28a);\qquad \frac{dw}{dt}=-i(\Omega^*\sigma-\Omega\sigma^*)\qquad(6.4.28b)$$
Constante de movimiento (análoga a (6.4.12)):
$$w^2(t)+4|\sigma(t)|^2=1\qquad(6.4.29),\ \text{p. 300}$$
**Aproximación adiabática:** la respuesta está casi en estado estacionario con el campo instantáneo; $d\sigma/dt=dw/dt=0$
(en realidad basta (6.4.28a)):
$$\sigma(t)=\frac{w(t)\Omega(t)}{2\Delta}\qquad(6.4.30)$$
$\sigma$ siempre en fase con $\Omega(t)$ ($w$ real). Con (6.4.29):
$$w(t)^2+\frac{w(t)^2|\Omega|^2}{\Delta^2}=1\qquad(6.4.31);\qquad w(t)=\frac{-|\Delta|}{\sqrt{\Delta^2+|\Omega(t)|^2}}\qquad(6.4.32)$$
$$\sigma(t)=-\frac{\Delta}{|\Delta|}\frac{\tfrac12\Omega(t)}{\sqrt{\Delta^2+|\Omega(t)|^2}}\qquad(6.4.33),\ \text{p. 300}$$
Polarización ($\sigma=\sigma_{ba}$):
$$P=N\mu_{ab}\sigma\qquad(6.4.34);\qquad P=-\frac{\Delta}{|\Delta|}\frac{\tfrac12N\mu_{ab}\Omega(t)}{\sqrt{\Delta^2+|\Omega(t)|^2}}\qquad(6.4.35),\ \text{p. 301}$$
Con $|\Delta|\gg|\Omega|$, desarrollando en $|\Omega|/\Delta$:
$$P=\frac{\Delta\Omega}{\Delta^2}\frac{-\tfrac12N\mu_{ab}}{(1+|\Omega|^2/\Delta^2)^{1/2}}=-\frac{\Delta\Omega}{\Delta^2}\frac12N\mu_{ab}\left(1-\frac12\frac{|\Omega|^2}{\Delta^2}+\cdots\right)\qquad(6.4.36)$$
Contribución de tercer orden (con $\Omega=2\mu_{ba}E/\hbar$):
$$\frac{|\Omega|^2\Omega\Delta N\mu_{ab}}{4\Delta^4}=\frac{2N|\mu_{ab}|^4}{\hbar^3\Delta^3}|E|^2E\qquad(6.4.37)$$
(el libro escribe "$n\mu_{ab}$" con $n$ minúscula; debe ser $N$). Por convención el coeficiente de $|E|^2E$ es $3\epsilon_0\chi^{(3)}$:
$$\chi^{(3)}=\frac{2N|\mu_{ba}|^4}{3\epsilon_0\hbar^3\Delta^3}\qquad(6.4.38),\ \text{p. 301}$$
Idéntico al resultado estacionario (6.3.37) en el límite $\Delta T_2\gg1$ para transición ensanchada radiativamente
($T_2/T_1=2$, $(\rho_{bb}-\rho_{aa})^{(\rm eq)}=-1$): $\frac43\cdot\frac12=\frac23$ (comprobación que confirma que a (6.3.37) le falta $1/\epsilon_0$).

### 6.5 Oscilaciones de Rabi y estados atómicos vestidos (p. 301–313)

Campos tan intensos que sacan una fracción importante de la población del fundamental. No solo se reduce la respuesta:
los corrimientos Stark inducidos por el láser modifican profundamente la estructura de niveles y crean **nuevas
resonancias** en la susceptibilidad. Se trabaja con la función de onda (no la matriz densidad); comentarios sobre
amortiguamiento al final.

#### 6.5.1 Solución de Rabi de la ecuación de Schrödinger (p. 302–307)

(Véase también Sargent *et al.* (1974, p. 26) y Dicke y Wittke (1960, p. 203).)
$$i\hbar\frac{\partial\psi}{\partial t}=\hat H\psi\qquad(6.5.1);\qquad \hat H=\hat H_0+\hat V(t)\qquad(6.5.2);\qquad \hat V(t)=\hat\mu\tilde E(t)\qquad(6.5.3),\ \text{p. 302}$$
con $\hat\mu=-e\hat r$ y $\tilde E(t)=Ee^{-i\omega t}+{\rm c.c.}$, $E$ constante, casi resonante con la transición $a\to b$.

> **Errata (p. 302):** (6.5.3) se lee $\hat V(t)=\hat\mu\tilde E(t)$, sin el signo menos de (6.2.4) $\hat V=-\hat\mu\tilde E$. El propio
> texto usa después $V_{ba}=-\mu_{ba}\tilde E(t)$ en (6.5.9); por consistencia debería ser $\hat V(t)=-\hat\mu\tilde E(t)$.

$$\psi(\mathbf r,t)=C_a(t)u_a(\mathbf r)e^{-i\omega_at}+C_b(t)u_b(\mathbf r)e^{-i\omega_bt}\qquad(6.5.4);\qquad \int d^3r\,u_i^*(\mathbf r)u_j(\mathbf r)=\delta_{ij}\qquad(6.5.5),\ \text{p. 302}$$
$C_a$, $C_b$: amplitudes de probabilidad. Sustituyendo en (6.5.1), multiplicando por $u_a^*$ (o $u_b^*$) e integrando:
$$\dot C_a=\frac1{i\hbar}C_bV_{ab}e^{-i\omega_{ba}t}\qquad(6.5.6);\qquad V_{ab}=V_{ba}^*=\int d^3r\,u_a^*\hat Vu_b\qquad(6.5.7);\qquad \dot C_b=\frac1{i\hbar}C_aV_{ba}e^{i\omega_{ba}t}\qquad(6.5.8),\ \text{p. 303}$$
con $\omega_{ba}=\omega_b-\omega_a$.
$$V_{ab}^*=V_{ba}=-\mu_{ba}\tilde E(t)=-\mu_{ba}(Ee^{-i\omega t}+E^*e^{i\omega t})\qquad(6.5.9)$$
$$\dot C_a=\frac{-\mu_{ab}}{i\hbar}C_b\left(E^*e^{-i(\omega_{ba}-\omega)t}+Ee^{-i(\omega_{ba}+\omega)t}\right)\qquad(6.5.10a)$$
$$\dot C_b=\frac{-\mu_{ba}}{i\hbar}C_a\left(Ee^{i(\omega_{ba}-\omega)t}+E^*e^{i(\omega_{ba}+\omega)t}\right)\qquad(6.5.10b),\ \text{p. 303}$$
RWA: se descartan los segundos términos (rápidos). Con $\Delta=\omega-\omega_{ba}$ (6.5.11):
$$\dot C_a=i\frac{\mu_{ab}E^*}{\hbar}C_be^{i\Delta t}\qquad(6.5.12a);\qquad \dot C_b=i\frac{\mu_{ba}E}{\hbar}C_ae^{-i\Delta t}\qquad(6.5.12b),\ \text{p. 303}$$

Solución de prueba:
$$C_a=Ke^{-i\lambda t}\qquad(6.5.13);\qquad C_b=\frac{-\hbar\lambda K}{\mu_{ab}E^*}e^{-i(\lambda+\Delta)t}\qquad(6.5.14),\ \text{p. 304}$$
y en (6.5.12b):
$$\lambda(\lambda+\Delta)=\frac{|\mu_{ba}|^2|E|^2}{\hbar^2}\qquad(6.5.15);\qquad \lambda_\pm=-\tfrac12\Delta\pm\tfrac12\Omega'\qquad(6.5.16)$$
con la **frecuencia de Rabi generalizada (o desintonizada)**
$$\Omega'=(|\Omega|^2+\Delta^2)^{1/2}\qquad(6.5.17),\ \text{p. 304}$$
y $\Omega=2\mu_{ba}E/\hbar$ (frecuencia de Rabi compleja). Solución general ($A_\pm$ = constantes de integración):
$$C_a(t)=e^{\frac12i\Delta t}\left(A_+e^{-\frac12i\Omega't}+A_-e^{\frac12i\Omega't}\right)\qquad(6.5.18a)$$
$$C_b(t)=\frac{-\hbar\dot C_a}{\mu_{ab}E^*}e^{-i\Delta t}=e^{-\frac12i\Delta t}\left(\frac{\Delta-\Omega'}{\Omega^*}A_+e^{-\frac12i\Omega't}+\frac{\Delta+\Omega'}{\Omega^*}A_-e^{\frac12i\Omega't}\right)\qquad(6.5.18b),\ \text{p. 304}$$

#### 6.5.2 Solución para un átomo inicialmente en el estado fundamental (p. 305–307)

$$C_a(0)=1,\quad C_b(0)=0\qquad(6.5.19);\qquad A_++A_-=1\qquad(6.5.20);\qquad (\Delta-\Omega')A_++(\Delta+\Omega')A_-=0\qquad(6.5.21)$$
$$A_+=1-A_-=\frac{\Omega'+\Delta}{2\Omega'}\qquad(6.5.22),\ \text{p. 305}$$
$$C_a(t)=e^{\frac12i\Delta t}\left[\cos(\tfrac12\Omega't)-\frac{i\Delta}{\Omega'}\sin(\tfrac12\Omega't)\right]\qquad(6.5.23)$$
$$C_b(t)=e^{-\frac12i\Delta t}\left(\frac{-\Omega}{2\Omega'}e^{-\frac12i\Omega't}+\frac{\Omega}{2\Omega'}e^{\frac12i\Omega't}\right)=ie^{-\frac12i\Delta t}\left[\frac{\Omega}{\Omega'}\sin(\tfrac12\Omega't)\right]\qquad(6.5.24),\ \text{p. 305}$$

> **Errata (p. 305):** en la primera línea de (6.5.23) los dos coeficientes se leen $(\Omega'+\Delta)/2\Omega'$. El segundo es $A_-=(\Omega'-\Delta)/2\Omega'$
> (de (6.5.22)); solo así se obtiene la segunda línea $\cos-\,(i\Delta/\Omega')\sin$, que sí es correcta.

$$|C_a|^2=\cos^2(\tfrac12\Omega't)+\frac{\Delta^2}{\Omega'^2}\sin^2(\tfrac12\Omega't)\qquad(6.5.25);\qquad |C_b|^2=\frac{|\Omega|^2}{\Omega'^2}\sin^2(\tfrac12\Omega't)\qquad(6.5.26)$$
$$|C_a|^2+|C_b|^2=1\qquad(6.5.27),\ \text{p. 305}$$
En resonancia exacta ($\Delta=0$):
$$|C_a|^2=\cos^2(\tfrac12|\Omega|t)\qquad(6.5.28a);\qquad |C_b|^2=\sin^2(\tfrac12|\Omega|t)\qquad(6.5.28b),\ \text{p. 306}$$
Las poblaciones oscilan entre 0 y 1 (Fig. 6.5.1, p. 306: $|C_a|^2$ y $|C_b|^2$ en contrafase). $C_a$ oscila a $|\Omega|/2$, la probabilidad a
$|\Omega|$ (la frecuencia de Rabi). Al aumentar $\Delta$ la oscilación es más rápida ($\Omega'$) pero de menor amplitud (Fig. 6.5.2, p. 306:
$|C_b|^2$ para $\Delta=0$, máximo 1, y $\Delta=2\Omega$, máximo $|\Omega|^2/\Omega'^2=1/5$, con frecuencia $\sqrt5$ veces mayor).

Dipolo inducido para el átomo inicialmente en $a$:
$$\langle\tilde\mu\rangle=\langle\psi|\hat\mu|\psi\rangle\qquad(6.5.29);\qquad \mu_{ab}=\langle a|\hat\mu|b\rangle=\langle b|\hat\mu|a\rangle^*=\mu_{ba}^*\qquad(6.5.30),\ \text{p. 307}$$
($\langle a|\hat\mu|a\rangle=\langle b|\hat\mu|b\rangle=0$)
$$\langle\tilde\mu\rangle=C_a^*C_b\mu_{ab}e^{-i\omega_{ba}t}+{\rm c.c.}\qquad(6.5.31)$$
$$\langle\tilde\mu\rangle=\mu_{ab}\frac{\Omega}{\Omega'}\left[\frac{-\Delta}{2\Omega'}e^{-i\omega t}+\frac14\left(\frac{\Delta}{\Omega'}-1\right)e^{-i(\omega+\Omega')t}+\frac14\left(\frac{\Delta}{\Omega'}+1\right)e^{-i(\omega-\Omega')t}\right]+{\rm c.c.}\qquad(6.5.32),\ \text{p. 307}$$

> **Errata (p. 307):** en el primer término de (6.5.32) se lee "$-\Delta/2\omega'$"; el cálculo directo con (6.5.23)–(6.5.24) da $-\Delta/2\Omega'$
> (Omega prima mayúscula, no omega minúscula).

El dipolo oscila a la frecuencia de forzamiento $\omega$ **y a las bandas laterales de Rabi** $\omega\pm\Omega'$. Origen: $C_a(t)$ contiene
frecuencias $-\frac12(\Delta\pm\Omega')$ y $C_b(t)$ contiene $\frac12(\Delta\pm\Omega')$; las frecuencias del dipolo son diferencias de las
componentes de frecuencia de la función de onda (Fig. 6.5.3).

Fig. 6.5.3 (p. 308): espectro de frecuencias de la función de onda (6.5.4). (a) $\Delta>0$: a campo débil, niveles $\omega_a$, $\omega_b$ y
niveles virtuales (punteados) desplazados $\Delta$; a campo fuerte, cada nivel se desdobla en dos separados $\Omega'$:
$\omega_b+\frac12\Delta\pm\frac12\Omega'$ y $\omega_a-\frac12\Delta\pm\frac12\Omega'$; las transiciones permitidas entre ellos dan $\omega-\Omega'$, $\omega$
(dos veces) y $\omega+\Omega'$. (b) $\Delta<0$: niveles $\omega_b-\frac12\Delta\pm\frac12\Omega'$ y $\omega_a+\frac12\Delta\pm\frac12\Omega'$.
(El pie de figura remite a "(6.5.28) y (6.5.29)" para $C_a$, $C_b$; por el contenido deberían ser (6.5.23) y (6.5.24).)

#### 6.5.3 Estados vestidos (p. 307–311)

(Autler y Townes, 1955; Cohen-Tannoudji y Reynaud, 1977.) Son soluciones con probabilidad de ocupación de $a$ (o $b$)
**constante en el tiempo**: $C_a$, $C_b$ solo dependen del tiempo vía factores de fase. A partir de (6.5.18):
$$A_+=1,\ A_-=0\ \ (\psi_+)\qquad(6.5.33a);\qquad A_+=0,\ A_-=1\ \ (\psi_-)\qquad(6.5.33b),\ \text{p. 308}$$
$$\psi_\pm=N_\pm\left\{u_a(\mathbf r)\exp[-i(\omega_a-\tfrac12\Delta\pm\tfrac12\Omega')t]+\frac{\Delta\mp\Omega'}{\Omega^*}u_b(\mathbf r)\exp[-i(\omega_b+\tfrac12\Delta\pm\tfrac12\Omega')t]\right\}\qquad(6.5.34),\ \text{p. 308}$$
Normalización:
$$\int|\psi_\pm|^2d^3r=1\qquad(6.5.35);\qquad |N_\pm|^2\left[1+\frac{(\Delta\mp\Omega')^2}{|\Omega|^2}\right]=1\qquad(6.5.36);\qquad N_\pm=\frac{\Omega^*}{\Omega'}\left[\frac{\Omega'}{2(\Omega'\mp\Delta)}\right]^{1/2}\qquad(6.5.37),\ \text{p. 309}$$
$$\psi_\pm=\frac{\Omega^*}{\Omega'}\left[\frac{\Omega'}{2(\Omega'\mp\Delta)}\right]^{1/2}u_a(\mathbf r)e^{-i(\omega_a-\frac12\Delta\pm\frac12\Omega')t}\mp\left[\frac{\Omega'\mp\Delta}{2\Omega'}\right]^{1/2}u_b(\mathbf r)e^{-i(\omega_b+\frac12\Delta\pm\frac12\Omega')t}\qquad(6.5.38),\ \text{p. 309}$$
Probabilidades:
$$\langle a|\psi_\pm\rangle=\frac{\Omega^*}{\Omega'}\left[\frac{\Omega'}{2(\Omega'\mp\Delta)}\right]^{1/2}e^{-i(\omega_a-\frac12\Delta\pm\frac12\Omega')t}\qquad(6.5.39);\qquad |\langle a|\psi_\pm\rangle|^2=\frac{|\Omega|^2}{\Omega'^2}\frac{\Omega'}{2(\Omega'\mp\Delta)}=\frac{|\Omega|^2}{2\Omega'(\Omega'\mp\Delta)}\qquad(6.5.40)$$
$$\langle b|\psi_\pm\rangle=\mp\left(\frac{\Omega'\mp\Delta}{2\Omega'}\right)^{1/2}e^{-i(\omega_b+\frac12\Delta\pm\frac12\Omega')t}\qquad(6.5.41);\qquad |\langle b|\psi_\pm\rangle|^2=\frac{\Omega'\pm\Delta}{2\Omega'}\ \text{(tal como se lee)}\qquad(6.5.42),\ \text{p. 309}$$

> **Errata (p. 309):** de (6.5.41) se sigue $|\langle b|\psi_\pm\rangle|^2=(\Omega'\mp\Delta)/2\Omega'$, no $(\Omega'\pm\Delta)/2\Omega'$ como se lee en (6.5.42).
> Además, usando $|\Omega|^2=\Omega'^2-\Delta^2$ en (6.5.40), $|\langle a|\psi_\pm\rangle|^2=(\Omega'\pm\Delta)/2\Omega'$, y solo con $\mp$ en (6.5.42) suman 1.

Las probabilidades son constantes: los estados vestidos son los **estados estacionarios del sistema acoplado átomo–campo**
(p. 309). Son soluciones de Schrödinger con $\hat H=\hat H_0+\hat V(t)$: si el sistema está en $\psi_+$ en $t=0$, permanece ahí.
No son autoestados de energía porque $\hat H$ depende explícitamente del tiempo (p. 310). Son ortogonales:
$$\langle\psi_+|\psi_-\rangle=0\qquad(6.5.43),\ \text{p. 310}$$
Dipolo inducido en un estado vestido (oscila solo a la frecuencia de forzamiento):
$$\langle\psi_\pm|\hat\mu|\psi_\pm\rangle=\mp\frac{\Omega}{2\Omega'}\mu_{ab}e^{-i\omega t}+{\rm c.c.}\qquad(6.5.44)$$
Momento de transición entre estados vestidos (no nulo):
$$\langle\psi_\pm|\hat\mu|\psi_\mp\rangle=\pm\mu_{ab}\frac{\Omega}{2\Omega'}\left(\frac{\Omega'\pm\Delta}{\Omega'\mp\Delta}\right)^{1/2}e^{-i(\omega\mp\Omega')t}\mp\mu_{ba}\frac{\Omega^*}{2\Omega'}\left(\frac{\Omega'\mp\Delta}{\Omega'\pm\Delta}\right)^{1/2}e^{i(\omega\pm\Omega')t}\qquad(6.5.45),\ \text{p. 310}$$
Fig. 6.5.4 (p. 310): diagrama de niveles de los estados vestidos $\psi_+$ y $\psi_-$ para (a) $\Delta>0$ y (b) $\Delta<0$, campo débil vs. fuerte.

**Límite de campo débil** ($|\Omega|\ll|\Delta|$):
$$\Omega'=(|\Omega|^2+\Delta^2)^{1/2}=|\Delta|\left(1+\frac{|\Omega|^2}{\Delta^2}\right)^{1/2}\simeq|\Delta|\left(1+\frac12\frac{|\Omega|^2}{\Delta^2}\right)\qquad(6.5.46),\ \text{p. 311}$$
Para $\Delta>0$:
$$\psi_+=\frac{\Omega^*}{|\Omega|}u_ae^{-i\omega_at}-\frac{|\Omega|}{2\Delta}u_be^{i(\omega_b+\Delta)t}\ \text{(tal como se lee)}\qquad(6.5.47a);\qquad \psi_-=\frac{\Omega^*}{2\Delta}u_ae^{-i(\omega_a-\Delta)t}+u_be^{-i\omega_bt}\qquad(6.5.47b)$$
$\psi_+$ es principalmente $\psi_a$ y $\psi_-$ principalmente $\psi_b$; la pequeña contribución a $\psi_+$ es el **nivel virtual** inducido por la transición.
Para $\Delta<0$:
$$\psi_+=-\frac{\Omega^*}{2\Delta}u_ae^{-i(\omega_a-\Delta)t}-u_be^{-i\omega_bt}\qquad(6.5.48a);\qquad \psi_-=\frac{\Omega^*}{|\Omega|}u_ae^{-i\omega_at}-\frac{|\Omega|}{2\Delta}u_be^{-i(\omega_b+\Delta)t}\qquad(6.5.48b),\ \text{p. 311}$$
Ahora $\psi_+$ es principalmente $\psi_b$ y $\psi_-$ principalmente $\psi_a$ (Fig. 6.5.5, p. 311: límite de campo débil; los niveles
punteados de las Figs. 6.5.3 y 6.5.4 anticipaban esto).

> **Errata (p. 311):** en (6.5.47a) la exponencial de $u_b$ se lee $e^{i(\omega_b+\Delta)t}$; de (6.5.38) con $\Omega'\simeq\Delta$ el exponente es
> $-i(\omega_b+\frac12\Delta+\frac12\Omega')t\simeq-i(\omega_b+\Delta)t$, como en (6.5.48b). Falta el signo menos.

#### 6.5.4 Inclusión de fenómenos de relajación (p. 312–313)

Sin amortiguamiento basta Schrödinger; la inversión oscila a $\Omega'=(\Omega^2+\Delta^2)^{1/2}$. Con amortiguamiento las oscilaciones
de Rabi se amortiguan y la diferencia de población tiende a un valor estacionario. Ecuaciones de la matriz densidad:
$$\dot p=\left(i\Delta-\frac1{T_2}\right)p-\frac{i}{\hbar}|\mu|^2Ew\qquad(6.5.49a);\qquad \dot w=-\frac{w+1}{T_1}-\frac{2i}{\hbar}(pE^*-p^*E)\qquad(6.5.49b),\ \text{p. 312}$$
con átomo en el fundamental en $t=0$:
$$p(0)=0,\quad w(0)=-1\qquad(6.5.50)$$
y campo encendido en $t=0$ ($E=0$ para $t<0$, constante para $t\ge0$). Solución general: Problema 4. Para $T_1=T_2$:
$$w(t)=w_0-(1+w_0)e^{-t/T_2}\left[\cos\Omega't+\frac{1}{\Omega'T_2}\sin\Omega't\right]\qquad(6.5.51a)$$
$$w_0=\frac{-(1+\Delta^2T_2^2)}{1+\Delta^2T_2^2+\Omega^2T_1T_2}\qquad(6.5.51b),\ \text{p. 312}$$
($w_0$ coincide con el valor estacionario (6.3.11) con $(\rho_{bb}-\rho_{aa})^{(\rm eq)}=-1$.) Fig. 6.5.6 (p. 313): oscilaciones de Rabi amortiguadas de
$w(t)$, que parte de $-1$, sobrepasa y oscila alrededor de $w_0$, amortiguándose en ~$T_2$. Tras el amortiguamiento el sistema
entra en uno de los estados vestidos del sistema átomo–campo. En el estado estacionario no hay oscilaciones de Rabi.
Resumen: sin amortiguamiento, la inversión oscila a $\Omega'$ y el dipolo a $\omega$ y $\omega\pm\Omega'$; con desfase, las oscilaciones
mueren en ~$T_2$. Adelanto de 6.6: con un campo fuerte a $\omega$ y uno débil a $\omega+\delta$, si $\delta$ (o $-\delta$) ≈ $\Omega'$ la frecuencia
de batido puede forzar la oscilación de Rabi; la diferencia de población oscila a $\delta$ y el dipolo contiene $\omega$ y $\omega\pm\delta$ (p. 313).

### 6.6 Mezcla de ondas ópticas en sistemas de dos niveles (p. 313–326)

Un campo fuerte (**bombeo**) y uno o más campos débiles (**sondas**, incapaces por sí solos de saturar el sistema). Ejemplo:
**espectroscopía de saturación** (Fig. 6.6.1, p. 314: bombeo fuerte $\omega$ y sonda débil $\omega+\delta$ cruzan un vapor atómico y se
mide la transmisión de la sonda en función de $\omega$, de la intensidad del bombeo y de $\delta$; da información sobre momentos
dipolares, $T_1$ y $T_2$). Otro ejemplo: **mezcla de cuatro ondas hacia adelante** (Fig. 6.6.2, p. 314: (a) bombeo $\omega$ y sonda $\omega+\delta$
copropagantes generan la banda lateral simétrica $\omega-\delta$, casi en ajuste de fase; (b) diagrama de niveles: $\omega+\omega\to(\omega+\delta)+(\omega-\delta)$,
dibujado para $\delta<0$). A baja intensidad de bombeo (teoría de perturbaciones del cap. 3): la absorción y dispersión de la sonda
se reducen algo por el bombeo, y la intensidad de la banda $\omega-\delta$ crece cuadráticamente con la intensidad del bombeo. Esto se
modifica profundamente cuando la frecuencia de Rabi $\Omega$ del bombeo supera la desintonía $\Delta$ y el ancho $1/T_2$: los niveles
se modifican fuertemente y aparecen **nuevas resonancias** en las respuestas de absorción y mezcla cuando $\delta\approx\pm\Omega'$ (p. 315).

#### 6.6.1 Solución de las ecuaciones de la matriz densidad para un átomo de dos niveles con campos de bombeo y sonda (p. 315–320)

$$\tilde E(t)=Ee^{-i\omega t}+{\rm c.c.}\qquad(6.6.1);\qquad \tilde p(t)=pe^{-i\omega t}+{\rm c.c.}\qquad(6.6.2),\ \text{p. 315}$$
con $w=\rho_{bb}-\rho_{aa}$, $p=\mu_{ab}\sigma_{ba}$:
$$\frac{dp}{dt}=\left(i\Delta-\frac1{T_2}\right)p-\frac{i}{\hbar}|\mu_{ba}|^2Ew\qquad(6.6.3);\qquad \frac{dw}{dt}=-\frac{w-w^{(\rm eq)}}{T_1}+\frac4\hbar{\rm Im}(pE^*)\qquad(6.6.4)$$
($\Delta=\omega-\omega_{ba}$). Amplitud del campo:
$$E=E_0+E_1e^{-i\delta t}\qquad(6.6.5),\quad |E_1|\ll|E_0|;\qquad \tilde E(t)=E_0e^{-i\omega t}+E_1e^{-i(\omega+\delta)t}+{\rm c.c.}\qquad(6.6.6),\ \text{p. 315}$$
$E_0$, $E_1$: amplitudes complejas del bombeo y de la sonda.

No hay solución exacta; se busca una solución **exacta en $E_0$ y a primer orden en $E_1$**. Forma estacionaria:
$$p=p_0+p_1e^{-i\delta t}+p_{-1}e^{i\delta t}\qquad(6.6.7);\qquad w=w_0+w_1e^{-i\delta t}+w_{-1}e^{i\delta t}\qquad(6.6.8),\ \text{p. 316}$$
$p_0$, $w_0$: solución solo con bombeo;
$$|p_1|,|p_{-1}|\ll|p_0|,\qquad |w_1|,|w_{-1}|\ll|w_0|\qquad(6.6.9)$$
A primer orden en $E_1$ solo aparecen las frecuencias $0$ y $\pm\delta$. Como $w$ es real, $w_{-1}=w_1^*$ y
$w(t)=w_0+2|w_1|\cos(\delta t+\phi)$: **la diferencia de población oscila armónicamente a la frecuencia de batido bombeo–sonda**, con
amplitud compleja $w_1$. Se igualan términos con igual dependencia temporal y se descartan productos de dos cantidades
pequeñas. Parte de frecuencia cero de (6.6.3): $0=(i\Delta-1/T_2)p_0-\frac{i}{\hbar}|\mu_{ba}|^2E_0w_0$:
$$p_0=\frac{\hbar^{-1}|\mu_{ba}|^2E_0w_0}{\Delta+i/T_2}\qquad(6.6.10),\ \text{p. 316}$$
Parte $e^{-i\delta t}$: $-i\delta p_1=(i\Delta-1/T_2)p_1-\frac{i}{\hbar}|\mu_{ba}|^2(E_0w_1+E_1w_0)$:
$$p_1=\frac{\hbar^{-1}|\mu_{ba}|^2(E_0w_1+E_1w_0)}{(\Delta-\delta)+i/T_2}\ \text{(tal como se lee)}\qquad(6.6.11),\ \text{p. 317}$$

> **Errata (p. 317):** despejando $p_1$ de la ecuación anterior se obtiene el denominador $(\Delta+\delta)+i/T_2$, no $(\Delta-\delta)+i/T_2$ (el
> texto repite por error el denominador de (6.6.12)). La propia ec. sin numerar que precede a (6.6.19) usa $\Delta+\delta+i/T_2$ en los términos
> que vienen de $p_1$, confirmando la corrección.

Parte $e^{i\delta t}$: $i\delta p_{-1}=(i\Delta-1/T_2)p_{-1}-\frac{i}{\hbar}|\mu_{ba}|^2(E_0w_{-1})$:
$$p_{-1}=\frac{\hbar^{-1}|\mu_{ba}|^2E_0w_{-1}}{(\Delta-\delta)+i/T_2}\qquad(6.6.12),\ \text{p. 317}$$
Inversión, parte de frecuencia cero:
$$0=-\frac{w_0-w^{(\rm eq)}}{T_1}+\frac4\hbar{\rm Im}(p_0E_0^*)\qquad(6.6.13)$$
$$\frac{w_0-w^{(\rm eq)}}{T_1}=\Omega^2w_0\,{\rm Im}\left(\frac{\Delta-i/T_2}{\Delta^2+1/T_2^2}\right)=\frac{-\Omega^2w_0/T_2}{\Delta^2+1/T_2^2}\qquad(6.6.14)$$
($\Omega=2|\mu_{ba}E|/\hbar$, aquí con $E\to E_0$)
$$w_0=\frac{w^{(\rm eq)}(1+\Delta^2T_2^2)}{1+\Delta^2T_2^2+\Omega^2T_1T_2}\qquad(6.6.15),\ \text{p. 317}$$
(igual a (6.3.11)). Parte oscilante de ${\rm Im}(pE^*)$ a $\pm\delta$, con ${\rm Im}\,z=(z-z^*)/2i$:
$${\rm Im}(pE^*)={\rm Im}(p_0E_1^*e^{i\delta t}+p_1E_0^*e^{-i\delta t}+p_{-1}E_0^*e^{i\delta t})=\frac1{2i}\left(p_0E_1^*e^{i\delta t}+p_1E_0^*e^{-i\delta t}+p_{-1}E_0^*e^{i\delta t}-p_0^*E_1e^{-i\delta t}-p_1^*E_0e^{i\delta t}-p_{-1}^*E_0e^{-i\delta t}\right)\qquad(6.6.16)$$
Parte $e^{-i\delta t}$ de (6.6.4): $-i\delta w_1=-\frac{w_1}{T_1}-\frac{2i}{\hbar}(p_1E_0^*-p_0^*E_1-p_{-1}^*E_0)$ (p. 317), de donde
$$w_1=\frac{2\hbar^{-1}(p_1E_0^*-p_0^*E_1-p_{-1}^*E_0)}{\delta+i/T_1}\qquad(6.6.17);\qquad w_{-1}=\frac{2\hbar^{-1}(p_1^*E_0-p_0E_1^*-p_{-1}E_0^*)}{\delta-i/T_1}\qquad(6.6.18),\ \text{p. 318}$$
con $w_{-1}=w_1^*$, como debe ser. Seis ecuaciones acopladas [(6.6.10), (6.6.11), (6.6.12), (6.6.15), (6.6.17), (6.6.18)] para
$p_0,p_1,p_{-1},w_0,w_1,w_{-1}$; $w_0$ ya es conocido; se resuelve primero $w_1$ sustituyendo $p_1$, $p_0$, $p_{-1}$ en (6.6.17):
$$\left(\delta+\frac{i}{T_1}\right)w_1=\frac{2|\mu_{ba}|^2}{\hbar^2}\left(\frac{|E_0|^2w_1}{\Delta+\delta+i/T_2}+\frac{E_1E_0^*w_0}{\Delta+\delta+i/T_2}-\frac{E_1E_0^*w_0}{\Delta-i/T_2}-\frac{|E_0|^2w_1}{\Delta-\delta-i/T_2}\right)\qquad\text{(p. 318)}$$
$$w_1=-\frac{w_0^2|\mu_{ba}|^2E_1E_0^*\hbar^{-2}(\delta-\Delta+i/T_2)(\delta+2i/T_2)(\Delta-i/T_2)^{-1}}{(\delta+i/T_1)(\delta-\Delta+i/T_2)(\Delta+\delta+i/T_2)-\Omega^2(\delta+i/T_2)}\ \text{(tal como se lee)}\qquad(6.6.19),\ \text{p. 318}$$
Denominador:
$$D(\delta)=\left(\delta+\frac{i}{T_1}\right)\left(\delta-\Delta+\frac{i}{T_2}\right)\left(\delta+\Delta+\frac{i}{T_2}\right)-\Omega^2\left(\delta+\frac{i}{T_2}\right)\qquad(6.6.20)$$
$$w_1=-2w_0|\mu_{ba}|^2E_1E_0^*\hbar^{-2}\frac{(\delta-\Delta+i/T_2)(\delta+2i/T_2)}{(\Delta-i/T_2)D(\delta)}\qquad(6.6.21),\ \text{p. 318}$$

> **Duda (p. 318):** (6.6.19) lleva $w_0^2$ y sin factor 2, mientras que (6.6.21), que se presenta como la misma ecuación reescrita, lleva
> $2w_0$. Resolviendo la ecuación lineal en $w_1$ de la p. 318 se obtiene un numerador lineal en $w_0$ con factor $2|\mu_{ba}|^2/\hbar^2$, es decir, la
> forma de (6.6.21); el "$w_0^2$" sin 2 de (6.6.19) parece errata. Las fórmulas posteriores (6.6.35)–(6.6.36) usan la forma de (6.6.21).

$w_1$ (y por tanto $p_1$, $p_{-1}$) es resonante si el bombeo está en el centro de línea ($\Delta=0$) o donde $D(\delta)=0$.

**Límite perturbativo** $\Omega^2\to0$ (teoría de $\chi^{(3)}$): $D$ se factoriza
$$D(\delta)=\left(\delta+\frac{i}{T_1}\right)\left(\delta-\Delta+\frac{i}{T_2}\right)\left(\Delta+\delta+\frac{i}{T_2}\right)\qquad(6.6.22);\qquad \text{ceros en }\delta=0,\pm\Delta\qquad(6.6.23),\ \text{p. 319}$$
(Fig. 6.6.3a). En $\delta=\Delta$ no hay resonancia en $w_1$ porque $\delta-\Delta+i/T_2$ del numerador cancela el del denominador; pero
si se conserva el término en $\Omega^2$ aparece una resonancia **cerca** de $\delta=\Delta$, cuya contribución de menor orden es $\chi^{(5)}$.
Fig. 6.6.3 (p. 319): resonancias de $D(\delta)$; (a) $\Omega^2\to0$: $\delta=-\Delta,0,\Delta$; (b) caso general: niveles vestidos desdoblados en
$\Omega'$, transiciones a $\omega-\Omega'$, $\omega$, $\omega+\Omega'$.

**Caso general** ($\Omega^2$ no pequeño): partes real e imaginaria de $D$, con $\Omega'=(\Omega^2+\Delta^2)^{1/2}$:
$$D(\delta)=\delta\left(\delta^2-\Omega'^2-\frac1{T_2^2}-\frac2{T_1T_2}\right)+i\left(\frac{\delta^2-\Delta^2}{T_1}+\frac{2\delta^2}{T_2}-\frac{\Omega^2}{T_2}-\frac1{T_1T_2^2}\right)\qquad(6.6.24),\ \text{p. 320}$$
La parte real se anula en
$$\delta=0,\qquad \delta=\pm\left(\Omega'^2+\frac1{T_2^2}+\frac2{T_1T_2}\right)^{1/2}\qquad(6.6.25)$$
Si $\Omega'T_2\gg1$, las tres resonancias están bien separadas:
$$D(\delta)=\delta(\delta^2-\Omega'^2)+i\left(\frac{\delta^2-\Delta^2}{T_1}+\frac{2\delta^2-\Omega^2}{T_2}\right)\qquad(6.6.26);\qquad \delta=0,\ \pm\Omega'\qquad(6.6.27),\ \text{p. 320}$$
Cerca de $\delta=0$:
$$D(\delta)=-\Omega'^2(\delta+i\Gamma_0)\qquad(6.6.28a);\qquad \Gamma_0=\frac{\Delta^2/T_1+\Omega^2/T_2}{\Delta^2+\Omega^2}\qquad(6.6.28b)$$
Cerca de $\delta=\mp\Omega'$:
$$D(\delta)=2\Omega'^2[(\delta\pm\Omega')+i\Gamma_\pm]\qquad(6.6.29a);\qquad \Gamma_\pm=\frac{\Omega^2/T_1+(2\Delta^2+\Omega^2)/T_2}{2(\Omega^2+\Delta^2)}\qquad(6.6.29b),\ \text{p. 320}$$
Las posiciones se entienden con las energías de los estados vestidos (Fig. 6.6.3b). Excitación débil ($\Omega^2\ll\Delta^2$): $\Gamma_0\to1/T_1$,
$\Gamma_\pm\to1/T_2$. Excitación fuerte ($\Omega^2\gg\Delta^2$): $\Gamma_0\to1/T_2$, $\Gamma_\pm\to\frac12(1/T_1+1/T_2)$ (p. 320–321).

**Respuesta del dipolo en las bandas laterales.** Sustituyendo $w_1$ en $p_1$:
$$p_1=\frac{\hbar^{-1}|\mu_{ba}|^2w_0E_1}{\Delta+\delta+i/T_2}\left[1-\frac{\tfrac12\Omega^2(\delta-\Delta+i/T_2)(\delta+2i/T_2)/(\Delta-i/T_2)}{(\delta+i/T_1)(\delta-\Delta+i/T_2)(\Delta+\delta+i/T_2)-\Omega^2(\delta+i/T_2)}\right]\qquad(6.6.30),\ \text{p. 321}$$
Dos contribuciones a la respuesta en $\omega+\delta$: la de la parte de frecuencia cero de $w$ (resonante solo en $\delta=-\Delta$) y la de las
**oscilaciones de población** (con las resonancias adicionales de $D(\delta)$). Sargent (1978): el segundo término cumple
$$\int_{-\infty}^{\infty}\frac{-\tfrac12\Omega^2(\delta-\Delta+i/T_2)(\delta+2i/T_2)(\Delta-i/T_2)^{-1}}{(\delta+i/T_1)(\delta-\Delta+i/T_2)(\Delta+\delta+i/T_2)-\Omega^2(\delta+i/T_2)}d\delta=0\qquad(6.6.31),\ \text{p. 321}$$
→ las oscilaciones de población no cambian la absorción integrada, solo la **redistribuyen espectralmente**. Forma combinada:
$$p_1=\frac{\hbar^{-1}|\mu_{ba}|^2w_0E_1}{D(\delta)}\left[\left(\delta+\frac{i}{T_1}\right)\left(\delta-\Delta+\frac{i}{T_2}\right)-\frac12\Omega^2\frac{\delta}{\Delta-i/T_2}\right]\qquad(6.6.32)$$
Banda lateral opuesta (con (6.6.12), (6.6.21) y $w_{-1}=w_1^*$):
$$p_{-1}=\frac{2w_0|\mu_{ba}|^4E_0^2E_1^*(\delta-\Delta-i/T_2)(-\delta+2i/T_2)(\Delta+i/T_2)^{-1}}{\hbar^3(\Delta-\delta+i/T_2)D^*(\delta)}\qquad(6.6.33),\ \text{p. 321}$$

#### 6.6.2 Susceptibilidad no lineal y ecuaciones de amplitudes acopladas (p. 322–326)

$P(\omega+\delta)=Np_1\equiv\epsilon_0\chi^{(1)}_{\rm eff}(\omega+\delta)E_1$:
$$\chi^{(1)}_{\rm eff}(\omega+\delta)=\frac{N|\mu_{ba}|^2w_0}{\epsilon_0\hbar D(\delta)}\left[\left(\delta+\frac{i}{T_1}\right)\left(\delta-\Delta+\frac{i}{T_2}\right)-\frac12\Omega^2\frac{\delta}{\Delta-i/T_2}\right]\qquad(6.6.34),\ \text{p. 322}$$
("susceptibilidad lineal efectiva": depende de la intensidad del bombeo). $P(\omega-\delta)=Np_{-1}\equiv3\epsilon_0\chi^{(3)}_{\rm eff}[\omega-\delta=\omega+\omega-(\omega+\delta)]E_0^2E_1^*$:
$$\chi^{(3)}_{\rm eff}[\omega-\delta=\omega+\omega-(\omega+\delta)]=\frac{2Nw_0|\mu_{ba}|^4(\delta-\Delta-i/T_2)(-\delta+2i/T_2)(\Delta+i/T_2)^{-1}}{3\epsilon_0\hbar^3(\Delta-\delta+i/T_2)D^*(\delta)}\qquad(6.6.35),\ \text{p. 322}$$
Si además está presente la onda generada $E_{-1}$ en $\omega-\delta$ (geometría de la Fig. 6.6.2):
$$P(\omega+\delta)=\epsilon_0\chi^{(1)}_{\rm eff}(\omega+\delta)E_1+3\epsilon_0\chi^{(3)}_{\rm eff}[\omega+\delta=\omega+\omega-(\omega-\delta)]E_0^2E_{-1}^*\qquad(6.6.36a)$$
$$P(\omega-\delta)=\epsilon_0\chi^{(1)}_{\rm eff}(\omega-\delta)E_{-1}+3\epsilon_0\chi^{(3)}_{\rm eff}[\omega-\delta=\omega+\omega-(\omega+\delta)]E_0^2E_1^*\qquad(6.6.36b),\ \text{p. 322}$$
($\chi^{(1)}_{\rm eff}(\omega-\delta)$ y $\chi^{(3)}_{\rm eff}[\omega+\delta=\ldots]$: reemplazar $\delta\to-\delta$ en (6.6.34)–(6.6.35)). Propagación (métodos del cap. 2):
$$E_{\pm1}=A_{\pm1}e^{ik_{\pm1}z}\qquad(6.6.37a);\qquad k_{\pm1}=n_{\pm1}(\omega\pm\delta)/c\qquad(6.6.37b);\qquad n_{\pm1}^2=1+{\rm Re}\,\chi^{(1)}_{\rm eff}(\omega\pm\delta)\qquad(6.6.37c),\ \text{p. 323}$$
Con la ecuación de onda (2.1.22) y la aproximación de amplitud lentamente variable:
$$\frac{dA_1}{dz}=-\alpha_1A_1+\kappa_1A_{-1}^*e^{i\Delta kz}\qquad(6.6.38a);\qquad \frac{dA_{-1}}{dz}=-\alpha_{-1}A_{-1}+\kappa_{-1}A_1^*e^{i\Delta kz}\qquad(6.6.38b)$$
$$\alpha_{\pm1}=-\frac12\left(\frac{\omega\pm\delta}{n_{\pm1}c}\right){\rm Im}\,\chi^{(1)}_{\rm eff}(\omega\pm\delta)\ \text{(tal como se lee)}\qquad(6.6.39a)$$
$$\kappa_{\pm1}=-i\frac32\left(\frac{\omega\pm\delta}{n_{\pm1}c}\right)\chi^{(3)}_{\rm eff}[\omega\pm\delta=\omega+\omega-(\omega\mp\delta)]A_0^2\ \text{(tal como se lee)}\qquad(6.6.39b);\qquad \Delta k=2k_0-k_1-k_{-1}\qquad(6.6.39c),\ \text{p. 323}$$
$k_0$: número de onda del bombeo. Nota al pie (p. 324): se puso arbitrariamente Re $\chi^{(1)}_{\rm eff}$ en $n_{\pm1}$ e Im en $\alpha_{\pm1}$; equivalentemente todo en
un $\alpha_{\pm1}$ complejo con $\Delta k=0$, o todo en un $n_{\pm1}$ complejo con $\alpha_{\pm1}=0$ (ver Problema 7).

> **Duda de signos (p. 323):** con la convención de Boyd $\tilde E=Ae^{i(kz-\omega t)}+{\rm c.c.}$ y la ecuación de amplitud lentamente variable
> $dA/dz=\frac{i\omega}{2nc}\frac{P_{\rm NL}}{\epsilon_0}e^{-ikz}$, se obtiene $\alpha_{\pm1}=+\frac12\frac{\omega\pm\delta}{n_{\pm1}c}{\rm Im}\,\chi^{(1)}_{\rm eff}$ (positivo para un medio
> absorbente, como exige que la p. 324 lo llame "coeficiente de absorción") y $\kappa_{\pm1}=+i\frac32\frac{\omega\pm\delta}{n_{\pm1}c}\chi^{(3)}_{\rm eff}A_0^2$. Los signos
> impresos en (6.6.39a,b) parecen invertidos; no se verificó con la fe de erratas oficial.

Resolución: formalmente equivalente al acoplamiento Stokes–anti-Stokes del Raman estimulado (cap. 10); detalle para dos niveles en
Boyd *et al.* (1981): amplificación significativa de $A_1$ y $A_{-1}$ cerca de la dirección hacia adelante, especialmente grande cuando
$\pm\delta\approx\Omega'$; experimentos: Harter *et al.* (1981). En la geometría de la Fig. 6.6.1 (ángulo $\theta$ grande entre bombeo y sonda),
$\Delta k$ es muy grande y las ecuaciones se desacoplan:
$$\frac{dA_1}{dz}=-\alpha_1A_1,\qquad \frac{dA_{-1}}{dz}=-\alpha_{-1}A_{-1}\qquad(6.6.40),\ \text{p. 324}$$
$\alpha_{\pm1}$ depende de $\delta$, de $\Delta$ y de la intensidad $I$ del bombeo.

**Espectro de absorción de la sonda** (Fig. 6.6.4, p. 325, para $\Delta T_2=-3$, $\Omega T_2=8$, $T_2/T_1=2$): tres rasgos, uno en la frecuencia
del láser ($\delta=0$) y dos en las **bandas laterales de Rabi** $\delta=\pm\Omega'$. $\alpha_1$ puede volverse **negativa** (ganancia) en dos de ellos
(predicho por Mollow, 1972; observado por Wu *et al.*, 1977, y Gruneisen *et al.*, 1988, 1989):
- **TP** (resonancia de tres fotones, en $\delta=-\Omega'$ en la figura): ganancia; el átomo pasa del nivel vestido más bajo al más alto
  absorbiendo dos fotones del bombeo y emitiendo uno en $\omega-\Omega'$.
- **RL** (resonancia de Rayleigh, cerca de $\delta=0$): rasgo dispersivo pequeño con ganancia; forma de **dispersión Rayleigh estimulada**
  (cap. 9), o equivalentemente debida a las **oscilaciones coherentes de población** (6.6.8), (6.6.21); transición del nivel inferior del
  doblete inferior al doblete superior, centrada en la frecuencia del bombeo. Su ganancia se ha usado para construir osciladores
  paramétricos ópticos (Grandclement *et al.*, 1987).
- **AC** (resonancia atómica corrida por efecto Stark ac, en $\delta=+\Omega'$): solo absorción; para el signo de desintonía de la figura se
  corre a frecuencias más altas.
Por Kramers–Kronig, a la ganancia estrecha se asocia una variación rápida del índice → gran modificación de la velocidad de grupo
$v_g=c/n_g$, $n_g=n+\omega(dn/d\omega)$: **luz lenta** ($n_g\gg1$), **luz rápida** ($0<n_g\ll1$) y $n_g<0$ (propagación "hacia atrás") (Bigelow
*et al.*, 2003a, b; Gehring *et al.*, 2006) (p. 325–326). Agarwal y Boyd (1988) generalizaron la teoría al campo cuantizado: las
fluctuaciones cuánticas pueden iniciar esta mezcla de cuatro ondas (p. 326).
(En la p. 326 aparece la errata tipográfica "ac= Stark effect".)

---

## Tablas y datos numéricos útiles del capítulo

| Magnitud | Valor | Condiciones | Fuente |
|---|---|---|---|
| $T_1$, línea 3s→3p del Na | 16 ns | — | p. 283, 293 |
| $C_s$ (autoensanchamiento, Na) | $1.50\times10^{-7}$ cm³/s | (6.2.21b) | p. 283 |
| $C_f$ (Na con Ar) | $2.53\times10^{-9}$ cm³/s | (6.2.21b) | p. 283 |
| $|\mu_{ba}|$, Na 3s→3p | $2.5ea_0=2.0\times10^{-29}$ C·m | — | p. 293 |
| $\Omega/2\pi$ | 1 GHz a $I=127$ W/cm² | (6.3.39) | p. 293 |
| $I_s^0$ | 5.27 mW/cm² = 52.7 W/m² | $T_1=16$ ns, $T_2=2T_1$ (ver duda) | p. 293 |
| $\chi^{(3)}$ casi resonante | $2.1\times10^{-16}$ m²/V² | $N=10^{14}$ cm⁻³, $w^{(\rm eq)}=-1$, $\Delta/2\pi c=1$ cm⁻¹, $T_2/T_1=2$ | p. 293 |
| Ancho FWHM (campo débil) | $2/T_2=2\gamma_{ba}$ | (6.3.25) con $\Omega\to0$ | p. 281, 289 |
| Ensanchamiento por potencia | factor $(1+\Omega^2T_1T_2)^{1/2}=(1+I/I_s^0)^{1/2}$ | en el centro de línea | p. 289 |
| Fig. 6.6.4 | $\Delta T_2=-3$, $\Omega T_2=8$, $T_2/T_1=2$ | espectro de la sonda | p. 325 |

Resumen de fórmulas clave: $\chi=-\frac{\alpha_0(0)c}{\omega_{ba}}\frac{\Delta T_2-i}{1+\Delta^2T_2^2+I/I_s^0}$; $\chi^{(3)}=-\chi^{(1)}/(3|E_s^\Delta|^2)$; $\Omega'=(|\Omega|^2+\Delta^2)^{1/2}$;
resonancias de bombeo–sonda en $\delta=0,\pm\Omega'$ con anchos $\Gamma_0$, $\Gamma_\pm$.

---

## Problemas (p. 326–327)

1. *Modelos alternativos de relajación.* Determinar cómo depende la absorción saturada de una transición atómica de la intensidad del
   campo láser incidente (monocromático) para un átomo de dos niveles abierto y para un átomo de dos niveles con un nivel intermedio
   acoplado no radiativamente, y comparar con los resultados de la sección 6.3 para el átomo cerrado.
2. *$\chi^{(3)}$ de un sólido dopado con impurezas.* Interesa a menudo el $\chi^{(3)}$ de un conjunto de átomos de dos niveles contenidos en
   un medio de índice constante $n_0$ (independiente de la longitud de onda y de la intensidad). Demostrar que el $\chi^{(3)}$ de tal sistema
   está dado por (6.3.36b) tal como aparece, o por (6.3.33b) con un factor $n_0$ en el numerador, o por (6.3.34a) o (6.3.34b) con un
   factor $n_0^2$ en el numerador. Cuando aparezcan $I_s^0$, $I_s^\Delta$ o $\alpha_0(\Delta)$, se entiende que las expresiones (6.3.30) y (6.3.31)
   para $I_s^0$ e $I_s^\Delta$ deben multiplicarse cada una por $n_0$ y la expresión (6.3.22b) para $\alpha_0(0)$ debe dividirse por $n_0$.
3. *Ortogonalidad de los estados vestidos.* Verificar (6.5.43).
4. *Amortiguamiento de las oscilaciones de Rabi.* Determinar la influencia de los procesos de relajación tipo $T_1$ y $T_2$ sobre las
   oscilaciones de Rabi predichas por la solución de Schrödinger para un átomo con campo intenso casi resonante. Resolver la ecuación
   de Bloch en la forma (6.5.49) para un átomo en el fundamental en $t=0$ sometido a un campo $Ee^{-i\omega t}+{\rm c.c.}$ encendido en $t=0$.
   Además, esbozar $w$ y $p$ en función del tiempo. [Pista: en cierto punto la complejidad se reduce mucho suponiendo $T_1=T_2$; hacer
   esta simplificación solo cuando sea necesario.]
5. *Tiempos de respuesta.* Estimar el tiempo de respuesta de no linealidades electrónicas no resonantes como las de la sección 4.3.
   El estudiante A argumenta que es bien sabido que el tiempo de respuesta es del orden del inverso de la desintonía del láser respecto
   de la resonancia atómica más cercana. El estudiante B argumenta que solo los procesos de relajación permiten al sistema llegar al
   estado estacionario y que, por tanto, el tiempo de respuesta es del orden del mayor de $T_1$ y $T_2$, es decir, del orden de $T_1$.
   ¿Quién tiene razón y en qué sentido es correcto cada uno? [Pista: considerar cómo se vería la Fig. 6.5.6 y la gráfica análoga de
   $p(t)$ en el límite $\Delta\gg\Omega$, $\Delta T_2\gg1$.] [Respuesta parcial: la no linealidad se enciende en un tiempo $\Delta^{-1}$ pero no alcanza
   su valor estacionario hasta un tiempo del orden de $T_1$.]
6. *Identidad relativa a las oscilaciones de población.* Verificar (6.6.31).
7. *Ecuaciones de onda acopladas para la mezcla de cuatro ondas hacia adelante.* Verificar que (6.6.38) se siguen de las ecuaciones
   referidas. Además, escribir explícitamente las dos formas alternativas de estas ecuaciones mencionadas en la nota al pie.

## Referencias principales (p. 327–328)

Allen y Eberly (1975), *Optical Resonance and Two-Level Atoms*; Cohen-Tannoudji, Dupont-Roc y Grynberg (1989), *Photons and Atoms*
(y *Atom–Photon Interactions*, 1991); Sargent (1978), *Phys. Rep.* 43, 223; Boyd y Sargent (1988), *JOSA B* 5, 1; Sargent, Scully y
Lamb (1974), *Laser Physics*; Autler y Townes (1955), *Phys. Rev.* 100, 703; Cohen-Tannoudji y Reynaud (1977), *J. Phys. B* 10;
Mollow (1972), *Phys. Rev. A* 5, 2217; Wu *et al.* (1977), *PRL* 38, 1077; Grischkowsky (1970), *PRL* 24, 866; Boyd, Raymer, Narum y
Harter (1981), *PRA* 24, 411; Harter *et al.* (1981), *PRL* 46, 1192; Gruneisen *et al.* (1988, 1989); Agarwal y Boyd (1988), *PRA* 38,
4019; Bigelow, Lepeshkin y Boyd (2003a, *PRL* 90, 113903; 2003b, *Science* 301, 200); Gehring *et al.* (2006), *Science* 312, 985;
Miles y Harris (1973), *IEEE JQE* 9, 470; Grandclement *et al.* (1987), *PRL* 59, 44; Dicke y Wittke (1960).

---

## Relación con el curso y con el proyecto final

- **Curso.** El capítulo no está en el programa explícito (tema 4 = cap. 1; tema 5 = cap. 2; tema 6 = 4.1, 4.2, 7.1, 7.2), pero
  complementa el tema 6: da el modelo microscópico más simple de un $n_2$ (y de $\beta$, vía Im $\chi^{(3)}$) **resonante**, y muestra que
  $\chi^{(3)}=-\chi^{(1)}/(3|E_s^\Delta|^2)$ tiene signo opuesto a $\chi^{(1)}$ (saturación): por debajo de la resonancia ($\Delta<0$) Re $\chi^{(3)}<0$
  y por encima Re $\chi^{(3)}>0$ (Fig. 6.3.3). Con $n_2=3\chi^{(3)}/(4n_0^2\epsilon_0c)$ (Boyd 4.1.19) se conecta directamente con 4.1. Ilustra
  también por qué la serie de potencias (6.1.1) solo vale para $I<I_s$ (6.1.3), y el Problema 5 responde a la pregunta del tiempo de
  respuesta de la no linealidad electrónica no resonante (~$1/\Delta$, cf. 4.3). El valor numérico $\chi^{(3)}\sim10^{-16}$ m²/V² en vapor de Na
  frente a ~$10^{-22}$ m²/V² de sólidos no resonantes (cap. 4) muestra el realce resonante a costa de absorción y lentitud ($T_1$).
- **Proyecto final (supercontinuo en guías de SiN/Si).** En SiN y Si el bombeo (≈1.55 µm) está lejos de resonancias electrónicas
  (régimen $|\Delta|T_2\gg1$, $|\Delta|\gg\Omega$): el Kerr es no resonante, prácticamente instantáneo (tiempo ~$1/\Delta$, Problema 5 y §6.4.2
  de seguimiento adiabático), y vale el desarrollo perturbativo; el modelo de dos niveles no se usa para calcular $n_2$ del SiN, pero
  justifica la respuesta instantánea que se asume en la NLSE. La saturación (6.1.2)/(6.3.28) y la absorción de dos fotones no están en
  este modelo de un solo fotón resonante; para el Si, la TPA y la absorción por portadores libres son otros mecanismos (ver caps. 4 y 12).
  El §6.6 (bandas laterales de Rabi, ganancia en mezcla de cuatro ondas hacia adelante, luz lenta) es conceptualmente útil para entender
  la inestabilidad modulacional y la ruptura del haz (cap. 7.1, "laser beam breakup" por FWM hacia adelante), aunque en el proyecto el
  medio es no resonante.

## Erratas y dudas de lectura (resumen)

1. (6.2.10b,c), p. 280: signo del término de interacción invertido; lo correcto es lo de (6.2.13b,c) (comprobado con (6.2.9)).
2. p. 289: la reducción de $\chi''$ en el centro de línea es por $(1+\Omega^2T_1T_2)$, no por su raíz.
3. p. 291: "$3\chi^{(3)}|E^2|$" debe ser $3\chi^{(3)}|E|^2$ (tipográfica).
4. (6.3.37), p. 292: falta $1/\epsilon_0$.
5. (6.3.40), p. 293: $I_s^0=52.7$ W/m² no se reproduce (da ≈64–72 W/m² con los datos del texto); $\Omega$ y $\chi^{(3)}$ sí cuadran.
6. p. 296: "introduced into Eq. (6.4.5b)" → (6.4.5a).
7. (6.4.37), p. 301: "$n\mu_{ab}$" → $N\mu_{ab}$.
8. (6.5.3), p. 302: falta el signo menos, $\hat V=-\hat\mu\tilde E$.
9. (6.5.23), p. 305: el segundo coeficiente de la primera línea es $(\Omega'-\Delta)/2\Omega'$.
10. (6.5.32), p. 307: "$2\omega'$" → $2\Omega'$.
11. Pie de la Fig. 6.5.3, p. 308: remite a (6.5.28)–(6.5.29); por contenido, (6.5.23)–(6.5.24).
12. (6.5.42), p. 309: debe ser $(\Omega'\mp\Delta)/2\Omega'$.
13. (6.5.47a), p. 311: exponente $-i(\omega_b+\Delta)t$ (falta el signo menos).
14. (6.6.11), p. 317: denominador $(\Delta+\delta)+i/T_2$.
15. (6.6.19), p. 318: "$w_0^2$" sin factor 2 no es consistente con (6.6.21) ($2w_0$), que es la forma correcta.
16. (6.6.39a,b), p. 323: signos de $\alpha_{\pm1}$ y $\kappa_{\pm1}$ aparentemente invertidos respecto de la convención de Boyd (duda, no confirmada).
17. p. 326: "ac= Stark effect" (tipográfica).
