import hashlib
import os

from pycheck import settings


def generate_exercise(exercise_id: str, category: str, test: int):
    # Ensure extension is not included in filename
    exercise_id = os.path.splitext(exercise_id)[0]
    hash = hashlib.md5(exercise_id.encode()).hexdigest()
    if (config := settings.EXERCISES_CONFIG_PATH / f'{hash}.py').exists():
        print('La configuración para este ejercicio ya existe!')
    else:
        config.write_text(settings.EXERCISES_CONFIG_TEMPLATE.lstrip())
        with open(settings.EXERCISES_DB, 'a') as f:
            f.write(f'{exercise_id},{hash},{category},{test}\n')
    print(hash)
