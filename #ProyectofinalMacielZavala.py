import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():
    messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - proyectofinalMacielZavala")
ventana.geometry("500x600")
ventana.resizable(False, False)


# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imagen = Image.open(os.path.join(BASE_DIR, "logo.png"))
    imagen = imagen.resize((250, 250))
    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(ventana, image=img_logo)
    lbl_logo.pack(pady=20)
except:
    lbl_sin_logo = tk.Label(ventana, text="(Aquí va el logo del sistema)", font=("Arial", 14))
    lbl_sin_logo.pack(pady=40)


# -------------------------
# ESTILO DE BOTONES
# -------------------------
estilo_boton = {
    "font": ("Arial", 12),
    "bg": "black",
    "fg": "white",
    "activebackground": "#333333",
    "activeforeground": "white",
    "width": 25,
    "height": 2,
    "bd": 0
}


# -------------------------
# BOTONES PRINCIPALES
# -------------------------
btn_reg_prod = tk.Button(ventana, text="Registro de Productos", command=abrir_registro_productos, **estilo_boton)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = tk.Button(ventana, text="Registro de Ventas", command=abrir_registro_ventas, **estilo_boton)
btn_reg_ventas.pack(pady=10)

btn_reportes = tk.Button(ventana, text="Reportes", command=abrir_reportes, **estilo_boton)
btn_reportes.pack(pady=10)

btn_acerca = tk.Button(ventana, text="Acerca de", command=abrir_acerca_de, **estilo_boton)
btn_acerca.pack(pady=10)


# -------------------------
# INICIO DE LA APP
# -------------------------
ventana.mainloop()