TITLE = 'Elementos duplicados consecutivos'

DESCRIPTION = '''
Dada una lista, genere otra lista eliminando los elementos duplicados consecutivos.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['items', list],
    ],
    'RETURN': [
        ['result', list],
    ],
}

CHECK_CASES = [
    [
        [[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]],
        [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]],
    ],
    [[['a', 'b', 'b', 'b', 'c', 'b']], [['a', 'b', 'c', 'b']]],
    [[[1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0]], [[1, 0, 1, 0, 1, 0]]],
]
