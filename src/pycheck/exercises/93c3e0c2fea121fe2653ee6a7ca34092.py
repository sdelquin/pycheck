TITLE = 'Contando vocales (en recursivo)'

DESCRIPTION = '''
Diseñe una función **recursiva** en Python que calcule el número de vocales que tiene un texto de entrada.

Notas:
- Se puede asumir que el texto de entrada simpre vendrá en minúsculas.
- No hay que preocuparse por vocales con tilde. No aparecerán.
- No hay que preocuparse por la cadena vacía. No aparecerá.
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'count_vowels',
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['num_vowels', int],
    ],
}

CHECK_CASES = [
    [['Bonito es mejor que feo'], [10]],
    [['Plano es mejor que anidado'], [11]],
    [['Ahora es mejor que nunca'], [9]],
    [['La legibilidad cuenta'], [9]],
    [['Simple es mejor que complejo'], [10]],
]
