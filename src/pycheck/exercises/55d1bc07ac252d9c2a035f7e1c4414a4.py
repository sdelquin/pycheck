TITLE = 'Intercambiar clave-valor en diccionarios'

DESCRIPTION = """
Partiendo de un diccionario de entrada, se pide construir un nuevo diccionario donde las claves sean los valores y los valores sean las claves.

En el caso de que un valor que se convierte en clave ya exista como clave, habrá que asignarle el mayor valor que corresponda.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['data', dict],
    ],
    'RETURN': [
        ['swapped_data', dict],
    ],
}

CHECK_CASES = [
    [[{'a': 1, 'b': 2, 'c': 3}], [{1: 'a', 2: 'b', 3: 'c'}]],
    [[{'a': 1, 'b': 2, 'c': 2, 'd': 3}], [{1: 'a', 2: 'c', 3: 'd'}]],
    [[{'d': 4, 'b': 2, 'c': 3, 'a': 4}], [{4: 'd', 2: 'b', 3: 'c'}]],
]
