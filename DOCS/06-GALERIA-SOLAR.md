# 06. Galería Solar

Documentación del sistema de gestión y visualización de imágenes solares diarias.

---

## Índice

1. [Estructura del Sistema](#estructura-del-sistema)
2. [Formato de Imágenes](#formato-de-imágenes)
3. [Agregar Imágenes Solares](#agregar-imágenes-solares)
4. [Visor de Imágenes](#visor-de-imágenes)
5. [Página de Inicio](#página-de-inicio)
6. [Página de Galería](#página-de-galería)
7. [Eliminar Imágenes](#eliminar-imágenes)

---

## Estructura del Sistema

El sistema de imágenes solares consta de:

1. **Almacenamiento:** Carpeta `public/imagen-solar-diaria/`
2. **Procesamiento:** Código en `src/pages/index.astro` y `src/pages/investigacion/galeria-solar.astro`
3. **Visualización:** Componente `SolarImageViewer.astro`

```
public/
└── imagen-solar-diaria/
    ├── 16-01-2026.jpg   # Formato: DD-MM-AAAA.jpg
    ├── 15-01-2026.jpg
    ├── 14-01-2026.jpg
    └── ...
```

---

## Formato de Imágenes

### Convención de Nombres

**Obligatorio:** Las imágenes deben seguir exactamente este formato:

```
DD-MM-AAAA.jpg
```

Donde:
- `DD` = Día (01-31)
- `MM` = Mes (01-12)
- `AAAA` = Año (4 dígitos)
- Extensión: `.jpg`, `.jpeg` o `.png`

### Ejemplos Válidos

```
✅ 16-01-2026.jpg
✅ 01-12-2024.jpg
✅ 31-12-2023.jpeg
✅ 15-06-2025.png
```

### Ejemplos Inválidos

```
❌ 16/01/2026.jpg      (usar guiones, no barras)
❌ 2026-01-16.jpg      (año primero)
❌ 16-1-2026.jpg       (mes sin cero)
❌ 16_01_2026.jpg      (guiones bajos)
❌ 16-01-2026.JPG      (mayúsculas en extensión)
❌ imagen-solar.jpg    (sin fecha)
```

### Especificaciones Técnicas

| Característica | Recomendación |
|----------------|---------------|
| **Formato** | JPG para fotos, PNG para gráficos |
| **Resolución** | Mínimo 1024x1024, ideal 2048x2048 |
| **Tamaño máximo** | 5MB (optimizar si es mayor) |
| **Proporción** | Cuadrada (1:1) preferible |
| **Color** | RGB, calidad 85-90% |

---

## Agregar Imágenes Solares

### Método 1: Subir Directamente

1. Prepara la imagen con el formato correcto: `DD-MM-AAAA.jpg`
2. Copia la imagen a: `public/imagen-solar-diaria/`
3. (Opcional) Ejecuta `npm run dev` para verificar
4. Compila: `npm run build`

```bash
# Ejemplo en terminal
cp ~/Descargas/16-01-2026.jpg public/imagen-solar-diaria/
```

### Método 2: Vía Git

```bash
# Copiar imagen
cp 16-01-2026.jpg public/imagen-solar-diaria/

# Agregar al repositorio
git add public/imagen-solar-diaria/16-01-2026.jpg
git commit -m "Agregar imagen solar del 16-01-2026"
git push
```

### Verificación

Después de agregar una imagen:

1. Ejecuta `npm run dev`
2. Visita `http://localhost:4321/investigacion/galeria-solar`
3. La imagen debería aparecer ordenada por fecha
4. Haz clic para probar el visor

---

## Visor de Imágenes

El componente `SolarImageViewer.astro` proporciona un visor interactivo.

### Características

- **Navegación:** Flechas izquierda/derecha o teclado (←/→)
- **Zoom:** Acercar/alejar con botones o rueda del ratón
- **Pan:** Arrastrar la imagen cuando hay zoom
- **Responsive:** Funciona en dispositivos móviles
- **Teclado:** Atajos de teclado para todas las funciones

### Atajos de Teclado

| Tecla | Acción |
|-------|--------|
| `ESC` | Cerrar visor |
| `←` | Imagen anterior (más antigua) |
| `→` | Imagen siguiente (más reciente) |
| `+` o `=` | Acercar zoom |
| `-` | Alejar zoom |
| `0` | Resetear zoom |
| Click fuera | Cerrar visor |

### Uso en Páginas

Para usar el visor en cualquier página:

```astro
---
import SolarImageViewer from '../components/SolarImageViewer.astro';

// Preparar datos
const imagenesParaVisor = [
  { path: "/imagen-solar-diaria/16-01-2026.jpg", fechaStr: "16/01/2026", id: "2026-01-16" },
  { path: "/imagen-solar-diaria/15-01-2026.jpg", fechaStr: "15/01/2026", id: "2026-01-15" }
];
---

<!-- Al final del layout -->
<SolarImageViewer imagenes={imagenesParaVisor} />
```

### Abrir el Visor desde Elementos

Para abrir el visor desde cualquier botón o imagen:

```astro
<button data-solar-viewer="/imagen-solar-diaria/16-01-2026.jpg">
  Ver imagen
</button>
```

El atributo `data-solar-viewer` con la ruta de la imagen activa el visor automáticamente.

---

## Página de Inicio

La página de inicio muestra la **imagen solar más reciente** destacada.

### Cómo Funciona

1. El sistema escanea `public/imagen-solar-diaria/`
2. Ordena las imágenes por fecha (más reciente primero)
3. Muestra la primera imagen con información
4. Al hacer clic, abre el visor con todas las imágenes

### Sección en index.astro

```astro
<section class="solar-daily">
  <!-- Muestra imagen más reciente -->
  {imagenMasReciente && (
    <button data-solar-viewer={imagenMasReciente.path}>
      <img src={imagenMasReciente.path} />
    </button>
  )}
</section>

<!-- Visor con todas las imágenes -->
<SolarImageViewer imagenes={imagenesParaVisor} />
```

---

## Página de Galería

La página `/investigacion/galeria-solar` muestra todas las imágenes en una cuadrícula.

### Características

- **Grid responsive:** 4 columnas en desktop, 2 en tablet, 1 en móvil
- **Orden:** De más reciente a más antigua
- **Información:** Muestra la fecha de cada imagen
- **Interacción:** Click para abrir en el visor

### Estructura de la Página

```astro
---
// src/pages/investigacion/galeria-solar.astro

// Obtener todas las imágenes
const imagenesGlob = import.meta.glob('/public/imagen-solar-diaria/*.{jpg,jpeg,png}', { eager: true });

// Procesar y ordenar
const imagenes = Object.keys(imagenesGlob)
  .map(path => {
    // Extraer fecha del nombre de archivo
    const match = filename.match(/^(\d{1,2})-(\d{1,2})-(\d{4})\.(jpg|jpeg|png)$/i);
    // ... procesamiento
  })
  .sort((a, b) => b.fecha.getTime() - a.fecha.getTime());
---

<!-- Grid de imágenes -->
<div class="gallery-grid">
  {imagenes.map((img) => (
    <button data-solar-viewer={img.path}>
      <img src={img.path} alt={`Imagen del ${img.fechaStr}`} />
      <span>{img.fechaStr}</span>
    </button>
  ))}
</div>
```

---

## Eliminar Imágenes

Para eliminar una imagen solar:

### Método 1: Eliminar Archivo

```bash
rm public/imagen-solar-diaria/16-01-2026.jpg
```

### Método 2: Vía Git

```bash
git rm public/imagen-solar-diaria/16-01-2026.jpg
git commit -m "Eliminar imagen solar del 16-01-2026"
git push
```

### Verificación

Después de eliminar:

1. Ejecuta `npm run build`
2. Verifica que no haya errores
3. La imagen ya no debería aparecer en la galería

---

## Respaldo de Imágenes

Es recomendable mantener un respaldo de las imágenes solares:

```bash
# Crear backup
zip -r backup-imagenes-solares-$(date +%Y%m%d).zip public/imagen-solar-diaria/

# O copiar a otra ubicación
cp -r public/imagen-solar-diaria/ /ruta/de/respaldo/
```

---

## Solución de Problemas

### Las imágenes no aparecen

1. Verifica el formato del nombre: `DD-MM-AAAA.jpg`
2. Verifica que estén en `public/imagen-solar-diaria/`
3. Reinicia el servidor de desarrollo
4. Verifica la consola del navegador (F12)

### Error al compilar

```
Cannot find module '/public/imagen-solar-diaria/...'
```

- Verifica que la imagen exista físicamente
- Verifica que la extensión sea correcta (.jpg, .jpeg, .png)
- Verifica permisos de lectura del archivo

### El visor no abre

- Verifica que `SolarImageViewer` esté importado en la página
- Verifica que el atributo `data-solar-viewer` tenga la ruta correcta
- Verifica la consola del navegador por errores de JavaScript

### Imágenes desordenadas

- Verifica que todas las imágenes sigan el formato `DD-MM-AAAA`
- Verifica que las fechas sean válidas
- Las imágenes se ordenan automáticamente de más reciente a más antigua

---

## Estadísticas

Para obtener información sobre las imágenes:

```bash
# Contar imágenes
ls public/imagen-solar-diaria/ | wc -l

# Ver tamaño total
du -sh public/imagen-solar-diaria/

# Ver imágenes más recientes
ls -lt public/imagen-solar-diaria/ | head -10
```

---

## Próximos Pasos

- [03-COMPONENTES.md](./03-COMPONENTES.md) - Documentación de SolarImageViewer
- [07-ESTILOS-Y-DISENO.md](./07-ESTILOS-Y-DISENO.md) - Personalizar estilos
