# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:41:52 2022

@author: Quantum Sage
"""

conv_f={'dollar':60, 'euro':91} #dollar/euro is key and the numbers are value
conv_f["gbp"]=110
print(conv_f)
print(conv_f.keys()) #print the keys
print(conv_f.values()) #print values
print(conv_f.items()) #print all the items in the dictionary
conv_f["yen"]=0.75
del conv_f["yen"]
list(conv_f) #returns keys as list