# WEB_700 - Handoff completo para Claude Code

## 1) Objetivo del proyecto

Landing visual para "SEVENHUNDRED" con:
- Header grande de marca (desktop y mobile diferenciados).
- Fondo visual (video en loop + fallback a imagen).
- Footer con 3 items de contacto.
- Nube de mini reproductores de proyectos.

Direccion visual pedida:
- Estetica oscura, limpia, editorial.
- Desktop sin scroll, pagina estatica.
- Mobile con composicion distinta y reproductores en columna derecha.

## 2) Ruta de trabajo actual

Ruta activa actual:
- `/Users/alainlazabarbieri/Library/Mobile Documents/com~apple~CloudDocs/CLAUDE_ICLOUD/700/WEB_700`

Ruta anterior (desarrollo original por Marcos):
- `/Users/alainlazabarbieri/Library/Mobile Documents/com~apple~CloudDocs/CLAUDE_ICLOUD/700/WEB_700`

Nota:
- Proyecto migrado de la máquina de Marcos a iCloud de Alain.

## 3) Estructura actual de archivos

Archivos clave:
- `index.html`
- `styles.css`
- `ASSETS_GUIDE.md`
- `scripts/update_projects_manifest.py`

Carpetas clave:
- `assets/static/fonts`
- `assets/static/headers/desktop`
- `assets/static/headers/mobile`
- `assets/backgrounds/desktop`
- `assets/backgrounds/mobile`
- `assets/projects`
- `assets/drawer`

## 4) Comportamiento implementado

### 4.1 Header

- Header desktop y mobile separados.
- Si falta el archivo del header activo, no se muestra (hide-if-missing).
- No hay fallback automatico entre desktop y mobile.

Rutas esperadas:
- Desktop: `assets/static/headers/desktop/header.svg`
- Mobile: `assets/static/headers/mobile/header.png`

### 4.2 Fondo

- Se usa video de fondo y fallback de imagen.
- Si el video falla, se oculta y queda visible la imagen de fondo.
- El video ahora solo aparece cuando esta listo (`is-ready`) para evitar pantalla negra.

Rutas esperadas:
- Desktop video: `assets/backgrounds/desktop/background.mp4`
- Mobile video: `assets/backgrounds/mobile/background.mp4`
- Desktop imagen fallback: `assets/backgrounds/desktop/background.jpg`
- Mobile imagen fallback: `assets/backgrounds/mobile/background.jpg`

Estado detectado reciente:
- En mobile faltaba `background.mp4`, por eso no salia bien el fondo.
- Se dejo fallback robusto para que siempre se vea `background.jpg`.

### 4.3 Footer

- Footer en parte baja con 3 items:
  - WORK
  - Telefono
  - Email
- Espaciado horizontal entre categorias.

### 4.4 Mini reproductores de proyectos

Desktop:
- Reproductores tipo ventana.
- Movibles (drag en barra superior).
- Redimensionables (esquinas).
- Sin reproductor separado flotante.

Mobile:
- Columna vertical a la derecha.
- Sin drag y sin resize.
- Sin HUD/controles visibles del reproductor.
- Scroll en la columna de videos, sin mover fondo.

## 5) Fuente de datos de proyectos

Fuente principal:
- `assets/projects/manifest.json`

Script de soporte:
- `scripts/update_projects_manifest.py`

Uso:
- Generar manifest una vez:
  - `python3 scripts/update_projects_manifest.py`
- Modo watch:
  - `python3 scripts/update_projects_manifest.py --watch`

Regla de titulos:
- El titulo visible se construye con nombre de archivo de video (si no se define `title`).

Estructura recomendada por proyecto:
- `assets/projects/<carpeta_proyecto>/<video>.mp4`
- `assets/projects/<carpeta_proyecto>/poster.jpg` (opcional)

## 6) Decisiones tecnicas tomadas durante el proceso

- Desktop bloqueado sin scroll.
- Eliminacion de recuadros/blancos no deseados.
- Mejora de nitidez de header proponiendo SVG.
- Cambio de fondo de imagen a video en loop.
- Ajuste de loop para minimizar micro-cortes.
- Ajustes de tamano y posicion de links/footer.
- En mobile, layout diferente para respetar composicion de arte.

## 7) Comandos utiles

Servidor local:
```bash
cd "/Users/alainlazabarbieri/Library/Mobile Documents/com~apple~CloudDocs/CLAUDE_ICLOUD/700/WEB_700"
python3 -m http.server 4173
```

URL local:
- `http://localhost:4173`

Parar servidor:
- `Ctrl + C`

Empaquetado shareable (sin .git):
```bash
cd "/Users/alainlazabarbieri/Library/Mobile Documents/com~apple~CloudDocs/CLAUDE_ICLOUD/700"
zip -r "WEB_700_claude_code_YYYYMMDD_HHMMSS.zip" "WEB_700" \
  -x "WEB_700/.git/*" "WEB_700/.DS_Store" "*/.DS_Store"
```

## 8) Estado Git actual (importante)

Commit local detectado:
- `a5fb2fa Initial commit WEB_700`

Problema actual de remoto:
- `origin` apunta a una ruta local (no a GitHub):
  - `/Users/alainlazabarbieri/Library/Mobile Documents/com~apple~CloudDocs/CLAUDE_ICLOUD/700/WEB_700`

Esto significa:
- Git local funciona, pero no esta empujando a GitHub remoto real.

Solucion recomendada:
```bash
cd "/Users/alainlazabarbieri/Library/Mobile Documents/com~apple~CloudDocs/CLAUDE_ICLOUD/700/WEB_700"
git remote set-url origin https://github.com/<usuario>/<repo>.git
git push -u origin main
```

## 9) Publicacion online y traspaso a cliente (resumen)

Flujo recomendado:
1. Repositorio en GitHub.
2. Conectar repo a Vercel/Netlify.
3. Configurar dominio del cliente (DNS + SSL).
4. Entregar propiedad al cliente:
   - Repo: cliente propietario.
   - Hosting: cuenta cliente.
   - Dominio: cuenta cliente.
   - Tu usuario como colaborador.

Si el repo empezo en cuenta del desarrollador:
- Transferir ownership al cliente antes o durante handoff final.

## 10) Checklist rapido para continuar sin bloqueo

1. Confirmar que `origin` apunte a GitHub real.
2. Push de `main`.
3. Verificar repo en web GitHub.
4. Levantar localhost y validar UI desktop/mobile.
5. Si se anaden carpetas de proyecto, regenerar `manifest.json` (o usar `--watch`).
6. Mantener assets activos con nombres de ruta fija (header/background).

## 11) Nota final para Claude Code

Prioridad de continuidad:
- Mantener look and feel actual.
- No romper flujo de sustitucion de assets por nombre fijo.
- Respetar diferencias de comportamiento entre desktop y mobile.
- Mantener fallback de fondo cuando falte video mobile.

