import os
import pathlib
import sys
from typing import Any

from pycheck.lib.exercise import Exercise


class Runner:
    def __init__(
        self,
        exercise_name: str,
        entrypoint: str,
        parameters: dict = None,
        outcome: Any = None,
        validations: list = None,
    ):
        self.exercise_name = exercise_name
        self.entrypoint = entrypoint
        self.parameters = parameters or {}
        self.outcome = outcome
        self.validations = validations or []

    def with_params(self, **kwargs):
        return Runner(
            self.exercise_name, self.entrypoint, kwargs, self.outcome, self.validations
        )

    def validate_returns(self, *args):
        items = args[:]
        if len(items) == 1:
            expected = items[0]
        else:
            expected = tuple(items)

        def _inner_validation(result):
            if result == expected:
                return (
                    True,
                    f'Expected {expected}, got {result}: [bold][green]{expected}'
                    f' == {result}[/]',
                )
            return (
                False,
                f'Expected {expected} got {result}: [bold][red]{expected} != {result}[/]',
            )

        validations = self.validations.copy()
        validations.append(_inner_validation)
        return Runner(
            self.exercise_name, self.entrypoint, self.parameters, self.outcome, validations
        )

    def validate_folder_exists(self, folder_name):
        def _inner_validation(result):
            if os.path.exists(folder_name):
                return True, f'La carpeta {folder_name} existe'
            return False, f'Debería existir la carpeta {folder_name}, pero no'

        validations = self.validations.copy()
        validations.append(_inner_validation)
        return Runner(
            self.exercise_name, self.entrypoint, self.parameters, self.outcome, validations
        )

    def checks(self):
        exercise = Exercise(self.exercise_name)
        target = exercise.get_target(entrypoint=self.entrypoint)
        try:
            result = target(**self.parameters)
        except Exception as err:
            _exc_type, _exc_obj, exc_tb = sys.exc_info()
            fname = pathlib.Path(exc_tb.tb_frame.f_code.co_filename)
            line = exc_tb.tb_lineno
            yield False, f'Error en {fname.name}:{line} {err}'
        else:
            for validation in self.validations:
                yield validation(result)

    def entrypoints(self):
        result = {}
        result['PARAMS'] = [
            (name, type(value).__name__) for name, value in self.parameters.items()
        ]
        result['RETURN'] = [
            (name, type(value).__name__) for name, value in self.outcome.items()
        ]
        return result
