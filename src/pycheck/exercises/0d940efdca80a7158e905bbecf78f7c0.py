from pycheck.lib.checkers import check_file_as_expected, check_file_exists

TITLE = 'Temperaturas medias'

DESCRIPTION = '''
Dado un fichero de entrada con 12 filas (meses) y 31 columnas (temperaturas de cada día) se pide:
1. Leer el fichero de datos.
2. Calcular la temperatura media de cada mes.
3. Escribir un fichero de salida con 12 filas (_meses_) y la temperatura media de cada mes _redondeando a 2 decimales_.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['input', str],
    ],
    'RETURN': None,
}

CHECK_CASES = [
    [['data/avg_temps/temperatures.dat'], []],
]

TARGET_CHECKS = [
    [check_file_exists, 'data/avg_temps/avg_temps.dat'],
    [check_file_as_expected, 'data/avg_temps/avg_temps.dat'],
]
