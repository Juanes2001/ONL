# Capítulo 17 — Semiconductor Photon Sources (Saleh & Teich, 2.ª ed.)

Páginas del libro 680–747 (PDF 702–769). Leído el 2026-11-05.

Fuente: B. E. A. Saleh y M. C. Teich, *Fundamentals of Photonics*, 2.ª ed., Wiley, 2007, cap. 17.
Convención del libro: dependencia temporal $e^{j\omega t}$, $j=\sqrt{-1}$; campos reales en caligráfica,
amplitudes complejas en negrita; unidades SI (las concentraciones de portadores el libro las da en
cm⁻³ y los coeficientes de ganancia en cm⁻¹, se conservan así). Las notaciones $\mathsf{n}$, $\mathsf{p}$,
$\mathsf{n}_0$, $\mathsf{p}_0$, $\Delta\mathsf{n}$ (el libro usa una fuente sans-serif para las
concentraciones de electrones y huecos, para distinguirlas del índice de refracción $n$) se transcriben
aquí como `n`, `p`, `Δn` en texto corrido y como $\mathsf{n}$ en LaTeX. $\mathsf{R}$ es la tasa de
inyección de pares (bombeo), $\mathfrak{R}$ la responsividad y $\mathcal{R}$ la reflectancia de potencia.

---

## Resumen del capítulo

El capítulo estudia las fuentes de fotones semiconductoras —diodos emisores de luz (LED), amplificadores
ópticos semiconductores (SOA), diodos superluminiscentes (SLD) y diodos láser (LD)— como transductores
electrón→fotón basados en una unión $p$–$n$ polarizada en directa (electroluminiscencia por inyección,
Fig. 17.0-1, p. 681). Parte de la teoría del cap. 16 (bandas, cuasi-niveles de Fermi, densidad
conjunta de estados) y de los caps. 14 y 15 (amplificadores y osciladores láser). Para el LED deduce el
flujo interno de fotones $\Phi=\eta_i\, i/e$, la eficiencia de extracción, la potencia de salida
$P_o=\eta_{ex}h\nu\, i/e$, la responsividad $\mathfrak{R}=\eta_{ex}\,1.24/\lambda_o$, el ancho espectral
$\Delta\nu\approx1.8kT/h$ y el tiempo de respuesta; después recorre los materiales III–V (GaAs, GaAsP,
InGaAsP, AlGaAs, AlInGaP, GaN, InGaN, AlGaN, AlInGaN) y los OLED. Para el SOA obtiene el coeficiente de
ganancia $\gamma_0(\nu)=(\lambda^2/8\pi\tau_r)\varrho(\nu)f_g(\nu)$, el ancho de banda
$E_g/h<\nu<(E_{fc}-E_{fv})/h$, el modelo lineal de ganancia pico $\gamma_p\approx\alpha(J/J_T-1)$ con la
densidad de corriente de transparencia $J_T=el\Delta\mathsf{n}_T/\eta_i\tau_r$, y justifica las
heteroestructuras dobles y los pozos cuánticos (densidad de estados escalonada). Para el LD combina ese
amplificador con el resonador Fabry–Perot de las caras clivadas: pérdidas $\alpha_r=(\alpha_s+\alpha_m)/\Gamma$,
corriente umbral $J_t=\frac{\alpha_r+\alpha}{\alpha}J_T$, flujo de salida
$\Phi_o=\eta_d(i-i_t)/e$, eficiencia diferencial externa $\eta_d=\eta_e\eta_i$, eficiencia de conversión
de potencia, características espectrales (modos longitudinales $\nu_F=c/2d$) y espaciales (modos
laterales, patrón de campo lejano $\lambda_o/l$ por $\lambda_o/w$), y operación monomodo (DBR, DFB). La
sección 17.4 cubre láseres de confinamiento cuántico (QW, MQW, capas tensionadas, hilos cuánticos, puntos
cuánticos, láseres de cascada cuántica) y láseres de microcavidad (micropilar, microdisco, microtoroide,
microesfera, cristal fotónico 2D), VCSEL y láseres de cristal fotónico, donde la reducción de la densidad
de modos $M(\nu)$ aumenta el factor $\beta$ de emisión espontánea acoplada y baja el umbral a μA.

---

## Secciones

### Introducción (p. 680–682)

- **Electroluminiscencia por inyección** (p. 681): los materiales de gap directo no brillan a temperatura
  ambiente porque hay muy pocos electrones/huecos térmicos; una polarización directa de la unión $p$–$n$
  inyecta electrones y huecos en la misma región del espacio y la radiación de recombinación resultante se
  llama *injection electroluminescence* (Sec. 13.5).
- **Fig. 17.0-1** (p. 681): la misma unión $p$–$n$ en directa operada como (a) LED, (b) SOA, (c) LD
  (con realimentación). Si la tensión directa supera cierto valor, hay inversión de población y la emisión
  estimulada supera a la absorción → SOA; con realimentación → LD.
- Aplicaciones (p. 681): LED visibles (indicadores, pantallas, señalización, iluminación, retroiluminación
  LCD), IR (controles remotos, ratones ópticos), UV (purificación de agua, esterilización, descontaminación,
  detección de agentes químicos/biológicos fluorescentes, comunicaciones encubiertas sin línea de vista).
  LD: DVD, comunicaciones por fibra de larga distancia, impresión, **bombeo óptico de amplificadores de
  fibra y láseres de estado sólido**; se modulan directamente con la corriente inyectada.
- Nota histórica (p. 680): el diodo láser se reportó casi simultáneamente en 1962 por GE, IBM y Lincoln
  Laboratory (MIT).

---

### 17.1 Light-Emitting Diodes (p. 682)

#### 17.1A Injection Electroluminescence (p. 682)

**Electroluminiscencia en equilibrio térmico** (p. 682). La recombinación radiativa e–h emite luz, pero en
equilibrio el flujo de fotones es despreciable.

- **Ejemplo 17.1-1, Photon Emission from GaAs in Thermal Equilibrium** (p. 682): con
  $\mathsf{n}_i\approx1.8\times10^6$ cm⁻³ y $\mathsf{r}_r\approx10^{-10}$ cm³/s, la tasa de
  electroluminiscencia $\mathsf{r}_r\mathsf{n}\mathsf{p}=\mathsf{r}_r\mathsf{n}_i^2\approx324$
  fotones/cm³·s; con $E_g=1.42$ eV $=1.42\times1.6\times10^{-19}$ J da una densidad de potencia
  $\approx7.4\times10^{-17}$ W/cm³; una capa de 2 μm produce $I\approx1.5\times10^{-20}$ W/cm², despreciable
  (capas más gruesas de 2 μm sufren reabsorción).
- Por la ley de acción de masas (16.1-14), $\mathsf{n}\mathsf{p}=\mathsf{n}_i^2$ está fijo si el dopado no
  es muy fuerte, así que dopar no aumenta la emisión: se necesita abundancia de electrones *y* huecos a la
  vez (p. 682).

**Electroluminiscencia con inyección de portadores** (p. 682–683). El bombeo (iluminación o, típicamente,
polarización directa de la unión $p$–$n$, Fig. 16.1-20) inyecta pares a una tasa $\mathsf{R}$
(pares/cm³·s), que juega el papel de la tasa de bombeo láser (Sec. 14.2). **Fig. 17.1-1** (p. 683):
portadores inyectados (tasa $\mathsf{R}$) → fotones emitidos (tasa $\Phi$).

Con $\mathsf{n}=\mathsf{n}_0+\Delta\mathsf{n}$, $\mathsf{p}=\mathsf{p}_0+\Delta\mathsf{p}$,
$\Delta\mathsf{n}=\Delta\mathsf{p}$ (se crean en pares) y tiempo de recombinación global (radiativo +
no radiativo) $\tau$, en estado estacionario generación = recombinación, $\mathsf{R}=\Delta\mathsf{n}/\tau$:

$$\Delta\mathsf{n}=\mathsf{R}\tau. \tag{17.1-1}$$

Para inyección débil $\tau\approx1/\mathsf{r}(\mathsf{n}_0+\mathsf{p}_0)$, con $\mathsf{r}$ el coeficiente
de recombinación (radiativo + no radiativo), así que $\mathsf{R}\approx\mathsf{r}\Delta\mathsf{n}(\mathsf{n}_0+\mathsf{p}_0)$ (p. 683).

Solo las recombinaciones radiativas generan fotones; la **eficiencia cuántica interna**
$\eta_i=\mathsf{r}_r/\mathsf{r}=\tau/\tau_r$ [(16.1-28), (16.1-30)] da el flujo de fotones generado en un
volumen $V$ (recuadro, p. 683):

$$\boxed{\Phi=\eta_i\mathsf{R}V=\eta_i\frac{V\Delta\mathsf{n}}{\tau}=\frac{V\Delta\mathsf{n}}{\tau_r}.}\tag{17.1-2}$$

$\eta_i$ depende del dopado, la temperatura y la concentración de defectos. Se usan semiconductores de gap
directo porque $\eta_i$ es mucho mayor: a temperatura ambiente $\eta_i\approx0.5$ para GaAs frente a
$\eta_i\approx10^{-5}$ para Si (Tabla 16.1-4) (p. 683).

- **Ejemplo 17.1-2, Injection Electroluminescence Emission from GaAs** (p. 684): con $\tau=50$ ns,
  $\eta_i=0.5$ y $\Delta\mathsf{n}=10^{17}$ cm⁻³, $\eta_i\Delta\mathsf{n}/\tau\approx10^{24}$
  fotones/cm³·s → densidad de potencia $\approx2.3\times10^5$ W/cm³ a $E_g=1.42$ eV; una lámina de 2 μm
  da $\approx46$ W/cm², $10^{21}$ veces el valor de equilibrio térmico. Un dispositivo de
  200 μm × 10 μm emite $\approx0.9$ mW.

**Intensidad espectral de los fotones de electroluminiscencia** (p. 684–685). Tasa de emisión espontánea
(fotones/s·Hz·cm³), de (16.2-17):

$$r_{sp}(\nu)=\frac{1}{\tau_r}\varrho(\nu)f_e(\nu),\tag{17.1-3}$$

con la densidad conjunta óptica de estados (16.2-9)

$$\varrho(\nu)=\frac{(2m_r)^{3/2}}{\pi\hbar^2}\sqrt{h\nu-E_g},\tag{17.1-4}$$

donde $1/m_r=1/m_v+1/m_c$ (masa reducida) y $E_g$ el gap. La condición de emisión (16.2-10):

$$f_e(\nu)=f_c(E_2)[1-f_v(E_1)],\tag{17.1-5}$$

probabilidad de que el estado de la banda de conducción

$$E_2=E_c+\frac{m_r}{m_c}(h\nu-E_g)\tag{17.1-6}$$

esté lleno *y* el estado de la banda de valencia

$$E_1=E_2-h\nu\tag{17.1-7}$$

esté vacío (conservación de energía y momento; **Fig. 17.1-2**, p. 685: transición vertical en el
diagrama $E$–$k$ porque el momento del fotón $h\nu/c$ es despreciable). Funciones de Fermi con
cuasi-niveles: $f_c(E)=1/\{\exp[(E-E_{fc})/kT]+1\}$, $f_v(E)=1/\{\exp[(E-E_{fv})/kT]+1\}$
(cuasi-equilibrio). Los parámetros $E_g,\tau_r,m_v,m_c,T$ y los cuasi-niveles $E_{fc},E_{fv}$ determinan
$r_{sp}(\nu)$; los cuasi-niveles salen de las concentraciones (16.1-10), (16.1-11):

$$\int_{E_c}^{\infty}\varrho_c(E)f_c(E)\,dE=\mathsf{n}=\mathsf{n}_0+\Delta\mathsf{n};\qquad
\int_{-\infty}^{E_v}\varrho_v(E)[1-f_v(E)]\,dE=\mathsf{p}=\mathsf{p}_0+\Delta\mathsf{n}.\tag{17.1-8}$$

Densidades de estados cerca de los bordes de banda [(16.1-7), (16.1-8)]:

$$\varrho_c(E)=\frac{(2m_c)^{3/2}}{2\pi^2\hbar^3}\sqrt{E-E_c};\qquad
\varrho_v(E)=\frac{(2m_v)^{3/2}}{2\pi^2\hbar^3}\sqrt{E_v-E}.\tag{17.1-9}$$

Para inyección débil (niveles de Fermi dentro del gap, a varios $kT$ de los bordes) las funciones de Fermi
se aproximan por sus colas exponenciales y el flujo espontáneo total es (p. 685)

$$\Phi=V\int_0^{\infty}r_{sp}(\nu)\,d\nu=\frac{V(m_r)^{3/2}}{\sqrt2\pi^{3/2}\hbar^3\tau_r}(kT)^{3/2}
\exp\!\left(\frac{E_{fc}-E_{fv}-E_g}{kT}\right),\tag{17.1-10}$$

extrapolado del Prob. 16.2-5. Al aumentar $\mathsf{R}$ sube $\Delta\mathsf{n}$, $E_{fc}$ se acerca a (o
entra en) la banda de conducción y $E_{fv}$ a la de valencia, y crece $f_e(\nu)$ y por tanto $r_{sp}$ y $\Phi$.

- **Ejercicio 17.1-1, Quasi-Fermi Levels of a Pumped Semiconductor** (p. 685–686). (a) A $T=0$ K sin
  generación térmica, mostrar que

