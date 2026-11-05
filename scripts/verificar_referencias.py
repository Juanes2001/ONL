"""
verificar_referencias.py — coteja las referencias de un informe Markdown contra las bases de
datos bibliográficas abiertas: Crossref, OpenAlex, Semantic Scholar, PubMed y arXiv.

    python3 scripts/verificar_referencias.py INFORME.md SALIDA.md [--json SALIDA.json]

Qué hace, por referencia:
  1. Extrae DOI (o identificador arXiv), título entrecomillado, primer apellido y año del texto.
  2. DOI → Crossref (metadatos canónicos), OpenAlex, Semantic Scholar y PubMed (existencia).
  3. Compara título / primer autor / año del informe con los de Crossref y marca discrepancias.
  4. Sin DOI → busca el título en Crossref y propone el mejor candidato (con su DOI).
  5. arXiv → confirma el preprint en la API de arXiv y busca si ya hay versión publicada.

Solo usa la biblioteca estándar (el Python de Linux de esta máquina no tiene numpy).
Scopus y Web of Science requieren clave institucional y NO se consultan.
"""
from __future__ import annotations

import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

UA = {"User-Agent": "ONL-verificador-referencias/1.0 (proyecto academico UNAL; python-urllib)"}
PAUSA_S2 = 3.2  # Semantic Scholar sin clave: ~100 peticiones / 5 min


# ───────────────────────── utilidades ─────────────────────────
def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace("₃", "3").replace("₄", "4").replace("₂", "2")
    s = s.replace("æ", "ae").replace("ø", "o").replace("ß", "ss").replace("ł", "l").replace("đ", "d")
    return re.sub(r"[^a-z0-9 ]+", " ", s)


STOP = set("a an the of in on for and to with by from at via using based its de la del el en y".split())


def tokens(s: str) -> set[str]:
    return {t for t in norm(s).split() if t not in STOP and len(t) > 1}


def similitud(a: str, b: str) -> float:
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def get_json(url: str, timeout: int = 30, reintentos: int = 3):
    for i in range(reintentos):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429 and i < reintentos - 1:
                time.sleep(10 * (i + 1))
                continue
            return e.code, None
        except Exception as e:  # red, timeout, JSON
            if i < reintentos - 1:
                time.sleep(2)
                continue
            return -1, str(e)
    return -1, None


def get_text(url: str, timeout: int = 30):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return -1, str(e)


# ───────────────────────── extracción del informe ─────────────────────────
# Admite paréntesis dentro del DOI (p. ej. 10.1016/0030-4018(92)90367-Z); el cierre sobrante se recorta en limpiar_doi.
RE_DOI = re.compile(r"(?:DOI\s+|doi\.org/)(10\.\d{4,9}/(?:[^\s,;()\]]|\([^\s()]*\))+)", re.I)
RE_ARXIV = re.compile(r"arXiv:\s*(\d{4}\.\d{4,5})", re.I)
RE_TITULO = re.compile(r"[\"“]([^\"”]+)[\"”]")
RE_ANIO = re.compile(r"\((\d{4})\)")
RE_ITEM = re.compile(r"^(\d+)\.\s+(.*)$")
RE_LINK = re.compile(r"\[([^\]]+)\]\(https?://doi\.org/((?:[^()\s]|\([^()\s]*\))+)\)")


def limpiar_doi(d: str) -> str:
    return d.rstrip(".,;:—–-").strip()


def primer_apellido(texto: str, enlace: bool = False) -> str:
    t = texto.strip().lstrip("*").strip()
    t = re.split(r",| et al\.| &| y ", t, maxsplit=1)[0]
    if enlace:
        # Texto de enlace: "Opt. Express 21, 22441" o "IEEE JSTQE 2026" no empiezan por un autor.
        # Pistas: abreviatura con punto, o un número que no es un año de 4 cifras.
        if "." in t or re.search(r"\b(?!(?:19|20)\d{2}\b)\d+\b", t):
            return ""
        tok = t.split()[0] if t.split() else ""
        if len(tok) >= 2 and tok.isupper():   # "APL 2010", "PRL 93": sigla de revista
            return ""
    t = t.replace("Del'Haye", "DelHaye")
    # Solo tokens alfabéticos: en texto de enlace tipo "Ikeda 1979" o "Ref. 21" el año o el número
    # no es un apellido. Apellidos compuestos tipo "Castelló-Pedrero": norm los separa; tomar el último.
    partes = [p for p in norm(t).split() if p.isalpha()]
    return partes[-1] if partes else ""


