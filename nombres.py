import os

# Obtener la ruta de la carpeta con las imágenes
carpeta = "/home/xitari/Escritorio/code/Animaciones/imagenes"

# Obtener una lista de los nombres de archivo en la carpeta
nombres_archivos = os.listdir(carpeta)

# Inicializar una lista vacía para los nombres de imagen
nombres_imagenes = []

# Recorrer la lista de nombres de archivo y agregar solo los nombres de archivo de imagen a la lista de nombres de imagen
for nombre in nombres_archivos:
    if nombre.endswith(".jpg") or nombre.endswith(".png"):
        nombres_imagenes.append(nombre)

# Imprimir la lista de nombres de imagen
print(nombres_imagenes)
print(len(nombres_imagenes))

