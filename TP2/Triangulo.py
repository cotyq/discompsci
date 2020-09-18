"""
3. Triángulo
Escriba una clase, Triángulo, que represente un triángulo.

La clase debe incluir los siguientes métodos que devuelven un valor lógico indicando el tipo del triángulo:
es_rectangulo (devuelve True para triángulos rectángulos) es_escaleno (devuelve True todos los lados distintos)
es_isosceles (devuelve True dos lados iguales y el otro distinto) es_equilatero (devuelve True los tres lados iguales)

"""


class Triangulo:
    def __init__(self, a, b, c):
        self.lados = [a, b, c]
        self.lados.sort()
        self.__verificar_triangulo__()

    def es_rectangulo(self):
        return self.lados[2] ** 2 == self.lados[0] ** 2 + self.lados[1] ** 2

    def es_escaleno(self):
        return self.lados[2] != self.lados[0] != self.lados[1]

    def es_isoceles(self):
        return self.lados[0] == self.lados[1] or self.lados[1] == self.lados[2]

    def es_equilatero(self):
        return self.lados[0] == self.lados[1] == self.lados[2]

    def __verificar_triangulo__(self):
        if self.lados[2] > sum(self.lados[:2]):
            raise ValueError("No es un triangulo")


if __name__ == "__main__":
    tri1 = Triangulo(3, 4, 5)
    print(tri1.es_equilatero())
    print(tri1.es_escaleno())
    print(tri1.es_isoceles())
    print(tri1.es_rectangulo())
