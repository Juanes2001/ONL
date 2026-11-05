# Apéndices A, B, C y Símbolos (Saleh & Teich, 2.ª ed.)

Páginas del libro 1122–1158 (PDF 1144–1180). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007.
Apéndice A "Fourier Transform" (pp. 1122–1131), Apéndice B "Linear Systems" (pp. 1132–1136),
Apéndice C "Modes of Linear Systems" (pp. 1137–1141) y "Symbols and Units" (pp. 1142–1158).

Convenciones de estos apuntes:
- Se respeta la notación del libro: $j = \sqrt{-1}$, dependencia temporal $\exp(j2\pi\nu t) = \exp(j\omega t)$,
  frecuencia $\nu$ en Hz, frecuencia angular $\omega = 2\pi\nu$ en rad/s. Unidades SI.
- Las ecuaciones conservan la numeración del libro (A.1-1, B.1-3, C.1-2, …). Las que el libro enmarca
  (ecuaciones "clave") se marcan con **[recuadro]**.
- Cada ítem lleva la página del libro entre corchetes, p. ej. [p. 1123].
- Todas las páginas fueron legibles; las dos únicas dudas de lectura se señalan explícitamente
  (Tabla A.2-1, fila "Chirp", y la nota sobre $\mathcal{B}$ en Símbolos).

---

## Apéndice A — Transformada de Fourier

### A.1 Transformada de Fourier unidimensional [pp. 1122–1124]

**Función armónica.** $F\exp(j2\pi\nu t)$ tiene frecuencia $\nu$ y amplitud compleja $F$. Su parte real
$|F|\cos(2\pi\nu t + \arg\{F\})$ es un coseno de amplitud $|F|$ y fase $\arg\{F\}$. $t$ suele ser el
tiempo y $\nu$ tiene unidades de ciclos/s o Hz. La función armónica es el "bloque de construcción" a
partir del cual otras funciones se obtienen por superposición [p. 1122].

**Teorema de Fourier.** Una función compleja $f(t)$ (bajo condiciones poco restrictivas) se descompone
como integral de superposición de armónicas de distintas frecuencias y amplitudes complejas:

$$f(t) = \int_{-\infty}^{\infty} F(\nu)\,\exp(j2\pi\nu t)\,d\nu \qquad \text{(A.1-1) Transformada inversa de Fourier [recuadro]}$$

La componente de frecuencia $\nu$ tiene amplitud compleja

$$F(\nu) = \int_{-\infty}^{\infty} f(t)\,\exp(-j2\pi\nu t)\,dt \qquad \text{(A.1-2) Transformada de Fourier [recuadro]}$$

$F(\nu)$ es la **transformada de Fourier** de $f(t)$ y $f(t)$ la **transformada inversa** de $F(\nu)$;
forman un par transformado: conocida una, se determina la otra [p. 1122].

**Convención de signo del libro (importante).** $\exp(j2\pi\nu t)$ es una armónica de **frecuencia
positiva**; $\exp(-j2\pi\nu t)$ representa frecuencia negativa. Algunos autores usan la convención
opuesta: signo positivo en el exponente de (A.1-2) y negativo en el de (A.1-1) [p. 1122].
(Ver también la convención *espacial* opuesta en A.3 y la sección final de estos apuntes.)

**Terminología de comunicaciones.** $f(t)$ = representación temporal de la señal; $F(\nu)$ =
representación en frecuencia. $|f(t)|^2$ es la **potencia de la señal** y $|F(\nu)|^2$ la
**densidad espectral de energía**. Si $|F(\nu)|^2$ se extiende sobre un rango amplio de frecuencias,
la señal tiene **ancho de banda** amplio [pp. 1122–1123].

#### Propiedades de la transformada de Fourier [p. 1123]

Se demuestran aplicando directamente (A.1-1) y (A.1-2).

- **Linealidad.** La TF de la suma de dos funciones es la suma de sus TF.
- **Escalamiento.** Si $f(t) \leftrightarrow F(\nu)$ y $\tau$ es un factor real de escala, entonces
  $f(t/\tau) \leftrightarrow |\tau|\,F(\tau\nu)$. Escalar $f(t)$ por $\tau$ escala su TF por $1/\tau$:
  si $\tau > 1$, $f(t/\tau)$ es una versión estirada de $f(t)$ y $F(\tau\nu)$ una versión comprimida
  de $F(\nu)$. La TF de $f(-t)$ es $F(-\nu)$.
- **Traslación temporal.** $f(t-\tau) \leftrightarrow \exp(-j2\pi\nu\tau)\,F(\nu)$. Un retardo $\tau$
  equivale a multiplicar la TF por el factor de fase $\exp(-j2\pi\nu\tau)$.
- **Traslación en frecuencia.** $f(t)\exp(j2\pi\nu_0 t) \leftrightarrow F(\nu-\nu_0)$. Multiplicar
  por una armónica de frecuencia $\nu_0$ desplaza la TF a una frecuencia mayor $\nu_0$.
- **Simetría.** Si $f(t)$ es real, $F(\nu)$ tiene simetría hermítica: $F(-\nu) = F^*(\nu)$. Si $f(t)$
  es real y simétrica, $F(\nu)$ también es real y simétrica.
- **Teorema de convolución.** Si $f_1 \leftrightarrow F_1$ y $f_2 \leftrightarrow F_2$, la TF inversa
  del producto

  $$F(\nu) = F_1(\nu)F_2(\nu) \qquad \text{(A.1-3)}$$

  es

  $$f(t) = \int_{-\infty}^{\infty} f_1(\tau)\,f_2(t-\tau)\,d\tau \qquad \text{(A.1-4) Convolución [recuadro]}$$

  (A.1-4) es la **convolución** de $f_1(t)$ con $f_2(t)$. Convolución en el tiempo ⇔ multiplicación
  en el dominio de Fourier.
- **Teorema de correlación.** La correlación de dos funciones complejas se define como

  $$f(t) = \int_{-\infty}^{\infty} f_1^*(\tau)\,f_2(t+\tau)\,d\tau \qquad \text{(A.1-5) Correlación [recuadro]}$$

  y las TF se relacionan por

  $$F(\nu) = F_1^*(\nu)\,F_2(\nu) \qquad \text{(A.1-6)}$$

- **Teorema de Parseval** [p. 1124]. La energía de la señal (integral de la potencia $|f(t)|^2$) es
  igual a la integral de la densidad espectral de energía $|F(\nu)|^2$:

  $$\int_{-\infty}^{\infty} |f(t)|^2\,dt = \int_{-\infty}^{\infty} |F(\nu)|^2\,d\nu \qquad \text{(A.1-7) Teorema de Parseval [recuadro]}$$

#### Ejemplos y funciones especiales [p. 1124]

Las TF de las funciones importantes del libro están en la **Tabla A.2-1** (así la numera el libro;
está en la p. 1125, dentro de A.2). No existe una "Tabla A.1-1" ni una "Tabla A.3-1" en estas páginas.
Con linealidad, escalamiento, retardo y traslación en frecuencia se obtienen las demás. Definiciones:

- $\mathrm{rect}(t) \equiv 1$ para $|t| \le \tfrac{1}{2}$ y $0$ en el resto: pulso de altura y ancho
  unidad centrado en $t = 0$.
- $\delta(t)$ = función impulso (delta de Dirac), definida como
  $\delta(t) = \lim_{\alpha\to\infty} \alpha\,\mathrm{rect}(\alpha t)$: límite de un pulso rectangular
  de área unidad cuando su ancho tiende a cero (altura a infinito).
- $\mathrm{sinc}(t) = \sin(\pi t)/(\pi t)$: simétrica, valor pico $1.0$ en $t = 0$, ceros en
  $t = \pm 1, \pm 2, \dots$

#### Tabla A.2-1 — Funciones seleccionadas y sus transformadas de Fourier [p. 1125]

Transcripción fiel (convención (A.1-2), signo negativo en el exponente directo). El libro acompaña
cada fila con una gráfica de $f(t)$ y de $F(\nu)$ (no reproducidas aquí).

| Función | $f(t)$ | $F(\nu)$ |
|---|---|---|
| Uniforme | $1$ | $\delta(\nu)$ |
| Impulso | $\delta(t)$ | $1$ |
| Rectangular | $\mathrm{rect}(t)$ | $\mathrm{sinc}(\nu)$ |
| Exponencial$^a$ | $\exp(-\lvert t\rvert)$ | $\dfrac{2}{1+(2\pi\nu)^2}$ |
| Gaussiana | $\exp(-\pi t^2)$ | $\exp(-\pi\nu^2)$ |
| Secante hiperbólica | $\mathrm{sech}(\pi t)$ | $\mathrm{sech}(\pi\nu)$ |
| Chirp$^b$ | $\exp(j\pi t^2)$ | $e^{j\pi/4}\exp(j\pi t^2)$ (ver nota de lectura) |
| $M = 2S+1$ impulsos | $\displaystyle\sum_{m=-S}^{S}\delta(t-m)$ | $\dfrac{\sin(M\pi\nu)}{\sin(\pi\nu)}$ |
| Peine (comb) | $\displaystyle\sum_{m=-\infty}^{\infty}\delta(t-m)$ | $\displaystyle\sum_{m=-\infty}^{\infty}\delta(\nu-m)$ |

Notas al pie de la tabla [p. 1125]:
- $^a$ Se muestra la exponencial de dos lados. La TF de la exponencial de un lado,
  $f(t) = \exp(-t)$ con $t \ge 0$, es $F(\nu) = 1/[1 + j2\pi\nu]$; su magnitud es
  $1/\sqrt{1+(2\pi\nu)^2}$.
- $^b$ Se grafican $\cos(\pi t^2)$ y $\cos(\pi\nu^2)$. La función $\sin(\pi t^2)$ se muestra en la
  Fig. 4.3-6.

**Nota de lectura (fila Chirp).** En el escaneo, la columna $F(\nu)$ de la fila "Chirp" se lee como
$e^{j\pi/4}\exp(j\pi t^2)$, es decir, con la variable $t$ y signo positivo, lo que parece una errata
de imprenta (la columna debería depender de $\nu$). Calculando con (A.1-2):
$\int \exp(j\pi t^2)\exp(-j2\pi\nu t)\,dt = e^{j\pi/4}\exp(-j\pi\nu^2)$ (integral de Fresnel
$\int\exp(j\pi u^2)\,du = e^{j\pi/4}$). Ese resultado es consistente con el ejemplo del "sistema
con chirp" del Apéndice B [p. 1133]: $h(t) = e^{-j\pi/4}\exp(j\pi t^2) \leftrightarrow H(\nu) = \exp(-j\pi\nu^2)$.
Por tanto la entrada correcta es $F(\nu) = e^{j\pi/4}\exp(-j\pi\nu^2)$; no lo doy como transcripción
literal sino como corrección razonada.

### A.2 Duración temporal y ancho espectral [pp. 1124–1128]

Ancho de $f(t)$ = duración temporal; ancho de $F(\nu)$ = ancho espectral (ancho de banda). No hay
definición única; **todas las definiciones comparten que el ancho espectral es inversamente
proporcional al ancho temporal**, por la propiedad de escalamiento [p. 1124].

#### Ancho RMS (raíz cuadrática media) [pp. 1124–1126]

Para una función real no negativa $f(t)$:

$$\sigma_t^2 = \frac{\int_{-\infty}^{\infty}(t-\bar t)^2 f(t)\,dt}{\int_{-\infty}^{\infty} f(t)\,dt},
\qquad \bar t = \frac{\int_{-\infty}^{\infty} t\,f(t)\,dt}{\int_{-\infty}^{\infty} f(t)\,dt} \qquad \text{(A.2-1)}$$

Si $f(t)$ es una distribución de masa ($t$ = posición), $\bar t$ es el centroide y $\sigma_t$ el radio
de giro; si $f(t)$ es una densidad de probabilidad, son la media y la desviación estándar [p. 1124].

Ejemplo: la **gaussiana** $f(t) = \exp(-t^2/2\sigma_t^2)$ tiene ancho RMS $\sigma_t$. Su TF es
$F(\nu) = (1/\sqrt{2\pi}\,\sigma_\nu)\exp(-\nu^2/2\sigma_\nu^2)$ con

$$\sigma_\nu = \frac{1}{2\pi\sigma_t} \qquad \text{(A.2-2)}$$

que es el ancho espectral RMS [p. 1124].

**Ancho RMS de potencia (power-rms width)** [p. 1125]. (A.2-1) no sirve para funciones negativas o
complejas; se usa entonces el ancho RMS de $|f(t)|^2$:

$$\sigma_t^2 = \frac{\int_{-\infty}^{\infty}(t-\bar t)^2 |f(t)|^2\,dt}{\int_{-\infty}^{\infty}|f(t)|^2\,dt},
\qquad \bar t = \frac{\int_{-\infty}^{\infty} t\,|f(t)|^2\,dt}{\int_{-\infty}^{\infty}|f(t)|^2\,dt}$$

**Relación de reciprocidad duración–ancho de banda** [pp. 1125–1126]. Por la desigualdad de Schwarz,
el producto de los anchos RMS de potencia de $f(t)$ y $F(\nu)$ cumple

$$\sigma_t\sigma_\nu \ge \frac{1}{4\pi} \qquad \text{(A.2-3) Relación de reciprocidad duración–ancho de banda [recuadro]}$$

con

$$\sigma_\nu^2 = \frac{\int_{-\infty}^{\infty}(\nu-\bar\nu)^2 |F(\nu)|^2\,d\nu}{\int_{-\infty}^{\infty}|F(\nu)|^2\,d\nu},
\qquad \bar\nu = \frac{\int_{-\infty}^{\infty} \nu\,|F(\nu)|^2\,d\nu}{\int_{-\infty}^{\infty}|F(\nu)|^2\,d\nu}$$

Duración y ancho espectral no pueden hacerse simultáneamente arbitrariamente pequeños. La gaussiana
$f(t) = \exp(-t^2/4\sigma_t^2)$ tiene ancho RMS de potencia $\sigma_t$; su TF también es gaussiana,
$F(\nu) = (1/2\sqrt{\pi}\,\sigma_\nu)\exp(-\nu^2/4\sigma_\nu^2)$, con ancho RMS de potencia

$$\sigma_\nu = \frac{1}{4\pi\sigma_t} \qquad \text{(A.2-4)}$$

Como $\sigma_t\sigma_\nu = 1/4\pi$, **la gaussiana alcanza el mínimo** del producto duración–ancho de
banda [p. 1126]. En frecuencia angular $\omega = 2\pi\nu$:

$$\sigma_t\sigma_\omega \ge \frac{1}{2} \qquad \text{(A.2-5)}$$

Reemplazando $t$ y $\omega$ por la posición $x$ y la frecuencia angular espacial $k$ (rad/m):

$$\sigma_x\sigma_k \ge \frac{1}{2} \qquad \text{(A.2-6)}$$

En mecánica cuántica, $\psi(x)$ describe la posición y $\phi(k)$ (su TF) el número de onda; las
incertidumbres son los anchos RMS de $|\psi(x)|^2$ y $|\phi(k)|^2$. Con $p = \hbar k$
($\hbar = h/2\pi$):

$$\sigma_x\sigma_p \ge \frac{\hbar}{2} \qquad \text{(A.2-7) Relación de incertidumbre de Heisenberg [recuadro]}$$

#### Ancho equivalente en potencia (power-equivalent width) [pp. 1126–1127]

Energía de la señal dividida por la potencia pico. Si el pico de $f(t)$ está en $t = 0$:

$$\tau = \int_{-\infty}^{\infty}\frac{|f(t)|^2}{|f(0)|^2}\,dt \qquad \text{(A.2-8)}$$

La exponencial de dos lados $f(t) = \exp(-|t|/\tau)$ tiene ancho equivalente en potencia $\tau$, igual
que la gaussiana $f(t) = \exp(-\pi t^2/2\tau^2)$. Esta definición se usa en la Sec. 11.1, donde el
**tiempo de coherencia** se define como el ancho equivalente en potencia del grado complejo de
coherencia temporal [p. 1127].

