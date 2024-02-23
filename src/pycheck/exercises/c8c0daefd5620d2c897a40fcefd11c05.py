from pathlib import Path

TITLE = 'Sumando filas'

DESCRIPTION = """
Dado un fichero de entrada que contiene números enteros (positivos y/o negativos), se pide obtener **la suma por filas** devolviendo una _tupla_ con los resultados.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['data_path', Path],
    ],
    'RETURN': [
        ['rsum', tuple],
    ],
}

CHECK_CASES = [
    [['data/sum_rows/data1.txt'], [(5, 48, 27)]],
    [['data/sum_rows/data2.txt'], [(-17, -98, 47, -54, -11)]],
    [['data/sum_rows/data3.txt'], [(281, 123, 155, 255, 198, 242)]],
]
