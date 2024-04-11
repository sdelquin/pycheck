TITLE = 'Obteniendo los biestables'

DESCRIPTION = """
Se dice (definición propia) que un número biestable ("bistable" en inglés) es aquel que contiene el mismo número de 0s que de 1s en su representación binaria.

Dado un rango [a, b] obtenga todos los números biestables entre _a_ y _b_ (incluyendo ambos extremos). Es obligatorio el uso de una función auxiliar que diga si un número es biestable o no.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['a', int],
        ['b', int],
    ],
    'RETURN': [
        ['bistables', list],
    ],
}

CHECK_CASES = [
    [[0, 40], [[2, 9, 10, 12, 35, 37, 38]]],
    [[129, 153], [[135, 139, 141, 142, 147, 149, 150, 153]]],
    [
        [2500, 2587],
        [
            [
                2501,
                2502,
                2505,
                2506,
                2508,
                2513,
                2514,
                2516,
                2520,
                2529,
                2530,
                2532,
                2536,
                2544,
                2575,
                2583,
                2587,
            ]
        ],
    ],
]
