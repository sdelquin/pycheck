import importlib.util
import os
import sys
from typing import get_type_hints

from pycheck import settings


def get_arg_casts(func: callable) -> list:
    arg_casts = []
    for param_name, param_type in get_type_hints(func).items():
        if param_name != 'return':
            cast = param_type if param_type in [int, bool, float, str] else eval
            arg_casts.append(cast)
    return arg_casts


def get_target_func(program_path: str):
    module_name = os.path.splitext(program_path)[0]
    spec = importlib.util.spec_from_file_location(module_name, program_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module.run


def get_check_cases(hashed_filename: str) -> list:
    program_path = f'{settings.CHECK_CASES_BASE_PATH}.{hashed_filename}'
    module = importlib.import_module(program_path)
    return module.__CHECK_CASES__
