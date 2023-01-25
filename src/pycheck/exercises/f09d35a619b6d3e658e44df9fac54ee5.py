TITLE = 'Consonantes comunes'

DESCRIPTION = '''
Dadas dos cadenas de texto, obtenga una nueva cadena de texto con las letras consonantes que se repiten en ambas frases. Ignore los espacios en blanco y muestre la cadena de salida con sus letras ordenadas.

Este ejercicio también se puede resolver mediante _conjuntos por comprensión_.

Notas:
- Las vocales pueden estar en minúsculas o en mayúsculas.
- Una consonante minúscula es equivalente a una consonantes mayúscula.
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
    [['Flat is bEtter than nested', 'Readability counts'], ['bdlnrst']],
    [['Now is better thAn never', 'Beautiful is better than ugly'], ['bhnrst']],
    [['Hello', 'Bye'], ['']],
]
