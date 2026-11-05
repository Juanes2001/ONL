# Capítulo 19 — Acousto-Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 804–833 (PDF 826–855). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 19.
Notación del libro: dependencia temporal $e^{j\omega t}$, $j=\sqrt{-1}$; campos reales en caligráfica
($\mathcal{E}$, $\mathcal{P}$, $\mathcal{S}$), amplitudes complejas en itálica/negrita ($E$, $A$, $\mathbf{k}$);
reflectancia de amplitud compleja $\mathsf{r}$ (letra "sans"), reflectancia de intensidad $\mathcal{R}$,
figura de mérito $\mathcal{M}$, coeficiente fotoelástico $\mathfrak{p}$ (en el libro una "p" gótica). Unidades SI.
Las secciones marcadas con * en el índice del libro son avanzadas (19.1B y 19.3).

## Resumen del capítulo

El índice de refracción de un medio se altera por la presencia de sonido (efecto **acusto-óptico**):
una onda acústica es una onda de deformación (*strain*) que, a través del efecto fotoelástico, crea una
onda de índice de refracción $n(x,t)=n-\Delta n_0\cos(\Omega t-qx)$ con $\Delta n_0=\tfrac12\mathfrak{p}n^3S_0$.
Como la frecuencia acústica es ≥ 5 órdenes de magnitud menor que la óptica, el medio se trata de forma
adiabática como un medio de índice graduado "congelado". La luz se refleja parcialmente en los planos de
índice y las reflexiones interfieren constructivamente solo cuando se cumple la **condición de Bragg**
$\sin\theta_{\mathcal B}=\lambda/2\Lambda$, equivalente a la conservación de momento $\mathbf{k}_r=\mathbf{k}+\mathbf{q}$;
la onda reflejada sufre un corrimiento Doppler $\omega_r=\omega\pm\Omega$ (interpretación cuántica: fotón + fonón →
fotón). La reflectancia es proporcional a la intensidad acústica $I_s$, a la figura de mérito del material
$\mathcal{M}=\mathfrak{p}^2n^6/\varrho v_s^3$ y a $(L/\sin\theta)^2$; con saturación (teoría de ondas acopladas)
$\mathcal{R}_e=\sin^2\sqrt{\mathcal R}$. Los haces (ópticos y acústicos) se tratan como superposición de ondas
planas, lo que lleva a la difracción de Raman–Nath (haz acústico delgado = rejilla de fase, órdenes ±θ, ±2θ, …).
En 19.2 se usan estas ideas para moduladores (ancho de banda $B=1/T$, $T=D/v_s$), escáneres (número de puntos
resolubles $N=TB$), conmutadores espaciales (capacidad de interconexión $ML\le N$), filtros sintonizables,
desplazadores de frecuencia y aisladores. En 19.3 se generaliza a medios anisótropos: tensor de deformación
$s_{ij}$, tensor elasto-óptico $\mathfrak{p}_{ijkl}$ (matriz 6×6, forma cúbica), ondas acústicas longitudinales
y transversales que convierten un cristal cúbico en uniaxial o biaxial, y difracción de Bragg con $n_r\neq n$
(ángulos de incidencia y reflexión distintos, reflexión frontal colineal $n_r-n=\lambda_o/\Lambda$).

## Secciones

### Introducción (p. 805–806)

- **Idea central (p. 805):** "sound can control light". El sonido modifica el índice del medio; dispositivos:
  moduladores, conmutadores, deflectores, filtros, aisladores, desplazadores de frecuencia, analizadores de
  espectro. Fig. 19.0-1: el sonido modifica el efecto del medio sobre la luz.
- Fig. 19.0-2 (p. 805): onda plana armónica de compresiones y rarefacciones; en las zonas comprimidas la
  densidad y el índice son mayores. Patrón de período Λ (longitud de onda del sonido) que viaja a la velocidad
  del sonido. En sólidos, las vibraciones de las moléculas alrededor de su equilibrio alteran la polarizabilidad
  óptica y por tanto $n$.
- El medio se convierte en un **medio de índice graduado dinámico** (inhomogéneo y variable en el tiempo).
  Como las frecuencias ópticas ≫ acústicas, hay dos escalas de tiempo muy distintas: enfoque **adiabático /
  cuasi-estacionario**: se resuelve el problema óptico en cada instante tratando al medio como inhomogéneo
  estático ("congelado") (p. 805–806).
- **Condición de Bragg (recuadro, p. 806):**
  $$\sin\theta=\frac{\lambda}{2\Lambda}\qquad(19.0\text{-}1)$$
  con $\lambda$ la longitud de onda de la luz *en el medio* y $\Lambda$ la del sonido (ver Ejercicio 2.5-3).
  Nombres: **difracción de Bragg**, reflexión de Bragg, dispersión de Bragg; el dispositivo es un reflector
  de Bragg, deflector de Bragg o **celda de Bragg**. Fig. 19.0-3: la onda acústica actúa como reflector
  parcial (divisor de haz) cuando θ cumple Bragg.
- *This Chapter* (p. 806): 19.1 teoría simple para medios lineales no dispersivos, ignorando anisotropía y
  polarización, con interpretación cuántica; 19.2 modulación y barrido; 19.3 efectos anisótropos y de
  polarización.

### 19.1 Interaction of Light and Sound (p. 806)

Se describe el efecto de una onda acústica escalar sobre una onda óptica escalar: primero ondas planas,
luego haces.

#### 19.1A Bragg Diffraction (p. 806)

**Onda acústica (p. 806–807).** Onda plana en dirección $x$, velocidad $v_s$, frecuencia $f$, $\Lambda=v_s/f$.
Deformación (desplazamiento relativo):
$$s(x,t)=S_0\cos(\Omega t-qx)\qquad(19.1\text{-}1)$$
$S_0$ amplitud, $\Omega=2\pi f$ frecuencia angular, $q=2\pi/\Lambda$ número de onda. Intensidad acústica (W/m²):
$$I_s=\tfrac12\varrho v_s^3S_0^2\qquad(19.1\text{-}2)$$
con $\varrho$ la densidad de masa.

**Perturbación del índice (p. 807).** Análoga al efecto Pockels (20.1-4):
$$\Delta n(x,t)=-\tfrac12\mathfrak{p}\,n^3 s(x,t)\qquad(19.1\text{-}3)$$
$\mathfrak{p}$ = **constante fotoelástica** (coeficiente elasto-óptico, *strain-optic coefficient*), adimensional.
El signo menos: deformación positiva (dilatación) reduce el índice. Por tanto
$$n(x,t)=n-\Delta n_0\cos(\Omega t-qx)\qquad(19.1\text{-}4)$$
$$\Delta n_0=\tfrac12\mathfrak{p}\,n^3S_0\qquad(19.1\text{-}5)$$
Combinando con (19.1-2), el cambio de índice es proporcional a la raíz de la intensidad acústica
(**recuadros, p. 807**):
$$\Delta n_0=\sqrt{\tfrac12\mathcal{M}I_s}\qquad(19.1\text{-}6)$$
$$\mathcal{M}=\frac{\mathfrak{p}^2n^6}{\varrho v_s^3}\qquad(19.1\text{-}7)$$
$\mathcal{M}$ (m²/W) es la **figura de mérito** de la fuerza del efecto acusto-óptico del material.

> **Ejemplo 19.1-1, Figura de mérito (p. 807).** Vidrio flint extra-denso: $\varrho=6.3\times10^3$ kg/m³,
> $v_s=3.1$ km/s, $n=1.92$, $\mathfrak{p}=0.25$ → $\mathcal{M}=1.67\times10^{-14}$ m²/W. Una onda acústica de
> $I_s=10$ W/cm² crea $\Delta n_0=2.89\times10^{-5}$.

**Onda óptica (p. 808).** Frecuencia $\nu$, $\omega=2\pi\nu$, $\lambda_o=c_o/\nu$, $\lambda=\lambda_o/n$,
$k=n\omega/c_o$, vector $\mathbf{k}$ en el plano $x$–$z$ formando ángulo $\theta$ con el eje $z$ (Fig. 19.1-1:
reflexiones desde las capas de un medio inhomogéneo de longitud $L$ a lo largo de $z$; la proyección sobre $x$
del trayecto es $L\sin\theta$).

