import sys
class Service:
    def __init__(self, repo):
        self.__repo = repo

    def load(self):
        self.__repo.load()

    def store(self):
        self.__repo.store()

    def getRepo(self):
        return self.__repo

    """
    lista - list
    vizitate - list
    functia gaseste nodul nevizitat si de cost minim
    returneaza acest nod
    """
    def getMinim(self, lista, vizitate):
        minim = sys.maxsize
        pozitie = 0
        for i in range(0, len(lista)):
            if (i + 1) not in vizitate and lista[i] < minim and lista[i] != 0:
                pozitie = i
                minim = lista[i]
        return pozitie + 1

    """
    harta - matrix of integers
    sursa - integer
    destinatie - integer
    functia gaseste solutia drumului de cost minim de la sursa la destinatie
    folosind o metoda greedy
    """
    def generareSolutie(self, harta, sursa, destinatie):
        solutie = [sursa]
        vizitate = []
        curent = sursa
        while len(vizitate) != self.__repo.getNrOrase():
            pozitie = self.getMinim(harta[curent - 1], vizitate)
            self.getRepo().setCost(self.getRepo().getCost() + harta[curent - 1][pozitie - 1])
            vizitate.append(curent)
            curent = pozitie
            solutie.append(curent)
            if curent == destinatie:
                break
        print(len(solutie) - 1)
        print(solutie)
        print(self.getRepo().getCost())
        self.__repo.setSolutie(solutie)
