TITLE = 'Producto acumulado en cuadrados'

DESCRIPTION = """
Dado un número entero calcule el producto acumulado de cada valor al cuadrado hasta llegar a dicho número.

Por ejemplo, si _n=4_ el resultado saldría del siguiente cálculo:
```
 2    2    2    2
1  ⋅ 2  ⋅ 3  ⋅ 4  = 576
```
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
    [[1], [1]],
    [[4], [576]],
    [[7], [25401600]],
    [[10], [13168189440000]],
]
