"""
2. Herencia
Establezca una jerarquía de clases que represente a los estudiantes de una universidad sabiendo que todos los
estudiantes se caracterizan por un nombre y un número. Hay varios tipos de estudiantes: los estudiantes ocasionales,
sean de cursos de verano o de cursos específicos (se matriculan de un curso determinado), los que cursan solo una
tecnicatura, licenciatura.

Además, la universidad imparte cursos de especialización gratuitos para sus empleados.

"""


class Estudiante:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero


class EstudianteOcasional(Estudiante):
    def __init__(self, nombre, numero, curso):
        super().__init__(nombre, numero)
        self.curso = curso


class EstudianteEmpleado(Estudiante):
    def __init__(self, nombre, numero, curso):
        super().__init__(nombre, numero)
        self.curso = curso


class EstudianteDeGrado(Estudiante):
    def __init__(self, nombre, numero, carrera):
        super().__init__(nombre, numero)
        self.carrera = carrera
