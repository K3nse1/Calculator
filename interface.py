import tkinter as tk

def interface ():

    root = tk.Tk()

    # Tamaño de la ventana
    root.geometry("500x400")

    # Título
    root.title("Calculadora")

    # Icono
    root.iconbitmap("images/icon.ico")

    # Color del fondo
    root.config(bg = "black")

    return root.mainloop()
