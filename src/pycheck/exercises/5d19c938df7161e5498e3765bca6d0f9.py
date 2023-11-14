TITLE = 'Donando sangre'

DESCRIPTION = """
Escriba un programa que acepte edad, peso, pulso y número de plaquetas de una persona y determine si cumple con [los requisitos para donar sanger](http://www3.gobiernodecanarias.org/sanidad/ichh/donantes/requisitos.asp).
"""

ENTRYPOINT = {
    'PARAMS': [
        ['age', int],
        ['weight', int],
        ['heartbeat', int],
        ['platelets', int],
    ],
    'RETURN': [
        ['suitable_for_donation', bool],
    ],
}

CHECK_CASES = [
    [[34, 81, 70, 151_000], [True]],
    [[17, 81, 70, 200_000], [False]],
    [[50, 47, 70, 171_000], [False]],
    [[50, 47, 70, 128_000], [False]],
    [[19, 86, 90, 210_000], [True]],
    [[19, 86, 120, 210_000], [False]],
]
