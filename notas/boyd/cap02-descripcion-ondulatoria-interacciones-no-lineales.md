# Capítulo 2 — Wave-Equation Description of Nonlinear Optical Interactions (Boyd, 3.ª ed.)

Páginas del libro 69–133 (PDF 87–151; la p. 134 del libro está en blanco y el cap. 3 empieza en la
p. 135). Leído el 2026-11-14.

Fuente: R. W. Boyd, *Nonlinear Optics*, 3.ª ed., Academic Press (Elsevier), 2008, cap. 2. Las citas
de página son páginas del libro (sumar 18 para la página del PDF).

Convención del libro (SI): $\tilde E(t)=Ee^{-i\omega t}+\text{c.c.}$, $E_i=A_ie^{ik_iz}$ con $A_i$ amplitud lentamente
variable; $\tilde P(t)=\epsilon_0[\chi^{(1)}\tilde E+\chi^{(2)}\tilde E^2+\chi^{(3)}\tilde E^3+\dots]$; intensidad $I_i=2n_i\epsilon_0c|A_i|^2$ (2.2.16);
$d_{\rm eff}=\tfrac12\chi^{(2)}_{\rm eff}$. La tilde marca cantidades que varían rápido en el tiempo. Ojo: el signo de $\Delta k$
cambia según la sección (SFG: $\Delta k=k_1+k_2-k_3$; DFG/OPA/OPO: $\Delta k=k_3-k_1-k_2$; SHG: $\Delta k=2k_1-k_2$;
haces enfocados: $\Delta k=qk_1-k_q$).

---

## Resumen del capítulo

El capítulo pasa de la susceptibilidad no lineal (cap. 1) a la propagación: a partir de las ecuaciones de
Maxwell en un medio sin cargas ni corrientes libres, no magnético y con $\tilde{\mathbf D}=\epsilon_0\tilde{\mathbf E}+\tilde{\mathbf P}$, deduce la
ecuación de onda forzada en la que la polarización no lineal $\tilde{\mathbf P}^{\rm NL}$ actúa como fuente, primero en
forma general y luego componente a componente de frecuencia en medios dispersivos (2.1). Con la
aproximación de amplitud lentamente variable obtiene las **ecuaciones de amplitudes acopladas** de la
generación de suma de frecuencias (SFG) y, en el límite de bombas no agotadas, la ley
$I_3\propto d_{\rm eff}^2I_1I_2L^2\,\mathrm{sinc}^2(\Delta kL/2)$, con la longitud de coherencia $L_{\rm coh}=2/\Delta k$ (2.2). Muestra por qué con
dispersión normal no hay ajuste de fase en medios isótropos y cómo se logra con **birrefringencia** (tipos I
y II, tablas para uniaxiales positivos y negativos, sintonía por ángulo con $n_e(\theta)$ y por temperatura,
walkoff) (2.3), y con **cuasi‑ajuste de fase** (QPM) en materiales periódicamente polarizados, donde
$d_Q=(2/\pi)d_{\rm eff}$ y $\Lambda=2L_{\rm coh}$ en primer orden (2.4). Deriva las **relaciones de Manley–Rowe** (conservación de la
potencia y del flujo de fotones) (2.5). Resuelve exactamente la SFG con bomba fuerte (conversión
ascendente: intercambio periódico $\cos/\sin$ con $g=\sqrt{\kappa^2+\Delta k^2/4}$) (2.6) y la **SHG** con agotamiento según
Armstrong et al. (variables normalizadas $u_1,u_2,\theta$, conservación de $u_1^2+u_2^2$ y de $\Gamma=u_1^2u_2\cos\theta$, soluciones
$u_2=\tanh\zeta$, $u_1=\mathrm{sech}\,\zeta$), con un estimado de 2 % de eficiencia para un láser CW de 1 W y
aplicaciones (SHG de superficies, microscopía no lineal) (2.7). La **DFG** con bomba no agotada da
crecimiento exponencial de señal e idler (amplificación paramétrica) (2.8), base del **OPO**: ganancia $g$,
umbrales de DRO ($g^2L^2=l_1l_2$) y SRO ($g^2L^2=2l_1$), sintonía, influencia de la estructura de modos, estabilidad
y ancho de línea, e historia (2.9). Luego trata **haces gaussianos enfocados**: ecuación paraxial, haz
gaussiano, generación del armónico $q$ con la integral $J_q$, el efecto de la fase de Gouy (THG nula con
$\Delta k=0$ en enfoque fuerte) y el resultado de **Boyd–Kleinman** ($L/b=2.84$, $\Delta k=3.2/L$) (2.10). Termina con la
**óptica no lineal en una interfaz**: SH reflejado, ley de Snell no lineal y estimado de la SHG superficial de
medios centrosimétricos (~$10^{-3}$ en amplitud respecto al volumen no centrosimétrico) (2.11). Cierra con
22 problemas.

---

## Secciones

### 2.1 The Wave Equation for Nonlinear Optical Media (p. 69)

**Imagen física (p. 69–70, Fig. 2.1.1).** En SFG cada átomo desarrolla un dipolo oscilante con
componente en $\omega_1+\omega_2$; un átomo aislado radiaría con patrón dipolar (Fig. 2.1.1b), pero un
conjunto de $N$ dipolos con fases fijadas por los campos incidentes actúa como un *arreglo de
dipolos en fase* si se cumple la condición de ajuste de fase (Eq. 2.2.14): el campo emitido hacia
adelante es $N$ veces el de un átomo y la intensidad $N^2$ veces (Fig. 2.1.1c, haz bien definido).

**Ecuaciones de Maxwell (SI)**, p. 70 (la tilde denota cantidad que varía rápido en el tiempo):

$$\nabla\cdot\tilde{\mathbf D}=\tilde\rho \quad(2.1.1),\qquad \nabla\cdot\tilde{\mathbf B}=0\quad(2.1.2),$$
$$\nabla\times\tilde{\mathbf E}=-\frac{\partial\tilde{\mathbf B}}{\partial t}\quad(2.1.3),\qquad \nabla\times\tilde{\mathbf H}=\frac{\partial\tilde{\mathbf D}}{\partial t}+\tilde{\mathbf J}\quad(2.1.4).$$

Supuestos: sin cargas libres $\tilde\rho=0$ (2.1.5), sin corrientes libres $\tilde{\mathbf J}=0$ (2.1.6), material
no magnético $\tilde{\mathbf B}=\mu_0\tilde{\mathbf H}$ (2.1.7), pero no lineal en
$$\tilde{\mathbf D}=\epsilon_0\tilde{\mathbf E}+\tilde{\mathbf P}\quad(2.1.8),\ \text{p. 71},$$
con $\tilde{\mathbf P}$ dependiente no linealmente del campo local.

**Derivación (p. 71).** Rotacional de (2.1.3), intercambio de derivadas, (2.1.4), (2.1.6), (2.1.7) para
reemplazar $\nabla\times\tilde{\mathbf B}$ por $\mu_0\partial\tilde{\mathbf D}/\partial t$:
$$\nabla\times\nabla\times\tilde{\mathbf E}+\mu_0\frac{\partial^2\tilde{\mathbf D}}{\partial t^2}=0\quad(2.1.9a)$$
y eliminando $\tilde{\mathbf D}$ con (2.1.8), con $\mu_0=1/\epsilon_0c^2$:
$$\nabla\times\nabla\times\tilde{\mathbf E}+\frac{1}{c^2}\frac{\partial^2\tilde{\mathbf E}}{\partial t^2}=-\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde{\mathbf P}}{\partial t^2}\quad(2.1.9b)$$
— la forma **más general** de la ecuación de onda en ONL. Con la identidad
$\nabla\times\nabla\times\tilde{\mathbf E}=\nabla(\nabla\cdot\tilde{\mathbf E})-\nabla^2\tilde{\mathbf E}$ (2.1.10): en óptica lineal de medios isótropos sin
fuentes $\nabla\cdot\tilde{\mathbf E}=0$ (porque $\nabla\cdot\tilde{\mathbf D}=0$), pero en ONL el término en general **no** se anula
ni en medios isótropos, por la relación más general (2.1.8). Aun así se puede despreciar en casos
de interés: se anula idénticamente para una onda plana transversal infinita y suele ser pequeño
cuando vale la aproximación de amplitud lentamente variable (§2.2). En adelante (p. 72):
$$\nabla^2\tilde{\mathbf E}-\frac{1}{c^2}\frac{\partial^2\tilde{\mathbf E}}{\partial t^2}=\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde{\mathbf P}}{\partial t^2}\quad(2.1.11),\qquad \nabla^2\tilde{\mathbf E}-\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde{\mathbf D}}{\partial t^2}=0\quad(2.1.12).$$

**Separación lineal/no lineal (p. 72):** $\tilde{\mathbf P}=\tilde{\mathbf P}^{(1)}+\tilde{\mathbf P}^{\rm NL}$ (2.1.13);
$\tilde{\mathbf D}=\tilde{\mathbf D}^{(1)}+\tilde{\mathbf P}^{\rm NL}$ (2.1.14a), $\tilde{\mathbf D}^{(1)}=\epsilon_0\tilde{\mathbf E}+\tilde{\mathbf P}^{(1)}$ (2.1.14b), y
$$\nabla^2\tilde{\mathbf E}-\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde{\mathbf D}^{(1)}}{\partial t^2}=\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde{\mathbf P}^{\rm NL}}{\partial t^2}\quad(2.1.15).$$

*Medio sin pérdidas ni dispersión:* $\tilde{\mathbf D}^{(1)}=\epsilon_0\boldsymbol\epsilon^{(1)}\cdot\tilde{\mathbf E}$ (2.1.16a) con tensor dieléctrico real
independiente de la frecuencia; isótropo: $\tilde{\mathbf D}^{(1)}=\epsilon_0\epsilon^{(1)}\tilde{\mathbf E}$ (2.1.16b), $\epsilon^{(1)}$ escalar
adimensional (permitividad relativa) y $\epsilon_0=8.85\times10^{-12}$ F/m. Entonces (p. 73)
$$-\nabla^2\tilde{\mathbf E}+\frac{\epsilon^{(1)}}{c^2}\frac{\partial^2\tilde{\mathbf E}}{\partial t^2}=-\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde{\mathbf P}^{\rm NL}}{\partial t^2}\quad(2.1.17):$$
ecuación de onda **forzada**; la respuesta no lineal es el término fuente. Sin fuente: ondas libres
con velocidad $c/n$, $n^2=\epsilon^{(1)}$.

*Medio dispersivo (p. 73):* cada componente de frecuencia por separado,
$\tilde{\mathbf E}(\mathbf r,t)=\sum_n'\tilde{\mathbf E}_n(\mathbf r,t)$ (2.1.18a), ídem $\tilde{\mathbf D}^{(1)}$ (2.1.18b) y $\tilde{\mathbf P}^{\rm NL}$ (2.1.18c), suma solo
sobre frecuencias **positivas**, con
$$\tilde{\mathbf E}_n(\mathbf r,t)=\mathbf E_n(\mathbf r)e^{-i\omega_nt}+\text{c.c.}\quad(2.1.19a)$$
(idem (2.1.19b) para $\mathbf D^{(1)}_n$ y (2.1.19c) para $\mathbf P^{\rm NL}_n$). Sin disipación,
$\tilde{\mathbf D}^{(1)}_n=\epsilon_0\boldsymbol\epsilon^{(1)}(\omega_n)\cdot\tilde{\mathbf E}_n$ (2.1.20), y para cada componente
$$\nabla^2\tilde{\mathbf E}_n-\frac{\epsilon^{(1)}(\omega_n)}{c^2}\frac{\partial^2\tilde{\mathbf E}_n}{\partial t^2}=\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde{\mathbf P}_n^{\rm NL}}{\partial t^2}\quad(2.1.21).$$
*Medio disipativo (p. 74):* tensor complejo entre amplitudes complejas,
$\mathbf D^{(1)}_n(\mathbf r)=\epsilon_0\boldsymbol\epsilon^{(1)}(\omega_n)\cdot\mathbf E_n(\mathbf r)$ (2.1.22), y
$$\nabla^2\mathbf E_n(\mathbf r)+\frac{\omega_n^2}{c^2}\boldsymbol\epsilon^{(1)}(\omega_n)\cdot\mathbf E_n(\mathbf r)=-\frac{\omega_n^2}{\epsilon_0c^2}\mathbf P^{\rm NL}_n(\mathbf r)\quad(2.1.23).$$

### 2.2 The Coupled-Wave Equations for Sum-Frequency Generation (p. 74)

