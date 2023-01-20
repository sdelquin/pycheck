TITLE = '¿Hay stock?'

DESCRIPTION = '''
Usted es encargado de una empresa de merchandising y dispone de un cierto stock para los artículos. El cliente hace un pedido especificando el artículo y la cantidad requerida.

Usted debe comprobar si existe stock para la cantidad solicitada del artículo indicando _True_ o _False_.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['stock', dict],
        ['merch', str],
        ['amount', int],
    ],
    'RETURN': [
        ['available', bool],
    ],
}

CHECK_CASES = [
    [[{'pen': 20, 'cup': 11, 'keyring': 40}, 'cup', 9], [True]],
    [[{'pen': 20, 'cup': 11, 'keyring': 40}, 'pen', 21], [False]],
    [[{'pen': 20, 'cup': 11, 'keyring': 40}, 'keyring', 40], [True]],
]
