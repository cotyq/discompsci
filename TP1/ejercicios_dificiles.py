import math


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
