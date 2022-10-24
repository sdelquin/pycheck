CONFIG = {
    'ut1-pop0-ej1': {
        'arg_casts': [int],
        'cases': [
            [[31256], (8, 40, 56)],
            [[3601], (1, 0, 1)],
            [[9099], (2, 31, 39)],
        ],
    },
    'ut1-pop0-ej2': {
        'arg_casts': [str],
        'cases': [
            [['GGTTACCAACCCAGTCGAAAATTTGGTCAGGG'], (28.125, 28.125, 21.875, 21.875)],
            [['ATGGGATCCTAGCCCCTTAG'], (20.0, 25.0, 25.0, 30.0)],
            [['GGATTCTGAGAATCCGCTAATGCC'], (25.0, 25.0, 25.0, 25.0)],
        ],
    },
    'ut1-pop1-ej1': {
        'arg_casts': [int, int],
        'cases': [
            [[5, 7], 68.08392021690038],
            [[6, 2], 36.53589838486224],
            [[21, 4], 447.83484861008833],
        ],
    },
    'ut1-pop1-ej2': {
        'arg_casts': [int],
        'cases': [
            [[99], 4],
            [[201], 4],
            [[3219], 6],
        ],
    },
    'ut1-pop1-ej3': {
        'arg_casts': [str, int, str],
        'cases': [
            [['e', 2, 'diferencia'], 'diforoncia'],
            [['u', -2, 'uruguay'], 'irigiay'],
            [['a', 4, 'anatolia'], 'unutoliu'],
        ],
    },
    'ut1-pop1-ej4': {
        'arg_casts': [str],
        'cases': [
            [['A131F7'], '(161,49,247)'],
            [['FF11FF'], '(255,17,255)'],
            [['123456'], '(18,52,86)'],
        ],
    },
    'ut1-pop1-ej5': {
        'arg_casts': [str],
        'cases': [
            [['hola probando'], 'hola-probando'],
            [['áéíóú'], 'aeiou'],
            [['TWIST & SHOUT'], 'twist-&-shout'],
        ],
    },
}
