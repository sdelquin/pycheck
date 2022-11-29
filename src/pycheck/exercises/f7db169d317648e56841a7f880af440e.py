TITLE = 'Partición por el número'

DESCRIPTION = '''
Dada una lista de entrada de valores numéricos y dado un número de referencia, obtenga una lista de dos listas, donde la primera lista contenga todos los números de la lista de entrada menores que el número de referencia y donde la segunda lista contenga todos los números de la lista de salida mayores o iguales que el número de referencia.

Mantenga el mismo orden en el que vienen los números de la lista de entrada.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['values', list],
        ['ref_value', int],
    ],
    'RETURN': [
        ['npartition', list],
    ],
}

CHECK_CASES = [
    [[[4, 3, 2, 9, 8, 5], 4], [[[3, 2], [4, 9, 8, 5]]]],
    [[[5, 3, 8, 7, 11, 19, 12, 15], 10], [[[5, 3, 8, 7], [11, 19, 12, 15]]]],
    [[[1, 2, 3], 10], [[[1, 2, 3], []]]],
    [[[1, 2, 3], -10], [[[], [1, 2, 3]]]],
]
