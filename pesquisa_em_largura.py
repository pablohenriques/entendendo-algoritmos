from collections import deque


def pessoa_e_vendedor(nome):
    return nome[-1] == "m"


def pesquisa(ngrafo):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += ngrafo["voce"]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa not in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(f"{pessoa} é um(a) vendedor(a) de manga")
                return True
            else:
                fila_de_pesquisa += ngrafo[pessoa]
                verificadas.append(pessoa)
    return False


def init_grafo():
    grafo = {}
    grafo["voce"] = ["alice", "bob", "claire"]
    grafo["bob"] = ["anuj", "peggy"]
    grafo["alice"] = ["peggy"]
    grafo["claire"] = ["thom", "jonny"]
    grafo["anuj"] = []
    grafo["peggy"] = []
    grafo["thom"] = []
    grafo["jonny"] = []
    return grafo


if __name__ == '__main__':
    fgrafo = init_grafo()
    resultado = pesquisa(fgrafo)
