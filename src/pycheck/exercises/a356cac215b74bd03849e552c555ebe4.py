TITLE = 'Precio sin IGIC'

DESCRIPTION = '''
Calcule el precio de un artículo quitándole el IGIC indicado.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['price_with_igic', float],
        ['igic', float],
    ],
    'RETURN': [
        ['clean_price', float],
    ],
}

CHECK_CASES = [
    [[120, 7], [112.15]],
    [[50, 4.5], [47.85]],
    [[1500, 9.75], [1366.74]],
]

SOURCE = 'https://www.codewars.com/kata/5890d8bc9f0f422cf200006b'
