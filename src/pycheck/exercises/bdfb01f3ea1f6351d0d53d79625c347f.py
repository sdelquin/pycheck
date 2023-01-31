from pathlib import Path

TITLE = 'Histograma'

DESCRIPTION = '''
Un [histograma](https://es.wikipedia.org/wiki/Histograma) es un diagrama que permite visualizar la distribución de frecuencias sobre un determinado conjunto de valores.

Partiendo de un fichero de entrada que contiene letras de forma consecutiva se pide calcular la _frecuencia absoluta_ de cada una de las etiquetas (letras) y generar un fichero de salida con el histograma correspondiente.

Para el caso que nos ocupa, la salida debería ser:

```
A ██████████████████ 18
B ███████████████ 15
C █████████████ 13
D █████████████ 13
E ███████████ 11
F ██████████ 10
G ██████ 6
H ██████████████ 14
```
'''

ENTRYPOINT = {
    'PARAMS': [
        ['data_path', Path],
    ],
    'RETURN': [
        ['histogram_path', Path],
    ],
}

CHECK_CASES = [
    [['data/histogram/data.txt'], ['data/histogram/histogram.txt']],
]
