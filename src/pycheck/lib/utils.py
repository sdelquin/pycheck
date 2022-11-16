import importlib.util
import os
import subprocess
import sys
from types import ModuleType

import pkg_resources

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
    return f"""
'''
{description}
'''


def {fname}({params}) -> {_return[1].__name__}:
    # TU CÓDIGO AQUÍ
    return {_return[0]}
""".lstrip()


def update_pycheck():
    url = f'git+{settings.GITHUB_REPO}'
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', url])


def get_pycheck_version():
    return pkg_resources.get_distribution('pycheck').version
