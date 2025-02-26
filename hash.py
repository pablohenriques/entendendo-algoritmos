votaram = {}


def verifica_eleitor(nome):
    if votaram.get(nome):
        print("Mande embora")
    else:
        votaram[nome]=True
        print("Deixe votar")


if __name__ == '__main__':
    verifica_eleitor("Tom")
    verifica_eleitor("Mike")
    verifica_eleitor("Mike")
 