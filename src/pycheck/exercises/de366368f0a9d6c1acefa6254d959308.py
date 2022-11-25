TITLE = 'Aplana la lista'

DESCRIPTION = '''
Dada una lista - que puede contener sublistas (sólo en 1 nivel de anidamiento) - genere otra lista "aplanada".
'''

ENTRYPOINT = {
    'PARAMS': [
        ['elements', list],
    ],
    'RETURN': [
        ['flatten_elements', list],
    ],
}

CHECK_CASES = [
    [
        [[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]],
        [[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]],
    ],
    [[['a', ['b', 'c'], 'd']], [['a', 'b', 'c', 'd']]],
    [[[[1], [2], [3], [4]]], [[1, 2, 3, 4]]],
]
