DESCRIPTION = '''
Calcule el área de un triángulo a partir de su base y su altura.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['base', float],
        ['height', float],
    ],
    'RETURN': [
        ['area', float],
    ],
}

CHECK_CASES = [
    [[3, 3], [4.5]],
    [[1, 100], [50.0]],
    [[9.99, 3.11], [15.53445]],
]
