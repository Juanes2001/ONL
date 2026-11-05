# Capítulo 7 — Photonic-Crystal Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 243–288 (PDF 265–310). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 7.
Convención del libro: dependencia temporal $e^{j\omega t}$, $j=\sqrt{-1}$, ondas que avanzan en $+z$ como
$\exp(-jkz)$; amplitudes complejas en negrita ($\mathbf{E}$, $\mathbf{H}$) o itálica ($U$); matrices en
negrita sans ($\mathbf{M}$, $\mathbf{S}$). Transmitancia/reflectancia de **amplitud**: $\mathrm{t}$, $\mathrm{r}$;
de **intensidad**: $\mathcal{T}=|\mathrm{t}|^2$, $\mathcal{R}=|\mathrm{r}|^2$. $k_o=\omega/c_o$ (vacío),
$c_o$ = velocidad de la luz en vacío, $\epsilon_o$ = permitividad del vacío. Unidades SI.

---

## Resumen del capítulo

El capítulo trata la óptica de medios **volumétricos** (bulk) formados por capas dieléctricas múltiples y
por estructuras periódicas 1D, 2D y 3D (cristales fotónicos). Parte de las ecuaciones de Helmholtz
generalizadas para medios inhomogéneos (p. 245) y desarrolla en §7.1 un formalismo matricial — matriz de
transferencia de onda $\mathbf{M}$ y matriz de scattering $\mathbf{S}$ — que permite calcular la
transmitancia y reflectancia de cualquier pila de capas por simple producto de matrices (pp. 246–253);
lo aplica al etalón Fabry-Perot (finesse, rango espectral libre, transmitancia en función de la
frecuencia y del ángulo, pp. 254–257) y a la rejilla de Bragg de $N$ segmentos, donde aparece la
"reflexión total" sobre bandas espectrales enteras (stop bands) gracias al factor de interferencia
$\Psi_N=\sin N\Phi/\sin\Phi$ (pp. 257–264). En §7.2 se pasa al medio periódico infinito: los modos son
ondas de Bloch $p_K(z)e^{-jKz}$ (p. 265), la relación de dispersión $\cos(K\Lambda)=\mathrm{Re}\{1/\mathrm{t}\}$
sale de un problema de autovalores $2\times2$ de la celda unitaria (pp. 268–272), y aparece la
estructura de bandas con **bandgaps fotónicos**, el índice efectivo y el índice de grupo (pp. 272–274);
un enfoque alternativo de Fourier (pp. 274–277) da la condición de acoplamiento fuerte
$\omega\bar n/c_o\approx|K+mg|$ (condición de ajuste de fase) y el ancho del primer gap
$\omega_\pm=\omega_{\mathcal B}\sqrt{1\pm|\eta_1|/\eta_0}$; finalmente se estudian las fronteras entre medio periódico
y homogéneo y el **reflector omnidireccional** (pp. 277–279). §7.3 generaliza a 2D y 3D (retículos,
retículo recíproco, zona de Brillouin irreducible, bandgap completo, ejemplos: huecos en retículo
triangular, esferas en retículo diamante, Yablonovite, woodpile, holes-and-poles; pp. 279–286).

---

## Secciones

### Introducción del capítulo (p. 244–246)

- Fig. 7.0-1 (p. 244): estructuras fotónicas periódicas 1D (pila de láminas), 2D (barras paralelas) y 3D
  (retículo de cubos/esferas/huecos).
- Idea central (p. 244): las ondas ópticas interactúan de forma especial con medios periódicos cuando el
  periodo es del orden de $\lambda$; aparecen bandas espectrales en las que la onda no puede propagarse
  sin atenuación severa: **photonic bandgaps**, análogos a la reflexión total interna pero para todas las
  direcciones; se deben a la interferencia destructiva de las ondas dispersadas hacia adelante y se
  extienden sobre bandas finitas, no solo frecuencias aisladas. Analogía con las bandas de energía de
  los electrones en sólidos cristalinos → nombre **photonic crystals**.
- Para medio dieléctrico inhomogéneo con $\epsilon(\mathbf r)$ (ver §5.2B del libro), la onda armónica de
  frecuencia $\omega$ satisface las **ecuaciones de Helmholtz generalizadas** (recuadro, p. 245):

$$\eta(\mathbf r)\,\nabla\times(\nabla\times\mathbf E)=\frac{\omega^2}{c_o^2}\mathbf E, \tag{7.0-1}$$

$$\nabla\times[\eta(\mathbf r)\,\nabla\times\mathbf H]=\frac{\omega^2}{c_o^2}\mathbf H, \tag{7.0-2}$$

  con $\eta(\mathbf r)=\epsilon_o/\epsilon(\mathbf r)$ la **impermeabilidad eléctrica** (§6.3A). Son problemas de
  autovalores: el operador diferencial aplicado al campo da una constante ($\omega^2/c_o^2$, los autovalores)
  por el campo; las autofunciones son los modos. Se trabaja con la ecuación de $\mathbf H$ (7.0-2) porque su
  operador es hermítico (razón explicada en §7.2C y §7.3, p. 275 nota al pie).
- Medios multicapa: $\epsilon(\mathbf r)$ constante a trozos → se resuelve con ondas en medios homogéneos +
  condiciones de frontera (Fresnel). Medios periódicos: $\epsilon$, $\eta$ periódicos → la constante de
  propagación deja de ser proporcional a $\omega$; los modos no son ondas planas $\exp(-j\mathbf k\cdot\mathbf r)$
  sino **modos de Bloch**: ondas viajeras moduladas por ondas estacionarias (p. 245).
- Cristales fotónicos en otros capítulos (p. 245–246): espejos "perfectos" dieléctricos; guías de onda
  (§8.4); fibras "holey" (§9.4); microrresonadores de cristal fotónico (§10.4D y §17.4C).
- Supuesto en todo el capítulo: medios isótropos, permitividad escalar $\epsilon$ (p. 245).

---

### 7.1 Optics of Dielectric Layered Media (p. 246)

#### 7.1A Matrix Theory of Multilayer Optics (p. 246)

**Planteamiento (p. 246).** Una onda plana normalmente incidente sobre un medio por capas sufre
reflexiones y transmisiones múltiples en cada frontera (Fig. 7.1-1a). En vez de seguir las infinitas
"micro" reflexiones, el enfoque "macro" reconoce que en cada capa solo hay dos tipos de onda: la
*colectada* hacia adelante $U^{(+)}$ y la *colectada* hacia atrás $U^{(-)}$ (Fig. 7.1-1b). Determinar la
propagación equivale a determinar las amplitudes de ese par en todas partes.

**Matriz de transferencia de onda (wave-transfer matrix, o transmission matrix), p. 246–247.** Entre
dos planos 1 y 2:

$$\begin{bmatrix}U_2^{(+)}\\ U_2^{(-)}\end{bmatrix}=\begin{bmatrix}A&B\\ C&D\end{bmatrix}\begin{bmatrix}U_1^{(+)}\\ U_1^{(-)}\end{bmatrix}. \tag{7.1-1}$$

$\mathbf M$ depende solo de las propiedades ópticas del medio entre los dos planos. Para una cascada de
elementos $\mathbf M_1,\mathbf M_2,\dots,\mathbf M_N$ numerados de izquierda a derecha (p. 247):

$$\mathbf M=\mathbf M_N\cdots\mathbf M_2\mathbf M_1, \tag{7.1-2}$$

idéntica a la fórmula de cascada de matrices de rayos (1.4-10). **Ojo al orden inverso.**

**Matriz de scattering ($\mathbf S$), p. 247.** Expresa ondas *salientes* en función de las *entrantes*:

$$\begin{bmatrix}U_2^{(+)}\\ U_1^{(-)}\end{bmatrix}=\begin{bmatrix}\mathrm t_{12}&\mathrm r_{21}\\ \mathrm r_{12}&\mathrm t_{21}\end{bmatrix}\begin{bmatrix}U_1^{(+)}\\ U_2^{(-)}\end{bmatrix}. \tag{7.1-3}$$

- $\mathrm t_{12}$, $\mathrm r_{12}$: transmitancia y reflectancia de amplitud hacia adelante (onda que incide desde la
  izquierda, "de medio 1 a medio 2"); $\mathrm t_{21}$, $\mathrm r_{21}$: hacia atrás (onda desde la derecha).
- Verificación: si $U_2^{(-)}=0$ entonces $U_2^{(+)}=\mathrm t_{12}U_1^{(+)}$ y $U_1^{(-)}=\mathrm r_{12}U_1^{(+)}$;
  si $U_1^{(+)}=0$ entonces $U_2^{(+)}=\mathrm r_{21}U_2^{(-)}$ y $U_1^{(-)}=\mathrm t_{21}U_2^{(-)}$.
- Ventaja de $\mathbf S$: elementos con significado físico directo. Desventaja: la $\mathbf S$ de una cascada
  **no** es el producto de las $\mathbf S$ individuales (p. 247). Procedimiento práctico (p. 248): multiplicar
  las $\mathbf M$ y convertir al final a $\mathbf S$.

**Ejemplo 7.1-1. Propagación en medio homogéneo (p. 248).** Capa de ancho $d$ e índice $n$:
$U_2^{(+)}=e^{-j\varphi}U_1^{(+)}$, $U_1^{(-)}=e^{-j\varphi}U_2^{(-)}$, con $\varphi=nk_od$:

$$\mathbf M=\begin{bmatrix}e^{-j\varphi}&0\\ 0&e^{j\varphi}\end{bmatrix},\qquad \mathbf S=\begin{bmatrix}e^{-j\varphi}&0\\ 0&e^{-j\varphi}\end{bmatrix},\qquad \varphi=nk_od. \tag{7.1-4}$$

**Relaciones de conversión (recuadro, p. 248):**

$$\mathbf M=\begin{bmatrix}A&B\\ C&D\end{bmatrix}=\frac{1}{\mathrm t_{21}}\begin{bmatrix}\mathrm t_{12}\mathrm t_{21}-\mathrm r_{12}\mathrm r_{21}&\mathrm r_{21}\\ -\mathrm r_{12}&1\end{bmatrix}, \tag{7.1-5}$$

$$\mathbf S=\begin{bmatrix}\mathrm t_{12}&\mathrm r_{21}\\ \mathrm r_{12}&\mathrm t_{21}\end{bmatrix}=\frac{1}{D}\begin{bmatrix}AD-BC&B\\ -C&1\end{bmatrix}. \tag{7.1-6}$$

No válidas en los límites $\mathrm t_{21}=0$ o $D=0$. Nótese que **$\mathrm t_{21}=1/D$** y **$\mathrm r_{12}=-C/D$**: la
reflectancia hacia adelante sale directamente de los elementos $C$ y $D$ de $\mathbf M$ total.

**Summary (recuadro sombreado, p. 248).** Procedimiento sistemático: (1) dividir la pila en cascada
de elementos (fronteras + capas homogéneas); (2) obtener $\mathbf M$ de cada elemento (vía Fresnel → $\mathbf S$
→ (7.1-5)); (3) multiplicar según (7.1-2); (4) convertir la $\mathbf M$ total a $\mathbf S$ con (7.1-6) para
leer $\mathrm t$ y $\mathrm r$ de toda la pila.

**Dos sistemas en cascada: fórmulas de Airy (p. 249).** Sistema con elementos $\mathrm t_{12},\mathrm r_{21},\mathrm r_{12},\mathrm t_{21}$
seguido de otro con $\mathrm t_{23},\mathrm r_{32},\mathrm r_{23},\mathrm t_{32}$ (multiplicando $\mathbf M$ y convirtiendo a $\mathbf S$):

$$\mathrm t_{13}=\frac{\mathrm t_{12}\mathrm t_{23}}{1-\mathrm r_{21}\mathrm r_{23}},\qquad \mathrm r_{13}=\mathrm r_{12}+\frac{\mathrm t_{12}\mathrm t_{21}\mathrm r_{23}}{1-\mathrm r_{21}\mathrm r_{23}}. \tag{7.1-7}$$

