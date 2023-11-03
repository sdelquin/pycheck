TITLE = 'Colores en HEXA'

DESCRIPTION = """
Convierta la representación hexadecimal de un color en su versión decimal RGB.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['hex_color', str],
    ],
    'RETURN': [
        ['rgb_color', str],
    ],
}

CHECK_CASES = [
    [['A131F7'], ['(161,49,247)']],
    [['FF11FF'], ['(255,17,255)']],
    [['123456'], ['(18,52,86)']],
]
