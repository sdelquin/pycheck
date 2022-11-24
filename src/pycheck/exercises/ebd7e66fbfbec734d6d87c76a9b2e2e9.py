DESCRIPTION = '''
A partir de una lista de valores numéricos y un tamaño, obtenga otra lista con todos los
subconjuntos en cascada que se puedan crear con dicho tamaño.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['values', list],
        ['size', int],
    ],
    'RETURN': [
        ['cascading', list],
    ],
}

CHECK_CASES = [
    [[[1, 2, 3, 4], 3], [[[1, 2, 3], [2, 3, 4]]]],
    [[[1, 2, 3, 4], 2], [[[1, 2], [2, 3], [3, 4]]]],
    [[[1, 2, 3, 4], 1], [[[1], [2], [3], [4]]]],
    [[[], 1], [[]]],
]

SOURCE = 'https://www.codewars.com/kata/545af3d185166a3dec001190'