Si entre ambos hay propagación en medio homogéneo de longitud $d$ e índice $n$ ($\varphi=nk_od$), Fig.
7.1-2 (recuadro **Airy's Formulas**, p. 249):

$$\mathrm t_{13}=\frac{\mathrm t_{12}\mathrm t_{23}\exp(-j\varphi)}{1-\mathrm r_{21}\mathrm r_{23}\exp(-j2\varphi)},\qquad \mathrm r_{13}=\mathrm r_{12}+\frac{\mathrm t_{12}\mathrm t_{21}\mathrm r_{23}\exp(-j2\varphi)}{1-\mathrm r_{21}\mathrm r_{23}\exp(-j2\varphi)}. \tag{7.1-8}$$

Derivación alternativa (p. 249): sumar las ondas internas $U^{(+)}=U_0^{(+)}(1+h+h^2+\cdots)=U_0^{(+)}/(1-h)$,
con $U_0^{(+)}=\mathrm t_{12}U_i$ y $h=\mathrm r_{21}\mathrm r_{23}\exp(-j2\phi)$ el **factor de multiplicación por vuelta
completa** (round-trip); $U_t=\mathrm t_{23}e^{-j\phi}U^{(+)}$. (El texto usa $\phi=nk_od$ en este párrafo, mismo
significado que $\varphi$.)

**Relaciones de conservación para medios sin pérdidas (p. 249–250).** Si el medio entre planos 1 y 2
no tiene pérdidas y los medios de entrada y salida tienen la misma impedancia e índice,
$|U_1^{(+)}|^2+|U_2^{(-)}|^2=|U_2^{(+)}|^2+|U_1^{(-)}|^2$ para cualquier combinación de entradas; eligiendo
$(U_1^{(+)},U_2^{(-)})=(1,0),(0,1),(1,1)$:

$$|\mathrm t_{12}|=|\mathrm t_{21}|\equiv|\mathrm t|,\quad |\mathrm r_{12}|=|\mathrm r_{21}|\equiv|\mathrm r|,\quad |\mathrm t|^2+|\mathrm r|^2=1, \tag{7.1-9}$$

$$\mathrm t_{12}/\mathrm t_{21}^*=-\mathrm r_{12}/\mathrm r_{21}^*. \tag{7.1-10}$$

Para la $\mathbf M$ (p. 250):

$$|D|=|A|,\quad |C|=|B|,\quad |A|^2-|B|^2=1, \tag{7.1-11}$$

$$\det\mathbf M=C/B^*=A/D^*=\mathrm t_{12}/\mathrm t_{21},\quad |\det\mathbf M|=1. \tag{7.1-12}$$

**Sistemas recíprocos sin pérdidas (p. 250).** Si además $\mathrm t_{21}=\mathrm t_{12}\equiv\mathrm t$ y $\mathrm r_{21}=\mathrm r_{12}\equiv\mathrm r$:

$$|\mathrm t|^2+|\mathrm r|^2=1,\quad \mathrm t/\mathrm r=-(\mathrm t/\mathrm r)^*,\quad \arg\{\mathrm t\}-\arg\{\mathrm r\}=\pm\pi/2, \tag{7.1-13}$$

(las fases de transmisión y reflexión difieren en $\pi/2$), y

$$A=D^*,\quad B=C^*,\quad |A|^2-|B|^2=1,\quad \det\mathbf M=1. \tag{7.1-14}$$

Forma simple (recuadro **Lossless Reciprocal System**, p. 250):

$$\mathbf S=\begin{bmatrix}\mathrm t&\mathrm r\\ \mathrm r&\mathrm t\end{bmatrix},\qquad \mathbf M=\begin{bmatrix}1/\mathrm t^*&\mathrm r/\mathrm t\\ \mathrm r^*/\mathrm t^*&1/\mathrm t\end{bmatrix}. \tag{7.1-15}$$

El sistema queda descrito por dos números complejos $\mathrm t$, $\mathrm r$ ligados por (7.1-13).

**Ejemplo 7.1-2. Espejo parcialmente reflectante (beamsplitter), p. 250–251.** Sistema recíproco sin
pérdidas en medio homogéneo; con $\arg\{\mathrm t\}=0$, (7.1-13) da $\arg\{\mathrm r\}=\mp\pi/2$, $\mathrm r=\mp j|\mathrm r|$.
Con el signo $+$:

$$\mathbf S=\begin{bmatrix}|\mathrm t|&j|\mathrm r|\\ j|\mathrm r|&|\mathrm t|\end{bmatrix},\quad |\mathrm t|^2+|\mathrm r|^2=1; \tag{7.1-16}$$

$$\mathbf M=\frac{1}{|\mathrm t|}\begin{bmatrix}1&j|\mathrm r|\\ -j|\mathrm r|&1\end{bmatrix}. \tag{7.1-17}$$

Espejo ideal: $|\mathrm r|=1$, $|\mathrm t|=0$ → (7.1-17) no aplica; $\mathbf M$ no representa bien un espejo perfecto
porque los dos lados quedan aislados (p. 251).

**Ejemplo 7.1-3. Frontera dieléctrica única (p. 251).** Por Fresnel (§6.2), incidencia normal entre
$n_1$ y $n_2$:

$$\mathbf S=\begin{bmatrix}\mathrm t_{12}&\mathrm r_{21}\\ \mathrm r_{12}&\mathrm t_{21}\end{bmatrix}=\frac{1}{n_1+n_2}\begin{bmatrix}2n_1&n_2-n_1\\ n_1-n_2&2n_2\end{bmatrix}, \tag{7.1-18}$$

$$\mathbf M=\frac{1}{2n_2}\begin{bmatrix}n_2+n_1&n_2-n_1\\ n_2-n_1&n_2+n_1\end{bmatrix}. \tag{7.1-19}$$

(Este sistema no es recíproco en el sentido de (7.1-15): $\mathrm t_{12}\neq\mathrm t_{21}$ porque los medios de
entrada y salida difieren; $\det\mathbf M=n_1/n_2$.)

**Ejemplo 7.1-4. Propagación seguida de frontera (p. 251).** Capa $n_1$ de ancho $d$ seguida de
frontera a $n_2$: $\mathbf M=$ (7.1-19)·(7.1-4):

$$\mathbf M=\frac{1}{2n_2}\begin{bmatrix}(n_2+n_1)e^{-j\varphi}&(n_2-n_1)e^{j\varphi}\\ (n_2-n_1)e^{-j\varphi}&(n_2+n_1)e^{j\varphi}\end{bmatrix},\qquad \varphi=n_1k_od. \tag{7.1-20}$$

**Ejemplo 7.1-5. Propagación seguida de transmisión por una lámina (slab), p. 251–252.** Cascada
$n_1\to n_2$ (ancho $d_1$ en $n_1$) y $n_2\to n_1$ (ancho $d_2$ en $n_2$); producto en orden inverso:

$$\mathbf M=\frac{1}{4n_1n_2}\begin{bmatrix}(n_1+n_2)e^{-j\varphi_2}&(n_1-n_2)e^{j\varphi_2}\\ (n_1-n_2)e^{-j\varphi_2}&(n_1+n_2)e^{j\varphi_2}\end{bmatrix}\begin{bmatrix}(n_2+n_1)e^{-j\varphi_1}&(n_2-n_1)e^{j\varphi_1}\\ (n_2-n_1)e^{-j\varphi_1}&(n_2+n_1)e^{j\varphi_1}\end{bmatrix}, \tag{7.1-21}$$

$\varphi_1=n_1k_od_1$, $\varphi_2=n_2k_od_2$. Sus elementos cumplen (7.1-14):

$$A=D^*=\frac{1}{\mathrm t^*}=\frac{1}{4n_1n_2}\left[(n_1+n_2)^2e^{-j\varphi_2}-(n_2-n_1)^2e^{j\varphi_2}\right]e^{-j\varphi_1}, \tag{7.1-22}$$

$$B=C^*=\frac{\mathrm r}{\mathrm t}=\frac{1}{4n_1n_2}(n_2^2-n_1^2)\left[e^{-j\varphi_2}-e^{j\varphi_2}\right]e^{j\varphi_1}, \tag{7.1-23}$$

$$\mathrm t=\exp(-j\varphi_1)\frac{4n_1n_2\exp(-j\varphi_2)}{(n_1+n_2)^2-(n_1-n_2)^2\exp(-j2\varphi_2)}. \tag{7.1-24}$$

Se obtiene también de Airy (7.1-8) con $\mathrm t_{12}=\mathrm t_{32}=2n_1/(n_1+n_2)$, $\mathrm t_{21}=\mathrm t_{23}=2n_2/(n_1+n_2)$,
$\mathrm r_{12}=\mathrm r_{32}=-\mathrm r_{21}=-\mathrm r_{23}=(n_1-n_2)/(n_1+n_2)$ (p. 252).

**Ejercicio 7.1-1. Película de cuarto de onda como recubrimiento antirreflejante (p. 252, Fig.
7.1-3).** Película $n_2$, espesor $d$, entre $n_1$ y $n_3$. Derivar el elemento $B$ de $\mathbf M$ y mostrar
que la reflectancia desde el medio 1 es cero si $d=\lambda/4$ y $n_2=\sqrt{n_1n_3}$, con $\lambda=\lambda_o/n_2$.
(Idea: $\mathrm r_{12}=-C/D$ de (7.1-6); con $B=C^*$ basta anular $B$.)

**Ondas oblicuas en medios por capas (p. 252–253).** Fig. 7.1-4: en cada capa todas las ondas hacia
adelante son paralelas entre sí, igual las de retroceso, y ambas forman el mismo ángulo con $\pm z$. El
enfoque "macro" sigue valiendo; la diferencia es que $\mathrm t_{12},\mathrm r_{21},\mathrm r_{12},\mathrm t_{21}$ dependen del
ángulo y de la polarización (§6.2). Propagación oblicua a ángulo $\theta$ en medio homogéneo: (7.1-4)
con $\varphi=nk_od\cos\theta$ (p. 253).

**Ejemplo 7.1-6. Frontera única, onda oblicua TE (y TM), p. 253.** Con Snell $n_1\sin\theta_1=n_2\sin\theta_2$
y Fresnel (6.2-8), (6.2-9):

$$\mathbf S=\frac{1}{\tilde n_1+\tilde n_2}\begin{bmatrix}2a_{12}\tilde n_1&\tilde n_2-\tilde n_1\\ \tilde n_1-\tilde n_2&2a_{21}\tilde n_2\end{bmatrix}, \tag{7.1-25}$$

$$\mathbf M=\frac{1}{2a_{21}\tilde n_2}\begin{bmatrix}\tilde n_1+\tilde n_2&\tilde n_2-\tilde n_1\\ \tilde n_2-\tilde n_1&\tilde n_1+\tilde n_2\end{bmatrix}, \tag{7.1-26}$$

con las definiciones (p. 253):
- TE: $\tilde n_1=n_1\cos\theta_1$, $\tilde n_2=n_2\cos\theta_2$, $a_{12}=a_{21}=1$.
- TM: $\tilde n_1=n_1\sec\theta_1$, $\tilde n_2=n_2\sec\theta_2$, $a_{12}=\cos\theta_1/\cos\theta_2=1/a_{21}$.

**Ejemplo 7.1-7. Lámina, onda oblicua (p. 253).** Misma estructura que 7.1-5 con onda oblicua:
(7.1-27) es (7.1-21) con $n_i\to\tilde n_i$ y $\varphi_i\to\tilde\varphi_i$, donde $\tilde\varphi_1=n_1k_od_1\cos\theta_1$,
$\tilde\varphi_2=n_2k_od_2\cos\theta_2$ (los factores $a_{12}a_{21}=1$ se cancelan). Transmitancia generalizada:

$$\mathrm t=\exp(-j\tilde\varphi_1)\frac{4\tilde n_1\tilde n_2\exp(-j\tilde\varphi_2)}{(\tilde n_1+\tilde n_2)^2-(\tilde n_1-\tilde n_2)^2\exp(-j2\tilde\varphi_2)}. \tag{7.1-28}$$

#### 7.1B Fabry–Perot Etalon (p. 254)

Introducido en §2.5B; filtro / analizador de espectro / resonador (§10.1). Aquí se trata con matrices.

**Etalón de espejos (p. 254).** Dos espejos sin pérdidas ($\mathrm t_1,\mathrm r_1$; $\mathrm t_2,\mathrm r_2$) separados $d$ con
medio $n$:

$$\mathbf M=\begin{bmatrix}1/\mathrm t_1^*&\mathrm r_1/\mathrm t_1\\ \mathrm r_1^*/\mathrm t_1^*&1/\mathrm t_1\end{bmatrix}\begin{bmatrix}e^{-j\varphi}&0\\ 0&e^{j\varphi}\end{bmatrix}\begin{bmatrix}1/\mathrm t_2^*&\mathrm r_2/\mathrm t_2\\ \mathrm r_2^*/\mathrm t_2^*&1/\mathrm t_2\end{bmatrix},\quad \varphi=nk_od. \tag{7.1-29}$$

(Nota: el libro escribe el producto en este orden; por (7.1-2) el primer espejo atravesado es el de la
derecha del producto.) Como el sistema es recíproco sin pérdidas, $\mathrm t=1/D$:

$$\mathrm t=\frac{\mathrm t_1\mathrm t_2\exp(-j\varphi)}{1-\mathrm r_1\mathrm r_2\exp(-j2\varphi)}, \tag{7.1-30}$$

$$\mathcal T=|\mathrm t|^2=\frac{|\mathrm t_1\mathrm t_2|^2}{|1-\mathrm r_1\mathrm r_2\exp(-j2\varphi)|^2}. \tag{7.1-31}$$

Similar a (2.5-16). Suponiendo $\arg\{\mathrm r_1\mathrm r_2\}=0$ (nota al pie: reproduce (2.5-18) si $\varphi$ se
reemplaza por la fase de ida y vuelta $2\varphi$):

$$\mathcal T=\frac{\mathcal T_{\max}}{1+(2\mathcal F/\pi)^2\sin^2\varphi}, \tag{7.1-32}$$

$$\mathcal T_{\max}=\frac{|\mathrm t_1\mathrm t_2|^2}{(1-|\mathrm r_1\mathrm r_2|)^2}=\frac{(1-|\mathrm r_1|^2)(1-|\mathrm r_2|^2)}{(1-|\mathrm r_1\mathrm r_2|)^2}, \tag{7.1-33}$$

**Finesse** (recuadro, p. 254):

$$\mathcal F=\frac{\pi\sqrt{|\mathrm r_1\mathrm r_2|}}{1-|\mathrm r_1\mathrm r_2|}. \tag{7.1-34}$$

Propiedades (p. 255): $\mathcal F$ crece monótonamente con $\mathrm r_1\mathrm r_2$; si $\mathrm r_1\mathrm r_2=0{.}99$, $\mathcal F\approx313$.
$\mathcal T$ es periódica en $\varphi$ con periodo $\pi$; máximo $\mathcal T_{\max}$ (=1 si $|\mathrm r_1|=|\mathrm r_2|$) cuando
$\varphi$ es múltiplo entero de $\pi$; para $\mathcal F$ grande los picos tienen ancho $\approx\pi/\mathcal F$.
Como $\varphi=nk_od=(\omega/c)d$ es proporcional a la frecuencia, $\varphi=\pi$ ↔ $\nu=\nu_F$:

$$\nu_F=\frac{c}{2d},\qquad \omega_F=\frac{\pi c}{d} \tag{7.1-35}$$

**rango espectral libre** (free spectral range; aquí $c=c_o/n$). Transmitancia en frecuencia (recuadro,
p. 255):

$$\mathcal T(\nu)=\frac{\mathcal T_{\max}}{1+(2\mathcal F/\pi)^2\sin^2(\pi\nu/\nu_F)}, \tag{7.1-36}$$

periódica con periodo $\nu_F$, picos en las frecuencias de resonancia $\nu_q=q\nu_F$ ($q$ entero); para
$\mathcal F\gg1$ es una función tipo peine. Ancho espectral de cada línea:

$$\delta\nu=\frac{\nu_F}{\mathcal F}, \tag{7.1-37}$$

un factor $\mathcal F$ menor que la separación entre resonancias. Fig. 7.1-5 (p. 255): $\mathcal T$ y
$\mathcal R=1-\mathcal T$ vs. frecuencia, mostrando $\nu_F=c/2d$ y $\delta\nu=\nu_F/\mathcal F$.

Uso como filtro sintonizable / analizador (p. 255–256): el ancho espectral de la luz medida debe ser
menor que $\nu_F$ para evitar ambigüedad; se sintoniza variando $d$: $\Delta\nu_q=-(qc/2d^2)\Delta d=-\nu_q\Delta d/d$,
mientras que $\nu_F$ cambia solo en $-\nu_F\Delta d/d$. **Ejemplo numérico (p. 256):** $d=1{.}5$ cm, $n=1$ →
$\nu_F=10$ GHz; con $\nu=10^{14}$ Hz ($q=10^4$), $\Delta d=1{.}5\ \mu$m ($10^{-4}$ relativo) desplaza el pico en
$\Delta\nu_q=10$ GHz y cambia $\nu_F$ solo en 1 MHz (a 9.999 GHz).

**La lámina dieléctrica como etalón Fabry-Perot (p. 256).** De (7.1-24), lámina $n_2$ ancho $d$ en $n_1$:

$$\mathrm t=\frac{4n_1n_2\exp(-j\varphi)}{(n_1+n_2)^2-(n_1-n_2)^2\exp(-j2\varphi)},\quad \varphi=n_2k_od. \tag{7.1-38}$$

Reproduce (7.1-30) con $\mathrm t_1\mathrm t_2=4n_1n_2/(n_1+n_2)$ [sic, así en el libro; dimensionalmente debería
leerse $4n_1n_2/(n_1+n_2)^2$] y $\mathrm r_1\mathrm r_2=(n_1-n_2)^2/(n_1+n_2)^2$. Valen (7.1-32) y (7.1-36); la finesse:

$$\mathcal F=\frac{\pi}{4}\frac{|n_2^2-n_1^2|}{n_1n_2}. \tag{7.1-39}$$

Valores grandes de $\mathcal F$ no se logran con láminas: para $n_1=1{.}5$ (SiO₂) y $n_2=3{.}5$ (Si),
$\mathcal F=1{.}68$ (Fig. 7.1-6, p. 256: $\mathcal T$ oscila entre ~0.5 y 1, sin picos agudos). Para subir $\mathcal F$
hay que recubrir las caras.

**Transmitancia fuera de eje (p. 256–257).** Onda a ángulo $\theta$ con el eje: (7.1-30) con
$\tilde\varphi=nk_od\cos\theta$;

$$\mathcal T(\nu)=\frac{\mathcal T_{\max}}{1+(2\mathcal F/\pi)^2\sin^2(\pi\cos\theta\,\nu/\nu_F)}. \tag{7.1-40}$$

Máximos (recuadro **Resonance Condition**, p. 257):

$$\nu=q\,\nu_F\sec\theta,\qquad q=1,2,\dots,\qquad \nu_F=c/2d. \tag{7.1-41}$$

Fig. 7.1-7 (p. 257): (a) onda oblicua; (b) luz blanca de fuente puntual → anillos concéntricos de
distintos colores; (c) curvas $\theta$ vs. $\nu/\nu_F$ de (7.1-41). A cada ángulo solo pasa un conjunto
discreto de frecuencias; si el ancho espectral de la luz es $<\nu_F$, cada frecuencia ↔ un único ángulo
→ analizador de espectro.

#### 7.1C Bragg Grating (p. 257)

Introducida en Ejercicio 2.5-3 (espejos planos parcialmente reflectantes equiespaciados). Aquí se
generaliza a $N$ segmentos multicapa idénticos y se desarrolla una teoría exacta matricial.

**Teoría simplificada (p. 257–258).** Supuestos del Ejercicio 2.5-3: (1) espejos débilmente
reflectantes (onda incidente no se agota), (2) reflexiones secundarias despreciables:

$$\mathcal R_N=\frac{\sin^2N\varphi}{\sin^2\varphi}R. \tag{7.1-42}$$

(Nota al pie, p. 257: en el Ej. 2.5-3 $\varphi$ es la fase entre fasores sucesivos; aquí esa fase se llama
$2\varphi$ por ser de ida y vuelta.) El factor $\sin^2N\varphi/\sin^2\varphi$ es la intensidad de la suma de $N$
fasores unitarios con diferencia de fase $2\varphi$: vale $N^2$ cuando $2\varphi=q2\pi$ (condición de Bragg), y
cae con ancho $\propto1/N$. Con espejos a distancia $\Lambda$ y fase de ida y vuelta $2\varphi=2k\Lambda\cos\theta$, el
máximo ocurre cuando $2k\Lambda\cos\theta=2q\pi$ (recuadros, p. 258):

$$\cos\theta=q\frac{\lambda}{2\Lambda}=q\frac{\omega_{\mathcal B}}{\omega}=q\frac{\nu_{\mathcal B}}{\nu}, \tag{7.1-43}$$

$$\nu_{\mathcal B}=\frac{c}{2\Lambda},\qquad \omega_{\mathcal B}=\frac{\pi c}{\Lambda} \tag{7.1-44}$$

(**frecuencia de Bragg**). Fig. 7.1-8 (p. 258): lugar geométrico de $\nu$ y $\theta$ que cumplen Bragg;
ejemplo: $\nu=1{.}5\nu_{\mathcal B}$ → $\theta=48{.}2°$, ángulo de Bragg $\theta_{\mathcal B}=41{.}8°$ (medido desde el
plano de la rejilla). A incidencia normal, picos en $\nu=q\nu_{\mathcal B}$; para $\nu<\nu_{\mathcal B}$ no se
cumple Bragg a ningún ángulo; para $\nu_{\mathcal B}<\nu<2\nu_{\mathcal B}$ a un solo ángulo
$\theta=\cos^{-1}(\lambda/2\Lambda)$, cuyo complemento es el **ángulo de Bragg** (recuadro, p. 258):

$$\theta_{\mathcal B}=\sin^{-1}(\lambda/2\Lambda). \tag{7.1-45}$$

Para $\nu\ge2\nu_{\mathcal B}$ se cumple en más de un ángulo.

**Teoría matricial (p. 259–261).** Incluye transmisiones/reflexiones múltiples y agotamiento; resultado
sorprendente: la reflexión total ocurre sobre **bandas** alrededor de los múltiplos de $\nu_{\mathcal B}/\cos\theta$.
Rejilla de $N$ segmentos idénticos (Fig. 7.1-9), cada uno con matriz unimodular recíproca sin pérdidas

$$\mathbf M_o=\begin{bmatrix}1/\mathrm t^*&\mathrm r/\mathrm t\\ \mathrm r^*/\mathrm t^*&1/\mathrm t\end{bmatrix}, \tag{7.1-46}$$

$\mathcal T=|\mathrm t|^2$, $\mathcal R=|\mathrm r|^2$. Como $\mathbf M=\mathbf M_o^N$ y $\det\mathbf M_o=1$:

$$\mathbf M_o^N=\Psi_N\mathbf M_o-\Psi_{N-1}\mathbf I, \tag{7.1-47}$$

con (recuadros, p. 259)

$$\Psi_N=\frac{\sin N\Phi}{\sin\Phi}, \tag{7.1-48}$$

$$\cos\Phi=\mathrm{Re}\{1/\mathrm t\}. \tag{7.1-49}$$

(Se prueba por inducción.) Escribiendo $\mathbf M_o^N$ en la forma (7.1-15) con $\mathrm t_N$, $\mathrm r_N$:

$$\mathbf M_o^N=\begin{bmatrix}1/\mathrm t_N^*&\mathrm r_N/\mathrm t_N\\ \mathrm r_N^*/\mathrm t_N^*&1/\mathrm t_N\end{bmatrix}, \tag{7.1-50}$$

y comparando elementos (p. 260):

$$\frac{1}{\mathrm t_N}=\Psi_N\frac{1}{\mathrm t}-\Psi_{N-1}, \tag{7.1-51}$$

$$\frac{\mathrm r_N}{\mathrm t_N}=\Psi_N\frac{\mathrm r}{\mathrm t}. \tag{7.1-52}$$

De (7.1-52) con $\mathcal R=1-\mathcal T$:

$$\mathcal T_N=\frac{\mathcal T}{\mathcal T+\Psi_N^2(1-\mathcal T)}, \tag{7.1-53}$$

$$\mathcal R_N=\frac{\Psi_N^2\mathcal R}{1-\mathcal R+\Psi_N^2\mathcal R}. \tag{7.1-54}$$

(**Bragg-Grating Reflectance**, recuadro p. 260.)

**Summary (recuadro sombreado, p. 260).** $\mathcal R_N$ se relaciona con $\mathcal R$ de un segmento por la
relación no lineal (7.1-54), que contiene el factor de interferencia $\Psi_N$ (7.1-48), dependiente de $N$ y
de $\Phi$, ligado a $\mathrm t$ por (7.1-49).

Límites (p. 260): si $\mathcal R\ll1$ y $\Psi_N^2\mathcal R\ll1$,

$$\mathcal R_N\approx\Psi_N^2\mathcal R=\frac{\sin^2N\Phi}{\sin^2\Phi}\mathcal R, \tag{7.1-55}$$

igual a (7.1-42) con $\Phi$ en el papel de $\varphi$. Si $\Psi_N^2\gg1$: $\mathcal R_N\approx\Psi_N^2\mathcal R/(1+\Psi_N^2\mathcal R)$
(saturación, típica de sistemas con realimentación); si $\Psi_N^2\mathcal R\gg1$, $\mathcal R_N\to1$: el dispositivo
de $N$ segmentos es un espejo perfecto aunque cada segmento refleje poco.

Dos regímenes según $\Phi=\cos^{-1}(\mathrm{Re}\{1/\mathrm t\})$ (p. 260–261):

- **Reflexión parcial y cero (p. 261):** $|\mathrm{Re}\{1/\mathrm t\}|\le1$ → $\Phi$ real. Máximo cuando $\Psi_N=N$:
  $\mathcal R_N=N^2\mathcal R/(1-\mathcal R+N^2\mathcal R)$; no llega a 1 salvo $\mathcal R=1$ (ej.: $N=10$, $\mathcal R=0{.}5$ →
  $\mathcal R_N\approx0{.}99$). **Transmitancia total** ($\mathcal R_N=0$) cuando $\Psi_N=0$, i.e. $\sin N\Phi=0$,
  $\Phi=q\pi/N$, $q=0,1,\dots,N-1$: $N$ frecuencias de resonancia (tunelado a través de segmentos
  reflectantes).
- **Reflexión total (p. 261):** $|\mathrm{Re}\{1/\mathrm t\}|=|\cos\Phi|>1$ → $\Phi=\Phi_R+j\Phi_I$ complejo. Con
  $\cos(\Phi_R+j\Phi_I)=\cos\Phi_R\cosh\Phi_I-j\sin\Phi_R\sinh\Phi_I$ e igualando partes real e imaginaria de
  (7.1-49): $\sin\Phi_R=0$, $\Phi_R=m\pi$, $\cos\Phi_R=\pm1$, y (recuadros **Total-Reflection Regime**):

$$\cosh\Phi_I=|\mathrm{Re}\{1/\mathrm t\}|, \tag{7.1-56}$$

$$\Psi_N=\pm\frac{\sinh N\Phi_I}{\sinh\Phi_I}, \tag{7.1-57}$$

  signo $=\cos(Nm\pi)/\cos(m\pi)$. $|\Psi_N|$ crece exponencialmente con $N$ → $\mathcal R_N\approx1$; las ondas
  hacia adelante se vuelven evanescentes (como en reflexión total interna).

Como $\Phi$ depende de $\mathrm t(\nu)$, los regímenes corresponden a bandas espectrales: **stop bands**
(reflexión total, transmisión casi bloqueada) y **passbands** (con transmisión total en resonancias
específicas) (p. 261).

**Ejemplo 7.1-8. Pila de espejos parcialmente reflectantes (p. 261–262).** $N$ espejos idénticos a
distancia $\Lambda$ en medio $n$ (Fig. 7.1-10a). Segmento = propagación $\Lambda$ + espejo; $\mathbf M_o=$
(7.1-17)·(7.1-4):

$$\mathbf M_o=\frac{1}{|\mathrm t|}\begin{bmatrix}e^{-j\varphi}&j|\mathrm r|e^{j\varphi}\\ -j|\mathrm r|e^{-j\varphi}&e^{j\varphi}\end{bmatrix},\qquad \varphi=nk_o\Lambda=\pi\nu/\nu_{\mathcal B}, \tag{7.1-58}$$

$\nu_{\mathcal B}=c/2\Lambda$. Entonces $\mathrm t=|\mathrm t|e^{j\varphi}$ y

$$\cos\Phi=\frac{1}{|\mathrm t|}\cos\varphi\quad\text{para }|\cos\varphi|\le|\mathrm t|, \tag{7.1-59}$$

$$\cosh\Phi_I=\frac{1}{|\mathrm t|}|\cos\varphi|\quad\text{para }|\cos\varphi|>|\mathrm t|. \tag{7.1-60}$$

Fig. 7.1-10 (p. 262), $N=10$, $|\mathrm r|^2=0{.}5$: (b) $\Phi$ y $\Phi_I$ vs. $\varphi$ (no lineal); (c) $\mathcal R_N$ vs.
$\nu/\nu_{\mathcal B}$: en el régimen normal (sombreado) múltiples picos con ceros entre ellos, ninguno llega
a 1 aunque $\Psi_N$ alcance $N=10$; en las stop bands (centradas en $\nu_{\mathcal B}$, $2\nu_{\mathcal B}$, …, $\varphi=\pi$,
$2\pi$, …) $\Psi_N\approx3000$ en el centro ($|\mathrm t|^2=0{.}5$) y $\mathcal R_N\approx1$. Stop bands centradas en
múltiplos de $\nu_{\mathcal B}$ (incluida la de $\nu=0$ en este sistema, ver p. 272).

**Ejemplo 7.1-9. Rejilla de Bragg dieléctrica (p. 262–263, Fig. 7.1-11).** $N$ capas $n_2$ de ancho
$d_2$ en medio $n_1$, separadas $d_1$: pila de $N$ dobles capas del Ejemplo 7.1-5. De (7.1-22):

$$\mathrm{Re}\left\{\frac{1}{\mathrm t}\right\}=\frac{(n_1+n_2)^2}{4n_1n_2}\cos(\varphi_1+\varphi_2)-\frac{(n_2-n_1)^2}{4n_1n_2}\cos(\varphi_1-\varphi_2), \tag{7.1-61}$$

$\varphi_1=n_1k_od_1$, $\varphi_2=n_2k_od_2$. Con $\varphi_1+\varphi_2=k_o(n_1d_1+n_2d_2)=\pi\nu/\nu_{\mathcal B}$,
$\nu_{\mathcal B}=(c_o/\bar n)/2\Lambda$, $\bar n=(n_1d_1+n_2d_2)/\Lambda$ (índice promedio), y
$\varphi_1-\varphi_2=\zeta\pi\nu/\nu_{\mathcal B}$ con $\zeta=(n_1d_1-n_2d_2)/(n_1d_1+n_2d_2)$. $\nu_{\mathcal B}$ es la
frecuencia en que la fase de ida y vuelta de un segmento $2k_o(n_1d_1+n_2d_2)=2\pi$. Fig. 7.1-11 (p. 263):
$N=10$, $d_1=d_2$, $n_1=1{.}5$, $n_2=3{.}5$, en medio ajustado $n_1$: stop bands con $\mathcal R\approx1$ centradas
en múltiplos de $\nu_{\mathcal B}=c/2\Lambda$ ($c=c_o/\bar n$). (En la figura la banda alrededor de $2\nu_{\mathcal B}$
es la "stop band 2" y la de $3\nu_{\mathcal B}$ es más angosta; no hay stop band en $\nu=0$.)

**Ejemplo 7.1-10. Rejilla dieléctrica, incidencia oblicua (p. 263).** Generalización con
$n_1\sin\theta_1=n_2\sin\theta_2$:

$$\mathrm{Re}\left\{\frac{1}{\mathrm t}\right\}=\frac{(\tilde n_1+\tilde n_2)^2}{4\tilde n_1\tilde n_2}\cos(\tilde\varphi_1+\tilde\varphi_2)-\frac{(\tilde n_2-\tilde n_1)^2}{4\tilde n_1\tilde n_2}\cos(\tilde\varphi_1-\tilde\varphi_2), \tag{7.1-62}$$

$\tilde\varphi_i=n_ik_od_i\cos\theta_i$; $\tilde n_i=n_i\cos\theta_i$ (TE), $\tilde n_i=n_i\sec\theta_i$ (TM). Fig. 7.1-12
(p. 263): $\mathcal R$ vs. $\nu/\nu_{\mathcal B}$ a $\theta_1=0°,30°,60°,70°$ para TE y TM (rejilla de Fig. 7.1-11):
las stop bands se corren a frecuencias mayores con el ángulo; en TM se angostan mucho (cerca de Brewster
desaparecen), en TE se mantienen anchas. El rango angular con $\mathcal R=1$ crece con el contraste $n_2/n_1$.

**Rejilla de Bragg en medio no ajustado (p. 264).** El análisis anterior exige medio externo con índice
igual al de la primera capa (matched). En la práctica (aire) hay que incluir las fronteras: se escribe
$\mathbf M$ del sistema completo y se convierte a $\mathbf S$. Si $\mathbf M_o^N$ es la rejilla en medio ajustado,

$$\mathbf M=\mathbf M_e\mathbf M_o^{N-1}\mathbf M_i, \tag{7.1-63}$$

$\mathbf M_i$: frontera de entrada; $\mathbf M_e$: $N$-ésimo segmento con frontera hacia el medio externo.

**Ejemplo 7.1-11. Reflectancia de rejilla dieléctrica en medio no ajustado (p. 264).** Capas
$n_1,n_2$ (anchos $d_1,d_2$) en medio $n_0$, incidencia a $\theta_0$. En (7.1-63): $\mathbf M_i$ = frontera
$n_0\to n_1$ (Ej. 7.1-6); $\mathbf M_o$ = segmento (Ej. 7.1-7); $\mathbf M_e$ = propagación $d_1$ en $n_1$ + lámina
$d_2$ en $n_2$ + frontera a $n_0$. Luego (7.1-6) → $\mathbf S$; la reflectancia es $\mathrm r_{12}$. Fig. 7.1-13
(p. 264): $\mathcal R$ vs. $\theta$ a $\nu/\nu_{\mathcal B}=0{.}9,\,1,\,1{.}2$, (a) en medio ajustado ($n=n_1$) y (b) en aire
($n=1$). **En aire la rejilla tiene reflectancia unidad a todos los ángulos, ambas polarizaciones, en la
banda $0{.}97\nu_{\mathcal B}$ a $1{.}18\nu_{\mathcal B}$** (reflector omnidireccional; se retoma en §7.2D).

---

### 7.2 One-Dimensional Photonic Crystals (p. 265)

Cristal fotónico 1D: propiedades ópticas periódicas en una dirección (eje de periodicidad $z$),
constantes en las ortogonales. $\epsilon(z)$ y $\eta(z)=\epsilon_o/\epsilon(z)$ periódicas:

$$\eta(z+\Lambda)=\eta(z), \tag{7.2-1}$$

$\Lambda$ = periodo. Onda en eje polarizada en $x$ ($E_x$, $H_y$ funciones solo de $z$), (7.0-2) queda:

$$-\frac{d}{dz}\left[\eta(z)\frac{d}{dz}\right]H_y=\frac{\omega^2}{c_o^2}H_y. \tag{7.2-2}$$

Onda fuera de eje en el plano $x$–$z$, polarización TM ($\mathbf H$ según $y$):

$$\left\{-\frac{\partial}{\partial z}\left[\eta(z)\frac{\partial}{\partial z}\right]+\eta(z)\frac{\partial^2}{\partial x^2}\right\}H_y=\frac{\omega^2}{c_o^2}H_y. \tag{7.2-3}$$

Ambas son problemas de autovalores para los modos $H_y(x,z)$ (p. 265).

#### 7.2A Bloch Modes (p. 265)

Medio homogéneo: invariante a traslación arbitraria; un modo es una onda que ante traslación solo cambia
por una constante multiplicativa de módulo 1; $\exp(-jkz)$ lo es, con autovalor $\exp(-jkd)$ de la
traslación por $d$ (Apéndice C).

**Modos de Bloch en eje (p. 265–266).** Medio periódico 1D invariante a traslación por $\Lambda$; modos que
conservan su forma salvo un factor de fase (recuadro **Bloch Mode**):

$$U(z)=p_K(z)\exp(-jKz), \tag{7.2-4}$$

$U$ = cualquier componente $E_x,E_y,H_x,H_y$; $K$ constante (**Bloch wavenumber**); $p_K(z)$ periódica de
periodo $\Lambda$. Traslación por $\Lambda$ → factor $\exp(-jK\Lambda)$. Es una onda plana $\exp(-jKz)$ modulada por
$p_K(z)$ (onda estacionaria), Fig. 7.2-1(a). Como $p_K$ es periódica, se expande en armónicos
$\exp(-jmgz)$, $m=0,\pm1,\dots$ (recuadro, p. 266):

$$g=2\pi/\Lambda, \tag{7.2-5}$$

así que la onda de Bloch es superposición de ondas planas de frecuencias espaciales $K+mg$ (Fig.
7.2-1b); análogo al corrimiento Doppler. Dos modos con $K$ y $K'=K+g$ son equivalentes
($\exp(-jK'\Lambda)=\exp(-jK\Lambda)$) → basta considerar $K$ en un intervalo de ancho $g$; el intervalo
$[-g/2,g/2]=[-\pi/\Lambda,\pi/\Lambda]$ es la **primera zona de Brillouin** (p. 266).

**Modos de Bloch fuera de eje (p. 266–267, recuadro Off-Axis Bloch Mode):**

$$U(x,y,z)=p_K(z)\exp(-jKz)\exp(-jk_xx). \tag{7.2-6}$$

La uniformidad en $x$ impone solo la forma $\exp(-jk_xx)$; donde el índice es $n$, $k_x=nk_o\sin\theta$; $n\sin\theta$ y
$k_x$ no cambian entre capas (Snell).

**Modos normales al eje (p. 267, recuadro):** si el ángulo en el medio más denso supera el crítico, los
modos viajan lateralmente ($x$) con $K=0$:

$$U(x,y,z)=p_0(z)\exp(-jk_xx), \tag{7.2-7}$$

$p_0(z)$ periódica = onda estacionaria a lo largo del eje de periodicidad.

**Problema de autovalores, relación de dispersión y bandgaps (p. 267–268).** Para cada $K$, los
autovalores $\omega^2/c_o^2$ dan un conjunto discreto de $\omega$ → relación de dispersión $\omega$–$K$,
función periódica multivaluada de $K$ con periodo $g$, usualmente graficada en la zona de Brillouin
(Fig. 7.2-2a). Vista como función monótona creciente de $K$ presenta saltos discretos en $K=$ múltiplos
enteros de $g/2$: esos saltos son los **photonic bandgaps** (bandas espectrales no cruzadas por las
curvas de dispersión → no hay modos propagantes).

Origen de la discontinuidad (p. 267): en $K=g/2$ el periodo de la onda viajera es exactamente la mitad
del periodo del medio. Los modos con $k=\pm g/2$ ven versiones invertidas del medio,
$p_{-g/2}(z)=p_{g/2}(-z)$, pero son el mismo modo (sus $K$ difieren en $g$); así en el borde de la zona hay
dos funciones de Bloch invertidas una de la otra, que interactúan de forma distinta con el medio
inhomogéneo → dos autovalores $\omega$ distintos → discontinuidad. Principio variacional (Apéndice C,
p. 267–268): energía variacional $E_v=\tfrac12(\mathbf H,\mathcal L\mathbf H)/(\mathbf H,\mathbf H)$ con
$(\mathbf H,\mathcal L\mathbf H)=\int|\mathbf D(\mathbf r)|^2/\epsilon(\mathbf r)\,d\mathbf r$; se minimiza concentrando $\mathbf D$ donde
$1/\epsilon$ es menor (índice mayor). En el borde de la zona (Fig. 7.2-2b), la autofunción de menor
frecuencia (punto A) concentra $\mathbf D$ en la capa de mayor índice; la de mayor frecuencia (B) en la
de menor índice.

Dos enfoques para resolver el problema de autovalores (p. 268): **Fourier Optics** (expandir $\eta(z)$ y
$p_K(z)$ en series de Fourier → problema matricial de autovalores, numérico; §7.2C) y **Matrix Optics**
(medios por capas: usar las matrices de §7.1A/7.1C → problema de autovalores $2\times2$; §7.2B).

#### 7.2B Matrix Optics of Periodic Media (p. 268)

Medio periódico = celdas unitarias (**unit cells**) idénticas repetidas con periodo $\Lambda$ (Fig. 7.2-3);
cada celda es un sistema recíproco sin pérdidas con matriz unimodular

$$\mathbf M_o=\begin{bmatrix}1/\mathrm t^*&\mathrm r/\mathrm t\\ \mathrm r^*/\mathrm t^*&1/\mathrm t\end{bmatrix}, \tag{7.2-8}$$

$\mathcal T=|\mathrm t|^2$, $\mathcal R=|\mathrm r|^2$. Es una rejilla de Bragg con infinitos segmentos. Amplitudes
$\{U_m^{(\pm)}\}$ al inicio $z=m\Lambda$ de la celda $m$; recurrencia:

$$\begin{bmatrix}U_{m+1}^{(+)}\\ U_{m+1}^{(-)}\end{bmatrix}=\mathbf M_o\begin{bmatrix}U_m^{(+)}\\ U_m^{(-)}\end{bmatrix}. \tag{7.2-9}$$

**Problema de autovalores y modos de Bloch (p. 269–270).** Los modos son ondas autorreproducentes:

$$\begin{bmatrix}U_{m+1}^{(+)}\\ U_{m+1}^{(-)}\end{bmatrix}=e^{-j\Phi}\begin{bmatrix}U_m^{(+)}\\ U_m^{(-)}\end{bmatrix},\quad m=1,2,\dots; \tag{7.2-10}$$

tras una celda los módulos no cambian y las fases se corren en $\Phi$ (**fase de Bloch**); $K=\Phi/\Lambda$
(recuadro **Bloch Phase**):

$$\Phi=K\Lambda. \tag{7.2-11}$$

Con $m=0$:

$$\mathbf M_o\begin{bmatrix}U_0^{(+)}\\ U_0^{(-)}\end{bmatrix}=e^{-j\Phi}\begin{bmatrix}U_0^{(+)}\\ U_0^{(-)}\end{bmatrix}, \tag{7.2-12}$$

problema de autovalores $2\times2$; $e^{-j\Phi}$ autovalor, $(U_0^{(+)},U_0^{(-)})$ autovector. De
$\det(\mathbf M_o-e^{-j\Phi}\mathbf I)=0$ y $|\mathrm t|^2+|\mathrm r|^2=1$:
$e^{-j\Phi}=\tfrac12(1/\mathrm t+1/\mathrm t^*)\pm j\{1-[\tfrac12(1/\mathrm t+1/\mathrm t^*)]^2\}^{1/2}$, de donde (recuadro, p. 270):

$$\cos\Phi=\mathrm{Re}\left\{\frac{1}{\mathrm t}\right\}. \tag{7.2-13}$$

Idéntica a (7.1-49) de la rejilla de Bragg. Solo dos soluciones independientes: $\pm\Phi$ en $[-\pi,\pi]$
(modos hacia adelante y hacia atrás); sumar múltiplos de $2\pi$ no da nada nuevo. Autovectores:

$$\begin{bmatrix}U_0^{(+)}\\ U_0^{(-)}\end{bmatrix}\propto\begin{bmatrix}\mathrm r/\mathrm t\\ e^{-j\Phi}-1/\mathrm t^*\end{bmatrix}. \tag{7.2-14}$$

La función periódica $p_K(z)$ se obtiene propagando $U_0^{(\pm)}$ por la celda; si la primera capa es
homogénea con $n_1$ y ancho $d_1$:

$$p_K(z)e^{-jKz}=U_0^{(+)}e^{-jn_1k_oz}+U_0^{(-)}e^{jn_1k_oz},\quad 0<z<d_1, \tag{7.2-15}$$

$$p_K(z)\propto\left[-\mathrm r e^{-jn_1k_oz}+(e^{-jK\Lambda}-1)e^{jn_1k_oz}\right]e^{jKz},\quad 0<z<d_1. \tag{7.2-16}$$

**Relación de dispersión y estructura de bandas fotónicas (p. 270–271).** Como $\Phi=K\Lambda$ y
$\mathrm t=\mathrm t(\omega)$ (recuadro **Dispersion Relation**):

$$\cos\left(2\pi\frac{K}{g}\right)=\mathrm{Re}\left\{\frac{1}{\mathrm t(\omega)}\right\}, \tag{7.2-17}$$

$g=2\pi/\Lambda$. Periódica en $K$ con periodo $g$; dominio restringido a la zona de Brillouin
$[-g/2,g/2]=[-\pi/\Lambda,\pi/\Lambda]$ (↔ $\Phi\in[-\pi,\pi]$); por paridad del coseno, a cada $\omega$ hay
$\pm K$ (modos hacia adelante/atrás). Dos regímenes (p. 271):
- **Régimen de propagación:** $K$ real, $|\mathrm{Re}\{1/\mathrm t(\omega)\}|\le1$; bandas numeradas 1, 2, … desde la de
  menor frecuencia.
- **Régimen de bandgap fotónico:** $K$ complejo, $|\mathrm{Re}\{1/\mathrm t(\omega)\}|>1$; ondas evanescentes
  rápidamente atenuadas; corresponden a las stop bands de la rejilla de §7.1C; también llamados
  **photonic bandgaps (PBG)** o **forbidden gaps**.

Se grafica $K$ en unidades de $g=2\pi/\Lambda$ y $\omega$ en unidades de $\omega_{\mathcal B}=\pi c/\Lambda$, $c=c_o/\bar n$;
$\omega_{\mathcal B}/(g/2)=c$ es la pendiente de $\omega=cK$ en el medio homogéneo de índice promedio (p. 271).

**Ejemplo 7.2-1. Pila periódica de espejos parcialmente reflectantes (p. 271–272).** Con
$\mathrm t=|\mathrm t|e^{j\varphi}$, $\varphi=nk_o\Lambda=(\omega/c)\Lambda$ (Ej. 7.1-8) en (7.2-13) (recuadro):

$$\cos\left(2\pi\frac{K}{g}\right)=\frac{1}{|\mathrm t|}\cos\left(\pi\frac{\omega}{\omega_{\mathcal B}}\right), \tag{7.2-18}$$

$\omega_{\mathcal B}=c\pi/\Lambda$. Fig. 7.2-4 (p. 271): diagrama de dispersión con $|\mathrm t|^2=0{.}5$; bandgaps
centrados en $\omega_{\mathcal B},2\omega_{\mathcal B},\dots$ (sin solución real); **en este sistema el bandgap más bajo
empieza en $\omega=0$** (p. 272). Líneas punteadas: $\omega=cK$.

**Ejemplo 7.2-2. Capas dieléctricas alternadas (p. 272, Fig. 7.2-5).** $n_1,n_2$, anchos $d_1,d_2$,
$\Lambda=d_1+d_2$ (rejilla del Ej. 7.1-9 con $N=\infty$). Con $\mathrm{Re}\{1/\mathrm t\}=\mathrm{Re}\{A\}$ de (7.1-61),
$\varphi_1+\varphi_2=\pi\omega/\omega_{\mathcal B}$, $\varphi_1-\varphi_2=\zeta\pi\omega/\omega_{\mathcal B}$,
$\omega_{\mathcal B}=(c_o/\bar n)(\pi/\Lambda)$, $\bar n=(n_1d_1+n_2d_2)/\Lambda$, $\zeta=(n_1d_1-n_2d_2)/(n_1d_1+n_2d_2)$
(recuadro):

$$\cos\left(2\pi\frac{K}{g}\right)=\frac{1}{\mathrm t_{12}\mathrm t_{21}}\left[\cos\left(\pi\frac{\omega}{\omega_{\mathcal B}}\right)-|\mathrm r_{12}|^2\cos\left(\pi\zeta\frac{\omega}{\omega_{\mathcal B}}\right)\right], \tag{7.2-19}$$

$\mathrm t_{12}\mathrm t_{21}=4n_1n_2/(n_1+n_2)^2$, $|\mathrm r_{12}|^2=(n_2-n_1)^2/(n_1+n_2)^2$. Fig. 7.2-5: $n_1=1{.}5$,
$n_2=3{.}5$, $d_1=d_2$; gaps centrados en $\omega_{\mathcal B}$ y múltiplos, alternando entre el borde ($K=g/2$)
y el centro ($K=0$) de la zona; **aquí alrededor de $\omega=0$ sí hay modos propagantes**. Menor contraste
→ gaps más angostos, pero **existen para cualquier contraste no nulo** (p. 272).

**Velocidades de fase y de grupo (p. 272–273).** $K$ ↔ velocidad de fase $\omega/K$ e índice efectivo
$n_{\rm eff}=c_oK/\omega$; velocidad de grupo $v=d\omega/dK$ ↔ índice de grupo efectivo $N_{\rm eff}=c_o\,dK/d\omega$
(§5.6). Se leen de la curva $\omega$–$K$ (pendiente de la recta al origen y pendiente local). Fig. 7.2-6
(p. 273): a bajas frecuencias en la primera banda $n_{\rm eff}\approx\bar n$ (medio homogéneo promedio);
$n_{\rm eff}$ crece por encima de $\bar n$ hacia el borde de banda; en el fondo de la segunda banda
$n_{\rm eff}<\bar n$ y sube hacia $\bar n$ a mitad de banda. Esa caída se explica por la distribución
espacial de los modos (ortogonales): el modo del tope de la banda inferior concentra energía en las
capas de mayor índice; el del fondo de la superior, en las de menor índice. **$N_{\rm eff}$ crece mucho al
acercarse a los bordes del gap (por arriba y por abajo): la velocidad de grupo cae, los pulsos son muy
lentos cerca del bandgap** (p. 273).

**Relación de dispersión fuera de eje y estructura de bandas (p. 273–274).** Misma ecuación
$\cos(K\Lambda)=\mathrm{Re}\{1/\mathrm t(\omega)\}$ con $\mathrm{Re}\{1/\mathrm t\}$ de (7.1-62) (depende de ángulos y de TE/TM).
Como $k_x=n_1k_o\sin\theta_1=n_2k_o\sin\theta_2$ es común, conviene la superficie 3D $\omega=\omega(K,k_x)$; cada $k_x$
da un diagrama como Fig. 7.2-5. **Diagrama de dispersión proyectado** (projected dispersion diagram,
Fig. 7.2-7, p. 274): bordes de bandas y gaps vs. $k_x$ para TE y TM (bandas sombreadas; blanco = gaps).
Cada ángulo de incidencia es una recta por el origen: $\theta_1$ en la capa 1 ↔ $k_x=(\omega/c_1)\sin\theta_1$,
$\omega=(c_1/\sin\theta_1)k_x$, $c_1=c_o/n_1$; la recta $\omega=c_1k_x$ (**light line**) ↔ $\theta_1=90°$; análogamente
$\omega=c_2k_x$ (se muestra solo esta, asumiendo $n_2>n_1$, $c_2<c_1$). Los puntos entre ambas light lines
son modos normales al eje (viajan lateralmente por reflexión total en el medio denso). Fig. 7.2-7:
$n_1=1{.}5$, $n_2=3{.}5$, $d_1=d_2=\Lambda/2$, $\omega_{\mathcal B}=\pi c_o/\Lambda\bar n$; rectas a $0°,20°,40°,60°,90°$ y
ángulo de Brewster $\theta_B=66{.}8°$.

¿Hay un rango de frecuencias prohibido a todos los ángulos y polarizaciones (bandgap completo)? Debería
alinearse el gap para todo $k_x$ entre $k_x=0$ y $k_x=\omega/c_2$ y ambas polarizaciones. **No es posible en
1D**; sí en 2D y 3D (§7.3). Caso especial donde nunca hay gap: onda TM a Brewster
$\theta_B=\tan^{-1}(n_2/n_1)$ en la capa 1; la reflectancia de la celda es cero, las ondas de ida y vuelta se
desacoplan y no hay efecto colectivo (p. 274).

#### 7.2C Fourier Optics of Periodic Media (p. 274)

Aplicable a medios periódicos arbitrarios (incluso continuos) y generalizable a 2D/3D. Onda en eje
polarizada en $x$, ecuación (7.2-2); $\eta(z)$ periódica:

$$\eta(z)=\sum_{\ell=-\infty}^{\infty}\eta_\ell\exp(-j\ell gz), \tag{7.2-20}$$

$g=2\pi/\Lambda$ (el libro dice "rad/mm"), $\eta_\ell$ coeficiente del armónico $\ell$; $\eta$ real → $\eta_{-\ell}=\eta_\ell^*$.
La parte periódica de la onda de Bloch (7.2-4):

$$p_K(z)=\sum_{m=-\infty}^{\infty}C_m\exp(-jmgz), \tag{7.2-21}$$

$$H_y(z)=\sum_{m=-\infty}^{\infty}C_m\exp[-j(K+mg)z]. \tag{7.2-22}$$

Sustituyendo en (7.2-2) e igualando armónicos de igual frecuencia espacial:

$$\sum_{\ell=-\infty}^{\infty}F_{m\ell}C_\ell=\frac{\omega^2}{c_o^2}C_m,\qquad F_{m\ell}=(K+mg)(K+\ell g)\,\eta_{m-\ell}, \tag{7.2-23}$$

$m=0,\pm1,\pm2,\dots$ Problema de autovalores matricial para $\{C_m\}$: para cada $K$, autovalores
$\omega^2/c_o^2$ → múltiples $\omega$ → relación $\omega$–$K$; autovectores $\{C_m\}$ → $p_K(z)$. Como
$\eta_{m-\ell}=\eta_{\ell-m}^*$, $\mathbf F$ es hermítica ($F_{m\ell}=F_{\ell m}^*$). Con la ecuación de $\mathbf E$ la
matriz sería no hermítica (por eso se usa $\mathbf H$; nota al pie p. 275: el operador de (7.0-2) es hermítico,
el del campo eléctrico no).

**Solución aproximada (p. 275–277).** Los armónicos de la onda se acoplan vía los armónicos del medio:
armónico óptico $K+\ell g$ × armónico del medio $(m-\ell)g$ → contribuye al armónico óptico $K+mg$.
Separando el término $m$ de (7.2-23):

$$C_m=\sum_{\ell\neq m}\frac{\eta_{m-\ell}}{\eta_o}\frac{(K+\ell g)(K+mg)}{(\bar n\omega/c_o)^2-(K+mg)^2}C_\ell,\quad m=0,\pm1,\pm2,\dots, \tag{7.2-24}$$

$\bar n=1/\sqrt{\eta_0}$ índice promedio. Acoplamiento fuerte si el denominador es pequeño:

$$\omega\bar n/c_o\approx|K+mg|. \tag{7.2-25}$$

Condición de resonancia entre armónicos; también **condición de ajuste de fase (phase matching)**
(p. 276). Fig. 7.2-8 (p. 276): (7.2-25) como igualdad, curvas en V para cada $m$; las intersecciones de la
curva $m=0$ (punteada) con $m=-1,-2,\dots$ (círculos llenos) son los bandgaps de orden 1, 2, …; en cada
una $K$ es múltiplo entero de $\tfrac12g$ y $\omega$ múltiplo de $\omega_{\mathcal B}=(c_o/\bar n)g/2$, o
$\nu_{\mathcal B}=(c_o/\bar n)/2\Lambda$; corresponde a la **longitud de onda de Bragg $\lambda_{\mathcal B}=2\Lambda$** en el
medio → reflexión total. Intersecciones sin marcar no son independientes (mismo $\omega$, $K$ difiere en $g$).

Bandgap de orden más bajo: intersección $m=0$ con $m=-1$ (punto 1); solo $C_0$ y $C_{-1}$ se acoplan
fuertemente:

$$C_0=\frac{\eta_1}{\eta_0}\frac{(K-g)K}{\omega^2\bar n^2/c_o^2-K^2}C_{-1}, \tag{7.2-26}$$

$$C_{-1}=\frac{\eta_1^*}{\eta_0}\frac{K(K-g)}{\omega^2\bar n^2/c_o^2-(K-g)^2}C_0, \tag{7.2-27}$$

$\eta_{-1}=\eta_1^*$. Autoconsistencia (recuadro **Dispersion Relation**, p. 276):

$$\frac{|\eta_1|^2}{\eta_0^2}K^2(K-g)^2=\left[\omega^2\frac{\bar n^2}{c_o^2}-K^2\right]\left[\omega^2\frac{\bar n^2}{c_o^2}-(K-g)^2\right]. \tag{7.2-28}$$

Válida cerca del borde del gap (Fig. 7.2-9, p. 277). En $K=\tfrac12g$ da dos frecuencias:

$$\omega_\pm=\omega_{\mathcal B}\sqrt{1\pm|\eta_1|/\eta_0}, \tag{7.2-29}$$

bordes del primer bandgap; centro en $\omega_{\mathcal B}=(c_o/\bar n)(g/2)=(\pi/\Lambda)(c_o/\bar n)$. La razón
ancho del gap / frecuencia central (**gap-midgap ratio**) crece con el contraste de impermeabilidad
$|\eta_1|/\eta_0$ (p. 277). El gap de orden $m$ se obtiene con la misma fórmula sustituyendo $|\eta_m|/\eta_0$:
los gaps superiores los gobiernan los armónicos espaciales superiores de $\eta(z)$.

**Ondas fuera de eje (p. 277).** TM en el plano $x$–$z$, ecuación (7.2-3); onda de Bloch:

$$H_y(z)=\sum_{m=-\infty}^{\infty}C_m\exp[-j(K+mg)z]\exp(-jk_xx), \tag{7.2-30}$$

$$\sum_{\ell=-\infty}^{\infty}F_{m\ell}C_\ell=\frac{\omega^2}{c_o^2}C_m,\qquad F_{m\ell}=[(K+\ell g)(K+mg)+k_x^2]\,\eta_{m-\ell}. \tag{7.2-31}$$

Generaliza (7.2-23); se resuelve para cada par $(K,k_x)$.

#### 7.2D Boundaries Between Periodic and Homogeneous Media (p. 277)

Hasta ahora el medio periódico era infinito. Ahora: reflexión/transmisión en fronteras. Otras
configuraciones (láminas o huecos en medios periódicos): §9.4 y §10.4D.

**Reflexión omnidireccional en una frontera única (p. 278).** Frontera entre medio homogéneo
semi-infinito y medio periódico 1D semi-infinito (Fig. 7.2-10). Gobernada por el ajuste de fase: $k_x$
debe conservarse ($k_x=k\sin\theta=(\omega/c_o)n\sin\theta$; origen de Snell, §2.4A). Conociendo $k_x$ y $\omega$, la
relación $\omega=\omega(K,k_x)$ del medio periódico (polarización adecuada) da $K$; si $\omega$ cae en un gap para
ese $k_x$, la onda no se propaga en el medio periódico y se refleja totalmente. Región accesible desde el
medio homogéneo: $k_x=(\omega/c_o)n\sin\theta$ → $k_x<(\omega/c_o)n$, i.e. $\omega>(c_o/n)k_x$; acotada por la **light
line** $\omega=(c_o/n)k_x$, o $\omega/\omega_{\mathcal B}=(\bar n/n)[k_x/(g/2)]$, que corresponde a $\theta=90°$ en el medio
externo. Fig. 7.2-10 (p. 279) = Fig. 7.2-7 + light lines para $n=1$ (aire). **En la banda espectral entre
$\omega_1$ y $\omega_2$ todos los puntos $\omega$–$k_x$ dentro de las light lines caen en un bandgap: ninguna
onda incidente, de cualquier ángulo o polarización, puede acoplarse a un modo propagante → la frontera
es un reflector omnidireccional perfecto.** Hay una segunda banda así a frecuencias mayores.

**Lámina de material periódico en medio homogéneo (p. 278–279).** Es una rejilla de Bragg con $N$
finito (§7.1C). Passbands/stop bands de la rejilla coinciden matemáticamente con bandas/bandgaps del
medio infinito; pero la transmitancia/reflectancia espectral de la rejilla tiene oscilaciones sensibles
a $N$ y a las fronteras, sin contraparte en el medio infinito. Índices efectivos para la rejilla: se
define $\arg\{\mathrm t_N\}=(\omega/c_o)n_{\rm eff}d$ (medio homogéneo equivalente de espesor $d$) y
$N_{\rm eff}=n_{\rm eff}+\omega\,dn_{\rm eff}/d\omega$ [ver (5.6-2)]; oscilan dentro de las passbands, pero para $N$
grande (> 100) se lavan y coinciden con los del medio infinito (p. 279).

Lámina homogénea embebida en medio periódico: la luz queda atrapada por reflexión omnidireccional → guía
de onda (§8.4) (p. 279).

---

### 7.3 Two- and Three-Dimensional Photonic Crystals (p. 279)

Generalización de Bloch y de $\omega$–$K$. 2D: bandgaps **2D-completos** (comunes a ambas polarizaciones y
a toda dirección en el plano de periodicidad). Bandgaps **3D-completos** (todas direcciones y
polarizaciones) solo en 3D (p. 279).

#### 7.3A Two-Dimensional Photonic Crystals (p. 280)

**Estructuras periódicas 2D (p. 280).** Barras/tubos paralelos en retículo rectangular (Fig. 7.3-1);
$\eta(x,y)=\epsilon_o/\epsilon(x,y)$ periódica en $x,y$, uniforme en $z$; periodos $a_1,a_2$:

$$\eta(x+m_1a_1,y+m_2a_2)=\eta(x,y), \tag{7.3-1}$$

$$\eta(x,y)=\sum_{\ell_1=-\infty}^{\infty}\sum_{\ell_2=-\infty}^{\infty}\eta_{\ell_1,\ell_2}\exp(-j\ell_1g_1x)\exp(-j\ell_2g_2x), \tag{7.3-2}$$

$g_1=2\pi/a_1$, $g_2=2\pi/a_2$. [Nota: el libro imprime $\exp(-j\ell_2g_2x)$ en el segundo factor; por
contexto debería ser $\exp(-j\ell_2g_2y)$.] La transformada de Fourier 2D es un conjunto de deltas en un
retículo rectilíneo: el **retículo recíproco** (Fig. 7.3-1c). Modos 2D de Bloch (ondas paralelas al
plano $x$–$y$):

$$U(x,y)=p_{K_x,K_y}(x,y)\exp(-jK_xx)\exp(-jK_yy), \tag{7.3-3}$$

$(K_x,K_y)$ = par de números de onda de Bloch; $(K_x+g_1,K_y+g_2)$ no es modo nuevo; primera zona de
Brillouin: rectángulo $[-g_1/2<K_x\le g_1/2]\times[-g_2/2<K_y\le g_2/2]$. Con todas las simetrías se reduce
a la **zona de Brillouin irreducible**; para retículo cuadrado ($a_1=a_2=a$) es el triángulo ΓMX (Fig.
7.3-1d).

**Estructuras 2D oblicuas (skew-periodic), p. 280–281.** Huecos cilíndricos en retículo triangular
(Fig. 7.3-2). Vectores primitivos $\mathbf a_1,\mathbf a_2$; vector de retículo $\mathbf R=m_1\mathbf a_1+m_2\mathbf a_2$;
$\epsilon(\mathbf r_T+\mathbf R)=\epsilon(\mathbf r_T)$, $\mathbf r_T=(x,y)$. Retículo recíproco: $\mathbf g_1,\mathbf g_2$ ortogonales a
$\mathbf a_1,\mathbf a_2$ respectivamente, módulos $g_1=2\pi/a_1\sin\theta$, $g_2=2\pi/a_2\sin\theta$ ($\theta$ = ángulo
entre $\mathbf a_1$ y $\mathbf a_2$); $\mathbf G=\ell_1\mathbf g_1+\ell_2\mathbf g_2$. Fig. 7.3-2: $a_1=a_2=a$, $\theta=120°$; zona
de Brillouin hexagonal; irreducible = triángulo ΓMK. Modos:

$$U(\mathbf r_T)=p_{\mathbf K}(\mathbf r_T)\exp(-j\mathbf K_T\cdot\mathbf r_T), \tag{7.3-4}$$

$\mathbf K_T=(K_x,K_y)$ vector de onda de Bloch; $\mathbf K_T$ y $\mathbf K_T+\mathbf G$ equivalentes. Relación de
dispersión: imponer que (7.3-3) o (7.3-4) satisfagan Helmholtz generalizada, vía Fourier (p. 281).

**Ejemplo 7.3-1. Huecos cilíndricos en retículo triangular (p. 281–282, Fig. 7.3-3).** Medio $n=3{.}6$
con huecos de aire de radio $0{.}48a$ en retículo triangular de constante $a$. Relación de dispersión
calculada para TE y TM en el plano ($k_z=0$): bandgap 2D-completo cerca de $\omega_0=\pi c_o/a$. Abscisa:
$\mathbf K_T$ sobre el perímetro del triángulo ΓMK; ordenada en unidades de $\omega_0$. Gap más ancho con mayor
contraste; la mayoría de geometrías presentan gaps si el contraste es suficiente. Esta estructura es la
de las fibras "holey" (§9.4). (Nota al pie: S. G. Johnson y J. D. Joannopoulos, *Opt. Express* 8,
173–190, 2001.)

Onda oblicua respecto al plano $x$–$y$ (p. 282):

$$U(\mathbf r_T)=p_{\mathbf K}(\mathbf r_T)\exp(-j\mathbf K_T\cdot\mathbf r_T)\exp(-jk_zz), \tag{7.3-5}$$

$k_z$ constante; bandas = superficies $\omega=\omega(\mathbf K_T,k_z)$. Bandgap 3D-completo = $\omega$ no alcanzado por
ninguna combinación de $\mathbf K_T$, $k_z$ reales. **En 2D hay gap completo para $k_z=0$ pero no para todas
las ondas fuera del plano** (p. 282).

#### 7.3B Three-Dimensional Photonic Crystals (p. 282)

**Estructura cristalina (p. 282–283).** Duplicados de una estructura básica (esfera, cubo) en puntos de
un retículo 3D $\mathbf R=m_1\mathbf a_1+m_2\mathbf a_2+m_3\mathbf a_3$ ($\mathbf a_i$ vectores primitivos):

$$\eta(\mathbf r+\mathbf R)=\eta(\mathbf r), \tag{7.3-6}$$

$$\eta(\mathbf r)=\sum_{\mathbf G}\eta_{\mathbf G}\exp(-j\mathbf G\cdot\mathbf r), \tag{7.3-7}$$

$\mathbf G=\ell_1\mathbf g_1+\ell_2\mathbf g_2+\ell_3\mathbf g_3$ (retículo recíproco), con

$$\mathbf g_1=2\pi\frac{\mathbf a_2\times\mathbf a_3}{\mathbf a_1\cdot\mathbf a_2\times\mathbf a_3},\quad \mathbf g_2=2\pi\frac{\mathbf a_3\times\mathbf a_1}{\mathbf a_1\cdot\mathbf a_2\times\mathbf a_3},\quad \mathbf g_3=2\pi\frac{\mathbf a_1\times\mathbf a_2}{\mathbf a_1\cdot\mathbf a_2\times\mathbf a_3}, \tag{7.3-8}$$

$\mathbf g_1\cdot\mathbf a_1=2\pi$, $\mathbf g_1\cdot\mathbf a_2=\mathbf g_1\cdot\mathbf a_3=0$; $\mathbf G\cdot\mathbf R=2\pi$ [sic; en general múltiplo
entero de $2\pi$]. Si los $\mathbf a_i$ son ortogonales, los $\mathbf g_i$ también y $g_i=2\pi/a_i$. Fig. 7.3-4
(p. 283): esferas dieléctricas en retículo diamante (fcc) con $\mathbf a_1=(a/\sqrt2)(\hat{\mathbf x}+\hat{\mathbf y})$,
$\mathbf a_2=(a/\sqrt2)(\hat{\mathbf y}+\hat{\mathbf z})$, $\mathbf a_3=(a/\sqrt2)(\hat{\mathbf x}+\hat{\mathbf z})$; retículo recíproco bcc;
zona de Brillouin = celda de Wigner–Seitz; irreducible = poliedro con vértices ΓXULKW.

**Modos de Bloch 3D (p. 283–284).** $p_{\mathbf K}(\mathbf r)\exp(-j\mathbf K\cdot\mathbf r)\hat{\mathbf e}$, $\mathbf K$ = **Bloch
wavevector**, $\hat{\mathbf e}$ polarización; traslación por $\mathbf R$ → factor $\exp(-j\mathbf K\cdot\mathbf R)$. $\mathbf K$ y
$\mathbf K+\mathbf G$ equivalentes ($\exp(-j\mathbf G\cdot\mathbf R)=1$). Zona de Brillouin = volumen de puntos más cercanos
al origen Γ del retículo recíproco que a cualquier otro punto; con simetrías → zona irreducible.

**Estructura de bandas fotónicas (p. 284).** Fourier 3D:

$$p_{\mathbf K}(\mathbf r)=\sum_{\mathbf G}C_{\mathbf G}\exp(-j\mathbf G\cdot\mathbf r), \tag{7.3-9}$$

$$\mathbf H(\mathbf r)=p_{\mathbf K}(\mathbf r)\exp(-j\mathbf K\cdot\mathbf r)\hat{\mathbf e}=\sum_{\mathbf G}C_{\mathbf G}\exp[-j(\mathbf K+\mathbf G)\cdot\mathbf r]\hat{\mathbf e}. \tag{7.3-10}$$

Sustituyendo (7.3-7) y (7.3-10) en (7.0-2), con
$\nabla\times\exp(-j\mathbf K\cdot\mathbf r)\hat{\mathbf e}=-j(\mathbf K\times\hat{\mathbf e})\exp(-j\mathbf K\cdot\mathbf r)$:

$$-\sum_{\mathbf G'}(\mathbf K+\mathbf G)\times\left[(\mathbf K+\mathbf G')\times\hat{\mathbf e}\right]\eta_{\mathbf G-\mathbf G'}C_{\mathbf G'}=\frac{\omega^2}{c_o^2}C_{\mathbf G}\hat{\mathbf e}. \tag{7.3-11}$$

Producto punto con $\hat{\mathbf e}$ e identidad $\mathbf A\cdot(\mathbf B\times\mathbf C)=-(\mathbf B\times\mathbf A)\cdot\mathbf C$:

$$\sum_{\mathbf G'}F_{\mathbf G\mathbf G'}C_{\mathbf G'}=\frac{\omega^2}{c_o^2}C_{\mathbf G},\qquad F_{\mathbf G\mathbf G'}=\left[(\mathbf K+\mathbf G)\times\hat{\mathbf e}\right]\cdot\left[(\mathbf K+\mathbf G')\times\hat{\mathbf e}\right]\eta_{\mathbf G-\mathbf G'}. \tag{7.3-12}$$

$\eta$ real → $\eta_{\mathbf G-\mathbf G'}=\eta^*_{\mathbf G'-\mathbf G}$ → $F_{\mathbf G\mathbf G'}$ hermítica. Para cada $\mathbf K$, autovalores
$\omega^2/c_o^2$ → diagrama $\omega$–$\mathbf K$ y estructura de bandas; autovectores $\{C_{\mathbf G}\}$ → $p_{\mathbf K}(\mathbf r)$.

**Ejemplos 3D (p. 285–286):**
- **Huecos esféricos en retículo diamante (Fig. 7.3-5, p. 285):** esferas de aire de radio $0{.}325a$ en
  material $n=3{.}6$, solapadas (forman venas); bandgap 3D-completo entre las dos bandas más bajas, de
  $\omega_0=\pi c_o/a$ a $1{.}32\,\omega_0$ aprox. Fabricadas en silicio creciéndolo en los huecos de un ópalo de
  esferas de sílice sinterizadas y removiendo la plantilla (Blanco *et al.*, *Nature* 405, 437, 2000).
- **Yablonovite (Fig. 7.3-6a):** primera observación experimental de gap 3D completo (Yablonovitch,
  1991); variante del diamante: tres huecos cilíndricos perforados en cada punto de un retículo
  triangular superficial, a $35°$ de la normal y separados $120°$ en azimut; gap-midgap ratio 0.19 con
  $n=3{.}6$.
- **Woodpile (Fig. 7.3-6b):** pila 1D de capas, cada una un cristal 2D de "troncos" paralelos; capas
  adyacentes rotadas $90°$, desplazadas medio paso cada dos capas; secuencia que se repite cada cuatro
  capas; simetría tetragonal centrada en caras. En silicio con feature mínimo 180 nm: gap 3D completo
  para $\lambda=1{.}35$–$1{.}95\ \mu$m (Fleming y Lin, *Opt. Lett.* 24, 49, 1999).
- **Holes and poles (Fig. 7.3-6c):** capas alternadas de huecos cilíndricos en retículo hexagonal y de
  postes alineados con los huecos; en silicio, stop band para todos los ángulos en $\lambda=1{.}15$–$1{.}6\ \mu$m
  (Qi *et al.*, *Nature* 429, 538, 2004).
- Woodpile y holes-and-poles permiten introducir **defectos puntuales** (hueco o barra faltante) →
  guías de cristal fotónico (§8.5), nanorresonadores (§10.4D), emisores controlados (cap. 17). La
  posibilidad de insertar defectos es la ventaja principal de 2D/3D, pues los 1D ya sirven bien como
  reflectores omnidireccionales (p. 286).

---

### Reading List (p. 286–288)

Libros sobre medios por capas y periódicos: Višňovský (2006), Stenzel (2005), **P. Yeh, *Optical Waves in
Layered Media*, Wiley 2005**, Brillouin (1953/2003), Nevière & Popov (2003), Born & Wolf (7.ª ed. 2002,
§1.6), **Kashyap, *Fiber Bragg Gratings* (1999)**, Chew (1990), Yariv & Yeh (1985). Libros sobre cristales
fotónicos: Yasumoto (2006), Lourtioz *et al.* (2005), Sakoda (2.ª ed. 2005), Busch *et al.* (2004), Inoue &
Ohtaka (2004), Noda & Baba (2003), Kochergin (2003), **Slusher & Eggleton, *Nonlinear Photonic Crystals*
(2003)**, Johnson & Joannopoulos (2002), Soukoulis (1996), **Joannopoulos, Meade & Winn, *Photonic
Crystals: Molding the Flow of Light* (1995)**, Senechal (1995). Artículos: Yablonovitch PRL 58, 2059 (1987);
John PRL 58, 2486 (1987); Yablonovitch & Gmitter JOSA A 7, 1792 (1990); Yablonovitch, Gmitter & Leung
PRL 67, 2295 (1991); Fink *et al.*, *Science* 282, 1679 (1998) (reflector omnidireccional dieléctrico);
Johnson & Joannopoulos *Opt. Express* 8, 173 (2001); etc.

---

## Tablas y datos numéricos útiles

| Dato | Valor | Página |
|---|---|---|
| Finesse de etalón con $\mathrm r_1\mathrm r_2=0{.}99$ | $\mathcal F\approx313$ | 255 |
| Etalón $d=1{.}5$ cm, $n=1$ | $\nu_F=10$ GHz; con $\nu=10^{14}$ Hz ($q=10^4$), $\Delta d=1{.}5\ \mu$m → $\Delta\nu_q=10$ GHz, $\Delta\nu_F=1$ MHz | 256 |
| Índice SiO₂ (ejemplo del libro) | $n_1=1{.}5$ | 256, 263 |
| Índice Si (ejemplo del libro) | $n_2=3{.}5$ | 256, 263 |
| Finesse de lámina Si en SiO₂ | $\mathcal F=\frac{\pi}{4}\frac{|n_2^2-n_1^2|}{n_1n_2}=1{.}68$ | 256 |
| Ángulo de Bragg para $\nu=1{.}5\nu_{\mathcal B}$ | $\theta=48{.}2°$ desde el eje; $\theta_{\mathcal B}=41{.}8°$ desde el plano | 258 |
| Rejilla $N=10$ espejos, $\mathcal R=0{.}5$: máximo en passband | $\mathcal R_N\approx0{.}99$ | 261 |
| Rejilla $N=10$ espejos, $|\mathrm t|^2=0{.}5$: $\Psi_N$ en centro de stop band | $\approx3000$ | 262 |
| Rejilla dieléctrica $N=10$, $n_1=1{.}5/n_2=3{.}5$, $d_1=d_2$, en aire | $\mathcal R=1$ a todo ángulo y polarización para $0{.}97\nu_{\mathcal B}$–$1{.}18\nu_{\mathcal B}$ | 264 |
| Ángulo de Brewster capas 1.5/3.5 (desde capa 1) | $\theta_B=\tan^{-1}(n_2/n_1)=66{.}8°$ | 274 |
| Cristal 2D huecos de aire en $n=3{.}6$, retículo triangular | radio $0{.}48a$; gap 2D completo cerca de $\omega_0=\pi c_o/a$ | 281–282 |
| Cristal 3D esferas de aire en diamante, $n=3{.}6$ | radio $0{.}325a$; gap de $\omega_0=\pi c_o/a$ a $1{.}32\omega_0$ | 285 |
| Yablonovite, $n=3{.}6$ | gap-midgap ratio 0.19; huecos a $35°$ de la normal, $120°$ en azimut | 285–286 |
| Woodpile en Si (feature 180 nm) | gap 3D completo $\lambda=1{.}35$–$1{.}95\ \mu$m | 285 |
| Holes-and-poles en Si | stop band $\lambda=1{.}15$–$1{.}6\ \mu$m, todos los ángulos | 286 |
| GaAs / AlAs (Prob. 7.1-7) | $n_1=3{.}57$, $n_2=2{.}94$ | 288 |
| Prob. 7.2-1 | $n_1=1{.}5$, $n_2=3{.}5$, $\Lambda=2\ \mu$m; repetir con $3{.}4/3{.}6$ | 288 |

Fórmulas rápidas de referencia (todas en este capítulo):
- Medio homogéneo: $\varphi=nk_od$ (normal), $\varphi=nk_od\cos\theta$ (oblicuo). (p. 248, 253)
- Frontera normal: $\mathrm t_{12}=2n_1/(n_1+n_2)$, $\mathrm r_{12}=(n_1-n_2)/(n_1+n_2)$, $\mathrm r_{21}=-\mathrm r_{12}$. (p. 251–252)
- Oblicuo: TE $\tilde n=n\cos\theta$; TM $\tilde n=n\sec\theta$. (p. 253)
- FP: $\nu_F=c/2d$, $\delta\nu=\nu_F/\mathcal F$, $\mathcal F=\pi\sqrt{|\mathrm r_1\mathrm r_2|}/(1-|\mathrm r_1\mathrm r_2|)$. (p. 254–255)
- Bragg: $\nu_{\mathcal B}=c/2\Lambda$, $\omega_{\mathcal B}=\pi c/\Lambda$, $\lambda_{\mathcal B}=2\Lambda$ (en el medio), $g=2\pi/\Lambda$,
  $\bar n=(n_1d_1+n_2d_2)/\Lambda$, $c=c_o/\bar n$. (p. 258, 262, 271, 276)
- Relación de dispersión 1D: $\cos(K\Lambda)=\mathrm{Re}\{1/\mathrm t(\omega)\}$; gap si $|\mathrm{Re}\{1/\mathrm t\}|>1$. (p. 270–271)
- Primer gap (Fourier): $\omega_\pm=\omega_{\mathcal B}\sqrt{1\pm|\eta_1|/\eta_0}$. (p. 276)

---

## Problemas al final del capítulo (p. 288)

Ninguno aparece marcado con asterisco en el libro (no hay problemas "avanzados" señalados en esta
lista). No hay problemas de la sección 7.3. La numeración empieza en 7.1-2 porque 7.1-1 es el ejercicio
dentro del texto (p. 252).

- **7.1-2 Beamsplitter Slab.** Lámina dieléctrica sin pérdidas ($n$, $d$) a $45°$ como divisor de haz:
  derivar transmitancia y reflectancia y esbozar su dependencia espectral para TE y TM.
- **7.1-3 Air Gap in Glass.** Transmitancia de una brecha de aire plana de ancho $d=\lambda/2$ en vidrio de
  índice $n$: (a) incidencia normal; (b) onda TE con ángulo mayor que el crítico. ¿Puede la onda
  tunelar a través de la brecha?
- **7.1-4 Multilayer Device in an Unmatched Medium.** Si un dispositivo multicapa tiene reflectancia $\mathrm r_m$
  en medio ajustado $n_1$, mostrar que en un medio $n$ la reflectancia es $\mathrm r=(\mathrm r_b+\mathrm r_m)/(1+\mathrm r_b\mathrm r_m)$,
  $\mathrm r_b=(n-n_1)/(n+n_1)$; evaluar los límites $\mathrm r_b=0$, $\mathrm r_b=1$, $\mathrm r_m=0$, $\mathrm r_m=1$.
- **7.1-5 Quarter-Wave Film: Angular Dependence of Reflectance.** Para el recubrimiento antirreflejante
  del Ejercicio 7.1-1, derivar la reflectancia en función del ángulo de incidencia.
- **7.1-6 Quarter-Wave and Half-Wave Stacks.** Reflectancia de una pila de $N$ dobles capas de igual
  espesor óptico $n_1d_1=n_2d_2$, igual a $\lambda_o/4$ y a $\lambda_o/2$.
- **7.1-7 GaAs/AlAs Bragg Grating Reflector.** $N$ unidades GaAs ($n_1=3{.}57$) / AlAs ($n_2=2{.}94$) de
  cuarto de onda cada una, en GaAs extendido; calcular y graficar $\mathcal T$ y $\mathcal R$ vs. $N=1,\dots,10$ a
  la frecuencia de Bragg.
- **7.1-8 Bragg Grating: Angular and Spectral Dependence of Reflectance.** Programa de álgebra matricial
  para la matriz de transferencia y la reflectancia de una rejilla de $N$ capas alternadas; verificar
  las Figs. 7.1-12 y 7.1-13.
- **7.2-1 Gap–Midgap Ratio.** Con el enfoque de Fourier, determinar la frecuencia de Bragg y el
  gap-midgap ratio del gap más bajo para capas de igual espesor óptico con $n_1=1{.}5$, $n_2=3{.}5$,
  $\Lambda=2\ \mu$m (onda en eje); repetir con $n_1=3{.}4$, $n_2=3{.}6$; comparar.
- **7.2-2 Off-Axis Wave in 1D Periodic Medium.** Derivar las ecuaciones análogas a (7.2-24)–(7.2-28)
  para onda fuera de eje con vector de onda transversal $k_x$.
- **7.2-3 Normal-to-Axis Wave in a 1D Periodic Medium.** Con los resultados de 7.2-2, mostrar que no hay
  bandgaps para una onda que viaja lateralmente ($K=0$).
- **7.2-4 Omnidirectional Reflector.** Pila periódica de dobles capas con $n_1d_1=n_2d_2$, $n_2=2n_1$,
  $\Lambda=d_1+d_2$ como reflector omnidireccional en aire: graficar la dispersión proyectada con la light
  line del aire (como Fig. 7.2-10) y determinar el rango de frecuencias (en unidades de $\omega_{\mathcal B}$)
  de reflexión omnidireccional.

---

## Relación con Óptica No Lineal

**Con los temas del curso:**

- *Ondas EM y Helmholtz en medios inhomogéneos.* Las ecuaciones (7.0-1)/(7.0-2) (p. 245) son la
  versión de autovalores de la ecuación de onda con $\epsilon(\mathbf r)$; el mismo punto de partida que
  la ecuación de onda no lineal de Boyd (§2.1) antes de añadir $\mathbf P^{NL}$ como fuente. La
  discusión sobre por qué el operador para $\mathbf H$ es hermítico y el de $\mathbf E$ no (p. 275,
  284) es útil para entender métodos numéricos de modos (MPB, FDE de Lumerical).
- *Absorción y dispersión / pulsos en medios dispersivos / GVD.* §7.2B (p. 272–273) define
  $n_{\rm eff}=c_oK/\omega$ y el índice de grupo $N_{\rm eff}=c_o\,dK/d\omega$ a partir de la curva $\omega$–$K$,
  y muestra que **cerca de los bordes del bandgap la velocidad de grupo cae ("slow light")** y la
  curvatura de $\omega(K)$ (GVD) es enorme. Es dispersión *estructural* (geométrica), no material: el
  mismo mecanismo que da la dispersión de guía en guías de Si₃N₄ y permite diseñar GVD anómala para
  solitones y supercontinuo. La definición de índices efectivos para una rejilla finita vía
  $\arg\{\mathrm t_N\}=(\omega/c_o)n_{\rm eff}d$ (p. 279) es exactamente cómo se extrae $n_g$ de una respuesta
  espectral simulada.
- *Polarización y cristales.* El capítulo distingue TE/TM en todas las fórmulas oblicuas
  ($\tilde n=n\cos\theta$ vs. $n\sec\theta$, p. 253) y muestra que en TM a Brewster no hay gap (p. 274): base
  para entender la dependencia en polarización de rejillas y de reflectores omnidireccionales.
- *Condición de ajuste de fase (phase matching).* La ecuación (7.2-25) $\omega\bar n/c_o\approx|K+mg|$
  (p. 276) es formalmente la condición de **quasi-phase-matching**: el armónico $g=2\pi/\Lambda$ del
  medio aporta el vector de onda que falta, igual que el vector de red $K_m=2\pi m/\Lambda$ en cristales
  periódicamente polarizados (PPLN) para SHG/DFG. Las ecuaciones acopladas (7.2-26)–(7.2-27) tienen la
  misma estructura que las ecuaciones de modos acoplados de la teoría de rejillas de Bragg en fibra
  (Kashyap, en la lista de lectura), que a su vez es la base de los **solitones de gap** y de la
  **biestabilidad en rejillas no lineales** (Slusher & Eggleton, *Nonlinear Photonic Crystals*, también
  en la lista).
- *Susceptibilidades $\chi^{(2)}$, $\chi^{(3)}$, índice dependiente de la intensidad, SPM/XPM, Raman, FWM.*
  El capítulo es lineal, pero provee el "andamio": (i) un Fabry-Perot con medio Kerr es el ejemplo
  canónico de biestabilidad óptica — (7.1-32)/(7.1-36) con $\varphi=n(I)k_od$ dependiente de la intensidad;
  (ii) la densidad de estados y el slow light en bordes de banda amplifican efectos $\chi^{(3)}$ (SPM,
  FWM, Raman) por el factor $(N_{\rm eff}/n)^2$; (iii) los cristales fotónicos 2D/3D con defectos
  puntuales (p. 286) son los nanorresonadores donde se busca $\chi^{(2)}$/$\chi^{(3)}$ eficiente a baja
  potencia.

**Con el proyecto final (anillos add-drop en Si₃N₄, sensado de índice):**

- *Matrices de transferencia y de scattering (§7.1A, p. 246–251).* Es el formalismo exacto que se usa
  para modelar un **anillo add-drop**: el acoplador direccional es una matriz $\mathbf S$ recíproca sin
  pérdidas de la forma (7.1-16) ($\mathrm t=|\mathrm t|$, $\mathrm r=j|\mathrm r|$ ↔ $t$ y $j\kappa$ del acoplador, con
  $|t|^2+|\kappa|^2=1$), y la propagación por medio anillo es (7.1-4) con $\varphi=n_{\rm eff}k_oL/2$ (más un
  factor de pérdidas $e^{-\alpha L/4}$ si se incluye atenuación). Multiplicar $\mathbf M$ y convertir a $\mathbf S$
  con (7.1-6) da directamente la transmisión through y drop. Las fórmulas de Airy (7.1-8, p. 249) son
  la transmisión del anillo como función de la fase de vuelta completa: $1-\mathrm r_{21}\mathrm r_{23}e^{-j2\varphi}$
  es el denominador resonante del anillo ($1-t_1t_2 a e^{-j\theta}$).
- *Fabry-Perot (§7.1B, p. 254–257) ↔ anillo.* Las definiciones son las mismas que se miden en el
  espectro del anillo: **FSR** $\nu_F=c/2d$ → para el anillo $\nu_F=c_o/(n_gL)$; **finesse** (7.1-34) y
  **ancho de línea** $\delta\nu=\nu_F/\mathcal F$ (7.1-37) → $Q=\nu/\delta\nu$; transmitancia lorentziana-periódica
  (7.1-36). La sintonía $\Delta\nu_q=-\nu_q\,\Delta d/d$ (p. 255–256) es el análogo exacto de la **sensibilidad
  de un refractómetro resonante**: $\Delta\nu_q/\nu_q=-\Delta(n_{\rm eff}L)/(n_{\rm eff}L)$, i.e.
  $\Delta\lambda_{\rm res}=\lambda\,\Delta n_{\rm eff}/n_g$; el ejemplo numérico de p. 256 (cambio relativo $10^{-4}$
  de camino óptico → corrimiento de un FSR entero) sirve de verificación de órdenes de magnitud para el
  barrido $n_{\rm clad}=1{.}33\to1{.}37$. La discusión de que el ancho espectral de la luz debe ser $<\nu_F$
  para evitar ambigüedad (p. 255) aplica igual al rango de medida del sensor.
- *Espejo de Bragg / rejilla (§7.1C, p. 257–264).* (7.1-54) y los regímenes de $\Phi$ real/complejo
  describen cualquier reflector distribuido: útil si se quiere cerrar la cavidad con DBR en vez de
  acopladores, o para interpretar stop bands en guías corrugadas; la forma (7.1-63) para medio no
  ajustado es el esquema correcto cuando hay fronteras de entrada/salida (p. 264). Las Figs. 7.1-11 a
  7.1-13 son referencia visual de cómo se ven stop bands y lóbulos laterales en un espectro simulado.
- *Dispersión de guías y supercontinuo.* La construcción $\omega$–$K$ → $n_{\rm eff}$, $N_{\rm eff}$ (p. 272–273)
  y la relación $N_{\rm eff}=n_{\rm eff}+\omega\,dn_{\rm eff}/d\omega$ (p. 279, ec. 5.6-2) son las que se aplican al
  barrido FDE de la guía de Si₃N₄ para obtener $n_g(\lambda)$ y $\beta_2$. Los cristales fotónicos 2D (p.
  280–282, fibras holey §9.4) son la alternativa clásica para ingeniería de dispersión en supercontinuo.
- *Sensado de índice.* La reflexión omnidireccional y las light lines (p. 278–279) muestran cómo el
  índice del medio externo $n$ (cladding/analito) desplaza la región accesible $\omega>(c_o/n)k_x$; en el
  anillo, el análogo es el corrimiento de $n_{\rm eff}$ con $n_{\rm clad}$ (fracción de campo evanescente),
  que el formalismo $\mathbf M$/$\mathbf S$ convierte en corrimiento de resonancia.
