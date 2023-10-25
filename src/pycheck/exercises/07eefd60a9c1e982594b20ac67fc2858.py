TITLE = 'Suma repetida'

DESCRIPTION = """
Dado un número entero _n_ compute el valor de _n + nn + nnn_

Notas:
- Por ejemplo, si _n=2_ hay que calcular: 2 + 22 + 222 = 246
- Contemplar únicamente _n_ en el intervalo [0,9]
"""

ENTRYPOINT = {
    'PARAMS': [
        ['n', int],
    ],
    'RETURN': [
        ['result', int],
    ],
}

CHECK_CASES = [
    [[3], [369]],
    [[4], [492]],
    [[5], [615]],
]
