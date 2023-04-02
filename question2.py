import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
import sys
from networkx.drawing.layout import spring_layout

import sknetwork as skn
from sklearn.metrics.cluster import normalized_mutual_info_score


## Graphes utilisés

caltech = "../graphs/Caltech36.graphml"

graph_Caltech = nx.read_graphml(caltech)


mit = "../graphs/MIT8.graphml"

graph_MIT = nx.read_graphml(mit)



johns_Hopkins = "../graphs/Johns Hopkins55.graphml"

graph_Johns_Hopkins = nx.read_graphml(johns_Hopkins)

print("ok")

## Test

#Attributs : gender, dorm,

G = graph_Caltech

print(G.nodes.data())

print(nx.get_node_attributes(G, "major"))

## Question a






fig = plt.figure("Degree of graphs", figsize=(8, 8))
# Create a gridspec for adding subplots of different sizes
axgrid = fig.add_gridspec(5, 4)

G = graph_Caltech

degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
dmax = max(degree_sequence)

ax2 = fig.add_subplot(axgrid[1:3, 1:3])
ax2.bar(*np.unique(degree_sequence, return_counts=True))
ax2.set_title("Degree histogram Caltech")
ax2.set_xlabel("Degree")
ax2.set_ylabel("# of Nodes")



G = graph_MIT

degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
dmax = max(degree_sequence)

ax2 = fig.add_subplot(axgrid[3:, 2:])
ax2.bar(*np.unique(degree_sequence, return_counts=True))
ax2.set_title("Degree histogram MIT")
ax2.set_xlabel("Degree")
ax2.set_ylabel("# of Nodes")



G = graph_Johns_Hopkins

degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
dmax = max(degree_sequence)

ax2 = fig.add_subplot(axgrid[3:, :2])
ax2.bar(*np.unique(degree_sequence, return_counts=True))
ax2.set_title("Degree histogram Johns Hopkins")
ax2.set_xlabel("Degree")
ax2.set_ylabel("# of Nodes")

fig.tight_layout()
plt.show()


## Question b

G = graph_Caltech
print(nx.transitivity(G))
print(nx.average_clustering(G))
print(nx.density(G))


G = graph_MIT
print(nx.transitivity(G))
print(nx.average_clustering(G))
print(nx.density(G))

G = graph_Johns_Hopkins
print(nx.transitivity(G))
print(nx.average_clustering(G))
print(nx.density(G))


## Question c




G = graph_Caltech

degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
local_clust = nx.clustering(G)
cluster = list(local_clust.values())




fig = plt.figure("Degree of a random graph", figsize=(8, 8))
# Create a gridspec for adding subplots of different sizes
axgrid = fig.add_gridspec(5, 4)

ax1 = fig.add_subplot(axgrid[0:, :8])
plt.plot(degree_sequence, cluster, 'o', linestyle="None")
#ax1.plot(degree_sequence, "b-", marker="o")
ax1.set_title("Degree Rank Plot of Caltech students")
ax1.set_ylabel("Local clustering coefficient")
ax1.set_xlabel("Degree")

print(degree_sequence)

plt.show()





## Autres graphes

american75 = "../graphs/American75.graphml"

graph_american75 = nx.read_graphml(american75)

auburn71 = "../graphs/Auburn71.graphml"

graph_auburn71 = nx.read_graphml(auburn71)

brown11 = "../graphs/Brown11.graphml"

graph_brown11 = nx.read_graphml(brown11)

cornell5 = "../graphs/Cornell5.graphml"

graph_cornell5 = nx.read_graphml(cornell5)

duke14 = "../graphs/Duke14.graphml"

graph_duke14 = nx.read_graphml(duke14)

harvard1 = "../graphs/Harvard1.graphml"

graph_harvard1 = nx.read_graphml(harvard1)

howard90 = "../graphs/Howard90.graphml"

graph_howard90 = nx.read_graphml(howard90)

penn94 = "../graphs/Penn94.graphml"

graph_penn94 = nx.read_graphml(penn94)

reed98 = "../graphs/Reed98.graphml"

graph_reed98 = nx.read_graphml(caltech)



