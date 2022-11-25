TITLE = 'Intervalo desplegado'

DESCRIPTION = '''
El objetivo de este ejercicio es simular el comportamiento de un intervalo matemático de dos números enteros.

Dada una cadena de texto que contiene una descripción del intervalo, genere una lista con todos los números incluidos en dicho intervalo.

[a,b]: Todos los números entre a y b, con a y b incluidos en el intervalo.
(a,b]: Todos los números entre a y b, sin incluir a pero incluyendo a b.
[a,b): Todos los números entre a y b, inlucyendo a pero sin incluir a b.
(a,b): Todos los números entre a y b, sin incluir a ni b.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['interval', str],
    ],
    'RETURN': [
        ['irange', list],
    ],
}

CHECK_CASES = [
    [['[3,10]'], [[3, 4, 5, 6, 7, 8, 9, 10]]],
    [['(3,10]'], [[4, 5, 6, 7, 8, 9, 10]]],
    [['[3,10)'], [[3, 4, 5, 6, 7, 8, 9]]],
    [['[3,10]'], [[3, 4, 5, 6, 7, 8, 9, 10]]],
]
