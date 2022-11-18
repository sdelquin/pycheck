from .checking import Checking
from .exercise import Exercise


def check(filepath: str) -> dict:
    exercise = Exercise(filepath)
    target_func = exercise.get_target_func()
    runnings = []
    for args, expected_output in exercise.check_cases:
        output = target_func(*args)
        output = output if exercise.multiple_returns else [output]
        passed = all(pout == pexp for pout, pexp in zip(output, expected_output))
        runnings.append(dict(passed=passed, output=output))
    return Checking(exercise, runnings)


def run(filepath: str, args: list[str]):
    exercise = Exercise(filepath)
    target_func = exercise.get_target_func()
    args = [cast(arg) for cast, arg in zip(exercise.arg_casts, args)]
    return target_func(*args)
