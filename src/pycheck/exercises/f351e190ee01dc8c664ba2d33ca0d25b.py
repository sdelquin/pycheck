TITLE = 'Suma de cuadrados'

EMPTY_TEMPLATE = True

DESCRIPTION = '''
Escriba una función en Python que reproduzca lo siguiente:
```
           2    2
f(x, y) = x  + y 
```
'''

ENTRYPOINT = {
    'NAME': 'f',
    'PARAMS': [
        ['x', int],
        ['y', int],
    ],
    'RETURN': [
        ['result', int],
    ],
}

CHECK_CASES = [
    [[3, 4], [25]],
    [[-5, -7], [74]],
    [[-2, 8], [68]],
]
