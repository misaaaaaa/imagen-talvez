# imagen-elixir

bitácora en 

---

bitácora del curso dictado por cynthia shuffer en doctorado artes y humanidades: "una imagen, tal vez. genealogías críticas fuera de norma".

---

## Instrucciones: Actualizar el mosaico web

Para actualizar las imágenes desplegadas en [index.html](./index.html):

1. Edita el archivo [imagenes.md](./imagenes.md) agregando, quitando o comentando las imágenes que deseas mostrar.
   - Las imágenes deben estar guardadas localmente dentro del repositorio; puedes usar rutas relativas desde la raíz, como `./imagenes/archivo.jpg` o `./buscador-magos/magos-img/archivo.jpg`.
   - El texto alternativo entre corchetes `![descripción](./imagenes/archivo.ext)` se usará como pie de foto en el modal.
   - Para ocultar una imagen sin borrarla, coméntala usando `<!-- ![...](./imagenes/archivo.ext) -->`.
2. Ejecuta el script de actualización en la terminal:

```bash
python3 grid-update.py
```

El script leerá [imagenes.md](./imagenes.md), ignorará las comentadas y regenerará automáticamente el mosaico en [index.html](./index.html).
