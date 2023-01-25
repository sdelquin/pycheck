from pathlib import Path

TITLE = 'Contando como wc'

DESCRIPTION = '''
"wc" es una utilidad super conocida en sistemas Linux. Nos permite contar el número de líneas, palabras y bytes que hay en un fichero.

Escriba un programa en Python que simule el mismo comportamiento, recibiendo una ruta a un fichero y devolviendo esas tres variables.

Notas:
- El número de bytes que ocupa un string "s" se puede calcular con: len(s.encode('utf-8'))
- Ojo con las líneas en blanco, pueden llevarle a un resultado incorrecto.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['input_path', Path],
    ],
    'RETURN': [
        ['num_lines', int],
        ['num_words', int],
        ['num_bytes', int],
    ],
}

CHECK_CASES = [
    [['data/wc/lorem.txt'], [7, 232, 1470]],
    [['data/wc/emojis.txt'], [1, 5, 26]],
]
