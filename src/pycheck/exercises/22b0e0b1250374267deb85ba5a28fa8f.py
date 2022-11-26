TITLE = 'Palabras con longitud'

DESCRIPTION = '''
Dada una cadena de texto conteniendo palabras separadas por espacios, obtenga una lista que contenga cada palabra junto a su tamaño.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['words_length', list],
    ],
}

CHECK_CASES = [
    [['todo se transforma'], [['todo 4', 'se 2', 'transforma 10']]],
    [['prueba'], [['prueba 6']]],
    [['tiene mucha importancia'], [['tiene 5', 'mucha 5', 'importancia 11']]],
]

SOURCE = 'https://www.codewars.com/kata/559d2284b5bb6799e9000047'
