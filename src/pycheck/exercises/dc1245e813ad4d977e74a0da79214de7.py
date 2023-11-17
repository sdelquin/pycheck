TITLE = 'Left strip'

DESCRIPTION = """
Implemente el mismo comportamiento de la función **lstrip()** de Python sin utilizar ninguna variante de las funciones _strip()_ existentes en Python.

Es decir, dada una cadena de texto de entrada y otra cadena representando los caracteres a _"stripear"_ (eliminar) se debe devolver una nueva cadena de texto eliminando del principio aquellos caracteres indicados.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
        ['blacklist', str],
    ],
    'RETURN': [
        ['stext', str],
    ],
}

CHECK_CASES = [
    [['955428PAYLOAD', '0123456789'], ['PAYLOAD']],
    [['aaaioueeooPAYLOAD', 'aeiou'], ['PAYLOAD']],
    [[';::-;..PAYLOAD', ',.:;-'], ['PAYLOAD']],
]
