numeros = []

numeros.append(float(input("\nIngrese el primer número: ")))
numeros.append(float(input("Ingrese el segundo número: ")))

while True:

    print("\nLas operaciones son:\n1 : Suma\n2 : Resta\n3 : Multiplicación\n4 : División\n")

    eleccion = input("Ingrese una opción: ")

    if eleccion == "1":
        resultado = int(numeros[0] + numeros[1]) if (numeros[0] + numeros[1]).is_integer() else numeros[0] + numeros[1]
        numeros[0] = int(numeros[0]) if numeros[0].is_integer() else numeros[0]
        numeros[1] = int(numeros[1]) if numeros[1].is_integer() else numeros[1]
        print(str(numeros[0]) + " + " + str(numeros[1]) + " = " + str(resultado) + "\n")

    elif eleccion == "2":
        resultado = int(numeros[0] - numeros[1]) if (numeros[0] - numeros[1]).is_integer() else numeros[0] - numeros[1]
        numeros[0] = int(numeros[0]) if numeros[0].is_integer() else numeros[0]
        numeros[1] = int(numeros[1]) if numeros[1].is_integer() else numeros[1]
        print(str(numeros[0]) + " - " + str(numeros[1]) + " = " + str(resultado) + "\n")

    elif eleccion == "3":
        resultado = int(numeros[0] * numeros[1]) if (numeros[0] * numeros[1]).is_integer() else numeros[0] * numeros[1]
        numeros[0] = int(numeros[0]) if numeros[0].is_integer() else numeros[0]
        numeros[1] = int(numeros[1]) if numeros[1].is_integer() else numeros[1]
        print(str(numeros[0]) + " * " + str(numeros[1]) + " = " + str(resultado) + "\n")

    elif eleccion == "4":
        resultado = int(numeros[0] / numeros[1]) if (numeros[0] / numeros[1]).is_integer() else numeros[0] / numeros[1]
        numeros[0] = int(numeros[0]) if numeros[0].is_integer() else numeros[0]
        numeros[1] = int(numeros[1]) if numeros[1].is_integer() else numeros[1]
        print(str(numeros[0]) + " / " + str(numeros[1]) + " = " + str(resultado) + "\n")

    else:
        print("Opción inválida\n")

    texto = input("¿Ejecutar otra vez? (S/N) ").lower()

    if (texto != "s"):
        break

    numeros[0] = float(input("\nIngrese el primer número: "))
    numeros[1] = float(input("Ingrese el segundo número: "))