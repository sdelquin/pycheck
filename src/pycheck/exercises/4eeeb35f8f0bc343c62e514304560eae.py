TITLE = 'Frecuencia de elementos consecutivos'

EMPTY_TEMPLATE = True

DESCRIPTION = '''
Escriba una función que reciba una lista de elementos y un parámetro "opcional" para el formato de salida. El objetivo es encontrar **la frecuencia de aparición de elementos consecutivos** en la lista de entrada.

Si el parámetro de salida como cadena de texto está a _False_ se deberá devolver una lista de tuplas, donde cada tupla contiene el elemento y el número de repeticiones (frecuencia). Si el parámetro de salida como cadena de texto está a _True_ se deberá devolver una cadena de texto con _elemento:frecuencia_ separados por comas.

Notas:
- Se debe obligar a que el primer parámetro (lista de elementos) sea pasado **como posicional**.
- El segundo parámetro para el formato de salida como cadena de texto debe ser _falso_ por defecto.
'''

ENTRYPOINT = {
    'NAME': 'cfreq',
    'PARAMS': [
        ['items', list],
        ['as_string', bool],
    ],
    'RETURN': [
        ['freqs', list],
    ],
}

CHECK_CASES = [
    [[[1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5], False], [[(1, 1), (2, 3), (4, 3), (5, 4)]]],
    [[[1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5], True], ['1:1,2:3,4:3,5:4']],
    [[[], False], [[]]],
    [[[], True], ['']],
    [[[0, 0, 9, 5, 5, 5, 1, 1, 1], False], [[(0, 2), (9, 1), (5, 3), (1, 3)]]],
    [[[1, 2, 3], True], ['1:1,2:1,3:1']],
]
