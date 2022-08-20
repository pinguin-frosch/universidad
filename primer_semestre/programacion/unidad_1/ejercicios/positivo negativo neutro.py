# 1.- Cree un algoritmo que, al ingresar un número, identifique si es positivo, negativo o neutro

# Hecho por Gabriel Barrientos

print(" Positivo, negativo o neutro ".center(60, "="))
def repetir():
    eleccion = input("\n¿Ejecutar el programa de nuevo? (S/N): ")
    if eleccion.upper() == "S" or eleccion.upper() == "SI" or eleccion.upper() == "SÍ":
        calcular()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")

def calcular():
    try:
        numero = float(input("\nIngrese un número: "))
        if numero > 0:
            print("El número es positivo.")
        elif numero < 0:
            print("El número es negativo.")
        else:
            print("El número es neutro.")
    except ValueError:
        print("No ingresó un número.")
    finally:
        repetir()

calcular()