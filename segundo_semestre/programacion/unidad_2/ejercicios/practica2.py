class Estado:
    cod_estado: str
    nombre_estado: str
    
    def __init__(self, cod_estado, nombre_estado):
        self.cod_estado = cod_estado
        self.nombre_estado = nombre_estado
        
    def get_cod_estado(self):
        return self.cod_estado
    
    def set_cod_estado(self, cod_estado):
        self.cod_estado = cod_estado
        
    def get_nombre_estado(self):
        return self.nombre_estado
    
    def set_nombre_estado(self, nombre_estado):
        self.nombre_estado = nombre_estado
        
    def info_estado(self):
        return f"Código estado: {self.get_cod_estado()}, Nombre estado: {self.get_nombre_estado()}"

class Personas:
    run: str
    nombres: str
    
    def __init__(self, run, nombres):
        self.run = run
        self.nombres = nombres
        
    def get_run(self):
        return self.run
    
    def set_run(self, run):
        self.run = run
        
    def get_nombres(self):
        return self.nombres
        
    def set_nombres(self, nombres):
        self.nombres = nombres
        
    def info_personas(self):
        return f"Run: {self.get_run()}, Nombres: {self.get_nombres()}"

class Alumnos(Personas):
    telefono: str
    cod_alumnos_estado: Estado
    
    def __init__(self, run, nombres, telefono, cod_alumnos_estado):
        self.run = run
        self.nombres = nombres
        self.telefono = telefono
        self.cod_alumnos_estado = cod_alumnos_estado
    
    def get_telefono(self):
        return self.telefono
    
    def set_telefono(self, telefono):
        self.telefono = telefono
        
    def get_cod_alumnos_estado(self):
        return self.cod_alumnos_estado
    
    def set_cod_alumnos_estado(self, cod_alumnos_estado):
        self.cod_alumnos_estado = cod_alumnos_estado
        
    def info_alumnos(self):
        return f"{self.info_personas()}, Teléfono: {self.get_telefono()}, Estado: {self.cod_alumnos_estado.info_estado()}"

def menu():
    print("\n1 - Agregar estado")
    print("2 - Información estado")
    print("3 - Agregar alumno")
    print("4 - Información alumno")
    print("5 - Ver opciones")
    print("6 - Salir")

menu()
valor = True
while(valor):
    opcion = input("\nIngrese una opción (5 para ver opciones): ")

    # Agregar estado
    if opcion == "1":
        codigo = input("\nCódigo: ")
        nombre = input("Nombre: ")
        es1 = Estado(codigo, nombre)

    # Información estado
    elif opcion == "2":
        # Si el estado no existe no podemos imprimir su información
        try:
            print(f"\n{es1.info_estado()}")
        except NameError:
            print("\nAún no existe ningún estado.")

    # Agregar alumno
    elif opcion == "3":
        # No podemos crear un alumno si no tenemos ningún estado
        try:
            es1
            run = input("\nRun: ")
            nombres = input("Nombres: ")
            telefono = input("Teléfono: ")
            estado = es1
            alumno = Alumnos(run, nombres, telefono, estado)
        except NameError:
            print("\nSe debe crear un estado antes del alumno.")

    # Información alumno
    elif opcion == "4":
        # Si no hay alumno no podemos mostrar su información
        try:
            print(f"\n{alumno.info_alumnos()}")
        except NameError:
            print("\nAún no existe ningún alumno.")

    # Ver opciones
    elif opcion == "5":
        menu()

    # Salir
    elif opcion == "6":
        print("\nSaliendo...")
        valor = False

    # Ninguna opción
    else:
        print("\nIngresó una opción que no existe.")