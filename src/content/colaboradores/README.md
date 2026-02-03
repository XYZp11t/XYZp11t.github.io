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
└── README.md                  # Este archivo
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

Descripción opcional del investigador (aparece como contenido del markdown).
```

**Ejemplo completo:**

```yaml
---
nombre: "Dr. Mario Rodríguez Martínez"
imagen: "/colaboradores/DrMarioRod.jpg"
perfil:
  cargo: "Responsable del Laboratorio"
  areaEstudio: ""
  oficina: ""
  telefono: ""
  email: "mrodriguez@enesmorelia.unam.mx"
esEncargado: true
orden: 1
---

Responsable del Laboratorio LACIGE.
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
---
```

**Importante:** El nombre del archivo debe contener palabras clave que permitan asociarlo a su institución. Por ejemplo:
- `dr-americo-gonzalez.md` → se asocia automáticamente a IGUM
- `dr-luis-zapata.md` → se asocia automáticamente a IRYA

Las palabras clave de asociación están definidas en `src/pages/colaboradores.astro`.

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

Luego actualiza el mapeo en `src/pages/colaboradores.astro` para asociar investigadores a este nuevo grupo:

```typescript
const mapeoInstituciones: Record<string, string[]> = {
  // ... grupos existentes ...
  'SIGLAS': ['palabra-clave-1', 'palabra-clave-2'],
};
```

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

### Grupo

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `institucion` | string | ✅ | Nombre completo de la institución |
| `siglas` | string | ✅ | Siglas o abreviatura |
| `tipo` | enum | ✅ | `"interno"` o `"externo"` |
| `orden` | number | | Posición en la lista |

## Consejos

1. **Imágenes**: Guarda las imágenes en `/public/colaboradores/` con nombres descriptivos.
2. **Orden**: Usa `orden: 1` para el responsable, `orden: 2-10` para académicos principales, etc.
3. **Campos vacíos**: Todos los campos pueden estar vacíos (`''`), pero deben existir en el archivo.
4. **Desarrollo**: En modo desarrollo (`npm run dev`), los cambios se reflejan inmediatamente sin necesidad de rebuild.

## Solución de Problemas

### Los cambios no aparecen
- Verifica que el archivo tenga extensión `.md`
- Revisa que el frontmatter (entre `---`) esté bien formado
- Asegúrate de que no haya errores de sintaxis YAML

### Un investigador no aparece en el grupo correcto
- Verifica que el nombre del archivo contenga alguna de las palabras clave definidas en el mapeo
- Revisa que el grupo tenga el `tipo` correcto ("interno" o "externo")

### Error de validación
- Todos los campos en `perfil` deben ser strings (usar `''` para vacío)
- `esEncargado` debe ser `true` o `false` (sin comillas)
- `orden` debe ser un número
