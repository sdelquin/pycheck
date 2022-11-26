TITLE = 'Baricentro de un triángulo'

DESCRIPTION = '''
Dado un triángulo definido por sus tres extremos A, B y C (x,y para cada punto), calcule su baricentro utilizando la siguiente fórmula:

```
     x  + x  + x
      A    B    C
x  = ────────────
 0         3

     y  + y  + y
      A    B    C
y  = ────────────
 0         3
```

Consulte [la imagen del triángulo aquí](https://i.imgur.com/hpDQY8o.png?1).
Calcule el resultado **redondeando a 4 decimales**.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['A', list],
        ['B', list],
        ['C', list],
    ],
    'RETURN': [
        ['x0', float],
        ['y0', float],
    ],
}

CHECK_CASES = [
    [[[4, 6], [12, 4], [10, 10]], [8.6667, 6.6667]],
    [[[4, 2], [12, 2], [6, 10]], [7.3333, 4.6667]],
]

SOURCE = 'https://www.codewars.com/kata/5601c5f6ba804403c7000004'
