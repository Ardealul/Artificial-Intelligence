import networkx as nx


# read from .txt
def readNet(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(" ")
        for j in range(n):
            mat[-1].append(int(elems[j]))
    net["mat"] = mat
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if (mat[i][j] == 1):
                d += 1
            if (j > i):
                noEdges += mat[i][j]
        degrees.append(d)
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    f.close()
    return net


# read from .gml
def readNetwokGml(fileName):
    net = {}
    graph = nx.readwrite.read_gml(fileName, label='id')
    net['graph'] = graph
    net['noNodes'] = len(graph.nodes)
    net['noEdges'] = len(graph.edges)
    degrees = []
    for node in graph.degree:
        degrees.append(node[1])
    net['degrees'] = degrees
    # print(net['degrees'])
    matrix = []
    # print(graph.adj)
    for edge in graph.adj:
        neighbours = graph.adj[edge]
        l = [0] * net['noNodes']
        for n in neighbours:
            nod = (list(graph.nodes())).index(n)
            l[nod] = 1
        matrix.append(l)
    net['mat'] = matrix
    net['firstNode'] = list(graph.nodes.keys())[0]
    net['lastNode'] = list(graph.nodes.keys())[-1]
    return net