Ancho espectral equivalente en potencia:

$$\mathcal{B} = \int_{-\infty}^{\infty}\frac{|F(\nu)|^2}{|F(0)|^2}\,d\nu \qquad \text{(A.2-9)}$$

Si $f(t)$ es real ($|F(\nu)|^2$ simétrico) y con pico en $\nu = 0$, se define usualmente el ancho de
frecuencias positivas:

$$B = \int_{0}^{\infty}\frac{|F(\nu)|^2}{|F(0)|^2}\,d\nu \qquad \text{(A.2-10)}$$

Para $F(\nu) = \tau/(1+j2\pi\nu\tau)$:

$$B = \frac{1}{4\tau} \qquad \text{(A.2-11)}$$

Esta definición se usa en la Sec. 18.6A (ancho de banda de circuitos de fotodetección con ruido
fotónico y de circuito; ver Problema 18.5-5) [p. 1127].

Con Parseval (A.1-7) y $F(0) = \int f(t)\,dt$, (A.2-10) se escribe

$$B = \frac{1}{2T} \qquad \text{(A.2-12)}$$

donde

$$T = \frac{\left[\int_{-\infty}^{\infty} f(t)\,dt\right]^2}{\int_{-\infty}^{\infty} f^2(t)\,dt} \qquad \text{(A.2-13)}$$

es otra definición de duración (cuadrado del área bajo $f$ dividido por el área bajo $f^2$). En este
caso el producto duración–ancho de banda es $BT = \tfrac{1}{2}$ [p. 1127].

#### Anchos a $1/e$, a mitad del máximo y a 3 dB [pp. 1127–1128]

Duración a una fracción prescrita del máximo ($1/\sqrt{2}$, $1/2$, $1/e$, $1/e^2$). Se usa el
semiancho o el ancho completo. Las dos medidas más comunes: **FWHM** (ancho completo a mitad del
máximo) y el semiancho a $1/\sqrt{2}$ del máximo, llamado **ancho de 3 dB**. Tres ejemplos:

1. **Exponencial de un lado** $f(t) = \exp(-t/\tau)$ para $t \ge 0$, $0$ para $t < 0$ (respuesta de
   muchos sistemas eléctricos y ópticos): semiancho a $1/e$ del máximo $\Delta t_{1/e} = \tau$. La
   magnitud de su TF $F(\nu) = \tau/(1+j2\pi\nu\tau)$ tiene ancho de 3 dB (semiancho a $1/\sqrt{2}$):

   $$\Delta\nu_{3\text{-dB}} = \frac{1}{2\pi\tau} \qquad \text{(A.2-14)}$$

2. **Exponencial de dos lados** $f(t) = \exp(-|t|/\tau)$: semiancho a $1/e$ $\Delta t_{1/e} = \tau$.
   Su TF $F(\nu) = 2\tau/[1+(2\pi\nu\tau)^2]$, la **distribución lorentziana**, tiene FWHM

   $$\Delta\nu_{\mathrm{FWHM}} = \frac{1}{\pi\tau} \qquad \text{(A.2-15)}$$

   y se escribe usualmente $F(\nu) = (\Delta\nu/2\pi)/[\nu^2 + (\Delta\nu/2)^2]$ con
   $\Delta\nu = \Delta\nu_{\mathrm{FWHM}}$. La lorentziana describe el espectro de ciertas emisiones
   luminosas (Sec. 13.3D) [p. 1128].

3. **Gaussiana** $f(t) = \exp(-t^2/2\tau^2)$: ancho completo a $1/e$ $\Delta t_{1/e} = 2\sqrt{2}\,\tau$.
   Su TF $F(\nu) = \sqrt{2\pi}\,\tau\exp(-2\pi^2\tau^2\nu^2)$ tiene ancho completo a $1/e$

   $$\Delta\nu_{1/e} = \frac{\sqrt{2}}{\pi\tau} \qquad \text{(A.2-16)}$$

   y FWHM

   $$\Delta\nu_{\mathrm{FWHM}} = \frac{\sqrt{2\ln 2}}{\pi\tau} \qquad \text{(A.2-17)}$$

   de modo que

   $$\Delta\nu_{\mathrm{FWHM}} = \sqrt{\ln 2}\;\Delta\nu_{1/e} = 0.833\,\Delta\nu_{1/e} \qquad \text{(A.2-18)}$$

   La gaussiana describe también el espectro de ciertas emisiones (Sec. 13.3D) y la distribución
   espacial de haces de luz (Sec. 3.1) [p. 1128].

#### Resumen de constantes duración × ancho de banda (derivadas de A.2)

| Función $f(t)$ | Medida temporal | Medida espectral | Producto |
|---|---|---|---|
| Gaussiana $\exp(-t^2/4\sigma_t^2)$ | $\sigma_t$ (RMS de potencia) | $\sigma_\nu = 1/4\pi\sigma_t$ | $\sigma_t\sigma_\nu = 1/4\pi$ (mínimo); $\sigma_t\sigma_\omega = 1/2$ |
| Gaussiana $\exp(-t^2/2\sigma_t^2)$ | $\sigma_t$ (RMS de $f$) | $\sigma_\nu = 1/2\pi\sigma_t$ | $\sigma_t\sigma_\nu = 1/2\pi$ |
| Gaussiana $\exp(-t^2/2\tau^2)$ | $\Delta t_{1/e} = 2\sqrt2\,\tau$ | $\Delta\nu_{1/e} = \sqrt2/\pi\tau$; $\Delta\nu_{\rm FWHM} = \sqrt{2\ln2}/\pi\tau$ | $\Delta t_{1/e}\Delta\nu_{1/e} = 4/\pi$ |
| Exponencial un lado $\exp(-t/\tau)$ | $\Delta t_{1/e} = \tau$ | $\Delta\nu_{3\text{-dB}} = 1/2\pi\tau$; $B = 1/4\tau$ | $\tau\,\Delta\nu_{3\text{-dB}} = 1/2\pi$; $\tau B = 1/4$ |
| Exponencial dos lados $\exp(-\lvert t\rvert/\tau)$ (↔ lorentziana) | $\Delta t_{1/e} = \tau$; ancho eq. potencia $\tau$ | $\Delta\nu_{\rm FWHM} = 1/\pi\tau$ | $\tau\,\Delta\nu_{\rm FWHM} = 1/\pi$ |
| Cualquiera, $B$ y $T$ de (A.2-10), (A.2-13) | $T$ | $B$ | $BT = 1/2$ |

(Los productos de la última columna los calculé yo a partir de las fórmulas del libro; las fórmulas
individuales son textuales.) Para la gaussiana en FWHM temporal, usando $\Delta t_{\rm FWHM} = 2\sqrt{2\ln2}\,\tau$
y (A.2-17): $\Delta t_{\rm FWHM}\Delta\nu_{\rm FWHM} = 4\ln2/\pi \approx 0.441$, el valor clásico de
los pulsos gaussianos "limitados por transformada" (este número no aparece en el libro; lo derivo).

### A.3 Transformada de Fourier bidimensional [pp. 1128–1130]

Función de dos variables $f(x,y)$; si $x, y$ son coordenadas de un punto en el plano, $f(x,y)$ es un
patrón espacial (p. ej. el campo óptico en un plano). La armónica
$F\exp[-j2\pi(\nu_x x + \nu_y y)]$ es el bloque de construcción; $\nu_x$, $\nu_y$ son las
**frecuencias espaciales** en $x$ y $y$. Como $x, y$ están en mm, $\nu_x, \nu_y$ están en ciclos/mm o
líneas/mm [p. 1128]. La Fig. A.3-1 muestra la parte real
$|F|\cos[2\pi\nu_x x + 2\pi\nu_y y + \arg\{F\}]$ para (a) $\nu_x = 0$, (b) $\nu_y = 0$, (c) caso
arbitrario (franjas horizontales, verticales e inclinadas; $\arg\{F\} = 0$) [p. 1129].

$$f(x,y) = \iint_{-\infty}^{\infty} F(\nu_x,\nu_y)\exp[-j2\pi(\nu_x x + \nu_y y)]\,d\nu_x\,d\nu_y \qquad \text{(A.3-1) TF inversa [recuadro]}$$

$$F(\nu_x,\nu_y) = \iint_{-\infty}^{\infty} f(x,y)\exp[j2\pi(\nu_x x + \nu_y y)]\,dx\,dy \qquad \text{(A.3-2) TF [recuadro]}$$

**Signo opuesto respecto al caso temporal.** (A.3-2) y (A.1-2) difieren en el signo del exponente. La
elección es arbitraria mientras directa e inversa tengan signos opuestos. En el libro,
$\exp(j2\pi\nu t)$ tiene frecuencia temporal positiva, mientras que
$\exp[-j2\pi(\nu_x x + \nu_y y)]$ tiene frecuencias espaciales positivas. Se eligen signos distintos
para simplificar la notación del Cap. 4 (óptica de Fourier), donde la onda viajera
$\exp(+j2\pi\nu t)\exp[-j(k_x x + k_y y + k_z z)]$ tiene dependencias temporal y espacial de signos
opuestos [p. 1129].

#### Propiedades [pp. 1129–1130]

- **Teorema de convolución.** Si $f(x,y)$ es la convolución 2D de $f_1$ y $f_2$ (con TF $F_1$, $F_2$),

  $$f(x,y) = \iint_{-\infty}^{\infty} f_1(x',y')\,f_2(x-x',y-y')\,dx'\,dy' \qquad \text{(A.3-3)}$$

  entonces

  $$F(\nu_x,\nu_y) = F_1(\nu_x,\nu_y)\,F_2(\nu_x,\nu_y) \qquad \text{(A.3-4)}$$

  Convolución en el espacio ⇔ multiplicación en Fourier.
- **Funciones separables.** Si $f(x,y) = f_x(x)f_y(y)$, su TF 2D es producto de una función de
  $\nu_x$ y otra de $\nu_y$, relacionada con las TF 1D por
  $F(\nu_x,\nu_y) = F_x(-\nu_x)\,F_y(-\nu_y)$ (el signo menos viene del cambio de convención). Ejemplos:
  TF de $\delta(x-x_0)\delta(y-y_0)$ (impulso en $(x_0,y_0)$) es la armónica
  $\exp[j2\pi(\nu_x x_0 + \nu_y y_0)]$; TF de la gaussiana $\exp[-\pi(x^2+y^2)]$ es la gaussiana
  $\exp[-\pi(\nu_x^2+\nu_y^2)]$ [p. 1130].
- **Funciones con simetría circular.** La TF de una función circularmente simétrica también lo es.
  Ejemplo: la **función circ**

  $$f(x,y) = \begin{cases} 1, & \sqrt{x^2+y^2} \le 1 \\ 0, & \text{en otro caso} \end{cases} \qquad \text{(A.3-5)}$$

  denotada $\mathrm{circ}(x,y)$, tiene TF

  $$F(\nu_x,\nu_y) = \frac{J_1(2\pi\nu_\rho)}{\nu_\rho}, \qquad \nu_\rho = \sqrt{\nu_x^2+\nu_y^2} \qquad \text{(A.3-6)}$$

  con $J_1$ la función de Bessel de orden 1. La Fig. A.3-2 muestra (a) el cilindro circ de radio 1 y
  altura 1 y (b) su TF, un "sombrero" con el primer cero en $\nu_\rho = 0.61$ [p. 1130].

### Lista de lecturas del Apéndice A [p. 1131]

- E. Kamen, *Introduction to Signals and Systems*, Macmillan, 1987, 2.ª ed. 1990.
- A. Gabel y R. A. Roberts, *Signals and Linear Systems*, Wiley, 1973, 3.ª ed. 1987.
- C. D. McGillem y G. R. Cooper, *Continuous and Discrete Signal and System Analysis*, Oxford
  University Press, 3.ª ed. 1991.
- A. V. Oppenheim, A. S. Willsky y S. H. Nawab, *Signals and Systems*, Prentice Hall, 1983, 2.ª ed. 1997.
- R. N. Bracewell, *The Fourier Transform and Its Applications*, McGraw-Hill, 3.ª ed. 2000.
- J. D. Gaskill, *Linear Systems, Fourier Transforms, and Optics*, Wiley, 1978.
- L. E. Franks, *Signal Theory*, Prentice Hall, 1969, ed. revisada 1981.
- A. Papoulis, *Systems and Transforms with Applications in Optics*, McGraw-Hill, 1968; Krieger,
  reedición 1986.
- A. Papoulis, *The Fourier Integral and Its Applications*, McGraw-Hill, 1962, reimpreso 1987.

---

## Apéndice B — Sistemas lineales

Revisión de las características básicas de sistemas lineales uni- y bidimensionales [p. 1132].

### B.1 Sistemas lineales unidimensionales [pp. 1132–1135]

Sistema con entrada $f_1(t)$ y salida $f_2(t)$ (p. ej. un oscilador armónico forzado por $f_1(t)$ que
responde con un desplazamiento $f_2(t)$). La regla que relaciona salida con entrada puede ser una
ecuación diferencial, una transformada integral o una operación simple como $f_2(t) = \log f_1(t)$
[p. 1132].

**Sistemas lineales.** Un sistema es *lineal* si cumple superposición: la respuesta a la suma de dos
entradas es la suma de las respuestas. La salida en $t$ es una superposición ponderada de las
contribuciones de la entrada en distintos instantes $\tau$:

$$f_2(t) = \int_{-\infty}^{\infty} h(t;\tau)\,f_1(\tau)\,d\tau \qquad \text{(B.1-1)}$$

$h(t;\tau)$ pondera la contribución de la entrada en $\tau$ a la salida en $t$. Si
$f_1(t) = \delta(t-\tau)$, (B.1-1) da $f_2(t) = h(t;\tau)$: $h(t;\tau)$ es la **función de respuesta
impulsiva** (también **función de Green**) [p. 1132].

**Sistemas lineales invariantes al desplazamiento.** Un sistema lineal es **invariante en el tiempo**
o **invariante al desplazamiento** si al desplazar la entrada en el tiempo, la salida se desplaza
igual sin cambiar. Entonces $h(t;\tau) = h(t-\tau)$ y (B.1-1) se vuelve

$$f_2(t) = \int_{-\infty}^{\infty} h(t-\tau)\,f_1(\tau)\,d\tau \qquad \text{(B.1-2) [recuadro]}$$

La salida es la **convolución** de la entrada con $h(t)$ [ver (A.1-4)]. Si $f_1 = \delta(t)$,
$f_2 = h(t)$; si $f_1 = \delta(t-\tau)$, $f_2 = h(t-\tau)$ (Fig. B.1-1: dos impulsos en $0$ y $\tau$
producen dos réplicas de $h$ desplazadas) [pp. 1132–1133].

**Función de transferencia** [p. 1133]. Por el teorema de convolución, las TF $F_1(\nu)$, $F_2(\nu)$
y $H(\nu)$ de $f_1$, $f_2$ y $h$ cumplen

$$F_2(\nu) = H(\nu)\,F_1(\nu) \qquad \text{(B.1-3) [recuadro]}$$

Si la entrada es la armónica $F_1(\nu)\exp(j2\pi\nu t)$, la salida $H(\nu)F_1(\nu)\exp(j2\pi\nu t)$
es armónica de la misma frecuencia con amplitud compleja modificada (Fig. B.1-2). $H(\nu)$ es la
**función de transferencia** del sistema = TF de la respuesta impulsiva. (B.1-3) es la clave de los
métodos de Fourier: descomponer la entrada en armónicas, multiplicar cada amplitud por $H$ a su
frecuencia y superponer.

**Ejemplos** [p. 1133]:
- *Sistema ideal*: $H(\nu) = 1$, $h(t) = \delta(t)$; la salida es réplica de la entrada.
- *Sistema ideal con retardo*: $H(\nu) = \exp(-j2\pi\nu\tau)$, $h(t) = \delta(t-\tau)$; réplica
  retardada $\tau$.
