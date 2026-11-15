# Resumen de la sesión del 2026-11-12 al 2026-11-14 — proyecto final: estado del arte y referencias

**Fecha de cierre: 2026-11-14 (sábado).** Rama `taller-02-y-apuntes`. Ningún archivo de esta sesión
tiene commit (Juanes no lo ha pedido).

Este archivo basta para retomar el proyecto final en otro chat. Orden de lectura sugerido:
`CLAUDE.md` → este archivo → `proyecto-final/referencias-a-descargar.md` →
`proyecto-final/reports/Propiedades no lineales SiN y Si.md` →
`proyecto-final/simulaciones/seccion_v1/ESTADO.md` §0.

Para arrancar el siguiente chat:

> Lee `notas/resumen-sesion-2026-11-14-proyecto-final.md` y continúa con el protocolo de cálculo
> de supercontinuo en SiN.

---

## 1. Qué se pidió y qué se hizo, en orden

1. **Volver a contextualizarse con el proyecto final** (supercontinuo en anillos de SiN) y
   recordar el estado del arte y qué artículos descargar para anillos all-pass y add-drop.
   - Se releyeron `notas/contexto-proyecto.md`, las memorias, el informe
     `proyecto-final/reports/Estado del arte supercontinuo en anillos.md` (118 refs, DOI
     verificados el 2026-10-30) y `proyecto-final/simulaciones/seccion_v1/ESTADO.md`.
   - Se creó `proyecto-final/lectura-estado-del-arte.md`: lista de lectura por bloques con
     casillas (fundamentos de anillo y LLE; solitón + ondas dispersivas; SiN delgado y dispersión
     normal; bombeo pulsado; add-drop, agua y sensado).
2. **Dónde leer sobre supercontinuo en detalle y cómo llevarlo a chip; estado de Lumerical para
   no lineal (v202 local y v261 del cluster).**
   - Se ubicaron en el Agrawal local (4.ª ed., **página del PDF = página del libro + 4**,
     comprobado) las secciones de supercontinuo y sus requisitos (ver §3).
   - Se agregó a la lista de lectura un "Bloque 0" de supercontinuo (fibra → chip).
   - Se resumió lo que puede Lumerical en no lineal, a partir del informe
     `reports/Simulación no lineal anillos add drop.md` (ver §4).
3. **Búsqueda profunda (nov-2021 → nov-2026) sobre propiedades no lineales del SiN y del Si**,
   más supercontinuo en guías de ambos, con lista corta de artículos para descargar.
   - Primero se respondió si ya se había buscado (ver §2).
   - Cuatro frentes de investigación en paralelo; notas en
     `proyecto-final/research_notes/Propiedades no lineales SiN y Si/`
     (`propiedades_no_lineales_SiN.md`, `supercontinuo_guias_SiN.md`,
     `propiedades_no_lineales_Si.md`, `supercontinuo_guias_Si_y_comparacion.md`).
   - Informe: `proyecto-final/reports/Propiedades no lineales SiN y Si.md` (ver §5).
   - Después de redactarlo se cotejaron en Crossref los 10 DOI marcados "por confirmar":
     todos coinciden. **Corrección:** *Opt. Express* 21, 32192 (2013), n₂ y absorción
     multifotónica en Si en el IR medio, es de **T. Wang et al.**, no de "Gai" como decían las
     notas (corregido en el informe, no en las notas crudas).
4. **Juntar todas las referencias a descargar en un solo documento.**
   - `proyecto-final/referencias-a-descargar.md`: 67 referencias sin duplicar, **22 prioritarias
     (★)**, con enlace DOI/arXiv y acceso (OA, arXiv o de pago). Secciones: 0 bases del
     supercontinuo; A SiN; B Si; C microanillos (incluye todo lo seleccionado del estado del arte
     de anillos). Se verificaron en Crossref también Bogaerts 2012, Kippenberg 2004, Heidt 2010,
     Tian 2026, Ren 2024 y Brès 2023. Quedan sin verificar 4: libro de Dudley & Taylor,
     Xiang 2022, Zhang 2025 (arXiv) y Della Torre 2021.
   - `proyecto-final/lectura-estado-del-arte.md` ahora remite a ese archivo en su primera línea y
     queda como guía de lectura por bloques (con las páginas del Agrawal).
