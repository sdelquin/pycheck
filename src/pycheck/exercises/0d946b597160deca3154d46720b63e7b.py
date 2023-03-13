TITLE = 'Contando ovejas'

DESCRIPTION = '''
No te puedes dormir, pero afortunadamente un programa Python te ayuda a ello. Dado un número entero _num_sheeps_ devuelve la cuenta de las ovejas...
'''

ENTRYPOINT = {
    'PARAMS': [
        ['num_sheeps', int],
    ],
    'RETURN': [
        ['sleep', str],
    ],
}

CHECK_CASES = [
    [[0], ['']],
    [[3], ['sheep...sheep...sheep...']],
    [[5], ['sheep...sheep...sheep...sheep...sheep...']],
    [[7], ['sheep...sheep...sheep...sheep...sheep...sheep...sheep...']],
]

SOURCE = 'https://www.codewars.com/kata/5b077ebdaf15be5c7f000077'