- *Sistema con respuesta exponencial*: $H(\nu) = \tau/(1+j2\pi\nu\tau)$, $h(t) = e^{-t/\tau}$ para
  $t \ge 0$ y $0$ en otro caso; sistema descrito por una ecuación diferencial lineal de primer orden
  (circuito $R$-$C$ con constante de tiempo $\tau$). Un impulso produce una respuesta que decae
  exponencialmente.
- *Sistema con chirp*: $H(\nu) = \exp(-j\pi\nu^2)$, $h(t) = e^{-j\pi/4}\exp(j\pi t^2)$; el sistema
  impone un desfase proporcional a $\nu^2$. Un impulso de entrada genera una señal con chirp: armónica
  cuya frecuencia instantánea (derivada de la fase) crece linealmente con el tiempo. **Describe la
  propagación de pulsos ópticos en medios con velocidad de fase dependiente de la frecuencia
  (Sec. 5.6)** y los cambios de la distribución espacial de ondas en propagación libre (Sec. 4.1C).

**Sistemas lineales invariantes causales** [pp. 1133–1134]. $h(t)$ de un sistema *causal* debe
anularse para $t < 0$ (la respuesta no empieza antes de la entrada). $h(t)$ no es simétrica y $H(\nu)$
debe ser compleja. Puede demostrarse (ref.: L. E. Franks, *Signal Theory*, 1969/1981) que si
$h(t) = 0$ para $t < 0$, las partes real $H'(\nu)$ e imaginaria $H''(\nu)$ de $H(\nu)$ cumplen

$$H'(\nu) = \frac{1}{\pi}\int_{-\infty}^{\infty}\frac{H''(s)}{s-\nu}\,ds \qquad \text{(B.1-4) [recuadro]}$$

$$H''(\nu) = \frac{1}{\pi}\int_{-\infty}^{\infty}\frac{H'(s)}{\nu-s}\,ds \qquad \text{(B.1-5) Transformada de Hilbert [recuadro]}$$

donde las integrales son valores principales de Cauchy:

$$\int_{-\infty}^{\infty} \equiv \lim_{\Delta\to0}\left(\int_{-\infty}^{\nu-\Delta} + \int_{\nu+\Delta}^{\infty}\right), \quad \Delta > 0$$

Funciones que cumplen (B.1-4)–(B.1-5) forman un **par de transformadas de Hilbert**; $H''$ es la
transformada de Hilbert de $H'$ [p. 1134].

Si además $h(t)$ es real, $H(-\nu) = H^*(\nu)$: $H'$ es par y $H''$ impar. Las integrales se
reescriben sobre $(0,\infty)$ y resultan las **relaciones de Kramers–Kronig**:

$$H'(\nu) = \frac{2}{\pi}\int_{0}^{\infty}\frac{s\,H''(s)}{s^2-\nu^2}\,ds \qquad \text{(B.1-6) [recuadro]}$$

$$H''(\nu) = \frac{2}{\pi}\int_{0}^{\infty}\frac{\nu\,H'(s)}{\nu^2-s^2}\,ds \qquad \text{(B.1-7) Relaciones de Kramers–Kronig [recuadro]}$$

Resumen: Hilbert / Kramers–Kronig relacionan parte real e imaginaria de la función de transferencia de
un sistema lineal, invariante y causal: conocida una a todas las frecuencias, se determina la otra
[p. 1134].

**Ejemplo: el oscilador armónico** [pp. 1134–1135]. El sistema

$$\left(\frac{d^2}{dt^2} + \sigma\frac{d}{dt} + \omega_0^2\right)f_2(t) = f_1(t) \qquad \text{(B.1-8)}$$

describe un oscilador con desplazamiento $f_2(t)$ bajo fuerza $f_1(t)$; $\omega_0$ = frecuencia angular
de resonancia, $\sigma$ = coeficiente de amortiguamiento. Sustituyendo $f_1 = \exp(j2\pi\nu t)$ y
$f_2 = H(\nu)\exp(j2\pi\nu t)$:

$$H(\nu) = \frac{1}{(2\pi)^2}\,\frac{1}{\nu_0^2 - \nu^2 + j\nu\Delta\nu} \qquad \text{(B.1-9)}$$

con $\nu_0 = \omega_0/2\pi$ (frecuencia de resonancia) y $\Delta\nu = \sigma/2\pi$. Partes real e
imaginaria:

$$H'(\nu) = \frac{1}{(2\pi)^2}\,\frac{\nu_0^2-\nu^2}{(\nu_0^2-\nu^2)^2 + (\nu\Delta\nu)^2} \qquad \text{(B.1-10)}$$

$$H''(\nu) = -\frac{1}{(2\pi)^2}\,\frac{\nu\Delta\nu}{(\nu_0^2-\nu^2)^2 + (\nu\Delta\nu)^2} \qquad \text{(B.1-11)}$$

Como el sistema es causal, $H'$ y $H''$ cumplen Kramers–Kronig. Si $\nu_0 \gg \Delta\nu$, son
funciones estrechas centradas en $\nu_0$; para $\nu \approx \nu_0$,
$(\nu_0^2-\nu^2) \approx 2\nu_0(\nu_0-\nu)$ y

$$H''(\nu) = -\frac{1}{(2\pi)^2}\,\frac{\Delta\nu/4\nu_0}{(\nu_0-\nu)^2 + (\Delta\nu/2)^2} \qquad \text{(B.1-12)}$$

$$H'(\nu) = 2\,\frac{\nu-\nu_0}{\Delta\nu}\,H''(\nu) \qquad \text{(B.1-13)}$$

La función de transferencia del oscilador armónico se usa en los Caps. 5 y 14 para describir medios
dieléctricos y sistemas atómicos. (B.1-12) tiene **forma lorentziana** [p. 1135].

### B.2 Sistemas lineales bidimensionales [pp. 1135–1136]

Un sistema 2D relaciona $f_1(x,y)$ (entrada) con $f_2(x,y)$ (salida); p. ej., campos ópticos en dos
planos paralelos, con el espacio libre y los componentes ópticos entre ellos como "sistema". Para un
sistema *lineal*:

$$f_2(x,y) = \iint_{-\infty}^{\infty} h(x,y;x',y')\,f_1(x',y')\,dx'\,dy' \qquad \text{(B.2-1)}$$

$h(x,y;x',y')$ = efecto de la entrada en $(x',y')$ sobre la salida en $(x,y)$: **función de respuesta
impulsiva** (también **point-spread function**, PSF) [p. 1135].

El sistema es **invariante al desplazamiento** (o **isoplanático**) si desplazar la entrada desplaza
la salida igual, sin alterarla (Fig. B.2-1: dos puntos → dos manchas iguales). Entonces
$h(x,y;x',y') = h(x-x',y-y')$ y (B.2-1) es la convolución 2D:

$$f_2(x,y) = \iint_{-\infty}^{\infty} h(x-x',y-y')\,f_1(x',y')\,dx'\,dy' \qquad \text{(B.2-2) [recuadro]}$$

Con el teorema de convolución 2D (A.3):

$$F_2(\nu_x,\nu_y) = H(\nu_x,\nu_y)\,F_1(\nu_x,\nu_y) \qquad \text{(B.2-3) [recuadro]}$$

donde $F_2$, $H$, $F_1$ son las TF de $f_2$, $h$, $f_1$. Una entrada armónica de amplitud $F_1$
produce una salida armónica de la misma frecuencia espacial con amplitud $H F_1$ (Fig. B.2-2:
$e^{-j2\pi(\nu_x x+\nu_y y)} \to H(\nu_x,\nu_y)e^{-j2\pi(\nu_x x+\nu_y y)}$). $H(\nu_x,\nu_y)$ es la
**función de transferencia** = TF de la respuesta impulsiva. Cualquiera de las dos caracteriza
completamente el sistema [p. 1136].

Ejemplo: $h(x,y) = \mathrm{circ}(x/\rho_s, y/\rho_s)$ difumina cada punto de la entrada en un disco
de radio $\rho_s$; su función de transferencia es $H(\nu_x,\nu_y) = \rho_s J_1(2\pi\rho_s\nu_\rho)/\nu_\rho$
con $\nu_\rho = (\nu_x^2+\nu_y^2)^{1/2}$ (forma de la Fig. A.3-2). El sistema atenúa severamente las
frecuencias espaciales mayores que $0.61/\rho_s$ líneas/mm [p. 1136].

### Lista de lecturas del Apéndice B [p. 1136]

"Ver la lista de lecturas del Apéndice A."

---

## Apéndice C — Modos de sistemas lineales [pp. 1137–1141]

Panorama de los modos de un sistema lineal descrito explícitamente por una relación entrada-salida
(matriz u operador integral) o implícitamente por una ecuación diferencial parcial lineal [p. 1137].

### Definición general [p. 1137]

Sistema lineal con operador $\mathcal{L}$ que actúa sobre un vector de entrada $\mathbf{X}$:

$$\mathbf{Y} = \mathcal{L}\mathbf{X} \qquad \text{(C.1-1)}$$

$\mathbf{X}$ puede ser un arreglo de números complejos (matriz columna) o una función compleja de una
o varias variables. Los **modos** son las entradas especiales que no se alteran (salvo una constante
multiplicativa) al pasar por el sistema:

$$\mathcal{L}\mathbf{X}_q = \lambda_q\mathbf{X}_q \qquad \text{(C.1-2) Problema de autovalores}$$

$q$ indexa el modo; $\mathbf{X}_q$ es un **autovector** (eigenvector); $\lambda_q$, el **autovalor**,
es en general complejo. (C.1-2) es el **problema de autovalores**.

Tres casos:
1. Sistema con relación entrada-salida explícita (arriba).
2. Sistema dinámico lineal con estado $\mathbf{X}(t)$ de $N$ variables: la evolución de cada variable
   depende de todas; en nuevas coordenadas las $N$ variables evolucionan independientemente, y el
   sistema se descompone en $N$ sistemas 1D independientes. Esas variables desacopladas son los modos.
3. Sistema descrito implícitamente por una EDP lineal que se escribe como (C.1-2) con $\mathcal{L}$
   un operador diferencial y $\mathbf{X}$ una función compleja: los modos son soluciones de la
   ecuación diferencial y los autovectores se llaman **autofunciones** (eigenfunctions). Entrada y
   salida no tienen sentido aquí.

**Conceptos de álgebra lineal** [p. 1137]. A cada par $\mathbf{X},\mathbf{Y}$ se asocia un escalar
complejo $(\mathbf{X},\mathbf{Y})$, el **producto interno**. $\sqrt{(\mathbf{X},\mathbf{X})}$ es la
**norma** ("longitud"). El producto interno de dos vectores de norma unidad es el "coseno del ángulo"
entre ellos; son **ortogonales** si el producto interno es cero. Para arreglos $\{X_i\}$, $\{Y_i\}$,
$i = 1,\dots,N$: $(\mathbf{X},\mathbf{Y}) = \sum_{i=1}^N X_i^* Y_i$. Para funciones $X(t)$, $Y(t)$:
$(\mathbf{X},\mathbf{Y}) = \int_{-\infty}^{\infty} X(t)^* Y(t)\,dt$ (en el escaneo aparece un "$=$"
sobrante entre la integral y el integrando, errata tipográfica del libro).

**Dos clases de operadores con propiedades especiales** [p. 1138]:
- **Operadores hermíticos.** $(\mathbf{X},\mathcal{L}\mathbf{Y}) = (\mathcal{L}\mathbf{X},\mathbf{Y})$.
  Sus autovalores son **reales** y sus autovectores **ortogonales**. Obedecen el **principio
  variacional**, basado en la energía variacional
  $E_v = \tfrac{1}{2}(\mathbf{X},\mathcal{L}\mathbf{X})/(\mathbf{X},\mathbf{X})$: el autovector
  $\mathbf{X}_1$ de menor autovalor minimiza $E_v$; $\mathbf{X}_2$ (siguiente autovalor) minimiza
  $E_v$ sujeto a ser ortogonal a $\mathbf{X}_1$, y así sucesivamente.
- **Operadores unitarios.** Describen sistemas físicos pasivos y sin pérdidas; conservan la norma:
  $(\mathcal{L}\mathbf{X},\mathcal{L}\mathbf{X}) = (\mathbf{X},\mathbf{X})$ (ejemplo: una rotación).
  Sus autovalores son unimodulares, $|\lambda_q| = 1$: fase pura.

### 1) Modos de un sistema lineal discreto [pp. 1138–1139]

$\mathbf{Y} = \mathbf{M}\mathbf{X}$, con $\mathbf{X} = (X_1,\dots,X_N)$ columna, $\mathbf{M}$ matriz
$N\times N$. Los modos son los vectores de entrada que permanecen paralelos a sí mismos:

$$\mathbf{M}\mathbf{X}_q = \lambda_q\mathbf{X}_q \qquad \text{(C.1-3)}$$

Los modos son los autovectores de $\mathbf{M}$ y los $\lambda_q$ se obtienen de
$\det(\mathbf{M}-\lambda\mathbf{I}) = 0$. Hay $N$ modos, $q = 1,\dots,N$.

**Sistemas binarios ($N = 2$)**, muy importantes en óptica: matriz $2\times2$ con elementos
$A, B, C, D$:

$$\begin{bmatrix} Y_1 \\ Y_2 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix}\begin{bmatrix} X_1 \\ X_2 \end{bmatrix}$$

Autovalores de $(A-\lambda)(D-\lambda) - BC = 0$ → $\lambda_1$, $\lambda_2$ [p. 1138].

Aplicaciones:
- **Óptica matricial de polarización** (Sec. 6.1B): $(X_1,X_2)$ = componentes del campo eléctrico de
  entrada en dos direcciones ortogonales (vector de Jones); $(Y_1,Y_2)$ = salida; $\mathbf{M}$ =
  matriz de Jones. Los modos son los **estados de polarización que se conservan** al atravesar el
  sistema [p. 1138].
- **Óptica matricial de rayos** (Sec. 1.4): $(X_1,X_2)$ = posición y ángulo de un rayo; $\mathbf{M}$ =
  matriz $ABCD$. En un sistema cerrado (resonador) los modos son posiciones y ángulos que se
  autorreproducen tras una vuelta, i.e. quedan confinados [p. 1138].
- **Óptica matricial multicapa** (Sec. 7.1A): ondas hacia adelante y hacia atrás en cada plano,
  $\mathbf{X} = (X_1,X_2)$; el conjunto de fronteras se describe por una matriz de transmisión
  $\mathbf{M}$. Los modos se autorreproducen; si el sistema se replica periódicamente (cristales
  fotónicos 1D, Sec. 7.2), los modos de propagación son los modos de $\mathbf{M}$ [p. 1139].

### 2) Modos de un sistema continuo descrito por un operador integral [pp. 1139–1140]

Función de tiempo $f(t)$ (pulso óptico o campo de banda ancha) a través de un sistema lineal invariante
(filtro óptico):

$$g(t) = \int_{-\infty}^{\infty} h(t-\tau)\,f(\tau)\,d\tau \qquad \text{(C.1-4)}$$

$\mathbf{X}, \mathbf{Y}$ son $f(t)$ y $g(t)$; $\mathcal{L}$ es un operador integral. Los modos son las
**armónicas** $\exp(j2\pi\nu t)$: la entrada $\exp(j2\pi\nu t)$ genera $H(\nu)\exp(j2\pi\nu t)$,
con $H(\nu)$ la TF de $h(t)$. Hay un **continuo de modos** con autovalores continuos $H(\nu)$; el
índice $q$ es la frecuencia $\nu$ [p. 1139].

Sistema 2D invariante (B.2-1):

$$g(x,y) = \iint_{-\infty}^{\infty} h(x-x',y-y')\,f(x',y')\,dx'\,dy' \qquad \text{(C.1-5)}$$

Autofunciones: armónicas 2D $\exp[j2\pi(\nu_x x + \nu_y y)]$; autovalores $H(\nu_x,\nu_y)$ (TF 2D de
$h$). Continuo de autofunciones indexado por $(\nu_x,\nu_y)$ [p. 1139].

**Simetría traslacional y modos armónicos.** No sorprende que las armónicas sean los automodos de un
sistema invariante al desplazamiento: la armónica es invariante a traslaciones temporales (sigue
siendo armónica), por eso es autofunción del sistema invariante (estacionario). Igualmente las
armónicas 2D, invariantes a traslación en el plano, son autofunciones de un sistema invariante en el
espacio (homogéneo) [p. 1139].

Si el sistema **no** es invariante en el espacio (sin simetría traslacional), en 2D:

$$g(x,y) = \iint_{-\infty}^{\infty} h(x,y;x',y')\,f(x',y')\,dx'\,dy' \qquad \text{(C.1-6)}$$

Las autofunciones no son necesariamente armónicas; se obtienen resolviendo (C.1-2) como ecuación
integral:

$$\iint_{-\infty}^{\infty} h(x,y;x',y')\,f_q(x',y')\,dx'\,dy' = \lambda_q f_q(x,y), \qquad q = 1,2,\dots \qquad \text{(C.1-7)}$$

$f_q(x,y)$ y $\lambda_q$ son las autofunciones y autovalores; $q$ indexa un conjunto **discreto** de
modos [pp. 1139–1140].

**Aplicación: modos de un resonador óptico** (Sec. 10.2E) [p. 1140]. Luz entre dos espejos paralelos
de un resonador láser: la distribución transversal al inicio y al final de una vuelta son entrada y
salida. Los modos del resonador son las distribuciones que mantienen su forma tras una vuelta. El
núcleo $h(x,y;x',y')$ en (C.1-7) representa propagación libre + reflexión en el primer espejo +
propagación de regreso + reflexión en el segundo. Espejos curvos o finitos hacen el sistema
*variante* al desplazamiento. Si los espejos son esféricos y modulan la luz con una fase cuadrática en
la distancia radial, los modos son funciones **Hermite–Gauss** de $x$ y $y$. Con aperturas, (C.1-7)
solo se resuelve numéricamente.

### 3) Modos de un sistema descrito por ecuaciones diferenciales ordinarias [p. 1140]

$N$ osciladores acoplados (figura: tres masas unidas por resortes, $X_1, X_2, X_3$):

$$\ddot{\mathbf{X}} = -\mathbf{M}\mathbf{X} \qquad \text{(C.1-8)}$$

$\mathbf{X} = (X_1,\dots,X_N)$, $\ddot{\mathbf{X}} = d^2\mathbf{X}/dt^2$, $\mathbf{M}$ matriz $N\times N$
con coeficientes independientes del tiempo (sistema invariante). La invariancia temporal exige modos
armónicos $\exp(j\omega t)$: $\mathbf{X}(t) = \mathbf{X}(0)\exp(j\omega t)$. Sustituyendo:

$$\mathbf{M}\mathbf{X} = \omega^2\mathbf{X} \qquad \text{(C.1-9)}$$

Problema de autovalores discreto: los autovalores dan las frecuencias de resonancia
$\omega_1,\dots,\omega_N$ y los autovectores son los **modos normales**. Todas las componentes de
$\mathbf{X}_q$ oscilan a la misma $\omega_q$ sin alterar sus amplitudes ni fases relativas: los modos
son soluciones estacionarias desacopladas entre sí.

### 4) Modos de un sistema descrito por una ecuación diferencial parcial [pp. 1140–1141]

Campos y ondas se describen por EDP: ecuaciones de Maxwell (campos E y H en un dieléctrico) y
ecuación de Schrödinger (función de onda en un potencial). Si el sistema es estacionario (medio y
potencial independientes del tiempo), cada modo es armónico en el tiempo, $\exp(j\omega t)$, y la
ecuación de onda se convierte en la **ecuación de Helmholtz generalizada**:

$$\nabla\times[\eta(\mathbf{r})\,\nabla\times\mathbf{H}] = \frac{\omega^2}{c_o^2}\,\mathbf{H} \qquad \text{(C.1-10)}$$

con $\eta(\mathbf{r}) = \epsilon_o/\epsilon(\mathbf{r})$ la **impermeabilidad eléctrica** [ver (7.0-2)].
Schrödinger da la ecuación independiente del tiempo:

$$\left[-\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r})\right]\psi(\mathbf{r}) = E\psi(\mathbf{r}) \qquad \text{(C.1-11)}$$

