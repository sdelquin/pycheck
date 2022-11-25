TITLE = 'Volumen de una esfera'

DESCRIPTION = '''
Obtenga el volumen de una esfera dado su radio. Use PI con 2 cifras decimales.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['radius', float],
    ],
    'RETURN': [
        ['volume', float],
    ],
}

CHECK_CASES = [
    [[5], [523.3333333333334]],
    [[15.658], [16072.271158372905]],
    [[9.99], [4174.11922248]],
]
