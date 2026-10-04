"""
almacen.py — checkpointing HDF5 y el CONTRATO entre pasos.

Aqui vive la decision de diseno central del protocolo v2: los pasos NO se pasan
resultados en memoria. Cada paso escribe:

    resultados/<paso>/<nombre>.h5      datos crudos del barrido (reanudable)
    resultados/<paso>/salida.json      el CONTRATO: escalares y vectores cortos

y los pasos posteriores leen el contrato desde disco. Consecuencias buscadas:

  * Cambiar un parametro del paso 4 no invalida nada del paso 1: sus HDF5 y su
    contrato siguen en disco y se reutilizan tal cual.
  * Cualquier paso se puede correr suelto, en cualquier orden, siempre que sus
    contratos de entrada existan. Si falta uno, el error dice exactamente que
    paso hay que correr antes.
  * Un barrido de horas interrumpido reanuda por `flags/computed`.
"""
from __future__ import annotations

import hashlib
import json
import os

# Antes de cargar h5py: sobre la UNC de WSL el bloqueo de archivos de HDF5
# falla. Ver la nota de comun/__init__.py.
os.environ.setdefault("HDF5_USE_FILE_LOCKING", "FALSE")

from datetime import datetime, timezone  # noqa: E402
from pathlib import Path  # noqa: E402

import h5py  # noqa: E402
import numpy as np  # noqa: E402

from . import entorno  # noqa: E402  (define el escenario activo)

RAIZ = Path(__file__).resolve().parent.parent

# Contratos y figuras: por escenario. La linea base ('' ) sigue en
# resultados/ y figuras/ exactamente como antes, asi que un estudio ya corrido
# no cambia de sitio al introducir los escenarios.
DIR_RESULTADOS = RAIZ / f"resultados{entorno.sufijo_escenario()}"
DIR_FIGURAS = RAIZ / f"figuras{entorno.sufijo_escenario()}"

# Barridos HDF5 pesados: SIEMPRE en la linea base, compartidos entre
# escenarios. Son fisica de la seccion transversal (Delta_n(gap), n_eff(ancho),
# n_g(radio)) y no dependen del presupuesto de perdida. Ver entorno.ESCENARIO.
DIR_CACHE = RAIZ / "resultados"


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  Carpetas indexadas por FIRMA de los parametros de entrada                ║
# ╚══════════════════════════════════════════════════════════════════════════╝
# Regla, fijada el 2026-09-02: el NOMBRE de la carpeta de un paso es la huella
# de sus parametros fisicos de entrada (`firma_config`, 16 hex).
#
#   misma firma  -> MISMA carpeta. Se borra entera y se vuelve a generar. Nunca
#                   se acumulan dos copias de un resultado identico.
#   otra firma   -> carpeta NUEVA, al lado de las que ya existen, de modo que
#                   dos juegos de parametros distintos conviven y se distinguen
#                   por el nombre sin tener que abrir nada.
#
#   resultados/<paso>/_actual.json     indice: cual es la firma vigente y con
#                                      que CONFIG se genero cada una
#   resultados/<paso>/<firma>/         salida.json + los .h5 del barrido
#   figuras/<paso>/                    las figuras de la ULTIMA corrida, planas
#                                      (sin firma: Juanes las quiere a la vista,
#                                      2026-09-14; se vacia y regenera en cada
#                                      corrida del paso)
#
# El borrado es DELIBERADO y lo pidio Juanes: prima que el arbol sea legible
# sobre conservar un barrido a medias. Un barrido interrumpido se pierde entero
# y hay que repetirlo. Si algun dia eso duele, el punto donde cambiarlo es
# `preparar_paso`: bastaria no borrar y dejar que `flags/computed` reanude.
NOMBRE_INDICE = "_actual.json"

# Paso en curso en ESTE proceso. Cada paso corre en su propio subproceso
# (main.py), asi que no hay riesgo de que dos pasos se pisen esta variable.
_ACTUAL = {"paso": None, "firma": None}


def _escribir_indice(dir_del_paso: Path, firma: str, cfg: dict) -> None:
    """Anota que firma es la vigente y con que CONFIG se genero cada una."""
    ruta = dir_del_paso / NOMBRE_INDICE
    idx = {}
    if ruta.exists():
        try:
            idx = json.loads(ruta.read_text())
        except Exception:
            idx = {}
    idx["actual"] = firma
    idx.setdefault("firmas", {})[firma] = {
        "generado": _ahora(),
        "config": _jsonificar({k: v for k, v in (cfg or {}).items()
                               if k not in CLAVES_NO_FISICAS}),
    }
    # Poda: una firma cuya carpeta ya no existe (borrada a mano) no debe seguir
    # anunciandose en el indice, o `_firma_vigente` apuntaria al vacio.
    idx["firmas"] = {k: v for k, v in idx["firmas"].items()
                     if k == firma or (dir_del_paso / k).exists()}
    ruta.write_text(json.dumps(idx, indent=2, ensure_ascii=False))