Supuestos: medio sin pérdidas, haces colimados, monocromáticos, CW, incidencia normal
(Fig. 2.2.1: cristal de longitud $L$, $d_{\rm eff}=\tfrac12\chi^{(2)}$, entradas $\omega_1,\omega_2$, salida
$\omega_3=\omega_1+\omega_2$), se ignora la doble refracción (generalización: Shen 1984, cap. 6). Aproximación
de campo escalar; $n_3$ es el índice correspondiente al estado de polarización de la onda $\omega_3$.

Sin fuente, la solución de (2.1.21) para onda plana en $+z$:
$$\tilde E_3(z,t)=A_3e^{i(k_3z-\omega_3t)}+\text{c.c.}\quad(2.2.1),\qquad k_3=\frac{n_3\omega_3}{c},\ n_3^2=\epsilon^{(1)}(\omega_3)\quad(2.2.2),$$
con $A_3$ constante; con fuente pequeña se toma como solución de prueba la misma forma con $A_3(z)$
lentamente variable. Fuente: $\tilde P_3(z,t)=P_3e^{-i\omega_3t}+\text{c.c.}$ (2.2.3), con, según (1.5.28),
$$P_3=4\epsilon_0d_{\rm eff}E_1E_2\quad(2.2.4);\qquad \tilde E_i(z,t)=E_ie^{-i\omega_it}+\text{c.c.},\ E_i=A_ie^{ik_iz}\quad(2.2.5),$$
$$P_3=4\epsilon_0d_{\rm eff}A_1A_2e^{i(k_1+k_2)z}\equiv p_3e^{i(k_1+k_2)z}\quad(2.2.6),\ \text{p. 75}.$$
Sustituyendo en (2.1.21) con $\nabla^2\to d^2/dz^2$:
$$\Big[\frac{d^2A_3}{dz^2}+2ik_3\frac{dA_3}{dz}-k_3^2A_3+\frac{\epsilon^{(1)}(\omega_3)\omega_3^2A_3}{c^2}\Big]e^{i(k_3z-\omega_3t)}+\text{c.c.}=\frac{-4d_{\rm eff}\omega_3^2}{c^2}A_1A_2e^{i[(k_1+k_2)z-\omega_3t]}+\text{c.c.}\quad(2.2.7)$$
El 3.º y 4.º términos se cancelan ($k_3^2=\epsilon^{(1)}(\omega_3)\omega_3^2/c^2$); se eliminan los c.c. y el factor $e^{-i\omega_3t}$:
$$\frac{d^2A_3}{dz^2}+2ik_3\frac{dA_3}{dz}=\frac{-4d_{\rm eff}\omega_3^2}{c^2}A_1A_2e^{i(k_1+k_2-k_3)z}\quad(2.2.8).$$
**Aproximación de amplitud lentamente variable (SVEA)**, p. 76, válida si
$$\Big|\frac{d^2A_3}{dz^2}\Big|\ll\Big|k_3\frac{dA_3}{dz}\Big|\quad(2.2.9)$$
(el cambio fraccional de $A_3$ en una distancia del orden de una longitud de onda es $\ll1$). Resulta
$$\frac{dA_3}{dz}=\frac{2id_{\rm eff}\omega_3^2}{k_3c^2}A_1A_2e^{i\Delta kz}\quad(2.2.10),\qquad \Delta k=k_1+k_2-k_3\quad(2.2.11)$$
(desajuste de vector de onda o de momento). Análogamente:
$$\frac{dA_1}{dz}=\frac{2id_{\rm eff}\omega_1^2}{k_1c^2}A_3A_2^*e^{-i\Delta kz}\quad(2.2.12a),\qquad \frac{dA_2}{dz}=\frac{2id_{\rm eff}\omega_2^2}{k_2c^2}A_3A_1^*e^{-i\Delta kz}\quad(2.2.12b).$$
Medio sin pérdidas ⇒ no hay términos de pérdida y, por la simetría de permutación completa (1.5.8),
el mismo $d_{\rm eff}$ en las tres ecuaciones. Forma general en términos de la amplitud lentamente variable
$p_3$ de la polarización:
$$\frac{dA_3}{dz}=\frac{i\omega_3}{2\epsilon_0n_3c}p_3e^{i\Delta kz}\quad(2.2.13),\ \text{con }P_3=p_3e^{i(k_1+k_2)z}.$$

#### 2.2.1 Phase-Matching Considerations (p. 77)

Con $A_1,A_2$ constantes (poca conversión): si $\Delta k=0$ (2.2.14) — **ajuste de fase perfecto** — $A_3$
crece linealmente con $z$ e $I_3\propto z^2$; los dipolos están en fase y la potencia radiada escala
como el cuadrado del número de átomos. Si $\Delta k\neq0$, integrando (2.2.10) de 0 a $L$:
$$A_3(L)=\frac{2id_{\rm eff}\omega_3^2A_1A_2}{k_3c^2}\int_0^Le^{i\Delta kz}dz=\frac{2id_{\rm eff}\omega_3^2A_1A_2}{k_3c^2}\Big(\frac{e^{i\Delta kL}-1}{i\Delta k}\Big)\quad(2.2.15).$$
Intensidad (Poynting promediado) para esta definición de amplitud:
$$I_i=2n_i\epsilon_0c|A_i|^2,\ i=1,2,3\quad(2.2.16),$$
$$I_3=\frac{8n_3\epsilon_0d_{\rm eff}^2\omega_3^4|A_1|^2|A_2|^2}{k_3^2c^3}\Big|\frac{e^{i\Delta kL}-1}{\Delta k}\Big|^2\quad(2.2.17).$$
Con (p. 78)
$$\Big|\frac{e^{i\Delta kL}-1}{\Delta k}\Big|^2=2L^2\frac{1-\cos\Delta kL}{(\Delta kL)^2}=L^2\frac{\sin^2(\Delta kL/2)}{(\Delta kL/2)^2}\equiv L^2\,\mathrm{sinc}^2(\Delta kL/2)\quad(2.2.18),$$
$$\boxed{I_3=\frac{8d_{\rm eff}^2\omega_3^2I_1I_2}{n_1n_2n_3\epsilon_0c^2}L^2\,\mathrm{sinc}^2\Big(\frac{\Delta kL}{2}\Big)}\quad(2.2.19).$$
Todo el efecto del desajuste está en el **factor de desajuste de fase** $\mathrm{sinc}^2(\Delta kL/2)$ (Fig. 2.2.2:
pico 1 en 0, lóbulos laterales pequeños, eje $\Delta kL/2$ de $-3\pi$ a $3\pi$). La eficiencia decae con
$|\Delta k|L$ oscilando: si $L\gtrsim1/\Delta k$ la onda generada se desfasa de su polarización motriz y la
potencia vuelve de $\omega_3$ a $\omega_1,\omega_2$. Longitud de acumulación coherente:
$$L_{\rm coh}=2/\Delta k\quad(2.2.20),\qquad \text{factor}=\mathrm{sinc}^2(L/L_{\rm coh})\quad(2.2.21),\ \text{p. 79}.$$
(Nota: otros textos definen la longitud de coherencia como $\pi/\Delta k$ o $2\pi/\Delta k$; verificar la definición al comparar con el Saleh u otras fuentes.)

### 2.3 Phase Matching (p. 79)

Para SFG con haces no agotados (2.3.1)–(2.3.2):
$$I_3=I_3^{(\max)}\Big[\frac{\sin(\Delta kL/2)}{\Delta kL/2}\Big]^2\quad(2.3.2).$$
Con agotamiento la dependencia ya no es (2.3.2), pero la generación eficiente sigue exigiendo
$\Delta k=0$. **Experimento de Maker et al. (1962)** (Fig. 2.3.1, p. 80): láser de rubí pulsado enfocado en
cuarzo; al rotar el cristal varía la longitud efectiva $L$ con $\Delta k\neq0$ aprox. constante ⇒ franjas de
Maker (señal SH vs. orientación $\theta$ de $-40^\circ$ a $40^\circ$, oscilaciones entre 0 y 1, mínimo ancho cerca de 0°).

**Imposibilidad con dispersión normal.** En un medio sin pérdidas entre $\omega_1$ y $\omega_3$
($\omega_1\le\omega_2<\omega_3$) el índice crece con la frecuencia, de modo que la condición colineal
$$\frac{n_1\omega_1}{c}+\frac{n_2\omega_2}{c}=\frac{n_3\omega_3}{c}\quad(2.3.3),\qquad \omega_1+\omega_2=\omega_3\quad(2.3.4)$$
no se cumple. Para SHG exige $n(\omega_1)=n(2\omega_1)$ (2.3.5), imposible si $n(\omega)$ es monótona. Para SFG:
$n_3=(n_1\omega_1+n_2\omega_2)/\omega_3$ (2.3.6) ⇒ $n_3-n_2=(n_1\omega_1-n_2\omega_1)/\omega_3$, i.e.
$$n_3-n_2=(n_1-n_2)\frac{\omega_1}{\omega_3}\quad(2.3.7),\ \text{p. 81};$$
con dispersión normal el lado izquierdo es $>0$ y el derecho $<0$: sin solución. Salidas: dispersión
anómala (cerca de absorción) o, lo más común, **birrefringencia**. Los cristales cúbicos son
ópticamente isótropos y no son ajustables en fase.

**Tabla 2.3.1** (p. 82): triclínico, monoclínico, ortorrómbico → biaxial; trigonal, tetragonal,
hexagonal → uniaxial; cúbico → isótropo.

Regla: la onda de mayor frecuencia $\omega_3$ se polariza en la dirección de **menor** índice
(extraordinaria en un uniaxial negativo, Fig. 2.3.2: $n_o$ y $n_e<n_o$ crecen con $\omega$ y divergen al
acercarse a una resonancia). Midwinter y Warner (1965): **tipo I** = las dos ondas de menor frecuencia
con la misma polarización; **tipo II** = polarizaciones ortogonales.

**Tabla 2.3.2** (p. 82), métodos para uniaxiales:

| | Positivo ($n_e>n_o$) | Negativo ($n_e<n_o$) |
|---|---|---|
| Tipo I | $n_3^o\omega_3=n_1^e\omega_1+n_2^e\omega_2$ | $n_3^e\omega_3=n_1^o\omega_1+n_2^o\omega_2$ |
| Tipo II | $n_3^o\omega_3=n_1^o\omega_1+n_2^e\omega_2$ | $n_3^e\omega_3=n_1^e\omega_1+n_2^o\omega_2$ |

La clasificación no presupone $\omega_1\lessgtr\omega_2$, pero en tipo II es más fácil (menos birrefringencia)
si $\omega_2>\omega_1$ con la asignación de la tabla; e independientemente, el tipo I es más fácil que el II.
Dos métodos: sintonía por ángulo y por temperatura.

**Angle tuning (p. 81–84).** Uniaxial: eje óptico ($c$ o $z$). Polarización **ordinaria**: perpendicular al
plano que contiene $\mathbf k$ y el eje óptico, índice $n_o$. **Extraordinaria**: en ese plano, índice
$$\frac{1}{n_e(\theta)^2}=\frac{\sin^2\theta}{\bar n_e^2}+\frac{\cos^2\theta}{n_o^2}\quad(2.3.8),\ \text{p. 83},$$
$\bar n_e$ = valor principal; $n_e(90^\circ)=\bar n_e$, $n_e(0)=n_o$ (derivación: Born & Wolf §14.3, Klein, Zernike y Midwinter).
Ejemplo: SHG tipo I en uniaxial negativo (Fig. 2.3.3: fundamental ordinaria, SH extraordinaria,
$\mathbf k$ a ángulo $\theta$ de $\hat c$):
$$n_e(2\omega,\theta)=n_o(\omega)\quad(2.3.9),\qquad \frac{\sin^2\theta}{\bar n_e(2\omega)^2}+\frac{\cos^2\theta}{n_o(2\omega)^2}=\frac{1}{n_o(\omega)^2}\quad(2.3.10),$$
$$\sin^2\theta=\frac{\dfrac{1}{n_o(\omega)^2}-\dfrac{1}{n_o(2\omega)^2}}{\dfrac{1}{\bar n_e(2\omega)^2}-\dfrac{1}{n_o(2\omega)^2}}\quad(2.3.11).$$
No siempre hay $\theta$ real: si la dispersión es muy grande o la birrefringencia muy pequeña, el lado
derecho supera 1 (p. 84).

**Temperature tuning (p. 84).** Inconveniente del ángulo: para $\theta\neq0,90^\circ$ el vector de Poynting
$\mathbf S$ y $\mathbf k$ no son paralelos en el rayo extraordinario ⇒ **walkoff**: rayos o y e con $\mathbf k$ paralelos se
separan, limitando el traslape y la eficiencia. En algunos cristales (notablemente niobato de litio)
la birrefringencia depende fuertemente de $T$: se fija $\theta=90^\circ$ (ajuste de fase no crítico) y se
varía $T$ (índices de LiNbO$_3$ vs. $T$: Hobden y Warner 1966).

