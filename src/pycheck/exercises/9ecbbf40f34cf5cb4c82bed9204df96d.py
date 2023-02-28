TITLE = 'Aquí tiene su vuelta'

DESCRIPTION = '''
Un cliente compra un artículo en una tienda con dinero suficiente (mayor o igual) que el importe del artículo. Por lo tanto hay que devolver el cambio. La tienda dispone de una serie concreta de monedas/billetes. El objetivo del ejercicio es devolver el cambio al cliente empezando por la moneda/billete más grande y llegando hasta la más pequeña.

Notas:
- Si el dinero es justo hay que devolver un diccionario vacío.
- Si el cambio no es posible hay que devolver _None_
'''

ENTRYPOINT = {
    'PARAMS': [
        ['to_give_back', float],
        ['available_currencies', list],
    ],
    'RETURN': [
        ['money_back', dict],
    ],
}

CHECK_CASES = [
    [[20, [5, 2, 1]], [{5: 4}]],
    [[7, [2, 1, 0.5]], [{2: 3, 1: 1}]],
    [[13.50, [5, 2, 0.5]], [{5: 2, 2: 1, 0.5: 3}]],
    [[11, [0.10, 0.5, 2]], [{2: 5, 0.5: 2.0}]],
    [[0, [0.5, 0.20, 0.10]], [{}]],
    [[4.75, [1, 5, 0.20]], [None]],
]
