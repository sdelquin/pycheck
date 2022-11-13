import sys

from pycheck.lib.core import PyChecker
from pycheck.lib.utils import get_check_cases, load_module


def check(*args):
    program_to_check = args[0]
    module = load_module(program_to_check)
    check_cases = get_check_cases(program_to_check)
    pychecker = PyChecker(module.run, check_cases, args)
    pychecker.run()


def entrypoint():
    check(*sys.argv[1:])


if __name__ == '__main__':
    entrypoint()
