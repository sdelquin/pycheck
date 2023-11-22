TITLE = 'Aplicando función por comprensión'

DESCRIPTION = """
Utilizando **listas por comprensión**, cree una lista que contenga el resultado de aplicar la función _f(x) = 3x + 2_ para el rango de _x_ dado en los valores de entrada.

Ejemplo: Si xmin=0 y xmax=5, la lista de valores resultante debería ser:
[2, 5, 8, 11, 14]
"""

ENTRYPOINT = {
    'PARAMS': [
        ['xmin', int],
        ['xmax', int],
    ],
    'RETURN': [
        ['values', list],
    ],
}

CHECK_CASES = [
    [[0, 10], [[2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32]]],
    [[-7, 0], [[-19, -16, -13, -10, -7, -4, -1, 2]]],
    [[131, 134], [[395, 398, 401, 404]]],
    [[0, 1], [[2, 5]]],
]
