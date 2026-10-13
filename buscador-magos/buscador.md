# Guía: imágenes de dominio público y acceso abierto sobre "mago"

Uso previsto: contextos académicos (trabajos, presentaciones, tesis, material docente).

---

## 1. Antes de buscar: tres puntos que cambian los resultados

### 1.1 "Mago" es ambiguo: delimitación y exclusión de cultura popular

> ⚠️ **Criterio de exclusión clave:** No interesan los magos de la cultura popular contemporánea, franquicias comerciales ni fantasía moderna (p. ej., Harry Potter, Gandalf / *El Señor de los Anillos*, Dungeons & Dragons, cómics, videojuegos, cine reciente). La búsqueda debe centrarse exclusivamente en perspectivas históricas, documentales, mítico-literarias clásicas, artísticas, antropológicas y del ilusionismo escénico histórico. Tampoco incluyas más a Houdini o magos del espectáculo del Siglo XX, tardío Siglo XIX.

La palabra cubre figuras distintas a lo largo de la historia, y cada una tiene su propio vocabulario visual. Define cuál necesitas dentro de este enfoque documental e histórico:

| Sentido de "mago" (histórico / documental) | Qué abarca | Términos de búsqueda sugeridos |
|---|---|---|
| Magia ritual / brujería clásica | Hechicería histórica, grimorios, círculos mágicos | `sorcerer`, `necromancer`, `hechicero`, `witchcraft` |
| Ilusionista / prestidigitador histórico | Trucos callejeros, cartelería de teatro y vodevil (s. XV–inicios s. XX) | `magician`, `conjurer`, `illusionist`, `prestidigitador`, `escamoteur` |
| Reyes Magos (Biblia / Antigüedad tardía) | Sacerdotes-astrónomos orientales, ofrenda | `Magi`, `Three Kings`, `Adoration of the Magi`, `Reyes Magos` |
| Sacerdote persa (zoroastrismo antiguo) | Origen etimológico del término *magus* | `magus`, `magi`, `Zoroastrian priest` |
| Figuras literarias/míticas canónicas | Arquetipos del folclore y literatura clásica premoderna | `Merlin`, `Merlín`, `Prospero`, `Faust`, `Circe`, `Hermogenes` |
| Tarot y esoterismo histórico | Arcanos mayores (Marsella, Rider-Waite 1909), hermetismo | `The Magician`, `Le Bateleur`, `El Mago tarot` |
| Alquimia y ciencias ocultas | Filosofía natural renacentista y barroca | `alchemist`, `alquimista`, `occult`, `philosopher's stone` |

### 1.2 Busca en varios idiomas

Los repositorios internacionales indexan sobre todo en inglés, francés, alemán y latín. Si solo buscas "mago" perderás la mayoría de los resultados. Prueba también `magus`, `magicien` (fr), `Zauberer` (de), `mago` (it) y `magus` (latín).

### 1.3 Dominio público ≠ cualquier "gratis"

- **Dominio público (PD / PDM):** sin derechos de autor vigentes.
- **CC0:** el titular renuncia a sus derechos. En la práctica equivale a dominio público.
- **CC BY / CC BY-SA:** libres, pero **no** son dominio público: exigen atribución (y, en SA, compartir igual).
- **Unsplash, Pexels, Pixabay:** licencias propias, **no** dominio público. Evítalas si necesitas dominio público estricto.

Para "mago" esto importa doblemente: además del impedimento legal (gran parte de la imagen contemporánea de magos como Gandalf, Harry Potter, Dungeons & Dragons, etc. está protegida por copyright y marcas registradas), **estas representaciones de la cultura pop quedan expresamente fuera del interés del proyecto**. Las fuentes requeridas son grabados, manuscritos iluminados, pinturas históricas, mosaicos, documentos esotéricos y cartelería de época conservados en archivos y museos.

---

## 2. Repositorios recomendados

### A. Agregadores (una sola búsqueda, muchas fuentes)

#### Openverse
- Web: https://openverse.org
- Cómo buscar: escribe `wizard` → en **Filtros → Licencias** marca **"Dominio público"** (CC0 y Public Domain Mark).
- API: `https://api.openverse.org/v1/images/?q=wizard&license=cc0,pdm`
- Ventaja: cubre muchas fuentes a la vez. Desventaja: algunos resultados llevan metadatos incompletos; **verifica en la página original**.

#### Europeana
- Web: https://www.europeana.eu/es
- Cómo buscar: busca `mago` o `magus` → filtros: **Tipo: Imagen** y **Reutilización: "Dominio público"**.
- Ventaja: interfaz en español y colecciones de bibliotecas y museos europeos (manuscritos iluminados, grabados).
- API: requiere clave gratuita.

#### Digital Public Library of America (DPLA)
- Web: https://dp.la
- Cómo buscar: `wizard` o `magician` → revisa el campo **"Rights"** de cada ítem.

#### Wikimedia Commons
- Web: https://commons.wikimedia.org
- Cómo buscar: `wizard`, `magician`, o navega por categorías (`Category:Wizards`, `Category:Magicians`, `Category:Adoration of the Magi`).
- Ejemplo de búsqueda: `wizard incategory:"Public domain"` o revisa la plantilla de licencia en cada archivo.
- ⚠️ **Licencias mezcladas.** Es enorme y útil, pero cada archivo tiene su propia licencia: lee la sección "Licencia" de la ficha de cada imagen.

### B. Museos con acceso abierto (CC0 / dominio público)

#### The Metropolitan Museum of Art
- Web: https://www.metmuseum.org/art/collection/search → marca **"Open Access"**.
- API (sin clave): `https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&isPublicDomain=true&q=wizard`
- Buen punto de partida para: arte europeo, escenas de Reyes Magos, grabados.

