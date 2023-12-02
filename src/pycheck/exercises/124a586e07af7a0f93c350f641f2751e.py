TITLE = 'Área del anillo'

DESCRIPTION = """
Dado el valor de entrada _z_ calcule el área gris de la [siguiente figura](https://pbs.twimg.com/media/GAW3ydYXgAA9WG2?format=jpg).

Notas:
- _z_ es el valor tanto del anillo exterior como del círculo interior.
- Use _PI_ con valor 3.14.
- Obtenga el resultado redondeando a dos cifras decimales.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['z', float],
    ],
    'RETURN': [
        ['white_area', float],
    ],
}

CHECK_CASES = [
    [[6], [226.08]],
    [[7], [307.72]],
    [[8], [401.92]],
]
