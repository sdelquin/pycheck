TITLE = 'Descomponiendo RGB'

DESCRIPTION = """
A partir de una cadena de texto que representa un color en formato RGB (_Red_, _Green_, _Blue_) descomponga sus valores individuales devolviendo el valor entero de cada componente de color.

Notas:
- No se puede utilizar la función _split()_.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['rgb_color', str],
    ],
    'RETURN': [
        ['red', int],
        ['green', int],
        ['blue', int],
    ],
}

CHECK_CASES = [
    [['(161,49,247)'], [161, 49, 247]],
    [['(255,17,255)'], [255, 17, 255]],
    [['(18,52,86)'], [18, 52, 86]],
]
