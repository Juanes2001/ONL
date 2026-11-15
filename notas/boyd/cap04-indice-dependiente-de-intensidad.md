# Capítulo 4 — The Intensity-Dependent Refractive Index (Boyd, 3.ª ed.)

Páginas del libro 207–252 (PDF 225–270). Leído el 2026-11-14.

Fuente: R. W. Boyd, *Nonlinear Optics*, 3.ª ed., Academic Press/Elsevier, 2008, cap. 4.
Las citas de página son páginas del libro (sumar 18 para la página del PDF).

Convención de Boyd (SI): $\tilde E(t)=E(\omega)e^{-i\omega t}+\text{c.c.}$, $\tilde P(t)=\epsilon_0[\chi^{(1)}\tilde E+\chi^{(2)}\tilde E^2+\chi^{(3)}\tilde E^3+\dots]$,
$I=2n_0\epsilon_0c|E(\omega)|^2$. **Ojo:** las secciones 4.4 (orientación molecular) y parte de 4.3 escriben
fórmulas con polarizabilidades en estilo gaussiano ($n^2=1+N\langle\alpha\rangle$, sin $4\pi$ ni $\epsilon_0$; resultados en esu); se
señala donde aparece.

Estructura: 4.1 Descripciones del índice dependiente de la intensidad · 4.2 Naturaleza tensorial de
$\chi^{(3)}$ (4.2.1 propagación en medios isótropos: rotación de la elipse) · 4.3 No linealidades
electrónicas no resonantes (4.3.1 oscilador anarmónico, 4.3.2 modelo cuántico, 4.3.3 límite de baja
frecuencia) · 4.4 Orientación molecular (4.4.1 propiedades tensoriales) · 4.5 Efectos térmicos (4.5.1 CW,
4.5.2 pulsados) · 4.6 Semiconductores (4.6.1 transiciones banda‑banda, 4.6.2 transiciones virtuales) ·
4.7 Comentarios finales · Problemas (11) · Referencias.

---

## Resumen del capítulo

El índice de refracción de muchos materiales depende de la intensidad de la luz con que se mide. El
capítulo define dos descripciones equivalentes del efecto Kerr óptico: $n=n_0+\bar n_2\langle\tilde E^2\rangle=n_0+2\bar n_2|E|^2$
y $n=n_0+n_2I$, y las relaciona con la susceptibilidad: $\bar n_2=3\chi^{(3)}/4n_0$, $n_2=3\chi^{(3)}/(4n_0^2\epsilon_0c)$, numéricamente
$n_2[\mathrm{m^2/W}]=283\,\chi^{(3)}[\mathrm{m^2/V^2}]/n_0^2$. Distingue autoacción (un haz, factor de degeneración 3) de acción cruzada
sobre una sonda (factor 6, $\bar n_2^{\rm (cross)}=2\bar n_2$: "weak‑wave retardation"). Da una tabla de mecanismos con
órdenes de magnitud de $n_2$, $\chi^{(3)}$ y tiempo de respuesta (electrónico $10^{-16}$ cm²/W, $10^{-15}$ s; orientación
molecular $10^{-14}$, $10^{-12}$ s; electrostricción $10^{-14}$, $10^{-9}$ s; absorción saturada $10^{-10}$, $10^{-8}$ s; térmico $10^{-6}$,
$10^{-3}$ s; fotorrefractivo, grande) y una tabla extensa de valores medidos (cristales, vidrios,
nanopartículas, polímeros, líquidos, aire, vacío, átomos fríos). En 4.2 muestra que en un medio isótropo
$\chi^{(3)}_{ijkl}=\chi_{1122}\delta_{ij}\delta_{kl}+\chi_{1212}\delta_{ik}\delta_{jl}+\chi_{1221}\delta_{il}\delta_{jk}$ con $\chi_{1111}=\chi_{1122}+\chi_{1212}+\chi_{1221}$; para el índice no lineal sólo
quedan dos constantes, los coeficientes de Maker–Terhune $A=6\chi_{1122}$ y $B=6\chi_{1221}$, con
$\mathbf P=\epsilon_0A(\mathbf E\cdot\mathbf E^*)\mathbf E+\tfrac12\epsilon_0B(\mathbf E\cdot\mathbf E)\mathbf E^*$. Descomponiendo en componentes circulares se obtiene que
$\sigma_+$ y $\sigma_-$ ven índices distintos, $\Delta n=(B/2n_0)(|E_-|^2-|E_+|^2)$, de modo que la elipse de polarización rota
(rotación no lineal de la elipse); sólo luz lineal o circular conserva su estado. La razón
$\delta n_{\rm lin}/\delta n_{\rm circ}=1+B/2A$ vale 4 (orientación molecular), 3/2 (electrónica no resonante) y 1
(electrostricción). Luego estudia los mecanismos físicos: la respuesta electrónica no resonante
(oscilador anarmónico, modelo cuántico con términos de uno y dos fotones, estimación $\chi^{(3)}\sim3\times10^{-22}$ m²/V²,
tiempo $\sim10^{-16}$ s), la orientación molecular (CS₂; $\bar n_2=N(\alpha_3-\alpha_1)^2/45n_0kT$, $B/A=6$), los efectos
térmicos ($\tau\approx\rho_0CR^2/\kappa$, $n_2^{\rm (th)}=(dn/dT)\alpha R^2/\kappa$, dominantes en CW y para pulsos $t_p\gtrsim30$ ps) y las no linealidades de
semiconductores (portadores libres, apantallamiento de excitones, llenado de bandas, renormalización
del gap; y para $\hbar\omega<E_g$ el modelo de dos bandas de Sheik‑Bahae con $n_2\propto G_2(\hbar\omega/E_g)/E_g^4$ y
$\beta\propto F_2(2\hbar\omega/E_g)/E_g^3$). Cierra con el máximo cambio de índice observable y la susceptibilidad
adimensional $\chi^{(3)}_D=\hbar\omega\chi^{(3)}/(2\epsilon_0\lambda^3)$.

---

## Secciones

### Introducción (p. 207)

El índice depende de la intensidad de la luz que lo mide. En el cap. 4 se dan las descripciones
matemáticas y los procesos físicos; el cap. 6 trata el índice no lineal por respuesta resonante de un
sistema atómico y el cap. 7 los procesos físicos que resultan del índice no lineal (autoenfoque, SPM…).

### 4.1 Descriptions of the Intensity-Dependent Refractive Index (p. 207)

**Definición con $\bar n_2$.**
$$n=n_0+\bar n_2\langle\tilde E^2\rangle \qquad (4.1.1),\ \text{p. 207}$$
$n_0$ = índice usual de campo débil; $\bar n_2$ = "índice de refracción de segundo orden", tasa a la que crece el
índice con la intensidad. Los corchetes angulares son promedio temporal. (Nota al pie: la barra sobre
$n_2$ evita confusión con la otra definición (4.1.15).) Para
$$\tilde E(t)=E(\omega)e^{-i\omega t}+\text{c.c.} \qquad (4.1.2)$$
$$\langle\tilde E(t)^2\rangle=2E(\omega)E(\omega)^*=2|E(\omega)|^2 \qquad (4.1.3)$$
$$n=n_0+2\bar n_2|E(\omega)|^2 \qquad (4.1.4),\ \text{p. 208}$$
Este cambio se llama **efecto Kerr óptico**, por analogía con el efecto Kerr electroóptico tradicional,
en el que el índice cambia en proporción al cuadrado de un campo estático aplicado.

**Relación con $\chi^{(3)}$ (un solo haz).** La parte de la polarización no lineal que afecta la propagación
del haz de frecuencia $\omega$ es
$$P^{\rm NL}(\omega)=3\epsilon_0\chi^{(3)}(\omega=\omega+\omega-\omega)|E(\omega)|^2E(\omega) \qquad (4.1.5)$$
(luz linealmente polarizada; se suprimen los índices tensoriales, ver 4.2). La polarización total:
$$P^{\rm TOT}(\omega)=\epsilon_0\chi^{(1)}E(\omega)+3\epsilon_0\chi^{(3)}|E(\omega)|^2E(\omega)\equiv\epsilon_0\chi_{\rm eff}E(\omega) \qquad (4.1.6)$$
$$\chi_{\rm eff}=\chi^{(1)}+3\chi^{(3)}|E(\omega)|^2 \qquad (4.1.7)$$
Usando en general $n^2=1+\chi_{\rm eff}$ (4.1.8) e introduciendo (4.1.4) a la izquierda y (4.1.7) a la derecha:
$$\big[n_0+2\bar n_2|E(\omega)|^2\big]^2=1+\chi^{(1)}+3\chi^{(3)}|E(\omega)|^2 \qquad (4.1.9)$$
Desarrollando al orden $|E|^2$: $n_0^2+4n_0\bar n_2|E|^2=(1+\chi^{(1)})+[3\chi^{(3)}|E|^2]$, de donde
$$n_0=(1+\chi^{(1)})^{1/2} \qquad (4.1.10)$$
$$\boxed{\bar n_2=\frac{3\chi^{(3)}}{4n_0}} \qquad (4.1.11),\ \text{p. 208}$$

