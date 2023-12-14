TITLE = 'Suma de la diagonal principal'

DESCRIPTION = """
Escriba un programa en Python que acepte una lista de listas representando una matriz numérica de valores enteros y compute la suma de los elementos de la diagonal principal.

Notas:
- Si no se trata de una [Matriz cuadrada](https://es.wikipedia.org/wiki/Matriz_cuadrada) devuelva None.
- Puede afrontar el ejercicio en _versión clásica_ o con _listas por comprensión_. ¡O incluso ambas!

"""

ENTRYPOINT = {
    'PARAMS': [
        ['matrix', list],
    ],
    'RETURN': [
        ['sum_diagonal', int],
    ],
}

CHECK_CASES = [
    [[[[4, 6, 1], [2, 9, 3], [1, 7, 7]]], [20]],
    [[[[1, 1], [1, 1]]], [2]],
    [[[[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [4, 2, 1, 8]]], [24]],
    [[[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]], [None]],
]
