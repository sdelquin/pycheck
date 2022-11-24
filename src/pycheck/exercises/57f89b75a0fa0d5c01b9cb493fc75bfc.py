DESCRIPTION = '''
Partiendo de una cadena de texto con números separados por comas, obtenga una nueva cadena
de texto donde se elimine el primer y el último número, y los elementos aparezcan separados
por espacios.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['numbers', str],
    ],
    'RETURN': [
        ['strip_numbers', str],
    ],
}

CHECK_CASES = [
    [['1,2,3'], ['2']],
    [['1,2,3,4'], ['2 3']],
    [['1,2,3,4,5'], ['2 3 4']],
    [['1,20,300,40,5'], ['20 300 40']],
    [[''], ['']],
    [['1'], ['']],
    [['1,2'], ['']],
]

SOURCE = 'https://www.codewars.com/kata/570597e258b58f6edc00230d'
