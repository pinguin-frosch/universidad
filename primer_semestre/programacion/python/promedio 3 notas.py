print("****************************** Promedio de 3 notas ******************************\n")
print("Se calculará el promedio de 3 notas. Ingréselas en este formato: 56, 33, 65, 23.\n")
print("Nótese que las notas no pueden ser mayores que 70 o menores que 10.")

nota1 = int(input("Ingrese nota 1: "))
while nota1 < 10 or nota1 > 70:
    nota1 = int(input("Valor incorrecto, ingrese otra vez la nota 1: "))

nota2 = int(input("Ingrese nota 2: "))
while nota2 < 10 or nota2 > 70:
    nota2 = int(input("Valor incorrecto, ingrese otra vez la nota 2: "))

nota3 = int(input("Ingrese nota 3: "))
while nota3 < 10 or nota3 > 70:
    nota3 = int(input("Valor incorrecto, ingrese otra vez la nota 3: "))

suma_parcial = nota1 + nota2 + nota3
divisor = 3

if suma_parcial % divisor == 0:
    promedio = int(suma_parcial / divisor)
    print("\nEl promedio entre " + str(nota1) +  ", " + str(nota2), "y", str(nota3), "es " + str(promedio))
else:
    placeholder = "{:.2f}"
    promedio = suma_parcial / divisor
    print("\nEl promedio entre " + str(nota1) +  ", " + str(nota2), "y", str(nota3), "es " + placeholder.format(promedio))

#Hecho por Gabriel Barrientos