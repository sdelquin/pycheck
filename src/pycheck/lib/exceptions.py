class ExerciseNotFoundError(Exception):
    def __init__(self, filename: str):
        message = f"El ejercicio '{filename}' no está disponible"
        super().__init__(message)