con $E = \hbar\omega$ y $V(\mathbf{r})$ el potencial [ver (13.1-3)]. Ambas tienen la forma (C.1-2)
con $\mathcal{L}$ un operador diferencial **hermítico** caracterizado por $\eta(\mathbf{r})$ o
$V(\mathbf{r})$. Los autovalores (reales) dan las frecuencias $\omega_q$ (y las energías $E_q$ en
Schrödinger); las autofunciones son las distribuciones espaciales de los campos (o funciones de onda).
El campo del modo $q$ evoluciona como $\exp(j\omega_q t)$ en todas las posiciones: cada modo es
estacionario [p. 1141].

**Modos en un medio homogéneo con condiciones de frontera** [p. 1141].
- Si $\eta(\mathbf{r})$ es constante, el sistema es invariante al desplazamiento y los modos deben
  ser armónicas de la posición: **ondas planas**. Igual con $V(\mathbf{r})$ constante: funciones de
  onda planas (la partícula es igualmente probable en todas partes).
- Si $\eta$ o $V$ son constantes dentro de una región finita con frontera que impone condiciones:
  modos de una **cavidad** con paredes perfectamente conductoras (campo eléctrico paralelo nulo en la
  superficie). Para un resonador rectangular, los modos son armónicas de la posición — **ondas
  estacionarias** oscilando al unísono (Sec. 10.3C). Análogamente, partícula en una caja cuántica
  (punto cuántico): la función de onda se anula en las fronteras (Sec. 16.1G).
- Medio homogéneo acotado en una sola dirección (dos espejos planos paralelos): las condiciones de
  frontera dan un conjunto discreto de ondas estacionarias en la dirección ortogonal a los espejos
  (transversal) y ondas viajeras en la dirección paralela (axial). Los modos viajan en esta **guía de
  onda óptica** como armónicas en la dirección axial sin alterar su distribución transversal
  (Sec. 8.1). Si $\beta_q$ es la **constante de propagación** del modo $q$, el autovalor es el factor
  de fase $\exp(-j\beta_q z)$.

**Modos en un medio periódico** [p. 1141]. Los modos están dictados por la distribución espacial del
medio, $\eta(\mathbf{r})$ o $V(\mathbf{r})$. Si es constante, los modos son invariantes a cualquier
traslación; si es periódica, invariantes a traslaciones por un periodo → los modos son **ondas de
Bloch** (Sec. 7.2A). Ejemplo: medio homogéneo en $x, y$ y periódico en $z$: el modo de Bloch es la
armónica $\exp(-jKz)$ modulada por una onda estacionaria periódica $p_K(z)$ con el periodo del medio;
la dependencia en $x, y$ es armónica. Para cada $K$, las frecuencias y las formas $p_K(z)$ dependen de
la función periódica. Esta simetría produce un espectro de autovalores (frecuencias $\omega$ o
energías $E = \hbar\omega$) en forma de **bandas separadas por bandas prohibidas** (bandgaps) sin
modos permitidos: estructura de bandas de los sólidos para un electrón en potencial periódico
(Sec. 13.1C) y **bandas fotónicas** en un cristal fotónico (Secs. 7.2 y 7.3).

---

## Símbolos y unidades [pp. 1142–1158]

Transcripción completa de la lista del libro, en tres partes: símbolos romanos y acrónimos
(pp. 1142–1154), símbolos griegos (pp. 1154–1158) y símbolos matemáticos (p. 1158). El libro **no**
indica la sección donde se define cada símbolo (solo símbolo, significado y unidad entre corchetes);
tampoco incluye tabla de prefijos SI ni de constantes físicas en estas páginas. Donde los apéndices
A–C definen el símbolo, lo anoto entre paréntesis.

Tipografía del libro: el mismo símbolo aparece en varias fuentes con significados distintos (itálica,
negrita, sans-serif, caligráfica $\mathcal{A}$, gótica/Fraktur $\mathfrak{A}$, doble trazo $\mathbb{A}$,
redonda). Aquí indico la fuente cuando no es la itálica normal: (sans), (neg) = negrita,
(cal) = caligráfica, (frak) = Fraktur, (bb) = doble trazo, (red) = redonda.

### Símbolos romanos y acrónimos

**A** [p. 1142]
- $a$ = Radio de una apertura o fibra [m]; también, Radio de un círculo [m]; también, Constante de red [m]; también, Parámetro de chirp de un pulso óptico
- $a$ (red) = Amplitud (magnitud) de una onda óptica; también, Amplitud compleja normalizada de un campo óptico ($|a|^2$ = densidad de flujo de fotones)
- $a$ (sans) = Amplitud compleja normalizada de un campo óptico en una cavidad ($|a|^2$ = número de fotones)
- $a$ (red, otra fuente) = Aceleración de un portador [m·s⁻²]
- $A$ = Envolvente compleja de una onda plana monocromática; también, Amplitud de un pulso
- $A(\mathbf{r})$ = Envolvente compleja de una onda monocromática
- $A(\nu)$ = Transformada de Fourier de la envolvente compleja de un pulso óptico
- $\mathbf{A}$ (neg) = Envolvente vectorial compleja de una onda plana monocromática; también, Potencial vectorial [V·s·m⁻¹]
- $\mathcal{A}(\mathbf{r},t)$ = Envolvente compleja de una onda policromática (p. ej. pulsada)
- $\mathcal{A}(t)$ = Envolvente compleja de un pulso óptico
- $A$ (sans) = Área [m²]; también, Elemento de la matriz de transferencia de rayos $ABCD$; también, Elemento de la matriz de transferencia de ondas $ABCD$
- $A_c$ (sans) = Área de coherencia [m²]
- $\mathbb{A}$ = Coeficiente A de Einstein [s⁻¹]
- AC = Corriente alterna
- ADM = Multiplexor add-drop
- AM = Modulación de amplitud
- APD = Fotodiodo de avalancha
- ASE = Emisión espontánea amplificada
- AWG = Redes de guías de onda (arrayed waveguide gratings)

**B** [p. 1142]
- $b$ = Radio de un círculo [m]; también, Coeficiente de chirp [s²]
- $B$ = Amplitud compleja de la densidad de flujo magnético [Wb·m⁻²]; también, Ancho de banda [Hz] (definido en (A.2-10), p. 1127)
- $B_0$ = Tasa de bits [bits·s⁻¹]
- $\mathcal{B}$ = Densidad de flujo magnético [Wb·m⁻²]; también, Ancho espectral equivalente en potencia [Hz] (definido en (A.2-9), p. 1127; el libro usa la misma letra caligráfica para ambos significados)
- $B$ (sans) = Elemento de la matriz de transferencia de rayos $ABCD$; también, Elemento de la matriz de transferencia de ondas $ABCD$
- $\mathbb{B}$ = Coeficiente B de Einstein [m³·J⁻¹·s⁻²]
- BEC = Condensado de Bose–Einstein
- BER = Tasa de error de bit
- BGR = Reflector de red de Bragg
- BRF = Filtro birrefringente
- BSO = Óxido de bismuto y silicio

**C** [pp. 1142–1143]
- $c$ = Velocidad de la luz; Velocidad de fase [m·s⁻¹]
- $c_o$ = Velocidad de la luz en el vacío [m·s⁻¹]
- $C$ = Capacitancia eléctrica [F]
- $C(\cdot)$ = Integral de Fresnel
- $\mathcal{C}$ = Coeficiente de acoplamiento en un acoplador direccional [m⁻¹]
- $C$ (sans) = Elemento de la matriz $ABCD$ de rayos; también, Elemento de la matriz $ABCD$ de ondas
- CARS = Dispersión Raman anti-Stokes coherente
- CCD = Dispositivo de carga acoplada
- CD = Disco compacto
- CDM = Multiplexación por división de código
- CDMA = Acceso múltiple por división de código
- CLSM = Microscopía confocal de barrido láser
- CMOS = Metal-óxido-semiconductor complementario
- CW = Onda continua
- CWDM = Multiplexación por división de longitud de onda gruesa (coarse)

**D** [p. 1143]
- $d$ = Diferencial
- $d\mathbf{r}$ = Volumen incremental [m³]
- $ds$ = Longitud incremental [m]
- $\mathrm{d}$ (red) = Coeficiente de no linealidad óptica de segundo orden [C·V⁻²]
- $\mathrm{d}_{ijk}$ = Elemento del tensor de no linealidad óptica de segundo orden [C·V⁻²]
- $\mathrm{d}_{iJ}$ = Elemento del tensor de no linealidad de segundo orden (índices contraídos) [C·V⁻²]
- $\mathrm{d}(\omega_3;\omega_1,\omega_2)$ = Coeficiente de no linealidad óptica de segundo orden (medio dispersivo) [C·V⁻²]
- $d$ (sans) = Distancia, Longitud [m]
- $d_p$ (sans) = Profundidad de penetración [m]
- $d_{\rm pulse}$ (sans) = Longitud de un pulso óptico de modos bloqueados [m]
- $d_S$ (sans) = Longitud a lo largo de una dimensión pequeña [m]
- $D$ = Diámetro [m]; también, Amplitud compleja de la densidad de flujo eléctrico [C·m⁻²]
- $D_w$ = Coeficiente de dispersión de guía de onda [s·m⁻²]
- $D_x, D_y$ = Anchos laterales [m]
- $D_\lambda$ = Coeficiente de dispersión del material [s·m⁻²]
- $D_\nu$ = Coeficiente de dispersión del material [s²·m⁻¹]
- $\mathcal{D}$ = Densidad de flujo eléctrico [C·m⁻²]
- $D$ (sans) = Elemento de la matriz $ABCD$ de rayos; también, Elemento de la matriz $ABCD$ de ondas
- DBR = Reflector de Bragg distribuido
- DC = Corriente directa
- DCF = Fibra compensadora de dispersión
- DEMUX = Demultiplexor
- DFB = Retroalimentación distribuida
- DFF = Fibra de dispersión aplanada
- DGD = Retardo de grupo diferencial
- DH = Doble heteroestructura
- DKDP = Fosfato dihidrógeno de potasio deuterado
- DMUX = Demultiplexor
- DPSS = Estado sólido bombeado por diodo
- DRO = Oscilador doblemente resonante
- DSF = Fibra de dispersión desplazada
- DVD = Disco de video digital
- DWDM = Multiplexación por división de longitud de onda densa

**E** [p. 1144]
- $e$ = Magnitud de la carga del electrón [C]
- $\hat{\mathbf{e}}_x$ = Vector unitario en la dirección $x$
- $E$ = Amplitud compleja del campo eléctrico [V·m⁻¹]; también, Campo eléctrico estacionario o lentamente variable [V·m⁻¹]
- $\mathcal{E}$ = Campo eléctrico [V·m⁻¹]
- $E$ (sans) = Energía [J]
- $E_A$ (sans) = Nivel de energía aceptor [J]
- $E_c$ (sans) = Energía en el fondo de la banda de conducción [J]
- $E_D$ (sans) = Nivel de energía donor [J]
- $E_f$ (sans) = Energía de Fermi [J]
- $E_{fc}$ (sans) = Energía cuasi-Fermi de la banda de conducción [J]
- $E_{fv}$ (sans) = Energía cuasi-Fermi de la banda de valencia [J]
- $E_g$ (sans) = Energía de la banda prohibida (bandgap) [J]
- $E_v$ (sans) = Energía en el tope de la banda de valencia [J]
- $E_\nu$ (sans) = Densidad espectral de energía [J·Hz⁻¹]
- EDFA = Amplificador de fibra dopada con erbio
- EIT = Transparencia inducida electromagnéticamente
- E/O = Electrónico a óptico
- EUV = Ultravioleta extremo

