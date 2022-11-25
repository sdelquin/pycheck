DESCRIPTION = '''
Dada una lista de entrada que contiene cadenas de texto representando el código numérico de
un carácter en valor hexadecimal, obtenga la cadena de texto correspondiente.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['hex_codes', list],
    ],
    'RETURN': [
        ['text', str],
    ],
}

CHECK_CASES = [
    [[['1f49a', '2728', '1f389', '1f3c6']], ['💚✨🎉🏆']],
    [[['47', '65', '6f', '72', '67', '65']], ['George']],
    [[['43', '6c', '6f', '6f', '6e', '65', '79']], ['Clooney']],
]
