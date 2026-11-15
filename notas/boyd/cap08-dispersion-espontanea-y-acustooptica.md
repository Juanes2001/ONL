# Capítulo 8 — Spontaneous Light Scattering and Acoustooptics (Boyd, 3.ª ed.)

Páginas del libro 391–428 (PDF 409–446). Leído el 2026-11-14.

Fuente: R. W. Boyd, *Nonlinear Optics*, 3.ª ed., Academic Press, 2008, cap. 8.
Las citas de página son páginas del libro (sumar 18 para la página del PDF).

Convención de Boyd (SI): $\tilde E(t)=Ee^{-i\omega t}+\text{c.c.}$ (amplitud $E$ = la mitad de la amplitud de pico),
$I=2n\epsilon_0c|E|^2$. En este capítulo $\epsilon$ denota la constante dieléctrica *relativa* ($\epsilon=1+\chi$) y
$\alpha$ la polarizabilidad definida por $\tilde{\mathbf p}=\epsilon_0\alpha\mathbf E$ (dimensiones de volumen). $\theta$ es el ángulo de dispersión;
$\phi$, el ángulo entre el dipolo inducido y la dirección de observación.

---

## Resumen del capítulo

El capítulo trata la dispersión **espontánea** de la luz (las propiedades del medio no son alteradas por el
haz) como preámbulo a la dispersión estimulada de los caps. 9 y 10. Clasifica el espectro dispersado en
Rayleigh (centro, no desplazada, por fluctuaciones de entropía), Rayleigh‑wing (fluctuaciones de orientación
de moléculas anisótropas), Brillouin (fonones acústicos) y Raman (fonones ópticos / vibraciones moleculares),
con sus desplazamientos, anchos, tiempos de relajación y ganancias típicas (Tabla 8.1.1). Establece que un
medio perfectamente homogéneo solo dispersa hacia adelante (origen del índice de refracción) y que la
dispersión lateral exige **fluctuaciones** del tensor dieléctrico, que se descompone en parte escalar
(Brillouin, Rayleigh), simétrica sin traza (Rayleigh‑wing) y antisimétrica (Raman). Define coeficiente de
dispersión $R$ y secciones eficaces total y diferencial. La teoría microscópica (§8.2) da la radiación dipolar
$d\sigma/d\Omega=(\omega^4/16\pi^2c^4)|\alpha|^2\sin^2\phi$, la ley $\omega^4$ de Rayleigh, el límite Thomson, la
sección eficaz del átomo de Lorentz y de esferas dieléctricas, y muestra con un argumento de celdas que la
luz dispersada por un conjunto de moléculas es proporcional a la **varianza** del número de moléculas por
celda (Poisson para gas ideal → $R=N\,d\sigma/d\Omega$; inválido en materia condensada). La teoría
termodinámica (§8.3) expresa $R$ en función de la constante electrostrictiva $\gamma_e=\rho\,\partial\epsilon/\partial\rho$ y la
compresibilidad isotérmica, y separa las fluctuaciones de densidad en adiabáticas (ondas de presión →
dobletes Brillouin desplazados $\Omega=2n\omega(v/c)\sin(\theta/2)$, de ancho $\Gamma'q^2$) e isobáricas (entropía,
ecuación de difusión → línea Rayleigh central no desplazada de ancho $(4\kappa/\rho c_p)k^2\sin^2(\theta/2)$),
con la relación de Landau–Placzek para sus intensidades. Finalmente (§8.4) aplica esto a la
**acustoóptica**: celdas de Bragg (condición $\lambda=2\Lambda\sin\theta$, ecuaciones de modos acoplados, eficiencia
$\sin^2|\kappa|L$, tolerancia angular, moduladores y deflectores) y difracción de Raman–Nath en celdas delgadas
(órdenes múltiples con intensidades $J_l^2(\delta)$, criterio $\lambda L/\Lambda^2$ grande o pequeño).

---

## Secciones

### 8.1 Features of Spontaneous Light Scattering (p. 391)

**Dispersión espontánea**: dispersión en condiciones en que las propiedades ópticas del material
*no* son modificadas por el haz incidente (en los caps. 9 y 10 se ve que el proceso cambia
profundamente cuando la intensidad es suficiente para modificarlas → dispersión estimulada).

Fig. 8.1.1 (p. 392): (a) montaje: haz incidente de frecuencia $\nu_0$ sobre un medio, luz dispersada
en todas direcciones; (b) espectro típico: línea Rayleigh centrada en $\nu_0$, alas Rayleigh‑wing
anchas alrededor, dos picos Brillouin cercanos a ambos lados y líneas Raman lejanas. Las
componentes desplazadas a frecuencias menores se llaman **Stokes**; a frecuencias mayores, **anti‑Stokes**.

- **Raman**: interacción con modos vibracionales de las moléculas; equivalentemente, dispersión
  por **fonones ópticos**.
- **Brillouin**: dispersión por ondas de sonido (ondas de presión, y por tanto de densidad, que se
  propagan); dispersión por **fonones acústicos**.
- **Rayleigh** (o Rayleigh‑center): dispersión por fluctuaciones de densidad *no propagantes*;
  formalmente, por fluctuaciones de **entropía**. Es *cuasielástica* (no desplaza la frecuencia).
- **Rayleigh‑wing**: dispersión por fluctuaciones en la **orientación** de moléculas anisotrópicas;
  como la reorientación es muy rápida, la componente es espectralmente muy ancha. No ocurre para
  moléculas con tensor de polarizabilidad isotrópico.

**Tabla 8.1.1** (p. 392) — valores típicos:

| Proceso | Desplazamiento (cm⁻¹) | Ancho de línea (cm⁻¹) | Tiempo de relajación (s) | Ganancia ᵃ (m/MW) |
|---|---|---|---|---|
| Raman | 1000 | 5 | $10^{-12}$ | $5\times10^{-5}$ |
| Brillouin | 0.1 | $5\times10^{-3}$ | $10^{-9}$ | $10^{-4}$ |
| Rayleigh | 0 | $5\times10^{-4}$ | $10^{-8}$ | $10^{-6}$ |
| Rayleigh‑wing | 0 | 5 | $10^{-12}$ | $10^{-5}$ |

ᵃ Ganancia de la versión estimulada del proceso.

#### 8.1.1 Fluctuations as the Origin of Light Scattering (p. 393)

Un medio **completamente homogéneo** solo dispersa en la dirección hacia adelante (Fabelinskii,
1968). Argumento de la Fig. 8.1.2: si el elemento $dV_1$ dispersa en la dirección $\theta$, para
cualquier $\theta\neq0$ existe un elemento vecino $dV_2$ (a distancia $\lambda/2\sin\theta$ en la
dirección transversal, de modo que la diferencia de camino es $\lambda/2$) cuyo campo interfiere
destructivamente. La dispersión en $\theta=0$ es la **dispersión coherente hacia adelante**, origen
del índice de refracción (Feynman *et al.*, 1963, §31). La dispersión requiere **fluctuaciones** en
alguna propiedad óptica: p. ej. si la densidad no es uniforme, el número de moléculas en $dV_1$ y
$dV_2$ difiere y la cancelación no es exacta.

Tensor dieléctrico (isótropo en promedio; Landau y Lifshitz, 1960):
$$\epsilon_{ik}=\bar\epsilon\,\delta_{ik}+\Delta\epsilon_{ik}, \qquad\text{(8.1.1, p. 393)}$$
con $\bar\epsilon$ la constante dieléctrica media y $\Delta\epsilon_{ik}$ las fluctuaciones (temporales y/o
espaciales). Descomposición en parte escalar y parte tensorial sin traza:
$$\Delta\epsilon_{ik}=\Delta\epsilon\,\delta_{ik}+\Delta\epsilon^{(t)}_{ik}, \qquad\text{(8.1.2, p. 394)}$$
- $\Delta\epsilon$ (escalar): fluctuaciones de presión, entropía, densidad o temperatura (y de concentración en
  soluciones) → **dispersión escalar**: Brillouin y Rayleigh.
- $\Delta\epsilon^{(t)}_{ik}$ ($\sum_i\Delta\epsilon^{(t)}_{ii}=0$) → **dispersión tensorial**:
$$\Delta\epsilon^{(t)}_{ik}=\Delta\epsilon^{(s)}_{ik}+\Delta\epsilon^{(a)}_{ik}, \qquad\text{(8.1.3, p. 394)}$$
  con la parte simétrica $\Delta\epsilon^{(s)}_{ik}=\Delta\epsilon^{(s)}_{ki}$ → Rayleigh‑wing, y la antisimétrica
  $\Delta\epsilon^{(a)}_{ik}=-\Delta\epsilon^{(a)}_{ki}$ → Raman.

$\Delta\epsilon$, $\Delta\epsilon^{(s)}_{ik}$ y $\Delta\epsilon^{(a)}_{ik}$ son estadísticamente independientes. La dispersión debida a
$\Delta\epsilon^{(t)}_{ik}$ se llama **despolarizada** (el grado de polarización de la luz dispersada es en general
menor que el de la incidente).

#### 8.1.2 Scattering Coefficient (p. 394)

