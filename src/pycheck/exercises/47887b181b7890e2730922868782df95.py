TITLE = 'Los unos cuentan en binario'

DESCRIPTION = """
Calcule el número de unos (1s) que contiene la representación binaria de un determinado número entero dado.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['number', int],
    ],
    'RETURN': [
        ['count_ones', int],
    ],
}

CHECK_CASES = [
    [[99], [4]],
    [[201], [4]],
    [[3219], [6]],
]
