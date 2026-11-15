# Capítulo 13 — Ultrafast and Intense-Field Nonlinear Optics (Boyd, 3.ª ed.)

Páginas del libro 561–587 (PDF 579–605; la p. 588 / PDF 606 está en blanco). Leído el 2026-11-14.

Fuente: R. W. Boyd, *Nonlinear Optics*, 3.ª ed., Academic Press/Elsevier, 2008, cap. 13.
Las citas de página son páginas del libro (sumar 18 para la página del PDF).

Convención del libro (SI): $\tilde E(t)=Ee^{-i\omega t}+\text{c.c.}$, $I=2n\epsilon_0c|E|^2$. **Atención:** este
capítulo es el que peor se convirtió de gaussiano a SI en la 3.ª ed.; quedan varios factores
$4\pi$, $48\pi^2$, etc. (marcados abajo como erratas), y la §13.8 está explícitamente en unidades
gaussianas.

---

## Resumen del capítulo

El capítulo tiene dos mitades. La primera (13.1–13.3) trata la propagación de **pulsos
ultracortos** en un medio no lineal y dispersivo: partiendo de la ecuación de onda en el dominio de
la frecuencia se deriva una ecuación para la envolvente lentamente variable que generaliza la
ecuación de Schrödinger no lineal (NLSE) de §7.5 e incluye dispersión de orden superior (operador
$\tilde D$), acoplamiento espacio‑tiempo (operador $[1+(i/\omega_0)\partial/\partial\tau]^{-1}$ sobre $\nabla_\perp^2$) y
autoempinamiento (*self‑steepening*, el mismo operador sobre la fuente no lineal), en la forma de
Brabec y Krausz (1997); también la dispersión de $\chi^{(3)}$. Luego se interpreta: longitudes
características de difracción, dispersión y no linealidad ($L_{\rm dif}$, $L_{\rm dis}$, $L_{\rm NL}$), índice de
grupo dependiente de la intensidad $n_2^{(g)}$ que produce autoempinamiento y ondas de choque ópticas
($L_{\rm ss}$), acoplamiento espacio‑tiempo y una breve sección de **generación de supercontinuo** (Alfano y
Shapiro 1970). La segunda mitad (13.4–13.8) trata la óptica no lineal de **campos intensos**, donde la
serie de potencias en $E$ deja de converger: campo atómico $E_{\rm at}$, electrón libre en un campo láser
(energía ponderomotriz, figura en 8, parámetro $a$), generación de armónicos altos (modelo de tres
pasos de Corkum, corte $\hbar\omega q_{\max}=3.17K+I_P$), plasmas (frecuencia de plasma, autoenfoque
relativista, $n_2$ relativista, $P_{\rm cr}$) y electrodinámica cuántica no lineal (campo de Schwinger
$E_{\rm QED}$, lagrangiano de Euler–Kockel/Heisenberg, $\chi^{(3)}$ del vacío).

---

## Secciones

### 13.1 Introduction (p. 561)

Se generan ya pulsos del orden de 1 attosegundo. Dos razones de interés en ONL: (1) la naturaleza de
las interacciones no lineales cambia profundamente con pulsos ultracortos (secciones 13.2–13.3);
(2) los pulsos cortos tienen potencias pico muy altas, porque la energía por pulso la fija la
capacidad de almacenamiento del medio de ganancia (segunda mitad del capítulo).

### 13.2 Ultrashort Pulse Propagation Equation (p. 561)

Procesos incluidos: autoempinamiento con formación de choque óptico, dispersión de orden superior y
acoplamiento espacio‑tiempo. Ecuación de onda en el dominio del tiempo (ver (2.1.15)):

$$-\nabla^2\tilde E+\frac1{c^2}\frac{\partial^2\tilde D^{(1)}}{\partial t^2}=-\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde P}{\partial t^2}. \qquad (13.2.1),\ \text{p. 562}$$

Transformadas de Fourier (integrales de $-\infty$ a $\infty$):

$$\tilde E(\mathbf r,t)=\int E(\mathbf r,\omega)e^{-i\omega t}d\omega/2\pi,\quad \tilde D^{(1)}(\mathbf r,t)=\int D^{(1)}(\mathbf r,\omega)e^{-i\omega t}d\omega/2\pi,\quad \tilde P(\mathbf r,t)=\int P(\mathbf r,\omega)e^{-i\omega t}d\omega/2\pi \qquad (13.2.2\text{a–c})$$

$$D^{(1)}(\mathbf r,\omega)=\epsilon_0\epsilon^{(1)}(\omega)E(\mathbf r,\omega), \qquad (13.2.3)$$

($\tilde P$ es solo la parte no lineal). Ecuación de onda en frecuencia:

$$\nabla^2E(\mathbf r,\omega)+\epsilon^{(1)}(\omega)(\omega^2/c^2)E(\mathbf r,\omega)=-(\omega^2/\epsilon_0c^2)P(\mathbf r,\omega). \qquad (13.2.4)$$

(**Errata menor:** se lee "$\epsilon_0\epsilon^{(1)}(\omega)(\omega^2/c^2)$" en el 2.º término. Hay una inconsistencia dimensional
heredada: en (13.2.1) el término de $\tilde D^{(1)}$ debería ser $\frac{1}{\epsilon_0c^2}\partial_t^2\tilde D^{(1)}$ ($=\mu_0\partial_t^2\tilde D^{(1)}$); hecho eso, el
$\epsilon_0$ desaparece de (13.2.4), consistente con $k^2=\epsilon(\omega)\omega^2/c^2$ de (13.2.9).)

Envolvente lentamente variable, con $\omega_0$ = portadora y $k_0$ = parte lineal del vector de onda en
$\omega_0$:

$$\tilde E(\mathbf r,t)=\tilde A(\mathbf r,t)e^{i(k_0z-\omega_0t)}+\text{c.c.}, \qquad (13.2.5)$$

$$\tilde A(\mathbf r,t)=\int A(\mathbf r,\omega)e^{-i\omega t}d\omega/2\pi, \qquad (13.2.6)$$

$$E(\mathbf r,\omega)\simeq A(\mathbf r,\omega-\omega_0)e^{ik_0z}\quad\text{(como en (7.5.16))}. \qquad (13.2.7)$$

En términos de $A(\mathbf r,\omega)$ (p. 563):

$$\nabla_\perp^2A+\frac{\partial^2A}{\partial z^2}+2ik_0\frac{\partial A}{\partial z}+[k^2(\omega)-k_0^2]A=-\frac{\omega^2}{\epsilon_0c^2}P(\mathbf r,\omega)e^{-ik_0z}, \qquad (13.2.8)$$

$$k^2(\omega)=\epsilon(\omega)(\omega^2/c^2). \qquad (13.2.9)$$

Expansión de $k(\omega)$:

$$k(\omega)=k_0+k_1(\omega-\omega_0)+D,\qquad D=\sum_{n=2}^\infty\frac1{n!}k_n(\omega-\omega_0)^n, \qquad (13.2.10)$$

$$k^2(\omega)=k_0^2+2k_0k_1(\omega-\omega_0)+2k_0D+2k_1D(\omega-\omega_0)+k_1^2(\omega-\omega_0)^2+D^2. \qquad (13.2.11)$$