5. **PDF de la lista.** `proyecto-final/referencias-a-descargar.pdf` (4 pp., A4, enlaces
   clicables, 3 MB por las fuentes incrustadas). Generado con PyMuPDF (`Story`) y el módulo
   `markdown` del Python de Windows; el script quedó en el scratchpad de la sesión (temporal, no
   en el repo). Para regenerarlo: markdown → HTML → `pymupdf.Story(...).write_with_links(...)`,
   con fuentes Segoe UI de `C:\Windows\Fonts`.
   - **Ningún artículo está descargado todavía.** En `bibliografia/` solo están Saleh, Agrawal y
     Boyd. Se ofreció bajar automáticamente los ~35 gratuitos a `bibliografia/articulos/`;
     Juanes no lo ha pedido.

## 2. ¿Ya se habían buscado las propiedades no lineales del SiN?

Solo en parte. `proyecto-final/referencias-no-lineal-SiN.txt` (búsqueda web del 2026-10-04,
DOI verificados) cubre χ⁽³⁾, supercontinuo, χ⁽²⁾ y sensado en SiN, pero su sección de propiedades
tiene solo 3 artículos anteriores a 2016 (Ikeda 2008, Tan 2010, Krückel 2015) y nada de silicio.
Por eso se hizo la búsqueda nueva. Ojo: Halir 2012, Johnson 2015, Epping 2015, Porcel 2017 y
Rebolledo-Salgado 2022 ya estaban verificados en esa lista.

## 3. Dónde leer sobre supercontinuo (Agrawal 4.ª ed., local)

| Tema | Sección | Páginas del libro |
|---|---|---|
| GNLSE | §2.3 | 31 |
| Dispersión de tercer orden | §3.3 | 62 |
| SPM; SPM con GVD | §4.1–4.2 | 79, 89 |
| Solitones | §5.2 | 129 |
| Efectos de orden superior (TOD, self-steepening, Raman) | §5.5 | 156–167 |
| γ y A_eff | §11.1 | 424 |
| **Supercontinuum Generation** | **§12.3** | **469–477** |
| **Temporal and Spectral Evolution** (modelado, fisión, coherencia) | **§12.4** | **477–495** |

Luego: Dudley, Genty & Coen, RMP 2006 (revisión canónica); Brès et al., *Nanophotonics* 2023
(supercontinuo en chip, OA); para el régimen de la guía de 400 nm (dispersión normal: SPM +
rompimiento de onda), Heidt 2010 y Rebolledo-Salgado 2022.

## 4. Lumerical para no lineal: v202 local frente a v261 del cluster

**Ninguna versión trae solver de la LLE ni simula peines o supercontinuo dentro de un anillo.**

| Capacidad | v202 (2020 R2, local) | v261 (2026 R1, cluster) |
|---|---|---|
| FDTD/varFDTD con χ⁽³⁾ ("Chi3/Chi2", "Chi3 Raman Kerr", "Kerr nonlinear", "Chi2") | Sí | Sí (no en GPU) |
| MODE FDE: n_eff, n_g, D, A_eff (γ a mano) | Sí | Sí |
| INTERCONNECT `FIBER` (GNLSE de fibra) | Probable, sin verificar | Sí |
| INTERCONNECT `NLSE_WGD` (GNLSE de guía; solo β₂, β₃) | No | Sí |
| INTERCONNECT `NL_RING` (add-drop 0-D: térmico, TPA, portadores) | No | Sí |
| `NL_RING` con Kerr | No | Solo con service pack ≥ R1.3: **sin comprobar** |
| Peine de Kerr / LLE | No | No |

Plan que se mantiene: FDE (local) → GNLSE y LLE add-drop propias en Python; `NLSE_WGD` del cluster
solo como contraste; FDTD del anillo completo descartado (Q = 10⁴ → τ_foton ≈ 8 ps; un peine pide
miles). Pendiente: confirmar el service pack de la v261 con un comando de solo lectura.

## 5. Resultados de la búsqueda de propiedades no lineales (informe del 2026-11-14)

**SiN**
- n₂(Si₃N₄ LPCVD, 1550 nm) = (2.2 ± 0.1)×10⁻¹⁹ m²/W sin artefacto térmico (Gao et al.,
  *Nat. Commun.* 13, 3323, 2022, OA); 1.62–2.44×10⁻¹⁹ según la estequiometría, regla de Miller
  (Tian et al., *Opt. Lett.* 51, 4424, 2026, de pago).
- Para el protocolo: n₂ central 2.4×10⁻¹⁹ m²/W, barrido 2.2–2.5×10⁻¹⁹ (más bajo si n₀ < 1.95);
  β_TPA = 0; sin portadores; Raman f_R = 0 en el caso base (solo prueba de sensibilidad).
