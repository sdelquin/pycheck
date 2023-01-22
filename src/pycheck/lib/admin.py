import hashlib
import os

from jinja2 import Environment, FileSystemLoader

from pycheck import settings


def generate_exercise(name: str, topic: str):
    # Ensure extension is not included in name
    name = os.path.splitext(name)[0]
    hash = hashlib.md5(name.encode()).hexdigest()
    if (config := settings.EXERCISES_CONFIG_DIR / f'{hash}.py').exists():
        print('La configuración para este ejercicio ya existe!')
    else:
        env = Environment(loader=FileSystemLoader(settings.TEMPLATES_DIR))
        template = env.get_template(settings.EXERCISE_CONFIG_TEMPLATE_NAME)
        context = dict()
        config.write_text(template.render(context))
        with open(settings.EXERCISES_DB, 'a') as f:
            f.write(f'{name},{hash},{topic}\n')
    print(hash)
