TITLE = 'Somos iguales, pero distintos'

DESCRIPTION = '''
Dada una lista de entrada, devuelva _True_ si todos sus elementos son iguales o _False_ en otro caso.
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
