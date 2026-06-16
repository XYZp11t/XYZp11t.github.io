# 06. Galería Solar

Documentación del sistema de gestión y visualización de imágenes solares diarias.

---

## Índice

1. [Estructura del Sistema](#estructura-del-sistema)
2. [Formato de Imágenes](#formato-de-imágenes)
3. [Agregar Imágenes (Desarrollo)](#agregar-imágenes-desarrollo)
4. [Agregar Imágenes (Producción con Apache)](#agregar-imágenes-producción-con-apache)
5. [Visor de Imágenes](#visor-de-imágenes)
6. [Página de Inicio](#página-de-inicio)
7. [Página de Galería](#página-de-galería)
8. [Eliminar Imágenes](#eliminar-imágenes)

---

## Estructura del Sistema

El sistema de imágenes solares consta de:

1. **Almacenamiento fuente:** Carpeta `public/imagen-solar-diaria/` (en el repositorio)
2. **Almacenamiento producción:** Carpeta `dist/imagen-solar-diaria/` (generado por el build)
3. **Procesamiento:** Código en `src/pages/index.astro` y `src/pages/investigacion/galeria-solar.astro`
4. **Visualización:** Componente `SolarImageViewer.astro`

```
# Estructura en desarrollo (repositorio)
public/
└── imagen-solar-diaria/
    ├── 16-01-2026.jpg   # Formato: DD-MM-AAAA.jpg
    ├── 15-01-2026.jpg
    └── ...

# Estructura en producción (después de npm run build)
dist/
└── imagen-solar-diaria/
    ├── 16-01-2026.jpg   # Copiado desde public/
    ├── 15-01-2026.jpg
    └── ...
```

**Flujo de imágenes:**
1. Imágenes se guardan en `public/imagen-solar-diaria/`
2. Al ejecutar `npm run build`, Astro copia las imágenes a `dist/imagen-solar-diaria/`
3. Apache sirve el contenido de la carpeta `dist/`
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

## Agregar Imágenes (Desarrollo)

Durante el desarrollo local, cuando tienes acceso al código fuente:

### Método 1: Copiar Directamente

```bash
# Copiar imagen a la carpeta public
cp ~/Descargas/16-01-2026.jpg public/imagen-solar-diaria/

# Verificar en desarrollo
npm run dev

# Compilar para producción
npm run build
```

### Método 2: Vía Git (Recomendado para proyectos versionados)

```bash
# Copiar imagen
cp 16-01-2026.jpg public/imagen-solar-diaria/

# Agregar al repositorio
git add public/imagen-solar-diaria/16-01-2026.jpg
git commit -m "Agregar imagen solar del 16-01-2026"
git push

# Desplegar (si tienes CI/CD configurado)
# o compilar manualmente
npm run build
```

---

## Agregar Imágenes (Producción con Apache)

Cuando el sitio ya está en producción con Apache apuntando a `/dist`:

### ⚠️ Importante: Entender el Flujo

```
┌─────────────────┐     npm run build      ┌─────────────────┐
│   public/       │  ───────────────────►  │     dist/       │
│   (fuente)      │                        │  (producción)   │
│                 │                        │                 │
│ imagen-solar/   │     Astro copia        │ imagen-solar/   │
│   ├── img1.jpg  │     las imágenes       │   ├── img1.jpg  │
│   └── img2.jpg  │     automáticamente    │   └── img2.jpg  │
└─────────────────┘                        └─────────────────┘
        ▲                                          │
        │                                          ▼
        │                                   ┌──────────────┐
        │                                   │    Apache    │
        │                                   │  (sirve web) │
        │                                   └──────────────┘
        │
   REPOSITORIO GIT
```

**Reglas importantes:**
- Apache sirve desde `dist/`, NO desde `public/`
- Cada vez que ejecutas `npm run build`, el contenido de `dist/` se regenera
- Las imágenes deben persistir en `public/` para que el build las incluya

---

### Opción 1: Subir al Repositorio y Recompilar (Recomendada)

**Cuándo usar:** Tienes acceso al repositorio y puedes hacer deploy.

```bash
# En tu máquina local o servidor con acceso al código

# 1. Navegar al proyecto
cd /ruta/al/proyecto/web_lacige

# 2. Copiar la nueva imagen a public/
cp /ruta/de/la/nueva-imagen.jpg public/imagen-solar-diaria/16-02-2026.jpg

# 3. (Opcional) Si usas git, agregar al repo
git add public/imagen-solar-diaria/16-02-2026.jpg
git commit -m "Agregar imagen solar 16-02-2026"
git push

# 4. Recompilar el proyecto
npm run build

# 5. Verificar que la imagen está en dist/
ls -la dist/imagen-solar-diaria/

# 6. Apache ya sirve automáticamente desde dist/
# No necesitas reiniciar Apache
```

---

### Opción 2: Subir Directamente a Producción (Temporal)

**Cuándo usar:** Necesitas que la imagen aparezca inmediatamente y no puedes recompilar ahora.

**Advertencia:** Esta imagen se perderá si vuelves a hacer `npm run build` sin haberla agregado a `public/`.

```bash
# En el servidor de producción

# 1. Copiar imagen directamente a dist/
cp /tmp/nueva-imagen.jpg /var/www/lacige/dist/imagen-solar-diaria/16-02-2026.jpg

# 2. Verificar permisos
chmod 644 /var/www/lacige/dist/imagen-solar-diaria/16-02-2026.jpg
chown www-data:www-data /var/www/lacige/dist/imagen-solar-diaria/16-02-2026.jpg

# 3. La imagen está disponible inmediatamente
# URL: https://tusitio.com/imagen-solar-diaria/16-02-2026.jpg
```

**Para hacer permanente esta imagen:**
```bash
# También copiar a public/ para que persista en próximos builds
cp /tmp/nueva-imagen.jpg /var/www/lacige/public/imagen-solar-diaria/16-02-2026.jpg
```

---

### Opción 3: Configurar Directorio Persistente en Apache

**Cuándo usar:** Quieres poder subir imágenes sin recompilar y sin riesgo de perderlas.

Configura Apache para servir imágenes desde una ubicación persistente:

```apache
# /etc/apache2/sites-available/lacige.conf

<VirtualHost *:80>
    ServerName lacige.unam.mx
    DocumentRoot /var/www/lacige/dist
    
    # Alias para imágenes solares (persistente)
    Alias /imagen-solar-diaria /var/www/lacige/imagenes-solares-persistentes
    
    <Directory /var/www/lacige/imagenes-solares-persistentes>
        Require all granted
        Options -Indexes
    </Directory>
    
    # El resto del sitio desde dist/
    <Directory /var/www/lacige/dist>
        Require all granted
    </Directory>
</VirtualHost>
```

Luego:
```bash
# Crear carpeta persistente
mkdir -p /var/www/lacige/imagenes-solares-persistentes

# Copiar imágenes existentes
cp /var/www/lacige/dist/imagen-solar-diaria/* /var/www/lacige/imagenes-solares-persistentes/

# Ahora puedes subir imágenes aquí sin recompilar
cp nueva-imagen.jpg /var/www/lacige/imagenes-solares-persistentes/16-02-2026.jpg

# Recargar Apache
sudo systemctl reload apache2
```

---

### Opción 4: Usar SFTP/SCP desde tu máquina local

Subir imágenes directamente al servidor:

```bash
# Usando scp
scp 16-02-2026.jpg usuario@servidor:/var/www/lacige/public/imagen-solar-diaria/

# Luego conectar por SSH y recompilar
ssh usuario@servidor
cd /var/www/lacige
npm run build
```

O si configuras el directorio persistente (Opción 3):
```bash
scp 16-02-2026.jpg usuario@servidor:/var/www/lacige/imagenes-solares-persistentes/
```

---

### Resumen: Qué Opción Elegir

| Situación | Opción Recomendada |
|-----------|-------------------|
| Tienes acceso al repo y puedes hacer deploy | **Opción 1:** Subir a `public/` + `npm run build` |
| Necesitas resultado inmediato, sin acceso al repo | **Opción 2:** Subir directamente a `dist/` (temporal) |
| Subirás imágenes frecuentemente | **Opción 3:** Configurar directorio persistente en Apache |
| Trabajas desde tu máquina local | **Opción 4:** SFTP/SCP + recompilar |

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

1. El sistema escanea las imágenes disponibles
2. Ordena las imágenes por fecha (más reciente primero)
3. Muestra la primera imagen con información
4. Al hacer clic, abre el visor con todas las imágenes

**Nota sobre producción:** La imagen mostrada depende de las imágenes presentes en `dist/imagen-solar-diaria/` (o tu directorio persistente si configuraste Opción 3).

---

## Página de Galería

La página `/investigacion/galeria-solar` muestra todas las imágenes en una cuadrícula.

### Características

- **Grid responsive:** 4 columnas en desktop, 2 en tablet, 1 en móvil
- **Orden:** De más reciente a más antigua
- **Información:** Muestra la fecha de cada imagen
- **Interacción:** Click para abrir en el visor

---

## Eliminar Imágenes

### En Desarrollo

```bash
rm public/imagen-solar-diaria/16-01-2026.jpg
npm run build
```

### En Producción

```bash
# Opción A: Eliminar de public/ y recompilar
rm /var/www/lacige/public/imagen-solar-diaria/16-01-2026.jpg
cd /var/www/lacige && npm run build

# Opción B: Eliminar directamente de dist/ (temporal)
rm /var/www/lacige/dist/imagen-solar-diaria/16-01-2026.jpg

# Opción C: Si usas directorio persistente
rm /var/www/lacige/imagenes-solares-persistentes/16-01-2026.jpg
```

---

## Respaldo de Imágenes

Es recomendable mantener un respaldo de las imágenes solares:

```bash
# Crear backup desde public/ (fuente original)
zip -r backup-imagenes-solares-$(date +%Y%m%d).zip public/imagen-solar-diaria/

# O desde el directorio persistente (si usas Opción 3)
zip -r backup-imagenes-solares-$(date +%Y%m%d).zip /var/www/lacige/imagenes-solares-persistentes/
```

---

## Solución de Problemas

### Las imágenes no aparecen

1. Verifica el formato del nombre: `DD-MM-AAAA.jpg`
2. Verifica que estén en la ubicación correcta:
   - Desarrollo: `public/imagen-solar-diaria/`
   - Producción: `dist/imagen-solar-diaria/` (o tu directorio persistente)
3. Verifica permisos de lectura: `chmod 644 imagen.jpg`
4. Verifica que Apache tenga acceso: `chown www-data:www-data imagen.jpg`
5. Reinicia Apache si cambiaste la configuración: `sudo systemctl restart apache2`

### Error 404 al acceder a imágenes

```
404 Not Found: /imagen-solar-diaria/16-01-2026.jpg
```

- Verifica que la imagen exista en el servidor
- Si usas directorio persistente (Opción 3), verifica el `Alias` en Apache
- Verifica que la ruta en el navegador coincida con la ubicación física

### Las imágenes nuevas no aparecen después de subirlas

- Si subiste a `dist/` directamente: Verifica que no se haya sobrescrito con un nuevo build
- Si subiste a `public/`: Recuerda ejecutar `npm run build` para copiar a `dist/`
- Limpia la caché del navegador (Ctrl+Shift+R)

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

## Checklist para Agregar Imágenes en Producción

- [ ] La imagen sigue el formato `DD-MM-AAAA.jpg`
- [ ] Decidí qué opción usar (1, 2, 3 o 4)
- [ ] Copié la imagen a la ubicación correcta
- [ ] (Opción 1) Ejecuté `npm run build` para compilar
- [ ] (Opción 2) También copié a `public/` para persistencia
- [ ] Verifiqué permisos: `chmod 644 imagen.jpg`
- [ ] Verifiqué propietario: `chown www-data:www-data imagen.jpg` (si aplica)
- [ ] Probé la URL en el navegador
- [ ] Verifiqué que aparece en la galería

---

## Próximos Pasos

- [03-COMPONENTES.md](./03-COMPONENTES.md) - Documentación de SolarImageViewer
- [07-ESTILOS-Y-DISENO.md](./07-ESTILOS-Y-DISENO.md) - Personalizar estilos
