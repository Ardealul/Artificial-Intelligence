import collections
from random import randint

from networkx import Graph

import reading
import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import warnings

from GA import GA
from utils import modularity, generateNewValue, randomNeighbourOfNode, components, determinateComponents, createPlot
from reading import *


def main():
    """
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'songbirds.in')
    net = reading.readNet(filePath)
    """

    net = readNetwokGml("real/lesmserables/lesmiserables.gml")
    # print(net['mat'])

    MIN = 0
    MAX = net['noNodes']

    # initialise de GA parameters
    gaParam = {'popSize': 100, 'noGen': 100}
    # problem parameters
    problParam = {'min': MIN, 'max': MAX, 'function': modularity, 'network': net, 'noDim': MAX, 'noBits': 8,
                  'mat': net['mat']}

    ga = GA(gaParam, problParam)
    ga.initialisation()  # representation
    ga.evaluation()  # fitness
    print("Population: " + str(ga.population.__repr__()))

    for generation in range(gaParam['noGen']):
        # ga.oneGenerationElitism()
        # ga.oneGeneration()
        # ga.oneGenerationSteadyState()
        ga.oneGenerationSteadyState1()

        bestChromo = ga.bestChromosome()
        communities = components(bestChromo.repres)

        print('Community: ' + str(communities))
        print('Nr of communities: ' + str(np.amax(np.array(communities))))
        print('Best solution in generation ' + str(generation) + ' is: x = ' + str(
            bestChromo.repres) + ' with fitness = ' + str(bestChromo.fitness))

    bestChromo = ga.bestChromosome()
    communities = components(bestChromo.repres)
    print('-----------------------Final result-----------------------')
    print('Community: ' + str(components(bestChromo.repres)))
    print('Fitness: ' + str(bestChromo.fitness))
    print('Nr of communities: ' + str(np.amax(np.array(communities))))
    for l in determinateComponents(communities):
        print(l)

    createPlot(net, communities)

    # print(modularity(communities, net))
    # print(randint(0, 1))
    # print([randint(0, 1) for _ in range(0, 5)])


main()
