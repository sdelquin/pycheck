TITLE = 'Una sencilla función'

DESCRIPTION = """
Escriba un programa en Python que partiendo de dos valores enteros _a_ y _b_ calcule el resultado de la siguiente expresión:

```
             ___  
      -a ⋅ ╲╱|b|  
G = ──────────────
         2     ___
    b ⋅ a  ⋅ ╲╱|a|
```

NOTA:
- Obtenga el resultado redondeando a 7 decimales.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['a', int],
        ['b', int],
    ],
    'RETURN': [
        ['G', float],
    ],
}

CHECK_CASES = [
    [[-5, 7], [0.0338062]],
    [[6, -2], [0.0481125]],
    [[-21, 4], [0.0051957]],
]
