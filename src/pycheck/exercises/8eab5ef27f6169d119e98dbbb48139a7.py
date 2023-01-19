TITLE = 'Mezclando diccionarios'

DESCRIPTION = '''
Dados dos diccionarios de entrada, escriba un programa en Python que mezcle ambos diccionarios en uno único de salida, **sin usar métodos de mezcla definidos en Python** como:
```
{**a, **b}
a.update(b)
```
'''

ENTRYPOINT = {
    'PARAMS': [
        ['d1', dict],
        ['d2', dict],
    ],
    'RETURN': [
        ['merged', dict],
    ],
}

CHECK_CASES = [
    [[{'a': 1, 'b': 2}, {'a': 3, 'c': 4}], [{'a': 3, 'b': 2, 'c': 4}]],
    [[{0: 1, 1: 0}, {0: 0, 1: 1}], [{0: 0, 1: 1}]],
    [[{}, {'x': 2.1, 'y': 3.4}], [{'x': 2.1, 'y': 3.4}]],
    [[{}, {}], [{}]],
]
