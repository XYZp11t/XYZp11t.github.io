# 07. Estilos y Diseño

Guía completa del sistema de estilos del sitio LACIGE, incluyendo colores, tipografía, espaciado y componentes de diseño.

---

## Índice

1. [Sistema de Colores](#sistema-de-colores)
2. [Tipografía](#tipografía)
3. [Espaciado](#espaciado)
4. [Bordes y Sombras](#bordes-y-sombras)
5. [Contenedores](#contenedores)
6. [Botones](#botones)
7. [Clases de Utilidad](#clases-de-utilidad)
8. [Personalización](#personalización)

---

## Sistema de Colores

Todos los colores se definen como **CSS Custom Properties** en `src/styles/global.css`.

### Colores Principales

| Variable | Valor | Uso |
|----------|-------|-----|
| `--color-primary` | `#003D79` | Azul institucional, encabezados, enlaces |
| `--color-primary-dark` | `#002a54` | Hover states, fondos oscuros |
| `--color-primary-light` | `#0056a8` | Acentos claros |
| `--color-accent` | `#D59F0F` | Dorado, botones CTA, énfasis |
| `--color-accent-dark` | `#b8890d` | Hover de acentos |
| `--color-accent-light` | `#e8b52a` | Estados claros |
| `--color-earth` | `#84754E` | Marrón tierra, textos secundarios |

### Colores Neutros

| Variable | Valor | Uso |
|----------|-------|-----|
| `--color-white` | `#FFFFFF` | Fondos claros, texto sobre oscuro |
| `--color-off-white` | `#F8F6F3` | Fondo principal del sitio |
| `--color-gray-100` | `#F1EDE8` | Fondos secundarios, tarjetas |
| `--color-gray-200` | `#E3DDD4` | Bordes, separadores |
| `--color-gray-300` | `#C9C1B4` | Bordes sutiles |
| `--color-gray-400` | `#9E9588` | Texto deshabilitado |
| `--color-gray-500` | `#73695C` | Texto secundario |
| `--color-gray-600` | `#4D4538` | Texto cuerpo |
| `--color-gray-700` | `#2D2820` | Texto principal |
| `--color-black` | `#1A1612` | Texto muy oscuro |

### Uso de Colores

```css
/* En CSS */
.elemento {
  background-color: var(--color-primary);
  color: var(--color-white);
  border: 1px solid var(--color-gray-200);
}

/* Hover */
.elemento:hover {
  background-color: var(--color-primary-dark);
}
```

---

## Tipografía

### Fuentes

| Variable | Fuente | Uso |
|----------|--------|-----|
| `--font-display` | 'Playfair Display', serif | Títulos, encabezados |
| `--font-body` | 'Source Sans 3', sans-serif | Cuerpo de texto, UI |

### Tamaños de Título

| Elemento | Tamaño | Peso |
|----------|--------|------|
| `h1` | `clamp(2.25rem, 5vw, 3.5rem)` | 700 |
| `h2` | `clamp(1.75rem, 4vw, 2.5rem)` | 600 |
| `h3` | `clamp(1.375rem, 3vw, 1.75rem)` | 600 |
| `h4` | `1.25rem` | 600 |

### Tamaños de Texto

| Clase/Elemento | Tamaño | Uso |
|----------------|--------|-----|
| Cuerpo | `1rem` (16px) | Texto general |
| `.text-sm` | `0.875rem` (14px) | Texto pequeño, metadata |
| `.text-xs` | `0.75rem` (12px) | Etiquetas, subtítulos |
| `.text-lg` | `1.125rem` (18px) | Énfasis, introducciones |
| `.text-xl` | `1.25rem` (20px) | Destacados |

### Uso Tipográfico

```css
/* Título de página */
.page-title {
  font-family: var(--font-display);
  font-size: clamp(2.25rem, 5vw, 3.5rem);
  color: var(--color-primary);
}

/* Texto de cuerpo */
.body-text {
  font-family: var(--font-body);
  font-size: 1rem;
  line-height: 1.7;
  color: var(--color-gray-600);
}
```

---

## Espaciado

El sistema usa una escala basada en `rem` (root em).

| Variable | Valor | Píxeles |
|----------|-------|---------|
| `--space-xs` | `0.25rem` | 4px |
| `--space-sm` | `0.5rem` | 8px |
| `--space-md` | `1rem` | 16px |
| `--space-lg` | `1.5rem` | 24px |
| `--space-xl` | `2rem` | 32px |
| `--space-2xl` | `3rem` | 48px |
| `--space-3xl` | `4rem` | 64px |
| `--space-4xl` | `6rem` | 96px |

### Uso de Espaciado

```css
.componente {
  padding: var(--space-lg);
  margin-bottom: var(--space-xl);
  gap: var(--space-md);
}
```

---

## Bordes y Sombras

### Bordes Redondeados

| Variable | Valor | Uso |
|----------|-------|-----|
| `--radius-sm` | `4px` | Botones, inputs pequeños |
| `--radius-md` | `8px` | Tarjetas, contenedores |
| `--radius-lg` | `16px` | Tarjetas grandes, modales |
| `--radius-full` | `9999px` | Elementos circulares (badges, avatares) |

### Sombras

| Variable | Valor | Uso |
|----------|-------|-----|
| `--shadow-sm` | `0 1px 3px rgba(0, 61, 121, 0.08)` | Estados sutiles |
| `--shadow-md` | `0 4px 12px rgba(0, 61, 121, 0.1)` | Tarjetas default |
| `--shadow-lg` | `0 8px 24px rgba(0, 61, 121, 0.12)` | Hover de tarjetas |
| `--shadow-xl` | `0 16px 48px rgba(0, 61, 121, 0.16)` | Modales, dropdowns |

---

## Contenedores

### Contenedor Principal

```css
.container {
  width: 100%;
  max-width: var(--container-max);  /* 1280px */
  margin: 0 auto;
  padding: 0 var(--space-lg);       /* 0 1.5rem */
}
```

### Contenedor Estrecho

```css
.container--narrow {
  max-width: var(--container-narrow);  /* 800px */
}
```

### Uso

```html
<div class="container">
  <!-- Contenido de ancho completo -->
</div>

<div class="container container--narrow">
  <!-- Contenido de texto, artículos -->
</div>
```

---

## Botones

### Clases de Botones

| Clase | Apariencia | Uso |
|-------|------------|-----|
| `.btn` | Base | Todas las variantes |
| `.btn--primary` | Azul sólido | Acciones principales |
| `.btn--secondary` | Borde azul | Acciones secundarias |
| `.btn--accent` | Dorado | CTAs, destacados |

### Estilo Base

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-sm);
  padding: var(--space-sm) var(--space-xl);
  font-family: var(--font-body);
  font-size: 0.9375rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border: 2px solid transparent;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all var(--transition-base);
}
```

### Uso

```html
<button class="btn btn--primary">Aceptar</button>
<button class="btn btn--secondary">Cancelar</button>
<button class="btn btn--accent">¡Destacado!</button>
```

---

## Clases de Utilidad

### Alineación de Texto

```css
.text-center { text-align: center; }
.text-left   { text-align: left; }
.text-right  { text-align: right; }
```

### Margen Superior

```css
.mt-sm  { margin-top: var(--space-sm); }
.mt-md  { margin-top: var(--space-md); }
.mt-lg  { margin-top: var(--space-lg); }
.mt-xl  { margin-top: var(--space-xl); }
.mt-2xl { margin-top: var(--space-2xl); }
```

### Margen Inferior

```css
.mb-sm  { margin-bottom: var(--space-sm); }
.mb-md  { margin-bottom: var(--space-md); }
.mb-lg  { margin-bottom: var(--space-lg); }
.mb-xl  { margin-bottom: var(--space-xl); }
.mb-2xl { margin-bottom: var(--space-2xl); }
```

### Uso

```html
<h2 class="text-center mb-lg">Título Centrado</h2>
<p class="mt-xl">Párrafo con margen superior</p>
```

---

## Transiciones

| Variable | Valor | Uso |
|----------|-------|-----|
| `--transition-fast` | `150ms ease` | Hover rápidos |
| `--transition-base` | `250ms ease` | Hover estándar |
| `--transition-slow` | `400ms ease` | Animaciones |

### Uso

```css
.elemento {
  transition: all var(--transition-base);
}

.elemento:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}
```

---

## Etiquetas (Tags)

### Clases de Etiquetas

| Clase | Apariencia | Uso |
|-------|------------|-----|
| `.tag` | Gris claro | Etiquetas generales |
| `.tag--primary` | Azul | Categorías principales |
| `.tag--accent` | Dorado | Destacados |

### Uso

```html
<span class="tag">Astronomía</span>
<span class="tag--primary">Nuevo</span>
<span class="tag--accent">Destacado</span>
```

---

## Personalización

### Cambiar Colores Principales

Edita `src/styles/global.css`:

```css
:root {
  /* Cambiar azul institucional */
  --color-primary: #nuevo-color;
  --color-primary-dark: #nuevo-color-oscuro;
  
  /* Cambiar acento dorado */
  --color-accent: #nuevo-acento;
}
```

### Cambiar Tipografía

1. Actualiza el import de Google Fonts:

```css
@import url('https://fonts.googleapis.com/css2?family=Nueva+Fuente&display=swap');
```

2. Actualiza las variables:

```css
:root {
  --font-display: 'Nueva Fuente', serif;
  --font-body: 'Otra Fuente', sans-serif;
}
```

### Cambiar Espaciado

```css
:root {
  --space-lg: 2rem;  /* Aumentar espaciado grande */
  --space-xl: 3rem;  /* Aumentar espaciado extra grande */
}
```

### Media Queries

Los breakpoints principales:

```css
/* Desktop grande */
@media (max-width: 1280px) { }

/* Desktop */
@media (max-width: 1024px) { }

/* Tablet */
@media (max-width: 768px) { }

/* Móvil */
@media (max-width: 640px) { }
```

---

## Archivos de Estilos

| Archivo | Ubicación | Contenido |
|---------|-----------|-----------|
| `global.css` | `src/styles/global.css` | Variables, reset, utilidades globales |
| `article.css` | `src/styles/article.css` | Estilos específicos para artículos de divulgación |

### Cargar Estilos

En cada componente o página:

```astro
---
import '../styles/global.css';
---
```

O en el layout principal (`Layout.astro`):

```astro
---
import '../styles/global.css';
---
```

---

## Buenas Prácticas

1. **Usar variables CSS** siempre que sea posible
2. **No usar valores fijos** (px) para espaciado o colores
3. **Usar `rem`** en lugar de `px` para tamaños
4. **Probar en móvil** todos los cambios
5. **Mantener consistencia** con el sistema existente

---

## Próximos Pasos

- [03-COMPONENTES.md](./03-COMPONENTES.md) - Ver componentes que usan estos estilos
- [08-CONFIGURACION.md](./08-CONFIGURACION.md) - Configuración de build
