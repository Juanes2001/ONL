# Tarea 1 — Punto 3: razón entre 2.º y 3.er armónico (serie de Taylor)

**Enunciado.** En el problema 2b, estimar la relación de amplitud entre el segundo y tercer
armónico considerando los términos cuadrático y cúbico de la serie de Taylor de la función de
transferencia, y comparar con los resultados obtenidos en 2b.

Código: `punto3.m`. Figura: `figuras/punto3_taylor_vs_exacto.png`.

## Parámetros

| Magnitud | Valor |
|---|---|
| Corriente de saturación inversa, i₀ | 10 pA |
| Voltaje térmico, V_T = kT/e | 26 mV |
| Polarización DC, V₀ | 0.3 V |
| Amplitud de la señal, V₁ | 0.2 V |
| Frecuencia, f | 50 Hz (ω = 2π·50 rad/s) |
| Parámetro adimensional, x = V₁/V_T | 7.6923 |

## Derivación

**1. Punto de expansión.** La señal oscila alrededor de V₀, así que la función de transferencia
se expande en torno al punto de operación. Se define u(t) = v(t) − V₀ = V₁ cos ωt:

$$ i = i_0\left[e^{(V_0+u)/V_T} - 1\right] = I_s\, e^{u/V_T} - i_0, \qquad I_s \equiv i_0 e^{V_0/V_T} = 1.0259\ \mu\text{A}. $$

**2. Serie de Taylor hasta orden 3:**

$$ e^{u/V_T} \approx 1 + \frac{u}{V_T} + \frac{1}{2}\left(\frac{u}{V_T}\right)^2 + \frac{1}{6}\left(\frac{u}{V_T}\right)^3 . $$

Con u/V_T = x cos ωt:

$$ i \approx I_s\left[1 + x\cos\omega t + \frac{x^2}{2}\cos^2\omega t + \frac{x^3}{6}\cos^3\omega t\right] - i_0 . $$

**3. Linealización de las potencias del coseno:**

$$ \cos^2\omega t = \tfrac12\left(1 + \cos 2\omega t\right), \qquad
   \cos^3\omega t = \tfrac14\left(3\cos\omega t + \cos 3\omega t\right). $$

**4. Agrupación por frecuencia:**

| Componente | Amplitud (Taylor, orden 3) | Origen |
|---|---|---|
| DC | I_s(1 + x²/4) − i₀ | términos 0 y 2 |
| f | I_s(x + x³/8) | términos 1 y 3 |
| 2f | **I_s x²/4** | solo el término cuadrático |
| 3f | **I_s x³/24** | solo el término cúbico |

**5. Razón entre armónicos.**

$$ \frac{I_{2f}}{I_{3f}} \approx \frac{x^2/4}{x^3/24} = \frac{6}{x} = \frac{6V_T}{V_1}
   = \frac{6(0.026\ \text{V})}{0.2\ \text{V}} = 0.78 . $$

## Resultado exacto (2b)

Con la función generatriz de Bessel modificada, e^{x cos θ} = I₀(x) + 2Σₙ Iₙ(x) cos nθ, la
amplitud exacta del armónico n es I_n = 2 I_s Iₙ(x). Por tanto:

$$ \left.\frac{I_{2f}}{I_{3f}}\right|_{\text{exacta}} = \frac{I_2(7.6923)}{I_3(7.6923)} = 1.4065 , $$

que coincide con la FFT de `punto2b.m` (1.4065).

## Comparación

| Componente | Taylor (mA) | Exacto (mA) | Taylor / exacto |
|---|---|---|---|
| DC | 0.0162 | 0.3291 | 0.049 |
| 50 Hz | 0.0663 | 0.6137 | 0.108 |
| 100 Hz | 0.0152 | 0.4986 | 0.030 |
| 150 Hz | 0.0195 | 0.3545 | 0.055 |
| **Razón I₂f/I₃f** | **0.780** | **1.4065** | error −44.5 % |

1. **La razón de Taylor subestima la exacta en un 44.5 %,** y las amplitudes absolutas quedan
   entre 10 y 30 veces por debajo. La serie truncada solo vale si x = V₁/V_T ≪ 1. Aquí
   x ≈ 7.7, y los términos de orden 4, 5, … no son despreciables: la serie de eˣ se trunca en
   1 + x + x²/2 + x³/6 ≈ 114, mientras que e^{7.69} ≈ 2190.
2. **Por qué la razón falla menos que las amplitudes.** El error de truncamiento afecta a los
   dos armónicos de forma parecida y se cancela parcialmente en el cociente.
3. **Rango de validez.** Para x → 0, Iₙ(x) ≈ (x/2)ⁿ/n!, así que I₂/I₃ → 6/x: la estimación
   de Taylor es el límite de señal pequeña del resultado exacto. Numéricamente, el error es
   menor al 10 % para V₁ < 63 mV (x < 2.4); ver el panel superior de la figura.
4. **Expansión alrededor de v = 0.** Si se expande en v = 0 en lugar de V₀, la razón da
   6(V_T + V₀)/V₁ = 9.78, mucho peor: la serie se evalúa lejos de su centro (v/V_T hasta ≈ 19).
5. **Analogía óptica.** El término cuadrático es el único que genera 2f y el cúbico el único
   que genera 3f, igual que χ⁽²⁾ genera el segundo armónico y χ⁽³⁾ el tercero en
   P = ε₀[χ⁽¹⁾E + χ⁽²⁾E² + χ⁽³⁾E³ + …] (Hagan, Kik & Van Stryland, notas OSE5312, ec. 15.2,
   p. 159). La expansión perturbativa solo es válida si el campo es pequeño frente a la escala
   característica de la no linealidad: el campo atómico en óptica, V_T en el diodo.
