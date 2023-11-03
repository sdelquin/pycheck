TITLE = 'Apellido en mayúsculas, suma uno'

DESCRIPTION = """
Dado un nombre completo de persona en formato _apellido,nombre_ se pide calcular una **métrica** del siguiente modo:
- Si el apellido está en mayúsculas, se devolverá la longitud del nombre + 1.
- Si el apellido no está en mayúsculas, se devolverá la longitud del nombre.

Notas:
- No se podrá utilizar la función _split()_
"""

ENTRYPOINT = {
    'PARAMS': [
        ['fullname', str],
    ],
    'RETURN': [
        ['fmetric', int],
    ],
}

CHECK_CASES = [
    [['Kernighan,Brian'], [5]],
    [['RITCHIE,Dennis'], [7]],
    [['van Rossum,Guido'], [5]],
]
