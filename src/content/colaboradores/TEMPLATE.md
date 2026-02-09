# Templates para Colaboradores

## Template: Colaborador Interno (Básico)

Copia este template para crear un colaborador interno sin biografía detallada:

```markdown
---
nombre: "Dr. [Nombre Completo]"
imagen: ""
perfil:
  cargo: "Técnico Académico T. C."  # O "Profesor...", "Estudiante de posdoctorado"
  areaEstudio: ""
  oficina: ""
  telefono: ""
  email: ""
esEncargado: false
orden: 999
---
```

**Notas para internos:**
- El campo `cargo` determina el grupo: `"posdoctorado"` → Posdoctorantes, cualquier otro → Académicos
- Guarda el archivo en: `src/content/colaboradores/internos/`

---

## Template: Colaborador Interno (Con Biografía Completa)

Copia este template para crear un colaborador con biografía y página dedicada:

```markdown
---
nombre: "Dr. [Nombre Completo]"
imagen: "/colaboradores/nombre-foto.jpg"
perfil:
  cargo: "Técnico Académico T. C."
  areaEstudio: "Descripción del área de investigación"
  oficina: "Edificio A, Oficina 101"
  telefono: "(443) 000-0000"
  email: "correo@enesmorelia.unam.mx"
esEncargado: false
orden: 10
---

Escribe la biografía directamente, usando párrafos simples. No uses estilos 
especiales de introducción. Solo información real y verificada del investigador.

Puedes agregar tantos párrafos como necesites para describir su trayectoria,
formación académica, premios, membresías, etc.

## Líneas de Investigación

Describe las líneas de investigación (solo si aplica).

<div class="research-areas">
  <span class="research-tag">Línea 1</span>
  <span class="research-tag">Línea 2</span>
  <span class="research-tag">Línea 3</span>
</div>

## Publicaciones Selectas

<div class="publication-list">
  <div class="publication-item">
    <span class="pub-number">1</span>
    <div class="pub-content">
      <span class="pub-title">Título completo del artículo científico</span>
      <span class="pub-authors">Autor A, Autor B, Autor C</span>
      <span class="pub-journal">Nombre de la Revista, Volumen, Páginas (Año)</span>
      <a class="pub-link" href="https://doi.org/xxxxx" target="_blank" rel="noopener">DOI: xxxxx</a>
    </div>
  </div>

  <div class="publication-item">
    <span class="pub-number">2</span>
    <div class="pub-content">
      <span class="pub-title">Otra publicación importante</span>
      <span class="pub-authors">Autor D, Autor E</span>
      <span class="pub-journal">Otra Revista, Volumen, Páginas (Año)</span>
      <a class="pub-link" href="https://doi.org/yyyyy" target="_blank" rel="noopener">DOI: yyyyy</a>
    </div>
  </div>
</div>

## Proyectos

<div class="project-list">
  <div class="project-item">
    <span class="project-period">2020 – Actualidad</span>
    <p>Título del proyecto de investigación</p>
    <p class="project-funding">Descripción breve, institución financiadora...</p>
  </div>

  <div class="project-item">
    <span class="project-period">2018 – 2023</span>
    <p>Otro proyecto relevante</p>
    <p class="project-funding">Descripción...</p>
  </div>
</div>
```

---

## Template: Colaborador Externo (Básico)

Copia este template para crear un colaborador externo:

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
```

**Notas para externos:**
- El campo `grupoSiglas` debe coincidir con las siglas del grupo en `src/content/colaboradores/grupos/`
- Guarda el archivo en: `src/content/colaboradores/externos/`

---

## Template: Colaborador Externo (Con Biografía)

```markdown
---
nombre: "Dr. [Nombre Completo]"
imagen: "/colaboradores/nombre-foto.jpg"
perfil:
  cargo: "Investigador Titular"
  areaEstudio: "Área de especialización"
  oficina: "Edificio Principal, Oficina 201"
  telefono: "(443) 000-0000"
  email: "correo@institucion.mx"
esEncargado: false
orden: 10
grupoSiglas: "IGUM"  # Cambia por las siglas de la institución
---

Biografía del investigador usando párrafos simples.

## Líneas de Investigación

<div class="research-areas">
  <span class="research-tag">Área 1</span>
  <span class="research-tag">Área 2</span>
