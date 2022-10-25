import importlib
import re
from typing import Iterable


def get_config(exercise_id: str):
    module_path, exercise_slug = re.match(r'^(.*)\.([^.]+)+$', exercise_id).groups()
    module_path = f'pycheck.config.{module_path}'
    module = importlib.import_module(module_path)
    return getattr(module, exercise_slug)


def run_cases(cases: Iterable, func: callable):
    for __args, __expected_output in cases:
        if (__output := func(*__args)) != __expected_output:
            print(f'❌ No funciona para la entrada {__args}')
            print(f'   Salida esperada: {__expected_output}')
            print(f'   Salida obtenida: {__output}')
            break
    else:
        print('✅ ¡Enhorabuena! Todo funciona bien')


def run_custom(arg_casts: Iterable, args: Iterable, func: callable):
    __args = [cast(arg) for cast, arg in zip(arg_casts, args)]
    if (__result := func(*__args)) is not None:
        print(__result)
