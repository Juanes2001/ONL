# Óptica No Lineal (ONL)

Proyecto de seguimiento de la materia **Óptica No Lineal**, Universidad Nacional de Colombia,
semestre 2026-II. Aquí el usuario (Juan Esteban Rodríguez Ochoa) trabaja los talleres y el
proyecto final del curso, apoyado en la bibliografía que va agregando.

## Propósito

Resolver talleres, desarrollar el proyecto final y acumular apuntes del curso. Cuando exista
`notas/generalidades-del-curso.md` (programa, calendario, evaluación), **leerlo antes de
preparar cualquier entregable**.
Al iniciar una sesión, leer `notas/contexto-proyecto.md` (estado del trabajo, entorno, resultados y
decisiones pendientes).

## Estructura

- `bibliografia/` — libros y artículos; lista de referencias en `bibliografia/README.md`.
- `talleres/taller-NN-<tema>/` — enunciado, código, figuras y solución de cada taller.
- `proyecto-final/` — propuesta, bitácora, código, resultados e informe.
- `notas/` — apuntes por tema y `notas/bitacora-sesiones.md`.
- `scripts/` — código reutilizable; `datos/` — datos crudos; `figuras/` — figuras generadas.

## Convenciones

- Idioma de notas, README y commits: español.
- Bibliografía se guarda tal cual se recibe. Los PDF/DjVu/EPUB de `bibliografia/` están
  ignorados por git (derechos de autor; el repo es público). Al agregar una referencia,
  registrarla en `bibliografia/README.md`.
- Antes de resolver un taller, consultar la bibliografía del tema y citar fuente y página
  (ej. Boyd, *Nonlinear Optics*, 3.ª ed., §2.2, p. 69).
- Notación: seguir la convención de la bibliografía principal del curso (unidades SI;
  susceptibilidades χ⁽ⁿ⁾, polarización P̃(t) = ε₀[χ⁽¹⁾Ẽ + χ⁽²⁾Ẽ² + χ⁽³⁾Ẽ³ + …]). Si se usa
  otra convención (gaussiana, d_eff vs χ⁽²⁾), indicarlo explícitamente.
- Las derivaciones se escriben completas, paso a paso; los resultados numéricos se reportan con
  unidades y los parámetros usados.
- Los datos crudos en `datos/` no se modifican; se procesan desde `scripts/` o desde el taller.
- Las figuras llevan ejes con magnitud y unidades.
- Al cerrar cada sesión, registrar lo hecho y lo pendiente en `notas/bitacora-sesiones.md`.

## Simulaciones Lumerical (local, vía lumapi)

Protocolo heredado del repo de tesis `../fotonica-integrada` (solo lectura; copiado el
2026-10-04). Skills en `.claude/skills/`: **`lumerical-arranque-simulaciones` es obligatoria
antes de correr MODE/FDTD/INTERCONNECT**; `lumerical-script-builder` para construir scripts;
`lumerical-analisis-resultados` para medir y diagnosticar; `vigilancia-procesos-largos` para
todo lo que tarde > 5 min. `.claude/rules/fdtd-cluster.md` solo aplica a `proyecto-final/cluster/`.

- ⚠ **PRIORIDAD DE LA TESIS (Juanes, 2026-10-04).** Las simulaciones de ONL se corren
  **SOLAMENTE si el Lumerical local está libre**: ninguna sesión ni motor de Lumerical vivo de
  fotonica-integrada (o sin atribuir). Las simulaciones pesadas que necesiten el cluster siguen
  la misma regla: solo si no hay jobs de la tesis corriendo ni en cola. Si está ocupado, **no se
  lanza**, se informa y se espera. Nunca se mata, cancela ni toca nada de la tesis.
- **Antes de lanzar (siempre):** skill `recursos-simulaciones` →
  `python3 scripts/ram_lumerical.py --celdas N` (o `--fde`, `--necesita-gb X`). Comprueba el
  turno (código 4 = OCUPADO) y la RAM (7.4 GB compartidos; sin RAM, `app.run()` se cuelga sin
  error). Local vs. cluster: lo que no cabe en RAM local o tardaría > 6 h va al cluster
  (`proyecto-final/cluster/`, `~/juanes_sims/onl_<estudio>/`).
- **Entorno de esta máquina:** Lumerical **v202** en Windows
  (`C:\Program Files\Lumerical\v202`); los pasos se lanzan con el Python de Windows
  (`/mnt/c/Users/*/AppData/Local/Programs/Python/Python311/python.exe`, autodetectado por
  `main.py`), que es el único que ve `lumapi`. El orquestador `main.py` corre con el Python
  de Linux.
- **Nuevo estudio:** copiar `proyecto-final/simulaciones/_plantilla/` a
  `proyecto-final/simulaciones/<estudio>/` (trae `comun/entorno.py`, `almacen.py`,
  `modos.py`, `graficas.py`, `plataforma.py`, `main.py`, `pasos/_ruta.py`). Un paso por
  archivo `pasos/pasoNN_<descripcion>.py`, que empieza con `import _ruta` y llama
  `almacen.preparar_paso(PASO, cfg)`. Contrato entre pasos: `salida.json`; barridos en HDF5
  con `flags/computed`; carpetas por firma de parámetros.
- **Reglas que no se rompen:** no hay pre-vuelo (se corre y ya); abrir sesión es lento y no
  es cuelgue, nunca matar Lumerical por iniciativa propia; FDTD siempre con
  `entorno.preparar_motor()` (cd + save en directorio nativo de Windows, no la UNC de WSL) y
  `entorno.correr_motor_fdtd()` (motor por subproceso) + `app.load()`; una sola licencia →
  simulaciones en serie; cerrar la sesión en `finally`; `HDF5_USE_FILE_LOCKING=FALSE` antes
  de `h5py`; configuración por argumentos, no por variables de entorno.
- Unidades SI hacia Lumerical; `SPEED_OF_LIGHT = 299_792_458.0` exacto; figuras PNG + PDF
  (`scripts/plotting.py` o `comun/graficas.py`). Archivos pesados (`.fsp`, `.h5` grandes)
  fuera de git.
- ⚠ La autorización de la tesis para matar y relanzar procesos congelados > 1 h 30 min
  (skill `vigilancia-procesos-largos` §4.1) **no se hereda**: en este repo, preguntar antes
  de matar cualquier proceso, salvo que Juanes lo autorice aquí.
- Datos de la plataforma (geometrías, pérdidas, Q): `proyecto-final/contexto-fotonica-integrada.md`.

## Proyecto final: decisiones vigentes

- **Sensado de VOLUMEN (bulk)**: el anillo add-drop sensor es un refractómetro (analito
  n = 1.33 → 1.37 como cladding completo), sin foco en sustancias específicas y **sin
  funcionalización**. La detección superficial se abordará mucho más adelante; no
  mezclarla en los estudios actuales.
- Estudio activo: `proyecto-final/simulaciones/seccion_v1/` (leer su `ESTADO.md` §0 al retomar).
