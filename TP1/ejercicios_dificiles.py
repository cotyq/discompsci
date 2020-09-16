import textwrap


def invitados(d):
    """
    Imaginen que poseemos un diccionario de la forma nombre -> estado (clave -> valor),
    el estado representa si la persona cuyo nombre es nombre irá o no a tu cumpleaños
    """
    a = []
    for i in d:
        if d[i] == "Asistirá":
            a.append(i)
    return a


def justificar(s):
    """
    Dado un string implementar la función justificar que fija la longitud de cada línea en 80 caracteres
     y justifica cada línea.
     """
    print(textwrap.fill(s, width=80))
