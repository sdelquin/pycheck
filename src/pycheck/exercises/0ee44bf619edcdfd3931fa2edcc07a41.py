TITLE = 'No me interesan los pares'

DESCRIPTION = '''
Dada una lista, genere otra lista eliminando los elementos que ocupan posiciones pares.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['items', list],
    ],
    'RETURN': [
        ['filter', list],
    ],
}

CHECK_CASES = [
    [[[1, 2, 1, 2, 1, 2]], [[1, 1, 1]]],
    [[['a', 'b', 'a', 'b', 'a']], [['a', 'a', 'a']]],
    [[[1, 1, 2, 2, 3, 3]], [[1, 2, 3]]],
]

SOURCE = 'https://www.codewars.com/kata/5769b3802ae6f8e4890009d2'
