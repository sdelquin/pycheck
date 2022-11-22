from pathlib import Path

import pytest

import pycheck

EXERCISE_PATH = Path(__file__).parent / 'exercises/sum.py'


@pytest.fixture
def exercise():
    return pycheck.Exercise(EXERCISE_PATH)


@pytest.fixture
def runnings():
    return [
        dict(passed=True, output=[3, 4]),
        dict(passed=True, output=[1, 9]),
        dict(passed=True, output=[200, 55]),
    ]
