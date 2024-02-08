import random
import tkinter as tk
from random import randint
from string import ascii_letters, digits, punctuation
from tkinter import ttk, messagebox

def generar_contrasena():
    longitud = randint(12, 16)
    caracteres = ascii_letters + digits + punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    contrasena_entry.delete(0, tk.END)
    contrasena_entry.insert(0, contrasena)
    print("Contraseña generada:", contrasena)

def copiar_contrasena():
    contrasena = contrasena_entry.get()
    ventana.clipboard_clear()
    ventana.clipboard_append(contrasena)
    print("Contraseña copiada al portapapeles:", contrasena)

def salir():
    respuesta = messagebox.askquestion("Salir", "¿Está seguro de que desea salir? Se eliminará la contraseña del portapapeles.")
    if respuesta == "yes":
        ventana.clipboard_clear()
        ventana.destroy()
ventana = tk.Tk()
ventana.geometry("350x210")
ventana.title("ClaveGen v1.0")

# Etiqueta de advertencia
etiqueta_advertencia = tk.Label(ventana, text="Al presionar Salir, la contraseña se eliminará del portapapeles.",
                                fg="red", font=("Arial", 8))
etiqueta_advertencia.pack(padx=10, pady=5)

# Entrada para la contraseña
contrasena_entry = ttk.Entry(ventana, width=30)
contrasena_entry.pack(padx=10, pady=10)

# Botones
boton_generar = tk.Button(ventana, text="Generar contraseña", command=generar_contrasena)
boton_generar.pack(padx=10, pady=10)

boton_copiar = tk.Button(ventana, text="Copiar", command=copiar_contrasena)
boton_copiar.pack(padx=10, pady=10)

boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(padx=10, pady=10)

# Cerrar la aplicación con la "X"
ventana.protocol("WM_DELETE_WINDOW", salir)

ventana.mainloop()
