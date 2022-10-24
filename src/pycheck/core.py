from pycheck.config import CONFIG


def check(exercise_id: str, argv: list, target_func: callable):
    exercise_cfg = CONFIG[exercise_id]
    if argv[1].strip() == '-k':
        for __args, __expected_output in CONFIG[exercise_id]['cases']:
            if (__output := target_func(*__args)) != __expected_output:
                print(f'❌ No funciona para la entrada {__args}')
                print(f'   Salida esperada: {__expected_output}')
                print(f'   Salida obtenida: {__output}')
                break
        else:
            print('✅ ¡Enhorabuena! Todo funciona bien')
    else:
        __args = [cast(arg) for cast, arg in zip(exercise_cfg['arg_casts'], argv[1:])]
        if (__result := target_func(*__args)) is not None:
            print(__result)
