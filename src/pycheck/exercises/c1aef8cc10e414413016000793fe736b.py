TITLE = 'Una métrica para cadena de texto'

DESCRIPTION = '''
Calcule la siguiente métrica para una cadena de texto dada: Número total de caracteres multiplicado por número total de vocales.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['metric', int],
    ],
}

CHECK_CASES = [
    [['ordenador'], [36]],
    [['pantalla'], [24]],
    [['procesador'], [40]],
]