def _con_entradas_de_ambiente(cfg: dict) -> dict:
    """CONFIG mas las entradas que NO viven en el pero cambian los numeros.

    El MOTOR ('analitico' / 'interconnect') es una entrada fisica de pleno
    derecho: son dos modelos distintos y sus resultados no son intercambiables.
    Llega por `--motor`, no por CONFIG, asi que hay que meterlo en la firma a
    mano. Sin esto los dos motores caian en la MISMA carpeta y correr el modelo
    analitico borraba el barrido de INTERCONNECT de 28 min. Encontrado y
    corregido el 2026-09-02 al validar el mecanismo de firmas.
    """
    extra = dict(cfg)
    pedir = getattr(entorno, "motor_pedido", None)
    if pedir is not None and "MOTOR" not in extra:
        extra["MOTOR"] = pedir()
    return extra


def preparar_paso(paso: str, cfg: dict) -> str:
    """Abre la carpeta de trabajo del paso. LLAMAR AL PRINCIPIO DE CADA PASO.

    Devuelve la firma. Si ya existia una carpeta con esa misma firma la BORRA
    antes de recrearla: correr dos veces con los mismos parametros deja un
    resultado, no dos.
    """
    import shutil

    firma = firma_config(_con_entradas_de_ambiente(cfg))
    _ACTUAL["paso"], _ACTUAL["firma"] = paso, firma
    for raiz in {DIR_RESULTADOS, DIR_CACHE}:
        base = raiz / paso
        destino = base / firma
        if destino.exists():
            shutil.rmtree(destino)
        destino.mkdir(parents=True, exist_ok=True)
        _escribir_indice(base, firma, cfg)
    # Las figuras van planas en figuras/<paso>/: se vacia la carpeta para que
    # no queden figuras de una corrida anterior con otro nombre.
    d_fig = DIR_FIGURAS / paso
    if d_fig.exists():
        shutil.rmtree(d_fig)
    d_fig.mkdir(parents=True, exist_ok=True)
    return firma


def _firma_vigente(paso: str, raiz: Path):
    """Firma con la que leer un paso. El paso en curso usa la suya; para
    cualquier otro se lee su indice, que apunta a su ultima corrida."""
    if paso == _ACTUAL["paso"] and _ACTUAL["firma"]:
        return _ACTUAL["firma"]
    for candidata in (raiz, DIR_RESULTADOS, DIR_CACHE):
        ruta = candidata / paso / NOMBRE_INDICE
        if ruta.exists():
            try:
                f = json.loads(ruta.read_text()).get("actual")
                if f and (raiz / paso / f).exists():
                    return f
            except Exception:
                pass
    return None


def _resolver(paso: str, raiz: Path) -> Path:
    """Carpeta de un paso dentro de `raiz`, con firma si la hay.

    Si no hay indice se devuelve la carpeta plana: asi se siguen leyendo los
    resultados anteriores al 2026-09-02, que no estaban indexados.
    """
    firma = _firma_vigente(paso, raiz)
    d = (raiz / paso / firma) if firma else (raiz / paso)
    d.mkdir(parents=True, exist_ok=True)
    return d


def dir_paso(paso: str) -> Path:
    return _resolver(paso, DIR_RESULTADOS)


def dir_cache(paso: str) -> Path:
    """Donde van los HDF5 de barrido: compartidos entre escenarios."""
    return _resolver(paso, DIR_CACHE)


def dir_figuras_paso(paso: str) -> Path:
    """Figuras planas por paso, sin subcarpeta de firma (ver cabecera)."""
    d = DIR_FIGURAS / paso
    d.mkdir(parents=True, exist_ok=True)
    return d


def _ahora() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  CONTRATO entre pasos                                                    ║
# ╚══════════════════════════════════════════════════════════════════════════╝
def _jsonificar(v):
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.floating,)):
        f = float(v)
        return None if not np.isfinite(f) else f
    if isinstance(v, (np.bool_,)):
        return bool(v)
    if isinstance(v, np.ndarray):
        return [_jsonificar(x) for x in v.tolist()]
    if isinstance(v, (list, tuple)):
        return [_jsonificar(x) for x in v]
    if isinstance(v, dict):
        return {str(k): _jsonificar(x) for k, x in v.items()}
    if isinstance(v, float):
        return None if not np.isfinite(v) else v
    if isinstance(v, Path):
        return str(v)
    return v


