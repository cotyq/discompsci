def matcheos(lista):
    """
    Implementar la función macheos que dada una lista de strings devuelve un número representando
    la cantidad de strings que tienen mas de dos caracteres y cuyos últimos dos strings son iguales.
    """
    return len([palabra for palabra in lista if len(palabra) > 2 and palabra[-1] == palabra[-2]])


def front_x(lista):
    """
    Dada una lista de strings, implementar la funcion front_x que devuelve una lista ordenada exceptuando las palabras
    que comiencen con x, las cuales deben ir al principio.
    Por ejemplo, ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] devuelve ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    con_x = [word for word in lista if word[0] == 'x']
    sin_x = [word for word in lista if word[0] != 'x']

    return sorted(con_x) + sorted(sin_x)


def sort_last(lista):
    """
    Dada una lista de tuplas no vacias, implementar la funcion sort_last que devuelve una lista
    con las tuplas ordenadas de forma incremental en el último elemento de la tupla.
    Ejemplo: aplicar sort_last a [(1, 7), (1, 3), (3, 4, 5), (2, 2)] devuelve [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    return sorted(lista, key=lambda x: x[-1])


def tablas(numero):
    """
    Implementar la función tablas que dado un argumento nro, devuelve la tabla de multiplicar de nro del 1 al 10.
    """
    return [i * numero for i in range(1, 11)]
