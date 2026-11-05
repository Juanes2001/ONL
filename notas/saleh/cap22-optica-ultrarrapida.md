# Capítulo 22 — Ultrafast Optics (Saleh & Teich, 2.ª ed.)

Páginas del libro 936–1015 (PDF 958–1037). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 22.
Convención del libro: dependencia temporal $e^{j\omega t}$ con $j=\sqrt{-1}$; función de onda compleja
$U(\mathbf r,t)$ normalizada tal que $I=|U|^2$ (W/m²); envolvente compleja $\mathcal A(t)$ (caligráfica),
amplitudes complejas en negrita; transformada de Fourier $V(\nu)=\int U(t)\,e^{-j2\pi\nu t}\,dt$.
Los nombres de las secciones y los números de ecuaciones son los del libro. Las secciones marcadas con
`*` son las que el libro marca como avanzadas/opcionales.

---

## Resumen del capítulo

El capítulo trata la óptica de pulsos ultracortos (ps–fs–as). Parte de la descripción temporal y
espectral de un pulso (envolvente compleja, intensidad, fase, frecuencia instantánea, chirp,
espectrograma) y del pulso gaussiano con chirp como modelo analítico (§22.1). Luego describe el
filtrado lineal de pulsos por sistemas dispersivos, reduciéndolo a un retardo de grupo más un
**filtro de chirp** (fase cuadrática en frecuencia, coeficiente $b$) y mostrando cómo tal filtro
ensancha o comprime pulsos gaussianos con chirp; se presentan implementaciones con prismas, redes de
difracción y redes de Bragg chirpeadas, y la compresión mediante modulador de fase cuadrática
(QPM) + filtro de chirp (§22.2). La §22.3 aplica esto a la fibra óptica: el medio dispersivo es un
filtro de chirp con $b=D_\nu z/\pi$, de donde salen la longitud de dispersión $z_0=\pi\tau_0^2/D_\nu$,
el ensanchamiento $\tau(z)=\tau_0\sqrt{1+(z/z_0)^2}$, el chirp $a(z)=z/z_0$, la ecuación de
difusión de la envolvente lenta (SVE) y la analogía dispersión–difracción (QPM ≡ lente temporal).
La §22.4 trata la óptica lineal de pulsos ultra-estrechos donde espacio y tiempo se acoplan (óptica
de rayos, de Fourier y de haces). La §22.5 cubre la óptica no lineal pulsada: procesos paramétricos
con pulsos (SHG, desfase por velocidad de grupo), la NLSE y los solitones ópticos (orden, periodo,
potencia), y la generación de supercontinuo. La §22.6 describe la detección de pulsos con detectores
"lentos": autocorrelación de intensidad, medición espectral, medición de fase (SPIDER) y
espectrograma (FROG).

---

## Secciones

### 22.1 Pulse Characteristics (p. 937)

#### Introducción al capítulo (p. 937)

- "Ultrafast"/"ultrashort" en óptica: pulsos de ns, ps, fs y más cortos. En electrónica un pulso de
  1 ns ya tiene ancho espectral de GHz; un pulso de 1 ps tendría ancho THz y uno de fs cubriría cientos
  de THz (del 0 Hz al borde del visible ≈ 0.3 µm), con incertidumbre de energía $\Delta E\,\Delta t\ge h/2$
  mayor de 1.5 eV (del orden de la banda prohibida de semiconductores), lo que hace inviable la
  electrónica convencional a esas escalas (p. 937).
- Los pulsos de láseres conmutados o con mode-locking (§15.4) se comprimen y reconforman con
  componentes dispersivos lineales y no lineales (p. 937).

#### 22.1A Temporal and Spectral Characteristics (p. 937)

**Representaciones temporal y espectral (p. 938).** Función de onda compleja
$U(t)=\mathcal A(t)\exp(j\omega_0 t)$, con $\mathcal A(t)$ la envolvente compleja y
$\omega_0=2\pi\nu_0$ la frecuencia angular central. $\mathcal A(t)=|\mathcal A(t)|\exp[j\varphi(t)]$,
de modo que $U(t)=|\mathcal A(t)|\exp\{j[\omega_0 t+\varphi(t)]\}$. Intensidad
$I(t)=|U(t)|^2=|\mathcal A(t)|^2$ (W/m²); $\int I(t)\,dt$ es la **densidad de energía** (J/m²).

Perfiles típicos (p. 938): gaussiano $I(t)\propto\exp(-2t^2/\tau^2)$ (§22.1B); lorentziano
$I(t)\propto 1/(1+t^2/\tau^2)$; secante hiperbólica $I(t)\propto\operatorname{sech}^2(t/\tau)$
(solitones, §22.5B). $\tau$ es la constante de tiempo de cada perfil.

Dominio espectral: $V(\nu)=\int U(t)\exp(-j2\pi\nu t)\,dt=|V(\nu)|\exp[j\psi(\nu)]$;
$S(\nu)=|V(\nu)|^2$ es la **intensidad espectral** y $\psi(\nu)$ la **fase espectral**. $V(\nu)$ está
centrada en $\nu_0$ y se anula para $\nu<0$ (señal analítica, §2.6A). La transformada de la
envolvente, $A(\nu)=\int\mathcal A(t)\exp(-j2\pi\nu t)\,dt=V(\nu-\nu_0)$, está centrada en $\nu=0$.
Si el espectro es angosto, la envolvente varía poco dentro de un ciclo óptico $1/\nu_0$; no así para
pulsos ultra-estrechos (p. 938).

- **Fig. 22.1-1** (p. 938): (a) parte real de $U(t)$, $|\mathcal A(t)|$, $I(t)$ y $\varphi(t)$;
  (b) $S(\nu)$ y $\psi(\nu)$.

**Anchos temporal y espectral (p. 938).** Se definen sobre $I(t)$ y $S(\nu)$ con cualquiera de las
medidas del Apéndice A.2; salvo indicación contraria se usa el FWHM: $\tau_{\rm FWHM}$ y $\Delta\nu$.
Por la relación de Fourier, $\Delta\nu\propto 1/\tau_{\rm FWHM}$; para el gaussiano
$\tau_{\rm FWHM}\Delta\nu=0.44$.

- **Fig. 22.1-2** (p. 939): (a) recta $\Delta\nu=0.44/\tau_{\rm FWHM}$ desde 1 fs hasta 1 ns
  (regímenes "femtosecond / picosecond / nanosecond optics"); (b) ancho en longitud de onda
  $\Delta\lambda$ correspondiente para $\lambda_0=0.5,\ 1,\ 1.5$ µm. Ejemplo: un pulso de 10 fs tiene
  $\Delta\nu=44$ THz, i.e. $\Delta\lambda=37,\ 147,\ 331$ nm para $\lambda_0=0.5,\ 1,\ 1.5$ µm. La
  relación es lineal si $\Delta\nu\ll\nu_0$.

Conversión a longitud de onda (p. 939): $S_\lambda(\lambda)=S(\nu)|d\nu/d\lambda|=(c/\lambda^2)S(c/\lambda)$.
Si $\Delta\nu\ll\nu_0$, $\Delta\lambda\approx|d\lambda/d\nu|\Delta\nu$:

$$\boxed{\Delta\lambda\approx\frac{\lambda_0^2}{c}\,\Delta\nu}\qquad\text{(22.1-1) Spectral Width}$$

con $\lambda_0=c/\nu_0$. En unidades prácticas ($\Delta\nu$ en THz, $\lambda_0$ en µm, $\Delta\lambda$ en nm):

$$\Delta\lambda\approx 3.3\,\lambda_0^2\,\Delta\nu\qquad\text{(22.1-2)}$$

Ejemplo: $\Delta\nu=1$ THz ↔ $\Delta\lambda=1$ nm en $\lambda_0=0.55$ µm y 4 nm en 1.1 µm. Para pulsos
ultra-estrechos (gran $\Delta\nu$) la expresión exacta es

$$\Delta\lambda=\frac{c}{\nu_0-\Delta\nu/2}-\frac{c}{\nu_0+\Delta\nu/2}=\frac{\lambda_0^2}{c}\frac{\Delta\nu}{1-(\Delta\nu/2\nu_0)^2}\qquad\text{(22.1-3)}$$

aunque ahí el concepto de ancho espectral pierde sentido: un pulso de 2 fs tiene $\Delta\nu=220$ THz,
$\Delta\lambda=847$ nm en $\lambda_0=1$ µm (del visible al IR) (p. 939).

**Frecuencia instantánea (p. 939).** Derivada de la fase de $U(t)$:

$$\boxed{\omega_i=\omega_0+\frac{d\varphi}{dt},\qquad \nu_i=\nu_0+\frac{1}{2\pi}\frac{d\varphi}{dt}}\qquad\text{(22.1-4) Instantaneous Frequency}$$

Fase lineal $\varphi(t)=2\pi f t$ ⇒ desplazamiento fijo $\nu_i=\nu_0+f$; fase no lineal ⇒ frecuencia
instantánea dependiente del tiempo (p. 940).

**Pulsos con chirp (p. 940).** Un pulso está **chirpeado** (modulado en frecuencia, FM) si $\nu_i$
varía en el tiempo. Si $\nu_i$ crece con $t$ en el centro del pulso ($t=0$), i.e. $\varphi''>0$:
**up-chirped**; si decrece ($\varphi''<0$): **down-chirped**. Si la fase es cuadrática,
$\varphi(t)=at^2/\tau^2$, entonces $\nu_i=\nu_0+(a/\pi\tau^2)t$ es lineal en $t$ (**linealmente
chirpeado**) y $\varphi''=2a/\tau^2$. Se define el **parámetro de chirp**

$$\boxed{a=\tfrac12\varphi''\tau^2}\qquad\text{(22.1-5) Chirp Parameter}$$

Up-chirp si $a>0$, down-chirp si $a<0$. En $t=\tau/2$ la frecuencia instantánea ha aumentado
$a/2\pi\tau$, del orden de $a\Delta\nu$: $a$ mide la razón entre el cambio de frecuencia instantánea
en el semiancho y el ancho espectral $\Delta\nu$ (p. 940). Para fase arbitraria, $a$ representa el
chirp de orden más bajo (término cuadrático del desarrollo de Taylor alrededor del centro).

- **Fig. 22.1-3** (p. 940): pulsos de 20 fs y $\nu_0=300$ THz up-chirped (R→B: la frecuencia sube
  de 200 a 400 THz) y down-chirped (B→R).

**Espectro variable en el tiempo (p. 941).** La transformada de Fourier no dice *cuándo* ocurre cada
frecuencia. Con una ventana deslizante $W(t-\tau)$ de duración $T$ se define la **transformada de
Fourier de tiempo corto**:

$$\boxed{\Phi(\nu,\tau)=\int U(t)\,W(t-\tau)\exp(-j2\pi\nu t)\,dt}\qquad\text{(22.1-6) Short-Time Fourier Transform}$$

y su módulo al cuadrado $S(\nu,t)=|\Phi(\nu,t)|^2$ es el **espectrograma** (imagen tiempo–frecuencia).

- **Fig. 22.1-4** (p. 941): espectrograma de dos pulsos gaussianos de $\tau=60$ fs y $\nu_0=100$ THz,
  el primero up-chirped ($a=5$) y el segundo down-chirped ($a=-5$, menor amplitud); ventana gaussiana
  con $\tau=20$ fs. Se ven dos franjas inclinadas con pendientes opuestas.

#### 22.1B Gaussian and Chirped-Gaussian Pulses (p. 942)

**Pulso gaussiano limitado por transformada (p. 942).** Envolvente de fase constante y módulo gaussiano:

$$\mathcal A(t)=A_0\exp(-t^2/\tau^2)\qquad\text{(22.1-7)}$$

con $\tau$ real. $I(t)=I_0\exp(-2t^2/\tau^2)$, $I_0=|A_0|^2$, ancho total a $1/e$ igual a
$\sqrt2\tau$ y

$$\tau_{\rm FWHM}=\sqrt{2\ln2}\,\tau=1.18\tau\qquad\text{(22.1-8)}$$

$A(\nu)\propto\exp(-\pi^2\tau^2\nu^2)$, y la intensidad espectral

$$S(\nu)\propto\exp\left[-2\pi^2\tau^2(\nu-\nu_0)^2\right]\qquad\text{(22.1-9)}$$

con FWHM

$$\Delta\nu=0.375/\tau=0.44/\tau_{\rm FWHM}\qquad\text{(22.1-10)}$$

de modo que $\tau_{\rm FWHM}\Delta\nu=0.44$. El gaussiano sin chirp tiene el **mínimo producto
ancho temporal × ancho espectral** (Apéndice A.2): por eso se llama **transform-limited**
(Fourier-transform limited, bandwidth limited) (p. 942).

**Pulso gaussiano con chirp (p. 942).** $\mathcal A(t)=A_0\exp(-\alpha t^2)$ con
$\alpha=(1-ja)/\tau^2$ complejo ($\tau$, $a$ reales):

$$\mathcal A(t)=A_0\exp(-t^2/\tau^2)\exp(jat^2/\tau^2)\qquad\text{(22.1-11)}$$

Módulo gaussiano, intensidad gaussiana, fase cuadrática $\varphi=at^2/\tau^2$ ⇒ $\nu_i=\nu_0+at/\pi\tau^2$
(chirp lineal con parámetro $a$): up-chirp si $a>0$, down-chirp si $a<0$, sin chirp si $a=0$.
Transformada $A(\nu)\propto\exp(-\pi^2\nu^2/\alpha)$, también gaussiana;
$S(\nu)\propto\exp[-2\pi^2\tau^2(\nu-\nu_0)^2/(1+a^2)]$, con FWHM
$\Delta\nu=(0.375/\tau)\sqrt{1+a^2}=(0.44/\tau_{\rm FWHM})\sqrt{1+a^2}$: un factor $\sqrt{1+a^2}$
mayor que el del pulso sin chirp del mismo $\tau$. Producto
$\tau_{\rm FWHM}\Delta\nu=0.44\sqrt{1+a^2}$ ⇒ el gaussiano sin chirp ($a=0$) tiene el mínimo
producto. La fase espectral $\psi(\nu)\propto a\nu^2$ es cuadrática en frecuencia (p. 942).

**Tabla 22.1-1 (p. 943) — Propiedades temporales y espectrales de un pulso gaussiano con chirp**
(amplitud pico $A_0$, intensidad pico $I_0=|A_0|^2$, frecuencia central $\nu_0$, constante de
tiempo $\tau$, parámetro de chirp $a$):

| Magnitud | Expresión | Ec. |
|---|---|---|
| Envolvente compleja | $\mathcal A(t)=A_0\exp[-(1-ja)t^2/\tau^2]$ | (22.1-12) |
| Intensidad | $I(t)=I_0\exp(-2t^2/\tau^2)$ | (22.1-13) |
| Densidad de energía | $\int I(t)\,dt=\sqrt{\pi/2}\,I_0\tau$ | (22.1-14) |
| Semiancho a $1/e$ | $\tau_{1/e}=\sqrt2\,\tau$ | (22.1-15) |
| Ancho FWHM | $\tau_{\rm FWHM}=1.18\tau$ | (22.1-16) |
| Fase | $\varphi(t)=at^2/\tau^2$ | (22.1-17) |
| Transformada de Fourier | $A(\nu)=\dfrac{A_0\tau}{2\sqrt{\pi(1-ja)}}\exp\left[-\dfrac{\pi^2\tau^2\nu^2}{1-ja}\right]$ | (22.1-18) |
| Intensidad espectral | $S(\nu)=\dfrac{I_0\tau^2}{4\pi\sqrt{1+a^2}}\exp\left[-\dfrac{2\pi^2\tau^2(\nu-\nu_0)^2}{1+a^2}\right]$ | (22.1-19) |
| Semiancho espectral a $1/e$ | $\Delta\nu_{1/e}=\dfrac{2}{\tau}\sqrt{1+a^2}$ | (22.1-20) |
| Ancho espectral FWHM | $\Delta\nu=\dfrac{0.375}{\tau}\sqrt{1+a^2}=\dfrac{0.44}{\tau_{\rm FWHM}}\sqrt{1+a^2}$ | (22.1-21) |
| Fase espectral | $\psi(\nu)=-2\pi^2\tau^2[a/(1+a^2)]\nu^2$ | (22.1-22) |
| Frecuencia instantánea | $\nu_i=\nu_0+(a/\pi\tau^2)\,t$ | (22.1-23) |

Nota sobre (22.1-14): en la imagen el prefactor se lee como $\sqrt{\pi/2}\,I_0\tau$ (consistente con
$\int\exp(-2t^2/\tau^2)dt=\tau\sqrt{\pi/2}$).

- **Fig. 22.1-5** (p. 943): perfiles temporales y espectrales de tres pulsos gaussianos con
  $\nu_0=300$ THz ($\lambda=1$ µm, ciclo óptico 3.3 fs) y $\tau_{\rm FWHM}=5$ fs ($\tau=4.23$ fs).
  (a) Transform-limited: $\Delta\nu=88$ THz ($\Delta\lambda=73$ nm). (b) Up-chirped con $a=2$:
  $\Delta\nu$ es $\sqrt{1+a^2}=\sqrt5$ veces mayor, $\Delta\nu=197$ THz; $\nu_i=\nu_0(1\pm at/\pi\nu_0\tau)=300(1\pm0.497)$
  THz en $t=\pm\tau$; barrido de 151 a 449 THz entre $-\tau$ y $+\tau$ (λ de 0.67 a 1.99 µm).
  (c) Igual que (b) pero down-chirped, $a=-2$.

#### 22.1C Spatial Characteristics (p. 944)

En espacio libre o medio lineal homogéneo no dispersivo, $U(\mathbf r,t)$ obedece
$\nabla^2U-(1/c^2)\partial^2U/\partial t^2=0$. Soluciones exactas: onda plana pulsada y onda esférica
pulsada; además el haz gaussiano pulsado (aproximado). Estudio más detallado en §22.4.

**Onda plana pulsada (p. 944).** $U(\mathbf r,t)=\mathcal A(t-z/c)\exp[j\omega_0(t-z/c)]$, con
$\mathcal A(t)$ arbitraria; $I(t-z/c)$, $I(t)=|\mathcal A(t)|^2$. Si el ancho de $I(t)$ es $\tau$, el
pulso ocupa una distancia $\Delta z=c\tau$ y viaja sin cambio a velocidad $c$ (**Fig. 22.1-6**).

| Ancho temporal $\tau$ | 1 ns | 1 ps | 1 fs | 1 as |
|---|---|---|---|---|
| Ancho espacial $c\tau$ | 30 cm | 0.3 mm | 0.3 µm | 0.3 nm |

Onda plana a ángulo $\theta$ con $z$:
$U(\mathbf r,t)=\mathcal A[t-(x\sin\theta+z\cos\theta)/c]\exp[-jk_0(x\sin\theta+z\cos\theta)]\exp(j\omega_0 t)$;
en una instantánea (t fijo) el pulso es una franja brillante inclinada (**Fig. 22.1-7(a)**). Un pulso
de 100 fs es una franja de 30 µm. Una línea vertical ($z$ fijo) en una instantánea registra
$I(-x\sin\theta/c+\text{const})$: el perfil temporal se puede leer en el perfil espacial de la
instantánea, lo que se usa en detección (§22.5B) (p. 944).

**Onda esférica pulsada (p. 944).** $U(r,t)=(1/r)g(t-r/c)\exp[j\omega_0(t-r/c)]$; frentes de onda
esféricos concéntricos; en cada instante ocupa un cascarón de ancho radial $c\tau$ (**Fig. 22.1-7(b)**).

**\*Onda paraxial modulada por un pulso lento (p. 944–945).** Si la envolvente varía poco dentro de
un ciclo óptico: **envolvente lentamente variable (SVE)**, $\Delta\nu\ll\nu_0$, comportamiento
espacial ≈ el de la onda CW en $\nu_0$ (**onda pulsada cuasi-CW**). Si además es paraxial (§2.2C),
$U(\mathbf r,t)=\mathcal A(\mathbf r,t)\exp(-jk_0z)\exp(j\omega_0 t)$ con
$\partial^2\mathcal A/\partial z^2\ll k_0^2\mathcal A$ y $\partial^2\mathcal A/\partial t^2\ll\omega_0^2\mathcal A$;
la ecuación de onda da

$$\boxed{\nabla_T^2\mathcal A-j\frac{4\pi}{\lambda_0}\left(\frac{\partial\mathcal A}{\partial z}+\frac1c\frac{\partial\mathcal A}{\partial t}\right)=0}\qquad\text{(22.1-24) Paraxial SVE Equation}$$

con $\nabla_T^2=\partial^2/\partial x^2+\partial^2/\partial y^2$. Para CW ($\partial\mathcal A/\partial t=0$)
se recupera la ecuación paraxial de Helmholtz (2.2-23). Se verifica que
$\mathcal A(\rho,z,t)=g(t-z/c)\mathcal A_0(\mathbf r)$ la satisface si $\mathcal A_0$ cumple la
Helmholtz paraxial $\nabla_T^2\mathcal A_0-j(4\pi/\lambda_0)\partial\mathcal A_0/\partial z=0$: en
esta aproximación, una onda paraxial de longitud de onda $\lambda_0$ puede modularse con un pulso lento
de forma arbitraria sin alterar su comportamiento espacial (p. 945).

- **Fig. 22.1-7** (p. 945): instantáneas (cuatro tiempos) de (a) onda plana pulsada inclinada,
  (b) onda esférica pulsada, (c) haz gaussiano pulsado; cada instantánea contiene una línea de ancho
  $c\tau$.

**Haz gaussiano pulsado (p. 945).** En el caso cuasi-CW:

$$\mathcal A(\rho,z,t)=g(t-z/c)\frac{jz_0}{z+jz_0}\exp\left(-j\frac{\pi}{\lambda_0}\frac{\rho^2}{z+jz_0}\right)\qquad\text{(22.1-25)}$$

