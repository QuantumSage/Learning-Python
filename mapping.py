# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:26:53 2022

@author: Quantum Sage
"""

import scipy.misc
from PIL import Image
import numpy as np
import random

img=scipy.misc.read("pn.png")
count_pun=0
count_in=0
count=0
while(count<=10000):
    x=random.randint(0,300)
    y=random.randint(0,168)
    z=0
    if(img[x][y][z]==60):
        count_in=count_in+1
        count=count+1
    else:
        if(img[x][y][z]==80):
            count_pun=count_pun+1
            count+=1

area=count_pun/count_in*3287263
print(area)
