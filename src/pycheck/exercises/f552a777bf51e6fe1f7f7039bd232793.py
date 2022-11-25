TITLE = 'Desplegando caracteres'

DESCRIPTION = '''
Dada una lista de strings, obtenga otra lista que contenga todos los caracteres de cada uno de los strings de la lista de entrada.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['texts', list],
    ],
    'RETURN': [
        ['chars', list],
    ],
}

CHECK_CASES = [
    [[['uno', 'dos', 'tres']], [['u', 'n', 'o', 'd', 'o', 's', 't', 'r', 'e', 's']]],
    [[['', '', '']], [[]]],
    [[['abc', 'abc', 'abc']], [['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']]],
]