$g(t)$ función lenta arbitraria del tiempo retardado, $z_0$ rango de Rayleigh (longitud de difracción).
Salvo el retardo, no hay acoplamiento espacio–tiempo: el haz mantiene su perfil gaussiano y el pulso su
perfil temporal (Fig. 22.1-7(c)). Para pulsos ultra-estrechos (sin SVE) sí hay acoplamiento
espacio–tiempo y una onda gaussiana en ambos se vuelve no gaussiana al propagarse (§22.4) (p. 946).

---

### 22.2 Pulse Shaping and Compression (p. 946)

El perfil temporal de un pulso corto se altera inevitablemente al atravesar un sistema dispersivo,
porque sus componentes espectrales se atenúan y/o desfasan de manera distinta; el efecto es más
dramático cuanto más corto el pulso (mayor $\Delta\nu$). Esta sección considera solo efectos
temporales (ondas planas pulsadas) y sistemas lineales; los efectos espaciales van en §22.4 y la
dispersión en medios no lineales en §22.5 (p. 946).

#### 22.2A Chirp Filters (p. 946)

**Filtrado lineal de un pulso (p. 946).** Sistema lineal invariante en el tiempo con función de
transferencia $H(\nu)$ (Apéndice B):

$$V_2(\nu)=H(\nu)V_1(\nu)\qquad\text{(22.2-1)}$$

Solo importa $H(\nu)$ en la banda de ancho $\Delta\nu$ alrededor de $\nu_0$. Con
$U(t)=\mathcal A(t)\exp(j2\pi\nu_0t)$ y $V(\nu)=A(\nu-\nu_0)$, definiendo $f=\nu-\nu_0$:

$$A_2(f)=H_e(f)A_1(f)\qquad\text{(22.2-2)}$$

$$\boxed{H_e(f)=H(\nu_0+f)}\qquad\text{(22.2-3) Envelope Transfer Function}$$

(**Fig. 22.2-1**, p. 947: filtrar la función de onda con $H(\nu)$ ≡ filtrar la envolvente con
$H_e(f)$.) $H(\nu)=|H(\nu)|\exp[-j\Psi(\nu)]$, $H_e(f)=|H_e(f)|\exp[-j\Psi_e(f)]$ con
$\Psi_e(f)=\Psi(\nu_0+f)$. La fase del filtro suele ser más importante que el módulo; el capítulo
trata **filtros de fase** ($|H(\nu)|$ ≈ constante en la banda de interés). En el dominio del tiempo:

$$\mathcal A_2(t)=\int_{-\infty}^{\infty}h_e(t-t')\mathcal A_1(t')\,dt'\qquad\text{(22.2-4)}$$

con $h_e(t)$ la transformada inversa de $H_e(f)$ (p. 947).

**Filtro ideal (p. 947).** Conserva la forma, multiplica por una constante y retarda:

$$H_e(f)=H_0\exp(-j2\pi f\tau_d)\qquad\text{(22.2-5)}$$

$G=|H_0|^2$ ganancia/atenuación de intensidad, $\tau_d$ retardo; fase lineal
$\Psi_e(f)=\Psi_0+2\pi\tau_df$ (Fig. 22.2-2(a)). $\mathcal A_2(t)=H_0\mathcal A_1(t-\tau_d)$,
$I_2(t)=GI_1(t-\tau_d)$. Para un medio con coeficiente de atenuación $\alpha$, velocidad $c$ y
espesor $d$: $H_e(f)=\exp(-\alpha d/2)\exp(-j2\pi fd/c)$, $G=\exp(-\alpha d)$, $\tau_d=d/c$. Un
medio no dispersivo de índice $n$ ($c=c_0/n$): $H(\nu)=\exp(-\alpha d/2)\exp(-j\beta d)$ con
$\beta=2\pi\nu/c$. Si $\alpha$ y $n$ dependen de $\nu$ (medio dispersivo) el filtro no es ideal (§22.3).

**El filtro de chirp (p. 948).** El más importante en óptica ultrarrápida: filtro de fase con fase
cuadrática $\Psi_e(f)=b\pi^2f^2$ (Fig. 22.2-2(b)):

$$\boxed{H_e(f)=\exp(-jb\pi^2f^2)}\qquad\text{(22.2-6) Chirp-Filter Transfer Function}$$

$b$ real (unidades s²) es el **coeficiente de chirp** del filtro; $b>0$ **up-chirping**, $b<0$
**down-chirping**. Respuesta al impulso (Tabla A.2-1):

$$\boxed{h_e(t)=\frac{1}{\sqrt{j\pi b}}\exp(jt^2/b)}\qquad\text{(22.2-7) Chirp-Filter Impulse-Response Function}$$

también gaussiana con fase cuadrática en el tiempo (chirp lineal, up si $b>0$). Una cascada de dos
filtros de chirp $b_1$, $b_2$ equivale a uno con $b=b_1+b_2$: la acción de un filtro de chirp es
**reversible** con otro de signo contrario (p. 948). De (22.2-7) en (22.2-4):

$$\mathcal A_2(t)=\frac{1}{\sqrt{j\pi b}}\int_{-\infty}^{\infty}\mathcal A_1(t')\exp\left[j\frac{(t-t')^2}{b}\right]dt'\qquad\text{(22.2-8)}$$

matemáticamente similar a la difracción de Fresnel (4.3-12); para $b$ grande se vuelve similar a
Fraunhofer (una transformada de Fourier). La analogía difracción–dispersión se formaliza en §22.3D.

**Aproximación de un filtro de fase arbitrario por un filtro de chirp (p. 949).** Si módulo y fase
varían lentamente en la banda del pulso: $|H(\nu_0+f)|\approx|H(\nu_0)|\equiv|H_0|$ y
$\Psi(\nu_0+f)\approx\Psi_0+\Psi'f+\tfrac12\Psi''f^2$, con $\Psi_0=\Psi(\nu_0)$,
$\Psi'=d\Psi/d\nu|_{\nu_0}$, $\Psi''=d^2\Psi/d\nu^2|_{\nu_0}$:

