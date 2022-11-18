import subprocess
import sys

import pkg_resources

from pycheck import settings


def update_pycheck():
    url = f'git+{settings.GITHUB_REPO}'
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', url])


def get_pycheck_version():
    return pkg_resources.get_distribution('pycheck').version
