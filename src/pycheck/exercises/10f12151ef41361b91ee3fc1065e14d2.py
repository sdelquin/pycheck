TITLE = 'Números primos'

DESCRIPTION = """
Determine si un número dado es un [número primo](https://es.wikipedia.org/wiki/N%C3%BAmero_primo).
"""

ENTRYPOINT = {
    'PARAMS': [
        ['n', int],
    ],
    'RETURN': [
        ['isprime', bool],
    ],
}

CHECK_CASES = [
    [[2], [True]],
    [[3], [True]],
    [[10], [False]],
    [[11], [True]],
    [[27], [False]],
    [[31], [True]],
    [[55], [False]],
    [[67], [True]],
]
