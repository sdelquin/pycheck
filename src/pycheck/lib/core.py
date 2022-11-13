from typing import Iterable

from . import utils


class PyChecker:
    def __init__(self, cmd: Iterable):
        self.filename, *self.cli_args = cmd
        self.target_func = utils.get_target_func(self.filename)
        self.check_cases = utils.get_check_cases(self.filename)
        self.arg_casts = utils.get_arg_casts(self.target_func)
        self.flag = self.cli_args[0] if len(self.cli_args) > 0 else ''

    def run_cases(self):
        for args, expected_output in self.check_cases:
            if (output := self.target_func(*args)) != expected_output:
                print(f'❌ No funciona para la entrada {args}')
                print(f'   Salida esperada: {expected_output}')
                print(f'   Salida obtenida: {output}')
                break
        else:
            print('✅ ¡Enhorabuena! Todo funciona bien')

    def run_custom(self):
        args = [cast(arg) for cast, arg in zip(self.arg_casts, self.cli_args)]
        if (result := self.target_func(*args)) is not None:
            print(result)

    def list_cases(self):
        for args, expected_output in self.check_cases:
            print(f'{args}: {expected_output}')

    def run(self):
        match self.flag:
            case '':
                self.run_cases()
            case '-l':
                self.list_cases()
            case '-h':
                self.usage()
            case _:
                self.run_custom()

    def usage(self):
        print(
            '''🚨 Modo de uso:
pycheck <program.py> [ARGS]
    Comprueba tu programa contra los casos establecidos.
    -h: Muestra esta ayuda.
    -l: Muestra un listado de los casos (entradas y salidas esperadas).
    [ARGS]: Ejecuta tu programa con los argumentos indicados.'''
        )
