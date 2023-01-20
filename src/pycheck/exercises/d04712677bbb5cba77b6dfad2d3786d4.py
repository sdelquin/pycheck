TITLE = 'Ordene mi diccionario'

DESCRIPTION = '''
Dado un diccionario de entrada, escriba un programa que lo ordene en base a sus valores de forma ascendente.

Se puede asumir que:
- Tanto las claves como los valores del diccionario de entrada van a ser cadenas de texto.
- Tanto las claves como los valores del diccionario de entrada no van a contener dos puntos ':'
'''

ENTRYPOINT = {
    'PARAMS': [
        ['unsorted_items', dict],
    ],
    'RETURN': [
        ['sorted_items', dict],
    ],
}

CHECK_CASES = [
    [[{'a': 'two', 'b': 'one', 'c': 'three'}], [{'b': 'one', 'c': 'three', 'a': 'two'}]],
    [
        [{'mar': 'azul', 'tierra': 'marrón', 'aire': 'blanco'}],
        [{'mar': 'azul', 'aire': 'blanco', 'tierra': 'marrón'}],
    ],
    [
        [{'M': 'MacOS', 'L': 'Linux', 'W': 'Windows'}],
        [{'L': 'Linux', 'M': 'MacOS', 'W': 'Windows'}],
    ],
    [[{}], [{}]],
]
