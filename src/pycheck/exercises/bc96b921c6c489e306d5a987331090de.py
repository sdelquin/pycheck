TITLE = 'Conversor de temperatura'

DESCRIPTION = """
La idea es crear un conversor de temperatura genérico partiendo de un texto que identifica su naturaleza. _Es obligatorio crear una función adicional como clausura_ llamada _temp_converter()_ para realizar el ejercicio.

La clausura se debe invocar (desde la función principal) de la siguiente manera:
```
converter = temp_converter(source)
result = converter(temp)
```
Notas:
- Las únicas naturalezas (source) admitidas son: _c2f_ (Celsius a Fahrenheit) y _f2c_ (Fahrenheit a Celsius).
- Puedes ver las fórmulas para pasar de una a otra [en este enlace](https://www.saberespractico.com/wp-content/uploads/2015/05/celsius-vs-fahrenheit1.jpg).
- Si llega una operación distinta a las admitidas el resultado debe ser: _None_
- Obtenga el resultado redondeando _round()_ a dos cifras decimales.
"""

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'PARAMS': [
        ['source', str],
        ['temp', float],
    ],
    'RETURN': [
        ['result', float],
    ],
}

CHECK_CASES = [
    [['c2f', 32.1], [89.78]],
    [['f2c', 79.8], [26.56]],
    [['c2f', 21.3], [70.34]],
    [['f2c', 98.4], [36.89]],
]
