TITLE = 'N elevado a N'

DESCRIPTION = '''
Dada una lista de números enteros positivos y un número no negativo _N_, calcule el valor del elemento en la posición _N_ elevado a _N_.

Ejemplo:
[1, 2, 3, 4] y N=2, el resultado sería 3^2 = 9

Notas:
- Si _N_ está fuera de rango, hay que devolver el valor -1.
- _N_ se representa por "power" en el parámetro de entrada.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['values', list],
        ['power', int],
    ],
    'RETURN': [
        ['result', int],
    ],
}

CHECK_CASES = [
    [[[1, 2, 3, 4], 2], [9]],
    [[[1, 2, 3], 3], [-1]],
    [[[10, 20, 30, 40, 50], 4], [6250000]],
]

SOURCE = 'https://www.codewars.com/kata/57d814e4950d8489720008db'
