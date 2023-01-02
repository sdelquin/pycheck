import conftest
import pytest

from pycheck import NotAuthorizedError
from pycheck.lib import utils


def test_admin_required():
    conftest.disable_key_admin()
    with pytest.raises(NotAuthorizedError):
        utils.admin_required()


def test_hash(exercise):
    hash = utils.gen_hash(conftest.EXERCISE_PATH.stem)
    assert exercise.hash == hash
