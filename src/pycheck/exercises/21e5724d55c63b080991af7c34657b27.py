TITLE = 'Creando operaciones'

DESCRIPTION = '''
La idea es crear operaciones aritméticas básicas partiendo de un texto que identifica la operación y sus operandos. _Es obligatorio crear una función adicional como clausura_ llamada _make_oper()_ para realizar el ejercicio.

La clausura se debe invocar (desde la función principal) de la siguiente manera:
```
operation = make_oper(oper)
result = operation(num1, num2)
```
Notas:
- Las únicas operaciones admitidas son: _add_ _sub_ _mul_ _div_
- Si llega una operación distinta a las admitidas el resultado debe ser: _None_
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'PARAMS': [
        ['oper', str],
        ['num1', int],
        ['num2', int],
    ],
    'RETURN': [
        ['result', float],
    ],
}

CHECK_CASES = [
    [['add', 3, 4], [7]],
    [['sub', 3, 4], [-1]],
    [['mul', 3, 4], [12]],
    [['div', 3, 4], [0.75]],
    [['abc', 3, 4], [None]],
]
