# Documentación LACIGE - Laboratorio de Ciencias Geoespaciales

## Índice de Documentación

Esta carpeta contiene la documentación completa del sitio web del LACIGE. A continuación encontrarás enlaces a cada sección:

1. **[01-INSTALACION-Y-SETUP.md](./01-INSTALACION-Y-SETUP.md)** - Guía para instalar, configurar y hacer deploy del sitio
2. **[02-ESTRUCTURA-DEL-PROYECTO.md](./02-ESTRUCTURA-DEL-PROYECTO.md)** - Explicación de la organización de archivos
3. **[03-COMPONENTES.md](./03-COMPONENTES.md)** - Documentación de todos los componentes reutilizables
4. **[04-ARTICULOS-DIVULGACION.md](./04-ARTICULOS-DIVULGACION.md)** - Cómo crear y gestionar artículos de divulgación
5. **[05-PUBLICACIONES-CIENTIFICAS.md](./05-PUBLICACIONES-CIENTIFICAS.md)** - Cómo agregar publicaciones y tesis
6. **[06-GALERIA-SOLAR.md](./06-GALERIA-SOLAR.md)** - Sistema de imágenes solares y visor
7. **[07-ESTILOS-Y-DISENO.md](./07-ESTILOS-Y-DISENO.md)** - Guía de estilos, colores y CSS
8. **[08-CONFIGURACION.md](./08-CONFIGURACION.md)** - Configuración de Astro y build
9. **[09-COLABORADORES.md](./09-COLABORADORES.md)** - Gestión de investigadores y colaboradores

---

## Resumen Rápido

### Tecnologías Utilizadas
- **Astro 5.x** - Framework de generación de sitios estáticos
- **TypeScript** - Tipado estático para JavaScript
- **CSS Custom Properties** - Variables CSS para estilos consistentes
- **View Transitions** - Transiciones suaves entre páginas

### Estructura de Carpetas Principal
```
src/
├── components/     # Componentes reutilizables (Astro)
├── content/        # Contenido Markdown (artículos, publicaciones, colaboradores)
│   ├── colaboradores/   # Investigadores internos y externos
│   ├── divulgacion/     # Artículos de divulgación
│   └── publicaciones/   # Publicaciones científicas
├── layouts/        # Layouts de página
├── pages/          # Rutas del sitio
├── styles/         # Estilos CSS globales
└── content.config.ts  # Configuración de colecciones de contenido
```

### Comandos Principales
```bash
npm run dev      # Servidor de desarrollo
npm run build    # Construir sitio para producción
npm run preview  # Previsualizar build de producción
```

---

## Contacto y Soporte

Para dudas técnicas sobre el sitio web, contactar al desarrollador responsable.

**Nota importante:** Esta documentación debe mantenerse actualizada cada vez que se realicen cambios significativos en la estructura o funcionalidad del sitio.
