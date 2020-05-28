class Repo:
    def __init__(self):
        self.__nrOrase = 0
        self.__harta = []
        self.__solutie = []
        self.__sursa = 0
        self.__destinatie = 0
        self.__cost = 0
        self.__loadFile()

    """
    functia citeste si initializeaza datele din fisier
    """
    def __loadFile(self):
        try:
            file = open("hard.txt", "r")
        except IOError:
            return []
        line = file.readline().strip()
        print("Nr de orase: " + line)
        self.__nrOrase = int(line)
        line = file.readline().strip()
        i = 0
        print("Harta este: ")
        while line != "" and i < self.__nrOrase:
            print(line)
            attrs = line.split(",")
            linie = []
            for a in attrs:
                linie.append(int(a))
            self.__harta.append(linie)
            line = file.readline().strip()
            i += 1
        if line != "":
            self.__sursa = int(line)
            print("Nodul sursa este: " + str(self.__sursa))
            line = file.readline().strip()
            self.__destinatie = int(line)
            print("Nodul destinatie este: " + str(self.__destinatie))
        else:
            self.__sursa = 1
            self.__destinatie = 1
        file.close()

    def load(self):
        self.__loadFile()

    """
    functia scrie in fisier:
        ->nr de orase aferente solutiei
        ->orasele aferente solutiei
        ->costul drumului intre orasele solutiei
    """
    def __storeToFile(self):
        file = open("hard_solution.txt", "a")
        file.write(str(len(self.__solutie) - 1))
        file.write("\n")
        file.write(str(self.__solutie))
        file.write("\n")
        file.write(str(self.__cost))
        file.write("\n")
        file.close()

    def store(self):
        self.__storeToFile()

    def getNrOrase(self):
        return self.__nrOrase

    def getHarta(self):
        return self.__harta

    def getSursa(self):
        return self.__sursa

    def getDestinatie(self):
        return self.__destinatie

    def getSolutie(self):
        return self.__solutie

    def setSolutie(self, solutie):
        self.__solutie = solutie

    def getCost(self):
        return self.__cost

    def setCost(self, cost):
        self.__cost = cost