from pathlib import Path

import typer
from rich import print

import pycheck
from pycheck.lib import utils
from pycheck.lib.exceptions import ExerciseNotAvailableError, TemplateNotFoundError

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
):
    '''Comprueba el ejercicio contra los casos de prueba establecidos.'''
    try:
        checking = pycheck.check(filepath)
    except TemplateNotFoundError as err:
        print(err)
    except ExerciseNotAvailableError as err:
        print(err)
    else:
        checking.display()


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
):
    '''Muestra la especificación del ejercicio.'''
    try:
        exercise = pycheck.Exercise(filepath)
    except ExerciseNotAvailableError as err:
        print(err)
    else:
        exercise.show()


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
