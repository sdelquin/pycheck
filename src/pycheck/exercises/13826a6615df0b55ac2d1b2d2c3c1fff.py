TITLE = 'Ficho cuando toca'

DESCRIPTION = '''
Dada una hora en formato HH:MM y un número de minutos (en valor entero), calcule la hora resultante (en formato HH:MM) si sumamos los minutos a la hora de entrada.

Trabaje con formato de 24 horas.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['time', str],
        ['offset', int],
    ],
    'RETURN': [
        ['final_time', str],
    ],
}

CHECK_CASES = [
    [['17:15', 240], ['21:15']],
    [['8:05', 265], ['12:30']],
    [['22:55', 315], ['4:10']],
]
