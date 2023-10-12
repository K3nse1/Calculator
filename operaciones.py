
def suma (n1, n2):
    return n1 + n2


def resta (n1, n2):
    return n1 - n2


def multiplicacion (n1, n2):
    return n1 * n2


def division (n1, n2):
    return n1 / n2

# import tkinter as tk
#
# # Función para actualizar el display
# def actualizar_display(valor):
#     display.config(text=valor)
#
# # Función para manejar los clics de los botones numéricos
# def boton_numero_clicado(numero):
#     valor_actual = display.cget("text")
#     nuevo_valor = valor_actual + numero
#     actualizar_display(nuevo_valor)
#
# # Función para manejar el clic del botón "C" (borrar)
# def boton_borrar_clicado():
#     actualizar_display("")
#
# # Configuración de la ventana principal
# ventana = tk.Tk()
# ventana.title("Calculadora")
#
# # Crear el display
# display = tk.Label(ventana, text="", font=("Helvetica", 20))
# display.grid(row=0, column=0, columnspan=4)
#
# # Crear los botones numéricos
# botones_numeros = [
#     "7", "8", "9",
#     "4", "5", "6",
#     "1", "2", "3",
#     "0"
# ]
#
# fila, columna = 1, 0
# for numero in botones_numeros:
#     tk.Button(ventana, text=numero, font=("Helvetica", 16), command=lambda num=numero: boton_numero_clicado(num)).grid(row=fila, column=columna)
#     columna += 1
#     if columna > 2:
#         columna = 0
#         fila += 1
#
# # Botón de borrar
# tk.Button(ventana, text="C", font=("Helvetica", 16), command=boton_borrar_clicado).grid(row=5, column=0)
#
# ventana.mainloop()
