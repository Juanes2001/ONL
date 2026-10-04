---
name: recursos-simulaciones
description: Decidir DÓNDE y CUÁNDO puede correr una simulación de Lumerical de ONL — solo en el Lumerical local si está libre de la tesis fotonica-integrada y la RAM alcanza, o en el cluster wegener si es pesada y el cluster no tiene jobs de la tesis. Úsala SIEMPRE antes de lanzar un FDTD 3D, varFDTD, un barrido FDE/MODE o INTERCONNECT, cuando el usuario pregunte si se puede correr algo, o cuando una sesión de Lumerical se cuelgue al arrancar.
---

# Turno y recursos: ONL nunca le quita Lumerical a la tesis

## La regla (Juanes, 2026-10-04)

> **La tesis (fotonica-integrada) tiene prioridad sobre ONL, en local y en el cluster.**

1. **Local.** Las simulaciones de ONL se corren **SOLAMENTE si el Lumerical local
   está libre**: ninguna sesión ni motor de Lumerical vivo que no sea de ONL. Si
   la tesis está usando Lumerical, ONL **no lanza**, aunque la RAM alcance.
2. **Cluster.** Las simulaciones pesadas que necesitan recursos del cluster
   siguen la misma regla: se lanzan **solamente si el cluster no tiene jobs de la
   tesis corriendo ni en cola**.
3. **Nunca se interfiere con la tesis:** no se mata, no se cancela (`scancel`),
   no se re-prioriza ni se toca ningún proceso o job suyo. Tampoco se escribe en su
   repositorio ni en sus carpetas del cluster.

Si el recurso está ocupado: **no lanzar, informar con cifras y esperar** (o
preguntar a Juanes). Mientras tanto se adelanta lo que no necesita Lumerical:
scripts, análisis y GNLSE en Python.

## Relación con la regla "no hay pre-vuelo"

La skill `lumerical-arranque-simulaciones` prohíbe sondear la instalación, la
licencia o los puertos. **Esta comprobación no es eso**: no abre Lumerical ni toca
procesos. Solo lee la lista de procesos y la RAM de Windows (~5 s). Se hace
siempre, por orden de Juanes.

## 1. ¿Local o cluster?

| Va a LOCAL | Va al CLUSTER |
|---|---|
| FDE/MODE, varFDTD, FDTD 3D pequeño, INTERCONNECT | FDTD 3D que no cabe en la RAM local (abajo) o que tardaría **> 6 h** aquí |
| Necesidad estimada ≤ RAM utilizable local | Barridos 3D de muchos puntos |

Esta máquina tiene **7.4 GB de RAM** compartidos con Windows, la VM de WSL y lo que
Juanes tenga abierto. En la práctica, un FDTD 3D de más de ~3–4 GB ya es candidato
al cluster (laplace: 96 CPU, 251 GB).

## 2. Local: medir turno y RAM

```bash
python3 scripts/ram_lumerical.py --celdas 40e6          # FDTD 3D de 40 M celdas
python3 scripts/ram_lumerical.py --fde                  # sesión MODE/FDE
python3 scripts/ram_lumerical.py --necesita-gb 2.5      # necesidad ya conocida
python3 scripts/ram_lumerical.py                        # solo estado y turno
```

Se ejecuta con el Python de **Linux**, sin dependencias. Atribuye cada proceso de
Lumerical a **ONL**, **fotonica-integrada** o **sin atribuir**, según su línea de
comandos o la de sus padres (`onl_proyecto` frente a `plataforma_*`, `cascada_*`,
`pruebas_*`…). Códigos de salida:

| código | veredicto | qué se hace |
|---|---|---|
| 4 | **LUMERICAL OCUPADO** | **no se lanza**: hay una sesión o motor vivo que no es de ONL. Se informa (PID, proyecto, hora) y se espera |
| 2 | **NO CABE** | no se lanza: bajar malla o dominio, esperar, o ir al cluster |
| 1 | **AJUSTADO** | solo con confirmación de Juanes |
| 0 | **CABE** / **LIBRE** | lanzar según `lumerical-arranque-simulaciones` |
| 3 | no midió | no se lanza a ciegas; revisar `powershell.exe` |

- **"Sin atribuir" cuenta como ocupado.** Suele ser una sesión huérfana de la
  tesis (`fdtd-solutions.exe -server -hide` cuyo padre ya no existe). No se mata:
  se reporta y Juanes decide.
- `ansysli_client.exe` solo (sin sesión ni motor) no ocupa: es el cliente de
  licencias y queda vivo un rato.
- La tesis registra **una sola plaza de licencia**: es otra razón para no correr
  en paralelo.

### Estimar la necesidad

| Tipo | Estimación | Calibración |
|---|---|---|
| FDTD 3D | celdas × 40 B × 1.3 + 0.35 GB de sesión | medido aquí: 1.2–1.6 GB con 30–37 M celdas (tesis, `plataforma_v3_slot/ESTADO.md`) |
| Monitores grandes (campo en todo el dominio, muchas frecuencias) | puntos × frecuencias × 48 B, **aparte** | los 40 B/celda ya incluyen monitores de puerto pequeños |
| Sesión MODE/FDE | ~1 GB | orden de magnitud |

Celdas con malla tensorial:
`N ≈ Π_ejes [ Σ_tramos (longitud/paso) ] + 2·capas_PML por eje`.
Una caja fina impone sus líneas a todo el rango del dominio en los otros ejes. Si
hay un `<fsp>_p0.log` de una corrida parecida, su cifra manda.

## 3. Cluster: comprobar que la tesis no lo está usando

Contrato de código: `.claude/rules/fdtd-cluster.md` (aplica a
`proyecto-final/cluster/`). Guía operativa, de solo lectura:
`../fotonica-integrada/docs/cluster_guia_para_agentes.md`. Conexión con el comando
`entry_cluster` de la tesis (`../fotonica-integrada/scripts/entry_cluster`). **La
contraseña la teclea Juanes**, nunca el agente.

Antes de cada `sbatch`:

```bash
entry_cluster --status                                   # ¿conexión viva?
entry_cluster 'squeue -u $USER -o "%.8i %.24j %.8T %.10M %Z"'
```

- La cuenta del cluster es **compartida** (otras personas usan `raven_sims/`,
  `raul_sims/`…). **Jobs de la tesis** = los que tienen el directorio de trabajo
  (`%Z`) bajo `~/juanes_sims/` y **no** bajo `~/juanes_sims/onl_*`.
- **Hay un job de la tesis en `R` o `PD` → ONL no lanza.** Se informa y se espera.
- Los jobs de otras personas no bloquean, pero se cuentan para estimar la espera.
- ONL escribe **solo** en `~/juanes_sims/onl_<estudio>/`. Nunca toca las carpetas
  de la tesis ni de otros usuarios.
- **Partición `core`** (la `leve` está caída), sin `sacct`. Nunca `scancel` sin
  orden explícita de Juanes, y jamás sobre un job que no sea de ONL.

## 4. Informar

Siempre con cifras, por ejemplo: «Lumerical local ocupado: fdtd-engine PID 1234
[fotonica-integrada], 1.6 GB; ONL espera» o «local libre, disponible 3.1 GB,
necesidad ~2.0 GB: AJUSTADO, ¿lanzo?».

En corridas largas, repite la medida en cada mirada de
`vigilancia-procesos-largos`. Si mientras corre ONL arranca algo de la tesis,
**avisa a Juanes**: con **disponible < 0.3 GB** y dos procesos vivos, el cuelgue
está cerca.
