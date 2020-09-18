"""
6. Introspección
Implementar la función evaluar que tome un objeto y un string como parámetros y si el string es un atributo, que
devuelva el valor del atributo.

Si es un método, devolver el resultado de aplicar el método al objeto (usar parámetros opcionales en evaluar para
parámetros de métodos con parámetros) y si no es un método, ni un atributo, lanzar una Exception del tipo
UnkonowTypeError que es-un TypeError el cual recibe comp parámetro el nombre del atributo desconocido.
"""


class UnkonowTypeError(TypeError):
    def __init__(self, palabra):
        super().__init__(palabra)


def introspeccion(objeto, fun_or_attr, *args, **kwargs):
    try:
        if hasattr(objeto, fun_or_attr) and not callable(getattr(objeto, fun_or_attr)):
            return getattr(objeto, fun_or_attr)
        if callable(getattr(objeto, fun_or_attr)):
            return getattr(objeto, fun_or_attr)(*args, **kwargs)
    except AttributeError:
        raise UnkonowTypeError(fun_or_attr)


class Fruta:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def mensaje(self, texto='El contenido es: '):
        print(texto + self.nombre)


if __name__ == "__main__":
    manzana = Fruta('manzana', 'roja')
    introspeccion(manzana, 'nombre')
    introspeccion(manzana, 'mensaje')
    introspeccion(manzana, 'mensaje', 'El mensaje modificado es: ')
    introspeccion(manzana, 'mensaje2')
