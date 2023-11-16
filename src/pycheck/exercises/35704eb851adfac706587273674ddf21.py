TITLE = 'Distancia Hamming'

DESCRIPTION = """
Calcule la [distancia hamming](https://es.wikipedia.org/wiki/Distancia_de_Hamming) entre dos cadenas de texto dadas.

NOTAS:
- Si las cadenas de texto tienen distinta longitud habrá que devolver -1.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['text1', str],
        ['text2', str],
    ],
    'RETURN': [
        ['dhamming', int],
    ],
}

CHECK_CASES = [
    [['0001010011101', '0000110010001'], [4]],
    [['abc', 'abcd'], [-1]],
    [['teclado', 'techado'], [1]],
    [['esperanza', 'esmeralda'], [3]],
]
