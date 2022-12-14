import conftest
from typer.testing import CliRunner

import pycheck
from pycheck import Exercise, NotAuthorizedError
from pycheck.main import app

runner = CliRunner()


def test_version(mocker):
    mocker.patch('pycheck.lib.utils.get_pycheck_version')
    result = runner.invoke(app, ['--version'])
    assert result.exit_code == 0
    pycheck.lib.utils.get_pycheck_version.assert_called_once()


def test_update(mocker):
    mocker.patch('pycheck.lib.utils.update_pycheck')
    result = runner.invoke(app, ['update'])
    assert result.exit_code == 0
    pycheck.lib.utils.update_pycheck.assert_called_once()


def test_create_template(mocker, exercise: Exercise):
    mocker.patch('pycheck.lib.exercise.Exercise.create_template')
    result = runner.invoke(app, ['template', str(exercise.filepath)])
    assert result.exit_code == 0
    exercise.create_template.assert_called_once()


def test_show(exercise: Exercise):
    result = runner.invoke(app, ['show', str(exercise.filepath)])
    assert result.exit_code == 0


def test_check(mocker, exercise: Exercise):
    mocker.patch('pycheck.check')
    result = runner.invoke(app, ['check', str(exercise.filepath)])
    assert result.exit_code == 0
    pycheck.check.assert_called_once()


def test_run(mocker, exercise: Exercise):
    mocker.patch('pycheck.run')
    result = runner.invoke(app, ['run', str(exercise.filepath), '2', '3'])
    assert result.exit_code == 0
    pycheck.run.assert_called_once()


def test_help(mocker):
    mocker.patch('pycheck.run')
    result = runner.invoke(app, ['--help'])
    assert result.exit_code == 0
    assert 'Usage' in result.stdout


def test_boot(mocker, exercise: Exercise):
    mocker.patch('pycheck.lib.exercise.Exercise.show')
    mocker.patch('pycheck.lib.exercise.Exercise.create_template')
    result = runner.invoke(app, ['boot', str(exercise.filepath)])
    assert result.exit_code == 0
    exercise.show.assert_called_once()
    exercise.create_template.assert_called_once()


# ADMIN


def test_generate(exercise: Exercise):
    conftest.disable_key_admin()
    result = runner.invoke(app, ['generate', str(exercise.filepath)])
    assert result.exit_code != 0
    assert result.exc_info[0] == NotAuthorizedError


def test_hash(exercise: Exercise):
    conftest.disable_key_admin()
    result = runner.invoke(app, ['hash', exercise.name])
    assert result.exit_code != 0
    assert result.exc_info[0] == NotAuthorizedError
