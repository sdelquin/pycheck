from typing import get_type_hints


def get_arg_casts(func: callable):
    arg_casts = []
    for param_name, param_type in get_type_hints(func).items():
        if param_name != 'return':
            cast = param_type if param_type in [int, bool, float, str] else eval
            arg_casts.append(cast)
    return arg_casts
