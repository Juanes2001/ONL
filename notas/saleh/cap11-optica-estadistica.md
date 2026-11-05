# Capítulo 11 — Statistical Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 403–443 (PDF 425–465). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 11
"Statistical Optics". Notación del libro: dependencia temporal $e^{j\omega t}$, $j=\sqrt{-1}$;
$u(\mathbf r,t)=\mathrm{Re}\{U(\mathbf r,t)\}$ es la función de onda real y $U(\mathbf r,t)$ la
función de onda compleja; $\langle\cdot\rangle$ denota promedio de conjunto (ensemble). Las
intensidades son $|U|^2$ en W/cm² tal como las define el libro (unidades SI en todo lo demás).
Cuando el libro usa letras caligráficas (p. ej. $\mathcal S(\nu)$, $\mathcal V$, $\mathcal P$,
$\mathcal J$) aquí se escriben $S(\nu)$, $\mathcal V$, $\mathbb P$, $\mathcal J$ respectivamente.

Las ecuaciones marcadas con **[recuadro]** son las que el libro enmarca como resultados
principales.

---

## Resumen del capítulo

El capítulo introduce la teoría de la coherencia parcial: cómo describir la luz aleatoria (la que
emite un cuerpo caliente, la dispersada por superficies rugosas o medios turbulentos) con promedios
estadísticos en lugar de funciones deterministas. En §11.1 (p. 405) se definen la intensidad
promedio, la función de coherencia temporal $G(\tau)$ y su versión normalizada $g(\tau)$, el
tiempo y la longitud de coherencia, la densidad espectral de potencia (teorema de Wiener–Khinchin)
y la relación inversa entre ancho espectral y tiempo de coherencia; después se generalizan al
espacio con la función de coherencia mutua $G(\mathbf r_1,\mathbf r_2,\tau)$, la intensidad mutua,
el área de coherencia y la densidad espectral cruzada, y se estudian ondas planas y esféricas
parcialmente coherentes (coherencia longitudinal). En §11.2 (p. 419) se deduce la ecuación de
interferencia para ondas parcialmente coherentes, la visibilidad $\mathcal V=|g_{12}|$, el
interferograma de Michelson, la espectroscopía por transformada de Fourier, la tomografía de
coherencia óptica (OCT), el interferómetro de Young con luz parcialmente coherente y la distancia
de coherencia $\rho_c\approx\lambda/\theta_s$. En §11.3 (p. 427, sección avanzada) se trata la
propagación de la intensidad mutua a través de sistemas ópticos lineales, la formación de imágenes
con iluminación incoherente (función de dispersión de punto, frecuencia de corte, resolución
$1.22\lambda/\theta$), la ganancia de coherencia espacial por propagación y el teorema de Van
Cittert–Zernike con el interferómetro estelar de Michelson. En §11.4 (p. 436) se introduce la
polarización parcial: matriz de coherencia $\mathbf G$, su transformación por dispositivos de
Jones, parámetros de Stokes, esfera de Poincaré, luz no polarizada y polarizada, y el grado de
polarización $\mathbb P$.

---

## Secciones

### Introducción del capítulo (p. 404–405)

- **Óptica estadística** = estudio de las propiedades de la luz aleatoria. La aleatoriedad proviene
  de fluctuaciones impredecibles de la fuente (luz natural: superposición de emisiones de muchos
  átomos independientes con frecuencias y fases distintas) o del medio (superficies rugosas, vidrio
  difusor, fluidos turbulentos). También se la llama **teoría de la coherencia óptica** (p. 404).
- Luz coherente = determinista, p. ej. la onda monocromática $u(\mathbf r,t)=\mathrm{Re}\{U(\mathbf
  r)\exp(j\omega t)\}$ con $U(\mathbf r)=A\exp(-jkr)/r$ (onda esférica). **Fig. 11.0-1** (p. 404):
  dependencia temporal y frentes de onda de (a) onda esférica monocromática (coherente) y (b) luz
  aleatoria (frentes de onda irregulares). **Fig. 11.0-2** (p. 404): tres ondas aleatorias; la (b)
  es más "intensa", la envolvente de la (c) fluctúa "más rápido".
- Como $u(\mathbf r,t)$ satisface la ecuación de onda y condiciones de frontera, sus promedios
  estadísticos también obedecen leyes. La teoría de coherencia define esos promedios, sus leyes y
  las medidas por las que la luz se clasifica como **coherente, incoherente o parcialmente
  coherente** (p. 405).
- Plan del capítulo (p. 405): §11.1 intensidad y función de coherencia mutua, coherencia temporal y
  espacial, relación con la monocromaticidad; §11.2 interferencia; §11.3 transmisión por sistemas
  ópticos; §11.4 polarización parcial. Se remarca que luz espacialmente coherente no tiene por qué
  ser temporalmente coherente, y luz monocromática no tiene por qué ser espacialmente coherente.

---

### 11.1 Statistical Properties of Random Light (p. 405)

Una onda óptica arbitraria se describe por $u(\mathbf r,t)=\mathrm{Re}\{U(\mathbf r,t)\}$ con
$U(\mathbf r,t)$ la función de onda compleja (p. ej. $U(\mathbf r)\exp(j\omega t)$ para luz
monocromática, o suma de muchas de ellas con distinta $\nu$ para luz policromática; ver §2.6A).
Para luz aleatoria tanto $u$ como $U$ son funciones aleatorias (p. 405).

#### 11.1A Optical Intensity (p. 405)

- Intensidad de luz coherente (determinista): $$I(\mathbf r,t)=|U(\mathbf r,t)|^2 \qquad (11.1\text{-}1)$$
  (ver §2.2A y §2.6A). Para luz monocromática es independiente del tiempo; para pulsos varía.
- **[recuadro] Intensidad promedio** (p. 405):
  $$I(\mathbf r,t)=\langle|U(\mathbf r,t)|^2\rangle \qquad (11.1\text{-}2)$$
  donde $\langle\cdot\rangle$ es el **promedio de conjunto** sobre muchas realizaciones (la onda se
  produce repetidamente bajo las mismas condiciones). Se la llama simplemente "intensidad";
  $|U(\mathbf r,t)|^2$ es la **intensidad aleatoria o instantánea**. Para luz determinista
  (11.1-2) ≡ (11.1-1) (p. 406).
- **Estacionariedad** (p. 406): la luz es estadísticamente estacionaria si sus promedios son
  invariantes en el tiempo; entonces $I(\mathbf r,t)=I(\mathbf r)$. No significa constancia de la
  onda sino de sus promedios. Ejemplo: lámpara incandescente con corriente constante. **Fig.
  11.1-1** (p. 406): (a) onda estacionaria: $|U|^2$ fluctúa, $I$ constante; (b) no estacionaria
  (pulso de corriente): $I(t)$ varía.
- Para luz estacionaria el promedio de conjunto suele poder sustituirse por un promedio temporal:
  $$I(\mathbf r)=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|U(\mathbf r,t)|^2\,dt \qquad (11.1\text{-}3)$$

#### 11.1B Temporal Coherence and Spectrum (p. 406)

Se consideran las fluctuaciones de luz *estacionaria* en una posición fija $\mathbf r$ (se omite
$\mathbf r$: $U(t)$, $I$). Las fluctuaciones tienen una escala de tiempo, la "memoria" del proceso:
dentro de ella la función parece suave; a escalas mayores, "rugosa" y errática (p. 406–407).

**Función de coherencia temporal** (p. 407). Autocorrelación de la función aleatoria compleja
estacionaria $U(t)$:
$$\textbf{[recuadro]}\quad G(\tau)=\langle U^*(t)\,U(t+\tau)\rangle \qquad (11.1\text{-}4)$$
o, como promedio temporal,
$$G(\tau)=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}U^*(t)\,U(t+\tau)\,dt \qquad (11.1\text{-}5)$$
(ver Apéndice A, §A.1). Interpretación con fasores (p. 407, **Fig. 11.1-2**: fasor $U(t)$ con
argumento uniforme en $[0,2\pi)$, de modo que $\langle U(t)\rangle=0$): la fase del producto
$U^*(t)U(t+\tau)$ es el ángulo entre los fasores $U(t)$ y $U(t+\tau)$; si están descorrelacionados
ese ángulo es uniforme y el promedio $G(\tau)$ se anula; si están correlacionados el producto tiene
una dirección preferente y $G(\tau)\neq0$.
Propiedades: simetría hermítica $G(-\tau)=G^*(\tau)$ y
$$I=G(0) \qquad (11.1\text{-}6)$$

**Grado de coherencia temporal** (p. 408). Medida de coherencia insensible a la intensidad:
$$\textbf{[recuadro]}\quad g(\tau)=\frac{G(\tau)}{G(0)}=\frac{\langle U^*(t)U(t+\tau)\rangle}{\langle U^*(t)U(t)\rangle} \qquad (11.1\text{-}7)$$
**grado complejo de coherencia temporal**, con
$$0\le|g(\tau)|\le1 \qquad (11.1\text{-}8)$$
Para luz determinista monocromática $U(t)=A\exp(j\omega_0 t)$:
$$g(\tau)=\exp(j\omega_0\tau) \qquad (11.1\text{-}9)$$
de modo que $|g(\tau)|=1$ para todo $\tau$ (correlación completa a todo retardo). En general
$|g(\tau)|$ decae desde $|g(0)|=1$ y las fluctuaciones se descorrelacionan para $\tau$ grande.

**Tiempo de coherencia** (p. 408–409). Si $|g(\tau)|$ decrece monótonamente, el valor $\tau_c$
en que cae a un valor prescrito ($\tfrac12$ o $1/e$) mide la memoria de las fluctuaciones. **Fig.
11.1-3** (p. 408): ejemplos de $u(t)$, $|g(\tau)|$ y $\tau_c$ para (a) tiempo de coherencia corto y
(b) largo; en ambos $\tau_c$ es mayor que un ciclo óptico; dentro de $\tau_c$ la onda es
aproximadamente sinusoidal, más allá no se puede predecir amplitud ni fase. Para $\tau<\tau_c$ las
fluctuaciones están "fuertemente" correlacionadas; para $\tau>\tau_c$, "débilmente". En general
$\tau_c$ es el ancho de $|g(\tau)|$; la definición usual es el **ancho equivalente en potencia**
(ver §A.2 y (A.2-8); nótese $g(0)=1$):
$$\textbf{[recuadro]}\quad \tau_c=\int_{-\infty}^{\infty}|g(\tau)|^2\,d\tau \qquad (11.1\text{-}10)$$
El tiempo de coherencia de la luz monocromática es infinito.

> **Ejercicio 11.1-1 — Coherence Time** (p. 409). Verificar que las siguientes expresiones son
> consistentes con la definición (11.1-10) de $\tau_c$:
> $$g(\tau)=\begin{cases}\exp\!\left(-\dfrac{|\tau|}{\tau_c}\right) & \text{(exponencial)}\\[2ex]
> \exp\!\left(-\dfrac{\pi\tau^2}{2\tau_c^2}\right) & \text{(gaussiana)}\end{cases} \qquad (11.1\text{-}11)$$
> ¿En qué factor cae $|g(\tau)|$ al pasar $\tau$ de 0 a $\tau_c$ en cada caso? *(Resultado: en el
> caso exponencial $\int e^{-2|\tau|/\tau_c}d\tau=\tau_c$ y $|g(\tau_c)|=e^{-1}\approx0.37$; en el
> gaussiano $\int e^{-\pi\tau^2/\tau_c^2}d\tau=\tau_c$ y $|g(\tau_c)|=e^{-\pi/2}\approx0.21$.)*

