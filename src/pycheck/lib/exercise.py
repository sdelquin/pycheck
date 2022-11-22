import hashlib
import importlib
import os
import sys

import typer
from rich import print
from rich.panel import Panel
from rich.table import Table

from pycheck import settings

from .exceptions import ExerciseNotAvailableError, TemplateNotFoundError


class Exercise:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.filename = os.path.basename(self.filepath)
        self.config_hash = hashlib.md5(self.filename.encode()).hexdigest()
        self.config_path = f'{settings.EXERCISES_FOLDER}.{self.config_hash}'
        self.__get_config()
        self.__get_arg_casts()
        self.multiple_returns = len(self.entrypoint['return']) > 1

    def create_template(self, ask_on_overwrite: bool = True):
        if (
            os.path.exists(self.filepath)
            and ask_on_overwrite
            and not typer.confirm('Ya existe la plantilla. ¿Desea sobreescribirla?')
        ):
            return
        template = self.__render_template()
        with open(self.filepath, 'w') as f:
            f.write(template)

    def get_target_func(self) -> callable:
        module_name = os.path.splitext(self.filepath)[0]
        spec = importlib.util.spec_from_file_location(module_name, self.filepath)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        try:
            spec.loader.exec_module(module)
        except FileNotFoundError:
            raise TemplateNotFoundError(self.filepath)
        return getattr(module, self.entrypoint['name'])

    def show_description(self):
        panel = Panel(
            self.description,
            title='Descripción del ejercicio',
            expand=False,
            border_style='purple',
        )
        print(panel)

    def show_list_cases(self):
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

        print(table)

    def show(self):
        self.show_description()
        self.show_list_cases()

    def __get_config(self):
        try:
            config = importlib.import_module(self.config_path)
        except ModuleNotFoundError:
            raise ExerciseNotAvailableError(self.filename)
        self.description = config.DESCRIPTION.strip()
        self.entrypoint = {
            'name': config.ENTRYPOINT.get('NAME', settings.ENTRYPOINT_NAME),
            'params': config.ENTRYPOINT['PARAMS'],
            'return': config.ENTRYPOINT['RETURN'],
        }
        self.check_cases = config.CHECK_CASES

    def __get_arg_casts(self):
        PRIMITIVE_TYPES = [int, bool, float, str]
        self.arg_casts = []
        for _, param_type in self.entrypoint['params']:
            cast = param_type if param_type in PRIMITIVE_TYPES else eval
            self.arg_casts.append(cast)

    def __render_template(self) -> str:
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
    {settings.CODEHERE_PLACEHOLDER}
    return {return_names}
"""
