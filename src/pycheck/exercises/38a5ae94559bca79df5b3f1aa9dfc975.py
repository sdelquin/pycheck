DESCRIPTION = '''
Dada una lista de valores numéricos, obtenga la suma de los valores invertidos.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['numbers', list],
    ],
    'RETURN': [
        ['add_inv', int],
    ],
}

CHECK_CASES = [
    [[[1, 2, 3, 4, 5]], [-15]],
    [[[-1, 2, -3, 4, -5]], [3]],
    [[[1, -2, 3, -4, 5]], [-3]],
]

SOURCE = 'https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad'
