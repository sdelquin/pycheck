from typing import Iterable

from pycheck.core import PyChecker


def check(exercise_id: str, cli_args: Iterable, target_func: callable):
    pychecker = PyChecker(exercise_id, cli_args, target_func)
    pychecker.run()
