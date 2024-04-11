TITLE = 'Calculando el máximo con recursividad'

DESCRIPTION = """
Dada una lista de elementos calcule el máximo de todos ellos utilizando una función recursiva.

Notas:
- No se puede utilizar la función "built-in" _max()_.
"""

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'rmax',
    'PARAMS': [
        ['items', list],
    ],
    'RETURN': [
        ['max_item', int],
    ],
}

CHECK_CASES = [
    [[[5, 3, 9, 2, 7]], [9]],
    [[[21, 34, 15, 11, 45, 32]], [45]],
    [[[102, 299, 476, 322, 632, 286, 117]], [632]],
]
