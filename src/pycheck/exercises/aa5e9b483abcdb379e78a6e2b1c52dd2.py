TITLE = 'Calculadora lógica'

DESCRIPTION = '''
Dada una lista de valores booleanos y un operador lógico, calcule el resultado booleano tras aplicar el operador a la lista de valores de entrada de forma secuencial.

Tenga en cuenta que los dos únicos posibles operadores de entrada son 'and' y 'or' y que siempre van a aparecer en minúsculas.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['values', list],
        ['oper', str],
    ],
    'RETURN': [
        ['result', bool],
    ],
}

CHECK_CASES = [
    [[[True, True, False], 'and'], [False]],
    [[[True, True, False], 'or'], [True]],
    [[[True, True, True], 'and'], [True]],
    [[[False, False, False], 'and'], [False]],
]
