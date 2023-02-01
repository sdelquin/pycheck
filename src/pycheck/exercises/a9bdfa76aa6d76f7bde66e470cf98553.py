from pathlib import Path

TITLE = 'Yellow Submarine'

DESCRIPTION = '''
Tenemos un submarino que se mueve en "x" (distancia) y en "y" (profundidad). Los movimientos del submarino vienen definidos en un fichero de entrada con el formato:
```
<Litros de combustible>
<X>:<Y>,<X>:<Y>,...
```
El submarino empieza en distancia 0 y profundidad 0, y se va moviendo en función de lo especificado en el fichero de entrada. _Ojo porque en la profundidad un valor positivo implica "descender" y un valor negativo implica "ascender"_.

El objetivo es encontrar las siguiente 3 variables finales: **distancia, profundidad y combustible.**

Notas:
- El consumo del submarino es de 3 litros por metro (de distancia).
- Si el submarino agota el combustible se debe parar.
- Si el submarino trata de "subir" de profundidad 0 se debe parar.
- Si el submarino trata de "bajar" de profundidad 600m se debe parar.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['route_path', Path],
    ],
    'RETURN': [
        ['distance', int],
        ['depth', int],
        ['fuel', int],
    ],
}

CHECK_CASES = [
    [['data/submarine/route1.dat'], [320, 151, 740]],
    [['data/submarine/route2.dat'], [60, 64, 0]],
    [['data/submarine/route3.dat'], [60, -1, 820]],
    [['data/submarine/route4.dat'], [176, 601, 2792]],
]
