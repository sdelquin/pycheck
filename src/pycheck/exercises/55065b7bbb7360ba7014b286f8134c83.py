TITLE = 'Contando divisores'

DESCRIPTION = """
Escribe un programa en Python que calcule el número de divisores que tiene un número dado.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['number', int],
    ],
    'RETURN': [
        ['num_divisors', int],
    ],
}

CHECK_CASES = [
    [[67], [2]],
    [[99], [6]],
    [[1024], [11]],
]