$D$ = dispersión de orden alto; $k_1=1/v_g$. Sustituyendo en (13.2.8) y despreciando $D^2$ ("invariablemente
pequeño"):

$$\nabla_\perp^2A+\frac{\partial^2A}{\partial z^2}+2ik_0\frac{\partial A}{\partial z}+2k_0k_1(\omega-\omega_0)A+2k_0DA+2k_1D(\omega-\omega_0)A+k_1^2(\omega-\omega_0)^2A=-(\omega^2/\epsilon_0c^2)P(z,\omega)e^{-ik_0z}. \qquad (13.2.12)$$

(**Errata:** en el libro el lado derecho de (13.2.12) aparece **sin** el signo menos; por consistencia
con (13.2.8) y (13.2.13) debe llevarlo.)

Volviendo al dominio del tiempo (multiplicar por $e^{-i(\omega-\omega_0)t}$ e integrar sobre $\omega-\omega_0$, con
$(\omega-\omega_0)\to i\partial/\partial t$):

$$\left[\nabla_\perp^2+\frac{\partial^2}{\partial z^2}+2ik_0\left(\frac{\partial}{\partial z}+k_1\frac{\partial}{\partial t}\right)+2ik_1\tilde D\frac{\partial}{\partial t}+2k_0\tilde D-k_1^2\frac{\partial^2}{\partial t^2}\right]\tilde A(\mathbf r,t)=\frac1{\epsilon_0c^2}\frac{\partial^2\tilde P}{\partial t^2}e^{-i(k_0z-\omega_0t)}, \qquad (13.2.13)$$

$$\tilde D=\sum_{n=2}^\infty\frac1{n!}k_n\left(i\frac{\partial}{\partial t}\right)^n=-\frac12k_2\frac{\partial^2}{\partial t^2}+\cdots \qquad (13.2.14)$$

(**Erratas:** en (13.2.13) el último término se lee $-k_1\,\partial^2/\partial t^2$; debe ser $-k_1^2\,\partial^2/\partial t^2$, como
en (13.2.18). En (13.2.14) se lee $1/n$; por (13.2.10) debe ser $1/n!$ (no cambia el término $n=2$).)

Polarización con envolvente lenta (p. 564):

$$\tilde P(\mathbf r,t)=\tilde p(\mathbf r,t)e^{i(k_0z-\omega_0t)}+\text{c.c.}, \qquad (13.2.15)$$

y para respuesta de tercer orden instantánea

$$\tilde p(\mathbf r,t)=3\epsilon_0\chi^{(3)}|\tilde A(\mathbf r,t)|^2\tilde A(\mathbf r,t). \qquad (13.2.16)$$

$$\frac{\partial\tilde P}{\partial t}=\left(-i\omega_0\tilde p+\frac{\partial\tilde p}{\partial t}\right)e^{i(k_0z-\omega_0t)}+\text{c.c.}=-i\omega_0\left[\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial t}\right)\tilde p\right]e^{i(k_0z-\omega_0t)}+\text{c.c.}, \qquad (13.2.17\text{a})$$

$$\frac{\partial^2\tilde P}{\partial t^2}=-\omega_0^2\left[\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial t}\right)^2\tilde p\right]e^{i(k_0z-\omega_0t)}+\text{c.c.} \qquad (13.2.17\text{b})$$

En (13.2.13):

$$\left[\nabla_\perp^2+\frac{\partial^2}{\partial z^2}+2ik_0\left(\frac{\partial}{\partial z}+k_1\frac{\partial}{\partial t}\right)+2k_0\tilde D+2ik_1\tilde D\frac{\partial}{\partial t}-k_1^2\frac{\partial^2}{\partial t^2}\right]\tilde A=-\frac{\omega_0^2}{\epsilon_0c^2}\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial t}\right)^2\tilde p. \qquad (13.2.18)$$

(**Errata (resto gaussiano):** el libro escribe el prefactor del lado derecho como $-4\pi\omega_0^2/c^2$; en SI es
$-\omega_0^2/\epsilon_0c^2$, como en (13.2.21) en adelante.)

Tiempo retardado:

$$z'=z,\qquad \tau=t-\frac{1}{v_g}z=t-k_1z, \qquad (13.2.19)$$