**Modelo de capas (p. 808).** Como $f\ll\nu$ (≥ 5 órdenes), se congela el índice:
$$n(x)=n-\Delta n_0\cos(qx-\varphi)\qquad(19.1\text{-}8)$$
con $\varphi$ fase fija; luego se toma $\varphi=\Omega t$. Se divide el medio en capas planas ortogonales a $x$;
cada una refleja parcialmente; se supone reflectancia pequeña (onda transmitida **no agotada**).
Si $\Delta\mathsf{r}=(d\mathsf{r}/dx)\Delta x$ es la reflectancia incremental de una capa en $x$:
$$\mathsf{r}=\int_{-L/2}^{L/2}e^{j2kx\sin\theta}\frac{d\mathsf{r}}{dx}\,dx\qquad(19.1\text{-}9)$$
El factor $e^{j2kx\sin\theta}$ aparece porque la onda reflejada en $x$ está adelantada una distancia $2x\sin\theta$
respecto a la reflejada en $x=0$. Se toman iguales los números de onda incidente y reflejado.
$$\frac{d\mathsf{r}}{dx}=\frac{d\mathsf{r}}{dn}\frac{dn}{dx}=\frac{d\mathsf{r}}{dn}\,q\,\Delta n_0\sin(qx-\varphi)\qquad(19.1\text{-}10)$$
($d\mathsf{r}/dn$ sale de las ecuaciones de Fresnel, no depende de $x$). Con $\sin(qx-\varphi)=[e^{j(qx-\varphi)}-e^{-j(qx-\varphi)}]/2j$ (p. 808–809):
$$\mathsf{r}=j\mathsf{r}_0e^{j\varphi}\frac1L\int_{-L/2}^{L/2}e^{j(2k\sin\theta-q)x}dx-j\mathsf{r}_0e^{-j\varphi}\frac1L\int_{-L/2}^{L/2}e^{j(2k\sin\theta+q)x}dx\qquad(19.1\text{-}11)$$
$$\mathsf{r}_0=\tfrac12\Delta n_0\,qL\,\frac{d\mathsf{r}}{dn}\qquad(19.1\text{-}12)$$
Integrando y con $\varphi=\Omega t$:
$$\mathsf{r}=\mathsf{r}_++\mathsf{r}_-\qquad(19.1\text{-}13)$$
**Recuadro (p. 809), Amplitude Reflectance:**
$$\mathsf{r}_\pm=\pm j\mathsf{r}_0\,\mathrm{sinc}\!\left[(2k\sin\theta\mp q)\frac{L}{2\pi}\right]e^{\pm j\Omega t}\qquad(19.1\text{-}14)$$
con $\mathrm{sinc}(x)=\sin(\pi x)/(\pi x)$. $\mathsf{r}_+$ = reflexión **upshifted** (máxima en $2k\sin\theta=q$),
$\mathsf{r}_-$ = **downshifted** (máxima en $2k\sin\theta=-q$). Si $L$ es grande los máximos son agudos y solo
un término es significativo a la vez, según $\theta=\pm\sin^{-1}(q/2k)$.

**Condición de Bragg (p. 809).** La sinc vale 1 cuando $q=2k\sin\theta$, es decir $\theta=\theta_{\mathcal B}=\sin^{-1}(q/2k)$,
el **ángulo de Bragg**. Con $q=2\pi/\Lambda$, $k=2\pi/\lambda$ (**recuadro, Bragg Angle**):
$$\sin\theta_{\mathcal B}=\frac{\lambda}{2\Lambda}\qquad(19.1\text{-}15)$$
Es el ángulo para el que las reflexiones incrementales de planos separados Λ tienen desfase 2π e interfieren
constructivamente [Ejercicio 2.5-3 y (7.1-45)].

> **Ejemplo 19.1-2, Ángulo de Bragg (p. 809).** Vidrio flint, $v_s=3$ km/s, $n=1.95$, $\lambda_o=633$ nm
> ($\lambda=325$ nm), $f=100$ MHz ($\Lambda=30$ µm) → $\theta_{\mathcal B}=5.4$ mrad ≈ 0.31° (ángulo interno).
> En aire el ángulo externo es $\theta'_{\mathcal B}\approx n\theta_{\mathcal B}=0.61°$. Con $f=1$ GHz,
> $\theta_{\mathcal B}=3.1°$.

**Forma vectorial (p. 810).** Con $\mathbf{q}=(q,0,0)$, $\mathbf{k}=(-k\sin\theta,0,k\cos\theta)$,
$\mathbf{k}_r=(k\sin\theta,0,k\cos\theta)$, la condición $q=2k\sin\theta_{\mathcal B}$ equivale a (**recuadro**):
$$\mathbf{k}_r=\mathbf{k}+\mathbf{q}\qquad(19.1\text{-}16)$$
Fig. 19.1-2: diagrama vectorial (triángulo isósceles con lados $2\pi/\lambda$ y base $2\pi/\Lambda$).

**Tolerancia en la condición de Bragg (p. 810).** La dependencia angular es
$\mathrm{sinc}[(q-2k\sin\theta)L/2\pi]=\mathrm{sinc}[(\sin\theta-\sin\theta_{\mathcal B})2L/\lambda]$. Primer cero
cuando $\sin\theta-\sin\theta_{\mathcal B}=\lambda/2L$; como $\theta_{\mathcal B}$ es pequeño,
la reflectancia se anula a una desviación angular $\theta-\theta_{\mathcal B}\approx\lambda/2L$ — anchura
angular extremadamente pequeña porque $L\gg\lambda$ (interferencia destructiva de las reflexiones
incrementales). Fig. 19.1-3: $|\mathsf{r}|^2$ vs. $\theta$, pico en $\theta_{\mathcal B}$ de anchura $\lambda/2L$.

**Corrimiento Doppler (p. 811).** $\mathsf{r}_+\propto e^{j\Omega t}$; con $E\propto e^{j\omega t}$ la onda
reflejada $E_r=\mathsf{r}_+E\propto e^{j(\omega+\Omega)t}$ tiene (**recuadro, Doppler Shift**):
$$\omega_r=\omega+\Omega\qquad(19.1\text{-}17)$$
La reflexión viene acompañada de un corrimiento de frecuencia igual a la frecuencia del sonido. Interpretación
Doppler (Ejercicio 2.6-1, Sec. 13.3D): superficies que se mueven a $v_s$; $\omega_r=\omega(1+2v_s\sin\theta/c)$
con $v_s\sin\theta$ la componente de velocidad en la dirección de la luz; usando $\sin\theta=\lambda/2\Lambda$,
$v_s=\Lambda\Omega/2\pi$, $c=\lambda\omega/2\pi$ se reproduce (19.1-17). Como $\Omega\ll\omega$ (error < 1 parte en
$10^5$), las longitudes de onda incidente y reflejada son ≈ iguales, lo que justifica usar el mismo $k$ en
(19.1-9) y vectores de igual longitud $n\omega/c_o$ en la Fig. 19.1-2.

