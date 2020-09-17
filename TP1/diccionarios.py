def mapeo(palabra):
    """
    Implementar la función mapeo que toma un string y devuelve un diccionario con cada caracter como clave
    y la posición del caracter como valor. Ejemplo, evaluar mapeo a casa devuelve {‘c’: 0, ‘a’:1, ‘s’:2,}
    """
    map = {}
    for i in range(len(palabra)-1, -1, -1):
        map[palabra[i]] = i
    return map


def busqueda_reversa(diccionario, objeto):
    """
    Implementar la función busqueda_reversa que dado un diccionario y un objeto cualquiera,
    permita buscar por valores de diccionarios en vez de claves
    """
    for i in diccionario:
        if diccionario[i] == objeto:
            return i
