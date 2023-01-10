import configparser
import os

from pycheck import settings
from pycheck.lib import api


def get_student_id():
    if (filename := settings.USER_CONFIG).exists():
        user_config = configparser.ConfigParser()
        with open(filename, 'r') as user_config_file:
            user_config.read_file(user_config_file)
            username = user_config.get('auth', 'username')
            context = user_config.get('auth', 'context')
            return f'{username}@{context}'
    return None


def status():
    return api.api_get(api.URL_STATUS)


def login(username: str, context: str, password: str) -> tuple[bool, str]:
    '''Validarse como usuario en pycheck.es.
    Devuelve una tupla con dos elementos:
    - El primer elemento indica si se ha logeado correctamente.
    - El segundo elemento depende del valor del primero:
      - Si el login ha sido correcto, este valor contiene el token de autenticación.
      - Si el login ha sido incorrecto, este valor contiene el mensaje de error.
    '''
    response = api.api_post(
        api.URL_LOGIN,
        username=username,
        context=context,
        password=password,
    )
    if response['status'] == api.STATUS_OK:
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