Luz cuyo $\tau_c$ es mucho mayor que las diferencias de retardo del sistema es efectivamente
coherente; equivalentemente, si $c\tau_c$ es mucho mayor que todas las diferencias de camino óptico.
$$\textbf{[recuadro]}\quad l_c=c\,\tau_c \qquad (11.1\text{-}12)\ \text{Longitud de coherencia}$$

**Densidad espectral de potencia** (p. 409–410). Transformada de Fourier de $U(t)$:
$$V(\nu)=\int_{-\infty}^{\infty}U(t)\exp(-j2\pi\nu t)\,dt \qquad (11.1\text{-}13)$$
$\langle|V(\nu)|^2\rangle\,d\nu$ es la energía promedio por unidad de área con frecuencias en
$[\nu,\nu+d\nu]$ (densidad espectral de energía); $V(\nu)=0$ para $\nu<0$ por la definición de $U$
(§2.6A). Como una función estacionaria es eterna y tiene energía infinita se usa la *potencia*
espectral: con la transformada truncada
$$V_T(\nu)=\int_{-T/2}^{T/2}U(t)\exp(-j2\pi\nu t)\,dt \qquad (11.1\text{-}14)$$
$$S(\nu)=\lim_{T\to\infty}\frac{1}{T}\langle|V_T(\nu)|^2\rangle \qquad (11.1\text{-}15)$$
es la **densidad espectral de potencia** (no nula solo para $\nu>0$). Como $|U|^2$ es intensidad
(W/cm²), $S(\nu)\,d\nu$ es la potencia promedio por unidad de área en $[\nu,\nu+d\nu]$: $S(\nu)$ es
la densidad espectral de intensidad (W/cm²·Hz), llamada "densidad espectral" o "espectro".
$$I=\int_0^{\infty}S(\nu)\,d\nu \qquad (11.1\text{-}16)$$
**Teorema de Wiener–Khinchin** (p. 410; demostración en Prob. 11.1-5): $G(\tau)$ y $S(\nu)$ son
par de Fourier,
$$\textbf{[recuadro]}\quad S(\nu)=\int_{-\infty}^{\infty}G(\tau)\exp(-j2\pi\nu\tau)\,d\tau \qquad (11.1\text{-}17)$$
**Fig. 11.1-4** (p. 410): el espectro varía con la posición en una imagen en color (cuadro
*Dahlias* de Matisse): perfiles espectrales para rojo (pico ~650 nm), verde (~550 nm) y azul
(~470 nm).

**Ancho espectral** (p. 411). El espectro suele estar confinado a una banda estrecha alrededor de
$\nu_0$; el **ancho espectral** o **ancho de línea** $\Delta\nu$ es el ancho de $S(\nu)$. Por la
relación de Fourier, los anchos de $S(\nu)$ y $G(\tau)$ son inversos: espectro ancho ↔ $\tau_c$
corto; línea estrecha ↔ $\tau_c$ largo (**Fig. 11.1-5**, p. 411). Límite monocromático:
$G(\tau)=I\exp(j\omega_0\tau)$, $S(\nu)=I\,\delta(\nu-\nu_0)$, $\tau_c=\infty$, $\Delta\nu=0$. El
tiempo de coherencia puede aumentarse con un filtro óptico que reduzca el ancho espectral, al costo
de perder energía.

Definición más común: FWHM de $S(\nu)$. La relación $\Delta\nu_{\rm FWHM}$–$\tau_c$ depende del
perfil (**Tabla 11.1-1**, p. 411; ver también §A.2):

| Densidad espectral | Rectangular | Lorentziana | Gaussiana |
|---|---|---|---|
| $\Delta\nu_{\rm FWHM}$ | $\dfrac{1}{\tau_c}$ | $\dfrac{1}{\pi\tau_c}\approx\dfrac{0.32}{\tau_c}$ | $\dfrac{\sqrt{2\ln2/\pi}}{\tau_c}\approx\dfrac{0.66}{\tau_c}$ |

Otra definición conveniente (p. 411):
$$\Delta\nu_c=\frac{\left(\int_0^{\infty}S(\nu)\,d\nu\right)^2}{\int_0^{\infty}S^2(\nu)\,d\nu} \qquad (11.1\text{-}18)$$
con la cual, independientemente del perfil (Ejercicio 11.1-2):
$$\textbf{[recuadro]}\quad \Delta\nu_c=\frac{1}{\tau_c} \qquad (11.1\text{-}19)\ \text{Ancho espectral}$$
Si $S(\nu)$ es rectangular entre $\nu_0-B/2$ y $\nu_0+B/2$, (11.1-18) da $\Delta\nu_c=B$. Las dos
definiciones $\Delta\nu_c$ y $\Delta\nu_{\rm FWHM}\equiv\Delta\nu$ difieren en un factor entre
$1/\pi\approx0.32$ y 1 para los perfiles de la tabla (p. 412).

> **Ejercicio 11.1-2 — Relation Between Spectral Width and Coherence Time** (p. 412). Demostrar
> que $\tau_c$ de (11.1-10) y $\Delta\nu_c$ de (11.1-18) cumplen $\tau_c=1/\Delta\nu_c$. Pista:
> usar las definiciones, la relación de Fourier entre $S(\nu)$ y $G(\tau)$ y el teorema de Parseval
> [(A.1-7)].

**Tabla 11.1-2** (p. 412) — Anchos espectrales, tiempos y longitudes de coherencia en el vacío:

| Fuente | $\Delta\nu_c$ (Hz) | $\tau_c=1/\Delta\nu_c$ | $l_c=c\tau_c$ |
|---|---|---|---|
| Luz solar filtrada ($\lambda_o=0.4$–$0.8\ \mu$m) | $3.74\times10^{14}$ | 2.67 fs | 800 nm |
| LED ($\lambda_o=1\ \mu$m, $\Delta\lambda_o=50$ nm) | $1.5\times10^{13}$ | 67 fs | 20 μm |
| Lámpara de sodio de baja presión | $5\times10^{11}$ | 2 ps | 600 μm |
| Láser He–Ne multimodo ($\lambda_o=633$ nm) | $1.5\times10^{9}$ | 0.67 ns | 20 cm |
| Láser He–Ne monomodo ($\lambda_o=633$ nm) | $1\times10^{6}$ | 1 μs | 300 m |

> **Ejemplo 11.1-1 — A Wave Comprising a Random Sequence of Wavepackets** (p. 412–413). La luz
> de una fuente incoherente se modela como paquetes de onda emitidos en instantes aleatorios, cada
> uno con fase aleatoria (emitido por un átomo distinto; **Fig. 11.1-6**). Paquete sinusoidal con
> envolvente exponencial emitido en $t=0$:
> $$U_p(t)=\begin{cases}A_p\exp\!\left(-\dfrac{t}{\tau_c}\right)\exp(j\omega_0 t), & t\ge0\\ 0, & t<0\end{cases} \qquad (11.1\text{-}20)$$
> Tiempos de emisión totalmente aleatorios; las fases aleatorias e independientes van en $A_p$.
> Resultado: $g(\tau)=\exp(-|\tau|/\tau_c)\exp(j\omega_0\tau)$ (módulo = exponencial bilateral) y
> espectro **lorentziano** $S(\nu)=(\Delta\nu/2\pi)/[(\nu-\nu_0)^2+(\Delta\nu/2)^2]$ con
> $\Delta\nu=1/\pi\tau_c$ (Tabla A.2-1). El tiempo de coherencia es exactamente la duración de un
> paquete: la luz está correlacionada dentro de la duración de un paquete individual.

#### 11.1C Spatial Coherence (p. 413)

**Función de coherencia mutua** (p. 413). Correlación cruzada de $U(\mathbf r_1,t)$ y
$U(\mathbf r_2,t)$:
$$\textbf{[recuadro]}\quad G(\mathbf r_1,\mathbf r_2,\tau)=\langle U^*(\mathbf r_1,t)\,U(\mathbf r_2,t+\tau)\rangle \qquad (11.1\text{-}21)$$
Forma normalizada, **grado complejo de coherencia**:
$$\textbf{[recuadro]}\quad g(\mathbf r_1,\mathbf r_2,\tau)=\frac{G(\mathbf r_1,\mathbf r_2,\tau)}{\sqrt{I(\mathbf r_1)I(\mathbf r_2)}} \qquad (11.1\text{-}22)$$
Con $\mathbf r_1=\mathbf r_2=\mathbf r$ se recuperan (11.1-4) y (11.1-7); con $\tau=0$,
$I(\mathbf r)=G(\mathbf r,\mathbf r,0)$. Es el coeficiente de correlación cruzada de
$U^*(\mathbf r_1,t)$ y $U(\mathbf r_2,t+\tau)$:
$$0\le|g(\mathbf r_1,\mathbf r_2,\tau)|\le1 \qquad (11.1\text{-}23)$$
$|g|=0$: fasores independientes con fases uniformes (descorrelación); $|g|=1$: correlación total.
Nótese que $|g(\mathbf r_1,\mathbf r_2,0)|$ no es necesariamente 1, pero $|g(\mathbf r,\mathbf
r,0)|=1$ por definición (p. 414). **Fig. 11.1-7** (p. 414): $|g(\mathbf r_1,\mathbf r_2,\tau)|$ vs.
$|\mathbf r_1-\mathbf r_2|$ y $\tau$; en (a) el máximo para cada separación ocurre en $\tau=0$; en
(b) ocurre en $|\mathbf r_1-\mathbf r_2|=c\tau$ (onda plana aleatoria propagándose en $z$: puntos
$z_1,z_2$ totalmente correlacionados al retardo $\tau_0=|z_2-z_1|/c$).

> **Ejercicio 11.1-3 — Differential Equations Governing the Mutual Coherence Function** (p. 414).
> En el vacío $U$ cumple $\nabla^2U-(1/c^2)\partial^2U/\partial t^2=0$. Usando (11.1-21), mostrar
> que $G(\mathbf r_1,\mathbf r_2,\tau)$ satisface
> $$\nabla_1^2G-\frac{1}{c^2}\frac{\partial^2G}{\partial\tau^2}=0 \quad(11.1\text{-}24a), \qquad \nabla_2^2G-\frac{1}{c^2}\frac{\partial^2G}{\partial\tau^2}=0 \quad(11.1\text{-}24b)$$
> con $\nabla_1^2$, $\nabla_2^2$ los laplacianos respecto a $\mathbf r_1$ y $\mathbf r_2$.

**Intensidad mutua** (p. 414–415). Función de coherencia mutua en $\tau=0$:
$$G(\mathbf r_1,\mathbf r_2,0)=\langle U^*(\mathbf r_1,t)U(\mathbf r_2,t)\rangle \qquad (11.1\text{-}25)$$
denotada $G(\mathbf r_1,\mathbf r_2)$; su diagonal da $I(\mathbf r)=G(\mathbf r,\mathbf r)$. Cuando
las diferencias de camino óptico del sistema son mucho menores que $l_c=c\tau_c$, la luz tiene
coherencia temporal efectivamente completa y
$$G(\mathbf r_1,\mathbf r_2,\tau)=G(\mathbf r_1,\mathbf r_2)\exp(j\omega_0\tau) \qquad (11.1\text{-}26)$$
luz **cuasi-monocromática**: la intensidad mutua describe completamente la coherencia espacial.
$$\textbf{[recuadro]}\quad g(\mathbf r_1,\mathbf r_2)=\frac{G(\mathbf r_1,\mathbf r_2)}{\sqrt{I(\mathbf r_1)I(\mathbf r_2)}} \qquad (11.1\text{-}27)\ \text{Intensidad mutua normalizada}$$
$|g(\mathbf r_1,\mathbf r_2)|\in[0,1]$ mide el grado de coherencia espacial ($\tau=0$); si $U$ es
determinista, $|g|=1$ en todas partes.

