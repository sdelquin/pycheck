TITLE = 'Enumerando elementos modo humano'

DESCRIPTION = """
Dada una cadena de texto con elementos separados por "dos puntos", se pide hacer un programa en Python que devuelva otra cadena enumerando los elementos como lo haría un humano.

Esto es separando los elementos por _comas_ y el último elemento por _and_.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['items', str],
    ],
    'RETURN': [
        ['enum_items', str],
    ],
}

CHECK_CASES = [
    [['apples'], ['apples']],
    [['apples:oranges'], ['apples and oranges']],
    [['apples:oranges:bananas'], ['apples, oranges and bananas']],
    [['apples:oranges:bananas:lemons'], ['apples, oranges, bananas and lemons']],
]