**Dos formas de medir (Fig. 4.1.1, p. 209).** (a) Un haz intenso modifica su propia propagación:
sale $E(\omega)e^{i\phi_{\rm NL}}$. (b) Un haz intenso $E(\omega)$ modifica la propagación de una sonda débil $E(\omega')$:
sale $E(\omega')e^{i\phi_{\rm NL}}$. Para la sonda:
$$P^{\rm NL}(\omega')=6\epsilon_0\chi^{(3)}(\omega'=\omega'+\omega-\omega)|E(\omega)|^2E(\omega') \qquad (4.1.12)$$
El factor de degeneración 6 es el doble que en (4.1.5), **incluso si $\omega'=\omega$**, porque la sonda es
físicamente distinguible de la bomba por su dirección de propagación. La sonda ve
$$n=n_0+2\bar n_2^{\rm (cross)}|E(\omega)|^2 \qquad (4.1.13)$$
$$\bar n_2^{\rm (cross)}=\frac{3\chi^{(3)}}{2n_0} \qquad (4.1.14),\ \text{p. 209}$$
$\bar n_2^{\rm (cross)}=2\bar n_2$: una onda intensa afecta el índice de una onda débil de la misma frecuencia el doble
de lo que afecta su propio índice. Para $n_2>0$ esto se conoce como **weak‑wave retardation** (Chiao *et al.*,
1966) (p. 210).

**Definición con $n_2$ e intensidad** (para el caso de un haz; la extensión a dos haces es directa):
$$n=n_0+n_2I \qquad (4.1.15),\ \text{p. 210}$$
$$I=2n_0\epsilon_0c|E(\omega)|^2 \qquad (4.1.16)$$
Como $n$ debe ser el mismo en ambas descripciones, $2\bar n_2|E(\omega)|^2=n_2I$ (4.1.17), luego
$$n_2=\frac{\bar n_2}{n_0\epsilon_0c} \qquad (4.1.18)$$
$$\boxed{n_2=\frac{3}{4n_0^2\epsilon_0c}\chi^{(3)}} \qquad (4.1.19)$$
$$n_2\Big(\frac{\mathrm{m^2}}{\mathrm W}\Big)=\frac{283}{n_0^2}\chi^{(3)}\Big(\frac{\mathrm{m^2}}{\mathrm{V^2}}\Big) \qquad (4.1.20)$$
(Verificación: $3/(4\epsilon_0c)=3/(4\times8.854\times10^{-12}\times2.998\times10^8)=282.5$ Ω.) En unidades gaussianas (conversión en
el apéndice):
$$n_2\Big(\frac{\mathrm{cm^2}}{\mathrm W}\Big)=\frac{12\pi^2}{n_0^2c}10^7\chi^{(3)}(\text{esu})=\frac{0.0395}{n_0^2}\chi^{(3)}(\text{esu}) \qquad (4.1.21),\ \text{p. 210}$$
(con $c$ en cm/s: $12\pi^2\times10^7/3\times10^{10}=0.0395$).

**Tabla 4.1.1 — Valores típicos del índice no lineal (luz linealmente polarizada), p. 211.**

| Mecanismo | $n_2$ (cm²/W) | $\chi^{(3)}_{1111}$ (m²/V²) | Tiempo de respuesta (s) |
|---|---|---|---|
| Polarización electrónica | $10^{-16}$ | $10^{-22}$ | $10^{-15}$ |
| Orientación molecular | $10^{-14}$ | $10^{-20}$ | $10^{-12}$ |
| Electrostricción | $10^{-14}$ | $10^{-20}$ | $10^{-9}$ |
| Absorción atómica saturada | $10^{-10}$ | $10^{-16}$ | $10^{-8}$ |
| Efectos térmicos | $10^{-6}$ | $10^{-12}$ | $10^{-3}$ |
| Efecto fotorrefractivo | (grande) | (grande) | (depende de la intensidad) |

Nota b: el efecto fotorrefractivo suele dar una respuesta muy fuerte que normalmente no puede
describirse con un $\chi^{(3)}$ (o $n_2$), porque la polarización no lineal no depende del campo aplicado de la
misma manera que en los otros mecanismos. Dónde se tratan: electrónico, orientación y térmico en este
capítulo; absorción saturada en el cap. 7; electrostricción en el cap. 9; fotorrefractivo en el cap. 11.

Métodos de medida de $\chi^{(3)}$: revisados por Hellwarth (1977). **Ejemplo numérico (p. 211):** CS₂ tiene
$n_2\approx3\times10^{-14}$ cm²/W; un haz de $I=1$ MW/cm² produce $\Delta n=3\times10^{-8}$. Aunque pequeño, cambios de este orden
producen efectos dramáticos (cap. 7) en interacciones con ajuste de fase.

**Tabla 4.1.2 — Coeficientes ópticos de tercer orden de varios materiales (p. 212–213).**

| Material | $n_0$ | $\chi^{(3)}$ (m²/V²) | $n_2$ (cm²/W) | Comentarios / ref. |
|---|---|---|---|---|
| *Cristales* | | | | |
| Al₂O₃ | 1.8 | $3.1\times10^{-22}$ | $2.9\times10^{-16}$ | 1 |
| CdS | 2.34 | $9.8\times10^{-20}$ | $5.1\times10^{-14}$ | 1, 1.06 μm |
| Diamante | 2.42 | $2.5\times10^{-21}$ | $1.3\times10^{-15}$ | 1 |
| GaAs | 3.47 | $1.4\times10^{-18}$ | $3.3\times10^{-13}$ | 1, 1.06 μm |
| Ge | 4.0 | $5.6\times10^{-19}$ | $9.9\times10^{-14}$ | 2, THG $|\chi^{(3)}|$ |
| LiF | 1.4 | $6.2\times10^{-23}$ | $9.0\times10^{-17}$ | 1 |
| **Si** | **3.4** | $\mathbf{2.8\times10^{-18}}$ | $\mathbf{2.7\times10^{-14}}$ | 2, THG $|\chi^{(3)}|$ |
| TiO₂ | 2.48 | $2.1\times10^{-20}$ | $9.4\times10^{-15}$ | 1 |
| ZnSe | 2.7 | $6.2\times10^{-20}$ | $3.0\times10^{-14}$ | 1, 1.06 μm |
| *Vidrios* | | | | |
| Sílice fundida | 1.47 | $2.5\times10^{-22}$ | $3.2\times10^{-16}$ | 1 |
| Vidrio As₂S₃ | 2.4 | $4.1\times10^{-19}$ | $2.0\times10^{-13}$ | 3 |
| BK-7 | 1.52 | $2.8\times10^{-22}$ | $3.4\times10^{-16}$ | 1 |
| BSC | 1.51 | $5.0\times10^{-22}$ | $6.4\times10^{-16}$ | 1 |
| Galato de Pb‑Bi | 2.3 | $2.2\times10^{-20}$ | $1.3\times10^{-14}$ | 4 |
| SF-55 | 1.73 | $2.1\times10^{-21}$ | $2.0\times10^{-15}$ | 1 |
| SF-59 | 1.953 | $4.3\times10^{-21}$ | $3.3\times10^{-15}$ | 1 |
| *Nanopartículas* | | | | |
| CdSSe en vidrio | 1.5 | $1.4\times10^{-20}$ | $1.8\times10^{-14}$ | 3, no res. |
| Vidrio CS 3-68 | 1.5 | $1.8\times10^{-16}$ | $2.3\times10^{-10}$ | 3, res. |
| Oro en vidrio | 1.5 | $2.1\times10^{-16}$ | $2.6\times10^{-10}$ | 3, res. |
| *Polímeros (polidiacetilenos)* | | | | |
| PTS | — | $8.4\times10^{-18}$ | $3.0\times10^{-12}$ | 5, no res. |
| PTS | — | $-5.6\times10^{-16}$ | $-2.0\times10^{-10}$ | 6, res. |
| 9BCMU | — | — | $2.7\times10^{-18}$ | 7, $|n_2|$, res. |
| 4BCMU | 1.56 | $-1.3\times10^{-19}$ | $-1.5\times10^{-13}$ | 8, no res., $\beta=0.01$ cm/MW |
| *Líquidos* | | | | |
| Acetona | 1.36 | $1.5\times10^{-21}$ | $2.4\times10^{-15}$ | 9 |
| Benceno | 1.5 | $9.5\times10^{-22}$ | $1.2\times10^{-15}$ | 9 |
| Disulfuro de carbono | 1.63 | $3.1\times10^{-20}$ | $3.2\times10^{-14}$ | 9, $\tau=2$ ps |
| CCl₄ | 1.45 | $1.1\times10^{-21}$ | $1.5\times10^{-15}$ | 9 |
| Diyodometano | 1.69 | $1.5\times10^{-20}$ | $1.5\times10^{-14}$ | 9 |
| Etanol | 1.36 | $5.0\times10^{-22}$ | $7.7\times10^{-16}$ | 9 |
| Metanol | 1.33 | $4.3\times10^{-22}$ | $6.9\times10^{-16}$ | 9 |
| Nitrobenceno | 1.56 | $5.7\times10^{-20}$ | $6.7\times10^{-14}$ | 9 |
| Agua | 1.33 | $2.5\times10^{-22}$ | $4.1\times10^{-16}$ | 9 |
| *Otros* | | | | |
| Aire | 1.0003 | $1.7\times10^{-25}$ | $5.0\times10^{-19}$ | 10 |
| Ag | — | $2.8\times10^{-19}$ | — | 2, THG $|\chi^{(3)}|$ |
| Au | — | $7.6\times10^{-19}$ | — | 2, THG $|\chi^{(3)}|$ |
| Vacío | 1 | $3.4\times10^{-41}$ | $1.0\times10^{-34}$ | 11 |
| Átomos fríos | 1.0 | $7.1\times10^{-8}$ | 0.2 | 12, (EIT BEC) |
| Fluoresceína en vidrio | 1.5 | $(2.8+2.8i)\times10^{-8}$ | $0.035(1+i)$ | 13, $\tau=0.1$ s |

Notas de la tabla (p. 213): (a) Se usa la definición de $\chi^{(3)}$ del libro (ec. (1.1.2) o (1.3.21)),
consistente con Bloembergen (1964); algunos autores usan una definición que da valores **cuatro veces
menores**; los valores de literatura se convirtieron a la definición del libro. $n_2$ se define por
$n=n_0+n_2I$. $\beta$ = coeficiente de absorción de dos fotones. (b) Referencias: 1 Chase y Van Stryland (1995),
2 Bloembergen *et al.* (1969), 3 Vogel *et al.* (1991), 4 Hall *et al.* (1989), 5 Lawrence *et al.* (1994), 6 Carter
*et al.* (1985), 7 Molyneux *et al.* (1993), 8 Erlich *et al.* (1993), 9 Sutherland (1996), 10 Pennington *et al.*
(1989), 11 Euler y Kockel (1935), 12 Hau *et al.* (1999), 13 Kramer *et al.* (1986) (numeración en el orden en
que la nota las lista).

> **Duda de lectura (nota a de la Tabla 4.1.2, p. 213):** se lee "the relation between $n_2$ and $\chi^{(3)}$ is
> consequently $n_2=12\pi^2\chi^{(3)}/n_0^2$". Esa es la forma gaussiana sin el factor $10^7/c$; en SI la relación correcta es
> (4.1.19)–(4.1.20) y en gaussianas la (4.1.21) (que la misma nota da a continuación con 0.0395).

### 4.2 Tensor Nature of the Third-Order Susceptibility (p. 211)

$\chi^{(3)}_{ijkl}$ es un tensor de rango 4 con 81 elementos; en sólidos de baja simetría todos pueden ser
independientes y no nulos (Butcher, 1965); con más simetría el número se reduce y en un medio isótropo
(vidrio, líquido, vapor) sólo quedan **tres** independientes.

Caso general de frecuencias arbitrarias, $\chi_{ijkl}\equiv\chi^{(3)}_{ijkl}(\omega_4=\omega_1+\omega_2+\omega_3)$. Equivalencia de los ejes (p. 213):
$$\chi_{1111}=\chi_{2222}=\chi_{3333} \qquad (4.2.1a)$$
$$\chi_{1122}=\chi_{1133}=\chi_{2211}=\chi_{2233}=\chi_{3311}=\chi_{3322} \qquad (4.2.1b)$$
$$\chi_{1212}=\chi_{1313}=\chi_{2323}=\chi_{2121}=\chi_{3131}=\chi_{3232} \qquad (4.2.1c)$$
$$\chi_{1221}=\chi_{1331}=\chi_{2112}=\chi_{2332}=\chi_{3113}=\chi_{3223} \qquad (4.2.1d)$$
Estos 21 son los únicos no nulos: cada índice cartesiano que aparece debe aparecer un número par de
veces. Un índice impar, p. ej. $\chi_{1222}$, daría respuesta en $\hat x_1$ por campo en $\hat x_2$, y en un medio isótropo
no hay razón para preferir $+\hat x_1$ a $-\hat x_1$.

Los cuatro tipos no son independientes (p. 214):
$$\chi_{1111}=\chi_{1122}+\chi_{1212}+\chi_{1221} \qquad (4.2.2)$$
(se deduce exigiendo que $\mathbf P$ sea igual en dos sistemas rotados un ángulo arbitrario; conviene una rotación
de 45° alrededor de $\hat x_3$ — Problema 2). Forma compacta:
$$\chi_{ijkl}=\chi_{1122}\delta_{ij}\delta_{kl}+\chi_{1212}\delta_{ik}\delta_{jl}+\chi_{1221}\delta_{il}\delta_{jk} \qquad (4.2.3)$$
tres elementos independientes para frecuencias arbitrarias.

**THG**, $\chi_{ijkl}(3\omega=\omega+\omega+\omega)$: por simetría de permutación intrínseca $\chi_{1122}=\chi_{1212}=\chi_{1221}$:
$$\chi_{ijkl}(3\omega=\omega+\omega+\omega)=\chi_{1122}(3\omega=\omega+\omega+\omega)(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}) \qquad (4.2.4)$$
un solo elemento independiente.

**Índice no lineal**, $\chi_{ijkl}(\omega=\omega+\omega-\omega)$: la permutación intrínseca exige $\chi_{1122}=\chi_{1212}$:
$$\chi_{ijkl}(\omega=\omega+\omega-\omega)=\chi_{1122}(\omega=\omega+\omega-\omega)(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl})+\chi_{1221}(\omega=\omega+\omega-\omega)(\delta_{il}\delta_{jk}) \qquad (4.2.5)$$
La polarización (ver también (1.3.21)):
$$P_i(\omega)=3\epsilon_0\sum_{jkl}\chi_{ijkl}(\omega=\omega+\omega-\omega)E_j(\omega)E_k(\omega)E_l(-\omega) \qquad (4.2.6)$$
Sustituyendo (4.2.5):
$$P_i=6\epsilon_0\chi_{1122}E_i(\mathbf E\cdot\mathbf E^*)+3\epsilon_0\chi_{1221}E_i^*(\mathbf E\cdot\mathbf E) \qquad (4.2.7)$$
$$\mathbf P=6\epsilon_0\chi_{1122}(\mathbf E\cdot\mathbf E^*)\mathbf E+3\epsilon_0\chi_{1221}(\mathbf E\cdot\mathbf E)\mathbf E^* \qquad (4.2.8),\ \text{p. 215}$$

