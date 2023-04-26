from pathlib import Path

TITLE = 'Temperaturas medias'

DESCRIPTION = '''
Dado un fichero de entrada con 12 filas (meses) y 31 columnas (temperaturas de cada día) se pide:
1. Leer el fichero de datos.
2. Calcular la temperatura media de cada mes.
3. Escribir un fichero de salida con 12 filas (_meses_) y la temperatura media de cada mes.
4. Usar formato de string con 2 cifras decimales para la salida.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['input_path', Path],
    ],
    'RETURN': [
        ['output_path', Path],
    ],
}

CHECK_CASES = [
    [['data/avg_temps/temperatures.dat'], ['data/avg_temps/avg_temps.dat']],
]
