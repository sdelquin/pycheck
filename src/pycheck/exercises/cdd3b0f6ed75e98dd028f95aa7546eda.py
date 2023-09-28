TITLE = 'El cuadrado rojo'

DESCRIPTION = '''
Calcule el área del cuadrado rojo dada la longitud del arco _A_. Use _PI_ con 2 cifras decimales.

IMPORTANTE: Redondee el resultado a 10 cifras decimales.

[Imagen del cuadrado rojo](https://i.imgur.com/nJrae8n.png)
'''

ENTRYPOINT = {
    'PARAMS': [
        ['arc_A', float],
    ],
    'RETURN': [
        ['area', float],
    ],
}

CHECK_CASES = [
    [[1], [0.4056959714]],
    [[0.25], [0.0253559982]],
    [[9.99], [40.4884985192]],
]

SOURCE = 'https://www.codewars.com/kata/5748838ce2fab90b86001b1a'
