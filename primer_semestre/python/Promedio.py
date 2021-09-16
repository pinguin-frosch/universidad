print("Calculadora de promedios.")
print("\nRecuerde no colocar más de un espacio entre las notas, tampoco coloque un espacio al final de la última nota.")

def repetir():
    desicion = input("\n¿Ejecutar otra vez el programa? (S/N): ")
    
    if desicion.upper() == "SI" or desicion.upper() == "S" or desicion.upper() == "SÍ":
        asignacion()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")

def asignacion():
    try:
        global notas
        notas = input("\nIngrese las notas separadas por espacios: ").split(" ")

        for x in range(len(notas)):
            notas[x] = float(notas[x])

        calcular()

    except ValueError:
        print("\nIngresó un valor incorrecto o colocó espacios donde no debía.")
        repetir()

def calcular():
    suma = 0

    for x in range(len(notas)):
        suma += notas[x]

    promedio = int(suma / len(notas)) if (suma / len(notas)).is_integer() else suma / len(notas)
    
    print("El promedio es: {}".format(promedio))
    repetir()

asignacion()