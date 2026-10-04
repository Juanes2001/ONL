# Diagnóstico: síntoma → causa

Todos verificados en runtime. Ninguno lanza excepción por sí solo.

## ⚠ El orden correcto: mapea el campo ANTES de conjeturar

Ante un puerto a cero, la tentación es probar hipótesis baratas una a una
(condiciones de frontera, malla, tiempo de simulación, orientación de monitores).
**No lo hagas.** En un caso real se gastaron ocho rondas así, todas negativas, y el
problema quedó acorralado con dos medidas en cuanto se miró el campo.

Primero:

1. **Monitor de campo sobre todo el dominio** y muestrea |E|² a lo largo del camino
   que la luz debería seguir. Distingue de golpe entre "se corta de repente"
   (discontinuidad geométrica), "decae progresivamente" (radiación) y "no está donde
   debería" (no se guía).
2. **Integra en cortes perpendiculares**, no en un punto. En una guía curva el modo
   se desplaza hacia el radio exterior: muestrear en el centro geométrico confunde
   desplazamiento con pérdida.
3. **Compara la posición del pico contra la trayectoria de un rayo recto.** Si
   coinciden, la estructura no está guiando en absoluto, y ninguna hipótesis sobre
   monitores o mallas va a explicarlo.

Y un control que vale por diez conjeturas: **barre el parámetro del que depende la
física**. La pérdida por curvatura decae exponencialmente con R; si la transmisión
**empeora** al aumentar el radio, no es física de ningún tipo — es el montaje o el
motor.

## `T = 0.0000` exacto en toda la banda

1. **El monitor de expansión no está ligado** a un monitor DFT con `setexpansion()`.
2. **La `mode selection` de la fuente y la del monitor no coinciden** → solapamiento cero.
3. **El puerto está en el extremo equivocado**, o la potencia está en `T_backward` y se
   está leyendo `T_forward` (o al revés).

*Cómo confirmar el 3:* pon monitores de expansión en **los dos** extremos del bus y mira
cuál recibe potencia. Diferencia real medida: 0.837 contra 0.0001.

## Through plano, sin dips — nada acopla al resonador

- **varFDTD:** los `test points` caen en una zona sin núcleo (típicamente el hueco del
  anillo) y el colapso 3D→2D se hace sobre el cladding. Firma característica:
  `T_through ≈ 0.60` plano y `T_drop = 0` exacto.
- **Gap mal resuelto:** cuenta las celdas dentro del gap. Menos de ~3 y el acoplamiento
  no se resuelve.
- **La fuente no inyecta:** ver el punto siguiente.

## La simulación termina muchísimo antes de lo esperado

Estima el coste: celdas × timesteps. Si el tiempo real es órdenes de magnitud menor, el
autoshutoff cortó porque **no había campo que decayera**.

- **FDTD 3D:** la región definida como medio dominio deja fuente y monitores medio fuera;
  no graban nada y el `dft_` sale vacío.
- **Simetría mal puesta:** `Anti-Symmetric` mata el modo TE₀ (0.0073 contra 0.9846).
- Un resonador de alto Q que **sí** acopla mantiene energía durante `~15·τ`: si corta
  mucho antes, no acopló.

## El Q sale bajo pero el espectro tiene buena pinta

Por orden de probabilidad:

1. **FWHM medido sin interpolar** → Q subestimado hasta un 8 %. Descártalo primero.
2. **El método.** varFDTD subestima el Q de forma masiva (−47 % medido). Repite en 3D.
3. **Gap poco resuelto:** ~3.5 celdas en el gap sobreestiman el acoplamiento y bajan el Q
   cargado.
4. **Autoshutoff demasiado alto:** trunca la cola de la resonancia. Debe ser `1e-5`.

## Los números no coinciden con la tabla de diseño

Haz el experimento de control: **cambia una sola cosa**.

- Cambia de solver con la misma geometría → si el número se mueve, es del método.
- Cambia la geometría con el mismo solver → aísla el trazado.
- **Coinciden varios métodos entre sí pero no con el diseño** → el sospechoso es el dato
  de diseño. Un artefacto numérico no sobrevive al cambio de solver.

Reporta la evidencia y el alcance del cambio; no toques el parámetro. Un `n_eff` tabulado
que no describe la geometría afecta a todos los componentes de la familia, no solo al que
estás simulando.

## Pérdida inesperada en un puerto

Comprueba primero si hay **solapes geométricos no intencionados**: dos guías rectas que
llegan al PML por sus cuatro extremos pueden cruzarse. Calcula los rectángulos:

```python
solape_x = (max(a_x0, b_x0), min(a_x1, b_x1))
solape_y = (max(a_y0, b_y0), min(a_y1, b_y1))
hay_cruce = solape_x[0] < solape_x[1] and solape_y[0] < solape_y[1]
```

Un cruce **aguas abajo** del punto de acoplamiento degrada solo ese puerto; el resto del
circuito no se entera. Dilo así de explícito: cambia por completo si el hallazgo es grave
o irrelevante para la función del dispositivo.
