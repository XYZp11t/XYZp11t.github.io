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
grupoSiglas: "IGUM"                         # ← Siglas de la institución
---
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

Luego, al crear colaboradores para esta institución, usa el campo `grupoSiglas` con las siglas definidas:

```yaml
---
nombre: "Dr. Nuevo Investigador"
# ... otros campos ...
grupoSiglas: "SIGLAS"  # ← Usa las siglas del nuevo grupo
---
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
| `grupoSiglas` | string | Solo externos | Siglas de la institución (ej: `"IGUM"`, `"IRYA"`) |

### Grupo

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `institucion` | string | ✅ | Nombre completo de la institución |
| `siglas` | string | ✅ | Siglas o abreviatura |
| `tipo` | enum | ✅ | `"interno"` o `"externo"` |
| `orden` | number | | Posición en la lista |

## Templates

### Template Colaborador Interno

```yaml
---
nombre: "Dr. [Nombre Completo]"
imagen: ""
perfil:
  cargo: "Técnico Académico T. C."
  areaEstudio: ""
  oficina: ""
  telefono: ""
  email: ""
esEncargado: false
orden: 999
---
```

### Template Colaborador Externo

```yaml
---
nombre: "Dr. [Nombre Completo]"
imagen: ""
perfil:
  cargo: ""
  areaEstudio: ""
  oficina: ""
  telefono: ""
  email: ""
esEncargado: false
orden: 999
grupoSiglas: "IGUM"  # Cambia por las siglas de la institución
---
```

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

**Internos:** Verifica que el campo `cargo` contenga el texto correcto:
- `"posdoctorado"` → Grupo Posdoctorantes
- Cualquier otro → Grupo Académicos

**Externos:** Verifica que el campo `grupoSiglas` coincida exactamente con las siglas definidas en el archivo del grupo (en `src/content/colaboradores/grupos/`).

### Error de validación
- Todos los campos en `perfil` deben ser strings (usar `''` para vacío)
- `esEncargado` debe ser `true` o `false` (sin comillas)
- `orden` debe ser un número
- `grupoSiglas` debe coincidir exactamente con las siglas del grupo
