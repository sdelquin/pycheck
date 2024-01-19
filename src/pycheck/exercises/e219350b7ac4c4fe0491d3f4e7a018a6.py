TITLE = '¿Está ordenado?'

DESCRIPTION = """
Determine si una lista de valores están ordenados (de forma ascendente).

Está prohibido el uso de las funciones _sort()_, _sorted()_, _min()_ y _max()_.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['items', list],
    ],
    'RETURN': [
        ['items_sorted', bool],
    ],
}

CHECK_CASES = [
    [[['a', 'f', 't']], [True]],
    [[['f', 'a', 't']], [False]],
    [[[0, 10, 100, 1000]], [True]],
    [[[1, 0]], [False]],
    [[[0]], [True]],
    [[[]], [True]],
    [[['Z']], [True]],
    [[['😀', '😡']], [True]],
    [[['4.5', '1.2', '7.3', '9.9']], [False]],
]
