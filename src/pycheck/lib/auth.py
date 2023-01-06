import configparser
import json
import os
import urllib.request

from pycheck import settings
from pycheck.lib import api


def get_student_id():
    filename = settings.USER_CONFIG
    if filename.exists():
        user_config = configparser.ConfigParser()
        with open(filename, 'r') as user_config_file:
            user_config.read_file(user_config_file)
            username = user_config.get('auth', 'username')
            context = user_config.get('auth', 'context')
            return f"{username}@{context}"
    return None


def status():
    return api.api_get(api.URL_STATUS)


def login(username: str, context: str, password: str) -> tuple[bool, str]:
    '''Validarse como usuario en pycheck.es.
    '''
    response = api.api_post(
        api.URL_LOGIN,
        username=username,
        context=context,
        password=password,
        )
    if response['status'] == 'ok':
        token = response['result']
        user_config = configparser.ConfigParser()
        user_config['auth'] = {
            'username': username,
            'context': context,
            'token': token,
            }
        filename = settings.USER_CONFIG
        os.makedirs(filename.parent, exist_ok=True)
        with open(settings.USER_CONFIG, 'w') as user_config_file:
            user_config.write(user_config_file)
        return True, token
    else:
        error_message = response['message']
        return False, error_message
