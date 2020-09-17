import re
import textwrap


def invitados(dicc):
    """
    Imaginen que poseemos un diccionario de la forma nombre -> estado (clave -> valor),
    el estado representa si la persona cuyo nombre es nombre irá o no a tu cumpleaños
    , por ejemplo:

    invitados = {"María": "Asistirá", "Luis": "Asistirá", "Ángel": "No asistirá",
    "Pedro": "Asistirá", "Carla": "No asistirá"}

    Implementar la función invitados que devuelve solo aquellas personas que asistirán al cumpleaños.
    """
    return [nombre for nombre in dicc.keys() if dicc[nombre] == 'Asistirá']


def justificar(palabra):
    """
    Dado un string implementar la función justificar que fija la longitud de cada línea en 80 caracteres
     y justifica cada línea.
     """
    return textwrap.fill(palabra, width=80)


if __name__ == "__main__":
    # invit = {"María": "Asistirá", "Luis": "Asistirá", "Ángel": "No asistirá", "Pedro": "Asistirá",
    #          "Carla": "No asistirá"}
    # print(invitados(invit))

    texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur in tristique quam. Proin tortor " \
            "turpis, tempus nec nisl luctus, pharetra malesuada purus. Donec eu dui ullamcorper, sagittis massa et, " \
            "efficitur arcu. Nunc ut mattis sapien, non suscipit lacus. Mauris rutrum pellentesque nulla. Duis " \
            "tincidunt feugiat nisi ut interdum. Morbi a sem odio. Nulla suscipit est eu erat elementum, in " \
            "accumsan magna aliquet. Maecenas sollicitudin tellus vel justo molestie, sed cursus felis auctor. " \
            "Curabitur porta purus egestas, tincidunt libero ut, ornare justo. Duis sit amet nisl efficitur, " \
            "luctus sem a, volutpat diam."

    print(justificar(texto))
