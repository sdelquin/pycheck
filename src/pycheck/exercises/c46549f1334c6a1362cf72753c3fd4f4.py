TITLE = 'Palabras en orden inverso'

DESCRIPTION = '''
Dado un string que contiene palabras separadas por espacio, obtenga otro string donde las palabras estén en orden inverso. En la cadena de salida todo el texto debe quedar en **minúsculas**.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['reversing', str],
    ],
}

CHECK_CASES = [
    [['Hello World'], ['world hello']],
    [['Esto es Python'], ['python es esto']],
    [['último caso de comprobación'], ['comprobación de caso último']],
]

SOURCE = 'https://www.codewars.com/kata/57a55c8b72292d057b000594'
