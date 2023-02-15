TITLE = 'Pangrama'

DESCRIPTION = '''
Escriba una función en Python que determine si una cadena de texto es un [pangrama](https://es.wikipedia.org/wiki/Pangrama).
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'is_pangram',
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['pangram_text', bool],
    ],
}

CHECK_CASES = [
    [['The quick brown fox jumps over the lazy dog'], [True]],
    [['Sylvia wagt quick den Jux bei Pforzheim'], [True]],
    [['Portez ce whisky au vieux juge blond qui fume'], [True]],
    [['No soy un pangrama'], [False]],
]
