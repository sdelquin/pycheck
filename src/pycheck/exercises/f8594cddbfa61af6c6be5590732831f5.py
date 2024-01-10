TITLE = 'Población promedio'

DESCRIPTION = """
Partiendo de un diccionario de ciudades (_claves_) y poblaciones (_valores_) -suponiendo que estas ciudades son las únicas que existen en el planeta- calcule el porcentaje de población relativo de cada una de ellas con respecto al total, dando como salida un diccionario.

Obtenga la media de población con una precisión de **3 decimales**.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['pdata', dict],
    ],
    'RETURN': [
        ['avg_data', dict],
    ],
}

CHECK_CASES = [
    [
        [{'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000}],
        [{'Tokyo': 34.536, 'Delhi': 23.954, 'Shanghai': 22.171, 'Mumbai': 19.339}],
    ],
    [
        [
            {
                'Adeje': 49270,
                'La Orotava': 42434,
                'Los Silos': 4644,
                'Santa Úrsula': 15361,
                'Tegueste': 11359,
            }
        ],
        [
            {
                'Adeje': 40.035,
                'La Orotava': 34.48,
                'Los Silos': 3.774,
                'Santa Úrsula': 12.482,
                'Tegueste': 9.23,
            }
        ],
    ],
    [
        [
            {
                'Agaete': 5633,
                'Gáldar': 24567,
                'Telde': 102472,
            }
        ],
        [
            {
                'Agaete': 4.246,
                'Gáldar': 18.517,
                'Telde': 77.237,
            }
        ],
    ],
]
