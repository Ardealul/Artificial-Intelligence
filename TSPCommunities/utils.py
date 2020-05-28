from math import sqrt
from random import randint, uniform


def generateNewValue(lim1, lim2):
    return uniform(lim1, lim2)


def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']
    M = 2 * noEdges
    Q = 0.0
    for i in range(0, noNodes):
        for j in range(0, noNodes):
            if communities[i] == communities[j]:
                Q += (mat[i][j] - degrees[i] * degrees[j] / M)
    return Q * 1 / M


def generateChromosome(n):
    # n is the number of nodes in the graph
    res = [1 for _ in range(n + 1)]
    for i in range(1, len(res) - 1):
        ok = 0
        while ok == 0:
            x = randint(2, n)
            if x not in res:
                res[i] = x
                ok = 1
    return res


def fitnessOfChromosome(chromosome, matrix):
    res = 0
    for i in range(len(chromosome) - 1):
        res += matrix[chromosome[i] - 1][chromosome[i + 1] - 1]
    return res


def distanceBetweenTwoNodes(node1, node2):
    return sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)