$$E_{fc}=E_c+(3\pi^2)^{2/3}\frac{\hbar^2}{2m_c}(\Delta\mathsf{n})^{2/3},\tag{17.1-11a}$$
$$E_{fv}=E_v-(3\pi^2)^{2/3}\frac{\hbar^2}{2m_v}(\Delta\mathsf{n})^{2/3},\tag{17.1-11b}$$
$$E_{fc}-E_{fv}=E_g+(3\pi^2)^{2/3}\frac{\hbar^2}{2m_r}(\Delta\mathsf{n})^{2/3},\tag{17.1-11c}$$

  con $\Delta\mathsf{n}\gg\mathsf{n}_0,\mathsf{p}_0$ (todos los $\Delta\mathsf{n}$ electrones ocupan los
  niveles más bajos de la banda de conducción, y los $\Delta\mathsf{p}$ huecos los más altos de la de
  valencia; comparar con Ejercicio 16.1-3). (b) Esbozar $f_c(\nu)$ y $r_{sp}(\nu)$ para dos valores de
  $\Delta\mathsf{n}$ y determinar el efecto de la temperatura (Fig. 17.1-3).
- **Fig. 17.1-3** (p. 686): bandas y funciones de Fermi en cuasi-equilibrio (a) a $T=0$ K (escalones) y
  (b) a $T>0$ K (suavizadas).
- **Ejercicio 17.1-2, Spectral Intensity of Injection Electroluminescence under Weak Injection**
  (p. 686): si $E_c-E_{fc}\gg kT$ y $E_{fv}-E_v\gg kT$, mostrar que (recuadro)

$$\boxed{r_{sp}(\nu)=D\sqrt{h\nu-E_g}\,\exp\!\left(-\frac{h\nu-E_g}{kT}\right),\quad h\nu\ge E_g,}\tag{17.1-12a}$$

$$D=\frac{(2m_r)^{3/2}}{\pi\hbar^2\tau_r}\exp\!\left(\frac{E_{fc}-E_{fv}-E_g}{kT}\right),\tag{17.1-12b}$$

  función exponencialmente creciente de $E_{fc}-E_{fv}$. Tiene exactamente la misma forma que el espectro
  en equilibrio térmico (Fig. 16.2-9) pero magnificado por $D/D_0=\exp[(E_{fc}-E_{fv})/kT]$; en equilibrio
  $E_{fc}=E_{fv}$ y se recuperan (16.2-21), (16.2-22) (p. 686–687).
- **Fig. 17.1-4** (p. 687): $r_{sp}(\nu)$ vs $h\nu$ bajo inyección débil: arranca en $E_g$, pico cerca
  de $E_g$, cola exponencial; anchura $\sim kT$.
- **Ejercicio 17.1-3, Electroluminescence Spectral Linewidth** (p. 687). (a) El pico de (17.1-12) está en

$$\boxed{h\nu_p=E_g+\tfrac12kT.}\tag{17.1-13}\ \text{(Peak Frequency)}$$

  (b) La anchura total a media altura (FWHM) es

$$\boxed{\Delta\nu\approx1.8\,kT/h.}\tag{17.1-14}\ \text{(Spectral Width, Hz)}$$

  En compuestos puede ser mayor por la aleatoriedad de la composición (**alloy broadening**).
  (c) En longitud de onda $\Delta\lambda\approx1.8\lambda_p^2kT/hc$ con $\lambda_p=c/\nu_p$; con $kT$ en eV y
  $\lambda$ en μm,

$$\Delta\lambda\approx1.45\,\lambda_p^2\,kT.\tag{17.1-15}$$

  (d) Calcular $\Delta\nu$ y $\Delta\lambda$ a $T=300$ K para $\lambda_p=0.8$ μm y 1.6 μm.
  (Con $kT=0.0259$ eV: $\Delta\nu\approx1.8\times0.0259/4.136\times10^{-15}\approx11$ THz
  —el libro redondea a 10 THz en p. 695—; $\Delta\lambda\approx24$ nm a 0.8 μm y $\approx96$ nm a 1.6 μm.)

#### 17.1B LED Characteristics (p. 687)

El LED es una unión $p$–$n$ *polarizada en directa* con alta tasa de recombinación radiativa de los
portadores minoritarios inyectados; material usualmente de gap directo. Se determinan potencia, espectro,
patrón espacial, eficiencia, responsividad y tiempo de respuesta (p. 687).

**Flujo interno de fotones y eficiencia interna** (p. 688). **Fig. 17.1-5** (p. 688): diagrama de bandas de
una homounión $p$–$n$ fuertemente dopada y fuertemente polarizada en directa; los cuasi-niveles de Fermi
(líneas discontinuas) están separados por $eV$ y en la región de la unión coexisten electrones y huecos.
**Fig. 17.1-6** (p. 689): LED simple con región activa de espesor $l$.

Con corriente $i$, el número de portadores/s que cruzan la unión es $i/e$; tasa de inyección:

$$\mathsf{R}=\frac{i/e}{V},\tag{17.1-16}$$

$$\Delta\mathsf{n}=\frac{(i/e)\tau}{V},\tag{17.1-17}$$

y por (17.1-2) el **flujo interno de fotones** (recuadro, p. 688):

$$\boxed{\Phi=\eta_i\frac{i}{e}.}\tag{17.1-18}\ \text{(Internal Photon Flux)}$$

$\eta_i$ = (flujo de fotones generado)/(flujo de electrones inyectado). Se aumenta con dobles
heteroestructuras (Sec. 16.1F) y pozos cuánticos múltiples MQW (Sec. 16.1G): concentran portadores,
reducen $\tau_r$, elevan $\eta_i$ [(16.1-30), (16.1-31), (17.1-18)]; las capas de confinamiento deben estar
acopladas en red con la región activa; evitar superficies accesibles a ambos portadores (recombinación no
radiativa) (p. 689).

**Eficiencia de extracción** (p. 689–692). **Fig. 17.1-7** (p. 689): rayos $A$ (normal), $B$ (oblicuo),
$C$ (fuera del cono crítico, atrapado por reflexión total interna).

- Rayo $A$: atenuación por absorción en el material $n$ de espesor $l_1$,

$$\eta_1=\exp(-\alpha l_1),\tag{17.1-19}$$

  y transmisión de Fresnel en incidencia normal semiconductor–aire [(6.2-15)],

$$\eta_2=1-\frac{(n-1)^2}{(n+1)^2}=\frac{4n}{(n+1)^2};\tag{17.1-20}$$

  para GaAs $n=3.6$ → $\eta_2=0.68$. $\eta_A=\eta_1\eta_2$.
- Rayo $B$: más camino y más reflexión, $\eta_B<\eta_A$.
- Rayo $C$: fuera del ángulo crítico $\theta_c=\sin^{-1}(1/n)$ hay reflexión total interna. El casquete
  esférico subtendido tiene área $A=\int_0^{\theta_c}2\pi r\sin\theta\,r\,d\theta=2\pi r^2(1-\cos\theta_c)$,
  frente a $4\pi r^2$, así que la fracción dentro del cono es

$$\eta_3=\tfrac12(1-\cos\theta_c)=\tfrac12\left(1-\sqrt{1-1/n^2}\right)\approx1/4n^2.\tag{17.1-21}$$

  Para $n=3.6$ solo el 1.9 % puede transmitirse. Para un paralelepípedo con $n>\sqrt2$ la razón es
  $3[1-(1-1/n^2)^{1/2}]$ (Ejercicio 1.2-6). En la práctica $\eta_3$ puede ser mayor por absorción y
  reemisión dentro del cono (p. 690).

La **eficiencia de extracción $\eta_e$** es la eficiencia con que los fotones internos salen de la
estructura; capas antirreflejo (Ejercicio 7.1-1) reducen Fresnel y aumentan $\eta_e$ (p. 690).

- **Ejercicio 17.1-4, Extraction of Light from a Planar-Surface LED** (p. 690–691): (a) deducir (17.1-21);
  (b) ángulos críticos y fracción extraída hacia aire para GaAs ($n=3.6$), GaN ($n=2.5$) y polímero
  transparente ($n=1.5$), ignorando absorción y Fresnel; (c) mejora al recubrir un LED plano de GaAs con
  polímero de $n=1.5$; (d) índice del polímero que maximiza la fracción emitida hacia el aire si se tiene en
  cuenta Fresnel en las dos interfaces.

Formas de mejorar $\eta_e$ (p. 691–692): geometrías (**Fig. 17.1-8**: domo hemisférico, cilindro con
anillo de escape, cono invertido, pirámide invertida truncada), rugosidad/textura superficial
(**Fig. 17.1-9**), capas difusoras de corriente (*current-spreading / window layers*), capas bloqueadoras de
corriente, contactos reflectantes/transparentes, sustratos transparentes, reflectores de Bragg distribuidos
(cap. 7) entre región activa y sustrato absorbente, *flip-chip*, cristal fotónico 2D (Sec. 7.3A; huecos de
100–250 nm en la capa difusora), y **microrresonador** (Secs. 10.1B y 10.4; **Fig. 17.1-10**, p. 692: dos
espejos —100 % y ~50 %— forman una cavidad del tamaño de la longitud de onda que canaliza la emisión en un
modo resonante dentro del cono de extracción; véase Sec. 17.4B).

**Patrón espacial de la luz emitida** (p. 692–693). LED de superficie plana: radiador **lambertiano**,
intensidad $\propto\cos\theta$ ($\theta$ respecto a la normal), mitad a $\theta=60°$; se debe a la ley de
Snell. **Fig. 17.1-11**: LED encapsulado en epoxi (protege, reduce el desajuste de índice, actúa como
lente). **Fig. 17.1-12**: patrones (a) lambertiano, (b) lente hemisférica, (c) lente parabólica. Un epoxi
de índice intermedio da una mejora de 2–3× en extracción (p. 693). LED de borde y diodos láser: patrón
estrecho $\cos^s\theta$ con $s>1$; para $s=10$ la intensidad cae a la mitad a $\theta\approx21°$.

**Flujo de fotones de salida y eficiencia externa** (p. 693):

$$\Phi_o=\eta_e\Phi=\eta_e\eta_i\frac{i}{e},\tag{17.1-22}$$

$$\boxed{\eta_{ex}\equiv\eta_e\eta_i.}\tag{17.1-23}\ \text{(External Efficiency)}$$

$$\boxed{\Phi_o=\eta_{ex}\frac{i}{e},}\tag{17.1-24}\ \text{(External Photon Flux)}$$

$$\boxed{P_o=h\nu\Phi_o=\eta_{ex}h\nu\frac{i}{e}.}\tag{17.1-25}\ \text{(Output Power)}$$

Valores típicos (p. 694): $\eta_i$ entre 50 % y casi 100 %; $\eta_e$ hasta 50 % en dispositivos bien
diseñados; $\eta_{ex}$ típicamente < 50 %. **Eficiencia de conversión de potencia** (*wall-plug*):

$$\eta_c=\frac{P_o}{iV}=\eta_{ex}\frac{h\nu}{eV},\tag{17.1-26}$$

con $V$ la caída de tensión; si $h\nu\approx eV$, $\eta_c\approx\eta_{ex}$.

**Responsividad** (p. 694):

$$\mathfrak{R}=\frac{P_o}{i}=\frac{h\nu\Phi_o}{i}=\eta_{ex}\frac{h\nu}{e},\tag{17.1-27}$$

$$\boxed{\mathfrak{R}=\eta_{ex}\frac{1.24}{\lambda_o}.}\tag{17.1-28}\ \text{(LED Responsivity, W/A; }\lambda_o\text{ en μm)}$$

Ej.: a $\lambda_o=1.24$ μm, $\mathfrak{R}=\eta_{ex}$ W/A; con $\eta_{ex}=1/2$, 1 mA → 0.5 mW. La
proporcionalidad $P_o\propto i$ vale en un rango limitado: **Fig. 17.1-13** (p. 694), LED MQW InGaN/GaN a
420 nm, lineal hasta ~20 mA con pendiente 0.3 mW/mA (satura a mayor corriente); de (17.1-28)
$\eta_{ex}=0.10$.

**Distribución espectral** (p. 695). Para bombeo débil el pico está en $\nu_p=(E_g+kT/2)/h$ y la FWHM
$\Delta\nu\approx1.8kT/h$ ($\Delta\nu\approx10$ THz a 300 K, independiente de $\nu$); en longitud de onda

$$\boxed{\Delta\lambda\approx1.45\,\lambda_p^2\,kT,}\tag{17.1-29}\ \text{(Spectral Width, μm; }kT\text{ en eV)}$$

Ej.: $\lambda_p=1$ μm a 300 K → $\Delta\lambda\approx36$ nm. **Fig. 17.1-14** (p. 695): espectros
normalizados de LED UV (magenta) y visibles entre ~0.2 y 0.75 μm: AlN tiene el mayor gap de los nitruros
III (210 nm); AlGaN para UV medio y cercano; InGaN para violeta, azul y verde; AlInGaP para amarillo,
naranja y rojo. El ancho crece como $\lambda_p^2$; el LED verde muestra ensanchamiento adicional por
aleación. Espectros IR cercano (InGaAsP) en Fig. P17.1-5 (p. 745).

**Tiempo de respuesta** (p. 695–696). LED de iluminación: limitados por la constante $RC$ (gran área y
capacidad). LED de comunicaciones: limitados por el tiempo de vida $\tau$ de los portadores minoritarios
(ecuación diferencial lineal de primer orden, Sec. 16.1D). Con $i=i_0+i_1\cos(\Omega t)$ y respuesta lineal,
$P=P_0+P_1\cos(\Omega t+\varphi)$; la función de transferencia $H(\Omega)=(P_1/i_1)\exp(j\varphi)$ es

$$H(\Omega)=\frac{\mathfrak{R}}{1+j\Omega\tau},\tag{17.1-30}$$

