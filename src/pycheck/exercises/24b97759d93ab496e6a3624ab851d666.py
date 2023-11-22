TITLE = 'Producto escalar'

DESCRIPTION = """
Dados dos vectores (listas) de la misma dimensión, utilice la función zip() para calcular su [producto escalar](https://es.wikipedia.org/wiki/Producto_escalar).

Ejemplo:

```
v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]

v1 · v2 = [4⋅9 + 3·2 + 8·7 + 1·3] = 101
```

Nota:
- Si los vectores tienen distinta dimensión habrá que devolver _None_.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['vector1', list],
        ['vector2', list],
    ],
    'RETURN': [
        ['dprod', float],
    ],
}

CHECK_CASES = [
    [[[4, 3, 8, 1], [9, 2, 7, 3]], [101]],
    [[[9, 1, 2], [8, 7, 5]], [89]],
    [[[4, 2], [8, 7, 3]], [None]],
    [[[8, 3, 5, 6, 4], [3, 7, 7, 9, 3]], [146]],
]
