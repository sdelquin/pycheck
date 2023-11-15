TITLE = 'Todo son caritas'

DESCRIPTION = """
Dada una cadena de texto que represente una carita _emoji_ se pide que se devuelva el _emoji_ en cuestión.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['emoji_text', str],
    ],
    'RETURN': [
        ['emoji', str],
    ],
}

CHECK_CASES = [
    [['happy'], ['😀']],
    [['SAD'], ['😔']],
    [['Angry'], ['😡']],
    [['peNsive'], ['🤔']],
    [['surpriseD'], ['😮']],
]
