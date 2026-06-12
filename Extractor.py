import os
import re
import sys
from colorama import init, Fore  # Librería para el color del texto

# Inicializar colorama
init(autoreset=True)

# Nombre del creador oculto en una variable
CREADOR = "FSCHOOL"  

# Función para verificar que el nombre del creador no haya sido modificado
def verificar_creador():
    if CREADOR != "FSCHOOL":
        print("El nombre del creador ha sido modificado. El script se detendrá.")
        sys.exit(1)

# Verificar el nombre del creador al inicio
verificar_creador()

# Función para crear las carpetas necesarias si no existen
def crear_carpetas():
    rutas = ["/sdcard/Listas/", "/sdcard/Listas/resultado/"]
    
    for ruta in rutas:
        if not os.path.exists(ruta):
            os.makedirs(ruta)  # Crea la carpeta y subcarpetas si no existen
            print(f"Carpeta creada: {ruta}")
        else:
            print(f"La carpeta ya existe: {ruta}")

# Ejecutar la función para crear las carpetas
crear_carpetas()

# Nuevo banner personalizado
banner = """

╭━━━━━━━━╮
┃⠀⠀⠀●══  ┃
┃████████┃
┃████████┃
┃Friends ┃
┃████████┃
┃█School█┃
┃████████┃
┃████████┃
┃████████┃
┃⠀⠀⠀⠀○⠀⠀⠀┃
╰━━━━━━━━╯ 
"""

# Título
titulo = "COMBOS FULL EXTRAIDOS"

# Texto "BY: FSCHOOL" debajo del banner, con las copas 🍷🍷🍷
by_FSCHOOL = "BY: ៚⋞×͜͡𝔉𝔯𝔦𝔢𝔫𝔡𝔰 𝔖𝔠𝔥𝔬𝔬𝔩ᶠ×ᷤ⋟࿐"

# Mostrar el banner en color rojo
print(Fore.RED + banner)

# Mostrar el título en color rojo, debajo del banner
print(Fore.RED + titulo)

# Mostrar "BY: FSCHOOL" debajo del título con las copas 🍷🍷🍷
print(Fore.RED + by_FSCHOOL)

# Función para obtener las combinaciones de usuario y contraseña existentes
def obtener_combinaciones_existentes(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', errors='ignore') as archivo:
            combinaciones = set()
            for linea in archivo:
                # Cada línea debe tener un formato "usuario:contraseña"
                if ":" in linea:
                    combinaciones.add(linea.strip())
            return combinaciones
    except FileNotFoundError:
        return set()

# Función para guardar las combinaciones de usuario y contraseña
def guardar_combinaciones(ruta_archivo, combinaciones):
    with open(ruta_archivo, 'w') as archivo:
        for combinacion in combinaciones:
            archivo.write(combinacion + '\n')

# Ruta de la carpeta que contiene los archivos de texto
carpeta = "/sdcard/Listas/"

# Expresión regular para buscar username y password
patron_usuario_contraseña = re.compile(r'username\s*=\s*([^\s&]+)\s*.*\s*password\s*=\s*([^\s&]+)', re.IGNORECASE)

# Lista para almacenar las combinaciones de usuario y contraseña encontradas
combinaciones_encontradas = set()

# Iterar sobre cada archivo en la carpeta
for nombre_archivo in os.listdir(carpeta):
    ruta_archivo = os.path.join(carpeta, nombre_archivo)

    # Verificar si es un archivo de texto
    if os.path.isfile(ruta_archivo) and nombre_archivo.endswith(".txt"):
        try:
            with open(ruta_archivo, 'r', errors='ignore') as archivo:
                contenido = archivo.read()

                # Buscar coincidencias con la expresión regular
                coincidencias = patron_usuario_contraseña.findall(contenido)

                # Agregar las combinaciones (usuario:contraseña) encontradas a la lista
                for usuario, contrasena in coincidencias:
                    combinaciones_encontradas.add(f"{usuario}:{contrasena}")
        except UnicodeDecodeError as e:
            print(f"Error al decodificar {ruta_archivo}: {e}")
            pass  # Ignorar errores y continuar

# Ruta del archivo donde se guardarán las combinaciones
ruta_resultado = "/sdcard/Listas/resultado/base_de_user&pass.txt"

# Obtener las combinaciones existentes del archivo
combinaciones_existentes = obtener_combinaciones_existentes(ruta_resultado)

# Unir las combinaciones existentes con las nuevas y eliminar duplicados
combinaciones_finales = combinaciones_existentes.union(combinaciones_encontradas)

# Guardar las combinaciones en el archivo final
guardar_combinaciones(ruta_resultado, sorted(combinaciones_finales))

# Mensaje de confirmación
print(f"Se han guardado las combinaciones en: {ruta_resultado}")