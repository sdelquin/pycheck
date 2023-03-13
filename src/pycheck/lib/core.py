import contextlib
import sys

from .checking import Checking
from .exercise import Exercise


def check(
    source: str | Exercise,
    ignore_stdout: bool = False,
    ignore_stdin: bool = False,
    case_no: int = 0,
) -> Checking:
    '''source puede ser la ruta al fichero del ejercicio o bien
    una instancia del ejercicio'''

    def as_parameters(**kwargs):
        buff = [f'{name}={value!r}' for name, value in kwargs.items()]
        return ', '.join(buff)

    exercise = source if isinstance(source, Exercise) else Exercise(source)
    for case_no, chk in enumerate(exercise.checks, start=1):
        for is_ok, msg in chk.checks():
            print(case_no, as_parameters(**chk.parameters), msg, is_ok)


def run(source: str | Exercise, args: list[str]):
    '''source puede ser la ruta al fichero del ejercicio o bien
    una instancia del ejercicio'''
    exercise = source if isinstance(source, Exercise) else Exercise(source)
    target_func = exercise.get_target()
    args = [cast(arg) for cast, arg in zip(exercise.arg_casts, args)]
    return target_func(*args)
