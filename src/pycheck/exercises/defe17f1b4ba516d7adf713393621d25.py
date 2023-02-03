from pathlib import Path

TITLE = 'Buscando palabras comunes'

DESCRIPTION = '''
Dado un fichero de texto encuentre el número de palabras comunes entre cada combinación de líneas del fichero de entrada.

Por ejemplo, si una línea es "Hola me llamo Python" y otra es "Me voy a programar en Python", el resultado sería 2 porque hay dos palabras en común: "me" y "Python".

Notas:
- **La salida se debe escribir en un fichero de salida**, donde cada línea contendrá el número de palabras coincidentes para cada combinación de dos líneas del fichero de entrada.
- La búsqueda no debe diferenciar entre mayúsculas y minúsculas.
- La combinación de una línea con sí misma está contemplada.
- Se puede suponer que las palabras estarán siempre separadas por un único espacio.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['input_path', Path],
    ],
    'RETURN': [
        ['output_path', Path],
    ],
}

CHECK_CASES = [
    [['data/common_words/minizen.txt'], ['data/common_words/output.txt']],
]
