TITLE = 'Años bisiestos'

DESCRIPTION = '''
Dada una variable `year` con un valor entero, compruebe si dicho año es **bisiesto** o no lo es.

Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre 100, o bien si es divisible entre 400. Puede hacer la comprobación en [esta lista de años bisiestos](https://es.wikipedia.org/wiki/Anexo:A%C3%B1os_bisiestos_en_los_siglos_XX,_XXI_y_XXII).
'''

ENTRYPOINT = {
    'PARAMS': [
        ['year', int],
    ],
    'RETURN': [
        ['is_leap_year', bool],
    ],
}

CHECK_CASES = [
    [[1900], [False]],
    [[1904], [True]],
    [[1983], [False]],
    [[1992], [True]],
    [[2000], [True]],
    [[2002], [False]],
    [[2052], [True]],
    [[2100], [False]],
]
