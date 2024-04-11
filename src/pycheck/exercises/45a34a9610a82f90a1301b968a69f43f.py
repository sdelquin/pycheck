TITLE = 'Etiquetas equivalentes'

DESCRIPTION = """
Determina si dos etiquetas HTML dadas son equivalentes o no.

Notas:
- Una etiqueta en mayúsculas es equivalente a otra en minúsculas si contiene los mismos caracteres.
- Es obligatorio el uso de, al menos, una función auxiliar.
"""

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'PARAMS': [
        ['tag1', str],
        ['tag2', str],
    ],
    'RETURN': [
        ['equals', bool],
    ],
}

CHECK_CASES = [
    [['<img src="cat.jpg" width=30>', '<IMG src="dog.jpg">'], [True]],
    [['<div class="contents">', '<div>'], [True]],
    [['<p style="color: red">', '<table style="color: green">'], [False]],
    [['<head id="main">', '<div id="main">'], [False]],
]
