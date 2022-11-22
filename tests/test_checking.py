from pycheck import Checking, Exercise, settings


def test_instance(exercise: Exercise, runnings: list):
    checking = Checking(exercise, runnings)
    assert isinstance(checking, Checking)


def test_display(exercise: Exercise, runnings: list, capsys):
    checking = Checking(exercise, runnings)
    checking.display()
    captured = capsys.readouterr()
    assert settings.STATUS_PASSED_EMOJI in captured.out
    assert settings.MSG_PASSED_EMOJI in captured.out


def test_display_only_summary(exercise: Exercise, runnings: list, capsys):
    checking = Checking(exercise, runnings)
    checking.display(True)
    captured = capsys.readouterr()
    assert settings.STATUS_PASSED_EMOJI not in captured.out
    assert settings.MSG_PASSED_EMOJI in captured.out
