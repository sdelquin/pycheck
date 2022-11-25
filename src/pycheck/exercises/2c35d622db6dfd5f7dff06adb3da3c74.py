TITLE = 'No eres consecutivo'

DESCRIPTION = '''
El objetivo es encontrar el primer número no consecutivo dentro de una lista de valores numéricos enteros. Si todos los valores son consecutivos entonces el resultado es None.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['values', list],
    ],
    'RETURN': [
        ['target', int],
    ],
}

CHECK_CASES = [
    [[[1, 2, 3, 4, 6, 7, 8]], [6]],
    [[[101, 102, 103]], [None]],
    [[[-5, -4, -3, 0, 3, 4, 5]], [0]],
    [[[1]], [None]],
    [[[]], [None]],
]

SOURCE = 'https://www.codewars.com/kata/58f8a3a27a5c28d92e000144'