**Reflectancia pico (p. 811–812).** $\mathcal{R}=|\mathsf{r}_+|^2$ = razón de intensidades reflejada/incidente;
en $\theta=\theta_{\mathcal B}$, $\mathcal R=|\mathsf{r}_0|^2$:
$$\mathcal{R}=\tfrac14\Delta n_0^2q^2L^2\left|\frac{d\mathsf{r}}{dn}\right|^2\qquad(19.1\text{-}18)$$
$d\mathsf{r}/dn$ por Fresnel (Sec. 6.2). TE: (6.2-8) con $n_1=n+\Delta n$, $n_2=n$, $\theta_1=90°-\theta$, Snell para
$\theta_2$; despreciando segundo orden, $\Delta\mathsf{r}=-\Delta n/2n\sin^2\theta$:
$$\frac{d\mathsf{r}}{dn}=\frac{-1}{2n\sin^2\theta}\qquad(19.1\text{-}19)\ \text{(TE)}$$
$$\frac{d\mathsf{r}}{dn}=\frac{-\cos2\theta}{2n\sin^2\theta}\qquad(19.1\text{-}20)\ \text{(TM)}$$
En la mayoría de dispositivos $\theta$ es muy pequeño, $\cos2\theta\approx1$ y (19.1-19) sirve para ambas
polarizaciones. Con la condición de Bragg $q=2k\sin\theta=4\pi n\sin\theta/\lambda_o$:
$$\mathcal{R}=\frac{\pi^2}{\lambda_o^2}\left(\frac{L}{\sin\theta}\right)^2\Delta n_0^2\qquad(19.1\text{-}21)$$
Con (19.1-6) (**recuadro, p. 812, Reflectance**):
$$\mathcal{R}=\frac{\pi^2}{2\lambda_o^2}\left(\frac{L}{\sin\theta}\right)^2\mathcal{M}I_s\qquad(19.1\text{-}22)$$
Proporcional a $I_s$, a $\mathcal M$ y al cuadrado de la distancia oblicua de penetración $L/\sin\theta$.
Sustituyendo $\sin\theta=\lambda/2\Lambda$:
$$\mathcal{R}=2\pi^2n^2\frac{L^2\Lambda^2}{\lambda_o^4}\mathcal{M}I_s\qquad(19.1\text{-}23)$$
→ $\mathcal R\propto\lambda_o^{-4}\propto\omega^4$, típico de fenómenos de dispersión de luz (como Rayleigh).

**Saturación (p. 812).** Según (19.1-22) $\mathcal R$ superaría 1 con sonido intenso: viola la hipótesis de no
agotamiento. Incluyendo el agotamiento (Sec. 19.1B) (**recuadro**):
$$\mathcal{R}_e=\sin^2\sqrt{\mathcal R}\qquad(19.1\text{-}24)$$
$\mathcal R$ = expresión aproximada (19.1-22), $\mathcal R_e$ = exacta. Si $\mathcal R\ll1$, $\mathcal R_e\approx\mathcal R$.
Fig. 19.1-4: $\mathcal R_e$ vs. $I_s$: lineal al inicio, alcanza 1 y luego decrece.

> **Ejemplo 19.1-3, Reflectancia de un reflector de Bragg (p. 812–813).** Flint extra-denso,
> $\mathcal M=1.67\times10^{-14}$ m²/W, $\lambda_o=633$ nm (He–Ne), $I_s=10$ W/cm², $L/\sin\theta=1$ mm →
> $\mathcal R=0.0206$, $\mathcal R_e=0.0205$ (≈ 2 % reflejado). Con $I_s=100$ W/cm²: $\mathcal R=0.206$,
> $\mathcal R_e=0.192$ (≈ 19 %).

**Difracción de Bragg downshifted (p. 813).** Geometría $2k\sin\theta=-q$ ($\theta$ negativo: la luz incidente
forma ángulo agudo con la onda sonora, Fig. 19.1-5). Domina $\mathsf{r}_-$:
$$\mathsf{r}_-=-j\mathsf{r}_0e^{-j\Omega t}\qquad(19.1\text{-}25)$$
$$\omega_s=\omega-\Omega\qquad(19.1\text{-}26)$$
$$\mathbf{k}_s=\mathbf{k}-\mathbf{q}\qquad(19.1\text{-}27)$$
(19.1-27) es una **condición de ajuste de fase** (*phase matching*). El corrimiento hacia abajo es coherente con
Doppler porque luz y sonido viajan en la misma dirección.

**Interpretación cuántica (p. 813–814).** Luz = fotones de energía $\hbar\omega$ y momento $\hbar\mathbf{k}$;
sonido = **fonones** de energía $\hbar\Omega$ y momento $\hbar\mathbf{q}$. Un fotón se combina con un fonón
para generar un nuevo fotón con la suma de energía y momento: $\hbar\omega_r=\hbar\omega+\hbar\Omega$ y
$\hbar\mathbf{k}_r=\hbar\mathbf{k}+\hbar\mathbf{q}$ → se recuperan Doppler (19.1-17) y Bragg (19.1-16).
Fig. 19.1-6: diagrama fotón + fonón → fotón.

#### *19.1B Coupled-Wave Theory (p. 814)

**Bragg como proceso de dispersión (p. 814–815).** Según Sec. 5.2B, la propagación en un medio homogéneo con
perturbación lenta $\Delta n$ obedece
$$\nabla^2\mathcal{E}-\frac{1}{c^2}\frac{\partial^2\mathcal{E}}{\partial t^2}\approx-\mathcal{S}\qquad(19.1\text{-}28)$$
$$\mathcal{S}=-\mu_o\frac{\partial^2\Delta\mathcal{P}}{\partial t^2}=-2\mu_o\epsilon_o n\frac{\partial^2}{\partial t^2}(\Delta n\,\mathcal{E})\qquad(19.1\text{-}29)$$
fuente de radiación proporcional a la segunda derivada de $\Delta n\,\mathcal E$ [ver (5.2-20)]. En Bragg $\Delta n$
la crea el sonido, así que la fuente depende del campo acústico y del campo óptico total (incidente + dispersado).
**Primera aproximación de Born:** la fuente se calcula con el campo incidente solamente. Con onda plana
incidente y perturbación plana:
$$\mathcal{E}=\mathrm{Re}\{A\exp[j(\omega t-\mathbf{k}\cdot\mathbf{r})]\}\qquad(19.1\text{-}30)$$
$$\Delta n=-\Delta n_0\cos(\Omega t-\mathbf{q}\cdot\mathbf{r})\qquad(19.1\text{-}31)$$
$$\mathcal{S}=-\left(\frac{\Delta n_0}{n}\right)\left(k_r^2\,\mathrm{Re}\{A\exp[j(\omega_rt-\mathbf{k}_r\cdot\mathbf{r})]\}+k_s^2\,\mathrm{Re}\{A\exp[j(\omega_st-\mathbf{k}_s\cdot\mathbf{r})]\}\right)\qquad(19.1\text{-}32)$$
con $\omega_r=\omega+\Omega$, $\mathbf{k}_r=\mathbf{k}+\mathbf{q}$, $k_r=\omega_r/c$; $\omega_s=\omega-\Omega$,
$\mathbf{k}_s=\mathbf{k}-\mathbf{q}$, $k_s=\omega_s/c$. Dos fuentes de luz a $\omega\pm\Omega$ con vectores
$\mathbf{k}\pm\mathbf{q}$ que emiten la onda plana reflejada upshifted (si $|\mathbf{k}+\mathbf{q}|=\omega_r/c\approx\omega/c$)
o downshifted (si $|\mathbf{k}-\mathbf{q}|\approx\omega/c$); ambas condiciones no se cumplen simultáneamente.
Así se prueban independientemente Bragg y Doppler. (19.1-32) indica intensidad emitida $\propto\omega_r^4\approx\omega^4$
(eficiencia $\propto\lambda^{-4}$). La reflectancia por esta vía se pide en el Prob. 19.1-2.

