class ExerciseNotAvailableError(Exception):
    def __init__(self, filename: str):
        message = f"""El ejercicio '{filename}' no está disponible.
Revise el nombre del fichero. Si el problema persiste consulte al profesorado."""
        super().__init__(message)


class TemplateNotFoundError(Exception):
    def __init__(self, filepath: str):
        message = f"""No se encuentra la plantilla para el ejercicio '{filepath}'.
Puede generarla usando: 'pycheck template {filepath}'"""
        super().__init__(message)