**Coeficientes de Maker y Terhune (1965; Maker *et al.*, 1964):**
$$A=6\chi_{1122}\quad(\text{o } A=3\chi_{1122}+3\chi_{1212}) \qquad (4.2.9a)$$
$$B=6\chi_{1221} \qquad (4.2.9b)$$
$$\boxed{\mathbf P=\epsilon_0A(\mathbf E\cdot\mathbf E^*)\mathbf E+\tfrac12\epsilon_0B(\mathbf E\cdot\mathbf E)\mathbf E^*} \qquad (4.2.10)$$
El primer término tiene el carácter vectorial de $\mathbf E$ (misma helicidad que $\mathbf E$), el segundo el de $\mathbf E^*$
(helicidad opuesta). **Fig. 4.2.1:** (a) procesos resonantes a un fotón (absorción‑emisión dos veces, vía un
nivel real) contribuyen sólo a $A$ (se mostrará en (4.3.14)); (b) procesos resonantes a dos fotones
contribuyen en general a $A$ y $B$ ((4.3.13), (4.3.14)); en ciertos casos (Fig. 7.2.9) sólo a $B$.

**Susceptibilidad lineal efectiva** (p. 216): definiendo $P_i=\sum_j\epsilon_0\chi^{\rm (eff)}_{ij}E_j$ (4.2.11), (4.2.10) y (4.2.11)
coinciden si
$$\chi^{\rm (eff)}_{ij}=\epsilon_0A'(\mathbf E\cdot\mathbf E^*)\delta_{ij}+\tfrac12\epsilon_0B'(E_iE_j^*+E_i^*E_j) \qquad (4.2.12a)$$
$$A'=A-\tfrac12B=6\chi_{1122}-3\chi_{1221} \qquad (4.2.12b)$$
$$B'=B=6\chi_{1221} \qquad (4.2.12c)$$

> **Errata probable (4.2.12a), p. 216:** se lee $\chi^{\rm (eff)}_{ij}=\epsilon_0A'(\dots)+\tfrac12\epsilon_0B'(\dots)$. Como (4.2.11) ya tiene $\epsilon_0$ fuera,
> por consistencia dimensional debería ser $\chi^{\rm (eff)}_{ij}=A'(\mathbf E\cdot\mathbf E^*)\delta_{ij}+\tfrac12B'(E_iE_j^*+E_i^*E_j)$ (sin $\epsilon_0$).
> Comprobación: $\sum_j[A'(\mathbf E\cdot\mathbf E^*)\delta_{ij}+\tfrac12B(E_iE_j^*+E_i^*E_j)]E_j=(A-\tfrac B2)(\mathbf E\cdot\mathbf E^*)E_i+\tfrac B2E_i(\mathbf E\cdot\mathbf E^*)+\tfrac B2E_i^*(\mathbf E\cdot\mathbf E)$ = (4.2.10)/$\epsilon_0$. ✓.

El tensor del índice no lineal de un medio isótropo tiene sólo **dos** elementos independientes; su razón
depende del mecanismo:
$$B/A=6,\quad B'/A'=-3\quad\text{orientación molecular} \qquad (4.2.13a)$$
$$B/A=1,\quad B'/A'=2\quad\text{respuesta electrónica no resonante} \qquad (4.2.13b)$$
$$B/A=0,\quad B'/A'=0\quad\text{electrostricción} \qquad (4.2.13c)$$
(justificación: (4.4.37) orientación, (4.3.14) electrónica de electrones ligados, (9.2.15) electrostricción).
$A=B$ por definición siempre que valga la simetría de Kleinman.

Traza:
$$\mathrm{Tr}\,\chi_{ij}\equiv\sum_i\chi_{ii}=(3A'+B')\mathbf E\cdot\mathbf E^* \qquad (4.2.14)$$
se anula para orientación molecular: la orientación no añade "polarizabilidad adicional", sólo redistribuye
la existente entre componentes tensoriales (p. 216–217). Para una transición atómica resonante, $B/A$
depende de los momentos angulares de los niveles (Saikan y Kiguchi, 1982).

#### 4.2.1 Propagation through Isotropic Nonlinear Media (p. 217)

Sólo luz lineal o circularmente polarizada se transmite con su estado de polarización intacto; la luz
elíptica sufre una rotación de la elipse con la distancia.

Descomposición circular:
$$\mathbf E=E_+\hat{\boldsymbol\sigma}_++E_-\hat{\boldsymbol\sigma}_- \qquad (4.2.15)$$
$$\hat{\boldsymbol\sigma}_\pm=\frac{\hat{\mathbf x}\pm i\hat{\mathbf y}}{\sqrt2} \qquad (4.2.16)$$
Por convención $\hat\sigma_+$ = circular **izquierda** y $\hat\sigma_-$ = circular **derecha** (haz que viaja en $+z$; Fig. 4.2.2).
Identidades: $\hat\sigma_\pm^*=\hat\sigma_\mp$, $\hat\sigma_\pm\cdot\hat\sigma_\pm=0$, $\hat\sigma_\pm\cdot\hat\sigma_\mp=1$. Entonces (p. 218)
$\mathbf E^*\cdot\mathbf E=|E_+|^2+|E_-|^2$ y $\mathbf E\cdot\mathbf E=2E_+E_-$, de modo que
$$\mathbf P^{\rm NL}=\epsilon_0A(|E_+|^2+|E_-|^2)\mathbf E+\epsilon_0B(E_+E_-)\mathbf E^* \qquad (4.2.17)$$
Con $\mathbf P^{\rm NL}=P_+\hat\sigma_++P_-\hat\sigma_-$ (4.2.18), y notando que $\mathbf E^*=E_+^*\hat\sigma_-+E_-^*\hat\sigma_+$:
$$P_+=\epsilon_0A(|E_+|^2+|E_-|^2)E_++\epsilon_0B(E_+E_-)E_-^*=\epsilon_0A|E_+|^2E_++\epsilon_0(A+B)|E_-|^2E_+ \qquad (4.2.19a)$$
$$P_-=\epsilon_0A|E_-|^2E_-+\epsilon_0(A+B)|E_+|^2E_- \qquad (4.2.19b)$$
$$P_\pm\equiv\epsilon_0\chi^{\rm NL}_\pm E_\pm \qquad (4.2.20a)$$
$$\chi^{\rm NL}_\pm=A|E_\pm|^2+(A+B)|E_\mp|^2 \qquad (4.2.20b)$$
Ecuación de onda (con $\tilde{\mathbf E}=\mathbf Ee^{-i\omega t}+$c.c., $\tilde{\mathbf P}=\mathbf Pe^{-i\omega t}+$c.c.):
$$\nabla^2\mathbf E(z,t)=\frac{\epsilon^{(1)}}{c^2}\frac{\partial^2\mathbf E(z,t)}{\partial t^2}+\frac{1}{\epsilon_0c^2}\frac{\partial^2}{\partial t^2}\mathbf P^{\rm NL} \qquad (4.2.21)$$
Como $P_\pm\propto E_\pm$, cada componente circular obedece (p. 219)
$$\nabla^2\tilde E_\pm(z,t)=\frac{\epsilon^{\rm (eff)}_\pm}{c^2}\frac{\partial^2\tilde E_\pm(z,t)}{\partial t^2} \qquad (4.2.22a)$$
$$\epsilon^{\rm (eff)}_\pm=\epsilon^{(1)}+\chi^{\rm NL}_\pm \qquad (4.2.22b)$$
Ondas planas con velocidad de fase $c/n_\pm$, $n_\pm=[\epsilon^{\rm (eff)}_\pm]^{1/2}$. Con $n_0^2=\epsilon^{(1)}$:
$n_\pm^2=n_0^2+[A|E_\pm|^2+(A+B)|E_\mp|^2]=n_0^2\big(1+\frac{1}{n_0^2}[\dots]\big)$, y
$$n_\pm\simeq n_0+\frac{1}{2n_0}\big[A|E_\pm|^2+(A+B)|E_\mp|^2\big] \qquad (4.2.23)$$
$$\boxed{\Delta n\equiv n_+-n_-=\frac{B}{2n_0}\big(|E_-|^2-|E_+|^2\big)} \qquad (4.2.24)$$
Depende sólo de $B$, no de $A$. Como las componentes circulares viajan con distinta velocidad, la elipse
rota (análogo a la actividad óptica lineal).

Ángulo de rotación:
$$\mathbf E(z)=A_+e^{in_+\omega z/c}\hat\sigma_++A_-e^{in_-\omega z/c}\hat\sigma_-=\big(A_+e^{i\frac12\Delta n\omega z/c}\hat\sigma_++A_-e^{-i\frac12\Delta n\omega z/c}\hat\sigma_-\big)e^{i\frac12(n_++n_-)\omega z/c} \qquad (4.2.25)$$
Con $k_m=\tfrac12(n_++n_-)\omega/c$ y
$$\theta=\tfrac12\Delta n\frac{\omega}{c}z \qquad (4.2.26a)$$
$$\mathbf E(z)=\big(A_+\hat\sigma_+e^{i\theta}+A_-\hat\sigma_-e^{-i\theta}\big)e^{ik_mz} \qquad (4.2.26b),\ \text{p. 220}$$
Es la elipse incidente rotada un ángulo $\theta$ (medido en sentido horario en el plano $xy$, según la
convención de actividad óptica; Fig. 4.2.3), porque
$$\hat\sigma_\pm e^{\pm i\theta}=\frac{\hat{\mathbf x}'\pm i\hat{\mathbf y}'}{\sqrt2} \qquad (4.2.27)$$
con $x'=x\cos\theta-y\sin\theta$ (4.2.28a), $y'=x\sin\theta+y\cos\theta$ (4.2.28b). Medir $\theta$ es un método sensible para
determinar $B$.

Casos sin rotación:
- **Circular** (sólo una componente):
$$\delta n_{\rm circular}=\frac{1}{2n_0}A|E|^2 \qquad (4.2.29)$$
  depende de $A$ y no de $B$.
- **Lineal** ($|E_-|^2=|E_+|^2$, $\Delta n=0$); con $|E|^2=2|E_+|^2=2|E_-|^2$ (p. 221):
$$\delta n_{\rm linear}=\frac{1}{2n_0}\big(A+\tfrac12B\big)|E|^2 \qquad (4.2.30)$$
  y $A+\tfrac12B=3\chi_{1111}$ por (4.2.2) y (4.2.9). [Consistencia: $\delta n_{\rm lin}=3\chi_{1111}|E|^2/2n_0=2\bar n_2|E|^2$ con (4.1.11). ✓]

Si $A$ y $B$ tienen el mismo signo, la luz lineal sufre mayor cambio que la circular:
$$\frac{\delta n_{\rm linear}}{\delta n_{\rm circular}}=1+\frac{B}{2A}=\begin{cases}4 & \text{orientación molecular}\\ \tfrac32 & \text{electrónica no resonante}\\ 1 & \text{electrostricción}\end{cases}\qquad(\text{p. 221})$$
Con dos haces contrapropagantes el análisis es mucho más complejo: biestabilidad de polarización,
inestabilidades y caos (teoría: Gaeta *et al.*, 1987; experimentos: Gauthier *et al.*, 1988, 1990).

### 4.3 Nonresonant Electronic Nonlinearities (p. 221)

Resultan de la respuesta no lineal de los electrones ligados. No es grande ($\chi^{(3)}\sim10^{-22}$ m²/V² típico) pero
está presente en **todos** los dieléctricos; ciertos orgánicos (polidiacetileno) llegan a $10^{-17}$ m²/V² por los
electrones $\pi$ deslocalizados. Son extremadamente rápidas (sólo procesos virtuales): el tiempo de respuesta
es el de distorsión de la nube electrónica, estimado como el periodo orbital de Bohr
$\tau=2\pi a_0/v$, con $a_0=0.5\times10^{-10}$ m y $v\simeq c/137$: $\tau\simeq10^{-16}$ s (p. 222).

#### 4.3.1 Classical, Anharmonic Oscillator Model of Electronic Nonlinearities (p. 222)

Modelo de la §1.4 con potencial
$$U(\mathbf r)=\tfrac12m\omega_0^2|\mathbf r|^2-\tfrac14mb|\mathbf r|^4 \qquad (4.3.1)$$
$b$ fenomenológico, del orden $\omega_0^2/d^2$ ($d$ = dimensión atómica). De (1.4.52), para el índice no lineal:
$$\chi^{(3)}_{ijkl}(\omega=\omega+\omega-\omega)=\frac{Nbe^4[\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}]}{3\epsilon_0m^3D(\omega)^3D(-\omega)} \qquad (4.3.2)$$
con $D(\omega)=\omega_0^2-\omega^2-2i\omega\gamma$. En notación de Maker–Terhune:
$$A=B=\frac{2Nbe^4}{\epsilon_0m^3D(\omega)^3D(-\omega)} \qquad (4.3.3)$$
— en el modelo clásico $A=B$ para cualquier frecuencia (resonante o no). Lejos de resonancia ($\omega\ll\omega_0$,
$D\to\omega_0^2$) y con $b=\omega_0^2/d^2$:
$$\chi^{(3)}\simeq\frac{Ne^4}{\epsilon_0m^3\omega_0^6d^2} \qquad (4.3.4)$$
**Ejemplo:** $N=4\times10^{22}$ cm⁻³, $d=3\times10^{-10}$ m, $\omega_0=7\times10^{15}$ rad/s → $\chi^{(3)}\simeq3\times10^{-22}$ m²/V² (p. 222).

