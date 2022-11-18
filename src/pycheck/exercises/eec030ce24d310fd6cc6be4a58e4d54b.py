DESCRIPTION = '''
Calcule el área de un círculo a partir de su radio. Tenga en cuenta:
- Usar PI con 2 cifras decimales.
- Devolver el resultado con 2 cifras decimales.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['radius', float],
    ],
    'RETURN': [
        ['area', float],
    ],
}

CHECK_CASES = [
    [[4], [50.24]],
    [[100], [31400.00]],
    [[39.8], [4973.89]],
]
