# 7.	De acuerdo con el siguiente problema, realice el algoritmo en Python (47 pts.)

# Cree una aplicación de Consola que simule el comportamiento de una maquina dispensadora de dulces, considerando:
# a)	Cree un menú con 5 productos.
# b)	Valide los datos ingresados correctamente, en caso de ingresar un valor erróneo volver a solicitar.
# c)	Utilice listas para administrar los productos y sus precios.
# d)	Validar correctamente el ingreso del dinero, en caso de que el dinero sea insuficiente, debe mostrar mensaje y solicitar ingresar más dinero, esto hasta que permita realizar la compra del producto.
# e)	La aplicación debe permitir devolver un vuelto, en caso de ser necesario.
# f)	Aplicar de manera autónoma la comunicación del algoritmo (retroalimentación entre usuario y aplicación de consola).
# g)	Una vez finalizada la aplicación .py, agregar código a continuación:

# Hecho por Gabriel Barrientos

print("========= Máquina dispensadora de dulces =========")

precios = [350, 300, 350, 400, 200]
productos = ["Chocman", "Super 9", "Bachata", "Triton", "Carioca"]

def repetir():
    eleccion = input("\n¿Quiere volver a comprar? (S/N): ")
    if eleccion.upper() in ("SI", "SÍ", "S"):
        compra()
    else:
        input("\nGracias por usar la máquina, que tenga un buen día. ")

def diferencia(dinero, precio, opcion = 1):
    if opcion == 1:
        vuelto = dinero - precio
        if type(dinero) == float or type(precio) == float:
            vuelto = int(vuelto) if vuelto.is_integer() else vuelto
            return vuelto
        else:
            return vuelto
    elif opcion == 2:
        diferencia = precio - dinero
        if type(dinero) == float or type(precio) == float:
            diferencia = int(diferencia) if diferencia.is_integer() else diferencia
            return diferencia
        else:
            return diferencia

def compra():
    print("")
    for i in range(5):
        print("{}) {} - ${}".format(i + 1, productos[i], precios[i]))

    try:
        dulce = int(input("\nSeleccione un producto: "))
        if dulce not in (1, 2, 3, 4, 5):
            raise IndexError

        dinero = float(input("\nIngrese el dinero $"))
        dinero = int(dinero) if dinero.is_integer() else dinero
        if dinero < 0:
            raise ValueError

        while dinero < precios[dulce - 1]:
            print("\nDinero: ${}, le faltan ${}".format(dinero, diferencia(dinero, precios[dulce - 1], 2)))
            dinero_extra = float(input("Dinero insuficiente, ingrese más dinero $"))
            if dinero_extra < 0:
                print("No puede quitar su dinero, solo puede añadir más.")
                continue
            dinero += dinero_extra
            dinero = int(dinero) if dinero.is_integer() else dinero

        if dinero >= precios[dulce - 1]:
            print("\nAquí está su {}, su vuelto es ${}. Gracias por su compra.".format(productos[dulce - 1], diferencia(dinero, precios[dulce - 1]))) 

        repetir()

    except ValueError:
        print("\nIngresó un valor incorrecto.")
        repetir()

    except IndexError:
        print("\nEse producto no existe.")
        repetir()

compra()