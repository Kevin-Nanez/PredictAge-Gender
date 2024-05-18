import os

def encontrar_numero_mas_grande(ruta):
    numero_mas_grande = float('-inf')  # Inicializar con el valor más pequeño posible
    
    # Recorrer todas las subcarpetas y archivos en la ruta dada
    for directorio_raiz, _, archivos in os.walk(ruta):
        for nombre_archivo in archivos:
            # Obtener el nombre del archivo y su extensión
            nombre, extension = os.path.splitext(nombre_archivo)
            
            # Verificar si la extensión es '.png'
            if extension.lower() == '.png':
                # Intentar convertir el nombre del archivo a un número
                try:
                    numero_archivo = int(nombre)
                    if numero_archivo > numero_mas_grande:
                        numero_mas_grande = numero_archivo
                except ValueError:
                    # Si el nombre del archivo no es un número, ignorarlo
                    continue
    
    if numero_mas_grande != float('-inf'):
        return numero_mas_grande
    else:
        return None

# Ruta de la carpeta principal que contiene las subcarpetas con las imágenes
ruta_carpeta_principal = 'C:\\Users\\Kevin\\OneDrive\\Escritorio\\Dataset\\face_age'

# Llamar a la función para encontrar el número más grande
numero_mas_grande = encontrar_numero_mas_grande(ruta_carpeta_principal)

if numero_mas_grande is not None:
    print(f"El número más grande encontrado en los nombres de archivo es: {numero_mas_grande}")
else:
    print("No se encontraron archivos PNG en las subcarpetas.")
