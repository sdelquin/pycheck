from pathlib import Path

TITLE = 'Frecuencia de palabras'

DESCRIPTION = '''
Dado un fichero de texto y un valor umbral se pide hacer un programa en Python que calcule la frecuencia de cada palabra en el fichero de entrada pero únicamente mostrando aquellas entradas con frecuencia mayor o igual que el valor umbral.

Notas:
- La salida se dará en forma de diccionario donde las claves serán las palabras y los valores serán las frecuencias.
- Se puede suponer que todas las palabras se separan única y exclusivamente por un espacio.
- No hay que hacer distinción entre mayúsculas y minúsculas.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['input_path', Path],
        ['lower_bound', int],
    ],
    'RETURN': [
        ['freq', dict],
    ],
}

CHECK_CASES = [
    [['data/word_freq/cistercian.txt', 9], [{'the': 20, 'to': 10}]],
    [
        ['data/word_freq/cistercian.txt', 8],
        [{'the': 20, 'of': 8, 'a': 8, 'to': 10, 'you': 8}],
    ],
    [
        ['data/word_freq/cistercian.txt', 7],
        [{'the': 20, 'of': 8, 'in': 7, 'a': 8, 'and': 7, 'to': 10, 'you': 8}],
    ],
    [
        ['data/word_freq/cistercian.txt', 6],
        [{'the': 20, 'of': 8, 'in': 7, 'a': 8, 'and': 7, 'what': 6, 'to': 10, 'you': 8}],
    ],
    [
        ['data/word_freq/cistercian.txt', 5],
        [
            {
                'the': 20,
                'of': 8,
                'in': 7,
                'a': 8,
                'for': 5,
                'and': 7,
                'what': 6,
                'to': 10,
                'you': 8,
            }
        ],
    ],
]