Haz de intensidad $I_0$ sobre un volumen $V$; intensidad dispersada $I_s$ medida a distancia $L$
(Fig. 8.1.3: volumen de dispersión, ángulo $\theta$, detector de área $dA$). Suponiendo linealidad en
$I_0$ y en $V$ y ley del inverso del cuadrado:
$$I_s=\frac{I_0RV}{L^2}, \qquad\text{(8.1.4, p. 394)}$$
$R$ = **coeficiente de dispersión**. Con un detector de área proyectada $dA$, $dP=I_s\,dA$ y
$d\Omega=dA/L^2$, de modo que $dP/d\Omega=I_sL^2$:
$$\frac{dP}{d\Omega}=I_0RV. \qquad\text{(8.1.5, p. 395)}$$
Cualquiera de las dos sirve como definición de $R$ (dimensiones de inverso de longitud). Para luz
visible dispersada a 90°: $R=2\times10^{-8}\ \text{cm}^{-1}$ en aire y $1.4\times10^{-4}\ \text{m}^{-1}$ en agua (p. 395;
ver nota de unidades en *Erratas*).

#### 8.1.3 Scattering Cross Section (p. 395)

Molécula individual iluminada con $I_0$ (Fig. 8.1.4); potencia total dispersada
$$P=\sigma I_0, \qquad\text{(8.1.6, p. 395)}$$
$\sigma$ = sección eficaz total (área efectiva para remover luz del haz). Sección eficaz diferencial:
$$\frac{dP}{d\Omega}=I_0\frac{d\sigma}{d\Omega}, \qquad\text{(8.1.7, p. 396)}\qquad
\sigma=\int_{4\pi}\frac{d\sigma}{d\Omega}\,d\Omega. \qquad\text{(8.1.8)}$$
Si las $\mathcal N$ moléculas del volumen $V$ dispersan **independientemente**, comparando con (8.1.5):
$$R=\frac{\mathcal N}{V}\frac{d\sigma}{d\Omega}. \qquad\text{(8.1.9, p. 396)}$$
Advertencia del libro: no es de validez general; un medio completamente homogéneo tiene $R=0$, no
$(\mathcal N/V)\,d\sigma/d\Omega$. Regla: (8.1.9) vale para medios **diluidos** y es totalmente inválida para
materia condensada.

### 8.2 Microscopic Theory of Light Scattering (p. 396)

Tratamiento por el campo dispersado por cada molécula; adecuado para gases diluidos (efectos
colectivos despreciables). Geometría (Fig. 8.2.1, p. 397): luz polarizada linealmente incide sobre
una molécula; $\theta$ = ángulo de dispersión, $\phi$ = ángulo entre el dipolo inducido y la dirección de
observación $\mathbf r$.

Campo incidente e intensidad:
$$\tilde{\mathbf E}=\mathbf E_0e^{-i\omega t}+\text{c.c.},\qquad I_0=(2nc\epsilon_0)|\mathbf E_0|^2 \qquad\text{(8.2.1, p. 397)}$$
sobre una molécula mucho menor que $\lambda$. Dipolo inducido, con polarizabilidad $\alpha(\omega)$:
$$\tilde{\mathbf p}=\epsilon_0\alpha(\omega)\mathbf E_0e^{-i\omega t}+\text{c.c.} \qquad\text{(8.2.2, p. 397)}$$
Intensidad radiada a distancia $L$ (vector de Poynting; Jackson 1982, §9.2):
$$I_s=\frac{n\langle\ddot{\tilde p}^2\rangle}{16\pi^2\epsilon_0c^3L^2}\sin^2\phi=\frac{n\omega^4\epsilon_0|\alpha(\omega)|^2|\mathbf E_0|^2}{8\pi^2c^3L^2}\sin^2\phi \qquad\text{(8.2.3, p. 397)}$$
($\langle\ \rangle$ = promedio temporal; $\langle\ddot{\tilde p}^2\rangle=2\omega^4\epsilon_0^2|\alpha|^2|\mathbf E_0|^2$).
Con $d\sigma/d\Omega=(dP/d\Omega)/I_0=I_sL^2/I_0$:
$$\frac{d\sigma}{d\Omega}=\frac{1}{16\pi^2}\frac{\omega^4}{c^4}|\alpha(\omega)|^2\sin^2\phi. \qquad\text{(8.2.4, p. 398)}$$
La dependencia $\sin^2\phi$ vale para cualquier $\alpha(\omega)$: es consecuencia de suponer el dispersor
pequeño frente a $\lambda$ (solo dipolo eléctrico, sin multipolos). Integrando ($\int\sin^2\phi\,d\Omega=8\pi/3$):
$$\sigma=\int_{4\pi}d\Omega\frac{d\sigma}{d\Omega}=\frac{8\pi}{3}\frac{1}{16\pi^2}\frac{\omega^4}{c^4}|\alpha(\omega)|^2=\frac{1}{6\pi}\frac{\omega^4}{c^4}|\alpha(\omega)|^2. \qquad\text{(8.2.5, p. 398)}$$
Para polarización en el plano de la Fig. 8.2.1, $\theta+\phi=90°$:
$$\left(\frac{d\sigma}{d\Omega}\right)_p=\frac{1}{16\pi^2}\frac{\omega^4}{c^4}|\alpha(\omega)|^2\cos^2\theta. \qquad\text{(8.2.6, p. 398)}$$
Para polarización perpendicular al plano, $\phi=90°$ para todo $\theta$:
$$\left(\frac{d\sigma}{d\Omega}\right)_s=\frac{1}{16\pi^2}\frac{\omega^4}{c^4}|\alpha(\omega)|^2. \qquad\text{(8.2.7, p. 398)}$$
Luz no polarizada (promedio de ambas):
$$\left(\frac{d\sigma}{d\Omega}\right)_{\text{unpolarized}}=\frac{1}{32\pi^2}\frac{\omega^4}{c^4}|\alpha(\omega)|^2(1+\cos^2\theta). \qquad\text{(8.2.8, p. 398)}$$

**Ejemplo: átomo de Lorentz.** Con (1.4.17), (1.4.10) y $\chi(\omega)=N\alpha(\omega)$:
$$\alpha(\omega)=\frac{e^2/m\epsilon_0}{\omega_0^2-\omega^2-2i\omega\gamma}, \qquad\text{(8.2.9, p. 399)}$$
($\omega_0$ resonancia, $\gamma$ tasa de amortiguamiento dipolar), y
$$\sigma=\frac{8\pi}{3}\left(\frac{e^2}{4\pi\epsilon_0mc^2}\right)^2\frac{\omega^4}{(\omega_0^2-\omega^2)^2+4\omega^2\gamma^2}. \qquad\text{(8.2.10, p. 399)}$$
Fig. 8.2.2: $\sigma(\omega)$ nula en $\omega=0$, pico lorentziano de ancho $2\gamma$ en $\omega_0$ y meseta constante a alta
frecuencia. Límites:
$$\sigma=\frac{8\pi}{3}\left(\frac{e^2}{4\pi\epsilon_0mc^2}\right)^2\frac{\omega^4}{\omega_0^4}\quad(\omega\ll\omega_0), \qquad\text{(8.2.11a)}$$
$$\sigma=\frac{2\pi}{3}\left(\frac{e^2}{4\pi\epsilon_0mc^2}\right)^2\frac{\omega_0^2}{(\omega_0-\omega)^2+\gamma^2}\quad(\omega\simeq\omega_0), \qquad\text{(8.2.11b)}$$
$$\sigma=\frac{8\pi}{3}\left(\frac{e^2}{4\pi\epsilon_0mc^2}\right)^2\quad(\omega\gg\omega_0). \qquad\text{(8.2.11c, p. 399)}$$
(a) $\sigma\propto\omega^4$: **dispersión de Rayleigh** (cielo azul). (b) forma lorentziana cerca de resonancia.
(c) constante del orden de $r_e^2$, con el radio clásico del electrón $r_e=e^2/4\pi\epsilon_0mc^2=2.82\times10^{-15}$ m:
**dispersión Thomson** (el libro escribe "Thompson", p. 400).

**Ejemplo: esferas dieléctricas pequeñas** (radio $a\ll\lambda$, constante dieléctrica $\epsilon_1$ dentro, $\epsilon$ fuera;
electrostática, Stratton 1941 p. 206; Jackson 1982 p. 158):
$$\alpha=4\pi\epsilon\,\frac{\epsilon_1-\epsilon}{\epsilon_1+2\epsilon}\,a^3. \qquad\text{(8.2.12, p. 400)}$$
$\alpha$ depende de la frecuencia solo a través de $\epsilon(\omega)$, $\epsilon_1(\omega)$. Con (8.2.5):
$$\sigma=16\pi^2\,\frac{8\pi}{3}\frac{\omega^4}{c^4}\,a^6\epsilon^2\left(\frac{\epsilon_1-\epsilon}{\epsilon_1+2\epsilon}\right)^2 \quad\text{(tal como está impreso; ver Erratas)} \qquad\text{(8.2.13, p. 400)}$$
De nuevo $\sigma\propto\omega^4$, y $\sigma\propto(\text{volumen})^2$.

