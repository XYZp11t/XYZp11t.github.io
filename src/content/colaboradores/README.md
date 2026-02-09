# Gestión de Colaboradores

Este directorio contiene la información de todos los colaboradores del LACIGE. Los datos se organizan usando **Astro Content Collections**, lo que permite agregar, modificar o eliminar colaboradores sin necesidad de hacer rebuild del sitio en desarrollo.

## Estructura de Archivos

```
src/content/colaboradores/
├── grupos/                    # Definición de instituciones/grupos
│   ├── academicos.md         # Académicos LACIGE (internos)
│   ├── posdoctorantes.md     # Posdoctorantes (internos)
│   ├── igum.md               # Instituto de Geofísica U. Michoacán
│   ├── irya.md               # Instituto de Radioastronomía y Astrofísica
│   └── ...
├── internos/                  # Colaboradores internos
│   ├── dr-mario-rodriguez.md
│   ├── dr-sinhue-haro.md
│   └── ...
├── externos/                  # Colaboradores externos
│   ├── dr-americo-gonzalez.md
│   └── ...
├── README.md                  # Este archivo
└── TEMPLATE.md                # Template base
```

## Cómo Agregar un Nuevo Colaborador

### 1. Colaborador Interno (Académico o Posdoctorante)

Crea un archivo `.md` en `src/content/colaboradores/internos/` con el siguiente formato:

```yaml
---
nombre: "Dr. [Nombre Completo]"
imagen: "/colaboradores/nombre-archivo.jpg"  # Opcional, dejar '' si no hay
perfil:
  cargo: "Técnico Académico T. C."           # O "Profesor...", "Estudiante de posdoctorado", etc.
  areaEstudio: "Descripción del área..."     # Opcional
  oficina: "Edificio A, Oficina 101"         # Opcional
  telefono: "+52 (443) 000-0000"             # Opcional
  email: "correo@enesmorelia.unam.mx"        # Opcional
esEncargado: false                           # true solo para el responsable del lab
orden: 10                                    # Orden de aparición (menor = primero)
---

Escribe aquí la biografía del colaborador. Párrafos simples con la información
relevante sobre su trayectoria, formación, investigación, etc.

## Líneas de Investigación

Descipción de las líneas de investigación (opcional).

<div class="research-areas">
  <span class="research-tag">Área 1</span>
  <span class="research-tag">Área 2</span>
</div>

## Publicaciones Selectas

<div class="publication-list">
  <div class="publication-item">
    <span class="pub-number">1</span>
    <div class="pub-content">
      <span class="pub-title">Título del paper</span>
      <span class="pub-authors">Autores</span>
      <span class="pub-journal">Revista, Año</span>
      <a class="pub-link" href="https://doi.org/...">DOI: ...</a>
    </div>
  </div>
</div>

## Proyectos

<div class="project-list">
  <div class="project-item">
    <span class="project-period">2020 – Actualidad</span>
    <p>Título del proyecto</p>
    <p class="project-funding">Descripción o financiamiento...</p>
  </div>
</div>
```

### 2. Colaborador Externo

Crea un archivo `.md` en `src/content/colaboradores/externos/`:

```yaml
---
nombre: "Dr. [Nombre Completo]"
imagen: ""
perfil:
  cargo: ""
  areaEstudio: "Física Solar y Clima Espacial"
  oficina: "Edificio Principal, Oficina 201"
  telefono: "+52 (443) 123-4567"
  email: "correo@institucion.unam.mx"
esEncargado: false
orden: 1
grupoSiglas: "IGUM"                         # ← Siglas de la institución
---

Contenido de la biografía...
```

**El campo `grupoSiglas` determina a qué institución pertenece el colaborador.** Debe coincidir con las siglas definidas en `src/content/colaboradores/grupos/`.

**Siglas disponibles:**

| Institución | Siglas |
|-------------|--------|
| Instituto de Geofísica U. Michoacán | `IGUM` |
| Instituto de Radioastronomía y Astrofísica | `IRYA` |
| Instituto de Geofísica | `IG` |
| Centro de Alta Tecnología | `CAT` |
| Instituto de Ciencias Nucleares | `ICN` |
| Universidad de Sonora | `UNISON` |
| Instituto de Astronomía - Ensenada | `IA-ENS` |
| Universidad Autónoma de Nuevo León | `UANL` |
| INAOE | `INAOE` |

### 3. Nueva Institución/Grupo

Para agregar una nueva institución, crea un archivo en `src/content/colaboradores/grupos/`:

```yaml
---
institucion: "Nombre Completo de la Institución"
siglas: "SIGLAS"
tipo: "externo"        # "interno" o "externo"
orden: 10              # Orden de aparición
---
```

Luego, al crear colaboradores para esta institución, usa el campo `grupoSiglas` con las siglas definidas.

## Campos del Schema

### Investigador

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `nombre` | string | ✅ | Nombre completo del investigador |
| `imagen` | string | | Ruta a la imagen (relativa a `/public`) |
| `perfil.cargo` | string | | Cargo o posición |
| `perfil.areaEstudio` | string | | Área de investigación |
| `perfil.oficina` | string | | Ubicación de oficina |
| `perfil.telefono` | string | | Teléfono de contacto |
| `perfil.email` | string | | Correo electrónico |
| `esEncargado` | boolean | | `true` si es el responsable del laboratorio |
| `orden` | number | | Posición en la lista (menor = primero) |
| `grupoSiglas` | string | Solo externos | Siglas de la institución (ej: `"IGUM"`, `"IRYA"`) |

