TITLE = 'Reorganizando fechas'

DESCRIPTION = """
Transforme una fecha de entrada en otra de salida pero modificando su formato.

Notas:
- Formato de fecha de entrada: <mes>/<día>/<año-con-2-cifras>
- Formato de fecha de salida: <día>-<mes>-<año-con-4-cifras>
- Las fechas son _cadenas de caracteres_
- Habrá otro parámetro de entrada indicando el año base (_entero_)
"""

ENTRYPOINT = {
    'PARAMS': [
        ['input_date', str],
        ['base_year', int],
    ],
    'RETURN': [
        ['output_date', str],
    ],
}

CHECK_CASES = [
    [['12/31/23', 2000], ['31-12-2023']],
    [['2/21/15', 1800], ['21-02-1815']],
    [['10/1/87', 1900], ['01-10-1987']],
    [['9/29/1', 1700], ['29-09-1701']],
]
