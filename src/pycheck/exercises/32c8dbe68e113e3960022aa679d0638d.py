DESCRIPTION = '''
Dada una lista de números, obtenga otra lista donde se eliminen los duplicados.
Mantenga el orden de los números en la lista de salida tal y como aparecen en la de entrada.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['nums_dups', list],
    ],
    'RETURN': [
        ['nums_unique', list],
    ],
}

CHECK_CASES = [
    [[[2, 3, 2, 2, 1, 5, 4, 2, 4, 9]], [[2, 3, 1, 5, 4, 9]]],
    [[[0, 9, 0, 9, 0, 9]], [[0, 9]]],
    [[[1, 2, 3, 4, 5, 4, 3, 2, 1]], [[1, 2, 3, 4, 5]]],
]

SOURCE = 'https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118'
