TITLE = 'Agrupando palabras'

DESCRIPTION = '''
Dada una lista de palabras, agrúpelas por su letra inicial a través de un _diccionario de listas_.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['words', list],
    ],
    'RETURN': [
        ['group_words', dict],
    ],
}

CHECK_CASES = [
    [
        [
            [
                'mesa',
                'móvil',
                'barco',
                'coche',
                'avión',
                'bandeja',
                'casa',
                'monitor',
                'carretera',
                'arco',
            ]
        ],
        [
            {
                'm': ['mesa', 'móvil', 'monitor'],
                'b': ['barco', 'bandeja'],
                'c': ['coche', 'casa', 'carretera'],
                'a': ['avión', 'arco'],
            }
        ],
    ],
]
