TITLE = 'Reimplementando range para flotantes'

DESCRIPTION = """
Escriba un programa Python que simule el comportamiento de la función "range()" pero utilizando valores flotantes.

Los datos de entrada serán:
- Valor de comienzo.
- Valor de final.
- Paso.

Notas:
- No podemos llegar nunca al valor superior. Hay que quedarse siempre por debajo. 
"""

ENTRYPOINT = {
    'PARAMS': [
        ['start', float],
        ['stop', float],
        ['step', float],
    ],
    'RETURN': [
        ['values', list],
    ],
}

CHECK_CASES = [
    [[0, 10, 1], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]],
    [[0, 2, 0.25], [[0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75]]],
    [[0, 1, 0.21], [[0, 0.21, 0.42, 0.63, 0.84]]],
    [[0, 1, 1], [[0]]],
    [[0, 0, 1], [[]]],
    [[-3.25, 0, 0.5], [[-3.25, -2.75, -2.25, -1.75, -1.25, -0.75, -0.25]]],
    [[7, 12, 4.2], [[7, 11.2]]],
]
