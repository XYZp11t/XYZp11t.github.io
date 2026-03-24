# 04. Artículos de Divulgación

Guía completa para crear, editar y gestionar artículos de divulgación científica en el sitio LACIGE.

---

## Índice

1. [Estructura de un Artículo](#estructura-de-un-artículo)
2. [Frontmatter (Metadatos)](#frontmatter-metadatos)
3. [Crear un Nuevo Artículo](#crear-un-nuevo-artículo)
4. [Contenido Markdown](#contenido-markdown)
5. [Imágenes en Artículos](#imágenes-en-artículos)
6. [Ejemplo Completo](#ejemplo-completo)
7. [Visualización en el Sitio](#visualización-en-el-sitio)

---

## Estructura de un Artículo

Los artículos se encuentran en: `src/content/divulgacion/`

Cada artículo es un archivo **Markdown** (`.md`) con esta estructura:

```markdown
---
# FRONTMATTER: Metadatos del artículo
titulo: "Título del Artículo"
descripcion: "Descripción corta para previews"
autor: "Nombre del Autor"
fecha: 2024-01-15
imagen: "/ruta/de/la/imagen.jpg"
etiquetas: ["tag1", "tag2", "tag3"]
destacado: true
---

# CONTENIDO: Cuerpo del artículo en Markdown

## Subtítulo

Texto del artículo con **negritas**, *cursivas*, etc.
```

---

## Frontmatter (Metadatos)

Los metadatos van entre triples guiones `---` al inicio del archivo.

### Campos Requeridos

| Campo | Tipo | Descripción | Ejemplo |
|-------|------|-------------|---------|
| `titulo` | `string` | Título del artículo | `"Tránsito de Mercurio"` |
| `descripcion` | `string` | Resumen corto (150-200 caracteres) | `"Guía completa sobre..."` |
| `autor` | `string` | Nombre completo del autor | `"Dr. Mario Rodríguez"` |
| `fecha` | `date` | Fecha de publicación (YYYY-MM-DD) | `2024-01-15` |

### Campos Opcionales

| Campo | Tipo | Descripción | Ejemplo |
|-------|------|-------------|---------|
| `imagen` | `string` | Ruta de imagen destacada | `"/transito-mercurio/mercurio.jpg"` |
| `etiquetas` | `string[]` | Array de etiquetas | `["astronomía", "eventos"]` |
| `destacado` | `boolean` | Mostrar en página de inicio | `true` o `false` |
| `galeria` | `object` | Configuración de galería de imágenes | `{ ruta: "/evento/imagenes", titulo: "Galería" }` |

### Ejemplo de Frontmatter

```yaml
---
titulo: "Tránsito de Mercurio por el Disco Solar"
descripcion: "Guía completa sobre el fenómeno astronómico donde Mercurio cruza frente al Sol, sus etapas y cómo observarlo de forma segura."
autor: "Dr. Mario Rodríguez Martínez"
fecha: 2016-05-02
imagen: "/transito-mercurio/mercurio.jpg"
etiquetas: ["astronomía", "eventos", "magnetosfera", "Mercurio", "observación solar"]
destacado: true
---
```

---

## Crear un Nuevo Artículo

### Paso 1: Crear el Archivo

1. Navega a `src/content/divulgacion/`
2. Crea un archivo con nombre descriptivo en **kebab-case**:
   - ✅ `transito-de-mercurio.md`
   - ✅ `eclipse-parcial-2024.md`
   - ❌ `Artículo del Sol.md` (no usar espacios)
   - ❌ `articulo1.md` (ser más descriptivo)

### Paso 2: Agregar Frontmatter

Copia esta plantilla y modifica los valores:

```markdown
---
titulo: "TÍTULO DEL ARTÍCULO"
descripcion: "Descripción corta que aparecerá en las tarjetas de preview (máximo 200 caracteres)."
autor: "Nombre del Autor"
fecha: 2024-01-15
imagen: "/carpeta/imagen.jpg"
etiquetas: ["etiqueta1", "etiqueta2", "etiqueta3"]
destacado: false
---

```

### Paso 3: Escribir el Contenido

Escribe el cuerpo del artículo usando Markdown (ver sección siguiente).

### Paso 4: Guardar y Verificar

1. Guarda el archivo
2. Ejecuta `npm run dev`
3. Visita `http://localhost:4321/divulgacion`
4. Haz clic en tu artículo para verificar que se ve correctamente

---

## Contenido Markdown

El cuerpo del artículo usa **Markdown** con HTML opcional.

### Formato Básico

```markdown
# Título Principal (H1)
## Subtítulo (H2)
### Sub-subtítulo (H3)

**Texto en negrita**
*Texto en cursiva*
***Texto en negrita y cursiva***

- Elemento de lista
- Otro elemento
  - Sub-elemento

1. Lista numerada
2. Segundo elemento

[Texto del enlace](https://ejemplo.com)

> Cita en bloque
```

### Elementos Especiales

#### Figuras con Imágenes

Para imágenes con leyenda, usa la etiqueta `<figure>`:

```markdown
<figure>
  <img src="/ruta/imagen.png" alt="Descripción accesible">
  <figcaption>Figura 1. Leyenda de la imagen.</figcaption>
</figure>
```

#### Cajas de Advertencia

Para alertas importantes:

```markdown
<h2 class="advertencia">¡ADVERTENCIA!</h2>

<div class="advertencia-box">
<p><strong>Nunca se debe observar el Sol de forma directa</strong>, ya que esto puede provocar daños irreversibles a la vista.</p>
</div>
```

#### Información del Autor

```markdown
<p class="autor-info"><strong>Por:</strong> Dr. Mario Rodríguez Martínez</p>
```

### Código HTML Permitido

Puedes usar HTML dentro del Markdown:

```markdown
<div class="article-content">

## Título

Texto normal.

</div>
```

---

## Imágenes en Artículos

### Ubicación

Las imágenes deben ir en la carpeta `public/`:

```
public/
├── transito-de-mercurio/
│   ├── mercurio.jpg          # Imagen principal
│   ├── etapas.png            # Diagrama
│   └── densidad.png          # Gráfica
└── eclipse-2024/
    ├── eclipse.jpg
    └── fotos/
        ├── foto1.jpg
        └── foto2.jpg
```

### Formato Recomendado

- **Formato:** JPG para fotos, PNG para gráficos/diagramas
- **Tamaño:** Máximo 1920px de ancho
- **Peso:** Optimizar para web (menos de 500KB ideal)
- **Nombres:** Descriptivos, sin espacios, en minúsculas

### Referenciar Imágenes

```markdown
<!-- Imagen simple -->
<img src="/transito-mercurio/mercurio.jpg" alt="Descripción">

<!-- Imagen con caption -->
<figure>
  <img src="/transito-mercurio/etapas.png" alt="Diagrama de etapas">
  <figcaption>Figura 1. Etapas del tránsito.</figcaption>
</figure>
```

### Imagen Destacada

La imagen que se muestra en la tarjeta del artículo:

```yaml
---
imagen: "/transito-mercurio/mercurio.jpg"
---
```

**Recomendaciones:**
- Proporción 16:10
- Mínimo 800px de ancho
- Representativa del contenido

---

## Galería de Imágenes (Carrusel)

Para artículos de eventos o actividades con múltiples fotografías, se puede incluir un carrusel interactivo que muestra las imágenes en grupos de 3 (desktop), 2 (tablet) o 1 (móvil).

### Configuración

Agrega la sección `galeria` al frontmatter:

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

### Campos de la Galería

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `ruta` | `string` | Sí | Ruta a la carpeta con las imágenes (debe estar en `public/`) |
| `titulo` | `string` | No | Título mostrado sobre el carrusel (default: "Galería de imágenes") |

### Estructura de Carpetas

```
public/
└── TTP2026/
    └── imagenes/
        ├── _DSC4609.jpg
        ├── _DSC4619.jpg
        ├── IMG_2234.JPG
        └── ... (58 imágenes en total)
```

### Funcionamiento del Carrusel

#### Visualización

| Dispositivo | Imágenes visibles | Navegación |
|-------------|-------------------|------------|
| Desktop (≥1024px) | 3 imágenes | Por páginas de 3 |
| Tablet (640-1023px) | 2 imágenes | Por páginas de 2 |
| Móvil (<640px) | 1 imagen | Por páginas de 1 |

#### Controles

- **Flechas laterales (← →)**: Navegar entre páginas
- **Dots indicadores**: Saltar a una página específica
- **Botón ▶/⏸**: Pausar/reanudar reproducción automática
- **Swipe**: Navegar en dispositivos táctiles

#### Autoplay

- Las imágenes cambian automáticamente cada **5 segundos**
- Se pausa al hacer **hover** con el mouse
- Se pausa al hacer **clic** en una imagen (abre lightbox)
- Se reanuda al quitar el mouse

### Visor Lightbox

Al hacer clic en cualquier imagen del carrusel:

- Se abre un visor a **pantalla completa**
- Navegación **imagen por imagen** (no por páginas)
- Muestra contador "X / 58"
- **Teclado**: ← → para navegar, ESC para cerrar
- **Swipe**: En móviles para cambiar de imagen

### Preparar Imágenes para la Galería

1. **Copiar imágenes** a la carpeta `public/[nombre-evento]/imagenes/`
2. **Formatos soportados**: `.jpg`, `.jpeg`, `.png`
3. **Optimización recomendada**:
   - Tamaño máximo: 1920px de ancho
   - Peso: menos de 500KB por imagen
   - Calidad: 80-85% para fotos

### Notas Importantes

- El carrusel se muestra automáticamente al final del contenido del artículo
- Las imágenes se cargan de forma progresiva (lazy loading)
- El orden de las imágenes en el carrusel corresponde al orden del array interno `IMAGES_LIST` en el componente

---

## Ejemplo Completo

Archivo: `src/content/divulgacion/eclipse-solar-2024.md`

```markdown
---
titulo: "Eclipse Solar Parcial de 2024"
descripcion: "Todo lo que necesitas saber sobre el eclipse solar parcial visible en México el 8 de abril de 2024, horarios y recomendaciones de observación."
autor: "Dra. Ana López García"
fecha: 2024-03-15
imagen: "/eclipse-2024/eclipse-promo.jpg"
etiquetas: ["astronomía", "eclipse", "eventos", "observación solar"]
destacado: true
---

<div class="article-content">

<h1>Eclipse Solar Parcial de 2024</h1>

<p class="autor-info"><strong>Por:</strong> Dra. Ana López García</p>

<p>El próximo <strong>8 de abril de 2024</strong> se producirá un eclipse solar parcial visible desde gran parte de México. Este evento astronómico es una oportunidad única para observar la interacción entre el Sol y la Luna.</p>

## ¿Qué es un eclipse solar?

Un eclipse solar ocurre cuando la Luna se interpone entre la Tierra y el Sol, bloqueando parcial o totalmente la luz solar. En este caso, será un **eclipse parcial**, lo que significa que la Luna cubrirá solo una parte del disco solar.

## Horarios de observación

Para la ciudad de Morelia, los horarios aproximados serán:

- **Inicio:** 10:30 horas
- **Máximo:** 12:15 horas
- **Fin:** 13:50 horas

<figure>
  <img src="/eclipse-2024/mapa-eclipse.png" alt="Mapa de visibilidad del eclipse">
  <figcaption>Figura 1. Mapa mostrando las zonas de visibilidad del eclipse en México.</figcaption>
</figure>

## Recomendaciones de seguridad

<h2 class="advertencia">¡ADVERTENCIA!</h2>

<div class="advertencia-box">
<p><strong>Nunca observes el Sol directamente</strong> sin protección adecuada. Usa lentes especiales para eclipses o el método de proyección.</p>
</div>

### Métodos de observación segura:

1. **Lentes certificados ISO 12312-2**
2. **Proyector pinhole (cámara oscura)**
3. **Telescopio con filtro solar**

## El LACIGE y el eclipse

El Laboratorio de Ciencias Geoespaciales estará realizando observaciones durante el evento. Visítanos en las instalaciones de la ENES Morelia.

</div>
```

---

## Visualización en el Sitio

### Página de Divulgación

Todos los artículos aparecen en: `/divulgacion`

- Ordenados por fecha (más recientes primero)
- Muestran tarjeta con imagen, título, descripción y autor

### Página de Inicio

Solo los artículos con `destacado: true` aparecen en la sección "Últimas Publicaciones" de la página de inicio.

### Página Individual

Cada artículo tiene su propia página:
- URL: `/divulgacion/[nombre-del-archivo]`
- Ejemplo: `/divulgacion/eclipse-solar-2024`
- Incluye: imagen destacada, metadatos, contenido, botones para compartir

---

## Editar un Artículo Existente

1. Localiza el archivo en `src/content/divulgacion/`
2. Abre el archivo `.md`
3. Realiza los cambios
4. Guarda y verifica en el navegador

**Nota:** Si modificas la `fecha`, el artículo cambiará de posición en el listado.

---

## Eliminar un Artículo

1. Elimina el archivo `.md` de `src/content/divulgacion/`
2. (Opcional) Elimina las imágenes asociadas de `public/`
3. Ejecuta `npm run build` para verificar que no hay errores

---

## Solución de Problemas

### El artículo no aparece

- Verifica que la `fecha` esté en formato correcto: `YYYY-MM-DD`
- Verifica que el archivo tenga extensión `.md`
- Reinicia el servidor de desarrollo

### La imagen no se muestra

- Verifica que la ruta comience con `/`
- Verifica que la imagen exista en la carpeta `public/`
- Recarga la página con `Ctrl+F5`

### Error al compilar

- Verifica que el frontmatter esté correctamente cerrado con `---`
- Verifica que no haya caracteres especiales en el título sin escapar

---

## Próximos Pasos

- [05-PUBLICACIONES-CIENTIFICAS.md](./05-PUBLICACIONES-CIENTIFICAS.md) - Agregar publicaciones
- [06-GALERIA-SOLAR.md](./06-GALERIA-SOLAR.md) - Gestión de imágenes solares
