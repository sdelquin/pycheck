TITLE = 'Tiro porque me toca'

DESCRIPTION = '''
En este juego, la heroína se mueve de izquierda a derecha. El jugador tira el dado y se mueve dos veces el número indicado por el dado.

Dada la posición actual de la heroína y el resultado del dado (1-6) calcule la nueva posición.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['current_pos', int],
        ['dice', int],
    ],
    'RETURN': [
        ['final_pos', int],
    ],
}

CHECK_CASES = [
    [[3, 6], [15]],
    [[1, 4], [9]],
    [[5, 2], [9]],
]

SOURCE = 'https://www.codewars.com/kata/563a631f7cbbc236cf0000c2'
