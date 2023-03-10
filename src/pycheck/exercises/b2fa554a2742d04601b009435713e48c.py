TITLE = 'Encuentra la integral'

DESCRIPTION = '''
La entrada será una cadena de texto con dos números separados por una coma. El primer número es el _coeficiente_ y el segundo número es el _exponente_. Por ejemplo:
```
3,2 --> 3x^2
```
Para obtener la integral tenemos que añadir 1 al _exponente_ y dividir el _coeficiente_ por dicho número. En el ejemplo anterior:
```
3x^2 --> 1x^3
```
'''

ENTRYPOINT = {
    'PARAMS': [
        ['symbol', str],
    ],
    'RETURN': [
        ['integral', str],
    ],
}

CHECK_CASES = [
    [['3,2'], ['1x^3']],
    [['12,5'], ['2x^6']],
    [['20,1'], ['10x^2']],
    [['40,3'], ['10x^4']],
    [['90,2'], ['30x^3']],
]

SOURCE = 'https://www.codewars.com/kata/59811fd8a070625d4c000013'
