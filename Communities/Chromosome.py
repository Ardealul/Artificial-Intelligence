from random import randint
from utils import generateNewValue, randomNeighbourOfNode

class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.__repres = [0 for _ in range(problParam['noDim'])]

        for i in range(problParam['noDim']):
            self.__repres[i] = randomNeighbourOfNode(i + 1, self.__problParam['mat'])
        # print(self.__repres)

        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    # standard uniform cross-over
    def crossover(self, c):
        mask = [randint(0, 1) for _ in range(self.__problParam['noDim'])]
        offspring = [0 for _ in range(self.__problParam['noDim'])]
        for i in range(self.__problParam['noDim']):
            if mask[i] == 0:
                offspring[i] = self.repres[i]
            else:
                offspring[i] = c.__repres[i]
        result = Chromosome(c.__problParam)
        result.repres = offspring
        return result

    def mutation(self):
        pos = randint(0, len(self.__repres) - 1)
        # self.__repres[pos] = randint(self.__problParam['min'], self.__problParam['max'])
        # self.__repres[pos] = randomNeighbourOfNode(pos + 1, self.__problParam['mat'])
        self.__repres[pos] = randomNeighbourOfNode(self.__repres[pos], self.__problParam['mat'])

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness