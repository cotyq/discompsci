def mapeo(s):
    """
    Implementar la función mapeo que toma un string y devuelve un diccionario con cada caracter como clave
    y la posición del caracter como valor. Ejemplo, evaluar mapeo a casa devuelve {‘c’: 0, ‘a’:1, ‘s’:2,}
    """
    if isinstance(s,str):
        d = {}
        for i in range(len(s)-1,-1,-1):
            d[s[i]] = i
        return d
    else:
        print("Dame un string!") 


def busqueda_reversa(d, v):
    """
    Implementar la función busqueda_reversa que dado un diccionario y un objeto cualquiera,
    permita buscar por valores de diccionarios en vez de claves
    """
    return list(d.keys())[list(d.values()).index(v)]
