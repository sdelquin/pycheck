TITLE = 'Valor máximo'

DESCRIPTION = '''
Dada una lista de valores numéricos enteros, obtenga su máximo valor.

Prohibido utilizar:
- La función "built-in" max().
- La función "built-in" sorted().
'''

ENTRYPOINT = {
    'PARAMS': [
        ['values', list],
    ],
    'RETURN': [
        ['max_value', int],
    ],
}

CHECK_CASES = [
    [[[-11, 10, -6, 15, -1]], [15]],
    [[[5, 9, -6, 9, -2, -9, -7, 2]], [9]],
    [[[-7, -5, -5, -8, -3]], [-3]],
]
