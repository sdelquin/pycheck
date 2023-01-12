TITLE = 'Un set al tenis'

DESCRIPTION = '''
Escenario: Partido de Tenis. Dada una cadena de texto con letras A o B indicando si el jugador A ha ganado un punto o si el jugador B ha ganado un punto, haga un programa en Python que determine el resultado del set.

Hay que tener en cuenta una posible situación de _tie-break_ cuando ambos jugadores empatan a 6 juegos. En este caso ganará el juego quien llegue al menos a 7 puntos con distancia de al menos 2.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['points', str],
    ],
    'RETURN': [
        ['games_player1', int],
        ['games_player2', int],
    ],
}

CHECK_CASES = [
    [['AABBAABABBBABABABBBAAABBBABAABBABBAABBBABABBAAAABBBBABBBAB'], [3, 6]],
    [
        [
            'AABAABABBABAAABABBBAABABABABABABABBBBABBABAAAAABBAABAABBABBAABBAAABBBAABAAABBBBABABAABBBABB'
        ],
        [6, 7],
    ],
    [
        ['ABAABABBBAAABBAABBAABABBBABABBABABAAABBBBAAAAAABBBBABBAABBBABBAAABBAAAAAABBABAA'],
        [7, 5],
    ],
]
