from pathlib import Path

TITLE = 'Reemplazo de caracteres'

DESCRIPTION = '''
El objetivo es reemplazar caracteres en un fichero de entrada. Los caracteres a reemplazar vienen definidos en una variable de entrada como cadena de texto, con el formato:
```
<old_char><new_char>|<old_char><new_char>|...
```
La salida debe ser otro fichero de texto con el mismo contenido que la entrada pero reemplazando los caracteres indicados.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['input_path', Path],
        ['replacements', str],
    ],
    'RETURN': [
        ['output_path', Path],
    ],
}

CHECK_CASES = [
    [
        ['data/replace_chars/noticia.txt', 'áa|ée|íi|óo|úu'],
        ['data/replace_chars/r_noticia.txt'],
    ],
]
