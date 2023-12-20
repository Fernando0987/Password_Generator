import random
import string
import getpass

def generar_contraseña(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = ''
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def guardar_contraseña(contraseña, archivo):
    with open(archivo, 'a') as f:
        f.write(contraseña + '\n')
    print("Contraseña guardada en el archivo:", archivo)

def mostrar_contraseña(contraseña):
    print("Contraseña generada:")
    print(contraseña)

# Ejemplo de uso
longitud = int(input("Ingrese la longitud de la contraseña: "))
incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
incluir_minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower() == 's'
incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
incluir_simbolos = input("¿Incluir símbolos de puntuación? (s/n): ").lower() == 's'
contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
mostrar_contraseña(contraseña)

guardar = input("¿Desea guardar la contraseña en un archivo o en un gestor de contraseñas? (archivo/gestor): ").lower()
if guardar == 'archivo':
    archivo = input("Ingrese el nombre del archivo para guardar la contraseña: ")
    guardar_contraseña(contraseña, archivo)
elif guardar == 'gestor':
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña_maestra = getpass.getpass("Ingrese su contraseña maestra: ")
    # Aquí iría el código para guardar la contraseña en un gestor de contraseñas
    print("Contraseña guardada en el gestor de contraseñas.")
else:
    print("Opción no válida.")