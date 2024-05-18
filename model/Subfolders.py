import os

def obtener_subcarpetas(ruta):
    # Lista para almacenar los nombres de las subcarpetas
    subcarpetas = []
    
    # Verificar si la ruta es un directorio válido
    if os.path.isdir(ruta):
        # Obtener la lista de subdirectorios en la ruta dada
        subdirectorios = next(os.walk(ruta))[1]
        
        # Agregar los nombres de los subdirectorios a la lista
        subcarpetas.extend(subdirectorios)
    
    # Devolver los nombres de las subcarpetas separados por coma
    return ', '.join(subcarpetas)

# Ruta de la carpeta
ruta_carpeta = 'C:\\Users\\Kevin\\OneDrive\\Escritorio\\Dataset\\face_age'

# Obtener y mostrar las subcarpetas
subcarpetas = obtener_subcarpetas(ruta_carpeta)
print("Subcarpetas en la carpeta:", subcarpetas)
