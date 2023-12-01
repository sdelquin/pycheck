TITLE = 'Encontrando el primer y el último dígito'

DESCRIPTION = """
Determine el primer y el último dígito de una cadena de texto dada.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['first_digit', int],
        ['last_digit', int],
    ],
}

CHECK_CASES = [
    [['1abc2'], [1, 2]],
    [['pqr3stu8vwx'], [3, 8]],
    [['a1b2c3d4e5f'], [1, 5]],
    [['treb7uchet'], [7, 7]],
]
