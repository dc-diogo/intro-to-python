import pytest


def fatorial(n):
    if n < 1:
        return 1
    else:
        return n * fatorial(n-1)  # chamada recursiva


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def busca_binaria(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista)-1

    if max < min:
        return False
    else:
        meio = min + (max-min)//2

    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio-1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio+1, max)
    else:
        return meio


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)


def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito

    if not lado_direito:
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])


@ pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])
def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado


@ pytest.mark.parametrize("entrada, resposta", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13)])
def testa_fibonacci(entrada, resposta):
    assert fibonacci(entrada) == resposta


lista = [10, 20, 30, 40, 50, 60]


@ pytest.mark.parametrize("lista, valor, esperado", [
    (lista, 10, 0),
    (lista, 20, 1),
    (lista, 30, 2),
    (lista, 40, 3),
    (lista, 50, 4),
    (lista, 60, 5),
    (lista, 70, False),
    (lista, 15, False),
    (lista, -10, False),
])
def testa_busca_binaria(lista, valor, esperado):
    assert busca_binaria(lista, valor) == esperado
