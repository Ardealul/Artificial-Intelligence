# read from a .txt in which i have the matrix of the graph
from math import sqrt
from utils import distanceBetweenTwoNodes


# read from a .txt in which i have the adjacent matrix
def readNet(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(",")
        for j in range(n):
            mat[-1].append(int(elems[j]))
    net['mat'] = mat
    f.close()
    return net


# read from a .txt in which i have the coordinates of each node
def readNetHard(fileName):
    f = open(fileName, "r")
    net = {}
    n = f.readline()
    while not n[0].isnumeric():
        n = f.readline()
    line = n.split(" ")
    coordinatesList = [[float(line[1]), float(line[2])]]
    n = f.readline()
    while n[0].isnumeric():
        line = n.split(" ")
        coordinatesList.append([float(line[1]), float(line[2])])
        n = f.readline()
    net['noNodes'] = len(coordinatesList)
    mat = []
    for i in range(net['noNodes']):
        line = [0 for _ in range(net['noNodes'])]
        for j in range(net['noNodes']):
            if i != j:
                distance = distanceBetweenTwoNodes(coordinatesList[i], coordinatesList[j])
                line[j] = distance
        mat.append(line)
    net['mat'] = mat
    return net






