import sys

from pycheck.lib.core import PyChecker
from pycheck.lib.utils import load_module


def check(*args):
    module = load_module(args[0])
    pychecker = PyChecker(module.run, module.CHECK_CASES, args)
    pychecker.run()


def entrypoint():
    check(*sys.argv[1:])


if __name__ == '__main__':
    entrypoint()
