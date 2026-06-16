# 03. Componentes

Documentación detallada de todos los componentes reutilizables del sitio LACIGE.

---

## Índice de Componentes

1. [Layout](#layoutastro) - Layout base
2. [Header](#headerastro) - Navegación superior
3. [Footer](#footerastro) - Pie de página
4. [Hero](#heroastro) - Banner principal
5. [PageHeader](#pageheaderastro) - Encabezado de página
6. [SectionHeader](#sectionheaderastro) - Título de sección
7. [ArticleCard](#articlecardastro) - Tarjeta de artículo
8. [FeatureCard](#featurecardastro) - Tarjeta con icono
9. [SolarImageViewer](#solarimageviewerastro) - Visor de imágenes solares
10. [EventGallery](#eventgalleryastro) - Carrusel de imágenes de eventos

---

## Layout.astro

**Ubicación:** `src/layouts/Layout.astro`

Layout base que envuelve todas las páginas del sitio.

### Props

| Propiedad | Tipo | Requerido | Default | Descripción |
|-----------|------|-----------|---------|-------------|
| `title` | `string` | No | "LACIGE - Laboratorio..." | Título de la página (SEO) |
| `description` | `string` | No | Descripción por defecto | Meta descripción (SEO) |
| `image` | `string` | No | `/favicon.svg` | Imagen para Open Graph |

### Uso

```astro
---
import Layout from '../layouts/Layout.astro';
---

<Layout 
  title="Divulgación | LACIGE"
  description="Artículos de divulgación científica"
  image="/imagen-destacada.jpg"
>
  <h1>Contenido de la página</h1>
</Layout>
```

### Características

- Incluye metadatos SEO (title, description, Open Graph)
- Carga fuentes de Google Fonts
- Implementa View Transitions para navegación suave
- Incluye Header y Footer automáticamente
- Precarga imágenes y enlaces para mejor rendimiento

---

## Header.astro

**Ubicación:** `src/components/Header.astro`

Menú de navegación principal con soporte para dropdowns.

### Props

*No tiene props.* El menú se configura dentro del archivo.

### Configuración del Menú

Para modificar el menú, edita el array `menuItems` en el frontmatter:

```astro
const menuItems = [
  { label: 'Inicio', href: '/' },
  { 
    label: 'Investigación', 
    href: '/investigacion',
    children: [
      { label: 'Galería Solar', href: '/investigacion/galeria-solar' },
      { label: 'Publicaciones', href: '/investigacion/publicaciones' }
    ]
  },
  // ... más items
];
```

### Características

- **Menú responsive:** Se convierte en hamburguesa en móviles
- **Dropdowns:** Soporta submenús de dos niveles
- **Indicador activo:** Resalta la página actual
- **Sticky:** Se mantiene fijo al hacer scroll

---

## Footer.astro

**Ubicación:** `src/components/Footer.astro`

Pie de página con información de contacto y enlaces.

### Props

*No tiene props.*

### Estructura

```
Footer/
├── Logo y descripción del LACIGE
├── Enlaces Rápidos
├── Enlaces de Investigación
├── Enlaces Institucionales
└── Información de Contacto
    ├── Dirección
├── Email
└── Teléfono
```

### Personalización

Para modificar los enlaces, edita estos arrays en el frontmatter:

```astro
const quickLinks = [
  { label: 'Inicio', href: '/' },
  { label: 'Divulgación', href: '/divulgacion' }
];

const researchLinks = [
  { label: 'Galería Solar', href: '/investigacion/galeria-solar' }
];
```

Para actualizar la información de contacto, busca la sección `<address>` en el template.

---

## Hero.astro

**Ubicación:** `src/components/Hero.astro`

Banner principal grande para páginas de inicio.

### Props

| Propiedad | Tipo | Requerido | Default | Descripción |
|-----------|------|-----------|---------|-------------|
| `titulo` | `string` | Sí | - | Título principal |
| `subtitulo` | `string` | No | - | Texto pequeño superior |
| `descripcion` | `string` | No | - | Párrafo descriptivo |
| `imagen` | `string` | No | - | URL de imagen de fondo |
| `ctaPrimario` | `object` | No | - | Botón principal `{ texto, enlace }` |
| `ctaSecundario` | `object` | No | - | Botón secundario `{ texto, enlace }` |
| `overlay` | `boolean` | No | `true` | Mostrar degradado oscuro |
| `centrado` | `boolean` | No | `true` | Centrar contenido |
| `altura` | `string` | No | `'large'` | Altura: 'full', 'large', 'medium', 'small' |

### Uso

```astro
<Hero 
  titulo="Laboratorio de Ciencias Geoespaciales"
  subtitulo="Bienvenidos al LACIGE"
  descripcion="Investigación en física solar y clima espacial"
  imagen="/imagen-fondo.jpg"
  ctaPrimario={{ texto: "Conocer más", enlace: "/sobre-nosotros" }}
  ctaSecundario={{ texto: "Contacto", enlace: "/contacto" }}
  altura="large"
/>
```

### Características

- Animación de partículas flotantes
- Animaciones de entrada (fadeInUp)
- Indicador scroll-down animado
- Gradiente overlay configurable

---

## PageHeader.astro

**Ubicación:** `src/components/PageHeader.astro`

Encabezado simple para páginas internas (no inicio).

### Props

| Propiedad | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `titulo` | `string` | Sí | Título de la página |
| `subtitulo` | `string` | No | Etiqueta pequeña superior |

### Uso

```astro
<PageHeader 
  titulo="Divulgación Científica"
  subtitulo="Compartiendo Conocimiento"
/>
```

### Características

- Fondo azul institucional
- Diseño compacto
- Responsive

---

## SectionHeader.astro

**Ubicación:** `src/components/SectionHeader.astro`

Título de sección con línea decorativa.

### Props

| Propiedad | Tipo | Requerido | Default | Descripción |
|-----------|------|-----------|---------|-------------|
| `titulo` | `string` | Sí | - | Título de la sección |
| `subtitulo` | `string` | No | - | Texto pequeño superior |
| `descripcion` | `string` | No | - | Párrafo descriptivo |
| `centrado` | `boolean` | No | `true` | Centrar contenido |
| `claro` | `boolean` | No | `false` | Colores claros (para fondos oscuros) |

### Uso

```astro
<SectionHeader 
  subtitulo="Investigación"
  titulo="Áreas de Estudio"
  descripcion="Nuestro laboratorio se especializa en..."
  centrado={true}
/>
```

---

## ArticleCard.astro

**Ubicación:** `src/components/ArticleCard.astro`

Tarjeta para mostrar artículos de divulgación.

### Props

| Propiedad | Tipo | Requerido | Default | Descripción |
|-----------|------|-----------|---------|-------------|
| `titulo` | `string` | Sí | - | Título del artículo |
| `descripcion` | `string` | Sí | - | Descripción corta |
| `fecha` | `Date` | Sí | - | Fecha de publicación |
| `autor` | `string` | Sí | - | Nombre del autor |
| `imagen` | `string` | No | - | URL de imagen |
| `etiquetas` | `string[]` | No | `[]` | Array de etiquetas |
| `enlace` | `string` | Sí | - | URL del artículo |
| `destacado` | `boolean` | No | `false` | Estilo destacado (más grande) |

### Uso

```astro
<ArticleCard 
  titulo="Tránsito de Mercurio"
  descripcion="Guía completa sobre el fenómeno astronómico..."
  fecha={new Date('2024-01-15')}
  autor="Dr. Mario Rodríguez"
  imagen="/transito-mercurio/mercurio.jpg"
  etiquetas=["astronomía", "eventos"]
  enlace="/divulgacion/transito-de-mercurio"
  destacado={false}
/>
```

### Características

- Placeholder automático si no hay imagen
- Badge "Destacado" opcional
- Máximo 2 etiquetas visibles
- Efecto hover con elevación
- Animación de imagen al hacer hover

---

## FeatureCard.astro

**Ubicación:** `src/components/FeatureCard.astro`

Tarjeta con icono para áreas de investigación.

### Props

| Propiedad | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `titulo` | `string` | Sí | Título de la tarjeta |
| `descripcion` | `string` | Sí | Descripción |
| `icono` | `string` | Sí | Nombre del icono (ver lista abajo) |
| `enlace` | `string` | No | URL si es clickeable |

### Iconos Disponibles

| Icono | Descripción |
|-------|-------------|
| `sol` | Sol/estrella |
| `viento` | Viento/líneas |
| `publicacion` | Documento/papel |
| `divulgacion` | Burbuja de chat |
| `equipo` | Grupo de personas |
| `beca` | Gorro de graduación |
| `infraestructura` | Edificio |
| `historia` | Reloj |
| `contacto` | Sobre/email |
| `sitios` | Globo terráqueo |

### Uso

```astro
<FeatureCard 
  titulo="Galería Solar"
  descripcion="Observación y registro visual..."
  icono="sol"
  enlace="/investigacion/galeria-solar"
/>
```

---

## SolarImageViewer.astro

**Ubicación:** `src/components/SolarImageViewer.astro`

Visor modal interactivo para imágenes solares.

### Props

| Propiedad | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `imagenes` | `Array` | Sí | Array de objetos con `{ path, fechaStr, id }` |

### Formato de Datos

```typescript
interface ImageData {
  path: string;      // Ruta de la imagen: "/imagen-solar-diaria/16-01-2026.jpg"
  fechaStr: string;  // Fecha formateada: "16/01/2026"
  id: string;        // ID único: "2026-01-16"
}
```

### Uso

```astro
---
const imagenesParaVisor = [
  { path: "/imagen-solar-diaria/16-01-2026.jpg", fechaStr: "16/01/2026", id: "2026-01-16" },
  { path: "/imagen-solar-diaria/15-01-2026.jpg", fechaStr: "15/01/2026", id: "2026-01-15" }
];
---

<SolarImageViewer imagenes={imagenesParaVisor} />
```

### Funcionalidades

- **Navegación:** Flechas izquierda/derecha para cambiar imágenes
- **Zoom:** Botones +, -, y 0 para zoom (también rueda del mouse)
- **Pan:** Arrastrar imagen cuando está con zoom
- **Teclado:** 
  - `ESC` - Cerrar
  - `←` / `→` - Navegar
  - `+` / `-` - Zoom
  - `0` - Resetear zoom
- **Responsive:** Adaptado para móviles con navegación táctil

### Cómo Abrir el Visor

Para abrir el visor desde cualquier elemento, usa el atributo `data-solar-viewer`:

```astro
<button data-solar-viewer="/imagen-solar-diaria/16-01-2026.jpg">
  Ver imagen
</button>
```

---

## EventGallery.astro

**Ubicación:** `src/components/EventGallery.astro`

Carrusel interactivo para mostrar galerías de imágenes de eventos con navegación por páginas, autoplay y visor lightbox.

### Props

| Propiedad | Tipo | Requerido | Default | Descripción |
|-----------|------|-----------|---------|-------------|
| `folderPath` | `string` | Sí | - | Ruta a la carpeta de imágenes (ej: `"/TTP2026/imagenes"`) |
| `titulo` | `string` | No | `"Galería de imágenes"` | Título mostrado sobre el carrusel |

### Uso

```astro
---
import EventGallery from '../components/EventGallery.astro';
---

<EventGallery 
  folderPath="/TTP2026/imagenes"
  titulo="Galería del Evento"
/>
```

### Configuración en Artículos de Divulgación

Para agregar una galería a un artículo de divulgación, añade la configuración `galeria` al frontmatter:

```yaml
---
titulo: "Teacher Training Programme (TTP) 2026"
descripcion: "Resumen del evento..."
autor: "Dr. Mario Rodríguez Martínez"
fecha: 2026-03-24
imagen: "/TTP2026/IAU_SP.png"
etiquetas: ["astronomía", "eventos"]
destacado: true
galeria:
  ruta: "/TTP2026/imagenes"
  titulo: "Galería del Evento TTP 2026"
---
```

El sistema detectará automáticamente la configuración y renderizará el carrusel al final del artículo.

### Funcionamiento del Carrusel

#### Visualización por Página

El carrusel muestra las imágenes en grupos (páginas):

| Dispositivo | Imágenes por página | Ancho de cada imagen |
|-------------|---------------------|----------------------|
| Desktop (≥1024px) | 3 | 33.33% |
| Tablet (640-1023px) | 2 | 50% |
| Móvil (<640px) | 1 | 100% |

Ejemplo: Con 58 imágenes en desktop:
- Página 1: Imágenes 1-3
- Página 2: Imágenes 4-6
- ...
- Página 20: Imágenes 58 (última)

#### Navegación

- **Flechas laterales**: Avanzar/retroceder una página completa
- **Indicadores (dots)**: Saltar directamente a una página específica
- **Swipe táctil**: Deslizar en dispositivos móviles
- **Autoplay**: Cambio automático cada 5 segundos

#### Controles de Reproducción

- **Botón ▶/⏸**: Pausar o reanudar el autoplay
- **Pausa automática**: Se pausa al hacer hover o al abrir el lightbox
- **Reanudación**: Al quitar el mouse, el autoplay se reanuda

### Visor Lightbox

Al hacer clic en cualquier imagen del carrusel, se abre un visor a pantalla completa.

#### Cómo Cerrar el Lightbox

| Método | Descripción |
|--------|-------------|
| **Botón X** | Click en el botón ✕ blanco de la esquina superior derecha (debajo del header) |
| **Click fuera** | Click en cualquier zona oscura fuera de la imagen |
| **Tecla ESC** | Presiona la tecla Escape del teclado |

**Nota sobre el diseño:** El botón X aparece en la esquina superior derecha, debajo de la barra de navegación del sitio para evitar que se solape con ella. La imagen se muestra centrada en la pantalla con márgenes ajustados para no quedar detrás del header.

#### Navegación en el Lightbox

| Acción | Método |
|--------|--------|
| Imagen anterior | Flecha izquierda (←) o swipe derecha en móvil |
| Imagen siguiente | Flecha derecha (→) o swipe izquierda en móvil |
| Contador | Muestra "X / 58" indicando la posición actual |

**Nota:** Click en la imagen itself no cierra el visor, solo navega si hay controles.

#### Navegación en Lightbox vs Carrusel

- **Carrusel**: Navega por **páginas** (grupos de 3 imágenes)
- **Lightbox**: Navega por **imágenes individuales** (una por una)

### Estructura de Carpetas de Imágenes

```
public/
└── TTP2026/
    └── imagenes/
        ├── _DSC4609.jpg
        ├── _DSC4619.jpg
        ├── IMG_2234.JPG
        └── ... (58 imágenes total)
```

### Lista de Imágenes

El componente lee automáticamente los archivos de la carpeta indicada en `folderPath` en tiempo de build. No es necesario listar las imágenes manualmente. Consulta la guía completa en [12-GALERIA-EVENTOS.md](./12-GALERIA-EVENTOS.md).

### Buenas Prácticas

1. **Nombres de archivo**: Usar nombres descriptivos o mantener los originales de la cámara
2. **Formato**: JPG para fotos, máximo 1920px de ancho
3. **Peso**: Optimizar imágenes para web (menos de 500KB ideal)
4. **Cantidad**: El carrusel funciona bien con cualquier cantidad de imágenes (se calculan automáticamente las páginas)

---

## Crear Nuevos Componentes

### Convenciones

1. **Nombre:** PascalCase (ej: `MiComponente.astro`)
2. **Ubicación:** `src/components/`
3. **Estructura:**

```astro
---
// 1. Frontmatter: imports y lógica
interface Props {
  titulo: string;
  descripcion?: string;
}

const { titulo, descripcion = 'Default' } = Astro.props;
---

<!-- 2. Template HTML -->
<div class="mi-componente">
  <h2>{titulo}</h2>
  {descripcion && <p>{descripcion}</p>}
</div>

<!-- 3. Estilos scoped -->
<style>
  .mi-componente {
    padding: var(--space-lg);
  }
</style>

<!-- 4. Scripts (opcional) -->
<script>
  // JavaScript del componente
</script>
```

### Buenas Prácticas

- Usar TypeScript para tipar las props
- Usar variables CSS para colores y espaciado
- Hacer componentes responsivos con media queries
- Documentar props complejas
- Usar `loading="lazy"` en imágenes

---

## Próximos Pasos

- [04-ARTICULOS-DIVULGACION.md](./04-ARTICULOS-DIVULGACION.md) - Crear contenido
- [07-ESTILOS-Y-DISENO.md](./07-ESTILOS-Y-DISENO.md) - Personalizar estilos
