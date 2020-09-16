import numpy as np

def matcheos(l):
    """
    Implementar la función macheos que dada una lista de strings devuelve un número representando
    la cantidad de strings que tienen mas de dos caracteres y cuyos últimos dos strings son iguales.
    """
    if isinstance(l,list):
        c = 0
        for i in l:
            if isinstance(i,str):
                print("Dame una lista de strings!")
            elif len(i) > 2:
                if i[-1] ==i[-2]:
                    c += 1
        return c
    else:
        print("Dame una lista!")


def front_x(l):
    """
    Dada una lista de strings, implementar la funcion front_x que devuelve una lista ordenada exceptuando las palabras
    que comiencen con x, las cuales deben ir al principio.
    Por ejemplo, ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] devuelve ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    x = []
    
    for i in l:
        if isinstance(i,str):
                print("Dame una lista de strings!")
        elif i[0] == "x":
            x.append(i)
            l.pop(l.index(i))
    x.sort()
    l.sort()
    x += l
    return x


def sort_last(l):
    """
    Dada una lista de tuplas no vacias, implementar la funcion sort_last que devuelve una lista
    con las tuplas ordenadas de forma incremental en el último elemento de la tupla.
    Ejemplo: aplicar sort_last a [(1, 7), (1, 3), (3, 4, 5), (2, 2)] devuelve [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    if isinstance(l,list):
        return l.sort(key = lambda l: l[-1]) 
    else:
        print("Dame una lista!")


def tablas(nro):
    """
    Implementar la función tablas que dado un argumento nro, devuelve la tabla de multiplicar de nro del 1 al 10.
    """
    return np.arange(1,11,1)*nro
