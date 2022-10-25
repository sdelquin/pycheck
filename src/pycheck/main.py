from typing import Iterable

from pycheck.core import PyChecker


def check(exercise_id: str, cmd: Iterable, target_func: callable):
    pychecker = PyChecker(exercise_id, cmd, target_func)
    pychecker.run()
