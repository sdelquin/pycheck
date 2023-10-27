TITLE = 'En las bases del ADN'

DESCRIPTION = '''
Dada una secuencia de ADN calcule el porcentaje de presencia de cada base (sobre el total). 

Existen cuatro posibles bases:
- ADENINA (A)
- GUANINA (G)
- TIMINA (T)
- CITOSINA (C)
'''

ENTRYPOINT = {
    'PARAMS': [
        ['dna', str],
    ],
    'RETURN': [
        ['adenines_rate', float],
        ['guanines_rate', float],
        ['thymines_rate', float],
        ['cytosines_rate', float],
    ],
}

CHECK_CASES = [
    [['GGTTACCAACCCAGTCGAAAATTTGGTCAGGG'], (28.125, 28.125, 21.875, 21.875)],
    [['ATGGGATCCTAGCCCCTTAG'], (20.0, 25.0, 25.0, 30.0)],
    [['GGATTCTGAGAATCCGCTAATGCC'], (25.0, 25.0, 25.0, 25.0)],
]
