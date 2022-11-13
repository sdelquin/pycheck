import hashlib
import importlib.util
import sys
from pathlib import Path
from typing import get_type_hints


def get_arg_casts(func: callable):
    arg_casts = []
    for param_name, param_type in get_type_hints(func).items():
        if param_name != 'return':
            cast = param_type if param_type in [int, bool, float, str] else eval
            arg_casts.append(cast)
    return arg_casts


def load_module(module_path: str, module_name: str = 'program'):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def get_check_cases(module_path: str):
    filename = Path(module_path).name
    hashed_filename = hashlib.md5(filename.encode()).hexdigest()
    module_path = f'pycheck.check_cases.{hashed_filename}'
    module = importlib.import_module(module_path)
    return module.__CHECK_CASES__
