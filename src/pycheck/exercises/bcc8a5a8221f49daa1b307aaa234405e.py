DESCRIPTION = '''
Dado un número entero no negativo, genere una lista con los dígitos de dicho número
en orden inverso.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['number', int],
    ],
    'RETURN': [
        ['rev_digits', list],
    ],
}

CHECK_CASES = [
    [[35231], [[1, 3, 2, 5, 3]]],
    [[1], [[1]]],
    [[4287690], [[0, 9, 6, 7, 8, 2, 4]]],
]

SOURCE = 'https://www.codewars.com/kata/5583090cbe83f4fd8c000051'
