TITLE = 'Mitad fuera'

DESCRIPTION = """
Se recibe un conjunto de números enteros _A_ y se debe generar otro conjunto _B_ tal que:

- Los valores de _B_ son los que están en _A_ división entera por 2.
- Si el resultado de la división es un valor que existe en _A_ no se debe incluir en _B_.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['values', set],
    ],
    'RETURN': [
        ['half_out_values', set],
    ],
}

CHECK_CASES = [
    [[{6, 12, 4, 50, 100}], [{3, 2, 25}]],
    [[{42, 21, 14, 18, 7}], [{9, 10, 3}]],
    [[{11, 8, 37, 21, 84, 5}], [{2, 4, 10, 42, 18}]],
    [[{10, 4, 5}], [{2}]],
]
