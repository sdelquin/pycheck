TITLE = 'Palíndromo'

DESCRIPTION = '''
Escriba una función en Python que determine si una cadena de texto es un [palíndromo](https://es.wikipedia.org/wiki/Pal%C3%ADndromo).
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'is_palindrome',
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['palindrome_text', bool],
    ],
}

CHECK_CASES = [
    [['ana lava lana'], [True]],
    [['Yo dono rosas oro no doy'], [True]],
    [['yo soy'], [True]],
    [['La ruta natural'], [True]],
    [['No soy un palíndromo'], [False]],
]
