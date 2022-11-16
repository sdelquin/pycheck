import hashlib
import os
import subprocess
import sys

from pycheck import settings

from . import utils


class PyCheck:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.filename = os.path.basename(self.filepath)
        config = utils.get_config(self.hash)
        self.description = config.DESCRIPTION.strip()
        self.entrypoint_name = config.ENTRYPOINT.get('NAME', settings.ENTRYPOINT_NAME)
        self.entrypoint_params = config.ENTRYPOINT['PARAMS']
        self.entrypoint_return = config.ENTRYPOINT['RETURN']
        self.check_cases = config.CHECK_CASES
        self.arg_casts = utils.get_arg_casts(self.entrypoint_params)

    def check(self):
        target_func = utils.get_target_func(self.filepath, self.entrypoint_name)
        for args, expected_output in self.check_cases:
            if (output := target_func(*args)) != expected_output:
                print(f'❌ No funciona para la entrada {args}')
                print(f'   Salida esperada: {expected_output}')
                print(f'   Salida obtenida: {output}')
                break
        else:
            print('✅ ¡Enhorabuena! Todo funciona bien')

    def run(self, args: list[str]):
        target_func = utils.get_target_func(self.filepath, self.entrypoint_name)
        args = [cast(arg) for cast, arg in zip(self.arg_casts, args)]
        if (result := target_func(*args)) is not None:
            print(result)

    def list_cases(self):
        for args, expected_output in self.check_cases:
            print(f'{args}: {expected_output}')

    @property
    def hash(self) -> str:
        return hashlib.md5(self.filename.encode()).hexdigest()

    def create_template(self):
        template = utils.render_template(
            self.description,
            self.entrypoint_name,
            self.entrypoint_params,
            self.entrypoint_return,
        )
        with open(self.filename, 'w') as f:
            f.write(template)

    def update(self):
        url = f'git+{settings.GITHUB_REPO}'
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', url])