**Colección de moléculas** (Fig. 8.2.3, p. 401): se divide $V$ en celdas $V'$ tan pequeñas que todas
las moléculas de cada celda radian en fase:
$$I_{V'}=\nu^2I_{\text{mol}}, \qquad\text{(8.2.14, p. 400)}$$
$\nu$ = número de moléculas en $V'$. Por el argumento de 8.1, la cancelación entre celdas es completa
si todas tienen el mismo número de moléculas; solo la fluctuación contribuye, con
$\overline{\Delta\nu^2}=\overline{\nu^2}-\bar\nu^2$:
$$I_V=I_{\text{mol}}\overline{\Delta\nu^2}\,\frac{V}{V'} \qquad\text{(8.2.15, p. 401)}$$
($V/V'$ = número de celdas). $I_V=0$ si la fluctuación se anula. Gas ideal (posiciones no
correlacionadas, estadística de Poisson), con $N$ la densidad numérica media:
$$\bar\nu=NV', \qquad\text{(8.2.16)}\qquad \overline{\Delta\nu^2}=\overline{\nu^2}-\bar\nu^2=\bar\nu, \qquad\text{(8.2.17, p. 401)}$$
$$I_V=\bar\nu\frac{V}{V'}I_{\text{mol}}=NVI_{\text{mol}}=\mathcal NI_{\text{mol}}. \qquad\text{(8.2.18, p. 402)}$$
Para gas ideal la intensidad total es la de una molécula por el número total $\mathcal N=NV$; vale (8.1.9):
$$R=N\frac{d\sigma}{d\Omega}, \qquad\text{(8.2.19)}\qquad R=\frac{N}{16\pi^2}\frac{\omega^4}{c^4}|\alpha(\omega)|^2\sin^2\phi. \qquad\text{(8.2.20, p. 402)}$$
Si el medio es tan diluido que
$$n=1+\tfrac12N\alpha(\omega), \qquad\text{(8.2.21)}$$
$$R=\frac{\omega^4}{c^4}\frac{|n-1|^2}{4\pi^2N}\sin^2\phi. \qquad\text{(8.2.22, p. 402)}$$
Permite determinar $N$ a partir de dos constantes ópticas ($n$ y $R$ a un $\phi$ fijo); la primera
medición precisa del número de Loschmidt ($N_0=2.7\times10^{19}\ \text{cm}^{-3}$ a TPE) se hizo así.

### 8.3 Thermodynamic Theory of Scalar Light Scattering (p. 402)

Descripción macroscópica: la dispersión surge de fluctuaciones de la constante dieléctrica escalar,
que a su vez provienen de fluctuaciones termodinámicas (densidad, temperatura). Se divide $V$ en
celdas $V'$ que radian en fase en la dirección $\theta$; $\Delta\epsilon$ = fluctuación promediada en $V'$. Como
$\epsilon=1+\chi$, $\Delta\chi=\Delta\epsilon$, y la celda adquiere
$$\tilde{\mathbf P}=\Delta\chi\tilde{\mathbf E}_0=\Delta\epsilon\tilde{\mathbf E}_0, \qquad\text{(8.3.1, p. 403)}$$
$$\tilde{\mathbf p}=\epsilon_0V'\tilde{\mathbf P}=\epsilon_0\Delta\epsilon V'\tilde{\mathbf E}_0. \qquad\text{(8.3.2, p. 403)}$$
(En (8.3.1) $\tilde{\mathbf P}$ se usa sin el factor $\epsilon_0$, que se reintroduce en (8.3.2).) Con (8.2.3),
$I_s=(nc\epsilon_0)\langle\tilde E_s^2\rangle$ e $I_0=(nc\epsilon_0)\langle\tilde E_0^2\rangle$:
$$I_s=I_0\frac{\omega^4V'^2\langle\Delta\epsilon^2\rangle\sin^2\phi}{16\pi^2L^2c^4}, \qquad\text{(8.3.3, p. 403)}$$
intensidad de una celda; el total es $V/V'$ veces mayor porque las fluctuaciones de celdas distintas no
están correlacionadas.

Tomando $\rho$ y $T$ como variables independientes:
$$\Delta\epsilon=\left(\frac{\partial\epsilon}{\partial\rho}\right)_T\Delta\rho+\left(\frac{\partial\epsilon}{\partial T}\right)_\rho\Delta T. \qquad\text{(8.3.4, p. 403)}$$
El segundo término suele despreciarse (error ≈ 2 %, Fabelinskii 1968), porque $\epsilon$ depende mucho más de
$\rho$ que de $T$ (por eso no importa retener el subíndice $T$). Así $\langle\Delta\epsilon^2\rangle=(\partial\epsilon/\partial\rho)^2\langle\Delta\rho^2\rangle$, o
$$\langle\Delta\epsilon^2\rangle=\gamma_e^2\frac{\langle\Delta\rho^2\rangle}{\rho_0^2}, \qquad\text{(8.3.5, p. 403)}$$
con $\rho_0$ la densidad media y la **constante electrostrictiva**
$$\gamma_e=\left(\rho\frac{\partial\epsilon}{\partial\rho}\right)_{\rho=\rho_0} \qquad\text{(8.3.6, p. 404)}$$
(el nombre se justifica en §9.1). Por mecánica estadística (Fabelinskii 1968, Ap. I, Ec. (I.13);
Landau y Lifshitz 1969):
$$\frac{\langle\Delta\rho^2\rangle}{\rho_0^2}=\frac{kTC_T}{V'}, \qquad\text{(8.3.7, p. 404)}\qquad C_T=-\frac1V\left(\frac{\partial V}{\partial p}\right)_T \qquad\text{(8.3.8)}$$
($C_T$ = compresibilidad isotérmica). Interpretación: las fluctuaciones son de origen térmico; mayor
compresibilidad → mayor excursión; volumen menor → más fácil cambiar su densidad media.
Sustituyendo (8.3.5) y (8.3.7) en (8.3.3) y multiplicando por $V/V'$:
$$I_s=I_0\frac{\omega^4V}{16\pi^2L^2c^4}\gamma_e^2C_TkT\sin^2\phi, \qquad\text{(8.3.9a, p. 404)}$$
$$R=\frac{\omega^4}{16\pi^2c^4}\gamma_e^2C_TkT\sin^2\phi. \qquad\text{(8.3.9b, p. 404)}$$

#### 8.3.1 Ideal Gas (p. 404)

Ecuación de estado $pV=\mathcal NkT$ (8.3.10); $(\partial V/\partial p)_T=-\mathcal NkT/p^2$:
$$C_T=\frac{\mathcal NkT}{Vp^2}=\frac1p=\frac{V}{\mathcal NkT}. \qquad\text{(8.3.11, p. 405)}$$
Si $\epsilon-1\propto\rho$ ($\epsilon=1+A\rho$), $\partial\epsilon/\partial\rho=(\epsilon-1)/\rho$ y
$$\gamma_e=\epsilon-1. \qquad\text{(8.3.12, p. 405)}$$
Entonces, con $N=\mathcal N/V$:
$$I_s=I_0\frac{\omega^4V}{16\pi^2L^2c^4}\frac{(\epsilon-1)^2}{N}\sin^2\phi, \qquad\text{(8.3.13)}\qquad
R=\frac{(\epsilon-1)^2\omega^4\sin^2\phi}{16\pi^2c^4N}. \qquad\text{(8.3.14, p. 405)}$$
Como $\epsilon-1=2(n-1)$ en un gas diluido, coincide con el resultado microscópico (8.2.22).

#### 8.3.2 Spectrum of the Scattered Light (p. 405)

(8.3.9a) da la intensidad *total*; para el *espectro* hay que estudiar la dinámica de las
fluctuaciones de densidad:
$$\Delta\tilde\epsilon=\left(\frac{\partial\epsilon}{\partial\rho}\right)\Delta\tilde\rho. \qquad\text{(8.3.15, p. 405)}$$
Ahora se toman la entropía $s$ y la presión $p$ como variables independientes:
$$\Delta\tilde\rho=\left(\frac{\partial\rho}{\partial p}\right)_s\Delta\tilde p+\left(\frac{\partial\rho}{\partial s}\right)_p\Delta\tilde s. \qquad\text{(8.3.16, p. 405)}$$
Primer término: fluctuaciones de densidad **adiabáticas** (ondas acústicas) → **Brillouin**. Segundo:
fluctuaciones **isobáricas** (de entropía o temperatura) → **Rayleigh‑center**. Tienen ecuaciones de
movimiento muy distintas y, por tanto, espectros muy distintos.

#### 8.3.3 Brillouin Scattering (p. 406)

Ecuación de onda acústica para la presión (Fabelinskii 1968, §34.9):
$$\frac{\partial^2\Delta\tilde p}{\partial t^2}-\Gamma'\nabla^2\frac{\partial\Delta\tilde p}{\partial t}-v^2\nabla^2\Delta\tilde p=0, \qquad\text{(8.3.17, p. 406)}$$
con la velocidad del sonido
$$v^2=\left(\frac{\partial p}{\partial\rho}\right)_s. \qquad\text{(8.3.18)}$$
Compresibilidad y módulo volumétrico:
$$C\equiv\frac1K=-\frac1V\frac{\partial V}{\partial p}=\frac1\rho\frac{\partial\rho}{\partial p}. \qquad\text{(8.3.19, p. 406)}$$
Isotérmica vs. adiabática:
$$\frac{C_T}{C_s}=\frac{c_p}{c_V}\equiv\gamma \qquad\text{(8.3.20)}$$
($c_p$, $c_V$ calores específicos por unidad de masa, J/(kg K); $\gamma$ = índice adiabático), de modo que
$$v^2=\frac{K_s}{\rho}=\frac{1}{C_s\rho}. \qquad\text{(8.3.21, p. 406)}$$
Gas ideal: $C_s=C_T/\gamma=1/\gamma p$, y
$$v=\left(\frac{\gamma p}{\rho}\right)^{1/2}=\left(\frac{\gamma\mathcal NkT}{\rho V}\right)^{1/2}=\left(\frac{\gamma kT}{\mu}\right)^{1/2}, \qquad\text{(8.3.22, p. 407)}$$
$\mu$ = masa molecular: la velocidad del sonido es del orden de la velocidad térmica media.

**Tabla 8.3.1** (p. 407) — velocidades del sonido típicas $v$ (m/s):

| Material | $v$ (m/s) |
|---|---|
| *Gases*: aire seco | $3.31\times10^2$ |
| He | $9.65\times10^2$ |
| H₂ | $12.84\times10^2$ |
| vapor de agua | $4.94\times10^2$ |
| *Líquidos*: CS₂ | $1.15\times10^3$ |
| CCl₄ | $0.93\times10^3$ |
| etanol | $1.21\times10^3$ |
| agua | $1.50\times10^3$ |
| *Sólidos*: sílice fundida | $5.97\times10^3$ |
| lucita | $2.68\times10^3$ |

Parámetro de amortiguamiento:
$$\Gamma'=\frac1\rho\left[\frac43\eta_s+\eta_b+\frac{\kappa}{C_p}(\gamma-1)\right], \qquad\text{(8.3.23, p. 407)}$$
$\eta_s$ = viscosidad de cizalla, $\eta_b$ = viscosidad volumétrica (bulk), $\kappa$ = conductividad térmica; en la
mayoría de materiales ópticos el último término es mucho menor que los dos primeros (convenciones de
viscosidad: Apéndice de §9.6). Onda de prueba:
$$\Delta\tilde p=\Delta p\,e^{i(qz-\Omega t)}+\text{c.c.} \qquad\text{(8.3.24, p. 407)}$$
Sustituida en (8.3.17) da la relación de dispersión
$$\Omega^2=q^2(v^2-i\Omega\Gamma'), \qquad\text{(8.3.25, p. 408)}$$
$$q^2=\frac{\Omega^2}{v^2-i\Omega\Gamma'}=\frac{\Omega^2/v^2}{1-i\Omega\Gamma'/v^2}\simeq\frac{\Omega^2}{v^2}\left(1+\frac{i\Omega\Gamma'}{v^2}\right), \qquad\text{(8.3.26)}$$
$$q\simeq\frac\Omega v+\frac{i\Gamma}{2v}, \qquad\text{(8.3.27)}\qquad \Gamma=\Gamma'q^2 \qquad\text{(8.3.28, p. 408)}$$
($\Gamma$ = tasa de decaimiento del fonón; aproximación válida si $\Omega\Gamma'\ll v^2$). La intensidad acústica decae como
$$|\Delta p(z)|^2=|\Delta p(0)|^2e^{-\alpha_sz}, \qquad\text{(8.3.29)}\qquad \alpha_s=\frac{q^2\Gamma'}{v}=\frac\Gamma v, \qquad\text{(8.3.30)}$$
$$\tau_p=\frac1\Gamma=\frac1{q^2\Gamma'} \qquad\text{(8.3.31, p. 408)}$$
(coeficiente de absorción del sonido y tiempo de vida del fonón).

Tasa de dispersión por estas ondas acústicas. Campo incidente y ecuación de onda con fuente:
$$\tilde E_0(z,t)=E_0e^{i(\mathbf k\cdot\mathbf r-\omega t)}+\text{c.c.}, \qquad\text{(8.3.32)}\qquad
\nabla^2\tilde E-\frac{n^2}{c^2}\frac{\partial^2\tilde E}{\partial t^2}=\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde P}{\partial t^2}. \qquad\text{(8.3.33, p. 408)}$$
(Misma forma que la ecuación de onda (2.1.17) del libro.) Con $\tilde P=\epsilon_0(\partial\epsilon/\partial\rho)\Delta\tilde\rho\tilde E_0$ y solo la parte adiabática
$\Delta\tilde\rho=(\partial\rho/\partial p)_s\Delta\tilde p$:
$$\tilde P(\mathbf r,t)=\epsilon_0\left(\frac{\partial\epsilon}{\partial\rho}\right)\left(\frac{\partial\rho}{\partial p}\right)_s\Delta\tilde p\,\tilde E_0=\epsilon_0\gamma_eC_s\Delta\tilde p(\mathbf r,t)\tilde E_0(z,t), \qquad\text{(8.3.34, p. 409)}$$
Componente típica de la perturbación de presión térmica:
$$\Delta\tilde p(\mathbf r,t)=\Delta p\,e^{i(\mathbf q\cdot\mathbf r-\Omega t)}+\text{c.c.} \qquad\text{(8.3.35)}$$
Combinando:
$$\nabla^2\tilde{\mathbf E}-\frac{n^2}{c^2}\frac{\partial^2\tilde{\mathbf E}}{\partial t^2}=-\frac{\gamma_eC_s}{c^2}\Big[(\omega-\Omega)^2E_0\Delta p^*e^{i(\mathbf k-\mathbf q)\cdot\mathbf r-i(\omega-\Omega)t}+(\omega+\Omega)^2E_0\Delta p\,e^{i(\mathbf k+\mathbf q)\cdot\mathbf r-i(\omega+\Omega)t}+\text{c.c.}\Big]. \qquad\text{(8.3.36, p. 409)}$$
Primer término → Stokes; segundo → anti‑Stokes.

#### 8.3.4 Stokes Scattering (First Term in Eq. (8.3.36)) (p. 409)

Componente de la polarización con
$$\mathbf k'\equiv\mathbf k-\mathbf q, \qquad\text{(8.3.37)}\qquad \omega'\equiv\omega-\Omega, \qquad\text{(8.3.38)}$$
$$\omega=|\mathbf k|c/n, \qquad\text{(8.3.39)}\qquad \Omega=|\mathbf q|v. \qquad\text{(8.3.40, p. 409)}$$
Se acopla eficientemente a la onda dispersada solo si se cumple la relación de dispersión óptica
$$\omega'=|\mathbf k'|c/n. \qquad\text{(8.3.41, p. 410)}$$
Para cada dirección de dispersión, $\mathbf q$ y $\Omega$ quedan fijados (Fig. 8.3.1: (a) $\mathbf k$ y $\mathbf k'$ formando el
ángulo $\theta$; (b) triángulo $\mathbf k'=\mathbf k-\mathbf q$; (c) la luz se dispersa en una onda acústica que **se aleja**).
Como $\Omega\ll\omega$, $|\mathbf k|\simeq|\mathbf k'|$ y
$$|\mathbf q|=2|\mathbf k|\sin(\theta/2), \qquad\text{(8.3.42)}\qquad \Omega=2|\mathbf k|v\sin(\theta/2)=2n\omega\frac vc\sin(\theta/2). \qquad\text{(8.3.43, p. 410)}$$
Desplazamiento nulo hacia adelante y máximo en retrodispersión ($\theta=180°$):
$$\Omega_{\max}=2n\frac vc\omega. \qquad\text{(8.3.44, p. 410)}$$
**Ejemplo numérico** (p. 411): $\omega/2\pi=3\times10^{14}$ Hz ($\lambda=1\ \mu$m), $v=1\times10^3$ m/s, $n=1.5$ →
$\Omega_{\max}/2\pi=3\times10^9$ Hz.

#### 8.3.5 Anti-Stokes Scattering (Second Term in Eq. (8.3.36)) (p. 411)

$$\mathbf k'\equiv\mathbf k+\mathbf q, \qquad\text{(8.3.45)}\qquad \omega'\equiv\omega+\Omega, \qquad\text{(8.3.46, p. 411)}$$
con $\omega=|\mathbf k|c/n$, $\Omega=|\mathbf q|v$ y la condición $\omega'=|\mathbf k'|c/n$. Igual que antes,
$$|\mathbf q|=2|\mathbf k|\sin(\theta/2), \qquad\text{(8.3.47)}\qquad \Omega=2n\omega\frac vc\sin(\theta/2). \qquad\text{(8.3.48, p. 411)}$$
Fig. 8.3.2: análoga a la 8.3.1, pero la onda acústica **se acerca** (la luz se refleja en una onda que
avanza hacia ella y gana frecuencia).

**Ancho de línea Brillouin.** Si se incluye la atenuación acústica, la luz dispersada en $\theta$ no es
monocromática; su ancho (FWHM) es
$$\delta\omega=1/\tau_p=\Gamma'q^2, \qquad\text{(8.3.49, p. 412)}$$
$$\delta\omega=4\Gamma'|\mathbf k|^2\sin^2(\theta/2)=4n^2\Gamma'\frac{\omega^2}{c^2}\sin^2(\theta/2). \qquad\text{(8.3.50)}$$
En retrodispersión, $\delta\omega/2\pi\sim100$ MHz típico para líquidos orgánicos. Cociente ancho/desplazamiento:
$$\frac{\delta\omega}{\Omega}=\frac{2n\Gamma'\omega}{vc}\sin(\theta/2). \qquad\text{(8.3.51, p. 412)}$$
Fig. 8.3.3: espectro con la línea central (Rayleigh, ancho $\delta\omega_c$) y dos líneas Brillouin desplazadas $\pm\Omega$
con ancho $\delta\omega$.

#### 8.3.6 Rayleigh Center Scattering (p. 412)

Contribución isobárica (segundo término de (8.3.16)), $\propto\Delta\tilde s$. La entropía obedece la misma ecuación
que la temperatura:
$$\rho c_p\frac{\partial\Delta\tilde s}{\partial t}-\kappa\nabla^2\Delta\tilde s=0, \qquad\text{(8.3.52, p. 412)}$$
una ecuación de **difusión**, no de onda. Solución:
$$\Delta\tilde s=\Delta s_0e^{-\delta t}e^{-i\mathbf q\cdot\mathbf r}, \qquad\text{(8.3.53, p. 413)}\qquad \delta=\frac{\kappa}{\rho c_p}q^2. \qquad\text{(8.3.54)}$$
Las ondas de entropía **no se propagan** → solo producen una componente no desplazada, de ancho
$\delta\omega_c=\delta$:
$$\delta\omega_c=\frac{4\kappa}{\rho c_p}|\mathbf k|^2\sin^2(\theta/2). \qquad\text{(8.3.55, p. 413)}$$
**Ejemplo**: agua líquida, $\kappa=6$ mW/(cm K), $\rho=1$ g/cm³, $c_p=4.2$ J/(g K); retrodispersión de luz de 500 nm:
$\delta\omega_c/2\pi=1.4\times10^7$ Hz (ver *Erratas*: el número sale con $|\mathbf k|=2\pi/\lambda_{\rm vacío}$).

**Relación de Landau–Placzek** (Fabelinskii 1968, Ec. (5.39)):
$$\frac{I_c}{2I_B}=\frac{c_p-c_v}{c_v}=\gamma-1, \qquad\text{(8.3.56, p. 413)}$$
$I_c$ = intensidad integrada de la componente central; $I_B$ = la de cada componente Brillouin.

### 8.4 Acoustooptics (p. 413)

El análisis anterior se aplica cuando la onda de sonido se impone externamente con un transductor:
moduladores de intensidad o frecuencia y deflectores de haces. Dos regímenes:

- **Bragg**: longitudes de interacción largas, donde importa el ajuste de fase; un solo haz difractado
  (analogía con rayos X en planos atómicos); eficiencia apreciable (> 50 %).
- **Raman–Nath**: longitud de interacción corta; el ajuste de fase no importa; suelen aparecer varios
  órdenes. (El criterio preciso se da en §8.4.2.)

#### 8.4.1 Bragg Scattering of Light by Sound Waves (p. 414)

Celda de Bragg (Fig. 8.4.1, p. 415: transductor alimentado con rf a $\Omega$ en la base; onda acústica viajera de
período $\Lambda$ que sube con velocidad $v$; haz de entrada $\mathbf k_1,\omega_1$ a ángulo $\theta$; salen el haz
transmitido y el dispersado $\mathbf k_2,\omega_2$). Onda acústica de frecuencia $\Omega$ y longitud de onda
$\Lambda=2\pi v/\Omega$. El campo dispersado por cada frente acústico es pequeño, pero se suma en fase si
(construcción de la Fig. 8.4.2: diferencia de camino $2\Lambda\sin\theta$)
$$\lambda=2\Lambda\sin\theta, \qquad\text{(8.4.1, p. 414)}$$
**condición de Bragg** ($\lambda$ = longitud de onda de la luz *en el medio*): la diferencia de camino entre
reflexiones en máximos acústicos sucesivos es una longitud de onda óptica.
**Ejemplo**: $v=1.5\times10^5$ cm/s, $\Omega/2\pi=200$ MHz → $\Lambda=2\pi v/\Omega=7.5\ \mu$m; con $\lambda=0.5\ \mu$m,
$\sin\theta=1/30$ y ángulo de deflexión $2\theta=4°$.

Como condición de ajuste de fase (Fig. 8.4.3(a)):
$$\mathbf k_2=\mathbf k_1+\mathbf q, \qquad\text{(8.4.2, p. 414)}$$
$$\omega_2=\omega_1+\Omega. \qquad\text{(8.4.3, p. 415)}$$
Como $\Omega\ll\omega_1$, $|\mathbf k_2|\simeq|\mathbf k_1|$. La Fig. 8.4.1 es el caso en que la onda acústica avanza hacia la
onda óptica incidente; para sonido en sentido opuesto:
$$\mathbf k_2=\mathbf k_1-\mathbf q, \qquad\text{(8.4.4a)}\qquad \omega_2=\omega_1-\Omega. \qquad\text{(8.4.4b, p. 415)}$$
Las Figs. 8.4.1 y 8.4.2 no cambian salvo el sentido de la velocidad del sonido; el diagrama de ajuste de
fase pasa de la Fig. 8.4.3(a) ($\mathbf q$ hacia arriba, $\mathbf k_2=\mathbf k_1+\mathbf q$) a la 8.4.3(b) ($\mathbf q$ hacia abajo), p. 416.

**Teoría.** Se considera el cambio $\Delta\tilde\epsilon$ inducido por la variación de densidad acústica, supuesto lineal:
$$\Delta\tilde\epsilon=\frac{\partial\epsilon}{\partial\rho}\Delta\tilde\rho=\gamma_e\frac{\Delta\tilde\rho}{\rho_0}. \qquad\text{(8.4.5, p. 416)}$$
Riguroso para líquidos; cualitativamente correcto para otros materiales. Para materiales anisótropos,
relación tensorial convencional con el **tensor elasto‑óptico** (strain‑optic) $p_{ijkl}$:
$$[\Delta(\epsilon^{-1})]_{ij}=\sum_{kl}p_{ijkl}S_{kl}, \qquad\text{(8.4.6)}\qquad S_{kl}=\frac12\left(\frac{\partial d_k}{\partial x_l}+\frac{\partial d_l}{\partial x_k}\right) \qquad\text{(8.4.7, p. 416)}$$
($S_{kl}$ = tensor de deformación; $d_k$ = componente $k$ del desplazamiento de una partícula). Si el cambio es pequeño:
$$(\Delta\epsilon)_{il}=-\sum_{jk}\epsilon_{ij}[\Delta(\epsilon^{-1})]_{jk}\epsilon_{kl}. \qquad\text{(8.4.8, p. 416)}$$

Geometría de la Fig. 8.4.4 (p. 417): $\mathbf q$ a lo largo de $z$, la luz atraviesa la celda a lo largo de $x$.
$$\tilde E_1=A_1e^{i(\mathbf k_1\cdot\mathbf r-\omega_1t)}+\text{c.c.}, \qquad\text{(8.4.9)}\qquad \tilde E_2=A_2e^{i(\mathbf k_2\cdot\mathbf r-\omega_2t)}+\text{c.c.}, \qquad\text{(8.4.10)}$$
con $\omega_2=\omega_1+\Omega$ y casi ajuste de Bragg
$$\mathbf k_2\simeq\mathbf k_1+\mathbf q. \qquad\text{(8.4.11, p. 417)}$$
$$\Delta\tilde\epsilon=\Delta\epsilon\,e^{i(\mathbf q\cdot\mathbf r-\Omega t)}+\text{c.c.}, \qquad\text{(8.4.12)}$$
con $\Delta\epsilon=\gamma_e\Delta\rho/\rho_0$ (o la componente tensorial apropiada de (8.4.6)). El campo total $\tilde E=\tilde E_1+\tilde E_2$ cumple
$$\nabla^2\tilde E-\frac{n^2+\Delta\tilde\epsilon}{c^2}\frac{\partial^2\tilde E}{\partial t^2}=0, \qquad\text{(8.4.13, p. 417)}$$
($n$ = índice sin onda acústica); $\Delta\tilde\epsilon$ oscila a $\Omega$ y acopla $\omega_1$ con $\omega_2=\omega_1+\Omega$.

Parte que oscila a $\omega_1$:
$$\frac{\partial^2A_1}{\partial x^2}+\frac{\partial^2A_1}{\partial z^2}+2ik_{1x}\frac{\partial A_1}{\partial x}+2ik_{1z}\frac{\partial A_1}{\partial z}-(k_{1x}^2+k_{1z}^2)A_1+\frac{n^2\omega_1^2}{c^2}A_1+\frac{\omega_2^2}{c^2}A_2\Delta\epsilon^*e^{i(\mathbf k_2-\mathbf k_1-\mathbf q)\cdot\mathbf r}=0. \qquad\text{(8.4.14, p. 418)}$$
Simplificaciones: (1) SVEA (se desprecian segundas derivadas); (2) $A_1$ depende solo de $x$ (invariancia
traslacional en $z$), $\partial A_1/\partial z=0$; (3) $k_{1x}^2+k_{1z}^2=n^2\omega_1^2/c^2$:
$$2ik_{1x}\frac{dA_1}{dx}=-\frac{\omega_2^2}{c^2}A_2\Delta\epsilon^*e^{i(\mathbf k_2-\mathbf k_1-\mathbf q)\cdot\mathbf r}. \qquad\text{(8.4.15)}$$
El desajuste $\mathbf k_2-\mathbf k_1-\mathbf q\equiv-\Delta\mathbf k$ solo puede tener componente $x$ (extensión infinita en $z$):
$$(\mathbf k_2-\mathbf k_1-\mathbf q)\cdot\mathbf r\equiv-\Delta k\,x, \qquad\text{(8.4.16)}$$
$$\frac{dA_1}{dx}=\frac{i\omega_2^2\Delta\epsilon^*}{2k_{1x}c^2}A_2e^{-i\Delta kx}, \qquad\text{(8.4.17)}\qquad
\frac{dA_2}{dx}=\frac{i\omega_1^2\Delta\epsilon}{2k_{2x}c^2}A_1e^{i\Delta kx}. \qquad\text{(8.4.18, p. 418)}$$
Con $\omega_1\simeq\omega_2\equiv\omega$ y $k_{1x}\simeq k_{2x}\equiv k_x$:
$$\frac{dA_1}{dx}=i\kappa A_2e^{-i\Delta kx}, \qquad\text{(8.4.19a)}\qquad \frac{dA_2}{dx}=i\kappa^*A_1e^{i\Delta kx}, \qquad\text{(8.4.19b)}$$
$$\kappa=\frac{\omega^2\Delta\epsilon^*}{2k_xc^2}. \qquad\text{(8.4.20, p. 419)}$$
Incidencia exacta al ángulo de Bragg ($\Delta k=0$):
$$\frac{dA_1}{dx}=i\kappa A_2,\qquad \frac{dA_2}{dx}=i\kappa^*A_1. \qquad\text{(8.4.21)}$$
Con $A_2(0)=0$ (condiciones de la Fig. 8.4.4):
$$A_1(x)=A_1(0)\cos(|\kappa|x), \qquad\text{(8.4.22a)}\qquad A_2(x)=\frac{i\kappa^*}{|\kappa|}A_1(0)\sin(|\kappa|x). \qquad\text{(8.4.22b, p. 419)}$$
$$|A_1(x)|^2+|A_2(x)|^2=|A_1(0)|^2 \qquad\text{(8.4.23)}$$
(conservación de la energía óptica, pues $\Omega\ll\omega$). **Eficiencia de difracción**:
$$\eta\equiv\frac{|A_2(L)|^2}{|A_1(0)|^2}=\sin^2(|\kappa|L). \qquad\text{(8.4.24, p. 419)}$$
Intensidad de la onda acústica ($K=1/C$ módulo volumétrico, $\Delta\rho$ amplitud compleja):
$$I=Kv\frac{\langle\Delta\tilde\rho^2\rangle}{\rho_0^2}=2Kv\left|\frac{\Delta\rho}{\rho_0}\right|^2, \qquad\text{(8.4.25, p. 419)}$$
y con (8.4.5), $I=2Kv|\Delta\epsilon|^2/\gamma_e^2$.
Constante de acoplamiento en función de la intensidad acústica, con $k_x=n(\omega/c)\cos\theta$:
$$|\kappa|=\frac{\omega\gamma_e}{2nc\cos\theta}\left(\frac{I}{2Kv}\right)^{1/2}. \qquad\text{(8.4.26, p. 420)}$$
**Ejemplo (agua)**: $n=1.33$, $\gamma_e=0.82$, $v=1.5\times10^3$ m/s, $K=2.19\times10^{11}$ "m²/Newton" (así impreso; ver
*Erratas*: debe ser $2.19\times10^{9}$ N/m²), $\cos\theta\simeq1$, $\lambda_{\rm vacío}=0.5\ \mu$m ($\omega=3.8\times10^{15}$ rad/s), intensidad acústica
$1.0$ W/cm² (≈ 1 W de potencia acústica en un haz de ≈ 1 cm de diámetro) → $|\kappa|=1.5\ \text{cm}^{-1}$. Conversión de 100 %
para $|\kappa|L=\pi/2$, es decir $L=1.0$ cm.

**Incidencia fuera del ángulo de Bragg** (Fig. 8.4.5: (a) $\theta_1=\theta_2=\theta_B$, $\Delta k=0$; (b) $\theta_1\neq\theta_2$, aparece $\Delta\mathbf k$ a lo
largo de $x$). Componentes $x$ y $z$ del diagrama (b), con $k_1\simeq k_2=k$:
$$k\cos\theta_1-k\cos\theta_2=\Delta k, \qquad\text{(8.4.27a)}\qquad k\sin\theta_1+k\sin\theta_2=q. \qquad\text{(8.4.27b, p. 420)}$$
Ángulo de Bragg:
$$\theta_B=\sin^{-1}\frac{q}{2k}=\sin^{-1}\frac{\lambda}{2\Lambda}; \qquad\text{(8.4.28, p. 421)}$$
si $\theta_1=\theta_B$, entonces $\theta_2=\theta_B$ y $\Delta k=0$. Fuera de Bragg:
$$\theta_1=\theta_B+\Delta\theta, \qquad\text{(8.4.29a)}\qquad \theta_2=\theta_B-\Delta\theta \qquad\text{(8.4.29b)}$$
($\Delta\theta\ll1$; (8.4.29b) mantiene (8.4.27b)). Desarrollando $\cos(\theta_B\pm\Delta\theta)=\cos\theta_B\mp(\sin\theta_B)\Delta\theta$ en (8.4.27a):
$$\Delta k=-\Delta\theta\,q. \qquad\text{(8.4.30, p. 421)}$$
Solución de (8.4.19) para $\Delta k$ arbitrario sin campo externo a $\omega_2$:
$$A_1(x)=e^{-i(1/2)\Delta kx}A_1(0)\left(\cos sx+i\frac{\Delta k}{2s}\sin sx\right), \qquad\text{(8.4.31a)}$$
$$A_2(x)=ie^{i(1/2)\Delta kx}A_1(0)\frac{\kappa^*}{s}\sin sx, \qquad\text{(8.4.31b)}$$
$$s^2=|\kappa|^2+\left(\tfrac12\Delta k\right)^2. \qquad\text{(8.4.32, p. 421)}$$
$$\eta(\Delta k)\equiv\frac{|A_2(L)|^2}{|A_1(0)|^2}=\frac{|\kappa|^2}{|\kappa|^2+(\frac12\Delta k)^2}\sin^2\left\{\left[|\kappa|^2+\left(\tfrac12\Delta k\right)^2\right]^{1/2}L\right\}. \qquad\text{(8.4.33, p. 421)}$$
Para $\Delta k\neq0$ el máximo es siempre < 100 %. Desarrollo en serie:
$$\eta(\Delta k)=\eta(0)+\Delta k\left.\frac{d\eta}{d(\Delta k)}\right|_{0}+\frac12(\Delta k)^2\left.\frac{d^2\eta}{d(\Delta k)^2}\right|_{0}+\cdots \qquad\text{(8.4.34, p. 422)}$$
y hasta segundo orden
$$\eta(\Delta k)=\eta(0)\left[1-\frac{(\Delta k)^2}{4|\kappa|^2}\left(1-\frac{|\kappa|L\cos(|\kappa|L)}{\sin(|\kappa|L)}\right)\right], \qquad\text{(8.4.35a)}\qquad \eta(0)=\sin^2(|\kappa|L). \qquad\text{(8.4.35b)}$$
(El libro imprime "$|\kappa|K\cos(|\kappa|L)$" en el numerador; ver *Erratas*.)

**Aplicaciones**: (i) **modulador de amplitud** (Fig. 8.4.6): frecuencia rf fija, amplitud modulada → varía la
profundidad de la rejilla acústica y con ella la intensidad del haz difractado; (ii) **deflector** (Fig. 8.4.7, p. 423):
se varía $\Omega$, cambia $\Lambda$ y con ello el ángulo $\theta_2$ de (8.4.29b); el rango útil está limitado porque $\eta$ cae fuera
del ángulo de Bragg (8.4.33).

#### 8.4.2 Raman–Nath Effect (p. 423)

Lo anterior supone que un rayo atraviesa muchos frentes acústicos (Fig. 8.4.8, p. 424):
$$L\tan\theta_1\gg\Lambda, \qquad\text{(8.4.36)}$$
junto con la condición de Bragg
$$\sin\theta_1=\frac{\lambda}{2\Lambda}. \qquad\text{(8.4.37)}$$
Con $\theta_1\ll1$ ($\tan\theta_1\simeq\theta_1$):
$$\frac{\lambda L}{\Lambda^2}\gg1 \qquad\text{(8.4.38, p. 423)}$$
→ régimen de **Bragg**. El límite opuesto es **Raman–Nath** (Fig. 8.4.9, p. 425): incidencia casi normal; el índice
varía con período $\Lambda$ y la luz se difracta en esa rejilla con dispersión angular característica
$$\delta\theta=\frac\lambda\Lambda. \qquad\text{(8.4.39, p. 423)}$$
Celda tan delgada que no hay difracción múltiple:
$$\delta\theta L<\Lambda, \qquad\text{(8.4.40)}\qquad \frac{\lambda L}{\Lambda^2}<1, \qquad\text{(8.4.41, p. 424)}$$
lo opuesto a (8.4.38).

Análisis. Onda acústica e índice:
$$\Delta\tilde\rho=\Delta\rho\,e^{i(qz-\Omega t)}+\text{c.c.}, \qquad\text{(8.4.42)}\qquad \Delta\tilde n=\Delta n\,e^{i(qz-\Omega t)}+\text{c.c.} \qquad\text{(8.4.43)}$$
Con $\tilde n=n_0+\Delta\tilde n$, $\tilde n=\tilde\epsilon^{1/2}$, $\tilde\epsilon=\epsilon_b+\Delta\tilde\epsilon$: $n_0=\epsilon_b^{1/2}$, $\Delta\tilde n=\Delta\tilde\epsilon/2n_0$, y con
$\Delta\tilde\epsilon=\gamma_e\Delta\tilde\rho/\rho_0$:
$$\Delta n=\frac{\gamma_e\Delta\rho}{2n_0\rho_0}. \qquad\text{(8.4.44, p. 424)}$$
Fases elegidas para que
$$\Delta\tilde n(z,t)=2\Delta n\sin(qz-\Omega t). \qquad\text{(8.4.45)}$$
Campo incidente y fase acumulada tras el espesor $L$:
$$\tilde E(\mathbf r,t)=Ae^{i(kx-\omega t)}+\text{c.c.}, \qquad\text{(8.4.46, p. 425)}$$
$$\phi=\Delta\tilde n\frac\omega cL=2\Delta n\frac\omega cL\sin(qz-\Omega t)\equiv\delta\sin(qz-\Omega t), \qquad\text{(8.4.47)}$$
$$\delta=2\Delta n\omega L/c \qquad\text{(8.4.48)}$$
(**índice de modulación**).
$$\tilde E(\mathbf r,t)=Ae^{i[kx-\omega t+\delta\sin(qz-\Omega t)]}+\text{c.c.} \qquad\text{(8.4.49)}$$
Con la identidad de Bessel (Jacobi–Anger)
$$e^{i\delta\sin y}=\sum_{l=-\infty}^{\infty}J_l(\delta)e^{ily}, \qquad\text{(8.4.50)}$$
$$\tilde E(\mathbf r,t)=A\sum_{l=-\infty}^{\infty}J_l(\delta)e^{i[(kx+lqz)-(\omega+l\Omega)t]}+\text{c.c.} \qquad\text{(8.4.51, p. 425)}$$
Superposición de ondas planas con frecuencias $\omega+l\Omega$ y vectores $\mathbf k+l\mathbf q$; el orden $l$ sale a (Fig. 8.4.10, $l=2$)
$$\theta_l=\tan^{-1}\left(\frac{lq}{k}\right)\simeq\frac{lq}{k}=\frac{l\lambda}{\Lambda}, \qquad\text{(8.4.52, p. 426)}$$
$$I_l=|A|^2J_l(\delta)^2. \qquad\text{(8.4.53)}$$
(8.4.48) y (8.4.53) son las **ecuaciones de Raman–Nath**.

**Onda estacionaria**:
$$\tilde n(z,t)=2\Delta n\cos\Omega t\sin qz, \qquad\text{(8.4.54)}$$
$$\phi=2\Delta n\frac\omega cL\cos\Omega t\sin qz\equiv\delta\cos\Omega t\sin qz, \qquad\text{(8.4.55)}$$
$$\tilde E(\mathbf r,t)=Ae^{i(kx-\omega t+\delta\cos\Omega t\sin qz)}+\text{c.c.}, \qquad\text{(8.4.56)}$$
$$\tilde E(\mathbf r,t)=A\sum_{l=-\infty}^{\infty}J_l(\delta\cos\Omega t)\exp[i(kx+lqz)-i\omega t]+\text{c.c.} \qquad\text{(8.4.57, p. 426)}$$
$$\theta_l\simeq\frac{lq}{k}=\frac{l\lambda}{\Lambda}, \qquad\text{(8.4.58)}\qquad I_l=|A|^2J_l(\delta\cos\Omega t)^2. \qquad\text{(8.4.59, p. 427)}$$
Cada componente queda **modulada en amplitud** (en vez de desplazada en frecuencia).

---

## Tablas y datos numéricos útiles

- **Tabla 8.1.1** (p. 392): desplazamiento / ancho / tiempo de relajación / ganancia estimulada —
  Raman 1000 cm⁻¹ / 5 cm⁻¹ / $10^{-12}$ s / $5\times10^{-5}$ m/MW; Brillouin 0.1 / $5\times10^{-3}$ / $10^{-9}$ / $10^{-4}$;
  Rayleigh 0 / $5\times10^{-4}$ / $10^{-8}$ / $10^{-6}$; Rayleigh‑wing 0 / 5 / $10^{-12}$ / $10^{-5}$.
- **Tabla 8.3.1** (p. 407): velocidades del sonido (aire seco 331 m/s; He 965; H₂ 1284; vapor de agua 494; CS₂ 1150;
  CCl₄ 930; etanol 1210; agua 1500; sílice fundida 5970; lucita 2680 m/s).
- $R$ a 90° en el visible: aire $2\times10^{-8}$ cm⁻¹; agua $1.4\times10^{-4}$ m⁻¹ $=1.4\times10^{-6}$ cm⁻¹ (p. 395).
- Radio clásico del electrón $r_e=2.82\times10^{-15}$ m (p. 400); número de Loschmidt $N_0=2.7\times10^{19}$ cm⁻³ (p. 402).
- Brillouin: $\Omega_{\max}/2\pi=3\times10^9$ Hz para $\lambda=1\ \mu$m, $v=10^3$ m/s, $n=1.5$ (p. 411); ancho $\delta\omega/2\pi\sim100$ MHz en
  retrodispersión para líquidos orgánicos (p. 412).
- Rayleigh central en agua (500 nm, retro): $\delta\omega_c/2\pi=1.4\times10^7$ Hz con $\kappa=6$ mW/(cm K), $\rho=1$ g/cm³,
  $c_p=4.2$ J/(g K) (p. 413).
- Celda de Bragg típica: $v=1.5\times10^5$ cm/s, $\Omega/2\pi=200$ MHz → $\Lambda=7.5\ \mu$m; $\lambda=0.5\ \mu$m → $2\theta=4°$ (p. 414).
- Bragg en agua: $\gamma_e=0.82$, $I_{\rm ac}=1$ W/cm² → $|\kappa|=1.5$ cm⁻¹, conversión total en $L=1.0$ cm (p. 420).
- Criterio de régimen: $\lambda L/\Lambda^2\gg1$ Bragg; $\lambda L/\Lambda^2<1$ Raman–Nath (pp. 423–424).

---

## Problemas (pp. 427–428)

1. *Light scattering in air.* Estimar numéricamente, con el modelo de Lorentz del átomo, la sección eficaz de
   dispersión del nitrógeno molecular (N₂) para luz visible de 500 nm. Usar el resultado para estimar el
   coeficiente de dispersión $R$ del aire en condiciones normales (STP). Comparar con el valor obtenido con la
   Ec. (8.2.22) y el índice de refracción conocido del aire. (El valor medido para dispersión a 90° de luz no
   polarizada, $R^u_{90}$, es aproximadamente $2\times10^{-8}$ cm⁻¹.) Estimar también la distancia de atenuación de la
   luz en el aire, es decir, la distancia de propagación en que la intensidad cae a $1/e$ por pérdidas de
   dispersión. [Resp.: $\alpha=(16\pi/3)R^u_{90}=3\times10^{-7}$ cm⁻¹ $=(33\ \text{km})^{-1}$.]
2. *Light scattering in water.* Con la Ec. (8.3.9b) y valores de manual de $\gamma_e$ y $C_T$, estimar $R$ para agua líquida
   a temperatura ambiente, dispersión a 90° de luz visible de 500 nm, y la distancia de atenuación de la luz en
   agua. [Resp.: con $C_T=4.5\times10^{-11}$ cm²/dina, $n=1.33$, $\gamma_e=(n^2-1)(n^2+2)/3=0.98$ y $T=300$ K,
   $R=2.8\times10^{-6}\sin^2\phi$ cm⁻¹, y para luz no polarizada a 90° $R^u_{90}=1.4\times10^{-6}$ cm⁻¹. La constante de
   atenuación es $\alpha=(16\pi/3)R^u_{90}=2.34\times10^{-5}$ cm⁻¹ $=(426\ \text{m})^{-1}$.]
3. *Polarizability of a dielectric sphere.* Verificar la Ec. (8.2.12).
4. *Acoustic attenuation in water.* Estimar numéricamente el coeficiente de absorción acústica $\alpha_s$ en agua a
   frecuencias de $10^3$, $10^6$ y $10^9$ Hz. [Resp.: la viscosidad de cizalla de baja frecuencia del agua es
   $\eta_s=0.01$ dina s/cm², y la relación de Stokes da $\eta_d=-(2/3)\eta_s$. Se obtiene $\Gamma'=0.66\times10^{-2}$ cm²/s. Como
   $\alpha_s=q^2\Gamma'/v$ y $q=\Omega/v$, con $v=1.5\times10^6$ cm/s, $\alpha_s=7.7\times10^{-14}$ cm⁻¹ a 1 kHz y $\alpha_s=7.7\times10^{-2}$ cm⁻¹ a
   1 GHz.] (Ver *Erratas* sobre $v$.)
5. *Inverse dielectric tensor.* Verificar la Ec. (8.4.8).
6. *Solution of the Bragg acoustooptics equations.* Verificar las Ecs. (8.4.31a) a (8.4.35b).
7. *Acoustooptic beam deflector.* Deflector acustoóptico: el ángulo de incidencia $\theta_1$ queda fijo y se varía la
   frecuencia acústica $\Omega$ para controlar el ángulo de deflexión $\theta_2$. Deducir una fórmula para el máximo ángulo de
   deflexión útil, definido arbitrariamente como aquel en que la eficiencia de difracción cae al 50 % de su
   máximo. Evaluarla para el caso tratado tras la Ec. (8.4.26), con $|\kappa|L=\pi/2$, $L=1.1$ cm y $\Lambda=30\ \mu$m.
   [Resp.: partiendo de la Ec. (8.4.25) [sic; debe ser (8.4.35)] y de la relación $\Delta k=-\tfrac12q\,\delta\theta$, la eficiencia cae
   50 % cuando el ángulo de incidencia aumenta en
   $$\delta\theta=\frac{2\sqrt2|\kappa|}{q}\left[1-\frac{|\kappa|L\cos|\kappa|L}{\sin|\kappa|L}\right]^{1/2}.$$
   Para $|\kappa|L=\pi/2$ (eficiencia 100 % en $\Delta k=0$) se simplifica a $\delta\theta=2\sqrt2|\kappa|/q$. Numéricamente, $2\delta\theta=0.22°$.]

## Referencias (p. 428)

Fabelinskii (1968) *Molecular Scattering of Light*, Plenum; Feynman, Leighton y Sands (1963) *Feynman
Lectures* vol. I; Jackson (1982) *Classical Electrodynamics*; Landau y Lifshitz (1960) *Electrodynamics of
Continuous Media* (cap. 14) y (1969) *Statistical Physics*; Stratton (1941) *Electromagnetic Theory*.
Lecturas adicionales: Fabelinskii (1997) en *Progress in Optics* XXXVII; Yariv (1975) *Quantum Electronics*;
Yariv y Yeh (1984) *Optical Waves in Crystals*.

---

## Relación con el curso y con el proyecto final

- **Curso.** El cap. 8 no está en los temas 4–6 del programa (Boyd caps. 1, 2, 4.1–4.2, 7.1–7.2), pero es la base
  conceptual de la dispersión estimulada (cap. 9, SBS; cap. 10, SRS). La Tabla 8.1.1 es una referencia rápida de
  órdenes de magnitud de Raman vs. Brillouin. La constante electrostrictiva $\gamma_e$ (8.3.6) reaparece en §9.1 y en
  la contribución electrostrictiva a $n_2$ (Boyd §4.1). El tratamiento de Bragg por modos acoplados (8.4.14)–(8.4.24)
  repite la técnica SVEA del cap. 2 (Boyd §2.2), con solución $\cos/\sin$ como en el acoplador direccional.
- **Proyecto final (SC en guías de SiN/Si).** (i) La dispersión Rayleigh por fluctuaciones (8.1.1, 8.2.15) es el
  mismo mecanismo físico que la pérdida por rugosidad de paredes en guías integradas (fluctuaciones de $\epsilon$ en la
  interfaz); explica la dependencia $\lambda^{-4}$ cualitativa de las pérdidas de dispersión de volumen. (ii) Brillouin
  espontáneo/estimulado y la Tabla 8.3.1 (sílice: $v\approx5.97$ km/s) dan la escala del desplazamiento Brillouin
  en guías ($\Omega/2\pi\sim$ 10–30 GHz en retrodispersión a 1.55 µm para SiO₂/SiN; estimación propia con (8.3.44),
  no del libro). (iii) Raman (fonones ópticos) es el mecanismo de la respuesta retardada $h_R(t)$ que entra en la
  GNLSE del supercontinuo; en SiN amorfo su ganancia es pequeña y ancha, en Si cristalino es estrecha (15.6 THz).
- **Proyecto (sensado de volumen).** La relación de Landau–Placzek y el coeficiente $R$ del agua
  ($1.4\times10^{-6}$ cm⁻¹) dan la escala de la dispersión espontánea en el analito acuoso del anillo sensor: despreciable
  frente a otras pérdidas.

---

## Erratas o dudas de lectura

1. **(8.2.13), p. 400.** Se lee $\sigma=16\pi^2\frac{8\pi}{3}\frac{\omega^4}{c^4}a^6\epsilon^2\left(\frac{\epsilon_1-\epsilon}{\epsilon_1+2\epsilon}\right)^2$. Sustituyendo (8.2.12) en (8.2.5),
   $\sigma=\frac{1}{6\pi}\frac{\omega^4}{c^4}16\pi^2\epsilon^2a^6(\dots)^2=\frac{8\pi}{3}\frac{\omega^4}{c^4}a^6\epsilon^2(\dots)^2$: por consistencia **sobra el factor $16\pi^2$**.
2. **(8.4.35a), p. 422.** Se lee "$|\kappa|K\cos(|\kappa|L)$" en el numerador; por consistencia (y como en la respuesta del
   Problema 7) debería ser $|\kappa|L\cos(|\kappa|L)$. Verificado desarrollando (8.4.33) a segundo orden en $\Delta k$.
3. **Ejemplo de Bragg en agua, p. 420.** Se lee $K=2.19\times10^{11}$ m²/Newton. El módulo volumétrico del agua es
   $\approx2.2\times10^9$ N/m² (unidades de presión), y es con $K=2.19\times10^9$ N/m² que (8.4.26) da $|\kappa|=1.5$ cm⁻¹ (comprobado:
   $\omega\gamma_e/2nc=3.9\times10^6$ m⁻¹, $(I/2Kv)^{1/2}=3.9\times10^{-5}$). Debería ser $2.19\times10^9$ N/m² (o $2.19\times10^{10}$ dina/cm²).
4. **p. 421**, texto previo a (8.4.30): se lee "(2k sin θ_B)Δθ = Δk"; desarrollando (8.4.27a) resulta
   $-(2k\sin\theta_B)\Delta\theta=\Delta k$, coherente con la ecuación (8.4.30) $\Delta k=-\Delta\theta\,q$ (falta el signo en el texto).
   También p. 419: "Eq. (8.4.19b) reduces to the set" debería referirse a (8.4.19) (ambas ecuaciones); igual en
   p. 421 "We next solve Eqs. (8.4.19b)".
5. **Problema 4, p. 427.** La respuesta usa $v=1.5\times10^6$ cm/s, pero la velocidad del sonido en agua es
   $1.5\times10^5$ cm/s (Tabla 8.3.1). Los números impresos ($7.7\times10^{-14}$ y $7.7\times10^{-2}$ cm⁻¹) corresponden a
   $v=1.5\times10^6$ cm/s; con el valor correcto, $\alpha_s=\Omega^2\Gamma'/v^3$ sería 1000 veces mayor ($\approx77$ cm⁻¹ a 1 GHz,
   $7.7\times10^{-11}$ cm⁻¹ a 1 kHz). Además la respuesta habla de $\eta_d$ (viscosidad de dilatación) mientras (8.3.23) usa $\eta_b$.
6. **Problema 2, p. 427.** $(n^2-1)(n^2+2)/3$ con $n=1.33$ da 0.966, no 0.98 (diferencia menor). Además en el texto
   (p. 420) se usa $\gamma_e=0.82$ para el agua: dos valores distintos de $\gamma_e$ del agua en el mismo capítulo.
7. **Problema 7, p. 428.** "Starting with Eq. (8.4.25)": por el contenido debería ser (8.4.35).
8. **Ejemplo Rayleigh central, p. 413.** El valor $\delta\omega_c/2\pi=1.4\times10^7$ Hz se reproduce usando $|\mathbf k|=2\pi/\lambda$ con
   $\lambda=500$ nm *en vacío*; con $|\mathbf k|=2\pi n/\lambda$ ($n=1.33$) daría $\approx2.5\times10^7$ Hz. No es error grave, pero conviene
   saber qué $k$ se usó.
9. **(8.3.1), p. 403.** $\tilde{\mathbf P}=\Delta\chi\tilde{\mathbf E}_0$ se escribe sin $\epsilon_0$ (que aparece luego en (8.3.2) como
   $\tilde{\mathbf p}=\epsilon_0V'\tilde{\mathbf P}$); el resultado final es consistente, pero la notación de $\tilde P$ difiere de la del resto del libro.
   En (8.4.7) el segundo término está impreso como $\partial d_l/dx_k$ (d recta); se entiende $\partial$.
10. **p. 400**: "Thompson scattering" → Thomson. **p. 395**: las unidades de $R$ se dan mezcladas (cm⁻¹ para aire,
    m⁻¹ para agua); no es error numérico.
