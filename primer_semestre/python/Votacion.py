#Hecho por Gabriel Barrientos
from datetime import date

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

print("\nCalculadora de edad. Permite saber si puede votar.")
fecha_actual = date.today()

def repetir():
    desicion = input("\n¿Quiere ejecutar el programa otra vez? (S/N): ")

    if desicion.upper() == "SI" or desicion.upper() == "SÍ" or desicion.upper() == "S":
        asignacion()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")

def asignacion():
    try:
        global fecha_nacimiento
        fecha_nacimiento = input("\nIngrese su fecha de nacimiento en formato día-mes-año (Ejemplo: 9-12-1988): ").split("-")

        for i in range(len(fecha_nacimiento)):
            fecha_nacimiento[i] = int(fecha_nacimiento[i])
            
        fecha_nacimiento = date(fecha_nacimiento[2], fecha_nacimiento[1], fecha_nacimiento[0])

        calcular()
    except IndexError:
        print("\nLe faltó ingresar datos.")
        repetir()

    except ValueError:
        print("\nIngresó una fecha incorrecta o guiones extra.")
        repetir()

def calcular():
    delta = fecha_actual - fecha_nacimiento

    texto = "{}-{}-{} ({} de {} de {})".format(fecha_nacimiento.day, fecha_nacimiento.month, fecha_nacimiento.year, fecha_nacimiento.day, meses[fecha_nacimiento.month - 1], fecha_nacimiento.year)

    if delta.days >= 6575:
        print("\nSu fecha de nacimiento es: " + texto + ". Es mayor de edad. Tiene permitido votar.")
    elif delta.days < 6575 and delta.days >= 0:
        print("\nSu fecha de nacimiento es: " + texto + ". Es menor de edad. No tiene permitido votar.")
    else:
        print("\nEdad incorrecta. No puede tener una edad negativa. Su supuesta fecha de nacimiento es: " + texto + ".") 

    repetir()

asignacion()