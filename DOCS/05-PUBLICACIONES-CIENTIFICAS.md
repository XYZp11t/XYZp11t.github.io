# 05. Publicaciones Científicas

Guía para agregar y gestionar publicaciones científicas (artículos y tesis) del LACIGE.

---

## Índice

1. [Tipos de Publicaciones](#tipos-de-publicaciones)
2. [Estructura de Datos](#estructura-de-datos)
3. [Crear un Artículo Científico](#crear-un-artículo-científico)
4. [Crear una Tesis](#crear-una-tesis)
5. [Campos de Metadatos](#campos-de-metadatos)
6. [Ejemplos Completos](#ejemplos-completos)
7. [Categorías de Producción](#categorías-de-producción)

---

## Tipos de Publicaciones

El sistema soporta dos tipos de publicaciones:

| Tipo | Descripción | Campos Específicos |
|------|-------------|-------------------|
| `articulo` | Artículos en revistas científicas | `revista`, `doi`, `categoria` |
| `tesis` | Tesis de posgrado | `institucion`, `director` |

---

## Estructura de Datos

Las publicaciones se encuentran en: `src/content/publicaciones/`

Formato general:

```markdown
---
# FRONTMATTER: Metadatos
titulo: "Título de la publicación"
autores: ["Autor 1", "Autor 2", "Autor 3"]
anio: 2024
tipo: "articulo" | "tesis"
# ... campos específicos
---

Resumen o información adicional en texto libre.
```

---

## Crear un Artículo Científico

### Paso 1: Crear el Archivo

Crea un archivo en `src/content/publicaciones/` con nombre descriptivo:

```
articulo-[tema-corto]-[año].md
```

Ejemplos:
- `articulo-ionosfera-mexart-2012.md`
- `articulo-viento-solar-2023.md`
- `articulo-magnetosfera-2018.md`

### Paso 2: Frontmatter para Artículos

```yaml
---
titulo: "Título completo del artículo"
autores: ["Apellido, Nombre", "Apellido2, Nombre2"]
revista: "Nombre de la Revista, Volumen, Páginas"
anio: 2024
doi: "10.xxxx/xxxxx"  # Opcional
resumen: "Resumen de la publicación..."
tipo: "articulo"
categoria: "previa" | "produccion"  # Opcional
enlace: "https://doi.org/..."  # Opcional
---

Texto opcional con información adicional.
```

---

## Crear una Tesis

### Paso 1: Crear el Archivo

```
tesis-[tema-corto]-[año].md
```

Ejemplos:
- `tesis-magnetosfera-terrestre-2015.md`
- `tesis-perturbaciones-ionosfericas-2020.md`

### Paso 2: Frontmatter para Tesis

```yaml
---
titulo: "Título completo de la tesis"
autores: ["Apellido, Nombre del tesista"]
anio: 2024
resumen: "Resumen de la tesis..."
tipo: "tesis"
institucion: "Universidad o Institución"
director: "Dr. Nombre del Director"
directorInstitucion: "Institución del director"  # Opcional
enlace: "https://repositorio.unam.mx/..."  # Opcional
---

Texto opcional con información adicional.
```

---

## Campos de Metadatos

### Campos Comunes (Todos los Tipos)

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `titulo` | `string` | Sí | Título completo de la publicación |
| `autores` | `string[]` | Sí | Array de autores (formato: "Apellido, Nombre") |
| `anio` | `number` | Sí | Año de publicación |
| `resumen` | `string` | Sí | Resumen o descripción breve |
| `tipo` | `enum` | Sí | `"articulo"` o `"tesis"` |
| `enlace` | `string` | No | URL al documento o repositorio |

### Campos Específicos para Artículos

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `revista` | `string` | No | Nombre de revista, volumen y páginas |
| `doi` | `string` | No | DOI del artículo |
| `categoria` | `enum` | No | `"previa"` o `"produccion"` |

### Campos Específicos para Tesis

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `institucion` | `string` | No | Universidad o institución donde se defendió |
| `director` | `string` | No | Nombre del director de tesis |
| `directorInstitucion` | `string` | No | Institución del director |

---

## Ejemplos Completos

### Ejemplo: Artículo Científico

Archivo: `articulo-ionospheric-disturbances-2014.md`

```markdown
---
titulo: "Ionospheric disturbances detected by Interplanetary Scintillation (IPS)")
autores: ["Carrillo-Vargas, A.", "Pérez-Enríquez, H. R.", "Rodríguez-Martínez, M.", "López-Montes, R."]
revista: "Advances in Space Research, Volume 53, Issue 10, p. 1473-1484"
anio: 2014
doi: "10.1016/j.asr.2014.02.005"
resumen: "Análisis de perturbaciones ionosféricas detectadas mediante el método de centelleo interplanetario (IPS)."
tipo: "articulo"
categoria: "previa"
enlace: "https://doi.org/10.1016/j.asr.2014.02.005"
---

Este trabajo presenta el análisis de perturbaciones ionosféricas utilizando el método de centelleo interplanetario (IPS) con datos del arreglo MEXART.
```

### Ejemplo: Artículo sin DOI

```markdown
---
titulo: "Análisis de señales de radio en eventos geomagnéticos"
autores: ["García-López, M.", "Rodríguez-Martínez, M."]
revista: "Revista Mexicana de Astronomía y Astrofísica, Vol. 45, pp. 123-135"
anio: 2019
resumen: "Estudio de las variaciones en señales de radio causadas por tormentas geomagnéticas."
tipo: "articulo"
categoria: "produccion"
---
```

### Ejemplo: Tesis de Doctorado

Archivo: `tesis-magnetosfera.md`

```markdown
---
titulo: "Estudio de la magnetosfera terrestre durante eventos de tormentas geomagnéticas"
autores: ["Hernández-Pérez, Juan Carlos"]
anio: 2015
resumen: "Tesis doctoral que analiza la respuesta de la magnetosfera terrestre durante eventos de tormentas geomagnéticas intensas usando datos satelitales."
tipo: "tesis"
institucion: "Universidad Nacional Autónoma de México"
director: "Dr. Mario Rodríguez Martínez"
directorInstitucion: "UNAM - ENES Morelia"
enlace: "https://tesis.unam.mx/tesis/12345"
---

Tesis doctoral presentada en la Universidad Nacional Autónoma de México como requisito parcial para obtener el grado de Doctor en Ciencias (Astrofísica).
```

### Ejemplo: Tesis de Maestría

```markdown
---
titulo: "Caracterización de perturbaciones ionosféricas usando el arreglo MEXART"
autores: ["Sánchez-García, María Elena"]
anio: 2018
resumen: "Tesis de maestría sobre la caracterización de perturbaciones ionosféricas mediante el análisis de datos del arreglo MEXART."
tipo: "tesis"
institucion: "Universidad Nacional Autónoma de México"
director: "Dr. Mario Rodríguez Martínez"
---
```

---

## Categorías de Producción

Los artículos pueden clasificarse en dos categorías:

### `"previa"` (Producción Previa)

Artículos publicados antes de la formación del LACIGE o por investigadores antes de unirse al laboratorio.

```yaml
---
categoria: "previa"
---
```

### `"produccion"` (Producción del LACIGE)

Artículos producidos durante la operación del LACIGE.

```yaml
---
categoria: "produccion"
---
```

### Sin categoría

Si no se especifica, el artículo aparecerá en ambas secciones o en la sección general.

---

## Visualización en el Sitio

Las publicaciones se muestran en tres páginas:

### 1. Página General (`/investigacion/publicaciones`)

- Muestra tanto artículos como tesis
- Agrupadas por año
- Ordenadas de más reciente a más antigua

### 2. Página de Artículos (`/investigacion/publicaciones/articulos`)

- Solo artículos científicos
- Separados en secciones:
  - **Producción del LACIGE** (categoria: produccion)
  - **Producción Previa** (categoria: previa)

### 3. Página de Tesis (`/investigacion/publicaciones/tesis`)

- Solo tesis de posgrado
- Agrupadas por año
- Muestra información del director y la institución

---

## Formato de Autores

### Formato Recomendado

```yaml
autores: ["Apellido-Paterno, Nombre", "Apellido2, Nombre2"]
```

### Ejemplos

```yaml
# Un autor
autores: ["Rodríguez-Martínez, Mario"]

# Dos autores
autores: ["Pérez-Enríquez, H. R.", "Carrillo-Vargas, A."]

# Múltiples autores
autores: [
  "Carrillo-Vargas, A.",
  "Pérez-Enríquez, H. R.",
  "Rodríguez-Martínez, M.",
  "López-Montes, R."
]
```

---

## Formato de Revista

El campo `revista` debería incluir:
- Nombre de la revista
- Volumen
- Número (opcional)
- Páginas

```yaml
revista: "Nombre de Revista, Volume 49, Issue 11, p. 1570-1580"
```

---

## Enlaces (DOI y URLs)

### DOI

Si el artículo tiene DOI, incluirlo así:

```yaml
doi: "10.1016/j.asr.2011.12.017"
```

El DOI se usará para crear un enlace automático a: `https://doi.org/10.1016/j.asr.2011.12.017`

### Enlace Directo

Para enlaces a repositorios institucionales u otros:

```yaml
enlace: "https://repositorio.unam.mx/handle/12345/67890"
```

---

## Solución de Problemas

### La publicación no aparece

- Verifica que el campo `tipo` sea exactamente `"articulo"` o `"tesis"`
- Verifica que `anio` sea un número (sin comillas)
- Reinicia el servidor de desarrollo

### Error de validación

- Verifica que `autores` sea un array (con corchetes)
- Verifica que no haya comas faltantes entre campos
- Verifica que el frontmatter cierre correctamente con `---`

### Problemas de formato

- El campo `anio` debe ser número: `anio: 2024` (sin comillas)
- El campo `autores` debe ser array: `autores: ["Autor1", "Autor2"]`

---

## Próximos Pasos

- [04-ARTICULOS-DIVULGACION.md](./04-ARTICULOS-DIVULGACION.md) - Artículos de divulgación
- [06-GALERIA-SOLAR.md](./06-GALERIA-SOLAR.md) - Gestión de imágenes solares
