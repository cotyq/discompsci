import math


def invitados(d):
    """
    Imaginen que poseemos un diccionario de la forma nombre -> estado 
    (clave -> valor), el estado representa si la persona cuyo nombre es nombre 
    irá o no a tu cumpleaños
    """
    a = []
    for i in d:
        if d[i] == "Asistirá":
            a.append(i)
    return a


def justificar(s):
    """
    Dado un string implementar la función justificar que fija la longitud de 
    cada línea en 80 caracteres y justifica cada línea.
    """
    palabras = s.split()
    final = []
    linea = []
    c = 0
    for palabra in palabras:
        if c + len(palabra) < 80 - len(linea):
            linea.append(palabra)
            c += len(palabra)
        else:
            espacios_extra = 80 - len(linea) - c
            if espacios_extra > 0:
                k = math.ceil((len(linea) / espacios_extra))
                for i in range(0, len(linea), k):
                    linea[i] += " "
            final.append(" ".join(linea))
            linea = [palabra]
            c = len(palabra)
    final.append(" ".join(linea))
    return "\n".join(final)


if __name__ == "__main__":
    invit = {
        "María": "Asistirá",
        "Luis": "Asistirá",
        "Ángel": "No asistirá",
        "Pedro": "Asistirá",
        "Carla": "No asistirá",
    }
    print(invitados(invit))

    texto = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur in tristique quam. Proin tortor "
        "turpis, tempus nec nisl luctus, pharetra malesuada purus. Donec eu dui ullamcorper, sagittis massa et, "
        "efficitur arcu. Nunc ut mattis sapien, non suscipit lacus. Mauris rutrum pellentesque nulla. Duis "
        "tincidunt feugiat nisi ut interdum. Morbi a sem odio. Nulla suscipit est eu erat elementum, in "
        "accumsan magna aliquet. Maecenas sollicitudin tellus vel justo molestie, sed cursus felis auctor. "
        "Curabitur porta purus egestas, tincidunt libero ut, ornare justo. Duis sit amet nisl efficitur, "
        "luctus sem a, volutpat diam."
    )

    print(justificar(texto))
