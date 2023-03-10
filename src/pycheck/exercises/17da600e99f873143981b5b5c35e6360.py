TITLE = 'Identificando secuencias consecutivas de un tamaño'

DESCRIPTION = '''
Cree una función que nos informe sobre cuál es el primer número que se repite en _x_ ocasiones, o más, seguidas en una lista. Debe aceptar una lista de números enteros y el número objetivo de ocasiones a encontrar.

Notas:
- En el caso de que exista un número que cumpla con el número de repeticiones en secuencia hay que devolver dicho número, en otro caso, hay que devolver _False_.
- Resuelva el problema **utilizando recursión**.
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'consecutive_seq',
    'PARAMS': [
        ['items', list],
        ['target_count', list],
    ],
    'RETURN': [
        ['output', int],
    ],
}

CHECK_CASES = [
    [[[1, 74, 56, 56, 56, 332, 8, 8, 8], 3], [56]],
    [[[1, 10, 20, 30, 30, 30, 30, 30, 40, 50], 5], [30]],
    [[[11, 9, 20, 71, 51, 51, 2, 4, 4, 4, 4], 4], [4]],
    [[[7], 1], [7]],
    [[[77, 16, 99, 21, 1], 2], [False]],
]
