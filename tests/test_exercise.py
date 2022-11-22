import os
import re
import shutil

import conftest
import pytest

from pycheck import Exercise
from pycheck.lib.exceptions import ExerciseNotAvailableError, TemplateNotFoundError


def test_instance(exercise: Exercise):
    assert isinstance(exercise, Exercise)
    assert exercise.filename == os.path.basename(conftest.EXERCISE_PATH)
    assert exercise.filepath == conftest.EXERCISE_PATH
    assert re.match(r'^[a-f0-9]{32}$', exercise.config_hash)
    assert len(exercise.description) > 0
    assert len(exercise.entrypoint.keys()) > 0
    assert len(exercise.check_cases) > 0
    assert len(exercise.arg_casts) > 0
    assert not exercise.multiple_returns


def test_instance_file_not_found():
    with pytest.raises(ExerciseNotAvailableError):
        Exercise('strange.py')


def test_get_target_func(exercise: Exercise):
    func = exercise.get_target_func()
    assert func is not None


def test_get_target_func_no_template():
    exercise = Exercise(conftest.EXERCISE_NAME)
    with pytest.raises(TemplateNotFoundError):
        exercise.get_target_func()


def test_create_template(exercise: Exercise):
    filepath_bak = exercise.filepath + '.bak'
    shutil.copy(exercise.filepath, filepath_bak)
    exercise.create_template(ask_on_overwrite=False)
    template_contents = open(exercise.filepath).read()
    assert os.path.isfile(exercise.filepath)
    assert exercise.description in template_contents
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
