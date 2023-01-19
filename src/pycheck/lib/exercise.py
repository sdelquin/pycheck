import importlib
import sys
from pathlib import Path

import typer
from rich import print
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table

from pycheck import settings

from . import utils
from .exceptions import (
    CheckCaseNotFoundError,
    ExerciseNotAvailableError,
    TemplateNotFoundError,
)


class Exercise:
    def __init__(self, name: Path | str):
        '''
        exercise_name puede ser:
            a) El nombre del ejercicio (sum)
            b) Un string representando la ruta al ejercicio (ex/sum.py)
            c) Un objeto Path que almacena el ejercicio (ex/sum.py)
        '''
        self.filepath = name if isinstance(name, Path) else Path(name)
        if not self.filepath.suffix:
            self.filepath = self.filepath.with_suffix('.py')
        self.name = self.filepath.stem
        self.filename = self.filepath.name
        self.hash = utils.gen_hash(self.name)
        self.config_path = settings.EXERCISES_CONFIG_PATH / self.hash
        self.config_module = f'{settings.EXERCISES_CONFIG_MODULE}.{self.hash}'
        self.__get_config()
        self.__get_arg_casts()
        self.multiple_returns = len(self.entrypoint['return']) > 1
        self.case_no = 0

    def __str__(self):
        return self.name

    def set_check_case(self, case_no: int = 0):
        try:
            self.check_cases = (
                self.check_cases if case_no == 0 else [self.check_cases[case_no - 1]]
            )
        except IndexError:
            raise CheckCaseNotFoundError(self, case_no)
        else:
            self.case_no = case_no

    def create_template(self, ask_on_overwrite: bool = True):
        if (
            self.filepath.exists()
            and ask_on_overwrite
            and not typer.confirm('Ya existe la plantilla. ¿Desea sobreescribirla?')
        ):
            return
        self.filepath.write_text(self.__render_template())
        utils.succ_msg(f"Plantilla creada satisfactoriamente: [cyan]{self.filepath}")

    def get_target_func(self, ignore_stdin: bool = False) -> callable:
        module_name = self.filepath.stem
        spec = importlib.util.spec_from_file_location(module_name, self.filepath)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        try:
            spec.loader.exec_module(module)
        except FileNotFoundError:
            raise TemplateNotFoundError(self)
        if ignore_stdin:
            setattr(module, 'input', lambda _: '0')
        return getattr(module, self.entrypoint['name'])

    def show_description(self):
        panel = Panel(
            Markdown(self.description),
            title=self.title,
            expand=False,
            border_style='purple',
        )
        print(panel)

    def show_check_cases(self):
        table = Table(show_header=True)

        table.add_column('#', header_style='grey42', style='grey42')
        # Parámetros de entrada
        for param_name, param_type in self.entrypoint['params']:
            heading = f'[italic](entrada)[/]\n{param_name}: {param_type.__name__}'
            table.add_column(heading, header_style='yellow')
        # Valores de retorno
        for return_name, return_type in self.entrypoint['return']:
            heading = f'[italic](salida)[/]\n{return_name}: {return_type.__name__}'
            table.add_column(heading, header_style='blue')

        case_start = 1 if self.case_no == 0 else self.case_no
        for case_no, (args, expected_output) in enumerate(
            self.check_cases, start=case_start
        ):
            case = str(case_no)
            fargs = [repr(arg) for arg in args]
            fout = [repr(out) for out in expected_output]
            row = fargs + fout
            table.add_row(case, *row)

        print(table)

    def show(self, description=True, check_cases=True):
        if description:
            self.show_description()
        if check_cases:
            self.show_check_cases()

    def __get_config(self):
        try:
            config = importlib.import_module(self.config_module)
        except ModuleNotFoundError:
            raise ExerciseNotAvailableError(self)
        self.description = config.DESCRIPTION.strip()
        self.entrypoint = {
            'name': config.ENTRYPOINT.get('NAME', settings.ENTRYPOINT_NAME),
            'params': config.ENTRYPOINT['PARAMS'],
            'return': config.ENTRYPOINT['RETURN'],
        }
        self.check_cases = config.CHECK_CASES
        self.title = config.TITLE.upper()

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
        args = ', '.join(repr(c) for c in self.check_cases[0][0])
        return_names = [ret_name for ret_name, _ in self.entrypoint['return']]
        output_placeholder = (
            ' = '.join(return_names) + f" = '{settings.OUTPUT_PLACEHOLDER}'"
        )
        return_sentence = 'return ' + ', '.join(return_names)
        return_type = (
            'tuple' if self.multiple_returns else self.entrypoint['return'][0][1].__name__
        )
        title = f"# {'*' * len(self.title)}\n# {self.title}\n# {'*' * len(self.title)}"
        func = self.entrypoint['name']

        return f"""{title}


def {func}({params}) -> {return_type}:
    # {settings.CODEHERE_PLACEHOLDER}
    {output_placeholder}
    {return_sentence}


if __name__ == '__main__':
    {func}({args})
"""
