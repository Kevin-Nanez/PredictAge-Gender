import os
from PIL import Image

def renombrar_imagenes(carpeta, numero_inicial):
    # Verificar si la carpeta existe
    if not os.path.exists(carpeta):
        print("La carpeta especificada no existe.")
        return
    
    # Obtener una lista de todos los archivos en la carpeta y sus subcarpetas
    archivos = []
    for directorio_raiz, _, nombres_archivos in os.walk(carpeta):
        for nombre_archivo in nombres_archivos:
            archivos.append(os.path.join(directorio_raiz, nombre_archivo))
    
    # Iterar sobre cada archivo
    for i, archivo in enumerate(archivos):
        # Verificar si el archivo es una imagen
        extension = os.path.splitext(archivo)[1].lower()
        if extension not in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            print(f"Ignorando archivo no compatible: {archivo}")
            continue
        
        # Renombrar y/o convertir la imagen
        nuevo_nombre = os.path.join(os.path.dirname(archivo), f"{numero_inicial + i}.png")
        
        if extension != '.png':
            # Convertir la imagen a formato PNG si no lo está
            try:
                img = Image.open(archivo)
                # Recortar 70 píxeles del lado derecho e izquierdo
                width, height = img.size
                left = 70
                top = 0
                right = width - 70
                bottom = height
                img = img.crop((left, top, right, bottom))
                # Redimensionar la imagen a 200x200 píxeles
                img = img.resize((200, 200))
                img.save(nuevo_nombre)
            except Exception as e:
                print(f"No se pudo convertir {archivo} a formato PNG: {str(e)}")
                continue
        else:
            # Si ya es PNG, simplemente renombrar
            try:
                img = Image.open(archivo)
                # Recortar 70 píxeles del lado derecho e izquierdo
                width, height = img.size
                left = 70
                top = 0
                right = width - 70
                bottom = height
                img = img.crop((left, top, right, bottom))
                # Redimensionar la imagen a 200x200 píxeles
                img = img.resize((200, 200))
                img.save(nuevo_nombre)
                #os.remove(archivo)
            except Exception as e:
                print(f"No se pudo renombrar {archivo} a {nuevo_nombre}: {str(e)}")
                continue
                
        print(f"Archivo {archivo} renombrado, recortado y redimensionado a {nuevo_nombre}")

# Especifica la carpeta y el número inicial para el renombrado
carpeta_a_procesar = "C:\\Users\\Kevin\\OneDrive\\Escritorio\\Dataset\\yo"
numero_inicial = 9778

# Llamar a la función para renombrar y convertir las imágenes
renombrar_imagenes(carpeta_a_procesar, numero_inicial)
