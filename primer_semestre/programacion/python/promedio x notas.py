# 6.- Crear un algoritmo que permita obtener el promedio de un numero de notas ingresadas, el algoritmo debe consultar cuantas notas desea ingresar.

# Hecho por Gabriel Barrientos

print(" Promedio de x notas ".center(50, "="))
def repetir():
    eleccion = input("\n¿Repetir el programa? (S/N): ")
    if eleccion.upper() == "S" or eleccion.upper() == "SI" or eleccion.upper() == "SÍ":
        calcular()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")

def calcular():
    try:
        cantidad = int(input("\n¿De cuántas notas quiere calcular el promedio? "))

        if cantidad < 1:
            raise ValueError

        suma = 0
        print("\nRecuerde ingresar las notas en formato: 34, 54, 16, etc.\n")

        for x in range(cantidad):
            nota_temporal = int(input("Ingrese la nota {}: ".format(x + 1)))

            while nota_temporal < 10 or nota_temporal > 70:
                nota_temporal = int(input("Valor incorrecto. Ingrese otra vez la nota {}: ".format(x + 1)))

            suma += nota_temporal

        promedio = suma / cantidad
        promedio = int(promedio) if promedio.is_integer() else promedio

        print("\nEl promedio de las notas es {}.".format(promedio))
    except ValueError:
        print("\nIngresó valores incorrectos.")
    finally:
        repetir()

calcular()