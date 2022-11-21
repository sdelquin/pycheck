DESCRIPTION = '''
El escarabajo tigre es el animal más veloz del planeta llegando a alcanzar el equivalente
a 400 km/h.

Dado que sus distancias son más cortas, convierta la velocidad de km/h a cm/s.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['speed_km_h', float],
    ],
    'RETURN': [
        ['speed_cm_s', float],
    ],
}

CHECK_CASES = [
    [[1.08], [30]],
    [[4.25], [118]],
    [[0.099], [2]],
]

SOURCE = 'https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6'