**Área de coherencia** (p. 415). $|g(\mathbf r_1,\mathbf r_2)|$ vale 1 en $\mathbf r_1=\mathbf r_2$
y decae con $|\mathbf r_1-\mathbf r_2|$ (no necesariamente de forma monótona). El área barrida por
$\mathbf r_1$ dentro de la cual $|g|$ supera un valor prescrito ($\tfrac12$ o $1/e$) es el **área
de coherencia** $A_c$ (**Fig. 11.1-8**, p. 416: dos ejemplos; en (a) $A_c$ menor que en (b)). Luz
coherente ideal: $A_c=\infty$. Criterio práctico: si $A_c$ es mayor que la apertura del sistema
($|g|\approx1$ en todos los puntos de interés) la luz se considera coherente; si $A_c$ es menor que
la resolución del sistema, $g(\mathbf r_1,\mathbf r_2)=0$ para casi todo $\mathbf r_1\neq\mathbf
r_2$ y la luz es **incoherente**. Una superficie caliente extensa radia con $A_c\sim\lambda^2$, de
modo que en la práctica es incoherente. Coherencia e incoherencia completas son idealizaciones,
límites de la coherencia parcial.

**Densidad espectral cruzada** (p. 416–417). Alternativa en el dominio de la frecuencia:
transformada de Fourier de $G(\mathbf r_1,\mathbf r_2,\tau)$ respecto a $\tau$,
$$\textbf{[recuadro]}\quad S(\mathbf r_1,\mathbf r_2,\nu)=\int_{-\infty}^{\infty}G(\mathbf r_1,\mathbf r_2,\tau)\exp(-j2\pi\nu\tau)\,d\tau \qquad (11.1\text{-}28)$$
(**cross-spectral density** o espectro de potencia cruzado). Con $\mathbf r_1=\mathbf r_2$ se
reduce a $S(\nu)$ de (11.1-17). Versión normalizada:
$$s(\mathbf r_1,\mathbf r_2,\nu)=\frac{S(\mathbf r_1,\mathbf r_2,\nu)}{\sqrt{S(\mathbf r_1,\mathbf r_1,\nu)\,S(\mathbf r_2,\mathbf r_2,\nu)}} \qquad (11.1\text{-}29)$$
con módulo en $[0,1]$: grado de coherencia espacial a la frecuencia $\nu$.
**Luz cross-spectrally pure** (espectralmente pura): cuando $S(\mathbf r_1,\mathbf r_2,\nu)=G(\mathbf
r_1,\mathbf r_2)\,s(\nu)$ (posición y frecuencia separables); entonces $G(\mathbf r_1,\mathbf
r_2,\tau)=G(\mathbf r_1,\mathbf r_2)\,g(\tau)$ con $g(\tau)$ la transformada inversa de $s(\nu)$; si
se normaliza $\int s(\nu)d\nu=1$, $G(\mathbf r_1,\mathbf r_2)$ es la intensidad mutua. Propiedades:
1. En una posición, $S(\mathbf r,\mathbf r,\nu)=I(\mathbf r)s(\nu)$: mismo perfil espectral en todas
   partes (una imagen tendría el mismo color con brillo variable).
2. $$s(\mathbf r_1,\mathbf r_2,\nu)=G(\mathbf r_1,\mathbf r_2)/\sqrt{G(\mathbf r_1,\mathbf r_1)G(\mathbf r_2,\mathbf r_2)}=g(\mathbf r_1,\mathbf r_2) \qquad (11.1\text{-}30)$$
   independiente de la frecuencia: la intensidad mutua normalizada describe la coherencia espacial a
   todas las frecuencias (p. 417).

#### 11.1D Longitudinal Coherence (p. 417)

Ejemplos de ondas aleatorias con frentes de onda fijos (planos y esféricos).

**Onda plana parcialmente coherente** (p. 417–418):
$$U(\mathbf r,t)=\mathfrak a\!\left(t-\frac{z}{c}\right)\exp\!\left[j\omega_0\!\left(t-\frac{z}{c}\right)\right] \qquad (11.1\text{-}31)$$
(propagación en $z$ en medio homogéneo con velocidad $c$; satisface la ecuación de onda para
cualquier $\mathfrak a(t)$, §2.6A; si $\mathfrak a(t)$ es aleatoria la luz es parcialmente
coherente). Función de coherencia mutua:
$$G(\mathbf r_1,\mathbf r_2,\tau)=G_a\!\left(\tau-\frac{z_2-z_1}{c}\right)\exp\!\left[j\omega_0\!\left(\tau-\frac{z_2-z_1}{c}\right)\right] \qquad (11.1\text{-}32)$$
con $G_a(\tau)=\langle\mathfrak a^*(t)\mathfrak a(t+\tau)\rangle$ (independiente de $t$).
Consecuencias: $I(\mathbf r)=G_a(0)$ constante en el espacio; coherencia temporal
$G(\mathbf r,\mathbf r,\tau)=G_a(\tau)e^{j\omega_0\tau}$ independiente de la posición;
$g(\mathbf r,\mathbf r,\tau)=g_a(\tau)e^{j\omega_0\tau}$ con $g_a=G_a(\tau)/G_a(0)$; $\tau_c$ = ancho
de $|g_a(\tau)|$, igual en todas partes; $S(\nu)$ = transformada de $G_a(\tau)$ desplazada en
$\nu_0$, igual en todo el espacio. Coherencia espacial:
$$G(\mathbf r_1,\mathbf r_2,0)=G_a\!\left(\frac{z_1-z_2}{c}\right)\exp\!\left[j\omega_0\frac{z_1-z_2}{c}\right] \qquad (11.1\text{-}33)$$
$$g(\mathbf r_1,\mathbf r_2,0)=g_a\!\left(\frac{z_1-z_2}{c}\right)\exp\!\left[j\omega_0\frac{z_1-z_2}{c}\right] \qquad (11.1\text{-}34)$$
Si $z_1=z_2$ (mismo plano transversal), $|g|=|g_a(0)|=1$: puntos de un mismo frente de onda están
totalmente correlacionados, área de coherencia transversal infinita (**Fig. 11.1-9**, p. 418).
Puntos con separación axial $|z_2-z_1|/c>\tau_c$, es decir $|z_2-z_1|>l_c$, están aproximadamente
descorrelacionados. **Resumen** (p. 418): la onda plana parcialmente coherente es espacialmente
coherente en cada plano transversal pero parcialmente coherente en la dirección axial; la
coherencia longitudinal corresponde uno a uno con la temporal. El cociente $l_c/l_{\max}$ (longitud
de coherencia / máxima diferencia de camino óptico del sistema) gobierna el papel de la coherencia:
si $l_c\gg l_{\max}$ la onda es efectivamente coherente.

**Onda esférica parcialmente coherente** (p. 418–419) (ver §2.2B y §2.6A):
$$U(\mathbf r,t)=\frac{1}{r}\,\mathfrak a\!\left(t-\frac{r}{c}\right)\exp\!\left[j\omega_0\!\left(t-\frac{r}{c}\right)\right] \qquad (11.1\text{-}35)$$
$$G(\mathbf r_1,\mathbf r_2,\tau)=\frac{1}{r_1r_2}G_a\!\left(\tau-\frac{r_2-r_1}{c}\right)\exp\!\left[j\omega_0\!\left(\tau-\frac{r_2-r_1}{c}\right)\right] \qquad (11.1\text{-}36)$$
con $G_a(\tau)=\langle\mathfrak a^*(t)\mathfrak a(t+\tau)\rangle$. $I(\mathbf r)=G_a(0)/r^2$ (ley del
inverso del cuadrado); $\tau_c$ y $S(\nu)$ iguales en todo el espacio; para $\tau=0$ todos los
puntos de un frente de onda esférico están totalmente correlacionados, y puntos en frentes
separados radialmente por $|r_2-r_1|\gg l_c$ están descorrelacionados (**Fig. 11.1-10**, p. 419).
**Resultado destacado**: una onda parcialmente coherente arbitraria transmitida por un *pinhole*
genera una onda esférica parcialmente coherente: *el pinhole imparte coherencia espacial pero no
temporal* (actúa como filtro espacial). Si además se coloca un filtro óptico de banda muy estrecha
en el pinhole, la onda queda aproximadamente monocromática: coherencia temporal (por el filtro
espectral) y espacial (por el pinhole) completas; el precio es la pérdida de energía por ambos
filtrados (p. 418–419).

---

### 11.2 Interference of Partially Coherent Light (p. 419)

La interferencia de luz coherente se trató en §2.5; aquí se trata la de luz parcialmente coherente.

#### 11.2A Interference of Two Partially Coherent Waves (p. 419)

Dos ondas $U_1$, $U_2$ con intensidades $I_1=\langle|U_1|^2\rangle$, $I_2=\langle|U_2|^2\rangle$ y
correlación cruzada $G_{12}=\langle U_1^*U_2\rangle$, normalizada
$$g_{12}=\frac{\langle U_1^*U_2\rangle}{\sqrt{I_1I_2}} \qquad (11.2\text{-}1)$$
Intensidad de la superposición:
$$I=\langle|U_1+U_2|^2\rangle=I_1+I_2+G_{12}+G_{12}^*=I_1+I_2+2\,\mathrm{Re}\{G_{12}\}=I_1+I_2+2\sqrt{I_1I_2}\,\mathrm{Re}\{g_{12}\} \qquad (11.2\text{-}2)$$
$$\textbf{[recuadro]}\quad I=I_1+I_2+2\sqrt{I_1I_2}\,|g_{12}|\cos\varphi \qquad (11.2\text{-}3)\ \text{Ecuación de interferencia}$$
con $\varphi=\arg\{g_{12}\}$. Límites: (1) ondas totalmente correlacionadas, $g_{12}=e^{j\varphi}$,
$|g_{12}|=1$ → fórmula coherente (2.5-4); (2) descorrelacionadas, $g_{12}=0$ → $I=I_1+I_2$, sin
interferencia (p. 419–420).

**Visibilidad** (p. 420) (profundidad de modulación, contraste):
$$\mathcal V=\frac{I_{\max}-I_{\min}}{I_{\max}+I_{\min}} \qquad (11.2\text{-}4)$$
$$\mathcal V=\frac{2\sqrt{I_1I_2}}{I_1+I_2}|g_{12}| \qquad (11.2\text{-}5)$$
$$\textbf{[recuadro]}\quad \mathcal V=|g_{12}| \quad (I_1=I_2) \qquad (11.2\text{-}6)\ \text{Visibilidad}$$
**Fig. 11.2-1** (p. 420): $I/2I_0$ sinusoidal en $\varphi$ con visibilidad $|g_{12}|$.

#### 11.2B Interference and Temporal Coherence (p. 420)

