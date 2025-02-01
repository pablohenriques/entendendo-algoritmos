import unittest


def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i

        return menor_indice


def ordenacao_por_selecao(arr: list):
    novo_arr = []

    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_arr.append(arr.pop(menor))

    return novo_arr


class TestOrdenacaoSelecao(unittest.TestCase):

    def test_ordenacao(self):
        lista = [5, 3, 6, 2, 10]
        resultado = ordenacao_por_selecao(lista)
        lista_esperada = [2, 3, 5, 6, 10]
        assert resultado == lista_esperada
