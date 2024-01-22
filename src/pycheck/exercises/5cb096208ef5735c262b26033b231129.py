TITLE = "Hiperfactorial"

DESCRIPTION = """
El hiperfactorial de un número _n_ se calcula como el producto sucesivo de los decrementos de _n_ elevado a sí mismo.

Por ejemplo, el hiperfactorial de 5 se calcula como:
```
 5    4    3    2    1
5  * 4  * 3  * 2  * 1  = 86400000
```
Se pide escribir una función que calcule el hiperfactorial de un número _n_.

Notas:
- n >= 1
- Puede plantear la versión iterativa y la versión recursiva.
"""

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    "NAME": "hyperfactorial",
    "PARAMS": [
        ["n", int],
    ],
    "RETURN": [
        ["hyperfactorial", int],
    ],
}

CHECK_CASES = [
    [[1], [1]],
    [[3], [108]],
    [[5], [86400000]],
    [[7], [3319766398771200000]],
]
