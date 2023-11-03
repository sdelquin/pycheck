TITLE = 'Desplazando la vocal'

DESCRIPTION = """
El objetivo es desplazar una determinada vocal sobre un texto dado.

NOTAS:
- El desplazamiento (_offset_) es un número entero positivo o negativo.
- Este _offset_ indica las posiciones que hay que "desplazar" una vocal. Por ejemplo si el desplazamiento es 2 sobre la vocal "a" nos tendremos que ir a la vocal "i" (a-e-i).
- No hay que preocuparse de _offsets_ demasiado grandes o demasiado pequeños. Esto no va a ocurrir.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['target_vowel', str],
        ['target_offset', int],
        ['input_text', str],
    ],
    'RETURN': [
        ['output_text', str],
    ],
}

CHECK_CASES = [
    [['e', 2, 'diferencia'], ['diforoncia']],
    [['u', -2, 'uruguay'], ['irigiay']],
    [['a', 4, 'anatolia'], ['unutoliu']],
    [['e', 1, 'bereber'], ['biribir']],
]
