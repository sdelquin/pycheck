TITLE = 'Intervalo desplegado'

DESCRIPTION = '''
El objetivo de este ejercicio es simular el comportamiento de un intervalo matemático con dos números enteros.

Dada una cadena de texto que contiene una descripción del intervalo, genere una lista con todos los números incluidos en dicho intervalo.

- [a,b]: Todos los números entre _a_ y _b_, con _a_ y _b_ incluidos en el intervalo.
- (a,b]: Todos los números entre _a_ y _b_, sin incluir _a_ pero incluyendo _b_.
- [a,b): Todos los números entre _a_ y _b_, incluyendo _a_ pero sin incluir _b_.
- (a,b): Todos los números entre _a_ y _b_, sin incluir _a_ ni _b_.

Tener en cuenta que los valores del intervalo pueden ser **números de varias cifras**.
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
    [['(3,10)'], [[4, 5, 6, 7, 8, 9]]],
    [['[20,24)'], [[20, 21, 22, 23]]],
    [['[101,103]'], [[101, 102, 103]]],
    [['(2001,2006)'], [[2002, 2003, 2004, 2005]]],
]
