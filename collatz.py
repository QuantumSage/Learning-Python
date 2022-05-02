# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 23:53:18 2022

@author: Quantum Sage
"""

import networkx as nx
import matplotlib.pyplot as plt

#Collatz Conjecture
G=nx.read_edgelist(r"location.txt", create_using=nx.DiGraph(), nodetype=int)
nx.draw(G,with_labels=True)
plt.show()
