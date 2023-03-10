TITLE = 'Quitando primero y último'

DESCRIPTION = '''
Dada una cadena de texto, se pide eliminar el primer y el último caracter de dicha cadena de texto.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['stext', str],
    ],
}

CHECK_CASES = [
    [['What can I do'], ['hat can I d']],
    [['Only when I sleep'], ['nly when I slee']],
    [['Runaway'], ['unawa']],
]

SOURCE = 'https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0'
