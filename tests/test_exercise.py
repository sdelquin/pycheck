import os
import re
import shutil

import conftest
import pytest

from pycheck import (
    CheckCaseNotFoundError,
    Exercise,
    ExerciseNotAvailableError,
    TemplateNotFoundError,
)


def test_instance(exercise: Exercise):
    assert isinstance(exercise, Exercise)
    assert exercise.filepath == conftest.EXERCISE_PATH
    assert exercise.filename == conftest.EXERCISE_PATH.name
    assert re.match(r'^[a-f0-9]{32}$', exercise.hash)
    assert len(exercise.description) > 0
    assert len(exercise.entrypoint.keys()) > 0
    assert len(exercise.check_cases) > 0
    assert len(exercise.arg_casts) > 0
    assert not exercise.multiple_returns


def test_instance_file_not_found():
    with pytest.raises(ExerciseNotAvailableError):
        Exercise('strange.py')


def test_instance_from_stem():
    exercise = Exercise(conftest.EXERCISE_PATH.stem)
    assert isinstance(exercise, Exercise)


def test_get_target_func(exercise: Exercise):
    func = exercise.get_target_func()
    assert func is not None


def test_get_target_func_no_template():
    exercise = Exercise(conftest.EXERCISE_PATH.name)
    with pytest.raises(TemplateNotFoundError):
        exercise.get_target_func()


def test_create_template(exercise: Exercise):
    filepath_bak = exercise.filepath.with_suffix('.bak')
    shutil.copy(exercise.filepath, filepath_bak)
    exercise.create_template(ask_on_overwrite=False)
    template_contents = open(exercise.filepath).read()
    assert os.path.isfile(exercise.filepath)
    assert exercise.description in template_contents
    assert "if __name__ == '__main__':" in template_contents
    assert 'def' in template_contents
    assert 'return' in template_contents
    shutil.copy(filepath_bak, exercise.filepath)
    os.remove(filepath_bak)


def test_show(exercise: Exercise, capsys):
    exercise.show()
    captured = capsys.readouterr()
    assert len(captured.out) > 0
    assert exercise.description in captured.out
    for args, output in exercise.check_cases:
        assert all(str(arg) in captured.out for arg in args)
        assert all(str(out) in captured.out for out in output)


def test_show_description(exercise: Exercise, capsys):
    exercise.show(description=True, check_cases=False)
    captured = capsys.readouterr()
    assert len(captured.out) > 0
    assert exercise.description in captured.out
    assert 'result' not in captured.out


def test_show_check_cases(exercise: Exercise, capsys):
    exercise.show(description=False, check_cases=True)
    captured = capsys.readouterr()
    assert len(captured.out) > 0
    assert exercise.description not in captured.out
    assert 'result' in captured.out


def test_set_check_case(exercise: Exercise):
    exercise.set_check_case(2)
    assert len(exercise.check_cases) == 1
    assert exercise.check_cases == [[[1, 9], [10]]]


def test_set_check_case_not_found(exercise: Exercise):
    with pytest.raises(CheckCaseNotFoundError):
        exercise.set_check_case(100)
