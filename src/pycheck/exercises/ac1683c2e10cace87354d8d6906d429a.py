TITLE = 'La clave es la clave'

DESCRIPTION = '''
A partir de un diccionario, obtenga un nuevo diccionario eliminando los espacios de sus claves respetando los valores correspondientes.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['items', dict],
    ],
    'RETURN': [
        ['fitems', dict],
    ],
}

CHECK_CASES = [
    [
        [{'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}],
        [{'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}],
    ],
]