### 2.4 Quasi-Phase-Matching (p. 84)

Cuándo no sirve la birrefringencia: material sin birrefringencia (GaAs), birrefringencia
insuficiente (problema que empeora a longitudes de onda cortas: el índice crece rápido con $\omega$ mientras
$n_o-n_e$ es casi constante), o cuando se quiere usar $d_{33}$ (mucho mayor que los no diagonales), que
exige todas las ondas con la misma polarización.

**Idea (p. 85, Fig. 2.4.1):** material periódicamente polarizado (*periodically poled*): la orientación
de un eje cristalino (a menudo el eje $c$ de un ferroeléctrico) se invierte periódicamente con período
$\Lambda$, invirtiendo el signo de $d_{\rm eff}$. **Fig. 2.4.2** (p. 86): amplitud del campo generado vs. $z/L_{\rm coh}$
(0–8): (a) ajuste perfecto, crecimiento lineal; (c) con desajuste, oscila periódicamente sin crecer; (b) QPM con $\Lambda=2L_{\rm coh}$: cada vez que la amplitud iba a decrecer se
invierte $d_{\rm eff}$ y crece monótonamente, aunque más despacio que en (a).

Formulación: onda cuadrada
$$d(z)=d_{\rm eff}\,\mathrm{sign}[\cos(2\pi z/\Lambda)]\quad(2.4.1),\qquad d(z)=d_{\rm eff}\sum_{m=-\infty}^{\infty}G_m\exp(ik_mz)\quad(2.4.2),$$
$k_m=2\pi m/\Lambda$ (vector de red del $m$-ésimo armónico), y para (2.4.1) (p. 87)
$$G_m=(2/m\pi)\sin(m\pi/2)\quad(2.4.3),\qquad G_1=2/\pi.$$
Suponiendo que una componente de Fourier domina y con SVEA:
$$\frac{dA_1}{dz}=\frac{2i\omega_1d_Q}{n_1c}A_3A_2^*e^{-i(\Delta k_Q-2k_m)z}\ (2.4.4a),\quad \frac{dA_2}{dz}=\frac{2i\omega_2d_Q}{n_2c}A_3A_1^*e^{-i(\Delta k_Q-2k_m)z}\ (2.4.4b),\quad \frac{dA_3}{dz}=\frac{2i\omega_3d_Q}{n_3c}A_1A_2e^{i\Delta k_Qz}\ (2.4.4c),$$
$$d_Q=d_{\rm eff}G_m\quad(2.4.5),\qquad \Delta k_Q=k_1+k_2-k_3+k_m\quad(2.4.6).$$
(Ver erratas: el exponente de (2.4.4a,b) se lee así en el libro.) Formalmente idénticas a (2.2.10),
(2.2.12) con $d_{\rm eff}\to d_Q$ y $\Delta k\to\Delta k_Q$ (nótese $2i\omega d/nc=2id\omega^2/kc^2$). Como $d_Q$ decrece con $m$,
conviene QPM de primer orden:
$$\Delta k_Q=k_1+k_2-k_3-2\pi/\Lambda,\qquad d_Q=(2/\pi)d_{\rm eff}\quad(2.4.7),$$
$$\Lambda=2L_{\rm coh}=2\pi/(k_1+k_2-k_3)\quad(2.4.8).$$
**Ejemplo numérico (p. 88):** $L_{\rm coh}=3.4\ \mu$m para SHG de $1.06\ \mu$m en niobato de litio.
Fabricación: Armstrong et al. (1962) propusieron rebanar el medio y rotar segmentos alternos 180°
(capas demasiado delgadas); crecimiento con alternancia del eje $c$; inversión local; **poling
eléctrico** (Yamada et al. 1993): electrodo metálico en franjas arriba, plano de tierra abajo,
campo estático del orden de **21 kV/mm** que invierte los dominios ferroeléctricos solo bajo los
electrodos (PPLN). Polímeros también se polarizan periódicamente (Khanarian et al. 1990). Revisión:
Byer (1997).

### 2.5 The Manley–Rowe Relations (p. 88)

Tres ondas $\omega_1,\omega_2,\omega_3=\omega_1+\omega_2$ en medio sin pérdidas (Fig. 2.5.1). Con (p. 89)
$$I_i=2n_i\epsilon_0cA_iA_i^*\quad(2.5.1),\qquad \frac{dI_i}{dz}=2n_i\epsilon_0c\Big(A_i^*\frac{dA_i}{dz}+A_i\frac{dA_i^*}{dz}\Big)\quad(2.5.2),$$
y (2.2.12a): $dI_1/dz=4\epsilon_0d_{\rm eff}\omega_1(iA_3A_1^*A_2^*e^{-i\Delta kz}+\text{c.c.})$, es decir
$$\frac{dI_1}{dz}=-8\epsilon_0d_{\rm eff}\omega_1\,\mathrm{Im}(A_3A_1^*A_2^*e^{-i\Delta kz})\quad(2.5.3a),$$
$$\frac{dI_2}{dz}=-8\epsilon_0d_{\rm eff}\omega_2\,\mathrm{Im}(A_3A_1^*A_2^*e^{-i\Delta kz})\quad(2.5.3b),$$
$$\frac{dI_3}{dz}=-8\epsilon_0d_{\rm eff}\omega_3\,\mathrm{Im}(A_3^*A_1A_2e^{i\Delta kz})=8\epsilon_0d_{\rm eff}\omega_3\,\mathrm{Im}(A_3A_1^*A_2^*e^{-i\Delta kz})\quad(2.5.3c).$$
$dI_1/dz$ y $dI_2/dz$ tienen el mismo signo, opuesto al de $dI_3/dz$; la dirección del flujo de energía
depende de las fases relativas. Conservación de potencia: $I=I_1+I_2+I_3$ (2.5.4) y (p. 90)
$$\frac{dI}{dz}=-8\epsilon_0d_{\rm eff}(\omega_1+\omega_2-\omega_3)\,\mathrm{Im}(A_3A_1^*A_2^*e^{-i\Delta kz})=0\quad(2.5.5).$$
**Relaciones de Manley–Rowe** (Manley y Rowe 1959):
$$\frac{d}{dz}\Big(\frac{I_1}{\omega_1}\Big)=\frac{d}{dz}\Big(\frac{I_2}{\omega_2}\Big)=-\frac{d}{dz}\Big(\frac{I_3}{\omega_3}\Big)\quad(2.5.6),$$
$I_i/\omega_i\propto$ flujo de fotones (fotones por unidad de área y tiempo). Equivalentemente
$\frac{d}{dz}(I_2/\omega_2+I_3/\omega_3)=0$, $\frac{d}{dz}(I_1/\omega_1+I_3/\omega_3)=0$, $\frac{d}{dz}(I_1/\omega_1-I_2/\omega_2)=0$ (2.5.7), con
invariantes espaciales
$$M_1=\frac{I_2}{\omega_2}+\frac{I_3}{\omega_3},\qquad M_2=\frac{I_1}{\omega_1}+\frac{I_3}{\omega_3},\qquad M_3=\frac{I_1}{\omega_1}-\frac{I_2}{\omega_2}\quad(2.5.8).$$
La tasa de creación de fotones $\omega_1$ = la de $\omega_2$ = la de destrucción de fotones $\omega_3$ (Fig. 2.5.2, p. 91:
diagrama de niveles: un fotón $\omega_3$ sube, bajan $\omega_2$ y $\omega_1$). Aunque la derivación es clásica, es
consistente con la imagen cuántica porque supone simetría de permutación completa (mismo $d_{\rm eff}$
en las tres ecuaciones), que en cierto sentido es consecuencia de la mecánica cuántica (§1.5, tras 1.5.9).

### 2.6 Sum-Frequency Generation (p. 91)

Las ecuaciones (2.2.10)–(2.2.12b) se resuelven exactamente con funciones elípticas de Jacobi
(Armstrong et al. 1962; Problema 2); aquí se trata el caso más simple: $\omega_2$ intenso (bomba no
agotada, $A_2$ constante) y $\omega_1$ débil — **conversión ascendente** (*upconversion*) de una señal IR
débil $\omega_1$ a visible $\omega_3$ (Boyd y Townes 1977), útil porque el visible se detecta con mejor
sensibilidad. Fig. 2.6.1: típicamente no se aplica campo de entrada en $\omega_3$. Ecuaciones (p. 92):
$$\frac{dA_1}{dz}=K_1A_3e^{-i\Delta kz}\quad(2.6.1a),\qquad \frac{dA_3}{dz}=K_3A_1e^{+i\Delta kz}\quad(2.6.1b),$$
$$K_1=\frac{2i\omega_1^2d_{\rm eff}}{k_1c^2}A_2^*,\qquad K_3=\frac{2i\omega_3^2d_{\rm eff}}{k_3c^2}A_2\quad(2.6.2a),\qquad \Delta k=k_1+k_2-k_3\quad(2.6.2b).$$
**Caso $\Delta k=0$.** Derivando (2.6.1a): $d^2A_1/dz^2=K_1dA_3/dz$ (2.6.3) y con (2.6.1b)
$$\frac{d^2A_1}{dz^2}=-\kappa^2A_1\quad(2.6.4),\qquad \kappa^2\equiv-K_1K_3=\frac{4\omega_1^2\omega_3^2d_{\rm eff}^2|A_2|^2}{k_1k_3c^4}\quad(2.6.5)\ (\text{positivo}).$$
$A_1=B\cos\kappa z+C\sin\kappa z$ (2.6.6a), $A_3=(dA_1/dz)/K_1=-(B\kappa/K_1)\sin\kappa z+(C\kappa/K_1)\cos\kappa z$ (2.6.6b).
Con $A_3(0)=0$ ⇒ $C=0$, $B=A_1(0)$ (p. 93):
$$A_1(z)=A_1(0)\cos\kappa z\quad(2.6.7),\qquad A_3(z)=-A_1(0)\frac{\kappa}{K_1}\sin\kappa z\quad(2.6.8).$$
Con $\kappa/K_1=-i(n_1\omega_3/n_3\omega_1)^{1/2}|A_2|/A_2^*$ y $|A_2|/A_2^*=e^{i\phi_2}$ ($\phi_2$ fase de $A_2$):
$$A_3(z)=i\Big(\frac{n_1\omega_3}{n_3\omega_1}\Big)^{1/2}A_1(0)\sin\kappa z\,e^{i\phi_2}\quad(2.6.9).$$
Fig. 2.6.2: $|A_1|^2$ y $|A_3|^2$ intercambian energía periódicamente en $\kappa z$ (conversión completa y
regreso).

**Desajuste arbitrario (p. 94).** Prueba:
$$A_1(z)=(Fe^{igz}+Ge^{-igz})e^{-i\Delta kz/2}\quad(2.6.10),\qquad A_3(z)=(Ce^{igz}+De^{-igz})e^{i\Delta kz/2}\quad(2.6.11).$$
Sustituyendo en (2.6.1a) (2.6.12) e igualando coeficientes de $e^{\pm igz}$:
$F(ig-\tfrac12i\Delta k)=K_1C$ (2.6.13), $-G(ig+\tfrac12i\Delta k)=K_1D$ (2.6.14); en (2.6.1b) (2.6.15):
$C(ig+\tfrac12i\Delta k)=K_3F$ (2.6.16), $-D(ig-\tfrac12i\Delta k)=K_3G$ (2.6.17). Sistema para $F,C$:
$\begin{bmatrix}i(g-\frac12\Delta k)&-K_1\\-K_3&i(g+\frac12\Delta k)\end{bmatrix}\begin{bmatrix}F\\C\end{bmatrix}=0$; determinante nulo (p. 95):
$$g^2=-K_1K_3+\tfrac14\Delta k^2\quad(2.6.18),\qquad g=\sqrt{\kappa^2+\tfrac14\Delta k^2}\quad(2.6.19)$$
(raíz positiva, pues la prueba ya contiene $e^{\pm igz}$). Condiciones de frontera $A_1(0)=F+G$ (2.6.20),
$A_3(0)=C+D$ (2.6.21) más (2.6.13)–(2.6.14):
$$A_1(z)=\Big[A_1(0)\cos gz+\Big(\frac{K_1}{g}A_3(0)+\frac{i\Delta k}{2g}A_1(0)\Big)\sin gz\Big]e^{-i\Delta kz/2}\quad(2.6.22),$$
$$A_3(z)=\Big[A_3(0)\cos gz+\Big(\frac{-i\Delta k}{2g}A_3(0)+\frac{K_3}{g}A_1(0)\Big)\sin gz\Big]e^{i\Delta kz/2}\quad(2.6.23).$$
Con $A_3(0)=0$ (p. 96):
$$A_3(z)=\frac{K_3}{g}A_1(0)\sin gz\,e^{i\Delta kz/2}\quad(2.6.24),\qquad |A_3(z)|^2=|A_1(0)|^2\frac{|K_3|^2}{g^2}\sin^2gz\quad(2.6.25).$$
Al crecer $\Delta k$ la escala $g^{-1}$ se acorta pero el máximo cae por el factor $|K_3|^2/(\kappa^2+\tfrac14\Delta k^2)$
(Fig. 2.6.3: $|A_3|^2$ vs. $z$ para $\Delta k=0$ y $\Delta k=4\kappa$, este último con oscilaciones más rápidas y pequeñas).

