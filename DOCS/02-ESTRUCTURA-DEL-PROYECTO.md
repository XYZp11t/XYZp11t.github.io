# 02. Estructura del Proyecto

Esta guía explica la organización de archivos y carpetas del sitio web LACIGE.

---

## Vista General

```
web_lacige/
├── public/                    # Archivos estáticos accesibles públicamente
├── src/
│   ├── assets/               # Recursos internos (imágenes, fuentes)
│   ├── components/           # Componentes reutilizables
│   ├── content/              # Contenido en Markdown
│   │   ├── colaboradores/   # Investigadores (internos y externos)
│   │   │   ├── grupos/      # Instituciones/Grupos
│   │   │   ├── internos/    # Colaboradores internos (LACIGE)
│   │   │   └── externos/    # Colaboradores externos
│   │   ├── divulgacion/     # Artículos de divulgación
│   │   └── publicaciones/   # Publicaciones científicas
│   ├── layouts/              # Layouts de página
│   ├── pages/                # Rutas del sitio
│   └── styles/               # CSS global
├── DOCS/                     # Documentación
├── astro.config.mjs          # Configuración de Astro
├── content.config.ts         # Configuración de colecciones
├── package.json              # Dependencias
└── tsconfig.json             # Configuración TypeScript
```

---

## Carpeta `public/`

Contiene archivos estáticos que se copian directamente al build:

```
public/
├── favicon.svg               # Icono del sitio
├── LOGO_BLANCO_NOBG.svg     # Logo LACIGE blanco
├── LACIGE_LOGO_NEGRO_VECT.svg # Logo LACIGE negro
├── LETRAS_BG_NEGRO.svg      # Letras del logo
├── imagen-solar-diaria/     # Imágenes solares (formato: DD-MM-AAAA.jpg)
│   ├── 16-01-2026.jpg
│   ├── 15-01-2026.jpg
│   └── ...
└── transito-mercurio/       # Imágenes de artículos
    ├── mercurio.jpg
    └── etapas.png
```

**Nota:** Las imágenes solares deben seguir el formato `DD-MM-AAAA.jpg` para ser reconocidas automáticamente.

---

## Carpeta `src/components/`

Componentes reutilizables que pueden usarse en múltiples páginas:

| Componente | Descripción | Uso |
|------------|-------------|-----|
| `Header.astro` | Menú de navegación superior | Todas las páginas |
| `Footer.astro` | Pie de página | Todas las páginas |
| `Layout.astro` | Layout base con SEO | Todas las páginas |
| `Hero.astro` | Banner principal con título | Páginas de inicio |
| `PageHeader.astro` | Encabezado de página simple | Páginas internas |
| `SectionHeader.astro` | Título de sección | Secciones de contenido |
| `ArticleCard.astro` | Tarjeta de artículo | Listados de divulgación |
| `FeatureCard.astro` | Tarjeta con icono | Áreas de investigación |
| `SolarImageViewer.astro` | Visor de imágenes solares | Inicio y Galería Solar |

---

## Carpeta `src/content/`

Contenido en formato Markdown organizado en colecciones:

### `src/content/colaboradores/`

Gestión de investigadores y colaboradores del LACIGE:

```
colaboradores/
├── grupos/                    # Instituciones/Grupos de investigación
│   ├── academicos.md         # Académicos LACIGE
│   ├── posdoctorantes.md     # Posdoctorantes
│   ├── igum.md               # Instituto de Geofísica U. Michoacán
│   ├── irya.md               # Instituto de Radioastronomía y Astrofísica
│   └── ...
├── internos/                  # Colaboradores internos (LACIGE)
│   ├── dr-mario-rodriguez-martinez.md
│   ├── dr-sinhue-haro-corzo.md
│   └── ...
├── externos/                  # Colaboradores externos
│   ├── dr-americo-gonzalez-esparza.md
│   └── ...
├── README.md                  # Documentación rápida
└── TEMPLATE.md                # Template base
```

**Ver también:** [09-COLABORADORES.md](./09-COLABORADORES.md) para gestión detallada.

### `src/content/divulgacion/`

Artículos de divulgación científica. Cada archivo `.md` representa un artículo.

**Ejemplo:**
```
divulgacion/
├── transito-de-mercurio.md
├── eclipse-parcial-08-04-2024.md
└── eclipse-parcial-de-sol-21082017.md
```

### `src/content/publicaciones/`

Publicaciones científicas (artículos y tesis):

```
publicaciones/
├── articulo-ionospheric-disturbances-mexart-2012.md
├── articulo-radio-signal-anomalies-2016.md
└── tesis-magnetosfera.md
```

---

## Carpeta `src/layouts/`

Layouts que definen la estructura base de las páginas:

### `Layout.astro`

