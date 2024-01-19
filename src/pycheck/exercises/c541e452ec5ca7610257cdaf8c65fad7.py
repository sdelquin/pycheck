TITLE = 'Only words'

DESCRIPTION = """
Dada una lista heterogénea de elementos, sume las longitudes de aquellos elementos que sean cadenas de texto.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['items', list],
    ],
    'RETURN': [
        ['sum_words', int],
    ],
}

CHECK_CASES = [
    [[[99, 'x', 3, 5, 'hello', 'banana', 4]], [12]],
    [[[0, 1, 2, 3, 4, 5]], [0]],
    [[['']], [0]],
    [[['this', 'is', 'you']], [9]],
    [[[1, 'one', 2, 'two', 3, 'three', 4, 'four', 5, 'five']], [19]],
]
