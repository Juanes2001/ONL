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