**Ecuaciones de ondas acopladas (p. 815–816).** Más allá de Born: incluir el campo dispersado en $\mathcal S$.
Geometría upshifted, $\mathcal E=\mathrm{Re}\{E e^{j\omega t}\}+\mathrm{Re}\{E_r e^{j\omega_r t}\}$:
$$\mathcal{S}=\mathrm{Re}\{S e^{j\omega t}+S_r e^{j\omega_r t}\}+\text{términos de otras frecuencias}\qquad(19.1\text{-}33)$$
$$S=-k^2\frac{\Delta n_0}{n}E_r,\qquad S_r=-k_r^2\frac{\Delta n_0}{n}E\qquad(19.1\text{-}34)$$
Igualando frecuencias → dos **ecuaciones de Helmholtz acopladas**:
$$(\nabla^2+k^2)E=-S,\qquad(\nabla^2+k_r^2)E_r=-S_r\qquad(19.1\text{-}35)$$
Caso de ángulo pequeño ($\theta\ll1$, ambas ondas ≈ en $z$, $k\approx k_r$), $E=A e^{-jkz}$, $E_r=A_r e^{-jkz}$
con $A$, $A_r$ lentamente variables; con la aproximación de envolvente lenta (Sec. 2.2C)
$(\nabla^2+k^2)Ae^{-jkz}\approx-j2k(dA/dz)e^{-jkz}$ (**recuadro, p. 815**):
$$\frac{dA}{dz}=j\tfrac12\gamma A_r\qquad(19.1\text{-}36a)$$
$$\frac{dA_r}{dz}=j\tfrac12\gamma A\qquad(19.1\text{-}36b)$$
$$\gamma=k\frac{\Delta n_0}{n}\qquad(19.1\text{-}37)$$
Celda entre $z=0$ y $z=d$, condición de frontera $A_r(0)=0$ → solución armónica:
$$A(z)=A(0)\cos\frac{\gamma z}{2}\qquad(19.1\text{-}38a)$$
$$A_r(z)=jA(0)\sin\frac{\gamma z}{2}\qquad(19.1\text{-}38b)$$
Fig. 19.1-7: sube $|A_r|^2$ y baja $|A|^2$ con $z$ (intercambio periódico de energía). Reflectancia
$\mathcal R_e=|A_r(d)|^2/|A(0)|^2=\sin^2(\gamma d/2)=\sin^2\sqrt{\mathcal R}$ con $\mathcal R=(\gamma d/2)^2$;
usando (19.1-37): $\mathcal R=(\pi^2/\lambda_o^2)\Delta n_0^2d^2$ — exactamente (19.1-21) con $d=L/\sin\theta$
(p. 816).

#### 19.1C Bragg Diffraction of Beams (p. 816)

Onda plana óptica $\mathbf k$ + onda plana acústica $\mathbf q$ → onda plana $\mathbf{k}_r=\mathbf k+\mathbf q$
si $|\mathbf k+\mathbf q|\approx k=2\pi/\lambda$. Un *haz* se trata como superposición de ondas planas en distintas
direcciones (introducción del cap. 4).

**Haz óptico + onda plana acústica (p. 816–817).** Haz de anchura $D$: cono de ondas planas de semiángulo
$$\delta\theta=\frac{\lambda}{D}\qquad(19.1\text{-}39)$$
(factor 1.0 por convención; haz rectangular: $\lambda/D$ pico-a-primer-cero; circular: $1.22\lambda/D$; gaussiano
con $D=2W_0$: $\delta\theta=\lambda/\pi W_0=(2/\pi)\lambda/D\approx0.64\lambda/D$ [ver (3.1-20)]). Hay un solo
$\mathbf q$ y muchos $\mathbf k$ (misma longitud $2\pi/\lambda$) dentro del cono $\delta\theta$: solo **una**
dirección de $\mathbf k$ cumple Bragg; la onda reflejada es una **onda plana** única $\mathbf k_r$ (Fig. 19.1-8).

**Haz óptico + haz acústico (p. 817).** Haz acústico de anchura $D_s$: si $\Lambda\ll$ anchura del medio, el
sonido se propaga como onda libre con divergencia
$$\delta\theta_s=\frac{\Lambda}{D_s}\qquad(19.1\text{-}40)$$
La reflexión se halla emparejando ondas planas ópticas y acústicas que cumplan Bragg: muchos $\mathbf k$
(longitud $2\pi/\lambda$) y muchos $\mathbf q$ (longitud $2\pi/\Lambda$); solo contribuyen los pares que forman
**triángulo isósceles** (Fig. 19.1-9). Si $\delta\theta_s\gg\delta\theta$ y las direcciones centrales cumplen
Bragg, toda onda plana óptica encuentra pareja acústica y el haz reflejado tiene la misma divergencia
$\delta\theta$ que el incidente. Aplicación: sondear la distribución angular de energía de un haz sonoro con
un haz de luz de divergencia mucho menor variando el ángulo de incidencia.

**Onda plana óptica + haz acústico delgado: difracción de Raman–Nath (p. 818).** Haz acústico delgado =
ondas planas en muchas direcciones → difracta a ángulos muy distintos del Bragg de la dirección principal.
Fig. 19.1-10: onda óptica incidente perpendicular a la dirección principal de un haz acústico delgado;
Bragg se cumple si $\mathbf k_r$ forma ángulos $\pm\theta$ con
$$\sin\frac{\theta}{2}=\frac{\lambda}{2\Lambda}\qquad(19.1\text{-}41)$$
y, para $\theta$ pequeño (**recuadro, p. 818**):
$$\theta\approx\frac{\lambda}{\Lambda}\qquad(19.1\text{-}42)$$
Deflexión a $+\theta$ o $-\theta$ según el haz acústico viaje hacia arriba o abajo; onda acústica **estacionaria**
→ ambas direcciones. $\theta\approx\lambda/\Lambda$ es el ángulo de deflexión de una **rejilla de difracción**
de período Λ (Ejercicio 2.4-5): el haz acústico delgado es una **rejilla de fase delgada** que también difracta a
órdenes superiores $\pm2\theta,\pm3\theta,\ldots$ (Fig. 19.1-11a). Interpretación cuántica: un fotón + dos fonones
→ fotón de segundo orden, $\mathbf k_r=\mathbf k\pm2\mathbf q$ (Fig. 19.1-11b), $\omega_r=\omega\pm2\Omega$;
igual para órdenes superiores. Esta interacción con un haz sonoro *delgado y perpendicular* se llama dispersión
de **Raman–Nath** o **Debye–Sears** (nota al pie: Born & Wolf, *Principles of Optics*, 7.ª ed., cap. 12).

### 19.2 Acousto-Optic Devices (p. 819)

#### 19.2A Modulators (p. 819)

Para sonido débil la luz reflejada $\propto I_s$: con un transductor acústico controlado eléctricamente se
obtiene un **modulador analógico lineal** (Fig. 19.2-1a). Con potencia alta hay saturación y reflexión casi
total (Fig. 19.1-4): **conmutador óptico** que enciende/apaga la luz reflejada y apaga/enciende la transmitida
(Fig. 19.2-1b).

**Ancho de banda de modulación (p. 819–821).** Onda acústica de frecuencia $f_0$ modulada en amplitud con
señal de ancho de banda $B$ → componentes en $f_0\pm B$ (Fig. 19.2-2). Si luz y sonido son ondas planas,
la componente de frecuencia $f$ corresponde al ángulo de Bragg
$$\theta=\sin^{-1}\frac{\lambda}{2\Lambda}=\sin^{-1}\frac{f\lambda}{2v_s}\approx\frac{\lambda}{2v_s}f\qquad(19.2\text{-}1)$$
Para $\theta$ fijo, la luz interactúa con **una sola** componente armónica (Fig. 19.2-3): la onda reflejada es
monocromática a $\nu+f$ y **no modulada** → ancho de banda del modulador = 0 en el caso ideal.
Para lograr ancho de banda $B$ se usa un haz óptico de anchura $D$ y divergencia $\delta\theta=\lambda/D$ con
sonido plano: cada componente de frecuencia encuentra su ángulo de Bragg (Fig. 19.2-4). La banda $f_0\pm B$
se cubre con
$$\delta\theta\approx\frac{(2\pi/v_s)B}{2\pi/\lambda}=\frac{\lambda}{v_s}B\qquad(19.2\text{-}2)$$
$$B=v_s\frac{\delta\theta}{\lambda}=\frac{v_s}{D}\qquad(19.2\text{-}3)$$
**Recuadro (p. 820), Bandwidth:**
$$B=\frac1T,\qquad T=\frac{D}{v_s}\qquad(19.2\text{-}4)$$
$T$ = tiempo de tránsito del sonido a través de la cintura del haz de luz: se necesita $T$ para cambiar la
amplitud del sonido en toda la región de interacción → tasa máxima de modulación $1/T$. Para más ancho de banda,
**enfocar la luz a un diámetro pequeño** (p. 821).

