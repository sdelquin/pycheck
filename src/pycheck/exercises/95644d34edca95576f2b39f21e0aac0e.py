DESCRIPTION = '''
Como datos de entrada dispone de dos listas con valores numéricos que ya vienen ordenadas.
Obtenga una lista de salida con la mezcla de las dos listas de entrada de forma ordenada.

NOTAS:
- No se puede utilizar la función sorted().
- No hay que realizar ninguna validación en los datos de entrada.
- Las listas de entrada pueden tener elementos repetidos.
- Las listas de entrada pueden tener distinto tamaño.
- Las listas de entrada pueden tener elementos comunes. Elimine los duplicados en la lista
de salida.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['values1', list],
        ['values2', list],
    ],
    'RETURN': [
        ['merged', list],
    ],
}

CHECK_CASES = [
    [[[1, 2, 3, 4], [1, 1, 2, 3, 4, 5]], [[1, 2, 3, 4, 5]]],
    [[[1, 11], [1, 2, 10]], [[1, 2, 10, 11]]],
    [[[20, 30], [40, 50]], [[20, 30, 40, 50]]],
    [[[0, 0], [1, 1]], [[0, 1]]],
    [[[], []], [[]]],
]

SOURCE = 'https://www.codewars.com/kata/5899642f6e1b25935d000161'
