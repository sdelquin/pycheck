TITLE = 'Potencia recursiva'

DESCRIPTION = '''
Escriba un programa Python que calcule _x^n_ utilizando **recursividad**. Como es obvio, no se puede utilizar el operador **
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'power',
    'PARAMS': [
        ['x', int],
        ['n', int],
    ],
    'RETURN': [
        ['result', int],
    ],
}

CHECK_CASES = [
    [[3, 4], [81]],
    [[5, 3], [125]],
    [[6, 6], [46656]],
    [[1, 0], [1]],
    [[1, 1], [1]],
    [[0, 0], [1]],
    [[0, 1], [0]],
]
