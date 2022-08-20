# Crear clases, herencia y composición de alguna forma
# Hecho por Gabriel Barrientos

import datetime
from typing import Any

class Persona:
    nombre: str
    fecha_nacimiento: datetime.date

    def __init__(self, nombre: str, fecha_nacimiento: datetime.date) -> None:
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def get_nombre(self) -> str:
        return self.nombre

    def get_fecha_nacimiento(self) -> str:
        return self.fecha_nacimiento.strftime("%d-%m-%Y")

    def set_nombre(self, nombre: str) -> None:
        self.nombre = nombre

    def set_fecha_nacimiento(self, fecha_nacimiento: datetime.date) -> None:
        self.fecha_nacimiento = fecha_nacimiento

class Estudiante(Persona):
    notas: list[float] = []

    def __init__(self, nombre: str, fecha_nacimiento: datetime.date) -> None:
        super().__init__(nombre, fecha_nacimiento)    

    def get_notas(self) -> list[float]:
        return self.notas

    def set_notas(self, notas: list[float]) -> None:
        self.notas = notas

    def colocar_nota(self, nota: float) -> None:
        self.notas.append(nota)

    def borrar_nota(self, posicion: int) -> Any:
        try:
            self.notas.pop(posicion - 1)
        except IndexError:
            print(f"No existe la nota número {posicion}, omitiendo eliminación")

    def eliminar_notas(self) -> None:
        self.notas.clear()

    def promedio(self) -> Any:
        try:
            return round(sum(self.notas) / len(self.notas), 2)
        except ZeroDivisionError:
            return "No se puede calcular el promedio sin notas"

fecha = datetime.date(2003, 1, 14)
gabriel = Estudiante("Gabriel Barrientos", fecha)

print(f"Nombre:     {gabriel.get_nombre()}")
print(f"Nacimiento: {gabriel.get_fecha_nacimiento()}")

print("".center(60, "-"))

gabriel.colocar_nota(4.7)
gabriel.colocar_nota(5.9)
gabriel.colocar_nota(6.9)
gabriel.colocar_nota(4.7)

print(f"Notas:      {gabriel.get_notas()}")
print(f"Promedio:   {gabriel.promedio()}")

print("".center(60, "-"))

gabriel.borrar_nota(5)

print(f"Notas:      {gabriel.get_notas()}")
print(f"Promedio:   {gabriel.promedio()}")

print("".center(60, "-"))

gabriel.eliminar_notas()

print(f"Notas:      {gabriel.get_notas()}")
print(f"Promedio:   {gabriel.promedio()}")

print("".center(60, "-"))

gabriel.set_notas([6.9, 6.8, 6.9])

print(f"Notas:      {gabriel.get_notas()}")
print(f"Promedio:   {gabriel.promedio()}")