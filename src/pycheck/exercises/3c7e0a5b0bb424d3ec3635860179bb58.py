TITLE = 'Decorando con valores absolutos'

DESCRIPTION = '''
Escriba un decorador llamado _fabs()_ que convierta a su **valor absoluto** los dos primeros parámetros de la función que decora y devuelva el resultado de aplicar dicha función a sus dos argumentos. Aplique este decorador a la función _fprod()_ que es el punto de entrada del programa.

_¿Podría extender el decorador para que tuviera en cuenta un número indeterminado de argumentos posicionales?_
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'fprod',
    'PARAMS': [
        ['a', int],
        ['b', int],
    ],
    'RETURN': [
        ['output', int],
    ],
}

CHECK_CASES = [
    [[-3, 7], [21]],
    [[-3, -9], [27]],
    [[-1, 1], [1]],
    [[0, -10], [0]],
]
