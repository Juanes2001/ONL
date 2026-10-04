# Anatomía de un script de simulación

Para scripts destinados al cluster manda `.claude/rules/fdtd-cluster.md`; esto lo
complementa con lo que se aprendió construyendo las rutinas de RING_2.

## Esqueleto

```
docstring          qué simula, qué produce, cómo se corre, supuestos declarados
CONFIG             todos los parámetros juntos, en SI, comentados con unidad y razón
resolve_lumapi()   ruta desde CONFIG, assert con mensaje explícito
build_ring_and_buses()      geometría pura
build_mesh_overrides()      malla fina donde importa
build_simulation_region()   dominio, fronteras, tiempo, autoshutoff
build_source_and_monitors() fuente + pares dft_/exp_ por puerto
init_h5() / write_h5_results()   checkpoint antes y después de run()
main()             try/finally que SIEMPRE cierra la sesión
```

Cada función recibe `cfg` y `geom` y devuelve lo que la siguiente necesita. Nada de
estado global implícito entre pasos.

## CONFIG: las perillas que de verdad importan

```python
CONFIG = {
    "LUMAPI_PATH": "/opt/lumerical/v202/api/python",   # ruta del cluster (Linux)

    # ── Identidad de la estructura ────────────────────────────────────────
    "LAMBDA_RES_NM": 1550.0, "RING_RADIUS_UM": ..., "WG_WIDTH_UM": 1.000,
    "WG_HEIGHT_UM": 0.400, "N_SIN": 1.99, "N_SIO2": 1.4469,
    "GAP_IN_NM": ..., "GAP_OUT_NM": ..., "Q_FACTOR": 3100,

    # ── Ventana espectral ─────────────────────────────────────────────────
    "LAMBDA_START_NM": 1548.0, "LAMBDA_STOP_NM": 1568.0, "N_FREQ_POINTS": 1000,

    # ── Malla ─────────────────────────────────────────────────────────────
    "MESH_LAMBDA_REF_NM": 1550.0, "MESH_CELLS_PER_WVL": 10,
    "HALO_G0_MULTIPLE": 4, "MESH_ACCURACY_BULK": 2,

    # ── Dominio y duración ────────────────────────────────────────────────
    "PML_LAYERS": 12, "ACCESS_BUFFER_UM": 2.0,
    "AUTOSHUTOFF_MIN": 1e-5, "SIM_TIME_TAU_MULTIPLE": 15,

    # ── Inspección visual (solo local; en el cluster False / 0) ───────────
    "SHOW_GUI": False, "PAUSE_BEFORE_RUN_S": 0,

    "OUT_DIR": os.path.join(os.path.dirname(__file__), "resultados"),
}
```

**Ninguna perilla muerta.** Si un valor está en CONFIG debe aplicarse en algún sitio; si
no, se borra. Un bloque pensado para editarse a ciegas en el cluster no puede tener
mandos que no hacen nada. (`AUTOSHUTOFF_MIN` estuvo así, sin aplicarse, en cuatro
scripts a la vez.)

## Reglas numéricas

**Malla.** Paso = `λ_ref / (celdas_por_λ · n_local)`, evaluado con el índice del material
de cada zona: el núcleo pide paso más fino que el cladding. El halo de malla fina se
extiende `4·g₀` más allá de la guía, con `g₀ = 1/γ` y `γ = k₀·√(n_eff² − n_clad²)` la
longitud de decaimiento evanescente — más allá de eso el campo ya no está.

⚠ **Comprueba cuántas celdas caen dentro del gap de acoplamiento.** Con paso 77.9 nm y
gap 269.6 nm son ~3.5 celdas: suficiente para resultados creíbles, justo para el Q. Si el
Q sale sistemáticamente bajo, este es el primer sospechoso.

**Tiempo de simulación.** `sim_time = N · τ` con `τ = Q·λ/(2πc)` el tiempo de vida del
fotón; `N = 15` es un techo cómodo. El autoshutoff corta antes cuando la energía cae.

```python
SPEED_OF_LIGHT = 299_792_458.0        # exacto; 3e8 mete 0.07 % de sesgo
tau_s = q_factor * lambda_res_m / (2 * np.pi * SPEED_OF_LIGHT)
```

**Autoshutoff.** `1e-5`, no el default. Un anillo de alto Q sigue "sonando" mucho después
de que la fuente se apaga; cortar antes trunca el espectro y subestima el Q.

**Ventana espectral.** Al menos **2 FSR**, para poder medir el FSR — que es lo que valida
`n_g`. Con una sola resonancia en la ventana, el FSR no es medible. Resolución objetivo:
≥ 20 puntos por FWHM (20 pm por punto para un FWHM de 500 pm da ~25).

## Checkpointing

```python
def init_h5(path, cfg, n_freq, method):
    """Crea el HDF5 ANTES de run(): si el job muere queda un archivo válido,
    con metadata completa y computed=False, que la siguiente corrida reintenta."""
    with h5py.File(path, "w") as h5:
        nan = np.full(int(n_freq), np.nan, dtype=float)
        for name in ("results/lambda_m", "results/T_through", "results/T_drop"):
            h5.create_dataset(name, data=nan.copy(), maxshape=(None,))
        h5.create_dataset("flags/computed", data=False)
        meta = h5.create_group("metadata")
        meta.attrs["date_started"] = datetime.datetime.now().isoformat()
        meta.attrs["method"] = method
        for k, v in cfg.items():
            meta.attrs[k] = v if isinstance(v, (int, float, str)) else str(v)
        h5.flush()
```

`maxshape=(None,)` permite redimensionar si el solver devuelve otro número de puntos del
esperado. Al escribir, `resize()` antes de asignar y `flush()` después.

El nombre del archivo debe ser **determinista e incluir los parámetros del run**, para que
dos barridos distintos no colisionen: `fdtd3d_ring2_ideal_R19.1846um_gapIn270nm_..._h5`.

## Autocontención

Los scripts del cluster no importan nada del repositorio: si necesitan una función de
`src/`, se copia dentro bajo un comentario `# --- vendored desde src/physics.py ---`.
Los scripts que solo corren en local (figuras, análisis) sí pueden importar de `src/`.
