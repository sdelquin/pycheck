TITLE = 'Ella química'

DESCRIPTION = '''
Vamos a confeccionar un reactivo. Hay 8 componentes químicos para elegir, numerados desde el 1 hasta el 8. Las reglas de elaboración son las siguientes:
- Regla 1: El componente 1 y el componente 2 no se pueden seleccionar al mismo tiempo.
- Regla 2: El componente 3 y el componente 4 no se pueden seleccionar al mismo tiempo.
- Regla 3: El componente 5 y el componente 6 tienen que seleccionarse al mismo tiempo.
- Regla 4: El componente 7 o el componente 8 tienen que seleccionarse (uno de los dos, o los dos).

Dada una lista que contiene la fórmula con dígitos del 1 al 8 representando los componentes químicos, determine si la fórmula es válida en función de las reglas establecidas y obtenga el valor booleano correspondiente.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['formula', list],
    ],
    'RETURN': [
        ['valid', bool],
    ],
}

CHECK_CASES = [
    [[[1, 3, 7]], [True]],
    [[[7, 1, 2, 3]], [False]],
    [[[1, 3, 5, 7]], [False]],
    [[[1, 5, 6, 7, 3]], [True]],
    [[[5, 6, 7]], [True]],
    [[[5, 6, 7, 8]], [True]],
    [[[6, 7, 8]], [False]],
    [[[7, 8]], [True]],
]

SOURCE = 'https://www.codewars.com/kata/59c8b38423dacc7d95000008'