Layout principal que incluye:
- `<head>` con metadatos SEO
- `<Header />` componente
- `<main>` para el contenido
- `<Footer />` componente
- Transiciones entre páginas (View Transitions)

**Uso:**
```astro
---
import Layout from '../layouts/Layout.astro';
---
<Layout title="Título de página" description="Descripción">
  <!-- Contenido aquí -->
</Layout>
```

---

## Carpeta `src/pages/`

Define las rutas del sitio siguiendo la convención de Astro:

```
pages/
├── index.astro                    # / (Inicio)
├── contacto.astro                 # /contacto
├── becas.astro                    # /becas
├── colaboradores.astro            # /colaboradores
├── sitios.astro                   # /sitios
├── divulgacion/
│   ├── index.astro               # /divulgacion
│   └── [...slug].astro           # /divulgacion/[articulo]
├── investigacion/
│   ├── index.astro               # /investigacion
│   ├── galeria-solar.astro       # /investigacion/galeria-solar
│   └── prediccion-viento-solar.astro
│   └── publicaciones/
│       ├── index.astro           # /investigacion/publicaciones
│       ├── articulos.astro       # /investigacion/publicaciones/articulos
│       └── tesis.astro           # /investigacion/publicaciones/tesis
└── sobre-nosotros/
    ├── index.astro               # /sobre-nosotros
    ├── historia.astro            # /sobre-nosotros/historia
    └── infraestructura.astro     # /sobre-nosotros/infraestructura
```

### Rutas Dinámicas

- `[...slug].astro` - Genera páginas para cada artículo de divulgación
- Astro crea automáticamente las rutas basándose en los archivos Markdown

---

## Carpeta `src/styles/`

Estilos CSS globales:

| Archivo | Descripción |
|---------|-------------|
| `global.css` | Estilos base, variables CSS, utilidades |
| `article.css` | Estilos específicos para artículos de divulgación |

### Variables CSS Principales (en `global.css`)

```css
:root {
  /* Colores */
  --color-primary: #003D79;      /* Azul institucional */
  --color-accent: #D59F0F;       /* Dorado */
  --color-earth: #84754E;        /* Tierra */
  
  /* Tipografía */
  --font-display: 'Playfair Display', serif;
  --font-body: 'Source Sans 3', sans-serif;
  
  /* Espaciado */
  --space-xs: 0.25rem;   /* 4px */
  --space-sm: 0.5rem;    /* 8px */
  --space-md: 1rem;      /* 16px */
  --space-lg: 1.5rem;    /* 24px */
  --space-xl: 2rem;      /* 32px */
}
```

---

## Archivos de Configuración

### `astro.config.mjs`

Configuración principal de Astro:

```javascript
export default defineConfig({
  site: 'https://xyzp11t.github.io',  // URL del sitio
  base: '/'                           // Base path
});
```

### `content.config.ts`

Define las colecciones de contenido y sus esquemas:

- Colección `divulgacion` - Artículos de divulgación
- Colección `publicaciones` - Publicaciones científicas
- Colección `colaboradoresInternos` - Investigadores del LACIGE
- Colección `colaboradoresExternos` - Colaboradores de otras instituciones
- Colección `gruposColaboradores` - Instituciones y grupos de investigación

### `package.json`

Dependencias y scripts:

```json
{
  "dependencies": {
    "astro": "^5.17.1"
  },
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  }
}
```

---

## Convenciones de Nombres

### Archivos
- **Componentes:** `PascalCase.astro` (ej: `ArticleCard.astro`)
- **Páginas:** `kebab-case.astro` (ej: `galeria-solar.astro`)
- **Estilos:** `kebab-case.css` (ej: `global.css`)
- **Contenido:** `kebab-case.md` (ej: `transito-de-mercurio.md`)

### Imágenes
- **Logo:** `LACIGE_LOGO_NEGRO_VECT.svg`
- **Imágenes solares:** `DD-MM-AAAA.jpg` (ej: `16-01-2026.jpg`)
- **Imágenes de artículos:** En carpeta específica por artículo

---

## Flujo de Datos

1. **Contenido Markdown** → Procesado por Astro → **HTML estático**
2. **Componentes Astro** → Renderizados en build → **HTML + CSS + JS**
3. **Imágenes en public/** → Copiadas directamente → **Build final**

---

## Próximos Pasos

- [03-COMPONENTES.md](./03-COMPONENTES.md) - Documentación detallada de componentes
- [04-ARTICULOS-DIVULGACION.md](./04-ARTICULOS-DIVULGACION.md) - Crear artículos
- [05-PUBLICACIONES-CIENTIFICAS.md](./05-PUBLICACIONES-CIENTIFICAS.md) - Agregar publicaciones
- [09-COLABORADORES.md](./09-COLABORADORES.md) - Gestionar colaboradores
