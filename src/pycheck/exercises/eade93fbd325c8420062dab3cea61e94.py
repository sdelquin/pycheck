DESCRIPTION = '''
Dada una lista de valores numéricos enteros, obtenga el resultado de multiplicar
todos los valores en orden.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['numbers', list],
    ],
    'RETURN': [
        ['rmult', int],
    ],
}

CHECK_CASES = [
    [[[1, 2, 3, 4]], [24]],
    [[[101, 102, 103, 104]], [110355024]],
    [[[]], [1]],
    [[[1]], [1]],
]

SOURCE = 'https://www.codewars.com/kata/57f780909f7e8e3183000078'
