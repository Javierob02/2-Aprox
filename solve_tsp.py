from collections import namedtuple
import networkx as nx
import math
import matplotlib.pyplot as plt
import os

Point = namedtuple("Point", ['x', 'y'])


def length(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


def complete_graph(points):
    """ Creates a complete graph """
    graph = nx.Graph()
    for i in range(len(points)-1):
        graph.add_node(i)
        graph.add_edge(i, i+1, weight = length(points[i], points[i+1]))
    nx.draw(graph, with_labels=True)
    plt.show()

    return graph


def solve_2_approx(points):
    """ implements the Tree 2-approximate algorithm for TSP """
    g = []
    graph = complete_graph(points)
    arbol_minimo = nx.minimum_spanning_tree(graph)    #1. Exp. min
    multi_graph = nx.MultiGraph(arbol_minimo)       #2. Crear Multigrafo
    multi_graph.add_edges_from(arbol_minimo.edges())
    euler = nx.eulerian_circuit(multi_graph)      #3.Camino Euler

    for i in euler:
        if i[0] not in g:
            g.append(i[0])
    return g