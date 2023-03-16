import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
import sys
from networkx.drawing.layout import spring_layout

import sknetwork as skn
from sklearn.metrics.cluster import normalized_mutual_info_score


## Graphes utilisés

caltech = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Caltech36.graphml"

graph_Caltech = nx.read_graphml(caltech)


mit = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/MIT8.graphml"

graph_MIT = nx.read_graphml(mit)



johns_Hopkins = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Johns Hopkins55.graphml"

graph_Johns_Hopkins = nx.read_graphml(johns_Hopkins)

print("ok")



## Question a

# fonction TP

# G = graph_Caltech
#
# degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# hist, bin_edges = np.histogram(degree_sequence, density=True)
#
# plt.semilogy(bin_edges[:-1], hist, 'o', ms=15)
# plt.xlabel(r"$k$, degree ")
# plt.ylabel(r"PDF")
# plt.ylim(1e-3, 1e-1)
# plt.xlim(-2,200)
# plt.title("Degree distribution")
#
#
# G = graph_MIT
#
# degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# hist, bin_edges = np.histogram(degree_sequence, density=True)
#
# plt.semilogy(bin_edges[:-1], hist, 'o', ms=15)
# plt.xlabel(r"$k$, degree ")
# plt.ylabel(r"PDF")
# plt.ylim(1e-3, 1e-1)
# plt.xlim(-2,200)
# plt.title("Degree distribution")
#
# G = graph_Johns_Hopkins
#
# degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# hist, bin_edges = np.histogram(degree_sequence, density=True)
#
# plt.semilogy(bin_edges[:-1], hist, 'o', ms=15)
# plt.xlabel(r"$k$, degree ")
# plt.ylabel(r"PDF")
# plt.ylim(1e-3, 1e-1)
# plt.xlim(-2,200)
# plt.title("Degree distribution")
#
# plt.show()



#fonction networkx




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

#transitivity
#average_clustering





## POUBELLE



# ax0 = fig.add_subplot(axgrid[0:3, :])
# Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
# pos = nx.spring_layout(Gcc, seed=10396953)
# nx.draw_networkx_nodes(Gcc, pos, ax=ax0, node_size=20)
# nx.draw_networkx_edges(Gcc, pos, ax=ax0, alpha=0.4)
# ax0.set_title("Connected components of G")
# ax0.set_axis_off()

# ax1 = fig.add_subplot(axgrid[3:, :2])
# ax1.plot(degree_sequence, "b-", marker="o")
# ax1.set_title("Degree Rank Plot")
# ax1.set_ylabel("Degree")
# ax1.set_xlabel("Rank")