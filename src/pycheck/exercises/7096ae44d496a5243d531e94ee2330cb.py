TITLE = 'Asegurando argumentos positivos'

DESCRIPTION = """
Escriba un decorador _assert_positive()_ que asegure que todos los argumentos **numéricos** de la función decorada son positivos. En el caso de que no lo sean habrá que devolver _0_.

Aplique este decorador a la función _factorial()_ que calcula el factorial de un número.

Notas:
- Aunque _factorial()_ sólo recibe un argumento, el decorador debe funcionar para funciones con cualquier número de argumentos, tanto posicionales como nominales.
- La comprobación de ser positivo sólo se aplica para el caso de argumentos numéricos.
- No hay que comprobar si _n > 0_ en la función _factorial()_. De esto se debe encargar el decorador.
"""

EMPTY_TEMPLATE = True

ENTRYPOINT = {
    'NAME': 'factorial',
    'PARAMS': [
        ['n', int],
    ],
    'RETURN': [
        ['fact', int],
    ],
}

CHECK_CASES = [
    [[5], [120]],
    [[-5], [0]],
    [[9], [362880]],
    [[-9], [0]],
]
