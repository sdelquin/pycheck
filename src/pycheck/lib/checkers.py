import filecmp
import os
from pathlib import Path


def check_file_as_expected(file: str) -> bool:
    '''Comprueba que el contenido del fichero sea correcto.'''
    expected_file = Path(file).with_name('.expected')
    return filecmp.cmp(file, expected_file, shallow=False)


def check_file_exists(file: str) -> bool:
    '''Comprueba que el fichero existe.'''
    return os.path.exists(file)
