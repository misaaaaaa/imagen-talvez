#!/usr/bin/env python3
"""Servidor local para editor.html: sirve el repo y guarda constelaciones.

    python3 editor.py          -> abre http://127.0.0.1:8765/editor.html

Escribe constelacion.md y constelaciones/<nombre>.md (enteros), la línea de
tags de cada imagen en imagenes.md (solo esa línea) y el vocabulario tags.md.
"""
import json
import sys
import re
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

BASE = Path(__file__).resolve().parent
PUERTO = 8765
PERMITIDO = re.compile(r"^(constelacion|constelaciones/[a-z0-9-]+)\.md$")


TAG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINEA_TAGS = re.compile(r"^\s*(?:\*[a-z0-9-]+\*\s*)*\*[a-z0-9-]+\*(\s*)(.*)$")


def editar_tags(md, slug, tags):
    """Reemplaza solo la línea de tags del bloque "## slug" de imagenes.md."""
    m = re.search(rf"^## {re.escape(slug)}[ \t]*$", md, re.M)
    if not m:
        raise ValueError(f"no existe la imagen {slug}")
    ini = m.end()
    sig = re.search(r"^## ", md[ini:], re.M)
    fin = ini + sig.start() if sig else len(md)
    lineas = md[ini:fin].split("\n")
    nuevo = " ".join(f"*{t}*" for t in tags)

    idx = next((i for i, l in enumerate(lineas) if LINEA_TAGS.match(l)), None)
    if idx is not None:
        espacio, resto = LINEA_TAGS.match(lineas[idx]).groups()  # resto: p. ej. "-->"
        if nuevo:
            lineas[idx] = nuevo + espacio + resto
        elif resto:
            lineas[idx] = resto
        else:
            del lineas[idx]
            if idx < len(lineas) and idx > 0 and lineas[idx - 1] == "" and lineas[idx] == "":
                del lineas[idx]
    elif nuevo:
        k = next((i for i, l in enumerate(lineas) if "](" in l), None)
        if k is None:
            raise ValueError(f"{slug} no tiene imagen")
        lineas[k + 1:k + 1] = ["", nuevo]
    return md[:ini] + "\n".join(lineas) + md[fin:]


LINEA_FECHA = re.compile(r"^fecha:.*$")


def bloque(md, slug):
    """Inicio y fin del cuerpo del bloque "## slug" en imagenes.md."""
    m = re.search(rf"^## {re.escape(slug)}[ \t]*$", md, re.M)
    if not m:
        raise ValueError(f"no existe la imagen {slug}")
    ini = m.end()
    sig = re.search(r"^## ", md[ini:], re.M)
    return ini, ini + sig.start() if sig else len(md)


def editar_fecha(md, slug, fecha):
    """Escribe, cambia o borra la línea "fecha: ..." del bloque "## slug"."""
    fecha = " ".join(fecha.split())
    ini, fin = bloque(md, slug)
    lineas = md[ini:fin].split("\n")
    idx = next((i for i, l in enumerate(lineas) if LINEA_FECHA.match(l)), None)
    if idx is not None:
        if fecha:
            lineas[idx] = "fecha: " + fecha
        else:
            del lineas[idx]
            if 0 < idx < len(lineas) and lineas[idx - 1] == "" and lineas[idx] == "":
                del lineas[idx]
    elif fecha:
        # después de la línea de tags o, si no hay, después de la imagen
        k = next((i for i, l in enumerate(lineas) if LINEA_TAGS.match(l)), None)
        if k is None:
            k = next((i for i, l in enumerate(lineas) if "](" in l), None)
        if k is None:
            raise ValueError(f"{slug} no tiene imagen")
        lineas[k + 1:k + 1] = ["", "fecha: " + fecha]
    return md[:ini] + "\n".join(lineas) + md[fin:]


def archivos():
    lista = ["constelacion.md"]
    lista += sorted(f"constelaciones/{p.name}" for p in (BASE / "constelaciones").glob("*.md"))
    return lista


class Manejador(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(BASE), **k)

    def log_message(self, formato, *args):
        pass  # solo se imprime lo que se guarda

    def copyfile(self, origen, destino):
        try:
            super().copyfile(origen, destino)
        except OSError:
            pass  # el navegador cortó la descarga; la volverá a pedir

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def responder(self, codigo, datos):
        cuerpo = json.dumps(datos, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def do_GET(self):
        if urlparse(self.path).path == "/api/archivos":
            return self.responder(200, archivos())
        return super().do_GET()

    def leer_json(self):
        largo = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(largo).decode("utf-8"))

    def do_POST(self):
        url = urlparse(self.path)
        if url.path == "/api/tags/imagen":
            datos = self.leer_json()
            tags = list(dict.fromkeys(datos.get("tags", [])))
            if not all(TAG.match(t) for t in tags):
                return self.responder(400, {"error": "tag inválido"})
            ruta = BASE / "imagenes.md"
            try:
                md = editar_tags(ruta.read_text(encoding="utf-8"), datos.get("slug", ""), tags)
            except ValueError as e:
                return self.responder(400, {"error": str(e)})
            ruta.write_text(md, encoding="utf-8")
            print(f"tags de {datos['slug']}: {' '.join(tags) or '(ninguno)'}")
            return self.responder(200, {"ok": True, "tags": tags})
        if url.path == "/api/fecha":
            datos = self.leer_json()
            ruta = BASE / "imagenes.md"
            try:
                md = editar_fecha(ruta.read_text(encoding="utf-8"), datos.get("slug", ""), datos.get("fecha", ""))
            except ValueError as e:
                return self.responder(400, {"error": str(e)})
            ruta.write_text(md, encoding="utf-8")
            print(f"fecha de {datos['slug']}: {datos.get('fecha') or '(ninguna)'}")
            return self.responder(200, {"ok": True, "fecha": " ".join(datos.get("fecha", "").split())})
        if url.path == "/api/tags/nuevo":
            tag = self.leer_json().get("tag", "")
            if not TAG.match(tag):
                return self.responder(400, {"error": f"tag inválido: {tag}"})
            ruta = BASE / "tags.md"
            md = ruta.read_text(encoding="utf-8") if ruta.exists() else "# Tags\n"
            if not re.search(rf"^- {re.escape(tag)}\s*$", md, re.M):
                ruta.write_text(md.rstrip("\n") + f"\n- {tag}\n", encoding="utf-8")
                print(f"tag nuevo: {tag}")
            return self.responder(200, {"ok": True, "tag": tag})
        if url.path != "/api/guardar":
            return self.responder(404, {"error": "no existe"})
        archivo = parse_qs(url.query).get("archivo", [""])[0]
        if not PERMITIDO.match(archivo):
            return self.responder(400, {"error": f"archivo no permitido: {archivo}"})
        largo = int(self.headers.get("Content-Length", 0))
        texto = self.rfile.read(largo).decode("utf-8")
        destino = BASE / archivo
        destino.parent.mkdir(exist_ok=True)
        destino.write_text(texto, encoding="utf-8")
        print(f"guardado {archivo} ({len(texto)} caracteres)")
        return self.responder(200, {"ok": True, "archivo": archivo})


if __name__ == "__main__":
    servidor = ThreadingHTTPServer(("127.0.0.1", PUERTO), Manejador)
    url = f"http://127.0.0.1:{PUERTO}/editor.html"
    print(f"editor en {url}  (ctrl+c para salir)")
    if "--sin-navegador" not in sys.argv:
        webbrowser.open(url)
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        pass
