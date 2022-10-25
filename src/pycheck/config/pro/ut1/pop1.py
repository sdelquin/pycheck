ej1 = {
    'arg_casts': [int, int],
    'cases': [
        [[5, 7], 68.08392021690038],
        [[6, 2], 36.53589838486224],
        [[21, 4], 447.83484861008833],
    ],
}

ej2 = {
    'arg_casts': [int],
    'cases': [
        [[99], 4],
        [[201], 4],
        [[3219], 6],
    ],
}

ej3 = {
    'arg_casts': [str, int, str],
    'cases': [
        [['e', 2, 'diferencia'], 'diforoncia'],
        [['u', -2, 'uruguay'], 'irigiay'],
        [['a', 4, 'anatolia'], 'unutoliu'],
    ],
}

ej4 = {
    'arg_casts': [str],
    'cases': [
        [['A131F7'], '(161,49,247)'],
        [['FF11FF'], '(255,17,255)'],
        [['123456'], '(18,52,86)'],
    ],
}

ej5 = {
    'arg_casts': [str],
    'cases': [
        [['hola probando'], 'hola-probando'],
        [['áéíóú'], 'aeiou'],
        [['TWIST & SHOUT'], 'twist-&-shout'],
    ],
}
