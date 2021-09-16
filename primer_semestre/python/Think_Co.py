# 10.- Usted hizo con contrato con Think & Co, la empresa de Rafael Garay, en la cual firmo un contrato por una inversión a un año de plazo, con una ganancia de un 18% anual, de acuerdo a la fecha de firma del contrato, fecha de retiro del monto y cantidad del monto a invertir. Calcule la totalidad de ganancia.
# Importante: si dichos fondos se retiran antes de un año, generara una pérdida de un 7% de lo invertido.

# Hecho por Gabriel Barrientos

from datetime import date

print(" Bienvenido a Think & Co ".center(90, "="))

def respuesta_año(x):
    if x == 1:
        return "año"
    else:
        return "años"

def repetir():
    eleccion = input("\n¿Quiere volver a ejecutar el programa? (S/N): ")
    if eleccion.upper() in ("SÍ", "SI", "S"):
        main()
    else:
        input("\nGracias por usar nuestro simulador de inversión. Pulse intro para salir. ")

def main():
    try:
        fecha_contrato_cruda = input("\nIngrese la fecha de contrato en formato dd-mm-aaaa: ").split("-")
        for x in range(3):
            fecha_contrato_cruda[x] = int(fecha_contrato_cruda[x])
        fecha_contrato = date(fecha_contrato_cruda[2], fecha_contrato_cruda[1], fecha_contrato_cruda[0])

        fecha_retiro_cruda = input("\nIngrese la fecha de retiro en formato dd-mm-aaaa: ").split("-")
        for x in range(3):
            fecha_retiro_cruda[x] = int(fecha_retiro_cruda[x])
        fecha_retiro = date(fecha_retiro_cruda[2], fecha_retiro_cruda[1], fecha_retiro_cruda[0])

        delta = fecha_retiro - fecha_contrato
        if delta.days < 0:
            raise ValueError

        inversion = float(input("\nIngrese el monto de inversión $"))
        inversion = int(inversion) if inversion.is_integer() else inversion

        años = 0
        if (fecha_retiro.month > fecha_contrato.month) or (fecha_retiro.month == fecha_contrato.month and fecha_retiro.day >= fecha_contrato.day) or (fecha_retiro.year == fecha_contrato.year):
            años = fecha_retiro.year - fecha_contrato.year
        else:
            años = fecha_retiro.year - fecha_contrato.year - 1

        if años >= 1:
            ganancia_por_año = inversion * 0.18
            ganancia_total = ganancia_por_año * años
            if type(ganancia_total) == float:
                ganancia_total = int(ganancia_total) if ganancia_total.is_integer() else ganancia_total
            monto_total = inversion + ganancia_total
            if type(monto_total) == float:
                monto_total = int(monto_total) if monto_total.is_integer() else monto_total
            print(f"\nActualmente lleva {años} {respuesta_año(años)} invirtiendo, con eso generó una ganancia extra de ${ganancia_total}, que sumados a los ${inversion} que usted invirtió le da un total de ${monto_total} para retirar ahora mismo si lo desea.")
        if años == 0:
            perdida = inversion * 0.07
            if type(perdida) == float:
                perdida = int(perdida) if perdida.is_integer() else perdida
            monto_total = inversion - perdida
            if type(monto_total) == float:
                monto_total = int(monto_total) if monto_total.is_integer() else monto_total
            print(f"\nComo no ha pasado un año desde su inversión si retira ahora tendrá una pérdida de ${perdida}, con esa pérdida y su inversión inicial de ${inversion} puede retirar ${monto_total} si así lo desea, pero le recomendamos que espere un poco más para obtener un interés a favor.")

    except ValueError:
        print("Se equivocó al ingresar la fecha o la fecha de retiro es anterior a la de contrato.")

    finally:
        repetir()

main()