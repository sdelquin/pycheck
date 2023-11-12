TITLE = 'Contando vocales'

DESCRIPTION = """
Dada una cadena de texto, indique el número de vocales que tiene.

NOTA:
- No se puede utilizar la función _count()_
"""

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['num_vowels', int],
    ],
}

CHECK_CASES = [
    [['El camión chocó contra el árbol'], [11]],
    [['WELCOME HOME'], [5]],
    [['Órbita Laica'], [5]],
    [['Programar va de pensar, no de escribir'], [12]],
    [['Simple es mejor que complejo'], [9]],
]