Onda $U(t)$ con intensidad $I_0$ y $g(\tau)=\langle U^*(t)U(t+\tau)\rangle/I_0$ sumada a una
réplica retardada $U(t+\tau)$. Con $U_1=U(t)$, $U_2=U(t+\tau)$, $I_1=I_2=I_0$, $g_{12}=g(\tau)$:
$$I=2I_0[1+\mathrm{Re}\{g(\tau)\}]=2I_0[1+|g(\tau)|\cos\varphi(\tau)] \qquad (11.2\text{-}7)$$
con $\varphi(\tau)=\arg\{g(\tau)\}$. *La capacidad de una onda para interferir con una réplica
retardada de sí misma está gobernada por su grado complejo de coherencia temporal a ese retardo.*
Se implementa con divisores de haz (Mach–Zehnder o Michelson, Fig. 2.5-3) (p. 421).
Para la onda plana de §11.1D, $g(\tau)=g_a(\tau)e^{j\omega_0\tau}$, $\Delta\nu_c=1/\tau_c$:
$$I=2I_0\{1+|g_a(\tau)|\cos[\omega_0\tau+\varphi_a(\tau)]\} \qquad (11.2\text{-}8)$$
$\varphi_a=\arg\{g_a\}$. La relación $I$–$\tau$ es el **interferograma** (**Fig. 11.2-2**, p. 421:
Michelson con brazos $d_1$, $d_2$; $\tau=2(d_2-d_1)/c$; $I/2I_0$ vs. $\tau$ con envolvente
$2|g_{12}|$). Con $\Delta\nu_c\ll\nu_0$, $|g_a|$ y $\varphi_a$ varían lentamente frente al periodo
$1/\nu_0$; la visibilidad local es $\mathcal V=|g(\tau)|=|g_a(\tau)|$, máxima (1) cerca de $\tau=0$
y nula para $\tau\gg\tau_c$ (diferencia de camino ≫ $l_c$). **Solo hay interferencia si la
diferencia de camino óptico es menor que la longitud de coherencia.** Midiendo la visibilidad vs.
retardo se obtiene $|g(\tau)|$; la posición de los picos da la fase de $g(\tau)$.

**Espectroscopía por transformada de Fourier** (p. 421–422). Con
$$G(\tau)=I_0g(\tau)=\int_0^{\infty}S(\nu)\exp(j2\pi\nu\tau)\,d\nu \qquad (11.2\text{-}9)$$
y $\int_0^\infty S(\nu)d\nu=I_0$, $S$ real:
$$I=2\int_0^{\infty}S(\nu)[1+\cos(2\pi\nu\tau)]\,d\nu \qquad (11.2\text{-}10)$$
superposición ponderada de interferogramas de cada componente monocromática (cada una con periodo
$1/\nu$ y visibilidad unidad; el compuesto pierde visibilidad por los periodos distintos). Midiendo
$I(\tau)$ e invirtiendo por Fourier se obtiene $S(\nu)$: **Fourier-transform spectroscopy**.

**Tomografía de coherencia óptica (OCT)** (p. 422–423). Técnica interferométrica para perfilar un
medio multicapa (reflectancia y profundidad de cada frontera) con fuente de corta longitud de
coherencia y un Michelson (**Fig. 11.2-3**: espejo móvil $d$, muestra con capas 1,2,3…, detector;
interferograma con grupos de franjas en $\tau_1,\tau_2,\dots$ de alturas $r_1,r_2,r_3$). Onda del
espejo móvil $U(t-\tau)$ con $\tau=d/c_o$; ondas reflejadas $\mathfrak r_iU(t-\tau_i)$ con
$\mathfrak r_i$ reflectancia de amplitud de la $i$-ésima frontera. Para divisor simétrico,
$I(\tau)=\langle|U(t-\tau)+\sum_i\mathfrak r_iU(t-\tau_i)|^2\rangle$:
$$I/2I_0=1+\sum_i\mathfrak r_i\,\mathrm{Re}\{g(\tau-\tau_i)\}+\sum_{ij}\mathfrak r_i\mathfrak r_j^*\,\mathrm{Re}\{g(\tau_j-\tau_i)\} \qquad (11.2\text{-}11)$$
El segundo término (interferencia referencia–muestra) es el importante; el tercero (reflexiones
múltiples) no depende de $\tau$ y se trata como fondo. Con $g(\tau)=g_a(\tau)e^{j\omega_0\tau}$:
$$I/2I_0\approx1+\sum_i\mathfrak r_i|g_a(\tau-\tau_i)|\cos[\omega_0(\tau-\tau_i)+\varphi_a(\tau-\tau_i)] \qquad (11.2\text{-}12)$$
Con fuente de corta $l_c$, $g_a$ es angosta y cada frontera genera un grupo de franjas de duración
$\tau_c$ centrado en su retardo → se obtienen reflectancias y espesores de capa. OCT es una técnica
de imagen efectiva en medicina clínica e ingeniería (p. 423).

#### 11.2C Interference and Spatial Coherence (p. 423)

Experimento de Young con dos pinholes en $\mathbf r_1=(-a,0,0)$, $\mathbf r_2=(a,0,0)$ iluminados por
$U(\mathbf r,t)$ parcialmente coherente (intensidades iguales en los pinholes); observación en
$\mathbf r=(x,0,d)$ con $d$ grande (aproximación paraboloidal); ángulo subtendido por los pinholes
$\theta\approx2a/d$ (**Fig. 11.2-4**, p. 423: franjas de periodo $\lambda/\theta$ y visibilidad
$|g(\mathbf r_1,\mathbf r_2)|$). En la aproximación de Fresnel [(2.2-17)]:
$$U_1(\mathbf r,t)\propto U\!\left(\mathbf r_1,t-\frac{|\mathbf r-\mathbf r_1|}{c}\right)\approx U\!\left(\mathbf r_1,t-\frac{d+(x+a)^2/2d}{c}\right) \qquad (11.2\text{-}13a)$$
$$U_2(\mathbf r,t)\propto U\!\left(\mathbf r_2,t-\frac{|\mathbf r-\mathbf r_2|}{c}\right)\approx U\!\left(\mathbf r_2,t-\frac{d+(x-a)^2/2d}{c}\right) \qquad (11.2\text{-}13b)$$
con $I_1=I_2=I_0$ y
$$g_{12}=\frac{\langle U_1^*(\mathbf r,t)U_2(\mathbf r,t)\rangle}{I_0}=g(\mathbf r_1,\mathbf r_2,\tau_x) \qquad (11.2\text{-}14)$$
$$\tau_x=\frac{|\mathbf r-\mathbf r_1|-|\mathbf r-\mathbf r_2|}{c}=\frac{(x+a)^2-(x-a)^2}{2dc}=\frac{2ax}{dc}=\frac{\theta}{c}x \qquad (11.2\text{-}15)$$
$$\textbf{[recuadro]}\quad I(x)=2I_0\left[1+|g(\mathbf r_1,\mathbf r_2,\tau_x)|\cos\varphi_x\right] \qquad (11.2\text{-}16)$$
$\varphi_x=\arg\{g(\mathbf r_1,\mathbf r_2,\tau_x)\}$, $\tau_x=\theta x/c$ (p. 424).

**Luz cuasi-monocromática** (p. 424): con $g(\mathbf r_1,\mathbf r_2,\tau)\approx g(\mathbf
r_1,\mathbf r_2)e^{j\omega_0\tau}$,
$$\textbf{[recuadro]}\quad I(x)=2I_0\left[1+\mathcal V\cos\!\left(\frac{2\pi\theta}{\lambda}x+\varphi\right)\right] \qquad (11.2\text{-}17)$$
$\lambda=c/\nu_0$, $\mathcal V=|g(\mathbf r_1,\mathbf r_2)|$, $\varphi=\arg\{g(\mathbf r_1,\mathbf
r_2)\}$: franjas sinusoidales de periodo $\lambda/\theta$; *la visibilidad es el módulo del grado
complejo de coherencia espacial en los dos pinholes*; los picos dependen de $\varphi$.

**Interferencia con luz de una fuente extensa** (p. 424–425). Onda plana coherente en $z$:
$U=\exp(-jkz)e^{j\omega_0t}$ → $g(\mathbf r_1,\mathbf r_2)=1$, $\mathcal V=1$, pico en $x=0$. Onda
plana inclinada un ángulo pequeño $\theta_x$ en el plano $x$–$z$: $U\approx\exp[-j(kz+k\theta_x
x)]e^{j\omega_0t}$ → $g(\mathbf r_1,\mathbf r_2)=\exp(-jk\theta_x2a)$: $\mathcal V=1$ pero
$\varphi=-k\theta_x2a=-2\pi\theta_x2a/\lambda$, el patrón se desplaza una fracción
$2a\theta_x/\lambda$ de periodo ($\varphi=2\pi$ ↔ un periodo). Fuente que subtiende $\theta_s$
(colección de ondas planas independientes): $\varphi\in\pm2\pi(\theta_s/2)2a/\lambda=\pm2\pi
\theta_sa/\lambda$, superposición de sinusoides desplazadas; si $\theta_s=\lambda/2a$,
$\varphi\in\pm\pi$ y las franjas se borran (visibilidad 0). **Fig. 11.2-5** (p. 425): las franjas
de Young se borran si $\theta_s>\lambda/2a$; si $2a<\lambda/\theta_s$ son visibles. Conclusión:
$$\textbf{[recuadro]}\quad \rho_c\approx\frac{\lambda}{\theta_s} \qquad (11.2\text{-}18)\ \text{Distancia de coherencia}$$
$$\textbf{[recuadro]}\quad A_c\approx\left(\frac{\lambda}{\theta_s}\right)^2 \qquad (11.2\text{-}19)$$
área de coherencia de luz emitida por una fuente que subtiende $\theta_s$. Ejemplo: el Sol subtiende
$0.5°$ → $\rho_c\approx\lambda/\theta_s\approx115\lambda$; a $\lambda=0.5\ \mu$m,
$\rho_c\approx57.5\ \mu$m. Análisis riguroso (§11.3C) para fuente circular incoherente uniforme:
$$\rho_c=1.22\frac{\lambda}{\theta_s} \qquad (11.2\text{-}20)$$

**Efecto del ancho espectral sobre la interferencia** (p. 426). Espectro angosto de ancho
$\Delta\nu_c\ll\nu_0$ centrado en $\nu_0$:
$$g(\mathbf r_1,\mathbf r_2,\tau)=g_a(\mathbf r_1,\mathbf r_2,\tau)\exp(j\omega_0\tau) \qquad (11.2\text{-}21)$$
con $g_a$ lentamente variable en $\tau$. Sustituyendo en (11.2-16):
$$\textbf{[recuadro]}\quad I(x)=2I_0\left[1+\mathcal V_x\cos\!\left(\frac{2\pi\theta}{\bar\lambda}x+\varphi_x\right)\right] \qquad (11.2\text{-}22)$$
$\mathcal V_x=|g_a(\mathbf r_1,\mathbf r_2,\tau_x)|$, $\varphi_x=\arg\{g_a(\mathbf r_1,\mathbf
r_2,\tau_x)\}$, $\tau_x=\theta x/c$, $\bar\lambda=c/\nu_0$. Franjas de periodo $\bar\lambda/\theta$
con visibilidad y fase variables. Si $|g_a|=1$ en $\tau=0$ y se anula para $\tau\gg\tau_c$, la
visibilidad es 1 en $x=0$ y se anula para $x\gg x_c=c\tau_c/\theta$:
$$x_c=\frac{l_c}{\theta} \qquad (11.2\text{-}23)$$
(**Fig. 11.2-6**, p. 426). **Número de franjas observables**:
$x_c/(\bar\lambda/\theta)=l_c/\bar\lambda=c\tau_c/\bar\lambda=\nu_0/\Delta\nu_c$ (cociente
longitud de coherencia / longitud de onda central, o frecuencia central / ancho de línea). Si
además $|g(\mathbf r_1,\mathbf r_2,0)|<1$ (fuente no espacialmente coherente), la visibilidad baja
más y se observan aún menos franjas.

