import hashlib
import os
from typing import Iterable

from . import utils


class PyChecker:
    def __init__(self, cmd: Iterable):
        self.filepath, *self.cli_args = cmd
        self.filename = os.path.basename(self.filepath)
        self.config = utils.get_config(self.hash)
        self.check_cases = self.config.__CHECK_CASES__
        self.template = self.config.__TEMPLATE__.lstrip()
        self.flag = self.cli_args[0].strip() if len(self.cli_args) > 0 else ''

    def run_cases(self):
        self.target_func = utils.get_target_func(self.filepath)
        for args, expected_output in self.check_cases:
            if (output := self.target_func(*args)) != expected_output:
                print(f'❌ No funciona para la entrada {args}')
                print(f'   Salida esperada: {expected_output}')
                print(f'   Salida obtenida: {output}')
                break
        else:
            print('✅ ¡Enhorabuena! Todo funciona bien')

    def run_custom(self):
        self.target_func = utils.get_target_func(self.filepath)
        self.arg_casts = utils.get_arg_casts(self.target_func)
        args = [cast(arg) for cast, arg in zip(self.arg_casts, self.cli_args)]
        if (result := self.target_func(*args)) is not None:
            print(result)

    def list_cases(self):
        for args, expected_output in self.check_cases:
            print(f'{args}: {expected_output}')

    @property
    def hash(self):
        return hashlib.md5(self.filename.encode()).hexdigest()

    def generate_template(self):
        with open(self.filename, 'w') as f:
            f.write(self.template)

    def run(self):
        match self.flag:
            case '':
                self.run_cases()
            case '-l':
                self.list_cases()
            case '-h':
                self.usage()
            case '--hash':
                print(self.hash)
            case '-g':
                self.generate_template()
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
