TITLE = 'Ordenando por edades'

DESCRIPTION = '''
Dada una lista que representa a personas y cuyos elementos son diccionarios, se pide ordenar la lista por el campo _age_ de cada diccionario.

Notas:
- Utilice la función predefinida _sorted()_
'''

ENTRYPOINT = {
    'PARAMS': [
        ['people', list],
    ],
    'RETURN': [
        ['speople', list],
    ],
}

CHECK_CASES = [
    [
        [
            [
                {'name': 'DeRozan', 'age': 33},
                {'name': 'Lonzo', 'age': 25},
                {'name': 'Beverly', 'age': 34},
                {'name': 'Dragic', 'age': 36},
                {'name': 'Williams', 'age': 21},
            ]
        ],
        [
            [
                {'name': 'Williams', 'age': 21},
                {'name': 'Lonzo', 'age': 25},
                {'name': 'DeRozan', 'age': 33},
                {'name': 'Beverly', 'age': 34},
                {'name': 'Dragic', 'age': 36},
            ]
        ],
    ],
    [
        [
            [
                {'name': 'Brogdon', 'age': 30},
                {'name': 'Brown', 'age': 26},
                {'name': 'Gallinari', 'age': 34},
                {'name': 'Horford', 'age': 36},
                {'name': 'Hauser', 'age': 25},
            ]
        ],
        [
            [
                {'name': 'Hauser', 'age': 25},
                {'name': 'Brown', 'age': 26},
                {'name': 'Brogdon', 'age': 30},
                {'name': 'Gallinari', 'age': 34},
                {'name': 'Horford', 'age': 36},
            ]
        ],
    ],
]