def escribir_contrato(paso: str, datos: dict, cfg: dict | None = None) -> Path:
    """Publica los productos de un paso. Sobrescribe el contrato anterior."""
    destino = dir_paso(paso) / "salida.json"
    carga = {
        "_meta": {
            "paso": paso,
            "generado": _ahora(),
            "perfil": (cfg or {}).get("PERFIL", os.environ.get(
                "PLATAFORMA_PERFIL", "completo")),
        },
        "config": _jsonificar(cfg or {}),
        "resultados": _jsonificar(datos),
    }
    destino.write_text(json.dumps(carga, indent=2, ensure_ascii=False))
    return destino


def ruta_contrato(paso: str) -> Path | None:
    """Contrato del paso, con HERENCIA desde la linea base.

    Un escenario solo re-corre los pasos que la perdida cambia (del acoplo
    critico en adelante). Todo lo anterior —anchos, radios, sensibilidad— es
    geometria y no depende del presupuesto de perdida, asi que se HEREDA del
    contrato de la linea base en vez de obligar a recorrer horas de FDTD 3D
    por escenario. Devuelve None si no esta en ninguno de los dos sitios.
    """
    for raiz in (DIR_RESULTADOS, DIR_CACHE):
        firma = _firma_vigente(paso, raiz)
        if firma:
            c = raiz / paso / firma / "salida.json"
            if c.exists():
                return c
        plano = raiz / paso / "salida.json"     # corridas sin indexar
        if plano.exists():
            return plano
    return None


def leer_contrato(paso: str, requerido: bool = True) -> dict | None:
    """Devuelve el bloque `resultados` del contrato de `paso`.

    Con requerido=True lanza un error que nombra el comando exacto que falta
    por correr, en vez de reventar mas adelante con un None inexplicable.
    """
    ruta = ruta_contrato(paso)
    if ruta is None:
        if not requerido:
            return None
        raise FileNotFoundError(
            f"Falta el contrato del paso {paso!r} "
            f"(ni en {DIR_RESULTADOS} ni en la linea base {DIR_CACHE}).\n"
            f"Corre primero:  python main.py --solo {paso}"
        )
    return json.loads(ruta.read_text())["resultados"]


def meta_contrato(paso: str) -> dict | None:
    ruta = ruta_contrato(paso)
    if ruta is None:
        return None
    d = json.loads(ruta.read_text())
    return {**d.get("_meta", {}), "config": d.get("config", {})}


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  Checkpointing HDF5 reanudable                                           ║
# ╚══════════════════════════════════════════════════════════════════════════╝
def _estructura_valida(ruta: Path, n_puntos: int) -> bool:
    """True si el HDF5 esta completo y su barrido tiene el tamano esperado."""
    try:
        with h5py.File(ruta, "r") as f:
            return ("flags/computed" in f and "metadata" in f and "results" in f
                    and f["flags/computed"].shape[0] == n_puntos)
    except Exception:
        return False


# Claves que NO cambian ningun numero: si solo cambia una de estas, la cache
# sigue siendo valida. Todo lo demas entra en la firma.
CLAVES_NO_FISICAS = frozenset({
    "OCULTAR_GUI", "GUARDAR_FSP_DIR", "PASO", "MALLA_ORIGEN",
    # Contabilidad que escribe el propio almacen, no parametros de entrada.
    # Excluirlas hace que la firma calculada sobre metadata/ de un archivo ya
    # existente coincida con la calculada sobre el CONFIG del paso, que es lo
    # que permite sellar archivos antiguos sin recalcularlos.
    "timestamp_start", "timestamp_end", "runs_completed", "firma",
})


def firma_config(cfg: dict) -> str:
    """Huella de los parametros con los que se calculo un barrido.

    Existe porque `_estructura_valida` NO basta. Un barrido de un solo punto
    (la medida de guia recta del protocolo de radios) tiene n_puntos = 1 con
    CUALQUIER geometria: al cambiar el ancho de 950 a 850 nm el archivo seguia
    pareciendo valido y se reutilizaba el n_g de la guia vieja, centrando la
    ventana de radios sobre una geometria que ya no existia. Sin ningun error:
    numeros creibles y equivocados. Es el fallo contra el que avisa el
    CLAUDE.md §8 (la clave debe incluir los parametros).

    La firma se calcula sobre el CONFIG completo menos CLAVES_NO_FISICAS, se
    guarda en metadata/firma y se compara al reabrir.
    """
    partes = []
    for k in sorted(cfg):
        if k in CLAVES_NO_FISICAS:
            continue
        v = cfg[k]
        if isinstance(v, (np.ndarray, list, tuple)):
            v = np.asarray(v).tolist()
        if isinstance(v, float):
            # Redondeo defensivo: dos corridas que fijan el mismo parametro no
            # pueden diferir por el ultimo bit del float y rehacer horas de FDTD.
            v = f"{v:.12g}"
        partes.append(f"{k}={v}")
    crudo = "|".join(partes)
    return hashlib.sha256(crudo.encode("utf-8")).hexdigest()[:16]


