# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:09:05 2022

@author: Quantum Sage
"""

import matplotlib.pyplot as plt
import networkx as nx
import random
import operator
G=nx.gnp_random_graph(10,0.5,directed=True) #directed graph shows arrows
nx.draw(G,with_labels=True) #shows the label for each nodes (0-9 for this one cause 10 nodes)
plt.show()  #x is the random source node
x=random.choice([i for i in range(G.number_of_nodes())]) 
dict_counter={}
for i in range(G.number_of_nodes()):
    dict_counter[i]=0
dict_counter[i]=dict_counter[i]+1 #updating source node +1 (cause selected node also gets +1 along with subsequent selects)
for i in range(1000000):
    list_n=list(G.neighbors(x))
    if(len(list_n)==0): #checking if its a sink node (no outgoing edges)
        x=random.choice([i for i in range(G.number_of_nodes())])
        dict_counter[x]+=1
    else: #choosing from the list of neighbor nodes
        x=random.choice(list_n)
        dict_counter[x]+=1
p=nx.pagerank(G)
sp=sorted(p.items(),key=operator.itemgetter(1)) #1 for sorting based on values or 0 for based on keys
srw=sorted(dict_counter.items(),key=operator.itemgetter(1))
print(sp)
print(srw)
