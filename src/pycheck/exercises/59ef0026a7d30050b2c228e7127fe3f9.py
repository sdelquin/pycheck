TITLE = 'Potencias de 2'

DESCRIPTION = '''
Dado un número entero no negativo obtenga una lista con todas las potencias de 2 con el exponente variando desde 0 hasta dicho valor (inclusive).

¿Podrías resolverlo también con _listas por comprensión_?
'''

ENTRYPOINT = {
    'PARAMS': [
        ['num_powers', int],
    ],
    'RETURN': [
        ['powers2', list],
    ],
}

CHECK_CASES = [
    [[0], [[1]]],
    [[1], [[1, 2]]],
    [[2], [[1, 2, 4]]],
]

SOURCE = 'https://www.codewars.com/kata/57a083a57cb1f31db7000028'
