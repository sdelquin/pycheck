import sys

from pycheck.lib.core import PyChecker


def check(*args):
    pychecker = PyChecker(args)
    pychecker.run()


def entrypoint():
    check(*sys.argv[1:])


if __name__ == '__main__':
    entrypoint()
