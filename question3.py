import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
import sys
from networkx.drawing.layout import spring_layout

import sknetwork as skn
from sklearn.metrics.cluster import normalized_mutual_info_score


## Initialisation des 11 graphes utilisés



caltech = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Caltech36.graphml"

graph_Caltech = nx.read_graphml(caltech)

print("ok")

mit = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/MIT8.graphml"

graph_MIT = nx.read_graphml(mit)

print("ok")

johns_Hopkins = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Johns Hopkins55.graphml"

graph_Johns_Hopkins = nx.read_graphml(johns_Hopkins)

print("ok")

american75 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/American75.graphml"

graph_american75 = nx.read_graphml(american75)

print("ok")

auburn71 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Auburn71.graphml"

graph_auburn71 = nx.read_graphml(auburn71)

print("ok")

brown11 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Brown11.graphml"

graph_brown11 = nx.read_graphml(brown11)

print("ok")

cornell5 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Cornell5.graphml"

graph_cornell5 = nx.read_graphml(cornell5)

print("ok")

duke14 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Duke14.graphml"

graph_duke14 = nx.read_graphml(duke14)

print("ok")

harvard1 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Harvard1.graphml"

graph_harvard1 = nx.read_graphml(harvard1)

print("ok")

howard90 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Howard90.graphml"

graph_howard90 = nx.read_graphml(howard90)

print("ok")

penn94 = "/Users/solyaneberge/TSP/NET4103/projet/Projet_NET4103/graphs/Penn94.graphml"

graph_penn94 = nx.read_graphml(penn94)

print("ok")

## Liste des graphes

graphs = [graph_Caltech, graph_MIT, graph_Johns_Hopkins, graph_american75, graph_auburn71, graph_brown11, graph_cornell5, graph_duke14, graph_harvard1, graph_howard90, graph_penn94]



## Test

#Attributs : student_fac, gender, major_index, second_major, dorm, year, high_school

G = graph_Caltech

print(G.nodes.data())

#print(nx.get_node_attributes(G, "gender"))


print(nx.attribute_assortativity_coefficient(G, "gender"))


## Question 3


def printAssortativityResult(X, Y, attribute):
    fig = plt.figure("Assortativity of " + attribute, figsize=(8, 8))
    print(fig)
    axgrid = fig.add_gridspec(5, 9)

    ax1 = fig.add_subplot(axgrid[3:, :4])
    ax1.scatter(X, Y)
    print("ok")
    ax1.set_title(attribute)
    ax1.set_ylabel(attribute + " assortativity")
    ax1.set_xlabel("Network size")
    ax1.set_xscale("log");
    ax1.axhline(y=0, color='black', linestyle='--')

    ax2 = fig.add_subplot(axgrid[3:, 5:])
    ax2.hist(Y)
    ax2.set_xlabel(attribute + " assortativity")
    ax2.axvline(x=0, color='black', linestyle='--')




def printAssortativities():
    sizes = []
    studentAss = [] #student_fac
    majorAss = [] #major_index
    vertexDegreeAss = []
    dormAss = [] #dorm

    for graph in graphs:
        print("ok")
        #graph = getGraph(univ[1])
        sizes.append(graph.size())
        #studentAss.append(nx.attribute_assortativity_coefficient(graph, "student_fac"))
        majorAss.append(nx.attribute_assortativity_coefficient(graph, "major_index"))
        #vertexDegreeAss.append(nx.degree_assortativity_coefficient(graph))
        #dormAss.append(nx.attribute_assortativity_coefficient(graph, "dorm"))

    #printAssortativityResult(sizes, studentAss, "student")
    printAssortativityResult(sizes, majorAss, "major")
    #printAssortativityResult(sizes, vertexDegreeAss, "degree")
    #printAssortativityResult(sizes, dormAss, "dorm")

printAssortativities()
plt.show()





## Initialisation

graph_size = []
assortativity_student_fac = []
assortativity_index_major = []
assortativity_vertex_degree = []
assortativity_dorm = []
assortativity_gender = []

G = graph_Caltech

