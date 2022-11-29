from pathlib import Path

import typer
from rich import print

import pycheck
from pycheck.lib import admin, utils
from pycheck.lib.exceptions import (
    CheckCaseNotFoundError,
    ExerciseNotAvailableError,
    TemplateNotFoundError,
)
from pycheck.lib.utils import admin_required

app = typer.Typer(
    add_completion=False,
    help='✨ pycheck es un comprobador de ejercicios escritos en Python.',
)


@app.command()
def update():
    '''Actualiza pycheck a su última versión disponible.'''
    utils.update_pycheck()


@app.command()
def check(
    filepath: Path = typer.Argument(
        ..., help='Ruta al ejercicio que se quiere comprobar.', show_default=False
    ),
    only_summary: bool = typer.Option(
        False,
        '--only-summary',
        '-s',
        show_default=False,
        help='Muestra únicamente el resumen como salida de la comprobación.',
    ),
    ignore_stdout: bool = typer.Option(
        False,
        '--ignore-stdout',
        '-z',
        show_default=False,
        help='Ignora los mensajes enviados a stdout al ejecutar el ejercicio.',
    ),
    ignore_stdin: bool = typer.Option(
        False,
        '--ignore-stdin',
        '-a',
        show_default=False,
        help='Ignora la entrada por stdin al ejecutar el ejercicio.',
    ),
    case_no: int = typer.Option(
        0,
        '--case-no',
        '-n',
        min=0,
        help='Número de caso a ejecutar. Con valor 0 se ejecutarán todos los casos.',
    ),
):
    '''Comprueba el ejercicio contra los casos de prueba establecidos.'''
    try:
        checking = pycheck.check(filepath, ignore_stdout, ignore_stdin, case_no)
    except TemplateNotFoundError as err:
        print(err)
    except ExerciseNotAvailableError as err:
        print(err)
    except CheckCaseNotFoundError as err:
        print(err)
    else:
        checking.show(only_summary)


@app.command()
def run(
    filepath: Path = typer.Argument(
        ..., help='Ruta al ejercicio que se quiere ejecutar.', show_default=False
    ),
    args: list[str] = typer.Argument(
        None, help='Argumentos propios para ejecutar el programa.', show_default=False
    ),
):
    '''Lanza la ejecución del ejercicio con argumentos propios.'''
    try:
        result = pycheck.run(filepath, args)
    except TemplateNotFoundError as err:
        print(err)
    except ExerciseNotAvailableError as err:
        print(err)
    else:
        print(result)


@app.command()
def template(
    filepath: Path = typer.Argument(
        ..., help='Ruta en la que crear la plantilla para el ejercicio.', show_default=False
    ),
    force: bool = typer.Option(
        False,
        '--force',
        '-f',
        show_default=False,
        help='Fuerza la creación de la plantilla, incluso si ya existe el fichero.',
    ),
):
    '''Crea la plantilla para resolver el ejercicio.'''
    try:
        exercise = pycheck.Exercise(filepath)
    except ExerciseNotAvailableError as err:
        print(err)
    else:
        exercise.create_template(ask_on_overwrite=not force)


@app.command()
def show(
    filepath: str = typer.Argument(
        ..., help='Identificador del ejercicio.', show_default=False
    ),
    description: bool = typer.Option(
        False,
        '--description',
        '-d',
        show_default=False,
        help='Mostrar la descripción del ejercicio.',
    ),
    check_cases: bool = typer.Option(
        False,
        '--check-cases',
        '-c',
        show_default=False,
        help='Mostrar los casos de prueba del ejercicio.',
    ),
):
    '''Muestra la especificación del ejercicio.'''
    try:
        exercise = pycheck.Exercise(filepath)
    except ExerciseNotAvailableError as err:
        print(err)
    else:
        if not description and not check_cases:
            description = check_cases = True
        exercise.show(description, check_cases)


@app.command(hidden=True)
def generate(
    exercise_id: str = typer.Argument(
        ..., help='Identificador del ejercicio.', show_default=False
    ),
    category: str = typer.Option(
        'undefined',
        '--categoría',
        '-c',
        help='Categoría que se va a asignar al ejercicio.',
    ),
    test: bool = typer.Option(
        False,
        '--test',
        '-t',
        help='Indica si el ejercicio es para examen.',
    ),
):
    '''Genera un nuevo ejercicio.'''
    admin_required()
    admin.generate_exercise(exercise_id, category, int(test))


@app.command(hidden=True)
def hash(
    exercise_id: str = typer.Argument(
        ..., help='Identificador del ejercicio.', show_default=False
    ),
):
    '''Obtiene el hash de un ejercicio.'''
    admin_required()
    print(utils.hash(Path(exercise_id).stem))


@app.callback(invoke_without_command=True)
def init(
    version: bool = typer.Option(
        False,
        '--version',
        show_default=False,
        help='Muestra la versión de pycheck instalada en el sistema.',
    ),
):
    if version:
        print(utils.get_pycheck_version())


if __name__ == "__main__":
    app()
