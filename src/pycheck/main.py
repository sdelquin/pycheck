import typer

import pycheck
from pycheck.lib import utils

app = typer.Typer(add_completion=False)


@app.command()
def run(
    filepath: str = typer.Argument(None, help='Ruta al programa que se quiere comprobar.'),
    args: list[str] = typer.Argument(
        None, help='Argumentos propios para ejecutar el programa.'
    ),
    list_cases: bool = typer.Option(
        False,
        '--list-cases',
        '-l',
        show_default=False,
        help='Muestra los casos de prueba establecidos.',
    ),
    description: bool = typer.Option(
        False,
        '--description',
        '-d',
        show_default=False,
        help='Muestra la descripción del problema.',
    ),
    create_template: bool = typer.Option(
        False,
        '--template',
        '-t',
        show_default=False,
        help='Crea la plantilla para resolver el problema.',
    ),
    run: bool = typer.Option(
        False,
        '--run',
        '-r',
        show_default=False,
        help='Ejecuta el programa con argumentos propios.',
    ),
    check: bool = typer.Option(
        False,
        '--check',
        '-c',
        show_default=False,
        help='Ejecuta el programa contra los casos de prueba.',
    ),
    update: bool = typer.Option(
        False,
        '--update',
        '-u',
        show_default=False,
        help='Actualiza pycheck a su última versión disponible.',
    ),
    version: bool = typer.Option(
        False,
        '--version',
        '-v',
        show_default=False,
        help='Muestra la versión de pycheck instalada en el sistema.',
    ),
):
    if update:
        utils.update_pycheck()
    elif version:
        print(utils.get_pycheck_version())
    else:
        exercise = pycheck.Exercise(filepath)
        if create_template:
            exercise.create_template()
        if description:
            print(exercise.description)
        if list_cases:
            exercise.list_cases()
        if check:
            checking = pycheck.check(filepath)
            checking.display()
        if run:
            print(pycheck.run(filepath, args))


if __name__ == "__main__":
    app()
