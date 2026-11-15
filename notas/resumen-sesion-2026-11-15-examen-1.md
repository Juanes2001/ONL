# Resumen de la sesión 2026-11-14 → 2026-11-15: preparación del Examen 1 y lectura del Boyd

Resumen de la conversación con Claude Code, para no perder el contexto si se cierra el chat.

## Pedido de Juanes

1. Leer el programa del curso. El Examen 1 es el **miércoles 2026-11-18** y cubre los **temas 1–4**:
   - Saleh 5.1, 5.2, 5.4, 2.2;
   - Saleh 3.1, 5.5, 5.6;
   - Saleh cap. 6;
   - Boyd cap. 1.
2. Usar los apuntes del Saleh, que ya estaban leídos completos en `notas/saleh/`.
3. Leer **todo** el Boyd y generar sus apuntes en `.md`.
4. Hacer un **resumen de fórmulas y teoría** en un solo PDF; el profesor permite tenerlo durante el examen.
5. Hacer un **taller completo** con ejercicios de ambos libros, parecidos a los de las tareas 1 y 2, también en PDF.

## Qué se hizo

### Programa del curso
`notas/Programa Óptica No Lineal_02_2026.pdf` (Prof. Rodrigo Acuña Herrera) trae diez temas:

| Tema | Contenido | Fuente |
|---|---|---|
| 1 | Ondas EM | Saleh 5.1, 5.2, 5.4, 2.2 |
| 2 | Haz gaussiano; absorción y dispersión; pulsos | Saleh 3.1, 5.5, 5.6 |
| 3 | Polarización y cristales | Saleh cap. 6 |
| 4 | Susceptibilidad no lineal | Boyd cap. 1 |
| 5 | Interacciones no lineales | Boyd cap. 2 |
| 6 | Índice dependiente de la intensidad | Boyd 4.1, 4.2, 7.1, 7.2 |
| 7–10 | Fibras | Agrawal |

Evaluación: dos exámenes (25 % cada uno), tareas 25 % y proyecto final 25 %.

### Lectura completa del Boyd → `notas/boyd/`
- PDF escaneado sin texto, 632 páginas. **Página del PDF = página del libro + 18.**
- Se leyó con 9 agentes en paralelo. Cada uno renderizó las páginas de su tramo con PyMuPDF (Python de Windows) a unos 110 dpi, y a 200 dpi donde hacía falta. Las instrucciones comunes estaban en un brief del scratchpad, que no se conserva.
- Resultado: 14 archivos y un `README.md` índice, unas 10 000 líneas en total. Cada capítulo tiene:
  - las secciones con sus ecuaciones numeradas en LaTeX;
  - tablas y datos numéricos;
  - **todos los problemas transcritos**;
  - la relación con el curso y con el proyecto;
  - las erratas marcadas.
- Páginas reales de cada capítulo:

  | Cap. | Pág. libro | Cap. | Pág. libro |
  |---|---|---|---|
  | 1 | 1–67 | 8 | 391–428 |
  | 2 | 69–133 | 9 | 429–471 |
  | 3 | 135–206 | 10 | 473–509 |
  | 4 | 207–252 | 11 | 511–541 |
  | 5 | 253–275 | 12 | 543–560 |
  | 6 | 277–328 | 13 | 561–587 |
  | 7 | 329–390 | Apéndices | 589–604 |

  El índice analítico va de la p. 605 a la 613. La tabla de contenido está en PDF 14–18 y quedó transcrita en `apendices.md` §2.
- Problemas transcritos por capítulo:

  | Cap. | Problemas | Cap. | Problemas |
  |---|---|---|---|
  | 1 | 12 | 8 | 7 |
  | 2 | 22 | 9 | 6 |
  | 3 | 9 | 10 | 2 |
  | 4 | 11 | 11 | 3 |
  | 5 | 3 | 12 | 2 |
  | 6 | 7 | 13 | 1 |
  | 7 | 19 | | |

### Resumen para el examen → `notas/examen-1/resumen-examen-1.tex` / `.pdf`
- 4 páginas, dos columnas, 9 pt. Se compila con Tectonic.
- §0 trae las constantes y una **tabla de convenciones Saleh ↔ Boyd**:
  - $e^{j\omega t}$ frente a $e^{-i\omega t}$;
  - $E_{\rm Saleh}=2E_{\rm Boyd}$;
  - el signo de $\chi''$;
  - $\mathrm d_{\rm Saleh}=\epsilon_0\chi^{(2)}/2$ y $\chi^{(3)}_{\rm Saleh}=\epsilon_0\chi^{(3)}_{\rm Boyd}/4$.
- §1–§4: un bloque por tema, con las fórmulas y la cita (ecuación y página).
- Al final, "cómo atacar un problema típico".