> **Ejercicio 19.2-1, Parámetros de moduladores acusto-ópticos (p. 821).** Determinar ángulo de Bragg y
> ancho de banda máximo de: **Modulador 1** — cuarzo fundido ($n=1.46$, $v_s=6$ km/s), $f=50$ MHz, He–Ne
> $\lambda_o=633$ nm, divergencia $\delta\theta=1$ mrad. **Modulador 2** — telurio ($n=4.8$, $v_s=2.2$ km/s),
> $f=100$ MHz, láser CO₂ $\lambda_o=10.6$ µm, anchura de haz $D=1$ mm. (Sin solución en el texto.)

#### 19.2B Scanners (p. 821)

Relación lineal entre ángulo de deflexión $2\theta$ y frecuencia sonora:
$$2\theta\approx\frac{\lambda}{v_s}f\qquad(19.2\text{-}5)$$
($\sin\theta\approx\theta$). Dificultad: $\theta$ es a la vez ángulo de incidencia y de reflexión; para cambiar
la reflexión hay que cambiar simultáneamente la incidencia y $f$: se logra **inclinando el haz sonoro** con un
*phased array* de transductores con fases relativas (Fig. 19.2-5), sincronizado con el modulador FM (p. 821–822).
Alternativa: haz sonoro con divergencia angular ≥ rango de barrido; al cambiar $f$ la luz selecciona la
componente acústica con la dirección adecuada (eficiencia baja).

**Ángulo de barrido (p. 822).** Con $f$ de $f_0$ a $f_0+B$, la deflexión $2\theta=(\lambda/v_s)f$ barre
(**recuadro, Scan Angle**):
$$\Delta\theta=\frac{\lambda}{v_s}B\qquad(19.2\text{-}6)$$
suponiendo $\delta\theta_s=\Lambda/D_s\ge\Delta\theta$. Ángulos de barrido grandes con materiales de $v_s$ pequeña.
Fig. 19.2-6.

**Número de puntos resolubles (p. 822–823).** Si la luz tiene anchura angular $\delta\theta=\lambda/D$ y
$\delta\theta\ll\delta\theta_s$, el haz deflectado también tiene anchura $\delta\theta$:
$$N=\frac{\Delta\theta}{\delta\theta}=\frac{(\lambda/v_s)B}{\lambda/D}=\frac{D}{v_s}B\qquad(19.2\text{-}7)$$
**Recuadro (p. 823), Number of Resolvable Spots:**
$$N=TB\qquad(19.2\text{-}8)$$
$B$ = ancho de banda del modulador FM que genera el sonido, $T=D/v_s$ tiempo de tránsito del sonido por el haz
de luz (Fig. 19.2-7). $N$ = **producto tiempo–ancho de banda** = grados de libertad del dispositivo. Para
aumentar $N$ conviene $T$ grande — lo opuesto al modulador, donde $B=1/T$ pide $T$ pequeño.

> **Ejercicio 19.2-2, Parámetros de un escáner acusto-óptico (p. 823).** Escáner de cuarzo fundido ($v_s=6$ km/s,
> $n=1.46$) para He–Ne ($\lambda_o=633$ nm), $f$ barrida de 40 a 60 MHz. ¿A qué anchura enfocar el haz para
> $N=100$? ¿Ángulo de barrido $\Delta\theta$? ¿Efecto de usar un material con sonido más lento (flint,
> $v_s=3.1$ km/s)? (Sin solución en el texto.)

**Escáner como analizador de espectro (p. 823–824).** Un sonido con espectro de varias frecuencias dispersa la
luz en direcciones distintas, con intensidad proporcional a la potencia de cada componente (Fig. 19.2-8:
$f_1+f_2+f_3$ → $\theta_1,\theta_2,\theta_3$).

#### 19.2C Space Switches (p. 824)

Celda como **conmutador espacial** (Sec. 23.3) que enruta uno o más haces a direcciones seleccionadas:
- Frecuencia acústica = una de $N$ valores $f_1,\dots,f_N$ → un haz a una de $N$ direcciones $\theta_1,\dots,\theta_N$
  (Fig. 19.2-9, con lente que enfoca a puntos).
- Sonido con dos frecuencias $f_1$, $f_2$ simultáneas → el haz se refleja a $\theta_1$ y $\theta_2$ a la vez
  (Fig. 19.2-10); con $M$ frecuencias, a $M$ direcciones (el analizador de espectro es un ejemplo).
- Celda dividida en dos segmentos (p. 825): señal eléctrica *frequency-shift-keyed* (pulso a $f_1$ y luego a
  $f_2$, cada uno de duración $T/2$, $T=W/v_s$, $W$ longitud de la celda): el haz superior va a $\theta_1$ y el
  inferior a $\theta_2$ (Fig. 19.2-11).
- Celda en $N$ segmentos con la misma $f$ pero distinta amplitud → **modulador espacial de luz (SLM)** que modula
  las intensidades de $N$ haces (Fig. 19.2-12; señal AM; útil en procesamiento óptico, Sec. 20.1E).
- Arquitectura más general: $L$ segmentos, cada uno con $M$ frecuencias → conmutador de acceso aleatorio de $L$
  haces a $M$ direcciones simultáneamente (Fig. 19.2-13).

**Capacidad de interconexión (p. 826).** Límite superior (**recuadro, Interconnection Capacity**):
$$ML\le N\qquad(19.2\text{-}9)$$
con $N=TB$. Justificación: $L$ segmentos de duración $T/L$ tienen incertidumbre de frecuencia inherente $L/T$ Hz;
las $M$ componentes deben separarse al menos eso dentro de $B$: $M(L/T)\le B$. Un solo haz ($L=1$) llega a $N=TB$
puntos; dos haces, a lo sumo $N/2$ cada uno, etc. Fig. 19.2-14: diagrama tiempo–frecuencia con $N=20$:
(a) escáner — 1 segmento temporal con $N$ frecuencias; (b) SLM — $N$ segmentos temporales con 1 frecuencia;
(c) conmutador — $L=5$ segmentos con $M=4$ frecuencias.

#### 19.2D Filters, Frequency Shifters, and Isolators (p. 827)

- **Filtros acusto-ópticos sintonizables:** $\sin\theta=\lambda/2\Lambda$; fijados $\theta$ y $\Lambda$, solo se
  refleja $\lambda=2\Lambda\sin\theta$ → filtro para luz de espectro amplio, sintonizable por $\theta$ o por $f$.
  > **Ejercicio 19.2-3, Poder de resolución de un filtro acusto-óptico (p. 827).** Mostrar que el poder
  > resolutivo espectral $\lambda/\Delta\lambda$ es $fT$ ($f$ frecuencia del sonido, $T$ tiempo de tránsito,
  > $\Delta\lambda$ mínima diferencia resoluble). (Sin solución en el texto.)
- **Desplazadores de frecuencia:** la luz reflejada está desplazada en ±$f$; útil en heterodinaje óptico
  (mezcla con oscilador local de distinta frecuencia, batido — Sec. 2.6B, detección Sec. 24.5), moduladores FM
  ópticos, velocimetría láser Doppler.
- **Aisladores ópticos:** válvula de un solo sentido (Sec. 6.6C, 23.1C), p. ej. para proteger láseres de
  semiconductor de la luz reflejada (ruido). Luz upshifted reflejada por un espejo vuelve a la celda, sufre una
  segunda difracción de Bragg con otro upshift → regresa con $2f$ de diferencia y un filtro la bloquea; incluso sin
  filtro, el láser puede ser insensible a esa luz desplazada (Fig. 19.2-15: fuente, filtro, celda, espejo).

### *19.3 Acousto-Optics of Anisotropic Media (p. 828)

Generaliza la teoría escalar a medios anisótropos y a la polarización de luz y sonido.

**Ondas acústicas en materiales anisótropos (p. 828).** Onda acústica = onda de deformación. Con
$\mathbf u=(u_1,u_2,u_3)$ el desplazamiento de las moléculas en $\mathbf x=(x_1,x_2,x_3)$, el tensor de deformación
es simétrico: $s_{ij}=\tfrac12(\partial u_i/\partial x_j+\partial u_j/\partial x_i)$, $i,j=1,2,3$. $s_{33}=\partial u_3/\partial x_3$
= deformación de tracción (*tensile*) en $z$ [Fig. 19.3-1a]; $s_{13}$ = cizalla (*shear*) [Fig. 19.3-1b].