nb = nx.number_of_nodes(G)
student_fac = nx.attribute_assortativity_coefficient(G, "student_fac")
index_major = nx.attribute_assortativity_coefficient(G, "major_index")
degree = nx.degree_assortativity_coefficient(G)
dorm = nx.attribute_assortativity_coefficient(G, "dorm")
gender = nx.attribute_assortativity_coefficient(G, "gender")

graph_size = graph_size + [nb]
assortativity_student_fac = assortativity_student_fac + [student_fac]
assortativity_index_major = assortativity_index_major + [index_major]
assortativity_vertex_degree = assortativity_vertex_degree + [degree]
assortativity_dorm = assortativity_dorm + [dorm]
assortativity_gender = assortativity_gender + [gender]

print(graph_size)

G = graph_MIT
nb = nx.number_of_nodes(G)
student_fac = nx.attribute_assortativity_coefficient(G, "student_fac")
index_major = nx.attribute_assortativity_coefficient(G, "major_index")
degree = nx.degree_assortativity_coefficient(G)
dorm = nx.attribute_assortativity_coefficient(G, "dorm")
gender = nx.attribute_assortativity_coefficient(G, "gender")

graph_size = graph_size + [nb]
assortativity_student_fac = assortativity_student_fac + [student_fac]
assortativity_index_major = assortativity_index_major + [index_major]
assortativity_vertex_degree = assortativity_vertex_degree + [degree]
assortativity_dorm = assortativity_dorm + [dorm]
assortativity_gender = assortativity_gender + [gender]

print(graph_size)

G = graph_Johns_Hopkins
nb = nx.number_of_nodes(G)
student_fac = nx.attribute_assortativity_coefficient(G, "student_fac")
index_major = nx.attribute_assortativity_coefficient(G, "major_index")
degree = nx.degree_assortativity_coefficient(G)
dorm = nx.attribute_assortativity_coefficient(G, "dorm")
gender = nx.attribute_assortativity_coefficient(G, "gender")

graph_size = graph_size + [nb]
assortativity_student_fac = assortativity_student_fac + [student_fac]
assortativity_index_major = assortativity_index_major + [index_major]
assortativity_vertex_degree = assortativity_vertex_degree + [degree]
assortativity_dorm = assortativity_dorm + [dorm]
assortativity_gender = assortativity_gender + [gender]

print(graph_size)

G = graph_american75
nb = nx.number_of_nodes(G)
student_fac = nx.attribute_assortativity_coefficient(G, "student_fac")
index_major = nx.attribute_assortativity_coefficient(G, "major_index")
degree = nx.degree_assortativity_coefficient(G)
dorm = nx.attribute_assortativity_coefficient(G, "dorm")
gender = nx.attribute_assortativity_coefficient(G, "gender")

graph_size = graph_size + [nb]
assortativity_student_fac = assortativity_student_fac + [student_fac]
assortativity_index_major = assortativity_index_major + [index_major]
assortativity_vertex_degree = assortativity_vertex_degree + [degree]
assortativity_dorm = assortativity_dorm + [dorm]
assortativity_gender = assortativity_gender + [gender]

print(graph_size)

G = graph_auburn71
nb = nx.number_of_nodes(G)
student_fac = nx.attribute_assortativity_coefficient(G, "student_fac")
index_major = nx.attribute_assortativity_coefficient(G, "major_index")
degree = nx.degree_assortativity_coefficient(G)
dorm = nx.attribute_assortativity_coefficient(G, "dorm")
gender = nx.attribute_assortativity_coefficient(G, "gender")

graph_size = graph_size + [nb]
assortativity_student_fac = assortativity_student_fac + [student_fac]
assortativity_index_major = assortativity_index_major + [index_major]
assortativity_vertex_degree = assortativity_vertex_degree + [degree]
assortativity_dorm = assortativity_dorm + [dorm]
assortativity_gender = assortativity_gender + [gender]

print(graph_size)

G = graph_brown11
nb = nx.number_of_nodes(G)
student_fac = nx.attribute_assortativity_coefficient(G, "student_fac")
index_major = nx.attribute_assortativity_coefficient(G, "major_index")
degree = nx.degree_assortativity_coefficient(G)
dorm = nx.attribute_assortativity_coefficient(G, "dorm")
gender = nx.attribute_assortativity_coefficient(G, "gender")