### 2.7 Second-Harmonic Generation (p. 96)

Medio sin pérdidas en $\omega_1$ y $\omega_2=2\omega_1$ (simetría de permutación completa); se sigue a Armstrong
et al. (1962). Fig. 2.7.1 (p. 97): cristal de longitud $L$, $d_{\rm eff}=\tfrac12\chi^{(2)}$. Campo total
$\tilde E(z,t)=\tilde E_1+\tilde E_2$ (2.7.1), con
$$\tilde E_j(z,t)=E_j(z)e^{-i\omega_jt}+\text{c.c.}\ (2.7.2),\quad E_j(z)=A_j(z)e^{ik_jz}\ (2.7.3),\quad k_j=n_j\omega_j/c,\ n_j=[\epsilon^{(1)}(\omega_j)]^{1/2}\ (2.7.4),$$
$$\frac{\partial^2\tilde E_j}{\partial z^2}-\frac{\epsilon^{(1)}(\omega_j)}{c^2}\frac{\partial^2\tilde E_j}{\partial t^2}=\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde P_j}{\partial t^2}\quad(2.7.5),$$
$\tilde P^{\rm NL}=\tilde P_1+\tilde P_2$ (2.7.6), $\tilde P_j=P_je^{-i\omega_jt}+\text{c.c.}$ (2.7.7), y por (1.5.28)–(1.5.29):
$$P_1(z)=4\epsilon_0d_{\rm eff}E_2E_1^*=4\epsilon_0d_{\rm eff}A_2A_1^*e^{i(k_2-k_1)z}\quad(2.7.8),\qquad P_2(z)=2\epsilon_0d_{\rm eff}E_1^2=2\epsilon_0d_{\rm eff}A_1^2e^{2ik_1z}\quad(2.7.9)$$
— **factores de degeneración distintos** (4 vs. 2). Ecuaciones acopladas (p. 98):
$$\frac{dA_1}{dz}=\frac{2i\omega_1^2d_{\rm eff}}{k_1c^2}A_2A_1^*e^{-i\Delta kz}\quad(2.7.10),\qquad \frac{dA_2}{dz}=\frac{i\omega_2^2d_{\rm eff}}{k_2c^2}A_1^2e^{i\Delta kz}\quad(2.7.11),\qquad \Delta k=2k_1-k_2\quad(2.7.12).$$
Con bomba no agotada ($A_1$ cte.) (2.7.11) se integra directamente. En general: variables reales de
módulo y fase, adimensionales:
$$A_1=\Big(\frac{I}{2n_1\epsilon_0c}\Big)^{1/2}u_1e^{i\phi_1}\ (2.7.13),\qquad A_2=\Big(\frac{I}{2n_2\epsilon_0c}\Big)^{1/2}u_2e^{i\phi_2}\ (2.7.14),$$
$I=I_1+I_2$ (2.7.15), $I_j=2n_j\epsilon_0c|A_j|^2$ (2.7.16). Por Manley–Rowe $I$ es invariante, y
$$u_1(z)^2+u_2(z)^2=1\quad(2.7.17).$$
Distancia normalizada $\zeta=z/l$ (2.7.18), con (p. 99)
$$l=\Big(\frac{2n_1^2n_2}{\epsilon_0cI}\Big)^{1/2}\frac{c}{2\omega_1d_{\rm eff}}\quad(2.7.19)\ \text{[así impreso; ver erratas]},$$
distancia característica de intercambio de energía; fase relativa y desajuste normalizado:
$$\theta=2\phi_1-\phi_2+\Delta kz\quad(2.7.20),\qquad \Delta s=\Delta k\,l\quad(2.7.21).$$
Tras álgebra "directa pero larga":
$$\frac{du_1}{d\zeta}=u_1u_2\sin\theta\ (2.7.22),\qquad \frac{du_2}{d\zeta}=-u_1^2\sin\theta\ (2.7.23),\qquad \frac{d\theta}{d\zeta}=\Delta s+\frac{\cos\theta}{\sin\theta}\frac{d}{d\zeta}(\ln u_1^2u_2)\ (2.7.24).$$
**Caso $\Delta s=0$.** (2.7.24) equivale a $\frac{d}{d\zeta}\ln(u_1^2u_2\cos\theta)=0$ (2.7.25) ⇒
$$u_1^2u_2\cos\theta=\Gamma\quad(2.7.26),$$
constante fijada por las condiciones en $\zeta=0$. Dos cantidades conservadas: $u_1^2+u_2^2$ y $u_1^2u_2\cos\theta$.
Desacoplando (p. 100): $du_2/d\zeta=\pm(1-u_2^2)(1-\cos^2\theta)^{1/2}$ (2.7.27);
$$\frac{du_2}{d\zeta}=\pm(1-u_2^2)\Big(1-\frac{\Gamma^2}{u_1^4u_2^2}\Big)^{1/2}=\pm(1-u_2^2)\Big(1-\frac{\Gamma^2}{(1-u_2^2)^2u_2^2}\Big)^{1/2}\quad(2.7.28),$$
$u_2\,du_2/d\zeta=\pm[(1-u_2^2)^2u_2^2-\Gamma^2]^{1/2}$, o
$$\frac{du_2^2}{d\zeta}=\pm2[(1-u_2^2)^2u_2^2-\Gamma^2]^{1/2}\quad(2.7.29),$$
de forma estándar con solución en funciones elípticas de Jacobi; en general fundamental y armónico
intercambian energía periódicamente (Fig. 2.7.2, fracción de potencia $u_j^2$ vs. $\zeta$, tras Armstrong).

**Caso $\Gamma=0$** (p. 101): ocurre si alguno de los campos de entrada es cero o si $\cos\theta=0$
inicialmente; como $\Gamma$ se conserva, $\cos\theta=0$ (2.7.30a) en todo $\zeta$; se elige $\sin\theta=-1$
(2.7.30b): la fase relativa es invariante. Entonces
$$\frac{du_1}{d\zeta}=-u_1u_2\ (2.7.31),\qquad \frac{du_2}{d\zeta}=u_1^2\ (2.7.32)\ \Rightarrow\ \frac{du_2}{d\zeta}=1-u_2^2\ (2.7.33),\qquad u_2=\tanh(\zeta+\zeta_0)\ (2.7.34).$$
Con $u_1(0)=1$, $u_2(0)=0$ (2.7.35) (no incide SH): $\zeta_0=0$,
$$\boxed{u_2(\zeta)=\tanh\zeta\ (2.7.36),\qquad u_1(\zeta)=\mathrm{sech}\,\zeta\ (2.7.37)}$$
y con solo el fundamental en $z=0$ (p. 102)
$$l=\frac{(n_1n_2)^{1/2}c}{2\omega_1d_{\rm eff}|A_1(0)|}\quad(2.7.38).$$
Fig. 2.7.3: $u_1$ decae (sech) y $u_2$ crece (tanh), se cruzan cerca de $\zeta\approx0.9$; para $\zeta\to\infty$ toda la
radiación pasa al armónico; como $\tanh(\zeta+\zeta_0)$ tiene la misma asíntota, con $\Gamma=0$ todo el
fundamental acaba convertido para cualquier razón inicial $u_1/u_2$. Para $\Delta k$ arbitrario Armstrong
también resolvió con integrales elípticas: **Fig. 2.7.4** (p. 103): $u_2$ vs. $\zeta$ (0–2.5) para $\Delta s=0$
(tanh, satura en 1), 2, 10, 25: el desajuste baja la eficiencia y produce oscilaciones más rápidas y
de menor amplitud.

**Estimado numérico de eficiencia con láser CW (p. 102–104).** Potencia $P$ enfocada a radio $w_0$ en el
centro del cristal:
$$I_1=\frac{P}{\pi w_0^2}=2n_1\epsilon_0cA_1^2\quad(2.7.39);$$
enfoque óptimo con profundidad focal igual a $L$ (ver §2.10):
$$b\equiv\frac{2\pi w_0^2}{\lambda_1/n_1}=L\quad(2.7.40)\ \Rightarrow\ A_1=\Big(\frac{P}{\epsilon_0c\lambda_1L}\Big)^{1/2}\quad(2.7.41),$$
$$\zeta=\frac{L}{l}=\Big(\frac{16\pi^2d_{\rm eff}^2LP}{\epsilon_0cn_1n_2\lambda_1^3}\Big)^{1/2}\quad(2.7.42).$$
Valores típicos: $d_{\rm eff}=4\times10^{-12}$ m/V, $L=1$ cm, $P=1$ W, $\lambda=0.5\times10^{-6}$ m, $n=2$ ⇒ **$\zeta=0.14$**
(verificado: 0.138). Eficiencia
$$\eta=\frac{u_2^2(L)}{u_1^2(0)}\quad(2.7.43)$$
y con (2.7.36), $\eta=\tanh^2(0.14)\approx$ **2 %** (p. 104).

#### 2.7.1 Applications of Second-Harmonic Generation (p. 104)

*Surface nonlinear optics.* SHG está prohibida en medios centrosimétricos, pero la superficie
carece de simetría de inversión: hay SHG superficial en materiales de cualquier grupo de simetría;
su intensidad y distribución angular dependen críticamente de la morfología y de impurezas.
Revisiones: Shen (1985, 1989); cálculo de la intensidad: Mizrahi y Sipe (1988).

*Nonlinear optical microscopy* (p. 104–105). Mayor resolución transversal y longitudinal (el proceso
se excita donde la intensidad es máxima); señal lejos en frecuencia del fondo por esparcimiento
lineal; longitudes de onda largas no dañinas para tejidos biológicos con resolución de longitud de
onda más corta; respuesta intrínseca o cromóforos no lineales. SHG confocal con pulsos fs: Curley et
al. (1992); imágenes de objetos de fase porque el ajuste de fase depende de la variación de índice
(Muller et al. 1998); tomografía SHG de materiales biológicos (Guo et al. 1997); imagen 3D con
pulsos fs de la estructura microcristalina del triborato de litio (Gauderon et al. 1998); células
vivas (Campagnola et al. 1999); membranas marcadas con colorantes estirílicos (Moreaux et al. 2000).
THG: objetos transparentes (Muller et al. 1998), microscopio de barrido para material biológico
(Yelin y Silberberg 1999). No armónicos: iluminación estructurada + absorción saturable, resolución
transversal de **50 nm** (Gustafsson 2005); STED (Westphal y Hell 2005), **16 nm** o 1/50 de la longitud
de onda de operación.

### 2.8 Difference-Frequency Generation and Parametric Amplification (p. 105)

Ondas $\omega_3$ (fuerte, no agotada, $A_3$ cte.) y $\omega_1$ producen $\omega_2=\omega_3-\omega_1$; sin campo incidente en
$\omega_2$ (Fig. 2.8.1). Ecuaciones (p. 106):
$$\frac{dA_1}{dz}=\frac{2i\omega_1^2d_{\rm eff}}{k_1c^2}A_3A_2^*e^{i\Delta kz}\quad(2.8.1a),\qquad \frac{dA_2}{dz}=\frac{2i\omega_2^2d_{\rm eff}}{k_2c^2}A_3A_1^*e^{i\Delta kz}\quad(2.8.1b),$$
$$\Delta k=k_3-k_1-k_2\quad(2.8.2)\ \text{(signo opuesto a la convención de SFG, Eq. 2.2.11)}.$$
Con $\Delta k=0$: derivando (2.8.1b) y usando el conjugado de (2.8.1a) para eliminar $dA_1^*/dz$,
$$\frac{d^2A_2}{dz^2}=\frac{4\omega_1^2\omega_2^2d_{\rm eff}^2}{k_1k_2c^4}A_3A_3^*A_2\equiv\kappa^2A_2\quad(2.8.3),\qquad \kappa^2=\frac{4d_{\rm eff}^2\omega_1^2\omega_2^2}{k_1k_2c^4}|A_3|^2\quad(2.8.4),$$
$A_2(z)=C\sinh\kappa z+D\cosh\kappa z$ (2.8.5). Con $A_2(0)=0$, $A_1(0)$ arbitrario (2.8.6):
$$A_1(z)=A_1(0)\cosh\kappa z\quad(2.8.7),\qquad A_2(z)=i\Big(\frac{n_1\omega_2}{n_2\omega_1}\Big)^{1/2}\frac{A_3}{|A_3|}A_1^*(0)\sinh\kappa z\quad(2.8.8).$$
Fig. 2.8.2 (p. 107): ambos crecen monótonamente y para $\kappa z\gg1$ como $e^{\kappa z}$. El campo $\omega_1$ conserva su fase
inicial (se amplifica); la fase de $\omega_2$ depende de la de la bomba y la de $\omega_1$. Contraste con SFG
(oscilatoria). Intuición (Fig. 2.8.3, p. 108): el campo $\omega_1$ estimula la transición descendente que
genera $\omega_2$ y viceversa ⇒ refuerzo mutuo ⇒ crecimiento exponencial. Lenguaje: **amplificación
paramétrica**; la señal ($\omega_1$) se amplifica y se genera la onda *idler* ($\omega_2=\omega_3-\omega_1$); con espejos
altamente reflectores en $\omega_1$ y/o $\omega_2$ se obtiene un **oscilador paramétrico**. "El primer OPO CW fue
construido por Giordmaine y Miller en 1965" (p. 108; ver erratas: en p. 115 el de Giordmaine–Miller es
pulsado y el primer CW es Smith et al. 1968). Revisión: Byer y Herbst (1977). Caso $\Delta k\neq0$: Problema 4.

