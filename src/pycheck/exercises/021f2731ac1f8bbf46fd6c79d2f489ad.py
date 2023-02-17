TITLE = 'Ordenando con burbujas'

DESCRIPTION = '''
Ordene una lista de entrada utilizando el [algoritmo de la burbuja](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif).

Notas:
- No modifique la lista de entrada, devuelva una lista nueva.
- No utilice las funciones predefinidas _sort()_ ni _sorted()_.
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'bubble',
    'PARAMS': [
        ['items', list],
    ],
    'RETURN': [
        ['sorted_items', list],
    ],
}

CHECK_CASES = [
    [[[]], [[]]],
    [[[1]], [[1]]],
    [[[2, 1]], [[1, 2]]],
    [[[3, 3, 3, 2, 2, 1]], [[1, 2, 2, 3, 3, 3]]],
    [[[9, 8, 7, 6, 5, 4, 3, 2, 1]], [[1, 2, 3, 4, 5, 6, 7, 8, 9]]],
]
