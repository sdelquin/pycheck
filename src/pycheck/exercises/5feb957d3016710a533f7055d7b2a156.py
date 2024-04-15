TITLE = 'Troceado recursivo'

DESCRIPTION = """
Dada una cadena de texto, se pide trocearla con un tamaño _wsize_ utilizando una función recursiva.
"""

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'rslice',
    'PARAMS': [
        ['text', str],
        ['wsize', int],
    ],
    'RETURN': [
        ['stext', list],
    ],
}

CHECK_CASES = [
    [
        ['La felicidad no es algo que viene hecho. Proviene de tus propias acciones', 10],
        [
            [
                'La felicid',
                'ad no es a',
                'lgo que vi',
                'ene hecho.',
                ' Proviene ',
                'de tus pro',
                'pias accio',
                'nes',
            ],
        ],
    ],
    [
        [
            'Si crees que eres demasiado pequeño para hacer la diferencia, intenta dormir con un mosquito',
            20,
        ],
        [
            [
                'Si crees que eres de',
                'masiado pequeño para',
                ' hacer la diferencia',
                ', intenta dormir con',
                ' un mosquito',
            ],
        ],
    ],
    [
        [
            'El amor es la ausencia de juicio',
            5,
        ],
        [
            [
                'El am',
                'or es',
                ' la a',
                'usenc',
                'ia de',
                ' juic',
                'io',
            ],
        ],
    ],
]
