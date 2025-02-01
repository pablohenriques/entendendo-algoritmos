import unittest


def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None


class TestPesquisaBinaria(unittest.TestCase):

    def test_lista_impar(self):
        lista = [1, 3, 5, 7, 9]
        resultado = pesquisa_binaria(lista, 7)
        assert resultado is not None
        assert resultado == 3

    def test_lista_par(self):
        lista = [1, 3, 5, 7, 9, 10]
        resultado = pesquisa_binaria(lista, 10)
        assert resultado is not None
        assert resultado == 5

    def test_lista_sem_numero(self):
        lista = [1, 3, 5, 7, 9, 10]
        resultado = pesquisa_binaria(lista, 11)
        assert resultado is None