---

### *11.3 Transmission of Partially Coherent Light Through Optical Systems (p. 427) — sección avanzada

Se extiende lo de los caps. 2 y 4 (transmisión de luz coherente por componentes delgados,
aperturas y espacio libre) a luz cuasi-monocromática parcialmente coherente: $l_c=c\tau_c=c/\Delta
\nu_c$ mucho mayor que las diferencias de camino del sistema, de modo que $G(\mathbf r_1,\mathbf
r_2,\tau)\approx G(\mathbf r_1,\mathbf r_2)\exp(j\omega_0\tau)$. Las leyes de transmisión de la
función determinista $U(\mathbf r)$ se aplican también a la función aleatoria; el interés está en
las leyes para los promedios $I(\mathbf r)$ y $G(\mathbf r_1,\mathbf r_2)$ (p. 427).

#### 11.3A Propagation of Partially Coherent Light (p. 427)

**Componentes ópticos delgados** (p. 427): $U_2(\mathbf r)=\mathfrak t(\mathbf r)U_1(\mathbf r)$ con
$\mathfrak t(x,y)$ la transmitancia de amplitud:
$$G_2(\mathbf r_1,\mathbf r_2)=\mathfrak t^*(\mathbf r_1)\,\mathfrak t(\mathbf r_2)\,G_1(\mathbf r_1,\mathbf r_2) \qquad (11.3\text{-}1)$$
$$I_2(\mathbf r)=|\mathfrak t(\mathbf r)|^2I_1(\mathbf r) \qquad (11.3\text{-}2)$$
$$|g_2(\mathbf r_1,\mathbf r_2)|=|g_1(\mathbf r_1,\mathbf r_2)| \qquad (11.3\text{-}3)$$
Un componente delgado puede cambiar la intensidad pero **no altera el módulo del grado de coherencia
espacial** (**Fig. 11.3-1**); si su transmitancia fuera aleatoria, sí alteraría la coherencia.

