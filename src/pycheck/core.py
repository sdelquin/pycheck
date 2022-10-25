from pycheck import utils


def check(exercise_id: str, argv: list, target_func: callable):
    exercise_cfg = utils.get_config(exercise_id)
    if argv[1].strip() == '-k':
        utils.run_cases(exercise_cfg['cases'], target_func)
    else:
        utils.run_custom(exercise_cfg['arg_casts'], argv[1:], target_func)
