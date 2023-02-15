TITLE = 'Número en intervalo'

DESCRIPTION = '''
Escriba una función en Python que indique si un número está en un determinado intervalo.

Notas:
- Los límites deben tenerse en cuenta como parte del intervalo.
- El número debe ser obligatoriamente un **parámetro posicional**.
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'in_range',
    'PARAMS': [
        ['value', int],
        ['lower_limit', int],
        ['upper_limit', int],
    ],
    'RETURN': [
        ['inside', bool],
    ],
}

CHECK_CASES = [
    [[3, 2, 5], [True]],
    [[10, 10, 10], [True]],
    [[-1, -10, 10], [True]],
    [[5, 0, 1], [False]],
]
