from typing import Any

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

class Calculadora:
    n1: float
    n2: float
            
    def __init__(self, n1: float) -> None:
        self.n1 = n1

    def get_n1(self) -> float:
        return self.n1

    def set_n1(self, n1: float) -> None:
        self.n1 = n1

    def get_n2(self) -> float:
        return self.n2

    def set_n2(self, n2: float) -> None:
        self.n2 = n2

    def sumar(self) -> float:
        return self.n1 + self.n2

    def restar(self) -> float:
        return self.n1 - self.n2

    def multiplicar(self) -> float:
        return self.n1 * self.n2

    def dividir(self) -> Any:
        if self.n2 != 0:
            return self.n1 / self.n2
        else:
            return "No se puede dividir por 0"

while True:
    n1 = input("Ingrese el primer número:  ")
    if isfloat(n1):
        n1 = float(n1)
        break

while True:
    n2 = input("Ingrese el segundo número: ")
    if isfloat(n2):
        n2 = float(n2)
        break

calculadora = Calculadora(n1)

calculadora.set_n2(n2)

print(f"\n{calculadora.n1} + {calculadora.n2} = {calculadora.sumar()}")
print(f"{calculadora.n1} - {calculadora.n2} = {calculadora.restar()}")
print(f"{calculadora.n1} * {calculadora.n2} = {calculadora.multiplicar()}")
print(f"{calculadora.n1} / {calculadora.n2} = {calculadora.dividir()}\n")