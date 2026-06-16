# 12. Galería de Eventos (EventGallery)

Documentación del componente `EventGallery.astro` — carrusel de imágenes para eventos con visor lightbox.

---

## Índice

1. [Uso básico](#uso-básico)
2. [Props disponibles](#props-disponibles)
3. [Uso en artículos de divulgación](#uso-en-artículos-de-divulgación)
4. [Uso en páginas Astro](#uso-en-páginas-astro)
5. [Múltiples galerías en una misma página](#múltiples-galerías-en-una-misma-página)
6. [Cómo agregar imágenes](#cómo-agregar-imágenes)
7. [Comportamiento del carrusel](#comportamiento-del-carrusel)
8. [Visor Lightbox](#visor-lightbox)

---

## Uso básico

Coloca las imágenes en una subcarpeta dentro de `public/` y pasa esa ruta al componente:

```astro
---
import EventGallery from '../components/EventGallery.astro';
---

<EventGallery folderPath="/practica-GTM-2026" />
```

El componente lee automáticamente los archivos de esa carpeta en tiempo de build. No es necesario listar las imágenes manualmente.

---

## Props disponibles

| Prop | Tipo | Requerido | Valor por defecto | Descripción |
|------|------|-----------|-------------------|-------------|
| `folderPath` | `string` | **Sí** | — | Ruta a la carpeta de imágenes, relativa a `public/`. Debe empezar con `/`. |
| `titulo` | `string` | No | `"Galería de imágenes"` | Título que aparece sobre el carrusel. |

### Ejemplo completo

```astro
<EventGallery
  folderPath="/eventos/congreso-2026"
  titulo="Congreso Internacional 2026"
/>
```

---

## Uso en artículos de divulgación

Los artículos en `src/content/divulgacion/` son archivos `.md`. No pueden importar componentes directamente. En su lugar, se configura la galería desde el **frontmatter** y el sistema la renderiza automáticamente al final del artículo.

### Paso 1 — Agregar la galería al frontmatter

```yaml
---
titulo: "Nombre del Evento"
descripcion: "Descripción del evento..."
autor: "Dr. Nombre Apellido"
fecha: 2026-06-16
imagen: "/eventos/nombre-evento/portada.jpg"
etiquetas: ["astronomía", "eventos"]
galeria:
  ruta: "/eventos/nombre-evento/fotos"
  titulo: "Galería del Evento"
---
```

El campo `galeria` tiene dos subclaves:
- `ruta` — ruta a la carpeta de imágenes (igual que `folderPath` en el componente)
- `titulo` — título que aparece sobre el carrusel

### Paso 2 — Agregar las imágenes

Crea la carpeta indicada en `ruta` dentro de `public/` y copia las imágenes ahí:

```
public/
└── eventos/
    └── nombre-evento/
        └── fotos/
            ├── 1.jpeg
            ├── 2.jpeg
            └── ...
```

Listo. El sistema detecta el campo `galeria` automáticamente y renderiza el carrusel.

---

## Uso en páginas Astro

En cualquier archivo `.astro`, importa el componente y úsalo con la ruta de la carpeta:

```astro
---
import Layout from '../../layouts/Layout.astro';
import EventGallery from '../../components/EventGallery.astro';
---

<Layout title="Mi página">
  <h1>Evento especial</h1>
  <p>Descripción del evento...</p>

  <EventGallery
    folderPath="/eventos/nombre-evento/fotos"
    titulo="Fotos del evento"
  />
</Layout>
```

### Ruta de la carpeta

`folderPath` es la ruta **web** relativa a `public/`. Si tus imágenes están en `public/practica-GTM-2026/`, el valor es `/practica-GTM-2026`.

```
public/practica-GTM-2026/   →   folderPath="/practica-GTM-2026"
public/TTP2026/imagenes/    →   folderPath="/TTP2026/imagenes"
public/eventos/fotos/       →   folderPath="/eventos/fotos"
```

---

## Múltiples galerías en una misma página

El componente soporta varias instancias independientes en la misma página. Cada galería tiene su propio carrusel, autoplay y lightbox sin interferencias:

```astro
<EventGallery
  folderPath="/eventos/dia-1"
  titulo="Día 1 — Conferencias"
/>

<EventGallery
  folderPath="/eventos/dia-2"
  titulo="Día 2 — Prácticas"
/>
```

---

## Cómo agregar imágenes

### Formatos soportados

`.jpg` · `.jpeg` · `.png` · `.gif` · `.webp` · `.avif` · `.svg` · `.bmp`

### Estructura de carpeta recomendada

```
public/
└── nombre-evento/
    ├── 1.jpeg
    ├── 2.jpeg
    ├── 3.jpeg
    └── ...
```

### Nombres de archivo

El componente ordena las imágenes **alfabéticamente** (con ordenación natural: `1, 2, 10` en lugar de `1, 10, 2`). Para controlar el orden usa nombres numéricos (`1.jpeg`, `2.jpeg`, ...) o prefijos con ceros (`001.jpg`, `002.jpg`, ...).

### Recomendaciones de tamaño

| Característica | Recomendación |
|----------------|---------------|
| Formato | JPEG para fotos |
| Ancho máximo | 1 920 px |
| Peso máximo | 300 KB por imagen |
| Optimización | Usar `sharp` o Squoosh antes de subir |

---

## Comportamiento del carrusel

### Columnas por dispositivo

| Dispositivo | Columnas | Ancho de pantalla |
|-------------|----------|--------------------|
| Desktop | 3 imágenes | ≥ 1 024 px |
| Tablet | 2 imágenes | 640 – 1 023 px |
| Móvil | 1 imagen | < 640 px |

### Autoplay

- Avanza automáticamente cada **4 segundos**.
- Se pausa al pasar el cursor sobre el carrusel.
- Se pausa al enfocar con teclado (accesibilidad).
- Se pausa cuando la pestaña queda en segundo plano.
- Se respeta `prefers-reduced-motion`: si el usuario tiene activada la opción de reducir movimiento, el autoplay no arranca.

### Controles

| Control | Acción |
|---------|--------|
| Botones `‹` `›` | Página anterior / siguiente |
| Puntos indicadores | Saltar a una página específica |
| Botón ▶/⏸ | Pausar o reanudar el autoplay |
| Teclas `←` `→` | Navegar (cuando el carrusel está enfocado) |
| Swipe | Deslizar en pantallas táctiles |

---

## Visor Lightbox

Al hacer clic en cualquier imagen del carrusel se abre el visor a pantalla completa.

### Cómo cerrar

| Método | Descripción |
|--------|-------------|
| Botón `✕` | Esquina superior derecha |
| Clic fuera | Clic en el área oscura fuera de la imagen |
| Tecla `Esc` | Teclado |

### Navegación en el lightbox

| Acción | Método |
|--------|--------|
| Imagen anterior | Botón `‹`, tecla `←`, o swipe hacia la derecha |
| Imagen siguiente | Botón `›`, tecla `→`, o swipe hacia la izquierda |
| Contador | Indica posición actual: `3 / 22` |

> **Nota:** La navegación del lightbox es **imagen por imagen**, mientras que el carrusel navega por **páginas** (grupos de 2–3 imágenes).