tipo circuito $RC$: tiempo de subida $\tau$ y ancho de banda a 3 dB $B=1/2\pi\tau$ (Hz). Como
$1/\tau=1/\tau_r+1/\tau_{nr}$, reducir $\tau_{nr}$ baja $\eta_i=\tau/\tau_r$; conviene maximizar el producto
$\eta_iB=1/2\pi\tau_r$ reduciendo solo $\tau_r$ (elección de material y dopado). Tiempos de subida
típicos 1–50 ns → anchos de banda de hasta cientos de MHz (p. 696).

**Circuitería electrónica** (p. 696–697). **Fig. 17.1-15**: (a) fuente de corriente ideal, (b) fuente de
tensión + resistencia serie, (c) transistor para modulación analógica, (d) conmutación por transistor para
modulación digital. Iluminación arquitectónica: LED en serie con corriente PWM (nivel ∝ ciclo de trabajo);
bancos RGB para color arbitrario, controlados por microprocesador (p. 696–697).

#### 17.1C Materials and Device Structures (p. 697)

Semiconductores III–V binarios monocristalinos (no naturales) desde los años 50; muchas aleaciones de gap
directo (alta $\eta_i$) y larga vida (a diferencia de los II–VI). Industria actual basada en ternarios y
cuaternarios InGaAsP, AlInGaP y AlInGaN. **Fig. 17.1-16**: semáforo con LED III–V. **Fig. 17.1-17**:
(a) LED de emisión superficial (luz por la cara paralela a la región activa), (b) LED de emisión por el
borde (p. 697).

- **GaAs** (p. 697–698): primer diodo láser (1962), $\lambda_o=0.873$ μm cerca de $\lambda_g$; el LED de
  GaAs fue un subproducto. Otros binarios directos con electroluminiscencia y láser: GaSb
  ($\lambda_g=1.70$ μm), InP (0.919 μm), InAs (3.44 μm), InSb (7.29 μm); crecidos por VPE y LPE.
- **GaAsP** (p. 698): GaAs$_{1-x}$P$_x$; el gap pasa al visible (rojo) al añadir P; aunque se vuelve
  indirecto, con dopado de nitrógeno (GaAsP:N, GaP:N; a veces Zn y O) se consigue naranja, amarillo y verde
  (impurezas isoelectrónicas localizadas que absorben el cambio de momento). $\eta_{ex}$ pequeñas
  (0.02–0.5 %) en parte por desajuste de red con GaAs. Baratos: controles remotos, indicadores.
- **InGaAsP** (p. 698): In$_{1-x}$Ga$_x$As$_{1-y}$P$_y$; gap sintonizable con la composición en
  $0.549$ μm (GaP) $\le\lambda_g\le3.44$ μm (InAs), acoplable en red a InP eligiendo $x$ e $y$ (región
  punteada de Fig. 16.1-7(a)); solo parte del rango es de gap directo. LED para enlaces cortos a
  $\lambda_o\approx1330$ nm (**Fig. 17.1-18**, p. 698: LED tipo Saul–Lee–Burrus de emisión superficial a
  1.3 μm, región activa acoplada en red a InP, montado *flip-chip*, luz sale por el sustrato con lente
  integrada). Los sistemas de larga distancia a 1550 nm usan LD (mejor acoplo a fibra monomodo, cap. 24).
  LED de In$_x$Ga$_{1-x}$As de bajo coste en productos de consumo.
- **AlGaAs** (p. 699): Al$_x$Ga$_{1-x}$As, gap directo rojo e IR cercano, acoplado en red a GaAs para
  todas las fracciones de Al; dobles heteroestructuras Al$_x$Ga$_{1-x}$As/Al$_y$Ga$_{1-y}$As (los MQW
  sufren distribución no uniforme de portadores); problema: oxidación y corrosión si hay mucho Al.
- **AlInGaP** (p. 699): (Al$_x$Ga$_{1-x}$)$_y$In$_{1-y}$P, gap directo en IR cercano y visible largo;
  acoplado a GaAs para (Al$_x$Ga$_{1-x}$)$_{0.5}$In$_{0.5}$P; el ternario In$_{0.5}$Ga$_{0.5}$P tiene
  $\lambda_g=650$ nm (punteros láser, DVD). Material de alto brillo rojo–naranja–ámbar–amarillo (semáforos,
  señalización). Mejoras: sustrato GaP transparente por *wafer bonding*, MQW, cavidad resonante (RC).
  **Fig. 17.1-19** (p. 699): LED RC MQW AlInGaP/InGaP a 650 nm para fibra de plástico (600–650 nm), con
  reflectores de Bragg AlAs/AlGaAs y lente.
- **GaN** (p. 699–700): binario directo con $\lambda_g=0.366$ μm (UV cercano); crecido por MBE, MOCVD o
  HVPE sobre zafiro (gran desajuste de red, pero tolera muchas dislocaciones); electroluminiscencia 1971,
  primer LED $p$–$n$ de GaN 1992. Progenitor de InGaN, AlGaN, AlInGaN.
- **InGaN** (p. 700): In$_x$Ga$_{1-x}$N directo, $366$ nm (GaN) $\le\lambda_g\le1.61$ μm (InN); difícil
  con mucho In (agregados de InN → ensanchamiento por aleación del LED verde). Material de alto brillo
  para $366\le\lambda_o\le580$ nm (UV cercano, violeta, azul, verde), complementario de AlInGaP. MQW
  GaN/InGaN con 3–5 pozos (límite por la longitud de difusión de huecos). **Fig. 17.1-20** (p. 700): LED
  MQW GaN/InGaN a 420 nm: barreras GaN de 5 nm y cuatro pozos In$_x$Ga$_{1-x}$N de 2.5 nm, sustrato
  GaN sobre zafiro (transparente a 420 nm). También puntos cuánticos autoensamblados.
- **AlGaN** (p. 700–701): Al$_x$Ga$_{1-x}$N directo, $200$ nm (AlN) $\le\lambda_g\le366$ nm (GaN): UV
  medio y cercano ($200\le\lambda_o\le390$ nm). Dificultad: cae la conductividad tipo $p$ al aumentar AlN
  (escasez de huecos). Se han operado LED de AlN a 210 nm. DH/QW/MQW Al$_x$Ga$_{1-x}$N/Al$_y$Ga$_{1-y}$N;
  plantillas AlGaN/AlN/zafiro como sustratos transparentes (GaN absorbe por debajo de 366 nm).
- **AlInGaN** (p. 701): (Al$_x$In$_y$Ga$_{1-x-y}$)N acoplable en red a GaN (análogo a AlInGaP/GaAs e
  InGaAsP/InP), rango 366 nm → ~250 nm (AlInN acoplado a GaN). Pozos AlInGaN/InGaN/AlInGaN; In mejora
  $\eta_i$; capa de contacto transparente.
- **LED de luz blanca** (p. 701): (1) LED azul o UV cercano de nitruro + fósforos (fotoluminiscencia,
  Sec. 13.5B; **Fig. 17.1-21**); (2) mezcla de LED de distintas composiciones (el verde tiene menor
  $\eta_i$, pero da buen rendimiento cromático). Ventajas sobre incandescente: mayor eficiencia *wall-plug*
  y eficacia luminosa, vida, coste, tamaño.
- **LED orgánicos** (p. 701–702): moléculas pequeñas (**OLED**) o polímeros conjugados (**PLED**,
  Sec. 16.1B); hojas plásticas pixeladas, flexibles, enrollables, autoluminosas (pantallas, retroiluminación
  LCD). OLED: dos películas orgánicas (~100 nm) forman una heterounión entre ánodo (ITO transparente) y
  cátodo (Ca); los portadores forman excitones ligados que emiten en la heterounión; dopantes
  fluorescentes (azul) y fosforescentes (verde, rojo) aprovechan excitones singlete y triplete
  (Sec. 13.5B) → **WOLED** con $\eta_i$ casi unidad. **Fig. 17.1-22** (p. 702): estructura OLED
  (transportadores TPD de huecos y Alq₃ de electrones). PLED: región activa tipo $n$ (PPV) con huecos
  inyectados por una capa orgánica $p$; más fáciles y eficientes pero menos colores. Dendrímeros
  fosforescentes (núcleo Ir(2-fenilpiridina)₃) combinan ambas ventajas.

---

### 17.2 Semiconductor Optical Amplifiers (p. 702)

Principio igual al de otros amplificadores láser: inversión de población por inyección de corriente en una
unión $p$–$n$ en directa. La teoría es más compleja porque las transiciones son entre bandas, pero el SOA
puede verse como un sistema de **cuatro niveles** (Fig. 14.2-6) con los dos superiores en la banda de
conducción y los dos inferiores en la de valencia (p. 702–703).

#### 17.2A Gain and Bandwidth (p. 703)

**Fig. 17.2-1** (p. 703): (a) absorción de un fotón → par e–h; (b) recombinación estimulada por un fotón →
fotón idéntico. Las tasas $r_{st}(\nu)$ y $r_{ab}(\nu)$ [(16.2-18), (16.2-19)] dependen de la densidad
espectral de flujo de fotones $\phi_\nu$, de $\tau_r$, de $\varrho(\nu)$ y de las probabilidades de
ocupación $f_e(\nu)$ y $f_a(\nu)$. Con la aproximación parabólica,

$$E_2=E_c+\frac{m_r}{m_c}(h\nu-E_g),\qquad E_1=E_2-h\nu,\tag{17.2-1}$$

$$\varrho(\nu)=\frac{(2m_r)^{3/2}}{\pi\hbar^2}\sqrt{h\nu-E_g},\quad h\nu\ge E_g\tag{17.2-2}$$

(crece como la raíz cuadrada del exceso de energía sobre el gap). **Factor de inversión de Fermi**
[(16.2-25)]:

$$f_g(\nu)=f_e(\nu)-f_a(\nu)=f_c(E_2)-f_v(E_1),\tag{17.2-3}$$

función de $T$, $E_{fc}$ y $E_{fv}$ (es decir, del bombeo). Inversión completa $f_g=1$ posible en
principio → se comporta como sistema de cuatro niveles. **Coeficiente de ganancia neto**
$\gamma_0(\nu)=[r_{st}(\nu)-r_{ab}(\nu)]/\phi_\nu$ [(16.2-24)] (recuadro, p. 704):

$$\boxed{\gamma_0(\nu)=\frac{\lambda^2}{8\pi\tau_r}\varrho(\nu)f_g(\nu).}\tag{17.2-4}\ \text{(Gain Coefficient)}$$

Comparando con (14.1-4), $\varrho(\nu)f_g(\nu)$ juega el papel de $Ng(\nu)$ y
$\sigma(\nu)\approx\gamma_0(\nu)/\Delta\mathsf{n}$ (p. 704).

**Ancho de banda del amplificador** (p. 704–705). Hay ganancia neta cuando $f_c(E_2)>f_v(E_1)$,
equivalente a $h\nu<E_{fc}-E_{fv}$ (Ejercicio 16.2-1); en equilibrio térmico ($E_{fc}=E_{fv}=E_f$) nunca
hay ganancia. Con $h\nu>E_g$ para transiciones banda–banda (recuadro, p. 705):

$$\boxed{\frac{E_g}{h}<\nu<\frac{E_{fc}-E_{fv}}{h}.}\tag{17.2-5}\ \text{(Amplifier Bandwidth)}$$

Para $h\nu<E_g$ el medio es transparente; para $h\nu>E_{fc}-E_{fv}$ atenúa. El ancho de banda **crece con
el bombeo** (a diferencia del amplificador atómico, Fig. 14.1-2). A $T=0$ K:

$$f_g(\nu)=\begin{cases}+1,& h\nu<E_{fc}-E_{fv}\\-1,&\text{en otro caso}\end{cases}\tag{17.2-6}$$

**Fig. 17.2-2** (p. 705): $\varrho(\nu)$, $f_g(\nu)$ y $\gamma_0(\nu)$ a $T=0$ K (sólido) y a
temperatura ambiente (discontinuo); el factor $\nu^{-2}$ de $\lambda^2$ varía tan poco que se ignora.

**Dependencia de la ganancia con el bombeo** (p. 705–706). $\mathsf{R}$ constante → $\Delta\mathsf{n}=\Delta\mathsf{p}=\mathsf{R}\tau$;
con $\mathsf{n}$ y $\mathsf{p}$ se hallan $E_{fc},E_{fv}$ por (17.1-8) y luego $\gamma_0(\nu)$ por (17.2-4).

- **Ejemplo 17.2-1, Gain Coefficient for an InGaAsP SOA** (p. 706): In$_{0.72}$Ga$_{0.28}$As$_{0.6}$P$_{0.4}$,
  $E_g=0.95$ eV, $\lambda_o=1300$ nm, $T=300$ K, no dopado con $\approx2\times10^{17}$ cm⁻³ residuales,
  $\tau_r=2.5$ ns, $m_c\approx0.06m_0$, $m_v\approx0.4m_0$, $n\approx3.5$. **Fig. 17.2-3(a)**:
  $\gamma_0(\nu)$ vs $h\nu$ para $\Delta\mathsf{n}=1$ a $1.8\times10^{18}$ cm⁻³ (ancho de banda y pico
  crecen con $\Delta\mathsf{n}$; la energía mínima de amplificación baja ligeramente por estados de cola de
  banda). A $\Delta\mathsf{n}=1.8\times10^{18}$ cm⁻³ se amplifica entre 0.91 y 0.97 eV: ancho total
  14.5 THz (80 nm); FWHM (ancho a 3 dB) 10 THz ≈ 50 nm a 1300 nm (comparar Tabla 14.3-1).
  **Fig. 17.2-3(b)**: $\gamma_p$ vs $\Delta\mathsf{n}$; a $1.8\times10^{18}$, $\gamma_p=270$ cm⁻¹
  (grande frente a amplificadores atómicos). [Datos de N. K. Dutta, *J. Appl. Phys.* 51, 6095 (1980) y
  Dutta & Nelson, *J. Appl. Phys.* 53, 74 (1982).]

