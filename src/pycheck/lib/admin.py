import hashlib
import os

from pycheck import settings


def generate_exercise(name: str, topic: str):
    # Ensure extension is not included in name
    name = os.path.splitext(name)[0]
    hash = hashlib.md5(name.encode()).hexdigest()
    if (config := settings.EXERCISES_CONFIG_PATH / f'{hash}.py').exists():
        print('La configuración para este ejercicio ya existe!')
    else:
        config.write_text(settings.EXERCISES_CONFIG_TEMPLATE.lstrip())
        with open(settings.EXERCISES_DB, 'a') as f:
            f.write(f'{name},{hash},{topic}\n')
    print(hash)
