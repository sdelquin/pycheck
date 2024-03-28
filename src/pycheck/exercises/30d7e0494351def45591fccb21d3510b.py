TITLE = 'Calculando potencias a mano'

DESCRIPTION = """
Sin utilizar el operador ** de Python ni tampoco la función _pow()_ predefinida, haz un programa que permita calcular _x elevado a n_.

Ejemplo:

```
 4                
3  = 3 ⋅ 3 ⋅ 3 ⋅ 3
```
"""

ENTRYPOINT = {
    'PARAMS': [
        ['x', int],
        ['n', int],
    ],
    'RETURN': [
        ['p', int],
    ],
}

CHECK_CASES = [
    [[3, 4], [81]],
    [[5, 9], [1953125]],
    [[7, 14], [678223072849]],
]
