TITLE = 'Distancia euclídea'

DESCRIPTION = '''
Calcule la distancia euclídea entre dos puntos _(x1, y1)_ y _(x2, y2)_.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['x1', float],
        ['y1', float],
        ['x2', float],
        ['y2', float],
    ],
    'RETURN': [
        ['distance', float],
    ],
}

CHECK_CASES = [
    [[3, 5, -7, -4], [13.45362404707371]],
    [[2.1, 4.3, -2.3, 8.5], [6.082762530298219]],
    [[0.1, 0.2, -0.1, -0.2], [0.447213595499958]],
]
