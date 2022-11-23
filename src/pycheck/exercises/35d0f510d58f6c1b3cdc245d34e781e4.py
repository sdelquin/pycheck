DESCRIPTION = '''
Dada una lista de entrada, devuelva True si todos sus elementos son iguales o
False en otro caso.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['items', list],
    ],
    'RETURN': [
        ['all_same', bool],
    ],
}

CHECK_CASES = [
    [[[1, 1, 1, 1, 1, 1]], [True]],
    [[[1, 1, 1, 1, 2]], [False]],
    [[['a', 'b', 'c']], [False]],
]
