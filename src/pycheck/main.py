import sys
from typing import Iterable
import importlib.util

from pycheck.lib.core import PyChecker


def check(target_func: callable, check_cases: Iterable, cmd: Iterable):
    pychecker = PyChecker(target_func, check_cases, cmd)
    pychecker.run()


def load_module(module_path: str, module_name: str = 'program'):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def entrypoint():
    module = load_module(sys.argv[0])
    check(module.run, module.CHECK_CASES, sys.argv)
