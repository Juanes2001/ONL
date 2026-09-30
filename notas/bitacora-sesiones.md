# Bitácora de sesiones de trabajo

Registro de cada sesión de trabajo en el repositorio: qué se hizo, qué decisiones se tomaron y
qué queda pendiente. La entrada más reciente va arriba.

## 2026-09-30 (miércoles) — Tarea 1, punto 4: Saleh 5.2-1 (a)

### Hecho
- `git pull`: llegó `talleres/taller-01-fundamentos/punto4_cintura_haz.py` (cálculo de la cintura
  w₀ de un haz gaussiano, trabajado por el usuario en el otro dispositivo).
- Lectura completa del cap. 5 de Saleh & Teich (§5.1–5.7, pp. 149–195 del libro = pp. 171–217 del
  PDF). El PDF es escaneado y no tiene texto extraíble: se leyó renderizando las páginas con
  PyMuPDF. Desfase de páginas: página del PDF = página del libro + 22.
- Saleh 5.2-1 (a), 𝒫 = ε₀χℰ − a∇×ℰ: lineal, homogéneo, no dispersivo en el tiempo,
  **espacialmente dispersivo** (P = ε₀χE + j a k×E) e isótropo (supuesto; medio quiral u
  ópticamente activo). Solución en
  `talleres/taller-01-fundamentos/solucion-punto4-saleh-5.2-1a.md`.
- Se comparó con el razonamiento del usuario: coincide en lineal, homogéneo y no dispersivo.
  Le faltaba la dispersión espacial, y su justificación de la linealidad (que "∇×ℰ es un campo
  independiente") no era correcta: la linealidad se debe a que ∇× es un operador lineal.

### Pendiente
- Saleh 5.2-1 (b)–(d), 5.3-1, 5.4-1 y 3.1-4 (este último ya tiene `punto4_cintura_haz.py`).
- Punto 1 de la Tarea 1; decisiones pendientes de `notas/contexto-proyecto.md` §6.

## 2026-09-27 (domingo) — Tarea 1, punto 2

### Hecho
- Revisión de `notas/`: programa del curso, clases 1 y 2, `nlo_presentation.pdf` (unidades
  gaussianas) y notas OSE5312 de Hagan, Kik & Van Stryland (SI; cap. 15–16 no lineal).
- Se verificó que MATLAB R2024b (Windows) se ejecuta desde WSL en modo `-batch`.
- `talleres/taller-01-fundamentos/punto2a.m` (i = v²) y `punto2b.m` (diodo mezclador):
  espectros de amplitud por FFT (fs = 10 kHz, T = 1 s, Δf = 1 Hz), validados contra la
  solución analítica (expansión trigonométrica y funciones de Bessel modificadas Iₙ(x),
  x = 0.2/0.026). Figuras en `talleres/taller-01-fundamentos/figuras/`.
- Punto 3: `punto3.m` y `solucion-punto3.md`. Razón I₂f/I₃f por Taylor (alrededor de V₀)
  = 6V_T/V₁ = 0.78 vs. exacta I₂(x)/I₃(x) = 1.4065 (error −44.5 %); Taylor válido (<10 %)
  solo para V₁ < 63 mV.
- Documento `solucion-puntos-2-3.pdf` (20 pp., fuente `solucion-puntos-2-3.tex`) con la
  derivación completa de los puntos 2 y 3, figuras, verificaciones y código. Se compila con
  Tectonic (`tectonic solucion-puntos-2-3.tex`); no hay LaTeX instalado en el sistema.

### Pendiente
- Puntos 1 y 4 (Saleh 5.2-1, 5.3-1, 5.4-1, 3.1-4).
- Registrar la bibliografía en `bibliografia/README.md`; crear `notas/generalidades-del-curso.md`.

## 2026-09-26 (sábado) — Creación del repositorio

### Hecho
- Se creó el repositorio `ONL` con la estructura inicial: `bibliografia/`, `talleres/`,
  `proyecto-final/`, `notas/`, `scripts/`, `datos/` y `figuras/`.
- Los PDF de `bibliografia/` quedan fuera del repo (`.gitignore`) por derechos de autor.

### Pendiente
- Agregar el programa y calendario del curso en `notas/generalidades-del-curso.md`.
- Cargar la bibliografía del curso y registrarla en `bibliografia/README.md`.
