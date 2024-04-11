TITLE = 'Redondeando con un decorador'

DESCRIPTION = """
El objetivo de este ejercicio es implementar y aplicar un **decorador con un parámetro** que permita redondear el resultado de una función a un número de cifras decimales. El decorador se llamará _cround()_ y recibirá un parámetro para el número de cifras decimales a redondear. 

La función principal "avg" debe calcular la media de los valores que se les pasa y hay que aplicarle el decorador _cround()_ explicado anteriormente con 2 cifras decimales.
"""

ENTRYPOINT = {
    'NAME': 'avg',
    'PARAMS': [
        ['values', list],
    ],
    'RETURN': [
        ['result', float],
    ],
}

CHECK_CASES = [
    [[[6, 3, 9, 3, 5, 4, 5, 7, 2, 3, 6]], [4.82]],
    [[[32, 21, 99, 56, 31, 83, 24, 68]], [51.75]],
    [[[455, 231, 956, 336, 275, 359]], [435.33]],
]
