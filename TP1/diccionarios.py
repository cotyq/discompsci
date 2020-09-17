def mapeo(palabra):
    """
    Implementar la función mapeo que toma un string y devuelve un diccionario con cada caracter como clave
    y la posición del caracter como valor. Ejemplo, evaluar mapeo a casa devuelve {‘c’: 0, ‘a’:1, ‘s’:2,}
    """
    d = {}
    for i, letra in enumerate(palabra):
        if letra not in d:
            d[letra] = i
    return d


def busqueda_reversa(diccionario, obj):
    """
    Implementar la función busqueda_reversa que dado un diccionario y un objeto cualquiera,
    permita buscar por valores de diccionarios en vez de claves
    """
    return [key for key in diccionario.keys() if diccionario[key] == obj]


if __name__ == "__main__":
    # print(mapeo('casa'))

    d = {'Franco': 'UNL', 'Coty': 'UTN', 'Eugenio': 'UNL'}
    print(busqueda_reversa(d, 'UNL'))