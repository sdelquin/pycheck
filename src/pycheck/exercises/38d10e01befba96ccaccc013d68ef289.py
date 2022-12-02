TITLE = 'Cada nota en su sitio'

DESCRIPTION = '''
Tenemos almacenadas las notas de un examen en un diccionario. Es necesario separar al alumnado que aprobó y al que suspendió en dos diccionarios. Igualmente habrá que pasar a mayúsculas el nombre del alumnado que aprobó y a minúsculas el nombre del alumnado que suspendió. Escriba un programa en Python que realice esta operación usando _diccionarios por comprensión_.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['marks', dict],
    ],
    'RETURN': [
        ['passed', dict],
        ['failed', dict],
    ],
}

CHECK_CASES = [
    [
        [{'Ana': 4, 'Domingo': 7, 'Eva': 5, 'Álvaro': 3, 'Juan': 8, 'Belén': 1}],
        [{'DOMINGO': 7, 'EVA': 5, 'JUAN': 8}, {'ana': 4, 'álvaro': 3, 'belén': 1}],
    ],
]
