TITLE = 'Separando recurso Samba'

DESCRIPTION = """
Dada una ruta remota de recurso [samba](https://es.wikipedia.org/wiki/Samba_(software)) debe separar el nombre del equipo (IP) y la ruta.
"""

ENTRYPOINT = {
    'PARAMS': [
        ['smb_path', str],
    ],
    'RETURN': [
        ['host', str],
        ['path', str],
    ],
}

CHECK_CASES = [
    [['//1.1.1.1/aprende/python'], ['1.1.1.1', '/aprende/python']],
    [['//samba-server/psf/guido'], ['samba-server', '/psf/guido']],
    [['//8.6.4.2/data/work/upload/'], ['8.6.4.2', '/data/work/upload/']],
]
