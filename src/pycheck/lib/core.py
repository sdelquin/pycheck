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
    exercise = source if isinstance(source, Exercise) else Exercise(source)
    exercise.set_check_case(case_no)
    redirect_stdout = None if ignore_stdout else sys.stdout
    target_func = exercise.get_target_func(ignore_stdin)
    runnings = []
    for args, expected_output in exercise.check_cases:
        with contextlib.redirect_stdout(redirect_stdout):
            output = target_func(*args)
        output = output if exercise.multiple_returns else [output]
        passed = all(pout == pexp for pout, pexp in zip(output, expected_output))
        runnings.append(dict(passed=passed, output=output))
    return Checking(exercise, runnings)


def run(source: str | Exercise, args: list[str]):
    '''source puede ser la ruta al fichero del ejercicio o bien
    una instancia del ejercicio'''
    exercise = source if isinstance(source, Exercise) else Exercise(source)
    target_func = exercise.get_target_func()
    args = [cast(arg) for cast, arg in zip(exercise.arg_casts, args)]
    return target_func(*args)
