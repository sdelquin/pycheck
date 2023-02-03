from pathlib import Path

TITLE = 'Suma criptográfica'

DESCRIPTION = '''
Dado un fichero de entrada en el que vienen una serie de códigos encriptados, debemos desencriptar dichos códigos y ser capaces de realizar la suma de todos los valores.

Ejemplo de fichero de entrada:
```
sdhjwshjvoghmcrh
uvghvoaxaxwbmcetws
sduvhjhjvopket
```

Cada línea representa un número, y los códigos criptográficos siguen la siguiente tabla:

```
+----+---+
| sd | - |
| vo | . |
| ax | 0 |
| gh | 1 |
| hj | 2 |
| uv | 3 |
| ws | 4 |
| pk | 5 |
| et | 6 |
| mc | 7 |
| rh | 8 |
| wb | 9 |
+----+---+
```

Notas:
- Todos los códigos criptográficos siempre ocupan 2 caracteres.
- Si aparece un código criptográfico que no existe en la tabla se debe ignorar.
- Trabaje siempre con **valores flotantes**.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['crypto_path', Path],
    ],
    'RETURN': [
        ['sum_cr', float],
    ],
}

CHECK_CASES = [
    [['data/sum_crypto/data1.crypto'], [-533.728236]],
    [['data/sum_crypto/data2.crypto'], [5689.511]],
    [['data/sum_crypto/data3.crypto'], [-7587.0658]],
]
