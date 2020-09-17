def matcheos(lista):
    """
    Implementar la función macheos que dada una lista de strings devuelve un número representando
    la cantidad de strings que tienen mas de dos caracteres y cuyos últimos dos strings son iguales.
    """
    c = 0
    for palabra in lista:
        c += 1 if len(palabra) > 2 and palabra[-2] == palabra[-1] else 0
    return c



def front_x(lista):
    """
    Dada una lista de strings, implementar la funcion front_x que devuelve una lista ordenada exceptuando las palabras
    que comiencen con x, las cuales deben ir al principio.
    Por ejemplo, ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] devuelve ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    lista_x, lista_abc = [], []
    for palabra in lista:
        if palabra[0] == 'x':
            lista_x.append(palabra)
        else:
            lista_abc.append(palabra)
    lista_x.sort()
    lista_abc.sort()
    return lista_x + lista_abc


def sort_last(lista):
    """
    Dada una lista de tuplas no vacias, implementar la funcion sort_last que devuelve una lista
    con las tuplas ordenadas de forma incremental en el último elemento de la tupla.
    Ejemplo: aplicar sort_last a [(1, 7), (1, 3), (3, 4, 5), (2, 2)] devuelve [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    lista.sort(key=lambda l: l[-1])
    return lista

def tablas(numero):
    """
    Implementar la función tablas que dado un argumento nro, devuelve la tabla de multiplicar de nro del 1 al 10.
    """
    return [numero * i for i in range(1, 11)]


if __name__ == "__main__":
    # print(matcheos(['casa', 'laaa', 'auto', 'leeee']))

    # print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))

    # print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))

    print(tablas(3))