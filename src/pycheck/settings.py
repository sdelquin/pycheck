from pathlib import Path

from prettyconf import config

PROJECT_DIR = Path(__file__).parent.parent.parent

CONFIG_BASE_PATH = config('CONFIG_BASE_PATH', default='pycheck.config')
ENTRYPOINT_NAME = config('ENTRYPOINT_NAME', default='run')
GITHUB_REPO = config('GITHUB_REPO', default='https://github.com/sdelquin/pycheck.git')
PYPROJECT_PATH = config('PYPROJECT_PATH', default=PROJECT_DIR / 'pyproject.toml')
