TITLE = 'Contando letras y dígitos'

DESCRIPTION = """
Dada una cadena de texto, calcule el número de letras y dígitos que contiene.

Notas:
- No se puede utilizar la función _count()_
- No hay que preocuparse por letras con tilde.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['num_letters', int],
        ['num_digits', int],
    ],
}

CHECK_CASES = [
    [['pycheck 1.2.35'], [7, 4]],
    [['Michael Jordan: 23'], [13, 2]],
    [['Estrella Polar'], [13, 0]],
    [['25/05/1977'], [0, 8]],
]
