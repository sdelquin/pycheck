TITLE = 'Ordenando mediante decoradores'

DESCRIPTION = """
Escriba un decorador llamado _sort()_ que permita ordenar el resultado de cualquier función (siempre que devuelva un iterable) tomando un parámetro opcional que indique si la ordenación es ascendente o descendente.

Notas:
- Aplique este decorador a la función _extract_evens()_ (punto de entrada del programa) que debe extraer los números pares de un iterable de entrada. 
- Aplique este decorador indicando con su argumento _ordenación descendente_.
"""

ENTRYPOINT = {
    'NAME': 'extract_evens',
    'PARAMS': [
        ['values', list],
    ],
    'RETURN': [
        ['even_values', list],
    ],
}

CHECK_CASES = [
    [[[6, 3, 2, 9, 7, 4]], [[6, 4, 2]]],
    [[[6, 8, 10, 7, 1]], [[10, 8, 6]]],
    [[[5, 4, 3, 2, 1]], [[4, 2]]],
]
