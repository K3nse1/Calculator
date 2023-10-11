import tkinter as tk
import operaciones

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

    # Definimos nuestro frame
    myFrame = tk.Frame()

    # Empaquetamos el frame en la raíz
    myFrame.pack(fill = "x")

    # Damos color al frame para verlo
    myFrame.config (bg = "white")

    myFrame.config(width = "650", height = "350")

    bt1 = tk.Button(myFrame, text="1", padx=2, pady=2)
    bt1.grid (row=1, column=0)

    bt2 = tk.Button(myFrame, text="2", padx=2, pady=2)
    bt2.grid(row=1, column=1)

    bt3 = tk.Button(myFrame, text="3", padx=2, pady=2)
    bt3.grid(row=1, column=2)

    bt4 = tk.Button(myFrame, text="4", padx=2, pady=2)
    bt4.grid(row=2, column=0)

    bt5 = tk.Button(myFrame, text="5", padx=2, pady=2)
    bt5.grid(row=2, column=1)

    bt6 = tk.Button(myFrame, text="6", padx=2, pady=2)
    bt6.grid(row=2, column=2)

    bt7 = tk.Button(myFrame, text="7", padx=2, pady=2)
    bt7.grid(row=2, column=0)

    bt8 = tk.Button(myFrame, text="8", padx=2, pady=2)
    bt8.grid(row=2, column=1)

    bt9 = tk.Button(myFrame, text="9", padx=2, pady=2)
    bt9.grid(row=2, column=2)

    bt0 = tk.Button(myFrame, text="0", padx=2, pady=2)
    bt0.grid(row=3, column=0)

    bt_dot = tk.Button(myFrame, text=".", command=operaciones.suma, padx=2, pady=2)
    bt_dot.grid(row=3, column=1)

    bt_sum = tk.Button(myFrame, text="+", padx=2, pady=2)
    bt_sum.grid(row=1, column=3)

    bt_dif = tk.Button(myFrame, text="-", padx=2, pady=2)
    bt_dif.grid(row=2, column=3)

    bt_mul = tk.Button(myFrame, text="x", padx=2, pady=2)
    bt_mul.grid(row=3, column=3)

    bt_div = tk.Button(myFrame, text="/", padx=2, pady=2)
    bt_div.grid(row=3, column=2)

    return root.mainloop()


interface()
