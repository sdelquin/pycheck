TITLE = 'Obteniendo el número de palabras'

DESCRIPTION = '''
Sabiendo que la longitud de una lista se calcula igual que la longitud de una cadena de texto, obtenga el número de palabras que contiene una cadena de texto dada.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['num_words', int],
    ],
}

CHECK_CASES = [
    [['Before software can be reusable it first has to be usable'], [11]],
    [['You should prefer readability over performance in almost all cases'], [10]],
    [['Models are not right or wrong they are more or less useful'], [12]],
]