> **Ejemplo 19.3-1, Onda acústica longitudinal (p. 828).** $u_1=u_2=0$, $u_3=A_0\sin(\Omega t-qz)$ →
> solo $s_{33}=S_0\cos(\Omega t-qz)$ (19.3-1), con $S_0=-qA_0$. Estira en $z$ y viaja en $z$: longitudinal.
>
> **Ejemplo 19.3-2, Onda acústica transversal (p. 828).** $u_1=A_0\sin(\Omega t-qz)$, $u_2=u_3=0$ →
> solo $s_{13}=s_{31}=S_0\cos(\Omega t-qz)$ (19.3-2), con $S_0=-\tfrac12qA_0$. Viaja en $z$, vibra en $x$:
> transversal (cizalla).

Las velocidades longitudinal y transversal son características del medio y dependen en general de la dirección
de propagación.

**Efecto fotoelástico (p. 829).** Medio anisótropo descrito por el tensor de impermeabilidad eléctrica
$\boldsymbol\eta=\epsilon_o\boldsymbol\epsilon^{-1}$ (Sec. 6.3) → elipsoide de índices. Con deformación,
$\eta_{ij}=\eta_{ij}(s_{kl})$ (**efecto fotoelástico**); expansión de Taylor a primer orden:
$$\eta_{ij}(s_{kl})\approx\eta_{ij}(0)+\sum_{kl}\mathfrak{p}_{ijkl}s_{kl},\qquad i,j,l,k=1,2,3\qquad(19.3\text{-}3)$$
$\mathfrak{p}_{ijkl}=\partial\eta_{ij}/\partial s_{kl}$ = **tensor elasto-óptico** (*strain-optic tensor*), rango 4.
Por simetría de $\eta_{ij}$ y $s_{kl}$, se contraen $(i,j)\to I=1..6$ y $(k,l)\to K=1..6$ (Tabla 20.2-1) →
matriz 6×6 $\mathfrak p_{IK}$. Para un **cristal cúbico** (19.3-4, *Strain-Optic Matrix, Cubic Crystal*):
$$\mathfrak p_{IK}=\begin{bmatrix}\mathfrak p_{11}&\mathfrak p_{12}&\mathfrak p_{12}&0&0&0\\ \mathfrak p_{12}&\mathfrak p_{11}&\mathfrak p_{12}&0&0&0\\ \mathfrak p_{12}&\mathfrak p_{12}&\mathfrak p_{11}&0&0&0\\ 0&0&0&\mathfrak p_{44}&0&0\\ 0&0&0&0&\mathfrak p_{44}&0\\ 0&0&0&0&0&\mathfrak p_{44}\end{bmatrix}\qquad(19.3\text{-}4)$$
También válida para medios **isótropos** con la restricción $\mathfrak p_{44}=\tfrac12(\mathfrak p_{11}+\mathfrak p_{12})$
(solo dos coeficientes independientes).

> **Ejemplo 19.3-3, Onda longitudinal en cristal cúbico (p. 829–830).** La onda del Ej. 19.3-1 viaja a lo
> largo de un eje de un cristal cúbico de índice $n$. Sustituyendo (19.3-1) y (19.3-4) en (19.3-3):
> $$\eta_{11}=\eta_{22}=\frac1{n^2}+\mathfrak p_{12}S_0\cos(\Omega t-qz)\qquad(19.3\text{-}5)$$
> $$\eta_{33}=\frac1{n^2}+\mathfrak p_{11}S_0\cos(\Omega t-qz)\qquad(19.3\text{-}6)$$
> $$\eta_{ij}=0,\quad i\ne j\qquad(19.3\text{-}7)$$
> El cristal, inicialmente isótropo, se vuelve **uniaxial** con eje óptico en $z$ (dirección del sonido):
> $$\frac1{n_o^2}=\frac1{n^2}+\mathfrak p_{12}S_0\cos(\Omega t-qz)\qquad(19.3\text{-}8)$$
> $$\frac1{n_e^2}=\frac1{n^2}+\mathfrak p_{11}S_0\cos(\Omega t-qz)\qquad(19.3\text{-}9)$$
> Con $(1+\Delta)^{-1/2}\approx1-\Delta/2$ ($|\Delta|\ll1$):
> $$n_o\approx n-\tfrac12n^3\mathfrak p_{12}S_0\cos(\Omega t-qz)\qquad(19.3\text{-}10)$$
> $$n_e\approx n-\tfrac12n^3\mathfrak p_{11}S_0\cos(\Omega t-qz)\qquad(19.3\text{-}11)$$
> La forma del elipsoide cambia periódicamente en espacio y tiempo pero los ejes principales no (Fig. 19.3-2:
> de esfera a elipsoide de revolución con eje $z$, mostrado para $\Omega t-qx=0,\pi/2,\pi$).

> **Ejercicio 19.3-1, Onda transversal en cristal cúbico (p. 830).** La onda del Ej. 19.3-2 viaja a lo largo
> de un eje del cristal cúbico. Mostrar que el cristal se vuelve **biaxial** con índices principales
> $$n_1\approx n-\tfrac12n^3\mathfrak p_{44}S_0\cos(\Omega t-qz)\qquad(19.3\text{-}12)$$
> $$n_2\approx n\qquad(19.3\text{-}13)$$
> $$n_3\approx n+\tfrac12n^3\mathfrak p_{44}S_0\cos(\Omega t-qz)\qquad(19.3\text{-}14)$$

En el Ej. 19.3-3 y el Ejerc. 19.3-1 el sonido altera los valores principales pero no las direcciones
principales; en general (otras direcciones/polarizaciones) cambian ambos (p. 830).

**Difracción de Bragg en medio anisótropo (p. 830–831).** Mismos principios que 19.1 pero las ondas incidente y
reflejada viajan con velocidades distintas → los ángulos de incidencia y reflexión **no tienen que ser iguales**.
Condición de conservación de momento (ajuste de fase):
$$\mathbf k_r=\mathbf k+\mathbf q\qquad(19.3\text{-}15)$$
con $k=(2\pi/\lambda_o)n$, $k_r=(2\pi/\lambda_o)n_r$, $q=2\pi/\Lambda$; $n$ y $n_r$ índices de la onda incidente y
reflejada. Con $\theta$ y $\theta_r$ los ángulos de incidencia y reflexión (Fig. 19.3-3), componentes $z$ y $x$:
$$\frac{2\pi}{\lambda_o}n_r\cos\theta_r=\frac{2\pi}{\lambda_o}n\cos\theta\qquad(19.3\text{-}16)$$
$$\frac{2\pi}{\lambda_o}n_r\sin\theta_r+\frac{2\pi}{\lambda_o}n\sin\theta=\frac{2\pi}{\Lambda}\qquad(19.3\text{-}17)$$
$$n_r\cos\theta_r=n\cos\theta\qquad(19.3\text{-}18a)$$
$$n_r\sin\theta_r+n\sin\theta=\frac{\lambda_o}{\Lambda}\qquad(19.3\text{-}18b)$$
Dados $\lambda_o$ y $\Lambda$ se resuelven $\theta$ y $\theta_r$; $n$ y $n_r$ dependen en general de $\theta$ y
$\theta_r$ vía el elipsoide de índices del cristal no perturbado.
Caso **colineal** ($\theta=\pm\pi/2$, $\theta_r=\pi/2$; + reflexión trasera, − reflexión frontal, Fig. 19.3-4):
$$n_r\pm n=\frac{\lambda_o}{\Lambda}\qquad(19.3\text{-}19)$$
Reflexión trasera (+): requiere $\Lambda<\lambda_o$, improbable salvo sonido de muy alta frecuencia.
**Reflexión frontal** (−): incidente y reflejada deben tener **polarizaciones distintas** para que $n_r\ne n$
(p. 831). (Base del Prob. 19.3-2 y de los filtros acusto-ópticos colineales.)

