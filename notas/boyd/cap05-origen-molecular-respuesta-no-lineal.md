# Capítulo 5 — Molecular Origin of the Nonlinear Optical Response (Boyd, 3.ª ed.)

Páginas del libro 253–275 (PDF 271–293; la p. 276 / PDF 294 está en blanco). Leído el 2026-11-14.

Fuente: R. W. Boyd, *Nonlinear Optics*, 3.ª ed., Academic Press/Elsevier, 2008, cap. 5.
Las citas de página son páginas del libro (sumar 18 para la página del PDF).

Convención de Boyd (SI): $\tilde E(t)=Ee^{-i\omega t}+\text{c.c.}$, $\tilde P=\epsilon_0[\chi^{(1)}\tilde E+\chi^{(2)}\tilde E^2+\chi^{(3)}\tilde E^3+\dots]$, $I=2n\epsilon_0c|E|^2$.
**Ojo:** buena parte del capítulo escribe polarizabilidades e hiperpolarizabilidades en estilo gaussiano
($\chi^{(1)}=N\alpha$ sin $\epsilon_0$, $\alpha=\tfrac92a_0^3$, $\gamma$ en esu, ecuaciones de cristal líquido "en unidades gaussianas como en
Khoo"); se indica donde aplica.

Estructura: 5.1 Susceptibilidades por teoría de perturbaciones independiente del tiempo (5.1.1 átomo de
hidrógeno, 5.1.2 expresión general en el límite cuasiestático) · 5.2 Modelos semiempíricos (Miller
generalizado, Wang, modelo de Boling–Glass–Owyoung) · 5.3 Polímeros conjugados · 5.4 Modelo de carga de
enlace (bond‑charge) · 5.5 Óptica no lineal de medios quirales · 5.6 Cristales líquidos · Problemas (3) ·
Referencias.

---

## Resumen del capítulo

Las expresiones cuánticas completas del cap. 3 (teoría de perturbaciones dependiente del tiempo) son
demasiado complicadas para cálculos prácticos; el capítulo presenta enfoques más simples, basados en la
respuesta a nivel molecular. En el límite muy no resonante ($\omega\ll\omega_0$) el campo es cuasiestático y las
susceptibilidades se obtienen derivando la energía de polarización $W(\tilde E)$: $\chi^{(n-1)}=-nW^{(n)}/(\epsilon_0\tilde E^n)$. Para el
hidrógeno, el efecto Stark da $\alpha=\tfrac92a_0^3$ y $\gamma=\tfrac{3555}{16}a_0^7/e^6$ (así impreso; por consistencia gaussiana debería ser $e^2$, ver erratas), consistentes con las leyes de escala
$\alpha\simeq V$ y $\gamma\propto V^{7/3}$. En general, con la teoría de perturbaciones estacionaria se obtienen fórmulas
estáticas de $\alpha$, $\beta$, $\gamma$ como sumas sobre estados; con la aproximación de Unsöld (una sola frecuencia
media $\omega_0$) y la clausura, $\alpha\propto\langle x^2\rangle$, $\beta\propto-\langle x^3\rangle$, $\gamma\propto\langle x^4\rangle-2\langle x^2\rangle^2$ (momentos de la distribución electrónica;
$\gamma=\alpha^2g/\hbar\omega_0$ con $g$ la curtosis) y, usando la regla de suma de Thomas–Reiche–Kuhn, $\alpha\sim L^4$, $\beta\sim L^7$, $\gamma\sim L^{10}$:
las no linealidades crecen muy rápido con el tamaño molecular. Los modelos semiempíricos (Miller
generalizado a tercer orden, Wang $\chi^{(3)}=Q'(\chi^{(1)})^2$, y el modelo de Boling, Glass y Owyoung) predicen $n_2$ a
partir de propiedades lineales (índice y su dispersión), con $(gf)\approx3$ empírico. Los polímeros conjugados
(electrones $\pi$ deslocalizados) dan $\chi^{(3)}$ enormes; el modelo de pozo cuadrado 1D da $\gamma\propto L^5$, confirmado
experimentalmente. El modelo de carga de enlace asigna polarizabilidades a cada enlace (Phillips–Van
Vechten–Levine) y predice $\chi^{(3)}$ de Ge, Si y GaAs con ≈30% de exactitud. Los medios quirales isótropos
carecen de centro de inversión y permiten SFG/DFG (no SHG) sólo con haces no colineales,
$\mathbf P=\epsilon_0A_{123}\mathbf E\times\mathbf F$. Los cristales líquidos muestran no linealidades orientacionales enormes y lentas
(fase isótropa: $n_2\propto1/(T-T^*)$; fase nemática: hasta $10^9$ veces el CS₂).

---

## Secciones

### Introducción (p. 253)

El cap. 3 dio una teoría cuántica general (perturbaciones dependientes del tiempo) con la dependencia
completa en frecuencia de las susceptibilidades, pero demasiado compleja para cálculos prácticos. Este
capítulo revisa enfoques más simples, muchos basados en las propiedades ópticas a nivel molecular, y
describe brevemente polímeros conjugados, moléculas quirales y cristales líquidos.

### 5.1 Nonlinear Susceptibilities Calculated Using Time-Independent Perturbation Theory (p. 253)

Teoría de perturbaciones independiente del tiempo (Jha y Bloembergen, 1968; Ducuing, 1977): más fácil de
implementar; justificada porque a menudo interesa el límite muy no resonante $\omega\ll\omega_0$ (para evitar pérdidas
por absorción), donde el campo es cuasiestático (p. 254).

Polarización (con la convención de que la tilde se mantiene también para campos cuasiestáticos o
estáticos):
$$\tilde P=\epsilon_0\chi^{(1)}\tilde E+\epsilon_0\chi^{(2)}\tilde E^2+\epsilon_0\chi^{(3)}\tilde E^3+\cdots \qquad (5.1.1)$$
Energía almacenada al polarizar el medio:
$$W=-\int_0^{\tilde E}\tilde P(\tilde E')d\tilde E'=-\frac12\chi^{(1)}\tilde E^2-\frac13\chi^{(2)}\tilde E^3-\frac14\chi^{(3)}\tilde E^3\cdots\equiv W^{(2)}+W^{(3)}+W^{(4)}+\cdots \qquad (5.1.2)$$

> **Errata (5.1.2), p. 254:** se lee "$-\tfrac14\chi^{(3)}\tilde E^3$" y faltan los $\epsilon_0$. Integrando (5.1.1) debería ser
> $W=-\tfrac12\epsilon_0\chi^{(1)}\tilde E^2-\tfrac13\epsilon_0\chi^{(2)}\tilde E^3-\tfrac14\epsilon_0\chi^{(3)}\tilde E^4-\cdots$ (consistente con (5.1.3), que sí lleva $\epsilon_0$).

Si se conoce $W(\tilde E)$ (por cálculo o, p. ej., por medidas de efecto Stark):
$$\chi^{(n-1)}=-\frac{nW^{(n)}}{\epsilon_0\tilde E^n} \qquad (5.1.3)$$
y más generalmente, aun sin la serie,
$$\chi^{(n-1)}=\frac{-1}{\epsilon_0(n-1)!}\frac{\partial^nW}{\partial\tilde E^n}\bigg|_{E=0} \qquad (5.1.4)$$

> **Duda de lectura (5.1.4):** con $W^{(n)}=-\tfrac1n\epsilon_0\chi^{(n-1)}\tilde E^n$ se obtiene $\partial^nW/\partial\tilde E^n=-(n-1)!\,\epsilon_0\chi^{(n-1)}$, que concuerda con
> $(n-1)!$ en el denominador. ✓ (Se deja constancia de que es coherente con (5.1.3).)

Nota al pie (p. 254): para campos variables en el tiempo (5.1.3) sigue valiendo con $W^{(n)}$ y $\tilde E^n$ reemplazados
por sus promedios temporales $\langle W^{(n)}\rangle$, $\langle\tilde E^n\rangle$. Para $\tilde E=Ee^{-i\omega t}+$c.c. $=2E\cos(\omega t+\phi)$: $\tilde E^n=2^nE^n\cos^n(\omega t+\phi)$,
$\langle\tilde E^n\rangle=2^nE^n\langle\cos^n(\omega t+\phi)\rangle$, con $\langle\cos^2\rangle=1/2$ y $\langle\cos^4\rangle=3/8$.

#### 5.1.1 Hydrogen Atom (p. 254)

Por consideraciones de efecto Stark se conoce la energía del fundamental en función de $E$ (Schiff, 1968;
Sewell, 1949); el cálculo usa simetrías especiales del hidrógeno y no se generaliza (p. 255):
$$\frac{w}{2R}=-\frac12-\frac94\Big(\frac{E}{E_{\rm at}}\Big)^2-\frac{3555}{64}\Big(\frac{E}{E_{\rm at}}\Big)^4+\cdots \qquad (5.1.5)$$
con $R=13.6$ eV (Rydberg) y $E_{\rm at}=e/4\pi\epsilon_0a_0^2=m^2e^5/(4\pi\epsilon_0)^3\hbar^4=5.14\times10^{11}$ V/m (unidad atómica de campo). Con
$W=Nw$ ($N$ densidad de átomos) en (5.1.3):
$$\chi^{(1)}=N\alpha,\qquad\alpha=\frac92a_0^3 \qquad (5.1.6a)$$
$$\chi^{(3)}=N\gamma,\qquad\gamma=\frac{3555}{16}\frac{a_0^7}{e^6} \qquad (5.1.6b)$$
$a_0=4\pi\epsilon_0\hbar^2/me^2$. Leyes de escala para polarizabilidades no resonantes:
$$\alpha\simeq\text{volumen atómico }V \qquad (5.1.7a)$$
$$\gamma\propto V^{7/3} \qquad (5.1.7b)$$

> **Erratas (p. 255):** (i) se lee "$R=e^2\hbar^2/4\pi\epsilon_0mc^2=13.6$ eV", dimensionalmente incorrecto; debería ser
> $R=e^2/(8\pi\epsilon_0a_0)=me^4/[2(4\pi\epsilon_0)^2\hbar^2]=13.6$ eV (la misma $E_0$ que el libro escribe bien en la p. 266).
> (ii) En (5.1.6b) se lee $a_0^7/e^6$; en el sistema gaussiano en que está escrita (5.1.6a) ($2R=e^2/a_0$, $E_{\rm at}=e/a_0^2$), la
> derivación da $W^{(4)}=-\tfrac{3555}{64}\tfrac{a_0^7}{e^2}E^4$ y $\gamma=-4W^{(4)}/E^4=\tfrac{3555}{16}a_0^7/e^2$. Por consistencia dimensional ($\gamma E^4$ = energía,
> $\alpha=\tfrac92a_0^3$ ✓ con la misma derivación) debería ser $e^2$, no $e^6$. (iii) Las fórmulas (5.1.6) son gaussianas: en SI
> faltaría $4\pi\epsilon_0$ y un $\epsilon_0$ en $\chi=N\alpha/\epsilon_0$.

#### 5.1.2 General Expression for the Nonlinear Susceptibility in the Quasi-Static Limit (p. 255)

$$\hat H=\hat H_0+\hat V \qquad (5.1.8)$$
$\hat H_0$ = átomo libre; $\hat V$ = perturbación cuasiestática:
$$\hat V=-\hat\mu\tilde E \qquad (5.1.9)$$
$\hat\mu=-e\hat x$ (operador dipolo). Ecuación de Schrödinger estacionaria:
$$\hat H|\psi_n\rangle=w_n|\psi_n\rangle \qquad (5.1.10)$$
Series perturbativas (p. 256):
$$w_n=w_n^{(0)}+w_n^{(1)}+w_n^{(2)}+\cdots \qquad (5.1.11a)$$
$$|\psi_n\rangle=|\psi_n^{(0)}\rangle+|\psi_n^{(1)}\rangle+|\psi_n^{(2)}\rangle+\cdots \qquad (5.1.11b)$$
(procedimiento detallado en Dalgarno, 1961). Energías:
$$w_n^{(1)}=e\tilde E\langle n|x|n\rangle \qquad (5.1.12a)$$
$$w_n^{(2)}=e^2\tilde E^2\sum_s{}'\frac{\langle n|x|s\rangle\langle s|x|n\rangle}{w_s^{(0)}-w_n^{(0)}} \qquad (5.1.12b)$$
$$w_n^{(3)}=e^3\tilde E^3\sum_{st}{}'\frac{\langle n|x|s\rangle\langle s|x|t\rangle\langle t|x|n\rangle}{(w_s^{(0)}-w_n^{(0)})(w_t^{(0)}-w_n^{(0)})} \qquad (5.1.12c)$$
$$w_n^{(4)}=e^4\tilde E^4\sum_{stu}{}'\frac{\langle n|x|s\rangle\langle s|x|t\rangle\langle t|x|u\rangle\langle u|x|n\rangle}{(w_s^{(0)}-w_n^{(0)})(w_t^{(0)}-w_n^{(0)})(w_u^{(0)}-w_n^{(0)})}-e^2\tilde E^2w_n^{(2)}\sum_u{}'\frac{\langle n|x|u\rangle\langle u|x|n\rangle}{(w_u^{(0)}-w_n^{(0)})^2} \qquad (5.1.12d)$$
(prima: se omite el estado $n$).

> **Nota sobre signos (5.1.12b):** la corrección de 2.º orden del fundamental es negativa; con
> $w_s^{(0)}-w_n^{(0)}>0$ en el denominador el término escrito sería positivo para $n=g$. La forma estándar es
> $\sum'|V_{ns}|^2/(w_n^{(0)}-w_s^{(0)})$. Se transcribe tal cual se lee; el signo correcto se recupera en (5.1.13) vía (5.1.3).

Con $W=Nw$, estado fundamental $g$ y (5.1.3) (p. 256):
$$\chi^{(1)}=N\alpha,\qquad\alpha=\alpha_{xx}=\frac{2e^2}{\hbar}\sum_{s\neq g}\frac{x_{gs}x_{sg}}{\omega_{sg}} \qquad (5.1.13a)$$
$$\chi^{(2)}=N\beta,\qquad\beta=\beta_{xxx}=\frac{3e^3}{\hbar^2}\sum_{s,t\neq g}\frac{x_{gt}x_{ts}x_{sg}}{\omega_{tg}\omega_{sg}} \qquad (5.1.13b)$$
$$\chi^{(3)}=N\gamma,\qquad\gamma=\gamma_{xxxx}=\frac{4e^4}{\hbar^3}\Bigg(\sum_{s,t,u\neq g}\frac{x_{gu}x_{ut}x_{ts}x_{sg}}{\omega_{ug}\omega_{tg}\omega_{sg}}-\sum_{s,t\neq g}\frac{x_{gt}x_{tg}x_{gs}x_{sg}}{\omega_{tg}\omega_{sg}^2}\Bigg) \qquad (5.1.13c)$$
con $\hbar\omega_{sg}=w_s^{(0)}-w_g^{(0)}$. $\chi^{(3)}$ se descompone en dos términos (Fig. 5.1.1, p. 257): (a) $g\to s\to t$ (dos
fotones arriba) y bajada por $u$; (b) $g\to s\to g$ y $g\to t\to g$. Totalmente consistente con el modelo dependiente
del tiempo (4.3.12) pero más simple de obtener. (Estilo gaussiano: $\chi=N\alpha$ sin $\epsilon_0$.)

Las (5.1.13) son las predicciones cuánticas de los valores **estáticos**; aún requieren todas las
frecuencias de resonancia y momentos dipolares conectados al fundamental.

**Aproximación de Unsöld:** reemplazar cada frecuencia de resonancia ($\omega_{sg}$…) por una frecuencia media $\omega_0$:
$$\alpha=\frac{2e^2}{\hbar\omega_0}\sum_s{}'\langle g|x|s\rangle\langle s|x|g\rangle \qquad (5.1.14)$$
$$\alpha=\frac{2e^2}{\hbar\omega_0}\langle g|x\hat Ox|g\rangle,\qquad\hat O=\sum_s{}'|s\rangle\langle s| \qquad (5.1.15)$$
Se reemplaza $\hat O$ por la suma sin restricción
$$\hat O=\sum_s|s\rangle\langle s| \qquad (5.1.16)$$
(justificado porque para estados de paridad definida $\langle g|x|g\rangle=0$, así que da igual incluir $g$), y por clausura
$$\sum_s|s\rangle\langle s|=1 \qquad (5.1.17)$$
se obtiene (p. 258):
$$\alpha=\frac{2e^2}{\hbar\omega_0}\langle x^2\rangle \qquad (5.1.18a)$$
(proporcional al momento cuadrupolar eléctrico de la distribución electrónica del fundamental). Análogamente:
$$\beta=-\frac{3e^3}{\hbar^2\omega_0^2}\langle x^3\rangle \qquad (5.1.18b)$$
$$\gamma=\frac{4e^4}{\hbar^3\omega_0^3}\big[\langle x^4\rangle-2\langle x^2\rangle^2\big] \qquad (5.1.18c)$$
Las hiperpolarizabilidades miden momentos de orden superior de la distribución electrónica y crecen
rápidamente con el tamaño de la nube. Combinando (5.1.18a) y (5.1.18c):
$$\gamma=\alpha^2\frac{g}{\hbar\omega_0},\qquad g=\Big[\frac{\langle x^4\rangle}{\langle x^2\rangle^2}-2\Big] \qquad (5.1.19)$$
$g$ = cantidad adimensional (la **curtosis** en estadística), cuarto momento normalizado.

Además $\omega_0$ se puede expresar con los momentos de $x$, mediante la regla de suma de
**Thomas–Reiche–Kuhn** (Bethe y Salpeter, 1977, ec. (61)):
$$\frac{2m}{\hbar}\sum_k\omega_{kg}|x_{kg}|^2=Z \qquad (5.1.20)$$
($Z$ = número de electrones ópticamente activos). Con $\omega_{kg}\to\omega_0$ y clausura:
$$\omega_0=\frac{Z\hbar}{2m\langle x^2\rangle} \qquad (5.1.21)$$
Sustituyendo en (5.1.18) (p. 259):
$$\alpha=\frac{4e^2m}{Z\hbar^2}\langle x^2\rangle^2 \qquad (5.1.22)$$
$$\beta=-\frac{12e^3m^2}{Z^2\hbar^4}\langle x^2\rangle^2\langle x^3\rangle \qquad (5.1.23)$$
$$\gamma=\frac{32e^4m^3}{Z^3\hbar^6}\langle x^2\rangle^3\big(\langle x^4\rangle-2\langle x^2\rangle^2\big) \qquad (5.1.24)$$
Leyes de escala con la dimensión característica $L$ de la molécula: $\alpha\sim L^4$, $\beta\sim L^7$, $\gamma\sim L^{10}$. Resultado
importante: los coeficientes no lineales crecen muy rápido con el tamaño molecular. $\alpha$ mide el momento
cuadrupolar, $\beta$ el octupolar y $\gamma$ depende del hexadecapolar ("hexadecimal pole" en el texto) y del
cuadrupolar. Nota al pie: hay una contribución adicional a $\beta$ por la diferencia de momento dipolar
permanente entre fundamental y excitado, no incluida en este modelo.

(Verificación: (5.1.22)–(5.1.24) se obtienen exactamente de (5.1.18) con (5.1.21). ✓)

### 5.2 Semiempirical Models of the Nonlinear Optical Susceptibility (p. 259)

La regla de Miller (§1.4) predice bien $\chi^{(2)}$; su generalización a tercer orden:
$$\chi^{(3)}(\omega_4,\omega_3,\omega_2,\omega_1)=A\chi^{(1)}(\omega_4)\chi^{(1)}(\omega_3)\chi^{(1)}(\omega_2)\chi^{(1)}(\omega_1) \qquad (5.2.1)$$
$\omega_4=\omega_1+\omega_2+\omega_3$, $A$ ≈ independiente de la frecuencia y casi igual para todos los materiales. Wynne (1969): válida
para ciertos materiales (cristales iónicos), no universal.

**Relación de Wang (1970)**, más general, en el límite cuasiestático:
$$\chi^{(3)}=Q'(\chi^{(1)})^2,\qquad Q'=g'/N_{\rm eff}\hbar\omega_0 \qquad (5.2.2)$$
$N_{\rm eff}=Nf$ (densidad molecular × fuerza de oscilador), $\omega_0$ frecuencia media, $g'$ adimensional ≈ 1, casi igual
para todos los materiales (p. 260). Empíricamente exacta tanto para gases a baja presión (donde Miller falla)
como para cristales iónicos (donde Miller funciona). Comparando con (5.1.19), $g'$ está íntimamente ligado a la
curtosis de la distribución electrónica; no parece haber argumento físico simple de por qué $g'$ sería
universal.

**Modelo de Boling, Glass y Owyoung (1978).** Predice $n_2$ a partir de propiedades lineales. Índice lineal por
Lorentz–Lorenz ((3.8.8a)) y oscilador de Lorentz ((1.4.17) o (3.5.25)):
$$\frac{n^2-1}{n^2+2}=\frac13N\alpha \qquad (5.2.3a)$$
$$\alpha=\frac{fe^2/m}{\omega_0^2-\omega^2} \qquad (5.2.3b)$$
($f$ = fuerza de oscilador de la transición dominante). Midiendo $n(\omega)$ se obtienen $\omega_0$ y $Nf$. Índice no lineal:
$$n_2=\frac{3}{4n^2\epsilon_0c}\chi^{(3)},\qquad\chi^{(3)}=L^4N\gamma,\qquad L=\frac{n^2+2}{3} \qquad (5.2.4a)$$
$$\gamma=\frac{g\alpha^2}{\hbar\omega_0} \qquad (5.2.4b)$$
((5.2.4b) es la forma microscópica de Wang, con $g$ parámetro libre). Despejando $\alpha$ de (5.2.3) e insertando:
$$\boxed{n_2=\frac{(n^2+2)^2(n^2-1)^2(gf)}{6n^2\epsilon_0c\hbar\omega_0(Nf)}} \qquad (5.2.5)$$
Predice $n_2$ con $n$, $\omega_0$ y $(Nf)$ (de la dispersión) y $(gf)$, constante para muchos materiales: **$(gf)=3$**
empíricamente (p. 261).

> **Verificación de (5.2.5):** de (5.2.3a), $N\alpha=3(n^2-1)/(n^2+2)$; $\chi^{(3)}=L^4Ng\alpha^2/\hbar\omega_0=\frac{(n^2+2)^4}{81}\frac{g}{N\hbar\omega_0}\frac{9(n^2-1)^2}{(n^2+2)^2}=\frac{(n^2+2)^2(n^2-1)^2g}{9N\hbar\omega_0}$;
> $n_2=\frac{3}{4n^2\epsilon_0c}\chi^{(3)}=\frac{(n^2+2)^2(n^2-1)^2g}{12n^2\epsilon_0c\hbar\omega_0N}$. Escribiendo $g/N=(gf)/(Nf)$ resulta un factor $1/12$, no $1/6$. La diferencia de
> factor 2 puede venir de la convención de $\chi^{(3)}$ vs $\gamma$ (no se aclara en el texto); se deja como duda (la
> fórmula además mezcla $\alpha$ gaussiano en (5.2.3a) con $\epsilon_0$ en (5.2.4a)).

**Fig. 5.2.1 (p. 261):** $n_2$ medido vs calculado con (5.2.5), en $10^{-13}$ esu (escala log 0.3–300), para
fluoruros (LiF, MgF₂, NaF, KF, CaF₂, SrF₂, BaF₂, CdF₂, LaF₃…), cloruros (NaCl, KCl, AgCl), bromuros (KBr, NaBr),
óxidos (SiO₂(o,e), Al₂O₃(o), CaCO₃, KDP, MgAl₂O₄, YAG, YAlO₃, CaWO₄, ZrO₂, ZnO, SrTiO₃, TiO₂, KTP, granates
GGG, GSGG, YGG, LLGG, GSAG, Y₂O₃, BeAl₂O₄, LAP) y sulfuros (ZnS, CdS); dos rectas teóricas para dos valores
de $(gf)$ (Adair *et al.*, 1989). Lenz *et al.* (2000): modelo relacionado con buen poder predictivo para vidrios
calcogenuros.

### 5.3 Nonlinear Optical Properties of Conjugated Polymers (p. 262)

Ciertos polímeros conjugados tienen respuesta extremadamente grande: el polidiacetileno PTS tiene
$\chi^{(3)}=3.5\times10^{-18}$ m²/V² frente a $2.7\times10^{-20}$ m²/V² del CS₂ (nótese que la Tabla 4.1.2 da $8.4\times10^{-18}$ y $3.1\times10^{-20}$).

Conjugado = enlaces simples y dobles (o simples y triples) alternados; saturado = sólo simples; polienos =
moléculas con muchos dobles enlaces. **Fig. 5.3.1 (p. 263):** (a) poliacetileno (C–C=C–C=…); (b) enlace simple
= enlace $\sigma$; (c) doble enlace = $\sigma$ + $\pi$ (solapamiento de dos orbitales $p$); (d) las dos representaciones con
simples y dobles intercambiados; (e) distribución de carga: electrones $\sigma$ localizados en el eje, $\pi$
deslocalizados a lo largo de la cadena. Los electrones $\pi$, menos ligados y lejos del eje de simetría,
responden más libremente → mayores respuestas lineal y no lineal. La cadena real es superposición de ambas
configuraciones.

Modelo: electrones $\pi$ libres en un pozo cuadrado 1D de longitud $L$ (la cadena). Rustagi y Ducuing (1974):
$$\alpha=\frac{8L^3}{3a_0\pi^2\mathcal N}\qquad\text{y}\qquad\gamma=\frac{256L^5}{45a_0^3e^2\pi^6\mathcal N^5} \qquad (5.3.1)$$
$\mathcal N$ = número de electrones por unidad de longitud, $a_0$ radio de Bohr (ver Problema 2). La respuesta lineal crece
rápido con $L$ y la no lineal aún más. En materia condensada el número de cadenas por volumen disminuye con
$L$, así que $\chi^{(1)}$ y $\chi^{(3)}$ crecen menos que $\alpha$ y $\gamma$ (p. 263–264).

> **Errata (p. 263):** se lee "will increase less rapidly with $L$ than do $\alpha$ and $\beta$ themselves"; por contexto
> ($\chi^{(1)}$, $\chi^{(3)}$, ec. (5.3.1)) debería ser "$\alpha$ and $\gamma$". Además el texto remite al "Problem 3" para (5.3.1),
> pero el problema del pozo cuadrado es el 2.

**Fig. 5.3.2 (p. 264):** $\gamma_{1111}$ medido (esu, $10^{-36}$–$10^{-31}$) vs número de dobles enlaces (1–20, log‑log), datos de
Hermann y Ducuing (1974); la recta tiene pendiente 5, según (5.3.1). Para pasar $\gamma$ a SI (m⁵/V²) multiplicar
por $1.4\times10^{-14}$.

### 5.4 Bond-Charge Model of Nonlinear Optical Properties (p. 264)

En átomos libres la base natural son los autoestados atómicos; en un cristal es más natural pensar los
electrones externos localizados en los enlaces (los de capa interna contribuyen de forma despreciable). Se
puede asignar polarizabilidad lineal y de orden superior a cada enlace (Levine, 1969; Chemla, 1971), poco
afectada por los enlaces vecinos (p. 265); la susceptibilidad se predice sumando (con orientación) las
respuestas de los enlaces.

**Fig. 5.4.1:** (a) enlace entre $A$ y $B$ idealizado como carga puntual $q$ entre los iones; $r_A$, $r_B$ radios
covalentes; $d=r_A+r_B$ longitud de enlace. Según Levine (1973):
$$q=en_v(1/\epsilon+\tfrac13f_c) \qquad (5.4.1)$$
$n_v$ electrones por enlace, $\epsilon$ constante dieléctrica estática, $f_c$ grado fraccional de covalencia. (b) Campo
paralelo al eje: la carga se mueve $\delta r=\alpha_\parallel E/q$ y
$$-\Delta r_A=\Delta r_B=\delta r=\alpha_\parallel E/q \qquad (5.4.2)$$
(c) Campo perpendicular: $\delta r=\alpha_\perp E/q$ y a orden más bajo (p. 266)
$$\Delta r_A=\frac{\delta r^2}{2r_A}=\frac{\alpha_\perp^2E^2}{2r_Aq^2} \qquad (5.4.3a)$$
$$\Delta r_B=\frac{\delta r^2}{2r_B}=\frac{\alpha_\perp^2E^2}{2r_Bq^2} \qquad (5.4.3b)$$
Un campo paralelo cambia $r_A$, $r_B$ linealmente; uno perpendicular sólo a segundo orden.

Predicción cuantitativa (Chemla *et al.*, 1974). Según Phillips (1967) y Van Vechten (1969):
$$\alpha\equiv\tfrac13(\alpha_\parallel+2\alpha_\perp)=(2a_0)^3D\frac{E_0^2}{E_g^2} \qquad (5.4.4)$$
$a_0=4\pi\epsilon_0\hbar^2/me^2$, $E_0=me^4/2(4\pi\epsilon_0)^2\hbar^2$ (Rydberg), $D$ factor numérico ≈ 1, $E_g$ gap medio del enlace:
$$E_g^2=E_h^2+C^2 \qquad (5.4.5)$$
$$E_h=40d^{-2.5} \qquad (5.4.6a)$$
(contribución homopolar; $d$ en Å, $E_h$ en eV),
$$C=1.5e^{-kR}\Big(\frac{z_A}{r_A}-\frac{z_B}{r_B}\Big)e^2 \qquad (5.4.6b)$$
(contribución heteropolar; $z_A$, $z_B$ electrones de valencia; $e^{-kR}$ factor de apantallamiento de
Thomas–Fermi con $R=\tfrac12(r_A+r_B)=\tfrac12d$).

La respuesta no lineal se atribuye a la variación de $\alpha_{ij}$ inducida por el campo (p. 267):
$$p_i=p_i^{(1)}+p_i^{(2)}+p_i^{(3)}+\cdots=\Big[(\alpha_{il})_0+\Big(\frac{\partial\alpha_{il}}{\partial E_j}\Big)E_j+\frac12\Big(\frac{\partial^2\alpha_{il}}{\partial E_j\partial E_k}\Big)E_jE_k\Big]E_l+\cdots\equiv(\alpha_{il})_0E_l+\beta_{ijk}E_jE_l+\gamma_{ijkl}E_jE_kE_l+\cdots \qquad (5.4.7)$$
Enlaces axialmente simétricos ($z$ a lo largo del enlace); componentes no nulas posibles:
$$\beta_\parallel=\beta_{zzz},\quad\beta_\perp=\beta_{xzx} \qquad (5.4.8a)$$
$$\gamma_\parallel=\gamma_{zzzz},\quad\gamma_\perp=\gamma_{xxxx},\quad\gamma_{\parallel\perp}=\gamma_{zzxx} \qquad (5.4.8b)$$
Por (5.4.3) un campo transversal no produce cambio de orden impar en $\alpha_{ij}$:
$$\Big(\frac{\partial}{\partial E_\perp}\Big)^q\alpha_{ij}=0\quad\text{para }q\text{ impar} \qquad (5.4.9)$$
El modelo cumple Kleinman (no considera dispersión), así que $\beta_\perp\equiv\partial\alpha_{xx}/\partial E_z$ se puede escribir
$$\beta_\perp=\frac{\partial\alpha_{xz}}{\partial E_x} \qquad (5.4.10)$$
que se anula por (5.4.9). Igualmente
$$\gamma_{\parallel\perp}=\frac12\frac{\partial^2\alpha_{xz}}{\partial E_x\partial E_z}=0 \qquad (5.4.11)$$
Sólo quedan:
$$\beta_\parallel=\frac{\partial\alpha_\parallel}{\partial E_\parallel}=3\frac{\partial\alpha}{\partial E_\parallel} \qquad (5.4.12)$$
$$\gamma_\parallel=\frac{\partial^2\alpha_\parallel}{\partial E_\parallel^2}=\frac32\frac{\partial^2\alpha}{\partial E_\parallel^2} \qquad (5.4.13)$$
$$\gamma_\perp=\frac{\partial^2\alpha_\perp}{\partial E_\perp^2}=\frac34\frac{\partial^2\alpha}{\partial E_\perp^2} \qquad (5.4.14)$$

> **Duda (5.4.13)–(5.4.14):** según (5.4.7) $\gamma=\tfrac12\partial^2\alpha/\partial E^2$, pero en (5.4.13)–(5.4.14) se escribe $\gamma_\parallel=\partial^2\alpha_\parallel/\partial E_\parallel^2$ sin el
> 1/2 (y (5.4.11) sí lo lleva). Se transcribe tal cual; posible inconsistencia de factor 2.

Aplicación (p. 268): $E_h$ y $C$ se desarrollan en serie del campo con (5.4.2)–(5.4.3); con (5.4.4) se obtiene $\alpha(E)$ y,
con (5.4.12)–(5.4.14), las hiperpolarizabilidades; finalmente $\chi^{(2)}_{ijk}$ y $\chi^{(3)}_{ijkl}$ sumando sobre todos los enlaces
de la celda con su orientación. **Chemla *et al.* (1974): ≈30% de exactitud en el $\chi^{(3)}$ de Ge, Si y GaAs.** Levine
(1973) tiene tablas extensas de comparación.

**Tabla 5.4.1 — Hiperpolarizabilidades de enlace representativas $\gamma$, en unidades de $1.4\times10^{-50}$ m⁵/V² (Kajzar y
Messier, 1985), p. 268.**

| Enlace | $\lambda=1.064$ μm | $\lambda=1.907$ μm |
|---|---|---|
| C–Cl | $0.90\pm0.04$ | 0.7725 |
| C–H | $0.05\pm0.04$ | $-0.0275$ |
| O–H | $0.42\pm0.02$ | 0.5531 |
| C–C | $0.32\pm0.42$ | 0.6211 |
| C=C | $1.03\pm1.52$ | 0.61 |
| C–O | $0.24\pm0.19$ | 0.30 |
| C=O | $0.82\pm1.1$ | 0.99 |

### 5.5 Nonlinear Optics of Chiral Media (p. 268)

Molécula quiral: tiene "lateralidad", su imagen especular es distinta (CS₂, H₂O, CH₄ son aquirales; muchos
orgánicos, p. ej. azúcares como la dextrosa, son quirales). En óptica lineal los medios quirales muestran
actividad óptica (rotación de la polarización lineal; Jenkins y White, 1976): **dextrógiro** si rota en
sentido horario (mirando hacia el haz), **levógiro** si antihorario (p. 269). Enantiómeros = imágenes
especulares; mezcla racémica = mezcla igual, sin actividad óptica.

**Fig. 5.5.1:** colecciones de espirales derechas (a) e izquierdas (b): isótropas pero sin centro de inversión.
Un líquido de moléculas quirales es isótropo y no centrosimétrico → puede tener $\chi^{(2)}$: produce SFG o DFG, pero
**no SHG**, y sólo si los dos haces son **no colineales**. Teoría: Giordmaine (1965); experimento: Rentzepis
*et al.* (1966); trabajos recientes: Verbiest *et al.* (1998).

$$P_i(\omega_\sigma)=2\epsilon_0\sum_{jk}\chi^{(2)}_{ijk}(\omega_\sigma=\omega_1+\omega_2)E_jF_k \qquad (5.5.1)$$
($E_j$ a $\omega_1$, $F_k$ a $\omega_2$, que puede ser negativa).
$$P_i=\epsilon_0\sum_{jk}S_{ijk}(E_jF_k+E_kF_j)+\epsilon_0\sum_{jk}A_{ijk}(E_jF_k-E_kF_j) \qquad (5.5.2)$$
$$S_{ijk}=\tfrac12(\chi^{(2)}_{ijk}+\chi^{(2)}_{ikj}) \qquad (5.5.3a)$$
$$A_{ijk}=\tfrac12(\chi^{(2)}_{ijk}-\chi^{(2)}_{ikj}) \qquad (5.5.3b),\ \text{p. 270}$$
$A_{ijk}$ se anula para SHG o, en general, cuando vale Kleinman. Para un medio isótropo no centrosimétrico (grupo
puntual $\infty\infty$), $S_{ijk}\equiv0$ y los únicos elementos no nulos de $A_{ijk}$ son
$$A_{123}=A_{231}=A_{312} \qquad (5.5.4)$$
$$\mathbf P=\epsilon_0A_{123}\,\mathbf E\times\mathbf F \qquad (5.5.5)$$
**Experimento de Rentzepis *et al.* (Fig. 5.5.2):** haces a 694 nm y 347 nm, de frecuencias distintas (para $A_{123}\neq0$),
polarizaciones ortogonales ($\mathbf E\times\mathbf F\neq0$) y no colineales ($\mathbf P$ con componente transversal) sobre una celda con
arabinosa; señal de suma a 2314 Å (231 nm) hacia el fotodetector, para las formas dextro y levo, sin señal
con la mezcla racémica. $A_{123}=1.3\times10^{-18}$ m/V (comparar: $d_\parallel$(cuarzo) $=1.61\times10^{-17}$ m/V). Reexamen detallado:
Belkin *et al.* (2001) (p. 271).

> **Nota:** el texto escribe "Rentzipis" en la p. 269–270; la referencia es Rentzepis, Giordmaine, Wecht
> (1966) PRL 16, 792.

### 5.6 Nonlinear Optics of Liquid Crystals (p. 271)

No linealidades grandes, lentas (ms o más), útiles para ciertas aplicaciones. Moléculas grandes y
anisótropas. Por encima de una temperatura de transición (típicamente ~100 °C) fase isótropa (líquido
ordinario); por debajo, fase mesotrópica con orientaciones de moléculas vecinas muy correlacionadas
("cristal líquido"); a temperaturas aún menores, sólido. **Fig. 5.6.1:** (a) fase nemática (posiciones al azar,
ejes largos alineados con el *director*); (b) nemática quiral o colestérica (el director rota entre planos
sucesivos). Fuertes no linealidades en ambas fases (Peccianti *et al.*, 2000; Wang y Shen, 1973).

**Fase isótropa** (p. 272): no linealidad de orientación molecular (§4.4), pero mucho mayor y muy dependiente de
la temperatura. Hanson *et al.* (1977):
$$n_2=\frac{2.54\times10^{-15}}{n_0(T-T^*)}\ \frac{\mathrm{m^2K}}{\mathrm W},\qquad T>T^* \qquad (5.6.1)$$
$$\tau=\frac{e^{2800/T(\mathrm K)}}{T-T^*}\,7\times10^{-11}\ \text{ns K},\qquad T>T^* \qquad (5.6.2)$$
con $T^*=77$ °C. Entre 130 y 80 °C, $n_2$ va de 3.2 a $60\times10^{-13}$ cm²/W y $\tau$ de 1 a 72 ns: 10 a 200 veces el CS₂.
(Verificación con $n_0\approx1.5$: $T-T^*=53$ K → $3.2\times10^{-17}$ m²/W $=3.2\times10^{-13}$ cm²/W; 3 K → $5.6\times10^{-12}$ cm²/W ✓.)

**Mesofase:** aún más fuerte; reorientación colectiva de muchas moléculas que interactúan; respuesta efectiva
hasta **$10^9$ veces** la del CS₂. Experimentos con moléculas ancladas a las paredes (Fig. 5.6.2): (a) alineación
planar (superficies frotadas con rayas donde se anclan las moléculas); (b) alineación homeotrópica
(surfactante que alinea perpendicular a las ventanas).

Ángulo $\theta+\theta_0$ entre director y $\mathbf k$ ($\theta_0$ sin láser, $\theta$ reorientación inducida). Khoo (2007) (geometría de la
Fig. 5.6.2(b), unidades gaussianas como Khoo) (p. 273):
$$K_1\frac{d^2\theta}{dz^2}+(n_e^2-n_o^2)\frac{|A|^2}{4\pi}\sin2(\theta+\theta_0)=0 \qquad (5.6.3)$$
$K_1$ constante elástica; $n_o$, $n_e$ índices ordinario y extraordinario sin láser; condiciones de frontera en $z=0$ y
$z=d$. Khoo y Shen (1985): perfil del director como en la Fig. 5.6.3 (reorientación en el centro de la celda,
anclado en las paredes) y cambio de índice promedio $\Delta n=n_2I$ con
$$n_2=\frac{(n_e^2-n_o^2)^2\sin^2(2\beta)d^2}{24K_1c} \qquad (5.6.4)$$
Para $d=100$ μm, $n_e^2-n_o^2=0.6$, $K_1=10^{-6}$ dyn, $\beta=45°$:
$$n_2=5\times10^{-7}\ \mathrm{m^2/W} \qquad (5.6.5)$$

> **Duda numérica (5.6.5):** evaluando (5.6.4) en cgs: $0.36\times(10^{-2}\,\text{cm})^2/(24\times10^{-6}\times3\times10^{10})=5\times10^{-11}$ cm²·s/erg $=5\times10^{-4}$ cm²/W
> $=5\times10^{-8}$ m²/W, un factor 10 menor que el valor impreso. No se pudo reconciliar; verificar con Khoo antes de citar.
> (El símbolo $\beta$ de (5.6.4) es presumiblemente el ángulo $\theta_0$ entre director y $\mathbf k$; el texto no lo define.)

---

## Tablas y datos numéricos útiles

- $E_{\rm at}=5.14\times10^{11}$ V/m; Rydberg 13.6 eV; hidrógeno $\alpha=\tfrac92a_0^3$, $\gamma=\tfrac{3555}{16}a_0^7/e^2$ (gaussiano; ver errata).
- Escalas: $\alpha\simeq V$, $\gamma\propto V^{7/3}$; con TRK: $\alpha\sim L^4$, $\beta\sim L^7$, $\gamma\sim L^{10}$; polímero conjugado (pozo 1D): $\alpha\propto L^3$, $\gamma\propto L^5$.
- Boling–Glass–Owyoung: $n_2$ desde $n$, $\omega_0$, $Nf$ con $(gf)=3$.
- PTS: $\chi^{(3)}=3.5\times10^{-18}$ m²/V² (vs CS₂ $2.7\times10^{-20}$ m²/V², en el texto de la §5.3).
- Conversión de hiperpolarizabilidad: $\gamma$[m⁵/V²] $=1.4\times10^{-14}\gamma$[esu].
- Quiral: arabinosa $A_{123}=1.3\times10^{-18}$ m/V; cuarzo $d_\parallel=1.61\times10^{-17}$ m/V.
- Cristal líquido isótropo: $n_2=2.54\times10^{-15}/[n_0(T-T^*)]$ m²K/W, $T^*=77$ °C; nemático: hasta $10^9\times$ CS₂, (5.6.5) $5\times10^{-7}$ m²/W.
- Tabla 5.4.1 de hiperpolarizabilidades de enlace (arriba).

---

## Problemas (p. 273–274)

1. ***Stark shift in hydrogen.*** Verificar la ecuación (5.1.5).
2. ***Nonlinear response of the square-well potential.*** Usando el formalismo de la §5.1, calcular las
   susceptibilidades lineal y de tercer orden de un conjunto de electrones confinados en un pozo de potencial
   cuadrado unidimensional infinitamente profundo. Este cálculo constituye un modelo simple de la respuesta
   óptica de un polímero conjugado. [Pista: ver Rustagi y Ducuing, 1974.]
3. ***Classical calculation of the second-order response of chiral materials.*** Considerar un oscilador
   anarmónico con potencial $V=\tfrac12(k_ax^2+k_by^2+k_cz^2)+Axyz$. Calcular su respuesta a un campo
   $\mathbf E(t)=\mathbf E_1e^{-i\omega_1t}+\mathbf E_2e^{-i\omega_2t}+$c.c. Luego, suponiendo una distribución de tales osciladores orientada al azar,
   derivar $\chi^{(2)}$ del material. ¿Posee contribuciones simétrica y antisimétrica? Mostrar que la contribución
   antisimétrica se puede expresar como $\mathbf P=\chi_{\rm NL}\mathbf E_1\times\mathbf E_2$.

---

## Referencias principales (p. 274–275)

- Perturbaciones estacionarias: Bethe y Salpeter (1977); Dalgarno (1961); Ducuing (1977) Enrico Fermi LXIV;
  Jha y Bloembergen (1968) Phys. Rev. 171, 891; Sewell (1949); Schiff (1968) *Quantum Mechanics*, 3.ª ed., ec.
  (33.9).
- Semiempíricos: Adair, Chase, Payne (1989) PRB 39, 3337; **Boling, Glass, Owyoung (1978) IEEE JQE 14, 601**;
  Lenz *et al.* (2000) Opt. Lett. 25, 254; Wang (1970) PRB 2, 2045; Wynne (1969) Phys. Rev. 178, 1295.
- Polímeros conjugados: Hermann y Ducuing (1974) JAP 45, 5100; Rustagi y Ducuing (1974) Opt. Commun. 10,
  258. Lecturas: Chemla y Zyss (1987); Kuzyk y Dirk (1998); Prasad y Williams (1991); Blau *et al.* (1991) PRL
  67, 1423 (y comentarios 1992).
- Carga de enlace: Chemla (1971) PRL 26, 1441; **Chemla, Begley, Byer (1974) IEEE JQE 10, 71**; Kajzar y Messier
  (1985) PRA 32, 2352; Levine (1969) PRL 22, 787; Levine (1973) PRB 7, 2600; Phillips (1967) PRL 19, 415; Van
  Vechten (1969) Phys. Rev. 182, 891.
- Quirales: Belkin *et al.* (2001) PRL 87, 113001; Giordmaine (1965) Phys. Rev. 138, A1599; Jenkins y White
  (1976); Rentzepis, Giordmaine, Wecht (1966) PRL 16, 792; Verbiest *et al.* (1998) Science 282, 913.
- Cristales líquidos: Hanson, Shen, Wang (1977) Appl. Phys. 14, 65; Khoo (2007) *Liquid Crystals*, 2.ª ed., cap.
  8; Khoo y Shen (1985) Opt. Eng. 24, 579; Peccianti *et al.* (2000) APL 77, 7; Wang y Shen (1973) PRL 30, 895 y
  PRA 10 (1974) 1277.

---

## Relación con Óptica No Lineal

- No es materia directa del programa (los temas 4–6 cubren Boyd cap. 1, cap. 2 y §4.1–4.2, 7.1–7.2), pero
  complementa el **tema 4**: (5.1.3)–(5.1.4) dan una vía muy simple para obtener $\chi^{(n)}$ estáticos derivando la
  energía, coherente con el oscilador anarmónico y la regla de Miller (§1.4); la generalización de Miller a
  $\chi^{(3)}$ (5.2.1) y la relación de Wang (5.2.2) amplían esa discusión.
- Para el **tema 6** explica por qué $n_2$ crece con el índice lineal y disminuye con la frecuencia de resonancia
  (5.2.5): materiales de alto índice / gap pequeño tienen $n_2$ grande (misma tendencia que $n_2\propto E_g^{-4}$ de la §4.6.2).
- La §5.5 (medios quirales) ilustra la regla de simetría: isótropo ≠ centrosimétrico; sólo el término
  antisimétrico ($\mathbf E\times\mathbf F$) sobrevive y la SHG está prohibida (útil para preguntas conceptuales sobre $\chi^{(2)}$ y
  Kleinman).

## Relación con el proyecto final (supercontinuo / no linealidades en SiN y Si)

- **Estimar $n_2$ de Si₃N₄ (o SiN rico en Si) desde datos lineales:** el modelo de Boling–Glass–Owyoung (5.2.5)
  permite una estimación con $n(\lambda)$ (ajuste Sellmeier → $\omega_0$, $Nf$) y $(gf)\approx3$; sirve como verificación de orden de
  magnitud frente a los valores de literatura (≈ $2.4\times10^{-19}$ m²/W para Si₃N₄ estequiométrico; mayor en SiN rico en
  Si, consistente con $n$ mayor y $E_g$ menor). Cuidado con el posible factor 2 señalado en la duda de (5.2.5).
- **Modelo de carga de enlace:** Chemla *et al.* (1974) predice el $\chi^{(3)}$ de Si con ≈30% de exactitud; justifica que el
  $n_2$ del Si (enlaces Si–Si covalentes, gap pequeño) sea ~20× el del Si₃N₄ (enlaces Si–N más iónicos, gap ≈ 5 eV):
  $E_g^2=E_h^2+C^2$ crece con la heteropolaridad $C$ y $\alpha\propto E_g^{-2}$.
- **Escalas de tiempo:** las no linealidades orientacionales (cristales líquidos, ns–ms) son irrelevantes para
  SC en guías sólidas; la respuesta en SiN/Si es electrónica (fs), más la respuesta Raman (cap. 10) y, en Si,
  los portadores libres de la §4.6.1.

## Erratas y dudas de lectura (resumen)

1. (5.1.2), p. 254: falta $\epsilon_0$ y el último término debe ser $\tilde E^4$, no $\tilde E^3$.
2. p. 255: $R=e^2\hbar^2/4\pi\epsilon_0mc^2$ dimensionalmente incorrecto; debería ser $me^4/[2(4\pi\epsilon_0)^2\hbar^2]$.
3. (5.1.6b), p. 255: $a_0^7/e^6$ → por consistencia gaussiana $a_0^7/e^2$.
4. (5.1.12b), p. 256: signo del denominador ($w_s-w_n$ vs $w_n-w_s$) incoherente con un desplazamiento negativo del fundamental.
5. (5.2.5), p. 260: al rehacer la derivación desde (5.2.3)–(5.2.4) sale $1/12$ en vez de $1/6$ (posible convención de $\gamma$).
6. p. 262: PTS y CS₂ con $\chi^{(3)}$ distintos a los de la Tabla 4.1.2 ($3.5\times10^{-18}$ vs $8.4\times10^{-18}$; $2.7\times10^{-20}$ vs $3.1\times10^{-20}$).
7. p. 263: "than do $\alpha$ and $\beta$" → "$\alpha$ and $\gamma$"; remite al Problema 3 cuando el pozo cuadrado es el Problema 2.
8. (5.4.13)–(5.4.14), p. 267: falta el factor 1/2 de (5.4.7) (posible factor 2).
9. p. 269–270: "Rentzipis" → Rentzepis.
10. (5.6.5), p. 273: la evaluación de (5.6.4) da $5\times10^{-8}$ m²/W, no $5\times10^{-7}$; $\beta$ no está definido en el texto.
