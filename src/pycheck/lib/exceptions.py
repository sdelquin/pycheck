class ExerciseNotAvailableError(Exception):
    def __init__(self, filename: str):
        message = f"""El ejercicio '{filename}' no está disponible.
Revise el nombre del fichero. Si el problema persiste consulte al profesorado."""
        super().__init__(message)


class TemplateNotFoundError(Exception):
    def __init__(self, filepath: str):
        message = f"""No se encuentra la plantilla para el ejercicio '{filepath}'.
Revise el nombre del ejercicio y si está trabajando en la carpeta adecuada.
Puede generar la plantilla usando: 'pycheck template {filepath}'"""
        super().__init__(message)


class CheckCaseNotFoundError(Exception):
    def __init__(self, case_no: int, filename: str):
        message = (
            f"No se encuentra el caso de prueba {case_no} para el ejercicio '{filename}'"
        )
        super().__init__(message)


class NotAuthorizedError(Exception):
    def __init__(self):
        super().__init__('Usted no está autorizado para acceder a este recurso.')