</div>

## Publicaciones Recientes

<div class="publication-list">
  <div class="publication-item">
    <span class="pub-number">1</span>
    <div class="pub-content">
      <span class="pub-title">Título de la publicación</span>
      <span class="pub-authors">Autores</span>
      <span class="pub-journal">Revista, Año</span>
      <a class="pub-link" href="https://doi.org/...">DOI: ...</a>
    </div>
  </div>
</div>
```

---

## Siglas disponibles para colaboradores externos

| Sigla | Institución |
|-------|-------------|
| `IGUM` | Instituto de Geofísica unidad Michoacán |
| `IRYA` | Instituto de Radioastronomía y Astrofísica |
| `IG` | Instituto de Geofísica |
| `CAT` | Centro de Alta Tecnología |
| `ICN` | Instituto de Ciencias Nucleares |
| `UNISON` | Universidad de Sonora |
| `IA-ENS` | Instituto de Astronomía - Ensenada, B.C. |
| `UANL` | Universidad Autónoma de Nuevo León |
| `INAOE` | Instituto Nacional de Astrofísica, Óptica y Electrónica |

---

## Guía de Clases CSS para Biografías

### Biografía
Escribe directamente los párrafos de texto. No uses contenedores especiales ni estilos de introducción.

```markdown
Escribe la biografía directamente así. Párrafos simples sin divs ni clases especiales.
```

### Líneas de investigación (tags separados por puntos)
```html
<div class="research-areas">
  <span class="research-tag">Física Solar</span>
  <span class="research-tag">Clima Espacial</span>
  <span class="research-tag">MHD</span>
</div>
```

### Publicaciones (numeración simple)
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

### Proyectos (compactos, sin cajas grandes)
```html
<div class="project-list">
  <div class="project-item">
    <span class="project-period">2022 – Actualidad</span>
    <p>Nombre del proyecto</p>
    <p class="project-funding">Información de financiamiento...</p>
  </div>
</div>
```

---

## Agregar CV

Para agregar un enlace al CV en la página de biografía:

1. Guarda el archivo PDF en: `/public/CVs/`
2. En el frontmatter, agrega el campo `cv` con la ruta al archivo:

```yaml
---
nombre: "Dr. [Nombre Completo]"
imagen: "/colaboradores/nombre-foto.jpg"
cv: "/CVs/nombre-del-cv.pdf"  # ← Agrega esta línea
perfil:
  cargo: "..."
  ...
---
```

3. Si el campo `cv` está vacío (`""`) o no existe, no se mostrará el botón
4. El CV se abre en una pestaña nueva

Ejemplo de estructura de archivos:
```
public/
├── CVs/
│   ├── cv-mario-rodriguez.pdf
│   └── cv-jose-juan-gonzalez.pdf
└── colaboradores/
    └── DrMarioRod.jpg
```

---

## Notas importantes

1. **La información de contacto va en el frontmatter**: No repitas el email o teléfono en el body del markdown, ya que se muestra automáticamente en:
   - La tarjeta del colaborador en `/colaboradores`
   - El sidebar de la página de biografía individual

2. **El botón "Ver biografía" aparece automáticamente**: Si el archivo tiene contenido después del frontmatter (más de 10 caracteres), se mostrará el botón en la tarjeta.

3. **Página dedicada automática**: Cada colaborador con biografía tendrá su propia página en `/colaborador/nombre-del-archivo`.

4. **Imágenes**: Guarda las fotos en `/public/colaboradores/` y usa la ruta `/colaboradores/nombre-archivo.jpg`.

5. **CVs**: Guarda los archivos PDF en `/public/CVs/` para habilitar la descarga desde la página de biografía.

6. **Enlaces**: Usa siempre `target="_blank" rel="noopener"` para enlaces externos.

7. **Orden de aparición**: Los colaboradores se ordenan por el campo `orden` (menor número = aparece primero).

8. **Encargado**: Solo un colaborador debe tener `esEncargado: true` (el responsable del laboratorio).

9. **No inventes contenido**: Solo incluye información real y verificada de cada colaborador.

10. **Diseño limpio**: Prefiere diseños compactos y profesionales. Evita cajas grandes o estilos llamativos.
