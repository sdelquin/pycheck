import hashlib
import subprocess
import sys

import pkg_resources
from rich import print

from pycheck import settings

from .exceptions import NotAuthorizedError


def update_pycheck():
    url = f'git+{settings.GITHUB_REPO}'
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', url])


def get_pycheck_version():
    return pkg_resources.get_distribution('pycheck').version


def admin_required():
    key_hash = gen_hash(settings.KEY_ADMIN_PRIVATE)
    if key_hash != settings.KEY_ADMIN_PUBLIC:
        raise NotAuthorizedError()


def gen_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()


def succ_msg(text: str):
    print(f'[green]{settings.SUCCESS_MSG_EMOJI}[/] {text}')


def err_msg(text: str):
    print(f'[red]{settings.ERROR_MSG_EMOJI}[/] {text}')


def warn_msg(text: str):
    print(f'[yellow]{settings.WARNING_MSG_EMOJI}[/] {text}')