Saturación (p. 707): como en otros amplificadores homogéneos (Sec. 14.4); la gran sección eficaz
(Tabla 14.3-1) implica pequeña densidad de flujo de saturación $\phi_s\approx1/\tau_r\sigma(\nu)$
[(14.4-2), (14.4-3)] → ganancia global limitada. Ruido de ASE (Sec. 14.5) más fluctuaciones térmicas y de
portadores.

**Coeficiente de ganancia pico aproximado** (p. 707). Modelo empírico lineal en $\Delta\mathsf{n}$
(recuadro):

$$\boxed{\gamma_p\approx\alpha\left(\frac{\Delta\mathsf{n}}{\Delta\mathsf{n}_T}-1\right),}\tag{17.2-7}\ \text{(Peak Gain Coefficient, Linear Approximation)}$$

con $\gamma_p=-\alpha$ en $\Delta\mathsf{n}=0$ ($\alpha$ = coeficiente de absorción sin inyección) y
$\gamma_p=0$ en $\Delta\mathsf{n}=\Delta\mathsf{n}_T$ (**concentración de transparencia**, emisión y
absorción se equilibran). **Fig. 17.2-4** (p. 707).

- **Ejemplo 17.2-2, Approximate Peak Gain Coefficient for an InGaAsP SOA** (p. 707): ajuste de la
  Fig. 17.2-3(b) con $\Delta\mathsf{n}_T\approx1.25\times10^{18}$ cm⁻³ y $\alpha=600$ cm⁻¹; para
  $\Delta\mathsf{n}=1.4\Delta\mathsf{n}_T=1.75\times10^{18}$ cm⁻³, $\gamma_p=240$ cm⁻¹; para $d=350$ μm,
  $\exp(\gamma_pd)\approx4447$ (36.5 dB), reducido en la práctica por saturación y pérdidas de acoplo
  (3–5 dB por faceta).

Al pasar $\Delta\mathsf{n}$ de abajo a arriba de $\Delta\mathsf{n}_T$ el semiconductor pasa de absorbedor
fuerte ($f_g<0$) a amplificador de alta ganancia ($f_g>0$); la misma gran probabilidad de transición
lo hace buen absorbedor y buen amplificador [(16.2-18), (16.2-19)] (p. 708).

#### 17.2B Pumping (p. 708)

- **Bombeo óptico** (**Fig. 17.2-5**, p. 708): fotones de bombeo con $h\nu>E_g$ generan pares; si la
  relajación intrabanda es mucho más rápida que la interbanda se establece inversión estacionaria
  (Sec. 14.2).
- **Bombeo por corriente** (p. 708–709): inyección en una unión $p$–$n$ fuertemente dopada; los
  cuasi-niveles quedan dentro de las bandas (Fig. 17.1-5) y hay ganancia en $E_g\le h\nu\le E_{fc}-E_{fv}$.
  El espesor $l$ de la región activa lo fijan las longitudes de difusión de los minoritarios; típicamente
  $l=1$–3 μm en InGaAsP. Con corriente $i$ por área $A=wd$ ($w$ anchura, $d$ altura) en volumen $lA$
  (**Fig. 17.2-6**, p. 709: portadores perpendiculares a la unión, fotones en el plano de la unión),
  $\mathsf{R}=i/elA=J/el$ con $J=i/A$:

$$\Delta\mathsf{n}=\tau\mathsf{R}=\frac{\tau}{elA}i=\frac{\tau}{el}J.\tag{17.2-8}$$

Dentro del modelo lineal (recuadros, p. 709):

$$\boxed{\gamma_p\approx\alpha\left(\frac{J}{J_T}-1\right).}\tag{17.2-9}\ \text{(Peak Gain Coefficient)}$$

$$\boxed{J_T=\frac{el}{\eta_i\tau_r}\Delta\mathsf{n}_T,}\tag{17.2-10}\ \text{(Transparency Current Density)}$$

con $\eta_i=\tau/\tau_r$. **Fig. 17.2-7** (p. 710): $\gamma_p$ vs $J$, $-\alpha$ en $J=0$, cero en
$J_T$. **$J_T\propto l$**: una región activa más delgada reduce la corriente de transparencia —clave del
diseño de SOA y LD (p. 709).

- **Ejemplo 17.2-3, Gain of an InGaAsP SOA** (p. 709): $T=300$ K, $\tau_r=2.5$ ns, $\eta_i=0.5$,
  $\Delta\mathsf{n}_T=1.25\times10^{18}$ cm⁻³, $\alpha=600$ cm⁻¹, $l=2$ μm, $d=200$ μm, $w=10$ μm →
  $J_T=3.2\times10^4$ A/cm²; con $J=3.5\times10^4$ A/cm², $\gamma_p\approx56$ cm⁻¹ y
  $G=\exp(\gamma_pd)=\exp(1.12)\approx3$; pero $A=2\times10^{-5}$ cm² exige $i=JA=700$ mA.

**Motivación de las heteroestructuras** (p. 710): con $l=0.1$ μm, $J_T$ bajaría ×20 a 1600 A/cm², pero
los portadores difundirían fuera (longitudes de difusión de varios μm) → se confinan con una
heteroestructura, que además confina la luz.

#### 17.2C Heterostructures (p. 710)

Doble heteroestructura: barreras de potencial en ambos lados de la unión limitan la difusión de minoritarios
→ $l$ hasta ~0.1 μm (pozos cuánticos permiten ~0.01 μm, Sec. 17.2D). Si la capa activa tiene índice
ligeramente mayor que las vecinas, la estructura es una guía de ondas (Sec. 8.2). Tres capas acopladas en
red (**Fig. 17.2-8**, p. 711): capa 1 tipo $p$ ($E_{g1},n_1$), capa 2 tipo $p$ ($E_{g2},n_2$), capa 3 tipo
$n$ ($E_{g3},n_3$), con $E_{g1},E_{g3}>E_{g2}$ (confinamiento de portadores) y $n_2>n_1,n_3$
(confinamiento de luz); capa 2 muy delgada (0.1–0.2 μm) para minimizar $J_T$; la emisión estimulada
ocurre en la unión $p$–$n$ entre capas 2 y 3 (p. 710).

Ventajas (p. 711): (1) más ganancia para una $J$ dada por el menor $l$ [(17.2-9), (17.2-10)]; (2) más
ganancia por confinamiento de fotones (guía de ondas); (3) menos pérdidas porque las capas 1 y 3 no absorben
($h\nu=E_{g2}<E_{g1},E_{g3}$).

Ejemplos (p. 711): **InGaAsP/InP** (activa In$_{1-x}$Ga$_x$As$_{1-y}$P$_y$ acoplada a InP; banda
1.1–1.7 μm); **GaAs/AlGaAs** (activa GaAs, $E_{g2}=1.42$ eV, $n_2=3.6$; Al$_x$Ga$_{1-x}$As con
$E_g>1.43$ eV y $n$ 5–10 % menor; 0.82–0.88 μm para $x=0.35$–0.5).

#### 17.2D Quantum-Well Structures (p. 711)

