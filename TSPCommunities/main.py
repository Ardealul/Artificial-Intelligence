from random import randint

import reading
from Chromosome import Chromosome
from GA import GA
from utils import modularity, generateChromosome, fitnessOfChromosome, distanceBetweenTwoNodes

import os


def main():
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'mediumF.txt')

    fileName = filePath.split("\\")[-1]
    if fileName == "hardE.txt" or fileName == "berlin52.txt":
        net = reading.readNet2(filePath)
    else:
        net = reading.readNet(filePath)
    print(net)

    MIN = 0
    MAX = net['noNodes']

    # initialise de GA parameters
    gaParam = {'popSize': 100, 'noGen': 150}
    # problem parameters
    problParam = {'min': MIN, 'max': MAX, 'function': fitnessOfChromosome, 'network': net, 'noNodes': MAX,
                  'noBits': 8, 'mat': net['mat']}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    print("Population: " + str(ga.population.__repr__()))

    for generation in range(gaParam['noGen']):
        # ga.oneGeneration()
        # ga.oneGenerationElitism()
        # ga.oneGenerationSteadyState()
        ga.oneGenerationSteadyState1()

        bestChromo = ga.bestChromosome()

        print('Best solution in generation ' + str(generation) + ' is: x = ' + str(
            bestChromo.repres) + ' with fitness = ' + str(bestChromo.fitness))

    bestChromo = ga.bestChromosome()
    print('Best solution is: x = ' + str(bestChromo.repres) + '\nwith fitness = ' + str(bestChromo.fitness))


main()
