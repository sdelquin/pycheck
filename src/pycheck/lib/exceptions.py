class ExerciseNotAvailableError(Exception):
    def __init__(self, exercise):
        message = f"""El ejercicio '{exercise.id}' no está disponible.
Revise el nombre y si el problema persiste consulte al profesorado.
Puede actualizar la aplicación usando: 'pycheck update'"""
        super().__init__(message)


class TemplateNotFoundError(Exception):
    def __init__(self, exercise):
        message = f"""No se encuentra la plantilla para el ejercicio '{exercise}'.
Revise el nombre del ejercicio y si está trabajando en la carpeta adecuada.
Puede generar la plantilla usando: 'pycheck template {exercise}'"""
        super().__init__(message)


class CheckCaseNotFoundError(Exception):
    def __init__(self, exercise, case_no):
        message = (
            f"No se encuentra el caso de prueba {case_no} para el ejercicio '{exercise}'"
        )
        super().__init__(message)


class NotAuthorizedError(Exception):
    def __init__(self):
        super().__init__('Usted no está autorizado para acceder a este recurso.')
