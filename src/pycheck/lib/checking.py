from rich.console import Console
from rich.table import Table

from pycheck import settings

from .exercise import Exercise


class Checking:
    def __init__(self, exercise: Exercise, runnings: list):
        self.exercise = exercise
        self.runnings = runnings
        self.passed = all([running['passed'] for running in self.runnings])

    def display(self, only_summary=False):
        console = Console()
        table = Table(show_header=True)

        if not only_summary:
            table.add_column('#', header_style='grey42', style='grey42')
            for param_name, _ in self.exercise.entrypoint['params']:
                heading = f'[italic](entrada)[/]\n{param_name}'
                table.add_column(heading, header_style='yellow')
            for return_name, _ in self.exercise.entrypoint['return']:
                heading = f'[italic](esperado)[/]\n{return_name}'
                table.add_column(heading, header_style='blue')
            for return_name, _ in self.exercise.entrypoint['return']:
                heading = f'[italic](obtenido)[/]\n{return_name}'
                table.add_column(heading, header_style='cyan')
            table.add_column('Status')

            case_start = 1 if self.exercise.case_no == 0 else self.exercise.case_no
            for case_no, (check_case, running) in enumerate(
                zip(self.exercise.check_cases, self.runnings), start=case_start
            ):
                args, expected_output = check_case
                case = str(case_no)
                fargs = [str(arg) for arg in args]
                fexp = [str(out) for out in expected_output]
                fout = [str(out) for out in running['output']]
                emoji = (
                    settings.STATUS_PASSED_EMOJI
                    if running['passed']
                    else settings.STATUS_NOT_PASSED_EMOJI
                )
                table.add_row(case, *fargs, *fexp, *fout, emoji)

            console.print(table)

        if self.exercise.case_no == 0:
            if self.passed:
                console.print(
                    f'{settings.MSG_PASSED_EMOJI} ¡Enhorabuena! Todo funciona bien',
                    style='bold green',
                )
            else:
                console.print(
                    f'{settings.MSG_NOT_PASSED_EMOJI} ¡Atención! Hay errores en '
                    'algunos casos de prueba',
                    style='bold red',
                )
