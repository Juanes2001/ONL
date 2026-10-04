# Verificar antes de gastar horas

Cuatro escalones, de segundos a horas. Cada uno atrapa una clase distinta de fallo.

## 1. Smoke test diminuto (segundos)

Antes de tocar la estructura real, comprueba que **el motor arranca y devuelve datos**:
guía recta con el stack real, dominio de pocas µm, malla burda, `simulation time` corto.

Qué debe dar: `T ≈ 1.0` y `run()` terminando en segundos. Si `run()` se cuelga sin lanzar
ningún proceso `fdtd-engine`, el problema es del entorno, no del script.

Aprovecha para verificar en el mismo test cualquier propiedad de la que no estés seguro
(`set` sobre un nombre inválido sí lanza excepción) y, si vas a usar simetría, corre la
**misma** geometría con y sin ella y compara: deben coincidir.

## 2. Harness de construcción sin `run()` (segundos)

Importa el script real por ruta con `importlib`, llama a sus funciones `build_*`
verdaderas, comprueba lo que se pueda leer de vuelta y hace `save()`. Nunca llama a
`run()`.

```python
spec = importlib.util.spec_from_file_location(name, path)
m = importlib.util.module_from_spec(spec); sys.modules[name] = m
spec.loader.exec_module(m)
m.CONFIG["LUMAPI_PATH"] = LUM_API_LOCAL          # el CONFIG apunta al cluster
app = lumapi.FDTD(hide=True)
geom = m.build_ring_and_buses(app, m.CONFIG)
...
assert app.getnamed(REGION, "auto shutoff min") == m.CONFIG["AUTOSHUTOFF_MIN"]
app.select("dft_through"); app.select("exp_through")   # lanza si no existen
```

Esto atrapa nombres de API mal, propiedades inactivas y objetos que no se crearon. **No**
atrapa las trampas silenciosas: la ligadura de `setexpansion` no es legible por API.

## 3. Inspección visual en el CAD

Abrir la GUI y **mirar la estructura** es lo único que atrapa los errores de geometría que
no dan error: puertos en el extremo equivocado, guías que se cruzan sin querer, monitores
mal orientados, overrides de malla desplazados.

```python
app = lumapi.FDTD(hide=not cfg["SHOW_GUI"])
...
if cfg["PAUSE_BEFORE_RUN_S"] > 0:
    time.sleep(cfg["PAUSE_BEFORE_RUN_S"])   # ventana para revisar antes de arrancar
app.run()
```

Los defaults van en `False` / `0`: el cluster exige headless y sin llamadas gráficas.

## 4. Corrida real: qué mirar en cuanto termine

- **¿El tiempo es plausible?** Compáralo con celdas × timesteps. Una simulación 3D de
  millones de celdas que termina en 48 s **no simuló nada**: cortó por autoshutoff porque
  la fuente no inyectaba o el campo no se propagaba.
- **¿Aparecieron procesos del motor?** Sin `fdtd-engine` / `varfdtd-engine` en la lista de
  procesos, no hubo solver.
- **¿Hay ceros exactos?** `T = 0.0000` en toda la banda es configuración, no física.
- **¿El espectro tiene la forma esperada?** Un through plano sin dips significa que nada
  acopla al resonador.

## El entorno de esta máquina (Lumerical en Windows, repo en WSL2)

```bash
WINPY="/mnt/c/Users/JUANES_/AppData/Local/Programs/Python/Python311/python.exe"
"$WINPY" "$(wslpath -w <ruta_wsl_del_script>)"
```

Dentro del script de Python (Windows), **antes** de `import lumapi`:

```python
os.add_dll_directory(r"C:\Program Files\Lumerical\v202\bin")        # sin esto:
os.add_dll_directory(r"C:\Program Files\Lumerical\v202\api\python") # FileNotFoundError
sys.path.append(r"C:\Program Files\Lumerical\v202\api\python")      # interopapi.dll
```

Dos ajustes al correr en local un script pensado para el cluster:

- `CONFIG["LUMAPI_PATH"]` → la ruta de Windows.
- `CONFIG["OUT_DIR"]` → un directorio **nativo de Windows**, no la UNC de WSL: el motor
  escribe ahí sus temporales. Después se copia el `.h5` al `resultados/` del estudio.

Detalles adicionales:

- `h5py` sobre rutas UNC `\\wsl.localhost\...` falla al bloquear el archivo; usa
  `h5py.File(p, "r", locking=False)`.
- La consola de Windows es cp1252 y revienta al imprimir `λ` o `·`. Al principio del
  script: `sys.stdout.reconfigure(encoding="utf-8", errors="replace")`.
- Los procesos `fdtd-solutions.exe` / `mode-solutions.exe` colgados retienen licencia:
  `taskkill.exe /F /IM fdtd-solutions.exe`.
- Simulaciones largas: lánzalas en segundo plano, nunca bloqueando la sesión. Medido en
  esta máquina: varFDTD ~1–8 min, FDTD 3D ~5.5–6 h.
