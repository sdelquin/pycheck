TITLE = 'Alfabeto circular'

DESCRIPTION = '''
Escriba una función generadora (auxiliar) que devuelva los caracteres del alfabeto de forma consecutiva y con desplazamiento circular, es decir, cuando se llegue al final del alfabeto que empiece por el principio.

La función principal debe devolver la conversión a cadena de texto de la llamada a la función generadora auxiliar.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['max_letters', int],
    ],
    'RETURN': [
        ['text', str],
    ],
}

CHECK_CASES = [
    [[0], ['']],
    [[10], ['abcdefghij']],
    [[43], ['abcdefghijklmnopqrstuvwxyzabcdefghijklmnopq']],
    [
        [99],
        [
            'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstu'
        ],
    ],
]
