def facturas(cantidad):
    """
    Dado una número de facturas, implementar una función que devuleva el string
    Cantidad de facturas: <nro> donde nro es el número que se pasa como argumento.
    Si las facturas son mas de 12, se tiene que devolver Cantidad de facturas: muchas.
    """
    pass


def ambos(w):
    """
    Dado un string s, implementar la función ambos que devuelve un string
    construido con los dos primeros y dos últimos caracteres. Por ejemplo,
    aplicar ambos a primavera devuelve prra. Si s posee menos de dos caracteres,
    el resultado es el string vacio.
    """
    pass


def fix(uwu):
    """
    Dado un string s, implementar una función fix que reemplaza todas las
    ocurrencias del primer caracter por * a excepción de la primera ocurrencia.
    Por ejemplo evaluar fix a la palabra burbuja devuelve bur*uja.
    Ayuda, estudiar la función replace.
    """
    return uwu[0] + uwu[1:].replace(uwu[0], '*')


def mezclar(a, b):
    """
    Dados dos strings a y b, implementar la función mezclar que devuleve el
    string a y b separados por un espacio, excepto los primeros caracteres
    de cada string que son intercambiados. Por ejemplo, mezclar('mix' , 'pod')
    devuelve pix mod.
    """
    return f'{b[0]}{a[1:]} {a[0]}{b[1:]}'
