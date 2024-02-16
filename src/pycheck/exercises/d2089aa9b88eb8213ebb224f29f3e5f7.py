TITLE = 'Rellenando valores pendientes'

DESCRIPTION = """
Dada una lista de entrada que contiene números enteros, hay que rellenar aquellos valores que falten. Ojo porque pueden haber números repetidos que se deben respetar.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['numbers', list],
    ],
    'RETURN': [
        ['fnumbers', list],
    ],
}

CHECK_CASES = [
    [[[0, 1, 3, 5]], [[0, 1, 2, 3, 4, 5]]],
    [[[0, 1, 1, 2, 2, 4, 6]], [[0, 1, 1, 2, 2, 3, 4, 5, 6]]],
    [[[0, 1, 1, 1, 5, 6, 6, 8]], [[0, 1, 1, 1, 2, 3, 4, 5, 6, 6, 7, 8]]],
]
