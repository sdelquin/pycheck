TITLE = 'Valor máximo'

DESCRIPTION = """
Dada una lista de valores numéricos enteros, obtenga su mínimo valor.

Implementa la solución usando la función "built-in" _max()_.

Prohibido utilizar:
- La función "built-in" _min()_.
- La función "built-in" _sorted()_.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['values', list],
    ],
    'RETURN': [
        ['min_value', int],
    ],
}

CHECK_CASES = [
    [[[-11, 10, -6, 15, -1]], [-11]],
    [[[5, 9, -6, 9, -2, -9, -7, 2]], [-9]],
    [[[-7, -5, -5, -8, -3]], [-8]],
]
