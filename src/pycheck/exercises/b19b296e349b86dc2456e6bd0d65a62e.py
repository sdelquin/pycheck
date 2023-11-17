TITLE = 'Convirtiendo ADN a ARN'

DESCRIPTION = """
Escribe un programa en Python que realice la conversión de una secuencia de ADN en su correspondiente ARN. El ARN es igual que el ADN salvo que la Timina se sustituye por Uracilo (`U`).

NOTA:
- No se puede utilizar la función _replace()_
"""

ENTRYPOINT = {
    'PARAMS': [
        ['adn', str],
    ],
    'RETURN': [
        ['arn', str],
    ],
}

CHECK_CASES = [
    [['AGTCCCAGGT'], ['AGUCCCAGGU']],
    [['GCGCACTCTTCTTTGCTCTT'], ['GCGCACUCUUCUUUGCUCUU']],
    [['CCGGAGATTGGCTACTGAAGATCCA'], ['CCGGAGAUUGGCUACUGAAGAUCCA']],
]
