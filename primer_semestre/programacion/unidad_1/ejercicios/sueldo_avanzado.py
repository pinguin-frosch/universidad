# 9.- A un trabajador le pagan según sus horas trabajadas y la tarifa está a un valor por hora. Si la cantidad de horas trabajadas es mayor a 45 horas, la tarifa por hora se incrementa en un 50% para las horas extras (sobre las 45 horas). Calcular el salario del trabajador dadas las horas trabajadas y la tarifa.

# Hecho por Gabriel Barrientos

print(" Calcular sueldo con bonificación sobre 45 horas ".center(80, "="))

def repetir():
    eleccion = input("\n¿Quiere volver a ejecutar el programa? (S/N): ")
    if eleccion.upper() in ("SÍ", "SI", "S"):
        sueldo()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")

def sueldo():
    try:
        horas = int(input("\nIngrese la cantidad de horas trabajadas: "))
        if horas < 0:
            raise ValueError

        valor_hora = float(input("Ingrese el valor pagado por hora $"))
        if valor_hora < 0:
            raise ValueError

        bono = valor_hora * 1.5
        sueldo = 0

        if horas >= 0 and horas <= 45:
            sueldo = horas * valor_hora
            if type(sueldo) == float:
                sueldo = int(sueldo) if sueldo.is_integer() else sueldo
            print(f"Su sueldo es ${sueldo}. Sin horas extras.")

        else:
            sueldo = (45 * valor_hora) + ((horas - 45) * bono)
            if type(sueldo) == float:
                sueldo = int(sueldo) if sueldo.is_integer() else sueldo
            print(f"Su sueldo es ${sueldo}. Con {horas - 45} horas extras.")

    except ValueError:
        print("No le pagan por horas negativas ni por horas parciales, tampoco puede tener un valor por hora negativo.")
    finally:
        repetir()

sueldo()