# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 21:15:52 2022

@author: Quantum Sage
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
l=[1,2,3]
G.add_nodes_from(l) #same as the one down just more streamlined

"""
manually adding nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)

also G.clear() removes G's data
"""
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(2,3)
print(G.edges())
nx.draw(G)
plt.show()

G=nx.complete_graph(10) #displaying a complete graph
nx.draw(G)
plt.show()

G=nx.gnp_random_graph(10,0.5) #displaying a graph with 0.5/1 chance to add an edge between two nodes
print(G.edges())
nx.draw(G)
plt.show()

G=nx.barabasi_albert_graph(50,2) #scalefree graph where nodes with higher degree has more chance to get another edge with more iteration of nodes added
nx.draw(G)
plt.show()

nx.write_gexf(G,"C:/Users/Quantum Sage/Desktop/python/analysis1.gexf") #G being the graph object and the other being the path (if just the name, it will make the file in default directory)