Si la capa activa tiene 5–10 nm (menor que la longitud de onda de de Broglie de un electrón termalizado)
→ **pozo cuántico** (Sec. 16.1G). La banda de conducción se divide en subbandas $q=1,2,\dots$ con fondos en
$E_c+E_q$, $E_q=\hbar^2(q\pi/l)^2/2m_c$ (Figs. 16.1-24, 16.1-26; $q_1$ y $d_1$ del cap. 16 corresponden a
$q$ y $l$ aquí); cada subbanda tiene relación $E$–$k$ parabólica y **densidad de estados constante**
(escalera, (16.1-37)). Valencia: subbandas en $E_v-E'_q$, $E'_q=\hbar^2(q\pi/l)^2/2m_v$. Las transiciones
conservan energía, momento y el número cuántico $q$ (**Fig. 17.2-9**, p. 712: (a) relaciones $E$–$k$ de las
subbandas; (b) $\varrho(\nu)$ escalonada frente a la raíz cuadrada del material masivo; el primer escalón
en $E_{g1}=E_g+E_1+E'_1$). Las expresiones de la Sec. 16.2 se aplican reemplazando $E_g$ por
$E_{gq}=E_g+E_q+E'_q$ y usando densidad de estados constante; la ganancia total es la suma sobre
subbandas (p. 712).

**Densidad de estados** (p. 712–713): un fotón $h\nu$ interactúa con $E=E_c+E_q+(m_r/m_c)(h\nu-E_{gq})$
en la subbanda superior y $E-h\nu$ en la inferior; $\varrho(\nu)=(dE/d\nu)\varrho_c(E)=(hm_r/m_c)\varrho_c(E)$,
y de (16.1-37):

$$\varrho(\nu)=\begin{cases}\dfrac{hm_r}{m_c}\dfrac{m_c}{\pi\hbar^2l}=\dfrac{2m_r}{\hbar l},& h\nu>E_g+E_q+E'_q\\[2mm]0,&\text{en otro caso}\end{cases}\tag{17.2-11}$$

**Coeficiente de ganancia** (p. 713):

$$\gamma_0(\nu)=\frac{\lambda^2}{8\pi\tau_r}\varrho(\nu)f_g(\nu),\tag{17.2-12}$$

con el mismo $f_g(\nu)$ que en masivo pero distinta $\varrho(\nu)$. **Fig. 17.2-10** (p. 713):
$\varrho$, $f_g$ y $\gamma_0$ para QW (sólido) y masivo (discontinuo): el QW tiene **menor ganancia pico y
perfil más estrecho**. Si solo hay un escalón por debajo de $E_{fc}-E_{fv}$ (condición usual), la ganancia
máxima ($f_g=1$, $\varrho=2m_r/\hbar l$) es

$$\gamma_m=\frac{\lambda^2m_r}{2\tau_r\hbar l}.\tag{17.2-13}$$

**Relación ganancia–corriente** (p. 714): al subir $J$ crece $E_{fc}-E_{fv}$; cuando apenas supera $E_{g1}$
la ganancia crece bruscamente y satura en $\gamma_m$; cuando supera $E_{g2}$ (subbandas $q=2$) hay otro
salto, etc. → perfil de ganancia potencialmente muy ancho (amplio rango de sintonía).

**Materiales y estructuras** (p. 714): el SOA es como un LD operado sobre transparencia pero bajo umbral
(Sec. 17.3). IR cercano: InGaAsP, InGaAs, InP; en 1300–1600 nm, $\Delta\lambda\approx50$ nm
($\Delta\nu\approx10$ THz a 1300 nm), más ancho que EDFA y similar a RFA (Secs. 14.3C, 14.3D). SOA de
pozo cuántico: menor corriente de transparencia. SOA de puntos cuánticos: hasta 200 nm
($\Delta\nu\approx25$ THz a 1550 nm). Ganancia limitada a ≈15 dB (saturación, 3–5 dB de inserción por
faceta); saturación → interferencia intercanal e intersímbolo (inadecuados para DWDM, Sec. 24.3C); tiempo
de recombinación corto (Tabla 14.3-1) → ruido de alta frecuencia, figuras de ruido ≈8–10 dB frente a 3 dB
del EDFA. Como amplificador de onda viajera (un solo paso) las reflectancias de las facetas deben ser
mínimas (capas AR, guías inclinadas); si no, ganancia modulada por los modos del resonador u oscilación.
Usos: redes metropolitanas, **elementos ópticos no lineales y conmutadores ópticos (Sec. 23.3C),
conversión de longitud de onda**.

- **Ejemplo 17.2-4, Waveguide Amplifiers** (p. 715): SOA MQW en forma de guía de ondas (modo fundamental,
  mayor potencia de saturación, acoplo directo a fibra monomodo); un amplificador InGaAsP/InP QW de 1 cm a
  1550 nm da 13 dB de ganancia fibra a fibra (Juodawlkis et al., *IEEE Photon. Technol. Lett.* 17, 279,
  2005).

**Comparación SOA vs OFA** (p. 715). Ventajas: longitud de onda central elegible por material, compatible
con circuitos optoelectrónicos integrados, bombeo eléctrico, tamaño pequeño, bajo coste. Desventajas: baja
ganancia, baja potencia de salida saturada, alto ruido, interferencia intercanal/intersímbolo, sensibilidad
térmica, a reflexiones de facetas y a la polarización, control de modos transversales, alta pérdida de
inserción, incompatibilidad geométrica con la fibra. En conjunto, inferior a EDFA y RFA (Sec. 24.1C).

#### 17.2E Superluminescent Diodes (p. 715)

**SLD**: diodos con inyección tan fuerte que la emisión estimulada supera a la espontánea, sin señal de
entrada: emiten ASE (Sec. 14.5). **Fig. 17.2-11** (p. 716): SLD MQW InGaAsP/InP con contacto en franja
que inyecta corriente solo en parte del dispositivo (para evitar realimentación y oscilación; también
franjas afiladas, capas AR o facetas inclinadas). Potencia mayor que LED y menor que LD (Fig. 17.3-5);
espectro más estrecho que LED y más ancho que LD (Fig. 17.3-7). Usos donde la larga coherencia del láser
molesta: tomografía de coherencia óptica (Sec. 11.2B), giroscopios de fibra, sensores de fibra; también
los OFA se usan como fuentes superluminiscentes (p. 716).

---

### 17.3 Laser Diodes (p. 716)

#### 17.3A Amplification, Feedback, and Oscillation (p. 716)

Diodo láser = SOA + realimentación óptica, generalmente por las caras clivadas del cristal (salto de
índice semiconductor–aire → reflectores; el cristal es a la vez medio de ganancia y resonador
Fabry–Perot, **Fig. 17.3-1**, p. 717: unión $p$–$n$ con dos superficies clivadas paralelas; el libro
rotula la anchura $w$, el espesor de la región activa $l$, la longitud $d$ y el área de inyección $A$). También llamado *diode laser* o *semiconductor injection laser*. Diferencia con el
LED: luz por emisión estimulada (LED: espontánea). Ventajas: alta potencia, alta eficiencia, tamaño,
compatibilidad electrónica, bombeo y modulación por corriente; desventaja: mayor ancho de banda y menor
coherencia que otros láseres (p. 716).

**Amplificación láser** (p. 717). De (17.2-9), (17.2-10):

$$\gamma_p\approx\alpha\left(\frac{J}{J_T}-1\right),\qquad J_T=\frac{el}{\eta_i\tau_r}\Delta\mathsf{n}_T,\tag{17.3-1}$$

con $\tau_r$ vida radiativa, $\eta_i=\tau/\tau_r$, $l$ espesor de la región activa, $\alpha$ coeficiente de
absorción en equilibrio térmico, $\Delta\mathsf{n}_T$, $J_T$ transparencia.

**Realimentación** (p. 717). Resonador plano de longitud $d$ y sección $lw$; reflectancia de potencia
semiconductor–aire

$$\mathcal{R}=\left(\frac{n-1}{n+1}\right)^2\tag{17.3-2}$$

[(6.2-15), Tabla 16.2-1]; GaAs $n=3.6$ → $\mathcal{R}=0.32$ (suficiente, no hacen falta espejos externos).

**Pérdidas del resonador** (p. 718). Pérdida por reflexión (la luz útil) [(10.1-22)]:

$$\alpha_m=\alpha_{m1}+\alpha_{m2}=\frac{1}{2d}\ln\!\left(\frac{1}{\mathcal{R}_1\mathcal{R}_2}\right);\tag{17.3-3}$$

si $\mathcal{R}_1=\mathcal{R}_2=\mathcal{R}$, $\alpha_m=(1/d)\ln(1/\mathcal{R})$. Pérdida total

$$\alpha_r=\alpha_s+\alpha_m,\tag{17.3-4}$$

con $\alpha_s$ otras pérdidas (absorción por portadores libres, Fig. 16.2-2; dispersión por
inhomogeneidades; crece con impurezas e imperfecciones interfaciales; 10–100 cm⁻¹). El término $-\alpha$
de (17.3-1) ya incluye la absorción del material. La luz que se extiende fuera de la capa activa (sobre
todo si $l$ es pequeño) se propaga en medio con pérdidas; se define el **factor de confinamiento
$\Gamma$** = fracción de energía óptica dentro de la región activa (**Fig. 17.3-2**, p. 719:
(a) homoestructura, (b) heteroestructura con salto de índice que confina el modo); suponiendo que la
energía exterior se pierde,

$$\alpha_r=\frac{1}{\Gamma}(\alpha_s+\alpha_m).\tag{17.3-5}$$

Tres estructuras según el confinamiento lateral (en el plano de la unión): **broad-area** (sin
confinamiento), **gain-guided** (variaciones laterales de ganancia) e **index-guided** (variaciones
laterales de índice) (p. 718).

**Condición de ganancia: umbral láser** (p. 718–719). Oscilación si $\gamma_p>\alpha_r$ [(15.1-12)];
umbral $\gamma_p=\alpha_r$, $J=J_t$ en (17.3-1) (recuadros):

$$\boxed{J_t=\frac{\alpha_r+\alpha}{\alpha}J_T,}\tag{17.3-6}\ \text{(Threshold Current Density)}$$

$$\boxed{J_T=\frac{el}{\eta_i\tau_r}\Delta\mathsf{n}_T,}\tag{17.3-7}\ \text{(Transparency Current Density)}$$

$J_t/J_T=(\alpha_r+\alpha)/\alpha\approx1$ si $\alpha\gg\alpha_r$. Con $i=JA$, $A=wd$: $i_T=J_TA$,
$i_t=J_tA$. Menor $J_t$ = mejor láser: maximizar $\eta_i$; minimizar $\alpha_r$, $\Delta\mathsf{n}_T$ y $l$;
pero al reducir $l$ demasiado cae $\Gamma$ y sube $\alpha_r$ → $J_t$ tiene un mínimo (**Fig. 17.3-3**,
p. 720: $J_t$ vs $l$ para homoestructura y doble heteroestructura; la DH mantiene $\Gamma\approx1$ a
menor $l$ y alcanza un mínimo más bajo). $\Delta\mathsf{n}_T$ y $\alpha$ dependen de $T$ → $J_t$ y la
frecuencia del pico también; el control térmico estabiliza la salida y modifica la frecuencia (p. 719–720).

- **Ejemplo 17.3-1, Threshold Current for an InGaAsP Homostructure Laser Diode** (p. 720): parámetros de
  Ejemplos 17.2-1/17.2-2 ($\Delta\mathsf{n}_T=1.25\times10^{18}$ cm⁻³, $\alpha=600$ cm⁻¹, $\tau_r=2.5$ ns,
  $n=3.5$, $\eta_i=0.5$, 300 K), $d=200$ μm, $w=10$ μm, $l=2$ μm. $J_T=3.2\times10^4$ A/cm²;
  $\mathcal{R}=0.31$, $\alpha_m=(1/d)\ln(1/\mathcal{R})=59$ cm⁻¹; con $\alpha_s=59$ cm⁻¹ y $\Gamma\approx1$,
  $\alpha_r=118$ cm⁻¹; $J_t=[(118+600)/600](3.2\times10^4)=3.8\times10^4$ A/cm²; $i_t=J_twd\approx760$ mA.
  Las homoestructuras casi no se usan (difícil CW sin refrigeración).
- **Ejemplo 17.3-2, Threshold Current for an InGaAsP Heterostructure Laser Diode** (p. 720): igual pero
  $l=0.1$ μm y $\Gamma=1$ → $J_T=1600$ A/cm², $J_t=1915$ A/cm², $i_t=38$ mA. Esta reducción hizo posible
  la operación CW a temperatura ambiente.

#### 17.3B Power and Efficiency (p. 720)

**Flujo interno de fotones** (p. 720–721). Para $J>J_t$ la ganancia supera las pérdidas, el flujo crece y
la saturación (Fig. 15.2-1) lleva la ganancia a igualar las pérdidas. Como en (15.2-2), (15.2-13),
$\Phi\propto\mathsf{R}-\mathsf{R}_t$ y, con $\mathsf{R}\propto i$ (17.2-8) (recuadro, p. 721):

$$\boxed{\Phi=\begin{cases}\eta_i\dfrac{i-i_t}{e},& i>i_t\\[1mm]0,& i\le i_t\end{cases}}\tag{17.3-8}\ \text{(Steady-State Internal Photon Flux)}$$

$$\boxed{P=\eta_i(i-i_t)\frac{1.24}{\lambda_o},}\tag{17.3-9}\ \text{(Internal Laser Power; }\lambda_o\text{ μm, }P\text{ W, }i\text{ A)}$$

**Flujo de salida y eficiencia** (p. 721–722). Eficiencia de extracción $\eta_e$ [(15.2-16)] = (pérdida
asociada a la luz transmitida útil)/(pérdida total $\alpha_r$): un espejo $\eta_e=\alpha_{m1}/\alpha_r$; ambos
$\eta_e=\alpha_m/\alpha_r=[(1/d)\ln(1/\mathcal{R})]/\alpha_r$ (recuadros):

$$\boxed{\Phi_o=\eta_e\eta_i\frac{i-i_t}{e}.}\tag{17.3-10}\ \text{(Laser Output Photon Flux)}$$

$$\boxed{\eta_d=\eta_e\eta_i.}\tag{17.3-11}\ \text{(External Differential Quantum Efficiency)}$$

$$\eta_d=\frac{d\Phi_o}{d(i/e)}.\tag{17.3-12}$$

$$\boxed{P_o=\eta_d(i-i_t)\frac{1.24}{\lambda_o},}\tag{17.3-13}\ \text{(Laser Output Power; }\lambda_o\text{ μm, }P_o\text{ W, }i\text{ A)}$$

= **curva luz–corriente** (*light-current curve*); su pendiente sobre el umbral es la **responsividad
diferencial** (W/A):

$$\mathfrak{R}_d=\frac{dP_o}{di}=\eta_d\frac{1.24}{\lambda_o}.\tag{17.3-14}$$

**Fig. 17.3-4** (p. 722): curvas L–I medidas (sólido) e ideales (discontinuo) de (a) LD MQW
InGaAsP/InGaAsP *gain-guided* a 1550 nm (estructura en Fig. 17.4-8) y (b) LD MQW GaN/InGaN a 405 nm;
saturación por no linealidades. **Tabla 17.3-1** (p. 722, ver sección de tablas): mismo $\eta_d=0.33$,
pero $\mathfrak{R}_d$ ×4 mayor en GaN por la menor longitud de onda.

**Eficiencia de conversión de potencia** (*wall-plug*) (recuadro, p. 723):

$$\boxed{\eta_c=\eta_d\left(1-\frac{i_t}{i}\right)\frac{h\nu}{eV}.}\tag{17.3-15}\ \text{(Power Conversion Efficiency)}$$

Para $i\gg i_t$ y $eV\approx h\nu$, $\eta_c\approx\eta_d$. Los LD superan el 50 % (muy por encima de otros
láseres, Tabla 15.3-1); el resto es calor → disipadores (p. 723).

- **Ejemplo 17.3-3, Comparison of Efficiencies for MQW and DH InGaAsP Laser Diodes** (p. 723): DH
  InGaAsP/InP del Ejemplo 17.3-2 con $\eta_i=0.5$, $\alpha_m=59$ cm⁻¹, $\alpha_r=118$ cm⁻¹, $i_t=38$ mA:
  usando ambas caras $\eta_e=\alpha_m/\alpha_r=0.5$, $\eta_d=\eta_e\eta_i=0.25$; a 1300 nm
  $\mathfrak{R}_d=0.24$ W/A; con $i=50$ mA, $i-i_t=12$ mA y $P_o=12\times0.24=2.9$ mW. El MQW de la
  Fig. 17.3-4(a)/Tabla 17.3-1 tiene menor umbral y mayor $\eta_d$, como se espera.

**Resumen (recuadro, p. 723)** — cuatro eficiencias del diodo láser:
- eficiencia cuántica interna $\eta_i=\mathsf{r}_r/\mathsf{r}=\tau/\tau_r$ (fracción radiativa de las
  recombinaciones);
- eficiencia de extracción $\eta_e$ (fracción útil de la luz perdida por la cavidad);
- eficiencia cuántica diferencial externa $\eta_d=\eta_e\eta_i$;
- eficiencia de conversión de potencia (*wall-plug*) $\eta_c$ = potencia óptica emitida / potencia
  eléctrica suministrada.
La responsividad diferencial $\mathfrak{R}_d$ (W/A) también es útil.

**Comparación LED, SLD y LD** (p. 723–724). Bajo umbral el LD emite espontáneamente como un LED. LED:
$\eta_i$, $\eta_e$ (transmitancia), $\eta_{ex}=\eta_i\eta_e$, $\eta_c$, $\mathfrak{R}$; LD: $\eta_i$,
$\eta_e$, $\eta_d$, $\mathfrak{R}_d$, con $i\to(i-i_t)$. $\eta_e$ del LD > del LED porque la emisión
estimulada concentra la luz en modos particulares más extraíbles → $\eta_d$(LD) > $\eta_{ex}$(LED). SLD:
intermedio. **Fig. 17.3-5** (p. 724): curvas L–I de LED, SLD y LD MQW InGaAsP/InP a 1600 nm; el LD tiene
responsividad y eficiencia mucho mayores; la curva del SLD se curva hacia arriba y la del LED hacia abajo
(saturación).

#### 17.3C Spectral and Spatial Characteristics (p. 724)

**Características espectrales** (p. 724–725). Tres factores (Sec. 15.2B): (1) ancho de banda $B$ donde
$\gamma_0(\nu)>\alpha_r$; (2) ensanchamiento homogéneo o inhomogéneo (Sec. 13.3D); (3) modos del
resonador, espaciado $\nu_F=c/2d$. Particularidades del LD: (1) ganancia muy ancha (bandas, no niveles
discretos); (2) ensanchamiento homogéneo (procesos intrabanda rápidos) pero el **spatial hole burning**
permite oscilar muchos modos longitudinales a la vez (Sec. 15.2B), especialmente en cavidades cortas;
(3) $d$ pequeño → $\nu_F$ grande, aun así caben muchos modos en $B$: $M=B/\nu_F$ [(15.2-21)].

- **Ejemplo 17.3-4, Number of Longitudinal Modes in an InGaAsP Laser Diode** (p. 725): $n=3.5$,
  $d=400$ μm → $\nu_F=c/2d\approx107$ GHz; en $\lambda_o=1300$ nm, $\lambda_F=\lambda_o\nu_F/\nu=\lambda_o^2/2nd\approx0.6$ nm;
  con $B=1.2$ THz ($\Delta\lambda\approx7$ nm) oscilan ≈11 modos. **Fig. 17.3-6** (p. 725): espectro de
  un láser InGaAsP *index-guided* de heteroestructura enterrada a 1300 nm con un modo transversal y ~11
  longitudinales (Nelson et al., *IEEE JQE* 17, 202, 1981). Ancho de línea de cada modo: decenas de MHz
  (index-guided) a pocos GHz (gain-guided). Para un solo modo: $d<c/2B\approx36$ μm.

**Comparación de espectros** (**Fig. 17.3-7**, p. 726): LED, SLD y LD InGaAsP/InP a 1600 nm, normalizados;
el estrechamiento por emisión estimulada es evidente en SLD y más en LD.

**Características espaciales** (p. 726). Modos transversales $(l,m)$ y longitudinal $q$ (Sec. 15.2C). En
el LD el haz se extiende fuera de la capa activa: los modos transversales son los de la guía dieléctrica
formada por las capas (Sec. 8.3, sección rectangular $l\times w$). Si $l/\lambda_o$ es pequeño, un solo modo
en la dirección perpendicular a la unión; como $w\gg\lambda_o$, varios **modos laterales** (paralelos al
plano de la unión; **Fig. 17.3-8**: $(l,m)=(1,1),(1,2),(1,3)$); más modos cuanto mayor $w/\lambda_o$.

**Patrón de campo lejano** (p. 727). Divergencia angular $\approx\lambda_o/l$ (perpendicular a la unión) y
$\approx\lambda_o/w$ (paralela) (**Fig. 17.3-9**); análogo al haz gaussiano de diámetro $2W_0$ con
$\theta\approx(2/\pi)(\lambda_o/2W_0)=\lambda_o/\pi W_0$ [(3.1-21)]. Ej.: $l=2$ μm, $w=10$ μm,
$\lambda_o=800$ nm → ≈23° y 5°. Un LD monomodo (menor $w$) diverge aún más. El haz elíptico y asimétrico
dificulta la colimación.

**Operación monomodo** (p. 727–728). Los modos laterales de orden alto están menos confinados (mayor
$\alpha_r$) → algunos no oscilan o lo hacen a menor potencia. Para alta potencia en un solo modo espacial:
reducir $l$ y $w$ (guía monomodo; también baja $i_t$); eliminar modos laterales con estructuras
gain-guided o index-guided. Un solo modo longitudinal (frecuencia única): acortar $d$ hasta que $\nu_F$
supere el ancho de ganancia; resonadores de múltiples espejos (Sec. 15.2D, Fig. 15.2-15); **reflectores
distribuidos** en lugar de las facetas (facetas con AR): rejilla de Bragg en el plano de la unión
(**Fig. 17.3-10(a)**, p. 728): refleja si el periodo $\Lambda=q\lambda/2$ (Secs. 2.4B, 7.1C) → **láser DBR**
(*distributed Bragg reflector*); rejilla DBR bajo o sobre la región activa (**Fig. 17.3-10(b)**);
corrugación entre capa activa y de guía → índice periódico → **láser DFB** (*distributed feedback*,
**Fig. 17.3-10(c)**): anchos espectrales estrechos y gran ancho de banda de modulación; fuentes de
comunicaciones 1300–1600 nm (Sec. 17.4C).

---

### 17.4 Quantum-Confined and Microcavity Lasers (p. 728)

#### 17.4A Quantum-Confined Lasers (p. 728)

Confinamiento de portadores a dimensiones menores que la longitud de onda de de Broglie de un electrón
termalizado (≈50 nm en GaAs): 1, 2, 3 dimensiones → pozo, hilo, punto cuántico (**Fig. 17.4-1**, p. 729:
(a) QW, (b) hilo, (c) punto, con capas de confinamiento y reflectores de Bragg). Al bajar la
dimensionalidad las curvas de ganancia suben en altura y se estrechan → menor umbral, mayor $\eta_d$, menor
ancho de línea; pero menor volumen de interacción → menos potencia en hilos y puntos (p. 728).

**Láseres de pozo cuántico** (p. 728–729). Un SQW tiene $l<10$ nm (vs ≈100 nm DH, ≈2 μm homounión).
**Fig. 17.4-2** (p. 729): $\gamma_p$ vs $J$ para SQW y DH masivo: el SQW tiene $J_T$ mucho menor
($J_{T1}\ll J_{T2}$) pero la ganancia satura en múltiplos de $\gamma_m$ [(17.2-13)] (escalones $\gamma_m$,
$2\gamma_m$). Ventajas del QW frente al DH (lista, p. 729): menor $J_t$; mayor $\eta_d$; mayor $\eta_c$;
ganancia más estrecha; menor ancho de línea de los modos; respuesta más rápida (mayor frecuencia de
modulación); menor dependencia de la temperatura.

**Láseres MQW** (p. 729–730). **Fig. 17.4-3**. Con $N$ pozos la ganancia es $N$ veces la de cada pozo,
pero a igual bombeo cada pozo recibe $\Delta\mathsf{n}/N$; por la no linealidad ganancia–$\Delta\mathsf{n}$
cada pozo da $\xi\gamma_p/N$ ($\xi\gtrless1$ según el punto de operación) → total $\xi\gamma_p$. SQW mejor
a baja corriente; MQW mejor a alta corriente, por un factor menor que $N$.

**Láseres de capas tensionadas** (*strained-layer*, p. 730). Región activa con constante de red distinta
(suficientemente delgada para acomodarse sin dislocaciones; p. ej. InGaAs en AlGaAs/InGaAs: compresión
biaxial en el plano, expansión perpendicular). La tensión compresiva (1) aumenta $E_g$, (2) rompe la
degeneración en $k=0$ de huecos pesados y ligeros, (3) hace anisótropa la banda de valencia (masa ligera en
el plano, pesada perpendicular). Efectos: longitud de onda ajustable; menor $J_t$ porque la menor masa de
huecos permite que $E_{fv}$ descienda más fácilmente y se cumpla $E_{fc}-E_{fv}>E_g$ [(16.2-12)] a menor
inyección.

**Láseres de hilos cuánticos y multihilo** (p. 730–731). **Fig. 17.4-4**: región activa de hilos
múltiples; en principio anchos de línea más estrechos por mayor confinamiento, pero la fabricación III–V
va muy por detrás de los QW.

- **Ejemplo 17.4-1, Performance of Multiquantum-Wire and Quantum-Well Lasers** (p. 731): cinco hilos
  InGaAsP de 1 mm × 23 nm, revestidos de InP, separados 80 nm, láser CW a 300 K en 1550 nm:
  $i_t=140$ mA, $J_t=800$ A/cm², $\eta_d=40$ %, $\eta_c=2$ % (Yagi et al., *Jpn. J. Appl. Phys.* 43,
  3401, 2004); inferior al QW del mismo chip: $i_t=100$ mA, $J_t=500$ A/cm², $\eta_d=50$ %, $\eta_c=6$ %
  (volumen activo pequeño y grandes pérdidas ópticas).

**Láseres de puntos cuánticos** (p. 731–732). *Quantum dots / quantum boxes / nanocristales*: cubos,
esferas o pirámides de 1–10 nm (un cubo de GaAs de 10 nm tiene ~40 000 átomos); confinados por
semiconductor de mayor gap o embebidos en vidrio/polímero. Niveles = excitones, agudos; la energía crece al
reducir el tamaño (Fig. 13.1-12, Sec. 13.1C) → sintonía por tamaño. **Fig. 17.4-5** (p. 732): región
activa multipunto (capas con puntos autoensamblados de 10–50 nm); pueden emitir banda ancha o servir como
amplificadores.

- **Ejemplo 17.4-2, Quantum-Dot Silicon Photonics** (p. 732): el confinamiento reduce $\Delta x$ y por
  $\Delta x\Delta k\ge\frac12$ [(A.2-6)] aumenta $\Delta k$, lo que elimina la necesidad de fonón en la
  recombinación radiativa (análogo a GaP:N). Puntos de semiconductores de gap indirecto tienen $\eta_i$ muy
  superior al masivo; la pasivación superficial aumenta la tasa radiativa de excitones inducidos por
  superficie → emisión práctica en nanopartículas de Si, Si poroso, Ge; se intenta lograr láser en
  nanoestructuras de Si.

**Láseres de cascada cuántica (QCL)** (p. 732–734). Unipolares: un solo electrón genera múltiples fotones
por transiciones intersubbanda en cascada ("*band-structure engineering*"). Versión QW
(**Fig. 17.4-6(a)**, p. 733): etapas con inyector (superred tipo $n$: minibandas separadas por minigaps,
Sec. 13.1C) y región activa QW intrínseca; el electrón entra por túnel resonante desde el fondo de una
minibanda (nivel 3) al nivel láser superior 2; emite $\nu=E_{21}/h$ al pasar 2→1 (Sec. 16.2D), decae a 0
por fonones y entra por túnel en la siguiente etapa; 20–100 etapas. Como láser de 4 niveles: nivel 2
desalineado con la minibanda siguiente ($\tau_2\approx1$ ps), nivel 1 se vacía rápido a 0
($\tau_1\approx0.1$ ps) (Sec. 14.2B). Versión superred (**Fig. 17.4-6(b)**): transición entre dos
minibandas, frecuencia fijada por el minigap; mejor para $\lambda_o\ge10$ μm, admite más corriente.
Diseño *bound-to-continuum*: estado discreto superior → minibanda inferior (combina ambas ventajas).
Materiales: AlInAs/InGaAs en InP, AlGaAs/GaAs; también AlAsSb/InGaAs, AlGaN/GaN, SiGe; longitud
≈0.5–3 mm, anchura 5–20 μm. Rango 2–70 μm (espesores de pozo fijan subbandas, Ejercicio 16.1-5); cavidad
externa con rejilla rotatoria: sintonía gruesa ≈10 % del centro (≈1 μm en 10 μm); sintonía fina ≈0.1 μm
por corriente/temperatura (índice efectivo → camino óptico); monomodo con DFB. QCL IR medio: temperatura
ambiente, mW a cientos de mW CW, modulación rápida, *modelocking* a pulsos de ps, fuentes THz (decenas de
mW CW refrigerados), hasta 150 μm ($\nu=2$ THz). Variantes: sin inyector, guiado por plasmones
superficiales, multilongitud de onda, **supercontinuo** (etapas con pozos de distinto espesor), láser Raman
bombeado por un QCL integrado. Aplicaciones con detectores HgCdTe y microbolómetros VO$_x$ (Sec. 18.5):
análisis de trazas, sensado químico, isótopos, espectroscopia IR (transiciones vibracionales-rotacionales,
Sec. 13.1B), comunicaciones inalámbricas IR seguras para el ojo. Nota al pie (p. 734): los láseres de
sales de plomo llegan a ≈30 μm pero están limitados a mW, poca sintonía y requieren refrigeración.

#### 17.4B Microcavity Lasers (p. 734)

Confinamiento de **fotones** a dimensiones del orden de $\lambda_o\approx1$ μm $\gg\lambda$ (de Broglie);
*microrresonador*: una o más dimensiones de pocas $\lambda$ o menos; *microcavidad*: pequeña en todas las
dimensiones (términos intercambiables). El confinamiento de fotones y de portadores son independientes
(microcavidad con homounión; o QCL con resonador grande), pero la mayoría de láseres de microcavidad usan
regiones activas cuánticamente confinadas (p. 734). **Fig. 17.4-7** (p. 735): micropilar (DBR arriba y
abajo), microdisco, cristal fotónico 2D (defecto = cavidad), microtoroide, microesfera (Secs. 10.4B,
10.4C); análogos de QW, hilo y punto.

Resonador grande ($d\gg\lambda$): densidad de modos $M(\nu)=8\pi\nu^2/c^3$ [(10.3-10)]; la emisión
espontánea en modos distintos del láser es energía desperdiciada; en un LD de borde la fracción $\beta$ de
emisión espontánea acoplada a un modo es $\beta\approx10^{-5}$; la corriente de umbral se gasta
principalmente en reponer esa emisión espontánea. En microcavidades, grandes espaciados en una o más
direcciones de $k$ → modos ausentes en bandas extensas; con confinamiento en todas las direcciones,
conjunto discreto (Fig. 10.4-1). Colocar un emisor allí **inhibe** la emisión espontánea en modos
inexistentes y la redirige a los disponibles; en modos de alto $Q$ y pequeño volumen se **realza**
(efecto Purcell, Sec. 13.3E). Aumentar $\beta$ varios órdenes reduce $i_t$ en la misma proporción (de mA a
μA). También con colorantes orgánicos, sílice dopada con tierras raras y polímeros (p. 735).

**Resumen (recuadro, p. 735)** — los láseres de microcavidad ofrecen: tamaño reducido; umbral reducido;
ancho espectral reducido; ancho espacial reducido; mayor eficiencia. Su tamaño implica operar a baja
potencia.

- **Ejemplo 17.4-3, Single Photons on Demand from a Quantum Dot** (p. 736): un punto cuántico de InAs en
  un micropilar emite fotones individuales dirigidos preferentemente por la cara superior (acoplo a
  fibra); factor Purcell (13.3-47) grande (volumen modal pequeño, $Q$ alto, Tabla 10.4-1); emisión
  antiagrupada (*antibunched*) y *photon-number squeezed*, varianza de cuentas sub-Poissoniana
  (Sec. 12.3B); también por electroluminiscencia en unión $p$–$i$–$n$; aplicación en criptografía cuántica.

#### 17.4C Materials and Device Structures (p. 736)

Láseres semiconductores desde UV medio a IR lejano, de nW a kW (bancos); casi todos con regiones activas
cuánticamente confinadas.

**Diodos láser convencionales (emisión por el borde)** (p. 736): DVD, impresoras, comunicaciones; **bombeo
de amplificadores de fibra, láseres de fibra y de estado sólido**. Materiales como los LED: AlInGaN,
AlInGaP, InGaAs, InGaAsP; longitud típica $l\approx500$ μm, anchura $w\approx2$ μm [el libro usa aquí $l$
para la longitud y $w$ para la anchura]. Longitudes de onda comunes: 635–650 nm (punteros, DVD, fibra de
plástico); 785 nm (CD); 850 nm (enlaces cortos); 1300–1600 nm (larga distancia); también 375, 405, 440,
670, 830 nm. Sales de plomo hasta ≈30 μm con dificultades; QCL muy superiores en IR medio/lejano.
Multimodo de alta potencia (bombeo de OFA, fibras multinúcleo, DPSS, Sec. 15.3A): >5 W en franja de 50 μm,
kW en apilamientos de barras; acoplados a fibra. Bombeo: **808 nm** (Nd:YVO₄, Nd:YAG), **940 nm**
(Yb:YAG), **980 nm** (sílice dopada con Er). $\eta_c\approx45$ % típico, >75 % logrado.

- **Láseres de guía en cresta (*ridge-waveguide*, RW)** (p. 737): un solo modo espacial; guiado débil en
  franja y confinamiento lateral por inyección restringida bajo la cresta; Fabry–Perot con facetas clivadas;
  cientos de mW. **Fig. 17.4-8**: RW MQW InGaAsP/InGaAsP a 1550 nm, 500 μm, seis pozos InGaAsP de 7 nm
  (compresión) entre barreras InGaAsP de 10 nm (tensión); $i_t=15$ mA, $\eta_d=0.33$,
  $\mathfrak{R}_d=0.26$ W/A, ≈20 mW (curva L–I en Fig. 17.3-4(a)). Usos: espectroscopia, metrología.
- **Láseres DFB de heteroestructura enterrada** (p. 737–738): capas $p$ y $n$ alternadas restringen la
  corriente a la región activa (confinamiento lateral); película dieléctrica → guiado por ganancia; rejilla
  DFB adyacente a la región activa (**Fig. 17.4-9**, 1300–1600 nm). Compatible con integración; >1 W
  monomodo; $i_t<10$ mA, $\mathfrak{R}_d\approx0.4$ W/A; anchos espectrales estrechos (críticos para WDM).

**Láseres de emisión superficial de cavidad vertical (VCSEL)** (p. 738–740). El microrresonador más
común: luz por la cara superior de un microrresonador planar 1D; visible e IR cercano; diámetros hasta
≈1 μm. **Fig. 17.4-10** (p. 738): VCSEL de gran área (320 μm) MQW GaAs/InGaAs a 995 nm; región activa
entre DBR AlGaAs/GaAs altamente reflectantes; película dieléctrica + capas de confinamiento AlAs localizan
la inyección y confinan lateralmente el modo (Miller et al., *IEEE JSTQE* 7, 210, 2001). Como la región
activa tiene decenas de nm, la ganancia por paso es baja (fracción del 1 %) → DBR con docenas de capas y
alta ganancia; cuidado térmico. VCSEL pequeños: umbrales en μA, $\eta_c$ hasta ≈70 %. **Fig. 17.4-11**
(p. 739): espectro (centrado en ~995 nm, anchura ~2 nm), curva L–I (umbral $i_t=1.1$ A, ~1 W a 3 A) y
campo lejano (±~10°) del VCSEL de gran área. **Fig. 17.4-12**: VCSEL con región activa de puntos
cuánticos (MQD InGaAs/GaAs). **Fig. 17.4-13**: (a) VCSEL con cristal fotónico en el DBR para control
lateral de modos; (b) VCSEL con modulador de electroabsorción integrado (hacia 40 Gbit/s). Alta densidad
de empaquetamiento: ejemplo temprano de ≈1 millón de VCSEL cilíndricos InGaAs QW (diámetro ≈2 μm,
altura ≈5.5 μm, ~970 nm) en 1 cm² de GaAs, $i_t\approx100$ μA CW a 300 K (**Fig. 17.4-14**, p. 740:
micrografías SEM, In$_{0.2}$Ga$_{0.8}$As QW, 1–5 μm de diámetro, DBR AlAs/GaAs, cortesía de J. L. Jewell,
Picolight). Los arreglos pueden tener distribución prefijada de frecuencias.

**Láseres de microcavidad de cristal fotónico** (p. 740–741). Defectos en cristales fotónicos 2D +
emisores cuánticos → láseres sin umbral de tamaño $\lambda$, sintonizables, de alta velocidad de
modulación. **Fig. 17.4-15(a)**: láser de cristal fotónico monomodo a temperatura ambiente, bombeo
eléctrico por un poste de InP submicrométrico (1 μm de alto), $i_t=260$ μA, seis pozos InGaAsP
compensados en tensión, $\lambda_o=1520$ nm, 2 nW a 0.5 mA, $\mathfrak{R}\approx10^{-5}$,
$Q\approx2500$, $V\approx6\times10^{-2}$ μm³ (Park et al., *Science* 305, 1444, 2004). Efecto Purcell
cuando $\Delta\nu$ de emisión < $\delta\nu$ del modo (Sec. 13.3E, Fig. 13.3-12): factor
$(3/4\pi^2)(\lambda^3/V)Q\approx400$. **Fig. 17.4-15(b)**: arreglo acoplado coherentemente →
**microcavity-array laser** (*nanocavity-array laser*): 9×9 = 81 cavidades de 1.5 μm² (≈15 μm² en
total), cuatro pozos InGaAsP/InP, $\lambda_o=1534$ nm, bombeo óptico pulsado a 808 nm, umbral ≈2.5 mW,
$\beta\approx0.1$, 12 μW pico monomodo; el umbral sube con el número de cavidades pero la eficiencia sube
más (Altug & Vučković, *Opt. Express* 13, 8819, 2005).

---

### Reading List (p. 741–745)

Listas: libros sobre amplificadores y láseres (ver caps. 14 y 15); física de semiconductores y
nanoestructuras (ver cap. 16); **libros sobre LED y diodos láser** (p. 741–742; p. ej. Schubert,
*Light-Emitting Diodes*, 2.ª ed. 2006; **R. R. Alfano, ed., *The Supercontinuum Laser Source*, 2.ª ed.
2006**; Chuang; Coldren & Corzine, *Diode Lasers and Photonic Integrated Circuits*, 1995; Agrawal & Dutta,
*Semiconductor Lasers*, 1993; Yu, *Analysis and Design of VCSELs*, 2003; Ghafouri-Shiraz, *DFB Laser
Diodes and Optical Tunable Filters*, 2003; Ye, *Tunable External Cavity Diode Lasers*, 2004; Ustinov et
al., *Quantum Dot Lasers*, 2003; Nakamura et al., *The Blue Laser Diode*, 2000); **optoelectrónica**
(p. 742; Krier; Liu, *Photonic Devices*; Chuang, *Physics of Optoelectronic Devices*, 1995); **fotónica de
silicio** (p. 743; Jalali et al., *Raman-Based Silicon Photonics*, IEEE JSTQE 12, 412, 2006; Pavesi &
Lockwood, *Silicon Photonics*, 2004; Reed & Knights; Pavesi et al., *Nature* 408, 440, 2000);
**artículos** (p. 743–744; QCL: Faist 2006, Capasso et al. *Physics Today* 2002; Noda/Painter cristales
fotónicos; Chang-Hasnain VCSELs 1998; Jewell 1990; Michler et al. turnstile de fotón único 2000);
**históricos** (p. 744–745; Alferov y Kroemer, Nobel 2000; Faist et al. QCL *Science* 1994; Jewell VCSEL
1989; Hall, Nathan, Holonyak, Quist 1962; Basov 1961; Bernard & Duraffourg 1961; von Neumann 1953;
Round 1907).

---

## Tablas y datos numéricos útiles

**Tabla 17.3-1** (p. 722) — parámetros extraídos de las curvas L–I de la Fig. 17.3-4:

| Material | $\lambda_o$ (nm) | $i_t$ (mA) | $\eta_d$ | $\mathfrak{R}_d$ (W/A) |
|---|---|---|---|---|
| InGaAsP/InGaAsP (MQW, gain-guided) | 1550 | 15 | 0.33 | 0.26 |
| GaN/InGaN (MQW) | 405 | 35 | 0.33 | 1.0 |

**Constantes y fórmulas prácticas**
- $kT=0.0259$ eV a 300 K; $\Delta\nu\approx1.8kT/h\approx10$ THz (LED, 300 K, p. 695);
  $\Delta\lambda\approx1.45\lambda_p^2kT$ (μm, eV) → 36 nm a 1 μm (p. 695).
- $\mathfrak{R}=\eta_{ex}\cdot1.24/\lambda_o$ W/A ($\lambda_o$ en μm) (p. 694); $h\nu$(eV) $=1.24/\lambda_o$(μm).
- Fresnel normal: $\eta_2=4n/(n+1)^2$; $\mathcal{R}=[(n-1)/(n+1)]^2$; fracción en el cono crítico
  $\approx1/4n^2$ (p. 690, 717).

**Parámetros de materiales que aparecen**
- GaAs: $E_g=1.42$ eV, $n=3.6$ ($\eta_2=0.68$, $\mathcal{R}=0.32$, $\eta_3=1.9$ %), $\mathsf{n}_i\approx1.8\times10^6$ cm⁻³,
  $\mathsf{r}_r\approx10^{-10}$ cm³/s, $\eta_i\approx0.5$, $\tau=50$ ns (ej.), $m_c=0.07m_0$, $m_v=0.50m_0$
  (Prob. 17.2-3/17.2-5), $\lambda$ de Broglie térmica ≈50 nm, LD a 0.873 μm (p. 682–684, 697, 728, 746).
- Si: $\eta_i\approx10^{-5}$ (p. 683).
- InGaAsP (In$_{0.72}$Ga$_{0.28}$As$_{0.6}$P$_{0.4}$): $E_g=0.95$ eV, $\lambda_o=1300$ nm, $n=3.5$
  ($\mathcal{R}=0.31$), $\tau_r=2.5$ ns, $m_c=0.06m_0$, $m_v=0.4m_0$, residual $2\times10^{17}$ cm⁻³;
  ajuste lineal $\Delta\mathsf{n}_T=1.25\times10^{18}$ cm⁻³, $\alpha=600$ cm⁻¹; $\gamma_p=270$ cm⁻¹ a
  $\Delta\mathsf{n}=1.8\times10^{18}$ cm⁻³; ancho de ganancia 10 THz ≈ 50 nm (FWHM), 14.5 THz ≈ 80 nm
  total; $l$ típico 1–3 μm (p. 706–709).
- Gaps/longitudes de onda de gap: GaSb 1.70 μm, InP 0.919 μm, InAs 3.44 μm, InSb 7.29 μm, GaP 0.549 μm,
  GaN 0.366 μm, InN 1.61 μm, AlN 200 nm (210 nm emitido), In$_{0.5}$Ga$_{0.5}$P 650 nm (p. 698–700).
- Rangos: InGaAsP 0.549–3.44 μm (acoplado a InP); InGaN 366–580 nm (alto brillo); AlGaN 200–390 nm;
  AlInGaN 366–250 nm; AlGaAs/GaAs 0.82–0.88 μm ($x=0.35$–0.5); InGaAsP/InP 1.1–1.7 μm (p. 698–711).
- $\eta_{ex}$ GaAsP: 0.02–0.5 % (p. 698). LED InGaN/GaN 420 nm: 0.3 mW/mA, $\eta_{ex}=0.10$ (p. 694).
- Pérdidas: $\alpha_s$ 10–100 cm⁻¹ (p. 718). SOA: ganancia ≲15 dB, inserción 3–5 dB/faceta, NF 8–10 dB
  (EDFA 3 dB) (p. 714). QD-SOA ancho 200 nm (25 THz a 1550 nm) (p. 714).
- Tiempos LED: subida 1–50 ns → $B$ hasta cientos de MHz (p. 696).
- LD: $\nu_F=c/2nd$ [el libro escribe $\nu_F=c_o/2nd$ en el Ejemplo 17.3-4 y $c/2d$ con $c$ la velocidad
  en el medio en la Sec. 15.2]; 107 GHz y $\lambda_F=0.6$ nm para $d=400$ μm, $n=3.5$, 1300 nm; ancho
  de línea por modo: decenas de MHz (index-guided), GHz (gain-guided); $d\approx36$ μm para monomodo con
  $B=1.2$ THz (p. 725). Divergencia 23° × 5° para $l=2$ μm, $w=10$ μm, 800 nm (p. 727).
- Umbrales: homounión 760 mA, DH 38 mA (Ejemplos 17.3-1/2); RW 15 mA; DFB enterrado < 10 mA,
  $\mathfrak{R}_d\approx0.4$ W/A; VCSEL pequeño μA (100 μA en el arreglo de 1 cm²), VCSEL 320 μm 1.1 A;
  PC-laser 260 μA ($Q\approx2500$, $V\approx0.06$ μm³, Purcell ≈400, $\beta\approx0.1$ en arreglo);
  $\beta\approx10^{-5}$ en LD de borde (p. 720, 735–741).
- QCL: $\tau_2\approx1$ ps, $\tau_1\approx0.1$ ps; 20–100 etapas; 0.5–3 mm × 5–20 μm; 2–70 μm; sintonía
  ≈10 % (rejilla externa) y ≈0.1 μm (corriente/T) a 10 μm; hasta 150 μm (2 THz) (p. 733–734).
- Bombeo de estado sólido/fibra: 808 nm (Nd), 940 nm (Yb:YAG), 980 nm (Er); $\eta_c\approx45$ %,
  hasta >75 % (p. 736).
- Fórmula empírica de reducción de gap por colas de banda (Prob. 17.2-4, p. 746):
  $\Delta E_g(\text{eV})\approx(-1.6\times10^{-8})(\mathsf{p}^{1/3}+\mathsf{n}^{1/3})$, concentraciones en cm⁻³.

---

## Problemas al final del capítulo (p. 745–747)

La numeración continúa la de los ejercicios del texto (17.1-1 a 17.1-4 están en el texto). Los marcados
con * son avanzados.

- **17.1-5 LED Spectral Widths** (p. 745): estimar gráficamente las FWHM (nm, Hz, eV) de siete espectros
  de las Figs. 17.1-14 y P17.1-5 centrados en 0.37, 0.53, 0.64, 0.91, 1.30, 1.93 y 2.25 μm; comparar con
  las fórmulas del Ejercicio 17.1-3; estimar el ensanchamiento por aleación del LED de 0.53 μm.
  **Fig. P17.1-5**: espectros normalizados de LED InGaAsP en el IR cercano (0.8–2.4 μm), anchura
  creciente como $\lambda_p^2$.
- **17.1-6 External Efficiency of an LED** (p. 745): deducir $\eta_e$ para luz interna no polarizada
  incluyendo la dependencia angular de la reflexión de Fresnel semiconductor–aire (Sec. 6.2).
- **17.1-7 Coupling Light from an LED into an Optical Fiber** (p. 745): fracción de potencia de un LED
  plano ($n=3.6$, emisión $\propto\cos^4\theta$, área menor que el núcleo, pegado al núcleo) aceptada por
  una fibra de salto de índice con NA = 0.1 en aire y núcleo $n=1.46$ (Sec. 9.1).
- **17.2-1 Bandwidth of a Semiconductor Optical Amplifier** (p. 745): con la Fig. 17.2-3(a), graficar el
  ancho de banda total del SOA InGaAsP vs $\Delta\mathsf{n}$; fórmula lineal aproximada; graficar
  ganancia vs ancho de banda.
- **17.2-2 Peak Gain Coefficient of a SOA at $T=0$ K** (p. 745–746): (a) mostrar que el pico de
  $\gamma_0(\nu)$ a 0 K está en $\nu=(E_{fc}-E_{fv})/h$; (b) expresión analítica de $\gamma_p(\Delta\mathsf{n})$
  a 0 K; (c) graficar para InGaAsP ($\lambda_o=1300$ nm, $n=3.5$, $\tau_r=2.5$ ns, $m_c=0.06m_0$,
  $m_v=0.4m_0$) con $\Delta\mathsf{n}$ de 1 a $2\times10^{18}$ cm⁻³; (d) comparar con Fig. 17.2-3(b).
- ***17.2-3 Gain Coefficient of a GaAs SOA** (p. 746): GaAs tipo $p$ a 300 K ($E_g\approx1.40$ eV,
  $m_c=0.07m_0$, $m_v=0.50m_0$, $n=3.6$, $\mathsf{p}_0=1.2\times10^{18}$ cm⁻³, $\tau_r\approx2$ ns).
  (a) Calcular $\gamma_0(\nu)$ vs $h\nu$ con (17.2-2)–(17.2-4) a 0 K; (b) lo mismo por computador a 300 K;
  (c) graficar $\gamma_p(\Delta\mathsf{n})$ en ambos casos; (d) $\alpha$ y $\Delta\mathsf{n}_T$ del modelo
  lineal; (e) ancho de banda total (Hz, nm, eV) vs $\Delta\mathsf{n}$; (f) comparar con **Fig. P17.2-3**
  (ganancia y ganancia pico de un SOA de GaAs según Panish, *Proc. IEEE* 64, 1512, 1976; curvas para
  $\Delta\mathsf{n}=1.2$ a $2\times10^{18}$ cm⁻³, $h\nu$ 1.38–1.44 eV, $\gamma_0$ hasta ~300 cm⁻¹).
- **17.2-4 Bandgap Reduction Arising from Band-Tail States** (p. 746): con
  $\Delta E_g(\text{eV})\approx(-1.6\times10^{-8})(\mathsf{p}^{1/3}+\mathsf{n}^{1/3})$ (cm⁻³):
  (a) $\mathsf{p}$ que reduce el gap 0.02 eV en InGaAsP y GaAs tipo $p$; (b) $\Delta\mathsf{n}$ que lo
  reduce 0.02 eV en material no dopado ($\mathsf{n}_i$ despreciable); (c) comparar $E_g+\Delta E_g$ con la
  energía donde $\gamma_0$ se anula por el lado de baja frecuencia en Fig. P17.2-3(a).
- **17.2-5 Amplifier Gain and Bandwidth** (p. 746–747): GaAs con $\mathsf{n}_i=1.8\times10^6$ cm⁻³,
  $\tau=50$ ns, $E_g=1.42$ eV, $m_c=0.07m_0$, $m_v=0.50m_0$, $T=0$ K. (a) Frecuencia central, ancho de banda
  y ganancia neta pico de un amplificador de $d=200$ μm, $w=10$ μm, $l=2$ μm con 1 mA; (b) número de
  canales de voz de 4 kHz que caben en ese ancho de banda; (c) tasa de bits si cada canal usa 64 kbit/s.
- **17.2-6 Transition Cross Section** (p. 747): $\sigma(\nu)$ de GaAs en función de $\Delta\mathsf{n}$ a
  0 K (probabilidad de emisión/absorción estimulada $=\phi\sigma(\nu)$); por qué es menos útil para SOA
  que para otros amplificadores.
- ***17.2-7 Gain Profile** (p. 747): SOA InGaAsP a 1550 nm ($n=3.5$, Fig. 17.2-6) con capas AR
  idénticas en ambas facetas: reflectividad máxima de las facetas para que la variación del perfil de
  ganancia por la dependencia frecuencial de la transmitancia Fabry–Perot [(7.1-32)] sea < 10 %.
- **17.3-1 Dependence of Output Power on Refractive Index** (p. 747): identificar los términos de
  $\Phi_o$ (17.3-10) que dependen del índice del cristal.
- **17.3-2 Longitudinal Modes** (p. 747): InGaAsP con $E_g=0.91$ eV, $n=3.5$, $E_{fc}-E_{fv}=0.96$ eV,
  $d=250$ μm sin pérdidas: número máximo de modos longitudinales que pueden oscilar.
- **17.3-3 Minimum Gain Required for Lasing** (p. 747): cristal InGaAsP de 500 μm, $n=3.5$, sin otras
  pérdidas: ganancia que compensa justo las pérdidas de reflexión en las caras.
- ***17.3-4 Modal Spacings with a Wavelength-Dependent Refractive Index** (p. 747): LD de 430 μm a
  $\lambda_c=650$ nm con $n(\lambda_o)=n_0-a(\lambda_o-\lambda_c)$, $n_0=3.4$, $a=dn/d\lambda_o$.
  (a) Explicar por qué el espaciado observado $\Delta\lambda\approx0.12$ nm no coincide con
  $\nu_F=c/2d$; (b) estimar $a$; (c) explicar el *mode pulling* en un láser de gas y compararlo.

---

## Relación con Óptica No Lineal

**Con los temas del curso**
- *Ondas EM, absorción y dispersión*: el coeficiente de ganancia $\gamma_0(\nu)$ (17.2-4) es un
  coeficiente de absorción negativo; el signo de $f_g(\nu)$ decide absorción/ganancia (p. 704–705). El
  modelo lineal $\gamma_p\approx\alpha(\Delta\mathsf{n}/\Delta\mathsf{n}_T-1)$ (17.2-7) es la forma en que
  se parametriza un medio activo saturable, útil como contraste con los coeficientes de absorción no lineal
  (absorción de dos fotones, saturación) que se tratan con χ⁽³⁾. El Prob. 17.3-4 (índice dependiente de
  $\lambda$, *mode pulling*) conecta directamente con la dispersión $n(\lambda)$ y con la distinción entre
  $c/2d$ y el espaciado real de modos $\lambda^2/2n_gd$ (hay que usar el índice de grupo).
- *Haz gaussiano*: el campo lejano del diodo láser se compara con la divergencia gaussiana
  $\theta=\lambda_o/\pi W_0$ (3.1-21) (p. 727); el haz elíptico de un LD de borde exige óptica anamórfica
  para enfocarlo en una guía o fibra.
- *Pulsos en medios dispersivos / GVD*: no se tratan aquí, pero el ancho espectral del LD (varios modos
  en $B\approx1$ THz) y del SLD/LED (10 THz) determina la coherencia temporal y la dispersión cromática en
  fibra (Sec. 24, p. 698 menciona por qué los LD sustituyen a los LED a 1550 nm).
- *χ⁽³⁾, índice dependiente de la intensidad, FWM*: el SOA se cita explícitamente como **elemento óptico
  no lineal, conmutador y conversor de longitud de onda** (p. 714, Sec. 23.3C); su saturación de ganancia
  (sección eficaz grande, $\phi_s$ pequeña, p. 707) y la dependencia del índice con $\Delta\mathsf{n}$ (que
  el libro usa para sintonizar QCL por corriente, p. 733) son los mecanismos de la no linealidad de los
  SOA (XGM/XPM/FWM). El efecto Purcell y la modificación de $M(\nu)$ en microcavidades (p. 735) son el
  marco para entender el realce de procesos no lineales en resonadores de alto $Q$ y pequeño volumen.
- *Raman*: el libro menciona láseres Raman bombeados por un QCL integrado (p. 734) y la fotónica de
  silicio basada en Raman (Reading List, Jalali et al., p. 743).
- *Supercontinuo*: aparece el QCL de supercontinuo (etapas con pozos de distinto espesor, p. 734) y la
  referencia Alfano, *The Supercontinuum Laser Source* (p. 741), que es bibliografía directa del proyecto.

**Con el proyecto final (anillos add-drop en Si₃N₄, dispersión, supercontinuo, sensado)**
- *Diodos láser como bombeo de microanillos*: lo que fija la potencia disponible es la curva L–I
  $P_o=\eta_d(i-i_t)\,1.24/\lambda_o$ (17.3-13) con $\mathfrak{R}_d=\eta_d\,1.24/\lambda_o$ (17.3-14);
  valores reales en Tabla 17.3-1 (0.26 W/A a 1550 nm, $i_t=15$ mA, ≈20 mW para RW; DFB enterrado >1 W
  monomodo, $\mathfrak{R}_d\approx0.4$ W/A, $i_t<10$ mA, p. 737–738). Para bombear un anillo de Si₃N₄
  (Q alto, FSR de decenas a cientos de GHz) el bombeo debe ser **monomodo longitudinal** y estrecho:
  Fabry–Perot clivado con $d=400$ μm da ≈11 modos separados 107 GHz (0.6 nm) (Ejemplo 17.3-4); los
  anchos de línea por modo son decenas de MHz (index-guided) a GHz (gain-guided) (p. 725), por lo que
  conviene un DFB/DBR (p. 727–728) o un láser de cavidad externa (Ye, *Tunable External Cavity Diode
  Lasers*, p. 741) para alinear el bombeo con una resonancia cuyo ancho es $\nu_0/Q$ (≈200 MHz para
  $Q=10^6$ a 193 THz).
- *Sintonía*: la frecuencia del pico de ganancia y $J_t$ dependen de $T$ (p. 719–720); el índice efectivo
  cambia con corriente y temperatura, lo que desplaza los modos (sintonía fina ≈0.1 μm a 10 μm en QCL,
  p. 733; mismo mecanismo en LD a 1550 nm). Esto da el modo de barrer el bombeo por la resonancia del
  anillo (necesario para el barrido térmico del *soliton step* en generación de peines/supercontinuo).
- *Ancho de banda de ganancia disponible*: InGaAsP cubre 1.1–1.7 μm (p. 711), con 50 nm FWHM de ganancia
  a 1300 nm (p. 706); QD-SOA hasta 200 nm (p. 714) — relevante si se piensa amplificar el bombeo o un
  peine ancho en chip.
- *Microcavidades y VCSEL*: la Sec. 17.4B describe microdiscos, microtoroides, microesferas y cristales
  fotónicos (Fig. 17.4-7) con la misma física de densidad de modos y factor $\beta$ que un microanillo; el
  factor Purcell $(3/4\pi^2)(\lambda^3/V)Q$ (p. 740) y el $Q\approx2500$, $V\approx0.06$ μm³ del láser de
  cristal fotónico son referencias para comparar con el $Q$ y el volumen modal del anillo de Si₃N₄. Los
  VCSEL (p. 738–740) ofrecen umbrales de μA, $\eta_c$ hasta 70 %, haz circular de baja divergencia
  (±10°, Fig. 17.4-11) y arreglos densos; su potencia (mW en dispositivos pequeños, ~1 W solo en 320 μm
  de diámetro multimodo) limita su uso como bombeo de no linealidades en Si₃N₄, pero son candidatos para
  integración con anillos de sensado (fuente + anillo + detector en el mismo chip).
- *Sensado de índice de refracción*: para interrogar un anillo refractométrico se necesita o un láser
  sintonizable estrecho (DFB/DBR con barrido térmico) o una fuente ancha (LED/SLD, 10 THz de ancho, Fig.
  17.3-7) con analizador de espectro; el SLD (p. 715–716) es la fuente de bajo coste y baja coherencia que
  el libro recomienda para interferometría y sensores de fibra.
- *Acoplo a guías*: las eficiencias de extracción y los patrones de emisión (Secs. 17.1B, 17.3C, Prob.
  17.1-7) y la nota sobre acoplo de LD a fibra monomodo (p. 698, Ejemplo 17.2-4 con acoplo directo a fibra
  monomodo) sirven para estimar la potencia que efectivamente entra en la guía de bus del anillo.
