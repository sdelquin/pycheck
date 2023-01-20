TITLE = 'Consonantes comunes'

DESCRIPTION = '''
Dadas dos cadenas de texto, obtenga una nueva cadena de texto con las letras consonantes que se repiten en ambas frases. Ignore los espacios en blanco y muestre la cadena de salida con sus letras ordenadas.

Este ejercicio también se puede resolver mediante _conjuntos por comprensión_.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['text1', str],
        ['text2', str],
    ],
    'RETURN': [
        ['cconst', str],
    ],
}

CHECK_CASES = [
    [['Flat is better than nested', 'Readability counts'], ['bdlnst']],
    [['Now is better than never', 'Beautiful is better than ugly'], ['bhnrst']],
    [['Hello', 'Bye'], ['']],
]
