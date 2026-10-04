# ESTADO — `seccion_v1` · sección transversal de SiN para χ⁽³⁾ en un anillo add-drop refractómetro

## 0. LÉEME PRIMERO

**Creado el 2026-10-04.** El código está escrito y verificado sin Lumerical. **Las
simulaciones FDE NO se han corrido**: el Lumerical local estaba ocupado por la tesis.
Plan físico y criterios: `proyecto-final/plan-simulaciones-seccion.md`.

**Modo de sensado: VOLUMEN (bulk).** El anillo sensor es un **refractómetro**, sin foco en
sustancias específicas. El cladding superior es el analito líquido completo, n = 1.33 → 1.37,
**sin capa funcionalizada**. ⚠ La detección **superficial** (funcionalización) se
abordará **más adelante** en el proyecto; este estudio no la modela.

Antes de lanzar cualquier paso con Lumerical: skill `recursos-simulaciones`. ONL **solo**
corre si el Lumerical local está libre de la tesis (fotonica-integrada) y la RAM alcanza.
Para esperar sin tocar nada:

    scripts/esperar_lumerical_libre.sh --fde      # sale con 0 cuando se puede lanzar

## 1. Pasos

| paso | qué | herramienta | estado |
|---|---|---|---|
| `paso00_validacion` | reproduce la guía 800×400 de la tesis (n_eff 1.59673, n_g 1.97978; tolerancias 0.1 % y 0.3 %) + diferencia con la malla de producción | FDE | **pendiente (Lumerical)** |
| `paso01_materiales` | Sellmeier SiN (Luke 2015) y SiO₂ (Malitson 1965) anclados a 1.99 / 1.4469; agua de Segelstein anclada a 1.33 | Python | ✔ 04/10: D_mat SiO₂ 21.9 ps/(nm·km) ✓, agua 47.05 dB/cm ✓, residuo del ajuste 9.6e-4 ✓; D_mat(1550): SiN −6.6, agua +189 |
| `paso02_dispersion_h400` | H = 400 nm: 8 anchos × 25 λ (1.0–2.2 µm) × {SiO₂, analito} × {TE0, TM0}; sensado n = 1.33/1.35/1.37 | FDE (~424 solves, 1–2 h) | **pendiente** |
| `paso03_espesor_referencia` | H = 400–900 nm × 3 anchos, SiO₂: frontera normal/anómala (solo referencia) | FDE (~234 solves) | **pendiente** |
| `paso04_curvatura` | anchos finalistas × R 20–120 µm × 7 λ: α_bend (PML), n_g, β₂ del modo curvado, FSR, D1, D2 | FDE curvado | **pendiente** (necesita paso02) |
| `paso05_cifras_no_lineales` | Q_int, P_th del anillo (all-pass y add-drop), S_bulk, S/FWHM, L_D, L_NL, N; elige el candidato para la GNLSE | Python | pendiente (necesita paso02) |
| `paso06_gnlse` | primer espectro de SC (RK4IP, Taylor hasta β₄, self-steepening, sin Raman) | Python | pendiente (necesita paso05) |

## 2. Cómo correr (cuando el Lumerical esté libre)

Desde `proyecto-final/simulaciones/seccion_v1/`, con el Python de Linux (`main.py` lanza
cada paso con el Python de Windows, que es el que ve lumapi):

    python3 main.py --solo paso00_validacion                  # 1) DEBE dar VALIDACION OK
    python3 main.py --perfil rapido --desde paso02_dispersion_h400   # 2) humo end-to-end, minutos
    python3 main.py --desde paso02_dispersion_h400            # 3) producción (horas: en background)

- Barridos interrumpidos: relanzar el MISMO comando con `--reanudar`. Conserva lo ya
  calculado (`flags/computed`); sin esa opción, la carpeta de la firma se borra.
- Correr en background y vigilar con `vigilancia-procesos-largos`: marcadores = stdout
  (una línea por solve) y `flags/computed` del HDF5.
- La sesión MODE abre una vez por paso y se cierra en `finally`.

## 3. Verificaciones hechas sin Lumerical (2026-10-04)

- `pruebas_sin_lumerical.py` (Python de Windows): 6/6 OK. β₂ de un n_eff sintético
  (error 0.09 %), signo de D, solitón N = 1 tras 5 L_D (error 1e-11), fase de SPM γP₀L
  exacta, ensanchamiento lineal de un gaussiano √10 exacto, energía conservada a 5e-4.
- Cadena completa paso02 → 04 → 05 → 06 con un `app` de Lumerical SIMULADO (perfil
  rápido, en el scratchpad): corre de punta a punta, escribe HDF5, contratos y figuras.
  Las cifras del simulacro no son física.
- No verificado (solo se sabrá con Lumerical): nombres de propiedades del FDE curvado
  con PML (`y min bc` … = "PML"; si fallan, lanzan error) y la selección TE0/TM0 en
  guías anchas multimodo.

## 4. Supuestos abiertos

1. n₂ del agua (2.7e-20 m²/W) sin verificar; su peso en γ es pequeño.
2. Pérdida extra: SiO₂ 1.0 dB/cm; analito 7.0 dB/cm (curva + acopladores de la tesis,
   job 3247). El agua se calcula aparte con Γ_abs.
3. P_th usa n_g en lugar de "n" (orden de magnitud).
4. Coeficientes del Sellmeier de Luke tomados de refractiveindex.info: confirmarlos con el
   artículo (DOI verificado).
5. La dispersión del analito es la del agua desplazada a n = 1.33 (la del analito real puede
   diferir).
