TITLE = 'Mínimo de 3 valores'

DESCRIPTION = """
Dados 3 números calcule el mínimo.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['value1', int],
        ['value2', int],
        ['value3', int],
    ],
    'RETURN': [
        ['min_value', int],
    ],
}

CHECK_CASES = [
    [[7, 4, 9], [4]],
    [[2, 5, 1], [1]],
    [[9, 3, 7], [3]],
    [[9, 9, 9], [9]],
]
