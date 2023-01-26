from pathlib import Path

TITLE = 'Leyendo ficheros CSV'

DESCRIPTION = '''
Dado un fichero de entrada en formato CSV, escriba un programa en Python que sea capaz de convertirlo a una lista de diccionarios.

Notas:
- Si se encuentra un "True" o un "False" habrá que convertirlo al tipo booleano de Python.
- Si se encuentra un número habrá que convertirlo a tipo numérico de Python.
- Se puede asegurar que los números que aparezcan siempre van a ser enteros.
- Se puede asegurar que los ficheros de entrada siempre tendrán el nombre de las columnas en la primera fila.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['datafile', Path],
    ],
    'RETURN': [
        ['data', list],
    ],
}

CHECK_CASES = [
    [
        ['data/read_csv/pokemon.csv'],
        [
            [
                {
                    'Name': 'Bulbasaur',
                    'Type_1': 'Grass',
                    'Type_2': 'Poison',
                    'Total': 318,
                    'HP': 45,
                    'Attack': 49,
                    'Defense': 49,
                    'Sp_Atk': 65,
                    'Sp_Def': 65,
                    'Speed': 45,
                    'Generation': 1,
                    'Legendary': False,
                },
                {
                    'Name': 'Ivysaur',
                    'Type_1': 'Grass',
                    'Type_2': 'Poison',
                    'Total': 405,
                    'HP': 60,
                    'Attack': 62,
                    'Defense': 63,
                    'Sp_Atk': 80,
                    'Sp_Def': 80,
                    'Speed': 60,
                    'Generation': 1,
                    'Legendary': False,
                },
                {
                    'Name': 'Venusaur',
                    'Type_1': 'Grass',
                    'Type_2': 'Poison',
                    'Total': 525,
                    'HP': 80,
                    'Attack': 82,
                    'Defense': 83,
                    'Sp_Atk': 100,
                    'Sp_Def': 100,
                    'Speed': 80,
                    'Generation': 1,
                    'Legendary': False,
                },
                {
                    'Name': 'Charizard',
                    'Type_1': 'Fire',
                    'Type_2': 'Flying',
                    'Total': 534,
                    'HP': 78,
                    'Attack': 84,
                    'Defense': 78,
                    'Sp_Atk': 109,
                    'Sp_Def': 85,
                    'Speed': 100,
                    'Generation': 1,
                    'Legendary': False,
                },
                {
                    'Name': 'Butterfree',
                    'Type_1': 'Bug',
                    'Type_2': 'Flying',
                    'Total': 395,
                    'HP': 60,
                    'Attack': 45,
                    'Defense': 50,
                    'Sp_Atk': 90,
                    'Sp_Def': 80,
                    'Speed': 70,
                    'Generation': 1,
                    'Legendary': False,
                },
                {
                    'Name': 'Weedle',
                    'Type_1': 'Bug',
                    'Type_2': 'Poison',
                    'Total': 195,
                    'HP': 40,
                    'Attack': 35,
                    'Defense': 30,
                    'Sp_Atk': 20,
                    'Sp_Def': 20,
                    'Speed': 50,
                    'Generation': 1,
                    'Legendary': False,
                },
                {
                    'Name': 'Kakuna',
                    'Type_1': 'Bug',
                    'Type_2': 'Poison',
                    'Total': 205,
                    'HP': 45,
                    'Attack': 25,
                    'Defense': 50,
                    'Sp_Atk': 25,
                    'Sp_Def': 25,
                    'Speed': 35,
                    'Generation': 1,
                    'Legendary': False,
                },
                {
                    'Name': 'Beedrill',
                    'Type_1': 'Bug',
                    'Type_2': 'Poison',
                    'Total': 395,
                    'HP': 65,
                    'Attack': 90,
                    'Defense': 40,
                    'Sp_Atk': 45,
                    'Sp_Def': 80,
                    'Speed': 75,
                    'Generation': 1,
                    'Legendary': False,
                },
                {
                    'Name': 'Pidgey',
                    'Type_1': 'Normal',
                    'Type_2': 'Flying',
                    'Total': 251,
                    'HP': 40,
                    'Attack': 45,
                    'Defense': 40,
                    'Sp_Atk': 35,
                    'Sp_Def': 35,
                    'Speed': 56,
                    'Generation': 1,
                    'Legendary': False,
                },
                {
                    'Name': 'Pidgeotto',
                    'Type_1': 'Normal',
                    'Type_2': 'Flying',
                    'Total': 349,
                    'HP': 63,
                    'Attack': 60,
                    'Defense': 55,
                    'Sp_Atk': 50,
                    'Sp_Def': 50,
                    'Speed': 71,
                    'Generation': 1,
                    'Legendary': False,
                },
            ]
        ],
    ],
]
