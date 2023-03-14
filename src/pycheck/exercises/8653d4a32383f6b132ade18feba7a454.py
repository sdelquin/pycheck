TITLE = 'Decorando la suma de valores'

DESCRIPTION = '''
En este ejercicio el dato de entrada es una lista "supuestamente" de valores enteros. Debe crear una función que sume los valores de dicha lista, pero con ciertos matices:
1. La función principal debe chequear que todos los valores de la lista sean valores enteros. Si alguno no es entero esto supone un error. Usar la función _is_instance()_ para la comprobación de tipos.
2. La función principal debe devolver dos valores (como una tupla):
    - El primero es el estado: _True_ si todo fue bien o _False_ si hubo algún error.
    - El segundo es el resultado: Si todo fue bien devolver la suma de los valores, si hubo algún error devolver la cadena "Not int value found"
3. Se debe crear una **función auxiliar (decorador)** llamada _result_as_status()_ que convierta la salida de la función principal en un diccionario con claves _status_ y _result_.
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'PARAMS': [
        ['values', list],
    ],
    'RETURN': [
        ['rstatus', dict],
    ],
}

CHECK_CASES = [
    [[[3, 4, 2]], [{'status': True, 'result': 9}]],
    [[[3, 'x', 2]], [{'status': False, 'result': 'Not int value found'}]],
]
