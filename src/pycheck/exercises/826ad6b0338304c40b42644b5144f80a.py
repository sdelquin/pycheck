TITLE = 'Números perfectos'

DESCRIPTION = '''
Escriba una función en Python que indique si un número es [perfecto](https://es.wikipedia.org/wiki/N%C3%BAmero_perfecto). _Utilice una función auxiliar que calcule los divisores propios_.
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'is_perfect',
    'PARAMS': [
        ['n', int],
    ],
    'RETURN': [
        ['perfect_n', bool],
    ],
}

CHECK_CASES = [
    [[28], [True]],
    [[496], [True]],
    [[512], [False]],
    [[1024], [False]],
    [[8128], [True]],
]
