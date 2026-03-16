# Estructura de Recursos

## Carpetas

- `assets/static/`: recursos fijos de la web.
- `assets/static/fonts/`: tipografias.
- `assets/static/headers/desktop/`: header de escritorio.
- `assets/static/headers/mobile/`: header de movil.
- `assets/backgrounds/desktop/`: fondo de escritorio.
- `assets/backgrounds/mobile/`: fondo de movil.
- `assets/projects/`: manifest de mini reproductores.
- `assets/drawer/`: cajon para guardar versiones antiguas.

## Archivos activos (rutas fijas)

- Header escritorio: `assets/static/headers/desktop/header.svg`
- Header movil: `assets/static/headers/mobile/header.png`
- Fondo escritorio video: `assets/backgrounds/desktop/background.mp4`
- Fondo movil video: `assets/backgrounds/mobile/background.mp4`
- Fondo escritorio imagen fallback: `assets/backgrounds/desktop/background.jpg`
- Fondo movil imagen fallback: `assets/backgrounds/mobile/background.jpg`
- Manifest de proyectos: `assets/projects/manifest.json`

## Como sustituir recursos rapido

- Header escritorio: reemplaza `header.svg` por otro con el mismo nombre.
- Header movil: reemplaza `header.png` por otro con el mismo nombre.
- Fondo escritorio: reemplaza `background.mp4` (y opcionalmente `background.jpg`).
- Fondo movil: reemplaza `background.mp4` (y opcionalmente `background.jpg`).

## Tamano recomendado de fondo movil

- Formato vertical 9:19.5 (ejemplos: `1080x2340`, `1170x2532`).
- Mantener zona importante del arte hacia la izquierda.
- Si usas imagen de fallback: exportar en PNG/JPG con ese ratio.

## Comportamiento si falta el header

- Si falta el archivo del header activo (desktop o movil), el header no se muestra.
- No se usa fallback automatico entre desktop y movil.

## Mini reproductores movibles y redimensionables

- Los proyectos se renderizan desde `assets/projects/manifest.json`.
- Cada proyecto vive en su propia carpeta dentro de `assets/projects/`.
- Desktop:
  - Cada reproductor es una ventana independiente.
  - Se mueve arrastrando la barra superior.
  - Se hace grande o pequeno arrastrando desde las esquinas.
  - No existe player separado.
- Movil:
  - Se muestra una columna de videos a la derecha.
  - No son movibles ni redimensionables.
  - Sin HUD/controles del reproductor.
  - La columna hace scroll sin mover el fondo.

## Campos del manifest

- `id`: identificador unico.
- `folder`: ruta de la carpeta del proyecto.
- `file`: nombre del video dentro de la carpeta.
- `title` (opcional): si no se indica, se genera automaticamente desde `file`.
- `poster` (opcional): si no se indica, usa `poster.jpg` dentro de la carpeta.
- `x`: posicion horizontal en porcentaje (desktop).
- `y`: posicion vertical en porcentaje (desktop).
- `w` (opcional): ancho inicial en pixeles.
- `h` (opcional): alto inicial en pixeles.

## Estructura recomendada de proyecto

- `assets/projects/<slug>/<video>.mp4`
- `assets/projects/<slug>/poster.jpg` (opcional)

## Generacion automatica del manifest

- Generar una vez:
  - `python3 scripts/update_projects_manifest.py`
- Modo automatico (watch):
  - `python3 scripts/update_projects_manifest.py --watch`
- En modo watch, cuando creas carpeta o cambias videos dentro de `assets/projects/`, se regenera `assets/projects/manifest.json`.

## Versiones antiguas

- Guarda las versiones previas en `assets/drawer/` con nombres descriptivos:
  - `header_desktop_v1.svg`
  - `background_mobile_v3.mp4`
