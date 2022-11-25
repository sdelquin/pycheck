TITLE = 'El lobo acecha'

DESCRIPTION = '''
Usted es granjera y debe cuidar sus ovejas, pero existe un lobo merodeando por la zona y hay peligro de que coma alguna oveja.

La lista de entrada contiene ovejas y un lobo. Casos:
a) Si el lobo está cerca de una oveja, habrá que responder con el mensaje:
   "Cuidado oveja X, el lobo te va a comer".
b) Si el lobo está al final de la lista, habrá que responder con el mensaje:
   "No te quiero ver más por aquí, lobo"

Las posiciones hay que calcularlas empezando por el final de la lista con índice 1.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['farm', list],
    ],
    'RETURN': [
        ['msg', str],
    ],
}

CHECK_CASES = [
    [[['oveja', 'oveja', 'lobo', 'oveja']], ['Cuidado oveja 1, el lobo te va a comer']],
    [[['lobo', 'oveja', 'oveja', 'oveja']], ['Cuidado oveja 3, el lobo te va a comer']],
    [[['lobo', 'oveja']], ['Cuidado oveja 1, el lobo te va a comer']],
    [[['oveja', 'oveja', 'oveja', 'lobo']], ['No te quiero ver más por aquí, lobo']],
]

SOURCE = 'https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15'
