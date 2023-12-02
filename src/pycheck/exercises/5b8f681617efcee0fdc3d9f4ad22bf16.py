TITLE = 'Comprobando igualdad de potencias'

DESCRIPTION = """
Dado un valor entero positivo _n_ compruebe que se cumple la siguiente igualdad:
```
         2           
⎛  n    ⎞      n     
⎜ ___   ⎟     ___    
⎜ ╲     ⎟     ╲     3
⎜ ╱    k⎟  =  ╱    k 
⎜ ‾‾‾   ⎟     ‾‾‾    
⎝k = 1  ⎠    k = 1   
```

→ **El objetivo es calcular ambos lados de la igualdad**. Por ejemplo, para _n=3_ se cumple:
```
           2    3    3    3
(1 + 2 + 3)  = 1  + 2  + 3 
```

"""

ENTRYPOINT = {
    'PARAMS': [
        ['n', int],
    ],
    'RETURN': [
        ['left_side', int],
        ['right_side', int],
    ],
}

CHECK_CASES = [
    [[1], [1, 1]],
    [[2], [9, 9]],
    [[3], [36, 36]],
    [[4], [100, 100]],
    [[5], [225, 225]],
]
