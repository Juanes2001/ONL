---
name: lumerical-analisis-resultados
description: Extraer, interpretar y explicar los resultados de una simulación fotónica — λ de resonancia, extinción, FWHM, Q, FSR, n_g y n_eff — decidir si son creíbles, diagnosticar los que no lo son, y presentarlos en figuras y tablas. Úsala al analizar el espectro de un anillo o resonador, al comparar solvers o geometrías, al preparar figuras de resultados, o cuando un resultado de simulación no cuadre con lo esperado.
---

# Analizar y explicar resultados de simulación

Un espectro no es un resultado hasta que sabes si es creíble. Esta skill cubre cómo
medir cada magnitud sin sesgo, cómo decidir si el número es real o un artefacto, y cómo
presentarlo.

## 1. Medir

Detalle y código en `references/metricas.md`. Lo que más se equivoca:

- **FWHM: interpola los cruces a media altura.** Tomar la muestra más cercana introduce
  un error de hasta 2 muestras. Con paso de 20 pm eso son 40 pm sobre un FWHM de 500 pm:
  **un 8 % de error en Q**. En un caso real la diferencia fue entre concluir "Q −3.3 %
  por debajo del diseño" y el correcto "+1.0 % por encima".
- **ER en dB** = `10·log10(T_through fuera de resonancia / T_through en resonancia)`.
  Di siempre respecto a qué nivel se mide.
- **FSR** necesita ≥ 2 resonancias en la ventana. Si solo hay una, el FSR no es medible —
  dilo en vez de estimarlo.
- **n_g e n_eff** son magnitudes *derivadas*; explicita la fórmula y el orden `m` usado.

## 2. Decidir si el resultado es creíble

Antes de interpretar, descarta que sea un artefacto. Ver `references/diagnostico.md`.

Señales de que **no** hay física detrás:

| Síntoma | Causa habitual |
|---|---|
| `T = 0.0000` exacto en toda la banda | monitor sin ligar, o polarización desalineada |
| Through plano, sin dips | nada acopla al resonador |
| La simulación termina muchísimo antes de lo esperado | autoshutoff cortó: no había campo |
| Un puerto a cero y el otro bien | puerto en el extremo equivocado, o sentido mal leído |

## 3. Separar el error del método del error del modelo

Es la distinción más útil que puedes aportar, y se hace con **un experimento de control**:
repite el mismo caso cambiando **una sola** cosa.

- **Cambia de solver, misma geometría.** Si el número cambia, es del método. Medido:
  varFDTD daba Q ≈ 1640 y FSR 11.16 nm donde FDTD 3D daba 3130 y 9.79 — un **−47 % en Q**
  que era enteramente del método.
- **Cambia la geometría, mismo solver.** Aísla el efecto del trazado.
- **Si varios métodos independientes coinciden entre sí pero discrepan del diseño, el
  sospechoso es el dato de diseño.** Un artefacto numérico no sobrevive al cambio de
  solver. Ocurrió con una λ de resonancia 5 nm desplazada en los cuatro casos: apuntaba a
  que el `n_eff` tabulado no describía la geometría simulada.

**No "arregles" un parámetro del proyecto para que cuadre.** Repórtalo con la evidencia y
deja la decisión a quien conozca el alcance del cambio.

## 4. Explicar

Estructura que funciona: **el veredicto primero, la evidencia después, lo que no cuadra al
final y sin disimular.**

- Da el número **y su desviación contra lo esperado**, en la misma línea. `Q = 3130
  (diseño 3100, +1.0 %)` se entiende; `Q = 3130` no.
- **Cuantifica lo que afirmes.** "El cruce penaliza el through" es una impresión;
  "cuesta 14.2 % del through fuera de resonancia, 0.9689 → 0.8316, y el drop no se ve
  afectado (0.8888 → 0.8887)" es un resultado.
- **Explica el mecanismo, no solo el número.** Por qué el cruce no toca el drop: está
  aguas abajo del punto de acoplamiento.
- **Traduce a consecuencias para la plataforma.** Un desplazamiento en bloque de las
  resonancias mantiene el escalonado relativo pero corre la ventana absoluta del
  instrumento: eso es lo que el lector necesita decidir.
- Cuando corrijas una cifra que ya diste, dilo explícitamente y explica por qué la nueva
  es la buena.

## 5. Figuras

Ver `references/figuras.md`. En corto: PNG **y** PDF vectorial vía `save_fig()` de
`src/plotting.py`, una figura por magnitud con la anotación que la explica, el **color
codificando el solver** y el **trazo la geometría** — así la identidad de cada curva no
depende solo del color.

## Referencias

| Archivo | Qué contiene |
|---|---|
| `references/metricas.md` | Cómo se mide cada magnitud, con código |
| `references/diagnostico.md` | Síntomas → causas, y cómo confirmarlas |
| `references/figuras.md` | Convenciones visuales y catálogo de figuras |