**Sistema óptico arbitrario** (p. 428) (espacio libre o componentes gruesos; cap. 4):
$$U_2(\mathbf r)=\int h(\mathbf r;\mathbf r')\,U_1(\mathbf r')\,d\mathbf r' \qquad (11.3\text{-}4)$$
con $h(\mathbf r;\mathbf r')$ la respuesta al impulso (integral doble sobre el plano de entrada
$\mathbf r'=(x',y')$; **Fig. 11.3-2**).
$$\textbf{[recuadro]}\quad G_2(\mathbf r_1,\mathbf r_2)=\iint h^*(\mathbf r_1;\mathbf r_1')\,h(\mathbf r_2;\mathbf r_2')\,G_1(\mathbf r_1',\mathbf r_2')\,d\mathbf r_1'\,d\mathbf r_2' \qquad (11.3\text{-}5)\ \text{Intensidad mutua}$$
$$\textbf{[recuadro]}\quad I_2(\mathbf r)=\iint h^*(\mathbf r;\mathbf r_1')\,h(\mathbf r;\mathbf r_2')\,G_1(\mathbf r_1',\mathbf r_2')\,d\mathbf r_1'\,d\mathbf r_2' \qquad (11.3\text{-}6)\ \text{Intensidad de imagen}$$
*Conocer la intensidad de entrada $I_1(\mathbf r)$ por sí sola no basta en general para determinar
la de salida $I_2(\mathbf r)$*: se necesita la intensidad mutua de entrada.

#### 11.3B Image Formation with Incoherent Light (p. 429)

Luz de entrada incoherente: $G_1$ se anula apenas $\mathbf r_2$ se separa de $\mathbf r_1$
(distancia de coherencia ≪ dimensiones del sistema, p. ej. la resolución). Se escribe
$G_1(\mathbf r_1,\mathbf r_2)=\sqrt{I_1(\mathbf r_1)I_1(\mathbf r_2)}\,g(\mathbf r_1-\mathbf r_2)$
con $g$ muy angosta; bajo la integral se sustituye $g(\mathbf r_1-\mathbf r_2)=\sigma\,\delta(\mathbf
r_1-\mathbf r_2)$, $\sigma=\int g(\mathbf r)d\mathbf r$ (área bajo $g$):
$$G_1(\mathbf r_1,\mathbf r_2)\approx\sigma\sqrt{I_1(\mathbf r_1)I_1(\mathbf r_2)}\,\delta(\mathbf r_1-\mathbf r_2) \qquad (11.3\text{-}7)$$
(no es exacta —$\delta(0)\to\infty$— pero vale para evaluar integrales como (11.3-6)). Resulta:
$$\textbf{[recuadro]}\quad I_2(\mathbf r)=\int I_1(\mathbf r')\,h_i(\mathbf r;\mathbf r')\,d\mathbf r' \qquad (11.3\text{-}8)\ \text{Ecuación de imagen (iluminación incoherente)}$$
$$\textbf{[recuadro]}\quad h_i(\mathbf r;\mathbf r')=\sigma|h(\mathbf r;\mathbf r')|^2 \qquad (11.3\text{-}9)\ \text{Respuesta al impulso (iluminación incoherente)}$$
$h_i$ se llama **función de dispersión de punto** (point-spread function). Con luz incoherente la
intensidad de salida es superposición ponderada de intensidades de entrada: no hay interferencia,
las intensidades simplemente se suman (**Fig. 11.3-3**: (a) coherente: amplitudes relacionadas por
$h$; (b) incoherente: intensidades relacionadas por $h_i=\sigma|h|^2$).

Si $h(\mathbf r;\mathbf r')=h(\mathbf r-\mathbf r')$ el sistema es **invariante al desplazamiento
(isoplanático)** [el libro dice "shift variant or isoplanatic", p. 430; debe leerse *shift
invariant*] (Apéndice B): $h_i(\mathbf r;\mathbf r')=h_i(\mathbf r-\mathbf r')$, las integrales son
convoluciones 2D y los sistemas se describen por funciones de transferencia $H(\nu_x,\nu_y)$ y
$H_i(\nu_x,\nu_y)$ (transformadas de Fourier de $h$ y $h_i$).

**Sistema de imagen de una lente** (§4.4C; **Fig. 11.3-4**, p. 430: plano objeto a $d_1$, lente
con apertura $p(x,y)$, plano imagen a $d_2$). Con iluminación coherente (Fresnel):
$$h(\mathbf r)\propto P\!\left(\frac{x}{\lambda d_2},\frac{y}{\lambda d_2}\right) \qquad (11.3\text{-}10)$$
$P(\nu_x,\nu_y)$ = transformada de Fourier de la función pupila $p(x,y)$ (1 dentro de la apertura,
0 fuera). Con iluminación cuasi-monocromática espacialmente incoherente:
$$h_i(\mathbf r)=\sigma|h(\mathbf r)|^2\propto\left|P\!\left(\frac{x}{\lambda d_2},\frac{y}{\lambda d_2}\right)\right|^2 \qquad (11.3\text{-}11)$$
con $\lambda$ la longitud de onda de $\nu_0$.

> **Ejemplo 11.3-1 — Imaging System with a Circular Aperture** (p. 430–432). Apertura circular de
> radio $a$: $p=1$ dentro del círculo. Transformada:
> $$P(\nu_x,\nu_y)=\frac{aJ_1(2\pi\nu_\rho a)}{\nu_\rho},\qquad \nu_\rho=\sqrt{\nu_x^2+\nu_y^2} \qquad (11.3\text{-}12)$$
> ($J_1$ función de Bessel, §A.3). Respuesta coherente [el libro dice "substituting into
> (11.1-36)", p. 431; se refiere a (11.3-10)]:
> $$h(x,y)\propto\left[\frac{J_1(2\pi\nu_s\rho)}{\pi\nu_s\rho}\right],\qquad \rho=\sqrt{x^2+y^2} \qquad (11.3\text{-}13)$$
> $$\nu_s=\frac{\theta}{2\lambda},\qquad \theta=\frac{2a}{d_2} \qquad (11.3\text{-}14)$$
> Respuesta incoherente:
> $$h_i(x,y)\propto\left[\frac{J_1(2\pi\nu_s\rho)}{\pi\nu_s\rho}\right]^2 \qquad (11.3\text{-}15)$$
> Ambas tienen su primer cero en $2\pi\nu_s\rho=3.832$, $\rho_s\approx3.832/2\pi\nu_s=3.832\lambda/\pi\theta$:
> $$\textbf{[recuadro]}\quad \rho_s\approx1.22\frac{\lambda}{\theta} \qquad (11.3\text{-}16)\ \text{Resolución de dos puntos}$$
> La imagen de un punto es una mancha $h_i$ de radio $\rho_s$; dos puntos separados $\rho_s$: la
> imagen de uno se anula en el centro de la del otro → $\rho_s$ mide la resolución. **Fig. 11.3-5**
> (p. 431): respuestas al impulso y funciones de transferencia para (a) coherente y (b)
> incoherente; se indica $1.22\lambda F_\#$ y $1/\lambda F_\#$. Funciones de transferencia (Apéndice
> B):
> $$H(\nu_x,\nu_y)=\begin{cases}1, & \nu_\rho<\nu_s\\ 0, & \text{en otro caso}\end{cases} \qquad (11.3\text{-}17)$$
> $$H_i(\nu_x,\nu_y)=\begin{cases}\dfrac{2}{\pi}\left[\cos^{-1}\dfrac{\nu_\rho}{2\nu_s}-\dfrac{\nu_\rho}{2\nu_s}\sqrt{1-\left(\dfrac{\nu_\rho}{2\nu_s}\right)^2}\right], & \nu_\rho<2\nu_s\\[2ex] 0, & \text{en otro caso}\end{cases} \qquad (11.3\text{-}18)$$
> normalizadas a 1 en $\nu_\rho=0$. Coherente: transferencia plana con corte $\nu_s=\theta/2\lambda$
> líneas/mm; incoherente: cae aproximadamente linealmente con corte $2\nu_s=\theta/\lambda$. Objeto
> en el infinito: $d_1=\infty$, $d_2=f$, $\theta=2a/f=1/F_\#$ con $F_\#=f/2a$:
> $$\textbf{[recuadro]}\quad \text{Frecuencia de corte (líneas/mm)}=\begin{cases}\dfrac{1}{2\lambda F_\#} & \text{(iluminación coherente)}\\[2ex] \dfrac{1}{\lambda F_\#} & \text{(iluminación incoherente)}\end{cases} \qquad (11.3\text{-}19)$$
> Advertencia (p. 432): no concluir que la iluminación incoherente es "superior" por tener el doble
> de ancho de banda espacial: una función de transferencia describe imagen de amplitud compleja, la
> otra de intensidad; no son comparables directamente.

#### 11.3C Gain of Spatial Coherence by Propagation (p. 432)

Con entrada incoherente, $G_1\to\sigma\sqrt{I_1(\mathbf r_1)I_1(\mathbf r_2)}\,\delta(\mathbf
r_1-\mathbf r_2)$ en (11.3-5):
$$\textbf{[recuadro]}\quad G_2(\mathbf r_1,\mathbf r_2)=\sigma\int h^*(\mathbf r_1;\mathbf r)\,h(\mathbf r_2;\mathbf r)\,I_1(\mathbf r)\,d\mathbf r \qquad (11.3\text{-}20)\ \text{Intensidad mutua}$$
La luz recibida ya no es incoherente: *la luz gana coherencia espacial por el mero hecho de
propagarse*. La radiación de cada punto se esparce y solapa con la de los vecinos; dos puntos de
salida reciben contribuciones comunes (**Fig. 11.3-6**, p. 433). Analogía: ruido blanco por un
filtro pasa-bajos aumenta su tiempo de coherencia; la propagación es un filtrado espacial que
recorta el ancho de banda espacial y aumenta el área de coherencia (p. 432).

**Teorema de Van Cittert–Zernike** (p. 433). Fijando $\mathbf r_1=\mathbf 0$ en (11.3-20):
$$G_2(\mathbf 0,\mathbf r_2)=\sigma\int h^*(\mathbf 0;\mathbf r)\,h(\mathbf r_2;\mathbf r)\,I_1(\mathbf r)\,d\mathbf r \qquad (11.3\text{-}21)$$
Definiendo $U_2(\mathbf r_2)=G_2(\mathbf 0,\mathbf r_2)$ y $U_1(\mathbf r)=\sigma h^*(\mathbf
0;\mathbf r)I_1(\mathbf r)$:
$$U_2(\mathbf r_2)=\int h(\mathbf r_2;\mathbf r)\,U_1(\mathbf r)\,d\mathbf r \qquad (11.3\text{-}22)$$
que es exactamente (11.3-4). La intensidad mutua $G(\mathbf 0,\mathbf r_2)$ a la salida de un sistema
con entrada incoherente es matemáticamente idéntica a la amplitud compleja que se observaría si una
onda coherente $U_1(\mathbf r)=\sigma h^*(\mathbf 0;\mathbf r)I_1(\mathbf r)$ entrara al mismo
sistema. Ejemplo: entrada incoherente uniforme en una apertura $p(\mathbf r)$ y sistema = espacio
libre, $h(\mathbf r';\mathbf r)=\exp(-jk|\mathbf r'-\mathbf r|)/|\mathbf r'-\mathbf r|$: $G_2(\mathbf
0,\mathbf r_2)$ coincide con la amplitud de una onda esférica $\sigma p(\mathbf r)\exp(jkr)/r$
convergente hacia $\mathbf 0$ transmitida por la apertura. Esta similitud entre difracción de luz
coherente y ganancia de coherencia de luz incoherente es el **teorema de Van Cittert–Zernike**.

**Ganancia de coherencia en el espacio libre** (p. 433–434). Dos planos paralelos separados $d$
(**Fig. 11.3-7**); entrada cuasi-monocromática, espacialmente incoherente, intensidad $I(x,y)$ de
extensión finita; $d$ suficientemente grande para Fraunhofer. Respuesta al impulso [(4.2-3)]:
$$h(\mathbf r;\mathbf r')=h_0\exp\!\left(-j\pi\frac{x^2+y^2}{\lambda d}\right)\exp\!\left(j2\pi\frac{xx'+yy'}{\lambda d}\right) \qquad (11.3\text{-}23)$$
$\mathbf r=(x,y,d)$, $\mathbf r'=(x',y',0)$, $h_0=(j/\lambda d)\exp(-j2\pi d/\lambda)$. Sustituyendo
en (11.3-20):
$$|G(x_1,y_1,x_2,y_2)|=\sigma_1\left|\iint_{-\infty}^{\infty}\exp\!\left\{j\frac{2\pi}{\lambda d}[(x_2-x_1)x+(y_2-y_1)y]\right\}I(x,y)\,dx\,dy\right| \qquad (11.3\text{-}24)$$
$\sigma_1=\sigma|h_0|^2=\sigma/\lambda^2d^2$. Con la transformada 2D de $I(x,y)$
$$\mathcal J(\nu_x,\nu_y)=\iint_{-\infty}^{\infty}\exp[j2\pi(\nu_xx+\nu_yy)]\,I(x,y)\,dx\,dy \qquad (11.3\text{-}25)$$
evaluada en $\nu_x=(x_2-x_1)/\lambda d$, $\nu_y=(y_2-y_1)/\lambda d$:
$$\textbf{[recuadro]}\quad |g(x_1,y_1,x_2,y_2)|=\left|\mathcal J\!\left(\frac{x_2-x_1}{\lambda d},\frac{y_2-y_1}{\lambda d}\right)\right|\Big/\mathcal J(0,0) \qquad (11.3\text{-}26)$$
Relación de Fourier entre el perfil de intensidad de una fuente incoherente y el grado de coherencia
espacial de su campo lejano (análoga a la de amplitudes coherentes en §4.2A, como anticipa Van
Cittert–Zernike). Implicaciones (p. 434): fuente pequeña → $\mathcal J$ ancha → área de coherencia
grande; fuente puntual → área de coherencia infinita (campo espacialmente coherente, cf. §11.1D);
fuente extensa → área de coherencia pequeña.

> **Ejemplo 11.3-2 — Radiation from an Incoherent Circular Source** (p. 435). $I(x,y)=I_0$ en un
> círculo de radio $a$:
> $$|g(x_1,y_1,x_2,y_2)|=\left|\frac{2J_1(\pi\rho\theta_s/\lambda)}{\pi\rho\theta_s/\lambda}\right| \qquad (11.3\text{-}27)$$
> $\rho=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$, $\theta_s=2a/d$ (**Fig. 11.3-8**). Primer cero de $J_1$ en
> 3.832 → área de coherencia = círculo de radio $\rho_c=3.832(\lambda/\pi\theta_s)$:
> $$\textbf{[recuadro]}\quad \rho_c=1.22\frac{\lambda}{\theta_s} \qquad (11.3\text{-}28)\ \text{Distancia de coherencia}$$
> (cf. (11.2-18), obtenida con un análisis menos riguroso). El área de coherencia es $\propto
> 1/\theta_s^2$. Ejemplo numérico: fuente incoherente con $\lambda=0.6\ \mu$m y radio 1 cm vista a
> $d=100$ m → $\rho_c\approx3.7$ mm.

**Medida del diámetro angular de estrellas: interferómetro estelar de Michelson** (p. 435–436).
Estrella = disco incoherente de diámetro $2a$ con brillo uniforme; a distancia $d$, la coherencia
cae a 0 cuando la separación de los puntos de observación llega a $\rho_c=1.22\lambda/\theta_s$;
midiendo $\rho_c$ se obtiene $\theta_s=2a/d$. Sol: $\theta_s=0.5°=8.7\times10^{-3}$ rad →
$\rho_c=140\lambda$; a $\lambda=0.5\ \mu$m, $\rho_c=70\ \mu$m (los agujeros de Young deberían estar
a menos de 70 μm). α-Orión (primera estrella medida así): $\theta_s=22.6\times10^{-8}$ rad →
$\rho_c=3.1$ m a $\lambda=0.57\ \mu$m. **Fig. 11.3-9** (p. 436): interferómetro estelar de
Michelson: espejos móviles $M_1$, $M_2$ separados $\rho$ alimentan un Young; se varía $\rho$ y se
mide la visibilidad; cuando $\rho=\rho_c=1.22\lambda/\theta_s$ la visibilidad es 0.

---

### 11.4 Partial Polarization (p. 436)

La teoría escalar a menudo no basta (cap. 6); la **teoría de la polarización parcial** caracteriza
las componentes del vector campo por correlaciones y correlaciones cruzadas como las del capítulo.
Se ignoran efectos espaciales: onda TEM plana en $z$ con componentes complejas $U_x(t)$, $U_y(t)$
aleatorias. Autocorrelaciones (funciones de coherencia temporal):
$$G_{xx}(\tau)=\langle U_x^*(t)U_x(t+\tau)\rangle \qquad (11.4\text{-}1)$$
$$G_{yy}(\tau)=\langle U_y^*(t)U_y(t+\tau)\rangle \qquad (11.4\text{-}2)$$
Correlación cruzada:
$$G_{xy}(\tau)=\langle U_x^*(t)U_y(t+\tau)\rangle \qquad (11.4\text{-}3)$$
$$g_{xy}(\tau)=\frac{G_{xy}(\tau)}{\sqrt{G_{xx}(0)G_{yy}(0)}} \qquad (11.4\text{-}4)$$
coeficiente de correlación cruzada, $0\le|g_{xy}(\tau)|\le1$ (0: componentes descorrelacionadas; 1:
totalmente correlacionadas). En general las propiedades espectrales y de polarización están ligadas,
pero para luz **cuasi-monocromática** toda la dependencia en $\tau$ es $\approx\exp(j\omega_0\tau)$ y
la polarización se describe por los valores en $\tau=0$: $G_{xx}$, $G_{yy}$, $G_{xy}$. $G_{xx}=I_x$
y $G_{yy}=I_y$ son reales (intensidades de las componentes); $G_{xy}$ es compleja y
$G_{yx}=G_{xy}^*$ (p. 436).

**Matriz de coherencia** (p. 437). Matriz hermítica 2×2:
$$\mathbf G=\begin{bmatrix}G_{xx}&G_{xy}\\G_{yx}&G_{yy}\end{bmatrix} \qquad (11.4\text{-}5)$$
Diagonal: intensidades $I_x$, $I_y$; fuera de la diagonal: correlaciones cruzadas; traza
$\mathrm{Tr}\,\mathbf G=I_x+I_y\equiv\bar I$ = intensidad total. En términos del vector de Jones
$\mathbf J=\begin{bmatrix}U_x\\U_y\end{bmatrix}$ (definido con funciones de onda complejas, no con
envolventes como en §6.1B):
$$\langle\mathbf J^*\mathbf J^\dagger\rangle=\left\langle\begin{bmatrix}U_x^*\\U_y^*\end{bmatrix}[U_x\ \ U_y]\right\rangle=\begin{bmatrix}\langle U_x^*U_x\rangle&\langle U_x^*U_y\rangle\\\langle U_y^*U_x\rangle&\langle U_y^*U_y\rangle\end{bmatrix}=\mathbf G \qquad (11.4\text{-}6)$$
donde $\dagger$ denota transpuesta. Un dispositivo de polarización con matriz de Jones $\mathbf T$
transforma $\mathbf J'=\mathbf T\mathbf J$ [(6.1-17); matrices en (6.1-18)–(6.1-25)], de modo que
$\mathbf G'=\langle\mathbf T^*\mathbf J^*(\mathbf T\mathbf J)^\dagger\rangle=\mathbf T^*\langle\mathbf J^*\mathbf J^\dagger\rangle\mathbf T^\dagger$:
$$\textbf{[recuadro]}\quad \mathbf G'=\mathbf T^*\mathbf G\,\mathbf T^\dagger \qquad (11.4\text{-}7)$$
Formalismo para el efecto de dispositivos de polarización sobre luz parcialmente polarizada.

**Parámetros de Stokes y esfera de Poincaré** (p. 437–438). Generalización de (6.1-9) como promedio:
$$\textbf{[recuadro]}\quad \begin{aligned}
\mathsf S_0&=\langle|U_x|^2\rangle+\langle|U_y|^2\rangle=G_{xx}+G_{yy} &(11.4\text{-}8a)\\
\mathsf S_1&=\langle|U_x|^2\rangle-\langle|U_y|^2\rangle=G_{xx}-G_{yy} &(11.4\text{-}8b)\\
\mathsf S_2&=2\,\mathrm{Re}\{\langle U_x^*U_y\rangle\}=2\,\mathrm{Re}\{G_{xy}\} &(11.4\text{-}8c)\\
\mathsf S_3&=2\,\mathrm{Im}\{\langle U_x^*U_y\rangle\}=2\,\mathrm{Im}\{G_{xy}\} &(11.4\text{-}8d)
\end{aligned}$$
$\mathsf S_0$ = suma de la diagonal = intensidad total $\bar I$; $\mathsf S_1$ = diferencia de
intensidades; $\mathsf S_2$, $\mathsf S_3$ ∝ partes real e imaginaria de la correlación cruzada. De
$|G_{xy}|^2\le G_{xx}G_{yy}$ se sigue $\mathsf S_1^2+\mathsf S_2^2+\mathsf S_3^2\le\mathsf S_0^2$ (igualdad
para luz coherente). Representación en la **esfera de Poincaré**: punto de coordenadas
$(\mathsf S_1/\mathsf S_0,\mathsf S_2/\mathsf S_0,\mathsf S_3/\mathsf S_0)$, dentro o sobre la esfera
unidad (p. 438).

**Luz no polarizada** (p. 438): componentes de igual intensidad y descorrelacionadas,
$I_x=I_y\equiv\tfrac12\bar I$, $G_{xy}=0$:
$$\textbf{[recuadro]}\quad \mathbf G=\tfrac12\bar I\begin{bmatrix}1&0\\0&1\end{bmatrix} \qquad (11.4\text{-}9)\ \text{Luz no polarizada}$$
Por (11.4-7) y (6.1-22) es invariante a rotaciones: las componentes siempre tienen igual intensidad y
están descorrelacionadas; el campo es estadísticamente isótropo en el plano $x$–$y$ (**Fig.
11.4-1**, p. 438: fluctuaciones del vector campo para (a) no polarizada, (b) parcialmente
polarizada, (c) polarizada circular RCP; (d) esfera de Poincaré con puntos "Unpolarized" en el
origen, "Partially polarized" interior, "Polarized" en la superficie, RCP en el polo). Un
polarizador la convierte en linealmente polarizada con intensidad $\tfrac12\bar I$ (sigue siendo
aleatoria); un retardador no la afecta (solo desfasa componentes de fase ya aleatoria); un rotador
la deja no polarizada [se demuestra con (11.4-7), (11.4-9), (6.1-18), (6.2-14), (6.1-20)]. Stokes:
$(\mathsf S_0,\mathsf S_1,\mathsf S_2,\mathsf S_3)=(\bar I,0,0,0)$ → origen de la esfera.

**Luz polarizada** (p. 439): $|g_{xy}|=1$ con $g_{xy}=G_{xy}/\sqrt{I_xI_y}$ (componentes
perfectamente correlacionadas):
$$\mathbf G=\begin{bmatrix}I_x&\sqrt{I_xI_y}\,e^{j\varphi}\\\sqrt{I_xI_y}\,e^{-j\varphi}&I_y\end{bmatrix} \qquad (11.4\text{-}10)$$
$\varphi=\arg g_{xy}$. Con $U_x=\sqrt{I_x}$, $U_y=\sqrt{I_y}e^{j\varphi}$:
$$\mathbf G=\begin{bmatrix}U_x^*U_x&U_x^*U_y\\U_y^*U_x&U_y^*U_y\end{bmatrix}=\mathbf J^*\mathbf J^\dagger \qquad (11.4\text{-}11)$$
misma forma que la matriz de coherencia de una onda coherente; con los vectores de Jones de la
Tabla 6.1-1 se obtienen las matrices de cada estado. **[recuadro]** Dos ejemplos:
$$\text{Lineal en }x:\ \mathbf G=\bar I\begin{bmatrix}1&0\\0&0\end{bmatrix};\qquad \text{Circular derecha:}\ \mathbf G=\tfrac12\bar I\begin{bmatrix}1&j\\-j&1\end{bmatrix}$$
Para (11.4-11), $\mathsf S_1^2+\mathsf S_2^2+\mathsf S_3^2=\mathsf S_0^2$: punto sobre la superficie de
la esfera. Distinción no polarizada vs. circular: en ambas $I_x=I_y$, pero en la circular las
componentes están totalmente correlacionadas (un retardador la convierte en lineal; polos N/S de la
esfera) y en la no polarizada descorrelacionadas (un retardador no la cambia; origen).

**Grado de polarización** (p. 439–440):
$$\mathbb P=\sqrt{1-\frac{4\det\mathbf G}{(\mathrm{Tr}\,\mathbf G)^2}} \qquad (11.4\text{-}12)$$
$$=\sqrt{1-4\left[\frac{I_xI_y}{(I_x+I_y)^2}\right](1-|g_{xy}|^2)} \qquad (11.4\text{-}13)$$
Propiedades: $0\le\mathbb P\le1$; $\mathbb P=1$ para luz polarizada ($|g_{xy}|=1$), $\mathbb P=0$ para
no polarizada ($I_x=I_y$, $g_{xy}=0$); invariante a rotaciones (det y traza invariantes ante
transformaciones unitarias); en términos de Stokes
$$\mathbb P=\frac{\sqrt{\mathsf S_1^2+\mathsf S_2^2+\mathsf S_3^2}}{\mathsf S_0} \qquad (11.4\text{-}14)$$
= distancia al origen en la esfera de Poincaré; una onda parcialmente polarizada siempre puede
verse como mezcla de dos ondas descorrelacionadas, una totalmente polarizada y una no polarizada,
con intensidad polarizada / total = $\mathbb P$ (Ejercicio 11.4-1).

> **Ejercicio 11.4-1 — Partially Polarized Light** (p. 440). Mostrar que la superposición de luz
> no polarizada de intensidad $(I_x+I_y)(1-\mathbb P)$ y luz linealmente polarizada de intensidad
> $(I_x+I_y)\mathbb P$, con $\mathbb P$ dado por (11.4-13), produce luz cuyas componentes $x$, $y$
> tienen intensidades $I_x$, $I_y$ y correlación cruzada normalizada $|g_{xy}|$.

---

### Reading List (p. 440–442)

Referencias generales (Kokhanovsky 2003; O'Neill 1963/2003; Lauterborn & Kurz 2003; Born & Wolf,
*Principles of Optics*, 7.ª ed. 2002, cap. 10; Frieden 2001; **Goodman, *Statistical Optics*,
Wiley 1985/2000**; Rowe 1999; Brosseau 1998; **Mandel & Wolf, *Optical Coherence and Quantum
Optics*, CUP 1995**; Lefèvre 1993; Reynolds et al. 1989; Peřina 1985; Dainty (speckle) 1984;
Marathay 1982; Saleh 1978; Crosignani et al. 1975; Beran & Parrent 1964/1974; Hanbury-Brown 1974;
Troup 1967), libros de funciones aleatorias (Papoulis & Pillai 2002; Parzen; Helstrom; Davenport &
Root; Vanmarcke; Thomas), libros de OCT (Brezinski 2006; Drexler 2003, 2005; Bouma & Tearney 2002)
y artículos (Tomlins & Wang 2005 y Fercher et al. 2003 sobre OCT; Mandel & Wolf, *Rev. Mod. Phys.*
37, 231, 1965; Thompson 1969; Tango & Twiss 1980; Wolf 1978; etc.).

---

## Tablas y datos numéricos útiles

- **Tabla 11.1-1** (p. 411), relación $\Delta\nu_{\rm FWHM}$ – $\tau_c$ (con $\tau_c$ de (11.1-10)):
  rectangular $1/\tau_c$; lorentziana $1/\pi\tau_c\approx0.32/\tau_c$; gaussiana
  $\sqrt{2\ln2/\pi}/\tau_c\approx0.66/\tau_c$. Con la definición (11.1-18), $\Delta\nu_c=1/\tau_c$
  siempre (11.1-19).
- **Tabla 11.1-2** (p. 412), fuentes típicas (ver tabla completa en §11.1B): luz solar filtrada
  $\Delta\nu_c=3.74\times10^{14}$ Hz, $\tau_c=2.67$ fs, $l_c=800$ nm; LED (1 μm, 50 nm)
  $1.5\times10^{13}$ Hz, 67 fs, 20 μm; sodio baja presión $5\times10^{11}$ Hz, 2 ps, 600 μm; He–Ne
  multimodo $1.5\times10^{9}$ Hz, 0.67 ns, 20 cm; He–Ne monomodo $10^{6}$ Hz, 1 μs, 300 m.
- Ejercicio 11.1-1 (p. 409): $g$ exponencial $\exp(-|\tau|/\tau_c)$, gaussiano
  $\exp(-\pi\tau^2/2\tau_c^2)$.
- Ejemplo 11.1-1 (p. 413): paquetes con envolvente exponencial → espectro lorentziano
  $S(\nu)=(\Delta\nu/2\pi)/[(\nu-\nu_0)^2+(\Delta\nu/2)^2]$, $\Delta\nu=1/\pi\tau_c$.
- Área de coherencia de una superficie caliente extensa: $\sim\lambda^2$ (p. 415).
- Sol: $\theta_s=0.5°=8.7\times10^{-3}$ rad; $\rho_c\approx\lambda/\theta_s\approx115\lambda$
  (estimación simple, p. 425) o $1.22\lambda/\theta_s=140\lambda$ (riguroso, p. 435); a
  $\lambda=0.5\ \mu$m: 57.5 μm y 70 μm respectivamente.
- α-Orión: $\theta_s=22.6\times10^{-8}$ rad → $\rho_c=3.1$ m a $\lambda=0.57\ \mu$m (p. 435).
- Fuente incoherente circular, $\lambda=0.6\ \mu$m, radio 1 cm, $d=100$ m → $\rho_c\approx3.7$ mm
  (p. 435).
- Primer cero de $J_1(x)$: $x=3.832$ → factor $3.832/\pi=1.22$ (p. 431, 435).
- Frecuencias de corte de una lente con $F_\#$: coherente $1/(2\lambda F_\#)$, incoherente
  $1/(\lambda F_\#)$ líneas/mm (11.3-19, p. 432); resolución $\rho_s\approx1.22\lambda/\theta=1.22
  \lambda F_\#$ (11.3-16).
- Número de franjas de Young observables con luz espacialmente coherente: $l_c/\bar\lambda=\nu_0/
  \Delta\nu_c$ (p. 426).

---

## Problemas al final del capítulo (p. 442–443)

(Los ejercicios 11.1-1, 11.1-2, 11.1-3 y 11.4-1 están en el texto; aquí la numeración de problemas
continúa.) Los marcados con * son avanzados (sección 11.3).

- **11.1-4 Lorentzian Spectrum.** LED con espectro lorentziano, $\Delta\nu$ (FWHM) $=10^{13}$ Hz,
  $\lambda_o=0.7\ \mu$m. Hallar $\Delta\lambda_o$ (nm), $\tau_c$, $l_c$ y el máximo retardo con
  $|g(\tau)|>0.5$.
- **11.1-5 Proof of the Wiener–Khinchin Theorem.** Con (11.1-4), (11.1-14) y (11.1-15) demostrar
  que $S(\nu)$ es la transformada de Fourier de $G(\tau)$ y que $I=\int S(\nu)d\nu$.
- **11.1-6 Mutual Intensity.** $G(x_1,x_2)=I_0\exp[-(x_1^2+x_2^2)/W_0^2]\exp[-(x_1-x_2)^2/\rho_c^2]$.
  Dibujar $I(x)$, deducir y dibujar $g(x_1,x_2)$ vs. $x_1-x_2$; significado físico de $I_0$, $W_0$,
  $\rho_c$.
- **11.1-7 Mutual Coherence Function.** $G(x_1,x_2,\tau)=\exp(-\pi\tau^2/2\tau_c^2)\exp[j2\pi
  u(x_1,x_2)\tau]\exp[-(x_1-x_2)^2/\rho_c^2]$ con $u=5\times10^{14}$ s⁻¹ si $x_1+x_2>0$ y
  $6\times10^{14}$ s⁻¹ si $x_1+x_2<0$, $\rho_c=1$ mm, $\tau_c=1\ \mu$s. Hallar intensidad, densidad
  espectral de potencia, longitud de coherencia y distancia de coherencia transversal; cuáles
  dependen de la posición; aspecto de la imagen en película de color.
- **11.1-8 Coherence Length.** Mostrar que para línea estrecha $l_c\approx\lambda^2/\Delta\lambda$;
  y que para espectro uniforme entre $\lambda_{\min}$ y $\lambda_{\max}=2\lambda_{\min}$,
  $l_c=\lambda_{\max}$.
- **11.1-9 Effect of Spectral Width on Spatial Coherence.** Fuente puntual en el origen con espectro
  lorentziano y $\tau_c=10$ ps. Hallar la intensidad mutua normalizada entre $(0,0,d)$ y $(x,0,d)$
  con $d=10$ cm; dibujar su módulo vs. $x$.
- **11.1-10 Gaussian Mutual Intensity.** $G(\mathbf r_1,\mathbf r_2,\tau)=J(\mathbf r_1-\mathbf
  r_2)\exp(j\omega_0\tau)$ en el vacío. (a) Mostrar que $J(\mathbf r)$ cumple Helmholtz
  $\nabla^2J+k_o^2J=0$, $k_o=\omega_0/c$. (b) Con la solución de haz gaussiano
  $J(\mathbf r)=\frac{1}{q(z)}\exp[-jk_o(x^2+y^2)/2q(z)]\exp(-jk_oz)$, $q(z)=z+jz_0$, hallar el área
  de coherencia cerca del eje y mostrar que crece con $|z|$ (la onda gana coherencia al propagarse).
- **11.2-1 Effect of Spectral Width on Fringe Visibility.** Lámpara de sodio lorentziana,
  $\Delta\nu=5\times10^{11}$ Hz, en un Michelson. Máxima diferencia de camino con $\mathcal V>\tfrac12$.
- **11.2-2 Number of Observable Fringes in Young's Interferometer.** Número de franjas para cada
  fuente de la Tabla 11.1-2, suponiendo coherencia espacial completa.
- **11.2-3 Spectrum of a Superposition of Two Waves.** $U=U_1+U_2$ con espectros gaussianos
  idénticos ($\Delta\nu$, $\nu_0$), no necesariamente descorrelacionadas. Hallar $S(\nu)$ de la
  superposición; explorar si puede ser gaussiano con centro desplazado $\nu_1\neq\nu_0$ (lo que
  cuestionaría el uso del Doppler para medir velocidades estelares).
- ***11.3-1 Partially Coherent Gaussian Beam.** Luz cuasi-monocromática con $I(x)=I_0\exp(-2x^2/
  W_0^2)$ y $g(x_1,x_2)=\exp[-(x_1-x_2)^2/\rho_c^2]$ en $z=0$. Mostrar que en Fraunhofer
  $I_z(x)\propto\exp[-2x^2/W^2(z)]$ y deducir $W(z)$ en función de $W_0$, $\rho_c$, $\lambda$;
  discutir el efecto de la coherencia espacial sobre la divergencia.
- ***11.3-2 Fourier-Transform Lens.** Luz incoherente uniforme ilumina una transparencia de
  transmitancia de intensidad $f(x,y)$ entre los planos focales de una lente. Hallar la intensidad
  observada y comparar con el caso coherente (§4.2).
- ***11.3-3 Light from Two-Point Incoherent Source.** Fuente incoherente cuasi-monocromática que
  emite en dos puntos separados $2a$. Intensidad mutua normalizada a distancia $d$ (Fraunhofer).
- ***11.3-4 Coherence of Light Transmitted Through a Fourier-Transform Optical System.** Fuente
  incoherente uniforme por una rendija de ancho $2a$ entre planos focales de una lente. Intensidad
  mutua normalizada en el plano focal posterior.
- **11.4-2 Partially Polarized Light.** $I_x=I_y=\tfrac12$, $\arg g_{xy}=\pi/2$. (a) Graficar
  $\mathbb P$ vs. $|g_{xy}|$. (b) Matriz de coherencia para $\mathbb P=0,\ 0.5,\ 1$ y naturaleza de
  la luz. (c) Intensidad transmitida por un polarizador con eje en $x$.

---

## Relación con Óptica No Lineal

**Temas del curso**

- *Ondas EM y haz gaussiano.* La función de coherencia mutua obedece la ecuación de onda en cada
  argumento (Ej. 11.1-3, p. 414) y, para luz cuasi-monocromática, la intensidad mutua obedece
  Helmholtz (Prob. 11.1-10): el haz gaussiano del cap. 3 reaparece como solución para $J(\mathbf
  r)$, y la coherencia espacial finita ($\rho_c$) aumenta la divergencia del haz (Prob. *11.3-1).
  Útil al justificar por qué un haz de bombeo parcialmente coherente se enfoca peor y reduce la
  eficiencia de procesos no lineales que escalan con la intensidad.
- *Absorción/dispersión y pulsos en medios dispersivos; GVD.* La pareja Wiener–Khinchin
  $G(\tau)\leftrightarrow S(\nu)$ (11.1-17, p. 410) y la relación $\Delta\nu_c=1/\tau_c$ (11.1-19)
  son el análogo estadístico de la relación tiempo–ancho de banda de un pulso: un pulso corto
  transformado-limitado tiene espectro ancho igual que una luz con $\tau_c$ corto. La Tabla 11.1-1
  (p. 411) da los factores de forma para perfiles rectangular, lorentziano y gaussiano, que son los
  mismos que aparecen en el producto $\Delta\nu\,\Delta t$ de pulsos. La longitud de coherencia
  $l_c=c\tau_c$ (11.1-12) fija cuánta diferencia de camino tolera un interferómetro: relevante para
  caracterizar pulsos (autocorrelación de intensidad ≈ interferograma de Michelson, (11.2-7)–
  (11.2-8), p. 420–421) y para espectroscopía por transformada de Fourier (11.2-10).
- *Polarización y cristales.* La matriz de coherencia $\mathbf G=\langle\mathbf J^*\mathbf
  J^\dagger\rangle$ (11.4-5/6, p. 437), su transformación $\mathbf G'=\mathbf T^*\mathbf G\mathbf
  T^\dagger$ (11.4-7) con las matrices de Jones del cap. 6 (polarizadores, retardadores, rotadores),
  los parámetros de Stokes (11.4-8) y el grado de polarización $\mathbb P$ (11.4-12 a 11.4-14) son el
  lenguaje correcto para luz que atraviesa cristales birrefringentes o celdas electro-ópticas cuando
  la fuente no es perfectamente polarizada (p. ej. luz de un SLD o de un supercontinuo
  despolarizado). Las matrices de los casos límite (no polarizada (11.4-9), lineal en $x$, circular
  derecha, p. 439) sirven como punto de partida de cálculos.
- *Susceptibilidad no lineal, χ⁽²⁾, χ⁽³⁾, índice dependiente de la intensidad.* Los procesos no
  lineales dependen de $\langle|U|^4\rangle$ y de productos de campos, no solo de la intensidad
  promedio $\langle|U|^2\rangle$ (11.1-2): la estadística de la fuente (p. ej. luz térmica de
  paquetes aleatorios, Ejemplo 11.1-1, p. 412–413, frente a luz láser coherente, $|g(\tau)|=1$)
  modifica la eficiencia de SHG, SPM y FWM. Este capítulo da las herramientas (promedios de
  conjunto, $G$, $g$) para formular esas correcciones.
- *Propagación de pulsos en fibras, SPM/solitones/XPM, Raman, FWM.* Los interferómetros con luz de
  baja coherencia (OCT, p. 422–423) y la condición "solo hay interferencia si la diferencia de
  camino es menor que $l_c$" (p. 421) son la base de medidas de dispersión de guías por
  interferometría de luz blanca; la mezcla de dos ondas con espectros gaussianos (Prob. 11.2-3) y la
  ganancia de coherencia por filtrado (p. 432: analogía ruido blanco → filtro pasa-bajos) ayudan a
  interpretar el espectro de un supercontinuo, que es ancho (bajo $\tau_c$) y, según el régimen de
  generación, puede ser poco coherente de disparo a disparo.

**Proyecto final (anillos add-drop en Si₃N₄, dispersión de guías, supercontinuo, sensado de índice)**

- *Coherencia temporal y ancho espectral ↔ supercontinuo.* El supercontinuo tiene $\Delta\nu$
  enorme → $\tau_c$ de pocos fs y $l_c<1\ \mu$m (comparable a la luz solar filtrada de la Tabla
  11.1-2, p. 412: $l_c=800$ nm). Esto limita la interferometría con supercontinuo a diferencias de
  camino submicrométricas y explica por qué los resonadores de anillo con FSR fino "ven" el
  supercontinuo como fuente incoherente de banda ancha; la respuesta del add-drop se obtiene
  entonces integrando la transmitancia espectral contra $S(\nu)$ (11.1-16/17), no sumando amplitudes.
  La definición de $\Delta\nu_c$ (11.1-18) y el número de franjas observables $\nu_0/\Delta\nu_c$
  (p. 426) dan criterios cuantitativos.
- *Sensado de índice de refracción.* Un anillo con $Q$ alto equivale a un filtro de ancho
  $\Delta\nu=\nu_0/Q$; la luz filtrada por la resonancia tiene $\tau_c=Q/\nu_0$ (11.1-19) y gana
  coherencia a costa de energía (p. 411, 419). Para leer el desplazamiento de resonancia con una
  fuente de banda ancha conviene recordar que la visibilidad del interferograma decae como
  $|g(\tau)|$ (11.2-8) y que el espectro medido es la convolución del perfil de la fuente con la
  respuesta del anillo (Wiener–Khinchin). La OCT (11.2-11/12) es además el prototipo de
  interferómetro de baja coherencia que se puede adaptar a medir el camino óptico en función del
  índice del analito.
- *Dispersión de guías.* La medición de $n_g$ y GVD por interferometría de luz blanca (Michelson o
  Mach–Zehnder con la guía en un brazo) se rige por (11.2-7)–(11.2-10): el interferograma es la
  transformada de Fourier del espectro ponderado por la fase dispersiva de la guía; de aquí se
  extrae $\beta_2$. Las ondas plana y esférica parcialmente coherentes (11.1-31 a 11.1-36, p. 417–
  418) muestran que la coherencia longitudinal es la temporal "vista en $z$": en una guía
  monomodo la coherencia espacial es completa y solo importa la temporal.
- *Matriz de coherencia / Stokes.* En guías de Si₃N₄ los modos TE y TM tienen $n_{\rm eff}$
  distintos; si la fuente excita ambos con correlación parcial, la luz a la salida es parcialmente
  polarizada y su estado se describe con $\mathbf G$ y $(\mathsf S_0,\dots,\mathsf S_3)$ (p. 437–
  440). El grado de polarización $\mathbb P$ (11.4-14) y la esfera de Poincaré (Fig. 11.4-1(d))
  permiten cuantificar la despolarización introducida por la birrefringencia de la guía o por el
  anillo, y la regla (11.4-7) da el efecto de polarizadores/retardadores en el banco de medida.
