TITLE = 'Claves desde valores'

DESCRIPTION = """
Se pide obtener la(s) clave(s) de un diccionario cuyo valor es uno dado.

Notas:
- Habrá que devolver una tupla con las claves correspondientes.
- Puede que el valor buscado no exista en el diccionario.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['items', dict],
        ['target_value', int],
    ],
    'RETURN': [
        ['source_keys', tuple],
    ],
}

CHECK_CASES = [
    [[{'A': 1, 'B': 2, 'C': 3, 'D': 3, 'E': 4}, 3], [('C', 'D')]],
    [[{'X': 10, 'Y': 10, 'Z': 10}, 10], [('X', 'Y', 'Z')]],
    [[{'U': 5, 'V': 6, 'W': 7, 'R': 8}, 4], [()]],
    [[{'U': 5, 'V': 6, 'W': 7, 'R': 8}, 8], [('R',)]],
]