**F** [p. 1144]
- $f$ = Distancia focal de una lente [m]; también, Frecuencia [Hz]
- $f(E)$ = Función de Fermi
- $f_a$ = Probabilidad de que se satisfaga la condición de absorción
- $f_c(E)$ = Función de Fermi de la banda de conducción
- $f_{\rm col}$ = Tasa de colisiones [s⁻¹]
- $f_e$ = Probabilidad de que se satisfaga la condición de emisión
- $f_g$ = Factor de inversión de Fermi
- $f_v(E)$ = Función de Fermi de la banda de valencia
- $\mathrm{f}$ (red) = Distancia focal [m]
- $f$ (sans) = Frecuencia del sonido [Hz]; también, Frecuencia de modulación [Hz]
- $F$ = Factor de exceso de ruido de un fotodiodo de avalancha
- $F_\#$ = Número $F$ de una lente
- $\mathcal{F}$ = Finura (finesse) de un resonador; también, Fuerza [kg·m·s⁻²]
- FBG = Red de Bragg en fibra
- FDM = Multiplexación por división de frecuencia
- FDMA = Acceso múltiple por división de frecuencia
- FET = Transistor de efecto de campo
- FEL = Láser de electrones libres
- FFT = Transformada rápida de Fourier
- FIR = Infrarrojo lejano
- FM = Modulado en frecuencia
- FON = Red de fibra óptica
- FPA = Arreglo en plano focal
- FROG = Frequency-resolved optical gating
- FSK = Modulación por desplazamiento de frecuencia
- FUV = Ultravioleta lejano
- FWHM = Ancho completo a mitad del máximo
- FWM = Mezcla de cuatro ondas

**G** [pp. 1144–1145]
- $g$ = Parámetro $g$ de un resonador
- $g(\mathbf{r}_1,\mathbf{r}_2)$ = Intensidad mutua normalizada
- $g(\mathbf{r}_1,\mathbf{r}_2,\tau)$ = Grado complejo de coherencia
- $g(\nu)$ = Función de forma de línea de una transición [Hz⁻¹]
- $g(\tau)$ = Grado complejo de coherencia temporal
- $g_0$ = Factor de ganancia
- $g_{\nu 0}(\nu)$ = Función de forma de línea ensanchada por colisiones electrón–fonón en un semiconductor [Hz⁻¹]
- $\mathrm{g}$ (red) = Coeficiente de acoplamiento en una interacción paramétrica [m⁻³]
- $g$ (sans) = Parámetro de degeneración
- $G$ = Ganancia de un amplificador; también, Ganancia de un fotodetector; también, Conductancia [Ω⁻¹]
- $G(\mathbf{r}_1,\mathbf{r}_2)$ = Intensidad mutua [W·m⁻²]
- $G(\mathbf{r}_1,\mathbf{r}_2,\tau)$ = Función de coherencia mutua [W·m⁻²]
- $G(\nu)$ = Ganancia de un amplificador óptico
- $G(\tau)$ = Función de coherencia temporal [W·m⁻²]
- $\mathbf{G}$ (neg) = Matriz de coherencia [W·m⁻²]; también, Vector de giración de un medio ópticamente activo
- $G$ (sans) = Tasa de fotoionización en un material fotorrefractivo [m⁻³·s⁻¹]
- $G_0$ (sans) = Tasa de generación térmica electrón–hueco en un semiconductor [m⁻³·s⁻¹]
- $\mathbf{G}$ (neg sans) = Vector de la red recíproca [m⁻¹]
- $\mathbb{G}_n(\cdot)$ = Funciones de Hermite–Gauss
- GR = Generación-recombinación
- GRIN = Índice gradual
- GVD = Dispersión de velocidad de grupo

**H** [p. 1145]
- $h$ = Factor complejo de atenuación de amplitud por vuelta en un resonador; también, Constante de Planck [J·s]
- $h(t)$ = Función de respuesta impulsiva de un sistema lineal (App. B, (B.1-2), p. 1132)
- $h(x,y)$ = Función de respuesta impulsiva de un sistema lineal 2D (App. B, (B.2-2), p. 1136)
- $h_D(t)$ = Función de respuesta impulsiva del detector
- $\hbar$ = $h/2\pi$ [J·s]
- $H$ = Amplitud compleja del campo magnético [A·m⁻¹]
- $\mathcal{H}$ = Campo magnético [A·m⁻¹]
- $H(\nu)$ (sans) = Función de transferencia de un sistema lineal (App. B, (B.1-3), p. 1133)
- $H'(\nu)$ (sans) = Parte real de la función de transferencia (App. B, p. 1134)
- $H''(\nu)$ (sans) = Parte imaginaria de la función de transferencia (App. B, p. 1134)
- $H(\nu_x,\nu_y)$ (sans) = Función de transferencia de un sistema lineal 2D (App. B, (B.2-3), p. 1136)
- $H_e(f)$ (sans) = Función de transferencia de la envolvente de un sistema lineal
- $\mathfrak{H}^{(1)}_\ell(\cdot)$ = Función de Hankel de primera especie de orden $\ell$
- $\mathbb{H}_n(\cdot)$ = Polinomios de Hermite
- HHG = Generación de armónicos de orden alto
- HVPE = Epitaxia en fase de vapor de hidruros

**I** [pp. 1145–1146]
- $i$ = Corriente eléctrica [A]; también, Entero
- $i_e$ = Corriente de electrones [A]
- $i_h$ = Corriente de huecos [A]
- $i_p$ = Corriente fotoeléctrica [A]
- $i_s$ = Corriente inversa en un diodo $p$–$n$ semiconductor [A]
- $i_t$ = Corriente umbral de un diodo láser [A]
- $i_T$ = Corriente de transparencia de un amplificador de diodo láser [A]
- $I$ = Intensidad óptica [W·m⁻²]
- $I(t)$ = Intensidad de un pulso óptico [W·m⁻²]
- $I_s$ = Intensidad óptica de saturación de un amplificador o absorbedor [W·m⁻²]; también, Intensidad acústica [W·m⁻²]
- $I_\nu$ = Intensidad espectral [W·m⁻²·Hz⁻¹]
- $I_0(\cdot)$ = Función de Bessel modificada de orden cero
- $\mathcal{I}$ = Transformada de Fourier del perfil de intensidad; también, Momento de inercia [kg·m²]
- IM = Modulación de intensidad
- IR = Infrarrojo
- ISI = Interferencia entre símbolos

**J** [p. 1146]
- $j$ = $\sqrt{-1}$; también, Entero
- $J$ = Densidad de corriente eléctrica [A·m⁻²]
- $J_e$ = Densidad de corriente de electrones [A·m⁻²]
- $J_h$ = Densidad de corriente de huecos [A·m⁻²]
- $J_\ell(\cdot)$ = Función de Bessel de primera especie de orden $\ell$ (App. A, (A.3-6), p. 1130)
- $J_p$ = Densidad de corriente fotoeléctrica [A·m⁻²]
- $J_t$ = Densidad de corriente umbral de un diodo láser [A·m⁻²]
- $J_T$ = Densidad de corriente de transparencia de un amplificador de diodo láser [A·m⁻²]
- $\mathbf{J}$ (neg) = Vector de Jones
- $\mathcal{J}$ = Número cuántico de momento angular total
- $\mathfrak{J}$ (neg frak) = Vector densidad de corriente eléctrica [A·m⁻²]

**K** [p. 1146]
- $k$ = Número de onda [m⁻¹]; también, Entero
- $k_o$ = Número de onda en el vacío [m⁻¹]
- $k_T = \sqrt{k_x^2+k_y^2}$ = Componente transversal del vector de onda [m⁻¹]
- $k_x, k_y$ = Componentes del vector de onda en $x$ y $y$ [m⁻¹]; también, Frecuencias angulares espaciales en $x$ y $y$ [rad·m⁻¹]
- $k_0$ = Número de onda central [m⁻¹]
- $\mathbf{k}$ (neg) = Vector de onda [m⁻¹]
- $\mathbf{k}_g$ (neg) = Vector de onda de una red (grating) [m⁻¹]
- $\mathrm{k}$ (red) = Razón de ionización de un fotodiodo de avalancha
- $k$ (sans) = Constante de Boltzmann [J·K⁻¹]
- $\mathrm{K}_m(\cdot)$ = Función de Bessel modificada de segunda especie de orden $m$
- $K$ (sans) = Número de onda de Bloch [m⁻¹] (App. C, p. 1141)
- $\mathbf{K}$ (neg sans) = Vector de onda de Bloch [m⁻¹]
- KDP = Fosfato dihidrógeno de potasio

**L** [pp. 1146–1147]
- $l$ = Longitud [m]; también, Entero
- $l_c$ = Longitud de coherencia [m]
- $\ell$ = Número cuántico azimutal
- $\ell_0$ = Camino óptico de la componente de frecuencia central de un pulso
- $L$ = Longitud [m]; también, Inductancia eléctrica [H]; también, Factor de pérdida; también, Entero
- $L_c$ = Longitud de coherencia en una interacción paramétrica [m]
- $L_0 = \pi/2\mathcal{C}$ = Longitud de acoplamiento (distancia de transferencia) en un acoplador direccional [m]
- $\mathcal{L}$ = Operador lineal (App. C, (C.1-1), p. 1137)
- $\mathfrak{L}$ = Número cuántico de momento angular orbital
- ${}^{2S+1}\mathfrak{L}_{\mathcal{J}}$ = Símbolo de término para números cuánticos de momento angular con acoplamiento LS
- $L$ (sans) = Momento angular [J·s]
- $\mathbb{L}^l_m(\cdot)$ = Polinomio de Laguerre de orden $l$ e índice $m$
- LAN = Red de área local
- LANL = Los Alamos National Laboratory
- LASER = Amplificación de luz por emisión estimulada de radiación
- LBO = Triborato de litio
- LC = Cristal líquido
- LCD = Pantalla de cristal líquido
- LCP = Polarizado circularmente a izquierda
- LD = Diodo láser
- LED = Diodo emisor de luz
- LHS = Lado izquierdo
- LLNL = Lawrence Livermore National Laboratory
- LMA = Área modal grande
- LP = Linealmente polarizado
- LPE = Epitaxia en fase líquida
- LWI = Emisión láser sin inversión
- LWIR = Infrarrojo de onda larga

**M** [p. 1147]
- $m$ = Masa de una partícula [kg]; también, Entero; también, Contraste o profundidad de modulación
- $m_c$ = Masa efectiva de un electrón en la banda de conducción [kg]
- $m_r$ = Masa reducida de un par electrón–hueco en un semiconductor [kg]
- $m_v$ = Masa efectiva de un hueco en la banda de valencia [kg]
- $m = m_0$ = Masa del electrón libre [kg]
- $m$ (sans) = Número de fotones; también, Número de fotoelectrones
- $\mathrm{m}$ (red) = Número cuántico magnético
- $M$ = Aumento (magnificación) en un sistema de imagen; también, Número de modos; también, Entero
- $\mathcal{M}$ = Densidad de magnetización [A·m⁻¹]; también, Número de modos de luz térmica; también, Figura de mérito del efecto acusto-óptico [m²·W⁻¹]
- $M$ (sans) = Masa de un átomo o molécula [kg]
- $M_r$ (sans) = Masa reducida de un átomo o molécula [kg]
- $M(\nu)$ (sans) = Densidad de modos en un resonador o cavidad [m⁻³·Hz⁻¹ para 3D; m⁻¹·Hz⁻¹ para 1D]
- $\mathbf{M}$ (neg) = Matriz de transferencia de rayos; también, Matriz de transferencia de ondas (App. C, (C.1-3), p. 1138)
- $\mathrm{M}^2$ = Factor que indica la desviación de un perfil de haz óptico respecto a la forma gaussiana
- MBE = Epitaxia por haces moleculares
- MEMS = Sistemas microelectromecánicos
- MIM = Metal–aislante–metal
- MIR = Infrarrojo medio
- MIRACL = Mid-infrared advanced chemical laser
- MKS = Sistema de unidades metro/kilogramo/segundo
- MMF = Fibra multimodo
- MOCVD = Depósito químico en fase de vapor metal-orgánico
- MQD = Puntos cuánticos múltiples
- MQW = Pozos cuánticos múltiples
- MOSFET = Transistor de efecto de campo metal-óxido-semiconductor
- MUV = Ultravioleta medio
- MUX = Multiplexor
- MWIR = Infrarrojo de onda media
- MZI = Interferómetro de Mach–Zehnder

**N** [pp. 1147–1148]
- $n$ = Índice de refracción; también, Entero
- $n(\mathbf{r})$ = Índice de refracción de un medio inhomogéneo
- $n(\theta)$ = Índice de refracción de la onda extraordinaria con vector de onda a un ángulo $\theta$ del eje óptico de un cristal uniaxial
- $n_e$ = Índice de refracción extraordinario
- $n_o$ = Índice de refracción ordinario
- $n_2$ = Coeficiente Kerr óptico (índice de refracción no lineal) [m²·W⁻¹]
- $\mathrm{n}$ (red) = Densidad de número de fotones [m⁻³]
- $\mathrm{n}_s$ (red) = Densidad de número de fotones de saturación [m⁻³]
- $n$ (sans) = Número de fotones
- $\mathrm{n}$ (red, otra fuente) = Número cuántico principal
- $\mathrm{n}$ (red) = Concentración de electrones en un semiconductor [m⁻³]
- $\mathrm{n}_i$ (red) = Concentración de electrones/huecos en un semiconductor intrínseco [m⁻³]
- $\mathrm{n}_0$ (red) = Concentración de equilibrio de electrones en un semiconductor [m⁻³]
- $N$ = Índice de grupo; también, Entero; también, Número de átomos; también, Número de puntos resolubles de un escáner
- $N_F$ = Número de Fresnel
- $N$ (sans) = Densidad de número [m⁻³]; también, $N = N_2 - N_1$ = Diferencia de densidad de población entre los niveles 2 y 1 [m⁻³]
- $N_a$ (sans) = Densidad de número atómica [m⁻³]
- $N_A$ (sans) = Densidad de número de átomos aceptores ionizados en un semiconductor [m⁻³]
- $N_D$ (sans) = Densidad de número de átomos donores ionizados en un semiconductor [m⁻³]
- $N_t$ (sans) = Diferencia de población umbral de un láser [m⁻³]
- $N_0$ (sans) = Diferencia de población en estado estacionario en ausencia de radiación amplificada [m⁻³]
- NA = Apertura numérica
- NEA = Afinidad electrónica negativa
- NIF = National Ignition Facility
- NIR = Infrarrojo cercano
- NLDC = Acoplador direccional no lineal
- NOLM = Espejo de lazo óptico no lineal
- NRZ = Sin retorno a cero
- NUV = Ultravioleta cercano
- NZ-DSF = Fibra de dispersión desplazada no nula

**O** [p. 1148]
- OA = Amplificador óptico
- OADM = Multiplexor óptico add-drop
- OC = Portadora óptica
- OCT = Tomografía de coherencia óptica
- ODMUX = Demultiplexor óptico
- O/E = Óptico a electrónico
- OFA = Amplificador de fibra óptica
- OFC = Conversión de frecuencia óptica
- OLED = Diodo orgánico emisor de luz
- OMUX = Multiplexor óptico
- OOK = Modulación on–off (on–off keying)
- OPA = Amplificador paramétrico óptico
- OPC = Conjugación de fase óptica
- OPO = Oscilador paramétrico óptico
- OXC = Conmutador de cruce óptico

