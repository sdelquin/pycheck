TITLE = 'Aproximando el seno'

DESCRIPTION = '''
Existe una aproximación al seno de un ángulo x expresado en grados:

```
             4x(180 - x)
sin(x) ≈ ──────────────────
         40500 - x(180 - x)
```

Calcule dicha aproximación utilizando operaciones en Python. Descomponga la expresión en subcálculos almacenados en variables. Tenga en cuenta aquellas expresiones comunes para no repetir cálculos y seguir el principio [DRY](https://es.wikipedia.org/wiki/No_te_repitas).

¿Qué tal funciona la aproximación? Compare sus resultados con los "verdaderos":
- sin(90) = 1.0
- sin(45) = 0.7071067811865475
- sin(50) = 0.766044443118978
'''

ENTRYPOINT = {
    'PARAMS': [
        ['x', float],
    ],
    'RETURN': [
        ['sin', float],
    ],
}

CHECK_CASES = [
    [[90], [1.0]],
    [[45], [0.7058823529411765]],
    [[50], [0.7647058823529411]],
]
