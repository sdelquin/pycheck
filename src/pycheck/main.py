import typer

from pycheck import PyCheck
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
        pychecker = PyCheck(filepath)
        if list_cases:
            pychecker.list_cases()
        if create_template:
            pychecker.create_template()
        if run:
            pychecker.run(args)
        if check:
            pychecker.check()


if __name__ == "__main__":
    app()
