TITLE = 'Decimal a binario'

DESCRIPTION = '''
Convierta un número decimal entero a su representación binaria (como string).
'''

ENTRYPOINT = {
    'PARAMS': [
        ['num', int],
    ],
    'RETURN': [
        ['to_bin', str],
    ],
}

CHECK_CASES = [
    [[1], ['1']],
    [[11], ['1011']],
    [[42], ['101010']],
]

SOURCE = 'https://www.codewars.com/kata/59fca81a5712f9fa4700159a'
