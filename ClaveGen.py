import random
import tkinter as tk
import pyperclip
from string import ascii_letters, digits, punctuation
from tkinter import ttk, messagebox

def generar_contrasena():
    try:
        longitud = int(longitud_entry.get())
        if longitud <= 0 or longitud > 1000:
            messagebox.showerror("Error", "La longitud debe ser un número entero positivo menor o igual a 1000.")
            return
    except ValueError:
        messagebox.showerror("Error", "La longitud debe ser un número entero positivo menor o igual a 1000.")
        return

    caracteres = ""
    if incluir_caracteres.get():
        caracteres += punctuation
    if incluir_numeros.get():
        caracteres += digits
    if incluir_mayusculas.get():
        caracteres += ascii_letters.upper()
    if incluir_minusculas.get():
        caracteres += ascii_letters.lower()
    if incluir_especiales.get():
        caracteres += 'ñáéíóúüç'

    if not caracteres:
        messagebox.showerror("Error", "Debe seleccionar al menos una opción de caracteres.")
        return

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))

    contrasena_entry.delete(0, tk.END)
    contrasena_entry.insert(0, contrasena)
    print("Contraseña generada:", contrasena)

def copiar_contrasena():
    contrasena = contrasena_entry.get()
    pyperclip.copy(contrasena)
    print("Contraseña copiada al portapapeles:", contrasena)

def salir():
    respuesta = messagebox.askquestion("Salir", "¿Está seguro de que desea salir? Se eliminará la contraseña del portapapeles.")
    if respuesta == "yes":
        contrasena_entry.delete(0, tk.END)
        pyperclip.copy('')
        ventana.destroy()

ventana = tk.Tk()
ventana.geometry("500x350")
ventana.title("ClaveGen v2.0")

frame_superior = ttk.Frame(ventana)
frame_superior.pack(padx=10, pady=5)

etiqueta_advertencia = tk.Label(frame_superior, text="Al presionar Salir, la contraseña se eliminará del portapapeles.",
                                fg="red", font=("Arial", 8))
etiqueta_advertencia.grid(row=0, column=0, columnspan=2, padx=5, pady=2)

longitud_label = ttk.Label(frame_superior, text="Longitud de la contraseña:")
longitud_label.grid(row=1, column=0, padx=5, pady=2)

longitud_entry = ttk.Entry(frame_superior, width=10)
longitud_entry.grid(row=1, column=1, padx=5, pady=2)

opciones_frame = ttk.LabelFrame(ventana, text="Opciones de caracteres")
opciones_frame.pack(padx=10, pady=5, fill="x")

incluir_caracteres = tk.BooleanVar()
incluir_numeros = tk.BooleanVar()
incluir_mayusculas = tk.BooleanVar()
incluir_minusculas = tk.BooleanVar()
incluir_especiales = tk.BooleanVar()

caracteres_check = ttk.Checkbutton(opciones_frame, text="Caracteres especiales", variable=incluir_caracteres)
caracteres_check.grid(row=0, column=0, padx=5, pady=2, sticky="w")

numeros_check = ttk.Checkbutton(opciones_frame, text="Números", variable=incluir_numeros)
numeros_check.grid(row=1, column=0, padx=5, pady=2, sticky="w")

mayusculas_check = ttk.Checkbutton(opciones_frame, text="Mayúsculas", variable=incluir_mayusculas)
mayusculas_check.grid(row=0, column=1, padx=5, pady=2, sticky="w")

minusculas_check = ttk.Checkbutton(opciones_frame, text="Minúsculas", variable=incluir_minusculas)
minusculas_check.grid(row=1, column=1, padx=5, pady=2, sticky="w")

especiales_check = ttk.Checkbutton(opciones_frame, text="Especiales (ñáéíóúüç)", variable=incluir_especiales)
especiales_check.grid(row=2, column=0, columnspan=2, padx=5, pady=2, sticky="w")

contrasena_entry = ttk.Entry(ventana, width=30)
contrasena_entry.pack(padx=10, pady=10)

boton_generar = tk.Button(ventana, text="Generar contraseña", command=generar_contrasena)
boton_generar.pack(padx=10, pady=5)

boton_copiar = tk.Button(ventana, text="Copiar", command=copiar_contrasena)
boton_copiar.pack(padx=10, pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(padx=10, pady=5)

firma_label = ttk.Label(ventana, text="Hecho con ❤ por Para", foreground="gray")
firma_label.pack(padx=10, pady=2)
firma_label.bind("<Button-1>", lambda e: abrir_sitio_web("https://eliecer.bio"))

def abrir_sitio_web(url):
    import webbrowser
    webbrowser.open_new(url)

ventana.protocol("WM_DELETE_WINDOW", salir)

ventana.mainloop()
