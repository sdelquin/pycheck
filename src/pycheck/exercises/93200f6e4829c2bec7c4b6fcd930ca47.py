TITLE = 'Primer elemento repetido n-veces'

DESCRIPTION = """
Dada una lista de números enteros positivos se pide encontrar el primer número que se repite "n" veces, donde "n" también es un valor de entrada al programa.

Notas:
- Si no hay ningún número que cumpla esta condición se debe devolver -1.
- No se puede utilizar la función _count()_.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['numbers', list],
        ['nrep', int],
    ],
    'RETURN': [
        ['target_num', int],
    ],
}

CHECK_CASES = [
    [[[2, 3, 5, 3, 2, 1, 8, 2], 3], [2]],
    [[[1, 2, 3], 2], [-1]],
    [[[], 5], [-1]],
    [[[1, 1, 1, 5, 2, 5, 5], 3], [1]],
    [[[3, 9, 2, 7, 2, 9, 1, 9, 9], 4], [9]],
    [[[7, 7, 3, 3, 2, 2, 7, 2, 3, 7, 3, 7, 7, 1], 6], [7]],
]
