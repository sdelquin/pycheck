TITLE = 'Máximo común divisor'

DESCRIPTION = """
Encuentre el **máximo común divisor** mediante una **función recursiva**.

Utilice el _algoritmo de Euclides_ que dice así:

Si se desea encontrar el máximo común divisor entre dos números naturales _a_ y _b_, se siguen las siguientes reglas:
1. Si _b = 0_ entonces _gcd(a, b) = a_
2. En otro caso, _gcd(a, b) = gcd(b, r)_ donde _r_ es el resto de dividir _a_ entre _b_.
"""

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'gcd',
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
