TITLE = 'Encuentre el Unicode'

DESCRIPTION = '''
La carta Unicode de caracteres griegos se puede consultar [en este enlace](https://symbl.cc/en/unicode/blocks/greek-coptic/). Dado un caracter y un desplazamiento _offset_ (valor entero positivo o negativo), encuentre el nuevo caracter en la carta Unicode que se encuentra _offset_ unidades antes o después del caracter dado.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['source_char', str],
        ['offset', int],
    ],
    'RETURN': [
        ['target_char', str],
    ],
}

CHECK_CASES = [
    [['δ', -2], ['β']],
    [['μ', 4], ['π']],
    [['φ', 0], ['φ']],
]
