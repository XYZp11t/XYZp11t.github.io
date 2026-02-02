# 08. Configuración

Guía de configuración del proyecto Astro, TypeScript y opciones de build.

---

## Índice

1. [astro.config.mjs](#astroconfigmjs)
2. [content.config.ts](#contentconfigts)
3. [tsconfig.json](#tsconfigjson)
4. [package.json](#packagejson)
5. [Configuración de Build](#configuración-de-build)
6. [Variables de Entorno](#variables-de-entorno)

---

## astro.config.mjs

**Ubicación:** `astro.config.mjs`

Archivo principal de configuración de Astro.

### Configuración Actual

```javascript
// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://xyzp11t.github.io',
  base: '/'
});
```

### Opciones Disponibles

| Opción | Valor Actual | Descripción |
|--------|--------------|-------------|
| `site` | `https://xyzp11t.github.io` | URL base del sitio (para SEO y sitemap) |
| `base` | `/` | Ruta base del sitio |

### Cambiar el Dominio

Para cambiar la URL del sitio (ej: al mover a producción):

```javascript
export default defineConfig({
  site: 'https://lacige.unam.mx',
  base: '/'
});
```

### Subdirectorio

Si el sitio se aloja en un subdirectorio:

```javascript
export default defineConfig({
  site: 'https://enes.unam.mx',
  base: '/lacige'
});
```

Esto hará que las URLs sean: `https://enes.unam.mx/lacige/`

---

## content.config.ts

**Ubicación:** `src/content.config.ts`

Define las colecciones de contenido y sus esquemas de validación.

### Estructura

```typescript
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Colección de artículos de divulgación
const divulgacion = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/divulgacion" }),
  schema: z.object({
    titulo: z.string(),
    descripcion: z.string(),
    autor: z.string(),
    fecha: z.date(),
    imagen: z.string().optional(),
    etiquetas: z.array(z.string()).default([]),
    destacado: z.boolean().default(false),
  }),
});

// Colección de publicaciones científicas
const publicaciones = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/publicaciones" }),
  schema: z.object({
    titulo: z.string(),
    autores: z.array(z.string()),
    revista: z.string().optional(),
    anio: z.number(),
    doi: z.string().optional(),
    resumen: z.string(),
    tipo: z.enum(['articulo', 'tesis']),
    categoria: z.enum(['produccion', 'previa']).optional(),
    enlace: z.string().optional(),
    institucion: z.string().optional(),
    director: z.string().optional(),
    directorInstitucion: z.string().optional(),
  }),
});

export const collections = { divulgacion, publicaciones };
```

### Tipos de Datos (Zod)

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| `z.string()` | Cadena de texto | `"Título"` |
| `z.number()` | Número | `2024` |
| `z.date()` | Fecha | `2024-01-15` |
| `z.boolean()` | Booleano | `true` / `false` |
| `z.array(z.string())` | Array de strings | `["tag1", "tag2"]` |
| `z.enum(['a', 'b'])` | Uno de los valores | `'articulo'` o `'tesis'` |
| `.optional()` | Campo opcional | Puede omitirse |
| `.default(valor)` | Valor por defecto | `[]` o `false` |

### Agregar una Nueva Colección

Para crear una nueva colección (ej: "noticias"):

```typescript
const noticias = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/noticias" }),
  schema: z.object({
    titulo: z.string(),
    fecha: z.date(),
    resumen: z.string(),
    imagen: z.string().optional(),
  }),
});

export const collections = { divulgacion, publicaciones, noticias };
```

Luego crear la carpeta: `src/content/noticias/`

---

## tsconfig.json

**Ubicación:** `tsconfig.json`

Configuración de TypeScript.

### Configuración Actual

```json
{
  "extends": "astro/tsconfigs/strict",
  "include": [".astro/types.d.ts", "**/*"],
  "exclude": ["dist"]
}
```

### Opciones

- **`extends: "astro/tsconfigs/strict"`** - Usa la configuración estricta de Astro
- **`include`** - Archivos a incluir en la compilación
- **`exclude`** - Archivos a excluir

### Modificar Configuración

Para agregar opciones personalizadas:

```json
{
  "extends": "astro/tsconfigs/strict",
  "include": [".astro/types.d.ts", "**/*"],
  "exclude": ["dist"],
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true
  }
}
```

---

## package.json

**Ubicación:** `package.json`

Define dependencias y scripts del proyecto.

### Configuración Actual

```json
{
  "name": "",
  "type": "module",
  "version": "0.0.1",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "astro": "^5.17.1"
  }
}
```

### Scripts Disponibles

| Script | Comando | Descripción |
|--------|---------|-------------|
| `dev` | `astro dev` | Servidor de desarrollo |
| `build` | `astro build` | Compilar para producción |
| `preview` | `astro preview` | Previsualizar build |
| `astro` | `astro` | CLI de Astro |

### Dependencias

| Paquete | Versión | Descripción |
|---------|---------|-------------|
| `astro` | `^5.17.1` | Framework principal |

### Agregar Dependencias

```bash
# Dependencia de producción
npm install nombre-paquete

# Dependencia de desarrollo
npm install -D nombre-paquete
```

### Ejemplo: Agregar un Plugin

```bash
npm install @astrojs/sitemap
```

```json
{
  "dependencies": {
    "astro": "^5.17.1",
    "@astrojs/sitemap": "^3.0.0"
  }
}
```

---

## Configuración de Build

### Build de Desarrollo

```bash
npm run dev
```

- URL: `http://localhost:4321`
- Hot reload activado
- Source maps disponibles

### Build de Producción

```bash
npm run build
```

Genera los archivos en `dist/`:

```
dist/
├── index.html
├── divulgacion/
├── investigacion/
├── sobre-nosotros/
├── _astro/           # Assets procesados (CSS, JS)
└── imagen-solar-diaria/  # Copiado de public/
```

### Previsualizar Producción

```bash
npm run preview
```

- Usa los archivos de `dist/`
- Simula el comportamiento en producción
- Útil para verificar antes de deploy

---

## Variables de Entorno

### Archivo .env

Crear `.env` en la raíz (no se sube a git):

```bash
# .env
PUBLIC_API_URL=https://api.ejemplo.com
PUBLIC_SITE_NAME=LACIGE
```

Variables con prefijo `PUBLIC_` están disponibles en el cliente.

### Uso en Astro

```astro
---
// Frontmatter (servidor)
const apiUrl = import.meta.env.PUBLIC_API_URL;
---

<!-- En template -->
<p>API: {import.meta.env.PUBLIC_API_URL}</p>

<!-- En script -->
<script>
  console.log(import.meta.env.PUBLIC_API_URL);
</script>
```

### .gitignore

El archivo `.env` ya está incluido en `.gitignore`:

```gitignore
# environment variables
.env
.env.production
```

---

## Configuración de Git

### .gitignore

```gitignore
# build output
dist/

# generated types
.astro/

# dependencies
node_modules/

# logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# environment variables
.env
.env.production

# macOS-specific files
.DS_Store
```

### Configuración de Usuario

```bash
git config user.name "Tu Nombre"
git config user.email "tu@email.com"
```

---

## Optimizaciones de Build

### Compresión de Imágenes

Astro no comprime imágenes automáticamente. Recomendaciones:

1. **Optimizar antes de subir:**
   - JPG para fotos (calidad 80-85%)
   - PNG para gráficos
   - Tamaño máximo: 1920px de ancho

2. **Herramientas:**
   - TinyPNG (web)
   - ImageOptim (Mac)
   - Squoosh (web)

### Minificación

Astro minifica automáticamente:
- CSS
- JavaScript
- HTML

### Code Splitting

Astro genera automáticamente:
- Un bundle por página
- CSS crítico inline
- Preloading de recursos

---

## Despliegue (Deployment)

### GitHub Pages

1. Configurar `astro.config.mjs`:

```javascript
export default defineConfig({
  site: 'https://tusuario.github.io',
  base: '/nombre-repo'
});
```

2. Crear workflow `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: withastro/action@v1
      - uses: actions/deploy-pages@v1
```

### Netlify

1. Conectar repositorio en Netlify
2. Configurar build:
   - Build command: `npm run build`
   - Publish directory: `dist`

### Vercel

1. Importar proyecto en Vercel
2. Framework preset: Astro
3. Build se configura automáticamente

---

## Solución de Problemas

### Error: "Cannot find module"

```bash
# Limpiar caché
rm -rf node_modules package-lock.json
npm install
```

### Error: "Port already in use"

```bash
# Usar otro puerto
npm run dev -- --port 3000
```

### Build falla

```bash
# Limpiar y reconstruir
rm -rf dist .astro
npm run build
```

### Tipos de TypeScript no encontrados

```bash
# Reiniciar servidor de TypeScript
npx astro sync
```

---

## Actualizaciones

### Actualizar Astro

```bash
# Ver versiones disponibles
npm outdated

# Actualizar Astro
npm install astro@latest

# Actualizar todas las dependencias
npm update
```

### Verificar Breaking Changes

Antes de actualizar:

1. Revisar: https://docs.astro.build/en/upgrade/
2. Leer el changelog
3. Probar en ambiente de desarrollo
4. Hacer backup antes de actualizar

---

## Próximos Pasos

- [01-INSTALACION-Y-SETUP.md](./01-INSTALACION-Y-SETUP.md) - Revisar instalación
- [02-ESTRUCTURA-DEL-PROYECTO.md](./02-ESTRUCTURA-DEL-PROYECTO.md) - Entender estructura
