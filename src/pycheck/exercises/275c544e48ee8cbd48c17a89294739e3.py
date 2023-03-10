TITLE = 'Intercambiando tu nombre'

DESCRIPTION = '''
Escriba un programa en Python que acepte el nombre y los apellidos de una persona y los devuelva en orden inverso separados por una coma. Utilice _f-strings_ para implementarlo.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['name', str],
        ['surname', str],
    ],
    'RETURN': [
        ['fullname', str],
    ],
}

CHECK_CASES = [
    [['Sergio', 'Delgado Quintero'], ['Delgado Quintero, Sergio']],
    [['Grace', 'Hopper'], ['Hopper, Grace']],
    [['Guido', 'Van Rossum'], ['Van Rossum, Guido']],
]