### Grupo

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `institucion` | string | ✅ | Nombre completo de la institución |
| `siglas` | string | ✅ | Siglas o abreviatura |
| `tipo` | enum | ✅ | `"interno"` o `"externo"` |
| `orden` | number | | Posición en la lista |

## Página de Biografía

Si el archivo markdown contiene contenido después del frontmatter (más de 10 caracteres), se mostrará automáticamente:

1. Un botón **"Ver biografía"** en la tarjeta del colaborador
2. Una **página dedicada** accesible en `/colaborador/[nombre-del-archivo]`

### Estructura HTML recomendada:

#### Biografía
Escribe párrafos normales de texto. No uses estilos especiales de introducción.

```markdown
Escribe la biografía directamente, sin divs especiales. Párrafos simples
con la información relevante.
```

#### Líneas de investigación (tags separados por puntos):
```html
<div class="research-areas">
  <span class="research-tag">Física Solar</span>
  <span class="research-tag">Clima Espacial</span>
</div>
```

#### Lista de publicaciones (numeradas):
```html
<div class="publication-list">
  <div class="publication-item">
    <span class="pub-number">1</span>
    <div class="pub-content">
      <span class="pub-title">Título del paper</span>
      <span class="pub-authors">Lista de autores</span>
      <span class="pub-journal">Revista, Volumen, Año</span>
      <a class="pub-link" href="https://doi.org/...">DOI: ...</a>
    </div>
  </div>
</div>
```

#### Proyectos (compactos, sin cajas grandes):
```html
<div class="project-list">
  <div class="project-item">
    <span class="project-period">2020 – Actualidad</span>
    <p>Título del proyecto</p>
    <p class="project-funding">Información de financiamiento...</p>
  </div>
</div>
```

## Clases CSS Disponibles

| Clase | Uso |
|-------|-----|
| `.bio-section` | Contenedor de sección de biografía (opcional) |
| `.research-areas` | Contenedor de tags de líneas de investigación |
| `.research-tag` | Tag individual de línea de investigación |
| `.publication-list` | Contenedor de lista de publicaciones |
| `.publication-item` | Item individual de publicación |
| `.pub-number` | Número de publicación |
| `.pub-content` | Contenedor de contenido de publicación |
| `.pub-title` | Título del paper |
| `.pub-authors` | Lista de autores |
| `.pub-journal` | Nombre de la revista |
| `.pub-link` | Enlace al DOI |
| `.project-list` | Contenedor de lista de proyectos |
| `.project-item` | Item individual de proyecto |
| `.project-period` | Período del proyecto |
| `.project-funding` | Información de financiamiento |

## Currículum Vitae (CV)

Si deseas agregar un CV para un colaborador:

1. Guarda el archivo PDF en la carpeta `/public/CVs/`
2. En el frontmatter del archivo `.md`, agrega el campo `cv` con la ruta al archivo:

```yaml
---
nombre: "Dr. Mario Rodríguez Martínez"
imagen: "/colaboradores/DrMarioRod.jpg"
cv: "/CVs/cv_MRM_ENESM.pdf"  # ← Agrega esta línea
perfil:
  cargo: "Responsable del Laboratorio"
  ...
---
```

3. Si el campo `cv` está vacío (`""`) o no existe, no se mostrará el botón "Ver CV"
4. El CV se abre en una pestaña nueva del navegador

## Consejos

1. **Imágenes**: Guarda las imágenes en `/public/colaboradores/` con nombres descriptivos.
2. **CVs**: Guarda los archivos PDF en `/public/CVs/` para que aparezca el enlace de descarga.
3. **Orden**: Usa `orden: 1` para el responsable, `orden: 2-10` para académicos principales, etc.
4. **Campos vacíos**: Todos los campos pueden estar vacíos (`''`), pero deben existir en el archivo.
5. **Biografía**: Si agregas contenido markdown después del frontmatter, aparecerá el botón "Ver biografía" y se creará la página dedicada.
6. **Información de contacto**: No repitas el email o teléfono en el body del markdown, ya que se muestra automáticamente en la tarjeta del colaborador y en el sidebar de la página de biografía.
7. **URLs amigables**: La página de biografía tendrá la URL `/colaborador/nombre-del-archivo` (sin la extensión `.md`).
8. **No inventes contenido**: Solo agrega información que realmente tengas del colaborador.
9. **Diseño limpio**: Evita cajas grandes y estilos llamativos. Prefiere diseños compactos y profesionales.

## Solución de Problemas

### Los cambios no aparecen
- Verifica que el archivo tenga extensión `.md`
- Revisa que el frontmatter (entre `---`) esté bien formado
- Asegúrate de que no haya errores de sintaxis YAML

### El botón "Ver biografía" no aparece
- El contenido debe tener al menos 10 caracteres
- Verifica que haya contenido después del segundo `---`

### La página de biografía no se genera
- Verifica que el archivo no tenga errores de sintaxis
- Asegúrate de que el `id` del archivo sea único

### Un investigador no aparece en el grupo correcto

**Internos:** Verifica que el campo `cargo` contenga el texto correcto:
- `"posdoctorado"` → Grupo Posdoctorantes
- Cualquier otro → Grupo Académicos

**Externos:** Verifica que el campo `grupoSiglas` coincida exactamente con las siglas definidas en el archivo del grupo.

### Error de validación
- Todos los campos en `perfil` deben ser strings (usar `''` para vacío)
- `esEncargado` debe ser `true` o `false` (sin comillas)
- `orden` debe ser un número
- `grupoSiglas` debe coincidir exactamente con las siglas del grupo
