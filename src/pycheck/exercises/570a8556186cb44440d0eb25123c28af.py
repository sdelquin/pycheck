TITLE = 'Todo en alfabético'

DESCRIPTION = """
Escriba un programa en Python que acepte una cadena de texto e indique si todos sus caracteres son alfabéticos.

NOTAS:
- No usar la función _isalpha()_
- Usar una constante: ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
"""

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['isalpha', bool],
    ],
}

CHECK_CASES = [
    [['hello-world'], [False]],
    [['Computer'], [True]],
    [['first_in_first_out'], [False]],
    [['Development'], [True]],
    [['Programming is fun!'], [False]],
]
