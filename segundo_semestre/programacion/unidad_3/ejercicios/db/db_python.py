import pymysql
from sys import exit

from pymysql.err import Error

def error(e):
    print(f"Error {e.args[0]}: {e.args[1]}")

print("MySQL - Python")

class ConexionBD:
    def __init__(self, host, user, passwd, db):
        try:
            print(f"\nIniciando conexión en {host} en la base de datos {db}...")
            self.connection = pymysql.connect(
                host=host,
                user=user,
                passwd=passwd,
                db=db
            )
            self.cursor = self.connection.cursor()
            print("Conexión exitosa.")
        except pymysql.Error as e:
            error(e)
            print("Finalizando sesión...")
            exit(1)

    def autentificar_persona(self, run, clave):
        try:
            print("\nAutentificando usuario...")
            consulta = f"select concat(nombres, ' ', apellidos) as 'Nombre completo', telefono from persona where run = '{run}' and clave = '{clave}';"
            self.cursor.execute(consulta)
            persona = self.cursor.fetchone()
            if self.cursor.rowcount == 1:
                print(f"Nombre completo: {persona[0]}")
                print(f"Teléfono: {persona[1]}")
            else:
                print("Usuario o contraseña incorrectos.")
        except pymysql.Error as e:
            error(e)

    def listar_personas(self):
        try:
            print("\nListando personas...")
            consulta = "select * from persona;"
            self.cursor.execute(consulta)
            personas = self.cursor.fetchall()
            for i, persona in enumerate(personas):
                if i == 0:
                    print("".center(80, "-"))
                print(f"Run: {persona[0]}")
                print(f"Nombre completo: {persona[1]} {persona[2]}")
                print(f"Teléfono: {persona[3]}")
                print("".center(80, "-"))
            print("Fin listado.")
        except pymysql.Error as e:
            error(e)

    def insertar_persona(self, run, nombre, apellido, telefono, clave):
        try:
            print("\nInsertando persona...")
            consulta = f"insert into persona values('{run}', '{nombre}', '{apellido}', '{telefono}', '{clave}');"
            self.cursor.execute(consulta)
            print("Inserción finalizada.")
        except pymysql.Error as e:
            error(e)

    def actualizar_persona(self, run, nombre, apellido, telefono, clave):
        try:
            print("\nActualizando persona...")
            consulta = f"update persona set nombres = '{nombre}', apellidos = '{apellido}', telefono = '{telefono}', clave = '{clave}' where run = '{run}'"
            self.cursor.execute(consulta)
            print(f"Registro actualizado correctamente.")
        except pymysql.Error as e:
            error(e)

    def borrar_persona(self, run):
        try:
            print("\nEliminando persona...")
            consulta = f"select concat(nombres, ' ', apellidos) from persona where run = '{run}'"
            self.cursor.execute(consulta)
            persona = self.cursor.fetchone()
            consulta = f"delete from persona where run = '{run}'"
            self.cursor.execute(consulta)
            if persona is None:
                print("No existe el registro, nada eliminado.")
            else:
                print(f"{persona[0]} eliminado/a.")
        except pymysql.Error as e:
            error(e)
    
    def commit(self):
        try:
            print("\nIniciando commit...")
            self.connection.commit()
            print("Commit finalizado.")
        except pymysql.Error as e:
            error(e)

# Conexión a localhost
bd = ConexionBD("127.0.0.1", "root", "", "db_python")

# Insertar 3 personas
bd.insertar_persona("11.111.111-1", "Gabriel", "Barrientos", "+56966842427", "LKfdu929vn")
bd.insertar_persona("22.222.222-2", "Charlotte", "Rodriguez", "+56922222222", ")8v9skf9ks")
bd.insertar_persona("33.333.333-3", "Nombre", "Apellido", "+56912895829", "Vkjd3@sd")

bd.listar_personas()

# Autentificación correcta
bd.autentificar_persona("11.111.111-1", "LKfdu929vn")

# Autentificación incorrecta
bd.autentificar_persona("22.222.222-2", ")8v9skf9ky")

# Actualizar persona sin nombre, nuevo nombre muy original
bd.actualizar_persona("33.333.333-3", "Nuevo nombre", "Nuevo apellido", "+56912344321", "O9dfjv91")

# Borrar persona
bd.borrar_persona("11.111.111-1")

# Listado final para ver el resultado
bd.listar_personas()

# Commit solo para confirmar los cambios, ejecutar solo cuando se haya verificado que la información es correcta
bd.commit()