def _firma_guardada(ruta: Path):
    try:
        with h5py.File(ruta, "r") as f:
            v = f["metadata"].attrs.get("firma")
            return v.decode() if isinstance(v, bytes) else (
                str(v) if v is not None else None)
    except Exception:
        return None


def init_h5(ruta: Path, cfg: dict, ejes: dict, campos, n_puntos: int) -> Path:
    """Crea el HDF5 ANTES del barrido con todo preasignado.

    metadata/  atributos del CONFIG + los ejes del barrido + `firma`
    results/   un dataset por campo, lleno de NaN, maxshape abierto
    flags/computed  booleano por punto

    Un job interrumpido deja siempre un archivo valido y reintentable. Una
    cache calculada con OTROS parametros se descarta: ver `firma_config`.
    """
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    firma = firma_config(cfg)
    firma_previa = _firma_guardada(ruta) if ruta.exists() else None
    coincide = (firma_previa == firma)
    if ruta.exists() and not coincide:
        print(f"[almacen] {ruta.name}: la cache se calculo con otros parametros "
              f"(firma {firma_previa} != {firma}). Se rehace.", flush=True)
    if ruta.exists() and coincide and _estructura_valida(ruta, n_puntos):
        with h5py.File(ruta, "a") as f:
            for c in campos:
                if f"results/{c}" not in f:
                    f.create_dataset(f"results/{c}",
                                     data=np.full(n_puntos, np.nan),
                                     maxshape=(None,))
            f.flush()
        return ruta
    if ruta.exists():
        # Archivo truncado o de una geometria de barrido distinta: rehacerlo es
        # correcto, reutilizarlo daria indices desalineados en silencio.
        log_reemplazo = ruta.with_suffix(ruta.suffix + ".invalido")
        ruta.replace(log_reemplazo)

    with h5py.File(ruta, "w") as f:
        md = f.create_group("metadata")
        for k, v in cfg.items():
            try:
                md.attrs[k] = v if not isinstance(v, (list, tuple)) else np.asarray(v)
            except (TypeError, ValueError):
                md.attrs[k] = str(v)
        md.attrs["timestamp_start"] = _ahora()
        md.attrs["firma"] = firma
        for nombre, arr in ejes.items():
            md.create_dataset(nombre, data=np.asarray(arr))
        rg = f.create_group("results")
        for c in campos:
            rg.create_dataset(c, data=np.full(n_puntos, np.nan), maxshape=(None,))
        f.create_group("flags").create_dataset(
            "computed", data=np.zeros(n_puntos, dtype=bool), maxshape=(None,))
        f.flush()
    return ruta


def ya_calculado(ruta: Path, i: int) -> bool:
    if not Path(ruta).exists():
        return False
    with h5py.File(ruta, "r") as f:
        return bool(f["flags/computed"][i])


def escribir_punto(ruta: Path, i: int, valores: dict) -> None:
    """Escribe un punto y marca computed=True, con flush inmediato."""
    with h5py.File(ruta, "a") as f:
        for k, v in valores.items():
            if f"results/{k}" not in f:
                f.create_dataset(f"results/{k}",
                                 data=np.full(f["flags/computed"].shape[0], np.nan),
                                 maxshape=(None,))
            f[f"results/{k}"][i] = float(v) if v is not None else np.nan
        f["flags/computed"][i] = True
        f.flush()


def leer_resultados(ruta: Path) -> dict:
    """Devuelve {campo: array} + 'computed' del HDF5 de un barrido."""
    with h5py.File(ruta, "r") as f:
        out = {k: f[f"results/{k}"][:] for k in f["results"].keys()}
        out["computed"] = f["flags/computed"][:]
        for k in f["metadata"].keys():
            out[f"eje_{k}"] = f[f"metadata/{k}"][:]
    return out


def cerrar_h5(ruta: Path, n_computed: int) -> None:
    with h5py.File(ruta, "a") as f:
        f["metadata"].attrs["timestamp_end"] = _ahora()
        f["metadata"].attrs["runs_completed"] = int(n_computed)
        f.flush()
