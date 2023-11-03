TITLE = 'En binario claro'

DESCRIPTION = """
Obtenga la representación binaria de un número entero dado.

Notas:
- No se puede utilizar la función _strip()_.
- No se puede utilizar _f-strings_.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['number', int],
    ],
    'RETURN': [
        ['nbin', str],
    ],
}

CHECK_CASES = [
    [[233], ['11101001']],
    [[1983], ['11110111111']],
    [[120], ['1111000']],
]
