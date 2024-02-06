TITLE = 'Primer elemento duplicado'

DESCRIPTION = """
Dada una lista de números enteros positivos se pide encontrar el primer número duplicado.

Notas:
- Si no hay ningún número que cumpla esta condición se debe devolver -1.
- No se puede utilizar la función _count()_.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['numbers', list],
    ],
    'RETURN': [
        ['fdup', int],
    ],
}

CHECK_CASES = [
    [[[2, 3, 5, 3, 2]], [3]],
    [[[1, 2, 3]], [-1]],
    [[[]], [-1]],
    [[[1, 1, 1, 5, 2, 5, 5]], [1]],
    [[[3, 7, 2, 9, 1, 9, 9]], [9]],
]
