from pathlib import Path

TITLE = '¿Dónde están las palabras? Matarile'

DESCRIPTION = '''
Dado un fichero de texto y una palabra objetivo se pide indicar el número de línea y el número de columna en la que se encuentran todas las ocurrencias de dicha palabra en el fichero de entrada.

Notas:
- La salida del programa será una lista de tuplas. Cada tupla contiene dos valores: el número de línea y el número de columna.
- Se puede suponer que las palabras se separan por un único espacio.
- La búsqueda debe funcionar aunque no coincidan mayúsculas y minúsculas.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['data_path', Path],
        ['target_word', str],
    ],
    'RETURN': [
        ['matches', list],
    ],
}

CHECK_CASES = [
    [['data/find_words/bzrp.txt', 'persona'], [[(41, 17), (43, 17), (73, 17), (75, 17)]]],
    [['data/find_words/bzrp.txt', 'amor'], [[(52, 5)]]],
    [['data/find_words/bzrp.txt', 'aquí'], [[(11, 1), (68, 1)]]],
    [
        ['data/find_words/bzrp.txt', 'yo'],
        [[(18, 5), (19, 15), (20, 15), (33, 1), (55, 1), (59, 1), (70, 1), (76, 17)]],
    ],
]
