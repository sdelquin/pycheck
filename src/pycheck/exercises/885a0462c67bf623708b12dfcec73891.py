DESCRIPTION = '''
Una tienda de informática quiere llevar la cuenta de cuántos ordenadores y cuántos
monitores vende. Para ello lleva un registro en una lista donde cada elemento representa un
día de trabajo. A su vez, cada día de trabajo es una sublista con dos elementos: el primero
representa el número de PCs vendidos y el segundo el número de monitores vendidos.

Calcule el número total de PCs vendidos y de monitores vendidos.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['sales', list],
    ],
    'RETURN': [
        ['pcs', int],
        ['displays', int],
    ],
}

CHECK_CASES = [
    [[[[4, 5], [1, 3], [3, 2]]], [8, 10]],
    [[[[1, 0], [0, 1], [1, 1]]], [2, 2]],
    [[[[4, 5]]], [4, 5]],
    [[[]], [0, 0]],
]
