TITLE = 'Fibonacci recursivo'

DESCRIPTION = """
Usando una **función recursiva**, encuentre el enésimo término de la [Sucesión de Fibonacci](https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci).

Por ejemplo, si _n = 10_ habría que devolver el valor 55 ya que es el que ocupa la posición _10_ en la Sucesión de Fibonacci.

Notas:
- La "primera" posición sería la 0, es decir _n = 0_.
"""

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'fibonacci',
    'PARAMS': [
        ['n', int],
    ],
    'RETURN': [
        ['fibo', int],
    ],
}

CHECK_CASES = [
    [[0], [0]],
    [[1], [1]],
    [[2], [1]],
    [[10], [55]],
    [[20], [6765]],
]
