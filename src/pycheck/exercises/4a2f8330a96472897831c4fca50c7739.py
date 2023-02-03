from pathlib import Path

TITLE = 'Sumando columnas'

DESCRIPTION = '''
Dado un fichero de entrada que contiene números enteros (positivos y/o negativos), se pide obtener **la suma por columnas** devolviendo una _tupla_ con los resultados.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['data_path', Path],
    ],
    'RETURN': [
        ['csum', tuple],
    ],
}

CHECK_CASES = [
    [['data/sum_cols/data1.txt'], [(42, 8, 30)]],
    [['data/sum_cols/data2.txt'], [(11, -59, -22, -19, 11, 17, -72)]],
    [['data/sum_cols/data3.txt'], [(299, 271, 434, 250)]],
]
