TITLE = 'Por encima y por debajo de la media'

DESCRIPTION = """
Dada una lista de entrada que contiene valores flotantes de **notas de exámenes**, obtenga dos listas de salida:
- La primera lista con las notas menores o iguales que la media.
- La segunda lista con las notas mayores que la media.

Notas:
- El orden de las notas debe ser el mismo que tienen en la lista de entrada.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['marks', list],
    ],
    'RETURN': [
        ['below_avg', list],
        ['above_avg', list],
    ],
}

CHECK_CASES = [
    [
        [[3.7, 1.2, 9.5, 4.7, 6.3, 7.2, 3.8, 1.1, 1.4]],
        [[3.7, 1.2, 3.8, 1.1, 1.4], [9.5, 4.7, 6.3, 7.2]],
    ],
    [
        [[0, 3.8, 1.2, 1.9, 4.7, 5.1, 3.6, 4.4, 9.2, 7.4]],
        [[0, 3.8, 1.2, 1.9, 3.6], [4.7, 5.1, 4.4, 9.2, 7.4]],
    ],
    [
        [[9.9, 9.7, 5.6, 1.8, 4.3, 7.5, 6.6, 6.4]],
        [[5.6, 1.8, 4.3, 6.4], [9.9, 9.7, 7.5, 6.6]],
    ],
]
