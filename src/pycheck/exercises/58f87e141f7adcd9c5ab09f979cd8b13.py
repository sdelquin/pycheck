TITLE = 'Resolviendo una operación simple'

DESCRIPTION = """
Dados dos valores numéricos de entrada así como un operador (como símbolo _string_) calcule el resultado de la operación.

NOTAS:
- Utilice la sentencia _match-case_.
- En caso de que la operación no sea suma, resta, multiplicación o división, el resultado debe ser _None_.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['num1', int],
        ['num2', int],
        ['op', str],
    ],
    'RETURN': [
        ['result', float],
    ],
}

CHECK_CASES = [
    [[5, 2, '+'], [7]],
    [[5, 2, '-'], [3]],
    [[5, 2, '*'], [10]],
    [[5, 2, '/'], [2.5]],
    [[5, 2, '&'], [None]],
]
