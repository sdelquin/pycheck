TITLE = 'Borrando valores clave'

DESCRIPTION = '''
Dado un **diccionario** _cuyos valores son listas_, genere un diccionario nuevo donde se borre el contenido de dichas listas.

Resuelva el ejercicio utilizando **diccionarios por comprensión**.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['items', dict],
    ],
    'RETURN': [
        ['citems', dict],
    ],
}

CHECK_CASES = [
    [
        [{'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}],
        [{'C1': [], 'C2': [], 'C3': []}],
    ],
]