**P** [pp. 1148–1149]
- $p$ = Probabilidad; también, Momento [kg·m·s⁻¹]; también, Parámetro de perfil de una fibra de índice gradual
- $p(n)$ = Probabilidad de $n$ eventos
- $p(x,y)$ = Función de apertura o función pupila
- $p_{\rm ab}$ = Densidad de probabilidad de absorción (modo con un fotón) [s⁻¹]
- $p_{\rm sp}$ = Densidad de probabilidad de emisión espontánea (a un modo) [s⁻¹]
- $p_{\rm st}$ = Densidad de probabilidad de emisión estimulada (modo con un fotón) [s⁻¹]
- $\mathrm{p}$ (red) = Momento dipolar [C·m]
- $p$ (sans) = Componente de cuadratura normalizada del campo eléctrico
- $\mathrm{p}$ (red) = Constante fotoelástica (coeficiente elasto-óptico)
- $\mathfrak{p}_{ijkl}$ = Elemento del tensor elasto-óptico
- $\mathfrak{p}_{IK}$ = Elemento del tensor elasto-óptico (índices contraídos)
- $\mathrm{p}$ (red) = Concentración de huecos en un semiconductor [m⁻³]
- $\mathrm{p}_0$ (red) = Concentración de equilibrio de huecos en un semiconductor [m⁻³]
- $P$ = Amplitud compleja de la densidad de polarización eléctrica [C·m⁻²]
- $P(\nu_x,\nu_y)$ = Transformada de Fourier de la función de apertura $p(x,y)$
- $P_{\rm ab}$ = Densidad de probabilidad de absorción (modo con muchos fotones) [s⁻¹]
- $P_{\rm NL}$ = Amplitud compleja de la componente no lineal de la densidad de polarización [C·m⁻²]
- $P_{\rm sp}$ = Densidad de probabilidad de emisión espontánea (a cualquier modo) [s⁻¹]
- $P_{\rm st}$ = Densidad de probabilidad de emisión estimulada (modo con muchos fotones) [s⁻¹]
- $P^\ell_{\rm m}(\cdot)$ = Función de Legendre adjunta de un resonador de microesfera
- $\mathcal{P}$ = Densidad de polarización eléctrica [C·m⁻²]
- $\mathcal{P}_{\rm L}$ = Componente lineal de la densidad de polarización [C·m⁻²]
- $\mathcal{P}_{\rm NL}$ = Componente no lineal de la densidad de polarización [C·m⁻²]
- $P$ (sans) = Potencia óptica [W]
- $P_p$ (sans) = Potencia de bombeo [W]
- $P_\nu$ (sans) = Densidad espectral de potencia [W·Hz⁻¹]
- $P_\pi$ (sans) = Potencia óptica de media onda en un medio Kerr [W]
- $\mathbb{P}$ = Grado de polarización
- $\mathrm{P}$ (red) = Potencia óptica [dBm]
- PAL-SLM = Modulador espacial de luz alineado en paralelo
- PBG = Banda fotónica prohibida
- PBS = Divisor de haz polarizante
- PCF = Fibra de cristal fotónico
- PCM = Modulación por codificación de pulsos
- PG-FROG = FROG con compuerta de polarización
- PIN = Tipo $p$ – intrínseco – tipo $n$
- PLC = Circuito de onda de luz planar
- PLED = Diodo emisor de luz de polímero
- PM = Modulación de fase
- PMD = Dispersión por modo de polarización
- PMT = Tubo fotomultiplicador
- PPLN = Niobato de litio polarizado periódicamente
- PROM = Modulador óptico de lectura Pockels
- PSK = Modulación por desplazamiento de fase
- PWM = Modulación por ancho de pulso

**Q** [pp. 1149–1150]
- $q$ = Carga eléctrica [C]; también, Número de onda de una onda acústica [m⁻¹]; también, Entero (índice de modo, orden de difracción, número cuántico) (App. C: índice de modo, p. 1137)
- $q(z)$ = Parámetro complejo de un haz gaussiano [m]
- $\mathbf{q}$ (neg) = Vector de onda de una onda acústica [m⁻¹]
- $Q$ = Carga eléctrica [C]; también, Factor de calidad de un resonador óptico
- QCSE = Efecto Stark de confinamiento cuántico
- QD = Punto cuántico
- QDIP = Fotodetector infrarrojo de puntos cuánticos
- QED = Electrodinámica cuántica
- QPM = Ajuste de fase cuasi (quasi-phase matching); también, Modulador de fase cuadrático
- QWIP = Fotodetector infrarrojo de pozos cuánticos

**R** [p. 1150]
- $r$ = Distancia radial en coordenadas esféricas [m]; también, Distancia radial en coordenadas cilíndricas [m]
- $r_n$ = Radios de las órbitas electrónicas permitidas en un átomo de Bohr [m]
- $r_1$ = Radio de Bohr del estado base del hidrógeno [m]
- $\mathbf{r}$ (neg) = Vector de posición [m]
- $\hat{\mathbf{r}}$ = Vector unitario radial en coordenadas esféricas
- $\mathrm{r}$ (red) = Reflectancia de amplitud compleja
- $|\mathrm{r}|$ = Magnitud del factor de atenuación de amplitud por vuelta en un resonador
- $r(\nu)$ (sans) = Tasa de emisión/absorción de fotones en un semiconductor [s⁻¹·m⁻³·Hz⁻¹]
- $\mathfrak{r}$ = Coeficiente electro-óptico lineal (Pockels) [m·V⁻¹]; también, Número cuántico rotacional
- $\mathfrak{r}_{ijk}$ = Elemento del tensor electro-óptico lineal [m·V⁻¹]
- $\mathfrak{r}_{Ik}$ = Elemento del tensor electro-óptico lineal (índices contraídos) [m·V⁻¹]
- $\mathrm{r}$ (red, otra fuente) = Coeficiente de recombinación electrón–hueco [m³·s⁻¹]
- $\mathrm{r}_{\rm nr}$ = Coeficiente de recombinación no radiativa electrón–hueco [m³·s⁻¹]
- $\mathrm{r}_r$ = Coeficiente de recombinación radiativa electrón–hueco [m³·s⁻¹]
- $R$ = Radio de curvatura [m]; también, Resistencia eléctrica [Ω]
- $R(z)$ = Radio de curvatura de un haz gaussiano [m]
- $R_0$ = Radio del cilindro en que se confina un rayo meridional [m]
- $\mathbf{R}(\theta)$ (neg) = Matriz de Jones para rotación de coordenadas por un ángulo $\theta$
- $\mathcal{R}$ = Reflectancia de intensidad o potencia
- $R$ (sans) = Tasa de bombeo [s⁻¹·m⁻³]; también, Tasa de recombinación en un semiconductor [s⁻¹·m⁻³]; también, Tasa de inyección electrón–hueco en un semiconductor [s⁻¹·m⁻³]
- $R_t$ (sans) = Tasa de bombeo umbral de un láser [s⁻¹·m⁻³]
- $\mathbf{R}$ (neg sans) = Vector de red [m]
- $\mathfrak{R}$ = Responsividad de una fuente de fotones [W·A⁻¹]; también, Responsividad de un fotodetector [A·W⁻¹]
- $\mathfrak{R}_d$ = Responsividad diferencial de un diodo láser [W·A⁻¹]
- $\mathbb{R}_{\mathrm{n}\ell}(r)$ = Función de Laguerre asociada al átomo de hidrógeno de orden $\ell$ e índice $\mathrm{n}$
- RC = Cavidad resonante
- $RC$ = Combinación resistencia–capacitor
- RCP = Polarizado circularmente a derecha
- REFA = Amplificadores de fibra dopada con tierras raras
- RF = Radiofrecuencia
- RFA = Amplificador de fibra Raman
- RFL = Láser de fibra Raman
- RHS = Lado derecho
- RMS = Raíz cuadrática media
- ROADM = Multiplexor óptico add-drop reconfigurable
- RW = Guía de onda de cresta (ridge)
- RZ = Retorno a cero

**S** [pp. 1150–1151]
- $s$ = Longitud o distancia [m]
- $s(x,t)$ = Función de onda de deformación (strain)
- $s_{ij}$ = Elemento del tensor de deformación
- $s(\mathbf{r}_1,\mathbf{r}_2,\nu)$ (sans) = Densidad espectral cruzada normalizada
- $\mathfrak{s}$ = Coeficiente electro-óptico cuadrático (Kerr) [m²·V⁻²]; también, Número cuántico de espín
- $\mathfrak{s}_{ijkl}$ = Elemento del tensor electro-óptico cuadrático [m²·V⁻²]
- $\mathfrak{s}_{IK}$ = Elemento del tensor electro-óptico cuadrático (índices contraídos) [m²·V⁻²]
- $S$ = Fuerza de transición (fuerza de oscilador) [m²·Hz]
- $S(\mathbf{r},t)$ = Amplitud compleja de una fuente de radiación [V·m⁻³]
- $S(\cdot)$ = Integral de Fresnel
- $\mathcal{S}$ = Fuente de radiación óptica creada por un campo incidente [V·m⁻³]; también, Número cuántico de momento angular de espín
- $\mathcal{S}$ (neg cal) = Vector de Poynting [W·m⁻²]
- $S(\mathbf{r})$ (sans) = Eikonal [m]
- $S(\mathbf{r}_1,\mathbf{r}_2,\nu)$ (sans) = Densidad espectral cruzada [W·m⁻²·Hz⁻¹]
- $S(\nu)$ (sans) = Intensidad espectral de una onda o pulso óptico [W·m⁻²·Hz⁻¹]; también, Densidad espectral de potencia [W·m⁻²·Hz⁻¹]
- $S(\nu,t)$ (sans) = Espectrograma de un pulso óptico [$S(\nu,t) = |\Phi(\nu,t)|^2$]
- $\mathbf{S}$ (neg) = Matriz de dispersión (scattering)
- $\mathbb{S}$ = Momento angular de espín del fotón [J·s]
- $\mathrm{S}_{[\,]}$ = Parámetros de Stokes
- SAGM = Separate-absorption-grading-multiplication
- SAM = Separate-absorption-multiplication
- SBN = Niobato de estroncio y bario
- SBS = Dispersión Brillouin estimulada
- SCG = Generación de supercontinuo
- SDH = Jerarquía digital síncrona
- SEED = Dispositivo de efecto autoelectro-óptico
- SESAM = Espejo absorbedor saturable de semiconductor
- SFG = Generación de suma de frecuencias
- SH = Segundo armónico
- SHG = Generación de segundo armónico
- SHG-FROG = FROG por generación de segundo armónico
- SLAC = Stanford Linear Accelerator Center
- SLD = Diodo superluminiscente
- SLM = Modulador espacial de luz
- SMF = Fibra monomodo
- SNOM = Microscopía óptica de barrido de campo cercano
- SNR = Relación señal a ruido
- SOA = Amplificador óptico de semiconductor
- SOI = Silicio sobre aislante
- SONET = Red óptica síncrona
- SOS = Sílice sobre silicio
- SPAD = Fotodiodo de avalancha de fotón único
- SPDC = Conversión paramétrica descendente espontánea
- SPM = Automodulación de fase
- SPP = Plasmón-polaritón de superficie
- SQW = Pozo cuántico único
- SRO = Oscilador simplemente resonante
- SRS = Dispersión Raman estimulada
- SSFS = Desplazamiento de autofrecuencia de solitón
- SSPD = Detector superconductor de fotón único
- SVE = Envolvente lentamente variable
- SXR = Rayos X blandos

**T** [pp. 1151–1152]
- $t$ = Tiempo [s]
- $t_{\rm sp}$ = Tiempo de vida espontáneo [s]
- $\mathrm{t}$ (red) = Transmitancia de amplitud compleja; también, Tiempo normalizado de un pulso óptico
- $T$ = Temperatura [K]
- $\mathbf{T}$ (neg) = Matriz de Jones
- $\mathcal{T}$ = Transmitancia de intensidad o potencia; también, Razón de transferencia o transmisión de potencia
- $T$ (sans) = Tiempo de tránsito [s]; también, Tiempo de conteo [s]; también, Tiempo de conmutación [s]; también, Intervalo de tiempo de bit [s]; también, Tiempo de resolución ($T = 1/2B$, $B$ = ancho de banda) [s]; también, Periodo de una onda ($T = 1/\nu$) [s]
- $T_F = 1/\nu_F$ (sans) = Inverso del espaciamiento de frecuencias de los modos de un resonador Fabry–Perot ($T_F = 2d/c$) [s]; también, Periodo de un tren de pulsos láser de modos bloqueados [s]
- $T_2$ (sans) = Tiempo de colisión electrón–fonón [s]
- TDM = Multiplexación por división de tiempo
- TDMA = Acceso múltiple por división de tiempo
- TE = Transversal eléctrico
- TEM = Transversal electromagnético
- TFF = Filtro de película delgada
- TGG = Granate de terbio y galio
- THG = Generación de tercer armónico
- TM = Transversal magnético
- TOAD = Demultiplexor óptico asimétrico de terahertz
- TPLSM = Microscopía de fluorescencia de barrido láser de dos fotones
- TSI = Intercambio de ranura temporal
- TST = Tiempo-espacio-tiempo

**U** [p. 1152]
- $u$ = Desplazamiento [m]
- $u(\mathbf{r},t)$ = Función de onda de una onda óptica
- $\hat{\mathbf{u}}$ = Vector unitario
- $\mathrm{u}$ (red) = Número de electrones en una subcapa
- $U(\mathbf{r})$ = Amplitud compleja de una onda óptica monocromática
- $U(\mathbf{r},t)$ = Función de onda compleja de una onda óptica
- $U(t)$ = Función de onda compleja de un pulso óptico
- $\mathcal{U}(x)$ = Función escalón unitario
- UV = Ultravioleta

**V** [pp. 1152–1153]
- $v$ = Velocidad de grupo de una onda [m·s⁻¹]
- $v(\mathbf{r},\nu)$ = Transformada de Fourier de la función de onda de una onda óptica
- $v_s$ = Velocidad del sonido [m·s⁻¹]
- $v$ (sans) = Velocidad de un átomo u objeto [m·s⁻¹]
- $v_e$ (sans) = Velocidad de un electrón [m·s⁻¹]
- $v_h$ (sans) = Velocidad de un hueco [m·s⁻¹]
- $\mathbf{v}$ (neg) = Vector velocidad de un portador de carga [m·s⁻¹]
- $\mathfrak{v}$ = Número cuántico vibracional
- $V$ = Volumen [m³]; también, Volumen modal [m³]; también, Voltaje [V]
- $V(\mathbf{r},\nu)$ = Transformada de Fourier de la función de onda compleja de una onda óptica
- $V(\nu)$ = Transformada de Fourier de la función de onda compleja de un pulso óptico
- $V_c$ = Voltaje crítico de una celda de cristal líquido [V]
- $V_\pi$ = Voltaje de media onda de un retardador o modulador electro-óptico [V]
- $V_0$ = Diferencia de potencial interna (built-in) en una unión $p$–$n$ [V]; también, Voltaje de conmutación de un acoplador direccional [V]
- $\mathcal{V}$ = Visibilidad
- $\mathfrak{V}$ = Constante de Verdet [min·Oersted⁻¹·cm⁻¹]
- $V$ (sans) = Parámetro $V$ de una fibra
- $V(\mathbf{r})$ (sans) = Energía potencial [J] (App. C, (C.1-11), p. 1140)
- $\mathbb{V}$ = Número de Abbe de un medio dispersivo
- VCSEL = Láser de emisión superficial de cavidad vertical
- VLSI = Integración a muy gran escala
- VOx = Óxido de vanadio
- VPE = Epitaxia en fase de vapor
- VUV = Ultravioleta de vacío

**W** [p. 1153]
- $w$ = Ancho [m]
- $\mathrm{w}$ (red) = Flujo de fotones integrado (potencia óptica integrada en unidades de número de fotones)
- $w_d$ (sans) = Ancho de la región de absorción en un fotodiodo de avalancha [m]
- $w_m$ (sans) = Ancho de la región de multiplicación en un fotodiodo de avalancha [m]
- $W$ = Densidad de energía electromagnética promediada en el tiempo [J·m⁻³]
- $W(t)$ = Función ventana para la transformada de Fourier de tiempo corto
- $W(z)$ = Ancho (radio) de un haz gaussiano a distancia axial $z$ del centro del haz [m]
- $W_0$ = Radio de la cintura de un haz gaussiano [m]
- $\mathcal{W}$ = Densidad de energía electromagnética [J·m⁻³]
- $W$ (sans) = Densidad de probabilidad de absorción de luz de bombeo [s⁻¹]
- $W_i$ (sans) = Densidad de probabilidad de absorción y emisión estimulada [s⁻¹]
- $\mathrm{W}$ (red) = Función de trabajo fotoeléctrica [J]
- WC = Convertidor de longitud de onda
- WCI = Intercambio de canal de longitud de onda
- WDM = Multiplexación por división de longitud de onda
- WDMA = Acceso múltiple por división de longitud de onda
- WGM = Modo de galería de susurros
- WGR = Enrutador de red de guías de onda
- WKB = Wentzel–Kramers–Brillouin
- WOLED = OLED blanco

