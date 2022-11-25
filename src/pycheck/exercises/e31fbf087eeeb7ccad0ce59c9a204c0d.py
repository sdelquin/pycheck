TITLE = 'Postes en la carretera'

DESCRIPTION = '''
Hay postes cerca de la carretera. La distancia entre los postes es la misma y el ancho de los postes también es el mismo.

Se aceptan tres parámetros de entrada:
- Número de postes.
- Distancia entre postes (en metros).
- Ancho del poste (centímetros).

Calcule la distancia (en centímetros) entre la primera y el último poste (quitando el
ancho de la primera y el último poste).
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
