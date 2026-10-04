---
name: lumerical-script-builder
description: Construir un script de simulación Lumerical (FDTD 3D, varFDTD/MODE) a partir de la descripción de una estructura fotónica — dada en palabras, en una imagen/diagrama o en un GDS. Cubre extraer los parámetros, elegir el motor, construir geometría/malla/región/fuente/monitores, verificar antes de gastar horas de cómputo, y el checkpointing. Úsala cuando pidan simular un anillo, una guía, un acoplador o cualquier estructura en Lumerical, o cuando haya que corregir un script de simulación existente.
---

# Construir scripts de simulación en Lumerical

Esta skill destila lo aprendido construyendo y depurando las rutinas de RING_2. **El
patrón dominante de fallo no es el error de sintaxis: es el script que corre entero,
no lanza ninguna excepción y devuelve ceros o física falsa.** Casi todo lo de aquí
existe para atrapar eso antes de gastar horas.

## Procedimiento

### 1. Extraer los parámetros de la descripción

Antes de escribir código, deja fijados **por escrito** estos valores. Si alguno no se
puede determinar, decláralo como supuesto explícito en el docstring — nunca lo inventes
en silencio.

| Grupo | Qué hace falta |
|---|---|
| Geometría | radio o longitud, ancho `w`, altura `h`, gaps de acoplamiento, orientación de cada guía |
| Materiales | índice del núcleo y del cladding (o el material de la biblioteca), simetría vertical del stack |
| Óptica | λ central, ventana espectral, polarización (TE₀/TM₀), n_eff y n_g esperados |
| Puertos | cuál es input, through, drop, add — y **por qué extremo sale cada uno** |
| Referencia | Q, FSR, FWHM esperados, para saber si el resultado es creíble |

Según la fuente:

- **En palabras.** Pregunta solo por lo que cambie el resultado; el resto se deriva. Si
  el proyecto tiene tablas de parámetros (p. ej. `TABLE1`/`TABLE2` con una fila por
  componente), **prefiérelas a la documentación en prosa**: son salida directa del solver
  de modos. Anota la discrepancia si la hay.
- **Desde una imagen o diagrama.** Extrae la topología y sobre todo la **orientación
  relativa de las guías** y en qué extremo está cada puerto. Las cotas de una figura no
  son fiables: confírmalas con el usuario o con las tablas.
- **Desde un GDS.** Lee capas y coordenadas para sacar la geometría real. Es la única
  fuente que resuelve sin ambigüedad el *routing* (curvas, cruces, ángulos entre guías).
  Cuando una descripción mencione un "ángulo", **casi siempre es geometría de routing, no
  un `theta` de fuente** — ver la trampa 6 en `references/api-lumerical.md`.

### 2. Elegir el motor

- **varFDTD (`lumapi.MODE`)** para validar topología, acoplamiento y forma del espectro.
  Minutos en vez de horas. **No sirve para números absolutos**: medido contra FDTD 3D en
  la misma geometría, se equivocó **−47 % en Q** y **−9 % en n_g**.
- **FDTD 3D (`lumapi.FDTD`)** para n_eff, n_g, FSR y Q. Es la referencia.

El flujo bueno es: varFDTD primero para descartar errores de construcción baratos, FDTD 3D
después para los números.

### 3. Construir

Sigue la anatomía de `references/anatomia-script.md` y **lee entero
`references/api-lumerical.md` antes de escribir una sola llamada** — contiene los nombres
correctos y las seis trampas silenciosas verificadas en runtime contra Lumerical v202.

Regla transversal: **explica en 2–3 líneas de comentario el porqué físico** de cada
bloque del solver (malla, tiempo de simulación, condiciones de frontera). Sin eso, el
siguiente que lo lea no puede distinguir un valor razonado de uno copiado.

### 4. Verificar antes de correr

No lances una simulación larga sin pasar por `references/verificacion.md`. En orden:
smoke test diminuto → harness de construcción sin `run()` → inspección visual en el CAD →
corrida real. Cada escalón cuesta segundos y ahorra horas.

### 5. Correr y guardar

Checkpointing obligatorio: el HDF5 se crea **antes** de `run()` con la metadata completa,
los resultados preasignados a `NaN` y `flags/computed = False`; al terminar se escriben
los datos y se marca `True`, con `flush()` en ambos momentos. Un job interrumpido debe
reanudarse, no empezar de cero.

## Qué es fácil equivocarse

- **Dar por buena una simulación que "corrió bien".** Una simulación que termina
  sospechosamente rápido casi siempre cortó por autoshutoff porque no había nada
  propagándose. Compara siempre el tiempo real con lo esperado por número de celdas y
  timesteps.
- **Confiar en que un monitor existe = un monitor mide.** Un `modeexpansion` sin
  `setexpansion()` no devuelve nada, y no avisa.
- **Aceptar un `T = 0.0000` exacto como resultado físico.** Un cero exacto en toda la
  banda es un fallo de configuración, no una medida.
- **Tocar los parámetros del proyecto para que cuadren.** Si el resultado no coincide con
  la tabla de diseño y **varios métodos independientes coinciden entre sí**, el sospechoso
  es la tabla, no el solver. Repórtalo, no lo "corrijas" — un cambio así suele afectar a
  toda la plataforma.

## Referencias

| Archivo | Qué contiene |
|---|---|
| `references/api-lumerical.md` | Nombres reales de la API y las seis trampas silenciosas |
| `references/anatomia-script.md` | Estructura del script, malla, tiempo de simulación, checkpointing |
| `references/verificacion.md` | Smoke test, harness de construcción, entorno WSL2↔Windows |