#### 4.3.2 Quantum-Mechanical Model of Nonresonant Electronic Nonlinearities (p. 223)

Se parte de (3.2.33):
$$\chi^{(3)}_{kjih}(\omega_\sigma,\omega_r,\omega_q,\omega_p)=\frac{N}{\epsilon_0\hbar^3}\mathcal P_F\sum_{lmn}\left[\frac{\mu^k_{gn}\mu^j_{nm}\mu^i_{ml}\mu^h_{lg}}{(\omega_{ng}-\omega_\sigma)(\omega_{mg}-\omega_q-\omega_p)(\omega_{lg}-\omega_p)}\right] \qquad (4.3.5)$$
con $\omega_\sigma=\omega_r+\omega_q+\omega_p$. Para $\chi^{(3)}_{kjih}(\omega,\omega,\omega,-\omega)$ parece divergir: $\omega_{mg}-\omega_q-\omega_p=0$ si $m=g$ y $\omega_p=-\omega_q=\pm\omega$.
La divergencia es aparente (Hanna *et al.*, 1979; Orr y Ward, 1971). Se separan los términos $m=g$:
$$\chi^{(3)}=\frac{N}{\epsilon_0\hbar^3}\mathcal P_F\Bigg[\sum_{lmn}{}'\frac{\mu^k_{gn}\mu^j_{nm}\mu^i_{ml}\mu^h_{lg}}{(\omega_{ng}-\omega_\sigma)(\omega_{mg}-\omega_q-\omega_p)(\omega_{lg}-\omega_p)}-\sum_{ln}\frac{\mu^k_{gn}\mu^j_{ng}\mu^i_{gl}\mu^h_{lg}}{(\omega_{ng}-\omega_\sigma)(\omega_q+\omega_p)(\omega_{lg}-\omega_p)}\Bigg] \qquad (4.3.6)$$
(prima: se omite $m=g$). Con la identidad
$$\frac{1}{XY}=\frac{1}{(X+Y)Y}+\frac{1}{(X+Y)X} \qquad (4.3.7)$$
y $X=\omega_q+\omega_p$, $Y=\omega_{lg}-\omega_p$ (p. 224):
$$\chi^{(3)}=\frac{N}{\epsilon_0\hbar^3}\mathcal P_F\Bigg[\sum_{lmn}{}'\frac{\mu^k_{gn}\mu^j_{nm}\mu^i_{ml}\mu^h_{lg}}{(\omega_{ng}-\omega_\sigma)(\omega_{mg}-\omega_q-\omega_p)(\omega_{lg}-\omega_p)}-\sum_{ln}\frac{\mu^k_{gn}\mu^j_{ng}\mu^i_{gl}\mu^h_{lg}}{(\omega_{ng}-\omega_\sigma)(\omega_{lg}+\omega_q)(\omega_{lg}-\omega_p)}\Bigg] \qquad (4.3.8)$$
más la contribución
$$\mathcal P_F\sum_{ln}\frac{\mu^k_{gn}\mu^j_{ng}\mu^i_{gl}\mu^h_{lg}}{(\omega_{ng}-\omega_\sigma)(\omega_{lg}+\omega_q)(\omega_q+\omega_p)} \qquad (4.3.9)$$
que se anula: para cada término (4.3.10a) existe otro con $n\leftrightarrow l$, $(-\omega_\sigma,k)\leftrightarrow(\omega_q,i)$ y $(\omega_p,h)\leftrightarrow(\omega_r,j)$,
$$\frac{\mu^i_{gl}\mu^h_{lg}\mu^k_{gn}\mu^j_{ng}}{(\omega_{lg}+\omega_q)(\omega_{ng}-\omega_\sigma)(\omega_r-\omega_\sigma)} \qquad (4.3.10b)$$
y como $\omega_\sigma=\omega_p+\omega_q+\omega_r$, $(\omega_q+\omega_p)=-(\omega_r-\omega_\sigma)$: iguales en magnitud y opuestos. (4.3.8) equivale a (4.3.5) sin
divergencias aparentes.

Al expandir $\mathcal P_F$, cada término de (4.3.8) son 24 términos (48 en total). Su carácter resonante se analiza
con diagramas como Fig. 3.2.3 (nota: esa figura supone las tres frecuencias positivas; aquí dos son
positivas y una negativa). Reteniendo sólo los términos casi resonantes (p. 225):
$$\chi^{(3)}_{kjih}(\omega=\omega+\omega-\omega)=\frac{N}{6\epsilon_0\hbar^3}\Bigg(\sum_{lmn}{}'\frac{\mu^k_{gn}\mu^h_{nm}\mu^i_{ml}\mu^j_{lg}+\mu^k_{gn}\mu^h_{nm}\mu^j_{ml}\mu^i_{lg}+\mu^h_{gn}\mu^k_{nm}\mu^i_{ml}\mu^j_{lg}+\mu^h_{gn}\mu^k_{nm}\mu^j_{ml}\mu^i_{lg}}{(\omega_{ng}-\omega)(\omega_{mg}-2\omega)(\omega_{lg}-\omega)}$$
$$-\sum_{ln}\frac{\mu^k_{gn}\mu^j_{ng}\mu^h_{gl}\mu^i_{lg}+\mu^k_{gn}\mu^i_{ng}\mu^h_{gl}\mu^j_{lg}+\mu^h_{gn}\mu^i_{ng}\mu^k_{gl}\mu^j_{lg}+\mu^h_{gn}\mu^j_{ng}\mu^k_{gl}\mu^i_{lg}}{(\omega_{ng}-\omega)(\omega_{lg}-\omega)(\omega_{lg}-\omega)}\Bigg) \qquad (4.3.11)$$
Primera suma: procesos resonantes a **dos fotones**; segunda: resonantes a **un fotón** (Fig. 4.3.1: (a) $g\to l\to m$
absorbiendo dos fotones y regresando por $n$; (b) $g\to l\to g$ y $g\to n\to g$).

Elementos para un medio isótropo:
$$\chi_{1111}=\frac{2N}{3\epsilon_0\hbar^3}\sum_{lmn}{}'\frac{\mu^x_{gn}\mu^x_{nm}\mu^x_{ml}\mu^x_{lg}}{(\omega_{ng}-\omega)(\omega_{mg}-2\omega)(\omega_{lg}-\omega)}-\frac{2N}{3\epsilon_0\hbar^3}\sum_{ln}\frac{\mu^x_{gn}\mu^x_{ng}\mu^x_{gl}\mu^x_{lg}}{(\omega_{ng}-\omega)(\omega_{lg}-\omega)(\omega_{lg}-\omega)} \qquad (4.3.12)$$
Contribuyen ambos tipos. Para $\omega$ menor que toda resonancia (p. 226): el término de **dos fotones tiende a
ser positivo** (hay probabilidad no nula de que el átomo esté en un estado excitado $l$ o $n$, cuya
polarizabilidad lineal suele ser mayor que la del fundamental → aumenta la polarizabilidad efectiva); el de
**un fotón es siempre negativo** (numerador definido positivo): origen en la saturación de la respuesta
atómica (disminuye la susceptibilidad lineal positiva), o bien efecto Stark ac (§6.5), que aumenta la
separación entre niveles y disminuye la respuesta (Fig. 4.3.2: para $\omega<\omega_{lg}$ el Stark ac separa más $g$ y $l$).

$$\chi_{1221}\ \big(=\tfrac16B\big)=\frac{2}{3}\frac{N}{\epsilon_0\hbar^3}\sum_{lmn}{}'\frac{\mu^x_{gn}\mu^x_{nm}\mu^y_{ml}\mu^y_{lg}}{(\omega_{ng}-\omega)(\omega_{mg}-2\omega)(\omega_{lg}-\omega)} \qquad (4.3.13)$$
Los términos de un fotón no contribuyen a $\chi_{1221}$: involucran productos $\mu^x_{gl}\mu^y_{lg}$ que siempre se anulan
(nota al pie: tomando $x$ como eje de cuantización, si $\mu^x_{gl}\neq0$ entonces $\mu^y_{gl}=0$ y viceversa).
$$\chi_{1122}\ \big(=\tfrac16A\big)=\frac{N}{3\epsilon_0\hbar^3}\sum_{lmn}{}'\frac{\mu^x_{gn}\mu^y_{nm}\mu^y_{ml}\mu^x_{lg}+\mu^x_{gn}\mu^y_{nm}\mu^x_{ml}\mu^y_{lg}}{(\omega_{ng}-\omega)(\omega_{mg}-2\omega)(\omega_{lg}-\omega)}-\frac{N}{3\epsilon_0\hbar^3}\sum_{ln}\frac{\mu^x_{gn}\mu^x_{ng}\mu^y_{gl}\mu^y_{lg}}{(\omega_{ng}-\omega)(\omega_{mg}-\omega)(\omega_{lg}-\omega)} \qquad (4.3.14),\ \text{p. 227}$$

> **Duda de lectura (4.3.14):** en el denominador del segundo término (suma sobre $l,n$) se lee $(\omega_{mg}-\omega)$;
> en esa suma no hay índice $m$, por consistencia con (4.3.11)–(4.3.12) debería ser $(\omega_{lg}-\omega)$.

#### 4.3.3 $\chi^{(3)}$ in the Low-Frequency Limit (p. 227)

Si $\omega$ es mucho menor que toda resonancia (p. ej. aislante con luz visible), todos los términos de $\mathcal P_F$
contribuyen comparablemente y no hay simplificación. Hecho experimental: en el límite de baja frecuencia
$\chi_{1122}$ y $\chi_{1221}$ (y por tanto $\chi_{1111}=2\chi_{1122}+\chi_{1221}$) son **positivos** para la gran mayoría de materiales. Vale
Kleinman: $\chi_{1122}=\chi_{1221}$, es decir $B=A$. Estimación de orden de magnitud de (4.3.5):
$$\chi^{(3)}\simeq\frac{8N\mu^4}{\epsilon_0\hbar^3\omega_0^3} \qquad (4.3.15)$$
($\mu$ dipolo típico, $\omega_0$ resonancia típica). Aunque (4.3.4) y (4.3.15) tienen dependencias distintas, coinciden
si $d\to a_0=4\pi\epsilon_0\hbar^2/me^2$, $\mu\to-ea_0$ y $\omega_0\to$ Rydberg en frecuencia angular $me^4/32\pi^2\epsilon_0^2\hbar^3$. El modelo cuántico
también predice $\chi^{(3)}\sim3\times10^{-22}$ m²/V².

**Tabla 4.3.1 — Coeficientes de materiales con no linealidad electrónica (p. 228).**

| Material | $n_0$ | $\chi_{1111}$ (m²/V²) | $n_2$ (m²/W) |
|---|---|---|---|
| Diamante | 2.42 | $21\times10^{-22}$ | $10\times10^{-20}$ |
| Granate de itrio y aluminio (YAG) | 1.83 | $8.4\times10^{-22}$ | $8.4\times10^{-20}$ |
| Zafiro | 1.8 | $4.2\times10^{-22}$ | $3.7\times10^{-20}$ |
| Vidrio crown borosilicato | 1.5 | $3.5\times10^{-22}$ | $4.4\times10^{-20}$ |
| Sílice fundida | 1.47 | $2.8\times10^{-22}$ | $3.67\times10^{-20}$ |
| CaF₂ | 1.43 | $2.24\times10^{-22}$ | $3.1\times10^{-20}$ |
| LiF | 1.4 | $1.4\times10^{-22}$ | $2.0\times10^{-20}$ |

Nota: valores de experimentos de mezcla de frecuencias, sin contribución electrostrictiva (proceso lento
que no responde a frecuencias ópticas). "El valor de $\bar n_2$ se calcula como $\bar n_2=3\pi\chi_{1111}/n_0$" (adaptado de
Hellwarth, 1977, Tablas 7.1 y 9.1). (La fila del YAG está muy tenue en el escaneo; se leyó con zoom.)

> **Dudas en la Tabla 4.3.1:** la nota da $\bar n_2=3\pi\chi_{1111}/n_0$, que es la fórmula gaussiana (en SI sería
> $3\chi/4n_0$, (4.1.11)). Con (4.1.20) el YAG daría $283\times8.4\times10^{-22}/1.83^2=7.1\times10^{-20}$ m²/W, no $8.4\times10^{-20}$; las demás filas
> sí cumplen (4.1.20) aproximadamente (diamante $1.0\times10^{-19}$, zafiro $3.7\times10^{-20}$, sílice $3.67\times10^{-20}$).

### 4.4 Nonlinearities Due to Molecular Orientation (p. 228)

Líquidos de moléculas anisótropas (tensor de polarizabilidad anisótropo) tienen $n_2$ grande: las moléculas
tienden a alinearse con el campo óptico y cambia la polarizabilidad media por molécula.

**CS₂** (Fig. 4.4.1): molécula en forma de cigarro (esferoide prolato), con
$$\alpha_3>\alpha_1 \qquad (4.4.1)$$
($\alpha_3$ paralelo al eje de simetría, $\alpha_1$ perpendicular). En un campo dc el dipolo inducido $\mathbf p$ no es paralelo a
$\mathbf E$, se desvía hacia el eje; aparece un torque
$$\boldsymbol\tau=\mathbf p\times\mathbf E \qquad (4.4.2),\ \text{p. 229}$$
que alinea la molécula; la agitación térmica se opone (factor de Boltzmann). Energía:
$$dU=-\mathbf p\cdot d\mathbf E=-p_3dE_3-p_1dE_1 \qquad (4.4.3)$$
$p_3=\alpha_3E_3$ (4.4.4), $p_1=\alpha_1E_1$ (4.4.5), $dU=-\alpha_3E_3dE_3-\alpha_1E_1dE_1$ (4.4.6),
$$U=-\tfrac12(\alpha_3E_3^2+\alpha_1E_1^2) \qquad (4.4.7)$$
Con $\theta$ ángulo entre $\mathbf E$ y el eje molecular (p. 230):
$$U=-\tfrac12[\alpha_3E^2\cos^2\theta+\alpha_1E^2\sin^2\theta]=-\tfrac12\alpha_1E^2-\tfrac12(\alpha_3-\alpha_1)E^2\cos^2\theta \qquad (4.4.8)$$
Energía menor con el eje paralelo a $\mathbf E$ (Fig. 4.4.2).

Campo óptico (luz lineal): $\tilde E^2$ tiene componentes cerca de frecuencia cero y en $2\omega$; los tiempos de
relajación orientacional son de unos pocos ps, así que la orientación responde sólo a la parte lenta:
$E^2\to\overline{\tilde E^2}$ (promedio sobre muchos ciclos).

> **Errata (p. 230):** se lee "We thus replace $E$ in Eq. (4.4.9) by…"; por consistencia debería ser Eq. (4.4.8)
> (la (4.4.9) es la del índice).

Sin campo local:
$$n^2=1+\chi=1+N\langle\alpha\rangle \qquad (4.4.9)$$
(estilo gaussiano/"polarizabilidad en unidades de volumen": sin $4\pi$ ni $\epsilon_0$). Como $\langle U\rangle=-\tfrac12|E|^2\langle\alpha\rangle$, comparando con
el promedio de (4.4.8) (p. 231):
$$\langle\alpha\rangle=\alpha_3\langle\cos^2\theta\rangle+\alpha_1\langle\sin^2\theta\rangle=\alpha_1+(\alpha_3-\alpha_1)\langle\cos^2\theta\rangle \qquad (4.4.10)$$
$$\langle\cos^2\theta\rangle=\frac{\int d\Omega\cos^2\theta\exp[-U(\theta)/kT]}{\int d\Omega\exp[-U(\theta)/kT]} \qquad (4.4.11)$$
Parámetro de intensidad
$$J=\tfrac12(\alpha_3-\alpha_1)\overline{\tilde E^2}/kT \qquad (4.4.12)$$
y con $d\Omega=2\pi\sin\theta d\theta$:
$$\langle\cos^2\theta\rangle=\frac{\int_0^\pi\cos^2\theta\exp(J\cos^2\theta)\sin\theta d\theta}{\int_0^\pi\exp(J\cos^2\theta)\sin\theta d\theta} \qquad (4.4.13)$$
Límite $J\to0$:
$$\langle\cos^2\theta\rangle_0=\frac{\int_0^\pi\cos^2\theta\sin\theta d\theta}{\int_0^\pi\sin\theta d\theta}=\tfrac13 \qquad (4.4.14)$$
$$\langle\alpha\rangle_0=\tfrac13\alpha_3+\tfrac23\alpha_1 \qquad (4.4.15)$$
$$n_0^2=1+N(\tfrac13\alpha_3+\tfrac23\alpha_1) \qquad (4.4.16)$$
(sin alineación, 1/3 del eje de simetría + 2/3 de las direcciones perpendiculares). Campo intenso:
$$n^2=1+N[\alpha_1+(\alpha_3-\alpha_1)\langle\cos^2\theta\rangle] \qquad (4.4.17)$$
$$n^2-n_0^2=N(\alpha_3-\alpha_1)\big(\langle\cos^2\theta\rangle-\tfrac13\big) \qquad (4.4.18),\ \text{p. 232}$$
Con $n^2-n_0^2\simeq2n_0(n-n_0)$:
$$n=n_0+\delta n \qquad (4.4.19)$$
$$\delta n\equiv n-n_0=\frac{N}{2n_0}(\alpha_3-\alpha_1)\big(\langle\cos^2\theta\rangle-\tfrac13\big) \qquad (4.4.20)$$
$\langle\cos^2\theta\rangle$ se expresa con la integral de Dawson. **Fig. 4.4.3:** $\langle\cos^2\theta\rangle-\tfrac13$ vs $J$ (0–20): crece casi
linealmente para $J\lesssim5$ y satura en $2/3$ (alineación completa).

Expandiendo las exponenciales (p. 233):
$$\langle\cos^2\theta\rangle=\frac13+\frac{4J}{45}+\frac{8J^2}{945}+\cdots \qquad (4.4.21)$$
$$\delta n=\frac{N}{2n_0}(\alpha_3-\alpha_1)\frac{4J}{45}=\frac{N}{45n_0}(\alpha_3-\alpha_1)^2\frac{\overline{\tilde E^2}}{kT} \qquad (4.4.22)$$
$$\delta n=\bar n_2\overline{\tilde E^2} \qquad (4.4.23)$$
$$\boxed{\bar n_2=\frac{N}{45n_0}\frac{(\alpha_3-\alpha_1)^2}{kT}} \qquad (4.4.24)$$
$\bar n_2>0$ tanto si $\alpha_3>\alpha_1$ como si $\alpha_3<\alpha_1$: el torque siempre alinea de modo que la luz vea una polarizabilidad
**mayor**.

**Campo local:** con la ley de Lorentz–Lorenz (ver (3.8.8a))
$$\frac{n^2-1}{n^2+2}=\frac13N\langle\alpha\rangle \qquad (4.4.25)$$
y $\tilde E^2$ reemplazado por el cuadrado del campo local de Lorentz (§3.8):
$$\bar n_2=\frac{N}{45n_0}\Big(\frac{n_0^2+2}{3}\Big)^4\frac{(\alpha_3-\alpha_1)^2}{kT} \qquad (4.4.26)$$
consistente con la prescripción de la §3.8: multiplicar por el factor de campo local $[(n_0^2+2)/3]^4$ de (3.8.25).

> **Errata tipográfica (p. 233):** "local-field correction factor $^{(3)}=[(n_0^2+2)/3]^4$": falta el símbolo del factor
> (debería leerse $\mathcal L^{(3)}=[(n_0^2+2)/3]^4$, como en (3.8.25)).

**Valores numéricos para CS₂ (p. 234):** máximo $\delta n$ posible = 0.58 (alineación completa). $J=1$ corresponde a
$E\simeq3\times10^9$ V/m. $\bar n_2=1.3\times10^{-11}$ esu (dígitos del exponente tenues en el escaneo). Con (4.1.18) y $n_0=1.63$ se
convierte a $n_2=3\times10^{-22}$ m²/W.

> **Duda numérica (p. 234):** $n_2=3\times10^{-22}$ m²/W es inconsistente con la Tabla 4.1.2, que para CS₂ da
> $n_2=3.2\times10^{-14}$ cm²/W $=3.2\times10^{-18}$ m²/W (y con $\chi^{(3)}=3.1\times10^{-20}$ m²/V², (4.1.20) da $3.3\times10^{-18}$ m²/W). Probablemente debería ser
> $3\times10^{-18}$ m²/W (≈ $3\times10^{-14}$ cm²/W, el valor citado en la p. 211). Además (4.1.18) relaciona $n_2$ con $\bar n_2$ en SI, no
> en esu; con esu habría que usar la conversión del apéndice.

#### 4.4.1 Tensor Properties of $\chi^{(3)}$ for the Molecular Orientation Effect (p. 234)

Close *et al.* (1966): para una molécula con tres polarizabilidades principales $a,b,c$ distintas, la
polarizabilidad media en equilibrio térmico es
$$\langle\alpha_{ij}\rangle=\alpha\delta_{ij}+\gamma_{ij} \qquad (4.4.27)$$
$$\alpha=\tfrac13(a+b+c) \qquad (4.4.28)$$
$$\gamma_{ij}=C\sum_{kl}(3\delta_{ik}\delta_{jl}-\delta_{ij}\delta_{kl})\overline{\tilde E^{\rm loc}_k(t)\tilde E^{\rm loc}_l(t)} \qquad (4.4.29)$$
$$C=\frac{(a-b)^2+(b-c)^2+(a-c)^2}{90kT} \qquad (4.4.30)$$
($\tilde E^{\rm loc}$ = campo local de Lorentz; el apéndice de la sección lo deriva para molécula axialmente simétrica;
el caso general queda como ejercicio, Problema 5). Sin campo local, $\tilde E_k(t)=E_ke^{-i\omega t}+$c.c. (4.4.31), y
$$\overline{\tilde E^{\rm loc}_k(t)\tilde E^{\rm loc}_l(t)}=E_kE_l^*+E_k^*E_l \qquad (4.4.32)$$
Polarización (p. 235):
$$P_i=\epsilon_0\sum_jN\langle\alpha_{ij}\rangle E_j \qquad (4.4.33)$$
$$P_i^{(3)}=\epsilon_0N\sum_j\gamma_{ij}E_j \qquad (4.4.34)$$
$$P_i^{(3)}=\epsilon_0NC\sum_{jkl}(3\delta_{ik}\delta_{jl}-\delta_{ij}\delta_{kl})(E_kE_l^*+E_k^*E_l)E_j$$
$$\mathbf P^{(3)}=\epsilon_0NC[3(\mathbf E\cdot\mathbf E^*)\mathbf E+3(\mathbf E\cdot\mathbf E)\mathbf E^*-(\mathbf E\cdot\mathbf E^*)\mathbf E-(\mathbf E\cdot\mathbf E^*)\mathbf E]=\epsilon_0NC[(\mathbf E\cdot\mathbf E^*)\mathbf E+3(\mathbf E\cdot\mathbf E)\mathbf E^*] \qquad (4.4.35)$$
En notación de Maker–Terhune:
$$\mathbf P^{(3)}=\epsilon_0A(\mathbf E\cdot\mathbf E^*)\mathbf E+\tfrac12\epsilon_0B(\mathbf E\cdot\mathbf E)\mathbf E^* \qquad (4.4.36)$$
$$B=6A=6NC\ \Rightarrow\ B=6A=N\left[\frac{(a-b)^2+(b-c)^2+(a-c)^2}{15kT}\right] \qquad (4.4.37)$$
Se confirma $B/A=6$ (4.2.13a). Con campo local:
$$B=6A=\Big(\frac{n_0^2+2}{3}\Big)^4N\left[\frac{(a-b)^2+(b-c)^2+(a-c)^2}{15kT}\right] \qquad (4.4.38)$$

### 4.5 Thermal Nonlinear Optical Effects (p. 235)

Efectos grandes y a menudo indeseados: parte de la potencia se absorbe, sube la temperatura y cambia el
índice. En gases el índice siempre disminuye con $T$ (a presión constante); en materia condensada puede
aumentar o disminuir. Escalas de tiempo largas (orden de segundos) → fenómenos fuertemente dependientes
del tiempo (p. 236). Modelo:
$$\tilde n=n_0+\Big(\frac{dn}{dT}\Big)\tilde T_1 \qquad (4.5.1)$$
($\tilde T_1$ = cambio de temperatura inducido; la tilde indica dependencia explícita en el tiempo) con la ecuación de
transporte de calor
$$(\rho_0C)\frac{\partial\tilde T_1}{\partial t}-\kappa\nabla^2\tilde T_1=\alpha\tilde I(r) \qquad (4.5.2)$$
$(\rho_0C)$ = capacidad calorífica por unidad de volumen ($\rho_0$ densidad, $C$ calor específico por masa), $\kappa$
conductividad térmica, $\alpha$ coeficiente de absorción lineal. Los efectos térmicos son **no locales** (el cambio
de índice en un punto depende de la intensidad en puntos vecinos).

**Tabla 4.5.1 — Propiedades térmicas (p. 237).**

| Material | $(\rho_0C)$ (J/cm³) | $\kappa$ (W/m K) | $dn/dT$ (K⁻¹) |
|---|---|---|---|
| Diamante | 1.76 | 660 | — |
| Etanol | 1.91 | 0.168 | — |
| Sílice fundida | 1.67 | 1.4 | $1.2\times10^{-5}$ |
| Cloruro de sodio | 1.95 | 6.4 | $-3.6\times10^{-5}$ |
| Agua (líquida) | 4.2 | 0.56 | — |
| Aire | $1.2\times10^{-3}$ | $26\times10^{-3}$ | $-1.0\times10^{-6}$ |

Notas: listados más amplios en el *CRC Handbook of Chemistry and Physics* (Sección D) y el *AIP Handbook*
(Sección 4). $dn/dT$ puede ser positivo o negativo; para materia condensada típicamente en $\pm3\times10^{-5}$ K⁻¹ (AIP
Handbook, 6b). Aire: $C$ a presión constante, valores a STP; $(\rho_0C)\propto$ densidad, $\kappa$ independiente de la densidad
y para todo gas ideal $dn/dT=-(n-1)/T$.

**Geometría (Fig. 4.5.1):** haz circular de intensidad $I_0$, radio $R$, potencia $P=\pi R^2I_0$ (o energía $Q$) sobre una
placa de espesor $L$ y absorción $\alpha$.

**Tiempo de respuesta:** con $\partial\tilde T_1/\partial t\to T_1/\tau$ y $\nabla^2\tilde T_1\to T_1/R^2$: $(\rho_0C)T_1/\tau\approx\kappa T_1/R^2$,
$$\tau\approx\frac{(\rho_0C)R^2}{\kappa} \qquad (4.5.3)$$
Con $(\rho_0C)=10^6$ J/m³ K, $\kappa=1$ W/m K, $R=1$ mm: $\tau\approx1$ s; con $R=10$ μm, $\tau\approx100$ μs. Mucho mayor que la duración de
casi todos los pulsos: para CW importa la potencia (o intensidad); para pulsos importa la energía $Q=PT$ (o
la fluencia) (p. 237–238).

#### 4.5.1 Thermal Nonlinearities with Continuous-Wave Laser Beams (p. 238)

Estado estacionario:
$$-\kappa\nabla^2\tilde T_1=\alpha\tilde I(r) \qquad (4.5.4)$$
Con $\nabla^2\tilde T_1\to-T_1^{\rm (max)}/R^2$:
$$T_1^{\rm (max)}=\frac{\alpha I^{\rm (max)}R^2}{\kappa} \qquad (4.5.5)$$
$$\Delta n=\Big(\frac{dn}{dT}\Big)\frac{\alpha I^{\rm (max)}R^2}{\kappa} \qquad (4.5.6)$$
Definiendo $\Delta n=n_2^{\rm (th)}I^{\rm (max)}$:
$$n_2^{\rm (th)}=\Big(\frac{dn}{dT}\Big)\frac{\alpha R^2}{\kappa} \qquad (4.5.7)$$
Depende de la geometría ($R^2$), no es propiedad intrínseca, pero cuantifica el efecto. Con $dn/dT=10^{-5}$ K⁻¹,
$\alpha=1$ cm⁻¹, $R=1$ mm, $\kappa=1$ W/m K: $n_2^{\rm (th)}=10^{-5}$ cm²/W (frente a $n_2=3\times10^{-16}$ cm²/W de la sílice). Aun con $R=10$ μm y
$\alpha=0.01$ cm⁻¹: $n_2^{\rm (th)}=10^{-11}$ cm²/W. **Conclusión:** los efectos térmicos suelen ser el mecanismo no lineal dominante
con haces CW (p. 239). Análisis: Bespalov *et al.* (1989), Hoffman (1986), Martin y Hellwarth (1979),
Tochio *et al.* (1981); en gases, Bentley *et al.* (2000).

#### 4.5.2 Thermal Nonlinearities with Pulsed Laser Beams (p. 239)

Para pulsos el cambio es proporcional a la energía $Q=\int\tilde P(t)dt$ (o fluencia $F=\int\tilde I(t)dt$), no a la potencia: no se
puede describir con $n_2^{\rm (th)}$; $\Delta\tilde n$ crece (o decrece) monótonamente durante el pulso. Criterio: cuándo
$$\Delta n^{\rm (th)}=\Big(\frac{dn}{dT}\Big)T_1^{\rm (max)} \qquad (4.5.8)$$
supera a
$$\Delta n^{\rm (el)}=n_2^{\rm (el)}I \qquad (4.5.9)$$
Para $t_p\ll\tau$ se desprecia la difusión:
$$(\rho_0C)\frac{\partial\tilde T_1}{\partial t}=\alpha\tilde I(r) \qquad (4.5.10)$$
$$T_1^{\rm (max)}=\frac{\alpha I^{\rm (max)}t_p}{(\rho_0C)} \qquad (4.5.11)$$
El térmico domina si (p. 240)
$$t_p\geq\frac{n_2^{\rm (el)}(\rho_0C)}{(dn/dT)\alpha} \qquad (4.5.12)$$
Con $n_2^{\rm (el)}=3\times10^{-16}$ cm²/W, $(\rho_0C)=1\times10^6$ J/m³ K, $dn/dT=1\times10^{-5}$ K⁻¹, $\alpha=1$ cm⁻¹:
$$t_p\geq30\ \text{ps} \qquad (4.5.13)$$
Los efectos térmicos contribuyen para todos salvo los pulsos más cortos ($t_p\ll30$ ps).

### 4.6 Semiconductor Nonlinearities (p. 240)

Importancia: respuestas grandes e integración (electrónica, láseres y componentes no lineales en un mismo
sustrato). Bandas de valencia (llenas) y de conducción (vacías) separadas por $E_g$ (Fig. 4.6.1). Distinción
crucial: $\hbar\omega>E_g$ (transferencia real de electrones a la banda de conducción, respuesta lenta) vs
$\hbar\omega<E_g$ (respuesta esencialmente instantánea por procesos paramétricos vía niveles virtuales).

#### 4.6.1 Nonlinearities Resulting from Band-to-Band Transitions (p. 241)

Población de la banda de conducción:
$$\frac{dN_c}{dt}=\frac{\alpha I}{\hbar\omega}-\frac{(N_c-N_c^{(0)})}{\tau_R} \qquad (4.6.1)$$
($\alpha$ absorción a la frecuencia del láser, $N_c^{(0)}$ población de equilibrio, $\tau_R$ tiempo de recombinación
electrón‑hueco). Estacionario:
$$N_c=N_c^{(0)}+\frac{\alpha I\tau_R}{\hbar\omega} \qquad (4.6.2)$$
Si el pulso es más corto que $\tau_R$, $N_c$ crece monótonamente durante el pulso. Mecanismos:

**Respuesta de electrones libres** (ver (13.7.3)):
$$\epsilon(\omega)=\epsilon_b-\frac{\omega_p^2}{\omega(\omega+i/\tau)} \qquad (4.6.3)$$
$\epsilon_b$ = contribución de las cargas ligadas, $\omega_p^2=N_ce^2/\epsilon_0m$, $\tau$ tiempo de respuesta óptico (≠ $\tau_R$, típicamente
mucho menor). $\epsilon$ disminuye con la intensidad. En estado estacionario (Problema 11), $n=n_0+n_2I$ con (p. 242)
$$n_0^2=\epsilon_b-\frac{N_c(0)e^2}{\epsilon_0m\omega(\omega+i/\tau)} \qquad (4.6.4)$$
$$n_2=-\frac{e^2\alpha\tau_R}{2\epsilon_bn_0m\hbar\omega^3} \qquad (4.6.5)$$
$n_2\propto\omega^{-3}$: domina a longitudes de onda largas. Con $m=0.1m_e$ (masa efectiva), $n_0=3.5$, $\alpha=10^4$ cm⁻¹,
$\hbar\omega=0.75$ eV, $\tau_r=10$ ns: $n_2=3\times10^{-10}$ m²/W.

> **Erratas menores (p. 242):** "bound changes" debería ser "bound charges"; el tiempo se escribe $\tau_r$ en el
> ejemplo y $\tau_R$ en la fórmula (es el mismo). Duda: en (4.6.5) aparece $\epsilon_b$ en el denominador además de $n_0$ y
> $\epsilon_0$ no aparece; dimensionalmente $e^2\alpha\tau_R/(m\hbar\omega^3)$ tiene unidades de C²·m⁻¹·s/(kg·J·s⁻³); para obtener m²/W hace falta
> un $\epsilon_0$ en el denominador. Por consistencia con (4.6.4) debería leerse $n_2=-e^2\alpha\tau_R/(2\epsilon_0n_0m\hbar\omega^3)$ (se transcribe tal
> cual se lee, $\epsilon_b$).

**Apantallamiento por plasma:** el material se vuelve débilmente conductor y la interacción de Coulomb se
debilita. Límite clásico (Maxwell–Boltzmann):
$$V=\frac{e^2}{4\pi\epsilon_0\epsilon r}e^{-\kappa r} \qquad (4.6.6)$$
$$\kappa=\sqrt{\frac{N_ce^2}{\epsilon_0kT}} \qquad (4.6.7)$$
(número de onda de apantallamiento de Debye–Hückel; $\epsilon$ = constante dieléctrica real). Consecuencia: los
excitones pueden desaparecer a alta densidad de electrones. Niveles excitónicos (p. 243):
$$E_n=E_c-R^*/n^2 \qquad (4.6.8)$$
$R^*=\hbar^2(2m_ra_0^{*2})^{-1}$ (Rydberg efectivo), $m_r$ masa reducida, $a_0^*=4\pi\epsilon_0\hbar^2(m_re^2)^{-1}$ radio de Bohr efectivo.
**Fig. 4.6.2:** absorción del Cu₂O a 4.2 K, picos 2p, 3p, 4p, 5p entre 2145 y 2170 meV, $\alpha$ de 200 a 400 cm⁻¹
(Tayagaki *et al.*, 1995). **Fig. 4.6.3:** (a) espectro con pico excitónico bajo el borde de banda; (b) con
electrones excitados el excitón desaparece; (c) el cambio de índice asociado, dispersivo. Kramers–Kronig:
$$\Delta n(\omega)=\frac c\pi\int_0^\infty\frac{\Delta\alpha(\omega')d\omega'}{\omega'^2-\omega^2} \qquad (4.6.9)$$
(valor principal). $\Delta n>0$ del lado de alta frecuencia de la resonancia excitónica, $<0$ del lado bajo; sólo
apreciable cerca de la resonancia (p. 244).

**Llenado de bandas:** al pasar electrones a la banda de conducción la absorción disminuye (análogo a la
saturación atómica del cap. 6, pero con el principio de Pauli → rango de energías). Baja el índice por
debajo del borde y lo sube por encima (mismo sentido que un átomo de dos niveles). Cálculo por
Kramers–Kronig: Peyghambarian *et al.* (1993, §13‑4) (p. 245).

**Renormalización del gap:** por razones sutiles (intercambio y correlaciones de Coulomb) $E_g$ disminuye a
altas concentraciones de electrones de conducción.

#### 4.6.2 Nonlinearities Involving Virtual Transitions (p. 245)

$\hbar\omega<E_g$ (Fig. 4.6.4): no hay absorción de un fotón; procesos virtuales de "dos fotones" (b), en general
mucho más fuertes que los de "un fotón" (c) salvo cerca de $E_g$. Modelo de Sheik‑Bahae *et al.* (1990, 1991)
(dos bandas parabólicas; detalles de teoría de bandas fuera del alcance). Con $\Delta n=n_2I$ (p. 246):
$$n_2=K\frac{\hbar c\sqrt{E_p}}{2n_0^2E_g^4}G_2(\hbar\omega/E_g) \qquad (4.6.10)$$
$E_p=21$ eV; $K$ parámetro libre, empíricamente $3.1\times10^3$ en unidades con $E_p$, $E_g$ en eV y $n_2$ en cm²/W;
$$G_2(x)=\frac{-2+6x-3x^2-x^3-\frac34x^4-\frac34x^5+2(1-2x)^{3/2}\Theta(1-2x)}{64x^6} \qquad (4.6.11)$$
($\Theta$ = escalón de Heaviside). Absorción de dos fotones, $\alpha=\alpha_0+\beta I$:
$$\beta=\frac{K\sqrt{E_p}}{n_0^2E_g^3}F_2(2\hbar\omega/E_g) \qquad (4.6.12)$$
$$F_2(2x)=\frac{(2x-1)^{3/2}}{(2x)^5}\quad\text{para }2x>1 \qquad (4.6.13)$$
y $F_2=0$ en otro caso. **Fig. 4.6.5 (p. 247):** $F_2$ y $G_2$ vs $x=\hbar\omega/E_g$ (0–1): la TPA se anula para $\hbar\omega<E_g/2$
(energía); **$n_2$ tiene un pico en $\hbar\omega/E_g\approx0.54$, se anula en $\approx0.69$ y es negativo para $\hbar\omega/E_g\gtrsim0.69$**. $n_2\propto E_g^{-4}$:
semiconductores de gap estrecho dan respuestas mucho mayores. **Fig. 4.6.6 (p. 248):** $n_2n_0/K'G_2$ vs $E_g$
(log‑log, 0.5–20 eV, $10^{-5}$–10) con datos de Ge, CdTe, ZnSe, CdS₀.₃Se₀.₅, CdS, ZnTe, ZnS, AgCl, SBN, ZnO,
NaBr, KCl, NaCl, CaCO₃, KDP, KF, MgF₂, KBr, MgO, Al₂O₃, SiO₂, BaF₂, SrF₂, CaF₂, LiF₂ sobre la recta del
modelo: muy buen acuerdo.

Ambos mecanismos (lento banda‑banda e instantáneo) coexisten; Said *et al.* (1992):
$$\Delta n=n_2I+\sigma_rN_c \qquad (4.6.14)$$
($\sigma_r$ = cambio de índice por unidad de densidad de electrones de conducción).

**Tabla 4.6.1 — Coeficientes no lineales de semiconductores (Said *et al.*, 1992), p. 247.**

| Semiconductor | $\beta$ (m/TW) | $n_2$ (m²/W) | $\sigma_r$ (m³) |
|---|---|---|---|
| ZnSe a 532 nm | 58 | $-6.8\times10^{-18}$ | $-0.8\times10^{-27}$ |
| GaAs a 1064 nm | 260 | $-4.1\times10^{-17}$ | $-6.5\times10^{-27}$ |
| CdTe a 1064 nm | 260 | $-3\times10^{-17}$ | $-5\times10^{-27}$ |
| ZnTe a 1064 nm | 42 | $1.2\times10^{-17}$ | $-0.75\times10^{-27}$ |

### 4.7 Concluding Remarks (p. 247)

Se asumió $\Delta n=n_2I$ monótono, pero hay un cambio máximo observable por saturación o por daño láser.
Récord citado: $\Delta n_{\rm max}=0.14$ (Brzozowski *et al.*, 2003) en pozos cuánticos múltiples InGaAs/InAlGaAs a
≈1500 nm con fluencia de 116 μJ/cm² (p. 248).

Susceptibilidad adimensional (Kok *et al.*, 2002):
$$\chi^{(3)}_D=E^2_{1,\max}\chi^{(3)} \qquad (4.7.1)$$
$E^2_{1,\max}$ = máximo campo que produce un solo fotón en espacio libre; localizando el pulso en un volumen $\sim\lambda^3$:
$$\frac{\hbar\omega}{\lambda^3}=2\epsilon_0E^2_{1,\max} \qquad (4.7.2)$$
$$\chi^{(3)}_D=\frac{\hbar\omega}{2\epsilon_0\lambda^3}\chi^{(3)} \qquad (4.7.3),\ \text{p. 249}$$
Sílice fundida ($\chi^{(3)}=2.5\times10^{-22}$), $\lambda=1.0$ μm: $\chi^{(3)}_D=4.5\times10^{-13}$. Las interacciones no resonantes son
extremadamente débiles a escala local; sólo el efecto acumulado sobre grandes distancias produce campos
intensos. Para las no linealidades más grandes (condensado de Bose–Einstein de la Tabla 4.1.2) $\chi^{(3)}_D\approx100$.

> **Erratas/dudas (p. 249):** (i) las unidades de $\chi^{(3)}$ de la sílice se leen "m²/W²"; deberían ser m²/V².
> (ii) Recalculando (4.7.3): $\hbar\omega=hc/\lambda=1.99\times10^{-19}$ J, $2\epsilon_0\lambda^3=1.77\times10^{-29}$ F·m², cociente $1.12\times10^{10}$ V²/m²; por
> $2.5\times10^{-22}$ m²/V² da $\chi^{(3)}_D\approx2.8\times10^{-12}$, no $4.5\times10^{-13}$ (factor ≈ 6 ≈ 2π de diferencia; quizá se usó $\hbar\omega$ con
> $\omega=c/\lambda$ en vez de $2\pi c/\lambda$). Verificar antes de citar el número.

---

## Tablas y datos numéricos útiles

- Conversión clave: $n_2=\dfrac{3\chi^{(3)}}{4n_0^2\epsilon_0c}$, $n_2[\mathrm{m^2/W}]=283\chi^{(3)}[\mathrm{m^2/V^2}]/n_0^2$; $n_2[\mathrm{cm^2/W}]=0.0395\chi^{(3)}[\mathrm{esu}]/n_0^2$; $n_2=\bar n_2/(n_0\epsilon_0c)$;
  $\bar n_2=3\chi^{(3)}/4n_0$; acción cruzada $\bar n_2^{\rm (cross)}=2\bar n_2$; $1$ cm²/W $=10^{-4}$ m²/W.
- Mecanismos y tiempos (Tabla 4.1.1): electrónico $10^{-15}$ s (estimación de Bohr $10^{-16}$ s), orientación $10^{-12}$ s
  (CS₂: $\tau=2$ ps), electrostricción $10^{-9}$ s, absorción saturada $10^{-8}$ s, térmico $10^{-3}$ s (estimación
  $\rho_0CR^2/\kappa$: 1 s para $R=1$ mm, 100 μs para $R=10$ μm).
- Isótropo: $\chi_{1111}=\chi_{1122}+\chi_{1212}+\chi_{1221}$; $A=6\chi_{1122}$, $B=6\chi_{1221}$; $\delta n_{\rm lin}=(A+B/2)|E|^2/2n_0=3\chi_{1111}|E|^2/2n_0$;
  $\delta n_{\rm circ}=A|E|^2/2n_0$; $B/A$ = 6 (orientación), 1 (electrónica, Kleinman), 0 (electrostricción).
- Valores relevantes para el proyecto (Tabla 4.1.2): **Si** $n_0=3.4$, $\chi^{(3)}=2.8\times10^{-18}$ m²/V² (de THG), $n_2=2.7\times10^{-14}$ cm²/W
  $=2.7\times10^{-18}$ m²/W; **sílice fundida** $n_0=1.47$, $n_2=3.2\times10^{-16}$ cm²/W $=3.2\times10^{-20}$ m²/W (Tabla 4.3.1: $3.67\times10^{-20}$ m²/W);
  **agua** $n_0=1.33$, $n_2=4.1\times10^{-16}$ cm²/W. El libro **no** da valores para Si₃N₄.
- Térmico: $n_2^{\rm (th)}=(dn/dT)\alpha R^2/\kappa$; sílice $dn/dT=1.2\times10^{-5}$ K⁻¹, $\kappa=1.4$ W/m K, $\rho_0C=1.67$ J/cm³; agua
  $\kappa=0.56$ W/m K, $\rho_0C=4.2$ J/cm³.
- Semiconductores (Sheik‑Bahae): $n_2\propto G_2(\hbar\omega/E_g)/(n_0^2E_g^4)$, pico en $\hbar\omega/E_g\approx0.54$, cambio de signo en 0.69; TPA sólo si
  $\hbar\omega>E_g/2$, $\beta\propto F_2/(n_0^2E_g^3)$.

---

## Problemas (p. 249–251)

1. ***$n_2$ for a lossy medium.*** Generalizar la derivación de (4.1.19) para permitir que el índice lineal sea
   complejo $\bar n_0$. [Resp.: reemplazar $n_0^2$ del denominador de (4.1.19) por $\bar n_0\,\mathrm{Re}\,\bar n_0$.]
2. ***Tensor properties of $\chi^{(3)}$ for an isotropic medium.*** Derivar las ecuaciones (4.2.2).
3. ***Ellipse rotation.*** Una muestra de 1 cm de disulfuro de carbono se ilumina con luz elípticamente
   polarizada de intensidad $I=1$ MW/cm². Determinar cómo depende el ángulo de rotación de la elipse de la
   elipticidad, y calcular numéricamente el valor máximo del ángulo. Cuantificar la elipticidad con el
   parámetro $\delta$ ($-1\le\delta\le1$) que define el vector unitario de polarización
   $\hat{\boldsymbol\epsilon}=(\hat{\mathbf x}+i\delta\hat{\mathbf y})/(1+\delta^2)^{1/2}$. [Pista: la respuesta de tercer orden del CS₂ se debe
   principalmente a la orientación molecular.]
4. ***Sign of $\chi^{(3)}$.*** Verificar la afirmación del texto de que el primer término de (4.3.12) es positivo
   siempre que $\omega$ sea menor que toda frecuencia de resonancia del sistema atómico.
5. ***Tensor properties of the molecular orientation effect.*** Derivar (4.4.27)–(4.4.30) para el caso general en
   que $a$, $b$ y $c$ son todos distintos. [Este problema es extremadamente difícil.]
6. ***Thermal nonlinearities.*** En la §4.5 se usó análisis dimensional; aquí la ecuación de transporte de calor
   se resuelve exactamente. Un haz de diámetro $D_1$ y potencia $P$ se propaga por una varilla larga de vidrio
   de diámetro $D_2$, cuya superficie exterior se mantiene a $T_0$. Estado estacionario y perfil transversal de
   intensidad uniforme. Determinar la temperatura local $T$ en cada punto de la varilla y el máximo cambio
   de índice. Evaluar numéricamente para condiciones realistas.
7. ***Nonlinearity due to the magnetic force.*** Onda plana sobre un electrón libre; si el campo es intenso, la
   fuerza magnética $\mathbf F_M=(-e/c)\mathbf v\times\mathbf B$ (forma gaussiana) afecta su movimiento — una fuente de respuesta
   electrónica no lineal.
   (a) Mostrar que para $\mathbf E=\hat{\mathbf x}(E_0e^{i(kz-\omega t)}+$c.c.$)$ la fuerza electromagnética es
   $\mathbf F_{EM}=-e(E_0e^{-i\omega t}+\text{c.c.})\big[\hat{\mathbf x}\big(1-\frac{\dot z}{c}\big)+\hat{\mathbf z}\big(\frac{\dot x}{c}\big)\big]$. ¿Qué tan grande (orden de magnitud) puede ser
   $\dot x/c$ para un electrón libre en un haz de intensidad pico $10^{17}$ W/cm²?
   (b) Derivar $\chi^{(2)}(2\omega)$ y $\chi^{(2)}(0)$ para un conjunto de electrones libres en función de la densidad $N$
   (sin fuerzas "friccionales"). ¿En qué dirección(es) se emite la luz a $2\omega$?
   (c) Derivar $\chi^{(3)}(\omega)$ y $\chi^{(3)}(3\omega)$.
   (d) Los buenos conductores se modelan como electrones libres. Suponiendo que la fuerza magnética es la
   única fuente de no linealidad, estimar el orden de magnitud de $\chi^{(3)}(\omega)$ para el oro.
8. ***Nonlinear phase shift of a focused gaussian beam.*** Derivar la fase no lineal de un haz gaussiano
   enfocado de cintura $w_0$ y potencia $\mathcal P$ al atravesar un material con $n_2$, integrando la intensidad en el eje
   de $z=-\infty$ a $z=+\infty$. Comentar la exactitud del método y especular sobre métodos computacionales más
   precisos.
9. ***Nonlinear phase shift of a focused gaussian beam.*** Suponiendo válido el procedimiento anterior,
   determinar numéricamente la fase no lineal que puede obtener un haz gaussiano enfocado en vidrio óptico
   con la potencia justo bajo el umbral de daño. Suponer primero una placa de 1 cm, y describir cómo escala
   la fase con el espesor. Cintura en el centro del bloque; el daño de volumen (no de superficie) es el
   limitante. Tomar $I(\text{daño})=10$ GW/cm².
10. ***Nonlinear phase shift of a focused gaussian beam.*** Igual al anterior, pero el daño de superficie es el
    proceso limitante.
11. ***Semiconductor nonlinear response.*** Derivar (4.6.5).

---

## Referencias principales (p. 251–252)

- Generales: Bloembergen (1964) *Nonlinear Optics*; Chase y Van Stryland (1995) *CRC Handbook of Laser
  Science and Technology*, §8.1; Chiao, Kelley, Garmire (1966) PRL 17, 1158 (weak‑wave retardation); Close
  *et al.* (1966) IEEE JQE 2, 553; Hellwarth (1977) Prog. Quantum Electron. 5, 1–68 (medidas de $\chi^{(3)}$);
  Hanna, Yuratich, Cotter (1979); Orr y Ward (1971) Mol. Phys. 20, 513; Sutherland (1996) *Handbook of
  Nonlinear Optics*, cap. 8; Euler y Kockel (1935) (no linealidad del vacío); Hau *et al.* (1999) Nature 397,
  594 (EIT en BEC).
- Tensor: Butcher (1965); Maker y Terhune (1965) Phys. Rev. A137, 801; Maker, Terhune, Savage (1964) PRL 12,
  507; Saikan y Kiguchi (1982) Opt. Lett. 7, 555; Gaeta *et al.* (1987) PRL 58, 2432; Gauthier *et al.* (1988,
  1990).
- Térmicos: Bentley *et al.* (2000) Opt. Lett. 25, 1192; Bespalov *et al.* (1989); Hoffman (1986) JOSA B 3, 253;
  Martin y Hellwarth (1979) APL 34, 371; Tochio *et al.* (1981).
- Semiconductores: Peyghambarian, Koch, Mysyrowicz (1993) *Introduction to Semiconductor Optics*; Said *et al.*
  (1992) JOSA B 9, 405; **Sheik‑Bahae, Hagan, Van Stryland (1990) PRL 65, 96**; Sheik‑Bahae *et al.* (1991) IEEE
  JQE 27, 1296; Tayagaki *et al.* (1995). Lecturas: Butcher y Cotter (1990) cap. 8; Weber (1995) CRC
  Handbook Suppl. 2.
- Comentarios finales: Brzozowski *et al.* (2003) APL 82, 4429; Kok, Lee, Dowling (2002) PRA 66, 063814.

---

## Relación con Óptica No Lineal

- **Tema 6 del programa (Boyd 4.1, 4.2, 7.1, 7.2).** Las §4.1 y §4.2 son materia directa: definiciones $\bar n_2$ y
  $n_2$ y su relación con $\chi^{(3)}$ ((4.1.11), (4.1.19), (4.1.20)); factor de degeneración 3 vs 6 y $\bar n_2^{\rm (cross)}=2\bar n_2$
  (base de la XPM: la sonda ve el doble); Tabla 4.1.1 de mecanismos con tiempos de respuesta; Tabla 4.1.2
  de valores; forma isótropa del tensor (4.2.3); coeficientes $A$, $B$ (4.2.10); rotación no lineal de la
  elipse (4.2.24)–(4.2.26) y $\delta n_{\rm lin}/\delta n_{\rm circ}=1+B/2A$. El cap. 7 (autoenfoque, SPM) usa $n=n_0+n_2I$ tal cual.
- **Equivalencias con Saleh (ver `notas/saleh/cap21-optica-no-lineal.md`):** el $n_2$ en m²/W de Boyd (4.1.19) es
  idéntico al de Saleh (21.3-6); Saleh usa $\chi^{(3)}_{\rm S}=\epsilon_0\chi^{(3)}_{\rm B}/4$. Ojo con tablas que usan la definición de
  $\chi^{(3)}$ "cuatro veces menor" (nota a de la Tabla 4.1.2) y con $\bar n_2$ vs $n_2$.
- **Tema 4 (Boyd cap. 1):** (4.3.2)–(4.3.4) aplican el oscilador anarmónico de la §1.4 y dan el orden de
  magnitud $\chi^{(3)}\sim3\times10^{-22}$ m²/V²; la simetría de Kleinman ($A=B$) conecta con §1.5.

## Relación con el proyecto final (supercontinuo / no linealidades en guías de SiN y Si)

- **Si:** la Tabla 4.1.2 da $n_2=2.7\times10^{-14}$ cm²/W $=2.7\times10^{-18}$ m²/W (de $|\chi^{(3)}|$ por THG, Bloembergen *et al.* 1969); valores
  modernos a 1550 nm son del orden de $(4$–$6)\times10^{-18}$ m²/W (fuera del libro, comprobar en la bibliografía del
  proyecto). Con $E_g\approx1.12$ eV, a 1550 nm ($\hbar\omega=0.80$ eV) $\hbar\omega/E_g\approx0.71>0.5$: **hay TPA** ($F_2\neq0$) y, según el modelo de
  dos bandas, $G_2$ estaría cerca del cambio de signo (el modelo es para gap directo; el Si es indirecto, así que
  sólo orientativo). La TPA genera portadores libres → (4.6.1)–(4.6.5): absorción y refracción por portadores
  libres (FCA/FCD), con $n_2^{\rm FC}<0$ y lenta ($\tau_R$) — el mecanismo que limita el SC en Si en el NIR.
- **SiN (Si₃N₄):** $E_g\approx5$ eV ⇒ $\hbar\omega/E_g\approx0.16$ a 1550 nm: sin TPA, $G_2$ pequeño y positivo; por el escalamiento
  $n_2\propto E_g^{-4}$ se espera un $n_2$ ≈ 10× el de la sílice (el libro no lo tabula; valor de literatura $\approx2.4\times10^{-19}$ m²/W).
  Respuesta electrónica no resonante, $\tau\sim$ fs: apta para SPM/SC de pulsos ultracortos.
- **Efectos térmicos:** para CW o pulsos largos el $n_2^{\rm (th)}$ domina (4.5.7), (4.5.13). Relevante para el anillo
  sensor (autodesplazamiento térmico de la resonancia, biestabilidad térmica en microanillos) y para el
  analito acuoso (agua: $\kappa=0.56$ W/m K, absorbe en el NIR). Para el refractómetro de volumen (1.33→1.37) el
  Kerr electrónico es despreciable con potencias de sondeo bajas, pero el térmico puede no serlo.
- **Polarización:** en guías de SiN/Si los modos TE/TM son casi lineales, así que vale $\delta n_{\rm lin}=3\chi_{1111}|E|^2/2n_0$;
  con $B/A=1$ (electrónico) la XPM entre polarizaciones ortogonales vale 2/3 de la de copolarizadas
  (de (4.2.5): $\chi_{1122}+\chi_{1212}=2\chi_{1111}/3$), resultado estándar que Agrawal usa en fibras.

## Erratas y dudas de lectura (resumen)

1. Nota a, Tabla 4.1.2 (p. 213): "$n_2=12\pi^2\chi^{(3)}/n_0^2$" — forma gaussiana incompleta; en SI usar (4.1.19)/(4.1.20).
2. (4.2.12a), p. 216: sobran los $\epsilon_0$ en $\chi^{\rm (eff)}_{ij}$.
3. (4.3.14), p. 227: en la suma sobre $l,n$ aparece $(\omega_{mg}-\omega)$; debería ser $(\omega_{lg}-\omega)$.
4. Tabla 4.3.1, p. 228: nota con $\bar n_2=3\pi\chi_{1111}/n_0$ (gaussiana); fila YAG ($8.4\times10^{-20}$ m²/W) no cumple (4.1.20) (daría $7.1\times10^{-20}$).
5. p. 230: "replace $E$ in Eq. (4.4.9)" → debería ser (4.4.8).
6. p. 233: falta el símbolo del factor de campo local ($\mathcal L^{(3)}$).
7. p. 234: CS₂ $n_2=3\times10^{-22}$ m²/W, inconsistente con la Tabla 4.1.2 ($3.2\times10^{-18}$ m²/W); probablemente $3\times10^{-18}$.
8. p. 242: "bound changes" → "bound charges"; $\tau_r$/$\tau_R$; (4.6.5) parece requerir $\epsilon_0$ en lugar de (o además de) $\epsilon_b$.
9. p. 249: unidades "m²/W²" → m²/V²; el valor $\chi^{(3)}_D=4.5\times10^{-13}$ no se reproduce con (4.7.3) (da $\approx2.8\times10^{-12}$).
10. §4.4 y Problema 7 usan fórmulas en estilo gaussiano ($n^2=1+N\alpha$, $\mathbf F=(-e/c)\mathbf v\times\mathbf B$, $\bar n_2$ en esu).
