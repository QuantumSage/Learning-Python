# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 00:25:12 2022

@author: Quantum Sage
"""

import math
import string
import numpy as np
import calendar

#Things Im finding out now:
    
#round is inbuilt function and doesnt need math library but obv floor needs the library
n=21.5678
print(round(n))

#also math.floor() rounds off the the lower digit but int() just truncates
n=-3.5
print(math.floor(n),int(n)) #it will return -4 and -3
    
r="Hey There!"
print(list(r)) #will print ['H', 'e', 'y', ' ', 'T', 'h', 'e', 'r', 'e', '!']

s=input() #input is always string!!!!!!!! so make sure to convert it to int before using for calc
st="010101010101"
print(st*2) #2x the string!

string = "abcd"     #string reversal
string = string[::-1]
print(string)

#lists if copied from another list directly, it will result in call by reference type thingie
#so if l=a (a being list) and l[0]=555 a[0] will also be 555
#to mitigate this:
a=[1,2,3,4,5,6]
l=a[:]
l[0]=555
print(l,a)

#int cant be converted to list and vice versa so string has to be the middle ground for conversion
l1=[1,2,3,4]
lc="".join(list(map(str,l1))) #map will return a datatype called map so make sure to use list() to covert it to list
print(lc[0]) #also map(datatype,iterable) pls make sure to remember that

#for the love of god pls remember index!!! (or dont loop works as well but its just better)
l=[[1,2,3,4]]*4 #clever way to duplicate items (also the bracket matters it shows it has 2 dimensions)

#friendly reminder to use a[:x] to obtain halves of the actual list 

n=3
print(n**3) #will return cube of 3 as ** means exponent 

a=["Practice","makes","man","perfect"] #Practice will take precedence cause its higher in ascii value
print(a.sort())

#range can take(2,11) for 2-10

print(abs(420.211)) #returns absolute value 
print(math.fabs(420.211)) #same as abs but returns floating points even if input is integer

print(a[-1]) #prints the last digit
a=a[:-1] #deletes the last element and if looped it will go into infinite loop

#conda list to see all the libraries available

#a.sort() and sorted(a) is quite the same but the diff is that sort works on a but sorted creates a copy

#also special characters come after 122

a1='b'
if(a1>='a' and a1<='z'): #apparently this fucking works lmao
    print('yes')
    
b=np.array([[1,2],[3,4]]) #axis=0 rowwise and 1=columnwise so here answer is 4,6
print(np.sum(b,axis=0))

l1=[[1,2,3],[4,5,6]]
l1=np.array(l1)
print(l1.T) #.T and l1.transpose() is fucking same

print(calendar.prcal(2022)) #prints pretty much the whole calendar

print(calendar.isleap(2022)) #leap year check