**X** [p. 1153]
- $x$ = Coordenada de posición; desplazamiento [m]
- $\hat{\mathbf{x}}$ = Vector unitario en la dirección $x$
- $\mathrm{x}(t)$ (red) = Transformada de Fourier inversa de la susceptibilidad de un medio dispersivo $\chi(\nu)$
- $x$ (sans) = Componente de cuadratura normalizada del campo eléctrico
- $X$ = Densidad de flujo de fotones normalizada a la entrada de un amplificador óptico
- $\hat{\mathbf{X}}$ = Vector de entrada a un sistema lineal (App. C, (C.1-1), p. 1137)
- $\mathcal{X}(u)$ = Función real asociada al haz de Hermite–Gauss
- $\mathcal{X}^{(2)}(\omega_1,\omega_2)$ = Susceptibilidad no lineal de segundo orden
- $X(\cdot)$ (sans) = Tasa de cambio normalizada de la distribución radial en el núcleo de una fibra de índice escalonado
- XC = Conmutador de cruce (cross-connect)
- XGM = Modulación de ganancia cruzada
- XPM = Modulación de fase cruzada
- XUV = Ultravioleta extremo

**Y** [pp. 1153–1154]
- $y$ = Coordenada de posición [m]
- $Y$ = Densidad de flujo de fotones normalizada a la salida de un amplificador óptico
- $\hat{\mathbf{Y}}$ = Vector de salida de un sistema lineal (App. C, (C.1-1), p. 1137)
- $\mathcal{Y}(v)$ = Función real asociada al haz de Hermite–Gauss
- $Y(\cdot)$ (sans) = Tasa de cambio normalizada de la distribución radial en el revestimiento de una fibra de índice escalonado
- YIG = Granate de hierro e itrio

**Z** [p. 1154]
- $z$ = Coordenada de posición (cartesiana o cilíndrica) [m]
- $z_0$ = Rango de Rayleigh de un haz gaussiano [m]; también, Rango de Rayleigh de un pulso gaussiano que viaja en un medio dispersivo [m]
- $\mathrm{z}$ (red) = Distancia normalizada de un pulso óptico [m]
- $Z$ = Número atómico
- $\mathcal{Z}(\cdot)$ = Función real asociada al haz de Hermite–Gauss

### Símbolos griegos [pp. 1154–1158]

**α** [p. 1154]
- $\alpha$ = Coeficiente de atenuación o absorción [m⁻¹]; también, Ángulo del vértice de un prisma; también, Coeficiente de torsión de un cristal líquido nemático torcido [m⁻¹]
- $\alpha_e$ = Coeficiente de ionización de electrones en un semiconductor [m⁻¹]
- $\alpha_h$ = Coeficiente de ionización de huecos en un semiconductor [m⁻¹]
- $\alpha_m$ = Coeficiente de pérdida de un resonador atribuido a un espejo [m⁻¹]
- $\alpha_r$ = Coeficiente efectivo de pérdida distribuida total [m⁻¹]
- $\alpha_s$ = Coeficiente de pérdida de un medio láser [m⁻¹]
- $\alpha_p$ = Valor medio de $p$ para un estado coherente
- $\alpha_x$ = Valor medio de $x$ para un estado coherente
- $\alpha_\nu$ = Coeficiente de dispersión angular [Hz⁻¹]
- $\alpha$ (sans) = Coeficiente de atenuación de una fibra óptica [dB/km]

**β** [p. 1154]
- $\beta = k_z$ = Constante de propagación [m⁻¹]; también, Coeficiente de retardo de fase de un cristal líquido nemático torcido [m⁻¹] (App. C: $\beta_q$ del modo $q$, p. 1141)
- $\beta'$ = Primera derivada de $\beta$ respecto a $\omega$ [m⁻¹·s]
- $\beta''$ = Segunda derivada de $\beta$ respecto a $\omega$ [m⁻¹·s²]
- $\beta(\nu)$ = Constante de propagación en un medio dispersivo [m⁻¹]
- $\beta_0 = \beta(\nu_0)$ = Constante de propagación a la frecuencia central $\nu_0$ [m⁻¹]
- $\beta$ (sans) = Coeficiente de acoplamiento de emisión espontánea

**γ, Γ** [p. 1154]
- $\gamma$ = Coeficiente de ganancia [m⁻¹]; también, Coeficiente de acoplamiento en un dispositivo paramétrico [m⁻¹]; también, Coeficiente no lineal en teoría de solitones; también, Coeficiente de decaimiento lateral en una guía de onda [m⁻¹]; también, Coeficiente de magnetogiración [m²·Wb⁻¹]
- $\gamma(\nu)$ = Coeficiente de ganancia de un amplificador óptico [m⁻¹]
- $\gamma_p$ = Coeficiente de ganancia pico de un amplificador de diodo láser [m⁻¹]
- $\gamma_0(\nu)$ = Coeficiente de ganancia de señal pequeña de un amplificador óptico [m⁻¹]
- $\Gamma$ = Retardo (retardation); también, Factor de confinamiento

**δ, Δ** [pp. 1154–1155]
- $\delta(\cdot)$ = Función delta o impulso (App. A, p. 1124)
- $\delta x$ = Incremento de $x$
- $\delta\nu$ = Ancho espectral de un modo de resonador [Hz]
- $\Delta$ = Espesor de un componente óptico delgado [m]; también, Cambio fraccional del índice de refracción en una fibra o guía de onda
- $\Delta x$ = Incremento de $x$
- $\Delta\mathrm{n}$ = Concentración de pares electrón–hueco en exceso [m⁻³]
- $\Delta\mathrm{n}_T$ = Concentración de portadores inyectados en un amplificador óptico de semiconductor en transparencia [m⁻³]
- $\Delta\nu$ = Ancho espectral o ancho de línea [Hz]
- $\Delta\nu_c = 1/\tau_c$ = Ancho espectral [Hz]
- $\Delta\nu_D$ = Ancho de línea Doppler [Hz]
- $\Delta\nu_{\rm FWHM}$ = Ancho espectral completo a mitad del máximo [Hz] (App. A, (A.2-15), (A.2-17), p. 1128)
- $\Delta\nu_s$ = Ancho de línea de un amplificador saturado [Hz]

**ε** [p. 1155]
- $\epsilon$ = Permitividad eléctrica de un medio [F/m]; también, Error de enfoque [m⁻¹]
- $\epsilon_{ij}$ = Componente del tensor de permitividad eléctrica [F/m]
- $\epsilon_e$ = Permitividad eléctrica efectiva [F/m]
- $\epsilon_o$ = Permitividad eléctrica del vacío [F/m]
- $\boldsymbol{\epsilon}$ (neg) = Tensor de permitividad eléctrica [F/m]

**ζ, η** [p. 1155]
- $\zeta(z)$ = Fase axial en exceso de un haz gaussiano
- $\eta$ = Impedancia de un medio dieléctrico [Ω]
- $\eta_o$ = Impedancia del vacío [Ω]
- $\eta$ (sans) = Impermeabilidad eléctrica (App. C, (C.1-10): $\eta(\mathbf{r}) = \epsilon_o/\epsilon(\mathbf{r})$, p. 1140)
- $\eta_{ij}$ (sans) = Componente del tensor de impermeabilidad eléctrica
- $\boldsymbol{\eta}$ (neg sans) = Tensor de impermeabilidad eléctrica
- $\eta$ (red) = Eficiencia cuántica de un fotodetector
- $\eta_c$ (red) = Eficiencia de conversión de potencia (eficiencia global, wall-plug)
- $\eta_d$ (red) = Eficiencia cuántica diferencial externa
- $\eta_e$ (red) = Eficiencia de extracción; también, Eficiencia de transmisión
- $\eta_{\rm ex}$ (red) = Eficiencia externa
- $\eta_i$ (red) = Eficiencia cuántica interna
- $\eta_s$ (red) = Eficiencia diferencial de conversión de potencia; también, Eficiencia de pendiente (slope)

**θ, Θ** [p. 1155]
- $\theta$ = Ángulo; también, Ángulo de torsión en un cristal líquido; también, Ángulo de desviación de un prisma
- $\bar\theta = 90° - \theta$ = Complemento del ángulo $\theta$
- $\theta_a$ = Ángulo de aceptación
- $\theta_B$ = Ángulo de Brewster
- $\theta_{\rm B}$ = Ángulo de Bragg
- $\theta_c$ = Ángulo crítico
- $\bar\theta_c$ = Ángulo crítico complementario
- $\theta_d$ = Ángulo de desviación de un prisma
- $\theta_s$ = Ángulo subtendido por la fuente
- $\theta_0$ = Ángulo de divergencia de un haz gaussiano
- $\hat{\boldsymbol{\theta}}$ = Vector unitario polar en coordenadas esféricas
- $\vartheta$ = Umbral
- $\Theta_{\ell m}(\theta)$ = Función de Legendre asociada al átomo de hidrógeno

**κ, λ, Λ** [pp. 1155–1156]
- $\kappa$ = Constante elástica de un oscilador armónico [J·m⁻²]
- $\lambda$ = Longitud de onda [m]
- $\lambda_A$ = Límite de longitud de onda larga del aceptor [m]
- $\lambda_c$ = Longitud de onda de corte [m]
- $\lambda_F$ = Espaciamiento en longitud de onda de modos Fabry–Perot adyacentes [m]
- $\lambda_g$ = Longitud de onda de la banda prohibida (límite de longitud de onda larga) de un semiconductor [m]
- $\lambda_o$ = Longitud de onda en el vacío [m]
- $\lambda_p$ = Longitud de onda de máxima densidad de energía de cuerpo negro [m]
- $\lambda_q$ = Autovalores de un problema de autovalores (App. C, (C.1-2), p. 1137)
- $\lambda_0$ = Longitud de onda central [m]
- $\lambda$ (sans) = Longitud de onda de de Broglie [m]
- $\Lambda$ = Periodo espacial de una red o estructura periódica [m]; también, Longitud de onda de una onda acústica [m]

**μ** [p. 1156]
- $\mu$ = Permeabilidad magnética [H·m⁻¹]; también, Movilidad de portadores en un semiconductor [m²·s⁻¹·V⁻¹]
- $\mu_e$ = Movilidad de electrones [m²·s⁻¹·V⁻¹]
- $\mu_h$ = Movilidad de huecos [m²·s⁻¹·V⁻¹]
- $\mu_o$ = Permeabilidad magnética del vacío [H·m⁻¹]

**ν** [p. 1156]
- $\nu$ = Frecuencia [Hz] (App. A, (A.1-1))
- $\nu_c$ = Frecuencia de corte [Hz]
- $\nu_F$ = Espaciamiento en frecuencia de modos Fabry–Perot adyacentes; rango espectral libre de un espectrómetro Fabry–Perot [Hz]
- $\nu_p$ = Frecuencia de máxima densidad de energía de cuerpo negro [Hz]
- $\nu_s$ = Ancho de banda espacial de un sistema de imagen [m⁻¹]
- $\nu_q$ = Frecuencia del modo $q$ [Hz]
- $\nu_x, \nu_y$ = Frecuencias espaciales en las direcciones $x$ y $y$ [m⁻¹] (App. A, (A.3-1), p. 1129)
- $\nu_{\rm B}$ = Frecuencia de Bragg [Hz]
- $\nu_A$ = Frecuencia de desplazamiento anti-Stokes [Hz]
- $\nu_B$ = Frecuencia Brillouin [Hz]
- $\nu_R$ = Frecuencia Raman [Hz]
- $\nu_S$ = Frecuencia de desplazamiento Stokes [Hz]
- $\nu_\rho$ = Componente radial de la frecuencia espacial: $\nu_\rho = \sqrt{\nu_x^2+\nu_y^2}$ [m⁻¹] (App. A, (A.3-6), p. 1130)
- $\nu_0$ = Frecuencia central [Hz]

**ξ** [p. 1156]
- $\xi$ = Coeficiente de acoplamiento en mezcla de cuatro ondas
- $\xi_{\rm sp}(\nu)$ = Densidad de flujo de fotones de ruido de amplificador por unidad de longitud [m⁻³·s⁻¹]

**ρ, ϱ** [p. 1156]
- $\rho$ = Poder rotatorio de un medio ópticamente activo [m⁻¹]; también, Resistividad [Ω·m]; también, $\rho = \sqrt{x^2+y^2}$ = Distancia radial en coordenadas cilíndricas [m]
- $\rho_c$ = Distancia de coherencia [m]
- $\rho_s$ = Radio del disco de Airy [m]; también, Radio de la mancha de desenfoque de un sistema de imagen [m] (App. B, p. 1136)
- $\varrho$ = Densidad de masa de un medio [kg·m⁻³]; también, Densidad de carga [C·m⁻³]
- $\varrho(k)$ = Densidad de estados en número de onda [m⁻²]
- $\varrho(\nu)$ = Densidad espectral de energía [J·m⁻³·Hz⁻¹]; también, Densidad conjunta óptica de estados [m⁻³·Hz⁻¹]
- $\varrho_c(E)$ = Densidad de estados cerca del borde de la banda de conducción [m⁻³·J⁻¹ en un semiconductor masivo]
- $\varrho_v(E)$ = Densidad de estados cerca del borde de la banda de valencia [m⁻³·J⁻¹ en un semiconductor masivo]
- $\rho(\nu)$ (sans) = Modo de cavidad lorentziano normalizado [Hz⁻¹]

**σ** [p. 1156]
- $\sigma$ = Conductividad [Ω⁻¹·m⁻¹]
- $\sigma_s$ = Matriz de espín de Pauli
- $\sigma(\nu)$ = Sección eficaz de transición [m²]
- $\sigma_{\max}$ = Sección eficaz de transición máxima [m²]
- $\sigma_q$ = Parámetro de ruido de circuito
- $\sigma_x$ = Desviación estándar de una variable aleatoria $x$; ancho RMS de una función de $x$ (App. A, (A.2-1), p. 1124)
- $\sigma_0 = \sigma(\nu_0)$ = Sección eficaz de transición a la frecuencia central $\nu_0$ [m²]
- $\sigma$ (sans) = Coeficiente de amortiguamiento de un oscilador armónico [s⁻¹] (App. B, (B.1-8), p. 1134)
- $\boldsymbol{\sigma}$ (neg) = Tensor de conductividad [Ω⁻¹·m⁻¹]

**τ** [pp. 1156–1157]
- $\tau$ = Tiempo de vida [s]; también, Tiempo de decaimiento [s]; también, Tiempo de relajación [s]; también, Ancho de una función del tiempo [s] (App. A, (A.2-8), p. 1127); también, Tiempo de vida de recombinación electrón–hueco de portadores en exceso en un semiconductor [s]
- $\tau_c$ = Tiempo de coherencia [s]
- $\tau_{\rm col}$ = Tiempo medio entre colisiones [s]
- $\tau_d$ = Tiempo de retardo [s]
- $\tau_e$ = Tiempo de tránsito de electrones [s]
- $\tau_h$ = Tiempo de tránsito de huecos [s]
- $\tau_m$ = Tiempo de multiplicación en un fotodiodo de avalancha [s]
- $\tau_{\rm nr}$ = Tiempo de vida de recombinación no radiativa electrón–hueco [s]
- $\tau_p$ = Tiempo de vida del fotón en un resonador [s]
- $\tau_{\rm pulse}$ = Duración de un pulso óptico de modos bloqueados [s]
- $\tau_r$ = Tiempo de vida de recombinación radiativa electrón–hueco [s]
- $\tau_{RC}$ = Constante de tiempo $RC$ [s]
- $\tau_s$ = Constante de tiempo de saturación de una transición láser [s]
- $\tau_{21}$ = Tiempo de vida de una transición entre los niveles 2 y 1 [s]

