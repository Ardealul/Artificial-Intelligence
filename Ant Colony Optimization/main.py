import sys

from Ant import Ant
from Colony import Colony
from reading import readNet, readNetHard
import matplotlib.pyplot as plot


def menu():
    print("-----------------")
    print("1. easy1.txt")
    print("2. easy2.txt")
    print("3. easy3.txt")
    print("4. mediumF.txt")
    print("5. hardE.txt")
    print("6. berlin52.txt")
    print("0. exit")
    print("-----------------")


if __name__ == '__main__':
    net = {}
    while True:
        menu()
        command = input()
        if command == "1":
            net = readNet("files/easy1.txt")
        elif command == "2":
            net = readNet("files/easy2.txt")
        elif command == "3":
            net = readNet("files/easy3.txt")
        elif command == "4":
            net = readNet("files/mediumF.txt")
        elif command == "5":
            net = readNetHard("files/hardE.txt")
        elif command == "6":
            net = readNetHard("files/berlin52.txt")
        elif command == "0":
            break
        else:
            print("Invalid command")

        print(net)

        noNodes = net['noNodes']
        matrix = net['mat']
        params = {'colSize': 10, 'noIter': 150,
                  'noNodes': noNodes, 'matrix': matrix, 'alpha': 2, 'beta': 5, 'ro': 0.1, 'initPheromone': 1.0,
                  'q0': 0.5, 'noChanges': 2, 'minValue': 1, 'maxValue': 50}

        colony = Colony(params)

        bestSolution = Ant(params)
        bestSolution.distance = sys.maxsize

        for i in range(params['noIter']):
            colony.initialisation()
            colony.constructSolution()
            solution = colony.bestSolution()
            print("Best ant in generation: " + str(i) + " is: " + str(solution.solution) + " with cost: " + str(
                solution.distance))
            if solution.distance < bestSolution.distance:
                bestSolution = solution
            colony.pheromoneUpdate()
            # colony.dynamic()

        print("The legend ant is: " + str(bestSolution))

