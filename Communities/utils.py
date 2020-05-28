import collections
from random import uniform, choice
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import warnings


def generateNewValue(lim1, lim2):
    return uniform(lim1, lim2)


def binToInt(x):
    val = 0
    # x.reverse()
    for bit in x:
        val = val * 2 + bit
    return val


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


def createPlot(net, communities):
    warnings.simplefilter('ignore')
    A = np.matrix(net["mat"])
    G = nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(6, 6))  # image is 8 x 8 inches
    nx.draw_networkx_nodes(G, pos, node_size=700, cmap=plt.cm.RdYlBu, node_color=communities)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.show(G)


# returneaza un vector in care fiecare pozitie(nod) are asociata comunitatea din care face parte, ex: [1 2 1 1 2 1]
def components(l):
    # print("chromosome: " + str(l))
    # [1 2 3 4 5 6]

    # [2 3 2 5 1 4] --> [1,2], [2,3], [4,5], [5,1], [6,4]
    # dfs
    def dfs(node):
        communities[node - 1] = count
        # print("communities: " + str(communities))
        visited.add(node)
        # print("visited: " + str(visited))
        for n in neighbour[node]:
            if n not in visited:
                dfs(n)

    # determinate the edges
    edges = []
    for i in range(0, len(l)):
        edges.append([i + 1, l[i]])

    # print("edges: " + str(edges))
    # finding number of connected components
    neighbour = collections.defaultdict(list)
    for e in edges:
        u, v = e[0], e[1]
        neighbour[u].append(v)
        neighbour[v].append(u)
    visited = set()
    count = 0
    communities = [0 for _ in range(0, len(l))]
    for i in range(1, len(l) + 1):
        if i not in visited:
            count += 1
            dfs(i)
    # print("final community: " + str(communities))
    return communities


# returneaza o lista de liste, listele fiind formate din toate nodurile unei comunitati
def determinateComponents(components):
    maxim = np.amax(np.array(components))
    result = []
    for i in range(1, maxim + 1):
        l = []
        for j in range(0, len(components)):
            if components[j] == i:
                l.append(j + 1)
        result.append(l)
    return result


def randomNeighbourOfNode(node, matrix):
    neighbours = []
    l = matrix[node - 1]
    for i in range(len(l)):
        if l[i] == 1:
            neighbours.append(i + 1)
    # print("neighbours: " + str(neighbours))
    if not neighbours:
        return node
    selected = choice(neighbours)
    # print("selected: " + str(selected))
    return selected
