import random
import string
import getpass
import tkinter as tk
from tkinter import messagebox

def generar_contraseña(longitud, *inclusiones):
    caracteres = ''
    if inclusiones[0]:
        caracteres += string.ascii_uppercase
    if inclusiones[1]:
        caracteres += string.ascii_lowercase
    if inclusiones[2]:
        caracteres += string.digits
    if inclusiones[3]:
        caracteres += string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def guardar_contraseña(contraseña, archivo):
    with open(archivo, 'a') as f:
        f.write(contraseña + '\n')
    messagebox.showinfo("Contraseña guardada", f"La contraseña ha sido guardada en el archivo: {archivo}")

def generar_y_mostrar_contraseña():
    longitud = int(entry_longitud.get())
    inclusiones = (
        var_mayusculas.get(),
        var_minusculas.get(),
        var_numeros.get(),
        var_simbolos.get()
    )
    contraseña = generar_contraseña(longitud, *inclusiones)
    label_contraseña.config(text=contraseña)

    if var_guardar.get() == 1:
        archivo = entry_archivo.get()
        guardar_contraseña(contraseña, archivo)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")

# Crear y posicionar los elementos
label_longitud = tk.Label(ventana, text="Longitud de la contraseña:")
label_longitud.pack()
entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

var_mayusculas = tk.IntVar()
var_minusculas = tk.IntVar()
var_numeros = tk.IntVar()
var_simbolos = tk.IntVar()

check_mayusculas = tk.Checkbutton(ventana, text="Incluir letras mayúsculas", variable=var_mayusculas)
check_mayusculas.pack()
check_minusculas = tk.Checkbutton(ventana, text="Incluir letras minúsculas", variable=var_minusculas)
check_minusculas.pack()
check_numeros = tk.Checkbutton(ventana, text="Incluir números", variable=var_numeros)
check_numeros.pack()
check_simbolos = tk.Checkbutton(ventana, text="Incluir símbolos de puntuación", variable=var_simbolos)
check_simbolos.pack()

button_generar = tk.Button(ventana, text="Generar y Mostrar Contraseña", command=generar_y_mostrar_contraseña)
button_generar.pack()

label_contraseña = tk.Label(ventana, text="")
label_contraseña.pack()

var_guardar = tk.IntVar()
check_guardar = tk.Checkbutton(ventana, text="Guardar en archivo", variable=var_guardar)
check_guardar.pack()

label_archivo = tk.Label(ventana, text="Nombre del archivo:")
label_archivo.pack()
entry_archivo = tk.Entry(ventana)
entry_archivo.pack()

# Ejecutar la ventana
ventana.mainloop()