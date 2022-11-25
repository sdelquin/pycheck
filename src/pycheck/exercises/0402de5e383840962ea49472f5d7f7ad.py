DESCRIPTION = '''
Dada una lista de valores numéricos enteros y un valor entero "target", obtenga
la mayor distancia de cualquier elemento de la lista con respecto a "target".
'''

ENTRYPOINT = {
    'PARAMS': [
        ['values', list],
        ['target', int],
    ],
    'RETURN': [
        ['max_diff', int],
    ],
}

CHECK_CASES = [
    [[[7, 3, 1, 12, 21, 4], 8], [13]],
    [[[-5, -9, 12, 18], 15], [24]],
    [[[1, 1, 1], 1], [0]],
    [[[], 1], [0]],
]
