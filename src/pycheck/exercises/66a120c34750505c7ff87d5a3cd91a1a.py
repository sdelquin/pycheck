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
    [[{}], [True]],
]
