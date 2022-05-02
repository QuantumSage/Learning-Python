# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 22:36:55 2022

@author: Quantum Sage
"""
L = list(map(int, input().split()))
max=int(L[0])
for i in L:
  if(int(i)>max):
    max=int(i)
l1=[0]*(max+1)
for i in L:
  l1[i]=i
for i in range(len(l1)):
  print(l1[i],end=" ")
  
  
