TITLE = 'Animales super rápidos'

DESCRIPTION = '''
El **escarabajo tigre** es uno de los animales más veloces del planeta llegando a alcanzar el equivalente a 400 km/h (si hablamos de un humano de estatura media).

Dado que sus distancias son más cortas, convierta la velocidad de _km/h_ a _cm/s_.
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
    [[1.08], [30.0]],
    [[4.25], [118.0]],
    [[0.099], [2.0]],
]

SOURCE = 'https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6'
