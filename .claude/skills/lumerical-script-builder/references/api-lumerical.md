# API de Lumerical: nombres reales y trampas silenciosas

Todo lo de aquí está **verificado en runtime contra Lumerical v202**. Las trampas son
fallos que **no lanzan ninguna excepción**: la simulación corre entera y devuelve ceros o
física falsa.

## Nombres que cuestan (estos sí lanzan error)

| Quieres | En FDTD 3D | En varFDTD / MODE |
|---|---|---|
| Fuente de modo | `addmode()` | `addmodesource()` |
| Selección de modo | `"fundamental TE mode"` | `"fundamental mode"` / `"user select"` (**no** acepta TE) |
| Corte ⊥ a propagación en x | `"2D X-normal"` | `"linear y"` |
| Corte ⊥ a propagación en y | `"2D Y-normal"` | `"linear x"` |
| Ángulo de la fuente | `"theta"` (no `"angle theta"`) | `"theta"`; **no existe `"phi"`** (es 2D) |
| Autoshutoff | `"auto shutoff min"` | igual |

Más detalles:

- El `modeexpansion` de **varFDTD rechaza** los tipos `2D *-normal`; solo acepta
  `linear x` / `linear y`. El de **FDTD 3D acepta los tres** `2D *-normal`.
- Bajo `"linear y"` solo está activa la propiedad `"y span"`; bajo `"linear x"`, solo
  `"x span"`. Fijar la otra da `property is inactive`.
- `getexpansion()` **no existe** en la API de Python: la ligadura DFT↔expansión no se
  puede verificar leyendo propiedades, solo corriendo.
- `getresult(mon, "T")` sobre un monitor de expansión lanza
  `Can not find result 'T'`. El resultado se llama `"expansion for <puerto>"`.

## Las seis trampas silenciosas

### 1. `addmodeexpansion` sin ligar → el job termina sin datos

Un monitor de expansión **no graba campos por sí mismo**: expande los de un monitor DFT
que hay que ligarle explícitamente. Cada puerto son **dos** objetos con idéntica geometría.

```python
app.addpower();          app.set("name", f"dft_{port}");  # ...geometría...
app.addmodeexpansion();  app.set("name", f"exp_{port}");  # ...misma geometría...
app.set("mode selection", MODO)
app.setexpansion(port, f"dft_{port}")     # <-- sin esto no hay nada que expandir
```

Se lee así:

```python
r = app.getresult(f"exp_{port}", f"expansion for {port}")
# claves: T_forward, T_backward, T_net, T_total, a, b, N, P, f, lambda
T = np.real(np.array(r["T_forward"]).flatten())
```

### 2. `mode selection` desalineada entre fuente y expansión → `T_forward = 0.0000`

Si el monitor expande sobre una polarización distinta a la inyectada, el solapamiento da
**cero exacto sin ningún error**. Reproducido: fuente `fundamental mode` + expansión
`fundamental TE mode` → 0.0; alineadas → 1.0. **Usa la misma cadena en ambos.**

### 3. varFDTD: los `test points` por defecto caen donde no hay guía

varFDTD colapsa 3D→2D calculando el índice efectivo del slab en unos puntos de test que
por defecto rodean el **origen**. En una geometría de anillo grande el origen es el
**hueco**, puro cladding: el colapso se hace sobre el cladding, la estructura deja de
guiar y nada acopla.

*Síntoma:* `T_through` plano (~0.60) sin dips, `T_drop = 0` exacto, y autoshutoff cortando
a los segundos en vez de agotar el `simulation time`.

```python
mode.setnamed("varFDTD", "x0", 0.0)
mode.setnamed("varFDTD", "y0", geom["bus1_y_um"] * 1e-6)   # sobre el núcleo de una guía
```

### 4. FDTD 3D: la región debe abarcar la estructura completa, no medio dominio

Con simetría, la región se define sobre la **estructura entera centrada en el plano de
simetría** — es la condición de frontera la que hace que Lumerical simule solo la mitad.
Recortar el dominio a mano deja fuente y monitores medio fuera: los monitores no graban,
el `dft_` sale vacío y `getresult` falla con `Can not find result 'expansion for ...'`.

```python
fdtd.set("z", 0.0); fdtd.set("z span", 2 * z_half_um * 1e-6)   # completo, centrado en z=0
fdtd.set("z min bc", "Symmetric")
```

Medido en una guía recta SiN 3D contra la referencia sin simetría:

```
región completa + PML             T_forward 0.9846   8.0 s   <- referencia
región completa + Symmetric       T_forward 0.9846   4.0 s   <- correcto para TE0, mitad de coste
región completa + Anti-Symmetric  T_forward 0.0073   3.0 s   <- mata el modo TE0
```

