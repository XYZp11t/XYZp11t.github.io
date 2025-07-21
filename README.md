# 🌞 Visualización 3D de Capas Solares

Un proyecto web interactivo para visualizar modelos 3D de las capas solares utilizando Astro y Three.js.

## 🚀 Características

- **Visualización 3D Interactiva**: Explora modelos 3D con controles de navegación intuitivos
- **Controles de Navegación**: Rotación, zoom y pan con el mouse
- **Rotación Automática**: Opción para rotación automática del modelo
- **Diseño Responsive**: Funciona perfectamente en dispositivos móviles y de escritorio
- **Iluminación Realista**: Sombras y efectos de luz para mejor visualización
- **Interfaz Moderna**: Diseño limpio y profesional con gradientes y animaciones

## 🛠️ Tecnologías Utilizadas

- **[Astro](https://astro.build/)**: Framework web para el frontend
- **[Three.js](https://threejs.org/)**: Biblioteca 3D para WebGL
- **[GLTF Loader](https://threejs.org/docs/#examples/en/loaders/GLTFLoader)**: Carga de modelos 3D en formato GLB
- **[OrbitControls](https://threejs.org/docs/#examples/en/controls/OrbitControls)**: Controles de navegación 3D
- **TypeScript**: Tipado estático para mejor desarrollo

## 📁 Estructura del Proyecto

```
espaciales/
├── src/
│   ├── components/
│   │   └── CapasSolares.astro    # Componente principal del visualizador 3D
│   ├── layouts/
│   │   └── Layout.astro          # Layout base de la aplicación
│   ├── models/
│   │   └── capas_test7.glb       # Modelo 3D de las capas solares
│   └── pages/
│       ├── index.astro           # Página principal
│       └── about.astro           # Página de información del proyecto
├── public/
│   └── favicon.svg
└── package.json
```

## 🚀 Instalación y Uso

### Prerrequisitos

- Node.js (versión 16 o superior)
- npm o yarn

### Instalación

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd espaciales
```

2. Instala las dependencias:
```bash
npm install
```

3. Ejecuta el servidor de desarrollo:
```bash
npm run dev
```

4. Abre tu navegador y ve a `http://localhost:4321`

### Scripts Disponibles

- `npm run dev` - Inicia el servidor de desarrollo
- `npm run build` - Construye la aplicación para producción
- `npm run preview` - Previsualiza la build de producción

## 🎮 Controles del Visualizador

### Navegación con Mouse
- **Click + Arrastrar**: Rotar la vista alrededor del modelo
- **Scroll**: Zoom in/out
- **Click derecho + Arrastrar**: Pan (mover la vista)

### Botones de Control
- **Resetear Vista**: Vuelve a la posición inicial de la cámara
- **Rotar Modelo**: Activa/desactiva la rotación automática del modelo

## 📱 Responsive Design

El visualizador está optimizado para funcionar en:
- **Desktop**: Vista completa con controles expandidos
- **Tablet**: Interfaz adaptada para pantallas medianas
- **Mobile**: Controles reorganizados para pantallas pequeñas

## 🔧 Personalización

### Cambiar el Modelo 3D

Para usar un modelo diferente:

1. Coloca tu archivo `.glb` en la carpeta `src/models/`
2. Actualiza la ruta en `src/components/CapasSolares.astro`:
```javascript
loader.load('/models/tu-modelo.glb', (gltf) => {
  // ...
});
```

### Modificar la Iluminación

Puedes ajustar la iluminación modificando los parámetros en el componente:

```javascript
// Luz ambiental
const luzAmbiente = new THREE.AmbientLight(0xffffff, 0.4);

// Luz direccional
const luzDireccional = new THREE.DirectionalLight(0xffffff, 0.8);
```

## 🎨 Características del Diseño

- **Gradientes Modernos**: Fondos con gradientes atractivos
- **Sombras y Efectos**: Sombras suaves y efectos hover
- **Tipografía Clara**: Fuentes legibles y jerarquía visual clara
- **Colores Consistente**: Paleta de colores coherente en toda la aplicación

## 📄 Páginas

### Página Principal (`/`)
- Visualizador 3D interactivo
- Controles de navegación
- Información básica del proyecto

### Acerca del Proyecto (`/about`)
- Descripción detallada del proyecto
- Lista de características
- Tecnologías utilizadas
- Enlaces de navegación

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🙏 Agradecimientos

- [Three.js](https://threejs.org/) por la excelente biblioteca 3D
- [Astro](https://astro.build/) por el framework web moderno
- La comunidad de desarrolladores web por las herramientas y recursos

---

**¡Disfruta explorando las capas solares en 3D! 🌟**