graph_size = graph_size + [nb]
assortativity_student_fac = assortativity_student_fac + [student_fac]
assortativity_index_major = assortativity_index_major + [index_major]
assortativity_vertex_degree = assortativity_vertex_degree + [degree]
assortativity_dorm = assortativity_dorm + [dorm]
assortativity_gender = assortativity_gender + [gender]

print(graph_size)

G = graph_cornell5
nb = nx.number_of_nodes(G)
student_fac = nx.attribute_assortativity_coefficient(G, "student_fac")
index_major = nx.attribute_assortativity_coefficient(G, "major_index")
degree = nx.degree_assortativity_coefficient(G)
dorm = nx.attribute_assortativity_coefficient(G, "dorm")
gender = nx.attribute_assortativity_coefficient(G, "gender")

graph_size = graph_size + [nb]
assortativity_student_fac = assortativity_student_fac + [student_fac]
assortativity_index_major = assortativity_index_major + [index_major]
assortativity_vertex_degree = assortativity_vertex_degree + [degree]
assortativity_dorm = assortativity_dorm + [dorm]
assortativity_gender = assortativity_gender + [gender]

print(graph_size)

G = graph_duke14
nb = nx.number_of_nodes(G)
student_fac = nx.attribute_assortativity_coefficient(G, "student_fac")
index_major = nx.attribute_assortativity_coefficient(G, "major_index")
degree = nx.degree_assortativity_coefficient(G)
dorm = nx.attribute_assortativity_coefficient(G, "dorm")
gender = nx.attribute_assortativity_coefficient(G, "gender")

graph_size = graph_size + [nb]
assortativity_student_fac = assortativity_student_fac + [student_fac]
assortativity_index_major = assortativity_index_major + [index_major]
assortativity_vertex_degree = assortativity_vertex_degree + [degree]
assortativity_dorm = assortativity_dorm + [dorm]
assortativity_gender = assortativity_gender + [gender]

print(graph_size)

G = graph_harvard1
nb = nx.number_of_nodes(G)
student_fac = nx.attribute_assortativity_coefficient(G, "student_fac")
index_major = nx.attribute_assortativity_coefficient(G, "major_index")
degree = nx.degree_assortativity_coefficient(G)
dorm = nx.attribute_assortativity_coefficient(G, "dorm")
gender = nx.attribute_assortativity_coefficient(G, "gender")

graph_size = graph_size + [nb]
assortativity_student_fac = assortativity_student_fac + [student_fac]
assortativity_index_major = assortativity_index_major + [index_major]
assortativity_vertex_degree = assortativity_vertex_degree + [degree]
assortativity_dorm = assortativity_dorm + [dorm]
assortativity_gender = assortativity_gender + [gender]

print(graph_size)

G = graph_howard90
nb = nx.number_of_nodes(G)
student_fac = nx.attribute_assortativity_coefficient(G, "student_fac")
index_major = nx.attribute_assortativity_coefficient(G, "major_index")
degree = nx.degree_assortativity_coefficient(G)
dorm = nx.attribute_assortativity_coefficient(G, "dorm")
gender = nx.attribute_assortativity_coefficient(G, "gender")

graph_size = graph_size + [nb]
assortativity_student_fac = assortativity_student_fac + [student_fac]
assortativity_index_major = assortativity_index_major + [index_major]
assortativity_vertex_degree = assortativity_vertex_degree + [degree]
assortativity_dorm = assortativity_dorm + [dorm]
assortativity_gender = assortativity_gender + [gender]

print(graph_size)

G = graph_penn94
nb = nx.number_of_nodes(G)
student_fac = nx.attribute_assortativity_coefficient(G, "student_fac")
index_major = nx.attribute_assortativity_coefficient(G, "major_index")
degree = nx.degree_assortativity_coefficient(G)
dorm = nx.attribute_assortativity_coefficient(G, "dorm")
gender = nx.attribute_assortativity_coefficient(G, "gender")

