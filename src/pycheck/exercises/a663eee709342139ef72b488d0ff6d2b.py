from pathlib import Path

TITLE = '¿Dónde están las palabras? Matarile'

DESCRIPTION = '''
Dado un fichero de texto y una palabra objetivo se pide indicar el número de línea y el número de columna en la que se encuentran todas las ocurrencias de dicha palabra en el fichero de entrada.

Notas:
- La salida del programa será una lista de tuplas. Cada tupla contiene dos valores: el número de línea y el número de columna.
- Se puede suponer que las palabras se separan por un único espacio, pero hay que tener en cuenta la posible existencia de los siguientes caracteres como frontera de palabras: .,:;()'¡!-
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
    [['data/find_words/bzrp.txt', 'buena'], [[(41, 25), (43, 25), (73, 25), (75, 25)]]],
    [
        ['data/find_words/bzrp.txt', 'yo'],
        [
            [
                (18, 5),
                (19, 15),
                (20, 15),
                (29, 1),
                (33, 1),
                (55, 1),
                (59, 1),
                (70, 1),
                (76, 17),
            ]
        ],
    ],
    [
        ['data/find_words/bzrp.txt', 'tú'],
        [
            [
                (2, 17),
                (7, 17),
                (20, 41),
                (21, 16),
                (24, 40),
                (45, 17),
                (46, 16),
                (49, 40),
                (76, 43),
                (77, 16),
                (80, 40),
                (88, 40),
            ]
        ],
    ],
    [
        ['data/find_words/bzrp.txt', 'me'],
        [[(30, 8), (30, 21), (36, 1), (38, 16), (38, 29), (67, 17), (68, 6)]],
    ],
    [
        ['data/find_words/bzrp.txt', 'Tás'],
        [[(58, 2)]],
    ],
]