### 2.9 Optical Parametric Oscillators (p. 108)

Fig. 2.9.1: (a) al generar $\omega_i=\omega_p-\omega_s$ se amplifica la onda de entrada de menor frecuencia $\omega_s$
(bomba $\omega_p=\omega_3$, señal $\omega_s=\omega_1$, idler $\omega_i=\omega_2$); (b) cristal $\chi^{(2)}$ de longitud $L$ entre espejos con
reflectividades $R_1,R_2$ (señal, idler). **Doblemente resonante (DRO)**: espejos altamente
reflectores en $\omega_s$ y $\omega_i$; **simplemente resonante (SRO)**: en uno solo. Cerca de la degeneración
($\omega_s=\omega_i$) tiende a operar como DRO (en tipo II se puede suprimir por polarización la realimentación de
una de las ondas). Fuente sintonizable versátil en IR, visible y UV, CW o pulsos de ns, ps o fs.

Ganancia (p. 109), con (2.9.1a,b) idénticas a (2.8.1) y $\Delta k\equiv k_3-k_1-k_2$:
$$A_1(z)=\Big[A_1(0)\Big(\cosh gz-\frac{i\Delta k}{2g}\sinh gz\Big)+\frac{\kappa_1}{g}A_2^*(0)\sinh gz\Big]e^{i\Delta kz/2}\quad(2.9.2a),$$
$$A_2(z)=\Big[A_2(0)\Big(\cosh gz-\frac{i\Delta k}{2g}\sinh gz\Big)+\frac{\kappa_2}{g}A_1^*(0)\sinh gz\Big]e^{i\Delta kz/2}\quad(2.9.2b),$$
$$g=[\kappa_1\kappa_2^*-(\Delta k/2)^2]^{1/2},\qquad \kappa_i=\frac{2i\omega_i^2d_{\rm eff}A_3}{k_ic^2}\quad(2.9.3).$$
Con $\Delta k=0$, $A_2(0)=0$ (p. 110):
$$A_1(z)=A_1(0)\cosh gz\Rightarrow\tfrac12A_1(0)\exp(gz)\quad(2.9.4a),$$
$$A_2(z)=i\Big(\frac{n_1\omega_2}{n_2\omega_1}\Big)^{1/2}\frac{A_3}{|A_3|}A_1^*(0)\sinh gz\to O(1)A_1^*(0)\exp(gz)\quad(2.9.4b):$$
crecimiento exponencial asintótico con **coeficiente de ganancia de amplitud $g$**.

**Umbral de oscilación (p. 110).** Espejos idénticos con reflectividades de intensidad $R_1,R_2$. Primera
aproximación: ganancia fraccional de energía por paso = pérdida fraccional por paso. Con resonancia
exacta, $\Delta k=0$, DRO con $R_1=R_2\equiv R$, $1-R\ll1$:
$$(e^{2gL}-1)=2(1-R)\quad(2.9.5)\ \Rightarrow\ gL=1-R\quad(2.9.6)\quad(2gL\ \text{no grande frente a 1}),$$
condición formulada por Giordmaine y Miller (1965). Más general: los campos deben replicarse en cada
ida y vuelta:
$$A_1(0)=\Big[A_1(0)\cosh gL+\frac{\kappa_1}{g}A_2^*(0)\sinh gL\Big](1-l_1)\quad(2.9.7a),$$
$$A_2^*(0)=\Big[A_2^*(0)\cosh gL+\frac{\kappa_2^*}{g}A_1(0)\sinh gL\Big](1-l_2)\quad(2.9.7b),$$
$l_i=1-R_ie^{-\alpha_iL}$ = pérdida fraccional de **amplitud** por paso ($\alpha_i$ coef. de absorción en $\omega_i$). Exigiendo ambas (p. 111):
$$\cosh gL=1+\frac{l_1l_2}{2-l_1-l_2}\quad(2.9.8).$$
DRO ($l_1,l_2\ll1$, $\cosh gL\approx1+\tfrac12g^2L^2$): $g^2L^2=l_1l_2$ (2.9.9), consistente con (2.9.6). SRO (sin
realimentación del idler, $l_2=1$; $l_1\ll1$): $g^2L^2=2l_1$ (2.9.10). El umbral de $gL$ del SRO es mayor en un
factor $(2/l_2)^{1/2}$, pero suele preferirse el SRO por su mayor estabilidad. Con $\Delta k\neq0$: reemplazar
$g^2$ por $g^2\,\mathrm{sinc}^2(\Delta kL/2)$ en (2.9.9) y (2.9.10).

**Sintonía en longitud de onda.** $\omega_s+\omega_i=\omega_p$ permite cualquier $\omega_s<\omega_p$; la salida la fija $\Delta k=0$,
que se cumple para a lo sumo un par $\omega_s,\omega_i$ (por ángulo o temperatura, §2.3). El ancho de banda se
estrecha con elementos selectivos (etalones) dentro de la cavidad.

#### 2.9.1 Influence of Cavity Mode Structure on OPO Tuning (p. 112)

El espaciado de modos y el ancho de cada resonancia son mucho menores que el ancho de la curva de
ganancia paramétrica (Fig. 2.9.2). **Ejemplo (nota al pie, p. 112):** $L_c=15$ cm ⇒ $\Delta\nu_c=c/2L_c=1$ GHz; fineza
$\mathcal F=100$ ⇒ ancho de cada modo 1 GHz/$\mathcal F$ = 10 MHz; ancho de ganancia ≈ **100 GHz**, estimado suponiendo
que $\Delta kL$ (cero en el centro) llega a $\pi$ en el borde de la línea, con $dn/d\nu\sim10^{-15}$ s.

*SRO* (Fig. 2.9.3a, p. 113): oscila en el modo de cavidad más cercano al pico de ganancia ($\Delta k=0$) y en
uno solo: al arrancar, la bomba se agota y la ganancia baja al nivel de pérdida de ese modo; los demás
quedan bajo umbral (análogo a un láser con ensanchamiento homogéneo). *DRO* (Fig. 2.9.3b; ejes de señal e
idler crecen en sentidos opuestos para que $\omega_s+\omega_i=\omega_p$ en cada punto horizontal): oscila donde coinciden
un modo de señal y uno de idler, no necesariamente cerca del pico ⇒ sintonía no suave e inestabilidad
(pequeñas fluctuaciones de $\omega_p$ o de $L$ dan grandes cambios de $\omega_s$). El argumento supone modos no
equiespaciados; en una cavidad con medio dispersivo (p. 114)
$$\Delta\nu_c=\frac{1}{n^{(g)}}\frac{c}{2L_c},\qquad n^{(g)}=n+\nu\frac{dn}{d\nu}\quad(2.9.11)\quad\text{(índice de grupo; Problemas 7 y 8)}.$$
Estimación de la separación $\delta\omega$ entre el pico de ganancia y la oscilación real:
$$\Delta\omega\equiv\omega_p-\omega_s^{(m)}-\omega_i^{(m)}\quad(2.9.12)$$
(oscila solo si $\Delta\omega\lesssim\delta\omega_c$, ancho espectral de la resonancia). Al saltar un modo en $\omega_s$ y en $\omega_i$:
$$\delta(\Delta\omega)=2\pi\Big(\frac{c}{2n_s^{(g)}L_c}-\frac{c}{2n_i^{(g)}L_c}\Big)=\frac{\pi c}{L_c}\Big(\frac{n_i^{(g)}-n_s^{(g)}}{n_s^{(g)}n_i^{(g)}}\Big)\quad(2.9.13).$$
Sin control activo de la longitud, cerca de $\Delta k=0$, $\Delta\omega$ puede valer hasta medio espaciado de modos:
$$\Delta\omega_0\simeq\frac12\Big(\frac{2\pi c}{2n^{(g)}L_c}\Big)=\frac{\pi c}{2n^{(g)}L_c}\quad(2.9.14),\qquad N=\frac{\Delta\omega_0}{\delta(\Delta\omega)}=\frac{n^{(g)}}{2(n_s^{(g)}-n_i^{(g)})}\quad(2.9.15),$$
$$\delta\omega=\Delta\omega_cN\simeq\frac{2\pi c}{2n^{(g)}L_c}N=\frac{\pi c}{2L_c}\frac{1}{(n_s^{(g)}-n_i^{(g)})}\quad(2.9.16),$$
muy grande si $n_s^{(g)}\approx n_i^{(g)}$ (p. 115). **Ancho de línea operativo**: por ruido técnico (vibraciones ⇒
jitter $\delta\omega_c$ de cada modo; ancho espectral de la bomba $\delta\omega_p$), $\delta\omega_{\rm eff}=\max(\delta\omega_c,\delta\omega_p)$ y
$$N_{\rm osc}=\frac{\delta\omega_{\rm eff}}{\delta(\Delta\omega)}=\frac{\max(\delta\omega_p,\delta\omega_c)}{\delta(\Delta\omega)}\quad(2.9.17),\qquad \delta\omega^{(\rm osc)}=N_{\rm OPO}\Delta\omega_c=\frac{n_g}{n_g^{(s)}-n_g^{(i)}}\max(\delta\omega_p,\delta\omega_c)\quad(2.9.18).$$
El ancho de un OPO tiende a ser mucho mayor que el de la bomba o el de la cavidad desnuda (se reduce con
estabilización activa). (2.9.18) diverge formalmente en la degeneración para tipo I (no para tipo II):
Bosenberg y Tang (1990) observaron un OPO tipo II más angosto que uno tipo I del mismo material.

**Historia (p. 115–116):** primer OPO: Giordmaine y Miller (1965), LiNbO$_3$, pulsado; CW: Smith et al. (1968),
Ba$_2$NaNb$_5$O$_{15}$; renacer en los 80 con β-BaB$_2$O$_4$ (BBO), LiB$_3$O$_5$ (LBO) y KTiOPO$_4$ (KTP) (alta no linealidad,
alta resistencia al daño, gran birrefringencia): sintonía continua de **0.42 a 2.3 μm** en un OPO de BBO con
eficiencias de hasta **32 %** (Bosenberg et al. 1989); pulsos fs sintonizables en KTP (Edelstein et al. 1989);
OPOs con QPM en niobato de litio periódicamente polarizado.

### 2.10 Nonlinear Optical Interactions with Focused Gaussian Beams (p. 116)

En la práctica la radiación se enfoca para aumentar la intensidad y la eficiencia; se abandona la
aproximación de ondas planas infinitas.

#### 2.10.1 Paraxial Wave Equation (p. 116)

