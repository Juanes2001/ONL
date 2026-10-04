---
name: vigilancia-procesos-largos
description: Vigilar un proceso largo que ya está corriendo — una simulación de Lumerical, un barrido, un job del cluster — preguntando cada cierto tiempo si sigue avanzando, para distinguir "va lento" de "está congelado" sin matarlo. Úsala siempre que se lance algo en background que tarde más de ~5 min, y cuando haya que decidir si un proceso que lleva horas sin escribir está muerto o trabajando.
---

# Vigilar un proceso largo sin matarlo

Esta skill existe porque en este proyecto ya pasó lo caro: una corrida lanzada a
las 18:33 se colgó a las 19:41 y **estuvo 16 h sin escribir una línea antes de
que nadie lo notara**. El problema no fue el cuelgue: fue que nadie preguntó.

Y el error simétrico también cuesta: **abrir una sesión de Lumerical es lento, y
que tarde no prueba que esté colgada.** Matarla destruye la evidencia y tira el
trabajo.

Las dos reglas, juntas:

> **Preguntar seguido. No matar nunca por iniciativa propia.**

---

## 1. Antes de lanzar: deja escrito qué es "progreso"

Un proceso no se vigila por el reloj, se vigila por **evidencia de avance**.
Antes de arrancar, fija **al menos dos** marcadores independientes y anótalos:

| Marcador | Cómo se mira |
|---|---|
| Líneas nuevas en stdout | `tail -3 <log>` · `wc -l <log>` |
| Puntos escritos en la caché | `flags/computed` del HDF5 del paso |
| El `.fsp` apareciendo / creciendo | `ls -l` del directorio de trabajo del motor |
| Tiempo de CPU del proceso | tiene que **subir** entre dos miradas |
| Archivos de salida nuevos | `find <dir> -newermt '-10 minutes'` |

Dos marcadores, no uno: un log puede quedarse mudo durante una etapa larga y
perfectamente sana, y entonces el `.fsp` o el tiempo de CPU son los que hablan.

Lánzalo siempre en background (`run_in_background`), **nunca con un `timeout`
corto que lo decapite**.

---

## 2. La cadencia: pregunta, no esperes

Elige el mecanismo por el número de avisos que necesitas:

- **Un solo aviso al terminar** → `Bash` con `run_in_background` y un comando
  que salga cuando se cumpla la condición:
  `until [ -f resultados/salida.json ]; do sleep 60; done`
- **Un aviso por cada evento** (cada punto del barrido, cada error) →
  `Monitor` con un filtro que cubra **el éxito y el fallo**:
  `tail -f corrida.log | grep -E --line-buffered "punto |Traceback|Error|Killed|MemoryError"`
- **Un latido periódico mientras trabajas en otra cosa** → `/loop` sin intervalo
  (auto-ritmo) o `ScheduleWakeup`.

**Silencio no es éxito.** Si el filtro solo busca la línea de éxito, un proceso
que revienta se ve exactamente igual que uno que sigue trabajando. Pregúntate
siempre: *si esto acabara de morir, ¿mi filtro diría algo?* Si la respuesta es
no, ensancha el filtro.

Cadencia razonable en este repositorio:

| Etapa | Cada cuánto mirar |
|---|---|
| Abriendo la sesión de lumapi | 2–3 min (puede tardar minutos y es normal) |
| Barrido de FDE / MODE (puntos de segundos) | 2–5 min |
| FDTD 3D (horas) | 15–30 min |
| Job del cluster | según lo que tarde en cambiar la cola, nunca menos de 5 min |

Y **di en voz alta lo que ves en cada mirada**: «llevan 42 min, 7/15 puntos
computados, el `.fsp` creció a 310 MB». Un parte con cifras es lo que permite
decidir; «sigue corriendo» no.

---

## 3. La firma exacta de un cuelgue de Lumerical en esta máquina

Verificada dos veces (2026-08-24 y §3.1 del `ESTADO.md` de `plataforma_v2`):

```
fdtd-solutions.exe VIVO, con el tiempo de CPU CONGELADO (p. ej. 0:00:07 sin
moverse durante 60 s), ~27 MB de memoria,
NINGÚN proceso fdtd-engine,
y NINGÚN .fsp nuevo en el directorio de trabajo del motor.
```

Cómo mirarlo desde WSL, sin tocar nada:

```bash
tasklist.exe /FI "IMAGENAME eq fdtd-solutions.exe" /FO LIST | tr -d '\r'
tasklist.exe /FI "IMAGENAME eq fdtd-engine*"       /FO LIST | tr -d '\r'
ls -l "$DIR_TRABAJO_MOTOR"          # ¿apareció el .fsp? ¿está creciendo?
```

Interpretación:

- **Tiempo de CPU que sube** → está trabajando, aunque el log esté mudo. Esperar.
- **CPU congelada + hay `fdtd-engine`** → el motor está en marcha; casi siempre
  es una etapa larga. Esperar y volver a mirar.
- **CPU congelada + NO hay `fdtd-engine` + no se escribió el `.fsp`** → se quedó
  clavado **abriendo la sesión**, no simulando. Éste es el cuelgue conocido.
  Como `_preparar_motor()` hace `cd()` + `save()` **antes** de `run()`, que el
  `.fsp` no exista es la prueba de dónde murió.
