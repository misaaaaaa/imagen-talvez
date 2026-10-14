#!/usr/bin/env python3
import html
import os
import random
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "imagenes"
INDEX_HTML = BASE_DIR / "index.html"
IMAGES_MD = BASE_DIR / "imagenes.md"

VALID_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif", ".svg"}


def parse_images_from_md():
    """Lee imagenes.md, ignora comentarios HTML y extrae las imágenes activas."""
    if not IMAGES_MD.exists():
        print(f"Aviso: {IMAGES_MD} no existe. Se leerá directamente la carpeta imagenes/.")
        return None

    text = IMAGES_MD.read_text(encoding="utf-8")

    # Eliminar bloques de comentarios HTML: <!-- ... --> (multilínea o en una sola línea)
    text_without_comments = re.sub(r'<!--[\s\S]*?-->', '', text)

    # Extraer imágenes en formato Markdown: ![alt](url)
    md_img_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
    items = []

    for match in md_img_pattern.finditer(text_without_comments):
        alt_text = match.group(1).strip()
        img_path = match.group(2).strip()

        # Resolver la ruta en disco (puede ser relativa a imagenes/ o a la raíz del repositorio)
        rel_path = img_path.lstrip("./")
        file_on_disk = BASE_DIR / rel_path
        if not file_on_disk.is_file():
            # Intentar también directamente dentro de IMAGES_DIR por nombre de archivo
            filename = Path(rel_path).name
            file_on_disk = IMAGES_DIR / filename
            target_src = f"imagenes/{filename}"
            if not file_on_disk.is_file():
                file_on_disk = BASE_DIR / "buscador-magos" / "magos-img" / filename
                target_src = f"buscador-magos/magos-img/{filename}"
        else:
            target_src = rel_path

        if file_on_disk.is_file() and file_on_disk.suffix.lower() in VALID_EXTENSIONS:
            items.append({
                "src": target_src,
                "alt": alt_text or file_on_disk.stem.replace("-", " ").replace("_", " ").title()
            })
        else:
            print(f"Aviso: archivo referenciado en imagenes.md no encontrado o no válido: {img_path}")

    return items


def get_image_files_fallback():
    """Si no hay imagenes.md, lee directamente la carpeta imagenes/."""
    if not IMAGES_DIR.exists():
        return []
    files = [
        f.name
        for f in IMAGES_DIR.iterdir()
        if f.is_file() and f.suffix.lower() in VALID_EXTENSIONS and not f.name.startswith(".")
    ]
    items = []
    for f in files:
        alt = Path(f).stem.replace("-", " ").replace("_", " ").title()
        items.append({"src": f"imagenes/{f}", "alt": alt})
    return items


def build_images_html(items):
    lines = []
    for item in items:
        safe_alt = html.escape(item["alt"], quote=True)
        featured = ' class="featured"' if item["src"] == "imagenes/mago.jpg" else ""
        lines.append(f'    <img src="{item["src"]}" alt="{safe_alt}"{featured}>')
    return "\n".join(lines)


def update_index_html():
    if not INDEX_HTML.exists():
        print(f"Error: {INDEX_HTML} no encontrado.")
        return

    content = INDEX_HTML.read_text(encoding="utf-8")

    images = parse_images_from_md()
    if images is None:
        images = get_image_files_fallback()

    random.shuffle(images)

    new_images_html = build_images_html(images)

    pattern = r'(<div class="mosaic" id="mosaic">)[\s\S]*?(</div>)'
    replacement = f"\\1\n{new_images_html}\n  \\2"

    if not re.search(pattern, content):
        print("Error: no se encontró <div class=\"mosaic\" id=\"mosaic\"> en index.html")
        return

    updated_content = re.sub(pattern, replacement, content, count=1)
    INDEX_HTML.write_text(updated_content, encoding="utf-8")
    print(f"index.html actualizado exitosamente con {len(images)} imágenes desde imagenes.md.")


if __name__ == "__main__":
    update_index_html()
