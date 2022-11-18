from pathlib import Path

from prettyconf import config

PROJECT_DIR = Path(__file__).parent.parent.parent

EXERCISES_FOLDER = config('EXERCISES_FOLDER', default='pycheck.exercises')
ENTRYPOINT_NAME = config('ENTRYPOINT_NAME', default='run')
GITHUB_REPO = config('GITHUB_REPO', default='https://github.com/sdelquin/pycheck.git')
PYPROJECT_PATH = config('PYPROJECT_PATH', default=PROJECT_DIR / 'pyproject.toml')
STATUS_PASSED_EMOJI = config('STATUS_PASSED_EMOJI', default='✅')
STATUS_NOT_PASSED_EMOJI = config('STATUS_NOT_PASSED_EMOJI', default='❌')
MSG_PASSED_EMOJI = config('MSG_PASSED_EMOJI', default='🍏')
MSG_NOT_PASSED_EMOJI = config('MSG_NOT_PASSED_EMOJI', default='🚨')
