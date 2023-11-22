TITLE = 'Encontrando isogramas'

DESCRIPTION = """
Determine si una cadena de texto dada es un **isograma**, es decir, no se repite ninguna letra.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['is_isogram', bool],
    ],
}

CHECK_CASES = [
    [['lumberjacks'], [True]],
    [['background'], [True]],
    [['downstream'], [True]],
    [['six-year-old'], [True]],
    [['circus'], [False]],
    [['fantastical'], [False]],
    [['left-hand-side'], [False]],
    [['symmetrical'], [False]],
]
