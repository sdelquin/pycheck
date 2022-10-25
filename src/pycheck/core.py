from typing import Iterable

from pycheck import utils


class PyChecker:
    def __init__(self, exercise_id: str, cmd: Iterable, target_func: callable):
        self.exercise_id = exercise_id
        self.filename, *self.cli_args = cmd
        self.flag = self.cli_args[0].strip()
        self.target_func = target_func
        self.config = utils.get_config(exercise_id)

    def run_cases(self):
        for args, expected_output in self.config['cases']:
            if (output := self.target_func(*args)) != expected_output:
                print(f'❌ No funciona para la entrada {args}')
                print(f'   Salida esperada: {expected_output}')
                print(f'   Salida obtenida: {output}')
                break
        else:
            print('✅ ¡Enhorabuena! Todo funciona bien')

    def run_custom(self):
        args = [cast(arg) for cast, arg in zip(self.config['arg_casts'], self.cli_args)]
        if (result := self.target_func(*args)) is not None:
            print(result)

    def run(self):
        match self.flag:
            case '-k':
                self.run_cases()
            case _:
                self.run_custom()
