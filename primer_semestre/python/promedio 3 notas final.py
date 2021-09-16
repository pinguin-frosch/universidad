notas = []

notas.append(input("\nIngrese nota 1: "))
notas.append(input("Ingrese nota 2: "))
notas.append(input("Ingrese nota 3: "))

suma = 0

for x in range(3):
    suma += float(notas[x])

promedio = int(suma / 3) if (suma / 3).is_integer() else (suma / 3)

print("\nEl promedio entre {}, {} y {} es {}".format(notas[0], notas[1], notas[2], promedio))

input("Pulse intro para salir.")