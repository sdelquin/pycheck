TITLE = '¿Es binario?'

DESCRIPTION = """
Compruebe si un número dado es binario o no.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['number', str],
    ],
    'RETURN': [
        ['binary', bool],
    ],
}

CHECK_CASES = [
    [['101011010111'], [True]],
    [['101101013101'], [False]],
    [['1'], [True]],
    [['0'], [True]],
    [['A'], [False]],
    [['125'], [False]],
    [['111111'], [True]],
    [['000000'], [True]],
]
