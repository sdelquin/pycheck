TITLE = 'Contando letras'

DESCRIPTION = '''
Usando un diccionario, cuente el número de veces que se repite cada letra en una cadena de texto dada.

NOTA: No se puede usar la función "count".
'''

ENTRYPOINT = {
    'PARAMS': [
        ['sentence', str],
    ],
    'RETURN': [
        ['counter', dict],
    ],
}

CHECK_CASES = [
    [['boom'], [{'b': 1, 'o': 2, 'm': 1}]],
    [['ada'], [{'a': 2, 'd': 1}]],
    [['tree'], [{'t': 1, 'r': 1, 'e': 2}]],
    [['debugging'], [{'d': 1, 'e': 1, 'b': 1, 'u': 1, 'g': 3, 'i': 1, 'n': 1}]],
    [[''], [{}]],
]
