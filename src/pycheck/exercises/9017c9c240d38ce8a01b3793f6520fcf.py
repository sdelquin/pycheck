TITLE = 'La multiplicación de Jack'

DESCRIPTION = '''
A Jack le gusta hacer una multiplicación muy particular: Dado un número _n_ multiplica _n_ por 5 elevado al número de dígitos de _n_.

Por ejemplo:
```
n = 10 --> 10 * 5²
```
'''

ENTRYPOINT = {
    'PARAMS': [
        ['n', int],
    ],
    'RETURN': [
        ['result', int],
    ],
}

CHECK_CASES = [
    [[3], [15]],
    [[10], [250]],
    [[200], [25000]],
    [[0], [0]],
    [[-3], [-15]],
]

SOURCE = 'https://www.codewars.com/kata/5708f682c69b48047b000e07'