#### Art Institute of Chicago
- Web: https://www.artic.edu/collection → filtra **"Public Domain"**.
- API: `https://api.artic.edu/api/v1/artworks/search?q=wizard&query[term][is_public_domain]=true`

#### Cleveland Museum of Art
- Web: https://www.clevelandart.org/art/collection/search → filtra **"Open Access"**.
- API: `https://openaccess-api.clevelandart.org/api/artworks/?q=wizard&cc0`

#### Rijksmuseum
- Web: https://www.rijksmuseum.nl/en/rijksstudio
- Ventaja: imágenes de alta resolución, muchas de grabados y pintura holandesa (buena para Reyes Magos y alquimistas).

#### Smithsonian Open Access
- Web: https://www.si.edu/openaccess → filtra por **CC0**.
- API: `https://api.si.edu/openaccess/api/v1.0/search?q=wizard&api_key=TU_CLAVE` (clave gratuita en https://api.data.gov/signup).

#### Wellcome Collection
- Web: https://wellcomecollection.org/works → filtra **Licencias: "Public Domain Mark"** o **CC0**.
- Muy útil para: alquimia, magia, ocultismo, medicina antigua, grabados de brujería.

#### Getty Open Content
- Web: https://www.getty.edu/art/collection → filtra **"Open Content"**.

### C. Bibliotecas y archivos

#### Library of Congress
- Web: https://www.loc.gov/pictures/ y https://www.loc.gov/free-to-use/
- Cómo buscar: `magician` (carteles históricos de espectáculos de magia son abundantes). Revisa siempre el **"Rights Advisory"**.

#### New York Public Library Digital Collections
- Web: https://digitalcollections.nypl.org → marca **"Public domain"** en filtros.

#### Internet Archive
- Web: https://archive.org
- Libros antiguos ilustrados sobre magia, alquimia y demonología (siglos XV–XIX). Además, la colección **"Internet Archive Book Images"** en Flickr contiene ilustraciones extraídas de libros: https://www.flickr.com/photos/internetarchivebookimages

#### Biblioteca Digital Hispánica (Biblioteca Nacional de España)
- Web: https://bdh.bne.es
- Cómo buscar: `mago`, `hechicero`, `Reyes Magos`. Útil para material en español, aunque **revisa las condiciones de reutilización** de cada documento: no todo está en dominio público.

#### Flickr Commons
- Web: https://www.flickr.com/commons
- Archivos de instituciones con "sin restricciones de derechos de autor conocidas". Ojo: "no known copyright restrictions" **no equivale a una garantía** de dominio público.

#### NASA Image and Video Library
- Sin relevancia temática directa para "mago", pero sirve si buscas, por ejemplo, la nebulosa "El Mago" (*Wizard Nebula*, NGC 7380). Búscala con `Wizard Nebula`.

---

## 3. Flujo de trabajo recomendado

1. **Define el sentido de "mago"** (sección 1.1) y arma 5–8 términos de búsqueda en varios idiomas.
2. **Empieza por Openverse y Europeana** con filtro de dominio público.
3. **Profundiza en museos y bibliotecas** (Met, Rijksmuseum, Wellcome, Library of Congress) con los mismos términos.
4. **Verifica la licencia en la fuente original**, no solo en el agregador.
5. **Descarga la mayor resolución disponible** y registra los metadatos (sección 4).
6. **Cita la fuente aunque no sea obligatorio.** En lo académico, atribuir es buena práctica y permite que otros verifiquen.

---

## 4. Registro de metadatos (plantilla)

Guarda esto por cada imagen. Si alguien cuestiona el uso, necesitas poder demostrar el origen y la condición legal.

```
Título:
Autor / artista (si se conoce):
Fecha de la obra:
Institución o repositorio:
URL de la ficha:
Fecha de consulta:
Licencia / declaración de derechos (ej. CC0, PDM):
Notas (ej. "fotografía de obra del s. XVI; reproducción fiel"):
```

**Formato de cita sugerido (adáptalo a APA, MLA, Chicago, etc.):**

> Autor. (Año). *Título de la obra* [Grabado/Pintura/Manuscrito]. Institución. URL. Dominio público.

---

## 5. Limitaciones que debes tener presentes

- **El dominio público depende del país.** Una obra puede estar libre en un país y protegida en otro (según la fecha de muerte del autor y las leyes locales). Las instituciones que marcan explícitamente **CC0 o PDM** reducen el riesgo.
- **Reproducciones fotográficas de obras antiguas:** en muchas jurisdicciones una reproducción fiel de una obra 2D en dominio público no genera nuevos derechos, pero **no es universal**. Prefiere repositorios que declaren la imagen como libre.
- **Derechos que persisten aunque la obra sea de dominio público:** marcas, derechos de imagen de personas fotografiadas, y restricciones de uso que algunas instituciones imponen por contrato.
- **Las condiciones de las APIs cambian.** Revisa la documentación oficial antes de automatizar descargas o construir algo sobre ellas.
- **Esta guía no es asesoría legal.** Si la imagen irá a una publicación formal, consulta la política de derechos de tu institución o editorial.

---

## 6. Ejemplos de búsqueda para empezar

| Qué buscas | Término | Dónde probar primero |
|---|---|---|
| Hechicero medieval | `wizard`, `magus` | Wellcome, Internet Archive, Europeana |
| Mago ilusionista (siglos XIX–XX) | `magician poster` | Library of Congress, NYPL |
| Reyes Magos | `Adoration of the Magi` | Met, Rijksmuseum, Europeana |
| Merlín / Arturo | `Merlin` | Internet Archive, Wikimedia Commons |
| Alquimista | `alchemist` | Wellcome, Rijksmuseum, Getty |
| Carta del tarot | `The Magician tarot` | Wikimedia Commons, Met |