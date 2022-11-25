TITLE = 'Valor máximo y mínimo'

DESCRIPTION = '''
Dada una lista de valores numéricos, encuentre el valor máximo y el valor mínimo de la misma. No se pueden utilizar las funciones "built-in" max() y min(), y tampoco sorted().
'''

ENTRYPOINT = {
    'PARAMS': [
        ['values', list],
    ],
    'RETURN': [
        ['max_value', int],
        ['min_value', int],
    ],
}

CHECK_CASES = [
    [[[4, 6, 2, 1, 9, 63, -134, 566]], [566, -134]],
    [[[-52, 56, 30, 29, -54, 0, -110]], [56, -110]],
    [[[42, 54, 65, 87, 0]], [87, 0]],
    [[[5]], [5, 5]],
]

SOURCE = 'https://www.codewars.com/kata/577a98a6ae28071780000989'
