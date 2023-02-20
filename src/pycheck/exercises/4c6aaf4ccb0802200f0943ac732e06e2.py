TITLE = 'Cuadrado mágico'

DESCRIPTION = '''
Un [cuadrado mágico](https://es.wikipedia.org/wiki/Cuadrado_m%C3%A1gico) es una **matriz cuadrada** donde _la suma de sus números por filas, columnas y diagonales es la misma_.

Dada una lista de listas (matriz cuadrada) determine si es o no es un cuadrado mágico.

Notas:
- Se puede suponer que todas las matrices de entrada serán cuadradas.
- Ayúdate de funciones auxilares.
- Las listas por comprensión son un poderoso aliado.
- Tenga en cuenta ser eficiente.
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'is_magic_square',
    'PARAMS': [
        ['values', list],
    ],
    'RETURN': [
        ['output', bool],
    ],
}

CHECK_CASES = [
    [[[]], [True]],
    [[[[4, 9, 2], [3, 5, 7], [8, 1, 6]]], [True]],
    [[[[4, 9, 1], [3, 5, 7], [8, 1, 6]]], [False]],
    [[[[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]], [True]],
    [[[[16, 3, 2, 12], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]], [False]],
    [[[[1, 14, 14, 4], [11, 7, 6, 9], [8, 10, 10, 5], [13, 2, 3, 15]]], [True]],
    [[[[1, 14, 14, 3], [11, 7, 6, 9], [8, 10, 10, 5], [13, 2, 3, 15]]], [False]],
    [
        [
            [
                [49, 48, 11, 46, 6, 12, 3],
                [7, 13, 14, 31, 32, 35, 43],
                [8, 30, 28, 21, 26, 20, 42],
                [45, 33, 23, 25, 27, 17, 5],
                [9, 34, 24, 29, 22, 16, 41],
                [10, 15, 36, 19, 18, 37, 40],
                [47, 2, 39, 4, 44, 38, 1],
            ]
        ],
        [True],
    ],
]
