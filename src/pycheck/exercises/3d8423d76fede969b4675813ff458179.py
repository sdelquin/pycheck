TITLE = 'Suma recortada'

DESCRIPTION = '''
Dada una lista de valores numéricos, calcule la suma de todos sus elementos sin tener en cuenta el valor máximo y el valor mínimo.

NOTAS:
- Pueden haber varios valores máximos o varios valores mínimos (repeticiones).
- Puede venir la lista vacía como entrada.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['values', list],
    ],
    'RETURN': [
        ['tsum', int],
    ],
}

CHECK_CASES = [
    [[[6, 2, 1, 8, 10]], [16]],
    [[[1, 1, 11, 2, 3]], [5]],
    [[[1]], [0]],
    [[[1, 1]], [0]],
    [[[1, 2]], [0]],
    [[[]], [0]],
]

SOURCE = 'https://www.codewars.com/kata/576b93db1129fcf2200001e6'
