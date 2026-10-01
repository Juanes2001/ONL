# Contexto del proyecto — para retomar el trabajo en otro dispositivo

Última actualización: 2026-09-30. Este archivo resume **todo lo hecho hasta ahora** y lo necesario
para continuar sin la conversación original. Complementa `notas/bitacora-sesiones.md` (registro
cronológico) y `CLAUDE.md` (convenciones del repo).

---

## 1. Estado general

| Ítem | Estado |
|---|---|
| Estructura del repo | Hecha (commit `5f53c0f`) |
| Lectura de todo `notas/` y del enunciado de la Tarea 1 | Hecha (resúmenes en §4) |
| Tarea 1 — punto 1 | **Hecho** (manuscrito del usuario, transcrito al documento final) |
| Tarea 1 — punto 2 (a y b) | **Hecho** (scripts, figuras, PDF) — commit `ae3243c` |
| Tarea 1 — punto 3 | **Hecho** (script, figura, PDF) — commit `ae3243c` |
| Tarea 1 — punto 4 (Saleh 5.2-1, 5.3-1, 5.4-1, 3.1-4) | **Hecho** |
| Tarea 1 — documento final | **Hecho**, en revisión: `taller-01-fundamentos/Tarea_1_ONL.pdf` (formato de `talleres/Homework_3_PIC.pdf`) |
| Discrepancia del "−1" en la ecuación del diodo | **Decisión pendiente** (ver §6.1) |
| PDF de terceros en `notas/` y `talleres/` | **Decisión pendiente** (ver §6.2) |
| `bibliografia/README.md` (tabla de referencias) | Pendiente de llenar |
| `notas/generalidades-del-curso.md` | Pendiente (el contenido está en §3 de este archivo) |

---

## 2. Entorno de trabajo (dispositivo original)

- **SO:** Windows + WSL2 (Ubuntu). Repo en `/home/juanes/proyectos/ONL`.
- **MATLAB R2024b** instalado en Windows (`C:\Program Files\MATLAB\R2024b`). Se ejecuta desde WSL
  en modo batch; hay que hacer `cd` a la ruta UNC de la carpeta:
  ```bash
  "/mnt/c/Program Files/MATLAB/R2024b/bin/matlab.exe" -batch \
    "cd('\\\\wsl.localhost\\Ubuntu\\home\\juanes\\proyectos\\ONL\\talleres\\taller-01-fundamentos'); punto2a"
  ```
  (`wslpath -w <ruta>` da la ruta Windows.) La consola de MATLAB muestra mal las tildes en
  `fprintf`, pero las figuras salen bien. Las figuras se generan con `'Visible','off'` y
  `exportgraphics`.
- **LaTeX:** no hay distribución instalada. El PDF se compiló con **Tectonic 0.15.0** (binario único,
  descarga paquetes al vuelo) bajado a una carpeta temporal:
  ```bash
  curl -sSL -o t.tar.gz "https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%400.15.0/tectonic-0.15.0-x86_64-unknown-linux-musl.tar.gz"
  tar xzf t.tar.gz && ./tectonic solucion-puntos-2-3.tex
  ```
  Alternativa permanente: `sudo apt install texlive-xetex texlive-lang-spanish` y compilar con
  `xelatex` (el `.tex` usa `fontspec`, requiere XeLaTeX/LuaLaTeX). Cuidado: con `babel` en español,
  `\,\%` **dentro de modo matemático** rompe la compilación ("Incompatible glue units"); escribir el
  `\%` fuera de `$…$`.
- **Python:** `python3` del sistema sin numpy/scipy. Para leer PDF se usó PyMuPDF en un venv temporal
  (`pip install pymupdf`). No hay `pdftotext`/`pdftoppm`.

---

## 3. El curso (del programa, `notas/Programa Óptica No Lineal_02_2026.pdf`)

**Óptica No Lineal**, Escuela de Física, Universidad Nacional de Colombia — Medellín, 2026-II.
Profesor: **Rodrigo Acuña Herrera**.

- **Descripción:** fenómenos no lineales con aplicaciones en láseres, comunicaciones ópticas,
  switches ópticos, mezcladores ópticos, procesamiento de señales y solitones.
