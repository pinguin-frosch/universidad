margen = 30 # Controla el margen de la primera columna al mostrar los datos
ancho = 50 # Controla el ancho de los títulos

class Estado:
    cod_estado: int
    nombre_estado: str

    # Constructor semiautomático
    def __init__(self, cod_estado: int) -> None:
        self.cod_estado = cod_estado

    # Getters
    def get_cod_estado(self) -> int:
        return self.cod_estado

    def get_nombre_estado(self) -> str:
        return self.nombre_estado

    # Setters
    def set_cod_estado(self, cod_estado: int) -> None:
        self.cod_estado = cod_estado

    def set_nombre_estado(self, nombre_estado: str) -> None:
        self.nombre_estado = nombre_estado

    # Métodos
    def info_estado(self) -> str:
        return "Código estado: ".ljust(margen) + f"{self.get_cod_estado()}\n" +\
            "Nombre estado: ".ljust(margen) + f"{self.get_nombre_estado()}"

class Profesion:
    cod_profesion: str
    nombre_profesion: str

    # Constructor semiautomático
    def __init__(self, cod_profesion: str) -> None:
        self.cod_profesion = cod_profesion

    # Getters
    def get_codigo_profesion(self) -> str:
        return self.cod_profesion

    def get_nombre_profesion(self) -> str:
        return self.nombre_profesion

    # Setters
    def set_codigo_profesion(self, codigo_profesion: str) -> None:
        self.cod_profesion = codigo_profesion

    def set_nombre_profesion(self, nombre_profesion: str) -> None:
        self.nombre_profesion = nombre_profesion

    # Métodos
    def info_profesion(self) -> str:
        return "Código profesión: ".ljust(margen) + f"{self.get_codigo_profesion()}\n" +\
            "Nombre profesión: ".ljust(margen) + f"{self.get_nombre_profesion()}"

class Licencia:
    cod_licencia: str
    detalle_licencia: str

    # Constructor semiautomático
    def __init__(self, cod_licencia: str) -> None:
        self.cod_licencia = cod_licencia

    # Getters
    def get_codigo_licencia(self) -> str:
        return self.cod_licencia

    def get_detalle_licencia(self) -> str:
        return self.detalle_licencia

    # Setters
    def set_codigo_licencia(self, codigo_licencia: str) -> None:
        self.cod_licencia = codigo_licencia

    def set_detalle_licencia(self, detalle_licencia: str) -> None:
        self.detalle_licencia = detalle_licencia

    # Métodos
    def info_licencia(self) -> str:
        return "Código licencia: ".ljust(margen) + f"{self.get_codigo_licencia()}\n" +\
            "Detalle licencia: ".ljust(margen) + f"{self.get_detalle_licencia()}"

class Empleado:
    run_empleado: str
    nombres_empleado: str
    cod_estado: Estado
    telefono: str # Lo cambié a str porque tiene más sentido en este contexto
    clave: str

    # Constructor semiautomático
    def __init__(self, run_empleado: str, nombres_empleado: str) -> None:
        self.run_empleado = run_empleado
        self.nombres_empleado = nombres_empleado
    
    # Getters
    def get_run_empleado(self) -> str:
        return self.run_empleado

    def get_nombres_empleado(self) -> str:
        return self.nombres_empleado

    def get_cod_estado(self) -> Estado:
        return self.cod_estado

    def get_telefono(self) -> str:
        return self.telefono

    def get_clave(self) -> str:
        return self.clave

    # Setters
    def set_run_empleado(self, run_empleado: str) -> None:
        self.run_empleado = run_empleado

    def set_nombres_empleado(self, nombres_empleado: str) -> None:
        self.nombres_empleado = nombres_empleado

    def set_cod_estado(self, cod_estado: Estado) -> None:
        self.cod_estado = cod_estado

    def set_telefono(self, telefono: str) -> None:
        self.telefono = telefono

    def set_clave(self, clave: str) -> None:
        self.clave = clave

    # Métodos
    def info_empleado(self) -> str:
        return "Run: ".ljust(margen) + f"{self.get_run_empleado()}\n" +\
            "Nombres: ".ljust(margen) + f"{self.get_nombres_empleado()}\n" +\
            "Teléfono: ".ljust(margen) + f"{self.get_telefono()}\n" +\
            "Clave: ".ljust(margen) + f"{self.get_clave()}\n" +\
            f"{self.cod_estado.info_estado()}"

class Administrativo(Empleado):
    cod_carrera: Profesion
    direccion: str

    # Constructor semiautomático
    def __init__(self, run_empleado: str, nombres_empleado: str, direccion: str) -> None:
        super().__init__(run_empleado, nombres_empleado)
        self.direccion = direccion

    # Getters
    def get_cod_carrera(self) -> Profesion:
        return self.cod_carrera

    def get_direccion(self) -> str:
        return self.direccion

    # Setters
    def set_cod_carrera(self, cod_carrera: Profesion) -> None:
        self.cod_carrera = cod_carrera

    def set_direccion(self, direccion: str) -> None:
        self.direccion = direccion

    # Métodos
    def info_administrativo(self) -> str:
        return f"{self.info_empleado()}\n" +\
            "Dirección: ".ljust(margen) + f"{self.get_direccion()}\n" +\
            f"{self.cod_carrera.info_profesion()}"

