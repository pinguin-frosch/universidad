# 11.- Cree un algoritmo que permita convertir entre °C y °F, permitiendo elegir al usuario la opción que desea realizar, para esto se realizara un menú donde utilizaremos las sentencias repetir y según.

# Hecho por Gabriel Barrientos

print(" Transformar entre °C y °F ".center(50, "="))

def repetir():
    eleccion = input("\n¿Repetir el programa? (S/N): ")
    if eleccion.upper() == "S" or eleccion.upper() == "SI" or eleccion.upper() == "SÍ":
        calcular()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")

def celsius_a_fahrenheit(x):
    return int(1.8 * x + 32) if (1.8 * x + 32).is_integer() else (1.8 * x + 32)

def fahrenheit_a_celsius(x):
    return int((x - 32) / 1.8) if ((x - 32) / 1.8).is_integer() else ((x - 32) / 1.8)

def calcular():
    print("\n 1 - Celsius a Fahrenheit.\n 2 - Fahrenheit a Celsius.")
    eleccion = input("\nSeleccione una de las dos opciones: ")

    if eleccion == "1":
        temperatura = float(input("\nIngrese una temperatura en grados Celsius: "))
        temperatura = int(temperatura) if temperatura.is_integer() else temperatura
        print("\n{}°C es igual que {}°F.".format(temperatura, celsius_a_fahrenheit(temperatura)))
    elif eleccion == "2":
        temperatura = float(input("\nIngrese una temperatura en grados Fahrenheit: "))
        temperatura = int(temperatura) if temperatura.is_integer() else temperatura
        print("\n{}°F es igual que {}°C.".format(temperatura, fahrenheit_a_celsius(temperatura)))
    else:
        print("\nEsa opción no existe.")
    
    repetir()

calcular()