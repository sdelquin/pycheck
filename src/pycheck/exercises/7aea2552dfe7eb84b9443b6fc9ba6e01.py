from pathlib import Path

TITLE = 'Simulando el comando tail'

DESCRIPTION = """
Dado un fichero de entrada y un número _n_ de líneas, devuelva las _n_ últimas líneas del fichero como una cadena de texto.
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
    [['data/head/nba_season22.txt', 3], ['John Collins\nJericho Sims\nJaMychal Green']],
    [
        ['data/head/nba_season22.txt', 5],
        ['Joel Embiid\nJohn Butler Jr.\nJohn Collins\nJericho Sims\nJaMychal Green'],
    ],
    [
        ['data/head/nba_season22.txt', 7],
        [
            'Joe Ingles\nJoe Wieskamp\nJoel Embiid\nJohn Butler Jr.\nJohn Collins\nJericho Sims\nJaMychal Green'
        ],
    ],
]
