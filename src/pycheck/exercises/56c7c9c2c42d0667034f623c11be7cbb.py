TITLE = 'Menor id sin usar'

DESCRIPTION = '''
Dada una lista de números enteros positivos representando identificadores únicos de objetos, determine cuál es el menor identificador sin usar. Puede suponer que no habrán valores repetidos en la lista de entrada.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['ids', list],
    ],
    'RETURN': [
        ['smallest_unused_id', int],
    ],
}

CHECK_CASES = [
    [[[3, 1, 8, 4, 9]], [2]],
    [[[7, 2, 12, 21, 5]], [1]],
    [[[1, 2, 3, 5, 10, 7]], [4]],
    [[[4, 3, 2, 1]], [5]],
]

SOURCE = 'https://www.codewars.com/kata/55eea63119278d571d00006a'