Cada componente obedece (forma de 2.1.21)
$$\nabla^2\tilde{\mathbf E}_n-\frac{1}{(c/n)^2}\frac{\partial^2\tilde{\mathbf E}_n}{\partial t^2}=\frac{1}{\epsilon_0c^2}\frac{\partial^2\tilde{\mathbf P}_n}{\partial t^2}\quad(2.10.1),$$
$$\tilde{\mathbf E}_n(\mathbf r,t)=\mathbf A_n(\mathbf r)e^{i(k_nz-\omega_nt)}+\text{c.c.}\quad(2.10.2a),\qquad \tilde{\mathbf P}_n(\mathbf r,t)=\mathbf p_n(\mathbf r)e^{i(k_n'z-\omega_nt)}+\text{c.c.}\quad(2.10.2b),$$
con amplitudes complejas que varían en el espacio (ondas no planas) y vector de onda de la polarización
$k_n'$ posiblemente distinto de $k_n$. Con $\nabla^2=\partial^2/\partial z^2+\nabla_T^2$ ($\nabla_T^2=\partial_x^2+\partial_y^2$, o
$(1/r)\partial_r(r\partial_r)+(1/r^2)\partial_\phi^2$) y SVEA en $z$ (p. 117):
$$2ik_n\frac{\partial\mathbf A_n}{\partial z}+\nabla_T^2\mathbf A_n=-\frac{\omega_n^2}{\epsilon_0c^2}\mathbf p_ne^{i\Delta kz},\qquad \Delta k=k_n'-k_n\quad(2.10.3)$$
— **ecuación de onda paraxial** (se desprecia $\partial^2A/\partial z^2$, justificado si la onda se propaga
principalmente a lo largo de $z$).

#### 2.10.2 Gaussian Beams (p. 117)

Solución libre ($\mathbf p_n=0$), aproximación escalar (Kogelnik y Li 1966):
$$A(r,z)=\mathcal A\frac{w_0}{w(z)}e^{-r^2/w(z)^2}e^{ikr^2/2R(z)}e^{i\Phi(z)}\quad(2.10.4a),$$
$$w(z)=w_0[1+(\lambda z/\pi w_0^2)^2]^{1/2}\ (2.10.4b)\ \text{(radio }1/e\text{ del campo)},\qquad R(z)=z[1+(\pi w_0^2/\lambda z)^2]\ (2.10.4c),$$
$$\Phi(z)=-\arctan(\lambda z/\pi w_0^2)\quad(2.10.4d)\ \text{(fase respecto a la onda plana)},$$
$w_0$ = radio de cintura ($z=0$), $\lambda=2\pi c/n\omega$ = longitud de onda **en el medio**; divergencia de campo
lejano $\theta_{\rm ff}=\lambda/\pi w_0$. Fig. 2.10.1 (p. 118): (a) perfil gaussiano de amplitud, ancho $2w(z)$ al nivel
$1/e$; (b) $w(z)$ y $R(z)$; (c) parámetro confocal $b$: en $z=\pm b/2$ el diámetro vale $2\sqrt2w_0$. Forma compacta
(Problema 10):
$$A(r,z)=\frac{\mathcal A}{1+i\zeta}e^{-r^2/w_0^2(1+i\zeta)}\quad(2.10.5a),\qquad \zeta=2z/b\quad(2.10.5b),\qquad b=2\pi w_0^2/\lambda=kw_0^2\quad(2.10.5c)$$
($\zeta$ aquí no tiene relación con el de (2.7.18)). Potencia total, con $\mathcal P=\int I\,2\pi r\,dr$ e $I=2n\epsilon_0c|A|^2$ (p. 119):
$$\mathcal P=n\epsilon_0c\pi w_0^2|\mathcal A|^2\quad(2.10.6).$$

#### 2.10.3 Harmonic Generation Using Focused Gaussian Beams (p. 119)

Armónico $q$-ésimo, $\omega_q=q\omega$, con $p_q=\epsilon_0\chi^{(q)}A_1^q$, $\chi^{(q)}=\chi^{(q)}(q\omega=\omega+\omega+\dots+\omega)$:
$$2ik_q\frac{\partial A_q}{\partial z}+\nabla_T^2A_q=-\frac{\omega_q^2}{c^2}\chi^{(q)}A_1^qe^{i\Delta kz},\qquad \Delta k=qk_1-k_q\quad(2.10.7),$$
$$A_1(r,z)=\frac{\mathcal A_1}{1+i\zeta}e^{-r^2/w_0^2(1+i\zeta)}\quad(2.10.8).$$
Bomba constante; prueba con la misma dependencia radial que la fuente:
$$A_q(r,z)=\frac{\mathcal A_q(z)}{1+i\zeta}e^{-qr^2/w_0^2(1+i\zeta)}\quad(2.10.9)$$
— haz con el **mismo parámetro confocal** que el fundamental (el armónico se genera coherentemente en
una región de igual extensión longitudinal). Satisface (2.10.7) con muy buena aproximación si
$$\frac{d\mathcal A_q}{dz}=\frac{iq\omega}{2n_qc}\chi^{(q)}\mathcal A_1^q\frac{e^{i\Delta kz}}{(1+i\zeta)^{q-1}}\quad(2.10.10),$$
$$\mathcal A_q(z)=\frac{iq\omega}{2nc}\chi^{(q)}\mathcal A_1^qJ_q(\Delta k,z_0,z)\quad(2.10.11a),\qquad J_q(\Delta k,z_0,z)=\int_{z_0}^z\frac{e^{i\Delta kz'}dz'}{(1+2iz'/b)^{q-1}}\quad(2.10.11b),\ \text{p. 120},$$
$z_0$ = entrada al medio. Como $b$ es el mismo, la cintura del armónico es $q^{1/2}$ veces menor y su
divergencia $\theta_{\rm ff}$ también $q^{1/2}$ veces menor. Soluciones constructivas: Kleinman et al. (1966) para SHG,
Ward y New (1969) para el caso general.

*Límite de onda plana* ($b\gg|z_0|,|z|$):
$$J_q=\int_{z_0}^ze^{i\Delta kz'}dz'=\frac{e^{i\Delta kz}-e^{i\Delta kz_0}}{i\Delta k}\quad(2.10.12a),\qquad |J_q|^2=L^2\,\mathrm{sinc}^2(\Delta kL/2),\ L=z-z_0\quad(2.10.12b).$$
*Enfoque fuerte dentro del medio* ($z_0=-|z_0|$, $z=|z|$, $b\ll|z_0|,|z|$): límites $\to\pm\infty$,
$$J_q=\int_{-\infty}^{\infty}\frac{e^{i\Delta kz'}dz'}{(1+2iz'/b)^{q-1}}\quad(2.10.13a),\qquad J_q=\begin{cases}0,&\Delta k\le0,\\[2pt] \dfrac b2\dfrac{2\pi}{(q-2)!}\Big(\dfrac{b\Delta k}{2}\Big)^{q-2}e^{-b\Delta k/2},&\Delta k>0\end{cases}\quad(2.10.13b)$$
(integración de contorno, Problema 12). **Fig. 2.10.2** (p. 121): $J_3/b$ vs. $b\Delta k$ (−10 a 10) para THG: cero
para $b\Delta k\le0$, sube abruptamente, máximo ≈ 1.15 en $b\Delta k=2$ (de (2.10.13b) con $q=3$: $J_3/b=\pi(b\Delta k/2)e^{-b\Delta k/2}$,
máximo $\pi/e\approx1.16$) y luego decae. Resultado sorprendente: con enfoque fuerte, la THG se anula
idénticamente con ajuste de fase perfecto y se maximiza con desajuste **positivo**. Explicación: **fase de
Gouy** (anomalía de fase, Gouy 1890): todo haz adquiere un desfase de $\pi$ al pasar por el foco; la
polarización $p=\epsilon_0\chi^{(q)}A_1^q$ adquiere un desfase $q$ veces mayor y no acopla eficientemente con $A_q$ salvo que
$\Delta k$ lo compense. **Fig. 2.10.3** (p. 122): (a) diagrama de vectores de onda para THG con $\Delta k>0$; (b) el haz
enfocado contiene una dispersión angular de $\mathbf k$ que permite un proceso no colineal ajustado en fase; (c)
con $\Delta k<0$ no es posible.

**Optimización de Boyd y Kleinman (1968)** (p. 121–122): para SHG, máxima eficiencia cuando el walkoff es
despreciable, la cintura está en el **centro del cristal**, **$L/b=2.84$** y **$\Delta k=3.2/L$**:
$$\mathcal P_{2\omega}=K\Big[\frac{128\pi^2\omega_1^3d_{\rm eff}^2L}{c^4n_1n_2}\Big]\mathcal P_\omega^2\quad(2.10.14),$$
$K$ = constante que depende del sistema de unidades; en el **sistema gaussiano** (el del trabajo original)
$K=1.068$. Nótese $\mathcal P_{2\omega}\propto L$ (no $L^2$) en enfoque óptimo (Problema 21). Heurísticamente, SFG y DFG se
optimizan con el mismo parámetro confocal para ambos haces de entrada y los mismos criterios.

### 2.11 Nonlinear Optics at an Interface (p. 122)

Fig. 2.11.1 (p. 123): (a) onda sobre un material de segundo orden: además del SH hacia adelante (§2.7)
se genera un SH **reflejado** mucho más débil; (b) material **centrosimétrico**: sin $\chi^{(2)}$ de volumen, pero
la interfaz rompe la simetría de inversión en una capa del orden de un diámetro molecular que emite SH;
muy sensible a la estructura superficial y a moléculas adsorbidas ⇒ diagnóstico en ciencia de superficies.

**Caso (a).** Onda incidente $\tilde{\mathbf E}_i=\mathbf E_i(\omega_i)e^{-i\omega_it}+\text{c.c.}$, $\mathbf E_i(\omega_i)=\mathbf A_i(\omega_i)e^{i\mathbf k_i(\omega_i)\cdot\mathbf r}$ (2.11.1); transmitida
$\mathbf E_T(\omega_i)=\mathbf A_T(\omega_i)e^{i\mathbf k_T(\omega_i)\cdot\mathbf r}$ (2.11.2) (de Fresnel). Se ignora la birrefringencia (nula en cristales
cúbicos no centrosimétricos como GaAs). Polarización no lineal en $\omega_s=2\omega_i$ (p. 124):
$$\tilde{\mathbf P}(\mathbf r,t)=\mathbf Pe^{-i\omega_st}+\text{c.c.},\quad \mathbf P=\mathbf pe^{i\mathbf k_s(\omega_s)\cdot\mathbf r},\quad \mathbf p=\hat{\mathbf p}\epsilon_0\chi^{(2)}_{\rm eff}A_T^2(\omega_i)\quad(2.11.3),\qquad \mathbf k_s(\omega_s)=2\mathbf k_T(\omega_i).$$
Solo se trata $\mathbf p$ **perpendicular al plano de incidencia (geometría TE)** (el otro caso: Bloembergen y
Pershan 1962; Shen 1984). Por (2.1.23):
$$\nabla^2\mathbf E(\omega_s)+[\epsilon(\omega_s)\omega_s^2/c^2]\mathbf E(\omega_s)=-(\omega_s^2/\epsilon_0c^2)\mathbf p_\perp e^{i\mathbf k_s\cdot\mathbf r}\quad(2.11.4).$$
Solución = particular + homogénea (onda plana de amplitud $\mathbf A(\omega_s)$ y vector $\mathbf k_T(\omega_s)$):
$$\mathbf E_T(\omega_s)=\mathbf A(\omega_s)e^{i\mathbf k_T(\omega_s)\cdot\mathbf r}+\frac{(\omega_s^2/\epsilon_0c^2)}{|\mathbf k_s|^2-|\mathbf k_T(\omega_s)|^2}\mathbf p_\perp e^{i\mathbf k_s\cdot\mathbf r}\quad(2.11.5),$$
$k_s=\sqrt{\epsilon(\omega_s)}\,\omega_s/c$ [así en el texto; ver (2.11.9)], $|\mathbf k_T(\omega_s)|^2=\epsilon_T(\omega_s)\omega_s^2/c^2$. La continuidad de las componentes
tangenciales de $\mathbf E$ y $\mathbf H$ exige una onda SH reflejada
$$\mathbf E_R(\omega_s)=\mathbf A_R(\omega_s)e^{i\mathbf k_R(\omega_s)\cdot\mathbf r}\quad(2.11.6)$$
y que $\mathbf k_s$, $\mathbf k_T(\omega_s)$ y $\mathbf k_R(\omega_s)$ tengan la misma componente a lo largo de la interfaz (Fig. 2.11.2, p. 125: $x$
en la interfaz dentro del plano de incidencia, $z$ normal; ángulos $\theta_i,\theta_R,\theta_s,\theta_T$; (b) $\mathbf E_\perp$ en $y$ y
$\mathbf H$ en el plano $xz$):
$$k_x^s=k_x^R(\omega_s)=k_x^T(\omega_s)\quad(2.11.7),\qquad k_x^s\equiv2k_x^T(\omega_i),$$
$$k_T(\omega_s)=\epsilon_T^{1/2}(\omega_s)\omega_s/c\ (2.11.8a),\quad k_R(\omega_s)=\epsilon_R^{1/2}(\omega_s)\omega_s/c\ (2.11.8b),\quad k_i(\omega_i)=\epsilon_R^{1/2}(\omega_i)\omega_i/c\ (2.11.8c),$$
$\epsilon_R$ = constante dieléctrica del medio lineal incidente, $\epsilon_T$ = la del medio no lineal; constante dieléctrica
ficticia $\epsilon_s$ asociada a la polarización (p. 126): $k_s=\epsilon_s^{1/2}\omega_s/c$ (2.11.9). **Ley de Snell no lineal**:
$$\epsilon_R^{1/2}(\omega_i)\sin\theta_i=\epsilon_R^{1/2}(\omega_s)\sin\theta_R=\epsilon_T^{1/2}(\omega_s)\sin\theta_T=\epsilon_s^{1/2}\sin\theta_s\quad(2.11.10).$$
Condiciones de frontera ($E_\perp=E_y$):
$$E_y:\ A_\perp^R=A_\perp^T+p_\perp/\epsilon_0c^2[\epsilon_s-\epsilon_T(\omega_s)],$$
$$H_x:\ -\epsilon_R^{1/2}(\omega_s)A_\perp^R\cos\theta_R=\epsilon_T^{1/2}(\omega_s)A_\perp^T\cos\theta_T+p_\perp\cos\theta_s\epsilon_s^{1/2}/[\epsilon_s-\epsilon_T(\omega_s)]\quad(2.11.11).$$
Resolviendo:
$$E_\perp^R=\frac{-\mu_0p_\perp e^{i\mathbf k_R(\omega_s)\cdot\mathbf r}}{[\epsilon_T^{1/2}(\omega_s)\cos\theta_T+\epsilon_R^{1/2}(\omega_s)\cos\theta_R][\epsilon_T^{1/2}(\omega_s)\cos\theta_T+\epsilon_s^{1/2}\cos\theta_s]}\equiv A_\perp^Re^{i\mathbf k_R(\omega_s)\cdot\mathbf r}\quad(2.11.12a),$$
$$E_\perp^T=\frac{-\mu_0p_\perp}{\epsilon_T(\omega_s)-\epsilon_s}\Big[e^{i\mathbf k_s\cdot\mathbf r}-\frac{\epsilon_s^{1/2}\cos\theta_s+\epsilon_R^{1/2}(\omega_s)\cos\theta_R}{\epsilon_T^{1/2}(\omega_s)\cos\theta_T+\epsilon_R^{1/2}(\omega_s)\cos\theta_R}e^{i\mathbf k_T(\omega_s)\cdot\mathbf r}\Big]\quad(2.11.12b).$$
El SH transmitido = onda homogénea ($\mathbf k_T$) + onda inhomogénea ($\mathbf k_s$), con
$$\mathbf k_s-\mathbf k_T=\Delta k\,\hat z=(\omega_s/c)[\epsilon_s^{1/2}\cos\theta_s-\epsilon_T^{1/2}(\omega_s)\cos\theta_T]\hat z\quad(2.11.13).$$
Entonces (p. 127)
$$E_\perp^T=\Big[A_\perp^R+\frac{\mu_0(\omega_s/c)^2p_\perp}{2k_T(\omega_s)}\Big(\frac{e^{i\Delta kz}-1}{\Delta k}\Big)\Big]e^{i\mathbf k_T(\omega_s)\cdot\mathbf r}\equiv A_\perp^Te^{i\mathbf k_T(\omega_s)\cdot\mathbf r}\quad(2.11.14):$$
onda plana de amplitud variable; la variación (ajuste de fase imperfecto) es la **interferencia de las
soluciones homogénea e inhomogénea** de la ecuación forzada. Con $\Delta kz\ll1$, a primer orden:
$$A_\perp^T=A_\perp^R+\frac{(\omega/c)^2p_\perp(iz)}{2\epsilon_0c^2k_T(\omega_s)}=A_\perp^R+\frac{i(\omega/c)p_\perp z}{2\epsilon_0c^2\epsilon^{1/2}(\omega_s)}\quad(2.11.15):$$
crece linealmente desde el valor de frontera $A_\perp^R$, que por (2.11.12a) vale en orden de magnitud
$$A_\perp^R\simeq-\frac{p_\perp}{4\epsilon_0c^2\epsilon}\quad(2.11.16),\qquad A_\perp^T\simeq-\frac{\pi p_\perp}{4\epsilon_0c^2\epsilon}[1-2ik_T(\omega_s)z]\quad(2.11.17)\ \text{[ver erratas]},$$
($\epsilon$ = valor característico cerca de la interfaz). El término de superficie equivale al de volumen para un
espesor
$$t=\lambda/4\pi\quad(2.11.18).$$
**Caso (b), interfaz entre centrosimétricos** (p. 127–128): un tratamiento exacto exigiría las propiedades
moleculares de la interfaz (se deducen propiedades macroscópicas de las microscópicas, no al revés).
Estimado: $\chi^{(2)}$ típico de un no centrosimétrico confinado a un espesor molecular $a_0$; con (2.11.18):
$$A_\perp^T(\text{centrosim.})=\frac{4\pi a_0}{\lambda}A_\perp^T(\text{no centrosim.})\simeq10^{-3}A_\perp^T(\text{no centrosim.})\quad(2.11.19),$$
en acuerdo con modelos detallados (Mizrahi y Sipe 1988).

---

## Tablas y datos numéricos útiles

**Fórmulas clave (SI, convención de Boyd):**

| Proceso | Resultado | Ec. |
|---|---|---|
| SFG, bombas no agotadas | $I_3=\dfrac{8d_{\rm eff}^2\omega_3^2I_1I_2}{n_1n_2n_3\epsilon_0c^2}L^2\,\mathrm{sinc}^2(\Delta kL/2)$ | (2.2.19) |
| Longitud de coherencia | $L_{\rm coh}=2/\Delta k$ | (2.2.20) |
| QPM 1.er orden | $d_Q=(2/\pi)d_{\rm eff}$, $\Lambda=2L_{\rm coh}=2\pi/(k_1+k_2-k_3)$ | (2.4.7)–(2.4.8) |
| QPM orden $m$ | $G_m=(2/m\pi)\sin(m\pi/2)$ | (2.4.3) |
| Manley–Rowe | $\frac{d}{dz}(I_1/\omega_1)=\frac{d}{dz}(I_2/\omega_2)=-\frac{d}{dz}(I_3/\omega_3)$ | (2.5.6) |
| SFG bomba fuerte | $\lvert A_3\rvert^2=\lvert A_1(0)\rvert^2\frac{\lvert K_3\rvert^2}{g^2}\sin^2gz$, $g=\sqrt{\kappa^2+\Delta k^2/4}$ | (2.6.25), (2.6.19) |
| SHG con agotamiento, $\Delta k=0$ | $u_2=\tanh(z/l)$, $u_1=\mathrm{sech}(z/l)$, $l=\frac{(n_1n_2)^{1/2}c}{2\omega_1d_{\rm eff}\lvert A_1(0)\rvert}$ | (2.7.36)–(2.7.38) |
| DFG/OPA, $\Delta k=0$ | $A_1=A_1(0)\cosh\kappa z$, $A_2\propto A_1^*(0)\sinh\kappa z$ | (2.8.7)–(2.8.8) |
| Umbral OPO | general $\cosh gL=1+\frac{l_1l_2}{2-l_1-l_2}$; DRO $g^2L^2=l_1l_2$; SRO $g^2L^2=2l_1$ | (2.9.8)–(2.9.10) |
| Haz gaussiano | $b=kw_0^2=2\pi w_0^2/\lambda$, $\mathcal P=n\epsilon_0c\pi w_0^2\lvert\mathcal A\rvert^2$ | (2.10.5c), (2.10.6) |
| Boyd–Kleinman SHG | $L/b=2.84$, $\Delta k=3.2/L$, $K=1.068$ (gaussiano) | (2.10.14) |
| SH superficial | $t=\lambda/4\pi$; centrosim./no centrosim. $\approx4\pi a_0/\lambda\approx10^{-3}$ | (2.11.18)–(2.11.19) |

**Datos numéricos del texto:**

- $\epsilon_0=8.85\times10^{-12}$ F/m (p. 72).
- $L_{\rm coh}=3.4\ \mu$m para SHG de 1.06 μm en LiNbO$_3$ (p. 88).
- Campo de poling periódico de LiNbO$_3$: ~21 kV/mm (p. 88).
- SHG CW: $d_{\rm eff}=4\times10^{-12}$ m/V, $L=1$ cm, $P=1$ W, $\lambda=0.5\ \mu$m, $n=2$ ⇒ $\zeta=0.14$, $\eta\approx2$ % (p. 103–104).
- OPO: $L_c=15$ cm ⇒ $\Delta\nu_c=1$ GHz; $\mathcal F=100$ ⇒ ancho de modo 10 MHz; ancho de ganancia ~100 GHz con $dn/d\nu\sim10^{-15}$ s (p. 112).
- OPO de BBO: sintonía 0.42–2.3 μm, eficiencia hasta 32 % (p. 115).
- Microscopía: 50 nm (Gustafsson 2005), 16 nm = λ/50 (STED, Westphal y Hell 2005) (p. 105).
- Tabla 2.3.1 (clasificación óptica de sistemas cristalinos) y Tabla 2.3.2 (condiciones tipo I/II): ver §2.3.

---

## Problemas al final del capítulo (p. 128–132)

1. *Infrared upconversion.* Una forma de detectar IR es convertirlo al visible por SFG. Radiación IR de
   frecuencia $\omega_1$ se mezcla con un láser intenso de frecuencia $\omega_2$ para formar la señal convertida en
   $\omega_3=\omega_1+\omega_2$. Derivar una fórmula de cómo la eficiencia cuántica de conversión de fotones IR a fotones
   visibles depende de la longitud $L$ y del coeficiente $d_{\rm eff}$ del cristal y del desajuste $\Delta k$. Estimar
   numéricamente la eficiencia cuántica para conversión de IR de 10 μm con un cristal de proustita de 1 cm,
   1 W de láser a 0.65 μm, ajuste de fase perfecto y enfoque óptimo. [Resp.: $\eta_Q=2\%$.]
2. *Sum-frequency generation.* Resolver las ecuaciones acopladas de SFG (2.2.10)–(2.2.12b) con $\Delta k=0$ pero sin
   la aproximación de §2.6 de que la amplitud de $\omega_2$ es constante. [Pista: muy difícil; ver Armstrong et
   al. (1962).]
3. *Systems of units.* Reescribir cada ecuación destacada de las secciones 2.1 a 2.5 en el sistema gaussiano.
4. *Difference-frequency generation.* Resolver las ecuaciones de DFG en el límite de bomba constante y
   verificar las Ecs. (2.9.2). Suponer $\omega_1+\omega_2=\omega_3$, $A_3$ constante, medio sin pérdidas, $\Delta k$ arbitrario y, en
   general, señal de entrada en las tres frecuencias. Interpretar con esbozos de casos representativos y casos
   límite (ajuste perfecto, solo dos campos de entrada).
5. *Second-harmonic generation.* Verificar que (2.7.29) tiene soluciones del tipo de la Fig. 2.7.2.
6. *Second-harmonic generation.* Resolver las ecuaciones acopladas de SHG con $A_2=0$ y $A_1$ arbitrario en $z=0$ y
   $\Delta k$ arbitrario. Esbozar $|A(2\omega)|^2$ vs. $z$ para varios $\Delta k$ y verificar los resultados de la Fig. 2.7.2.
7. *Mode structure of an optical cavity.* Verificar (2.9.11). [Resp. (del libro): con $n(\nu)$, un número entero
   $m$ de medias longitudes de onda cabe en $L_c$: $m\lambda/2=L_c$, y con $\lambda=c/n\nu$, $n\nu=cm/2L_c$. Entre modos adyacentes
   $\Delta(n\nu)=n\Delta\nu+\nu\Delta n=[n+\nu(dn/d\nu)]\Delta\nu$ y $\Delta(cm/2L_c)=c/2L_c$, así que
   $\Delta\nu=\frac{c}{2L_c(n+\nu\,dn/d\nu)}=\frac{v_g}{2L_c}=\frac{c}{2n_gL_c}$, con $v_g=c/[n+\nu(dn/d\nu)]$ y $n_g=n+\nu(dn/d\nu)$.]
8. *Mode structure of an optical cavity.* Generalizar el anterior a una cavidad de longitud $L$ con el medio
   material de longitud $L_c<L$.
9. *Quasi-phase-matching.* Generalizar la discusión de (2.4.1) a (2.4.6) permitiendo longitudes distintas de
   secciones invertidas y no invertidas: período $\Lambda$, longitud invertida $l$. Mostrar cómo se modifica cada
   ecuación y comentar el cambio en $d_Q$ y en la condición de QPM.
10. *Gaussian laser beams.* Verificar que (2.10.4a) y (2.10.5a) son descripciones equivalentes de un haz
    gaussiano y que satisfacen la ecuación paraxial (2.10.3).
11. *Gaussian laser beams.* Verificar que la prueba (2.10.9) satisface la ecuación paraxial en la forma (2.10.7)
    si $\mathcal A_q(z)$ satisface la EDO (2.10.10).
12. *Phase matching with focused beams.* Evaluar la integral de (2.10.13a) y verificar (2.10.13b).
13. *Third-harmonic generation.* Con ajuste de fase perfecto, derivar y resolver exactamente las ecuaciones
    acopladas de THG en un material sin pérdidas, incluyendo los procesos descritos por $\chi^{(3)}(3\omega;\omega,\omega,\omega)$ y
    $\chi^{(3)}(\omega;3\omega,-\omega,-\omega)$. Calcular la intensidad del tercer armónico en función de la longitud de interacción:
    (a) en el límite de bomba no agotada; (b) en el caso general en que la intensidad de bomba no es constante.
14. *Poynting's theorem.* Derivar el teorema de Poynting para un material no lineal con $\tilde{\mathbf D}=\epsilon_0\tilde{\mathbf E}+\tilde{\mathbf P}$,
    $\tilde{\mathbf P}=\epsilon_0[\chi^{(1)}\tilde{\mathbf E}+\chi^{(2)}\tilde{\mathbf E}^2+\chi^{(3)}\tilde{\mathbf E}^3]$, no magnético ($\tilde{\mathbf B}=\mu_0\tilde{\mathbf H}$).
15. *Backward second-harmonic generation.* La Fig. 2.1.1c implica que la SHG se radia hacia adelante pero no
    apreciablemente hacia atrás. Verificarlo derivando la ecuación de amplitud acoplada para un SH que se
    propaga hacia atrás y mostrar que su amplitud nunca se vuelve apreciable. (Un cálculo más riguroso con la
    misma conclusión está en §2.11.)
16. *Second-harmonic generation.* SHG con $\Delta k=0$ y $\Delta k\neq0$ en material sin pérdidas. Dar las condiciones bajo las
    que: (i) fundamental y armónico intercambian energía periódicamente; (ii) el SH adquiere asintóticamente toda
    la energía; (iii) el fundamental adquiere asintóticamente toda la energía; (iv) parte de la energía está en
    cada componente y esa fracción no varía con $z$.
17. *Manley–Rowe relations.* Derivar las relaciones de Manley–Rowe para SHG, de forma análoga a §2.5 para SFG.
18. *Phase-matching requirements.* Explicar por qué procesos como la SHG solo son eficientes si $\Delta k=0$, mientras
    que no hay tal requisito para la absorción de dos fotones.
19. *Elementary treatment of second-harmonic generation.* Como alternativa más simple al tratamiento del texto,
    seguir la sugerencia tras (2.7.12): resolver (2.7.11) en el límite de bomba no agotada y expresar la
    intensidad generada en función de la intensidad del fundamental, la longitud $L$ y $\Delta k$.
20. *Cascaded optical nonlinearities.* Por propagación, una no linealidad de segundo orden puede imitar una de
    tercer orden. Calcular el desfase que adquiere una onda en un material de segundo orden en condiciones de
    SHG casi ajustada en fase y determinar cuándo el desfase del fundamental es aproximadamente proporcional al
    producto longitud × intensidad. Partiendo de (2.7.10) y (2.7.11), eliminar $A_2$ para obtener
    $$\frac{d^2A_1}{dz^2}+i\Delta k\frac{dA_1}{dz}-\Gamma^2(1-2|A_1/A_0|^2)A_1=0,$$
    con $\Gamma$ constante (dar su expresión) y $A_0$ el valor incidente del fundamental. Mostrar que, bajo condiciones
    adecuadas (especificarlas), la solución es una onda cuya fase crece linealmente con $L$ y con la intensidad $I$.
21. *Optimum focusing and second-harmonic generation.* Explicar por qué con enfoque óptimo la potencia de SH
    escala linealmente, y no cuadráticamente, con la longitud $L$ del cristal (ver (2.10.14)).
22. *Harmonic generation with focused gaussian beams.* Desarrollar una comprensión conceptual de por qué la
    intensidad del armónico generado se anula cuando el factor $\Delta kL$ es negativo o cero (ver Fig. 2.10.2).

**Referencias más importantes (p. 132–133):** Armstrong, Bloembergen, Ducuing, Pershan, *Phys. Rev.* **127**, 1918
(1962); Maker et al., *PRL* **8**, 21 (1962); Manley y Rowe, *Proc. IRE* **47**, 2115 (1959); Midwinter y Warner,
*Brit. J. Appl. Phys.* **16**, 1135 (1965); Hobden y Warner, *Phys. Lett.* **22**, 243 (1966); Boyd y Townes, *APL*
**31**, 440 (1977); Byer y Herbst (1977) en Shen (ed.), *Tunable Infrared Generation*; QPM: Fejer, Magel, Jundt,
Byer, *IEEE JQE* **28**, 2631 (1992); Yamada et al., *APL* **62**, 435 (1993); Byer, *J. Nonlinear Opt. Phys. Mater.*
**6**, 549 (1997); OPO: Giordmaine y Miller, *PRL* **14**, 973 (1965); Smith et al., *APL* **12**, 308 (1968); Bosenberg et
al., *APL* **55**, 1952 (1989); Bosenberg y Tang, *APL* **56**, 1819 (1990); Myers et al., *JOSA B* **12**, 2102 (1995);
haces enfocados: Boyd y Kleinman, *J. Appl. Phys.* **39**, 3597 (1968); Kleinman, Ashkin, Boyd, *Phys. Rev.* **145**,
338 (1966); Kogelnik y Li, *Appl. Opt.* **5**, 1550 (1966); Ward y New, *Phys. Rev.* **185**, 57 (1969); Bjorklund, *IEEE
JQE* **11**, 287 (1975); Gouy, *C. R. Acad. Sci. Paris* **110**, 1251 (1890); interfaz: Bloembergen y Pershan, *Phys.
Rev.* **128**, 602 (1962); Shen, *The Principles of Nonlinear Optics* (1984), §6.4; Mizrahi y Sipe, *JOSA B* **5**, 660
(1988).

---

## Relación con Óptica No Lineal

- **Curso:** este capítulo es el **tema 5** del programa (ecuación de onda para medios no lineales y procesos de
  segundo orden). Usa directamente el tema 4 (Boyd cap. 1): $P_3=4\epsilon_0d_{\rm eff}E_1E_2$ (1.5.28),
  $P(2\omega)=2\epsilon_0d_{\rm eff}E^2$ (1.5.29), $d_{\rm eff}$ y la simetría de permutación completa (1.5.8), que es la que
  garantiza un mismo $d_{\rm eff}$ en las tres ecuaciones acopladas y, con ello, Manley–Rowe. Es la versión SI con
  $e^{-i\omega t}$ de lo que el Saleh trata en §21.2, 21.4–21.5 (ver `notas/saleh/cap21-optica-no-lineal.md`;
  atención: el Saleh usa amplitudes de pico con $e^{j\omega t}$, $I=|E|^2/2\eta$ y otra definición de longitud de
  coherencia). Las ecuaciones (2.2.10)–(2.2.12), (2.2.19), (2.3.11), (2.4.7)–(2.4.8), (2.7.36)–(2.7.38) y
  (2.9.8)–(2.9.10) son las de uso más frecuente en talleres.
- **Proyecto final (supercontinuo / no linealidades en guías de SiN y Si):** el SiN amorfo y el Si cristalino
  son (casi) centrosimétricos, así que los procesos $\chi^{(2)}$ de volumen de este capítulo no dominan; lo
  relevante para el SC es $\chi^{(3)}$ (caps. 4 y 7). Sin embargo, el capítulo aporta herramientas que se usan tal
  cual: (i) la deducción de la ecuación de onda forzada y de la SVEA (2.1–2.2), que en guías se generaliza a la
  ecuación de modos acoplados y a la NLSE; (ii) el concepto de $\Delta k$ y $\mathrm{sinc}^2(\Delta kL/2)$, que reaparece como
  ajuste de fase de la FWM y de la emisión de ondas dispersivas (radiación de Cherenkov) en el SC; (iii) la
  ecuación paraxial y la fase de Gouy (2.10) como análogo del término de difracción/dispersión; (iv) §2.11 y
  §2.7.1: la SHG de superficie/interfaz explica la SHG observada en guías de SiN (ruptura de simetría en
  interfaces y por tensiones o campos estáticos), un efecto que se menciona en la literatura de SC en SiN como
  fuente de componentes espectrales en el visible; (v) el índice de grupo $n_g=n+\nu\,dn/d\nu$ (2.9.11, Problema 7),
  necesario para FSR y dispersión de guías y resonadores.

---

## Erratas o dudas de lectura

1. **(2.7.19), p. 99:** se lee $l=\big(\frac{2n_1^2n_2}{\epsilon_0cI}\big)^{1/2}\frac{c}{2\omega_1d_{\rm eff}}$. Dimensionalmente y por consistencia
   con (2.7.13) y (2.7.38), debería ser $l=\big(\frac{2n_1^2n_2\,\epsilon_0c}{I}\big)^{1/2}\frac{c}{2\omega_1d_{\rm eff}}$ (con $I=2n_1\epsilon_0c|A_1(0)|^2$ esto
   reproduce exactamente (2.7.38)).
2. **(2.4.4a,b), p. 87:** el exponente se lee $e^{-i(\Delta k_Q-2k_m)z}$. Por consistencia con (2.4.4c) y con la
   afirmación de que las ecuaciones son "formalmente idénticas" a (2.2.10)–(2.2.12), debería ser $e^{-i\Delta k_Qz}$.
   Además (2.4.6) define $\Delta k_Q=k_1+k_2-k_3+k_m$ y (2.4.7) usa $-2\pi/\Lambda$ (corresponde a la componente $m=-1$, o a
   definir $\Delta k_Q$ con $-k_m$).
3. **p. 87:** "Because of the tendency for $d_Q$ to decrease with increasing values of $m$ (see Eq. (2.9.3))";
   por contenido la referencia debería ser (2.4.3)/(2.4.5); (2.9.3) define $g$ y $\kappa_i$ del OPO.
4. **p. 92 y p. 94:** "The solution to Eq. (2.4.1)…" y "Let us next solve Eqs. (2.4.1)…"; por contexto deben ser
   las Ecs. (2.6.1). (2.4.1) es la modulación $d(z)$ de QPM.
5. **(2.11.17), p. 127:** se lee $A_\perp^T\simeq-\frac{\pi p_\perp}{4\epsilon_0c^2\epsilon}[1-2ik_T(\omega_s)z]$. A partir de (2.11.15) y (2.11.16) se obtiene
   $-\frac{p_\perp}{4\epsilon_0c^2\epsilon}[1-2ik_Tz]$, sin el factor $\pi$ (probable resto de la versión gaussiana). No altera
   (2.11.18), que solo depende del corchete.
6. **p. 108 vs. p. 115:** en p. 108 dice "The first cw optical parametric oscillator was built by Giordmaine and
   Miller in 1965"; en p. 115 el OPO de Giordmaine y Miller (1965) es *pulsado* y el primer CW es de Smith et
   al. (1968). Debería decir "the first optical parametric oscillator".
7. **(2.9.13) vs. (2.9.15)–(2.9.16):** el orden de la resta de índices de grupo cambia
   ($n_i^{(g)}-n_s^{(g)}$ vs. $n_s^{(g)}-n_i^{(g)}$); solo importa en valor absoluto. Notación inconsistente en (2.9.18):
   $\delta\omega^{(\rm osc)}$ y $N_{\rm OPO}$ frente a $\delta\omega^{(\rm OPO)}$ y $N_{\rm osc}$ del texto, y $n_g^{(s)}$ frente a $n_s^{(g)}$.
8. **(2.5.3a), p. 89, primera línea:** se lee $2n_i\epsilon_0c$; para la onda 1 debería ser $2n_1\epsilon_0c$ (el resultado final es
   correcto).
9. **(2.11.5), p. 124:** se define $k_s=\sqrt{\epsilon(\omega_s)}\,\omega_s/c$, pero en (2.11.9) se introduce la constante ficticia
   $\epsilon_s$ con $k_s=\epsilon_s^{1/2}\omega_s/c$; la segunda es la definición coherente con el resto (en general $k_s=2k_T(\omega_i)$).
10. **p. 74, tras (2.1.22):** "This expression, along with Eqs. (2.1.17) and (2.1.18)"; probablemente debería decir
    (2.1.18) y (2.1.19). Problema 19 dice "undeplated" (errata tipográfica por *undepleted*).
11. **Nota de unidades:** (2.10.14) con $128\pi^2$ y $K=1.068$ está en el sistema gaussiano del trabajo original;
    no debe evaluarse en SI sin convertir (el texto lo advierte).
12. (2.6.23), (2.9.4b), (2.10.10) y la frase con $L/b=2.84$ salen tenues en el escaneo; se verificaron a 200 dpi.
