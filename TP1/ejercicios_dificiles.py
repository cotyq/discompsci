def invitados(diccionario):
    """
    Imaginen que poseemos un diccionario de la forma nombre -> estado (clave -> valor),
    el estado representa si la persona cuyo nombre es nombre irá o no a tu cumpleaños.
    Implementar la función invitados que devuelve solo aquellas personas que asistirán al cumpleaños.
    """
    return [i for i in diccionario if diccionario[i] == "Asistirá"]


def justificar(palabra):
    """
    Dado un string implementar la función justificar que fija la longitud de cada línea en 80 caracteres
     y justifica cada línea.
     """
    lines = []
    start = 0
    width = 80
    while start + width < len(palabra):
        last_space = palabra[start:start + width].rfind(' ')
        end = start + last_space if last_space != -1 else start + width
        lines.append(palabra[start:end])
        start = end + 1 if last_space != -1 else end
    lines.append(palabra[start:])
    return '\n'.join(lines)


def main():
    loren = """Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32"""
    print(justificar(loren))

    raro = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
    print(justificar(raro))


if __name__ == "__main__":
    main()
