import os
import random
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
from string import ascii_letters, digits, punctuation
import webbrowser
from ttkbootstrap import Style

class ClaveGen:
    def __init__(self):
        self.window = tk.Tk()
        self.style = Style(theme='flatly')
        self.window.title("ClaveGen 3")
        self.window.geometry("600x450")
        
        icon_path = os.path.join(os.path.dirname(__file__), 'static', 'padlock.png')
        if os.path.exists(icon_path):
            self.window.iconphoto(True, tk.PhotoImage(file=icon_path))
        
        self.create_widgets()
        self.window.protocol("WM_DELETE_WINDOW", self.exit)
        
    def create_widgets(self):
        self.create_header()
        self.create_length_frame()
        self.create_options_frame()
        self.create_password_frame()
        self.create_buttons()
        self.create_footer()
        
    def create_header(self):
        header_frame = ttk.Frame(self.window, padding="20 20 20 0")
        header_frame.pack(fill='x')
        
        ttk.Label(header_frame, text="ClaveGen 3", 
                  font=("Helvetica", 18, "bold")).pack()
        
        ttk.Separator(self.window).pack(fill='x', padx=20, pady=10)
        
    def create_length_frame(self):
        length_frame = ttk.Frame(self.window, padding="20 10")
        length_frame.pack(fill='x')
        
        ttk.Label(length_frame, text="Longitud de contraseña:").pack(side='left')
        
        self.length_var = tk.IntVar(value=12)
        self.length_scale = ttk.Scale(length_frame, from_=8, to=50, variable=self.length_var, 
                                      length=200, command=self.update_length_label)
        self.length_scale.pack(side='left', padx=10)
        
        self.length_label = ttk.Label(length_frame, text="12")
        self.length_label.pack(side='left')
        
    def update_length_label(self, *args):
        self.length_label.config(text=str(self.length_var.get()))
        
    def create_options_frame(self):
        options_frame = ttk.LabelFrame(self.window, text="Opciones de caracteres", padding="20 10")
        options_frame.pack(padx=20, pady=10, fill='x')
        
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=False)
        self.include_extra_special = tk.BooleanVar(value=False)
        
        options = [
            ("Mayúsculas", self.include_uppercase),
            ("Minúsculas", self.include_lowercase),
            ("Números", self.include_numbers),
            ("Caracteres especiales", self.include_special),
            ("Caracteres extra (ñÑáéíóúÁÉÍÓÚ)", self.include_extra_special)
        ]
        
        for text, var in options:
            cb = ttk.Checkbutton(options_frame, text=text, variable=var, style='success.TCheckbutton')
            cb.pack(anchor='w', pady=2)
        
    def create_password_frame(self):
        password_frame = ttk.Frame(self.window, padding="20 10")
        password_frame.pack(fill='x')
        
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(password_frame, textvariable=self.password_var, 
                                        font=("Courier", 12), width=40)
        self.password_entry.pack(side='left', padx=(0, 10))
        
        ttk.Button(password_frame, text="Copiar", style='info.TButton', 
                   command=self.copy_password).pack(side='left')
        
    def create_buttons(self):
        button_frame = ttk.Frame(self.window, padding="20 10")
        button_frame.pack(fill='x')
        
        ttk.Button(button_frame, text="🔀 Generar contraseña", style='success.TButton', 
                   command=self.generate_password).pack(side='left', padx=(0, 10))
        ttk.Button(button_frame, text="Salir", style='danger.TButton', 
                   command=self.exit).pack(side='left')
        
    def create_footer(self):
        footer_frame = ttk.Frame(self.window, padding="20")
        footer_frame.pack(fill='x', side='bottom')
        
        ttk.Label(footer_frame, text="Hecho con ❤ por E1DIGITAL", 
                  foreground="gray").pack(side='left')
        
        github_button = ttk.Button(footer_frame, text="GitHub", style='link.TButton', 
                                   command=lambda: self.open_website("https://github.com/E1DIGITALPF"))
        github_button.pack(side='right')
        
    def generate_password(self):
        length = self.length_var.get()
        
        char_sets = []
        if self.include_uppercase.get(): char_sets.append(ascii_letters.upper())
        if self.include_lowercase.get(): char_sets.append(ascii_letters.lower())
        if self.include_numbers.get(): char_sets.append(digits)
        if self.include_special.get(): char_sets.append(punctuation)
        if self.include_extra_special.get(): char_sets.append("ñÑáéíóúÁÉÍÓÚ")
        
        if not char_sets:
            messagebox.showerror("Error", "Por favor selecciona al menos una opción de caracteres.")
            return
        
        all_chars = ''.join(char_sets)
        password = ''.join(random.choice(all_chars) for _ in range(length))
        
        self.password_var.set(password)
        self.password_entry.config(style='success.TEntry')
        self.window.after(1000, lambda: self.password_entry.config(style='TEntry'))

    def copy_password(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("¡Éxito!", "Contraseña copiada al portapapeles.")
        else:
            messagebox.showwarning("¡Precaución!", "No hay contraseña para copiar")

    def exit(self):
        if messagebox.askyesno("Salir", "¿Estás seguro que quieres salir? Esto eliminará el portapapeles"):
            pyperclip.copy('')
            self.window.destroy()

    @staticmethod
    def open_website(url):
        webbrowser.open_new(url)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ClaveGen()
    app.run()