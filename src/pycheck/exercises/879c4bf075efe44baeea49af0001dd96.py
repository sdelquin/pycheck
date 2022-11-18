DESCRIPTION = '''
Una ecuación de segundo grado se define como ax^2 + bx + c = 0 y, (en determinados casos)
tiene dos soluciones:
             ________
            ╱ 2      
     -b + ╲╱ b  - 4ac
x  = ────────────────
 1          2a       
             ________
            ╱ 2      
     -b - ╲╱ b  - 4ac
x  = ────────────────
 2          2a       

Escriba un programa en Python que calcule estas dos soluciones. Tenga en cuenta subdividir
los cálculos y reutilizar variables, por ejemplo el dicriminante [https://bit.ly/3OcZSuN].
'''

ENTRYPOINT = {
    'PARAMS': [
        ['a', int],
        ['b', int],
        ['c', int],
    ],
    'RETURN': [
        ['x1', float],
        ['x2', float],
    ],
}

CHECK_CASES = [
    [[4, -6, 2], [1.0, 0.5]],
    [[1, 2, -3], [1.0, -3.0]],
    [[-1, -2, 8], [-4.0, 2.0]],
]
