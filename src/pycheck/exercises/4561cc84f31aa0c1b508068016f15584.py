TITLE = 'Se pone en verde'

DESCRIPTION = """
Escribe un programa en Python que implemente la lógica de un semáforo, de tal manera que pase de verde a amarillo, de amarillo a rojo y de rojo a verde.

Notas:
- Hacer el programa utilizando los emojis 🟢 🟠 🔴
"""

ENTRYPOINT = {
    'PARAMS': [
        ['color', str],
    ],
    'RETURN': [
        ['new_color', str],
    ],
}

CHECK_CASES = [
    [['🟢'], ['🟠']],
    [['🟠'], ['🔴']],
    [['🔴'], ['🟢']],
]
