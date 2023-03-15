TITLE = 'Suma de cocientes'

DESCRIPTION = '''
Escriba una función **recursiva** que calcule la suma de cocientes de un número.

La suma de cocientes un número entero _n_ se define como:
```
  n                          
____                         
╲                            
 ╲    1       1   1         1
 ╱    ─ = 1 + ─ + ─ + ... + ─
╱     k       2   3         n
‾‾‾‾                         
k = 1                        
```
Por ejempo, si _n=4_ entonces la suma de cocientes quedaría como: _1 + 1/2 + 1/3 + 1/4_

Tenga en cuenta que n >= 1
'''

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'sum_quot',
    'PARAMS': [
        ['n', int],
    ],
    'RETURN': [
        ['squot', float],
    ],
}

CHECK_CASES = [
    [[1], [1]],
    [[5], [2.283333333333333]],
    [[6], [2.4499999999999997]],
    [[7], [2.5928571428571425]],
    [[8], [2.7178571428571425]],
    [[9], [2.8289682539682537]],
    [[10], [2.9289682539682538]],
]
