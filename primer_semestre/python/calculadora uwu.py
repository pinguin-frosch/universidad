#Hecho por Gabriel Barrientos
print("Calculadora simple. Solo para números reales.")
print("\nSi quiere usar números decimales utilice un punto, no una coma.")

numeros = [0, 0]

def suma(x, y):
	try:
		return int(x + y) if (x + y).is_integer() else x + y
	except OverflowError:
		return "El resultado es muy grande"

def resta(x, y):
	try:
		return int(x - y) if (x - y).is_integer() else x - y
	except OverflowError:
		return "El resultado es muy grande"

def multiplicacion(x, y):
	try:
		return int(x * y) if (x *  y).is_integer() else x * y
	except OverflowError:
		return "El resultado es muy grande"

def division(x, y):
	try:
		return int(x / y) if (x / y).is_integer() else x / y
	except ZeroDivisionError:
		return "No se puede dividir por 0"
	except OverflowError:
		return "El resultado es muy grande"

def potenciacion(x, y):
	try:
		return int(x ** y) if (x ** y).is_integer() else x ** y
	except OverflowError:
		return "El resultado es muy grande"
			
def modulo(x, y):
	try:
		return int(x % y) if (x % y).is_integer() else x % y
	except ZeroDivisionError:
		return "No se puede calcular módulo 0"
	except OverflowError:
		return "El resultado es muy grande"

def repetir():
	texto = input("\n¿Ejecutar otra vez? (S/N): ")
	if texto.upper() == "S" or texto.upper() == "SI" or texto.upper() == "SÍ":
		asignacion()
	else:
		input("\nGracias por usar. Pulse intro para salir. ")
		
def asignacion():
	try:
		numeros[0] = float(input("\nIngrese el primer número: "))
		numeros[1] = float(input("Ingrese el segundo número: "))
		
		print("\nLas operaciones son:\n1 : Suma\n2 : Resta\n3 : Multiplicación\n4 : División\n5 : Potenciación\n6 : Módulo")
		
		calcular()
	except ValueError:
		print("\nNo ingresó un número.")
		repetir()
	except AttributeError:
		print("\nAlgo salió mal, probablemente el resultado era un número complejo.")
		repetir()

def calcular():
	operacion = input("\nIngrese la operación: ")
	
	if operacion == "1":
		print("{} + {} = {}".format(int(numeros[0]) if numeros[0].is_integer() else numeros[0], int(numeros[1]) if numeros[1].is_integer() else numeros[1], suma(numeros[0], numeros[1])))
	elif operacion == "2":
		print("{} - {} = {}".format(int(numeros[0]) if numeros[0].is_integer() else numeros[0], int(numeros[1]) if numeros[1].is_integer() else numeros[1], resta(numeros[0], numeros[1])))
	elif operacion == "3":
		print("{} * {} = {}".format(int(numeros[0]) if numeros[0].is_integer() else numeros[0], int(numeros[1]) if numeros[1].is_integer() else numeros[1], multiplicacion(numeros[0], numeros[1])))
	elif operacion == "4":
		print("{} / {} = {}".format(int(numeros[0]) if numeros[0].is_integer() else numeros[0], int(numeros[1]) if numeros[1].is_integer() else numeros[1], division(numeros[0], numeros[1])))
	elif operacion == "5":
		print("{} ^ {} = {}".format(int(numeros[0]) if numeros[0].is_integer() else numeros[0], int(numeros[1]) if numeros[1].is_integer() else numeros[1], potenciacion(numeros[0], numeros[1])))
	elif operacion == "6":
		print("{} % {} = {}".format(int(numeros[0]) if numeros[0].is_integer() else numeros[0], int(numeros[1]) if numeros[1].is_integer() else numeros[1], modulo(numeros[0], numeros[1])))
	else:
		print("Operacion incorrecta.")
	
	repetir()
	
asignacion()