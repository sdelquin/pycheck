from pathlib import Path

TITLE = 'De texto a Markdown'

DESCRIPTION = '''
Partiendo de un fichero de texto que representa un guión de un informe con sus epígrafes, obtenga el fichero [markdown](https://markdown.es/sintaxis-markdown/) equivalente. Habrá que tener en cuenta que los tabuladores indican el nivel de profundidad de cada título.

Notas:
- Se puede suponer que no habrá otros tabuladores distintos a los de comienzo de línea.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['text_path', Path],
    ],
    'RETURN': [
        ['md_path', Path],
    ],
}

CHECK_CASES = [
    [['data/txt2md/outline.txt'], ['data/txt2md/outline.md']],
]
