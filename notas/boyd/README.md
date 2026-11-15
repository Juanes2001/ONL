# Apuntes del Boyd, *Nonlinear Optics*, 3.ª ed. (Academic Press, 2008)

Lectura completa del libro, capítulo por capítulo, hecha el 2026-11-14 a partir del PDF escaneado
de `bibliografia/`. El PDF **no tiene capa de texto** y se leyó renderizando cada página como imagen.
Regla de páginas: **página del PDF = página del libro + 18**. La tabla de contenido del escaneo está
en PDF 14–18, después de los prefacios; está transcrita en `apendices.md` §2.

Cada archivo `capNN-<tema>.md` contiene:
- mapa de secciones con páginas;
- resumen por sección con las ecuaciones clave, numeradas como en el libro;
- tablas y datos numéricos;
- **todos los problemas del capítulo transcritos**;
- relación con el programa del curso y con el proyecto final;
- erratas o dudas de lectura, marcadas explícitamente en vez de corregidas en silencio.

Convención del libro (SI): $\tilde E=Ee^{-i\omega t}+\text{c.c.}$, $\tilde P=\epsilon_0[\chi^{(1)}\tilde E+\chi^{(2)}\tilde E^2+\chi^{(3)}\tilde E^3+\dots]$,
$I=2n\epsilon_0c|E|^2$, $d=\chi^{(2)}/2$. La tabla de equivalencias con el Saleh está en
`notas/saleh/README.md` y en `notas/saleh/cap21-optica-no-lineal.md`.

## Mapa de capítulos

| Cap. | Título | Pág. libro | Pág. PDF | Apuntes | Programa ONL |
|---|---|---|---|---|---|
| — | Front matter, contenido; Apéndices A–E (unidades SI/gaussianas, conversión, $I$–$E$, constantes) | i–xvi; 589–604 | 1–18; 607–622 | `apendices.md` | Tema 4 (unidades) |
| 1 | The Nonlinear Optical Susceptibility | 1–67 | 19–85 | `cap01-susceptibilidad-optica-no-lineal.md` | **Tema 4** |
| 2 | Wave-Equation Description of Nonlinear Optical Interactions | 69–133 | 87–151 | `cap02-descripcion-ondulatoria-interacciones-no-lineales.md` | **Tema 5** |
| 3 | Quantum-Mechanical Theory of the Nonlinear Optical Susceptibility | 135–206 | 153–224 | `cap03-teoria-cuantica-susceptibilidad.md` | apoyo |
| 4 | The Intensity-Dependent Refractive Index | 207–252 | 225–270 | `cap04-indice-dependiente-de-intensidad.md` | **Tema 6** (4.1, 4.2) |
| 5 | Molecular Origin of the Nonlinear Optical Response | 253–275 | 271–293 | `cap05-origen-molecular-respuesta-no-lineal.md` | — |
| 6 | Nonlinear Optics in the Two-Level Approximation | 277–328 | 295–346 | `cap06-aproximacion-de-dos-niveles.md` | — |
| 7 | Processes Resulting from the Intensity-Dependent Refractive Index | 329–390 | 347–408 | `cap07-procesos-indice-dependiente-intensidad.md` | **Tema 6** (7.1, 7.2) |
| 8 | Spontaneous Light Scattering and Acoustooptics | 391–428 | 409–446 | `cap08-dispersion-espontanea-y-acustooptica.md` | — |
| 9 | Stimulated Brillouin and Stimulated Rayleigh Scattering | 429–471 | 447–489 | `cap09-brillouin-y-rayleigh-estimulados.md` | apoyo (tema 10) |
| 10 | Stimulated Raman Scattering and Stimulated Rayleigh-Wing Scattering | 473–509 | 491–527 | `cap10-raman-estimulado.md` | apoyo (tema 10) |
| 11 | The Electrooptic and Photorefractive Effects | 511–541 | 529–559 | `cap11-electrooptica-y-fotorrefractividad.md` | — |
| 12 | Optically Induced Damage and Multiphoton Absorption | 543–560 | 561–578 | `cap12-dano-optico-y-absorcion-multifotonica.md` | proyecto (TPA en Si) |
| 13 | Ultrafast and Intense-Field Nonlinear Optics | 561–587 | 579–605 | `cap13-optica-no-lineal-ultrarrapida-y-campos-intensos.md` | apoyo (SC, NLSE) |
| — | Índice analítico | 605–613 | 623–631 | (`apendices.md` §8) | — |

La PDF 632 no pertenece al libro: es una hoja de metadatos del digitalizador.

## Erratas y dudas más relevantes para el curso

Hay una lista completa al final de cada apunte. Las más relevantes:

- **(1.2.14b), p. 12:** imprime $n_2=3\chi^{(3)}/(2n_0^2\epsilon_0c)$. Lo correcto, como en la (4.1.19), es $3\chi^{(3)}/(4n_0^2\epsilon_0c)$.
- **Tabla 1.5.3, p. 50:**
  - KDP y KD*P aparecen como "2m"; son de la clase $\bar42m$.
  - En LiNbO₃ dice "$d_{32}=-30$"; debería ser $d_{33}$.
- **Tabla 1.5.2, p. 47:** en la clase 3 dice "−yyz", debería ser −yyx; en la clase 622 dice "xzy=−yxz", debería ser xzy=−yzx.
- **§1.5.8:** el plano espejo de 3m contiene al eje ternario, no es perpendicular a él.
- **(2.7.19), p. 99:** el factor $1/(\epsilon_0cI)$ debería ser $\epsilon_0c/I$.
- **(2.4.4):** exponente del cuasi-ajuste de fase.
- **(2.11.17), (2.10.14):** quedan restos de unidades gaussianas.
- **(4.2.12a):** sobran los $\epsilon_0$.
- **Cap. 7:**
  - (7.3.5) es $I=2n\epsilon_0c|A|^2$; al libro le falta la $c$.
  - Hay inconsistencias de signo en $\kappa_2$ en la conjugación de fase, entre (7.2.23b) y (7.2.24b).
- **Caps. 12–13 y §4.4, §5.1, §5.6, §9.6:** varios restos gaussianos de la conversión a SI de la 3.ª edición.

## Relación con el examen 1 (temas 1–4)

El tema 4 es el cap. 1 completo. Material preparado a partir de estos apuntes y de los del Saleh:
- `notas/examen-1/resumen-examen-1.pdf`: resumen de fórmulas para consultar durante el examen.
- `notas/examen-1/taller-repaso-examen-1.pdf`: taller de repaso de 39 problemas con respuestas.