- **Objetivos:** 1) entender la literatura de óptica no lineal; 2) adquirir técnicas analíticas y
  numéricas para analizar sistemas no lineales (sólidos y guías de onda).
- **Temas:**
  1. Review: ondas electromagnéticas (Saleh 5.1, 5.2, 5.4, 2.2)
  2. Haz gaussiano (Saleh 3.1); absorción y dispersión (Saleh 5.5); pulsos en medios dispersivos (Saleh 5.6)
  3. Polarización y cristales ópticos (Saleh cap. 6)
  4. Susceptibilidad óptica no lineal (Boyd cap. 1)
  5. Interacciones ópticas no lineales (Boyd cap. 2)
  6. Índice de refracción dependiente de la intensidad y aplicaciones (Boyd 4.1, 4.2, 7.1, 7.2)
  7. Propagación de pulsos en fibras (Agrawal caps. 1 y 2)
  8. Dispersión de velocidad de grupo (Agrawal cap. 3)
  9. Automodulación, solitones y modulación cruzada (Agrawal 4.1, 4.2, 5.1, 5.2, 7.1)
  10. Raman estimulado y mezcla de cuatro ondas (Agrawal 8.1, 8.2, 10.1, 10.2)
- **Bibliografía oficial:** Saleh & Teich, *Fundamentals of Photonics* (2007); Boyd, *Nonlinear
  Optics*, 3.ª ed. (2008); Agrawal, *Nonlinear Fiber Optics*, **5.ª** ed. (2012).
- **Evaluación:** 2 exámenes (25 % c/u), tareas (25 %), proyecto final (25 %: informe tipo artículo +
  simulaciones + presentación).

---

## 4. Material disponible y resúmenes

### 4.1 `bibliografia/` (PDF ignorados por git — copiarlos a mano al otro dispositivo)

- Saleh & Teich, *Fundamentals of Photonics*.
- Boyd, *Nonlinear Optics*, 3.ª ed. **Es un escaneo sin capa de texto** (no se puede buscar texto).
  Página del PDF = página del libro + 18 (p. 1 del libro = p. 19 del PDF). Citas ya verificadas:
  ec. (1.1.2) p. 2 (expansión de P); campo atómico E_at = 5.14×10¹¹ V/m p. 3; ec. (1.2.2) p. 5 (SHG);
  ecs. (1.2.3)–(1.2.5) p. 6 (SFG/DFG); ec. (1.2.13) p. 11 (cos³, THG).
- Agrawal, *Nonlinear Fiber Optics*, **4.ª ed.** (el programa cita la 5.ª: la numeración de
  secciones puede no coincidir).

### 4.2 `notas/` (PDF sin versionar — ver §6.2)

- **`class1.pdf`** (9 pp.): Maxwell, ecuación de onda con P_NL, relaciones constitutivas (lineal,
  no dispersivo, homogéneo, isótropo), ondas planas y esféricas, haz gaussiano (q(z), w(z), R(z),
  fase de Gouy), modos Hermite-Gauss y Laguerre-Gauss, factor M².
