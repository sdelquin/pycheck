TITLE = 'Valores iguales en diccionario'

DESCRIPTION = '''
Acepte un diccionario como entrada y compruebe si todos sus valores son iguales o no.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['items', dict],
    ],
    'RETURN': [
        ['all_same', bool],
    ],
}

CHECK_CASES = [
    [[{'a': 1, 'b': 1, 'c': 1, 'd': 1}], [True]],
    [[{'a': 1, 'b': 2, 'c': 3, 'd': 4}], [False]],
    [[{1: 'a', 2: 'b', 3: 'c', 4: 'd'}], [False]],
    [[{1: 'a', 2: 'a', 3: 'a', 4: 'a'}], [True]],
    [[{}], [True]],
]