def extraer_items(md: str):
    """Lista numerada de la sección Referencias (formato 'N. Autor, "Título", Rev. (año). DOI x')."""
    items = []
    en_ref = False
    for linea in md.splitlines():
        if linea.startswith("## ") and "Referencias" in linea:
            en_ref = True
            continue
        if not en_ref:
            continue
        m = RE_ITEM.match(linea.strip())
        if not m:
            continue
        n, texto = int(m.group(1)), m.group(2)
        doi = RE_DOI.search(texto)
        arx = RE_ARXIV.search(texto)
        tit = RE_TITULO.search(texto)
        anios = RE_ANIO.findall(texto)
        items.append({
            "n": n, "texto": texto,
            "doi": limpiar_doi(doi.group(1)) if doi else None,
            "arxiv": arx.group(1) if arx else None,
            "titulo": tit.group(1) if tit else None,
            "apellido": primer_apellido(texto),
            "anio": int(anios[-1]) if anios else None,
            "sin_verificar": "sin verificar" in texto.lower(),
        })
    return items


def extraer_links(md: str):
    """Enlaces [texto](https://doi.org/DOI) en el cuerpo, uno por DOI (informes sin lista numerada)."""
    vistos, items = {}, []
    for m in RE_LINK.finditer(md):
        texto, doi = m.group(1), limpiar_doi(m.group(2))
        if doi in vistos:
            continue
        vistos[doi] = True
        anios = re.findall(r"\b(19\d{2}|20\d{2})\b", texto)
        items.append({"n": len(items) + 1, "texto": texto, "doi": doi, "arxiv": None,
                      "titulo": None, "apellido": primer_apellido(texto, enlace=True),
                      "anio": int(anios[-1]) if anios else None, "sin_verificar": False})
    return items


# ───────────────────────── consultas ─────────────────────────
def crossref_doi(doi: str):
    st, js = get_json("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe=""))
    if st != 200 or not isinstance(js, dict):
        return {"ok": False, "http": st}
    m = js["message"]
    fecha = (m.get("issued") or m.get("published-online") or {}).get("date-parts", [[None]])[0]
    aut = m.get("author") or []
    return {"ok": True, "http": st,
            "titulo": (m.get("title") or [""])[0],
            "autor": (aut[0].get("family") if aut else "") or "",
            "anio": fecha[0] if fecha else None,
            "revista": (m.get("container-title") or [""])[0],
            "tipo": m.get("type"),
            "doi": m.get("DOI")}


def crossref_busqueda(consulta: str, filas: int = 3):
    url = ("https://api.crossref.org/works?rows=%d&query.bibliographic=%s"
           % (filas, urllib.parse.quote(consulta)))
    st, js = get_json(url)
    if st != 200 or not isinstance(js, dict):
        return []
    out = []
    for m in js["message"].get("items", []):
        fecha = (m.get("issued") or {}).get("date-parts", [[None]])[0]
        aut = m.get("author") or []
        out.append({"doi": m.get("DOI"), "titulo": (m.get("title") or [""])[0],
                    "autor": (aut[0].get("family") if aut else "") or "",
                    "anio": fecha[0] if fecha else None,
                    "revista": (m.get("container-title") or [""])[0]})
    return out


def openalex_doi(doi: str):
    st, js = get_json("https://api.openalex.org/works/https://doi.org/" + urllib.parse.quote(doi, safe=""))
    if st != 200 or not isinstance(js, dict):
        return {"ok": False, "http": st}
    return {"ok": True, "http": st, "titulo": js.get("title") or js.get("display_name") or "",
            "anio": js.get("publication_year"), "citas": js.get("cited_by_count")}


def s2_doi(doi: str):
    st, js = get_json("https://api.semanticscholar.org/graph/v1/paper/DOI:%s?fields=title,year,externalIds"
                      % urllib.parse.quote(doi, safe=""))
    if st != 200 or not isinstance(js, dict):
        return {"ok": False, "http": st}
    return {"ok": True, "http": st, "titulo": js.get("title") or "", "anio": js.get("year"),
            "pmid": (js.get("externalIds") or {}).get("PubMed")}


def pubmed_doi(doi: str):
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&term=%s[AID]"
           % urllib.parse.quote(doi))
    st, js = get_json(url)
    if st != 200 or not isinstance(js, dict):
        return {"ok": False, "http": st}
    ids = js.get("esearchresult", {}).get("idlist", [])
    return {"ok": bool(ids), "http": st, "pmid": ids[0] if ids else None}


