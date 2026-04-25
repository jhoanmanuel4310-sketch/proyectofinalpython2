import tkinter as tk

ventana = tk.Tk()
ventana.title("Programa para subir a repositorio")
ventana.geometry("400x250")
ventana.configure(bg="#1e1e2f")  # Fondo oscuro moderno

# Fuente y estilo mejorados
etiqueta = tk.Label(
    ventana,
    text="Este programa es de\nManuel Maciel y Jafet Zavala",
    font=("Helvetica", 16, "bold"),  # Tipografía más grande y en negrita
    fg="#ffcc00",  # Color de texto llamativo (amarillo)
    bg="#1e1e2f",  # Igual al fondo para integración
    justify="center"
)

etiqueta.pack(expand=True)

ventana.mainloop()