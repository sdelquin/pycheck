import importlib
import re


def get_config(exercise_id: str):
    module_path, exercise_slug = re.match(r'^(.*)\.([^.]+)+$', exercise_id).groups()
    module_path = f'pycheck.config.{module_path}'
    module = importlib.import_module(module_path)
    return getattr(module, exercise_slug)
