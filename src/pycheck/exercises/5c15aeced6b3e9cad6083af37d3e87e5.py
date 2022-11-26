TITLE = 'Descubriendo impares'

DESCRIPTION = '''
Devuelva una lista únicamente con los números impares que vienen en la entrada. Tenga en cuenta que pueden venir valores repetidos en la entrada.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['values', list],
    ],
    'RETURN': [
        ['odds', list],
    ],
}

CHECK_CASES = [
    [[[1, 2, 3, 4, 5]], [[1, 3, 5]]],
    [[[1, 1, 2, 2, 3, 3]], [[1, 3]]],
    [[[2, 4, 6]], [[]]],
]

SOURCE = 'https://www.codewars.com/kata/559f80b87fa8512e3e0000f5'
