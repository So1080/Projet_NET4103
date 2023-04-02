from abc import ABC
from abc import abstractmethod
import networkx as nx
import numpy as np
#import progressbar
import math


## Initialisation des 11 graphes utilisés


#
# caltech = "../graphs/Caltech36.graphml"
#
# graph_Caltech = nx.read_graphml(caltech)
#
# print("ok")
#
# mit = "../graphs/MIT8.graphml"
#
# graph_MIT = nx.read_graphml(mit)
#
# print("ok")
#
# johns_Hopkins = "../graphs/Johns Hopkins55.graphml"
#
# graph_Johns_Hopkins = nx.read_graphml(johns_Hopkins)
#
# print("ok")
#
# american75 = "../graphs/American75.graphml"
#
# graph_american75 = nx.read_graphml(american75)
#
# print("ok")
#
auburn71 = "../graphs/Auburn71.graphml"

graph_auburn71 = nx.read_graphml(auburn71)

print("ok")
#
# brown11 = "../graphs/Brown11.graphml"
#
# graph_brown11 = nx.read_graphml(brown11)
#
# print("ok")
#
# cornell5 = "../graphs/Cornell5.graphml"
#
# graph_cornell5 = nx.read_graphml(cornell5)
#
# print("ok")
#
# duke14 = "../graphs/Duke14.graphml"
#
# graph_duke14 = nx.read_graphml(duke14)
#
# print("ok")
#
# harvard1 = "../graphs/Harvard1.graphml"
#
# graph_harvard1 = nx.read_graphml(harvard1)
#
# print("ok")
#
# howard90 = "../graphs/Howard90.graphml"
#
# graph_howard90 = nx.read_graphml(howard90)
#
# print("ok")
#
# penn94 = "../graphs/Penn94.graphml"
#
# graph_penn94 = nx.read_graphml(penn94)
#
# print("ok")

## Liste des graphes

graphs = [graph_Caltech, graph_MIT, graph_Johns_Hopkins, graph_american75, graph_auburn71, graph_brown11, graph_cornell5, graph_duke14, graph_harvard1, graph_howard90, graph_penn94]

## Initialisation



class LinkPrediction(ABC):
    def __init__(self, graph):
        """
        Constructor
        Parameters
        ----------
        graph : Networkx graph
        """
        self.graph = graph
        self.N = len(graph)

    def neighbors(self, v) :
        """
        Return the neighbors list of a node
        Parameters
        ----------
        v : int
        node id
        Return
        ------
        neighbors_list : python list
        """
        neighbors_list = self.graph.neighbors(v)
        return list(neighbors_list)

    #@abstractmethod
    def fit(self):
        raise NotImplementedError("Fit must be implemented")




class CommonNeighbors(LinkPrediction):
    def __init__(self, graph):
        super(CommonNeighbors, self).__init__(graph)

    def calc(self, nodes):
        xNeighbors = self.neighbors(nodes[0])
        yNeighbors = self.neighbors(nodes[1])
        return len(set(xNeighbors) & set(yNeighbors))


class Jacard(LinkPrediction):
    def __init__(self, graph):
        super(Jacard, self).__init__(graph)

    def calc(self, nodes):
        xNeighbors = self.neighbors(nodes[0])
        yNeighbors = self.neighbors(nodes[1])
        inter = len(set(xNeighbors) & set(yNeighbors))
        union = len(set(xNeighbors).union(set(yNeighbors)))
        return inter/union

class AdamicAdard(LinkPrediction):
    def __init__(self, graph):
        super(AdamicAdard, self).__init__(graph)

    def calc(self, nodes):
        xNeighbors = self.neighbors(nodes[0])
        yNeighbors = self.neighbors(nodes[1])
        inter = set(xNeighbors) & set(yNeighbors)
        res = 0
        for node in inter:
            res = res + 1/math.log(len(self.neighbors(node)))

        return res



## Execution


import random

def evaluate(graph, link):
    edges = list(graph.edges())
    nodes = list(graph.nodes())
    M = len(edges)
    F = [0.05, 0.1, 0.15, 0.2]

    res = []

    for f in F:
        removed = []
        m = math.floor(M * f)
        for i in range(m):
            removed.append(edges.pop(random.randrange(len(edges))))
        edgeLinks = []
        for x in nodes:
            for y in nodes:
                if(x!=y):
                    edgeLinks.append((x, y))
        edgeLinks.sort(key = link.calc, reverse = True)
        predicted = edgeLinks[:M]
        res.append(len(set(removed) & set(predicted))/m)
    print(res)
    print("")

def evaluateGraph(graph):



    print("Common Neighbors:")
    link = CommonNeighbors(graph)
    evaluate(graph, link)

    print("Jacard:")
    link = Jacard(graph)
    evaluate(graph, link)

    print("Adamic / Adard:")
    link = AdamicAdard(graph)
    evaluate(graph, link)

G = graph_auburn71

evaluateGraph(G)

