TITLE = 'Un juego al tenis'

DESCRIPTION = '''
Escenario: Partido de Tenis. Dada una cadena de texto con letras A o B indicando si el jugador A ha ganado un punto o si el jugador B ha ganado un punto, haga un programa en Python que determine quién ha ganado el juego actual.

Nota: Es obvio que el jugador que ha ganado el último punto del juego también ha ganado el juego, pero nos interesa irlo calculando de forma secuencial para prepararnos de cara a ejercicios más completos.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['points', str],
    ],
    'RETURN': [
        ['winner', str],
    ],
}

CHECK_CASES = [
    [['ABAABA'], ['A']],
    [['BABABAABBB'], ['B']],
    [['AAABA'], ['A']],
    [['BBBAAAABABBAAA'], ['A']],
]
