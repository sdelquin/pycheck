TITLE = 'Edades cruzadas'

DESCRIPTION = """
Escribe un programa en Python que, dada la edad de una madre y su hija, calcule en qué momento de sus vidas (desde el comienzo) la edad de la madre fue o será el doble que la edad de su hija. Lo que habrá que devolver es la edad de la madre y la edad de su hija en el momento en el que la madre doble en edad a su hija.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['mother_age', int],
        ['daughter_age', int],
    ],
    'RETURN': [
        ['target_mother_age', int],
        ['target_daughter_age', int],
    ],
}

CHECK_CASES = [
    [[67, 23], [88, 44]],
    [[50, 20], [60, 30]],
    [[24, 14], [20, 10]],
]
