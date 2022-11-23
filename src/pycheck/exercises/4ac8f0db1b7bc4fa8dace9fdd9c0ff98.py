DESCRIPTION = '''
Genere una lista on los "n" primeros múltiplos de "x", donde "n" y "x" son parámetros de
entrada representando valores enteros mayores que 0.

Resuelva el ejercicio utilizando listas por comprensión.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['x', int],
        ['n', int],
    ],
    'RETURN': [
        ['multiples', list],
    ],
}

CHECK_CASES = [
    [[1, 10], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]],
    [[2, 5], [[2, 4, 6, 8, 10]]],
    [[3, 8], [[3, 6, 9, 12, 15, 18, 21, 24]]],
]

SOURCE = 'https://www.codewars.com/kata/5513795bd3fafb56c200049e'
