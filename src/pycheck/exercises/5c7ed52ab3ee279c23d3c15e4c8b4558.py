TITLE = 'Separando mayúsculas y minúsculas'

DESCRIPTION = '''
Dada una lista de palabras, escriba una función que devuelva dos listas, la primera con las palabras que vienen en minúsculas y la segunda con las palabras que vienen en mayúsculas.

Notas:
- Ignore aquellas palabras que mezclan mayúsculas y minúsculas.
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'split_case',
    'PARAMS': [
        ['words', list],
    ],
    'RETURN': [
        ['lower_words', list],
        ['upper_words', list],
    ],
}

CHECK_CASES = [
    [
        [['AZUL', 'blanco', 'NEGRO', 'amarillo']],
        [['blanco', 'amarillo'], ['AZUL', 'NEGRO']],
    ],
    [
        [['FEDORA', 'debian', 'OPENSUSE', 'ubuntu', 'MacOS']],
        [['debian', 'ubuntu'], ['FEDORA', 'OPENSUSE']],
    ],
    [
        [['python', 'c', 'javascript']],
        [['python', 'c', 'javascript'], []],
    ],
]
