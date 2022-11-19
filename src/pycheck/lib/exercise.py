import hashlib
import importlib
import os
import sys

from rich.console import Console
from rich.table import Table

from pycheck import settings

from .exceptions import ExerciseNotFoundError


class Exercise:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.filename = os.path.basename(self.filepath)
        self.get_config()
        self.get_arg_casts()
        self.multiple_returns = len(self.entrypoint['return']) > 1

    @property
    def hash(self) -> str:
        return hashlib.md5(self.filename.encode()).hexdigest()

    def create_template(self):
        template = self.render_template()
        with open(self.filepath, 'w') as f:
            f.write(template)

    def get_target_func(self) -> callable:
        module_name = os.path.splitext(self.filepath)[0]
        spec = importlib.util.spec_from_file_location(module_name, self.filepath)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return getattr(module, self.entrypoint['name'])

    def list_cases(self):
        console = Console()
        table = Table(show_header=True)

        for param_name, _ in self.entrypoint['params']:
            table.add_column(param_name, header_style='yellow')
        for return_name, _ in self.entrypoint['return']:
            table.add_column(return_name, header_style='blue')

        for args, expected_output in self.check_cases:
            fargs = [str(arg) for arg in args]
            fout = [str(out) for out in expected_output]
            row = fargs + fout
            table.add_row(*row)

        console.print(table)

    def render_template(self) -> str:
        params = ', '.join(
            f'{param}: {annot.__name__}' for param, annot in self.entrypoint['params']
        )
        return_names = ', '.join(ret_name for ret_name, _ in self.entrypoint['return'])
        return_type = (
            'tuple' if self.multiple_returns else self.entrypoint['return'][0][1].__name__
        )
        return f"""'''
{self.description}
'''


def {self.entrypoint['name']}({params}) -> {return_type}:
    # TU CÓDIGO AQUÍ
    return {return_names}
"""

    def get_config(self):
        config_path = f'{settings.EXERCISES_FOLDER}.{self.hash}'
        try:
            config = importlib.import_module(config_path)
        except ModuleNotFoundError:
            raise ExerciseNotFoundError(self.filename)
        self.description = config.DESCRIPTION.strip()
        self.entrypoint = {
            'name': config.ENTRYPOINT.get('NAME', settings.ENTRYPOINT_NAME),
            'params': config.ENTRYPOINT['PARAMS'],
            'return': config.ENTRYPOINT['RETURN'],
        }
        self.check_cases = config.CHECK_CASES

    def get_arg_casts(self):
        PRIMITIVE_TYPES = [int, bool, float, str]
        self.arg_casts = []
        for _, param_type in self.entrypoint['params']:
            cast = param_type if param_type in PRIMITIVE_TYPES else eval
            self.arg_casts.append(cast)
