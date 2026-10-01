# Bitácora de sesiones de trabajo

Registro de cada sesión de trabajo en el repositorio: qué se hizo, qué decisiones se tomaron y
qué queda pendiente. La entrada más reciente va arriba.

## 2026-09-30 (miércoles, tarde) — Tarea 1: documento final

### Hecho
- Lectura del manuscrito del usuario (`talleres/Tarea1.pdf`, 16 pp.): punto 1 y punto 4
  (3.1-4, 5.2-1 a, 5.3-1, 5.4-1). Enunciados verificados en Saleh (pp. 195 y 84 del libro).
- El punto 1 es Saleh 5.1-1: f(t) = exp(−t²/τ²)·exp(j2πν₀t) (con portadora; la transcripción
  anterior de este repo la omitía).
- Documento final `talleres/taller-01-fundamentos/Tarea_1_ONL.tex` / `.pdf` (22 pp.) con el
  formato de `talleres/Homework_3_PIC.pdf`: puntos 1–4 (a pedido del usuario, sin sección de
  referencias ni apéndice de código; las fuentes se citan en línea).
  Compila con Tectonic.
- Redactados en el estilo del inciso (a): Saleh 5.2-1 (b) no lineal/no dispersivo/local/homogéneo,
  (c) lineal/dispersivo (oscilador de Lorentz)/local/homogéneo, (d) lineal/no dispersivo/local/
  inhomogéneo.
- Verificación del manuscrito: punto 1, 3.1-4 y 5.4-1 correctos. **Errores corregidos en 5.3-1**:
  (a) β = k₀/√2 (no 2π/λ₀: el campo no es onda plana y debe cumplir Helmholtz); (b) H tiene además
  componente H_z = −j(E₀/√2η₀)cos(βy)e^{−jβz} (el reemplazo ∇ → −jk solo vale para ondas planas).
  (c) y (d) quedan igual (la potencia promedio va en +z; la parte en y es reactiva).
- En 2b se incluyó la nota sobre el "−1" del enunciado (se mantiene Shockley; §6.1 del contexto).

### Pendiente
- Revisión del usuario del documento final; decidir si se sube `Tarea1.pdf`/`Homework_3_PIC.pdf`
  al repo (PDF de terceros sin versionar).

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
