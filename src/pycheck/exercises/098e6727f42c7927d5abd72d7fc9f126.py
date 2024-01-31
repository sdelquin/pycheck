TITLE = 'Palabra diversa'

DESCRIPTION = """
Dada una lista de palabras, indique cuál de todas ellas es la más diversa, entendiendo por diversa **la que más letras distintas del abecedario utiliza**.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['words', list],
    ],
    'RETURN': [
        ['dword', str],
    ],
}

CHECK_CASES = [
    [[['dictionary', 'turtle', 'flexibility', 'humanity']], ['dictionary']],
    [[['light', 'environment', 'watermelon', 'happiness']], ['watermelon']],
    [
        [['telescope', 'blackboard', 'microprocessor', 'incomprehensibility', 'destination']],
        ['incomprehensibility'],
    ],
]
