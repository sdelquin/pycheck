TITLE = 'Multiplicando matrices de 2x2'

DESCRIPTION = """
Escriba un programa que permita [multiplicar matrices](https://www.matricesydeterminantes.com/matrices/multiplicacion-de-matrices-2x2-y-3x3-ejemplos-y-ejercicios-resueltos-paso-a-paso/) únicamente de 2 filas por 2 columnas.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['A', list],
        ['B', list],
    ],
    'RETURN': [
        ['P', list],
    ],
}

CHECK_CASES = [
    [[[[6, 4], [8, 9]], [[3, 2], [1, 7]]], [[[22, 40], [33, 79]]]],
    [[[[2, 0], [0, 2]], [[1, 0], [0, 1]]], [[[2, 0], [0, 2]]]],
    [[[[9, 7], [3, 2]], [[8, 4], [7, 3]]], [[[121, 57], [38, 18]]]],
]
