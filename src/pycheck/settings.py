from pathlib import Path

from prettyconf import config

PROJECT_DIR = Path(__file__).parent

EXERCISES_CONFIG_DIR = config('EXERCISES_CONFIG_DIR', default=PROJECT_DIR / 'exercises')
EXERCISES_CONFIG_MODULE = config('EXERCISES_CONFIG_MODULE', default='pycheck.exercises')
EXERCISES_DB = config('EXERCISES_DB', default=PROJECT_DIR / 'exercises.csv')

ENTRYPOINT_NAME = config('ENTRYPOINT_NAME', default='run')
EMPTY_TEMPLATE = config('EMPTY_TEMPLATE', default=False, cast=config.boolean)
GITHUB_REPO = config('GITHUB_REPO', default='https://github.com/sdelquin/pycheck.git')
PYCHECK_DOCS_URL = config('PYCHECK_DOCS_URL', default='https://pycheck.es/docs')

STATUS_PASSED_EMOJI = config('STATUS_PASSED_EMOJI', default='✅')
STATUS_NOT_PASSED_EMOJI = config('STATUS_NOT_PASSED_EMOJI', default='❌')
MSG_PASSED_EMOJI = config('MSG_PASSED_EMOJI', default='💚')
MSG_NOT_PASSED_EMOJI = config('MSG_NOT_PASSED_EMOJI', default='🚨')
SUCCESS_MSG_EMOJI = config('SUCCESS_MSG_EMOJI', default='✔')
ERROR_MSG_EMOJI = config('ERROR_MSG_EMOJI', default='✕')
WARNING_MSG_EMOJI = config('WARNING_MSG_EMOJI', default='⚠')

OUTPUT_PLACEHOLDER = config('OUTPUT_PLACEHOLDER', default='output')
KEY_ADMIN_PRIVATE = config('PYCHECK_KEY_ADMIN', default='pycheck')
KEY_ADMIN_PUBLIC = 'a5bd2041a4fe583cfb4782077d3054da'

USER_CONFIG = Path.home() / '.config' / 'pycheck' / 'pycheck.ini'
URL_API = config('URL_API', default='http://localhost:8000/api')

TEMPLATES_DIR = config('TEMPLATES_DIR', default=PROJECT_DIR / 'templates')
EXERCISE_TEMPLATE_NAME = config('EXERCISE_TEMPLATE_NAME', default='exercise.py')
EXERCISE_EMPTY_TEMPLATE_NAME = config('EXERCISE_TEMPLATE_NAME', default='empty_exercise.py')
EXERCISE_CONFIG_TEMPLATE_NAME = config(
    'EXERCISE_CONFIG_TEMPLATE_NAME', default='exercise_config.py'
)
EXERCISE_CONFIG_DATA_DIRNAME = config('EXERCISE_CONFIG_DATA_DIRNAME', default='data')
