TITLE = 'Aquí tiene su vuelta (max)'

DESCRIPTION = '''
Un cliente compra un artículo en una tienda con dinero suficiente (mayor o igual) que el importe del artículo. Por lo tanto hay que devolver el cambio. La tienda dispone de una serie concreta de monedas/billetes **con un máximo de unidades de cada moneda/billete**. El objetivo del ejercicio es devolver el cambio al cliente empezando por la moneda/billete más grande y llegando hasta la más pequeña.

Notas:
- Si el dinero es justo hay que devolver un diccionario vacío.
- Si el cambio no es posible hay que devolver _None_
'''

ENTRYPOINT = {
    'PARAMS': [
        ['to_give_back', float],
        ['available_currencies', dict],
    ],
    'RETURN': [
        ['money_back', dict],
    ],
}

CHECK_CASES = [
    [[20, {5: 3, 2: 7, 1: 3}], [{5: 3, 2: 2, 1: 1}]],
    [[7, {2: 1, 1: 3, 0.5: 10}], [{2: 1, 1: 3, 0.5: 4}]],
    [[13.50, {5: 20, 2: 1, 0.5: 7}], [{5: 2, 2: 1, 0.5: 3}]],
    [[11, {0.10: 2, 0.5: 10, 2: 7}], [{2: 5, 0.5: 2.0}]],
    [[0, {0.5: 5, 0.20: 5, 0.10: 5}], [{}]],
    [[4.75, {1: 5, 5: 5, 0.20: 5}], [None]],
    [[10, {5: 1, 2: 10}], [None]],
]