### Taller de repaso → `notas/examen-1/taller-repaso-examen-1.tex` / `.pdf`
- 10 páginas, **39 problemas**: 1–7 tema 1; 8–17 tema 2; 18–27 tema 3; 28–39 tema 4.
- [N] marca los que piden cálculo o programa; [⋆] los de mayor profundidad.
- No repite los problemas ya resueltos en las tareas: S 5.1-1, 5.2-1a, 5.3-1, 5.4-1, 3.1-4, Ej. 5.5-1, 6.1-8, 6.2-5, 6.3-2 y 6.6-2.
- Problemas destacados:
  - simulación con FFT del oscilador anarmónico (análogo al diodo de la Tarea 1);
  - Kramers–Kronig numérico;
  - Sellmeier de la sílice y del GaAs;
  - compresión de un pulso con chirp;
  - ajuste de fase en BBO con el elipsoide de índices;
  - $d_{\rm eff}$ de BBO y GaAs;
  - $n_2$ de la sílice, el SiN y el Si;
  - un problema integrador del oscilador al cristal.
- **Respuestas numéricas** al final. Las calculó Claude con scripts de Python que no se guardaron; conviene verificarlas al resolver. Valores de control:

  | Problema | Resultado |
  |---|---|
  | 9 | $W_0=0.200$ mm, cintura a 10.0 cm del primer plano |
  | 15 | sílice: $D_\lambda=0$ en 1.273 µm; $\beta_2(1.55)=-28.0$ ps²/km. GaAs: cero de dispersión en 6.84 µm |
  | 17 | 100 fs en 1 cm de sílice → 100.5 fs; 20 fs → 53.9 fs |
  | 21 | rombo de Fresnel con $n=1.51$: 48.6° y 54.6° |
  | 24 | BBO: $\theta_{pm}=22.9°$, walk-off 3.19°, $L_c=13.4$ µm |
  | 25 | KTP: $V_z=17.3°$ |
  | 29 | Boyd Prob. 1.2: $P(2\omega)=4.72\times10^{-11}$ C/m² |
  | 35 | GaAs [111]: $d_{\rm eff}=2d_{14}/\sqrt3=427$ pm/V |

### Erratas encontradas (importantes para el examen)
- **Boyd (1.2.14b):** imprime $n_2=3\chi^{(3)}/(2n_0^2\epsilon_0c)$; lo correcto es $3\chi^{(3)}/(4n_0^2\epsilon_0c)$, como en la (4.1.19).
- **Boyd, Tabla 1.5.3:**
  - KDP aparece como "2m"; es de la clase $\bar42m$.
  - En LiNbO₃ dice "$d_{32}=-30$"; es $d_{33}$.
- **Boyd, Tabla 1.5.2:** en la clase 3 dice "−yyz", debería ser −yyx; en la clase 622 dice "xzy=−yxz", debería ser xzy=−yzx.
- **Boyd §1.5.8:** el plano espejo de 3m contiene al eje ternario, no es perpendicular a él.
- **Lo que el Boyd no trae:** el valor numérico del δ de Miller, y $d_{\rm eff}$ para clases distintas de 3m. En los apuntes van marcados como datos de la literatura, para verificar.
- **Saleh (6.2-13), p. 213, verificado renderizando la página:** la fórmula de la fase TM en reflexión total da 0 en $\theta_c$, pero la Fig. 6.2-5 muestra π.
  - Calculando directamente con Fresnel (6.2-8)–(6.2-9), con vidrio a $1.2\,\theta_c$: $\varphi_{TE}=+61.5°$, $\varphi_{TM}=-73.5°$.
  - El retardo es 135° en la convención de Saleh, que equivale a 45° en la de Born & Wolf.
- Erratas de los demás capítulos: al final de cada apunte y resumidas en `notas/boyd/README.md`.

## Archivos creados o modificados en la sesión

| Archivo | Cambio |
|---|---|
| `notas/boyd/*.md` | nuevos: 14 apuntes y `README.md` |
| `notas/examen-1/` | nuevos: los dos `.tex` y sus PDF |
| `notas/bitacora-sesiones.md` | entrada 2026-11-14 → 2026-11-15 |
| `bibliografia/README.md` | Boyd marcado como leído completo |
| `notas/resumen-sesion-2026-11-15-examen-1.md` | este archivo |
| memoria de Claude Code | `apuntes-boyd-completos.md`, local y fuera del repo |

**Nada se ha subido a git.** La rama actual es `taller-02-y-apuntes`, que además ya tenía cambios pendientes de sesiones anteriores.

## Entorno usado
- **Compilación:**
  ```bash
  cd notas/examen-1 && ../../talleres/taller-02-dispersion-polarizacion/tectonic <archivo>.tex
  ```
  El binario de Tectonic, `tectonic`, está en la carpeta del taller 2 y no está en git. Compila sin errores.
- **Python con PyMuPDF, numpy y scipy:** `/mnt/c/Users/jero0/AppData/Local/Programs/Python/Python311/python.exe`.
- **Preámbulo LaTeX:** babel con `es-noshorthands,es-nodecimaldot,es-tabla`. Los símbolos ↔ y ★ no existen en Latin Modern; se usan `$\leftrightarrow$` y `$\star$`.

## Pendiente
- Resolver el taller de repaso antes del miércoles 2026-11-18. Verificar las respuestas y avisar si alguna no cuadra.
- Decidir si se hace commit de `notas/boyd/` y `notas/examen-1/`. Los apuntes y los PDF propios sí pueden ir al repo; los PDF de los libros no.
- Después del examen: repasar en los apuntes del Boyd los caps. 2 (tema 5), 4 y 7 (tema 6).
- Siguen los pendientes del proyecto final (ver `notas/resumen-sesion-2026-11-14-proyecto-final.md`).
