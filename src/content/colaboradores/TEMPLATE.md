# Templates para Colaboradores

## Template: Colaborador Interno

Copia este template para crear un colaborador interno (académico o posdoctorante):

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

Descripción opcional del investigador.
```

**Notas para internos:**
- El campo `cargo` determina el grupo: `"posdoctorado"` → Posdoctorantes, cualquier otro → Académicos
- Guarda el archivo en: `src/content/colaboradores/internos/`

---

## Template: Colaborador Externo

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

Descripción opcional del investigador.
```

**Notas para externos:**
- El campo `grupoSiglas` debe coincidir con las siglas del grupo en `src/content/colaboradores/grupos/`
- Guarda el archivo en: `src/content/colaboradores/externos/`

**Siglas disponibles:**
- `IGUM` - Instituto de Geofísica unidad Michoacán
- `IRYA` - Instituto de Radioastronomía y Astrofísica
- `IG` - Instituto de Geofísica
- `CAT` - Centro de Alta Tecnología
- `ICN` - Instituto de Ciencias Nucleares
- `UNISON` - Universidad de Sonora
- `IA-ENS` - Instituto de Astronomía - Ensenada, B.C.
- `UANL` - Universidad Autónoma de Nuevo León
- `INAOE` - Instituto Nacional de Astrofísica, Óptica y Electrónica