**φ, ϕ, Φ** [p. 1157]
- $\phi$ = Ángulo en coordenadas cilíndricas; también, Densidad de flujo de fotones [m⁻²·s⁻¹]
- $\phi(p)$ = Función de onda en momento [s^{1/2}·kg^{−1/2}·m^{−1/2}]
- $\phi_\nu$ = Densidad espectral de flujo de fotones [m⁻²·s⁻¹·Hz⁻¹]
- $\phi_s(\nu)$ = Densidad de flujo de fotones de saturación [m⁻²·s⁻¹]
- $\hat{\boldsymbol{\Phi}}$ = Vector unitario azimutal en coordenadas esféricas
- $\varphi$ = Diferencia de fase
- $\varphi(t)$ = Fase de la envolvente compleja de un pulso óptico
- $\varphi_0$ = Desplazamiento de fase por reflexión en un espejo de resonador
- $\varphi(\nu)$ = Coeficiente de desplazamiento de fase de un amplificador óptico [m⁻¹]
- $\Phi$ = Flujo de fotones [s⁻¹]
- $\Phi(\nu,t)$ = Transformada de Fourier de tiempo corto
- $\Phi_{\rm m}(\phi)$ = Función armónica del átomo de hidrógeno
- $\Phi_\nu$ = Flujo espectral de fotones [s⁻¹·Hz⁻¹]

**χ** [p. 1157]
- $\chi$ = Susceptibilidad eléctrica; también, Afinidad electrónica [J]
- $\chi'$ = Parte real de la susceptibilidad eléctrica $\chi$
- $\chi''$ = Parte imaginaria de la susceptibilidad eléctrica $\chi$
- $\chi(\nu)$ = Susceptibilidad eléctrica de un medio dispersivo
- $\chi_{ij}$ = Componente del tensor de susceptibilidad eléctrica
- $\chi^{(3)}$ = Coeficiente de no linealidad óptica de tercer orden [C·m·V⁻³]
- $\chi^{(3)}_{ijkl}$ = Elemento del tensor de no linealidad óptica de tercer orden [C·m·V⁻³]
- $\chi^{(3)}_{IK}$ = Elemento del tensor de no linealidad de tercer orden (índices contraídos) [C·m·V⁻³]
- $\chi$ (sans) = Ángulo de elipticidad de la elipse de polarización
- $\boldsymbol{\chi}$ (neg) = Tensor de susceptibilidad eléctrica

**ψ, Ψ** [p. 1157]
- $\psi$ = Amplitud normalizada de un pulso óptico
- $\psi(t)$ = Fase espectral de un pulso óptico
- $\psi(x)$ = Función de onda de posición de una partícula [m^{−1/2}] (App. A, p. 1126)
- $\psi(\mathbf{r},t)$ = Función de onda de una partícula [m^{−3/2}·s^{−1/2}]
- $\psi$ (sans) = Orientación del eje mayor de la elipse de polarización
- $\Psi(\mathcal{E})$ = Densidad de polarización no lineal [C·m⁻²]
- $\Psi_e(f)$ = Fase de la función de transferencia de la envolvente

**ω, Ω** [pp. 1157–1158]
- $\omega$ = Frecuencia angular [rad·s⁻¹]
- $\omega_{\rm B}$ = Frecuencia angular de Bragg [rad·s⁻¹]
- $\omega_p$ = Frecuencia de plasma [rad·s⁻¹]
- $\omega_0$ = Frecuencia angular central [rad·s⁻¹] (App. B, (B.1-8): frecuencia angular de resonancia del oscilador, p. 1134)
- $\Omega$ = Frecuencia angular de una onda acústica [rad·s⁻¹]; también, Frecuencia angular de una señal eléctrica armónica [rad·s⁻¹]; también, Ángulo sólido

### Símbolos matemáticos [p. 1158]

- $\partial$ = Diferencial parcial
- $\nabla$ = Operador gradiente
- $\nabla\cdot$ = Operador divergencia
- $\nabla\times$ = Operador rotacional
- $\nabla^2$ = Operador laplaciano ($\nabla^2 = \partial^2/\partial x^2 + \partial^2/\partial y^2 + \partial^2/\partial z^2$ en coordenadas cartesianas)
- $\nabla_T^2$ = Operador laplaciano transversal ($\nabla_T^2 = \partial^2/\partial x^2 + \partial^2/\partial y^2$ en cartesianas)
- $\bar x = \langle x\rangle$ = Media de la cantidad $x$

Unidades que aparecen en la lista y conviene tener presentes: la no linealidad de segundo orden
$\mathrm{d}$, $\mathrm{d}_{ijk}$ está en [C·V⁻²] y la de tercer orden $\chi^{(3)}$ en [C·m·V⁻³]
(convención del libro, con $\mathcal{P}_{\rm NL}$ en C·m⁻²); el coeficiente Kerr $n_2$ en [m²·W⁻¹];
el coeficiente Pockels $\mathfrak{r}$ en [m·V⁻¹] y el Kerr electro-óptico $\mathfrak{s}$ en [m²·V⁻²];
$\beta'$ en [m⁻¹·s] y $\beta''$ en [m⁻¹·s²]; $D_\lambda$ en [s·m⁻²] y $D_\nu$ en [s²·m⁻¹].

---

## Relación con Óptica No Lineal

### 1. Convención de signos: Saleh frente a Boyd y Agrawal

- **Saleh & Teich**: onda temporal $\exp(+j2\pi\nu t) = \exp(+j\omega t)$ con frecuencia positiva;
  TF directa $F(\nu) = \int f(t)e^{-j2\pi\nu t}dt$ [p. 1122]; onda viajera
  $\exp(+j\omega t)\exp[-j(k_x x + k_y y + k_z z)]$ [p. 1129]; modo guiado con autovalor
  $\exp(-j\beta_q z)$ [p. 1141]. Ingeniería: $j$, $e^{j\omega t}$.
- **Boyd**, *Nonlinear Optics*, y **Agrawal**, *Nonlinear Fiber Optics*: física, $i$ y
  $\tilde E(t) = E e^{-i\omega t} + \text{c.c.}$, onda viajera $e^{i(kz-\omega t)}$. Es la
  convención opuesta: $j \to -i$. Consecuencias prácticas:
  - Un retardo $\tau$ es $e^{-j2\pi\nu\tau}$ en Saleh y $e^{+i\omega\tau}$ en Boyd/Agrawal.
  - La parte imaginaria de $\chi$ (o de $H$): en Saleh, pérdida ⇔ $\chi'' $ con el signo de
    (B.1-11), $H'' < 0$ para un sistema amortiguado; en Boyd, absorción ⇔ $\mathrm{Im}\,\chi > 0$.
    Al pasar fórmulas entre libros hay que conjugar.
  - La definición de $\beta''$ (GVD) no cambia de signo, pero la fase acumulada del chirp sí:
    $H(\nu) = \exp(-j\pi\nu^2)$ en Saleh [p. 1133] ↔ $\exp(+i\,\cdot)$ en Agrawal.
  - La convención *espacial* de Saleh (A.3-2, exponente $+j$) es la contraria a su propia convención
    temporal; se eligió para que la onda plana lleve $e^{j(\omega t - \mathbf{k}\cdot\mathbf{r})}$.
    Para el curso (notación de Boyd en CLAUDE.md: $\tilde P = \epsilon_0[\chi^{(1)}\tilde E + \chi^{(2)}\tilde E^2 + \dots]$),
    cualquier resultado tomado de Saleh debe anotarse como "convención $e^{j\omega t}$" y
    convertirse con $j \to -i$.

### 2. Transformadas de pulsos y producto tiempo–ancho de banda

- La Tabla A.2-1 [p. 1125] da los pares que más usa el curso: gaussiana ↔ gaussiana,
  $\mathrm{sech}(\pi t) \leftrightarrow \mathrm{sech}(\pi\nu)$ (perfil del solitón fundamental de
  Agrawal), chirp $\exp(j\pi t^2)$ (pulso con chirp lineal / propagación dispersiva), peine de
  impulsos ↔ peine (trenes de pulsos de láseres de modos bloqueados, peines de frecuencia) y
  $M$ impulsos ↔ $\sin(M\pi\nu)/\sin(\pi\nu)$ (espectro de un tren finito).
- Relación de reciprocidad (A.2-3)/(A.2-5): $\sigma_t\sigma_\nu \ge 1/4\pi$, $\sigma_t\sigma_\omega \ge 1/2$,
  mínimo para la gaussiana [p. 1126]. En FWHM (derivado arriba): $\Delta t\,\Delta\nu \ge 0.441$
  para gaussiana; para sech², Agrawal da $0.315$ (no está en Saleh). Esto es el criterio de pulso
  "limitado por transformada" que se usa al analizar SPM, compresión de pulsos y supercontinuo.
- Anchos a 3 dB, $1/e$ y FWHM y sus conversiones (A.2-14)–(A.2-18) [p. 1128]: la lorentziana
  $2\tau/[1+(2\pi\nu\tau)^2]$ con $\Delta\nu_{\rm FWHM} = 1/\pi\tau$ es la forma de línea homogénea
  (decaimiento exponencial $\exp(-|t|/\tau)$ del dipolo); aparece en la susceptibilidad resonante
  de Boyd cap. 3 y 6 y en el modelo de Lorentz (B.1-9)–(B.1-13).
- Escalamiento [p. 1123]: $f(t/\tau) \leftrightarrow |\tau|F(\tau\nu)$ es la regla para pasar de las
  tablas normalizadas a pulsos de duración $\tau$ real.

### 3. Sistemas lineales, Kramers–Kronig y el oscilador de Lorentz (Taller 2: dispersión)

- (B.1-6)–(B.1-7) [p. 1134] son las relaciones de **Kramers–Kronig** para la función de transferencia
  de cualquier sistema lineal causal con $h(t)$ real; aplicadas a $\chi(\nu) = \chi'(\nu) + j\chi''(\nu)$
  (ver $\mathrm{x}(t)$ = TF inversa de $\chi(\nu)$, p. 1153) dan la relación índice–absorción que se
  usa en el tema de dispersión del Taller 2 y en Boyd §1.7 (con la salvedad de signo del punto 1).
- El oscilador armónico (B.1-8)–(B.1-13) [pp. 1134–1135] es el **modelo de Lorentz** del medio
  dieléctrico: $H(\nu) \propto 1/(\nu_0^2 - \nu^2 + j\nu\Delta\nu)$, aproximación lorentziana cerca de
  resonancia (B.1-12) y relación dispersiva (B.1-13) $H' = 2[(\nu-\nu_0)/\Delta\nu]H''$. Boyd
  §1.4 obtiene $\chi^{(2)}$, $\chi^{(3)}$ añadiendo términos anarmónicos a esta misma ecuación; la
  parte lineal es exactamente (B.1-9) con $\Delta\nu = \sigma/2\pi$ ($\sigma$ = amortiguamiento,
  llamado $2\gamma$ en Boyd).
- El "sistema con chirp" $H(\nu) = \exp(-j\pi\nu^2)$ [p. 1133] es el propagador de dispersión de
  segundo orden: en Agrawal, $\tilde A(z,\omega) = \tilde A(0,\omega)\exp(i\beta_2\omega^2 z/2)$.
  Identificando $\pi\nu^2 \leftrightarrow \beta_2\omega^2 z/2$ se obtiene la longitud de dispersión.
- Sistemas 2D (B.2) y función de transferencia espacial [pp. 1135–1136]: propagación en espacio libre y
  óptica de Fourier; relevante si en el proyecto final se analiza el acoplamiento espacial a la guía o
  patrones de campo lejano, no para la dinámica no lineal temporal.

### 4. Modos de guías y resonadores (proyecto final)

- Apéndice C formaliza lo que calcula el solver FDE de Lumerical MODE: la ecuación (C.1-10)
  $\nabla\times[\eta\nabla\times\mathbf{H}] = (\omega^2/c_o^2)\mathbf{H}$ con $\eta = \epsilon_o/\epsilon(\mathbf{r})$
  es un problema de autovalores hermítico [p. 1141]; en una guía invariante en $z$ los modos son
  armónicos en $z$ con autovalor $\exp(-j\beta_q z)$ y perfil transversal fijo [p. 1141]. $n_{\rm eff} = \beta_q/k_o$
  y $n_g$ (lista de símbolos: $N$ = índice de grupo, $v$ = velocidad de grupo) son lo que
  `modos.py` extrae para el anillo de `seccion_v1`.
- Operadores hermíticos ⇒ autovalores reales y modos ortogonales [p. 1138]: justifica la
  descomposición modal y el cálculo de solapes (overlap) entre el modo del anillo y el del bus, y el
  principio variacional explica por qué el modo fundamental concentra el campo en el núcleo de alto
  índice.
- Modos de un resonador por operador integral (C.1-7) y modos Hermite–Gauss [p. 1140]: marco para
  el anillo add-drop como sistema de "una vuelta" cuyo modo se autorreproduce con autovalor
  $|h|e^{-j\varphi}$ ($h$ = factor de atenuación por vuelta, lista de símbolos p. 1145); de ahí salen
  resonancia, FSR y $Q$ (símbolos $\nu_F$, $\tau_p$, $Q$).
- Sistemas binarios (C.1-3) con matriz $2\times2$ [p. 1138]: matrices de Jones (polarización TE/TM
  del Taller 2), matrices de transferencia multicapa y acopladores direccionales (coeficiente
  $\mathcal{C}$, longitud $L_0 = \pi/2\mathcal{C}$); el acoplador bus-anillo se modela así.
- Medios periódicos y ondas de Bloch [p. 1141]: base conceptual de redes de Bragg, QPM (PPLN) y
  cristales fotónicos; relevante para el tema de ajuste de fase cuasi ($\Lambda$ = periodo) en
  $\chi^{(2)}$.

### 5. Símbolos que conviene fijar para el curso (con unidades del libro)

$\mathrm{d}$, $\mathrm{d}_{ijk}$, $\mathrm{d}_{iJ}$ [C·V⁻²]; $\chi^{(3)}$, $\chi^{(3)}_{ijkl}$ [C·m·V⁻³];
$\mathcal{P}_{\rm NL}$ [C·m⁻²]; $n_2$ [m²·W⁻¹]; $\mathfrak{r}_{ijk}$ [m·V⁻¹]; $\mathfrak{s}_{ijkl}$
[m²·V⁻²]; $\beta$, $\beta'$, $\beta''$, $D_\lambda$, $D_\nu$ (dispersión); $\gamma$ (coeficiente no
lineal de solitones); $\xi$ (acoplamiento FWM); $L_c$ (longitud de coherencia paramétrica);
$\Lambda$ (periodo de QPM); $\nu_S$, $\nu_A$, $\nu_R$, $\nu_B$ (desplazamientos Stokes/anti-Stokes,
Raman, Brillouin); acrónimos SHG, SFG, THG, FWM, SPM, XPM, SRS, SBS, SCG, OPA, OPO, SPDC, QPM, PPLN,
SSFS. Las unidades de $\mathrm{d}$ y $\chi^{(3)}$ en Saleh (C·V⁻², C·m·V⁻³) corresponden a definir
$\mathcal{P}_{\rm NL} = 2\mathrm{d}\mathcal{E}^2 + 4\chi^{(3)}\mathcal{E}^3$ sin el factor $\epsilon_0$
delante; en la convención del curso (Boyd, $P = \epsilon_0\chi^{(2)}E^2$) $\chi^{(2)}$ y $\chi^{(3)}$
quedan en m/V y m²/V². Hay que convertir ($\chi^{(2)}_{\rm Boyd} = 2\mathrm{d}_{\rm Saleh}/\epsilon_0$,
$\chi^{(3)}_{\rm Boyd} = 4\chi^{(3)}_{\rm Saleh}/\epsilon_0$; verificar contra Saleh cap. 21 antes de usarlo,
pues esta equivalencia la infiero de las unidades y no de estas páginas).
