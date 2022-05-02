# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 00:38:04 2022

@author: Quantum Sage
"""

roll=input()
print(roll.split('@')[0],roll.split("@")[1].split(".")[0],end="") 

"""
Bro treated the list returned by roll.split('@') as a complete list(duh) and got the [0]th element 
of the list which in this case the first half of the input. On the other hand same thing happened 
just he nested another split on it to get the half between @ and .

The main point to consider here is that you dont need a variable to do list operation, you just have
to get iterable returned to do op on it
"""

#simplified for the monke brain!
a = input()
b = a.split('.')

r = b[0].split('@')[0]
i = b[0].split('@')[1]

print(r, i)

