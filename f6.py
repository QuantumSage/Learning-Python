# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:37:52 2022

@author: Quantum Sage
"""

import networkx as nx
import numpy

G=nx.read_edgelist("C:/Users/Quantum Sage/Desktop/python/facebook_combined.txt")
N=list(G.nodes())
spll=[]
for u in N:
    for v in N:
        if u!=v:
            l=nx.shortest_path_length(G,u,v)
            print("Shortest length between",u,"and",v,"is:",l)
            spll.append(l)
min_spl=min(spll)
max_spl=max(spll)
avg_spl=numpy.average(spll)
print("Minimum shortest path:",min_spl)
print("Maximum shortest path:",max_spl)
print("Average shortest path:",min_spl)