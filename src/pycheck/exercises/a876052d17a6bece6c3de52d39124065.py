DESCRIPTION = '''
Como datos de entrada tendrá dos listas representando las dimensiones de sendos cuboides:
   o--------o
  / c      /|
 /        / | b
o--------o  |      ---> [a, b, c]
|        |  o
|        | /
|    a   |/
o--------o

Debe calcular la diferencia de volumen entre los dos cuboides como valor positivo,
indpendientemente de qué cuboide sea mayor.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['cuboid1', list],
        ['cuboid2', list],
    ],
    'RETURN': [
        ['vol_diff', float],
    ],
}

CHECK_CASES = [
    [[[2, 2, 3], [5, 4, 1]], [8]],
    [[[3, 4, 2], [9, 1, 6]], [30]],
    [[[1, 1, 1], [1, 1, 1]], [0]],
]

SOURCE = 'https://www.codewars.com/kata/58cb43f4256836ed95000f97'
