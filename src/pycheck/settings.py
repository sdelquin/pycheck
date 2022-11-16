from prettyconf import config

CONFIG_BASE_PATH = config('CONFIG_BASE_PATH', default='pycheck.config')
ENTRYPOINT_NAME = config('ENTRYPOINT_NAME', default='run')
