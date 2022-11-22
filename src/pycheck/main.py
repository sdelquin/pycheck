import typer

import pycheck
from pycheck.lib import utils

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
    filepath: str = typer.Argument(
        ..., help='Ruta al ejercicio que se quiere comprobar.', show_default=False
    ),
):
    '''Comprueba el ejercicio contra los casos de prueba establecidos.'''
    checking = pycheck.check(filepath)
    checking.display()


@app.command()
def run(
    filepath: str = typer.Argument(
        ..., help='Ruta al ejercicio que se quiere ejecutar.', show_default=False
    ),
    args: list[str] = typer.Argument(
        None, help='Argumentos propios para ejecutar el programa.', show_default=False
    ),
):
    '''Lanza la ejecución del ejercicio con argumentos propios.'''
    exercise = pycheck.Exercise(filepath)
    print(pycheck.run(exercise, args))


@app.command()
def template(
    filepath: str = typer.Argument(
        ..., help='Identificador del ejercicio.', show_default=False
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
    exercise = pycheck.Exercise(filepath)
    exercise.create_template(ask_on_overwrite=not force)


@app.command()
def show(
    filepath: str = typer.Argument(
        ..., help='Identificador del ejercicio.', show_default=False
    ),
):
    '''Muestra la especificación del ejercicio.'''
    exercise = pycheck.Exercise(filepath)
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
