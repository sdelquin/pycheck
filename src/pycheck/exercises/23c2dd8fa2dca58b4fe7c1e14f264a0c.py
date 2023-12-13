TITLE = 'Fibonacci generador'

DESCRIPTION = """
Escriba una función generadora que devuelva cada vez el siguiente valor de la sucesión de Fibonacci.

Notas:
- La función generadora se debe construir pasando el número _n_ de valores a generar.
- La función principal debe hacer uso de la función generadora convirtiendo a lista los valores generados.
"""

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'PARAMS': [
        ['n', int],
    ],
    'RETURN': [
        ['fibo', list],
    ],
}

CHECK_CASES = [
    [[1], [[0]]],
    [[2], [[0, 1]]],
    [[10], [[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]]],
    [
        [20],
        [
            [
                0,
                1,
                1,
                2,
                3,
                5,
                8,
                13,
                21,
                34,
                55,
                89,
                144,
                233,
                377,
                610,
                987,
                1597,
                2584,
                4181,
            ]
        ],
    ],
]