graph_size = graph_size + [nb]
assortativity_student_fac = assortativity_student_fac + [student_fac]
assortativity_index_major = assortativity_index_major + [index_major]
assortativity_vertex_degree = assortativity_vertex_degree + [degree]
assortativity_dorm = assortativity_dorm + [dorm]
assortativity_gender = assortativity_gender + [gender]

print(graph_size)
print(assortativity_student_fac)
print(assortativity_index_major)
print(assortativity_vertex_degree)
print(assortativity_dorm)
print(assortativity_gender)

size_sequence = sorted(graph_size, reverse=True)
# fac_sequence = sorted(assortativity_student_fac, reverse=True)
# major_sequence = sorted(assortativity_index_major, reverse=True)
# degree_sequence = sorted(assortativity_vertex_degree, reverse=True)
# dorm_sequence = sorted(assortativity_dorm, reverse=True)
# gender_sequence = sorted(assortativity_gender, reverse=True)
#
# print(size_sequence)
# print(fac_sequence)
# print(major_sequence)
# print(degree_sequence)
# print(dorm_sequence)
# print(gender_sequence)


## Dessin graphs



## Student_fac

fig = plt.figure("Student/faculty status and graph size", figsize=(8, 8))
# Create a gridspec for adding subplots of different sizes
axgrid = fig.add_gridspec(5, 4)

ax1 = fig.add_subplot(axgrid[0:, :8])
plt.plot(size_sequence, assortativity_student_fac, 'o', linestyle="None")
#ax1.plot(degree_sequence, "b-", marker="o")
ax1.set_title("Student/faculty status and graph size")
ax1.set_ylabel("Assortativity of student_fac")
ax1.set_xlabel("Size of graph")

#print(degree_sequence)

plt.show()

## Index_major

print(assortativity_index_major)

fig = plt.figure("Major and graph size", figsize=(8, 8))
# Create a gridspec for adding subplots of different sizes
axgrid = fig.add_gridspec(5, 4)

ax1 = fig.add_subplot(axgrid[0:, :8])
plt.plot(size_sequence, assortativity_index_major, 'o', linestyle="None")
#ax1.plot(degree_sequence, "b-", marker="o")
ax1.set_title("Major and graph size")
ax1.set_ylabel("Assortativity of index_major")
ax1.set_xlabel("Size of graph")

#print(degree_sequence)

plt.show()

## Vertex degree

fig = plt.figure("Vertex degree and graph size", figsize=(8, 8))
# Create a gridspec for adding subplots of different sizes
axgrid = fig.add_gridspec(5, 4)

ax1 = fig.add_subplot(axgrid[0:, :8])
plt.plot(size_sequence, assortativity_vertex_degree, 'o', linestyle="None")
#ax1.plot(degree_sequence, "b-", marker="o")
ax1.set_title("Vertex degree and graph size")
ax1.set_ylabel("Assortativity of degree")
ax1.set_xlabel("Size of graph")

#print(degree_sequence)

plt.show()


## Dorm

fig = plt.figure("Dorms and graph size", figsize=(8, 8))
# Create a gridspec for adding subplots of different sizes
axgrid = fig.add_gridspec(5, 4)

ax1 = fig.add_subplot(axgrid[0:, :8])
plt.plot(size_sequence, assortativity_dorm, 'o', linestyle="None")
#ax1.plot(degree_sequence, "b-", marker="o")
ax1.set_title("Dorms and graph size")
ax1.set_ylabel("Assortativity of dorm")
ax1.set_xlabel("Size of graph")

#print(degree_sequence)

plt.show()



## Gender

fig = plt.figure("Genders and graph size", figsize=(8, 8))
# Create a gridspec for adding subplots of different sizes
axgrid = fig.add_gridspec(5, 4)

ax1 = fig.add_subplot(axgrid[0:, :8])
plt.plot(size_sequence, assortativity_gender, 'o', linestyle="None")
#ax1.plot(degree_sequence, "b-", marker="o")
ax1.set_title("Genders and graph size")
ax1.set_ylabel("Assortativity of gender")
ax1.set_xlabel("Size of graph")

#print(degree_sequence)

plt.show()









