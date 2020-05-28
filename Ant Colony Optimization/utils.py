from math import sqrt


def distanceBetweenTwoNodes(node1, node2):
    return sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)