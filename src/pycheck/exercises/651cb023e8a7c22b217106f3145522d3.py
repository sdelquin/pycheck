TITLE = 'Piedra, papel o tijera'

DESCRIPTION = """
Acepte la opción de dos jugadoras en [Piedra-Papel-Tijera](https://es.wikipedia.org/wiki/Piedra,_papel_o_tijera) y decida el resultado final.

NOTAS:
- La entrada siempre vendrá en forma de _string_ con valores 'piedra', 'papel' o 'tijera', pero puede estar en mayúsculas, minúsculas o mezcla de ellas.
- La salida deberá de ser un valor numérico entero:
    - 1 si gana la primera jugadora.
    - 2 si gana la segunda jugadora.
    - 0 si hay empate.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['choice1', str],
        ['choice2', str],
    ],
    'RETURN': [
        ['winner', int],
    ],
}

CHECK_CASES = [
    [['piedra', 'PAPEL'], [2]],
    [['tijera', 'papel'], [1]],
    [['piedra', 'papel'], [2]],
    [['TIJERA', 'Piedra'], [2]],
    [['papel', 'tijera'], [2]],
    [['papel', 'papel'], [0]],
    [['tijera', 'TIJERA'], [0]],
]
