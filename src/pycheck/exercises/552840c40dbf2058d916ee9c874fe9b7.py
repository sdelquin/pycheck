TITLE = 'Ordenando números'

DESCRIPTION = """
Ordene la lista de números dada de manera ascendente **sin utilizar la función sorted()**.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['numbers', list],
    ],
    'RETURN': [
        ['sorted_numbers', list],
    ],
}

CHECK_CASES = [
    [[[4, 2, 9, 7, 1, 8]], [[1, 2, 4, 7, 8, 9]]],
    [[[21, 11, 5, 34, 42, 7, 16, 3, 51, 18]], [[3, 5, 7, 11, 16, 18, 21, 34, 42, 51]]],
    [[[3, 2, 2, 5, 7, 1, 7, 9, 2, 9, 9, 4]], [[1, 2, 2, 2, 3, 4, 5, 7, 7, 9, 9, 9]]],
    [[[0]], [[0]]],
    [[[1, 0]], [[0, 1]]],
]
