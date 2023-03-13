from pycheck.lib.runner import Runner

TITLE = 'Una media muy sencilla'

DESCRIPTION = '''
Dados dos valores de entrada calcula la media.
'''

runner = Runner('simple_mean', 'calc_mean')

CHECKS = [
    runner.with_params(a=120, b=7).validate_returns(63.5),
    runner.with_params(a=3, b=5).validate_returns(4.0),
    runner.with_params(a=3, b=33).validate_returns(18.0),
]
