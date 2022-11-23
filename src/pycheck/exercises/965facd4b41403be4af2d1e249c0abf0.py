DESCRIPTION = '''
Dada una lista de enteros y enteros como cadenas de texto, calcule la suma de todos los
valores de la lista como si todos sus elementos fueran números.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['items', list],
    ],
    'RETURN': [
        ['sum_items', int],
    ],
}

CHECK_CASES = [
    [[[1, '2', 3, '4', 5]], [15]],
    [[['0', '-1', '-2', '-3', '-4', '-5']], [-15]],
    [[[100, 90, 80, 70, '60', '50', '40', '30', '20', '10']], [550]],
]

SRC = 'https://www.codewars.com/kata/57eaeb9578748ff92a000009'
