from pathlib import Path

import typer
from rich import print
from rich.text import Text

import pycheck
from pycheck.lib import admin, utils
from pycheck.lib.exceptions import (
    CheckCaseNotFoundError,
    ExerciseNotAvailableError,
    TemplateNotFoundError,
)
from pycheck.lib.utils import admin_required
from pycheck.lib import auth

OK = Text("[bold green]✓ OK[/bold green]")
ERROR = Text("[bold red]✕ ERROR[/bold red]")

app = typer.Typer(
    add_completion=False,
    help='✨ pycheck es un comprobador de ejercicios escritos en Python.',
    no_args_is_help=True,
)


@app.command()
def update():
    '''Actualiza pycheck a su última versión disponible.'''
    utils.update_pycheck()


@app.command()
def check(
    name: Path = typer.Argument(
        ..., help='Nombre del ejercicio (puede ser una ruta).', show_default=False
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
        checking = pycheck.check(name, ignore_stdout, ignore_stdin, case_no)
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
    name: Path = typer.Argument(
        ..., help='Nombre del ejercicio (puede ser una ruta).', show_default=False
    ),
    args: list[str] = typer.Argument(
        None, help='Argumentos propios para ejecutar el programa.', show_default=False
    ),
):
    '''Lanza la ejecución del ejercicio con argumentos propios.'''
    try:
        result = pycheck.run(name, args)
    except TemplateNotFoundError as err:
        print(err)
    except ExerciseNotAvailableError as err:
        print(err)
    else:
        print(result)


@app.command()
def template(
    name: Path = typer.Argument(
        ..., help='Nombre del ejercicio (puede ser una ruta).', show_default=False
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
        exercise = pycheck.Exercise(name)
    except ExerciseNotAvailableError as err:
        print(err)
    else:
        exercise.create_template(ask_on_overwrite=not force)


@app.command()
def show(
    name: str = typer.Argument(..., help='Nombre del ejercicio.', show_default=False),
    description: bool = typer.Option(
        False,
        '--description',
        '-d',
        show_default=False,
        help='Muestra la descripción del ejercicio.',
    ),
    check_cases: bool = typer.Option(
        False,
        '--check-cases',
        '-c',
        show_default=False,
        help='Muestra los casos de prueba del ejercicio.',
    ),
):
    '''Muestra la especificación del ejercicio.'''
    try:
        exercise = pycheck.Exercise(name)
    except ExerciseNotAvailableError as err:
        print(err)
    else:
        if not description and not check_cases:
            description = check_cases = True
        exercise.show(description, check_cases)


@app.command()
def boot(name: str = typer.Argument(..., help='Nombre del ejercicio.', show_default=False)):
    '''Muestra la especificación del ejercicio y crea la plantilla.'''
    try:
        exercise = pycheck.Exercise(name)
    except ExerciseNotAvailableError as err:
        print(err)
    else:
        exercise.show()
        exercise.create_template()


@app.command()
def whoami():
    '''Si estás identificado, muestra tu identificador como estudiante.
    '''
    student_id = auth.get_student_id()
    print(student_id or "No estás identificado.")


@app.command()
def status():
    '''Muestra el estado de la api de pycheck.es.
    '''
    status = auth.status()
    print(status['result'])


@app.command()
def login(
        student: str = typer.Argument(
            ...,
            help='Identificador de usuario en formato <username>@<context>',
            ),
        password: str = typer.Option(
            ...,
            prompt=True,
            hide_input=True,
            ),
        ):
    '''Validarse como usuario en pycheck.es.
    '''
    username, context = student.split('@')
    is_valid, token_or_error_message = auth.login(username, context, password)
    if is_valid:
        print(
            f"{OK} [bold]{username}[/bold] Identificado correctamente"
            f" en [bold]{context}[/bold]")
    else:
        error_message = token_or_error_message
        print(f"{ERROR} Error de identificación: {error_message}")

# *************************************************
# ADMIN
# *************************************************


@app.command(hidden=True)
def generate(
    name: str = typer.Argument(..., help='Nombre del ejercicio.', show_default=False),
    topic: str = typer.Option(
        'undefined',
        '--topic',
        '-t',
        help='Tema al que se va a asignar el ejercicio.',
    ),
):
    '''Genera un nuevo ejercicio.'''
    admin_required()
    admin.generate_exercise(name, topic)


@app.command(hidden=True)
def hash(
    name: str = typer.Argument(..., help='Nombre del ejercicio.', show_default=False),
):
    '''Obtiene el hash de un ejercicio.'''
    admin_required()
    print(utils.gen_hash(Path(name).stem))


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
