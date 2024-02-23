from pathlib import Path

TITLE = 'Código morse'

DESCRIPTION = """
El [código morse](https://es.wikipedia.org/wiki/C%C3%B3digo_morse) es un sistema de representación de letras y números mediante señales emitidas de forma intermitente.

Habrá un fichero en el que se encuentran las señales de código morse. El programa también recibirá una frase que habrá que convertir a código morse utilizando las señales dadas.

Notas:
- Habrá que ignorar cualquier caracter que no sea alfanumérico.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['morse_signals', Path],
        ['sentence', str],
    ],
    'RETURN': [
        ['morse_sentence', str],
    ],
}

CHECK_CASES = [
    [
        ['data/morse_code/signals.morse', 'hello, world!'],
        ['.... . .-.. .-.. --- .-- --- .-. .-.. -..'],
    ],
    [
        ['data/morse_code/signals.morse', 'now is better than never!'],
        ['-. --- .-- .. ... -... . - - . .-. - .... .- -. -. . ...- . .-.'],
    ],
    [
        ['data/morse_code/signals.morse', 'Believe in YOU 😀'],
        ['-... . .-.. .. . ...- . .. -. -.-- --- ..-'],
    ],
]
