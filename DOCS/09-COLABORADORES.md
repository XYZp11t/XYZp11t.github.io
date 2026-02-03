# 09. Gestión de Colaboradores

Guía para agregar, editar y gestionar los colaboradores del LACIGE (investigadores internos y externos).

---

## Índice

1. [Estructura de Datos](#estructura-de-datos)
2. [Tipos de Colaboradores](#tipos-de-colaboradores)
3. [Agregar un Colaborador Interno](#agregar-un-colaborador-interno)
4. [Agregar un Colaborador Externo](#agregar-un-colaborador-externo)
5. [Agregar una Nueva Institución](#agregar-una-nueva-institución)
6. [Campos de Metadatos](#campos-de-metadatos)
7. [Ejemplos Completos](#ejemplos-completos)
8. [Solución de Problemas](#solución-de-problemas)

---

## Estructura de Datos

Los colaboradores se organizan en colecciones de contenido de Astro:

```
src/content/colaboradores/
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

---

## Tipos de Colaboradores

### Colaboradores Internos

Investigadores que pertenecen al LACIGE:

- **Académicos**: Profesores, técnicos académicos, investigadores
- **Posdoctorantes**: Estudiantes de posdoctorado

### Colaboradores Externos

Investigadores de otras instituciones que colaboran con el LACIGE:

- IGUM (Instituto de Geofísica unidad Michoacán)
- IRYA (Instituto de Radioastronomía y Astrofísica)
- IG (Instituto de Geofísica)
- Y otras instituciones...

---

## Agregar un Colaborador Interno

### Paso 1: Crear el Archivo

Crea un archivo en `src/content/colaboradores/internos/` con nombre descriptivo:

```
[titulo]-[nombre]-[apellido].md
```

Ejemplos:
- `dr-mario-rodriguez-martinez.md`
- `dr-sinhue-haro-corzo.md`
- `ing-pablo-garcia-cruz.md`

### Paso 2: Contenido del Archivo

```markdown
---
nombre: "Dr. [Nombre Completo]"
imagen: "/colaboradores/nombre-archivo.jpg"  # Opcional
perfil:
  cargo: "Técnico Académico T. C."           # Ver opciones abajo
  areaEstudio: "Descripción del área..."     # Opcional
  oficina: "Edificio A, Oficina 101"         # Opcional
  telefono: "+52 (443) 000-0000"             # Opcional
  email: "correo@enesmorelia.unam.mx"        # Opcional
esEncargado: false                           # true solo para el responsable
orden: 10                                    # Orden de aparición
---

Descripción opcional del investigador.
```

### Paso 3: Opciones de Cargo (Internos)

El campo `cargo` determina la agrupación del investigador:

| Cargo | Grupo |
|-------|-------|
| `"Responsable del Laboratorio"` | Académicos (destacado) |
| `"Técnico Académico T. C."` | Académicos |
| `"Profesor Asociado..."` | Académicos |
| `"Profesor-Investigador..."` | Académicos |
| `"Estudiante de posdoctorado"` | Posdoctorantes |
| `""` (vacío) | Académicos |

---

## Agregar un Colaborador Externo

### Paso 1: Crear el Archivo

Crea un archivo en `src/content/colaboradores/externos/`:

```
[titulo]-[nombre]-[apellido].md
```

Ejemplos:
- `dr-americo-gonzalez-esparza.md`
- `dr-luis-zapata.md`

### Paso 2: Contenido del Archivo

```markdown
---
nombre: "Dr. [Nombre Completo]"
imagen: "/colaboradores/foto.jpg"  # Opcional, dejar '' si no hay
perfil:
  cargo: ""                              # Generalmente vacío para externos
  areaEstudio: "Física Solar..."         # Opcional
  oficina: "Edificio Principal..."       # Opcional
  telefono: "+52 (443) 123-4567"         # Opcional
  email: "correo@institucion.mx"         # Opcional
esEncargado: false
orden: 1
grupoSiglas: "IGUM"                      # ← Siglas de la institución
---
```

### Paso 3: Especificar la Institución

El campo `grupoSiglas` determina a qué institución pertenece el colaborador. Debe coincidir con las siglas definidas en `src/content/colaboradores/grupos/`.

**Siglas disponibles:**

| Institución | Siglas para grupoSiglas |
|-------------|------------------------|
| Instituto de Geofísica U. Michoacán | `"IGUM"` |
| Instituto de Radioastronomía y Astrofísica | `"IRYA"` |
| Instituto de Geofísica | `"IG"` |
| Centro de Alta Tecnología | `"CAT"` |
| Instituto de Ciencias Nucleares | `"ICN"` |
| Universidad de Sonora | `"UNISON"` |
| Instituto de Astronomía - Ensenada | `"IA-ENS"` |
| Universidad Autónoma de Nuevo León | `"UANL"` |
| INAOE | `"INAOE"` |

---

## Agregar una Nueva Institución

Para agregar una nueva institución de colaboración:

### Paso 1: Crear el Grupo

Crea un archivo en `src/content/colaboradores/grupos/`:

```markdown
---
institucion: "Nombre Completo de la Institución"
siglas: "SIGLAS"
tipo: "externo"
orden: 10
---
```

Ejemplo:
```markdown
---
institucion: "Instituto de Geofísica unidad Michoacán"
siglas: "IGUM"
tipo: "externo"
orden: 1
---
```

### Paso 2: Agregar Colaboradores

Crea archivos de colaboradores en `src/content/colaboradores/externos/` usando el campo `grupoSiglas` con las siglas de la nueva institución:

```markdown
---
nombre: "Dr. Nuevo Investigador"
imagen: ""
perfil:
  cargo: ""
  areaEstudio: ""
  oficina: ""
  telefono: ""
  email: ""
esEncargado: false
orden: 1
grupoSiglas: "SIGLAS"  # ← Usa las siglas del nuevo grupo
---
```

---

## Campos de Metadatos

### Campos del Investigador

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `nombre` | `string` | Sí | Nombre completo del investigador |
| `imagen` | `string` | No | Ruta a la imagen (relativa a `/public`) |
| `perfil.cargo` | `string` | No | Cargo o posición |
| `perfil.areaEstudio` | `string` | No | Área de investigación |
| `perfil.oficina` | `string` | No | Ubicación de oficina |
| `perfil.telefono` | `string` | No | Teléfono de contacto |
| `perfil.email` | `string` | No | Correo electrónico |
| `esEncargado` | `boolean` | No | `true` si es el responsable del laboratorio |
| `orden` | `number` | No | Posición en la lista (menor = primero) |
| `grupoSiglas` | `string` | Solo externos | Siglas del grupo/institución (ej: `"IGUM"`, `"IRYA"`)

### Campos del Grupo

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `institucion` | `string` | Sí | Nombre completo de la institución |
| `siglas` | `string` | Sí | Siglas o abreviatura |
| `tipo` | `enum` | Sí | `"interno"` o `"externo"` |
| `orden` | `number` | No | Posición en la lista |

---

## Ejemplos Completos

### Ejemplo: Responsable del Laboratorio

```markdown
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

### Ejemplo: Académico con Información Completa

```markdown
---
nombre: "Dr. Sinhué A. R. Haro Corzo"
imagen: "/colaboradores/DrSinhue.jpg"
perfil:
  cargo: "Técnico Académico T. C."
  areaEstudio: "Instrumentación espacial y análisis de datos del entorno heliosférico."
  oficina: "Edificio A, Oficina 102"
  telefono: "+52 (443) 000-0000"
  email: "sinhue.haro@lacige.unam.mx"
esEncargado: false
orden: 2
---
```

### Ejemplo: Posdoctorante

```markdown
---
nombre: "Dra. María García López"
imagen: ""
perfil:
  cargo: "Estudiante de posdoctorado"
  areaEstudio: "Física solar y clima espacial"
  oficina: "Edificio B, Oficina 205"
  telefono: ""
  email: "m.garcia@lacige.unam.mx"
esEncargado: false
orden: 1
---
```

### Ejemplo: Colaborador Externo Completo

```markdown
---
nombre: "Dr. Américo González Esparza"
imagen: ""
perfil:
  cargo: ""
  areaEstudio: "Física Solar y Clima Espacial"
  oficina: "Edificio Principal, Oficina 201"
  telefono: "+52 (443) 123-4567"
  email: "agonsalez@igeofisica.unam.mx"
esEncargado: false
orden: 1
grupoSiglas: "IGUM"
---
```

### Ejemplo: Colaborador Externo Mínimo

```markdown
---
nombre: "Dr. Ernesto Aguilar Rodríguez"
imagen: ""
perfil:
  cargo: ""
  areaEstudio: ""
  oficina: ""
  telefono: ""
  email: ""
esEncargado: false
orden: 2
grupoSiglas: "IGUM"
---
```

---

## Solución de Problemas

### El colaborador no aparece

- Verifica que el archivo tenga extensión `.md`
- Revisa que el frontmatter (entre `---`) esté bien formado
- Asegúrate de que no haya errores de sintaxis YAML
- Para externos: verifica que el campo `grupoSiglas` coincida exactamente con las siglas del grupo

### El colaborador aparece en el grupo incorrecto

**Internos:** Verifica que el campo `cargo` contenga el texto correcto:
- `"posdoctorado"` → Grupo Posdoctorantes
- Cualquier otro → Grupo Académicos

**Externos:** Verifica que el campo `grupoSiglas` coincida exactamente con las siglas definidas en el archivo del grupo (en `src/content/colaboradores/grupos/`).

### Error de validación

- Todos los campos en `perfil` deben ser strings (usar `''` para vacío)
- `esEncargado` debe ser `true` o `false` (sin comillas)
- `orden` debe ser un número

### Las imágenes no se muestran

- Guarda las imágenes en `/public/colaboradores/`
- Usa rutas absolutas: `/colaboradores/nombre-imagen.jpg`
- Formatos soportados: jpg, png, webp
- Deja el campo como `''` si no hay imagen

---

## Template Base

### Template para Colaborador Interno

```markdown
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

Descripción opcional del investigador.
```

### Template para Colaborador Externo

```markdown
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

Descripción opcional del investigador.
```

---

## Notas Importantes

1. **Hot Reload**: En modo desarrollo (`npm run dev`), los cambios se reflejan inmediatamente
2. **Sin rebuild**: No es necesario hacer `npm run build` para agregar colaboradores
3. **Orden**: Usa `orden: 1` para el responsable, números consecutivos para el resto
4. **Campos vacíos**: Todos los campos pueden estar vacíos (`''`), pero deben existir
5. **Imágenes**: Las imágenes deben guardarse en `/public/colaboradores/`

---

## Próximos Pasos

- [05-PUBLICACIONES-CIENTIFICAS.md](./05-PUBLICACIONES-CIENTIFICAS.md) - Agregar publicaciones
- [04-ARTICULOS-DIVULGACION.md](./04-ARTICULOS-DIVULGACION.md) - Crear artículos de divulgación
