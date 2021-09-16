# 9.	De acuerdo con el siguiente problema, realice el algoritmo en Python (15 pts.)

# Cree una aplicación de Consola que solicite un número de días y que entregue el número de semanas correspondientes a esos días ingresados.  Ej: Si ingreso 9 días, debería entregarme: “Son 1 semana, con 2 días”:

# Hecho por Gabriel Barrientos

print(" Calcular número de semanas ".center(70, "="))

def respuesta(x, y):
    if x == 1 and y == 1:
        return "\nEs {} semana y {} día."
    elif x != 1 and y == 1:
        return "\nSon {} semanas y {} día."
    elif x == 1 and y != 1:
        return "\nEs {} semana y {} días."
    elif x != 1 and y != 1:
        return "\nSon {} semanas y {} días."

def repetir():
    eleccion = input("\n¿Quiere volver a ejecutar el programa? (S/N): ")
    if eleccion.upper() in ("SÍ", "SI", "S"):
        calcular()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")

def calcular():
    try:
        dias = int(input("\nIngrese una cantidad de días: "))
        if dias < 0:
            raise ValueError
        semanas = dias // 7
        dias_restantes = dias % 7

        print(respuesta(semanas, dias_restantes).format(semanas, dias_restantes))

        repetir()

    except ValueError:
        print("\nLos días deben ser un número entero y no pueden ser un número negativo.")
        repetir()

calcular()