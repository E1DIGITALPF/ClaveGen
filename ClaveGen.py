import random
import tkinter as tk
from string import ascii_letters, digits, punctuation
from tkinter import ttk, messagebox

def generar_contrasena():
    longitud = 12
    caracteres = ascii_letters + digits + punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud-1))
    posicion_coma = random.randint(0, len(contrasena))
    contrasena = contrasena[:posicion_coma] + ',' + contrasena[posicion_coma:]
    
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

etiqueta_advertencia = tk.Label(ventana, text="Al presionar Salir, la contraseña se eliminará del portapapeles.",
                                fg="red", font=("Arial", 8))
etiqueta_advertencia.pack(padx=10, pady=5)

contrasena_entry = ttk.Entry(ventana, width=30)
contrasena_entry.pack(padx=10, pady=10)

boton_generar = tk.Button(ventana, text="Generar contraseña", command=generar_contrasena)
boton_generar.pack(padx=10, pady=10)

boton_copiar = tk.Button(ventana, text="Copiar", command=copiar_contrasena)
boton_copiar.pack(padx=10, pady=10)

boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(padx=10, pady=10)

ventana.protocol("WM_DELETE_WINDOW", salir)

ventana.mainloop()