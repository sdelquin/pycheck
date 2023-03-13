import importlib
import sys
import zipfile
from pathlib import Path
from typing import Callable

import typer
from jinja2 import Environment, FileSystemLoader
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
        self.config_module = f'{settings.EXERCISES_CONFIG_MODULE}.{self.hash}'
        self.config_data_path = (settings.EXERCISES_CONFIG_DIR / self.hash).with_suffix(
            '.zip'
        )
        self.data_dir = (
            self.filepath.parent / f'{settings.EXERCISE_CONFIG_DATA_DIRNAME}/{self.name}'
        )
        self._get_config()
        self.case_no = 0

    def __str__(self):
        return self.name

    def create_template(self, ask_on_overwrite: bool = True):
        if not (
            self.filepath.exists()
            and ask_on_overwrite
            and not typer.confirm('Ya existe la plantilla. ¿Desea sobreescribirla?')
        ):
            self.filepath.write_text(self._render_template())
            utils.succ_msg(f"Plantilla creada satisfactoriamente: [cyan]{self.filepath}")

        if zipfile.is_zipfile(self.config_data_path):
            if not (
                self.data_dir.exists()
                and ask_on_overwrite
                and not typer.confirm(
                    'Ya existe la carpeta de datos. ¿Desea sobreescribirla?'
                )
            ):
                with zipfile.ZipFile(self.config_data_path) as zf:
                    zf.extractall(self.data_dir)
                utils.succ_msg(
                    f"Carpeta de datos creada satisfactoriamente: [cyan]{self.data_dir}"
                )

    def get_target(self, entrypoint: str, ignore_stdin: bool = False) -> Callable:
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
        return getattr(module, entrypoint)

    def show_description(self):
        panel = Panel(
            Markdown(self.description),
            title=self.title,
            expand=False,
            border_style='purple',
        )
        print(panel)

    def show_check_cases(self):
        pass

    def show(self, description=True, check_cases=True):
        if description:
            self.show_description()
        if check_cases:
            self.show_check_cases()

    def _get_config(self):
        try:
            config = importlib.import_module(self.config_module)
        except ModuleNotFoundError:
            raise ExerciseNotAvailableError(self)
        self.title = config.TITLE.upper()
        self.description = config.DESCRIPTION.strip()
        self.checks = config.CHECKS

    def _render_template(self) -> str:
        # Title
        title = f"# {'*' * len(self.title)}\n# {self.title}\n# {'*' * len(self.title)}"
        # Function name
        func = self.entrypoint['name']
        # Params
        params = ', '.join(
            f'{param}: {annot.__name__}' for param, annot in self.entrypoint['params']
        )
        # Args
        args = ', '.join(repr(c) for c in self.check_cases[0][0])
        # Return
        if self.multiple_returns:
            return_type = 'tuple'
        elif self.returns_file:
            return_type = 'bool'
        else:
            return_type = self.entrypoint['return'][0][1].__name__
        if self.returns_file:
            return_name = self.entrypoint['return'][0][0]
            expected_file = f'{self.data_dir / ".expected"}'
            return_items = f"filecmp.cmp({return_name}, '{expected_file}', shallow=False)"
            output_path = self.check_cases[0][1][0]
            output_placeholder = f"{return_name} = '{output_path}'"
        else:
            return_names = [ret_name for ret_name, _ in self.entrypoint['return']]
            return_items = ', '.join(return_names)
            output_placeholder = (
                ' = '.join(return_names) + f" = '{settings.OUTPUT_PLACEHOLDER}'"
            )

        env = Environment(
            loader=FileSystemLoader(settings.TEMPLATES_DIR),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        template_name = (
            settings.EXERCISE_EMPTY_TEMPLATE_NAME
            if self.empty_template
            else settings.EXERCISE_TEMPLATE_NAME
        )
        template = env.get_template(template_name)
        context = dict(
            title=title,
            func=func,
            params=params,
            return_type=return_type,
            output_placeholder=output_placeholder,
            return_items=return_items,
            args=args,
            returns_file=self.returns_file,
            params_have_files=self.params_have_files,
        )
        return template.render(context)
