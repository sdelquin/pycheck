TITLE = 'Nombre viceversa'

DESCRIPTION = '''
Dado un nombre, obtenga el nombre completo intercambiando nombre y apellidos.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['fullname', str],
    ],
    'RETURN': [
        ['swapname', str],
    ],
}

CHECK_CASES = [
    [['John McClane'], ['McClane John']],
    [['Charles Foster Kane'], ['Foster Kane Charles']],
    [['Terminator T-800'], ['T-800 Terminator']],
]

SOURCE = 'https://www.codewars.com/kata/559ac78160f0be07c200005a'