def arxiv_id(aid: str):
    st, xml = get_text("http://export.arxiv.org/api/query?id_list=" + aid)
    if st != 200 or not xml:
        return {"ok": False, "http": st}
    ent = xml.split("<entry>", 1)[-1]
    t = re.search(r"<title>(.*?)</title>", ent, re.S)
    y = re.search(r"<published>(\d{4})", ent)
    d = re.search(r'<arxiv:doi[^>]*>(.*?)</arxiv:doi>', ent, re.S)
    titulo = re.sub(r"\s+", " ", t.group(1)).strip() if t else ""
    if not titulo or "Error" in titulo:
        return {"ok": False, "http": st}
    return {"ok": True, "http": st, "titulo": titulo, "anio": int(y.group(1)) if y else None,
            "doi_declarado": d.group(1).strip() if d else None}


# ───────────────────────── evaluación ─────────────────────────
def evaluar(it: dict, cr: dict):
    avisos = []
    if it.get("titulo") and cr.get("titulo"):
        s = similitud(it["titulo"], cr["titulo"])
        if s < 0.5:
            avisos.append(f"título difiere (sim {s:.2f}): «{cr['titulo'][:90]}»")
    if it.get("apellido") and cr.get("autor"):
        a, b = norm(it["apellido"]).replace(" ", ""), norm(cr["autor"]).replace(" ", "")
        if a and b and a not in b and b not in a:
            avisos.append(f"primer autor difiere: informe «{it['apellido']}» vs base «{cr['autor']}»")
    if it.get("anio") and cr.get("anio") and abs(it["anio"] - cr["anio"]) > 1:
        avisos.append(f"año difiere: informe {it['anio']} vs base {cr['anio']}")
    return avisos


def verificar(items: list[dict]):
    res = []
    for it in items:
        r = {**it, "crossref": None, "openalex": None, "s2": None, "pubmed": None,
             "arxiv_api": None, "candidatos": [], "avisos": [], "veredicto": ""}
        print(f"[{it['n']:3d}] {it['doi'] or it['arxiv'] or it['texto'][:60]}", flush=True)
        if it["doi"]:
            r["crossref"] = crossref_doi(it["doi"])
            r["openalex"] = openalex_doi(it["doi"])
            r["pubmed"] = pubmed_doi(it["doi"])
            r["s2"] = s2_doi(it["doi"])
            time.sleep(PAUSA_S2)
            if r["crossref"]["ok"]:
                r["avisos"] = evaluar(it, r["crossref"])
                r["veredicto"] = "OK" if not r["avisos"] else "REVISAR"
            elif r["openalex"]["ok"] or r["s2"]["ok"]:
                r["veredicto"] = "OK (sin Crossref)"
            else:
                r["veredicto"] = "DOI NO RESUELVE"
                # intento de rescate por título
                if it.get("titulo"):
                    r["candidatos"] = crossref_busqueda(it["titulo"])
        elif it["arxiv"]:
            r["arxiv_api"] = arxiv_id(it["arxiv"])
            if r["arxiv_api"]["ok"]:
                r["avisos"] = evaluar(it, {"titulo": r["arxiv_api"]["titulo"]})
                r["veredicto"] = "PREPRINT OK" if not r["avisos"] else "PREPRINT REVISAR"
                busq = it.get("titulo") or r["arxiv_api"]["titulo"]
                r["candidatos"] = [c for c in crossref_busqueda(busq, 3)
                                   if similitud(busq, c["titulo"]) >= 0.6]
            else:
                r["veredicto"] = "ARXIV NO RESUELVE"
        else:
            consulta = it.get("titulo") or re.sub(r"\(\d{4}\).*", "", it["texto"])
            r["candidatos"] = crossref_busqueda(consulta, 3)
            mejor = max(r["candidatos"], key=lambda c: similitud(consulta, c["titulo"]), default=None)
            if mejor and similitud(consulta, mejor["titulo"]) >= 0.6:
                r["veredicto"] = "SIN DOI → CANDIDATO"
            else:
                r["veredicto"] = "SIN DOI → NO HALLADO"
        res.append(r)
    return res


