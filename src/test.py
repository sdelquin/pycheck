import sys

from pycheck import check

CHECK_CASES = [
    [[3, 4], 7],
    [[1, 9], 10],
    [[200, 55], 255],
]


def run(a: int, b: int) -> int:
    result = a + b
    return result


if __name__ == '__main__':
    check(run, CHECK_CASES, sys.argv)
