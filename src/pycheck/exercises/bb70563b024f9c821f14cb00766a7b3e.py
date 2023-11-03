TITLE = 'Dame un slug sencillo'

DESCRIPTION = """
Obtenga el _slug_ de un texto dado. Un _slug_ es una cadena de texto con las siguiente características:
- Todas las letras están en minúsculas.
- Los espacios se sustituyen por guiones medios.
- Las vocales con tilde se sutituyen por vocales sin tilde.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['text', str],
    ],
    'RETURN': [
        ['slug', str],
    ],
}

CHECK_CASES = [
    [['hola probando'], ['hola-probando']],
    [['aéíóu'], ['aeiou']],
    [['El árbol de azúcar'], ['el-arbol-de-azucar']],
    [['TWIST & SHOUT'], ['twist-&-shout']],
]
