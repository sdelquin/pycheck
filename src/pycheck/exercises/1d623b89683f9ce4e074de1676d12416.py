TITLE = 'La suma más sencilla'

DESCRIPTION = '''
Escriba un programa en Python que sume dos números enteros a y b.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['a', int],
        ['b', int],
    ],
    'RETURN': [
        ['result', int],
    ],
}

CHECK_CASES = [
    [[3, 4], [7]],
    [[1, 9], [10]],
    [[200, 55], [255]],
]
