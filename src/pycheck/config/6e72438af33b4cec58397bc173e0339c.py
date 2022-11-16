DESCRIPTION = '''
Comprobar que pycheck funciona correctamente.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['a', int],
        ['b', int],
    ],
    'RETURN': ['result', int],
}

CHECK_CASES = [
    [[3, 4], 7],
    [[1, 9], 10],
    [[200, 55], 255],
]