- **`.fsp` escrito pero el motor no arranca** → mira si el proyecto quedó sobre
  la UNC de WSL (`\\wsl.localhost\...`): ahí `run()` se cuelga sin error.

---

## 3-bis. La firma de un job parado en el CLUSTER (wegener)

Allá no hay `tasklist` ni `fdtd-engine` que mirar desde fuera: el motor vive
dentro de un contenedor Docker, lanzado por SLURM. Los marcadores son otros.

```bash
entry_cluster 'squeue -u $USER'                       # ¿sigue en la cola?
entry_cluster 'tail -20 ~/juanes_sims/<est>/results/<algo>_NNNN.out'
entry_cluster 'tail -5  ~/juanes_sims/<est>/results/<algo>_NNNN.err'
entry_cluster 'ls -la   ~/juanes_sims/<est>/results/job_NNNN_*/'
```

⚠ **`sacct` no existe en este cluster.** No se puede consultar el histórico de
un job terminado: si no quedó en el `.out`, se perdió.

Interpretación:

- **En `squeue` con estado `PD`** → no está parado, está *esperando recurso*.
  Mira `NODELIST(REASON)`: si dice `PartitionDown`, el `.slurm` pidió la
  partición por defecto (`leve`), que está **caída**. Se arregla con
  `--partition=core`.
- **En `R` y el `.out` creciendo** → trabajando.
- **En `R` y el `.out` mudo mucho rato** → mira los archivos del `RUN_DIR`: el
  `.fsp` apareciendo o creciendo es la prueba independiente.
- **Fuera de la cola sin marcador de éxito** → murió. `.err` y `container.log`
  dicen por qué.

Y el equivalente exacto del cuelgue local, que allá se manifiesta al revés —no
como un proceso congelado, sino como **un `run()` que termina demasiado rápido**:

> Una simulación 3D cuyo `run()` vuelve en **menos de 1 s** y no deja ningún
> `*.log` de motor junto al `.fsp` **no simuló nada**. Es un fallo de
> configuración del solver, no un resultado. Medido en los jobs 1886–1888.

Por eso todo script del cluster **cronometra su propio `run()`** y avisa.

---

## 4. Qué hacer cuando de verdad no avanza

En este orden, y sin saltarse el último paso:

1. **Recoger la evidencia** (los tres marcadores, con números y con la hora).
2. **Informar al usuario de lo que se observa**, no de lo que se supone.
3. **Preguntarle si aborta.** La decisión es suya, siempre.

**Nunca** `taskkill` por iniciativa propia. Matar un proceso de Lumerical:

- destruye la evidencia de por qué se colgó,
- tira el trabajo si estaba cargando,
- y, si la sesión retenía la única plaza de licencia, deja el estado peor que
  antes.

La excepción es lo que el usuario pida explícitamente. Si autoriza abortar,
antes de matar guarda: `tasklist` completo, `tail -50` del log, el listado del
directorio de trabajo y los `flags/computed`.

### 4.1 Autorización permanente de Juanes (2026-10-01): reinicio automático tras 1 h 30 min

Juanes autorizó, para cualquier proceso de más de 3 h, **matar y relanzar sin
preguntarle** cuando **ningún marcador de avance cambia durante 1 h 30 min**
(`CLAUDE.md` §10). El procedimiento, en orden:

1. Guardar la evidencia, que es lo que el kill destruiría:
   - cola;
   - `tail` del `.out` y del `.err`;
   - `*_p0.log` del motor;
   - listado del directorio del run;
   - en local, `tasklist` y `flags/computed`.
2. Relanzar **con los mismos parámetros**, reanudando desde el checkpoint si el
   script lo admite (`JS_REANUDAR` en los `.slurm` del cluster).
3. Pasar a depender del job nuevo los jobs que dependían del viejo
   (`scontrol update JobId=<dep> Dependency=afterany:<nuevo>`). Si no, un
   `afterany` arrancaría el dependiente en cuanto se cancele el viejo.
4. Matar el viejo (`scancel` en el cluster; en local, el proceso de Lumerical
   colgado).
5. Informar a Juanes después, con la evidencia y el nuevo identificador.

Límites:
- **Máximo 2 reinicios por trabajo.** Al tercer cuelgue se para y se le avisa: un
  cuelgue que se repite no es mala suerte, es un problema que reiniciar no
  arregla.
- **Por debajo de 1 h 30 min sin cambios no se toca nada.** Abrir una sesión,
  mallar o sincronizar logs puede tardar y no es un cuelgue.

En el cluster lo aplica `scripts/cluster/vigia.sh` (con
`~/juanes_sims/progreso.sh` como reporte de solo lectura).

---

## 5. Lo que sí se puede hacer mientras espera

Un proceso largo no bloquea la sesión. Mientras corre, adelanta lo que no
dependa de su resultado: el script de figuras (que lee del `.h5`, no del
solver), la entrada de la bitácora, el `ESTADO.md`. Cuando termine, ya solo hay
que leer los números.

Y si el barrido es reanudable —en este repositorio lo son todos, por
`flags/computed`— recuérdalo al informar: un corte no cuesta la corrida entera,
cuesta el punto en curso. Eso cambia por completo el coste de abortar.