$$\frac{\partial}{\partial z}=\frac{\partial}{\partial z'}-k_1\frac{\partial}{\partial\tau},\qquad \frac{\partial}{\partial t}=\frac{\partial}{\partial\tau}. \qquad (13.2.20)$$

Resulta (p. 565):

$$\left[\nabla_\perp^2+\frac{\partial^2}{\partial z'^2}-2k_1\frac{\partial}{\partial z'}\frac{\partial}{\partial\tau}+k_1^2\frac{\partial^2}{\partial\tau^2}+2ik_0\left(\frac{\partial}{\partial z'}-k_1\frac{\partial}{\partial\tau}+k_1\frac{\partial}{\partial\tau}\right)+2k_0\tilde D+2ik_1\tilde D\frac{\partial}{\partial\tau}-k_1^2\frac{\partial^2}{\partial\tau^2}\right]\tilde A=-\frac{\omega_0^2}{\epsilon_0c^2}\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right)^2\tilde p. \qquad (13.2.21)$$

Aproximación de amplitud lentamente variable (se elimina $\partial^2/\partial z'^2$):

$$\left[\nabla_\perp^2-2k_1\frac{\partial}{\partial z'}\frac{\partial}{\partial\tau}+2ik_0\frac{\partial}{\partial z'}+2k_0\tilde D+2ik_1\tilde D\frac{\partial}{\partial\tau}\right]\tilde A=-\frac{\omega_0^2}{\epsilon_0c^2}\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right)^2\tilde p, \qquad (13.2.22)$$

o bien

$$\left[\nabla_\perp^2+2ik_0\frac{\partial}{\partial z'}\left(1+\frac{ik_1}{k_0}\frac{\partial}{\partial\tau}\right)+2k_0\tilde D\left(1+\frac{ik_1}{k_0}\frac{\partial}{\partial\tau}\right)\right]\tilde A=-\frac{\omega_0^2}{\epsilon_0c^2}\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right)^2\tilde p. \qquad (13.2.23)$$

(**Errata:** en el lado derecho de (13.2.23) el libro omite la $i$: se lee $(1+\frac{1}{\omega_0}\frac{\partial}{\partial\tau})^2$; verificado a 200
dpi; debe ser $(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau})^2$ como en (13.2.22) y (13.2.24).)

Razón $k_1/k_0=v_g^{-1}/(n\omega_0/c)=n_g/(n\omega_0)$; sin dispersión $n_g=n$ y $k_1/k_0=1/\omega_0$:

$$\left[\nabla_\perp^2+2ik_0\frac{\partial}{\partial z'}\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right)+2k_0\tilde D\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right)\right]\tilde A=-\frac{\omega_0^2}{\epsilon_0c^2}\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right)^2\tilde p, \qquad (13.2.24)$$

$$\left[\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right)^{-1}\nabla_\perp^2+2ik_0\frac{\partial}{\partial z'}+2k_0\tilde D\right]\tilde A=-\frac{\omega_0^2}{\epsilon_0c^2}\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right)\tilde p. \qquad (13.2.25)$$

(13.2.25) generaliza la NLSE: incluye dispersión de orden superior ($\tilde D$), acoplamiento
espacio‑tiempo (operador del lado izquierdo) y autoempinamiento (operador del lado derecho). Es la
forma de **Brabec y Krausz (1997)** (p. 566). Sirve para muchas no linealidades, p. ej. tercer y quinto
orden instantáneos: $\tilde p=3\epsilon_0\chi^{(3)}|\tilde A|^2\tilde A+10\epsilon_0\chi^{(5)}|\tilde A|^4\tilde A$.

**Dispersión de $\chi^{(3)}$** (aproximación más baja; Diels y Rudolph, 1996, p. 139), con
$\chi^{(3)}(\omega)\equiv\chi^{(3)}(\omega=\omega+\omega-\omega)$:

$$\chi^{(3)}(\omega)=\chi^{(3)}(\omega_0)+(\omega-\omega_0)\frac{d\chi^{(3)}}{d\omega}, \qquad (13.2.26)$$

$$p(\omega)=3\epsilon_0\left[\chi^{(3)}(\omega_0)+(\omega-\omega_0)\frac{d\chi^{(3)}}{d\omega}\right]|A(\omega)|^2A(\omega), \qquad (13.2.27)$$

$$\tilde p(\tau)=3\epsilon_0\left[\chi^{(3)}(\omega_0)+\frac{d\chi^{(3)}}{d\omega}i\frac{\partial}{\partial\tau}\right]|\tilde A|^2\tilde A. \qquad (13.2.28)$$

Por consistencia se conservan solo términos de primer orden en $\partial/\partial\tau$:

$$\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right)^2=\left(1+\frac{2i}{\omega_0}\frac{\partial}{\partial\tau}-\frac1{\omega_0^2}\frac{\partial^2}{\partial\tau^2}\right)\approx\left(1+\frac{2i}{\omega_0}\frac{\partial}{\partial\tau}\right), \qquad (13.2.29)$$

y la ecuación queda (p. 567)

$$\left[\nabla_\perp^2+2ik_0\frac{\partial}{\partial z'}\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right)+2k_0\tilde D\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right)\right]\tilde A=(-3/c^2)\omega_0^2\chi^{(3)}(\omega_0)\left[1+\left(2+\frac{\omega_0}{\chi^{(3)}(\omega_0)}\frac{d\chi^{(3)}}{d\omega}\right)\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right]|\tilde A|^2\tilde A. \qquad (13.2.30)$$

(En el libro los corchetes del lado izquierdo de (13.2.30) están mal colocados — "$\nabla_\perp^2+2ik_0\frac{\partial}{\partial z'}[(1+\dots)+2k_0\tilde D(\dots)]$" —; aquí
se escribe como en (13.2.24).) Otras no linealidades: Gaeta (2000).

### 13.3 Interpretation of the Ultrashort-Pulse Propagation Equation (p. 567)

Versión simplificada de (13.2.24): factores $[1+(i/\omega_0)\partial/\partial\tau]\to1$ y solo dispersión de segundo
orden en $\tilde D$:

$$\frac{\partial A(\mathbf r,t)}{\partial z'}=\left[\frac{i}{2k_0}\nabla_\perp^2-\frac{i}{2}k_2\frac{\partial^2}{\partial\tau^2}+\frac{3i\omega_0}{2n_0c}\chi^{(3)}(\omega_0)|\tilde A|^2\right]\tilde A. \qquad (13.3.1)$$

Tres efectos: difracción (laplaciano transverso), ensanchamiento temporal por GVD (segunda derivada
temporal) y adquisición no lineal de fase. Longitudes características:

$$L_{\rm dif}=\tfrac12k_0w_0^2\quad\text{(difracción)}, \qquad (13.3.2\text{a})$$

$$L_{\rm dis}=T^2/|k_2|\quad\text{(dispersión)}, \qquad (13.3.2\text{b})$$

$$L_{\rm NL}=\frac{2n_0c}{3\omega_0\chi^{(3)}|A|^2}=\frac{1}{(\omega_0/c)n_2I}\quad\text{(no lineal)}. \qquad (13.3.2\text{c})$$

$w_0$ = radio característico del haz, $T$ = duración característica del pulso; domina el proceso con
la menor longitud (p. 568). **Ejemplo:** sílice fundida a 800 nm, $n_2=3.5\times10^{-20}$ m²/W y
$k_2=446$ fs²/cm; para un pulso de 20 fs, $L_{\rm dis}\approx0.9$ cm, es decir, el pulso aproximadamente
duplica su duración en 0.9 cm de sílice. ($20^2/446=0.90$ cm ✓.)

#### 13.3.1 Self-Steepening (p. 568)

Se aísla el factor $[1+(i/\omega_0)\partial/\partial\tau]$ en la fuente no lineal, usando (13.2.30) (no linealidad
dispersiva) y volviendo al marco de laboratorio $z,t$, donde aparece $k_1\partial\tilde A/\partial t=(1/v_g)\partial\tilde A/\partial t=(n_0^{(g)}/c)\partial\tilde A/\partial t$:

$$\frac{\partial\tilde A}{\partial z}-\frac{n_0^{(g)}}{c}\frac{\partial\tilde A}{\partial t}=\frac{i}{2k_0}\nabla_\perp^2\tilde A-\frac{i}{2}k_2\frac{\partial^2\tilde A}{\partial t^2}+\frac{3i\omega_0}{2n_0c}\chi^{(3)}(\omega_0)|\tilde A|^2\tilde A+\frac{i3\omega_0}{2n_0c}\chi^{(3)}(\omega_0)\left(2+\frac{\omega_0}{\chi^{(3)}(\omega_0)}\frac{d\chi^{(3)}}{d\omega}\right)\frac{i}{\omega_0}\frac{\partial}{\partial t}|\tilde A|^2A. \qquad (13.3.3)$$

(**Erratas:** (i) el libro escribe el término de Kerr como $\frac{i6\pi\omega_0}{n_0c}\chi^{(3)}$ — resto gaussiano —; en SI es
$\frac{3i\omega_0}{2n_0c}\chi^{(3)}$, como en (13.3.1) y en $\gamma_1$ de (13.3.4). (ii) El signo del 2.º término del lado
izquierdo se lee "$-$" aquí y en (13.3.5), (13.3.7); por (13.2.20) ($\partial/\partial z'=\partial/\partial z+k_1\partial/\partial t$) debería ser
"$+$". Se transcribe tal cual el libro.)

Coeficientes no lineales:

$$\gamma_1=\frac{3\omega_0}{2n_0c}\chi^{(3)}(\omega_0),\qquad \gamma_2=\frac{3\omega_0}{2n_0c}\chi^{(3)}(\omega_0)\left(1+\frac12\frac{\omega_0}{\chi^{(3)}}\frac{d\chi^{(3)}}{d\omega}\right). \qquad (13.3.4)$$

Sin dispersión, $\gamma_1=\gamma_2$. Forma compacta:

$$\frac{\partial\tilde A}{\partial z}-\frac{n_0^{(g)}}{c}\frac{\partial\tilde A}{\partial t}=\frac{i}{2k_0}\nabla_\perp^2\tilde A-\frac{i}{2}k_2\frac{\partial^2\tilde A}{\partial t^2}+i\gamma_1|A|^2A-2\gamma_2\frac{1}{\omega_0}\frac{\partial}{\partial t}(|\tilde A|^2A). \qquad (13.3.5)$$

$$\frac{\partial}{\partial t}(|\tilde A|^2\tilde A)=\frac{\partial}{\partial t}(\tilde A^2\tilde A^*)=\tilde A^2\frac{\partial\tilde A^*}{\partial t}+2\tilde A^*\tilde A\frac{\partial\tilde A}{\partial t}=2|\tilde A|^2\frac{\partial\tilde A}{\partial t}+\tilde A^2\frac{\partial\tilde A^*}{\partial t}. \qquad (13.3.6)$$

El primer término es una contribución dependiente de la intensidad a la velocidad de grupo; el
segundo no tiene interpretación simple: término de mezcla de cuatro ondas dispersivo (p. 569):

$$\frac{\partial\tilde A}{\partial z}-\frac{n_{\rm eff}^{(g)}}{c}\frac{\partial\tilde A}{\partial t}=\frac{i}{2k_0}\nabla_\perp^2\tilde A-\frac{i}{2}k_2\frac{\partial^2\tilde A}{\partial t^2}+i\gamma_1|A|^2A-\frac{2\gamma_2}{\omega_0}\tilde A^2\frac{\partial\tilde A^*}{\partial t}, \qquad (13.3.7)$$

$$n_{\rm eff}^{(g)}=n_0^{(g)}+\frac{4\gamma_2c}{\omega_0}|\tilde A|^2\equiv n_0^{(g)}+n_2^{(g)}I, \qquad (13.3.8)$$

$$n_2^{(g)}=\frac{48\pi^2}{n_0^2c}\chi^{(3)}(\omega_0)\left[1+\frac12\frac{\omega_0}{\chi^{(3)}(\omega_0)}\frac{d\chi^{(3)}}{d\omega}\right]\quad\text{(tal como está impreso)}. \qquad (13.3.9)$$

(**Errata (resto gaussiano) en (13.3.9):** con (13.3.8), (13.3.4) e $I=2n_0\epsilon_0c|A|^2$ se obtiene en SI
$n_2^{(g)}=\dfrac{3}{n_0^2\epsilon_0c}\chi^{(3)}(\omega_0)\left[1+\tfrac12\tfrac{\omega_0}{\chi^{(3)}}\tfrac{d\chi^{(3)}}{d\omega}\right]=4n_2\left[1+\dots\right]$, con $n_2=3\chi^{(3)}/4n_0^2\epsilon_0c$
(el $48\pi^2/n_0^2c$ es $4\times$ el $12\pi^2/n_0^2c$ gaussiano). Esto choca con la afirmación de p. 570 de que
normalmente $n_2^{(g)}\approx n_2$; el factor 4 viene de haber conservado $(1+\tfrac{i}{\omega_0}\partial_\tau)^2$ en la
fuente en vez de una sola potencia como en (13.2.25). Duda abierta; no se corrige.)

La intensidad modifica el índice de grupo, que depende de la susceptibilidad y de su dispersión. Con
$n_2^{(g)}>0$ (caso usual) el pico del pulso se frena más que los flancos → se empina el **flanco
posterior** (autoempinamiento); si se vuelve infinitamente abrupto se forma una **onda de choque
óptica**. **Fig. 13.3.1**: (a) pulso gaussiano incidente, (b) autoempinamiento del flanco posterior,
(c) choque. Referencias: DeMartini *et al.* (1967), Yang y Shen (1984), Gaeta (2000). Longitud de
autoempinamiento (p. 570):

$$L_{\rm ss}=\frac{cT}{n_2^{(g)}I}. \qquad (13.3.10)$$

Con $n_2^{(g)}\approx n_2$, $L_{\rm ss}\gg L_{\rm NL}$ (salvo pulsos extremadamente cortos, $cT\gg1/k_0$), así que el
autoempinamiento es difícil de observar. ($L_{\rm ss}/L_{\rm NL}=\omega_0T\cdot n_2/n_2^{(g)}$.)

#### 13.3.2 Space-Time Coupling (p. 570)

Influencia de $[1+(i/\omega_0)\partial/\partial\tau]^{-1}$ en el lado izquierdo de (13.2.25), en un medio lineal y sin
dispersión:

$$\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right)^{-1}\nabla_\perp^2\tilde A+2ik_0\frac{\partial}{\partial z'}\tilde A=0, \qquad (13.3.11)$$

$$\nabla_\perp^2\tilde A+\left(1+\frac{i}{\omega_0}\frac{\partial}{\partial\tau}\right)2ik_0\frac{\partial}{\partial z'}\tilde A=0. \qquad (13.3.12)$$

Ejemplo artificial $\tilde A=a(\mathbf r)e^{-i\delta\omega t}$ (campo monocromático a $\omega_0+\delta\omega$):

$$\nabla_\perp^2a+\left(1+\frac{\delta\omega}{\omega_0}\right)2ik_0\frac{\partial a}{\partial z'}=0, \qquad (13.3.13)$$

$$\nabla_\perp^2a+2i(k_0+\delta k)\frac{\partial a}{\partial z'}=0,\qquad \delta k=k_0(\delta\omega/\omega_0). \qquad (13.3.14)$$

La onda difracta como una de frecuencia $\omega_0+\delta\omega$: en un pulso ultracorto cada componente
espectral difracta con distinto ángulo de cono y tras propagarse tiene distinta dependencia radial
(p. 571). Implicaciones para autoenfoque: Rothenberg (1992).

#### 13.3.3 Supercontinuum Generation (p. 571)

Un pulso corto e intenso sufre gran ensanchamiento espectral; observado por primera vez por
**Alfano y Shapiro (1970)**. Ejemplo: Fork *et al.* (1983), pulso de 80 fs, intensidad pico
$\sim10^{14}$ W/cm², 0.5 mm de etilenglicol → espectro de $0.4\omega_0$ a $3.3\omega_0$. También en gases (Corkum *et
al.*, 1986). Según el libro, el mecanismo físico parece ser el **autoempinamiento** (Yang y Shen,
1984) que lleva a la formación de choque óptico (Gaeta, 2000).

### 13.4 Intense-Field Nonlinear Optics (p. 571)

La mayoría de los fenómenos (excepción obvia: el fotorrefractivo, cap. 11) se describen con

$$\tilde P(t)=\chi^{(1)}\tilde E(t)+\chi^{(2)}\tilde E(t)^2+\chi^{(3)}\tilde E(t)^3+\cdots \qquad (13.4.1)$$

(**Errata (resto gaussiano):** falta el factor $\epsilon_0$ global de la convención SI del libro, (1.1.2).)
Para campos grandes la serie puede no converger: en resonancia, cuando la frecuencia de Rabi
$\Omega=\mu_{ba}E/\hbar$ es comparable a $1/T_1$ (cap. 6); incluso fuera de resonancia, cuando $E$ se acerca al
campo atómico

$$E_{\rm at}=\frac{e/4\pi\epsilon_0}{a_0^2}=\frac{e/4\pi\epsilon_0}{(4\pi\epsilon_0\hbar^2/me^2)^2}=6\times10^{11}\ \text{V/m}, \qquad (13.4.2)$$

(nota: en §12.4 el mismo campo se daba como $5\times10^{11}$ V/m; el valor exacto es $5.14\times10^{11}$ V/m), con
intensidad (tomando $E_{\rm at}$ como campo **pico** de una onda linealmente polarizada; p. 572)

$$I_{\rm at}=\tfrac12\epsilon_0cE_{\rm at}^2=4\times10^{16}\ \text{W/cm}^2=4\times10^{20}\ \text{W/m}^2. \qquad (13.4.3)$$

Hay láseres de más de $10^{20}$ W/cm² (Mourou *et al.*, 1998). Marco conceptual: el cálculo del cap. 3
supone

$$\hat H=\hat H_0+\hat V(t),\qquad \hat V(t)=-\mu\tilde E(t), \qquad (13.4.4)$$

con $V\ll H_0$; en campos intensos ocurre lo contrario, $V\gg H_0$, así que conviene empezar por el
electrón libre en un campo láser.

### 13.5 Motion of a Free Electron in a Laser Field (p. 572)

Sin efectos relativistas ni magnéticos; $\tilde{\mathbf E}(t)=\tilde E(t)\hat x$, $\tilde E(t)=Ee^{-i\omega t}+\text{c.c.}$:

$$m\ddot{\tilde x}=-e\tilde E(t)\quad\text{o}\quad m\ddot{\tilde x}=-eEe^{-i\omega t}+\text{c.c.}, \qquad (13.5.1)$$

$$\tilde x(t)=xe^{-i\omega t}+\text{c.c.}, \qquad (13.5.2)$$

$$x=eE/m\omega^2. \qquad (13.5.3)$$

Energía cinética promedio $K=\tfrac12m\langle\dot{\tilde x}^2\rangle$ (p. 573), con

$$\dot{\tilde x}(t)=(-i\omega x)e^{-i\omega t}+\text{c.c.}, \qquad (13.5.4)$$

(**errata menor:** el libro imprime $e^{i\omega t}$ en (13.5.4)), de donde

$$K=\frac{e^2E^2}{m\omega^2}=\frac{e^2E_{\rm peak}^2}{4m\omega^2}. \qquad (13.5.5)$$

Es la **energía de "jitter"** o **ponderomotriz** (Kibble, 1966). Ejemplo a $\lambda=1.06\ \mu$m: $K=13.6$ eV
(energía atómica típica) para $I=1.3\times10^{14}$ W/cm² $=1.3\times10^{18}$ W/m²; $K=4.2$ keV para $I=I_{\rm at}$; y $K=mc^2=500$
keV para $I=4.8\times10^{18}$ W/cm² $=4.8\times10^{22}$ W/m². (Coincide con la fórmula práctica
$U_p[\text{eV}]=9.33\times10^{-14}I[\text{W/cm}^2]\lambda^2[\mu\text{m}]$.)

Las ecuaciones (13.5.1)–(13.5.2) son lineales en el campo; la no linealidad aparece por efectos
**magnéticos** y **relativistas**. Magnético (ver problema 1): propagación en $z$, $\tilde{\mathbf B}=\tilde B\hat y$,
$\tilde B=Be^{i\omega t}+\text{c.c.}$, $B=E/c$ en vacío; fuerza $\mathbf F=\mathbf v\times\mathbf B$ en $z$:

$$m\ddot{\tilde z}=\left[\left(-\frac{ieE}{m\omega}\right)e^{-i\omega t}+\text{c.c.}\right]\left[Be^{-i\omega t}+\text{c.c.}\right]. \qquad (13.5.6)$$

(Inconsistencia menor: el texto escribe $Be^{i\omega t}$ y la ecuación $Be^{-i\omega t}$.) Términos a frecuencia cero
y $\pm2\omega$: el movimiento en $z$ es una oscilación a $2\omega$ de amplitud $eEB/m^2\omega^3$ superpuesta a una
deriva uniforme; esa velocidad produce fuerza magnética en $x$ a $3\omega$, y así aparecen todos los
armónicos (nota: generalización del problema 7 del cap. 4).

Relativista (p. 574): masa variable cuando $v\sim c$. Landau y Lifshitz (1960): para polarización
lineal de campo pico $E_0$, $\tilde E=E_0\cos(\omega t-\omega z/c)$, el electrón describe una **figura en 8**
superpuesta a una traslación uniforme en $z$. En el marco que se mueve con la velocidad de
traslación:

$$x=\frac{\beta c}{\omega}\cos\eta,\qquad y=0,\qquad z=\frac{\beta^2c}{8\omega}\sin2\eta, \qquad (13.5.7)$$

$$\eta=\omega(t-z/c), \qquad (13.5.8\text{a})$$
$$\beta=eE_0/\gamma'\omega, \qquad (13.5.8\text{b})$$
$$\gamma'^2=m^2c^2+e^2E_0^2/2\omega^2. \qquad (13.5.8\text{c})$$

Polarización circular, $E_y=E_0\cos(\omega t-\omega z/c)$, $E_x=E_0\sin(\omega t-\omega z/c)$: círculo de radio $ecE_0/\gamma\omega^2$
con velocidad angular uniforme:

$$x=\frac{\beta c}{\omega}\cos\omega t,\qquad y=\frac{\beta c}{\omega}\sin\omega t,\qquad z=0. \qquad (13.5.9)$$

**Fig. 13.5.1** (p. 575): (a) figura en 8 en el plano $xz$ (lineal); (b) círculo en el plano $xy$
(circular). Más detalle: Sarachik y Schappert (1970), Castillo‑Herrara y Johnston (1993).

Parámetro adimensional $a$ (potencial vector adimensional, invariante de Lorentz):

$$a^2=\frac{K}{mc^2}=\frac{e^2E^2}{m^2c^2\omega^2}, \qquad (13.5.10)$$

$$a^2=\frac2\pi\frac{Ir_0\lambda^2}{mc^3}, \qquad (13.5.11)$$

con $r_0=e^2/4\pi\epsilon_0mc^2$ (radio clásico del electrón), $\lambda=2\pi c/\omega$, $I=\tfrac12\epsilon_0cE^2$. $a^2\ll1$:
no relativista; $a^2\gtrsim1$: relativista; $a^2\gg1$: ultrarrelativista.

(**Duda de lectura:** (13.5.11) solo se sigue de $a^2=e^2E^2/m^2c^2\omega^2$ si $E$ es el campo **pico** (porque
$I=\tfrac12\epsilon_0cE^2$); pero entonces $a^2\neq K/mc^2$, ya que por (13.5.5) $K=e^2E_{\rm peak}^2/4m\omega^2$. Con $E$ =
amplitud compleja, (13.5.10) es correcta y (13.5.11) sería $a^2=Ir_0\lambda^2/(2\pi mc^3)$. Hay un factor 4 de
ambigüedad entre las dos igualdades.)

### 13.6 High-Harmonic Generation (p. 575)

Un haz intenso (en el sentido de $K\gg I_P$, potencial de ionización) sobre un medio atómico emite en
la dirección de avance **todos los armónicos impares** $q\omega$ hasta un orden de corte $q_{\max}$, la
mayoría con eficiencia comparable → **no es perturbativo** (no es un proceso $\chi^{(q)}$, que daría
eficiencias decrecientes). Se han observado órdenes $q=221$ (Chang *et al.*, 1999). Intensidades
típicas $10^{14}$–$10^{16}$ W/cm².

**Modelo de Corkum (1993):** el campo ioniza el átomo; aunque $K\gg I_P$, la oscilación devuelve el
electrón al núcleo una vez por periodo; por el potencial $1/r^2$ solo siente fuerza apreciable (y
radia, campo ∝ aceleración) cerca del núcleo → cada electrón emite un tren de pulsos separados por
un periodo. En el conjunto, la mitad de los electrones sale cerca del máximo positivo y la otra mitad
cerca del negativo → pulsos separados por **medio periodo**, mutuamente coherentes; el espectro es
la TF del tren: componentes separadas por $2\omega$ → solo armónicos impares, consistente con la
simetría de medios centrosimétricos (§1.5). **Fig. 13.6.1** (p. 576): (a) trayectoria del electrón
tras la ionización; (b) campo radiado, pulsos separados $\pi/\omega$; (c) espectro $S(\omega)$ con picos
separados $2\omega_L$ hasta $q_{\max}\omega_L$.

**Corte** (p. 577; **Fig. 13.6.2**): la energía disponible es la cinética más el potencial de
ionización; ingenuamente $q_{\max}\hbar\omega=K+I_P$, pero cálculos detallados dan coeficiente 3.17:

$$q_{\max}\hbar\omega=3.17K+I_P. \qquad (13.6.1)$$

Buen acuerdo con los datos.

Historia: Agostini *et al.* (1979), **ionización por encima del umbral (ATI)**: varios picos en el
espectro de fotoelectrones separados por $\hbar\omega$ (la teoría perturbativa de orden más bajo predecía
uno solo). Doble ionización (Walker *et al.*, 1994). Ferray *et al.* (1988): hasta el armónico 33 con
$10^{13}$ W/cm² en Ar, Kr y Xe (**Fig. 13.6.3**, p. 578: intensidad relativa de armónicos, $1$ para $q=1$,
$\sim3\times10^{-4}$ para $q=3$… meseta $\sim10^{-5}$ entre $q\approx7$ y 27, caída hasta $\sim10^{-7}$ en $q\approx33$; el eje
dice "Realtive", errata tipográfica). Kulander y Shore (1989): primeros modelos numéricos exitosos.
L'Huillier y Balcou (1993): pulsos de 1 ps, $10^{15}$ W/cm², hasta el armónico 135 en Ne. Corkum (1993):
modelo descrito; casi a la vez Schafer *et al.* (1993). Lewenstein *et al.* (1994): teoría cuántica
completa. Chang *et al.* (1997): He con pulsos de 26 fs de Ti:zafiro a 800 nm; picos hasta el orden 221
y estructura no resuelta hasta 460 eV (2.7 nm, orden 297). Schnürer *et al.* (1998): $\lambda=2.5$ nm,
$h\nu=500$ eV. Durfee *et al.* (1999): ajuste de fase de HHG en guía capilar llena de gas.

### 13.7 Nonlinear Optics of Plasmas and Relativistic Nonlinear Optics (p. 579)

Plasma = gas parcial o totalmente ionizado. Dos papeles: (1) procesos no lineales (ionización
multifotónica) crean plasma, cuyo índice lineal modifica la propagación; (2) el plasma responde de
forma intrínsecamente no lineal.

Formación ($N_e$ electrones, $N_i$ iones, $N_T$ átomos totales por unidad de volumen):

$$\frac{dN_e}{dt}=\frac{dN_i}{dt}=(N_T-N_i)\sigma^{(N)}I^N-rN_eN_i, \qquad (13.7.1)$$

$\sigma^{(N)}$ = sección eficaz de $N$ fotones (§12.5), $r$ = tasa de recombinación (despreciable en pulsos
cortos; $N_e$ crece monótonamente durante el pulso).

Óptica lineal del plasma: con (13.5.2)–(13.5.3), $\tilde p(t)=pe^{-i\omega t}+\text{c.c.}=-e\tilde x(t)$, y $p=\epsilon_0\alpha(\omega)E$:

$$\alpha(\omega)=-\frac{e^2}{\epsilon_0m\omega^2}, \qquad (13.7.2)$$

$$\epsilon=1+N\alpha(\omega)=1-\frac{Ne^2}{\epsilon_0m\omega^2}, \qquad (13.7.3)$$

$$\epsilon=1-\frac{\omega_p^2}{\omega^2},\qquad \omega_p^2=\frac{Ne^2}{\epsilon_0m}\ \text{(frecuencia de plasma)}. \qquad (13.7.4)$$

Plasma subdenso ($\omega_p^2<\omega^2$): $\epsilon>0$, $n=\sqrt\epsilon$ real, hay propagación. Sobredenso ($\omega_p^2>\omega^2$): $\epsilon<0$,
$n$ imaginario, no hay propagación (p. 580). Comparación con electrón ligado (ver (1.4.17), con
$\chi^{(1)}(\omega)=N\epsilon_0\alpha(\omega)$ — **duda:** con $p=\epsilon_0\alpha E$ debería ser $\chi^{(1)}=N\alpha$, como en (13.7.3)):

$$\alpha(\omega)=\frac{e^2/m\epsilon_0}{\omega_0^2-\omega^2-2i\omega\gamma}, \qquad (13.7.5)$$

$$\alpha_{\rm bound}=\frac{e^2}{\epsilon_0m\omega_0^2}\quad(\omega\ll\omega_0). \qquad (13.7.6)$$

El electrón libre tiene polarizabilidad de signo opuesto y (para $\omega\ll\omega_0$) mucho mayor → la
formación de plasma da una contribución **negativa** grande al índice. La contribución iónica es
despreciable (masa grande).

Mecanismos no lineales en plasmas: (1) **ponderomotrices**: las cargas son expulsadas de las regiones
de campo alto; importantes solo para pulsos largos (hay tiempo de movimiento); mismo origen que la
electrostricción (§9.2). Aunque $\alpha<0$ para el electrón libre y $>0$ en materia, ambos aumentan el
índice (en el plasma, al expulsar electrones que aportan índice negativo). (2) **Relativistas**
(Wagner *et al.*, 1997): para $I\gtrsim10^{18}$ W/cm² un electrón alcanza velocidades relativistas en medio
periodo; igualando $K$ a $mc^2$, o intuitivamente con el campo (p. 581)

$$E_{\rm rel}=2mc^2/\lambda e, \qquad (13.7.7)$$

(en medio periodo una partícula relativista recorre $\lambda/2$), con $I=\tfrac12\epsilon_0cE_{\rm rel}^2\sim10^{18}$ W/cm².

Aun con $v\ll c$, el cambio de masa $m\to\gamma m$,

$$\gamma=\frac1{\sqrt{1-v^2/c^2}}, \qquad (13.7.8)$$

modifica la frecuencia de plasma y el índice:

$$n^2=1-\frac{\omega_p^2}{\gamma\omega^2}, \qquad (13.7.9)$$

con, en general (Max *et al.*, 1974; Sprangle *et al.*, 1987), suponiendo velocidad transversal ≫
longitudinal y $E_0$ = amplitud pico:

$$\gamma^2=1+\frac{e^2E_0^2}{m^2\omega^2c^2}. \qquad (13.7.10)$$

(Equivale a usar la velocidad **pico** del electrón en (13.7.8).) A orden más bajo:

$$\gamma=1+\frac12\frac{e^2E_0^2}{m^2\omega^2c^2}\equiv1+x, \qquad (13.7.11)$$

$$n^2=1-\frac{\omega_p^2}{\omega^2(1+x)}\simeq1-\frac{\omega_p^2}{\omega^2}(1-x)=n_0^2+\frac{\omega_p^2}{\omega^2}x,\qquad n_0^2=1-\omega_p^2/\omega^2, \qquad (13.7.12),\ \text{p. 582}$$

$$n\simeq n_0+\frac1{2n_0}\frac{\omega_p^2}{\omega^2}x\equiv n_0+n_2I. \qquad (13.7.13)$$

Con $I=\tfrac12n_0\epsilon_0cE_0^2$:

$$n_2=\frac{\omega_p^2e^2}{2n_0^2\epsilon_0m^2c^3\omega^4}. \qquad (13.7.14)$$

Contribución puramente relativista ($\hbar$ no aparece). Forma intuitiva:

$$n_2=\frac{1}{2\pi n_0^2}\left(\frac{\omega_p}{\omega}\right)^2\left[\frac{\lambda^2}{(mc^2)/(r_0/c)}\right], \qquad (13.7.15)$$

con $r_0=e^2/4\pi\epsilon_0mc^2=2.6\times10^{-15}$ m (así impreso; el valor correcto es $2.82\times10^{-15}$ m). El
corchete = unidad relativista fundamental de índice no lineal: área $\lambda^2$ sobre la potencia unidad
$P_{\rm rel}$ ($mc^2$ entre el tiempo de tránsito de la luz por $r_0$):

$$P_{\rm rel}=\frac{mc^2}{(r_0/c)}=\frac{(0.5\times10^6)(1.6\times10^{-19})}{(2.6\times10^{-15}/3\times10^8)}=9.2\times10^9\ \text{W}. \qquad (13.7.16)$$

(Con $r_0=2.82\times10^{-15}$ m sale $8.7\times10^9$ W.) A $\lambda=1\ \mu$m:

$$n_2=\frac1{2\pi n_0^2}\left(\frac{\omega_p}{\omega}\right)^2\left(\frac{10^{-12}}{9.2\times10^9}\right)=\frac1{2\pi n_0^2}\left(\frac{\omega_p}{\omega}\right)^21.1\times10^{-22}\ \frac{\text{m}^2}{\text{W}}. \qquad (13.7.17)$$

(En el libro la segunda igualdad dice $(\omega_0/\omega)^2$; debe ser $(\omega_p/\omega)^2$.)

Potencia crítica de autoenfoque con (7.1.10) (p. 583):

$$P_{\rm cr}=\frac{(0.61)^2\pi\lambda^2}{8n_0n_2}\simeq\frac{\lambda^2}{8n_0n_2}, \qquad (13.7.18)$$

$$P_{\rm cr}=\frac\pi4n_0c\left(\frac{mc^2}{e}\right)^2\left(\frac{\omega}{\omega_p}\right)^2=6.7\left(\frac{\omega}{\omega_p}\right)^2\ \text{GW}. \qquad (13.7.19)$$

(**Nota de unidades:** la primera forma de (13.7.19) es gaussiana; en SI es
$\frac\pi4n_0(4\pi\epsilon_0c)(mc^2/e)^2(\omega/\omega_p)^2=\frac\pi4n_0(\omega/\omega_p)^2\,mc^3/r_0$, que con $r_0$ exacto da $6.8$ GW ✓.)
Sprangle *et al.* (1987) obtuvieron una expresión similar con 2 en lugar de $\pi/4$ (17 GW en lugar de 6.7).
Observado experimentalmente por Monot *et al.* (1995). Forma sugestiva:

$$P_{\rm cr}=\frac\pi4n_0\left(\frac{\omega}{\omega_p}\right)^2\left(\frac{mc^2}{r_0/c}\right). \qquad (13.7.20)$$

### 13.8 Nonlinear Quantum Electrodynamics (p. 583)

Además de $E_{\rm rel}=2mc^2/e\lambda$, existe un campo $E_{\rm QED}$ donde importan los efectos del vacío cuántico:

$$E_{\rm QED}=\frac{mc^2}{e\lambda\!\!\!^-_c},\qquad \lambda\!\!\!^-_c=\frac{\hbar}{mc}. \qquad (13.8.1)$$

$\lambda\!\!\!^-_c$ = longitud de onda Compton reducida, "$3.6\times10^{-11}$ cm" (así impreso; el valor correcto es $3.86\times10^{-11}$
cm). Nota al pie: de $\Delta E\Delta t\gtrsim\hbar$ con $\Delta E=mc^2$ y $\Delta t=\Delta x/c$, $\Delta x=\hbar/mc$; un fotón de longitud de onda
menor que $\sim\lambda\!\!\!^-_c$ crearía un par electrón–positrón. $E_{\rm QED}$ acelera un electrón a velocidades
relativistas en una distancia del tamaño del electrón → creación espontánea de pares (p. 584).

$$E_{\rm QED}=1.32\times10^{16}\ \text{V/cm}=1.32\times10^{20}\ \text{V/m}\quad\text{(así impreso)}. \qquad (13.8.2)$$

(**Errata:** $10^{16}$ V/cm $=10^{18}$ V/m; el valor correcto (campo de Schwinger) es $1.32\times10^{18}$ V/m.)

$$I_{\rm QED}=\tfrac12\epsilon_0cE_{\rm QED}^2=4\times10^{29}\ \text{W/cm}^2. \qquad (13.8.3)$$

(Con $1.32\times10^{18}$ V/m sale $2.3\times10^{29}$ W/cm².) Supera lo que producen los láseres actuales; es la máxima
intensidad posible (un campo mayor se absorbería instantáneamente por creación de pares). En el
marco de un electrón relativista de energía $E$ el campo aumenta por $\gamma=E/mc^2$; creación de pares
electrón–láser observada por Burke *et al.* (1997).

**No linealidad del vacío** (Euler y Kockel, 1935), en **unidades gaussianas** (resto de la sección):

$$\epsilon_{ik}=\delta_{ik}+\frac{e^4\hbar}{45\pi m^4c^7}\left[2(E^2-B^2)\delta_{ik}+7B_iB_k\right]. \qquad (13.8.4)$$

Para ondas planas en vacío $|\mathbf E|=|\mathbf B|$ y el primer término se anula:

$$\epsilon_{ik}=\delta_{ik}+\frac{7e^4\hbar}{45\pi m^4c^7}B_iB_k, \qquad (13.8.5)$$

$$\epsilon_{ik}=\delta_{ik}+\frac{7}{45\pi}\frac{e^2}{\hbar c}\frac{B_iB_k}{E_{\rm QED}^2}. \qquad (13.8.6)$$

La respuesta es apreciable solo para $B\gtrsim E_{\rm QED}$ (p. 585). Tensorialmente distinta (aparece $B$, no
$E$), pero suprimiendo el carácter tensorial: con $D=\epsilon E=E+4\pi P$, $D^{NL}=4\pi P^{NL}$:

$$\frac{7}{45\pi}\frac{e^2}{\hbar c}\frac{\tilde B^2\tilde E}{E_{\rm QED}^2}=4\pi\chi^{(3)}\tilde E^3, \qquad (13.8.7)$$

y con $\tilde B=\tilde E$:

$$\chi^{(3)}=\frac{7}{180\pi^2}\frac{e^2}{\hbar c}\frac1{E_{\rm QED}^2}=1.44\times10^{-32}\ \text{esu}. \qquad (13.8.8)$$

Comparación: CS₂, $\chi^{(3)}=1.9\times10^{-12}$ esu. Índice no lineal $n_2=(12\pi^2/c)\chi^{(3)}$ (gaussiano; para pasar a
cm²/W hay que multiplicar por $10^7$, cf. Apéndice C):

$$n_2=5.6\times10^{-34}\ \text{cm}^2/\text{W}. \qquad (13.8.9)$$

Potencia crítica (cap. 7):

$$P_{\rm cr}=\frac{\lambda^2}{8n_0n_2}, \qquad (13.8.10)$$

a $\lambda=1\ \mu$m:

$$P_{\rm cr}=4.4\times10^{24}\ \text{W}, \qquad (13.8.11)$$

mucho mayor que cualquier fuente contemplada. (**Duda:** con (13.8.9)–(13.8.10) y $n_0=1$ sale
$10^{-8}/(8\times5.6\times10^{-34})=2.2\times10^{24}$ W; el libro da el doble.)

---

## Tablas y datos numéricos útiles

| Magnitud | Valor | Página |
|---|---|---|
| Sílice fundida, 800 nm: $n_2$ | $3.5\times10^{-20}$ m²/W | 568 |
| Sílice fundida, 800 nm: $k_2$ (GVD) | 446 fs²/cm | 568 |
| $L_{\rm dis}$ para pulso de 20 fs en sílice | ≈ 0.9 cm | 568 |
| Supercontinuo (Fork 1983): 80 fs, $10^{14}$ W/cm², 0.5 mm etilenglicol | $0.4\omega_0$ – $3.3\omega_0$ | 571 |
| $E_{\rm at}$ | $6\times10^{11}$ V/m (cap. 12: $5\times10^{11}$) | 571 |
| $I_{\rm at}$ | $4\times10^{16}$ W/cm² | 572 |
| $K$ a 1.06 μm | 13.6 eV @ $1.3\times10^{14}$ W/cm²; 4.2 keV @ $I_{\rm at}$; 500 keV @ $4.8\times10^{18}$ W/cm² | 573 |
| HHG: intensidades típicas | $10^{14}$–$10^{16}$ W/cm² | 575 |
| HHG: corte | $q_{\max}\hbar\omega=3.17K+I_P$ | 577 |
| HHG: orden máximo observado | 221 (He, 26 fs, 800 nm) | 575, 578 |
| Umbral relativista | $I\gtrsim10^{18}$ W/cm² | 580–581 |
| $P_{\rm rel}=mc^2/(r_0/c)$ | $9.2\times10^9$ W | 582 |
| $n_2$ relativista a 1 μm | $(1/2\pi n_0^2)(\omega_p/\omega)^2\,1.1\times10^{-22}$ m²/W | 582 |
| $P_{\rm cr}$ relativista | $6.7(\omega/\omega_p)^2$ GW (Sprangle: 17) | 583 |
| $E_{\rm QED}$ | $1.32\times10^{16}$ V/cm | 584 |
| $I_{\rm QED}$ | $4\times10^{29}$ W/cm² | 584 |
| $\chi^{(3)}$ del vacío | $1.44\times10^{-32}$ esu | 585 |
| $\chi^{(3)}$ del CS₂ | $1.9\times10^{-12}$ esu | 585 |
| $n_2$ del vacío | $5.6\times10^{-34}$ cm²/W | 585 |
| $P_{\rm cr}$ del vacío (1 μm) | $4.4\times10^{24}$ W | 585 |

---

## Problema (p. 586)

1. Considere el movimiento **no relativista** de un electrón libre en el campo láser
   $\tilde{\mathbf E}(z,t)=E_0\cos\omega t\,\hat{\mathbf x}$, $\tilde{\mathbf B}(z,t)=B_0\cos\omega t\,\hat{\mathbf y}$ con $B_0=E_0$. El electrón se inyecta en
   reposo en $x=0$, $y=0$ en el instante $t_0$.
   (a) Resuelva la ecuación de movimiento y determine $x(t)$, $y(t)$, $z(t)$, $v_x(t)$, $v_y(t)$ y $v_z(t)$
   para todo $t>t_0$. Grafique la trayectoria tanto en el marco de laboratorio como en un marco en el
   que el electrón está en promedio en reposo (especifique cuál es). Algunos resultados dependen de
   $t_0$; para esos, muestre gráficas para varios valores de $t_0$ (el libro dice "$t$").
   (b) Ignorando la contribución magnética, calcule la energía cinética pico y promedio en el tiempo.
   (c) Repita para polarización circular.

(1 problema. Nota: $B_0=E_0$ es la relación gaussiana; en SI sería $B_0=E_0/c$.)

---

## Referencias principales (p. 586–587)

- *13.1–13.3 Ultrafast NLO*: Alfano y Shapiro (1970) *PRL* **24**, 592; Brabec y Krausz (1997) *PRL*
  **78**, 3282; Corkum, Rolland y Srinivasan‑Rao (1986) *PRL* **57**, 2268; DeMartini *et al.* (1967)
  *Phys. Rev.* **164**, 312; Diels y Rudolph (1996) *Ultrashort Laser Pulse Phenomena*, Academic
  Press; Fork *et al.* (1983) *Opt. Lett.* **8**, 1; Gaeta (2000) *PRL* **84**, 3582; Rothenberg (1992)
  *Opt. Lett.* **17**, 1340; Yang y Shen (1984) *Opt. Lett.* **9**, 510.
- *13.4–13.5*: Castillo‑Herrara y Johnston (1993) *IEEE Trans. Plasma Sci.* **21**, 125; Kibble (1966)
  *PRL* **16**, 1054; Landau y Lifshitz (1960) *Classical Theory of Fields*, §48; Mourou, Barty y Perry
  (1998) *Phys. Today* **51**, 22; Sarachik y Schappert (1970) *PRD* **1**, 2738.
- *13.6 HHG*: Agostini *et al.* (1979) *PRL* **42**, 1127; Chang *et al.* (1997) *PRL* **79**, 2967; Chang *et
  al.* (1999) *PRL* **82**, 2006; Corkum (1993) *PRL* **71**, 1994; Durfee *et al.* (1999) *PRL* **83**, 2187;
  Ferray *et al.* (1988) *J. Phys. B* **21**, L31; Kulander y Shore (1989) *PRL* **62**, 524; Lewenstein *et
  al.* (1994) *PRA* **49**, 2117; L'Huillier y Balcou (1993) *PRL* **70**, 774; Schnürer *et al.* (1998) *PRL*
  **80**, 3236; Schafer *et al.* (1993) *PRL* **70**, 1599; Walker *et al.* (1994) *PRL* **73**, 1127.
- *13.7 Plasmas*: Max, Arons y Langdon (1974) *PRL* **33**, 209; Monot *et al.* (1995) *PRL* **74**, 2953;
  Sprangle, Tang y Esarey (1987) *IEEE Trans. Plasma Sci.* **15**, 145; Wagner *et al.* (1997) *PRL* **78**,
  3125.
- *13.8 QED*: Burke *et al.* (1997) *PRL* **79**, 1626; Euler y Kockel (1935) *Naturwiss.* **23**, 246.

---

## Relación con el curso y con el proyecto final

- **Curso:** extiende el tema 6 (Boyd 4.1–4.2 y 7.1–7.2): la NLSE de §7.5 y la potencia crítica de
  autoenfoque (7.1.10) reaparecen aquí; $L_{\rm NL}=1/[(\omega_0/c)n_2I]$ es el inverso de la fase no lineal por
  unidad de longitud de la SPM. Útil para preguntas de examen de orden de magnitud ($L_{\rm dis}$ de 20 fs
  en sílice, $I_{\rm at}$, energía ponderomotriz).
- **Proyecto final (supercontinuo en SiN/Si):** §13.2–13.3 es la base de la **GNLSE** que se usará
  para simular supercontinuo en guías: (13.3.5) con $\gamma_1$, $\gamma_2$ es la NLSE con término de
  autoempinamiento $\propto(1/\omega_0)\partial_t(|A|^2A)$ y dispersión de orden alto $\tilde D=\sum k_n(i\partial_t)^n/n!$. En guías
  integradas $k_n\to\beta_n$ del modo y $\gamma=n_2\omega_0/(cA_{\rm eff})$ (con $A$ normalizada a potencia), y deben
  añadirse Raman, TPA y portadores libres (Si). Las longitudes $L_{\rm dis}=T_0^2/|\beta_2|$ y $L_{\rm NL}=1/(\gamma P_0)$
  dan el número de solitón $N^2=L_{\rm dis}/L_{\rm NL}$ que gobierna la fisión de solitones (mecanismo dominante del
  SC en régimen anómalo, que el libro no menciona: su afirmación de que el mecanismo del SC es el
  autoempinamiento/choque refleja la visión de 2000 para medios volumétricos normales; para guías y
  fibras la referencia estándar es Dudley, Genty y Coen, *RMP* 78, 1135 (2006)).
- El acoplamiento espacio‑tiempo (§13.3.2) no aplica en guías monomodo (el modo fija el perfil
  transversal), salvo vía la dependencia en frecuencia de $A_{\rm eff}$.