### Reading List (p. 832)

Libros: Poon & Kim (*Engineering Optics with MATLAB*, 2006); Wolfe (*Imaging Phonons*, 2005); Musgrave (*Crystal
Acoustics*, 1970/2003); **Yariv & Yeh, *Optical Waves in Crystals* (Wiley 1984/2003)**; Royer & Dieulesaint
(*Elastic Waves in Solids* vol. 2, 2000); Nye (*Physical Properties of Crystals*, 1957/2001); **Born & Wolf,
*Principles of Optics*, 7.ª ed. 2002, cap. 12**; Korpel (*Acousto-Optics*, 1988/1997); Berg & Pellegrino (eds.,
*Acousto-Optic Signal Processing*, 1983/1996); Goutzoulis & Pape (eds., 1994); Gusev & Karabutov (*Laser
Optoacoustics*, 1993); Scott (1992); Xu & Stroud (*Acousto-Optic Devices*, Wiley 1992); Bunkin et al. (*Lasers in
Acoustics*, 1991); Das & De Cusatis (1991); Tsai (*Guided-Wave Acoustooptics*, Springer 1990); Magdich & Molchanov
(1989); Gottlieb, Ireland & Ley (1983); Narasimhamurty (*Photoelastic and Electro-Optic Properties of Crystals*,
1981); Nelson (1979); Sapriel (*Acousto-Optics*, Wiley 1979); Berry (*The Diffraction of Light by Ultrasound*, 1966).
Artículos: Korpel (ed.), *Selected Papers on Acousto Optics*, SPIE Milestone 16, 1990; número especial de
*Proc. IEEE* vol. 69, n.º 1, 1981.

## Tablas y datos numéricos útiles

| Material / parámetro | Valor | Dónde |
|---|---|---|
| Vidrio flint extra-denso: $\varrho$ | $6.3\times10^3$ kg/m³ | Ej. 19.1-1, p. 807 |
| Vidrio flint extra-denso: $v_s$ | 3.1 km/s | Ej. 19.1-1, p. 807; Ejerc. 19.2-2, p. 823 |
| Vidrio flint extra-denso: $n$ | 1.92 | Ej. 19.1-1, p. 807 |
| Vidrio flint extra-denso: $\mathfrak p$ | 0.25 | Ej. 19.1-1, p. 807 |
| Vidrio flint extra-denso: $\mathcal M$ | $1.67\times10^{-14}$ m²/W | Ej. 19.1-1, p. 807 |
| $\Delta n_0$ con $I_s=10$ W/cm² (flint) | $2.89\times10^{-5}$ | Ej. 19.1-1, p. 807 |
| Vidrio flint (Ej. 19.1-2): $v_s$, $n$ | 3 km/s, 1.95 | p. 809 |
| $\theta_{\mathcal B}$ (633 nm, 100 MHz, flint) | 5.4 mrad ≈ 0.31° interno, 0.61° externo | p. 809 |
| $\theta_{\mathcal B}$ (633 nm, 1 GHz, flint) | 3.1° | p. 809 |
| $\mathcal R$, $\mathcal R_e$ (flint, 10 W/cm², $L/\sin\theta=1$ mm) | 0.0206, 0.0205 | Ej. 19.1-3, p. 813 |
| $\mathcal R$, $\mathcal R_e$ (flint, 100 W/cm²) | 0.206, 0.192 | Ej. 19.1-3, p. 813 |
| Cuarzo fundido: $n$, $v_s$ | 1.46, 6 km/s | Ejerc. 19.2-1/19.2-2, p. 821, 823 |
| Telurio: $n$, $v_s$ | 4.8, 2.2 km/s | Ejerc. 19.2-1, p. 821 |
| LiNbO₃: $n$, $v_s$ | 2.3, 7.4 km/s | Prob. 19.1-4, p. 833 |
| Cristal uniaxial Prob. 19.3-2: $n_e$, $n_o$ | 2.200, 2.286 (λ₀ = 633 nm) | p. 833 |
| Razón $f/\nu$ típica | ≥ 5 órdenes de magnitud | p. 808, 811 |
| Divergencias de haz | rect. $\lambda/D$; circular $1.22\lambda/D$; gaussiano $\lambda/\pi W_0\approx0.64\lambda/D$ | p. 816 |

Fórmulas de diseño rápidas (todas en el libro, páginas indicadas):
- $\Lambda=v_s/f$; $\theta_{\mathcal B}\approx\lambda_o f/(2nv_s)$ (p. 809, 820).
- Anchura angular de Bragg $\approx\lambda/2L$ (p. 810).
- Modulador: $B=1/T=v_s/D$ (p. 820). Escáner: $\Delta\theta=\lambda B/v_s$, $N=TB=DB/v_s$ (p. 822–823).
- Conmutador: $ML\le TB$ (p. 826). Filtro: $\lambda/\Delta\lambda=fT$ (Ejerc. 19.2-3, p. 827).
- Reflectancia: $\mathcal R=\dfrac{\pi^2}{2\lambda_o^2}\left(\dfrac{L}{\sin\theta}\right)^2\mathcal M I_s$, $\mathcal R_e=\sin^2\sqrt{\mathcal R}$ (p. 812).

## Problemas al final del capítulo (p. 832–833)

- **19.1-1 Diffraction of Light from Various Periodic Structures.** Discutir la difracción de una onda plana de
  longitud de onda λ (configuración geométrica y corrimiento(s) de frecuencia) por: (a) onda acústica viajera
  de longitud Λ; (b) onda acústica estacionaria de longitud Λ; (c) medio transparente de índice graduado con
  variación sinusoidal de período Λ; (d) medio estratificado de capas alternas de dos materiales, período Λ
  (Sec. 7.1C).
- ***19.1-2 Bragg Diffraction as a Scattering Process.** Con la fuente de dispersión de (19.1-32),
  $\mathcal S=\mathrm{Re}\{S_r(\mathbf r)e^{j\omega_rt}\}$, $S_r(\mathbf r)=-(\Delta n_0/n)k_r^2A\exp(-j\mathbf k_r\cdot\mathbf r)$,
  en la primera aproximación de Born, resolver $\nabla^2E+k^2E=-S$ usando la solución de campo lejano
  (Prob. 21.2-6) $E(\mathbf r)\approx\dfrac{\exp(-jkr)}{4\pi r}\displaystyle\int_V S_r(\mathbf r')\exp(jk\hat{\mathbf r}\cdot\mathbf r')\,d\mathbf r'$
  y obtener la reflectancia de la celda cuando se cumple Bragg; comparar con (19.1-22).
- **19.1-3 Condition for Raman–Nath Diffraction.** Derivar la anchura máxima $D_s$ de un haz acústico de longitud
  Λ que permite difracción de Raman–Nath de luz de longitud λ (Fig. 19.1-10).
- **19.1-4 Combined Acousto-Optic and Electro-Optic Modulation.** Cristal de LiNbO₃ en una cavidad de microondas
  a 3 GHz: por piezoelectricidad se lanza una onda acústica; luz He–Ne (633 nm) se refleja; $n=2.3$,
  $v_s=7.4$ km/s. Hallar el ángulo de Bragg. Como LiNbO₃ también es electro-óptico, el campo modula la fase de la
  luz: dibujar el espectro de la luz reflejada; si el campo es un pulso corto, dibujar el espectro en distintos
  instantes indicando las contribuciones EO y AO.
- **19.2-4 Acousto-Optic Modulation.** Diseñar un sistema que convierta $U(t)=A\exp(j\omega t)$ en una onda
  modulada $A\cos(\Omega t)\exp(j\omega t)$ usando una celda con $s(x,t)=S_0\cos(\Omega t-qx)$. Pista: usar
  reflexiones upshifted y downshifted.
- **19.2-5 Frequency-Shift-Free Bragg Reflector.** Diseñar un sistema acusto-óptico que deflecte la luz sin
  imponer corrimiento de frecuencia. Pista: dos celdas de Bragg.
