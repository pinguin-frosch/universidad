# 8.- Dada las horas trabajadas por un trabajador y el valor por hora contratado, calcular su sueldo

# Hecho por Gabriel Barrientos

print(" Calcular sueldo ".center(50, "="))

def repetir():
    eleccion = input("\n¿Quiere volver a ejecutar el programa? (S/N): ")
    if eleccion.upper() in ("SÍ", "SI", "S"):
        sueldo()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")
    pass

def sueldo():
    try:
        horas = int(input("\nIngrese la cantidad de horas trabajadas: "))
        if horas < 0:
            raise ValueError
        valor_hora = float(input("Ingrese el valor pagado por hora $"))

        sueldo = horas * valor_hora
        sueldo = int(sueldo) if sueldo.is_integer() else sueldo

        if sueldo >= 0:
            print("Su sueldo es: ${}".format(sueldo))
        else:
            print("Su sueldo es: ${}. Pero no debería tener un sueldo negativo, ingrese correctamente el valor por hora la próxima vez.".format(sueldo))
    except ValueError:
        print("No le pagan por horas negativas y tampoco por horas parciales.")
    finally:
        repetir()

sueldo()