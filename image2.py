# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 22:02:42 2022

@author: Quantum Sage
"""

import numpy
from PIL import Image


"""
compressions:
0-31: 0
32-63: 1
64-95: 2
96-127: 3
128-159: 4
160-191: 5
192-223: 6
224-255: 7
"""




im=Image.open("new2.jpg")
pixelMap=im.load()
print(im.mode)
img=Image.new(im.mode,im.size)
pixelNew=img.load()

print(pixelMap[10,50])
for i in range(img.size[0]):
    for j in range(img.size[1]):
        s=int(str(pixelMap[i,j]))
        if(s>=0 and s<=31):
            pixelNew=0
        elif(s>=32 and s<=63):
            pixelNew=10
        elif(s>=64 and s<=95):
            pixelNew=20
        elif(s>=96 and s<=127):
            pixelNew=30
        elif(s>=128 and s<=159):
            pixelNew=40
        elif(s>=160 and s<=191):
            pixelNew=50
        elif(s>=192 and s<=223):
            pixelNew=60
        elif(s>=224 and s<=255):
            pixelNew=70
        pixelMap[i,j]=pixelNew
img=Image.fromarray(pixelMap)
img.save("modified.jpg")

    