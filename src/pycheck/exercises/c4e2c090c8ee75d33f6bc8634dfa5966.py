TITLE = 'Encontrando repetición de vocales'

DESCRIPTION = """
Dada una cadena de texto indique cuántas vocales se repiten de manera consecutiva al principio de la misma.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['nrep', int],
    ],
}

CHECK_CASES = [
    [['aaaantequera'], [4]],
    [['aeropuerto'], [2]],
    [['IiInteligencia'], [3]],
    [['Oouuuhhh'], [5]],
]
