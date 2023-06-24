import tkinter as tk

# Crear la ventana
ventana = tk.Tk()
ventana.title("Mi Aplicación")
ventana.geometry("400x300")

# Crear un widget de etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
