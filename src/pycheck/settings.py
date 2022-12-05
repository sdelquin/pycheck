from pathlib import Path

from prettyconf import config

PROJECT_DIR = Path(__file__).parent.parent.parent

EXERCISES_CONFIG_PATH = config(
    'EXERCISES_CONFIG_PATH', default=PROJECT_DIR / 'src/pycheck/exercises'
)
EXERCISES_CONFIG_MODULE = config('EXERCISES_CONFIG_MODULE', default='pycheck.exercises')
EXERCISES_DB = config('EXERCISES_DB', default=PROJECT_DIR / 'exercises.csv')
ENTRYPOINT_NAME = config('ENTRYPOINT_NAME', default='run')
GITHUB_REPO = config('GITHUB_REPO', default='https://github.com/sdelquin/pycheck.git')
PYPROJECT_PATH = config('PYPROJECT_PATH', default=PROJECT_DIR / 'pyproject.toml')
STATUS_PASSED_EMOJI = config('STATUS_PASSED_EMOJI', default='✅')
STATUS_NOT_PASSED_EMOJI = config('STATUS_NOT_PASSED_EMOJI', default='❌')
MSG_PASSED_EMOJI = config('MSG_PASSED_EMOJI', default='💚')
MSG_NOT_PASSED_EMOJI = config('MSG_NOT_PASSED_EMOJI', default='🚨')
CODEHERE_PLACEHOLDER = config('CODEHERE_PLACEHOLDER', default='tu código aquí')
PYCOIN_EMOJI = config('PYCOIN_EMOJI', default='🏆')
KEY_ADMIN_PRIVATE = config('PYCHECK_KEY_ADMIN', default='pycheck')
KEY_ADMIN_PUBLIC = '6526dcaf98cd26d64747fad780736a8b'
SUCCESS_MSG_EMOJI = config('SUCCESS_MSG_EMOJI', default='✔')

EXERCISES_CONFIG_TEMPLATE = """
TITLE = ''

DESCRIPTION = '''
'''

ENTRYPOINT = {
    'PARAMS': [
        ['a', int],
    ],
    'RETURN': [
        ['x1', float],
    ],
}

CHECK_CASES = [
    [[], []],
]

SOURCE = ''
"""