**Para TE₀ la BC correcta es `Symmetric`.** Verifica siempre la simetría contra el mismo
caso sin simetría antes de confiar en ella.

### 5. Los puertos drop y add se confunden con facilidad

Hay que razonar el **sentido de circulación** en el anillo, no suponerlo:

- Luz entrando por el bus inferior hacia **+x** → acopla en la tangencia inferior →
  circula en sentido **antihorario**.
- En la tangencia **superior** viaja hacia **−x** → el drop es el extremo **−x** de ese
  bus, y su potencia está en **`T_backward`**.
- En la tangencia **derecha** (bus vertical) viaja hacia **+y** → el drop es el extremo
  **+y**, y su potencia está en **`T_forward`**.

*Cómo confirmarlo sin adivinar:* pon monitores de expansión en **los dos** extremos del
bus y mira cuál recibe potencia. Medido en un caso real: el extremo correcto daba
`T_backward = 0.837` y el opuesto `0.0001`.

### 6. Un "ángulo" en la descripción casi nunca es `theta` de la fuente

Poner `theta` en un *mode source* **rota el perfil del modo**. Un modo guiado es solución
para propagación *a lo largo* del eje: inyectarlo en ángulo dentro de una guía recta hace
que **radie en vez de acoplar**.

Cuando una descripción menciona un ángulo, lo que casi siempre significa es el **ángulo
entre las guías** (geometría de routing). La inyección debe ser **siempre normal a la cara
del núcleo**. Confírmalo contra el layout/GDS antes de modelarlo.

⚠ Si dos guías rectas perpendiculares llegan las dos al PML por sus cuatro extremos, se
**cruzan** geométricamente. Calcula el solape y dilo: en un caso real costó **14 % del
through** en 3D (9 % en varFDTD, que subestima porque no modela la radiación vertical).
Un cruce aguas abajo del punto de acoplamiento no afecta al drop.

## 7. varFDTD no propaga por un arco abierto

Verificado el 2026-08-19 con un bend de 90° en SiN (1000 x 400 nm, SiO2):

```
motor      R=19um   R=30um   R=50um   R=80um
varFDTD    0.0009   0.0003   0.0001   0.0000    <- EMPEORA con R: imposible
FDTD 3D    0.9930     --       --       --      <- misma geometria
```

La luz atraviesa el arco **en linea recta**, sin guiarse, con cualquier radio. La
posicion del pico coincide con la trayectoria de un rayo libre. Descartado por medida
directa: rango de theta, `bend orientation`, malla (hasta accuracy 4 y caja fina en
todo el cuadrante), tiempo de simulacion (10x), margen al PML (2 a 12 um), solape del
acceso con el arco, y el indice del modelo (n=1.99 en todo el arco, leido del mallado).

Causa: varFDTD colapsa la dimension vertical apoyandose en un modo de referencia, y en
un arco la guia **rota** mientras propaga. En un anillo CERRADO el modo es
autoconsistente y sobrevive al colapso (RING_2 resuena con Q ~1640 en varFDTD); en un
arco abierto alimentado desde una guia recta, no.

**=> Cualquier medida propagativa sobre un arco aislado va en FDTD 3D.** varFDTD sigue
sirviendo para guias rectas (una medida de n_g por fase en recta dio 1.824, coherente
con el 1.809 del FSR del anillo en el mismo motor).

## Monitores de expansion en un bend: dos detalles que sesgan el resultado

1. **No los pongas en los extremos exactos del arco.** Ahi el campo todavia es el modo
   recto y no solapa con el curvado: medido, `T_forward` satura en 0.50. Metelos unos
   grados dentro y sube a 0.97. El error por no ser el corte exactamente normal a la
   propagacion es cos(5 grados) = 0.996, despreciable.
2. **La longitud de fase es la que separa los MONITORES, no el arco completo.** Entra
   directamente en `n_g = (c/L)*dphi/domega`, asi que confundirlas da un n_g sesgado
   **sin ningun sintoma visible**: numero creible y equivocado.

`bend orientation` tampoco es cosmetico: con el valor equivocado el solapamiento de un
puerto cae de 0.97 a 0.006. Pruebala y quedate con la que da alto en **ambos** puertos.

## Otras propiedades útiles

```python
app.setnamed("FDTD", "background material", "<Object defined dielectric>")
app.setnamed("FDTD", "index", n_clad)
app.setglobalsource("wavelength start", lam0 * 1e-9)
app.setglobalsource("wavelength stop",  lam1 * 1e-9)
app.setglobalmonitor("frequency points", n_pts)
```
