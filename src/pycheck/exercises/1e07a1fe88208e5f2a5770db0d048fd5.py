TITLE = 'Suma de la diagonal principal'

DESCRIPTION = '''
Escriba un programa en Python que acepte una lista de listas representando una matriz numérica de valores enteros y compute la suma de los elementos de la diagonal principal.

Lo puede afrontar en _versión clásica_ o con _listas por comprensión_. ¡O incluso ambas!
'''

ENTRYPOINT = {
    'PARAMS': [
        ['matrix', list],
    ],
    'RETURN': [
        ['sum_diagonal', int],
    ],
}

CHECK_CASES = [
    [[[[4, 6, 1], [2, 9, 3], [1, 7, 7]]], [20]],
    [[[[1, 1], [1, 1]]], [2]],
    [[[[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]]], [16]],
]
