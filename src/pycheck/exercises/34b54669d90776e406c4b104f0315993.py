TITLE = 'Convirtiendo HTML a Markdown'

DESCRIPTION = '''
Dada un fragmento de HTML que contiene una etiqueta de encabezado <h1>, <h2>, ... Se pide transformarlo a su correspondiente versión de [Markdown](https://markdown.es).
'''

ENTRYPOINT = {
    'PARAMS': [
        ['html', str],
    ],
    'RETURN': [
        ['markdown', str],
    ],
}

CHECK_CASES = [
    [['<h1>Core</h1>'], ['# Core']],
    [['<h2>Tipos de datos</h2>'], ['## Tipos de datos']],
    [['<h3>Cadenas de texto</h3>'], ['### Cadenas de texto']],
]
