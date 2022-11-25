import hashlib
import subprocess
import sys

import pkg_resources

from pycheck import settings

from .exceptions import NotAuthorizedError


def update_pycheck():
    url = f'git+{settings.GITHUB_REPO}'
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', url])


def get_pycheck_version():
    return pkg_resources.get_distribution('pycheck').version


def admin_required():
    key_hash = hashlib.md5(settings.KEY_ADMIN_PRIVATE.encode()).hexdigest()
    if key_hash != settings.KEY_ADMIN_PUBLIC:
        raise NotAuthorizedError()
