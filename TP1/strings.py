def facturas(cantidad):
    """
    Dado una número de facturas, implementar una función que devuleva el string
    Cantidad de facturas: <nro> donde nro es el número que se pasa como argumento.
    Si las facturas son mas de 12, se tiene que devolver Cantidad de facturas: muchas.
    """
    valor = 'muchas' if cantidad > 12 else str(cantidad)
    return 'Cantidad de facturas: ' + valor


def ambos(s):
    """
    Dado un string s, implementar la función ambos que devuelve un string
    construido con los dos primeros y dos últimos caracteres. Por ejemplo,
    aplicar ambos a primavera devuelve prra. Si s posee menos de dos caracteres,
    el resultado es el string vacio.
    """
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]


def fix(s):
    """
    Dado un string s, implementar una función fix que reemplaza todas las
    ocurrencias del primer caracter por * a excepción de la primera ocurrencia.
    Por ejemplo evaluar fix a la palabra burbuja devuelve bur*uja.
    Ayuda, estudiar la función replace.
    """
    return s[0] + s.replace(s[0], '*')[1:]


def mezclar(a, b):
    """
    Dados dos strings a y b, implementar la función mezclar que devuleve el
    string a y b separados por un espacio, excepto los primeros caracteres
    de cada string que son intercambiados. Por ejemplo, mezclar('mix' , 'pod')
    devuelve pix mod.
    """
    return b[0] + a[1:] + ' ' + a[0] + b[1:]


if __name__ == "__main__":
    # print(facturas(15))
    # print(facturas(11))

    # print(ambos('c'))
    # print(ambos('ca'))
    # print(ambos('cas'))
    # print(ambos('casa'))
    # print(ambos('casamiento'))

    # print(fix('burbuja'))

    print(mezclar('mix', 'pod'))