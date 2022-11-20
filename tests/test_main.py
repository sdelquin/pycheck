from typer.testing import CliRunner

import pycheck
from pycheck import Exercise
from pycheck.main import app

runner = CliRunner()


def test_update(mocker):
    mocker.patch('pycheck.lib.utils.update_pycheck')
    result = runner.invoke(app, ['-u'])
    assert result.exit_code == 0
    pycheck.lib.utils.update_pycheck.assert_called_once()


def test_version(mocker):
    mocker.patch('pycheck.lib.utils.get_pycheck_version')
    result = runner.invoke(app, ['-v'])
    assert result.exit_code == 0
    pycheck.lib.utils.get_pycheck_version.assert_called_once()


def test_create_template(mocker, exercise: Exercise):
    mocker.patch('pycheck.lib.exercise.Exercise.create_template')
    result = runner.invoke(app, ['-t', exercise.filepath])
    assert result.exit_code == 0
    exercise.create_template.assert_called_once()


def test_description(exercise: Exercise):
    result = runner.invoke(app, ['-d', exercise.filepath])
    assert result.exit_code == 0


def test_list_cases(mocker, exercise: Exercise):
    mocker.patch('pycheck.lib.exercise.Exercise.list_cases')
    result = runner.invoke(app, ['-l', exercise.filepath])
    assert result.exit_code == 0
    exercise.list_cases.assert_called_once()


def test_check(mocker, exercise: Exercise):
    mocker.patch('pycheck.check')
    result = runner.invoke(app, ['-c', exercise.filepath])
    assert result.exit_code == 0
    pycheck.check.assert_called_once()


def test_run(mocker, exercise: Exercise):
    mocker.patch('pycheck.run')
    result = runner.invoke(app, ['-r', exercise.filepath, '2', '3'])
    assert result.exit_code == 0
    pycheck.run.assert_called_once()


def test_help(mocker):
    mocker.patch('pycheck.run')
    result = runner.invoke(app, ['--help'])
    assert result.exit_code == 0
    assert 'Usage' in result.stdout
