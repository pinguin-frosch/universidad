# 2.- Cree un algoritmo que lea dos números, calculando y escribiendo el valor de su suma, resta, producto y división.

# Hecho por Gabriel Barrientos

print(" Calculadora simple entre dos números ".center(50, "="))
def repetir():
    eleccion = input("\n¿Repetir el programa? (S/N): ")
    if eleccion.upper() == "S" or eleccion.upper() == "SI" or eleccion.upper() == "SÍ":
        asignar()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")

def asignar():
    global numero1, numero2
    try:
        numero1 = float(input("\nIngrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        numero1 = int(numero1) if numero1.is_integer() else numero1
        numero2 = int(numero2) if numero2.is_integer() else numero2
        operacion()
    except ValueError:
        print("\nNo ingresó un número.")
    finally:
        repetir()

def calcular(x, y, z):
    if x == 1:
        if type(numero1) == float or type(numero2) == float:
            return int(y + z) if (y + z).is_integer() else (y + z)
        else:
            return y + z
    elif x == 2:
        if type(numero1) == float or type(numero2) == float:
            return int(y - z) if (y - z).is_integer() else (y - z)
        else:
            return y - z
    elif x == 3:
        if type(numero1) == float or type(numero2) == float:
            return int(y * z) if (y * z).is_integer() else (y * z)
        else:
            return y * z
    elif x == 4:
        try:
            return int(y / z) if (y / z).is_integer() else (y / z)
        except ZeroDivisionError:
            return "No se puede dividir por 0"

def operacion():
    print("\n{} + {} = {}".format(numero1, numero2, calcular(1, numero1, numero2)))
    print("{} - {} = {}".format(numero1, numero2, calcular(2, numero1, numero2)))
    print("{} * {} = {}".format(numero1, numero2, calcular(3, numero1, numero2)))
    print("{} / {} = {}".format(numero1, numero2, calcular(4, numero1, numero2)))

asignar()