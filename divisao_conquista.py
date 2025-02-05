import unittest


def soma_recursiva(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[-1] + soma_recursiva(arr[:-1])


def contagem_recursiva(lista):
    if len(lista) == 1:
        return 1
    else:
        return 1 + contagem_recursiva(lista[:-1])


def maior_valor_recursivo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        maior_valor = lista[-1]
        chamada = maior_valor_recursivo(lista[:-1])
        if chamada > maior_valor:
            maior_valor = chamada
        return maior_valor


def pesquisa_binaria_recursiva(lista, item, v=None):
    if v is None:
        baixo = 0
        alto = len(lista) - 1
        meio = (baixo + alto) // 2
    else:
        if v == len(lista) or v < 0:
            return None
        meio = v

    chute = lista[meio]

    if chute == item:
        return meio
    if chute > item:
        meio = meio - 1
        return pesquisa_binaria_recursiva(lista, item, v=meio)
    if chute < item:
        meio = meio + 1
        return pesquisa_binaria_recursiva(lista, item, v=meio)


class RecursaoFuncoesTest(unittest.TestCase):

    def test_soma_recursao(self):
        lista = [1, 2, 3]
        resultado = soma_recursiva(lista)
        assert resultado == 6

    def test_contagem_recursiva(self):
        lista = [1, 2, 3, 4, 5, 6]
        resultado = contagem_recursiva(lista)
        assert resultado == 6

    def test_maior_valor_recursivo(self):
        lista = [1, 2, 3, 100, 5]
        resultado = maior_valor_recursivo(lista)
        assert resultado == 100

    def test_pesquisa_binaria_recursiva(self):
        lista =  [2, 5, 7, 8, 11, 12]
        resultado = pesquisa_binaria_recursiva(lista, 15)
        assert resultado is None

    def test_pesquisa_binaria_recursiva_primeiro_numero_fora(self):
        lista = [2, 5, 7, 8, 11, 12, 15, 19, 100]
        resultado = pesquisa_binaria_recursiva(lista, 1)
        assert resultado is None

    def test_pesquisa_binaria_recursiva_ultimo_numero_fora(self):
        lista = [2, 5, 7, 8, 11, 12, 15, 19, 100]
        resultado = pesquisa_binaria_recursiva(lista, 101)
        assert resultado is None

    def test_pesquisa_binaria_recursiva_lista_par(self):
        lista = [2, 5, 7, 8, 11, 12]
        resultado = pesquisa_binaria_recursiva(lista, 8)
        assert resultado == 3


    def test_pesquisa_binaria_recursiva_lista_impar(self):
        lista = ['apple', 'banana', 'cherry', 'date', 'grape']
        resultado = pesquisa_binaria_recursiva(lista, 'date')
        assert resultado == 3