class Conductor(Empleado):
    cod_licencia: Licencia
    correo: str

    # Constructor semiautomático
    def __init__(self, run_empleado: str, nombres_empleado: str, cod_licencia: Licencia) -> None:
        super().__init__(run_empleado, nombres_empleado)
        self.cod_licencia = cod_licencia

    # Getters
    def get_cod_licencia(self) -> Licencia:
        return self.cod_licencia

    def get_correo(self) -> str:
        return self.correo

    # Setters
    def set_cod_licencia(self, cod_licencia: Licencia) -> None:
        self.cod_licencia = cod_licencia

    def set_correo(self, correo: str) -> None:
        self.correo = correo

    # Métodos
    def info_conductor(self) -> str:
        return f"{self.info_empleado()}\n" +\
            "Correo: ".ljust(margen) + f"{self.get_correo()}\n" +\
            f"{self.cod_licencia.info_licencia()}"

def menu() -> None:
    print("\n 1 - Agregar estado")
    print(" 2 - Agregar licencia")
    print(" 3 - Agregar profesión")
    print(" 4 - Agregar conductor")
    print(" 5 - Agregar administrativo")
    print(" 6 - Información estado")
    print(" 7 - Información licencia")
    print(" 8 - Información profesión")
    print(" 9 - Información conductor")
    print("10 - Información administrativo")
    print("11 - Ver opciones")
    print("12 - Salir")

menu()

valor = True
while(valor):
    opcion = input("\nIngrese una opción (11 para ver opciones): ")

    # Agregar estado
    if opcion == "1":
        try:
            cod_estado = int(input("\n" + "Código del estado: ".ljust(margen)))
        except ValueError:
            print("\nEl código debe ser un número entero")
            continue

        nombre_estado = input("Nombre del estado: ".ljust(margen))

        # Creando el estado
        estado = Estado(cod_estado)
        estado.set_nombre_estado(nombre_estado)

    # Agregar licencia
    elif opcion == "2":
        cod_licencia = input("\n" + "Código de la licencia: ".ljust(margen))
        detalle_licencia = input("Detalle de la licencia: ".ljust(margen))

        # Creando la licencia
        licencia = Licencia(cod_licencia)
        licencia.set_detalle_licencia(detalle_licencia)

    # Agregar profesión
    elif opcion == "3":
        cod_profesion = input("\n" + "Código de la profesión: ".ljust(margen))
        nombre_profesion = input("Nombre de la profesión: ".ljust(margen))

        # Creando la profesión
        profesion = Profesion(cod_profesion)
        profesion.set_nombre_profesion(nombre_profesion)

    # Agregar conductor
    elif opcion == "4":
        try:
            licencia
            estado
        except NameError:
            print("\nDebe ingresar el estado y la licencia antes")
            continue

        run_conductor = input("\n" + "Run del conductor: ".ljust(margen))
        nombres_conductor = input("Nombres del conductor: ".ljust(margen))
        telefono_conductor = input("Teléfono del conductor: ".ljust(margen))
        clave_conductor = input("Clave del conductor: ".ljust(margen))
        correo_conductor = input("Correo del conductor: ".ljust(margen))

        # Creando el conductor
        conductor = Conductor(run_conductor, nombres_conductor, licencia)
        conductor.set_cod_estado(estado)
        conductor.set_telefono(telefono_conductor)
        conductor.set_clave(clave_conductor)
        conductor.set_correo(correo_conductor)

    # Agregar administrativo
    elif opcion == "5":
        try:
            profesion
            estado
        except NameError:
            print("\nDebe ingresar el estado y la profesión antes")
            continue

        run_administrativo = input("\n" + "Run del administrativo: ".ljust(margen))
        nombres_administrativo = input("Nombres del administrativo: ".ljust(margen))
        telefono_administrativo = input("Teléfono del administrativo: ".ljust(margen))
        clave_administrativo = input("Clave del administrativo: ".ljust(margen))
        direccion_administrativo = input("Dirección del administrativo: ".ljust(margen))

        # Creando el administrativo
        administrativo = Administrativo(run_administrativo, nombres_administrativo, direccion_administrativo)
        administrativo.set_cod_estado(estado)
        administrativo.set_telefono(telefono_administrativo)
        administrativo.set_clave(clave_administrativo)
        administrativo.set_cod_carrera(profesion)

    # Información estado
    elif opcion == "6":
        try:
            print("\n" + " Info estado ".center(ancho, "*"))
            print(f"{estado.info_estado()}")
        except NameError:
            print("Aún no existe un estado")
        finally:
            print(" Fin info estado ".center(ancho, "*"))

    # Información licencia
    elif opcion == "7":
        try:
            print("\n" + " Info licencia ".center(ancho, "*"))
            print(f"{licencia.info_licencia()}")
        except NameError:
            print("Aún no existe una licencia")
        finally:
            print(" Fin info licencia ".center(ancho, "*"))

    # Información profesión
    elif opcion == "8":
        try:
            print("\n" + " Info profesión ".center(ancho, "*"))
            print(f"{profesion.info_profesion()}")
        except NameError:
            print("Aún no existe una profesión")
        finally:
            print(" Fin info profesión ".center(ancho, "*"))

    # Información conductor
    elif opcion == "9":
        try:
            print("\n" + " Info conductor ".center(ancho, "*"))
            print(f"{conductor.info_conductor()}")
        except NameError:
            print("Aún no existe un conductor")
        finally:
            print(" Fin info conductor ".center(ancho, "*"))

    # Información administrativo
    elif opcion == "10":
        try:
            print("\n" + " Info administrativo ".center(ancho, "*"))
            print(f"{administrativo.info_administrativo()}")
        except NameError:
            print("Aún no existe un adminstrativo")
        finally:
            print(" Fin info administrativo ".center(ancho, "*"))

    # Ver opciones
    elif opcion == "11":
        menu()

    # Salir
    elif opcion == "12":
        valor = False
        print("\nSaliendo...")

    else:
        print("\nNo es una opción valida")