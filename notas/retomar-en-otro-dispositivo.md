# Retomar el trabajo en otro dispositivo

Estado al 2026-11-05. Este archivo basta para contextualizarse sin la conversación original ni la
memoria local de Claude Code, que **no viaja con el repo**. Lo esencial de esa memoria está aquí.

## 1. Traer el trabajo

```bash
git clone https://github.com/Juanes2001/ONL.git   # o git fetch origin, si ya existe
cd ONL
git switch taller-02-y-apuntes                    # si ya se fusionó en main: git switch main
```

Orden de lectura: `CLAUDE.md` → este archivo → `notas/contexto-proyecto.md` →
primera entrada de `notas/bitacora-sesiones.md`.

Para arrancar una sesión de Claude Code:

> Lee `notas/retomar-en-otro-dispositivo.md` y continúa con los pendientes del taller 2.

## 2. Dónde estamos

- **Foco actual:** Tarea 2 (`talleres/taller-02-dispersion-polarizacion/`), lista salvo lo de §3.
- **Proyecto final:** en pausa desde el 2026-11-04 para dedicarse al taller 2 (ver §6).
- **Saleh & Teich, 2.ª ed.:** leído completo; apuntes en `notas/saleh/` (ver §5).

## 3. Tarea 2: estado y pendientes

Documento: `Tarea_2_ONL.tex` → `Tarea_2_ONL.pdf` (20 pp., 8 puntos). Compila sin referencias rotas
ni desbordes.

**Verificado:** Sellmeier con derivadas analíticas, FFT propia frente a la solución analítica
(error ~1e-15), Jones, Brewster, walk-off, cadena de polarizadores y sympy con residuo cero en los
puntos 1, 2, 4 y 7. Hubo dos rondas de revisión más una lectura independiente: se corrigieron
errores de interpretación y de unidades, y ningún resultado numérico en recuadro cambió.

**Pendientes, por orden:**

1. **Ejecutar `punto4_pulso_dispersion.m`.** Nunca se ha ejecutado: MATLAB R2026b falló con el error
   de licencia 5201. Figuras y Tabla 3 salen de la réplica `punto4_pulso_dispersion_py.py`. Hay que
   iniciar sesión en MathWorks, correrlo, comparar con la Tabla 3 y quitar del punto 4 y del apéndice
   la nota de que no se pudo ejecutar. Puede fallar aunque la lógica sea la misma.
2. **Decidir el dibujo del punto 2.** El enunciado pide "a mano alzada" y el documento trae una
   figura por computador.
3. **Leer los puntos 5, 7 y 8.** La segunda revisión halló allí errores que la primera no vio; las
   frases de interpretación son lo menos blindado.
4. **Revisar la maquetación.** La p. 16 no se inspeccionó en la versión final y la p. 4 queda medio
   vacía por una figura flotante.

**Sin verificar del todo:** Fig. 6.3-12(a) y ecuaciones de §6.5 (cotejadas solo con los apuntes),
numeración de la 1.ª edición del "problema 5.6-3" (suposición) e índices de la calcita (externos al
libro). El documento aclara estos dos últimos.

Convenciones del taller (Saleh): $e^{j\omega t}$; $D_\nu=2\pi\beta''$ en s²/m;
$z_0=\pi\tau_0^2/|D_\nu|$; $\tau_0$ es la semianchura a $1/e$ de la amplitud.

## 4. Lo que NO está en git

Hay que copiarlo a mano (repo público; material con derechos o de terceros):

- `bibliografia/*.pdf|djvu|epub`, entre ellos el Saleh escaneado.
- `notas/*.pdf`: programa, `class1`, `class2`, `nlo_presentation`, notas de Hagan, Kik & Van Stryland.
- `talleres/Tarea2-OpticaNoLineal (1).pdf`: enunciado de la Tarea 2.
- `.claude/rules/fdtd-cluster.md`: trae IP, cuenta y licencia del cluster.
- `tectonic` y `t.tar.gz`: el binario para compilar LaTeX.

No volver a subir nada de esto sin que Juanes lo decida (`notas/contexto-proyecto.md` §6.2).

## 5. Entorno

Compilar la tarea, con Tectonic en la carpeta del taller (enlace de descarga en
`notas/contexto-proyecto.md` §2):

```bash
cd talleres/taller-02-dispersion-polarizacion && ./tectonic Tarea_2_ONL.tex
```

Con babel en español, `\%` en modo matemático y `\max` dentro de un pie de figura rompen la
compilación.

Las rutas de esta máquina (WSL `kali-linux`) cambian en otro dispositivo; hay que ajustarlas:

- Python con numpy, scipy, sympy, matplotlib y PyMuPDF:
  `/mnt/c/Users/jero0/AppData/Local/Programs/Python/Python311/python.exe`.
- MATLAB: `/mnt/c/Program Files/MATLAB/R2026b/bin/matlab.exe`. La orden de uso está en el encabezado
  del `.m`, con la ruta UNC de esta máquina.

Figuras: `punto4_pulso_dispersion_py.py` y `figuras_puntos_2_7_8.py` escriben en `figuras/`.

Saleh: el PDF no tiene capa de texto y página PDF = página del libro + 22. Consultar primero
`notas/saleh/` (índice, erratas y convenciones Saleh ↔ Boyd en su `README.md`; buscar con grep por
número de ecuación) y renderizar la página solo para confirmar un detalle. En los apuntes,
"cálculo propio" y "[sic]" marcan lo que no es del libro.

## 6. Proyecto final (en pausa)

Tema: supercontinuo en anillos de SiN sobre la plataforma de la tesis (`fotonica-integrada`, repo
aparte, **solo lectura**). Resumen en `proyecto-final/contexto-fotonica-integrada.md`.

- Informes en `proyecto-final/reports/`; notas en `proyecto-final/research_notes/`. Referencias
  verificadas el 2026-10-30 con `scripts/verificar_referencias.py`: todas bien salvo la tesis de
  Segelstein (sin DOI) y 4 preprints de arXiv. Scopus y WoS los coteja Juanes desde la UNAL.
- Conclusiones: el Si₃N₄ de 400 nm a 1550 nm es de dispersión normal, así que la ruta son pulsos
  oscuros o bombeo pulsado. El anillo en agua (Q~10⁴) tiene P_th ≈ 130 W y no sirve de generador.
  Generador en SiO₂ y sensor en agua probablemente van separados.
- `proyecto-final/simulaciones/seccion_v1/` (FDE → GNLSE) está escrito y sin correr, a la espera de
  Lumerical libre. Al retomar, leer su `ESTADO.md` §0 y las entradas 2026-10-29/30 de la bitácora.

## 7. Reglas que no se rompen

- No hacer commit ni push sin orden de Juanes.
- La tesis tiene prioridad en Lumerical y en el cluster: si están ocupados, no se lanza nada.
- No matar procesos sin preguntar.
- Sensado de volumen, sin funcionalización.
- Al cerrar cada sesión, registrar lo hecho en `notas/bitacora-sesiones.md`.
