TITLE = 'Una sencilla función'

DESCRIPTION = """
Escriba un programa en Python que partiendo de dos valores enteros _a_ y _b_ calcule el resultado de la siguiente expresión:

```
     2    2     _____
F = a  + b  - ╲╱a ⋅ b
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
        ['F', float],
    ],
}

CHECK_CASES = [
    [[5, 7], [68.0839202]],
    [[6, 2], [36.5358984]],
    [[21, 4], [447.8348486]],
]