# ───────────────────────── salida ─────────────────────────
def marca(x):
    if x is None:
        return "–"
    return "✔" if x.get("ok") else "✘"


def escribir_md(res: list[dict], ruta: Path, informe: str):
    n = len(res)
    cuenta = {}
    for r in res:
        cuenta[r["veredicto"]] = cuenta.get(r["veredicto"], 0) + 1
    L = [f"# Verificación de referencias — {Path(informe).name}", "",
         f"Fecha: {time.strftime('%Y-%m-%d')}. Bases consultadas: Crossref (metadatos canónicos), "
         "OpenAlex, Semantic Scholar (S2), PubMed y la API de arXiv. Scopus y Web of Science no se "
         "consultaron (requieren clave institucional).", "",
         f"Referencias: {n}. Resumen: " + ", ".join(f"{k}: {v}" for k, v in sorted(cuenta.items())), "",
         "Veredictos: **OK** = el DOI resuelve en Crossref y título, primer autor y año coinciden con el "
         "informe; **REVISAR** = resuelve pero algo no coincide (ver aviso); **DOI NO RESUELVE** = ninguna "
         "base conoce ese DOI; **SIN DOI → CANDIDATO** = la búsqueda por título propone un DOI.", "",
         "| # | Ref. (informe) | DOI / arXiv | Crossref | OpenAlex | S2 | PubMed | Veredicto | Avisos / candidato |",
         "|---|---|---|---|---|---|---|---|---|"]
    for r in res:
        ref = r["texto"][:70].replace("|", "\\|") + ("…" if len(r["texto"]) > 70 else "")
        ident = r["doi"] or (f"arXiv:{r['arxiv']}" if r["arxiv"] else "—")
        extra = "; ".join(r["avisos"])
        if r["candidatos"] and r["veredicto"] not in ("OK", "REVISAR"):
            c = r["candidatos"][0]
            extra += (" " if extra else "") + f"candidato: {c['autor']} {c['anio']}, «{c['titulo'][:70]}», DOI {c['doi']}"
        if r.get("arxiv_api") and r["arxiv_api"].get("ok") and r["arxiv_api"].get("doi_declarado"):
            extra += (" " if extra else "") + f"DOI declarado en arXiv: {r['arxiv_api']['doi_declarado']}"
        L.append(f"| {r['n']} | {ref} | {ident} | {marca(r['crossref']) if r['doi'] else '–'} | "
                 f"{marca(r['openalex']) if r['doi'] else '–'} | {marca(r['s2']) if r['doi'] else '–'} | "
                 f"{marca(r['pubmed']) if r['doi'] else '–'} | {r['veredicto']} | {extra.replace('|', '/')} |")
    L += ["", "## Detalle de Crossref (título canónico, primer autor, año, revista)", ""]
    for r in res:
        cr = r.get("crossref")
        if cr and cr.get("ok"):
            L.append(f"- [{r['n']}] {cr['autor']} ({cr['anio']}), «{cr['titulo']}», {cr['revista']} "
                     f"[{cr['tipo']}]. DOI {cr['doi']}")
    ruta.write_text("\n".join(L) + "\n", encoding="utf-8")


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    informe, salida = argv[1], Path(argv[2])
    md = Path(informe).read_text(encoding="utf-8")
    items = extraer_items(md) or extraer_links(md)
    print(f"{len(items)} referencias extraídas de {informe}", flush=True)
    res = verificar(items)
    escribir_md(res, salida, informe)
    if "--json" in argv:
        Path(argv[argv.index("--json") + 1]).write_text(json.dumps(res, ensure_ascii=False, indent=1),
                                                         encoding="utf-8")
    malos = [r for r in res if r["veredicto"] not in ("OK", "PREPRINT OK")]
    print(f"\nListo: {len(res)} referencias; {len(res) - len(malos)} OK, {len(malos)} por revisar → {salida}")
    for r in malos:
        print(f"  [{r['n']}] {r['veredicto']}: {'; '.join(r['avisos']) or r['texto'][:80]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
