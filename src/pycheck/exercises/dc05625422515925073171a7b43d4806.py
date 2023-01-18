TITLE = 'Movimientos de inventario'

DESCRIPTION = '''
Somos responsables del **inventario de una empresa**. A final de mes nos llega una _cadena de texto_ indicando los movimientos del inventario.
Esta cadena de texto tiene el formato siguiente:
```
<mov_art>,<mov_art>,<mov_art>,...
```
El objetivo es saber el estado final del inventario de cada artículo a través de un diccionario donde las **claves** son los artículos y los **valores** son la cantidad de artículos existentes.

Notas:
- El inventario puede quedar en números negativos.
- Los nombres de los artículos son letras (cadenas de texto de 1 caracter).
- Las modificaciones de inventario siempre son números enteros (pueden ser negativos).
'''

ENTRYPOINT = {
    'PARAMS': [
        ['imoves', str],
    ],
    'RETURN': [
        ['inventory', dict],
    ],
}

CHECK_CASES = [
    [['A1,B4,A-2,A7,B1,C4'], [{'A': 6, 'B': 5, 'C': 4}]],
    [['X2,Y9,Z3,Y-2,Z-4,Y3,X-8,W5'], [{'X': -6, 'Y': 10, 'Z': -1, 'W': 5}]],
    [['R-2,S0,S2,S-8,R21,R-3,S11,R4'], [{'R': 20, 'S': 5}]],
]
