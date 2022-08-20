# debe mostrar mensaje y solicitar ingresar más dinero, esto hasta que permita realizar
# la compra del producto.La aplicación debe permitir devolver un vuelto, en caso de
# ser necesario.

print("**")
print("*     ＣＯＭＰＲＡＳ   ＥＮ   ＭＡＱＵＩＮＩＴＡ   ＤＥ   ＤＵＬＣＥＳ(　・ω・)⊃-[二二]          *")
print("**")

productos = ["Fanta", "Papas Fritas", "Chettos", "Oreo", "Donas"]
precio = [700, 750, 800, 600, 500]
print("1", productos[0], precio[0])
print("2", productos[1], precio[1])
print("3", productos[2], precio[2])
print("4", productos[3], precio[3])
print("5", productos[4], precio[4])
Maquina = int(input("Ingrese un producto para solicitar su compra : "))
if Maquina == 1 or Maquina == 2 or Maquina == 3 or Maquina == 4 or Maquina == 5:
    Dinero = float(input("Porfavor a coninuacion introdusca su dinero $: "))
    while Dinero < precio[Maquina-1]:
        Saldoextra = float(input("Falta dinero, ingrese el monto que desde agregar: "))
        Dinero += Saldoextra
    if Dinero > precio[Maquina-1]:
        print("Usted puede comprar")
    if Dinero == precio[Maquina-1]:
        print("Usted puede comprar")
else:
    print("Usted escojio un producto inexistente")