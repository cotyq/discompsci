"""
Un cerrojo con combinación tiene las siguientes propiedades básicas: la combinación (una secuencia de tres números); el
cerrojo se puede abrir proporcionando la combinación; y la combinación se puede cambiar, pero solamente por alguien que
conoce la combinación actual.

Diseñe una clase con métodos abrir, cerrar y cambiar_combinacion, y atributos para almacenar la combinación y el estado
de la puerta, cerrada o abierta.

La combinación debería asignarse en el constructor.
"""


class Puerta():
    def __init__(self, combinacion):
        self.__validar_combinacion__(combinacion)
        self.combinacion = combinacion
        self.abierta = False

    def abrir(self, comb):
        if self.combinacion == comb:
            print('Abriendo la puerta...')
            self.abierta = True
        else:
            print('Clave incorrecta.')
        return self.abierta

    def cerrar(self):
        print('Cerrando la puerta...')
        self.abierta = False
        return self.abierta

    def cambiar_combinacion(self, comb_vieja, comb_nueva):
        if self.combinacion == comb_vieja:
            self.combinacion = comb_nueva
            print('Combinacion cambiada exitosamente.')
        else:
            print('La combinacion vieja es incorrecta.')


    def __validar_combinacion__(self, combinacion):
        if len(combinacion) != 3:
            raise ValueError("La longitud de la combinación es incorrecta")
        if not ('000' <= combinacion <= '999'):
            raise ValueError("Debe ser un numero.")


if __name__ == "__main__":
    try:
        puerta_de_casa = Puerta('1234')
    except ValueError as e:
        print(e)
    puerta_de_casa = Puerta('123')
    puerta_de_casa.abrir('543')
    puerta_de_casa.abrir('123')
    puerta_de_casa.cerrar()
    puerta_de_casa.cambiar_combinacion('885', '455')
    puerta_de_casa.cambiar_combinacion('123', '455')
