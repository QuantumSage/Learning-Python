# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:20:29 2022

@author: Quantum Sage
"""

import networkx as nx

U=nx.Graph() #undirected graph generated (further operations needed to shape it tho)
G=nx.DiGraph()
print(G.nodes()) #to view nodes present 
G.add_nodes_from([i for i in range(5)])
print(list(G.nodes()))
print(G.edges()) #prints the edges present but in this case no o/p cause empty
G.add_edges(1,2) #adds an edge between two nodes

print(G.out_edges()) #print outgoing edges for directed graph
print(G.in_edges()) #print incoming edges for directed graph

#in above two lines, both will show the same o/p but their real usecase lies when used for specific node

print(G.out_edges(1)) #prints outedges of the node 1 which is (1,2)
print(G.in_edges(1)) #prints nothing as there isnt any incoming edge




