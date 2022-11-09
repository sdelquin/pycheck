import os
from typing import Iterable

from pycheck.lib.core import PyChecker


def check(target_func: callable, check_cases: Iterable, cmd: Iterable):
    pychecker = PyChecker(target_func, check_cases, cmd)
    pychecker.run()


def hello():
    print(os.getcwd())
