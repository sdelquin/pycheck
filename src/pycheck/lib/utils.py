import importlib.util
import os
import subprocess
import sys
from types import ModuleType

import pkg_resources
from rich.console import Console
from rich.table import Table

from pycheck import settings


def get_target_func(program_path: str, entrypoint_name: str) -> callable:
    module_name = os.path.splitext(program_path)[0]
    spec = importlib.util.spec_from_file_location(module_name, program_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return getattr(module, entrypoint_name)


def get_arg_casts(entrypoint_params: list) -> list:
    PRIMITIVE_TYPES = [int, bool, float, str]
    arg_casts = []
    for _, param_type in entrypoint_params:
        cast = param_type if param_type in PRIMITIVE_TYPES else eval
        arg_casts.append(cast)
    return arg_casts


def get_config(hashed_filename: str) -> ModuleType:
    config_path = f'{settings.CONFIG_BASE_PATH}.{hashed_filename}'
    return importlib.import_module(config_path)


def render_template(description: str, fname: str, params: list, _return: list) -> str:
    params = ', '.join(f'{param}: {annot.__name__}' for param, annot in params)
    return_names = ', '.join(ret_name for ret_name, _ in _return)
    return_type = _return[0][1].__name__ if len(_return) == 1 else 'tuple'
    return f"""
'''
{description}
'''


def {fname}({params}) -> {return_type}:
    # TU CÓDIGO AQUÍ
    return {return_names}
""".lstrip()


def update_pycheck():
    url = f'git+{settings.GITHUB_REPO}'
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', url])


def get_pycheck_version():
    return pkg_resources.get_distribution('pycheck').version


def show_cases(check_cases: list, params: list, _return: list):
    console = Console()
    table = Table(show_header=True)

    for param_name, _ in params:
        table.add_column(param_name, header_style='yellow')
    for return_name, _ in _return:
        table.add_column(return_name, header_style='blue')

    for args, expected_output in check_cases:
        fargs = [str(arg) for arg in args]
        fout = [str(out) for out in expected_output]
        row = fargs + fout
        table.add_row(*row)

    console.print(table)


def show_grade(grade: dict):
    if grade['passed']:
        print('✅ ¡Enhorabuena! Todo funciona bien')
    else:
        print(f'❌ No funciona para la entrada {grade["args"]}')
        print(f'   Salida esperada: {grade["expected_output"]}')
        print(f'   Salida obtenida: {grade["output"]}')
