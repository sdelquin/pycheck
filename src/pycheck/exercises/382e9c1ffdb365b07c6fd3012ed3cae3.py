DESCRIPTION = '''
El primer siglo abarca desde el año 1 hasta el año 100 (inclusive). El segundo siglo desde
el año 101 hasta el año 200 (inclusive). Y así sucesivamente.

Dado un año, calcule el siglo al que pertenece.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['year', int],
    ],
    'RETURN': [
        ['century', int],
    ],
}

CHECK_CASES = [
    [[1705], [18]],
    [[1900], [19]],
    [[1601], [17]],
    [[2000], [20]],
    [[1999], [20]],
]

SOURCE = 'https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097'
