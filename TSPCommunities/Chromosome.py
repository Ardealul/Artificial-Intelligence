from random import randint, seed, random
from utils import generateChromosome, generateNewValue


# permutation-based representation
class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam  # problParam has to store the number of nodes/cities
        self.__repres = generateChromosome(problParam['max'])
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

    def crossover(self, c):
        # order XO
        pos1 = randint(1, self.__problParam['noNodes'] - 1)
        pos2 = randint(1, self.__problParam['noNodes'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.__repres[pos1: pos2 + 1]  # [ : )
        for el in c.__repres[pos2 + 1:-1] + c.__repres[1:pos2 + 1]:  # here
            if el not in newrepres:
                if len(newrepres) < self.__problParam['noNodes'] - pos1:
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1
        new = [1] + newrepres + [1]
        offspring = Chromosome(self.__problParam)
        offspring.repres = new
        return offspring

    def mutation(self):
        # insert mutation
        pos1 = randint(1, self.__problParam['noNodes'] - 1)
        pos2 = randint(1, self.__problParam['noNodes'] - 1)
        self.__repres[pos1], self.__repres[pos2] = self.__repres[pos2], self.__repres[pos1]

    def mutationWithProbability(self, mutationProbability):
        # each gene it may or may not be swap with another one according to a probability
        for i in range(1, self.__problParam['noNodes']):
            probability = generateNewValue(0, 1)
            if probability < mutationProbability:
                pos = randint(1, self.__problParam['noNodes'] - 1)
                self.__repres[i], self.__repres[pos] = self.__repres[pos], self.__repres[i]

    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
