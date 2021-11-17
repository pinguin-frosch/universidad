import pymysql
from sys import exit

class ConexionBD:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host="localhost",
                user="root",
                passwd="",
                db="db_python"
            )
            self.cursor = self.connection.cursor()
            print("Conexión exitosa.")
        except pymysql.Error as e:
            print(f"Error {e.args[0]}: {e.args[1]}")
            exit(1)

    def autentificar_usuarios(self, run, clave):
        try:
            consulta = f"select concat(nombres, ' ', apellidos) as 'Nombre completo', telefono from persona where run = '{run}' and clave = '{clave}';"
            self.cursor.execute(consulta)
            persona = self.cursor.fetchone()
            if self.cursor.rowcount == 1:
                print(f"Nombre completo: {persona[0]}")
                print(f"Teléfono: {persona[1]}")
            else:
                print("Usuario o contraseña incorrectos.")
        except pymysql.Error as e:
            print(f"Error {e.args[0]}: {e.args[1]}")

    def listar_usuarios(self):
        try:
            consulta = "select * from persona;"
            self.cursor.execute(consulta)
            personas = self.cursor.fetchall()
            for i, persona in enumerate(personas):
                if i == 0:
                    print("\n", "".center(80, "-"), sep="")
                print(f"Run: {persona[0]}")
                print(f"Nombre completo: {persona[1]} {persona[2]}")
                print(f"Teléfono: {persona[3]}")
                print("".center(80, "-"))
        except pymysql.Error as e:
            print(f"Error {e.args[0]}: {e.args[1]}")

    def insertar_persona(self, rut, nombre, apellido, telefono, clave):
        try:
            consulta = f"insert into persona values('{rut}', '{nombre}', '{apellido}', '{telefono}', '{clave}');"
            self.cursor.execute(consulta)
            self.listar_usuarios()
        except pymysql.Error as e:
            print(f"Error {e.args[0]}: {e.args[1]}")

bd = ConexionBD()
# bd.autentificar_usuarios("11.111.111-1", "Xder87k")
# bd.listar_usuarios()
# bd.insertar_persona("55.555.555-5", "abraham", "lincoln", "+56955555555", "asdflvor3")