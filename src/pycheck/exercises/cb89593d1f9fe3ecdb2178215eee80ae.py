TITLE = 'Calculando el factorial de un número'

EMPTY_TEMPLATE = True

DESCRIPTION = '''
Escriba una función que calcule el [factorial](https://es.wikipedia.org/wiki/Factorial) de un número _n_. El factorial de un número _n_ se define como:
```
n! = n · (n - 1) · (n - 2) · ... · 1
```

Notas:
- 0! = 1
- El factorial de un número negativo no se puede calcular.
'''

ENTRYPOINT = {
    'NAME': 'factorial',
    'PARAMS': [
        ['n', int],
    ],
    'RETURN': [
        ['fact', int],
    ],
}

CHECK_CASES = [
    [[5], [120]],
    [[0], [1]],
    [[-1], [None]],
]
