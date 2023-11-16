TITLE = 'Máximo común divisor'

DESCRIPTION = """
Encuentre el **máximo común divisor** entre dos números enteros.

NOTAS:
- No es necesario utilizar ningún algoritmo existente.
- Basta con probar divisores.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['a', int],
        ['b', int],
    ],
    'RETURN': [
        ['gcd_value', int],
    ],
}

CHECK_CASES = [
    [[1, 1], [1]],
    [[3, 7], [1]],
    [[46, 64], [2]],
    [[12, 44], [4]],
    [[28, 91], [7]],
]
