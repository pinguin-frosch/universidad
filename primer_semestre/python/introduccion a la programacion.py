# 5.- Crear un algoritmo que permita obtener el promedio de sus 3 notas obtenidas en el módulo “Introducción a la programación”

# Hecho por Gabriel Barrientos

print(" Promedio de 3 notas ".center(70, "="))

def determinar(x):
    if x >= 40 and x <= 70:
        return "aprobó"
    if x >= 10 and x < 40:
        return "reprobó"

def repetir():
    eleccion = input("\n¿Volver a ejecutar? (S/N): ")
    if eleccion.upper() == "S" or eleccion.upper() == "SI" or eleccion.upper() == "SÍ":
        calcular()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")

def calcular():
    try:
        print("\nRecuerde ingresar las notas en formato: 70, 10, 34, etc.")

        notas = [0, 0, 0]
        notas[0] = int(input("\nIngrese la nota 1: "))
        while notas[0] < 10 or notas[0] > 70:
            print("\nLas notas no pueden ser mayores que 70 o menores que 10.")
            notas[0] = int(input("Ingrese nuevamente la nota 1: "))

        notas[1] = int(input("\nIngrese la nota 2: "))
        while notas[1] < 10 or notas[1] > 70:
            print("\nLas notas no pueden ser mayores que 70 o menores que 10.")
            notas[1] = int(input("Ingrese nuevamente la nota 2: "))

        notas[2] = int(input("\nIngrese la nota 3: "))
        while notas[2] < 10 or notas[2] > 70:
            print("\nLas notas no pueden ser mayores que 70 o menores que 10.")
            notas[2] = int(input("Ingrese nuevamente la nota 3: "))

        suma = 0
        
        for i in range(len(notas)):
            suma += notas[i]

        promedio = suma / 3
        promedio = int(promedio) if promedio.is_integer() else promedio

        print(f"\nEl promedio entre {notas[0]}, {notas[1]} y {notas[2]} es {promedio}.\n\nEl/la estudiante {determinar(promedio)} el módulo \"Introducción a la programación\".")
    except ValueError:
        print("\nNo ingresó notas o usó números decimales.")
    finally:
        repetir()

calcular()