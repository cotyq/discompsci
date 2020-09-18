"""
4. Personas
Construya una estructura de clases que represente una serie de personas caracterizadas por el nombre (compuesto de
nombre de pila y dos apellidos) y el número del DNI. Debe ser posible imprimir los datos completos de una persona y
devolver el nombre o el DNI independientemente.

"""


class Persona:
    def __init__(self, nombre, apellido1, apellido2, dni):
        self.__nombre = nombre
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__dni = dni

        self.padre = None
        self.madre = None

    @property
    def nombre_completo(self):
        return self.__nombre + ' ' + self.__apellido1 + ' ' + self.__apellido2

    @property
    def dni(self):
        return self.__dni

    def __str__(self):
        return f'Nombre completo: {self.nombre_completo}.\n' \
               f'DNI: {self.dni}\n' \
               f'{"" if self.padre is None else "Padre: " + self.padre.nombre_completo}\n' \
               f'{"" if self.madre is None else "Madre: " + self.madre.nombre_completo}'

    def asignar_padres(self, padre, madre):
        self.padre = padre
        self.madre = madre


"""
5. Vínculos
Modifique el ejemplo anterior para poder construir un árbol genealógico donde se establezca dinámicamente un vínculo que
 indique qué persona es el padre y cual la madre de una persona dada.

"""

if __name__ == "__main__":
    franco = Persona('Franco', 'Lopez', 'Alaniz', 756765)
    papa = Persona('Mos', 'f3', 'qwee', 34634)
    mama = Persona('Mara', 'asdas', 'Conasdasta', 2356)
    franco.asignar_padres(papa, mama)

    print(franco)
