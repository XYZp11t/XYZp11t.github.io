# 11. Modelo sunRunner3D — Simulaciones MHD de viento solar

Documentación de la página `/investigacion/modelo-sunrunner3d`, que presenta la visualización interactiva de simulaciones globales MHD de corrientes de viento solar generadas con el modelo sunRunner3D.

---

## Índice

1. [Descripción](#descripción)
2. [Ubicación de archivos](#ubicación-de-archivos)
3. [Cómo actualizar el video](#cómo-actualizar-el-video)
4. [Convención de nombres de archivo](#convención-de-nombres-de-archivo)
5. [Detección automática del video más reciente](#detección-automática-del-video-más-reciente)
6. [Fecha de actualización dinámica](#fecha-de-actualización-dinámica)
7. [Internacionalización (ES / EN)](#internacionalización-es--en)
8. [Estructura de la página](#estructura-de-la-página)
9. [Responsividad](#responsividad)

---

## Descripción

La página muestra:

- Un **encabezado** con el título, reloj UTC en tiempo real y selector de idioma (ES / EN).
- Un **reproductor de video** con el video de simulación más reciente y su poster.
- Una **tarjeta de descripción** con la fecha de actualización del video y el texto explicativo del modelo.
- Un bloque de **instituciones colaboradoras** (Predictive Science Inc, ENES Morelia, LACIGE).
- Una sección de **referencias científicas** (artículos y tesis relacionados con sunRunner3D).

---

## Ubicación de archivos

| Recurso | Ruta |
|---------|------|
| Página Astro | `src/pages/investigacion/modelo-sunrunner3d.astro` |
| Videos de simulación | `public/sw-prediction/` |
| Posters de video | `public/sw-prediction/` |
| Ruta URL | `/investigacion/modelo-sunrunner3d` |

---

## Cómo actualizar el video

1. Coloca el nuevo video MP4 en `public/sw-prediction/` siguiendo la convención de nombres.
2. Coloca la imagen poster (PNG) correspondiente en el mismo directorio.
3. Ejecuta `npm run build` (o haz deploy). La página detectará automáticamente el video más reciente.

> **No es necesario modificar ningún archivo de código.** El sistema detecta el video con el número de rotación de Carrington más alto y lo usa como fuente del reproductor.

---

## Convención de nombres de archivo

### Video

```
cr{CR}.mp4
```

### Poster

```
poster_cr{CR}.png
```

Donde `{CR}` es el número de rotación de Carrington (entero), por ejemplo:

| Archivo | Rotación de Carrington |
|---------|------------------------|
| `cr2307.mp4` | CR 2307 |
| `poster_cr2307.png` | CR 2307 |
| `cr2308.mp4` | CR 2308 (más reciente) |
| `poster_cr2308.png` | CR 2308 (más reciente) |

El sistema selecciona el archivo con el **número CR más alto** como el video activo.

---

## Detección automática del video más reciente

La detección ocurre en el **frontmatter de Astro**, ejecutado en Node.js durante la compilación:

```typescript
import { readdir, stat } from 'node:fs/promises';
import { join } from 'node:path';

const swDir = join(process.cwd(), 'public', 'sw-prediction');
const dirFiles = await readdir(swDir);

const videoPattern = /^cr(\d+)\.mp4$/;
const videos = dirFiles
  .filter(f => videoPattern.test(f))
  .map(f => ({ file: f, cr: parseInt(f.match(videoPattern)![1], 10) }))
  .sort((a, b) => b.cr - a.cr);

const latest = videos[0];
const videoSrc = `/sw-prediction/${latest.file}`;
const posterSrc = `/sw-prediction/poster_cr${latest.cr}.png`;
```

- Se filtran todos los archivos `.mp4` que coincidan con el patrón `cr{número}.mp4`.
- Se ordenan de **mayor a menor** número de CR.
- Se selecciona el primero (el más reciente).
- El poster correspondiente se construye como `poster_cr{CR}.png`.

---

## Fecha de actualización dinámica

La fecha que aparece en la tarjeta ("Actualizado el: YYYY-MM-DD") se obtiene de la **fecha de modificación del archivo de video** en disco:

```typescript
const videoStat = await stat(join(swDir, latest.file));
const videoDate = videoStat.mtime.toISOString().split('T')[0]; // YYYY-MM-DD
```

Esto garantiza que la fecha mostrada corresponde siempre al video activo, sin necesidad de actualizarla manualmente.

---

## Internacionalización (ES / EN)

La página soporta cambio de idioma en tiempo de ejecución mediante JavaScript en el cliente. El idioma seleccionado se guarda en `localStorage` con la clave `prediction-lang`.

### Textos traducibles

| ID de elemento | ES | EN |
|----------------|----|----|
| `section-label` | Investigación | Research |
| `page-title` | Simulaciones globales MHD... | Global MHD Simulations... |
| `timestamp-label` | Actualizado el: | Updated: |
| `video-description` | Texto completo en español | Full text in English |
| `collaborators-label` | Instituciones colaboradoras: | Collaborating institutions: |
| `references-title` | Referencias | References |
| `references-articles-title` | Artículos Científicos | Scientific Articles |
| `references-theses-title` | Tesis | Theses |

> La fecha (`video-date`) **no se traduce** — siempre se muestra en formato ISO `YYYY-MM-DD` independientemente del idioma.

### Reloj en tiempo real

El encabezado muestra la hora actual en UTC, actualizada cada segundo. Se limpia automáticamente al navegar fuera de la página (compatible con View Transitions de Astro).

---

## Estructura de la página

```
<Layout>
  <section.prediction-header>     ← Encabezado azul con título, reloj UTC y selector ES/EN
  <section.video-section>
    <div.video-wrapper>            ← Reproductor de video con poster (16:9, borde dorado)
    <div.video-info>               ← Fecha "Actualizado el:" + descripción del modelo
    <div.video-collaborators>      ← Logos de Predictive Science Inc, ENES Morelia, LACIGE
  <section.references-section>
    <div.references-category>      ← Artículos Científicos (5 artículos)
    <div.references-category>      ← Tesis (2 tesis)
```

---

## Responsividad

| Breakpoint | Comportamiento |
|-----------|---------------|
| `> 768px` | Header con título e controles en fila horizontal |
| `≤ 768px` | Header en columna; controles con ancho completo |
| `≤ 540px` | Controles en columna; tamaño de logos reducido; nombre de Predictive Science oculto |

---

## Menú de navegación

El ítem está en `src/components/Header.astro`, dentro del submenú de **Investigación**:

```typescript
{ label: 'Modelo sunRunner3D', href: '/investigacion/modelo-sunrunner3d' },
```

---

## Próximos pasos

- [10-NEOS-LEOS.md](./10-NEOS-LEOS.md) — Página de reportes de NEOs y LEOs (patrón similar de detección automática)
- [02-ESTRUCTURA-DEL-PROYECTO.md](./02-ESTRUCTURA-DEL-PROYECTO.md) — Estructura general del sitio
- [07-ESTILOS-Y-DISENO.md](./07-ESTILOS-Y-DISENO.md) — Variables CSS y sistema de diseño
