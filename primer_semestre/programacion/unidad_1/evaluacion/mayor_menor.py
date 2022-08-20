# 8.	De acuerdo con el siguiente problema, realice el algoritmo en Python (15 pts.)

# Cree una aplicación de consola que solicite dos números y calcule cuál de ellos es el mayor; debe mostrar un mensaje identificando el número mayor, y también no debe permitir que se ingresen dos números iguales:

# Hecho por Gabriel Barrientos

print(" Calcular número mayor ".center(50, "="))
def repetir():
    eleccion = input("\n¿Quiere volver a ejecutar el programa? (S/N): ")
    if eleccion.upper() in ("SÍ", "SI", "S"):
        calcular()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")

def calcular():
    try:
        numero1 = float(input("\nIngrese el primer número: "))
        numero2 = float(input("\nIngrese el segundo número: "))

        while numero2 == numero1:
            numero2 = float(input("\nNo pueden ser iguales, ingrese el número dos otra vez: "))

        numero_mayor = numero1 if numero1 > numero2 else numero2
        numero_mayor = int(numero_mayor) if numero_mayor.is_integer() else numero_mayor

        print("\nEl número mayor es {}.".format(numero_mayor))

        repetir()

    except ValueError:
        print("\nDebe ingresar números, no letras u otros símbolos.")
        repetir()

calcular()