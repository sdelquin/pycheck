import hashlib
import os

from . import utils


class PyCheck:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.filename = os.path.basename(self.filepath)
        self.config = utils.get_config(self.hash)
        self.check_cases = self.config.__CHECK_CASES__
        self.template = self.config.__TEMPLATE__.lstrip()

    def check(self):
        self.target_func = utils.get_target_func(self.filepath)
        for args, expected_output in self.check_cases:
            if (output := self.target_func(*args)) != expected_output:
                print(f'❌ No funciona para la entrada {args}')
                print(f'   Salida esperada: {expected_output}')
                print(f'   Salida obtenida: {output}')
                break
        else:
            print('✅ ¡Enhorabuena! Todo funciona bien')

    def run(self, args: list[str]):
        self.target_func = utils.get_target_func(self.filepath)
        self.arg_casts = utils.get_arg_casts(self.target_func)
        args = [cast(arg) for cast, arg in zip(self.arg_casts, args)]
        if (result := self.target_func(*args)) is not None:
            print(result)

    def list_cases(self):
        for args, expected_output in self.check_cases:
            print(f'{args}: {expected_output}')

    @property
    def hash(self):
        return hashlib.md5(self.filename.encode()).hexdigest()

    def create_template(self):
        with open(self.filename, 'w') as f:
            f.write(self.template)
