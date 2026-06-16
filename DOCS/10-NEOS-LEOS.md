# 10. Reportes de NEOs y LEOs

Documentación de la página `/investigacion/neos-leos`, que presenta una línea del tiempo dinámica con los reportes técnicos de ingreso de meteoroides, NEOs (Near-Earth Objects), LEOs (Low-Earth Orbit Objects) y otros objetos espaciales a la atmósfera terrestre.

---

## Índice

1. [Descripción](#descripción)
2. [Ubicación del archivo](#ubicación-del-archivo)
3. [Cómo agregar un nuevo reporte](#cómo-agregar-un-nuevo-reporte)
4. [Convención de nombres de archivo](#convención-de-nombres-de-archivo)
5. [Detección dinámica de PDFs](#detección-dinámica-de-pdfs)
6. [Sistema de tipos extensible](#sistema-de-tipos-extensible)
7. [Estructura de la página](#estructura-de-la-página)
8. [Responsividad](#responsividad)

---

## Descripción

La página muestra:

- Un **encabezado** con el título y subtítulo en inglés.
- Un **bloque de texto introductorio** con la descripción del proyecto y del código DAEDALUS.
- Una **línea del tiempo vertical** ordenada **del más reciente al más antiguo**, agrupada por año, donde cada evento muestra:
  - Fecha (día, mes y año).
  - Tipo de evento (con color diferenciado y leyenda dinámica).
  - Localización del evento.
  - Botón **"Ver PDF"** outline con icono que abre el documento en una nueva pestaña.

---

## Ubicación del archivo

| Recurso | Ruta |
|---------|------|
| Página Astro | `src/pages/investigacion/neos-leos.astro` |
| PDFs de reportes | `public/Informes-NEOs-LEOs/` |
| Ruta URL | `/investigacion/neos-leos` |

---

## Cómo agregar un nuevo reporte

1. Coloca el archivo PDF en `public/Informes-NEOs-LEOs/`.
2. Nombra el archivo siguiendo la **convención de nombres** descrita abajo.
3. Ejecuta `npm run build` (o haz deploy). La página lo detectará automáticamente.

> **No es necesario modificar ningún archivo de código.** El sistema lee el directorio en tiempo de compilación, soporta cualquier tipo de objeto espacial y genera la leyenda automáticamente.

---

## Convención de nombres de archivo

El nombre del archivo determina toda la información que se muestra en la línea del tiempo. El formato es:

```
{Tipo}_{Localización}-{DD}-{MM}-{AA}.pdf
```

### Reglas de parsing

El parser separa el nombre del archivo así:

1. Toma los **tres últimos segmentos** separados por `-` como **fecha** (`DD-MM-AA`). Cada uno debe tener exactamente dos dígitos.
2. El resto del nombre es la **cabecera**.
3. En la cabecera, el **primer guion bajo (`_`)** separa el tipo de la localización.
4. En la localización, los `_` restantes se reemplazan por espacios.

### Componentes

| Componente | Descripción | Ejemplo |
|-----------|-------------|---------|
| `Tipo` | Cualquier categoría de objeto. **No hay lista cerrada.** | `Bolido`, `NEO`, `LEO`, `Asteroide`, `Cometa`, `Meteoro`... |
| `Localización` | Nombre del lugar u objeto. Usa `_` en lugar de espacios. Puede contener guiones. | `Valle_Mexico`, `2024_YR4` |
| `DD` | Día con dos dígitos | `16` |
| `MM` | Mes con dos dígitos | `04` |
| `AA` | Año con dos dígitos (se asume siglo XXI, p. ej. `25` → `2025`) | `25` |

### Ejemplos de nombres válidos

| Archivo | Tipo | Localización | Fecha mostrada |
|---------|------|-------------|----------------|
| `Bolido_Michoacan-12-04-25.pdf` | Bólido | Michoacan | 12 de Abril de 2025 |
| `Bolido_Valle_Mexico-16-04-25.pdf` | Bólido | Valle Mexico | 16 de Abril de 2025 |
| `NEO_2024_YR4-24-02-25.pdf` | NEO | 2024 YR4 | 24 de Febrero de 2025 |
| `LEO_482_Kosmos-10-05-25.pdf` | LEO | 482 Kosmos | 10 de Mayo de 2025 |
| `LEO_Starship-13-06-25.pdf` | LEO | Starship | 13 de Junio de 2025 |
| `Asteroide_Apophis-14-08-26.pdf` | Asteroide | Apophis | 14 de Agosto de 2026 |
| `Cometa_C2023_A3-22-09-26.pdf` | Cometa | C2023 A3 | 22 de Septiembre de 2026 |

### Reglas

- Los **tres últimos guiones (`-`)** delimitan la fecha. Cualquier otro guion forma parte de la cabecera.
- Los **guiones bajos (`_`)** separan palabras en la localización.
- El **primer `_` de la cabecera** marca el final del tipo y el inicio de la localización.
- Los archivos cuyo nombre no contenga al menos `Tipo_Localización-DD-MM-AA` son ignorados silenciosamente.

---

## Detección dinámica de PDFs

La detección ocurre en el **frontmatter de Astro**, que se ejecuta en Node.js durante la compilación:

```typescript
import { readdirSync } from 'fs';
import { resolve } from 'path';

const informesDir = resolve('./public/Informes-NEOs-LEOs');
events = readdirSync(informesDir)
  .filter(f => f.toLowerCase().endsWith('.pdf'))
  .map(parseFilename)
  .filter((e): e is EventInfo => e !== null)
  // Más recientes primero
  .sort((a, b) => b.dateISO.localeCompare(a.dateISO));
```

- Los archivos se ordenan **del más reciente al más antiguo**.
- Se agrupan automáticamente por año.
- Los archivos que no cumplen el formato son descartados sin errores.
- Si el directorio no existe o está vacío, se muestra un mensaje informativo.

---

## Sistema de tipos extensible

La página acepta **cualquier tipo de objeto** sin requerir cambios en el código. La asignación de color y nombre visible funciona en dos capas:

### Capa 1: Tipos conocidos

En el frontmatter hay dos diccionarios pre-poblados con los tipos comunes:

```typescript
const KNOWN_TYPE_COLORS: Record<string, string> = {
  neo:       '#003D79',  // azul institucional
  leo:       '#1b6e4e',  // verde oscuro
  bolido:    '#b45309',  // ámbar
  asteroide: '#7c3aed',  // violeta
  cometa:    '#0891b2',  // cyan
  meteoro:   '#dc2626',  // rojo
  meteorito: '#dc2626',
  satelite:  '#475569',  // pizarra
  basura:    '#525252',
};

const KNOWN_TYPE_DISPLAY: Record<string, string> = {
  bolido:    'Bólido',
  asteroide: 'Asteroide',
  cometa:    'Cometa',
  satelite:  'Satélite',
  basura:    'Basura espacial',
  // ...
};
```

> Las **claves se comparan en minúsculas**, así que `Bolido`, `bolido` o `BOLIDO` funcionan igual.

### Capa 2: Tipos nuevos (fallback automático)

Si el tipo no está en `KNOWN_TYPE_COLORS`, se asigna un color **determinístico** a partir del hash del nombre, eligiendo de una paleta extendida:

```typescript
const FALLBACK_PALETTE = [
  '#7c3aed', '#0891b2', '#dc2626', '#0d9488', '#d97706',
  '#5b21b6', '#0e7490', '#9f1239', '#115e59', '#92400e',
];
```

El nombre visible se genera capitalizando la primera letra (o conservando si ya es acrónimo en mayúsculas).

### Cómo agregar un tipo conocido (opcional)

Para que un tipo nuevo aparezca con un color y nombre específicos:

1. Edita `src/pages/investigacion/neos-leos.astro`.
2. Agrega una entrada a `KNOWN_TYPE_COLORS` con la clave en minúsculas:
   ```typescript
   bolido: '#b45309',
   ```
3. (Opcional) Agrega también una entrada a `KNOWN_TYPE_DISPLAY` si el nombre lleva tilde o forma especial:
   ```typescript
   bolido: 'Bólido',
   ```

> Si simplemente colocas el PDF sin tocar el código, el sistema funcionará perfectamente con un color asignado automáticamente.

### Leyenda dinámica

La leyenda en la parte superior de la línea del tiempo se construye automáticamente a partir de los tipos presentes en los archivos detectados, ordenados alfabéticamente.

---

## Estructura de la página

```
<Layout>
  <section.neos-header>         ← Encabezado azul institucional con acento dorado
  <section.neos-intro>          ← Texto justificado del proyecto DAEDALUS
  <section.timeline-section>    ← Línea del tiempo
    <div.timeline-heading>      ← Título "Registro de eventos" + leyenda dinámica
    <div.timeline>
      <div.year-group>          ← Un grupo por año (descendente)
        <div.year-sep>          ← Separador con año en tipografía display dorada
        <article.entry>         ← Una entrada por reporte
          <time.entry__date>    ← Día grande + mes abreviado
          <div.entry__body>     ← Tipo (con borde inferior de color) + nombre + fecha
          <a.entry__pdf-btn>    ← Botón outline "Ver PDF" con icono
```

Cada `.entry` recibe la variable CSS `--type-color` inline, que aplica el color del tipo al borde del badge, al borde del botón y al estado hover.

---

## Responsividad

| Breakpoint | Comportamiento |
|-----------|---------------|
| `> 900px` | Layout en 3 columnas: fecha · contenido · botón PDF |
| `≤ 900px` | Botón PDF baja debajo del contenido (grid 2 columnas) |
| `≤ 768px` | Texto del intro pasa a alineación izquierda (mejor lectura sin justificar) |
| `≤ 540px` | Tipografía reducida y espaciado compacto; leyenda envuelve a múltiples líneas |

---

## Menú de navegación

El ítem está ubicado en `src/components/Header.astro`, dentro del submenú de **Investigación**, entre *Modelo sunRunner3D* y *Publicaciones*:

```typescript
{ label: 'NEOs y LEOs', href: '/investigacion/neos-leos' },
```

---

## Próximos pasos

- [02-ESTRUCTURA-DEL-PROYECTO.md](./02-ESTRUCTURA-DEL-PROYECTO.md) — Estructura general del sitio
- [07-ESTILOS-Y-DISENO.md](./07-ESTILOS-Y-DISENO.md) — Variables CSS y sistema de diseño
