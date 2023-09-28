TITLE = 'Interés compuesto'

DESCRIPTION = '''
Compute el capital final (_Cf_) a partir del capital inicial (_Ci_), el tipo de interés (_i_) y el número de años (_n_). Fórmula del interés compuesto:
```
                     n
C  = C  ⋅ (1 + i/100)
 f    i
```

La correspondencia con las variables del programa es la siguiente:

- _Ci_ → amount
- _i_ → rate
- _n_ → years
- _Cf_ → future_amount
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
