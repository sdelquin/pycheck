TITLE = 'Banagrama'

DESCRIPTION = """
Un banagrama es un concepto "inventado" a partir del concepto de anagrama.

Se dice (yo digo) que una palabra _A_ es un **banagrama** de otra _B_ si todas las letras de _A_ están incluidas en _B_. El programa debe indicar si una palabra es banagrama de otra.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['word1', str],
        ['word2', str],
    ],
    'RETURN': [
        ['is_banagram', bool],
    ],
}

CHECK_CASES = [
    [['gabana', 'banagrama'], [True]],
    [['caprese', 'supermercado'], [True]],
    [['Voluta', 'AUTOMOVIL'], [True]],
    [['potaje', 'espejo'], [False]],
    [['vano', 'Ventana'], [False]],
    [['dispuesto', 'DISPOSITIVO'], [False]],
]