- γ: calcular escalar (Lumerical) y vectorial (Afshar & Monro, *Opt. Express* 17, 2298, 2009) y
  reportar la diferencia (hasta ~2× en guías de alto contraste).
- Única octava en SiN de 400 nm: con recubrimiento de TeO₂ que sube γ ~2.5× (Mbonde et al.,
  arXiv:2309.08318; 258 W, 100 fs, 1565 nm). Sin recubrimiento se espera supercontinuo coherente
  por debajo de una octava (SPM + rompimiento de onda en dispersión normal).
- **No hay supercontinuo publicado en SiN con cladding de agua** → hueco que el proyecto puede ocupar.

**Si**
- Sin mediciones nuevas en 2021–2026. Valores de referencia (Sinclair 2019): n₂ = 5.2×10⁻¹⁸ m²/W,
  β_TPA = 7.6×10⁻¹² m/W (0.76 cm/GW), FOM ≈ 0.44. γ ~200× el del SiN, pero la TPA consume la
  potencia en ~0.1 mm a 100 W.
- El frente reciente se fue al IR medio con SiGe/Ge (Calcaterra 2025: 4–13 µm, 311 W) y a los
  nitruros ricos en Si (Cao 2022: 17 pJ a 1555 nm).
- Constantes de portadores libres y de Raman del Si quedaron **[NV]** (de memoria): cotejarlas en
  Lin, Painter & Agrawal 2007.

**Lo que más pesa en el resultado:** no n₂, sino el β(ω) de la guía de 400 nm (nadie lo ha
publicado; interpolación previa: β₂ ≈ +400 a +800 ps²/km con óxido) y la pérdida por el agua
(~5–15 dB/cm a 1550 nm con Γ_agua 0.1–0.3). Por eso lo primero es correr el FDE de `seccion_v1`
con los dos claddings.

**Sin verificar en el informe:** coeficientes del Sellmeier de Luke (el DOI sí), la expresión de
γ de Afshar–Monro tal como se transcribió, σ_FCA, k_c, μ, Raman del Si, n₂ del agua, valor de SRN
de Belogolovskii, factor 2π en el τ_R de Karpov. Tampoco se extrajeron las tablas de Lafforgue 2022
y Brès 2023.

## 6. Archivos creados o modificados en esta sesión (sin commit)

| Archivo | Qué es |
|---|---|
| `proyecto-final/lectura-estado-del-arte.md` | Guía de lectura por bloques (nuevo) |
| `proyecto-final/referencias-a-descargar.md` | **Lista única de 67 referencias, 22 ★** (nuevo) |
| `proyecto-final/referencias-a-descargar.pdf` | La misma lista en PDF con enlaces (nuevo) |
| `proyecto-final/reports/Propiedades no lineales SiN y Si.md` | Informe de la búsqueda profunda (nuevo) |
| `proyecto-final/research_notes/Propiedades no lineales SiN y Si/` | 4 notas de investigación (nuevo) |
| `notas/resumen-sesion-2026-11-14-proyecto-final.md` | Este resumen (nuevo) |
| `notas/bitacora-sesiones.md` | Entrada del 2026-11-14 |
| `notas/retomar-en-otro-dispositivo.md` | §2 apunta a este resumen |

## 7. Próximos pasos

1. **Juanes:** descargar las 22 referencias ★ (o pedir que se bajen automáticamente las gratuitas
   a `bibliografia/articulos/`) y registrarlas en `bibliografia/README.md`.
2. **Protocolo de cálculo de supercontinuo en SiN** (lo que Juanes anunció como siguiente):
   FDE (n_eff, A_eff, Γ por región; TE₀/TM₀; 0.6–2.6 µm; cladding SiO₂ y agua 1.33–1.37) →
   β(ω) completo → γ escalar y vectorial → GNLSE (RK4IP, choque, Raman opcional, pérdida del FDE,
   coherencia |g₁₂|) → diagnóstico L_D, L_NL, N. Para Si: γ complejo, TPA/3PA y ecuación de
   portadores. La tabla de valores centrales y barridos está en el informe, sección "El protocolo".
3. Correr `seccion_v1` (paso00 → paso06) cuando el Lumerical local esté libre de la tesis
   (`scripts/ram_lumerical.py`, skill `recursos-simulaciones`).
4. Cotejar en los PDF los valores [NV] antes de usarlos; extraer las tablas de Lafforgue 2022 y
   Brès 2023.
5. Confirmar el service pack de la v261 del cluster (Kerr en `NL_RING`).
6. Commit de lo de esta sesión cuando Juanes lo pida (los PDF de terceros siguen fuera de git).
