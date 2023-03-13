TITLE = 'Sumando con anidamiento'

DESCRIPTION = '''
Dada una lista que puede contener números o listas anidadas de números, calcule la suma de todos sus valores utilizando una **función recursiva**.
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'sum_nested',
    'PARAMS': [
        ['items', list],
    ],
    'RETURN': [
        ['_sum', int],
    ],
}

CHECK_CASES = [
    [[[1, [2, 4], 5, [6, [7, 8]]]], [33]],
    [[[10, [5, 6, [7, [8, 9]]]]], [45]],
    [[[1, [2, [3, [4]]]]], [10]],
    [[[]], [0]],
]
