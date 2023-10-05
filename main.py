# from interface import interface

n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce otro: "))

operacion_deseada = input ("Introduce una operación a realizar: suma, resta, multiplicacion o division: ")

opciones = {
    "suma": n1 + n2,
    "resta": n1 - n2,
    "multiplicacion": n1 * n2,
    "division": n1 / n2
}

if operacion_deseada not in opciones.keys():
    print ("Operación no comtemplada")
else:
    print ("El resultado de la", operacion_deseada, "es", opciones.get(operacion_deseada))