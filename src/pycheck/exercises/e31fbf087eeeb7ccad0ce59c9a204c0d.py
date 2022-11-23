DESCRIPTION = '''
Hay columnas cerca de la carretera. La distancia entre las columnas es la misma y el ancho
de las columnas también es el mismo.

Se aceptan tres parámetros de entrada:
- Número de columnas.
- Distancia entre columnas (en metros).
- Ancho de la columna (centímetros).

Calcule la distancia (en centímetros) entre la primera y la última columna (quitando el
ancho de la primera y la última columna).
'''

ENTRYPOINT = {
    'PARAMS': [
        ['num_pillars', int],
        ['gap_pillars', float],
        ['pillar_width', float],
    ],
    'RETURN': [
        ['inter_distance', float],
    ],
}

CHECK_CASES = [
    [[10, 5, 30], [4740.0]],
    [[2, 1.5, 50], [150.0]],
    [[5, 2.25, 75], [1125.0]],
]
