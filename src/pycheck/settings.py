from prettyconf import config

CONFIG_BASE_PATH = config('CONFIG_BASE_PATH', default='pycheck.config')
ENTRYPOINT_NAME = config('ENTRYPOINT_NAME', default='run')
GITHUB_REPO = config('GITHUB_REPO', default='https://github.com/sdelquin/pycheck.git')
