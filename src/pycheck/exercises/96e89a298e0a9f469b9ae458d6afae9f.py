from pathlib import Path

TITLE = 'Simulando el comando head'

DESCRIPTION = """
Dado un fichero de entrada y un número _n_ de líneas, devuelva las _n_ primeras líneas del fichero como una cadena de texto.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['file', Path],
        ['n', int],
    ],
    'RETURN': [
        ['lines', str],
    ],
}

CHECK_CASES = [
    [['data/head/nba_season22.txt', 3], ['Quentin Grimes\nQuenton Jackson\nPat Connaughton\n']],
    [
        ['data/head/nba_season22.txt', 5],
        ['Quentin Grimes\nQuenton Jackson\nPat Connaughton\nRJ Barrett\nPrecious Achiuwa\n'],
    ],
    [
        ['data/head/nba_season22.txt', 7],
        [
            'Quentin Grimes\nQuenton Jackson\nPat Connaughton\nRJ Barrett\nPrecious Achiuwa\nRaiQuan Gray\nR.J. Hampton\n'
        ],
    ],
]