$$H_e(f)\approx|H_0|\exp\left[-j\left(\Psi_0+\Psi'f+\tfrac12\Psi''f^2\right)\right]\qquad\text{(22.2-9)}$$

≡ cascada de un filtro ideal (constante $H_0=|H_0|\exp(-j\Psi_0)$ más un retardo) y un filtro de
chirp (**Fig. 22.2-3**):

$$\boxed{\tau_d=\Psi'/2\pi}\qquad\text{(22.2-10) Group Delay}$$

$$\boxed{b=\frac{\Psi''}{2\pi^2}}\qquad\text{(22.2-11) Chirp Coefficient}$$

Conclusión (p. 949): la principal fuente de distorsión en un sistema dispersivo con fase lenta es un
filtro de chirp. El término de tercer orden corresponde a un filtro de fase $\exp(-j\tfrac16\Psi'''f^3)$.

**Filtrado con chirp de un pulso gaussiano limitado por transformada (p. 950).** Entrada
$\mathcal A_1(t)=A_{10}\exp(-t^2/\tau_1^2)$, $A_1(f)=(A_{10}\tau_1/2\sqrt\pi)\exp(-\pi^2\tau_1^2f^2)$.
Salida:

$$A_2(f)=A_0\frac{\tau_1}{2\sqrt\pi}\exp[-\pi^2(\tau_1^2+jb)f^2]\qquad\text{(22.2-12)}$$

(en el libro el prefactor aparece como $A_0$; debe entenderse $A_{10}$). Se identifica con la
transformada (22.1-18) de un gaussiano chirpeado de ancho $\tau_2$ y chirp $a_2$:

$$A_2(f)=A_{20}\frac{\tau_2}{2\sqrt{\pi(1-ja_2)}}\exp\left(-\frac{\pi^2\tau_2^2f^2}{1-ja_2}\right)\qquad\text{(22.2-13)}$$

Igualando exponentes:

$$\tau_1^2+jb=\frac{\tau_2^2}{1-ja_2}\qquad\text{(22.2-14)}$$

y amplitudes $A_{20}=A_{10}\sqrt{1-ja_2}\,\tau_1/\tau_2$. Resultado (recuadro, p. 950):

$$\boxed{\begin{aligned}\text{Ancho}\quad&\tau_2=\tau_1\sqrt{1+b^2/\tau_1^4} &\text{(22.2-15)}\\\text{Chirp}\quad&a_2=b/\tau_1^2 &\text{(22.2-16)}\\\text{Amplitud}\quad&A_{20}=\frac{A_{10}}{\sqrt{1+jb/\tau_1^2}} &\text{(22.2-17)}\end{aligned}}$$

Conclusiones (p. 950–951):
- *El ancho aumenta* por el factor $\sqrt{1+a_2^2}=\sqrt{1+b^2/\tau_1^4}$. Para $|b|=\tau_1^2$ el
  factor es $\sqrt2$ (el filtro empieza a importar cuando $|b|$ ~ cuadrado del ancho). Para
  $|b|\gg\tau_1^2$, $\tau_2\approx|b|/\tau_1$: el ancho filtrado ∝ $|b|$ y ∝ $1/\tau_1$ — los pulsos
  más cortos se ensanchan más.
- *El pulso queda chirpeado* con $a_2\propto b$ y $\propto1/\tau_1^2$; up-chirp si $b>0$, down-chirp
  si $b<0$. Para $b=\tau_1^2$, $a_2=1$.
- *El ancho espectral no cambia*: $(0.375/\tau_2)\sqrt{1+a_2^2}=0.375/\tau_1=\Delta\nu$ (filtro de
  fase no altera $S(\nu)$). La compresión espectral por ensanchamiento temporal se compensa
  exactamente con el ensanchamiento espectral por chirp.
- **Fig. 22.2-4** (p. 951): $\tau_2/\tau_1$ y $a_2$ vs $b/\tau_1^2$.

**Filtrado con chirp de un pulso gaussiano con chirp (p. 951).** Entrada
$\mathcal A_1(t)=A_{10}\exp[-(1-ja_1)t^2/\tau_1^2]$, salida
$\mathcal A_2(t)=A_{20}\exp[-(1-ja_2)t^2/\tau_2^2]$ con

$$\frac{\tau_2^2}{1-ja_2}=\frac{\tau_1^2}{1-ja_1}+jb\qquad\text{(22.2-18)}$$

Separando partes real e imaginaria (p. 952):

$$\tau_2=\tau_1\sqrt{1+2a_1\frac{b}{\tau_1^2}+(1+a_1^2)\frac{b^2}{\tau_1^4}}\qquad\text{(22.2-19)}$$

$$a_2=a_1+(1+a_1^2)\frac{b}{\tau_1^2}\qquad\text{(22.2-20)}$$

Anulando $d\tau_2/db$ se obtiene el $b_{\min}$ que da el ancho mínimo $\tau_0$:

$$\boxed{\begin{aligned}\text{Ancho mínimo}\quad&\tau_0=\frac{\tau_1}{\sqrt{1+a_1^2}} &\text{(22.2-21)}\\\text{Coef. de chirp}\quad&b_{\min}=-a_1\tau_0^2=-\frac{a_1}{1+a_1^2}\tau_1^2 &\text{(22.2-22)}\end{aligned}}$$

y en términos de $b_{\min}$ y $\tau_0$:

$$\boxed{\begin{aligned}\text{Ancho}\quad&\tau_2=\tau_0\sqrt{1+(b-b_{\min})^2/\tau_0^4} &\text{(22.2-23)}\\\text{Chirp}\quad&a_2=(b-b_{\min})/\tau_0^2 &\text{(22.2-24)}\end{aligned}}$$

Para $b=b_{\min}$: $\tau_2=\tau_0$ y $a_2=0$ (máximamente comprimido y sin chirp). Si el pulso
original es up-chirped ($a_1>0$), $b_{\min}<0$: hace falta un filtro down-chirping para comprimir.
Si $a_1=0$, no se puede comprimir ($b_{\min}=0$, $\tau_0=\tau_1$). (22.2-23)–(22.2-24) son
(22.2-15)–(22.2-16) con $b\to b-b_{\min}$: las gráficas de la Fig. 22.2-4 valen con un corrimiento
horizontal $b_{\min}$ (p. 952).

- **Ejemplo 22.2-1 (p. 952–953). Compresión y expansión de un pulso chirpeado con un filtro de chirp.**
  (a) Gaussiano con $\tau_1$ y $a_1=-1$: $b_{\min}=\tfrac12\tau_1^2$, factor de compresión
  $\sqrt{1+a_1^2}=\sqrt2$, $\tau_0=\tau_1/\sqrt2$. Fig. 22.2-5(a): $\tau_2/\tau_0$ vs $b/\tau_0^2$;
  para $b>0$ pequeño se comprime y gana chirp positivo; compresión máxima en $b/\tau_0^2=1$
  ($b/\tau_1^2=0.5$); más allá se expande; para $b<0$ se expande con más down-chirp.
  (b) Up-chirped con $a_1=1$: un filtro up-chirping ($b>0$) lo expande ($a_2>1$); uno down-chirping
  lo comprime, máximo en $b/\tau_0^2=-1$ ($b/\tau_1^2=-0.5$) (Fig. 22.2-5(b)).
- **Fig. 22.2-5** (p. 953): $\tau_2/\tau_0$ y $a_2$ vs $b/\tau_0^2$ para $a_1=-1$ y $a_1=1$.

**Aplicación: amplificador de pulsos chirpeados (chirped pulse amplifier, p. 953).** Para evitar
saturación y autoenfoque en el amplificador, se estira el pulso con un filtro de chirp $b>0$ (baja la
potencia pico conservando la energía), se amplifica y luego se comprime con un filtro de chirp
$b<0$ de igual magnitud (**Fig. 22.2-6**).

#### 22.2B Implementations of Chirp Filters (p. 954)

Orígenes de dispersión en componentes ópticos (p. 954):
- **Dispersión material**: dependencia en frecuencia de $n$ y/o de la absorción.
- **Dispersión espacial**: *angular* (ángulo de deflexión dependiente de $\nu$: redes, elementos
  holográficos, prismas por dispersión material); *multitrayecto* (p. ej. **dispersión modal** en
  guías, §8.2); *interferométrica* (medios estratificados, redes de Bragg, resonadores);
  *difractiva* (difracción en aberturas pequeñas, esparcimiento en inhomogeneidades; incluye la
  **dispersión de guía de onda** en guías monomodo, §8.2).
- **Dispersión por polarización**: anisotropía dependiente de λ.
- **Dispersión no lineal**: dependencia en λ de efectos no lineales (SPM, interacciones paramétricas
  con conservación de energía y phase-matching dependientes de frecuencia).

**Filtros de chirp por dispersión angular (p. 954–955).** Un elemento desvía la componente de
frecuencia $\nu$ un ángulo $\theta(\nu)$ respecto a la de $\nu_0$ ($\theta(\nu_0)=0$). Si $\ell_0$ es
el camino óptico de la componente central, el de la componente $\nu$ es $\ell_0\cos\theta(\nu)$
(Fig. 22.2-7(a)):

$$\Psi(\nu)=\frac{2\pi\nu}{c}\ell_0\cos\theta(\nu)\qquad\text{(22.2-25)}$$

y $H(\nu)=\exp[-j\Psi(\nu)]$. Un haz pulsado se filtra con **cuatro elementos dispersivos
idénticos** (Fig. 22.2-7(b)): uno separa las componentes, otro invertido las devuelve a paralelas, y
dos más en orden inverso revierten el proceso; el sistema total es un filtro de fase con
$\Psi(\nu)=(2\pi\nu/c)\ell_0\cos\theta(\nu)$, con $\ell_0$ el camino total de la componente central.
Para $\theta$ pequeño, $\cos\theta\approx1-\tfrac12\theta^2$:

$$\Psi(\nu)\approx\frac{2\pi\nu}{c}\ell_0\left[1-\tfrac12\theta^2(\nu)\right]\qquad\text{(22.2-26)}$$

Derivadas en $\nu_0$:

$$\Psi'\approx\frac{2\pi}{c}\ell_0,\qquad\Psi''\approx-\frac{2\pi\nu}{c}\ell_0\left(\frac{d\theta}{d\nu}\right)^2\qquad\text{(22.2-27)}$$

Por (22.2-10)–(22.2-11): retardo $\tau_d=\ell_0/c$ y

$$\boxed{b\approx-\frac{\ell_0}{\pi\lambda_0}\alpha_\nu^2}\qquad\text{(22.2-28) Angular-Dispersion Chirp Coefficient}$$

con $\alpha_\nu=d\theta/d\nu$ el **coeficiente de dispersión angular**. Como $b<0$ siempre
(independiente del signo de $\alpha_\nu$), estos filtros son siempre **down-chirping** (p. 955).

- **Ejemplo 22.2-2 (p. 955–956). Filtro de chirp con prisma.** $\theta(\nu)=\theta_d(\nu)-\theta_d(\nu_0)$,
  $\alpha_\nu=(d\theta_d/dn)(dn/d\nu)$. Con $dn/d\nu=-(\lambda_0/\nu_0)dn/d\lambda_0=(n-N)/\nu_0$,
  donde $N=n-\lambda_0dn/d\lambda_0$ es el índice de grupo (§5.6):
  $$\alpha_\nu=\frac{n-N}{\nu_0}\frac{d\theta_d}{dn}\qquad\text{(22.2-29)}$$
  Para un prisma delgado de ángulo de ápice $\alpha$, $\theta_d=(n-1)\alpha$ (1.2-7), $d\theta_d/dn=\alpha$:
  $$\alpha_\nu=\frac{n-N}{\nu_0}\alpha\qquad\text{(22.2-30)}$$
  BK7 en $\lambda_0=800$ nm: $n=1.51$, $N=3.11$ [sic, así aparece en el libro], con $\alpha=15°$:
  $\alpha_\nu=1.11\times10^{-15}$ s = 1.11 fs. Para $\ell_0=1$ cm, (22.2-28) da
  $b=-5\times10^{-27}$ s² ≈ $-(71\text{ fs})^2$. Un pulso sin chirp de $\tau_1=50$ fs se ensancha
  por $(1+b^2/\tau_1^4)^{1/2}\approx2.23$ y queda con $a_2=b/\tau_1^2=2$ [sic; con $b<0$ el signo
  sería negativo, el libro escribe 2]. (**Fig. 22.2-8**: filtro de chirp de cuatro prismas.)
- **Ejemplo 22.2-3 (p. 956). Filtro de chirp con red de difracción.** Red de periodo $\Lambda$,
  ángulos de incidencia y difracción $\theta_1$, $\theta_2$ (2.4-13); $\theta_2=\theta_{20}+\theta(\nu)$:
  $$\sin\theta_1+\sin[\theta_{20}+\theta(\nu)]=\frac{\lambda}{\Lambda}=\frac{c}{\nu\Lambda}\qquad\text{(22.2-31)}$$
  Derivando en $\nu_0$:
  $$\alpha_\nu=\frac{d\theta}{d\nu}=\frac{-c}{\nu_0^2\Lambda\cos\theta_{20}}=\frac{-\lambda_0^2}{c\Lambda\cos\theta_{20}}\qquad\text{(22.2-32)}$$
  Caso simétrico $\theta_1=\theta_{20}$, $\sin\theta_{20}=\lambda_0/2\Lambda$:
  $$\alpha_\nu=-\frac1{\nu_0}\frac{\lambda_0}{\sqrt{\Lambda^2-(\lambda_0/2)^2}}\qquad\text{(22.2-33)}$$
  $$b=-\frac{\lambda_0\ell_0}{\pi c^2}\frac{\lambda_0^2}{\Lambda^2-(\lambda_0/2)^2}\qquad\text{(22.2-34)}$$
  Para $\lambda_0=800$ nm y $\Lambda=1.6$ µm: $\alpha_\nu=-2.72$ fs; con $\ell_0=10$ cm,
  $b=-2.94\times10^{-25}$ s² $=-(542\text{ fs})^2$. (**Fig. 22.2-9**: red de difracción como filtro
  down-chirping, cuatro redes.)

**Filtros de chirp con redes de Bragg (p. 957).** Una red de Bragg de periodo $\Lambda$ refleja
solo $\lambda$ con $\Lambda=m\lambda/2$ (§7.1C). Si el periodo varía con la posición (red chirpeada),
cada segmento refleja la longitud de onda que coincide con el periodo local, con distintos caminos:
filtro de fase dependiente de frecuencia. Con $\Lambda^{-1}(z)=\Lambda_0^{-1}+\xi z$ (frecuencia
lineal en $z$), la componente $\nu$ se refleja en $z$ tal que $\Lambda=mc/2\nu$, i.e.
$z=2\nu/mc\xi-1/\xi\Lambda_0$; recorre $2z$ y adquiere fase $\Psi=(2\pi\nu/c)(2z)$:

$$\Psi=(8\pi/mc^2\xi)\nu^2+(4\pi/c\xi\Lambda_0)\nu\qquad\text{(22.2-35)}$$

⇒ retardo $\tau_d=2/c\xi\Lambda_0$ y

$$\boxed{b=\frac{8}{m\pi\xi c^2}}\qquad\text{(22.2-36) Bragg-Grating Chirp Coefficient}$$

$\xi>0$ (frecuencia creciente, periodo decreciente, Fig. 22.2-10) ⇒ $b>0$ up-chirping; $\xi<0$ ⇒
down-chirping (p. 957).

#### 22.2C Pulse Compression (p. 957)

Un pulso limitado por transformada **no** se puede comprimir con un filtro de chirp (lo expande y
chirpea sin cambiar $\Delta\nu$). Sí se puede con un **modulador de fase cuadrática (QPM)** seguido
de un filtro de chirp: el QPM *multiplica* el pulso por $\exp(j\zeta t^2)$ ($\zeta$ constante), lo que
introduce chirp y ensancha el espectro sin alterar el ancho temporal; el filtro de chirp posterior
mantiene el nuevo espectro y comprime el ancho temporal a un nuevo pulso transform-limited (p. 957–958).

Con $\mathcal A(t)=A_0\exp(-t^2/\tau_1^2)$, el QPM da $\mathcal A_1(t)=A_{10}\exp[-(1-ja_1)t^2/\tau_1^2]$ con

$$a_1=\zeta\tau_1^2\qquad\text{(22.2-37)}$$

$\zeta>0$ ⇒ up-chirp, luego filtro down-chirping comprime; $\zeta<0$ ⇒ down-chirp, luego filtro
up-chirping. Factor de compresión $\sqrt{1+a_1^2}=\sqrt{1+\zeta^2\tau_1^4}$.

- **Fig. 22.2-11** (p. 958): QPM ($e^{j\zeta t^2}$) + filtro de chirp con $b=b_{\min}=-a_1\tau_1^2/(1+a_1^2)$.
  Tabla en la figura: ancho $\tau_1\to\tau_1\to\tau_0=\tau_1/\sqrt{1+a_1^2}$; chirp
  $0\to a_1=\zeta\tau_1^2\to0$; ancho espectral $\Delta\nu\to\Delta\nu\sqrt{1+a_1^2}\to\Delta\nu\sqrt{1+a_1^2}$.

Si el pulso original ya tiene chirp $a_1$, el QPM lo convierte en otro del mismo ancho con

$$\boxed{a_2=a_1+\zeta\tau_1^2}\qquad\text{(22.2-38) Effect of QPM on Chirp Parameter}$$

Un QPM con $\zeta$ de signo opuesto a $a_1$ puede deschirpear o invertir el chirp (p. 958).

**Resumen (recuadro, p. 958).** QPM y filtro de chirp son duales (uno es el análogo de Fourier del otro):

| | Operación | Efecto espectral | Efecto temporal |
|---|---|---|---|
| QPM | multiplicación por fase cuadrática | altera el ancho espectral | conserva el ancho temporal |
| Filtro de chirp | convolución con fase cuadrática | conserva el ancho espectral | altera el ancho temporal |

Los QPM se implementan con moduladores electro-ópticos (§20.1B), aunque producir $\exp(j\zeta t^2)$ no
es sencillo; o pasivamente por el **efecto Kerr óptico** (automodulación de fase, §22.5C) (p. 959).

#### 22.2D Pulse Shaping (p. 959)

Los filtros de chirp no sirven para dar forma arbitraria. Para eso: mapeo frecuencia→espacio o
tiempo→espacio con modulación espacial.

**Mapeo frecuencia–espacio (p. 959–960).** Red + lente ($f$) proyectan la transformada de Fourier
del perfil temporal como patrón espacial en el plano focal; un modulador (máscara litográfica u
holográfica, o SLM programable, §20.3B) modifica módulo y fase; una segunda lente + red recombinan
(transformada inversa). Equivale al filtrado espacial de la óptica de Fourier (§4.4B)
(**Fig. 22.2-12**). Si $\theta(\nu)$ es la deflexión de la red, la componente $\nu$ se enfoca en
$x=\theta(\nu)f$; una máscara $p(x)$ equivale a $H(\nu)=p[\theta(\nu)f]$; con $\theta(\nu)\approx\alpha_\nu\nu$
($\alpha_\nu$ de (22.2-32)):

$$H(\nu)=p(\alpha_\nu f\nu)\qquad\text{(22.2-39)}$$

Posición $x$ ↔ frecuencia $\nu=x/\alpha_\nu f$; ancho espectral $\Delta\nu$ ↔ ancho $X=\alpha_\nu f\Delta\nu$.
Para un haz de ancho finito $W$ en la red, cada componente tiene dispersión angular $\lambda/W=c/\nu W$,
i.e. extensión espacial $\delta x=f\lambda_0/W=cf/\nu W$ que limita la resolución: una máscara de ancho
$X$ tiene $M=X/\delta x=XW/(\lambda_0f)$ puntos independientes; $\delta x$ ↔ $\delta\nu=\lambda_0/(\alpha_\nu W)$
⇒ resolución espectral $M=XW/\lambda_0f$ puntos. Tecnologías de SLM: espejos deformables, arreglos de
cristal líquido (ms–sub-ms), deflectores acusto-ópticos (µs, bajo ciclo útil), arreglos
optoelectrónicos de semiconductor (ns) (p. 960).

**Mapeo tiempo–espacio (p. 960–961).** SLM pegado a una red, seguido de un sistema de lentes $2f$ con
un pinhole en eje en el plano de Fourier (**Fig. 22.2-13**). La red multiplica la componente $\nu$ (de
envolvente $A_1(\nu)$) por $\exp(j2\pi\gamma\nu x)$; el SLM modula con $p(x)$; el sistema de lentes
integra espacialmente:

$$A_2(\nu)\propto A_1(\nu)\int p(x)\exp(j2\pi\gamma\nu x)\,dx\propto A_1(\nu)P(-\gamma\nu)\qquad\text{(22.2-40)}$$

con $P(\nu_x)$ la transformada espacial de $p(x)$: sistema lineal con $H(\nu)\propto P(-\gamma\nu)$ ⇒

$$h(t)\propto p(-t/\gamma)\qquad\text{(22.2-41)}$$

La transmitancia del SLM en $x$ controla la respuesta al impulso en el único instante $t=-\gamma x$:
mapeo directo tiempo–espacio para sintetizar pulsos de fs con perfil arbitrario (p. 960).

---

### 22.3 Pulse Propagation in Optical Fibers (p. 960)

Propagación de un pulso en un medio lineal dispersivo extendido (fibra) vista como filtro lineal con
función de transferencia gobernada por $\beta(\nu)$; para envolventes lentas se aproxima por retardo +
filtro de chirp (§22.2A). Se deduce una ecuación diferencial para la envolvente y la analogía con la
difracción (p. 960–961).

#### 22.3A The Optical Fiber as a Chirp Filter (p. 961)

**El medio dispersivo como filtro (p. 961).** Una onda plana monocromática de frecuencia $\nu$ que
viaja $z$ sufre fase $\beta(\nu)z$, $\beta(\nu)=2\pi\nu n(\nu)/c_0$: multiplicación por
$\exp[-j\beta(\nu)z]$. Como una onda pulsada $U(z,t)$ es superposición de monocromáticas,
$H(\nu)=\exp[-j\beta(\nu)z]$ es la función de transferencia: $V(z,\nu)=\exp[-j\beta(\nu)z]V(0,\nu)$.
Con espectro angosto, $U(z,t)=\mathcal A(z,t)\exp(-j\beta_0z)\exp(j2\pi\nu_0t)$, $\beta_0=\beta(\nu_0)$;
$V(z,\nu)=A(z,\nu-\nu_0)\exp(-j\beta_0z)$ ⇒ $A(z,\nu-\nu_0)=A(0,\nu-\nu_0)\exp\{-j[\beta(\nu)-\beta(\nu_0)]z\}$.
Con $f=\nu-\nu_0$:

$$A(z,f)=H_e(f)A(0,f)\qquad\text{(22.3-1)}$$

$$\boxed{H_e(f)=\exp\{-j[\beta(\nu_0+f)-\beta(\nu_0)]z\}}\qquad\text{(22.3-2) Envelope Transfer Function}$$

Filtro de fase $H_e(f)=\exp[-j\Psi(f)]$ con $\Psi(f)=[\beta(\nu_0+f)-\beta(\nu_0)]z$ (**Fig. 22.3-1**,
p. 962: un medio dispersivo equivale a un filtro de fase sobre la envolvente).

**Aproximación por retardo + filtro de chirp (p. 962).** Si $\beta(\nu)$ varía lentamente en la banda
del pulso: $\Psi(f)\approx\Psi'f+\tfrac12\Psi''f^2$ ($\Psi(0)=0$):

$$H_e(f)\approx\exp[-j(\Psi'f+\tfrac12\Psi''f^2)]=\exp(-j2\pi\tau_df)\exp(-jb\pi^2f^2)\qquad\text{(22.3-3)}$$

con $\tau_d=\Psi'/2\pi$ y $b=\Psi''/2\pi^2$. Retardo de grupo
$\tau_d=\Psi'/2\pi=(1/2\pi)(d\beta/d\nu)z=(d\beta/d\omega)z=z/v$, con

$$\boxed{v=1/\beta'=\frac{c_0}{N}}\qquad\text{(22.3-4) Group Velocity }(\beta'=d\beta/d\omega)$$

la velocidad de grupo y $N=n-\lambda_0dn/d\lambda_0$ el índice de grupo (§5.6). El filtro de chirp
tiene $b=\Psi''/2\pi^2=(1/2\pi^2)(d^2\beta/d\nu^2)z=2\beta''z$, $\beta''=d^2\beta/d\omega^2$:

$$\boxed{b=2\beta''z=\frac{D_\nu}{\pi}z}\qquad\text{(22.3-5) Chirp Coefficient}$$

$$\boxed{D_\nu=2\pi\beta''=\frac{d}{d\nu}\left(\frac1v\right)=\frac{\lambda_0^3}{c_0^2}\frac{d^2n}{d\lambda_0^2}}\qquad\text{(22.3-6) GVD Coefficient }(\beta''=d^2\beta/d\omega^2)$$

$D_\nu$ es el **coeficiente de dispersión de velocidad de grupo (GVD)**: derivada del retardo de
grupo por unidad de longitud respecto a $\nu$ (§5.6). Unidades: s²/m (o s/m·Hz). $\beta''>0$
($D_\nu>0$): **dispersión normal** (GVD positiva), filtro up-chirping ($b>0$). $\beta''<0$
($D_\nu<0$): **dispersión anómala** (GVD negativa), filtro down-chirping ($b<0$) (p. 962–963).

- **Ejemplo 22.3-1 (p. 963). Filtro de chirp ajustable con dispersión angular y material en un
  prisma.** Si el rayo central atraviesa una longitud $L$ de prisma, la dispersión material añade
  $b=2\beta''L=D_\nu L/\pi$. BK7 en 800 nm: $D_\nu=0.284\times10^{-24}$ s²/m [así en el libro], con
  $L=1$ cm: $b=D_\nu L/\pi=+9\times10^{-28}$ s² = $+(30$ fs$)^2$. La contribución angular (Ej. 22.2-2)
  es $b\approx-(71$ fs$)^2$; la suma neta es negativa. $L$ se ajusta moviendo el prisma
  perpendicularmente a su base (**Fig. 22.3-2**).

**Resumen (recuadro, p. 963).** La propagación de un pulso en un medio dispersivo ≈ retardo con
velocidad de grupo $v=1/\beta'=c_0/N$ + filtro de chirp con $b=2\beta''z=D_\nu z/\pi$, proporcional a
$z$. $\beta'$, $\beta''$ son derivadas de $\beta$ respecto a $\omega$; $D_\nu=2\pi\beta''$ es el
coeficiente GVD.

#### 22.3B Propagation of a Gaussian Pulse in an Optical Fiber (p. 963)

**Pulso de entrada gaussiano limitado por transformada (p. 963–964).** Ancho $\tau_0$ en $z=0$. A
distancia $z$: retardo $\tau_d=z/v$ y filtro de chirp $b=D_\nu z/\pi$. Por (22.2-15)–(22.2-17) el
pulso sigue gaussiano con $\tau(z)=\tau_0[1+(D_\nu^2/\pi^2\tau_0^4)z^2]^{1/2}$, chirp
$a(z)=(D_\nu/\pi\tau_0^2)z$ y amplitud $A_0(z)=A_0[1-j(D_\nu/\pi\tau_0^2)z]^{-1/2}$. Definiendo $z_0$
tal que $D_\nu/\pi\tau_0^2=1/z_0$ se obtiene la Tabla 22.3-1. $|z_0|$ es la **longitud de dispersión**.

**Tabla 22.3-1 (p. 964) — Pulso gaussiano en un medio dispersivo** (velocidad de grupo $v$,
coeficiente $D_\nu$, parámetro de dispersión $z_0$; en $z=0$ transform-limited con ancho $\tau_0$,
amplitud $A_0$, $I_0=|A_0|^2$):

| Magnitud | Expresión | Ec. |
|---|---|---|
| Envolvente compleja | $\mathcal A(z,t)=A_0\sqrt{\dfrac{-jz_0}{z-jz_0}}\exp\left[j\dfrac{\pi}{D_\nu}\dfrac{(t-z/v)^2}{z-jz_0}\right]$ | (22.3-7) |
| Intensidad | $I(z,t)=I_0\dfrac{\tau_0}{\tau(z)}\exp\left[-2\dfrac{(t-z/v)^2}{\tau^2(z)}\right]$ | (22.3-8) |
| Densidad de energía | $\int I\,dt=\sqrt{\pi/2}\,I_0\tau_0$ | (22.3-9) |
| Ancho del pulso | $\tau(z)=\tau_0\sqrt{1+(z/z_0)^2}$ | (22.3-10) |
| Parámetro de chirp | $a(z)=z/z_0$ | (22.3-11) |
| Longitud de dispersión $\lvert z_0\rvert$ | $z_0=\pi\dfrac{\tau_0^2}{D_\nu}=\dfrac{\tau_0^2}{2\beta''}$ | (22.3-12) |
| Ancho espectral | $\Delta\nu=\dfrac{0.375}{\tau_0}$ | (22.3-13) |

Observaciones (p. 964–965):
- El centro del pulso se retrasa $z/v$: viaja a la velocidad de grupo $v=1/\beta'$.
- $\tau(z)$ es mínimo ($\tau_0$) en $z=0$ y crece con $|z|$ (Fig. 22.3-3). En $z=|z_0|$ se expande
  $\sqrt2$; en $z=\sqrt3|z_0|$ se duplica. Para $z\gg|z_0|$, $\tau(z)\approx\tau_0z/|z_0|=(|D_\nu|/\pi\tau_0)z$:
  expansión lineal a una tasa inversamente proporcional al ancho inicial. Con $\Delta\nu=0.375/\tau_0$:
  $\tau(z)\approx(1/0.375\pi)|D_\nu|\Delta\nu\,z=0.85|D_\nu|\Delta\nu\,z$ — $D_\nu$ es la tasa de
  ensanchamiento por unidad de distancia por unidad de ancho espectral (s/m·Hz). En términos de
  $D_\lambda$ [ps/km·nm]: $\tau(z)\approx0.85|D_\lambda|\Delta\lambda\,z$ (aprox. de (5.6-8)).
- El chirp $a(z)$ es 0 en $z=0$ y crece linealmente, alcanzando magnitud 1 en $z=|z_0|$. Signo de $a$
  = signo de $D_\nu$: dispersión normal ($D_\nu>0$) ⇒ up-chirp para $z>0$ (en el visible, "azul"
  viaja más lento que "rojo", consistente con up-chirp). Lo contrario para dispersión anómala.
- $|z_0|$ depende de $|D_\nu|$ y $\tau_0$: es la distancia a la que el ancho crece $\sqrt2$ y el chirp
  alcanza magnitud 1.
- $\Delta\nu=0.375/\tau_0$ no cambia (filtro de fase): la compresión espectral por expansión temporal
  se compensa con el ensanchamiento espectral por chirp.
- La densidad de energía es independiente de $z$ (medio sin pérdidas).
- **Fig. 22.3-3** (p. 965): $\tau(z)/\tau_0$ y $a(z)$ vs $z/z_0$ para un pulso inicialmente sin chirp
  en un medio con GVD positiva (sale up-chirped, R adelante y B detrás).

- **Ejemplo 22.3-2 (p. 965). Ensanchamiento de pulsos en vidrio BK7.** En $\lambda=620$ nm,
  $\beta''=1.02\times10^{-25}$ s²/m. Para 1 cm: $b=2\beta''z=2.04\times10^{-23}$ s² = (4.5 ps)². Un
  gaussiano de $\tau_0=4.5$ ps se expande $\sqrt2$ al cruzar la lámina. Para $\tau_0=100$ fs,
  $|z_0|=\tau_0^2/2|\beta''|=0.5$ mm [sic; con los números dados sale 0.049 mm ≈ 0.05 mm, el libro
  escribe 0.5 mm]; el pulso duplica su ancho en $\sqrt3z_0=0.87$ mm.

**Pulso de entrada gaussiano con chirp (p. 965–966).** Por (22.2-21), un gaussiano con $\tau_1$ y
$a_1$ en $z=0$ alcanza el ancho mínimo

$$\boxed{\tau_0=\frac{\tau_1}{\sqrt{1+a_1^2}}}\qquad\text{(22.3-14) Minimum Width}$$

a la distancia $z_{\min}$ con $(D_\nu/\pi)z_{\min}=b_{\min}$; de (22.2-22):

$$z_{\min}=-a_1\frac{\pi}{D_\nu}\tau_0^2\qquad\text{(22.3-15)}$$

$$\boxed{z_{\min}=-a_1z_0}\qquad\text{(22.3-16) Location of Minimum Width}$$

con $z_0=\pi\tau_0^2/D_\nu$. De (22.2-23)–(22.2-24):

$$\boxed{\begin{aligned}\tau(z)&=\tau_0\sqrt{1+(z-z_{\min})^2/z_0^2} &\text{(22.3-17)}\\a(z)&=(z-z_{\min})/z_0 &\text{(22.3-18)}\end{aligned}}$$

Idénticas a (22.3-10)–(22.3-11) con un corrimiento $z_{\min}$: la Tabla 22.3-1 vale universalmente
colocando el inicio del medio en la posición que corresponde al chirp inicial. Ejemplo: $z_0>0$
(dispersión normal) y $a_1=-1$ ⇒ $z_{\min}=z_0$, el medio empieza en $z=-z_0$; el pulso se comprime
$\sqrt2$, queda sin chirp en $z=z_0$ y luego se ensancha con up-chirp (**Fig. 22.3-4**, p. 966).

Casos (p. 967):
- Medio normal ($D_\nu>0$, $z_0>0$): pulso down-chirped ($a_1<0$) ⇒ $z_{\min}>0$, se comprime;
  up-chirped ($a_1>0$) ⇒ $z_{\min}<0$, no se comprime.
- Medio anómalo ($D_\nu<0$, $z_0<0$): up-chirped ⇒ $z_{\min}>0$, se comprime; down-chirped ⇒ no.
- **Resumen:** hay compresión si un pulso up-chirped viaja por un medio down-chirping (anómalo) o un
  pulso down-chirped por un medio up-chirping (normal).

**Compresión con QPM y medio dispersivo (p. 967–968).** Pulso inicial transform-limited de ancho
$\tau_1$; QPM $\exp(j\zeta t^2)$ ⇒ $a_1=\zeta\tau_1^2$, ancho espectral ×$\sqrt{1+a_1^2}$. Con
$\zeta<0$ y GVD positiva (o $\zeta>0$ y GVD negativa) hay compresión a

$$\tau_0=\frac{\tau_1}{\sqrt{1+a_1^2}}=\frac{\tau_1}{\sqrt{1+\zeta^2\tau_1^4}}\qquad\text{(22.3-19)}$$

en

$$z_{\min}=-a_1z_0=-\frac{\pi\tau_0^2}{D_\nu}a_1=-\frac{\pi}{D_\nu}\frac{\tau_1^2a_1}{1+a_1^2}=-\frac{\pi\zeta}{D_\nu}\frac{\tau_1^4}{1+\zeta^2\tau_1^4}\qquad\text{(22.3-20)}$$

positivo si $\zeta$ y $D_\nu$ tienen signos opuestos (**Fig. 22.3-5**). En el límite $a_1=\zeta\tau_1^2\gg1$:

$$\tau_0\approx\frac{\tau_1}{a_1}=\frac1{\zeta\tau_1}\qquad\text{(22.3-21)}$$

y $z_{\min}\approx f$ con

$$f=\frac{\pi}{-\zeta D_\nu}\qquad\text{(22.3-22)}$$

la **distancia focal** de este sistema de "enfoque de pulsos" (p. 968).

- **Ejemplo 22.3-3 (p. 968). Compresión de pulsos en fibra de sílice.** (a) Gaussiano con
  $\tau=100$ fs y $\lambda_0=850$ nm (Ti:zafiro) en fibra de sílice; dispersión normal con
  $D_\lambda=-200$ ps/km·nm (Fig. 5.6-5) ⇒ $D_\nu=-(\lambda_0^2/c_0)D_\lambda=+4.82\times10^{-25}$ s²/m.
  Sin chirp inicial, $\tau_0=100$ fs ⇒ $z_0=\pi\tau_0^2/D_\nu=6.52$ cm; ahí se expande $\sqrt2$ con
  $a=1$. En $z=6.52$ m: ×≈100 ⇒ 10 ps, $a=100$. (b) Con QPM $\exp(j\zeta t^2)$, $a_1=\zeta\tau^2$;
  para $\zeta=-10^{-2}$ (fs)⁻², $a_1=-1$ (down-chirp): se comprime a $\tau_0=100/\sqrt2=77$ fs
  [sic: $100/\sqrt2=70.7$ fs] en $z_{\min}=-a_1z_0=\pi\tau_0^2/D_\nu=3.26$ cm; luego se expande más
  rápido; en $z=6.52$ m el factor es ≈ $z/z_0=200$ ⇒ 14.1 ps.

- **Ejercicio 22.3-1 (p. 968). Compensación de dispersión en fibras.** El ensanchamiento se elimina
  balanceando dispersión normal y anómala. (a) Pulso sin chirp, $\lambda_0=1.55$ µm, $\tau_1=10$ ps,
  en fibra de sílice con dispersión anómala $D_\lambda=+20$ ps/km·nm. Determinar $\tau$ y $a$ en
  $d_1=100$ km. (b) Si se quiere comprimir de nuevo a 10 ps con otra fibra de longitud $d_2$ (Fig.
  22.3-6) con dispersión normal $D_\lambda=-100$ ps/km·nm, determinar $d_2$.
  (**Fig. 22.3-6**: $\tau(z)$ crece en el tramo GVD(+) [sic en la figura] y vuelve a $\tau_1$ en el
  tramo GVD(−); $a(z)$ sube a $a$ y baja a 0.)
- **Ejercicio 22.3-2 (p. 969). Compensación de dispersión con una secuencia periódica de moduladores
  de fase.** QPMs $\exp(j\zeta t^2)$ espaciados $2d$ en una fibra con GVD negativa y $\zeta>0$: el
  ancho y el chirp oscilan periódicamente (Fig. 22.3-7). Mostrar que la condición para el patrón
  periódico es
  $$\zeta=-\frac{2a}{\tau^2}=-\frac{2d/z_0}{\tau_0^2[1+(d/z_0)^2]}=-\frac{2D_\nu d}{\pi\tau_0^4[1+(D_\nu d/\pi\tau_0^2)^2]}\qquad\text{(22.3-23)}$$
  donde $\tau_0$ y $\tau$ son los anchos mínimo y máximo, $a$ el chirp y $z_0=\pi\tau_0^2/D_\nu$.
  (**Fig. 22.3-7**: $\tau(z)$ en dientes de sierra entre $\tau_0$ y $\tau_1$; $a(z)$ entre $-a$ y $a$.)

#### \*22.3C Slowly Varying Envelope Diffusion Equation (p. 969)

Con $H_e(f)=\exp(-j2\pi zf/v)\exp(-j\pi D_\nu zf^2)$ (aprox. cuadrática), la envolvente satisface

$$\frac{\partial^2\mathcal A}{\partial t^2}+j\frac{4\pi}{D_\nu}\left(\frac{\partial\mathcal A}{\partial z}+\frac1v\frac{\partial\mathcal A}{\partial t}\right)=0\qquad\text{(22.3-24)}$$

Ignorando el retardo $z/v$ (marco móvil con el pulso):

$$\boxed{\frac{\partial^2\mathcal A}{\partial t^2}+j\frac{4\pi}{D_\nu}\frac{\partial\mathcal A}{\partial z}=0}\qquad\text{(22.3-25) SVE Diffusion Equation}$$

que es la **ecuación de difusión**. (Equivalente a $\partial\mathcal A/\partial z=j(D_\nu/4\pi)\partial^2\mathcal A/\partial t^2$.)

*Demostración (p. 969)*: de $A(z,f)=A(0,f)H_e(z,f)\approx A(0,f)\exp[-j2\pi(z/v)f-j\pi D_\nu zf^2]$,
derivando en $z$: $(d/dz)A(z,f)\approx[-j2\pi f/v-j\pi D_\nu f^2]A(z,f)$; la transformada inversa de
$j2\pi fA$ y $(j2\pi f)^2A$ son $\partial\mathcal A/\partial t$ y $\partial^2\mathcal A/\partial t^2$,
lo que da (22.3-24).

Respuesta al impulso de la ecuación de difusión (p. 970):

$$h_e(t)=\frac1{\sqrt{jD_\nu z}}\exp\left(j\frac{\pi t^2}{D_\nu z}\right)\qquad\text{(22.3-26)}$$

idéntica a la del filtro de chirp (22.2-7) con $b=D_\nu z/\pi$. Para $\mathcal A(0,t)=A_0\exp(-t^2/\tau_0^2)$
la solución es gaussiana: $\mathcal A(z,t)=A_0\sqrt{-jz_0/(z-jz_0)}\exp[j(\pi/D_\nu)t^2/(z-jz_0)]$,
$z_0=\pi\tau_0^2/D_\nu$; con $t\to t-z/v$ se reproduce (22.3-7).

*\*Derivación desde Helmholtz (p. 970)*: de $[d^2/dz^2+\beta^2(\nu)]V(z,\nu)=0$ con
$V=A(z,\nu-\nu_0)\exp(-j\beta_0z)$ y la aproximación SVE
$d^2[A\exp(-j\beta_0z)]/dz^2\approx[-j2\beta_0dA/dz-\beta_0^2A]\exp(-j\beta_0z)$:
$-j2\beta_0dA/dz+[\beta^2(\nu_0+f)-\beta_0^2]A=0$; con dispersión débil
$\beta^2(\nu_0+f)-\beta_0^2\approx2\beta_0[\beta(\nu_0+f)-\beta_0]$ y
$\beta(\nu)\approx\beta_0+2\pi f\beta'+2\pi^2f^2\beta''$ se llega a $-jdA/dz+[2\pi f\beta'+2\pi^2f^2\beta'']A=0$,
cuya inversa de Fourier es $-j\partial\mathcal A/\partial z-j\beta'\partial\mathcal A/\partial t-\tfrac12\beta''\partial^2\mathcal A/\partial t^2=0$;
con $\beta'=1/v$ y $\beta''=D_\nu/2\pi$ se obtiene (22.3-24).

#### \*22.3D Analogy Between Dispersion and Diffraction (p. 970)

La ecuación de difusión SVE $\partial^2\mathcal A/\partial t^2+j(4\pi/D_\nu)\partial\mathcal A/\partial z=0$
(1D, marco móvil, sin términos de orden > 2) y la Helmholtz paraxial
$\nabla_T^2A-j(4\pi/\lambda)\partial A/\partial z=0$ (2D) son ambas ecuaciones de difusión: el
ensanchamiento temporal (dispersión) obedece la misma ley que el ensanchamiento espacial
(difracción), con $t$ en el papel de $\rho=(x,y)$ y $-D_\nu$ en el papel de $\lambda$. Si $t$ se mide
en unidades de distancia $ct$, el papel lo hace $c^2D_\nu$: para $D_\nu=10^{-23}$ s²/m,
$c^2D_\nu\approx0.9$ µm (equivale a 3 fs). La lente ($\exp(j\pi\rho^2/\lambda f)$) es análoga al QPM
($\exp(j\zeta t^2)=\exp[j\pi t^2/(-D_\nu f)]$, $\zeta=-\pi D_\nu f$ [sic en el texto; de la Tabla 22.3-2,
$f=\pi/(-D_\nu\zeta)$]): el QPM es una **lente temporal** que comprime el pulso a un mínimo en $z=f$
con $f=\pi/(-D_\nu\zeta)$, confirmando (22.3-22) (p. 970–971).

**Tabla 22.3-2 (p. 971) — Difracción (paraxial) vs dispersión (2.º orden)**

| | Difracción | | Dispersión |
|---|---|---|---|
| Envolvente | $A(\rho,z)$ | Envolvente | $\mathcal A(z,t)$ |
| Coord. transversal | $\rho=\sqrt{x^2+y^2}$ | Tiempo | $t$ |
| Coord. axial | $z$ | Coord. axial | $z$ |
| Helmholtz paraxial | $\nabla_T^2A-j\dfrac{4\pi}{\lambda}\dfrac{\partial A}{\partial z}=0$ | Difusión SVE (marco móvil) | $\dfrac{\partial^2\mathcal A}{\partial t^2}+j\dfrac{4\pi}{D_\nu}\dfrac{\partial\mathcal A}{\partial z}=0$ |
| Longitud de onda | $\lambda$ | Coef. de dispersión | $-D_\nu$ |
| Respuesta al impulso $h_e(\rho)$ | $\dfrac{j}{\lambda z}\exp\left(-j\dfrac{\pi\rho^2}{\lambda z}\right)$ | Respuesta al impulso $h_e(t)$ | $\dfrac1{\sqrt{jD_\nu z}}\exp\left(j\dfrac{\pi t^2}{D_\nu z}\right)$ |
| Lente | $\exp(j\pi\rho^2/\lambda f)$ | QPM | $\exp(j\zeta t^2)$ |
| Distancia focal | $f$ | Distancia focal | $f=\pi/(-D_\nu\zeta)$ |

**Tabla 22.3-3 (p. 971) — Haz gaussiano en espacio libre vs pulso gaussiano en medio dispersivo**

| | Haz gaussiano | | Pulso gaussiano |
|---|---|---|---|
| Ancho | $W(z)=W_0\sqrt{1+(z/z_0)^2}$ | Ancho | $\tau(z)=\tau_0\sqrt{1+(z/z_0)^2}$ |
| Longitud de difracción | $z_0=\pi W_0^2/\lambda$ | Longitud de dispersión | $\lvert z_0\rvert=\pi\tau_0^2/\lvert D_\nu\rvert$ |
| Ángulo de divergencia | $\theta_0=\lambda/\pi W_0$ | Tasa de ensanchamiento (s/m) | $\lvert D_\nu\rvert/\pi\tau_0$ |
| Curvatura del frente | $\dfrac1{R(z)}=\dfrac{2\pi}{\lambda}\dfrac{z}{z^2+z_0^2}$ | Tasa de chirp | $\varphi''=\dfrac{2\pi}{D_\nu}\dfrac{z}{z^2+z_0^2}$ |
| Chirp espacial | $a(z)=\dfrac{W^2(z)}{2R(z)}=\dfrac z{z_0}$ | Parámetro de chirp | $a(z)=\tfrac12\varphi''\tau^2(z)=\dfrac z{z_0}$ |

$z_0$ (dispersión) es análogo al rango de Rayleigh; pero mientras éste es siempre positivo, el de
dispersión es positivo para dispersión normal y negativo para anómala — de ahí el signo negativo en
la envolvente (22.3-7) (p. 971).

- **Fig. 22.3-8** (p. 972): analogías óptica espacial ↔ óptica temporal: (a) ensanchamiento (espacio
  libre ↔ GVD); (b) enfoque (lente ↔ QPM(+)·GVD(−)); (c) formación de imagen (GVD(−)·QPM(+)·GVD(−));
  (d) relevo (QPMs periódicos); (e) transformada de Fourier ($2f$ temporal: GVD(−)·QPM(+)·GVD(−)).
  En la columna derecha se asume GVD negativa; con GVD positiva el QPM debe ser negativo.

Consecuencias (p. 972–973):
- Ensanchamiento temporal ↔ difracción espacial.
- Compresión por QPM ↔ enfoque por lente: como una lente enfoca un haz a $W_1=(\lambda/\pi W_0)f$,
  el QPM comprime a $\tau_1=(-D_\nu/\pi\tau_0)f=1/\zeta\tau_0$ con $f=\pi/(-D_\nu\zeta)$. También
  enfoca dos pulsos estrechos separados en $z=0$ a uno solo en $z=f$.
- Imagen con una lente ↔ **lente temporal** que genera una réplica magnificada o reducida del perfil
  temporal (imagen temporal, Prob. 22.3-4).
- Relevo con lentes periódicas ↔ secuencia periódica de QPMs que mantiene el ancho.
- Sistema $2f$ de Fourier ↔ sistema $2f$ temporal con QPM: convierte un pulso modulado en fase en uno
  modulado en amplitud cuyo perfil temporal es la transformada de Fourier del original.
- Diferencia esencial: $\lambda>0$ siempre; $-D_\nu$ puede tener ambos signos. Un impulso de luz en un
  medio con $D_\nu<0$ (anómalo) se ensancha como pulso down-chirped; con $D_\nu>0$ (normal) como
  up-chirped. La difracción solo permite ondas divergentes (p. 973).

---

### 22.4 Ultrafast Linear Optics (p. 973)

Las características espaciales y temporales de las ondas pulsadas están intrínsecamente acopladas:
el ensanchamiento o enfoque espacial depende del perfil temporal inicial y la forma temporal depende
del perfil espacial. Esto es pronunciado para pulsos ultra-estrechos y sistemas con dispersión
angular. Solo la onda plana y la esférica mantienen *exactamente* su perfil temporal (§22.1C); con
envolvente lenta (cuasi-CW) los cambios temporal y espacial se desacoplan *aproximadamente*; para
pulsos ultra-estrechos esa aproximación falla. La sección estudia haces pulsados ultra-estrechos en
sistemas de imagen simples: primero con óptica de rayos, luego con óptica de ondas/Fourier (p. 973).

#### 22.4A Ray Optics (p. 973)

Los rayos viajan a $c=c_0/n$ (ley de Snell); en §9.3B se usó esto para estimar el ensanchamiento de
pulsos en fibras por la diferencia entre el camino más largo y el más corto. En componentes
dispersivos hay que usar la velocidad de grupo $v=c_0/N$ en lugar de la de fase $c=c_0/n$, con
$N=n-\lambda\,dn/d\lambda$ el índice de grupo: el ensanchamiento es la diferencia entre el mayor y
el menor retardo de grupo entre todos los caminos (p. 973–974).

**Ensanchamiento en un sistema de imagen de una lente (p. 974).** Pulso emitido en $P_1$, rayos que
se reúnen en el conjugado $P_2$ (Fig. 22.4-1). Si el vidrio no es dispersivo, por Fermat todos llegan
a la vez (sin ensanchamiento). Con dispersión se define el **retardo diferencial** = retardo de grupo
− retardo de fase, nulo en las partes no dispersivas del camino. Para un rayo en $(x,y)$ del plano de
la lente, con espesor $d(x,y)$:

$$\Delta\tau(x,y)=\left|\frac1c-\frac1v\right|d(x,y)=\frac{|n-N|}{c_0}d(x,y)\qquad\text{(22.4-1)}$$

Ancho del pulso ensanchado = diferencia entre máximo y mínimo de $\tau(x,y)$:

$$\Delta\tau(x,y)=|n-N|\frac{\Delta d}{c_0}\qquad\text{(22.4-2)}$$

con $\Delta d$ la diferencia entre espesor máximo y mínimo. Para lente delgada de focal $f$ y espesor
máximo $d_0$, con (2.4-6) y (2.4-10): $d(x,y)=d_0-(x^2+y^2)/2R=d_0-(x^2+y^2)/2(n-1)f$, así
$\Delta d=(D/2)^2/2(n-1)f$ ($D$ diámetro) y $\Delta\tau=[|n-N|/(n-1)](D/2)^2/2c_0f$:

$$\boxed{\Delta\tau=\frac{|n-N|}{n-1}\frac1{8F_\#^2}\frac f{c_0}}\qquad\text{(22.4-3) Pulse Spreading}$$

con $F_\#=f/D$ el número F. Ejemplo: lente BK7 en $\lambda=400$ nm, $n=1.53$,
$n-N=\lambda\,dn/d\lambda=-0.052$; $f=30$ mm, $F_\#=2$ ⇒ $\Delta\tau\approx307$ fs. El
ensanchamiento es resultado de la dispersión material diferencial por los múltiples caminos; sin
dispersión material, los múltiples caminos no ensanchan (Fermat) (p. 974–975).

#### \*22.4B Wave and Fourier Optics (p. 975)

Un haz monocromático estrecho se abre en un cono con ángulo ∝ λ y ∝ 1/ancho; cuando lo modula un
pulso ultracorto, cada componente de λ se abre en su propio cono (las de λ corta en conos más
estrechos). Lejos del eje hay menos energía de λ corta ⇒ corrimiento al rojo, compresión del ancho
espectral y ensanchamiento temporal (**Fig. 22.4-2**, p. 975). Las características espacial y
temporal se entrelazan en la propia propagación.

Enfoque de Fourier: $U(\mathbf r,t)$ se descompone en componentes monocromáticas
$V(\mathbf r,\nu)=\int U(\mathbf r,t)\exp(j2\pi\nu t)\,dt$ [así escrito en p. 975, con signo +],
cada una se propaga con las herramientas de los caps. 3–10 y se recombina por
$U(\mathbf r,t)=\int V(\mathbf r,\nu)\exp(-j2\pi\nu t)\,d\nu$.

**Óptica de Fourier de ondas pulsadas (p. 975–976).** Entre dos planos paralelos (1, 2) con sistema
lineal arbitrario:

$$V_2(x,y,\nu)=\iint h(x,x',y,y',\nu)V_1(x',y',\nu)\,dx'dy'\qquad\text{(22.4-4)}$$

con $h$ la respuesta al impulso a frecuencia $\nu$ (cap. 4). Respuestas al impulso con la dependencia
en $\nu$ explícita:
- **Espacio libre** (Fresnel, (4.1-18)), distancia $z$:
  $$h(x,x',y,y',\nu)\approx\frac{j\nu}{cz}\exp\left[-j\frac{2\pi\nu}{c}\frac{(x-x')^2+(y-y')^2}{2z}\right]\qquad\text{(22.4-5)}$$
  (se ignora $\exp(-j2\pi\nu z/c)$, retardo constante $z/c$).
- **Abertura**: multiplicación por la función de abertura (1 dentro, 0 fuera).
- **Lente** de focal $f$:
  $$t(x,y,\nu)\approx\exp\left(-jn\frac{2\pi\nu}{c_0}d_0\right)\exp\left(j\frac{2\pi\nu}{c_0}\frac{\rho^2}{2f}\right)\qquad\text{(22.4-6)}$$
  $$\frac1f=(n-1)\left(\frac1{R_1}-\frac1{R_2}\right)\qquad\text{(22.4-7)}$$
  Si $n$ depende de λ, $f$ depende de $\nu$: aberración cromática, importante en la distorsión de
  pulsos ultracortos.

**Sistema óptico de transformada de Fourier (p. 976–977).** Fraunhofer entre planos focales de una
lente (ignorando $y$):

$$h(x,x',\nu)\approx\frac{j\nu}{cz}\exp\left(-j\frac{2\pi\nu}{cf}xx'\right)\qquad\text{(22.4-8)}$$

Fuerte acoplamiento espacio-temporal. Caso separable $U_1(x,t)=g(t)p(x)$ (onda plana pulsada por un
SLM con transmitancia $p(x)$ independiente de la frecuencia, Fig. 22.4-3): $V_1(x,\nu)=G(\nu)p(x)$ y

$$V_2(x,\nu)\propto j\nu G(\nu)P(\nu x/cf)\qquad\text{(22.4-9)}$$

con $P(\nu_x)=\int p(x)\exp(j2\pi\nu_xx)\,dx$. Ya no es separable. En una posición fija $x_0$ del
plano de salida, la función de transferencia temporal es

$$H(\nu)\propto j\nu P(\nu x_0/cf)\qquad\text{(22.4-10)}$$

versión escalada de la transformada espacial de $p(x)$; la respuesta al impulso temporal:

$$\boxed{h(t)\propto p(tcf/x_0)}\qquad\text{(22.4-11) Space-to-Time Conversion}$$

La transmitancia del SLM en $x$ controla $h(t)$ en el único instante $t=(x_0/cf)x$: conversión
directa espacio→tiempo para conformar pulsos (cf. §22.2D) (**Fig. 22.4-3**, p. 977).

#### \*22.4C Beam Optics (p. 978)

**Haz gaussiano modulado por un pulso.** $U_1(x,y,t)=g(t)\exp(-\rho^2/W_0^2)$, $V_1\propto G(\nu)\exp(-\rho^2/W_0^2)$.
A distancia $z$, por (22.4-4) y (22.4-5):

$$V_2(x,y,\nu)\propto\nu G(\nu)\frac{jz_0(\nu)}{z+jz_0(\nu)}\exp\left(-j\frac{\pi\nu}{c}\frac{\rho^2}{z+jz_0(\nu)}\right)\qquad\text{(22.4-12)}$$

$$z_0(\nu)=\frac{\pi W_0^2}{c}\nu\qquad\text{(22.4-13)}$$

rango de Rayleigh a la frecuencia $\nu$ (la expresión (3.1-5) con la dependencia en frecuencia
explícita; $W(z)$ y $R(z)$ también dependen de $\nu$). Con espectro angosto, $\nu\approx\nu_0$ y la
dependencia es separable (22.1-25); para pulsos ultra-estrechos no. En general hace falta solución
numérica (p. 978).

**Haz gaussiano con pulso gaussiano (p. 978–980).** $g(t)=\exp(-t^2/\tau_0^2)\exp(j2\pi\nu_0t)$,
$G(\nu)\propto\exp[-\pi^2\tau_0^2(\nu-\nu_0)^2]$. En zona lejana ($z\gg z_0(\nu)$ para todo $\nu$):
$[z+jz_0(\nu)]^{-1}\approx z^{-1}[1-jz_0(\nu)/z]$ en el exponente, $z^{-1}$ en la amplitud:

$$V_2(x,y,\nu)\propto j\nu\exp[-\pi^2\tau_0^2(\nu-\nu_0)^2]\exp\left(-\pi^2\frac{W_0^2\rho^2}{c^2z^2}\nu^2\right)\exp\left(-j2\pi\nu\frac{\rho^2}{2cz}\right)\qquad\text{(22.4-14)}$$

Transformada inversa: la fase es un retardo $\rho^2/2cz$; $j\nu$ es una derivada $\partial/\partial t$;
las dos gaussianas en $\nu$ se combinan en una cuya inversa es gaussiana. Forma normalizada:

$$\boxed{U_2(x,y,t)\propto\frac{\exp[-\pi N\rho^2/(\rho^2+\rho_0^2)]}{1+\rho^2/\rho_0^2}\frac{\exp(-t_\rho^2/\tau_\rho^2)}{1+jt_\rho/\pi N\tau_0}\exp(-j2\pi\nu_\rho t_\rho)}\qquad\text{(22.4-15) Gaussian-Pulsed Gaussian Beam}$$

con (p. 979):

$$t_\rho=t-\rho^2/2cz=t-\pi N\tau_0(z/z_0)(\rho^2/2\rho_0^2)\qquad\text{(22.4-16) retardo dependiente de la posición}$$
$$\tau_\rho=\tau_0\sqrt{1+\rho^2/\rho_0^2}\qquad\text{(22.4-17) constante de tiempo dependiente de la posición}$$
$$\nu_\rho=\frac{\nu_0}{1+\rho^2/\rho_0^2}=\frac{N/\tau_0}{1+\rho^2/\rho_0^2}\qquad\text{(22.4-18) frecuencia central dependiente de la posición}$$
$$N=\nu_0\tau_0\qquad\text{(22.4-19) número de ciclos ópticos en el ancho }\tau_0$$
$$\rho_0=\pi NW(z)=\pi NW_0z/z_0\qquad\text{(22.4-20)}$$

con $W(z)=W_0z/z_0$ el radio de campo lejano del haz CW en $\nu_0$ y $z_0=\pi W_0^2/\lambda_0$. En
función de $\rho/\rho_0$ y $t/\tau_0$ la función de onda queda descrita por $N$ y $z/z_0$.
Intensidad:

$$I_2(x,y,t)\propto\frac{\exp[-2\pi N\rho^2/(\rho^2+\rho_0^2)]}{1+\rho^2/\rho_0^2}\frac{\exp(-2t_\rho^2/\tau_\rho^2)}{1+t_\rho^2/\pi^2N^2\tau_0^2}\qquad\text{(22.4-21)}$$

(función universal de $t/\tau_0$ y $\rho/\rho_0$ con un solo parámetro $N$). Intensidad espectral:

$$S_2(x,y,\nu)\propto\frac{\nu^2}{\nu_0^2}\exp\left[-2\pi^2N^2\frac{\rho^2}{\rho^2+\rho_0^2}\right]\exp\left[-2\pi^2N^2\frac{(\nu-\nu_\rho)^2}{\nu_\rho^2}\right]\qquad\text{(22.4-22)}$$

Características en zona lejana (p. 979–980; **Fig. 22.4-4**):
- Retardo $\rho^2/2cz$ = tiempo de viaje del centro del haz al punto $(\rho,z)$.
- Perfil temporal = gaussiana de ancho $\tau_\rho=\tau_0[1+\rho^2/\rho_0^2]^{1/2}$ × lorentziana de
  ancho $\pi N\tau_0$. El ancho gaussiano es $\tau_0$ en el eje y crece con $\rho$ ($\sqrt2\tau_0$ en
  $\rho=\rho_0$). La fase $\arctan(t_\rho/\pi N\tau_0)$ de la lorentziana es la manifestación del
  efecto Gouy (§3.1B) para haces gaussianos pulsados.
- La frecuencia central $\nu_\rho$ decrece monótonamente con $\rho$ desde $\nu_0$ hasta $\nu_0/2$ en
  $\rho=\rho_0$ (los componentes de λ larga se abren en conos más anchos, Fig. 22.4-2); lejos del eje
  el ancho espectral es menor y el temporal mayor.
- La distribución espacial, inicialmente de un solo pico, se aplana y se hace de dos picos al decaer
  con $t$.
- **Fig. 22.4-4** (p. 980): superficies $I_1(\rho,t)$ e $I_2(\rho,t)$ en campo lejano y $S_2(\rho,\nu)$,
  con $N=5$ ($\nu_0=750$ THz, $\lambda_0=400$ nm, $\tau_0=6.67$ fs); $W_0=1$ mm ⇒ $z_0=7.85$ m,
  $W_0z/z_0=5$ mm, $\rho_0\approx8$ cm.

**Enfoque de un haz pulsado (p. 980–981).** Haz $p(x,y)$ con pulso $g(t)$, lente $f$ y distancia $z$:

$$V_2(x,y,\nu)\propto G(\nu)\iint dx'dy'\,p(x',y')\exp\left(-j\frac{2\pi\nu}{c}d_0\right)\exp\left(j\frac{2\pi\nu}{c}\frac{x'^2+y'^2}{2f}\right)\exp\left(-j\frac{2\pi\nu}{c}\frac{(x-x')^2+(y-y')^2}{2z}\right)\qquad\text{(22.4-23)}$$

(lente con abertura mayor que el haz). Si la lente no es dispersiva, en el plano focal $z=f$:

$$V_2(x,y,\nu)\propto\nu G(\nu)P\left(\frac{\nu x}{cf},\frac{\nu y}{cf}\right)\exp\left(-j\frac{2\pi\nu}{c}\frac{\rho^2}{2f}\right)\qquad\text{(22.4-24)}$$

con $P(\nu_x,\nu_y)=\iint p(x,y)\exp[j2\pi(\nu_xx+\nu_yy)]\,dxdy$. En el tiempo:

$$U_2(x,y,t)\propto\int\nu G(\nu)P\left(\frac{\nu x}{cf},\frac{\nu y}{cf}\right)\exp\left[j2\pi\nu\left(t-\frac{\rho^2}{2cf}\right)\right]d\nu\qquad\text{(22.4-25)}$$

Hay retardo $t-\rho^2/2cf$ y la transformada del perfil espacial, escalada por $cf/\nu$, se promedia
sobre el espectro del pulso. Para gaussiano espacial $p=\exp(-\rho^2/W_0^2)$ y temporal:

$$V_2(x,y,\nu)\propto\nu\exp[-\pi^2\tau_0^2(\nu-\nu_0)^2]\exp\left[-\left(\frac{\pi W_0}{cf}\right)^2\nu^2\rho^2\right]\exp\left(-j2\pi\nu\frac{\rho^2}{2cf}\right)\qquad\text{(22.4-26)}$$

idéntica a (22.4-14) con $z=f$: valen (22.4-15)–(22.4-22) con $z=f$, $z_0$ del haz original, y

$$\rho_0=\pi NW_0f/z_0=N\lambda_0f/W_0=\pi NW_0'\qquad\text{(22.4-27)}$$

con $W_0'=\lambda_0f/\pi W_0$ el radio en el plano focal del haz CW. $\rho_0$ es $\pi N$ veces $W_0'$.
**Fig. 22.4-5** (p. 982): perfil espaciotemporal en el plano focal ($N=5$, $z_0\gg f$); la
diferencia con la Fig. 22.4-4 es que el retardo $\rho^2/2cf=\tau_0(\pi N/2)(f/z_0)(\rho^2/\rho_0^2)$
es despreciable para $f\ll z_0$ con $\rho<\rho_0$.

**\*Haces pulsados en medios dispersivos (p. 981–983).** En un medio lineal homogéneo la ecuación de
Helmholtz $[\nabla^2+\beta^2(\nu)]V(\mathbf r,\nu)=0$ describe difracción + dispersión para cualquier
$\beta(\nu)$ y cualquier $V(\mathbf r,\nu)$; luego transformada inversa. Con aproximaciones
paraxial + SVE (Tabla 22.3-2) se obtiene la **ecuación de onda paraxial generalizada**:

$$\boxed{-\lambda_0\nabla_T^2\mathcal A+D_\nu\frac{\partial^2\mathcal A}{\partial t^2}+j4\pi\left(\frac{\partial\mathcal A}{\partial z}+\frac1v\frac{\partial\mathcal A}{\partial t}\right)=0}\qquad\text{(22.4-28) Generalized Paraxial Wave Equation}$$

que generaliza (22.1-24) (medio no dispersivo, $D_\nu=0$) y (2.2-23) (CW). *Demostración (p. 982)*:
con $U=\mathcal A\exp(-j\beta_0z)\exp(j2\pi\nu_0t)$, $V(\mathbf r,\nu)=A(\mathbf r,\nu-\nu_0)\exp(-j\beta_0z)$
y la aproximación paraxial $(d^2/dz^2)[A\exp(-j\beta_0z)]\approx[-j2\beta_0dA/dz-\beta_0^2A]\exp(-j\beta_0z)$:

$$[\nabla_T^2-j2\beta_0\partial/\partial z]A+[\beta^2(\nu_0+f)-\beta_0^2]A=0\qquad\text{(22.4-29)}$$

Con dispersión débil, $\beta^2(\nu_0+f)-\beta_0^2\approx2\beta_0[\beta(\nu_0+f)-\beta_0]$ y
$\beta(\nu_0+f)=\beta_0+2\pi f\beta'+2\pi^2f^2\beta''$:

$$\nabla_T^2A-j2\beta_0\partial A/\partial z+2\beta_0[2\pi f\beta'+2\pi^2f^2\beta'']A=0\qquad\text{(22.4-30)}$$

Inversa de Fourier ($j2\pi f\to\partial/\partial t$, $-4\pi^2f^2\to\partial^2/\partial t^2$):

$$\nabla_T^2\mathcal A-2\beta_0\left[j\partial\mathcal A/\partial z+j\beta'\partial\mathcal A/\partial t+\tfrac12\beta''\partial^2\mathcal A/\partial t^2\right]=0\qquad\text{(22.4-31)}$$

y con $\beta'=1/v$, $\beta''=D_\nu/2\pi$, $\beta_0=2\pi/\lambda_0$ se obtiene (22.4-28).

Solución gaussiana espacio-temporal de (22.4-28):

$$A(x,y,z,t)=A_0\sqrt{\frac{-jz_0'}{z-jz_0'}}\exp\left[-j\frac{\pi}{D_\nu}\frac{t-z/v}{z-jz_0'}\right]\cdot\frac{jz_0}{z+jz_0}\exp\left(-j\frac{\pi}{\lambda}\frac{\rho^2}{z+jz_0}\right)\qquad\text{(22.4-32)}$$

[nota: en el libro el numerador del primer exponente aparece como $t-z/v$; por coherencia con (22.3-7)
debería ser $(t-z/v)^2$] con envolvente inicial $\mathcal A(x,y,0,t)=A_0\exp(-t^2/\tau_0^2)\exp(-\rho^2/W_0^2)$,
$z_0'=\pi\tau_0^2/D_\nu$ (longitud de dispersión) y $z_0=\pi W_0^2/\lambda$ (longitud de difracción).
Combina difracción (cap. 3) y dispersión (§22.3) de forma separable (**Fig. 22.4-6**, p. 983: tres
instantáneas, ensanchamiento transversal $W(z)$ por difracción y longitudinal $c\tau(z)$ por
dispersión). Como (22.4-28) y (22.4-32) son separables, sus aproximaciones equivalen a la cuasi-CW de
§22.1C.

**\*Ecuación de la envolvente para haz pulsado ultra-estrecho (p. 983).** Sin SVE, la dependencia
espacio-tiempo no es separable. De Helmholtz con $V=A(\mathbf r,\nu-\nu_0)\exp(-j\beta_0z)$,
$\nu=\nu_0+f$: $[\nabla_T^2+\partial^2/\partial z^2-j2\beta_0\partial/\partial z]A+[\beta^2(\nu_0+f)-\beta_0^2]A=0$;
expandiendo $\beta^2(\nu_0+f)-\beta_0^2\approx(2\beta_0\beta')2\pi f+\tfrac12(2\beta'^2+2\beta_0\beta'')(2\pi f)^2$:

$$-\lambda_0\nabla_T^2\mathcal A+D_\nu\frac{\partial^2\mathcal A}{\partial t^2}+j4\pi\left(\frac{\partial}{\partial z}+\frac1v\frac{\partial}{\partial t}\right)\mathcal A-\lambda_0\left(\frac{\partial^2}{\partial z^2}-\frac1{v^2}\frac{\partial^2}{\partial t^2}\right)\mathcal A=0\qquad\text{(22.4-33)}$$

con $v=1/\beta'$ y $D_\nu=2\pi\beta''$. Más general que (22.4-28) (sin aproximación paraxial ni de
dispersión débil). Si $\beta'^2\ll\beta_0\beta''$ (o $\lambda_0/v^2\ll D_\nu$) y
$\partial^2\mathcal A/\partial z^2\ll(4\pi/\lambda_0)\partial\mathcal A/\partial z$, el cuarto término es
despreciable y se recupera (22.4-28). En el marco móvil $t'=t-z/v$, $z'=z$:

$$-\lambda_0\nabla_T^2\mathcal A+D_\nu\frac{\partial^2\mathcal A}{\partial t'^2}+j4\pi\frac{\partial\mathcal A}{\partial z'}-\lambda_0\left(\frac{\partial^2\mathcal A}{\partial z'^2}-\frac2v\frac{\partial^2\mathcal A}{\partial t'\partial z'}\right)=0\qquad\text{(22.4-34)}$$

que exhibe claramente el acoplamiento espacio-temporal (término cruzado $\partial^2/\partial t'\partial z'$).

---

### 22.5 Ultrafast Nonlinear Optics (p. 984)

Las secciones anteriores trataron medios *lineales* (papel de la GVD). Aquí se consideran medios *no
lineales*: los efectos no lineales son más frecuentes con pulsos ultracortos por su alta intensidad.
Se revisitan la mezcla de tres ondas (χ⁽²⁾) y de dos y cuatro ondas (χ⁽³⁾) del cap. 21 para ondas
pulsadas. §22.5A procesos paramétricos pulsados (mezcla de tres ondas, rectificación óptica, SPM);
§22.5B solitones ópticos; §22.5C supercontinuo (p. 984).

#### 22.5A Pulsed Parametric Processes (p. 984)

Mezcla de tres ondas (§21.2C CW; teoría acoplada §21.4). Condiciones: conservación de energía y
momento con las frecuencias y vectores de onda centrales: $\omega_1+\omega_2=\omega_3$,
$\mathbf k_1+\mathbf k_2=\mathbf k_3$. Sin dispersión la teoría CW vale a cada instante (cuasi-CW) y
las envolventes obedecen las ecuaciones acopladas (21.4-20) (p. 984).

**Efecto walk-off (p. 984–985).** Con dispersión de primer orden (sin GVD), las tres ondas viajan a
sus velocidades de grupo sin cambiar forma; como difieren, los pulsos se separan y la mezcla cesa:
**walk-off**. Condición adicional para mezcla eficiente: $v_1=v_2=v_3$. **Fig. 22.5-1**: diagrama
espacio–tiempo de SHG colineal degenerado ($\omega_1=\omega_2=\omega$, $\omega_3=2\omega$), la SH es
más rápida y se separa. Es difícil cumplir a la vez phase matching y group-velocity matching. Con
error de phase matching $\Delta k$ la SHG decae en $L_c=2\pi/|\Delta k|$ (longitud de coherencia,
(21.2-28)). Con error de velocidad de grupo $\Delta\beta'=1/v_3-1/v_1$, el retardo tras $z$ es
$\Delta\beta'z=z/v_3-z/v_1$; cuando iguala el ancho $\tau$ los pulsos dejan de solaparse:

$$\boxed{L_g=\tau/|\Delta\beta'|}\qquad\text{(22.5-1) Walk-Off Length}$$

La menor de $L_c$ y $L_g$ dicta qué efecto domina. Ejemplo: KDP, fundamental ordinaria
$\lambda_1=1.06$ µm, SH extraordinaria $\lambda_3=0.5$ µm [sic], Type-II o-e-o:
$\Delta\beta'=2(1/v_3-1/v_1)\approx5.2\times10^{-10}$ s/m; para 100 fs, $L_g\approx0.2$ mm (p. 985).

**\*Ecuaciones acopladas para mezcla pulsada de tres ondas (p. 985–986).** Campos
$\mathcal E_q=\mathrm{Re}\{\sqrt{2\eta\hbar\omega_q}\,a_q(z,t)\exp[j(\omega_qt-\beta_qz)]\}$,
$q=1,2,3$, con $a_q$ envolventes normalizadas, $\beta_q$ constantes de propagación en $\omega_q$.
Con SVE y Taylor a dos términos $\beta(\omega_q+\Omega)\approx\beta_q+\Omega\beta_q'$:

$$\left(\frac{\partial}{\partial z}+\frac1{v_1}\frac{\partial}{\partial t}\right)a_1=-jga_3a_2^*,\quad\left(\frac{\partial}{\partial z}+\frac1{v_2}\frac{\partial}{\partial t}\right)a_2=-jga_3a_1^*,\quad\left(\frac{\partial}{\partial z}+\frac1{v_3}\frac{\partial}{\partial t}\right)a_3=-jga_1a_2\qquad\text{(22.5-2)}$$

con $v_q=1/\beta_q'$ y $g$ dado por (21.4-21). Si $v_1=v_2=v_3=v$, en el marco móvil se reducen a
las CW (21.4-20) con $z\to z-vt$. Con GVD (Prob. 22.5-2), Taylor a tres términos
$\beta(\omega_q+\Omega)\approx\beta_q+\Omega\beta_q'+\tfrac12\Omega^2\beta_q''$:

$$\left(\frac{\partial}{\partial z}+\frac1{v_q}\frac{\partial}{\partial t}-j\frac{\beta_q''}{2}\frac{\partial^2}{\partial t^2}\right)a_q=\text{(lado derecho de (22.5-2))},\quad q=1,2,3\qquad\text{(22.5-3)}$$

**Rectificación óptica pulsada: generación de pulsos THz (p. 986–987).** Un pulso óptico con ancho
espectral en el rango THz se convierte hacia abajo en un pulso THz, como si se rectificara
(**Fig. 22.5-2**: pulso óptico de 2 ps → pulso THz de ~2 ps). Para $\mathcal E(t)=\mathrm{Re}\{\mathcal A(t)\exp(j\omega_0t)\}$
en medio con coeficiente $\mathsf d$, la polarización $2\mathsf d\mathcal E^2(t)$ tiene un término en
$2\omega_0$ (SHG) y

$$\mathcal P_{\rm THz}=\mathsf d|\mathcal A(t)|^2\qquad\text{(22.5-4)}$$

(rectificación óptica, §21.2A, 21.2C, 21.4B). Por Fourier, pares $\omega_1=\omega$, $\omega_2=\omega+\Omega$
generan $P_{\rm THz}(\Omega)=2\mathsf dE^*(\omega)E(\omega+\Omega)$ y sumando:

$$P_{\rm THz}(\Omega)=\int2\mathsf dE^*(\omega)E(\omega+\Omega)\,d\omega\qquad\text{(22.5-5)}$$

(con dispersión no lineal, $\mathsf d\to\mathsf d(\Omega,\omega,\omega+\Omega)$, §21.7). Error de
phase matching:

$$\Delta k=k(\omega+\Omega)-k(\omega)-k(\Omega)\qquad\text{(22.5-6)}$$

Si $\Omega\ll\omega$:

$$\Delta k\approx\Omega\,dk/d\omega-k(\Omega)=\Omega[1/v(\omega)-1/c(\Omega)]=[N(\omega)-n(\Omega)]\Omega/c_0\qquad\text{(22.5-7)}$$

con $v(\omega)=(dk/d\omega)^{-1}$ y $N(\omega)$ índice de grupo óptico, $c(\Omega)$ y $n(\Omega)$
velocidad de fase e índice en THz. **Diseño: índice de grupo óptico = índice de refracción en THz.**
Para cristal de longitud $L$, el error es pequeño si $L<L_c=2\pi/|\Delta k|$; se incluye
$\int_0^L\exp(j\Delta kz)dz=[\exp(j\Delta kL)-1]/j\Delta k$ en (22.5-5) (p. 987).

**Automodulación de fase (SPM) de pulsos (p. 987–988).** En medios Kerr (§21.3A), tras distancia
$z$: $\Delta\varphi=-n_2Ik_0z$. Para un pulso, $I=I(t)$:

$$\Delta\varphi(t)=-n_2I(t)k_0z\qquad\text{(22.5-8)}$$

⇒ cambio de frecuencia instantánea (22.1-4):

$$\Delta\omega_i=-n_2\frac{dI}{dt}k_0z\qquad\text{(22.5-9)}$$

Con $n_2>0$: la mitad trasera ($dI/dt<0$) sube de frecuencia (azul), la delantera ($dI/dt>0$) baja
(rojo): el pulso queda **up-chirped** en su centro. SPM sirve para introducir chirp y conformar
pulsos (§22.2C) (**Fig. 22.5-3**, p. 987). Cerca del centro, gaussiano ≈ parábola
$I(t)=I_0\exp(-2t^2/\tau^2)\approx I_0[1-2t^2/\tau^2]$ ⇒ parte variable de la fase
$\Delta\varphi\approx2n_2I_0k_0zt^2/\tau^2$: chirp lineal con $a=2n_2I_0k_0z/\tau^2$, del mismo
signo que $n_2$. SPM es un QPM $\exp(jat^2/\tau^2)=\exp(j\zeta t^2)$ con

$$\zeta=2n_2I_0k_0z/\tau^2\qquad\text{(22.5-10)}$$

$$\boxed{a=z/z_{\rm NL},\qquad z_{\rm NL}=(2n_2I_0k_0)^{-1}}\qquad\text{(22.5-11) SPM Chirp Parameter}$$

$|z_{\rm NL}|$ es la **longitud característica no lineal** del medio Kerr: la fase introducida al
viajar $2|z_{\rm NL}|$ a intensidad pico $I_0$ es la unidad ($n_2I_0k_0\cdot2|z_{\rm NL}|=1$). Se
supuso GVD despreciable frente a SPM: $|z_0|\gg|z_{\rm NL}|$. La modulación de fase por SPM +
dispositivo dispersivo lineal (red, prismas) comprime por $\sqrt{1+a^2}=\sqrt{1+(z/z_{\rm NL})^2}$ (p. 988).

- **Ejemplo 22.5-1 (p. 988). Compresión con SPM de fibra y GVD de red.** Pulso de 65 fs, potencia
  pico $P_0=300$ kW, $\lambda_0=620$ nm, en fibra de sílice de 9 mm y área $A=100$ µm²
  (Fig. 22.5-4). $n_2\approx3.2\times10^{-20}$ m²/W ⇒ $|z_{\rm NL}|=|2n_2I_0k_0|^{-1}=\lambda_0A/4\pi|n_2|P_0\approx0.5$ mm.
  Con $z=9$ mm, $a=z/z_{\rm NL}=18$ ⇒ compresión máxima $\sqrt{1+a^2}\approx18$, pulso de 3.6 fs.
  GVD de la fibra: en 620 nm $\beta''=6\times10^{-26}$ s²/m ⇒ $z_0=\tau_0^2/2\beta''=3.5$ cm para
  $\tau_0=65$ fs; como $z_0\gg z_{\rm NL}$ la SPM domina. La red debe tener
  $b=[a/(1+a^2)]\tau_0^2\approx2.35\times10^{-28}$ s² = (3.6 fs)² [debe ser negativo para
  comprimir un pulso up-chirped; en la figura la red es "negative GVD"].
- **Fig. 22.5-4** (p. 988): fibra (SPM positiva) + red de difracción (GVD negativa).

#### 22.5B Optical Solitons (p. 988)

La interacción SPM + GVD en un medio Kerr dispersivo puede dar ensanchamiento o compresión netos
según magnitudes y signos. Bajo ciertas condiciones un pulso de forma e intensidad prescritas viaja
sin alterar su forma, como en un medio lineal no dispersivo: la GVD compensa por completo la SPM
(**Fig. 22.5-5(c)**). Son **ondas solitarias**; los **solitones** ópticos son ondas solitarias
ortogonales: al cruzarse no se alteran sus perfiles de intensidad (solo adquieren fases) (p. 988–989).

- **Fig. 22.5-5** (p. 989): (a) medio lineal con GVD negativa (anómala): B viaja más rápido que R ⇒
  ensanchamiento (down-chirp). (b) Medio no lineal no dispersivo con $n_2>0$: SPM pone R adelante y
  B atrás (up-chirp) sin cambiar la forma; si luego entra en (a), se comprime (B alcanza a R).
  (c) Medio no lineal dispersivo (GVD negativa + SPM positiva): onda solitaria.
- **Fig. 22.5-6** (p. 989): analogía de transporte (bicicleta lenta–carro pesado–deportivo rápido
  sobre un suelo elástico que el carro deforma: los tres viajan a la misma velocidad).

Los solitones tienen perfil y nivel de intensidad característicos para los que SPM y GVD se
equilibran; cualquier ensanchamiento refuerza la compresión y viceversa: son los **modos
(autofunciones) del sistema no lineal dispersivo** (p. 989–990).

**Condición de solitón (derivación simple, p. 990).** Igualar a cero la suma de fases introducidas
por SPM y GVD en $\Delta z$. SPM: QPM $\exp(j\zeta t^2)$ con $\zeta=2n_2I_0k_0\Delta z/\tau_0^2$
($I_0$, $\tau_0$ pico y ancho). GVD: fase $at^2/\tau_0^2$ con $a=\Delta z/z_0=2\beta''\Delta z/\tau_0^2$
(Tabla 22.3-1). Condición: fases iguales y opuestas:

$$\zeta=-\frac{a}{\tau_0^2}\qquad\text{(22.5-12)}$$

$$\boxed{k_0n_2I_0=-\frac{\beta''}{\tau_0^2}}\qquad\text{(22.5-13) Soliton Condition (Phase)}$$

$$\boxed{z_{\rm NL}=-z_0}\qquad\text{(22.5-14) Soliton Condition (Length)}$$

la longitud de dispersión iguala la longitud característica no lineal: la fase SPM en una distancia
$2|z_0|$ es la unidad ($-k_0n_2I_02z_0=1$). También se obtiene pensando en el medio como secuencia
periódica de elementos SPM y GVD (Fig. 22.5-7, idéntico al relevo del Ejercicio 22.3-2) en el límite
$\Delta z\to0$ (de (22.3-23)). En términos de la amplitud $A_0$ ($I_0=|A_0|^2/2\eta$, $\eta$
impedancia):

$$\boxed{A_0\tau_0=\sqrt{-\beta''/\gamma}}\qquad\text{(22.5-15) Soliton Condition (Area)}$$

$$\gamma=k_0n_2/2\eta=\pi n_2/\lambda_0\eta\qquad\text{(22.5-16)}$$

$\gamma$ y $\beta''$ de signos opuestos. Para un material dado $A_0\tau_0$ es fijo ⇒ (p. 991):
- Amplitud pico $A_0\propto1/\tau_0$.
- Potencia pico $\propto1/\tau_0^2$.
- Densidad de energía $\int I\,dt\propto1/\tau_0$: un solitón más corto lleva más energía.
- **Fig. 22.5-7** (p. 991): modelo con elementos SPM(+) y GVD(−) alternados; $\tau(z)$ oscila entre
  $\tau_0$ y $\tau_1$, $a(z)$ en dientes de sierra entre $-a$ y $a$.

Envolvente del solitón (p. 991):

$$\boxed{|\mathcal A(t)|=|A_0|\operatorname{sech}(t/\tau_0)}\qquad\text{(22.5-17) Soliton Envelope}$$

$\operatorname{sech}=1/\cosh$ (**Fig. 22.5-8**, p. 992: sech vs gaussiana de igual altura y FWHM):
amplitud pico $A_0$; FWHM del perfil de amplitud $2.63\tau_0$; área bajo el perfil de amplitud
$2\pi A_0\tau_0$; $I(t)\propto|A_0|^2\operatorname{sech}^2(t/\tau_0)$ con
$\tau_{\rm FWHM}=1.76\tau_0$.

**Ecuación de onda no lineal de envolvente lenta (p. 991–993).** De la ecuación de onda (21.1-3):

$$\left[\nabla^2-\frac1{c_0^2}\frac{\partial^2}{\partial t^2}\right]\mathcal E=\mu_0\frac{\partial^2}{\partial t^2}(\mathcal P_L+\mathcal P_{\rm NL})\qquad\text{(22.5-18)}$$

con $\mathcal P_L$ lineal (dispersión) y $\mathcal P_{\rm NL}=4\chi^{(3)}\mathcal E^3$ no dispersiva.
En Fourier:

$$[\nabla^2+\beta^2(\omega)]E=-\mu_0\omega^2P_{\rm NL}\qquad\text{(22.5-19)}$$

Onda plana pulsada en $z$, $\beta_0=\beta(\omega_0)=\omega_0/c$:

$$\mathcal E=\mathrm{Re}\{\mathcal A(z,t)\exp[j(\omega_0t-\beta_0z)]\}\qquad\text{(22.5-20)}$$

Con (1) SVE, (2) dispersión débil, (3) no linealidad pequeña:

$$\boxed{\frac{D_\nu}{4\pi}\frac{\partial^2\mathcal A}{\partial t^2}+\gamma|\mathcal A|^2\mathcal A+j\left(\frac{\partial}{\partial z}+\frac1v\frac{\partial}{\partial t}\right)\mathcal A=0}\qquad\text{(22.5-21) Nonlinear SVE Wave Equation}$$

$v=1/\beta'$, $D_\nu=2\pi\beta''$, $\gamma$ de (22.5-16). Para $\gamma=0$ se recupera (22.3-24).
*Derivación (p. 992–993)*: con $E=A(z,\omega-\omega_0)\exp(-j\beta_0z)$, $P_{\rm NL}=A_{\rm NL}\exp(-j\beta_0z)$,
$\Omega=\omega-\omega_0$:
$$[\partial^2/\partial z^2+\beta^2(\omega)][A\exp(-j\beta_0z)]=-\mu_0\omega^2A_{\rm NL}\exp(-j\beta_0z)\qquad\text{(22.5-22)}$$
$\omega^2\to\omega_0^2$; SVE ⇒
$$[-j2\beta_0d/dz]A+[\beta^2(\omega_0+\Omega)-\beta_0^2]A=-\mu_0\omega_0^2A_{\rm NL}\qquad\text{(22.5-23)}$$
dispersión débil y Taylor a 3 términos ⇒
$$-j2\beta_0\frac{dA}{dz}+2\beta_0(\Omega\beta'+\tfrac12\Omega^2\beta'')A=-\mu_0\omega_0^2A_{\rm NL}\qquad\text{(22.5-24)}$$
Como $\mathcal P_{\rm NL}=4\chi^{(3)}\mathcal E^3$ tiene componentes en $\omega_0$ y $3\omega_0$, se
retiene solo $\omega_0$: $\mathcal P_{\rm NL}=\mathrm{Re}\{\mathcal A_{\rm NL}\exp[j(\omega_0t-\beta_0z)]\}$ y (21.3-3a)
$$A_{\rm NL}=3\chi^{(3)}|A|^2A\qquad\text{(22.5-25)}$$
Volviendo al tiempo ($j\Omega A\to\partial\mathcal A/\partial t$, $-\Omega^2A\to\partial^2\mathcal A/\partial t^2$)
sale (22.5-21). Alternativamente: medio ≈ lineal con $\beta(\omega)+\Delta\beta$, $\Delta\beta=(\omega_0/c_0)n_2I$,
$I=|A|^2/2\eta$ lenta; el análisis de Fourier que dio (22.3-24) se modifica con un término ∝ $\Delta\beta A$,
que produce $\gamma|A|^2A$.

**Ecuación no lineal de Schrödinger (p. 993).** Ondas solitarias solo si $\beta''<0$ (GVD negativa)
y $\gamma>0$ ($n_2>0$). Normalización: tiempo a $\tau_0$ (ancho del pulso), distancia a $2z_0$ con
$z_0=\tau_0^2/2\beta''$ (longitud de dispersión), amplitud a $A_0=(-\beta''/\gamma)^{1/2}/\tau_0$
(amplitud que cumple (22.5-15)). En marco retardado:

$$\mathsf t=\frac{t-z/v}{\tau_0},\qquad\mathsf z=\frac z{2z_0},\qquad\psi=\frac A{A_0}\qquad\text{(22.5-26)}$$

$$\boxed{\frac12\frac{\partial^2\psi}{\partial\mathsf t^2}+|\psi|^2\psi+j\frac{\partial\psi}{\partial\mathsf z}=0}\qquad\text{(22.5-27) Nonlinear Schrödinger Equation}$$

**Solitón fundamental (p. 994).** Separación de variables $\psi(\mathsf z,\mathsf t)=\mathcal T(\mathsf t)\exp[j\mathcal Z(\mathsf z)]$
con $\mathcal T$, $\mathcal Z$ reales: $\mathcal Z'(\mathsf z)=\vartheta$, $\mathcal T''(\mathsf t)=2(\vartheta-\mathcal T^2)\mathcal T$;
con $\mathcal T=\mathcal T'=0$ en $|\mathsf t|\to\infty$ y $\mathcal T=1$, $\mathcal T'=0$ en $\mathsf t=0$:
$\mathcal T=\operatorname{sech}(\mathsf t)$, $\mathcal Z=\tfrac12\mathsf z$:

$$\psi(\mathsf z,\mathsf t)=\operatorname{sech}(\mathsf t)\exp(j\mathsf z/2)\qquad\text{(22.5-28)}$$

$$\boxed{\mathcal A(z,t)=A_0\operatorname{sech}\left(\frac{t-z/v}{\tau_0}\right)\exp(jz/4z_0)}\qquad\text{(22.5-29) Fundamental Soliton}$$

viaja a $v$ sin cambiar forma, si el pulso incidente es

$$\mathcal A(0,t)=A_0\operatorname{sech}(t/\tau_0)\qquad\text{(22.5-30)}$$

**Solitones de orden superior (p. 994).** Con $\psi(0,\mathsf t)=N\operatorname{sech}(\mathsf t)$, $N$
entero: **onda solitón-N**, periódica en $\mathsf z$ con periodo $\mathsf z_p=\pi/2$, el **periodo del
solitón**, distancia física $z_p=\pi|z_0|=(\pi/2)\tau_0^2/|\beta''|$. En $z=0$ es sech con amplitud
$N$ veces la fundamental. Se contrae inicialmente, se divide en pulsos distintos que luego se
fusionan y reproducen el pulso inicial en $z=z_p$; patrón periódico. El $N=2$:

$$\psi(\mathsf z,\mathsf t)=4\frac{\cosh3\mathsf t+3e^{4j\mathsf z}\cosh\mathsf t}{\cosh4\mathsf t+4\cosh2\mathsf t+3\cos4\mathsf z}e^{j\mathsf z/2}\qquad\text{(22.5-31)}$$

(**Fig. 22.5-9**, p. 995: $|\psi|$ para $N=1$ y $N=2$ vs $t/\tau_0$ y $z/z_p$.) La compresión y
expansión periódicas se deben a un desbalance periódico entre compresión (chirp por SPM) y
ensanchamiento (GVD). La compresión inicial se ha usado para generar pulsos sub-ps.

**Interacción solitón–solitón (p. 994–995).** Dos solitones lanzados con cierta separación se
comportan como si se atrajeran o repelieran. Dos fundamentales idénticos se atraen, colapsan en un
pulso y luego se repelen, periódicamente con periodo

$$L_p=\pi\exp(T/2\tau_0)z_0\qquad\text{(22.5-32)}$$

con $T$ la separación inicial centro a centro. Para $T=10\tau_0$, $L_p\approx466z_0$ (grande), pero
puede importar en fibras largas y limita los sistemas de comunicación por solitones (§24.2E).

- **Ejemplo 22.5-2 (p. 995). Solitones en fibras ópticas.** Observados primero en 700 m de fibra
  monomodo de sílice con láser mode-locked en $\lambda_0=1.55$ µm (región anómala, $\lambda_0>1.3$ µm),
  sech con $\tau_0=4$ ps ($\tau_{\rm FWHM}=1.76\tau_0=7$ ps). $D_\lambda=16$ ps/nm·km (Fig. 9.3-5) ⇒
  $\beta''=D_\nu/2\pi=(-\lambda_0^2/c_0)D_\lambda/2\pi\approx-20$ ps²/km. $n=1.45$,
  $n_2=3.19\times10^{-20}$ m²/W ⇒ $\gamma=(\pi/\lambda_0)n_2/\eta=2.48\times10^{-16}$ m/V²
  ($\eta=\eta_0/n=260$ Ω). $A_0=(|\beta''|/\gamma)^{1/2}/\tau_0\approx2.25\times10^6$ V/m ⇒
  $I_0=A_0^2/2\eta\approx10^6$ W/cm²; con área 10 µm², potencia ≈ 100 mW. Periodo
  $z_p=\pi z_0=\pi\tau_0^2/2|\beta''|=1.26$ km.

**Generación y mantenimiento (p. 995–996).** Para excitar el fundamental se requiere perfil sech con
el producto exacto $A_0\tau_0$ (22.5-15); menor ⇒ pulso ordinario; mayor ⇒ fundamental (o superior)
más energía espuria. Con otro perfil o chirp, puede evolucionar a solitón en unos pocos periodos.
Con pérdidas, la no linealidad se debilita y la dispersión domina ⇒ ensanchamiento; se compensa con
amplificación Raman distribuida (§21.3A) o amplificación localizada con espaciado ≪ $z_p$. Solitones
de pocos ps se han transmitido por miles de km (§22.1D [sic], aplicaciones a comunicaciones).

**Láseres de solitones (p. 996).** Fibra monomodo en anillo (**Fig. 22.5-10**): amplificador de fibra
dopada con erbio (§14.3C) + fibra sin dopar para conformación y acción solitónica; mode-locking por
modulador de fase; sistema integrado con bombeo de diodo InGaAsP y modulador integrado.

**Solitones oscuros (p. 996).** Depresión breve en la intensidad de una onda continua; propiedades
similares a los brillantes pero se generan en la región de dispersión normal ($\lambda_0<1.3$ µm en
sílice); robustos, útiles en conmutación óptica.

**Analogía solitones temporales–espaciales (p. 996–997).** Los solitones espaciales (haces
autoguiados, §21.3B) son ondas monocromáticas localizadas transversalmente que viajan en un medio no
lineal sin cambiar su distribución espacial (difracción ⇔ SPM espacial), según

$$\boxed{-\frac{\lambda}{4\pi}\frac{\partial^2\mathcal A}{\partial x^2}+\gamma|\mathcal A|^2\mathcal A+j\frac{\partial\mathcal A}{\partial z}=0}\qquad\text{(22.5-33) Nonlinear Beam Diffraction}$$

$\gamma=\pi n_2/\lambda\eta_0$ (equivalente a (21.3-11)). La NLSE temporal (22.5-21) en marco móvil
($t'=t-z/v$, $z'=z$):

$$\boxed{\frac{D_\nu}{4\pi}\frac{\partial^2\mathcal A}{\partial t^2}+\gamma|\mathcal A|^2\mathcal A+j\frac{\partial\mathcal A}{\partial z}=0}\qquad\text{(22.5-34) Nonlinear Pulse Dispersion}$$

$\gamma=\pi n_2/\lambda\eta_0$. Idéntica a (22.5-33) con $t\leftrightarrow x$ y $-D_\nu\leftrightarrow\lambda$.
"Solitón" designa soluciones genéricas de la NLSE que se propagan sin cambio, temporales o espaciales.

**Solitones espaciotemporales y balas de luz (p. 997).** Haz pulsado que mantiene perfiles espacial
*y* temporal en un medio Kerr con GVD negativa: ensanchamiento temporal y difracción compensados a la
vez por SPM y autoenfoque ($n_2>0$):

$$\boxed{-\frac{\lambda}{4\pi}\nabla_T^2\mathcal A+\frac{D_\nu}{4\pi}\frac{\partial^2\mathcal A}{\partial x^2}+\gamma|\mathcal A|^2\mathcal A+j\frac{\partial\mathcal A}{\partial z}=0}\qquad\text{(22.5-35) Nonlinear Diffraction \& Dispersion}$$

[así impreso: el segundo término lleva $\partial^2/\partial x^2$, debería ser $\partial^2/\partial t^2$].
Condición necesaria: igualdad de longitud de dispersión $|z_0|=\pi\tau_0^2/|D_\nu|$ y de difracción
$z_0=\pi W_0^2/\lambda$ ⇒ $\tau_0/W_0=(\lambda/|D_\nu|)^{1/2}$. **Fig. 22.5-11**: (a) ensanchamiento
espacial y temporal en medio lineal dispersivo; (b) solitón espaciotemporal.

#### \*22.5C Supercontinuum Light (p. 997)

Luz de alto brillo con espectro continuo ultra-ancho. **Generación de supercontinuo (SCG)**: pulso
ultracorto de alta potencia pico (bombeo) por un medio no lineal con propiedades dispersivas
especiales (fibras de dispersión desplazada, aplanada, microestructuradas, de cristal fotónico PCF).
Se han demostrado espectros de 400 a 3000 nm. Mecanismos: SPM, dispersión Raman estimulada (SRS),
mezcla de cuatro ondas (FWM) y corrimiento de autofrecuencia del solitón (SSFS), individual o
conjuntamente; sensibles al signo de la dispersión en $\lambda_0$ del bombeo y a la posición relativa
de la longitud de onda de dispersión cero $\lambda_{\rm ZD}$. Los espectros más anchos se obtienen con
$\lambda_0$ cerca de $\lambda_{\rm ZD}$; las PCF no lineales con $\lambda_{\rm ZD}$ cerca del
Ti:zafiro hicieron práctica la SCG (p. 997–998).

- **Fig. 22.5-12** (p. 998): tres escenarios según $D_\lambda(\lambda)$ y $\lambda_{\rm ZD}$: (a)
  SPM + SRS (bombeo en región normal); (b) solitón + SSFS (bombeo en región anómala, cerca de
  $\lambda_{\rm ZD}$); (c) FWM (dos $\lambda_{\rm ZD}$ con $\lambda_0$ entre ellas; espectro de dos picos).

Mecanismos (p. 998):
- **SPM**: principal en fibras con dispersión normal ($D_\lambda<0$) en $\lambda_0$ (no hay solitones).
  Ensancha el espectro por $\sqrt{1+a^2}$ con $a=L/z_{\rm NL}$, $z_{\rm NL}=(2n_2I_0k_0)^{-1}$.
- **SRS**: ensancha más hacia λ largas (corrimiento hacia abajo en frecuencia).
- Si $\lambda_0$ cerca de $\lambda_{\rm ZD}$, SPM/SRS llevan el espectro a la región anómala y se forman
  solitones; éstos sufren un corrimiento de su portadora a λ mayores que crece con la potencia:
  **SSFS**, originado en la SRS intrapulso.
- Fibra microestructurada con dos $\lambda_{\rm ZD}$ separadas y $\lambda_0$ entre ellas: SPM + **FWM**.
  SPM ensancha el bombeo y permite phase matching de FWM, generando luz a frecuencias mayores y
  menores (espectro bimodal; con suficiente ensanchamiento los picos se fusionan en una distribución
  plana).

---

### 22.6 Pulse Detection (p. 999)

Los fotodetectores más rápidos son demasiado lentos para pulsos ultra-estrechos. Los métodos usan un
obturador óptico ultrarrápido (compuerta) controlado por un pulso de referencia más corto y un retardo
controlable; se repite a distintos retardos para estimar $I(t)$. Para la fase $\phi(t)$ se usan
técnicas interferométricas combinadas con procesos no lineales. En el dominio espectral el pulso se
caracteriza por $S(\nu)$ y $\psi(\nu)$ (analizadores de espectro e interferometría). Los componentes
del sistema de medida alteran el pulso; hay que minimizarlo o compensarlo (p. 999).

#### 22.6A Measurement of Intensity (p. 999)

**Fotodetección directa (p. 999).** Con detector de respuesta mucho más corta que el pulso:

$$i(t)=\mathfrak RAI(t)\qquad\text{(22.6-1) Fast Detector}$$

$A$ área activa, $\mathfrak R$ responsividad (A/W, §18.1B). Con respuesta al impulso $h_D(t)$
($\int h_D\,dt=\mathfrak R$):

$$i(t)=A\int I(\tau)h_D(t-\tau)\,d\tau\qquad\text{(22.6-2) Arbitrary Detector}$$

Si el pulso es mucho más corto que la respuesta, $i(t)\approx h_D(t)A\int I(\tau)d\tau$; con
constante de tiempo del receptor $\tau_c$ mayor:

$$i(t)\approx\tau_c^{-1}\mathfrak RA\int I(\tau)\,d\tau\qquad\text{(22.6-3) Slow Detector}$$

El receptor mide el área (energía): integrador sin resolución temporal (**Fig. 22.6-1**, p. 1000).

**Pulso corto con detector lento y obturador rápido (p. 1000–1001).** La compuerta se abre una
ventana corta $W(t-\tau)$ en el pulso; el detector lento mide la energía transmitida; se repite a
distintos $\tau$ (**Fig. 22.6-2**). Las compuertas electrónicas no alcanzan ps/fs: compuerta óptica
controlada por un pulso de referencia mucho más corto (cap. 23):

$$i(\tau)\propto\int I(t)W(t-\tau)\,dt\qquad\text{(22.6-4)}$$

Ideal $W=\delta(t)$ ⇒ $i\propto I(\tau)$; en general convolución; resolución = ancho de $W(t)$
(velocidad de la compuerta). El retardo puede aplicarse a $W$ o a $I$.

- **Fig. 22.6-3** (p. 1001): (a) **compuerta Kerr óptica**: el pulso de referencia
  $I_r(t)=|U_r(t)|^2$ altera el retardo de la celda Kerr entre polarizadores cruzados ⇒
  $W(t)\propto I_r(t)=|U_r(t)|^2$. (b) **Compuerta SHG**: $U(t)$ y $U_r(t)$ con polarizaciones
  ortogonales en configuración Type-II colineal (§21.2D) generan SH con amplitud ∝ $U(t)U_r(t)$ ⇒
  $W(t)\propto U_r(t)$.

**Pulso único vs tren de pulsos (p. 1001).** Con un tren periódico de pulsos idénticos, se cambia
$\tau=m\Delta\tau$ para cada pulso y se registran secuencialmente (**Fig. 22.6-4**); la tasa de
repetición debe permitir que el detector lento se recupere. Para un pulso único: copias por un
elemento de abanico (fan-out), cada una con distinto retardo, compuerta y arreglo de detectores
(**Fig. 22.6-5**, p. 1002).

**Transformación temporal→espacial: principio de la cámara streak (p. 1001–1002).** Onda plana
pulsada a ángulo $\theta$ con $z$: $I(t-[x\sin\theta+z\cos\theta]/c)$; un detector plano en $z=0$ ve
$I(t-x\sin\theta/c)$: en $x$ el pulso se retrasa $\tau_x=x\sin\theta/c$. Una instantánea en $t=0$
registra $I(-x\sin\theta/c)$: perfil invertido escalado, ancho transversal $c\tau_0/\sin\theta$.
Ejemplo: $\tau_0=10$ ps ⇒ $c\tau_0=3$ mm; con $\theta=30°$, 6 mm en el detector. Es la base de la
**cámara streak** (luz reflejada en un tambor giratorio y "estirada"; o cuña de vidrio)
(**Fig. 22.6-6**). El obturador puede ser Kerr o SHG. Implementación útil (**Fig. 22.6-7**, p. 1003):
pulso y compuerta como ondas oblicuas ortogonalmente polarizadas a $\pm\theta$,
$U(t-[x\sin\theta+z\cos\theta]/c)$ y $U_r(t-[-x\sin\theta+z\cos\theta]/c)$, retardo relativo
$\tau_x=(2\sin\theta/c)x$; SHG Type-II no colineal genera onda ∝ $UU_r$, intensidad ∝ $II_r$ ⇒ la
señal detectada es la autocorrelación $G_I(\tau_x)$.

**Medición de autocorrelación de intensidad (p. 1002–1003).** Si no hay pulso de referencia más
corto, se puede comprimir el pulso (W = versión comprimida de $I$), o usar $I^2(t)$ (por SHG; más
estrecho), o procesos de orden mayor. O usar el propio pulso como compuerta (**Fig. 22.6-8**):

$$\boxed{G_I(\tau)=\int I(t)I(t-\tau)\,dt}\qquad\text{(22.6-5) Intensity Autocorrelation}$$

Simétrica, máxima $G_I(0)$ en $\tau=0$, → 0 en $\tau\to\infty$; en general más ancha que el pulso.
Gaussiano $I(t)=\exp(-2t^2/\tau_0^2)$ de ancho $\tau_0$ ⇒ $G_I(\tau)\propto\exp(-\tau^2/\tau_0^2)=\exp[-2(\tau/\sqrt2\tau_0)^2]$:
ancho $\sqrt2\tau_0$. La transformada de $G_I$ es $|\tilde I(\nu)|^2$ ($\tilde I$ transformada de
$I$): da $|\tilde I|$ pero no su fase ⇒ no basta para recuperar $I(t)$, salvo pulso simétrico
($I(-t)=I(t)$, $\tilde I$ real). Si el perfil matemático es conocido, sí permite estimar parámetros
(p. ej. el ancho) (p. 1003).

#### 22.6B Measurement of Spectral Intensity (p. 1004)

**Analizador de espectro óptico.** Banco de filtros espectrales + detectores lentos ⇒ $S(\nu)=|A(\nu)|^2$.
No se recupera $\mathcal A(t)$ sin la fase (salvo pulso simétrico). **Fig. 22.6-9**: (a) sistema
Fourier → $|\cdot|^2$; (b) implementación con prismas y detector espacial.

**Analizador de espectro interferométrico (p. 1004–1005).** Michelson como espectrómetro de
Fourier (§11.2). Haz dividido, uno retrasado $\tau$: campo $\frac1{\sqrt2}[U(t)+U(t-\tau)]$,
intensidad $\frac12|U(t)+U(t-\tau)|^2$; detector lento:

$$R_U(\tau)=\tfrac12\int|U(t)+U(t-\tau)|^2dt=\tfrac12\int|U(t)|^2dt+\tfrac12\int|U(t-\tau)|^2dt+\mathrm{Re}\int U^*(t)U(t-\tau)\,dt$$

Con $U=\mathcal A(t)\exp(j2\pi\nu_0t)$:

$$R_U(\tau)=G_A(0)+\mathrm{Re}\{G_A(\tau)\exp(-j2\pi\nu_0\tau)\}=G_A(0)+|G_A(\tau)|\cos[2\pi\nu_0\tau-\arg\{G_A(\tau)\}]\qquad\text{(22.6-6)}$$

$$G_A(\tau)=\int A^*(t)A(t-\tau)\,dt\qquad\text{(22.6-7)}$$

autocorrelación de la envolvente compleja = transformada inversa de $S(\nu)=|A(\nu)|^2$. $R_U(\tau)$
es un patrón de franjas de visibilidad $|G_A(\tau)|/G_A(0)$; analizando visibilidad y posición de
franjas se obtiene $G_A(\tau)$: misma información que el analizador convencional (**Fig. 22.6-10**).

#### 22.6C Measurement of Phase (p. 1005)

Caracterización completa: módulo y fase de $U(t)=\sqrt{I(t)}\exp[j2\pi\nu_0t+\varphi(t)]$ o de
$V(\nu)=\sqrt{S(\nu)}\exp[j\psi(\nu)]$. §22.6A da $I(t)$ sin $\varphi(t)$; §22.6B da $S(\nu)$ sin
$\psi(\nu)$. Bajo ciertas condiciones una función compleja se determina de $I(t)$ y $S(\nu)$. Aquí:
medidas directamente sensibles a $\varphi(t)$ o $\psi(\nu)$, basadas en interferometría (p. 1005).

**Interferometría espectral (p. 1005–1006).** Heterodinaje (interferometría "temporal", §2.6B):
$U(t)$ mezclado con referencia $U_r(t)=\sqrt{I_r(t)}\exp[j2\pi\nu_rt+\varphi_r(t)]$, $\nu_r=\nu_0+f$:

$$|U(t)+U_r(t)|^2=I(t)+I_r(t)+2\sqrt{I(t)I_r(t)}\cos[2\pi ft+\varphi_r(t)-\varphi(t)]\qquad\text{(22.6-8)}$$

interferograma con batido $f$ y fase variable $\varphi_r(t)-\varphi(t)$ extraíble. Pero para pulsos
ultrarrápidos el detector lento borra toda estructura temporal: no aplicable. Sí funciona en el
dominio de Fourier: **interferometría espectral**. $U(t)$ retrasado $\tau$ fijo + referencia $U_r(t)$
de la misma frecuencia; la transformada de la suma se mide con detector lento (**Fig. 22.6-11**).
Con $V(\nu)=\sqrt{S(\nu)}\exp[j\psi(\nu)]$ y $V_r(\nu)=\sqrt{S_r(\nu)}\exp[j\psi_r(\nu)]$:

$$|V(\nu)e^{-j2\pi\tau\nu}+V_r(\nu)|^2=S(\nu)+S_r(\nu)+2\sqrt{S(\nu)S_r(\nu)}\cos[2\pi\tau\nu+\psi_r(\nu)-\psi(\nu)]\qquad\text{(22.6-9)}$$

franjas en frecuencia con visibilidad dada por $S(\nu)$ y posiciones por $\psi(\nu)-\psi_r(\nu)$ ⇒
información completa de $V(\nu)$ y de $U(t)$. (22.6-8) y (22.6-9) son duales ($t\leftrightarrow\nu$,
$\tau\leftrightarrow f$). Dificultad: hace falta referencia conocida.

**Interferometría espectral autorreferenciada (p. 1006).** El pulso no puede ser su propia referencia
(el término de fase se anula si $\psi_r=\psi$). Se usa una versión desplazada en frecuencia,
$V_r(\nu)=V(\nu+f)$:

$$|V(\nu)e^{-j2\pi\nu\tau}+V(\nu+f)|^2=S(\nu)+S(\nu+f)+2\sqrt{S(\nu)S(\nu+f)}\cos[2\pi\nu\tau+\psi(\nu)-\psi(\nu+f)]\qquad\text{(22.6-10)}$$

(**Fig. 22.6-12**, p. 1007). Se estima $\psi(\nu+f)-\psi(\nu)$; con $f$ pequeño ≈ derivada
$d\psi/d\nu$, que se integra para obtener $\psi(\nu)$. [Es el principio de SPIDER; el libro no usa ese
nombre.]

**Interferometría no lineal (p. 1006–1008).** El interferómetro convencional mide el área de
$|U(t)+U(t-\tau)|^2$ (solo $S(\nu)$). Elevando al cuadrado antes de detectar (SHG en cristal no lineal):

$$R_U^{(2)}(\tau)=\int\left||U(t)+U(t-\tau)|^2\right|^2dt\qquad\text{(22.6-11)}$$

(**Fig. 22.6-13**: suma, $(\cdot)^2$ por SHG, detector lento). Con $U=\mathcal A\exp(j2\pi\nu_0t)$,
separando términos en 0, $\nu_0$ y $2\nu_0$:

$$R_U^{(2)}(\tau)\propto C_0(\tau)+4\mathrm{Re}\{C_1(\tau)e^{j2\pi\nu_0\tau}\}+2\mathrm{Re}\{C_2(\tau)e^{j4\pi\nu_0\tau}\}\qquad\text{(22.6-12)}$$

$$C_0(\tau)=\int I^2(t)dt+\int I^2(t-\tau)dt+4\int I(t)I(t-\tau)dt=2G_I(0)+4G_I(\tau)\qquad\text{(22.6-13)}$$
$$C_1(\tau)=\int\mathcal A^*(t)\mathcal A(t-\tau)[I(t)+I(t-\tau)]dt\qquad\text{(22.6-14)}$$
$$C_2(\tau)=\int[\mathcal A^*(t)\mathcal A(t-\tau)]^2dt\qquad\text{(22.6-15)}$$

$G_I$ de (22.6-5). Tres términos: uno no oscilatorio $C_0$ (solo intensidad, sin fase) y dos
oscilatorios en $\nu_0$ y $2\nu_0$ (dependen de intensidad y fase), separables por Fourier. Envolvente
superior con máximo $R_U^{(2)}(0)=16\int I^2dt=16G_I(0)$ e inferior con mínimo $R_U^{(2)}(0)=0$;
asintótico $R_U^{(2)}(\infty)=C_0(\infty)=2\int I^2dt=2G_I(0)$; razón $R^{(2)}(\infty)/R^{(2)}(0)$ de
8 en $\tau=0$ a 1 en $\tau=\infty$. Para gaussiano con chirp lineal ($\tau_0$, $a$):

$$C_0(\tau)=2G_I(0)[1+2\exp(-\tau^2/\tau_0^2)]\qquad\text{(22.6-16)}$$
$$C_1(\tau)=2G_I(0)\exp[-(3+a^2)\tau^2/4\tau_0^2]\cos(a\tau^2/2\tau_0^2)\qquad\text{(22.6-17)}$$
$$C_2(\tau)=G_I(0)\exp[-(1+a^2)\tau^2/\tau_0^2]\qquad\text{(22.6-18)}$$

**Fig. 22.6-14** (p. 1008): $R_U^{(2)}(\tau)/R_U^{(2)}(\infty)$ para $a=0,4,8$; el punto donde
desaparecen las oscilaciones es muy sensible a $a$ ⇒ sirve para estimar $a$. No hay procedimiento
general para la fase; sirve para verificar modelos o estimar parámetros.

*Interferometría no lineal con detectores no lineales (p. 1008).* El cuadrado lo hace el detector por
absorción de dos fotones (fotodiodo con $E_g$ entre $h\nu$ y $2h\nu$; fotocorriente ∝ $I^2$):

$$R_U'^{(2)}(\tau)=\int|U(t)+U(t-\tau)|^4dt\qquad\text{(22.6-19)}$$

que, como (22.6-11), contiene información de distribución y ancho.

#### \*22.6D Measurement of Spectrogram (p. 1009)

Espectrograma (§22.1A):

$$S(\nu,\tau)=|\Phi(\nu,\tau)|^2;\qquad\Phi(\nu,\tau)=\int U(t)W(t-\tau)\exp(-j2\pi\nu t)\,dt\qquad\text{(22.6-20)}$$

Se mide pasando $U(t)$ por una compuerta controlada por $W(t-\tau)$ y midiendo el espectro del
producto en cada $\tau$ (**Fig. 22.6-15**): espejo móvil (retardo) + analizador de espectro +
compuerta óptica. Técnica: **frequency-resolved optical gating (FROG)**. Sin compuerta corta se usa
el propio pulso:
- Compuerta SHG (Fig. 22.6-7): SH ∝ $U(t)U(t-\tau)$ ⇒ $W(t)\propto U(t)$:
  $$\Phi(\nu,\tau)=\int U(t)U(t-\tau)\exp(-j2\pi\nu t)\,dt\qquad\text{(22.6-21)}$$
  la **función de distribución de Wigner**; sistema **SHG-FROG** (**Fig. 22.6-16(a)**), apto para
  pulso único.
- Compuerta Kerr por polarización (Fig. 22.6-3(a)): $W(t)\propto I(t)=|U(t)|^2$:
  $$\Phi(\nu,\tau)=\int U(t)|U(t-\tau)|^2\exp(-j2\pi\nu t)\,dt\qquad\text{(22.6-22)}$$
  **PG-FROG** (polarization-gated, **Fig. 22.6-16(b)**).
- Otras: THG ($W\propto U^2$), autodifracción ($W\propto[U^*(t)]^2$) (p. 1010).

**Estimación de la función de onda desde el espectrograma (p. 1010–1011).** En general

$$S(\nu,\tau)=|\Phi(\nu,\tau)|^2;\qquad\Phi(\nu,\tau)=\int g(t,\tau)\exp(-j2\pi\nu t)\,dt\qquad\text{(22.6-23)}$$

con $g(t,\tau)=U(t)W(t-\tau)$ y $W$ relacionada con $U$ ($W=U$ SHG-FROG; $W=|U|^2$ PG-FROG). Si se
conociera $\Phi$:

$$g(t,\tau)=\int\Phi(\nu,\tau)\exp(j2\pi\nu t)\,d\nu\qquad\text{(22.6-24)}$$

$$\int g(t,\tau)d\tau=U(t)\int W(t-\tau)d\tau\propto U(t)\qquad\text{(22.6-25)}$$

(constante = área de la ventana, desconocida). Estimar $\Phi$ desde $S=|\Phi|^2$ es un **problema de
fase faltante**; algoritmo iterativo (p. 1011): (1) de $S$ se obtiene $|\Phi|=S^{1/2}$; con una fase
inicial supuesta, se estima $U(t)$ (inversa en $\nu$, integral en $\tau$); (2) con $U(t)$ se calcula
$\Phi$ y una nueva fase, que se combina con $|\Phi|$ medido para mejorar $U(t)$; (3) se itera hasta
converger a un $U(t)$ consistente con el espectrograma. **Fig. 22.6-17** (p. 1011): espectrograma
SHG-FROG medido de un pulso de 4.5 fs (2.5 ciclos), $I(t)$, $\varphi(t)$, $S(\lambda)$, $\psi(\lambda)$
estimados y espectrograma recalculado (Baltuška, Pshenichnikov y Wiersma, IEEE JQE 35, 459–478, 1999).

---

### Reading List (p. 1011–1013)

**General** (ver también la del cap. 21): Diels & Rudolph, *Ultrashort Laser Pulse Phenomena*,
Elsevier, 2.ª ed. 2006 · **Agrawal, *Nonlinear Fiber Optics*, Academic, 1991, 4.ª ed. 2006** ·
Gibbon, *Short Pulse Laser Interactions with Matter*, Imperial College Press, 2005 · Rullière (ed.),
*Femtosecond Laser Pulses*, Springer, 2.ª ed. 2005 · Uesaka (ed.), *Femtosecond Beam Science*, 2005 ·
Kärtner (ed.), *Few-Cycle Laser Pulse Generation and Its Applications*, Springer, 2004 · Andreev,
*Generation and Application of Ultrahigh Laser Fields*, 2002 · Trebino (ed.), *Frequency-Resolved
Optical Gating*, Kluwer, 2000 · Kamiya et al. (eds.), *Femtosecond Technology*, Springer, 1999 ·
Shvartsburg, *Time-Domain Optics of Ultrashort Waveforms*, Oxford, 1996 · Sueta & Okoshi (eds.),
*Ultrafast and Ultra-Parallel Optoelectronics*, Wiley, 1996 · Trebino & Walmsley (eds.), SPIE Proc.
2116, 1994 · Kaiser (ed.), *Ultrashort Laser Pulses*, Springer, 1993 · Shvartsburg, *Non-Linear Pulses
in Integrated and Waveguide Optics*, Oxford, 1993 · Akhmanov, Vysloukh & Chirkin, *Optics of
Femtosecond Laser Pulses*, AIP, 1992 · Dianov et al., *Nonlinear Effects in Optical Fibers*, Harwood,
1989 · Rudolph & Wilhelmi, *Light Pulse Compression*, Harwood, 1989 · Herrmann & Wilhelmi, *Lasers for
Ultrashort Light Pulses*, North-Holland, 1987.

**Libros sobre solitones**: Mollenauer & Gordon, *Solitons in Optical Fibers*, Academic, 2006 ·
Dauxois & Peyrard, *Physics of Solitons*, Cambridge, 2006 · Malomed, *Soliton Management in Periodic
Systems*, Springer, 2006 · Taylor (ed.), *Optical Solitons: Theory and Experiment*, Cambridge, 1992/2005 ·
Hasegawa & Matsumoto, *Optical Solitons in Fibers*, Springer, 3.ª ed. 2003 · Kivshar & Agrawal,
*Optical Solitons: From Fibers to Photonic Crystals*, Academic, 2003 · Akhmediev & Ankiewicz,
*Solitons, Nonlinear Pulses and Beams*, Chapman & Hall, 1997 · Drazin & Johnson, *Solitons: An
Introduction*, Cambridge, 1989/1993 · Olver & Sattinger (eds.), *Solitons in Physics, Mathematics, and
Nonlinear Optics*, Springer, 1990 · Dodd, Eilbeck, Gibbon & Morris, *Solitons and Nonlinear Wave
Equations*, Academic, 1982/1984 · Lamb, *Elements of Soliton Theory*, Wiley, 1980 · Lonngren & Scott
(eds.), *Solitons in Action*, Academic, 1978.

**Artículos** (selección): número especial IEEE JSTQE 12(2), 2006 · Goulielmakis et al., "Direct
Measurement of Light Waves", *Science* 305, 1267–1270 (2004) · Mourou & Umstadter, "Extreme Light",
*Sci. Am.* 286(5), 81–86 (2002) · IEEE JSTQE 7(4), 2001 · Leaird & Weiner, "Femtosecond Direct
Space-to-Time Pulse Shaping", IEEE JQE 37, 494–504 (2001) · IEEE JSTQE 6(6), 2000 · Baltuška,
Pshenichnikov & Wiersma, "SHG FROG in the Single-Cycle Regime", IEEE JQE 35, 459–478 (1999) ·
Walmsley, "Measuring Ultrafast Optical Pulses Using Spectral Interferometry", *Opt. & Phot. News*
10(4), 29–33 (1999) · Weiner, "Femtosecond Fourier Optics", en *Int. Trends in Optics and Photonics*,
Springer, 1999, 233–246 · IEEE JSTQE 4(2), 1998 · Segev & Stegeman, "Self-Trapping of Optical Beams:
Spatial Solitons", *Physics Today* 51(8), 42–48 (1998) · Binjrajka et al., *Opt. Lett.* 21, 1756–1758
(1996) · Wefers, Nelson & Weiner, en *Ultrafast Phenomena X*, Springer, 1996, 159–160 · Weiner,
"Femtosecond Optical Pulse Shaping and Processing", *Prog. Quantum Electron.* 19, 161–238 (1995) ·
Haus, "Optical Fiber Solitons", *Proc. IEEE* 81, 970–983 (1993) · Trebino & Kane, "Using Phase
Retrieval to Measure the Intensity and Phase of Ultrashort Pulses: FROG", *JOSA A* 10, 1101–1111
(1993) · Kempe & Rudolph, *Phys. Rev. A* 48, 4721–4729 (1993); *Opt. Lett.* 18, 137–139 (1993) ·
Kempe, Rudolph, Stamm & Wilhelmi, *JOSA B* 9, 1158–1165 (1992) · Weiner, "Dark Optical Solitons", en
Taylor (ed.), 1992, 378–408 · Gosnell & Taylor (eds.), *Selected Papers on Ultrafast Laser
Technology*, SPIE Milestone 44, 1991 · Christov, "Generation and Propagation of Ultrashort Optical
Pulses", *Prog. Optics* 29, 199–291 (1991) · Oughstun, "Pulse Propagation in a Linear, Causally
Dispersive Medium", *Proc. IEEE* 79, 1379–1390 (1991) · Bell, "Light That Acts Like Natural Bits",
*IEEE Spectrum* 27(8), 56–57 (1990) · Kolner & Nazarathy, "Temporal Imaging with a Time Lens",
*Opt. Lett.* 14, 630–632 (1989) · Zewail, "Laser Femtochemistry", *Science* 242, 1645–1653 (1988) ·
Haus & Islam, "Theory of the Soliton Laser", IEEE JQE 21, 1172–1188 (1985).

---

## Tablas y datos numéricos útiles

### Constantes y relaciones de conversión

- Producto tiempo–ancho de banda gaussiano: $\tau_{\rm FWHM}\Delta\nu=0.44$ (sin chirp);
  $0.44\sqrt{1+a^2}$ con chirp $a$ (p. 942). $\tau_{\rm FWHM}=1.18\tau$; $\Delta\nu=0.375/\tau$.
- Sech: $\tau_{\rm FWHM}=1.76\tau$ (intensidad), FWHM de amplitud $2.63\tau$, $\Delta\nu=0.315/\tau_{\rm FWHM}$
  (Prob. 22.1-2: $S(\nu)=\operatorname{sech}^2(\pi^2\tau\nu)$, $\Delta\nu=0.993/\tau$ [sic en el enunciado]).
- $\Delta\lambda\approx(\lambda_0^2/c)\Delta\nu$; $\Delta\lambda[\text{nm}]\approx3.3\,\lambda_0^2[\text{µm}]\,\Delta\nu[\text{THz}]$ (p. 939).
- Pulso de 10 fs: $\Delta\nu=44$ THz ⇒ $\Delta\lambda=37/147/331$ nm en 0.5/1/1.5 µm. Pulso de 2 fs
  en 1 µm: $\Delta\nu=220$ THz, $\Delta\lambda=847$ nm (p. 939).
- Extensión espacial $c\tau$: 1 ns → 30 cm; 1 ps → 0.3 mm; 1 fs → 0.3 µm; 1 as → 0.3 nm (p. 944).
- $D_\nu=2\pi\beta''=(\lambda_0^3/c_0^2)d^2n/d\lambda_0^2$ [s²/m]; $D_\nu=-(\lambda_0^2/c_0)D_\lambda$
  con $D_\lambda$ en s/m² (ps/km·nm) (p. 962, 968, 995). $b=2\beta''z=D_\nu z/\pi$.
- $z_0=\pi\tau_0^2/D_\nu=\tau_0^2/2\beta''$ (ancho $\tau_0$ a $1/e$ de la amplitud, i.e. $\tau_{\rm FWHM}/1.18$).
- $z_{\rm NL}=(2n_2I_0k_0)^{-1}=\lambda_0A/(4\pi n_2P_0)$ (p. 988). Solitón: $z_{\rm NL}=-z_0$;
  $I_0|z_0|=\lambda_0/4\pi n_2$ (Prob. 22.5-4).
- $\gamma=k_0n_2/2\eta=\pi n_2/\lambda_0\eta$ [m/V²]; $\eta=\eta_0/n$; $I=|A|^2/2\eta$ (p. 990, 995).
- Periodo del solitón $z_p=\pi|z_0|=(\pi/2)\tau_0^2/|\beta''|$; interacción $L_p=\pi\exp(T/2\tau_0)z_0$.
- Dualidad difracción–dispersión: $\lambda\leftrightarrow-D_\nu$; $c^2D_\nu$ con $D_\nu=10^{-23}$ s²/m
  ≈ 0.9 µm (p. 970).

### Parámetros de materiales que aparecen en el capítulo

| Material / condición | Parámetro | Valor | Página |
|---|---|---|---|
| BK7, 800 nm | $n$, $N$ | 1.51, 3.11 [sic] | 956 |
| BK7, 800 nm | $D_\nu$ | $0.284\times10^{-24}$ s²/m | 963 |
| BK7, 620 nm | $\beta''$ | $1.02\times10^{-25}$ s²/m | 965 |
| BK7, 400 nm | $n$, $n-N=\lambda dn/d\lambda$ | 1.53, −0.052 | 974 |
| Sílice, 850 nm | $D_\lambda$, $D_\nu$ | −200 ps/km·nm, $+4.82\times10^{-25}$ s²/m | 968 |
| Sílice, 1.55 µm | $D_\lambda$ | +20 ps/km·nm (Ej. 22.3-1); 16 ps/nm·km ⇒ $\beta''\approx-20$ ps²/km (Ej. 22.5-2) | 968, 995 |
| Sílice, 620 nm | $n_2$, $\beta''$ | $3.2\times10^{-20}$ m²/W, $6\times10^{-26}$ s²/m | 988 |
| Sílice, 1.55 µm | $n$, $n_2$, $\eta$, $\gamma$ | 1.45, $3.19\times10^{-20}$ m²/W, 260 Ω, $2.48\times10^{-16}$ m/V² | 995 |
| Sílice, 800 nm | $D_\lambda$ | −110 ps/km·nm (Prob. 22.6-1) | 1015 |
| Fibra compensadora (Ej. 22.3-1) | $D_\lambda$ | −100 ps/km·nm | 968 |
| KDP, Type-II, 1.06 µm → 0.53 µm | $\Delta\beta'$ | $5.2\times10^{-10}$ s/m ⇒ $L_g\approx0.2$ mm (100 fs) | 985 |
| Red, $\Lambda=1.6$ µm, 800 nm | $\alpha_\nu$; $b$ ($\ell_0=10$ cm) | −2.72 fs; $-2.94\times10^{-25}$ s² = −(542 fs)² | 956 |
| Prisma BK7 15°, 800 nm | $\alpha_\nu$; $b$ ($\ell_0=1$ cm) | 1.11 fs; $-5\times10^{-27}$ s² = −(71 fs)² | 956 |
| Zona de dispersión cero en sílice | $\lambda_{\rm ZD}$ | ≈ 1.3 µm (anómala para $\lambda>1.3$ µm) | 995, 996 |

### Resultados numéricos de los ejemplos

- Ej. 22.3-2: BK7 1 cm en 620 nm: $b=(4.5$ ps$)^2$; pulso de 100 fs: $|z_0|$ = 0.5 mm [sic], se
  duplica en 0.87 mm.
- Ej. 22.3-3: sílice 850 nm, $\tau_0=100$ fs: $z_0=6.52$ cm; en 6.52 m → 10 ps ($a=100$); con QPM
  $\zeta=-10^{-2}$ fs⁻²: mínimo 77 fs [sic] en 3.26 cm, 14.1 ps en 6.52 m.
- Ej. 22.5-1: 65 fs, 300 kW, 620 nm, fibra 9 mm/100 µm²: $z_{\rm NL}\approx0.5$ mm, $a=18$, compresión
  a 3.6 fs; $z_0=3.5$ cm; $b_{\rm red}\approx(3.6$ fs$)^2$.
- Ej. 22.5-2: solitón 1.55 µm, $\tau_0=4$ ps (7 ps FWHM): $A_0\approx2.25\times10^6$ V/m,
  $I_0\approx10^6$ W/cm², $P\approx100$ mW (10 µm²), $z_p=1.26$ km.
- §22.4A: lente BK7 400 nm, $f=30$ mm, $F_\#=2$: $\Delta\tau\approx307$ fs.
- Fig. 22.4-4: $N=5$, 750 THz, $\tau_0=6.67$ fs, $W_0=1$ mm: $z_0=7.85$ m, $\rho_0\approx8$ cm.

Las Tablas 22.1-1, 22.3-1, 22.3-2 y 22.3-3 están transcritas completas en sus secciones.

---

## Problemas al final del capítulo (p. 1013–1015)

Los marcados con * son avanzados según el libro.

- **22.1-1 Superposición de dos pulsos gaussianos.** Un pulso gaussiano limitado por transformada se
  suma a un pulso gaussiano con chirp de parámetro $a$ y parámetros por lo demás idénticos. Deducir
  expresiones para la intensidad, la fase, la intensidad espectral, la fase espectral y el parámetro
  de chirp del pulso superposición.
- **22.1-2 El pulso secante hiperbólica.** Un pulso tiene envolvente compleja $\operatorname{sech}(t/\tau)$,
  con $\operatorname{sech}(\cdot)=1/\cosh(\cdot)$ y $\tau$ una constante de tiempo. Mostrar que el
  ancho de la función intensidad es $\tau_{\rm FWHM}=1.76\tau$, la intensidad espectral es
  $S(\nu)=\operatorname{sech}^2(\pi^2\tau\nu)$ y el ancho espectral FWHM es $\Delta\nu=0.993/\tau$.
  Comparar con el pulso gaussiano. (Ver la tabla de transformadas de Fourier del Apéndice A.)
- **22.2-1 Filtro de chirp con prisma grueso.** Un prisma grueso se usa como filtro de chirp. El
  ángulo de incidencia se elige para satisfacer la condición de Brewster para minimizar la pérdida por
  reflexión. El ángulo de ápice $\alpha$ se elige tal que el rayo incidente y el rayo central
  desviado sean simétricos respecto al prisma. Bajo estas dos condiciones, mostrar que el ángulo de
  desviación $\theta_d$ satisface la condición $d\theta_d/dn=-2$ y el coeficiente de chirp está dado
  por $b\approx-4(n-N)^2\ell_0\lambda_0/\pi c^2$. Mostrar que, con todos los parámetros iguales, el
  coeficiente de chirp es mayor que en el prisma delgado (ver Ejemplo 22.2-2) por un factor $4/\alpha^2$.
- **22.2-2 Filtro de chirp con red de Bragg.** Diseñar un filtro de chirp con red de Bragg para
  pulsos de frecuencia central $\nu_0=300$ THz (longitud de onda 1 µm) y $\tau_{\rm FWHM}=0.44$ ps. El
  filtro debe tener coeficiente de chirp $b=(2$ ps$)^2$. Especificar las dimensiones de la red y el
  paso máximo y mínimo de su estructura periódica para asegurar que todas las componentes espectrales
  del pulso sean reflejadas por la red.
- **22.2-3 Propagación de un pulso rectangular por una fibra óptica.** Un pulso rectangular de ancho
  $\tau$ viaja por una fibra óptica, modelada como filtro de chirp con parámetro $b=D_\nu z/\pi$
  [ver (22.3-5)]. Mostrar que a una distancia $z$ suficientemente larga el pulso cambia su forma de
  rectangular a función sinc. Deducir una expresión para el nuevo ancho del pulso.
- **22.2-4 Formación de imagen temporal con una "lente temporal".** Un pulso óptico de ancho $\tau_1$
  y forma arbitraria viaja una distancia $d_1$ por una fibra con GVD positiva, luego es modulado por un
  factor de fase $\exp(j\zeta t^2)$ y después viaja una distancia $d_2$ por una fibra del mismo
  material. El ancho del pulso final es $\tau_2$. Suponiendo que $d_1$ y $d_2$ son mucho mayores que la
  longitud de dispersión $z_0$ de la fibra, mostrar que el nuevo pulso será una réplica retardada del
  pulso original con magnificación temporal $\tau_2/\tau_1=d_2/d_1$ si se cumple la condición
  $1/d_1+1/d_2=1/f$, donde $f=-\pi/\zeta D_\nu$ es la distancia focal del modulador de fase para este
  medio ($\zeta$ es negativo y $f$ positivo). Demostrar que el sistema es equivalente a un sistema de
  formación de imagen temporal.
- **22.5-1 Mezcla de ondas chirpeadas y amplificación de chirp.** (a) Tres ondas pulsadas colineales
  con frecuencias angulares centrales $\omega_1$, $\omega_2$ y $\omega_3=\omega_1+\omega_2$ se mezclan en
  un medio no lineal de segundo orden con coeficiente no lineal $\mathsf d$. El medio es dispersivo y
  tiene índices de refracción $n_1$, $n_2$, $n_3$ y velocidades de grupo $v_1$, $v_2$, $v_3$ a las
  tres frecuencias centrales. Los tres pulsos están chirpeados con parámetros $a_1$, $a_2$, $a_3$.
  ¿Cuál debe ser la relación entre $a_1$, $a_2$ y $a_3$ para una mezcla de tres ondas eficiente?
  *Pista*: suponer que las relaciones de conservación de energía y momento (phase matching) se
  satisfacen en todo instante. (b) Demostrar que el parámetro de chirp de la señal y/o el idler puede
  ser mayor que el del bombeo. Discutir posibles aplicaciones de este proceso de "amplificación de chirp".
- **\*22.5-2 Mezcla pulsada de tres ondas en un medio con GVD.** Deducir las ecuaciones acopladas de
  mezcla de tres ondas (22.5-3) para un medio con GVD. Se puede usar el siguiente procedimiento: partir
  de la ecuación de Helmholtz con fuente igual a la transformada de Fourier de
  $\mathcal S=\mu_0\partial^2\mathcal P_{\rm NL}/\partial t^2$, donde $\mathcal P_{\rm NL}=2\mathsf d\mathcal E^2$.
  Expresar el campo $\mathcal E$ como superposición de tres ondas con frecuencias centrales distintas y
  envolventes lentas, y convertir la ecuación de Helmholtz en tres ecuaciones separadas a las tres
  frecuencias. Simplificar estas ecuaciones usando la aproximación SVE, dispersión débil y un
  desarrollo de Taylor de tres términos de la constante de propagación. Usar una transformada inversa
  de Fourier para convertir las ecuaciones de vuelta al dominio del tiempo.
- **22.5-3 Dependencia de las características del solitón con la GVD.** Comparar las características
  de dos solitones fundamentales de igual energía que viajan en dos medios extendidos (p. ej., fibras
  ópticas) con coeficientes GVD $D_\lambda=20$ ps/km·nm y $D_\lambda=10$ ps/km·nm, pero por lo demás
  propiedades ópticas idénticas (mismo índice de refracción y mismo coeficiente Kerr $n_2$). Comparar
  los anchos de los solitones, la amplitud pico, el área bajo el perfil de amplitud y la distancia del
  solitón.
- **22.5-4 Solitones en fibra óptica.** Mostrar que el producto de la intensidad pico y la longitud de
  dispersión para el solitón fundamental es una constante, $I_0|z_0|=\lambda_0/4\pi n_2$. Para una
  fibra de sílice con coeficiente Kerr $n_2=3.19\times10^{-20}$ m²/W determinar la intensidad pico
  $I_0$ para una distancia de dispersión $|z_0|=30$ km.
- **22.6-1 Medición de un pulso gaussiano.** Un pulso óptico gaussiano limitado por transformada de
  50 fs de ancho (FWHM) y frecuencia central correspondiente a 800 nm se mide con el correlador de
  intensidad ilustrado en la Fig. 22.6-8. (a) Determinar la forma y el ancho FWHM de la función de
  autocorrelación medida. (b) Se ha sugerido que la medición mejoraría si uno de los pulsos, digamos
  el de la rama superior, se estira deliberadamente al pasar por una fibra de sílice. ¿Cuál debe ser la
  longitud de la fibra para estirar el pulso por un factor de 5? (La sílice tiene coeficiente de
  dispersión $D_\lambda=-110$ ps/km·nm en 800 nm.) ¿Cuál sería el ancho de la nueva función de
  correlación tras insertar la fibra? (c) Si esta idea se aplica al interferómetro no lineal de la
  Fig. 22.6-13, colocando la fibra también en la rama superior, describir posibles méritos y problemas
  de esta idea como herramienta de medición de pulsos.
- **22.6-2 Interferómetro con detector de absorción de dos fotones.** Un interferómetro que usa un
  absorbedor de dos fotones como detector mide la función (22.6-19). Comparar este interferómetro con
  un interferómetro no lineal que usa un generador de segundo armónico seguido de un detector
  convencional, que mide (22.6-11). Desarrollar (22.6-19) en una forma similar a (22.6-12) y comparar
  los distintos términos.

---

## Relación con Óptica No Lineal

### Mapa con los temas 7–9 del curso (Agrawal, *Nonlinear Fiber Optics*, caps. 1–5)

| Tema del programa / Agrawal | Sección de Saleh cap. 22 | Qué aporta |
|---|---|---|
| Agrawal cap. 1 (introducción: fibras, dispersión, no linealidad Kerr) | §22.1A–B (p. 937–943); §22.2B (p. 954); §22.5A (p. 987–988) | Definición de pulso gaussiano con chirp (Tabla 22.1-1), $\tau_{\rm FWHM}\Delta\nu=0.44\sqrt{1+a^2}$; tipos de dispersión; $n_2$, SPM como QPM, $z_{\rm NL}$ |
| Agrawal cap. 2 (ecuación de propagación de pulsos, NLSE) | §22.3A, C (p. 961–970); §22.5B (p. 991–993) | $H_e(f)=\exp\{-j[\beta(\nu_0+f)-\beta_0]z\}$; Taylor de $\beta$ ($\beta'$, $\beta''$); ecuación de difusión SVE (22.3-25) ≡ ec. de la envolvente lineal; NLSE (22.5-21), (22.5-27) con normalización (22.5-26). Ojo: Saleh usa $e^{j\omega t}$ y $D_\nu=2\pi\beta''$; Agrawal usa $e^{-i\omega t}$ y $\beta_2=\beta''$, $L_D=T_0^2/\lvert\beta_2\rvert$ (= $\lvert z_0\rvert$ de Saleh ×2: $z_0=\tau_0^2/2\beta''$), $L_{\rm NL}=1/(\gamma_{\rm Agrawal}P_0)$ |
| Agrawal cap. 3 (GVD: ensanchamiento, chirp, $D$, dispersión de tercer orden) | §22.2A (p. 950–953); §22.3B (p. 963–968); §22.3D (p. 970–973) | $\tau(z)=\tau_0\sqrt{1+(z/z_0)^2}$, $a(z)=z/z_0$, $z_{\min}=-a_1z_0$; compresión de pulsos con chirp (signo de $a_1$ vs signo de $D_\nu$); $D_\lambda\leftrightarrow D_\nu\leftrightarrow\beta''$; compensación de dispersión (Ej. 22.3-1); analogía con difracción (Tablas 22.3-2, 22.3-3); tercer orden mencionado en p. 949 |
| Agrawal cap. 4 (SPM: chirp inducido, ensanchamiento espectral, interacción SPM–GVD) | §22.2C (p. 957–959); §22.5A (p. 987–988) | $\Delta\varphi(t)=-n_2I(t)k_0z$, $\Delta\omega_i=-n_2k_0z\,dI/dt$; $a=z/z_{\rm NL}$; QPM ↔ SPM; compresión SPM + red (Ej. 22.5-1); Fig. 22.5-5 |
| Agrawal cap. 5 (solitones ópticos) | §22.5B (p. 988–997) | Condición de solitón (22.5-13)–(22.5-15); sech (22.5-17); solitón fundamental (22.5-29); orden $N$, periodo $z_p=\pi\lvert z_0\rvert$; interacción (22.5-32); Ej. 22.5-2; solitones oscuros; láseres de solitones; analogía espacial |
| Supercontinuo (Agrawal, caps. posteriores) | §22.5C (p. 997–998) | Mecanismos SPM, SRS, FWM, SSFS y papel de $\lambda_{\rm ZD}$ |
| Caracterización de pulsos | §22.6 (p. 999–1011) | Autocorrelación, interferometría espectral, FROG |

### Para la Tarea 2 (dispersión y polarización)

- Definición del pulso gaussiano con chirp y su espectro: Tabla 22.1-1, p. 943 (citar como Saleh &
  Teich, 2.ª ed., §22.1B, Tabla 22.1-1, p. 943).
- Propagación en medio dispersivo: §22.3A–B, Tabla 22.3-1, p. 964 (ec. (22.3-10)–(22.3-12)).
- Conversión $D_\lambda\to D_\nu\to\beta''$: p. 962 ec. (22.3-6) y Ej. 22.3-3 p. 968.
- Ecuación de la envolvente $\partial\mathcal A/\partial z=j(D_\nu/4\pi)\partial^2\mathcal A/\partial t^2$
  (forma equivalente de (22.3-25), p. 969) con solución por Fourier
  $A(z,f)=\exp(-j\pi D_\nu zf^2)A(0,f)$ (ec. (22.3-3), p. 962).

### Para el proyecto final (anillos add-drop en Si₃N₄, dispersión de guías, supercontinuo, sensado)

- **Dispersión de guías**: §22.2B (p. 954) clasifica la dispersión de guía de onda (confinamiento) y
  modal como "difractiva/multitrayecto"; la cadena $n_{\rm eff}(\lambda)\to\beta(\omega)\to\beta',\beta''\to D_\nu, D_\lambda$
  de (22.3-4)–(22.3-6) es exactamente lo que se extrae de un barrido FDE/MODE de la guía de Si₃N₄
  ($\beta''=d^2\beta/d\omega^2$; $D_\lambda=-(2\pi c_0/\lambda_0^2)\beta''$). La longitud de dispersión
  $z_0=\tau_0^2/2\beta''$ fija la escala de longitud frente al perímetro del anillo.
- **Supercontinuo en Si₃N₄**: §22.5C (p. 997–998) da el criterio de diseño (bombear cerca de
  $\lambda_{\rm ZD}$, régimen anómalo para fisión de solitones + SSFS, dos $\lambda_{\rm ZD}$ para FWM
  bimodal); §22.5B da la escala de potencia del solitón $A_0\tau_0=\sqrt{-\beta''/\gamma}$ y el
  periodo $z_p$; el orden del solitón de entrada $N^2=z_0/z_{\rm NL}$ (equivalente a
  $N^2=L_D/L_{\rm NL}$ de Agrawal) determina la dinámica de fisión. La compresión inicial del solitón
  $N=2$ (Fig. 22.5-9) es el mecanismo que precede al ensanchamiento espectral.
- **Resonadores como filtros dispersivos**: p. 954 señala que los resonadores ópticos tienen fuerte
  selectividad en frecuencia y son "altamente dispersivos" (dispersión interferométrica); la respuesta
  de fase del anillo add-drop cerca de resonancia actúa como filtro de chirp (22.2-11) sobre un pulso
  (retardo de grupo (22.2-10) ↔ $Q$ y tiempo de vida del fotón).
- **Sensado de índice de refracción (bulk)**: no se trata directamente en el cap. 22; lo pertinente es
  el vínculo $n_{\rm eff}$(cladding) → $\beta$ → corrimiento de resonancia, y el hecho de que un cambio
  de índice del analito cambia también $\beta''$ (dispersión de guía) — relevante si se quiere usar el
  mismo anillo en régimen pulsado.
- **Medición**: §22.6 (autocorrelación SHG, FROG) es la referencia para caracterizar los pulsos de
  bombeo si el proyecto llega a la parte experimental; §22.6B (analizador de espectro) para el
  espectro de salida del supercontinuo.