- **`class2.pdf`** (5 pp.): absorción (χ = χ' + iχ''), absorción débil/fuerte, Kramers-Kronig,
  modelo de Lorentz, Sellmeier, velocidad de grupo, GVD, D_ν y D_λ, dispersión normal/anómala.
- **`nlo_presentation.pdf`** (42 diapositivas, "Introduction to Nonlinear Optics", **unidades
  gaussianas**): historia del láser, SHG de Franken (1961), P = χ⁽¹⁾E + χ⁽²⁾E² + χ⁽³⁾E³, SHG/SFG/DFG/OR
  (diap. 21–22), phase matching cualitativo, procesos de 3.er orden (22 componentes), n = n₀ + n₂I,
  tablas de n₂ y χ⁽³⁾ (diap. 32–33), autoenfoque, DFWM y conjugación de fase. Errata: en diap. 31 el
  paso a χ_eff cambia 3|E|²χ⁽³⁾ por 4π|E|²χ⁽³⁾. No trata diodos ni MATLAB.
- **`Hagan, Kik & Van Stryland - Fundamentals of optical science.pdf`** (191 pp.): notas del curso
  CREOL OSE5312 (UCF), SI, convención e^{i(kz−ωt)}. Caps. 15–16 (pp. 159–177): materiales no
  lineales, oscilador anarmónico, SHG, SFG/DFG (ec. 15.31, p. 163), THG. Apéndice D (p. 185):
  transformadas de Fourier. (Estas páginas las revisó un subagente; no se verificaron directamente.)

---

## 5. Tarea 1

### 5.1 Enunciado (transcrito de `talleres/Tarea 1.pdf`)

1. Una onda EM en el espacio libre tiene campo eléctrico **E** = f(t − z/c₀) x̂, con
   f(t) = exp(−t²/τ²)·exp(j2πν₀t) y τ constante (es Saleh 5.1-1). Describa la naturaleza física de la onda (polarización,
   dirección de propagación, envolvente, factor de propagación, etc.) y determine el campo magnético.
2. Use MATLAB para dibujar la amplitud de la transformada de Fourier de la salida vs. frecuencia:
   - (a) dispositivo con ley i = v², entrada v = cos(2π50t) + cos(2π120t);
   - (b) diodo mezclador con i = i₀[exp(ev/kT − 1)] **(así aparece: el −1 dentro de la exponencial,
     ver §6.1)**, i₀ = 10 pA (corriente de polarización inversa), kT/e = 26 mV; entrada
     v = 0.3 + 0.2cos(2π50t) V.
3. En 2b, estimar la relación de amplitud entre el 2.º y 3.er armónico con los términos cuadrático y
   cúbico de la serie de Taylor de la función de transferencia. Comparar con 2b.
4. Resolver de Saleh, *Fundamentals of Photonics*: 5.2-1, 5.3-1, 5.4-1 y 3.1-4.

### 5.2 Archivos (`talleres/taller-01-fundamentos/`)

| Archivo | Contenido |
|---|---|
| `punto2a.m` | FFT de i = v²; tabla FFT vs. analítico; figura |
| `punto2b.m` | FFT del diodo; comparación con Bessel; figuras lineal y log |
| `punto3.m` | Taylor vs. exacto; barrido de la razón vs. V₁; figura |
| `figuras/*.png` | `punto2a_espectro`, `punto2b_espectro`, `punto2b_espectro_log`, `punto3_taylor_vs_exacto` |
| `solucion-punto3.md` | Derivación del punto 3 en Markdown |
| `punto4_cintura_haz.py` | Cintura w₀ de un haz gaussiano dados w₁ y R₁ (Saleh 3.1-4) |
| `solucion-punto4-saleh-5.2-1a.md` | Saleh 5.2-1 (a): clasificación del medio 𝒫 = ε₀χℰ − a∇×ℰ |
| `solucion-puntos-2-3.tex` / `.pdf` | Documento completo (20 pp.) con derivaciones, figuras, verificaciones y código |

Parámetros numéricos comunes: f_s = 10 kHz, T = 1 s (N = 10 000, Δf = 1 Hz, número entero de
periodos → sin fuga espectral), espectro unilateral A_k = 2|X[k]|/N, A_0 = |X[0]|/N.
Notación del PDF: j = √−1 (para no confundir con la corriente i).

### 5.3 Resultados

**2a** — exacto: i = 1 + cos(2π70t) + ½cos(2π100t) + cos(2π170t) + ½cos(2π240t).
Líneas: DC 1 A (≈ rectificación óptica), 70 Hz 1 A (DFG), 100 Hz 0.5 A (SHG), 170 Hz 1 A (SFG),
240 Hz 0.5 A (SHG). Las frecuencias de entrada no aparecen. FFT = analítico a 6 cifras;
Parseval ⟨i²⟩ = 2.25 verificado.

**2b** — con i = i₀[e^{v/V_T} − 1] (forma de Shockley): i = I_s e^{x cos ωt} − i₀,
I_s = i₀e^{V₀/V_T} = 1.0259 µA, x = V₁/V_T = 7.6923. Por la función generatriz de Bessel
modificada, e^{x cos θ} = I₀(x) + 2Σ Iₙ(x) cos nθ ⇒ A₀ = I_s I₀(x) − i₀, Aₙ = 2 I_s Iₙ(x).

| f (Hz) | 0 | 50 | 100 | 150 | 200 | 250 | 300 | 350 |
|---|---|---|---|---|---|---|---|---|
| \|I\| (mA) | 0.3291 | 0.6137 | 0.4986 | 0.3545 | 0.2221 | 0.1235 | 0.0615 | 0.0276 |

Corriente: tren de pulsos de 2.248 mA pico (ancho ≈ 1.1 ms). Verificado: DC = media; Σ amplitudes =
i(0); Parseval (RMS 0.72 mA).

**3** — Taylor hasta orden 3 alrededor de V₀: A₂f = I_s x²/4, A₃f = I_s x³/24 ⇒
**A₂f/A₃f = 6V_T/V₁ = 0.78**, frente al exacto **I₂(x)/I₃(x) = 1.4065** (error −44.5 %; amplitudes
absolutas 10–30× por debajo). Falla porque x ≈ 7.7 ≫ 1 (1 + x + x²/2 + x³/6 = 114 vs. eˣ = 2191).
Taylor es el límite x ≪ 1 de Bessel (Iₙ ≈ (x/2)ⁿ/n! ⇒ 6/x); error < 10 % solo si V₁ < 63 mV.
Expandiendo alrededor de v = 0 se obtiene 6(V_T + V₀)/V₁ = 9.78 (peor). Analogía: V_T ↔ E_at.

**4 — Saleh 5.2-1 (a)** — 𝒫 = ε₀χℰ − a∇×ℰ: lineal (∇× es lineal), homogéneo, no dispersivo en
el tiempo, **espacialmente dispersivo** (con ondas planas, P = ε₀χE + j a k×E: depende de k) e
isótropo (supuesto; es el modelo de un medio quiral u ópticamente activo). Definiciones: Saleh
§5.2, p. 156. Nota: el PDF de Saleh es escaneado; página del PDF = página del libro + 22.

---

## 6. Decisiones pendientes

### 6.1 El "−1" en la ecuación del diodo

El enunciado escribe i = i₀[exp(ev/kT − 1)]. Se resolvió con la forma de Shockley
i₀[exp(ev/kT) − 1], por considerarse un error de digitación:
1. con v = 0 debe ser i = 0 (la forma literal da i₀/e ≈ 3.7 pA);
2. i₀ se llama "corriente de polarización inversa": solo con Shockley i → −i₀ en inversa fuerte;
3. Shockley es la ecuación estándar.

Si se toma literal, i = (i₀/e)e^{v/V_T}: mismo espectro escalado por 1/e ≈ 0.368 (DC 0.1211 mA,
50 Hz 0.2258, 100 Hz 0.1834, 150 Hz 0.1304 mA; pico 0.827 mA). **El punto 3 no cambia** (la razón
sigue siendo 1.4065 y Taylor 0.78, porque el factor constante se cancela).

Propuesta hecha al usuario (sin respuesta aún): mantener Shockley como resultado principal y agregar
al PDF un recuadro con esta discusión y la tabla de la forma literal.

### 6.2 PDF de terceros sin versionar

`notas/*.pdf` (clases, presentación, programa, notas de Hagan) y `talleres/Tarea 1.pdf` **no están en
el repo** (repo público; material con derechos de autor). Opciones planteadas: ignorarlos en
`.gitignore` como `bibliografia/`, o subir solo algunos (programa, enunciado). En el otro
dispositivo hay que copiarlos a mano si se necesitan.

---

## 7. Próximos pasos sugeridos

1. Resolver §6.1 (y, si se acepta, añadir el recuadro al PDF y recompilar).
2. Punto 1 de la Tarea 1 (pulso gaussiano que viaja en +z, polarización x̂;
   **H** = (1/η₀) f(t − z/c₀) ŷ).
3. Punto 4: Saleh 5.2-1 (b)–(d), 5.3-1, 5.4-1 y 3.1-4 (5.2-1 (a) ya está hecho).
4. Llenar `bibliografia/README.md` y crear `notas/generalidades-del-curso.md` (usar §3).
5. Registrar cada sesión en `notas/bitacora-sesiones.md`.
