TITLE = 'Contando milisegundos'

DESCRIPTION = '''
Un reloj muestra horas, minutos y segundos a partir de medianoche. Calcule el número de milisegundos desde media noche a partir de estos tres parámetros.

0 <= horas <= 23
0 <= minutos <= 59
0 <= segundos <= 59
'''

ENTRYPOINT = {
    'PARAMS': [
        ['hours', int],
        ['minutes', int],
        ['seconds', int],
    ],
    'RETURN': [
        ['time_since_midnight', float],
    ],
}

CHECK_CASES = [
    [[0, 1, 1], [61000]],
    [[2, 1, 0], [7260000]],
    [[10, 45, 30], [38730000]],
]

SOURCE = 'https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a'
