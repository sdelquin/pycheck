from pathlib import Path

TITLE = 'Sumando matrices'

DESCRIPTION = '''
Dados dos ficheros de texto que contienen sendas matrices _cuadradas_, obtenga la suma de dichas matrices en un fichero de salida con el mismo formato.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['matrix1_path', Path],
        ['matrix2_path', Path],
    ],
    'RETURN': [
        ['result_path', Path],
    ],
}

CHECK_CASES = [
    [
        ['data/sum_matrix/matrix1.dat', 'data/sum_matrix/matrix2.dat'],
        ['data/sum_matrix/result.dat'],
    ],
]
