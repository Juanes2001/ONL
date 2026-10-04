---
name: lumerical-arranque-simulaciones
description: Arrancar y ejecutar simulaciones de Lumerical en este repositorio — abrir la sesión de lumapi, elegir intérprete, directorio de trabajo del motor, correr en background y vigilar el progreso. Úsala SIEMPRE que haya que correr un paso, un barrido o un estudio que toque MODE, FDTD o INTERCONNECT, y también al crear un entorno de simulación nuevo para que arranque sin fricción.
---

# Arrancar simulaciones de Lumerical en este repositorio

Esta skill existe por una razón concreta: **se ha perdido tiempo varias veces
haciendo comprobaciones de entorno en vez de correr la simulación**. La regla de
oro es una sola.

## Regla nº 1 — No hay pre-vuelo. Se corre y ya.

Cuando el usuario pide correr una simulación, **se corre**. No se antepone nada:

- ❌ No sondear la instalación, ni el servidor de licencias, ni puertos, ni
  servicios, ni `License.ini`, ni `tasklist`.
- ❌ No escribir un "smoke test" previo para ver si Lumerical abre.
- ❌ No preguntar si hay licencia disponible.
- ✅ Llamar al punto de entrada del entorno y lanzar el paso.

`lumapi` es el único intermediario. Ha funcionado y hay estudios completos
corridos con él en este repositorio (`plataforma_v2`, `cascada_v2`, con
resultados de FDE, FDTD 3D e INTERCONNECT en disco). Si algo del arranque falla,
**el propio traceback lo dirá**, y ese sí es el momento de mirarlo.

**Excepción en ONL (Juanes, 2026-10-04):** antes de lanzar, se comprueba el turno y
la RAM con la skill `recursos-simulaciones` (`python3 scripts/ram_lumerical.py ...`,
~5 s). No abre Lumerical ni sondea la licencia. **ONL solo corre si el Lumerical
local está libre de la tesis** (y en el cluster, solo sin jobs de la tesis). Si
dice OCUPADO o NO CABE, no se lanza.

## Regla nº 2 — Abrir una sesión es LENTO. No la mates.

Una sesión puede tardar minutos en abrir. **Que tarde no es una prueba de que
esté colgada.** Nunca hay que matar un proceso de Lumerical porque «lleva
mucho»; matarlo destruye la evidencia y, si estaba cargando, tira el trabajo.

Cómo se hace bien:

1. Lanzar el paso **en background** (`run_in_background`), nunca con un
   `timeout` corto que lo decapite.
2. Vigilar el **progreso real**, no el reloj: líneas nuevas en stdout, el `.fsp`
   apareciendo en el directorio de trabajo, puntos escritos en el HDF5
   (`flags/computed`).
3. Solo si NO hay ningún progreso durante mucho tiempo, informar al usuario de
   lo que se observa y **preguntarle**. La decisión de abortar es suya.

## Cómo se abre una sesión

Siempre por el módulo `comun/entorno.py` del estudio. No se reimplementa a mano.

```python
from comun import entorno
app = entorno.abrir_fdtd(ocultar_gui=True)     # o abrir_mode(...)
try:
    ...
finally:
    app.close()                                 # SIEMPRE en finally
```

En un script autocontenido para el cluster, donde no se puede importar del
repositorio, se vendoriza `importar_lumapi()` tal cual. Lo único que no se puede
simplificar:

```python
# Windows: hacen falta LOS DOS directorios de DLL.
# Sin bin/ falla al cargar el solver; sin api/python falla interopapi.dll
# con FileNotFoundError.
for d in (rf"{raiz}\bin", rf"{raiz}\api\python"):
    os.add_dll_directory(d)
sys.path.insert(0, rf"{raiz}\api\python")
import lumapi
```

## Las cuatro trampas del entorno que sí hay que respetar

Ninguna se descubre con un diagnóstico previo; todas están ya resueltas en el
código. Se copian, no se re-investigan.

1. **El motor de FDTD no arranca sobre la UNC de WSL.** Si el `.fsp` vive en
   `\\wsl.localhost\...`, `run()` se cuelga sin error. Todo script que llame a
   `run()` hace `cd()` a un directorio nativo de Windows y guarda ahí el `.fsp`
   antes de correr → `entorno.dir_trabajo_motor()`. MODE/FDE no lo necesita:
   resuelve en proceso.
2. **HDF5 no bloquea archivos sobre esa UNC.** `HDF5_USE_FILE_LOCKING=FALSE`
   hay que exportarlo **antes** de importar `h5py`. Ya lo hace `comun/almacen.py`
   en su cabecera.
3. **Las variables de entorno de Linux no llegan al Python de Windows** salvo
   que estén en `WSLENV`. La configuración se pasa **por argumentos de línea de
   comandos**, no por entorno. Por eso `entorno.py` lee `argv` antes que `os.environ`.
4. **El intérprete no es el mismo que el orquestador.** `main.py` corre bajo el
   Python de **Linux**; los pasos se lanzan con el Python de **Windows**, que es
   el único que ve `lumapi`. La ruta se autodetecta (`_python_ejecutor()`), nunca
   se escribe en el código. Invocar `main.py` con el Python de Windows revienta
   con `UnicodeEncodeError` de cp1252.

## Una sola plaza de licencia

Las simulaciones corren **en serie**, nunca en paralelo. Y un proceso de
Lumerical que quedó vivo retiene la plaza, así que:

- Cerrar siempre en `finally:`.
- `close()` puede dejar el proceso huérfano. En barridos largos conviene barrer
  huérfanos entre puntos, o la RAM se agota en una noche.

## Al crear un entorno de simulación nuevo

Se copia el arranque de un entorno que ya corre (`plataforma_v2`), no se escribe
desde cero: `comun/entorno.py`, `comun/almacen.py`, `main.py` y el patrón
`pasos/pasoNN_*.py` con `_ruta.py`. Así el entorno nuevo hereda las cuatro
trampas ya resueltas y arranca a la primera.

Y todo paso llama `almacen.preparar_paso(PASO, cfg)` al empezar (CLAUDE.md §7);
si el paso elige motor, **después** de resolverlo.
