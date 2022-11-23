DESCRIPTION = '''
Compute el valor futuro de una cantidad de dinero (capital final), a partir del capital
inicial, el tipo de interés y el número de años. Fórmula del interés compuesto:

                 n
C  = C  ⋅ (1 + i)
 f    i
'''

ENTRYPOINT = {
    'PARAMS': [
        ['amount', float],
        ['rate', float],
        ['years', int],
    ],
    'RETURN': [
        ['future_amount', float],
    ],
}

CHECK_CASES = [
    [[10_000, 3.5, 7], [12722.792627665729]],
    [[7_500, 0.25, 21], [7903.751377796907]],
    [[125_000, 0.045, 9], [125507.16220745872]],
]
