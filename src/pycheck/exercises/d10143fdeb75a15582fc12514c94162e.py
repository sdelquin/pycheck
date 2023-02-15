TITLE = 'Extracción de pares'

DESCRIPTION = '''
Escriba una función en Python que reciba una lista de valores enteros y devuelva otra lista sólo con aquellos valores pares.
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'PARAMS': [
        ['values', list],
    ],
    'RETURN': [
        ['evens', list],
    ],
}

CHECK_CASES = [
    [[[1, 2, 3, 4, 5, 6, 7, 8, 9]], [[2, 4, 6, 8]]],
    [[[8, 6, 1, 2, 3, 4]], [[8, 6, 2, 4]]],
    [[[]], [[]]],
    [[[1, 3, 5]], [[]]],
    [[[2, 2, 2]], [[2, 2, 2]]],
]
