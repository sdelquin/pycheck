TITLE = 'Separando el tiempo'

DESCRIPTION = '''
Dada una cantidad (entera) de tiempo en segundos, calcule el número de horas, minutos y segundos que corresponden.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['seconds', int],
    ],
    'RETURN': [
        ['hours', int],
        ['minutes', int],
        ['seconds', int],
    ],
}

CHECK_CASES = [
    [[31256], (8, 40, 56)],
    [[3601], (1, 0, 1)],
    [[9099], (2, 31, 39)],
]
