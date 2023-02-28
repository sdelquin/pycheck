from pathlib import Path

TITLE = 'Máquina de vending'

DESCRIPTION = '''
Consulte la descripción del ejercicio en [este enlace](https://github.com/sdelquin/pro/blob/main/ut4/te1/README.md).
'''

ENTRYPOINT = {
    'PARAMS': [
        ['operations_path', Path],
    ],
    'RETURN': [
        ['status_path', Path],
    ],
}

CHECK_CASES = [
    [['data/vending/operations.dat'], ['data/vending/status.dat']],
]
