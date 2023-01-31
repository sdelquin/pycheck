from pathlib import Path

TITLE = 'La palabra más larga'

DESCRIPTION = '''
Dado un fichero de texto encuentre la palabra más larga.

Notas:
- Si hay varias palabras con la misma longitud devuelva la última ocurrencia.
- Tener en cuenta los siguientes símbolos como frontera de palabras: ,.;:()
'''

ENTRYPOINT = {
    'PARAMS': [
        ['input_path', Path],
    ],
    'RETURN': [
        ['longest_word', str],
    ],
}

CHECK_CASES = [
    [['data/longest_word/python.txt'], ['multiplataforma']],
    [['data/longest_word/java.txt'], ['implementaciones']],
]
