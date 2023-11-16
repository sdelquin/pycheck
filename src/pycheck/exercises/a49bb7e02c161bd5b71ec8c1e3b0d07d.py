TITLE = 'Producto cartesiano en cadenas de texto'

DESCRIPTION = """
A partir de dos cadenas de texto compute el [producto cartesiano](https://es.wikipedia.org/wiki/Producto_cartesiano) letra a letra, dando como resultado un nuevo _string_ completo.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['text1', str],
        ['text2', str],
    ],
    'RETURN': [
        ['cartesian', str],
    ],
}

CHECK_CASES = [
    [['xy', '$#'], ['x$x#y$y#']],
    [['abc', '123'], ['a1a2a3b1b2b3c1c2c3']],
    [['ho', 'ho'], ['hhhoohoo']],
    [['😀😡', '🤔😔'], ['😀🤔😀😔😡🤔😡😔']],
]
