# 01. Instalación y Setup

Esta guía explica cómo instalar el proyecto, ejecutarlo en desarrollo y construirlo para producción.

---

## Requisitos Previos

Antes de comenzar, necesitas tener instalado:

1. **Node.js** versión 18.0 o superior
   - Descargar desde: https://nodejs.org/
   - Verificar instalación: `node --version`

2. **npm** (viene incluido con Node.js)
   - Verificar: `npm --version`

3. **Git** (para clonar el repositorio)
   - Descargar desde: https://git-scm.com/

---

## Instalación del Proyecto

### Paso 1: Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd web_lacige
```

### Paso 2: Instalar Dependencias

```bash
npm install
```

Este comando instalará:
- Astro 5.17.1 (framework principal)
- TypeScript (tipado)
- Otras dependencias necesarias

---

## Comandos Disponibles

### Desarrollo Local

```bash
npm run dev
```

- Inicia un servidor de desarrollo en `http://localhost:4321`
- Recarga automática cuando guardas cambios
- Muestra errores en tiempo real

### Construir para Producción

```bash
npm run build
```

- Genera el sitio estático en la carpeta `dist/`
- Optimiza imágenes, CSS y JavaScript
- Prepara el sitio para deployment

### Previsualizar Build

```bash
npm run preview
```

- Muestra cómo se verá el sitio en producción
- Usa la carpeta `dist/` generada por `build`
- Útil para verificar antes de publicar

---

## Estructura de Archivos Generada

Después de la instalación, tendrás esta estructura:

```
web_lacige/
├── .astro/              # Configuración interna de Astro
├── node_modules/        # Dependencias instaladas
├── public/              # Archivos estáticos (imágenes, favicon, etc.)
├── src/                 # Código fuente
│   ├── components/      # Componentes Astro
│   ├── content/         # Artículos y publicaciones
│   ├── layouts/         # Layouts de página
│   ├── pages/           # Rutas del sitio
│   └── styles/          # CSS global
├── DOCS/                # Documentación (esta carpeta)
├── astro.config.mjs     # Configuración de Astro
├── package.json         # Dependencias y scripts
└── tsconfig.json        # Configuración de TypeScript
```

---

## Solución de Problemas Comunes

### Error: "Cannot find module"

```bash
# Eliminar node_modules y reinstalar
rm -rf node_modules package-lock.json
npm install
```

### Error: "Port 4321 is already in use"

```bash
# Usar otro puerto
npm run dev -- --port 3000
```

### Cambios no se reflejan

```bash
# Limpiar caché de Astro
rm -rf .astro
npm run dev
```

---

## Deployment (Publicación)

### GitHub Pages

El sitio está configurado para deploy automático en GitHub Pages:

1. Configurar en `astro.config.mjs`:
```javascript
export default defineConfig({
  site: 'https://xyzp11t.github.io',
  base: '/'
});
```

2. Los archivos se generan en `dist/` al ejecutar `npm run build`

3. Subir los archivos de `dist/` a la rama `gh-pages` o configurar GitHub Actions

### Otros Servicios

Para otros servicios (Netlify, Vercel, etc.):

1. Conectar el repositorio al servicio
2. Configurar el comando de build: `npm run build`
3. Configurar la carpeta de salida: `dist`

---

## Actualizaciones de Dependencias

Para mantener el proyecto actualizado:

```bash
# Verificar actualizaciones disponibles
npm outdated

# Actualizar todas las dependencias
npm update

# O actualizar una específica
npm update astro
```

---

## Configuración del Editor (VS Code recomendado)

### Extensiones Recomendadas

1. **Astro** - Soporte oficial para archivos .astro
2. **TypeScript Importer** - Autocompletado de imports
3. **ESLint** - Linting de código
4. **Prettier** - Formateo de código

### Configuración de VS Code

Crear `.vscode/settings.json`:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "[astro]": {
    "editor.defaultFormatter": "astro-build.astro-vscode"
  }
}
```

---

## Próximos Pasos

Una vez instalado, revisa:
- [02-ESTRUCTURA-DEL-PROYECTO.md](./02-ESTRUCTURA-DEL-PROYECTO.md) - Entender la organización
- [04-ARTICULOS-DIVULGACION.md](./04-ARTICULOS-DIVULGACION.md) - Agregar contenido
- [07-ESTILOS-Y-DISENO.md](./07-ESTILOS-Y-DISENO.md) - Personalizar estilos
