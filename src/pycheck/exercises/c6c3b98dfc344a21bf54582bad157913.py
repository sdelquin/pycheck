TITLE = 'Multiplicando matrices'

DESCRIPTION = """
Escriba un programa que permita [multiplicar matrices](https://ekuatio.com/como-multiplicar-matrices/) de cualquier dimensión.

Caso especial: Si el número de columnas de la primera matriz no coincide con el número de filas de la segunda matriz hay que devolver _None_.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['A', list],
        ['B', list],
    ],
    'RETURN': [
        ['P', list],
    ],
}

CHECK_CASES = [
    [[[[1, 2, 3], [4, 5, 6]], [[5, -1], [1, 0], [-2, 3]]], [[[1, 8], [13, 14]]]],
    [[[[1, 2, 3], [1, 1, 1], [0, 1, -1]], [[1], [2], [1]]], [[[8], [4], [1]]]],
    [[[[9, 7], [3, 2]], [[8, 4], [7, 3]]], [[[121, 57], [38, 18]]]],
    [
        [[[9, 1, 8, 4], [3, 8, 2, 8], [5, 5, 2, 6]], [[2, 3], [4, 1], [6, 4], [3, 7]]],
        [[[82, 88], [74, 81], [60, 70]]],
    ],
    [[[[1, 4, 5], [3, 2, 1]], [[4, 3, 2], [5, 6, 8]]], [None]],
]
