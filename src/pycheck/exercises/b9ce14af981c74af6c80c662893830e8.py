TITLE = 'Tupla de duplas'

DESCRIPTION = '''
Dada una tupla de duplas (2 valores) obtenga una tupla con dos diccionarios:
- El primer diccionario con los primeros valores de cada dupla.
- El segundo diccionario con los segundos valores de cada dupla.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['input', tuple],
    ],
    'RETURN': [
        ['output', set],
    ],
}

CHECK_CASES = [
    [[((4, 3), (8, 2), (7, 5), (8, 2), (9, 1))], [({8, 9, 4, 7}, {1, 2, 3, 5})]],
    [[((1, 2), ('|', '@'), ('!', '\"'))], [({1, '!', '|'}, {2, '"', '@'})]],
]
