DESCRIPTION = '''
Dado un número entero no negativo "n", obtenga una lista con los números desde "n" hasta 1.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['n', int],
    ],
    'RETURN': [
        ['rev_nums', list],
    ],
}

CHECK_CASES = [
    [[5], [[5, 4, 3, 2, 1]]],
    [[10], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]],
    [[1], [[1]]],
    [[0], [[]]],
]

SOURCE = 'https://www.codewars.com/kata/5a00e05cc374cb34d100000d'
