TITLE = 'Sumando solo positivos'

DESCRIPTION = '''
Dada una lista de números, calcule la suma de todos los valores positivos.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['numbers', list],
    ],
    'RETURN': [
        ['sum_positive', int],
    ],
}

CHECK_CASES = [
    [[[1, -4, 7, 12]], [20]],
    [[[-1, -1, -1, -1, -1, -1]], [0]],
    [[[1, -1, 2, -2, 3, -3, 4, -4, 5, -5]], [15]],
    [[[]], [0]],
]

SOURCE = 'https://www.codewars.com/kata/5715eaedb436cf5606000381'
