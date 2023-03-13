TITLE = 'La palabra perdida'

DESCRIPTION = '''
Dado un texto de entrada, una palabra presente en el texto y una palabra de reemplazo, obtenga el mismo texto sustituyendo la palabra presente por la palabra de reemplazo.

Notas:
- La palabra presente sólo aparecerá una única vez en el texto.
- Utilice únicamente operaciones de búsqueda, concatenación y troceado de cadenas de texto.
- No se puede utilizar la función _replace()_
'''

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
        ['target_word', str],
        ['replace_word', str],
    ],
    'RETURN': [
        ['mtext', str],
    ],
}

CHECK_CASES = [
    [
        ['This is a beautiful night on the Atlantic', 'beautiful', 'terrible'],
        ['This is a terrible night on the Atlantic'],
    ],
    [
        ['Tomorrow will be a wonderful day in the beach', 'wonderful', 'great'],
        ['Tomorrow will be a great day in the beach'],
    ],
    [
        ['Keep calm and write Python', 'write', 'enjoy'],
        ['Keep calm and enjoy Python'],
    ],
]
