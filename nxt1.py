# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:57:51 2022

@author: Quantum Sage
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.barbell_graph(4,2) #no. of nodes in a community with how many nodes in between the communities
nx.draw(G) #multiple usage of same var will result in overwriting
plt.show() #creates a new network graph for next operations

G=nx.complete_graph(4) #all nodes are connected to itself and 4 is the no. of nodes
nx.draw(G)
plt.show()

G=nx.cycle_graph(5) #all nodes are connected to themselves in a circle and in this case a pentagon
nx.draw(G)
plt.show()

G=nx.ladder_graph(5) #draws a ladder like network
nx.draw(G)

L=nx.complete_graph(5)
nx.draw(L) #still results in drawing on the same graph even after using another variable

G=nx.path_graph(5)
nx.draw(G)
plt.show()

G=nx.star_graph(5)
nx.draw(G) #draws a star graph with 1 centre node and 5 disjoing nodes (no edges for em)
plt.show()

G=nx.wheel_graph(6)
nx.draw(G) #draws a wheel graph??
plt.show()

G=nx.random_graph(5,0.5) #generates a graph with no. of edges and probability of edge creation
nx.draw() #it draws edges randomly so... random graph!
plt.show()

