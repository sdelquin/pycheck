from pathlib import Path

TITLE = 'Han cantado línea'

DESCRIPTION = '''
Dado un fichero de texto y un número de línea como entradas al programa, devuelva la línea que corresponda del fichero. Si el número de línea indicado no corresponde con ninguno del fichero se debe devolver None.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['input_path', Path],
        ['line_no', int],
    ],
    'RETURN': [
        ['line', str],
    ],
}

CHECK_CASES = [
    [['data/get_line/nasdaq.txt', 20], ['Starbucks Corp']],
    [['data/get_line/nasdaq.txt', 51], ['Palo Alto Networks Inc']],
    [['data/get_line/starwars.dat', 3], ['Return of the Jedi,May 25-1983']],
    [['data/get_line/starwars.dat', 8], ['The Last Jedi,December 15-2017']],
    [['data/get_line/nasdaq.txt', 0], [None]],
    [['data/get_line/starwars.dat', -10], [None]],
]
