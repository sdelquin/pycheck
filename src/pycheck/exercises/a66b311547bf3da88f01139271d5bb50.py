TITLE = 'Descifrando ciudades'

DESCRIPTION = '''
El dato de entrada a su programa es una _cadena de texto_ con el siguiente formato:
```
<city>:<population>;<city>:<population>;<city>:<population>;....
```
El objetivo es conseguir obtener un diccionario donde las claves sean las **ciudades** y los valores sean los **habitantes** (como enteros).
'''

ENTRYPOINT = {
    'PARAMS': [
        ['cinfo', str],
    ],
    'RETURN': [
        ['cities', dict],
    ],
}

CHECK_CASES = [
    [
        ['Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000'],
        [
            {
                'Tokyo': 38140000,
                'Delhi': 26454000,
                'Shanghai': 24484000,
                'Mumbai': 21357000,
            }
        ],
    ],
]
