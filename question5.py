from abc import ABC
from abc import abstractmethod
import networkx as nx
import numpy as np
#import progressbar
import math


## Initialisation des 11 graphes utilisés



caltech = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Caltech36.graphml"

graph_Caltech = nx.read_graphml(caltech)

print("ok")

# mit = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/MIT8.graphml"
#
# graph_MIT = nx.read_graphml(mit)
#
# print("ok")
#
# johns_Hopkins = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Johns Hopkins55.graphml"
#
# graph_Johns_Hopkins = nx.read_graphml(johns_Hopkins)
#
# print("ok")
#
# american75 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/American75.graphml"
#
# graph_american75 = nx.read_graphml(american75)
#
# print("ok")
#
# auburn71 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Auburn71.graphml"
#
# graph_auburn71 = nx.read_graphml(auburn71)
#
# print("ok")
#
# brown11 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Brown11.graphml"
#
# graph_brown11 = nx.read_graphml(brown11)
#
# print("ok")
#
# cornell5 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Cornell5.graphml"
#
# graph_cornell5 = nx.read_graphml(cornell5)
#
# print("ok")
#
# duke14 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Duke14.graphml"
#
# graph_duke14 = nx.read_graphml(duke14)
#
# print("ok")
#
# harvard1 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Harvard1.graphml"
#
# graph_harvard1 = nx.read_graphml(harvard1)
#
# print("ok")
#
# howard90 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Howard90.graphml"
#
# graph_howard90 = nx.read_graphml(howard90)
#
# print("ok")
#
# penn94 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Penn94.graphml"
#
# graph_penn94 = nx.read_graphml(penn94)
#
# print("ok")

## Liste des graphes

graphs = [graph_Caltech, graph_MIT, graph_Johns_Hopkins, graph_american75, graph_auburn71, graph_brown11, graph_cornell5, graph_duke14, graph_harvard1, graph_howard90, graph_penn94]


## Execution

import random

def labelProg(graph, attribute):
    graph_1 = graph
    nodes = list(graph.nodes())
    F = [0.1, 0.2, 0.3]
    M = len(nodes)

    res = []

    for f in F:
        m = math.floor(M * f)
        selectedNodes = []
        for i in range(m):
            rand = random.randint(0, M - 1)
            selectedNodes.append(str(rand))
            graph.nodes[str(rand)][attribute] = None
        changed = True
        n=0
        while(changed and n<1000):
            changed = False
            n = n+1
            for node in selectedNodes:
                attr = []
                for nei in list(graph.neighbors(node)):
                    attr.append(graph.nodes[str(nei)][attribute])
                mostFreq = max(set(attr), key = attr.count)
                if(mostFreq != None):
                    graph.nodes[node][attribute] = mostFreq
                    changed = True
        originGraph = graph
        countCorrect = 0
        for node in selectedNodes:
            if(graph.nodes[node][attribute] == originGraph.nodes[node][attribute]):
                countCorrect = countCorrect + 1
        res.append(countCorrect/m)
    print(attribute + " : " + str(res))



labelProg(graph_Caltech, "dorm")
labelProg(graph_Caltech, "major_index")
labelProg(graph_Caltech, "gender")

