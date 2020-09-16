def facturas(nro):
    """
    Dado una número de facturas, implementar una función que devuleva el string
    Cantidad de facturas: <nro> donde nro es el número que se pasa como argumento.
    Si las facturas son mas de 12, se tiene que devolver Cantidad de facturas: muchas.
    """
    if isinstance(nro,int) or isinstance(nro,float):
        if nro < 13:
            return f"Cantidad de facturas: {nro}"
        else:
            return "Cantidad de facturas: muchas"
    else:
        print("Dame un numero!")


def ambos(s):
    """
    Dado un string s, implementar la función ambos que devuelve un string
    construido con los dos primeros y dos últimos caracteres. Por ejemplo,
    aplicar ambos a primavera devuelve prra. Si s posee menos de dos caracteres,
    el resultado es el string vacio.
    """
    if isinstance(s,str):
        if len(s) > 2:
            return s[0]+s[1]+s[-2]+s[-1]
        else:
            return ""
    else:
        print("Dame un string!")


def fix(s):
    """
    Dado un string s, implementar una función fix que reemplaza todas las
    ocurrencias del primer caracter por * a excepción de la primera ocurrencia.
    Por ejemplo evaluar fix a la palabra burbuja devuelve bur*uja.
    Ayuda, estudiar la función replace.
    """
    if isinstance(s,str):
        return s[0]+s[1:].replace(s[0],"*")
    else:
        print("Dame un string!")


def mezclar(a, b):
    """
    Dados dos strings a y b, implementar la función mezclar que devuleve el
    string a y b separados por un espacio, excepto los primeros caracteres
    de cada string que son intercambiados. Por ejemplo, mezclar('mix' , 'pod')
    devuelve pix mod.
    """
    if isinstance(a,str) and isinstance(b,str):
        return b[0] + a[1:] + " " + a[0] + b[1:]
    else:
        print("Dame dos strings!")
