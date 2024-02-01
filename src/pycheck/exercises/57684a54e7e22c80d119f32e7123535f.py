TITLE = 'Formateando a colores en hexadecimal'

DESCRIPTION = """
Los colores RGB se pueden representar por un valor hexadecimal (de 6 dígitos). Dado un valor entero se pide formtearlo como hexadecimal con un tamaño de 6 dígitos rellenando con ceros si es necesario.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['intcolor', int],
    ],
    'RETURN': [
        ['hexcolor', str],
    ],
}

CHECK_CASES = [
    [[45782], ['00B2D6']],
    [[4098423], ['3E8977']],
    [[527], ['00020F']],
    [[832923], ['0CB59B']],
]
