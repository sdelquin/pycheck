DESCRIPTION = '''
Calcule el área del cuadrado rojo dada la longitud del arco A.
Use PI con 2 cifras decimales.

Círculo rojo: https://i.imgur.com/nJrae8n.png
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
    [[1], [0.40569597143900354]],
    [[0.25], [0.02535599821493772]],
    [[9.99], [40.488498519209706]],
]

SOURCE = 'https://www.codewars.com/kata/5748838ce2fab90b86001b1a'
