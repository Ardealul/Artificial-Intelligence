from random import uniform, randint

from Ant import Ant


class Colony:
    def __init__(self, params):
        self.__params = params
        self.__population = []
        self.__pheromoneMatrix = [[0.0 for _ in range(self.__params['noNodes'])] for _ in range(self.__params['noNodes'])]

    @property
    def population(self):
        return self.__population

    @property
    def pheromoneMatrix(self):
        return self.__pheromoneMatrix

    def initialisation(self):
        self.__population = []
        for _ in range(self.__params['colSize']):
            a = Ant(self.__params)
            self.__population.append(a)

    def constructSolution(self):
        for i in range(1, self.__params['noNodes']):
            for k in range(self.__params['colSize']):
                q = uniform(0, 1)
                if q <= self.__params['q0']:
                    neighbour = self.selectMostAtractive(k)
                else:
                    neighbour = self.selectMostAtractiveByWheel(k)
                # adding node to solution
                newSolution = self.__population[k].solution + [neighbour]
                self.__population[k].solution = newSolution
                # local pheromone update
                pos1 = self.population[k].solution[-2]
                pos2 = self.population[k].solution[-1]
                self.pheromoneMatrix[pos1 - 1][pos2 - 1] = (1.0 - self.__params['ro']) * self.pheromoneMatrix[pos1 - 1][pos2 - 1] + self.__params['ro'] * self.__params['initPheromone']
                self.pheromoneMatrix[pos2 - 1][pos1 - 1] = (1.0 - self.__params['ro']) * self.pheromoneMatrix[pos2 - 1][pos1 - 1] + self.__params['ro'] * self.__params['initPheromone']
                if i == self.__params['noNodes'] - 1:
                    first = self.population[k].solution[0]
                    last = self.population[k].solution[-1]
                    self.pheromoneMatrix[first - 1][last - 1] = (1.0 - self.__params['ro']) * self.pheromoneMatrix[first - 1][last - 1] + self.__params['ro'] * self.__params['initPheromone']
                    self.pheromoneMatrix[last - 1][first - 1] = (1.0 - self.__params['ro']) * self.pheromoneMatrix[last - 1][first - 1] + self.__params['ro'] * self.__params['initPheromone']

        for i in range(self.__params['colSize']):
            self.population[i].distance = self.calculateDistance(self.population[i].solution)

    def selectMostAtractive(self, k):
        neighbours = self.getUnvisitedNeighbours(k)
        node = self.population[k].solution[-1]
        argMax = 0.0
        chosen = neighbours[0]
        for i in neighbours:
            pheromonePerEdge = (self.pheromoneMatrix[i - 1][node - 1] ** self.__params['alpha']) * ((1.0 / self.__params['matrix'][i - 1][node - 1]) ** self.__params['beta'])
            if pheromonePerEdge > argMax:
                argMax = pheromonePerEdge
                chosen = i
        return chosen

    def selectMostAtractiveByWheel(self, k):
        neighbours = self.getUnvisitedNeighbours(k)
        node = self.population[k].solution[-1]
        sum = 0.0
        for i in neighbours:
            sum += (self.pheromoneMatrix[i - 1][node - 1] ** self.__params['alpha']) * ((1.0 / self.__params['matrix'][i - 1][node - 1]) ** self.__params['beta'])
        pick = uniform(0, sum)
        current = 0.0
        for i in neighbours:
            current += (self.pheromoneMatrix[i - 1][node - 1] ** self.__params['alpha']) * ((1.0 / self.__params['matrix'][i - 1][node - 1]) ** self.__params['beta'])
            if current > pick:
                return i
        return neighbours[0]

    def getUnvisitedNeighbours(self, k):
        node = self.population[k].solution[-1]
        neighbours = []
        for i in range(self.__params['noNodes']):
            if self.__params['matrix'][node - 1][i] != 0 and i + 1 not in self.__population[k].solution:
                neighbours.append(i + 1)
        return neighbours

    def pheromoneUpdate(self):
        ant = self.bestSolution().solution
        for i in range(len(ant) - 1):
            self.pheromoneMatrix[ant[i] - 1][ant[i + 1] - 1] = (1.0 - self.__params['ro']) * self.pheromoneMatrix[ant[i] - 1][ant[i + 1] - 1] + self.__params['ro'] * (1.0 / self.calculateDistance(self.bestSolution().solution))
            self.pheromoneMatrix[ant[i + 1] - 1][ant[i] - 1] = (1.0 - self.__params['ro']) * self.pheromoneMatrix[ant[i + 1] - 1][ant[i] - 1] + self.__params['ro'] * (1.0 / self.calculateDistance(self.bestSolution().solution))
        self.pheromoneMatrix[ant[0] - 1][ant[-1] - 1] = (1.0 - self.__params['ro']) * self.pheromoneMatrix[ant[0] - 1][ant[-1] - 1] + self.__params['ro'] * (1.0 / self.calculateDistance(self.bestSolution().solution))
        self.pheromoneMatrix[ant[-1] - 1][ant[0] - 1] = (1.0 - self.__params['ro']) * self.pheromoneMatrix[ant[-1] - 1][ant[0] - 1] + self.__params['ro'] * (1.0 / self.calculateDistance(self.bestSolution().solution))

    def pheromoneUpdateForEach(self, x):
        ant = x.solution
        for i in range(len(ant) - 1):
            self.pheromoneMatrix[ant[i] - 1][ant[i + 1] - 1] = (1.0 - self.__params['ro']) * self.pheromoneMatrix[ant[i] - 1][ant[i + 1] - 1] + self.__params['ro'] * (1.0 / self.calculateDistance(ant))
            self.pheromoneMatrix[ant[i + 1] - 1][ant[i] - 1] = (1.0 - self.__params['ro']) * self.pheromoneMatrix[ant[i + 1] - 1][ant[i] - 1] + self.__params['ro'] * (1.0 / self.calculateDistance(ant))

    def bestSolution(self):
        minim = self.population[0].distance
        index = 0
        for i in range(1, self.__params['colSize']):
            if self.population[i].distance < minim:
                minim = self.population[i].distance
                index = i
        return self.population[index]

    def calculateDistance(self, solution):
        distance = 0
        for i in range(len(solution) - 1):
            distance += self.__params['matrix'][solution[i] - 1][solution[i + 1] - 1]
        distance += self.__params['matrix'][solution[-1] - 1][solution[0] - 1]
        return distance

    def dynamic(self):
        for _ in range(self.__params['noChanges']):
            maxValue = self.__params['maxValue']
            minValue = self.__params['minValue']
            value = randint(minValue, maxValue)
            node1 = 0
            node2 = 0
            while node1 == node2:
                node1 = randint(0, self.__params['noNodes'] - 1)
                node2 = randint(0, self.__params['noNodes'] - 1)
            self.__params['matrix'][node1][node2] = value
            self.__params['matrix'][node2][node1] = value

            print("New cost of edge [" + str(node1) + "," + str(node2) + "] is: " + str(value))
