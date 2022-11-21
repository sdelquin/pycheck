from rich.console import Console
from rich.table import Table

from pycheck import settings

from .exercise import Exercise


class Checking:
    def __init__(self, exercise: Exercise, runnings: list):
        self.exercise = exercise
        self.runnings = runnings
        self.passed = all([running['passed'] for running in self.runnings])

    def display(self):
        console = Console()
        table = Table(show_header=True)

        for param_name, _ in self.exercise.entrypoint['params']:
            table.add_column(param_name, header_style='yellow')
        for return_name, _ in self.exercise.entrypoint['return']:
            table.add_column(f'{return_name}:obj', header_style='blue')
        for return_name, _ in self.exercise.entrypoint['return']:
            table.add_column(f'{return_name}:res', header_style='cyan')
        table.add_column('Status')

        for check_case, running in zip(self.exercise.check_cases, self.runnings):
            args, expected_output = check_case
            fargs = [str(arg) for arg in args]
            fexp = [str(out) for out in expected_output]
            fout = [str(out) for out in running['output']]
            emoji = (
                settings.STATUS_PASSED_EMOJI
                if running['passed']
                else settings.STATUS_NOT_PASSED_EMOJI
            )
            table.add_row(*fargs, *fexp, *fout, emoji)

        console.print(table)
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
