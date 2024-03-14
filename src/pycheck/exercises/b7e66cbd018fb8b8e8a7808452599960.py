TITLE = 'Cualificando números'

DESCRIPTION = """
Dado un número entero positivo, separe las cifras de millares por comas.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['number', int],
    ],
    'RETURN': [
        ['qnumber', str],
    ],
}

CHECK_CASES = [
    [[1], ['1']],
    [[10], ['10']],
    [[100], ['100']],
    [[1000], ['1,000']],
    [[10000], ['10,000']],
    [[100000000000], ['100,000,000,000']],
]
