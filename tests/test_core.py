from pycheck import Exercise, check, run


def test_check(exercise: Exercise):
    checking = check(exercise)
    assert checking.exercise == exercise
    assert checking.passed


def test_run(exercise: Exercise):
    result = run(exercise, [4, 5])
    assert result == 9
