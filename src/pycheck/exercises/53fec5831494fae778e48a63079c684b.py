TITLE = 'Generando cuadrados'

EMPTY_TEMPLATE = True

DESCRIPTION = '''
Escriba una función que reciba un parámetro _n_ y que incluya **una expresión generadora** para calcular los _n_ primeros números enteros elevados al cuadrado.

Notas:
- La función debe **devolver una lista** de los valores al cuadrado.
- _n_ ∈ {0, ℤ+}
'''

ENTRYPOINT = {
    'NAME': 'gen_sq',
    'PARAMS': [
        ['n', int],
    ],
    'RETURN': [
        ['squared', list],
    ],
}

CHECK_CASES = [
    [[0], [[]]],
    [[10], [[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]]],
    [[15], [[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]]],
    [
        [20],
        [
            [
                0,
                1,
                4,
                9,
                16,
                25,
                36,
                49,
                64,
                81,
                100,
                121,
                144,
                169,
                196,
                225,
                256,
                289,
                324,
                361,
            ]
        ],
    ],
]
