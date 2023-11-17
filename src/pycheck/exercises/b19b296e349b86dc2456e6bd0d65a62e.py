TITLE = 'Convirtiendo ADN a ARN'

DESCRIPTION = """
Escribe un programa en Python que realice la conversión de una secuencia de ADN en su correspondiente ARN. El ARN es igual que el ADN salvo que la Timina se sustituye por Uracilo (`U`).
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
