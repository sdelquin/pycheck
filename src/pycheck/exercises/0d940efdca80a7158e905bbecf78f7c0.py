TITLE = 'Temperaturas medias'

DESCRIPTION = '''
Dado un fichero de entrada con 12 filas (meses) y 31 columnas (temperaturas de cada día) se pide:
1. Leer el fichero de datos.
2. Calcular la temperatura media de cada mes.
3. Escribir un fichero de salida con 12 filas (_meses_) y la temperatura media de cada mes _redondeando a 2 decimales_.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['input.dat', str],
    ],
    'RETURN': [
        ['output.dat', str],
    ],
}

CHECK_CASES = [
    [['temperatures.dat'], ['avg_temps.dat']],
]
