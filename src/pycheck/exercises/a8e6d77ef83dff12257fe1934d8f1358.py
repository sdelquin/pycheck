TITLE = 'Dígito de control del NIF'

DESCRIPTION = '''
Se pide obtener [el dígito de control de un NIF](https://www.interior.gob.es/opencms/ca/servicios-al-ciudadano/tramites-y-gestiones/dni/calculo-del-digito-de-control-del-nif-nie/) de entrada.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['nif', str],
    ],
    'RETURN': [
        ['wnif', str],
    ],
}

CHECK_CASES = [
    [['78654355'], ['78654355J']],
    [['65895421'], ['65895421F']],
    [['43298006'], ['43298006T']],
]
