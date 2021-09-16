# 2.- Crear un algoritmo que calcule la raíz cuadrada del número que introduzca el usuario. Si se introduce un número negativo, debe mostrar un mensaje de error y volver a pedirlo (tantas veces como sea necesario).

# Hecho por Gabriel Barrientos

print(" Raíz cuadrada de un número ".center(50, "="))

def calcular():
    try:
        numero = float(input("\nIngrese un número: "))

        while numero < 0:
            numero = float(input("\nNo puede ser menor que 0, ingréselo de nuevo: "))

        numero = int(numero) if numero.is_integer() else numero
        resultado = int(numero ** (0.5)) if (numero ** (0.5)).is_integer() else (numero ** (0.5))

        print("\nLa raíz cuadrada de {} es {}.".format(numero, resultado))
    except ValueError:
        print("\nNo ingresó un número.")
    finally:
        repetir()

def repetir():
    eleccion = input("\n¿Repetir? (S/N): ")
    if eleccion.upper() == "S" or eleccion.upper() == "SI" or eleccion.upper() == "SÍ":
        calcular()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")

calcular()