- ***19.3-2 Front Bragg Diffraction.** Onda acústica transversal de longitud Λ en dirección $x$ en un cristal
  uniaxial ($n_o$, $n_e$, eje óptico en $z$). Derivar la $\lambda_o$ de una onda incidente que viaja en $x$,
  polarizada en $z$, que satisface Bragg frontal; polarización de la onda reflejada; hallar Λ si
  $\lambda_o=633$ nm, $n_e=2.200$, $n_o=2.286$.

(Numeración tal cual aparece en el libro: no hay 19.2-1 a 19.2-3 en la lista de problemas porque esos números
corresponden a los ejercicios del texto; tampoco hay 19.3-1 por la misma razón.)

## Relación con Óptica No Lineal

**Con los temas del curso.**

- **Ondas EM / ajuste de fase.** $\mathbf k_r=\mathbf k+\mathbf q$ (19.1-16, p. 810) y $\omega_r=\omega+\Omega$
  (19.1-17, p. 811) son exactamente conservación de momento y energía: el mismo esquema de *phase matching* que
  aparece en SHG/SFG/DFG con χ⁽²⁾ ($\mathbf k_3=\mathbf k_1+\mathbf k_2$) y en FWM con χ⁽³⁾. El libro lo llama
  explícitamente "phase-matching condition" (p. 813). Los diagramas vectoriales (Figs. 19.1-2, 19.1-5, 19.3-3)
  son los mismos triángulos de $\Delta\mathbf k$ que se dibujan en ONL.
- **Teoría de ondas acopladas (19.1B, p. 814–816).** La derivación es el prototipo de las ecuaciones acopladas
  de ONL: ecuación de onda con fuente $\mathcal S=-\mu_o\partial^2\Delta\mathcal P/\partial t^2$ (19.1-29),
  aproximación de envolvente lenta (SVEA), $dA/dz=j\tfrac12\gamma A_r$ (19.1-36). Compárese con la ecuación de
  onda no lineal de Boyd $\nabla^2\tilde E-\frac{n^2}{c^2}\partial_t^2\tilde E=\mu_0\partial_t^2\tilde P^{NL}$ y con las
  ecuaciones acopladas de SHG. La solución $\cos(\gamma z/2)$, $\sin(\gamma z/2)$ y el intercambio de energía
  (Fig. 19.1-7) son el análogo de la conversión periódica en SHG con $\Delta k=0$. La "primera aproximación de
  Born" ≈ aproximación de bombeo no agotado.
- **Dispersión de Brillouin (tema del curso: Brillouin estimulado en fibras).** La difracción de Bragg por una onda
  acústica *es* dispersión de Brillouin: fotón + fonón → fotón (p. 813–814, Fig. 19.1-6), con corrimiento
  $\pm\Omega$ (Stokes = downshifted (19.1-26), anti-Stokes = upshifted (19.1-17)). Diferencias con SBS: aquí la
  onda acústica es *impuesta* por un transductor (proceso lineal en la luz, $\mathcal R\propto I_s$); en SBS la
  onda acústica la genera la propia luz por **electrostricción** (la inversa del efecto fotoelástico (19.1-3)),
  lo que hace al proceso no lineal (χ⁽³⁾ efectivo) y da ganancia $g_B\propto\mathfrak p^2 n^7/(\varrho v_s\lambda^2\Delta\nu_B)$
  — nótese la misma combinación $\mathfrak p^2n^6/\varrho v_s$ de la figura de mérito (19.1-7). La geometría
  colineal de 19.3 (19.3-19, p. 831) con reflexión *trasera* ($n_r+n=\lambda_o/\Lambda$ → $\Lambda=\lambda/2$,
  $\Omega_B=2nv_s\omega/c$) es exactamente la geometría de SBS en fibras (contrapropagante, corrimiento
  ≈ 11 GHz a 1550 nm en sílice); el libro dice que requiere "very-high-frequency acoustic waves", que es
  justo lo que SBS genera. La anchura de la condición de Bragg $\lambda/2L$ (p. 810) ↔ ancho de banda de
  ganancia Brillouin.
- **Raman.** La interpretación con fonones (p. 813) se extiende a Raman (fonones ópticos en lugar de acústicos);
  las ecuaciones acopladas (19.1-36) tienen la misma estructura que las de bombeo–Stokes.
- **Índice dependiente de la intensidad / χ⁽³⁾.** $\Delta n_0=\sqrt{\mathcal M I_s/2}$ (19.1-6) es un cambio de
  índice inducido por una onda (acústica); el efecto Kerr es $\Delta n=n_2I$ inducido por la propia luz. Útil
  como comparación de órdenes de magnitud ($\Delta n_0\sim3\times10^{-5}$ con 10 W/cm² de sonido, p. 807).
- **Polarización y cristales (19.3).** Tensor de impermeabilidad $\boldsymbol\eta$, elipsoide de índices,
  contracción de índices $(ij)\to I$ y matriz 6×6 (19.3-4): el mismo formalismo que el tensor electro-óptico
  $r_{IJ}$ (cap. 20) y el tensor $d_{il}$ de χ⁽²⁾. Cristal cúbico → uniaxial (Ej. 19.3-3) o biaxial
  (Ejerc. 19.3-1) bajo deformación: birrefringencia inducida, relevante para entender birrefringencia
  inducida en guías por *stress*.
- **Absorción/dispersión, haz gaussiano.** $\mathcal R\propto\omega^4$ (p. 812, 815) como en dispersión Rayleigh;
  descomposición angular de haces (19.1-39, p. 816) con divergencia gaussiana $\lambda/\pi W_0$.
- **Pulsos / productos tiempo–ancho de banda.** $B=1/T$, $N=TB$ (p. 820–823) y la incertidumbre $L/T$ Hz de
  un segmento de duración $T/L$ (p. 826) son la relación tiempo–ancho de banda que reaparece en pulsos y GVD.
- **Dispositivos.** Los AOM son los moduladores/desplazadores de frecuencia estándar de laboratorio
  (heterodinaje, p. 827; *mode-locking* activo; *pulse pickers*); útil para interpretar montajes de SPM/solitones
  o Brillouin donde se usa un AOM para generar el desplazamiento de ~Ω.

**Con el proyecto final (anillos add-drop en Si₃N₄, dispersión de guías, supercontinuo, sensado de índice).**

- **Reflectores de Bragg y resonancias.** La condición $\sin\theta_{\mathcal B}=\lambda/2\Lambda$ y la anchura
  $\lambda/2L$ (p. 806–810) son las de una rejilla de Bragg en guía (caso colineal: $\Lambda=\lambda/2n_{\rm eff}$);
  es el mismo lenguaje de ajuste de fase que el acoplamiento anillo–bus y la resonancia $m\lambda=n_{\rm eff}L$.
  La teoría de ondas acopladas 19.1B es la base de los modelos de acoplador direccional y de rejillas en guía.
- **Sensado de índice.** Un cambio $\Delta n_0\sim10^{-5}$ (p. 807) desplaza la condición de Bragg; es el mismo
  orden de magnitud de sensibilidad que se busca con el refractómetro de anillo (analito 1.33 → 1.37 como
  cladding); el argumento de "anchura $\lambda/2L$ ⇒ selectividad" es análogo al de $Q$ alto ⇒ mejor resolución
  del sensor.
- **SBS en Si₃N₄ / supercontinuo.** En guías de nitruro de silicio bombeadas con pulsos para supercontinuo, el
  Brillouin estimulado es un posible limitador de potencia en régimen CW/cuasi-CW; los parámetros que gobiernan
  su ganancia ($\mathfrak p$, $\varrho$, $v_s$, $n$, (19.1-7)) son los de este capítulo. También existen
  dispositivos acusto-ópticos integrados (p. ej. en AlN/LiNbO₃) que usan la ecuación (19.3-18) con $n_r\ne n$ para
  conversión de modos.
- **Birrefringencia inducida por tensión.** La matriz fotoelástica (19.3-4) permite estimar cómo el *stress*
  residual del Si₃N₄ sobre SiO₂ cambia $n_{TE}$ vs. $n_{TM}$, lo que afecta la dispersión de la guía y la
  posición de las resonancias del anillo.
