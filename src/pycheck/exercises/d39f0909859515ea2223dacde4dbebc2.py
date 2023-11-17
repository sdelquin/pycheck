TITLE = 'Producto recortado'

DESCRIPTION = """
Escriba un programa que reciba dos valores numéricos flotantes y calcule su producto, teniendo en cuenta que también se proporciona un mínimo _A_ y un máximo _B_.

Comportamiento:
- Si el producto está entre _A_ y _B_: dar el producto como resultado.
- Si el producto es menor que _A_: dar _A_ como resultado.
- Si el producto es mayor que _B_: dar _B_ como resultado.

Notas:
- Redondear el resultado a 2 cifras decimales.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['value1', float],
        ['value2', float],
        ['vmin', float],
        ['vmax', float],
    ],
    'RETURN': [
        ['rmul', float],
    ],
}

CHECK_CASES = [
    [[3.21, 7.44, 0, 20.51], [20.51]],
    [[4.32, 1.71, 8.02, 19.46], [8.02]],
    [[2.86, 5.09, 1.03, 15.43], [14.56]],
]
