TITLE = 'Contando sin contar'

DESCRIPTION = '''
Cree una función que cuente el número de veces que aparece un determinado valor en una tupla.

Notas:
- Se puede suponer que la tupla sólo contendrá valores numéricos enteros.
- No se puede utilizar la función predefinida _count()_
- Utilice anotación de tipos y valores por defecto (según corresponda).
- Documente la función siguiendo el formato [Sphinx](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html).
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'mcount',
    'PARAMS': [
        ['items', tuple],
        ['target', int],
    ],
    'RETURN': [
        ['count', int],
    ],
}

CHECK_CASES = [
    [[(1, 2, 3, 1, 1, 5, 6, 1), 1], [4]],
    [[(2, 2, 2, 2, 2), 2], [5]],
    [[(1, 2, 3, 4, 5), 0], [0]],
    [[(), 1], [0]],
]
