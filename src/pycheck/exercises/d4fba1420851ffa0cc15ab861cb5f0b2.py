TITLE = 'Diccionario en construcción'

DESCRIPTION = '''
Dada lista de listas con varios elementos, obtenga un diccionario donde las claves serán los primeros elementos de las sublistas y los valores serán los restantes (como listas).
'''

ENTRYPOINT = {
    'PARAMS': [
        ['items', list],
    ],
    'RETURN': [
        ['unpack_items', dict],
    ],
}

CHECK_CASES = [
    [
        [
            [
                ['Episode IV - A New Hope', 'May 25', 1977, 'George Lucas'],
                ['Episode V - The Empire Strikes Back', 'May 21', 1980],
                ['Episode VI - Return of the Jedi', 'May 25', 1983],
            ]
        ],
        [
            {
                'Episode IV - A New Hope': ['May 25', 1977, 'George Lucas'],
                'Episode V - The Empire Strikes Back': ['May 21', 1980],
                'Episode VI - Return of the Jedi': ['May 25', 1983],
            }
        ],
    ],
]
