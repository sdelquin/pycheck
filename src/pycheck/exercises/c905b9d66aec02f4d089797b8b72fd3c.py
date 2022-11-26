TITLE = '¿Qué es lo siguiente?'

DESCRIPTION = '''
Dada una lista de elementos y un elemento de dicha lista, devuelva **el elemento que sigue al elemento dado**. Si el elemento aparece más de una vez en la lista de entrada, devuelva el elemento después de la primera ocurrencia.

Cuando el elemento dado *no esté presente* en la lista o *no haya ninguno a continuación*, debería devolver None.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['items', list],
        ['ref_item', object],
    ],
    'RETURN': [
        ['target_item', object],
    ],
}

CHECK_CASES = [
    [[[1, 2, 3, 4, 5, 6, 7], 3], [4]],
    [[['Ana', 'Sara', 'Noelia'], 'Sara'], ['Noelia']],
    [[[3.21, 9.54, 6.32, 9.99], 6.32], [9.99]],
    [[[1, 2, 3], 4], [None]],
    [[[1, 2, 3], 3], [None]],
]

SOURCE = 'https://www.codewars.com/kata/542ebbdb494db239f8000046'
