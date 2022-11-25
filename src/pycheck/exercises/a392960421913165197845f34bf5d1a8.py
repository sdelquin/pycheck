TITLE = 'Xor'

DESCRIPTION = '''
El "o exclusivo" (xor) es una operación lógica que sigue las siguientes reglas:
- False xor False -> False
- True xor False -> True
- False xor True -> True
- True xor True -> False

Básicamente sólo es verdadero cuando una (y solo una) de las dos entradas es verdadera.
Escriba un programa que calcule el xor a partir de dos parámetros de entrada.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['v1', bool],
        ['v2', bool],
    ],
    'RETURN': [
        ['xor', bool],
    ],
}

CHECK_CASES = [
    [[False, False], [False]],
    [[True, False], [True]],
    [[False, True], [True]],
    [[True, True], [False]],
]

SOURCE = 'https://www.codewars.com/kata/56fa3c5ce4d45d2a52001b3c'
