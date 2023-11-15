TITLE = 'Combinando teclas'

DESCRIPTION = """
Combinando las teclas _CTRL_ y _ALT_ podemos conseguir muchos _shortcuts_ (atajos de teclado) en sistemas tipo _Linux_.

Se pide identificar las combinaciones de teclas indicando la función que realizan.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['key1', str],
        ['key2', str],
        ['key3', str],
    ],
    'RETURN': [
        ['action', str],
    ],
}

CHECK_CASES = [
    [['CTRL', 'ALT', 'T'], ['Open terminal']],
    [['CTRL', 'ALT', 'L'], ['Lock screen']],
    [['CTRL', 'ALT', 'D'], ['Show desktop']],
    [['ALT', 'F2', ''], ['Run console']],
    [['CTRL', 'Q', ''], ['Close window']],
    [['CTRL', 'ALT', 'DEL'], ['Log out']],
]
