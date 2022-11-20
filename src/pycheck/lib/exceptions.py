class ExerciseNotFoundError(Exception):
    def __init__(self, filename: str):
        message = f"El ejercicio '{filename}' no está disponible"
        super().__init__(message)


class TemplateNotFoundError(Exception):
    def __init__(self, filename: str):
        message = f"""No se encuentra plantilla para el ejercicio '{filename}'.
Puede generarla con 'pycheck -t {filename}'"""
        super().__init__(message)
